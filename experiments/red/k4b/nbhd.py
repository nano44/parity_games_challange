#!/usr/bin/env python3
"""L-RED box 6 (produced on Opus 5.5): exhaustive one-step neighbourhood of a game (delete an edge, add an edge, change a
priority, flip an owner), scored with carry/klow.py in both orders; prints hits ((K-in) violation or incomplete run) and
the 10 best neighbours by (kin, -minprod, dupmin, eaten). With STEPS=k, repeats steepest ascent k times from the best neighbour (ties: first; visited games skipped).
Usage: nbhd.py G.pg OUTDIR"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "carry"))
import klow, pg
G0 = pg.read(sys.argv[1]); out = sys.argv[2]; os.makedirs(out, exist_ok=True); seen = set()
def variants(g0):
    n = g0.n; mp = max(g0.prio) + 2
    for v in range(n):
        for w in g0.succ[v]:
            if len(g0.succ[v]) > 1: yield f"del{v}-{w}", g0.prio, g0.owner, [[x for x in s if not (u == v and x == w)] for u, s in enumerate(g0.succ)]
        for w in range(n):
            if w not in g0.succ[v]: yield f"add{v}-{w}", g0.prio, g0.owner, [sorted(s + [w]) if u == v else s for u, s in enumerate(g0.succ)]
        for q in range(mp + 1):
            if q != g0.prio[v]: yield f"pr{v}={q}", [q if u == v else x for u, x in enumerate(g0.prio)], g0.owner, g0.succ
        yield f"own{v}", g0.prio, [1 - x if u == v else x for u, x in enumerate(g0.owner)], g0.succ
def step(g0, depth):
  res = []
  for tag, pr, ow, su in variants(g0):
    g = pg.Game(pr, ow, su); h = pg.dumps(g)
    if h in seen: continue
    seen.add(h)
    for order in ("oink", "stable"):
        m = klow.measure_game(g, order)
        if m["wsearch"] == 0: continue
        key = (m["incomplete"], m["kin"], -m["minprod"], m["dupmin"], m["eaten"]); res.append((key, tag, order, h))
        if m["incomplete"] or m["kin"]:
            fn = os.path.join(out, f"nb_d{depth}_{tag}_{order}.pg"); open(fn, "w").write(h); print("HIT", tag, order, m, fn, flush=True)
  res.sort(key=lambda r: r[0], reverse=True); print("depth", depth, len(res), "scored; best", [r[:3] for r in res[:3]], flush=True)
  return res
g = G0
for depth in range(int(os.environ.get("STEPS", "1"))):
    r = step(g, depth)
    if not r: break
    open(os.path.join(out, f"best_d{depth}.pg"), "w").write(r[0][3]); g = pg.parse(r[0][3])
