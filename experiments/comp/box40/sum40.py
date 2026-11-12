#!/usr/bin/env python3
"""box 40 item 2 summary of ties40 random outputs (unit: genome). Usage: sum40.py OUT.jsonl ..."""
import sys, json
for f in sys.argv[1:]:
    R = [json.loads(l) for l in open(f)]; A = [r for r in R if not r.get("capped")]
    tie = [r for r in A if r["tiestates"]]; exc = [r for r in A if r["Hmax"] > r["T3n"]]; low = [r for r in A if r["Hmin"] < r["T3n"]]
    lx = [r for r in A if "locmax" in r and r["locmax"] > r["n5v_maxloc"]]
    print(f, "genomes", len(R), "capped", len(R) - len(A), "legal_n5v", sum(r["legal"] for r in A), "with_ties", len(tie),
          "Hmax>T3n", len(exc), "by", sorted(r["Hmax"] - r["T3n"] for r in exc), "Hmin<T3n", len(low),
          "locmax>n5v", len(lx), "maxHM", max((r.get("HM", -99) for r in A), default=None),
          "max_ratio_any_path", max((r.get("ratio_max", -1) for r in A), default=None),
          "locfail_any", sum(r.get("locfail_any", 0) for r in A), "chainfail_any", sum(r.get("chainfail_any", 0) for r in A),
          "maxT3n", max(r["T3n"] for r in A), "N+M", min(r["N"] + r["M"] for r in R), "-", max(r["N"] + r["M"] for r in R))
