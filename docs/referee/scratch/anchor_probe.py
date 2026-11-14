#!/usr/bin/env python3
"""REFEREE successor 22: own control for packet P-N5-ANCHOR (L-NEW box 134, l-new f009a9a1, sha1 ad97ad88). Own engine rl_engine (SPEC
only); no lane code. Per N5 run: W_k := play values of (sigma_k, tau_k); FL transition j: not a fallback at j-1, tau_j = tau_(j-1),
sigma_j != sigma_(j-1), W_j = W_(j-1). FL run = maximal consecutive FL transitions a+1..b. Then, per run (packet §1 definitions):
  TIGHT  sigma_j(x) in T_x (x not in CN), in T_c (c in CN), every state of the run           (Lemma FL-TIGHT)
  PRE    Lemma PREFIX (a): the Xi_j-play equals the W-play up to the first A in ODIFF_j u CN; (b) levels; checked at every y not in CN
  TIME   in an epoch with first source state s0, an Even x not in CN moves at j only if j - s0 <= l(x) - 1   (FL-ANCHOR (i))
  CNM    after s0 + l* - 1, each Even c in CN moves at most |T_c| - 1 times in the epoch      (FL-ANCHOR (ii))
  EPO    epoch length <= CAP; RUN  FL <= CAP (1 + GCH); CIRC GCH <= FL - 1                 (FL-ANCHOR (iii), Lemma CIRC)
Prints per run: a, b, FL, CAP, GCH, epochs, ODIFF Xi-changes over run states (j in (a, b]), with the vertices. Usage: anchor_probe.py
FILE.pg [FILE.start] (start: PARTIAL rule of s4b_probe, i.e. S3 start overwritten by the file)."""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
import s4b_probe as SB


def play(nx, v):
    seq, seen = [], set()
    while v not in seen: seen.add(v); seq.append(v); v = nx[v]
    return seq


def main(a):
    g = RE.parse(a[0]); n = g.n
    start = SB.partial_start(g, a[1]) if len(a) > 1 else None
    st = RE.run(g, start); K = len(st) - 1; cnt = Counter(); out = []
    NX = [[s["s"][v] if g.owner[v] == 0 else s["t"][v] for v in range(n)] for s in st]
    W = [[RE.play_value(g, NX[k], v) for v in range(n)] for k in range(K + 1)]
    FLt = [j for j in range(1, K + 1) if not st[j - 1]["fb"] and st[j]["t"] == st[j - 1]["t"] and st[j]["s"] != st[j - 1]["s"]
           and W[j] == W[j - 1]]
    runs, cur = [], []
    for j in FLt:
        if cur and j == cur[-1] + 1: cur.append(j)
        else:
            if cur: runs.append(cur)
            cur = [j]
    if cur: runs.append(cur)
    for r in runs:
        A0, B = r[0] - 1, r[-1]; Wr = W[A0]; ta = st[A0]["t"]
        lev = [Wr[v][2] for v in range(n)]; CN = {v for v in range(n) if lev[v] == 0}
        T = {}
        for x in range(n):
            if g.owner[x] != 0: continue
            if x in CN: T[x] = {y for y in g.succ[x] if Wr[y][0] == x}
            else: T[x] = {y for y in g.succ[x] if g.ext(x, Wr[y]) == Wr[x]}
        ls = max([lev[x] for x in range(n) if g.owner[x] == 0 and x not in CN] or [1])
        CAP = (ls - 1) + sum(len(T[c]) - 1 for c in CN if g.owner[c] == 0)
        def odiff(j): return {o for o in range(n) if g.owner[o] == 1 and st[j]["sb"][o] != ta[o]}
        def G(j):
            od = odiff(j)
            return (tuple(st[j]["sb"][o] for o in range(n) if g.owner[o] == 1), tuple((o, st[j]["Xi"][o]) for o in sorted(od)),
                    tuple((c, st[j]["Xi"][c]) for c in sorted(CN)))
        for j in range(A0, B + 1):
            for x in T:
                cnt["tight_chk"] += 1
                if st[j]["s"][x] not in T[x]: cnt["TIGHT_V"] += 1
            od = odiff(j); nxi = [st[j]["s"][v] if g.owner[v] == 0 else st[j]["sb"][v] for v in range(n)]
            for y in range(n):
                if y in CN: continue
                p = play(NX[j], y); q = play(nxi, y)
                i = next(i for i, v in enumerate(p) if v in od or v in CN)
                cnt["pre_chk"] += 1
                if p[:i + 1] != q[:i + 1] or any(lev[v] >= lev[y] for v in p[1:i]): cnt["PRE_V"] += 1
        gch = sum(1 for j in range(A0 + 1, B) if G(j) != G(j - 1))
        if gch > (B - A0) - 1: cnt["CIRC_V"] += 1
        if B - A0 > CAP * (1 + gch): cnt["RUN_V"] += 1
        # epochs: transitions j (source state j-1) grouped by G(j-1)
        eps, e = [], [r[0]]
        for j in r[1:]:
            if G(j - 1) == G(e[-1] - 1): e.append(j)
            else: eps.append(e); e = [j]
        eps.append(e)
        for e in eps:
            s0 = e[0] - 1
            if len(e) > CAP: cnt["EPO_V"] += 1
            mv = Counter()
            for j in e:
                for x in T:
                    if st[j]["s"][x] == st[j - 1]["s"][x]: continue
                    if x not in CN:
                        cnt["moves_nonCN"] += 1
                        if j - s0 > lev[x] - 1: cnt["TIME_V"] += 1
                    elif j - 1 >= s0 + ls - 1: mv[x] += 1
            for c, k in mv.items():
                if k > len(T[c]) - 1: cnt["CNM_V"] += 1
        oxc = [(j, o) for j in range(A0 + 1, B + 1) for o in sorted(odiff(j) | odiff(j - 1)) if st[j]["Xi"][o] != st[j - 1]["Xi"][o]
               and o in odiff(j - 1)]
        out.append("RUN [%d, %d] FL %d CAP %d GCH %d epochs %d ODIFF-Xi-changes %d %s" % (A0, B, B - A0, CAP, gch, len(eps), len(oxc), oxc[:12]))
    print("FILE", os.path.basename(a[0]), "n", n, "K", K, "fallbacks", sum(1 for s in st if s["fb"]), "FLruns", len(runs), "FLtrans", len(FLt))
    for o in out: print(o)
    for k in sorted(cnt): print(k, cnt[k])
    print("VIOLATIONS", sum(v for k, v in cnt.items() if k.endswith("_V")))


if __name__ == "__main__":
    main(sys.argv[1:])
