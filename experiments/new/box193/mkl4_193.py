#!/usr/bin/env python3
# P-N5-ASC line L-4 generator (L-NEW successor 63). From the repo root: python3 experiments/new/box193/mkl4_193.py
# L-4 = L-3 + R5 (REFEREE 28, R-P-N5-ASC.md §E at claude/referee 013f821b): CHAIN-DECOMP's hypothesis as the packet's l. 80.
# Asserts the old string occurs once in L-3, and REFEREE's predicted sha1 4017305a34eac21615ba8f172a9b899544d25659 (5,198 B, 125 / 125).
import hashlib
OLD = "(Lemma CHAIN-DECOMP) if the first e-vertex on v's play is f, then"
NEW = "(Lemma CHAIN-DECOMP) if seq_t(v) = (f, …), i.e. the first e-vertex on v's play is f and f ∈ Π_t(v), then"
L = open("docs/new/P-N5-ASC-line-L3.txt", encoding="utf-8").read()
assert L.count(OLD) == 1, L.count(OLD)
L = L.replace(OLD, NEW); b = L.encode("utf-8"); h = hashlib.sha1(b).hexdigest()
print("R5 old once, applied; sha1", h, len(b), "bytes; parens", L.count("("), L.count(")"))
assert h == "4017305a34eac21615ba8f172a9b899544d25659" and len(b) == 5198 and L.count("(") == L.count(")") == 125
assert L.count("\n") == 1 and "|" not in L
open("docs/new/P-N5-ASC-line-L4.txt", "w", encoding="utf-8").write(L)
