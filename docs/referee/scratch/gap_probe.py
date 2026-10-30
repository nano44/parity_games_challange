#!/usr/bin/env python3
"""REFEREE successor 19: own control for packet P-N5-GAP (L-NEW box 69, l-new 28ceeadc, sha1 d67f8e04).
Own engine rl_engine (SPEC S1-S5 from the text; no lane code). W[t] = val(sigma_t, tau_t), Wn[t] = val(sigma_{t+1}, tau_t), Z_t = {Xi != W}.
  XW     Xi_t <= W_t pointwise
  FBW    W_{k+1} <= W_k at tau-fixed Even fallbacks
  OPT    OPT-OFF (GAP form) with rho = sigma_{t+1} in H_t (S4a steps) and rho = sigma_k in H_k (Even fallbacks): v not own cycle node,
         (v, c) in H: val(c) <= val(rho v).  OPT_2b counts the case the proof's Case 2 misses (c's rho-play meets v's cycle node u before v).
  GMON   GAP-MON; SWIN SW-IN; ZF Z-FLAT (a)-(c); REOP REOPEN-W at in-phase S4a steps; RED Theorem GAP-RED per phase
  LW     LATE-W (leave s -> s+1 in a piece, later blocked state t', off-cycle on [s+1, t']); LP LATE-PIECE per piece and edge
MUT: 1 SW-IN without the own-Xi-cycle exclusion; 2 REOPEN-W at tau-changing S4a steps (W read in the new frame);
  3 GAP-MON at S4a steps; 4 LATE-W without the off-cycle premise; 5 GAP-RED without ZF_P.
Usage: gap_probe.py rand N lo hi seed | FILES...  (env MUT, MAXN, RANDSTARTS, NOSTART)"""
import sys, os, random
from collections import Counter
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
    ev = [v for v in range(n) if g.owner[v] == 0]
    S = [x["s"] for x in st]; TA = [tuple(x["t"][v] for v in range(n) if g.owner[v] == 1) for x in st]
    nx = lambda s, t: [s[v] if g.owner[v] == 0 else t[v] for v in range(n)]
    W = [[RE.play_value(g, nx(S[t], st[t]["t"]), v) for v in range(n)] for t in range(T + 1)]
    Wn = [[RE.play_value(g, nx(S[t + 1], st[t]["t"]), v) for v in range(n)] for t in range(T)]
    X = [x["Xi"] for x in st]; Is = [set(x["Is"]) for x in st]
    fb = [st[t]["fb"] for t in range(T)]; efb = [fb[t] and bool(Is[t]) for t in range(T)]
    tch = [TA[t + 1] != TA[t] for t in range(T)]
    s4a = [bool(Is[t]) and not fb[t] and S[t + 1] != S[t] for t in range(T)]
    Z = [{v for v in range(n) if X[t][v] != W[t][v]} for t in range(T + 1)]
    lamX = [tuple(x[0] for x in X[t]) for t in range(T + 1)]
    inH = lambda t, v, y: S[t][v] == y or (v, y) in Is[t]
    for t in range(T + 1):
        for v in range(n):
            cnt["XW_chk"] += 1
            if key(X[t][v]) > key(W[t][v]): fail(cnt, "XW", name, t, v)
    # OPT-OFF (GAP form)
    for t in range(T):
        if s4a[t]: vals, rho = Wn[t], S[t + 1]
        elif efb[t]: vals, rho = W[t], S[t]
        else: continue
        nxt = nx(rho, st[t]["t"])
        for v in ev:
            u = vals[v][0]
            if u == v: continue
            for c in g.succ[v]:
                if not inH(t, v, c): continue
                cnt["OPT_chk"] += 1
                if key(vals[c]) > key(vals[rho[v]]): fail(cnt, "OPT", name, t, v, c)
                pre, cy = RE.lasso(nxt, c); seq = pre + cy
                if v in seq and u in seq[:seq.index(v)]:
                    cnt["OPT_2b"] += 1
                    pi = seq[:seq.index(v)]
                    if not any(g.rank[y] > g.rank[u] for y in pi[:pi.index(u)]): cnt["OPT_2b_S0"] += 1
    for k in range(T):
        if efb[k]:
            cnt["FB"] += 1
            for v in range(n):
                if key(W[k + 1][v]) > key(W[k][v]): fail(cnt, "FBW", name, k, v)
            if not Z[k + 1] <= Z[k]: fail(cnt, "GMON", name, k)
            for v in range(n):
                if v not in Z[k] and (X[k + 1][v] != X[k][v] or W[k + 1][v] != W[k][v]): fail(cnt, "GMON2", name, k, v)
            for v in ev:
                if S[k + 1][v] != S[k][v]:
                    own = X[k][v][0] == v or X[k + 1][v][0] == v
                    if own and MUT != 1: continue
                    cnt["SWIN_chk"] += 1
                    if not (key(X[k + 1][v]) > key(X[k][v]) and v in Z[k]): fail(cnt, "SWIN" if not own else "SWINmut", name, k, v)
            if Z[k + 1] == Z[k]:
                cnt["ZFLAT"] += 1
                for v in range(n):
                    if (X[k + 1][v] != X[k][v] or W[k + 1][v] != W[k][v]) and v not in Z[k]: fail(cnt, "ZF", name, k, v)
                    if key(X[k + 1][v]) < key(X[k][v]): fail(cnt, "ZFX", name, k, v)
        if s4a[k] and MUT == 3 and not Z[k + 1] <= Z[k]: fail(cnt, "GMONmut", name, k)
    # phases
    a = 0; phases = []
    for t in range(1, T + 2):
        if t == T + 1 or lamX[t] != lamX[a] or TA[t] != TA[a]: phases.append((a, t - 1)); a = t
    for (a, b) in phases:
        f = zf = ro = 0; wch = 0
        for k in range(a, b):
            if efb[k]:
                f += 1; zf += Z[k + 1] == Z[k]
            elif s4a[k]:
                ro += len(Z[k + 1] - Z[k]); wch += sum(W[k + 1][v] != W[k][v] for v in range(n))
                for v in Z[k + 1] - Z[k]:
                    cnt["REOP_chk"] += 1
                    if not key(W[k + 1][v]) > key(W[k][v]): fail(cnt, "REOP", name, k, v)
            else: fail(cnt, "INPHASE", name, k)
        cnt["RED_chk"] += 1; cnt["f_max"] = max(cnt["f_max"], f); cnt["ZF_max"] = max(cnt["ZF_max"], zf)
        rhs = len(Z[a]) + ro + (zf if MUT != 5 else 0)
        if f > rhs: fail(cnt, "RED" if MUT != 5 else "REDmut", name, a, f, len(Z[a]), ro, zf)
        if f > n + wch + zf: fail(cnt, "RED2", name, a)
    if MUT == 2:
        for k in range(T):
            if s4a[k] and tch[k]:
                Wk1 = W[k + 1]
                for v in set(range(n)) - Z[k]:
                    if v in Z[k + 1]:
                        cnt["REOP2_chk"] += 1
                        if not key(Wk1[v]) > key(W[k][v]): fail(cnt, "REOPmut", name, k, v)
    # pieces: LATE-W, LATE-PIECE
    a = 0; pieces = []
    for t in range(1, T + 2):
        if t == T + 1 or not (s4a[t - 1] and not tch[t - 1]): pieces.append((a, t - 1)); a = t
    blocked = lambda t, v, c: c != S[t][v] and key(W[t][c]) > key(W[t][S[t][v]]) and (v, c) not in Is[t]
    for (a, b) in pieces:
        for v in ev:
            for c in g.succ[v]:
                leaves = [s for s in range(a, b) if S[s][v] == c and S[s + 1][v] != c]
                for s in leaves:
                    for tp in range(s + 1, b + 1):
                        if blocked(tp, v, c):
                            off = all(W[x][v][0] != v for x in range(s + 1, tp + 1))
                            if off or MUT == 4:
                                cnt["LW_chk"] += 1
                                if not key(W[tp][c]) > key(W[s + 1][c]): fail(cnt, "LW" if off else "LWmut", name, s, tp, v, c)
                            break
                adopt = [u for u in range(a, b) if S[u + 1][v] == c and S[u][v] != c]
                rb = []; cl = 0
                for u in adopt:
                    if not any(blocked(t, v, c) for t in range(a, u + 1)): continue
                    lv = [s for s in leaves if s + 1 <= u]
                    if not lv: rb.append(u); continue
                    s = lv[-1]; tps = [t for t in range(s + 1, u + 1) if blocked(t, v, c)]
                    if not tps: continue
                    rb.append(u)
                    if len(rb) > 1 and any(W[x][v][0] == v for x in range(s + 1, tps[0] + 1)): cl += 1
                if rb:
                    wc = sum(W[t + 1][c] != W[t][c] for t in range(a, b))
                    cnt["LP_chk"] += 1; cnt["LP_rb"] += len(rb); cnt["LP_max"] = max(cnt["LP_max"], len(rb))
                    if len(rb) > 1 + wc + cl: fail(cnt, "LP", name, a, v, c)


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
