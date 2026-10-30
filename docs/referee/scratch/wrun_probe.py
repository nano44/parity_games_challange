#!/usr/bin/env python3
"""REFEREE successor 20: own control for packet P-N5-WRUN (L-NEW box 92, l-new 7668bc9b, sha1 fae68aa0). Own engine rl_engine; no lane code.
W-run = maximal run of states of one tau-stretch with no S4c fallback transition and no lambda_W change (RESULTS R89).
Checks (per W-run F, transitions t -> t+1 with t, t+1 in F):
  STEP  every transition switches an Even vertex; switched v takes an edge of Isigma_t
  XR    XI-RUN on F and on every sub-stretch R of F (|R| <= sum SW_R <= m_E + sum_c d_E(c) RISE_R(c)); SWR SW-RETURN per (v, c) on F
  RET   RET-XiRISE: each return k -> k+1 of X to g (last leave s) has Xi_k(g) > Xi_s(g); RET_F(X,g) <= XiCH_F(g)
  E0    E0-BOUND E0_F(X, g) <= n;  WC  WAIT-CYCLE' (REG self-routed blocks; later states of the WHOLE run)
  GD    GAP-DEV;  XP  XiCH-PCH;  RS  RSTAR-PCH (R*_F <= sum_(y,z) XiCH_F(z));  PM  PREFIX-MON k=1..3;  LR  LEVEL-RED k=1..3
  ND    NO-DEV when Xi = W on all of F;  SUB  [SUB] on every sub-interval of F;  BR  BIP-RED;  RW  REL2-WRISE under (A1), (A2)
MUT: 1 WAIT-CYCLE' without "pi avoids Z*" (and without g != sigma X): tests the line's block definition; 2 RET-XiRISE with Xi_k(g) > Xi_{s+1}(g)
     (window from s+1: may fail); 5 WAIT-CYCLE' with the LINE's block definition (g = sigma_t(X) allowed, no Z* avoidance); 3 [SUB] with (n-2) in place of (n-1); 4 XI-RUN without the m_E term.
Usage: wrun_probe.py FILES... | rand N lo hi seed   (env MUT, MAXN, NOSTART, ONLYSTART, STARTF, NOWC)"""
import sys, os, random
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
MUT = int(os.environ.get("MUT", "0"))
EX = []; STAT = Counter()


def fail(cnt, tag, *a):
    cnt[tag + "_V"] += 1
    if len(EX) < 40: EX.append((tag,) + a)


def nxs(g, s, t): return [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]


def wruns(g, st, W):
    out, a = [], 0
    for k in range(len(st) - 1):
        cut = st[k]["t"] != st[k + 1]["t"] or st[k]["fb"] or [x[0] for x in W[k]] != [x[0] for x in W[k + 1]]
        if cut: out.append((a, k)); a = k + 1
    out.append((a, len(st) - 1))
    return out


def gt(g, x, y): return g.key(x) > g.key(y)


def terms(g, m):
    out, r = [], g.n - 1
    while r >= 0:
        if (m >> r) & 1: out.append((2, r) if g.prio[g.byrank[r]] % 2 == 0 else (0, -r))
        r -= 1
    return out


def prek(g, m, k):
    t = terms(g, m)[:k]
    return tuple(t + [(1, 0)] * (k - len(t)))


def analyse(cnt, g, start, name):
    st = RE.run(g, start); n = g.n; T = len(st) - 1
    Ev = [v for v in range(n) if g.owner[v] == 0]
    mE = sum(len(g.succ[v]) for v in Ev); dE = Counter(c for v in Ev for c in g.succ[v])
    W = [[RE.play_value(g, nxs(g, s["s"], s["t"]), v) for v in range(n)] for s in st]
    Xi = [s["Xi"] for s in st]
    Iset = [set(s["Is"]) for s in st]
    def blocked(t, y, z): return z != st[t]["s"][y] and gt(g, W[t][z], W[t][st[t]["s"][y]]) and (y, z) not in Iset[t]
    # WAIT-CYCLE' over the whole run: collect REG blocks, then test later states
    if not os.environ.get("NOWC"):
        for t in range(T + 1):
            s, sb = st[t]["s"], st[t]["sb"]; nx = nxs(g, s, sb)
            for X in Ev:
                preX, Zs = RE.lasso(nx, X); Z = set(Zs); cst = Xi[t][X][0]
                for gg in g.succ[X]:
                    if (X, gg) in Iset[t]: continue
                    if gg == s[X] and MUT != 5: continue
                    pi, x = [], gg; ok = True; seen = set()
                    while x != X:
                        if x in seen: ok = False; break
                        seen.add(x); pi.append(x); x = nx[x]
                    if not ok: continue
                    if X in Z and any(v in Z for v in pi):
                        if MUT not in (1, 5): continue
                    E0 = cst == X and all(g.rank[v] < g.rank[X] for v in pi)
                    if E0: continue
                    cnt["WC_blocks"] += 1
                    pat = [(v, s[v]) for v in pi if g.owner[v] == 0]
                    for t2 in range(t + 1, T + 1):
                        if st[t2]["s"][X] == gg and all(st[t2]["s"][v] == w for v, w in pat):
                            fail(cnt, "WC", name, t, X, gg, t2); break
    for (a, b) in wruns(g, st, W):
        L = b - a; cnt["wruns"] += 1; cnt["trans"] += L
        if L == 0: continue
        SW = Counter(); ENT = Counter(); RISE = Counter(); WCH = 0; FL = 0
        for k in range(a, b):
            sw = [v for v in Ev if st[k]["s"][v] != st[k + 1]["s"][v]]
            if not sw: fail(cnt, "STEP", name, k)
            for v in sw:
                SW[v] += 1; ENT[(v, st[k + 1]["s"][v])] += 1
                if (v, st[k + 1]["s"][v]) not in Iset[k]: fail(cnt, "STEPI", name, k, v)
            for c in range(n):
                if Xi[k][c] != Xi[k + 1][c]: RISE[c] += 1
            if W[k] != W[k + 1]: WCH += 1
            else: FL += 1
        bound = (0 if MUT == 4 else mE) + sum(dE[c] * RISE[c] for c in range(n))
        if not (L <= sum(SW.values()) <= bound): fail(cnt, "XR", name, a, b)
        STAT["xr_ratio_x1000"] = max(STAT["xr_ratio_x1000"], 1000 * L // max(1, bound))
        for (v, c), e in ENT.items():
            if e > 1 + RISE[c]: fail(cnt, "SWR", name, a, v, c)
        # sub-stretches (XI-RUN) and [SUB]
        Wch = [W[k] != W[k + 1] for k in range(a, b)]
        late_at = {}
        BL = [[(y, z) for y in Ev for z in g.succ[y] if blocked(k, y, z)] for k in range(a, b)]
        SWk = [[v for v in Ev if st[k]["s"][v] != st[k + 1]["s"][v]] for k in range(a, b)]
        RIk = [[c for c in range(n) if Xi[k][c] != Xi[k + 1][c]] for k in range(a, b)]
        for a2 in range(a, b):
            blk = set(); Rs = 0; wc = 0; sws = 0; ri = Counter()
            for k in range(a2, b):
                blk.update(BL[k - a])          # blocked at a state of [a2, k]; an edge blocked at k is not in I(k), so not adoptable at k -> k+1
                if any((v, st[k + 1]["s"][v]) in blk for v in SWk[k - a]): Rs += 1
                wc += Wch[k - a]; sws += len(SWk[k - a])
                for c in RIk[k - a]: ri[c] += 1
                if not (k + 1 - a2 <= sws <= (0 if MUT == 4 else mE) + sum(dE[c] * ri[c] for c in ri)): fail(cnt, "XR", name, a2, k + 1)
                if wc > (n - (2 if MUT == 3 else 1)) * (Rs + 1): fail(cnt, "SUB", name, a, b, a2, k + 1)
                cnt["SUB_chk"] += 1
        # returns: RET-XiRISE, E0-BOUND
        held = defaultdict(set); lastleave = {}; RET = Counter()
        for X in Ev: held[X].add(st[a]["s"][X])
        for k in range(a, b):
            for X in Ev:
                d, e = st[k]["s"][X], st[k + 1]["s"][X]
                if d == e: continue
                lastleave[(X, d)] = k
                if e in held[X]:
                    RET[(X, e)] += 1
                    s0 = lastleave.get((X, e))
                    if s0 is not None:
                        ref = Xi[s0 + 1][e] if MUT == 2 else Xi[s0][e]
                        if not gt(g, Xi[k][e], ref): fail(cnt, "RET", name, k, X, e)
                held[X].add(e)
        for (X, e), r in RET.items():
            if r > RISE[e]: fail(cnt, "RETC", name, a, X, e)
        # GAP-DEV, R*_F, RSTAR-PCH
        Rstar = 0; blk = set()
        for k in range(a, b + 1):
            if k > a:
                sw = [v for v in Ev if st[k - 1]["s"][v] != st[k]["s"][v]]
                if any((v, st[k]["s"][v]) in blk for v in sw): Rstar += 1
            if k == b: break
            for y in Ev:
                for z in g.succ[y]:
                    if blocked(k, y, z):
                        blk.add((y, z)); cnt["GD_chk"] += 1
                        if not gt(g, W[k][z], Xi[k][z]): fail(cnt, "GD", name, k, y, z)
                        nx = nxs(g, st[k]["s"], st[k]["sb"]); pre, cy = RE.lasso(nx, z)
                        if not any(g.owner[o] == 1 and st[k]["sb"][o] != st[k]["t"][o] for o in pre + cy): fail(cnt, "GD2", name, k, y, z)
        if Rstar > sum(RISE[z] for y in Ev for z in g.succ[y]): fail(cnt, "RS", name, a, b)
        STAT["maxRstar"] = max(STAT["maxRstar"], Rstar)
        # XiCH-PCH, PREFIX-MON, LEVEL-RED
        for z in range(n):
            pch = 0; deep = Counter(); lowch = Counter()
            for k in range(a, b):
                x0, x1 = Xi[k][z], Xi[k + 1][z]
                if x0[0] == x1[0] and x0[1] != x1[1]:
                    pch += 1; r = (x0[1] ^ x1[1]).bit_length() - 1; dep = bin(x0[1] >> (r + 1)).count("1")
                    for kk in (1, 2, 3):
                        p0, p1 = prek(g, x0[1], kk), prek(g, x1[1], kk)
                        if p1 < p0 or (dep < kk and not p1 > p0): fail(cnt, "PM", name, k, z, kk)
                        if dep >= kk: deep[kk] += 1
                if x0[0] == x1[0] and x0[1] != x1[1]:
                    for kk in (1, 2, 3):
                        p0, p1 = prek(g, x0[1], kk), prek(g, x1[1], kk)
                        if p1 < p0: fail(cnt, "PM", name, k, z, kk)
            if RISE[z] > n * (n + 1 + pch): fail(cnt, "XP", name, a, z)
            for kk in (1, 2, 3):
                if pch > n * (2 * n + 1) ** kk + deep[kk]: fail(cnt, "LR", name, a, z, kk)
        # NO-DEV
        if all(Xi[k] == W[k] for k in range(a, b + 1)):
            cnt["ND_runs"] += 1
            if Rstar != 0 or WCH > n - 1 or L > (n - 1) + 4 * n * n * (n - 1): fail(cnt, "ND", name, a, b)
            STAT["ND_maxlen"] = max(STAT["ND_maxlen"], L)
        # BIP-RED
        SB = sum(1 for k in range(a, b) if st[k]["sb"] != st[k + 1]["sb"])
        phis, a2 = [], a
        for k in range(a, b):
            if st[k]["sb"] != st[k + 1]["sb"]: phis.append((a2, k)); a2 = k + 1
        phis.append((a2, b)); Ro = 0
        for (p, q) in phis:
            blk = set(); r = 0
            for k in range(p, q):
                for y in Ev:
                    for z in g.succ[y]:
                        if blocked(k, y, z): blk.add((y, z))
                sw = [v for v in Ev if st[k]["s"][v] != st[k + 1]["s"][v]]
                if any((v, st[k + 1]["s"][v]) in blk for v in sw): r += 1
            Ro = max(Ro, r)
        if L > SB + (SB + 1) * (n - 1) * (Ro + 1) + FL: fail(cnt, "BR", name, a, b)
        STAT["maxSB"] = max(STAT["maxSB"], SB)


def blocked_before(st, g, W, Iset, y, z, p, k):
    for t in range(p, k + 1):
        if z != st[t]["s"][y] and gt(g, W[t][z], W[t][st[t]["s"][y]]) and (y, z) not in Iset[t]: return True
    return False


def main(a):
    import core_probe as CP
    cnt = Counter()
    def do(g, name, extra=None):
        if os.environ.get("STARTF"): extra = CP.parse_start(g, os.environ["STARTF"])
        starts = ([extra] if extra and not os.environ.get("NOSTART") else []) + ([] if os.environ.get("ONLYSTART") and extra else [RE.best_reward_start(g)])
        for s0 in starts:
            try: analyse(cnt, g, s0, name)
            except RuntimeError: cnt["maxit"] += 1
    if a[0] == "rand":
        import dual_probe as D
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
    for k in sorted(STAT): print("STAT", k, STAT[k])
    print("VIOLATIONS", sum(v for k, v in cnt.items() if k.endswith("_V")))
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
