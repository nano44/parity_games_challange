#!/bin/bash
# box 40 item 1: scc40 on L-SI's 26 frozen instances (copied from claude/l-red 59daaef2 experiments/red/r232/inst, SHA1SUMS), compare with
# L-SI's out/inst99.out (claude/l-si f65e0fb9, copied to inst/inst99.out.lsi); control CTRL=1 (direct successors) on MW8_2, FW8_2.
cd "$(dirname "$0")"
python3 scc40.py $(awk 'NR>1 && $1 ~ /json/ {print "inst/"$1}' inst/inst99.out.lsi) > out/scc40_inst26.out 2>&1; echo "run exit $?"
CTRL=1 python3 scc40.py inst/MW8_2.json inst/FW8_2.json > out/scc40_ctrl.out 2>&1; echo "ctrl exit $?"
python3 - <<'PY'
import json
L = {l.split()[0]: l.split() for l in open("inst/inst99.out.lsi") if l.split()[0].endswith(".json")}
mm = 0
for l in open("out/scc40_inst26.out"):
    w = l.split(); r = json.loads(l[l.index("{"):]); a = L[w[0]]
    mine = [w[2], w[4], r["T3"], r["nscc"], r["big"], r["maxloc"], r["ratio"], r["locfail"], r["chainfail"]]
    theirs = [a[1], a[2], int(a[3]), int(a[4]), int(a[5]), int(a[6]), float(a[7]), int(a[8]), int(a[9])]
    ok = [str(x) == str(y) if i < 2 else x == y for i, (x, y) in enumerate(zip(mine, theirs))]
    if not all(ok): mm += 1; print("MISMATCH", w[0], "mine", mine, "lsi", theirs)
print("compared", len(L), "mismatches", mm)
PY
