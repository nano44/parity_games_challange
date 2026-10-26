#!/usr/bin/env python3
"""REFEREE probe for packet P-N5-SCOPE (docs/new/P-N5-SCOPE-box36.md, pin 8998ee6, sha1 c3f5ed37...). Own trace (u1_probe.trace = the n5.py
loop, asserted equal to n5.run). Written from the packet's definitions, independent of experiments/new/box35/.
Every game (general random games too):
 KEY     at every transition with tau unchanged, lambda_U (cycle nodes of Odd's valuation of tau on the dual) is unchanged
 CNL     Even S4c fallback whose gates all have lambda(y) = y and level -1: (i) Xi_{k+1} = Xi_k, (ii) Isigma_{k+1} empty, (iii) the next
         transition changes tau or N5 stops (k+1 is the last state of its (lambda_Xi, tau) phase)
C^1O only (exactly one Odd vertex with out-degree > 1, asserted); PHASE = (lambda_Xi, tau); R excludes o:
 WCH     H2 at both ends and w changing: crossing, or Xi changes at t0 = tau(o) in F; per phase <= (n - 2)(X + 1) + X
 SC      scope runs per phase <= #(h)-runs + #WCH <= (1 + T + f) + (n - 2)(X + 1) + X
 FBI     every non-tame in-phase transition is a crossing; every maximal run of non-crossing in-phase transitions has <= n_E(2n - 1) fallbacks
 NH1     fallbacks of a phase at not-H1 states <= n_E(2n - 1)(ceil(T/2) + 1) + T
Usage: scope_probe.py game.pg ... | lib | rand N nmin nmax seed | gen N nmin nmax seed"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U, l2_probe as L2
from fb_probe import lev, coarse, BOT, INF, rand_game

EX = []


def general(g, cnt, name):
    """KEY and CN-LAST on any game (own trace)."""
    n = g.n; E, Ed, out, it, fb = U.trace(g); st = []
    for (s, t, f, Is, s4a) in out:
        Xi, sb = E.evaluate(s); Ux, _ = Ed.evaluate(t)
        st.append(dict(s=s, t=t, fb=bool(f), Is=list(Is), Xi=Xi, lam=tuple(x[0] for x in Xi), lamU=tuple(x[0] for x in Ux)))
    for k in range(len(st) - 1):
        a, b = st[k], st[k + 1]
        if a["t"] == b["t"]:
            cnt["KEY_chk"] += 1
            if a["lamU"] != b["lamU"]: cnt["KEY_FAIL"] += 1; EX.append((name, "KEY", k))
        if a["fb"] and a["Is"]:
            gl = [(y, z, lev(a["Xi"][a["s"][y]], a["Xi"][z])) for y, z in a["Is"]]
            cnt["evenfb"] += 1; cnt["evenfb_lvm1"] += all(l == -1 for _, _, l in gl)
            if all(a["lam"][y] == y and l == -1 for y, z, l in gl):
                cnt["CNL_chk"] += 1
                if b["Xi"] != a["Xi"]: cnt["CNLi_FAIL"] += 1; EX.append((name, "CNLi", k))
                if b["Is"]: cnt["CNLii_FAIL"] += 1; EX.append((name, "CNLii", k))
                if k + 1 < len(st) - 1 and st[k + 2]["t"] == b["t"]: cnt["CNLiii_FAIL"] += 1; EX.append((name, "CNLiii", k))
                if k + 1 == len(st) - 1: cnt["CNL_stop"] += 1
            elif all(l == -1 for _, _, l in gl): cnt["evenfb_lvm1_noncycle"] += 1


def c1o(g, cnt, name):
    n = g.n; nE = sum(1 for v in range(n) if g.owner[v] == 0); E, o, st, it, nfb = L2.states(g); T_ = len(st) - 1
    for a in st:
        gl = [lev(a["Xi"][a["s"][y]], a["Xi"][z]) for y, z in a["Is"]]; a["M"] = max(gl, default=BOT)
    inph = [st[k]["key"] == st[k + 1]["key"] for k in range(T_)]
    k = 0
    while k <= T_:
        j = k
        while j < T_ and inph[j]: j += 1
        phase(g, E, st, list(range(k, j + 1)), cnt, o, nE, name); k = j + 1


def phase(g, E, st, Ps, cnt, o, nE, name):
    n = g.n; cnt["phases"] += 1; trs = Ps[:-1]
    lam = [x[0] for x in st[Ps[0]]["Xi"]]; c = lam[o]; Usz = sum(1 for v in range(n) if lam[v] == c)
    cross = {t: st[t]["R"] != st[t + 1]["R"] for t in trs}; X = sum(cross.values()); f = sum(st[t]["fb"] for t in trs)
    tog = [t for t in trs if st[t]["H1"] != st[t + 1]["H1"]]; T = len(tog)
    # WCH
    wch = []
    for t in trs:
        a, b = st[t], st[t + 1]
        if a["H2"] and b["H2"] and a["W"][o] != b["W"][o]:
            wch.append(t); t0 = a["t"][o]; cnt["WCH_tr"] += 1
            if not cross[t] and (t0 in a["R"] or t0 == o or a["Xi"][t0] == b["Xi"][t0]): cnt["WCH_FAIL"] += 1; EX.append((name, "WCH", t))
    if len(wch) > (n - 2) * (X + 1) + X: cnt["WCH_count_FAIL"] += 1
    cnt["max_WCH"] = max(cnt["max_WCH"], len(wch))
    # (h)-runs and scope runs
    hr = sum(1 for t in Ps if st[t]["h"] and (t == Ps[0] or not st[t - 1]["h"]))
    ins = {t: st[t]["h"] and st[t + 1]["H2"] and st[t + 1]["W"][o] == st[t]["W"][o] for t in trs}
    sc = sum(1 for t in trs if ins[t] and (t == Ps[0] or not ins[t - 1]))
    Tb = Usz * (n + 1) + n - 1
    if sc > hr + len(wch): cnt["SC_FAIL"] += 1; EX.append((name, "SC", Ps[0], sc, hr, len(wch)))
    if sc > (1 + Tb + f) + (n - 2) * (X + 1) + X: cnt["SC_bound_FAIL"] += 1
    cnt["max_scope_runs"] = max(cnt["max_scope_runs"], sc); cnt["scope_runs"] += sc
    # FB-INT: non-tame => crossing; per maximal non-crossing run <= n_E(2n - 1)
    for t in trs:
        a, b = st[t], st[t + 1]; M = a["M"]
        tame = M >= INF or all(coarse(a["Xi"][v], M) == coarse(b["Xi"][v], M) for v in range(n))
        if not tame:
            cnt["nontame"] += 1
            if not cross[t]: cnt["FBI_nontame_FAIL"] += 1; EX.append((name, "FBInt", t))
    run_fb = 0; mx = 0
    for t in trs:
        if cross[t]: run_fb = 0; continue
        run_fb += st[t]["fb"]; mx = max(mx, run_fb)
        if run_fb > nE * (2 * n - 1): cnt["FBI_FAIL"] += 1; EX.append((name, "FBI", t))
    cnt["max_fb_noncross_run"] = max(cnt["max_fb_noncross_run"], mx)
    # NH1-FB
    nh = sum(1 for t in trs if st[t]["fb"] and not st[t]["H1"]); cnt["NH1_fb"] += nh
    if nh > nE * (2 * n - 1) * ((T + 1) // 2 + 1) + T: cnt["NH1_FAIL"] += 1
    cnt["max_NH1_fb"] = max(cnt["max_NH1_fb"], nh)


def merge(cnt, c):
    for k, v in c.items(): cnt[k] = max(cnt[k], v) if k.startswith("max") else cnt[k] + v


if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0] in ("rand", "gen"):
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_game(rng, lo, hi) if a[0] == "gen" else U.rand_c1o(rng, lo, hi)
            if g is None: continue
            cnt["runs"] += 1; c = Counter(); general(g, c, "%s%d" % (a[0], i))
            if a[0] == "rand": c1o(g, c, "rand%d" % i)
            merge(cnt, c)
    else:
        files = L2.libfiles() if a[0] == "lib" else a
        for p in files:
            g = U.load(p); c = Counter(); general(g, c, os.path.basename(p)); c1o(g, c, os.path.basename(p)); cnt["files"] += 1; merge(cnt, c)
            if any("FAIL" in k for k in c): print(p, {k: v for k, v in c.items() if "FAIL" in k}, flush=True)
    print(dict(sorted(cnt.items())))
    for e in EX[:30]: print("  ", e)
