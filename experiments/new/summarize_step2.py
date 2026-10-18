#!/usr/bin/env python3
"""One verdict-table row per step-2 CSV (experiments/new/step2/*.csv): N and n range, N1 iterations, last local log-log slopes,
whether every finished row is checked OK. Usage: summarize_step2.py fam ..."""
import csv, sys, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
for fam in sys.argv[1:]:
    rows = list(csv.DictReader(open(os.path.join(HERE, "step2", fam + ".csv"))))
    ok = [r for r in rows if r["even_iters"]]; bad = [r for r in ok if "OK strategies verified" not in r["check"]]
    to = [r for r in rows if r["secs"].startswith(("TIMEOUT", "BUDGET", "STOPPED"))]
    n = [float(r["n"]) for r in ok]; it = [int(r["even_iters"]) + int(r["odd_iters"]) for r in ok]; s = [max(float(r["secs"]), 1e-3) for r in ok]
    sl = lambda y: [round(math.log(y[i + 1] / y[i]) / math.log(n[i + 1] / n[i]), 2) for i in range(len(y) - 1) if n[i + 1] > n[i] and y[i] > 0][-3:]
    print(f"| {fam} | N = {ok[0]['N']}..{ok[-1]['N']} (n = {int(n[0])}..{int(n[-1])}){'; stop at N = ' + to[0]['N'] + ': ' + to[0]['secs'].split(' (')[0] if to else ''} | {it[0]} .. {it[-1]} (largest phase {max(int(r['max_phase']) for r in ok)}) | {sl(it)} / {sl(s)} | {len(ok) - len(bad)}/{len(ok)} | {'polynomial-looking; agrees, strategies verified' if not bad else 'CHECK ' + bad[0]['N'] + ': ' + bad[0]['check'][:40]} |")
