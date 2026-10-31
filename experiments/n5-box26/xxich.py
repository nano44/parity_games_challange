#!/usr/bin/env python3
"""Box 26: xich.py (mine, n5b) vs L-NEW's xirise.py 'xich' (max over W-runs and vertices of XICH_F(v)) on the box-83 corpus, from the committed
new/box85/xirise_{sbcg,alt}.txt (l-new 893b9346). Also collects, per game, max XICH, its |F|, the max |F| and n.
Usage (from experiments/): xxich.py > n5-box26/results/xxich.txt"""
import ast, os, re, subprocess, sys
from multiprocessing.pool import ThreadPool
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))


def ref(path):
    out = {}
    for line in open(path):
        m = re.match(r"GAME (\S+) XIRISE n (\d+) .* maxima (\{.*\})", line)
        if m:
            out[m.group(1)] = (int(m.group(2)), ast.literal_eval(m.group(3)))
    return out


def mine(item):
    pgf, stf = item
    o = subprocess.run(["timeout", "900", sys.executable, "-I", os.path.join(HERE, "xich.py"), pgf] + ([stf] if stf else []),
                       capture_output=True, text=True, cwd=ROOT).stdout
    m = re.search(r"XICH n (\d+) it \d+ runs \d+ maxXICH (\d+) \(v -?\d+\) F (\d+) sum (\d+) I (\d+) \| max\|F\| (\d+)", o)
    return pgf, (tuple(int(x) for x in m.groups()) if m else None)


os.chdir(ROOT)
lists = [([(l.strip(), None) for l in open("new/box59/sbcg.lst") if l.strip() and not l.startswith("#")], "new/box85/xirise_sbcg.txt"),
         ([tuple((l.split() + [None])[:2]) for l in open("si/root/logs/alt_all.lst") if l.strip()], "new/box85/xirise_alt.txt")]
tot = dict(games=0, agree=0, disagree=0, fail=0); top = []
for items, rf in lists:
    R = ref(rf)
    with ThreadPool(4) as pool:
        for pgf, m in pool.imap(mine, items):
            tot["games"] += 1
            if m is None:
                tot["fail"] += 1; print("MINE-FAIL", pgf); continue
            n, mx, F, s, I, Fmax = m; top.append((mx / n, mx, n, F, Fmax, pgf))
            if pgf not in R or R[pgf][1]["xich"] != mx:
                tot["disagree"] += 1; print("DISAGREE", pgf, mx, R.get(pgf))
            else:
                tot["agree"] += 1
print("TOTAL", tot)
for t in sorted(top, reverse=True)[:8]:
    print("TOP maxXICH/n %.3f maxXICH %d n %d |F| %d max|F| %d %s" % t)
print("TOP-ABS", sorted(top, key=lambda t: t[1], reverse=True)[:5])
