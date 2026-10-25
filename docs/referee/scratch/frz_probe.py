#!/usr/bin/env python3
"""REFEREE probe for packet P-N5-FRZ (docs/new/P-N5-FRZ-box34.md, pin 25fda0f, sha1 39df373c...). Own trace (u1_probe.trace = the n5.py
loop, asserted equal to n5.run); every game asserted in C^1O (exactly one Odd vertex with out-degree > 1). Written from the packet's
definitions, independent of experiments/new/box34/. PHASE = (lambda_Xi, tau) constant (packet §0); R excludes o, Rbar = R + {o}.
Checks:
 NLMF    (h) S4a step with r_j > MF_j: no vertex of R_j leaves Rbar; MF_{j+1} <= MF_j
 FACT0   (h) states: every W-cycle node = lambda(v); c_theta in F
 ARENA   S4a step from an (h) state: every W-improving edge (y, z) of G_tau outside the arena is F -> Rbar, not a gate, with lev(W sigma y, W z) <= r
 STEP12  window states (h, r <= l): COARSE_l(Xi) = COARSE_l(W); COARSE_l(W) non-decreasing along the window (fallbacks included)
 FREEZE  first n-state window at l (every l in {bot, -1, ..., n-1}): for every later phase state t with an H2 state at or after it,
         COARSE_l(Xi_t) = COARSE_l(Xi_F); at H2 states also COARSE_l(W_t) = COARSE_l(Xi_F)
 RATCH   (a) at H2 states t >= F: COARSE_l(theta) = COARSE_l(w), H3, r <= l; (b) l >= 0: COARSE_{l-1}(theta) over H1 states in T takes
         <= 2 d_o values, COARSE_{l-1}(w) over T changes <= 1 time
 BLOCK   l >= 0, I = maximal runs of consecutive states t >= F with (h) and the pair (COARSE_{l-1} theta, COARSE_{l-1} w) constant and
         different: a vertex that leaves R at an S4a step inside I never re-enters R inside I
 XRUN    fallback-free runs Q, SN prefix P with H1 at every state: no crossing with both ends in P after F(bot); per level l >= 0 the
         crossings with both ends in [F(l), F(l-1)) are <= 6 (d_o + 1) n; total <= 13 (d_o + 1) n^3; REL_Q <= 13 d_o (d_o + 1) n^3
 SUB     (w, r)-subruns with rho >= 0: COARSE_rho(Xi) = COARSE_rho(W), constant from k0 + n - 1 on; S4a leave then next re-entry inside
         the subrun: strict COARSE_rho increase
Usage: frz_probe.py game.pg ... | frz_probe.py lib | frz_probe.py rand N nmin nmax seed"""
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
        gl = [(y, z, lev(Xi[s[y]], Xi[z])) for y, z in Is]
        st.append(dict(s=s, t=t, fb=bool(f), Is=set(Is), Xi=Xi, W=W, R=R, Rb=Rb, nx=nx, H1=H1, H2=H2, h=H1 and H2 and H3,
                       r=lev(Xi[o], W[o]) if H3 else INF, MF=max([l for y, z, l in gl if z not in Rb], default=BOT),
                       key=(tuple(x[0] for x in Xi), t)))
    return E, o, st


def run(g, cnt, name=""):
    n = g.n; E, o, st = states(g); key = E.key; T = len(st) - 1; do = len(set(g.succ[o]))
    lam = lambda a: [x[0] for x in a["Xi"]]
    for a in st:
        if a["h"]:
            cnt["FACT0_chk"] += 1
            if any(a["W"][v][0] != a["Xi"][v][0] for v in range(n)) or a["Xi"][o][0] in a["Rb"]: cnt["FACT0_FAIL"] += 1
    inph = [st[k]["key"] == st[k + 1]["key"] for k in range(T)]
    for k in range(T):
        if not inph[k]: continue
        a, b = st[k], st[k + 1]
        if not a["fb"] and a["h"]:
            if a["r"] > a["MF"]:
                cnt["NLMF_chk"] += 1
                if not a["R"] <= b["Rb"] or b["MF"] > a["MF"]: cnt["NLMF_FAIL"] += 1; EX.append((name, "NLMF", k))
            for y in range(n):  # ARENA
                if g.owner[y] != 0: continue
                for z in set(g.succ[y]):
                    if z == a["s"][y] or not key(a["W"][z]) > key(a["W"][a["s"][y]]) or (y, z) in a["Is"]: continue
                    cnt["ARENA_withheld"] += 1
                    if not (y not in a["Rb"] and z in a["Rb"] and lev(a["W"][a["s"][y]], a["W"][z]) <= a["r"]):
                        cnt["ARENA_FAIL"] += 1; EX.append((name, "ARENA", k, y, z))
    # phases
    k = 0
    while k < T:
        if not inph[k]: k += 1; continue
        j = k
        while j + 1 < T and inph[j + 1]: j += 1
        phase(g, E, st, k, j + 1, cnt, o, do, name); k = j + 1


def phase(g, E, st, p0, p1, cnt, o, do, name):
    """states p0..p1 inclusive form one phase"""
    n = g.n; key = E.key; Ps = list(range(p0, p1 + 1))
    lastH2 = max([t for t in Ps if st[t]["H2"]], default=None)
    for l in [BOT] + list(range(-1, n)):
        win = [t for t in Ps if st[t]["h"] and st[t]["r"] <= l]
        for t in win:  # STEP 1
            cnt["STEP1_chk"] += 1
            if any(coarse(st[t]["Xi"][v], l) != coarse(st[t]["W"][v], l) for v in range(n)): cnt["STEP1_FAIL"] += 1
        F = None; run_ = 0
        for t in Ps:
            run_ = run_ + 1 if (st[t]["h"] and st[t]["r"] <= l) else 0
            if t > p0 and run_ >= 2 and coarse_le(E, st, t - 1, t, l) is False: cnt["STEP2_FAIL"] += 1
            if run_ == n and F is None: F = t
        if F is None or lastH2 is None or lastH2 < F: continue
        cnt["FREEZE_windows"] += 1
        if l >= 0:  # §C count (Lead 08:41Z / R2-N5-FRZ C.3 (i)): S4a leaves at (h) states t >= F of the phase
            for t in Ps:
                if t >= F and t < p1 and st[t]["h"] and not st[t]["fb"]:
                    cnt["LEAVE_h_afterF_tr"] += 1; cnt["LEAVE_h_afterF"] += len(st[t]["R"] - st[t + 1]["Rb"])
        T_ = [t for t in Ps if t >= F and st[t]["H2"]]
        for t in Ps:
            if t < F or t > lastH2: continue
            cnt["FREEZE_chk"] += 1
            if any(coarse(st[t]["Xi"][v], l) != coarse(st[F]["Xi"][v], l) for v in range(n)): cnt["FREEZEa_FAIL"] += 1; EX.append((name, "FREEZEa", F, t, l))
            if st[t]["H2"] and any(coarse(st[t]["W"][v], l) != coarse(st[F]["Xi"][v], l) for v in range(n)): cnt["FREEZEb_FAIL"] += 1
        for t in T_:  # RATCHET (a)
            if coarse(st[t]["Xi"][o], l) != coarse(st[t]["W"][o], l) or st[t]["r"] > l: cnt["RATCHa_FAIL"] += 1
            if st[t]["H1"] and not st[t]["h"]: cnt["RATCHa_h_FAIL"] += 1
        if l >= 0:  # RATCHET (b), BLOCK
            th = [coarse(st[t]["Xi"][o], l - 1) for t in T_ if st[t]["H1"]]
            if len(set(th)) > 2 * do: cnt["RATCHb_FAIL"] += 1
            ws = [coarse(st[t]["W"][o], l - 1) for t in T_]
            if sum(ws[i] != ws[i + 1] for i in range(len(ws) - 1)) > 1: cnt["RATCHb_w_FAIL"] += 1
            cnt["RATCHb_chk"] += 1
            pair = lambda t: (coarse(st[t]["Xi"][o], l - 1), coarse(st[t]["W"][o], l - 1))
            t = F
            while t <= p1:
                if not (st[t]["h"] and pair(t)[0] != pair(t)[1]): t += 1; continue
                u = t
                while u + 1 <= p1 and st[u + 1]["h"] and pair(u + 1) == pair(t): u += 1
                I = range(t, u + 1); cnt["BLOCK_runs"] += 1; left = set()
                for s in range(t, u):
                    if not st[s]["fb"]:
                        cnt["BLOCK_S4a_leaves"] += len(st[s]["R"] - st[s + 1]["Rb"])  # §C count (R2-N5-FRZ C.3 (i))
                        left |= st[s]["R"] - st[s + 1]["Rb"]
                    if left & st[s + 1]["R"]: cnt["BLOCK_FAIL"] += 1; EX.append((name, "BLOCK", s, l))
                t = u + 1
    xrun(g, E, st, p0, p1, cnt, o, do, name)
    sub(g, E, st, p0, p1, cnt, o, name)


def coarse_le(E, st, a, b, l):
    """COARSE_l(W_a) <= COARSE_l(W_b) pointwise? (coarse order: cycle-node reward, then top of the coarse symmetric difference)"""
    for v in range(len(st[a]["W"])):
        x, y = st[a]["W"][v], st[b]["W"][v]
        if coarse(x, l) == coarse(y, l): continue
        if not E.key(x) < E.key(y): return False
    return True


def xrun(g, E, st, p0, p1, cnt, o, do, name):
    n = g.n; k = p0
    while k < p1:
        if st[k]["fb"]: k += 1; continue
        j = k
        while j + 1 < p1 and not st[j + 1]["fb"]: j += 1
        Q = list(range(k, j + 2)); k = j + 1  # states of the fallback-free run
        cth = st[Q[0]]["Xi"][o][0]
        P = []
        for t in Q:
            if st[t]["W"][o][0] == cth: P.append(t)
            else: break
        if not P or not all(st[t]["H1"] for t in P): continue
        cnt["XRUN_runs"] += 1
        def Fl(l):
            r_ = 0
            for t in P:
                r_ = r_ + 1 if st[t]["r"] <= l else 0
                if r_ == n: return t
            return None
        cross = [t for t in P[:-1] if st[t]["R"] != st[t + 1]["R"]]
        Fb = Fl(BOT)
        if Fb is not None and any(t >= Fb for t in cross): cnt["XRUN_afterbot_FAIL"] += 1; EX.append((name, "XRUN_bot", Fb))
        if Fb is not None: cnt["XRUN_afterbot_tr"] += len([t for t in P[:-1] if t >= Fb])  # §C count (R2-N5-FRZ C.3 (ii))
        if Fl(-1) is not None: cnt["XRUN_seg_m1_runs"] += 1
        cnt["XRUN_leaves_from_last_P"] += len(st[P[-1]]["R"] - st[P[-1] + 1]["Rb"]) if P[-1] < Q[-1] else 0
        for l in range(0, n):
            a, b = Fl(l), Fl(l - 1)
            if a is None: continue
            seg = [t for t in cross if t >= a and (b is None or t + 1 < b)]
            if len(seg) > 6 * (do + 1) * n: cnt["XRUN_seg_FAIL"] += 1
        if len(cross) > 13 * (do + 1) * n ** 3: cnt["XRUN_FAIL"] += 1
        exits = set(g.succ[o]); rel = sum(len([e for e in exits if e in st[t]["R"] and e not in st[t + 1]["R"]]) for t in Q[:-1])
        if rel > 13 * do * (do + 1) * n ** 3: cnt["XRUN_REL_FAIL"] += 1
        cnt["max_XRUN_cross"] = max(cnt["max_XRUN_cross"], len(cross)); cnt["max_XRUN_REL"] = max(cnt["max_XRUN_REL"], rel)


def sub(g, E, st, p0, p1, cnt, o, name):
    n = g.n; t = p0
    while t <= p1:
        a = st[t]
        if not (a["h"] and a["r"] >= 0): t += 1; continue
        u = t
        while u + 1 <= p1 and st[u + 1]["h"] and st[u + 1]["W"][o] == a["W"][o] and st[u + 1]["r"] == a["r"]: u += 1
        S = list(range(t, u + 1)); rho = a["r"]; t = u + 1; cnt["SUB_runs"] += 1
        for x in S:
            if any(coarse(st[x]["Xi"][v], rho) != coarse(st[x]["W"][v], rho) for v in range(n)): cnt["SUBi_FAIL"] += 1
        if len(S) >= n:
            F = S[n - 1]
            for x in S[n - 1:]:
                if any(coarse(st[x]["Xi"][v], rho) != coarse(st[F]["Xi"][v], rho) for v in range(n)): cnt["SUBii_FAIL"] += 1
        for L in S[:-1]:
            if st[L]["fb"]: continue
            for v in st[L]["R"] - st[L + 1]["Rb"]:
                for E_ in range(L + 1, S[-1]):
                    if v in st[E_ + 1]["R"]:
                        cnt["SUBiii_chk"] += 1
                        x1, x0 = coarse(st[E_ + 1]["Xi"][v], rho), coarse(st[L]["Xi"][v], rho)
                        if not (x1 != x0 and E.key(st[E_ + 1]["Xi"][v]) > E.key(st[L]["Xi"][v])): cnt["SUBiii_FAIL"] += 1; EX.append((name, "SUBiii", L, E_, v))
                        break


def merge(cnt, c):
    for k, v in c.items(): cnt[k] = max(cnt[k], v) if k.startswith("max") else cnt[k] + v


if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for _ in range(N):
            g = U.rand_c1o(rng, lo, hi)
            if g is None: continue
            cnt["runs"] += 1; c = Counter(); run(g, c); merge(cnt, c)
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
    for e in EX[:30]: print("  ", e)
