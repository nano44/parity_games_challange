#!/usr/bin/env python3
"""L-RED R201 WCLIMB: keep the Xi part of a genome fixed (Xi-targets, beta ranks, parities: the improvement cube / decomposable AUSO of
L-NEW box 153) and hill-climb over the W side only: mover levels (0..D-1), per-option W-targets (a mover one level down; none at
level 0), distinct gate indices, and (FREESTART=1) the start. Score = L(G), the IDEAL run length under r187/ideal.py (the reference
simulator; RESULTS R104 semantics). Usage: wclimb.py genome.json D ITERS SEED out.json"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
G0 = json.load(open(sys.argv[1])); D, IT, SEED, out = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
R = random.Random(SEED); N = G0["N"]; FS = os.environ.get("FREESTART") == "1"
def fix(G):   # repair W-targets after level changes: each option's W-target must be a mover one level down
    for v in range(N):
        l = G["lev"][v]; low = [u for u in range(N) if G["lev"][u] == l - 1]
        for k in range(2):
            if l == 0: G["opts"][v][k][0] = -1
            elif not low: G["lev"][v] = 0; G["opts"][v][0][0] = G["opts"][v][1][0] = -1; break
            elif G["opts"][v][k][0] not in low: G["opts"][v][k][0] = R.choice(low)
    return G
def score(G):
    S, why = ideal.traj(G, cap=5000); return len(S) - 1
def rand():
    G = json.loads(json.dumps(G0)); G["lev"] = [R.randrange(D) for _ in range(N)]
    g = R.sample(range(2 * N), 2 * N); G["gate"] = [[g[2 * v], g[2 * v + 1]] for v in range(N)]
    for v in range(N):
        for k in range(2): G["opts"][v][k][0] = -2
    return fix(G)
best = None
for rs in range(int(os.environ.get("RESTARTS", "5"))):
    G = rand(); sc = score(G)
    for it in range(IT):
        H2 = json.loads(json.dumps(G)); r = R.random()
        if r < 0.3: v = R.randrange(N); H2["lev"][v] = R.randrange(D)
        elif r < 0.6: v = R.randrange(N); k = R.randrange(2); H2["opts"][v][k][0] = -2
        elif r < 0.9:
            a, b = R.sample(range(2 * N), 2); ga = H2["gate"][a // 2][a % 2]; H2["gate"][a // 2][a % 2] = H2["gate"][b // 2][b % 2]; H2["gate"][b // 2][b % 2] = ga
        elif FS: H2["start"][R.randrange(N)] ^= 1
        H2 = fix(H2); s2 = score(H2)
        if s2 >= sc: G, sc = H2, s2
    print(f"restart {rs}: L {sc} levels {sorted(G['lev'])}", flush=True)
    if best is None or sc > best[0]: best = (sc, G)
json.dump(best[1], open(out, "w"))
print(f"WCLIMB {sys.argv[1]} N {N} D {D} best L {best[0]} (2n = {2 * N}) -> {out}", flush=True)
