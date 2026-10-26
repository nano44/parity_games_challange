#!/usr/bin/env python3
"""Box 46 climber (DATA) against CONJECTURE IMM (imm.py): maximise (IMM failures, in-phase S4a steps from a W-honest state h into a
non-honest h+1) from the S3 start, by box43 climb.mutate. Usage: immclimb.py K NMAX STEPS SEED OUTDIR [--seed FILE.pg] [--prime: maximise IMM' failures first]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, os.path.join(HERE, "..", "box21")); sys.path.insert(0, HERE)
import climb, imm
from multi import rand_ckO, odd_choices
from n5x import load
climb.DEG2 = False
PRIME = "--prime" in sys.argv
def score(g):
    imm.C.clear(); del imm.FIRST[:]; del imm.MID[:]
    E = imm.Engine(g); Ed = imm.Engine(imm.dual(g)); s, t = imm.start_pair(g, E, Ed, None); pre = 0; k = 0
    try:
        imm.check(g, None, 200000, "climb", cap=600)
        while k < 600:
            vs, sb = E.evaluate(tuple(s)); r = imm.step(g, E, Ed, s, t)
            if r is None: break
            w = imm.hon.wvals(g, s, t)
            if tuple(vs) == tuple(w) and not r[4] and tuple(r[1]) == tuple(t):
                vs2, _ = E.evaluate(tuple(r[0])); w2 = imm.hon.wvals(g, r[0], r[1])
                if tuple(vs2) != tuple(w2): pre += 1
            s, t = r[0], r[1]; k += 1
    except RecursionError: return None
    return ((imm.C.get("IMMP_V", 0),) if PRIME else ()) + (sum(v for k, v in imm.C.items() if k.startswith("IMM_V")), pre)
if __name__ == "__main__":
    K, NMAX, STEPS, SEED = map(int, sys.argv[1:5]); OUT = sys.argv[5]; os.makedirs(OUT, exist_ok=True); rng = random.Random(SEED)
    g = load(sys.argv[sys.argv.index("--seed") + 1]) if "--seed" in sys.argv else None
    while g is None: g = rand_ckO(rng, K + 2, max(K + 3, NMAX // 2), K)
    NMAX = max(NMAX, g.n); O = odd_choices(g); best = score(g) or ((0, 0, 0) if PRIME else (0, 0)); print("start", best, "n", g.n, flush=True)
    for t in range(STEPS):
        r = climb.mutate(rng, g, O, NMAX, None)
        if r is None: continue
        h, O2, _ = r; sc = score(h)
        if sc is None: continue
        if sc >= best:
            if sc > best:
                print(t, sc, "n", h.n, flush=True)
                climb.save(os.path.join(OUT, f"best_imm{'p' if PRIME else ''}_k{K}_n{NMAX}_s{SEED}.pg"), h, None, {"IMM": sc[0], "PRE": sc[1]})
                if sc[0] > 0: print("IMM' FAILURE FOUND" if PRIME else "IMM FAILURE FOUND", flush=True)
            g, O, best = h, O2, sc
    print("done", best, flush=True)
