#!/usr/bin/env python3
"""Box 25: Prop X lifted to Z := X ∪ Reach(o) (closed under successors). Check: the sequence of distinct (σ|Z, τ) along N5 on G
equals N5's run on G[Z] from the restricted start. Also reports |Y \\ Reach(o)| ("above" vertices).
Usage: propz.py --random N nmin nmax seed [--randstart] | propz.py game.pg [start]"""
from common import *
def reach(g, o):
    R = {o}; st = [o]
    while st:
        x = st.pop()
        for y in g.succ[x]:
            if y not in R: R.add(y); st.append(y)
    return R
def check(g, st, cnt):
    n = g.n; o = odd_choice(g); Y = split(g, o); Z = sorted(set(range(n)) - Y | reach(g, o))
    if len(Z) == n: cnt["Z_all"] += 1; return
    h, keep = subgame(g, Z); idx = {v: i for i, v in enumerate(keep)}
    seq = []
    for s, t in st:
        x = (tuple(s[v] for v in Z if g.owner[v] == 0), t[o])
        if not seq or seq[-1] != x: seq.append(x)
    s0, t0 = st[0]
    hst, _ = trace(h, ({idx[v]: idx[s0[v]] for v in Z if g.owner[v] == 0}, {idx[v]: idx[t0[v]] for v in Z if g.owner[v] == 1}), check=False)
    hseq = [(tuple(keep[s[idx[v]]] for v in Z if g.owner[v] == 0), keep[t[idx[o]]]) for s, t in hst]
    cnt["runs"] += 1; cnt["above_max"] = max(cnt["above_max"], n - len(Z))
    if hseq != seq: cnt["fail"] += 1
if __name__ == "__main__":
    RS = "--randstart" in sys.argv
    if RS: sys.argv.remove("--randstart")
    cnt = {"games": 0, "Z_all": 0, "runs": 0, "fail": 0, "above_max": 0}
    a = sys.argv[1:]
    if a[0] == "--random":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi)
            if g is None: continue
            start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            cnt["games"] += 1; st, _ = trace(g, start, check=False); check(g, st, cnt)
    else:
        g = load(a[0]); s0 = readstart(a[1]) if len(a) > 1 else None; st, _ = trace(g, s0); cnt["games"] += 1; check(g, st, cnt)
    print(cnt)
