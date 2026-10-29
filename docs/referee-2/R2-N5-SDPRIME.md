# R2-N5-SDPRIME: REFEREE-2 report on packet P-N5-SDPRIME (box 25): Theorem STATIC-DEPTH′, its Remark (contains R77 (c)), Corollary EPOCH
Referee: REFEREE-2 successor 19 (session_01V5yGRZzoAVpZvqB1LedCVF), Opus 5.5 (D15, L37). Written 2026-10-29 from 04:05Z (date -u).
Object: docs/si/P-N5-SDPRIME-box25.md, sha1 54678c38a04842bd936a9bf4b241d47ad8ab90a3 (measured with `git show <ref>:<path> | sha1sum` at l-si edc14c51
and origin/claude/l-si: both equal the pin; not on trunk at 04:04Z), 106 lines, frozen. Author L-SI successor 21. Quote base 55e0bcbda.
INDEPENDENCE:
- I have not opened any file under docs/referee/ on SDPRIME and have not run `git log` on origin/claude/referee.
- Name count `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic sdprime`: 0 at 2026-10-29 04:04:20Z; 0 at 2026-10-29 04:12:45Z (push turn, after `git fetch origin claude/referee`). Names only.
Lane tools (experiments/si/piece/sdprime.py, epochs.py, experiments/si/rund/quotecheck.py) NOT run or imported.
Checker: docs/referee-2/R2-N5-SDPRIME/sdprime_check.py (own; reuses my lane's R2-N5-DEPTH/depth_check.py only for cycles(), H_b and d*, R77's
objects); quotes with ../R2-N5-CORE/qcheck.py; run_all.sh; logs/.
- N5 on G: my lane's SPEC loop (dual_check.Runner on si.py = SPEC S1, read-only).
- Ξ, W: my own play values.
- T_W, T_H, the recursion dW / dH / d, (H4′) in both of its forms, J_b, and the epochs are all built from the packet's definitions.
Scope (D1): structural lemmas inside one phase. Pieces with CF ≥ 1 and pieces outside the hypotheses are not bounded (CONJECTURE PIECE OPEN). Not
a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Verdicts (all "(Opus 5.5, D15)")
| § | item | verdict |
| --- | --- | --- |
| §2 | Theorem STATIC-DEPTH′ (hypotheses (H1′), (H2), (H3′), (H4′), GEN_W) | SIGN |
| §2 | (H4′)'s equivalence (recursion well founded ⇔ J_b acyclic) and d(v) = vertices of a longest J_b-path | SIGN (proof steps; checked) |
| §2 | Remark: STATIC-DEPTH′ contains RESULTS R77 (c) | SIGN |
| §3 | Corollary EPOCH (b − a ≤ (CF + 1)·n − 1, with (H4′) and GEN_W at every epoch end) | SIGN (a REDUCTION; GEN_W wording, N-SD-2) |
| §1 | quotes | 11/12 VERBATIM in the tagged lines. 1 not verbatim: the (SW) quote at RESULTS l. 3768-3769 inserts "…" where the source has only a line break (N-SD-1; content identical). SHIFT=1 control 0/12 |
| §4 | data, CONJECTURE PIECE, CONJECTURE STATIC-DEPTH′-TIE | not signed |
No gap. Notes N-SD-1..7.

## 1. Proof check (against RESULTS R77's landed text, R80 (a), R18 (d) / P2, (SW) and SPEC)
- Premises.
  - R77 (c)'s proof steps (W-MONO) and (Ξ-SUCC) are landed as facts on in-phase S4a transitions. Neither uses λ_W.
    - W-MONO: σ_t lies in S4a's arena, so the arena optimum's W dominates W_t (R18 (d) Lemma S (a), P2).
    - Ξ-SUCC: (SW) together with pointwise Ξ-monotonicity.
    - Data: 0 failures of either at the 283 + 657 + 24 + 56 transitions where λ_W changes (WMONO_lw, XSUCC_lw).
  - R77's third step (CV) (cycle vertices constant, from (H1), (H3)) is replaced here by item 1, from (H3′). This is the right replacement:
    only the end state's cycles are used as constant.
  - R80 (a) EVERY-SWITCH is landed (R80) in the form quoted.
- Item 1. A vertex on a W-cycle Z at b keeps Z as its W-play at every t, since Z is a W-cycle there by (H3′). Likewise for honest cycles. An
  Even vertex of T has σ_t(v) = its successor on that cycle = σ_b(v). ✓
- Item 2 (Odd v ∉ T_W, resp. ∉ T_H). τ(v)'s W-play at b avoids v, otherwise v would lie on its W-cycle at b. So settling passes back one step.
  For the honest frame, σ̄ is constant by (H2). ✓
- Item 3. Even v ∈ T_H ∖ T_W keeps σ_b(v) by item 1, and item 2's argument applies. Symmetric for T_W ∖ T_H. ✓
- Item 4 (A).
  - If y ∉ {σ_t v} ∪ Iσ_t(v), totality of the S1 order gives Ξ_t(y) ⊴ Ξ_t(σ_t v).
  - The last switch t′ ≥ t of v to y gives Ξ_{t′}(y) ▷ Ξ_{t′}(σ_{t′} v) by (SW).
  - Ξ-SUCC gives Ξ_{t′}(σ_{t′} v) ⊵ Ξ_t(σ_t v). y is H-settled at t and t′, so Ξ_t(y) = Ξ_{t′}(y): a valuation is a function of the play.
  - That is a contradiction. ✓ (Checked as STEPA: 10,540,227 + 8,589,064 + 38,414 instances.)
- Item 4 (B).
  - s′ uses state-t arena edges: (A) at v, and S4a's output at every other vertex.
  - y's W-play under σ_{t+1} is its play at b (W-settled, t + 1 > s). It avoids v, so it is also y's play under s′, and W_{s′}(v) = W_b(v).
  - Lemma S (a) (pointwise greatest) gives ⊵; W-MONO from t + 1 to b gives ⊴. ✓ (STEPB: 9,531,639 + 7,602,983 + 29,715.)
- Item 4 (C).
  - The cycle node c of W_b(v) lies on the W-cycle Z of b, which is a W-cycle at t + 1 by (H3′). So v's W-play at t + 1, which has cycle node c,
    ends in Z.
  - GEN_W (two W-plays from v to the same cycle with equal valuations) makes the two plays equal. So σ_{t+1}(v) = y.
  - The honest step then follows from y H-settled and v ∉ T_H. ✓
  - GEN_W is used only in the form "W-plays of v at two states of [a, b] with equal W-valuation are equal". My checker tests exactly that form
    per interval.
- Item 5.
  - For t ≥ a + max d, σ_t = σ_b, so a transition inside [a + max d, b] would contradict R80 (a). ✓
  - d(v) = 1 + max(d(J_b-successors)), and J_b is acyclic and visits distinct Even vertices outside T. So max d ≤ |Even ∖ T| ≤ n − 1, with
    T ≠ ∅. ✓
- (H4′)'s parenthetical: a recursion cycle meeting no Even vertex outside T stays in one frame's dependency chain. That chain follows that
  frame's successor map at b (τ or σ̄ at Odd vertices, σ_b at the Even vertices of the other frame's T). So it would be a cycle of that map at
  b, hence inside that frame's T, where the recursion stops. ✓
  - Checked: H4EQ (recursion well founded ⇔ J_b acyclic) and DEQ (dW = dH = longest J_b-path count on Even ∖ T), 0 failures. (H4′) fails at
    4 + 28 (H3′)-intervals.
- Remark (contains R77 (c)).
  - R77's (H3) gives (H3′) with T_W = T_H.
  - The W-play and the honest play at b are H_b-paths: Odd v ∉ D has τ(v) = σ̄(v), and u ∈ D keeps both edges in H_b. So a J_b-edge is an H_b-path
    outside the cycle vertices, and (H4) ⇒ (H4′) and d ≤ d*. ✓
  - Checked on every interval with R77's (H1)-(H4) (λ_W constant, the two frames' cycles equal and constant, H_b acyclic): (H3′) and (H4′) hold
    and d(v) ≤ d*(v) on 26,103 + 47,270 + 475 intervals (REM, REM_d: 0).
- Corollary EPOCH.
  - The epochs are built backwards with a_k least. They tile [a, b], so b − a = Σ (b_i − a_i) + (k − 1), and each epoch has (H3′) by
    construction.
  - For i ≥ 2, minimality makes state a_i − 1 fail (H3′) for [a_i − 1, b_i], while [a_i, b_i] passes. So some cycle of b_i is a cycle at a_i
    but not at a_i − 1: it appears at a_i − 1 → a_i. These transitions are distinct, so k − 1 ≤ CF.
  - With STATIC-DEPTH′ per epoch, b − a ≤ kn − 1 ≤ (CF + 1)n − 1. ✓
  - Checked: EPcut, EPsum, EPh3, EPAPP (the appearing cycle found at every cut), EPCF, EPlen and EPOCH. 0 failures on 1,133 + 1,812 + 91 + random
    pieces.

## 2. Data (own checker; every non-mutation run 0 violations)
| corpus | runs | pieces | (H3′) intervals (SDCAP 60) | with GEN_W (used form) | beyond R77's hypotheses | T_W ≠ T_H | λ_W moves | other cycles come and go | R77 intervals (REM) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alt_all (413, given start else S3; start validation: 1 entry) | 413 | 1,133 | 32,404 | 32,268 | 6,297 | 6,158 | 562 | 3 | 26,103 |
| lib41_noref × 3 | 1,230 | 1,812 | 52,303 | 52,102 | 5,005 | 4,811 | 681 | 0 | 47,270 |
| named (si/root/instances 7, nep90_n40) | 8 | 91 | 634 | 634 | 159 | 159 | 159 | 3 | 475 |
| random kO n 8-20 / k2 n 6-16 / k4 n 8-20 (3,000 / 3,000 / 2,000 games × 3) | 24,000 | see logs | 968 (kO) | 968 | 93 (kO) | 93 | 1 | 0 | 875 |
- Longest STATIC-DEPTH′ interval: 55 transitions (x32_rand64, n 64, max d 56). The bound b − a = max d is attained (sharp) in 369 + 429 intervals.
- Intervals without GEN_W (used form) that satisfy the other hypotheses: 132 + 173. Every per-vertex and length conclusion still held there (no
  FAIL_noGEN counter): consistent with CONJECTURE STATIC-DEPTH′-TIE (not signed).
- EPOCH:
  - at most 6 epochs and CF ≤ 5 per piece (tog6a_n32), as §4 says;
  - pieces with every hypothesis at every epoch end: 1,121 + 1,785, of them with CF ≥ 1: 24 + 50;
  - k − 1 = CF in 1,133 + 1,812 of the pieces;
  - no piece with b − a > n − 1 (counter pieces_over_n_minus_1 absent), consistent with CONJECTURE PIECE.
- Controls (SD_MUT; on lib41 × 3 and random kO):
  - dm1 (settling demanded from a + d − 1) bites 19,355 + 923 (SETW, SETH);
  - onlyH ((H3′) demanded for honest cycles only) bites 3,009 + 38, LEN 23 + 1 among them: the length bound itself fails;
  - onlyW (W-cycles only) bites 368 + 30, LEN 7.
  - So both halves of (H3′) carry the theorem, and the depth is exact (the d − 1 bound fails).

## 3. Notes (not gaps)
- N-SD-1 (quote).
  - [Q docs/RESULTS.md@55e0bcbda:3768-3769] «(SW): every Even switch of N5 is to an edge … of Iσ». The source reads "(SW): every Even switch of N5
    is to an edge" / "of Iσ" over a line break.
  - The "…" marks an omission that does not exist. Content identical; 11/12 quotes verbatim by my strict checker.
  - The lane's quotecheck presumably treats "…" as a wildcard.
- N-SD-2 (GEN_W "at every epoch end").
  - GEN_W as defined in R77 (c) is a property of (G, τ), and τ is fixed on the phase. So "GEN_W at every epoch end" in EPOCH is either redundant
    or means the used form per epoch.
  - The proof needs only the used form per epoch, which is what I checked. Wording.
- N-SD-3 (thin spot). The packet's "cycles other than the end state's may come and go" is exercised in only 3 + 0 + 3 intervals.
  - The two other new freedoms are well exercised: T_W ≠ T_H (6,158 + 4,811 + 159) and λ_W moving (562 + 681 + 159).
  - EPOCH with CF ≥ 1 and all hypotheses: 24 + 50 pieces.
- N-SD-4 ((H4′) is not vacuous). It fails at 4 + 28 (H3′)-intervals. GEN_W's used form fails at 230 + 343 intervals (most outside (H3′)).
- N-SD-5 (premise use). Ξ-SUCC needs only (SW) and pointwise Ξ-monotonicity (R15 (a), (d)). The (M2κ) citation inherited from R77 is fine
  but stronger than needed.
- N-SD-6 (R77's (CV) step). STATIC-DEPTH′'s proof does not use R77's (CV) (cycle vertices constant). It uses item 1, which holds only for the
  end-state cycles. This is what allows other cycles to come and go; the packet says so implicitly.
- N-SD-7 (§4 counts, not to sign).
  - My piece counts (1,133 alt_all, 1,812 lib41 × 3) differ from §4's (872 alt_all, 943 lib41). The piece notion or runs per game probably
    differ: mine are maximal σ̄-constant sub-runs with ≥ 1 transition of every fallback-free in-phase run.
  - I count sub-intervals, not whole pieces, so the "844 of 872" figure is not directly comparable.

## 4. DONE / FINDINGS / NEEDS
- DONE: this report; docs/referee-2/R2-N5-SDPRIME/{sdprime_check.py, named.lst, run_all.sh, logs/}.
- FINDINGS: STATIC-DEPTH′, its Remark and Corollary EPOCH all SIGN, no gap. Both halves of (H3′) are needed (the onlyW / onlyH controls break
  the length bound), and the d bound is exact (dm1). One quote carries a spurious "…" (N-SD-1). "Other cycles come and go" is barely exercised
  (N-SD-3).
- NEEDS: Lead: the §C word (REFEREE reviews in parallel; I have not opened docs/referee/ on SDPRIME); route N-SD-1..7 to L-SI.
