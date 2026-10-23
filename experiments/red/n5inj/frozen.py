"""L-RED box 26 (produced on Opus 5.5): N5 (experiments/new/n5.py run(), read-only) started from (sigma, tau*) with tau* an OPTIMAL
Odd strategy (Odd's final strategy of an N5 run from best-reward, which has It = empty), sigma uniformly random. Then Odd never moves
(It depends on tau alone) and the run is Even's 'best reply to tau* among improving edges' chain (R58 §4).
Reports the max iterations over the random starts, per game.  Usage: frozen.py G.pg STARTS SEED | frozen.py random COUNT NMIN NMAX SEED STARTS"""
import os, random, sys
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
for d in ("new", "si", "harness"):
    sys.path.insert(0, os.path.join(R, "experiments", d))
import n5  # noqa: E402
import pg  # noqa: E402
from si import Engine  # noqa: E402


def odd_optimal(g):
    """An Odd strategy tau with I_tau = empty: classical switch-all SI on the dual (si.py Engine, best-reward start)."""
    Ed = Engine(n5.dual(g)); t = list(Ed.initial("best"))
    while True:
        val, _ = Ed.evaluate(tuple(t)); I = Ed.improving(tuple(t), val)
        if not I: return t
        for v in {v for v, _ in I}:
            t[v] = max((w for x, w in I if x == v), key=lambda w: (Ed.key(val[w]), w))


def trial(g, starts, rng):
    tau = odd_optimal(g); E = Engine(g); worst = 0
    for _ in range(starts):
        sig = {v: rng.choice(E.succ[v]) for v in range(g.n) if g.owner[v] == 0}
        tt = {v: tau[v] for v in range(g.n) if g.owner[v] == 1}
        it, fb, *_ = n5.run(g, "n5", (sig, tt))
        worst = max(worst, it)
    return worst


if __name__ == "__main__":
    if sys.argv[1] == "random":
        cnt, nmin, nmax, seed, starts = map(int, sys.argv[2:7]); rng = random.Random(seed); hist = {}
        best = (0, None)
        for i in range(cnt):
            n = rng.randint(nmin, nmax)
            prio = [rng.randint(0, n) for _ in range(n)]; owner = [rng.randint(0, 1) for _ in range(n)]
            succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) for _ in range(n)]
            g = pg.Game(prio, owner, succ); w = trial(g, starts, rng)
            hist[w] = hist.get(w, 0) + 1
            if w > best[0]: best = (w, (prio, owner, succ))
        print("max iterations from (random sigma, optimal tau*): histogram", dict(sorted(hist.items())), "best", best[0])
    else:
        g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
        print(os.path.basename(sys.argv[1]), "n", g.n, "max iterations from (random sigma, tau*):", trial(g, int(sys.argv[2]), random.Random(int(sys.argv[3]))))
