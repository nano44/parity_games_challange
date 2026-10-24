#!/usr/bin/env python3
"""Counter-nesting depth of the theta-change level sequence of a joint lambda-phase (levels.py).  D(empty) = 0; otherwise split the
sequence at the occurrences of its maximum level M and set D = 1 + max D(pieces).  A k-bit binary counter has depth k; an
'additive' sequence (each level at most once) has depth = number of distinct levels but every piece is short.  Also prints,
per maximal level-block, how many changes occur between consecutive changes at levels >= r (max over r): 'max refix'."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import levels as LV
def depth(seq):
    if not seq: return 0
    M = max(seq); pieces = []; cur = []
    for x in seq:
        if x == M: pieces.append(cur); cur = []
        else: cur.append(x)
    pieces.append(cur)
    return 1 + max(depth(p) for p in pieces)
def pathdepth(seq):
    return depth([l for l in seq if l >= 0])
if __name__ == "__main__":
    for spec in sys.argv[1:]:
        p, _, s = spec.partition(":")
        n, seq = LV.run(p, s or None)
        L = [l for l, _ in seq]
        mult = max((sum(1 for l in L if l == r) for r in set(L) if r >= 0), default=0)
        print(f"{os.path.basename(p):22s} n={n} theta-changes={len(L)} path-set changes={sum(1 for l in L if l >= 0)} distinct levels={len(set(l for l in L if l >= 0))} max per level={mult} depth(all)={depth(L)} depth(path-set only)={pathdepth(L)}")
