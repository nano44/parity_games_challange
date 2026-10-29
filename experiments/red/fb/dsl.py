#!/usr/bin/env python3
"""L-RED successor 24: tiny DSL for hand constructions. spec = list of (name, owner, prio, [succ names], start succ name or None).
build(spec) -> (pg.Game, start pair dicts, names). write(spec, path) writes a .pg (labels = names) and a full .start."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "sel"))
import trace as T

def build(spec):
    idx = {s[0]: i for i, s in enumerate(spec)}
    assert len(idx) == len(spec), "duplicate names"
    prio = [s[2] for s in spec]; owner = [s[1] for s in spec]
    succ = [sorted(set(idx[x] for x in s[3])) for s in spec]
    sig, tau = {}, {}
    for i, s in enumerate(spec):
        if s[4] is not None:
            w = idx[s[4]]; assert w in succ[i], (s[0], s[4])
            (sig if s[1] == 0 else tau)[i] = w
    return T.pg.Game(prio, owner, succ), (sig, tau), [s[0] for s in spec]

def write(spec, path):
    g, (sig, tau), nm = build(spec)
    E, Ed = T.Engine(g), T.Engine(T.dual(g))
    s, t = list(E.initial("best")), list(Ed.initial("best"))
    for v, w in sig.items(): s[v] = w
    for v, w in tau.items(): t[v] = w
    with open(path, "w") as f:
        f.write("parity %d;\n" % (g.n - 1))
        for v in range(g.n):
            f.write('%d %d %d %s "%s";\n' % (v, g.prio[v], g.owner[v], ",".join(map(str, g.succ[v])), nm[v]))
    with open(path[:-3] + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join("%d:%d" % (v, s[v]) for v in range(g.n) if g.owner[v] == 0) + "\n")
        f.write("TAU0 " + " ".join("%d:%d" % (v, t[v]) for v in range(g.n) if g.owner[v] == 1) + "\n")
