#!/usr/bin/env python3
"""Box 45d (L-RED successor 19; Lead 05:44Z): exact checker of P-N5-H3 (docs/si/P-N5-H3-box16.md, sha1 680e4528), written from the
packet's §1-§6 text (not from L-SI's gdnc.py / tcdir.py). Trace: experiments/red/o1/o1_19.trace (own copy of n5.py's loop).
Per state k: Ξ_k, σ̄_k from SPEC S1 (Engine.evaluate); W_k(v) := S1 value of the (σ_k, τ_k)-play from v, computed from the play itself
(lasso; cycle node = top-ranked cycle vertex; P = prefix before the first visit of the cycle node, ranked above it; ℓ = edges to it).
D_k := {Odd u : σ̄_k(u) != τ_k(u)}; u(v) := first vertex of D_k on v's (σ_k, τ_k)-play (v included); R_D := {v : u(v) exists}.
(h3_D): λ_Ξ(u) = λ_W(u) for u ∈ D_k. lev(x, y) := ∞ (cycle nodes differ) / top rank of P(x) Δ P(y) / −1 (only lengths) / ⊥ (equal).
M_D := max_{u ∈ D_k} lev(Ξ_k(u), W_k(u)), ⊥ if D_k = ∅. COARSE_L(x) := (c, P ∩ V_{>L}) (ranks > L).
Checks: RD_A   R55 (a) Ξ = W on F_D (sanity of the W computation);
        TCC    TC-CLASS: λ_Ξ(v) = λ_Ξ(u(v)), λ_W(v) = λ_W(u(v)) for v ∈ R_D (every state);
        C2H3   at every (h3_D) state: COARSE_L(Ξ(v)) = COARSE_L(W(v)) for all v, all L from max(M_D, −1) to n − 1;
        WMG    W_{k+1} ⊵ W_k pointwise at every in-phase S4a transition;
        FRZ    (frz_move_gap = max over qualifying runs of (index of the last COARSE_L(W) change) − (n − 1); > 0 is a kill)
        on every maximal fallback-free in-phase run S with (h3_D) at all its states, L := max(max_S M_D, −1): COARSE_L(W) constant
               from state k0 + n − 1 on (non-vacuous only if |S| >= n states).
Reported: counts, longest qualifying run (states) vs n, FRZ non-vacuous runs, and the 'kill' = a qualifying run of >= n states whose
COARSE_L(W) moves after its (n − 1)-th state. Usage: h3_19.py file game.pg [start.json]"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "o1"))
import o1_19 as O, pg, verify
BOT, INF = -2, 10 ** 9

def play_val(E, g, sig, tau, v):
    n = g.n; seen = {}; path = []
    while v not in seen:
        seen[v] = len(path); path.append(v); v = sig[v] if g.owner[v] == 0 else tau[v]
    cyc = path[seen[v]:]; c = max(cyc, key=lambda x: E.rank[x])
    i = path.index(c); P = 0
    for x in path[:i]:
        if E.rank[x] > E.rank[c]: P |= E.bit[x]
    return (c, P, i), path

def lev(E, x, y):
    if x[0] != y[0]: return INF
    d = x[1] ^ y[1]
    if d: return d.bit_length() - 1
    return -1 if x[2] != y[2] else BOT

def coarse(x, L): return (x[0], x[1] & ~((1 << (L + 1)) - 1)) if L >= 0 else (x[0], x[1])

def analyse(g, start=None, cap=5000):
    n = g.n; S, FB, E = O.trace(g, start, "n5", cap)
    ev = [E.evaluate(s) for s, _ in S]; Xi = [X for X, _ in ev]; SB = [B for _, B in ev]
    r = dict(n=n, ITER=len(FB), states=0, h3_states=0, c2_checks=0, tcc_checks=0, wmg_checks=0, frz_runs=0, frz_nonvac=0,
             frz_longest=0, frz_gap=-10 ** 9, frz_move_gap=-10 ** 9, frz_moves=0, fails=[])
    lamX = [tuple(x[0] for x in X) for X in Xi]
    W, lamW, D, U, MD, H3 = [], [], [], [], [], []
    for k, (sig, tau) in enumerate(S):
        Wk, uk = [], []
        Dk = {u for u in range(n) if g.owner[u] == 1 and SB[k][u] != tau[u]}
        for v in range(n):
            val, path = play_val(E, g, sig, tau, v); Wk.append(val)
            uk.append(next((x for x in path if x in Dk), None))
        W.append(Wk); lamW.append(tuple(x[0] for x in Wk)); D.append(Dk); U.append(uk)
        h3 = all(lamX[k][u] == lamW[k][u] for u in Dk); H3.append(h3)
        md = max((lev(E, Xi[k][u], Wk[u]) for u in Dk), default=BOT); MD.append(md)
        r["states"] += 1
        for v in range(n):
            if uk[v] is None and tuple(Xi[k][v]) != tuple(Wk[v]): r["fails"].append(f"RD_A k={k} v={v}")
            if uk[v] is not None:
                r["tcc_checks"] += 1
                if lamX[k][v] != lamX[k][uk[v]] or lamW[k][v] != lamW[k][uk[v]]: r["fails"].append(f"TCC k={k} v={v}")
        if h3:
            r["h3_states"] += 1
            for L in range(max(md, -1), n):
                r["c2_checks"] += 1
                if any(coarse(Xi[k][v], L) != coarse(Wk[v], L) for v in range(n)): r["fails"].append(f"C2H3 k={k} L={L} MD={md}"); break
    # phases, WM-G, FRZ runs
    a = 0; N = len(S)
    while a < N:
        b = a
        while b + 1 < N and lamX[b + 1] == lamX[a] and S[b + 1][1] == S[a][1]: b += 1
        for k in range(a, b):
            if not FB[k]:
                r["wmg_checks"] += 1
                if any(E.key(W[k + 1][v]) < E.key(W[k][v]) for v in range(n)): r["fails"].append(f"WMG k={k}")
        # maximal fallback-free runs of states inside [a, b] with (h3_D) at every state
        k = a
        while k <= b:
            if not H3[k]: k += 1; continue
            k0 = k
            while k + 1 <= b and not FB[k] and H3[k + 1]: k += 1
            k1 = k; L = max(max(MD[k0:k1 + 1]), -1); length = k1 - k0 + 1
            last = None
            for t in range(k0, k1):
                if any(coarse(W[t + 1][v], L) != coarse(W[t][v], L) for v in range(n)): last = t + 1 - k0; r["frz_moves"] += 1
            if last is not None: r["frz_move_gap"] = max(r["frz_move_gap"], last - (n - 1))
            r["frz_runs"] += 1; r["frz_longest"] = max(r["frz_longest"], length); r["frz_gap"] = max(r["frz_gap"], length - n)
            if length >= n:
                r["frz_nonvac"] += 1; ref = [coarse(W[k0 + n - 1][v], L) for v in range(n)]
                for t in range(k0 + n - 1, k1 + 1):
                    if [coarse(W[t][v], L) != ref[v] for v in range(n)].count(True): r["fails"].append(f"FRZ k0={k0} t={t} L={L}"); break
            k += 1
        a = b + 1
    win, ws = E.regions(S[-1][0]); e = verify.check(g, win, ws)
    if e: r["fails"].append("OUT_STRAT " + e[0])
    return r

if __name__ == "__main__" and sys.argv[1] == "file":
    a = sys.argv; g = pg.parse("".join(l for l in open(a[2]) if not l.lstrip().startswith("%")))
    st = json.load(open(a[3]))["start"] if len(a) > 3 and a[3].endswith(".json") else None
    print(json.dumps(analyse(g, st)))

def libmain(seed, R, nmax, files):
    import random
    rng = random.Random(seed); tot = {}; fails = {}; best = {}; runs = 0
    for f in files:
        try: g = pg.parse("".join(l for l in open(f) if not l.lstrip().startswith("%")))
        except Exception: continue
        if g.n > nmax or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) < 1: continue
        for k in range(R + 1):
            st = None if k == 0 else [rng.choice(g.succ[v]) for v in range(g.n)]
            r = analyse(g, st); runs += 1
            for kk in ("states", "h3_states", "c2_checks", "tcc_checks", "wmg_checks", "frz_runs", "frz_nonvac", "frz_moves"): tot[kk] = tot.get(kk, 0) + r[kk]
            for x in r["fails"]:
                fails[x.split()[0]] = fails.get(x.split()[0], 0) + 1
                if fails[x.split()[0]] <= 3: print("FAIL", f, x, st, flush=True)
            for kk in ("frz_longest", "frz_gap", "frz_move_gap"):
                if kk not in best or r[kk] > best[kk][0]: best[kk] = (r[kk], os.path.basename(f), st is None)
    print("RUNS", runs, "TOT", tot, "FAILS", fails, "BEST", best, flush=True)

def randmain(seed, count, nmin, nmax, kmax):
    import random
    rng = random.Random(seed); tot = {}; fails = {}; best = {}
    for i in range(count):
        n = rng.randint(nmin, nmax); prio = [rng.randrange(2 * n) for _ in range(n)]; owner = [0 if rng.random() < 0.6 else 1 for _ in range(n)]
        succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3)) if owner[v] == 0 else 1))) for v in range(n)]
        for o in rng.sample(range(n), rng.randint(2, kmax)): owner[o] = 1; succ[o] = sorted(set(rng.sample(range(n), rng.randint(2, max(2, n // 2)))))
        g = pg.Game(prio, owner, succ); st = None if i % 2 == 0 else [rng.choice(g.succ[v]) for v in range(n)]
        r = analyse(g, st)
        for kk in ("states", "h3_states", "c2_checks", "tcc_checks", "wmg_checks", "frz_runs", "frz_nonvac", "frz_moves"): tot[kk] = tot.get(kk, 0) + r[kk]
        for x in r["fails"]:
            fails[x.split()[0]] = fails.get(x.split()[0], 0) + 1
            if fails[x.split()[0]] <= 3: print("FAIL", x, json.dumps(dict(prio=prio, owner=owner, succ=succ, start=st)), flush=True)
        for kk in ("frz_longest", "frz_gap", "frz_move_gap"):
            if kk not in best or r[kk] > best[kk]: best[kk] = r[kk]
    print("RAND", count, "TOT", tot, "FAILS", fails, "BEST", best, flush=True)

if __name__ == "__main__" and sys.argv[1] == "lib": libmain(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5:])
if __name__ == "__main__" and sys.argv[1] == "rand": randmain(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
