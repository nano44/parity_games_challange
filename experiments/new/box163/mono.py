#!/usr/bin/env python3
"""L-NEW box 163 probe (DATA): along forced runs (box 162 c-steps, ISO 𝓛^R genomes, random bit schedules) does every mover's CURRENT
Xi-value (box 150 integer encoding) never fall (MONO across flips), and does every moving frame raise some current value strictly?"""
import os, sys, random
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box162", "flipcheck.py")
ns = {"__file__": P, "__name__": "lib"}; exec(open(P).read(), ns)
rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 163); fall = nostrict = frames = 0
for i in range(int(sys.argv[2]) if len(sys.argv) > 2 else 2000):
    d = 2 + i % 4; G = ns["rand_lr"](d, rng, True); g = ns["Gen"](G); N = G["N"]
    u = tuple(rng.randint(0, 1) for _ in range(N))
    for t in range(60):
        c = rng.randint(0, 1); v0 = [g.face(u, x, u[x]) for x in range(2, N)]
        u2 = ns["cstep"](g, u, c)
        if u2 == u: continue
        frames += 1; v1 = [g.face(u2, x, u2[x]) for x in range(2, N)]
        if any(b < a for a, b in zip(v0, v1)): fall += 1
        if not any(b > a for a, b in zip(v0, v1)): nostrict += 1
        u = u2
print(f"MONO-FLIP frames {frames} fall {fall} nostrict {nostrict}")
