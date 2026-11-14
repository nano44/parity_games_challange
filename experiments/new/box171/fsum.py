#!/usr/bin/env python3
"""summary of frozen.py data by degree and number of levels d: max #top-only intervals, with argmax and its lower-step count.
Usage: fsum.py file.json ..."""
import os, sys, json
H_ = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H_, "..", "box165", "permover.py")).read().split("\nif __name__")[0])
best = {}
for f in sys.argv[1:]:
    try: G = json.load(open(f)); assert "N" in G; S, _ = Gen(G).run(G["start"])
    except Exception: continue
    top = max(G["lev"]); low = [v for v in range(G["N"]) if G["lev"][v] < top]; D = max(len(o) for o in G["opts"])
    k = "".join("L" if any(S[t][v] != S[t - 1][v] for v in low) else "T" for t in range(1, len(S)))
    I = sum(1 for i, c in enumerate(k) if c == "T" and (i == 0 or k[i - 1] == "L")); key = (D, top + 1)
    if I > best.get(key, (-1,))[0]: best[key] = (I, os.path.basename(f), len(S) - 1, k.count("L"))
for key in sorted(best): print("deg %d d %d: max top-only intervals %d (%s, T %d, lower steps %d)" % (*key, *best[key]))
