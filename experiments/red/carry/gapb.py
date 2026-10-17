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

def loww(path):
    """L-ALG's dtl_loww.py (unmodified, subprocess, LALG3_DIR >= cf68c58): count of 'LOW-W VIOLATION'."""
    ld = os.environ.get("LALG3_DIR")
    if not ld: return 0
    r = subprocess.run([sys.executable, os.path.join(ld, "experiments", "alg", "dtl_loww.py"), os.path.abspath(path)],
                       capture_output=True, text=True, timeout=180, cwd=os.path.join(ld, "experiments", "alg"))
    m = re.search(r"'LOW-W VIOLATION': (\d+)", r.stdout)
    if not m: raise RuntimeError(r.stdout[-300:] + r.stderr[-300:])
    return int(m.group(1))

def kfirst(path):
    """L-ALG's dtl_whichpiece.py (unmodified, subprocess, LALG4_DIR >= 704f8dc): (K-first) failures = searches - FIRST."""
    ld = os.environ.get("LALG4_DIR")
    if not ld: return 0
    r = subprocess.run([sys.executable, os.path.join(ld, "experiments", "alg", "dtl_whichpiece.py"), os.path.abspath(path)],
                       capture_output=True, text=True, timeout=180, cwd=os.path.join(ld, "experiments", "alg"))
    m = re.search(r"\{'searches': (\d+),.*?'FIRST': (\d+)", r.stdout)
    if not m: raise RuntimeError(r.stdout[-300:] + r.stderr[-300:])
    return int(m.group(1)) - int(m.group(2))

def k4b(path):
    """L-ALG's dtl_k4b.py (unmodified, subprocess, LALG5_DIR >= 31fdd98): table rows with 'REGIONS OUTSIDE' or V* outside."""
    ld = os.environ.get("LALG5_DIR")
    if not ld: return 0
    r = subprocess.run([sys.executable, os.path.join(ld, "experiments", "alg", "dtl_k4b.py"), os.path.abspath(path)],
                       capture_output=True, text=True, timeout=180, cwd=os.path.join(ld, "experiments", "alg"))
    bad = 0
    for line in r.stdout.splitlines():
        m = re.match(r"^(\d+) \((.*)\)$", line.strip())
        if m and ("OUTSIDE" in m.group(2).upper() and "INSIDE" not in m.group(2).split(",")[-1].upper()): bad += int(m.group(1))
        elif m and "OUTSIDE" in m.group(2).upper(): bad += int(m.group(1))
    return bad

def measure(path):
    m = dupcheck.measure(path); m["kfirst"] = kfirst(path); m["k4b"] = k4b(path); low, tot = near(path); m.update(near_low=low, near=tot, loww=loww(path)); return m

def score(path):
    m = measure(path)
    return (10 ** 12 * (m["unsolved"] + m["wrong"]) + 10 ** 11 * m["kin_viol"] + 3 * 10 ** 10 * min(m["kfirst"], 3) + 2 * 10 ** 10 * min(m["k4b"], 3) + 10 ** 10 * min(m["loww"], 9) + 10 ** 9 * m["dupW"] + 10 ** 8 * m["tw_straddle"] + 10 ** 7 * min(m["orphW"], 9)
            + 10 ** 6 * m["barren"] + 10 ** 5 * m["dup"] + 10 ** 4 * min(m["orphans"], 9)
            + 10 ** 3 * min(m["near_low"], 9) + 10 * min(m["near"], 500) + m["searches"])

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        print(os.path.basename(f), os.environ.get("DTL_ORDER", "stable"), measure(f))
