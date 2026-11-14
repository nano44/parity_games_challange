#!/usr/bin/env python3
"""Box 210 (L-NEW successor 72): which steps of GEN-LEVEL hold along the SIGMA-sequence of an N5 run (SPEC S1-S5; the loop is copied
from experiments/new/n5.py mode n5, engine experiments/si si.Engine) on split-form games. DATA for the remark in §8 of
docs/new/N5-GENLEVEL-box210.md; no statement about N5 is made. States = iterations (sigma may stay the same at an iteration).
Counters as gen210.py, reference b = the last state. Expected 0 (they do not depend on the switching rule): K1, K3, K4, L1, L3, L3m.
Expected to FIRE (S4a is not switch-best): K5, and with it L4, L4c, P3. Also printed: fallbacks (SPEC S4c).
Usage: n5lev210.py --pg FILE.pg ... (best-reward start pair, split game) | n5lev210.py SEED COUNT N0 D DEG EVTOP (random start pairs)"""
import sys, os, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gen210
ROOT = gen210.ROOT; sys.path[:0] = [os.path.join(ROOT, "experiments/new")]
import pg
from si import Engine
def dual(h): return pg.Game([p + 1 for p in h.prio], [1 - o for o in h.owner], [list(s) for s in h.succ])
def n5hist(g, sigma, tau, cap=5000):
    n = g.n; E, Ed = Engine(g), Engine(dual(g)); hist = []; fb = 0
    while len(hist) < cap:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        hist.append((list(sigma), vs, list(sbar)))
        if not Is and not It: break
        ns, nt = list(sigma), list(tau)
        if Is:
            opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
            for v, w in Is: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
            _, best = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ))).evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 0: ns[v] = best[v]
        if It:
            opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
            for v, w in It: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
            _, best = Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 1: nt[v] = best[v]
        if ns == sigma and nt == tau:
            fb += 1
            if Is:
                for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
            else:
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        sigma, tau = ns, nt
    return E, hist, fb
def analyse(n, n0, pr, ow, succ, sigma0, tau0, c):
    g = pg.Game(pr, ow, succ); E, hist, fb = n5hist(g, sigma0, tau0); T = len(hist) - 1; rank = E.rank
    c["games"] += 1; c["Tmax"] = max(c["Tmax"], T); c["Tsum"] += T; c["fallbacks"] += fb
    oddmax = max([pr[v] for v in range(n) if pr[v] % 2] + [0]); H = [v for v in range(n0, n) if pr[v] % 2 == 0 and pr[v] > oddmax]
    hmask = sum(1 << rank[v] for v in H); Hs = set(H); c["Hsize"] += len(H)
    rew = lambda v: (rank[v] + 1) if pr[v] % 2 == 0 else -(rank[v] + 1)
    val = [h[1] for h in hist]; sig = [h[0] for h in hist]; tau = [h[2] for h in hist]
    nxt = [[sig[t][v] if ow[v] == 0 else tau[t][v] for v in range(n)] for t in range(T + 1)]
    cls = [[(rew(val[t][v][0]), val[t][v][1] & hmask) for v in range(n)] for t in range(T + 1)]
    oddc = [v for v in range(n) if ow[v] == 1 and len(succ[v]) > 1]; evc = [v for v in range(n) if ow[v] == 0 and len(succ[v]) > 1]; evs = set(evc)
    for t in range(T + 1):
        for v in range(n):
            w = nxt[t][v]
            if (v in Hs and cls[t][v] < cls[t][w]) or (v not in Hs and cls[t][v] != cls[t][w]): c["K3"] += 1
        for q in oddc:
            if cls[t][q] != min(cls[t][y] for y in succ[q]): c["K4"] += 1
        if t < T:
            c["K1"] += sum(1 for v in range(n) if cls[t + 1][v] < cls[t][v])
            for x in evc: c["K5"] += sum(1 for y in succ[x] if cls[t + 1][x] < cls[t][y])
    if T: gen210.level(T, n, c, cls, nxt, sig, tau, succ, evc, evs, oddc, list(range(n0, n)))
if __name__ == "__main__":
    a = sys.argv[1:]; c = collections.Counter()
    if a[0] == "--pg":
        for fn in a[1:]:
            c = collections.Counter(); g0 = pg.read(fn); n, n0, pr, ow, succ = gen210.split(list(g0.prio), list(g0.owner), [list(s) for s in g0.succ])
            g = pg.Game(pr, ow, succ); analyse(n, n0, pr, ow, succ, list(Engine(g).initial("best")), list(Engine(dual(g)).initial("best")), c)
            print("n5lev pg", os.path.basename(fn), "n", n, "fallbacks", c["fallbacks"], gen210.show(c), flush=True)
    else:
        seed, cnt, n0, d, deg, evtop = (int(x) for x in a[:6]); rng = random.Random(seed)
        for i in range(cnt):
            n, n0_, pr, ow, succ = gen210.gen(rng, n0, d, deg, evtop); g = pg.Game(pr, ow, succ)
            sigma = [rng.choice(succ[v]) if ow[v] == 0 else -1 for v in range(n)]; tau = [rng.choice(succ[v]) if ow[v] == 1 else -1 for v in range(n)]
            analyse(n, n0_, pr, ow, succ, sigma, tau, c)
        print("n5lev rand seed", seed, "games", cnt, "n0", n0, "d", d, "deg", deg, "evtop", evtop, "fallbacks", c["fallbacks"], gen210.show(c), flush=True)
