# R2-N5-STAIR: second-referee report on P-N5-STAIR (REFEREE-2 successor 24, Opus 5.5, D15)
- Object: docs/new/P-N5-STAIR-box112.md @ l-new 9a58765f, sha1 3177124132afc1896438d148d8fbd4b7e2eaee52 (re-hashed: match), 195 lines.
  The RESULTS line is the draft in packet §11 (no separate line file at 9a58765f).
- Independence: written before opening any docs/referee/ file on STAIR.
- Scope: REDUCTIONS / EQUIVALENCES inside W-runs. Nothing is bounded. G-N5-TIME stays OPEN. DESC-LIN is a CONJECTURE.
- Lead brief 12:40Z: sign SANDWICH, FROZEN, BW-ACC, BIT / BIT-ALT / FIRST-GOOD, RESET-RED, COPY, RESET-ROOT, DESC-COPY, ASC-RUN and
  Theorem STAIR.
  - Lead reading L42, quoted from the brief (not yet in docs/DECISIONS.md at trunk): «O-ARENA is WITHDRAWN from the to-sign list (it needs
    [S4b-OPT], which R57's premise does not cover). Do not sign it; check that nothing else uses it.»

## 1. Claims table
| § | item | verdict | gap |
| --- | --- | --- | --- |
| 2 | Lemma O-ARENA | NOT SIGNED (withdrawn, L42) | — |
| 3 | Lemma SANDWICH | SIGNED | none |
| 3 | Corollary FROZEN (BW, AF, LS non-decreasing) | SIGNED | none |
| 4 | Lemma BW-ACC | SIGNED | none |
| 5 | Fact BIT, Lemma BIT-ALT, Lemma FIRST-GOOD | SIGNED | none |
| 5 | Theorem RESET-RED (both directions) | SIGNED | none |
| 6 | Lemma COPY | SIGNED | none (precision P-1) |
| 6 | Corollary RESET-ROOT | SIGNED | none (precision P-2) |
| 6 | Corollary DESC-COPY | SIGNED | none |
| 7 | Lemma ASC-RUN | SIGNED | none |
| 7 | Theorem STAIR (both directions) | SIGNED | none |
| 8-10 | DEAD ends, DATA, erratum, DESC-LIN | not signed | DATA note F-1 (sbq2 start) |
| 11 | RESULTS line draft | REQUIRED changes STAIR-L1 to L6 (§5) | — |
- Gap map: EMPTY.

## 2. Premises against the landed text (trunk at this report's merge)
- [1E-N3]: R57's standing premise, as R96 / R97 quote it: «for S4a at a transition k → k + 1, σ_(k+1) is the pointwise optimum of the
  one-player arena H_k». ✓
- [R15a]: Ξ non-decreasing at every S4a step, as R96 / R97 use it. ✓
- [XW], [W-MON]: R91 (l. 6384), «Ξ_t ⊴ W_t pointwise, W does not fall at an S4a step (read with τ_t)». On a W-run every transition is an
  S4a step with τ fixed (R97 / [SET] §1), so W_(k+1) ⊵ W_k on F. ✓
- [LEX]: R93 (l. 6972) defines the coordinate sequence: reward of the cycle node; for each rank r from n − 1 down to 0, +1 / −1 / 0; length,
  negated when the cycle node has even priority. It states that the SPEC S1 order is lexicographic in it. The length is n + 2. ✓ My tool
  checks CS order = engine order on every compared pair (LEXK).
- [PLAY]: R97 (l. 8032), the proof of PLAY-CAUSE^S, which I signed (R2-N5-SRC §2). Φ(y; (c, P, ℓ)) = (c, P ∪ {y if more relevant}, ℓ + 1)
  needs y off the suffix path. COPY satisfies this: v ∉ C, and z's W-path to c avoids v. ✓
- O-ARENA and [S4b-OPT] occur only in packet l. 7 (to-sign list), l. 28-29 ([S4b-OPT]), §2 (l. 40-47), the §11 line draft (l. 179, 181) and
  the DONE / NEEDS notes. §3-§7 use neither: grep, and a read of every proof. ✓

## 3. Item checks
- SANDWICH. With i = lcp(x, z):
  - a first difference of y from x (or z) at j < i would put y outside [x, z];
  - at i, x_i < z_i and x_i ≤ y_i ≤ z_i, so y_i differs from one of them. ✓
- FROZEN. Per vertex:
  - W_k ⊴ W_k′ ⊴ W_q ([W-MON] iterated);
  - Ξ_k ⊴ Ξ_k′ ⊴ W_k′ ⊴ W_q ([R15a], [XW], [W-MON]);
  - Ξ_k ⊴ Ξ_k′ ⊴ Ξ_end.
  SANDWICH gives lcp(x, z) ≤ lcp(y, z). The range n(n + 2) comes from lcp ≤ n + 2. ✓
- BW-ACC. Φ = M·BW − A with A ∈ [0, n(n + 2)] and M − n(n + 2) = 1:
  - a BW-rise gives ΔΦ ≥ 1, and a BW-flat A-fall gives ΔΦ ≥ 1;
  - an N_F transition gives ΔΦ ≥ −n(n + 2);
  - summing gives |F| ≤ (M + 1)n(n + 2) + (1 + n(n + 2))N_F = (M + 1)n(n + 2) + M·N_F.
  W-constant transitions are in N_F: Ξ_k ⊴ Ξ_(k+1) ⊴ W, so A does not fall (SANDWICH). ✓
- BIT.
  - Rank bits are oriented so that 1 is better for Even at the first differing rank (Q1).
  - The threshold vector [sl ≥ j], j = −n … n, is 1…10…0 with sl + n + 1 ones, so it is lex-increasing in sl.
  - sl = ℓ (c odd) or −ℓ (c even), so larger sl is better.
  - |sl| ≤ n.
  - β is injective on values with one cycle node. ✓
- BIT-ALT: a 0/1 sequence alternates. ✓ FIRST-GOOD: a W-change is a strict rise with the same cycle node, so the first differing β bit
  goes 0 → 1. ✓
- RESET-RED.
  - Each change of W(v) has its own GOOD flip, so WCH(v) ≤ Σ_b GOOD ≤ (3n + 1) + Σ_b BAD. Summing gives n(3n + 1) + TD.
  - |F| = T1 + WCT and WCT ≤ Σ_v WCH.
  - Converse: a change has ≤ 3n + 1 flips, and Σ_v WCH ≤ n·WCT. ✓
- COPY.
  - W_j(v) = Φ(v; W_j(z)) on the fixed cycle node c = λ_W(v).
  - v's own rank bit is constant: v ∉ P(z), and [v ∈ P(v)] depends only on v versus c.
  - The other rank bits are copied.
  - sl(v) = sl(z) ± 1, with the sign fixed by c's parity, so v's threshold bit at j is z's at j ∓ 1.
  - The one bit of v outside z's range is constant (1 below, 0 above).
  - The one bit of z with no image is constant too: [sl(z) ≥ n] = 0 when ℓ(z) ≤ n − 1, and [sl(z) ≥ −n] = 1.
  - So the non-constant bits of v and z correspond bijectively and in order, which is stronger than the packet's «every flip of W(v) is a
    flip of W(z)».
  - The position map (identity on ranks, shift ±1 on thresholds) is strictly increasing. ✓
  - P-1 (precision): the packet states one direction («every flip of W(v) at k is a flip of W(z)»). DESC-COPY also uses the converse
    («every change of z in (k′, k) would be copied to v»), which holds by the bijection above. Suggest stating COPY as «β(W(v)) and
    β(W(z)) have the same flips, through an increasing position map».
- RESET-ROOT.
  - Follow v's W_(k+1)-path.
  - If no Even vertex before c switched, the path up to c is unchanged and W(v) is unchanged (R1 of R97: W(v) reads only the path up to c).
    So the first switched Even y lies before c and y ∉ C.
  - COPY along the unswitched prefix carries v's reset bit to a reset bit of y, by an injective position map.
  - So each (y, bit) at k receives at most one bit per v, which gives TD ≤ n·Σ.
  - P-2 (precision): «Its first vertex y that is Even and switched» should read «… before λ_W(v)». A switched C-node c (a CN switch) has
    the constant value (c, ∅, 0) and cannot carry a reset. The proof's «the prefix does not pass one before y» says this, but the
    statement does not.
- DESC-COPY.
  - On [k′, k + 1] v's successor is z.
  - By COPY's bijection, z changes exactly when v does, in (k′, k).
  - So z's consecutive changes are at k′ and k, and the increasing position map carries v's descent to z's. ✓
- ASC-RUN.
  - After change j, bit q_j is 1 and stays 1 until the next change.
  - A next change with the same first-difference position would flip it 0 → 1: impossible.
  - Non-descents strictly decrease, over 3n + 1 positions. ✓
- STAIR.
  - Ψ starts at ≤ n(3n + 1) (initial ψ = 3n + 1 per vertex) and ends ≥ 0.
  - An ascent (a first change included, since 3n + 1 > every position) lowers ψ by ≥ 1, and a descent raises it by ≤ 3n.
  - Descent-free W-changing transitions lower Ψ by ≥ 1, so they number ≤ n(3n + 1) + 3n·DESC_F. Add ≤ DESC_F others.
  - Converse: DESC ≤ Σ WCH ≤ n·WCT. ✓

## 4. Mechanical checks and pins (own code)
- Tool: docs/referee-2/R2-N5-STAIR/stair_check.py.
  - It is my LATEP state loop with my WRUN start reader. The lane's box107-111 tools are not imported.
  - CS and β are built from the packet text, and every claim is checked per W-run.
  - Logs: R2-N5-STAIR/logs.
- Pins, all from 9a58765f:
  - hd_H40 (be553fc9, start 1bec3b9b): one W-run [0, 40], n 122, |F| 40, WCT 40, WCH 2420, DESC 0, TD 0. This equals the lane's «WT 40 WCT
    40 WCH 2420 … TD 0» and «DESC 0».
  - hit_b6a_1 (ff1cd2f9, start 89ae7c5b): three W-runs, 9 + 6 + 23 = 38 transitions, WCH 10 + 33 + 70 = 113, DESC 0 + 12 + 12 = 24. This
    equals the lane's «WT 38 WCH 113 DESC 24» (the lane sums over W-runs).
  - x31_rx48 (34b44d5d, start b3ba35d9): W-run [36, 50] has 14 transitions, 13 of them T4 (all W-changing; the longest consecutive T4 run is
    13). Over the game T4 = 17 (4 + 13), the lane's «T4 17». DEAD (a) reproduced.
  - u23sw64_n32 (18b46837, start c69511c1): W-run [1, 9], 8 transitions, WCT 0. DEAD (b)'s W-constant interval is reproduced.
  - tog6a_n32 (fd0e2c7e, start 85953cf5): W-run [4, 9], 5 transitions, 1 W-constant. That is consistent with DEAD (c) at k = 8.
  - obs_K12_m24 (7df541fb, start 23db47dd): one W-run [0, 324], DESC 12. This is DEAD (e)'s count.
  - All pins: 0 violations.
- Corpus (box 50b's 1,132 games; the same run set as the lane):
| run | runs | violations | W-run transitions | BW rises | W-changing | with a reset | Σ WCH | DESC | T4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sbcg.lst (runs=1) | 719 | 0 | 6,921 | 6,729 | 6,882 | 6,440 | 40,934 | 9,885 | 142 |
| alt_all, with start (runs=0) | 94 | 0 | 2,842 | 2,791 | 2,839 | 2,649 | 13,108 | 2,448 | 34 |
| alt_all, start-less (runs=1) | 319 | 0 | 4,265 | 4,113 | 4,228 | 3,896 | 12,815 | 2,422 | 115 |
| total | 1,132 | 0 | 14,028 | 13,633 | 13,949 | 12,985 | 66,857 | 14,755 | 291 |
- Every total equals the lane's §8 DATA exactly: 14,028 W-run transitions; BW rises at 13,633; resets at 12,985 of 13,949 W-changing
  transitions; Σ_v WCH 66,857 against DESC 14,755.
- RESET-ROOT holds at every reset: ROOT checks 59,285, 0 violations; the lane's 12,985 / 12,985 counts transitions.
- Random 300 games (seed 31, n 5-12, 4 starts): 0 violations.

## 4b. R162 (DESC-LIN DEAD): pins re-run with my tool
- Pins from claude/l-red 54832628, experiments/red/desc/instances, with their start files:
  - cp_K4: one W-run [0, 44], n 192, |F| 44, WCH 3904, DESC 388. That is R162's «| 4 | 192 | 44 | … | 388 |» (DESC/n 2.02).
  - suf_K4: one W-run [0, 44], n 103, |F| 44, DESC 28. That is R162's DESC column, 28.
  - 0 violations of every STAIR check. DESC grows past any c·n while |F| stays at 44: DESC-LIN is DEAD as R162 says.
  - STAIR's bound |F| ≤ T1 + n(3n + 1) + (3n + 1)·DESC holds (WCT 44).
- R162's STAIR-U (lane-proved) is not reviewed here.

## 5. RESULTS line draft (§11): strict symbol test, TARGET.md scope words
- **STAIR-L1 (REQUIRED, L42).** Remove «and its S4b mirror [S4b-OPT]» from the premises and the clause «(Lemma O-ARENA) W_k is σ_k's
  best-response value with Odd restricted to O(τ) = τ ∪ Iτ;». O-ARENA is withdrawn, and nothing else in the line needs [S4b-OPT].
- **STAIR-L2 (REQUIRED).** «R?? [refereed-only]» is a heading marker. Lanes write lines without one (L41 / C104 N-1). The line is also a
  bulleted multi-line draft; it should be one line in its own file.
- **STAIR-L3 (REQUIRED; unbound symbols).**
  - q in «CS W_q»: F = [p, q] is not written in the line.
  - CS: write «CS := RESULTS R93's coordinate sequence».
  - N_F in BW-ACC: undefined in the line. Write «N_F := the transitions of F at which Σ_v lcp(CS W_k, CS W_q) does not rise and A_k :=
    Σ_v lcp(CS Ξ_k, CS W_k) does not fall».
  - «W's oriented bits» (β) and «first-difference positions» need their definitions: β as in packet §5, and q_j(v) as in DESC-COPY.
- **STAIR-L4 (REQUIRED; wider than signed).** «(COPY, RESET-ROOT, DESC-COPY) resets and descents are copied from switched vertices» is
  not what was signed.
  - RESET-ROOT roots every reset at a switched Even vertex before λ_W(v).
  - DESC-COPY copies a descent of an UNSWITCHED v to its successor, not «from switched vertices».
  - Fix: state the two corollaries as in the packet. For example: «every reset of W(v) at k is copied from a reset of W(y) for the first Even
    y switched at k on v's W_(k+1)-path before λ_W(v), so TD_F ≤ n Σ_k Σ_(y switched at k) (resets of W(y) at k); a descent of v at k
    with v unswitched since its previous change is a descent of its successor».
- **STAIR-L5 (REQUIRED, DATA scope).** «HDEPTH is DEAD (hit_b6a_1)» is a DEAD label for a statement the line never defines. Name it
  («h^W ≤ 2 (box 107)») or drop it. TARGET.md scope words: «REDUCTIONS and EQUIVALENCES (no count is bounded here; … G-N5-TIME stays OPEN;
  not M3, not a step-4 pass, not a TARGET.md claim)» ✓.
- **STAIR-L6 (REQUIRED, scope tail; Lead 13:04Z).** «DESC-LIN is a CONJECTURE» → «DESC-LIN DEAD (L-RED R162, claude/l-red 54832628)».
  - R162: passive observer copies of obs (family cp_K) give DESC ≈ n²/88 with |F| unchanged.
  - My stair_check.py on R162's pin cp_K4 is in R2-N5-STAIR §4b.
  - The signed claims are unaffected, since Theorem STAIR is an EQUIVALENCE (DESC is not bounded).
  - The packet's §10 is likewise superseded.
- Precision: n is bound fleet-wide by TARGET.md l. 8.

## 6. Findings
- F-1 (DATA, not to sign). §8 lists «sbq2_K8_m16 (L-SI box 54, 70f485cd…; faithfulness per their lanes) have 0 descents». The box-54 start
  file of that game (experiments/si/src54/inst/sbq2_K8_m16.start, sha1 98b0927a) sets «TAU0 … 242:243».
  - 243 is not a successor of the Odd vertex 242 (succ(242) = 244, 246, …, 258).
  - My runner (no validation, τ(242) = 243 kept) shows τ(242) = 243 at all 153 states. Every play through 242 uses a non-edge.
  - L-NEW's n5x.start_pair applies start entries without validation.
  - So that DATA point is on a non-game. It does not affect any signed item. The same instance carries L-SI's box-54 DEAD
    (R2-N5-ODD.md F-1).

## Verdict (Opus 5.5, D15)
- SIGNED: SANDWICH, FROZEN, BW-ACC, BIT, BIT-ALT, FIRST-GOOD, RESET-RED, COPY, RESET-ROOT, DESC-COPY, ASC-RUN and Theorem STAIR.
- NOT SIGNED: O-ARENA (L42). Nothing else uses it.
- Gap map: EMPTY. Precisions P-1 (COPY's two directions) and P-2 (RESET-ROOT «before λ_W(v)»).
- Line draft: REQUIRED STAIR-L1 to STAIR-L6.
- DATA finding F-1.
