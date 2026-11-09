#!/usr/bin/env python3
"""L-LOWER 13: replay a decoded genome with two independent simulators (l6/sim6.py and l9/fenc.c with TRAJ=1) and report how many
leading rows of the core TARGET the free run follows (core movers 0..2H-1), plus the run's T and the two simulators' agreement.
Usage: prefcheck.py GENOME TARGET FENC_BINARY"""
import sys, os, subprocess
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '..', 'l6'))
import sim6
G, tp, fe = sys.argv[1:4]
L = open(tp).read().split(); rows, nc = int(L[0]), int(L[1]); S = [L[2 + i] for i in range(rows)]
D = sim6.rd(G); R, O = sim6.run(D, cap=4000)
a = [''.join(map(str, r[:nc])) for r in R]
out = subprocess.run([fe, G], capture_output=True, text=True, env=dict(os.environ, TRAJ='1')).stdout.split('\n')
b = [''.join(map(str, D['start']))[:nc]] + [ln.split()[1][:nc] for ln in out if ln and ln[0].isdigit()]   # fenc prints rows t >= 1
def lead(X):
    k = 0
    while k < len(X) and k < len(S) and X[k] == S[k]: k += 1
    return k
print(os.path.basename(G), 'sim6 T', len(a) - 1, 'fenc T', len(b) - 1, 'sim6==fenc', a == b, 'rows followed (sim6, fenc):', lead(a), lead(b),
      'of target', rows)
