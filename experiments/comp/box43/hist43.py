#!/usr/bin/env python3
"""L-COMP box 43 item 1 (a): the run of MY IDEAL-CYC engine (box37/ideal37.py: my builder of Gamma(G), n5b SpecSI's VJ values with
Odd's optimal counterstrategy, my Howard step and tie rule) written in the --hist format of L-NEW 72's level208.py (claude/l-new
8db300fe, experiments/new/box208/level208.py header: «--hist HIST.json runs every counter on a history in that format (nxt[t][v] = the
successor of v on its play at t, cls[t][v] = [reward, E])»; fields {genome, g3, n, T, movers, kind, owner, succ, ebit, nxt, cls}).
kind[v] = first letter of my vertex name: x mover, g gate, b beta, e e-vertex, cX, cW, K core (level208 uses only «e» and «x»).
reward = the priority of the cycle node, negated if odd; E = the e-vertices of Pi as a number, bit i = the i-th least relevant e-vertex
(relevance = (priority, index)). No code of level208.py, gfc203, idealcyc or si.py is used here.
Usage: hist43.py G.json OUT.json"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "box37")]
import ideal37


def hist(G):
    g, V, Hs = ideal37.run(G); n, N, T = g.n, G["N"], len(Hs) - 1
    kind = [None] * n
    for k, v in V.items(): kind[v] = k[0] if isinstance(k, tuple) else k
    evs = sorted((v for v in range(n) if kind[v] == "e"), key=lambda v: (g.prio[v], v)); ebit = {v: 1 << i for i, v in enumerate(evs)}
    rew = lambda v: g.prio[v] if g.prio[v] % 2 == 0 else -g.prio[v]
    nxt, cls = [], []
    for val, ch, st in Hs:
        row = [st[v] if g.owner[v] == 0 else ch[v] for v in range(n)]
        assert all(row[v] in g.succ[v] for v in range(n))
        nxt.append(row); cls.append([[rew(val[v][0]), sum(ebit[u] for u in val[v][1] if u in ebit)] for v in range(n)])
    return dict(genome=G, g3=False, n=n, T=T, movers=[V[("x", x)] for x in range(N)], kind=kind, owner=list(g.owner),
                succ=[list(s) for s in g.succ], ebit={str(v): b for v, b in ebit.items()}, nxt=nxt, cls=cls)


if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); G = G.get("genome", G); P = hist(G); json.dump(P, open(sys.argv[2], "w"))
    print("ideal37 engine", os.path.basename(sys.argv[1]), "n", P["n"], "T", P["T"])
