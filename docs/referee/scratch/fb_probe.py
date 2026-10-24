#!/usr/bin/env python3
"""REFEREE probe for packet P-N5-FB (docs/si/P-N5-FB-box7.md, pin 348393b, sha1 9ece9994...). Own N5 trace (u1_probe.trace = the n5.py
loop, asserted equal to n5.run). Definitions from the packet §1: lev, COARSE_L, gate level, M_k, TAME; phase = (lambda_Xi, lambda_U, tau)
constant, transitions of a phase have BOTH ends in it (phase-exit transitions are counted separately).
Checks:
 ENG     Theta_{sigma_k sigmabar_k} = Xi_k (the play value of (sigma, sigmabar) equals the engine valuation)
 SBMIN   for every Odd v: Xi(sigmabar v) is a minimum of Xi over succ(v) (VJ00 p.14's definition of sigmabar); split by v = lambda(v)
 NC      (sigma_{k+1}, sigmabar_k)-graph: every cycle's top t has lambda_k(t) = t
 CSIa    NC and L = M_k < inf => COARSE_L(Xi_{k+1}) = COARSE_L(Xi_k); converse: not NC => COARSE_L(V) != COARSE_L(Xi_k) (V = Theta_{H'})
 TAMEb   lambda_{k+1} = lambda_k and every Odd u has lev(Xi_k(sb_k u), Xi_k(sb_{k+1} u)) <= M_k => tame
 MONO    tame => M_{k+1} <= M_k (every transition, not only in-phase)
 NOINF   lambda_{k+1} = lambda_k, y switches to z => lambda_k(z) = lambda_k(sigma_k y)
 FB      per phase: beta monotone in blocks, strict beta rise at every in-phase fallback, M < inf at in-phase fallbacks,
         per-block bound, #fallbacks <= nE(2n-1)(J+1) + J
 J1/OFF/CAP  (C^1O only) at non-tame in-phase transitions: J1; OFF at all in-phase transitions; CAP
Usage: fb_probe.py game.pg ... | fb_probe.py rand N nmin nmax seed [c1o]"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U, pg
from si import Engine
BOT, INF = -2, 10 ** 6

def lev(x, y):
    if x == y: return BOT
    if x[0] != y[0]: return INF
    d = x[1] ^ y[1]
    return d.bit_length() - 1 if d else -1

def coarse(x, L):
    if L >= INF: return 0
    if L <= BOT: return x
    return (x[0], x[1] & ~((1 << (L + 1)) - 1))

def play_value(E, nx, v):
    """VJ00 play value of v's play in the functional graph nx (si.py representation)"""
    seq, pos = [], {}
    x = v
    while x not in pos: pos[x] = len(seq); seq.append(x); x = nx[x]
    cyc = seq[pos[x]:]; c = max(cyc, key=lambda u: E.rank[u]); pre = seq[:seq.index(c)]
    mask = 0
    for u in pre:
        if E.rank[u] > E.rank[c]: mask |= E.bit[u]
    return (c, mask, len(pre))

def cycles(nx):
    seen, out = set(), []
    for v in range(len(nx)):
        path, x = [], v
        while x not in seen and x not in path: path.append(x); x = nx[x]
        if x in path: out.append(path[path.index(x):])
        seen.update(path)
    return out

def run(g, cnt, c1o):
    n = g.n; o = U.assert_c1o(g) if c1o else None
    E, Ed, out, it, fb = U.trace(g)
    st = []
    for (s, t, f, Is, s4a) in out:
        Xi, sb = E.evaluate(s); Ux, _ = Ed.evaluate(t)
        H = [s[v] if g.owner[v] == 0 else sb[v] for v in range(n)]
        gl = [lev(Xi[s[y]], Xi[z]) for y, z in Is]
        M = max(gl) if gl else BOT
        st.append(dict(s=s, t=t, fb=f, Is=Is, Xi=Xi, sb=sb, H=H, M=M, lam=tuple(x[0] for x in Xi),
                       ph=(tuple(x[0] for x in Xi), tuple(x[0] for x in Ux), t)))
        for v in range(n):
            if play_value(E, H, v) != Xi[v]: cnt["ENG_FAIL"] += 1
        for v in range(n):
            if g.owner[v] == 1:
                mn = min(E.key(Xi[u]) for u in g.succ[v]); ok = E.key(Xi[sb[v]]) == mn
                tag = "cyc" if Xi[v][0] == v else "noncyc"
                cnt["SBMIN_" + tag] += 1
                if not ok: cnt["SBMIN_notmin_" + tag + ("_o" if v == o else "")] += 1
    K = len(st) - 1
    tame = []
    for k in range(K):
        a, b = st[k], st[k + 1]; M = a["M"]
        tm = all(coarse(a["Xi"][v], M) == coarse(b["Xi"][v], M) for v in range(n)); tame.append(tm)
        Hp = [b["s"][v] if g.owner[v] == 0 else a["sb"][v] for v in range(n)]
        nc = all(a["lam"][max(C, key=lambda u: E.rank[u])] == max(C, key=lambda u: E.rank[u]) for C in cycles(Hp))
        if M < INF and M != BOT:
            if nc:
                cnt["CSIa_NC"] += 1
                if not tm: cnt["CSIa_FAIL"] += 1
            else:
                cnt["CSIa_notNC"] += 1
                V = [play_value(E, Hp, v) for v in range(n)]
                if all(coarse(V[v], M) == coarse(a["Xi"][v], M) for v in range(n)): cnt["CSIa_converse_FAIL"] += 1
        if not tm: cnt["nontame"] += 1; cnt["nontame_NC"] += nc
        same_lam = a["lam"] == b["lam"]
        if same_lam and all(lev(a["Xi"][a["sb"][u]], a["Xi"][b["sb"][u]]) <= M for u in range(n) if g.owner[u] == 1):
            cnt["TAMEb_cases"] += 1
            if not tm: cnt["TAMEb_FAIL"] += 1
        if tm:
            cnt["MONO_cases"] += 1
            if b["M"] > M: cnt["MONO_FAIL"] += 1
        if same_lam:
            for y in range(n):
                if g.owner[y] == 0 and a["s"][y] != b["s"][y]:
                    cnt["NOINF_cases"] += 1
                    if a["lam"][b["s"][y]] != a["lam"][a["s"][y]]: cnt["NOINF_FAIL"] += 1
    # phases
    nE = sum(1 for v in range(n) if g.owner[v] == 0)
    i = 0
    while i <= K:
        j = i
        while j < K and st[j + 1]["ph"] == st[i]["ph"]: j += 1
        if j < K and st[j]["fb"]: cnt["fb_at_phase_exit"] += 1
        phase(g, E, st[i:j + 1], tame[i:j], nE, cnt, o)
        i = j + 1

def phase(g, E, P, tame, nE, cnt, o):
    n = g.n; T = len(P) - 1
    if T <= 0: return
    cnt["phases"] += 1
    nf = sum(P[i]["fb"] for i in range(T)); J = sum(1 for x in tame if not x)
    cnt["FB_fallbacks"] += nf; cnt["FB_maxJ"] = max(cnt["FB_maxJ"], J)
    if nf > nE * (2 * n - 1) * (J + 1) + J: cnt["FB_FAIL"] += 1
    # blocks: maximal runs of tame transitions with M constant
    i = 0
    while i < T:
        if not tame[i]: i += 1; continue
        j = i
        while j < T and tame[j] and P[j]["M"] == P[i]["M"]: j += 1
        M = P[i]["M"]; bf = 0
        for k in range(i, j):
            a, b = P[k], P[k + 1]
            for y in range(n):
                if g.owner[y] != 0: continue
                ba, bb = coarse(a["Xi"][a["s"][y]], M - 1 if M > -1 else BOT), coarse(b["Xi"][b["s"][y]], M - 1 if M > -1 else BOT)
                if M < INF and M != BOT:
                    if coarse(a["Xi"][a["s"][y]], M) != coarse(b["Xi"][b["s"][y]], M): cnt["FB1_const_FAIL"] += 1
                    if cmp_coarse(E, ba, bb) > 0: cnt["FB1_mono_FAIL"] += 1
            if a["fb"]:
                bf += 1
                if M >= INF or M == BOT: cnt["FB_fallback_M_infbot_FAIL"] += 1; continue
                Ml = M - 1 if M > -1 else BOT
                if not any(cmp_coarse(E, coarse(a["Xi"][a["s"][y]], Ml), coarse(b["Xi"][b["s"][y]], Ml)) < 0
                           for y in range(n) if g.owner[y] == 0): cnt["FB2_FAIL"] += 1
        if bf:
            cnt["blocks_with_fb"] += 1; cnt["FB_max_block_fb"] = max(cnt["FB_max_block_fb"], bf)
            if bf > (nE if M >= 0 else nE * (n - 1)): cnt["FB3_FAIL"] += 1
        i = j
    if o is None: return
    for k in range(T):
        a, b = P[k], P[k + 1]; M = a["M"]
        Rb = {v for v in range(n) if U.reaches(U.nxt_of(g, b["s"], b["t"]), v, o)}
        for v in range(n):
            if v not in Rb:
                cnt["OFF_checks"] += 1
                if coarse(a["Xi"][v], M) != coarse(b["Xi"][v], M): cnt["OFF_FAIL"] += 1
        if tame[k]: continue
        A, B = a["sb"][o], b["sb"][o]
        cnt["J1_cases"] += 1
        if A == B or not lev(a["Xi"][A], a["Xi"][B]) > M: cnt["J1_FAIL"] += 1
        for e in g.succ[o]:
            if lev(a["Xi"][A], a["Xi"][e]) <= M:
                cnt["CAP_checks"] += 1
                if e not in Rb: cnt["CAP_FAIL"] += 1
        if a["Xi"][o][0] == o: cnt["nontame_o_cyclenode"] += 1

def cmp_coarse(E, x, y):
    """compare coarse values (c, mask) or full values by E's order: -1, 0, 1"""
    if len(x) == 3: kx, ky = E.key(x), E.key(y)
    else: kx, ky = (E.rew[x[0]], E.weight(x[1])), (E.rew[y[0]], E.weight(y[1]))
    return (kx > ky) - (kx < ky)

def rand_game(rng, lo, hi):
    n = rng.randint(lo, hi); owner = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), min(n, rng.choice((1, 2, 2, 3)))))) for _ in range(n)]
    return pg.Game([rng.randrange(n + 2) for _ in range(n)], owner, succ)

if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); c1o = len(a) > 5 and a[5] == "c1o"; rng = random.Random(seed)
        for _ in range(N):
            g = U.rand_c1o(rng, lo, hi) if c1o else rand_game(rng, lo, hi)
            if g is None: continue
            cnt["runs"] += 1; run(g, cnt, c1o)
    else:
        for p in a:
            g = U.load(p); c = Counter(); run(g, c, True); cnt.update({k: v for k, v in c.items() if "max" not in k})
            for k, v in c.items():
                if "max" in k: cnt[k] = max(cnt[k], v)
            if any("FAIL" in k for k in c) or c["SBMIN_notmin_cyc_o"]: print(p, {k: v for k, v in c.items() if "FAIL" in k or "notmin" in k})
            cnt["runs"] += 1
    print(dict(sorted(cnt.items())))
