#!/usr/bin/env python3
"""L-RED box 13 (produced on Opus 5.5): at every chain-changing transition of a phase, the vertices that supply a NEW K-v-all key
(b12_pot.run / chain / keys / sig imported UNMODIFIED from LALG_DIR), with their new key and their keys seen earlier in the
phase, plus the depth-0 chain (j, |R_j|, rank, |V_j|) of both searches. Usage: DTL_ORDER=... newkeys.py G.pg [max]"""
import sys, os
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
import pg, b12_pot as B
sys.setrecursionlimit(100000)
g = pg.read(sys.argv[1]); MX = int(sys.argv[2]) if len(sys.argv) > 2 else 5; order = os.environ.get("DTL_ORDER", "stable")
d = B.run(g, order); seen = None; prev = None; pch = None; shown = 0
for ph, calls in getattr(d, "log", []):
    ch = B.chain(calls, g.n); k = B.keys(ch)["K-v-all"]
    if prev is not None and prev[0] == ph and B.sig(ch) != prev[1]:
        new = k - seen; vs = sorted({x[0] for x in new})
        if len(vs) <= 1 and shown < MX:
            shown += 1
            print("chain before:", [(j, len(R), r, len(V)) for j, R, r, V, pc, _ in pch])
            print("chain after: ", [(j, len(R), r, len(V)) for j, R, r, V, pc, _ in ch])
            for x in sorted(new): print("  new key", x, "| earlier keys of v:", sorted(y[1:] for y in seen if y[0] == x[0]))
    if prev is None or prev[0] != ph: seen = set()
    seen |= k; prev = (ph, B.sig(ch)); pch = ch
