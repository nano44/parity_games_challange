"""L-RED box 30 (produced on Opus 5.5): hill climb against L-NEW box 26's lemmas on C^1O (docs/new/N5-reentry-box26.md §3):
Lemma RM (no route decrease at (h) states inside a phase) and Lemma RE / gap G26-1 (no re-entry of class OTHER).
Uses L-NEW's experiments/new/box25/routemono.run and reentry.run UNMODIFIED (canonical start). Games: C^1O with o = 0, mutated as
thetaclimb.py. Fitness: (RM violations at (h) states [DEC_arena_h + DEC_fb_h], OTHER re-entries, THETA + ROUTE re-entries,
-edges). Saves any game with a violation. Usage: lemmaclimb.py n SECONDS SEED OUT [--from G.pg]"""
import os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
args = sys.argv[1:]
SECS = float(args[1])
sys.argv = [sys.argv[0], args[0], "0", args[2], args[3]] + args[4:]      # thetaclimb runs its own loop at import: 0 s
sys.path.insert(0, HERE)
import thetaclimb as TC  # noqa: E402  (reads n SECONDS SEED OUT [--from] from argv; we reuse its mutate/fix/load/write)
sys.path.insert(0, os.path.join(R0, "experiments", "new", "box25")); sys.path.insert(0, os.path.join(R0, "experiments", "new", "box21"))
import routemono, reentry  # noqa: E402
import pg, time  # noqa: E402


def score(G):
    g = pg.Game(*[list(x) for x in G]); c1, c2 = Counter(), Counter()
    try:
        routemono.run(g, None, c1); reentry.run(g, None, c2)
    except Exception:
        return (-1, 0, 0, 0)
    return (c1["DEC_arena_h"] + c1["DEC_fb_h"], c2["OTHER"], c2["THETA"] + c2["ROUTE"], -sum(len(x) for x in g.succ))


best = TC.load(sys.argv[sys.argv.index("--from") + 1]) if "--from" in sys.argv else TC.rand_game()
bs = score(best); t0 = time.time(); steps = 0; print("start", bs, flush=True)
while time.time() - t0 < SECS:
    steps += 1; c = TC.mutate(best); cs = score(c)
    if cs >= bs:
        if cs[:3] > bs[:3]: print(f"step {steps} t {time.time() - t0:.0f}s fitness {cs}", flush=True); TC.write(c)
        best, bs = c, cs
        if bs[0] or bs[1]: print("VIOLATION", bs, flush=True); TC.write(best); break
TC.write(best); print("FINAL", bs, steps, flush=True)
