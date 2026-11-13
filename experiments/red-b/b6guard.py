#!/usr/bin/env python3
"""L-RED-B packet P-N5-EXP: the FROZEN guard and the APPEND-ONLY guard (fixes entry 7; run by check.sh; files only, no git).

  frozen   [docs/red-b/P-N5-EXP.md does not have the sha1 of its freeze commit 350d84eb]
  prefix   the number of landed stages of docs/red-b/P-N5-EXP-fixes.md whose text is no longer a byte prefix of the file:
           the first 125 lines (entry 1, claude/l-red-b 06d399c2), the first 829 (entries 1-5, 24f4d436), the first 881
           (entries 1-6, 0c8fdf9e), the first 1147 (entries 1-7, b1a93700), the first 1180 (entries 1-8, the commit of entry 8),
           each with the sha1 the whole file had there
  l1       [docs/red-b/P-N5-EXP-line-L1.txt does not have its sha1 (line L-1 is never edited; L-2 is built from it by b6line.py)]
  l2, l3   the same for the lines L-2 (history) and L-3 (the line of record, fixes entry 8)
Prints one line «guard frozen F prefix P of S l1 L l2 L l3 L»; exit 1 unless all are 0.
Control B6G_CTRL=1: one character of entry 1 is changed in memory; prefix must fire at every stage."""
import sys, os, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.normpath(os.path.join(HERE, "..", "..", "docs", "red-b"))
FROZEN = "c0449b17193f19619f33b366096762dfde27d542"
L1 = "59c5309377eda882ba436ffe7eb03fbff598c7c8"
L2 = "6e047c676e582484fe8eb87891764e8c1a7d9a18"
L3 = "fd9074a3b9961f59a1b64d5acdaa28529306ede9"
STAGES = [(125, "4c692ab2a092708d206719759f966a0ae4f98e5a"), (829, "9dc9179fb08063cd59de25c5d3e16b0f8c693fbd"),
          (881, "43a941eb6249f0278e342438f92293b7f7a4449e"), (1147, "abb6b96869d627c7aba23226feb18f847298a8f1"),
          (1180, "013290889e9e08f58ae162baa0c2eb5082f4b135")]
sha1 = lambda b: hashlib.sha1(b).hexdigest()

if __name__ == "__main__":
    frozen = int(sha1(open(os.path.join(D, "P-N5-EXP.md"), "rb").read()) != FROZEN)
    l1 = int(sha1(open(os.path.join(D, "P-N5-EXP-line-L1.txt"), "rb").read()) != L1)
    l2 = int(sha1(open(os.path.join(D, "P-N5-EXP-line-L2.txt"), "rb").read()) != L2)
    l3 = int(sha1(open(os.path.join(D, "P-N5-EXP-line-L3.txt"), "rb").read()) != L3)
    fx = open(os.path.join(D, "P-N5-EXP-fixes.md"), "rb").read()
    if os.environ.get("B6G_CTRL") == "1":
        i = fx.index(b"Entry 1")
        fx = fx[:i] + b"e" + fx[i + 1:]
    lines = fx.split(b"\n")
    prefix = 0
    for n, h in STAGES:
        prefix += int(len(lines) <= n or sha1(b"\n".join(lines[:n]) + b"\n") != h)
    print(f"guard frozen {frozen} prefix {prefix} of {len(STAGES)} l1 {l1} l2 {l2} l3 {l3}")
    sys.exit(1 if (frozen or prefix or l1 or l2 or l3) else 0)
