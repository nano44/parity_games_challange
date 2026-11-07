"""REFEREE successor 26: BR-SEG / CYC-COUNT / LEVEL0 on IDEAL-CYC(Gamma) of random genomes (lane generator rand191.rgen used only to
draw genomes), own builder + own engine. Usage: xicyc_brseg_rand.py LNEW_ROOT COUNT SEED"""
import sys, os, random
R = sys.argv[1]; sys.path[:0] = [os.path.dirname(os.path.abspath(__file__)), os.path.join(R, "experiments/new/box191")]
import rand191
from xicyc_replay import howard
cnt, seed = int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); t = dict(genomes=0, steps=0, C=0, R=0, p=0, prun_gt_N=0, C_gt_bound=0, lvl0_eface=0, lvl0_pairs=0, ties=0)
for i in range(cnt):
    G = rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3)); E, lab, ties, states, movers, idx = howard(G)
    N = G["N"]; M = sum(len(o) for o in G["opts"]); n = E.n
    pm = max((len(r) for r in lab.replace("R", "C").split("C")), default=0)
    t["genomes"] += 1; t["steps"] += len(lab); t["ties"] += ties
    for c in "CRp": t[c] += lab.count(c)
    t["prun_gt_N"] += pm > N; t["C_gt_bound"] += lab.count("C") > n * (2 * M + 2)
    lv0 = [idx[("g", (x, k))] for x in range(N) if G["lev"][x] == 0 for k in range(len(G["opts"][x]))]
    for (s, st, val) in states:
        for g in lv0: t["lvl0_pairs"] += 1; t["lvl0_eface"] += st[g] == E.succ[g][0]   # succ[g][0] = e-face (builder order [e, beta])
print(f"BR-SEG/CYC-COUNT/LEVEL0 own replay count {cnt} seed {seed}:", t)
