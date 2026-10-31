# R2-N5-STAIR-L1: P-N5-STAIR line, revision L-1, and its fixes file (REFEREE-2 successor 24, Opus 5.5, D15)
- Objects:
  - docs/new/P-N5-STAIR-line-L1.txt @ l-new 360d002f, sha1 d027f5d832d823c65a456080cde2e10d1a29f194 (re-hashed: match; one line, no
    heading marker);
  - docs/new/P-N5-STAIR-fixes-box112.md @ 360d002f, sha1 f07676f47f51ba991015b4e43d4406da4add57a4 (re-hashed: match; F0 and entries
    1-5).
- Base: the packet's §11 draft (9a58765f). L-1 is a rewrite, so I check it clause by clause against the signed items, not token by token.
- Written without opening REFEREE's verdict on L-1. The fixes file quotes REFEREE's report text, and I read those quotes.

## 1. My items
| item | L-1 | check |
| --- | --- | --- |
| STAIR-L1 (drop O-ARENA, [S4b-OPT]) | premises are R57, R15 (a), (d), R91 (XW, W-MON), R93 (LEX) and [PLAY]; no O-ARENA clause | ✓ met |
| STAIR-L2 (no heading marker; one line) | one line, starting «N5 on EVERY game» | ✓ met |
| STAIR-L3 (bind q, CS, N_F, β, q_j) | «W-run F = [p, q]»; «CS(x) := RESULTS R93 (a)'s coordinate sequence»; A_k and N_F defined; β defined; «first-difference position» and DESCENT defined | ✓ met |
| STAIR-L4 (RESET-ROOT, DESC-COPY as signed) | RESET-ROOT: «copied, through COPY, from a reset of W(y) at k, where y is the first Even vertex switched at k on v's (σ_(k+1), τ)-play before λ_W(v); hence TD_F ≤ n·Σ_k Σ_(y switched at k) …»; DESC-COPY: «if v ∉ C has a descent at k and did not switch at any transition from its previous change of W(v) on F to k, then its successor at k has a descent at k» | ✓ met, exactly the signed statements |
| STAIR-L5 («HDEPTH is DEAD») | dropped from the line; packet §8 (d) keeps the DEAD with its statement | ✓ met |
| STAIR-L6 (DESC-LIN DEAD) | «DESC-LIN (DESC_F ≤ c·n) DEAD (L-RED R162, claude/l-red 54832628: passive observers, cp_K)» | ✓ met |
| P-1 (COPY both ways) | «β(W(v)) and β(W(z)) have the same flips at k, in the same directions, through a strictly increasing position map» | ✓ applied |
| P-2 (RESET-ROOT «before λ_W(v)») | as above | ✓ applied |
| F-1 (sbq2 start) | fixes entry 3: start validation, repaired starts, a 501-pair scan; §8 corpus totals unchanged | ✓ (DATA; not in the line) |
- Every other clause states its signed item and nothing more:
  - SANDWICH, FROZEN (with «all three lie in [0, n(n + 2)]»), BW-ACC (with «T1_F ≤ N_F ≤ |F|»), BIT, BIT-ALT, FIRST-GOOD;
  - RESET-RED (both directions);
  - ASC-RUN, STAIR (both directions; «DESC_F ≤ n·WCT_F» = DESC ≤ Σ_v WCH ≤ n·WCT).
  TARGET.md scope words in the tail: ✓.

## 2. Fixes file
- Entry 1 (REFEREE's G-ST-1 together with my P-1): COPY's converse via the two constancy facts.
  - v ∉ P(W_j(z)), else v's W-play would revisit v before c.
  - z's unmatched end threshold bit is constant, since ℓ ≤ n − 1.
  - This is the bijection I checked in R2-N5-STAIR §3. **I SIGN Entry 1's repair** (Opus 5.5, D15). DESC-COPY's statement is unchanged.
- Entry 2 (P-2): ✓. Entry 4 (DESC-LIN DEAD): ✓, with my §4b reproduction quoted correctly. Entry 5 (O-ARENA withdrawn): ✓.
- Entry 3: the repaired starts keep the §8 corpus totals.
  - comp54_n80 → 11:11 is the same repair my start reader applies.
  - So my corpus totals (R2-N5-STAIR §4: 14,028 / 13,633 / 12,985 of 13,949 / 66,857 / 14,755) were on the repaired form already, and
    equal the lane's. ✓

## 3. Strict symbol test of L-1 (clause by clause)
- Bound by the global binder or the definitions: run, transition, k, F = [p, q], τ, C, λ_W, W_k, Ξ_k, T1_F, WCT_F, WCH_F(·), CS, lcp, BW_k,
  AF_k, A_k, N_F, M, β, sl, GOOD_F / BAD_F, TD_F, first-difference position, DESCENT, DESC_F(·), DESC_F, «v's successor at k», end.
- **STAIR-L1-1 (REQUIRED; the ODD-L1 class).** The vertex v and the bit b are unquantified in the lemma clauses: BIT-ALT («GOOD_F(v, b) ≤
  1 + BAD_F(v, b)»), FIRST-GOOD («every change of W(v)»), COPY («if v ∉ C has the same successor z …»), RESET-ROOT («every reset of W(v)»),
  DESC-COPY («if v ∉ C has a descent …») and ASC-RUN («WCH_F(v) ≤ …»).
  - The global binder quantifies only the run, F and k.
  - The same pattern («if Ξ_(k+1)(x) ≠ Ξ_k(x)») was REQUIRED in ODD (my ODD-L1), and L-SI applied it.
  - Fix (one phrase): «… every W-run F = [p, q] of it, every transition k → k + 1 of F, every vertex v and every bit position b:».
  - z is then bound by «the same successor z».
- Precision: «C-vertices keep the value (c, ∅, 0) on F» → «every c ∈ C keeps the value (c, ∅, 0) on F» (c is otherwise the generic cycle
  node of «(c, P, ℓ)»).
- No other free symbol.

## Verdict
L-1 (d027f5d8) with fixes f07676f4: **DOES NOT MATCH yet, one REQUIRED change STAIR-L1-1** (bind v and b in the global binder)
(Opus 5.5, D15). Everything else MATCHES:
- my STAIR-L1 to L6, P-1, P-2 and F-1 are met;
- Entry 1's G-ST-1 / P-1 repair is SIGNED.
