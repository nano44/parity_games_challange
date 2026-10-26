#!/usr/bin/env python3
"""Box 39 (1): R̄-rises with θ fixed (RW_S, docs/new/N5-TAUW-box38.md §6). For every maximal run of consecutive in-phase HN states
(H1 ∧ ¬H2) with θ constant: transitions, transitions with an R̄-rise (z ∈ R̄_t ∩ R̄_{t+1}, z ≠ o, Ξ_t(z) ◁ Ξ_{t+1}(z)) split by
fallback / S4a, rises per vertex, crossings; c_w at the run's states (o or not). Reports maxima against n. DATA only.
Usage: rwcount.py game.pg [game.state] ...   (non-𝒞^1O files are skipped and counted)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box38"))
from neb_run import *

def cw_of(g, r, o, E):
    s, t = r["s"], r["t"]; nx = [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]
    C = [o]; x = nx[o]
    while x != o: C.append(x); x = nx[x]
    return max(C, key=lambda v: E.rank[v])

def runs_of(g, s0):
    rows, o, E = trace(g, s0); N = len(rows)
    HN = [r["h1"] and not r["h2"] for r in rows]
    out = []; a = 0
    while a < N:
        if not HN[a]: a += 1; continue
        b = a
        while b + 1 < N and HN[b + 1] and rows[b + 1]["ph"] == rows[a]["ph"] and rows[b + 1]["th"] == rows[a]["th"]: b += 1
        out.append((a, b)); a = b + 1
    return rows, o, E, out

def stats(g, s0, acc, name):
    rows, o, E, runs = runs_of(g, s0); n = g.n
    for a, b in runs:
        if b == a: continue
        T = b - a; rt = rf = ra = 0; per = {}; X = 0; cwne = 0; rises_total = 0
        for k in range(a, b):
            R0 = set(rows[k]["R"]) | {o}; R1 = set(rows[k + 1]["R"]) | {o}
            if R0 != R1: X += 1
            if cw_of(g, rows[k], o, E) != o: cwne += 1
            X0, X1 = rows[k]["Xi"], rows[k + 1]["Xi"]
            zs = [z for z in (R0 & R1) - {o} if E.key(X0[z]) < E.key(X1[z])]
            if zs:
                rt += 1; rises_total += len(zs)
                if rows[k]["fb"]: rf += 1
                else: ra += 1
                for z in zs: per[z] = per.get(z, 0) + 1
        bump(acc, "runs"); bump(acc, "transitions", T)
        mx(acc, "max_rise_transitions_per_run", rt, n, name, a, b, rf, ra, X)
        mx(acc, "max_rise_transitions_per_run_over_n", rt / n, n, name, a, b)
        mx(acc, "max_rises_per_vertex", max(per.values()) if per else 0, n, name, a, b)
        bump(acc, "rise_transitions_fallback", rf); bump(acc, "rise_transitions_S4a", ra)
        if cwne: bump(acc, "runs_with_cw_ne_o"); mx(acc, "max_rise_tr_cw_ne_o_run", rt, n, name, a, b, rf, ra, X)

if __name__ == "__main__":
    acc = {}; args = sys.argv[1:]; i = 0
    while i < len(args):
        f = args[i]; s0 = None
        if i + 1 < len(args) and args[i + 1].endswith(".state"): s0 = list(map(int, open(args[i + 1]).read().split())); i += 1
        try: g = load(f)
        except Exception: bump(acc, "load_fail"); i += 1; continue
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1: stats(g, s0, acc, f)
        else: bump(acc, "skipped_not_C1O")
        i += 1
    for key in sorted(acc): print(key, acc[key])
