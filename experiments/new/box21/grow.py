#!/usr/bin/env python3
"""Box 21: growth climb for the frozen-tau* phase EXCESS = (max N5 iterations in one joint λ-phase from (sigma_0, tau*)) - (n - 1).
Mutations of climb_fix.py plus 'add a vertex' (random priority/owner, 1-3 successors, 1-2 in-edges). Accept if excess >= current.
Usage: grow.py seed.pg seed secs out nmax   (GROW_FIT=bestph: canonical run, counted only if S3's tau_0 is honest-optimal)"""
import sys, os, random, time
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))  # box21 -I: find sibling modules
from n5x import *
from climb_fix import mutate, fit_tstarph, fit_bestph
FIT = fit_bestph if os.environ.get("GROW_FIT") == "bestph" else fit_tstarph
def tolist(g): return [list(g.prio), list(g.owner), [list(s) for s in g.succ]]
def addv(rng, G):
    prio, owner, succ = [list(G[0]), list(G[1]), [list(s) for s in G[2]]]; n = len(prio)
    prio.append(rng.randrange(n + 1)); owner.append(rng.randrange(2)); succ.append(sorted(set(rng.sample(range(n + 1), rng.choice((1, 2, 3))))))
    for _ in range(rng.choice((1, 2))):
        u = rng.randrange(n); succ[u] = sorted(set(succ[u]) | {n})
    return [prio, owner, succ]
def ex(G):
    try: return FIT(G) - (len(G[0]) - 1)
    except Exception: return -10 ** 9
if __name__ == "__main__":
    G = tolist(load(sys.argv[1])); rng = random.Random(int(sys.argv[2])); secs = float(sys.argv[3]); out = sys.argv[4]; nmax = int(sys.argv[5])
    f = ex(G); t0 = time.time(); it = 0; print("start", len(G[0]), f, flush=True)
    while time.time() - t0 < secs:
        H = addv(rng, G) if (rng.random() < 0.08 and len(G[0]) < nmax) else mutate(rng, G); it += 1
        fh = ex(H)
        if fh >= f:
            if fh > f or len(H[0]) != len(G[0]):
                print(f"{time.time()-t0:7.0f}s it {it} n {len(H[0])} excess {fh} phase {fh + len(H[0]) - 1}", flush=True)
                n = len(H[0])
                with open(out + ".pg", "w") as fo:
                    fo.write(f"parity {n-1};\n" + "".join(f"{v} {H[0][v]} {H[1][v]} {','.join(map(str, H[2][v]))};\n" for v in range(n)))
            G, f = H, fh
    print("FINAL", len(G[0]), f)
