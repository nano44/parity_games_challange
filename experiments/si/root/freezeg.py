#!/usr/bin/env python3
"""L-SI box 20 (successor 16): DATA for note §9 (Lead's GO (q), 14:53Z: the gate-region freeze, Theorem FREEZE-G, Corollary RELAY-PIECE).
Per phase, class c, U := U_c, D-direct gate u (u in D_t, sigma-bar_t(u) and tau(u) in A_t := F_D(t) cap U): R_u(t) := the vertices of U whose
first D_t-vertex is u (u included); E_t := A_t u R_u(t); N_t(z) := the path weight of W_t(z) (= M_t(z) on A_t); Delta_t(u) := M_t(tau u) -
M_t(sigma-bar_t u). A G-INTERVAL [s, e]: maximal run of in-phase S4a transitions with u D-direct, A and R_u non-increasing and Delta(u)
constant. G' := the graph on E in which A-vertices keep their edges into A (Even) or tau (Odd), R_u-vertices keep their edges into E (Even)
or tau (Odd, u: tau(u)), c a sink.
  GA_V   FREEZE-G (a): N_t(z) >= the best weight of a simple G'[E_t]-path from z to c with <= t - s edges (walk Bellman-Ford, DFS witness when
         it exceeds; ga_checks, ga_eq binding, ga_unk budget out);
  GB_V   FREEZE-G (b): on intervals longer than L := |E_s| - 1, N constant on E from s + L on; also M = N - Delta on R_u (GM_V);
  RP_V   RELAY-PIECE: for Odd q in U, q != u, the states t >= s + L of the interval with sigma-bar_t(q) in E_t: M(q) takes <= deg(q) values.
  Coverage: relay rho events (Xi change at an Odd choice vertex q != u whose chosen option lies in E at both ends) inside long intervals.
Control MUT=1: (a) with one more edge (must bite).
Usage: freezeg.py --one GAME [START] | --list FILE [KMIN] (env RS, NMAX)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import *
C = Counter(); VIOL = []; MUT = os.environ.get("MUT") == "1"

def state(g, E, A, U, u):
    D = Dset(g, A); Au = avoid(A["wn"], D, g.n) & U
    if u not in D or A["sb"][u] not in Au or A["t"][u] not in Au: return None
    Ru = {z for z in U if first_D(A["wn"], z, D) == u}
    dl = M(E, A["vs"][A["t"][u]]) - M(E, A["vs"][A["sb"][u]])
    N = {z: E.weight(A["W"][z][1]) for z in Au | Ru}
    return Au, Ru, dl, N

def check_a(g, E, A, Au, Ru, N, c, j, name):
    Es = Au | Ru
    if c not in Au: return
    adj = {}
    for v in Es:
        if v == c: continue
        tgt = Au if v in Au else Es
        adj[v] = [x for x in set(g.succ[v]) if x in tgt] if g.owner[v] == 0 else ([A["t"][v]] if A["t"][v] in tgt else [])
    B = {v: None for v in Es}; B[c] = 0
    for _ in range(j):
        B2 = dict(B)
        for v, xs in adj.items():
            for x in xs:
                if B[x] is not None and (B2[v] is None or wt(E, v, c) + B[x] > B2[v]): B2[v] = wt(E, v, c) + B[x]
        B = B2
    for z in Es:
        C["ga_checks"] += 1
        if B[z] is None or B[z] <= N[z]: C["ga_eq"] += (B[z] == N[z]); continue
        budget = [20000]; best = [None]
        def dfs(v, seen, w, d):
            budget[0] -= 1
            if budget[0] < 0: return
            if v == c:
                if best[0] is None or w > best[0]: best[0] = w
                return
            if d == j: return
            for x in adj.get(v, ()):
                if x not in seen: seen.add(x); dfs(x, seen, w + wt(E, v, c), d + 1); seen.discard(x)
        dfs(z, {z}, 0, 0)
        if budget[0] < 0: C["ga_unk"] += 1
        elif best[0] is not None and best[0] > N[z]: C["GA_V"] += 1; VIOL.append(("GA", name, z, j))

def run(g, name, start=None):
    E, R = rows(g, start); Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    for i, j in phases(R):
        cls = {}
        for v in range(g.n): cls.setdefault(R[i]["vs"][v][0], set()).add(v)
        for c, U in cls.items():
            if len(U) < 3: continue
            for u in [q for q in Q if q in U and q != c]:
                S = {k: state(g, E, R[k], U, u) for k in range(i, j + 1)}
                k = i
                while k <= j:
                    if S[k] is None: k += 1; continue
                    s = k
                    while (k < j and not R[k]["fb"] and S[k + 1] is not None and S[k + 1][0] <= S[k][0] and S[k + 1][1] <= S[k][1]
                           and S[k + 1][2] == S[k][2]): k += 1
                    e = k; k += 1
                    if e == s: continue
                    C["intervals"] += 1
                    for t in range(s, e + 1):
                        Au, Ru, dl, N = S[t]; check_a(g, E, R[t], Au, Ru, N, c, t - s + (1 if MUT else 0), name)
                    L = len(S[s][0] | S[s][1]) - 1
                    if e - s <= L: continue
                    C["long_intervals"] += 1; base = s + L; Nb = S[base][3]
                    for t in range(base, e + 1):
                        Au, Ru, dl, N = S[t]
                        for z in Au | Ru:
                            C["gb_checks"] += 1
                            if N[z] != Nb[z]: C["GB_V"] += 1; VIOL.append(("GB", name, i, u, t, z))
                        for z in Ru:
                            if M(E, R[t]["vs"][z]) != N[z] - dl: C["GM_V"] += 1; VIOL.append(("GM", name, z))
                    for q in Q:
                        if q not in U or q in (u, c): continue
                        vals = {M(E, R[t]["vs"][q]) for t in range(base, e + 1) if R[t]["sb"][q] in (S[t][0] | S[t][1])}
                        if vals: C["rp_checks"] += 1
                        if len(vals) > len(set(g.succ[q])): C["RP_V"] += 1; VIOL.append(("RP", name, q, len(vals)))
                        C["covered_relay_rho"] += sum(1 for t in range(base, e) if R[t]["sb"][q] in (S[t][0] | S[t][1])
                                                      and R[t + 1]["sb"][q] in (S[t + 1][0] | S[t + 1][1])
                                                      and E.key(R[t]["vs"][q]) != E.key(R[t + 1]["vs"][q]))

def main():
    a = sys.argv[1:]
    if a[0] == "--one":
        g = load(a[1]); run(g, a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        kmin = int(a[2]) if len(a) > 2 else 2
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin:
                continue
            run(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                run(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                   {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for v in VIOL[:8]: print("VIOLATION", v)
    print("FREEZEG PASS" if not VIOL else "FREEZEG FAIL")

if __name__ == "__main__":
    main()
