#!/usr/bin/env python3
"""L-NEW box 53: LINEAR RANKING-FUNCTION search for N5 (Podelski-Rybalchenko style, read as a potential): find coefficients c with
c . (f(s_{t+1}) - f(s_t)) >= 1 at EVERY transition of a corpus (f = feat.py's features; c increasing = a ranking function -c decreasing).
Modes:
  uni   one c over the 24 UNIFORM features, shared by every transition of every game in the corpus;
  pv    per game, one c over its 21n PER-VERTEX features plus the 24 uniform ones (non-uniform; infeasible => no linear ranking function
        over these features on that game at all);
  rk    per game, PER-RANK features (feat.py), the least L-infinity norm of a ranking c (growth along families);
  uni1  the uni LP separately for each game of the corpus;
  lex   lexicographic (uniform features): rounds of an LP that keeps every remaining transition non-decreasing and makes as many as possible
        strictly increasing (>= 1); those are removed; depth = rounds until none remain, or STUCK.
Certificates (exact, integer, re-checked in pure Python by cert.py): FEASIBLE -> integer c with c.Delta >= 1 everywhere; INFEASIBLE ->
integer y >= 0 on transitions (Farkas) with sum_t y_t Delta_t = 0 exactly and sum y > 0. Written to experiments/new/out/box53/NAME.json (gitignored); compact pins via mkcert.py into box53/cert/.
Corpus spec (any mix): GAME.pg[:START] | rand:K:SEED:NMIN:NMAX | list:FILE (L-SI list format) | dual:GAME.pg (the dual game, S3 start).
Feature family: FAM=0 (default) the 24 uniform features, FAM=4 the 24 moment features (feat.MNAMES), FAM=5 both (45), FAM=6 the edge bits, FAM=7 the 45 + edge bits (6, 7: per game only, mode uni1).
Usage: [FAM=4] rlp.py MODE NAME SPEC..."""
import sys, os, json, random
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE); import feat
import pg
from n5x import dual

def games(specs):
    for sp in specs:
        if sp.startswith("rand:"):
            _, K, S, a, b = sp.split(":"); rng = random.Random(int(S))
            for k in range(int(K)):
                n = rng.randint(int(a), int(b)); pr = [rng.randint(0, n) for _ in range(n)]; ow = [rng.randint(0, 1) for _ in range(n)]
                su = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) for _ in range(n)]
                yield "rand%s_%d" % (S, k), pg.Game(pr, ow, su), None
        elif sp.startswith("list:"):
            for line in open(sp[5:]):
                p = line.split()
                if not p or p[0].startswith("#"): continue
                X = lambda q: os.path.join(ROOT, q) if os.path.exists(os.path.join(ROOT, q)) else os.path.join(ROOT, "experiments", q)
                yield p[0], feat.load(X(p[0])), feat.readstart(X(p[1])) if len(p) > 1 else None
        elif sp.startswith("dual:"):
            yield sp, dual(feat.load(sp[5:])), None
        else:
            gp, _, st = sp.partition(":"); yield gp, feat.load(gp), feat.readstart(st) if st else None

FAM = int(os.environ.get("FAM", "0"))        # 0: uniform-24 (feat.NAMES); 4: moments (feat.MNAMES); 5: both (45)
FNAMES = lambda: {4: feat.MNAMES, 5: feat.NAMES + feat.MNAMES[:21], 6: None, 7: None}.get(FAM, feat.NAMES)

def collect(specs, nmax=10 ** 9, which=None):
    which = FAM if which is None else which
    T = []                                   # (game, t, Delta)
    for name, g, st in games(specs):
        if g.n > nmax: continue
        try: S = feat.states(g, st)
        except Exception as e: print("SKIP", name, repr(e)[:60]); continue
        for t in range(len(S) - 1): T.append((name, t, [b - a for a, b in zip(S[t][which], S[t + 1][which])]))
    return T

def colscale(D):
    s = np.abs(D).max(axis=0); s[s == 0] = 1.0; return D / s, s

def solve_c(D):
    """min sum |c'| s.t. (D/s) c' >= 1 (columns scaled by their max |entry|); returns c = c'/s or None."""
    Ds, sc = colscale(D); m, k = Ds.shape
    A = np.hstack([-Ds, Ds]); r = linprog(np.ones(2 * k), A_ub=A, b_ub=-np.ones(m), bounds=[(0, None)] * (2 * k), method="highs")
    return None if r.status != 0 else (r.x[:k] - r.x[k:]) / sc

def farkas(D):
    """max sum y, D^T y = 0, 0 <= y <= 1."""
    m, k = D.shape
    r = linprog(-np.ones(m), A_eq=D.T, b_eq=np.zeros(k), bounds=[(0, 1)] * m, method="highs")
    return r.x if r.status == 0 and -r.fun > 1e-7 else None

def intvec(x, den=10 ** 6):
    fr = [Fraction(v).limit_denominator(den) for v in x]; L = 1
    for f in fr: L = L * f.denominator // __import__("math").gcd(L, f.denominator)
    return [int(f * L) for f in fr]

def cert_c(T, c):
    """an integer c with c . Delta >= 1 at every transition (exact check), from the LP's c by rational rounding; None if rounding fails."""
    import math
    for den in (10 ** 3, 10 ** 5, 10 ** 7, 10 ** 9):
        fr = [Fraction(float(v)).limit_denominator(den) for v in c]; L = 1
        for f in fr: L = L * f.denominator // math.gcd(L, f.denominator)
        ci = [int(f * L) for f in fr]; worst = min(sum(a * b for a, b in zip(ci, d)) for _, _, d in T)
        if worst >= 1: return ci
        if worst > 0: return [v * (1 // worst + 1) for v in ci] if False else None
    return None

def kernel1(rows_):
    """exact kernel of the matrix whose COLUMNS are the vectors rows_ (Fractions); returns a basis list."""
    k = len(rows_[0]); m = len(rows_); A = [[Fraction(rows_[j][i]) for j in range(m)] for i in range(k)]
    piv = []; r = 0
    for col in range(m):
        p_ = next((i for i in range(r, k) if A[i][col] != 0), None)
        if p_ is None: continue
        A[r], A[p_] = A[p_], A[r]; pv = A[r][col]; A[r] = [x / pv for x in A[r]]
        for i in range(k):
            if i != r and A[i][col] != 0:
                f = A[i][col]; A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append(col); r += 1
    free = [c for c in range(m) if c not in piv]; basis = []
    for fcol in free:
        v = [Fraction(0)] * m; v[fcol] = Fraction(1)
        for i, pc in enumerate(piv): v[pc] = -A[i][fcol]
        basis.append(v)
    return basis

def cert_y(T, y):
    """minimal infeasible support (circuit) and its exact positive integer Farkas vector, or None."""
    sup = [i for i, v in enumerate(y) if v > 1e-9]
    i = 0
    while i < len(sup):                      # drop transitions while the rest stays infeasible
        trial = sup[:i] + sup[i + 1:]
        if trial and farkas(np.array([T[j][2] for j in trial], dtype=float)) is not None: sup = trial
        else: i += 1
    B = kernel1([T[j][2] for j in sup])
    if len(B) != 1: return None
    v = B[0]
    if all(x < 0 for x in v): v = [-x for x in v]
    if not all(x > 0 for x in v): return None
    L = 1
    for x in v: L = L * x.denominator // __import__("math").gcd(L, x.denominator)
    yi = [0] * len(T)
    for j, x in zip(sup, v): yi[j] = int(x * L)
    k = len(T[0][2])
    assert all(sum(yi[j] * T[j][2][c] for j in sup) == 0 for c in range(k))
    return yi

def run_uni(name, T, names):
    D = np.array([d for _, _, d in T], dtype=float); c = solve_c(D); out = dict(name=name, mode="uni", transitions=len(T), features=names)
    if c is not None:
        ci = cert_c(T, c); out.update(result="FEASIBLE", c=ci)
        print("FEASIBLE", name, len(T), {n_: v for n_, v in zip(names, ci or c.round(3)) if v})
    else:
        y = farkas(D); yi = cert_y(T, y) if y is not None else None
        sup = [(T[i][0], T[i][1], yi[i] if yi else float(y[i])) for i in range(len(T)) if (yi[i] if yi else y[i]) > 0] if y is not None else []
        out.update(result="INFEASIBLE", y=sup, exact=yi is not None)
        print("INFEASIBLE", name, len(T), "support", len(sup), "games", sorted({s[0] for s in sup})[:8], "exact" if yi else "inexact")
    return out

def run_lex(name, T, names):
    rem = list(range(len(T))); rounds = []
    while rem:
        D0 = np.array([T[i][2] for i in rem], dtype=float); D, sc = colscale(D0); m, k = D.shape
        # vars c (k, free) and delta (m in [0,1]); D c - delta >= 0; maximise sum delta
        A = np.hstack([-D, np.eye(m)]); bnd = [(-1e4, 1e4)] * k + [(0, 1)] * m
        r = linprog(np.r_[np.zeros(k), -np.ones(m)], A_ub=A, b_ub=np.zeros(m), bounds=bnd, method="highs")
        if r.status != 0: rounds.append("LPFAIL"); break
        c = r.x[:k]; strict = [rem[i] for i in range(m) if D[i] @ c >= 1 - 1e-7]; c = c / sc
        if not strict: rounds.append("STUCK(%d left)" % m); break
        rounds.append((len(strict), {n_: round(v, 3) for n_, v in zip(names, c) if abs(v) > 1e-9}))
        rem = [i for i in rem if i not in set(strict)]
    print("LEX", name, len(T), "depth", len(rounds), [r if isinstance(r, str) else r[0] for r in rounds])
    return dict(name=name, mode="lex", transitions=len(T), rounds=rounds, stuck=bool(rounds) and isinstance(rounds[-1], str))

def main():
    mode, name, specs = sys.argv[1], sys.argv[2], sys.argv[3:]
    os.makedirs(os.path.join(HERE, "..", "out", "box53"), exist_ok=True)
    if mode == "uni1":                       # the uniform LP game by game (which single games already have no uniform ranking function)
        res = []
        for gname, g, st in games(specs):
            try: S = feat.states(g, st)
            except Exception as e: print("SKIP", gname); continue
            T = [(gname, t, [b - a for a, b in zip(S[t][FAM], S[t + 1][FAM])]) for t in range(len(S) - 1)]
            if T: r = run_uni(gname, T, FNAMES() or ["e%d" % i for i in range(len(T[0][2]))]); r["n"] = g.n; res.append(r)
        json.dump(res, open(os.path.join(HERE, "..", "out", "box53", name + ".json"), "w"))
        bad = sorted((r["n"], r["transitions"], r["name"]) for r in res if r["result"] == "INFEASIBLE")
        print("SUMMARY", name, "games", len(res), "infeasible", len(bad), "smallest", bad[:5])
        return
    if mode == "rk":                         # per game, PER-RANK features, minimise the largest |coefficient| (L-infinity)
        res = []
        for gname, g, st in games(specs):
            S = feat.states(g, st); T = [[b - a for a, b in zip(S[t][3], S[t + 1][3])] for t in range(len(S) - 1)]
            if not T: continue
            D = np.array(T, dtype=float); m, k = D.shape
            # vars c (k) and z: min z, D c >= 1, -z <= c_i <= z
            A = np.vstack([np.hstack([-D, np.zeros((m, 1))]), np.hstack([np.eye(k), -np.ones((k, 1))]), np.hstack([-np.eye(k), -np.ones((k, 1))])])
            b = np.r_[-np.ones(m), np.zeros(2 * k)]
            r = linprog(np.r_[np.zeros(k), 1.0], A_ub=A, b_ub=b, bounds=[(None, None)] * k + [(0, None)], method="highs")
            z = r.x[-1] if r.status == 0 else None
            print("RK", gname, "n", g.n, "transitions", m, "features", k, "Linf", None if z is None else round(z, 4))
            res.append(dict(name=gname, n=g.n, transitions=m, Linf=z))
        json.dump(res, open(os.path.join(HERE, "..", "out", "box53", name + ".json"), "w"))
        return
    if mode == "pv":
        res = []
        for gname, g, st in games(specs):
            S = feat.states(g, st)
            T = [(gname, t, [b - a for a, b in zip(S[t][1] + S[t][0], S[t + 1][1] + S[t + 1][0])]) for t in range(len(S) - 1)]
            if not T: continue
            res.append(run_uni(gname, T, ["pv%d" % i for i in range(len(T[0][2]))]))
        json.dump(res, open(os.path.join(HERE, "..", "out", "box53", name + ".json"), "w"))
        return
    T = collect(specs)
    out = run_uni(name, T, FNAMES()) if mode == "uni" else run_lex(name, T, FNAMES())
    json.dump(out, open(os.path.join(HERE, "..", "out", "box53", name + ".json"), "w"))

if __name__ == "__main__":
    main()
