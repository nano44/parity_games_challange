#!/usr/bin/env python3
"""L-SI box 4: classify crossings of N5 runs on one-Odd-choice games, per joint λ-phase (box 28 conventions: phases = maximal
runs with (λ_Ξ, λ_U, τ(o)) constant; R = vertices ≠ o whose (σ, τ)-play reaches o; reads experiments/new/box28 read-only).
Per transition k -> k+1: switched Even vertices S; ACTIVE crossers = switched vertices whose R-membership changes; PASSIVE = the
rest of R_k Δ R_{k+1}. Active kinds: EA (entry, arena step), LA (leave to an o-free target, arena), LF (leave at a fallback),
LL (loop-leave: new target was in R_k, but the new play closes a cycle avoiding o), E? / L? otherwise.
assert_run(): the profile's iteration and fallback counts equal experiments/new/n5.py run()'s (notes trap: never cite unchecked).
Usage: xclass.py game.pg [--all]    (prints per-phase totals; --all prints every crossing transition)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments/new/box28"))
from fbre import *          # profile, reach_o, odd_choice, load, Engine, wvals, vset, n5 (via n5x)
import n5

def assert_run(g, rows, start=None):
    it, fb, *_ = n5.run(g, "n5", start)
    assert (it, fb) == (len(rows) - 1, sum(1 for r in rows if r["fb"])), ((it, fb), len(rows) - 1)
    return it, fb

def classify(g, rows, k, o):
    s0, s1 = rows[k]["s"], rows[k + 1]["s"]; A, B = rows[k]["R"], rows[k + 1]["R"]
    S = [v for v in range(g.n) if g.owner[v] == 0 and s0[v] != s1[v]]
    act = []
    for y in S:
        if (y in A) == (y in B): continue
        z = s1[y]
        if y in B: kind = "EA" if not rows[k]["fb"] else "EF"
        elif rows[k]["fb"]: kind = "LF"
        elif z in A: kind = "LL"
        else: kind = "LA"
        act.append((y, kind))
    actset = {y for y, _ in act}
    passive = (A ^ B) - actset
    return S, act, passive

def annotate(g, rows):
    o = odd_choice(g)
    for r in rows: r["R"] = reach_o(g, r["s"], r["t"], o)
    return o

def phase_stats(g, start=None, show=False, name=""):
    rows, ph = profile(g, start); assert_run(g, rows, start); o = annotate(g, rows); out = []
    for (x, y) in ph:
        st = dict(phase=(x, y), T=y - x, X=0, EA=0, EF=0, LA=0, LF=0, LL=0, Pin=0, Pout=0, Xnoact=0, tc=0, wc=0, nh=0)
        for k in range(x, y):
            A, B = rows[k]["R"], rows[k + 1]["R"]
            st["tc"] += rows[k]["th"] != rows[k + 1]["th"]; st["wc"] += rows[k]["w"] != rows[k + 1]["w"]
            st["nh"] += not (all(rows[k]["h"]) and all(rows[k + 1]["h"]))
            if A == B: continue
            st["X"] += 1
            S, act, pas = classify(g, rows, k, o)
            if not act: st["Xnoact"] += 1
            for _, kd in act: st[kd] += 1
            st["Pin"] += len([v for v in pas if v in B]); st["Pout"] += len([v for v in pas if v in A])
            if show: print(f"  {name} k {k}: fb {rows[k]['fb']} θch {int(rows[k]['th'] != rows[k+1]['th'])} active {act} passive in {sorted(v for v in pas if v in B)} out {sorted(v for v in pas if v in A)} |R| {len(A)}->{len(B)}")
        out.append(st)
    return rows, out

if __name__ == "__main__":
    g = load(sys.argv[1]); nm = os.path.basename(sys.argv[1])
    rows, out = phase_stats(g, show="--all" in sys.argv, name=nm)
    for st in out:
        if st["T"] >= 4: print(nm, "n", g.n, st)

def eqthr(r):
    """'E' if θ = w at the state, 'T' if θ ◁ w (throttled), 'N' if (h) fails."""
    return "N" if not all(r["h"]) else ("E" if r["th"] == r["w"] else "T")
