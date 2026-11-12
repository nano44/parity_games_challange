#!/usr/bin/env python3
"""L-RED 66 R234: DEPTH-COUNT3 (L-SI 51 box 100 §3) on Gamma3 HOW3 runs (engine r232/how3_232, env LNEW).
For every vertex v and step t -> t+1 with Omega_t(v) != Omega_(t+1)(v), the change kind (box 100 §3): LAM (Lambda changes), PI depth d
(d = #elements of Pi_t above z), LEN (Pi equal; box 100 sets depth = |Pi_t|).  P-rise := the c+1 most relevant elements of Pi change.
Counters (unit: vertex change; set: the HOW3 run of each instance; scope: every Gamma3 vertex, and the faces pe/pbeta of every gate):
  lenshallow   = LEN changes with |Pi_t| <= c (depth in [0, c] by the definition, but P does NOT rise: the case §3's proof omits)
  shallow_noP  = changes of depth in [0, c] with no P-rise (must equal lenshallow if the rest of §3's proof is right; must-0 for PI kinds)
  maxcnt / bound = max over v of #changes of depth in [0, c] vs n3 (S_c(n3) - 1) (descriptive)
  twocross_unm = gate flips whose left face keeps its value (TWO-CROSS (i), must-0); ctrl_to_unm = same for the face Odd moves TO
                 (control, fires when TWO-CROSS is not vacuous)
  charged_lenshallow = gate flips that TWO-CROSS charges (face Odd leaves) to a LEN change with |Pi| <= c
CMAX = c (default 3). Usage: d234.py G.json ... | d234.py rand SEED COUNT"""
import sys, os, json
from math import comb
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r232"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r221q"))
import how3_232 as H, own
c = int(os.environ.get("CMAX", "3"))
def kind(vj, A, B):
    if A[0] != B[0]: return ("LAM", -1)
    d = A[1] ^ B[1]
    if d:
        z = max(d, key=lambda u: vj.rk[u]); return ("PI", sum(1 for u in A[1] if vj.rk[u] > vj.rk[z]))
    return ("LEN", len(A[1]))
def top(vj, S): return frozenset(sorted(S, key=lambda u: -vj.rk[u])[:c + 1])
def items():
    if sys.argv[1] == "rand":     # random genomes from L-RED's own generator (r231/dep231.rgen), as r232/rand232.py
        import random; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r231")); from dep231 import rgen
        rng = random.Random(int(sys.argv[2]))
        for i in range(int(sys.argv[3])): yield "r%d" % i, rgen(rng, rng.randint(1, 5), rng.randint(1, 4), rng.choice([2, 3, 4]))
    else:
        for fn in sys.argv[1:]:
            G = json.load(open(fn)); G = G.get("genome", G); G.pop("_evals", None); yield fn, G
TOT = {}
for fn, G in items():
    full = []; seq = H.how3(G, full=full); gm, sig0, tau0, V, O = H.build(G); n = gm.n; vj = own.VJ(gm.prio)
    faces = {V[(p, q)] for q in O for p in ("pe", "pbeta")}
    r = dict(n3=n, T3=len(seq) - 1, lenshallow=0, lenshallow_face=0, shallow_noP_PI=0, charged_lenshallow=0, charged_total=0, twocross_unm=0, ctrl_to_unm=0)
    cnt = [0] * n
    for t in range(len(full) - 1):
        A, B = full[t][0], full[t + 1][0]
        for v in range(n):
            if A[v] == B[v]: continue
            k, d = kind(vj, A[v], B[v])
            if k != "LAM" and d <= c:
                cnt[v] += 1
                if top(vj, A[v][1]) == top(vj, B[v][1]):
                    if k == "LEN": r["lenshallow"] += 1; r["lenshallow_face"] += v in faces
                    else: r["shallow_noP_PI"] += 1
        for q in O:
            g = V[("g", q)]; a, b = full[t][1][g], full[t + 1][1][g]
            if a != b:
                r["charged_total"] += 1
                if A[a] == B[a]: r["twocross_unm"] += 1          # TWO-CROSS (i): the face Odd leaves must change (must-0)
                if A[b] == B[b]: r["ctrl_to_unm"] += 1           # control: the face Odd moves TO need not change (fires)
                k, d = kind(vj, A[a], B[a])
                if k == "LEN" and d <= c: r["charged_lenshallow"] += 1
    S = sum(comb(n, j) for j in range(c + 2)); r["maxcnt"] = max(cnt); r["bound"] = n * (S - 1)
    for k in ("lenshallow", "lenshallow_face", "shallow_noP_PI", "charged_lenshallow", "charged_total", "twocross_unm", "ctrl_to_unm"):
        TOT[k] = TOT.get(k, 0) + r[k]
    TOT["n"] = TOT.get("n", 0) + 1
    if sys.argv[1] != "rand" or r["lenshallow"] or r["twocross_unm"]: print(os.path.basename(fn), r, flush=True)
print("TOTAL", TOT, flush=True)
