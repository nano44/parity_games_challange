#!/usr/bin/env python3
"""L-RED successor 30: (FO*) under the MIXED frame. CDAG_n (as sf/cdmask.py) with TWO-LEVEL Odd gates on edges x -> u:
o -> {u, b}; b -> p (Odd) -> {z, q}; q -> z2. b, q get random priorities (odd or even, between levels or below the sink), z, z2
random reader targets in {sink, 1..n}. Start sigma_0 = every CDAG vertex -> sink, tau_0 = RANDOM over Odd vertices (not tau*).
Measures, per sampled game: the longest tau-stretch (sigma-changes between consecutive tau-changes; n5b SPEC trace).
Gate vertices are Odd and CDAG vertices are the only Even choices, so a stretch counts CDAG switches only.
Usage: mixgate.py n samples seed"""
import sys, os, random
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, R + "/experiments/n5-second"); sys.path.insert(0, R + "/experiments/hard-families"); sys.path.insert(0, R + "/experiments/harness")
import n5b

class G: pass

def build(n, cfg):
    prio = [2] + [4 * (n + 1 - v) + 2 for v in range(1, n + 1)]; own = [0] * (n + 1); succ = [[0]] + [[] for _ in range(n)]
    for v in range(1, n + 1):
        succ[v].append(0)
        for u in range(1, v):
            c = cfg.get((v, u))
            if c is None: succ[v].append(u); continue
            bp, z, qp, z2 = c; o = len(prio); b, p, q = o + 1, o + 2, o + 3
            prio += [0, bp, 0, qp]; own += [1, 1, 1, 1]; succ += [[u, b], [p], [z, q], [z2]]; succ[v].append(o)
    g = G(); g.n = len(prio); g.prio = prio; g.owner = own; g.succ = succ
    g.pred = [[] for _ in range(g.n)]
    for v in range(g.n):
        for w in succ[v]: g.pred[w].append(v)
    return g

def dump(g):
    return "parity %d;\n" % (g.n - 1) + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n))

def stretch(tr):
    best = cur = 0
    for (a, b), (c, d) in zip(tr, tr[1:]):
        if b != d: cur = 0
        if a != c: cur += 1; best = max(best, cur)
    return best

if __name__ == "__main__":
    n, N, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); rnd = random.Random(seed)
    edges = [(v, u) for v in range(2, n + 1) for u in range(1, v)]
    prios = list(range(1, 4 * n + 8))
    hist = {}; best = None
    for _ in range(N):
        cfg = {}
        for e in edges:
            if rnd.random() < 0.85:
                cfg[e] = (rnd.choice(prios), rnd.randrange(0, n + 1), rnd.choice(prios), rnd.randrange(0, n + 1))
        g = build(n, cfg)
        sig0 = [0 if v <= n else -1 for v in range(g.n)]
        tau0 = [rnd.choice(g.succ[v]) if g.owner[v] == 1 else -1 for v in range(g.n)]
        tr = []
        try:
            win, strat, it, fb = n5b.N5(g, mode="spec").run(sigma=sig0, tau=tau0, trace=tr)
        except Exception as ex:
            continue
        s = stretch(tr); hist[s] = hist.get(s, 0) + 1
        if best is None or s > best[0]: best = (s, it, fb, cfg, tau0)
    print("hist", dict(sorted(hist.items())))
    print("best stretch", best[0], "iterations", best[1], "fb", best[2])
    print("cfg", best[3]); print("tau0", best[4])
    g = build(n, best[3]); open(os.path.join(os.environ.get("TMPDIR", "/tmp"), f"mixgate_best_n{n}_s{seed}.pg"), "w").write(dump(g))
