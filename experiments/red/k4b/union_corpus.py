#!/usr/bin/env python3
"""L-RED box 6 (produced on Opus 5.5): disjoint union GADGET + each corpus game (gadget first, then the game; and the
game first, then the gadget), kfuzz.check in both orders. Usage: union_corpus.py GADGET.pg OUTDIR FILES..."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "carry"))
import kfuzz, pg
def union(a, b):
    k = a.n; return pg.Game(a.prio + b.prio, a.owner + b.owner, a.succ + [[w + k for w in s] for s in b.succ])
gad = pg.read(sys.argv[1]); out = sys.argv[2]; os.makedirs(out, exist_ok=True); tot = {}
for f in sys.argv[3:]:
    try: q = pg.read(f)
    except Exception: continue
    if q.n > 80: continue
    for tag, g in (("gq", union(gad, q)), ("qg", union(q, gad))):
        for order in ("oink", "stable"):
            try: bad = kfuzz.check(g, order)
            except Exception as e: bad = ["ERR"]
            for b in set(bad):
                tot[b] = tot.get(b, 0) + 1
                if b.startswith("_"): continue
                fn = os.path.join(out, f"{os.path.basename(f)[:-3]}_{tag}_{order}_{b}.pg"); open(fn, "w").write(pg.dumps(g))
                print(b, order, tag, f, flush=True)
print(tot)
