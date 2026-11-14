#!/usr/bin/env python3
"""L-SI box 85 hill-climb over two85 cfgs (wiring kinds + lane lengths) at fixed h. Score (lexicographic) = (CNT, REARM, tog(1) - 2 tog(2),
hubH) from ana85 (CNT = in-order binary counter prefix; REARM = carry-reset-then-set of bit 1). Keeps every genome whose Lemma FLIP
excess > 0 (a finding against L-RED R222 §4) in OUTDIR/flipex_*.json. Usage: climb85.py BOX81DIR h SEED ITERS OUTDIR"""
import sys, os, json, random, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import two85, ana85; from gen83 import save
B81, h, seed, iters, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
ana85.B81 = B81; rng = random.Random(seed); os.makedirs(out, exist_ok=True); td = tempfile.mkdtemp()
WK = ["L", "L-", "B-", "M-", "B+", "L+", "Lw"]; AK = ["L", "L-", "B-", "M-", "L+"]; LK = ["B+", "L-", "B-", "M-", "L+"]
def rnd():
    c = {"h": h, "L": [rng.randint(1, 3 * l) for l in range(1, h + 1)], "LM": [rng.randint(2, 6 * l) for l in range(2, h + 1)],
         "lmin": rng.choice([1, 2]), "w": [k for k in WK if rng.random() < .3], "wait": [k for k in AK if rng.random() < .2],
         "lw": ["M+"] + [k for k in LK if rng.random() < .25], "lup": rng.choice(["B+", "M+", "L+"]), "lexit": rng.choice(["B+", "M+"]), "mup": 1}
    c["LL"] = [rng.randint(1, 6 * l) for l in range(c["lmin"], h + 1)]; return c
def mutate(c):
    c = json.loads(json.dumps(c)); r = rng.randrange(7)
    if r == 0: k = rng.choice(WK); c["w"] = sorted(set(c["w"]) ^ {k})
    elif r == 1: k = rng.choice(AK); c["wait"] = sorted(set(c["wait"]) ^ {k})
    elif r == 2: k = rng.choice(LK); c["lw"] = ["M+"] + sorted(set(c["lw"][1:]) ^ {k})
    elif r == 3: c["lup"] = rng.choice(["B+", "M+", "L+"]); c["lexit"] = rng.choice(["B+", "M+"])
    elif r == 4:
        c["lmin"] = 3 - c["lmin"]; c["LL"] = ([rng.randint(1, 6)] + c["LL"]) if c["lmin"] == 1 else c["LL"][1:]
    else:
        key = rng.choice(["L", "LM", "LL"]); i = rng.randrange(len(c[key])); c[key][i] = max(1, c[key][i] + rng.choice([-3, -2, -1, 1, 2, 3]))
    return c
def score(c):
    G, nm = two85.build(c); p = os.path.join(td, "g.json"); save(G, nm, p); a = ana85.analyse(p)
    fe = max(x for x in a["flipex"] if x is not None) if any(x is not None for x in a["flipex"]) else None
    if fe is not None and fe > 0: save(G, nm, os.path.join(out, f"flipex_s{seed}_{a['T']}_{rng.randrange(10**6)}.json"))
    return (a["CNT"], a["REARM"], a["tog"][0] - 2 * a["tog"][1], a["hubH"]), a
best = None
for it in range(iters):
    c = rnd() if best is None or rng.random() < .05 else mutate(best[1])
    try: s, a = score(c)
    except Exception as ex: continue
    if best is None or s >= best[0]:
        if best is None or s > best[0]:
            print(f"it {it} score {s} T {a['T']} R {a['R']} C {a['C']} tog {a['tog']} U {a['U']} maxDE {a['maxDE']} flipex {a['flipex']} pre {a['pre']} cfg {json.dumps(c)}", flush=True)
        best = (s, c)
json.dump(best[1], open(os.path.join(out, f"best_h{h}_s{seed}.json"), "w")); print("BEST", best[0], json.dumps(best[1]))
