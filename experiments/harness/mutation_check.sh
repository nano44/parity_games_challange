#!/usr/bin/env bash
# Plant faults in a temporary copy of the harness, hide Oink, and confirm that selftest.py FAILS for each one
# (REFEREE review claude/referee 5251a48). Not part of check.sh (takes ~1 min). Exit 1 if any fault goes unnoticed.
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
run() {  # name file python-expression-old python-expression-new expected-failing-step
  local name="$1" file="$2" old="$3" new="$4" step="$5"
  local T; T="$(mktemp -d)"; mkdir -p "$T/experiments"; cp -r "$HERE" "$T/experiments/harness"
  python3 - "$T/experiments/harness/$file" "$old" "$new" <<'PY'
import sys
p, old, new = sys.argv[1:4]; s = open(p).read()
assert s.count(old) == 1, f"pattern not unique in {p}: {old!r}"
open(p, "w").write(s.replace(old, new))
PY
  sed -i 's|^OINK = .*|OINK = "/nonexistent/oink"|' "$T/experiments/harness/solvers.py"   # no Oink
  local out; out="$(cd "$T/experiments/harness" && timeout 110 python3 -I selftest.py 2>/dev/null)"
  rm -rf "$T"
  if echo "$out" | grep -q "SELFTEST FAIL" && echo "$out" | grep -q "^$step\..*FAILURES\|FAIL: .*" ; then
    echo "caught   $name  -> $(echo "$out" | grep '^FAIL:' | head -1 | cut -c1-110)"
  else
    echo "MISSED   $name"; echo "$out" | tail -5; MISSED=1
  fi
}
MISSED=0
run "compare.py region check disabled"  compare.py 'if diff:' 'if False:' 4
run "verify.py cycle test removed"      verify.py  'if q % 2 != p:' 'if False:' 5
run "verify.py leave-region check off"  verify.py  'if win[s] != p:' 'if False:' 5
run "verify.py missing-strategy check"  verify.py  'if s is None:' 'if False:' 5
run "verify.py non-edge check off"      verify.py  'if s not in g.succ[v]:' 'if False:' 5
run "verify.py opponent-escape check"   verify.py  '            if out:' '            if False:' 5
# baseline: the unmodified copy must PASS without Oink
T="$(mktemp -d)"; mkdir -p "$T/experiments"; cp -r "$HERE" "$T/experiments/harness"
sed -i 's|^OINK = .*|OINK = "/nonexistent/oink"|' "$T/experiments/harness/solvers.py"
(cd "$T/experiments/harness" && timeout 110 python3 -I selftest.py 2>/dev/null | grep -q "SELFTEST PASS") && echo "baseline (no faults, no Oink): PASS" || { echo "baseline FAILED"; MISSED=1; }
rm -rf "$T"
exit $MISSED
