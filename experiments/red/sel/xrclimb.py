#!/usr/bin/env python3
"""L-RED successor 23: hill climb for super-linear XR (docs/si/N5-ALT-box23.md §6 item 1, CONJECTURE XR-LIN) at k = 1 (exactly one Odd
vertex of out-degree >= 2), S3 start. Fitness = max over vertices z and phases P of XR_P(z); a phase = maximal stretch with tau and both
cycle-node maps (Xi_sigma, Xi_tau) constant. Mutations: L-NEW's experiments/new/box21/climb_fix.py mutate (read-only).
Usage: xrclimb.py SEED.pg|RAND1SINK N seed secs OUT.pg [--clone] [--sw: fitness SW*1000 + PL (phsw.py)] [--pl: fitness PL*1000 + fallbacks in that phase] [--kmax K] [--start FILE: fixed start pair, invalid entries fall back to S3]   (pads SEED to N vertices with random Even vertices; writes the best game to OUT.pg)"""
import sys, os, time, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "..", "..")
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
import trace as T
from climb_fix import mutate

SWFIT = "--sw" in sys.argv
PLFIT = "--pl" in sys.argv
START = T.readstart(sys.argv[sys.argv.index("--start") + 1]) if "--start" in sys.argv else None
def vstart(G):
    if START is None: return ({}, {})
    return tuple({v: w for v, w in d.items() if v < len(G[2]) and w in G[2][v] and G[1][v] == o} for d, o in zip(START, (0, 1)))
KMAX = int(sys.argv[sys.argv.index("--kmax") + 1]) if "--kmax" in sys.argv else 1
def xrfit(G, cap=4000):
    prio, owner, succ = G; n = len(prio)
    if any(not s for s in succ): return -1
    kk = sum(1 for v in range(n) if owner[v] == 1 and len(set(succ[v])) > 1)
    if kk < 1 or kk > KMAX: return -1
    if PLFIT:
        import phsw
        g = T.pg.Game(list(prio), list(owner), [sorted(set(s)) for s in succ])
        try: PL, FB = phsw.plfb(g, vstart(G), cap=cap)
        except Exception: return -1
        return PL * 1000 + FB
    if SWFIT:
        import phsw
        g = T.pg.Game(list(prio), list(owner), [sorted(set(s)) for s in succ])
        try: PL, SW, arg, it = phsw.measure(g, vstart(G), cap=cap)
        except Exception: return -1
        return SW * 1000 + PL
    g = T.pg.Game(list(prio), list(owner), [sorted(set(s)) for s in succ])
    states = []
    try: T.run(g, vstart(G), cap=cap, log=lambda *a: None, states=states)
    except Exception: return -1
    E, Ed = T.Engine(g), T.Engine(T.dual(g))
    vals = []; lam = []
    for s, t in states:
        v = E.evaluate(s)[0]; vt = Ed.evaluate(t)[0]
        vals.append(v); lam.append((t, tuple(x[0] for x in v), tuple(x[0] for x in vt)))
    best = 0; a = 0
    for k in range(1, len(states) + 1):
        if k == len(states) or lam[k] != lam[k - 1]:
            for z in range(n):
                best = max(best, sum(1 for t in range(a, k - 1) if vals[t][z] != vals[t + 1][z]))
            a = k
    return best

CLONE = "--clone" in sys.argv
def clone(rng, G, n0):
    """Copy a core vertex (owner, priority +- 0..2, successors) into an inert padding slot (self-loop only) and redirect one in-edge."""
    prio, owner, succ = [list(G[0]), list(G[1]), [list(s) for s in G[2]]]; n = len(prio)
    free = [p for p in range(n0, n) if succ[p] == [p]]
    if not free: return [prio, owner, succ]
    p = rng.choice(free); v = rng.randrange(n0)
    owner[p] = owner[v]; prio[p] = max(0, prio[v] + rng.choice((-2, -1, 0, 1, 2))); succ[p] = list(succ[v])
    preds = [u for u in range(n) if v in succ[u] and u != p]
    if preds:
        u = rng.choice(preds)
        if rng.random() < 0.5: succ[u] = sorted(set(succ[u]) - {v} | {p})
        else: succ[u] = sorted(set(succ[u]) | {p})
    return [prio, owner, succ]

def load(path):
    g = T.pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
    return [list(g.prio), list(g.owner), [list(s) for s in g.succ]]

def save(G, path):
    prio, owner, succ = G
    with open(path, "w") as f:
        f.write("parity %d;\n" % (len(prio) - 1))
        for v in range(len(prio)): f.write("%d %d %d %s;\n" % (v, prio[v], owner[v], ",".join(map(str, sorted(set(succ[v]))))))

def main():
    seedp, N, seed, secs, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
    rng = random.Random(seed)
    if seedp == "RAND1SINK":
        import gen1sink
        best0 = None
        for _ in range(200):   # best of 200 random 1-sink games as the start
            H = gen1sink.gen(N, rng); f = xrfit(H)
            if best0 is None or f > best0[0]: best0 = (f, H)
        G = best0[1]
    else: G = load(seedp)
    n0 = len(G[0])
    for v in range(n0, N):   # inert padding: isolated Even self-loops; the climb wires them in
        G[0].append(rng.randrange(N + 3)); G[1].append(0); G[2].append([v])
    f = xrfit(G); best = (f, G); t0 = time.time(); it = 0
    print("start fit", f, "n", N, flush=True)
    while time.time() - t0 < secs:
        it += 1
        H = clone(rng, best[1], n0) if (CLONE and rng.random() < 0.15) else mutate(rng, best[1])
        fh = xrfit(H)
        if fh >= best[0]:
            if fh > best[0]: print("%.0fs it %d fit %d (%.2fn)" % (time.time() - t0, it, fh, (fh % 1000 if SWFIT else (fh // 1000 if PLFIT else fh)) / N), flush=True); save(H, out)
            best = (fh, H)
    save(best[1], out); print("END fit", best[0], "n", N, "iters", it, flush=True)

if __name__ == "__main__":
    main()
