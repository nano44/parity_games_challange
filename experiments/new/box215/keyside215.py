#!/usr/bin/env python3
"""Box 215 KEYSIDE-ALL DATA (L-NEW successor 75). N5 (box190 n5v.step, mode KM_MODE = spec (default) | xi) from S3 on Gamma3(G) up to its
first fallback; the movers' options s_0, ..., s_T read through gamma3.mover_state. Keys are computed HERE from the genome alone, by
P-IDEAL-KEYS §0's definition: key_s(x, k) = (g(x, k)) at level 0 (or when wt < 0), else key_s(wt(x, k), s(wt(x, k))) + (g(x, k)),
g = G["gate"]; compared lexicographically. KP_s(x) = the key-least option; KF_x = #steps where KP changes; W(x) = W-closure of x.
Must-0 counters (any genome, Xi-cyclic included):
  lkp    (unit (step, mover)): KP(x) changes at step t but no mover of W(x) moves at t                         [LOCAL-KP (b)]
  pkf    (unit (state, degree-2 mover of level >= 1 with distinct W-targets a, b)): KP_s(x) = 0 differs from ord_s(a, b)   [PAIR-KF (b)]
  pkfa   (unit (state, degree-2 mover of level >= 1 with equal W-targets)): KP_s(x) is not the smaller-gate option   [PAIR-KF (a)]
  kflip  (unit movers of degree <= 2): moves(x) > 1 + KF_x                                                     [KEYFLIP / PAIR-MOVES]
  casc   (unit (step, same-level pair)): a flip of (p, q) that is neither own nor below                         [CASCADE]
  ftt    (unit pairs): flips(p, q) > T                                                                         [F <= T]
  ladder (unit (genome, level)): on an L^R_d-shaped genome, F(0) > moves(0) + moves(1) or F(l) > moves(2l) + moves(2l + 1) + F(l - 1)
Descriptive: T, xcyc (1 if the Xi-graph x -> xt has a cycle), lr (1 if L^R_d-shaped), flipsum, maxF, maxmoves.
Controls: KM_MODE=xi (N5'-xi: Howard's tie rule) must fire kflip; KS_CTRL=1 (keys with the gate indices replaced by a fixed random
  permutation, seed 5; reversing the order would be inert: every comparison flips at the same steps) must fire kflip; KS_CTRL=2 (CASCADE
  without its «own» case) must fire casc where own flips exist.
Usage: keyside215.py G.json ... | keyside215.py --rand SEED COUNT MODE [cyc]   (cyc: count only Xi-cyclic genomes)"""
import sys, os, json, random, collections, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box208"))
import level208
import n5v, eg195, gamma3, n5x
MODE = os.environ.get("KM_MODE", "spec"); CTRL = os.environ.get("KS_CTRL", "0")
KEYS = ("lkp", "pkf", "pkfa", "kflip", "casc", "ftt", "ladder", "T", "xcyc", "lr", "flipsum", "maxF", "maxmoves")
MAXK = ("T", "maxF", "maxmoves")

def cyclic(G):
    adj = {x: [xt for (_, xt, _) in G["opts"][x] if xt >= 0] for x in range(G["N"])}; col = {}
    def dfs(x):
        col[x] = 1
        for y in adj[x]:
            if col.get(y) == 1 or (y not in col and not dfs(y)): return False
        col[x] = 2; return True
    return int(not all(x in col or dfs(x) for x in adj))

def lrshaped(G):
    lev = G["lev"]; N = G["N"]; d = max(lev) + 1
    if N != 2 * d or any(lev[x] != x // 2 for x in range(N)) or any(len(o) != 2 for o in G["opts"]): return 0
    return int(all(G["opts"][x][k][0] == 2 * (lev[x] - 1) + k for x in range(N) if lev[x] >= 1 for k in (0, 1)))

def states(G):
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0)
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    S = [gamma3.mover_state(G, V, sigma, eg195.PADS)]
    while len(S) <= 20000:
        res = n5v.step(g, E, Ed, sigma, tau, MODE)
        if res is None or res[4]: break
        sigma, tau = list(res[0]), list(res[1]); S.append(gamma3.mover_state(G, V, sigma, eg195.PADS))
    return S

def one(G):
    N, lev, opts = G["N"], G["lev"], G["opts"]; gate = G["gate"]; sgn = 1
    if CTRL == "1":
        M = sum(len(o) for o in opts); perm = list(range(M)); random.Random(5).shuffle(perm); gate = [[perm[gk] for gk in row] for row in gate]
    S = states(G); T = len(S) - 1; c = collections.Counter(); c["T"] = T; c["xcyc"] = cyclic(G); c["lr"] = lr = lrshaped(G)
    assert all(k >= 0 for s in S for k in s), "a mover off its gates"
    order = sorted(range(N), key=lambda x: lev[x])
    def keys(s):
        K = {}
        for x in order:
            for k, (wt, _, _) in enumerate(opts[x]):
                K[(x, k)] = ((sgn * gate[x][k],) if wt < 0 or lev[x] == 0 else K[(wt, s[wt])] + (sgn * gate[x][k],))
        return K
    Ks = [keys(s) for s in S]
    KP = [[min(range(len(opts[x])), key=lambda k: K[(x, k)]) for x in range(N)] for K in Ks]
    W = []
    for x in range(N):
        seen = set(); st = [w for (w, _, _) in opts[x] if w >= 0]
        while st:
            y = st.pop()
            if y in seen: continue
            seen.add(y); st += [w for (w, _, _) in opts[y] if w >= 0]
        W.append(seen)
    Mv = [None] + [set(x for x in range(N) if S[t][x] != S[t - 1][x]) for t in range(1, T + 1)]
    moves = [sum(1 for t in range(1, T + 1) if x in Mv[t]) for x in range(N)]; c["maxmoves"] = max(moves) if moves else 0
    KF = [sum(1 for t in range(1, T + 1) if KP[t][x] != KP[t - 1][x]) for x in range(N)]
    for t in range(1, T + 1):
        for x in range(N):
            if KP[t][x] != KP[t - 1][x] and not (Mv[t] & W[x]): c["lkp"] += 1
    for x in range(N):
        if len(opts[x]) == 2 and lev[x] >= 1:
            a, b = opts[x][0][0], opts[x][1][0]
            for t, (s, K) in enumerate(zip(S, Ks)):
                if a != b:
                    if (KP[t][x] == 0) != (K[(a, s[a])] < K[(b, s[b])]): c["pkf"] += 1
                elif KP[t][x] != min((0, 1), key=lambda k: sgn * gate[x][k]): c["pkfa"] += 1
        if len(opts[x]) <= 2 and moves[x] > 1 + KF[x]: c["kflip"] += 1
    flips = {}
    for l in set(lev):
        for p, q in itertools.combinations([x for x in range(N) if lev[x] == l], 2):
            ord_ = [Ks[t][(p, S[t][p])] < Ks[t][(q, S[t][q])] for t in range(T + 1)]; f = 0
            for t in range(1, T + 1):
                if ord_[t] == ord_[t - 1]: continue
                f += 1
                if CTRL != "2" and (p in Mv[t] or q in Mv[t]): continue
                if l == 0: c["casc"] += 1; continue
                kp, kq = S[t][p], S[t][q]
                wp, wq = opts[p][kp][0], opts[q][kq][0]
                if wp == wq or wp < 0 or wq < 0: c["casc"] += 1; continue
                if (Ks[t][(wp, S[t][wp])] < Ks[t][(wq, S[t][wq])]) == (Ks[t - 1][(wp, S[t - 1][wp])] < Ks[t - 1][(wq, S[t - 1][wq])]): c["casc"] += 1
            flips[(p, q)] = f; c["flipsum"] += f
            if f > T: c["ftt"] += 1
    if lr:
        d = max(lev) + 1; F = [flips.get((2 * l, 2 * l + 1), 0) for l in range(d)]; c["maxF"] = max(F)
        if F[0] > moves[0] + moves[1]: c["ladder"] += 1
        for l in range(1, d):
            if F[l] > moves[2 * l] + moves[2 * l + 1] + F[l - 1]: c["ladder"] += 1
    return c

def fmt(c): return " ".join("%s %d" % (k, c[k]) for k in KEYS)

if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--rand":
        seed, cnt, mode = int(a[1]), int(a[2]), a[3]; only = len(a) > 4 and a[4] == "cyc"; rng = random.Random(seed); k = 0; tot = collections.Counter()
        while k < cnt:
            G = eg195.gen(rng, mode)
            if G is None or G["N"] < 2 or (only and not cyclic(G)): continue
            k += 1; cc = one(G)
            for key in KEYS: tot[key] = max(tot[key], cc[key]) if key in MAXK else tot[key] + cc[key]
        print("rand", mode, "seed", seed, "genomes", k, "cyconly", int(only), "KM_MODE", MODE, "ctrl", CTRL, fmt(tot), flush=True)
    else:
        for fn in a:
            G = json.load(open(fn)); G = G.get("genome", G)
            print(os.path.basename(fn), "KM_MODE", MODE, "ctrl", CTRL, fmt(one(G)), flush=True)
