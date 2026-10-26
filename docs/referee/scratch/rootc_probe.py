#!/usr/bin/env python3
"""REFEREE succ. 16, for the §C of R-N5-ROOT (REFEREE-2's N-ROOT-3, and RELAY-PIECE's multi-value case). Own engine only (rl_engine; the
DL-SPLIT classification exactly as root_probe.py). Counts:
 II_ONLY       clean D-leaves (case (A)) where only (ii) holds: no (i), no TOG at e1, no TIE
 II_NORHO_U    of those, u's own value Xi(u) does not change at t -> t+1 (no rho event at u, so (ii) is not a FLIP ROUTE event at u)
 II_NORHO_C    of those, no q in Q_c (u included) changes Xi at t -> t+1: the transition carries no rho event of class c at all, so no ROUTE,
               RELAY or CYC event in P-N5-FLIP's sense (they are rho events); then DL-SPLIT's Consequence holds only with (ii) read as
               "a route change at the D-leaving vertex u" (N-ROOT-3)
 RLP_DCHG      RELAY-PIECE runs (u in DD, A and R_u non-increasing, S4a) in which Delta(u) changes after s + L_A (multi-value case of (i))
Usage: rootc_probe.py files...  (env RANDSTARTS 2, MAXN 40)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, epr_probe as E
from flip_probe import nxt, on_cycle, class_exit, kap
from root_probe import firstD
EX = []


def analyse(g, start, cnt, name):
    st = RE.run(g, start); n = g.n
    Q = {v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1}
    for x in st:
        x["nx"] = nxt(g, x["s"], x["sb"])
        x["D"] = {u for u in Q if x["sb"][u] != x["t"][u]}
        x["fu"] = [firstD(g, x["s"], x["t"], x["D"], v) for v in range(n)]
    K = len(st); k = 0
    while k < K:
        j = k; lam = tuple(v[0] for v in st[k]["Xi"])
        while j + 1 < K and tuple(v[0] for v in st[j + 1]["Xi"]) == lam and st[j + 1]["t"] == st[k]["t"]: j += 1
        a, b = k, j; tau = st[a]["t"]
        for c in sorted(set(lam)):
            U = {v for v in range(n) if lam[v] == c}
            if len(U) < 2: continue
            A = {t: {v for v in U if st[t]["fu"][v] is None} for t in range(a, b + 1)}
            s4a = {t: not st[t]["fb"] for t in range(a, b)}
            Qc = sorted((Q & U) - {c}); stop = set(Qc) | {c}
            for t in range(a, b):
                if not s4a[t] or A[t + 1] <= A[t]: continue
                s0, s1 = st[t], st[t + 1]
                for z in A[t + 1] - A[t]:
                    u = s0["fu"][z]
                    if u in s1["D"]: continue
                    if on_cycle(s0["nx"], u) or on_cycle(s1["nx"], u): continue
                    y1, y2 = s0["sb"][u], s1["sb"][u]
                    pre, cy = RE.lasso(s0["nx"], y2)
                    if u in pre or u in cy: continue
                    cnt["CLEAN_A"] += 1
                    p1, e1 = class_exit(s0["nx"], y1, stop)
                    i_ = e1 is not None and e1 != c and s0["Xi"][e1] != s1["Xi"][e1]
                    ii = any(class_exit(s0["nx"], y, stop) != class_exit(s1["nx"], y, stop) for y in g.succ[u] if y in U)
                    tog = e1 is not None and e1 != c and u in set(sum(RE.lasso(s1["nx"], e1), []))
                    tie = kap(g, s0["Xi"][y2]) == kap(g, s0["Xi"][y1])
                    if ii and not (i_ or tog or tie):
                        cnt["II_ONLY"] += 1
                        if s0["Xi"][u] == s1["Xi"][u]: cnt["II_NORHO_U"] += 1
                        if all(s0["Xi"][q] == s1["Xi"][q] for q in set(Qc) | {u}):
                            cnt["II_NORHO_C"] += 1
                            if len(EX) < 10: EX.append(("II_NORHO_C", name, t, c, z, u))
            # RELAY-PIECE multi-value case
            M = lambda t, z: g.weight(st[t]["Xi"][z][1])
            for u in Qc:
                Ru = lambda t: {z for z in U if st[t]["fu"][z] == u}
                DD = lambda t: u in st[t]["D"] and st[t]["sb"][u] in A[t] and tau[u] in A[t]
                t = a
                while t <= b:
                    if not DD(t): t += 1; continue
                    s = t; e = t
                    while e < b and s4a[e] and DD(e + 1) and A[e + 1] <= A[e] and Ru(e + 1) <= Ru(e): e += 1
                    LA = max(len(A[s]) - 1, 0)
                    if s + LA <= e - 1:
                        cnt["RLP_nonvac"] += 1
                        vals = [M(q, tau[u]) - M(q, st[q]["sb"][u]) for q in range(s + LA, e + 1)]
                        if len(set(vals)) > 1: cnt["RLP_DCHG"] += 1
                    t = e + 1
        k = j + 1


def main(a):
    cnt = Counter(); nst = int(os.environ.get("RANDSTARTS", "2"))
    for f in a:
        path, _, sp = f.partition(":")
        if path.endswith(".start"): continue
        try: g = RE.parse(path)
        except Exception: cnt["parse_err"] += 1; continue
        if g.n > int(os.environ.get("MAXN", "40")): cnt["skip_big"] += 1; continue
        r = random.Random(os.path.relpath(path))
        for j, s0 in enumerate([RE.best_reward_start(g)] + [D.rand_start(g, r) for _ in range(nst)]):
            cnt["RUNS"] += 1; analyse(g, s0, cnt, "%s/%d" % (os.path.relpath(path), j))
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
