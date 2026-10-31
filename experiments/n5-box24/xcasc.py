#!/usr/bin/env python3
"""Box 24: casc.py (mine, n5b) vs L-NEW's retcause.py (n5x) per W-run, on L-NEW's corpus files experiments/new/box99/cause_{sbcg,alt}.txt
(l-new 95d52c5c, read with git show into a scratch dir; passed as arguments). For every game L-NEW printed (retcause.py had 300 s per game),
for every W-run with >= 1 return: (a, b), returns, EROOT max returns per root, EROOT chain-depth histogram, max children per node, max
children per return node, PERROOT max returns of one Even X per root. Mine: casc.py -v in its own process (900 s cap).
Usage (from experiments/): xcasc.py LIST.lst|alt CAUSE.txt [--jobs 4]"""
import ast
import os
import re
import subprocess
import sys
from multiprocessing.pool import ThreadPool

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))


def lnew(path):
    """L-NEW's file was written by xargs -P 4, so some lines carry two interleaved records: the LAST record of a line is used (greedy
    '.*' prefix), and a game whose EROOT / PERROOT line has no preceding RUN record is dropped (GARBLED, reported)."""
    G = {}; bad = set()
    for line in open(path):
        m = re.match(r".*GAME (\S+) RUN (\d+)-(\d+) F \d+ returns (\d+)", line)
        if m:
            G.setdefault(m.group(1), []).append(dict(a=int(m.group(2)), b=int(m.group(3)), returns=int(m.group(4)))); continue
        m = re.match(r".*GAME (\S+)\s+EROOT .* max returns per root (\d+) chain depth (\{.*?\}) max children per node (\d+) max children per return node (\d+)", line)
        if m and m.group(1) not in G:
            bad.add(m.group(1)); continue
        if m:
            G[m.group(1)][-1].update(casc=int(m.group(2)), depth=ast.literal_eval(m.group(3)), kids=int(m.group(4)), kids_ret=int(m.group(5))); continue
        m = re.match(r".*GAME (\S+)\s+PERROOT max returns of one Even X per root (\d+)", line)
        if m and m.group(1) in G:
            G[m.group(1)][-1].update(pxr=int(m.group(2)))
    for x in bad:
        G.pop(x, None); print("GARBLED (dropped)", x)
    return G


def mine(item):
    pgf, stf = item
    o = subprocess.run(["timeout", "900", sys.executable, "-I", os.path.join(HERE, "casc.py"), pgf] + ([stf] if stf else []) + ["-v"],
                       capture_output=True, text=True, cwd=ROOT)
    runs = [ast.literal_eval(l.strip()) for l in o.stdout.splitlines() if l.startswith("  {")]
    head = next((l for l in o.stdout.splitlines() if l.startswith("CASC")), None)
    return pgf, head, runs


def main():
    lst, cause = sys.argv[1], sys.argv[2]; jobs = int(sys.argv[sys.argv.index("--jobs") + 1]) if "--jobs" in sys.argv else 4
    os.chdir(ROOT); L = lnew(cause)
    items = []
    for l in open(lst):
        p = l.split()
        if p and not p[0].startswith("#") and p[0] in L:
            items.append((p[0], p[1] if len(p) > 1 else None))
    tot = dict(games=0, runs=0, agree=0, disagree=0, fail=0, bad=0)
    keys = ("returns", "casc", "depth", "kids", "kids_ret", "pxr")
    with ThreadPool(jobs) as pool:
        for pgf, head, runs in pool.imap(mine, items):
            tot["games"] += 1
            if head is None:
                tot["fail"] += 1; print("MINE-FAIL", pgf); continue
            tot["bad"] += int(re.search(r"bad (\d+)", head).group(1))
            M = {(r["a"], r["b"]): r for r in runs if r["returns"] > 0}
            T = {(r["a"], r["b"]): r for r in L[pgf]}
            if set(M) != set(T):
                tot["disagree"] += 1; print("DISAGREE runs", pgf, sorted(M), sorted(T)); continue
            for ab in T:
                tot["runs"] += 1
                d = [k for k in keys if k in T[ab] and M[ab][k] != T[ab][k]]
                if d:
                    tot["disagree"] += 1; print("DISAGREE", pgf, ab, {k: (M[ab][k], T[ab][k]) for k in d})
                else:
                    tot["agree"] += 1
    print("TOTAL", tot)


if __name__ == "__main__":
    main()
