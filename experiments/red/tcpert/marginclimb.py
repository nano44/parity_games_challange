#!/usr/bin/env python3
"""L-RED box 13 (produced on Opus 5.5): two-player hill climb against (VR-NEW_all) = key K-v-all, using L-ALG's
b12_pot.vr_score UNMODIFIED (imported from LALG_DIR; MARGIN=1): score (violations, -(fewest vertices supplying a new key at one
chain-changing transition), chain-changing transitions, searches) in the order DTL_ORDER; a candidate also needs >= 1
chain-changing transition. Mutations: add / remove an edge (keep one successor), flip an owner, shift a priority by +-1/+-2.
Every accepted game verifies on pinned Oink. A violation is saved as KILL_*.pg. MC_TIGHT=1: score (violations, -min margin, #transitions with margin <= 1, chain-changing).
Usage: marginclimb.py SEED.pg RNGSEED STEPS OUTDIR"""
import sys, os, random
os.environ["MARGIN"] = "1"
H = os.path.dirname(os.path.abspath(__file__)); A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg")
sys.path.insert(0, H); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
import tcpert as T, pg, b12_pot as B
sys.setrecursionlimit(100000)
seedf, rs, steps, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(rs); os.makedirs(out, exist_ok=True)
order = os.environ.get("DTL_ORDER", "stable"); tmp = os.path.join(out, f"m{rs}.pg"); g0 = pg.read(seedf)
def tight(g):
    """vr_score's own loop over b12_pot.run/chain/keys/sig (unmodified), counting the margin of EVERY chain-changing transition:
    returns (violations, -min margin, #transitions with margin <= 1, chain-changing transitions)."""
    d = B.run(g, order); viol = changing = t1 = 0; seen = None; prev = None; marg = g.n + 1
    for ph, calls in getattr(d, "log", []):
        ch = B.chain(calls, g.n); k = B.keys(ch)["K-v-all"]
        if prev is not None and prev[0] == ph and B.sig(ch) != prev[1]:
            changing += 1; m = len({x[0] for x in k - seen}); marg = min(marg, m); t1 += m <= 1
            if not (k - seen): viol += 1
        if prev is None or prev[0] != ph: seen = set()
        seen |= k; prev = (ph, B.sig(ch))
    return (viol, -marg, t1, changing)
def fit(pr, ow, su):
    g = pg.Game(pr, ow, su)
    try: sc = tight(g) if os.environ.get("MC_TIGHT") == "1" else B.vr_score(g, order, "K-v-all")
    except RecursionError: return (-9,)
    if sc[-1 if os.environ.get("MC_TIGHT") == "1" else 2] < 1: return (-9,)
    return sc
pr, ow, su = list(g0.prio), list(g0.owner), [list(s) for s in g0.succ]; n = len(pr); f = fit(pr, ow, su); best = f; print("start", f, flush=True)
for it in range(steps):
    p2, o2, s2 = list(pr), list(ow), [list(s) for s in su]; v = rng.randrange(n); k = rng.randrange(4)
    if k == 0: s2[v] = sorted(set(s2[v] + [rng.randrange(n)]))
    elif k == 1 and len(s2[v]) > 1: s2[v].remove(rng.choice(s2[v]))
    elif k == 2: o2[v] ^= 1
    else: p2[v] = max(0, p2[v] + rng.choice([-2, -1, 1, 2]))
    g = fit(p2, o2, s2)
    if g >= f:
        V = [[p2[i], o2[i], s2[i], str(i)] for i in range(n)]; r = T.solve(V, tmp)
        if not r[1]: print("NOT VERIFIED", r, flush=True); continue
        pr, ow, su, f = p2, o2, s2, g
        if f > best:
            best = f; print(it, f, flush=True); pg.write(pg.Game(pr, ow, su), os.path.join(out, f"best_r{rs}.pg"))
            if f[0] > 0: pg.write(pg.Game(pr, ow, su), os.path.join(out, f"KILL_r{rs}_it{it}.pg")); print("KILL K-v-all", flush=True)
print("done best", best)
