#!/usr/bin/env python3
r"""REFEREE-2 successor 14 (Opus 5.5, D15): mechanical check of packet P-N5-H3 (docs/si/P-N5-H3-box16.md sha1 680e4528 @ d096e404).
Derived from my R2-N5-NC/nc_check.py (packet withdrawn). State sequence: succ. 13's own SPEC loop (R2-N5-DUAL/dual_check.Runner on si.py).
Xi = S1 honest values; W_k := sigma_k's values in G_tau. COARSE_L, lev as in R25; D, u(v), pi_v, R_D, (NC), (h_D), (h3_D), M_D as in R55.
The lane's experiments/si/fb2o/ gdnc.py / tcdir.py NOT run or imported.
Checks:
  BP     (b') under (NC)
  TCC    TC-CLASS: every state, v in R_D: lambda_Xi(v) = lambda_Xi(u(v)), lambda_W(v) = lambda_W(u(v)); in-phase terminal change keeps
         lambda_Xi(u)
  C2H    C2-H3 under (h3_D) ALONE: COARSE_L(Xi) = COARSE_L(W) on V for every L with max(M_D, -1) <= L <= n
  WMG    at every in-phase S4a transition W_{k+1} >= W_k pointwise
  PCL    P^c_L on every maximal fallback-free in-phase run with (i), (ii) (checked directly, per L), every j (n <= PATHCAP)
  CRD    on those runs: freeze from k0 + n - 1
  FRZ    FRZ-U_H3: fallback-free in-phase runs with (h3_D) at every state, L = max(max_S M_D, -1): (i), (ii), freeze
Records: C2H checks at states with not (NC) / not (h_D); FRZ freeze checks with D != {} and with a not-(h_D) / not-(NC) state.
Mutations NC_MUT: b0 (BP without (NC)), pc1, crd1, c2l (C2H also one level below M_D, M_D >= 0: must fail somewhere).
Usage: h3_check.py files list.txt [runs] | start game.pg game.start | random N nmin nmax seed [kind] [starts] | climb steps nmin nmax seed out"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL"))
import dual_check as DC
pg, Engine, Stats = DC.pg, DC.Engine, DC.Stats
MUT = os.environ.get("NC_MUT", "")
PATHCAP = int(os.environ.get("PATHCAP", "9"))
BOT = -2
SCORE = [-10 ** 9]

def lasso(nxt, v):
    seen, path, x = set(), [], v
    while x not in seen: seen.add(x); path.append(x); x = nxt[x]
    return path, x

class Ctx:
    def __init__(s, g):
        s.g = g; s.n = g.n; s.E = Engine(g); s.Wc = {}
    def ckey(s, val, L):
        c, m, _ = val
        return (s.E.rew[c], s.E.weight(m >> (L + 1) << (L + 1)))
    def lev(s, x, y):
        if x[0] != y[0]: return float("inf")
        d = x[1] ^ y[1]
        if d: return d.bit_length() - 1
        return -1 if x[2] != y[2] else BOT
    def Wengine(s, tu):
        key = tuple(tu[v] for v in range(s.n) if s.g.owner[v] == 1)
        if key not in s.Wc:
            succ = [[tu[v]] if s.g.owner[v] == 1 else list(s.g.succ[v]) for v in range(s.n)]
            s.Wc[key] = Engine(pg.Game(list(s.g.prio), list(s.g.owner), succ))
        return s.Wc[key]

def state_info(ctx, sg, tu):
    g, n = ctx.g, ctx.n
    xi, tf = ctx.E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
    hn = [sg[v] if g.owner[v] == 0 else tf[v] for v in range(n)]
    wv, _ = ctx.Wengine(tu).evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
    wn = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
    D = frozenset(u for u in range(n) if g.owner[u] == 1 and hn[u] != tu[u])
    uv, pi = {}, {}
    for v in range(n):
        path, _ = lasso(wn, v)
        for i, x in enumerate(path):
            if x in D: uv[v] = x; pi[v] = path[:i]; break
    NC = all(not (u in lasso(hn, u)[0][lasso(hn, u)[0].index(lasso(hn, u)[1]):]) and
             not (u in lasso(wn, u)[0][lasso(wn, u)[0].index(lasso(wn, u)[1]):]) for u in D)
    def visits_D_after(nx, u):
        x = nx[u]; seen = set()
        while x not in seen:
            if x in D: return True
            seen.add(x); x = nx[x]
        return False
    hD = all(not visits_D_after(hn, u) and not visits_D_after(wn, u) for u in D)
    h3 = all(xi[u][0] == wv[u][0] for u in D)
    MD = max((ctx.lev(xi[u], wv[u]) for u in D), default=BOT)
    return dict(xi=xi, hn=hn, w=wv, wn=wn, D=D, u=uv, pi=pi, NC=NC, hD=hD, h3=h3, MD=MD)

def fold(E, path, val):
    for x in reversed(path): val = E.extend(x, val)
    return val

def best_paths(ctx, tu, cyc, L):
    """best[x][j] := max COARSE key over simple paths of G_tau from x to a vertex of cyc with <= j edges (prefix max)."""
    g, n, E = ctx.g, ctx.n, ctx.E
    best = {}
    for x in range(n):
        raw = {}
        # mask accumulates path vertices more relevant than the END u: computed at the end, so carry the path
        def dfs2(y, vis, path):
            if y in cyc:
                m = 0
                for p in path[:-1]:
                    if E.rank[p] > E.rank[y]: m |= E.bit[p]
                k = (E.rew[y], E.weight((m >> (L + 1)) << (L + 1)))
                ne = len(path) - 1
                if ne not in raw or k > raw[ne]: raw[ne] = k
            nexts = [tu[y]] if g.owner[y] == 1 else sorted(set(g.succ[y]))
            for z in nexts:
                if z not in vis:
                    vis.add(z); path.append(z); dfs2(z, vis, path); path.pop(); vis.discard(z)
        dfs2(x, {x}, [x])
        out, cur = {}, None
        for ne in range(n):
            if ne in raw and (cur is None or raw[ne] > cur): cur = raw[ne]
            out[ne] = cur
        best[x] = out
    return best

def check_run(gp, states, fbs, st, name):
    ctx = Ctx(gp); g, n, E = gp, gp.n, ctx.E
    I = [state_info(ctx, s, t) for s, t in states]
    st.inc("runs")
    for k, S in enumerate(I):
        st.inc("states")
        if S["hD"]: st.inc("states_hD")
        if S["NC"]: st.inc("states_NC")
        if S["NC"] and not S["hD"]: st.inc("states_NC_not_hD")
        if not (S["NC"] or MUT == "b0"): continue
        for v, u in S["u"].items():
            st.inc("BP_checks")
            p = S["pi"][v]
            ok = S["xi"][v] == fold(E, p, S["xi"][u]) and S["w"][v] == fold(E, p, S["w"][u])
            ps = set(p)
            ok = ok and not (set(lasso(S["hn"], u)[0]) & ps) and not (set(lasso(S["wn"], u)[0]) & ps)
            if not ok: st.bad("BP", f"{name}@{k}: v {v} u {u} NC {S['NC']} hD {S['hD']}")
            if S["NC"] and not S["hD"]: st.inc("BP_checks_NC_not_hD")
        pass
    for k, S in enumerate(I):
        # TC-CLASS
        for v, u in S["u"].items():
            st.inc("TCC_checks")
            if S["xi"][v][0] != S["xi"][u][0] or S["w"][v][0] != S["w"][u][0]: st.bad("TCC", f"{name}@{k}: v {v} u {u}")
        if not S["h3"]: continue
        st.inc("states_h3")
        if not S["NC"]: st.inc("states_h3_not_NC")
        if not S["hD"]: st.inc("states_h3_not_hD")
        L0 = int(max(S["MD"], -1))
        Ls = list(range(L0, n + 1))
        if MUT == "c2l" and S["MD"] >= 0: Ls = [int(S["MD"]) - 1] + Ls
        for L in Ls:
            st.inc("C2H_checks")
            if not S["NC"]: st.inc("C2H_checks_not_NC")
            if any(ctx.ckey(S["xi"][v], L) != ctx.ckey(S["w"][v], L) for v in range(n)):
                st.bad("C2H", f"{name}@{k}: L {L} MD {S['MD']}")
    # phases and fallback-free runs
    tauk = [tuple(t[v] for v in range(n) if g.owner[v] == 1) for _, t in states]
    lam = [tuple(S["xi"][v][0] for v in range(n)) for S in I]
    key = [(lam[k], tauk[k]) for k in range(len(states))]
    k0 = 0
    while k0 < len(states):
        k1 = k0
        while k1 + 1 < len(states) and key[k1 + 1] == key[k0]: k1 += 1
        st.inc("phases")
        for s in range(k0, k1):
            if fbs[s]: continue
            st.inc("WMG_transitions")
            for v in range(n):
                if E.key(I[s + 1]["w"][v]) < E.key(I[s]["w"][v]): st.bad("WMG", f"{name}@{s}: v {v}")
        for s_ in range(k0, k1):
            A, B = I[s_], I[s_ + 1]
            for v in set(A["u"]) & set(B["u"]):
                if A["u"][v] != B["u"][v]:
                    st.inc("TCC_terminal_changes")
                    if A["xi"][A["u"][v]][0] != B["xi"][B["u"][v]][0]: st.bad("TCC2", f"{name}@{s_}: v {v}")
        # maximal fallback-free runs inside the phase
        a = k0
        while a <= k1:
            b = a
            while b < k1 and not fbs[b]: b += 1
            check_ffrun(ctx, I, states, a, b, st, name)
            a = b + 1
        k0 = k1 + 1

def check_ffrun(ctx, I, states, a, b, st, name):
    g, n, E = ctx.g, ctx.n, ctx.E
    st.inc("ff_runs"); st.mxr("max_ff_run_transitions", (b - a, name))
    tu = states[a][1]
    def cond(k, L):
        S = I[k]
        return all(ctx.ckey(S["xi"][v], L) == ctx.ckey(S["w"][v], L) for v in range(n))
    lamW = [tuple(I[k]["w"][v][0] for v in range(n)) for k in range(a, b + 1)]
    # FRZ: (NC) and (h3) at every state
    if all(I[k]["h3"] for k in range(a, b + 1)):
        st.inc("FRZ_runs")
        L = int(max(max(I[k]["MD"] for k in range(a, b + 1)), -1))
        if not all(cond(k, L) for k in range(a, b + 1)): st.bad("FRZi", f"{name}@{a}: (i) fails")
        if len(set(lamW)) != 1: st.bad("FRZii", f"{name}@{a}: (ii) fails")
        if b - a >= n - 1:
            st.inc("FRZ_freeze_checks")
            if any(I[k]["D"] for k in range(a, b + 1)):
                st.inc("FRZ_freeze_checks_D_nonempty"); st.mxr("FRZ_freeze_D_nonempty_example", (b - a - (n - 1), f"{name}@{a} n {n}"))
                if any(not I[k]["hD"] for k in range(a, b + 1)):
                    st.inc("FRZ_freeze_checks_not_hD"); st.mxr("FRZ_freeze_not_hD_example", (b - a - (n - 1), f"{name}@{a} n {n}"))
                if any(not I[k]["NC"] for k in range(a, b + 1)):
                    st.inc("FRZ_freeze_checks_not_NC"); st.mxr("FRZ_freeze_not_NC_example", (b - a - (n - 1), f"{name}@{a} n {n}"))
            ref = [ctx.ckey(I[a + n - 1]["w"][v], L) for v in range(n)]
            for k in range(a + n - 1, b + 1):
                if [ctx.ckey(I[k]["w"][v], L) for v in range(n)] != ref: st.bad("FRZ", f"{name}@{k}")
        st.mxr("FRZ_run_minus_(n-1)", (b - a - (n - 1), name))
        if any(I[k]["D"] and not I[k]["hD"] for k in range(a, b + 1)):
            SCORE[0] = max(SCORE[0], b - a - (n - 1)); st.mxr("FRZ_run_with_notHD_state_minus_(n-1)", (b - a - (n - 1), name))
    # CR-D / P^c_L per L on maximal sub-runs where (i) and (ii) hold
    if n > PATHCAP: return
    for L in range(-1, n):
        k = a
        while k <= b:
            if not cond(k, L): k += 1; continue
            e = k
            while e + 1 <= b and cond(e + 1, L) and lamW[e + 1 - a] == lamW[k - a]: e += 1
            cyc = frozenset(v for v in range(n) if lamW[k - a][v] == v)
            best = best_paths(ctx, tu, cyc, L)
            st.inc("PCL_runs")
            for j in range(0, e - k + 1):
                W = I[k + j]["w"]
                jj = j + (1 if MUT == "pc1" else 0)
                for x in range(n):
                    bx = best[x].get(min(jj, n - 1))
                    st.inc("PCL_checks")
                    if bx is not None and ctx.ckey(W[x], L) < bx: st.bad("PCL", f"{name}@{k + j}: x {x} L {L} j {j}")
            frz = 1 if MUT == "crd1" else n - 1
            if e - k >= frz:
                st.inc("CRD_freeze_checks")
                if any(I[t]["D"] for t in range(k, e + 1)): st.inc("CRD_freeze_checks_D_nonempty")
                ref = [ctx.ckey(I[k + frz]["w"][v], L) for v in range(n)]
                for t in range(k + frz, e + 1):
                    if [ctx.ckey(I[t]["w"][v], L) for v in range(n)] != ref: st.bad("CRD", f"{name}@{t}: L {L}")
            st.mxr("CRD_run_minus_(n-1)", (e - k - (n - 1), name))
            k = e + 1

def run_game(gp, s, t, st, name):
    states, fbs = DC.Runner(gp).run(s, t)
    check_run(gp, states, fbs, st, name)

def starts(gp, r, rng):
    if r == 0: return list(Engine(gp).initial("best")), list(Engine(DC.dual(gp)).initial("best"))
    return [rng.choice(gp.succ[v]) for v in range(gp.n)], [rng.choice(gp.succ[v]) for v in range(gp.n)]

def rand_kO(rng, n, k):
    while True:
        gp = DC.rand_game(rng, n, "kO")
        odd = [v for v in range(n) if gp.owner[v] == 1]
        if len(odd) < k: continue
        keep = set(rng.sample(odd, k)); succ = [list(s) for s in gp.succ]
        for v in odd:
            if v not in keep: succ[v] = succ[v][:1]
        if all(len(set(succ[v])) >= 2 for v in keep): return pg.Game(list(gp.prio), list(gp.owner), succ)

def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3; rng = random.Random(1919)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                s, t = starts(gp, r, rng); run_game(gp, s, t, st, f"{path}#{r}")
    elif a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); kind = a[5] if len(a) > 5 else "kO"; k = int(a[6]) if len(a) > 6 else 2
        rng = random.Random(seed)
        for i in range(N):
            nn = rng.randint(nmin, nmax)
            gp = DC.rand_game(rng, nn, "kO") if kind == "kO" else rand_kO(rng, nn, int(kind[1:]))
            for r in range(1, k + 1):
                s, t = starts(gp, r, rng); run_game(gp, s, t, st, f"random{seed}:{i}#{r}")
    elif a[0] == "start":
        gp = pg.read(a[1]); s, t = [x[0] for x in gp.succ], [x[0] for x in gp.succ]
        for line in open(a[2]):
            parts = line.split()
            if not parts: continue
            tgt = s if parts[0] == "SIGMA0" else t
            for kv in parts[1:]:
                v, w = map(int, kv.split(":")); tgt[v] = w
        run_game(gp, s, t, st, os.path.basename(a[1]) + "#start")
    elif a[0] == "climb":
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FBRED")); import fbred_check as FC
        steps, nmin, nmax, seed, out = int(a[1]), int(a[2]), int(a[3]), int(a[4]), a[5]; rng = random.Random(seed)
        best = DC.rand_game(rng, rng.randint(nmin, nmax), "kO"); bsc = -10 ** 9
        for it in range(steps):
            cand = FC.mutate(rng, best) if it else best
            if cand.n > nmax: continue
            sc, bp = -10 ** 9, None
            for r in range(4):
                s, t = starts(cand, 1, rng); SCORE[0] = -10 ** 9
                run_game(cand, s, t, st, f"climb{seed}:{it}:{r}")
                if SCORE[0] > sc: sc, bp = SCORE[0], (s, t)
            if sc >= bsc and bp is not None:
                bsc, best = sc, cand
                open(out + ".pg", "w").write(pg.dumps(best))
                open(out + ".start", "w").write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in enumerate(bp[0]) if best.owner[v] == 0) +
                                                "\nTAU0 " + " ".join(f"{v}:{w}" for v, w in enumerate(bp[1]) if best.owner[v] == 1) + f"\nscore {bsc}\n")
        st.mxr("climb_best", (bsc, out))
    print("MODE", " ".join(a), "MUT", MUT or "-", "PATHCAP", PATHCAP)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")

if __name__ == "__main__":
    main()
