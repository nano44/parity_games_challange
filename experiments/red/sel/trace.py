#!/usr/bin/env python3
"""L-RED successor 23: N5 run (same loop as experiments/new/n5.py run(), mode n5, SPEC S1-S5) with a per-iteration trace:
kind (A = S4a/S4b step, FB = fallback), Even switches, tau changes, sigma-bar changes at Odd vertices, phase number (tau change).
Vertex names are read from the .pg labels. Usage: trace.py GAME.pg START [--quiet]  (prints RESULT iterations fb phases maxphase)"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "..", "..")
sys.path.insert(0, os.path.join(ROOT, "experiments", "si")); sys.path.insert(0, os.path.join(ROOT, "experiments", "harness"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new"))
import pg
from si import Engine
from n5 import dual

def names(path):
    nm = {}
    for l in open(path):
        m = re.match(r'\s*(\d+)\s+\d+\s+\d+\s+[\d,]+\s+"([^"]*)"', l)
        if m: nm[int(m.group(1))] = m.group(2)
    return nm

def run(g, start, cap=10 ** 6, log=print, nm=None):
    nm = nm or {}
    N = lambda v: nm.get(v, str(v))
    n = g.n; E, Ed = Engine(g), Engine(dual(g))
    sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    for v, w in start[0].items(): sigma[v] = w
    for v, w in start[1].items(): tau[v] = w
    it = fb = 0; phase = 0; plen = 0; maxp = 0; prev_sbar = None; hist = []
    while it < cap:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        sb = [sbar[v] if g.owner[v] == 1 else None for v in range(n)]
        if prev_sbar is not None:
            ch = [v for v in range(n) if g.owner[v] == 1 and sb[v] != prev_sbar[v]]
            if ch: log("     sbar: " + " ".join("%s->%s" % (N(v), N(sb[v])) for v in ch))
        prev_sbar = sb
        if not Is and not It: break
        it += 1
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
        kind = "A"
        if ns == sigma and nt == tau:
            fb += 1; kind = "FB"
            if Is:
                for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
            else:
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        if nt != tau: phase += 1; plen = 0
        plen += 1; maxp = max(maxp, plen)
        sw = [v for v in range(n) if ns[v] != sigma[v]]; tw = [v for v in range(n) if nt[v] != tau[v]]
        log("%4d %-2s ph%d Isz=%d  even: %s%s" % (it, kind, phase, len(Is), " ".join("%s->%s" % (N(v), N(ns[v])) for v in sw),
            ("  TAU: " + " ".join("%s->%s" % (N(v), N(nt[v])) for v in tw)) if tw else ""))
        hist.append((kind, sw, tw))
        sigma, tau = ns, nt
    return it, fb, phase, maxp, sigma, tau, hist

def readstart(path):
    L = open(path).read().split("\n")
    return tuple(dict(map(int, t.split(":")) for t in L[j].split()[1:]) for j in (0, 1))

if __name__ == "__main__":
    path, st = sys.argv[1], sys.argv[2]
    g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
    quiet = "--quiet" in sys.argv
    it, fb, ph, maxp, s, t, h = run(g, readstart(st), log=(lambda *a: None) if quiet else print, nm=names(path))
    print("RESULT n=%d iterations=%d fallback=%d tau_changes=%d longest_phase=%d" % (g.n, it, fb, ph, maxp))
