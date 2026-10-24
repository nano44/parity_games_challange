#!/usr/bin/env python3
"""Box 25 (settles REFEREE-2 N-3 vs P-N5-1OA §6): P-N5-1OA Lemma 1 on o-CYCLIC C^1O games.
At every state k whose transition k -> k+1 keeps σ|X and τ ("pure"), check that Ξ_k restricted to X equals the OPTIMAL valuation
of the one-player game G[X] (X = vertices with no path to o). Also check Prop X: distinct σ|X values along the run = N5's run on G[X].
Usage: lemma1cyc.py --random N nmin nmax seed [--randstart] | lemma1cyc.py game.pg [start]"""
from common import *
ALL = False
def check(g, st, cnt):
    n = g.n; o = odd_choice(g); Y = split(g, o); Xl = sorted(v for v in range(n) if v not in Y)
    if not Xl: cnt["X_empty"] += 1; return
    E = Engine(g); h, keep = subgame(g, Xl); idx = {v: i for i, v in enumerate(keep)}
    Eh, opt = opt_one_player(h)
    XE = [v for v in Xl if g.owner[v] == 0]
    for k in range(len(st) - 1):
        pure = all(st[k + 1][0][v] == st[k][0][v] for v in XE) and st[k + 1][1] == st[k][1]
        if not pure and not ALL: continue
        cnt["pure"] += 1; Xi, _ = E.evaluate(st[k][0])
        for v in Xl:
            a = vset(E, Xi[v]); b = vset(Eh, opt[idx[v]]); b = (keep[b[0]], frozenset(keep[u] for u in b[1]), b[2])
            if a != b: cnt["L1_fail"] += 1; break
    # Prop X: distinct σ|X sequence vs N5 on G[X] from the first σ|X
    seq = []
    for s, t in st:
        x = tuple(s[v] for v in XE)
        if not seq or seq[-1] != x: seq.append(x)
    s0 = st[0][0]; hst, _ = trace(h, ({idx[v]: idx[s0[v]] for v in XE}, {}), check=False)
    hseq = [tuple(keep[s[idx[v]]] for v in XE) for s, _ in hst]
    cnt["runs_X"] += 1
    if hseq != seq: cnt["propX_fail"] += 1
if __name__ == "__main__":
    ALL = "--allstates" in sys.argv
    if ALL: sys.argv.remove("--allstates")
    RS = "--randstart" in sys.argv
    if RS: sys.argv.remove("--randstart")
    cnt = {"games": 0, "X_empty": 0, "runs_X": 0, "pure": 0, "L1_fail": 0, "propX_fail": 0}
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
