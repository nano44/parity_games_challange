#!/usr/bin/env python3
"""Box 25: ins.py (mine, n5b) vs L-SI's treestab.py (n5x) on L-SI's committed corpus outputs experiments/si/sb53/tree_{alt,sbcg,red}.txt
(l-si 481bc6c2, read with git show; each line 'GAME PG [START] TREESTAB ...'). Fields: intervals, LTX, TSX, NOVT, KB, MAXKEYCH, MAXINS.
Usage (from experiments/): xins.py TREE.txt [--jobs 4]"""
import os
import re
import subprocess
import sys
from multiprocessing.pool import ThreadPool

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
F = ("intervals", "LTX", "TSX", "NOVT", "KB", "MAXKEYCH", "MAXINS")


def mine(item):
    args, ref = item
    o = subprocess.run(["timeout", "900", sys.executable, "-I", os.path.join(HERE, "ins.py")] + args, capture_output=True, text=True, cwd=ROOT)
    m = re.search(r"^INS .*", o.stdout, re.M)
    return args, ref, (dict((k, int(v)) for k, v in re.findall(r"(\w+) (\d+)", m.group(0).split("|")[0])) if m else None)


def main():
    os.chdir(ROOT); items = []
    for line in open(sys.argv[1]):
        if "TREESTAB" not in line:
            continue
        head, tail = line.split("TREESTAB", 1)
        args = head.split()[1:]
        ref = dict((k, int(v)) for k, v in re.findall(r"(\w+) (\d+)", tail))
        if all(os.path.exists(a) for a in args):
            items.append((args, ref))
    jobs = int(sys.argv[sys.argv.index("--jobs") + 1]) if "--jobs" in sys.argv else 4
    tot = dict(games=0, agree=0, disagree=0, fail=0); mx = dict(MAXINS=(0, None), MAXKEYCH=(0, None))
    with ThreadPool(jobs) as pool:
        for args, ref, m in pool.imap(mine, items):
            tot["games"] += 1
            if m is None:
                tot["fail"] += 1; print("MINE-FAIL", args); continue
            d = {k: (m[k], ref[k]) for k in F if m[k] != ref[k]}
            if d:
                tot["disagree"] += 1; print("DISAGREE", args[0], d)
            else:
                tot["agree"] += 1
            for k in mx:
                if m[k] > mx[k][0]:
                    mx[k] = (m[k], args[0])
    print("TOTAL", tot, "max", mx)


if __name__ == "__main__":
    main()
