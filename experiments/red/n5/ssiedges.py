"""L-RED box 25 (produced on Opus 5.5): edges used by SSI (n5.run mode 'ssi', i.e. 2309.02223 Alg. 2 SWITCH-ALL; loop replicated,
counts asserted equal to n5.run) from a start pair: prints every (v, w) that some strategy of the run takes, and the edges never taken.
Usage: ssiedges.py G.pg STARTFILE"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import n5tr  # noqa: E402
import n5  # noqa: E402
import pg  # noqa: E402
from si import Engine  # noqa: E402
path = sys.argv[1]; g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%"))); st = n5tr.read_start(sys.argv[2])
nm = n5tr.names_of(path); N = lambda v: nm.get(v, str(v))  # noqa: E731
E, Ed = Engine(g), Engine(n5.dual(g))
sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
for v, w in st[0].items(): sigma[v] = w
for v, w in st[1].items(): tau[v] = w
used = {(v, sigma[v]) for v in range(g.n) if g.owner[v] == 0} | {(v, tau[v]) for v in range(g.n) if g.owner[v] == 1}
it = 0
while True:
    vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
    vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
    if not Is and not It: break
    it += 1
    ns, nt = list(sigma), list(tau)
    for v, w in Is:
        if tbar[v] == w: ns[v] = w
    for v, w in It:
        if sbar[v] == w: nt[v] = w
    sigma, tau = ns, nt
    used |= {(v, sigma[v]) for v in range(g.n) if g.owner[v] == 0} | {(v, tau[v]) for v in range(g.n) if g.owner[v] == 1}
assert it == n5.run(g, "ssi", st)[0]
allE = {(v, w) for v in range(g.n) for w in set(g.succ[v]) if len(set(g.succ[v])) > 1}
print(f"SSI iterations {it}; choice edges {len(allE)}, used {len(allE & used)}; never used: " + " ".join(f"{N(v)}>{N(w)}" for v, w in sorted(allE - used)))
