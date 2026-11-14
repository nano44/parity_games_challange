#!/usr/bin/env python3
# REFEREE-2 successor 37: line requirements for P-N5-GATE's L-3 as exact old -> new strings against L-2 (9c0349b1, sha1 c0f2007d).
# Asserts each Old once in L-2; applies all to produce the REQUIRED-TEXT reference (l3req_applied.txt) for the byte test. Usage: l3req.py L2.txt OUT
import sys, hashlib
L = open(sys.argv[1], encoding="utf-8").read()
assert hashlib.sha1(L.encode()).hexdigest().startswith("c0f2007d")
REQ = [
 ("R-1/R-10", "on Γ3 instead the facts F1, F2, F3, F4′, F6, STRICT, CYC, CN2-3, LOC-GATE3, NO-TIE3, (E-DOM), (Core), E-MON3 of the pending packet P-N5-CHAIN (L-NEW, frozen claude/l-new 93531b03, landing as R125); for PAIR-EXPEL, EXPEL-COUNT and A*-EQUIV also §2 (a), SPLIT-COUNT and C-EQUIV of the pending packet P-N5-SPLIT (L-NEW, frozen claude/l-new 399cda07, referees pending)",
  "on Γ3 instead RESULTS R125 (P-N5-CHAIN): F1, F3, F4′, F6, STRICT, CN2-3, LOC-GATE3, NO-TIE3, LOC-K2-3, B-ONLY3, E-MON3, and F2, CYC, (E-DOM), (Core) from P-N5-CHAIN's frozen text (l-new 93531b03, sha1 6e613ba7, §2 and §4), (Core) in its W-1-repaired reading, applied only to non-core vertices (the faces of a gate and the successors of a mover or a gate; P-N5-CHAIN fixes entry 3, R-W; referee-originated: REFEREE-2 R2-P-N5-GATE G-1); for A*-EQUIV also SPLIT-COUNT and C-EQUIV of P-N5-SPLIT (L-NEW, frozen claude/l-new 399cda07, sha1 5bc1b1f3)"),
 ("R-5a", "(b) F1, F2, F3, (e) in its per-vertex form",
  "(b) F1, F2, F3 and F4′'s stated clause, (c) STRICT, (e) in its per-vertex form"),
 ("R-5b", "RESULTS R123 Lemmas CN2, LOC-GATE, B-ONLY",
  "RESULTS R123 Lemmas CN2, LOC-GATE, LOC-K2, B-ONLY"),
 ("R-5c", "for IDEAL-CYC; on Γ3 instead",
  "and (E-DOM), (Core) on Γ read off RESULTS R104's priorities and core edges (non-core vertices only), for IDEAL-CYC; on Γ3 instead"),
 ("R-4", "(Lemma PAIR-EXPEL, PROVED-CONDITIONAL on P-N5-SPLIT §2 (a))",
  "(Lemma PAIR-EXPEL)"),
 ("R-3/R-5d", "(Corollary A*-EQUIV, PROVED-CONDITIONAL on P-N5-SPLIT's SPLIT-COUNT and P-N5-CHAIN's C-EQUIV)",
  "(Corollary A*-EQUIV, on Γ3 only, PROVED-CONDITIONAL on P-N5-SPLIT's SPLIT-COUNT and C-EQUIV)"),
 ("R-8a", "C ≤ A*_all ≤ 1 + M·C and",
  "C ≤ A*_all ≤ 1 + M·C (each entry of a top starts a run, and every run but one starts at a change; referee-originated: REFEREE-2 R2-P-N5-GATE G-7) and"),
 ("R-8b", "is at most 1 + 3M·max Dhi_z,",
  "is at most 1 + 3M·max Dhi_z (at most 3M split pairs: the split is a mover or a gate, with M mover edges and 2M faces; referee-originated: REFEREE-2 R2-P-N5-GATE G-6),"),
 ("R-7a", "so if D's play avoids e_o over the run then",
  "so if D's play avoids e_o at every state of the run then"),
 ("R-7b", "(Lemma WAIT-QUIET) a gate whose D changes value at most K times while its play avoids e_o unlocks",
  "(Lemma WAIT-QUIET) a gate whose D's play avoids e_o at every state of the run and whose D changes value at most K times unlocks"),
 ("R-6a", "while on Γ3 that case needs B-ONLY on Γ3, which is not a premise here (OPEN within this entry, covered by E-FACE-PAYS (a) only)",
  "and on Γ3 it does not occur either, by RESULTS R125's B-ONLY3 (pβ_o is never an exception; pe_o is one only when D = c_W, and then Λ(pe_o) = c_W ≠ Λ(pβ_o); referee-originated: REFEREE-2 R2-P-N5-GATE G-5)"),
 ("R-6b", "while on Γ3 the proviso is a hypothesis here",
  "and on Γ3 it holds at every state by RESULTS R125's B-ONLY3 at the mover D, by the same argument (referee-originated: REFEREE-2 R2-P-N5-GATE G-5)"),
 ("R-9", "SAME-SUFFIX: copy rows",
  "SAME-SUFFIX (a record of box 94's nesting families, not a test of the lemma's statement): copy rows"),
]
out = L; ok = True
for rid, old, new in REQ:
    c = L.count(old); print(rid, "old occurs", c, "PASS" if c == 1 else "FAIL"); ok &= c == 1
    out = out.replace(old, new)
open(sys.argv[2], "w", encoding="utf-8").write(out)
print("applied sha1", hashlib.sha1(out.encode()).hexdigest(), len(out.encode()), "B; parens", out.count("("), out.count(")"), "; ALL", "PASS" if ok else "FAIL")
