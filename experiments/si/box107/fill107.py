#!/usr/bin/env python3
"""Box 107: the DATA block of docs/si/box107-timing.md is the verbatim content of this directory's out/*.out files.
fill107.py write : rewrite the block between the two DATA107 markers;  fill107.py check : exit 1 unless the block equals the files."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); DOC = os.path.join(HERE, "..", "..", "..", "docs", "si", "box107-timing.md")
FILES = ["abandon107.out", "replay107.out", "ctrl107.out", "syn107.out", "bil107.out", "up107.out", "replay107_up.out", "pn107.out"]
def block():
    out = []
    for f in FILES:
        out.append(f"--- out/{f}")
        out += open(os.path.join(HERE, "out", f)).read().rstrip("\n").split("\n")
    return "```\n" + "\n".join(out) + "\n```"
B, E = "<!-- DATA107 begin -->", "<!-- DATA107 end -->"
s = open(DOC).read(); i, j = s.index(B), s.index(E)
if sys.argv[1] == "write":
    open(DOC, "w").write(s[:i + len(B)] + "\n" + block() + "\n" + s[j:])
else:
    sys.exit(0 if s[i + len(B):j].strip("\n") == block() else 1)
