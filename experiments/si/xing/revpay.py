#!/usr/bin/env python3
"""L-SI box 4 (a): what each reversal of R pays with. For every reversal (zcount.py signs) in the longest phase: type ('+-', '-+',
'±'), whether the reversing transition is a fallback, the state kind at k (E: Ξ = W; T: (h) and Ξ ≠ W; N: (h) fails), and what
changed since the previous crossing transition: θ, w, (h) lost somewhere, fallback somewhere.
Usage: revpay.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zcount import *

def scan(path):
    g = load(path); rows, ph = profile(g); assert_run(g, rows); annotate(g, rows)
    agg = {}
    for (x, y) in ph:
        Z, sg = zsigns(rows, x, y); prev = None; prevk = None
        for s, k in sg:
            rev = s == "±" or (prev is not None and s != prev)
            if rev:
                a = prevk + 1 if prevk is not None else x
                th = any(rows[i]["th"] != rows[i + 1]["th"] for i in range(a, k + 1))
                w = any(rows[i]["w"] != rows[i + 1]["w"] for i in range(a, k + 1))
                nh = any(not all(rows[i]["h"]) for i in range(a, k + 2))
                fbb = any(rows[i]["fb"] for i in range(a, k))
                key = (("±" if s == "±" else prev + s), "fb" if rows[k]["fb"] else "ar", kindstate(rows[k]),
                       "θ" if th else "-", "w" if w else "-", "¬h" if nh else "-", "fb-between" if fbb else "-")
                agg[key] = agg.get(key, 0) + 1
            if s != "±": prev = s
            prevk = k
    return agg

if __name__ == "__main__":
    tot = {}
    for p in sys.argv[1:]:
        for k, c in scan(p).items(): tot[k] = tot.get(k, 0) + c
    for k, c in sorted(tot.items(), key=lambda t: -t[1]): print(c, k)
