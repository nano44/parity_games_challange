"""L-RED box 26 (produced on Opus 5.5): longest stretch of consecutive N5 iterations in which the opponent's strategy does not change
(R58 §5 (K2); declines.states replica, counts asserted = n5.run). Usage: stretch.py G.pg [START] | stretch.py random COUNT NMIN NMAX SEED"""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import declines  # noqa: E402
import n5tr  # noqa: E402
import pg  # noqa: E402


def longest(seq):
    best = [0, 0]
    for k in (0, 1):                      # k = the player whose strategy stays fixed
        cur = 0
        for t in range(len(seq) - 1):
            if seq[t][k] == seq[t + 1][k]: cur += 1; best[k] = max(best[k], cur)
            else: cur = 0
    return best                           # [longest with sigma fixed (Odd-only), longest with tau fixed (Even-only)]


if __name__ == "__main__":
    if sys.argv[1] == "random":
        cnt, nmin, nmax, seed = map(int, sys.argv[2:6]); rng = random.Random(seed); w = (0, None)
        for i in range(cnt):
            n = rng.randint(nmin, nmax)
            prio = [rng.randint(0, n) for _ in range(n)]; owner = [rng.randint(0, 1) for _ in range(n)]
            succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 4)))) for _ in range(n)]
            b = max(longest(declines.states(pg.Game(prio, owner, succ))))
            if b > w[0]: w = (b, n)
        print("random: longest one-sided stretch", w[0], "at n", w[1])
    else:
        g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
        st = n5tr.read_start(sys.argv[2]) if len(sys.argv) > 2 else None
        print(os.path.basename(sys.argv[1]), "n", g.n, "longest stretch with sigma fixed / tau fixed:", longest(declines.states(g, st)))
