#!/usr/bin/env python3
"""L-SI P-ACYC fixes entry 2: line L-3 = L-2 (docs/si/P-ACYC-line-L2.txt, sha1 3a3096a4…) with D-5 (REFEREE-2 32 Add. 2, claude/referee-2
d7ca68f4; string as routed by the Lead 03:06Z). The Old string must occur exactly once. Prints L-3. Usage: mkL3.py REPO_ROOT"""
import sys, os, hashlib
R = sys.argv[1]; L2 = open(os.path.join(R, "docs", "si", "P-ACYC-line-L2.txt"), "rb").read()
assert hashlib.sha1(L2).hexdigest() == "3a3096a45df6ca22e8099ca4e1a9ac1779c1321e", "L-2 changed"
L2 = L2.decode()
old, new = "along N5′-xi on Γ3 from S3 (pacyc81.py),", "along N5′-xi on Γ3 from S3 (pacyc81.py; τ by fix1/pacyc81t.py),"
assert L2.count(old) == 1
L3 = L2.replace(old, new); assert L3.count("(") == L3.count(")")
sys.stdout.write(L3)
