#!/usr/bin/env python3
"""L-LOWER 19: T(N) ladder: for every level-width profile W of N movers (all compositions of N; degree 2), T_max(W) = the largest L
with enc19 «len» SAT (s_L != s_(L-1)), found by L = 1, 2, ... until UNSAT; each SAT decode is replayed by rep19 (one217); the
first UNSAT is the certificate (DRUP separately with drup19.py). Usage: tlad19.py ONE217_DIR N OUTDIR [CAP_PER_Q=600] [LMAX=64]
Prints one line per profile and the max."""
import sys, os, subprocess, time
d217, N, od = sys.argv[1], int(sys.argv[2]), sys.argv[3]; cap = int(sys.argv[4]) if len(sys.argv) > 4 else 600
lmax = int(sys.argv[5]) if len(sys.argv) > 5 else 64; here = os.path.dirname(os.path.abspath(__file__))
def comps(n):
    if n == 0: yield []; return
    for f in range(1, n + 1):
        for r in comps(n - f): yield [f] + r
best = (0, None)
for W in comps(N):
    w = ','.join(map(str, W)); L = 1; last = None; verdict = ''
    while L <= lmax:
        t0 = time.time()
        try:
            o = subprocess.run([sys.executable, os.path.join(here, 'enc19.py'), w, str(L), 'len', os.path.join(od, f'T_W{w.replace(",", "")}_L{L}')],
                               capture_output=True, text=True, timeout=cap).stdout
        except subprocess.TimeoutExpired: verdict = f'NO ANSWER at L {L} (cap {cap} s)'; break
        if 'RESULT SAT' in o: last = L; L += 1; continue
        verdict = f'UNSAT at L {L} ({time.time() - t0:.1f} s, solver)'; break
    rep = ''
    if last:
        f = os.path.join(od, f'T_W{w.replace(",", "")}_L{last}')
        rep = subprocess.run([sys.executable, os.path.join(here, 'rep19.py'), d217, f + '.json', f + '.states'], capture_output=True, text=True).stdout.strip()
        rep = rep[rep.index('T_key'):] if 'T_key' in rep else rep
    print(f'TLAD N {N} W {w} T_max >= {last or 0} | {verdict} | replay {rep}', flush=True)
    if last and last > best[0] and 'UNSAT' in verdict: best = (last, w)
print(f'TLAD N {N} max over profiles with a certificate: T = {best[0]} (W {best[1]})')
