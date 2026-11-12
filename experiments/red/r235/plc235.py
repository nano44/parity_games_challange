#!/usr/bin/env python3
"""L-RED 66 R235: kill-side climb on box 208 (LEVEL / PLATEAU / ALL-TCYC) with L-RED's own engine and counter (lv235.analyse).
Score (env SCORE): ratio = (max (v - u)/(movers of Y), maxplat, T); plat = (maxplat, maxratio, T); T = (T, maxplat); odd = (#Odd gate flips, T) (L-LIT T69 (a): steer toward Odd flips; oddquiet is must-0).
Mutations r230/mut230 (env NMAX, DMAX). Any must-0 counter > 0 (phifail, nocyc, qfail, tfail, platfail, sharpfail) freezes the genome
to OUT/FAIL_<tag>_<k>.json at once and prints FAIL. Checkpoint every 10 evals (OUT/best_<tag>.json; RESUME=1); log OUT/plc_<tag>.log.
Usage: plc235.py TAG SEED EVALS START.json"""
import sys, os, json, random, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r230"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mut230, lv235
tag, seed, evals, start = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
rng = random.Random(seed); mut230.set_rng(rng); OUT = os.environ.get("OUT", "out/plc"); os.makedirs(OUT, exist_ok=True)
SC = os.environ.get("SCORE", "ratio")
ck = os.path.join(OUT, f"best_{tag}.json"); lg = open(os.path.join(OUT, f"plc_{tag}.log"), "a")
if os.environ.get("RESUME") == "1" and os.path.exists(ck): cur = json.load(open(ck)); done0 = cur.pop("_evals", 0)
else: cur = json.load(open(start)); cur = cur.get("genome", cur); cur.pop("_evals", None); done0 = 0
MUST0 = ("phifail", "nocyc", "qfail", "tfail", "platfail", "sharpfail", "oddquiet", "k2flips"); fails = 0
def score(G):
    r = lv235.analyse(G)
    s = {"ratio": (r["maxratio"], r["maxplat"], r["T"]), "plat": (r["maxplat"], r["maxratio"], r["T"]), "T": (r["T"], r["maxplat"]), "odd": (r["oddflips"], r["T"])}[SC]
    return s, r
cs, r = score(cur); t0 = time.time(); print("start", cs, "N", cur["N"], file=lg, flush=True)
for e in range(done0, evals):
    nG = mut230.mutate(cur)
    try: s, r = score(nG)
    except Exception as ex: print("ERR", e, repr(ex)[:120], file=lg, flush=True); continue
    if any(r[k] for k in MUST0):
        fails += 1; json.dump(nG, open(os.path.join(OUT, f"FAIL_{tag}_{fails}.json"), "w")); print("FAIL", tag, e, r, flush=True)
        print("FAIL", e, r, file=lg, flush=True)
    if s >= cs:
        if s > cs: print(e, "score", s, "N", nG["N"], "M", r["M"], file=lg, flush=True)
        cur, cs = nG, s
    if e % 10 == 9: json.dump(dict(cur, _evals=e + 1), open(ck, "w"))
json.dump(dict(cur, _evals=evals), open(ck, "w"))
print(f"END {tag} best {cs} N {cur['N']} fails {fails} secs {time.time() - t0:.0f}", file=lg, flush=True); print(f"END {tag} best {cs} fails {fails}", flush=True)
