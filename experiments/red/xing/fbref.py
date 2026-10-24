#!/usr/bin/env python3
"""Check of L-NEW's CONJECTURE (FBRE-F) (docs/new/N5-NH-box28.md §5b, l-new 2a195b3): in a (w, u*)-run, no vertex evicted from R by
an (Even S4c) fallback after the coarse freeze (run index >= n - 1) re-enters R later in that run.
(w, u*)-run = maximal consecutive states of one joint λ-phase (phaseprofile key) with (h), θ ◁ w, w fixed, u* fixed (as xclimb cycu).
Uses L-NEW's box25 helpers unmodified (step, Rset, wvals, oncycle). Prints per game: runs longer than n - 1, post-freeze fallback
evictions, their re-entries (VIOLATIONS), pre-freeze evictions re-entering (FBRE, allowed), and fallback waves in the longest run.
Usage: LNEW_BOX25=... fbref.py game.pg ..."""
import sys, os
sys.path.insert(0, os.environ["LNEW_BOX25"])
from common import *
from wdrop_h import oncycle
from thtrace import Rset

def analyse(g, cap=2000):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, None); rows = []; k = 0
    while k < cap:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0]
        pk = (tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]); th, w = E.key(Xi[o]), E.key(W[o])
        d = Xi[o][1] ^ W[o][1]; us = (d.bit_length() - 1) if d else None
        rows.append(dict(rk=(pk, w, us) if h and th < w else None, R=Rset(g, s, t, o), fb=0))
        r = step(g, E, Ed, s, t)
        if r is None: break
        rows[-1]["fb"] = int(bool(r[4]) and list(r[1]) == list(t)); s, t = list(r[0]), list(r[1]); k += 1
    out = dict(long_runs=0, post_ev=0, VIOL=0, pre_fbre=0, max_run=0, waves_max=0); i = 0; ex = []
    while i < len(rows):
        if rows[i]["rk"] is None: i += 1; continue
        j = i
        while j + 1 < len(rows) and rows[j + 1]["rk"] == rows[i]["rk"]: j += 1
        L = j - i; out["max_run"] = max(out["max_run"], L)
        if L > g.n - 1: out["long_runs"] += 1
        waves = 0
        for a in range(i, j):
            if not rows[a]["fb"]: continue
            ev = rows[a]["R"] - rows[a + 1]["R"]
            if ev: waves += 1
            for x in ev:
                post = a - i >= g.n - 1
                if post: out["post_ev"] += 1
                back = next((b for b in range(a + 2, j + 1) if x in rows[b]["R"]), None)
                if back is not None:
                    if post: out["VIOL"] += 1; ex.append((x, i, a, back))
                    else: out["pre_fbre"] += 1
        out["waves_max"] = max(out["waves_max"], waves)
        i = j + 1
    return out, ex[:5]

if __name__ == "__main__":
    for p in sys.argv[1:]:
        g = load(p); o, ex = analyse(g)
        print(f"{os.path.basename(p)} n={g.n} {o}" + (f" EXAMPLES (x, run start, eviction, re-entry): {ex}" if ex else ""), flush=True)
