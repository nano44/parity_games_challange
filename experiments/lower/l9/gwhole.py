#!/usr/bin/env python3
"""L-LOWER 9: one hsat.py instance (h, d, alpha, gate case), solved WHOLE (no cubes) by a second solver, pysat Glucose4, with a wall
time limit. Result line appended to l9/out/sat/<instance>.g4.res. UNSAT: CNF + DRUP proof written to OUTDIR (for l8/sat/drup.c).
SAT: decoded genome re-simulated by sim6, genome appended to the .res file. Skips an instance already decided there.
Usage: gwhole.py h d alpha gate tlimit_s OUTDIR"""
import sys, os, threading, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, '..', 'l8')); sys.path.insert(0, os.path.join(H, '..', 'l6'))
from hsat import build, decode
from sim6 import run, Fprof, caps
from pysat.solvers import Glucose4
h, d = int(sys.argv[1]), int(sys.argv[2]); al = list(map(int, sys.argv[3].split(','))); gp = tuple(map(int, sys.argv[4].split(','))) if sys.argv[4] != '-' else ()
tl = float(sys.argv[5]); out = sys.argv[6]
name = f"h{h}d{d}_a{''.join(map(str, al))}_g{''.join(map(str, gp)) or 'x'}"; res = os.path.join(H, 'out', 'sat', name + '.g4.res')
if os.path.exists(res) and any(w in open(res).read() for w in (' SAT ', ' UNSAT ')): print(name, 'already decided'); sys.exit(0)
c, E, SG, R, St, gate, T, N, M, LS, nc = build(h, d, al, gp)
print(name, 'vars', c.n, 'clauses', len(c.cl), flush=True)
s = Glucose4(bootstrap_with=c.cl, with_proof=True); tm = threading.Timer(tl, s.interrupt); tm.start(); t0 = time.time()
r = s.solve_limited(expect_interrupt=True); tm.cancel(); dt = time.time() - t0
st = 'SAT' if r is True else 'UNSAT' if r is False else 'TIMEOUT'
with open(res, 'a') as f: f.write(f'whole {st} {dt:.0f}s {time.strftime("%H:%MZ", time.gmtime())} vars {c.n} clauses {len(c.cl)}\n')
print(name, st, f'{dt:.0f}s', flush=True)
if st == 'UNSAT':
    with open(os.path.join(out, name + '.cnf'), 'w') as f:
        f.write(f'p cnf {c.n} {len(c.cl)}\n'); f.writelines(' '.join(map(str, cl)) + ' 0\n' for cl in c.cl)
    with open(os.path.join(out, name + '.g4.proof'), 'w') as f: f.writelines(l + '\n' for l in s.get_proof())
if st == 'SAT':
    D, S = decode(s.get_model(), E, SG, R, St, gate, T, N, M, d); S2, O2 = run(D); F = Fprof(D, O2)
    with open(res, 'a') as f:
        f.write(f'decoded: sim6 T {len(S2) - 1} F {F} caps {caps(F)} prefix = target {S2[:len(S)] == S}\n')
        for kk in ('d', 'xt', 'br', 'bp', 'gate', 'start'): f.write(f"GENOME {kk} {D[kk] if kk == 'd' else ' '.join(map(str, D[kk]))}\n")
