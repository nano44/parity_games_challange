#!/usr/bin/env python3
"""L-SI box 58 §10: CONJECTURE «Odd W-SEP» on data. For an Odd o that changes its choice at u (a re-decision, sigmabar_u(o) = a ->
sigmabar_(u+1)(o) = b), inside a W-run with tau fixed: does W strictly rise at u at one of a, b, tau(o)?
ALL*: every re-decision in a W-run; ESC*: re-decisions of Odd vertices on an escaped cycle (s included) at that escape's transition;
ESCE*: the same, on escaped cycles that contain an Even vertex (W-REOPEN's scope).
*D: those with o in D_u (sigmabar_u(o) != tau(o)) or D_(u+1). *SEP = with a W-rise, *NOSEP = without (the kill candidates).
Also *SEPWIDE: a W-rise at u anywhere on the W-plays of a, b or tau(o) (a weaker form).
Usage: wsep.py GAME.pg [START]"""
import sys, io, contextlib, os
ANC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "anc.py")
argv = sys.argv[1:]; sys.argv = [ANC] + argv
g = {'__file__': ANC, '__name__': 'x'}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(open(ANC).read(), ANC, 'exec'), g)
ROOT, runs, B, S, TAU, Wv, E, n, own, runof = g['ROOT'], g['runs'], g['B'], g['S'], g['TAU'], g['Wv'], g['E'], g['n'], g['own'], g['runof']
K = E.key
def wplay(k, tau, x):
    out, seen = [], set()
    while x not in seen: seen.add(x); out.append(x); x = S[k][x] if own[x] == 0 else tau[x]
    return out
onZ, onZE = set(), set()
for (u, z), r in ROOT.items():
    if r[0] == 'O' and r[2] is not None and u in runof:
        Zq = {(u, q) for q in [r[1]] + r[3] if own[q] == 1}; onZ |= Zq
        if any(own[q] == 0 for q in r[3]): onZE |= Zq
T = {f"{p}{q}": 0 for p in ("ALL", "ESC", "ESCE") for q in ("", "D", "SEP", "NOSEP", "SEPWIDE", "DNOSEP")}
EX = []
for r in runs:
    tau = TAU[r[0]]
    for u in r:
        W0, W1 = Wv(u, tau), Wv(u + 1, tau)
        rise = lambda v: K(W1[v]) > K(W0[v])
        for o in range(n):
            if own[o] != 1 or B[u][o] == B[u + 1][o]: continue
            a, b = B[u][o], B[u + 1][o]; inD = a != tau[o] or b != tau[o]
            sep = rise(a) or rise(b) or rise(tau[o])
            wide = sep or any(rise(q) for y in (a, b, tau[o]) for q in wplay(u, tau, y))
            for p in ("ALL",) + (("ESC",) if (u, o) in onZ else ()) + (("ESCE",) if (u, o) in onZE else ()):
                T[p] += 1; T[p + "D"] += inD; T[p + ("SEP" if sep else "NOSEP")] += 1; T[p + "SEPWIDE"] += wide
                T[p + "DNOSEP"] += inD and not sep
            if (u, o) in onZ and not sep and len(EX) < 3: EX.append((o, u, a, b, tau[o]))
for e in EX: print("ESCNOSEP o", *e)
print(f"WSEP {os.path.basename(argv[0])} " + " ".join(f"{a} {b}" for a, b in T.items()))
