#!/usr/bin/env python3
"""L-ALG (2026-10-15, DTL step 4, step (r1) of DTL-proof.md §2.3): is the stable best-vertex set of the FIRST best_vertices call of search s (empty if that call
returned -1) contained in that of the next search of the same player (on the vertices still unsolved)? Parses `oink --dtl -t -t` ("iteration k-even",
"current region: ...", "best vertices: ... (stable)"). Usage: dtl_monotone.py OINK RNGAME N_GAMES SEED [games...]
Prints violations (game saved to OUTDIR) and a summary. A violation is a candidate non-monotone pruning (NOTE N5)."""
import sys, os, re, subprocess, random
oink, rngame, N, seed = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
extra = sys.argv[5:]
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "out", "dtl_monotone"); os.makedirs(outdir, exist_ok=True)
rng = random.Random(seed)
def analyse(path):
    r = subprocess.run([oink, "--dtl", "-t", "-t", "--no-single", "--no-wcwc", path], capture_output=True, text=True, timeout=300)
    out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
    searches = []  # (player, region set, first stable set or None)
    cur = None
    for line in out.splitlines():
        m = re.search(r"iteration (\d+)-(even|odd)", line)
        if m: cur = [m.group(2), None, None]; searches.append(cur); continue
        if cur is None: continue
        m = re.search(r"current region:(.*)", line)
        if m and cur[1] is None: cur[1] = set(m.group(1).split()); continue
        m = re.search(r"best vertices:(.*)", line)
        if m and cur[2] is None:   # FIRST best_vertices call of the search (on the full unsolved region)
            cur[2] = set(m.group(1).replace("(stable)", "").split()) if "(stable)" in line else set(); continue
    viol = []
    for i in range(len(searches)):
        for j in range(i + 1, len(searches)):
            if searches[j][0] != searches[i][0]: continue
            a, b = searches[i], searches[j]
            if a[2] is None or b[2] is None or b[1] is None: break
            lost = {v for v in a[2] if v in b[1] and v not in b[2]}
            if lost: viol.append((i, j, sorted(lost)))
            break
    return viol, len(searches)
tot = 0; nv = 0
games = list(extra)
for i in range(N):
    n = rng.randint(5, 14); g = subprocess.run([rngame, str(n), str(rng.randint(2, n)), "1", str(rng.randint(1, 3))], capture_output=True, text=True).stdout
    path = os.path.join(outdir, "cur.pg"); open(path, "w").write(g); games.append(path)
for k, path in enumerate(games):
    viol, ns = analyse(path); tot += 1
    if viol:
        nv += 1; keep = os.path.join(outdir, f"viol_{seed}_{k}.pg")
        if path.endswith("cur.pg"): open(keep, "w").write(open(path).read())
        else: keep = path
        print("VIOLATION", keep, "searches", ns, viol[:3], flush=True)
print(f"done: {tot} games, {nv} with a non-monotone first stable set")
