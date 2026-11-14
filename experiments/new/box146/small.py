#!/usr/bin/env python3
"""L-NEW box 146: random search for the smallest DOWN-orientation counterexample to the split-level energy (energy.py) at d = 2
(any acyclic Xi, box143/dclimb.py rand). d = 2 has one split bit, so V0..VLEX coincide up to scale. Usage: small.py trials seed"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__))
s1 = open(os.path.join(HERE, "..", "box143", "dclimb.py")).read().split("def score(G):")[0]
n1 = {"__file__": os.path.join(HERE, "..", "box143", "dclimb.py")}; exec(s1, n1)
s2 = open(os.path.join(HERE, "energy.py")).read().split('\nif __name__ == "__main__":')[0]
n2 = {"__file__": os.path.join(HERE, "energy.py")}; exec(s2, n2)
trials, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); random.seed(seed); best = None
for i in range(trials):
    G = n1["rand"](2, rng); T, nun, nch, viol, first = n2["analyse"](G)
    if viol[("V0", "DOWN")] and (best is None or T < best[0]):
        best = (T, G, first[("V0", "DOWN")]); json.dump(G, open(os.path.join(HERE, "small_d2.json"), "w"))
        print("FOUND trial", i, "steps", T, "first", first[("V0", "DOWN")], flush=True)
print("DONE", "found" if best else "none")
