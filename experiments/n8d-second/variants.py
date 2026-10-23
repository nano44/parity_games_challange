"""Game transforms for the start-strategy / tie-break box (Lead 08:34Z, box 2b). Reads a PGSolver game, writes the transformed game.
  variants.py MODE IN.pg OUT.pg         or   variants.py MODE -- CMD ...   (game from CMD's stdout, result to stdout)
MODE: id       unchanged
      revedges every successor list reversed in file order (with tau_1 = first successor this is tau_1 = LAST successor of the
               original file; arc ties are by successor id in kl2/kl2fast, so they do not change)
      relabel  node ids reversed (v -> n-1-v), successor lists keep their file order: tau_1 = first successor is the same arc,
               but every 'smallest id' tie-break (§0 arc ties, R1 node choice) now picks the original LARGEST id."""
import os
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg  # noqa: E402


def transform(g, mode):
    n = g.n
    if mode == "id":
        return g
    if mode == "revedges":
        return pg.Game(g.prio, g.owner, [list(reversed(s)) for s in g.succ])
    if mode == "relabel":
        m = lambda v: n - 1 - v
        prio, owner, succ = [0] * n, [0] * n, [None] * n
        for v in range(n):
            prio[m(v)], owner[m(v)], succ[m(v)] = g.prio[v], g.owner[v], [m(w) for w in g.succ[v]]
        return pg.Game(prio, owner, succ)
    raise SystemExit(f"unknown mode {mode}")


if __name__ == "__main__":
    mode = sys.argv[1]
    if sys.argv[2] == "--":
        g = pg.parse(subprocess.run(sys.argv[3:], capture_output=True, text=True, check=True).stdout)
        sys.stdout.write(pg.dumps(transform(g, mode)))
    else:
        pg.write(transform(pg.read(sys.argv[2]), mode), sys.argv[3])
