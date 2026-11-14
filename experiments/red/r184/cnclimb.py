#!/usr/bin/env python3
"""L-RED R184: structured climb over CN gadgets (cngad.py) for CNMAX (W-cycle-node moves in one FL run; dcyc.analyse), default S3
start. SCORE = 1000*CNMAX + 10*CNMOV + LFL. Usage: cnclimb.py k iters seed out.pg"""
import sys, os, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r183")]
import cngad, dcyc, chain
def score(G):
    try: R = dcyc.summary(dcyc.analyse(cngad.build(G), None, cap=400))
    except Exception: return -1, None
    return 1000 * R["CNMAX"] + 10 * R["CNMOV"] + R["LFL"], R
k, iters, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
T = lambda: rng.randrange(32 + k) if rng.random() < 0.5 else rng.randrange(32)
EV = lambda: 2 * rng.randrange(2, 20)
G = [[EV(), [T(), 0], [T(), 0]] for _ in range(k)]
bs, R = score(G); print("START", bs, R, flush=True)
for it in range(iters):
    Hh = [[x[0], list(x[1]), list(x[2])] for x in G]; i = rng.randrange(k); f = rng.randrange(5)
    if f == 0: Hh[i][0] = EV()
    elif f in (1, 2): Hh[i][f][0] = T()
    else: Hh[i][f - 2][1] = rng.randrange(12)
    hs, HR = score(Hh)
    if hs >= bs:
        if hs > bs: print("IT", it, HR, flush=True)
        G, bs, R = Hh, hs, HR; chain.write(cngad.build(G), out + ".tmp"); os.replace(out + ".tmp", out)
print("BEST", R, G, flush=True)
