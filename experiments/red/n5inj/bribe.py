"""L-RED box 26 (produced on Opus 5.5): test of Conjecture BRIBE (R58 §5). At every iteration in which a player moves, compare
r = #improving edges it refuses (|I| minus switches taken) with the opponent's |I| at the same state.
Prints the pairs (r, opponent |I|) and the worst ratio r / max(1, opponent |I|). Usage: bribe.py G.pg [STARTFILE]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import declines  # noqa: E402
import n5tr  # noqa: E402
import pg  # noqa: E402
path = sys.argv[1]; g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
st = n5tr.read_start(sys.argv[2]) if len(sys.argv) > 2 else None
seq = declines.states(g, st); pairs = []
for t in range(len(seq) - 1):
    for k, I, J in ((0, 2, 3), (1, 3, 2)):
        s, s2 = seq[t][k], seq[t + 1][k]
        if s == s2: continue
        taken = sum(1 for v in range(g.n) if s[v] != s2[v])
        r = len(seq[t][I]) - taken
        pairs.append((r, len(seq[t][J]), "EO"[k], t + 1))
worst = max(pairs, key=lambda p: p[0] / max(1, p[1]))
print(f"{os.path.basename(path)}: moves {len(pairs)}; refused>0 at {sum(1 for p in pairs if p[0] > 0)}; refused>opp|I| at "
      f"{sum(1 for p in pairs if p[0] > p[1])}; worst (refused, opp |I|, mover, iteration) {worst}")
