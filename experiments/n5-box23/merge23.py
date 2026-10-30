#!/usr/bin/env python3
"""Box 23: merge exh23 part JSONs (counts summed, histograms summed, best = largest value, first part wins ties).
Usage: merge23.py OUT.json PART.json ..."""
import json, sys
out = None
for p in sys.argv[2:]:
    d = json.load(open(p))
    if out is None:
        out = dict(d); out["parts"] = []; out["seconds"] = 0
        out["counts"] = {k: 0 for k in d["counts"]}; out["hist"] = {k: {} for k in d["hist"]}; out["best"] = {k: None for k in d["best"]}
    out["parts"].append(f'{d["every"]}:{d["offset"]}'); out["seconds"] += d["seconds"]
    for k, v in d["counts"].items():
        out["counts"][k] += v
    for k, h in d["hist"].items():
        for x, c in h.items():
            out["hist"][k][x] = out["hist"][k].get(x, 0) + c
    for k, b in d["best"].items():
        if b is not None and (out["best"][k] is None or b[0] > out["best"][k][0]):
            out["best"][k] = b
out["every"], out["offset"] = 1, 0
json.dump(out, open(sys.argv[1], "w"), indent=1)
print("MERGED", len(out["parts"]), "parts", out["counts"], {k: (b[0] if b else None) for k, b in out["best"].items()}, "hist rs", out["hist"]["rs"], "fl", out["hist"]["fl"])
