#!/usr/bin/env python3
"""L-RED successor 24: path sets of the Odd choice vertices (gates) along a run. P_t(q) = vertices on the (sigma_t, sigma-bar_t)-play from q,
before the cycle node c, of rank above rank(c) (S1's P). Per phase: PCH (P changes of a gate), RESET (a change that removes an element
below the unchanged top: a low-digit reset), and RESET_STALL (resets at a state whose transition is a stall, i.e. an in-phase fallback).
Usage: gatep.py GAME.pg START|S3"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "sel"))
import trace as T
def rank_of(g):
    order = sorted(range(g.n), key=lambda v: (g.prio[v], v)); r = [0] * g.n
    for i, v in enumerate(order): r[v] = i
    return r
def pset(g, rk, s, sb, q):
    seen = []; v = q
    while v not in seen:
        seen.append(v); v = s[v] if g.owner[v] == 0 else sb[v]
    cyc = seen[seen.index(v):]; c = max(cyc, key=lambda u: rk[u])
    pre = seen[:seen.index(c)] if c in seen else seen
    return frozenset(u for u in pre if rk[u] > rk[c]), c
def measure(g, st, cap=5000):
    states = []; it, fb, ph, mp, s, t, hist = T.run(g, st, cap=cap, log=lambda *a: None, states=states)
    E, Ed = T.Engine(g), T.Engine(T.dual(g)); rk = rank_of(g)
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
    ev = [E.evaluate(s_) for s_, t_ in states]
    lam = [(t_, tuple(x[0] for x in ev[i][0]), tuple(x[0] for x in Ed.evaluate(t_)[0])) for i, (s_, t_) in enumerate(states)]
    P = [{q: pset(g, rk, states[i][0], ev[i][1], q) for q in Q} for i in range(len(states))]
    best = (0, 0, 0); cur = [0, 0, 0]
    for i in range(len(hist)):
        if lam[i + 1] != lam[i]: cur = [0, 0, 0]; continue
        for q in Q:
            a, ca = P[i][q]; b, cb = P[i + 1][q]
            if a != b:
                cur[0] += 1
                if a and b and max(a, key=lambda u: rk[u]) == max(b, key=lambda u: rk[u]) and (a - b):
                    cur[1] += 1
                    if i + 1 < len(hist) and hist[i + 1][0] == "FB": cur[2] += 1
        best = max(best, tuple(cur), key=lambda x: (x[2], x[1], x[0]))
    return best
if __name__ == "__main__":
    g = T.pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
    st = ({}, {}) if sys.argv[2] == "S3" else T.readstart(sys.argv[2])
    print("PCH RESET RESET_STALL", measure(g, st))
