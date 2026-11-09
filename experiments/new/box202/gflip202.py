#!/usr/bin/env python3
"""Box 202 (L-NEW successor 67): per-gate flip census on the Gamma3 Howard run (N5'-xi from S3, up to the first fallback).
For each gate g (Odd, faces pe_g, pbeta_g): flips(g) := #steps t with sigma-bar_(t-1)(g) != sigma-bar_t(g); lamch(g) := #steps at which
Lambda changes at pe_g or at pbeta_g. Printed: maxflip (max over gates of flips), at the argmax: lamch, the face Lambda values seen;
gates with flips > 2*lamch + 1 (counter k1fail: CONJECTURE K1-FLIP «flips(g) <= 2*lamch(g) + 1» — stated for k(G) = 1; measured
on every genome, the k is printed by fvs202). Also totflips and #gates that ever flip.
Usage: gflip202.py G.json ...  (ROOT: repo root, default from this file's place)."""
import sys, os, json, collections
ROOT = os.environ.get("ROOT") or os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
os.environ.setdefault("EG195_ROOT", ROOT)
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box195", "experiments/new/box191", "experiments/new/box189",
                "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import eg195, gamma3, n5v, n5x
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fvs202

for f in sys.argv[1:]:
    G = json.load(open(f)); k = fvs202.kfvs(G)[0]
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0); n = g.n; name = {v: kk for kk, v in V.items()}
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None); H = []
    while len(H) <= 20000:
        vs, tb = E.evaluate(tuple(sigma)); H.append((tuple(sigma), vs, tb)); res = n5v.step(g, E, Ed, sigma, tau, "xi")
        if res is None or res[4]: break
        sigma, tau = res[0], res[1]
    T = len(H) - 1
    gates = [v for v in range(n) if isinstance(name[v], tuple) and name[v][0] == "g"]
    fl = collections.Counter(); lc = collections.Counter(); lams = collections.defaultdict(set)
    for q in gates:
        pe, pb = V[("pe", name[q][1])], V[("pbeta", name[q][1])]
        for t in range(T + 1):
            lams[q].add((H[t][1][pe][0], H[t][1][pb][0]))
            if t == 0: continue
            fl[q] += H[t - 1][2][q] != H[t][2][q]
            lc[q] += (H[t - 1][1][pe][0] != H[t][1][pe][0]) or (H[t - 1][1][pb][0] != H[t][1][pb][0])
    k1fail = sum(1 for q in gates if fl[q] > 2 * lc[q] + 1)
    am = max(gates, key=lambda q: fl[q])
    print(os.path.basename(f), "k", k, "T3", T, "k1fail", k1fail, "| maxflip", fl[am], "at", name[am], "lamch", lc[am],
          "faceLambdas", len(lams[am]), "totflips", sum(fl.values()), "flipgates", sum(1 for q in gates if fl[q]), flush=True)
