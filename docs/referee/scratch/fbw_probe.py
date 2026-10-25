#!/usr/bin/env python3
"""REFEREE probe for packet P-N5-FBW (docs/si/P-N5-FBW-box9.md, pin e69772b, sha1 88337bd6...). Own trace (u1_probe.trace = the n5.py
loop, asserted equal to n5.run). Written from the packet's definitions, independent of experiments/si/coarse/.
Every game:
 POPT   at every Even S4c fallback, every gate (y, z): the single switch sigma[y -> z] against tau_k gives V'(y) <= W_k(y) (P-OPT's consequence)
 FBW    (a) l <= max(delta, -1); (b) l = -1 > delta => y own W- and Xi-cycle node; Step 1 (l > delta => W-improving at level l)
C^1O only (exactly one Odd vertex with out-degree > 1, asserted), scope runs with key (lambda_Xi, lambda_U, tau):
 FBWS   in-scope fallbacks: M <= max(r, -1); EQ / u* = none: M = -1 and every gate tail an own cycle node
 CLS2   fallback levels non-increasing along each scope run (all kinds)
 FLAT   in-scope fallback, M >= 0, (h) at k and k+1: (i) F_k <= F_{k+1} and same routes on Rbar_{k+1}; (ii) COARSE_M theta; (iii) all v; (iv) M_{k+1} <= M
 PL     per block (level M >= 0): tails never repeat inside a constant-COARSE_M run (STRETCH, last fallback included); N <= n_E(1 + D_M);
        first COARSE_M change of a dirty interval: S4a, O > M >= E, lev(theta) = O, absorption; if r > M on [f1, fN]: D_M <= d_o - 1 + REL_M
Usage: fbw_probe.py game.pg ... | fbw_probe.py lib | fbw_probe.py rand N nmin nmax seed [general]"""
import sys, os, random, glob
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U
from fb_probe import lev, coarse, BOT, INF, rand_game

EX = []


def route(nx, v, o):
    p, seen = [], set()
    while v != o:
        if v in seen: return None
        seen.add(v); p.append(v); v = nx[v]
    return tuple(p)


def run(g, cnt, name="", c1o=True):
    n = g.n; o = U.assert_c1o(g) if c1o else None
    E, Ed, out, it, fb = U.trace(g); key = E.key; st = []
    for (s, t, f, Is, s4a) in out:
        Xi, sb = E.evaluate(s); W = U.wval(g, E, s, t); d = dict(s=s, t=t, fb=bool(f), Is=Is, Xi=Xi, sb=sb, W=W)
        gl = [(y, z, lev(Xi[s[y]], Xi[z])) for y, z in Is]; d["gl"] = gl; d["M"] = max([l for _, _, l in gl], default=BOT)
        if c1o:
            Ux, _ = Ed.evaluate(t); nx = U.nxt_of(g, s, t); H = [s[v] if g.owner[v] == 0 else sb[v] for v in range(n)]
            R = frozenset(v for v in range(n) if U.reaches(nx, v, o)); H1 = not U.returns(H, o); H2 = not U.returns(nx, o)
            d.update(R=R, nx=nx, H=H, H2=H2, h=H1 and H2 and Xi[o][0] == W[o][0], r=lev(Xi[o], W[o]), lam=tuple(x[0] for x in Xi),
                     fkey=(tuple(x[0] for x in Xi), tuple(x[0] for x in Ux), t))
        st.append(d)
    # P-OPT and FBW at every Even fallback
    for k, a in enumerate(st):
        if not a["fb"] or not a["Is"]: continue
        cnt["fb_even"] += 1
        for y, z, l in a["gl"]:
            cnt["gates"] += 1; u = a["s"][y]
            dl = max(lev(a["Xi"][u], a["W"][u]), lev(a["Xi"][z], a["W"][z]))
            s2 = list(a["s"]); s2[y] = z; V2 = U.wval(g, E, tuple(s2), a["t"])
            if key(V2[y]) > key(a["W"][y]): cnt["POPT_FAIL"] += 1; EX.append((name, "POPT", k, y, z))
            if l > max(dl, -1): cnt["FBWa_FAIL"] += 1; EX.append((name, "FBWa", k, y, z, l, dl))
            if l > dl:
                cnt["FBW_l_gt_delta"] += 1
                if not (key(a["W"][z]) > key(a["W"][u]) and lev(a["W"][u], a["W"][z]) == l): cnt["FBWstep1_FAIL"] += 1
                if l == -1 and not (a["W"][y][0] == y and a["Xi"][y][0] == y): cnt["FBWb_FAIL"] += 1
    if not c1o: return
    T = len(st) - 1
    def ins(j): return st[j]["fkey"] == st[j + 1]["fkey"] and st[j]["h"] and st[j + 1]["H2"] and st[j + 1]["W"][o] == st[j]["W"][o]
    k = 0
    while k < T:
        if not ins(k): k += 1; continue
        j = k
        while j + 1 < T and ins(j + 1): j += 1
        scope(g, E, st, list(range(k, j + 1)), cnt, o, name); k = j + 1


def changes(g, a, b, lam):
    ch = []
    for v in range(g.n):
        if lam[v] == v: continue
        if g.owner[v] == 0 and a["s"][v] != b["s"][v]: ch.append((v, lev(a["Xi"][a["s"][v]], a["Xi"][b["s"][v]])))
        if g.owner[v] == 1 and a["sb"][v] != b["sb"][v]: ch.append((v, lev(a["Xi"][a["sb"][v]], a["Xi"][b["sb"][v]])))
    return ch


def scope(g, E, st, S, cnt, o, name):
    n = g.n; key = E.key; nE = sum(1 for v in range(n) if g.owner[v] == 0); exits = sorted(set(g.succ[o])); do = len(exits)
    cnt["scope_runs"] += 1
    fbs = [x for x in S if st[x]["fb"]]
    prev = None
    for x in fbs:
        a = st[x]; kind = "THRu" if a["r"] >= 0 else ("THR0" if a["r"] == -1 else "EQ")
        cnt["scope_fb_" + kind] += 1
        if a["M"] > max(a["r"], -1): cnt["FBWS_FAIL"] += 1; EX.append((name, "FBWS", x, kind, a["M"], a["r"]))
        if kind != "THRu":
            if a["M"] != -1: cnt["FBWS_eq_FAIL"] += 1
            if any(a["Xi"][y][0] != y for y, z, l in a["gl"]): cnt["FBWS_eqtail_FAIL"] += 1
        if prev is not None and a["M"] > prev: cnt["CLS2_FAIL"] += 1; EX.append((name, "CLS2", x, prev, a["M"]))
        prev = a["M"]
        # FLAT-ALL
        b = st[x + 1]; M = a["M"]
        if M >= 0 and a["h"] and b["h"]:
            cnt["FLAT_chk"] += 1; Fa = set(range(n)) - a["R"]; Fb = set(range(n)) - b["R"]
            if not Fa <= Fb: cnt["FLATi_FAIL"] += 1
            if any(route(b["nx"], v, o) != route(a["nx"], v, o) for v in b["R"]): cnt["FLATi_route_FAIL"] += 1
            if coarse(a["Xi"][o], M) != coarse(b["Xi"][o], M): cnt["FLATii_FAIL"] += 1
            if any(coarse(a["Xi"][v], M) != coarse(b["Xi"][v], M) for v in range(n)): cnt["FLATiii_FAIL"] += 1
            if b["M"] > M: cnt["FLATiv_FAIL"] += 1
    # PL: blocks of equal level M >= 0 (consecutive among fallbacks by CLS2)
    i = 0
    while i < len(fbs):
        M = st[fbs[i]]["M"]; j = i
        while j + 1 < len(fbs) and st[fbs[j + 1]]["M"] == M: j += 1
        B = fbs[i:j + 1]; i = j + 1
        if M < 0: continue
        cnt["blocks"] += 1; cnt["block_fb"] += len(B)
        f1, fN = B[0], B[-1]
        chg = [any(coarse(st[t]["Xi"][v], M) != coarse(st[t + 1]["Xi"][v], M) for v in range(n)) for t in range(f1, fN)]
        D = 0
        for a_, b_ in zip(B, B[1:]):
            ts = [t for t in range(a_ + 1, b_) if chg[t - f1]]
            if any(chg[t - f1] for t in [a_]): cnt["PL_fbchange_FAIL"] += 1  # FLAT-ALL (iii) at a block fallback (not the last)
            if not ts: continue
            D += 1; t = ts[0]; A, Bt = st[t], st[t + 1]; lam = A["lam"]; ch = changes(g, A, Bt, lam); lv = dict(ch)
            Ek = max([l for v, l in ch if g.owner[v] == 0], default=BOT); Ok = lv.get(o, BOT) if lam[o] != o else BOT
            x0 = A["sb"][o]
            ok = (not A["fb"]) and Ok > M >= Ek and lev(A["Xi"][o], Bt["Xi"][o]) == Ok and x0 not in A["R"] and x0 in Bt["R"]
            cnt["PLb_chk"] += 1
            if not ok: cnt["PLb_FAIL"] += 1; EX.append((name, "PLb", t, M, Ok, Ek))
        # STRETCH (tails do not repeat inside a constant-COARSE_M run, last fallback included)
        runid = [0]
        for t in range(f1, fN): runid.append(runid[-1] + chg[t - f1])
        seen = set()
        for f in B:
            rid = runid[f - f1]
            for y in sorted({y for y, z, l in st[f]["gl"] if l == M}):  # level-M tails of this fallback (a tail may have several gates)
                if (rid, y) in seen: cnt["STRETCH_FAIL"] += 1; EX.append((name, "STRETCH", f, y))
                seen.add((rid, y))
        if len(B) > nE * (1 + D): cnt["PLa_FAIL"] += 1
        cnt["max_block"] = max(cnt["max_block"], len(B)); cnt["max_D"] = max(cnt["max_D"], D)
        if all(st[t]["r"] > M for t in range(f1, fN + 1)):
            rel = sum(len([e for e in exits if e in st[f]["R"] and e not in st[f + 1]["R"]]) for f in B[:-1])
            cnt["PLc_chk"] += 1
            if D > (do - 1) + rel: cnt["PLc_FAIL"] += 1
            if len(B) > nE * (do + rel): cnt["PLc_N_FAIL"] += 1


def merge(cnt, c):
    for k, v in c.items(): cnt[k] = max(cnt[k], v) if k.startswith("max") else cnt[k] + v


if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); gen = len(a) > 5; rng = random.Random(seed)
        for _ in range(N):
            g = rand_game(rng, lo, hi) if gen else U.rand_c1o(rng, lo, hi)
            if g is None: continue
            cnt["runs"] += 1; c = Counter(); run(g, c, c1o=not gen); merge(cnt, c)
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
