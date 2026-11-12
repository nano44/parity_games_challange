#!/usr/bin/env python3
"""L-RED 66 R236 (3): diff two .pg games vertex by vertex: owners, successor lists, priorities; for the priority changes, classify the
changed vertices by the E-DOM-build's priority band (<= 5: core/pads/K1/K2; else carriers / top). Usage: d236.py A.pg B.pg"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import n5x236 as X
pa, oa, sa = X.parse(sys.argv[1]); pb, ob, sb = X.parse(sys.argv[2])
assert len(pa) == len(pb), ("sizes", len(pa), len(pb))
n = len(pa); own = sum(oa[v] != ob[v] for v in range(n)); suc = sum(sa[v] != sb[v] for v in range(n))
ch = [v for v in range(n) if pa[v] != pb[v]]
low = [v for v in ch if pb[v] <= 5 or pa[v] <= 5]
top = sorted(range(n), key=lambda v: -pb[v])[:3]; topa = sorted(range(n), key=lambda v: -pa[v])[:3]
print("vertices", n, "owner diffs", own, "successor-list diffs", suc, "priority diffs", len(ch), "of which touching priorities <= 5:", len(low),
      "| top-3 (B) vertices", top, [pb[v] for v in top], "in A", [pa[v] for v in top], "| top-3 (A)", topa, [pa[v] for v in topa],
      "| parity changes", sum(1 for v in ch if pa[v] % 2 != pb[v] % 2))
