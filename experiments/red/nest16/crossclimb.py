"""L-RED box 17 (produced on Opus 5.5): restricted climb modelled on the minimal 5 -> 6 step (R50 §4). Moves are only:
(a) add one edge from a C-vertex of one part to a vertex of ANOTHER part; (b) move one vertex's priority rank by up to +-40 (parity kept).
Parts are vertex ranges given by CUTS. Score starclimb.score (FIT honoured). Accept >=.
Usage: DTL_ORDER=.. CUTS=49,75 crossclimb.py START.pg STEPS SEED OUTDIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "xctx"))
sys.setrecursionlimit(100000)
import xscore as X, starclimb as SC


def reprio(g, order):
    prio = [0] * g.n; last = -1
    for v in order:
        p = last + 1
        if p % 2 != g.prio[v] % 2: p += 1
        prio[v] = p; last = p
    return prio


def move(g, C, cuts, rnd):
    part = lambda v: sum(1 for c in cuts if v >= c)
    succ = [list(s) for s in g.succ]; prio = list(g.prio)
    if rnd.random() < 0.6:
        cs = [v for v in range(g.n) if g.owner[v] == C]
        v = rnd.choice(cs); others = [w for w in range(g.n) if part(w) != part(v) and w not in succ[v]]
        if not others: return None
        succ[v] = sorted(succ[v] + [rnd.choice(others)])
    else:
        order = sorted(range(g.n), key=lambda v: g.prio[v]); v = rnd.randrange(g.n); i = order.index(v); order.pop(i)
        order.insert(max(0, min(len(order), i + rnd.randint(-40, 40))), v); prio = reprio(g, order)
    h = X.pg.Game(prio, list(g.owner), succ)
    return h if X.inclass(h, C) else None


if __name__ == "__main__":
    order = os.environ.get("DTL_ORDER", "stable"); cuts = [int(x) for x in os.environ.get("CUTS", "").split(",") if x]
    start, steps, seed, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rnd = random.Random(seed); g = X.distinct(X.pg.read(start)); C = X.controller(g); os.makedirs(out, exist_ok=True)
    sg = SC.score(g, order, C); print("start", sg, flush=True)
    for it in range(steps):
        h = move(g, C, cuts, rnd)
        if h is None: continue
        try:
            sh = SC.score(h, order, C)
        except RecursionError:
            continue
        if sh >= sg:
            if sh > sg: print(it, sh, flush=True); X.pg.write(h, os.path.join(out, f"cross_s{seed}_{it}_{sh[0]}.pg"))
            g, sg = h, sh
        if it % 50 == 0: print("hb", it, sg, flush=True)
    print("final", sg)
