"""L-RED box 27 (produced on Opus 5.5): pure-Y blocks of a canonical N5 run on C^1O, by L-NEW's definition (N5-1O-box22.md §6):
X = vertices with no path to o (the only Odd choice vertex); a pure-Y block = a maximal stretch of iterations in which sigma|X and
tau are both unchanged. Prints |X|, |Y|, o-acyclicity, the block lengths and the longest block. Run via declines.states (n5.py
replica, counts asserted = n5.run). Usage: blockcheck.py G.pg [STARTFILE]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import declines  # noqa: E402
import n5tr  # noqa: E402
import pg  # noqa: E402
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); n = g.n
st = n5tr.read_start(sys.argv[2]) if len(sys.argv) > 2 else None
oc = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]
assert len(oc) == 1, f"not C^1O: Odd choice vertices {oc}"
o = oc[0]; reach = {o}; ch = True
while ch:
    ch = False
    for v in range(n):
        if v not in reach and any(w in reach for w in g.succ[v]): reach.add(v); ch = True
X = [v for v in range(n) if v not in reach]; XE = [v for v in X if g.owner[v] == 0]
acyc = not any(w in reach for w in g.succ[o])
seq = declines.states(g, st)
blocks = []; cur = 0
for k in range(1, len(seq)):
    same = all(seq[k][0][v] == seq[k - 1][0][v] for v in XE) and seq[k][1] == seq[k - 1][1]
    if same: cur += 1
    else:
        if cur: blocks.append(cur)
        cur = 0
if cur: blocks.append(cur)
print(f"{os.path.basename(sys.argv[1])} n {n}: o {o}, o-acyclic {acyc}, |X| {len(X)}, |Y| {n - len(X)}, iterations {len(seq) - 1}, "
      f"pure-Y blocks {blocks}, longest {max(blocks, default=0)}")
