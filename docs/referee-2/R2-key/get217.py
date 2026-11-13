#!/usr/bin/env python3
"""REFEREE-2 successor 41: the inputs of the box 217 §6-§7 pre-read, taken by `git archive` / `git show` at pinned commits (nothing is
copied into the repo; run from the repository root after `git fetch origin` of the five lane branches).
  OUT/towers/   the 5 towers of box 212 (be167574, through R2-box212/get_inst.py, which checks the lane's SHA1SUMS)
  OUT/rec/      the 62 records of box 217 (a143d406, experiments/new/box217/out/rec)
  OUT/red/      L-RED R243's H5PLUS_L5.json (aa4f7680)
  OUT/corp/<lane>/  experiments/<dir> of five lanes at the pinned commits
  OUT/corpus.list   one line «sha1 N path» per DISTINCT genome among the JSON files of OUT/corp that are in R104's genome format, have an
                    acyclic Ξ-graph and meet box 217 §6.1's premises (W-targets one level down, distinct ε, distinct β priorities); the
                    first path in sorted order represents a content. Counts of what was dropped are printed.
Usage: get217.py OUT [LIST]    (with LIST: compares the rebuilt corpus.list with it, prints «list equal» or «list DIFFERS»)"""
import sys, os, json, hashlib, subprocess, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "R2-P-N5-END")); sys.path.insert(0, HERE)
import r2end, r2unit217
PINS = {"l-new": ("a143d4060d75f8463fe098b6ce18eef3febcd14b", "experiments/new"), "l-red": ("aa4f76805c9290b419d6388eb60ac32b3a03db7c", "experiments/red"),
        "l-lower": ("b6887effd52913cbd4e9519670de50d246dd2009", "experiments/lower"), "l-comp": ("6bfd49661c09b0f791d59da36350cce4bd9ea431", "experiments/comp"),
        "l-si": ("ff28a3fc15443ca22364fbe728b8b9cd587e8fa0", "experiments/si")}
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
sh = lambda c: subprocess.run(c, shell=True, check=True, capture_output=True, text=True).stdout
print(sh(f"python3 {HERE}/../R2-box212/get_inst.py be167574 {out}").strip())
os.makedirs(f"{out}/rec", exist_ok=True); os.makedirs(f"{out}/red", exist_ok=True)
for p in sh(f"git ls-tree -r --name-only {PINS['l-new'][0]} experiments/new/box217/out/rec/").split():
    open(f"{out}/rec/{os.path.basename(p)}", "w").write(sh(f"git show {PINS['l-new'][0]}:{p}"))
open(f"{out}/red/H5PLUS_L5.json", "w").write(sh(f"git show {PINS['l-red'][0]}:experiments/red/r243/inst/H5PLUS_L5.json"))
for lane, (com, d) in PINS.items():
    os.makedirs(f"{out}/corp/{lane}", exist_ok=True); sh(f"git archive {com} {d} | tar -x -C {out}/corp/{lane}")
seen = {}; why = collections.Counter()
for lane in sorted(PINS):
    for root, dirs, fs in os.walk(f"{out}/corp/{lane}"):
        dirs.sort()
        for f in sorted(fs):
            if not f.endswith(".json"): continue
            p = os.path.join(root, f)
            if os.path.getsize(p) > 400000: why["over 400 kB, not read"] += 1; continue
            try: G = json.load(open(p))
            except Exception: why["not JSON"] += 1; continue
            if isinstance(G, dict) and isinstance(G.get("genome"), dict): G = G["genome"]
            if not (isinstance(G, dict) and all(k in G for k in ("N", "lev", "opts", "gate", "br", "bp", "start"))): why["not a genome"] += 1; continue
            why["genome format"] += 1
            try:
                if not r2end.acyclic(G): why["Ξ-cyclic"] += 1; continue
                r2unit217.M1P(G)
            except AssertionError as e: why[f"premise fails: {e}"] += 1; continue
            except Exception as e: why[f"unreadable genome: {type(e).__name__}"] += 1; continue
            key = hashlib.sha1(json.dumps({k: G[k] for k in ("N", "lev", "opts", "gate", "br", "bp", "start")}, sort_keys=True).encode()).hexdigest()
            if key in seen: why["duplicate content"] += 1
            else: seen[key] = (os.path.relpath(p, out), G["N"])
lines = [f"{k} {N} {p}\n" for k, (p, N) in sorted(seen.items(), key=lambda kv: kv[1][0])]
open(f"{out}/corpus.list", "w").writelines(lines)
print("corpus: distinct valid Ξ-acyclic genomes", len(lines), "|", "; ".join(f"{k} {v}" for k, v in sorted(why.items())))
print("by lane:", dict(collections.Counter(p.split("/")[1] for p, _ in seen.values())))
if len(sys.argv) > 2: print("list equal" if open(sys.argv[2]).readlines() == lines else "list DIFFERS")
