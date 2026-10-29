#!/usr/bin/env python3
"""REFEREE-2 succ. 20: does the approved RESULTS line's GP* clause need GP*'s 'L <= k - a'? At the FIRST state k = a of a frozen W-phase,
look for x, z with (x, z) in I_sigma_a (an edge that is never BLOCKED, so the line's condition holds for the path x -> z whatever state it
is read at), z a W-cycle node, and W_a(x) < value(x -> z). Prints the first instances found."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gp_check as GC
DC, pg, Engine, dual = GC.DC, GC.pg, GC.Engine, GC.dual
found = 0
for line in [l.split() for l in open(sys.argv[1]) if l.strip()]:
    g = pg.read(os.path.join(DC.ROOT, line[0])); n = g.n; E = Engine(g)
    s, t = Engine(g).initial("best"), Engine(dual(g)).initial("best")
    states, fbs = DC.Runner(g).run(list(s), list(t))
    sg, tu = states[0]
    xe, _ = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
    Is = set(E.improving(tuple(sg), xe))
    nxW = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
    W = [GC.pval(E, nxW, v) for v in range(n)]
    for x, z in sorted(Is):
        if W[z][0] != z: continue
        val = (z, E.bit[x] if E.rank[x] > E.rank[z] else 0, 1)
        if E.key(W[x]) < E.key(val):
            print(f"INSTANCE {line[0]} (S3 start, state 0 = first state of its frozen W-phase): x={x} z={z} (x,z) in I_sigma_0; "
                  f"W_0(x)={W[x]} < value(x->z)={val}"); found += 1; break
    if found >= 3: break
print("found", found)
