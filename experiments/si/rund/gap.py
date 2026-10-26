#!/usr/bin/env python3
"""L-SI box 17: DATA for Lemma TWIN-GAP (docs/si/N5-RUND-box17.md). Scores: s_X(v) := w(P(Xi(v))), s_W(v) := w(P(W(v))), with
w(P) := sum over x in P of (+2^rank x if x even, -2^rank x if odd) (Engine.weight, S1's path component). Offset Delta(v) := s_W(v) - s_X(v).
Gate offset delta(u) := w(P(W u)) - w(P(Xi u)) for u in D_k.
Along maximal fallback-free in-phase runs (n5x.py step, read-only), at every transition k -> k+1 and every v with lambda_Xi(v) and
lambda_W(v) unchanged:
  MONO_V   s_X or s_W decreases (S1 monotonicity of Xi and of W inside a phase predicts 0; cycle nodes fixed, so the path component
           cannot drop)
  JUMP_V   Delta changes by d but neither s_W rises by >= d (d > 0) nor s_X rises by >= -d (d < 0) (arithmetic consequence of MONO)
  FAC_V    (h3_D) at k, v in R_D, c := lambda(v) not on pi_v, and Delta(v) != delta(u(v)); or c on pi_v and Delta(v) != 0
           (C2-H3's factorisation P_F(v) = (pi_v ∩ V_>c) ⊔ P_F(u(v)), exact in both frames)
Per run and vertex it counts the Delta-changes (dchg), and the run's score increase RANGE := total rise of s_W(v) + s_X(v); it reports
the max of dchg and the max of RANGE / Gamma, Gamma := the least nonzero |Delta change| at that vertex on the run (the TWIN-GAP bound).
Usage: gap.py --list FILE [KMIN] | --rand COUNT NLO NHI SEED | --one GAME [START]  (NMAX, RS env as rel.py)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "fb2o"))
from n5x import step, start_pair, Engine, dual, load, readstart
from tcdir import lasso, wval
C = Counter(); VIOL = []; TOP = []; BHIST = Counter(); RET = []

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        D = frozenset(u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u])
        wn = (lambda s, t: (lambda v: s[v] if g.owner[v] == 0 else t[v]))(list(s), tuple(t))
        W = [wval(E, wn, v) for v in range(g.n)]
        h3 = all(vs[u][0] == W[u][0] for u in D)
        M = max([(lambda d: d.bit_length() - 1 if d else -1)(vs[u][1] ^ W[u][1]) for u in D], default=-1) if h3 else None
        lows = [((vs[u][1] ^ W[u][1]) & -(vs[u][1] ^ W[u][1])).bit_length() - 1 for u in D if vs[u][1] != W[u][1]]
        ell = min(lows) if h3 and lows else None
        uu = [next((x for x in lasso(wn, v)[0] if x in D), None) for v in range(g.n)]
        sX = [E.weight(vs[v][1]) for v in range(g.n)]; sW = [E.weight(W[v][1]) for v in range(g.n)]
        if h3:
            for v in range(g.n):
                pl, _ = lasso(wn, v); u = next((x for x in pl if x in D), None)
                if u is None: continue
                C["fac_n"] += 1; c = vs[v][0]; pre = pl[:pl.index(u)]
                want = 0 if c in pre else sW[u] - sX[u]
                if sW[v] - sX[v] != want: C["FAC_V"] += 1; VIOL.append(("FAC", name, len(rows), v))
        stk = (D, frozenset(v for v in range(g.n) if uu[v] is not None), tuple((u, vs[u], W[u]) for u in sorted(D)), h3)
        # stretch_D key (N5-2O-T §0): D, R_D and the gates' two values constant; (h3_D) is part of the key (OFFSET-ONCE is tested under it)
        rows.append(dict(stk=stk, key=(tuple(x[0] for x in vs), tuple(t)), lx=[x[0] for x in vs], lw=[x[0] for x in W], sX=sX, sW=sW, M=M, uu=uu, ell=ell,
                         fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and not rows[j]["fb"] and rows[j + 1]["key"] == rows[i]["key"]: j += 1
        if j > i: run(g, name, rows, i, j)
        i = j + 1

def run(g, name, rows, i, j):
    C["runs"] += 1
    # OFFSET-ONCE (CONJECTURE test): inside a stretch_D segment of the run (D and gate values constant), with v's cycle nodes
    # constant, v's offset Delta never returns to a value it has left
    a = i
    while a <= j:
        b = a
        while b + 1 <= j and rows[b + 1]["stk"] == rows[a]["stk"]: b += 1
        if b > a and not rows[a]["stk"][3]:
            C["stretch_segs_noh3"] += 1
        elif b > a:
            C["stretch_segs"] += 1
            for v in range(g.n):
                if len({(rows[x]["lx"][v], rows[x]["lw"][v]) for x in range(a, b + 1)}) > 1: continue
                seq = [rows[x]["sW"][v] - rows[x]["sX"][v] for x in range(a, b + 1)]
                left, cur, nch = set(), seq[0], 0
                for y in seq[1:]:
                    if y != cur:
                        nch += 1; left.add(cur)
                        if y in left: C["RETURN"] += 1; RET.append((name, a, b, v, seq))
                        cur = y
                C["seg_dchg"] += nch; C["max_seg_dchg"] = max(C["max_seg_dchg"], nch)
        a = b + 1
    allh3 = all(rows[x]["M"] is not None for x in range(i, j + 1))
    Ls = max(max(rows[x]["M"] for x in range(i, j + 1)), -1) if allh3 else None
    if allh3:
        C["runs_h3"] += 1; base = i + g.n - 1
        ells = [rows[x]["ell"] for x in range(i, j + 1) if rows[x]["ell"] is not None]
        B = Ls - min(ells) + 1 if ells else None        # width of the gates' disagreement band [ell, L*]
        if B is not None: C["max_B"] = max(C["max_B"], B); BHIST[B] += 1
        for v in range(g.n):
            tot, post, gam = 0, 0, None
            for k in range(i, j):
                r0, r1 = rows[k], rows[k + 1]
                d = (r1["sW"][v] - r1["sX"][v]) - (r0["sW"][v] - r0["sX"][v])
                a, b = r0["uu"][v], r1["uu"][v]
                if a is not None and b is not None and a != b and r0["lw"][v] == r1["lw"][v]:
                    C["twin"] += 1; C["twin_dchg" if d else "twin_dpres"] += 1
                if d:
                    tot += 1
                    if k >= base: post += 1; gam = abs(d) if gam is None else min(gam, abs(d))
            C["max_tot_per_v"] = max(C["max_tot_per_v"], tot)
            bound = (g.n - 1) + (2 ** (B + 1) if B is not None else 0)       # TWIN-GAP (iii): offset changes per vertex per run
            if tot > bound: C["BOUND_V"] += 1; VIOL.append(("BOUND", name, i, j, v, tot, bound))
            if post:
                C["post_dchg"] += post; pb = (2 ** (Ls + 2) - 2) // gam if Ls >= 0 else 0   # TWIN-GAP (ii): post-freeze count * Gamma <= 2^(L*+2) - 2
                if post > pb: C["POST_V"] += 1; VIOL.append(("POST", name, i, j, v, post, pb))
    for v in range(g.n):
        dchg, rng, gam = 0, 0, None
        for k in range(i, j):
            r0, r1 = rows[k], rows[k + 1]
            if (r0["lx"][v], r0["lw"][v]) != (r1["lx"][v], r1["lw"][v]): dchg, rng, gam = 0, 0, None; continue   # new segment
            dx, dw = r1["sX"][v] - r0["sX"][v], r1["sW"][v] - r0["sW"][v]
            C["trans_v"] += 1
            if dx < 0 or dw < 0: C["MONO_V"] += 1; VIOL.append(("MONO", name, k, v, dx, dw)); continue
            d = (r1["sW"][v] - r1["sX"][v]) - (r0["sW"][v] - r0["sX"][v])
            if d:
                C["dchg"] += 1; dchg += 1; gam = abs(d) if gam is None else min(gam, abs(d))
                m = 2 if os.environ.get("MUT") == "1" else 1      # MUT=1: demand a doubled jump (control; must fail)
                if not ((d > 0 and dw >= m * d) or (d < 0 and dx >= -m * d)): C["JUMP_V"] += 1; VIOL.append(("JUMP", name, k, v))
            rng += dx + dw
            if dchg and gam:
                ratio = rng / gam
                if dchg > C["max_dchg"]: C["max_dchg"] = dchg; TOP.append(("dchg", dchg, name, i, j, v, g.n, "range/gamma", round(ratio, 2)))
                if ratio > C["max_ratio"]: C["max_ratio"] = ratio

def main():
    a = sys.argv[1:]
    if a[0] == "--one":
        g = load(a[1]); check(g, a[1], readstart(a[2]) if len(a) > 2 else None)
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
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin:
                continue
            check(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                check(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in TOP[-10:]: print("TOP", x)
    print("BHIST", sorted(BHIST.items()))
    for x in RET[:5]: print("RETURN", x)
    for v in VIOL[:10]: print("VIOLATION", v)
    print("GAP PASS" if not VIOL else "GAP FAIL")

if __name__ == "__main__":
    main()
