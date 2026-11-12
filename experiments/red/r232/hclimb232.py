#!/usr/bin/env python3
"""L-RED 65 R232 (c): kill-side climb on CONJECTURE SCC-LIN (L-SI 50 box 99). Genomes whose D(G) is ONE SCC; score = (H - M_C, H) with
H = max over ALL mover start vectors of the own-engine HOW3 length (how3_232.how3; full enumeration, genomes with > SMAX starts rejected).
Mutations r230/mut230.mutate (NMAX, DMAX env). Any H > M_C is frozen at once to OUT/SCCLIN_FAIL_<tag>_<k>.json and printed.
Checkpoint every 10 evals (OUT/best_<tag>.json, log OUT/hclimb_<tag>.log; RESUME=1). Usage: hclimb232.py TAG SEED EVALS START.json"""
import sys, os, json, random, itertools, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r230"))
import mut230
from how3_232 import how3, sccs
tag, seed, evals = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); mut230.set_rng(rng)
OUT = os.environ.get("OUT", "out/hclimb"); SMAX = int(os.environ.get("SMAX", "3000")); os.makedirs(OUT, exist_ok=True)
ck = os.path.join(OUT, f"best_{tag}.json"); lg = open(os.path.join(OUT, f"hclimb_{tag}.log"), "a")
if os.environ.get("RESUME") == "1" and os.path.exists(ck): cur = json.load(open(ck)); done0 = cur.pop("_evals", 0)
else: cur = json.load(open(sys.argv[4])); cur.pop("_evals", None); done0 = 0
def score(G):
    cs, _, _ = sccs(G)
    if len(cs) != 1: return None
    degs = [len(o) for o in G["opts"]]; tot = 1
    for d in degs: tot *= d
    if tot > SMAX: return None
    M = sum(degs); H = max(len(how3(G, start=list(s))) - 1 for s in itertools.product(*[range(d) for d in degs]))
    return (H - M, H, -M)
cs_ = score(cur); fails = 0; rej = 0; t0 = time.time()
print("start", cs_, "N", cur["N"], file=lg, flush=True)
for e in range(done0, evals):
    nG = mut230.mutate(cur)
    try: s = score(nG)
    except Exception as ex: print("ERR", e, repr(ex)[:100], file=lg, flush=True); continue
    if s is None: rej += 1; continue
    if s[0] > 0:
        fails += 1; json.dump(nG, open(os.path.join(OUT, f"SCCLIN_FAIL_{tag}_{fails}.json"), "w")); print("SCCLIN FAIL", tag, e, s, "N", nG["N"], flush=True)
    if s >= cs_:
        if s > cs_: print(e, "score", s, "N", nG["N"], "M", -s[2], file=lg, flush=True)
        cur, cs_ = nG, s
    if e % 10 == 9: json.dump(dict(cur, _evals=e + 1), open(ck, "w"))
json.dump(dict(cur, _evals=evals), open(ck, "w"))
print(f"END {tag} best {cs_} N {cur['N']} rejected {rej} fails {fails} secs {time.time() - t0:.0f}", file=lg, flush=True)
print(f"END {tag} best {cs_} fails {fails}", flush=True)
