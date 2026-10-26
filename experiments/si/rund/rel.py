#!/usr/bin/env python3
"""L-SI box 17: DATA for Lemma CR-REL (docs/si/N5-RUND-box17.md). CR-D (P-N5-H3 §5) with hypothesis (i) replaced by the EDGE ORDER
TRANSFER (i_rel) at level L: for every Even x, every z in succ(x), a := sigma_k(x):
    COARSE_L(W_k(z)) >_L COARSE_L(W_k(a))  =>  Xi_k(z) > Xi_k(a)   (strict, S1 order).
L_rel(k) := the least L in {-1, 0, 1, ..., maxrank} with (i_rel) at k (INF if none). (i_rel) is monotone in L.
Along every maximal fallback-free run S inside one phase (n5x.py step, read-only) it records:
  ii     the W-cycle-node map is constant on S (hypothesis (ii) of CR-D)
  Lr     max_S L_rel;  Md  max_S M_D if (h3_D) at every state, else INF
  FRZ    if (ii) and Lr < INF: COARSE_Lr(W) constant from state k_0 + n - 1 (0-based) on S; non-vacuous only when S has >= n + 1 states
  full   Lr < the rank of every W-cycle node of S (then COARSE_Lr(W(v)) is the full (c, P); after the freeze only lengths move)
  XIC    transitions of S with a Xi-change at some vertex; XIC_post those at states >= k_0 + n - 1
Checks: FRZ_V (CR-REL predicts 0). MUT=1: the freeze is tested at Lr - 1 (control; must fail when the data reach it). MUT=2: from state k_0 + 1 (control).
Usage: rel.py --list FILE [KMIN] | --rand COUNT NLO NHI SEED | --one GAME [START.json]"""
import sys, os, random, json
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "fb2o"))
from n5x import step, start_pair, Engine, dual, load
from tcdir import lasso, wval
MUT = os.environ.get("MUT") == "1"
MUT2 = os.environ.get("MUT") == "2"     # MUT=2: the freeze is tested from state k_0 + 1 instead of k_0 + n - 1 (control; must fail)
INF = 10 ** 9
C = Counter(); VIOL = []; LONG = []

def lev(x, y):
    if x[0] != y[0]: return INF
    d = x[1] ^ y[1]
    if d: return d.bit_length() - 1
    return -1 if x[2] != y[2] else -2

def ckey(E, x, L):
    m = (x[1] >> (L + 1)) << (L + 1) if L >= 0 else x[1]
    return (E.rew[x[0]], E.weight(m))

def lrel(g, E, s, vs, W):
    maxr = max(E.rank)
    for L in range(-1, maxr + 1):
        ok = True
        for x in range(g.n):
            if g.owner[x] != 0: continue
            a = s[x]; ka = ckey(E, W[a], L); xa = E.key(vs[a])
            for z in g.succ[x]:
                if z != a and ckey(E, W[z], L) > ka and not E.key(vs[z]) > xa: ok = False; break
            if not ok: break
        if ok: return L
    return INF

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        D = [u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u]]
        wn = (lambda s, t: (lambda v: s[v] if g.owner[v] == 0 else t[v]))(list(s), tuple(t))
        W = [wval(E, wn, v) for v in range(g.n)]
        h3 = all(vs[u][0] == W[u][0] for u in D)
        M = max([lev(vs[u], W[u]) for u in D], default=-2) if h3 else INF
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), vs=vs, W=W, M=M, Lr=lrel(g, E, s, vs, W), D=len(D),
                         fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and not rows[j]["fb"] and rows[j + 1]["key"] == rows[i]["key"]: j += 1
        if j > i: run(g, E, name, rows, i, j)
        i = j + 1

def run(g, E, name, rows, i, j):
    S = rows[i:j + 1]; C["runs"] += 1
    ii = all(tuple(x[0] for x in R["W"]) == tuple(x[0] for x in S[0]["W"]) for R in S)
    Lr = max(R["Lr"] for R in S); Md = max(R["M"] for R in S)
    C["ii"] += ii; C["Lr_fin"] += Lr < INF; C["Md_fin"] += Md < INF
    Md = max(Md, -1); C["Lr_lt_Md"] += Lr < Md; C["Lr_gt_Md"] += Lr > Md and Md < INF
    C["DnonE"] += any(R["D"] for R in S)
    cyc = {x[0] for R in S for x in R["W"]}; full = Lr < min(E.rank[c] for c in cyc)
    xic = sum(1 for k in range(len(S) - 1) if S[k]["vs"] != S[k + 1]["vs"])
    xicp = sum(1 for k in range(g.n - 1, len(S) - 1) if S[k]["vs"] != S[k + 1]["vs"])
    C["XIC"] += xic; C["XIC_post"] += xicp
    if not (ii and Lr < INF): return
    C["hyp"] += 1; C["hyp_full"] += full; C["hyp_notH3"] += Md >= INF
    L = Lr - 1 if MUT else Lr
    base = 1 if MUT2 else g.n - 1
    if len(S) >= base + 2:
        C["nonvac"] += 1; C["nonvac_full"] += full; C["nonvac_notH3"] += Md >= INF; C["nonvac_Lr_lt_Md"] += Lr < Md
        cont = max(bin(R["W"][v][1] >> (L + 1)).count("1") if L >= 0 else bin(R["W"][v][1]).count("1") for R in S for v in range(g.n))
        C["nonvac_content"] += cont > 0     # content: some W path set has a vertex above L (else the freeze says only (ii))
        LONG.append((name, i, j, g.n, Lr, Md if Md < INF else "INF", full, xic, xicp, "content", cont))
        for x in range(base + 1, len(S)):
            C["FRZ_n"] += 1
            if any(ckey(E, S[x]["W"][v], L) != ckey(E, S[base]["W"][v], L) for v in range(g.n)):
                C["FRZ_V"] += 1; VIOL.append(("FRZ", name, i, i + x)); break

def main():
    a = sys.argv[1:]
    if a[0] == "--one":
        g = load(a[1]); st = None
        if len(a) > 2:
            if a[2].endswith(".json"):
                d = json.load(open(a[2])); st = ({int(x): y for x, y in d["sigma"].items()}, {int(x): y for x, y in d["tau"].items()})
            else:
                from n5x import readstart; st = readstart(a[2])
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
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin: continue
            check(g, f)
            rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):     # RS=k: also k random start pairs per file (seeded by the relative path)
                check(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in LONG[:20]: print("NONVAC", x)
    for v in VIOL[:10]: print("VIOLATION", v)
    print("REL PASS" if not VIOL else "REL FAIL")

if __name__ == "__main__":
    main()
