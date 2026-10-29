#!/usr/bin/env python3
"""L-RED successor 24: hill climb at FIXED n for f = in-phase fallbacks of one phase (CONJECTURE FB-LIN: f <= n). Start pair: sigma from
the genome (every entry an existing edge), tau = the final tau of a pre-run from that start (Odd-optimal, so I_tau = 0 and tau never moves:
the TAUSTAR start). Mutations: priority (any value in 0..P), add / delete an edge, Even start entry. Fitness = 1000 f + total fallbacks.
Usage: fbclimb.py SEED.pg SEED.start|S3 seed secs OUTPREFIX [--keepodd] [--owntau: tau0 from the start file (valid entries), not TAUSTAR]"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "sel"))
import trace as T
from fbphase import fstats, reuse
REUSE = "--reuse" in sys.argv

def load(p, s):
    g = T.pg.parse("".join(l for l in open(p) if not l.lstrip().startswith("%")))
    st = ({}, {}) if s == "S3" else T.readstart(s)
    E = T.Engine(g); sig = list(E.initial("best"))
    for v, w in st[0].items():
        if g.owner[v] == 0 and w in g.succ[v]: sig[v] = w
    tau = {v: w for v, w in st[1].items() if g.owner[v] == 1 and w in g.succ[v]}
    return [list(g.prio), list(g.owner), [list(x) for x in g.succ], sig, tau]

def ev(G):
    prio, owner, succ, sig, tau0 = G
    g = T.pg.Game(list(prio), list(owner), [sorted(set(x)) for x in succ])
    s0 = {v: sig[v] for v in range(g.n) if owner[v] == 0}
    try:
        if OWNTAU:
            st = (s0, {v: w for v, w in tau0.items() if w in g.succ[v]})
        else:
            it, fb, ph, mp, s, t, h = T.run(g, (s0, {}), cap=3000, log=lambda *a: None)
            if it >= 3000: return None
            st = (s0, {v: t[v] for v in range(g.n) if owner[v] == 1})
        it2, fb2, *_ = T.run(g, st, cap=3000, log=lambda *a: None)
        if REUSE:
            f, R = reuse(g, st, cap=3000)
            return 100 * f + 1000 * R + fb2, f, st, R
        f, ph, it3 = fstats(g, st, cap=3000)
        return 1000 * f + fb2, f, st
    except Exception: return None

OWNTAU = "--owntau" in sys.argv
def mutate(rng, G, P, keepodd):
    prio, owner, succ, sig = [list(G[0]), list(G[1]), [list(x) for x in G[2]], list(G[3])]; n = len(prio)
    r = rng.randrange(6); v = rng.randrange(n)
    if r <= 1: prio[v] = rng.randrange(P)
    elif r == 2 or r == 3:
        if keepodd and owner[v] == 1: return None
        w = rng.randrange(n)
        if w in succ[v]:
            if len(succ[v]) == 1: return None
            succ[v].remove(w)
            if owner[v] == 0 and sig[v] == w: sig[v] = rng.choice(succ[v])
        else: succ[v].append(w)
    else:
        if owner[v] != 0: return None
        sig[v] = rng.choice(succ[v])
    return [prio, owner, succ, sig, dict(G[4])]

def save(out, G, st):
    prio, owner, succ, sig, _ = G
    with open(out + ".pg", "w") as f:
        f.write("parity %d;\n" % (len(prio) - 1))
        for v in range(len(prio)): f.write("%d %d %d %s;\n" % (v, prio[v], owner[v], ",".join(map(str, sorted(set(succ[v]))))))
    with open(out + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join("%d:%d" % (v, w) for v, w in sorted(st[0].items())) + "\n")
        f.write("TAU0 " + " ".join("%d:%d" % (v, w) for v, w in sorted(st[1].items())) + "\n")

if __name__ == "__main__":
    G = load(sys.argv[1], sys.argv[2]); seed, secs, out = int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
    keepodd = "--keepodd" in sys.argv
    rng = random.Random(seed); P = max(G[0]) + 4; n = len(G[0])
    cur = ev(G); best = cur; Gc = G; t0 = time.time(); print("n", n, "start f", cur[1], flush=True)
    while time.time() - t0 < secs:
        H = Gc
        for _ in range(rng.choice((1, 1, 2, 3))):
            H2 = mutate(rng, H, P, keepodd)
            if H2 is not None: H = H2
        e = ev(H)
        if e is None: continue
        if e[0] >= cur[0]:
            Gc, cur = H, e
            if e[0] > best[0]:
                best = e; save(out, H, e[2]); print("%.0fs f=%d fit=%d%s" % (time.time() - t0, e[1], e[0], (" R=%d" % e[3]) if REUSE else ""), flush=True)
    print("BEST f", best[1], "n", n)
