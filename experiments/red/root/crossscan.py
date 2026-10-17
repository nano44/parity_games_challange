#!/usr/bin/env python3
"""L-RED box 8 (produced on Opus 5.5): add ONE cross edge u -> w between the two halves of a stacked game (L = ids < H,
U = ids >= H) for every u in the given id range and every w in the other half; score with root/depthgrad.py (LALGR_DIR,
DTL_ORDER). Keeps variants with max depth >= 2 or incomplete. Usage: crossscan.py BASE.pg H UFROM UTO OUTDIR"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import depthgrad as DG
base, H, a, b, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
g0 = DG.pg.read(base); os.makedirs(out, exist_ok=True); sys.setrecursionlimit(100000)
for u in range(a, b):
    for w in (range(H, g0.n) if u < H else range(H)):
        succ = [list(s) for s in g0.succ]; succ[u] = sorted(set(succ[u]) | {w})
        g = DG.pg.Game(list(g0.prio), list(g0.owner), succ)
        try: m = DG.measure_game(g, os.environ.get("DTL_ORDER", "stable"))
        except Exception as e: print(u, w, "ERR", e, flush=True); continue
        print(u, w, m, flush=True)
        if m["maxd"] >= 2 or m["incomplete"]:
            with open(f"{out}/x_{u}_{w}.pg", "w") as f:
                f.write(f"parity {g.n - 1};\n" + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, succ[v]))};\n" for v in range(g.n)))
