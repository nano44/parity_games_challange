#!/usr/bin/env python3
"""Box 42: fbx18.analyse on library files × (S3 + R random start pairs). Failing (file, start) saved to OUT_<check>.json.
Usage: libst18.py seed R OUT file.pg ..."""
import sys, os, random, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import fbx18, sox
seed, R, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; rng = random.Random(seed); acc = {}; saved = set()
for f in sys.argv[4:]:
    try: g = sox.load(f)
    except Exception: continue
    if len(sox.oddchoice(g)) != 1 or g.n > 70: continue
    for r in range(R + 1):
        st = None if r == 0 else [rng.choice(g.succ[v]) for v in range(g.n)]
        before = dict(acc)
        try: fbx18.analyse(g, acc, os.path.basename(f), st)
        except AssertionError: continue
        for k, v in acc.items():
            if k.startswith("FAIL_") and v > before.get(k, 0) and k not in saved:
                saved.add(k); json.dump(dict(file=f, start=st), open(f"{out}_{k}.json", "w")); print("HIT", k, f, flush=True)
print(json.dumps(acc, sort_keys=True), flush=True)
