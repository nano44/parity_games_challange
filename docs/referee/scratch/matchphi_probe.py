#!/usr/bin/env python3
"""REFEREE succ. 17 probe for packet P-N5-MATCHPHI (docs/lit/P-N5-MATCHPHI.md, sha1 544705b7..., freeze l-lit 12b7d12a). Own code only
(no import of docs/lit/T33-match-phi-check.py; own MATCHED search by DFS over the outgoing ranks; own engine rl_engine for N5 data).
 ex K       Fact 1 on all rank pairs; Lemma MATCH-Phi on ALL ordered pairs (A, B), A != B (improving or not), for EVERY parity pattern of K
            ranks; counts of improving pairs, matched, carries.
 seq N L K  the Corollary on N random sequences of L subsets of K ranks (any sequence: the Remark's claim), and on N random weight-
            increasing sequences.
 files...   N5 (own engine): per (vertex, phase) PCH, NM, the Corollary's bound; maxima. LAMRUN=1: per lambda-run (lambda_Xi constant, tau free).
Mutations: MUT=1 (M2) dropped (uncovered odd additions allowed); MUT=2 (M1) non-strict (w(i) >= w(o)); MUT=3 the Corollary with W := K."""
import sys, os, itertools, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
MUT = int(os.environ.get("MUT", "0"))


def wpos(r, par): return (r + 1) if par[r] == 0 else -(r + 1)   # positions r + 1 over R_c = {0..K-1}


def weight(A, par): return sum((1 if par[r] == 0 else -1) << r for r in A)


def phi(A, par): return sum(wpos(r, par) for r in A)


def matched(A, B, par):
    outs = sorted(A - B); ins = sorted(B - A)
    def ok_pair(o, i): return wpos(i, par) >= wpos(o, par) if MUT == 2 else wpos(i, par) > wpos(o, par)
    need_in = {i for i in ins if par[i] == 1} if MUT != 1 else set()
    def dfs(k, used):
        if k == len(outs):
            return need_in <= used
        o = outs[k]
        if par[o] == 1 and dfs(k + 1, used): return True       # odd out may stay uncovered
        for i in ins:
            if i not in used and ok_pair(o, i) and dfs(k + 1, used | {i}): return True
        return False
    return dfs(0, frozenset())


def ex(K):
    cnt = Counter(); subs = [frozenset(c) for k in range(K + 1) for c in itertools.combinations(range(K), k)]
    for bits in range(2 ** K):
        par = [(bits >> r) & 1 for r in range(K)]
        for o in range(K):
            for i in range(K):
                if o != i:
                    cnt["F1_chk"] += 1
                    if (wpos(i, par) > wpos(o, par)) != (weight({i}, par) > weight({o}, par)): cnt["F1_FAIL"] += 1
        for r in range(K):
            if par[r] == 0 and not weight({r}, par) > 0: cnt["F1add_FAIL"] += 1
        for A in subs:
            for B in subs:
                if A == B: continue
                imp = weight(B, par) > weight(A, par)
                m = matched(A, B, par)
                cnt["PAIRS"] += 1; cnt["IMP"] += imp
                if m:
                    cnt["MATCHED"] += 1
                    if phi(B, par) - phi(A, par) < 1: cnt["LEMMA" + ("_MUT%d" % MUT if MUT in (1, 2) else "") + "_FAIL"] += 1
                    if not imp: cnt["MATCHED_but_not_improving"] += 1
                elif imp: cnt["CARRY_improving"] += 1
    return cnt


def corollary(seq, par, K, cnt, tag):
    W = K if MUT == 3 else K * (K + 1) // 2
    pch = sum(1 for t in range(len(seq) - 1) if seq[t] != seq[t + 1])
    nm = sum(1 for t in range(len(seq) - 1) if seq[t] != seq[t + 1] and not matched(seq[t], seq[t + 1], par))
    cnt[tag + "_chk"] += 1
    if pch > W * (nm + 1) + nm: cnt[tag + "_COR" + ("_MUT3" if MUT == 3 else "") + "_FAIL"] += 1
    return pch, nm


def seqs(N, L, K, seed):
    cnt = Counter(); rng = random.Random(seed)
    for _ in range(N):
        par = [rng.randint(0, 1) for _ in range(K)]
        seq = [frozenset(r for r in range(K) if rng.random() < 0.5) for _ in range(L)]
        corollary(seq, par, K, cnt, "ANY")
        cur = frozenset(r for r in range(K) if rng.random() < 0.5); inc = [cur]
        for _ in range(L * 4):
            nxt = frozenset(r for r in range(K) if rng.random() < 0.5)
            if weight(nxt, par) > weight(cur, par): inc.append(nxt); cur = nxt
        corollary(inc, par, K, cnt, "INC")
    return cnt


def n5(paths):
    import rl_engine as RE, core_probe as CP
    cnt = Counter(); best = (0, None)
    for path in paths:
        if path.endswith(".start"): continue
        try: g = RE.parse(path)
        except Exception: continue
        if g.n > int(os.environ.get("MAXN", "600")): continue
        sp = path[:-3] + ".start"
        s0 = CP.parse_start(g, sp) if os.path.exists(sp) else None
        st = RE.run(g, s0 or RE.best_reward_start(g)); cnt["RUNS"] += 1
        T = len(st); k = 0
        while k < T:
            j = k; lam = tuple(v[0] for v in st[k]["Xi"])
            while j + 1 < T and tuple(v[0] for v in st[j + 1]["Xi"]) == lam and (os.environ.get("LAMRUN") or st[j + 1]["t"] == st[k]["t"]): j += 1
            for v in range(g.n):
                c = lam[v]; rc = g.rank[c]; K = g.n - 1 - rc
                par = [g.prio[g.byrank[rc + 1 + p]] % 2 for p in range(K)]       # positions over R_c
                seq = [frozenset(r - rc - 1 for r in range(g.n) if (st[t]["Xi"][v][1] >> r) & 1) for t in range(k, j + 1)]
                if any(min(s, default=0) < 0 for s in seq): cnt["RC_FAIL"] += 1
                pch, nm = corollary(seq, par, K, cnt, "N5")
                if pch:
                    cnt["VP"] += 1; cnt["PCH"] += pch; cnt["NM"] += nm
                    cnt["MAX_PCH"] = max(cnt["MAX_PCH"], pch); cnt["MAX_NM"] = max(cnt["MAX_NM"], nm)
                    if nm / g.n > best[0]: best = (nm / g.n, (os.path.relpath(path), g.n, v, (k, j), pch, nm))
            k = j + 1
    print("MAX_NM_over_n", best)
    return cnt


def main(a):
    if a[0] == "ex": cnt = ex(int(a[1]))
    elif a[0] == "seq": cnt = seqs(int(a[1]), int(a[2]), int(a[3]), int(a[4]) if len(a) > 4 else 33)
    else: cnt = n5(a)
    for k in sorted(cnt): print(k, cnt[k])


if __name__ == "__main__":
    main(sys.argv[1:])
