#!/usr/bin/env python3
"""L-RED R197 TOPEXT: freeze a width-2 ladder genome and add ONE new top level (two movers, degree D) placed pi-FIRST (so the old part's run
is unchanged as long as nothing old points to the new movers: new movers are no Xi-target), with W-targets the old top level, free
Xi-targets (old movers or exit), new gates / beta ranks inserted anywhere in the old orders (order-preserving renumbering), climb the
new part only. Score (L, sum F). Usage: topext.py genome.json D iters seed out.json"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal, anal
G0 = json.load(open(sys.argv[1])); D, it, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); out = sys.argv[5]; rng = random.Random(seed)
N0 = G0["N"]; d0 = max(G0["lev"]) + 1; M0 = sum(len(o) for o in G0["opts"])
def build(P):
    """P = dict(xt=[[..]*D]*2, gpos=[floats]*2D, bpos=[floats]*2D, bp=[..], start=[..])"""
    G = json.loads(json.dumps(G0)); G["N"] = N0 + 2; G["lev"] = G0["lev"] + [d0, d0]; deg0 = len(G0["opts"][0])
    old_g = [(G0["gate"][v][k], 0, v, k) for v in range(N0) for k in range(len(G0["opts"][v]))]
    new_g = [(P["gpos"][2 * 0 + i], 1, N0 + i // D, i % D) for i in range(2 * D)]
    gates = {}
    for r, (_, _, v, k) in enumerate(sorted(old_g + new_g)): gates[(v, k)] = r
    G["gate"] = [[gates[(v, k)] for k in range(len(G0["opts"][v]) if v < N0 else D)] for v in range(N0 + 2)]
    # beta ranks: option index b; old b's keep their br order, new b's get positions
    old_b = [(G0["br"][b], 0, b) for b in range(M0)]; new_b = [(P["bpos"][i], 1, M0 + i) for i in range(2 * D)]
    br = [0] * (M0 + 2 * D)
    for r, (_, _, b) in enumerate(sorted(old_b + new_b)): br[b] = r
    G["br"] = br; G["bp"] = G0["bp"] + P["bp"]
    G["opts"] = G0["opts"] + [[[2 * (d0 - 1) + (k % 2), P["xt"][i][k], M0 + D * i + k] for k in range(D)] for i in range(2)]
    G["deg"] = max(D, G0.get("deg", 2)); G["start"] = list(G0["start"]) + P["start"]
    if "pi" in G0: G["pi"] = [p + 2 for p in G0["pi"]] + [0, 1]
    return G
def randP():
    return dict(xt=[[rng.choice(list(range(N0)) + [-1]) for k in range(D)] for i in range(2)], gpos=[rng.uniform(-1, M0 + 1) for _ in range(2 * D)],
                bpos=[rng.uniform(-1, M0 + 1) for _ in range(2 * D)], bp=[rng.randint(0, 1) for _ in range(2 * D)], start=[rng.randrange(D) for _ in range(2)])
def mut(P):
    Q = json.loads(json.dumps(P)); r = rng.random(); i = rng.randrange(2); k = rng.randrange(D)
    if r < 0.25: Q["xt"][i][k] = rng.choice(list(range(N0)) + [-1])
    elif r < 0.5: Q["gpos"][rng.randrange(2 * D)] = rng.uniform(-1, M0 + 1)
    elif r < 0.75: Q["bpos"][rng.randrange(2 * D)] = rng.uniform(-1, M0 + 1)
    elif r < 0.9: Q["bp"][rng.randrange(2 * D)] ^= 1
    else: Q["start"][i] = rng.randrange(D)
    return Q
def score(P):
    G = build(P); L, why, F, Mv, Dl, lagn, off = anal.run(G, 2); return (L, sum(F))
L0 = len(ideal.traj(G0)[0]) - 1
P = randP(); sc = score(P); best = (sc, P)
for i in range(it):
    if i % 5000 == 0 and i: P = json.loads(json.dumps(best[1])); sc = best[0]
    Q = mut(P); s2 = score(Q)
    if s2 >= sc: P, sc = Q, s2
    if sc > best[0]: best = (sc, json.loads(json.dumps(P)))
G = build(best[1]); json.dump(G, open(out, "w"))
print(f"TOPEXT {os.path.basename(sys.argv[1])} L0 {L0} -> L {best[0][0]} sumF {best[0][1]} D {D} seed {seed}", anal.run(G, 2)[2:4])
