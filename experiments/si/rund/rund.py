#!/usr/bin/env python3
"""L-SI box 17: DATA for RUN_D (docs/si/N5-RUND-box17.md). Twin terminal changes along fallback-free in-phase runs of N5 (n5x.py step,
read-only). A terminal change of v at k -> k+1 (both states in one phase, k not a fallback): v in R_D at k and k+1, u_k(v) != u_{k+1}(v)
(u(v) := the first D_k vertex on v's (sigma_k, tau)-play). TWIN: lambda_W(v) unchanged (TC-CN, N5-2O-T-box16 §8). Per twin change it
records:
  dch    D_k != D_{k+1}
  wsame  W_k(v) == W_{k+1}(v) (full value; WM-G gives W_{k+1}(v) >= W_k(v))
  lw     lev(W_k(v), W_{k+1}(v)): the top rank where v's W path set changes (-1: only the length changes; -2: equal)
  LW     the twin level top(P(W_k(u)) sym-diff P(W_k(u'))) at state k (u = old gate, u' = new gate; -1 if equal sets)
  M      max_S M_D over the run (if (h3_D) at every state of the run; else None); post = the change is at a state >= k_0 + n - 1
Checks:
  WMG_V  W_{k+1}(v) < W_k(v) in the S1 order at a twin change (WM-G predicts 0)
  FRZ_V  post and (h3_D) on the run and lw > L* := max(M, -1) (FRZ-U_H3 predicts 0)
Counts the twin changes per run and per (run, vertex), split by (dch, wsame, lw vs LW, lw vs L*).
MUT=1 control: FRZ test at L* - 1 (must fail when the data reach it).
Usage: rund.py --list FILE [KMIN] | --rand COUNT NLO NHI SEED | --one GAME [START.json] (random C^kO from multi.py; odd #: S3 start, even #:
random start pair)."""
import sys, os, random, json
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "fb2o"))
from n5x import step, start_pair, Engine, dual, load
from tcdir import lasso, wval
MUT = os.environ.get("MUT") == "1"
C = Counter(); VIOL = []; CASE = []; MAXRUN = [0, None]; MAXV = [0, None]; HIST = Counter()  # CASE: twin changes with D constant and a length-only W change

def lev(x, y):
    if x[0] != y[0]: return 10 ** 9
    d = x[1] ^ y[1]
    if d: return d.bit_length() - 1
    return -1 if x[2] != y[2] else -2

def top(m): return m.bit_length() - 1 if m else -1

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        D = frozenset(u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u])
        wn = (lambda s, t: (lambda v: s[v] if g.owner[v] == 0 else t[v]))(list(s), tuple(t))
        uu = {}
        for v in range(g.n):
            pl, _ = lasso(wn, v); uu[v] = next((x for x in pl if x in D), None)
        W = [wval(E, wn, v) for v in range(g.n)]
        h3 = all(vs[u][0] == W[u][0] for u in D)
        M = max([lev(vs[u], W[u]) for u in D], default=-2) if h3 else None
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), D=D, uu=uu, W=W, vs=vs, h3=h3, M=M, fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and not rows[j]["fb"] and rows[j + 1]["key"] == rows[i]["key"]: j += 1
        if j > i: run(g, E, name, rows, i, j)
        i = j + 1

def run(g, E, name, rows, i, j):
    C["runs"] += 1; C["trans"] += j - i
    allh3 = all(rows[x]["h3"] for x in range(i, j + 1))
    Ls = max(max(rows[x]["M"] for x in range(i, j + 1)), -1) if allh3 else None
    if MUT and Ls is not None: Ls -= 1
    C["runs_h3"] += allh3; C["runs_long"] += j - i >= g.n
    tw = 0; perv = Counter()
    for k in range(i, j):
        r0, r1 = rows[k], rows[k + 1]
        for v in range(g.n):
            a, b = r0["uu"][v], r1["uu"][v]
            if a is None or b is None or a == b: continue
            C["tc"] += 1
            if r0["W"][v][0] != r1["W"][v][0]: C["wmoving"] += 1; continue
            tw += 1; perv[v] += 1; C["twin"] += 1
            w0, w1 = r0["W"][v], r1["W"][v]
            dch = r0["D"] != r1["D"]; wsame = w0 == w1; lw = lev(w0, w1)
            if E.key(w1) < E.key(w0): C["WMG_V"] += 1; VIOL.append(("WMG", name, k, v))
            LW = top(r0["W"][a][1] ^ r0["W"][b][1]) if b in r0["D"] else None
            post = k >= i + g.n - 1
            C["dch"] += dch; C["wsame"] += wsame; C["w_lenonly"] += lw == -1
            C["h3run"] += allh3; C["post"] += post
            if LW is not None:
                C["LW_known"] += 1; C["lw_ge_LW"] += lw >= LW; C["lw_gt_LW"] += lw > LW
            if allh3:
                C["lw_le_Ls"] += lw <= Ls
                if post:
                    C["post_h3"] += 1
                    if lw > Ls: C["FRZ_V"] += 1; VIOL.append(("FRZ", name, i, k, v, lw, Ls))
            HIST[("dch" if dch else "D=", "wsame" if wsame else ("len" if lw == -1 else "set"))] += 1
            if not dch and lw == -1: CASE.append((name, k, v, a, b, w0, w1))
    if tw > MAXRUN[0]: MAXRUN[:] = [tw, (name, i, j, g.n)]
    if perv and max(perv.values()) > MAXV[0]: MAXV[:] = [max(perv.values()), (name, i, j, g.n)]

def main():
    a = sys.argv[1:]
    if a[0] == "--one":
        g = load(a[1]); st = None
        if len(a) > 2:
            d = json.load(open(a[2])); st = ({int(x): y for x, y in d["sigma"].items()}, {int(x): y for x, y in d["tau"].items()})
        check(g, a[1], st)
    elif a[0] == "--rand":
        sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box43")); from multi import rand_ckO
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); i = 0; K = int(os.environ.get("K", "0"))
        while i < cnt:
            g = rand_ckO(rng, lo, hi, K or rng.choice((2, 2, 3, 4)))
            if g is None: continue
            i += 1
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})
            check(g, f"rand seed {seed} #{i}", None if i % 2 else st)
    else:
        kmin = int(a[2]) if len(a) > 2 else 2
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > 48 or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin: continue
            check(g, f)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    print("HIST", dict(HIST)); print("MAX twin per run", MAXRUN); print("MAX twin per vertex per run", MAXV)
    for c in CASE[:5]: print("LENONLY", c)
    for v in VIOL[:10]: print("VIOLATION", v)
    print("RUND PASS" if not VIOL else "RUND FAIL")

if __name__ == "__main__":
    main()
