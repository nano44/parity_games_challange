#!/usr/bin/env python3
"""L-RED 61 R227: GREEDY SELF-LOOP growth. Each round: sample SAMP random new options (x, W-target w, Xi-target t, gate rank p, beta rank q, bp),
with t = x (self-loop, the GROW7 / CX4 digit pattern) with probability PSELF, else t random; keep the option with the best (A, #tops),
ties to the smaller rank change; stop when no strict gain in A or #tops. Engine own.py IDEAL-CYC Howard ([E-LEV]), cap 3000 (ascore226).
Freezes each round's genome to out/sg_<SEED>_r<round>.json; prints (round, A, #tops, T, N, M, N + M). Resumable: RESUME=file starts there.
Usage: selfgrow227.py SEED ROUNDS SAMP START.json"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r226"), os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
from compose226 import add_opt, check
from ascore226 import ascore
seed, R, SAMP, SG = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed); PS = float(os.environ.get("PSELF", "0.7"))
G = json.load(open(os.environ.get("RESUME", SG))); s = ascore(G); print("start", s, "N", G["N"], "M", len(G["br"]), flush=True)
r0 = int(os.environ.get("R0", "0"))
for rd in range(r0, R):
    N = G["N"]; M = len(G["br"]); best = None
    for _ in range(SAMP):
        x = rng.randrange(N); wt = -1 if G["lev"][x] == 0 else rng.choice([y for y in range(N) if G["lev"][y] == G["lev"][x] - 1])
        t = x if rng.random() < PS else rng.choice(list(range(N)) + [-1])
        Hh = add_opt(G, x, wt, t, rng.randint(0, M), rng.randint(0, M), rng.randrange(2))
        try: check(Hh); a = ascore(Hh)
        except Exception: continue
        if best is None or a[:2] > best[0][:2]: best = (a, Hh)
    if best is None or best[0][:2] <= s[:2]: print("round", rd, "no gain; best sampled", best and best[0], flush=True); break
    s, G = best; json.dump(G, open(f"out/sg_{seed}_r{rd}.json", "w"))
    print("round", rd, "A", s[0], "tops", s[1], "T", s[2], "N", G["N"], "M", len(G["br"]), "N+M", G["N"] + len(G["br"]), flush=True)
print("FINAL", s, flush=True)
