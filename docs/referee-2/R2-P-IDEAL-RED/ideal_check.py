#!/usr/bin/env python3
r"""REFEREE-2 successor 26 (Opus 5.5, D15): own check of packet P-IDEAL-RED (docs/new/P-IDEAL-RED.md, sha1 06f2c186 @ l-new 0ebddcf5).
Written from the packet text (§0-§8). The lane's box150/check.py, box139/paths.py and every other lane script are NOT imported.
Model (§0 = RESULTS R104's definition): genome JSON in the R178 format, opts[x][k] = [wt, xt, b] (-1 = none / X), gate[x][k], br[b],
bp[b], start[x]. Xi-values are SETS of beta ids, compared by the top-rank beta of the symmetric difference (NOT through ENC's integers;
ENC is checked separately). Keys under the NEW state, root-first. Every statement is checked for SEVERAL random topological orders pi
(the packet claims «every such pi») and for BOTH tie rules of h_t (smallest / largest index; «any fixed tie rule works»).
Violation counters (all must be 0):
  ENC      sign of e(P) - e(Q) differs from the set order, on every pair compared
  LOCAL    (a)/(b) on random state pairs agreeing on the chain / on strict descendants (and (c) keys)
  MONO     cv_(s_t)(x) < cv_(s_(t-1))(x)
  XINEW    some least-level mover h of Mv_t (EVERY tie) has s_t(h) in A_(s_(t-2))(h)
  RISE     (a) no strict rise at t-1, (b) Z_t empty, (c) z in Z_t with pi(z) <= pi(h) or z not a strict Xi-descendant
  CHAIN    (i) chained with pi(h_t) >= pi(h_(t-1)); (ii) T > N (1 + U); U-EQ: U > max(T - 1, 0)
  KEYFLIP  any mover with deg(x) = 2: moves(x) > 1 + KF_x (checked in every genome); KF-EQ in degree <= 2 genomes
  DECR     (a)-(c) and EXACT-ENERGY (E strictly falls; E(s_0) <= D^N - 1)
  TOPMONO  every k (degree <= 2)                RBOUND  every k, and U (degree <= 2)
  RESTR    INTERVAL-RESTRICT (i)-(iii), every k, every maximal TOP_k-constant interval: H built and RUN, states and labels compared
  ICHARGE  every r >= 2                         REC    RECURSION line 1, p_i strictly decreasing, p_i degree-2 positions, H_i shape
Info: X_KEYFLIP_deg3 = movers of degree >= 3 with moves(x) > 1 + KF'_x (KP := key-least option; the packet's §5 remark says this can
happen); X_TOP_deg3 = TOP-MONO failures in genomes with a degree >= 3 mover (box 147's remark).
NEG=old: keys read under the OLD state (control: XINEW must fire).
Usage: ideal_check.py random COUNT NMAX DMAX DEGMAX SEED [allstarts]  |  files G.json ...  (ALL=1: every start for N <= ALLN=9)"""
import sys, os, json, random, itertools
from math import comb
NEG = os.environ.get("NEG", ""); ALL = os.environ.get("ALL") == "1"; ALLN = int(os.environ.get("ALLN", "9")); NPI = int(os.environ.get("NPI", "3"))

class St:
    def __init__(s): s.c = {}; s.ex = {}
    def inc(s, k, v=1): s.c[k] = s.c.get(k, 0) + v
    def bad(s, k, m):
        s.inc("VIOL_" + k)
        if k not in s.ex: s.ex[k] = m

class Gen:
    def __init__(s, G):
        s.G = G; s.N = G["N"]; s.lev = G["lev"]; s.opts = G["opts"]; s.gate = G["gate"]; s.br = G["br"]; s.bp = G["bp"]
        s.deg = [len(o) for o in s.opts]
    def chain(s, st, x, k):
        out = [(x, k)]
        while s.opts[x][k][1] >= 0:
            x = s.opts[x][k][1]; k = st[x]; out.append((x, k))
            if len(out) > s.N + 1: raise RuntimeError("cyclic")
        return out
    def val(s, st, x, k): return frozenset(s.opts[y][kk][2] for (y, kk) in s.chain(st, x, k))
    def better(s, P, Q):   # P strictly better than Q (set order, §0)
        D = P ^ Q
        if not D: return False
        t = max(D, key=lambda b: s.br[b]); return (s.bp[t] == 0) == (t in P)
    def e(s, P): return sum((-1) ** s.bp[b] * 2 ** s.br[b] for b in P)
    def avail(s, st, x):
        cur = s.val(st, x, st[x]); return {st[x]} | {k for k in range(s.deg[x]) if k != st[x] and s.better(s.val(st, x, k), cur)}
    def key(s, st, x, k):
        wt = s.opts[x][k][0]; g = (s.gate[x][k],)
        return g if wt < 0 else s.key(st, wt, st[wt]) + g
    def run(s, start, cap=100000):
        S = [tuple(start)]; A = []
        while len(S) <= cap:
            st = S[-1]; Ast = [s.avail(st, x) for x in range(s.N)]; A.append(Ast)
            if all(len(a) == 1 for a in Ast): break
            ns = list(st)
            for l in sorted(set(s.lev)):
                for x in range(s.N):
                    if s.lev[x] == l: ns[x] = min(Ast[x], key=lambda k: s.key(st if NEG == "old" else ns, x, k))
            if tuple(ns) == st: break
            S.append(tuple(ns))
        return S, A

def topo_orders(G, rng, cnt):
    N = G["N"]; succ = [{o[1] for o in G["opts"][x] if o[1] >= 0} for x in range(N)]
    out = []
    for _ in range(cnt):
        indeg = [0] * N
        for x in range(N):
            for y in succ[x]: indeg[y] += 1
        ready = [x for x in range(N) if indeg[x] == 0]; order = []
        while ready:
            x = ready.pop(rng.randrange(len(ready))); order.append(x)
            for y in succ[x]:
                indeg[y] -= 1
                if indeg[y] == 0: ready.append(y)
        if len(order) < N: return None
        pi = [0] * N
        for i, x in enumerate(order): pi[x] = i
        out.append(pi)
    return out

def descendants(G, x):
    N = G["N"]; seen = set(); stack = [o[1] for o in G["opts"][x] if o[1] >= 0]
    while stack:
        y = stack.pop()
        if y not in seen: seen.add(y); stack += [o[1] for o in G["opts"][y] if o[1] >= 0]
    return seen

def labels(g, S, tie):
    """h_t (least level, tie by index rule), chained flags, U."""
    T = len(S) - 1; Mv = [None] + [{x for x in range(g.N) if S[t][x] != S[t - 1][x]} for t in range(1, T + 1)]
    h = [None] + [(min if tie == "min" else max)(sorted(Mv[t], key=lambda x: g.lev[x]), key=lambda x: (g.lev[x], x if tie == "min" else -x)) for t in range(1, T + 1)]
    ch = {}
    for t in range(2, T + 1):
        c = g.chain(S[t - 2], h[t], S[t][h[t]]); ch[t] = h[t - 1] in [y for (y, _) in c[1:]]
    return Mv, h, ch, sum(1 for t in ch if not ch[t])

def restrict(G, sa, pi, p):
    H = json.loads(json.dumps(G))
    for x in range(G["N"]):
        if pi[x] >= p: H["opts"][x] = [G["opts"][x][sa[x]]]; H["gate"][x] = [G["gate"][x][sa[x]]]
    st = [0 if pi[x] >= p else sa[x] for x in range(G["N"])]
    return H, st

def to_H_state(G, st, pi, p): return tuple(0 if pi[x] >= p else st[x] for x in range(G["N"]))

def TOP(Sset, pi, k): v = sorted((pi[x] for x in Sset), reverse=True)[:k]; return tuple(v + [-1] * (k - len(v)))

def check_run(G, start, st, name, pis, rng, deep=True):
    g = Gen(G); S, A = g.run(start); T = len(S) - 1; N = g.N
    st.inc("runs"); st.inc("steps", T)
    deg2 = max(g.deg) <= 2; D = max(g.deg)
    desc = [descendants(G, x) for x in range(N)]
    # ENC on every compared pair of the run (sampled: options of every mover at every state)
    for t in range(0, T + 1, max(1, T // 5)):
        for x in range(N):
            vals = [g.val(S[t], x, k) for k in range(g.deg[x])]
            for a in range(len(vals)):
                for b in range(len(vals)):
                    if a != b and g.better(vals[a], vals[b]) != (g.e(vals[a]) > g.e(vals[b])): st.bad("ENC", f"{name}@{t}")
    # LOCAL: random state pairs
    if deep:
        for _ in range(3):
            s1 = tuple(rng.randrange(d) for d in g.deg); x = rng.randrange(N)
            s2 = list(tuple(rng.randrange(d) for d in g.deg))
            for y in desc[x]: s2[y] = s1[y]
            for k in range(g.deg[x]):
                if g.val(s1, x, k) != g.val(s2, x, k): st.bad("LOCAL", f"{name} (b)")
            s3 = list(s2)
            for y in range(N):
                if g.lev[y] < g.lev[x]: s3[y] = s1[y]
            for k in range(g.deg[x]):
                if g.key(s1, x, k) != g.key(s3, x, k): st.bad("LOCAL", f"{name} (c)")
    cv = [[g.e(g.val(S[t], x, S[t][x])) for x in range(N)] for t in range(T + 1)]
    for t in range(1, T + 1):
        for x in range(N):
            if cv[t][x] < cv[t - 1][x]: st.bad("MONO", f"{name}@{t} x={x}")
    Mv = [None] + [{x for x in range(N) if S[t][x] != S[t - 1][x]} for t in range(1, T + 1)]
    for t in range(2, T + 1):
        lmin = min(g.lev[x] for x in Mv[t])
        for h in [x for x in Mv[t] if g.lev[x] == lmin]:
            w = S[t][h]
            if w in A[t - 2][h]: st.bad("XINEW", f"{name}@{t} h={h}"); continue
            if not g.better(g.val(S[t - 1], h, w), g.val(S[t - 2], h, w)) or g.val(S[t - 1], h, w) == g.val(S[t - 2], h, w): st.bad("RISE", f"{name}@{t} (a)")
            Z = [y for (y, _) in g.chain(S[t - 2], h, w)[1:] if y in Mv[t - 1]]
            if not Z: st.bad("RISE", f"{name}@{t} (b)")
            for z in Z:
                if z not in desc[h] or any(pi[z] <= pi[h] for pi in pis): st.bad("RISE", f"{name}@{t} (c)")
            st.inc("xinew_checks")
    for tie in ("min", "max"):
        _, h, ch, U = labels(g, S, tie)
        for pi in pis:
            for t in ch:
                if ch[t] and pi[h[t]] >= pi[h[t - 1]]: st.bad("CHAIN", f"{name}@{t} (i) tie={tie}")
        if T > N * (1 + U): st.bad("CHAIN", f"{name} (ii) T {T} U {U} tie={tie}")
        if U > max(T - 1, 0): st.bad("CHAIN", f"{name} U-EQ")
        if T >= 2: st.inc("CHAIN_U_" + tie, U)
    Uref = labels(g, S, "min")[3]
    # KEYFLIP
    moves = [sum(1 for t in range(1, T + 1) if x in Mv[t]) for x in range(N)]
    KF = [0] * N
    for x in range(N):
        if g.deg[x] == 2:
            KP = [min(range(2), key=lambda k: g.key(S[t], x, k)) for t in range(T + 1)]
            KF[x] = sum(1 for t in range(1, T + 1) if KP[t] != KP[t - 1])
            if moves[x] > 1 + KF[x]: st.bad("KEYFLIP", f"{name} x={x}")
        elif g.deg[x] >= 3:
            KP = [min(range(g.deg[x]), key=lambda k: g.key(S[t], x, k)) for t in range(T + 1)]
            kf = sum(1 for t in range(1, T + 1) if KP[t] != KP[t - 1])
            if moves[x] > 1 + kf: st.inc("X_KEYFLIP_deg3")
    if deg2:
        if T > sum(moves) or sum(moves) > N + sum(KF) or sum(KF) > N * T: st.bad("KEYFLIP", f"{name} KF-EQ")
    # DECREMENT, EXACT-ENERGY, TOP-*, INTERVAL-*  (per pi)
    c = [[len(A[t][x]) - 1 for x in range(N)] for t in range(T + 1)]
    for pi in pis:
        E = [sum(c[t][x] * D ** pi[x] for x in range(N)) for t in range(T + 1)]
        if D >= 2 and E[0] > D ** N - 1: st.bad("DECR", f"{name} E0")
        for t in range(1, T + 1):
            y = max(Mv[t], key=lambda x: pi[x])
            if c[t - 1][y] < 1 or c[t][y] >= c[t - 1][y]: st.bad("DECR", f"{name}@{t} (a)/(b)")
            for x in range(N):
                if pi[x] > pi[y] and (c[t][x] != c[t - 1][x] or S[t][x] != S[t - 1][x]): st.bad("DECR", f"{name}@{t} (c)")
            if E[t] >= E[t - 1]: st.bad("DECR", f"{name}@{t} energy")
        Sset = [{x for x in range(N) if c[t][x] >= 1} for t in range(T + 1)]
        RANK = [None] + [1 + sum(1 for x in Sset[t - 1] if pi[x] > pi[max(Mv[t], key=lambda z: pi[z])]) for t in range(1, T + 1)]
        topfail = False
        for k in range(1, N + 1):
            for t in range(1, T + 1):
                a, b = TOP(Sset[t], pi, k), TOP(Sset[t - 1], pi, k)
                ok = (a < b) if RANK[t] <= k else (a == b)
                if not ok: topfail = True
                if deg2 and not ok: st.bad("TOPMONO", f"{name}@{t} k={k}")
            if deg2:
                cnt = sum(1 for t in range(1, T + 1) if RANK[t] <= k)
                if cnt > sum(comb(N, j) for j in range(k + 1)) - 1: st.bad("RBOUND", f"{name} k={k}")
        if not deg2 and topfail: st.inc("X_TOP_deg3")
        if not deg2: continue
        _, hmin, chmin, U = labels(g, S, "min")
        R = max([RANK[t] for t in chmin if not chmin[t]], default=0)
        if U > sum(comb(N, j) for j in range(R + 1)) - 1: st.bad("RBOUND", f"{name} U")
        for r in range(2, N + 1):
            if sum(1 for t in range(1, T + 1) if RANK[t] == r) > (N - r + 1) * (1 + sum(1 for t in range(1, T + 1) if RANK[t] <= r - 1)): st.bad("ICHARGE", f"{name} r={r}")
        for k in (range(1, N + 1) if deep else (1,)):
            tops = [TOP(Sset[t], pi, k) for t in range(T + 1)]
            ivs = []; a = 0
            for t in range(1, T + 2):
                if t == T + 1 or tops[t] != tops[a]: ivs.append((a, t)); a = t
            for (a, b) in ivs:
                p = tops[a][k - 1]
                for t in range(a + 1, b):
                    if any(pi[x] >= p for x in Mv[t]): st.bad("RESTR", f"{name} (i) k={k}")
                H, hs = restrict(G, S[a], pi, p); gh = Gen(H); SH, _ = gh.run(hs)
                want = [to_H_state(G, S[t], pi, p) for t in range(a, b)]
                if [tuple(z) for z in SH[:b - a]] != want: st.bad("RESTR", f"{name} (ii) k={k} [{a},{b})"); continue
                _, _, chH, _ = labels(gh, SH, "min")
                for t in range(a + 2, b):
                    if chmin[t] != chH[t - a]: st.bad("RESTR", f"{name} (iii) k={k} t={t}")
                st.inc("restr_intervals")
        # RECURSION (k = 1)
        tops = [TOP(Sset[t], pi, 1) for t in range(T + 1)]
        ivs = []; a = 0
        for t in range(1, T + 2):
            if t == T + 1 or tops[t] != tops[a]: ivs.append((a, t)); a = t
        ps = [tops[a][0] for (a, b) in ivs]
        if any(ps[i] <= ps[i + 1] for i in range(len(ps) - 1)): st.bad("REC", f"{name} p not decreasing")
        rhs = len(ivs) - 1
        for (a, b), p in zip(ivs, ps):
            if p < 0:
                if b - a != 1 or b != T + 1: st.bad("REC", f"{name} p=-1 interval not last/empty")
                continue
            x = [z for z in range(N) if pi[z] == p][0]
            if g.deg[x] != 2: st.bad("REC", f"{name} p not deg 2")
            H, hs = restrict(G, S[a], pi, p); gh = Gen(H)
            if any(len(H["opts"][z]) == 2 and pi[z] >= p for z in range(N)): st.bad("REC", f"{name} H shape")
            SH, _ = gh.run(hs); rhs += labels(gh, SH, "min")[3] + 1
        if U > rhs: st.bad("REC", f"{name} line 1 U {U} > {rhs}")
        st.inc("rec_runs")

def rand_genome(rng, Nmax, dmax, degmax):
    d = rng.randint(1, dmax); N = rng.randint(d, max(d, Nmax))
    lev = list(range(d)) + [rng.randrange(d) for _ in range(N - d)]; rng.shuffle(lev)
    order = list(range(N)); rng.shuffle(order); pos = {x: i for i, x in enumerate(order)}
    opts = []; M = 0
    for x in range(N):
        o = []
        for k in range(rng.randint(1, degmax)):
            wt = -1 if lev[x] == 0 else rng.choice([y for y in range(N) if lev[y] == lev[x] - 1])
            cand = [y for y in range(N) if pos[y] > pos[x]]
            xt = rng.choice(cand) if cand and rng.random() < 0.7 else -1
            o.append([wt, xt, M]); M += 1
        opts.append(o)
    ids = list(range(M)); rng.shuffle(ids)
    for o in opts:
        for f in o: f[2] = ids.pop()
    gi = rng.sample(range(3 * M + 5), M); it = iter(gi)            # gate indices: distinct naturals with gaps
    gate = [[next(it) for _ in o] for o in opts]
    br = rng.sample(range(3 * M + 5), M); bp = [rng.randint(0, 1) for _ in range(M)]   # ranks: distinct naturals with gaps
    return dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=[rng.randrange(len(o)) for o in opts])

def main():
    a = sys.argv[1:]; st = St(); rng = random.Random(26)
    if a[0] == "random":
        cnt, Nmax, dmax, degmax, seed = map(int, a[1:6]); allst = len(a) > 6; rng = random.Random(seed)
        gens = [rand_genome(rng, Nmax, dmax, degmax) for _ in range(cnt)]
    else:
        gens = [json.load(open(f)) for f in a[1:]]; allst = ALL
    for i, G in enumerate(gens):
        pis = topo_orders(G, rng, NPI)
        if pis is None: st.inc("skipped_cyclic"); continue
        st.inc("genomes"); st.inc("deg2_genomes" if max(len(o) for o in G["opts"]) <= 2 else "deg3plus_genomes")
        starts = [G["start"]]
        if allst and G["N"] <= ALLN: starts = list(itertools.product(*[range(len(o)) for o in G["opts"]]))
        for s0 in starts: check_run(G, list(s0), st, f"g{i}", pis, rng, deep=(len(starts) <= 64 or s0 == tuple(G["start"])))
    viol = {k: v for k, v in st.c.items() if k.startswith("VIOL_")}
    print("IDEAL-CHECK", " ".join(f"{k} {v}" for k, v in sorted(st.c.items()) if not k.startswith("VIOL_")))
    print("VIOLATIONS", sum(viol.values()), " ".join(f"{k[5:]} {v}" for k, v in sorted(viol.items())))
    for k, m in st.ex.items(): print("  first", k, m)

if __name__ == "__main__":
    main()
