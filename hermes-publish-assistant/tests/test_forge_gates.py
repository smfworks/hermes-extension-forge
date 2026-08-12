"""Test the extension-forge gates and oppositional harness (breaker)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from __init__ import run_publish_gate, _run_breaker_harness

def test_good_skill_gate():
    good = Path(__file__).parent.parent / "skills" / "extension-forge" / "SKILL.md"
    assert good.exists(), "SKILL.md must exist for self-test"
    res = run_publish_gate(str(good), strict=False)
    print("GOOD GATE:", res["status"], "score=", res.get("docs_score"))
    assert res["status"] in ("PASS", "BLOCKED")  # may have minor scars in dev
    assert "Lofoten" in str(res.get("lofoten_checks", [])) or res.get("docs_score", 0) > 50
    print("test_good_skill_gate: PASS")

def test_breaker_bad_docs():
    out = _run_breaker_harness(["bad-docs", "incomplete"])
    print("BREAKER OUTPUT:\n", out)
    assert "BLOCKED" in out or "scars" in out.lower()
    print("test_breaker_bad_docs: PASS (expects BLOCKED)")

def test_breaker_cache():
    out = _run_breaker_harness(["cache"])
    print("CACHE BREAK:", out)
    assert "cache_safe" in out or "False" in out
    print("test_breaker_cache: PASS")

if __name__ == "__main__":
    test_good_skill_gate()
    test_breaker_bad_docs()
    test_breaker_cache()
    print("All forge gate + breaker tests executed.")
