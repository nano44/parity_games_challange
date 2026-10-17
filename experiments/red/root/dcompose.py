#!/usr/bin/env python3
"""L-RED box 8 (produced on Opus 5.5), Lead 21:33Z depth construction: stack K copies of a game (each copy's priorities shifted
by an EVEN amount above the previous copy, so parity and in-copy order are kept) and add 1..CMAX random cross edges from a
vertex of copy j+1 to a vertex of copy j whose owner matches OWN (default: same owner as the source). Score each union with
root/depthfit.py (L-ALG dtl_stealdepth.analyze unmodified; LALGR_DIR, DTL_ORDER). Keeps every union with max depth >= 2 or
max k >= 3 and prints the best. Usage: dcompose.py SEED COUNT K CMAX OUTDIR G.pg
MIXED=1: the parts are the given files G1.pg G2.pg ... in a random stacking order (K ignored), and each cross edge joins two
random distinct parts in a random direction (e.g. the R35 core plus L-ALG's dtl_chainfam UP clock)."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import depthfit as DF
seed, cnt, K, cmax, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
hs = [DF.pg.read(f) for f in sys.argv[6:]]; h = hs[0]; rng = random.Random(seed); os.makedirs(out, exist_ok=True); sys.setrecursionlimit(100000)
best = (-1,)
for it in range(cnt):
    prio, own, succ, shift, offs = [], [], [], 0, []
    parts = rng.sample(hs, len(hs)) if os.environ.get("MIXED") == "1" else [h] * K
    for hp in parts:
        o = len(prio); offs.append((o, hp.n)); prio += [p + shift for p in hp.prio]; own += list(hp.owner); succ += [[w + o for w in s] for s in hp.succ]
        shift = max(prio) + 1 + (max(prio) + 1) % 2
    edges = []
    for _ in range(rng.randint(1, cmax)):
        if os.environ.get("MIXED") == "1": a, b = rng.sample(range(len(parts)), 2)
        else: j = rng.randrange(len(parts) - 1); a, b = j + 1, j
        u = offs[a][0] + rng.randrange(offs[a][1]); w = offs[b][0] + rng.randrange(offs[b][1])
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
