#!/usr/bin/env python3
"""Box 38 (c): τ(o) ≠ o HN fallback states (H1 ∧ ¬H2, in-phase Even fallback). Classifies by case (A: rank(o) > rank(c_θ)) and by
whether c_w = o, where c_w is the top of o's W-cycle. For each R -> R̄ gate (v, z): its honest lev against rank(o) and 0, and whether
v's or z's route meets C_W ∖ {o} (the W-cycle through o). Breaks in τ(o) ≠ o HN stretches, charged to θ-changes or low rises
(lowrise.py's rule). One Odd choice vertex asserted. Usage: taunot.py game.pg [game.state] ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from neb_run import *
from mono import lev

def run(g, s0, acc, name):
    assert sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1
    rows, o, E = trace(g, s0); N = len(rows); n = g.n; HN = [r["h1"] and not r["h2"] for r in rows]
    for a in range(N - 1):
        r = rows[a]
        if not (HN[a] and r["fb"] and rows[a + 1]["ph"] == r["ph"] and r["t"][o] != o): continue
        s, t = r["s"], r["t"]; nx = [s[v] if g.owner[v] == 0 else t[v] for v in range(n)]
        C = [o]; x = nx[o]
        while x != o: C.append(x); x = nx[x]
        cw = max(C, key=lambda v: E.rank[v]); case = "A" if E.rank[o] > E.rank[r["Xi"][o][0]] else "B"
        key = f"{case}_cw{'=o' if cw == o else '!=o'}"; bump(acc, key + "_fbstates")
        Rb = set(r["R"]) | {o}; Xi = r["Xi"]
        def meets(v):
            while v != o:
                if v in C: return True
                v = nx[v]
            return False
        for y, z in E.improving(tuple(s), Xi):
            if y in Rb and z in Rb and y != o:
                L = lev(Xi[s[y]], Xi[z]); cls = ">=ro" if L >= E.rank[o] else ("0..ro" if L >= 0 else "-1")
                bump(acc, f"{key}_RRgate_lev{cls}_meetsC{int(meets(y) or meets(z))}")
                if L >= E.rank[o] and case == "A": mx(acc, "ex_" + key + "_highgate", 1, n, name, a, y, z, L)

if __name__ == "__main__":
    acc = {}; args = sys.argv[1:]; i = 0
    while i < len(args):
        f = args[i]; s0 = None
        if i + 1 < len(args) and args[i + 1].endswith(".state"): s0 = list(map(int, open(args[i + 1]).read().split())); i += 1
        g = load(f)
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1: run(g, s0, acc, f)
        else: bump(acc, "skipped_not_C1O")
        i += 1
    for key in sorted(acc): print(key, acc[key])
