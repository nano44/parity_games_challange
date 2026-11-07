#!/usr/bin/env python3
"""L-LOWER 7 (BOX L7) §7: search wirings for a fixed target trajectory (sched.schedule). Score = number of conditions the SOFT greedy
drops (when no option is unanimous it takes the option with the largest majority and drops the minority conditions); score 0 =
realizable (then the greedy is exact, GREEDY-COMPLETE). Simulated annealing over the option targets (mover or exit, acyclic).
Optional guard: no Ξ-path from mover Q into the set P. Usage: wsearch.py h steps seed [Q P1,P2] -> prints best score; writes the
best realizable genome to wsearch_h<h>_s<seed>.txt when the score reaches 0."""
import sys, os, random, math
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, '..', 'l6')); sys.path.insert(0, H)
from sim6 import topo, run, Fprof, caps, wr
from ranksolve import constraints, solve
from sched import schedule
def soft(cons, nopt):
    C = []
    for t, x, p, A, B in cons: C.append({m: (1 if ((m in B) == (p == 1)) else 0) for m in A ^ B})
    openc = set(range(len(C))); by = {}
    for i, r in enumerate(C):
        for m in r: by.setdefault(m, set()).add(i)
    left = set(by); dropped = 0
    while openc:
        best = None
        for m in left:
            cnt = [0, 0]
            for i in by[m]:
                if i in openc: cnt[C[i][m]] += 1
            if cnt[0] + cnt[1] == 0: continue
            sc = (min(cnt), -max(cnt))
            if best is None or sc < best[0]: best = (sc, m, 0 if cnt[0] >= cnt[1] else 1)
            if sc[0] == 0 and False: break
        if best is None: break
        (mn, _), m, sg = best; left.discard(m)
        for i in list(by[m]):
            if i in openc:
                if C[i][m] != sg: dropped += 1
                openc.discard(i)
    return dropped
def clos(xt, x):
    seen = set(); st = [x]
    while st:
        z = st.pop()
        for k in (0, 1):
            y = xt[2 * z + k]
            if y >= 0 and y not in seen: seen.add(y); st.append(y)
    return seen
def main():
    h, steps, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed)
    Q = int(sys.argv[4]) if len(sys.argv) > 4 else None; P = set(map(int, sys.argv[5].split(','))) if len(sys.argv) > 5 else set()
    D, S = schedule(h); N = 2 * D['d']
    def score(xt):
        E = dict(D); E['xt'] = xt
        if topo(E) is None: return None
        if Q is not None and clos(xt, Q) & P: return None
        return soft(constraints(E, S), 2 * N)
    while True:
        xt = [rng.randrange(-1, N) for _ in range(2 * N)]
        for x in range(N):
            for k in (0, 1):
                if xt[2 * x + k] == x: xt[2 * x + k] = -1
        sc = score(xt)
        if sc is not None: break
    best = (sc, list(xt)); temp = 2.0
    for it in range(steps):
        m = rng.randrange(2 * N); y = rng.randrange(-1, N)
        if y == m // 2: continue
        nx = list(xt); nx[m] = y; ns = score(nx)
        if ns is None: continue
        if ns <= sc or rng.random() < math.exp((sc - ns) / temp): xt, sc = nx, ns
        if sc < best[0]: best = (sc, list(xt))
        temp = max(0.05, temp * 0.9995)
        if best[0] == 0: break
    print('h', h, 'seed', seed, 'steps', it + 1, 'best dropped conditions', best[0], 'xt', best[1])
    if best[0] == 0:
        E = dict(D); E['xt'] = best[1]; res, core = solve(constraints(E, S), 2 * N); E['br'], E['bp'] = res
        S2, O2 = run(E); F = Fprof(E, O2); print('   realized: trajectory reproduced', S2[:len(S)] == S, 'F', F, 'caps', caps(F))
        wr(E, os.path.join(H, 'wsearch_h%d_s%d.txt' % (h, seed)))
main()
