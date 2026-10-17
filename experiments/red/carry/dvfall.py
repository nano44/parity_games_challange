#!/usr/bin/env python3
"""L-RED (box 5): attack on L-ALG's Lemma DV-MONO (GAP-A-M §21f-§21g). Runs L-ALG's experiments/alg/dtl_distval.py
(read-only; LALG_DIR >= efc8249; a transcription of dtl.cpp:553-639 computeDistanceValues) on one game in the order
DTL_ORDER and parses its totals. score = 1000 x transitions where some DV value FALLS (all transitions) + 10 x falls among
the author's checked searches + transitions. Usage: DTL_ORDER=oink LALG_DIR=.. dvfall.py G.pg"""
import sys, os, subprocess, re

def measure(path):
    ld = os.environ["LALG_DIR"]
    r = subprocess.run([sys.executable, os.path.join(ld, "experiments", "alg", "dtl_distval.py"), os.path.abspath(path)],
                       capture_output=True, text=True, timeout=120, cwd=os.path.join(ld, "experiments", "alg"))
    m = re.search(r"some value FALLS: (\d+) \| over all transitions incl\. dominion/last: (\d+) of (\d+)", r.stdout)
    if not m: raise RuntimeError(r.stdout[-300:] + r.stderr[-300:])
    return int(m.group(1)), int(m.group(2)), int(m.group(3))

def score(path):
    f, af, al = measure(path)
    return 1000 * af + 10 * f + al

if __name__ == "__main__":
    for f in sys.argv[1:]:
        a, b, c = measure(f); print(f"{os.path.basename(f)} order={os.environ.get('DTL_ORDER', 'stable')} checked-search falls {a}; all-transition falls {b} of {c}")
