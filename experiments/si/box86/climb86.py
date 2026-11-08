#!/usr/bin/env python3
"""L-SI box 86 hill-climb over lag86 cfgs (lane lengths L, copy lane law a, b, c; cpos, wreal, merge, cexit) at fixed h. Score (lex)
= (CNT, REARM, -#premature resets, hubH) from box85/ana85.py. Saves any genome with FLIP excess > 0 to OUTDIR/flipex_*.json.
Usage: climb86.py BOX81DIR h SEED ITERS OUTDIR"""
import sys, os, json, random, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "box85")]
import lag86, ana85; from gen83 import save
B81, h, seed, iters, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
ana85.B81 = B81; rng = random.Random(seed); os.makedirs(out, exist_ok=True); td = tempfile.mkdtemp()
def rnd():
    return {"h": h, "L": [rng.randint(1, 4 * l) for l in range(1, h + 1)], "a": rng.randint(0, 4), "b": rng.randint(0, 4), "c": rng.randint(1, 6),
            "cpos": rng.choice([1, -1]), "wreal": rng.choice([0, 1]), "merge": rng.choice([0, 1]), "cexit": rng.choice(["C", "B"])}
def mutate(c):
    c = json.loads(json.dumps(c)); r = rng.randrange(6)
    if r == 0: i = rng.randrange(h); c["L"][i] = max(1, c["L"][i] + rng.choice([-3, -2, -1, 1, 2, 3]))
    elif r == 1: k = rng.choice("abc"); c[k] = max(0 if k != "c" else 1, c[k] + rng.choice([-2, -1, 1, 2]))
    elif r == 2: c["cpos"] = -c["cpos"]
    elif r == 3: c["wreal"] ^= 1
    elif r == 4: c["merge"] ^= 1
    else: c["cexit"] = "B" if c["cexit"] == "C" else "C"
    return c
best = None
for it in range(iters):
    c = rnd() if best is None or rng.random() < .05 else mutate(best[1])
    try:
        G, nm = lag86.build(c); p = os.path.join(td, "g.json"); save(G, nm, p); a = ana85.analyse(p)
    except Exception: continue
    fe = [x for x in a["flipex"] if x is not None]
    if fe and max(fe) > 0: save(G, nm, os.path.join(out, f"flipex_s{seed}_{it}.json"))
    npre = 0 if a["pre"] == "[]" else a["pre"].count(",") + 1
    s = (a["CNT"], a["REARM"], -npre, a["hubH"])
    if best is None or s > best[0]:
        print(f"it {it} score {s} T {a['T']} tog {a['tog']} U {a['U']} flipex {a['flipex']} pre {a['pre']} cfg {json.dumps(c)}", flush=True)
    if best is None or s >= best[0]: best = (s, c)
json.dump(best[1], open(os.path.join(out, f"best_h{h}_s{seed}.json"), "w")); print("BEST", best[0], json.dumps(best[1]))
