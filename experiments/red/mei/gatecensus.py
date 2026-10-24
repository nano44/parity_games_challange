#!/usr/bin/env python3
"""Census of Even's improving set I(sigma) (N5's gate, against sigma-bar) over ALL Even strategies of a small game: histogram of
|I|, number of distinct valuations Xi (ties), and the out-set map sigma -> I(sigma) as a set of (vertex, successor) pairs.
For a strict unique-sink orientation on a cube (binary Even choices) the out-set map is a bijection (Szabo-Welzl), so at most d
strategies (d = number of Even choice vertices) have |I| = 1. Usage: gatecensus.py game.pg"""
import sys, os, itertools, collections
HERE = os.path.dirname(os.path.abspath(__file__))
for d in ("../../harness", "../../si"): sys.path.insert(0, os.path.join(HERE, d))
import pg
from si import Engine
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
E = Engine(g)
ch = [v for v in range(g.n) if g.owner[v] == 0 and len(g.succ[v]) > 1]
hist = collections.Counter(); outsets = collections.Counter(); xis = set(); N = 0
for combo in itertools.product(*[g.succ[v] for v in ch]):
    st = [g.succ[v][0] if g.owner[v] == 0 else -1 for v in range(g.n)]
    for v, w in zip(ch, combo): st[v] = w
    val, _ = E.evaluate(tuple(st)); I = E.improving(tuple(st), val)
    hist[len(I)] += 1; outsets[frozenset(v for v, _ in I)] += 1; N += 1
    xis.add(tuple(E.key(val[v]) for v in range(g.n)))
print(f"{os.path.basename(sys.argv[1])}: d={len(ch)} strategies={N} distinct Xi={len(xis)} |I| histogram={dict(sorted(hist.items()))} "
      f"out-set map injective={max(outsets.values()) == 1}")
