#!/usr/bin/env python3
"""Box 190: N5' variants on Gamma3(G) from S3 for the P-N5-REACH corpus C14; prints iterations per mode next to L(G) and depth."""
import sys, os, json, glob
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "box189")]
import n5v, gamma3, reachcheck
def xidepth(G):
    N = G["N"]; memo = {}
    def d(x):
        if x not in memo: memo[x] = 1 + max([d(o[1]) for o in G["opts"][x] if o[1] >= 0] or [0])
        return memo[x]
    return max(d(x) for x in range(N))
for f in sorted(glob.glob(os.path.join(HERE, "..", "box189", "corpus", "*.json"))):
    G = json.load(open(f)); L = len(reachcheck.ideal_traj(G)) - 1; g, *_ = gamma3.build(G, {"K", "pe", "pb", "m"})
    out = []
    for m in ("spec", "xi", "idx", "seq"):
        st, fb, _ = n5v.run(g, m); out.append(f"{m} {len(st) - 1}")
    print(f"{os.path.basename(f)} d {max(G['lev']) + 1} N {G['N']} Xi-depth {xidepth(G)} L {L} | " + " | ".join(out), flush=True)
