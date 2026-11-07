"""REFEREE s23: run xinew_probe.py's R104-text simulator on lane genome JSONs (N, lev, opts[[wt,xt,m]], gate, br, bp, start).
Prints per file: N T (own run) XINEW violations, option-value monotonicity failures (ALL options), current-value failures.
Usage: python3 -I xinew_lane.py file.json ..."""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xinew_probe import run, check, xval, better
tot = dict(files=0, steps=0, viol=0, mono_all=0, norise=0)
for p in sys.argv[1:]:
    G = json.load(open(p)); N = G["N"]
    opts = [[[o[0] if o[0] >= 0 else None, o[1] if o[1] >= 0 else 'X', G["br"][o[2]], G["bp"][o[2]], G["gate"][x][k]]
             for k, o in enumerate(G["opts"][x])] for x in range(N)]
    states, As = run(G["lev"], opts, list(G["start"]), 0)
    v, m, r = check(G["lev"], opts, states, As)
    print(os.path.basename(p), "N", N, "T", len(states) - 1, "XINEW", len(v), "MONO_ALL", m, "NORISE", r)
    tot['files'] += 1; tot['steps'] += len(states) - 1; tot['viol'] += len(v); tot['mono_all'] += m; tot['norise'] += r
print("TOTAL", tot)
