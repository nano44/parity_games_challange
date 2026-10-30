#!/usr/bin/env python3
"""L-SI box 38 (docs/si/N5-SPAN-box38.md): window and span forms of the switch-target laws, per pair (v, c) of a switching vertex v of
the improving player and a target c, inside one lambda-run (lambda^U-run on G^d for SIDE=O).
  in-windows  : transitions while sigma(v) = c (from v's entry into c to v's next leave of c),
  out-windows : transitions from a leave of c by v to v's next re-entry into c (closed ones only; the charge of SW-RETURN's proof),
  span        : transitions from v's first leave of c to v's last re-entry into c.
Lemma SPAN (lane): ENT_R(v, c) <= n * (1 + PCH^span_R(v, c)). Counters: SPAN_V (must be 0; --mut drops the n factor and must fire on
a run with length-only re-entries), OUTRISE_V (a closed out-window without a change of Xi(c): must be 0), and, maximised over pairs:
MAT/PCH/SEG in IN-windows, OUT-windows, SPAN (SEG = longest carry run between MATCHED changes, counted inside that set only).
Usage: win.py GAME.pg [START] [--mut]   (SIDE=E | O, default O)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "chg"))
from n5x import load, trace, Engine, dual, readstart
from compose import matched, bits
args = [a for a in sys.argv[1:] if not a.startswith("--")]; MUT = "--mut" in sys.argv
g = load(args[0]); n = g.n
st, _ = trace(g, readstart(args[1]) if len(args) > 1 else None, check=False)
SIDE = os.environ.get("SIDE", "O")
gg = dual(g) if SIDE == "O" else g; E = Engine(gg); T = len(st) - 1
U = [E.evaluate(tuple(s[1] if SIDE == "O" else s[0]))[0] for s in st]
imp = lambda k: st[k][1] if SIDE == "O" else st[k][0]
rk2v = {E.rank[v]: v for v in range(n)}; odd = lambda r: E.par[rk2v[r]] == 1
def kind(a, b):
    if a == b: return None
    if a[0] != b[0]: return "LAM"
    if a[1] == b[1]: return "LEN"
    rc = E.rank[a[0]]; w = lambda r: (r - rc) if not odd(r) else -(r - rc)
    return "MAT" if matched(bits(a[1]), bits(b[1]), w, odd) else "CAR"
lam = [tuple(u[v][0] for v in range(n)) for u in U]; runs = [0] + [k + 1 for k in range(T) if lam[k + 1] != lam[k]]
def stats(c, ts, K):
    ma = pc = cur = sg = 0
    for t in ts:
        k = K[t]
        if k in ("MAT", "CAR"): pc += 1
        if k == "MAT": ma += 1; cur = 0
        if k == "CAR": cur += 1; sg = max(sg, cur)
    return ma, pc, sg
best = {f: [0, 0, 0, None] for f in ("IN", "OUT", "SPAN")}; spanv = outv = pairs = span1 = 0; ex = None; maxent = 0
for i, j in zip(runs, runs[1:] + [T + 1]):
    owners = [v for v in range(n) if gg.owner[v] == 0]
    Kc = {}
    for v in owners:
        sw = [t for t in range(i, j - 1) if imp(t + 1)[v] != imp(t)[v]]
        for c in {imp(t + 1)[v] for t in sw}:
            if c not in Kc: Kc[c] = {t: kind(U[t][c], U[t + 1][c]) for t in range(i, j - 1)}
            K = Kc[c]
            ent = [t for t in sw if imp(t + 1)[v] == c]; lv = [t for t in sw if imp(t)[v] == c]
            pairs += 1; maxent = max(maxent, len(ent))
            on = [imp(t)[v] == c for t in range(i, j)]
            ins = [t for t in range(i, j - 1) if on[t - i] and imp(t + 1)[v] == c]
            outs = []; closed = 0
            for s in lv:
                nxt = [e for e in ent if e > s]
                if nxt:
                    e = nxt[0]; closed += 1; w = list(range(s, e)); outs += w
                    if not any(K[t] is not None for t in w): outv += 1
            span = list(range(lv[0], max(ent))) if lv and ent and max(ent) > lv[0] else []
            pspan = sum(1 for t in span if K[t] in ("MAT", "CAR"))
            if len(ent) > (1 if MUT else n) * (1 + pspan): spanv += 1; ex = ex or (v, c, i, len(ent), pspan)
            if len(ent) > 1 + pspan: span1 += 1               # control: without LEN-MONO's factor n (length-only re-entries)
            for f, ts in (("IN", ins), ("OUT", outs), ("SPAN", span)):
                s3 = stats(c, ts, K)
                for q in range(3):
                    if s3[q] > best[f][q]: best[f][q] = s3[q]; best[f][3] = best[f][3] if q else (v, c, i)
out = " ".join(f"{f}: MAT {b[0]} PCH {b[1]} SEG {b[2]} at {b[3]}" for f, b in best.items())
print(f"WIN {os.path.basename(args[0])} side {SIDE} n {n} pairs {pairs} maxENT {maxent} SPAN_V {spanv} SPAN1 {span1} OUTRISE_V {outv} | {out} | "
      f"RESETLINS {'PASS' if best['SPAN'][0] <= n else 'FAIL'} CARRYSEGS {'PASS' if best['SPAN'][2] <= n - 1 else 'FAIL'} "
      f"ex {ex} {'PASS' if spanv == outv == 0 else 'FAIL'}")
