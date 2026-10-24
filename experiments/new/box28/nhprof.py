#!/usr/bin/env python3
"""Box 28 (NH): per state of an N5 run on a C^1O game, which clause of (h) fails.
(h) at k (P-N5-RE §0): H1 the honest play from o (σ, σ̄) does not return to o; H2 the W-play from o (σ, τ) does not return to o;
H3 Ξ(o) and W(o) have the same cycle node. Phases as in box25/phaseprofile.py: maximal runs with (λ_Ξ, λ_U, τ(o)) constant.
A transition k -> k+1 is non-(h) if (h) fails at k or at k+1 (phaseprofile convention).
Usage: nhprof.py game.pg [start]            per-state table of the phases with a non-(h) transition
       nhprof.py --rand N lo hi seed [--randstart] [--write out.pg]   random o-cyclic C^1O; histogram and max per phase"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../box25"))
from common import *
from wdrop_h import oncycle

def profile(g, start=None):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); rows = []
    while True:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        h1 = not oncycle(g, s, sb, o); h2 = not oncycle(g, s, t, o); h3 = Xi[o][0] == W[o][0]
        r = step(g, E, Ed, s, t)
        fb = r[4] if r else None
        rows.append(dict(ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), h=(h1, h2, h3), split=sb[o] != t[o], fb=fb, tauch=None,
                         th=E.key(Xi[o]), w=E.key(W[o]), Xk=tuple(E.key(Xi[v]) for v in range(g.n)), Wk=tuple(E.key(W[v]) for v in range(g.n)), s=tuple(s), t=tuple(t)))
        if r is None: break
        s, t = r[0], r[1]
    for k in range(len(rows) - 1): rows[k]["tauch"] = rows[k]["t"] != rows[k + 1]["t"]
    ph, a = [], 0
    for i in range(1, len(rows) + 1):
        if i == len(rows) or rows[i]["ph"] != rows[i - 1]["ph"]: ph.append((a, i - 1)); a = i
    return rows, ph

def nh_in(rows, a, b):
    return [k for k in range(a, b) if not (all(rows[k]["h"]) and all(rows[k + 1]["h"]))]

def nh_split(rows, a, b):
    """non-(h) transitions with σ̄(o) ≠ τ(o) at k or k+1 (where the honest play and the W-play can differ)"""
    return [k for k in nh_in(rows, a, b) if rows[k]["split"] or rows[k + 1]["split"]]

def clause(hh):
    return "".join(n for n, x in zip(("1", "2", "3"), hh) if not x) or "-"

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] != "--rand":
        g = load(a[0]); rows, ph = profile(g, readstart(a[1]) if len(a) > 1 else None)
        for (x, y) in ph:
            nh = nh_in(rows, x, y)
            if not nh: continue
            print(f"phase {x}..{y} ({y - x} transitions), non-(h) transitions {len(nh)}")
            for k in range(x, y + 1):
                r = rows[k]
                dx = sum(rows[k+1]["Xk"][v] != r["Xk"][v] for v in range(g.n)) if k < y else '-'
                dw = sum(rows[k+1]["Wk"][v] != r["Wk"][v] for v in range(g.n)) if k < y else '-'
                print(f"  k {k}: failing (h) clauses {clause(r['h']):3s} split {int(r['split'])} fb {r['fb']} τ-change {r['tauch']} Ξ-changed vertices {dx} W-changed {dw} θ {r['th']} w {r['w']} τ(o) {r['ph'][2]}")
        sys.exit()
    RS = "--randstart" in a; out = a[a.index("--write") + 1] if "--write" in a else None
    N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
    runs = 0; best = (0, None); bestv = (0, None); vh = {}; bests = (0, None); sh = {}; hist = {}; tot = {"nh_tr": 0, "tr_in_long_phases": 0}; cl = {}
    for i in range(N):
        g = rand_c1o(rng, lo, hi, forced=0.0)
        if g is None: continue
        start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                 {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
        rows, ph = profile(g, start); runs += 1
        for (x, y) in ph:
            nh = nh_in(rows, x, y); hist[len(nh)] = hist.get(len(nh), 0) + 1; tot["nh_tr"] += len(nh)
            nhv = [k for k in nh if rows[k]["Xk"] != rows[k + 1]["Xk"]]; vh[len(nhv)] = vh.get(len(nhv), 0) + 1
            if len(nhv) > bestv[0]: bestv = (len(nhv), (g, start, x, y, g.n))
            ns_ = nh_split(rows, x, y); sh[len(ns_)] = sh.get(len(ns_), 0) + 1
            if len(ns_) > bests[0]: bests = (len(ns_), (g, start, x, y, g.n))
            for k in nh:
                for kk in (k, k + 1):
                    c = clause(rows[kk]["h"]); cl[c] = cl.get(c, 0) + 1
            if len(nh) > best[0]:
                best = (len(nh), (g, start, x, y, g.n))
    print(f"runs {runs}; phases by #non-(h) transitions {dict(sorted(hist.items()))}; failing-clause counts over endpoint states {cl}")
    print(f"phases by #Ξ-changing non-(h) transitions {dict(sorted(vh.items()))}")
    print(f"phases by #SPLIT non-(h) transitions {dict(sorted(sh.items()))}" + (f"; max {bests[0]} (n {bests[1][4]})" if bests[1] else ""))
    if bestv[1]: print(f"max Ξ-changing non-(h) transitions in one phase: {bestv[0]} (n {bestv[1][4]}, phase {bestv[1][2]}..{bestv[1][3]})")
    if best[1]:
        g, start, x, y, n = best[1]; print(f"max non-(h) transitions in one phase: {best[0]} (n {n}, phase {x}..{y})")
        if out:
            from abovefind import write
            E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start)
            write(g, ({v: s[v] for v in range(g.n) if g.owner[v] == 0}, {v: t[v] for v in range(g.n) if g.owner[v] == 1}), out)
