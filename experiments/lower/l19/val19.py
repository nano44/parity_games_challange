#!/usr/bin/env python3
"""L-LOWER 19: checker-mode validation of enc19 against box 217's simulator (one217.OneP, key rule).
For COUNT random degree-2 genomes on width profile W (levels numbered as enc19 does; Xi-targets to smaller index or exit, as
eg195 'acyc'), the genome is fixed by unit clauses (enc19 env FIXG form) and the run is unrolled L steps:
  (1) SAT, and the encoder's states s_0..s_L equal one217's key run padded with its last state (fixed point repeats);
  (2) forcing one bit of s_t (t = the first step where the run moves, or 1) to the wrong value: UNSAT.
Usage: val19.py ONE217_DIR W L COUNT SEED     (ONE217_DIR = a checkout of claude/l-new a32a588d's experiments/new/box217)"""
import sys, os, json, random
d217, W, L, cnt, seed = sys.argv[1], [int(v) for v in sys.argv[2].split(',')], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
sys.path.insert(0, d217); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import one217, enc19
from pysat.solvers import Solver
rng = random.Random(seed); lev = [l for l, w in enumerate(W) for _ in range(w)]; N = len(lev); M = 2 * N
bad = 0; tested = 0; Tmax = 0
for i in range(cnt):
    opts = []
    for x in range(N):
        oo = []
        for k in (0, 1):
            wt = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1
            xt = rng.choice(list(range(x)) + [-1, -1])
            oo.append([wt, xt, 2 * x + k])
        opts.append(oo)
    perm = list(range(M)); rng.shuffle(perm); br = list(range(M)); rng.shuffle(br)
    G = {"N": N, "lev": lev, "opts": opts, "gate": [[perm[2 * x], perm[2 * x + 1]] for x in range(N)], "br": br,
         "bp": [rng.randrange(2) for _ in range(M)], "start": [rng.randrange(2) for _ in range(N)]}
    S = one217.OneP(G).run("key"); Tmax = max(Tmax, len(S) - 1)
    ref = [tuple(s) for s in S][:L + 1]; ref += [ref[-1]] * (L + 1 - len(ref))
    E, info, V = enc19.build(W, L, 'free', fixg=G)
    sv = Solver(name='cadical195', bootstrap_with=E.cl); ok = sv.solve()
    if not ok: bad += 1; print('genome', i, 'UNSAT in checker mode (BAD)'); continue
    _, st = enc19.decode(sv.get_model(), V, N, M, lev)
    if st != ref: bad += 1; print('genome', i, 'state mismatch (BAD)', 'T', len(S) - 1); continue
    t = next((t for t in range(1, L + 1) if ref[t] != ref[t - 1]), 1); x = 0
    lit = V['S'][t][x]; ok2 = sv.solve(assumptions=[-lit if ref[t][x] else lit])
    if ok2: bad += 1; print('genome', i, 'wrong state accepted (BAD)')
    tested += 1
print(f'VAL19 W {W} L {L} genomes {cnt} tested {tested} bad {bad} maxT(sim) {Tmax}')
