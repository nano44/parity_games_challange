#!/usr/bin/env python3
"""L-NEW box 163 (DATA): per-bit totals under UNLIMITED flips. For a genome G (ISO R197 ladder) and a start u:
W_c(u) := max over bit schedules (any number of flips) of the number of MOVING frames that use bit c; T_inf(u) := max number of moving
frames. Exact by memoised search (the forced dynamics is acyclic by MONO-FLIP). Reports max over U-starts (level 0 at (0, 0)) of W_0, W_1,
T_inf and V_0. Usage: perbit.py genome.json ... | perbit.py --climb m seed iters (maximise max(W_0, W_1))"""
import os, sys, json, random
sys.setrecursionlimit(100000)
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box162", "flipcheck.py")
ns = {"__file__": P, "__name__": "lib"}; exec(open(P).read(), ns); Gen, cstep, allstates, Vk = ns["Gen"], ns["cstep"], ns["allstates"], ns["Vk"]
def stats(G):
    g = Gen(G); memo = {}
    def W(u):
        if u in memo: return memo[u]
        r = [0, 0, 0]
        for c in (0, 1):
            u2 = cstep(g, u, c)
            if u2[2:] == u[2:]: continue
            w = W(u2); r[c] = max(r[c], 1 + w[c]); r[1 - c] = max(r[1 - c], w[1 - c]); r[2] = max(r[2], 1 + w[2])
        memo[u] = tuple(r); return memo[u]
    out = [0, 0, 0, 0]
    for s in allstates(g.N):
        if s[:2] != (0, 0): continue
        w = W(s); out = [max(out[0], w[0]), max(out[1], w[1]), max(out[2], w[2]), max(out[3], Vk(g, s, 0))]
    return out
if sys.argv[1] == "--climb":
    m, seed, iters = map(int, sys.argv[2:5]); rng = random.Random(seed)
    src = open(os.path.join(H, "sumclimb.py")).read(); mut = {"__file__": os.path.join(H, "sumclimb.py")}
    exec(src.split("m, seed, iters")[0].replace('OBJ = os.environ.get("OBJ", "SUM")', 'OBJ = "SUM"'), mut)
    G = json.load(open(os.environ["START"])) if os.environ.get("START") else ns["rand_lr"](m + 1, rng, True); st = stats(G); sc = max(st[:2])
    for it in range(iters):
        G2 = mut["mutate"](G, rng); s2 = stats(G2)
        if max(s2[:2]) >= sc: G, st, sc = G2, s2, max(s2[:2])
    json.dump(G, open(os.path.join(H, "out", f"perbit_m{m}_s{seed}.json"), "w"))
    print(f"PERBIT-CLIMB m {m} seed {seed} W_0 W_1 T_inf V_0 = {st}", flush=True)
else:
    for f in sys.argv[1:]: print(f"{os.path.basename(f)} W_0 W_1 T_inf V_0 = {stats(json.load(open(f)))}")
