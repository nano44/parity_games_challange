#!/usr/bin/env python3
"""L-SI box 27: random-sampling kill search for CONJECTURE SINK-GROW (docs/si/N5-LAY-box27.md), structurally different from the
lay/wclimb.py climbs: independent random games (MODE=rand, lwp/rsamp.py's rgame) or library games (MODE=lib, env LIB) with random start
pairs, no climbing. Kill = SINK-GROW (SS_V), SEG-LAST or sink-lemma failure; saved. Tallies steps with no frontier vertex and W-/H-GROW
failures. Usage: ssamp.py TRIALS RNGSEED OUTPREFIX"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(HERE, "..", "lwp")); sys.path.insert(0, HERE)
for p in (os.path.join(HERE, "..", "grun"), os.path.join(HERE, "..", "root"), os.path.join(HERE, "..", "runlin")): sys.path.insert(0, p)
from common import rows, load
from growclimb import save
from rsamp import rgame
from seglast import slscore
from wsink import wsscore

def main():
    trials, seed, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    mode = os.environ.get("MODE", "rand"); nmin, nmax, dmax = (int(os.environ.get(k, d)) for k, d in (("NMIN", "4"), ("NMAX", "12"), ("DMAX", "3")))
    lib = [l.split()[0] for l in open(os.environ["LIB"]) if l.strip() and not l.startswith("#")] if mode == "lib" else []
    tot = dict(runs=0, K=0, WSR=0, HG=0, kills=0)
    for it in range(trials):
        g = load(os.path.join(ROOT, rng.choice(lib))) if lib else rgame(rng, rng.randint(nmin, nmax), dmax)
        if lib and g.n > int(os.environ.get("LIBNMAX", "80")): continue
        st = [rng.choice(g.succ[v]) for v in range(g.n)]
        sp = ({v: st[v] for v in range(g.n) if g.owner[v] == 0}, {v: st[v] for v in range(g.n) if g.owner[v] == 1})
        try: E, R = rows(g, sp, cap=1500)
        except (RecursionError, RuntimeError): continue
        d = wsscore(g, R); f2, _ = slscore(g, R); tot["runs"] += 1
        for k in ("K", "WSR", "HG"): tot[k] += d[k]
        if d["LEM"] + d["SS"] + f2 > 0:
            tot["kills"] += 1; save("%s_%d" % (out, it), g, st); print("trial", it, "KILL", d, "seglast", f2, "n", g.n, flush=True)
        if it % 2000 == 1999: print("trial", it + 1, tot, flush=True)
    print("final", tot, flush=True)

if __name__ == "__main__":
    main()
