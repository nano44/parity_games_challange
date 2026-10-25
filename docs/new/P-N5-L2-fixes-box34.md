# P-N5-L2 fixes file (box 34)
L-NEW successor 15 (Opus 5.5, D15/D18). Written 2026-10-25 08:5xZ by date -u, at the Lead's request (08:48Z). It answers the referee
reports on packet docs/new/P-N5-L2-box34.md (pinned trunk 04b3f48, sha1 cbea07392521bcdfbce137ba361bb581f9df11d7; never edited). This
file is a record of the repairs: the packet stays the object, and these lines replace or extend the named lines.
- REFEREE: docs/referee/R-N5-L2.md (referee 7626354). All seven statements signed, two with wording gaps. REFEREE-2: pending.

## 1. REFEREE gaps (both accepted; REFEREE's lines adopted verbatim)
- L2-1 (§2 Lemma H2-STICK, wording). Before "¬H2 at s: τ(o) ∈ R_s", add:
  "If τ(o) = o, ¬H2 holds at every state with this τ, in particular at s+1; assume τ(o) ≠ o below."
  - Reason: R excludes o, so "τ(o) ∈ R_s" is false when τ(o) = o, and R-STICK says nothing about o. The claim is trivial there: o's W-play
    is its self-loop at every state of the phase (τ is a phase constant). REFEREE counts 400 of the 520 library S4a steps with H1 ∧ ¬H2
    in this case. My box-35 survey of fallbacks found the same split: 91 of 104 (docs/new/N5-DROP-box35.md §5).
  - The Corollary (H2 states form a prefix of a fallback-free run with H1 throughout) is unchanged.
- L2-2 (§6 Lemma H1-INT (b), wording). Replace "every state k with H1 at k and ¬H1 at k+1" with:
  "every state k such that k → k+1 is a transition of the phase with H1 at k and ¬H1 at k+1".
  - Reason: R30 (f) H1-DROP is signed for k → k+1 inside a phase. Read literally, with k + 1 in the next phase, the clause is false. Witness:
    docs/referee/R-N5-L2/exitdrop_n3.pg (sha1 73c7a21b07e37c504bfdc8922fde9456deb5195e, n 3). The proof already cites the in-phase form.
  - Downstream: every later use (§7 X-RUN′, §8, docs/new/N5-DROP-box35.md, packet P-N5-TOG) concerns drops inside a phase.
    P-N5-TOG §3 does not use (b) at all: it reproves P(θ) = ∅ at ¬H1 states from its fact (F).

## 2. REFEREE's FINDING on §8 (not a gap; §8 was not to sign)
- DEAD END: CONJECTURE DROP-LEN (θ changes between two drops of a phase) and its weak form (≤ 1 drop per fallback-free run) are both FALSE.
  - Instance: docs/referee/R-N5-L2/droplen_cex_n12.pg (sha1 a6af26db3f75540aa0f519cf0420b890fd2d4cc9, n 12, o = 0).
  - Lane re-run (L-NEW succ. 15): n5.py n5 gives 4 iterations and 0 fallbacks. check_sol2.py gives "zielonka(oink zlk) OK strategies
    verified". One phase; θ = w = (2, ∅, 1) at every state. H1 toggles at every transition (states 0, 2 and 4 are ¬H1), so the drops are
    1 → 2 and 3 → 4, both S4a. Each transition is one S4a switch of σ(2), and 2 = c_θ is an odd own cycle node: 0 → 1 → 7 → 9 → 10.
  - The weak form was already refuted by onerun_cex_n32 (N5-DROP-box35 §3). The new content is that θ need not change at all.
- What holds the count instead: Theorem TOGGLE (P-N5-TOG, pinned d3daae1). togz.py on droplen_cex_n12: 4 toggles, 3 by σ(c) only and 1 by
  Z and σ(c), 0 failures. L-MONO there: Ω(2) odd, so L rises strictly at each σ(2) switch.
