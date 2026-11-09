#!/usr/bin/env python3
"""greedy: apply all units except KEEP; then greedy-add back units if the target is lost."""
import sys, os, json
sys.argv += []
from ablate37 import *
os.chdir(os.path.join(H, "../box36"))
diffs = [("del:" if m[0] not in mwm else "rev:") + m[0] for m in R["movers"] if m[0] not in mwm or m[2] != mwm[m[0]][2] or (len(m[2]) > 1 and m[3] != mwm[m[0]][3])] + ["gate"]
cur = [u for u in diffs]
def ev(units):
    G, Nd = build(units); r = measure(G); return qflips(G, Nd, r["rows"]), r["C"], r["T3"], G, Nd
q = ev(cur); print("all but br:", q[:3], "NM", q[3]["N"] + sum(map(len, q[3]["opts"])), "k", own36.kfvs(q[3], 1))
# greedy remove units from cur (i.e. un-apply) if needed to recover 34
for u in list(diffs):
    if q[0] >= 34: break
    t = [x for x in cur if x != u]; r = ev(t)
    if r[0] > q[0]: cur, q = t, r; print("keep", u, r[:3])
print("final applied units", len(cur), "kept edits:", [u for u in diffs if u not in cur], q[:3])
json.dump(q[4], open(os.environ["SP"] + "/core_named%s.json" % os.environ.get("TAG", ""), "w")); json.dump(q[3], open(os.environ["SP"] + "/core%s.json" % os.environ.get("TAG", ""), "w"))
