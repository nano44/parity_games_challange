#!/bin/bash
# box 41 item 1: deep41 on the 26 frozen instances (box40/inst = L-RED r232/inst, SHA1SUMS) vs L-SI box 100 out/cross100_inst.out
# (claude/l-si 23d39400, copied to inst/cross100_inst.out.lsi); control CTRL=1 on 3 instances.
cd "$(dirname "$0")"
python3 deep41.py $(awk '$1 ~ /json/ {print "../box40/inst/"$1}' inst/cross100_inst.out.lsi) > out/deep41_inst26.out 2>&1; echo "run exit $?"
CTRL=1 python3 deep41.py ../box40/inst/MWR4_2.json ../box40/inst/C6G8_n54.json ../box40/inst/DHIB26_2804.json > out/deep41_ctrl.out 2>&1; echo "ctrl exit $?"
python3 - <<'PY'
import json, ast
L = {}
for l in open("inst/cross100_inst.out.lsi"):
    w = l.split()
    if w and w[0].endswith(".json"): L[w[0]] = (int(w[2]), ast.literal_eval(l[l.index("{"):]))
mm = 0; tot = dict(deep=0, DeepInt=0); dm = -1
for l in open("out/deep41_inst26.out"):
    w = l.split(); r = json.loads(l[l.index("{"):]); T, a = L[w[0]]
    keys = ("deep", "dmax", "qflip", "qint", "gates", "unm", "multi", "maxfl")
    bad = [k for k in keys if r[k] != a[k]] + (["T3"] if r["T3"] != T else [])
    tot["deep"] += r["deep"]; tot["DeepInt"] += r["DeepInt"]; dm = max(dm, r["dmax"])
    if bad: mm += 1; print("MISMATCH", w[0], {k: (r.get(k), a.get(k, T)) for k in bad})
print("compared", len(L), "mismatching genomes", mm, "| mine: deep total", tot["deep"], "dmax", dm, "DeepInt total", tot["DeepInt"])
PY
