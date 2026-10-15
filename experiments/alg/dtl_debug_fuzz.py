#!/usr/bin/env python3
"""L-ALG (2026-10-15): completeness oracle for DTL. Runs a DEBUG build of Oink (NDEBUG off: dtl.cpp 1146-1151 throws
"search was incomplete!" if run() ends with unsolved vertices; with -t, a dominion at recursion depth != 0 exits -1 at
dtl.cpp 349-355) on random games from Oink's rngame and reports any run that does not end with "solution verified".
Usage: dtl_debug_fuzz.py DEBUG_OINK RNGAME OUTDIR N_GAMES [seed]; env DTL_NO_LOOPS=1 adds --no-loops (pinned A_DTL)  (games: n in 4..12, priorities <= n, degree 1..3).
Prints one line per failure (kind, seed, file) and a summary. Debug build: cmake -DCMAKE_BUILD_TYPE=Debug of tools/oink/src."""
import sys, os, subprocess, random
oink, rngame, outdir, N = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
seed = int(sys.argv[5]) if len(sys.argv) > 5 else 1
os.makedirs(outdir, exist_ok=True)
rng = random.Random(seed)
fails = 0
for i in range(N):
    n = rng.randint(4, 12); maxp = rng.randint(2, n); mind = 1; maxd = rng.randint(1, 3)
    g = subprocess.run([rngame, str(n), str(maxp), str(mind), str(maxd)], capture_output=True, text=True).stdout
    path = os.path.join(outdir, "cur.pg"); open(path, "w").write(g)
    for solver in ("dtl", "idtl"):
        r = subprocess.run([oink, f"--{solver}", "-v", "-t", "--no-single", "--no-wcwc"] + (["--no-loops"] if os.environ.get("DTL_NO_LOOPS") else []) + [path], capture_output=True, text=True, timeout=60)
        out = r.stdout + r.stderr
        if r.returncode != 0 or "solution verified" not in out:
            fails += 1; keep = os.path.join(outdir, f"fail_{solver}_{seed}_{i}.pg"); open(keep, "w").write(g)
            kind = "incomplete" if "incomplete" in out else ("logic_error" if "LOGIC" in out or r.returncode == 255 else f"rc={r.returncode}")
            print("FAIL", solver, kind, keep, out.strip().splitlines()[-1][:120] if out.strip() else "", flush=True)
print(f"done: {N} games x dtl,idtl, seed {seed}, failures {fails}")
