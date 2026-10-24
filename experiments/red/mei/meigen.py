#!/usr/bin/env python3
"""Mei's mean-payoff family Ĝ_h (arXiv 2610.27386 §5.1 p.20; graph Table 1 p.5) ported to a parity game per docs/lit/T31-mei-port.md (iii).
Even = Mei's Player 1 (a_i), Odd = Player 2. Costed edges split by forced cost vertices (owner Odd): w (W_i, odd priority),
k (-K_i, even priority), r (-R, even priority). Priorities exactly as T31's table (h >= 2).
Usage: meigen.py h out.pg  (also writes out.pg.start: Mei's start sigma_0 (4) and tau_0 = Odd's best reply, as SIGMA0/TAU0 lines)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness")); sys.path.insert(0, os.path.join(HERE, "..", "..", "si"))
import pg

def build(h):
    names = []; idx = {}
    def V(nm): idx[nm] = len(names); names.append(nm)
    for i in range(1, h + 2): V(f"a{i}"); V(f"b{i}")
    for i in range(1, h + 1):
        for nm in ("p", "q", "wp", "wq", "kp", "kq"): V(f"{nm}{i}")
    V("r")
    n = len(names); assert n == 8 * h + 3
    prio = [0] * n; owner = [1] * n; succ = [None] * n
    for i in range(1, h + 1):
        a, b, p, q = idx[f"a{i}"], idx[f"b{i}"], idx[f"p{i}"], idx[f"q{i}"]
        owner[a] = 0; succ[a] = [p, q]
        succ[p] = [idx[f"wp{i}"], idx[f"kp{i}"]]; succ[q] = [idx[f"wq{i}"], idx[f"kq{i}"]]
        succ[idx[f"wp{i}"]] = [idx[f"a{i+1}"]]; succ[idx[f"wq{i}"]] = [idx[f"b{i+1}"]]
        succ[idx[f"kp{i}"]] = [a]; succ[idx[f"kq{i}"]] = [a]
        succ[b] = [idx[f"a{i+1}"], idx[f"b{i+1}"]]
        prio[idx[f"kq{i}"]] = 6 + 4 * (h - i); prio[idx[f"kp{i}"]] = 8 + 4 * (h - i)
        if i == 1: prio[idx["wp1"]], prio[idx["wq1"]] = 3, 5
        else: prio[idx[f"wp{i}"]], prio[idx[f"wq{i}"]] = 4 * h + 4 * i - 3, 4 * h + 4 * i - 1
    A = idx[f"a{h+1}"]; owner[A] = 0; succ[A] = [A]; prio[A] = 1
    succ[idx[f"b{h+1}"]] = [idx["r"]]; succ[idx["r"]] = [A]; prio[idx["r"]] = 8 * h + 2
    assert len(set(p for p in prio if p > 0)) == len([p for p in prio if p > 0])  # injective non-zero priorities
    return pg.Game(prio, owner, succ, labels=names), idx

def mei_start(g, idx, h):
    from si import Engine
    E = Engine(g)
    sigma = [-1] * g.n
    for v in range(g.n):
        if g.owner[v] == 0: sigma[v] = g.succ[v][0]
    for i in range(1, h + 1): sigma[idx[f"a{i}"]] = idx[f"p{i}"]
    _, sbar = E.evaluate(tuple(sigma))
    s0 = {v: sigma[v] for v in range(g.n) if g.owner[v] == 0}
    t0 = {v: sbar[v] for v in range(g.n) if g.owner[v] == 1}
    return s0, t0

if __name__ == "__main__":
    h, out = int(sys.argv[1]), sys.argv[2]
    g, idx = build(h); pg.write(g, out)
    s0, t0 = mei_start(g, idx, h)
    with open(out + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(s0.items())) + "\n")
        f.write("TAU0 " + " ".join(f"{v}:{w}" for v, w in sorted(t0.items())) + "\n")
