#!/usr/bin/env python3
"""REFEREE probe for packet P-N5-L2 (docs/new/P-N5-L2-box34.md, pin 04b3f48, sha1 cbea0739...). Own trace (u1_probe.trace = the n5.py
loop, asserted equal to n5.run); every game asserted in C^1O (exactly one Odd vertex with out-degree > 1). Written from the packet's
definitions, independent of experiments/new/box34/. PHASE = (lambda_Xi, tau) constant (packet §0); R excludes o, Rbar = R + {o}.
Checks:
 H3C     §1 at every H2 state c_w = lambda(tau(o)); per phase H3 at all H2 states or none; with an (h) state: (h) <=> H1 and H2
 H2S     §2 in-phase S4a step with H1 and not H2 at s: not H2 at s+1; corollary: fallback-free runs with H1 everywhere: H2 states a prefix
 GP      §3 H3 and not H1: (a) not H2, c in Rbar; (b) c-first: Xi = W; o-first: Xi = pi (+) theta, W = pi (+) w, pi disjoint from o's honest
         path to c, from o's W-path to c, and from c; (c) lev(Xi v, W v) <= r for every v; c = o => theta = w = (o, {}, 0)
 FACT0H3 FREEZE' Fact 0 (i) W-cycle node of v = lambda(v), (ii) honest cycle node u has W(u) = (u, {}, 0), at every H3 state
 FRZ     §4 windows of n consecutive H3 states with r <= l (every l): Step 1 on the window, Step 2 (COARSE_l W non-decreasing), and for t >= F
         with some t2 >= t having H2 or H3: COARSE_l(Xi_t) = COARSE_l(Xi_F); at H2-or-H3 t also COARSE_l(W_t) = COARSE_l(W_F) = COARSE_l(Xi_F).
         Counted separately: windows containing a not-H1 state (new), checks at H3-and-not-H2 states t (new)
 DATA    §8 DROP-LEN (not to sign): consecutive in-phase drops with theta unchanged between them
 RC      §5 not H1: Rbar = lambda^{-1}(c_theta); in-phase transitions between two not-H1 states are not crossings
 HI      §6 (a) {k : P(theta_k) = {}} is an interval of the phase; (b) not-H1 states and pre-drop states lie in it; (c) on it theta =
         (c_theta, {}, len), len monotone, <= n - 1 changes
 XR      §7 fallback-free runs Q, SN prefix P (states with c_w = c_theta; prefix property asserted): crossings with both ends in P inside
         not-H1 runs = 0; crossings in P <= 13 (d_o+1) n^3 (t_Q+1) + t_Q; REL_Q <= d_o (C_P + 1) with C_P the ACTUAL crossing count in P
Usage: l2_probe.py game.pg ... | l2_probe.py lib | l2_probe.py rand|randb N nmin nmax seed"""
import sys, os, random, glob
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U
from fb_probe import lev, coarse, BOT, INF

EX = []


def states(g):
    n = g.n; o = U.assert_c1o(g); E, Ed, out, it, fb = U.trace(g); st = []
    for (s, t, f, Is, s4a) in out:
        Xi, sb = E.evaluate(s); W = U.wval(g, E, s, t); nx = U.nxt_of(g, s, t)
        H = [s[v] if g.owner[v] == 0 else sb[v] for v in range(n)]
        R = frozenset(v for v in range(n) if v != o and U.reaches(nx, v, o)); Rb = R | {o}
        H1 = not U.returns(H, o); H2 = not U.returns(nx, o); H3 = Xi[o][0] == W[o][0]
        st.append(dict(s=s, t=t, fb=bool(f), Is=set(Is), Xi=Xi, sb=sb, W=W, R=R, Rb=Rb, nx=nx, H=H, H1=H1, H2=H2, H3=H3,
                       h=H1 and H2 and H3, r=lev(Xi[o], W[o]) if H3 else INF, key=(tuple(x[0] for x in Xi), t)))
    return E, o, st, it, fb


def ext(E, path, x):
    for u in reversed(path): x = E.extend(u, x)
    return x


def run(g, cnt, name=""):
    n = g.n; E, o, st, it, nfb = states(g); T = len(st) - 1; do = len(set(g.succ[o]))
    cnt["states"] += len(st)
    for k, a in enumerate(st):
        Xi, W = a["Xi"], a["W"]; cth = Xi[o][0]; cw = W[o][0]
        cnt["nH1_states"] += not a["H1"]; cnt["H3nH1_states"] += a["H3"] and not a["H1"]
        if a["H2"]:
            cnt["H3C_chk"] += 1
            if cw != Xi[a["t"][o]][0]: cnt["H3C_FAIL"] += 1; EX.append((name, "H3C", k))
        if a["H3"]:  # Fact 0 at H3 states
            cnt["FACT0H3_chk"] += 1
            if any(W[v][0] != Xi[v][0] for v in range(n)): cnt["FACT0H3i_FAIL"] += 1; EX.append((name, "FACT0i", k))
            if any(W[u] != (u, 0, 0) for u in range(n) if Xi[u][0] == u): cnt["FACT0H3ii_FAIL"] += 1; EX.append((name, "FACT0ii", k))
        if a["H3"] and not a["H1"]:
            c = cth; cnt["GP_chk"] += 1
            if a["H2"] or c not in a["Rb"]: cnt["GPa_FAIL"] += 1; EX.append((name, "GPa", k))
            hp = set(U.play_to(a["H"], a["H"][o], c) or []) if c != o else set()  # o's honest path o -> sb(o) ~> c, minus o
            wp = set(U.play_to(a["nx"], a["nx"][o], c) or []) if c != o else set()
            for v in a["Rb"]:
                pc = U.play_to(a["nx"], v, c) if c != o else None
                po = U.play_to(a["nx"], v, o)
                if c != o and pc is not None and (po is None or len(pc) < len(po)):
                    cnt["GP_cfirst"] += 1
                    if Xi[v] != W[v]: cnt["GPb_cfirst_FAIL"] += 1; EX.append((name, "GPc", k, v))
                else:
                    cnt["GP_ofirst"] += 1; pi = po
                    if (set(pi) - {o}) & (hp | wp) or c in pi: cnt["GPb_disj_FAIL"] += 1; EX.append((name, "GPdisj", k, v))
                    if Xi[v] != ext(E, pi, Xi[o]) or W[v] != ext(E, pi, W[o]): cnt["GPb_ofirst_FAIL"] += 1; EX.append((name, "GPo", k, v))
            if any(lev(Xi[v], W[v]) > a["r"] for v in range(n)): cnt["GPc_FAIL"] += 1; EX.append((name, "GPlev", k))
            if c == o:
                cnt["GP_c_eq_o"] += 1
                if Xi[o] != (o, 0, 0) or W[o] != (o, 0, 0): cnt["GP_ceqo_FAIL"] += 1
        if not a["H1"]:
            cnt["RC_chk"] += 1
            if a["Rb"] != frozenset(v for v in range(n) if Xi[v][0] == cth): cnt["RC_FAIL"] += 1; EX.append((name, "RC", k))
    inph = [st[k]["key"] == st[k + 1]["key"] for k in range(T)]
    for k in range(T):
        if not inph[k]: continue
        a, b = st[k], st[k + 1]
        if not a["H1"] and not b["H1"]:
            cnt["RC_tr"] += 1
            if a["R"] != b["R"]: cnt["RC_cross_FAIL"] += 1; EX.append((name, "RCx", k))
        if not a["fb"] and a["H1"] and not a["H2"]:
            cnt["H2S_chk"] += 1
            if b["H2"]: cnt["H2S_FAIL"] += 1; EX.append((name, "H2S", k))
            if a["t"][o] == o: cnt["H2S_selfloop"] += 1
        cnt["drops"] += a["H1"] and not b["H1"]; cnt["rises"] += (not a["H1"]) and b["H1"]
    k = 0
    while k < T:
        if not inph[k]: k += 1; continue
        j = k
        while j + 1 < T and inph[j + 1]: j += 1
        phase(g, E, st, k, j + 1, cnt, o, do, name); k = j + 1
    return it, nfb


def phase(g, E, st, p0, p1, cnt, o, do, name):
    n = g.n; key = E.key; Ps = list(range(p0, p1 + 1)); cnt["phases"] += 1
    # H3C per phase
    h3 = {st[t]["H3"] for t in Ps if st[t]["H2"]}
    if len(h3) > 1: cnt["H3C_phase_FAIL"] += 1; EX.append((name, "H3Cph", p0))
    if any(st[t]["h"] for t in Ps):
        if any(st[t]["h"] != (st[t]["H1"] and st[t]["H2"]) for t in Ps): cnt["H3C_h_FAIL"] += 1
    # H1-INT
    cth = st[p0]["Xi"][o][0]
    I0 = [t for t in Ps if st[t]["Xi"][o][1] == 0]
    if I0:
        cnt["HI_phases_nonempty"] += 1
        if I0 != list(range(I0[0], I0[-1] + 1)): cnt["HIa_FAIL"] += 1; EX.append((name, "HIa", p0, I0))
        need = [t for t in Ps if not st[t]["H1"]] + [t for t in Ps[:-1] if st[t]["H1"] and not st[t + 1]["H1"]]
        if any(t not in I0 for t in need): cnt["HIb_FAIL"] += 1; EX.append((name, "HIb", p0))
        L = [st[t]["Xi"][o][2] for t in I0]
        if any(st[t]["Xi"][o][0] != cth for t in I0): cnt["HIc_FAIL"] += 1
        d = [L[i + 1] - L[i] for i in range(len(L) - 1)]
        if any(x > 0 for x in d) and any(x < 0 for x in d): cnt["HIc_mono_FAIL"] += 1; EX.append((name, "HIcmono", p0))
        ch = sum(1 for x in d if x != 0)
        if ch > n - 1 or max(L) > n - 1: cnt["HIc_count_FAIL"] += 1
        cnt["max_HI_len_changes"] = max(cnt["max_HI_len_changes"], ch)
        if any(st[t]["Xi"][o] != st[t + 1]["Xi"][o] and st[t]["Xi"][o][1] == st[t + 1]["Xi"][o][1] == 0 for t in I0[:-1]):
            cnt["HI_len_change_tr"] += 1
    elif any(not st[t]["H1"] for t in Ps): cnt["HIb_FAIL"] += 1
    # §8 DROP-LEN (NOT TO SIGN; DATA only): consecutive in-phase drops with theta unchanged between them
    dr = [t for t in Ps[:-1] if st[t]["H1"] and not st[t + 1]["H1"]]
    cnt["phases_2drops"] += len(dr) >= 2
    for i in range(len(dr) - 1):
        if st[dr[i]]["Xi"][o] == st[dr[i + 1]]["Xi"][o]: cnt["DATA_droplen_viol"] += 1; EX.append((name, "DROPLEN", dr[i], dr[i + 1]))
    # FREEZE'
    lastG = max([t for t in Ps if st[t]["H2"] or st[t]["H3"]], default=None)
    for l in [BOT] + list(range(-1, n)):
        F = None; run_ = 0; start = None
        for t in Ps:
            ok = st[t]["H3"] and st[t]["r"] <= l
            if ok and run_ == 0: start = t
            run_ = run_ + 1 if ok else 0
            if ok:
                cnt["FRZ_step1_chk"] += 1
                if any(coarse(st[t]["Xi"][v], l) != coarse(st[t]["W"][v], l) for v in range(n)): cnt["FRZ_step1_FAIL"] += 1; EX.append((name, "S1", t, l))
            if run_ >= 2 and not coarse_le(E, st, t - 1, t, l): cnt["FRZ_step2_FAIL"] += 1; EX.append((name, "S2", t, l))
            if run_ == n and F is None: F = t; W0 = start
        if F is None or lastG is None or lastG < F: continue
        new = any(not st[t]["H1"] for t in range(W0, F + 1))
        cnt["FRZ_windows"] += 1; cnt["FRZ_windows_nH1"] += new
        for t in Ps:
            if t < F or t > lastG: continue
            cnt["FRZ_chk"] += 1
            if any(coarse(st[t]["Xi"][v], l) != coarse(st[F]["Xi"][v], l) for v in range(n)): cnt["FRZa_FAIL"] += 1; EX.append((name, "FRZa", F, t, l))
            if st[t]["H2"] or st[t]["H3"]:
                if not st[t]["H2"]: cnt["FRZb_chk_H3notH2"] += 1
                if any(coarse(st[t]["W"][v], l) != coarse(st[F]["Xi"][v], l) or coarse(st[F]["W"][v], l) != coarse(st[F]["Xi"][v], l)
                       for v in range(n)): cnt["FRZb_FAIL"] += 1; EX.append((name, "FRZb", F, t, l))
    xrun(g, E, st, p0, p1, cnt, o, do, name)


def coarse_le(E, st, a, b, l):
    for v in range(len(st[a]["W"])):
        x, y = st[a]["W"][v], st[b]["W"][v]
        if coarse(x, l) == coarse(y, l): continue
        if not E.key(x) < E.key(y): return False
    return True


def xrun(g, E, st, p0, p1, cnt, o, do, name):
    n = g.n; k = p0; exits = set(g.succ[o])
    while k < p1:
        if st[k]["fb"]: k += 1; continue
        j = k
        while j + 1 < p1 and not st[j + 1]["fb"]: j += 1
        Q = list(range(k, j + 2)); k = j + 1
        cth = st[Q[0]]["Xi"][o][0]
        eq = [st[t]["W"][o][0] == cth for t in Q]
        if any(eq[i + 1] and not eq[i] for i in range(len(eq) - 1)): cnt["XR_prefix_FAIL"] += 1; EX.append((name, "XRpre", Q[0]))
        P = [t for t in Q if eq[t - Q[0]]]
        P = P[:next((i for i in range(len(P)) if P[i] != Q[0] + i), len(P))]
        cnt["XR_runs"] += 1
        if not P: continue
        tQ = sum(st[t]["H1"] != st[t + 1]["H1"] for t in P[:-1])
        cross = [t for t in P[:-1] if st[t]["R"] != st[t + 1]["R"]]
        cnt["XR_runs_nH1"] += any(not st[t]["H1"] for t in P)
        for t in cross:
            if not st[t]["H1"] and not st[t + 1]["H1"]: cnt["XR_nH1cross_FAIL"] += 1; EX.append((name, "XRnH1", t))
        if len(cross) > 13 * (do + 1) * n ** 3 * (tQ + 1) + tQ: cnt["XR_a_FAIL"] += 1
        rel = sum(len([e for e in exits if e in st[t]["R"] and e not in st[t + 1]["R"]]) for t in Q[:-1])
        if rel > do * (len(cross) + 1): cnt["XR_b_FAIL"] += 1; EX.append((name, "XRb", Q[0], rel, len(cross)))
        cnt["max_tQ"] = max(cnt["max_tQ"], tQ); cnt["max_XR_cross"] = max(cnt["max_XR_cross"], len(cross))
        cnt["XR_toggle_cross"] += sum(1 for t in cross if st[t]["H1"] != st[t + 1]["H1"])
        cnt["max_REL"] = max(cnt["max_REL"], rel)


def merge(cnt, c):
    for k, v in c.items(): cnt[k] = max(cnt[k], v) if k.startswith("max") else cnt[k] + v


def libfiles():
    files = []
    for p in sorted(glob.glob("experiments/**/*.pg", recursive=True)):
        try: g = U.load(p)
        except Exception: continue
        if g.n <= 64 and sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) == 1: files.append(p)
    return files


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
        files = libfiles() if a[0] == "lib" else a
        for p in files:
            c = Counter(); it, fb = run(U.load(p), c, os.path.basename(p)); cnt["files"] += 1; merge(cnt, c)
            if len(files) < 5: print(p, "iterations", it, "fallbacks", fb, dict(sorted(c.items())), flush=True)
            elif any("FAIL" in k for k in c): print(p, {k: v for k, v in c.items() if "FAIL" in k}, flush=True)
    print(dict(sorted(cnt.items())))
    for e in EX[:30]: print("  ", e)
