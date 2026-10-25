#!/usr/bin/env python3
"""REFEREE probe for packet P-N5-TOG (docs/new/P-N5-TOG-box35.md, pin d3daae1, sha1 7dfda8c8...). Own trace (u1_probe.trace = the n5.py
loop, asserted equal to n5.run); every game asserted in C^1O (exactly one Odd vertex with out-degree > 1). Written from the packet's
definitions, independent of experiments/new/box35/. PHASE = (lambda_Xi, tau) constant; c = lambda(o); U = lambda^{-1}(c).
Checks (per phase):
 LMONO   c != o: L_k = length of the cycle of c's H_k-play; Omega(c) even: L non-increasing, strict at a sigma(c) change; odd: reversed;
         sigma(c) changes <= n - 1
 ZC      Z_k = {(v, len Xi_k v) : v in U, P(Xi_k v) = {}}: per v the P = {} states form an interval with monotone length; #Z-changes <= |U|(n+1)
 TOG     every in-phase H1-toggle with c != o and Z_{k+1} = Z_k changes next(c), and c is Even; c = o: no toggle in the phase
 TC      toggles <= T = |U|(n+1) + n - 1, drops <= ceil(T/2)
 RS      maximal (h)-runs <= 1 + T + f; every (h)-run start inside the phase is an H1-toggle or an Even S4c fallback from H1 and not H2
 XSN     X_SN (S4a crossings k -> k+1 with c_w = c_theta at k) <= 13 (d_o+1) n^3 (f + 1 + T) + T; also the exact accounting
         X_SN <= sum_Q (C_P(Q) + [transition out of P(Q) is a crossing]) and the count of crossings out of a prefix (TOG-1)
Usage: tog_probe.py game.pg ... | tog_probe.py lib | tog_probe.py rand|randb N nmin nmax seed"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U, l2_probe as L2
from fb_probe import lev, BOT, INF

EX = []


def cyc_len(H, c):
    x, d = H[c], 1
    while x != c:
        x = H[x]; d += 1
        if d > len(H): return None
    return d


def run(g, cnt, name=""):
    n = g.n; E, o, st, it, nfb = L2.states(g); T = len(st) - 1; do = len(set(g.succ[o]))
    inph = [st[k]["key"] == st[k + 1]["key"] for k in range(T)]
    k = 0
    while k <= T:
        j = k
        while j < T and inph[j]: j += 1
        phase(g, E, st, list(range(k, j + 1)), cnt, o, do, name); k = j + 1
    return it, nfb


def phase(g, E, st, Ps, cnt, o, do, name):
    n = g.n; cnt["phases"] += 1; lam = [x[0] for x in st[Ps[0]]["Xi"]]; c = lam[o]; Uset = [v for v in range(n) if lam[v] == c]
    trs = Ps[:-1]  # transitions t -> t+1 inside the phase
    tog = [t for t in trs if st[t]["H1"] != st[t + 1]["H1"]]; drops = [t for t in tog if st[t]["H1"]]
    f = sum(st[t]["fb"] for t in trs)
    Tb = len(Uset) * (n + 1) + n - 1
    if c == o:
        cnt["phases_c_eq_o"] += 1
        if tog: cnt["TOG_ceqo_FAIL"] += 1; EX.append((name, "TOGceqo", Ps[0]))
    else:
        Ls = [cyc_len(st[t]["H"], c) for t in Ps]
        if None in Ls: cnt["LMONO_nocycle_FAIL"] += 1
        else:
            even = E.par[c] == 0; sch = 0
            for t in trs:
                a, b = Ls[t - Ps[0]], Ls[t + 1 - Ps[0]]; changed = st[t]["H"][c] != st[t + 1]["H"][c]
                ok = (b <= a if even else b >= a) and (not changed or (b < a if even else b > a))
                if not ok: cnt["LMONO_FAIL"] += 1; EX.append((name, "LMONO", t))
                sch += changed
            cnt["max_sigma_c_changes"] = max(cnt["max_sigma_c_changes"], sch)
            if sch > n - 1: cnt["LMONO_count_FAIL"] += 1
    # Z-COUNT
    Z = [frozenset((v, st[t]["Xi"][v][2]) for v in Uset if st[t]["Xi"][v][1] == 0) for t in Ps]
    for v in Uset:
        I = [t for t in Ps if st[t]["Xi"][v][1] == 0]
        if I and I != list(range(I[0], I[-1] + 1)): cnt["ZC_interval_FAIL"] += 1
        ls = [st[t]["Xi"][v][2] for t in I]; d = [ls[i + 1] - ls[i] for i in range(len(ls) - 1)]
        if any(x > 0 for x in d) and any(x < 0 for x in d): cnt["ZC_mono_FAIL"] += 1
    zch = sum(Z[i] != Z[i + 1] for i in range(len(Ps) - 1))
    if zch > len(Uset) * (n + 1): cnt["ZC_FAIL"] += 1
    cnt["max_Z_changes"] = max(cnt["max_Z_changes"], zch)
    # TOGGLE
    for t in tog:
        cnt["toggles"] += 1; i = t - Ps[0]; zsame = Z[i] == Z[i + 1]; csw = st[t]["H"][c] != st[t + 1]["H"][c]
        cnt["tog_fb"] += st[t]["fb"]
        cnt["tog_" + ("Zsame" if zsame else "Zchg") + ("_csw" if csw else "_cfix")] += 1
        if zsame and (not csw or g.owner[c] != 0): cnt["TOG_FAIL"] += 1; EX.append((name, "TOG", t))
    if len(tog) > Tb or len(drops) > (Tb + 1) // 2: cnt["TC_FAIL"] += 1
    cnt["max_toggles"] = max(cnt["max_toggles"], len(tog)); cnt["max_drops"] = max(cnt["max_drops"], len(drops))
    # RESTARTS
    hr = 0; prev = False
    for t in Ps:
        if st[t]["h"] and not prev:
            hr += 1
            if t > Ps[0]:
                a = st[t - 1]; cnt["RS_restarts"] += 1
                if a["H1"] != st[t]["H1"]: cnt["RS_by_toggle"] += 1
                elif a["fb"] and a["H1"] and not a["H2"] and a["Is"]: cnt["RS_by_evenfb"] += 1
                else: cnt["RS_FAIL"] += 1; EX.append((name, "RS", t - 1))
        prev = st[t]["h"]
    if hr > 1 + Tb + f: cnt["RS_count_FAIL"] += 1
    cnt["max_hruns"] = max(cnt["max_hruns"], hr)
    # X-SN-PHASE
    sn = lambda t: st[t]["W"][o][0] == st[t]["Xi"][o][0]
    XSN = sum(1 for t in trs if not st[t]["fb"] and sn(t) and st[t]["R"] != st[t + 1]["R"])
    if XSN > 13 * (do + 1) * n ** 3 * (f + 1 + Tb) + Tb: cnt["XSN_FAIL"] += 1
    cnt["max_XSN"] = max(cnt["max_XSN"], XSN)
    # exact accounting by fallback-free runs: crossings out of the SN prefix (the transition from P's last state)
    q = Ps[0]
    while q < Ps[-1]:
        if st[q]["fb"]: q += 1; continue
        e = q
        while e + 1 < Ps[-1] and not st[e + 1]["fb"]: e += 1
        Q = list(range(q, e + 2)); q = e + 1; P = []
        for t in Q:
            if sn(t): P.append(t)
            else: break
        if P and P[-1] < Q[-1] and st[P[-1]]["R"] != st[P[-1] + 1]["R"]:
            cnt["XSN_cross_out_of_P"] += 1
            if cnt["XSN_cross_out_of_P"] <= 3: EX.append((name, "XSN_out_of_P", P[-1]))


def merge(cnt, c):
    for k, v in c.items(): cnt[k] = max(cnt[k], v) if k.startswith("max") else cnt[k] + v


if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0] in ("rand", "randb"):
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for _ in range(N):
            g = U.rand_c1o(rng, lo, hi)
            if g is None: continue
            if a[0] == "randb":
                o = U.assert_c1o(g)
                sc = [sorted(set(g.succ[v]) | ({o} if v != o and g.owner[v] == 0 and rng.random() < 0.25 else set())) for v in range(g.n)]
                sc[o] = sorted(set(sc[o]) | set(rng.sample(range(g.n), min(g.n, 3))))
                g = U.pg.Game(list(g.prio), list(g.owner), sc)
            cnt["runs"] += 1; c = Counter(); run(g, c); merge(cnt, c)
    else:
        files = L2.libfiles() if a[0] == "lib" else a
        for p in files:
            c = Counter(); it, fb = run(U.load(p), c, os.path.basename(p)); cnt["files"] += 1; merge(cnt, c)
            if len(files) < 6: print(p, "iterations", it, "fallbacks", fb, {k: v for k, v in sorted(c.items()) if not k.startswith("tog_")}, flush=True)
            elif any("FAIL" in k for k in c): print(p, {k: v for k, v in c.items() if "FAIL" in k}, flush=True)
    print(dict(sorted(cnt.items())))
    for e in EX[:30]: print("  ", e)
