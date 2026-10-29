#!/usr/bin/env python3
"""L-SI box 39 (docs/si/N5-SPANW-box39.md): do span P-changes of a target come with W-changes? Even side, plain N5 run. For every lambda-run
(of Xi) and every pair (v, c), v Even switching into c inside it: span(v, c) = [v's first leave of c, v's last re-entry into c).
Per pair: PCH = transitions of the span at which P(Xi c) changes; CO = those at which W(c) also changes (W_t = val(sigma_t, tau_t) on
G_tau_t, so a tau-change can change W); WCH = span transitions at which W(c) changes; GUIDED = PCH transitions that are S4a steps with
tau constant; MIN = min(PCH, WCH) (the per-pair better of the Xi-charge and the W-charge). Reported: totals, max PCH, max (PCH - WCH), max PCH / (WCH + 1), and the pair attaining max PCH - WCH.
Usage: spanw.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, trace, Engine, readstart
import pg
args = [a for a in sys.argv[1:] if not a.startswith("--")]
g = load(args[0]); n = g.n; E = Engine(g)
st, _ = trace(g, readstart(args[1]) if len(args) > 1 else None, check=False); T = len(st) - 1
S = [tuple(s[0]) for s in st]; TAU = [tuple(s[1]) for s in st]
U = [E.evaluate(s)[0] for s in S]
WE = {}
def Wv(t):
    tau = TAU[t]
    if tau not in WE:
        WE[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]))
    return WE[tau].evaluate(S[t])[0]
W = [Wv(t) for t in range(T + 1)]
lam = [tuple(u[v][0] for v in range(n)) for u in U]; runs = [0] + [k + 1 for k in range(T) if lam[k + 1] != lam[k]]
tot = {"PCH": 0, "CO": 0, "WCH": 0, "TQ": 0}; mx = {"PCH": 0, "DIFF": 0, "RATIO": 0.0}; ex = None; pairs = 0
for i, j in zip(runs, runs[1:] + [T + 1]):
    for v in range(n):
        if g.owner[v] != 0: continue
        sw = [t for t in range(i, j - 1) if S[t + 1][v] != S[t][v]]
        for c in {S[t + 1][v] for t in sw}:
            ent = [t for t in sw if S[t + 1][v] == c]; lv = [t for t in sw if S[t][v] == c]
            if not (lv and ent and max(ent) > lv[0]): continue
            pairs += 1; span = range(lv[0], max(ent))
            P = [t for t in span if U[t][c][1] != U[t + 1][c][1]]
            Wc = [t for t in span if W[t][c] != W[t + 1][c]]
            co = sum(1 for t in P if W[t][c] != W[t + 1][c]); tq = sum(1 for t in P if TAU[t] == TAU[t + 1])
            for k, x in (("PCH", len(P)), ("CO", co), ("WCH", len(Wc)), ("TQ", tq)): tot[k] += x
            mx["MIN"] = max(mx.get("MIN", 0), min(len(P), len(Wc))); mx["ENT"] = max(mx.get("ENT", 0), len(ent))
            mx["PCH"] = max(mx["PCH"], len(P)); mx["RATIO"] = max(mx["RATIO"], len(P) / (len(Wc) + 1))
            if len(P) - len(Wc) > mx["DIFF"]: mx["DIFF"] = len(P) - len(Wc); ex = (v, c, i, len(P), len(Wc), co)
print(f"SPANW {os.path.basename(args[0])} n {n} iter {T} pairs {pairs} PCH {tot['PCH']} CO {tot['CO']} WCH {tot['WCH']} TQ {tot['TQ']} "
      f"maxPCH {mx['PCH']} maxDIFF {mx['DIFF']} maxRATIO {mx['RATIO']:.2f} maxMIN {mx.get('MIN', 0)} maxENT {mx.get('ENT', 0)} ex {ex}")
