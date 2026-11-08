#!/usr/bin/env python3
"""L-RED 56 R221 (d): trace N5'-xi on Gamma3(G) (box 190 n5v.step, mode xi) iteration by iteration: mover option tuple (gamma3.mover_state),
fallback flag of the iteration; print beside own.py's IDEAL-CYC trajectory. Needs env WT, WT3. Usage: trace221.py G.json"""
import sys, os, json
WT, WT3 = os.environ["WT"], os.environ["WT3"]
sys.path[:0] = [os.path.join(WT3, "experiments/new/box191"), os.path.join(WT, "experiments/new/box190"), os.path.join(WT, "experiments/harness"), os.path.join(WT3, "experiments/new/box189")]
import gamma3, n5v, n5x, pg
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import own
def topg(g): return f"parity {g.n - 1};\n" + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n))
G = json.load(open(sys.argv[1])); o, V, O, _ = own.run(G)
inv = {V[("g", (x, k))]: k for x in range(G["N"]) for k in range(len(G["opts"][x]))}
traj = [tuple(inv[v] for v in s) for s, _, _ in o]
pads = {"K", "pe", "pb", "m"}; g, sig, tau, VV = gamma3.build(G, pads); gp = pg.parse(topg(g))
E, Ed = n5v.Engine(gp), n5v.Engine(n5v.dual(gp)); sigma, tau = n5x.start_pair(gp, E, Ed, None); it = 0
print("own IDEAL-CYC trajectory:", traj)
print(it, gamma3.mover_state(G, VV, sigma, pads), "start")
while True:
    r = n5v.step(gp, E, Ed, sigma, tau, "xi")
    if r is None: break
    sigma, tau, Is, It, fb = r; it += 1
    print(it, gamma3.mover_state(G, VV, sigma, pads), "fb" if fb else "", "Is" if Is else "", "It" if It else "")
