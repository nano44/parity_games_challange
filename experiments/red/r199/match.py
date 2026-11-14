#!/usr/bin/env python3
"""L-RED R199 MATCH: for each mover's C-requirement (r199/req.py) list the simple functions of OTHER movers' current options that
meet it on every required state: copy / NOT of one mover, XOR / XNOR, AND / OR (with negations) of two. DATA aid for design."""
import sys, json, itertools
sys.path.insert(0, '.')
import req as RQ
T = json.load(open(sys.argv[1])); lev = [m[0] for m in T['movers']]; WT = [m[1] for m in T['movers']]
S = [tuple(s) for s in T['states']]; bad, rq = RQ.requirements(lev, WT, T['gate'], S); N = len(lev)
nm = lambda v: 'uv'[v % 2] + str(lev[v]) if v < 2 * (max(lev) + 1) else f"h{v}"
for x in range(N):
    R = [(s, b) for (s, v), b in rq.items() if v == x]
    if not R: continue
    found = []
    for y in range(N):
        if y == x: continue
        for neg in (0, 1):
            if all((S[s][y] ^ neg) == b for s, b in R): found.append(("NOT " if neg else "") + nm(y))
    for y, z in itertools.combinations([v for v in range(N) if v != x], 2):
        for neg in (0, 1):
            if all((S[s][y] ^ S[s][z] ^ neg) == b for s, b in R): found.append(("XNOR " if neg else "XOR ") + nm(y) + "," + nm(z))
        for a, c, o in itertools.product((0, 1), (0, 1), (0, 1)):
            f = lambda s: ((S[s][y] ^ a) & (S[s][z] ^ c)) ^ o
            if all(f(s) == b for s, b in R): found.append(f"{'NAND' if o else 'AND'}({'~' if a else ''}{nm(y)},{'~' if c else ''}{nm(z)})")
    print(nm(x), len(R), "req:", found[:12])
