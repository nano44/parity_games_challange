#!/usr/bin/env python3
"""L-SI box 58 §9: Odd-only escapes (the escaped cycle has no Even vertex), inside W-runs. Per escape of s from x at u:
XCHX  Xi(x) changes at u;  XSW  x is Odd and changes its choice at u;  XCHCL  some vertex of the escaped cycle (other than s) changes Xi at u.
ALLESC / ALLXCHX / ALLSCH: every W-run escape / those with Xi(x) changing / with Xi(s) changing (Lemma ESC-XCH: all).
Per (W-run, s, x): OOMAX the most Odd-only escapes; OOEXCESS escapes beyond the number of Xi(x)-changes in the W-run (bound test: 0?).
Usage: oddonly.py GAME.pg [START]"""
import sys, io, contextlib, os
ANC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "anc.py")
argv = sys.argv[1:]; sys.argv = [ANC] + argv
g = {'__file__': ANC, '__name__': 'x'}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(open(ANC).read(), ANC, 'exec'), g)
ROOT, runs, B, S, KEY, own, runof = g['ROOT'], g['runs'], g['B'], g['S'], g['KEY'], g['own'], g['runof']
T = dict(ALLESC=0, ALLXCHX=0, ALLSCH=0, OO=0, XCHX=0, XSW=0, XCHCL=0, OOMAX=0, OOEXCESS=0)
seen, per = set(), {}
for (u, z), r in ROOT.items():
    if r[0] != 'O' or r[2] is None or u not in runof or (r[1], u) in seen: continue
    seen.add((r[1], u)); s, cl = r[1], r[3]
    T['ALLESC'] += 1; T['ALLXCHX'] += KEY[u][B[u][s]] is not None; T['ALLSCH'] += KEY[u][s] is not None
    if any(own[q] == 0 for q in cl): continue
    x = B[u][s]; T['OO'] += 1
    T['XCHX'] += KEY[u][x] is not None; T['XSW'] += own[x] == 1 and B[u][x] != B[u + 1][x]
    T['XCHCL'] += any(KEY[u][q] is not None for q in cl)
    per.setdefault((runof[u], s, x), []).append(u)
for (ri, s, x), L in per.items():
    xch = sum(1 for k in runs[ri] if KEY[k][x] is not None)
    T['OOMAX'] = max(T['OOMAX'], len(L)); T['OOEXCESS'] += max(0, len(L) - xch)
print(f"ODDONLY {os.path.basename(argv[0])} " + " ".join(f"{a} {b}" for a, b in T.items()))
