#!/usr/bin/env python3
"""Box 38 (L-RED): independent checker of L-NEW succ. 15's Lemma L-MONO, Lemma Z-COUNT, Theorem TOGGLE and Corollary TOGGLE-COUNT,
written from docs/new/N5-DROP-box35.md (claude/l-new e0f3780; not from togz.py). Trace: sox.trace (asserted = n5.run).
Per phase (λ_Ξ, τ constant) with c := λ(o) != o, U := λ^{-1}(c), next_k = σ_k on Even, σ̄_k on Odd, H1_k: o on no honest cycle,
L_k := length of c's honest cycle (c, next(c), ... back to c), Z_k := {(v, len Ξ_k(v)) : v in U, P(Ξ_k v) = ∅}.
  LMONO    L non-increasing if Ω(c) even, non-decreasing if odd;   LSTRICT  next(c) changes => L changes
  ZINT     for each v in U the states with P(Ξ v) = ∅ form one interval;   ZLEN  len Ξ(v) monotone on it (one direction per v)
  TOGGLE   H1_k != H1_{k+1} => Z_k != Z_{k+1} or next_k(c) != next_{k+1}(c)
  TCOUNT   #toggles <= |U|(n+1) + n - 1
Usage: sox4.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sox, n5

def analyse(g, cap=5000):
    oc = sox.oddchoice(g); assert len(oc) == 1, "not C^1O"; o = oc[0]; n = g.n
    S, FB, E = sox.trace(g, cap)
    it, fb, *_ = n5.run(g, cap=cap); assert (it, fb) == (len(FB), sum(FB)), "trace differs from n5.run"
    N = len(S); ev = [E.evaluate(s) for s, _ in S]; Xi = [e[0] for e in ev]; sb = [e[1] for e in ev]
    lam = [tuple(x[0] for x in X) for X in Xi]
    nx = lambda k, v: S[k][0][v] if g.owner[v] == 0 else sb[k][v]
    def H1(k):
        x, seen = nx(k, o), set()
        while x not in seen:
            if x == o: return False
            seen.add(x); x = nx(k, x)
        return True
    def Lc(k, c):
        x, l = nx(k, c), 1
        while x != c and l <= n: x = nx(k, x); l += 1
        return l
    inph = [lam[k] == lam[k + 1] and S[k][1] == S[k + 1][1] for k in range(N - 1)]
    C, ex = {}, {}
    def bad(nm, k): C[nm] = C.get(nm, 0) + 1; ex.setdefault(nm, k)
    rows = []; k = 0
    while k < N - 1:
        if not inph[k]: k += 1; continue
        b = k
        while b + 1 < N - 1 and inph[b + 1]: b += 1
        a = k; k = b + 1
        c = lam[a][o]
        if c == o: continue
        U = [v for v in range(n) if lam[a][v] == c]; st = range(a, b + 2)
        h = {s: H1(s) for s in st}; L = {s: Lc(s, c) for s in st}
        Z = {s: frozenset((v, Xi[s][v][2]) for v in U if Xi[s][v][1] == 0) for s in st}
        even = g.prio[c] % 2 == 0
        tog = zonly = sonly = both = 0
        for s in range(a, b + 1):
            if (L[s + 1] > L[s]) if even else (L[s + 1] < L[s]): bad("LMONO", s)
            cch = nx(s, c) != nx(s + 1, c)
            if cch and L[s + 1] == L[s]: bad("LSTRICT", s)
            if h[s] != h[s + 1]:
                tog += 1; zch = Z[s] != Z[s + 1]
                if not zch and not cch: bad("TOGGLE", s)
                zonly += zch and not cch; sonly += cch and not zch; both += zch and cch
        for v in U:
            ins = [s for s in st if Xi[s][v][1] == 0]
            if ins and ins[-1] - ins[0] + 1 != len(ins): bad("ZINT", (a, v))
            ls = [Xi[s][v][2] for s in ins]
            if any(x < y for x, y in zip(ls, ls[1:])) and any(x > y for x, y in zip(ls, ls[1:])): bad("ZLEN", (a, v))
        if tog > len(U) * (n + 1) + n - 1: bad("TCOUNT", a)
        rows.append(dict(a=a, b=b, tog=tog, zonly=zonly, sonly=sonly, both=both, fb=sum(FB[a:b + 1]),
                         zch=sum(Z[s] != Z[s + 1] for s in range(a, b + 1)), cch=sum(nx(s, c) != nx(s + 1, c) for s in range(a, b + 1))))
    return dict(n=n, o=o, it=len(FB), fb=sum(FB), rows=rows, C=C, ex=ex)

if __name__ == "__main__":
    tot = {}
    for f in sys.argv[1:]:
        g = sox.load(f)
        if len(sox.oddchoice(g)) != 1: continue
        r = analyse(g); rs = r["rows"]
        m = {k: max((x[k] for x in rs), default=0) for k in ("tog", "zonly", "sonly", "both", "zch", "cch")}
        print(os.path.basename(f), f"n {r['n']} it {r['it']} fb {r['fb']} phases {len(rs)} max", m, "FAILS", r["C"] or 0, r["ex"] or "", flush=True)
        for x in rs:
            for kk in ("tog", "zonly", "sonly", "both"): tot[kk] = tot.get(kk, 0) + x[kk]
        for kk, v in r["C"].items(): tot[kk] = tot.get(kk, 0) + v
        tot["files"] = tot.get("files", 0) + 1; tot["phases"] = tot.get("phases", 0) + len(rs)
    print("TOTAL", tot)
