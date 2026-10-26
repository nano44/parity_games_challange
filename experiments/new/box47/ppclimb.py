#!/usr/bin/env python3
"""Box 47 climber (DATA) against CONJECTURE XD-1 (docs/new/N5-XDIR-box47.md): mutate a game (box43 climb.mutate) to maximise,
lexicographically, (max X_dir inside one U-run, max X_dir in one phase, max |D| = 2 states in one U-run, total X_dir), from the S3 start.
A U-run (U = {u, u'}) is a maximal run of one phase with D_k a subset of U. Two X_dir in one U-run = a ping-pong u -> u' -> u (or a
chain inside U). Usage: ppclimb.py K NMAX STEPS SEED OUTDIR [--seed FILE.pg]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box43", "../box21"): sys.path.insert(0, os.path.join(HERE, p))
import climb
from multi import rand_ckO, odd_choices
from n5x import load, step, start_pair, Engine, dual
climb.DEG2 = False

def score(g, cap=3000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append((tuple(x[0] for x in vs), tuple(t), frozenset(q for q in Q if sb[q] != t[q])))
        if r is None: break
        s, t = r[0], r[1]
    best = [0, 0, 0, 0]; i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1][:2] == rows[i][:2]: j += 1
        xs = [k for k in range(i, j) if len(rows[k][2]) == 1 and len(rows[k + 1][2]) == 1 and rows[k][2] != rows[k + 1][2]]
        best[1] = max(best[1], len(xs)); best[3] += len(xs)
        for k in xs:
            U = rows[k][2] | rows[k + 1][2]; x = y = k
            while x - 1 >= i and rows[x - 1][2] <= U: x -= 1
            while y + 1 <= j and rows[y + 1][2] <= U: y += 1
            best[0] = max(best[0], sum(1 for h in xs if x <= h < y))
            best[2] = max(best[2], sum(1 for h in range(x, y + 1) if rows[h][2] == U))
        i = j + 1
    return tuple(best)

if __name__ == "__main__":
    K, NMAX, STEPS, SEED = map(int, sys.argv[1:5]); OUT = sys.argv[5]; os.makedirs(OUT, exist_ok=True); rng = random.Random(SEED)
    g = load(sys.argv[sys.argv.index("--seed") + 1]) if "--seed" in sys.argv else None
    while g is None: g = rand_ckO(rng, K + 2, max(K + 3, NMAX // 2), K)
    NMAX = max(NMAX, g.n); O = odd_choices(g)
    try: best = score(g)
    except RecursionError: best = (0, 0, 0, 0)
    print("start", best, "n", g.n, flush=True)
    for t in range(STEPS):
        r = climb.mutate(rng, g, O, NMAX, None)
        if r is None: continue
        h, O2, _ = r
        try: sc = score(h)
        except RecursionError: continue
        if sc >= best:
            if sc > best:
                print(t, sc, "n", h.n, flush=True)
                climb.save(os.path.join(OUT, f"best_pp_k{K}_n{NMAX}_s{SEED}.pg"), h, None, {"URUNX": sc[0], "XDPH": sc[1]})
            g, O, best = h, O2, sc
    print("done", best, flush=True)
