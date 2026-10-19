#!/usr/bin/env python3
"""Box 7 falsification check of K9 (N5-K9-reading.md): K9's argument uses only that each player's moves switch improvements, so it
also applies to SSI (2309.02223 Alg. 2, switch-all; n5.py mode ssi) and to classical switch-all SI (Odd = best reply; si.py). On
their EXPONENTIAL runs the number of best-reply changes must therefore be large. Counts changes of σ̄_k (Odd's computed best reply).
Usage: k9_sanity.py ssi game.pg startfile | k9_sanity.py sa game.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from n5 import pg, Engine, dual
mode, path = sys.argv[1], sys.argv[2]
g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%"))); E, Ed = Engine(g), Engine(dual(g))
O = [v for v in range(g.n) if g.owner[v] == 1]; V0 = [v for v in range(g.n) if g.owner[v] == 0]
s, t = list(E.initial("best")), list(Ed.initial("best"))
if mode == "ssi":
    L = [l for l in open(sys.argv[3]) if l.split() and l.split()[0] in ("SIGMA0", "TAU0")]
    for j, arr in ((0, s), (1, t)):
        for tok in L[j].split()[1:]: v, w = map(int, tok.split(":")); arr[v] = w
it = em = om = cs = ct = 0
bs = tuple(E.evaluate(tuple(s))[1][v] for v in O); bt = tuple(Ed.evaluate(tuple(t))[1][v] for v in V0)
while True:
    vs, sbar = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
    vt, tbar = Ed.evaluate(tuple(t)); It = Ed.improving(tuple(t), vt) if mode == "ssi" else []
    if not Is and not It: break
    ns, nt = list(s), list(t)
    if mode == "ssi":
        for v, w in Is:
            if tbar[v] == w: ns[v] = w
        for v, w in It:
            if sbar[v] == w: nt[v] = w
    else:
        ns = list(E.rule_switch_all(tuple(s), vs, Is, None))
    it += 1; em += ns != s; om += nt != t; s, t = ns, nt
    nbs = tuple(E.evaluate(tuple(s))[1][v] for v in O); nbt = tuple(Ed.evaluate(tuple(t))[1][v] for v in V0)
    cs += nbs != bs; ct += nbt != bt; bs, bt = nbs, nbt
print(f"{mode} {os.path.basename(path)}: n={g.n} iterations {it}; Even moves {em}, changes of σ̄ {cs}; Odd moves {om}, changes of τ̄ {ct}")
