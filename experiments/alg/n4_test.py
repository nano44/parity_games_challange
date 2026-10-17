#!/usr/bin/env python3
"""Step (b) of C1.md: NE(k) on every canonical n = 4 game psolC leaves partly undecided (out/psolc_fail_n4.jsonl from
psolc_fail_n4.py; 1,380 games per A3). Reports the histogram of the smallest k that solves each game (k <= KMAX),
soundness against Zielonka, and verified oracle strategies on every solved game; the games needing the largest k (or
unsolved) are written to out/n4_hard.jsonl and the first few as .pg files to instances/.
Usage: n4_test.py [--kmax 3] [--file out/psolc_fail_n4.jsonl]"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import alglib, pg, verify

opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
kmax = int(opt("--kmax", 3))
path = opt("--file", os.path.join(HERE, "out", "psolc_fail_n4.jsonl"))
hist, hard, bad = {}, [], []
recs = [json.loads(l) for l in open(path)]
for rec in recs:
    g = alglib.from_record(rec)
    k, undec, verd = alglib.k_needed(g, rec["ref"], kmax, with_strat=True)
    hist[k] = hist.get(k, 0) + 1
    if verd and (verd["verify"] or verd["strat_fail"]):
        bad.append((rec, verd))
    if k == "UNSOUND" or k is None or k >= 2:
        hard.append(dict(rec, k=k, undec=undec))
print(f"{len(recs)} psolC-partial n=4 games; smallest k: " + ", ".join(f"k={k}: {c}" for k, c in sorted(hist.items(), key=str)))
print(f"strategy problems: {len(bad)}")
for rec, verd in bad[:5]:
    print("  ", rec, verd)
with open(os.path.join(HERE, "out", "n4_hard.jsonl"), "w") as f:
    for r in hard:
        f.write(json.dumps(r) + "\n")
os.makedirs(os.path.join(HERE, "instances"), exist_ok=True)
hard.sort(key=lambda r: (str(r["k"]), r["m"]))
for i, r in enumerate(hard[:6]):
    pg.write(alglib.from_record(r), os.path.join(HERE, "instances", f"n4_k{r['k']}_m{r['m']}_{i}.pg"))
    print("  hard:", r["k"], r["undec"], r["prio"], r["owner"], r["succ"], "ref", r["ref"])
