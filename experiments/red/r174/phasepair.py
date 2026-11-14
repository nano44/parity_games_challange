#!/usr/bin/env python3
"""L-RED R174 check of Lemma PHASE-PORTAL (docs/red/R174-zroute.md §1).
Pairs as in R173 portalck (consecutive moves i0 -> i1 @ j1, i1 -> i2 @ j2 of an Even h, same class X in G_F, no fallback at j1..j2,
inside one TWO-FIX window), with premise TH: node(W_j1(X)) = node(W_j2(X)) and NRW: h and the prefixes of i1, i2 are off X's W-plays at
j1 and j2. Lemma: if i2 was Xi-improving at state j1 - 1 (key Xi(i2) > key Xi(i0)), the move at j2 is an exact tau-tie.
Prints: pairs, TH+NRW pairs, of which i2 available at j1 (AV), AV pairs that are ties, VIOLATIONS (AV and not tie; must be 0),
and W-strict TH pairs (necessarily not AV: the Xi-gated steps of route (Z)).  Usage: phasepair.py G START"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "r170")); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, start_pair, readstart, Engine, dual
import pg
from freeze import run, windows, frozen

def play(succ1, x):
    s, v = set(), x
    while v not in s: s.add(v); v = succ1[v]
    return s

def analyze(g, st, cap=10 ** 6):
    E0, Ed0 = Engine(g), Engine(dual(g)); s, t = start_pair(g, E0, Ed0, st)
    S, T, F, E = run(g, s, t, cap=cap); W, SB = windows(g, S, T, E)
    n, own, pr = g.n, g.owner, g.prio; c = dict(pairs=0, th=0, av=0, avtie=0, bad=0, gated=0, K=len(S) - 1)
    for a, b in W:
        if b - a < 2: continue
        gf = frozen(g, SB[a], T[a]); tau, sb = T[a], SB[a]
        EW = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]))
        EX = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [sb[v]] for v in range(n)]))
        st1 = lambda j: tuple(S[j][v] if own[v] == 0 else -1 for v in range(n))
        def cls(h, x):
            v, seen = x, {h}
            while len(gf.succ[v]) == 1:
                if v in seen: return None, None
                seen.add(v); v = gf.succ[v][0]
            return (None, None) if v in seen else (v, seen - {h})
        for h in range(n):
            if own[h] != 0: continue
            mv = [(j, S[j - 1][h], S[j][h]) for j in range(a + 1, b + 1) if S[j][h] != S[j - 1][h]]
            for (j1, i0, i1), (j2, _, i2) in zip(mv, mv[1:]):
                if any(F[j] for j in range(j1, j2 + 1)): continue
                X, p1 = cls(h, i1); X2, p2 = cls(h, i2)
                if X is None or X2 != X: continue
                c["pairs"] += 1
                w1, w2 = EW.evaluate(st1(j1))[0], EW.evaluate(st1(j2))[0]
                pre = {h} | p1 | p2
                nrw = all(not (pre & play([S[j][v] if own[v] == 0 else tau[v] for v in range(n)], X)) for j in (j1, j2))
                if w1[X][0] != w2[X][0] or not nrw: continue
                c["th"] += 1
                x0 = EX.evaluate(st1(j1 - 1))[0]; av = EX.key(x0[i2]) > EX.key(x0[i0])
                tie = EW.key(w2[i1]) == EW.key(w2[i2])
                c["av"] += av; c["avtie"] += av and tie; c["bad"] += av and not tie; c["gated"] += (not tie) and not av
    return c

if __name__ == "__main__":
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
    r = analyze(g, st); print("PHASEPAIR " + os.path.basename(sys.argv[1]) + " " + " ".join(f"{k} {v}" for k, v in r.items()))
