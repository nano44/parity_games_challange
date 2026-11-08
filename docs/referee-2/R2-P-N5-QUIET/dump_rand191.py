# REFEREE-2 succ. 33: dumps the lane's random set (rand191.rgen, the call sequence of loc194/quiet194/bonly194 «rand COUNT SEED») as DATA
# to JSONL. Only the generator is called; no lane checking code is run. Usage: dump_rand191.py BOX191_DIR COUNT SEED OUT.jsonl
import sys, json, random
sys.path.insert(0, sys.argv[1]); import rand191
rng = random.Random(int(sys.argv[3]))
with open(sys.argv[4], "w") as f:
    for _ in range(int(sys.argv[2])): f.write(json.dumps(rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))) + "\n")
