#!/usr/bin/env python3
"""Box 48 climber (DATA): mutate a game (box43 climb.mutate) to maximise, lexicographically, (max NCONF_{>=2} in one phase, max N_ep^{>=2} in one
phase) from the S3 start; NCONF_{>=2} := distinct configurations sigma-bar|Q with |D_C| >= 2. Prints each improvement with n, sum_q deg(q) and
prod_q deg(q). Usage: ncclimb.py K NMAX STEPS SEED OUTDIR [--seed FILE.pg]"""
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
        rows.append((tuple(x[0] for x in vs), tuple(t), tuple(sb[q] for q in Q), sum(1 for q in Q if sb[q] != t[q])))
        if r is None: break
        s, t = r[0], r[1]
    best = (0, 0); i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1][:2] == rows[i][:2]: j += 1
        ph = rows[i:j + 1]
        c2 = len({r[2] for r in ph if r[3] >= 2}); e2 = sum(1 for k in range(len(ph)) if ph[k][3] >= 2 and (k == 0 or ph[k][2] != ph[k - 1][2]))
        best = max(best, (c2, e2)); i = j + 1
    return best
if __name__ == "__main__":
    K, NMAX, STEPS, SEED = map(int, sys.argv[1:5]); OUT = sys.argv[5]; os.makedirs(OUT, exist_ok=True); rng = random.Random(SEED)
    g = load(sys.argv[sys.argv.index("--seed") + 1]) if "--seed" in sys.argv else None
    while g is None: g = rand_ckO(rng, K + 2, max(K + 3, NMAX // 2), K)
    NMAX = max(NMAX, g.n); O = odd_choices(g)
    try: best = score(g)
    except RecursionError: best = (0, 0)
    print("start", best, "n", g.n, flush=True)
    for t in range(STEPS):
        r = climb.mutate(rng, g, O, NMAX, None)
        if r is None: continue
        h, O2, _ = r
        try: sc = score(h)
        except RecursionError: continue
        if sc >= best:
            if sc > best:
                Q = [v for v in range(h.n) if h.owner[v] == 1 and len(h.succ[v]) >= 2]; pd = 1
                for q in Q: pd *= len(h.succ[q])
                print(t, sc, "n", h.n, "|Q|", len(Q), "sumdeg", sum(len(h.succ[q]) for q in Q), "proddeg", pd, flush=True)
                climb.save(os.path.join(OUT, f"best_nc_k{K}_n{NMAX}_s{SEED}.pg"), h, None, {"NCONF2": sc[0], "NEP2": sc[1]})
            g, O, best = h, O2, sc
    print("done", best, flush=True)
