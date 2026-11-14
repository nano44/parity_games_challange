#!/usr/bin/env python3
"""L-RED R199 CEGAR: alternate r199/xwake.py (wake-order relaxation: proposes aux schedules) and r199/xisat.py (exact Xi side with all
states fixed). An aux schedule refuted by xisat is blocked (BLOCKS, exact: that schedule has no realisation, with the start / gate bits
re-chosen freely inside xisat? no: xisat fixes the proposed start and gate bits; the block removes the move pattern, so the loop is
exact only if every start / gate choice of a blocked pattern is refuted: we therefore refute each pattern for ALL 2^#aux starts x gate
bits consistent with it (build-style enumeration)). UNSAT of xwake = exact obstruction; xisat SAT = genome.
Usage: cegar.py main_target.json E maxiter prefix"""
import sys, os, json, subprocess, itertools
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import req as RQ, xisat, xisearch as XS, ideal
T = json.load(open(sys.argv[1])); E = sys.argv[2]; mx = int(sys.argv[3]); pre = sys.argv[4]
blk = pre + "_blocks.json"; json.dump([], open(blk, "w"))
lev0 = [m[0] for m in T["movers"]]; N0 = len(lev0); m0 = max(lev0) + 1; S0 = T["states"]; L = len(S0) - 1
for it in range(mx):
    r = subprocess.run([sys.executable, os.path.join(H, "xwake.py"), sys.argv[1], E, pre + "_w.json"], env=dict(os.environ, BLOCKS=blk), capture_output=True, text=True).stdout
    if "-> sat" not in r: print(f"CEGAR iter {it}: xwake {r.strip().splitlines()[0] if r.strip() else 'ERR'} -> EXACT UNSAT (all aux schedules refuted)", flush=True); break
    W = json.load(open(pre + "_w.json")); N = len(W["movers"]); lev = [m[0] for m in W["movers"]]; WT = [m[1] for m in W["movers"]]
    moves = {int(v): set(ts) for v, ts in W["moves"].items()}
    found = None; tried = 0; feas = 0
    for starts in itertools.product((0, 1), repeat=N - N0):
        for gb in itertools.product((0, 1), repeat=2 * (m0 + int(E) - m0)):
            start = list(S0[0]) + list(starts); gate = [list(g) for g in T["gate"]] + [[0, 0] for _ in range(N - N0)]
            for j, l in enumerate(range(m0, m0 + int(E))):
                for k in (0, 1):
                    lo, hi = 2000 + 4 * l + 2 * k, 2001 + 4 * l + 2 * k
                    gate[2 * l][k], gate[2 * l + 1][k] = (lo, hi) if gb[2 * j + k] else (hi, lo)
            S = [tuple(start)]; cur = list(start)
            for t in range(1, L + 1):
                cur = [S0[t][v] if v < N0 else (cur[v] ^ (1 if t in moves.get(v, ()) else 0)) for v in range(N)]; S.append(tuple(cur))
            bad, rq = RQ.requirements(lev, WT, gate, S)
            if bad: continue
            feas += 1; res, dt, sol = xisat.solve(lev, WT, S, rq, tmo=600)
            tried += 1
            if res == "sat":
                G = RQ.genome(lev, WT, gate, S[0], dict(xt=sol["xt"], pos=XS.topo(N, sol["xt"]), rank=sol["rank"], par=sol["par"]))
                json.dump(G, open(pre + "_genome.json", "w")); S2, why = ideal.traj(G); found = (len(S2) - 1, why, list(S2[:L + 1]) == S); break
            if res != "unsat": print("  xisat", res, "-> pattern not refuted; stopping (inexact)"); sys.exit(2)
        if found: break
    if found: print(f"CEGAR iter {it}: SAT genome {pre}_genome.json replay L {found[0]} {found[1]} matches {found[2]}", flush=True); break
    B = json.load(open(blk)); B.append(W["moves"]); json.dump(B, open(blk, "w"))
    print(f"CEGAR iter {it}: pattern refuted (W-feasible start/gate choices {feas}, xisat UNSAT each); blocked {len(B)}", flush=True)
else: print("CEGAR undecided after", mx)
