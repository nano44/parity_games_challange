#!/usr/bin/env python3
"""Box 5: along SSI's run (n5.py mode ssi, DLM start pair), apply N5's step (n5_lock.step = n5.py's loop) to every SSI state and
compare with SSI's step: count states where they agree (σ and τ), and list per-vertex disagreements (SSI keeps / N5 switches, etc.).
Usage: dlm_agree.py game.pg startfile"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n5
from n5 import pg, Engine, dual
from n5_lock import step
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
L = [l for l in open(sys.argv[2]) if l.split() and l.split()[0] in ("SIGMA0", "TAU0")]
st = tuple(dict(map(int, t.split(":")) for t in L[j].split()[1:]) for j in (0, 1))
E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best"))
for v, w in st[0].items(): s[v] = w
for v, w in st[1].items(): t[v] = w
it = agree = 0; kinds = {}
while True:
    vs, sbar = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs); vt, tbar = Ed.evaluate(tuple(t)); It = Ed.improving(tuple(t), vt)
    if not Is and not It: break
    ns, nt = list(s), list(t)
    for v, w in Is:
        if tbar[v] == w: ns[v] = w
    for v, w in It:
        if sbar[v] == w: nt[v] = w
    r = step(g, E, Ed, s, t); it += 1
    if (r[0], r[1]) == (ns, nt): agree += 1
    else:
        for v in range(g.n):
            a, b = (ns[v], r[0][v]) if g.owner[v] == 0 else (nt[v], r[1][v])
            if a != b:
                old = s[v] if g.owner[v] == 0 else t[v]
                k = ("E" if g.owner[v] == 0 else "O") + ("_ssi-keeps/n5-switches" if a == old else "_ssi-switches/n5-keeps" if b == old else "_both-switch-differently")
                kinds[k] = kinds.get(k, 0) + 1
    s, t = ns, nt
assert it == n5.run(g, "ssi", st)[0]
print(f"{os.path.basename(sys.argv[1])}: SSI iterations {it}; N5 step agrees with SSI's at {agree}/{it} SSI states; disagreements {kinds}")
