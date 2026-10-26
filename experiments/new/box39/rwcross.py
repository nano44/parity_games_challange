#!/usr/bin/env python3
"""Box 39 (1) §7: runs of consecutive in-phase HN states with θ and c_w constant (crossings allowed). Checks Lemma BF across
crossings (every transition, Even v ∈ R_k ∩ R_{k+1}, successor x ∈ R̄_k: M_{k+1}(v) ≥ wt(v) + M_k(x); FAIL_BFX) and CONJECTURE M-CROSS
(an M-rise at transition t needs t − s < N_s − 1, s = the run start or the last entry before t, N_s = |R̄| after it; FAIL_MCROSS).
DATA only. Usage: rwcross.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from rwclass import *

def analyse_x(g, acc, name):
    rows, o, E = trace(g, None); N = len(rows); n = g.n
    for r in rows: r["cw"] = cw_of(g, r, o, E) if (r["h1"] and not r["h2"]) else None
    HN = [r["h1"] and not r["h2"] for r in rows]; a = 0
    while a < N:
        if not HN[a]: a += 1; continue
        b = a
        while (b + 1 < N and HN[b + 1] and rows[b + 1]["ph"] == rows[a]["ph"] and rows[b + 1]["th"] == rows[a]["th"]
               and rows[b + 1]["cw"] == rows[a]["cw"]): b += 1
        ct = E.rank[rows[a]["Xi"][o][0]]; Ts = max(ct, E.rank[rows[a]["cw"]]); hi = ~((1 << (Ts + 1)) - 1)
        M = lambda val: E.weight(val[1] & hi); wt = lambda v: (E.weight(E.bit[v]) if E.rank[v] > Ts else 0)
        s = a; crosses = 0
        for k in range(a, b):
            R0, R1 = set(rows[k]["R"]), set(rows[k + 1]["R"]); X0, X1 = rows[k]["Xi"], rows[k + 1]["Xi"]
            if R0 != R1: crosses += 1
            for v in R0 & R1:
                if g.owner[v] != 0: continue
                for x in set(g.succ[v]):
                    if (x in R0 or x == o) and M(X1[v]) < wt(v) + M(X0[x]): bump(acc, "FAIL_BFX"); print("BFX", name, a, k, v, x)
            if any(M(X1[z]) > M(X0[z]) for z in (R0 & R1) | {o}):
                bump(acc, "Mrise_transitions")
                if k - s >= len(R1 | {o}) - 1 and k - s >= len(R0 | {o}) - 1: bump(acc, "FAIL_MCROSS"); print("MCROSS", name, a, s, k)
            if R1 - R0: s = k + 1
        if crosses: bump(acc, "runs_with_crossings"); bump(acc, "crossings", crosses)
        a = b + 1

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        try: g = load(f)
        except Exception: bump(acc, "load_fail"); continue
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1: analyse_x(g, acc, f)
        else: bump(acc, "skipped_not_C1O")
    for key in sorted(acc): print(key, acc[key])
