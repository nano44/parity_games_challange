#!/usr/bin/env python3
"""Box 38 (c): NO-ENTRY check on N5 runs from a given start pair (SPEC S3 "unless a start pair is given") or the canonical start.
Trace rows as box32 rows_w, but from (σ0, τ0). For every HN stretch (H1 ∧ ¬H2, one phase): after the first fallback at a, any entry
k -> k+1 (R_k ⊊ R_{k+1}) with θ constant on states [a, k+1] is a NO-ENTRY violation; reported with case (A/B) and τ(o) = o or not.
One Odd choice vertex asserted. Usage: neb_run.py game.pg [state-file]   (state file: σ as n integers, -1 at Odd vertices)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); B37 = os.path.join(HERE, "..", "box37")
sys.path.insert(0, B37); sys.path.insert(0, os.path.join(HERE, "..", "..", "si", "coarse"))
from outsn import *
import pg

def trace(g, s0=None, cap=10 ** 5):
    E, Ed = Engine(g), Engine(dual(g)); o = odd1(g); s, t = start_pair(g, E, Ed, None)
    if s0 is not None:
        s = list(s0); t = list(t); t[o] = o if o in g.succ[o] else t[o]
    rows = []
    while len(rows) < cap:
        Xi, sb = E.evaluate(tuple(s)); _, W = wvals(g, s, t); U, _ = Ed.evaluate(tuple(t))
        rows.append(dict(ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), R=reach_o(g, s, t, o), th=E.key(Xi[o]),
                         h1=not oncycle(g, s, sb, o), h2=not oncycle(g, s, t, o), Xi=Xi, s=list(s), t=list(t), fb=0))
        r = step(g, E, Ed, s, t)
        if r is None: break
        rows[-1]["fb"] = r[4]; s, t = r[0], r[1]
    return rows, o, E

def check(g, s0, acc, name):
    assert sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1
    rows, o, E = trace(g, s0); N = len(rows); bump(acc, "runs"); bump(acc, "transitions", N - 1)
    HN = [r["h1"] and not r["h2"] for r in rows]
    for a in range(N - 1):
        if not (HN[a] and rows[a]["fb"] and rows[a + 1]["ph"] == rows[a]["ph"]): continue
        too = rows[a]["t"][o] == o; case = "A" if E.rank[o] > E.rank[rows[a]["Xi"][o][0]] else "B"
        key = f"{case}_tauo{'=o' if too else '!=o'}"; bump(acc, key + "_fallbacks")
        k = a
        while k + 1 < N and HN[k + 1] and rows[k + 1]["ph"] == rows[a]["ph"] and rows[k + 1]["th"] == rows[a]["th"]:
            R0, R1 = set(rows[k]["R"]), set(rows[k + 1]["R"])
            if R1 > R0 or (R1 - R0 and not (R0 - R1)): bump(acc, key + "_VIOLATION"); mx(acc, "ex_" + key, 1, g.n, name, a, k)
            if k > a and [rows[k]["Xi"][v] for v in rows[k]["R"]] != [rows[k + 1]["Xi"][v] for v in rows[k]["R"]]: pass
            bump(acc, key + "_postfb_transitions"); k += 1

if __name__ == "__main__":
    acc = {}; args = sys.argv[1:]
    i = 0
    while i < len(args):
        f = args[i]; s0 = None
        if i + 1 < len(args) and args[i + 1].endswith(".state"):
            s0 = list(map(int, open(args[i + 1]).read().split())); i += 1
        g = load(f)
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1: check(g, s0, acc, f)
        else: bump(acc, "skipped_not_C1O")
        i += 1
    for key in sorted(acc): print(key, acc[key])
