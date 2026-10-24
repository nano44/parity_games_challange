#!/usr/bin/env python3
"""Box 26, Lemma PIECE check. A PIECE is a maximal run of transitions inside one (τ, joint-λ)-phase with θ, w constant, (h) at every
state, no S4c fallback, and no vertex crossing between R and F (R_k = R_{k+1}). Claim (READING): N5 restricted to R is an R17 arena
run of the route game and restricted to F an R17 arena run of the o-free game, so a piece has ≤ n − 2 value-changing transitions
(changes of Ξ or W). Reports the longest piece (value-changing transitions) vs n − 2, and per (θ, w)-stretch the number of crossing
transitions. Usage: piececheck.py game.pg [start] | piececheck.py --random N lo hi seed [--randstart]"""
from common import *
from thtrace import Rset
from wdrop_h import oncycle
from collections import Counter
def run(g, start, cnt):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); rows = []
    while True:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); Eg, W = wvals(g, s, t)
        h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0]
        rows.append(dict(lam=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), th=E.key(Xi[o]), w=E.key(W[o]), h=h, R=Rset(g, s, t, o),
                         val=(tuple(E.key(x) for x in Xi), tuple(E.key(x) for x in W)), fb=0))
        r = step(g, E, Ed, s, t)
        if r is None: break
        rows[-1]["fb"] = r[4]; s, t = list(r[0]), list(r[1])
    piece = 0; cross = 0
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        same = a["lam"] == b["lam"] and a["th"] == b["th"] and a["w"] == b["w"]
        if not same:
            piece = 0; cross = 0; continue
        if a["R"] != b["R"]:
            cross += 1; cnt["max_cross_per_stretch"] = max(cnt["max_cross_per_stretch"], cross); piece = 0; continue
        if not (a["h"] and b["h"]) or a["fb"]: piece = 0; continue
        if a["val"] != b["val"]:
            piece += 1
            if piece > cnt["max_piece"]: cnt["max_piece"] = piece; cnt["max_piece_n"] = g.n
            if piece > g.n - 2: cnt["PIECE_VIOLATION"] += 1
if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0] == "--random":
        RS = "--randstart" in a; N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            run(g, st, cnt)
        print(dict(cnt))
    else:
        g = load(a[0]); run(g, readstart(a[1]) if len(a) > 1 else None, cnt); print(a[0], "n", g.n, dict(cnt))
