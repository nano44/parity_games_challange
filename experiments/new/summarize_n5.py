#!/usr/bin/env python3
"""One table row per N5 sweep CSV (experiments/new/n5/*.csv): N and n range, iterations first..last, local log-log slope of
iterations in n (last 3), fallbacks, rows checked. Usage: summarize_n5.py fam ..."""
import csv, sys, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
for fam in sys.argv[1:]:
    rows = list(csv.DictReader(open(os.path.join(HERE, "n5", fam + ".csv"))))
    ok = [r for r in rows if r["n5_iterations"]]; bad = [r for r in ok if "OK strategies verified" not in r["check"]]
    stop = [r for r in rows if r["secs"].startswith(("TIMEOUT", "BUDGET"))]
    n = [float(r["n"]) for r in ok]; it = [max(int(r["n5_iterations"]), 1) for r in ok]
    sl = [round(math.log(it[i + 1] / it[i]) / math.log(n[i + 1] / n[i]), 2) for i in range(len(it) - 1) if n[i + 1] > n[i]][-3:]
    print(f"| {fam} | N = {ok[0]['N']}..{ok[-1]['N']} (n = {int(n[0])}..{int(n[-1])}){'; ' + stop[0]['secs'] + ' at N = ' + stop[0]['N'] if stop else ''} | {it[0]} .. {it[-1]} | {sl} | {sum(int(r['fallback']) for r in ok)} | {len(ok) - len(bad)}/{len(ok)} |")
