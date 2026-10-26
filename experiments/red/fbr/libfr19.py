#!/usr/bin/env python3
"""Box 45b: fbr19.analyse (FB-RED, late form, CN-ONLY, ACCEL (a), (SG), levels) on library files (any class, n <= NMAX) × (S3 + R
random start pairs). Usage: libfr19.py seed R NMAX OUT files..."""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import fbr19, pg
seed, R, NMAX, out, files = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5:]
rng = random.Random(seed); best = {}; fails = {}; runs = used = 0; tot = dict(sg=0, acc=0)
for f in files:
    try: g = pg.parse("".join(l for l in open(f) if not l.lstrip().startswith("%")))
    except Exception: continue
    if g.n > NMAX: continue
    used += 1
    for k in range(R + 1):
        st = None if k == 0 else [rng.choice(g.succ[v]) for v in range(g.n)]
        try: r = fbr19.analyse(g, st, cap=5000)
        except Exception as e: print("ERR", f, e); continue
        runs += 1; tot["sg"] += r["sg_checks"]; tot["acc"] += r["acc_checks"]; r["levels_n"] = r["levels"] / g.n; r["Nep_n"] = r["Nep"] / g.n
        for x in r["fails"]:
            fails[x.split()[0]] = fails.get(x.split()[0], 0) + 1
            if fails[x.split()[0]] <= 3: print("FAIL", f, x, st, flush=True); json.dump(dict(file=f, start=st, r=r), open(f"{out}_FAIL_{x.split()[0]}.json", "w"))
        for kk in ("fmax", "fn", "rhomax", "levels", "levels_n", "sw_trans", "late", "Nep", "Nep_n", "s4a_run", "s4a_run_pre", "sigbar_repeat", "epoch_n1"):
            if kk not in best or r[kk] > best[kk][0]: best[kk] = (r[kk], dict(file=f, start=st))
json.dump({k: v for k, v in best.items()}, open(out + "_best.json", "w"))
print("FILES", used, "RUNS", runs, "CHECKS", tot, "FAILS", fails, {k: (v[0], os.path.basename(v[1]["file"]), v[1]["start"] is None) for k, v in best.items()}, flush=True)
