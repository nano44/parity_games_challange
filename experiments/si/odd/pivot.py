#!/usr/bin/env python3
"""L-SI box 36 (docs/si/N5-PIVOT-box36.md): the PIVOT of a P-change of one vertex's valuation inside a lambda-run (lambda^U-run).
For x and t -> t + 1 with P(Xi_t x) != P(Xi_{t+1} x) and lambda constant: p := the first vertex of x's play at t (sigma, sigma-bar(sigma)
on G; tau, its best reply on G^d for SIDE=O) whose successor differs at t + 1. Lemma PIVOT (lane): the prefix x..p is shared, the new
suffix avoids it, so Delta P(x) = Delta P(p) and the change kind (MATCHED / CARRY) of x equals p's. Counters:
  INH_V    transitions where Delta P(x) != Delta P(p) or the pivot is missing (must be 0; --mut compares with the wrong vertex),
  SW / RP  pivots that are a switch of the improving player / a change of the opponent's best reply,
  PD_V     CONJECTURE PIVOT-DISTINCT: between consecutive MATCHED P-changes of x, the pivots of x's carries are pairwise distinct,
  DP_V     CONJECTURE PIVOT-DEEP: ... their depths (distance from x on the play at t) strictly increase,
  ED_V     CONJECTURE EDGE-DISTINCT: ... the pivot edges (p, new successor of p) are pairwise distinct,
  TQ_MAT   most MATCHED changes of one vertex inside one opponent-quiet stretch (opponent strategy constant) of a lambda-run,
  seg_max  longest carry segment, rp_car carries whose pivot is a reply change.
SHOWX=x prints x's changes with their pivots.
Usage: pivot.py GAME.pg [START]   (SIDE=E: Even's Xi on G; default SIDE=O: Odd's U on G^d)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "chg"))
from n5x import load, trace, Engine, dual, readstart
from compose import matched, bits
args = [a for a in sys.argv[1:] if not a.startswith("--")]; MUT = "--mut" in sys.argv
g = load(args[0]); n = g.n
st, fb = trace(g, readstart(args[1]) if len(args) > 1 else None, check=False)
SIDE = os.environ.get("SIDE", "O"); SHOWX = int(os.environ.get("SHOWX", "-1"))
gg = dual(g) if SIDE == "O" else g; E = Engine(gg); T = len(st) - 1
EV = [E.evaluate(tuple(s[1] if SIDE == "O" else s[0])) for s in st]
U = [ev[0] for ev in EV]
own = 1 if SIDE == "O" else 0                       # owner index of the improving player in g (dual swaps owners)
def nxt(k):
    s = st[k][1] if SIDE == "O" else st[k][0]; rep = EV[k][1]
    return [s[v] if gg.owner[v] == 0 else rep[v] for v in range(n)]
NX = [nxt(k) for k in range(T + 1)]
rk2v = {E.rank[v]: v for v in range(n)}; odd = lambda r: E.par[rk2v[r]] == 1
def kind(a, b):
    if a == b or a[0] != b[0] or a[1] == b[1]: return None
    rc = E.rank[a[0]]; w = lambda r: (r - rc) if not odd(r) else -(r - rc)
    return "MAT" if matched(bits(a[1]), bits(b[1]), w, odd) else "CAR"
lam = [tuple(u[v][0] for v in range(n)) for u in U]; runs = [0] + [k + 1 for k in range(T) if lam[k + 1] != lam[k]]
inh = sw = rp = pdv = dpv = edv = segmax = rpcar = nch = 0; ex = {}; tq = 0; tqx = None
opp = lambda k: tuple(st[k][0] if SIDE == "O" else st[k][1])
for i, j in zip(runs, runs[1:] + [T + 1]):
    for x in range(n):
        seg = []                                     # (pivot, depth) of carries since the last MATCHED change
        qm = 0                                       # MATCHED changes of x since the opponent's strategy last changed
        for t in range(i, j - 1):
            if t > i and opp(t) != opp(t - 1): qm = 0
            k = kind(U[t][x], U[t + 1][x])
            if k is None: continue
            nch += 1; c = U[t][x][0]; v = x; d = 0; seen = set(); p = None
            while v != c and v not in seen:
                seen.add(v)
                if NX[t + 1][v] != NX[t][v]: p = v; break
                v = NX[t][v]; d += 1
            q = (x if p != x else NX[t][x]) if MUT else p
            if p is None or U[t][x][1] ^ U[t + 1][x][1] != U[t][q][1] ^ U[t + 1][q][1]:
                inh += 1; ex.setdefault("INH", (x, t, p)); continue
            if gg.owner[p] == 0: sw += 1
            else: rp += 1
            if SHOWX == x:
                a, b = bits(U[t][x][1]), bits(U[t + 1][x][1]); f = lambda S: sorted(((rk2v[r], "o" if odd(r) else "e") for r in S), key=lambda z: -E.rank[z[0]])
                print("SHOW", x, i, t, k, "pivot", p, "depth", d, NX[t][p], "->", NX[t + 1][p], "out", f(a - b), "in", f(b - a))
            if k == "MAT":
                seg = []; qm += 1
                if qm > tq: tq = qm; tqx = (x, i, t)
                continue
            if gg.owner[p] != 0: rpcar += 1
            if any(p == a for a, _, _ in seg): pdv += 1; ex.setdefault("PD", (x, i, t, p, [a for a, _, _ in seg]))
            if seg and d <= seg[-1][1]: dpv += 1; ex.setdefault("DP", (x, i, t, p, d, seg[-1]))
            e = (p, NX[t + 1][p])
            if any(e == b for _, _, b in seg): edv += 1; ex.setdefault("ED", (x, i, t, e))
            seg.append((p, d, e)); segmax = max(segmax, len(seg))
# Switch-target forms (Lead 21:05Z after L-RED R120): counts only at TARGETS c of switching edges of the improving player inside the
# lambda-run (ENT_R(v, c) > 0 for some v, R86's notation). RESET-LIN-T: #MAT_R(c) <= n; CARRY-SEG-T: carry segments of c <= n - 1;
# PCH-QUAD-T: PCH_R(c) <= n^2 + n. Reported: max over all vertices (ALL) and over targets (T).
imp = lambda k: st[k][1] if SIDE == "O" else st[k][0]
tg = {"MAT": [0, 0], "SEG": [0, 0], "PCH": [0, 0]}; tgx = None
for i, j in zip(runs, runs[1:] + [T + 1]):
    tgt = {imp(t + 1)[v] for t in range(i, j - 1) for v in range(n) if imp(t + 1)[v] != imp(t)[v]}
    for x in range(n):
        ma = pc = cur = sg = 0
        for t in range(i, j - 1):
            k = kind(U[t][x], U[t + 1][x])
            if k: pc += 1
            if k == "MAT": ma += 1; cur = 0
            if k == "CAR": cur += 1; sg = max(sg, cur)
        for key, val in (("MAT", ma), ("SEG", sg), ("PCH", pc)):
            tg[key][0] = max(tg[key][0], val)
            if x in tgt:
                if key == "MAT" and val > tg[key][1]: tgx = (x, i)
                tg[key][1] = max(tg[key][1], val)
print(f"TARGET {os.path.basename(args[0])} side {SIDE} n {n} MAT_ALL {tg['MAT'][0]} MAT_T {tg['MAT'][1]} at {tgx} SEG_ALL {tg['SEG'][0]} "
      f"SEG_T {tg['SEG'][1]} PCH_ALL {tg['PCH'][0]} PCH_T {tg['PCH'][1]} RESETLINT {'PASS' if tg['MAT'][1] <= n else 'FAIL'} "
      f"CARRYSEGT {'PASS' if tg['SEG'][1] <= n - 1 else 'FAIL'} PCHQUADT {'PASS' if tg['PCH'][1] <= n * n + n else 'FAIL'}")
nm = os.path.basename(args[0])
print(f"PIVOT {nm} side {SIDE} n {n} iter {T} changes {nch} INH_V {inh} SW {sw} RP {rp} rp_car {rpcar} seg_max {segmax} "
      f"PD_V {pdv} DP_V {dpv} ED_V {edv} TQ_MAT {tq} at {tqx} ex {ex} {'PASS' if inh == 0 else 'FAIL'}")
