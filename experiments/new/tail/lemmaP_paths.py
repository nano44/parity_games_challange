#!/usr/bin/env python3
"""Box 11 §7 (REFEREE-2 G-1P-7): a FEASIBLE partial check of Lemma P on long phases where simple-path enumeration is infeasible. Two polynomial-size
consequences are checked at every in-phase step k of every λ-phase of a one-player switch-best run:
 C1 (what Theorem PH's proof uses): every improving edge (x,z) of ρ_k that is not cycle-closing (x not on the ρ_k-path π_z from z to its cycle
    node c and not on c's cycle) has |π_z| + 1 > k  [else Lemma P with r = x,π_z would make (x,z) non-improving].
 C2 (Lemma P on the paths that occur): for every earlier in-phase step j ≤ k, every vertex x and every successor z of x with x not on the
    ρ_j-path π^j_z: if |π^j_z| + 1 ≤ k then Ω_k(x) ⪰ value(x, π^j_z).
Reports checks and violations per instance. EXACT=1 uses n5.py's step (phase_trace.sbstep honours it). Usage: lemmaP_paths.py game.pg [...]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg
from n5 import Engine
from phase_trace import sbstep
def paths_of(g, s, E, vs):
    """for every vertex z: (path from z to its cycle node, excluding the cycle node; set of vertices on c's cycle)"""
    out = {}
    for z in range(g.n):
        c = vs[z][0]; path = []; x = z; seen = set()
        while x != c and x not in seen: seen.add(x); path.append(x); x = s[x] if g.owner[x] == 0 else g.succ[x][0]
        out[z] = path
    cyc = {}
    for z in range(g.n):
        c = vs[z][0]
        if c not in cyc:
            x = c; C = []
            while True:
                C.append(x); x = s[x] if g.owner[x] == 0 else g.succ[x][0]
                if x == c: break
            cyc[c] = set(C)
    return out, cyc
def value_of(E, path, u):
    P = 0
    for v in path:
        if E.rank[v] > E.rank[u]: P |= E.bit[v]
    return (u, P, len(path))
for p in sys.argv[1:]:
    g = pg.read(p); s = [g.succ[v][0] if g.owner[v] == 0 else -1 for v in range(g.n)]
    if os.path.exists(p + ".start"):
        for tok in open(p + ".start").readline().split()[1:]: a, b = map(int, tok.split(":")); s[a] = b
    E = Engine(g); lam0 = None; k = 0; hist = []; c1 = v1 = c2 = v2 = 0; maxk = 0
    while True:
        vs, _ = E.evaluate(tuple(s)); lam = tuple(vs[v][0] for v in range(g.n))
        if lam != lam0: lam0 = lam; k = 0; hist = []
        paths, cyc = paths_of(g, s, E, vs); hist.append(paths)
        Is = E.improving(tuple(s), vs)
        for (x, z) in Is:
            pz = paths[z]; c = vs[z][0]
            if x in pz or x in cyc[c]: continue
            c1 += 1
            if len(pz) + 1 <= k: v1 += 1; print("C1 VIOLATION", os.path.basename(p), dict(k=k, x=x, z=z, pathlen=len(pz)))
        for j, pj in enumerate(hist):
            for x in range(g.n):
                if g.owner[x] != 0: continue
                for z in g.succ[x]:
                    pz = pj[z]
                    if x in pz or lam[z] == x or len(pz) + 1 > k: continue   # x,π^j_z must be a simple path to a cycle node u != x
                    u = vs[z][0] if j == len(hist) - 1 else None
                    # cycle node of z at step j: recompute from hist? paths store only the path; cycle node = successor of last path vertex at step j is not stored; use current lam (phase-invariant)
                    u = lam[z]
                    c2 += 1
                    if E.key(vs[x]) < E.key(value_of(E, [x] + pz, u)): v2 += 1; print("C2 VIOLATION", os.path.basename(p), dict(k=k, j=j, x=x, z=z))
        ns, _, _ = sbstep(g, E, s)
        if ns is None or ns == s: break
        s = ns; k += 1; maxk = max(maxk, k)
    print(f"{os.path.basename(p)} n={g.n} rule={'n5.py' if os.environ.get('EXACT') == '1' else 'sbstep fixpoint'} longest in-phase k {maxk} | C1 checks {c1} violations {v1} | C2 checks {c2} violations {v2}")
