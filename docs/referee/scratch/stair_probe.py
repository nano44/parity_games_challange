#!/usr/bin/env python3
"""REFEREE successor 21: own control for packet P-N5-STAIR (L-NEW box 112, l-new 9a58765f, sha1 31771241). Own engine rl_engine; no
lane code. Per W-run F = [p, q] (RESULTS R89; tau, C fixed), W_k := val(s_k, tau), Xi_k := Xi_{s_k}; CS as in RESULTS R93 Fact LEX.
  FROZEN  BW_k = sum_v lcp(CS W_k(v), CS W_q(v)) and AF_k = sum_v lcp(CS Xi_k(v), CS W_q(v)) never fall on F
  BWACC   |F| <= (M + 1) n(n + 2) + M N_F, M = n(n + 2) + 1, N_F = transitions with BW flat and A not falling
  BIT     for equal cycle nodes, x < y iff beta(x) <lex beta(y) (checked on every pair W_k(v), W_(k+1)(v) and Xi_k, Xi_(k+1))
  FG      FIRST-GOOD: every change of W(v) flips its first differing bit 0 -> 1
  RR      RESET-RED  WCT <= sum WCH <= n(3n + 1) + TD
  ROOT    RESET-ROOT: each reset of W(v) at k has a first switched Even y on v's (s_(k+1), tau)-play, and W(y) has a reset at k
  DCOPY   DESC-COPY: a descent of v at k with v unswitched on [k', k] gives a descent of its successor z at k
  ASC     ASC-RUN q_(j+1) != q_j, and WCH(v) <= (3n + 1)(1 + DESC(v));  STAIR  WCT <= n(3n + 1) + (3n + 1) DESC
MUT 1: AF referenced to W_k (the remark's A; must bite where A falls). MUT 2: beta without orientation ([r in P] for every rank; FG bites).
Usage: stair_probe.py FILES... | rand N lo hi seed     (env MUT, MAXN; FILE.start used when present)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
MUT = int(os.environ.get("MUT", "0"))
EX = []


def fail(cnt, tag, *a):
    cnt[tag + "_V"] += 1
    if len(EX) < 30: EX.append((tag,) + a)


def nxs(g, s, t): return [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]


def CS(g, x):
    c, m, d = x
    out = [g.rew[c]]
    for r in range(g.n - 1, -1, -1):
        out.append(0 if not (m >> r) & 1 else (1 if g.prio[g.byrank[r]] % 2 == 0 else -1))
    out.append(d if g.prio[c] % 2 else -d)
    return out


def lcp(a, b):
    i = 0
    while i < len(a) and a[i] == b[i]: i += 1
    return i


def beta(g, x):
    c, m, d = x; n = g.n; out = []
    for r in range(n - 1, -1, -1):
        bit = (m >> r) & 1
        if MUT != 2 and g.prio[g.byrank[r]] % 2 == 1: bit = 1 - bit
        out.append(bit)
    sl = d if g.prio[c] % 2 else -d
    out += [1 if sl >= j else 0 for j in range(-n, n + 1)]
    return out


def analyse(cnt, g, start, name):
    st = RE.run(g, start); n = g.n; T = len(st) - 1
    Ev = [v for v in range(n) if g.owner[v] == 0]
    Xi = [s["Xi"] for s in st]
    W = [[RE.play_value(g, nxs(g, s["s"], s["t"]), v) for v in range(n)] for s in st]
    runs, a = [], 0
    for k in range(T):
        if st[k]["t"] != st[k + 1]["t"] or st[k]["fb"] or [x[0] for x in W[k]] != [x[0] for x in W[k + 1]]: runs.append((a, k)); a = k + 1
    runs.append((a, T))
    L = n * (n + 2); M = L + 1; NB = 3 * n + 1
    for (p, q) in runs:
        if q == p: continue
        cnt["wruns"] += 1; F = q - p; cnt["trans"] += F
        tau = st[p]["t"]; C = {v for v in range(n) if W[p][v][0] == v}
        csW = [[CS(g, W[k][v]) for v in range(n)] for k in range(p, q + 1)]
        csX = [[CS(g, Xi[k][v]) for v in range(n)] for k in range(p, q + 1)]
        BW = [sum(lcp(csW[i][v], csW[q - p][v]) for v in range(n)) for i in range(F + 1)]
        AF = [sum(lcp(csX[i][v], csW[i if MUT == 1 else q - p][v]) for v in range(n)) for i in range(F + 1)]
        A = [sum(lcp(csX[i][v], csW[i][v]) for v in range(n)) for i in range(F + 1)]
        for i in range(F):
            cnt["FROZEN_chk"] += 1
            if BW[i + 1] < BW[i]: fail(cnt, "FROZEN_BW", name, p + i)
            if AF[i + 1] < AF[i]: fail(cnt, "FROZEN_AF", name, p + i)
        NF = sum(1 for i in range(F) if BW[i + 1] == BW[i] and A[i + 1] >= A[i])
        if F > (M + 1) * L + M * NF: fail(cnt, "BWACC", name, p, q)
        B = [[beta(g, W[k][v]) for v in range(n)] for k in range(p, q + 1)]
        WCT = 0; WCH = Counter(); TD = 0; DESC = Counter(); last = {}; qs = {v: [] for v in range(n)}; desc_at = []
        for i in range(F):
            k = p + i; changed = [v for v in range(n) if W[k][v] != W[k + 1][v]]
            if changed: WCT += 1
            s0, s1 = st[k]["s"], st[k + 1]["s"]; sw = {y for y in Ev if s0[y] != s1[y]}
            nx1 = nxs(g, s1, tau)
            for v in range(n):
                for (x, y) in ((W[k][v], W[k + 1][v]), (Xi[k][v], Xi[k + 1][v])):
                    if x[0] == y[0] and x != y:
                        cnt["BIT_chk"] += 1
                        if (g.key(x) < g.key(y)) != (beta(g, x) < beta(g, y)): fail(cnt, "BIT", name, k, v)
            for v in changed:
                WCH[v] += 1
                b0, b1 = B[i][v], B[i + 1][v]
                j = lcp(b0, b1)
                if not (b0[j] == 0 and b1[j] == 1): fail(cnt, "FG", name, k, v)
                resets = [r for r in range(NB) if b0[r] == 1 and b1[r] == 0]
                TD += len(resets)
                if resets:
                    cnt["ROOT_chk"] += 1
                    pl, _ = RE.lasso(nx1, v)
                    path = (pl + _)
                    ys = [y for y in path if y in sw]
                    if not ys: fail(cnt, "ROOT_none", name, k, v)
                    else:
                        y = ys[0]
                        if not any(B[i][y][r] == 1 and B[i + 1][y][r] == 0 for r in range(NB)): fail(cnt, "ROOT", name, k, v, y)
                if qs[v]:
                    if j == qs[v][-1][1]: fail(cnt, "ASC", name, k, v)
                    if j > qs[v][-1][1]:
                        DESC[v] += 1; desc_at.append((v, qs[v][-1][0], k))
                qs[v].append((k, j))
        for v in range(n):
            if WCH[v] > NB * (1 + DESC[v]): fail(cnt, "ASCB", name, v)
        if not (WCT <= sum(WCH.values()) <= n * NB + TD): fail(cnt, "RR", name, p, q)
        if WCT > n * NB + NB * sum(DESC.values()): fail(cnt, "STAIR", name, p, q)
        cnt["WCT"] += WCT; cnt["WCH"] += sum(WCH.values()); cnt["TD"] += TD; cnt["DESC"] += sum(DESC.values())
        # DESC-COPY
        dset = {(v, k) for (v, _, k) in desc_at}
        for (v, k0, k) in desc_at:
            if v in C: continue
            if g.owner[v] == 0 and any(st[u]["s"][v] != st[u + 1]["s"][v] for u in range(k0, k + 1)): continue
            z = st[k]["s"][v] if g.owner[v] == 0 else tau[v]
            cnt["DCOPY_chk"] += 1
            if (z, k) not in dset: fail(cnt, "DCOPY", name, v, z, k)


def main(a):
    import core_probe as CP
    cnt = Counter()
    def do(g, name, extra=None):
        try: analyse(cnt, g, extra, name)
        except RuntimeError: cnt["maxit"] += 1
    if a and a[0] == "rand":
        import dual_probe as D
        N, lo, hi, seed = map(int, a[1:5]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            cnt["GAMES"] += 1; do(D.rand_ck(r2, nn, r2.randint(0, min(5, nn - 1))), "rand%d" % i)
    else:
        for p in a:
            if p.endswith(".start"): continue
            try: g = RE.parse(p)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "100")): cnt["skip_big"] += 1; continue
            sp = p[:-3] + ".start"; ex = None
            if os.path.exists(sp):
                try: ex = CP.parse_start(g, sp)
                except Exception: cnt["start_err"] += 1
            cnt["GAMES"] += 1; do(g, os.path.basename(p), ex)
    for k in sorted(cnt): print(k, cnt[k])
    print("VIOLATIONS", sum(v for k, v in cnt.items() if k.endswith("_V")))
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
