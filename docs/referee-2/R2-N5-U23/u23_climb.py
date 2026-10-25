#!/usr/bin/env python3
"""REFEREE-2 hill climb for P-N5-U23: non-event W-flat switches in U2 / U3 / U23 stretches, kind-A switches in event-free sub-runs
with no kind-B vertex (the L_B boundary case of (ii)), and tightness of (i)/(ii). Every scored run is fully checked by u23_check.
FIT=lit maximises the literal-(ii) excess in empty-kind-B sub-runs. Usage: u23_climb.py steps seed outprefix initial.pg"""
import sys, os, random
from collections import Counter
import u23_check as Z
U, RC = Z.U, Z.RC
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-RE"))
from re_climb import mutate
def write_pg(g, path):
    with open(path, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
def score(g, o, seed):
    st = RC.Stats(); st.mx = Counter(); rng = random.Random(seed)
    for r in range(4):
        s, t = U.br_start(g) if r == 0 else RC.rand_start(rng, g); Z.run_one(g, o, s, t, st, f"c#{r}")
    c, m = st.c, st.mx
    nonev = c["U2_wflat_switches"] + sum(v for k, v in c.items() if k.startswith("U3_switch_"))
    f = 50 * c["U2_wflat_switches"] + 10 * nonev + 20 * sum(v for k, v in c.items() if k.startswith("U3_subruns_kindB_empty"))
    if os.environ.get("FIT") == "lit":
        f = 100 * (m.get("U3_A_emptyB_max(step-(lam-3))", -10) + 10) + 30 * c.get("U3_(ii)_literal_fails_U23", 0) + 30 * c.get("U3_(ii)_literal_fails_U3", 0) + nonev
    return f, st
steps, seed, out, init = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]
rng = random.Random(seed); g = RC.parse(open(init).read()); o = U.one_odd(g)
best, st = score(g, o, seed); tot = Counter(); nv = 0
print("start", best, flush=True)
for i in range(steps):
    h = mutate(rng, g, o)
    if h is None: continue
    try: U.one_odd(h)
    except AssertionError: continue
    f, st = score(h, o, seed)
    for k, v in st.c.items(): tot[k] += v
    if st.c["VIOLATIONS"]:
        write_pg(h, f"{out}_VIOL_{i}.pg"); print("VIOLATION", st.viol[:5], flush=True); nv += 1; break
    if any(k.startswith("U3_(ii)_literal_fails") for k in st.c) and not os.path.exists(f"{out}_LIT.pg"):
        write_pg(h, f"{out}_LIT.pg"); print("LITERAL (ii) FAILS", st.examples.get("ii_literal"), flush=True)
    if f >= best:
        g = h
        if f > best:
            best = f; write_pg(g, f"{out}_best.pg")
            print(i, best, {k: v for k, v in st.c.items() if "switch" in k or "empty" in k or "literal" in k}, dict(st.mx), flush=True)
print("TOTALS", dict(tot)); print("RESULT", "FAIL" if nv else "OK", "violations", nv)
