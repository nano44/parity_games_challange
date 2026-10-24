"""L-RED box 26 (produced on Opus 5.5): R58 Lemma 1's premise on random games, both players, exhaustive over strategies.
Games: Oink's rngame (tools/oink/build, pinned 8fbf0a7) with seeds via its own randomness; we write each game to a temp file.
Usage: injbatch.py COUNT NMIN NMAX SEED   (prints totals; any collision with different valuation vectors is printed in full)"""
import io, os, random, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import injcheck  # noqa: E402
import pg  # noqa: E402
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
cnt, nmin, nmax, seed = map(int, sys.argv[1:5]); rng = random.Random(seed)
tot = {"games": 0, "strategies": 0, "collisions": 0, "bad": 0}
for i in range(cnt):
    n = rng.randint(nmin, nmax)
    # random game in Python (rngame has no seed option): priorities 0..n, out-degree 1..3, self-loops allowed
    prio = [rng.randint(0, n) for _ in range(n)]; owner = [rng.randint(0, 1) for _ in range(n)]
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) for _ in range(n)]
    g = pg.Game(prio, owner, succ)
    for side in ("even", "odd"):
        c, b, ns, _ = injcheck.check(g, side, out=io.StringIO())
        tot["strategies"] += ns; tot["collisions"] += c; tot["bad"] += b
        if b:
            print("BAD", side, prio, owner, succ)
    tot["games"] += 1
print(tot)
