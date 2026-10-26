#!/usr/bin/env python3
"""L-SI box 20 (successor 16): DATA for note §29 (Theorem FREEZE-A's hypothesis). Per phase, per maximal fallback-free run of in-phase S4a
transitions, per honest class c with |U_c| >= 2: A_t := F_D(t) cap U_c (the class vertices whose (sigma, tau)-play avoids D_t). FREEZE-A
needs A non-increasing along the run. Counted:
  runs, runs_mono (A non-increasing at every transition of the run, every class), IN (a vertex z entering A at an S4a transition), split by
  cause: DLEAVE (z's first D-vertex u at t is not in D_t+1: Odd's best reply at u now agrees with tau), SWITCH (otherwise: an Even vertex on
  z's old route pi_z switched off it), and by z's split status at t (SPLIT_IN: lambda_W(z) != lambda(z); RESULTS R63 (a) R-STICK_D says 0).
  Pieces: each run cut at the A-gains of the class (FREEZE-A's hypothesis holds on each piece; pieces, long_pieces).
  Also FREEZEA_V: on a long piece, a state t >= s + |A_s| - 1 and z in A_t with M_t(z) != M_{s+|A_s|-1}(z) (Theorem FREEZE-A (b) says 0;
  vacuous unless runs are long; the index is s + |A_s| - 1), and ROOTA_V: transitions after the freeze index at which q in Q_c with sigma-bar(q) in A at both ends
  changes M(q) more than deg(q) - 1 times on the run (FREEZE-A (c)).
Also BFA_V: FREEZE-A (a) at every state of every monotone class-run (bfa_checks, bfa_eq = binding checks, bfa_unk = DFS budget out).\nControl MUT2=1: one more edge than (a) allows (must bite). Control MUT=1: freeze index s in place of s + |A_s| - 1 (must bite on a set with long monotone runs).
Usage: shrink.py --one GAME [START] | --list FILE [KMIN] (env RS, NMAX)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import *
C = Counter(); VIOL = []; TOP = []; MUT2 = os.environ.get("MUT2") == "1"

def bfa(g, E, A, Aset, c, j, name):
    """FREEZE-A (a) at one state: M_t(z) >= the best weight of a simple path of G[A_t] from z to c with <= j edges. Walk Bellman-Ford gives an
    upper estimate; only when it exceeds M_t(z) is a simple witness searched by bounded DFS (UNK if the budget runs out)."""
    if c not in Aset: return
    adj = {v: ([x for x in set(g.succ[v]) if x in Aset] if g.owner[v] == 0 else ([A["t"][v]] if A["t"][v] in Aset else [])) for v in Aset if v != c}
    NEG = None; B = {v: NEG for v in Aset}; B[c] = 0
    for _ in range(j):
        B2 = dict(B)
        for v, xs in adj.items():
            for x in xs:
                if B[x] is not None and (B2[v] is None or wt(E, v, c) + B[x] > B2[v]): B2[v] = wt(E, v, c) + B[x]
        B = B2
    for z in Aset:
        C["bfa_checks"] += 1; mz = M(E, A["vs"][z])
        if B[z] is None or B[z] <= mz:
            C["bfa_eq"] += (B[z] == mz); continue
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
        if budget[0] < 0: C["bfa_unk"] += 1
        elif best[0] is not None and best[0] > mz: C["BFA_V"] += 1; VIOL.append(("BFA", name, z, j, best[0], mz))

def run(g, name, start=None):
    E, R = rows(g, start); Q = {v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2}
    for i, j in phases(R):
        cls = {}
        for v in range(g.n): cls.setdefault(R[i]["vs"][v][0], set()).add(v)
        k = i
        while k < j:
            if R[k]["fb"]: k += 1; continue
            s = k
            while k < j and not R[k]["fb"]: k += 1
            e = k                                  # states s..e, transitions s..e-1 all S4a
            C["runs"] += 1; mono = True; inrun = 0
            AS = [avoid(R[t]["wn"], Dset(g, R[t]), g.n) for t in range(s, e + 1)]
            for c, U in cls.items():
                if len(U) < 2: continue
                for t in range(s, e):
                    A0, A1 = AS[t - s] & U, AS[t - s + 1] & U
                    for z in A1 - A0:
                        mono = False; inrun += 1; C["IN"] += 1
                        D0, D1 = Dset(g, R[t]), Dset(g, R[t + 1]); u = first_D(R[t]["wn"], z, D0)
                        C["IN_DLEAVE" if (u is not None and u not in D1) else "IN_SWITCH"] += 1
                        if R[t]["W"][z][0] != R[t]["vs"][z][0]: C["SPLIT_IN"] += 1; VIOL.append(("SPLIT_IN", name, t - i, z))
                cuts = [t for t in range(s, e) if not AS[t - s + 1] & U <= AS[t - s] & U]
                bounds = [s] + [t + 1 for t in cuts]; ends = cuts + [e]
                for ps, pe in zip(bounds, ends):       # pieces [ps, pe]: A non-increasing, no fallback (FREEZE-A's hypothesis)
                    if pe <= ps: continue
                    C["pieces"] += 1
                    for t in range(ps, pe + 1): bfa(g, E, R[t], AS[t - s] & U, c, t - ps + (1 if MUT2 else 0), name)
                    L = max(len(AS[ps - s] & U) - 1, 0)
                    if pe - ps > L:
                        C["long_pieces"] += 1; base = ps if os.environ.get("MUT") == "1" else ps + L
                        for t in range(base, pe + 1):
                            for z in AS[t - s] & U:
                                if M(E, R[t]["vs"][z]) != M(E, R[base]["vs"][z]): C["FREEZEA_V"] += 1; VIOL.append(("FREEZEA", name, t, z))
                        for q in Q & U:
                            if q == c: continue
                            ch = sum(1 for t in range(base, pe) if R[t]["sb"][q] in AS[t - s] and R[t + 1]["sb"][q] in AS[t - s + 1]
                                     and M(E, R[t]["vs"][q]) != M(E, R[t + 1]["vs"][q]))
                            if ch > len(set(g.succ[q])) - 1: C["ROOTA_V"] += 1; VIOL.append(("ROOTA", name, q, ch))
            C["runs_mono"] += mono
            if inrun: TOP.append((inrun, e - s, name, i))

def main():
    a = sys.argv[1:]
    if a[0] == "--one":
        g = load(a[1]); run(g, a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        kmin = int(a[2]) if len(a) > 2 else 1
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
    for x in sorted(TOP, reverse=True)[:5]: print("TOP IN/runlen", x)
    for v in VIOL[:8]: print("VIOLATION", v)
    print("SHRINK PASS" if not VIOL else "SHRINK FAIL")

if __name__ == "__main__":
    main()
