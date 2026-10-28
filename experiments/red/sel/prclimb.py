#!/usr/bin/env python3
"""L-RED successor 23: priority-only climb on a FIXED topology (mkladchain.py), fixed start pair; fitness = (PL, fallbacks in that phase)
with PL the longest phase (phsw.plfb). Usage: prclimb.py L m seed secs OUT.pg [--fbfirst: fitness (fallbacks in longest phase, PL)]"""
import sys, os, time, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import trace as T, phsw, mkladchain as MK
FBFIRST = "--fbfirst" in sys.argv

def fit(names, own, succ, prio, sig, tau, cap=3000):
    idx = {nm: i for i, nm in enumerate(names)}
    g = T.pg.Game([prio[nm] for nm in names], [own[nm] for nm in names], [sorted(idx[x] for x in succ[nm]) for nm in names])
    st = ({idx[a]: idx[b] for a, b in sig.items()}, {idx[a]: idx[b] for a, b in tau.items()})
    try:
        PL, FB = phsw.plfb(g, st, cap=cap)
        return (FB, PL) if FBFIRST else (PL, FB)
    except Exception: return (-1, -1)

def main():
    L, m, seed, secs, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
    rng = random.Random(seed); names, own, succ = MK.build(L, m); sig, tau = MK.start(names, own, succ, L, m)
    P = 2 * len(names) + 2
    prio = {nm: rng.randrange(P) for nm in names}
    best = (fit(names, own, succ, prio, sig, tau), prio); t0 = time.time(); it = 0
    print("n", len(names), "start", best[0], flush=True)
    while time.time() - t0 < secs:
        it += 1; p = dict(best[1])
        for _ in range(rng.choice((1, 1, 2, 3))):
            if rng.random() < 0.5: p[rng.choice(names)] = rng.randrange(P)
            else:
                a, b = rng.sample(names, 2); p[a], p[b] = p[b], p[a]
        f = fit(names, own, succ, p, sig, tau)
        if f >= best[0]:
            if f > best[0]:
                print("%.0fs it %d fit %s n %d" % (time.time() - t0, it, f, len(names)), flush=True)
                MK.write(names, own, succ, p, sig, tau, out)
            best = (f, p)
    MK.write(names, own, succ, best[1], sig, tau, out); print("END", best[0], "iters", it, flush=True)

if __name__ == "__main__":
    main()
