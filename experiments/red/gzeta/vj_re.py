"""L-RED box 23 (produced on Opus 5.5): FAITHFULNESS check of gzeta.py (Lead 08:39Z). Classic strategy improvement for player 0 (Even =
Friedmann's improver) with Voege-Jurdzinski valuations (L-SI's experiments/si/si.py Engine, imported read-only) under RANDOM-EDGE
(si.py rule_random_edge: a uniform improving edge), from the all-0 start (first successor of every player-0 node, gzeta.py convention =
our reading of Lemma 4.74). Reports iterations, switches back to a 0-edge (cycle openings) and regions vs Oink zlk.
Usage: vj_re.py G.pg SEED"""
import sys, os, re, random, subprocess, tempfile
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, os.path.join(R, "experiments", "si")); sys.path.insert(0, os.path.join(R, "experiments", "harness")); sys.setrecursionlimit(100000)
import pg, si
txt = open(sys.argv[1]).read(); g = pg.parse(re.sub(r' "[^"]*"', "", txt)); rng = random.Random(int(sys.argv[2]))
E = si.Engine(g); strat = tuple(g.succ[v][0] if g.owner[v] == 0 else -1 for v in range(g.n))
it = opens = 0
while True:
    val = E.evaluate(strat)[0]
    imp = E.improving(strat, val)
    if not imp: break
    it += 1; new = E.rule_random_edge(strat, val, imp, rng); v = next(u for u in range(g.n) if new[u] != strat[u])
    if new[v] == g.succ[v][0]: opens += 1
    strat = new
win = E.regions(strat)[0]
with tempfile.NamedTemporaryFile("r", suffix=".sol") as f:
    subprocess.run([os.path.join(R, "tools", "oink", "build", "oink"), "--zlk", re.sub(r"$", "", sys.argv[1]), f.name], capture_output=True)
    ref = pg.read_sol(open(f.name).read(), g.n)
print(f"{os.path.basename(sys.argv[1])} seed {sys.argv[2]}: VJ Random-Edge iterations {it}, back-switches to a 0-edge {opens}, regions == oink zlk {list(win) == list(ref)}")
