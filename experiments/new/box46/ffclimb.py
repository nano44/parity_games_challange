#!/usr/bin/env python3
"""Box 46 climber (DATA) against CONJECTURE HON-FF (docs/new/N5-REC1-box46.md §1a): mutate a game (box43 climb.mutate) to maximise,
lexicographically, (gaps between consecutive W-honest states that contain a fallback at a non-honest state AND end with no LEV rise,
the number of such inside-fallback gaps, the fallbacks at non-honest states after an honest state of their phase), from the S3 start. LEV = levels.level in G_tau (exact; gaps whose levels hit the budget are
skipped). A score with first entry > 0 is a counterexample candidate (saved; re-check by hand). Usage: ffclimb.py K NMAX STEPS SEED OUTDIR [--seed FILE.pg]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, os.path.join(HERE, "..", "box21")); sys.path.insert(0, HERE)
import climb, hon, levels as L
from multi import rand_ckO, odd_choices
from n5x import load, step, start_pair, Engine, dual
climb.DEG2 = False
def score(g, budget=300000, cap=2000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None); rows = []
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t); w = hon.wvals(g, s, t)
        rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), hon=(tuple(vs) == tuple(w)), xi=vs, fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    bad = gaps = pre = 0; i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        a, b = i, j; i = j + 1; H = [k for k in range(a, b + 1) if rows[k]["hon"]]; tau = rows[a]["t"]
        pre += sum(1 for k in range(a, b) if rows[k]["fb"] and not rows[k]["hon"] and H and H[0] < k)
        frame = [[tau[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)]
        for h0, h1 in zip(H, H[1:]):
            if not any(rows[k]["fb"] for k in range(h0 + 1, h1)): continue
            gaps += 1
            try: l0, l1 = L.level(E, g, frame, rows[h0]["xi"], (), budget), L.level(E, g, frame, rows[h1]["xi"], (), budget)
            except L.Unknown: continue
            if l1 <= l0 < g.n - 1: bad += 1
    return (bad, gaps, pre)
if __name__ == "__main__":
    K, NMAX, STEPS, SEED = map(int, sys.argv[1:5]); OUT = sys.argv[5]; os.makedirs(OUT, exist_ok=True); rng = random.Random(SEED)
    g = load(sys.argv[sys.argv.index("--seed") + 1]) if "--seed" in sys.argv else None
    while g is None: g = rand_ckO(rng, K + 2, max(K + 3, NMAX // 2), K)
    NMAX = max(NMAX, g.n); O = odd_choices(g)
    try: best = score(g)
    except RecursionError: best = (0, 0, 0)
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
                climb.save(os.path.join(OUT, f"best_ff_k{K}_n{NMAX}_s{SEED}.pg"), h, None, {"BAD": sc[0], "GAPS": sc[1]})
            g, O, best = h, O2, sc
    print("done", best, flush=True)
