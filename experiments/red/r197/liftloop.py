#!/usr/bin/env python3
"""L-RED R197 LIFTLOOP: REL -> FIX lift loop with blocking clauses (queue item «d 4 exact by repeated lifts»). Repeat: solve the
relaxation (bmcfork REL=1, free distinct integer weights: its UNSAT is an exact upper bound) excluding every structure (Xi-targets,
gates, start) already refuted; lift the model with FIX (exact ranks / parities free); SAT -> done (exact witness), UNSAT -> block it.
Environment passes through (XI, FMIN, LEM, LAG, KF). Usage: liftloop.py d L maxiter outprefix"""
import sys, os, json, subprocess, time
H = os.path.dirname(os.path.abspath(__file__)); d, L, mx, pre = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
blk = pre + "_block.json"; json.dump([], open(blk, "w"))
for i in range(mx):
    t0 = time.time(); env = dict(os.environ, REL="1", BLOCK=blk)
    r = subprocess.run([sys.executable, os.path.join(H, "bmcfork.py"), d, L, pre + "_rel.json"], env=env, capture_output=True, text=True).stdout
    if "-> sat" not in r: print(f"LIFTLOOP iter {i}: REL {r.strip().splitlines()[0] if r.strip() else 'ERROR'} ({time.time() - t0:.0f} s): exact UNSAT (relaxation)", flush=True); break
    env = dict(os.environ, FIX=pre + "_rel.json"); env.pop("REL", None); env.pop("BLOCK", None); t1 = time.time()
    r2 = subprocess.run([sys.executable, os.path.join(H, "bmcfork.py"), d, L, pre + "_exact.json"], env=env, capture_output=True, text=True).stdout
    if "-> sat" in r2: print(f"LIFTLOOP iter {i}: REL sat ({t1 - t0:.0f} s), FIX sat ({time.time() - t1:.0f} s): exact SAT, {pre}_exact.json", flush=True); break
    B = json.load(open(blk)); B.append(json.load(open(pre + "_rel.json"))); json.dump(B, open(blk, "w"))
    print(f"LIFTLOOP iter {i}: REL sat ({t1 - t0:.0f} s), FIX unsat ({time.time() - t1:.0f} s): blocked {len(B)}", flush=True)
else: print("LIFTLOOP undecided after", mx, "iterations")
