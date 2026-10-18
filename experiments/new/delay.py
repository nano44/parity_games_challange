#!/usr/bin/env python3
"""L-NEW: delay transform (candidate killer for N1 DISC-ANNEAL). Input game G; every original priority is shifted by +2
(parity kept). Every edge (v, w) of an Even vertex v with >= 2 successors is replaced by a chain v -> c_1 -> ... -> c_L -> w
of fresh single-successor Odd vertices; the chain has priority 0 if w is v's best-reward start successor sigma0(v)
(L-SI's engine convention), else priority 1. Every cycle of G contains an original vertex (priority >= 2), so cycle winners,
hence W_E and W_O on the original vertices, are unchanged (a chain vertex wins with its successor).
Intent: for horizons 1/(1-gamma) << L only the chains' 0/1 rewards are visible, so sigma0 is optimal there and the later
phases of N1 start from sigma0, Friedmann's bad start.
Usage: delay.py game.pg L [uniform|byprio|invprio] > out.pg   (byprio: chain length 1 + L*pr(w)//maxpr; invprio: 1 + L*(maxpr-pr(w))//maxpr)"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg
src = "".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))
g = pg.parse(src); L0 = int(sys.argv[2]); n = g.n
mode = sys.argv[3] if len(sys.argv) > 3 else 'uniform'; mp = max(g.prio) or 1
def clen(w):
    if mode == 'byprio': return 1 + L0 * g.prio[w] // mp
    if mode == 'invprio': return 1 + L0 * (mp - g.prio[w]) // mp
    return L0
def rk(w):
    rr = g.prio[w] if g.prio[w] % 2 == 0 else -g.prio[w]
    return (rr, w if rr % 2 == 0 else -w)
prio = [p + 2 for p in g.prio]; owner = list(g.owner); succ = [None] * n
for v in range(n):
    s = sorted(set(g.succ[v]))
    if g.owner[v] == 0 and len(s) >= 2:
        s0 = max(s, key=rk); new = []
        for w in s:
            first = len(prio); L = clen(w)
            for i in range(L):
                prio.append(0 if w == s0 else 1); owner.append(1); succ.append(None)
            for i in range(L - 1):
                succ[first + i] = [first + i + 1]
            succ[first + L - 1] = [w]; new.append(first)
        succ[v] = new
    else:
        succ[v] = s
print(pg.dumps(pg.Game(prio, owner, succ)), end="")
