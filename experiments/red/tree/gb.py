#!/usr/bin/env python3
"""L-RED successor 32 (R131): named game builder + N5 step tracer (L-NEW n5x step). G = GB(); G.v(name, owner, prio, succs);
G.start(name, succ) sets sigma0 / tau0; G.game() -> (pg.Game, start); trace(G, watch) prints per step the sigma / tau changes by name and,
for watched vertices, W (val(sigma, tau) on G_tau) and Xi (val(sigma, Odd best response)) as (cycle node, top path priorities)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import step, start_pair, Engine, dual
import pg

class GB:
    def __init__(self): self.names, self.own, self.pr, self.sc, self.st = [], {}, {}, {}, {}
    def v(self, name, owner, prio, succ):
        assert name not in self.own, name
        self.names.append(name); self.own[name] = owner; self.pr[name] = prio; self.sc[name] = list(succ)
    def start(self, name, succ): self.st[name] = succ
    def game(self):
        ix = {v: i for i, v in enumerate(self.names)}; self.ix = ix
        for v in self.names:
            for w in self.sc[v]: assert w in ix, (v, w)
        g = pg.Game([self.pr[v] for v in self.names], [self.own[v] for v in self.names], [[ix[w] for w in self.sc[v]] for v in self.names])
        s0 = {ix[v]: ix[w] for v, w in self.st.items() if self.own[v] == 0}; t0 = {ix[v]: ix[w] for v, w in self.st.items() if self.own[v] == 1}
        return g, (s0, t0)
    def write(self, pgpath, startpath):
        g, (s0, t0) = self.game(); n = len(self.names)
        with open(pgpath, "w") as f:
            f.write(f"parity {n - 1};\n")
            for i, v in enumerate(self.names): f.write(f"{i} {self.pr[v]} {self.own[v]} {','.join(str(self.ix[w]) for w in self.sc[v])} \"{v}\";\n")
        E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, (s0, t0))
        with open(startpath, "w") as f:
            f.write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in range(n) if g.owner[v] == 0) + "\n")
            f.write("TAU0 " + " ".join(f"{v}:{t[v]}" for v in range(n) if g.owner[v] == 1) + "\n")

def desc(E, g, names, val):
    lam, mask, ln = val[0], val[1], val[2]
    ps = sorted((g.prio[v] for v in range(g.n) if mask & E.bit[v]), reverse=True)
    return f"{names[lam]}|{','.join(map(str, ps[:4]))}|{ln}"

def trace(G, watch=(), cap=400, quiet=False):
    g, st = G.game(); n = g.n; names = G.names; E, Ed = Engine(g), Engine(dual(g))
    s, t = start_pair(g, E, Ed, st); WE = {}
    def W(s, t):
        t = tuple(t)
        if t not in WE: WE[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]))
        return WE[t], WE[t].evaluate(tuple(s))[0]
    it = 0; out = []
    while it < cap:
        if watch and not quiet:
            we, wv = W(s, t); xv, _ = E.evaluate(tuple(s))
            print(f"  [{it}] " + "  ".join(f"{x}: W {desc(we, g, names, wv[G.ix[x]])} X {desc(E, g, names, xv[G.ix[x]])}" for x in watch))
        r = step(g, E, Ed, list(s), list(t))
        if r is None: break
        ns, nt, Is, It, fb, _, _ = r; it += 1
        ch = [f"{names[v]}->{names[ns[v]]}" for v in range(n) if ns[v] != s[v]] + [f"T {names[v]}->{names[nt[v]]}" for v in range(n) if nt[v] != t[v]]
        out.append(ch)
        if not quiet: print(f"{it}: {' '.join(ch)}{'  FB' if fb else ''}")
        s, t = ns, nt
    return it, out

def from_pg(pgpath, startpath=None):
    """GB from a .pg file with quoted names (and an optional SIGMA0 / TAU0 start file)."""
    G = GB(); rows = []
    for l in open(pgpath):
        l = l.strip().rstrip(";")
        if not l or l.startswith("parity"): continue
        a = l.split(None, 3); rest = a[3]; succ, _, nm = rest.partition(" "); nm = nm.strip().strip('"') or a[0]
        rows.append((int(a[0]), int(a[1]), int(a[2]), [int(x) for x in succ.split(",")], nm))
    nm = {i: x for i, _, _, _, x in rows}
    for i, p, o, s, x in rows: G.v(x, o, p, [nm[w] for w in s])
    if startpath:
        for l in open(startpath):
            for tok in l.split()[1:]:
                v, w = map(int, tok.split(":")); G.start(nm[v], nm[w])
    return G
