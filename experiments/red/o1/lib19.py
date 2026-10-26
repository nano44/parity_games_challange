#!/usr/bin/env python3
"""Box 45: o1_19.analyse on library files (𝒞^1O only, n ≤ NMAX) × (S3 start + R random start pairs), Oink on every run.
Usage: lib19.py seed R NMAX OUT [--of] files...   (prints per-file max line and a final summary; OUT_best.json, OUT_FAIL_*.json)"""
import sys, os, json, random, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import o1_19 as O, pg
a = [x for x in sys.argv[1:] if x != "--of"]; mode = "of" if "--of" in sys.argv else "n5"
seed, R, NMAX, out, files = int(a[0]), int(a[1]), int(a[2]), a[3], a[4:]
rng = random.Random(seed); tmp = tempfile.mkdtemp(); best = {}; fails = {}; runs = files_used = 0
keys = ("ITER", "ITERn", "PH", "Tmax", "Tn", "fmax", "fslack", "fslackhat", "fcap", "TAU", "Thmax", "Somax")
for f in files:
    try: g = pg.parse("".join(l for l in open(f) if not l.lstrip().startswith("%")))
    except Exception: continue
    if len(O.oddchoice(g)) != 1 or g.n > NMAX: continue
    files_used += 1
    for k in range(R + 1):
        st = None if k == 0 else [rng.choice(g.succ[v]) for v in range(g.n)]
        r = O.analyse(g, st, mode, tmp, True); runs += 1; r["ITERn"] = r["ITER"] / g.n
        for x in r["fails"]:
            fails[x.split()[0]] = fails.get(x.split()[0], 0) + 1; print("FAIL", f, x, st, flush=True)
            json.dump(dict(file=f, start=st, r=r), open(f"{out}_FAIL_{x.split()[0]}.json", "w"))
        for kk in keys:
            if kk not in best or r[kk] > best[kk][0]: best[kk] = (r[kk], dict(file=f, start=st, r=r))
json.dump({k: v[1] for k, v in best.items()}, open(out + "_best.json", "w"))
print("FILES", files_used, "RUNS", runs, "FAILS", fails, {k: (v[0], os.path.basename(v[1]["file"]), v[1]["start"] is None) for k, v in best.items()}, flush=True)
