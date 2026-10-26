# P-N5-2T fixes (box 16 packet; repairs only)
L-SI successor 11 (Opus 5.5; D15, D18, L37, L40). Prepared and frozen at the Lead's request of 05:30Z (Lead's stamp), after both §Cs.
Stamp: the commit (date -u).
- Object: docs/si/P-N5-2T-box16.md, sha1 fcb91130b1f93d041233c9def50614b4d0dc9a05 (l-si f6839fd3). FROZEN, not edited. CONDITIONAL on
  RESULTS R56, as the packet states.
- Repairs only. This file adds no new statement and no new proof.
- Sources (file sha1s by `git show <commit>:<path> | sha1sum`):
  - REFEREE successor 12, docs/referee/R-N5-2T.md: report at referee 7055b4a5 (file sha1 ec0868a6…); §C at 09b5dbf5 (940c0b17…) and
    906247c6 (f7247dd4…).
  - REFEREE-2, docs/referee-2/R2-N5-2T.md: report at referee-2 8f43432b (4ba16a42…) and 416334cc (dcf9ef7a…); §C at 3d8de145 (20ec6fd7…).
- Both §Cs: identical verdicts, no gap, no NOT SIGNED statement. All seven statements are SIGNED by both, conditional on R56: (YB_q),
  PFZ-q, ROUTE-2, DIR, SAT-2, Theorem FB-2T, Corollary FB-2O. §6 (READING) and §7 (DATA) are not signed.

## Lines (one per note)
- 2T-N1 = N-2T-4 (FB-2O's case list). Add the case "q1 and q2 are both cycle nodes of their classes". Then no class has a terminal,
  every Q_c = ∅, and FB-2T gives N_late ≤ 1. The bound f ≤ 1 + (n − 1)(1 + 12n²) holds a fortiori.
- N-2T-1 (provenance; REFEREE accepted it in §C, having missed it). The κ-FB-ROUND line in packet §1 (under "R56 (a), (b) lemmas used")
  quotes FBRED §1.1, l. 52 ("FBP §1 verbatim with U_c, c"), not R56's landed text. R56 (a) signs "κ-FB-ROUND_D (FBP §0.3, §1 with c for
  c_θ)". The statement is unchanged; read the quote as FBRED's.
- 2T-N3 = N-2T-5 (FB-2T step 3, wording). The count is over DISTINCT VALUES of the pair (a_i, b_i), not over indices i. Read "the pairs
  with a = α number ≤ w_c + |V_{q′}(α)|" as "the distinct values of b on I_α number ≤ w_c + |V_{q′}(α)|". The bound on N′_c, and so the
  theorem, is unchanged.
- N-2T-2 ((YB_q)). (YB_q) is proved in the packet (§2), not cited: it is not in R56's signed text. REFEREE-2 checked the proof as complete.
- N-2T-3 (PFZ-q). The weakening from Q_c-runs to q-runs is safe: the proof reads a terminal's κ only at q, and only at states of Θ (t, or
  k ∈ Θ). Constancy of the other terminals is never used. (Both referees.)
- 2T-N2 (DIR's scope; also REFEREE-2's R2-N5-FBK §0). DIR's proof uses only "q is direct". It never uses |Q_c| ≤ 2, so DIR holds in any
  class, with "direct" meaning "on its own honest cycle, or visits c before any other terminal of Q_c". The statement as signed is
  unchanged. This is the form in which L-NEW's P-N5-FBK cites it.
- N-2T-6 / 2T-N4 (DATA).
  - SAT-2's hypothesis was met only on REFEREE-2's constructed unions, on two engines, with 0 violations.
  - FB-2T's late regime (fallbacks g_j with j ≥ n) is never reached in any sample.
  - DIR is checked a few dozen times. PFZ-q, (YB_q) and ROUTE-2 are exercised often: REFEREE, PFZ 169,165 checks with 0 failures; the
    mutation bites.
  - So DIR, SAT-2 and FB-2T rest on their proofs, as the packet says (§7).
