#!/usr/bin/env python3
"""L-SI box 27: kill search for CONJECTURE WSINK-READY (lay/wsink.py). Score = 100 * (WSINK-READY, W-SINK, SINK-OFF and SEG-LAST failures)
+ 3 * (steps with no vertex that is both a W-sink and an H-sink) + (unready W-sinks). Third component = failures (> 0 is a kill).
OBJ=T adds 5 * (steps with an unready W-sink). OBJ=H (after W-GROW died, lay/instances/wgrow_kill_n90):
kill = H-GROW failure (third component) or SINK-SWITCH / SEG-LAST / sink-lemma failure (x 1000); W-GROW failures only shape the score.
OBJ=S (after H-GROW died, lay/instances/hgrow_kill_n89): kill = SINK-GROW / SEG-LAST / sink-lemma failure; shaping 10 * (W-GROW and
H-GROW failures) + sum over steps of 100 // (1 + ready W-sinks + H-sinks switching to target). Mutations as lwp/xclimb.py. Usage: wclimb.py SEED.pg SEED.start|- STEPS RNGSEED NMAX OUTPREFIX"""
import sys, os, random
os.environ["PMODE"] = "1"
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(HERE, "..", "lwp")); sys.path.insert(0, HERE)
for p in (os.path.join(HERE, "..", "root"), os.path.join(ROOT, "experiments", "new", "box43"), os.path.join(HERE, "..", "runlin")): sys.path.insert(0, p)
from common import rows, load, readstart
import climb
climb.DEG2 = False
from multi import odd_choices
from growclimb import clone, save, mkst
from seglast import slscore
from wsink import wsscore
OBJ = os.environ.get("OBJ", "")

def sc(g, st):
    try: E, R = rows(g, st, cap=1500)
    except (RecursionError, RuntimeError): return None
    if len(R) > 1500: return None
    d = wsscore(g, R); f2, _ = slscore(g, R); f = d["LEM"] + d["SS"] + f2
    if OBJ == "H":                        # box 27 after W-GROW died: kill = H-GROW, SINK-SWITCH, sink-lemma or SEG-LAST failure
        return (1000 * f + 100 * d["HG"] + 20 * d["WSR"] + 5 * d["S"] + 3 * d["K"] + d["U"], d["WSR"], 1000 * f + d["HG"])
    if OBJ == "S":                        # after W-GROW and H-GROW died: kill = SINK-GROW / SEG-LAST / sink-lemma failure
        return (1000 * f + 10 * (d["HG"] + d["WSR"]) + d["SUP"] + d["U"], d["HG"] + d["WSR"], f)
    f += d["WSR"]
    if OBJ == "T": return (100 * f + 5 * d["S"] + 3 * d["K"] + d["U"], d["S"], f)   # OBJ=T: also steps with an unready W-sink
    return (100 * f + 3 * d["K"] + d["U"], d["K"], f)

def main():
    gp, sp, steps, seed, nmax, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    rng = random.Random(seed); g = load(gp); O = sorted(odd_choices(g)); st = None
    if sp != "-":
        s, t = readstart(sp); st = [s.get(v, t.get(v)) for v in range(g.n)]
    cur = sc(g, mkst(g, st)); print("seed", cur, "n", g.n, flush=True); bestk = cur[2]
    for it in range(steps):
        res = clone(rng, g, O, nmax, st) if rng.random() < 0.25 else climb.mutate(rng, g, O, nmax, st)
        if res is None: continue
        g2, O2, st2 = res; s2 = sc(g2, mkst(g2, st2))
        if s2 is None or s2[0] < cur[0]: continue
        if s2[0] > cur[0]: print("step", it, "score", s2, "n", g2.n, flush=True); save(out, g2, st2)
        if s2[2] > bestk: bestk = s2[2]; save(out + "_k", g2, st2); print("step", it, "KILLSCORE", s2[2], "n", g2.n, flush=True)
        g, O, st, cur = g2, O2, st2, s2
    print("final", cur, "n", g.n, "best kill score", bestk)

if __name__ == "__main__":
    main()
