#!/usr/bin/env python3
"""L-RED box 6 (produced on Opus 5.5): (YZ) target (Lead 08:49Z; l-alg ced9921): a P piece with Y_0 ⊋ Z_f, i.e. Dom(prevV)
fires a stored tangle using a vertex of old X / an earlier top's part AND takes vertices the final region loop misses.
Runs two L-ALG tools UNMODIFIED in subprocesses (LALG10_DIR >= ced9921): dtl_ntf.py (Dom straddle firings; NT-f final-round
acceptances) and, through carry/yzwm.py, dtl_pnl.py (YZ / FM / WM / P-KT failures).
Score: 1e11 (yzwm bad + NT-f final-round acceptances) + 1e9 min(Dom straddle firings, 9) + 1e7 min(Dom firings, 9)
+ yzwm score below 1e11. Order from DTL_ORDER. Usage: yzs.py G.pg ..."""
import sys, os, re, ast, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def measure(path):
    ld = os.path.join(os.environ["LALG10_DIR"], "experiments", "alg")
    r = subprocess.run([sys.executable, os.path.join(ld, "dtl_ntf.py"), os.path.abspath(path)], capture_output=True, text=True, timeout=300, cwd=ld)
    if r.returncode != 0: raise RuntimeError(r.stderr[-300:])
    tab = ast.literal_eval(r.stdout.strip().splitlines()[-1])
    m = dict(strad=0, fire=0, final=0)
    for k, v in tab.items():
        if k.startswith("Dom(prevV) at a P piece fires a tangle"):
            m["fire"] += v
            if "straddle" in k: m["strad"] += v
        if k.startswith("-1 call:") and "final round" in k and "attract no tangle" not in k: m["final"] += v
    os.environ.setdefault("LALG8_DIR", os.environ["LALG10_DIR"]); import yzwm
    m.update(yzwm.measure(path)); return m

def score(path):
    m = measure(path)
    return (10 ** 11 * (m["bad"] + m["final"]) + 10 ** 9 * min(m["strad"], 9) + 10 ** 7 * min(m["fire"], 9)
            + 10 ** 6 * min(m["monoP"], 9) + min(m["P"], 999))

if __name__ == "__main__":
    for f in sys.argv[1:]:
        print(os.path.basename(f), os.environ.get("DTL_ORDER", "stable"), measure(f))
