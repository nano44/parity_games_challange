#!/usr/bin/env python3
"""L-RED R187 STABRUN: run real N5 (freeze.run = n5x.step, SPEC S1-S5) on a STAB game from its START and check at EVERY state j:
  TAU   tau_j = W-face (e) at every gate;   SBAR  sigma-bar_j (si.Engine's optimal Odd counterstrategy to sigma_j) = beta at every gate;
  FB    no fallback at transition j;        WEQ   W_j = W_0 at every vertex (W = valuation of the (sigma_j, tau_j) play).
FAITHFUL = the longest prefix of transitions on which all four hold (then the real run IS the IDEAL run with faces fixed by fact,
not by fiat). Also: K, moves per mover, and the IDEAL (fastcyc) step count. Usage: stabrun.py genome.json PAD [-v]"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r170"), os.path.join(H, "..", "..", "new", "box21"), os.path.join(H, "..", "r178")]
from n5x import Engine, dual
from freeze import run
import pg, stab

def analyse(G, pad, cap=5000, kgad=True, esc=True):
    g, sig, tau, gv, ev, bv = stab.build(G, pad, kgad=kgad, esc=esc)
    n = g.n; s = [sig.get(v, -1) for v in range(n)]; t = [tau.get(v, -1) for v in range(n)]
    S, T, F, E = run(g, s, t, cap=cap)
    WE = Engine(pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else [t[v]] for v in range(n)]))
    gates = sorted(gv.values()); inv = {gv[q]: q for q in gv}
    W0 = WE.evaluate(tuple(S[0][v] if g.owner[v] == 0 else -1 for v in range(n)))[0]
    rows = []; faithful = None
    for j in range(len(S)):
        sb = E.evaluate(S[j])[1]
        tauok = all(T[j][x] == ev[inv[x]] for x in gates); sbok = all(sb[x] == bv[inv[x]] for x in gates)
        W = WE.evaluate(tuple(S[j][v] if g.owner[v] == 0 else -1 for v in range(n)))[0] if tauok else None
        weq = W == W0
        rows.append((j, F[j], tauok, sbok, weq, sum(1 for x in gates if sb[x] != bv[inv[x]]), sum(1 for x in gates if T[j][x] != ev[inv[x]]),
                     sum(S[j][v] != S[j - 1][v] for v in range(G["N"])) if j else 0))
        if faithful is None and (not tauok or not sbok or not weq or F[j]): faithful = j - 1 if (j and (F[j] or not weq)) else max(j - 1, 0)
    if faithful is None: faithful = len(S) - 1
    return dict(n=n, K=len(S) - 1, faithful=faithful, rows=rows, S=S, g=g, gv=gv)

if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); pad = int(sys.argv[2]); R = analyse(G, pad, kgad=os.environ.get('KGAD', '1') == '1')
    try:
        import fastcyc; ideal = fastcyc.simulate(G)
    except Exception as e: ideal = repr(e)
    print(f"STAB {os.path.basename(sys.argv[1])} pad {pad} n {R['n']} K {R['K']} FAITHFUL {R['faithful']} IDEAL {ideal}")
    if "-v" in sys.argv:
        for r in R["rows"]: print("  j %d fb %d tau %s sbar %s W %s sbar!=X %d tau!=W %d moves %d" % r)
