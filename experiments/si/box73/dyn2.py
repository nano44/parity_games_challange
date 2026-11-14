#!/usr/bin/env python3
"""L-SI box 73: frame dynamics (frame.py step rule, BIT-CHAIN keys) on every m = 2 frame system of tables.txt x c_1 in {0,1}^2.
Per system: T0[b] = max flip-free run length with external bit b (any start); one-flip runs (start, b, flip after pre steps of the
b-run, post = flip-free (not b)-run from there); T1 = max pre + post. Library use: import dyn2; dyn2.step(tab, c, s, bb)."""
import sys
m = 2; U = 4
def step(tab, c, s, bb):
    bit = bb; ns = s
    for l in range(1, m + 1):
        kp = 1 - bit
        for z in (2 * (l - 1), 2 * (l - 1) + 1):
            cz = (tab[z] >> s) & 1
            if cz != ((s >> z) & 1) and cz == kp: ns ^= 1 << z
        if l < m:
            a, b2 = (ns >> (2 * (l - 1))) & 1, (ns >> (2 * (l - 1) + 1)) & 1
            bit = (1 - bit if a else bit) if a != b2 else c[(l, a)]
    return ns
def run(tab, c, s, bb, cap=64):
    seq = [s]
    while len(seq) <= cap:
        n = step(tab, c, seq[-1], bb)
        if n == seq[-1]: return seq
        seq.append(n)
    raise RuntimeError("cycle")
def analyse(tab, c):
    T0 = [0, 0]; T1 = 0; pq = set(); runs = {}
    for b in (0, 1):
        for s in range(1 << U):
            runs[(s, b)] = run(tab, c, s, b); T0[b] = max(T0[b], len(runs[(s, b)]) - 1)
    for b in (0, 1):
        for s in range(1 << U):
            seq = runs[(s, b)]
            for p in range(len(seq)):
                q = len(runs[(seq[p], 1 - b)]) - 1; pq.add((b, p, q)); T1 = max(T1, p + q)
    return T0, T1, pq
if __name__ == "__main__":
    tabs = [tuple(int(w, 16) for w in l.split()) for l in open("tables.txt")]
    mx = {}; best = [0, 0, 0]
    for tab in tabs:
        for cc in range(4):
            c = {(1, 0): cc & 1, (1, 1): cc >> 1}
            T0, T1, pq = analyse(tab, c)
            key = (max(T0), min(T0), T1); mx[key] = mx.get(key, 0) + 1
    for k in sorted(mx): print("maxT0 %d minT0 %d T1 %d : %d systems" % (k + (mx[k],)))
