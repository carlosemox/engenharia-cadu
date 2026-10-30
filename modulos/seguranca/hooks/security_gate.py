#!/usr/bin/env python3
"""Validate scoped, current security receipts. No audit, scanner, network or executor.

Receipts and the expected policy digest must be supplied by a trusted caller.
Hashes detect mismatch; they do NOT authenticate who produced a receipt.
PASS means this receipt meets the configured gate, never 'the app is secure'.
"""
import argparse
import hashlib
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

MAX_BYTES = 2 * 1024 * 1024
ID = re.compile(r'^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$')
DIGEST = re.compile(r'^[0-9a-f]{64}$')


def policy_hash(policy):
    """Stable hash of JSON data, not a signature or an authorization token."""
    raw = json.dumps(policy, ensure_ascii=False, sort_keys=True,
                     separators=(',', ':'), allow_nan=False).encode('utf-8')
    return hashlib.sha256(raw).hexdigest()


def _unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate_json_key')
        result[key] = value
    return result


def read_json(path):
    path = Path(path)
    if path.is_symlink() or not path.is_file():
        raise ValueError('invalid_input_file')
    with path.open('rb') as source:
        raw = source.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError('input_too_large')
    def reject_constant(_):
        raise ValueError('non_finite_number')
    return json.loads(raw.decode('utf-8'), object_pairs_hook=_unique,
                      parse_constant=reject_constant)


def _text(value):
    return isinstance(value, str) and bool(value.strip()) and len(value) <= 4096


def _fresh(value, now, limit):
    if not isinstance(value, str):
        return False
    try:
        dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
        return dt.tzinfo is not None and 0 <= now - dt.timestamp() <= limit
    except (ValueError, TypeError, OverflowError):
        return False


def _unexpired(value, now):
    if not isinstance(value, str):
        return False
    try:
        dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
        return dt.tzinfo is not None and dt.timestamp() > now
    except (ValueError, TypeError, OverflowError):
        return False


def _record_ok(item, snapshot, now, limit):
    return (isinstance(item, dict) and item.get('status') == 'PASS'
            and item.get('snapshot') == snapshot
            and _text(item.get('evidence_ref'))
            and _fresh(item.get('completed_at'), now, limit))


def evaluate(policy, receipt, *, event, snapshot, now=None):
    """Pure decision function. Required missing/stale/skipped evidence blocks."""
    now = time.time() if now is None else now
    reasons = []
    def block(reason):
        if reason not in reasons:
            reasons.append(reason)
    def result():
        return {'schema_version': '1.0', 'decision': 'BLOCKED' if reasons else 'PASS',
                'reasons': reasons, 'receipt_validation_only': True,
                'application_security_certified': False}
    if not isinstance(policy, dict) or not isinstance(receipt, dict):
        block('invalid_document'); return result()
    if (policy.get('schema_version') != '1.0' or policy.get('template_only') is not False
            or policy.get('enabled') is not True or not _text(policy.get('project_id'))):
        block('inactive_or_invalid_policy'); return result()
    rules = policy.get('events')
    if not isinstance(rules, dict) or not isinstance(event, str) or event not in rules:
        block('event_not_configured'); return result()
    rule = rules[event]
    if not isinstance(rule, dict):
        block('invalid_event_rule'); return result()
    required, limit = rule.get('required_checks'), rule.get('max_age_seconds')
    if (not isinstance(required, list) or not 1 <= len(required) <= 256
        or any(not isinstance(x, str) or not ID.fullmatch(x) for x in required)
        or len(set(required)) != len(required)
        or type(limit) is not int or limit <= 0
        or type(rule.get('require_independent_review')) is not bool
        or type(rule.get('require_verified_backup')) is not bool):
        block('invalid_event_rule'); return result()
    if not _text(snapshot):
        block('missing_external_snapshot'); return result()
    if receipt.get('schema_version') != '1.0' or receipt.get('template_only') is not False:
        block('inactive_or_invalid_receipt')
    if receipt.get('project_id') != policy['project_id']:
        block('project_mismatch')
    if receipt.get('event') != event:
        block('event_mismatch')
    if receipt.get('snapshot') != snapshot:
        block('snapshot_mismatch')
    try:
        if receipt.get('policy_sha256') != policy_hash(policy):
            block('policy_mismatch')
    except (TypeError, ValueError):
        block('invalid_policy_data')
    if not _fresh(receipt.get('created_at'), now, limit):
        block('receipt_stale_or_invalid_time')
    checks = receipt.get('checks')
    if not isinstance(checks, list) or len(checks) > 512:
        block('invalid_checks'); return result()
    by_id = {}
    for check in checks:
        if (not isinstance(check, dict) or not isinstance(check.get('id'), str)
                or not ID.fullmatch(check['id'])):
            block('invalid_check_record'); continue
        if check['id'] in by_id:
            block('duplicate_check')
        by_id[check['id']] = check
    for check_id in required:
        if not _record_ok(by_id.get(check_id), snapshot, now, limit):
            block('required_check_not_current_pass:' + check_id)
    # A receipt covers the selected batch, not the entire repository. Future batches
    # stay in the handoff; required unresolved coverage within this batch blocks.
    if receipt.get('coverage_gaps') != []:
        block('coverage_gap_or_missing_coverage')
    findings = receipt.get('findings')
    if not isinstance(findings, list) or len(findings) > 10000:
        block('missing_or_invalid_finding_register'); return result()
    seen = set()
    for finding in findings:
        if not isinstance(finding, dict):
            block('invalid_finding'); continue
        fid = finding.get('id')
        if not isinstance(fid, str) or not ID.fullmatch(fid) or fid in seen:
            block('invalid_or_duplicate_finding_id')
        else:
            seen.add(fid)
        severity, confidence, status = (finding.get(k) for k in ('severity', 'confidence', 'status'))
        if (severity not in ['Critical', 'High', 'Medium', 'Low', 'Informational']
            or confidence not in ['Confirmed', 'Likely', 'Needs validation']
            or status not in ['Open', 'Fixed, verification pending', 'Verified', 'False positive', 'Accepted risk']
            or finding.get('priority') not in ['Emergency', 'Urgent', 'Normal', 'Deferred']):
            block('invalid_finding_classification'); continue
        if status == 'False positive':
            if not (_text(finding.get('reason')) and _text(finding.get('review_ref'))):
                block('false_positive_not_reviewed')
            continue
        if status == 'Verified':
            if not (_text(finding.get('verification_ref'))
                    and finding.get('verification_snapshot') == snapshot):
                block('fix_verification_missing_or_stale')
            continue
        if finding['priority'] == 'Emergency':
            block('emergency_open')
        if severity in ['Critical', 'High']:
            block('confirmed_severe_unresolved' if confidence == 'Confirmed' else 'triage_pending')
        if event == 'pre-release' and severity != 'Informational' and status != 'Accepted risk':
            block('release_finding_disposition_missing')
        if status == 'Accepted risk':
            ex = finding.get('exception')
            if not (isinstance(ex, dict) and _text(ex.get('owner'))
                    and _text(ex.get('approval_ref')) and _text(ex.get('reason'))
                    and _unexpired(ex.get('expires_at'), now)):
                block('risk_exception_missing_or_expired')
    if rule['require_independent_review']:
        review = receipt.get('review')
        if not (_record_ok(review, snapshot, now, limit)
                and _text(review.get('author_execution_id'))
                and _text(review.get('reviewer_execution_id'))
                and review['author_execution_id'] != review['reviewer_execution_id']):
            block('independent_review_missing_or_invalid')
    if rule['require_verified_backup']:
        backup = receipt.get('backup')
        if not (isinstance(backup, dict) and backup.get('status') == 'VERIFIED'
                and backup.get('snapshot') == snapshot and _text(backup.get('evidence_ref'))
                and isinstance(backup.get('archive_sha256'), str)
                and DIGEST.fullmatch(backup['archive_sha256'])):
            block('backup_missing_or_mismatched')
    return result()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--policy', required=True)
    parser.add_argument('--receipt', required=True)
    parser.add_argument('--event', required=True)
    parser.add_argument('--snapshot', required=True)
    parser.add_argument('--project-root')
    parser.add_argument('--expected-policy-sha256')
    args = parser.parse_args(argv)
    try:
        if not args.project_root or not args.expected_policy_sha256:
            raise ValueError('trusted_context_missing')
        root = Path(args.project_root).resolve(strict=True)
        if not root.is_dir():
            raise ValueError('invalid_root')
        # Keep trusted policy/receipt out of the source tree and publication.
        for name in (args.policy, args.receipt):
            if Path(name).resolve().is_relative_to(root):
                raise ValueError('private_artifact_inside_project')
        policy = read_json(args.policy)
        if policy_hash(policy) != args.expected_policy_sha256:
            raise ValueError('trusted_policy_mismatch')
        receipt = read_json(args.receipt)
        decision = evaluate(policy, receipt, event=args.event, snapshot=args.snapshot)
        print(json.dumps(decision, ensure_ascii=False, allow_nan=False))
        return 0 if decision['decision'] == 'PASS' else 1
    except (OSError, ValueError, TypeError, RecursionError):
        # Never echo file contents, exception text, secret values or private paths.
        print(json.dumps({'schema_version': '1.0', 'decision': 'BLOCKED',
                          'reasons': ['input_or_trusted_context_invalid'],
                          'receipt_validation_only': True}))
        return 2


if __name__ == '__main__':
    sys.exit(main())
