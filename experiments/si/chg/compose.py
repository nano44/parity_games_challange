#!/usr/bin/env python3
"""L-SI box 28 (docs/si/N5-CHG-box28.md §9): the composition of Lead 11:01Z (STEP 2, option D), measured per PHASE (lambda_Xi and tau
constant, RESULTS R38 (a) KEY; in-phase S4c fallbacks included) with every inequality's slack:
  L                      phase length (transitions)
  (I0) L <= SWS := sum_v SW(v)                                   every in-phase transition changes sigma (tau is constant)
  (I1) SW(v) = sum_c ENT(v, c), ENT(v, c) <= 1 + RISE(c)        Lemma SW-RETURN (re-entry into c only after Xi(c) rose)
  (I2) RISE(c) <= PCH(c) + (PCH(c) + 1)(n - 1)                   Lemma LEN-MONO (between P-changes the length moves one way)
  (I3) PCH(c) <= (K(K+1)/2)(NM(c) + 1) + NM(c)                   L-LIT's Lemma MATCH-Phi (packet P-N5-MATCHPHI / P-N5-MPGS (A))
Counters (*_V a failure): I0_V, I1_V, LDIR_V (length moves the wrong way under a fixed P, or Xi falls), LBLK_V (> n - 1 length-only rises
in one P-block), I2_V, I3_V. NM(c) = carries: P-changes A -> B that are not MATCHED (T33 §1.2; decided by two maximum matchings, the
Mendelsohn-Dulmage theorem: a matching covering the even outgoing and the odd incoming ranks exists iff one covering each side does).
MODE=run: Corollary COMPOSE-RUN on the whole run (Even switches on lambda_Xi-runs, Odd switches on lambda_U-runs of the dual valuation
U of tau on G^d): RUNI0_V (run length > Even + Odd switches), EI1/OI1, ELDIR/OLDIR, ELBLK/OLBLK; TOP columns then read L, game, 0, T,
switches + B, sum (1 + RISE) + B, sum n (PCH + 1) + B, -, Even switches, Odd switches, B_Xi, B_U, n (B = lambda-change transitions).
fall_dK / fallmax_dK: P-changes at which Phi_d := sum of signed pos^d (d = 1, 2, 3) does not rise (all, and the most for one
vertex in one phase); CONJECTURE PHI-d-MONO would say fall_dK = 0 under S4a for some fixed d (it would bound PCH by the range n^(d+1)).
Prints per phase the sums S1 = sum_v SW(v), S2 = sum_(v,c) (1 + RISE(c)), S3 = sum_(v,c) (1 + PCH(c) + (PCH(c)+1)(n-1)),
S4 = the same with the MATCH-Phi bound for PCH; and the maxima of NM, PCH, RISE. Usage: compose.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart, phases, Engine, dual
C = Counter(); EX = []; TOP = []

def maxmatch(L, Rr, ok):
    own = {}
    def aug(x, seen):
        for y in Rr:
            if ok(x, y) and y not in seen:
                seen.add(y)
                if y not in own or aug(own[y], seen): own[y] = x; return True
        return False
    return sum(aug(x, set()) for x in L)

def matched(A, B, w, odd):
    outs, ins = A - B, B - A
    mo = [o for o in outs if not odd(o)]; mi = [i for i in ins if odd(i)]
    if maxmatch(mo, sorted(ins), lambda o, i: w(i) > w(o)) < len(mo): return False
    return maxmatch(mi, sorted(outs), lambda i, o: w(i) > w(o)) == len(mi)

def bits(m):
    out, r = set(), 0
    while m:
        if m & 1: out.add(r)
        m >>= 1; r += 1
    return frozenset(out)

def _run(E, g, R, name):
    n = g.n; rk2v = {E.rank[v]: v for v in range(n)}; odd = lambda r: E.par[rk2v[r]] == 1
    for i, j in phases(R):
        L = j - i; sw = Counter(); ent = Counter(); rise = Counter(); pch = Counter(); nm = Counter(); fall = Counter()
        for t in range(i, j):
            A, B = R[t], R[t + 1]
            for v in range(n):
                if g.owner[v] == 0 and A["s"][v] != B["s"][v]: sw[v] += 1; ent[(v, B["s"][v])] += 1
        for x in range(n):
            blk = 0
            for t in range(i, j):
                a, b = R[t]["vs"][x], R[t + 1]["vs"][x]
                if a == b: continue
                rise[x] += 1; c = a[0]
                if b[0] != c: C["LDIR_V"] += 1; EX.append(("LDIR", name, i, j, t, x, "cycle node")); continue
                if a[1] != b[1]:
                    pch[x] += 1; blk = 0
                    if E.weight(b[1]) <= E.weight(a[1]): C["LDIR_V"] += 1; EX.append(("LDIR", name, i, j, t, x, "P falls"))
                    rc = E.rank[c]; w = lambda r: (r - rc) if not odd(r) else -(r - rc)
                    if not matched(bits(a[1]), bits(b[1]), w, odd): nm[x] += 1
                    for d in (1, 2, 3):                 # Phi_d: signed pos^d weights; a FALL is a P-change with Phi_d not rising
                        wd = lambda r: (r - rc) ** d if not odd(r) else -((r - rc) ** d)
                        if sum(map(wd, bits(b[1]))) - sum(map(wd, bits(a[1]))) <= 0: C["fall_d%d" % d] += 1; fall[(d, x)] += 1
                else:
                    blk += 1
                    better = (b[2] < a[2]) if E.par[c] == 0 else (b[2] > a[2])
                    if not better: C["LDIR_V"] += 1; EX.append(("LDIR", name, i, j, t, x, "length", a[2], b[2]))
                    if blk > n - 1: C["LBLK_V"] += 1
            K = sum(1 for r in range(n) if r > E.rank[R[i]["vs"][x][0]])
            if rise[x] > pch[x] + (pch[x] + 1) * (n - 1): C["I2_V"] += 1; EX.append(("I2", name, i, j, x, rise[x], pch[x]))
            if pch[x] > (K * (K + 1) // 2) * (nm[x] + 1) + nm[x]: C["I3_V"] += 1; EX.append(("I3", name, i, j, x, pch[x], nm[x], K))
        S1 = sum(sw.values())
        if L > S1: C["I0_V"] += 1; EX.append(("I0", name, i, j, L, S1))
        for (v, c), e in ent.items():
            if e > 1 + rise[c]: C["I1_V"] += 1; EX.append(("I1", name, i, j, v, c, e, rise[c]))
        Ev = [v for v in range(n) if g.owner[v] == 0 and sw[v]]
        pairs = [(v, c) for v in Ev for c in set(g.succ[v])]
        S2 = sum(1 + rise[c] for v, c in pairs)
        S3 = sum(1 + pch[c] + (pch[c] + 1) * (n - 1) for v, c in pairs)
        def mb(c):
            K = sum(1 for r in range(n) if r > E.rank[R[i]["vs"][c][0]]); return (K * (K + 1) // 2) * (nm[c] + 1) + nm[c]
        S4 = sum(1 + mb(c) + (mb(c) + 1) * (n - 1) for v, c in pairs)
        for d in (1, 2, 3): C["fallmax_d%d" % d] = max(C["fallmax_d%d" % d], max((fall[(d, x)] for x in range(n)), default=0))
        C["phases"] += 1; C["nm_max"] = max(C["nm_max"], max(nm.values(), default=0)); C["pch_max"] = max(C["pch_max"], max(pch.values(), default=0))
        TOP.append((L, name, i, j, S1, S2, S3, S4, max(nm.values(), default=0), max(pch.values(), default=0), max(rise.values(), default=0), max(sw.values(), default=0), n))

def side(E, g, R, vals, own, key, name, tag):
    """one player's half of Corollary COMPOSE-RUN: over maximal runs of states with that player's cycle-node map constant (lambda-runs),
    switches of that player's vertices, and the bound sum_(v, c) (1 + RISE(c)) <= sum_(v, c) n (PCH(c) + 1); returns (switches, bound)."""
    n = g.n; rk2v = {E.rank[v]: v for v in range(n)}; odd = lambda r: E.par[rk2v[r]] == 1; T = len(R) - 1
    lam = [tuple(x[0] for x in vals[t]) for t in range(T + 1)]; tot_sw = tot_b2 = tot_b3 = 0; i = 0; nruns = 0
    while i < T:
        j = i
        while j < T and lam[j + 1] == lam[i]: j += 1
        nruns += 1
        if j > i:
            sw = Counter(); ent = Counter(); rise = Counter(); pch = Counter()
            for t in range(i, j):
                for v in range(n):
                    if g.owner[v] == own and R[t][key][v] != R[t + 1][key][v]: sw[v] += 1; ent[(v, R[t + 1][key][v])] += 1
            for x in range(n):
                blk = 0
                for t in range(i, j):
                    a, b = vals[t][x], vals[t + 1][x]
                    if a == b: continue
                    rise[x] += 1
                    if a[1] != b[1]:
                        pch[x] += 1; blk = 0
                        if E.weight(b[1]) <= E.weight(a[1]): C[tag + "LDIR_V"] += 1; EX.append((tag + "LDIR", name, i, j, t, x))
                    else:
                        blk += 1
                        if not ((b[2] < a[2]) if E.par[a[0]] == 0 else (b[2] > a[2])): C[tag + "LDIR_V"] += 1; EX.append((tag + "LDIR", name, i, j, t, x))
                        if blk > n - 1: C[tag + "LBLK_V"] += 1
            for (v, c), e in ent.items():
                if e > 1 + rise[c]: C[tag + "I1_V"] += 1; EX.append((tag + "I1", name, i, j, v, c, e, rise[c]))
            pairs = [(v, c) for v in range(n) if g.owner[v] == own and sw[v] for c in set(g.succ[v])]
            tot_sw += sum(sw.values()); tot_b2 += sum(1 + rise[c] for v, c in pairs); tot_b3 += sum(n * (pch[c] + 1) for v, c in pairs)
            C[tag + "pch_max"] = max(C[tag + "pch_max"], max(pch.values(), default=0))
        i = j + 1 if j > i else i + 1
    C[tag + "lambda_runs_max"] = max(C[tag + "lambda_runs_max"], nruns)
    bnd = sum(1 for t in range(T) if lam[t] != lam[t + 1])          # lambda-change transitions (<= n(n - 1), RESULTS R47 (a))
    return tot_sw, tot_b2, tot_b3, bnd

def runmode(E, g, R, name):
    """Corollary COMPOSE-RUN: the whole run, Even side on lambda_Xi-runs, Odd side on lambda_U-runs (dual valuations of tau on G^d)."""
    Ed = Engine(dual(g)); U = [Ed.evaluate(tuple(r["t"]))[0] for r in R]; T = len(R) - 1
    se, be2, be3, bE = side(E, g, R, [r["vs"] for r in R], 0, "s", name, "E")
    so, bo2, bo3, bO = side(Ed, g, R, U, 1, "t", name, "O")
    C["runs"] += 1
    if T > se + so + bE + bO: C["RUNI0_V"] += 1; EX.append(("RUNI0", name, T, se, so, bE, bO))
    if bE > g.n * (g.n - 1) or bO > g.n * (g.n - 1): C["R47_V"] += 1
    TOP.append((T, name, 0, T, se + so + bE + bO, be2 + bo2 + bE + bO, be3 + bo3 + bE + bO, 0, se, so, bE, bO, g.n))

def run(g, name, start=None):
    E, R = rows(g, start, cap=20000)
    if os.environ.get("MODE") == "run": runmode(E, g, R, name)
    else: _run(E, g, R, name)

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
                except Exception: C["SKIPPED_input"] += 1
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    print("columns: L, game, i, j, S1 = sum SW, S2 = sum (1 + RISE), S3 = (I2) bound, S4 = (I3) bound, max NM, max PCH, max RISE, max SW, n")
    for z in sorted(TOP, key=lambda z: (-z[0], z[1]))[:6]: print("TOP", z)
    if TOP and os.environ.get("MODE") != "run":
        z = max(TOP, key=lambda z: (z[8] / z[12], z[1])); print("NMTOP (max NM / n)", round(z[8] / z[12], 3), z)
        z = max(TOP, key=lambda z: (z[9] / z[12], z[1])); print("PCHTOP (max PCH / n)", round(z[9] / z[12], 3), z)
    if TOP: print("MAXRATIO L/S1 %.3f  S1/S2 %.3f" % (max(z[0] / max(1, z[4]) for z in TOP), max(z[4] / max(1, z[5]) for z in TOP)))
    for z in EX[:8]: print("EXAMPLE", z)
    ks = ("RUNI0", "R47", "EI1", "OI1", "ELDIR", "OLDIR", "ELBLK", "OLBLK") if os.environ.get("MODE") == "run" else ("I0", "I1", "LDIR", "LBLK", "I2", "I3")
    for k in ks: print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__":
    main()
