#!/usr/bin/env python3
"""L-SI box 20 (successor 16): DATA for note §10 (Lead's 15:02Z item: the per-gate reset count). Per phase, class c (|U| >= 3), Odd choice
vertex u of the class (u != c), and in-phase S4a transition t -> t+1 with u a D-direct gate at t (u in D_t, sigma-bar_t(u), tau(u) in
A_t := F_D(t) cap U), the RESETS of u at t -> t+1 (each counted once per transition, by kind):
  LEAVE   u not a D-direct gate at t + 1;
  DELTA   Delta(u) := M(tau u) - M(sigma-bar u) changes (sub-kind: DELTA_U if M(sigma-bar u) changes, i.e. u's own path weight; DELTA_T else);
  RGAIN   R_u(t+1) not a subset of R_u(t) (R_u: the class vertices whose first D-vertex is u);
  AGAIN   A_t+1 not a subset of A_t.
CHARGES looked for at the same transition (several may hold):
  ROOT    Xi changes at the class's root r (the Odd choice vertex of the class with the most rho events in the phase), r != u;
  SELF    Xi changes at u itself (u's own rho event; for u = r this is the root);
  PING    an Even vertex x outside R_u(t) switches to a vertex of R_u(t) (an entry into u's gate region, the ping-pong move);
  FLIP    some Odd choice vertex q of the class changes its chosen exit par(q) (first vertex of Q_c u {c} on sigma-bar(q)'s play) between t and
          t + 1 (the relay-flip events of RESULTS R69 FLIP, in this coarse form; N1/N2/N3 are not separated here);
  NONE    none of these. ONLYSELF: no charge other than SELF (for the root, SELF is rho_r itself: the circular charge).
Per kind, split by u = the root (prefix R_) or a relay (Q_): counts by charge, and NONE examples. rgain_from_A / rgain_from_U_other_gate: where the vertices entering R_u came from (A_t, or another gate's region).
Per (phase, u): resets inside one fallback-free run, max over runs (max_resets_run).
Usage: resets.py --one GAME [START] [-v] | --list FILE [KMIN] (env RS, NMAX)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import *
C = Counter(); EX = []; VERB = "-v" in sys.argv

def par(nxt, q, c, Ts):
    x, seen = nxt[q], {q}
    while x not in seen and x not in Ts and x != c: seen.add(x); x = nxt[x]
    return x

def gate(g, E, A, U, u):
    D = Dset(g, A); Au = avoid(A["wn"], D, g.n) & U
    ok = u in D and A["sb"][u] in Au and A["t"][u] in Au
    Ru = {z for z in U if first_D(A["wn"], z, D) == u}
    dl = M(E, A["vs"][A["t"][u]]) - M(E, A["vs"][A["sb"][u]]) if ok else None
    return ok, Au, Ru, dl

def run(g, name, start=None):
    E, R = rows(g, start); Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    for i, j in phases(R):
        cls = {}
        for v in range(g.n): cls.setdefault(R[i]["vs"][v][0], set()).add(v)
        rho = Counter()
        for k in range(i, j):
            for q in Q:
                if E.key(R[k]["vs"][q]) != E.key(R[k + 1]["vs"][q]): rho[q] += 1
        for c, U in cls.items():
            Ts = {q for q in Q if q in U and q != c}
            if len(U) < 3 or not Ts: continue
            root = max(Ts, key=lambda q: rho[q])
            pars = {k: {q: par(R[k]["nxt"], q, c, Ts) for q in Ts} for k in range(i, j + 1)}
            for u in Ts:
                G = {k: gate(g, E, R[k], U, u) for k in range(i, j + 1)}
                runres = 0
                for k in range(i, j):
                    if R[k]["fb"]:
                        C["max_resets_run"] = max(C["max_resets_run"], runres); runres = 0; continue
                    ok0, A0, R0, d0 = G[k]; ok1, A1, R1, d1 = G[k + 1]
                    if not ok0: continue
                    kinds = []
                    if not ok1: kinds.append("LEAVE")
                    else:
                        if d1 != d0:
                            kinds.append("DELTA_U" if M(E, R[k]["vs"][R[k]["sb"][u]]) != M(E, R[k + 1]["vs"][R[k + 1]["sb"][u]]) else "DELTA_T")
                        if not R1 <= R0:
                            kinds.append("RGAIN")
                            for z in R1 - R0: C["rgain_from_" + ("A" if z in A0 else ("U_other_gate" if first_D(R[k]["wn"], z, Dset(g, R[k])) is not None else "?"))] += 1
                        if not A1 <= A0: kinds.append("AGAIN")
                    if not kinds: continue
                    ch = []
                    if u != root and E.key(R[k]["vs"][root]) != E.key(R[k + 1]["vs"][root]): ch.append("ROOT")
                    if E.key(R[k]["vs"][u]) != E.key(R[k + 1]["vs"][u]): ch.append("SELF")
                    if any(g.owner[x] == 0 and x not in R0 and R[k]["s"][x] != R[k + 1]["s"][x] and R[k + 1]["s"][x] in R0 for x in range(g.n)):
                        ch.append("PING")
                    if pars[k] != pars[k + 1]: ch.append("FLIP")
                    if not ch: ch = ["NONE"]
                    runres += 1; C["resets"] += 1; C[f"isroot_{u == root}"] += 1
                    for kd in kinds:
                        pre = "R" if u == root else "Q"
                        C[f"{pre}_{kd}"] += 1
                        for h in ch: C[f"{pre}_{kd}_{h}"] += 1
                        if not [h for h in ch if h not in ("SELF", "NONE")]: C[f"{pre}_{kd}_ONLYSELF"] += 1
                        if ch == ["NONE"] and len(EX) < 12: EX.append((name, i, k - i, u, kd, u == root))
                    if VERB: print(f"  {name} phase@{i} t={k - i} u={u}{'(root)' if u == root else ''} {kinds} charges={ch}")
                C["max_resets_run"] = max(C["max_resets_run"], runres)

def main():
    a = [x for x in sys.argv[1:] if x != "-v"]
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
    for x in EX: print("NONE-EXAMPLE (game, phase, t, u, kind, u is root)", x)

if __name__ == "__main__":
    main()
