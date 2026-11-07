#!/usr/bin/env python3
"""L-LOWER 7 (BOX L7) §7: exhaustive over all acyclic wirings of d = 2 (no self-targets): is the sequential h = 2 target (sched.py,
alpha given as e.g. 1,0) realizable with ranks and signs free (GREEDY-COMPLETE)? Also counts which movers have infeasible own conditions."""
import sys, os, itertools
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, '..', 'l6')); sys.path.insert(0, H)
from sim6 import topo
from ranksolve import constraints, solve
from sched import schedule
from collections import Counter, defaultdict
AL = list(map(int, sys.argv[1].split(","))) if len(sys.argv) > 1 else [1, 1]
D, S = schedule(2, alpha=AL); N = 4; print('trajectory', S)
ok = 0; tot = 0; own = Counter()
for xt in itertools.product(range(-1, N), repeat=2 * N):
    if any(xt[m] == m // 2 for m in range(2 * N)): continue
    E = dict(D); E['xt'] = list(xt)
    if topo(E) is None: continue
    tot += 1; cons = constraints(E, S); by = defaultdict(list)
    for c in cons: by[c[1]].append(c)
    bad = tuple(x for x in range(N) if solve(by[x], 2 * N)[0] is None)
    own[bad] += 1
    if not bad and solve(cons, 2 * N)[0] is not None: ok += 1
print('acyclic wirings', tot, 'realizable', ok); print('movers with infeasible own conditions -> #wirings:', own.most_common(8))
