#!/usr/bin/env python3
"""Box 7: along N5's run (n5_lock.step = n5.py's loop), count changes of Odd's best reply σ̄_k (VJ counterstrategy to σ_k, on Odd's
vertices) and of Even's best reply τ̄_k (to τ_k, on Even's vertices), and the Even / Odd moves. By VJ00 Prop. 7.4 (one-player games,
O(n^3) for ANY policy), Even moves between two changes of σ̄ form an improvement sequence of the one-player game G_c (c = the constant
reply), so #Even moves ≤ O(n^3)·(1 + #changes of σ̄); dually for Odd. Usage: n5_brchanges.py game.pg [startfile]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from n5_lock import step
from n5 import pg, Engine, dual
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); E, Ed = Engine(g), Engine(dual(g))
s, t = list(E.initial("best")), list(Ed.initial("best"))
if len(sys.argv) > 2:
    L = [l for l in open(sys.argv[2]) if l.split() and l.split()[0] in ("SIGMA0", "TAU0")]
    for j, arr in ((0, s), (1, t)):
        for tok in L[j].split()[1:]: v, w = map(int, tok.split(":")); arr[v] = w
O = [v for v in range(g.n) if g.owner[v] == 1]; V0 = [v for v in range(g.n) if g.owner[v] == 0]
def br(): return tuple(E.evaluate(tuple(s))[1][v] for v in O), tuple(Ed.evaluate(tuple(t))[1][v] for v in V0)
bs, bt = br(); cs = ct = em = om = it = 0
while True:
    r = step(g, E, Ed, s, t)
    if r is None: break
    it += 1; em += r[0] != s; om += r[1] != t; s, t = r[0], r[1]
    ns, nt = br(); cs += ns != bs; ct += nt != bt; bs, bt = ns, nt
print(f"{os.path.basename(sys.argv[1])}: n={g.n} iterations {it}; Even moves {em}, changes of Odd's best reply {cs}; Odd moves {om}, changes of Even's best reply {ct}")
