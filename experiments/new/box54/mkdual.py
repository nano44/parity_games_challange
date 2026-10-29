#!/usr/bin/env python3
"""L-NEW box 54: write the DUAL game G^d (owners swapped, priorities + 1; same ids and successor lists) and, if a start file is given, the
swapped start (SIGMA0 <-> TAU0). Usage: mkdual.py GAME.pg OUT.pg [START OUT.start]"""
import sys
L = [l.rstrip("\n") for l in open(sys.argv[1]) if l.strip() and not l.lstrip().startswith("%")]
out = [L[0]]
for l in L[1:]:
    p = l.rstrip(";").split(None, 3); out.append("%s %d %d %s;" % (p[0], int(p[1]) + 1, 1 - int(p[2]), p[3].split()[0].rstrip(";")))
open(sys.argv[2], "w").write("\n".join(out) + "\n")
if len(sys.argv) > 3:
    S = {l.split()[0]: l.split()[1:] for l in open(sys.argv[3]) if l.strip()}
    open(sys.argv[4], "w").write("SIGMA0 " + " ".join(S.get("TAU0", [])) + "\nTAU0 " + " ".join(S.get("SIGMA0", [])) + "\n")
