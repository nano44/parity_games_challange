# N5-TORD (box 30): the trapped part of a frozen W-phase for |D| = 1 — prefix frame, Lemma H-P, Theorem TORD (≤ s² prefix W-changes per epoch), Theorem TRAP-FIX (c₁ ≠ c₂ ⇒ one epoch), Corollary FW-D1 (FW-BF's polynomial form for |D| = 1, c₁ ≠ c₂, tail-disjoint)
L-SI successor 26 (Opus 5.5; D18, Lead reading L40). Lead's brief 2026-10-29 13:15Z, STEP 2: «FW-BF's trapped part ... First the two-order
switch-best for |D| = 1: the arena comes from one VJ prefix order, the choice from another. Then the trap changes per frozen W-phase. The
weaker target is FW-D ≤ (|D|+1)(n−1).» Working note, unrefereed, not frozen. Not a TARGET.md claim. Nothing here bounds N5's running time;
G-N5-TIME stays OPEN. Labels (D18 / L40): PROVED (lane) / CONJECTURE / OPEN / DATA / READING / DEAD. Counts are TRANSITIONS.
Setting, notation and the lemmas used: docs/si/N5-FRZ-box29.md §0-§2, §7 (W-MON, XW, CN-W, W-SPLIT, EPOCH-U; frozen W-phase, epoch, S = S^p,
U = V ∖ S). Tools: experiments/si/tord/ (epoch2.py on the three corpora; abs2.py, abs3.py abstract models with climbs climb.py, climb3.py);
outputs tord/epoch2_*.txt, tord/logs/.

## Summary
| § | item | label |
| --- | --- | --- |
| §1 | prefix form: for trapped x, Ξ(x) = pre(x) ⊕ Ξ(o), W(x) = pre(x) ⊕ W(o); the two prefix orders ≤₁ (Ξ), ≤₂ (W) depend only on c₁ = λ_Ξ(o), c₂ = λ_W(o), both constant in a frozen W-phase; case list (same / X> / W>) | PROVED (lane) |
| §2 | Lemma PMON: inside an epoch, under TD (τ(o), σ̄(o) ∈ U), every trapped prefix is non-decreasing in ≤₁ and in ≤₂; a switched trapped vertex rises strictly in ≤₁ | PROVED (lane) |
| §3 | Lemma H-P: Lemma P (R17 (b)) for the common coarsening H (prefix set above θ_hi) of ≤₁ and ≤₂: after k steps of an epoch, H_k(x) ⊵ H(r) for every path r of ≤ k edges into o; so H is constant after s := \|S\| − 1 steps | PROVED (lane) |
| §4 | Theorem TORD: in an epoch (|D| = 1, TD), at most s² transitions change a trapped prefix in ≤₂ (≤ s if c₁ = c₂); if rank c₂ < rank c₁ at most s² transitions switch a trapped vertex | PROVED (lane) |
| §5 | Theorem TRAP-FIX: if c₁ ≠ c₂, S is constant in the whole frozen W-phase (one epoch). No TD needed. Generalisation to any D: the union of S_d over gates d with the same pair (c₁(d), c₂(d)), c₁(d) ≠ c₂(d), is constant | PROVED (lane) |
| §6 | Corollary FW-D1: a frozen W-phase with D = {o}, c₁ ≠ c₂ and TD has WCH ≤ \|U\| − 1 + s² < n² (and, if rank c₂ < rank c₁, length ≤ \|U\| − 1 + s²) | PROVED (lane) |
| §7 | DATA: 0 violations of every check on 1,546 |D| = 1 frozen W-phases (3,702 TD epochs); 303 with c₁ ≠ c₂, all one epoch; prefix W-changes per epoch ≤ s everywhere (max ratio 1.0) | DATA |
| §8 | abstract two-order model (abs2) and gate model (abs3): climbs plateau at exactly n_abs W-changing steps (same, EE, OO, OE; n ≤ 8) | DATA |
| §9 | open: CONJECTURE TORD-BF (≤ s per epoch); the c₁ = c₂ case: the number of epochs (the optimism trap is the obstruction, two failure modes F1/F2); |D| ≥ 2 | OPEN |

## 0. Setting (the part of box 29 used)
N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md). A frozen W-phase F (box 29 §0): τ, σ̄, D = {Odd u : σ̄(u) ≠ τ(u)}, λ_Ξ, λ_W constant, no
fallback. ρ_k := σ at the k-th state of F; W_k = val(ρ_k, τ), Ξ_k = val(ρ_k, σ̄_k) = val(ρ_k, σ̄) (σ̄ constant on F). Here D = {o}.
S_k := vertices whose (ρ_k, τ)-play meets o (o ∈ S_k); U_k := V ∖ S_k. An EPOCH is a maximal run of states of F with S_k constant
(box 29 §7). s := |S| − 1 (trapped vertices other than o). Facts used: (F1) S4a's ρ_{k+1} is pointwise W-optimal in the arena H_k
(Even v keeps {ρ_k(v)} ∪ Iσ_k(v), Odd v keeps τ(v); box 29 W-MON's proof); (V2) prefix monotonicity of VJ values (R17 (a)); EPOCH-U
(box 29 §7, lane): in an epoch U is closed under (ρ_k, τ)-plays, Ξ_k = W_k on U, at most |U| − 1 transitions change W on U.
TD (tail-disjoint) := τ(o) ∈ U and σ̄(o) ∈ U at every state of the epoch. DATA: TD holds in 3,702 of 4,021 |D| = 1 epochs (§7).

## 1. PROVED (lane): the prefix form and the case list
- For trapped x ≠ o, pre_k(x) := the (ρ_k, τ)-play from x up to and excluding its first visit of o. Since σ̄ = τ off D, the (ρ_k, σ̄)-play
  from x is the same up to o. So λ_Ξ(x) = λ_Ξ(o) =: c₁ and λ_W(x) = λ_W(o) =: c₂ (the plays from x continue as the plays from o), and
  under TD (o's two tails lie in U, which the plays from S do not re-enter before o): Ξ_k(x) = pre_k(x) ⊕ Ξ_k(o), W_k(x) = pre_k(x) ⊕ W_k(o)
  (⊕ = VJ00's extension, applied vertex by vertex). c₁, c₂ are constant on F (λ_Ξ, λ_W are).
- Consequence (by (V2)): for trapped y, y′ at the SAME state, Ξ_k(y) vs Ξ_k(y′) is the comparison of pre_k(y) vs pre_k(y′) in the prefix order
  ≤₁ for cycle node c₁: compare P₁ := {v on the prefix : rank v > rank c₁} by the top vertex of the symmetric difference (better if it is
  even and in the better set's side, as VJ00), then the length (c₁ even: shorter better; c₁ odd: longer better). W likewise with ≤₂ for
  c₂. (pre(o) = ∅.) So among trapped vertices the arena Iσ_k compares in ≤₁ and the choice (F1) optimises in ≤₂: the «two-order
  switch-best» of box 29 §7. The orders are FIXED on F (they depend on c₁, c₂ only, not on the tails' P-sets and lengths).
- Cases. By Lemma XW (Ξ ⊴ W) at o, either c₁ = c₂ («same»: ≤₁ = ≤₂) or reward(c₂) > reward(c₁). Then (rewards: even p′ ↦ p′, odd p′ ↦ −p′):
  X> (rank c₁ < rank c₂): c₂ is even (an odd c₂ above c₁ has reward below c₁'s). With θ_hi := rank c₂: ≤₂ = (H, length, shorter better),
       ≤₁ = (H, Mid, length in c₁'s direction), where H(p) := {v ∈ p : rank v > θ_hi}, Mid(p) := {v ∈ p : rank c₁ < rank v < rank c₂}.
  W> (rank c₂ < rank c₁): c₁ is odd (an even c₁ above c₂ has reward above c₂'s). With θ_hi := rank c₁: ≤₁ = (H, length, LONGER better),
       ≤₂ = (H, Mid, length in c₂'s direction).
  In both, ≤₁ and ≤₂ REFINE the H-order (a ▷_H b ⇒ a ▷₁ b and a ▷₂ b: the top differing vertex above θ_hi decides both).

## 2. PROVED (lane): Lemma PMON (prefix monotonicity inside an epoch, TD)
Lemma PMON. Let k → k + 1 be a transition inside an epoch of F (D = {o}, TD). For every trapped x ≠ o: pre_{k+1}(x) ⊵₂ pre_k(x) and
pre_{k+1}(x) ⊵₁ pre_k(x); if ρ_{k+1}(x) ≠ ρ_k(x) (x switched) then pre_{k+1}(x) ▷₁ pre_k(x).
Proof (≤₂). Let ρ̃ := ρ_k on S, ρ_{k+1} on U. ρ̃ is a strategy of the arena H_k (ρ_k's edges and ρ_{k+1}'s edges are in H_k). From x ∈ S the
ρ̃-play follows ρ_k inside S to o (the ρ_k-play from x stays in S_k = S), then τ(o) ∈ U (TD) and ρ_{k+1} inside U, which is closed under
ρ_{k+1}-plays (S_{k+1} = S). So val_ρ̃(x) = pre_k(x) ⊕ W_{k+1}(o) while W_{k+1}(x) = pre_{k+1}(x) ⊕ W_{k+1}(o). (F1) gives
W_{k+1}(x) ⊵ val_ρ̃(x); equal tails, so (V2) gives pre_{k+1}(x) ⊵₂ pre_k(x).
Proof (≤₁). Each switched trapped x moves to z := ρ_{k+1}(x) with (x, z) ∈ Iσ_k, i.e. Ξ_k(z) ▷ Ξ_k(ρ_k(x)); z ∈ S_{k+1} = S_k, so both
are trapped at state k and this reads pre_k(z) ▷₁ pre_k(ρ_k(x)) (§1). The ρ_{k+1}-plays from S reach o without a cycle (λ_W constant),
so induct on the ρ_{k+1}-distance to o; y := ρ_{k+1}(x), IH pre_{k+1}(y) ⊵₁ pre_k(y). Not switched (y = ρ_k(x)): x ∉ pre_{k+1}(y),
x ∉ pre_k(y), so (V2) gives x·pre_{k+1}(y) ⊵₁ x·pre_k(y). Switched: pre_{k+1}(y) ⊵₁ pre_k(y) ▷₁ pre_k(ρ_k(x)) (pre_k(y) is a simple path
from y, possibly through x; transitivity of the key order), and x lies in neither pre_{k+1}(y) nor pre_k(ρ_k(x)), so strict (V2) gives
pre_{k+1}(x) ▷₁ pre_k(x). □ (Tails do not enter the ≤₁ part; TD is used for the prefix form of the comparisons.)

## 3. PROVED (lane): Lemma H-P (Lemma P for the common coarsening)
Lemma H-P. Let an epoch of F start at state 0 (D = {o}, TD), and let r = (x = r₀, …, r_L = o) be a simple path of G_τ (Odd vertices keep
τ) with r₀, …, r_{L−1} ∈ S, L ≤ k. Then H_k(x) := H(pre_k(x)) ⊵_H H(r) := H({r₀, …, r_{L−1}}), as long as state k is in the epoch.
Proof by induction on k (k = 0: L = 0, x = o, both sides ∅). Step: r = x → z → r′, |r′| ≤ k, x ∉ r′; IH H_k(z) ⊵_H H(r′). Hx := {x} if
rank x > θ_hi, else ∅. Odd x: z = τ(x) = ρ(x); H_{k+1}(x) = Hx ∪ H_{k+1}(z) ⊵_H Hx ∪ H_k(z) (PMON) ⊵_H Hx ∪ H(r′) = H(r).
Case A, (x, z) ∉ Iσ_k: pre_k(z) ⊴₁ pre_k(ρ_k(x)), and ≤₁ refines H, so H(r′) ⊴_H H_k(z) ⊴_H H(pre_k(ρ_k(x))). x is in neither r′ nor
pre_k(ρ_k(x)), so H(r) = Hx ∪ H(r′) ⊴_H Hx ∪ H(pre_k(ρ_k(x))) = H_k(x) ⊴_H H_{k+1}(x) (PMON, ≤₂ refines H).
Case B, (x, z) ∈ Iσ_k. Let π := pre_k(z).
  B1, x ∉ π: ρ̂ := ρ_k[x → z] on S, ρ_{k+1} on U, is a strategy of H_k; its play from x is x, π, o, then U under ρ_{k+1}; (F1):
      pre_{k+1}(x) ⊕ W_{k+1}(o) = W_{k+1}(x) ⊵ val_ρ̂(x) = x·π ⊕ W_{k+1}(o), so pre_{k+1}(x) ⊵₂ x·π and H_{k+1}(x) ⊵_H Hx ∪ H(π) ⊵_H Hx ∪ H(r′).
  B2, x ∈ π: the ρ̂-play from x is the cycle Z = x, z, π[z..x) ⊆ S. pre_k(z) = π[z..x)·pre_k(x) and pre_k(ρ_k(x)) = pre_k(x) ∖ x, so the
      symmetric difference of their ≤₁-sets is D₁ := {v ∈ Z : rank v > rank c₁}, the lengths differ by |Z| > 0, and improvement means: D₁ ≠ ∅
      with top vertex even, or D₁ = ∅ and the longer side wins (c₁ odd). Let D_H := {v ∈ Z : rank v > θ_hi} ⊆ D₁.
      D_H ≠ ∅: top(D₁) = top(D_H) is EVEN and is the top of Z, with rank > θ_hi ≥ rank c₂, so reward(top Z) > reward(c₂); by (F1) W_{k+1}(x)
      is at least the value of the cycle Z, so λ_W(x) changes at k + 1: not a transition of F. Contradiction.
      D_H = ∅: π[z..x) and x have no vertex above θ_hi, so H_k(z) = H_k(x) and Hx = ∅; H(r) = H(r′) ⊴_H H_k(z) = H_k(x) ⊴_H H_{k+1}(x). □
Corollary H-STAB. Every simple path from x into o inside S has ≤ s edges, and pre_k(x) is one of them. So for k ≥ s, H_k(x) is the
⊴_H-maximum over those paths: H is constant on the epoch from step s on, and at most s transitions of the epoch change H at some vertex.

## 4. PROVED (lane): Theorem TORD (counts inside one epoch, |D| = 1, TD)
Theorem TORD. In an epoch of a frozen W-phase with D = {o} and TD, with s = |S| − 1:
 (i) c₁ = c₂: at most s transitions change some trapped prefix (Lemma H-P with θ_hi replaced by the full prefix order ≤₁ = ≤₂, which both
     sides then use: R17 (b)'s Lemma P with the cycle case B2 as in §3: D₁ ≠ ∅ ⇒ λ_W change; D₁ = ∅ ⇒ top(Z) is below the odd c₁, hence
     a better cycle for Even ⇒ λ_W change; and c₁ even with D₁ = ∅ is not improving).
 (ii) X> (rank c₁ < rank c₂, c₂ even): at most s² transitions change some trapped prefix in ≤₂.
 (iii) W> (rank c₂ < rank c₁, c₁ odd): at most s² transitions switch a trapped vertex (hence at most s² change a trapped prefix at all).
Proof. (ii) At most s such transitions lie in the first s steps (H-STAB: afterwards H is constant). After that ≤₂ = (H, length, shorter
better) with H fixed; by PMON (≤₂) each trapped prefix length is non-increasing, and a ≤₂-change of pre(x) is a strict decrease of
|pre(x)| ∈ [1, s]. So Σ_x |pre(x)| ≤ s² drops at each such transition: at most s(s − 1) of them. Total ≤ s + s(s − 1) = s².
(iii) After step s, ≤₁ = (H, length, LONGER better) with H fixed; by PMON (≤₁) every prefix length is non-decreasing and every switched
trapped vertex rises strictly in ≤₁, i.e. its length grows. So Σ_x |pre(x)| ≤ s² grows at each transition that switches a trapped
vertex: at most s(s − 1) after step s, s² in total. A prefix changes only if a vertex on it switches. □
- READING. (ii) bounds W-changes, not length: in X> a trapped switch can be W-silent (Mid rises at equal length), so the epoch's LENGTH
  is not bounded by this argument (FW-LEN stays CONJECTURE there). In W> the Ξ side is a length-only order after H-STAB, which bounds
  every trapped switch. The data (§7) and the abstract climbs (§8) never exceed s, so s² is the proof's slack, not the behaviour.

## 5. PROVED (lane): Theorem TRAP-FIX (c₁ ≠ c₂ ⇒ one epoch); the general-D form
Theorem TRAP-FIX. In a frozen W-phase F with D = {o} and c₁ = λ_Ξ(o) ≠ c₂ = λ_W(o), S_k is the same set at every state of F.
Proof. For trapped y, λ_Ξ(y) = c₁ and λ_W(y) = c₂ (§1; no TD needed: the plays from y continue as the plays from o). For untrapped u,
the (ρ, σ̄)- and (ρ, τ)-plays coincide (they meet no D vertex), so λ_Ξ(u) = λ_W(u). λ_Ξ and λ_W are constant on F. If y ∈ S_k ∖ S_{k+1},
then λ_Ξ(y) = c₁ at k and λ_Ξ(y) = λ_W(y) = c₂ at k + 1; if y ∈ S_{k+1} ∖ S_k, then λ_Ξ(y) = λ_W(y) = c₂ at k and c₁ at k + 1. Both
change λ_Ξ(y), so both contradict c₁ ≠ c₂. □
- General D (same proof). For a gate d ∈ D let S_d := vertices whose play meets D first at d; π(d) := (λ_Ξ(d), λ_W(d)). A vertex can move
  between S_d and S_{d′} only if π(d) = π(d′), and between S_d and U only if λ_Ξ(d) = λ_W(d). So for every pair π = (c, c′) with c ≠ c′
  the union ∪{S_d : π(d) = π} is constant on F; only gates with λ_Ξ(d) = λ_W(d) exchange vertices with U. PROVED (lane).
- So TRAP-MONO (box 29 §7, DEAD) fails only in the c₁ = c₂ case: its two counterexamples have |D| = 3 (fbrestart_cex_n12, lend107_n32).

## 6. PROVED (lane): Corollary FW-D1
Corollary FW-D1. A frozen W-phase F with D = {o}, c₁ ≠ c₂ and TD has at most |U| − 1 + s² W-changing transitions (n = |U| + s + 1, so
fewer than n² for n ≥ 2). If moreover rank c₂ < rank c₁ (W>), F has at most |U| − 1 + s² transitions.
Proof. F is one epoch (TRAP-FIX). A transition changes W at a vertex of U (EPOCH-U: ≤ |U| − 1 of them), or at a trapped vertex. W(o) =
o ⊕ W(τ(o)) with τ(o) ∈ U (TD), so a change of W at o, or a tail-induced change of W at trapped x (W(x) = pre(x) ⊕ W(o)), is a change of W on
U at the same transition. The remaining transitions change some trapped prefix in ≤₂: ≤ s² (TORD (ii); in W>, (iii); c₁ ≠ c₂ excludes (i)).
For the length in W>: a transition switches a trapped vertex (≤ s², TORD (iii)) or only U vertices, and then it changes W on U (EPOCH-U:
the restriction to U is switch-best on G_τ[U], where every switch raises W at the switched vertex): ≤ |U| − 1. □
- What this is against FW-BF (n − 1) and FW-D ((|D| + 1)(n − 1) = 2(n − 1)): a polynomial bound of the same type, quadratic instead of
  linear, for the |D| = 1 frozen W-phases with c₁ ≠ c₂ and TD (303 of 1,546 |D| = 1 frozen W-phases in the corpora; §7). With W-SPLIT
  (box 29 §2) such frozen W-phases contribute O(n²) each.

## 7. DATA (experiments/si/tord/epoch2.py; outputs tord/epoch2_{alt_start,lib41,sicorpus}.txt)
| corpus | \|D\| = 1 frozen W-phases | of them c₁ ≠ c₂ | epochs (same / X> / W>) | TD epochs | violations PMON1, PMON2, HLP, LMON, CNT, TRAPFIX, FWD1 |
| --- | --- | --- | --- | --- | --- |
| alt_all pinned starts (START=1) | 567 | 122 | 1,442 / 100 / 22 | 1,433 | 0 |
| lib41 (n ≤ 48) | 665 | 146 | 1,612 / 117 / 29 | 1,611 | 0 |
| experiments/si (START=1; 1 input skipped) | 314 | 35 | 664 / 31 / 4 | 658 | 0 |
- TRAP-FIX: every one of the 303 frozen W-phases with c₁ ≠ c₂ is ONE epoch; epochs per frozen W-phase reach 34 / 26 / 20, all in the
  c₁ = c₂ case.
- Prefix W-changes per epoch ≤ s in every epoch (CONJECTURE TORD-BF, below): largest ratio 1.0 (red/xing/instances/obr_eq_n24, W>, not
  TD, s = 4); largest count 111 (runlin/instances/runfam_K100, same, s = 126); 25 (lib41 / alt_all). Largest WCH/(n − 1) over the c₁ ≠ c₂
  frozen W-phases: 0.806 (red/xing/instances/kw25_n32, 25 at n 32, s = 28).
- The s(s − 1) term of TORD (ii)/(iii) never fires: in no TD epoch with c₁ ≠ c₂ does a trapped prefix length change after step s (the
  LMON control with the direction reversed, MUT=lmon, does not bite on lib41). Control that bites: MUT=hlp0 (H constant from step 1
  instead of s) fails on 128 lib41 epochs (e.g. new/box21/instances/oneodd_c16, b6_xl_n40). check.sh «box 30» pins oneodd_c16 (sha1
  827976e2…) and kw25_n32 (sha1 607f1cc0…).

## 8. DATA: the abstract models (experiments/si/tord/abs2.py, abs3.py; climbs climb.py, climb3.py; logs tord/logs/)
- abs2 (two-order switch-best, the static form of §1: Even-only graph on n_abs vertices into the gate, orders ≤₁ / ≤₂ from (θ₁, parity),
  (θ₂, parity) with reward(c₂) > reward(c₁); arena ≤₁-improving, choice the exhaustive pointwise ≤₂-optimum; cycles avoiding the gate are
  exits if better than c₂, else worst). Climbs, score (W-changing steps, steps), n_abs = 6, 7, 8, modes same / EE / OO / OE (and by steps):
  every climb plateaus at EXACTLY n_abs W-changing steps and n_abs steps (e.g. EE, n_abs = 8: one Bellman-Ford wave along a 7-edge path).
  So in the static model the two orders never beat the one-order bound. STALL (choice = ρ while the arena is non-trivial; N5 would fall
  back) is frequent with two orders and never occurs with one (random search, 2,000 games per n).
- abs3 (gate model for c₁ = c₂: untrapped vertices with direct paths to c, the gate's tail pessimistic (Ξ) or optimistic (W)): climbs at
  n_abs = 6, 7 plateau at n_abs W-changing steps, with up to 5 trap changes in a run (stopped by hand after ~10,000 steps each; logs end without FINAL).

## 9. OPEN, CONJECTURE, and the obstruction for c₁ = c₂
- CONJECTURE TORD-BF: in every epoch of a |D| = 1 frozen W-phase (TD), at most s transitions change a trapped prefix in ≤₂. DATA §7, §8.
  (Proved for c₁ = c₂, TORD (i); s² proved for c₁ ≠ c₂.)
- OPEN: the number of epochs when c₁ = c₂ (TRAP-FIX does not apply; up to 34 epochs per frozen W-phase in the data). Within each epoch the
  counts are linear (TORD (i) + EPOCH-U: ≤ s_e + |U_e| − 1 W-changes), so FW-BF for |D| = 1 reduces to the epoch count in the c₁ = c₂ case.
  READING (the obstruction). With c₁ = c₂ = c the frames differ only in the gate's tail (Ξ pessimistic α₁, W optimistic α₂ ▷ α₁, same c).
  A one-frame Lemma P across epochs fails in exactly two ways: (F1) an untrapped x is refused an edge into S by the arena (pre_z ⊕ α₁ ⊴
  W(ρx) ◁ pre_z ⊕ α₂): Case A in the W frame; (F2) a trapped x keeps (or takes) the gate although an arena edge to U is Ξ-better
  (optimism trap, box 29 §5; s_elim24_final x = 3): Case B in the Ξ frame. Each frame's Lemma P holds on the other frame's failure set.
- OPEN: |D| ≥ 2 (several gates with different tails: trapped comparisons are not pure prefix comparisons); the non-TD epochs (319 of 4,021).
- Next (Lead's order): the c₁ = c₂ epoch count (§10); then FW-D for |D| ≥ 2 via the gate classes of §5.

## DONE / FINDINGS / NEEDS
- DONE: this note; tools experiments/si/tord/ (epoch2.py, abs2.py, abs3.py, climb.py, climb3.py, search.py, show.py); data
  tord/epoch2_*.txt, tord/logs/; check.sh «box 30» block.
- FINDINGS: (1) PROVED (lane): for |D| = 1 the trapped dynamics is a two-order switch-best on PREFIXES with orders fixed by c₁, c₂ (§1),
  prefix-monotone in both orders inside an epoch (PMON), with Lemma P for the common coarsening H (H-P). (2) PROVED (lane): ≤ s² trapped
  prefix W-changes per epoch (TORD), and c₁ ≠ c₂ ⇒ ONE epoch (TRAP-FIX; general-D form by gate classes). (3) PROVED (lane) FW-D1: |D| = 1,
  c₁ ≠ c₂, TD ⇒ WCH ≤ |U| − 1 + s² < n². (4) DATA: 0 violations; prefix W-changes ≤ s per epoch everywhere; abstract climbs stop at n_abs.
  (5) OPEN: epochs for c₁ = c₂ (obstruction F1/F2), |D| ≥ 2, non-TD.
- NEEDS: none from the owner.

## 10. The c₁ = c₂ case: trap changes (Lead's second item). Written 2026-10-29T14:3xZ by date -u (see commit)
Tools: experiments/si/tord/cross.py (crossings per frozen W-phase), tord/silent.py (W-silent transitions), tord/xclimb.py (kill climbs);
outputs tord/cross_*.txt, tord/silent_*.txt, tord/out/ (climbs). Notation as §0; here c₁ = c₂ = c, so ≤₁ = ≤₂ on prefixes and the frames
differ only in the gate's tails: α₁ := Ξ(o) (pessimistic), α₂ := W(o) (optimistic), α₂ ⊵ α₁ (Lemma XW), same cycle node c.
- Remark (one frame). If α₂ = α₁ then Ξ = W at every vertex and the frozen W-phase is switch-best on G_τ in ONE frame: FW-D0's argument
  (R17 (b), (c)) gives ≤ n − 1 W-changes. So below α₂ ▷ α₁ («strict gap»); then S = {v : W(v) ▷ Ξ(v)} (play form = value form).
- Lemma SIL-EXIT (PROVED, lane). In a |D| = 1 frozen W-phase with c₁ = c₂, strict gap and TD at states k and k + 1: if the transition
  k → k + 1 is W-silent (W_{k+1} = W_k at every vertex), then no vertex enters S, and every switched vertex either leaves S or is its own
  cycle node (a flat cycle-closing switch, R17 (b) case B2). Proof. W is unchanged on U, so Ξ = W is unchanged on U, and α₁ = o ⊕ Ξ(σ̄(o)),
  α₂ = o ⊕ W(τ(o)) are unchanged (TD). A switched x rises strictly in Ξ unless it closes a flat cycle at itself (the switch (x, z) ∈ Iσ_k and
  Ξ_{k+1}(z) ⊵ Ξ_k(z), as in R17). x ∈ U_k ∩ U_{k+1}: Ξ = W at x, so W rises. x ∈ S_k ∩ S_{k+1}: Ξ = pre ⊕ α₁ with α₁ fixed, so pre rises in ≤₁
  = ≤₂, so W = pre ⊕ α₂ rises. x ∈ U_k ∩ S_{k+1}: W_{k+1}(x) = pre′ ⊕ α₂ ▷ pre′ ⊕ α₁ = Ξ_{k+1}(x) ⊵ Ξ_k(x) = W_k(x). All three contradict
  W-silence, so x ∈ S_k ∖ S_{k+1}. A non-switched vertex v entering S would have a first switched vertex w on its old play with w entering
  S (v's new play is its old play up to w, then w's new play). □ So in this case a phase's W-silent transitions only shrink S.
- DATA (silent.py, the three corpora): NO W-silent transition occurs in any |D| = 1, c₁ = c₂ frozen W-phase (SIL-EXIT is vacuous there:
  every transition of those frozen W-phases changes W). Two or more consecutive W-silent transitions occur in 23 frozen W-phases (9 alt_all,
  12 lib41, 2 experiments/si), up to 8 in a row (red/xing/instances/u23sw64_n32, |D| = 1, c₁ ≠ c₂: X> case, Mid rises at equal length, as
  TORD's READING says), so «W-silent transitions are isolated» is not a general fact (it was a candidate here, not a published claim).
- DATA (cross.py): |D| = 1, c₁ = c₂ frozen W-phases: 445 / 519 / 279 (alt_all pinned / lib41 / experiments/si), of which 257 / 305 / 150
  change S at least once. Trap-changing transitions TC per frozen W-phase ≤ 33 (red/so/instances/nleq33_n48, n 48: 0.70(n − 1)), 25
  (red/xing/instances/x32_waves48, n 48), 19 (si/riselast/instances/rl_b, n 32). Entries per vertex ≤ 2 and exits per vertex ≤ 2 everywhere;
  a vertex that leaves and re-enters occurs in 3 games (red/xing/instances/x31_re24: vertices 0-3 out at t = 2, in at 3, out at 4, in at
  5, gap = one length unit at the gate: α₁ = (∅, 2), α₂ = (∅, 1), c = 20 even; x31_ru24; si/xing/instances/zcl_rx_n48). TC ≤ WCH + 1
  in every such frozen W-phase (silent.py; max TC/WCH = 1.0, n5-exhaustive/instances/b6_xl2_n32 11/11).
- CONJECTURE TRAP-LIN: a |D| = 1, c₁ = c₂ frozen W-phase has at most n − 1 trap-changing transitions. With TORD (i) and EPOCH-U per epoch,
  TRAP-LIN would give WCH ≤ n(n − 1) for every |D| = 1 TD frozen W-phase (polynomial FW-BF for |D| = 1). Kill search: §10.1.
- READING (why a proof is not yet in hand). A re-entry needs the vertex's prefix to beat its previous prefix by the gap (re-entry at p′ after
  an exit at p: p′ ⊕ α₁ ⊵ Ξ ⊵ p ⊕ α₂), so each exit-entry round is a strict prefix improvement «by at least the gap». Bounding the number of
  such improvements per vertex needs a Lemma P across epochs, which fails in the two ways F1/F2 of §9.
### 10.1 Kill search for TRAP-LIN / X2 (tord/xclimb.py; logs tord/out/)
Score: max over |D| = 1, c₁ = c₂ frozen W-phases of TC/(n − 1) (kill: TC > n − 1, or a vertex entering S 3 times = CONJECTURE X2, or
FW-BF). Seeds nleq33_n48 (0.702), x32_waves48 (0.531), x31_re24 (0.173, 2 entries per vertex; also with XCR=1, which scores crossings).
The long trap-change runs of the corpora are MONOTONE WAVES (nleq33_n48: 33 transitions, each removes one vertex from S; x32_waves48: 25
transitions, each adds one), so TC ≤ n there for a trivial reason; non-monotone S occurs only in short phases (x31_re24: 4 transitions).
- RESULT (no kill; DATA): nleq33_n48 seed → 0.809 (n 43; stopped by hand at 14:57Z after 34,304+ steps); x32_waves48 → 0.868
  (n 39; 100,000 steps, entries per vertex 2); x31_re24 → 0.636 (n 12; 100,000 steps); x31_re24 with XCR=1 → 2 entries per vertex, no 3
  (n 11; 100,000 steps). TRAP-LIN and X2 stay CONJECTURES; the best TC/(n − 1) found is 0.868.
