#!/usr/bin/env python3
"""Python port of Oink's Two Counters generator (src/tools/tc.cpp, 8fbf0a7; max-parity, Even = 0) with variant knobs for
the DTL attack (Lead 13:56Z). Plain variant must reproduce tc N up to vertex renumbering (checked by solver work counts).
Knobs (all default = plain tc):
  dd        : DOUBLEDISTRACTION (tc.cpp line 22): a second gate LL per bit (L -> LL -> T).
  lane      : insert `lane` extra vertices (priority lane_pr, owner = bit's opponent) on each A/B -> input edge
              (the "deceleration lane" tc.cpp names in m = 3n but never uses).
  gates     : put `gates` gate vertices in series before T (L_1 -> ... -> L_k -> T), all with the input priority.
  zshift    : add `zshift` to the Z vertex priority (tc+ uses lopr+2 for its Z vertices).
  tprio     : override the T (tangle) vertex priority offset (default lopr).
  hprio_gap : extra gap between consecutive bits' high priorities (default 2 as in tc.cpp).
Usage: tcvar.py N [--dd] [--lane k] [--lane-pr p] [--gates k] [--zshift s] [--write f.pg] ; prints PGSolver format."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg


def tc(n, dd=False, lane=0, lane_pr=0, gates=1, zshift=0, tprio=None, hprio_gap=2):
    prio, owner, succ, names = [], [], [], []
    def new(p, o, name):
        prio.append(p); owner.append(o); succ.append([]); names.append(name); return len(prio) - 1
    def edge(a, b):
        if b not in succ[a]: succ[a].append(b)
    inp = [[None] * n, [None] * n]   # inp[player][bit] = gate (input/distraction) vertex of that player's bit
    bits = []                        # (pl, i, c, t, lopr) for the second pass (connectors need inputs of lower bits)
    toppo = (n + 3) * n + 6 * n
    for i in range(n):
        for pl, hipr, inpr, lopr in ((0, toppo - 2, toppo - 2 * n - 3, 2), (1, toppo - 1, toppo - 2 * n - 2, 1)):
            tag = f"{'Odd' if pl else 'Even'}-{i}"
            h = new(hipr, pl, f"{tag}-H")
            t = new(lopr if tprio is None else tprio + (1 - pl), 1 - pl, f"{tag}-T")
            gs = [new(inpr, 1 - pl, f"{tag}-L{k}") for k in range(gates)]
            if dd: gs.append(new(inpr, 1 - pl, f"{tag}-LL"))
            for a, b in zip(gs, gs[1:]): edge(a, b)
            edge(gs[-1], t); edge(t, h)
            inp[pl][i] = gs[0]
            bits.append((pl, i, h, t, lopr))
        toppo -= hprio_gap
    for (pl, i, h, t, lopr) in bits:
        tag = f"{'Odd' if pl else 'Even'}-{i}"
        prev = (t,)                   # chain of selectors S_j, j < i; prev = vertices that lead to the next selector
        for j in range(i):
            s = new(lopr - 1, pl, f"{tag}-S-{j}"); a = new(lopr - 1, 1 - pl, f"{tag}-A-{j}"); b = new(lopr - 1, 1 - pl, f"{tag}-B-{j}")
            for p_ in prev: edge(p_, s)
            edge(s, a); edge(s, b)
            ina, inb = inp[pl][j], inp[1 - pl][j]       # A -> own-parity input of bit j, B -> opponent's input of bit j
            for src, dst in ((a, ina), (b, inb)):
                cur = src
                for k in range(lane):
                    x = new(lane_pr, 1 - pl, f"{tag}-lane-{j}-{k}"); edge(cur, x); cur = x
                edge(cur, dst)
            prev = (a, b)
        # Z (distracted) vertex: from T's chain end to T, and to the opponent's inputs of higher bits (odd: only lower? per tc.cpp)
        z = new(lopr - 1 + zshift, pl, f"{tag}-Z")
        for p_ in prev: edge(p_, z)
        edge(z, t)
        for j in range(i + 1 - pl, n):           # tc.cpp line 112: for j = i+1-pl .. n-1: Z -> _in[j] (opponent's inputs)
            edge(z, inp[1 - pl][j])
        edge(h, inp[pl][(i + n - 1) % n])        # tc.cpp line 104: H -> own input of bit (i-1) mod n
    return pg.Game(prio, owner, [sorted(s) for s in succ], names)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    g = tc(int(args[0]), dd="--dd" in sys.argv, lane=int(opt("--lane", 0)), lane_pr=int(opt("--lane-pr", 0)),
           gates=int(opt("--gates", 1)), zshift=int(opt("--zshift", 0)))
    if "--write" in sys.argv: pg.write(g, opt("--write", ""))
    else: sys.stdout.write(pg.dumps(g))
