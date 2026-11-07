#!/usr/bin/env python3
"""L-RED R214: replay a genome from its STORED start with r187/ideal.py; print T, run end, per-mover moves, max mover, F per level
(moves of level-l movers summed), and lemck + box150 on that run. Usage: lowrep.py g.json ..."""
import sys, os, json, subprocess
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
for f in sys.argv[1:]:
    G = json.load(open(f)); N = G["N"]; d = max(G["lev"]) + 1; S, how = ideal.traj(G)
    mv = [sum(1 for t in range(1, len(S)) if S[t][z] != S[t - 1][z]) for z in range(N)]; z = max(range(N), key=lambda v: mv[v])
    tg = any(o[1] == z for v in range(N) for o in G["opts"][v])
    F = [mv[2 * l] + mv[2 * l + 1] for l in range(d)]
    l = subprocess.run(["python3", "r189/lemck.py", os.path.abspath(f)], capture_output=True, text=True, cwd=os.path.join(H, "..")).stdout.strip()
    b = subprocess.run(["python3", os.path.join(H, "..", "r212", "ref", "box150", "check.py"), f], capture_output=True, text=True).stdout.strip().splitlines()
    print(f"{os.path.basename(f)}: d {d} T {len(S) - 1} end {how} | max mover {z} lev {G['lev'][z]} Xi-target {int(tg)} moves {mv[z]} 2d {2 * d} "
          f"{'>2d' if mv[z] > 2 * d else '<=2d'} | moves {mv} | F {F} | {l[-80:]} | box150 {(b[-1] if b else 'NO OUTPUT')[:80]}", flush=True)
