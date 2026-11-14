#!/usr/bin/env python3
"""Box 189: random IDEAL-ACYC genomes (seeded). Per genome: (A) Gamma3 (all pads): S3 == stated start, N5 from S3 has an FL run
[0, L(G)] and movers follow the IDEAL run (run3.main); (B) Gamma (no pads): N5 from S3 iterations, and BLIND: the N5 run's state
sequence is IDENTICAL after re-drawing (br, bp) (keeping everything else). Usage: randtest.py SEED COUNT"""
import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import run3, gamma3, n5x
def gen(rng):
    d = rng.randint(1, 4); N = 0; lev = []
    for l in range(d):
        w = rng.randint(1, 3); lev += [l] * w
    N = len(lev); order = list(range(N)); rng.shuffle(order); pos = {x: i for i, x in enumerate(order)}   # Xi-topological order
    opts = []
    for x in range(N):
        deg = rng.randint(2, 3); o = []
        for k in range(deg):
            wt = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] > 0 else -1
            later = [y for y in range(N) if pos[y] > pos[x]]
            xt = rng.choice(later) if later and rng.random() < 0.7 else -1
            o.append([wt, xt, None])
        opts.append(o)
    M = sum(len(o) for o in opts); bids = list(range(M)); rng.shuffle(bids); i = 0
    for o in opts:
        for q in o: q[2] = bids[i]; i += 1
    gl = list(range(M)); rng.shuffle(gl); i = 0; gate = []
    for o in opts: gate.append(gl[i:i + len(o)]); i += len(o)
    br = list(range(M)); rng.shuffle(br); bp = [rng.randint(0, 1) for _ in range(M)]
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": [rng.randrange(len(o)) for o in opts]}
if __name__ == "__main__":
    seed, cnt = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); bad = 0; Ls = []; its0 = []; blind = 0
    tmp = f"/tmp/box189_rand_{seed}.json"
    for i in range(cnt):
        G = gen(rng); json.dump(G, open(tmp, "w"))
        same, it, runs, follow, L = run3.main(tmp, {"K", "pe", "pb", "m"})
        okA = same and follow == L and (L == 0 and runs == [] or runs and runs[0] == (0, L))
        g, *_ = gamma3.build(G, set()); st, _ = n5x.trace(g, None, check=False)
        G2 = dict(G); br = list(G["br"]); rng.shuffle(br); G2["br"] = br; G2["bp"] = [rng.randint(0, 1) for _ in br]
        g2, *_ = gamma3.build(G2, set()); st2, _ = n5x.trace(g2, None, check=False)
        okB = st == st2; blind += okB; its0.append(len(st) - 1); Ls.append(L)
        if not okA or not okB: bad += 1; json.dump(G, open(f"/tmp/box189_bad_{seed}_{i}.json", "w")); print("BAD", i, okA, okB)
    print(f"SEED {seed} genomes {cnt} Gamma3-ok {cnt - bad if True else 0} bad {bad} | L(G) max {max(Ls)} mean {sum(Ls)/len(Ls):.1f} | "
          f"Gamma-from-S3 iterations {sorted(set(its0))} | BLIND identical runs {blind}/{cnt}")
