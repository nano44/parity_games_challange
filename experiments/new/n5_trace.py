#!/usr/bin/env python3
"""Per-iteration trace of N5 (box 4). Same loop as n5.py mode n5 (copied verbatim, plus logging); the final line asserts the
counts equal n5.run's on the same input. Per iteration: |Iσ|, |Iτ|, vertices σ changes (σ'≠σ), vertices τ changes, fallback flag.
Usage: n5_trace.py game.pg [--labels]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n5
from n5 import pg, Engine, dual
def trace(g, out=print):
    n = g.n; E, Ed = Engine(g), Engine(dual(g))
    sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    it = fb = 0; rows = []
    while True:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        if not Is and not It: break
        it += 1
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
        f = 0
        if ns == sigma and nt == tau:
            fb += 1; f = 1
            if Is:
                for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
            else:
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        cs = [v for v in range(n) if ns[v] != sigma[v]]; ct = [v for v in range(n) if nt[v] != tau[v]]
        rows.append((it, len(Is), len(It), cs, ct, f))
        out(f"it {it}: |Is|={len(Is)} |It|={len(It)} fb={f} sigma_changes={len(cs)} {cs} tau_changes={len(ct)} {ct}")
        sigma, tau = ns, nt
    ri, rf, *_ = n5.run(g)
    assert (ri, rf) == (it, fb), (ri, rf, it, fb)
    out(f"TOTAL iterations={it} fallback={fb} (= n5.run)")
    return rows
if __name__ == "__main__":
    g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
    trace(g)
