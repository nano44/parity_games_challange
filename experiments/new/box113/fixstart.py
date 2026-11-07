#!/usr/bin/env python3
"""L-NEW box 113 (referee finding D-ODD-1 / F-1): repair a start file. Every entry that is not an edge of a vertex of that player
(SIGMA0: Even, TAU0: Odd) is replaced by n5x's default initial move ("best" initial strategy of experiments/si/si.py on the game or its
dual); valid entries are kept verbatim. Prints the replaced entries. With --complete, OUT lists every vertex of each player (valid entries, else the default),
as n5b (experiments/n5-second/n5b.py read_start) needs. Usage: fixstart.py G.pg START OUT [--complete]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, Engine, dual
g = load(sys.argv[1]); dflt = (list(Engine(g).initial("best")), list(Engine(dual(g)).initial("best")))
out, rep = [], []
for l in open(sys.argv[2]).read().split("\n"):
    t = l.split()
    if t and t[0] in ("SIGMA0", "TAU0"):
        own = 0 if t[0] == "SIGMA0" else 1; nt = [t[0]]
        for e in t[1:]:
            v, w = map(int, e.split(":"))
            if 0 <= v < g.n and g.owner[v] == own and w in g.succ[v]: nt.append(e)
            elif 0 <= v < g.n and g.owner[v] == own: nt.append(f"{v}:{dflt[own][v]}"); rep.append((t[0], v, w, dflt[own][v]))
            else: rep.append((t[0], v, w, "dropped (vertex of the other player)"))
        l = " ".join(nt)
    out.append(l)
if "--complete" in sys.argv:
    cur = ({}, {})
    for l in out:
        t = l.split()
        if t and t[0] in ("SIGMA0", "TAU0"):
            for e in t[1:]: v, w = map(int, e.split(":")); cur[0 if t[0] == "SIGMA0" else 1][v] = w
    out = [name + " " + " ".join(f"{v}:{cur[o].get(v, dflt[o][v])}" for v in range(g.n) if g.owner[v] == o) for o, name in ((0, "SIGMA0"), (1, "TAU0"))]
open(sys.argv[3], "w").write("\n".join(out) + ("\n" if "--complete" in sys.argv else ""))
print(f"FIXSTART {os.path.basename(sys.argv[2])} replaced {len(rep)}: {rep}")
