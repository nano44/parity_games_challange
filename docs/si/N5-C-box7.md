# N5 box 7: the proof side of carries (C). Fallbacks per phase are bounded by non-tame transitions
L-SI successor 3 (Opus 5.5, D18/L40). Lead GO 2026-10-24 21:3xZ. Started 21:31Z (date -u).
Labels (L40): PROVED (by whom; all PROVED items here are by L-SI succ. 3 and UNREFEREED unless stated), CONJECTURE, OPEN, DATA,
READING, FALSE.
Scope: these are lemmas about the candidate N5. They are not a running-time bound, not a TARGET.md claim, and not a step-4 pass.
G-N5-TIME stays OPEN.
ASSUMPTIONS, one line each:
- §2-§4 hold on EVERY parity game (no 𝒞^1O needed). §4 uses only "λ_Ξ constant" and "τ constant".
- §5 assumes 𝒞^1O (exactly one Odd vertex o with out-degree > 1; asserted by every script in experiments/si/coarse/).
- PHASE = joint λ-phase with τ constant (box 28 key (λ_Ξ, λ_U, τ(o)); P-N5-Z §0).

## 0. Results in short
- PROVED: **Lemma COARSE-SI** (§2), box 6's Step 1 written out in full, in two forms:
  - (a) general form, with the exact cycle condition (NC), and its converse;
  - (b) the in-phase form **TAME**, which needs no condition on Even and pins down where tameness can fail.
- PROVED: **Lemma MONO** (§3). Let M_k := the largest level of a gate edge at state k. Then M_{k+1} ≤ M_k at every TAME transition, i.e.
  every transition at which no Ξ(v) changes at a level above M_k. (Box 6's Step 2 with L = M_k.)
- PROVED: **Lemma NOINF** (§3). Inside a phase, no transition switches a gate edge whose target has a different cycle node. So every
  in-phase fallback has M_k < ∞.
- PROVED: **Theorem FB** (§4). Inside one phase,
      #S4c fallbacks ≤ n_E(2n − 1)(J + 1) + J,    J := #non-tame transitions of the phase,
  where n_E = #Even vertices.
  - So the predecessor's carries per phase (W-lowerings, by WM), and with them (C), are at most n_E(2n − 1)(J + 1) + J.
  - This settles NEXT item 4 ("carries per level"): inside a tame block of level M there are at most n_E fallbacks (M ≥ 0), or at most
    n_E(n − 1) (M = −1). The counter digit is the β-potential of §4.
- PROVED on 𝒞^1O (§5), on what a non-tame transition is:
  - **J1**: it is an exit jump: σ̄(o) changes, and lev(Ξ_k(σ̄_k o), Ξ_k(σ̄_{k+1} o)) > M_k.
  - **OFF**: every vertex whose new play avoids o keeps COARSE_{M_k}(Ξ).
  - **CAP**: every exit coarse-equal to the old argmin exit is captured into R_{k+1}.
- FALSE (§6): CONJECTURE (JUMP-EQ) of box 6.
  - Instance: x31_rx32 (L-RED, experiments/red/xing/instances, sha1 4fe9ec0e), transition 53 → 54. Re-verified: n5.py 55 iterations /
    3 fallbacks; Oink zlk OK, strategies verified.
  - (JUMP-EQ) is no longer needed: Theorem FB replaces the box 6 reduction.
- PROVED / DATA for NEXT item 3 (A), §6: a tame carry changes Ξ only at levels ≤ M_k, and the box 5 leaver carry level L satisfies
  L ≤ M_k. DATA: L = M_k at 201 of 201 in-phase evicting fallbacks.
- OPEN: J per phase. DATA: J ≤ 3 in every one of the 213 phases of the 53 instances, while INRs (NC failures) reach 26 per phase.
  So with Theorem FB, (C) is now reduced to the exit jumps above the gate level.

## 1. Setting and elementary facts
- Ranks: rank(v) ∈ {0, …, n − 1}, by (priority, index) (experiments/si/si.py). V_{>L} := vertices of rank > L.
- A valuation is x = (c, P, ℓ): cycle node c; path set P ⊆ V_{>rank c}; length ℓ. These are VJ00's Θ-values, with the path set stored
  modulo c as in si.py.
- ⊴ compares, in order:
  1. reward(c);
  2. P (the top differing rank decides by its parity);
  3. ℓ (by c's parity).
- u ⊕ x := (c, P ∪ ({u} if rank u > rank c), ℓ + 1).
- lev(x, y): ∞ if the cycle nodes differ; else the top rank of P(x) Δ P(y); else −1 if only the lengths differ; ⊥ if x = y.
  (Scripts: 99 for ∞, −2 for ⊥.)
- COARSE_L(x) := (c, P ∩ V_{>L}) for −1 ≤ L < ∞. COARSE_∞ is constant. COARSE_⊥(x) := x.
  - ⊴_L compares COARSE_L-values by steps 1-2 above, applied to P ∩ V_{>L}.
- Elementary facts (proofs are one line each):
  - (C1) x ⊴ y ⇒ COARSE_L x ⊴_L COARSE_L y. If the top difference lies above L, the coarse comparison sees the same top difference.
    Otherwise the coarse values are equal.
  - (C2) COARSE_L x = COARSE_L y ⟺ lev(x, y) ≤ L.
  - (C3) ⊴_L is antisymmetric on coarse values: the signed weight Σ ±2^rank is injective on sets.
  - (C4) COARSE_L(u ⊕ x) is a function of u and COARSE_L(x).
- Sources opened by me: Vöge-Jurdziński, BRICS RS-00-48, pdf sha256 485a12de… (the file R15 cites; fetched from brics.dk 21:35Z).
  - **Lemma 5.2** (p. 15) with the definition of Prog (p. 14): Θ_{στ} is the unique valuation with, for every edge (v, w) of the
    (σ, τ)-graph:
    - (P1) Λ(v) = Λ(w);
    - (P2) if Λ(v) ≠ v then Ξ(v) = v ⊕ Ξ(w);
    - (P3) if Λ(v) = v then Ξ(v) = (v, ∅, 0).
    The cycle node of v's play is the top (largest rank) vertex of its cycle (p. 15, "max≤(C) = ℓ").
  - **(11)** (p. 16): Ω_σ = Θ_{σσ̄}, and Θ_{σσ̄} ⊴ Θ_{στ} for every Odd strategy τ ("σ̄ is a best counter-strategy").
  - **Definition of σ̄** (p. 14): σ̄(v) minimises Ω_σ over succ(v).
- Signed results used:
  - R15 (a): Ξ_k ⊴ Ξ_{k+1}.
  - R15 (d): every N5 step for Even is Switch_I with I ⊆ Iσ_k. So σ_{k+1}(v) ∈ {σ_k(v)} ∪ Iσ_k(v) for every v, in S4a and in S4c.
- Notation:
  - Ξ_k = Θ_{σ_k σ̄_k}; λ_k(v) is the cycle node of Ξ_k(v).
  - H_k = the (σ_k, σ̄_k)-graph. Each vertex has exactly one successor in it.
  - Gate edge at k: (y, z) ∈ Iσ_k. Its level is lev(Ξ_k(σ_k y), Ξ_k(z)).
  - **M_k** := the max gate level at k (⊥ if Iσ_k = ∅).
  - A transition k → k+1 is **TAME** if COARSE_{M_k}(Ξ_{k+1}) = COARSE_{M_k}(Ξ_k) pointwise.

## 2. Lemma COARSE-SI (PROVED, L-SI succ. 3): box 6 Step 1 in full
**Telescoping claim (T).** Let L < ∞, and let H′ be a functional graph on V (one successor per vertex) such that every vertex p
satisfies
    COARSE_L(Ξ_k(succ_{H′} p)) = COARSE_L(Ξ_k(succ_{H_k} p)),   (E)
and every cycle of H′ has its top vertex t with λ_k(t) = t (call this (NC) for H′). Then COARSE_L(Θ_{H′}) = COARSE_L(Ξ_k) pointwise. Here
Θ_{H′}(v) is the VJ00 play value of v's H′-play.
Proof.
- Fix v. Let p_0 = v, p_{i+1} = succ_{H′}(p_i), and c := λ_k(v).
- (i) λ_k(p_i) = c for every i.
  - By (P1) on the H_k-edge (p_i, succ_{H_k} p_i): λ_k(p_i) = λ_k(succ_{H_k} p_i).
  - By (E) and L < ∞, the cycle nodes of Ξ_k(succ_{H_k} p_i) and Ξ_k(p_{i+1}) agree. Induction on i.
- (ii) The H′-play from v ends on a cycle C′. Its top t is on the play, so λ_k(t) = c by (i), and λ_k(t) = t by (NC). So t = c.
  - Let s be the first index with p_s = c.
  - The VJ00 play value is then Θ_{H′}(v) = p_0 ⊕ p_1 ⊕ … ⊕ p_{s−1} ⊕ (c, ∅, 0): cycle node = top of the cycle, path = the prefix
    before the first visit of c.
- (iii) For i < s, p_i ≠ c = λ_k(p_i), so p_i is not a cycle node of H_k.
  - (P2) gives Ξ_k(p_i) = p_i ⊕ Ξ_k(succ_{H_k} p_i).
  - By (C4) and (E): COARSE_L(Ξ_k(p_i)) = COARSE_L(p_i ⊕ Ξ_k(p_{i+1})).
  - (P3) gives Ξ_k(p_s) = Ξ_k(c) = (c, ∅, 0).
  - Downward induction from s with (C4): COARSE_L(Ξ_k(p_i)) = COARSE_L(p_i ⊕ … ⊕ p_{s−1} ⊕ (c, ∅, 0)) = COARSE_L(Θ_{H′}(p_i)).
    At i = 0 this is the claim. □

**(a) General form.** Let L < ∞, and let every gate edge at k used by σ_{k+1} have level ≤ L (in particular L = M_k). Let
H′ := the (σ_{k+1}, σ̄_k)-graph. If (NC) holds for H′, then COARSE_L(Ξ_{k+1}) = COARSE_L(Ξ_k).
Proof.
- H′ and H_k differ only at Even vertices that switch.
- A switched y uses a gate edge (R15 (d)) of level ≤ L, so (E) holds there by (C2). (E) is trivial elsewhere.
- By (T), COARSE_L(V) = COARSE_L(Ξ_k), where V := Θ_{σ_{k+1}σ̄_k}.
- Ξ_k ⊴ Ξ_{k+1} (R15 (a)) ⊴ V (VJ00 (11) for σ_{k+1} against the Odd strategy σ̄_k).
- (C1) and (C3) give COARSE_L(Ξ_k) = COARSE_L(Ξ_{k+1}). □

**Converse (exactness of (NC); PROVED).** If L < ∞ and (NC) fails for H′, then COARSE_L(V) ≠ COARSE_L(Ξ_k).
- Let t be the top of a bad cycle. V(t) has cycle node t, and Ξ_k(t) has cycle node λ_k(t) ≠ t.
- So (NC) is exactly the condition under which the L-coarse super-solution step goes through. Ξ_{k+1} itself can still agree,
  because Odd's new best reply may avoid the bad cycle; §2 (b) handles that case.

**(b) In-phase form, Lemma TAME.** Suppose λ_{k+1} = λ_k (true inside a phase), and every Odd vertex u has
lev(Ξ_k(σ̄_k u), Ξ_k(σ̄_{k+1} u)) ≤ M_k. Then k → k+1 is tame.
Proof.
- If M_k = ∞ there is nothing to show. Otherwise take H′′ := H_{k+1} = the (σ_{k+1}, σ̄_{k+1})-graph.
- (E) holds:
  - at switched Even vertices: gate edges of level ≤ M_k (R15 (d), (C2));
  - at Odd vertices: by hypothesis;
  - elsewhere: trivially.
- (NC) holds: a cycle of H_{k+1} with top t has λ_{k+1}(t) = t (VJ00 p. 15), and λ_{k+1} = λ_k.
- (T) gives COARSE_{M_k}(Θ_{H_{k+1}}) = COARSE_{M_k}(Ξ_k), and Θ_{H_{k+1}} = Ξ_{k+1}. □
- Note: this form does not use VJ00 (11) or R15 (a).

DATA (experiments/si/coarse/mono.py; runs asserted equal to n5.run):
- named set: 53 instances = the 30 named in-class ones (P-N5-Z fixes §1), the 12 zcl_*/ccl_*/nofe instances, and L-RED's x32_*,
  u1t_*, obr_*;
- 2,011 transitions in total; (NC) holds at 1,606 of them.
- (a): 0 violations. Converse: 0 violations. The same on 2 × 1,500 random games (seeds 701, 702; n 4-14; 3,379 transitions).

## 3. Lemma MONO and Lemma NOINF (PROVED, L-SI succ. 3)
**MONO.** If k → k+1 is tame, then every gate edge at k+1 has level ≤ M_k; that is, M_{k+1} ≤ M_k.
- This is box 6's Step 2 (PROVED by L-SI succ. 2) with L = M_k. Tameness is exactly its hypothesis. Restated proof:
  - Let (y, z) be a gate edge at k+1 and u := σ_{k+1}(y). Then COARSE_M(Ξ_k(u)) = COARSE_M(Ξ_k(σ_k y)), by (C2) and R15 (d).
  - If COARSE_M(Ξ_k(z)) ▷_M COARSE_M(Ξ_k(u)), then (y, z) is a gate edge at k of level > M_k. That is impossible, so
    COARSE_M(Ξ_k z) ⊴_M COARSE_M(Ξ_k u).
  - Both values are unchanged at k+1 (tame), so COARSE_M(Ξ_{k+1} z) ⊴_M COARSE_M(Ξ_{k+1} u).
  - Ξ_{k+1}(z) ▷ Ξ_{k+1}(u) and (C1) give ⊵_M. So the two are equal, and (C2) gives level ≤ M_k. □
- With §2 (a): M is non-increasing along every run of transitions at which (NC) holds.

**NOINF.** If λ_{k+1} = λ_k and y switches at k → k+1 to z, then lev(Ξ_k(σ_k y), Ξ_k(z)) < ∞.
Proof. Suppose λ_k(z) ≠ λ_k(σ_k y).
- If y is not a cycle node at k+1: (P1) on (y, z) at k+1 gives λ_{k+1}(y) = λ_{k+1}(z) = λ_k(z).
  - If y is not a cycle node at k either, (P1) at k gives λ_k(y) = λ_k(σ_k y) ≠ λ_k(z).
  - If y is a cycle node at k, then λ_k(y) = y = λ_{k+1}(y) makes y a cycle node at k+1, which this case excludes.
  - Either way λ changes.
- If y is a cycle node at k+1: λ_{k+1}(y) = y, so y is a cycle node at k too. Then (P1) on (y, σ_k y) at k gives λ_k(σ_k y) = y.
  (P1) on (y, z) at k+1 gives λ_{k+1}(z) = y, while λ_{k+1}(z) = λ_k(z) ≠ y. Contradiction. □
- Consequence. In an in-phase S4c fallback every vertex with a gate edge switches (n5.py), so the fallback has M_k < ∞.

DATA:
- MONO: 0 violations at the 1,606 NC transitions of the named set and at the 2,467 NC transitions of the random set. M rose 31 times
  (named) and 110 times (random), always at an NC failure.
- Tame form (tame.py): M never rose at a tame in-phase transition (1,830 in-phase transitions).

## 4. Theorem FB (PROVED, L-SI succ. 3): fallbacks per phase
Fix a phase, with transitions k → k+1.
- A **tame run** is a maximal run of consecutive tame transitions. A **block** is a maximal sub-run on which M_k is constant.
- For a block of level M and an Even vertex y, put β_k(y) := COARSE_{M−1}(Ξ_k(σ_k y)), with COARSE_{−2} := the full value (for M = −1).
**Theorem FB.** #S4c fallback transitions of the phase ≤ n_E(2n − 1)(J + 1) + J, where J = #non-tame transitions of the phase.
Proof.
- Step 1. Along a block, β(y) is non-decreasing and COARSE_M(Ξ(σ y)) is constant. Take a transition i → i+1 of the block.
  - σ_{i+1}(y) is σ_i(y) or a gate target at i, so Ξ_i(σ_{i+1} y) ⊵ Ξ_i(σ_i y), at level ≤ M (R15 (d), (C2)).
  - Ξ_{i+1}(σ_{i+1} y) ⊵ Ξ_i(σ_{i+1} y) (R15 (a)), at level ≤ M (tame).
  - Apply (C1) and (C2).
- Step 2. At a fallback i of a block of level M, some y has β_{i+1}(y) ▷ β_i(y).
  - M < ∞ (NOINF), and M ≠ ⊥ since Iσ_i ≠ ∅: an in-phase fallback is Even's, because an Odd fallback changes τ (FBL-N (i)).
  - Take y with a gate edge of level M. S4c switches y to its best gate target z*, best by (Ξ_i-key, index).
  - The level of (y, z*) is exactly M:
    - it is ≤ M by the definition of M;
    - for M ≥ 0 it is ≥ M. Let z be a level-M target. Then COARSE_{M−1}(Ξ_i z) ▷ COARSE_{M−1}(Ξ_i σ_i y) by (C1), (C2) and
      strictness. If lev(Ξ_i σ_i y, Ξ_i z*) < M, then COARSE_{M−1}(Ξ_i z*) = COARSE_{M−1}(Ξ_i σ_i y) ◁ COARSE_{M−1}(Ξ_i z),
      against z* ⊵ z and (C1).
  - So β_i(y) ◁ COARSE_{M−1}(Ξ_i z*) ⊴ COARSE_{M−1}(Ξ_{i+1} z*) = β_{i+1}(y), by R15 (a) and (C1).
- Step 3. Counting. Along a block, COARSE_M(Ξ(σ y)) is constant, so β(y) moves in a chain:
  - M ≥ 0: P ∩ V_{>M−1} is P ∩ V_{>M} plus or minus the single rank-M vertex, so β(y) takes at most 2 values and strictly increases
    at most once;
  - M = −1: only the length moves, inside {0, …, n − 1}, so β(y) strictly increases at most n − 1 times.
  - By Step 2, distinct fallbacks of the block use distinct increases. So a block has ≤ n_E fallbacks (M ≥ 0) or ≤ n_E(n − 1)
    (M = −1).
- Step 4. In a tame run M is non-increasing (MONO), so it has at most one block per value in {∞, n − 1, …, 0, −1, ⊥}.
  - Blocks of level ∞ or ⊥ contain no fallback (Step 2).
  - So a tame run has ≤ n·n_E + (n − 1)n_E = n_E(2n − 1) fallbacks.
  - There are ≤ J + 1 tame runs, and the J non-tame transitions add at most J more. □
**Corollary (PROVED, from FB and WM, P-N5-Z §8; R23).** Inside a phase:
- #W-lowering transitions ≤ n_E(2n − 1)(J + 1) + J;
- (C) (the '+−' reversals at fallbacks) is at most that too.
Hence (C) is polynomial in every phase with J ≤ poly(n). NEXT item 4 ("carries per level", the refill half of the counter) is Step 3:
it is not a θ-change count but a one-flip-per-vertex count on the first digit below the frozen part.

DATA (experiments/si/coarse/fbcount.py, all four of (i) β monotone, (ii) a strict increase at each fallback, (iii) M < ∞ at in-phase
fallbacks, (iv) the per-block bound):
- named set: 213 phases, 1,830 in-phase transitions, 207 in-phase fallbacks, 224 NC-blocks; 0 violations.
  - Max fallbacks in one block: 25, in ccl_w48_n48, n 48. That is under n_E.
- random 2 × 1,500 games (seeds 711, 712): 0 violations.
- random o-cyclic 𝒞^1O, 2 × 2,500 draws with random starts (seeds 721, 722, box 25 generator; 4,285 games): 0 violations; these are
  small (≤ 1 fallback per phase).
- Tame blocks (tame.py): max 25 fallbacks per tame block. M rose 0 times at tame transitions.

## 5. What a non-tame transition is, on 𝒞^1O (PROVED, L-SI succ. 3)
Inside a phase on 𝒞^1O, let k → k+1 be non-tame, with a := σ̄_k(o) and b := σ̄_{k+1}(o).
- **J1.** b ≠ a and lev(Ξ_k(a), Ξ_k(b)) > M_k. (So M_k < ∞.)
  - Every Odd vertex other than o has a single successor, so σ̄ can differ only at o.
  - If (J1) failed, Lemma TAME would make the transition tame. □
- **OFF.** If v ≠ o and v's (σ_{k+1}, τ)-play avoids o, i.e. v ∉ R̄_{k+1}, then COARSE_{M_k}(Ξ_{k+1}(v)) = COARSE_{M_k}(Ξ_k(v)).
  This holds at every in-phase transition, tame or not.
  - The H_{k+1}-play from v avoids o, so along it (E) holds: Even edges by R15 (d), and Odd vertices other than o are forced.
  - Its cycle avoids o, and its top t has λ_k(t) = λ_{k+1}(t) = t.
  - Run (T) on that play alone; the proof of (T) only uses the edges of v's play. □
- **CAP.** Every exit e ∈ succ(o) with lev(Ξ_k(a), Ξ_k(e)) ≤ M_k lies in R̄_{k+1}.
  - [Superseded: this step used "b minimises Ξ_{k+1} over succ(o)", which fails for SPEC's σ̄ at cycle nodes (REFEREE CAP-1).
    The repaired, case-free proof is in docs/si/P-N5-FB-fixes-box7.md, CAP-1.]
  - Ξ_{k+1}(e) ⊵ Ξ_{k+1}(b) (b minimises Ξ_{k+1} over succ(o); VJ00 p. 14) ⊵ Ξ_k(b) (R15 (a)).
  - By J1 and a's minimality, COARSE_{M}(Ξ_k b) ▷_M COARSE_M(Ξ_k a) = COARSE_M(Ξ_k e).
  - So COARSE_M(Ξ(e)) changes at k → k+1, and OFF puts e in R̄_{k+1}. □
- Consequences:
  - (a) Non-tame ⇒ (NC) fails for (σ_{k+1}, σ̄_k), by §2 (a). So a non-tame transition is an INR: the argmin exit a is captured, its
    new play returns to o.
  - (b) Most INRs are tame: 323 NC failures but only J = 23 non-tame transitions in the named set's phases. cycelim_cex_n32 and
    inr2_n32 have 11 INRs each and J = 0. That is why Theorem FB is stated with J and not with #INRs.
  - READING: J counts the times the whole bottom coarse class of exits, at the current gate level, gets captured at once.
DATA (experiments/si/coarse/jump.py, named set):
- J1 23/23. OFF: 40,704 vertex checks, 0 violations. CAP: 159 exit checks, 0 violations.
- In 23/23 non-tame transitions θ itself changes at a level > M_k (tame.py). 10/23 land in θ = w.

## 6. The predecessor's NEXT items 2 and 3
**Item 2: (JUMP-EQ) is FALSE (DATA, re-verified instance).**
- Statement (box 6 §6.2): inside a phase with w constant, if an INR at k → k+1 raises θ at a level above the level L of the most recent
  carry, then θ_{k+1} = w.
- Counterexample: experiments/red/xing/instances/x31_rx32.pg (L-RED), sha1 4fe9ec0e, 𝒞^1O with o = 0.
  - Re-verified with experiments/si/xing/reverify.sh: n5.py 55 iterations / 3 fallbacks; zielonka (Oink zlk) OK, strategies verified.
  - The transition is 53 → 54, w constant since the last carry (L = 24). σ̄(o) goes 24 → 31; this is an NC failure, i.e. an INR.
  - θ rises at level 25 > L. The state reached has (h), and θ_54 ≠ w_54.
  - Keys, as (reward, signed weight, ±length): θ_54 = (36, −2113929216, −4), w = (36, −1040187392, −4).
  - At 54 → 55 θ jumps again, to w (σ̄(o) = 9 = τ(o)). This is the "one post-carry THR jump" box 6 flagged.
- Over the named set, 10 transitions meet the hypothesis; 9 land in θ = w (jumpeq.py).
- In all 10, no evicting fallback follows at the same w. That weaker form is CONJECTURE (JUMP-NC), and Theorem FB does not need it.
- Theorem FB supersedes the box 6 reduction "(CL) ⟸ Step 1 + A + (JUMP-EQ)": it bounds the carries without ordering their levels.

**Item 3: A.**
- PROVED: at a tame carry, every Ξ(v) changes only at levels ≤ M_k (that is what "tame" means). The box 5 leaver carry level
  L := max over active leavers y of lev(Ξ_k y, Ξ_{k+1} y) is therefore ≤ M_k.
- DATA (jump.py): L = M_k at 201 of 201 in-phase evicting fallbacks of the named set. With that equality A reads "a carry changes Ξ
  only at levels ≤ its own level".
- READING for L ≥ M_k: a leaver y with a level-M gate edge, not a cycle node and of rank ≠ M, changes exactly at level M:
  - Ξ_k(y) = y ⊕ Ξ_k(σ_k y) and Ξ_{k+1}(y) = y ⊕ Ξ_{k+1}(z*), and these differ in COARSE_{M−1} by (C4) and Step 2 of §4.
  - What is not shown: that a level-M gate edge at an evicting fallback always has a leaver tail. FBL (R20 (b), u* ≠ none) leaves only
    R→F edges, flat cycle-node switches, and possibly cycle-closing F→F edges.
- (CL) in its M-form is MONO plus FB. Its leaver form follows from MONO wherever L = M_k at carries and no non-tame transition
  intervenes.

## 7. Where (C) stands now, and the open core
- Chain (each link labelled):
  - (C) ≤ #fallbacks per phase ≤ n_E(2n − 1)(J + 1) + J (PROVED, §4).
  - Each non-tame transition is an exit jump above M_k that captures the whole bottom coarse class of exits (PROVED, §5).
- OPEN: (J-poly) J ≤ poly(n) per phase.
  - DATA: J ≤ 3 per phase on all 213 phases of the named set, including every L-RED climb file on disk. Climbs so far targeted X,
    Z, carries or INRs, never J.
  - The obvious potential fails. θ rises at every non-tame transition at a level > M_k, but M_k can be small, and θ ⊴ w leaves an
    exponential range below w. A proof must use CAP: every non-tame transition captures a coarse class of exits that includes the
    argmin. Under H1 at k that argmin is ∉ R_k, so each non-tame transition is an entry of a whole exit class.
    - Proposed route (READING): bound the re-releases of captured exits. An exit that is σ̄(o) again at a later non-tame transition has
      left R in between, and leaves inside a tame run are fallback evictions (≤ n_E(2n − 1) per run, §4) or arena leaves.
- Outside idea used (D18), READING:
  - COARSE_L is a truncation map onto a quotient of the VJ00 closed semiring (VJ00 Remark, pp. 13-14: (M(V) × N, ⊕, max) is a closed
    semiring), in the way an ultrametric value group is truncated at a radius.
  - (T) says Ξ_k is a super-solution (Bellman fixed point) of the truncated one-player problem whenever the gate levels lie inside
    the radius.
  - β is the leading digit just below the radius. Theorem FB is the binary-counter amortization done one digit at a time: inside a
    freeze each digit flips at most once per vertex.
  - The multiplicative obstruction of box 3 does not appear here, because the frozen radius M can only shrink between non-tame
    transitions (MONO). Each tame run pays for its digits once.

## 8. Files
- experiments/si/coarse/mono.py: COARSE-SI (a) + converse, MONO.
- experiments/si/coarse/fbcount.py: Theorem FB (i)-(iv). Modes: named / --random / --c1o.
- experiments/si/coarse/tame.py: tame refinement, J, J_eq, M at tame transitions.
- experiments/si/coarse/jump.py: J1, OFF, CAP, L vs M.
- experiments/si/coarse/jumpeq.py: (JUMP-EQ) exactly as stated in box 6.
- Every script asserts its run against experiments/new/n5.py run() (iterations and fallbacks). §5 asserts exactly one Odd choice vertex.

## 9. Toward (J-poly): the exit potential D (𝒞^1O; PROVED parts by L-SI succ. 3, unrefereed)
Setting:
- ω := τ(o), the trusted exit, constant in a phase.
- At a state with H2, D_k := {e ∈ succ(o) ∖ R̄_k : Ξ_k(e) ◁ Ξ_k(ω)}: the free exits strictly below the trusted one.
- SCOPE: an in-phase transition k → k+1 is in scope if (h) holds at k, H2 holds at k+1, and w_{k+1} = w_k.
- J_in := #non-tame transitions in scope; J_out := the rest.

Preliminaries (PROVED; P-N5-Z §0 conventions, Lemma G = R19 (a)):
- Under H2, ω ∉ R̄_k, so Ξ_k(ω) = W_k(ω) (G (a)), and w_k = o ⊕ W_k(ω) by (P2) in the (σ_k, τ)-graph.
- So "w constant" gives W_{k+1}(ω) = W_k(ω). (F-pre applies: o lies on neither path.)
- Under H1, a := σ̄_k(o) ∉ R̄_k. a's honest play avoids o, and on 𝒞^1O whether a play reaches o does not depend on Odd's choices before
  o.

Lemmas:
- **MIN.** (PROVED; added 22:5xZ after REFEREE item CAP-1. SPEC's σ̄ is not a minimiser at cycle nodes.) If H1 holds at k, then
  λ_k(o) = c ≠ o, and a = σ̄_k(o) satisfies the following.
  - (i) Ξ_k(a) ⊴ Ξ_k(e) for every exit e ∉ R̄_k.
    - Let τ′ := σ̄_k[o → e]. The τ′-play from o is o, then e's H_k-play, which avoids o. So Θ_{σ_k τ′}(o) = o ⊕ Ξ_k(e).
    - (11) gives o ⊕ Ξ_k(a) = Ξ_k(o) ⊴ o ⊕ Ξ_k(e). Apply (F-pre): o lies on neither path and is neither cycle node.
  - (ii) Ξ_k(a) ◁ Ξ_k(e) for every exit e ∈ R_k.
    - The τ′-play from o is the cycle C = (o, π_e), with top t. c ∉ C, so (11) gives reward(t) > reward(c).
    - Case rank t > rank c: t is odd ⇒ reward(c) < reward(t) < 0 ⇒ c is odd and of higher rank. Impossible, so t is even, and
      L := (π_e, o) has an even top above c.
    - Case rank t < rank c: c even ⇒ reward(c) > reward(t). Impossible, so c is odd, and L has no vertex above c (longer is better
      for Even at an odd c).
    - Either way L ⊕ x ▷ x for x with cycle node c and L ∩ P(x) = ∅. So Ξ_k(e) = π_e ⊕ o ⊕ Ξ_k(a) = L ⊕ Ξ_k(a) ▷ Ξ_k(a), by (P2)
      along the route.
- **D1′.** If k → k+1 is non-tame and in scope, then a ∈ D_k.
  - ω is not captured (H2 at k+1), so CAP gives lev(Ξ_k a, Ξ_k ω) > M_k ≥ −1.
  - With (MIN) below this gives Ξ_k(a) ◁ Ξ_k(ω). And a ∉ R̄_k.
- **D2.** In scope, D_{k+1} ⊆ D_k ∪ Rel_k, where Rel_k := the exits in R_k ∖ R̄_{k+1} (exits RELEASED at k → k+1).
  - Take e ∈ D_{k+1} with e ∉ R̄_k. Then Ξ_k(e) ⊴ Ξ_{k+1}(e) (R15 (a)) ◁ Ξ_{k+1}(ω) = W_{k+1}(ω) = W_k(ω) = Ξ_k(ω).
- **D3.** At a non-tame transition, a ∉ D_{k+1}: a ∈ R̄_{k+1} by CAP.
- **NOREL-A.** In scope, an S4a (arena) transition releases no exit into D: Rel_k ∩ D_{k+1} = ∅.
  - Let e ∈ R_k be an exit and c the common cycle node (H3). By G (b), Ξ_k(e) = π_e ⊕ θ_k = L ⊕ Ξ_k(a), where L := π_e followed by o.
    L is disjoint from P(Ξ_k a) and from P(W_k ω): both plays avoid R̄_k.
  - Whether L ⊕ x ▷ x or L ⊕ x ◁ x, for x with cycle node c and L disjoint from P(x), depends only on L and c:
    - on the parity of the top vertex of L above rank c;
    - if L has no vertex above rank c, on c's parity (the length grows by |L|).
    Never equality.
  - (MIN) gives Ξ_k(a) ◁ L ⊕ Ξ_k(a). Hence W_k(ω) ◁ L ⊕ W_k(ω) = π_e ⊕ w_k = W_k(e) (G (b)).
  - At an arena step, WM gives W_{k+1}(e) ⊵ W_k(e) ▷ W_k(ω) = Ξ_{k+1}(ω).
  - If e ∉ R̄_{k+1}, then Ξ_{k+1}(e) = W_{k+1}(e) (G (a)), so e ∉ D_{k+1}. □
- **Corollary JD.** On a maximal run S of in-scope transitions,
      J_in(S) ≤ |succ(o)| + Σ_{fallbacks k ∈ S} |Rel_k ∩ D_{k+1}|.
  - Each non-tame transition removes its argmin a from D (D1′, D3).
  - D gains only released exits (D2), and only at fallbacks (NOREL-A).
- READING: this does not close (J-poly). Fallbacks per tame run are ≤ n_E(2n − 1) (FB), so JD and FB together give only the circular
  pair J ≤ d + d·#fb and #fb ≤ C(J + 1).
  - What would close it: a statement that most fallback releases cannot feed a non-tame capture.
  - The naive form is FALSE (DATA): (REL-NJ) "an exit released into D at a fallback is never the argmin of a later non-tame transition
    in the same scope run". It fails at 4 of 18 in-scope non-tame transitions: lev_l_sc k 34 (exit 8), x31_cu32 k 28 (exit 8),
    x31_cu32i k 36 (exit 3) and k 38 (exit 6).
  - Own probe, never stated as a lemma.
DATA (experiments/si/coarse/dpot.py, named set):
- D1 at THR states: 1,476/0. D1′: 18/0. D2: 1,708/0. D3: 18/0.
- Releases into D: 199 at fallbacks, 0 at arena steps (NOREL-A).
- J_in = 18. J_out = 5: 3 at OTHER states of zcl_cu_n48, and 2 at w-changes (x31_rx48 k 50, zcl_rx_n32 k 64).
- max |D| = 22 (run_m_inr2, n 32).
Jump levels under (h) with w constant (scratch classification, 20 cases):
- θ jumps exactly at rank(u*) in 18 of 20. So u* drops strictly, or θ reaches w, and there are at most n such jumps per w-value.
- The 2 others (x31_rx32 k 53, x32_nest40 k 55) jump below u* and are followed at once by a jump at u*.
- CONJECTURE (JU2): under (h) with w constant, a non-tame jump below rank(u*) is followed within one transition by a jump at rank(u*).
  Data 2/2, too thin to lean on.

## 10. J-climbs (DATA, after the packet; experiments/si/coarse/jclimb.py)
Fitness: (max J in one phase, total J, in-phase fallbacks). 4 climbs × 30 min, 22:0xZ-22:25Z. Bests are pinned in
experiments/si/coarse/instances/. Each was re-verified with experiments/si/xing/reverify.sh (n5.py; zielonka (Oink zlk) OK;
strategies verified) and is one-Odd-choice.

| best (seed) | n | sha1 | n5 it/fb | max J / phase | J_in / J_out (dpot.py) | in-phase fallbacks | releases into D |
| --- | --- | --- | --- | --- | --- | --- | --- |
| jcl_zcl_cu_n48 (zcl_cu_n48) | 48 | 53c69d2d | 23/1 | 17 | 3 / 14 | 0 | 0 |
| jcl_x31_cu32i (x31_cu32i) | 32 | 00e09994 | 16/1 | 12 | 12 / 0 | 0 | 0 |
| jcl_lev_l_sc (lev_l_sc) | 32 | e5b430b2 | 23/9 | 7 | 4 / 3 | 9 | 0 |
| jcl_x32_nest40 (x32_nest40) | 40 | fdb30eed | 36/23 | 5 | 1 / 4 | 21 | 0 |

- |succ(o)| on the four bests: 18, 14, 9, 6 (row order). So J_in ≤ |succ(o)| everywhere, as Corollary JD gives with 0 releases.
  jcl_x31_cu32i comes close: J_in 12 against |succ(o)| = 14.
- On the four bests together: J_in 20, J_out 21, releases into D 0. Every lemma check passed with 0 violations:
  - COARSE-SI (a) and its converse, MONO;
  - FB (i)-(iv);
  - J1 41/41; OFF 1,904; CAP 246; L = M at 30/30 carries;
  - D1-D3, D2.
- So J grows in the climbs in two ways:
  - runs of consecutive exit jumps with no release between them (≤ |succ(o)| per scope run, Corollary JD);
  - jumps at states where H2 fails. There ω itself is captured, so the D-argument does not apply. These are OTHER-touching
    transitions, counted by R21's O, which is open separately as (NH').
- READING: none of the climbs produced a jump paid by a release. The second climb round targets exactly that (JMODE=REL).

### Reversal split (DATA, scratch script, named set)
- '−' reversals: 62 at fallbacks, now bounded by FB, and 15 at arena steps.
- '±' reversals: 30, all at arena steps.
- '+' reversals: 80 at arena steps, 7 of them non-tame.
- Max per phase: fb− 8, ar− 6, ar± 9.
- So the rest of (Z), beyond (C), is the arena-step leaves and the '±' transitions (OPEN; next box).

## 11. (JU2) is FALSE; the open core restated
- (JU2) (§9) FALSE (DATA, re-verified pinned instance).
  - Instance: jcl_x31_cu32i (experiments/si/coarse/instances, sha1 00e09994; n5 16/1; Oink zlk OK; strategies verified; one o).
  - w constant with rank(u*) = 30 at states 5-8. θ jumps at levels 27, 22, 21, then 30; σ̄(o) goes 22 → 29 → 13 → 21 → 5.
  - Over the named set, the J-bests and the REL-climb snapshots (experiments/si/coarse/ju2.py): 60 in-scope jumps; 40 at rank(u*),
    20 below it; (JU2) holds at 10 of the 20.
  - No jump lies above rank(u*). That is PROVED: θ_k ◁ θ_{k+1} ⊴ w (R21 (a) XW) and Lemma U (ii) (L-SI succ. 1).
- So the sub-u* jumps run like a counter over Odd's exits. The u*-route does not bound J_in by itself.
- What remains is exactly what Corollary JD leaves open: jumps whose argmin was put back into D by a fallback release (REL).

## 12. Jumps paid by releases (DATA; REL climbs, fitness = #in-scope non-tame jumps whose argmin was released at an earlier fallback)
4 climbs × 30 min, 22:3xZ-23:03Z. Bests pinned in experiments/si/coarse/instances/rel_*. Each re-verified with reverify.sh (n5.py;
zielonka (Oink zlk) OK; strategies verified) and one-Odd-choice.

| best (seed) | n | sha1 | n5 it/fb | release-paid jumps |
| --- | --- | --- | --- | --- |
| rel_lev_l_sc (lev_l_sc) | 32 | d49ab614 | 19/1 | 12 |
| rel_x31_cu32i (x31_cu32i) | 32 | 7dc35abe | 19/1 | 11 |
| rel_zcl_rx_n32 (zcl_rx_n32) | 32 | 034731ca | 21/3 | 10 |

The fourth climb (seed x31_cu32) stalled at 2.
- Totals on the three: J_in = 33, all 33 release-paid; 76 releases into D from only 5 in-phase fallbacks; max |D| 23; max J per phase 12.
- All lemma checks: 0 violations. That covers COARSE-SI/MONO, FB (i)-(iv), J1, OFF 1,027, CAP 272, D1-D3, NOREL-A (0 arena releases),
  and L = M (5/5).
- READING. One fallback can release a whole bundle of exits into D, and then Odd walks through them, one non-tame jump per exit.
  - So per tame run: fallbacks ≤ n_E(2n − 1) (FB), and each releases ≤ |succ(o)| exits. That is consistent with J_in ≈ |succ(o)|·#fallbacks.
  - What the lemmas do not exclude is the alternation "fallback releases a bundle → Odd walks it → fallback releases again → …".
    FB's budget is per tame run, and every jump starts a new run.
  - A polynomial bound needs a potential that this alternation spends. θ rises at every jump, but only θ ⊴ w is known, which leaves
    an exponential range.
- Growth: J per phase 12 at n 32 here, 17 at n 48 (§10). No superlinear growth seen. Scale climbs at n 48-64 are running (§13).
