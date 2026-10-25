# R-N5-CLS: REFEREE report on packet P-N5-CLS (box 8: TRANSFER, OFFGATE, CN, NL, Theorem CLS1)
Referee: REFEREE (successor 6), Opus 5.5 (owner ruling D15, Lead reading L37). Packet P-N5-CLS: the Lead's message of 2026-10-25 02:40Z
(Lead's stamp). Object docs/si/P-N5-CLS-box8.md at pinned trunk 486107a, sha1 5bbfd872383d9b2c2d3caaf902b174d0aa54e4ae (checked:
`git show 486107a:docs/si/P-N5-CLS-box8.md | sha1sum`, 181 lines). Written 2026-10-25 02:44Z onward by date -u. Every verdict is
labelled (Opus 5.5, D15). Labels (D18/L40): PROVED (by whom) / CONJECTURE / OPEN. Independent of REFEREE-2: docs/referee-2/ not read for
this packet. Author: L-SI successor 3.
Dependencies read at trunk e1079b6b (merged into claude/referee): RESULTS R20 (b) FBL with docs/referee/R-N5-XA.md §3 (its proof, statewise);
R23 (f) GAP, (g) WM; R25 OFF / NOINF / FB step (2) (docs/si/P-N5-FB-box7.md §4-§5); R19 (a)/(b) Lemma G; R21 (a) XW; R15 (a)/(d).

## Verdicts
| statement | lane label | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 (C5), (C6), (C7) | PROVED (L-SI succ. 3) | SIGNED |
| §1 Fact R | PROVED | SIGNED |
| §1 Lemma CLU | PROVED (L-SI succ. 2, restated) | SIGNED |
| §2 Lemma TRANSFER (every game) | PROVED | SIGNED |
| §3 Lemma OFFGATE (𝒞^1O) | PROVED | SIGNED WITH GAP CLS-1 (wording: the M_k = ⊥ clause is vacuous inside a phase, and its reason is wrong) |
| §4 Lemma CN (every game, inside a phase) | PROVED | SIGNED WITH GAP CLS-2 (wording: y is an Even vertex; "gate level" is defined only for Even) |
| §5 Lemma NL (𝒞^1O) | PROVED | SIGNED |
| §6 Theorem CLS1 (𝒞^1O) | PROVED | SIGNED WITH GAP CLS-3 (citation: FBL is applied at a single fallback state as "a throttled stretch of length 1"; valid, because FBL's proof is statewise given τ unchanged at the fallback; closed) |
| §6 Corollary | PROVED | SIGNED WITH GAP CLS-4 (wording: "evicting fallback" is not defined in the packet) |
| §7 OG′ FALSE | FALSE | CONFIRMED (x31_re24, transition 1 → 2, own code; 17 more violations in random games) |
| §7 (H-EQ), per-level count, Θ per scope run | OPEN | not signed (not asked) |

The Lead's question (cls2 TOTAL "MF_up 1" next to "FBR_EQ 1"): this is NOT a fallback-level rise and is outside CLS1 on two counts. MF_up is
cls2's OG′ counter: MF = the max level of gates into F̄, not M_k. Its one hit is x31_re24 at transition 1 → 2, which is an S4a step, not a
fallback (MF_1 = −1, MF_2 = 22; M_1 = 23 ≥ 22, so OFFGATE holds). FBR_EQ 1 is a separate counter: one gate edge into R̄ at an in-scope
EQ fallback, of level ≤ −1 (cls2 reports no FBR_viol). My probe sees no rise of M at any in-scope fallback of any kind: named set
256 fallbacks (252 THR u* ≠ none, 4 EQ), library 534 (526 + 8 EQ). (Random games: 234 EQ in-scope fallbacks, but never two in one run, so vacuous.)

## 1. §1: elementary facts, Fact R, Lemma CLU (SIGNED)
- (C5) a ◁ b ⊴ c ⇒ lev(a, b) ≤ lev(a, c).
  - L = ⊥ is impossible (a = c). L = ∞ is trivial.
  - For finite L, lev(a, b) > L gives COARSE_L b ≠ COARSE_L a = COARSE_L c. (C1) gives COARSE_L c ⊴_L COARSE_L b ⊴_L COARSE_L c, so (C3)
    makes them equal: a contradiction. Correct.
- (C6) is the ultrametric inequality, via (C2). Correct.
- (C7): π disjoint from both path sets and both cycle nodes.
  - Equal cycle nodes: the same vertices of π (those above c) enter both path sets. The symmetric difference and its top are unchanged,
    and both lengths grow by |π|.
  - Different cycle nodes: lev = ∞ before and after, and the order is decided by the cycle nodes.
  Correct.
- Fact R: θ_k ⊴ θ_{k+1} (R15 (a)) and θ_{k+1} ⊴ w_{k+1} = w_k (XW at k+1, scope run). If θ changes, (C5) with θ_k ◁ θ_{k+1} ⊴ w_k gives
  lev(θ_k, θ_{k+1}) ≤ r_k, and (C6) gives r_{k+1} ≤ r_k. Correct. The order ⊥ < −1 < … is the packet's.
- State kinds under (h) are exhaustive (used in CLS1 (β)). If θ = w, Lemma G (b) gives Ξ = π ⊕ θ = π ⊕ w = W on R, and G (a) gives Ξ = W
  off R̄. So the state is EQ. If θ ≠ w, θ ◁ w (XW): THR, with r ≥ 0 or r = −1. DATA: KIND 0 failures.
- Lemma CLU: GAP (R23 (f)) gives Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ W_k(σ_k y). σ_k y ∈ R̄_k, since y ∈ R_k; σ_k y = o is allowed, with an empty route.
  Lemma G (b) rewrites the outer terms as π′ ⊕ θ_k and π′ ⊕ w_k. (C5) then (C7) give the bound r_k.
  - The (C7) disjointness: P(θ) is o and o's honest play after o, which lies in F under H1 (x0 = σ̄(o) ∈ F, as in R-N5-OE §2.1). P(w)
    is o and τ(o)'s play, in F under H2 (TC (i)). The common cycle node is λ_Ξ(o) ∈ F (TC (i); the packet cites the LOOP proof, also
    valid). π′ ⊆ R_k.
  - Correct. DATA: CLU 561 (named) / 1,253 (library) checks, 0 failures. C7use (lev(Ξ q, W q) = r, Ξ q ◁ W q on R under (h)): 15,647 /
    42,263, 0 failures.

## 2. Lemma TRANSFER (SIGNED; every game)
- u := σ_{k+1}(y). Ξ_k(u) ⊵ Ξ_k(σ_k y) by R15 (d) (u is σ_k y or a gate target), and Ξ_{k+1}(u) ⊵ Ξ_k(u) by R15 (a).
- The gate at k+1 has level > L. So COARSE_L(Ξ_{k+1} z) ▷_L COARSE_L(Ξ_{k+1} u), strictly ((C1), and (C2) for ≠).
- Chaining: COARSE_L(Ξ_k z) ▷_L COARSE_L(Ξ_k σ_k y). If Ξ_k(z) ⊴ Ξ_k(σ_k y), (C1) and (C3) would contradict this. So Ξ_k(z) ▷ Ξ_k(σ_k y)
  with distinct COARSE_L values, i.e. at a level > L (C2), and z ≠ σ_k(y).
- Correct. Only R15 is used, so it holds on every game. DATA: 99,815 (named) / 333,663 (library) (transition, gate, L) checks, 0 failures.

## 3. Lemma OFFGATE (SIGNED WITH GAP CLS-1)
- The main case is correct: OFF (R25, in-phase, tame or not) freezes COARSE_{M_k}(Ξ z) for z ∉ R̄_{k+1}. TRANSFER with L = M_k < ∞ turns a
  gate of level > M_k at k+1 into one at k, against the definition of M_k.
- CLS-1 (wording): the packet says "If M_k = ⊥, σ and Ξ are unchanged". M_k = ⊥ means there is no gate edge at k. Then S4a and S4c change
  nothing for Even, so the iteration changes τ, and the transition is not in a phase. The case is vacuous. Write "M_k ≥ −1 at every
  in-phase transition".
- DATA: OFFG 6,645 (named; equal to the packet's 6,645) / 18,368 (library) / 1,098 (random) gate checks, 0 failures.

## 4. Lemma CN (SIGNED WITH GAP CLS-2)
- λ_{k+1}(y) = y: y is the top of its H_{k+1}-cycle through z = σ_{k+1}(y), so P(Ξ_{k+1} z) = ∅ (Lemma 5.2).
- λ_k(z) = λ_{k+1}(z) = y in the phase, and Ξ_k(z) ⊴ Ξ_{k+1}(z). With the same cycle node, P(Ξ_k z), if non-empty, has an odd top.
- σ_k(y) lies on y's H_k-cycle, so P(Ξ_k σ_k y) = ∅. The gate gives P(Ξ_k z) ⊵ ∅.
- So P(Ξ_k z) = ∅, and the strict gate is length-only: level −1. Correct.
- CLS-2 (wording): "y switches to z" with "the gate level of (y, z)" presupposes an Even y (gates are Even's improving edges; R15 (d) makes
  every Even switch a gate). Say "Even y".
- DATA: CN 7 (named; equal to the packet's 7) / 19 (library) / 507 (random), 0 failures.

## 5. Lemma NL (SIGNED)
- (K*): Lemma G (b) and (C7) at j put Ξ_j(q) ◁ W_j(q) at level r_j > L, so the COARSE_L values are strictly ordered.
  - q ∉ R̄_{j+1} gives W_{j+1}(q) = Ξ_{j+1}(q) (G (a), no (h) needed). WM gives W_{j+1}(q) ⊵ W_j(q), since j → j+1 is not a fallback.
    This is the only place S4a is used.
  - Then (i) at q gives COARSE_L(Ξ_j q) ⊵_L COARSE_L(W_j q) ▷_L COARSE_L(Ξ_j q): a contradiction. Correct.
- (i): minimal counterexample by the H_{j+1}-distance to the cycle node.
  - v ∉ R̄_{j+1}, so its play avoids o: Odd vertices on it are forced, and v ≠ o.
  - v = c_v is excluded by (P3) at both ends (phase).
  - p_1 satisfies (i) by minimality, or p_1 = c_v.
  - If v's successor is unchanged, or switched along a gate of level ≤ L, (E) holds. Then (P2) at j and at j+1 (v is not its own cycle
    node at either, phase) and (C4) give (i) at v.
  - Otherwise q = p_1 is a gate target of level > L. (A_j) puts q outside F_j, and q ∉ R̄_{j+1}, q ≠ o, so q ∈ R_j ∖ R̄_{j+1} satisfies
    (i), against (K*).
  - Correct.
- (ii) from (i) + (K*). (iii): z ∈ F_{j+1} ⇒ z ∉ R̄_{j+1} ⊇ R_j (by (ii)), and z ≠ o, so z ∈ F_j. Then (i) and TRANSFER, against (A_j).
  Correct.
- The hypotheses are all used: (h) at j for Lemma G (b); r_j > L for (K*); (A_j) for (i). L = ⊥ is allowed. (A_j) then says there is no
  gate into F_j at all.
- DATA (every L with MF_j ≤ L < r_j, i.e. every L for which (A_j) holds): 9,818 (named) / 21,241 (library) / 19 (random) checks of
  (i)-(iii), 0 failures.
- x31_re24 (the OG′ instance): at transition 1 → 2, r_1 = −1 = MF_1, so no L satisfies NL's hypotheses. The R-collapse (21 → 1) there is
  outside NL, consistent with §7.

## 6. Theorem CLS1 and Corollary (SIGNED WITH GAPS CLS-3 closed, CLS-4 wording)
- (β) is correct. A fallback of S has (h) at its state, so it is THR (r ≥ 0 or r = −1) or EQ (r = ⊥) (§1, kinds exhaustive). Fact R
  then excludes an EQ or u* = none fallback before k1. So the induction hypothesis covers every earlier fallback, and L := M_{k0} is the
  running minimum.
  - L < ∞ by NOINF with FB-1.
  - L ≥ −1, since a fallback has a gate edge.
- Case r_{k1} ≤ L: by FBL (u* ≠ none), the switched edges are R → F leaves (≤ r_{k1} by CLU) or own-cycle-node switches (−1 by CN; the
  F → F switches of FBL's step 2 are of this kind). FB step (2) (M_{k1} is attained by a switched edge; each tail goes to its best
  target, and by (C5) the best target carries the max level) gives M_{k1} ≤ max(r_{k1}, −1) ≤ L. Correct.
- Case r_{k1} > L:
  - Fact R gives r_j ≥ r_{k1} > L on [k0, k1], with (h) at each state of S.
  - Base: (A_{k0+1}) by OFFGATE at k0 → k0+1.
  - Steps: every transition in (k0, k1) is in-phase and is not a fallback, so it is S4a (τ is constant). NL (iii) carries (A_j).
  - At k1, switched edges into F_{k1} are ≤ L by (A_{k1}). FBL leaves only own-cycle-node switches into R̄ (CN: −1).
  - So M_{k1} ≤ L. Correct.
- CLS-3 (citation, closed): FBL (R20 (b)) is stated for "a throttled S4c fallback state", a throttled stretch being a run with τ, joint
  λ-phase, θ, w constant, θ ◁ w and (h). The packet applies it at one state ("a throttled stretch of length 1"). I checked FBL's proof
  (R-N5-XA §3) for this use:
  - step 1 needs only that the fallback is Even's (τ unchanged at the transition, in phase) and that S4a returned σ_k;
  - step 2 (R → R none, F → F flat, F → R excluded for u* ≠ none) is statewise.
  So the length-1 reading is valid.
- CLS-4 (wording): the Corollary's "every one of its evicting fallbacks with u* ≠ none" uses "evicting", which the packet does not
  define. Every in-scope fallback with u* ≠ none is THR (it has (h) and θ ◁ w), so the clause holds under any definition. Drop the word,
  or cite its definition.
- DATA: 70 scope runs, 252 THR u* ≠ none + 4 EQ + 0 u* = none in-scope fallbacks (named; equal to the packet), max 33 fallbacks in one
  run. CLS1 checks: 252 named / 526 library, 0 failures. Fact R: 0 failures in 182 library scope runs. FBL switched-edge shape: 0 failures.
  Random games have at most 1 fallback per scope run (0 THR u* ≠ none), so they are VACUOUS for CLS1. The named and library instances
  carry the evidence.

## 7. §7 OG′: FALSE, CONFIRMED
- experiments/red/xing/instances/x31_re24.pg, sha1 49eaf50e960923f70ec6df2671561dd89e38882a, exactly one Odd choice vertex (asserted).
  - n5.py: 6 iterations, 0 fallbacks. check_sol2.py: "zielonka(oink zlk) OK strategies verified".
  - My trace: transition 1 → 2 is S4a, in-phase, (h), r = −1. MF_1 = −1, M_1 = 23, |R| 21 → 1. The gate (4, 8) at state 2 has level
    22 > MF_1.
  - So OG′ is FALSE and OFFGATE (bound M_1 = 23) holds there.
- Random games add 17 OG′ violations (rand seeds 8101, 8102), with 0 OFFGATE failures.

## 8. Data (DATA, not proof; docs/referee/scratch/cls_probe.py, sha1 0b18275a…, written from the packet's definitions, independent of
experiments/si/coarse/; own N5 trace asserted equal to n5.run; phase key (λ_Ξ, λ_U, τ); one Odd choice vertex asserted on every game)
| run | games | in-phase transitions | scope runs / in-scope fallbacks | failures |
| --- | --- | --- | --- | --- |
| named (experiments/si/coarse/named.txt 53 + instances/*.pg 12) | 65 | 2,057 | 70 / 256 (252 THR u* ≠ none, 4 EQ) | 0 (OG′ 1, expected) |
| library (every experiments/**/*.pg in 𝒞^1O, n ≤ 64) | 234 | 5,603 | 182 / 534 (526 THR u* ≠ none, 8 EQ) | 0 (OG′ 1 = x31_re24) |
| rand 4000, n 8-24, seed 8101 | 4,000 | 1,677 | 865 / 121 EQ | 0 (OG′ 9) |
| rand 1500, n 20-40, seed 8102 | 1,500 | 1,310 | 671 / 113 EQ | 0 (OG′ 8) |
- Checks with 0 failures in every run: C5, C6 (4.5 M triples), C7use, KIND, FACTR, CLU, TRANS, OFFG, CN, NL (i)-(iii), CLS1, FBL shape,
  no M rise at any in-scope fallback.
- I did not run the lane's scripts. The Lead re-ran run_cls.sh (byte-identical logs). My named-set counts equal the packet's §8 lines where
  they measure the same object (OFFGATE 6,645; CN 7; 70 scope runs; 252 / 4 / 0 fallback kinds).

## 9. Labels after this report (D18/L40)
- PROVED (L-SI successor 3; signed by REFEREE (Opus 5.5, D15), second referee pending):
  - on every game: (C5)-(C7), TRANSFER, and CN (inside a phase);
  - on 𝒞^1O: Fact R, Lemma CLU, OFFGATE, NL, Theorem CLS1 and its Corollary.
- FALSE: OG′ (x31_re24).
- OPEN: (H-EQ) (EQ / u* = none fallbacks of a scope run); ≤ n_E fallbacks per level; θ-changes per scope run; G-N5-TIME.
- Not a TARGET.md claim, not a step-4 pass. The TARGET.md diff is empty.

## Fixes-file lines (one per gap)
- CLS-1: §3 proof: replace "If M_k = ⊥, σ and Ξ are unchanged" with "M_k ≥ −1 at every in-phase transition (no gate ⇒ σ unchanged ⇒ τ
  changes, which leaves the phase)".
- CLS-2: §4 statement: "If λ_{k+1} = λ_k and an Even y with λ_k(y) = y switches …".
- CLS-3: §6: "FBL (R20 (b)) at the single state k1: its proof is statewise given that the fallback is Even's (τ unchanged in the phase)
  (R-N5-XA §3)".
- CLS-4: §6 Corollary: drop "evicting", or cite its definition (every in-scope fallback with u* ≠ none is THR).
