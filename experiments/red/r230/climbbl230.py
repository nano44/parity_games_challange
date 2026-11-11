#!/usr/bin/env python3
"""L-RED 64 R230 item 4: hill climb for a BETA-LOC / NOCYC-NOFLIP / K1-BASIN failure on IDEAL-CYC (betaloc230.measure, own engine).
Score lexicographic (bfail + nfail + kfail, ctrl, flips): ctrl = e-face pairs with premise (i) only (near-miss to bfail), flips = gate
flips. Mutations: mut230.mutate (NMAX, DMAX env). Accept if score >= current. Checkpoint every 50 evals to OUT/bestbl_<tag>.json +
OUT/climbbl_<tag>.log; RESUME=1 restarts from it. A failure is frozen at once to OUT/BLFAIL_<tag>_<k>.json.
Usage: climbbl230.py TAG SEED EVALS [START.json]"""
import sys, os, json, random, time
import mut230
from betaloc230 import measure, score
from bonly3_230 import rgen
tag, seed, evals = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); mut230.set_rng(rng)
OUT = os.environ.get("OUT", "out/climb"); os.makedirs(OUT, exist_ok=True)
ck = os.path.join(OUT, f"bestbl_{tag}.json"); lg = open(os.path.join(OUT, f"climbbl_{tag}.log"), "a")
if os.environ.get("RESUME") == "1" and os.path.exists(ck): cur = json.load(open(ck)); done0 = cur.pop("_evals", 0)
elif len(sys.argv) > 4: cur = json.load(open(sys.argv[4])); cur.pop("_evals", None); done0 = 0
else: cur = rgen(rng, 2, 2, 2); done0 = 0
cur = mut230.renum(cur); cs = score(measure(cur)); fails = 0; t0 = time.time()
for e in range(done0, evals):
    nG = mut230.mutate(cur)
    try: c = measure(nG, cap=3000)
    except Exception as ex: print("ERR", e, repr(ex)[:120], file=lg, flush=True); continue
    s = score(c)
    if s[0] > 0:
        fails += 1; json.dump(nG, open(os.path.join(OUT, f"BLFAIL_{tag}_{fails}.json"), "w")); print("FAIL", tag, e, c, flush=True); print("FAIL", e, c, file=lg, flush=True)
    if s >= cs:
        if s > cs: print(e, "score", s, "N", c["N"], "M", c["M"], "states", c["states"], file=lg, flush=True)
        cur, cs = nG, s
    if e % 50 == 49: json.dump(dict(cur, _evals=e + 1), open(ck, "w"))
json.dump(dict(cur, _evals=evals), open(ck, "w"))
print(f"END {tag} evals {evals} best score {cs} N {cur['N']} fails {fails} secs {time.time() - t0:.0f}", flush=True)
print(f"END evals {evals} best {cs} fails {fails}", file=lg, flush=True)
