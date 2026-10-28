#!/usr/bin/env python3
"""Box 16 §4/§5 table from results/rs2_*.log (randstarts2.py): per game and start family the worst value of each counter (with the run
that attains it), runs, FAIL count. Usage: rs2table.py"""
import glob, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
KEYS = ("it", "fb", "phases", "longest", "XR", "XRQ", "ALT", "TF", "TFG")
rows = []
for f in glob.glob(os.path.join(HERE, "results", "rs2_*.log")):
    lines = open(f).read().splitlines()
    runs = [l.split() for l in lines if l and not l.startswith(("#", "END", "EXIT"))]
    if not runs:
        continue
    tag = runs[0][0]; m = re.match(r"H(\d+)(\w*)", tag); n, var = int(m.group(1)), m.group(2) or "H_n"
    sha = next((l.split()[3] for l in lines if l.startswith("END") and " sha1 " in l), "?")
    fams = {}
    for r in runs:
        lab = r[1]; fam = "rand" if lab.startswith("rand") else "G" if lab.startswith("G") else lab
        d = {r[i]: int(r[i + 1]) for i in range(2, len(r) - 1, 2)}; d["ok"] = r[-1] == "OK"
        fams.setdefault(fam, []).append((lab, d))
    done = any(l.startswith("END") and " runs " in l for l in lines)
    for fam, L in fams.items():
        w = {}
        for k in KEYS:
            vals = [(d.get(k, -1), lab) for lab, d in L]
            w[k] = max(vals)
        rows.append((var, n, fam, sha, len(L), sum(not d["ok"] for _, d in L), w, done))
order = {"S3": 0, "F": 1, "rand": 2, "G": 3}
rows.sort(key=lambda r: (r[0] != "H_n", r[0], r[1], order.get(r[2], 9)))
print("| game | n | sha1 | starts | runs | FAIL | max it | max phases | max longest | max XR | max XRQ | max ALT | max TF | max TFG | complete |")
print("| --- " * 15 + "|")
for var, n, fam, sha, cnt, bad, w, done in rows:
    c = lambda k: f"{w[k][0]}" + (f" ({w[k][1]})" if fam in ("rand", "G") else "")
    print(f"| {var} | {n} | {sha[:8]} | {fam} | {cnt} | {bad} | {c('it')} | {c('phases')} | {c('longest')} | {c('XR')} | {c('XRQ')} | "
          f"{c('ALT')} | {c('TF')} | {c('TFG') if w['TFG'][0] >= 0 else '-'} | {'yes' if done else 'PARTIAL'} |")
