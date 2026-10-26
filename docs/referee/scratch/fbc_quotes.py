#!/usr/bin/env python3
"""REFEREE succ. 15: own check of the curly-quoted strings of a packet section against files at a commit. Prints, per quote, the files and
line ranges where it occurs (whitespace-normalised across line breaks), or MISSING. Usage: fbc_quotes.py packet commit startmarker file..."""
import sys, re, subprocess
pk, com, mark = sys.argv[1:4]; files = sys.argv[4:]
txt = open(pk).read(); txt = txt[txt.index(mark):]
quotes = re.findall(r"“(.*?)”", txt, re.S)
src = {f: subprocess.run(["git", "show", "%s:%s" % (com, f)], capture_output=True, text=True).stdout.split("\n") for f in files}
def norm(s): return re.sub(r"\s+", " ", s).strip()
for q in quotes:
    qn = norm(q); hits = []
    for f, L in src.items():
        for i in range(len(L)):
            for span in range(1, 4):
                if qn in norm(" ".join(L[i:i + span])): hits.append("%s:%d-%d" % (f, i + 1, i + span)); break
            if hits and hits[-1].startswith(f + ":%d-" % (i + 1)): break
    print(("OK   " if hits else "MISSING ") + qn[:70] + " | " + ", ".join(hits[:3]))
