#!/usr/bin/env python3
"""Box 191: data check of ONEP-POLY's two counts on the ONE-PLAYER model (ONEP=1 forced): every maximal run of PATH steps has
<= N steps (SEG-1P), and #CYCLE steps C <= N*M (CYC-COUNT); also reports the same counts on the TWO-player IDEAL-CYC.
Usage: seg1p191.py COUNT SEED   (random genomes, rand191.rgen with random d 1-6, w 1-3, D 2-3)"""
import sys, os, random, importlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import idealcyc, rand191
cnt, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed)
res = {}
for onep in (True, False):
    idealcyc.ONEP = onep; viol_seg = viol_c = 0; worst = 0.0; worstT = 0; r2 = random.Random(seed)
    for i in range(cnt):
        d, w, D = r2.randint(1, 6), r2.randint(1, 3), r2.randint(2, 3); G = rand191.rgen(r2, d, w, D)
        st, k = idealcyc.run(G, want_kinds=True); N = G["N"]; M = sum(len(o) for o in G["opts"])
        mr = max(len(r) for r in k.split("C")) if k else 0; C = k.count("C")
        viol_seg += mr > N; viol_c += C > N * M; worst = max(worst, mr / N); worstT = max(worstT, len(st) - 1)
    print(f"{'ONE' if onep else 'TWO'}-player: {cnt} genomes seed {seed}: maxrun > N in {viol_seg}, C > N*M in {viol_c}, max maxrun/N {worst:.2f}, max T {worstT}")
