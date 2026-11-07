#!/usr/bin/env python3
"""REFEREE successor 21: own control for packet P-N5-GATE (L-NEW box 120, l-new 516717da, sha1 ac88915d). Own engine rl_engine; no lane
code. LO_k := Xi_k, HI_k := the dual valuation Ut_k of tau_k (Lemma R: same triple, G's order), W_k := val(s_k, t_k).
  SQZ   LO_k <= W_k <= HI_k, LO non-decreasing, HI non-increasing (R18 (d) Lemma S (a)-(b), used on every game)
  SET   SETTLE-MON; BR  BRACKET-MON (per vertex lcp of CS LO, CS HI never falls); RED  K <= (n+1)(SG+1), K <= (n(n+2)+1)(BG+1)
  CR    CONSISTENT-RED's Corollary on every tau-stretch: length <= (INC+1)(B-1) + INC;  INC counted (not fallback and Is == IW)
  PH    §6: the largest number of W-changing transitions in one lambda_W-phase of a tau-stretch (MAXPH) against n - 1
MUT 1: HI taken as W (the sandwich's upper half collapses; SET must bite). MUT 2: BR with HI replaced by LO_(k+1)'s CS at k (must bite).
Usage: gate_probe.py FILES... | rand N lo hi seed   (env MUT, MAXN)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
import stair_probe as SP
MUT = int(os.environ.get("MUT", "0"))
EX = []


def fail(cnt, tag, *a):
    cnt[tag + "_V"] += 1
    if len(EX) < 30: EX.append((tag,) + a)


def analyse(cnt, g, start, name):
    st = RE.run(g, start); n = g.n; K = len(st) - 1; m = sum(len(s) for s in g.succ)
    key = g.key
    LO = [s["Xi"] for s in st]; HI = [s["Ut"] for s in st]
    W = [[RE.play_value(g, SP.nxs(g, s["s"], s["t"]), v) for v in range(n)] for s in st]
    if MUT == 1: HI = W
    for k in range(K + 1):
        for v in range(n):
            cnt["SQZ_chk"] += 1
            if not (key(LO[k][v]) <= key(W[k][v]) <= key(HI[k][v])): fail(cnt, "SQZ", name, k, v)
            if k < K and (key(LO[k + 1][v]) < key(LO[k][v]) or key(HI[k + 1][v]) > key(HI[k][v])): fail(cnt, "SQZM", name, k, v)
    SETs = [{v for v in range(n) if LO[k][v] == HI[k][v]} for k in range(K + 1)]
    B = []
    for k in range(K + 1):
        B.append(sum(SP.lcp(SP.CS(g, LO[k][v]), SP.CS(g, HI[k][v] if MUT != 2 else LO[min(k + 1, K)][v])) for v in range(n)))
    for k in range(K):
        if not SETs[k] <= SETs[k + 1]: fail(cnt, "SET", name, k)
        for v in range(n):
            a = SP.lcp(SP.CS(g, LO[k][v]), SP.CS(g, HI[k][v])); b = SP.lcp(SP.CS(g, LO[k + 1][v]), SP.CS(g, HI[k + 1][v]))
            if MUT == 2: a = SP.lcp(SP.CS(g, LO[k][v]), SP.CS(g, LO[k + 1][v]))
            if b < a: fail(cnt, "BR", name, k, v)
    def gap(grow):
        best = cur = 0
        for k in range(K):
            if grow(k): cur = 0
            else: cur += 1; best = max(best, cur)
        return best
    SG = gap(lambda k: SETs[k + 1] != SETs[k]); BG = gap(lambda k: B[k + 1] > B[k])
    if K > (n + 1) * (SG + 1) or K > (n * (n + 2) + 1) * (BG + 1): fail(cnt, "RED", name)
    cnt["K"] += K; cnt["SGmax"] = max(cnt["SGmax"], SG); cnt["BGmax"] = max(cnt["BGmax"], BG)
    Bb = (n * n - n + 1) * (n + m)
    k = 0
    while k < K:
        if st[k]["t"] != st[k + 1]["t"]: k += 1; continue
        a = k
        while k < K and st[k]["t"] == st[k + 1]["t"]: k += 1
        L = k - a; inc = 0; maxph = 0; ph = 0
        for j in range(a, a + L):
            t = st[j]["t"]; s = st[j]["s"]
            IW = {(y, z) for y in range(n) if g.owner[y] == 0 for z in g.succ[y] if z != s[y] and key(W[j][z]) > key(W[j][s[y]])}
            if st[j]["fb"] or set(st[j]["Is"]) != IW: inc += 1
            if j > a and [x[0] for x in W[j]] != [x[0] for x in W[j - 1]]: ph = 0
            if W[j] != W[j + 1]: ph += 1
            maxph = max(maxph, ph)
        cnt["stretches"] += 1; cnt["INC"] += inc; cnt["steps"] += L
        if L > (inc + 1) * (Bb - 1) + inc: fail(cnt, "CR", name, a)
        cnt["MAXPH"] = max(cnt["MAXPH"], maxph)
        if maxph > n - 1: cnt["PH_over"] += 1; EX.append(("PH_over", name, a, L, maxph, n - 1)) if len(EX) < 30 else None


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
            sp = os.environ.get("STARTF") or p[:-3] + ".start"; ex = None
            if os.path.exists(sp):
                try: ex = CP.parse_start(g, sp)
                except Exception: cnt["start_err"] += 1
            cnt["GAMES"] += 1; do(g, os.path.basename(p), ex)
    for k in sorted(cnt): print(k, cnt[k])
    print("VIOLATIONS", sum(v for k, v in cnt.items() if k.endswith("_V")))
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
