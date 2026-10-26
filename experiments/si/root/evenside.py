#!/usr/bin/env python3
"""L-SI box 22 (successor 18): DATA for docs/si/N5-EXIT-box22.md §8 (the Even side). Per phase, fallback-free run S and class c (as gcx.py:
|U_c| >= 3, Q_c nonempty), the per-class C-intervals of gcx.py (A non-increasing, D cap U_c constant, every D-direct offset constant) and the
C-CUTS (transitions in no C-interval). Each cut is classified (first match):
  AG     A grows;
  DCH    D cap U_c changes (necessarily a sigma-bar change at a gate, since tau is constant on the phase);
  OSB    an offset changes at a gate u whose sigma-bar(u) changes (an Odd choice change at a D-direct gate);
  DDSET  the set of D-direct gates changes with D fixed;
  OVAL   an offset changes with sigma-bar fixed at every changed gate (values below the gate moved).
Activity inside C-intervals: ESW_in (Even switches in U_c at transitions inside a C-interval), LASTSW_max (the largest index of an Even switch
inside its C-interval, 0-based), EXIT_at_cut / EXIT_in (exit-change transitions, exitx.py's par, at cuts / inside C-intervals),
SB_at_cut / SB_in (sigma-bar changes in Q_c at cuts / inside), and SBG (sigma-bar changes at vertices of D_t cup D_t+1, i.e. at gates).
E1MUT=1: E-ONEWAY's window conditions dropped (returns must then appear: control).
PURELATE: an Even switch at index >= |A_a| - 1 + |U_c| inside a C-interval pure at all its states (the READING of N5-ABSCYC §4
says none; a hit would refute the lift).
Usage: evenside.py --one GAME [START] | --list FILE [KMIN] (env RS, NMAX)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import rows, phases, load, readstart
import gcx, exitx
C = Counter()

def run(g, name, start=None):
    E, R = rows(g, start); Qs = {v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2}
    for i, j in phases(R):
        cls = {}
        for v in range(g.n): cls.setdefault(R[i]["vs"][v][0], set()).add(v)
        runs, s = [], i
        for k in range(i, j):
            if R[k]["fb"]: runs.append((s, k)); s = k + 1
        runs.append((s, j))
        for c, U in cls.items():
            Qc = {q for q in Qs if q in U and q != c}
            if len(U) < 3 or not Qc: continue
            I = {k: gcx.state_info(g, R[k], U, Qc) for k in range(i, j + 1)}
            OF = {k: gcx.offs(E, R[k], I[k][3]) for k in range(i, j + 1)}
            P = {k: {x: exitx.par(R[k], x, c, Qs) for x in Qc} for k in range(i, j + 1)}
            for s, e in runs:
                if e <= s: continue
                C["runs"] += 1; a = s; K = 0
                pure = lambda k: (I[k][0] & U) == I[k][3]
                for k in range(s, e):
                    D0, A0, fd0, DD0 = I[k]; D1, A1, fd1, DD1 = I[k + 1]
                    sbch = {q for q in Qc if R[k]["sb"][q] != R[k + 1]["sb"][q]}
                    sw = [w for w in U if g.owner[w] == 0 and R[k]["s"][w] != R[k + 1]["s"][w]]
                    exch = any(P[k][x] != P[k + 1][x] for x in Qc)
                    sbg = {q for q in sbch if q in D0 or q in D1}
                    cut = True
                    if not A1 <= A0: C["cut_AG"] += 1
                    elif (D0 & U) != (D1 & U): C["cut_DCH"] += 1
                    elif OF[k] != OF[k + 1]:
                        chg = {u for u in set(OF[k]) | set(OF[k + 1]) if OF[k].get(u) != OF[k + 1].get(u)}
                        if DD0 != DD1: C["cut_DDSET"] += 1
                        elif chg & sbch: C["cut_OSB"] += 1
                        else: C["cut_OVAL"] += 1
                    else: cut = False
                    tag = "at_cut" if cut else "in"
                    C["EXIT_" + tag] += exch; C["SB_" + tag] += len(sbch); C["SBG_" + tag] += len(sbg)
                    C["trans_" + tag] += 1
                    if cut: K += 1; a = k + 1
                    else:
                        C["ESW_in"] += len(sw)
                        if sw:
                            allpure = all(pure(m) for m in range(a, k + 2))
                            lim = len(I[a][1]) - 1 + len(U)          # READING (N5-ABSCYC §4): no switch at index >= |A_a| - 1 + |U_c| in a pure interval
                            C["sw_in_" + ("pure" if allpure else "impure")] += 1
                            if allpure and k - a >= lim: C["PURELATE"] += 1; print("PURELATE", name, i, s, a, k, len(U))
                            if allpure: C["pure_lastsw_max"] = max(C["pure_lastsw_max"], k - a)
                        if sw: C["LASTSW_max"] = max(C["LASTSW_max"], k - a); C["lastsw_minus_U_max_plus1000"] = max(C["lastsw_minus_U_max_plus1000"], 1000 + k - a - len(U))
                C["K_sum"] += K; C["K_max"] = max(C["K_max"], K)
                # Lemma E-ONEWAY: w switches a -> b at k with a's exit e1 on b's (k+1)-play; a later return to a at k2 with a's class exit path
                # and exit fixed on [k, k2] and e1 on w's play at every state of [k+1, k2] must not happen (E1_V); E1_chk counts the windows.
                T = Qc | {c}
                def cep(S, y):
                    pl = exitx.hplay(S, y, c) + [c]; idx = next(ii for ii, z in enumerate(pl) if z in T); return tuple(pl[:idx + 1])
                for k in range(s, e):
                    for w in U:
                        if g.owner[w] != 0 or w == c or R[k]["s"][w] == R[k + 1]["s"][w]: continue
                        a_, b_ = R[k]["s"][w], R[k + 1]["s"][w]; pa = cep(R[k], a_); e1 = pa[-1]
                        if e1 not in exitx.hplay(R[k + 1], b_, c) + [c]: continue
                        for k2 in range(k + 1, e):
                            if os.environ.get("E1MUT") != "1" and (cep(R[k2], a_) != pa or e1 not in exitx.hplay(R[k2], w, c) + [c]): break
                            if R[k2]["s"][w] != R[k2 + 1]["s"][w]:
                                C["E1_chk"] += 1
                                if R[k2 + 1]["s"][w] == a_ and (os.environ.get("E1MUT") == "1" or cep(R[k2 + 1], a_) == pa):
                                    C["E1_V"] += 1
                                    if os.environ.get("E1MUT") != "1": print("E1_V", name, k, k2, w)
                                break

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        kmin = int(a[2]) if len(a) > 2 else 1; ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            f = line.split()[0] if line.strip() and not line.startswith("#") else None
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin: continue
            run(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                run(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                   {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))

if __name__ == "__main__":
    main()
