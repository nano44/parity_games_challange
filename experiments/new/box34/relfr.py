#!/usr/bin/env python3
"""Box 34: Corollary NL-MF (docs/new/N5-REL-box34.md). At an in-phase S4a step j -> j+1 with (h) at j, put MF_j := max level of the
gates (y, z) at j with z in F_j (⊥ = -2 if none). Lemma NL (R29) with L := MF_j gives: if r_j > MF_j then no vertex leaves R and
MF_{j+1} <= MF_j. Checks both, and classifies every exit release (an exit of o leaving R at an S4a step) by r vs MF and by the gates
into F of level >= r (tail in R or F). Usage: relfr.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box33")); sys.path.insert(0, os.path.join(HERE, "..", "box32"))
from scopecov import h2
from dormant import *

def bump(acc, k, d=1): acc[k] = acc.get(k, 0) + d

def mf(E, g, row, o):
    Rb = set(row["R"]) | {o}; s = tuple(row["s"]); Xi = row["Xi"]
    gl = [(lev(Xi[s[y]], Xi[z]), y, z) for y, z in E.improving(s, Xi) if z not in Rb]
    return max([l for l, _, _ in gl] + [-2]), gl

def check(g, acc, name):
    rows, o = rows_w(g); E = Engine(g); n = g.n; ex = set(g.succ[o])
    for j in range(len(rows) - 1):
        a, b = rows[j], rows[j + 1]
        if a["ph"] != b["ph"] or a["fb"]: continue
        hh = a["h1"] and h2(a["nxt"], o) and a["Xi"][o][0] == a["W"][o][0]
        R0, R1 = set(a["R"]), set(b["R"]) | {o}
        lv = [v for v in R0 if v != o and v not in R1]; rel = [v for v in lv if v in ex]
        if not hh:
            if rel: bump(acc, "rel_noh")
            continue
        r = lev(a["Xi"][o], a["W"][o]); M, gl = mf(E, g, a, o); M1, _ = mf(E, g, b, o)
        bump(acc, "h_steps")
        wch = a["w"] != b["w"]
        if r > M:
            bump(acc, "frozen_steps")
            if lv: bump(acc, "NLMF_leave_FAIL"); acc.setdefault("ex_leave", (name, j))
            if M1 > M: bump(acc, "NLMF_mono_FAIL"); acc.setdefault("ex_mono", (name, j, M, M1))
        for q in rel:
            key = "rel_" + ("wchg" if wch else "wfix") + ("_frozen" if r > M else "_open")
            bump(acc, key)
            hi = [(l, y, z) for l, y, z in gl if l >= r]
            tails = "".join(sorted(set("R" if y in R0 else ("o" if y == o else "F") for _, y, _ in hi)))
            bump(acc, "relgates_tail_" + (tails or "none"))
            acc.setdefault("rel_list", []).append((name, j, q, r, M, a["M"], len(hi), tails, wch))
        if lv and not rel: bump(acc, "nonexit_leave_steps")

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a and a[0] == "--rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); d = 0
        while d < N:
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            check(g, acc, f"rand{seed}_{d}"); d += 1
    else:
        for f in a:
            g = load(f)
            if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
            check(g, acc, os.path.basename(f))
    rl = acc.pop("rel_list", [])
    for k in sorted(acc): print(k, acc[k])
    for x in rl: print("REL", *x)
