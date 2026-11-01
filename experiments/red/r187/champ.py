import sys, os, json
sys.path[:0] = [os.path.dirname(os.path.abspath(__file__))]
import t2, ideal, rel
for f in sys.argv[1:]:
    G = json.load(open(f)); S, why = ideal.traj(G)
    r = t2.cmp(G); st = rel.stats(G, S)
    print(os.path.basename(f), "IDEAL", len(S) - 1, why, "REAL faithful", r[2], "states equal", r[3], st, flush=True)
