#!/usr/bin/env python3
"""Box 46: rec0_20.analyse on (lib) library files × (S3 + R random start pairs), or (rand) random games with |Q| >= QMIN for SECS seconds.
FAIL dumps: OUT_FAIL_<kind>_<i>.json (at most 3 per kind; the failing run is re-run with Oink and both results are stored).
Usage: rrec0_20.py lib seed R NMAX OUT files...  |  rrec0_20.py rand seed secs nmin nmax QMIN R OUT"""
import sys, os, json, random, time, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rec0_20 as R0, pg
KEYS = ("N0", "N0f", "slack", "kind3", "kind3gap", "kind3all", "span", "spangap", "pre", "pregap", "post", "Nep", "fmax")
tmp = tempfile.mkdtemp(); best = {}; fails = {}; runs = 0; tot = dict(lvl=0, step1=0, ovf=0, phases=0, fbD0=0, fb=0)

def record(g, st, r, tag, out):
    global runs
    runs += 1; tot["lvl"] += r["lvl_checks"]; tot["step1"] += r["step1"]; tot["ovf"] += r["overflow"]; tot["phases"] += r["phases"]; tot["fbD0"] += r.get("fbD0", 0); tot["fb"] += r.get("fbany", 0)
    for x in r["fails"]:
        kk = x.split()[0]; fails[kk] = fails.get(kk, 0) + 1
        if fails[kk] <= 3:
            r2 = R0.analyse(g, st, True, tmp=tmp)
            json.dump(dict(tag=tag, prio=g.prio, owner=g.owner, succ=g.succ, start=st, r=r, r_oink=r2), open(f"{out}_FAIL_{kk}_{fails[kk]}.json", "w"))
            print("FAIL", tag, x, flush=True)
    for kk in KEYS:
        if kk in r and (kk not in best or r[kk] > best[kk][0]): best[kk] = (r[kk], dict(tag=tag, prio=g.prio, owner=g.owner, succ=g.succ, start=st))

def randgame(rng, nmin, nmax, qmin):
    while True:
        n = rng.randint(nmin, nmax)
        prio = [rng.randrange(2 * n) for _ in range(n)]; owner = [0 if rng.random() < 0.6 else 1 for _ in range(n)]
        succ = [sorted(set(rng.sample(range(n), rng.choice((1, 1, 2)) if owner[v] else rng.choice((1, 2, 2, 3))))) for v in range(n)]
        g = pg.Game(prio, owner, succ)
        if sum(1 for v in range(n) if owner[v] == 1 and len(succ[v]) > 1) >= qmin: return g

a = sys.argv
if a[1] == "lib":
    seed, Rn, NMAX, out, files = int(a[2]), int(a[3]), int(a[4]), a[5], a[6:]; rng = random.Random(seed)
    for f in files:
        try: g = pg.parse("".join(l for l in open(f) if not l.lstrip().startswith("%")))
        except Exception: continue
        if g.n > NMAX: continue
        for k in range(Rn + 1):
            st = None if k == 0 else [rng.choice(g.succ[v]) for v in range(g.n)]
            try: r = R0.analyse(g, st, False)
            except Exception as e: print("ERR", f, repr(e), flush=True); continue
            record(g, st, r, f, out)
else:
    seed, secs, nmin, nmax, qmin, Rn, out = int(a[2]), float(a[3]), int(a[4]), int(a[5]), int(a[6]), int(a[7]), a[8]
    rng = random.Random(seed); t0 = time.time()
    while time.time() - t0 < secs:
        g = randgame(rng, nmin, nmax, qmin)
        for k in range(Rn + 1):
            st = None if k == 0 else [rng.choice(g.succ[v]) for v in range(g.n)]
            record(g, st, R0.analyse(g, st, False), "rand", out)
json.dump({k: v[1] for k, v in best.items()}, open(out + "_best.json", "w"))
print("RUNS", runs, "TOT", tot, "FAILS", fails, {k: v[0] for k, v in best.items()}, flush=True)
