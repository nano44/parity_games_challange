#!/usr/bin/env python3
"""REFEREE successor 19: own control for packet P-N5-WCH (L-NEW box 79, l-new 2ad78f51, sha1 31caa72e).
Own engine rl_engine (SPEC S1-S5 from the text; no lane code); N5-LZC = rl_engine.run with S4a's sigma_new replaced by the keep-rule of §7.1
(built by patching one line of rl_engine.run's source). W[t] = val(sigma_t, tau_t), Wn[t] = val(sigma_{t+1}, tau_t).
  TIE   Lemma TIE (a)/(b) at every S4a step for every switched v with Wn(v) = W(v)
  NB    NEW-BOUND; RW  RET-WCH per return (W(e)-change in [k, u] unless the leave is a TT transition); RUN, REP  Corollaries (R90 REPEATs)
  SZ    SIL-Z (a), (b), (c) at class-S re-entries (R90 (e) classes, smallest anchor); SC  SC-GXC
  GC    GXC-CLOSE, GXC-SPLIT; LM  LEVEL-MON on every pair of Z-states of a segment; DP  DROP-PAID; FB  FBO-R56 / FBO-SPLIT; ZS  ZF-SPLIT
  ONE   WCH-ONE with w := the largest WCH_S(e) of the run
  LZ    (--lzc) LZ-OPT val(sigma', tau) = W*, LZ-STRICT, TIE = TT = 0, no class-S re-entry
MUT: 1 RET-WCH without TT; 2 GXC-SPLIT without TIE; 3 LEVEL-MON across W(v)-changing S4a steps; 4 ZF-SPLIT without DROP; 5 SIL-Z (b) at
  own-Xi-cycle v.   Usage: wch_probe.py [--lzc] FILES... | rand N lo hi seed  (env MUT, MAXN, RANDSTARTS, NOSTART)"""
import sys, os, random, inspect
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
MUT = int(os.environ.get("MUT", "0"))
EX = []
LZ = "--lzc" in sys.argv
LZSTAT = Counter()


def fail(cnt, tag, *a):
    cnt[tag + "_V"] += 1
    if len(EX) < 30: EX.append((tag,) + a)


def keep_rule(g, s, t, ch):
    n = g.n
    star = [ch[v] if g.owner[v] == 0 else None for v in range(n)]
    nx = [star[v] if g.owner[v] == 0 else t[v] for v in range(n)]
    Ws = [RE.play_value(g, nx, v) for v in range(n)]
    out = list(star)
    for v in range(n):
        if g.owner[v] != 0: continue
        d = s[v]
        if Ws[v][2] >= 1 and g.ext(v, Ws[d]) == Ws[v]: out[v] = d
        elif Ws[v] == (v, 0, 0) and Ws[d][0] == v and Ws[d][1] == 0: out[v] = d
    nx2 = [out[v] if g.owner[v] == 0 else t[v] for v in range(n)]
    LZSTAT["LZOPT_chk"] += 1
    if [RE.play_value(g, nx2, v) for v in range(n)] != Ws: LZSTAT["LZOPT_V"] += 1
    return out


src = inspect.getsource(RE.run).replace("sn = [ch[v] if g.owner[v] == 0 else None for v in range(g.n)]", "sn = KEEP(g, s, t, ch)")
ns = dict(RE.__dict__); ns["KEEP"] = keep_rule; exec(src, ns); run_lzc = ns["run"]


def lev(g, x, w):
    if x[0] != w[0]: return 1
    for r in range(g.n - 1, -1, -1):
        if ((x[1] >> r) & 1) != ((w[1] >> r) & 1): return 2 + (g.n - 1 - r)
    return g.n + 2


def analyse(cnt, g, start, name):
    n = g.n; key = g.key
    st = (run_lzc if LZ else RE.run)(g, start); T = len(st) - 1
    cnt["RUNS"] += 1; cnt["TRANS"] += T
    ev = [v for v in range(n) if g.owner[v] == 0]; mE = sum(len(g.succ[v]) for v in ev); nE = len(ev)
    dE = Counter(w for v in ev for w in g.succ[v])
    S = [x["s"] for x in st]; TA = [tuple(x["t"][v] for v in range(n) if g.owner[v] == 1) for x in st]
    nxf = lambda s, t: [s[v] if g.owner[v] == 0 else t[v] for v in range(n)]
    W = [[RE.play_value(g, nxf(S[t], st[t]["t"]), v) for v in range(n)] for t in range(T + 1)]
    Wn = [[RE.play_value(g, nxf(S[t + 1], st[t]["t"]), v) for v in range(n)] for t in range(T)]
    X = [x["Xi"] for x in st]; Is = [set(x["Is"]) for x in st]
    fb = [st[t]["fb"] for t in range(T)]; efb = [fb[t] and bool(Is[t]) for t in range(T)]
    tch = [TA[t + 1] != TA[t] for t in range(T)]
    s4a = [bool(Is[t]) and not fb[t] and S[t + 1] != S[t] for t in range(T)]
    bnd = [efb[t] or tch[t] for t in range(T)]
    lamW = [tuple(w[0] for w in W[t]) for t in range(T + 1)]; lamX = [tuple(x[0] for x in X[t]) for t in range(T + 1)]
    Z = [{v for v in range(n) if X[t][v] != W[t][v]} for t in range(T + 1)]
    inH = lambda t, v, y: S[t][v] == y or (v, y) in Is[t]
    gt = lambda a_, b_: key(a_) > key(b_)
    # ---- Lemma TIE, LZ-STRICT
    tie = set()
    for t in range(T):
        if not s4a[t]: continue
        nxp = nxf(S[t + 1], st[t]["t"])
        for v in ev:
            if S[t + 1][v] == S[t][v]: continue
            if LZ and not gt(Wn[t][v], W[t][v]): fail(cnt, "LZSTRICT", name, t, v)
            if Wn[t][v] != W[t][v]: continue
            if not tch[t]: tie.add((v, t))
            d = S[t][v]; cnt["TIE_chk"] += 1
            if Wn[t][v][0] != v:
                pre, cy = RE.lasso(nxp, d); path = pre + cy[:cy.index(Wn[t][d][0])] if Wn[t][d][0] in cy else pre
                if g.ext(v, Wn[t][d]) != Wn[t][v] or v in path: fail(cnt, "TIEa", name, t, v)
            else:
                if not (Wn[t][d][0] == v and Wn[t][d][1] == 0): fail(cnt, "TIEb", name, t, v)
    if LZ and tie: fail(cnt, "LZTIE", name, len(tie))
    # ---- W-runs: NEW-BOUND, RET-WCH, RUN-WCH, REP-WCH
    wr = []; a = 0
    for t in range(1, T + 2):
        if t == T + 1 or fb[t - 1] or tch[t - 1] or lamW[t] != lamW[t - 1]: wr.append((a, t - 1)); a = t
    blocked = lambda t, y, z: z != S[t][y] and gt(W[t][z], W[t][S[t][y]]) and (y, z) not in Is[t]
    for (a, b) in wr:
        if b == a: continue
        tr = range(a, b); L = b - a
        wch = {e: sum(W[s + 1][e] != W[s][e] for s in tr) for e in range(n)}
        tieF = sum(1 for (v, t) in tie if a <= t < b)
        ret = 0; tt = 0
        for v in ev:
            for e in g.succ[v]:
                rets = [u for u in tr if S[u + 1][v] == e != S[u][v] and any(S[r][v] == e for r in range(a, u + 1))]
                nret_pay = 0; ttv = 0
                for u in rets:
                    k = max(k for k in range(a, u) if S[k][v] == e != S[k + 1][v])
                    if W[k + 1][v] != W[k][v] or MUT == 1:
                        cnt["RW_chk"] += 1
                        if not any(W[s + 1][e] != W[s][e] for s in range(k, u + 1)): fail(cnt, "RW" if MUT != 1 else "RWmut", name, a, v, e, u)
                    else: ttv += 1
                ret += len(rets); tt += ttv
                if len(rets) > wch[e] + ttv and MUT != 1: fail(cnt, "RWN", name, a, v, e)
        cnt["RET"] += ret; cnt["TT"] += tt
        if L > mE + ret: fail(cnt, "NB", name, a)
        if L > mE + sum(dE[e] * wch[e] for e in range(n)) + tieF: fail(cnt, "RUN", name, a)
        late = defaultdict(list)
        for u in tr:
            for y in ev:
                z = S[u + 1][y]
                if z != S[u][y] and any(blocked(t, y, z) for t in range(a, u + 1)): late[(y, z)].append(u)
        rep = sum(len(x) - 1 for x in late.values()); cnt["REP"] += rep
        if rep > sum(dE[e] * wch[e] for e in range(n)) + tieF: fail(cnt, "REP", name, a)
    # ---- lambda-runs: class-S re-entries, SIL-Z, SC-GXC
    pa = [0] * (T + 1); a = 0
    for t in range(T + 1):
        if t > 0 and not (s4a[t - 1] and not tch[t - 1]): a = t
        pa[t] = a
    Wst = lambda u, j: W[u] if u <= j - 1 else Wn[j - 1]
    gxc = set()
    for t in range(T):
        for v in ev:
            if S[t + 1][v] != S[t][v] and not tch[t] and lamX[t + 1] == lamX[t] and v in Z[t] and gt(X[t + 1][v], X[t][v]) and not gt(W[t + 1][v], W[t][v]):
                gxc.add((v, t))
    cnt["GXC"] += len(gxc)
    lruns = []; a = 0
    for t in range(1, T + 2):
        if t == T + 1 or lamX[t] != lamX[a]: lruns.append((a, t - 1)); a = t
    for (ra, rb) in lruns:
        sil = nc = nt = 0
        for v in ev:
            for c in g.succ[v]:
                ent = [t for t in range(ra, rb) if S[t + 1][v] == c and S[t][v] != c]
                lv = [t for t in range(ra, rb) if S[t][v] == c and S[t + 1][v] != c]
                for j1 in ent:
                    j = j1 + 1; prev = [s for s in lv if s < j1]
                    if not prev or efb[j1] or not s4a[j1]: continue
                    s = prev[-1]; a2 = pa[j1]; q = None
                    for qq in range(max(s, a2), j1):
                        if inH(qq, v, c): q = qq + 1; break
                    if q is None: continue
                    if any(Wst(u, j)[v][0] == v for u in range(q, j + 1)): continue
                    if any(Wst(u, j)[c] != Wst(u + 1, j)[c] for u in range(q, j)): continue
                    sil += 1; cnt["SZ_chk"] += 1
                    if LZ: fail(cnt, "LZSIL", name, j1, v, c)
                    d = S[j1][v]
                    if not (W[j1][d] == Wn[j1][d] == Wn[j1][c] == W[j1][c] and Wn[j1][v] == W[j1][v]): fail(cnt, "SZa", name, j1, v, c)
                    ownj1 = X[j1][v][0] == v; ownj = X[j][v][0] == v
                    if not ownj1 or MUT == 5:
                        if not (d in Z[j1] and v in Z[j1]): fail(cnt, "SZb" if not ownj1 else "SZbmut", name, j1, v)
                    if not ownj1 and not ownj and not gt(X[j][v], X[j1][v]): fail(cnt, "SZc", name, j1, v)
                    if ownj1 or ownj: nc += 1
                    elif tch[j1]: nt += 1
                    elif (v, j1) not in gxc: fail(cnt, "SC", name, j1, v)
        cnt["SIL"] += sil; cnt["NC"] += nc; cnt["NT"] += nt
        gxcR = sum(1 for (v, t) in gxc if ra <= t < rb)
        if sil > gxcR + nc + nt: fail(cnt, "SC2", name, ra)
    if LZ: return
    # ---- phases
    phases = []; a = 0
    for t in range(1, T + 2):
        if t == T + 1 or lamX[t] != lamX[a] or TA[t] != TA[a]: phases.append((a, t - 1)); a = t
    for (a, b) in phases:
        tr = range(a, b)
        wchv = {v: sum(1 for k in tr if s4a[k] and W[k + 1][v] != W[k][v]) for v in range(n)}
        sumw = sum(wchv.values())
        fP = sum(efb[k] for k in tr); zf = [k for k in tr if efb[k] and Z[k + 1] == Z[k]]
        gx = [(v, t) for (v, t) in gxc if a <= t < b]
        tieP = [(v, t) for (v, t) in gx if s4a[t]]
        for (v, t) in gx:
            if s4a[t] and (v, t) not in tie: fail(cnt, "GXCTIE", name, t, v)
        cl = [(v, t) for (v, t) in gx if efb[t] and v not in Z[t + 1]]
        fbo = [(v, t) for (v, t) in gx if efb[t] and v in Z[t + 1]]
        cnt["CL"] += len(cl); cnt["FBO"] += len(fbo); cnt["ZF"] += len(zf); cnt["f"] += fP
        if len(cl) > len(Z[a]) + sumw: fail(cnt, "GCL", name, a)
        if len(gx) > (len(tieP) if MUT != 2 else 0) + len(cl) + len(fbo): fail(cnt, "GSP" if MUT != 2 else "GSPmut", name, a)
        # LEVEL-MON / DROP
        drop = defaultdict(set)
        for v in range(n):
            cut = [k for k in tr if s4a[k] and W[k + 1][v] != W[k][v]]
            segs = []; s0 = a
            for k in cut: segs.append((s0, k)); s0 = k + 1
            segs.append((s0, b))
            if MUT == 3: segs = [(a, b)]
            for (x0, x1) in segs:
                zs = [t for t in range(x0, x1 + 1) if v in Z[t]]
                lv = [lev(g, X[t][v], W[t][v]) for t in zs]
                cnt["LM_chk"] += 1
                if any(lv[i] > lv[i + 1] for i in range(len(lv) - 1)): fail(cnt, "LM" if MUT != 3 else "LMmut", name, a, v)
            for k in tr:
                if not (s4a[k] and W[k + 1][v] != W[k][v]) and v in Z[k] and v in Z[k + 1] and lev(g, X[k + 1][v], W[k + 1][v]) > lev(g, X[k][v], W[k][v]):
                    drop[v].add(k)
            if len(drop[v]) > (n + 1) * (1 + wchv[v]): fail(cnt, "DP", name, a, v)
        sdrop = sum(len(x) for x in drop.values())
        fbos = [(v, t) for (v, t) in fbo if lev(g, X[t + 1][v], W[t + 1][v]) == lev(g, X[t][v], W[t][v])]
        if len(fbo) > nE * fP: fail(cnt, "FBR", name, a)
        if len(fbo) > sdrop + len(fbos): fail(cnt, "FBS", name, a)
        nz = zfs = 0
        for k in zf:
            sw = [v for v in ev if S[k + 1][v] != S[k][v]]
            noown = [v for v in sw if X[k][v][0] != v and X[k + 1][v][0] != v]
            if not noown: nz += 1
            elif all(lev(g, X[k + 1][v], W[k + 1][v]) == lev(g, X[k][v], W[k][v]) for v in noown): zfs += 1
            elif MUT != 4 and not any(k in drop[v] for v in noown): fail(cnt, "ZSk", name, k)
        if len(zf) > nz + (sdrop if MUT != 4 else 0) + zfs: fail(cnt, "ZS" if MUT != 4 else "ZSmut", name, a)
        if fP > len(Z[a]) + sum(len(Z[k + 1] - Z[k]) for k in tr if s4a[k]) + len(zf): fail(cnt, "GRED", name, a)
        cnt["NZ"] += nz; cnt["ZFS"] += zfs; cnt["FBOS"] += len(fbos); cnt["DROP"] += sdrop


def main(a):
    import core_probe as CP, dual_probe as D
    a = [x for x in a if x != "--lzc"]
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
    cnt.update(LZSTAT)
    for k in sorted(cnt): print(k, cnt[k])
    print("VIOLATIONS", sum(v for k, v in cnt.items() if k.endswith("_V")))
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
