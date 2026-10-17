#!/usr/bin/env python3
"""Containment of HKP's classes in PA* on ALL canonical n-vertex games of those classes (Buchi, SCC-constant, deterministic),
plus greedy == PA* on them. Usage: classes_n4.py n"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pg, a1lib, peeling, zielonka
n = int(sys.argv[1])
cnt, bad = {}, {}
for cfg, m in a1lib.succ_orbits(n):
    for g in a1lib.games_on(cfg, n):
        cl = peeling.classes(g)
        if not any(cl.values()):
            continue
        ref = zielonka.solve(g)
        ps = peeling.both(g, ref, peeling.peeling)
        gr = peeling.both(g, ref, peeling.greedy)
        for c, v in cl.items():
            if v:
                cnt[c] = cnt.get(c, 0) + 1
                if not ps:
                    bad[c] = bad.get(c, 0) + 1
                    if bad[c] <= 3: print(f"{c}: PA* FALSE on", pg.dumps(g).replace("\n", " | "), flush=True)
        if ps != gr:
            cnt["greedy!=PA*"] = cnt.get("greedy!=PA*", 0) + 1
            if cnt["greedy!=PA*"] <= 3: print("greedy != PA*:", pg.dumps(g).replace("\n", " | "), ps, gr, flush=True)
print(f"n={n}: class sizes {cnt}; PA* false counts {bad}")
