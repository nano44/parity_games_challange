#!/usr/bin/env python3
"""L-ALG (2026-10-15, DTL step 4, (M-cross) of DTL-proof.md §3(a) Lemma S): region part. From a DEBUG Oink trace (-t -t prints
every sptl region "region P top v1 v2 ..." in pop order, top first), take the first sptl pass of the FIRST stable set of
each search; for consecutive same-player searches s < s', check for every top tau of s that is still unsolved:
tau is a top of s' and region(tau, s) ∩ G'_{s'} ⊆ ∪ { region(tau', s') : tau' processed at or before tau in s' }.
Usage: dtl_regions_monotone.py DEBUG_OINK RNGAME N_GAMES SEED [games...]. Prints violations and a summary."""
import sys, os, re, subprocess, random
oink, rngame, N, seed = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]); extra = sys.argv[5:]
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out", "dtl_regions"); os.makedirs(outdir, exist_ok=True)
rng = random.Random(seed)
def analyse(path):
    r = subprocess.run([oink, "--dtl", "-t", "-t", "--no-single", "--no-wcwc", "--no-loops", path], capture_output=True, text=True, timeout=600)
    out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
    searches = []; cur = None; phase = None
    for line in out.splitlines():
        m = re.search(r"iteration (\d+)-(even|odd)", line)
        if m: cur = {"pl": m.group(2), "G": None, "stable": False, "regions": [], "done": False}; searches.append(cur); phase = 0; continue
        if cur is None or cur["done"]: continue
        m = re.search(r"current region:(.*)", line)
        if m and cur["G"] is None: cur["G"] = set(m.group(1).split()); continue
        if "best vertices:" in line:
            if not cur["stable"] and not cur.get("seen"):
                cur["seen"] = True
                if "(stable)" in line: cur["stable"] = True   # first best_vertices call of the search is stable: a first piece
                else: cur["done"] = True                        # first call returned -1: no first-piece stable set, skip the search
                continue
            if cur["stable"]: cur["done"] = True
            continue
        if cur["stable"]:
            m = re.search(r"^\[\s*[\d.]+\] region \d+ (.*)$", line)
            if m:
                verts = [tok.split("->")[0] for tok in m.group(1).split()]
                if verts and any(verts[0] == rg[0] for rg in cur["regions"]): cur["done"] = True   # second pass starts
                elif verts: cur["regions"].append(verts)
            elif "new tangle" in line or "dominion" in line or "X" in line: cur["done"] = True
    viol = []
    for i in range(len(searches)):
        j = next((k for k in range(i + 1, len(searches)) if searches[k]["pl"] == searches[i]["pl"]), None)
        if j is None: continue
        a, b = searches[i], searches[j]
        if not a["stable"] or not b["stable"] or b["G"] is None: continue
        tops_b = [rg[0] for rg in b["regions"]]
        for rg in a["regions"]:
            tau = rg[0]
            if tau not in b["G"]: continue
            if tau not in tops_b: viol.append((i, j, tau, "top lost")); continue
            allowed = set(v for rg2 in b["regions"][:tops_b.index(tau) + 1] for v in rg2)
            lost = [v for v in rg if v in b["G"] and v not in allowed]
            if lost: viol.append((i, j, tau, "lost " + ",".join(lost[:5])))
    return viol, len(searches)
tot = 0; nv = 0; games = list(extra)
for i in range(N):
    n = rng.randint(5, 12); g = subprocess.run([rngame, str(n), str(rng.randint(2, n)), "1", str(rng.randint(1, 3))], capture_output=True, text=True).stdout
    path = os.path.join(outdir, "cur.pg"); open(path, "w").write(g); games.append(path)
for k, path in enumerate(games):
    viol, ns = analyse(path); tot += 1
    if viol:
        nv += 1; keep = path if not path.endswith("cur.pg") else os.path.join(outdir, f"viol_{seed}_{k}.pg")
        if keep != path: open(keep, "w").write(open(path).read())
        print("VIOLATION", keep, "searches", ns, viol[:3], flush=True)
print(f"done: {tot} games, {nv} with a non-monotone first-piece region")
