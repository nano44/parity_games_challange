#!/usr/bin/env python3
"""L-RED R199 CEGAR2: exact loop between r199/xwake.py (corrected wake-order relaxation; proposes extra-level moves, starts and gate bits)
and r199/xisat.py (exact Xi side with every state fixed). A refuted proposal (moves + start + gate bits) is blocked; xwake UNSAT = EXACT
UNSAT for this main target (its gate choice); xisat SAT = genome. Usage: cegar2.py main_target.json E maxiter prefix"""
import sys, os, json, subprocess, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import req as RQ, xisat, xisearch as XS, ideal
T = json.load(open(sys.argv[1])); E = int(sys.argv[2]); mx = int(sys.argv[3]); pre = sys.argv[4]
blk = pre + "_blocks.json"; json.dump([], open(blk, "w")); S0 = T["states"]; N0 = len(T["movers"]); L = len(S0) - 1; m0 = max(m[0] for m in T["movers"]) + 1
for it in range(mx):
    t0 = time.time()
    r = subprocess.run([sys.executable, os.path.join(H, "xwake.py"), sys.argv[1], str(E), pre + "_w.json"], env=dict(os.environ, BLOCKS=blk), capture_output=True, text=True).stdout
    if "-> sat" not in r: print(f"CEGAR2 iter {it}: xwake {r.strip().splitlines()[0] if r.strip() else 'ERR'} -> EXACT UNSAT", flush=True); break
    W = json.load(open(pre + "_w.json")); N = len(W["movers"]); lev = [m[0] for m in W["movers"]]; WT = [m[1] for m in W["movers"]]
    moves = {int(v): set(ts) for v, ts in W["moves"].items()}; start = list(S0[0]) + [W["start"][str(v)] if str(v) in W["start"] else W["start"][v] for v in range(N0, N)]
    gate = [list(g) for g in T["gate"]] + [[0, 0] for _ in range(N - N0)]
    for l in range(m0, m0 + E):
        for k in (0, 1):
            lo, hi = 2000 + 4 * l + 2 * k, 2001 + 4 * l + 2 * k; g = W["G"][f"{l},{k}"]
            gate[2 * l][k], gate[2 * l + 1][k] = (lo, hi) if g else (hi, lo)
    S = [tuple(start)]; cur = list(start)
    for t in range(1, L + 1):
        cur = [S0[t][v] if v < N0 else (cur[v] ^ (1 if t in moves.get(v, ()) else 0)) for v in range(N)]; S.append(tuple(cur))
    bad, rq = RQ.requirements(lev, WT, gate, S)
    if bad: print("CEGAR2 inconsistency: xwake proposal violates the W side", bad[:5]); sys.exit(3)
    allow = {}
    for x, y in W.get("edges", []): allow.setdefault(x, []).append(y)
    res, dt, sol = xisat.solve(lev, WT, S, rq, tmo=int(os.environ.get("QTMO", "180")), allow={v: allow.get(v, []) for v in range(N)})
    print(f"  quick (Xi-targets within xwake's edges) {res} {dt:.0f} s", flush=True)
    if res != "sat": res, dt, sol = xisat.solve(lev, WT, S, rq, tmo=int(os.environ.get("XTMO", "900")))
    if res == "sat":
        G = RQ.genome(lev, WT, gate, S[0], dict(xt=sol["xt"], pos=XS.topo(N, sol["xt"]), rank=sol["rank"], par=sol["par"]))
        json.dump(G, open(pre + "_genome.json", "w")); S2, why = ideal.traj(G)
        print(f"CEGAR2 iter {it}: SAT -> {pre}_genome.json replay L {len(S2) - 1} {why} matches {list(S2[:L + 1]) == S}", flush=True); break
    if res != "unsat": print(f"CEGAR2 iter {it}: xisat {res} ({dt:.0f} s) -> stopping, UNKNOWN", flush=True); sys.exit(2)
    B = json.load(open(blk)); B.append(dict(moves=W["moves"], start=W["start"], G=W["G"])); json.dump(B, open(blk, "w"))
    print(f"CEGAR2 iter {it}: refuted (xwake + xisat {time.time() - t0:.0f} s); blocked {len(B)}", flush=True)
else: print("CEGAR2 undecided after", mx)
