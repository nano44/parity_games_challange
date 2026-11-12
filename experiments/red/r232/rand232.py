#!/usr/bin/env python3
"""L-RED 65 R232: how3_232 counters (locfail, chainfail; own HOW3 engine) and the T3 cross-check against n5v on random genomes from
L-RED's own generator (r231/dep231.rgen = r221q brute221.rgen; Xi-cyclic allowed). Usage: rand232.py SEED COUNT"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r231"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r230"))
from dep231 import rgen
from how3_232 import how3, analyse
import ret230
rng = random.Random(int(sys.argv[1])); tot = dict(genomes=0, locfail=0, chainfail=0, t3diff=0, maxratio=0, maxT3=0)
for i in range(int(sys.argv[2])):
    G = rgen(rng, rng.randint(1, 5), rng.randint(1, 4), rng.choice([2, 3, 4])); a = analyse(G, how3(G)); t5 = ret230.run(G)["T3"]
    tot["genomes"] += 1; tot["locfail"] += a["locfail"]; tot["chainfail"] += a["chainfail"]; tot["t3diff"] += t5 != a["T3"]
    tot["maxratio"] = max(tot["maxratio"], a["maxratio"]); tot["maxT3"] = max(tot["maxT3"], a["T3"])
    if a["locfail"] or a["chainfail"] or t5 != a["T3"]: print("r%d" % i, a, "T3n5v", t5, flush=True)
print("TOTAL", tot, flush=True)
