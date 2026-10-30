#!/usr/bin/env python3
"""Box 23 (a): rstar.py (mine, n5b) vs L-NEW's xirise.py (n5x) on L-NEW's box-85 corpus (box 83: new/box59/sbcg.lst, si/root/logs/
alt_all.lst). Compares, per game, the fields both print: number of W-runs, max R*_F, max FL_F, max |F|, FREE-RED violations.
L-NEW's values are read from new/box85/xirise_{sbcg,alt}.txt (l-new 893b9346, read only); --rerun N also re-runs xirise.py itself
(unmodified, separate process) on the first N games of each list, to confirm the committed files are what the tool prints now.
Usage (from experiments/): python3 n5-box23/xcheck.py [--jobs 4] [--rerun 40] > n5-box23/results/xcheck.txt"""
import argparse
import ast
from multiprocessing.pool import ThreadPool
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))


def lnew(path):
    out = {}
    for line in open(path):
        m = re.match(r"GAME (\S+) XIRISE n (\d+) runs (\d+) (\{.*?\}) maxima (\{.*\})", line)
        if m:
            c, mx = ast.literal_eval(m.group(4)), ast.literal_eval(m.group(5))
            out[m.group(1)] = dict(runs=int(m.group(3)), rs=mx["rstar"], fl=mx["fl"], F=mx["F"], viol=c["viol_fr"])
        else:
            out[line.split()[1]] = None
    return out


def mine(args):
    pgf, stf = args   # own process per game, 900 s cap (xirise.py had 300 s)
    o = subprocess.run(["timeout", "900", "python3", "-I", os.path.join(HERE, "rstar.py"), pgf] + ([stf] if stf else []),
                       capture_output=True, text=True, cwd=ROOT)
    m = re.search(r"RSTAR it \d+ (\{.*\})", o.stdout)
    if not m:
        return pgf, None, f"rc {o.returncode} {o.stderr.strip()[-200:]}"
    s = ast.literal_eval(m.group(1))
    return pgf, dict(runs=s["runs"], rs=s["rs"], fl=s["fl"], F=s["F"], viol=s["viol_freered"]), s


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--jobs", type=int, default=4); ap.add_argument("--rerun", type=int, default=0)
    a = ap.parse_args(); os.chdir(ROOT)
    lists = [("sbcg", [(l.strip(), None) for l in open("new/box59/sbcg.lst") if l.strip() and not l.startswith("#")], "new/box85/xirise_sbcg.txt"),
             ("alt", [tuple(l.split()[:2]) if len(l.split()) > 1 else (l.split()[0], None) for l in open("si/root/logs/alt_all.lst") if l.strip()],
              "new/box85/xirise_alt.txt")]
    tot = dict(games=0, agree=0, disagree=0, lnew_missing=0, mine_fail=0)
    best = dict(rs=(0, None), fl=(0, None))
    for name, items, ref in lists:
        L = lnew(ref)
        with ThreadPool(a.jobs) as pool:
            for pgf, m, s in pool.imap(mine, items):
                tot["games"] += 1; l = L.get(pgf)
                if m is None:
                    tot["mine_fail"] += 1; print("MINE-FAIL", name, pgf, s); continue
                for k in best:
                    if m[k] > best[k][0]:
                        best[k] = (m[k], pgf)
                if l is None:
                    tot["lnew_missing"] += 1; print("LNEW-MISSING", name, pgf, m); continue
                if l == m:
                    tot["agree"] += 1
                else:
                    tot["disagree"] += 1; print("DISAGREE", name, pgf, "lnew", l, "mine", m)
        for pgf, stf in items[:a.rerun]:
            cmd = ["timeout", "300", "python3", "-I", "new/box85/xirise.py", pgf] + ([stf] if stf else [])
            o = subprocess.run(cmd, capture_output=True, text=True).stdout.strip().splitlines()
            line = f"GAME {pgf} {o[-1] if o else 'NONE'}"
            same = line.strip() == next((x.strip() for x in open(ref) if x.split()[1] == pgf), None)
            print("RERUN", name, pgf, "same-as-committed" if same else "DIFFERS: " + line)
    print("TOTAL", tot, "max", best)


if __name__ == "__main__":
    main()
