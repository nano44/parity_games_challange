#!/usr/bin/env python3
"""L-LOWER 8 (BOX L8 item 1): sequential schedule with PURE helpers, decided exactly. A pure helper has a constant preference p over
its free steps (as both helpers of HS2_d3; Lemma SINK: every sink is pure, but a pure helper may have any wiring): it moves to c_l
exactly at the free steps where c_l = p. So its trajectory is a function of (start bit, p) and its key sequence: 4 per helper mover.
Enumerated: all (start, p) of all helpers and all gate patterns of helper levels h..d-2; for each full trajectory the wiring search
of hsched.py (sink-first, joint ranksolve pruning, memo) decides realizability exactly. Scope: (lower target, d, pure helpers).
CLI: hsched3.py h d alpha [tlimit_s]"""
import sys, os, itertools, time
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..', 'l6')); sys.path.insert(0, os.path.join(H, '..', 'l7')); sys.path.insert(0, H)
from sim6 import okeys, run, Fprof, caps
from ranksolve import solve, constraints
from sched import schedule
from hsched import realize
def gates(d, hl):
    for gp in itertools.product(range(4), repeat=len(hl)):
        gate = [0, 2, 1, 3] + [v for l in range(1, d) for v in (4 * l + 1000, 4 * l + 1001, 4 * l + 1002, 4 * l + 1003)]
        for i, l in enumerate(hl):
            b0, b1 = gp[i] & 1, gp[i] >> 1
            gate[4 * l + 0], gate[4 * l + 2] = (5, 3) if b0 else (3, 5)
            gate[4 * l + 1], gate[4 * l + 3] = (5, 3) if b1 else (3, 5)
        yield gp, gate
def pure_trajs(LS, h, d, gate):
    T = len(LS) - 1; N = 2 * d; D = {'d': d, 'gate': gate}
    def rec(l, S):
        if l == d: yield [tuple(s) for s in S]; return
        c = [okeys(D, list(s) + [0] * (N - len(s)))[l - 1] for s in S]
        for (s0q, pq, s0f, pf) in itertools.product((0, 1), repeat=4):
            cols = []
            for s0, p in ((s0q, pq), (s0f, pf)):
                col = [s0]
                for t in range(1, T + 1):
                    cur = col[-1]; col.append(c[t] if (cur != c[t] and c[t] == p) else cur)
                cols.append(col)
            yield from rec(l + 1, [list(S[t]) + [cols[0][t], cols[1][t]] for t in range(T + 1)])
    yield from rec(h, [list(s) for s in LS])
def main():
    h, d = int(sys.argv[1]), int(sys.argv[2]); al = list(map(int, sys.argv[3].split(','))); tl = float(sys.argv[4]) if len(sys.argv) > 4 else 1e9
    _, LS = schedule(h, alpha=al); LS = [tuple(s[:2 * h]) for s in LS]; t0 = time.time()
    print('h', h, 'd', d, 'alpha', al, 'lower T', len(LS) - 1, 'pure helpers', flush=True)
    tot = 0; stats = {'solve': 0}; seen = set()
    for gp, gate in gates(d, list(range(h, d - 1))):
        for S in pure_trajs(LS, h, d, gate):
            key = (tuple(S), tuple(gate))
            if key in seen: continue
            seen.add(key); tot += 1
            if time.time() - t0 > tl: print('TIMEOUT after', tot, 'trajectories'); return
            xt = realize({'d': d, 'gate': gate}, S, stats)
            if xt is None: continue
            N = 2 * d; E = {'d': d, 'xt': xt, 'br': list(range(2 * N)), 'bp': [0] * (2 * N), 'gate': gate, 'start': list(S[0])}
            (br, bp), _ = solve(constraints(E, S), 2 * N); E['br'], E['bp'] = br, bp
            S2, O2 = run(E); F = Fprof(E, O2)
            print('RESULT REALIZED after', tot, 'trajectories; sim6 T', len(S2) - 1, 'F', F, 'caps', caps(F), 'prefix = target', S2[:len(S)] == S)
            for k in ('d', 'xt', 'br', 'bp', 'gate', 'start'): print('GENOME', k, E[k] if k == 'd' else ' '.join(map(str, E[k])))
            return
    print('RESULT NONE: h', h, 'd', d, 'alpha', al, 'pure-helper trajectories', tot, 'solves', stats['solve'], f'{time.time() - t0:.0f}s')
if __name__ == '__main__': main()
