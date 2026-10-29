#!/usr/bin/env python3
"""L-SI box 34 (docs/si/N5-CARX-box34.md): Odd-side carries NM^U (R85 / R86 F3, on G^d) per vertex per lambda^U-run, on plain N5
(box21/n5x.trace). Shows the vertices with the most carries, their labels, whether they are class-X options (box 33), and for the top
vertex its P-sequence as label sets (SHOW=1). Usage: carx.py GAME.pg [START]"""
import sys, os, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "chg"))
from n5x import load, trace, Engine, dual, readstart
from compose import matched, bits
args = [a for a in sys.argv[1:] if not a.startswith("--")]
g = load(args[0]); n = g.n
lab = {}
for line in open(args[0]):
    m = re.match(r'\s*(\d+)\s+\d+\s+[01]\s+[\d,]+\s*"([^"]*)"', line)
    if m: lab[int(m.group(1))] = m.group(2)
L = lambda v: f"{lab.get(v, v)}({v})"
st, fb = trace(g, readstart(args[1]) if len(args) > 1 else None, check=False)
SIDE = os.environ.get("SIDE", "O")                 # SIDE=E: Even's side (Xi of sigma on G, G's parities); default Odd's U on G^d
Ed = Engine(dual(g)) if SIDE == "O" else Engine(g); T = len(st) - 1
U = [Ed.evaluate(s[1] if SIDE == "O" else s[0])[0] for s in st]
rk2v = {Ed.rank[v]: v for v in range(n)}; odd = lambda r: Ed.par[rk2v[r]] == 1
def kind(a, b):
    if a == b: return None
    if a[0] != b[0]: return "LAM"
    if a[1] == b[1]: return "LEN"
    rc = Ed.rank[a[0]]; w = lambda r: (r - rc) if not odd(r) else -(r - rc)
    return "MAT" if matched(bits(a[1]), bits(b[1]), w, odd) else "CAR"
lam = [tuple(u[v][0] for v in range(n)) for u in U]; runs = [0] + [k + 1 for k in range(T) if lam[k + 1] != lam[k]]
best = []
for i, j in zip(runs, runs[1:] + [T + 1]):
    nm = Counter()
    for t in range(i, j - 1):
        for x in range(n):
            if kind(U[t][x], U[t + 1][x]) == "CAR": nm[x] += 1
    for x, c in nm.items(): best.append((c, x, i, j))
best.sort(reverse=True)
print(f"CARX {os.path.basename(args[0])} n {n} iter {T} runs {len(runs)} top: " + " ".join(f"{L(x)}:{c}@[{i},{j})" for c, x, i, j in best[:8]))
if os.environ.get("SHOW") and best:
    c, x, i, j = best[0]; S = lambda m: "{" + ",".join(L(rk2v[r]) for r in sorted(bits(m), reverse=True)) + "}"
    for t in range(i, j - 1):
        k = kind(U[t][x], U[t + 1][x])
        if k in ("CAR", "MAT"):
            a, b = bits(U[t][x][1]), bits(U[t + 1][x][1])
            print(t, k, "out", [L(rk2v[r]) + ("o" if odd(r) else "e") for r in sorted(a - b, reverse=True)], "in", [L(rk2v[r]) + ("o" if odd(r) else "e") for r in sorted(b - a, reverse=True)], "tau-chg", [L(v) for v in range(n) if st[t][1][v] != st[t + 1][1][v]][:6])
# CONJECTURE CARRY-CLIMB (box 34): inside a lambda^U-run, between consecutive MATCHED P-changes of U(x), the carries' entering tops
# (max rank of B \ A, -1 if empty) strictly increase. Counters: climbs, CLIMB_V, longest climb (carries), most climbs of one vertex.
MUT = "--mut" in sys.argv; cv = 0; ncl = 0; lmax = 0; climbs_x = 0; ex = None
for i, j in zip(runs, runs[1:] + [T + 1]):
    for x in range(n):
        seq = []; cnt = 1
        for t in range(i, j - 1):
            k = kind(U[t][x], U[t + 1][x])
            if k == "MAT": seq = []; cnt += 1
            elif k == "CAR":
                a, b = bits(U[t][x][1]), bits(U[t + 1][x][1]); top = max(b - a, default=-1)
                if seq and (top <= seq[-1]) ^ MUT: cv += 1; ex = ex or (x, i, t, seq[-1], top)
                seq.append(top); lmax = max(lmax, len(seq))
        ncl += cnt; climbs_x = max(climbs_x, cnt)
print(f"CLIMB {os.path.basename(args[0])} n {n} CLIMB_V {cv} longest_climb {lmax} max_climbs_per_vertex {climbs_x} ex {ex} {'PASS' if cv == 0 else 'FAIL'}")
# per-sweep carry counts of the max-NM vertex (sweeps separated by MATCHED P-changes / lambda^U-run ends)
c, x, i, j = best[0] if best else (0, 0, 0, 1); sw = [0]
for t in range(i, j - 1):
    k = kind(U[t][x], U[t + 1][x])
    if k == "MAT": sw.append(0)
    elif k == "CAR": sw[-1] += 1
print(f"SWEEPS {os.path.basename(args[0])} vertex {L(x)} NM {c} sweeps {sw}")
# CONJECTURES CARRY-SEG and SWEEP-GAIN (box 34). Per lambda^U-run and vertex x: carries between consecutive MATCHED P-changes <= n - 1
# (SEG_V otherwise); Phi (R85's signed position weight, G^d parities, positions relative to x's cycle node) at the states right after
# successive MATCHED P-changes strictly increases (GAIN_V otherwise). Together they would give PCH = O(n^3) (sweeps <= Phi's range).
D = os.environ.get("PHID", "1")                     # box 35: Phi_d (positions to the power d); "w" = S1's exact weight (Ed.weight)
def phi(val):
    if D == "w": return Ed.weight(val[1])
    rc = Ed.rank[val[0]]; d = int(D); return sum((r - rc) ** d if not odd(r) else -((r - rc) ** d) for r in bits(val[1]))
segv = gainv = 0; segmax = 0; exs = exg = None
for i, j in zip(runs, runs[1:] + [T + 1]):
    for x in range(n):
        car = 0; last = None
        for t in range(i, j - 1):
            k = kind(U[t][x], U[t + 1][x])
            if k == "CAR":
                car += 1; segmax = max(segmax, car)
                if car > n - 1: segv += 1; exs = exs or (x, i, t, car)
            elif k == "MAT":
                car = 0; p = phi(U[t + 1][x])
                if last is not None and (p <= last) ^ MUT: gainv += 1; exg = exg or (x, i, t, last, p)
                last = p
print(f"SWEEPGAIN{SIDE} {os.path.basename(args[0])} n {n} SEG_V {segv} longest_seg {segmax} GAIN_V {gainv} exs {exs} exg {exg} {'PASS' if segv == gainv == 0 else 'FAIL'}")
