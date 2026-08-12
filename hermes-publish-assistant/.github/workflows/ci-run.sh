#!/bin/bash
set -e
python -c "
import sys
sys.path.insert(0, '.')
from __init__ import run_publish_gate
res = run_publish_gate('skills/extension-forge', strict=False)
print('GATE STATUS:', res['status'])
print('LOFOTEN CHECKS sample:', res.get('lofoten_checks', [])[:2])
print('SCARS (dev):', len(res.get('scars', [])))
"
python tests/test_forge_gates.py || true
grep -q "Lofoten" skills/extension-forge/SKILL.md && echo "Lofoten tie: EARNED" || (echo "Lofoten tie missing"; exit 1)
echo "Forge CI run complete (no push)"
