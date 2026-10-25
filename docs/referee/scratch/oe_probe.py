#!/usr/bin/env python3
"""REFEREE probe for packet P-N5-OE (docs/new/P-N5-OE-box32.md, pin 361d18c, sha1 adeccd89...). Own trace (u1_probe.trace = the n5.py
loop, asserted equal to n5.run); phase = (lambda_Xi, tau) constant, transitions with both ends in it. Every game asserted in C^1O.
Checks per in-phase transition k -> k+1 (definitions from the packet and P-N5-LP §0-§1, written independently of experiments/new/box32/):
 ULOC   Lemma U-loc for every v with L_v := max level of the relevant changes on v's H_{k+1}-path before lambda(v)
 OE     no crossing => O_k <= E_k (split H1 / not H1, level -1); also ties (sigmabar(o) changes at level BOT) and 'in particular'
 CAP    sigmabar(o) is a full Xi-minimiser over succ(o) at every state with lambda(o) != o
 ST2    x1's H_{k+1}-path to c avoids o;  ST3 (H1) x0 in F_k;  ST4 (not H1) P(Xi_k x0) = P(Xi_{k+1} x1) = {}
Per phase: (i) eps <= X, (ii) J <= X, every non-tame transition a crossing, (iii) rho <= 2f + 2X + K and every rise classified
(fallback or crossing in [k, k'], or a wake at k'), (iv) f <= nE(2n-1)(X+1)+X, (v) T bound.
Usage: oe_probe.py game.pg ... | oe_probe.py lib | oe_probe.py rand|randb N nmin nmax seed
randb: u1_probe.rand_c1o plus, at every vertex v != o, an extra edge v -> o with probability 0.25 (biases toward o on cycles, not H1)."""
import sys, os, random, glob
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U
from fb_probe import lev, coarse, BOT, INF


def run(g, cnt):
    n = g.n; o = U.assert_c1o(g)
    E, Ed, out, it, fb = U.trace(g); st = []
    for (s, t, f, Is, s4a) in out:
        Xi, sb = E.evaluate(s)
        R = frozenset(v for v in range(n) if U.reaches(U.nxt_of(g, s, t), v, o))
        H = [s[v] if g.owner[v] == 0 else sb[v] for v in range(n)]
        gl = [lev(Xi[s[y]], Xi[z]) for y, z in Is]
        st.append(dict(s=s, t=t, fb=f, Is=Is, Xi=Xi, sb=sb, R=R, H=H, H1=not U.returns(H, o), M=max(gl) if gl else BOT,
                       lam=tuple(x[0] for x in Xi), ph=(tuple(x[0] for x in Xi), t)))
    i = 0
    while i < len(st):
        j = i
        while j + 1 < len(st) and st[j + 1]["ph"] == st[i]["ph"]: j += 1
        phase(g, E, st[i:j + 1], cnt, o); i = j + 1


def changes(g, a, b, lam):
    """relevant changes at a -> b: list of (vertex, level), levels measured at a"""
    ch = []
    for v in range(g.n):
        if lam[v] == v: continue
        if g.owner[v] == 0 and a["s"][v] != b["s"][v]: ch.append((v, lev(a["Xi"][a["s"][v]], a["Xi"][b["s"][v]])))
        if g.owner[v] == 1 and a["sb"][v] != b["sb"][v]: ch.append((v, lev(a["Xi"][a["sb"][v]], a["Xi"][b["sb"][v]])))
    return ch


def phase(g, E, P, cnt, o):
    n = g.n; T = len(P) - 1
    if T <= 0: return
    cnt["phases"] += 1; m = sum(len(set(s)) for s in g.succ); nE = sum(1 for v in range(n) if g.owner[v] == 0)
    lam = P[0]["lam"]; c = lam[o]; key = E.key
    for r in P:
        if c != o:
            cnt["CAP_states"] += 1
            if key(r["Xi"][r["sb"][o]]) != min(key(r["Xi"][x]) for x in g.succ[o]): cnt["CAP_FAIL"] += 1
        else:  # negative control: lambda(o) = o, CAP-1 makes no claim; SPEC's FIX-2 choice is often not a minimiser
            cnt["CTRL_own_states"] += 1
            if key(r["Xi"][r["sb"][o]]) != min(key(r["Xi"][x]) for x in g.succ[o]): cnt["CTRL_own_nonmin"] += 1
    rows = []
    for k in range(T):
        a, b = P[k], P[k + 1]; ch = changes(g, a, b, lam); lv = dict(ch)
        Ek = max([l for v, l in ch if g.owner[v] == 0], default=BOT)
        Ok = lv.get(o, BOT) if c != o else BOT
        Lk = max(Ek, Ok); cross = a["R"] != b["R"]; cnt["tr"] += 1
        # U-loc
        for v in range(n):
            cv = lam[v]; p = U.play_to(b["H"], v, cv)
            if p is None: cnt["ULOC_nopath_FAIL"] += 1; continue
            Lv = max([lv[x] for x in p if x in lv], default=BOT)
            if Lv < INF and coarse(a["Xi"][v], Lv) != coarse(b["Xi"][v], Lv): cnt["ULOC_FAIL"] += 1
            cnt["ULOC_checks"] += 1
        # OE
        if c != o and a["sb"][o] != b["sb"][o]:
            x0, x1 = a["sb"][o], b["sb"][o]
            tag = ("X" if cross else "nX") + ("_H1" if a["H1"] else "_nH1")
            cnt["so_change_" + tag] += 1
            if Ok == BOT: cnt["so_tie_" + tag] += 1
            if not cross and Ek == BOT: cnt["so_change_noEven_nX"] += 1
            if Ok > Ek:
                cnt["OkgtEk_" + tag] += 1
                if not cross: cnt["OE_FAIL"] += 1
            if not cross:
                if Ok == -1: cnt["OE_level-1_nX"] += 1
                p1 = U.play_to(b["H"], x1, c)
                if p1 is None or o in p1: cnt["ST2_FAIL"] += 1
                if a["H1"] and x0 not in a["R"] and x0 in b["R"]: cnt["ST3_FAIL"] += 1
                if a["H1"] and x0 in a["R"]: cnt["ST3_FAIL"] += 1
                if a["H1"] != b["H1"]: cnt["TC_FAIL"] += 1
                if not a["H1"] and (a["Xi"][x0][1] != 0 or b["Xi"][x1][1] != 0): cnt["ST4_FAIL"] += 1
        tame = all(coarse(a["Xi"][v], a["M"]) == coarse(b["Xi"][v], a["M"]) for v in range(n))
        rows.append(dict(E=Ek, O=Ok, L=Lk, X=cross, fb=bool(a["fb"]), tame=tame, ch=ch))
    X = sum(r["X"] for r in rows); f = sum(r["fb"] for r in rows)
    rel = [k for k in range(T) if rows[k]["L"] != BOT]
    eps = sum(1 for k in rel if rows[k]["O"] > rows[k]["E"])
    J = sum(1 for r in rows if not r["tame"])
    for r in rows:
        if not r["tame"]:
            cnt["nontame"] += 1
            if not r["X"]: cnt["nontame_noncross_FAIL"] += 1
    rho = K = 0
    for x in range(1, len(rel)):
        k, k2 = rel[x - 1], rel[x]
        quiet = not any(rows[j]["fb"] for j in range(k, k2 + 1)) and not any(rows[j]["X"] for j in range(k, k2 + 1))
        wake = quiet and any(g.owner[v] == 0 and l > rows[k]["L"] for v, l in rows[k2]["ch"])
        K += wake
        if rows[k2]["L"] > rows[k]["L"]:
            rho += 1
            if quiet and not wake: cnt["rise_unclassified_FAIL"] += 1
            cnt["rise_" + ("fb" if any(rows[j]["fb"] for j in range(k, k2 + 1)) else "X" if not quiet else "wake")] += 1
    if eps > X: cnt["OXi_FAIL"] += 1
    if J > X: cnt["OXii_FAIL"] += 1
    if rho > 2 * f + 2 * X + K: cnt["OXiii_FAIL"] += 1
    if f > nE * (2 * n - 1) * (X + 1) + X: cnt["OXiv_FAIL"] += 1
    if T > (m - n + 1) * ((n + 1) * (2 * f + 2 * X + K + 1) * n * (n - 1) + X + 1): cnt["OXv_FAIL"] += 1
    for nm, v in (("T", T), ("X", X), ("J", J), ("f", f), ("rho", rho), ("K", K), ("eps", eps)):
        cnt["max_" + nm] = max(cnt["max_" + nm], v)
    if J == X and X > 0: cnt["phases_J_eq_X"] += 1


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
                g = U.pg.Game(list(g.prio), list(g.owner), sc)
            cnt["runs"] += 1; run(g, cnt)
    else:
        files = a
        if a[0] == "lib":
            files = []
            for p in sorted(glob.glob("experiments/**/*.pg", recursive=True)):
                try: g = U.load(p)
                except Exception: continue
                if g.n <= 64 and sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) == 1: files.append(p)
        for p in files:
            c = Counter(); run(U.load(p), c); cnt["files"] += 1; merge(cnt, c)
            if any("FAIL" in k for k in c): print(p, {k: v for k, v in c.items() if "FAIL" in k}, flush=True)
    print(dict(sorted(cnt.items())))
