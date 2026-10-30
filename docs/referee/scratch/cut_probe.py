#!/usr/bin/env python3
"""REFEREE successor 19: own control for packet P-N5-CUT (L-SI box 43, l-si 2678f6c6, sha1 d6519d3d).
Own engine rl_engine (SPEC S1-S5 from the text; no lane code). Per N5 run, with W[t] := val(sigma_t, tau_t) and
Wn[t] := val(sigma_{t+1}, tau_t) (the frame of the old tau):
  OPT1   OPT-OFF (i) against one-edge deviations inside H_t (sigma' with v -> y, (v, y) in H_t), every x
  OPT2   OPT-OFF (ii): v off-cycle in Wn[t], (v, y) in H_t  =>  Wn[t](y) <= Wn[t](sigma_{t+1} v)
  WMON   W-MON': Wn[t] >= W[t] pointwise at every S4a step (counted separately at tau-changing ones: WMONX)
  CLS    re-entries per lambda-run: classes F / FR / C / P / S with the smallest anchor; S must be W-silent (W-RETURN-G);
         CUT-CHARGE  ENT <= 1 + FC + WCH* + SIL + CYC and FC <= B_R per pair and lambda-run; Remark #FR <= 1 per tau*-piece and pair
  FS     FRESH-SPLIT: (LATE) re-entries have (v, c) BLOCKED at j - 2
  LS     LATE-SPLIT on W-runs: (ii) off-cycle on [k+1, u2+1] => W(z) changes on [k+1, u2+1] or W-silent; (iii) strict rise before t
  WV     WV-R per guided stretch Q: WCH_Q(w) <= L + (L + 1)(n - 1)(R*_Q + 1), L = lambda_W changes in Q <= n(n - 1); R*_T <= m_E + REP_F
  THM    Theorem CUT-RED: T <= 2n(n-1) + (n(n-1)+1)(m_E[1 + 2B* + (B*+1)K] + SC* + O*); also the bookkeeping E*, O* step
MUT (each must bite somewhere): 1 OPT2 without the off-cycle premise; 2 anchors allowed before the piece (q - 1 < a, across a cut);
  3 LATE-SPLIT (ii) without the off-cycle premise; 4 CUT-CHARGE with FC := #F only (FR re-entries uncharged);
  5 W-MON' in the NEW frame tau_{t+1} at tau-changing S4a steps.
Usage: cut_probe.py rand N lo hi seed | FILES...  (env MUT, MAXN, RANDSTARTS, NOSTART=1: S3 start only)"""
import sys, os, random
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
MUT = int(os.environ.get("MUT", "0"))
EX = []


def fail(cnt, tag, *a):
    cnt[tag + "_V"] += 1
    if len(EX) < 30: EX.append((tag,) + a)


def runs_of(keys):
    """maximal runs of equal keys -> list of (a, b)"""
    out, a = [], 0
    for t in range(1, len(keys) + 1):
        if t == len(keys) or keys[t] != keys[a]: out.append((a, t - 1)); a = t
    return out


def analyse(cnt, g, start, name):
    n = g.n; key = g.key; st = RE.run(g, start); T = len(st) - 1
    cnt["RUNS"] += 1; cnt["TRANS"] += T
    ev = [v for v in range(n) if g.owner[v] == 0]; mE = sum(len(g.succ[v]) for v in ev)
    S = [x["s"] for x in st]; TA = [tuple(x["t"][v] for v in range(n) if g.owner[v] == 1) for x in st]
    nx = lambda s, t: [s[v] if g.owner[v] == 0 else t[v] for v in range(n)]
    W = [[RE.play_value(g, nx(S[t], st[t]["t"]), v) for v in range(n)] for t in range(T + 1)]
    Wn = [[RE.play_value(g, nx(S[t + 1], st[t]["t"]), v) for v in range(n)] for t in range(T)]
    Is = [set(x["Is"]) for x in st]
    fb = [st[t]["fb"] for t in range(T)]
    efb = [fb[t] and bool(Is[t]) for t in range(T)]
    tch = [TA[t + 1] != TA[t] for t in range(T)]
    s4a = [bool(Is[t]) and not fb[t] and S[t + 1] != S[t] for t in range(T)]
    bnd = [efb[t] or tch[t] for t in range(T)]
    for t in range(T):   # Fact B
        if not (s4a[t] or bnd[t]): fail(cnt, "FACTB", name, t)
    inH = lambda t, v, y: S[t][v] == y or (v, y) in Is[t]
    # tau*-pieces (guided stretches): maximal runs, tau constant, every inner transition an S4a step
    piece = [0] * (T + 1); pa = [0] * (T + 1); pieces = []; a = 0
    for t in range(T + 1):
        if t > 0 and not (s4a[t - 1] and not tch[t - 1]): pieces.append((a, t - 1)); a = t
        pa[t] = a
    pieces.append((a, T))
    for i, (a, b) in enumerate(pieces):
        for t in range(a, b + 1): piece[t] = i
    # --- OPT-OFF, W-MON'
    for t in range(T):
        if not s4a[t]: continue
        for x in range(n):
            cnt["WMON_chk"] += 1
            if key(Wn[t][x]) < key(W[t][x]): fail(cnt, "WMON", name, t, x)
        if tch[t]:
            cnt["WMONX_chk"] += 1
            if MUT == 5:
                Wnew = [RE.play_value(g, nx(S[t + 1], st[t + 1]["t"]), v) for v in range(n)]
                Wold = [RE.play_value(g, nx(S[t], st[t + 1]["t"]), v) for v in range(n)]
                if any(key(Wnew[x]) < key(Wold[x]) for x in range(n)): fail(cnt, "WMON5", name, t)
        base = nx(S[t + 1], st[t]["t"])
        for v in ev:
            ys = [y for y in g.succ[v] if inH(t, v, y)]
            for y in ys:
                if y != S[t + 1][v] and len(EX) < 1000 and cnt["OPT1_chk"] < 400000:
                    alt = list(base); alt[v] = y
                    cnt["OPT1_chk"] += 1
                    for x in range(n):
                        if key(RE.play_value(g, alt, x)) > key(Wn[t][x]): fail(cnt, "OPT1", name, t, v, y, x); break
                off = Wn[t][v][0] != v
                if off or MUT == 1:
                    cnt["OPT2_chk"] += 1
                    if key(Wn[t][y]) > key(Wn[t][S[t + 1][v]]): fail(cnt, "OPT2" if off else "OPT2mut", name, t, v, y)
    # frame-tau* value at state u in [q, j] for a re-entry at j-1 -> j
    def Wst(u, j):
        return W[u] if u <= j - 1 else Wn[j - 1]
    # --- lambda-runs: re-entries
    lam = [tuple(v[0] for v in x["Xi"]) for x in st]
    lamU = [tuple(v[0] for v in x["Ut"]) for x in st]
    Bstar = 0; SCstar = 0; Estar = 0
    for (ra, rb) in runs_of(lam):
        BR = sum(bnd[t] for t in range(ra, rb))
        Bstar = max(Bstar, BR)
        sw = sum(S[t + 1][v] != S[t][v] for t in range(ra, rb) for v in ev); Estar = max(Estar, sw)
        sc = 0; frp = Counter()
        for v in ev:
            for c in g.succ[v]:
                ent = [t for t in range(ra, rb) if S[t + 1][v] == c and S[t][v] != c]
                if not ent: continue
                lv = [t for t in range(ra, rb) if S[t][v] == c and S[t + 1][v] != c]
                cls = Counter(); s_last = None
                for j1 in ent:      # entry at j1 -> j1+1 ; j = j1 + 1
                    j = j1 + 1
                    prev = [s for s in lv if s < j1]
                    if not prev: cls["first"] += 1; continue
                    s = prev[-1]
                    if efb[j1]: cls["F"] += 1; continue
                    assert s4a[j1], "re-entry neither S4a nor Even fallback"
                    a = pa[j1]
                    lo = max(s, a) if MUT != 2 else max(s, ra)
                    q = None
                    for qq in range(lo, j1):        # q - 1 = qq in [max(s, a), j - 2]
                        if inH(qq, v, c): q = qq + 1; break
                    if q is None:
                        cls["FR"] += 1; frp[(piece[j1], v, c)] += 1
                        # FRESH-SPLIT (LATE) check
                        wc = any(key(Wst(u, j)[c]) != key(Wst(u + 1, j)[c]) for u in range(a, j))
                        if not wc and key(Wn[j1][c]) > key(Wn[j1][S[j1][v]]) and j1 > a:
                            offc = Wst(j - 1, j)[v][0] != v and Wst(j, j)[v][0] != v
                            if offc:
                                cnt["FS_LATE"] += 1; u = j1 - 1
                                if not (key(W[u][c]) > key(W[u][S[u][v]]) and (v, c) not in Is[u]): fail(cnt, "FS", name, j1, v, c)
                        continue
                    own = any(Wst(u, j)[v][0] == v for u in range(q, j + 1))
                    wch = any(Wst(u, j)[c] != Wst(u + 1, j)[c] for u in range(q, j))
                    if own: cls["C"] += 1
                    elif wch: cls["P"] += 1
                    else:
                        cls["S"] += 1
                        if Wn[j1][S[j1][v]] != Wn[j1][c]: fail(cnt, "WRETG" if MUT != 2 else "WRETGmut", name, j1, v, c, q)
                f, l = (lv[0], ent[-1]) if lv else (0, -1)
                wstar = sum(Wn[t][c] != W[t][c] for t in range(f, l + 1) if f <= t <= l)  # t -> t+1 inside span [f, l+1]
                FC = cls["F"] + cls["FR"] if MUT != 4 else cls["F"]
                for k, x in cls.items(): cnt["CLS_" + k] += x
                cnt["CC_chk"] += 1
                if len(ent) > 1 + FC + wstar + cls["S"] + cls["C"]: fail(cnt, "CC" if MUT != 4 else "CCmut", name, ra, v, c, dict(cls), wstar)
                if cls["F"] + cls["FR"] > BR: fail(cnt, "FCB", name, ra, v, c)
                sc += cls["S"] + cls["C"]
        for k, x in frp.items():
            if x > 1: fail(cnt, "FRREM", name, k)
        SCstar = max(SCstar, sc)
    Ostar = max(sum(tch[t] for t in range(a, b)) for (a, b) in runs_of(lamU))
    # --- W-runs: inside one tau-stretch, no S4c fallback, lambda_W constant
    lamW = [tuple(w[0] for w in W[t]) for t in range(T + 1)]
    wr = []; a = 0
    for t in range(1, T + 2):
        if t == T + 1 or fb[t - 1] or tch[t - 1] or lamW[t] != lamW[t - 1]: wr.append((a, t - 1)); a = t
    REPstar = 0; Rst = {}
    for (a, b) in wr:
        late = defaultdict(list); RT = 0
        for u in range(a, b):
            hit = False
            for y in ev:
                z = S[u + 1][y]
                if z != S[u][y] and any(key(W[t][z]) > key(W[t][S[t][y]]) and (y, z) not in Is[t] for t in range(a, u + 1)):
                    late[(y, z)].append(u); hit = True
            RT += hit
        rep = sum(len(x) - 1 for x in late.values())
        cnt["LS_late"] += sum(len(x) for x in late.values()); cnt["LS_rep"] += rep
        REPstar = max(REPstar, rep); Rst[(a, b)] = (RT, rep)
        if RT > mE + rep: fail(cnt, "RREP", name, a)
        for (y, z), us in late.items():
            for u1, u2 in zip(us, us[1:]):
                ks = [k for k in range(u1 + 1, u2) if S[k][y] == z and S[k + 1][y] != z]
                if not ks: fail(cnt, "LS_k", name, u1, u2); continue
                k = ks[-1]          # the leave before u2 (any leave works for (ii); take the last)
                off = all(W[x][y][0] != y for x in range(k + 1, u2 + 2))
                if not off and MUT != 3: cnt["LS_cyc"] += 1; continue
                ch = any(W[x][z] != W[x + 1][z] for x in range(k + 1, u2 + 1))
                sil = W[u2 + 1][S[u2][y]] == W[u2 + 1][z]
                cnt["LS_chk"] += 1; cnt["LS_sil"] += sil and not ch
                if not ch and not sil: fail(cnt, "LS2" if off else "LS2mut", name, y, z, u1, u2)
                for t in range(k + 1, u2 + 1):
                    if key(W[t][z]) > key(W[t][S[t][y]]) and (y, z) not in Is[t]:
                        cnt["LS3_chk"] += 1
                        if off and not key(W[t][z]) > key(W[k + 1][z]): fail(cnt, "LS3", name, y, z, t)
                        break
    # --- WV-R per guided stretch
    for (a, b) in pieces:
        if b == a: continue
        L = sum(lamW[t + 1] != lamW[t] for t in range(a, b))
        if L > n * (n - 1): fail(cnt, "LAM", name, a)
        Rq = max([Rst[w][0] for w in wr if a <= w[0] and w[1] <= b] or [0])
        bound = L + (L + 1) * (n - 1) * (Rq + 1)
        for w in range(n):
            wc = sum(W[t + 1][w] != W[t][w] for t in range(a, b))
            cnt["WV_chk"] += 1; cnt["WV_max_ratio_x1000"] = max(cnt["WV_max_ratio_x1000"], 1000 * wc // max(1, bound))
            if wc > bound: fail(cnt, "WV", name, a, w, wc, bound)
        for wa, wb in wr:   # W-runs inside the piece
            if (wa < a <= wb) or (wa <= b < wb): fail(cnt, "WRUN_CROSS", name, a, wa)
    # --- theorem
    nn = n * (n - 1)
    K = nn + (nn + 1) * (n - 1) * (mE + REPstar + 1)
    bound = 2 * nn + (nn + 1) * (mE * (1 + 2 * Bstar + (Bstar + 1) * K) + SCstar + Ostar)
    book = 2 * nn + (nn + 1) * (Estar + Ostar)
    cnt["THM_chk"] += 1
    if T > bound: fail(cnt, "THM", name, T, bound)
    if T > book: fail(cnt, "BOOK", name, T, book)
    for k_, x in (("Bstar", Bstar), ("REPstar", REPstar), ("SCstar", SCstar), ("Ostar", Ostar), ("T", T)):
        cnt["max_" + k_] = max(cnt["max_" + k_], x)


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
