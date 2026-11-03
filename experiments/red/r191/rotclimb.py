#!/usr/bin/env python3
"""L-RED R191 ROTCLIMB: hill-climb (r190/delclimb genome + mutations) for ROTATIONS: score = (max run of consecutive KEY-ALONE moves of
one mover (r191/altck.py), number of key-alone moves, L). Usage: rotclimb.py d w D iters seed out.json"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r190")]
import delclimb
sys.argv_saved = sys.argv; sys.argv = [sys.argv[0]]; import altck; sys.argv = sys.argv_saved
def score(G):
    T, a, h, mr, bad = altck.run(G); assert not bad, bad
    return (mr, a, T)
d, w, D, it, seed = map(int, sys.argv[1:6]); out = sys.argv[6]; rng = random.Random(seed)
G = delclimb.rand(d, w, D, rng); sc = score(G); best = (sc, G)
for i in range(it):
    if i % 20000 == 0 and i: G = json.loads(json.dumps(best[1])); sc = best[0]
    H2 = delclimb.mutate(G, rng); s2 = score(H2)
    if s2 >= sc: G, sc = H2, s2
    if sc > best[0]: best = (sc, json.loads(json.dumps(G))); json.dump(G, open(out, "w"))
print(f"ROTCLIMB d {d} w {w} D {D} seed {seed} maxrun {best[0][0]} key-alone {best[0][1]} L {best[0][2]}", flush=True)
