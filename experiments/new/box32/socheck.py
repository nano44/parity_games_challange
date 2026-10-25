#!/usr/bin/env python3
"""Box 32: checks of Lemma SO and Lemma TH (docs/new/N5-L-box32.md §6) per phase of N5 on C^1O:
  SO:  S_o (relevant σ̄(o) changes, λ(o) != o) <= Θ + (d_o − 1)(Θ + 1), Θ = #θ-changes; and every relevant σ̄(o) change with θ unchanged
       drops the old choice from the minimiser set T = {x in succ(o) : Ξ(x) = min}.
  TH:  Θ <= (n − 1) + n(X + 1) + X; under H1 every θ-change is a crossing or changes Ξ on F; under ¬H1 θ = (c_θ, ∅, d).
  J:   J (non-tame, R25) <= S_o.
Usage: socheck.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from mblock import *

def bump(acc, k, d=1): acc[k] = acc.get(k, 0) + d

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        g = load(f); rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]; n = g.n; d_o = len(g.succ[o])
        tame = [all(coarse(ev[i + 1][0][v], rows[i]["M"]) == coarse(ev[i][0][v], rows[i]["M"]) for v in range(n)) for i in range(len(rows) - 1)]
        k = 0
        while k < len(rows) - 1:
            if rows[k]["ph"] != rows[k + 1]["ph"]: k += 1; continue
            j = k
            while j + 1 < len(rows) - 1 and rows[j + 1]["ph"] == rows[j + 2]["ph"]: j += 1
            So = Th = X = J = 0
            for i in range(k, j + 1):
                X0, X1 = ev[i][0], ev[i + 1][0]; s0, s1 = ev[i][1][o], ev[i + 1][1][o]; cross = rows[i]["R"] != rows[i + 1]["R"]
                X += cross; J += not tame[i]
                if X0[o][0] == o: continue
                if X0[o] != X1[o]:
                    Th += 1
                    F = set(range(n)) - set(rows[i]["R"]) - {o}
                    if rows[i]["h1"]:
                        if not cross and not any(X0[v] != X1[v] for v in F): bump(acc, "TH_H1_FAIL")
                    elif X0[o][1] != 0 or X1[o][1] != 0: bump(acc, "TH_notH1_SHAPE_FAIL")
                if s0 != s1:
                    So += 1
                    if X0[o] == X1[o]:
                        mu = X1[s1]; T1 = [x for x in g.succ[o] if X1[x] == mu]
                        if s0 in T1: bump(acc, "SO_TIEBREAK_FAIL"); acc.setdefault("ex_so", (os.path.basename(f), i))
            bump(acc, "phases")
            if So > Th + (d_o - 1) * (Th + 1): bump(acc, "SO_BOUND_FAIL")
            if Th > (n - 1) + n * (X + 1) + X: bump(acc, "TH_BOUND_FAIL")
            if J > So: bump(acc, "J_GT_SO_FAIL"); acc.setdefault("ex_J", (os.path.basename(f), k))
            for key, val in (("max_So", So), ("max_Theta", Th), ("max_J", J)):
                if val > acc.get(key, (0,))[0]: acc[key] = (val, dict(n=n, d_o=d_o, So=So, Th=Th, X=X, J=J), os.path.basename(f))
            k = j + 1
    for kk in sorted(acc): print(kk, acc[kk])
