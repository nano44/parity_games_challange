#!/usr/bin/env python3
"""REFEREE-2 successor 35: byte test of P-N5-ASC line L-6 against L-5 (claude/l-new e28e962d, fe4d3f90…) + CHECKER 22's R6
(claude/checker 0ffde42c docs/checker/C135.md Add. 1). Own code. Usage: bt_l6.py L6_COMMIT [L6_PATH]  (run from the repo root)"""
import subprocess, sys, hashlib
def show(rev, p): return subprocess.run(["git", "show", f"{rev}:{p}"], capture_output=True, check=True).stdout.decode("utf-8")
L5 = show("e28e962d", "docs/new/P-N5-ASC-line-L5.txt")
print("L-5 sha1", hashlib.sha1(L5.encode()).hexdigest(), len(L5.encode()), "B")
old = ("(items 1..M compared by number, a run of forests with every chain lex-nondecreasing, an ascent a step to a larger item), "
       "a hub whose value has")
new = ("(items 1..M compared by number, a forest a map next from the items to the items and ⊥ without cycles, chain(x) := (x, next(x), "
       "next²(x), …) up to ⊥, compared as a set, a run of forests with every chain lex-nondecreasing, an ascent a step to a larger item), "
       "a hub (h_t an item or ⊥ at each time t, chain(⊥) := ∅, with chain_s(h_s) ≤ chain_t(h_t) for s < t) whose value chain_t(h_t) has")
print("old in L-5:", L5.count(old), " new in L-5:", L5.count(new))
exp = L5.replace(old, new)
print("expected L-6 sha1", hashlib.sha1(exp.encode()).hexdigest(), len(exp.encode()), "B", "parens", exp.count("("), exp.count(")"), "pipes", exp.count("|"))
if len(sys.argv) > 1:
    L6 = show(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "docs/new/P-N5-ASC-line-L6.txt")
    print("L-6 sha1", hashlib.sha1(L6.encode()).hexdigest(), len(L6.encode()), "B; old in L-6:", L6.count(old), " new in L-6:", L6.count(new))
    print("L-6 == L-5 + R6:", L6 == exp)
