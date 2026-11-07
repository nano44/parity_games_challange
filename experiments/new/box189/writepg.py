#!/usr/bin/env python3
"""Box 189: write Gamma3(G) (all pads) and Gamma(G) (no pads) as PGSolver .pg files plus a .start file (R104's stated start,
transported). Usage: writepg.py GENOME OUTPREFIX"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gamma3
def write(g, sig, tau, pre):
    with open(pre + ".pg", "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
    with open(pre + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(sig.items())) + "\n")
        f.write("TAU0 " + " ".join(f"{v}:{w}" for v, w in sorted(tau.items())) + "\n")
if __name__ == "__main__":
    G = json.load(open(sys.argv[1]))
    for tag, pads in (("g3", {"K", "pe", "pb", "m"}), ("g0", set())):
        g, sig, tau, V = gamma3.build(G, pads); write(g, sig, tau, sys.argv[2] + "_" + tag)
