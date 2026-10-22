#!/usr/bin/env python3
"""L-RED (Opus 5.5): depth-0 transition levels per phase, with context ids (to see FRESH vs revisited contexts, L-ALG F_j).
For consecutive same-player searches with no dominion found: level j = first depth-0 piece whose (R, kind, V) differs;
prints j and the id of R_j (first-seen order) for every transition; '*' = no depth-0 difference. Usage: levels.py GAME.pg"""
import sys, os, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ff", os.path.join(HERE, "..", "dtl", "dtl_flipflop.py"))
ff = importlib.util.module_from_spec(spec); spec.loader.exec_module(ff)
d = ff.load(sys.argv[1], "oink")
ids = {}; prev = None; line = []
print(f"n={d.n} tangles={d.tangles} dominions={d.dominions} iterations={d.iterations}")
for sr in d.searches:
    d0 = [p for p in sr["pieces"] if p["depth"] == 0]
    if prev is not None and prev["player"] == sr["player"] and not prev["dominions"] and prev["G"] == sr["G"]:
        pa = [p for p in prev["pieces"] if p["depth"] == 0]
        j = 0
        while j < min(len(pa), len(d0)) and (pa[j]["bv"]["R"], pa[j]["kind"], pa[j].get("V")) == (d0[j]["bv"]["R"], d0[j]["kind"], d0[j].get("V")):
            j += 1
        if j < min(len(pa), len(d0)):
            key = (j, pa[j]["bv"]["R"]); ids.setdefault(key, len([k for k in ids if k[0] == j]))
            line.append(f"{j}:{'c' if pa[j]['bv']['R'] == d0[j]['bv']['R'] else 'R'}{ids[key]}")
        else:
            line.append("*")
    elif prev is not None:
        print(f"  player {prev['player']} phase:", " ".join(line)); line = []
    prev = sr
print(f"  player {prev['player']} phase:", " ".join(line))
print("  (j:cK = change at level j in its K-th distinct level-j context; j:RK = the context itself differed)")
