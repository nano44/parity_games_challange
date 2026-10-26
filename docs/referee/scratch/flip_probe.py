#!/usr/bin/env python3
"""REFEREE succ. 14 probe for packet P-N5-FLIP (docs/si/P-N5-FLIP-box18.md, pin d67fdb87, sha1 96a7e088...). Own engine only (rl_engine =
SPEC S1-S5 from the text). No lane code. Per phase ((lambda_Xi, tau) constant) of every N5 run; honest play := (sigma_k, sigma-bar_k); classes
U_c := lambda^{-1}(c); kappa := (signed weight of P, s_c * length), s_c = +1 if c odd; Q := Odd vertices of out-degree >= 2; Q_c := Q n U_c - {c}.
 ADD     additivity (§1): kappa_s(z) = sum kwt(r) + kappa_s(e), r and e's play to c disjoint, for every z in U_c (e = first of Q_c u {c} after z)
 ROOT    in-phase t -> t+1 with all Q-exit paths equal => Xi equal on Reach_t(Q);  ROOT2  every rho-transition switches an Even vertex on a Q-exit path
 RR      ROUTE-RELAY: a RELAY event (q on no honest cycle at t, t+1) has a source;  SF  SELF-FREE: Q_c = {q} => no RELAY
 ROOTC   ROOT-C: all class exit paths of class c equal at t, t+1 => kappa equal on Q_c
 MINW    ROOT-C's proof claim kappa_s(q) = min over Pi_s(q) (walks enumerated, |Q_c| small); REAL counts walks whose 'positional strategy'
         play has a cycle node != c (the proof's sentence "each walk is the play ... with cycle node c" fails there); LOCAL checks the
         repair kappa_s(e) <= kwt(e) + kappa_s(y) for every e in Q_c, y in succ(e) n U_c
 STAT    STATIC: on a rho-free interval sigma-bar is constant on ALL Odd vertices, tau constant, sigma_{k+1} = S4a arena optimum against tau
 FLIP    flips (q1, q2, t1 < t2): FA  (a) kappa_t2(q2) >= kappa_t1(q2) + wt(C); FB (b) p1 intact => sigma-bar' play top w has rew(w) > rew(c);
         FC  (c) intact and disjoint => Z = C, wt(C) > 0, strict rise;  NC  N1 or N2 or N3;  N3L  N3-LEVEL lev >= rank(h)
 MUT=1   control: FA with wt(C) doubled (must fail where wt(C) > 0);  MUT=2 control: N3L with lev > rank(h) (strict; equality occurs)
Usage: flip_probe.py rand N nmin nmax kmax seed | files[:start]...   (env RANDSTARTS default 2, MAXN 64, WALKMAX 7 (|Q_c| for MINW))"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, epr_probe as E, hon_probe as HP
EX = []
MUT = int(os.environ.get("MUT", "0"))


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def nxt(g, s, sb):
    return [s[v] if g.owner[v] == 0 else (sb[v] if sb[v] is not None else g.succ[v][0]) for v in range(g.n)]


def sc(g, c): return 1 if g.prio[c] % 2 else -1


def kap(g, val):
    c, m, d = val
    return (g.weight(m), sc(g, c) * d)


def kwt(g, c, v):
    return ((1 << g.rank[v]) * (1 if g.prio[v] % 2 == 0 else -1) if g.rank[v] > g.rank[c] else 0, sc(g, c))


def add(a, b): return (a[0] + b[0], a[1] + b[1])


def on_cycle(nx, v):
    x = nx[v]; seen = set()
    while x not in seen:
        if x == v: return True
        seen.add(x); x = nx[x]
    return False


def class_exit(nx, y, stopset):
    """y's honest play up to the first vertex of stopset: (path before it, exit)"""
    p = []; x = y; seen = set()
    while x not in stopset:
        if x in seen: return p, None
        seen.add(x); p.append(x); x = nx[x]
    return p, x


def qexit(g, s, Q, q, y):
    p = [y]; x = y; seen = {y}
    while x not in Q:
        x = s[x] if g.owner[x] == 0 else g.succ[x][0]
        p.append(x)
        if x in seen: break
        seen.add(x)
    return tuple(p)


def play_top(g, nx, v):
    pre, cyc = RE.lasso(nx, v)
    return max(cyc, key=lambda u: g.rank[u])


def analyse(g, start, cnt, name):
    st = RE.run(g, start)
    n = g.n
    Q = {v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1}
    for x in st: x["nx"] = nxt(g, x["s"], x["sb"])
    K = len(st); k = 0
    while k < K:
        j = k
        lam = tuple(v[0] for v in st[k]["Xi"])
        while j + 1 < K and tuple(v[0] for v in st[j + 1]["Xi"]) == lam and st[j + 1]["t"] == st[k]["t"]: j += 1
        phase(g, st, k, j, lam, Q, cnt, name)
        k = j + 1


def phase(g, st, a, b, lam, Q, cnt, name):
    n = g.n; cnt["PHASES"] += 1
    C = sorted({lam[v] for v in range(n)})
    U = {c: {v for v in range(n) if lam[v] == c} for c in C}
    Qc = {c: sorted((Q & U[c]) - {c}) for c in C}
    # additivity at every state
    for k in range(a, b + 1):
        nx = st[k]["nx"]; Xi = st[k]["Xi"]
        for c in C:
            stop = set(Qc[c]) | {c}
            for z in U[c]:
                if z in stop: continue
                r, e = class_exit(nx, z, stop)
                cnt["ADD_chk"] += 1
                if e is None: fail(cnt, "ADD", name, k, z, "no exit"); continue
                tot = kap(g, Xi[e])
                for v in r: tot = add(tot, kwt(g, c, v))
                if tot != kap(g, Xi[z]): fail(cnt, "ADD", name, k, z)
    # repair of ROOT-C (LOCAL) and the min-over-walks claim (MINW, REAL), per state
    for k in range(a, b + 1):
        nx = st[k]["nx"]; Xi = st[k]["Xi"]; s = st[k]["s"]
        for c in C:
            stop = set(Qc[c]) | {c}
            ce = {}
            for e in Qc[c]:
                for y in g.succ[e]:
                    if y in U[c]: ce[(e, y)] = class_exit(nx, y, stop)
            for (e, y), (p, ex) in ce.items():
                cnt["LOCAL_chk"] += 1
                if kap(g, Xi[e]) > add(kwt(g, c, e), kap(g, Xi[y])): fail(cnt, "LOCAL", name, k, e, y)
            if not Qc[c] or len(Qc[c]) > int(os.environ.get("WALKMAX", "7")): continue
            for q in Qc[c]:
                best = None; nreal = 0; nw = 0
                stack = [(q, (q,), {}, (0, 0))]
                while stack:
                    e, used, choice, w = stack.pop()
                    if e == c:
                        nw += 1
                        if best is None or w < best: best = w
                        # realise: Odd strategy choice at the e_i, sigma-bar elsewhere
                        nx2 = list(nx)
                        for x, yy in choice.items(): nx2[x] = yy
                        pre, cyc = RE.lasso(nx2, q)
                        top = max(cyc, key=lambda u: g.rank[u])
                        if top != c:
                            nreal += 1
                            if g.rew[top] <= g.rew[c]: fail(cnt, "REALSIGN", name, k, q)
                        continue
                    for y in g.succ[e]:
                        if (e, y) not in ce: continue
                        p, ex = ce[(e, y)]
                        if ex is None or (ex != c and ex in used): continue
                        w2 = add(w, kwt(g, c, e))
                        for v in p: w2 = add(w2, kwt(g, c, v))
                        ch = dict(choice); ch[e] = y
                        stack.append((ex, used + (ex,), ch, w2))
                cnt["MINW_chk"] += 1; cnt["MINW_walks"] += nw; cnt["REAL_nonc"] += nreal
                if nreal and len(EX) < 40 and cnt["REAL_ex"] < 3: cnt["REAL_ex"] += 1; EX.append(("REAL_nonc", name, k, c, q, nreal))
                if best != kap(g, Xi[q]): fail(cnt, "MINW", name, k, q, best, kap(g, Xi[q]))
    # transitions
    for t in range(a, b):
        s0, s1 = st[t], st[t + 1]
        rho = [q for q in Q if s0["Xi"][q] != s1["Xi"][q]]
        cnt["TRANS"] += 1; cnt["RHO_TRANS"] += bool(rho)
        ex0 = {(q, y): qexit(g, s0["s"], Q, q, y) for q in Q for y in g.succ[q]}
        ex1 = {(q, y): qexit(g, s1["s"], Q, q, y) for q in Q for y in g.succ[q]}
        if ex0 == ex1:
            reach = set(Q) | {v for p in ex0.values() for v in p}
            cnt["ROOT_chk"] += 1
            if any(s0["Xi"][v] != s1["Xi"][v] for v in reach): fail(cnt, "ROOT", name, t)
        if rho:
            sw = {v for v in range(n) if g.owner[v] == 0 and s0["s"][v] != s1["s"][v]}
            onp = {v for p in ex0.values() for v in p[:-1]}
            cnt["ROOT2_chk"] += 1
            if not (sw & onp): fail(cnt, "ROOT2", name, t)
        for c in C:
            stop = set(Qc[c]) | {c}
            cp0 = {(q, y): class_exit(s0["nx"], y, stop) for q in Qc[c] for y in g.succ[q] if y in U[c]}
            cp1 = {(q, y): class_exit(s1["nx"], y, stop) for q in Qc[c] for y in g.succ[q] if y in U[c]}
            if Qc[c] and cp0 != cp1 and all(cp0[key][0] == cp1[key][0] for key in cp0):
                # ROOT-C read literally: class exit PATHS (the part strictly before the exit) equal, some exit differs
                cnt["ROOTC_LIT_chk"] += 1
                if any(kap(g, s0["Xi"][q]) != kap(g, s1["Xi"][q]) for q in Qc[c]):
                    cnt["ROOTC_LIT_viol"] += 1
                    if cnt["ROOTC_LIT_viol"] <= 3: EX.append(("ROOTC_LIT", name, t, c, [(key, cp0[key], cp1[key]) for key in cp0 if cp0[key] != cp1[key]][:2]))
            if cp0 == cp1 and Qc[c]:
                cnt["ROOTC_chk"] += 1
                if any(kap(g, s0["Xi"][q]) != kap(g, s1["Xi"][q]) for q in Qc[c]): fail(cnt, "ROOTC", name, t, c)
            for q in Qc[c]:
                if s0["Xi"][q] == s1["Xi"][q]: continue
                if on_cycle(s0["nx"], q) or on_cycle(s1["nx"], q): cnt["RHO_oncycle"] += 1; continue
                ys = [y for y in g.succ[q] if y in U[c]]
                route = any(cp0[(q, y)] != cp1[(q, y)] for y in ys)
                cnt["ROUTE" if route else "RELAY"] += 1
                if len(Qc[c]) == 1:
                    cnt["SF_chk"] += 1
                    if not route: fail(cnt, "SF", name, t, q)
                if route: continue
                cnt["RR_chk"] += 1
                src = False
                for y in ys:
                    e = cp0[(q, y)][1]
                    if e in (q, c) or e is None: continue
                    if kap(g, s0["Xi"][e]) != kap(g, s1["Xi"][e]): src = True
                    if (q not in RE.lasso(s0["nx"], e)[0] + RE.lasso(s0["nx"], e)[1]) != (q not in RE.lasso(s1["nx"], e)[0] + RE.lasso(s1["nx"], e)[1]): src = True
                if not src: fail(cnt, "RR", name, t, q)
    # STATIC on rho-free intervals
    k = a
    while k < b:
        if st[k]["fb"]: k += 1; continue
        x = k
        while k < b and not st[k]["fb"] and all(st[k + 1]["Xi"][q] == st[x]["Xi"][q] and st[k + 1]["sb"][q] == st[x]["sb"][q] for q in Q): k += 1
        if k == x: k += 1; continue
        cnt["STAT_chk"] += 1
        for z in range(x, k + 1):
            if any(st[z]["sb"][v] != st[x]["sb"][v] for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) == 1 and st[z]["sb"][v] is not None and st[x]["sb"][v] is not None): fail(cnt, "STAT", name, z, "forced")
            if st[z]["t"] != st[x]["t"]: fail(cnt, "STAT", name, z, "tau")
        for z in range(x, k):
            Is = st[z]["Is"]; s = st[z]["s"]; t = st[z]["t"]
            A = {v: {s[v]} for v in range(n) if g.owner[v] == 0}
            for v, w in Is: A[v].add(w)
            sn = st[z + 1]["s"]
            Wn = E.wval(g, sn, t)
            # sigma_{z+1} pointwise optimal in the arena against tau: no arena edge improves W (one-player optimality, (F1) contrapositive check)
            for v in A:
                for w in A[v]:
                    if g.key(Wn[w]) > g.key(Wn[sn[v]]) and not on_cycle([sn[u] if g.owner[u] == 0 else t[u] for u in range(n)], v): fail(cnt, "STAT", name, z, "arena")
    # FLIPS
    for c in C:
        stop = set(Qc[c]) | {c}
        par = {}
        for k in range(a, b + 1):
            nx = st[k]["nx"]
            for q in Qc[c]:
                p, ex = class_exit(nx, nx[q], stop)
                if ex in Qc[c] and ex != q: par[(k, q)] = (ex, tuple(p))
        for (t1, q1), (q2, p1) in par.items():
            for t2 in range(t1 + 1, b + 1):
                if par.get((t2, q2), (None,))[0] != q1: continue
                p2 = par[(t2, q2)][1]
                cnt["FLIPS"] += 1
                Cw = [q1] + list(p1) + [q2] + list(p2)
                wC = (0, 0)
                for v in Cw: wC = add(wC, kwt(g, c, v))
                k1 = kap(g, st[t1]["Xi"][q2]); k2 = kap(g, st[t2]["Xi"][q2])
                need = add(k1, wC) if MUT != 1 else add(add(k1, wC), wC)
                if k2 < need: fail(cnt, "FA", name, t1, t2, q1, q2)
                nx1, nx2 = st[t1]["nx"], st[t2]["nx"]
                intact1 = all(nx1[v] == nx2[v] for v in p1)
                intact2 = all(nx1[v] == nx2[v] for v in p2)
                disj = not (set(p1) & set(p2))
                y1 = nx1[q1]
                if intact1:
                    cnt["FB_chk"] += 1
                    nxp = list(nx2); nxp[q1] = y1
                    pre, cyc = RE.lasso(nxp, q1)
                    w = max(cyc, key=lambda u: g.rank[u])
                    if not g.rew[w] > g.rew[c]: fail(cnt, "FB", name, t1, t2)
                    if disj:
                        cnt["FC_chk"] += 1
                        if set(cyc) != set(Cw) or not wC > (0, 0) or not k2 > k1: fail(cnt, "FC", name, t1, t2)
                n1, n2 = not intact1, not disj
                n3 = (k2 > k1 and k2 >= add(k1, wC) and wC > (0, 0))
                cnt["NC_chk"] += 1; cnt["N1"] += n1; cnt["N2"] += n2; cnt["N3"] += n3
                if not (n1 or n2 or n3): fail(cnt, "NC", name, t1, t2)
                if disj:
                    h = max(Cw, key=lambda u: g.rank[u])
                    if g.rank[h] > g.rank[c] and g.prio[h] % 2 == 0 and (h not in p2 or intact2):
                        X1 = st[t1]["Xi"][q2][1]; X2 = st[t2]["Xi"][q2][1]
                        dif = X1 ^ X2; lev = dif.bit_length() - 1
                        cnt["N3L_chk"] += 1; cnt["N3L_eq"] += lev == g.rank[h]
                        if lev < g.rank[h] or (MUT == 2 and lev <= g.rank[h]): fail(cnt, "N3L", name, t1, t2, lev, g.rank[h])


def main(a):
    cnt = Counter(); rng = random.Random(1418); nst = int(os.environ.get("RANDSTARTS", "2"))
    def do(g, name, r, extra=None):
        starts = ([extra] if extra else []) + [RE.best_reward_start(g)] + [D.rand_start(g, r) for _ in range(nst)]
        for j, s0 in enumerate(starts):
            cnt["RUNS"] += 1; analyse(g, s0, cnt, "%s/%d" % (name, j))
    if a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            do(D.rand_ck(r2, nn, r2.randint(1, min(km, nn - 1))), "rand%d" % i, rng)
    else:
        for f in a:
            path, _, sp = f.partition(":")
            g = RE.parse(path)
            if g.n > int(os.environ.get("MAXN", "64")): cnt["skip_big"] += 1; continue
            do(g, os.path.relpath(path), random.Random(os.path.relpath(path)), HP.parse_start(g, sp) if sp else None)
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
