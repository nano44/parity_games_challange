#!/usr/bin/env python3
"""Box 37 (b): constructive search against NO-ENTRY (docs/new/N5-OUT-box37.md §6-§7). Given a base game, add ONE fresh Even vertex y
(no in-edges) with successors {v, f} and priority p, for all v, f and every priority p in 0..n, and count NO-ENTRY violations (rfrozen.py
classes S4A_afterfb_entry / FB_afterfb_entry). Writes the best gadget game. One Odd choice vertex asserted (rfrozen.run).
Usage: gadget.py base.pg out.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "box31"))
from rfrozen import *
from cascclimb import save

if __name__ == "__main__":
    g = load(sys.argv[1]); n = g.n; best = (0, None)
    for v in range(n):
        for f in range(n):
            if f == v: continue
            for p in range(n + 1):
                G = [list(g.prio) + [p], list(g.owner) + [0], [list(x) for x in g.succ] + [sorted({v, f})]]
                acc = {}
                try: run(pg.Game(*G), acc, "gad")
                except Exception: continue
                viol = acc.get("S4A_afterfb_entry", 0) + acc.get("FB_afterfb_entry", 0)
                if viol > best[0]: best = (viol, (v, f, p)); save(sys.argv[2], G); print("viol", viol, "v f p", v, f, p, flush=True)
    print("BEST", best)
