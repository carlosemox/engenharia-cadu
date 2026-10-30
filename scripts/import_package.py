#!/usr/bin/env python3
"""Import a reviewed ZIP after validating its digest, manifest and target paths.

No archive scripts are executed. Existing unrelated files are preserved.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import stat
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

MAX_BYTES = 20 * 1024 * 1024
MAX_FILES = 1000

def import_package(archive: Path, expected_sha256: str, root: Path, prefix: str) -> list[str]:
    if not re.fullmatch(r'[a-zA-Z0-9._-]+', prefix) or prefix in ('.', '..'):
        raise ValueError('Invalid repository prefix')
    if not re.fullmatch(r'[a-f0-9]{64}', expected_sha256):
        raise ValueError('Invalid SHA-256')
    if archive.stat().st_size > MAX_BYTES:
        raise ValueError('Archive exceeds size limit')
    if hashlib.sha256(archive.read_bytes()).hexdigest() != expected_sha256:
        raise ValueError('Archive SHA-256 mismatch')
    root = root.resolve()
    payload: dict[str, bytes] = {}
    with zipfile.ZipFile(archive) as z:
        infos = z.infolist()
        if len(infos) > MAX_FILES or sum(i.file_size for i in infos) > MAX_BYTES:
            raise ValueError('Archive expansion exceeds limit')
        for entry in infos:
            if entry.is_dir():
                continue
            parts = PurePosixPath(entry.filename).parts
            if (len(parts) < 2 or parts[0] != prefix or
                any(p in ('.', '..', '.git', '.github') for p in parts) or
                '\\' in entry.filename or any(ord(c) < 32 for c in entry.filename)):
                raise ValueError('Unsafe archive path')
            if stat.S_ISLNK(entry.external_attr >> 16):
                raise ValueError('Symlinks are not permitted')
            relative = '/'.join(parts[1:])
            if relative in payload or relative == 'scripts/import_package.py' or relative.startswith('tests/test_import_package'):
                raise ValueError('Duplicate or protected import path')
            target = root / relative
            if not target.resolve().is_relative_to(root):
                raise ValueError('Destination escapes repository')
            if any(p.is_symlink() for p in [target, *target.parents] if p != root):
                raise ValueError('Destination contains symlink')
            payload[relative] = z.read(entry)
    manifest_raw = payload.get('MANIFEST_SHA256.json')
    if manifest_raw is None:
        raise ValueError('Manifest missing')
    manifest = json.loads(manifest_raw)
    if not isinstance(manifest, dict) or set(manifest) != set(payload) - {'MANIFEST_SHA256.json'}:
        raise ValueError('Manifest coverage mismatch')
    for name, digest in manifest.items():
        if not isinstance(digest, str) or hashlib.sha256(payload[name]).hexdigest() != digest:
            raise ValueError('Manifest digest mismatch: ' + name)
    # Validate the whole package before writing any destination file.
    for name, contents in payload.items():
        target = root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        fd, temp = tempfile.mkstemp(prefix='.import-', dir=target.parent)
        try:
            with os.fdopen(fd, 'wb') as handle:
                handle.write(contents)
            os.chmod(temp, 0o644)
            os.replace(temp, target)
        finally:
            if os.path.exists(temp):
                os.unlink(temp)
    return sorted(payload)

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path, required=True)
    parser.add_argument('--sha256', required=True)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    parser.add_argument('--prefix', required=True)
    parser.add_argument('--paths-file', type=Path, required=True)
    args = parser.parse_args()
    paths = import_package(args.archive, args.sha256, args.root, args.prefix)
    args.paths_file.write_bytes(b''.join(name.encode('utf-8') + b'\0' for name in paths))
    print(json.dumps({'status': 'PASS', 'verified_files': len(paths), 'sha256': args.sha256}))

if __name__ == '__main__':
    main()
