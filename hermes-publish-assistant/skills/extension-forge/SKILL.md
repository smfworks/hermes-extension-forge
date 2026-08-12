---
name: extension-forge
description: "Governed publish gates, docs standards, GitHub automation for skills/plugins, and oppositional review harness. Lofoten-inspired: sustainable craft (precision fishing, stockfish preservation of value), community review like village knowledge sharing in rorbu and seasonal assemblies. Prevents bloat, ensures quality 'catches' for the Hermes extension ecosystem."
version: 1.0.0
author: Extension Governance Forge Team (Lofoten Sprint 2026-08)
category: devops
tags: [hermes, plugins, skills, governance, publish, review, github, lofoten, quality-gates]
metadata:
  hermes:
    related_skills: [github, code-quality, release-quality-engineering, hermes-agent, hermes-desktop-plugins]
    ship_target: smfworks/hermes-plugin-extension-forge or hermes-publish-assistant
---

# Extension Forge — Governed Publishing for Hermes Skills & Plugins

**Lofoten Tie-in (Earned, Not Pasted):**  
In Lofoten, sustainable cod fishing ("skrei") and the ancient art of stockfish production ("tørrfisk") demand precision: the right fish at the right season, careful drying on racks (hjell) to preserve value without rot, shared village knowledge for weather, tides, and quality. Overfishing or sloppy cure ruins the catch and the commons. Community "dugnad" (collective work) and rorbu gatherings review the season's take.  

`extension-forge` brings the same: precision "fishing" for high-value extensions (no bloat, full evidence), sustainable preservation (versioned SKILL.md + portable packages), and village-style oppositional review before "export" (GitHub publish). Bad PRs = "rotten fish" rejected at the gate. Good ones become durable stockfish for the ecosystem.

## Why This Exists (From Assessment Gaps)
- Publishing gaps: No standard gates for skills/plugins; third-party as standalone repos (per AGENTS.md + charter).
- Governance: Lacks built-in oppositional harness or recovery metrics.
- Docs standards: Inconsistent frontmatter, missing pitfalls/examples/verification.
- GitHub automation: Manual; no CI for extension quality.
- Addresses: plugin maturity, testing/hardening, long-horizon durability via governed artifacts.

**Core Principle (Narrow Waist):** Extensions live at edges. Forge enforces quality without bloating core.

## 1. Publish Gates (Governed Checklists)
Run before `hermes skills publish` or `hermes plugins install` prep, and in CI.

### Skill Publish Gate (Mandatory)
1. **Docs Complete**: Full SKILL.md with:
   - YAML frontmatter (name, description, version, category, tags)
   - Sections: trigger/when-to-use, numbered steps, pitfalls, examples, verification.
   - Evidence kinds listed (test, git, cli, curl, screenshot, delegate).
2. **No Bloat / Sustainable**: <200 lines core prose unless justified; references/ for long data. Lofoten: only "dry" what preserves value.
3. **Cache-Safe & Prompt-Safe**: No mid-conversation mutation of system prompt or tools unless via approved hooks.
4. **Tests/Evidence**: At least 1 passing selftest or pytest. Oppositional note with ≥1 "scar" (known limitation).
5. **Lofoten Check**: Metaphor earned (real tie to craft/sustainability/community); no tourism paste.
6. **Install/Portable**: Works via `hermes skills install` or bundled in plugin package (plugin.json + skills/ layout).

**CLI Usage (via hermes-publish-assistant):**
```bash
hermes publish-assistant gate skill ./my-skill/SKILL.md --strict
# Returns: PASS | BLOCKED: <reasons> | receipts in .forge/
```

### Plugin Publish Gate
1. Standalone repo under smfworks/hermes-plugin-*
2. plugin.yaml or __init__.py with register(ctx)
3. Bundled skills/ (portable v1) or docs.
4. Python package or dir-installable; no core tree pollution.
5. Desktop pane optional via hermes-desktop-plugins for review UI.
6. Full test (pytest or selftest CLI green); oppositional harness run.
7. GitHub: .github/ with PR template, workflow for gates.

**Example Gate Command Output (Hardened):**
```
[extension-forge] Lofoten Gate v1.0
Fishing Precision: 4/4 checks (docs, no-bloat, cache, evidence)
Village Review: 2 scars noted, 1 hardened
Stockfish Preservation: Portable layout verified
GitHub Automation: workflow + PR template present
RESULT: PASS (sha: abc123) — ready for `hermes plugins install smfworks/hermes-publish-assistant`
```

## 2. Docs Standards (Templates + Enforcement)
### Required SKILL.md Frontmatter
```yaml
---
name: my-extension
description: "One-line. Lofoten: precision cure for [problem]."
version: 1.0.0
category: software-development
tags: [hermes, example]
---
```

### Required Body Sections (Enforced by Forge)
- **When to Use** / Trigger
- **Steps** (numbered, exact commands)
- **Pitfalls** (table or list with fixes; include cache, install, auth)
- **Examples** (copy-paste runnable + expected output)
- **Verification** (receipts: files, test runs, curl 200, gh outputs)
- **Lofoten Notes** (optional but encouraged for SMF content)

**Bad Example (Will Fail Gate — Incomplete Docs):**
Missing pitfalls + no verification → BLOCKED: "Lofoten stockfish test: no scars documented; cache safety unproven."

**Good Example Template** (see below in Examples).

Use `smf-writing-checklist` + this forge for prose.

## 3. GitHub Automation for Skills/Plugins
### Recommended Repo Layout (Standalone for Plugin)
```
hermes-plugin-extension-forge/
├── .github/
│   ├── workflows/
│   │   └── extension-forge-ci.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── skills/
│   └── extension-forge/
│       └── SKILL.md
├── plugin/
│   └── __init__.py   # or plugin.yaml + register
├── tests/
│   └── test_forge_gates.py
├── README.md
└── pyproject.toml (if packaged)
```

### .github/workflows/extension-forge-ci.yml (Example)
```yaml
name: Extension Forge CI
on: [pull_request]
jobs:
  forge-gates:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Setup Hermes (stub for CI)
      run: pip install hermes-agent  # or use container
    - name: Run Publish Gates
      run: |
        python -m hermes_publish_assistant gate --all .
        # or hermes publish-assistant gate ...
    - name: Oppositional Break Test
      run: python tests/break_harness.py --simulate bad-docs incomplete-cache
    - name: Docs Lint + Lofoten Check
      run: python -c "
from hermes_publish_assistant import lint_docs
assert lint_docs('skills/extension-forge/SKILL.md')
"
```

### PR Template
```
## Extension Forge Checklist (Lofoten Village Review)
- [ ] Docs complete per standards (frontmatter + pitfalls + examples + verification)
- [ ] Gates passed locally (`hermes publish-assistant gate ...`)
- [ ] Oppositional scars documented + hardened
- [ ] Sustainable: no bloat, cache-safe, standalone
- [ ] Lofoten tie earned (precision/sustainability/community)
- [ ] Tests green; receipts attached

**Breaking Change?** No / Yes (describe)
**Ship Target:** smfworks/...
```

Use `gh pr create` + labels `extension-forge`, `governed`.

## 4. Oppositional Review Harness
**Breaker Role (Maelstrom-inspired):** Simulate "bad catch" to harden.

**Harness Implementation (in hermes-publish-assistant):**
- Inject bad cases: missing frontmatter, cache-unsafe edits, incomplete docs, oversized bloat, no tests, forced Lofoten paste.
- Run gates → expect BLOCKED.
- Record "scar" + fix in same PR.
- Metrics: time-to-harden, false-pass rate.

**Break Scenarios (Tested Below):**
1. Bad PR: SKILL.md without "pitfalls" section → fails docs gate.
2. Cache issue: Skill that mutates tool list mid-session → fails cache-safe.
3. Incomplete: No verification receipts → BLOCKED.
4. Bloat: 5k line SKILL without references/ → "overfishing" flag.

**Harden Loop:**
Maker writes → Breaker breaks → Maker fixes scar → Re-run gate → Village (2nd reviewer) signs.

## 5. Examples
### Example 1: Using the Forge to Ship a Skill
```bash
# 1. Scaffold (via assistant)
hermes publish-assistant scaffold my-precision-skill --lofoten

# 2. Edit SKILL.md (follow template)

# 3. Run gate (local)
hermes publish-assistant gate skill ./my-precision-skill/SKILL.md

# 4. Bundle in plugin or publish
hermes skills publish ./my-precision-skill

# 5. GitHub ship prep
gh repo create smfworks/hermes-plugin-my-precision --public
git push ...
gh pr create --title "feat: my-precision-skill via extension-forge" --body "..."
```

### Example 2: Oppositional Test Run (Simulated in Receipts)
See test runs below.

### Example 3: Lofoten Village Review Note in SKILL
"Like Lofoten fishermen reviewing the day's skrei on the dock before salting: every extension must survive the breaker before it is 'stockfished' into the shared store."

## 6. hermes-publish-assistant Integration
This skill is bundled with the `hermes-publish-assistant` Python plugin (see plugin/ dir in repo).

The assistant provides:
- `hermes publish-assistant gate ...` (CLI entry via register)
- `hermes publish-assistant review` (terminal UI with rich tables for gates; Lofoten fishing metaphor progress: "Casting line... Hooked quality... Reeling in evidence")
- Prep helpers: scaffold, lint, bundle-for-portable, gh-automation-gen
- Desktop pane hook (if desktop plugin loaded): "Forge Review" pane showing gate status, scars, publish readiness (uses host.request + ctx.register)

**Fishing Precision Metaphor in UI:**
- Cast (scan docs)
- Hook (validate each gate)
- Reel (harden scars)
- Preserve (generate portable package + git tag prep)
- Share (PR + village sign-off)

## 7. Testing, Breaking, Hardening (Evidence)
See receipts/ and test runs in this sprint.

**Verification Requirements (DoD for this skill itself):**
- [x] Full SKILL.md with all sections
- [ ] Gate script passes on self
- [ ] Break tests produce expected BLOCKED
- [ ] GitHub templates present
- [ ] Lofoten integration earned (this section)
- Receipts: files, outputs, gh status

## Pitfalls
| Pitfall | Fix (Forge Rule) |
|---------|------------------|
| Treating this as tourism metaphor | Require concrete mapping: e.g. "hjell drying rack = versioned SKILL.md + references/" |
| Passing gate without oppositional run | Always run breaker lane; 0 scars = suspicious |
| Cache break in published skill | Gate explicitly checks for system-prompt or tool-mutating patterns |
| Plugin touches core | Reject; must be standalone per AGENTS |
| Docs-only "publish" without evidence | Block; require test/curl/gh/curl receipts |

## References & Ship
- Charter: smf-blog-tests/2026-08-12-lofoten-sprint/charter/CHARTER.md
- Assessment: JeffVault/reports/lofoten-hermes-challenge-assessment-2026-08-11.md
- Target: smfworks GitHub (hermes-publish-assistant or extension-forge skill)
- Blog: aiclearinghouse-site/content/blog/ + sprint/blog

**Next:** Run gates on self, break, harden, ship prep.
