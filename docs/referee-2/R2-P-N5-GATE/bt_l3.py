#!/usr/bin/env python3
# REFEREE-2 successor 37: byte test of P-N5-GATE line L-3 (claude/l-si ef14451f) against the combined requirements of R2-P-N5-GATE
# Addendum 1 (8983b3d8). Usage: bt_l3.py L3.txt L2.txt. Own code; mkL3.py is not imported.
import sys, hashlib, difflib
L3, L2 = (open(p, encoding="utf-8").read() for p in sys.argv[1:3]); raw = open(sys.argv[1], "rb").read(); fails = 0
def ck(n, ok, info=""):
    global fails; fails += not ok; print(("PASS " if ok else "FAIL ") + n + (" :: " + info if info else ""))
ck("sha1 b60495b2", hashlib.sha1(raw).hexdigest().startswith("b60495b2"), f"{hashlib.sha1(raw).hexdigest()} {len(raw)}")
ck("one line, no |, parens", L3.count("\n") == 1 and "|" not in L3 and L3.count("(") == L3.count(")"), f"{L3.count('(')}")
for bad in ["§2 (a)", "P-N5-CHAIN's C-EQUIV", "lie on both of two plays", "not a premise here", "not among P-N5-CHAIN", "while its play avoids",
            "over the run then", "CTRL=a0", "is a hypothesis here", "L-RED R228", "afail", "pxfail", "box 94's 22 instances"]:
    ck("absent: " + bad, bad not in L3)
REQ = {
 "R-1/R-10 R125 list": "on Γ3 instead RESULTS R125 (P-N5-CHAIN): F1, F3, F4′, F6, STRICT, CN2-3, LOC-GATE3, NO-TIE3, LOC-K2-3, B-ONLY3, E-MON3, and F2, CYC, (E-DOM), (Core) from P-N5-CHAIN's frozen text (l-new 93531b03, sha1 6e613ba7, §2 and §4)",
 "R-1 (Core) repaired": "(Core) in its W-1-repaired reading, applied only to non-core vertices (the faces of a gate and the successors of a mover or a gate; P-N5-CHAIN fixes entry 3, R-W; referee-originated: REFEREE-2 R2-P-N5-GATE G-1)",
 "R-10 SPLIT cited as packet": "for A*-EQUIV also SPLIT-COUNT and C-EQUIV of P-N5-SPLIT (L-NEW, frozen claude/l-new 399cda07, sha1 5bc1b1f3)",
 "R-5a / 31:R-4": "(b) F1, F2, F3, F4′'s stated clause, F6, (c) STRICT, (e) in its per-vertex form",
 "R-5b / 31:R-5": "RESULTS R123 Lemmas CN2, LOC-GATE, LOC-K2, B-ONLY",
 "R-5c / 31:R-6": "and (E-DOM) and (Core) read off RESULTS R104's priorities and closed core with LOC-K2 (non-core vertices only",
 "R-4 / 31:R-1": "so no P-N5-SPLIT premise is used)",
 "31:R-1 §3 (a)": "P-N5-SPLIT §3 (a), Lemma REWIN (a)",
 "R-3 / 31:R-3": "C ≤ A*_all ≤ 1 + M·C (on both runs, with no P-N5-SPLIT premise",
 "R-3 Γ3 only": "and, on Γ3 only, C ≤ 3M·(1 + M·A*_route)",
 "R-3 C-EQUIV SPLIT's": "PROVED-CONDITIONAL on P-N5-SPLIT's SPLIT-COUNT and C-EQUIV)",
 "R-8a G-7": "referee-originated: REFEREE-2 R2-P-N5-GATE G-7",
 "R-8b G-6": "(at most 3M split pairs: the split is a mover or a gate, with M mover edges and 2M faces; referee-originated: REFEREE-2 R2-P-N5-GATE G-6)",
 "R-7a": "so if D's play avoids e_o at every state of the run then",
 "R-7b": "(Lemma WAIT-QUIET) a gate whose D's play avoids e_o at every state of the run and whose D changes value at most K times unlocks",
 "R-6a / G-a": "on Γ3 it does not occur either, by RESULTS R125's B-ONLY3",
 "R-6b / G-b": "on Γ3 it holds at every state 0, …, T3 by RESULTS R125's B-ONLY3 at the mover D",
 "31:D-1": "(unit: Odd vertex with two successors for grfail and gr2fail, flip for grwhy and trfail;",
 "31:D-2": "decfail 0 (unit (gate, state): the decider is at least as relevant as e_o; (a)'s order equivalence is not counted by the lane), glnfail and lowflip 0 (unit: flip with LAM ∧ PRIV at t − 1 and t;",
 "31:D-3": "unlfail (unlocks > 1 + ch_(p_e); the bounds unlocks ≤ 1 + relocks and unlocks ≤ ch_(p_b) are not counted by the lane)",
 "31:D-4 / R-9": "copy rows S(R_j) = S(R_(j−1)) as sets on every level of box 94's 20 simultaneous-clock instances (all but NSQ2_4, NSQ3_4",
 "31:D-5a": "PARALLEL: par1-3 0 (unit: change of H with an expelled letter, at route tuples; x's position after u′ not counted)",
 "source note": "with its fixes entries 1-3",
}
for k, s in REQ.items(): ck("present: " + k, L3.count(s) == 1, str(L3.count(s)))
a, b = L2.split(" "), L3.split(" ")
n = sum(1 for op in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if op[0] != "equal")
ck("changed regions L-2 -> L-3 read one by one (46)", n == 46, str(n))
print("FAILS", fails)
