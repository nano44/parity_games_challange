#!/usr/bin/env python3
"""L-SI box 109: gauntlet step 2 (first half) for the rules of n6.py: agreement with harness Zielonka on random games of varied
sizes, positional strategies checked by harness verify.check (D2 change 5).
Usage: rand109.py SEED COUNT NMAX MODE..   games: harness gen.random_game(n, P, 1, D, seed) with n uniform in [2, NMAX], P uniform
in [1, n + 1] priorities, out-degree 1..D, D uniform in [2, min(n, 6)].
Counters (must-0): wrong (unit: games with a vertex whose winner differs from Zielonka), badstrat (unit: games on which verify.check
complains about the positional strategies), capped (unit: games not finished within 10^5 iterations). Also max and total iterations.
CTRL=1: the winner of vertex 0 is flipped before the comparison (wrong must fire on every game)."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.environ.get("ROOT109") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE] + [os.path.join(ROOT, p) for p in ("experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import pg, gen, zielonka, verify, n6
CTRL = os.environ.get("CTRL", "0")
seed, cnt, nmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); modes = sys.argv[4:]
rng = random.Random(seed); games = []
for i in range(cnt):
    n = rng.randint(2, nmax); games.append(gen.random_game(n, rng.randint(1, n + 1), 1, rng.randint(2, max(2, min(n, 6))), rng.randrange(10 ** 9)))
ref = [list(zielonka.solve(g)) for g in games]
for mode in modes:
    wrong = bad = capped = mx = tot = 0; arg = None
    for g, z in zip(games, ref):
        r = n6.run(g, mode, cap=10 ** 5); capped += r["capped"]; tot += r["its"]
        if r["its"] > mx: mx, arg = r["its"], g.n
        win = list(r["win"])
        if CTRL == "1": win[0] = 1 - win[0]
        wrong += int(win != z)
        st = [r["strat"][v] if r["win"][v] == g.owner[v] else None for v in range(g.n)]
        bad += int(len(verify.check(g, r["win"], st)) > 0)
    print(f"R109 mode {mode} seed {seed} games {cnt} n<={nmax}{' CTRL 1' if CTRL == '1' else ''}: wrong {wrong} badstrat {bad} capped {capped} | max iterations {mx} (at n = {arg}) total iterations {tot}", flush=True)
