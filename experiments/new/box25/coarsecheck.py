#!/usr/bin/env python3
"""Box 27, COARSE check. In a (τ, joint-λ, θ, w)-stretch with (h) at every state, θ ◁ w and no S4c fallback, let u* = the most
relevant vertex of P(θ) Δ P(w) (if P(θ) = P(w): u* := none, coarse keeps the whole path set). COARSE(v) := (cycle node, path vertices
more relevant than u*), length ignored. Claims checked:
  (C1) coarse Ξ = coarse W at every vertex;
  (C2) coarse values change only within the first n − 1 transitions of the stretch (coarse R17);
  (C3) every re-entry into R (after any leave inside the stretch) has coarse Ξ(x) strictly higher than at the leave
       (when u* exists).
Usage: coarsecheck.py game.pg [start] | coarsecheck.py --random N lo hi seed [--randstart]"""
from common import *
from thtrace import Rset
from wdrop_h import oncycle
from collections import Counter
WITHFB = False
def coarse(E, val, ustar):
    c, mask, _ = val
    if ustar is None: return E.key((c, mask, 0))[:2]
    hi = sum(1 << r for r in range(E.rank[ustar] + 1, E.n))
    return E.key((c, mask & hi, 0))[:2]
def run(g, start, cnt):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); rows = []
    while True:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0]
        rows.append(dict(key=((tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), E.key(Xi[o]), E.key(W[o])),
                         ok=h and E.key(Xi[o]) < E.key(W[o]), Xi=Xi, W=W, R=Rset(g, s, t, o), fb=0, th=Xi[o], w=W[o]))
        r = step(g, E, Ed, s, t)
        if r is None: break
        rows[-1]["fb"] = r[4]; s, t = list(r[0]), list(r[1])
    k = 0
    while k < len(rows):
        if not rows[k]["ok"]: k += 1; continue
        j = k
        while j + 1 < len(rows) and rows[j + 1]["ok"] and rows[j + 1]["key"] == rows[k]["key"] and (WITHFB or not rows[j]["fb"]): j += 1
        if j > k:
            th, w = rows[k]["th"], rows[k]["w"]; d = th[1] ^ w[1]
            ustar = None
            if d:
                top = max(r for r in range(E.n) if d >> r & 1); ustar = [v for v in range(E.n) if E.rank[v] == top][0]
            cnt["stretches"] += 1
            C = [[coarse(E, rows[i]["Xi"][v], ustar) for v in range(g.n)] for i in range(k, j + 1)]
            for i in range(k, j + 1):
                for v in range(g.n):
                    if coarse(E, rows[i]["Xi"][v], ustar) != coarse(E, rows[i]["W"][v], ustar): cnt["C1_fail"] += 1
            last = 0
            for i in range(1, len(C)):
                if C[i] != C[i - 1]: last = i
            cnt["max_last_coarse_change"] = max(cnt["max_last_coarse_change"], last)
            if last > g.n - 1: cnt["C2_fail"] += 1
            leave = {}
            for i in range(k, j):
                for x in range(g.n):
                    if g.owner[x] != 0: continue
                    if x in rows[i]["R"] and x not in rows[i + 1]["R"]: leave[x] = i; cnt["leaves_fb" if rows[i]["fb"] else "leaves_arena"] += 1
                    elif x not in rows[i]["R"] and x in rows[i + 1]["R"] and x in leave:
                        cnt["reentries"] += 1
                        if ustar is None: cnt["reentries_no_ustar"] += 1
                        elif not C[i + 1 - k][x] > C[leave[x] - k][x]: cnt["C3_fail_after_fb" if rows[leave[x]]["fb"] else "C3_fail"] += 1
            cnt["stretch_len_max"] = max(cnt["stretch_len_max"], j - k)
        k = j + 1
if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if "--withfb" in a: a.remove("--withfb"); WITHFB = True
    if a[0] == "--random":
        RS = "--randstart" in a; N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.1)
            if g is None: continue
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            run(g, st, cnt)
        print(dict(cnt))
    else:
        g = load(a[0]); run(g, readstart(a[1]) if len(a) > 1 else None, cnt); print(a[0], "n", g.n, dict(cnt))
