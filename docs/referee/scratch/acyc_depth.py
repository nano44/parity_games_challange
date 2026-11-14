"""REFEREE 28: T_CYC against the level count d (max lev + 1) on set A with 5 random starts per genome (as acyc_replay starts 300 7 5),
Gamma only, own engine. Prints the number of runs with T > d and max T - d. Usage: acyc_depth.py LSI_BOX81"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); box = sys.argv[1]
sys.path[:0] = [box, os.path.join(box, "ref/experiments/new/box191"), os.path.join(box, "ref/experiments/new/box189")]
from lemma81 import agen
from acyc_replay import run
rng = random.Random(7); rs = random.Random(1007); runs = gt = 0; mx = -99; per = {}
for i in range(300):
    G = agen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3)); d = max(G["lev"]) + 1
    for j in range(5):
        H = dict(G); H["start"] = [rs.randrange(len(o)) for o in G["opts"]]; T = run(H, False)["T"]; runs += 1
        gt += T > d; mx = max(mx, T - d); per[d] = max(per.get(d, 0), T)
print("runs", runs, "T > d:", gt, "max T - d:", mx, "max T per d:", dict(sorted(per.items())))
