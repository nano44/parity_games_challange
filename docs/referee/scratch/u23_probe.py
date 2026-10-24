#!/usr/bin/env python3
"""REFEREE probe for packet P-N5-U23 (docs/new/P-N5-U23-box31.md, pin 7666336, sha1 ee3e5d1e...). Own trace (u1_probe.trace = the n5.py
loop, asserted equal to n5.run). Definitions from the packet §0-§2:
 phase = (lambda_Xi, lambda_U, tau) constant; STRETCH = maximal run of a phase with R, theta, w constant (transitions with both ends in it);
 W-flat run = maximal run of consecutive non-fallback transitions of a stretch with W unchanged on R;
 U2: not H1, c_theta != o, W frame in route form (H2 or lambda_W(o) = o); U3: not H2, c_w != o, honest frame in route form (H1 or
 lambda_Xi(o) = o); U23: not H1, not H2, c_theta != o, c_w != o.
Checks:
 U2   CASC-U2: switching R-vertex (Even, != o) of level |pi_v| switches only at run steps <= |pi_v| - 2; corollary bound
 U3   kinds (A: c_w on pi_v), events (a switching Even R-vertex changes kind, or c_w switches), event-free sub-runs;
      KCONST kinds constant on event-free sub-runs; (i) kind B switches at sub-run steps <= |pi_v| - 2;
      (ii) kind A at steps <= L_B + lambda(v) - 3 (packet form) -- and the corrected form with T := max(0, L_B - 1): <= T + lambda - 2;
      (iii) no switch at steps >= 2|R| - 4; corollary bound f + K_W + E + (K_W + f + E + 1)(2|R| - 4)
Every game asserts exactly one Odd vertex with out-degree > 1.
Usage: u23_probe.py game.pg ... | u23_probe.py rand N nmin nmax seed"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U

def run(g, cnt, name=None):
    o = U.assert_c1o(g); E, Ed, out, it, fb = U.trace(g); rows = U.states(g, E, Ed, out, o); n = g.n
    cnt["runs"] += 1
    a = 0
    for i in range(1, len(rows) + 1):
        if i == len(rows) or any(rows[i][key] != rows[a][key] for key in ("ph", "R")) or rows[i]["Xk"][o] != rows[a]["Xk"][o] \
                or rows[i]["Wk"][o] != rows[a]["Wk"][o]:
            stretch(g, E, o, rows[a:i], cnt, name); a = i

def classify(r, o):
    ct, cw = r["Xi"][o][0], r["W"][o][0]
    hf = r["H1"] or ct == o; wf = r["H2"] or cw == o
    if not r["H1"] and ct != o and wf: return "U2"
    if not r["H2"] and cw != o and hf: return "U3"
    if not r["H1"] and not r["H2"] and ct != o and cw != o: return "U23"
    return None

def stretch(g, E, o, S, cnt, name):
    typ = classify(S[0], o)
    if typ is None: return
    if any(classify(r, o) != typ for r in S): cnt["class_not_const_FAIL"] += 1; return
    n = g.n; R = S[0]["R"]; T = len(S) - 1; cnt["stretch_" + typ] += 1
    cw = S[0]["W"][o][0]
    f = sum(S[i]["fb"] for i in range(T))
    KW = sum(1 for i in range(T) if not S[i]["fb"] and any(S[i]["W"][v] != S[i + 1]["W"][v] for v in R))
    chg = sum(1 for i in range(T) if any(S[i]["Xk"][v] != S[i + 1]["Xk"][v] or S[i]["Wk"][v] != S[i + 1]["Wk"][v]
                                          or S[i]["s"][v] != S[i + 1]["s"][v] for v in R))
    Rl = [v for v in R if v != o]
    def sw(i, v): return g.owner[v] == 0 and S[i]["s"][v] != S[i + 1]["s"][v]
    flat = [not S[i]["fb"] and all(S[i]["W"][v] == S[i + 1]["W"][v] for v in R) for i in range(T)]
    runs = []; i = 0
    while i < T:
        if not flat[i]: i += 1; continue
        j = i
        while j < T and flat[j]: j += 1
        runs.append((i, j)); i = j
    cnt[typ + "_Wflat_runs"] += len(runs)
    if typ == "U2":
        if chg > f + KW + (KW + f + 1) * (len(R) - 2): cnt["U2_cor_FAIL"] += 1
        for (a, b) in runs:
            for st in range(a, b):
                for v in Rl:
                    if sw(st, v):
                        cnt["U2_switches"] += 1; lv = len(U.play_to(S[st]["nx"], v, o))
                        if st - a > lv - 2: cnt["U2_CASC_FAIL"] += 1
        return
    # U3 / U23
    def kind(r, v): return "A" if cw in U.play_to(r["nx"], v, o) else "B"
    E_tr = 0; ev = [False] * T
    for i in range(T):
        e = False
        for v in Rl:
            if sw(i, v) and (v == cw or kind(S[i], v) != kind(S[i + 1], v)): e = True
        ev[i] = e; E_tr += e and flat[i]
    if chg > f + KW + E_tr + (KW + f + E_tr + 1) * (2 * len(R) - 4): cnt["U3_cor_FAIL"] += 1
    cnt["U3_events"] += E_tr
    for (a, b) in runs:
        st = a
        while st < b:
            if ev[st]: st += 1; continue
            s0 = st
            while st < b and not ev[st]: st += 1
            sub(g, o, cw, S, s0, st, Rl, kind, sw, cnt, len(R))

def sub(g, o, cw, S, a, b, Rl, kind, sw, cnt, nR):
    cnt["U3_subruns"] += 1
    kinds = [{v: kind(S[i], v) for v in Rl} for i in range(a, b + 1)]
    if any(k != kinds[0] for k in kinds): cnt["U3_KCONST_FAIL"] += 1
    KB = [v for v in Rl if kinds[0][v] == "B"]
    LB = max((len(U.play_to(S[a]["nx"], v, o)) for v in KB), default=0)
    if not KB: cnt["U3_subruns_noKindB"] += 1
    Tc = max(0, LB - 1)
    for st in range(a, b):
        for v in Rl:
            if not sw(st, v): continue
            s = st - a; cnt["U3_switches"] += 1
            if s >= 2 * nR - 4: cnt["U3_iii_FAIL"] += 1
            if kinds[0][v] == "B":
                cnt["U3_switches_B"] += 1
                if s > len(U.play_to(S[st]["nx"], v, o)) - 2: cnt["U3_i_FAIL"] += 1
            else:
                cnt["U3_switches_A"] += 1; lam = len(U.play_to(S[st]["nx"], v, cw))
                if s > LB + lam - 3: cnt["U3_ii_packet_FAIL"] += 1; cnt["U3_ii_packet_FAIL_LB%d" % LB] += 1
                if s > Tc + lam - 2: cnt["U3_ii_corrected_FAIL"] += 1

if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for _ in range(N):
            g = U.rand_c1o(rng, lo, hi)
            if g is not None: run(g, cnt)
    else:
        for p in a:
            c = Counter(); run(U.load(p), c, p); cnt.update(c)
            if any("FAIL" in k for k in c): print(p, {k: v for k, v in c.items() if "FAIL" in k})
    print(dict(sorted(cnt.items())))
