#!/usr/bin/env python3
"""L-RED 64 R230 item 5: climb N5'-xi's T3 on Gamma3 with PERMUTED e-priorities ([E-LEV] violated: inv > 0) and U(G) <= UMAX, size
N <= NMAX, degree <= DMAX. Score (T3, total) at the cap (compare bests across caps for growth). Mutations: mut230.mutate (structure),
or an ekey move (swap two options' keys / re-draw one); a mutant with U > UMAX or inv = 0 is rejected (not evaluated twice).
Checkpoint every 25 evals to OUT/bestel_<tag>.json + OUT/climbel_<tag>.log (RESUME=1). Any nstd > 0 is frozen to OUT/ELFAIL_<tag>_<k>.json.
Usage: climbel230.py TAG SEED EVALS START.json   env UMAX (2), NMAX, DMAX, OUT, CAP"""
import sys, os, json, random, time
import mut230
from elev230 import measure, fix_ekey, U
tag, seed, evals = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); mut230.set_rng(rng)
UMAX = int(os.environ.get("UMAX", "2")); OUT = os.environ.get("OUT", "out/elev"); os.makedirs(OUT, exist_ok=True)
ck = os.path.join(OUT, f"bestel_{tag}.json"); lg = open(os.path.join(OUT, f"climbel_{tag}.log"), "a")
if os.environ.get("RESUME") == "1" and os.path.exists(ck): cur = json.load(open(ck)); done0 = cur.pop("_evals", 0)
else: cur = json.load(open(sys.argv[4])); cur.pop("_evals", None); done0 = 0
cur = fix_ekey(cur, rng); c = measure(cur); cs = (c["T3"], c["total"]); fails = 0; t0 = time.time(); rej = 0
print("start", c, file=lg, flush=True)
for e in range(done0, evals):
    if rng.random() < 0.35:
        nG = json.loads(json.dumps(cur)); ek = nG["ekey"]; xs = [x for x in range(nG["N"]) if ek[x]]
        x, y = rng.choice(xs), rng.choice(xs); k, l = rng.randrange(len(ek[x])), rng.randrange(len(ek[y]))
        if rng.random() < 0.5: ek[x][k], ek[y][l] = ek[y][l], ek[x][k]
        else: ek[x][k] = rng.random()
    else:
        nG = mut230.mutate(cur); nG = fix_ekey(nG, rng)
    if U(nG) > UMAX: rej += 1; continue
    try: c = measure(nG)
    except Exception as ex: print("ERR", e, repr(ex)[:120], file=lg, flush=True); continue
    if c["inv"] == 0: rej += 1; continue
    if c["nstd"]:
        fails += 1; json.dump(nG, open(os.path.join(OUT, f"ELFAIL_{tag}_{fails}.json"), "w")); print("NSTD", tag, e, c, flush=True)
    s = (c["T3"], c["total"])
    if s >= cs:
        if s > cs: print(e, "score", s, c, file=lg, flush=True)
        cur, cs = nG, s
    if e % 25 == 24: json.dump(dict(cur, _evals=e + 1), open(ck, "w"))
json.dump(dict(cur, _evals=evals), open(ck, "w"))
print(f"END {tag} evals {evals} best (T3, total) {cs} N {cur['N']} M {sum(map(len, cur['opts']))} U {U(cur)} rejected {rej} nstd-fails {fails} secs {time.time() - t0:.0f}", flush=True)
print(f"END evals {evals} best {cs} rejected {rej} fails {fails}", file=lg, flush=True)
