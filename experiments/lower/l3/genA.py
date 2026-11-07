#!/usr/bin/env python3
"""Family A (docs/lower/L3-families.md §5), explicit formula. Writes A_d as box150 JSON (R110 wiring) to stdout.
Ranks (M = 4d options): low band: (2l, 0) has rank l - 1 (l >= 1); high band, with h(l) := (d - 1) + 3(d - 1 - l):
(2l+1, 0) -> h(l), (2l, 1) -> h(l) + 1, (2l+1, 1) -> h(l) + 2 for l >= 1; level 0: (0,0) 4(d-1), (1,1) 4(d-1)+1, (0,1) 4(d-1)+2,
(1,0) 4(d-1)+3. Parities: even (0) for (2l+1, *) and (0,1), (1,1); odd (1) otherwise. Xi-targets: (2l,0) -> 2l+1, (2l,1) -> 2l-1,
(2l+1,0) -> 2l-2, (2l+1,1) -> 2l-4 (X if l = 1); (0,0) -> X, (0,1) -> 1, (1,*) -> X. Gates: level 0: (0,0) 2, (0,1) 0, (1,0) 3,
(1,1) 1; level l >= 1: g(2l, j) < g(2l+1, j) (gamma_l(j) = 1). Start: 00 at level 0, 11 at every level >= 1.
Usage: genA.py d"""
import sys, json
def genA(d):
    N = 2 * d; opts = [None] * N; gate = [None] * N; br = [0] * (2 * N); bp = [0] * (2 * N)
    def setopt(x, k, wt, xt, r, p): br[2 * x + k] = r; bp[2 * x + k] = p; return [wt, xt, 2 * x + k]
    B = 4 * (d - 1)
    opts[0] = [setopt(0, 0, -1, -1, B, 1), setopt(0, 1, -1, 1 if d >= 1 else -1, B + 2, 0)]
    opts[1] = [setopt(1, 0, -1, -1, B + 3, 1), setopt(1, 1, -1, -1, B + 1, 0)]
    gate[0] = [2, 0]; gate[1] = [3, 1]
    for l in range(1, d):
        h = (d - 1) + 3 * (d - 1 - l); e, o = 2 * l, 2 * l + 1
        opts[e] = [setopt(e, 0, 2 * l - 2, o, l - 1, 1), setopt(e, 1, 2 * l - 1, 2 * l - 1, h + 1, 1)]
        opts[o] = [setopt(o, 0, 2 * l - 2, 2 * l - 2, h, 0), setopt(o, 1, 2 * l - 1, 2 * l - 4 if l >= 2 else -1, h + 2, 0)]
        gate[e] = [1000 + 4 * l, 1002 + 4 * l]; gate[o] = [1001 + 4 * l, 1003 + 4 * l]
    return {"N": N, "lev": [x // 2 for x in range(N)], "deg": 2, "opts": opts, "gate": gate, "br": br, "bp": bp,
            "start": [0, 0] + [1] * (N - 2)}
if __name__ == "__main__":
    print(json.dumps(genA(int(sys.argv[1]))))
