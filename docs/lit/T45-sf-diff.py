#!/usr/bin/env python3
"""T45: run SF-Xi (docs/lit/T44-sf-variants.py) and L-NEW's N5-SF step (n5sf.py, passed as a path; e.g. git show 057a08eb:experiments/new/box54/n5sf.py > /tmp/x/n5sf.py, sha1 1ea3bdc7)
from the same states along the SF-Xi trace; print the first state where the two steps differ and the Xi comparison of the two results.
Run from the repo root: python3 -I docs/lit/T45-sf-diff.py game.pg start|- path/to/n5sf.py"""
import sys, os, importlib.util
R = os.getcwd()
for p in ("experiments/new", "experiments/si", "experiments/harness", "experiments/new/box21"): sys.path.insert(0, os.path.join(R, p))
def mod(name, path):
    sp = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
V = mod("v", "docs/lit/T44-sf-variants.py"); X = mod("x", sys.argv[3])
import pg, n5
from si import Engine
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); n = g.n
st = V.readstart(sys.argv[2]) if sys.argv[2] != "-" else None
E, Ed = Engine(g), Engine(n5.dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best"))
if st:
    for v, w in st[0].items(): s[v] = w
    for v, w in st[1].items(): t[v] = w
def sfxi(s, t):
    vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs); vt, _ = Ed.evaluate(tuple(t)); It = Ed.improving(tuple(t), vt)
    if not Is and not It: return None
    ns, nt = list(s), list(t)
    if Is: ns = list(V.si_opt(V.restricted(g, [([s[v]] + [w for x, w in Is if x == v]) if g.owner[v] == 0 else g.succ[v] for v in range(n)]), s))
    if It: nt = list(V.si_opt(V.restricted(n5.dual(g), [([t[v]] + [w for x, w in It if x == v]) if g.owner[v] == 1 else g.succ[v] for v in range(n)]), t))
    return ns, nt
k = 0; first = None
while True:
    a = sfxi(s, t); b = X.step(g, E, Ed, s, t)
    if a is None or b is None:
        print("both stop" if a is None and b is None else "STOP MISMATCH", "at", k); break
    bs, bt = list(b[0]), list(b[1])
    if (a[0], a[1]) != (bs, bt):
        dE = [(v, s[v], a[0][v], bs[v]) for v in range(n) if g.owner[v] == 0 and a[0][v] != bs[v]]
        dO = [(v, t[v], a[1][v], bt[v]) for v in range(n) if g.owner[v] == 1 and a[1][v] != bt[v]]
        va = E.evaluate(tuple(a[0]))[0]; vb = E.evaluate(tuple(bs))[0]
        better = sum(1 for v in range(n) if E.key(va[v]) > E.key(vb[v])); worse = sum(1 for v in range(n) if E.key(va[v]) < E.key(vb[v]))
        print(f"DIVERGE at state {k}: Even (v, cur, sfxi, n5sf) {dE[:6]}{'...' if len(dE) > 6 else ''} Odd {dO[:6]}; Xi(sfxi) > Xi(n5sf) at {better} vertices, < at {worse}")
        break
    s, t = a; k += 1
