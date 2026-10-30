#!/usr/bin/env python3
"""REFEREE successor 19: own control for packet P-N5-LATEP (L-SI box 53, l-si b63f2554, sha1 b15223e5).
Own engine rl_engine (SPEC S1-S5 from the text; no lane code). Per W-run F = [a, b] (tau-stretch, no S4c fallback, lambda_W constant):
  SUB    every LATE' adoption is R88-late
  FWR    FW-R*': WCH_F <= (n - 1)(R*'_T + 1)
  LS     LATE-SPLIT' (ii) for every REPEAT': unique leave k in (p, u); blocked t in [k+1, u-1]; off-cycle on [k+1, t] => W_t(z) > W_{k+1}(z)
  CIR    CIRCLE': REP' <= n_E R*', R*' <= m_E + REP', REP' <= X' + sum_z d_E(z) WCH_F(z)   (X' with the earliest blocked t)
  GC     GAP-CLIMB: s exists, z in Z_s, Xi climbs; tokens distinct; #LATE'(y, z) <= ZXC_F(z)
  CH     CHAIN: GXC <= TXC <= ZXC, ZXC = TXC + WZ
  TD     TXC-DESCENT along z's (sigma_{s+1}, sigmabar_{s+1})-play; TR  TXC-RED; LCT total <= n(n - 1)
MUT: 1 LATE-SPLIT' (ii) with R88-late REPEATs (block anywhere in F); 2 GAP-CLIMB with s searched from a (not t_b);
  3 TXC-DESCENT without terminal T3 (gates); 4 TXC-DESCENT without T4; 5 GAP-CLIMB with R88-late adoptions (distinct tokens).
Usage: latep_probe.py rand N lo hi seed | FILES...  (env MUT, MAXN, RANDSTARTS, NOSTART)"""
import sys, os, random
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
MUT = int(os.environ.get("MUT", "0"))
EX = []


def fail(cnt, tag, *a):
    cnt[tag + "_V"] += 1
    if len(EX) < 30: EX.append((tag,) + a)


def analyse(cnt, g, start, name):
    n = g.n; key = g.key; st = RE.run(g, start); T = len(st) - 1
    cnt["RUNS"] += 1; cnt["TRANS"] += T
    ev = [v for v in range(n) if g.owner[v] == 0]; nE = len(ev); mE = sum(len(g.succ[v]) for v in ev)
    dE = Counter(w for v in ev for w in g.succ[v])
    S = [x["s"] for x in st]; TA = [tuple(x["t"][v] for v in range(n) if g.owner[v] == 1) for x in st]
    nx = lambda s, t: [s[v] if g.owner[v] == 0 else t[v] for v in range(n)]
    W = [[RE.play_value(g, nx(S[t], st[t]["t"]), v) for v in range(n)] for t in range(T + 1)]
    X = [x["Xi"] for x in st]; Is = [set(x["Is"]) for x in st]; SB = [x["sb"] for x in st]
    fb = [st[t]["fb"] for t in range(T)]; tch = [TA[t + 1] != TA[t] for t in range(T)]
    lamW = [tuple(w[0] for w in W[t]) for t in range(T + 1)]; lamX = [tuple(x[0] for x in X[t]) for t in range(T + 1)]
    Z = [{v for v in range(n) if X[t][v] != W[t][v]} for t in range(T + 1)]
    D = [{o for o in range(n) if g.owner[o] == 1 and SB[t][o] != st[t]["t"][o]} for t in range(T + 1)]
    blocked = lambda t, y, z: z != S[t][y] and key(W[t][z]) > key(W[t][S[t][y]]) and (y, z) not in Is[t]
    gt = lambda a_, b_: key(a_) > key(b_)
    wr = []; a = 0
    for t in range(1, T + 2):
        if t == T + 1 or fb[t - 1] or tch[t - 1] or lamW[t] != lamW[t - 1]: wr.append((a, t - 1)); a = t
    lct_total = 0
    for (a, b) in wr:
        if b == a: continue
        cnt["WRUNS"] += 1
        tr = range(a, b)
        lct = sum(lamX[s + 1] != lamX[s] for s in tr); lct_total += lct
        wch = sum(W[s + 1] != W[s] for s in tr)
        wchz = {z: sum(W[s + 1][z] != W[s][z] for s in tr) for z in range(n)}
        adopt = defaultdict(list)
        for u in tr:
            for y in ev:
                if S[u + 1][y] != S[u][y]: adopt[(y, S[u + 1][y])].append(u)
        latep = defaultdict(list); rtp = set(); rt = set(); late88 = defaultdict(list)
        for (y, z), us in adopt.items():
            prev = None
            for u in us:
                lo = a if prev is None else max(a, prev + 1)
                bl = [t for t in range(lo, u) if blocked(t, y, z)]
                b88 = [t for t in range(a, u) if blocked(t, y, z)]
                if b88: rt.add(u); late88[(y, z)].append((u, prev, b88))
                if bl:
                    rtp.add(u); latep[(y, z)].append((u, prev, bl))
                    if not b88: fail(cnt, "SUB", name, y, z, u)
                prev = u
        RTP = len(rtp); cnt["LATEP"] += sum(len(x) for x in latep.values()); cnt["LATE88"] += sum(len(x) for x in late88.values())
        if wch > (n - 1) * (RTP + 1): fail(cnt, "FWR", name, a, wch, RTP)
        # LATE-SPLIT' (ii), CIRCLE'
        rep = 0; xp = 0; nonx_by_z = Counter()
        src = latep if MUT != 1 else late88
        for (y, z), L in src.items():
            for (u, p, bl) in L[1:]:
                rep += 1
                ks = [k for k in range(p + 1, u) if S[k][y] == z and S[k + 1][y] != z]
                if len(ks) != 1 and MUT != 1: fail(cnt, "LSK", name, y, z, u, ks)
                if not ks: continue
                k = ks[-1]; cand = [t for t in bl if t >= k + 1]
                if not cand: fail(cnt, "LST" if MUT != 1 else "LSTmut", name, y, z, u); continue
                t = cand[0]
                off = all(W[x][y][0] != y for x in range(k + 1, t + 1))
                if not off: xp += 1; continue
                nonx_by_z[z] += 1; cnt["LS_chk"] += 1
                if not gt(W[t][z], W[k + 1][z]): fail(cnt, "LS" if MUT != 1 else "LSmut", name, y, z, u, k, t)
        if MUT != 1:
            cnt["REPP"] += rep; cnt["XP"] += xp
            if rep > nE * RTP: fail(cnt, "CIR1", name, a)
            if RTP > mE + rep: fail(cnt, "CIR2", name, a)
            if rep > xp + sum(dE[z] * wchz[z] for z in range(n)): fail(cnt, "CIR3", name, a)
            for z, c in nonx_by_z.items():
                if c > dE[z] * wchz[z]: fail(cnt, "CIR3z", name, a, z)
        # ZXC, TXC, WZ, GXC sets
        ZXC = {(z, s) for s in tr for z in range(n) if z in Z[s] and gt(X[s + 1][z], X[s][z])}
        TXC = {(z, s) for s in tr for z in range(n) if gt(X[s + 1][z], X[s][z]) and W[s + 1][z] == W[s][z]}
        WZ = {(z, s) for (z, s) in ZXC if W[s + 1][z] != W[s][z]}
        GXC = {(v, s) for s in tr for v in ev if S[s + 1][v] != S[s][v] and TA[s + 1] == TA[s] and lamX[s + 1] == lamX[s]
               and v in Z[s] and gt(X[s + 1][v], X[s][v]) and not gt(W[s + 1][v], W[s][v])}
        cnt["ZXC"] += len(ZXC); cnt["TXC"] += len(TXC); cnt["GXC"] += len(GXC); cnt["WZ"] += len(WZ)
        if not GXC <= TXC: fail(cnt, "CH1", name, a)
        if not TXC <= ZXC: fail(cnt, "CH2", name, a)
        if ZXC != TXC | WZ or TXC & WZ: fail(cnt, "CH3", name, a)
        for z in range(n):
            if sum(1 for (x, s) in WZ if x == z) > wchz[z]: fail(cnt, "CH4", name, a, z)
        # GAP-CLIMB
        src = latep if MUT != 5 else late88
        for (y, z), L in src.items():
            toks = []
            for (u, p, bl) in L:
                tb = bl[-1] if MUT != 2 else a
                ss = [s for s in range(tb, u) if X[s + 1][z] != X[s][z]]
                cnt["GC_chk"] += 1
                if not ss: fail(cnt, "GC0", name, y, z, u); continue
                s = ss[0]
                if not (z in Z[s] and gt(X[s + 1][z], X[s][z])): fail(cnt, "GC" if MUT != 2 else "GCmut", name, y, z, u, s)
                toks.append(s)
            if len(set(toks)) != len(toks): fail(cnt, "GCTOK" if MUT != 5 else "GCTOKmut", name, y, z)
            zx = sum(1 for (x, s) in ZXC if x == z)
            if MUT != 5 and len(L) > zx: fail(cnt, "GCN", name, y, z)
        # TXC-DESCENT
        term = Counter()
        for (z, s) in TXC:
            nxs = [S[s + 1][v] if g.owner[v] == 0 else SB[s + 1][v] for v in range(n)]
            x = z; seen = set(); ok = False
            while x not in seen:
                if (x, s) not in TXC: fail(cnt, "TDX", name, z, s, x); break
                seen.add(x)
                t1 = lamX[s + 1][x] != lamX[s][x]
                t2 = g.owner[x] == 0 and S[s + 1][x] != S[s][x]
                t3 = g.owner[x] == 1 and (x in D[s] or x in D[s + 1]) and MUT != 3
                t4 = W[s][x][0] == x and MUT != 4
                if t1 or t2 or t3 or t4:
                    ok = True; kind = "T1" if t1 else "T2" if t2 else "T3" if t3 else "T4"; cnt["TD_" + kind] += 1
                    term[(x, s, kind)] += 1
                    if t2 and lamX[s + 1] == lamX[s] and (x, s) not in GXC: fail(cnt, "TDG", name, z, s, x)
                    break
                x = nxs[x]
            if not ok: fail(cnt, "TD" if MUT not in (3, 4) else "TDmut", name, z, s)
        GATE = {(o, s) for (o, s) in TXC if g.owner[o] == 1 and (o in D[s] or o in D[s + 1])}
        CNW = {(x, s) for (x, s) in TXC if W[s][x][0] == x}
        cnt["GATE"] += len(GATE); cnt["CNW"] += len(CNW); cnt["LCT"] += lct
        if len(TXC) > n * (len(GXC) + len(GATE) + len(CNW)) + n * n * lct: fail(cnt, "TR", name, a)
    if lct_total > n * (n - 1): fail(cnt, "LCT", name)


def main(a):
    import core_probe as CP, dual_probe as D
    cnt = Counter(); nst = int(os.environ.get("RANDSTARTS", "0"))
    def do(g, name, extra=None):
        r = random.Random(name)
        starts = ([extra] if extra and not os.environ.get("NOSTART") else []) + [RE.best_reward_start(g)] + [D.rand_start(g, r) for _ in range(nst)]
        for s0 in starts:
            try: analyse(cnt, g, s0, name)
            except RuntimeError: cnt["maxit"] += 1
    if a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            do(D.rand_ck(r2, nn, r2.randint(0, min(5, nn - 1))), "rand%d" % i)
    else:
        for path in a:
            if path.endswith(".start"): continue
            try: g = RE.parse(path)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "40")): cnt["skip_big"] += 1; continue
            sp = path[:-3] + ".start"; ex = None
            if os.path.exists(sp):
                try: ex = CP.parse_start(g, sp)
                except Exception: cnt["start_err"] += 1
            cnt["GAMES"] += 1; do(g, os.path.relpath(path), ex)
    for k in sorted(cnt): print(k, cnt[k])
    print("VIOLATIONS", sum(v for k, v in cnt.items() if k.endswith("_V")))
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
