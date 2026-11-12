#!/usr/bin/env python3
# Box 206 Addendum E (L-NEW successor 71), item E1: every «…» quote in section E1's «Quoted premise» bullet (up to «- Other box 206 statements»), whitespace-normalised,
# searched in trunk docs/RESULTS.md; prints the trunk line of each quote's first 60 characters.
# Usage (needs git objects): python3 quotes206E.py TRUNK_SHA   (run from experiments/new/box206)
import sys, subprocess, re
raw = subprocess.run(["git", "show", sys.argv[1] + ":docs/RESULTS.md"], capture_output=True, text=True, check=True).stdout
res = " ".join(raw.split())
doc = open("../../../docs/new/N5-DEPTH-box206.md", encoding="utf-8").read()
sec = doc[doc.index("### E1."):]; sec = sec[sec.index("Quoted premise"):sec.index("- Other box 206 statements")]
qs = [" ".join(q.split()) for q in re.findall(r"«([^«»]*)»", sec)]
miss = [q for q in qs if q not in res]
for q in qs:
    ln = [i + 1 for i, l in enumerate(raw.splitlines()) if " ".join(q.split()[:6]) in " ".join(l.split())]
    print("quote", repr(q[:60]), "line(s)", ln[:3], "found", q in res)
print("quotes", len(qs), "missing", len(miss), "trunk", sys.argv[1])
