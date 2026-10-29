#!/usr/bin/env python3
"""Box 17: merge exh17 part JSONs (same n, model, starts) into one table. Usage: merge.py OUT.json PART.json ..."""
import json, sys
P = [json.load(open(f)) for f in sys.argv[2:]]; o = dict(P[0]); o["parts"] = [f"{p['every']}:{p['offset']}" for p in P]
assert len({(p["n"], p["model"], p["all_starts"], p["every"]) for p in P}) == 1 and sorted(p["offset"] for p in P) == list(range(P[0]["every"]))
o["counts"] = {k: sum(p["counts"][k] for p in P) for k in P[0]["counts"]}; o["seconds"] = sum(p["seconds"] for p in P); o["every"], o["offset"] = 1, 0
for k in P[0]["best"]:
    bs = [p["best"][k] for p in P if p["best"][k]]; o["best"][k] = max(bs, key=lambda b: b[0]) if bs else None
    h = {}
    for p in P:
        for x, c in p["hist"][k].items(): h[x] = h.get(x, 0) + c
    o["hist"][k] = dict(sorted(h.items(), key=lambda t: int(t[0])))
o["violations"] = sum((p["violations"] for p in P), [])
json.dump(o, open(sys.argv[1], "w"), indent=1)
print("MERGED", json.dumps(dict(n=o["n"], counts=o["counts"], max={k: (b[0] if b else None) for k, b in o["best"].items()}, hist=o["hist"], violations=len(o["violations"]))))
