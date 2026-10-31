#!/usr/bin/env python3
"""L-RED R145 (a): attack on L-SI box 52 CONJECTURE FLIP-EV, on L-COMP's n5b SPEC (independent of L-SI's n5x). In a W-run (tau fixed,
lambda_W map constant, no fallback, sigma moves): an EXI / MOV sigma-bar flip at Odd o (sigmabar_k(o) != tau(o), sigmabar_(k+1)(o) !=
sigmabar_k(o)) with o not its own Xi-cycle node at k nor at k+1. FLIP-EV says Xi changes at some vertex of U_k + U_(k+1) at that transition
(U = deviation targets + Xi-successors of W-cycle nodes, R143). VIOL2: violations with no ENT flip at another Odd vertex either
(CONJECTURE FLIP-EV', R145). Prints candidates, violations (VIOL) and, for the search, the least number
of changing heads over candidate flips (MINHC). Usage: flipev.py GAME.pg [START]   |   flipev.py --search SEED.pg|rand:N RNG SECONDS OUT.pg"""
import sys, os, random, time
EXP = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
for p in ("n5-second", "harness", "hard-families"): sys.path.insert(0, os.path.join(EXP, p))
import n5b
pg = n5b.pg
def analyse(g, s0=None, t0=None, cap=300):
    N = n5b.N5(g); N.mode = "spec"; tr, fb = [], []
    try: N.run(s0, t0, trace=tr, fbtrace=fb, max_iter=cap)
    except Exception: return None
    SG = n5b.SpecSI(g); X = [SG.evaluate_choice(list(s)) for s, t in tr]; Wc = {}
    def W(s, t):
        if t not in Wc: Wc[t] = n5b.SpecSI(pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)]))
        return Wc[t].evaluate(list(s))
    cand, viol, minhc, wit, viol2 = 0, 0, None, None, 0
    for k in range(len(tr) - 1):
        (s, t), (s2, t2) = tr[k], tr[k + 1]
        if t != t2 or fb[k] or s == s2: continue
        W1, W2 = W(s, t), W(s2, t)
        if [x[0] for x in W1] != [x[0] for x in W2]: continue
        (x1, b1), (x2, b2) = X[k], X[k + 1]
        C = [v for v in range(g.n) if W1[v][0] == v]
        def U(s_, b_):
            u = {b_[v] for v in range(g.n) if g.owner[v] == 1 and b_[v] != t[v]}
            for c in C: u.add(s_[c] if g.owner[c] == 0 else b_[c])
            return u
        hc = sum(1 for u in U(s, b1) | U(s2, b2) if x1[u] != x2[u])
        ent = {q for q in range(g.n) if g.owner[q] == 1 and b1[q] == t[q] and b2[q] != t[q]}
        for o in range(g.n):
            if g.owner[o] != 1 or b1[o] == b2[o] or b1[o] == t[o]: continue
            if x1[o][0] == o or x2[o][0] == o: continue
            cand += 1
            if minhc is None or hc < minhc: minhc, wit = hc, (k, o, b1[o], b2[o])
            if hc == 0: viol += 1
            if hc == 0 and not (ent - {o}): viol2 += 1
    return cand, viol, minhc, wit, len(tr) - 1, viol2
def rand_game(rng, n):
    return pg.Game([rng.randrange(2 * n) for _ in range(n)], [rng.randrange(2) for _ in range(n)],
                   [sorted(set(rng.sample(range(n), rng.randint(1, 3)))) for _ in range(n)])
def mutate(rng, g):
    pr, ow, sc = list(g.prio), list(g.owner), [list(s) for s in g.succ]; n = len(pr); v = rng.randrange(n); r = rng.random()
    if r < 0.35: sc[v] = sorted(set(sc[v] + [rng.randrange(n)]))
    elif r < 0.55 and len(sc[v]) > 1: sc[v].pop(rng.randrange(len(sc[v])))
    elif r < 0.85: pr[v] = rng.randrange(2 * n)
    else: ow[v] ^= 1
    return pg.Game(pr, ow, sc)
S2 = os.environ.get("SCORE2") == "1"          # search target FLIP-EV' (VIOL2) instead of FLIP-EV (VIOL)
def score(r):
    if r is None or r[0] == 0: return (-99, 0)
    return (r[5], r[1], -r[2]) if S2 else (r[1], -r[2])
if __name__ == "__main__" and sys.argv[1] == "--search":
    rng = random.Random(int(sys.argv[3])); end = time.time() + float(sys.argv[4]); out = sys.argv[5]
    g = rand_game(rng, int(sys.argv[2][5:])) if sys.argv[2].startswith("rand:") else pg.read(sys.argv[2])
    f = score(analyse(g)); best = (f, g); it = 0
    while time.time() < end and best[0][0] < 1:
        it += 1; h = mutate(rng, g)
        if rng.random() < 0.5: h = mutate(rng, h)
        fh = score(analyse(h))
        if fh >= f: g, f = h, fh
        if fh > best[0]: best = (fh, h); print("improve", it, fh, flush=True)
    f, g = best
    pg.write(g, out); print(f"FLIPEV-SEARCH {sys.argv[2]} rng {sys.argv[3]} best (VIOL, -MINHC) {f} tries {it} -> {out}")
elif __name__ == "__main__":
    g = pg.read(sys.argv[1]); st = n5b.read_start(sys.argv[2], g) if len(sys.argv) > 2 else (None, None)
    r = analyse(g, *st, cap=5000)
    if r is None: print(f"FLIPEV {os.path.basename(sys.argv[1])} RUN-ERROR"); sys.exit(0)
    print(f"FLIPEV {os.path.basename(sys.argv[1])} n {g.n} iterations {r[4]} candidates {r[0]} VIOL {r[1]} MINHC {r[2]} witness (k, o, old, new) {r[3]} VIOL2 {r[5]}")
