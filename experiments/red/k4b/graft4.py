#!/usr/bin/env python3
"""L-RED box 6 (produced on Opus 5.5): L-ALG's (beta') shape (Lead 10:36Z): stored tangle {a, b}, a p-owned priority 2
(-> b, optionally -> base vertex A), b opponent-owned priority 1 (-> a, e), e priority 1 (owner 0 or 1) -> base vertices
S (|S| = 1 or 2). Exhaustive over A, owner(e), S on a base game, both orders, scored with carry/slow.py (loose / tight
S-LOW violations, incomplete runs). Usage: graft4.py BASE.pg OUTDIR  (LALG12_DIR set)"""
import sys, os, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "carry"))
import slow, pg
B = pg.read(sys.argv[1]); out = sys.argv[2]; os.makedirs(out, exist_ok=True); n = B.n; tot = {}; cnt = 0
a, b, e = n, n + 1, n + 2
for A in [None] + list(range(n)):
    for oe in (0, 1):
        for S in itertools.chain(itertools.combinations(range(n), 1), itertools.combinations(range(n), 2)):
            succ = [list(s) for s in B.succ] + [[b] + ([A] if A is not None else []), [a, e], list(S)]
            g = pg.Game(list(B.prio) + [2, 1, 1], list(B.owner) + [0, 1, oe], succ); cnt += 1
            fn = os.path.join(out, "cur.pg"); open(fn, "w").write(pg.dumps(g))
            for order in ("oink", "stable"):
                os.environ["DTL_ORDER"] = order
                try: m = slow.measure(fn)
                except Exception: continue
                for k in ("incomplete", "loose", "tight", "qual", "lowfail"): tot[k] = tot.get(k, 0) + (m[k] > 0)
                if m["incomplete"] or m["loose"] or m["tight"]:
                    hf = os.path.join(out, f"g4_{A}_{oe}_{'_'.join(map(str, S))}_{order}.pg"); open(hf, "w").write(pg.dumps(g)); print("HIT", order, m, hf, flush=True)
print("games", cnt, "runs with >0:", tot)
