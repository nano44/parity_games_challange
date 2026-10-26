#!/usr/bin/env python3
"""REFEREE-2 succ. 6 climb against P-N5-FBW. FIT=dirty (C^1O): dirty intervals inside level blocks (PL (b)/(c); NJB would be refuted),
then block sizes. FIT=fbw (general games, MODE=general): gates at Even fallbacks with l >= 0 and l = delta (FBW (a) tight), then Even
fallbacks. Every scored run fully checked; a violation is saved. Usage: fbw_climb.py steps seed out init.pg"""
import sys, os, random
from collections import Counter
import fbw_check as C
F = C.F; RC = F.RC
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-RE"))
from re_climb import mutate
def write_pg(g, path):
    with open(path, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
def gmutate(rng, g):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]; n = g.n; v = rng.randrange(n); r = rng.random()
    if r < 0.5:
        k = len(succ[v])
        if rng.random() < 0.5 and k > 1: succ[v].pop(rng.randrange(k))
        elif k < 3: succ[v].append(rng.randrange(n))
        else: succ[v][rng.randrange(k)] = rng.randrange(n)
    elif r < 0.8: prio[v] = rng.randrange(0, n + 1)
    else: owner[v] = 1 - owner[v]
    return RC.Game(prio, owner, succ)
FIT = os.environ.get("FIT", "dirty")
def score(rg, o, seed):
    g = F.to_lpg(rg); st = F.Stats(); st.ex = {}; rng = random.Random(seed)
    for r in range(4):
        s, t = F.start(g, rng, r > 0); C.check_run(g, s, t, st, f"c#{r}", o)
    c, m = st.c, st.mx
    if FIT == "dirty": f = 100 * c["PL_dirty_intervals"] + m["max_block_size"]
    else: f = 10 * c["FBW_tight_l>=0"] + c["even_fallbacks"]
    return f, st
steps, seed, out, init = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]
rng = random.Random(seed); g = RC.parse(open(init).read())
o = F.one_odd(F.to_lpg(g)) if FIT == "dirty" else None
best, st = score(g, o, seed); tot = Counter(); nv = 0
print("start", best, flush=True)
for i in range(steps):
    if FIT == "dirty":
        h = mutate(rng, g, o)
        if h is None: continue
        try: F.one_odd(F.to_lpg(h))
        except AssertionError: continue
    else: h = gmutate(rng, g)
    f, st = score(h, o, seed)
    for k, v in st.c.items(): tot[k] += v
    if st.c["VIOLATIONS"]:
        write_pg(h, f"{out}_VIOL_{i}.pg"); print("VIOLATION", st.viol[:5], flush=True); nv += 1; break
    if f >= best:
        g = h
        if f > best: best = f; write_pg(g, f"{out}_best.pg"); print(i, best, flush=True)
print("TOTALS", dict(tot)); print("RESULT", "FAIL" if nv else "OK", "violations", nv)
