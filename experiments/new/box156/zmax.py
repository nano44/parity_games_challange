#!/usr/bin/env python3
"""L-NEW box 156: EXACT z3 search over ALL IDEAL-ACYC genomes of degree <= 2 with N movers (RESULTS R104 model), every start.
Symbolic genome: pi = mover index (Xi-target of option (x,k) is X or a mover y > x: WLOG by relabelling along a topological order);
levels lev(x) in [0, N-1] with a W-target of level lev(x)-1 (none at level 0); degree 1 or 2 (deg1 flag: option 1 never used);
beta of option (x,k): eps = +-2^r, ranks r distinct over the used options (Lemma ENC of R105: Xi-order = integer order of sum eps);
gate indices distinct over all options; key of option = (key of its W-target under the NEW state) * B + gate (lex order of equal-length
tuples = integer order, B = 2N). Run: frame of L steps s_0..s_L, s_(t+1) = Step(s_t) (a fixed point stays fixed, so the run's T =
#{t < L : s_(t+1) != s_t} when L >= T).
Modes: T m       -> is there a genome + start with T >= m ?   (frame L = m)
       M2 L q    -> is there a genome + start with #{t < L : |Mv_t| >= 2} >= q, frame L (L must be >= max T for exactness)
Prints SAT + witness JSON (box 139/150 format) or UNSAT.  Usage: zmax.py N T m [out.json] | zmax.py N M2 L q [out.json]"""
import sys, json, time
from z3 import *
N = int(sys.argv[1]); mode = sys.argv[2]
if mode == "T": L = int(sys.argv[3]); q = None; out = sys.argv[4] if len(sys.argv) > 4 else None
else: L = int(sys.argv[3]); q = int(sys.argv[4]); out = sys.argv[5] if len(sys.argv) > 5 else None
DEG2ONLY = False
import os
if os.environ.get("DEG2"): DEG2ONLY = True
B = 2 * N; M = 2 * N
BV = os.environ.get("BV")
S = SolverFor("QF_BV") if BV else Solver()
import math
VW = M + 2 + max(1, math.ceil(math.log2(N + 1)))   # value width (sum of <= N terms +-2^r, r < M), signed
GW = max(1, math.ceil(math.log2(M)))               # bits per gate; key width GW * N
KW = GW * N + 1
def VI(name): return BitVec(name, VW) if BV else Int(name)
def KI(name): return BitVec(name, KW) if BV else Int(name)
def LT(a, b): return ULT(a, b) if BV else a < b
lev = [Int(f"lev{x}") for x in range(N)]; d1 = [Bool(f"d1_{x}") for x in range(N)]
wt = [[Int(f"wt{x}_{k}") for k in range(2)] for x in range(N)]
xt = [[Int(f"xt{x}_{k}") for k in range(2)] for x in range(N)]   # -1 = X
eps = [[VI(f"eps{x}_{k}") for k in range(2)] for x in range(N)]
mag = [[VI(f"mag{x}_{k}") for k in range(2)] for x in range(N)]
sg = [[Bool(f"sg{x}_{k}") for k in range(2)] for x in range(N)]
gt = [[KI(f"g{x}_{k}") for k in range(2)] for x in range(N)]
for x in range(N):
    S.add(lev[x] >= 0, lev[x] < N)
    if DEG2ONLY: S.add(Not(d1[x]))
    for k in range(2):
        S.add(Or(lev[x] == 0, Or([And(wt[x][k] == y, lev[y] == lev[x] - 1) for y in range(N) if y != x])))
        S.add(Implies(lev[x] == 0, wt[x][k] == -1))
        S.add(Or([xt[x][k] == -1] + [xt[x][k] == y for y in range(x + 1, N)]))
        S.add(Or([mag[x][k] == 2 ** r for r in range(M)]))
        S.add(eps[x][k] == If(sg[x][k], mag[x][k], -mag[x][k]))
        S.add(ULT(gt[x][k], M) if BV else And(gt[x][k] >= 0, gt[x][k] < M))
S.add(Distinct([mag[x][k] for x in range(N) for k in range(2)]))
S.add(Distinct([gt[x][k] for x in range(N) for k in range(2)]))
# symmetry breaking (exact): swapping the two option labels of a mover (and its state bit) maps runs to runs; deg-1 movers use option 0
if not os.environ.get("NOSYM"):
    for x in range(N): S.add(Or(d1[x], gt[x][0] < gt[x][1]))
LEVS = os.environ.get("LEVS")   # optional split: fix the level vector, e.g. LEVS=0,1,1,0,2
if LEVS:
    for x, l in enumerate(map(int, LEVS.split(","))): S.add(lev[x] == l)
LADDER = os.environ.get("LADDER")   # optional class: exactly LADDER movers on every level 0 .. N/LADDER - 1 (2-wide ladder: LADDER=2)
if LADDER:
    w_ = int(LADDER)
    for l in range(N // w_): S.add(Sum([If(lev[x] == l, 1, 0) for x in range(N)]) == w_)
# levels contiguous is implied by W-targets. symmetry: level-0 exists
S.add(Or([lev[x] == 0 for x in range(N)]))
st = [[Bool(f"s{t}_{x}") for x in range(N)] for t in range(L + 1)]
def sel(b, a1, a0): return If(b, a1, a0)
MV = []
for t in range(L + 1):
    # values of options under s_t (Xi-targets later in index order)
    V = [None] * N; opv = [[None, None] for _ in range(N)]
    for x in reversed(range(N)):
        for k in range(2):
            rest = BitVecVal(0, VW) if BV else 0
            for y in range(x + 1, N): rest = If(xt[x][k] == y, V[y], rest)
            opv[x][k] = eps[x][k] + rest
        V[x] = sel(st[t][x], opv[x][1], opv[x][0])
    if t == L: break
    # unstable: other option strictly better (deg 2 only)
    unst = [And(Not(d1[x]), sel(st[t][x], opv[x][0] > opv[x][1], opv[x][1] > opv[x][0])) for x in range(N)]
    # keys under NEW state s_(t+1)
    K = [KI(f"K{t}_{x}") for x in range(N)]
    def okey(x, k):
        base = BitVecVal(0, KW) if BV else 0
        for y in range(N):
            if y != x: base = If(wt[x][k] == y, K[y], base)
        return If(lev[x] == 0, gt[x][k], base * B + gt[x][k])
    for x in range(N):
        k1, k0 = okey(x, 1), okey(x, 0)
        cur, oth = sel(st[t][x], k1, k0), sel(st[t][x], k0, k1)
        mv = And(unst[x], LT(oth, cur))
        S.add(st[t + 1][x] == Xor(st[t][x], mv))
        S.add(K[x] == sel(st[t + 1][x], k1, k0))
    MV.append([Xor(st[t][x], st[t + 1][x]) for x in range(N)])
# deg-1 movers: state fixed to option 0 (harmless: option 1 unused)
for x in range(N): S.add(Implies(d1[x], Not(st[0][x])))
FIX = os.environ.get("FIX")
if FIX:
    F = json.load(open(FIX))
    for x in range(N):
        S.add(lev[x] == F["lev"][x]); S.add(d1[x] == (len(F["opts"][x]) == 1))
        for k, o in enumerate(F["opts"][x]):
            if o[0] >= 0: S.add(wt[x][k] == o[0])
            S.add(xt[x][k] == o[1]); m_ = o[2]; S.add(mag[x][k] == 2 ** F["br"][m_]); S.add(sg[x][k] == (F["bp"][m_] == 0))
            S.add(gt[x][k] == F["gate"][x][k])
        S.add(st[0][x] == (F["start"][x] == 1))
    assert S.check() == sat; mm = S.model()
    print(json.dumps([[1 if is_true(mm.eval(st[t][x], model_completion=True)) else 0 for x in range(N)] for t in range(L + 1)])); sys.exit()
if mode == "T":
    S.add(Or(MV[L - 1]))  # moves at step L  => T >= L (a fixed point stays fixed)
else:
    m2 = [If(And(Sum([If(b, 1, 0) for b in MV[t]]) >= 2, Or(MV[t + 1])), 1, 0) for t in range(L - 1)]  # steps 1..T-1
    S.add(Sum(m2) >= q)
t0 = time.time(); r = S.check(); dt = time.time() - t0
print(f"N={N} mode={mode} L={L} q={q} DEG2ONLY={DEG2ONLY}: {r} ({dt:.1f}s)", flush=True)
if r == sat:
    m = S.model(); ev = lambda e: m.eval(e, model_completion=True)
    levs = [ev(lev[x]).as_long() for x in range(N)]
    opts, gate, br, bp = [], [], [], []
    mags = sorted((ev(mag[x][k]).as_long(), x, k) for x in range(N) for k in range(2))
    rk = {(x, k): i for i, (_, x, k) in enumerate(mags)}
    gs = sorted((ev(gt[x][k]).as_long(), x, k) for x in range(N) for k in range(2)); gr = {(x, k): i for i, (_, x, k) in enumerate(gs)}
    idx = 0; BR, BP = [], []
    for x in range(N):
        D = 1 if is_true(ev(d1[x])) else 2; o = []; g = []
        for k in range(D):
            o.append([ev(wt[x][k]).as_long() if levs[x] > 0 else -1, ev(xt[x][k]).as_long(), idx]); g.append(gr[(x, k)])
            BR.append(rk[(x, k)]); BP.append(0 if is_true(ev(sg[x][k])) else 1); idx += 1
        opts.append(o); gate.append(g)
    start = [1 if is_true(ev(st[0][x])) else 0 for x in range(N)]
    G = {"N": N, "lev": levs, "opts": opts, "gate": gate, "br": BR, "bp": BP, "start": start, "xorder": list(range(N))}
    if out: json.dump(G, open(out, "w"))
    print(json.dumps(G), flush=True)
