#!/usr/bin/env python3
"""L-RED R170 FREEZE check (TWO-FIX windows, L-NEW box 121 Lemma TWO-FIX).
For every TWO-FIX window [a, b] of the N5 run on G (tau and sbar = si.Engine's optimal Odd counterstrategy to sigma both constant
on states a..b), build G_F := G with every Odd vertex v where sbar(v) = tau(v) cut down to the single edge v -> tau(v) (the ODIFF
vertices keep all their edges), and run N5 (n5x.step, SPEC S1-S5) on G_F from the start pair (sigma_a, tau_a).
Reports, per window of length >= MINL (env, default 2): L, ODIFF, the number of Odd choice vertices of G_F (outdeg > 1), whether the
first L states of the G_F run equal the window's states (REPLAY), the length of the whole G_F run (FRUN), and FFSEG := the longest run
of consecutive window transitions without an S4c fallback.
Usage: freeze.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg

def run(g, s, t, cap=10 ** 6):
    E, Ed = Engine(g), Engine(dual(g)); S, T, F = [tuple(s)], [tuple(t)], [0]
    while len(S) - 1 < cap:
        r = step(g, E, Ed, list(S[-1]), list(T[-1]))
        if r is None: break
        S.append(tuple(r[0])); T.append(tuple(r[1])); F.append(r[4])
    return S, T, F, E

def windows(g, S, T, E):
    n, own = g.n, g.owner
    SB = [tuple(-1 if own[v] == 0 else E.evaluate(x)[1][v] for v in range(n)) for x in S]
    K = len(S) - 1; w = []; k = 0
    while k < K:
        if T[k + 1] != T[k] or SB[k + 1] != SB[k]: k += 1; continue
        a = k
        while k < K and T[k + 1] == T[k] and SB[k + 1] == SB[k]: k += 1
        w.append((a, k))
    return w, SB

def frozen(g, sb, tau):
    succ = [list(g.succ[v]) if g.owner[v] == 0 or sb[v] != tau[v] else [tau[v]] for v in range(g.n)]
    return pg.Game(list(g.prio), list(g.owner), succ)

def main():
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
    E0, Ed0 = Engine(g), Engine(dual(g)); s, t = start_pair(g, E0, Ed0, st)
    S, T, F, E = run(g, s, t); W, SB = windows(g, S, T, E)
    minl = int(os.environ.get("MINL", "2")); nm = os.path.basename(sys.argv[1]); allok = True; best = 0
    print(f"FREEZE {nm} n {g.n} K {len(S) - 1} fallbacks {sum(F)} windows {len(W)}")
    for a, b in W:
        L = b - a
        if L < minl: continue
        gf = frozen(g, SB[a], T[a]); od = sum(1 for v in range(g.n) if g.owner[v] == 1 and SB[a][v] != T[a][v])
        och = sum(1 for v in range(g.n) if g.owner[v] == 1 and len(gf.succ[v]) > 1)
        FS, FT, FF, _ = run(gf, S[a], T[a], cap=10 ** 5)
        ok = len(FS) > L and all(FS[i] == S[a + i] and FT[i] == T[a + i] for i in range(L + 1))
        allok &= ok; best = max(best, L)
        seg = cur = 0
        for j in range(a + 1, b + 1):
            cur = 0 if F[j] else cur + 1; seg = max(seg, cur)
        print(f"  window [{a}, {b}] L {L} ODIFF {od} oddchoice(G_F) {och} fb_in_window {sum(F[a + 1:b + 1])} FFSEG {seg} REPLAY {ok} FRUN {len(FS) - 1}")
    print(f"FREEZE {nm} longest {best} all_replay {allok}")

if __name__ == "__main__":
    main()
