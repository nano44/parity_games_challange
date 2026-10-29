#!/usr/bin/env python3
"""L-RED successor 29: (FO*) probe. CDAG_n (L-NEW box 8) with Odd masks o_(x,u) on edges x -> u (u >= 1): o -> {u, b}, b (odd prio) -> z.
Priorities: sink 2 (self-loop), CDAG v: 4(n+1-v)+2, masks 0 (below the cycle: ignored but for length), b odd in between levels.
N5 (n5b SPEC) from sigma_0 = all CDAG -> sink, tau_0 = tau* (final tau of an S3 run). Enumerates reader configs; prints the best.
Usage: cdmask.py n [maxprint]"""
import sys, itertools, os
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, R + "/experiments/n5-second"); sys.path.insert(0, R + "/experiments/hard-families"); sys.path.insert(0, R + "/experiments/harness")
import n5b, pg

class G: pass

def build(n, cfg):
    # vertices: 0 sink, 1..n CDAG, then per masked edge: o, b
    prio = [2] + [4 * (n + 1 - v) + 2 for v in range(1, n + 1)]; own = [0] * (n + 1); succ = [[0]] + [[] for _ in range(n)]
    for v in range(1, n + 1):
        succ[v].append(0)
        for u in range(1, v):
            c = cfg.get((v, u))
            if c is None: succ[v].append(u); continue
            z, bp = c; o = len(prio); b = o + 1
            prio += [0, bp]; own += [1, 1]; succ += [[u, b], [z]]; succ[v].append(o)
    g = G(); g.n = len(prio); g.prio = prio; g.owner = own; g.succ = succ
    g.pred = [[] for _ in range(g.n)]
    for v in range(g.n):
        for w in succ[v]: g.pred[w].append(v)
    return g

def dump(g):
    return "parity %d;\n" % (g.n - 1) + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n))

def run(g, n):
    s = n5b.N5(g, mode="spec")
    win, strat, it, fb = s.run()
    if any(win[v] != 0 for v in range(n + 1)): return None
    # tau*: Odd's optimal = strat on Odd vertices? Odd vertices lie in Even's region: use final tau via a traced run
    tr = []; s.run(trace=tr); taus = list(tr[-1][1])
    sig0 = [0 if (1 <= v <= n or v == 0) else -1 for v in range(g.n)]
    try:
        _, _, it2, fb2 = n5b.N5(g, mode="spec").run(sigma=sig0, tau=taus)
    except Exception as e:
        return None
    return it2, fb2, it

if __name__ == "__main__":
    n = int(sys.argv[1]); edges = [(v, u) for v in range(2, n + 1) for u in range(1, v)]
    bps = [p for p in range(5, 4 * n + 7, 2)]
    opts = [None] + [(z, bp) for z in range(0, n + 1) for bp in bps]
    best = []
    for combo in itertools.product(opts, repeat=len(edges)):
        cfg = {e: c for e, c in zip(edges, combo) if c is not None}
        g = build(n, cfg); r = run(g, n)
        if r is None: continue
        best.append((r[0], r[1], r[2], cfg))
    best.sort(key=lambda t: -t[0])
    for t in best[: int(sys.argv[2]) if len(sys.argv) > 2 else 5]: print(t)
    print("configs", len(best))
