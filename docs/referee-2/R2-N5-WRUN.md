# R2-N5-WRUN: independent second-referee report on P-N5-WRUN (REFEREE-2 successor 23, Opus 5.5, D15)
Object: docs/new/P-N5-WRUN-box92.md @ l-new 7668bc9b (sha1 fae68aa004015c26e2f1f6d8803a6c45d7464dfa, 371 lines); line
docs/new/P-N5-WRUN-box92-line.txt (sha1 0faa5b80393bac1a6a3f6130926a4e18e3cf6129); candidate line revision L-1
docs/new/P-N5-WRUN-box92-line-L1.txt @ l-new 02a12a10 (sha1 d92521f7c7ffa28e0ebafeb1f8aeca3d3258b82f). All three re-hashed here (detached
worktree at 7668bc9b; `git show 02a12a10:…`): match the Lead's 16:59Z figures.
Independence: written before opening docs/referee/R-N5-WRUN.md. Revision L-1 applies REFEREE's first-report items; I read the line text
only, not REFEREE's report.
Landed sources re-read: RESULTS R15 (a), (b), (d); R86 (a) SW-RETURN and REFEREE's cell; R88 (BLOCKED, FW-R*); R89 (τ-stretch, W-run,
SUCC-MON, LATE-RISE, GP*-RUN, R*-RISE); R91 (XW, W-MON, W-SUCC, LATE-W); R93 (Fact LEX, NEW-BOUND, TIE_F); SPEC docs/new/N5-ssi-global.md
S1-S5 (unchanged at 7668bc9b). Other lanes' quoted texts opened at their SHAs: l-red 47000632 docs/red/R140-friedmann-port.md l. 41-46;
l-si a0d6f79b docs/si/N5-GATE-box51b.md §1, §10.3; my docs/referee-2/SUB-check.md (a11c2868).
Owner rulings applied: D1 «Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.»; D18 «Clearly
distinguish proven results from conjectures and open problems.»
Scope: REDUCTIONS and EQUIVALENCES inside W-runs of N5. No residual is bounded. W-runs are not whole runs. G-N5-TIME stays OPEN. Not M3, not a
step-4 pass, not a TARGET.md claim.

## 1. Verdict table
| § | item | verdict (Opus 5.5, D15) | gaps / notes |
| --- | --- | --- | --- |
| 1 | setting, premises, Fact STEP-SW | CHECKED; STEP-SW correct | 25 «» quotes of landed or lane text verbatim (the 6 others are the packet's own terms or the Lead's brief); N-1: Fact EXT as stated |
| 2 | other lanes' texts | quotes VERBATIM at their SHAs (ARENA-MAX l-red 47000632 l. 41-46; INTERVAL-SI / TIGHT-VALUE / FL-INT and RETURN-CHARGE / INT-XCH l-si a0d6f79b; [SUB] a11c2868) | ARENA-MAX, INTERVAL-SI, TIGHT-VALUE, RETURN-CHARGE not signed (not routed); FL-INT signed as part of E7 (elementary, §2.3 below) |
| 2.4 | [SUB] | quoted verbatim (my own SUB-check.md l. 5-11; REFEREE signed it independently, Lead 16:59Z) | so BIP-RED (§9) is unconditional once the Lead records the two signatures |
| 3.2 | Theorem XI-RUN (and the stretch form) | SIGNED | none |
| 3.3 | Corollary WRUN-EQ rows E1-E13 | SIGNED (each row, both directions as marked) | N-2: R3-POLY is not defined in the packet body (the line defines it); E10 vacuous (BIP-REL-1 DEAD, reproduced §4) |
| 4.2 | Lemma WAIT-CYCLE′, Corollaries DEAD-CYCLE, CHARGE | SIGNED | none |
| 4.3 | Lemma E0-BOUND | SIGNED | none |
| 4.4 | Theorem TRIPLE-RED | SIGNED | none |
| 5 | Lemma RET-ΞRISE, Theorem FREE-RED | SIGNED | none |
| 6 | Lemmas GAP-DEV, ΞCH-PCH, Theorem RSTAR-PCH | SIGNED | none |
| 7 | Lemmas LEX-SIGN, PREFIX-MON, Theorem LEVEL-RED | SIGNED | none |
| 8 | Definition BIP(ρ, τ), Lemma BIP-MON, Lemma NO-DEV (corrected) | SIGNED | N-3 (the correction note) |
| 9 | Theorem BIP-RED under [SUB] | SIGNED (implication; unconditional with [SUB] double-signed) | none |
| 10 | Lemma REL2-WRISE under (A1), (A2) | SIGNED | uses Fact EXT only where N-1's hypothesis holds |
| 11 | Corollary INT-XCH⁰ | SIGNED | none |
| 12-13 | CONJECTURES, DATA, DEAD, READING | not signed | DATA pins reproduced with my own engine (§4); BIP-REL-1 DEAD reproduced |
| line L-1 | d92521f7 | MATCHES §3-§11 in content | ONE REQUIRED fix (L-1: «strict release» unbound); precision L-2 to L-5 |

No gap. Nothing FALSE among the items to sign. One statement in the setting (Fact EXT) is FALSE as worded and TRUE with the hypothesis its uses
satisfy (N-1).

## 2. The items, as I checked them
### 2.1 Setting
- Fact STEP-SW. A transition of a W-run is not an S4c fallback (by definition) and keeps τ (one τ-stretch). R15 (d): every iteration changes σ
  or τ. So σ changes, by an S4a step whose σ_new lies in H_t (R57). ✓
- MON from R15 (a), (d) (Switch_I with I ⊆ Iσ, one edge per vertex), read on Ξ through R57. ✓
- **N-1 (Fact EXT, FALSE as worded).** «ext(y, ·) is strictly order-preserving and order-reflecting» fails when y lies in the path set of
  one argument. Instance: c with p′(c) < p′(y), x := (c, {y}, ℓ), x′ := (c, ∅, ℓ): x ≠ x′, but ext(y, x) = ext(y, x′) = (c, {y}, ℓ + 1). Its
  justification («either both arguments gain y or neither … the symmetric difference … unchanged») assumes y ∉ P(x) ∪ P(x′). My tool
  counts such pairs among Ξ-values actually met (control X_EXT_GLOBAL, hundreds of pairs, §4). TRUE with that hypothesis. The two uses
  satisfy it: §10 (i) applies it to W_{s+1}(h) and W_{s+1}(z), whose plays avoid y by (A1) and (A2); the quoted RETURN-CHARGE (§2.3, not
  signed) applies v ⊕ · to values of plays avoiding v. The second sentence («Ω(v) = ext(v, Ω(succ))» off own cycle node) is correct, and
  there y ∉ P(Ω(succ)) holds automatically (the successor's play reaches the cycle node before v). Fix: add «for values x, x′ with
  y ∉ P(x) ∪ P(x′)». No signed item changes.
### 2.2 Theorem XI-RUN (§3.2)
- |R| ≤ Σ_v SW_R(v) by STEP-SW (each transition switches an Even vertex; count one switch per transition). SW_R(v) = Σ_c ENT_R(v, c), with
  ENT_R(v, c) = 0 off Even edges. [R86] SW-RETURN on any stretch (REFEREE's cell, quoted verbatim): ENT_R(v, c) ≤ 1 + RISE_R(c). Summing
  over the m_E Even edges gives m_E + Σ_c d_E(c)·RISE_R(c); Σ_c d_E(c) = m_E gives the last form. ✓
### 2.3 Corollary WRUN-EQ (§3.3), row by row
- E1 ⇐ XI-RUN; ⇒ ΞCH_F(c) ≤ |F|. ✓ E2 ⇐ ΞCH-PCH; ⇒ PCH ≤ ΞCH. ✓ E3 ⇐ LEVEL-RED with k fixed ((2n + 1)^k is a polynomial), then E2; ⇒
  DEEP ≤ PCH. ✓ E4: |F| = WCH_F + FL_F (FL_F is the complement of WCH_F among F's transitions), FW-R* on F by GP*-RUN. ✓ E5: TRIPLE-RED;
  ⇒ REG, FREE ≤ RET ≤ |F|. ✓ E6: R93 NEW-BOUND; ⇒ WCH_F(e) ≤ |F|, TIE_F ≤ n_E·|F|. ✓ (N-2: «R3-POLY» is used in E6, E13 and §12 but defined
  only in the line, as (max_e WCH_F(e))-POLY; with that definition E6 and E13 check.)
- E7 with FL-INT. FL-INT is elementary as the row says: the W-constant intervals of F partition its states, the transitions inside them
  are exactly the FL transitions, and there are WCH_F + 1 of them. With E4: |F| ≤ (n − 1)(R*_F + 1) + (WCH_F + 1)·max_I |I| and
  WCH_F ≤ (n − 1)(R*_F + 1). ✓ So I sign FL-INT as used here (not INTERVAL-SI or TIGHT-VALUE).
- E8 ⇐ BIP-RED under [SUB]; ⇒ SB_F, R°_Φ, FL_F ≤ |F|. ✓ E9 ✓. E10 ✓ as an implication (R°_Φ ≤ the number of strict releases ≤ m_E under
  BIP-REL-1), but BIP-REL-1 is DEAD (L-RED R143; reproduced by my engine, §4), so E10 is vacuous. E11 ⇐ INT-XCH⁰. ✓ E12 = NO-DEV. ✓ E13 ✓.
- The «Reading of the table» sentence is a correct summary of E1-E8 (with E8 under [SUB]).
### 2.4 WAIT-CYCLE′, DEAD-CYCLE, CHARGE (§4.2)
- Claim A, Case 1 (X ∉ Z*): the play from σ_t1(X) never returns to X (X is on the tail), and no vertex of π is on it (from such a vertex
  the play would both reach X along π and continue along X's play, which avoids X). So the play from g is π, X, then X's play, and
  Ξ_t1(g) = (c*, P′ ∪ A, ℓ′ + 1 + |π|) with A disjoint from P′. A ≠ ∅: its top m decides; the block forces Ω(m) odd; z = m because the top
  of π ∪ {X} is above c* and so lies in A; rew(m) = −p′(m) < rew(c*) in both parities of c*. A = ∅: c* odd would make the longer value
  better for Even, against the block; so c* is even, c* ∉ C (c* is on X's play, C is not), and rew(z) ≤ p′(z) < p′(c*). ✓
- Case 2 (X ∈ Z*, X ≠ c*): π avoids Z* by the definition; the path set of σ_t1(X)'s value is ∅ (c* is the top of Z*), and X ∈ Z* is below
  c*, so A is the vertices of π above c*. ✓ Case 3 (X = c*, REG): REG with c* = X means some vertex of π is above X, so A ≠ ∅; its top is
  odd, else (X, g) would be improving. ✓
- The final step: under ρ′ (σ̄_t1 on the Odd vertices of π, σ̄_t elsewhere) the (σ_t, ρ′)-play from X follows C forever, because the
  Even vertices of π use Pat = σ_t1 and its Odd vertices use σ̄_t1, so each takes the next vertex of π, and X takes g. Optimality of σ̄_t
  (SPEC S1 / R57) gives Ξ_t(X) ⊴ val(σ_t, ρ′)(X), hence rew(λ(Ξ_t(X))) ≤ rew(z) < rew(c*), so Ξ_t(X) ◁ Ξ_t1(X): against MON. MON holds on
  the whole run, as the statement needs. ✓ DEAD-CYCLE: the same last step. ✓ CHARGE: at t2, σ_t2(X) = g, so the pattern must fail. ✓
### 2.5 E0-BOUND, TRIPLE-RED (§4.3-§4.4)
- At an E0 block the play from g is π then X, X is its own Ξ-cycle node, and π is below X: Ξ_t1(g) ∈ K = {(X, ∅, ℓ)}. At t2 − 1 the edge is
  improving (STEP-SW); SUCC-MON and the block give Ξ_{t2−1}(g) ▷ Ξ_{t1}(g). The windows are disjoint (t1^{i+1} > s^{i+1} ≥ t2^i). K is an interval
  of the order (equal rew, so cycle node X; equal path-set coordinates, so ∅). So Ξ_{t1^1}(g) ◁ … ◁ Ξ_{t1^last}(g) is a chain of `last`
  distinct elements of K, and last ≤ n. ✓
- TRIPLE-RED: one switch per transition; first adoptions ≤ m_E; each return in exactly one class; E0 ≤ n per edge. ✓
### 2.6 RET-ΞRISE, FREE-RED (§5)
- The chain Ξ_k(g) ▷ Ξ_k(σ_k X) ⊵ Ξ_{s+1}(h) ⊵ Ξ_s(h) ▷ Ξ_s(g) uses STEP-SW (h ∈ Iσ_s(X)), SUCC-MON over [s + 1, k], MON, and S2. The windows [s, k − 1] of successive returns of one edge are disjoint. ✓
  The DEDUPE remark (RETURN-CHARGE is the special case) is correct. FREE-RED ✓.
### 2.7 GAP-DEV, ΞCH-PCH, RSTAR-PCH (§6)
- GAP-DEV: BLOCKED, XW, not improving: W_q(z) ▷ W_q(σ_q y) ⊵ Ξ_q(σ_q y) ⊵ Ξ_q(z). If σ̄_q = τ on the Odd vertices of z's (σ_q, σ̄_q)-play,
  the two plays coincide and Ξ_q(z) = W_q(z). ✓
- ΞCH-PCH: λ(Ξ(z)) changes ≤ n − 1 times per run (rew strictly rises, by MON and LEX). Blocks with (λ, P) constant number ≤ n + PCH, and
  ℓ moves monotonically in [0, n − 1] inside each. Arithmetic: (n − 1) + PCH + (n + PCH)(n − 1) = n² − 1 + n·PCH ≤ n(n + 1 + PCH). ✓
- RSTAR-PCH: R*-RISE per Even edge, then ΞCH-PCH. ✓
### 2.8 LEX-SIGN, PREFIX-MON, LEVEL-RED (§7)
- PREFIX-MON: with equal cycle node, MON gives P ⊴ P′ in the S1 path-set order, i.e. lexicographic on (s_{n−1}, …, s_0) (LEX-SIGN). For P ≠ P′
  with top differing rank r and d common terms above r: d ≥ k leaves pre_k unchanged; d < k decides at term d + 1, in the three cases
  (0, +1), (−1, +1), (−1, 0), each strictly upward under the stated term order (I checked the six comparisons, including (r, −) < (r″, −) for
  r″ < r and (r, −) < NONE < (r″, +)). Values ≤ (2n + 1)^k. ✓
- LEVEL-RED: ≤ n blocks with λ(Ξ(v)) constant; the PCH-changes of depth < k strictly raise pre_k in their block. ✓
### 2.9 BIP, BIP-MON, NO-DEV (§8)
- On a frozen stretch, every transition starting in Φ is a BIP(ρ, τ) step: Ξ_t = val(σ_t, ρ), Iσ_t = Iρ_t, step = S4a's optimum (R57). ✓
- BIP-MON: in G_ρ Odd has one strategy, so val(σ, ρ) is VJ00's Ωσ there and R15 (a) applies to the switched subset of Iρ_t; and σ_t is a
  strategy of the arena, so the arena optimum against τ is ⊵ val(σ_t, τ). ✓
- NO-DEV (corrected): R*_F = 0 by GAP-DEV; WCH_F ≤ n − 1 by FW-R*; on an FL transition W, hence Ξ, and Ωτ are unchanged, so R15 (d) bounds
  runs of them by 4n(n − 1); ≤ n such runs. ✓ N-3: the CORRECTION paragraph is accurate: box 88's FL_F = 0 used a strict improvement that
  can fail at own cycle nodes. Since the FIXD review there is a sharper fact for the record, not needed here: at a Ξ-changing transition
  some switched vertex strictly rises (REFEREE's SW-KEEP, signed by me in R2-N5-FIXD-C.md C.4). At a Ξ-unchanged transition (the case
  NO-DEV must count) all switched vertices keep Ξ and are their own cycle nodes, so the corrected bound is the right form.
### 2.10 BIP-RED (§9), REL2-WRISE (§10), INT-XCH⁰ (§11)
- BIP-RED: the transitions not changing σ̄ lie in single frozen stretches; [SUB] with F′ = Φ, R*_T(Φ) = R°_Φ (the definitions coincide
  word for word); SB_F + 1 stretches. ✓
- REL2-WRISE: (i) π_s ∈ H_s; ARENA-MAX (= R57 read pointwise); (A2) makes val(π_s, τ)(z) = W_{s+1}(z) and y a tail vertex of its
  (π_s, τ)-play; (A1) gives W_{s+1}(y) = ext(y, W_{s+1}(h)); both arguments avoid y, so EXT reflects (N-1's hypothesis holds). (ii) W-SUCC
  on [s + 1, q2] (a W-run lies in one piece; (A1)). (iii) BLOCKED, not improving. ✓ The line's parenthesis «a special case of RESULTS R91
  Lemma LATE-W» is correct: (y, z) cannot be blocked at s + 1 (by (i), W_{s+1}(h) ⊵ W_{s+1}(z)), so q2 ≥ s + 2 is a «later state» in
  LATE-W's sense, under LATE-W's hypothesis (A1).
- INT-XCH⁰: XI-RUN with R = I. ✓

## 3. The proposed line, revision L-1 (d92521f7; verdicts on L-1 as the candidate)
Token diff against 0faa5b80 (difflib on whitespace tokens): header «revision L-1»; LATE-W added to R91's premises; the self-routed block
spelled out (g ≠ σ_t(X), route pairwise distinct, cycle avoidance); «for every k ≥ 1» for DEEP; [P-INT]'s polynomial moved in front and
«of every W-run»; PREFIX-MON's term order written out; the LATE-W parenthesis on REL2-WRISE; «one-way» → «proved in one direction only»;
BIP-REL-1 moved from «open» to «DEAD (L-RED R143, rel2_R2_n82, l-red 717f407a)». Each change is correct against the packet.
Strict symbol test, by hand, clause by clause:
- **L-1 (REQUIRED).** REL2-WRISE: «if (y, z) has a strict release in a frozen stretch …»: «strict release» is not bound in the line. The
  line defines R°_Φ («the transitions of Φ adopting an edge blocked at an earlier state of Φ») but not the term. Fix: «if (y, z) is adopted
  at a transition of a frozen stretch Φ at which it had been blocked at an earlier state of Φ (a strict release), y leaves z at s and
  (y, z) is blocked again at q2 > s in Φ, then …». Alternatively drop that hypothesis: the proof never uses the release.
- L-2 (precision). τ is unbound in two clauses: GAP-DEV «σ̄_q(o) ≠ τ(o)» (read τ_q) and BIP-MON «val(σ_t, τ)» (the W-run's τ). Elsewhere
  the line writes τ_t.
- L-3 (precision). «[P-INT] := for a polynomial p, every W-constant interval …» should read «there is a polynomial p such that every …»
  (as in the packet's Q-POLY).
- L-4 (precision). RSTAR-PCH «Σ_{(y, z)}»: «over Even edges (y, z)».
- L-5 (precision). «REG self-routed block» relies on «else an E0 one»; a REG block could be said explicitly to be one that is not E0.
- Every other symbol is bound: the run, states, n, n_E, m_E, d_E(c), switched / enters / leaves, Ξ_t, σ̄_t, values (c, P, ℓ), W_t, val, λ_W,
  the order, Iσ_t, H_t, τ-stretch, W-run F = [a, b], |F|, BLOCKED, late adoption, R*_F, ENT_R, SW_R, RISE_R, |R|, ΞCH_F, WCH_F(c), WCH_F, FL_F,
  TIE_F, PCH_F, P*_F, Q-POLY and every named POLY, return, RET_F, REG_F, E0_F, FREE_F, self-routed block, route, E0, depth, DEEP_{k,F}, frozen
  stretch, SB_F, R°_Φ, R°, [SUB], R*_T(F′), W-constant interval, XCH_I, (A1), (A2), s, q2, h and h2 (h2 only in the packet), k.
- Content: each clause states the packet's item (§3-§11) and nothing more. The ⇔ chain is exactly E1-E8, with E8 under [SUB]; the one-way list
  is E9 and E13. E10-E12 are not in the line (E12 is NO-DEV's clause). The honest-limits suffix is correct.
- TARGET.md diff: no claim about M4; n is TARGET.md's n; games are TARGET.md §1 games, read through SPEC S1. «W-runs are not whole runs»
  is stated. ✓
- [SUB] in the line is the [SUB] I checked (a11c2868), with R*_T(F′) defined as there.
- Line 0faa5b80 (for the record): the same content as L-1 without REFEREE's items; L-1 is the better candidate.

## 4. DATA: re-run with my own engine
Tool docs/referee-2/R2-N5-WRUN/wrun_check.py, on my R2-N5-LATEP state construction (my N5 loop; W-runs as in R89), with my own block, return,
prefix and frozen-stretch code from the packet text (the lane's box84-box92 scripts NOT imported). Start files: unlisted vertices take the
best-reward start; forced vertices take their only edge (the comp54_n80 repair of R2-N5-FIXD-C.md C.2). Checks STEP, SWR, XIR (and INT-XCH⁰),
RETX, E0B, TRI, WAIT (sampled REG blocks, every later state of the run), GDEV, PCH, RST, PRE (k = 1, 2, 3), LEV, NODEV, BIPR, SUBF, plus the
landed premises XIPLAY, XW, XIMON. Logs in R2-N5-WRUN/logs/.
- Corpus (the lane's: box59/sbcg.lst 719 runs; alt_all 94 with start files, including comp54_n80 repaired, plus 319 without): 1132 runs,
  14,028 W-run transitions: **0 violations of every check**. Returns REG 1,005 / E0 0 / FREE 5,260: exactly the packet's §13 figures.
  WAIT-CYCLE′: 286,472 sampled REG blocks, each checked against every later state of its run: 0 violations. GAP-DEV: 192,083 blocked
  (edge, state) records, 0 violations (the packet's 116,086 counts differently; I did not reconcile the convention). PREFIX-MON: 0 at
  k = 1, 2, 3, over 37,462 / 29,778 / 24,172 changes of depth ≥ k (controls: the deep changes exist). NO-DEV applied to 1,551 W-runs (Ξ = W
  throughout; longest 58, topfix_n10). Max XI-RUN ratio 0.272 (thetaA_n6 + start; packet 0.273, rounding). My W-run count 8,949 includes
  W-runs without transitions (the packet's 1,692 does not, I assume; not reconciled).
- Pins: pftheta34_n32 (sha1 b291d7bb…, best-reward start): W-run F[5, 39], |F| 34, max ΞCH 34, bound 1010 (packet: 34 / 34 / 1010) ✓.
  gate_K64_n581 + .start (sha1 a93c7c8b…): max |F| 71, max ΞCH 63, max R*_F 64 (packet: R*_F 64, ΞCH_F 63, |F| 71) ✓.
  fx_K8_m32 + .start (sha1 e995709e…): F[0, 280], |F| 280, max ΞCH 137, bound 2005 (packet 280 / 137 / 2005) ✓. latew_K16_m32 + .start
  (sha1 6d34c161…): F[0, 560], |F| 560, bound 4389 (packet 560 / 4389) ✓.
- BIP-REL-1 DEAD reproduced: experiments/red/rel2/instances/rel2_R2_n82.pg + .start at l-red 717f407a (sha1 064a8309…, start 2988324f…):
  one Even edge has 2 strict releases in one frozen stretch; all other checks 0 on that run.
- Control X_EXT_GLOBAL > 0 (N-1): pairs of Ξ-values met at a state whose ext(y, ·) images coincide.

## DONE / FINDINGS / NEEDS (this report)
- DONE: this report; wrun_check.py; logs.
- FINDINGS: (1) every item to sign (§3-§11, FL-INT inside E7) SIGNED, no gap, nothing FALSE. (2) [SUB] quoted verbatim. (3) Line L-1:
  one REQUIRED fix (L-1 «strict release» unbound), precision L-2..L-5. (4) N-1: Fact EXT is false as worded (instance x = (c, {y}, ℓ),
  x′ = (c, ∅, ℓ)), true with y ∉ P(x) ∪ P(x′), which all uses satisfy. (5) N-2: R3-POLY undefined in the packet body. (6) DATA pins
  reproduced, BIP-REL-1 kill reproduced.
- NEEDS: Lead: route L-1 (and N-1, N-2) to L-NEW 39; §C on your word.
