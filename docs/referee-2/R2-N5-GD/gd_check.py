#!/usr/bin/env python3
r"""REFEREE-2 successor 13 (Opus 5.5, D15): mechanical check of packet P-N5-GD (docs/new/P-N5-GD-box43.md sha1 b898ff82 @ 3c6f6c16).
State sequence: own SPEC N5 loop (R2-N5-DUAL/dual_check.Runner, on L-SI's si.py engine, read-only), from S3 and random start pairs, on
every game. sbar_k := SPEC S1's Odd counterstrategy (si tau_full). Play values from the definitions (R2-N5-RE/re_check.Game: (c, P, l), VJ00
order); Xi_k := value of the (sigma_k, sbar_k)-play, W_k := value of the (sigma_k, tau_k)-play. Lane's f1d.py not run or imported.
Checks: GDA  v in F_D => Xi(v) = W(v).
        GDB  (h_D) at k, v in R_D, u = u(v): Xi(v) = pi_v (+) Xi(u), W(v) = pi_v (+) W(u), and both plays from u avoid pi_v.
        GDC1 (h_D), (h3_D): for every pair y, z in R_D with u(y) = u(z): Xi-order of (pi_y (+) Xi(u), pi_z (+) Xi(u)) = W-order version.
        GDC2 (h_D), (h3_D): for EVERY L with M_D <= L <= n - 1 (and L = bot if M_D = bot): COARSE_L(Xi(v)) = COARSE_L(W(v)) for all v.
        F1D  per phase ((lambda_Xi, tau) constant), per maximal run with (D, R_D) constant: transitions with a Xi-change on F_D
             <= max(0, |F_D| - 1).
        WOD  transition k -> k+1 with tau restricted to Odd unchanged, u in D_k & D_{k+1}, (h_D) at k and k+1: W_{k+1}(u) >= W_k(u).
Mutations GD_MUT: gda (GDA on R_D instead of F_D), c2 (GDC2 at L = M_D - 1 when M_D >= 0), f1 (F1D with |F_D| - 2), wo (WOD reversed).
Usage: gd_check.py random N nmin nmax seed | files list.txt [runs]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL")); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RE"))
import dual_check as DC
import re_check as RC
pg, Engine, Stats = DC.pg, DC.Engine, DC.Stats
MUT = os.environ.get("GD_MUT", "")
INF, BOT = 10 ** 9, -10 ** 9

def lev(g, x, y):
    if x == y: return BOT
    if x[0] != y[0]: return INF
    d = x[1] ^ y[1]
    if d: return max(g.rank[u] for u in d)
    return -1

def coarse(g, x, L):
    if L == BOT: return x
    return (x[0], frozenset(u for u in x[1] if g.rank[u] > L))

def prefix(g, path, x):
    c, P, l = x
    return (c, P | frozenset(u for u in path if g.rank[u] > g.rank[c]), l + len(path))

def play_vertices(f, v):
    seen, path, x = set(), [], v
    while x not in seen: seen.add(x); path.append(x); x = f[x]
    return path

def state_info(g, E, sg, tu):
    n = g.n
    _, tf = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
    sbar = [tf[v] if g.owner[v] == 1 else None for v in range(n)]
    fh = [sg[v] if g.owner[v] == 0 else sbar[v] for v in range(n)]
    fw = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
    S = DC_State()
    S.fh, S.fw = fh, fw
    S.Xi = [g.play(fh, v)[0] for v in range(n)]; S.W = [g.play(fw, v)[0] for v in range(n)]
    S.D = frozenset(v for v in range(n) if g.owner[v] == 1 and sbar[v] != tu[v])
    S.u, S.pi = {}, {}
    for v in range(n):
        x, p, seen = v, [], set()
        while x not in seen and x not in S.D: seen.add(x); p.append(x); x = fw[x]
        if x in S.D: S.u[v] = x; S.pi[v] = p
    S.RD = frozenset(S.u); S.FD = frozenset(range(n)) - S.RD
    def after(f, u): return play_vertices(f, f[u])            # vertices visited after leaving u
    S.hD = all(not (set(after(fh, u)) & S.D) and not (set(after(fw, u)) & S.D) for u in S.D)
    S.h3D = all(S.Xi[u][0] == S.W[u][0] for u in S.D)
    S.MD = max((lev(g, S.Xi[u], S.W[u]) for u in S.D), default=BOT)
    S.lam = tuple(S.Xi[v][0] for v in range(n))
    return S

class DC_State: pass

def check_run(g, states, st, name):
    n = g.n; E = Engine(pg.Game(list(g.prio), list(g.owner), [list(s) for s in g.succ]))
    A = [state_info(g, E, list(s), list(t)) for s, t in states]
    st.inc("runs"); st.inc("states", len(A))
    for k, S in enumerate(A):
        # GDA
        tgt = S.RD if MUT == "gda" else S.FD
        for v in tgt:
            if S.Xi[v] != S.W[v]: st.bad("GDA", f"{name}@{k}: v {v}"); break
        if S.D: st.inc("states_D_nonempty")
        if len(S.D) >= 2: st.inc("states_D_ge2")
        if not S.hD: continue
        st.inc("states_hD")
        for v in S.RD:
            u = S.u[v]; p = S.pi[v]
            if S.Xi[v] != prefix(g, p, S.Xi[u]) or S.W[v] != prefix(g, p, S.W[u]): st.bad("GDB", f"{name}@{k}: v {v} values"); break
            if set(p) & (set(play_vertices(S.fh, u)) | set(play_vertices(S.fw, u))): st.bad("GDB", f"{name}@{k}: u's play meets pi_{v}"); break
        st.inc("GDB_vertices", len(S.RD))
        if not S.h3D: continue
        st.inc("states_hD_h3D")
        byu = {}
        for v in S.RD: byu.setdefault(S.u[v], []).append(v)
        for u, vs in byu.items():
            for i in range(len(vs)):
                for j in range(i + 1, len(vs)):
                    y, z = vs[i], vs[j]
                    a = g.cmp(prefix(g, S.pi[y], S.Xi[u]), prefix(g, S.pi[z], S.Xi[u]))
                    b = g.cmp(prefix(g, S.pi[y], S.W[u]), prefix(g, S.pi[z], S.W[u]))
                    st.inc("GDC1_pairs")
                    if a != b: st.bad("GDC1", f"{name}@{k}: pair {y},{z}")
        Ls = [BOT] if S.MD == BOT else list(range(S.MD, n))
        if MUT == "c2" and S.MD >= 0: Ls = [S.MD - 1]
        for L in Ls:
            st.inc("GDC2_levels")
            if any(coarse(g, S.Xi[v], L) != coarse(g, S.W[v], L) for v in range(n)): st.bad("GDC2", f"{name}@{k}: L {L} (M_D {S.MD})"); break
        if S.MD >= 0: st.inc("states_MD_ge0")
    # WOD
    for k in range(len(A) - 1):
        a, b = A[k], A[k + 1]
        if any(states[k][1][v] != states[k + 1][1][v] for v in range(n) if g.owner[v] == 1): continue
        if not (a.hD and b.hD): continue
        for u in a.D & b.D:
            c = g.cmp(b.W[u], a.W[u]); st.inc("WOD_checks")
            if (c < 0) if MUT != "wo" else (c >= 0 and a.W[u] != b.W[u]): st.bad("WOD", f"{name}@{k}: u {u}")
    # F1D
    key = [(S.lam, tuple(states[k][1][v] for v in range(n) if g.owner[v] == 1)) for k, S in enumerate(A)]
    k = 0
    while k < len(A):
        m = k
        while m + 1 < len(A) and key[m + 1] == key[k] and (A[m + 1].D, A[m + 1].RD) == (A[k].D, A[k].RD): m += 1
        FD = A[k].FD
        ch = sum(1 for q in range(k, m) if any(A[q].Xi[v] != A[q + 1].Xi[v] for v in FD))
        lim = max(0, len(FD) - (2 if MUT == "f1" else 1))
        st.inc("F1D_intervals")
        if ch > lim: st.bad("F1D", f"{name}: interval {k}-{m}: {ch} > {lim}")
        st.mxr("max_F1D_changes", (ch, name))
        k = m + 1

def to_rc(g):
    return RC.Game(list(g.prio), list(g.owner), [list(s) for s in g.succ])

def main():
    st = Stats(); a = sys.argv[1:]
    def go(gp, s, t, name):
        states, _ = DC.Runner(gp).run(s, t)
        check_run(to_rc(gp), states, st, name)
    if a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            gp = DC.rand_game(rng, rng.randint(nmin, nmax), "kO")
            s = [rng.choice(gp.succ[v]) for v in range(gp.n)]; t = [rng.choice(gp.succ[v]) for v in range(gp.n)]
            go(gp, s, t, f"random{seed}:{i}")
    else:
        runs = int(a[2]) if len(a) > 2 else 2; rng = random.Random(4444)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                if r == 0:
                    E, Ed = Engine(gp), Engine(DC.dual(gp)); s, t = list(E.initial("best")), list(Ed.initial("best"))
                else:
                    s = [rng.choice(gp.succ[v]) for v in range(gp.n)]; t = [rng.choice(gp.succ[v]) for v in range(gp.n)]
                go(gp, s, t, f"{path}#{r}")
    print("MODE", " ".join(a), "MUT", MUT or "-")
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")

if __name__ == "__main__":
    main()
