#!/usr/bin/env python3
"""Box 38 (c): build a NO-ENTRY-B attack from a state-level NO-RR-B counterexample (statesamp.py output). At the case-B fallback
state a (τ(o) = o) with a low-route R-rise at v (statesamp.py): add a fresh Even vertex y with successors {f, v}, σ(y) = f, and a chain
f = c_1 -> ... -> c_m -> x0 (x0 = σ̄(o)) of single-successor Even vertices, priority 0, with m = r_v + 1 (r_v = route length of v).
Then Ξ_a(σ y) = Ξ_a(v) (same P, same length: not a gate at a), and after the fallback switches v to a longer route, (y, v) is an honest
gate that W prefers (cycle o over c_θ). Writes the game and the start σ. Usage: neb_aug.py in.pg in.pg.state out.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); B37 = os.path.join(HERE, "..", "box37")
sys.path.insert(0, B37); sys.path.insert(0, os.path.join(HERE, "..", "..", "si", "coarse"))
from outsn import *
import pg

def main(fi, fs, fo):
    g = load(fi); s = list(map(int, open(fs).read().split())); o = odd1(g)
    E = Engine(g); t = [g.succ[v][0] if g.owner[v] == 1 else -1 for v in range(g.n)]; t[o] = o
    Xi, sb = E.evaluate(tuple(s)); Rb = set(reach_o(g, s, t, o)) | {o}
    Ed = Engine(dual(g)); ns = step(g, E, Ed, s, t)[0]
    Xi2, _ = E.evaluate(tuple(ns)); Rb2 = set(reach_o(g, ns, t, o)) | {o}; cth = Xi[o][0]
    def low_route(sig, u):
        nx = [sig[x] if g.owner[x] == 0 else t[x] for x in range(g.n)]
        while u != o:
            if E.rank[u] > E.rank[cth]: return False
            u = nx[u]
        return True
    good = [u for u in sorted(Rb & Rb2) if u != o and Xi2[u] != Xi[u] and low_route(s, u) and low_route(ns, u)]
    v = good[0]; z = ns[v]; x0 = sb[o]
    nxt = [s[u] if g.owner[u] == 0 else t[u] for u in range(g.n)]; r, u = 0, v
    while u != o: u = nxt[u]; r += 1
    m = r + 1; n = g.n; y = n; chain = list(range(n + 1, n + 1 + m))
    prio = list(g.prio) + [0] * (1 + m); owner = list(g.owner) + [0] * (1 + m); succ = [list(x) for x in g.succ]
    succ.append(sorted([chain[0], v]))
    for i, c in enumerate(chain): succ.append([chain[i + 1]] if i + 1 < m else [x0])
    s2 = list(s) + [chain[0]] + [succ[c][0] for c in chain]
    with open(fo, "w") as f:
        f.write(f"parity {len(prio) - 1};\n")
        for w in range(len(prio)): f.write(f"{w} {prio[w]} {owner[w]} {','.join(map(str, succ[w]))};\n")
    with open(fo + ".state", "w") as f: f.write(" ".join(map(str, s2)) + "\n")
    print(fo, "v", v, "z", z, "x0", x0, "r_v", r, "y", y, "m", m)

if __name__ == "__main__": main(*sys.argv[1:4])
