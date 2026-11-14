#!/usr/bin/env python3
"""REFEREE successor 33: is the lane's frozen WL_n.pg my W(G_n, iota) (wrap_f11.build + wrap_replay.wrap, Figure 4's priorities)?
Test: equal vertex and edge counts and equal multisets of 2-step signatures
(priority, owner, sorted successor (priority, owner, sorted successor priorities)). An index-free comparison, not a proof of isomorphism.
Usage: wrap_cmp.py n FILE.pg"""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as E, wrap_replay as WR, wrap_f11 as F
def sig(g):
    def s1(v): return (g.prio[v], g.owner[v], tuple(sorted(g.prio[w] for w in g.succ[v])))
    return collections.Counter((g.prio[v], g.owner[v], tuple(sorted(s1(w) for w in g.succ[v]))) for v in range(g.n))
n = int(sys.argv[1]); lane = E.parse(sys.argv[2])
nodes, idx, prio, owner, succ, s0 = F.build(n); mine, role = WR.wrap(prio, owner, succ, s0)
print(os.path.basename(sys.argv[2]), "n", n, "vertices", lane.n, mine.n, "edges", sum(map(len, lane.succ)), sum(map(len, mine.succ)),
      "signature multisets equal", sig(lane) == sig(mine), "identical as indexed", (lane.prio, lane.owner, lane.succ) == (mine.prio, mine.owner, mine.succ))
