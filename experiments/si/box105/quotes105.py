#!/usr/bin/env python3
"""L-SI box 105: the strings marked [Q] in docs/si/box105-key.md, checked at their sources (pinned commits, `git show`) and in the doc.
Usage: quotes105.py src   (needs the pinned refs fetched; prints one line per quote and a total)
       quotes105.py doc DOC.md   (every quoted string stands in DOC.md, up to line wrapping; exit 1 otherwise)"""
import sys, subprocess, re
TRUNK = "a9699c30c5cfce333b8c4b160321e42652d52560"; LNEW = "8db300fe3"
Q = [
 (TRUNK, "docs/RESULTS.md", "an IDEAL step moves every mover to the lexicographically least key (gate indices of the chain of W-targets under the new state, lowest level first) among its current option and the options with a strictly better Ξ-value, and the run stops when nothing is available or nothing changes"),
 (LNEW, "docs/new/P-N5-REACH.md", "a gate determines its pad, its owner and its faces"),
 (LNEW, "docs/new/P-N5-REACH.md", "e-indices follow gate indices ([DEF]; unchanged in Γ3)"),
 (TRUNK, "docs/RESULTS.md", "(T-BOUND) on 𝓛^R_d, F(l) ≤ 2^(l+2) − 2"),
]
norm = lambda t: re.sub(r"\s+", " ", t)
if sys.argv[1] == "src":
    fail = 0; cache = {}
    for ref, path, q in Q:
        if (ref, path) not in cache: cache[(ref, path)] = norm(subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True, text=True, check=True).stdout)
        ok = norm(q) in cache[(ref, path)]; fail += not ok; print(("OK   " if ok else "FAIL ") + f"{ref[:9]} {path}: {q[:70]}")
    print(f"QUOTES105 total {len(Q)} fail {fail}"); sys.exit(1 if fail else 0)
else:
    d = norm(open(sys.argv[2], encoding="utf-8").read()); miss = [q for _, _, q in Q if norm(q) not in d]
    print(f"QUOTES105 doc: {len(Q) - len(miss)} of {len(Q)} quoted strings present"); sys.exit(1 if miss else 0)
