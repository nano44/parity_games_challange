"""L-RED box 26 (produced on Opus 5.5): iterations per joint lambda-phase of an N5 run (lambda = cycle node of every vertex in Xi_sigma
and in Xi_tau on G^d; L-NEW box 21 Lemma Phi: at most 2n(n-1)+1 phases). Run = declines.states (n5.py replica, counts asserted).
Usage: phaselen.py G.pg [STARTFILE]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import declines  # noqa: E402
import n5  # noqa: E402
import n5tr  # noqa: E402
import pg  # noqa: E402
from si import Engine  # noqa: E402
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
st = n5tr.read_start(sys.argv[2]) if len(sys.argv) > 2 else None
seq = declines.states(g, st); E, Ed = Engine(g), Engine(n5.dual(g))
lam = [(tuple(x[0] for x in E.evaluate(s)[0]), tuple(x[0] for x in Ed.evaluate(t)[0])) for s, t, _, _ in seq]
runs = []; cur = 0
for i in range(1, len(lam)):
    cur += 1
    if lam[i] != lam[i - 1]: runs.append(cur); cur = 0
if cur: runs.append(cur)
print(f"{os.path.basename(sys.argv[1])} n {g.n}: iterations {len(seq) - 1}, iterations per joint lambda-phase {runs}, longest {max(runs, default=0)}")
