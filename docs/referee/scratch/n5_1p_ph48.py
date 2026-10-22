#!/usr/bin/env python3
"""REFEREE: Lemma P on ph_n48's long phase (R2's G-1P-7), on n5.py's OWN sigma sequence (replayed unmodified via n5_1p_probe.n5_trajectory),
restricted to simple paths of at most LMAX edges (full enumeration at n = 48 is infeasible). Usage: n5_1p_ph48.py game.pg LMAX"""
import sys, os, functools, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "experiments", "harness"))
import pg, n5_1p_probe as P
path, LMAX = sys.argv[1], int(sys.argv[2])
g = pg.read(path); n = g.n; owner = list(g.owner); succ = [sorted(set(s)) for s in g.succ]; prio = list(g.prio)
s0 = [succ[v][0] for v in range(n)]
for tok in open(path + ".start").readline().split()[1:]: a, b = map(int, tok.split(":")); s0[a] = b
it, fb, traj, E = P.n5_trajectory(prio, succ, owner, s0)
seq = [[s[v] if owner[v] == 0 else succ[v][0] for v in range(n)] for s, _ in traj]
print(f"{os.path.basename(path)} n={n} m={sum(len(s) for s in succ)} n5.py iterations={it} fallbacks={fb} strategies in sequence={len(seq)} LMAX={LMAX}", flush=True)
def table(U):
    best = {}
    def rec(u, x0, v, pathl, seen):
        if len(pathl) > LMAX: return
        for w in succ[v]:
            if w == u:
                Pset = frozenset(q for q in pathl if prio[q] > prio[u]); val = (u, Pset, len(pathl)); k = (u, x0, len(pathl))
                if k not in best or P.cmp_val(prio, val, best[k]) > 0: best[k] = val
            elif w not in seen and len(pathl) < LMAX:
                rec(u, x0, w, pathl + [w], seen | {w})
    for u in U:
        for x in range(n):
            if x != u: rec(u, x, x, [x], {x})
    return best
vals = [P.valuation(prio, s, n) for s in seq]
lams = [tuple(v[0] for v in Om) for Om in vals]
k = 0; checks = viol = 0; phases = []; start = 0; t0 = time.time()
best = table(set(lams[0]))
for j in range(len(seq)):
    if j > 0 and lams[j] != lams[j - 1]:
        phases.append((start, j - 1)); start = j; k = 0; best = table(set(lams[j]))
    elif j > 0: k += 1
    for (u, x, L), val in best.items():
        if L <= k:
            checks += 1
            if P.cmp_val(prio, vals[j][x], val) < 0: viol += 1; print("LEMMA P VIOLATION", dict(step=j, k=k, x=x, u=u, L=L, Om=vals[j][x], path=val))
phases.append((start, len(seq) - 1))
vc = [sum(1 for j in range(a, b) if vals[j + 1] != vals[j]) for a, b in phases]
print(f"phases (first,last strategy index)={phases} in-phase value-changing steps={vc} max={max(vc)} (n-1={n-1}); Lemma P checks (paths of <= {LMAX} edges)={checks} violations={viol} time={time.time()-t0:.0f}s")
