"""L-RED box 30 (produced on Opus 5.5): hill climb against L-SI's CONJECTURE (CYC-ELIM) (every non-eliminating window of a joint
lambda-phase contains <= c theta-changes): C^1O games (o = 0), canonical N5 runs, measure = L-SI's
experiments/si/orlens/thetaelim.run_g UNMODIFIED (max theta-changes inside one non-eliminating window). Mutations: thetaclimb.py's.
Fitness: (max theta-changes in a non-eliminating window, theta-changes in that phase, -edges).
Usage: cycelimclimb.py n SECONDS SEED OUT [--from G.pg]"""
import os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
args = sys.argv[1:]; SECS = float(args[1])
sys.argv = [sys.argv[0], args[0], "0", args[2], args[3]] + args[4:]      # thetaclimb runs its own loop at import: 0 s
sys.path.insert(0, HERE)
import thetaclimb as TC  # noqa: E402
sys.path.insert(0, os.path.join(R0, "experiments", "si", "orlens"))
import thetaelim as TE  # noqa: E402
import pg  # noqa: E402


def score(G):
    g = pg.Game(*[list(x) for x in G])
    try:
        _, _, b = TE.run_g(g, None, cap=20000)
    except Exception:
        return (-1, 0, 0)
    return (b[0], b[1], -sum(len(x) for x in g.succ))


best = TC.load(sys.argv[sys.argv.index("--from") + 1]) if "--from" in sys.argv else TC.rand_game()
bs = score(best); t0 = time.time(); steps = 0; print("start", bs, flush=True)
while time.time() - t0 < SECS:
    steps += 1; c = TC.mutate(best); cs = score(c)
    if cs >= bs:
        if cs[:2] > bs[:2]: print(f"step {steps} t {time.time() - t0:.0f}s: theta-changes in a non-elim window {cs[0]} (phase theta-changes {cs[1]})", flush=True); TC.write(c)
        best, bs = c, cs
TC.write(best); print("FINAL", bs, steps, flush=True)
