#!/usr/bin/env python3
"""L-SI box 26 (successor 22): random-sampling kill search for CONJECTURE L-WAVE' (docs/si/N5-LWP-box26.md). Structurally different from
the box-25 climbs (grun/gclimb.py OBJ=LW PMODE=1, mutations of one seed): independent random games and random start pairs, no climbing.
MODE=rand: games with n in [NMIN, NMAX], each vertex of out-degree 1..DMAX, priorities 0..n, owners fair coin; MODE=dag: dgame below; MODE=lib (env LIB=list file):
library games with random start pairs. Score = grun/lwave.py's maxgap (max gap - (n - 1), PMODE=1); > 0 is a kill. Saves every score >= 0.
Usage: rsamp.py TRIALS RNGSEED OUTPREFIX"""
import sys, os, random
os.environ["PMODE"] = "1"
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in (os.path.join(HERE, "..", "grun"), os.path.join(HERE, "..", "root"), os.path.join(HERE, "..", "runlin")): sys.path.insert(0, p)
from common import rows, load
from lwave import maxgap
from growclimb import save
import pg

def rgame(rng, n, dmax):
    L = ["parity %d;" % (n - 1)]
    for v in range(n):
        s = sorted(set(rng.randrange(n) for _ in range(rng.randint(1, dmax))))
        L.append("%d %d %d %s;" % (v, rng.randint(0, n), rng.randint(0, 1), ",".join(map(str, s))))
    return pg.parse("\n".join(L) + "\n")

def dgame(rng, n, dmax):
    """MODE=dag: the pure-length regime. Vertices 0..n-2 in topological order, edges only to larger indices, sink g = n-1 (self-loop,
    priority n + (n % 2), the unique top, even); every other priority 0, so every play reaches g, c = g and P = {} everywhere."""
    g = n - 1; L = ["parity %d;" % (n - 1)]
    for v in range(n - 1):
        s = sorted(set(rng.randrange(v + 1, n) for _ in range(rng.randint(1, dmax))))
        L.append("%d 0 %d %s;" % (v, rng.randint(0, 1), ",".join(map(str, s))))
    L.append("%d %d 0 %d;" % (g, n + (n % 2), g))
    return pg.parse("\n".join(L) + "\n")

def main():
    trials, seed, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    mode = os.environ.get("MODE", "rand"); nmin, nmax, dmax = (int(os.environ.get(k, d)) for k, d in (("NMIN", "4"), ("NMAX", "10"), ("DMAX", "3")))
    lib = [l.split()[0] for l in open(os.environ["LIB"]) if l.strip() and not l.startswith("#")] if mode == "lib" else []
    best, saved, done = -10 ** 6, 0, 0
    for it in range(trials):
        g = load(os.path.join(ROOT, rng.choice(lib))) if lib else (dgame if mode == "dag" else rgame)(rng, rng.randint(nmin, nmax), dmax)
        if lib and g.n > int(os.environ.get("LIBNMAX", "80")): continue
        st = [rng.choice(g.succ[v]) for v in range(g.n)]
        sp = ({v: st[v] for v in range(g.n) if g.owner[v] == 0}, {v: st[v] for v in range(g.n) if g.owner[v] == 1})
        try: E, R = rows(g, sp, cap=1500)
        except (RecursionError, RuntimeError): continue
        done += 1; sc = maxgap(g, R)
        if sc >= 0:
            saved += 1; save("%s_%d_%d" % (out, it, sc), g, st); print("trial", it, "score", sc, "n", g.n, flush=True)
        if sc > best: best = sc; print("trial", it, "best", sc, "n", g.n, flush=True)
    print("final trials %d evaluated %d best %d saved %d" % (trials, done, best, saved))

if __name__ == "__main__":
    main()
