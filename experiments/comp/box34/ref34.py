#!/usr/bin/env python3
"""L-COMP box 34: REFERENCE side of the cross-check = L-NEW's asc197.run, imported read-only from the checkout in env LNEW
(b61c2029 = BOX 33's engine, maxalt 0 for a one-letter tops sequence; f98e93ee = Add. 3 fixed counter). --noelev: the same one-line
gamma3 patch as box33/enum33.py (e-priorities by gate only). Also --game: dump gamma3.build's game (prio, owner, succ) for the
game-level comparison with own34.build. Reads genomes as JSON lines on stdin, writes one JSON line per genome."""
import sys, os, json, types
LNEW = os.environ['LNEW']; NOELEV = '--noelev' in sys.argv; GAME = '--game' in sys.argv
sys.path[:0] = [os.path.join(LNEW, p) for p in ("experiments/new/box197", "experiments/new/box196", "experiments/new/box195", "experiments/new/box191",
                "experiments/new/box189", "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
os.environ["ROOT"] = LNEW; os.environ["Q196_ROOT"] = LNEW; os.environ["EG195_ROOT"] = LNEW
if NOELEV:
    src = open(os.path.join(LNEW, "experiments/new/box189/gamma3.py")).read()
    old = 'sorted(O, key=lambda q: (lev[q[0]], gate[q[0]][q[1]]))): prio[V[("e", q)]]'
    assert src.count(old) == 1, 'gamma3 e-priority line not found'
    src = src.replace(old, 'sorted(O, key=lambda q: gate[q[0]][q[1]])): prio[V[("e", q)]]')
    mod = types.ModuleType("gamma3"); mod.__file__ = os.path.join(LNEW, "experiments/new/box189/gamma3.py")
    exec(compile(src, mod.__file__, "exec"), mod.__dict__); sys.modules["gamma3"] = mod
import asc197, gamma3, eg195
for line in sys.stdin:
    G = json.loads(line)
    if GAME:
        g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0)
        print(json.dumps({"prio": g.prio, "owner": g.owner, "succ": [sorted(s) for s in g.succ]}), flush=True); continue
    try:
        r = asc197.run(G); print(json.dumps({"T3": r["T3"], "maxalt": r.get("maxalt", 0)}), flush=True)
    except Exception as e:
        print(json.dumps({"err": repr(e)[:200]}), flush=True)
