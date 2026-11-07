# P-N5-STAIR (box 112): frozen ceilings, resets and the staircase on a W-run — a referee packet from L-NEW boxes 107-111
FROZEN 2026-10-31 (date -u: see the commit), L-NEW successor 41. For REFEREE and REFEREE-2.
- Scope: a REDUCTION / EQUIVALENCE. No count is bounded here; G-N5-TIME stays OPEN; DESC-LIN is a CONJECTURE; not M3, not a step-4 pass,
  not a TARGET.md claim.
- Source notes, history only: docs/new/N5-FINPOT-box107.md, N5-HDEPTH-box108.md, N5-WIDTH-box110.md, N5-STAIR-box111.md. This packet
  restates everything it uses; the notes are not needed to check it.
- To sign: §2 O-ARENA; §3 SANDWICH, FROZEN; §4 BW-ACC; §5 BIT, BIT-ALT, FIRST-GOOD, RESET-RED; §6 COPY, RESET-ROOT, DESC-COPY; §7 ASC-RUN,
  Theorem STAIR.
- Not to sign: §8 (DEAD ends, DATA), §9 (erratum), §10 (CONJECTURE DESC-LIN).
- Not included (by the Lead's 12:13Z scope): HIER-RED and its depth hierarchy (vacuous on L-RED R159's hd_H), CARRIER / GATE,
  NEW-EDGE / ARENA-RED, NO-LAG.

## 1. Setting, premises (all landed or SPEC)
- N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md). A run is the sequence of states (σ_k, τ_k); a transition is k → k + 1.
- Values (c, P, ℓ) are VJ valuations: cycle node, path set (vertices more relevant than c on the path to the first occurrence of c),
  length. ⊴ ◁ ⊵ ▷ is the SPEC S1 order (better for Even).
- Ξ_k := Ξ_{σ_k} (the (σ_k, σ̄_k)-play valuation, σ̄_k S1's Odd counterstrategy). Iσ_k := {(y, z) Even edge : Ξ_k(z) ▷ Ξ_k(σ_k y)}
  (SPEC S2). Iτ_k := Odd's improving edges for τ_k on the dual (SPEC S2).
- W-run F = [p, q] := RESULTS R89's: a maximal run of consecutive states of one τ-stretch, none of whose transitions is an S4c fallback
  or changes λ_W. On F, τ and C := {v : λ_W(v) = v} are fixed.
  - W_k := the valuation of the (σ_k, τ)-plays.
  - H_k := S4a's Even arena at k: Even y keeps {σ_k(y)} ∪ Iσ_k(y), Odd follows τ.
  - |F| := q − p, the transitions of F.
  - T1_F := the transitions of F with W_(k+1) = W_k. WCT_F := |F| − T1_F. WCH_F(v) := the transitions of F changing W(v).
- Premises used:
  - [1E-N3] RESULTS R57's standing SPEC premise: S1 realises Odd's pointwise optimum, and at S4a σ_(k+1) is the pointwise optimum of the
    one-player arena H_k.
  - [S4b-OPT] the Odd mirror of [1E-N3] for S4b (S3's best response): τ_(k+1) is a pointwise-optimal Odd strategy, against the OLD σ_k
    (n5b reading A6), of the one-player Odd arena O(τ_k) := {τ_k(o)} ∪ Iτ_k(o), with Even fixed to σ_k.
    - This is the same engine on the dual game. Lead reading needed whether R57's premise already covers it; it is used ONLY in §2.
  - [R15a] RESULTS R15 (a), (d): Ξ_(k+1) ⊵ Ξ_k pointwise at every S4a step.
  - [XW], [W-MON] RESULTS R91 Lemmas XW and W-MON: Ξ_k ⊴ W_k pointwise, and W does not fall at an S4a step read with τ_k. On a W-run:
    W_(k+1) ⊵ W_k for every transition k → k + 1 of F.
  - [LEX] RESULTS R93 Fact LEX: CS(x), the coordinate sequence of a value (reward of the cycle node, then the n signed rank coordinates
    from the most relevant down, then the signed length), orders values lexicographically exactly as ⊴. Its length is n + 2.
  - [PLAY] P-N5-SRC §2 (proof of PLAY-CAUSE^S, RESULTS R97): along one play y_0 y_1 …, val(y_0) = Φ(y_0; val(y_1)) with Φ independent of
    the state. On a fixed cycle node c, Φ(y; (c, P, ℓ)) = (c, P ∪ {y if y is more relevant than c}, ℓ + 1).
- R97's source events appear only in §8 (DEAD (e)).

## 2. Lemma O-ARENA
- Statement. Let k → k + 1 be a transition of F. Then W_k = Ξ^O(σ_k), where Ξ^O(σ) is the valuation of σ against Odd's pointwise-
  optimal response inside O(τ) (Odd restricted to O(τ), Even to σ). O(τ) depends on τ only, so it is fixed on F.
- Proof.
  - If Iτ_k = ∅, then O(τ) = {τ} and the claim is the definition of W_k.
  - Otherwise S4b sets τ_(k+1) := a pointwise optimum of O(τ_k) against σ_k [S4b-OPT].
  - On F, τ_(k+1) = τ_k = τ, so τ attains the pointwise optimum, and val(σ_k, τ) = Ξ^O(σ_k). □
- Reading, not signed. On a W-run, W and Ξ are the values of ONE Even strategy in two nested games G_O ⊆ G that differ only by Odd edges.
  [XW] is the inequality between them.

## 3. Lemma SANDWICH and Corollary FROZEN
- SANDWICH. For sequences of one length in lexicographic order, x ⊴ y ⊴ z implies lcp(x, z) = min(lcp(x, y), lcp(y, z)). In
  particular lcp(x, z) ≤ lcp(y, z).
  - Proof.
    - Let i := lcp(x, z). On [0, i), x and z agree, so y agrees with both: a first difference of y at j < i would put y outside [x, z].
    - If i < length, then x_i < z_i and x_i ≤ y_i ≤ z_i, so y_i ≠ x_i or y_i ≠ z_i. Hence min(lcp(x, y), lcp(y, z)) = i. □
- FROZEN. On F = [p, q], with every lcp taken on CS ([LEX]):
  - BW_k := Σ_v lcp(CS W_k(v), CS W_q(v)) is non-decreasing on [p, q];
  - AF_k := Σ_v lcp(CS Ξ_k(v), CS W_q(v)) is non-decreasing on [p, q];
  - on any run of S4a steps, LS_k := Σ_v lcp(CS Ξ_k(v), CS Ξ_end(v)) is non-decreasing, where end is the last state of that run.
  - All three lie in [0, n(n + 2)].
- Proof.
  - For k ≤ k′ ≤ q, [W-MON] gives W_k ⊴ W_k′ ⊴ W_q; [R15a] and [XW] give Ξ_k ⊴ Ξ_k′ ⊴ W_k′ ⊴ W_q; [R15a] alone gives Ξ_k ⊴ Ξ_k′ ⊴ Ξ_end.
  - Apply SANDWICH per vertex and sum. □
- Remark (not signed). A_k := Σ_v lcp(CS Ξ_k(v), CS W_k(v)) (L-SI box 53c) is not monotone: its reference W_k moves. Freezing the
  reference at q is what makes BW and AF monotone.

## 4. Lemma BW-ACC
- Statement. Let M := n(n + 2) + 1 and N_F := #{transitions of F at which BW does not rise and A does not fall}. Then
  |F| ≤ (M + 1)·n(n + 2) + M·N_F.
  - Every W-constant transition is in N_F, so N_F = T1_F + T4_F, where T4_F counts the W-changing transitions with BW flat and A not
    falling.
  - Conversely N_F ≤ |F|, so |F|-POLY ⟺ N-POLY.
- Proof.
  - Let Φ_k := M·BW_k − A_k. Then Φ ∈ [−n(n + 2), M·n(n + 2)], since A ∈ [0, n(n + 2)].
  - At a BW-rise, ΔΦ ≥ M − n(n + 2) = 1 (BW rises by an integer ≥ 1; A falls by ≤ n(n + 2)).
  - At a BW-flat A-fall, ΔΦ ≥ 1. At a transition in N_F, ΔΦ ≥ −n(n + 2). (BW never falls, by FROZEN.)
  - Summing, (|F| − N_F) − n(n + 2)·N_F ≤ Φ_q − Φ_p ≤ (M + 1)·n(n + 2).
  - W-constant transitions: BW is flat, and A_k ≤ A_(k+1) by SANDWICH (Ξ_k ⊴ Ξ_(k+1) ⊴ W_k = W_(k+1)). □

## 5. Bits: BIT-ALT, FIRST-GOOD, Theorem RESET-RED
- Encoding β (on F).
  - The cycle coordinate of W(v) is constant on F (λ_W fixed).
  - For a value x = (c, P, ℓ) with c fixed, β(x) ∈ {0, 1}^(3n+1) consists of:
    - for each rank r from the top, the bit [r ∈ P] if r has even priority and [r ∉ P] if odd;
    - then, with sl := ℓ if c has odd priority and −ℓ if even, the threshold bits [sl ≥ j] for j = −n, …, n.
  - Fact BIT. For values with the same cycle node, x ◁ y ⟺ β(x) <_lex β(y). Proof: [LEX]. Each rank coordinate is two-valued and
    oriented so that 1 is better for Even. A threshold vector is lex-increasing in sl. Lengths satisfy 0 ≤ ℓ ≤ n. □
- Definitions. For a vertex v and bit b, GOOD_F(v, b) (BAD_F(v, b)) := the transitions of F flipping bit b of β(W(v)) 0 → 1 (1 → 0).
  TD_F := Σ_(v, b) BAD_F(v, b), the RESETS.
- Lemma BIT-ALT. GOOD_F(v, b) ≤ 1 + BAD_F(v, b). Proof: a 0/1 sequence alternates. □
- Lemma FIRST-GOOD. Every change of W(v) on F flips its first differing bit 0 → 1. Proof: [W-MON] and Fact BIT. □
- Theorem RESET-RED (an EQUIVALENCE). WCT_F ≤ Σ_v WCH_F(v) ≤ n(3n + 1) + TD_F, so |F| ≤ T1_F + n(3n + 1) + TD_F. Conversely
  TD_F ≤ (3n + 1)·n·WCT_F.
  - Proof.
    - A W-changing transition changes some W(v).
    - FIRST-GOOD gives WCH_F(v) ≤ Σ_b GOOD_F(v, b), and BIT-ALT gives ≤ (3n + 1) + Σ_b BAD_F(v, b).
    - For the converse, a change has ≤ 3n + 1 flips. □

## 6. COPY, RESET-ROOT, DESC-COPY
- Lemma COPY.
  - Let k → k + 1 be a transition of F and v ∉ C a vertex whose successor on both the (σ_k, τ)- and the (σ_(k+1), τ)-play is the same z.
    That holds for Odd v (z = τ(v)), and for Even v with σ_k(v) = σ_(k+1)(v) = z.
  - Then β(W_j(v)) = π_v(β(W_j(z))) for j = k, k + 1, where π_v keeps v's own rank bit fixed, copies every other rank bit, and shifts the
    threshold block by one place (the same direction for all j).
  - Hence every flip of W(v) at k is a flip of W(z) at k in the same direction, and the first-difference position map is strictly
    increasing.
  - C-vertices have the constant value (c, ∅, 0) on F.
  - Proof.
    - [PLAY]: W_j(v) = Φ(v; W_j(z)), and Φ(v; ·) on the fixed cycle node λ_W(v) adds v's bit (the same at both j) and 1 to ℓ.
    - sl then moves by +1 or −1, the sign fixed by the parity of λ_W(v), so [sl′ ≥ j] = [sl ≥ j ∓ 1].
    - Lengths stay in [0, n]. □
- Corollary RESET-ROOT. If W(v) has a reset at k, follow v's (σ_(k+1), τ)-play.
  - Its first vertex y that is Even and switched at k (σ_(k+1)(y) ≠ σ_k(y)) exists, and β(W(y)) has a reset at k.
  - So TD_F ≤ n·Σ_k Σ_(y switched at k) (resets of W(y) at k).
  - Proof.
    - If no vertex of v's new play switched, it is v's old play too, so W(v) did not change.
    - Along the unswitched prefix, apply COPY step by step. C-vertices never change, so the prefix does not pass one before y. □
- Corollary DESC-COPY. For v ∉ C, let q_1(v), q_2(v), … be the first-difference positions of its successive W-changes on F (position 0 =
  most significant). A DESCENT is q_(j+1) > q_j (strictly less significant).
  - If v has a descent at k, and v did not switch at any transition of [k′, k] (k′ := v's previous change), then its successor z has a
    descent at k.
  - Proof.
    - On [k′, k + 1], v's successor is z (Even v unswitched; Odd v follows τ).
    - Every change of z in (k′, k) would be copied to v (COPY), so z's changes in [k′, k] are exactly at k′ and k.
    - COPY's position map is strictly increasing. □

## 7. ASC-RUN and Theorem STAIR
- Lemma ASC-RUN. q_(j+1)(v) ≠ q_j(v), and between two descents the positions strictly decrease. So
  WCH_F(v) ≤ (3n + 1)(1 + DESC_F(v)).
  - Proof.
    - After change j, bit q_j is 1 (FIRST-GOOD).
    - A next change with the same first-difference position would flip it 0 → 1 again, with the earlier bits unchanged. Impossible.
    - So a non-descent has q_(j+1) < q_j. There are 3n + 1 positions. □
- Theorem STAIR (an EQUIVALENCE).
  - Let ψ_k(v) := the position of v's last W-change on F before state k (3n + 1 if none), and Ψ_k := Σ_v ψ_k(v) ∈ [0, n(3n + 1)].
  - Then WCT_F ≤ n(3n + 1) + (3n + 1)·DESC_F, with DESC_F := Σ_v DESC_F(v). Hence |F| ≤ T1_F + n(3n + 1) + (3n + 1)·DESC_F. (L-NEW box 111
    stated the weaker form with 3n + 2 for 3n + 1.)
  - Conversely DESC_F ≤ Σ_v WCH_F(v) ≤ n·WCT_F, so WRUN-POLY ⟺ (T1 + DESC)-POLY.
  - Proof.
    - At a W-changing transition, each changed vertex either ascends (ψ falls by ≥ 1, ASC-RUN) or descends (ψ rises by ≤ 3n).
    - A W-changing transition with no descent lowers Ψ by ≥ 1; the others contain a descent, so they number ≤ DESC_F.
    - The total rise of Ψ is ≤ 3n·DESC_F, and Ψ starts ≤ n(3n + 1) and stays ≥ 0. So the descent-free W-changing transitions number
      ≤ n(3n + 1) + 3n·DESC_F. Add the ≤ DESC_F others. □
- Corollary RESET-STAIR (not a new count). Resets that no later descent re-fixes cost nothing in |F|: they sit inside ascending runs.
  STAIR's counted set is the descents, the carries.

## 8. DEAD ends and DATA (not to sign; instances faithful: n5b (experiments/n5-second/n5b.py via si/root/n5bcmp.py) identical state by state, Oink 8fbf0a7 --zlk and --tl «solution verified» and equal to N5's regions, unless noted)
- (a) «BW strictly rises at every W-changing transition»: DEAD on red/xing/instances/x31_rx48 (sha1 34b44d5d…, start
  new/box107/inst/x31_rx48.start b3ba35d9… = n5x default).
  - W-run 36..50 has 13 consecutive T4 transitions. W moves at CS position 17, while lcp with W_end is 4.
  - Pin «box 107 FINPOT».
- (b) «a potential referenced to the W-ceiling (A, AF, BW, rank of Ξ among W-values) pays a W-constant interval»: DEAD on
  red/tie/instances/u23sw64_n32 (18b46837…, start c69511c1…), states 1-9.
  - W is constant, and Ξ has a different cycle node at all 32 vertices, so every such potential is flat 8 times. LS pays the interval.
- (c) «every σ-move raises Ξ or W»: DEAD on red/so/instances/tog6a_n32 (fd0e2c7e…; start new/box111/tog6a_n32.start = n5x default), k = 8.
  - Even vertex 13, its own Ξ-cycle node with value (13, 0, 0), switches 30 → 27 (improving by length), and no value changes.
  - Pin «box 107».
- (d) «h^W ≤ 2» (HDEPTH, box 107): DEAD on new/box109/out/hit_b6a_1 (ff1cd2f9…, start 89ae7c5b…; n 32, h^W = 3). Pin «box 109».
  - L-RED R159's hd_H gives h^W = H by design. That is why HIER-RED is not in this packet.
- (e) «descents happen at, or after, R97 source events»: DEAD on red/xich/instances/obs_K12_m24 (7df541fb…, start 23db47dd…).
  - The 12 descents are all at selector 247, one per round, and 0 are at source events.
  - desc.py DSRC_NOW 0, DSRC_SINCE 0.
- DATA (desc.py, resets.py, finpot.py; corpus = L-SI box 53's 1,132 games, 14,028 W-run transitions):
  - BW rises at 13,633 transitions.
  - Resets occur at 12,985 of 13,949 W-changing transitions, and RESET-ROOT holds 12,985 / 12,985.
  - Σ_v WCH 66,857 against DESC 14,755, max 3.14·n per game. VIOL 0 for every bound above.
  - hd_H40 (L-RED, be553fc9…) and sbq2_K8_m16 (L-SI box 54, 70f485cd…; faithfulness per their lanes) have 0 descents.
- Pins in experiments/new/check.sh: «box 107 FINPOT», «box 110 WIDTH», «box 111 STAIR».

## 9. ERRATUM (box 108, docs/new/N5-HDEPTH-box108.md §2, Remark)
- «A reset at a fixed vertex is impossible anyway (W-MON)» is false. [W-MON] is lexicographic, and when W(v) improves at a position,
  every lower bit may get worse.
- Nothing in this packet uses the sentence. Box 110 §0b records the erratum.

## 10. CONJECTURE (not to sign)
- DESC-LIN: DESC_F ≤ c·n for every W-run. By STAIR it would give |F| = T1_F + O(n²). Routed to L-RED successor 38 by the Lead.

## 11. RESULTS line (draft)
- R?? [refereed-only] N5 on EVERY game (SPEC S1-S5; premises RESULTS R57's 1E-N3 and its S4b mirror [S4b-OPT], R15 (a), (d), R91
  (Lemmas XW, W-MON), R93 (Fact LEX), P-N5-SRC [PLAY]; W-run F as in RESULTS R89, W_k under F's τ, T1_F its W-constant transitions):
  - (Lemma O-ARENA) W_k is σ_k's best-response value with Odd restricted to O(τ) = τ ∪ Iτ;
  - (SANDWICH, FROZEN) Σ_v lcp(CS W_k, CS W_q) and Σ_v lcp(CS Ξ_k, CS W_q) are non-decreasing on F, with range n(n + 2);
  - (BW-ACC) |F| ≤ (M + 1)n(n + 2) + M·N_F, M = n(n + 2) + 1;
  - (BIT-ALT, FIRST-GOOD, RESET-RED) |F| ≤ T1_F + n(3n + 1) + TD_F, TD_F the good-to-bad flips of W's oriented bits;
  - (COPY, RESET-ROOT, DESC-COPY) resets and descents are copied from switched vertices;
  - (ASC-RUN, Theorem STAIR) |F| ≤ T1_F + n(3n + 1) + (3n + 1)·DESC_F, DESC_F the descents of W's first-difference positions.
  - (2026-10-31) — REDUCTIONS and EQUIVALENCES (no count is bounded here; DESC-LIN is a CONJECTURE; HDEPTH is DEAD (hit_b6a_1); G-N5-TIME
    stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim).

## DONE / FINDINGS / NEEDS
- DONE: this packet (sha1 and line count in the message to the Lead); new/box111/tog6a_n32.start (n5x default start; tog6a faithful:
  n5b identical, Oink zlk / tl verified, regions equal).
- FINDINGS: packet frozen. Lemmas to sign: O-ARENA, SANDWICH, FROZEN, BW-ACC, BIT, BIT-ALT, FIRST-GOOD, RESET-RED, COPY, RESET-ROOT,
  DESC-COPY, ASC-RUN, STAIR. W-MON and XW are cited as landed (R91), not re-proved.
- NEEDS: Lead: decide whether [S4b-OPT] is covered by R57's premise (used only in O-ARENA); route the packet to REFEREE 21 and REFEREE-2 24.
