# N5-WRET (box 37): switch-target forms after R120, and Lemma W-RETURN (the first S4a-specific charge)
L-SI successor 30 (Opus 5.5), D15 / D18, Lead reading L40. Lead's message 2026-10-29 21:05Z (after L-RED R120, l-red fe734a22): "(1)
Restate the conjectures you keep at switch targets (RESET-LIN-T, CARRY-SEG-T) and re-measure them on the corpus and on L-RED's wobs
pins. (2) Your proposed S4a-specific per-phase lemma for FG(τ) … It must use the best reply to τ inside σ ∪ Iσ". Working note,
unrefereed, not a TARGET.md claim. G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Tools: experiments/si/odd/pivot.py (TARGET line, §1), experiments/si/odd/wret.py (§2-§4). L-RED's pins copied read-only to
  experiments/si/odd/inst/red/ (wobs_K8_m32, wobs_K16_m64, d_wobs_K8_m32, with .start; from l-red fe734a22). Outputs
  odd/out/target_corpus_{E,O}.txt, odd/out/wret_corpus_{n5,fg}.txt. Pinned in si/check.sh «box 37».

## 1. Switch-target forms (CONJECTURES; DATA)
- A TARGET of a λ-run R (λ^U-run on G^d) is a vertex c with ENT_R(v, c) > 0 for some v of the improving player (R86's notation:
  some strategy of that player switches into c inside R).
- Why targets suffice (READING of R86 (c)): Σ_v SW_R(v) = Σ_{(v, c)} ENT_R(v, c), and a term with ENT_R(v, c) = 0 needs no bound. So
  SW-RETURN is used only at targets, and R86 (d)'s P*_R may be read as the maximum over targets. (L-NEW 35's COMPOSE-FREEZE narrows the
  Odd sum further, to unprotected targets.)
- CONJECTURE RESET-LIN-T: #MAT_R(c) ≤ n for every target c of every λ-run (λ^U-run) R.
- CONJECTURE CARRY-SEG-T: at every such target, ≤ n − 1 carries between consecutive MATCHED changes.
- CONJECTURE PCH-QUAD-T: PCH_R(c) ≤ n² + n at every such target. RESET-LIN-T ∧ CARRY-SEG-T imply it (box 35 §2 arithmetic).
- DATA, L-RED's R120 pins (pivot.py TARGET; ALL = over every vertex, T = over targets):

  | pin | side | n | #MAT ALL | #MAT T | longest carry segment ALL / T | PCH ALL / T |
  | --- | --- | --- | --- | --- | --- | --- |
  | wobs_K8_m32 | Even | 231 | 248 | 8 | 2 / 1 | 263 / 15 |
  | wobs_K16_m64 | Even | 455 | 1008 | 16 | 2 / 1 | 1039 / 31 |
  | d_wobs_K8_m32 | Odd | 231 | 248 | 8 | 2 / 1 | 263 / 15 |

  - ALL reproduces R120's 248 and 1008 at the observer, with a third counter (pivot.py, on n5x.trace).
  - The observer is not a target. The busiest target has K MATCHED changes: 104 at K = 8, 200 at K = 16, both λ-run 0.
- DATA, corpus (odd/sbcg.lst, 719 games per side, S3 start, 0 timeouts): RESET-LIN-T, CARRY-SEG-T and PCH-QUAD-T have 0 failures on
  both sides.
  - Even side: max #MAT_T / n = 0.75 (x31_cu16, 12 at n 16); max segment_T / n = 0.46 (b5_os_n24); max PCH_T / n = 1.5
    (rise_thin51_n40, 60 at n 40).
  - Odd side: 0.125, 0.156 and 0.344 (all wide_h16, n 32).
  - #MAT_T < #MAT_ALL in 105 (Even) and 101 (Odd) games.
- Composition: G-N5-TIME ⇐ RESET-LIN-T ∧ CARRY-SEG-T, via R86 (d) at targets, R86 (e)'s per-vertex premise and box 35 §2's
  arithmetic (O(n⁶ m)). R120 does not touch this form.

## 2. Lemma W-RETURN (PROVED, lane; uses S4a)
- Setting. A GUIDED STRETCH Q is a run of consecutive states of an N5 run with τ constant on Q, where every transition t → t + 1 of Q is
  an S4a step: σ_{t+1} is Even's optimal strategy against τ in G restricted to H_t := σ_t ∪ Iσ_t (no S4c fallback).
  - FG(τ)'s non-stall steps are the same setting.
  - W_t := val(σ_t, τ) on the one-player game G_τ, compared in the VJ order ⊴.
- Notation. CN_t(v) := the cycle node of W_t(v). v is OFF-CYCLE at t if CN_t(v) ≠ v.
- Facts used. S4a enters through the optimality of σ_{t+1} in G_τ|H_t.
  - (OPT) At every vertex v that is off-cycle at t + 1: W_{t+1}(u) ⊴ W_{t+1}(σ_{t+1} v) for every edge (v, u) ∈ H_t (successor form, as
    Iσ is). Stated first as an ASSUMPTION; now Lemma OPT-OFF (§7, PROVED lane).
    - It is the VJ one-player optimality criterion. It FAILS at a vertex's own cycle node, which needs only some cycle through it; this
      is the REFEREE trap "VJ00 5.8 at own cycle nodes".
    - Instance: red/so/instances/tog6b_n32.pg, vertex 13 = CN(13). At t = 2 → 3 S4a moves 13 from 21 to 29, and W_3(29) ◁ W_3(21).
    - DATA: wret.py OPT_V counts (OPT) failures at off-cycle vertices over every edge of H_t (§4).
  - (W-MON, box 29 Lemma W-MON) W_{t+1} ⊵ W_t pointwise on every transition of Q. Its proof: σ_t ⊆ H_t, and σ_{t+1} is pointwise
    optimal in G_τ|H_t.
  - (W-SUCC, PROVED here from (OPT) and W-MON) W_t(σ_t v) is non-decreasing on any interval of Q on which v is off-cycle at every
    state after the first.
    - If v does not switch at t, this is W-MON.
    - If v switches at t, then W_{t+1}(σ_{t+1} v) ⊵ W_{t+1}(σ_t v), by (OPT) with (v, σ_t v) ∈ σ_t ⊆ H_t, and this is ⊵ W_t(σ_t v) by
      W-MON.
- Statement. Let v be Even. Suppose v leaves w at k → k + 1 (σ_k(v) = w ≠ σ_{k+1}(v)) and next re-enters w at j − 1 → j, all inside Q.
  Suppose v is off-cycle at every state of [k + 1, j], and W(w) does not change on [k + 1, j]. Then W_j(σ_j v) = W_{j−1}(σ_{j−1} v):
  v's SUCCESSOR valuation does not change at the re-entry (W-SILENT).
- Proof.
  - (v, w) ∈ σ_k ⊆ H_k. So, by (OPT) at k + 1: W_j(w) = W_{k+1}(w) ⊴ W_{k+1}(σ_{k+1} v).
  - By (W-SUCC) on [k + 1, j − 1]: W_{k+1}(σ_{k+1} v) ⊴ W_{j−1}(σ_{j−1} v).
  - By (W-MON): W_{j−1}(σ_{j−1} v) ⊴ W_j(σ_{j−1} v).
  - By (OPT) at j, with (v, σ_{j−1} v) ∈ H_{j−1}: W_j(σ_{j−1} v) ⊴ W_j(σ_j v) = W_j(w).
  - The chain starts and ends at W_j(w), so every term is equal. □
- The vertex form W_j(v) = W_{j−1}(v) is not claimed. wret.py counts its failures as VFORM_V.
- Corollary W-ENT (PROVED, lane; (OPT) = Lemma OPT-OFF, §7). On a guided stretch Q, for Even v and any w:
  ENT_Q(v, w) ≤ 1 + WCH_Q(w) + SIL_Q(v, w) + CYC_Q(v, w).
  - CYC_Q(v, w) counts re-entries whose interval contains a state where v is its own W-cycle node.
  - WCH_Q(w) counts the transitions of Q at which W(w) changes; SIL_Q(v, w) counts v's W-silent entries into w (successor
    valuation unchanged).
  - Proof: consecutive re-entries own disjoint intervals [k + 1, j]. Each re-entry is charged to a W-change of w inside its own
    interval, or else it is silent by W-RETURN.
  - Together with SW-RETURN (Ξ, rule-generic): ENT_Q(v, w) ≤ 1 + min(RISE_Q(w), WCH_Q(w) + SIL_Q(v, w) + CYC_Q(v, w)).
- Where S4a enters: only through σ_{t+1}'s optimality in G_τ|H_t ((OPT) and W-MON). Under switch-all, W-MON, (OPT) and the lemma all fail
  (§3).

## 3. Control: without S4a, W-RETURN fails (DATA)
- wret.py MODE=sa:τ: plain switch-all, with W read against the same frozen τ, on switchallexp.
  - N = 3: WMON_V 22, WRET_V 39 (of 377 re-entries), OPT_V 198.
  - N = 5: WMON_V 124, WRET_V 287 (of 2,745 re-entries).
  - The counts are the same for τ = first and τ = σ̄(σ_0).
- Under S4a, on the same games and on fc_3:
  - N5 runs: WMON_V 0 and WRET_V 0.
  - FG(first): also 0 and 0. On fc_3 there are 218 re-entries, every one W-paid, none silent.
- Mutation (--mut drops the "W(w) unchanged" premise): fires 62 on fc_3 (N5).
- So W-RETURN is the S4a-specific step BARRIER-SI asked for: the frozen guide pays every return to an edge with a W-rise of its target,
  and a switch-all counter re-enters w with W(w) unchanged.

## 4. Corpus (DATA; odd/sbcg.lst, 719 games, S3 start for N5, start "best" for FG(first); 0 timeouts)
| run | re-entries in guided stretches | W-paid | W-silent | own-cycle-node (CYC, excluded) | WMON_V | OPT_V | WRET_V | most W-changes of one vertex in one stretch | longest stretch |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N5 | 5,918 | 5,872 | 45 | 13 | 0 | 0 | 0 | 41 (topfix_n10, n 210); max / n 0.5 | 159 (runfam_K40, n 79) |
| FG(first) | 12,024 | 12,016 | 7 | 43 | 0 | 0 | 0 | 45 (fcobs_6, n 163); max / n 0.42 | 49 (block_bk32, n 36) |
- (OPT) at off-cycle vertices holds on every edge of every H_t (OPT_V 0); the vertex form never failed either (VFORM_V 0).
- W-silent re-entries are real but rare: N5 33 in u23sw64_n32, 6 in u1t_own6_n32, 1 in u2flat73_n32; FG 4 in u1t_cex_n32. So SIL is a genuine term, not 0.

## 5. What W-RETURN gives (implication, PROVED lane) and what is left
- On a guided stretch, every transition changes σ. If σ did not change while τ is constant, the state would repeat, which is a fixed
  point or an S4c fallback, so no such transition lies in Q. Hence:
  |Q| ≤ Σ_v SW_Q(v) ≤ Σ_{(v, w) ∈ E, v Even, ENT_Q(v, w) > 0} (1 + WCH_Q(w)) + Σ_v (SIL_Q(v) + CYC_Q(v)).
- Bounding WCH_Q(w).
  - Split Q at the changes of W(w)'s cycle node. There are ≤ n − 1 of them per vertex on a fallback-free stretch (box 29 Lemma CN-W).
  - On each piece, LEN-MONO's proof read with W and W-MON gives ≤ n·WPCH + n − 1 changes, where WPCH counts w's W path-set changes.
  - So WCH_Q(w) ≤ n·WPCH_Q(w) + n².
- Corollary (implication; (OPT) = Lemma OPT-OFF): |Q| ≤ m_E·(1 + n·WPCH*_Q + n²) + SIL_Q + CYC_Q, with WPCH*_Q the most W path-set changes of one target in Q.
  - So GUIDE-POLY, and the length of every guided stretch of N5, reduce to W path-set changes in the ONE-PLAYER game G_τ under the
    "optimum of σ ∪ Iσ" dynamics, plus silent entries.
  - In switch-all's counter-model those are exactly what explodes. Under S4a, W is the optimum value of a growing family of one-player
    subgames.
- Left open:
  - (i) WPCH* per guided stretch. This is box 31's R88 GP* / FW-R* territory: W-changes there are charged to adoptions of blocked
    edges.
  - (ii) SIL and CYC (re-entries while v is its own W-cycle node): SIL rare (§4: 45 of 5,918 N5 re-entries, 33 of them in one game), CYC 13; neither bounded.
  - (iii) the number of guided stretches, i.e. τ-changes and fallbacks; this half is not addressed.

## 6. Composition toward G-N5-TIME (one line each)
- §1: the usable conjectures are RESET-LIN-T ∧ CARRY-SEG-T (0 failures; R120's observer is not a target); with them G-N5-TIME follows
  (O(n⁶ m)).
- §2-§3: W-RETURN is a proved, S4a-specific replacement of SW-RETURN's Ξ-charge by a W-charge inside guided stretches; it is false for
  switch-all.
- §5: guided-stretch length ≤ m_E(1 + n·WPCH* + n²) + SIL + CYC ((OPT) = Lemma OPT-OFF): the per-phase half of G-N5-TIME reduces to W path-set changes in a
  one-player game.

## 7. Lemma OPT-OFF: (OPT) is a theorem (PROVED, lane; Lead 21:26Z ask (a))
- Premise: SPEC S1 (docs/new/N5-ssi-global.md l. 32) states that the VJ procedure's output minimises S1's order "at every vertex at once".
  S4a reads σ_new as that output on the DUAL of the arena H_t against τ (l. 15, 52).
- Order reversal (checked from S1 l. 27-31 and n5.dual, priorities + 1).
  - Ranks are unchanged and every parity flips.
  - So, for distinct cycle nodes, reward_d = −(reward ± 1) reverses the reward order, case by case (even/even, odd/odd, even/odd).
  - The signed weight is negated, and the length rule flips with c's parity. P-membership (rank above c) is unchanged.
  - Hence the dual key of a valuation is the reverse of its key in G, and the dual's pointwise minimum is G's pointwise maximum.
  - So σ_new is POINTWISE OPTIMAL for Even in A := G_τ|H_t: W(σ_new) ⊵ W(σ'') at every vertex, for every Even strategy σ'' inside H_t.
- Statement. Let σ' be pointwise optimal in a one-player arena A (Odd fixed). Let v be Even with CN(v) ≠ v, where c := CN(v) is the
  cycle node of W(v), and let (v, y) ∈ A. Then W(y) ⊴ W(σ' v).
- Proof. Let σ'' := σ' with v → y.
  - Since v ≠ c, W(v) = ext(v, W(σ' v)), and σ' v's play to c avoids v.
  - ext(v, ·) preserves and reflects ⊴ between valuations whose paths to their cycle nodes avoid v. It keeps the cycle node (so the
    reward). With the same cycle node it adds v to both P or to neither, and adds 1 to both lengths.
  - Case 1: v is not on y's play. σ''-play from v is v, then y's σ'-play, so W''(v) = ext(v, W(y)). Optimality gives
    W''(v) ⊴ W(v), and reflection gives W(y) ⊴ W(σ' v).
  - Case 2: v is on y's path to y's cycle node. Then y's play continues as v's, so W(y) = (c, D ⊔ P(σ' v), ℓ + L), where D is the set of
    vertices of the segment y … v above c, and L ≥ 1. σ'' closes the cycle C = v → y → … → v.
    - If D ≠ ∅ with an even top, that top is C's top (rank > c), so W''(v) has a better reward than W(v): impossible. So the top of D is
      odd, and W(y) ◁ W(σ' v).
    - If D = ∅ and c is even, then W(y) is longer, so W(y) ◁.
    - If D = ∅ and c is odd, C's top t has rank < c, so reward(t) > reward(c): impossible.
  - Case 3: v is on y's cycle after c. Then CN(y) = c, and P(σ' v) = ∅ (σ' v runs along the cycle to c, whose top is c). σ'' closes
    C = v → y → … → c → … → v.
    - If P(y) = ∅, C's top is c and W''(v) = ext(v, W(y)): as in Case 1.
    - Otherwise C's top is t = top of P(y), with rank > c. v itself is below c because it is on c's cycle. If t is even, W''(v) is
      better: impossible. So t is odd, and W(y) ◁ W(σ' v).
  - These cases are exhaustive: if v is on y's play, it lies either on y's path to y's cycle node or on y's cycle. □
- Consequences.
  - (OPT) holds, so Lemma W-RETURN and Corollary W-ENT are PROVED (lane) with no assumption beyond SPEC S1's stated optimality.
  - The own-cycle-node exclusion is necessary (tog6b_n32, vertex 13).
  - DATA agrees: OPT_V = 0 on 1,438 corpus runs. Under switch-all OPT_V = 198 on switchallexp_3, where σ is not an optimum of anything.

## 8. Using R88 GP* / FW-R* and L-NEW's GP*-RUN, STRETCH-RED, R*-RISE (Lead 21:26Z ask (b); READING + DATA)
- The setting is the same. A W-run (P-N5-FRAME §3.3) is a fallback-free piece of a τ-stretch with λ_W constant, and a guided stretch
  (§2) is a fallback-free piece of a τ-stretch. Inside W-runs:
  - GP*-RUN: at most (n − 1)(R*_T + 1) W-changing transitions, where R*_T counts transitions containing a late adoption of a blocked edge.
  - R*-RISE: R*_T ≤ Σ_z d_E(z)·RISE_F(z), i.e. Ξ-rises. That goes back to PCH, the Ξ side.
- What W-ENT adds: a W-side charge for every re-entry, so for late adoptions too:
  #late adoptions of (y, z) ≤ ENT_F(y, z) ≤ 1 + WCH_F(z) + SIL + CYC.
  - Plugged into FW-R* this is CIRCULAR: WCH_F(z) ≤ #W-changing transitions ≤ (n − 1)(R*_T + 1). Circular, like CARRY-SEG with MATCH-Φ.
  - It closes only with a per-VERTEX W bound. If WCH_F(z) ≤ B for every target z, then:
    - |F| ≤ m_E(1 + B) + SIL + CYC directly (§5);
    - R*_T ≤ m_E(1 + B) + SIL + CYC, and FW-R* adds nothing.
- DATA, per-vertex W-changes in one guided stretch (wret.py maxWR):
  - corpus ≤ 0.5n (N5) and ≤ 0.42n (FG);
  - runquad_K8_m30_n192: 16, in a 264-transition stretch;
  - wobs_K8_m32: 16, in 280;
  - hntop_n8 (red/seg/instances, n 168): 171, in a 291-transition stretch, with one vertex making 163 switches.
- DEAD: W-VLIN (WCH_Q(z) ≤ n per vertex per guided stretch). Kill: hntop_n8, 171 > 168. Obstruction: H_n's lane sweeps (box 34 §2
  pattern) are W-changes of the top gate vertices, quadratic in N.
- CONJECTURE W-VPOLY: WCH_Q(z) ≤ n² per vertex per guided stretch. (hntop_n8: 171 ≪ n² = 28,224; one point, no family fit.)
  - With W-ENT: |Q| ≤ m_E(1 + n²) + SIL + CYC per guided stretch.
  - By §5, W-VPOLY is equivalent up to factors n to a polynomial bound on W path-set changes of one target in the one-player game G_τ.
- Composition: per guided stretch, G-N5-TIME's per-stretch half ⇐ W-VPOLY + polynomial SIL, CYC. The stretch count (τ-changes,
  fallbacks) is not addressed; STRETCH-RED's fb_S bound covers the fallbacks inside one τ-stretch.

## DONE / FINDINGS / NEEDS
- DONE: pivot.py TARGET line; wret.py (modes n5, fg:τ, sa:τ control; --mut); R120 pins copied; corpus runs; check.sh «box 37»; this note.
- FINDINGS:
  1. CONJECTURES RESET-LIN-T, CARRY-SEG-T, PCH-QUAD-T: 0 failures on 1,438 corpus runs. On R120's pins the target maximum is K.
  2. PROVED (lane): Lemma W-RETURN and Corollary W-ENT, S4a-specific; (OPT) is Lemma OPT-OFF (§7), from SPEC S1's pointwise optimality.
     A first version without the off-cycle premise was wrong (tog6b_n32, vertex 13).
  3. DATA: the switch-all control violates W-MON and W-RETURN.
  4. Implication: guided-stretch length ≤ m_E(1 + n·WPCH* + n²) + SIL + CYC.
  5. §8: DEAD W-VLIN (hntop_n8: 171 W-changes of one vertex in one guided stretch, n 168); CONJECTURE W-VPOLY; W-ENT + FW-R* is circular.
- NEEDS: none from the owner.
