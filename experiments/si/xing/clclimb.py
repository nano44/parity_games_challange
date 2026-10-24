#!/usr/bin/env python3
"""L-SI box 5: adversarial climb against CONJECTURE (CL) (carry levels non-increasing while w is constant; carries.py).
Fitness = (#CL violations in the longest phase, #carries, phase length). o-cyclic C^1O only (class asserted by xclass.annotate).
Usage: clclimb.py seed secs OUT seed.pg"""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carries import *
sys.path.insert(0, os.path.join(ROOT, "experiments/new/box21")); sys.path.insert(0, os.path.join(ROOT, "experiments/new/box25"))
from climb_fix import mutate
from pureY import split
import carries as C

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, -1, -1)
    g = pg.Game(*G)
    if not any(w in split(g, odd[0]) for w in G[2][odd[0]]): return (-1, -1, -1)
    try:
        tmp = "/tmp/claude-0/clclimb_%d.pg" % os.getpid()
        open(tmp, "w").write(f"parity {n-1};\n" + "".join(f"{v} {G[0][v]} {G[1][v]} {','.join(map(str, G[2][v]))};\n" for v in range(n)))
        out = C.scan(tmp, show=False)
        viol = sum(1 for a, b in zip(out, out[1:]) if b["wsame"] and b["carry_lev"] > a["carry_lev"] and a["carry_lev"] >= 0)
        return (viol, len(out), 0)
    except Exception: return (-1, -1, -1)

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    g = load(sys.argv[4]); n = g.n; G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G)
    t0 = time.time(); it = 0; print("start", f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True)
                open(out + ".pg", "w").write(f"parity {n-1};\n" + "".join(f"{v} {H[0][v]} {H[1][v]} {','.join(map(str, H[2][v]))};\n" for v in range(n)))
            G, f = H, fh
    print("FINAL", f, it, flush=True)
