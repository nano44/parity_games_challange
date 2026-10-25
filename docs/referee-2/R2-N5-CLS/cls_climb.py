#!/usr/bin/env python3
"""REFEREE-2 succ. 6 hill climb against P-N5-CLS. FIT=gt: CLS1 case r > L (weighted) + in-scope THR fallbacks; FIT=nl: NL (j, L) checks
with R nonempty + leaves at S4a (h) transitions. Every scored run (S3 start + 3 random starts) is fully checked by cls_check; a violation
is saved and stops the climb. Usage: cls_climb.py steps seed outprefix initial.pg"""
import sys, os, random
from collections import Counter
import cls_check as C
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
        s, t = F.start(g, rng, r > 0); C.check_run(g, s, t, st, f"c#{r}", o, rng)
    c = st.c; fit = os.environ.get("FIT", "gt")
    if fit == "gt": f = 20 * c["CLS1_case_r>L"] + 3 * c["CLS1_checks"] + c["scope_fallbacks_THR_u*!=none"]
    else: f = c["NL_admissible_with_R_nonempty"] + c["NL_no_admissible_L_with_leave"]
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
