#!/usr/bin/env python3
"""Box 31 (a): direct test of Lemma TB on random one-player arenas. Random game g, random sigma, tau; arena H = sigma's edge plus a
random subset of Even's other edges; sigma' = S4a's optimum of H against tau (same Engine call as n5.py S4a). For every Even v with
sigma'(v) != sigma(v) and val(sigma', tau)(v) = val(sigma, tau)(v), v not its own cycle node:
  odd c: sigma'(v) < sigma(v);  even c, values equal on v's whole old play to c: pk(sigma')(v) <lex pk(sigma)(v).
Usage: tbarena.py N nmin nmax seed"""
import sys, random
from tbcheck import *

def s4a(g, s, t, arena):
    succ = [sorted(arena[v]) if g.owner[v] == 0 else [t[v]] for v in range(g.n)]
    Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
    _, best = Er.evaluate(tuple(t[v] if g.owner[v] == 1 else -1 for v in range(g.n)))
    return [best[v] if g.owner[v] == 0 else s[v] for v in range(g.n)]

def main(N, lo, hi, seed):
    rng = random.Random(seed); st = dict(odd=0, oddviol=0, even=0, evenviol=0, evennc=0, selfc=0, opt_not_kept=0)
    for _ in range(N):
        g = layered(rng, lo, hi) if rng.random() < 0.5 else rgame(rng, lo, hi)
        s = [rng.choice(g.succ[v]) for v in range(g.n)]; t = list(s)
        arena = {v: {s[v]} | {w for w in g.succ[v] if rng.random() < 0.6} for v in range(g.n) if g.owner[v] == 0}
        ns = s4a(g, s, t, arena)
        Eg0, W0 = wvals(g, s, t); Eg1, W1 = wvals(g, ns, t)
        K0 = [Eg0.key(W0[x]) for x in range(g.n)]; K1 = [Eg1.key(W1[x]) for x in range(g.n)]
        for v in range(g.n):
            if g.owner[v] != 0 or ns[v] == s[v] or K0[v] != K1[v]: continue
            c = W0[v][0]
            if c == v: st["selfc"] += 1; continue
            if g.prio[c] % 2 == 1:
                st["odd"] += 1
                if not ns[v] < s[v]: st["oddviol"] += 1; st.setdefault("ex", (g, s, t, v, arena))
            else:
                seq, _ = play(g, s, t, v); route = seq[:seq.index(c)] if c in seq else seq
                if any(K0[x] != K1[x] for x in route): st["evennc"] += 1; continue
                a, b = pk(g, s, t, v, c), pk(g, ns, t, v, c); st["even"] += 1
                if a is None or b is None or not b < a: st["evenviol"] += 1; st.setdefault("ex2", (g, s, t, v, a, b))
    print("TBA", {k: v for k, v in st.items() if not k.startswith("ex")})
    for k in ("ex", "ex2"):
        if k in st: e = st[k]; print(k, "n", e[0].n, "prio", e[0].prio, "owner", e[0].owner, "succ", e[0].succ, "s", e[1], "v", e[3:])
if __name__ == "__main__": main(*map(int, sys.argv[1:5]))
