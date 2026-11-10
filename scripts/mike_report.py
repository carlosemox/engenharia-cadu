#!/usr/bin/env python3
"""Read-only local Mike report. No model/network/job mutation or scheduler."""
import argparse
import json
import os
import stat
from pathlib import Path
import time


def read(path):
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(fd, 'rb') as stream:
        info = os.fstat(stream.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_size > 1024 * 1024:
            raise ValueError('record must be a bounded regular file')
        raw = stream.read(1024 * 1024 + 1)
        if len(raw) > 1024 * 1024:
            raise ValueError('oversized record')
        return json.loads(raw)



def report(state, now=None):
    now = time.time() if now is None else now
    state = Path(state)
    result = {'agent': 'Mike', 'at': now, 'heartbeat_status': 'UNKNOWN',
              'process_liveness': 'NOT_VERIFIED', 'counts': {}, 'receipts': 0,
              'observed_tokens': {'prompt': None, 'completion': None},
              'token_coverage': 'NONE', 'errors': [], 'scope': 'synthetic-only',
              'development_models_requested': {'start_complex': 'Astra 6', 'routine': '5.3 Luna'},
              'development_model_observed': None, 'accepted_count': None}
    try:
        heartbeat = read(state / 'heartbeat.json')
        if type(heartbeat['at']) not in (int, float) or heartbeat['status'] not in {'IDLE', 'RUNNING', 'STOPPED'}:
            raise ValueError('invalid heartbeat')
        age = now - heartbeat['at']
        result['heartbeat_age_seconds'] = age
        result['heartbeat_status'] = heartbeat['status'] if 0 <= age <= 30 else 'STALE'
        result['pid_observed'] = heartbeat.get('pid')
    except (OSError, ValueError, KeyError, TypeError):
        result['errors'].append('heartbeat_unavailable_or_invalid')
    totals = [0, 0]; covered = 0
    for path in sorted((state / 'receipts').glob('*.json')):
        try:
            item = read(path)
            status = item['status']
            if status not in {'RUNNING','REVIEW_REQUIRED','FAILED','CANCELLED','INTERRUPTED'}:
                raise ValueError('unknown receipt state')
            result['counts'][status] = result['counts'].get(status, 0) + 1
            result['receipts'] += 1
            tokens = item.get('tokens', {})
            values = [tokens.get('prompt_eval_count'), tokens.get('eval_count')]
            if all(type(v) is int and v >= 0 for v in values):
                totals = [a+b for a,b in zip(totals, values)]; covered += 1
        except (OSError, ValueError, KeyError, TypeError, AttributeError):
            result['errors'].append('receipt_unavailable_or_invalid')
    if covered:
        result['observed_tokens'] = dict(zip(['prompt','completion'], totals))
        result['token_coverage'] = 'COMPLETE' if covered == result['receipts'] and not result['errors'] else 'PARTIAL'
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('state', type=Path)
    print(json.dumps(report(parser.parse_args().state), ensure_ascii=False, indent=2))
