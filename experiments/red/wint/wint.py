#!/usr/bin/env python3
"""L-RED R141: longest W-CONSTANT interval of an N5 run (n5b SPEC): maximal stretch of transitions with tau fixed, no fallback, sigma
changing and W = val(sigma, tau) unchanged at EVERY vertex (L-SI box 51b [P-INT]; CONJECTURE INT-LIN: |I| <= n - 1).
fit(game, start) -> (longest interval, iterations); also a hill-climbing search over random games.
Usage: wint.py GAME.pg [START]   |   wint.py --search SEED N SECONDS OUT.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, "..", ".."))
for p in ("n5-second", "harness"): sys.path.insert(0, os.path.join(EXP, p))
import n5b
def fit(g, s0=None, t0=None):
    N = n5b.N5(g); N.mode = "spec"; tr, fb = [], []
    try: N.run(s0, t0, trace=tr, fbtrace=fb, max_iter=5000)
    except Exception: return (0, 0)
    best = cur = 0; Wc = {}
    def W(s, t):
        if t not in Wc:
            h = n5b.pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)])
            Wc[t] = n5b.SpecSI(h)
        return Wc[t].evaluate(list(s))
    prev = None
    for i in range(len(tr) - 1):
        (s, t), (s2, t2) = tr[i], tr[i + 1]
        if t == t2 and not fb[i] and s != s2 and W(s, t) == W(s2, t): cur += 1; best = max(best, cur)
        else: cur = 0
    return (best, len(tr) - 1)
def rand_game(rng, n):
    return n5b.pg.Game([rng.randrange(2 * n) for _ in range(n)], [rng.randrange(2) for _ in range(n)],
                       [sorted(set(rng.sample(range(n), rng.randint(1, 3)))) for _ in range(n)])
def mutate(rng, g):
    pr, ow, sc = list(g.prio), list(g.owner), [list(s) for s in g.succ]; n = len(pr); v = rng.randrange(n); r = rng.random()
    if r < 0.5: sc[v] = sorted(set(rng.sample(range(n), rng.randint(1, 3))))
    elif r < 0.75: pr[v] = rng.randrange(2 * n)
    else: ow[v] ^= 1
    return n5b.pg.Game(pr, ow, sc)
if __name__ == "__main__" and sys.argv[1] == "--search":
    seed, n, secs, out = int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]; rng = random.Random(seed)
    g = rand_game(rng, n); f = fit(g); t_end = time.time() + secs; best = (f, g)
    while time.time() < t_end:
        h = mutate(rng, g) if rng.random() < 0.97 else rand_game(rng, n); fh = fit(h)
        if fh >= f: g, f = h, fh
        if f > best[0]: best = (f, g)
    f, g = best
    with open(out, "w") as fo:
        fo.write(f"parity {g.n - 1};\n" + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n)))
    print(f"WINT-SEARCH seed {seed} n {n} best interval {f[0]} (iterations {f[1]}) -> {out}")
elif __name__ == "__main__":
    g = n5b.pg.read(sys.argv[1]); st = n5b.read_start(sys.argv[2], g) if len(sys.argv) > 2 else (None, None)
    print(f"WINT {os.path.basename(sys.argv[1])} n {g.n} longest-W-constant-interval {fit(g, *st)[0]} iterations {fit(g, *st)[1]}")
