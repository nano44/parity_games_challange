#!/usr/bin/env python3
"""L-RED R171: fallbacks inside TWO-FIX windows. Per window [a, b] (tau and sbar constant, as L-NEW box 121): L, FB (S4c fallbacks),
XO (window transitions changing Xi at a vertex of O := {Odd v : sbar(v) != tau(v)}, as L-NEW box 123), ODIFF = |O|, and the maximal
fallback-free stretch. Usage: fbscore.py G.pg [START|-]  (one FBS line per window with L >= MINL, env, default 1; then a BEST line =
the window with the most fallbacks). Importable: windows_fb(g, s, t, cap) -> (list of dicts, K)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual

def windows_fb(g, s, t, cap=20000):
    n, own = g.n, g.owner
    E, Ed = Engine(g), Engine(dual(g)); S, T, F, X = [tuple(s)], [tuple(t)], [0], []
    v0, sb0 = E.evaluate(tuple(s)); X.append(v0); SB = [tuple(sb0[v] if own[v] == 1 else -1 for v in range(n))]
    while len(S) - 1 < cap:
        r = step(g, E, Ed, list(S[-1]), list(T[-1]))
        if r is None: break
        S.append(tuple(r[0])); T.append(tuple(r[1])); F.append(r[4])
        vx, sb = E.evaluate(S[-1]); X.append(vx); SB.append(tuple(sb[v] if own[v] == 1 else -1 for v in range(n)))
    K = len(S) - 1; out = []; k = 0
    while k < K:
        if T[k + 1] != T[k] or SB[k + 1] != SB[k]: k += 1; continue
        a = k
        while k < K and T[k + 1] == T[k] and SB[k + 1] == SB[k]: k += 1
        O = [v for v in range(n) if own[v] == 1 and SB[a][v] != T[a][v]]
        xo = sum(1 for j in range(a, k) if any(X[j + 1][v] != X[j][v] for v in O))
        seg = cur = 0
        for j in range(a + 1, k + 1):
            cur = 0 if F[j] else cur + 1; seg = max(seg, cur)
        out.append(dict(a=a, b=k, L=k - a, FB=sum(F[a + 1:k + 1]), XO=xo, ODIFF=len(O), FFSEG=seg))
    return out, K

def main():
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
    s, t = start_pair(g, Engine(g), Engine(dual(g)), st); W, K = windows_fb(g, s, t)
    nm = os.path.basename(sys.argv[1]); minl = int(os.environ.get("MINL", "1"))
    for w in W:
        if w["L"] >= minl: print(f"FBS {nm} n {g.n} K {K} [{w['a']}, {w['b']}] L {w['L']} FB {w['FB']} XO {w['XO']} ODIFF {w['ODIFF']} FFSEG {w['FFSEG']}")
    if W:
        w = max(W, key=lambda w: (w["FB"], w["L"]))
        print(f"BEST {nm} n {g.n} K {K} FB {w['FB']} XO {w['XO']} L {w['L']} ODIFF {w['ODIFF']} FB/n {w['FB'] / g.n:.3f} FB/((XO+1)n) {w['FB'] / ((w['XO'] + 1) * g.n):.3f}")

if __name__ == "__main__":
    main()
