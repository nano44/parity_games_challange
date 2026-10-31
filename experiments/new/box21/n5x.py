#!/usr/bin/env python3
"""Box 21 trace of N5 (docs/new/N5-ssi-global.md SPEC S1-S5): same loop as experiments/new/n5.py run(), but returns the
per-iteration states (sigma, tau, Is, It, fallback flag). trace() asserts its counts equal n5.run's on the same input.
Read-only use of n5.py / si.py."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in ("experiments/new", "experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(ROOT, p))
import pg, n5
from si import Engine
dual = n5.dual

def load(path):
    return pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))

def step(g, E, Ed, sigma, tau):
    """One N5 iteration from (sigma, tau). Returns (ns, nt, Is, It, fb, vs, vt) or None if Is = It = empty."""
    n = g.n
    vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
    vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
    if not Is and not It: return None
    ns, nt = list(sigma), list(tau)
    if Is:
        opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
        for v, w in Is: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
        Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
        _, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 0: ns[v] = best[v]
    if It:
        opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
        for v, w in It: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
        Er = Engine(pg.Game(list(g.prio), list(g.owner), succ))
        _, best = Er.evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 1: nt[v] = best[v]
    fb = 0
    if ns == sigma and nt == tau:
        fb = 1
        if Is:
            for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
        else:
            for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
    return ns, nt, Is, It, fb, vs, vt

def start_pair(g, E, Ed, start=None):
    sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    if start:
        for v, w in start[0].items(): sigma[v] = w
        for v, w in start[1].items(): tau[v] = w
        # start validation (box 113, referee finding D-ODD-1 / F-1): every start move must be an edge of its owner's vertex
        bad = [(v, w) for d, own in ((start[0], 0), (start[1], 1)) for v, w in d.items()
               if not (0 <= v < g.n and g.owner[v] == own and w in g.succ[v])]
        # strict for L-NEW's own tools (scripts under experiments/new) or when N5X_STRICT_START=1; other lanes' callers are unchanged
        # (their pinned checks, e.g. si/check.sh on src54's sbq2 start, are theirs to repair; reported to the Lead)
        strict = os.environ.get("N5X_STRICT_START") == "1" or os.path.abspath(sys.argv[0]).startswith(os.path.abspath(os.path.join(HERE, "..")) + os.sep)
        if bad and strict: raise SystemExit(f"start_pair: invalid start entries (vertex not of that player, or move not an edge): {bad[:5]}")
    return sigma, tau

def trace(g, start=None, cap=10 ** 6, check=True):
    E, Ed = Engine(g), Engine(dual(g))
    sigma, tau = start_pair(g, E, Ed, start)
    states = [(tuple(sigma), tuple(tau))]; fbs = 0
    while len(states) - 1 < cap:
        r = step(g, E, Ed, sigma, tau)
        if r is None: break
        sigma, tau, Is, It, fb, _, _ = r; fbs += fb
        states.append((tuple(sigma), tuple(tau)))
    if check:
        it, fb, *_ = n5.run(g, "n5", start, cap)
        assert (it, fb) == (len(states) - 1, fbs), ((it, fb), (len(states) - 1, fbs))
    return states, fbs

def readstart(path):
    """start file as in experiments/red/n5/instances/*.start: two lines 'SIGMA0 v:w ...' and 'TAU0 v:w ...'."""
    ls = [l.split() for l in open(path) if l.strip()]
    return tuple(dict(map(int, t.split(":")) for t in l[1:]) for l in ls[:2])
