#!/usr/bin/env python3
"""L-LOWER 16: two-stage C-element designer (see celem.py). Stage 1: trajectories W1 of C-elements (level L, source = any mover of
the clamped run or its negation, start). Stage 2: W2 = C-elements whose source is a W1 trajectory. Reports, per client, the least
stage at which some trajectory (or its negation) matches the client's required list on rows lo..P. Sources exclude the client and
movers whose clamped trajectory is not usable (none excluded here: acyclicity is checked when the design is built).
env EXCL=movers: drop source movers that are in EXCL or reach a member of EXCL (acyclicity for the client).
Usage: celem2.py GENOME TARGET P CLIENTS lo"""
import sys, os, subprocess, ast
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '..', 'l6')); sys.path.insert(0, os.path.join(here, '..', 'l7'))
import sim6, clamp
G, tp, P, CL, lo = sys.argv[1], sys.argv[2], int(sys.argv[3]), [int(c) for c in sys.argv[4].split(',')], int(sys.argv[5])
D = sim6.rd(G); T = open(tp).read().split(); tg = [[int(c) for c in T[2 + i]] for i in range(P + 1)]
tgt = [r + (D['start'][16:] if t == 0 else [0] * 48) for t, r in enumerate(tg)]
S = clamp.runclamp(D, tgt, set(range(16))); K = [sim6.okeys(D, list(s)) for s in S]
keys = {}
for L in range(8, 32):
    k = tuple(K[u][L - 1] for u in range(P + 1)); keys.setdefault(k, L)
def celem(src, key, w0):
    w = [w0]
    for u in range(1, P + 1):
        c = key[u]; w.append(c if (src[u - 1] == c and w[-1] != c) else w[-1])
    return tuple(w)
EXCL = set(int(c) for c in os.environ.get('EXCL', '').split(',') if c)
def reach(b):
    out = set(); st = [b]
    while st:
        y = st.pop()
        for k in (0, 1):
            z = D['xt'][2 * y + k]
            if z >= 0 and z not in out: out.add(z); st.append(z)
    return out
base = {}
for b in range(64):
    if b in EXCL or reach(b) & EXCL: continue
    tr = tuple(S[t][b] for t in range(P + 1))
    for nb in (0, 1): base.setdefault(tuple(v ^ nb for v in tr), ('m', b, nb))
def stage(srcs):
    out = {}
    for tr, why in srcs.items():
        for key, L in keys.items():
            for w0 in (0, 1):
                w = celem(tr, key, w0)
                for nw in (0, 1):
                    ww = tuple(v ^ nw for v in w)
                    if ww not in out and ww not in srcs: out[ww] = ('C', L, w0, nw, why)
    return out
W1 = stage(base); W2 = stage(W1)
print('distinct keys', len(keys), 'base', len(base), 'W1', len(W1), 'W2', len(W2))
for x in CL:
    l = subprocess.run([sys.executable, os.path.join(here, '..', 'l13', 'reqpref.py'), G, tp, str(x), str(P)], capture_output=True, text=True).stdout
    req = [(t, r) for t, r in ast.literal_eval(l[l.index('['):l.index('] |') + 1]) if t >= lo]
    for name, W in (('base', base), ('W1', W1), ('W2', W2)):
        h = [(tr, why) for tr, why in W.items() if all(tr[t] == r for t, r in req)]
        if h:
            print('client', x, 'first stage', name, 'hits', len(h))
            for tr, why in h[:4]: print('   ', ''.join(map(str, tr)), why)
            break
    else: print('client', x, 'no hit up to W2')
