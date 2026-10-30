# P-N5-GAP (packet, box 69): the gap set {Ξ ≠ W} at in-phase fallbacks, W-paid re-openings and late adoptions; FB-LIN as a reduction
L-NEW successor 35 (Opus 5.5), D14 / D18, Lead reading L40. Lead 2026-10-30 00:52Z: «FREEZE packet P-N5-GAP for the two referees. Content:
LATE-W and LATE-PIECE (box 66), GAP-MON (box 67), SW-IN, the Z-flat characterisation, REOPEN-W and REOPEN-CHARGE (box 68). Add the
composition, written as a REDUCTION». FROZEN 2026-10-30 (this commit; sha1 reported to the Lead). Sources: docs/new/N5-LATE-box66.md §2, N5-FBENERGY-box67.md §1-§2, N5-ZFLAT-box68.md §1-§4 (working
notes; THIS packet governs where they differ). Status: REDUCTION only. FB-LIN and G-N5-TIME stay OPEN. Not a TARGET.md claim.
Quote base: l-new da3fa7fa (= trunk merge; SPEC docs/new/N5-ssi-global.md lines 28-57 unchanged since 2a435f8f4).
No file of L-SI's box 40 / 42 (P-N5-CUT, LATE-SPLIT, REP-LIN) is used as a proof. L-SI's box 37 lemmas OPT-OFF and W-SUCC are NOT cited:
both are re-proved here (§2.4, §2.5).

## 0. What to sign
| § | item | label |
| --- | --- | --- |
| 2.1 | Lemma XW (carried; also RESULTS R21 (a), stated there in a 𝒞^1O setting) | PROVED (to sign) |
| 2.2 | Lemma W-MON (carried; RESULTS R88's object §2) | PROVED (to sign) |
| 2.3 | Lemma FB-W (carried from box 21 §2.5 Lemma W, not landed) | PROVED (to sign) |
| 2.4 | Lemma OPT-OFF (one-player optimality at an off-cycle vertex) | PROVED (to sign) |
| 2.5 | Lemma W-SUCC | PROVED (to sign) |
| 3.1 | Lemma LATE-W | PROVED (to sign) |
| 3.2 | Corollary LATE-PIECE | PROVED (to sign) |
| 4.1 | Lemma GAP-MON | PROVED (to sign) |
| 4.2 | Lemma SW-IN | PROVED (to sign) |
| 4.3 | Lemma Z-FLAT (characterisation) | PROVED (to sign) |
| 4.4 | Lemma REOPEN-W and Corollary REOPEN-CHARGE | PROVED (to sign) |
| 5 | Theorem GAP-RED (the composition; a REDUCTION of FB-LIN) | PROVED (to sign) |
| 6 | DEAD energies (lend9_n8), DATA, READING | NOT to sign |

## 1. Setting, premises, definitions
- N5 = SPEC S1-S5 (FIX 1-4 as in RESULTS); any parity game G = (V, E, Ω, owner), n = |V|. A run is the sequence of states (σ_t, τ_t); a
  TRANSITION is t → t + 1.
- [S1-val] [Q SPEC:28-29] «valuation of v under (σ, σ̄): (c, P, ℓ), c = the most relevant (max p') vertex of the cycle the play from v ends
  in, P = set of vertices on the play before reaching c with p' > p'(c), ℓ = number of steps to reach c.» Applied to any pair of positional
  strategies, one per player.
- [S1-ord] [Q SPEC:30-31] «order (better for Even): compare reward of c (p'(c) if even, −p'(c) if odd); then P by the signed weight
  Σ_{u∈P} (+2^rank(u) if Ω(u) even else −2^rank(u)); then ℓ: if c is odd, longer is better for Even; if c even, shorter is better.»
  ⊴ / ◁ (strict), ⊵ / ▷ the reverse. Distinct triples are distinct in the order (RESULTS R84 (a) Fact DELTA, as in R88 / R89).
- [S1-Xi] [Q SPEC:32] «Ξσ = valuation of every vertex under σ and Odd's OPTIMAL counterstrategy σ̄ (minimising this order at every vertex at
  once).» Ξ_t := Ξ_{σ_t}, σ̄_t, λ_Ξ := Ξ's cycle-node map.
- [S2] [Q SPEC:47] «Improving edges: Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than Ξσ(σ(v))}; Iτ the same on G^d for τ.»
- [S4a] [Q SPEC:51-53] «a. If Iσ ≠ ∅: A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v. Arena H: Even v keeps only edges to A(v); Odd v keeps only
  the edge to τ(v). σ_new = Odd's optimal counterstrategy (S1 procedure) in the dual of H to the dual-Even strategy τ, read as an Even
  strategy of G. (Even's one-player optimum against τ among "keep or take an improving edge".) Else σ_new = σ.»
- [S4c] [Q SPEC:56-57] «c. FALLBACK, if σ_new = σ and τ_new = τ: if Iσ ≠ ∅, for every Even v with an improving edge set σ_new(v) = the w
  with (v, w) ∈ Iσ maximising (Ξσ(w), w) (best valuation, ties: larger index); otherwise do the same for Odd on Iτ with G^d's valuations.»
- [R15] RESULTS R15 (a) «Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}»; (d) «N5: every
  iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and changes at least one of
  them». Hence Ξ_{t+1} ⊵ Ξ_t pointwise at every transition (if σ_{t+1} = σ_t, Ξ_{t+1} = Ξ_t).
- [F1] RESULTS R17 (a): «the optimum of a one-player game dominates every strategy of that game pointwise».
- [V1], [V2], [⊕] (R17's object docs/new/N5-phase-bound-box10.md l. 13-14, 20-22, as quoted in R88's object §1): «Prefix: x ⊕ (c, P, ℓ) :=
  (c, P ∪ {x if x more relevant than c}, ℓ + 1); this is the value of a play that steps from x to a vertex of value (c, P, ℓ) whose path to
  c avoids x.» «(V1) if x is not its own cycle node then Ω_ρ(x) = x ⊕ Ω_ρ(ρ(x)) and the ρ-path from ρ(x) to λ(x) avoids x. (V2) PREFIX
  MONOTONICITY: if a ⪯ b are values whose paths both avoid x (or whose cycle nodes differ), then x ⊕ a ⪯ x ⊕ b, and strictly if a ≺ b.»
  These are facts about the play of one fixed pair of positional strategies, so they apply to Ξ (pair σ, σ̄) and to W (pair σ, τ).
- Definitions.
  - W_t := the [S1-val] valuation of the (σ_t, τ_t)-plays; G_τ := G with Odd fixed to τ; for a W-value, "v is its own W-cycle node at t"
    means the cycle node of W_t(v) is v. Same for Ξ.
  - PHASE: a maximal run of consecutive states with (λ_Ξ, τ) constant (RESULTS R38 (a)). A transition is IN-PHASE if both its states are
    in one phase. An in-phase transition has τ_{t+1} = τ_t, hence changes σ (R15 (d)), hence is either an S4a step (S4a moved σ) or an
    Even S4c fallback (S4c's Odd branch changes τ).
  - τ-FIXED EVEN FALLBACK: a transition that is an S4c fallback with Iσ_k ≠ ∅ (S4c's Even branch). Then τ_{k+1} = τ_k. Every in-phase
    fallback is one.
  - PIECE: a maximal run of consecutive states with τ constant, all of whose transitions are S4a steps. H_t := σ_t ∪ Iσ_t, S4a's arena
    for Even at t, a one-player game (Odd follows τ_t).
  - BLOCKED at t (RESULTS R88): an Even edge (v, c), c ≠ σ_t(v), with W_t(c) ▷ W_t(σ_t v) and (v, c) ∉ Iσ_t.
  - GAP SET: Z_t := {v ∈ V : Ξ_t(v) ≠ W_t(v)}.
  - WCH^S4a_P(v) := the in-phase S4a transitions of the phase P at which W(v) changes.

## 2. Carried lemmas (all game-general)
### 2.1 Lemma XW
Ξ_t(v) ⊴ W_t(v) for every v and t. Proof: σ̄_t minimises [S1-ord] at every vertex at once among Odd's strategies against σ_t ([S1-Xi]);
τ_t is one of them. □ (RESULTS R21 (a) signs this statement; its setting line is 𝒞^1O, its proof is game-general, so it is carried here.)
### 2.2 Lemma W-MON
If t → t + 1 is an S4a step, then W^{τ_t}_{t+1} ⊵ W^{τ_t}_t pointwise, where W^τ_s := val(σ_s, τ) on G_τ. In particular W_{t+1} ⊵ W_t when
τ_{t+1} = τ_t. Proof: σ_{t+1} is the optimal strategy of the one-player game H_t ([S4a]); σ_t uses only edges of H_t; the (σ, τ_t)-plays
of H_t and G_{τ_t} coincide for strategies inside H_t; [F1]. □
### 2.3 Lemma FB-W (box 21 §2.5 Lemma W, fallback half)
If k → k + 1 is a τ-fixed Even fallback, then W_{k+1} ⊴ W_k pointwise. Proof: S4c fires only if σ_new = σ_k, and S4a computed σ_new as the
optimal strategy of H_k (Iσ_k ≠ ∅), so σ_k is optimal in H_k. S4c's σ_{k+1} sets σ_{k+1}(v) ∈ Iσ_k(v) or keeps σ_k(v), so it is a strategy
of H_k. τ_{k+1} = τ_k = τ. By [F1] in H_k, val(σ_k, τ) ⊵ val(σ_{k+1}, τ) pointwise. □
### 2.4 Lemma OPT-OFF
Let H be a one-player game of Even (Odd fixed), ρ an optimal strategy of H, Ω_ρ its valuation, v an Even vertex that is not its own
Ω_ρ-cycle node, and (v, c) an edge of H. Then Ω_ρ(c) ⊴ Ω_ρ(ρ(v)).
Proof. Suppose Ω_ρ(c) ▷ Ω_ρ(ρ v). Let u be the cycle node of Ω_ρ(v), and ρ′ := ρ[v → c], a strategy of H. By [F1], Ω_ρ ⊵ Ω_ρ′.
- Case 1: the ρ-play from c avoids v. The ρ′-play from v is v followed by that play. So Ω_ρ′(v) = v ⊕ Ω_ρ(c), and Ω_ρ(v) = v ⊕ Ω_ρ(ρ v) [V1].
  Both plays avoid v, so [V2] gives Ω_ρ′(v) ▷ Ω_ρ(v): contradiction.
- Case 2: the ρ-play from c visits v. Let π be its part before the first v (a simple path, possibly empty if c = v).
  - Then Ω_ρ(c) and Ω_ρ(ρ v) have the same cycle node u. Their path sets differ exactly in S := {y ∈ π ∪ {v} : y more relevant than u},
    and Ω_ρ(c) is |π| + 1 longer.
  - The ρ′-play from v is the cycle Z := v, π (back to v).
  - (i) If S ≠ ∅: Ω_ρ(c) ▷ Ω_ρ(ρ v) forces max S even. max S is the most relevant vertex of Z, so it is the cycle node of Ω_ρ′(v). It is
    even and more relevant than u, so its reward exceeds u's (both even: more relevant; u odd: positive > negative). So Ω_ρ′(v) ▷ Ω_ρ(v):
    contradiction.
  - (ii) If S = ∅: the comparison is by length, longer wins, so u is odd. Every vertex of Z is less relevant than u. The cycle node z of Z
    then has a greater reward than u: even z is positive; odd z less relevant has −p′(z) > −p′(u). Contradiction as in (i). □
### 2.5 Lemma W-SUCC
On an interval [p, q] of one piece with τ := its τ, if v is not its own W-cycle node at any state of [p + 1, q], then W_t(σ_t v) is
non-decreasing (⊴) for t ∈ [p, q]. Proof: transition t → t + 1 (p ≤ t < q) is an S4a step with τ fixed. If σ_{t+1}(v) = σ_t(v), W-MON. Else
OPT-OFF in H_t at state t + 1 (σ_{t+1} optimal in H_t; v not its own W-cycle node at t + 1; (v, σ_t v) ∈ σ_t ⊆ H_t) gives W_{t+1}(σ_t v) ⊴
W_{t+1}(σ_{t+1} v), and W-MON gives W_t(σ_t v) ⊴ W_{t+1}(σ_t v). □

## 3. Late adoptions inside a piece
### 3.1 Lemma LATE-W
Let Q be a piece. Let v leave c at s → s + 1 in Q (σ_s(v) = c ≠ σ_{s+1}(v)). Let t′ > s be a state of Q at which (v, c) is blocked, and let v
not be its own W-cycle node at any state of [s + 1, t′]. Then W_{t′}(c) ▷ W_{s+1}(c).
Proof. W_{t′}(c) ▷ W_{t′}(σ_{t′} v) (blocked) ⊵ W_{s+1}(σ_{s+1} v) (W-SUCC on [s + 1, t′]) ⊵ W_{s+1}(c) (OPT-OFF in H_s at state s + 1:
(v, c) = (v, σ_s v) ∈ H_s, v not its own W-cycle node at s + 1). □
### 3.2 Corollary LATE-PIECE
Let Q be a piece and (v, c) an Even edge. A LATE ADOPTION of (v, c) in Q is an S4a transition u → u + 1 of Q with σ_{u+1}(v) = c ≠ σ_u(v)
such that (v, c) is blocked at some state of Q before u + 1. It is RE-BLOCKED if, for the latest leave s → s + 1 of c by v in Q with
s + 1 ≤ u, there is a state t′ ∈ [s + 1, u] at which (v, c) is blocked. (The first late adoption with no earlier leave in Q counts as
re-blocked vacuously.) Then
  #(re-blocked late adoptions of (v, c) in Q) ≤ 1 + WCH_Q(c) + CL_Q(v, c),
where WCH_Q(c) := the transitions of Q at which W(c) changes, and CL_Q(v, c) := the re-blocked late adoptions (other than the first) whose
window [s + 1, t′] contains a state at which v is its own W-cycle node.
Proof. Let u_1 < u_2 < … be the re-blocked late adoptions. For i ≥ 2, the leave s_i satisfies u_{i−1} < s_i (v holds c from u_{i−1} + 1 until
it leaves), and the window (s_i, t′_i] ⊆ (u_{i−1}, u_i]. If the window has v off its own W-cycle throughout [s_i + 1, t′_i], LATE-W gives a
change of W(c) at a transition t → t + 1 with s_i + 1 ≤ t < t′_i, which lies in Q. Otherwise u_i is counted in CL. The windows are disjoint. □

## 4. The gap set
### 4.1 Lemma GAP-MON
If k → k + 1 is a τ-fixed Even fallback, then Z_{k+1} ⊆ Z_k, and every v ∉ Z_k has Ξ_{k+1}(v) = Ξ_k(v) and W_{k+1}(v) = W_k(v).
Proof. For v ∉ Z_k: W_{k+1}(v) ⊴ W_k(v) (FB-W) = Ξ_k(v) ⊴ Ξ_{k+1}(v) ([R15]) ⊴ W_{k+1}(v) (XW). So all four are equal. □
### 4.2 Lemma SW-IN
Let k → k + 1 be a τ-fixed Even fallback, and v an Even vertex with σ_{k+1}(v) ≠ σ_k(v) that is its own Ξ-cycle node neither at k nor at
k + 1. Then Ξ_{k+1}(v) ▷ Ξ_k(v); hence v ∈ Z_k.
Proof. w := σ_{k+1}(v) has (v, w) ∈ Iσ_k ([S4c]), so Ξ_k(w) ▷ Ξ_k(σ_k v) ([S2]). Ξ_{k+1}(w) ⊵ Ξ_k(w) ([R15]). So b := Ξ_{k+1}(w) ▷ a := Ξ_k(σ_k v).
By [V1] at k and k + 1, the plays of a and b avoid v, Ξ_k(v) = v ⊕ a and Ξ_{k+1}(v) = v ⊕ b. By [V2], v ⊕ b ▷ v ⊕ a. If v ∉ Z_k, GAP-MON
would give Ξ_{k+1}(v) = Ξ_k(v). □
### 4.3 Lemma Z-FLAT
Call a τ-fixed Even fallback k → k + 1 Z-FLAT if Z_{k+1} = Z_k. At a Z-flat fallback:
- (a) Ξ and W change only at vertices of Z_k (GAP-MON);
- (b) every switched Even vertex that is its own Ξ-cycle node neither at k nor at k + 1 lies in Z_k and has a strict Ξ-rise (SW-IN);
- (c) W_{k+1} ⊴ W_k pointwise (FB-W), and Ξ_{k+1} ⊵ Ξ_k pointwise ([R15]);
- (d) no vertex of Z_k has Ξ_{k+1}(v) = W_{k+1}(v) (definition).
Proof: as cited in each item. □
### 4.4 Lemma REOPEN-W and Corollary REOPEN-CHARGE
REOPEN-W. Let k → k + 1 be an in-phase S4a transition. If v ∉ Z_k and v ∈ Z_{k+1}, then W_{k+1}(v) ▷ W_k(v).
Proof. τ_{k+1} = τ_k, so W_{k+1} ⊵ W_k (W-MON) and Ξ_{k+1} ⊵ Ξ_k ([R15]). If W_{k+1}(v) = W_k(v): Ξ_{k+1}(v) ⊵ Ξ_k(v) = W_k(v) = W_{k+1}(v) ⊵
Ξ_{k+1}(v) (XW). So v ∉ Z_{k+1}. □
REOPEN-CHARGE. For a phase P, RO_P := Σ over the in-phase S4a transitions k → k + 1 of P of |Z_{k+1} ∖ Z_k|. Then RO_P ≤ Σ_v WCH^S4a_P(v).
Proof: each counted pair (v, k) has a W(v)-change at k → k + 1 by REOPEN-W. □

## 5. Theorem GAP-RED (a REDUCTION of FB-LIN)
For every phase P with first state a: let f_P := its in-phase fallbacks, ZF_P := its Z-flat in-phase fallbacks. Then
  f_P ≤ |Z_a| + RO_P + ZF_P ≤ n + Σ_v WCH^S4a_P(v) + ZF_P.
Proof. Every in-phase transition is an S4a step or a τ-fixed Even fallback (§1). Along P, |Z| starts at |Z_a| ≤ n and is ≥ 0. At an in-phase
fallback that is not Z-flat, |Z| drops by at least 1 (GAP-MON: Z_{k+1} ⊊ Z_k). At a Z-flat one it is unchanged. At an in-phase S4a step it
grows by at most |Z_{k+1} ∖ Z_k|. Summing: #(non-Z-flat in-phase fallbacks) ≤ |Z_a| + RO_P. Add ZF_P, then REOPEN-CHARGE. □
- So CONJECTURE FB-LIN (≤ n in-phase fallbacks per phase) and any polynomial form of it follow from:
  - polynomial bounds per phase on Σ_v WCH^S4a_P(v) (per-vertex W-changes at in-phase S4a steps); and
  - polynomial bounds on ZF_P (Z-flat fallbacks).
  Neither is bounded here.

## 6. NOT to sign: DEAD, DATA, READING
- DEAD (box 67, experiments/new/box67/energy.py): six candidate Lyapunov energies for "drops at every in-phase fallback". Of 731 alt_all
  fallbacks, the number at which each does NOT strictly drop (and its rises at S4a steps):
  - E1 = #Even v with Iσ(v) ≠ ∅: 537 (1220); E2 = Σ(rank + 1) over those: 414 (2947);
  - E3 = |Z|: 56 (2440); E4 = |D|, D = {Odd u : σ̄(u) ≠ τ(u)}: 685 (469);
  - E5 = #v whose (σ, τ)-play meets D: 55 (2429); E6 = #blocked edges: 304 (1111).
  - Smallest killing instance for E3 / E5: experiments/n5-epoch/instances/lend9_n8.pg with its .start (n 8). It has 3 in-phase fallbacks
    in one phase, with no drop of E3 (check.sh "box 67").
- DATA:
  - GAP-MON: Z grows at 0 of 788 in-phase fallbacks (alt_all 413 games + fb38_n48, pl130_n40, long121_n40 with starts).
  - SW-IN: 0 switched off-cycle vertices outside Z. REOPEN-W: 8532 / 8532 re-openings have a W-rise.
  - Z-flat: 56 of 788; record nep22f_n64 (10 in one phase, |Z| = 59 of 64, 1 Ξ cycle node in Z; check.sh "box 68").
  - LATE-W: 182 checks, 0 violations (box 66, latepair.py). The inversion-potential import for LATE is DEAD at piece boundaries:
    b6_xl2_n32 (sha1 909c7371…), one edge late-adopted 4 times in one λ-run, once per piece (check.sh "box 66").
- READING:
  - Z-flat fallbacks are Ξ-climbs inside a gap that stays open (the Ξ-route).
  - Re-openings are W-changes, i.e. the WCH ↔ R* quantity of RESULTS R88 / R89 (FW-R*, GP*-RUN) read per vertex.
- Pinned checks: experiments/new/check.sh blocks "box 66", "box 67", "box 68".

## DONE / FINDINGS / NEEDS
- DONE: this packet.
- FINDINGS: 13 items to sign (§0), all reductions or structural lemmas; no iteration bound.
- NEEDS: none from the owner.
