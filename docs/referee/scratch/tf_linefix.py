"""REFEREE successor 27: the required (TF-L1..TF-L3) and optional (TF-L4, TF-L5) changes to P-TOWER-FUEL's L-1, as exact
old/new pairs; asserts each old string occurs exactly once in L-1, applies them, prints the result's sha1 / size / paren balance."""
import sys, hashlib
L1 = open(sys.argv[1], encoding="utf-8").read()
PAIRS = [
 ("TF-L1", "DOUBLE-EQ 0 violations;",
  "DOUBLE-EQ 0 violations (no step moving both members and flips exactly at the steps moving a member: per (step, doubling level), 7,069; each member once per j-window: on the 757 j-windows; the same first mover: on the 61 doubling levels with F(j − 1) ≥ 1);"),
 ("TF-L2", "DOMINANCE-FREEZE 0 on 65,885 equal-decider state pairs and on 1,390 consecutive-move pairs;",
  "DOMINANCE-FREEZE 0 on 65,885 (consecutive-state pair, mover) units with equal deciders and on 1,390 (member of a doubling pair, pair of consecutive moves) units;"),
 ("TF-L3", "while 48 of its 127 6-windows fail, in each of which the crossed pair 6 is decided by the option (9, 1) of rank 87 (in none of the other 79)",
  "while 48 of its 127 6-windows do not contain one move of each of the movers 12 and 13 of the crossed pair 6, and in each of these 48 the option (9, 1) of rank 87 is dec_s(12) or dec_s(13) at some state s among s_(a−1), …, s_(e−1) of the window [a, e] (at no such state in any of the other 79)"),
 ("TF-L4", "the largest rank in the symmetric difference of the chains of A_0 and A_1",
  "the largest rank in the symmetric difference of the Ξ-chains of the current options of A_0 and A_1"),
 ("TF-L5", "violates PULSE, GAP ≥ 7 − j only at level 5, 30 times",
  "violates PULSE, GAP ≥ 7 − j (j = 1, …, 5) only at level 5, 30 times in 16 of its 63 5-windows"),
]
out = L1
for tag, old, new in PAIRS:
    n = L1.count(old); assert n == 1, (tag, n)
    assert out.count(old) == 1, (tag, "in progressive text")
    out = out.replace(old, new)
    print(tag, "old occurs once in L-1: OK; new occurs once in result:", out.count(new) == 1)
open(sys.argv[2], "w", encoding="utf-8").write(out)
b = out.encode()
print("proposed line: sha1", hashlib.sha1(b).hexdigest(), "bytes", len(b), "chars", len(out), "( =", out.count("("), ") =", out.count(")"))
print("L-1: ( =", L1.count("("), ") =", L1.count(")"))
