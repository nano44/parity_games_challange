#!/usr/bin/env python3
"""L-NEW box 72 §6: totals of run_txc.sh output (txc_*.txt): TXC / GXC / overlap / sources for N5 and N5-LZC, and tied.py's REPEAT counters."""
import re, ast, sys
from collections import Counter
for side in ("N5", "LZC"):
    tot = Counter(); src = Counter(); mx = {}
    tied = Counter()
    for f in ("txc_sbcg.txt", "txc_alt.txt"):
        for l in open(f):
            part = l.split(f" {side} TXC ")[1].split(" LZC ")[0].split(" TIEDN5 ")[0]
            for k in ("txc", "gxc", "gxc-in-wrun", "gxc-at-fb", "txc-and-gxc"): tot[k] += int(re.search(rf"(?<![\w-]){k} (\d+)", part).group(1))
            for k in ("max-per-z-wrun", "max-per-wrun"):
                x = int(re.search(rf"{k} (\d+)", part).group(1))
                if x > mx.get(k, (0,))[0]: mx[k] = (x, l.split()[1])
            src.update(ast.literal_eval(re.search(r"src (\{.*?\})", part).group(1)))
            tp = l.split(" TIEDN5 " if side == "N5" else " TIEDLZC ")[1]
            if side == "N5": tp = tp.split(" TIEDLZC ")[0]
            for k in ("rep", "tied", "untied", "reblk", "untied_reblk"): tied[k] += int(re.search(rf" {k} (\d+)", tp).group(1))
    print(side, dict(tot), "sources", dict(src), mx, "tied.py", dict(tied))
