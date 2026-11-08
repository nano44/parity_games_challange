#!/usr/bin/env python3
"""L-LOWER 8: resumable cube runner for hsat.py instances (container restarts every ~40 min kill long solves).
Instance (h, d, alpha, gate case) is split into cubes by the start bits of the helper movers 2h..2d-1 (2^(2(d-h)) cubes; each cube
adds the unit clauses of its start bits, so the cubes partition the instance). Each cube: CaDiCaL 1.5.3 (pysat Cadical153) with a
time limit; result line appended to out/sat/<instance>.res (SAT / UNSAT / TIMEOUT); UNSAT cubes write sat/<instance>_c<k>.cnf/.proof
(cube CNF = instance CNF + its units) for DRUP checking. Re-running skips cubes already decided. SAT in any cube: decoded genome,
checked by sim6, printed. CLI: hsat_run.py h d alpha gate [tlimit_s]"""
import sys, os, threading, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from hsat import build, decode
sys.path.insert(0, os.path.join(H, '..', 'l6'))
from sim6 import run, Fprof, caps
from pysat.solvers import Cadical153
h, d = int(sys.argv[1]), int(sys.argv[2]); al = list(map(int, sys.argv[3].split(','))); gp = tuple(map(int, sys.argv[4].split(','))) if sys.argv[4] != '-' else ()
tl = float(sys.argv[5]) if len(sys.argv) > 5 else 1500
name = f"h{h}d{d}_a{''.join(map(str, al))}_g{''.join(map(str, gp)) or 'x'}"; res = os.path.join(H, 'out', 'sat', name + '.res')
done = {}
if os.path.exists(res):
    for ln in open(res):
        w = ln.split()
        if w and w[0] == 'cube' and w[2] in ('SAT', 'UNSAT'): done[int(w[1])] = w[2]
c, E, SG, R, St, gate, T, N, M, LS, nc = build(h, d, al, gp)
hv = [St[0][x] for x in range(2 * h, N)]
print(name, 'vars', c.n, 'clauses', len(c.cl), 'conditions', nc, 'cubes', 2 ** len(hv), 'already decided', len(done), flush=True)
if 'SAT' in done.values(): print('instance already SAT'); sys.exit(0)
for k in range(2 ** len(hv)):
    if k in done: continue
    units = [[v if (k >> i) & 1 else -v] for i, v in enumerate(hv)]
    s = Cadical153(bootstrap_with=c.cl + units, with_proof=True); tm = threading.Timer(tl, s.interrupt); tm.start(); t0 = time.time()
    r = s.solve_limited(expect_interrupt=True); tm.cancel(); dt = time.time() - t0
    st = 'SAT' if r is True else 'UNSAT' if r is False else 'TIMEOUT'
    if st == 'UNSAT':
        base = os.path.join(H, 'sat', f'{name}_c{k}')
        with open(base + '.cnf', 'w') as f:
            f.write(f'p cnf {c.n} {len(c.cl) + len(units)}\n'); f.writelines(' '.join(map(str, cl)) + ' 0\n' for cl in c.cl + units)
        with open(base + '.proof', 'w') as f: f.writelines(l + '\n' for l in s.get_proof())
    with open(res, 'a') as f: f.write(f'cube {k} {st} {dt:.0f}s {time.strftime("%H:%MZ", time.gmtime())}\n')
    print('cube', k, st, f'{dt:.0f}s', flush=True)
    if st == 'SAT':
        D, S = decode(s.get_model(), E, SG, R, St, gate, T, N, M, d); S2, O2 = run(D); F = Fprof(D, O2)
        with open(res, 'a') as f:
            f.write(f'decoded: sim6 T {len(S2) - 1} F {F} caps {caps(F)} prefix = target {S2[:len(S)] == S}\n')
            for kk in ('d', 'xt', 'br', 'bp', 'gate', 'start'): f.write(f"GENOME {kk} {D[kk] if kk == 'd' else ' '.join(map(str, D[kk]))}\n")
        break
    s.delete()
