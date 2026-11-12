#!/usr/bin/env python3
"""L-RED 66 R234 item 3: kill-side climb on CONJECTURE DEEP3 (L-SI 51 box 100 §5.2). Score = (deepC, soft): deepC = sum over SCCs C of
Deep_c(C) (internal-gate flips after t0(C) charged to a change of depth > c; deep234.one), soft = sum of max(0, depth) over the
internal flips after t0 (a gradient). Mutations r230/mut230 (env NMAX, DMAX). Start: START.json or "rand:d,w,D" (r231 dep231.rgen).
Checkpoint every 10 evals (OUT/best_<tag>.json; RESUME=1), log OUT/dclimb_<tag>.log; every new best deepC is frozen to
OUT/deep_<tag>_<deepC>.json. Usage: dclimb234.py TAG SEED EVALS START"""
import sys, os, json, random, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r230"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r231"))
import deep234
import mut230
tag, seed, evals, start = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
rng = random.Random(seed); mut230.set_rng(rng); OUT = os.environ.get("OUT", "out/dclimb"); os.makedirs(OUT, exist_ok=True)
ck = os.path.join(OUT, f"best_{tag}.json"); lg = open(os.path.join(OUT, f"dclimb_{tag}.log"), "a")
if os.environ.get("RESUME") == "1" and os.path.exists(ck): cur = json.load(open(ck)); done0 = cur.pop("_evals", 0)
elif start.startswith("rand:"):
    from dep231 import rgen
    d, w, D = map(int, start[5:].split(",")); cur = rgen(rng, d, w, D); done0 = 0
else: cur = json.load(open(start)); cur = cur.get("genome", cur); cur.pop("_evals", None); done0 = 0
def score(G):
    o = deep234.one(G, soft=True); return (o["deepC"], o["soft"]), o
cs, o = score(cur); t0 = time.time(); print("start", cs, "N", cur["N"], file=lg, flush=True); bestd = cs[0]
for e in range(done0, evals):
    nG = mut230.mutate(cur)
    try: s, o = score(nG)
    except Exception as ex: print("ERR", e, repr(ex)[:120], file=lg, flush=True); continue
    if s >= cs:
        if s > cs: print(e, "score", s, "N", nG["N"], "M", sum(len(v) for v in nG["opts"]), "T3", o["T3"], file=lg, flush=True)
        cur, cs = nG, s
        if s[0] > bestd: bestd = s[0]; json.dump(nG, open(os.path.join(OUT, f"deep_{tag}_{s[0]}.json"), "w"))
    if e % 10 == 9: json.dump(dict(cur, _evals=e + 1), open(ck, "w"))
json.dump(dict(cur, _evals=evals), open(ck, "w"))
print(f"END {tag} best {cs} N {cur['N']} secs {time.time() - t0:.0f}", file=lg, flush=True); print(f"END {tag} best {cs} N {cur['N']}", flush=True)
