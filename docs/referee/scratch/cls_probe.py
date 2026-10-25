#!/usr/bin/env python3
"""REFEREE probe for packet P-N5-CLS (docs/si/P-N5-CLS-box8.md, pin 486107a, sha1 5bbfd872...). Own trace (u1_probe.trace = the n5.py
loop, asserted equal to n5.run). PHASE = joint lambda-phase with tau constant: key (lambda_Xi, lambda_U, tau) (the packet's R21 setting).
Every game asserted in C^1O (exactly one Odd vertex with out-degree > 1). Written from the packet's definitions, independent of
experiments/si/coarse/.
Checks:
 C5/C6   on triples of state valuations; C7use: under (h), lev(Xi(q), W(q)) = r and Xi(q) < W(q) for q in R (the use in CLU / NL)
 KIND    under (h): theta = w  =>  Xi = W pointwise (THR / EQ exhaustive)
 FACTR   r non-increasing along scope runs
 CLU     in-phase fallback, (h), theta < w: switched R -> F edges have level <= r
 TRANS   TRANSFER for every in-phase transition, gate at k+1, L in [-1, n-1]
 OFFG    gates at k+1 into V \\ Rbar_{k+1} have level <= M_k; OGP = the refuted OG' (bound MF_k), counted, not a failure
 CN      in-phase switch at y with lambda(y) = y: level -1
 NL      S4a in-phase, (h) at j, every L with MF_j <= L < r_j ((A_j) holds): (i), (ii), (iii)
 CLS1    scope runs: fallback k1 THR with r >= 0: M_{k1} <= min M of the earlier fallbacks of the run; kinds of in-scope fallbacks
 FBL     at in-phase THR (u* != none) fallbacks: switched edges are R -> F, or own-cycle-node switches (lambda(y) = y)
Usage: cls_probe.py game.pg ... | cls_probe.py lib | cls_probe.py rand N nmin nmax seed"""
import sys, os, random, glob, itertools
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U
from fb_probe import lev, coarse, BOT, INF


def states(g):
    n = g.n; o = U.assert_c1o(g)
    E, Ed, out, it, fb = U.trace(g); st = []
    for (s, t, f, Is, s4a) in out:
        Xi, sb = E.evaluate(s); Ux, _ = Ed.evaluate(t); W = U.wval(g, E, s, t)
        nx = U.nxt_of(g, s, t); H = [s[v] if g.owner[v] == 0 else sb[v] for v in range(n)]
        R = frozenset(v for v in range(n) if v != o and U.reaches(nx, v, o)); Rb = R | {o}
        H1 = not U.returns(H, o); H2 = not U.returns(nx, o); H3 = Xi[o][0] == W[o][0]
        gl = [(y, z, lev(Xi[s[y]], Xi[z])) for y, z in Is]
        st.append(dict(s=s, t=t, fb=bool(f), Is=Is, Xi=Xi, sb=sb, W=W, R=R, Rb=Rb, H2=H2, h=H1 and H2 and H3,
                       r=lev(Xi[o], W[o]), M=max([l for _, _, l in gl], default=BOT),
                       MF=max([l for y, z, l in gl if z not in Rb], default=BOT), gl=gl,
                       key=(tuple(x[0] for x in Xi), tuple(x[0] for x in Ux), t)))
    return E, o, st


def run(g, cnt, name=""):
    n = g.n; E, o, st = states(g); key = E.key
    for a in st:  # C5 / C6 on valuation triples, KIND
        vals = sorted(set(a["Xi"]), key=key)[:12]
        for x, y, z in itertools.combinations(vals, 3):  # x < y < z in Even's order
            cnt["C5_chk"] += 1
            if lev(x, y) > lev(x, z): cnt["C5_FAIL"] += 1
            if lev(x, z) > max(lev(x, y), lev(y, z)): cnt["C6_FAIL"] += 1
        if a["h"]:
            if a["r"] == BOT and any(a["Xi"][v] != a["W"][v] for v in range(n)): cnt["KIND_FAIL"] += 1
            if a["r"] != BOT:
                for q in a["R"]:
                    cnt["C7use_chk"] += 1
                    if lev(a["Xi"][q], a["W"][q]) != a["r"] or not key(a["Xi"][q]) < key(a["W"][q]): cnt["C7use_FAIL"] += 1
    T = len(st) - 1; inph = [st[k]["key"] == st[k + 1]["key"] for k in range(T)]
    for k in range(T):
        if not inph[k]: continue
        a, b = st[k], st[k + 1]; cnt["tr"] += 1
        sw = [(y, b["s"][y], lev(a["Xi"][a["s"][y]], a["Xi"][b["s"][y]])) for y in range(n)
              if g.owner[y] == 0 and a["s"][y] != b["s"][y]]
        # CN
        for y, z, l in sw:
            if a["Xi"][y][0] == y:
                cnt["CN_chk"] += 1
                if l != -1: cnt["CN_FAIL"] += 1
        # TRANSFER, OFFGATE, OG'
        gk = {(y, z): l for y, z, l in a["gl"]}
        for y, z, l in b["gl"]:
            for L in range(-1, n):
                if l > L and coarse(a["Xi"][z], L) == coarse(b["Xi"][z], L):
                    cnt["TRANS_chk"] += 1
                    if not ((y, z) in gk and gk[(y, z)] > L): cnt["TRANS_FAIL"] += 1
            if z not in b["Rb"]:
                cnt["OFFG_chk"] += 1
                if l > a["M"]: cnt["OFFG_FAIL"] += 1
                if l > a["MF"]: cnt["OGP_viol"] += 1; print("  OG'", name, k, (y, z), l, "MF_k", a["MF"], "M_k", a["M"], "fb", a["fb"], flush=True)
        # CLU, FBL
        if a["fb"] and a["h"] and a["r"] != BOT:
            for y, z, l in sw:
                if y in a["R"] and z not in a["Rb"]:
                    cnt["CLU_chk"] += 1
                    if l > a["r"]: cnt["CLU_FAIL"] += 1
                if a["r"] >= 0 and not ((y in a["R"] and z not in a["Rb"]) or a["Xi"][y][0] == y): cnt["FBL_FAIL"] += 1
        # NL
        if not a["fb"] and a["h"] and a["r"] != BOT:
            for L in range(max(a["MF"], BOT), a["r"]):
                cnt["NL_chk"] += 1
                if any(coarse(a["Xi"][v], L) != coarse(b["Xi"][v], L) for v in range(n) if v not in b["Rb"]): cnt["NLi_FAIL"] += 1
                if not a["R"] <= b["Rb"]: cnt["NLii_FAIL"] += 1
                if b["MF"] > L: cnt["NLiii_FAIL"] += 1
    # scope runs
    k = 0
    while k < T:
        def ins(j): return inph[j] and st[j]["h"] and st[j + 1]["H2"] and st[j + 1]["W"][o] == st[j]["W"][o]
        if not ins(k): k += 1; continue
        j = k
        while j + 1 < T and ins(j + 1): j += 1
        S = range(k, j + 1); cnt["scope_runs"] += 1; k = j + 1
        rs = [st[x]["r"] for x in range(S.start, S.stop + 1)]
        if any(rs[x + 1] > rs[x] for x in range(len(rs) - 1)): cnt["FACTR_FAIL"] += 1
        prevM = []
        for x in S:
            if not st[x]["fb"]: continue
            a = st[x]; kind = "THRu" if a["r"] >= 0 else ("THR0" if a["r"] == -1 else "EQ")
            cnt["scope_fb_" + kind] += 1
            if prevM and a["M"] > min(prevM):
                cnt["Mup_" + kind] += 1
                if kind == "THRu": cnt["CLS1_FAIL"] += 1
                print("  M rise", name, x, kind, a["M"], "min prev", min(prevM), flush=True)
            prevM.append(a["M"]); cnt["CLS1_chk"] += kind == "THRu"
        cnt["max_scope_fb"] = max(cnt["max_scope_fb"], len(prevM))


def merge(cnt, c):
    for k, v in c.items(): cnt[k] = max(cnt[k], v) if k.startswith("max") else cnt[k] + v


if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for _ in range(N):
            g = U.rand_c1o(rng, lo, hi)
            if g is not None: cnt["runs"] += 1; run(g, cnt)
    else:
        files = a
        if a[0] == "lib":
            files = []
            for p in sorted(glob.glob("experiments/**/*.pg", recursive=True)):
                try: g = U.load(p)
                except Exception: continue
                if g.n <= 64 and sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) == 1: files.append(p)
        for p in files:
            c = Counter(); run(U.load(p), c, os.path.basename(p)); cnt["files"] += 1; merge(cnt, c)
            if any("FAIL" in k for k in c): print(p, {k: v for k, v in c.items() if "FAIL" in k}, flush=True)
    print(dict(sorted(cnt.items())))
