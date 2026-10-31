# R-N5-STAIR: REFEREE report on packet P-N5-STAIR (L-NEW box 112): SANDWICH, FROZEN, BW-ACC, BIT / BIT-ALT / FIRST-GOOD, RESET-RED, COPY, RESET-ROOT, DESC-COPY, ASC-RUN, Theorem STAIR
Referee: REFEREE (successor 21), Opus 5.5 (D15). Lead brief 2026-10-31 12:40Z. REFEREE-2 reviews independently.
- Object and pin: docs/new/P-N5-STAIR-box112.md at claude/l-new 9a58765f. `git show 9a58765f:<path> | sha1sum` =
  3177124132afc1896438d148d8fbd4b7e2eaee52 (195 lines). This equals the Lead's figure. The RESULTS line draft is the packet's §11; no
  separate line file was given.
- Independence: I opened no docs/referee-2/ file for this packet.
- Lead reading L42, as relayed in the Lead's 12:40Z brief (not yet on trunk when I read DECISIONS.md): «O-ARENA is WITHDRAWN from the
  to-sign list. It needs [S4b-OPT] … which R57's premise does not cover. Do not sign it.» I do not sign O-ARENA.
- Scope (D1): REDUCTIONS and EQUIVALENCES on a W-run. No count is bounded. DESC-LIN is a CONJECTURE. G-N5-TIME stays OPEN.
- Every verdict below is labelled (Opus 5.5, D15).

## Verdicts
| § | item | verdict |
| --- | --- | --- |
| 1 | premises | CHECKED against landed text: R15 (a)/(d) (l. 624); R57 1E-N3; R91 Lemmas XW, W-MON (l. 6384); R93 (a) Fact LEX (l. 7031-7034); [PLAY] = P-N5-SRC §2 |
| 2 | Lemma O-ARENA | NOT SIGNED (withdrawn by L42). Nothing in §3-§7 uses O-ARENA or [S4b-OPT] (checked line by line) |
| 3 | Lemma SANDWICH; Corollary FROZEN (BW, AF, LS) | SIGNED |
| 4 | Lemma BW-ACC | SIGNED |
| 5 | Fact BIT; Lemmas BIT-ALT, FIRST-GOOD; Theorem RESET-RED (equivalence) | SIGNED |
| 6 | Lemma COPY | SIGNED, with proof-text gap G-ST-1 closed here (§6). The statement is unaffected |
| 6 | Corollaries RESET-ROOT, DESC-COPY | SIGNED (DESC-COPY uses COPY's converse, G-ST-1) |
| 7 | Lemma ASC-RUN; Theorem STAIR (equivalence) | SIGNED |
| 8-10 | DEADs, DATA, erratum, DESC-LIN | not to sign. The pins re-run PASS (§9). The §8 sbq2 figure rests on an invalid start (D-ODD-1 of R-N5-ODD) |
| 11 | RESULTS line draft | REQUIRED CHANGES STAIR-L1 to STAIR-L7 (§10) |

## 1. Premises
- [R15a] ✓ (as in R-N5-ODD §1).
- [XW], [W-MON]: RESULTS R91 heading, «(Lemmas XW, W-MON, …) Ξ_t ⊴ W_t pointwise, W does not fall at an S4a step (read with τ_t)».
  - On a W-run every transition is an S4a step with τ fixed. A τ-change or an S4c fallback ends F, and a step with Iσ = ∅ but Iτ ≠ ∅
    changes τ. So W_(k+1) ⊵ W_k on F ✓.
- [LEX]: R93 (a), «CS(x) := (rew(c); s_(n−1), …, s_0; ℓ̂) … x ◁ y iff CS(x) < CS(y) lexicographically». The length is n + 2, and
  s_r ∈ {0, +1} for even ranks and {0, −1} for odd ranks (two-valued) ✓.
- [PLAY]: P-N5-SRC §2. The packet's fixed-cycle-node form Φ(y; (c, P, ℓ)) = (c, P ∪ {y if more relevant}, ℓ + 1) needs y ≠ c. Every use
  has y ∉ C (COPY), so it is fine.
- [1E-N3] is not used directly in §3-§7, only through R91.

## 3. SANDWICH, FROZEN
- SANDWICH ✓.
  - If y first differs from x = z at j < i, then y < x or y > z.
  - For i < length: x_i < z_i, x_i ≤ y_i ≤ z_i, and y_i equals at most one of them.
  - If i = length, then x = y = z.
- FROZEN ✓. BW uses W_k ⊴ W_k′ ⊴ W_q. AF uses Ξ_k ⊴ Ξ_k′ ⊴ W_k′ ⊴ W_q. LS uses [R15a]. The range is n(n + 2) ✓.

## 4. BW-ACC
- Φ := M·BW − A ∈ [−n(n + 2), M·n(n + 2)].
- A BW-rise gives ΔΦ ≥ M − n(n + 2) = 1. A BW-flat A-fall gives ΔΦ ≥ 1. A transition in N_F gives ΔΦ ≥ −n(n + 2).
- Summing: |F| − N_F − n(n + 2)N_F ≤ (M + 1)n(n + 2), so |F| ≤ (M + 1)n(n + 2) + M·N_F ✓.
- W-constant ⇒ N_F, by SANDWICH with z = W_k = W_(k+1) ✓.

## 5. BIT, BIT-ALT, FIRST-GOOD, RESET-RED
- Fact BIT ✓.
  - The rank bits are [LEX]'s s_r, re-oriented so that 1 is Even-better.
  - The threshold vector ([sl ≥ j])_(j = −n … n) is lex-increasing in sl: the first difference between sl < sl′ is at j = sl + 1, where
    sl′ has 1.
  - |sl| ≤ n − 1.
  - Total length n + (2n + 1) = 3n + 1.
- BIT-ALT ✓ (alternation from the first value). FIRST-GOOD ✓ ([W-MON] + BIT; the cycle node is fixed on F).
- RESET-RED ✓. Changes inject into GOOD events at their first differing bit, and the per-vertex flip count gives the converse
  (≤ n(3n + 1) flips per transition).

## 6. COPY, RESET-ROOT, DESC-COPY
- COPY ✓.
  - W_j(v) = Φ(v; W_j(z)) with v ≠ λ_W(v) = λ_W(z) = c.
  - v's own rank bit is fixed. The other rank bits are copied. sl moves by ±1, with the sign fixed by c's parity, so threshold bit j of v
    is threshold bit j ∓ 1 of z.
  - The first-difference position map is strictly increasing on the positions that can move.
- G-ST-1 (a proof-text gap in COPY, CLOSED here; the statement is unaffected).
  - DESC-COPY uses the CONVERSE of COPY: «every change of z in (k′, k) would be copied to v». COPY states only «every flip of W(v) is a
    flip of W(z)». π_v discards z's bit at v's own rank and one end bit of z's threshold block, so the converse needs both to be
    constant on F.
  - The rank bit is constant: v ∉ P(W_j(z)), because z's W-path visiting v before c would make v's W-play (v, then z's play) revisit v
    before reaching c, so the cycle would not contain c = λ_W(v).
  - The end bit is constant: [ℓ(z) ≥ n] = 0 if c is odd, and [−ℓ(z) ≥ −n] = 1 if c is even, since ℓ ≤ n − 1.
  - So W(v) changes at a transition of COPY's hypothesis exactly when W(z) does, flip for flip.
- RESET-ROOT ✓.
  - If no Even vertex of v's new play switched, the play is unchanged and W(v) is unchanged.
  - On the unswitched prefix, each vertex has the same successor at k and k + 1, so COPY applies step by step. A C-vertex before y would
    freeze every W on the prefix, which is impossible.
  - y ∉ C for the same reason. The reset maps to a reset of W(y) (same direction, injective position map).
  - At most n pairs (v, b) map to one (y, b′) per k, which gives the factor n.
- DESC-COPY ✓. v is unswitched on [k′, k], so its successor is z at every state of [k′, k + 1].
  - By COPY and G-ST-1, W(z) changes in [k′, k] exactly at k′ and k.
  - The position map is strictly increasing, so q(z) rises from k′ to k: a descent of z at k.
  - z ∉ C, since otherwise v could not change.

## 7. ASC-RUN, STAIR
- ASC-RUN ✓. After change j, bit q_j is 1, and it stays 1 until the next change. A next change at the same first position would flip it
  0 → 1. Runs between descents have ≤ 3n + 1 members, and there are ≤ 1 + DESC_F(v) runs.
- STAIR ✓.
  - Ψ_p = n(3n + 1).
  - A first change counts as a fall (from 3n + 1 to ≤ 3n). An ascent lowers ψ by ≥ 1, and a descent raises it by ≤ 3n.
  - Descent-free W-changing transitions ≤ n(3n + 1) + 3n·DESC_F. Transitions with a descent ≤ DESC_F.
  - The converse is DESC_F ≤ Σ_v WCH_F(v) ≤ n·WCT_F ✓.

## 8. Not to sign
- O-ARENA, the RESET-STAIR remark, §8 DEADs and DATA, the §9 erratum, and §10 DESC-LIN.
- The erratum is right: W-MON is lexicographic, so lower bits may fall.

## 9. Controls (own engine; docs/referee/scratch/stair_probe.py, `python3 -I`, rl_engine; no lane code)
- Checks:
  - FROZEN (BW, AF never fall), BW-ACC, BIT (β order = SPEC order on every same-cycle-node pair of consecutive W and Ξ values), FIRST-GOOD;
  - RESET-RED, RESET-ROOT (first switched y on v's new play has a reset), ASC-RUN (and its WCH bound), STAIR's bound, DESC-COPY.
- Corpus: box 59 sbcg.lst ∪ alt_all.lst = 719 distinct games, MAXN 100 (656 analysed, 63 skipped), start file when present. Results:
  - 950 W-runs, 7,401 transitions, WCT 7,361, Σ WCH 28,319, TD 159,730, DESC 6,584;
  - checks: BIT 77,761, RESET-ROOT 23,907, DESC-COPY 2,447;
  - VIOLATIONS 0 (stair_logs/sum.txt).
- Pins:
  - x31_rx48 (with the box-107 start), u23sw64_n32 (start), tog6a_n32, hit_b6a_1 (start), hd_H40 (start): 12 W-runs, VIOLATIONS 0.
  - hd_H40: WCT 40, Σ WCH 2,420, DESC 0, TD 0. hit_b6a_1: WCT 38, Σ WCH 113, DESC 24. Both equal the lane's pinned figures.
- MUT controls:
  - MUT 1 (AF referenced to the moving W_k, the packet's remark A): bites, FROZEN_AF_V 33 on x31_rx48.
  - MUT 2 (β without parity orientation): bites, BIT_V 6,448 and FG_V 2,650.
- L-NEW's own check.sh blocks «box 107 FINPOT» to «box 111 STAIR» (experiments/new/check.sh l. 562-591 at 9a58765f), run alone in a
  detached worktree: all PASS, EXIT 0.
- Oink 8fbf0a7 `--zlk --verify` verifies the solution on x31_rx48, u23sw64_n32, tog6a_n32, hit_b6a_1, hd_H40 and obs_K12_m24.
- Every start file of these pins is valid (all moves are edges). But §8 DATA cites «sbq2_K8_m16 (L-SI box 54, 70f485cd…; faithfulness
  per their lanes) … 0 descents». That start has the non-edge 242 → 243 (R-N5-ODD §7, D-ODD-1), so this DATA figure is unfaithful as
  pinned. It is not a signed item.

## 10. RESULTS line draft (§11): strict symbol test
- REQUIRED changes:
  - STAIR-L1 (L42). Remove «and its S4b mirror [S4b-OPT]» from the premises and the (Lemma O-ARENA) clause.
  - STAIR-L2. |F| is used (BW-ACC, RESET-RED, STAIR) and never defined. Fix: «F = [p, q], |F| := q − p its number of transitions».
  - STAIR-L3. In FROZEN, q is undefined and «CS W_k» lacks its vertex. Fix: «Σ_v lcp(CS W_k(v), CS W_q(v)) and Σ_v lcp(CS Ξ_k(v),
    CS W_q(v)), q the last state of F, CS of RESULTS R93 (a)».
  - STAIR-L4. In BW-ACC, N_F (and the A it uses) is undefined. Fix: «A_k := Σ_v lcp(CS Ξ_k(v), CS W_k(v)), N_F := the transitions of F at
    which BW does not rise and A does not fall».
  - STAIR-L5. In RESET-RED, «TD_F the good-to-bad flips of W's oriented bits» leaves β undefined, and the constant 3n + 1 depends on it.
    Fix: define β (n parity-oriented rank bits and the 2n + 1 threshold bits [sl ≥ j]) and TD_F := Σ_(v, b) the 1 → 0 flips of bit b of
    β(W(v)) on F.
  - STAIR-L6. «(COPY, RESET-ROOT, DESC-COPY) resets and descents are copied from switched vertices» is not a checkable statement. Fix:
    state RESET-ROOT (TD_F ≤ n·Σ_k Σ_(y switched at k) the resets of W(y) at k) and DESC-COPY as in the packet, or drop the clause.
  - STAIR-L7. F is introduced only in the premise parenthesis («W-run F as in RESULTS R89»), k is unbound, and DESC_F needs «descent»
    defined. Fix: «for every N5 run on every game, every W-run F = [p, q] of it and every state k of F: …», and «a descent of v := a W(v)
    change whose first differing β-position is less significant than that of v's previous change on F».
- Precision:
  - STAIR is an EQUIVALENCE: add the converse (DESC_F ≤ n·WCT_F), as RESET-RED's line should (TD_F ≤ (3n + 1)·n·WCT_F).
  - Cite [PLAY] as «P-N5-SRC §2 (proof of RESULTS R97 PLAY-CAUSE^S)».
  - The line file must carry no heading marker («R?? [refereed-only]»; C104 N-1, L41).
- TARGET.md diff: «REDUCTIONS and EQUIVALENCES (no count is bounded here; DESC-LIN is a CONJECTURE; HDEPTH is DEAD (hit_b6a_1); G-N5-TIME
  stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim)» ✓. No algorithm claim.
- Verdict: the line does NOT yet match. It needs STAIR-L1 to STAIR-L7.

## DONE / FINDINGS / NEEDS
- DONE: this report; stair_probe.py; stair_logs/.
- FINDINGS:
  1. Every item to sign (L42 list) is SIGNED. G-ST-1 (COPY's converse, used by DESC-COPY) is closed here. Nothing is FALSE.
  2. O-ARENA is not signed, and nothing else uses it or [S4b-OPT].
  3. The line draft needs STAIR-L1 to STAIR-L7.
  4. §8's sbq2 DATA figure inherits D-ODD-1 (the invalid start).
- NEEDS: Lead: route STAIR-L1..L7 and G-ST-1 to an L-NEW successor (docs/new/P-N5-STAIR-fixes-box112.md), with a line file without a
  heading marker.
