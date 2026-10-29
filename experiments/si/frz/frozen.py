#!/usr/bin/env python3
"""L-SI box 29 (docs/si/N5-FRZ-box29.md): sigma-bar-FROZEN PIECES of N5 phases. A piece is a maximal stretch [a, b] of a phase (lambda_Xi,
tau constant) on which sigma-bar (Odd's optimal counterstrategy to sigma_t, the honest frame) is constant. On a piece Xi_t = val(sigma_t,
sigma-bar) in G1 := G with Odd fixed to sigma-bar, W_t = val(sigma_t, tau) in G2 := G with Odd fixed to tau; D := Odd u with sigma-bar(u) != tau(u).
Per piece: L (transitions), |D|, ESW (Even switches), WCH (W-changing transitions), XCH (Xi-changing transitions), SWmax (most switches
of one Even vertex), NMx (most Xi-carries of one vertex), NMw (most W-carries of one vertex), DPLAY (Even vertices whose W-play meets D at
a), and checks: WMON_V (W falls somewhere), XMON_V (Xi falls), ARENA_V (a switch outside sigma_t + I_t).
Usage: frozen.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "root")); sys.path.insert(0, os.path.join(HERE, "..", "chg"))
from common import rows, load, readstart, phases, Engine
from compose import matched, bits
C = Counter(); TOP = []; EXT = []

def pieces(R, i, j):
    a = i
    while a < j:
        b = a
        while b + 1 <= j and R[b + 1]["sb"] == R[a]["sb"]: b += 1
        if b > a: yield a, b
        a = b + 1 if b > a else a + 1

def carries(E, g, R, a, b, key, skipfb=False):
    """per vertex: carries (unmatched P-changes), P-changes, rises, cycle-node changes; skipfb: ignore S4c fallback transitions."""
    n = g.n; rk2v = {E.rank[v]: v for v in range(n)}; odd = lambda r: E.par[rk2v[r]] == 1; nm = Counter(); pc = Counter(); ri = Counter(); cn = Counter()
    for x in range(n):
        for t in range(a, b):
            if skipfb and R[t]["fb"]: continue
            p, q = R[t][key][x], R[t + 1][key][x]
            if p != q: ri[x] += 1
            if p[0] != q[0]: cn[x] += 1
            if p == q or p[0] != q[0] or p[1] == q[1]: continue
            pc[x] += 1
            rc = E.rank[p[0]]; w = lambda r: (r - rc) if not odd(r) else -(r - rc)
            if not matched(bits(p[1]), bits(q[1]), w, odd): nm[x] += 1
    return nm, pc, ri, cn

def _run(E, g, R, name):
    n = g.n; m = sum(len(set(g.succ[v])) for v in range(n))
    for i, j in phases(R):
        for a, b in pieces(R, i, j):
            D = {u for u in range(n) if g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u]}
            esw = wch = xch = 0; sw = Counter()
            for t in range(a, b):
                A, B = R[t], R[t + 1]
                for v in range(n):
                    if g.owner[v] == 0 and A["s"][v] != B["s"][v]:
                        sw[v] += 1; esw += 1
                wch += A["W"] != B["W"]; xch += A["vs"] != B["vs"]
                for v in range(n):
                    if E.key(B["W"][v]) < E.key(A["W"][v]): C["WMON_V"] += 1
                    if E.key(B["vs"][v]) < E.key(A["vs"][v]): C["XMON_V"] += 1
            nmx = carries(E, g, R, a, b, "vs")[0]; nmw, pcw, riw, cnw = carries(E, g, R, a, b, "W", True)
            fb = sum(R[t]["fb"] for t in range(a, b)); wsame = sum(1 for t in range(a, b) if not R[t]["fb"] and R[t]["W"] == R[t + 1]["W"])
            C["fb_in_pieces"] += fb; C["Wsame_nonfb"] += wsame; C["Wcyclenode_changes_nonfb"] += sum(cnw.values())
            EXT.append((b - a, name, a, b, len(D), fb, max(nmw.values(), default=0), max(pcw.values(), default=0), max(riw.values(), default=0), sum(riw.values()), g.n))
            L = b - a; C["pieces"] += 1; C["pieces_D%d" % min(len(D), 2)] += 1
            if not D and (L >= n + m): C["D0_V"] += 1
            TOP.append((L, name, a, b, len(D), esw, wch, xch, max(sw.values(), default=0), max(nmx.values(), default=0),
                        max(nmw.values(), default=0), n, m, j - i))

def run(g, name, start=None):
    E, R = rows(g, start, cap=20000); _run(E, g, R, name)

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p:
                f = os.path.join(ROOT, p[0]) if os.path.exists(os.path.join(ROOT, p[0])) else os.path.join(ROOT, "experiments", p[0])
                s = None
                if len(p) > 1 and os.environ.get("START") == "1":
                    s = os.path.join(ROOT, p[1]) if os.path.exists(os.path.join(ROOT, p[1])) else os.path.join(ROOT, "experiments", p[1])
                try: run(load(f), p[0], readstart(s) if s else None)
                except Exception as e: C["SKIPPED_input"] += 1
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    print("columns: L, game, a, b, |D|, ESW, WCH, XCH, SWmax, NMx, NMw, n, m, phase length")
    for z in sorted(TOP, key=lambda z: -z[0])[:6]: print("TOP", z)
    for d in (0, 1, 2):
        Z = [z for z in TOP if min(z[4], 2) == d]
        if Z:
            z = max(Z, key=lambda z: z[0] / z[11]); print("D%s max L/n = %.3f" % (d if d < 2 else "2+", z[0] / z[11]), z)
            z = max(Z, key=lambda z: z[9] / z[11]); print("D%s max NMx/n = %.3f" % (d if d < 2 else "2+", z[9] / z[11]), z)
    if TOP:
        z = max(TOP, key=lambda z: z[0] / ((z[4] + 1) * z[11])); print("max L/((|D|+1) n) = %.3f" % (z[0] / ((z[4] + 1) * z[11])), z)
        z = max(TOP, key=lambda z: z[8] / z[11]); print("max SWmax/n = %.3f" % (z[8] / z[11]), z)
    print("EXT columns: L, game, a, b, |D|, fallbacks, NMw(non-fb), PCHw max, RISEw max, sum RISEw, n")
    for z in sorted(EXT, key=lambda z: -z[0])[:4]: print("EXT", z)
    if EXT:
        z = max(EXT, key=lambda z: z[6]); print("EXT max NMw", z); z = max(EXT, key=lambda z: z[8] / z[10]); print("EXT max RISEw/n %.3f" % (z[8] / z[10]), z)
    for k in ("WMON", "XMON", "D0"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__":
    main()
