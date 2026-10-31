#!/usr/bin/env python3
"""L-COMP box 25 (Lead 02:50Z, INS): tight-arena insertions INS_I(c) and key changes KEYCH_I(x) in W-constant intervals of N5, my own
implementation on n5b (SPEC), from the TEXT of l-si docs/si/N5-SBF-box53.md §7 (481bc6c2; L-NEW box 106 setting). L-SI's treestab.py is
not imported (xins.py runs it in its own process).
- W-runs: n5-box23/rstar.wruns. W_t := VJ valuation (cycle node, path set, length) of the (σ_t, τ)-plays; Ξ_t, Iσ_t as SPEC S1 / S2.
- W-constant interval I = [p, e] inside a W-run: maximal with W_t = W_{t+1} for p <= t < e, e > p (scanned left to right inside the run).
- For an EVEN W-cycle node c (Ω(c) even): X_c := {x != c : λ_W(x) = c}. Tight successors of an Even y in X_c: T(y) := {z in succ(y) :
  λ_W(z) = c, y ⊕ W(z) = W(y)}, with y ⊕ (u, P, l) := (u, P ∪ {y} if y is more relevant than u (by (Ω, id)) else P, l + 1).
- Tight arena A_t(y) := ({σ_t(y)} ∪ Iσ_t(y)) ∩ T(y).
- LexTree(A): vertices of X_c in increasing W-length; key(c) := (), Odd x: key(x) := key(τ x) + (x,), Even x: the z in A(x) of least key
  (tuples compared lexicographically), key(x) := key(z) + (x,).
- INS_I(c): transitions t -> t+1 with p <= t <= e - 1 at which some A_{t+1}(y) is not a subset of A_t(y) (y Even in X_c); this is the range
  L-SI's treestab.py scans. INS2: the same with t <= e - 2 (the range of the §7 text). KEYCH_I(x), x in X_c: transitions t -> t+1, p <= t <= e-1,
  at which key_t(x) != key_{t+1}(x) (key_t: the path from x to c under σ_t on Even, τ on Odd, as a tuple read from c's end, c excluded).
- Checks: LTX (σ_{t+1} != LexTree(A_t) on Even X_c), TSX (an Even of X_c switches at t+1 -> t+2 <= e with no insertion at t), NOVT (an
  insertion z in A_{t+1}(y) \\ A_t(y) that is not a strict Ξ-overtake), KB (KEYCH_I(x) > 1 + INS_I(c)).
Per game: intervals, the checks, MAXKEYCH, MAXINS, MAXINS2, and for the max-INS (I, c): |I|, its W-run length.
Usage: ins.py GAME.pg [START] [-v]"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "n5-box23"))
import rstar  # noqa: E402
import n5b  # noqa: E402
import pg  # noqa: E402


def analyse(g, start=None):
    eng = rstar.Eng(g); SG = eng.N.SG; own = g.owner; n = g.n
    x = start or eng.start(); states, fbs, data = [], [], []
    while True:
        states.append(x); data.append(eng.sdata(*x)); nx = eng.step(*x)
        if nx is None:
            break
        fbs.append(nx[2]); x = (nx[0], nx[1])
    S = [s for s, _ in states]
    XIc = {}

    def xi(t):
        if t not in XIc:
            v = SG.evaluate(list(S[t]))
            imp = eng.N.improving(SG, list(S[t]), v)
            XIc[t] = (v, {(y, z) for y, zs in imp.items() for z in zs})
        return XIc[t]

    def plus(y, val):
        u, P, l = val
        return (u, P | {y} if SG.rel(y, u) > 0 else P, l + 1)

    def better(a, b):            # a strictly better than b for Even
        return SG.nvo(b, a) < 0

    res = dict(intervals=0, LTX=0, TSX=0, NOVT=0, KB=0, MAXKEYCH=0, MAXINS=0, MAXINS2=0, best=None)
    for a, b in rstar.wruns(eng, states, fbs, data):
        tau = states[a][1]; W = [data[t]["W"] for t in range(len(states))]
        k = a
        while k < b:
            e = k
            while e < b and W[e + 1] == W[e]:
                e += 1
            if e == k:
                k += 1; continue
            res["intervals"] += 1; Wk = W[k]
            cls = {}
            for v in range(n):
                cn = Wk[v][0]
                if v != cn and g.prio[cn] % 2 == 0:
                    cls.setdefault(cn, []).append(v)
            for cn, X in cls.items():
                EV = [y for y in X if own[y] == 0]
                T = {y: [z for z in sorted(set(g.succ[y])) if Wk[z][0] == cn and plus(y, Wk[z]) == Wk[y]] for y in EV}

                def arena(t):
                    _, I = xi(t)
                    return {y: frozenset(z for z in T[y] if z == S[t][y] or (y, z) in I) for y in EV}

                order = sorted(X, key=lambda v: (Wk[v][2], v))

                def lextree(A):
                    K = {cn: ()}; ch = {}
                    for v in order:
                        if own[v] == 1:
                            K[v] = K[tau[v]] + (v,)
                        else:
                            z = min(A[v], key=lambda w: K[w]); ch[v] = z; K[v] = K[z] + (v,)
                    return ch

                def keyof(t, v):
                    p = [v]; y = v
                    while y != cn:
                        y = S[t][y] if own[y] == 0 else tau[y]; p.append(y)
                        if len(p) > n + 1:
                            return None
                    return tuple(reversed(p[:-1]))

                AR = [arena(t) for t in range(k, e + 1)]
                ins = ins2 = 0
                for i, t in enumerate(range(k, e)):
                    ch = lextree(AR[i])
                    if any(S[t + 1][y] != ch[y] for y in EV):
                        res["LTX"] += 1
                    new = [(y, z) for y in EV for z in AR[i + 1][y] - AR[i][y]]
                    if new:
                        ins += 1; ins2 += t <= e - 2
                        v0, _ = xi(t); v1, _ = xi(t + 1)
                        for y, z in new:
                            if not (better(v1[z], v1[S[t + 1][y]]) and not better(v0[z], v0[S[t][y]])):
                                res["NOVT"] += 1
                    if t + 2 <= e and not new and any(S[t + 2][y] != S[t + 1][y] for y in EV):
                        res["TSX"] += 1
                kc = max(sum(1 for t in range(k, e) if keyof(t, v) != keyof(t + 1, v)) for v in X)
                res["KB"] += sum(1 for v in X if sum(1 for t in range(k, e) if keyof(t, v) != keyof(t + 1, v)) > 1 + ins)
                res["MAXKEYCH"] = max(res["MAXKEYCH"], kc); res["MAXINS2"] = max(res["MAXINS2"], ins2)
                res["MAXINS"] = max(res["MAXINS"], ins)
                if res["best"] is None or (ins, e - k) > res["best"][:2]:     # the max-INS (I, c), ties to the longer interval
                    res["best"] = (ins, e - k, b - a, cn, k, e)
            k = e
    return states, res


def main():
    g = pg.read(sys.argv[1]); args = [x for x in sys.argv[2:] if x != "-v"]
    st = rstar.overlay(g, rstar.Eng(g).start(), n5b.read_start(args[0], g)) if args else None
    states, r = analyse(g, st)
    b = r.pop("best")
    print(f"INS n {g.n} it {len(states) - 1} " + " ".join(f"{k} {v}" for k, v in r.items()) +
          (f" | max-INS interval: INS {b[0]} |I| {b[1]} W-run {b[2]} c {b[3]} [{b[4]}, {b[5]}]" if b else ""))


if __name__ == "__main__":
    main()
