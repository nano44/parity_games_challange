#!/usr/bin/env python3
"""REFEREE succ. 15 probe for P-N5-ROOT-box20 (sha1 d3788bc0) + addendum P-N5-ROOT-add-box20 (sha1 af1c7ad4). Own engine only (rl_engine,
epr_probe.wval for W = (sigma, tau)-play values, flip_probe helpers). No lane code. Per phase ((lambda, tau) const), per class U = U_c:
 BFF    BF-F_D: S4a t->t+1, Even v in U-{c}, v in F_D(t) n F_D(t+1), x in succ(v) n U: M_{t+1}(v) >= wt(v) + M_t(x)
 FRA    FREEZE-A on every piece (cut at fallbacks and A-gains): (a) M_t(z) >= best G[A_t]-path weight with <= t-s edges; (b) M_t <= MoptA_t
        at every t, = MoptA_t and constant after s+L; (c) Odd q, t >= s+L, sigmabar_t(q) in A_t: M_t(q) in V_q, <= deg(q)-1 changes
 RPC    ROOT-PIECE: rho^P_q(A) <= (f+G_c+1)(|U|+deg q-2)+f+G_c and Xi-changes <= (f+G_c+1)(|U|-1)(deg q+1)+f+G_c
 DLS    DL-SPLIT: every entering z of an A-gain is (A) or (B); in (A) with a CLEAN change at u: (i) or (ii) or (iii) (classified)
 GSA    GATE-SHIFT (a) at every state;  GSB  GATE-SHIFT (b) at every S4a transition
 FRG    FREEZE-G on every maximal G-interval: (a) N_t(z) >= best G'[E_t]-path weight with <= t-s edges; (b) N_t <= Mopt' at EVERY t
        (non-vacuous half), freeze after s+L; (c) after s+L; FRGX records max (e-s) - L (> 0 means (b)'s freeze / (c) are exercised)
 FRGC   non-vacuous inner step of FREEZE-G (c) at EVERY t of a G-interval: Odd q in U-{u,c}, sigmabar_t(q) in E_t: M_t(q) = wt(q) + M_t(y)
        for y = sigmabar_t(q) when q in D_t, or q in E_t when q not in D_t
 RLP    RELAY-PIECE on maximal runs (FREEZE-A hypothesis, u in DD, R_u non-increasing): (i) Delta takes <= deg(u) values after s+L_A,
        non-increasing; (ii) counts; RLPX records whether s+L_A <= e - 1 (non-vacuous)
Mutations: MUT=1 FRA (a) and FRG (a) with one more edge; MUT=2 GSB with Delta := 0 (M_{t+1}(z) >= wt(z) + M_t(x));
 MUT=3 BFF without v in F_D(t+1).
Usage: root_probe.py rand N nmin nmax kmax seed | files[:start]...  (env RANDSTARTS 2, MAXN 40, BUDGET 3e5 path extensions per call)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, hon_probe as HP, epr_probe as E
from flip_probe import nxt, on_cycle, class_exit, kap
EX = []
MUT = int(os.environ.get("MUT", "0"))
BUDGET = float(os.environ.get("BUDGET", "3e5"))


class Over(Exception): pass


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def wtv(g, c, v): return g.weight(1 << g.rank[v]) if g.rank[v] > g.rank[c] else 0


def best_paths(g, c, succ, verts, K):
    """best[z][j] = max wt-weight (minus c) of a simple path from z to c in the graph succ restricted to verts, <= j edges, j <= K"""
    vs = set(verts); best = {}; used = [0]
    for z in verts:
        b = [None] * (K + 1); stack = [(z, (z,), 0)]
        while stack:
            v, p, w = stack.pop(); used[0] += 1
            if used[0] > BUDGET: raise Over()
            if v == c:
                L = len(p) - 1
                if b[L] is None or w > b[L]: b[L] = w
                continue
            if len(p) - 1 >= K: continue
            w2 = w + wtv(g, c, v)
            for y in succ[v]:
                if y in vs and y not in p: stack.append((y, p + (y,), w2))
        cur = None; out = []
        for j in range(K + 1):
            if b[j] is not None and (cur is None or b[j] > cur): cur = b[j]
            out.append(cur)
        best[z] = out
    return best


def firstD(g, s, t, Dset, v):
    seen = set(); x = v
    while x not in seen:
        if x in Dset: return x
        seen.add(x); x = s[x] if g.owner[x] == 0 else t[x]
    return None


def route(g, s, t, Dset, v):
    """(sigma, tau)-path from v before its first D vertex"""
    p = []; x = v; seen = set()
    while x not in Dset and x not in seen:
        seen.add(x); p.append(x); x = s[x] if g.owner[x] == 0 else t[x]
    return p


def analyse(g, start, cnt, name):
    st = RE.run(g, start); n = g.n
    Q = {v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1}
    for x in st:
        x["nx"] = nxt(g, x["s"], x["sb"]); x["W"] = E.wval(g, x["s"], x["t"])
        x["D"] = {u for u in Q if x["sb"][u] != x["t"][u]}
        x["fu"] = [firstD(g, x["s"], x["t"], x["D"], v) for v in range(n)]
    K = len(st); k = 0
    while k < K:
        j = k; lam = tuple(v[0] for v in st[k]["Xi"])
        while j + 1 < K and tuple(v[0] for v in st[j + 1]["Xi"]) == lam and st[j + 1]["t"] == st[k]["t"]: j += 1
        phase(g, st, k, j, lam, Q, cnt, name)
        k = j + 1


def phase(g, st, a, b, lam, Q, cnt, name):
    n = g.n; cnt["PHASES"] += 1
    if b == a: return
    tau = st[a]["t"]; f = sum(1 for t in range(a, b) if st[t]["fb"])
    for c in sorted(set(lam)):
        U = {v for v in range(n) if lam[v] == c}
        if len(U) < 2: continue
        cls(g, st, a, b, c, U, Q, tau, f, cnt, name)


def cls(g, st, a, b, c, U, Q, tau, f, cnt, name):
    n = g.n
    M = lambda t, z: g.weight(st[t]["Xi"][z][1])
    def MW(t, z):
        w = st[t]["W"][z]
        return g.weight(w[1]) if w[0] == c else None
    A = {t: {v for v in U if st[t]["fu"][v] is None} for t in range(a, b + 1)}
    s4a = {t: not st[t]["fb"] for t in range(a, b)}
    # ---- BF-F_D
    for t in range(a, b):
        if not s4a[t]: continue
        for v in U:
            if v == c or g.owner[v] != 0 or v not in A[t]: continue
            if MUT != 3 and v not in A[t + 1]: continue
            if MUT == 3 and v in A[t + 1]: continue
            for x in g.succ[v]:
                if x not in U: continue
                cnt["BFF_chk"] += 1
                if M(t + 1, v) < wtv(g, c, v) + M(t, x): fail(cnt, "BFF", name, t, c, v, x)
    # ---- FREEZE-A pieces and ROOT-PIECE
    gains = [t for t in range(a, b) if s4a[t] and not A[t + 1] <= A[t]]
    cuts = sorted(set(gains) | {t for t in range(a, b) if not s4a[t]})
    pieces = []; s = a
    for t in cuts: pieces.append((s, t)); s = t + 1
    pieces.append((s, b))
    succA = lambda At: {v: ([y for y in g.succ[v] if y in At] if g.owner[v] == 0 else ([tau[v]] if tau[v] in At else [])) if v != c else []
                        for v in At}
    oddU = [q for q in U if g.owner[q] == 1]
    for (s, e) in pieces:
        if e < s: continue
        Ls = max(len(A[s]) - 1, 0)
        cnt["FRA_pieces"] += 1
        if e - s > Ls: cnt["FRA_pieces_pastfreeze"] += 1
        try:
            for t in range(s, e + 1):
                At = A[t]
                if c not in At: continue
                bp = best_paths(g, c, succA(At), sorted(At), max(len(At) - 1, 0))
                for z in At:
                    kk = min(t - s + (1 if MUT == 1 else 0), len(At) - 1)
                    lb = bp[z][kk] if kk >= 0 else None
                    cnt["FRA_a_chk"] += 1
                    if lb is not None and M(t, z) < lb: fail(cnt, "FRA_a", name, t, c, z)
                    mo = bp[z][-1]
                    cnt["FRA_b_chk"] += 1
                    if mo is not None and M(t, z) > mo: fail(cnt, "FRA_b", name, t, c, z)
                    if t >= s + Ls and mo is not None and M(t, z) != mo: fail(cnt, "FRA_bfreeze", name, t, c, z)
                    if t >= s + Ls and t > s + Ls and z in A[s + Ls] and M(t, z) != M(s + Ls, z): fail(cnt, "FRA_bconst", name, t, c, z)
        except Over: cnt["FRA_UNK"] += 1
        if s + Ls <= e:
            for q in oddU:
                Vq = {wtv(g, c, q) + M(s + Ls, y) for y in g.succ[q] if y in A[s + Ls]}
                ch = 0
                for t in range(s + Ls, e + 1):
                    if st[t]["sb"][q] not in A[t]: continue
                    cnt["FRA_c_chk"] += 1
                    if M(t, q) not in Vq: fail(cnt, "FRA_c", name, t, c, q)
                    if t < e and st[t + 1]["sb"][q] in A[t + 1] and M(t + 1, q) != M(t, q): ch += 1
                if ch > len(g.succ[q]) - 1: fail(cnt, "FRA_ccount", name, s, c, q, ch)
    Gc = len(gains)
    for q in oddU:
        rho = sum(1 for t in range(a, b) if st[t]["sb"][q] in A[t] and st[t + 1]["sb"][q] in A[t + 1] and M(t, q) != M(t + 1, q))
        xch = sum(1 for t in range(a, b) if st[t]["sb"][q] in A[t] and st[t + 1]["sb"][q] in A[t + 1] and st[t]["Xi"][q] != st[t + 1]["Xi"][q])
        dq = len(g.succ[q]); cnt["RPC_chk"] += 1
        if rho > (f + Gc + 1) * (len(U) + dq - 2) + f + Gc or xch > (f + Gc + 1) * (len(U) - 1) * (dq + 1) + f + Gc: fail(cnt, "RPC", name, a, c, q)
        cnt["MAX_RHOPQ"] = max(cnt["MAX_RHOPQ"], rho)
    # ---- DL-SPLIT
    Qc = sorted((Q & U) - {c}); stop = set(Qc) | {c}
    for t in gains:
        s0, s1 = st[t], st[t + 1]
        for z in A[t + 1] - A[t]:
            cnt["DLS_chk"] += 1
            u = s0["fu"][z]
            if u not in s1["D"]:
                cnt["DLS_A"] += 1
                clean = (not on_cycle(s0["nx"], u) and not on_cycle(s1["nx"], u))
                y1, y2 = s0["sb"][u], s1["sb"][u]
                if clean:
                    pre, cy = RE.lasso(s0["nx"], y2); clean = u not in pre and u not in cy
                if not clean: cnt["DLS_A_nonclean"] += 1; continue
                p1, e1 = class_exit(s0["nx"], y1, stop)
                i_ = e1 is not None and e1 != c and s0["Xi"][e1] != s1["Xi"][e1]
                ii = any(class_exit(s0["nx"], y, stop) != class_exit(s1["nx"], y, stop) for y in g.succ[u] if y in U)
                tog = e1 is not None and e1 != c and u in set(sum(RE.lasso(s1["nx"], e1), []))
                tie = kap(g, s0["Xi"][y2]) == kap(g, s0["Xi"][y1])
                cnt["DLS_i"] += i_; cnt["DLS_ii"] += ii; cnt["DLS_iii_tog"] += tog; cnt["DLS_iii_tie"] += tie
                if not (i_ or ii or tog or tie): fail(cnt, "DLS_A", name, t, c, z, u)
                if not (i_ or ii):
                    cnt["DLS_only_iii"] += 1
                    if cnt["DLS_only_iii_ex"] < 3: cnt["DLS_only_iii_ex"] += 1; EX.append(("ONLY_iii", name, t, c, z, u, tog, tie))
            else:
                cnt["DLS_B"] += 1
                if st[t]["W"][z][0] != lam_of(st, a, z): fail(cnt, "DLS_Bsplit", name, t, c, z)
                rt = route(g, s0["s"], s0["t"], s0["D"], z)
                if not any(g.owner[v] == 0 and s0["s"][v] != s1["s"][v] for v in rt): fail(cnt, "DLS_Bsw", name, t, c, z)
    gates(g, st, a, b, c, U, Q, tau, A, s4a, cnt, name, M, MW)


def lam_of(st, a, z): return st[a]["Xi"][z][0]


def gates(g, st, a, b, c, U, Q, tau, A, s4a, cnt, name, M, MW):
    n = g.n
    def DD(t):
        return {u for u in st[t]["D"] if u in U and st[t]["sb"][u] in A[t] and tau[u] in A[t]}
    DDs = {t: DD(t) for t in range(a, b + 1)}
    Delta = lambda t, u: M(t, tau[u]) - M(t, st[t]["sb"][u])
    Ru = lambda t, u: {z for z in U if st[t]["fu"][z] == u}
    # GATE-SHIFT (a)
    for t in range(a, b + 1):
        for z in U:
            u = st[t]["fu"][z]
            if u is None or u not in DDs[t]: continue
            cnt["GSA_chk"] += 1
            mw = MW(t, z)
            if mw is None or Delta(t, u) < 0 or M(t, z) != mw - Delta(t, u): fail(cnt, "GSA", name, t, c, z, u)
    # GATE-SHIFT (b)
    for t in range(a, b):
        if not s4a[t]: continue
        for z in U:
            if z == c or g.owner[z] != 0: continue
            u = st[t + 1]["fu"][z]
            if u is None or u not in DDs[t + 1]: continue
            for x in g.succ[z]:
                if x not in U: continue
                pre, cy = RE.lasso([st[t]["s"][v] if g.owner[v] == 0 else tau[v] for v in range(n)], x)
                if z in pre or z in cy: continue
                cnt["GSB_chk"] += 1
                mw1 = MW(t + 1, z)
                lhs = M(t + 1, z) if MUT == 2 else mw1
                if lhs is None or lhs < wtv(g, c, z) + M(t, x): fail(cnt, "GSB", name, t, c, z, x)
    # G-intervals and RELAY-PIECE runs
    for u in sorted((Q & U) - {c}):
        if g.owner[u] != 1: continue
        t = a
        while t <= b:
            if u not in DDs[t]: t += 1; continue
            s = t; e = t
            while e < b and s4a[e] and u in DDs[e + 1] and A[e + 1] <= A[e] and Ru(e + 1, u) <= Ru(e, u) and Delta(e + 1, u) == Delta(s, u): e += 1
            frg(g, st, s, e, c, U, u, tau, A, cnt, name, M, MW, Ru, Delta)
            t = e + 1
        t = a
        while t <= b:
            if u not in DDs[t]: t += 1; continue
            s = t; e = t
            while e < b and s4a[e] and u in DDs[e + 1] and A[e + 1] <= A[e] and Ru(e + 1, u) <= Ru(e, u): e += 1
            LA = max(len(A[s]) - 1, 0); cnt["RLP_runs"] += 1
            if s + LA <= e - 1: cnt["RLPX_nonvacuous"] += 1
            if s + LA <= e:
                vals = [Delta(k, u) for k in range(s + LA, e + 1)]
                cnt["RLP_chk"] += 1
                if len(set(vals)) > len(g.succ[u]) or any(vals[i + 1] > vals[i] for i in range(len(vals) - 1)): fail(cnt, "RLP_i", name, s, c, u)
                for q in U:
                    if g.owner[q] != 1 or q in (u, c): continue
                    Ek = lambda k: A[k] | Ru(k, u)
                    chg = sum(1 for k in range(s + LA, e) if st[k]["sb"][q] in Ek(k) and st[k + 1]["sb"][q] in Ek(k + 1) and M(k, q) != M(k + 1, q))
                    cnt["RLP_ii_chk"] += 1; cnt["RLP_ii_maxchg"] = max(cnt["RLP_ii_maxchg"], chg)
                    if chg > len(g.succ[u]) * (len(U) - 1 + len(g.succ[q])): fail(cnt, "RLP_ii", name, s, c, u, q)
            t = e + 1


def frg(g, st, s, e, c, U, u, tau, A, cnt, name, M, MW, Ru, Delta):
    n = g.n; cnt["FRG_intervals"] += 1
    Es = A[s] | Ru(s, u); L = len(Es) - 1
    cnt["FRGX_max_excess"] = max(cnt["FRGX_max_excess"], (e - s) - L + 1000) if cnt["FRGX_max_excess"] else (e - s) - L + 1000
    if e - s > L: cnt["FRGX_pastfreeze"] += 1
    def succE(t):
        At = A[t]; Rt = Ru(t, u); Et = At | Rt; out = {}
        for v in Et:
            if v == c: out[v] = []; continue
            if v in At: tgt = At
            else: tgt = Et
            out[v] = [y for y in g.succ[v] if y in tgt] if g.owner[v] == 0 else ([tau[v]] if tau[v] in tgt else [])
        return Et, out
    try:
        for t in range(s, e + 1):
            Et, sc = succE(t)
            if c not in Et: continue
            bp = best_paths(g, c, sc, sorted(Et), max(len(Et) - 1, 0))
            for z in Et:
                N = MW(t, z)
                if N is None: fail(cnt, "FRG_N", name, t, c, z); continue
                kk = min(t - s + (1 if MUT == 1 else 0), len(Et) - 1)
                cnt["FRG_a_chk"] += 1
                if bp[z][kk] is not None and N < bp[z][kk]: fail(cnt, "FRG_a", name, t, c, u, z)
                cnt["FRG_b_chk"] += 1
                if bp[z][-1] is not None and N > bp[z][-1]: fail(cnt, "FRG_b", name, t, c, u, z)
                if t >= s + L and bp[z][-1] is not None and N != bp[z][-1]: fail(cnt, "FRG_bfreeze", name, t, c, z)
            for q in U:
                if g.owner[q] != 1 or q in (u, c): continue
                y = st[t]["sb"][q]
                if y not in Et: continue
                cnt["FRGC_chk"] += 1
                if q in st[t]["D"]:
                    if M(t, q) != wtv(g, c, q) + M(t, y): fail(cnt, "FRGC", name, t, c, q)
                elif q not in Et: fail(cnt, "FRGC_mem", name, t, c, q)
                if t >= s + L:
                    cnt["FRG_c_chk"] += 1
                    Vq = {wtv(g, c, q) + M(s + L, yy) for yy in g.succ[q] if yy in (A[s + L] | Ru(s + L, u))}
                    if M(t, q) not in Vq: fail(cnt, "FRG_c", name, t, c, q)
    except Over: cnt["FRG_UNK"] += 1


def main(a):
    cnt = Counter(); rng = random.Random(1577); nst = int(os.environ.get("RANDSTARTS", "2"))
    def do(g, name, r, extra=None):
        starts = ([extra] if extra else []) + ([] if (extra and os.environ.get("NOS3")) else [RE.best_reward_start(g)]) + \
                 [D.rand_start(g, r) for _ in range(nst)]
        for j, s0 in enumerate(starts):
            cnt["RUNS"] += 1; analyse(g, s0, cnt, "%s/%d" % (name, j))
    if a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            do(D.rand_ck(r2, nn, r2.randint(0, min(km, nn - 1))), "rand%d" % i, rng)
    else:
        for f in a:
            path, _, sp = f.partition(":")
            try: g = RE.parse(path)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "40")): cnt["skip_big"] += 1; continue
            do(g, os.path.relpath(path), random.Random(os.path.relpath(path)), HP.parse_start(g, sp) if sp else None)
    if cnt["FRGX_max_excess"]: cnt["FRGX_max_excess"] -= 1000
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
