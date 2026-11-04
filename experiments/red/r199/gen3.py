#!/usr/bin/env python3
"""L-RED R199 GEN3: the period-8 three-level doubling target (levels 0..3 of a width-2 ladder): level 0 carries at 9, 17 (u0 / v0
LAG moves); level 1 moves at 1, 9, 17 (prompt mover) and 5, 13, 21 (late, offset 4); level 2 at every level-1 carry (prompt) and
2 later; level 3 at every level-2 carry and 1 later. F = [2, 6, 12, 24] at L 24 if the W side allows it. SWAP bits choose which of
u_l / v_l is the prompt mover. Extra levels / helpers come from the caller. Usage: gen3.py swapmask out.json"""
import sys, json, itertools
sys.path.insert(0, '.')
import build
def moves3(swap, P=8, nper=3, base_lev=0):
    L = P * nper; m = {}
    def put(l, prompt, late):
        a, b = (2 * l, 2 * l + 1) if not (swap >> l) & 1 else (2 * l + 1, 2 * l)
        m[a] = set(prompt); m[b] = set(late)
    put(0, [P + 1], [2 * P + 1]) if nper == 3 else None
    put(1, [1 + P * i for i in range(nper)], [1 + P // 2 + P * i for i in range(nper)])
    put(2, [1 + P // 2 * i for i in range(2 * nper)], [1 + P // 4 + P // 2 * i for i in range(2 * nper)])
    put(3, list(range(1, L + 1, 2)), list(range(2, L + 1, 2)))
    return L, m
if __name__ == "__main__":
    best = None
    for swap in range(16):
        L, m = moves3(swap); T = build.build(L, 4, m)
        print("swap", swap, "F", T["F"], "W-viol", len(T["bad"]), T["bad"][:6], "req", T["nreq"])
        if not T["bad"] and (best is None or sum(T["F"]) > sum(best["F"])): best = T
    if best: json.dump(best, open(sys.argv[1], "w"))
