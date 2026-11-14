#!/usr/bin/env python3
"""Box 191: data check of BR-SEG on the TWO-player IDEAL-CYC: label each step C (some VJ cycle node changes), R (no cycle node
changes but Odd's optimal counterstrategy sigma-bar, as computed by si.Engine, changes somewhere), p (neither). BR-SEG: every
maximal run of p-steps... precisely: every maximal stretch of consecutive steps t -> t+1 with Lambda_t = Lambda_(t+1) and sigma-bar_t
= sigma-bar_(t+1) for all its states has <= N steps. Usage: subrun191.py COUNT SEED | FILES.json"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import idealcyc, rand191

def labels(G):
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G); gi = {}
    for x in range(G["N"]):
        for v in h.succ[movers[x]]: gi[(x, inv[v])] = v
    prev = None; lab = []
    for s in st:
        cur = list(s0)
        for x in range(G["N"]): cur[movers[x]] = gi[(x, s[x])]
        vs, sb = E.evaluate(tuple(cur)); key = ([vs[v][0] for v in range(h.n)], [sb[v] for v in range(h.n) if h.owner[v] == 1])
        if prev is not None: lab.append("C" if key[0] != prev[0] else ("R" if key[1] != prev[1] else "p"))
        prev = key
    return "".join(lab)

def pure_max(lab):
    # a stretch of steps with constant (Lambda, sigma-bar) over ALL its states = a run of p's (each p keeps both)
    return max(len(r) for r in lab.replace("R", "C").split("C")) if lab else 0

if __name__ == "__main__":
    if sys.argv[1].endswith(".json"):
        for f in sys.argv[1:]:
            G = json.load(open(f)); lab = labels(G); print(os.path.basename(f), "N", G["N"], "T", len(lab), "C", lab.count("C"), "R", lab.count("R"), "maxpure", pure_max(lab), lab)
    else:
        cnt, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); viol = 0; worst = 0; tot = [0, 0, 0]
        for i in range(cnt):
            G = rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3)); lab = labels(G); mp = pure_max(lab)
            viol += mp > G["N"]; worst = max(worst, mp / G["N"]); tot = [tot[0] + lab.count("C"), tot[1] + lab.count("R"), tot[2] + lab.count("p")]
        print(f"count {cnt} seed {seed}: maxpure > N in {viol}; max maxpure/N {worst:.2f}; steps C {tot[0]} R {tot[1]} p {tot[2]}")
