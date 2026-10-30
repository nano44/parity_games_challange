#!/usr/bin/env python3
"""REFEREE successor 20: own control for packet P-N5-SRC (delta on P-N5-SETTLE), adapted from settle_probe.py:
SOURCES S_k = D_k u D_(k+1) u C; SOURCE EVENT = Xi changes on S_k. BLK: block <= (n-1) + m_C; SJ for Even y not in C; T0/T1 Lemma TAIL;
CYC: Case-2 sub-case counter (switched y not in C, b in H_(k-1)(y), y on c's sigma_k-cycle) for the exposition gap in [SET] Case 2.
Original header: own control for packet P-N5-SETTLE (L-SI box 52, l-si 6a70a520, sha1 aef403c3). Own engine rl_engine; no lane code.
Per W-run F (RESULTS R89; tau, C = {v : lambda_W(v) = v} fixed):
  U_k = {sbar_k(g) : g Odd, sbar_k(g) != tau(g)} u {Xi-successor of c : c in C}; EVENT (i) sbar changes, (ii) sigma changes at Even c in C,
  (iii) Xi changes at a vertex of U_k u U_{k+1}.
  BLK   every maximal event-free block has <= n - 1 transitions (RUN-SETTLE); SJ / XJ the fronts l_{k+1} >= j + 1 (S_j, X_j)
  PC    PLAY-CAUSE: each Xi-change at an event-free transition has a switched Even y not in C on x's (sigma_{k+1}, tau)-path
  RC    RUN-COUNT |F| <= n(E_F + 1) - 1;  HR  HEAD-RED's E_F <= sum SB + sum CN + sum HXU
  TI    sigma_{k+1}(v) is W_{k+1}-tight in H_k(v) for Even v not in C (Claim RG' consequence)
  IDX   c odd: sigma_{k+1}(v) = smallest-index tight edge of H_k(v) (IDX-MONO); LEX  c even: argmin key_{sigma_{k+1}} (LEX-BFS)
MUT: 1 block bound n - 2; 2 IDX with the largest index; 3 drop event (iii); 4 LEX with argmax; 5 fronts j + 2 (tightness control).
Usage: settle_probe.py FILES... | rand N lo hi seed   (env MUT, MAXN, NOSTART, ONLYSTART, STARTF)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
MUT = int(os.environ.get("MUT", "0"))
EX = []; STAT = Counter()


def fail(cnt, tag, *a):
    cnt[tag + "_V"] += 1
    if len(EX) < 40: EX.append((tag,) + a)


def nxs(g, s, t): return [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]


def path(nx, x, C):
    p = [x]
    while p[-1] not in C: p.append(nx[p[-1]])
    return p


def analyse(cnt, g, start, name):
    st = RE.run(g, start); n = g.n; T = len(st) - 1
    Ev = [v for v in range(n) if g.owner[v] == 0]; Od = [v for v in range(n) if g.owner[v] == 1]
    W = [[RE.play_value(g, nxs(g, s["s"], s["t"]), v) for v in range(n)] for s in st]
    Xi = [s["Xi"] for s in st]
    # W-runs
    runs, a = [], 0
    for k in range(T):
        if st[k]["t"] != st[k + 1]["t"] or st[k]["fb"] or [x[0] for x in W[k]] != [x[0] for x in W[k + 1]]: runs.append((a, k)); a = k + 1
    runs.append((a, T))
    for (a, b) in runs:
        if b == a: continue
        cnt["wruns"] += 1; cnt["trans"] += b - a
        tau = st[a]["t"]; C = {v for v in range(n) if W[a][v][0] == v}
        def U(k):
            s, sb = st[k]["s"], st[k]["sb"]
            u = {sb[o] for o in Od if sb[o] != tau[o]}
            for c in C: u.add(s[c] if g.owner[c] == 0 else sb[c])
            return u
        Dk = [{o for o in Od if st[k]["sb"][o] != tau[o]} for k in range(a, b + 1)]
        mC = sum(len(g.succ[c]) - 1 for c in C if g.owner[c] == 0)
        ev = []; HXS = Counter(); conly = []
        for k in range(a, b):
            S = Dk[k - a] | Dk[k + 1 - a] | C
            hx = [v for v in S if Xi[k][v] != Xi[k + 1][v]]
            for v in hx: HXS[v] += 1
            ev.append(bool(hx))
            sw = [y for y in Ev if st[k]["s"][y] != st[k + 1]["s"][y]]
            conly.append(all(y in C for y in sw))
        EF = sum(ev)
        if b - a > EF + (EF + 1) * (n - 1 + mC): fail(cnt, "RC", name, a, b)
        if EF > sum(HXS.values()): fail(cnt, "HR", name, a, b)
        k = a
        while k < b:
            if ev[k - a]: k += 1; continue
            k0 = k
            while k < b and not ev[k - a]: k += 1
            L = k - k0; STAT["maxblock"] = max(STAT["maxblock"], L)
            if L > (n - 1) + mC - (1 if MUT == 1 else 0): fail(cnt, "BLK", name, k0, k, n, mC)
            seen_c = False; tail = 0
            for kk in range(k0, k):
                if conly[kk - a]: seen_c = True; tail += 1
                elif seen_c: fail(cnt, "T1", name, kk)
                if conly[kk - a]:
                    if Xi[kk] != Xi[kk + 1] or W[kk] != W[kk + 1]: fail(cnt, "T0", name, kk)
                j = kk - k0; nx1 = nxs(g, st[kk + 1]["s"], tau)
                ell = [W[kk + 1][v][2] for v in range(n)]
                sw = [y for y in Ev if st[kk]["s"][y] != st[kk + 1]["s"][y] and y not in C]
                for y in sw:
                    if ell[y] < j + (2 if MUT == 5 else 1): fail(cnt, "SJ", name, kk, y, j)
                    if kk > a:
                        bb = st[kk + 1]["s"][y]; Hm = {st[kk - 1]["s"][y]} | {w for (x, w) in st[kk - 1]["Is"] if x == y}
                        if bb in Hm:
                            pre, cyc = RE.lasso(nxs(g, st[kk]["s"], tau), y)
                            if y in cyc:
                                cnt["CYC_case2"] += 1
                                if W[kk][bb][1]: cnt["CYC_case2_Pb"] += 1
                for x in range(n):
                    if Xi[kk][x] != Xi[kk + 1][x]:
                        if ell[x] < j + 1: fail(cnt, "XJ", name, kk, x, j)
                        p = path(nx1, x, C)
                        if not any(y in sw for y in p[:-1]): fail(cnt, "PC", name, kk, x)
                        cnt["PC_chk"] += 1
            STAT["maxtail"] = max(STAT["maxtail"], tail)
        # choice rules at every transition of F
        for k in range(a, b):
            I = set(st[k]["Is"]); s1 = st[k + 1]["s"]; nx1 = nxs(g, s1, tau); W1 = W[k + 1]
            for v in Ev:
                if v in C: continue
                Hk = sorted({st[k]["s"][v]} | {w for (x, w) in I if x == v})
                tight = [z for z in Hk if g.ext(v, W1[z]) == W1[v] and z != v]
                if s1[v] not in tight: fail(cnt, "TI", name, k, v); continue
                c = W1[v][0]
                if g.prio[c] % 2 == 1:
                    want = max(tight) if MUT == 2 else min(tight)
                    if s1[v] != want: fail(cnt, "IDX", name, k, v, s1[v], tight)
                    cnt["IDX_chk"] += 1
                else:
                    def key(z): return tuple(reversed(path(nx1, z, C)[:-1]))
                    want = (max if MUT == 4 else min)(tight, key=key)
                    if s1[v] != want: fail(cnt, "LEX", name, k, v, s1[v], tight)
                    cnt["LEX_chk"] += 1
                if len(tight) > 1: cnt["multi_tight"] += 1


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
        for p in a:
            if p.endswith(".start"): continue
            try: g = RE.parse(p)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "100")): cnt["skip_big"] += 1; continue
            sp = p[:-3] + ".start"; ex = None
            if os.path.exists(sp):
                try: ex = CP.parse_start(g, sp)
                except Exception: cnt["start_err"] += 1
            cnt["GAMES"] += 1; do(g, os.path.relpath(p), ex)
    for k in sorted(cnt): print(k, cnt[k])
    for k in sorted(STAT): print("STAT", k, STAT[k])
    print("VIOLATIONS", sum(v for k, v in cnt.items() if k.endswith("_V")))
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
