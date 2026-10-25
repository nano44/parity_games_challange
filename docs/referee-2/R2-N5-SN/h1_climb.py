#!/usr/bin/env python3
"""REFEREE-2 succ. 6 climb against fixes §2b: FIT=drop maximises in-phase H1 -> notH1 transitions (H1-DROP), FIT=om1 maximises H1
eps-transitions with O = -1 (the case H1-KEEP excludes), then H1 eps. Every scored run fully checked by h1_check; violation saved.
Usage: h1_climb.py steps seed out init.pg"""
import sys, os, random
from collections import Counter
import h1_check as H
F = H.F; RC = F.RC
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-RE"))
from re_climb import mutate
from sn_climb import write_pg
def score(rg, o, seed):
    g = F.to_lpg(rg); st = F.Stats(); st.ex = {}; rng = random.Random(seed)
    for r in range(4):
        s, t = F.start(g, rng, r > 0); H.check_run(g, s, t, st, f"c#{r}", o)
    c = st.c
    if os.environ.get("FIT", "drop") == "drop": f = 10 * c["DROP_transitions(H1 -> notH1 in phase)"] + c["DROP_divergences"]
    else: f = 100 * c["H1_eps_with_O=-1"] + c["H1_eps"]
    return f, st
steps, seed, out, init = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]
rng = random.Random(seed); g = RC.parse(open(init).read()); o = F.one_odd(F.to_lpg(g))
best, st = score(g, o, seed); tot = Counter(); nv = 0
print("start", best, flush=True)
for i in range(steps):
    h = mutate(rng, g, o)
    if h is None: continue
    try: F.one_odd(F.to_lpg(h))
    except AssertionError: continue
    f, st = score(h, o, seed)
    for k, v in st.c.items(): tot[k] += v
    if st.c["VIOLATIONS"]:
        write_pg(h, f"{out}_VIOL_{i}.pg"); print("VIOLATION", st.viol[:5], flush=True); nv += 1; break
    if f >= best:
        g = h
        if f > best: best = f; write_pg(g, f"{out}_best.pg"); print(i, best, flush=True)
print("TOTALS", dict(tot)); print("RESULT", "FAIL" if nv else "OK", "violations", nv)
