#!/usr/bin/env python3
"""Sum the TOTAL lines of mut_*.out (sweep3.sh): coverage, every must-0 counter, and the Seq / DEAD / max records."""
import glob, sys
MUST0 = ["entfail", "playfail", "prefail", "kindfail", "hwfail", "gtfail", "trfail", "abfail", "psa", "psb", "psc", "rw_psa", "rw_psb", "rw_psc",
         "lamb", "lamm", "spfail", "spl3M", "rcfail", "decfail", "rws1", "rws2", "rw1fail", "ph_a", "ph_b", "ph_c", "rafail", "rpfail", "rptfail",
         "recfail", "dmon", "pcfail", "bdfail", "awa", "awb", "awc", "awd", "awmv", "rootfail"]
COV = ["runs", "changes", "couples", "rewins", "Seq", "ascents", "d6", "d6m"]; MX = ["maxC", "maxSPL", "maxT3"]
tot = {}; files = sorted(glob.glob("mut_*.out"))
for f in files:
    t = [l for l in open(f) if l.startswith("TOTAL")]
    if not t: print(f, "no TOTAL (unfinished)"); continue
    a = t[-1].split(":", 1)[1].split(); d = dict(zip(a[0::2], map(int, a[1::2])))
    print(f, " ".join(f"{k} {d[k]}" for k in COV + MX), "| must-0 nonzero:", {k: d[k] for k in MUST0 if d[k]} or "none")
    for k in COV + MUST0: tot[k] = tot.get(k, 0) + d[k]
    for k in MX: tot[k] = max(tot.get(k, 0), d[k])
print("SUM", " ".join(f"{k} {tot.get(k, 0)}" for k in COV + MX), "| must-0 total:", sum(tot.get(k, 0) for k in MUST0))
