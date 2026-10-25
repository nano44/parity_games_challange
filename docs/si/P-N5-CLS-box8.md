# Referee packet P-N5-CLS: gates into F, frozen values, and fallback levels across a scope run (box 8 lemmas)
L-SI successor 3 (Opus 5.5, D18/L40). Written 2026-10-25 02:2xZ (date -u), at the Lead's request (02:13Z).
- Self-contained: definitions, statements, full proofs, the location of every dependency, the data and the scripts that produce it.
- Source text: docs/si/N5-C-box8.md §1, §2, §5, §12 (lane write-up, l-si c47be183). Where they differ, this packet governs.
- Status: L-SI successor 3's proofs, unrefereed. Labels: PROVED (L-SI succ. 3), DATA, FALSE, OPEN.
  - §2 (TRANSFER) holds on every game.
  - §3-§7 are on 𝒞^1O: exactly one Odd vertex o with out-degree > 1; every script asserts it.
- These are lemmas about the candidate N5. They are not a running-time bound, not a TARGET.md claim, and not a step-4 pass.
  G-N5-TIME stays OPEN.
- Statements: §1 elementary facts (C5), (C6) and Lemma CLU; §2 TRANSFER; §3 OFFGATE; §4 CN; §5 Lemma NL; §6 Theorem CLS1.
- §7 is NOT TO SIGN: the refuted OG′ and the open items. §8: data.

## 0. Objects and dependencies (only landed RESULTS)
- N5, S4a, S4c, gates Iσ_k, gate levels, M_k, valuations Ξ_k = Θ_{σ_k σ̄_k}, the graph H_k, levels lev, COARSE_L, (C1)-(C4): as in RESULTS
  R25 (packet P-N5-FB, docs/si/P-N5-FB-box7.md §0-§1, with its fixes files).
  - ⊥ < −1 < 0 < … < n − 1 < ∞ are the level values.
- PHASE: a joint λ-phase with τ constant (R21 setting). Inside a phase λ_{k+1} = λ_k and τ_{k+1} = τ_k.
- On 𝒞^1O, as in R19-R23:
  - θ_k := Ξ_k(o), w_k := W_k(o), W_k := the (σ_k, τ)-valuation;
  - R̄_k := {o} ∪ {v ≠ o : v's (σ_k, τ)-play reaches o}, R_k := R̄_k ∖ {o}, F_k := V ∖ R̄_k;
  - (h) := H1 ∧ H2 ∧ H3. State kinds: THR ((h) and θ ◁ w), EQ (Ξ = W pointwise).
  - Whether a play reaches o does not depend on Odd's choices before o (R23 §0).
- SCOPE RUN: a maximal run of consecutive in-phase transitions k → k+1 with (h) at k, H2 at k+1 and w_{k+1} = w_k.
- r_k := lev(θ_k, w_k). Under (h) the cycle nodes agree (H3), so r_k < ∞.
  - r_k ≥ 0 iff θ_k ◁ w_k with u* ≠ none, and then r_k = rank(u*_k).
  - r_k = −1 iff θ_k ◁ w_k with u* = none. r_k = ⊥ iff θ_k = w_k.
- Signed results used:
  - R15 (a) Ξ_k ⊴ Ξ_{k+1}; R15 (d) σ_{k+1}(v) ∈ {σ_k(v)} ∪ Iσ_k(v).
  - R19 (a) Lemma G: (a) off R̄, Ξ = W (no (h) needed); (b) under (h), on R, Ξ = π ⊕ θ and W = π ⊕ w, with π the route to o.
  - R20 (b) Lemma FBL, strong form for u* ≠ none: "at a throttled S4c fallback state there is no F→R and no R→R gate edge, so the
    fallback switches only leaves (R→F edges), apart from flat cycle-node switches" (R20 puts o in R).
    - A single fallback state with (h) and θ ◁ w is a throttled stretch of length 1.
  - R21 (a) Lemma XW: Ξ_k ⊴ W_k.
  - R23 (f) Lemma GAP: at a fallback inside a phase with (h) at k, every switched y → z with y ∈ R_k, z ∈ F_k satisfies
    Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ W_k(σ_k y).
  - R23 (g) Lemma WM: inside a phase, at every transition that is not an S4c fallback, W_{k+1} ⊵ W_k.
  - R25:
    - claim (T) and its proof step "(T) (iii)";
    - OFF (§5): v ∉ R̄_{k+1} ⇒ COARSE_{M_k}(Ξ_{k+1} v) = COARSE_{M_k}(Ξ_k v);
    - NOINF, with fixes FB-1 = G-FB-1: at an in-phase S4c fallback, M_k < ∞;
    - FB step (2): at an in-phase S4c fallback, M_k is attained by a switched edge (each tail switches to its best target, whose level
      is the max over its gate edges).
  - VJ00 (BRICS RS-00-48, pdf sha256 485a12de…) Lemma 5.2 (p. 15): Ξ_k is the play valuation of H_k; the cycle node of a play is the
    top of its cycle. This is the inherited engine link ENG-1 of R25.

## 1. Elementary facts, and Lemma CLU
- (C5) If a ◁ b ⊴ c then lev(a, b) ≤ lev(a, c).
  - Proof: put L := lev(a, c). If L = ⊥ then a = c and a ◁ b ⊴ a is impossible. Otherwise suppose lev(a, b) > L.
  - Then COARSE_L(b) ≠ COARSE_L(a) = COARSE_L(c) (C2). (C1) with b ▷ a gives COARSE_L(b) ▷_L COARSE_L(c), but b ⊴ c gives ⊴_L.
    Contradiction by (C3). □
- (C6) lev(a, c) ≤ max(lev(a, b), lev(b, c)).
  - Proof: with L := the max, COARSE_L(a) = COARSE_L(b) = COARSE_L(c) (C2). □
- (C7) If π is a vertex sequence disjoint from P(x), P(y) and from both cycle nodes, then lev(π ⊕ x, π ⊕ y) = lev(x, y), and the order
  between π ⊕ x and π ⊕ y is the order between x and y.
  - Proof: the same vertices are added to both path sets, and both lengths grow by |π|. □
- **Fact R (PROVED).** Along a scope run, r is non-increasing.
  - Proof: θ_k ⊴ θ_{k+1} (R15 (a)) and θ_{k+1} ⊴ w_{k+1} = w_k (R21 (a)). If θ_k = θ_{k+1} there is nothing to show.
  - Otherwise (C5) gives lev(θ_k, θ_{k+1}) ≤ r_k, and (C6) gives r_{k+1} ≤ max(lev(θ_{k+1}, θ_k), r_k) = r_k. □
- **Lemma CLU (PROVED; L-SI succ. 2, box 5, restated with its proof).** At an in-phase S4c fallback k with (h) and θ_k ◁ w_k, every
  switched y → z with y ∈ R_k and z ∈ F_k has level ≤ r_k.
  - Proof: GAP (R23 (f)) and Lemma G (b) give π′ ⊕ θ_k ◁ Ξ_k(z) ⊴ π′ ⊕ w_k, with π′ the route of σ_k(y). (C5) and (C7) give
    lev(π′ ⊕ θ_k, Ξ_k z) ≤ lev(π′ ⊕ θ_k, π′ ⊕ w_k) = r_k.
  - (C7) applies. π′ ⊆ R_k (the route stops before o). P(θ_k) and P(w_k) consist of o and vertices of o's honest / W-play after o,
    which avoid R_k (H1, H2). The common cycle node lies outside R̄_k (R23 (c), LOOP proof). □

## 2. Lemma TRANSFER (PROVED; every game)
Let k → k+1 be in-phase, let L < ∞, and let z satisfy COARSE_L(Ξ_{k+1} z) = COARSE_L(Ξ_k z). If (y, z) is a gate at k+1 of level
> L, then (y, z) is a gate at k of level > L.
- Proof: put u := σ_{k+1}(y). Ξ_k(u) ⊵ Ξ_k(σ_k y) (R15 (d)) and Ξ_{k+1}(u) ⊵ Ξ_k(u) (R15 (a)).
- With (C1): COARSE_L(Ξ_k z) = COARSE_L(Ξ_{k+1} z) ▷_L COARSE_L(Ξ_{k+1} u) ⊵_L COARSE_L(Ξ_k σ_k y). The first strict step holds
  because the gate is strict, so (C1) gives ⊵, and the level > L gives ≠ (C2).
- So Ξ_k(z) ▷ Ξ_k(σ_k y) at a level > L, and z ≠ σ_k(y). □

## 3. Lemma OFFGATE (PROVED; 𝒞^1O)
At every in-phase transition k → k+1, tame or not, every gate (y, z) at k+1 with z ∉ R̄_{k+1} has level ≤ M_k.
- Proof. If M_k = ∞ there is nothing to show. If M_k = ⊥, σ and Ξ are unchanged.
- Otherwise OFF (R25) gives COARSE_{M_k}(Ξ_{k+1} z) = COARSE_{M_k}(Ξ_k z). A gate at k+1 of level > M_k would by TRANSFER be a gate at
  k of level > M_k, against the definition of M_k. □
- Remark: only gates INTO R̄_{k+1} can exceed M_k at k+1. The off-R̄ form OG′ is FALSE (§7).

## 4. Lemma CN (PROVED; every game, inside a phase)
If λ_{k+1} = λ_k and y with λ_k(y) = y switches to z at k → k+1, then the gate level of (y, z) at k is −1.
- Proof: λ_{k+1}(y) = y, so y's H_{k+1}-play is a cycle with top y through z = σ_{k+1}(y). z's path to y is an arc of that cycle, so
  all its vertices have rank < rank y, and P(Ξ_{k+1} z) = ∅ (Lemma 5.2).
- λ_k(z) = λ_{k+1}(z) = y. Ξ_k(z) ⊴ Ξ_{k+1}(z) (R15 (a)) has the same cycle node y, so the signed weight of P(Ξ_k z) is ≤ 0.
- σ_k(y) lies on y's H_k-cycle, so P(Ξ_k σ_k y) = ∅. The gate gives weight(P(Ξ_k z)) ≥ 0.
- So P(Ξ_k z) = ∅ (the weight is injective), and the strict gate differs only in length: level −1. □

## 5. Lemma NL (PROVED; 𝒞^1O)
Let j → j+1 be an S4a transition (not an S4c fallback) inside a phase, with (h) at j. Let L < ∞ with r_j > L, and assume
- (A_j) every gate (y, z) at j with z ∈ F_j has level ≤ L.
Then:
- (i) COARSE_L(Ξ_{j+1} v) = COARSE_L(Ξ_j v) for every v ∉ R̄_{j+1};
- (ii) R_j ⊆ R̄_{j+1} (no leave);
- (iii) (A_{j+1}) holds.
Proof.
- Key step (K*). Let q ∈ R_j ∖ R̄_{j+1} satisfy (i). Then:
  - Lemma G (b) at j: Ξ_j(q) = π_q ⊕ θ_j and W_j(q) = π_q ⊕ w_j. By (C7), lev(Ξ_j q, W_j q) = r_j > L and Ξ_j(q) ◁ W_j(q), so
    COARSE_L(Ξ_j q) ◁_L COARSE_L(W_j q).
  - q ∉ R̄_{j+1}, so W_{j+1}(q) = Ξ_{j+1}(q) (Lemma G (a)). WM (R23 (g)) gives W_{j+1}(q) ⊵ W_j(q).
  - With (i) at q: COARSE_L(Ξ_j q) = COARSE_L(Ξ_{j+1} q) = COARSE_L(W_{j+1} q) ⊵_L COARSE_L(W_j q). Contradiction.
  - So no vertex of R_j ∖ R̄_{j+1} satisfies (i).
- (i). Suppose it fails. Take a failing v ∉ R̄_{j+1} whose H_{j+1}-play v = p_0, p_1, … reaches its cycle node c_v = λ_{j+1}(v) in
  the fewest steps.
  - The play avoids o (𝒞^1O), so every Odd vertex on it is forced. Its cycle's top t has λ_j(t) = λ_{j+1}(t) = t (phase).
  - If v = c_v, then Ξ(v) = (v, ∅, 0) at j and at j+1. So v ≠ c_v, and v is not a cycle node of H_j either (λ_j(v) = c_v).
  - p_1 ∉ R̄_{j+1} is nearer to c_v, so it satisfies (i).
  - If v keeps its edge, or switches along a gate of level ≤ L, then (E) holds at v. The step "(T) (iii)" of R25 (with (P2) at j and
    at j+1, and (C4)) gives (i) at v. Contradiction.
  - So v switched to q := p_1 along a gate of level > L. By (A_j), q ∉ F_j. And q ∉ R̄_{j+1}, q ≠ o, so q ∈ R_j ∖ R̄_{j+1} satisfies
    (i), against (K*).
- (ii) follows from (i) and (K*).
- (iii) Let (y, z) be a gate at j+1 with z ∈ F_{j+1}. By (ii) z ∈ F_j, and by (i) COARSE_L(Ξ z) is unchanged. A level > L would by
  TRANSFER give a gate at j of level > L into F_j, against (A_j). □

## 6. Theorem CLS1 (PROVED; 𝒞^1O): fallback levels never rise at THR fallbacks with u* ≠ none
Let S be a scope run, and let k1 be an S4c fallback of S at a THR state with r_{k1} ≥ 0 (u* ≠ none). Then
    M_{k1} ≤ min{M_k : k < k1 an S4c fallback of S}   (vacuous if there is none).
Proof. Induction over the fallbacks of S. Let k0 be the last fallback of S before k1, and suppose (induction) that the claim holds for
every fallback of S before k1 that is THR with u* ≠ none. Two kinds of k0 are possible.
- (α) k0 is THR with u* ≠ none. Then by induction L := M_{k0} is the minimum over the fallbacks up to k0. L < ∞ by NOINF (FB-1).
- (β) k0 is EQ or has u* = none. Then r_{k0} ≤ −1. By Fact R, r_{k1} ≤ r_{k0} ≤ −1, against r_{k1} ≥ 0. So (β) cannot occur. And by
  Fact R, every fallback of S before k1 is THR with u* ≠ none.
Case r_{k1} ≤ L.
- By FBL (R20 (b)), the switched edges at k1 are R → F edges and flat cycle-node switches.
- CLU bounds the former by r_{k1} ≤ L. CN gives −1 for the latter.
- With FB step (2) (R25), M_{k1} ≤ max(r_{k1}, −1) ≤ L. (L ≥ −1, since a fallback has a gate edge.)
Case r_{k1} > L.
- By Fact R, r_j ≥ r_{k1} > L for every state j ∈ [k0, k1], so every such state is THR with u* ≠ none ((h) holds in S). Show (A_j) for
  L at every j ∈ [k0+1, k1]:
  - j = k0 + 1: gates at k0 + 1 into F_{k0+1} = V ∖ R̄_{k0+1} have level ≤ M_{k0} = L (OFFGATE).
  - j → j+1 an S4a transition with j ∈ [k0+1, k1 − 1]: Lemma NL (iii), since r_j > L and (A_j).
  - j → j+1 an S4c fallback with k0 < j < k1: impossible, since k0 is the last fallback before k1.
- At k1, M_{k1} is attained by switched edges (FB step (2)).
  - Switched edges into F_{k1} are gates into F_{k1}, of level ≤ L by (A_{k1}).
  - By FBL there are no switched edges into R̄_{k1} other than flat cycle-node switches (CN: −1).
  - So M_{k1} ≤ L. □
Corollary (PROVED). Along a scope run, the levels of its THR fallbacks with u* ≠ none form a non-increasing sequence. These are all its
fallbacks before the first EQ / u* = none state (Fact R), and every one of its evicting fallbacks with u* ≠ none.

## 7. NOT TO SIGN: refuted forms and open items
- FALSE: OG′ "gates into F at k+1 have level ≤ MF_k := the max level of the gates at k into F_k".
  - Instance: experiments/red/xing/instances/x31_re24.pg (L-RED; sha1 49eaf50e; in R23's re-verified data), transition 1 → 2.
  - MF_1 = −1, while gate (4, 8) at state 2 has level 22. At state 1, 4 and 8 lie in R (the level-22 gate is (8, 14), R → R).
    At 1 → 2, R collapses from 21 vertices to {12} at an arena step.
  - OFFGATE (bound M_k) is the true form.
- OPEN (H-EQ): fallbacks of a scope run at EQ states or with u* = none.
  - Their R → F switched edges have level ≤ r ≤ −1 (CLU; NOFL-E at EQ: none).
  - Their other non-flat switched edges (R → R̄, and F → F with a non-cycle-node tail) are not bounded here.
  - DATA: 4 EQ fallbacks in scope; 0 with u* = none; the only such edge seen had level ≤ −1.
- OPEN: the second half of (CL-S), "≤ n_E fallbacks per level along a scope run".
  - Reduction (lane, box 8 §12): y is a level-M tail at two fallbacks only if COARSE_M(Ξ(σ y)) rose in between. For R-tails that is
    driven by θ-changes above M.
- OPEN: θ-changes per scope run without X (box 8 §13). The recursion T(≥ℓ) ≤ poly·(1 + T(>ℓ)) is multiplicative.
- Consequence for (C) (READING): CLS1 bounds the levels, not yet the number, of evicting fallbacks per scope run.

## 8. Data (DATA, not proof)
- Produced by experiments/si/coarse/run_cls.sh; logs in experiments/si/coarse/logs/cls_*.txt, in this packet's commit.
- Set: experiments/si/coarse/named.txt (53 files) + experiments/si/coarse/instances/*.pg (12 pinned climb bests, each re-verified with
  n5.py, Oink zlk and check_sol2.py). Each is asserted one-Odd-choice.
- Every script re-runs N5 and asserts (iterations, fallbacks) = experiments/new/n5.py run().
- cls2.py:
  - OFFGATE (gates at k+1 into F̄ vs M_k);
  - CN (in-phase cycle-node switches);
  - switched/gate edges into R̄ at in-phase fallbacks with (h);
  - MF monotonicity (OG′).
- rfinv.py:
  - (A) after a fallback in a scope run;
  - FRZ, LV, R-ROUTE;
  - (B1) (no gate above L into a leaver);
  - Lemma AL = NL (ii) (arena leaves after a fallback have r_j ≤ L);
  - fallback kinds.
- clscope.py: (CL-S) both halves (monotone levels; ≤ n_E per level) over scope runs.
- Results in the committed logs (65 files):
  - OFFGATE 6,645 gate checks / 0; CN 7 / 0; gate edges into R̄ at in-phase (h) fallbacks: 1 (EQ), flat;
  - (A) 0 violations; FRZ 25,646 / 0; R-ROUTE 9,319 / 0; LV and (B1) 554 / 0; AL 4 / 0;
  - in-scope fallbacks: 252 THR with u* ≠ none, 4 EQ, 0 with u* = none;
  - (CL-S): 70 scope runs, 256 fallbacks, 0 violations of either half;
  - OG′: 1 violation (x31_re24, 1 → 2), as in §7.
- The lane's earlier runs, which add L-RED's j7_n32 / j7_n48 (box 8 §1-§6), gave proportionally larger counts with the same 0s.
- Adversarial climbs (lane, box 8 §9; 4 × 40 min, ~145k mutation steps, jclimb.py modes CLS2 and RF): 0 violations.
