"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5): is (DV-nofall) set algebra? van Dijk's distance values
(dtl_distval.distval, transcription of dtl.cpp computeDistanceValues) under ARBITRARY growing sets of GENUINE p-tangles
(dtl_gentangle.genuine), not DTL-learned ones. Part 1: box 4's synthetic counters (dtl_lexcounter, dtl_staterevisit gadgets).
Part 2: random games n <= DVS_N (re-indexed by priority, mkdtl; before 00:30Z 2026-10-17 they were NOT, which voided those runs), random genuine tangles added one at a time in random order; reports chains where some value
falls. Usage: dtl_dvsynth.py [games] [seed]  (DVS_V=1 prints the first falls)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_pyref as D, gen, pg
from dtl_gentangle import genuine
from dtl_distval import distval

def mkdtl(g):
    """DTL on g with vertices re-indexed in non-decreasing priority order (stable: (priority, id)), as the pseudocode
    requires (top-down = descending index = descending priority). Returns (d, idx) with idx[new] = original id."""
    idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); new = {v: i for i, v in enumerate(idx)}
    return D.DTL([g.prio[v] for v in idx], [g.owner[v] for v in idx], [sorted(new[w] for w in g.succ[v]) for v in idx]), idx

def setT(d, tl):
    d.tv = [t[0] for t in tl]; d.tout = [t[1] for t in tl]
    d.tpr = [max(d.pr[v] for v, _ in t[0]) for t in tl]; d.tin = [[] for _ in range(d.n)]
    for i, t in enumerate(tl):
        for e in t[1]: d.tin[e].append(i)

def dv(d, p, tl):
    setT(d, tl); G = set(range(d.n)); return distval(d, G, p)

def falls(a, b):
    return [v for v in a if b.get(v, 0) < a[v]]

def gadget(Gd, sets):
    names = sorted(Gd, key=lambda k: (Gd[k][0], list(Gd).index(k))); ix = {k: i for i, k in enumerate(names)}
    d = D.DTL([Gd[k][0] for k in names], [Gd[k][1] for k in names], [[ix[w] for w in Gd[k][2]] for k in names])
    tl = [genuine(d, 0, {ix[k] for k in S}, random.Random(0)) for S in sets]
    assert all(tl)
    vals = [dv(d, 0, tl[:i]) for i in range(len(tl) + 1)]
    return [(i, sorted(names[v] for v in falls(vals[i], vals[i + 1]))) for i in range(len(tl))], [{names[v]: x for v, x in vv.items()} for vv in vals]

if __name__ == "__main__":
    import dtl_lexcounter as LC, dtl_staterevisit as SR
    print("lexcounter {s} -> {s, sigma}:", gadget(LC.G, [("y1", "y2", "y3", "y4"), ("y1", "z")]))
    print("staterevisit {} -> {s} -> {s, sigma} -> {s, sigma, tau}:", gadget(SR.G, [("y1", "y2", "y3", "y4"), ("y1", "z"), ("y3", "y4")]))
    games = int(sys.argv[1]) if len(sys.argv) > 1 else 2000; seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    rnd = random.Random(seed); nmax = int(os.environ.get("DVS_N", "10")); chains = bad = steps = 0
    for gi in range(games):
        n = rnd.randint(4, nmax); g = gen.random_game(n, n, 1, 3, rnd.randrange(10 ** 9))
        d, _ = mkdtl(g); p = rnd.randrange(2)
        cands = []
        for _ in range(60):
            C = set(rnd.sample(range(n), rnd.randint(1, min(n, 5))))
            t = genuine(d, p, C, rnd)
            if t and t[1] and sorted(v for v, _ in t[0]) not in [sorted(v for v, _ in c[0]) for c in cands]: cands.append(t)
        if len(cands) < 2: continue
        rnd.shuffle(cands); chains += 1; prev = dv(d, p, [])
        for i in range(1, len(cands) + 1):
            cur = dv(d, p, cands[:i]); steps += 1
            if falls(prev, cur):
                bad += 1
                if os.environ.get("DVS_V") and bad <= 3:
                    print("FALL game", gi, "n", n, "p", p, "after adding tangle", i, "vertices", falls(prev, cur), "values", [(v, prev[v], cur[v]) for v in falls(prev, cur)])
                    print("  GAME (internal ids = priority order; original ids idx)", [(d.pr[v], d.ow[v], d.outs[v]) for v in range(d.n)])
                    print("  TANGLES (vertex, strategy) / escapes, in order:", [(c[0], c[1]) for c in cands[:i]], flush=True)
                break
            prev = cur
    print(f"random genuine chains: {chains} chains, {steps} additions, chains with a fall: {bad}")
