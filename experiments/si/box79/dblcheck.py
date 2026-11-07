#!/usr/bin/env python3
"""L-SI box 79: machine check of packet P-IDEAL-DBL (docs/si/P-IDEAL-DBL.md). Deterministic, numpy-free.
Simulator: experiments/si/box76/tw.py Sim (own implementation of RESULTS R104's IDEAL model; cross-checked against L-NEW's box150 Gen
on the whole corpus in box 76). Scopes (printed separately):
  CORPUS = the 208 L^R_d genomes of the frozen P-IDEAL-MOVES corpus (box76/corpus_lr.json.gz), every start for N <= 10, the stored
           start otherwise (63,223 runs);
  LOWER  = L-LOWER 3's nine l3/kill genomes (box76/inst/lower/), stored start.
Counters (violations, each must be 0; the unit of each count is printed with it):
  WO    WINDOW-ONCE: (run, level j >= 1, j-window, member) with > 1 move in the window
  HIT   HIT: (run, mover, step) where [cv rises] != [the old chain meets Mv_t]
  ALTa  ALT-MIN (a): (run, degree-2 mover, k) with #{pi changes to k} > R_k
  ALTb  ALT-MIN (b): (run, mover) with PF > 2 min(R_0, R_1) + 1
  ALTc  ALT-MIN (c): (run, mover) with moves > 2 + 2 min(R_0, R_1)
  ALTd  ALT-MIN (d): (run, mover, k) with R_k(x) != R(xt(x, k)) (0 if X)
  DBLa  DBL-EQ (a): (run, level l >= 1) where [F(l) = 2F(l-1) + 2] != [the five conditions]
  DBLb  DBL-EQ (b): (run, doubling level, l-window, member) where the member does not move exactly once in the window
  DBLc  DBL-EQ (c): (run, doubling level) with gamma_l(0) != gamma_l(1), or an l-window whose first mover is not p iff not gamma
  TN    TOWER-NEED: (run, doubling level, member) with P(x) < f + 2, or (f >= 2 and a target X or with R < (f - 1)/2)
  PF    PASS-FREEZE: (run, level l in 1..d-2) with the pair l+1 never moving, split at s_0, and F(l+1) != F(l)
  FU2   FUEL (ii): (run, level l in 0..d-1) with E_l != {t : some mover on the old chain of some y in U_l moves at t}
Controls (must be > 0): ALTb_T, ALTc_T (the bounds minus 1); WO_T (windows where a member moves exactly once);
FU2_T ((run, level) with E_l nonempty); NEG=2 (key-least option ignoring availability) for HIT.
Usage: dblcheck.py   (NEG=2 for the control)"""
import sys, os, json, glob, itertools, collections
H = os.path.dirname(os.path.abspath(__file__)); B76 = os.path.join(H, "..", "box76"); sys.path.insert(0, B76)
from tw import load_corpus, is_lr, Sim, analyse

def run_checks(G, s0, C, I):
    sim = Sim(G); N = G["N"]; d = N // 2; lev = G["lev"]; o = G["opts"]
    S = sim.run(s0); a = analyse(sim, S); T = a["T"]; Mv = a["Mv"]; flip = a["flip"]; c = a["c"]; pi = a["pi"]
    I["runs"] += 1; I["steps"] += T
    V = [[(sim.val(S[t], x, 0), sim.val(S[t], x, 1)) for x in range(N)] for t in range(T + 1)]
    cv = [[V[t][x][S[t][x]] for x in range(N)] for t in range(T + 1)]
    mv = [sum(1 for t in range(1, T + 1) if x in Mv[t]) for x in range(N)]
    F = [sum(1 for t in range(1, T + 1) if flip[t][j]) for j in range(d)]
    def chain(s, y):
        out = [y]; z = o[y][s[y]][1]
        while z >= 0: out.append(z); z = o[z][s[z]][1]
        return out
    rise = [[False] * (T + 1) for _ in range(N)]
    for x in range(N):
        for t in range(1, T + 1):
            rise[x][t] = cv[t][x] > cv[t - 1][x]
            hit = any(z in Mv[t] for z in chain(S[t - 1], x))
            I["HIT units (run, mover, step)"] += 1
            if rise[x][t] != hit: C["HIT"] += 1
    R = [sum(rise[x]) for x in range(N)]
    # ALT-MIN
    for x in range(N):
        Rk = [sum(1 for t in range(1, T + 1) if V[t][x][k] > V[t - 1][x][k]) for k in range(2)]
        Pk = [sum(1 for t in range(1, T + 1) if pi[t][x] != pi[t - 1][x] and pi[t][x] == k) for k in range(2)]
        PF = Pk[0] + Pk[1]; m = min(Rk)
        I["ALT units (run, mover)"] += 1
        for k in range(2):
            C["ALTa"] += Pk[k] > Rk[k]
            y = o[x][k][1]; C["ALTd"] += Rk[k] != (R[y] if y >= 0 else 0)
        C["ALTb"] += PF > 2 * m + 1; C["ALTc"] += mv[x] > 2 + 2 * m
        C["ALTb_T"] += PF > 2 * m; C["ALTc_T"] += mv[x] > 1 + 2 * m
    # path counts
    memo = {}
    def P(x):
        if x < 0: return 1
        if x not in memo: memo[x] = P(o[x][0][1]) + P(o[x][1][1])
        return memo[x]
    for l in range(1, d):
        p, q = 2 * l, 2 * l + 1
        # j-windows of level l
        W = []; t = 1
        while t <= T:
            e = t
            while e + 1 <= T and not flip[e + 1][l - 1]: e += 1
            W.append((t, e)); t = e + 1
        for (t0, e) in W:
            for x in (p, q):
                I["WO units (run, level, window, member)"] += 1
                nm = sum(1 for u in range(t0, e + 1) if x in Mv[u])
                if nm > 1: C["WO"] += 1
                if nm == 1: C["WO_T"] += 1
        Phi = lambda t: sum(1 for x in (p, q) if S[t][x] != c[t][l])
        cond = Phi(0) == 2 and Phi(T) == 0
        for t in range(1, T + 1):
            if flip[t][l - 1] and Phi(t - 1) != 0: cond = False
            if p in Mv[t] and q in Mv[t]: cond = False
            if bool({p, q} & Mv[t]) != flip[t][l]: cond = False
        dbl = F[l] == 2 * F[l - 1] + 2
        I["DBLa units (run, level)"] += 1
        if dbl != cond: C["DBLa"] += 1
        if dbl:
            I["doubling (run, level)"] += 1
            for (t0, e) in W:
                for x in (p, q):
                    I["DBLb units (run, doubling level, window, member)"] += 1
                    if sum(1 for u in range(t0, e + 1) if x in Mv[u]) != 1: C["DBLb"] += 1
            gam = [G["gate"][p][k] < G["gate"][q][k] for k in range(2)]
            bad = gam[0] != gam[1]
            for (t0, e) in W:
                fp = min((u for u in range(t0, e + 1) if p in Mv[u]), default=None)
                fq = min((u for u in range(t0, e + 1) if q in Mv[u]), default=None)
                if fp is None or fq is None or (fp < fq) != (not gam[0]): bad = True
            C["DBLc"] += bad
            f = F[l - 1]
            for x in (p, q):
                I["TN units (run, doubling level, member)"] += 1
                ok = P(x) >= f + 2
                if f >= 2:
                    for k in range(2):
                        y = o[x][k][1]
                        if y < 0 or 2 * R[y] < f - 1: ok = False
                C["TN"] += not ok
        if l <= d - 2:
            r, w = 2 * l + 2, 2 * l + 3
            if mv[r] == 0 and mv[w] == 0 and S[0][r] != S[0][w]:
                I["PF units (run, level) frozen split"] += 1
                if F[l + 1] != F[l]: C["PF"] += 1
    # FUEL (ii)
    for l in range(d):
        U = sorted({o[x][k][1] for x in range(N) for k in range(2) if lev[x] <= l and o[x][k][1] >= 0 and lev[o[x][k][1]] > lev[x]})
        E = {t for t in range(1, T + 1) if any(cv[t][y] != cv[t - 1][y] for y in U)}
        Hh = {t for t in range(1, T + 1) if any(z in Mv[t] for y in U for z in chain(S[t - 1], y))}
        I["FU2 units (run, level)"] += 1
        if E != Hh: C["FU2"] += 1
        if E: C["FU2_T"] += 1

def main():
    for scope in ("CORPUS", "LOWER"):
        C = collections.Counter({k: 0 for k in ("WO", "HIT", "ALTa", "ALTb", "ALTc", "ALTd", "DBLa", "DBLb", "DBLc", "TN", "PF", "FU2", "ALTb_T", "ALTc_T", "WO_T", "FU2_T")})
        I = collections.Counter()
        if scope == "CORPUS":
            items = [(p, G, s0) for p, G in load_corpus() if is_lr(G)
                     for s0 in (itertools.product((0, 1), repeat=G["N"]) if G["N"] <= 10 else [tuple(G["start"])])]
        else:
            items = [(p, json.load(open(p)), None) for p in sorted(glob.glob(os.path.join(B76, "inst", "lower", "*.json")))]
        for p, G, s0 in items:
            run_checks(G, tuple(s0) if s0 is not None else tuple(G["start"]), C, I)
        print("%s violations: %s" % (scope, " ".join("%s %d" % (k, C[k]) for k in C if not k.endswith("_T"))))
        print("%s controls (must be > 0): ALTb_T %d ALTc_T %d WO_T %d FU2_T %d" % (scope, C["ALTb_T"], C["ALTc_T"], C["WO_T"], C["FU2_T"]))
        print("%s units: %s" % (scope, "; ".join("%s %d" % kv for kv in sorted(I.items()))))

if __name__ == "__main__":
    main()
