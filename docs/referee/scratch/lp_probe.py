#!/usr/bin/env python3
"""REFEREE probe for packet P-N5-LP (docs/new/P-N5-LP-box32.md, pin bc42f2c, sha1 d2c8121a...). Own trace (u1_probe.trace = the n5.py loop,
asserted equal to n5.run); phase = (lambda_Xi, tau) constant (the packet's definition), transitions with both ends in it.
Checks per in-phase transition: U (L_k < inf; COARSE_{L_k} Xi frozen), HI (+ its Consequence on M), UL, GR (a)/(b), NU run bound,
Theorem LP (both inequalities), DF (C^1O only; every arena edge (y, z) of H_k that is a gate edge at k+1 at an S4a step: sigma_{k+1}(y) in
R_{k+1}; split by whether y is its own W-cycle node at k+1), and DF's first step (W_{k+1}(z) <= W_{k+1}(a)).
Usage: lp_probe.py game.pg ... | lp_probe.py rand N nmin nmax seed [c1o]"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U, pg
from fb_probe import lev, coarse, BOT, INF, rand_game

def run(g, cnt, c1o):
    n = g.n; o = U.assert_c1o(g) if c1o else None
    E, Ed, out, it, fb = U.trace(g); st = []
    for (s, t, f, Is, s4a) in out:
        Xi, sb = E.evaluate(s); W = U.wval(g, E, s, t)
        R = frozenset(v for v in range(n) if U.reaches(U.nxt_of(g, s, t), v, o)) if c1o else None
        gl = [lev(Xi[s[y]], Xi[z]) for y, z in Is]
        st.append(dict(s=s, t=t, fb=f, s4a=s4a, Is=Is, Xi=Xi, sb=sb, W=W, R=R, M=max(gl) if gl else BOT,
                       lam=tuple(x[0] for x in Xi), ph=(tuple(x[0] for x in Xi), t)))
    i = 0
    while i < len(st):
        j = i
        while j + 1 < len(st) and st[j + 1]["ph"] == st[i]["ph"]: j += 1
        phase(g, E, st[i:j + 1], cnt, o); i = j + 1

def key(E, x): return E.key(x)

def phase(g, E, P, cnt, o):
    n = g.n; T = len(P) - 1
    if T <= 0: return
    cnt["phases"] += 1; m = sum(len(set(s)) for s in g.succ)
    Ls = []
    for k in range(T):
        a, b = P[k], P[k + 1]; lam = a["lam"]; L = BOT; evenL = BOT; relE = []
        for v in range(n):
            if lam[v] == v: continue
            if g.owner[v] == 0 and a["s"][v] != b["s"][v]:
                l = lev(a["Xi"][a["s"][v]], a["Xi"][b["s"][v]]); L = max(L, l); evenL = max(evenL, l); relE.append((v, l))
            if g.owner[v] == 1 and a["sb"][v] != b["sb"][v]:
                L = max(L, lev(a["Xi"][a["sb"][v]], a["Xi"][b["sb"][v]]))
        Ls.append((L, evenL))
        cnt["tr"] += 1
        if L >= INF: cnt["U_Linf_FAIL"] += 1; continue
        if any(coarse(a["Xi"][v], L) != coarse(b["Xi"][v], L) for v in range(n)): cnt["U_FAIL"] += 1
        if L == BOT: cnt["NU"] += 1; continue
        cnt["rel"] += 1
        # HI: y Even, not (own cycle node and switched)
        for y in range(n):
            if g.owner[y] != 0 or (lam[y] == y and a["s"][y] != b["s"][y]): continue
            for z in g.succ[y]:
                ga = z != a["s"][y] and key(E, a["Xi"][z]) > key(E, a["Xi"][a["s"][y]])
                gb = z != b["s"][y] and key(E, b["Xi"][z]) > key(E, b["Xi"][b["s"][y]])
                la = lev(a["Xi"][a["s"][y]], a["Xi"][z]); lb = lev(b["Xi"][b["s"][y]], b["Xi"][z])
                if (ga and la > L) != (gb and lb > L) or (ga and la > L and la != lb): cnt["HI_FAIL"] += 1
        Mk, Mk1 = a["M"], b["M"]
        if Mk > L and Mk1 != Mk: cnt["HIcons_FAIL"] += 1
        if Mk == L and Mk1 > L: cnt["HIcons_FAIL"] += 1
        # UL
        if L >= 0 and evenL == L and any(E.rank[v] == L and l == L for v, l in relE) and \
                not any(E.rank[v] != L and l == L for v, l in relE): cnt["UL_FAIL"] += 1
        # GR
        for l in range(n):
            def G(x): return {v for v in range(n) if E.rank[lam[v]] < l and (x["Xi"][v][1] >> l & 1) == (1 - E.rankpar[l])}
            Ga, Gb = G(a), G(b)
            if L <= l and not Ga <= Gb: cnt["GRa_FAIL"] += 1
            if L == l and evenL == L:
                for v, lv in relE:
                    if lv == L and not (v not in Ga and v in Gb): cnt["GRb_FAIL"] += 1
        # DF (C^1O, S4a step)
        if o is not None and a["s4a"] and not a["fb"]:
            arena = {y: {a["s"][y]} for y in range(n) if g.owner[y] == 0}
            for y, z in a["Is"]: arena[y].add(z)
            for y in arena:
                A = b["s"][y]
                for z in arena[y]:
                    if z == A or not key(E, b["Xi"][z]) > key(E, b["Xi"][A]): continue
                    own = b["W"][y][0] == y; cnt["DF_cases" + ("_ownW" if own else "")] += 1
                    if A not in b["R"]: cnt["DF_FAIL" + ("_ownW" if own else "")] += 1
                    if key(E, b["W"][z]) > key(E, b["W"][A]): cnt["DFstep1_FAIL" + ("_ownW" if own else "")] += 1
    # NU runs and Theorem LP
    nu = 0; Trel = sum(1 for L, _ in Ls if L != BOT)
    for L, _ in Ls + [(0, 0)]:
        if L == BOT: nu += 1
        else:
            if nu > m - n: cnt["NU_FAIL"] += 1
            nu = 0
    rel = [(L, e) for L, e in Ls if L != BOT]
    rho = sum(1 for x in range(1, len(rel)) if rel[x][0] > rel[x - 1][0]); eps = sum(1 for L, e in rel if e != L)
    if T > (m - n + 1) * (Trel + 1): cnt["LP1_FAIL"] += 1
    if Trel > (n + 1) * (rho + 1) * n * (n - 1) + eps: cnt["LP2_FAIL"] += 1
    cnt["max_rho"] = max(cnt["max_rho"], rho)

if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); c1o = len(a) > 5; rng = random.Random(seed)
        for _ in range(N):
            g = U.rand_c1o(rng, lo, hi) if c1o else rand_game(rng, lo, hi)
            if g is not None: cnt["runs"] += 1; run(g, cnt, c1o)
    else:
        for p in a:
            c = Counter(); run(U.load(p), c, True)
            if any("FAIL" in k for k in c): print(p, {k: v for k, v in c.items() if "FAIL" in k})
            for k, v in c.items(): cnt[k] = max(cnt[k], v) if "max" in k else cnt[k] + v
    print(dict(sorted(cnt.items())))
