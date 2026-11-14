#!/usr/bin/env python3
"""L-RED-B packet P-N5-EXP: the FROZEN guard and the APPEND-ONLY guard (fixes entry 7; run by check.sh; files only, no git).

  frozen   [docs/red-b/P-N5-EXP.md does not have the sha1 of its freeze commit 350d84eb]
  prefix   the number of landed stages of docs/red-b/P-N5-EXP-fixes.md whose text is no longer a byte prefix of the file:
           the first 125 lines (entry 1, claude/l-red-b 06d399c2), the first 829 (entries 1-5, 24f4d436), the first 881
           (entries 1-6, 0c8fdf9e), the first 1147 (entries 1-7, b1a93700), the first 1180 (entries 1-8, 10dfedb6), the first 1271
           (entries 1-9, 35f14318), the first 1368 (entries 1-10, abde9163), the first 1443 (entries 1-11, the commit
           of entry 11), each with the sha1 the whole file had there
  l1       [docs/red-b/P-N5-EXP-line-L1.txt does not have its sha1 (line L-1 is never edited; L-2 is built from it by b6line.py)]
  l2 .. l6     the same for the lines L-2 to L-5 (history) and L-6 (the line of record, fixes entry 11)
Prints one line «guard frozen F prefix P of S l1 L l2 L l3 L l4 L l5 L l6 L»; exit 1 unless all are 0.
Control B6G_CTRL=1: one character of entry 1 is changed in memory; prefix must fire at every stage."""
import sys, os, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.normpath(os.path.join(HERE, "..", "..", "docs", "red-b"))
FROZEN = "c0449b17193f19619f33b366096762dfde27d542"
L1 = "59c5309377eda882ba436ffe7eb03fbff598c7c8"
L2 = "6e047c676e582484fe8eb87891764e8c1a7d9a18"
L3 = "fd9074a3b9961f59a1b64d5acdaa28529306ede9"
L4 = "668fd1b88ea4ae28690f0b931d84b27a85928ca8"
L5 = "fbd857b08befb397e03e71c554cccb4542be3820"
L6 = "1e0ff12d51da7a4ee1aad12ed0fd9119a097896b"
STAGES = [(125, "4c692ab2a092708d206719759f966a0ae4f98e5a"), (829, "9dc9179fb08063cd59de25c5d3e16b0f8c693fbd"),
          (881, "43a941eb6249f0278e342438f92293b7f7a4449e"), (1147, "abb6b96869d627c7aba23226feb18f847298a8f1"),
          (1180, "013290889e9e08f58ae162baa0c2eb5082f4b135"), (1271, "b0b8475794ead69c1e8b57d0bb26a82ff18d77c9"),
          (1368, "c87fcbe8156d2b83a68ea6c505dab5cad071bbcf"), (1443, "214967a10752ac9b90981d01628bec13473da404")]
sha1 = lambda b: hashlib.sha1(b).hexdigest()

if __name__ == "__main__":
    frozen = int(sha1(open(os.path.join(D, "P-N5-EXP.md"), "rb").read()) != FROZEN)
    l1 = int(sha1(open(os.path.join(D, "P-N5-EXP-line-L1.txt"), "rb").read()) != L1)
    l2 = int(sha1(open(os.path.join(D, "P-N5-EXP-line-L2.txt"), "rb").read()) != L2)
    l3 = int(sha1(open(os.path.join(D, "P-N5-EXP-line-L3.txt"), "rb").read()) != L3)
    l4 = int(sha1(open(os.path.join(D, "P-N5-EXP-line-L4.txt"), "rb").read()) != L4)
    l5 = int(sha1(open(os.path.join(D, "P-N5-EXP-line-L5.txt"), "rb").read()) != L5)
    l6 = int(sha1(open(os.path.join(D, "P-N5-EXP-line-L6.txt"), "rb").read()) != L6)
    fx = open(os.path.join(D, "P-N5-EXP-fixes.md"), "rb").read()
    if os.environ.get("B6G_CTRL") == "1":
        i = fx.index(b"Entry 1")
        fx = fx[:i] + b"e" + fx[i + 1:]
    lines = fx.split(b"\n")
    prefix = 0
    for n, h in STAGES:
        prefix += int(len(lines) <= n or sha1(b"\n".join(lines[:n]) + b"\n") != h)
    print(f"guard frozen {frozen} prefix {prefix} of {len(STAGES)} l1 {l1} l2 {l2} l3 {l3} l4 {l4} l5 {l5} l6 {l6}")
    sys.exit(1 if (frozen or prefix or l1 or l2 or l3 or l4 or l5 or l6) else 0)
