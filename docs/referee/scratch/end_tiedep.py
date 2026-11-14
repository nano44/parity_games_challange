"""REFEREE successor 29: EXACT-L depends on SPEC's S1 tie-breaks. On IDEAL-ACYC genomes (own generator, family acyc): first fallback F
and total under my N5-w (S4a = a pointwise optimum of H with ties kept at sigma(v); end_replay.run mode n5w) vs L(G) (t3r_sim).
Usage: end_tiedep.py SEED COUNT"""
import sys, os, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import end_replay as er, t3r_sim
seed, cnt = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); tab = collections.Counter(); ex = None
for i in range(cnt):
    G = er.gen(rng, "acyc"); assert er.acyclic(G)
    c, info = er.run(G, "n5w"); L = len(t3r_sim.run(G)) - 1
    ok = info["F"] == L + 1 and info["it"] == L + 3; tab[(L >= 1, ok)] += 1
    if L >= 1 and not ok and ex is None: ex = (i, L, info["F"], info["it"])
print(f"N5-w on acyc {seed} x {cnt}: (L>=1, EXACT-L holds) -> genomes {dict(tab)}; first violation (index, L, F, total) {ex}")
