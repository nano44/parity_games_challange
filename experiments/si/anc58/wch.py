#!/usr/bin/env python3
"""L-SI box 58 §11: W-changes per vertex per W-run against |F| and source events (DATA). Per W-run F (tau fixed, lambda_W constant):
LEN = |F|; SRC = R97 source-event transitions (Xi changes at a vertex of D_k u D_(k+1) u C, as srcfuel.py); WCHMAX = max_v WCH_F(v)
(transitions of F at which W(v) changes); WCHSUM = sum_v WCH_F(v); WTRANS = transitions of F with some W-change.
Prints per game the W-run maximising WCHMAX, and the maxima of the ratios WCHMAX / LEN and WCHMAX / (1 + SRC).
Usage: wch.py GAME.pg [START]"""
import sys, io, contextlib, os
ANC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "anc.py")
argv = sys.argv[1:]; sys.argv = [ANC] + argv
g = {'__file__': ANC, '__name__': 'x'}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(open(ANC).read(), ANC, 'exec'), g)
runs, B, S, TAU, Wv, n, own, KEY = g['runs'], g['B'], g['S'], g['TAU'], g['Wv'], g['n'], g['own'], g['KEY']
best, rl, rs = None, 0.0, 0.0
for r in runs:
    tau = TAU[r[0]]; C = {v for v in range(n) if Wv(r[0], tau)[v][0] == v}
    wch = [0] * n; src = wt = 0
    for k in r:
        W0, W1 = Wv(k, tau), Wv(k + 1, tau); ch = [v for v in range(n) if W0[v] != W1[v]]
        for v in ch: wch[v] += 1
        wt += bool(ch)
        D = {o for o in range(n) if own[o] == 1 and (B[k][o] != tau[o] or B[k + 1][o] != tau[o])}
        src += any(KEY[k][v] is not None for v in D | C)
    row = dict(LEN=len(r), SRC=src, WCHMAX=max(wch), WCHSUM=sum(wch), WTRANS=wt)
    rl = max(rl, row['WCHMAX'] / len(r)); rs = max(rs, row['WCHMAX'] / (1 + src))
    if best is None or row['WCHMAX'] > best['WCHMAX']: best = row
best = best or dict(LEN=0, SRC=0, WCHMAX=0, WCHSUM=0, WTRANS=0)
print(f"WCH {os.path.basename(argv[0])} n {n} RUNS {len(runs)} " + " ".join(f"{a} {b}" for a, b in best.items()) + f" RLEN {rl:.3f} RSRC {rs:.3f}")
