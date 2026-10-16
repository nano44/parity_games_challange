#!/usr/bin/env python3
"""L-ALG (2026-10-15, GAP-A later pieces): with a patched debug Oink that prints "ITER depth d R: v1 v2 ..." at the start of
every search_rec iteration, assign each vertex its depth-0 piece index in a search = the number of the depth-0 iteration
after which it is no longer in R (vertices never removed get index = #iterations + 1). Test, for consecutive same-player
searches s < s', that index_{s'}(v) <= index_s(v) for every vertex unsolved in s' ("pieces refine"). Usage:
dtl_pieces_monotone.py PATCHED_OINK RNGAME N SEED [games...]; recipe for the patch in notes/L-ALG.md."""
import sys, os, re, subprocess, random
oink, rngame, N, seed = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]); extra = sys.argv[5:]
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out", "dtl_pieces"); os.makedirs(outdir, exist_ok=True)
rng = random.Random(seed)
def analyse(path):
    r = subprocess.run([oink, "--dtl", "-t", "--no-single", "--no-wcwc", "--no-loops", path], capture_output=True, text=True, timeout=600)
    out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
    searches = []; cur = None
    for line in out.splitlines():
        m = re.search(r"iteration (\d+)-(even|odd)", line)
        if m: cur = {"pl": m.group(2), "iters": []}; searches.append(cur); continue
        m = re.search(r"ITER depth (\d+) R:(.*)", line)
        if m and cur is not None and m.group(1) == "0": cur["iters"].append(set(m.group(2).split()))
    def index(sr):
        idx = {}; its = sr["iters"]
        if not its: return idx, set()
        for v in its[0]:
            k = next((i for i in range(1, len(its)) if v not in its[i]), len(its))
            idx[v] = k
        return idx, its[0]
    viol = []
    for i in range(len(searches)):
        j = next((k for k in range(i + 1, len(searches)) if searches[k]["pl"] == searches[i]["pl"]), None)
        if j is None: continue
        ia, Ga = index(searches[i]); ib, Gb = index(searches[j])
        bad = [(v, ia[v], ib[v]) for v in Gb if v in ia and ib[v] > ia[v]]
        if bad: viol.append((i, j, bad[:4]))
    return viol, len(searches)
tot = nv = 0; games = list(extra)
for i in range(N):
    n = rng.randint(5, 12); g = subprocess.run([rngame, str(n), str(rng.randint(2, n)), "1", str(rng.randint(1, 3))], capture_output=True, text=True).stdout
    p = os.path.join(outdir, "cur.pg"); open(p, "w").write(g); games.append(p)
for k, path in enumerate(games):
    viol, ns = analyse(path); tot += 1
    if viol:
        nv += 1; keep = path if not path.endswith("cur.pg") else os.path.join(outdir, f"viol_{seed}_{k}.pg")
        if keep != path: open(keep, "w").write(open(path).read())
        print("VIOLATION", os.path.basename(keep), "searches", ns, viol[:2], flush=True)
print(f"done: {tot} games, {nv} with a vertex removed LATER in a later search")
