# R-N5-OFFMONO-add3: REFEREE report on addendum 3 P-N5-OFFMONO-add3 (L-NEW box 49: Lemma OFFSET-MONO⁺, Corollary CHAIN-COUNT‴; every game)
Referee: REFEREE (successor 16), Opus 5.5 (owner ruling D15). FIRST referee (Lead message of 19:18Z by date -u).
- Object and pin: docs/new/P-N5-OFFMONO-add3-box49.md, sha1 b7cd0ff103ead10054c8f42f787369710f7feb40, 92 lines, author L-NEW successor 29:
  the same sha1 on my tree, at the l-new freeze 8b7e2e6e and at trunk 77f2664e (an ancestor of HEAD). Quote bases 3e03271f and c2a97189.
- Written 2026-10-26T19:20Z-19:24Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ file on add3 on my tree, on trunk or on origin/claude/referee-2 (re-listed in the same turn;
  0 / 0 / 0 at 19:23Z). No lane code run (experiments/new/box48/offmono3.py, quotecheck2.py neither executed nor imported). D1.
- Premises read against their text: P-N5-OFFMONO-box49 §0-§2 (setting, Step 1, Case N, Case L, CHAIN-SUM, EXIT_x); add1 §0 ((CYC-ID),
  (CYC-SHAPE)) and §2 (the charging proof); RESULTS R18 (d) Lemma S (a) (l. 803-804) with R57 (a) and 1E-N3; R38 (a) KEY (l. 1825); R56 (a);
  (SW) (l. 3768-3769); SPEC S1's order (l. 30).
- Quotes and pins: all 9 curly-quoted passages of §5 verbatim at their revisions (3e03271f: 7; c2a97189: 2), each ending at its cited line
  (scratch/fbc_quotes.py); the header's "c2a97189, l. 40-44, 58-60" and §4's "l. 58-59" point at the quoted text. Pins P-N5-OFFMONO-box49
  d9705ac6, add1 5911aba8, add2 f2d123ef, P-N5-FBPOLY-box41 de244dcd, P-N5-FBRED-box44 11b15455, SPEC 66fde9ef: match.
- Tool: scratch/add3_probe.py (own engine rl_engine; offmono_probe's κ, κwt, par; zch_probe's Z_t(c); checks in §3). Logs scratch/add3_logs/.

## Verdicts (sign-off line per item)
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | Lemma OFFSET-MONO⁺ (no honest-cycle hypothesis; Cases L1, L2) | SIGNED |
| §2 | Corollary CHAIN-COUNT‴ (sum form and D form; cut at EXIT_x only) | SIGNED (a REDUCTION to EXIT_x and D, both OPEN, as the packet says) |
| §3 | what becomes unnecessary in add1 / add2 | READING, not signed. It is consistent: the earlier cut forms follow from CHAIN-COUNT‴, and their lemmas are untouched |
| §4 | data | not signed |
No gap. It answers my predecessor's OFFADD-N2 / OFFMONO-N4: the CONJECTURE stated there is now PROVED (OFFSET-MONO⁺). Notes ADD3-N1..N3.
Nothing here bounds EXIT_x, D or N5's running time; not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. OFFSET-MONO⁺, re-derived (parentheticals checked one by one)
- Reduction ✓. q off every honest cycle at t: OFFSET-MONO itself. Otherwise q ∈ Z_t(c) by (CYC-ID), path-free, κ_t(q) = (0, s_c·ℓ) (CYC-SHAPE).
  Step 1 of OFFSET-MONO uses (Aκ) at t + 1 and t, (SW) and (M1κ) at the vertices of π. It needs π's vertices to be ≠ c and outside Q, and q's
  (t+1)-play to be simple before c. All of this holds whatever q's position at t ✓, so off_{t+1}(q; p) ⪰ κwt_c(q) + κ_t(y2) − κ_t(p) ✓.
  off_t(q; p) = κwt_c(q) + κ_t(y1) − κ_t(p) by (Aκ) at t (q ≠ c, next_t(q) = y1) ✓.
- y2 ∈ U_c, and y2's t-play ends in Z_t(c) ∋ q ✓, so it meets q ✓. One point the packet leaves implicit (ADD3-N1): y2 ≠ q. A self-loop at q
  would give λ_{t+1}(q) = q ≠ c against R38 (a); data: no y2 = q among the on-cycle checks.
- Case L1 ✓. ζ := y2's t-play up to q, before c, so c ∉ Z := q → ζ → q ✓. κ_t(y2) = κwt_c(Z) + κ_t(y1) by (Aκ) along ζ ✓. τ″ := σ̄_t[q ↦ y2]
  makes q's play the cycle Z ✓. Lemma S (a) with Ξ_t = L_{σ_t} (1E-N3) gives Ξ_t(q) ⊴ V″(q), with different cycle nodes, so reward(u*) >
  reward(c) ✓, and the rank argument gives κwt_c(Z) ⪰ (0, 0) ✓. That argument uses q only as the end of ζ ✓.
- Case L2 ✓. y2's t-play reaches c before q and avoids q up to c ✓. Under (σ_t, τ″) the play from q is q, y2's t-path to c, the arc of Z_t(c)
  from c to q, back to q: every vertex there except q keeps its choice ✓. The arc's vertices other than c rank below c (c is the top of Z_t(c))
  ✓, and q ranks below c (path-free) ✓.
  - P(Ξ_t y2) ≠ ∅: the new cycle's top u* = the top of P(Ξ_t y2), rank > rank(c) ✓; reward(u*) > reward(c) (Lemma S (a), different cycle
    nodes, injective rewards) ✓; u* odd would give reward −p′(u*) < min(±p′(c)) ✓, so u* even and M_t(y2) > 0 ✓; M_t(y1) = 0 since y1 lies on
    Z_t(c) or is c ✓ (CYC-SHAPE, A0κ). Strict ✓.
  - P(Ξ_t y2) = ∅: top c; V″(q) = (c, ∅, 1 + ℓ(Ξ_t y2)) = q ⊕ Ξ_t(y2) (rank(q) < rank(c)) ✓; (M1κ) with equal cycle nodes and (Aκ) at t give
    κ_t(y1) ⪯ κ_t(y2) ✓. (y2 = c falls here: V″(q) = (c, ∅, 1).)

## 2. CHAIN-COUNT‴, re-derived
- The charging proof is add1 §2's with the cut empty ✓. Every chain term is ⪰ (0, 0) by OFFSET-MONO⁺ at every level, on a cycle or not ✓.
  A strictly rising term is charged to (x, t) ✓, t ∈ EXIT_x or inside an x-piece‴ on which off(x; p) is non-decreasing ✓, distinct charges ✓,
  pieces ≤ |EXIT_x| + 1 ✓, |EXIT_x| + (D − 1)(|EXIT_x| + 1) ≤ D(|EXIT_x| + 1) ✓. "(so par(x) = p is constant on its states)" ✓.
- §3 READING ✓ as a reading: CYC_c, ZC_c and ZC″_c only add cut transitions, so they split pieces further and add a non-negative term. The
  three earlier corollaries follow; their lemmas (Z-CONST, ZCH-COUNT, FT-COUNT, FT-CONST, PF-CHOICE, TIE-CHARGE) are not affected.

## 3. Data (own engine; DATA, not proof; 0 failures of every signed check)
Checks: OMP (OFFSET-MONO⁺ at every in-phase transition and every q ∈ Q ∩ U ∖ {c}, split by q on / off an honest cycle at t), RED (on-cycle
q: κ_t(y2) ⪰ κ_t(y1), with the case L1 / L2a (P(Ξ_t y2) ≠ ∅, strict claimed) / L2b), ST1 (Step 1 at y2), CC3 (CHAIN-COUNT‴ sum and D forms,
J = the phase, D := the actual maximum of v_x over x-pieces‴).
| set (log in add3_logs/) | N5 runs | OMP on-cycle / off-cycle | L1 / L2a / L2b | ST1 | CC3 (Σ κ(q)-changes; max D) | failures |
| --- | --- | --- | --- | --- | --- | --- |
| lib 1,140 files, n ≤ 40 (4 parts), S3 + given + 2 random | 2,739 | 4,499 / 39,011 | 1 / 0 / 4,498 | 4,499 | 9,723 (10,910; 61) | 0 |
| lib41 (experiments/new/box41), n ≤ 64, S3 + 2 random | 1,130 | 855 / 15,231 | 0 / 0 / 855 | 855 | 2,559 (4,390; 52) | 0 |
| random 𝒞^kO, n 4-9, k ≤ 8, seed 351, S3 + 4 random | 100,000 | 4,036 / 13,403 | 0 / 0 / 4,036 | 4,036 | 16,654 (1,054; 3) | 0 |
| nep90 / nep76 / long121 at their starts | 3 | 0 / 1,208 | — | — | 13 (586; 69) | 0 |
- Case L1 occurs once, which the lane's data did not show: harm_n12_seed412 (experiments/new/instances/n5harm, sha1 5282c3f1), at its S3
  start, t = 1, c = 7, q = 10, y1 = 2, y2 = p = 11. y2's t-play is 11 → 10 → 2 → 8 → 3 → 7, so it meets q before c. Z = {10, 11} lies below c
  (c odd), κ_t(y2) − κ_t(y1) = (0, 5) − (0, 3) = (0, 2) = κwt_c(Z), and off(q; p) rises from (0, −1) to (0, 1). So L1's "otherwise" branch
  (wt_c(Z) = 0, c odd) is exercised once.
- Case L2a (P(Ξ_t y2) ≠ ∅, the strict sub-case) NEVER occurs in my data (0 of 9,390 on-cycle checks); it rests on PROOF ALONE (ADD3-N2).
- Controls (n ≤ 24 library, S3 + 2 random, 1,869 runs): MUT=1 (p off q's (t+1)-play, the lane's control) fails 361 on-cycle / 1,780
  off-cycle checks. MUT=2 (opposite length sign) fails 59 / 472. Both bite.

## 4. Notes (none blocks a signature)
- ADD3-N1 (proof, one clause). Say y2 ≠ q (a self-loop at q would make q its own cycle node at t + 1, against λ constant). Both cases need it.
- ADD3-N2 (DATA, vacuity). The strict sub-case L2a never occurs in my data; L1 occurs once. The landing text should carry "rests on proof
  alone" for L2a.
- ADD3-N3 (bookkeeping). With OFFSET-MONO⁺ signed, my predecessor's OFFADD-N2 (CONJECTURE candidate) and OFFMONO-N4 are answered. They should
  be marked "PROVED by P-N5-OFFMONO-add3" in the joint notes, not left as open conjectures.

DONE: this report. FINDINGS: OFFSET-MONO⁺ and CHAIN-COUNT‴ SIGNED, no gap; L1 exercised once (harm_n12_seed412), L2a never; ADD3-N1..N3.
NEEDS: Lead: route the notes to L-NEW's fixes file; §C against REFEREE-2 on your word.

## §C
The §C for this file is the UNIT §C at the end of docs/referee/R-N5-OFFMONO.md (OFFMONO + add1 + add2 + add3 against REFEREE-2 4e9a6372),
written 2026-10-28 by REFEREE successor 16: identical verdicts, joint gap map empty.
