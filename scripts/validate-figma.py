#!/usr/bin/env python3
"""Validate this collection's deliberately simple, single-file Figma format."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
expected = {p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md')}
files = sorted((ROOT / 'figma/skills').glob('*.md'))
errors = []
actual = {p.stem for p in files}
if actual != expected:
    errors.append(f'Coverage mismatch: missing={expected - actual}, extra={actual - expected}')
names = set()
for path in files:
    content = path.read_text()
    match = re.match(r'\A---\n(.*?)\n---\n(.+)', content, re.S)
    if not match:
        errors.append(f'{path.name}: missing frontmatter/body')
        continue
    fields = {}
    for line in match[1].splitlines():
        if ': ' not in line:
            errors.append(f'{path.name}: unsupported frontmatter line {line!r}')
            continue
        key, value = line.split(': ', 1)
        if key in fields:
            errors.append(f'{path.name}: duplicate {key}')
        fields[key] = value
    name = fields.get('name', '')
    if name != path.stem or len(name) > 64 or name in names:
        errors.append(f'{path.name}: invalid or duplicate name {name!r}')
    names.add(name)
    try:
        description = json.loads(fields.get('description', ''))
        if not isinstance(description, str) or not 10 <= len(description) <= 1024:
            raise ValueError('invalid description length/type')
    except (ValueError, TypeError):
        errors.append(f'{path.name}: description must be a quoted JSON-compatible YAML string')
    if fields.get('license') != 'MIT':
        errors.append(f'{path.name}: expected MIT license')
    body = match[2]
    if 'Copyright (c) 2026 Karl Koch' not in body or 'Permission is hereby granted' not in body:
        errors.append(f'{path.name}: missing standalone license notice')
    if path.stem == 'apple-native-ui' and 'Copyright (c) 2026 Bart Reardon' not in body:
        errors.append(f'{path.name}: missing macOS source attribution')
    # No local resources or tool-specific dependencies can survive a one-file upload.
    for target in re.findall(r'\]\(([^)]+)\)', body):
        if not target.startswith(('https://', 'http://', '#')):
            errors.append(f'{path.name}: local dependency {target}')
    if re.search(r'/Users/|mcp__|\.\./|references/|scripts/|assets/|\bSKILL\.md\b', body):
        errors.append(f'{path.name}: unsupported host or package dependency')
    if len(body.split()) > 1600:
        errors.append(f'{path.name}: exceeds collection editorial budget of 1600 words')
    print(f'{path.name}: {len(body.split())} body words')
if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'PASS: {len(files)} standalone editions; metadata, coverage, licenses and dependencies checked.')
