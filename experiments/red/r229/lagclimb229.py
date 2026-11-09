#!/usr/bin/env python3
"""L-RED 63 R229 item 1 (K6 at h >= 4): hill-climb over box 86's lag86 cfg space (the same space and moves as L-SI's climb86.py: lane
lengths L, copy-lane law a, b, c, cpos, wreal, merge, cexit) at fixed h, on R221 own.py with lag229's own counters.
Score (lex) = (CNT, REARM, -(N + M)); a full h-bit counter has CNT = 2^h. Freezes each strict (CNT, REARM) gain to
out/lc_<h>_<SEED>.json (+ .names.json, + .cfg.json). Usage: lagclimb229.py h SEED ITERS   (env SI86 as lag229)"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r221"), os.environ["SI86"]]
import lag86, lag229
h, seed, iters = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed)
def rnd():
    return {"h": h, "L": [rng.randint(1, 4 * l) for l in range(1, h + 1)], "a": rng.randint(0, 4), "b": rng.randint(0, 4), "c": rng.randint(1, 6),
            "cpos": rng.choice([1, -1]), "wreal": rng.choice([0, 1]), "merge": rng.choice([0, 1]), "cexit": rng.choice(["C", "B"])}
def mutate(c):
    c = json.loads(json.dumps(c)); r = rng.randrange(6)
    if r == 0: i = rng.randrange(h); c["L"][i] = max(1, c["L"][i] + rng.choice([-3, -2, -1, 1, 2, 3]))
    elif r == 1: k = rng.choice("abc"); c[k] = max(0 if k != "c" else 1, c[k] + rng.choice([-2, -1, 1, 2]))
    elif r == 2: c["cpos"] *= -1
    elif r == 3: c["wreal"] ^= 1
    elif r == 4: c["merge"] ^= 1
    else: c["cexit"] = "B" if c["cexit"] == "C" else "C"
    return c
best = None
for it in range(iters):
    c = rnd() if best is None or rng.random() < .05 else mutate(best[1])
    try:
        G, nm = lag86.build(c); _, tog, cnt, rearm, _ = lag229.bits_run(G, nm)
    except Exception as ex:
        continue
    sz = G["N"] + sum(len(o) for o in G["opts"]); s = (cnt, rearm, -sz)
    if best is None or s >= best[0]:
        if best is None or s[:2] > best[0][:2]:
            p = f"{H}/out/lc_{h}_{seed}"; json.dump(G, open(p + ".json", "w")); json.dump(nm, open(p + ".names.json", "w")); json.dump(c, open(p + ".cfg.json", "w"))
            print(it, "CNT", cnt, "REARM", rearm, "tog", tog, "N+M", sz, "cfg", json.dumps(c), flush=True)
        best = (s, c)
print("FINAL h", h, "best", best[0], json.dumps(best[1]), flush=True)
