#!/usr/bin/env python3
"""L-SI box 85: seeded random sweep over two85 wirings (cfg kinds) and lane lengths at a given h. Per genome: meas83 (bits, hubH, R, C,
premature resets) and priv84 (Lemma FLIP / PRIV-FLIP excess over all SET-type units). tog(l) = #steps where bit l (B_l's play passes
its own SET e) changes. Prints one line per sampled genome: score fields + cfg JSON. Usage: sweep85.py BOX81DIR h SEED COUNT"""
import sys, os, json, random, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); B81 = sys.argv[1]; os.environ["BOX81"] = os.path.abspath(B81)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "box84", "m2"))
import two85; from gen83 import save
import priv84
h, seed, count = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed)
WK = ["L", "L-", "B-", "M-", "B+", "L+", "Lw"]; AK = ["L", "L-", "B-", "M-", "L+"]; LK = ["M+", "B+", "L-", "B-", "M-", "L+"]
def sub(ks, p): return [k for k in ks if rng.random() < p]
def meas(path):
    o = subprocess.run([sys.executable, "-I", "-B", os.path.join(HERE, "..", "box83", "meas83.py"), path, B81], capture_output=True, text=True).stdout.split("\n")
    f = o[0].split(); T, R, C = int(f[f.index("T") + 1]), int(f[f.index("R") + 1]), int(f[f.index("C") + 1])
    bits = o[1].split(") ", 1)[1].split(); hubH = int(o[2].split("hubH ")[1].split()[0]); pre = o[2].split("at ")[1].split(" hubH")[0]
    tog = [sum(bits[t][i] != bits[t - 1][i] for t in range(1, len(bits))) for i in range(len(bits[0]))][::-1]   # tog[0] = B1
    return T, R, C, tog, hubH, pre != "[]"
td = tempfile.mkdtemp()
for it in range(count):
    c = {"h": h, "L": [rng.randint(1, 3 * l) for l in range(1, h + 1)], "LM": [rng.randint(2, 6 * l) for l in range(2, h + 1)],
         "lmin": rng.choice([1, 2]), "w": sub(WK, 0.3), "wait": sub(AK, 0.2), "lw": ["M+"] + sub(LK[1:], 0.25),
         "lup": rng.choice(["B+", "M+", "L+"]), "lexit": rng.choice(["B+", "M+"]), "mup": 1}
    c["LL"] = [rng.randint(1, 6 * l) for l in range(c["lmin"], h + 1)]
    try:
        G, nm = two85.build(c); p = os.path.join(td, "g.json"); save(G, nm, p)
        T, R, C, tog, hubH, pre = meas(p); fr = priv84.measure(G)
    except Exception as ex:
        print("ERR", repr(ex)[:80], json.dumps(c), flush=True); continue
    ok = tog[0] >= 2 * tog[1] + 2
    print(f"T {T} R {R} C {C} tog {','.join(map(str, tog))} hubH {hubH} pre {int(pre)} crit {int(ok)} flipex {fr['maxex_priv']}/{fr['maxex_nopriv']} cfg {json.dumps(c)}", flush=True)
