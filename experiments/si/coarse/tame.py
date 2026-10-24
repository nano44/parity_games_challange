#!/usr/bin/env python3
"""L-SI box 7: DATA for the tame refinement (docs/si/N5-C-box7.md §5). A transition k -> k+1 is TAME if COARSE_{M_k}(Ξ_{k+1}) =
COARSE_{M_k}(Ξ_k) pointwise (M_k = max gate level at k, mono.py). Per joint λ-phase: J = #non-tame transitions, how many of them are
NC failures (they all must be: Step 1), whether θ changes at level > M_k there, whether the next state has Ξ = W (θ = w; JUMP-EQ form),
fallbacks per tame block (max), M-increases at tame transitions (must be 0, Lemma MONO), and #evicting fallbacks (R→F switched edges).
Usage: tame.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fbcount import *
sys.path.insert(0, os.path.join(ROOT, "experiments/new/box28"))
from nhprof import wvals

def reach(g, s, t, o):
    nxt = lambda v: s[v] if g.owner[v] == 0 else t[v]; R = set()
    for v in range(g.n):
        if v == o: continue
        u = v; seen = set()
        while u not in seen and u != o: seen.add(u); u = nxt(u)
        if u == o: R.add(v)
    return R

def scan_t(g):
    E, out = states(g); n = g.n; o = odd_choice(g); assert o is not None, "not one-Odd-choice"
    Ed = n5.Engine(n5.dual(g))
    for a in out:
        gl = [lev(a["Xi"][a["s"][y]], a["Xi"][z]) for y, z in a["Is"]]; a["M"] = max(gl) if gl else -3
        a["key"] = (tuple(x[0] for x in a["Xi"]), a["t"], tuple(x[0] for x in Ed.evaluate(tuple(a["t"]))[0]))
        _, W = wvals(g, a["s"], a["t"]); a["W"] = W; a["R"] = reach(g, a["s"], a["t"], o)
    c = dict(tr=0, J=0, J_nc=0, J_thhigh=0, J_eq=0, Mup_tame=0, fb=0, evfb=0, maxfb_tblock=0, maxJ_phase=0, maxevfb_phase=0)
    ex = []
    j = 0
    while j < len(out) - 1:
        k = j
        while k + 1 < len(out) and out[k + 1]["key"] == out[j]["key"]: k += 1
        Jp = evp = 0; blk = None; bfb = 0
        for i in range(j, k):
            a, b = out[i], out[i + 1]; c["tr"] += 1; M = a["M"]
            tame = all(coarse(b["Xi"][v], M) == coarse(a["Xi"][v], M) for v in range(n))
            lam = [a["Xi"][v][0] for v in range(n)]
            nc = all(lam[t] == t for t in (max(C, key=lambda v: E.rank[v]) for C in cycles(g, b["s"], a["sb"])))
            if a["fb"]:
                c["fb"] += 1
                if any(y in a["R"] and b["s"][y] not in a["R"] and b["s"][y] != o for y in range(n) if g.owner[y] == 0 and b["s"][y] != a["s"][y]):
                    c["evfb"] += 1; evp += 1
            if not tame:
                Jp += 1; c["J"] += 1; c["J_nc"] += (not nc)
                c["J_thhigh"] += lev(a["Xi"][o], b["Xi"][o]) > M
                eq = b["Xi"][o] == b["W"][o]; c["J_eq"] += eq
                if not eq: ex.append(("J-not-eq", i, M, lev(a["Xi"][o], b["Xi"][o])))
                blk = None; continue
            if b["M"] > M: c["Mup_tame"] += 1; ex.append(("Mup", i))
            if blk != M:
                c["maxfb_tblock"] = max(c["maxfb_tblock"], bfb); blk = M; bfb = 0
            bfb += a["fb"]
        c["maxfb_tblock"] = max(c["maxfb_tblock"], bfb)
        c["maxJ_phase"] = max(c["maxJ_phase"], Jp); c["maxevfb_phase"] = max(c["maxevfb_phase"], evp)
        j = k + 1
    return c, ex

if __name__ == "__main__":
    T = {}
    for p in sys.argv[1:]:
        g = load(p); c, ex = scan_t(g)
        for kk, v in c.items(): T[kk] = max(T.get(kk, 0), v) if kk.startswith("max") else T.get(kk, 0) + v
        print(f"{os.path.basename(p):22s} n {g.n:3d}", c, ex[:4])
    print("TOTAL", T)
