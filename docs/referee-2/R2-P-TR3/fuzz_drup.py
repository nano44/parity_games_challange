#!/usr/bin/env python3
"""REFEREE-2 succ. 28: soundness / sanity fuzz of L-COMP's drup.c (and of my r2rup.c, same harness). Usage: fuzz_drup.py DRUP_BINARY SEED N
Random small CNFs (n <= 9 vars); proofs of four kinds: (G) Glucose 4 proofs of UNSAT formulas (completeness sanity),
(R) random lemma sequences with random deletions (soundness: any VERIFIED must be UNSAT by brute force),
(M) Glucose proofs mutated (lines dropped / literals flipped / lemmas injected), (S) SAT formulas with any proof.
Soundness criterion: drup prints «s VERIFIED» only on brute-force UNSAT formulas. Both deletion modes (default, IGNDEL=1)."""
import random, subprocess, sys, os, itertools, tempfile
from pysat.solvers import Solver
drup, seed, N = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); R = random.Random(seed)
td = tempfile.mkdtemp()
def unsat(n, F):
    for bits in range(1 << n):
        if all(any((l > 0) == bool(bits >> (abs(l) - 1) & 1) for l in c) for c in F): return False
    return True
def run(F, n, proof, igndel):
    fc, fp = os.path.join(td, 'f.cnf'), os.path.join(td, 'p.drup')
    open(fc, 'w').write(f"p cnf {n} {len(F)}\n" + "".join(" ".join(map(str, c)) + " 0\n" for c in F))
    open(fp, 'w').write("".join(l + "\n" for l in proof))
    env = dict(os.environ); env.pop('IGNDEL', None)
    if igndel: env['IGNDEL'] = '1'
    o = subprocess.run([drup, fc, fp], capture_output=True, text=True, env=env).stdout
    return o.startswith('s VERIFIED') or o.startswith('R2RUP VERIFIED')
cnt = {k: [0, 0] for k in 'GRMS'}; unsound = 0; incomplete_G = 0
for it in range(N):
    n = R.randint(2, 9); m = R.randint(1, 5 * n)
    F = [sorted({R.choice([-1, 1]) * R.randint(1, n) for _ in range(R.randint(1, 3))}) for _ in range(m)]
    U = unsat(n, F)
    s = Solver(name='glucose4', bootstrap_with=F, with_proof=True); sat = s.solve(); pf = s.get_proof() or []; s.delete()
    kinds = []
    if U: kinds.append(('G', pf))
    lem = []
    for _ in range(R.randint(0, 12)):
        c = sorted({R.choice([-1, 1]) * R.randint(1, n) for _ in range(R.randint(0, 3))})
        lem.append(('d ' if R.random() < 0.2 else '') + " ".join(map(str, c)) + " 0")
    kinds.append(('R', lem))
    if pf:
        mp = list(pf); op = R.choice(['drop', 'flip', 'inject'])
        i = R.randrange(len(mp))
        if op == 'drop': del mp[i]
        elif op == 'flip':
            t = mp[i].split()
            js = [j for j, x in enumerate(t) if x not in ('d', '0')]
            if js: j = R.choice(js); t[j] = str(-int(t[j])); mp[i] = " ".join(t)
        else: mp.insert(i, " ".join(str(R.choice([-1, 1]) * R.randint(1, n)) for _ in range(R.randint(0, 2))) + " 0")
        kinds.append(('M', mp))
    if not U: kinds.append(('S', pf + ['0']))
    for k, p in kinds:
        for ig in (False, True):
            v = run(F, n, p, ig); cnt[k][0] += 1; cnt[k][1] += v
            if v and not U: unsound += 1; print('UNSOUND', k, ig, F, p)
            if k == 'G' and not v and not ig: incomplete_G += 1
print('SEED', seed, 'formulas', N, ' '.join(f'{k}: runs {a} verified {b}' for k, (a, b) in cnt.items()),
      'UNSOUND', unsound, 'G proofs rejected (default mode)', incomplete_G)
