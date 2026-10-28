#!/usr/bin/env python3
"""Box 16 §5 (Lead 2026-10-28 21:05Z): H_n variants in which Odd's τ cannot shut a gate permanently. DATA probes, not [F] constructions.
  dual  dual(H_n) (hn.py mode fig): owners swapped, priorities + 1 (n5b.dual). Odd is now [F]'s counting player 0 (lane, stubborn
        cycles, gates' access nodes) and the gate choice at e_i is Even's. τ's improvements are then the [F] counter if N5 followed [F].
  ex    H_n (mode fig) with Odd's exit from e_i routed through a new Even node u_i: e_i -> {d1_i, u_i}, u_i -> {h_i, d2_i},
        Ω(u_i) = 8i - 4 (free and even in gate i's block 8i-5..8i+2; injective). Even can turn the exit back into the stubborn cycle
        (e_i -> u_i -> d2_i -> d3_i -> e_i, top priority Ω(e_i) = 8i even), so whether u_i is a safe exit for Odd depends on σ(u_i) and
        Odd's best gate choice depends on Even's state. Not 1-sink in general (Oink decides the winner).
iota(n, ix, var): the start of the counting player ([F]'s ι), as {vertex: successor}; for ex, ι plus ι(u_i) = h_i; for dual, ι is
        an Odd (τ) start in the dual game.
Usage: hn_var.py N VAR --out FILE.pg"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import hn, pg  # noqa: E402

VARS = ("dual", "ex")


def build(n, var):
    g, ix = hn.build(n, "fig")
    if var == "dual":
        return pg.Game([p + 1 for p in g.prio], [1 - o for o in g.owner], g.succ, g.labels), ix
    if var == "ex":
        prio, own, succ, lab = list(g.prio), list(g.owner), [list(s) for s in g.succ], list(g.labels)
        ix = dict(ix)
        for i in range(1, n + 1):
            u = len(prio); ix[f"u{i}"] = u
            prio.append(8 * i - 4); own.append(0); succ.append(sorted([ix[f"h{i}"], ix[f"d2_{i}"]])); lab.append(f"u{i}")
            succ[ix[f"e{i}"]] = sorted([ix[f"d1_{i}"], u])
        assert len(set(prio)) == len(prio)
        return pg.Game(prio, own, succ, lab), ix
    raise ValueError(var)


def iota(n, ix, var):
    s = hn.iota(n, ix)
    if var == "ex":
        for i in range(1, n + 1):
            s[ix[f"u{i}"]] = ix[f"h{i}"]
    return s


if __name__ == "__main__":
    n, var = int(sys.argv[1]), sys.argv[2]
    g, _ = build(n, var)
    pg.write(g, sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else sys.stdout.write(pg.dumps(g))
