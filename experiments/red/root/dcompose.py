#!/usr/bin/env python3
"""L-RED box 8 (produced on Opus 5.5), Lead 21:33Z depth construction: stack K copies of a game (each copy's priorities shifted
by an EVEN amount above the previous copy, so parity and in-copy order are kept) and add 1..CMAX random cross edges from a
vertex of copy j+1 to a vertex of copy j whose owner matches OWN (default: same owner as the source). Score each union with
root/depthfit.py (L-ALG dtl_stealdepth.analyze unmodified; LALGR_DIR, DTL_ORDER). Keeps every union with max depth >= 2 or
max k >= 3 and prints the best. Usage: dcompose.py SEED COUNT K CMAX OUTDIR G.pg"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import depthfit as DF
seed, cnt, K, cmax, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
h = DF.pg.read(sys.argv[6]); rng = random.Random(seed); os.makedirs(out, exist_ok=True); sys.setrecursionlimit(100000)
best = (-1,)
for it in range(cnt):
    prio, own, succ, shift, offs = [], [], [], 0, []
    for c in range(K):
        o = len(prio); offs.append(o); prio += [p + shift for p in h.prio]; own += list(h.owner); succ += [[w + o for w in s] for s in h.succ]
        shift = max(prio) + 1 + (max(prio) + 1) % 2
    edges = []
    for _ in range(rng.randint(1, cmax)):
        j = rng.randrange(K - 1); u = offs[j + 1] + rng.randrange(h.n); w = offs[j] + rng.randrange(h.n)
        succ[u] = sorted(set(succ[u]) | {w}); edges.append((u, w))
    g = DF.pg.Game(prio, own, [sorted(s) for s in succ])
    try: m = DF.measure_game(g, os.environ.get("DTL_ORDER", "stable"))
    except Exception as e: print(it, "ERR", e, flush=True); continue
    sc = (m["incomplete"], m["maxd"], m["maxk"], m["resteals"])
    print(it, sc, edges, flush=True)
    if m["incomplete"] or m["maxd"] >= 2 or m["maxk"] >= 3 or sc > best:
        best = max(best, sc)
        path = f"{out}/u{seed}_{it}.pg"
        with open(path, "w") as f:
            f.write(f"parity {len(prio) - 1};\n" + "".join(f"{v} {prio[v]} {own[v]} {','.join(map(str, sorted(succ[v])))};\n" for v in range(len(prio))))
print("best", best, flush=True)
