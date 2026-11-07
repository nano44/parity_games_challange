#!/usr/bin/env python3
"""L-RED R159: designed depth-h chain (self-referential gates, after l-new box 109's hit_b6a_1 reading).
Carrier v (Even, even prio E) -> y_h; gate y_i (Even) -> {c_i (odd digit marker m_i) -> y_(i-1), o_i}; o_i (Odd) -> {y_(i-1) (tau), v};
y_0 = z (sink, odd self-loop). Priorities: low vertices 0, z 3, E 4, m_h 5 < m_(h-1) 7 < ... < m_1 2h + 3 (m_1 = top digit, nearest z).
Gate i is Xi-open iff no digit m_j (j > i) is still on v's play: the back-edge v carries v's own play, so both sides of the comparison
share the same suffix (no root mismatch). Expected: digits fixed bottom-up, one per transition, hier depth h.
Usage: mkhd.py H OUT.pg OUT.start"""
import sys
h = int(sys.argv[1]); V, own, pr, E = [], {}, {}, {}
def add(nm, o, p, s): V.append(nm); own[nm] = o; pr[nm] = p; E[nm] = s
add("z", 0, 3, ["z"]); add("v", 0, 4, [f"y{h}"])
for i in range(h, 0, -1):
    nx = "z" if i == 1 else f"y{i - 1}"
    add(f"y{i}", 0, 0, [f"c{i}", f"o{i}"]); add(f"c{i}", 1, 2 * (h - i) + 5, [nx]); add(f"o{i}", 1, 0, [nx, "v"])
ix = {x: k for k, x in enumerate(V)}
with open(sys.argv[2], "w") as f:
    f.write(f"parity {len(V) - 1};\n")
    for x in V: f.write(f'{ix[x]} {pr[x]} {own[x]} {",".join(str(ix[w]) for w in E[x])} "{x}";\n')
with open(sys.argv[3], "w") as f:
    f.write("SIGMA0 " + " ".join(f"{ix[x]}:{ix[E[x][0]]}" for x in V if own[x] == 0) + "\n")
    f.write("TAU0 " + " ".join(f"{ix[x]}:{ix[E[x][0]]}" for x in V if own[x] == 1) + "\n")
