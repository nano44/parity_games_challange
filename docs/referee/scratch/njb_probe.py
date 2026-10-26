#!/usr/bin/env python3
"""REFEREE probe for packet P-N5-NJB (docs/si/P-N5-NJB-box9.md, pin a7d85b3, sha1 f43a8823...). Own trace (u1_probe.trace = the n5.py
loop, asserted equal to n5.run); every game asserted in C^1O (exactly one Odd vertex with out-degree > 1). Written from the packet's
definitions, independent of experiments/si/coarse/. R contains o here (P-N5-FBW §0: R-bar = {o} + ...; F = V \\ R-bar); scope runs with
key (lambda_Xi, lambda_U, tau) as in R29 / my fbw_probe.
Checks:
 RDROP   first COARSE_M change j of a dirty interval of a level-M block (M >= 0): r_j > M
 PLC     every block: D_M <= (d_o - 1) + REL_M and N <= n_E (d_o + REL_M); every dirty first change lies in P (r > M initial part)
 MS      intervals (f_i, f_i+1) with r > M on [f_i + 1, f_i+1]: (a) COARSE_M(theta_t) = min_{free exits} COARSE_M(o (+) Xi_t x), attained at
         sigmabar_t(o); (b) members leaving Mn enter R, members keep their COARSE_M value; (c) COARSE_M(theta) changes <=> Mn_{t+1} empty;
         (d) at block fallbacks f_i (i < N): Mn_{f_i} <= Mn_{f_i + 1}. Also: members entering R at a step together / other than sigmabar(o)
 NORF    in-scope fallback k0, L = M_k0, t* up to the next fallback of S with r > L on [k0+1, t*], S4a step j in (k0, t*) with a
         COARSE_L(theta) change: no gate (y, z) at t in [j+1, t*] with y in R_j and R_t, z in F_t
 ENTP    pattern behind ENT-SHAPE (5) [ENTP_strict: z rises at level exactly L at k0 -> k0+1, y unswitched with the same COARSE_L(b y)]: at an in-scope fallback k0 of level L >= 0 with (h) at k0+1, an Even edge (y, z) with z in
         R_k0 and F_k0+1 that is a level-L gate at k0+1 but not a gate of level L at k0 (z's rank-L bit turned good AT the fallback)
Usage: njb_probe.py game.pg ... | njb_probe.py lib | njb_probe.py rand N nmin nmax seed"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U, l2_probe as L2
from fb_probe import lev, coarse, BOT, INF

EX = []


def states(g):
    n = g.n; o = U.assert_c1o(g); E, Ed, out, it, fb = U.trace(g); st = []
    for (s, t, f, Is, s4a) in out:
        Xi, sb = E.evaluate(s); W = U.wval(g, E, s, t); Ux, _ = Ed.evaluate(t); nx = U.nxt_of(g, s, t)
        H = [s[v] if g.owner[v] == 0 else sb[v] for v in range(n)]
        R = frozenset(v for v in range(n) if U.reaches(nx, v, o)); H1 = not U.returns(H, o); H2 = not U.returns(nx, o)
        gl = [(y, z, lev(Xi[s[y]], Xi[z])) for y, z in Is]
        st.append(dict(s=s, t=t, fb=bool(f), Is=set(Is), gl=gl, M=max([l for _, _, l in gl], default=BOT), Xi=Xi, sb=sb, W=W, R=R,
                       H2=H2, h=H1 and H2 and Xi[o][0] == W[o][0], r=lev(Xi[o], W[o]), lam=tuple(x[0] for x in Xi),
                       fkey=(tuple(x[0] for x in Xi), tuple(x[0] for x in Ux), t)))
    return E, o, st, it, fb


def ckey(E, x, l):
    c = coarse(x, l)
    return E.key((c[0], c[1], x[2] if l <= BOT else 0))


def run(g, cnt, name=""):
    E, o, st, it, fb = states(g); T = len(st) - 1
    def ins(j): return st[j]["fkey"] == st[j + 1]["fkey"] and st[j]["h"] and st[j + 1]["H2"] and st[j + 1]["W"][o] == st[j]["W"][o]
    k = 0
    while k < T:
        if not ins(k): k += 1; continue
        j = k
        while j + 1 < T and ins(j + 1): j += 1
        scope(g, E, st, list(range(k, j + 1)), cnt, o, name); k = j + 1
    return it, fb


def mn(g, E, a, o, M):
    exits = sorted(set(g.succ[o])); th = coarse(a["Xi"][o], M)
    free = [x for x in exits if x not in a["R"]]
    vals = {x: coarse(E.extend(o, a["Xi"][x]), M) for x in free}
    return free, vals, {x for x in free if vals[x] == th}


def scope(g, E, st, S, cnt, o, name):
    n = g.n; nE = sum(1 for v in range(n) if g.owner[v] == 0); exits = sorted(set(g.succ[o])); do = len(exits)
    cnt["scope_runs"] += 1; fbs = [x for x in S if st[x]["fb"]]; end = S[-1] + 1
    # NORF: every in-scope fallback k0
    for i, k0 in enumerate(fbs):
        Lv = st[k0]["M"]; nxt = fbs[i + 1] if i + 1 < len(fbs) else end
        ts = k0 + 1
        while ts + 1 <= nxt and st[ts]["r"] > Lv: ts += 1
        tstar = ts if st[ts]["r"] > Lv else ts - 1  # last state with r > L, <= next fallback
        if tstar < k0 + 1: continue
        for j in range(k0 + 1, tstar):
            if st[j]["fb"] or coarse(st[j]["Xi"][o], Lv) == coarse(st[j + 1]["Xi"][o], Lv): continue
            cnt["NORF_j"] += 1
            for t in range(j + 1, tstar + 1):
                for y, z, l in st[t]["gl"]:
                    cnt["NORF_chk"] += 1
                    if y in st[j]["R"] and y in st[t]["R"] and y != o and z not in st[t]["R"]: cnt["NORF_FAIL"] += 1; EX.append((name, "NORF", k0, j, t, y, z))
            if tstar == nxt and nxt < end and st[nxt]["M"] >= 0:  # Corollary: non-flat switched edges at k are R -> F with an entrant tail
                a, b = st[nxt], st[nxt + 1]; cnt["NORF_cor_chk"] += 1
                for y, z, l in a["gl"]:
                    if l >= 0 and b["s"][y] == z and y in a["R"] and z not in a["R"] and y in st[j]["R"]: cnt["NORF_cor_FAIL"] += 1
    # ENT-SHAPE (5) pattern at every in-scope fallback of level >= 0
    for k0 in fbs:
        Lv = st[k0]["M"]; a, b = st[k0], st[k0 + 1]
        if Lv < 0 or not b["h"]: continue
        for y in range(n):
            if g.owner[y] != 0: continue
            for z in set(g.succ[y]):
                if not (z in a["R"] and z != o and z not in b["R"]): continue
                l1 = lev(b["Xi"][b["s"][y]], b["Xi"][z]); g1 = E.key(b["Xi"][z]) > E.key(b["Xi"][b["s"][y]])
                l0 = lev(a["Xi"][a["s"][y]], a["Xi"][z]); g0 = E.key(a["Xi"][z]) > E.key(a["Xi"][a["s"][y]])
                if g1 and l1 == Lv and not (g0 and l0 == Lv):
                    cnt["ENTP_pattern"] += 1
                    # strict: z itself rises at level exactly L at k0 -> k0+1 (bad -> good), y keeps sigma and COARSE_L(b y)
                    if (lev(a["Xi"][z], b["Xi"][z]) == Lv and E.key(b["Xi"][z]) > E.key(a["Xi"][z]) and a["s"][y] == b["s"][y]
                            and coarse(a["Xi"][a["s"][y]], Lv) == coarse(b["Xi"][b["s"][y]], Lv)):
                        cnt["ENTP_strict"] += 1; EX.append((name, "ENTP_strict", k0, y, z, Lv))
    # blocks
    i = 0
    while i < len(fbs):
        M = st[fbs[i]]["M"]; j = i
        while j + 1 < len(fbs) and st[fbs[j + 1]]["M"] == M: j += 1
        B = fbs[i:j + 1]; i = j + 1
        if M < 0: continue
        cnt["blocks"] += 1; f1, fN = B[0], B[-1]
        chg = {t: any(coarse(st[t]["Xi"][v], M) != coarse(st[t + 1]["Xi"][v], M) for v in range(n)) for t in range(f1, fN)}
        P_end = f1
        while P_end + 1 <= fN and st[P_end + 1]["r"] > M: P_end += 1
        if st[f1]["r"] <= M: P_end = f1 - 1
        cnt["blocks_rdrop"] += P_end < fN
        D = 0
        for a_, b_ in zip(B, B[1:]):
            ts = [t for t in range(a_ + 1, b_) if chg[t]]
            if ts:
                D += 1; jj = ts[0]; cnt["RDROP_chk"] += 1
                if not st[jj]["r"] > M: cnt["RDROP_FAIL"] += 1; EX.append((name, "RDROP", jj, M))
                if jj > P_end: cnt["PLC_notinP_FAIL"] += 1
            # MINSET on intervals with r > M on [a_+1, b_]
            if all(st[t]["r"] > M for t in range(a_ + 1, b_ + 1)):
                cnt["MS_intervals"] += 1
                for t in range(a_ + 1, b_ + 1):
                    A = st[t]; free, vals, Mn = mn(g, E, A, o, M); th = coarse(A["Xi"][o], M)
                    if A["lam"][o] == o: cnt["MS_lamo"] += 1; continue
                    m = min((ckey(E, E.extend(o, A["Xi"][x]), M) for x in free), default=None)
                    if m != ckey(E, A["Xi"][o], M) or A["sb"][o] not in Mn: cnt["MSa_FAIL"] += 1; EX.append((name, "MSa", t))
                    cnt["MS_states"] += 1; cnt["MS_sum_Mn"] += len(Mn); cnt["MS_Mn1"] += len(Mn) == 1
                    if t < b_:
                        Bt = st[t + 1]; free1, vals1, Mn1 = mn(g, E, Bt, o, M)
                        for x in Mn - Mn1:
                            if x not in Bt["R"]: cnt["MSb_FAIL"] += 1; EX.append((name, "MSb", t, x))
                        for x in Mn & Mn1:
                            if vals[x] != vals1[x]: cnt["MSb_val_FAIL"] += 1
                        ent = [x for x in Mn if x in Bt["R"]]
                        cnt["MS_member_entries"] += len(ent)
                        if len(ent) >= 2: cnt["MS_multi_entry"] += 1
                        if any(x != A["sb"][o] for x in ent): cnt["MS_entry_not_sbar"] += 1
                        chth = coarse(Bt["Xi"][o], M) != th
                        if chth != (len(Mn1) == 0): cnt["MSc_FAIL"] += 1; EX.append((name, "MSc", t))
                        if chth: cnt["MS_emptied"] += 1
        for f in B[:-1]:  # (d)
            if not st[f + 1]["h"]: continue
            _, _, m0 = mn(g, E, st[f], o, M); _, _, m1 = mn(g, E, st[f + 1], o, M); cnt["MSd_chk"] += 1
            if not m0 <= m1: cnt["MSd_FAIL"] += 1; EX.append((name, "MSd", f))
        rel = sum(len([e for e in exits if e in st[f]["R"] and e not in st[f + 1]["R"]]) for f in B[:-1])
        cnt["PLC_chk"] += 1
        if D > (do - 1) + rel or len(B) > nE * (do + rel): cnt["PLC_FAIL"] += 1; EX.append((name, "PLC", f1, D, do, rel, len(B)))
        cnt["max_D"] = max(cnt["max_D"], D); cnt["max_block"] = max(cnt["max_block"], len(B))


def merge(cnt, c):
    for k, v in c.items(): cnt[k] = max(cnt[k], v) if k.startswith("max") else cnt[k] + v


if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for _ in range(N):
            g = U.rand_c1o(rng, lo, hi)
            if g is not None: cnt["runs"] += 1; c = Counter(); run(g, c); merge(cnt, c)
    else:
        files = L2.libfiles() if a[0] == "lib" else a
        for p in files:
            c = Counter(); run(U.load(p), c, os.path.basename(p)); cnt["files"] += 1; merge(cnt, c)
            if any("FAIL" in k for k in c): print(p, {k: v for k, v in c.items() if "FAIL" in k}, flush=True)
    print(dict(sorted(cnt.items())))
    for e in EX[:30]: print("  ", e)
