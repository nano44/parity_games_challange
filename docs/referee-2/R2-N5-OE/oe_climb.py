#!/usr/bin/env python3
"""REFEREE-2 succ. 6 hill climb against P-N5-OE. FIT=noh1: relevant sigma-bar(o) changes off crossings under not-H1 (Lemma OE step 4);
FIT=off: relevant sigma-bar(o) changes off crossings (any case); FIT=jx: max(J - X) per phase, then J (Corollary OX (ii)).
Every scored run (S3 start + 3 random starts) is fully checked by oe_check; a violation is saved and stops the climb.
Usage: oe_climb.py steps seed outprefix initial.pg"""
import sys, os, random
from collections import Counter
import oe_check as C
F = C.F; RC = F.RC
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-RE"))
from re_climb import mutate
def write_pg(g, path):
    with open(path, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
def score(rg, o, seed):
    g = F.to_lpg(rg); st = F.Stats(); st.ex = {}; rng = random.Random(seed)
    for r in range(4):
        s, t = F.start(g, rng, r > 0); C.check_run(g, s, t, st, f"c#{r}", o)
    m, c = st.mx, st.c; fit = os.environ.get("FIT", "off")
    if fit == "noh1": f = 10 * c["S4_checks_offcross"] + c["S4_checks(not H1 at k)"]
    elif fit == "jx": f = 100 * (m.get("max(J-X)+1000", 0) - 1000) + m["max_J"]
    else: f = c["OE_relevant_sbar(o)_changes(no crossing)"]
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
        if f > best:
            best = f; write_pg(g, f"{out}_best.pg"); print(i, best, flush=True)
print("TOTALS", dict(tot)); print("RESULT", "FAIL" if nv else "OK", "violations", nv)
