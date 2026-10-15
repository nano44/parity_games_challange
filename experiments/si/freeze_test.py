#!/usr/bin/env python3
"""Test of the level-freezing claim behind the MSF heuristic (notes/L-SI.md): after an MSF switch at level r at vertex v,
does any vertex's valuation change above level r (cycle node, or a path bit of rank > r)?  Counts violations on random games
and on 1-sink games; prints the smallest violating game.  Usage: freeze_test.py [--games N] [--nmax 8] [--sink]"""
import sys, os, random, argparse
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, si
ap = argparse.ArgumentParser(); ap.add_argument("--games", type=int, default=3000); ap.add_argument("--nmax", type=int, default=8)
ap.add_argument("--sink", action="store_true"); ap.add_argument("--rule", default="msf"); ap.add_argument("--seed", type=int, default=0); a = ap.parse_args()
rng = random.Random(a.seed)


def rand_game(n):
    while True:
        prio = [rng.randrange(n + 2) for _ in range(n)]; owner = [rng.randrange(2) for _ in range(n)]
        succ = [sorted(rng.sample(range(n), rng.randint(1, min(n, 3)))) for _ in range(n)]
        if a.sink:
            prio[0], owner[0], succ[0] = 1, 1, [0]
            prio = [p if i == 0 else max(2, p) for i, p in enumerate(prio)]
        g = pg.Game(prio, owner, succ)
        if a.sink:
            seen = {0}; st = [0]
            while st:
                x = st.pop()
                for y in g.pred[x]:
                    if y not in seen: seen.add(y); st.append(y)
            if len(seen) < n: continue
        return g


def above(e, val, r):
    """valuation restricted to ranks > r: (cycle node, path bits of rank > r)"""
    w, path, ln = val
    return (w, path >> (r + 1))


viol = 0; cyc = 0; cyclic_viol = 0; total = 0; smallest = None; viol_games = 0
for gi in range(a.games):
    n = rng.randint(2, a.nmax); g = rand_game(n); e = si.Engine(g)
    strat = e.initial("best"); bad = False
    while True:
        val, _ = e.evaluate(strat); imp = e.improving(strat, val)
        if not imp: break
        new = si.RULES[a.rule](e)(strat, val, imp, None)
        v = [i for i in range(n) if new[i] != strat[i]][0]
        cyclic = (val[new[v]][1] >> e.rank[v]) & 1
        lv = e._level(val[strat[v]], val[new[v]])
        total += 1
        val2, _ = e.evaluate(new)
        if lv[0] == 2:          # path-level switch at rank lv[1]: nothing above may change
            r = lv[1]
            ch = [u for u in range(n) if above(e, val[u], r) != above(e, val2[u], r)]
            if ch and any(val[u][0] != val2[u][0] for u in range(n)):
                cyc += 1; ch = []          # a cycle node changed somewhere: counted separately
            if ch and cyclic:
                cyclic_viol += 1; ch = []  # the switched edge's target path passed through v: counted separately
            if ch:
                viol += 1; bad = True
                if smallest is None or g.n < smallest[0].n:
                    smallest = (g, strat, v, new[v], r, ch, val, val2)
        strat = new
    viol_games += bad
print(f"{'sink' if a.sink else 'random'} games: {a.games}, msf switches {total}, path-level switches that changed a cycle node: {cyc}; with all cycle nodes fixed, changed a path bit above their level: cycle-creating switch {cyclic_viol}, non-cycle-creating switch {viol} (in {viol_games} games)")
if smallest:
    g, strat, v, w, r, ch, val, val2 = smallest
    print("smallest violating game:"); print(pg.dumps(g)); print("strategy", strat, "switch", v, "->", w, "level rank", r, "changed", ch)
    for u in ch: print(" ", u, val[u], "->", val2[u], "ranks", g.prio, e.rank)
