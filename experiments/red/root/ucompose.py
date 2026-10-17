#!/usr/bin/env python3
"""L-RED box 7 (produced on Opus 5.5), target (A) (FALL, GAP-A-M §22l): stack several gadgets (each part's priorities
shifted by an EVEN amount above the previous part, so parities and in-part order are kept), add c random cross edges
(c = 0..CMAX; R19 showed plain unions stay at <= 2 descents because each part's dominion ends the phase), and score with
root/rootfit.py (L-ALG dtl_rootmono.py unmodified, LALGR_DIR; mode from ROOTFIT, default fall). Keeps every union whose
score's leading measure exceeds BASE. CHAIN=1 replaces the random cross edges by the fall3_n76 pattern: for every pair
of consecutive parts in the stack, one edge from a random Even-owned vertex of the upper part to a random Even-owned
vertex of the part below (plus 0..CMAX random edges of the same kind). K=k draws k DISTINCT parts from the given pool
for each union (default: all of them). Usage: ucompose.py SEED COUNT ORDER CMAX BASE OUTDIR G1.pg G2.pg ..."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rootfit
sys.path.insert(0, os.path.join(os.environ["LALGR_DIR"], "experiments", "harness"))
import pg
seed, cnt, order, cmax, base, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
parts = [pg.read(f) for f in sys.argv[7:]]; rng = random.Random(seed); os.makedirs(out, exist_ok=True)
os.environ.setdefault("ROOTFIT", "fall"); lead = {"fall": "desc", "ctx": "ctx", "dirty": "maxdirty", "falls": "maxfalls"}[os.environ["ROOTFIT"]]
best = (-1, None)
for i in range(cnt):
    prio, own, succ, shift, offs = [], [], [], 0, []
    for h in rng.sample(parts, int(os.environ.get("K", len(parts)))):   # random choice and stacking order
        o = len(prio); offs.append((o, o + h.n)); prio += [p + shift for p in h.prio]; own += list(h.owner); succ += [[w + o for w in s] for s in h.succ]
        shift = max(prio) + 1 + (max(prio) + 1) % 2
    N = len(prio)
    if os.environ.get("CHAIN") == "1":
        ev = [[v for v in range(a, b) if own[v] == 0] for a, b in offs]
        pairs = [(j + 1, j) for j in range(len(offs) - 1)]
        pairs += [rng.choice(pairs) for _ in range(rng.randint(0, cmax))] if pairs else []
        for hi, lo in pairs:
            u = rng.choice(ev[hi]); w = rng.choice(ev[lo]); succ[u] = sorted(set(succ[u]) | {w})
    else:
        for _ in range(rng.randint(0, cmax)):
            u = rng.randrange(N); w = rng.randrange(N); succ[u] = sorted(set(succ[u]) | {w})
    fn = os.path.join(out, f"uc_{seed}_{i}.pg"); open(fn, "w").write(pg.dumps(pg.Game(prio, own, succ)))
    m = rootfit.measure(fn, order); v = m[lead]
    if m["hit"] or v > base: print("UNION", i, m, fn, flush=True)
    else: os.unlink(fn)
    if v > best[0]: best = (v, i)
    if i % 20 == 0: print("progress", i, "best", best, flush=True)
print("done", cnt, "best", best)
