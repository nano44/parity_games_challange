#!/usr/bin/env python3
"""L-RED 65 R231 item 1: k = 1 kill-side climb on L-RED's own engine (dep231.measure + blk231.analyse; no L-NEW code).
Objective OBJ: dmov -> (must-0 fails, D_mov, T); q1 -> (must-0 fails, Q_(>1), T); t -> (must-0 fails, T, D_mov).
Mutations: r230/mut230.mutate; a mutant with min-FVS(Xi) != 1 is rejected. Size N <= NMAX, degree <= DMAX.
Any must-0 fail is frozen to OUT/FAIL_<tag>_<k>.json and printed. Checkpoint every 25 evals to OUT/best_<tag>.json + OUT/climb_<tag>.log;
RESUME=1 continues from the checkpoint. Usage: climb231.py TAG SEED EVALS START.json   env OBJ, NMAX, DMAX, OUT"""
import sys, os, json, random, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r230"))
import mut230
from dep231 import measure, MUST0
from blk231 import analyse, xi_k
tag, seed, evals = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); mut230.set_rng(rng)
OBJ = os.environ.get("OBJ", "dmov"); OUT = os.environ.get("OUT", "out/climb"); os.makedirs(OUT, exist_ok=True)
ck = os.path.join(OUT, f"best_{tag}.json"); lg = open(os.path.join(OUT, f"climb_{tag}.log"), "a")
if os.environ.get("RESUME") == "1" and os.path.exists(ck): cur = json.load(open(ck)); done0 = cur.pop("_evals", 0)
else: cur = json.load(open(sys.argv[4])); cur.pop("_evals", None); done0 = 0
def ev(G):
    c = measure(G); A = analyse(G); N = G["N"]
    c["Dmov"] = max(len(set(A["cls"][x])) for x in range(N)); c["Dtop"] = max(len(set(A["blk"][x])) for x in range(N)); c["b"] = A["b"]
    f = sum(c[k] for k in MUST0)
    s = {"dmov": (f, c["Dmov"], c["T"]), "q1": (f, c["Q>1"], c["T"]), "t": (f, c["T"], c["Dmov"])}[OBJ]
    return s, c
cs, c = ev(cur); fails = 0; rej = 0; t0 = time.time()
print("start", cs, {k: c[k] for k in ("N", "M", "T", "Q", "Q>1", "Dmov", "Dtop", "b", "hist")}, file=lg, flush=True)
for e in range(done0, evals):
    nG = mut230.mutate(cur)
    if xi_k(nG) != 1: rej += 1; continue
    try: s, c = ev(nG)
    except Exception as ex: print("ERR", e, repr(ex)[:120], file=lg, flush=True); continue
    if s[0]:
        fails += 1; json.dump(nG, open(os.path.join(OUT, f"FAIL_{tag}_{fails}.json"), "w")); print("FAIL", tag, e, c, flush=True)
    if s >= cs:
        if s > cs: print(e, "score", s, {k: c[k] for k in ("N", "M", "T", "Q", "Q>1", "Dmov", "Dtop", "b", "hist")}, file=lg, flush=True)
        cur, cs = nG, s
    if e % 25 == 24: json.dump(dict(cur, _evals=e + 1), open(ck, "w"))
json.dump(dict(cur, _evals=evals), open(ck, "w"))
print(f"END {tag} OBJ {OBJ} evals {evals} best {cs} N {cur['N']} M {sum(map(len, cur['opts']))} rejected {rej} fails {fails} secs {time.time() - t0:.0f}", file=lg, flush=True)
print(f"END {tag} best {cs} fails {fails}", flush=True)
