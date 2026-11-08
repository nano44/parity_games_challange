#!/usr/bin/env python3
"""L-RED 59 R225: BIN(M), an explicit run of the chain system CS(M) (P-N5-ASC §2) whose hub takes 2^M - 1 distinct values.
Items 1..M (rank = number). Time t = 1..2^M - 1, S_t = {i : bit i-1 of t is 1}. Forest: next_t(x) = min{y in S_t : y > x} (else None).
Hub h_t = min S_t, so its value chain_t(h_t) = S_t. Checks: forests acyclic (next strictly increases), every item's chain lex
non-decreasing in t (lex = compare by the most relevant element of the symmetric difference), hub values distinct and increasing.
Usage: bin225.py M_max"""
import sys
def lexle(a, b):
    d = a ^ b
    return (not d) or (max(d) in b)
for M in range(1, int(sys.argv[1]) + 1):
    prev = {x: None for x in range(1, M + 1)}; ph = None; vals = set(); bad = 0
    for t in range(1, 2 ** M):
        S = {i + 1 for i in range(M) if t >> i & 1}
        nxt = {x: min([y for y in S if y > x], default=None) for x in range(1, M + 1)}
        assert all(nxt[x] is None or nxt[x] > x for x in nxt)
        ch = {}
        for x in range(1, M + 1):
            c = set(); y = x
            while y is not None: c.add(y); y = nxt[y]
            ch[x] = frozenset(c)
            if prev[x] is not None and not lexle(prev[x], ch[x]): bad += 1
            prev[x] = ch[x]
        h = ch[min(S)]
        if ph is not None and not (lexle(ph, h) and ph != h): bad += 1
        ph = h; vals.add(h)
    print(f"BIN M {M}: hub values {len(vals)} (2^M-1 = {2**M-1}), violations {bad}, max ascents {M-1}")
