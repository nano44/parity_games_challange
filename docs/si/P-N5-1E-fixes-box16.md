# P-N5-1E fixes (box 16 packet; repairs only)
L-SI successor 11 (Opus 5.5; D15, D18, L37, L40). Prepared and frozen at the Lead's request of 04:40Z (Lead's stamp), after both §Cs.
Stamp: the commit (date -u).
- Object: docs/si/P-N5-1E-box16.md, sha1 e613db131d3871c038f53fcb4e009c33f47ca20e (l-si adb721b5; pinned trunk 7fef9699). FROZEN, not
  edited.
- Repairs only. This file adds no new statement and no new proof.
- Sources (file sha1s by `git show <commit>:<path> | sha1sum`):
  - REFEREE successor 12, docs/referee/R-N5-1E.md: report at referee c82c4ecf (file sha1 83008110…), §C at 6170561a (bc36bda6…).
  - REFEREE-2, docs/referee-2/R2-N5-1E.md: report at referee-2 ceed1f63 (successor 13; file sha1 c4347337…), §C at bd68d39d (successor 14;
    05bcde50…).
- Both §Cs: identical verdicts, no gap, no NOT SIGNED statement.
- Verdicts. All five to-sign items are SIGNED by both referees: (VJ) on every game, Lemma OUT-G (every game), Lemma BIT-G (every game),
  Theorem 1E-POLY (parameter and uniform forms), Corollary 1E-TIME. §6 (READING) and §7 (DATA) are not signed.

## Lines (one per note)
- 1E-N1 (BIT-G, statement wording; REFEREE, accepted by REFEREE-2's §C: "missed by our side"). Read R51 (c)'s last sentence into Lemma
  BIT-G's statement (packet §3): "The longest-path recursion of S1 (iv) is memoised, with the same outputs as SPEC's recursion (BIT-N1)."
  - The packet's §3 statement quotes R51 (c) without it, while the proof uses it ("with BIT-N1: S1 (iv)'s recursion is memoised").
  - With the sentence, the statement is R51 (c)'s landed text with "on every parity game" added.
- 1E-N2 = N-1E-2 ((VJ), source check). Both referees checked premise (VJ) on every game against the VJ00 PDF (BRICS RS-00-48, sha256
  485a12de…) independently: §2 (finite game graphs, every vertex with a successor), §4.3 (Ωσ(v) = min over the plays from v consistent
  with σ), §5.2 (Prop. 5.1, Lemma 5.2, eq. (11), p. 16). Landing note.
- 1E-N3 = N-1E-1 (standing premise, to be named at landing). Lemma OUT-G is about SPEC's Ξσ and σ̄ as SPEC S1 defines them (Odd's
  optimal counterstrategy). That S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance; the code's match is DATA (R15
  G-N5T-1). This is the same standing premise as RESULTS R51 (d). The packet states it in §2 ("The remaining link …") and §6 honest
  limit (iii).
- N-1E-4 (Theorem 1E-POLY, parameter form; REFEREE-2, same substance in REFEREE's §C). The parameter form uses the PROOFS of R54 (c) and
  R54 (d), applied to the one game G^d, not their uniform statements, which quantify over all 𝒞^1O games with n vertices. The packet
  writes this out in §4 step 3. Proved, not a reading.
- N-1E-3 (REFEREE-2; CLOSED by REFEREE's §C). The two quoted lines of REFEREE's R-N5-DUAL §C C.2 exist as quoted
  (docs/referee/R-N5-DUAL.md l. 138). REFEREE-2 did not verify them, for independence, and did not need them: both referees checked T*'s
  monotonicity directly.
- 1E-N4 (DATA; REFEREE). OUT-G holds at all 34,808 states with Iσ = ∅ in REFEREE's probe, 13,707 of them with Iτ ≠ ∅. The data agree with
  "Iτ = ∅ is not used".
- N-1E-5 / §6 (READING; both referees concur). With OUT-G signed, the output-correctness half of R15's G-N5T-3 is removed on every game,
  under the standing premise 1E-N3. Not signed here. The Lead records it and decides on the gap row. The running-time half
  (G-N5-TIME) stays OPEN for general games.

## Data
- No referee asks for more. REFEREE: 11,000 random 𝒞^1E runs, 9,000 random runs of any class, 1,101 lib41 runs; 0 failures.
  REFEREE-2: 7,500 random 𝒞^1E runs, 4,000 of any class, 824 lib41 runs; 0 failures.
- Both note that runs are short and the bound is far above every count: the theorem rests on its proof.
