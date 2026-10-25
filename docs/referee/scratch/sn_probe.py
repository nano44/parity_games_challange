#!/usr/bin/env python3
"""REFEREE probe for packet P-N5-SN (docs/new/P-N5-SN-box33.md, pin 2c70ef6, sha1 340d4f29...). Own trace (u1_probe.trace = the n5.py
loop, asserted equal to n5.run); every game asserted in C^1O (exactly one Odd vertex with out-degree > 1). Written from the packet's
definitions, independent of experiments/new/box33/.
PHASE (packet §0) = (lambda_Xi, tau) constant; R_k contains o; F_k = V \\ R_k. Scope runs and ABS-L use P-N5-CLS's key (lambda_Xi, lambda_U, tau).
Checks:
 OR      at every eps-transition (O_k > E_k): (a) x0 in R_{k+1} and x0's H_{k+1}-path to c visits o; (b) H1 => x0 in F_k; (c) lev(theta) = O_k, rises
 TCS     TC-SPLIT at every theta change
 RSTICK  S4a: v in R_s with W-cycle node != lambda(v) stays in R
 PREFIX  runs of consecutive non-fallback phase transitions: c_w = c_theta states are a prefix; no R-loss after it; crossings after <= n-1;
         per phase: crossings <= (f+1)(n-1) + f + X_SN
 H3H2    every state: H1 and H3 => H2
 LEAVE   S4a, H1 at s, q in R_s \\ {o} leaves: (h) at s; a relevant change on q's H_{s+1}-path before lambda(q), of level >= r_s
 ABSC    per run: #H1-eps <= (d_o - 1) + REL_run (REL_run = exit-leave events at the run's transitions); also the 'd_o + REL' form, the
         H1-eps transitions at fallbacks, and the per-phase form (d_o - 1)(f + 1) + REL
 WK      wakes (P-N5-LP §3) with y not its own W-cycle node and W unchanged at a and z from k' to k'+1: W-cycle node of y has even priority
 ABSL    scope runs, consecutive fallbacks k0 < k, L = M_k0, r_j > L on [k0+1, k]: every theta change above L at j in [k0+1, k-1] is an
         absorption at level O_j with x0 in R_t for t in [j+1, k]; their number <= d_o - 1
Usage: sn_probe.py game.pg ... | sn_probe.py lib | sn_probe.py rand|randb N nmin nmax seed"""
import sys, os, random, glob
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U
from fb_probe import lev, coarse, BOT, INF

EX = []


def states(g):
    n = g.n; o = U.assert_c1o(g)
    E, Ed, out, it, fb = U.trace(g); st = []
    for (s, t, f, Is, s4a) in out:
        Xi, sb = E.evaluate(s); Ux, _ = Ed.evaluate(t); W = U.wval(g, E, s, t)
        nx = U.nxt_of(g, s, t); H = [s[v] if g.owner[v] == 0 else sb[v] for v in range(n)]
        R = frozenset(v for v in range(n) if U.reaches(nx, v, o))  # contains o
        H1 = not U.returns(H, o); H2 = not U.returns(nx, o); H3 = Xi[o][0] == W[o][0]
        gl = [lev(Xi[s[y]], Xi[z]) for y, z in Is]
        st.append(dict(s=s, t=t, fb=bool(f), Is=Is, Xi=Xi, sb=sb, W=W, R=R, H=H, H1=H1, H2=H2, H3=H3, h=H1 and H2 and H3,
                       r=lev(Xi[o], W[o]), M=max(gl, default=BOT), lam=tuple(x[0] for x in Xi),
                       key=(tuple(x[0] for x in Xi), t), fkey=(tuple(x[0] for x in Xi), tuple(x[0] for x in Ux), t)))
    return E, o, st


def changes(g, a, b, lam):
    ch = []
    for v in range(g.n):
        if lam[v] == v: continue
        if g.owner[v] == 0 and a["s"][v] != b["s"][v]: ch.append((v, lev(a["Xi"][a["s"][v]], a["Xi"][b["s"][v]])))
        if g.owner[v] == 1 and a["sb"][v] != b["sb"][v]: ch.append((v, lev(a["Xi"][a["sb"][v]], a["Xi"][b["sb"][v]])))
    return ch


def run(g, cnt, name=""):
    n = g.n; E, o, st = states(g); key = E.key; T = len(st) - 1; exits = sorted(set(g.succ[o])); do = len(exits)
    for a in st:
        if a["H1"] and a["H3"] and not a["H2"]: cnt["H3H2_FAIL"] += 1
        cnt["H3H2_chk"] += a["H1"] and a["H3"]
    inph = [st[k]["key"] == st[k + 1]["key"] for k in range(T)]
    rows = {}
    for k in range(T):
        if not inph[k]: continue
        a, b = st[k], st[k + 1]; lam = a["lam"]; c = lam[o]; ch = changes(g, a, b, lam); lv = dict(ch)
        Ek = max([l for v, l in ch if g.owner[v] == 0], default=BOT); Ok = lv.get(o, BOT) if c != o else BOT
        rows[k] = dict(E=Ek, O=Ok, L=max(Ek, Ok), ch=ch, X=a["R"] != b["R"], fb=a["fb"])
        cnt["tr"] += 1
        th0, th1 = a["Xi"][o], b["Xi"][o]
        # fixes §2b: H1-DROP (H1 at k, not H1 at k+1 => P(theta_k) = {}), H1-KEEP (H1 eps with O_k >= 0 keeps H1)
        if a["H1"] and not b["H1"]:
            cnt["H1DROP_chk"] += 1
            if th0[1] != 0: cnt["H1DROP_FAIL"] += 1; EX.append((name, "H1DROP", k))
        if Ok > Ek and a["H1"]:
            cnt["H1KEEP_chk"] += Ok >= 0; cnt["eps_H1_Om1"] += Ok == -1
            if Ok >= 0 and not b["H1"]: cnt["H1KEEP_FAIL"] += 1; EX.append((name, "H1KEEP", k))
        # OR
        if Ok > Ek:
            x0, x1 = a["sb"][o], b["sb"][o]; cnt["OR_chk"] += 1; cnt["OR_chk_" + ("H1" if a["H1"] else "nH1")] += 1
            p = U.play_to(b["H"], x0, c)
            if p is None or o not in p or x0 not in b["R"]: cnt["ORa_FAIL"] += 1
            if a["H1"] and x0 in a["R"]: cnt["ORb_FAIL"] += 1
            if lev(th0, th1) != Ok or not key(th1) > key(th0): cnt["ORc_FAIL"] += 1
            if a["fb"]: cnt["eps_at_fallback"] += 1; cnt["eps_at_fallback_H1"] += a["H1"]
            if a["H1"] and not b["H1"]: cnt["eps_H1_to_nH1"] += 1; EX.append((name, "epsH1->nH1", k))
        # TC-SPLIT
        if th0 != th1:
            cnt["TCS_chk"] += 1; l = lev(th0, th1)
            if not (l <= Ek or (Ok > Ek and l == Ok)): cnt["TCS_FAIL"] += 1
        # R-STICK and LEAVE (S4a = in-phase non-fallback)
        if not a["fb"]:
            for v in a["R"]:
                if v != o and a["W"][v][0] != lam[v]:
                    cnt["RSTICK_chk"] += 1
                    if v not in b["R"]: cnt["RSTICK_FAIL"] += 1
            if a["H1"]:
                for q in a["R"] - b["R"]:
                    cnt["LEAVE_chk"] += 1
                    if not a["h"]: cnt["LEAVE_h_FAIL"] += 1; continue
                    p = U.play_to(b["H"], q, lam[q]) or []
                    ls = [lv[x] for x in p if x in lv]
                    if not ls: cnt["LEAVE_nochange_FAIL"] += 1
                    elif max(ls) < a["r"]: cnt["LEAVE_FAIL"] += 1
    # runs of consecutive non-fallback phase transitions, per phase
    k = 0
    while k < T:
        if not inph[k]: k += 1; continue
        j = k
        while j + 1 < T and inph[j + 1]: j += 1
        phase(g, E, st, rows, range(k, j + 1), cnt, o, exits, name); k = j + 1
    scope(g, E, st, cnt, o, do, name)


def phase(g, E, st, rows, P, cnt, o, exits, name):
    n = g.n; do = len(exits); cth = st[P.start]["lam"][o]
    f = sum(st[k]["fb"] for k in P); X = sum(rows[k]["X"] for k in P); XSN = 0
    eps_H1_total = 0; rel_total = 0
    runs, cur = [], []
    for k in P:
        if st[k]["fb"]:
            if cur: runs.append(cur)
            cur = []
            if rows[k]["O"] > rows[k]["E"] and st[k]["H1"]: eps_H1_total += 1
        else: cur.append(k)
    if cur: runs.append(cur)
    for Rn in runs:
        eq = [st[k]["W"][o][0] == cth for k in Rn] + [st[Rn[-1] + 1]["W"][o][0] == cth]
        if any(eq[i + 1] and not eq[i] for i in range(len(eq) - 1)): cnt["PREFIX_FAIL"] += 1
        after = [k for k in Rn if st[k]["W"][o][0] != cth]
        for k in after:
            if not st[k]["R"] <= st[k + 1]["R"]: cnt["PREFIX_loss_FAIL"] += 1
        if sum(rows[k]["X"] for k in after) > n - 1: cnt["PREFIX_count_FAIL"] += 1
        XSN += sum(rows[k]["X"] for k in Rn if st[k]["W"][o][0] == cth)
        cnt["PREFIX_runs"] += 1; cnt["PREFIX_X_after"] += sum(rows[k]["X"] for k in after)
        cnt["PREFIX_X_in"] += sum(rows[k]["X"] for k in Rn if st[k]["W"][o][0] == cth)
        # ABS-COUNT
        epsH1 = sum(1 for k in Rn if rows[k]["O"] > rows[k]["E"] and st[k]["H1"])
        rel = sum(len([x for x in exits if x in st[k]["R"] and x not in st[k + 1]["R"]]) for k in Rn)
        eps_H1_total += epsH1; rel_total += rel
        cnt["ABSC_runs"] += 1
        hk = [k for k in Rn if rows[k]["O"] > rows[k]["E"] and st[k]["H1"]]
        if hk and rows[hk[-1]]["O"] >= 0:
            cnt["ABSCp_chk"] += 1
            if epsH1 > (do - 1) + rel: cnt["ABSCp_FAIL"] += 1
        if epsH1 > (do - 1) + rel:
            cnt["ABSC_FAIL"] += 1; EX.append((name, "ABSC", Rn[0], Rn[-1], "epsH1", epsH1, "d_o", do, "REL", rel))
        if epsH1 > do + rel: cnt["ABSC_dplus_FAIL"] += 1
        cnt["max_ABSC_excess"] = max(cnt["max_ABSC_excess"], epsH1 - rel - (do - 1))
    if X > (f + 1) * (n - 1) + f + XSN: cnt["PREFIX_phase_FAIL"] += 1
    if eps_H1_total > (do - 1) * (f + 1) + rel_total: cnt["ABSC_phase_FAIL"] += 1; EX.append((name, "ABSCphase", P.start, eps_H1_total, do, f, rel_total))
    # WK: wakes as in P-N5-LP §3
    rel = [k for k in P if rows[k]["L"] != BOT]
    for x in range(1, len(rel)):
        k, k2 = rel[x - 1], rel[x]
        if any(st[j]["fb"] or rows[j]["X"] for j in range(k, k2 + 1)): continue
        a, b = st[k2], st[k2 + 1]
        for y, l in rows[k2]["ch"]:
            if g.owner[y] != 0 or l <= rows[k]["L"]: continue
            cnt["wakes"] += 1; A, Z = a["s"][y], b["s"][y]
            cnt["wakes_mode_" + ("even" if g.prio[a["W"][y][0]] % 2 == 0 else "odd")] += 1
            if a["W"][y][0] == y: continue
            if a["W"][A] == b["W"][A] and a["W"][Z] == b["W"][Z]:
                cnt["WK_chk"] += 1
                if g.prio[a["W"][y][0]] % 2 != 0: cnt["WK_FAIL"] += 1; EX.append((name, "WK", k2, y, A, Z))


def scope(g, E, st, cnt, o, do, name):
    T = len(st) - 1
    def ins(j): return st[j]["fkey"] == st[j + 1]["fkey"] and st[j]["h"] and st[j + 1]["H2"] and st[j + 1]["W"][o] == st[j]["W"][o]
    k = 0
    while k < T:
        if not ins(k): k += 1; continue
        j = k
        while j + 1 < T and ins(j + 1): j += 1
        S = list(range(k, j + 1)); k = j + 1
        fbs = [x for x in S if st[x]["fb"]]
        for i in range(1, len(fbs)):
            k0, k1 = fbs[i - 1], fbs[i]; L = st[k0]["M"]
            if not all(st[x]["r"] > L for x in range(k0 + 1, k1 + 1)): continue
            cnt["ABSL_windows"] += 1; absorbed = []
            for x in range(k0 + 1, k1):
                a, b = st[x], st[x + 1]
                if a["Xi"][o] != b["Xi"][o]: cnt["ABSL_theta_changes"] += 1
                if lev(a["Xi"][o], b["Xi"][o]) <= L: continue
                cnt["ABSL_chk"] += 1; x0, x1 = a["sb"][o], b["sb"][o]
                ok = x0 != x1 and x0 not in a["R"] and x0 in b["R"] and lev(a["Xi"][x0], a["Xi"][x1]) == lev(a["Xi"][o], b["Xi"][o]) or False
                ok = ok and all(x0 in st[t]["R"] for t in range(x + 1, k1 + 1))
                if not ok: cnt["ABSL_FAIL"] += 1; EX.append((name, "ABSL", x, k0, k1))
                absorbed.append(x0)
            if len(absorbed) > do - 1: cnt["ABSL_count_FAIL"] += 1


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
