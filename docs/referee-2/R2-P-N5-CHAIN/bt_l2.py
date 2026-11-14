#!/usr/bin/env python3
"""REFEREE-2 successor 35: byte test of P-N5-CHAIN line L-2 (claude/l-new 8b67d40e) against L-1 (71b75424, bd152dd9…) + CL-1 (as fixes
entry 1 / mkl2_196.py state it; REFEREE 29's report NOT read), and the place of my R-1, R-2, R-4, N-1 old strings in L-2. Own code."""
import subprocess, hashlib, difflib
def show(rev, p): return subprocess.run(["git", "show", f"{rev}:{p}"], capture_output=True, check=True).stdout.decode("utf-8")
L1 = show("71b75424", "docs/new/P-N5-CHAIN-line-L1.txt"); L2 = show("8b67d40e", "docs/new/P-N5-CHAIN-line-L2.txt")
h = lambda s: hashlib.sha1(s.encode()).hexdigest()
print("L-1", h(L1), len(L1.encode()), "B;  L-2", h(L2), len(L2.encode()), "B; parens", L2.count("("), L2.count(")"), "pipes", L2.count("|"), "lines", L2.count("\n"))
sm = difflib.SequenceMatcher(None, L1, L2, autojunk=False)
ops = [o for o in sm.get_opcodes() if o[0] != "equal"]
lo, hi = ops[0][1], ops[-1][2]; lo2, hi2 = ops[0][3], ops[-1][4]
print("changed region in L-1 [", lo, hi, ") vs L-2 [", lo2, hi2, ")")
print("L-1 side:", L1[lo:hi]); print("L-2 side:", L2[lo2:hi2])
print("outside the region equal:", L1[:lo] == L2[:lo2] and L1[hi:] == L2[hi2:])
for k, s in [("R-1", "QUIET3: wfail 0 (unit: quiet windows)"), ("R-2", "T-QUIET3: Tfail 0 (unit: runs)"),
             ("R-3", "controls fire (every fail counter has one):"), ("R-4", "LOC-K2-3: k2fail 0 (unit: states)"),
             ("N-1", "spec on 100 runs and 5 pinned genomes, check196.out)")]:
    print(k, "old string count in L-2:", L2.count(s))
