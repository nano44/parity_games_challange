#!/usr/bin/env python3
"""L-RED box 6 (produced on Opus 5.5): (K4-B) gadget with a pruning chain of length k (docs/red/R25). Vertices:
u (3, Odd) -> e, b';  e (4, Even) -> u;  a_1 (6, Even) -> e, c;  a_i (4+2i, Even) -> a_{i-1}, c;  b' (2k+5, Even) -> a_k;
c (2k+7, Odd) -> c. Round i of the first best_vertices call prunes a_{i-1} (a_0 = e); prevV = {a_k}; the threshold
piece then moves b' to X; at the next piece u's edge to b' lies outside R, u joins e's region, and that region is
Odd-won. Usage: gen_chain.py k > game.pg"""
import sys
k = int(sys.argv[1])
rows = [("u", 3, 1, ["e", "bp"]), ("e", 4, 0, ["u"])]
for i in range(1, k + 1): rows.append((f"a{i}", 4 + 2 * i, 0, ["e" if i == 1 else f"a{i-1}", "c"]))
rows += [("bp", 2 * k + 5, 0, [f"a{k}"]), ("c", 2 * k + 7, 1, ["c"])]
rows.sort(key=lambda r: r[1]); idx = {r[0]: i for i, r in enumerate(rows)}
print(f"parity {len(rows) - 1};")
for i, (nm, p, o, s) in enumerate(rows): print(f'{i} {p} {o} {",".join(str(idx[w]) for w in s)} "{nm}";')
