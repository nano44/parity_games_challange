#!/usr/bin/env python3
"""L-COMP box 32: replay a (decoded) genome with three engines and test REALIZES(genome, target):
fenc (L-LOWER 9 l9/fenc.c, ENC, exact d <= 64), sim6 (L-LOWER l6/sim6.py, Python big integers), replay30 (box30, my box27/sim.py).
Prints T, caps, F(0..H) per engine, and whether the core rows t = 0..T equal the target (fenc, sim6).
Usage: check32.py GENOME TARGET H"""
import sys, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'box31', 'l-lower'))
import enc32, sim6
gp, tp, H = sys.argv[1], sys.argv[2], int(sys.argv[3])
D = enc32.rdgen(gp); S, nc = enc32.rdtarget(tp); T = len(S) - 1; NC = 2 * H; d = D['d']
def caps(F):
    h = 0
    for l, v in enumerate(F):
        if v == 2 ** (l + 2) - 2: h += 1
        else: break
    return h
o = subprocess.run([os.path.join(HERE, 'bin', 'fenc'), gp], env=dict(os.environ, TRAJ='1'), capture_output=True, text=True).stdout
rows = [list(D['start'])]; Tf = Ff = None
for ln in o.split('\n'):
    w = ln.split()
    if not w: continue
    if w[0] == 'T': Tf = int(w[1]); Ff = list(map(int, w[3:3 + d]))
    elif w[0] != 'CYCLIC': rows.append([int(c) for c in w[1]])
rf = len(rows) - 1 == T and all(r[:NC] == S[t] for t, r in enumerate(rows))
St, O = sim6.run(D); Fs = sim6.Fprof(D, O); rs = len(St) - 1 == T and all(list(St[t][:NC]) == S[t] for t in range(len(St)))
o = subprocess.run([sys.executable, os.path.join(HERE, '..', 'box30', 'replay30.py'), gp], capture_output=True, text=True).stdout
w = o.split(); Tr = int(w[w.index('T') + 1]); Fr = list(map(int, w[w.index('F') + 1:]))
print(f'fenc     T {Tf} caps {caps(Ff)} F {" ".join(map(str, Ff[:H + 2]))} realizes {rf}')
print(f'sim6     T {len(St) - 1} caps {caps(Fs)} F {" ".join(map(str, Fs[:H + 2]))} realizes {rs}')
print(f'replay30 T {Tr} caps {caps(Fr)} F {" ".join(map(str, Fr[:H + 2]))}')
agree = Tf == len(St) - 1 == Tr and Ff == Fs == Fr
print('ENGINES AGREE' if agree else 'ENGINES DISAGREE', '| REALIZES' if (rf and rs) else '| DOES NOT REALIZE')
