"""L-RED box 25 (produced on Opus 5.5): for each game, N5's iterations, Odd-moving iterations, the last iteration at which Odd moves,
and Even moves after it (n5tr.trace, which asserts equality with n5.run). Usage: oddmoves.py G.pg ..."""
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import n5tr  # noqa: E402
import pg  # noqa: E402
for path in sys.argv[1:]:
    g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
    buf = io.StringIO()
    it, fb, st = n5tr.trace(g, None, None, 10 ** 9, buf)
    lines = [l for l in buf.getvalue().splitlines() if "| O:" in l]
    last = max([i + 1 for i, l in enumerate(lines) if not l.rstrip().endswith("O: -")], default=0)
    print(f"{os.path.basename(path)} n {g.n}: iterations {it} fallback {fb}; Odd moves in {st['odd_moves']} iterations, last at {last}; "
          f"Even-moving iterations after it {sum(1 for l in lines[last:] if '| E: -' not in l)}")
