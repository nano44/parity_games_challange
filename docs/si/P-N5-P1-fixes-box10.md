# Fixes to packet P-N5-P1: REFEREE-2's N-P1-1 and REFEREE's §5 READING correction
L-SI successor 6 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~13:05Z (date -u), at the Lead's request (12:43Z).
- Object: docs/si/P-N5-P1-box10.md, sha1 b98ca7941264affe4bfe79cb72b744d2ab158e07, pinned trunk 48a8a4c. FROZEN, not edited.
- Sources: REFEREE successor 8, docs/referee/R-N5-P1.md (§1-§4 SIGNED; §5 checked with one correction); REFEREE-2 successor 8,
  docs/referee-2/R2-N5-P1.md (referee-2 e036e4c; all SIGN, note N-P1-1). Neither report lists a gap. Both sign Lemma B, Lemma M,
  Lemma P1 (Steps 1-6), Corollary P1′ and the §4 hypothesis match.
- A record of repairs, not itself refereed text.

## N-P1-1 (§3, wording; REFEREE-2)
- Step 4, add: "For m = 0 the chain is the single vertex x_0, and the claim is V(x_0) ⊵ₓ V(x_0), true by reflexivity (Lemma B (a))."
- Step 6, add after "Let v_b be the first visit of the σ′-play to c0": "If b = 0, then v_0 = c0 and both values are (c0, ∅, 0); the claim
  holds with equality. Otherwise apply Step 4 as written."
- Neither case changes any argument: Step 4's induction starts at i = m − 1 only when m ≥ 1.

## §5 READING, correction (REFEREE)
- Replace "BL (e), FREE-FREEZE, EV, EV+ and TEV-RED depend on (P) only through BL (c); with P1 they become PROVED without condition, once
  P1 is signed" with:
  "BL (b) applies (P) to G_τ and BL (c) to G_τ[F_k], so these become unconditional. BL (e), FREE-FREEZE, EV and EV+ depend on (P) only
  through BL (c) and also become unconditional. TEV-RED as stated is NOT signed (RL-1 / G-RL-1, a proof gap independent of (P)). What
  becomes unconditional is TEV-RED′, which carries the hypothesis 'no Ev vertex lies on the cycle of x_t's σ_t-play'. At t = k in the
  ENT setting that hypothesis is Lemma CYC-EV (docs/si/P-N5-RL-fixes-box10.md RL-1; packet P-N5-ENT §3), which uses no (P). EQ-END keeps
  its CN-LAST condition."
- Lane note (not part of the correction): packet P-N5-ENT (docs/si/P-N5-ENT-box11.md, sha1 4fd22be7) uses (P) only through EV+. With P1
  landed and EV+ signed unconditionally, Theorem ENT-X and Corollaries NJB-A, D1, PL-S″ would lose the condition once P-N5-ENT itself
  is signed.

## Concordance

| row | REFEREE (R-N5-P1) | REFEREE-2 (R2-N5-P1) | status | governing line |
| --- | --- | --- | --- | --- |
| 1 | — | N-P1-1 (trivial cases m = 0, b = 0) | wording | this file, N-P1-1 |
| 2 | §5 READING correction (TEV-RED′, not TEV-RED) | §5 READING agreed (scope: one-player only) | READING corrected; not a signed item | this file, §5 |
