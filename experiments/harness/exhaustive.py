#!/usr/bin/env python3
"""Exhaustive tiny games (L-LIT bench rank 1). Every game with n vertices, owners in {0,1}, priorities in 0..P,
and every non-empty successor set (self-loops included).
  python API: iter_games(n, P) yields pg.Game
  CLI: exhaustive.py DIR n P [--stride K] [--offset J]   writes every K-th game (from J) as DIR/x_n{n}_P{P}_{index}.pg
Counts: n=1,P=3: 8; n=2,P=2: 324; n=3,P=2: 74088 (use --stride for file corpora; the in-process API for Python solvers)."""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pg


def iter_games(n, P):
    succsets = [list(s) for r in range(1, n + 1) for s in itertools.combinations(range(n), r)]
    for owners in itertools.product((0, 1), repeat=n):
        for prios in itertools.product(range(P + 1), repeat=n):
            for succ in itertools.product(succsets, repeat=n):
                yield pg.Game(prios, owners, succ)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    stride = int(sys.argv[sys.argv.index("--stride") + 1]) if "--stride" in sys.argv else 1
    offset = int(sys.argv[sys.argv.index("--offset") + 1]) if "--offset" in sys.argv else 0
    d, n, P = args[0], int(args[1]), int(args[2])
    os.makedirs(d, exist_ok=True)
    k = 0
    for i, g in enumerate(iter_games(n, P)):
        if i >= offset and (i - offset) % stride == 0:
            pg.write(g, os.path.join(d, f"x_n{n}_P{P}_{i:06d}.pg")); k += 1
    print(f"wrote {k} games to {d}")
