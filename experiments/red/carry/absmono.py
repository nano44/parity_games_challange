#!/usr/bin/env python3
"""L-RED (box 5): attack on L-ALG's (ABS-mono) (GAP-A-M §21j): PHI0 (sum of depth-0 removal indices) never RISES at a
transition whose first piece-level difference is not a RES at a depth-0 piece. Runs L-ALG's experiments/alg/dtl_dvctx.py
with DVC_PHI=1 (read-only; LALG_DIR >= 57e2256) in the order DTL_ORDER and parses its class table.
score = 1000 x violating transitions + non-RES-d0 transitions + (RES-d0 PHI0 rises)/10. Usage: absmono.py G.pg ..."""
import sys, os, subprocess, re, ast

def measure(path):
    ld = os.environ["LALG_DIR"]; env = dict(os.environ, DVC_PHI="1")
    r = subprocess.run([sys.executable, os.path.join(ld, "experiments", "alg", "dtl_dvctx.py"), os.path.abspath(path)],
                       capture_output=True, text=True, timeout=180, cwd=os.path.join(ld, "experiments", "alg"), env=env)
    viol = other = resrise = 0; seen = False
    for line in r.stdout.splitlines():
        m = re.match(r"^(\d+) (\(.*\))$", line.strip())
        if not m: continue
        seen = True; k = int(m.group(1)); t = ast.literal_eval(m.group(2))
        rises = t[-1] == "PHI0 RISES"; res0 = t[0] == "RES" and t[1] == "d0"
        if res0: resrise += k * rises
        else:
            other += k; viol += k * rises
    if not seen and r.returncode != 0: raise RuntimeError(r.stderr[-300:])
    return viol, other, resrise

def score(path):
    v, o, rr = measure(path)
    return 1000 * v + o + rr / 10.0

if __name__ == "__main__":
    for f in sys.argv[1:]:
        v, o, rr = measure(f); print(f"{os.path.basename(f)} order={os.environ.get('DTL_ORDER', 'stable')} ABS-mono violations {v} of {o} non-RES-d0 transitions; RES-d0 PHI0 rises {rr}")
