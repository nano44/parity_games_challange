#!/usr/bin/env python3
# Box 205 Addendum A (G3): every «…» premise quote of the addendum, whitespace-normalised, searched in trunk docs/RESULTS.md.
# Usage (needs git objects): python3 quotes205.py TRUNK_SHA   (run from experiments/new/box205)
import sys, subprocess, re
res = " ".join(subprocess.run(["git", "show", sys.argv[1] + ":docs/RESULTS.md"], capture_output=True, text=True, check=True).stdout.split())
doc = open("../../../docs/new/N5-BETALOC-box205.md", encoding="utf-8").read()
add = doc[doc.index("## Addendum A"):]
qs = [" ".join(q.split()) for q in re.findall(r"«([^»]*)»", add.split("Premises, quoted")[1].split("###")[0])]
miss = [q for q in qs if q not in res]
print("quotes", len(qs), "missing", len(miss), "trunk", sys.argv[1]); [print("MISSING", q) for q in miss]
