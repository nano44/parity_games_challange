#!/usr/bin/env python3
"""REFEREE succ. 9 probe for packet P-N5-LV2 (docs/si/P-N5-LV2-box12.md, pin 283bcb6, sha1 3b23a41f...). Own engine (rl_engine,
rl_probe.states / scope_runs; no lane code).
 STALE   STALE-GATE on EVERY game (C^1O or not): for every Even S4c fallback k0, every later state k, every gate (y, z) at k:
         Xi_k(z) != Xi_k0(z)
 EVG     (C^1O) EV-G: k0 an in-phase THR S4c fallback with (h), k > k0 in the same phase, gate (y, z) at k with z in F_k: z's play at k
         is not contained in F_k0
 SAND    (C^1O) in a scope run, after a state with r = -1: COARSE_-1(theta) unchanged
 SFB     (C^1O) per scope run: fallbacks by class (level >= 0 / level -1 with r >= 0 / r = -1 / EQ) and the bound 4 n n_E + 3;
         also the class bounds 2 n n_E, n n_E + 1, n n_E + 1, 1
Usage: lv2_probe.py files..."""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P
EX = []


def stale(g, run, cnt, name):
    for k0, a in enumerate(run):
        if not (a["fb"] and a["Is"]): continue
        for k in range(k0 + 1, len(run)):
            for y, z in run[k]["Is"]:
                cnt["STALE_chk"] += 1
                if run[k]["Xi"][z] == a["Xi"][z]: cnt["STALE_FAIL"] += 1; EX.append((name, "STALE", k0, k, y, z))


def c1o(g, cnt, name):
    o, st = P.states(g); P.OO[0] = o; n = g.n; T = len(st) - 1
    nE = sum(1 for v in range(n) if g.owner[v] == 0)
    inph, runs = P.scope_runs(st)
    # EV-G
    for k0 in range(T):
        a = st[k0]
        if not (inph[k0] and a["fb"] and a["Is"] and a["h"] and a["Xi"][o] != a["W"][o]): continue
        k = k0 + 1
        while True:
            for y, z in st[k]["Is"]:
                if z in st[k]["F"]:
                    pre, cyc = RE.lasso(st[k]["nx"], z)
                    cnt["EVG_chk"] += 1
                    if set(pre + cyc) <= a["F"]: cnt["EVG_FAIL"] += 1; EX.append((name, "EVG", k0, k, y, z))
            if k >= T or not inph[k]: break
            k += 1
    for S in runs:
        cnt["scope_runs"] += 1
        # SAND
        first = next((t for t in S + [S[-1] + 1] if st[t]["h"] and st[t]["Xi"][o] != st[t]["W"][o] and st[t]["r"] == -1), None)
        if first is not None:
            for t in range(first, S[-1] + 2):
                cnt["SAND_chk"] += 1
                if P.coarse(st[t]["Xi"][o], -1) != P.coarse(st[first]["Xi"][o], -1): cnt["SAND_FAIL"] += 1; EX.append((name, "SAND", first, t))
        cl = Counter()
        for k in S:
            a = st[k]
            if not (a["fb"] and a["Is"]): continue
            if a["Xi"][o] == a["W"][o]: cl["EQ"] += 1
            elif a["r"] == -1: cl["none"] += 1
            elif a["M"] == -1: cl["m1"] += 1
            else: cl["ge0"] += 1
        for kk, v in cl.items(): cnt["SFB_" + kk] += v
        # FLAT-ALL_-1^none at in-scope THR fallbacks with r = -1 and (h) at k+1; LV-NONE count per run
        for k in S:
            a, b = st[k], st[k + 1]
            if not (a["fb"] and a["Is"] and a["Xi"][o] != a["W"][o] and a["r"] == -1): continue
            if a["M"] != -1: cnt["NONE_M_FAIL"] += 1
            if not b["h"]: cnt["FLATN_no_h_next"] += 1; continue
            cnt["FLATN_chk"] += 1
            i1 = a["F"] <= b["F"] and all(z in a["Rb"] and (z == o or P.route(b["nx"], z, o) == P.route(a["nx"], z, o)) for z in b["Rb"])
            i2 = P.coarse(b["Xi"][o], -1) == P.coarse(a["Xi"][o], -1)
            i3 = all(P.coarse(b["Xi"][v], -1) == P.coarse(a["Xi"][v], -1) for v in range(n))
            i4 = b["M"] <= -1
            if not (i1 and i2 and i3 and i4): cnt["FLATN_FAIL"] += 1; EX.append((name, "FLATN", k, i1, i2, i3, i4))
        if cl["none"] >= 2: cnt["NONE_runs_with_2plus"] += 1
        tot = sum(cl.values()); cnt["SFB_max_per_run"] = max(cnt["SFB_max_per_run"], tot)
        if tot > 4 * n * nE + 3: cnt["SFB_FAIL"] += 1; EX.append((name, "SFB", S[0], tot))
        if cl["ge0"] > 2 * n * nE or cl["m1"] > n * nE + 1 or cl["none"] > n * nE + 1 or cl["EQ"] > 1:
            cnt["SFB_class_FAIL"] += 1; EX.append((name, "SFBclass", S[0], dict(cl)))


def main(a):
    cnt = Counter()
    for f in a:
        g = RE.parse(f)
        if g.n > 64: cnt["skip_big"] += 1; continue
        try: run = RE.run(g)
        except RuntimeError: cnt["maxit"] += 1; continue
        cnt["games"] += 1; stale(g, run, cnt, os.path.relpath(f, P.ROOT))
        try: P.assert_c1o(g)
        except AssertionError: cnt["not_c1o_stale_only"] += 1; continue
        cnt["games_c1o"] += 1; c1o(g, cnt, os.path.relpath(f, P.ROOT))
    for k in sorted(cnt): print("%-28s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:20]: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
