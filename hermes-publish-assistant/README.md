# hermes-publish-assistant

Lofoten Extension Governance Forge — Python plugin + bundled skill `extension-forge`.

## Install (standalone, per Hermes third-party policy)
```bash
# Future: hermes plugins install smfworks/hermes-publish-assistant
# Manual for now (sprint):
mkdir -p ~/.hermes/plugins/hermes-publish-assistant
cp -r ./* ~/.hermes/plugins/hermes-publish-assistant/
hermes plugins list
hermes plugins enable hermes-publish-assistant || true
```

## Usage
```bash
hermes publish-assistant gate ./skills/extension-forge --strict
hermes publish-assistant review .
hermes publish-assistant break bad-docs cache
hermes publish-assistant scaffold my-new-precision-skill
hermes publish-assistant gh
```

## What it enforces
- Governed publish gates (docs, sustainable, cache-safe, evidence)
- Docs standards (required sections + frontmatter)
- GitHub automation (CI + PR template)
- Oppositional review harness (breaker simulates bad PRs, expects scars + harden)
- Lofoten craft: precision "fishing", stockfish preservation, rorbu/village review

## Test / Harden
```bash
cd artifacts/hermes-publish-assistant
python tests/test_forge_gates.py
python -m __init__ gate skills/extension-forge
python -m __init__ break bad-docs
```

## Ship
- Target: smfworks GitHub (hermes-plugin-... or direct)
- Blog prep in aiclearinghouse-site
- Full receipts in sprint/receipts/

Lofoten: "The fish that survives the breaker and the hjell is the one that feeds the village all winter."
