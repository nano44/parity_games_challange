#!/usr/bin/env python3
"""L-RED R199 GENK: k nested doubling levels (levels 1..k over base level 0, F_0 = 2), period P = 2^k, L = 3P: level-0 carries at
P + 1, 2P + 1; level j moves at every level-(j-1) carry (prompt mover) and P / 2^j later (late mover). F = [2, 6, 12, ..., 3 * 2^k]
(levels 1..k double). Writes the req.py target (main levels 0..k). Usage: genk.py k swapmask out.json"""
import sys, json
sys.path.insert(0, '.')
import build
k, swap, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; P = 2 ** k; L = 3 * P; m = {}
def put(l, prompt, late):
    a, b = (2 * l, 2 * l + 1) if not (swap >> l) & 1 else (2 * l + 1, 2 * l)
    m[a] = set(prompt); m[b] = set(late)
put(0, [P + 1], [2 * P + 1])
for j in range(1, k + 1):
    per = P // 2 ** (j - 1); put(j, list(range(1, L + 1, per)), list(range(1 + per // 2, L + 1, per)))
T = build.build(L, k + 1, m); print("GENK k", k, "L", L, "F", T["F"], "W-viol", T["bad"], "req", T["nreq"]); json.dump(T, open(out, "w"))
