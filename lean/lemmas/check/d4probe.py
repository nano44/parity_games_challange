#!/usr/bin/env python3
"""D4 probe (L-FORMAL successor 4; Lead 02:06Z): can si.py's `par[x] is not v` (experiments/si/si.py l. 193, the walk of
FIX 2's cycle-node choice) be True for a value EQUAL to v, i.e. an int object equal to v but not identical to it?

Method: run the fleet's own N5 trace (box190/n5v.py step, mode "spec") on the given instances with a line tracer
(sys.settrace, si.py NOT modified) attached to every frame of Engine.evaluate; at each execution of l. 193 read the
frame's locals par, x, v and count
  walks      executions of l. 193
  big        those with v > 256 (outside CPython's small-int cache)
  eq_not_id  par[x] == v but par[x] is not v   (the defect case: the loop would walk past v's child)
  eq_id      par[x] == v and par[x] is v       (the normal stop)
Also probes, at l. 184 (`par = {v: None}`), whether v comes from `sorted(range(n), …)` (a fresh int object per vertex).
Usage: python3 -I lean/lemmas/check/d4probe.py FILE.pg|GENOME.json ... (json: Gamma3 via box189 gamma3.build)
env: D4_CAP (iterations per instance, default 30)."""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box190", "experiments/new/box21", "experiments/new",
                                                 "experiments/si", "experiments/harness", "experiments/new/box189")]
import n5x   # noqa: E402
import n5v   # noqa: E402
import si    # noqa: E402
from si import Engine   # noqa: E402

CAP = int(os.environ.get("D4_CAP", "30"))
SI_FILE = os.path.abspath(si.__file__)
LINE_WALK, LINE_PAR = 193, 184
assert open(SI_FILE).read().split("\n")[LINE_WALK - 1].strip().startswith("while par[x] is not v")
cnt = dict(walks=0, big=0, eq_not_id=0, eq_id=0, v_big_cycle_nodes=0)
examples = []


def local_tracer(frame, event, arg):
    if event == "line" and os.path.abspath(frame.f_code.co_filename) == SI_FILE:   # n5.py imports si via experiments/new/../si
        if frame.f_lineno == LINE_WALK:
            L = frame.f_locals
            par, x, v = L["par"], L["x"], L["v"]
            p = par[x]
            cnt["walks"] += 1
            if v > 256:
                cnt["big"] += 1
            if p is not None and p == v:
                if p is v:
                    cnt["eq_id"] += 1
                else:
                    cnt["eq_not_id"] += 1
                    if len(examples) < 5:
                        examples.append((v, x, id(p), id(v)))
        elif frame.f_lineno == LINE_PAR and frame.f_locals["v"] > 256:
            cnt["v_big_cycle_nodes"] += 1
    return local_tracer


def global_tracer(frame, event, arg):
    if event == "call" and frame.f_code is Engine.evaluate.__code__:
        return local_tracer
    return None


def load(path):
    if path.endswith(".json"):
        import gamma3
        G = json.load(open(path))
        gm, sig, tau, _ = gamma3.build(G, {"K", "pe", "pb", "m"})
        start = ({v: sig[v] for v in range(gm.n) if gm.owner[v] == 0}, {v: tau[v] for v in range(gm.n) if gm.owner[v] == 1})
        return gm, start
    g = n5x.load(path)
    sp = path[:-3] + ".start"
    return g, (n5x.readstart(sp) if os.path.exists(sp) else None)


for path in sys.argv[1:]:
    g, start = load(path)
    before = dict(cnt)
    E, Ed = Engine(g), Engine(n5x.dual(g))
    sigma, tau = n5x.start_pair(g, E, Ed, start)
    sys.settrace(global_tracer)
    it = 0
    try:
        while it < CAP:
            r = n5v.step(g, E, Ed, sigma, tau, "spec")
            if r is None:
                break
            sigma, tau = list(r[0]), list(r[1])
            it += 1
    finally:
        sys.settrace(None)
    print("%s n=%d iterations=%d %s" % (os.path.basename(path), g.n, it,
          " ".join("%s=%d" % (k, cnt[k] - before[k]) for k in cnt)), flush=True)
print("TOTAL " + " ".join("%s=%d" % kv for kv in cnt.items()))
print("EXAMPLES (v, x, id(par[x]), id(v)) of eq_not_id: %s" % examples)
# the construction, probed directly: v comes from sorted(range(n), key=...): distinct objects per vertex for n > 256
vs = sorted(range(600), key=lambda x: x)
print("identity probe: the object v=300 from sorted(range(600)) is the object 300 of a separate int(\"300\"):",
      vs[300] is int("300"))
