#!/usr/bin/env python3
"""L-RED box 11 (produced on Opus 5.5): (DEEP-STAB) check on structured games: random tcpert rule sets (1-4 parts, cut/loop
rules included) on tc(N), reference model via depthscan.scan in the given order. Prints violations (FIRST-BV-1 > 0) and a
summary of depth >= 1 births. Usage: lemmatc.py SEED TRIES N OUTDIR"""
import sys, os, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H); sys.path.insert(0, os.path.join(H, "..", "tcpert"))
os.environ["TCP_EXT"] = "1"
import depthscan as DS, tcpert as T, pg
seed, tries, N, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
os.makedirs(out, exist_ok=True); base = T.gen(N); games = deep = born = 0
for it in range(tries):
    rule = []
    for _ in range(rng.randint(1, 2)): rule += list(T.randrule(rng))
    V = T.apply(base, rule); g = pg.Game([v[0] for v in V], [v[1] for v in V], [v[2] for v in V])
    try: d = DS.scan(g)
    except RecursionError: continue
    games += 1; b = DS.deepborn(d); born += b; deep += 1 if b else 0
    if DS.firstbv1(d):
        f = os.path.join(out, f"viol_s{seed}_i{it}.pg"); pg.write(g, f); print("VIOLATION", rule, f, flush=True)
print(f"done games {games} with-depth>=1-births {deep} births {born}")
