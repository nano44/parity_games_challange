"""L-RED box 29 (produced on Opus 5.5): inside the LONGEST joint lambda-phase of an N5 run: per vertex, the number of switches and of
RETURNS (switching to a successor it used earlier in the same phase), for both players; prints the maxima and the sum of switches.
Run via declines.states (n5.py replica, counts asserted = n5.run). Usage: phasereturns.py G.pg [STARTFILE]"""
import os, sys
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import declines  # noqa: E402
import n5  # noqa: E402
import n5tr  # noqa: E402
import pg  # noqa: E402
from si import Engine  # noqa: E402
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); n = g.n
st = n5tr.read_start(sys.argv[2]) if len(sys.argv) > 2 else None
seq = declines.states(g, st); E, Ed = Engine(g), Engine(n5.dual(g))
lam = [(tuple(x[0] for x in E.evaluate(s)[0]), tuple(y[0] for y in Ed.evaluate(t)[0])) for s, t, _, _ in seq]
runs = []; a = 0
for i in range(1, len(seq) + 1):
    if i == len(seq) or lam[i] != lam[i - 1]: runs.append((a, i - 1)); a = i
a, b = max(runs, key=lambda r: r[1] - r[0])
sw = defaultdict(int); ret = defaultdict(int); used = defaultdict(set)
for k in range(a, b):
    for v in range(n):
        x, y = (seq[k][0][v], seq[k + 1][0][v]) if g.owner[v] == 0 else (seq[k][1][v], seq[k + 1][1][v])
        used[v].add(x)
        if x != y:
            sw[v] += 1
            if y in used[v]: ret[v] += 1
            used[v].add(y)
print(f"{os.path.basename(sys.argv[1])} n {n}: longest phase states {a}..{b} ({b - a} iterations); switches {sum(sw.values())}, "
      f"max switches at a vertex {max(sw.values(), default=0)}, max returns at a vertex {max(ret.values(), default=0)}, "
      f"vertices with a return {sum(1 for v in ret if ret[v])}")
