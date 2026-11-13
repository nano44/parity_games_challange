#!/usr/bin/env python3
"""REFEREE-2 successor 41: own counters for a PRE-READ of L-SI's box 107 (claude/l-si 06f072f1, docs/si/box107-timing.md): the timing
lemmas of full key enumeration on 1P(G). Own code on r2unit217.M1P (1P(G) from box 217 §6.1); no lane code (not abandon107.py).

Per genome the key run s_0..s_T; μ_t(x), K(x) (built explicitly for movers with |K(x)| ≤ T + 1 only: a full or enumerating mover has
|K(x)| ≤ T + 1). x FULL: sw(x) = |K(x)| − 1; x ENUMERATES: μ(x) takes every value of K(x). Must-0 counters (unit in brackets):
 FULL-ORDER   fo [full mover]: μ(x) does not run through K(x) in decreasing order one predecessor per switch, or changes without a switch
 ABANDON      ab [(full mover, step)]: the W-target of x's option at s_t changes its key at step t
 ENUM-ABANDON eab [(enumerating mover, step)]: the W-target w of s_t(x) = k changes its key κ → κ′ at step t and not (s_(t+1)(x) = k and
              κ′ ++ ε(x, k) is the immediate predecessor of κ ++ ε(x, k) in K(x))
 ONE-AHEAD    oa [(enumerating mover, option, time)]: Λ = {λ ∈ K_k(x) : λ ≤ μ_t(x)} ≠ ∅ and μ_t(w) ++ ε(x, k) < max Λ
 CAUSE        cause [(mover, step t ≥ 1) with a switch]: no strict Ξ-descendant of x switched at step t − 1 and no mover on the W-chains
              (under s_t) below x's options switches at step t
 On 2-wide degree-2 ladders (two movers per level, option o of a level-(l+1) mover into mover o of level l) with levels 0..h − 1 CAPPED
 (both movers full), h ≥ 2:
 ODOMETER (1) od1 [level j ≤ h − 2]: M_j = K(a_j) ⊔ K(b_j) in decreasing order does not alternate between the two owners
 ODOMETER (3) od3 [(level j ≤ h − 2, reader z of level j + 1, position p)]: not W(p) ≤ E(z, p), or not E(z, p) < E(z, p + 1), or not
              E(z, p + 1) < W(p + 2)   (E, W: the step after which the reader / the owner is at position p; the start counts as step −1)
 FROZEN       fz [(level 1 ≤ j ≤ h − 2, move of S_j to position i at step t)]: F_j did not move to i at a step t_F < t, or a level-(j − 1)
              key changes at a step in (t_F, t], or S_j's other option is not key-preferred at some step of [t_F, t], or ΞC(S_j) (the
              other option strictly Ξ-better) is true on some s_u, t_F ≤ u < t, or false on s_t
 Ξ-LAST       xl [the same moves]: no mover on the Ξ-path (under s_(t−1)) of the option S_j moves to switched at step t − 1 (t ≥ 1)
 FLIP-SUPPLY  fs [degree-2 mover]: Σ of sw over strict Ξ-descendants < sw(x) − 1, or sw(x) > 2^|D(x)| when every mover of D(x) has degree 2
Info: full, enum (movers), capped h per ladder, units tested.
Controls (--ctrl NAME): abnf (ABANDON on NON-full movers of level ≥ 1), eabne (ENUM-ABANDON on non-enumerating movers), oastrict (ONE-AHEAD
with >), causexi (CAUSE without the W alternative), causew (CAUSE without the Ξ alternative), od3strict (W(p) < E(z, p) strictly),
fzlate (FROZEN's interval extended by one step, (t_F, t + 1]), xl2 (Ξ-LAST with step t − 2).
Usage: r2box107.py [--ctrl NAME] [--quiet] [--list FILE] [--gen COUNT SEED] [--lad COUNT SEED D] [--mut COUNT SEED MAXMUT FILE] FILES..."""
import sys, os, json, random
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "R2-P-N5-END")]
import r2end, r2unit217 as U

def keyset(m, x, cap, memo):
    """K(x) as a sorted list (increasing), or None if |K(x)| > cap"""
    if x in memo: return memo[x]
    if m.K[x] > cap: memo[x] = None; return None
    out = []
    for k in range(m.deg[x]):
        e = m.eps[(x, k)]
        if m.lev[x] == 0: out.append((e,))
        else:
            sub = keyset(m, m.wt[(x, k)], cap, memo)
            if sub is None: memo[x] = None; return None
            out += [kk + (e,) for kk in sub]
    out.sort(); memo[x] = out; return out

def wchain(m, x, k, s):
    P = []; y = m.wt[(x, k)]
    while y >= 0: P.append(y); y = m.wt[(y, s[y])]
    return P

def analyse(m, S, C, ctrl, info):
    N, T = m.N, len(S) - 1
    MU = [m.keys(s)[0] for s in S]; VX = [m.vals(s)[1] for s in S]
    sw = [sum(S[t + 1][x] != S[t][x] for t in range(T)) for x in range(N)]
    memo = {}; full = []; enum = []
    for x in range(N):
        Kx = keyset(m, x, T + 1, memo)
        if Kx is None: continue
        vals = {MU[t][x] for t in range(T + 1)}
        if sw[x] == len(Kx) - 1: full.append(x)
        if len(vals) == len(Kx): enum.append(x)
    info["full"] += len(full); info["enum"] += len(enum)
    pos = {x: {kk: i for i, kk in enumerate(memo[x])} for x in set(full) | set(enum)}
    # FULL-ORDER
    for x in full:
        bad = MU[0][x] != memo[x][-1]
        for t in range(T):
            a, b = MU[t][x], MU[t + 1][x]
            if a != b and (S[t + 1][x] == S[t][x] or pos[x][b] != pos[x][a] - 1): bad = True
        C["fo"] += bad
    # ABANDON
    for x in range(N):
        isfull = x in full
        if m.lev[x] == 0 or not (isfull if ctrl != "abnf" else not isfull): continue
        for t in range(T):
            w = m.wt[(x, S[t][x])]; info["ab_units"] += 1
            if MU[t + 1][w] != MU[t][w]: C["ab"] += 1
    # ENUM-ABANDON, ONE-AHEAD
    for x in range(N):
        isen = x in enum
        if m.lev[x] == 0: continue
        if (isen if ctrl != "eabne" else (not isen and memo.get(x) is not None)):
            px = pos[x] if x in pos else {kk: i for i, kk in enumerate(memo[x])}
            for t in range(T):
                k = S[t][x]; w = m.wt[(x, k)]
                if MU[t + 1][w] != MU[t][w]:
                    info["eab_units"] += 1; e = (m.eps[(x, k)],)
                    if S[t + 1][x] != k or px[MU[t + 1][w] + e] != px[MU[t][w] + e] - 1: C["eab"] += 1
        if isen:
            Kx = memo[x]
            for k in range(m.deg[x]):
                w = m.wt[(x, k)]; e = m.eps[(x, k)]; Kk = [kk for kk in Kx if kk[-1] == e]
                for t in range(T + 1):
                    lam = [kk for kk in Kk if kk <= MU[t][x]]
                    if not lam: continue
                    info["oa_units"] += 1; cur = MU[t][w] + (e,); top = max(lam)
                    if (cur <= top) if ctrl == "oastrict" else (cur < top): C["oa"] += 1
    # CAUSE
    for t in range(1, T):
        for x in range(N):
            if S[t + 1][x] == S[t][x]: continue
            info["cause_units"] += 1
            xi = any(S[t][y] != S[t - 1][y] for y in m.desc[x] - {x})
            wl = any(S[t + 1][y] != S[t][y] for k in range(m.deg[x]) if m.lev[x] > 0 for y in wchain(m, x, k, S[t]))
            if ctrl == "causexi": wl = False
            if ctrl == "causew": xi = False
            if not xi and not wl: C["cause"] += 1
    # FLIP-SUPPLY
    for x in range(N):
        if m.deg[x] != 2: continue
        D = m.desc[x] - {x}
        if sum(sw[y] for y in D) < sw[x] - 1: C["fs"] += 1
        if all(m.deg[y] == 2 for y in D) and sw[x] > 2 ** len(D): C["fs"] += 1
    # ladder part
    d = max(m.lev) + 1
    lad = N == 2 * d and all(m.lev[x] == x // 2 and m.deg[x] == 2 for x in range(N)) and \
        all(m.wt[(x, o)] == 2 * (m.lev[x] - 1) + o for x in range(N) if m.lev[x] > 0 for o in range(2))
    if not lad: return
    info["ladders"] += 1; h = 0
    while h < d and 2 * h in full and 2 * h + 1 in full: h += 1
    info["hmax"] = max(info["hmax"], h)
    if h < 2: return
    info["capped_ladders"] += 1
    arr = lambda x, kk: next(t for t in range(T + 1) if MU[t][x] == kk) - 1      # step after which x is at key kk (−1: at the start)
    for j in range(h - 1):                                                      # j ≤ h − 2
        a, b = 2 * j, 2 * j + 1
        Mj = sorted([(kk, a) for kk in memo[a]] + [(kk, b) for kk in memo[b]], reverse=True)
        owners = [o for _, o in Mj]; info["od1_units"] += 1
        if any(owners[i] == owners[i + 1] for i in range(len(owners) - 1)): C["od1"] += 1; continue
        Fj, Sj = owners[0], owners[1]
        W = [arr(o, kk) for kk, o in Mj]
        for z in (2 * (j + 1), 2 * (j + 1) + 1):
            E = [arr(z, kk + (m.eps[(z, o % 2)],)) for kk, o in Mj]
            for p in range(len(Mj)):
                info["od3_units"] += 1
                bad = (W[p] >= E[p] and not (W[p] == E[p] == -1)) if ctrl == "od3strict" else W[p] > E[p]
                if p + 1 < len(Mj) and not E[p] < E[p + 1]: bad = True
                if p + 2 < len(Mj) and not E[p + 1] < W[p + 2]: bad = True
                C["od3"] += bad
        if j >= 1:
            a0, b0 = 2 * (j - 1), 2 * (j - 1) + 1
            Mp = sorted([(kk, a0) for kk in memo[a0]] + [(kk, b0) for kk in memo[b0]], reverse=True)
            for i, (kk, o) in enumerate(Mp):
                ks = kk + (m.eps[(Sj, o % 2)],); kf = kk + (m.eps[(Fj, o % 2)],)
                t = arr(Sj, ks); tF = arr(Fj, kf)
                if t < 0: continue                                           # S_j starts there: not a move
                info["fz_units"] += 1; bad = not tF < t; hi = t + 1 if ctrl == "fzlate" else t
                if not bad:
                    for u in range(max(tF + 1, 0), hi + 1):
                        if u < T and (MU[u + 1][a0] != MU[u][a0] or MU[u + 1][b0] != MU[u][b0]): bad = True
                    for u in range(max(tF, 0), t + 1):
                        oth = 1 - S[u][Sj]
                        kc = MU[u + 1][m.wt[(Sj, oth)]] < MU[u + 1][m.wt[(Sj, S[u][Sj])]]
                        xc = VX[u][(Sj, oth)] > VX[u][(Sj, S[u][Sj])]
                        if not kc: bad = True
                        if (u < t and xc) or (u == t and not xc): bad = True
                C["fz"] += bad
                if t >= 1:
                    info["xl_units"] += 1; tt = t - 2 if ctrl == "xl2" else t - 1
                    newopt = S[t + 1][Sj]
                    path = m.xipath(m.xt[(Sj, newopt)], S[t - 1]) if m.xt[(Sj, newopt)] >= 0 else []
                    if tt < 0 or not any(S[tt + 1][y] != S[tt][y] for y in path): C["xl"] += 1

MUST0 = ["fo", "ab", "eab", "oa", "cause", "fs", "od1", "od3", "fz", "xl"]

def main(a):
    ctrl = ""; quiet = False; Gs = []; i = 0
    while i < len(a):
        if a[i] == "--ctrl": ctrl = a[i + 1]; i += 2
        elif a[i] == "--quiet": quiet = True; i += 1
        elif a[i] == "--list":
            for l in open(a[i + 1]):
                h, _, pth = l.split(None, 2); G = json.load(open(pth.strip())); Gs.append((h[:10], G.get("genome", G)))
            i += 2
        elif a[i] == "--gen":
            rng = random.Random(int(a[i + 2])); c = 0
            while c < int(a[i + 1]):
                G = r2end.gen(rng, "acyc")
                if r2end.acyclic(G): Gs.append((f"gen{a[i + 2]}#{c}", G)); c += 1
            i += 3
        elif a[i] == "--lad":
            rng = random.Random(int(a[i + 2])); Gs += [(f"lad{a[i + 3]}_{a[i + 2]}#{c}", U.lad(rng, int(a[i + 3]))) for c in range(int(a[i + 1]))]; i += 4
        elif a[i] == "--mut":
            rng = random.Random(int(a[i + 2])); G0 = json.load(open(a[i + 4])); G0 = G0.get("genome", G0)
            Gs += [(f"mut{a[i + 2]}_{os.path.basename(a[i + 4])}#{c}", U.mutate(G0, rng, rng.randint(1, int(a[i + 3])))) for c in range(int(a[i + 1]))]; i += 5
        else:
            G = json.load(open(a[i])); G = G.get("genome", G)
            if r2end.acyclic(G): Gs.append((os.path.basename(a[i]), G))
            i += 1
    C = defaultdict(int); info = defaultdict(int)
    for name, G in Gs:
        m = U.M1P(G); S = m.run(); before = dict(C); i0 = dict(info)
        analyse(m, S, C, ctrl, info); info["runs"] += 1; info["steps"] += len(S) - 1
        if not quiet:
            print(f"{name} N {m.N} T {len(S) - 1} full {info['full'] - i0.get('full', 0)} enum {info['enum'] - i0.get('enum', 0)} "
                  + " ".join(f"{k} {C[k] - before.get(k, 0)}" for k in MUST0), flush=True)
    print(f"TOTAL ctrl {ctrl or '-'}: " + " ".join(f"{k} {C[k]}" for k in MUST0))
    print("INFO " + " ".join(f"{k} {info[k]}" for k in ("runs", "steps", "full", "enum", "ab_units", "eab_units", "oa_units", "cause_units",
                                                         "ladders", "capped_ladders", "hmax", "od1_units", "od3_units", "fz_units", "xl_units")))
    print("FIRED " + (" ".join(k for k in MUST0 if C[k]) or "none"))

if __name__ == "__main__":
    main(sys.argv[1:])
