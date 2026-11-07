#!/usr/bin/env python3
"""Box 191: REALIZE-CYC data check: N5'-xi's mover phase on Gamma3(G) (from S3) = the IDEAL-CYC run of G, state for state, and
N5'-xi iterations = T_CYC + 3. Usage: eq191.py GENOME.json ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import trace191 as T, idealcyc
ok = bad = 0
for f in sys.argv[1:]:
    G = json.load(open(f)); rows, states, fbs, g = T.trace(G, "xi"); ic = idealcyc.run(G)
    real = [r["ms"] for r in rows]; same = real[:len(ic)] == ic and len(states) - 1 == len(ic) - 1 + 3
    ok += same; bad += not same
    print(f"{os.path.basename(f):30s} N {G['N']:3d} xi {len(states) - 1:3d} T_CYC {len(ic) - 1:3d} {'MATCH' if same else 'MISMATCH'}")
print(f"TOTAL match {ok} mismatch {bad}")
