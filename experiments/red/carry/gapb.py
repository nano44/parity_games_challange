#!/usr/bin/env python3
"""L-RED (box 5): graded GAP-beta fitness (L-ALG GAP-C.md §6/§6a, Lead 02:01Z). Levels:
 (0) incomplete / wrong run, (3) duplicate-check hit, (2) orphan (carry/dupcheck.py, in process, LALG_DIR),
 (1) near-orphan whose last escape is removed at a threshold < pr(m) (L-ALG experiments/alg/dtl_nearorphan2.py, run
 unmodified in a subprocess from LALG2_DIR >= 1335713), plus the count of near-orphans as a gradient.
Order from DTL_ORDER. Usage: gapb.py G.pg ..."""
import sys, os, subprocess, re, ast
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dupcheck

def near(path):
    ld = os.environ.get("LALG2_DIR", os.environ["LALG_DIR"])
    r = subprocess.run([sys.executable, os.path.join(ld, "experiments", "alg", "dtl_nearorphan2.py"), os.path.abspath(path)],
                       capture_output=True, text=True, timeout=180, cwd=os.path.join(ld, "experiments", "alg"))
    low = tot = 0
    for line in r.stdout.splitlines():
        m = re.match(r"^(\d+) (\(.*\))$", line.strip())
        if not m: continue
        k = int(m.group(1)); t = ast.literal_eval(m.group(2)); tot += k
        if "threshold < pr(m)" in t: low += k
    return low, tot

def measure(path):
    m = dupcheck.measure(path); low, tot = near(path); m.update(near_low=low, near=tot); return m

def score(path):
    m = measure(path)
    return (10 ** 10 * (m["unsolved"] + m["wrong"]) + 10 ** 9 * m["dupW"] + 10 ** 8 * min(m["orphW"], 9)
            + 10 ** 7 * m["barren"] + 10 ** 6 * m["dup"] + 10 ** 5 * min(m["orphans"], 9)
            + 10 ** 4 * min(m["near_low"], 9) + 10 * min(m["near"], 500) + m["searches"])

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        print(os.path.basename(f), os.environ.get("DTL_ORDER", "stable"), measure(f))
