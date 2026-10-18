#!/usr/bin/env python3
"""L-RED box 11 (produced on Opus 5.5): GAP-C / correctness probe. Random small perturbations (1-4 of: add an edge, flip an
owner, change a priority by +-1..2) of Oink's hard-family generators (pinned tools/oink/build: counter_core, counter_dp,
counter_m, counter_ortl, counter_qpt, counter_rob, counter_rr, counter_symsi, tc, tc+) at small sizes; each game is solved by
pinned Oink `--dtl --no-single --no-wcwc --no-loops -v`. Any run without "solution verified" is saved and printed.
Usage: hfpert.py RNGSEED TRIES OUTDIR"""
import sys, os, random, subprocess, re
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tools", "oink", "build")
FAM = {"counter_core": [2, 3, 4], "counter_dp": [2, 3, 4], "counter_m": [2, 3, 4], "counter_ortl": [2, 3, 4], "counter_qpt": [2, 3],
       "counter_rob": [2, 3, 4], "counter_rr": [2, 3, 4], "counter_symsi": [2, 3], "tc": [2, 3, 4], "tc+": [1, 2, 3]}
def parse(txt):
    V = []
    for line in txt.splitlines():
        m = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)', line)
        if m: V.append([int(m[2]), int(m[3]), [int(x) for x in m[4].split(",")]])
    return V
seed, tries, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; rng = random.Random(seed); os.makedirs(out, exist_ok=True)
base = {}
for f, Ns in FAM.items():
    for N in Ns:
        try: base[(f, N)] = parse(subprocess.run([os.path.join(T, f), str(N)], capture_output=True, text=True, timeout=30).stdout)
        except Exception: pass
keys = [k for k, v in base.items() if len(v) > 1]; bad = ok = 0
for it in range(tries):
    k = rng.choice(keys); V = [[a, b, list(c)] for a, b, c in base[k]]; n = len(V)
    for _ in range(rng.randint(1, 4)):
        v = rng.randrange(n); t = rng.randrange(3)
        if t == 0: V[v][2] = sorted(set(V[v][2] + [rng.randrange(n)]))
        elif t == 1: V[v][1] ^= 1
        else: V[v][0] = max(0, V[v][0] + rng.choice([-2, -1, 1, 2]))
    p = os.path.join(out, f"cur{seed}.pg")
    with open(p, "w") as fh: fh.write(f"parity {n-1};\n" + "".join(f"{i} {a} {b} {','.join(map(str, c))};\n" for i, (a, b, c) in enumerate(V)))
    try: o = subprocess.run([os.path.join(T, "oink"), "--dtl", "--no-single", "--no-wcwc", "--no-loops", "-v", p, "/dev/null"], capture_output=True, text=True, timeout=60)
    except subprocess.TimeoutExpired: print("TIMEOUT", k, it, flush=True); continue
    txt = o.stdout + o.stderr
    if "solution verified" in txt: ok += 1
    else:
        bad += 1; q = os.path.join(out, f"bad_s{seed}_i{it}_{k[0]}_{k[1]}.pg"); os.replace(p, q); print("NOT VERIFIED", k, q, txt[-300:].replace("\n", " | "), flush=True)
print(f"done ok {ok} bad {bad}")
