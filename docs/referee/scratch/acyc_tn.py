"""REFEREE 28: per-genome T / N on set A (lemma81.agen 300 7) with own engine (acyc_replay.run, Gamma): max T/N over N >= 2, and the
Gamma3-vs-Gamma Howard equality count. Usage: acyc_tn.py LSI_BOX81"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); box = sys.argv[1]
sys.path[:0] = [box, os.path.join(box, "ref/experiments/new/box191"), os.path.join(box, "ref/experiments/new/box189")]
from lemma81 import agen
from acyc_replay import run
rng = random.Random(7); hist = {}; best = (0, None); Ns = {}
for i in range(300):
    G = agen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3)); N = G["N"]; T = run(G, False)["T"]
    Ns[N] = Ns.get(N, 0) + 1; hist[(N, T)] = hist.get((N, T), 0) + 1
    if N >= 2 and T / N > best[0]: best = (T / N, (i, N, T))
print("genomes per N:", dict(sorted(Ns.items())))
print("max T/N over N >= 2:", round(best[0], 3), "at (index, N, T)", best[1])
print("max T per N:", {N: max(T for (n, T) in hist if n == N) for N in sorted(Ns)})
