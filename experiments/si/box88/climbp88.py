#!/usr/bin/env python3
"""L-SI box 88: hill-climb over the MIRROR family's lane lengths (box84/pair84.py, MUP = 1) at fixed h. Score (lex) = (maxk, maxev,
maxdepth) of leap88.census on the real bits (default mode, as leap87). Seeds: the frozen HP_mup lane lengths extended by doubling.
Usage: climbp88.py BOX81DIR h SEED ITERS OUTDIR"""
import sys, os, json, random, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "box84")]
import leap88, pair84
B81, h, seed, IT, OUT = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
leap88.setup(B81); rng = random.Random(seed); os.makedirs(OUT, exist_ok=True)
base = {5: ([2, 4, 12, 17, 22], [5, 17, 20, 34])}
def seed_cfg():
    L, LM = base[5]; L = list(L); LM = list(LM)
    while len(L) < h: L.append(L[-1] + rng.randint(5, 15)); LM.append(LM[-1] + rng.randint(5, 20))
    return {"L": L[:h], "LM": LM[:h - 1]}
def mutate(c):
    c = json.loads(json.dumps(c)); k = rng.choice(["L", "LM"]); i = rng.randrange(len(c[k]))
    c[k][i] = max(1, c[k][i] + rng.choice([-5, -3, -2, -1, 1, 2, 3, 5])); return c
def score(c):
    G, nm = pair84.build(h, c["L"], c["LM"], 1)
    try: U, T = leap88.census(G, nm)
    except Exception: return (-1, 0, 0), None, None
    s = leap88.summary(U); s["T"] = T; return (s["maxk"], s["maxev"], s["maxdepth"]), s, (G, nm)
c = seed_cfg(); best, m, gn = score(c); print("seed", c, best, m, flush=True)
for it in range(IT):
    d = mutate(c); sc, mm, gg = score(d)
    if sc >= best:
        if sc > best:
            print(it, d, sc, mm, flush=True); json.dump(gg[0], open(os.path.join(OUT, f"HP{h}_best_{seed}.json"), "w"))
            json.dump(gg[1], open(os.path.join(OUT, f"HP{h}_best_{seed}.names.json"), "w")); json.dump(d, open(os.path.join(OUT, f"HP{h}_best_{seed}.cfg"), "w"))
        c, best = d, sc
print("final", c, best, flush=True)
