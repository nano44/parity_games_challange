# Referee packet P-N5-X: N5 inside a joint λ-phase is controlled by crossings and OTHER states (box 28)
L-NEW successor 10 (Opus 5.5, D15/D18). Written 2026-10-24 17:16Z-17:40Z (date -u), at the Lead's request (17:1xZ).
- Self-contained: definitions, statements, full proofs, and the location of every dependency.
- Source text: docs/new/N5-NH-box28.md §1-§5c. This packet is the final form of what a referee needs. Where the two differ,
  this packet governs.
- Status: L-NEW's proofs, unrefereed. These are lemmas about the candidate N5 on 𝒞^1O. They are not a running-time bound, not a
  TARGET.md claim, and not a step-4 pass. G-N5-TIME stays OPEN.
- Labels per statement: PROVED (L-NEW), READING, CONJECTURE, OPEN.
- Statements: XW (§1), EQ (§2), FBL-N (§3), NF (§4), F1 (§5), F2 (§6), Theorem X (§7), the (w, u*)-run table (§8), FB-W (§9).
  Conjectures and open items: §10.

## 0. Objects and dependencies
- N5: docs/new/N5-ssi-global.md SPEC S1-S5 (S4a arena step against τ; S4b; S4c fallback = switch-all on Iσ, each vertex to its best
  gate edge by (Ξ-key, index); on Iτ if Iσ = ∅). Iσ_k ("the gate") := Even's Ξ_k-improving edges.
- Valuations: VJ00 (BRICS RS-00-48), notation of docs/new/N5-phase-bound-box10.md §1; (V1), (V2), (F1) as in RESULTS R17 (a).
  - Ξ_k := Ω_{σ_k, σ̄_k}: Even's honest valuation, against Odd's best reply σ̄_k in G_{σ_k}.
  - W_k := Ω_{σ_k, τ_k}: the valuation of σ_k in G_τ, the one-player game with Odd fixed to τ_k.
  - θ_k := Ξ_k(o), w_k := W_k(o).
- Signed results used:
  - R15 (a): Ξ_{k+1} ⊵ Ξ_k.
  - R15 (d): at most 4n(n − 1) consecutive iterations leave both Ωσ and Ωτ unchanged.
  - R17: Lemma P, Theorem PH, (F1); every pointwise-optimal arena choice allowed (R17 (d)).
  - R18 (c): flat-case analysis. At a pointwise optimum of an arena, every arena edge that is improving for the valuation is FLAT:
    x = λ(x), z lies in x's region, and switching it changes no value.
  - R18 (d) Lemma S (c): S4a returns σ_k iff σ_k is a pointwise optimum of its arena.
  - R19 (a) Lemma G: (a) off R, Ξ = W, with no (h) needed; (b) under (h), on R, Ξ = π ⊕ θ and W = π ⊕ w; (c) under (h), an edge inside R
    is in the gate iff it is route-improving iff it is W-improving.
  - R19 (b): under (h), w = o ⊕ Ξ(τ(o)).
  - R19 (f) PIECE: in one joint λ-phase, a stretch with τ, w, R constant, (h) and no fallback has ≤ |R| − 1 + |F| − 1
    value-changing transitions; θ constant is NOT needed (N-RE-4).
- Packet P-N5-XA with its fixes (docs/new/P-N5-XA-fixes-box28.md; drafted as R20, CHECKER C29). Only §5 there ("flat fallbacks pass
  PIECE") and the lemmas named in §8 below are used.
- Class 𝒞^1O: exactly one Odd vertex o has out-degree > 1. A PHASE in this packet is a joint λ-phase (λ_Ξ and λ_U constant) with τ
  constant. On 𝒞^1O, τ is determined by τ(o).
- R_k: the vertices whose (σ_k, τ_k)-play reaches o, with o ∈ R_k by convention. F_k := V \ R_k. A transition k → k+1 is a
  CROSSING transition if R_{k+1} ≠ R_k.
- (h) at k: H1 (the honest play from o does not return to o), H2 (the W-play from o does not return to o), H3 (Ξ_k(o) and W_k(o)
  have the same cycle node). P-N5-RE §0.
- State types: EQ (Ξ_k = W_k pointwise); THR ((h) and Ξ_k ≠ W_k); OTHER ((h) fails and Ξ_k ≠ W_k). An OTHER-TOUCHING transition has
  an OTHER endpoint.
- A transition is VALUE-CHANGING if Ξ or W changes at some vertex, and VALUE-PRESERVING otherwise. A NON-FLAT fallback is a
  value-changing S4c transition.

## 1. Lemma XW (PROVED, L-NEW): Ξ_k ⊴ W_k pointwise
At every state k and vertex v, Ξ_k(v) ⊴ W_k(v). In particular θ_k ⊴ w_k.
Proof.
- Both are valuations in G_{σ_k}, where Even is fixed to σ_k and Odd chooses.
- σ̄_k is a pointwise-optimal counter-strategy for Odd there: VJ00 §5.2, Prop. 5.1 and Lemma 5.2, eq. (11); this is R17 (F1) on the
  dual game.
- So Ω_{σ_k, σ̄_k} ⊴ Ω_{σ_k, τ} for every Odd strategy τ, in particular τ_k. □
Corollaries.
- (XW1) Under (h), Ξ_k ≠ W_k iff θ_k ≠ w_k. Lemma G (a)-(b): off R the two agree, and on R they are π ⊕ θ and π ⊕ w.
- (XW2) The three types EQ / THR / OTHER partition the states.
- (XW3) Inside a phase, if w_{k+1} = w_k and θ_k = w_k, then θ_{k+1} = w_{k+1}. Indeed w_k = θ_k ⊴ θ_{k+1} ⊴ w_{k+1} = w_k, by
  R15 (a) and XW.

## 2. Lemma EQ (PROVED, L-NEW): runs with Ξ = W
Let Q be a run of consecutive EQ states inside one phase. Then Q has at most n − 1 value-changing transitions with both endpoints
in Q. (h) is not assumed.
Proof.
- At k ∈ Q, Ξ_k = W_k, so the gate Iσ_k equals G_τ's improving set at σ_k.
- S4a step k → k+1: σ_{k+1} is a pointwise optimum of the arena {σ_k(x)} ∪ Iσ_k(x) in G_τ. That is R17's switch-best step in the
  one-player game G_τ.
- S4c step k → k+1: Even's, since τ is fixed and τ_{k+1} = τ_k (S4c switches Odd only if Iσ_k = ∅, and then τ changes).
  - S4a returned σ_k, so σ_k is a pointwise arena optimum (R18 (d)). By R18 (c), every gate edge is flat.
  - S4c switches at most one flat edge per vertex. Flat switches change no valuation (R18 (c); box 25 §3). So W_{k+1} = W_k, and
    Ξ_{k+1} = W_{k+1} = W_k = Ξ_k.
  - R17's Lemma P invariant (R17 §2: Ω_k(x) ⪰ value(r) for every simple path r of ≤ j edges, j = the number of arena steps) is a
    statement about current values. Its induction step uses only the values and the strategy at that state, (V1), and (F1) for that
    step's arena. So it survives the fallback with j unchanged.
- W's cycle-node map equals Ξ's on Q, and Ξ's is constant in the phase.
- R17 Theorem PH in G_τ, counting arena steps from the first state of Q, gives ≤ n − 1 value-changing arena steps. Fallbacks in Q
  are value-preserving. □

## 3. Lemma FBL-N (PROVED, L-NEW): fallbacks without (h)
Let k → k+1 be an S4c fallback with τ_{k+1} = τ_k. Then:
- (i) it is Even's, and σ_k is a pointwise optimum of the S4a arena in G_τ;
- (ii) every gate edge (x, z) with x ∈ F_k is flat for W_k: x = λ_W(x), and λ_W(z) = x;
- (iii) if H2 fails at k, no gate edge goes from F_k to R_k.
Proof.
- (i) As in §2.
- (ii) x ∈ F_k: x's (σ_k, τ)-play avoids o, so σ_k(x) ∈ F_k and Ξ_k(σ_k x) = W_k(σ_k x) (Lemma G (a)). The edge is a gate edge, so
  Ξ_k(z) ▷ Ξ_k(σ_k x). XW gives W_k(z) ⊵ Ξ_k(z), so W_k(z) ▷ W_k(σ_k x). By R18 (c) at the arena optimum, the edge is flat.
- (iii) If z ∈ R_k and H2 fails, z's W-play reaches o and then runs around o's W-cycle C, so λ_W(z) ∈ C ⊆ R_k. With (ii),
  x = λ_W(z) ∈ R_k, a contradiction. □

## 4. Lemma NF (PROVED, L-NEW): every non-flat fallback outside OTHER is a crossing
Let k → k+1 be an S4c fallback inside a phase with neither endpoint OTHER. If it is value-changing, then R_{k+1} ≠ R_k.
Proof.
- k is EQ: the fallback is value-preserving (§2). So k is THR ((h) holds at k).
- Suppose R_{k+1} = R_k. Classify the switched edges (x, z), all of them gate edges (S4c switches only gate edges):
  - x ∈ F_k: then x ∈ F_{k+1}, so z ∉ R_{k+1} = R_k, i.e. z ∈ F_k. The edge is flat F → F (FBL-N (ii)).
  - x ∈ R_k \ {o}: then x ∈ R_{k+1}, so z ∈ R_{k+1} = R_k (o included). By Lemma G (c), an R → R gate edge is W-improving, so flat at
    the arena optimum (R18 (c)). That needs x = λ(x). But λ(x) = c ≠ x for x ∈ R_k under (h): an R-vertex on its own cycle would put
    o on its own honest cycle. So there is no such edge.
- So every switched edge is a flat F → F edge, and the switched vertices are cycle nodes with disjoint regions. No R-vertex switched.
- Claim: for every exit e of o, the valuation Ω_{σ, e} (Even fixed to σ, o fixed to e, other Odd vertices forced) is the same for
  σ_k and σ_{k+1}.
  - F-vertices: their plays avoid o in both, so their Ω_{σ, e}-values equal their G_τ-values. Those are unchanged by flat
    switches (R18 (c)).
  - R-vertices v: the play follows π_v (unchanged) to o and then e.
    - If e ∈ F, it continues along e's play, which avoids R (every R-vertex reaches o). So Ω_{σ, e}(v) = π_v ⊕ o ⊕ Ω_{σ, e}(e) by
      (V1), and that is unchanged.
    - If e ∈ R, the play closes the cycle o → e → π_e → o, made of unchanged R-paths. So it is unchanged.
- On 𝒞^1O, Odd chooses only at o, and σ̄ is pointwise optimal. So Ξ(v) = min over e of Ω_{σ, e}(v) (with equality for
  e = σ̄(o)), and W = Ω_{σ, τ(o)}. Both are unchanged, so the fallback is value-preserving, a contradiction. (No (h) is needed at
  k+1.) □

## 5. Lemma F1 (PROVED, L-NEW; PIECE's F-part read across w-changes and EQ states without (h)): F-values in an F-interval
An F-INTERVAL is a maximal run I of consecutive states of a phase such that no transition inside I is a crossing transition or an
OTHER-touching transition. (If I has ≥ 2 states, none of them is OTHER.)
Statement. On an F-interval I (with F := F_k, constant on I), the transitions inside I at which Ξ changes at some vertex of F are at
most |F| − 1. On F, Ξ = W.
Proof.
1. On F, Ξ_k = W_k at every k (Lemma G (a), no (h)). F is closed under σ_k (an F-vertex's successor continues its play, which
   avoids o) and contains no vertex with an Odd choice (o ∉ F).
   - Let 𝓕 be the one-player game G_τ restricted to F. Its values are W restricted to F.
2. Gate on F. For x ∈ F (Even) and z ∈ F, (x, z) ∈ Iσ_k iff it is 𝓕-improving at σ_k|F:
   - at EQ states, because Ξ = W;
   - at THR states, by Lemma G (a) at both endpoints.
3. S4a steps. σ_{k+1} is a pointwise optimum of G_τ's arena A_k. There is no crossing, so for x ∈ F, σ_{k+1}(x) ∈ F: otherwise
   x ∈ R_{k+1} = R_k. So σ_{k+1}|F is a strategy of 𝓕's arena A^𝓕_k = {σ_k(x)} ∪ (𝓕-improving edges at x).
   - Any strategy ρ of A^𝓕_k, extended by σ_{k+1} on R, is an A_k-strategy, because 𝓕-improving F-edges are gate edges (step 2).
   - By (F1) in G_τ, W_{k+1} dominates its valuation, which on F depends only on ρ.
   - So σ_{k+1}|F is a pointwise optimum of A^𝓕_k: R17's switch-best step on 𝓕.
4. S4c steps inside I are value-preserving: a non-flat one would be a crossing (Lemma NF). So F-values do not change, and Lemma P's
   invariant on 𝓕 carries over with j unchanged (as in §2).
5. λ on F is λ_Ξ, constant in the phase.
6. R17 Lemma P and Theorem PH on 𝓕 (forced Odd vertices have one successor; R-N5-XA XA-4) give ≤ |F| − 1 value-changing arena
   steps. □
Note (what is new against R19 (f)). PIECE's F-part was signed for stretches with w constant and (h) at every state. The proof above
uses neither: w and θ never enter, and EQ states without (h) are covered by step 2.

## 6. Lemma F2 (PROVED, L-NEW): leaving EQ for THR changes an F-value
Let k → k+1 lie inside an F-interval, with k EQ and k+1 THR. Then τ(o) ∈ F, and Ξ(τ(o)) changes at this transition. Also, at every
transition inside an F-interval with both endpoints THR, a change of w is a change of Ξ(τ(o)).
Proof.
- (h) at k+1 includes H2: o's W-play does not return to o. So τ(o)'s (σ_{k+1}, τ)-play avoids o, i.e. τ(o) ∈ F_{k+1} = F_k.
- At k, τ(o) ∈ F_k, so o's W-play o → τ(o) → … does not return to o, and o is not its own cycle node. By (V1) and Lemma G (a),
  w_k = o ⊕ W_k(τ(o)) = o ⊕ Ξ_k(τ(o)). At k+1, w_{k+1} = o ⊕ Ξ_{k+1}(τ(o)) (R19 (b)).
- If Ξ(τ(o)) did not change, then w_{k+1} = w_k. EQ at k gives θ_k = w_k. By XW3, θ_{k+1} = w_{k+1}, so k+1 would be EQ (XW1), a
  contradiction.
- Second claim: R19 (b) at both endpoints. □

## 7. Theorem X (READING: an assembly of §1-§6 and signed results; L-NEW)
Inside one phase, let X := #crossing transitions and O := #OTHER-touching transitions. Then the phase has at most
    (3n² (1 + X + O) + X + O + 1) · (4n(n − 1) + 1) = O(n⁴ (1 + X + O))
transitions.
Proof.
1. Cut the phase at its crossing and OTHER-touching transitions. The pieces are the F-intervals, at most 1 + X + O of them.
2. Fix an F-interval I, with F constant.
   - Split I into BLOCKS: maximal runs of EQ states and of THR states.
   - Each EQ → THR transition is an F-value change (F2). By F1 there are ≤ |F| − 1 of them. Blocks alternate, so I has
     ≤ 2(|F| − 1) + 2 = 2|F| blocks.
3. EQ blocks: ≤ n − 1 value-changing transitions each (Lemma EQ).
4. THR blocks. Cut each one at its w-changes. Each w-change is an F-value change (F2, second claim), so all THR blocks of I together
   have ≤ |F| − 1 of them.
   - Each resulting SUB-BLOCK has τ, w and R constant, (h) at every state, and no non-flat fallback (NF).
   - Its flat fallbacks switch only flat F → F edges (the proof of NF). So both piece runs continue through them
     (P-N5-XA-fixes §5, whose argument needs exactly this).
   - PIECE (R19 (f), θ free) gives ≤ |R| − 1 + |F| − 1 ≤ n − 2 value-changing transitions per sub-block.
   - There are ≤ #THR blocks + (|F| − 1) ≤ 2|F| sub-blocks.
5. Value-changing transitions inside I:
   ≤ (|F| + 1)(n − 1)            [EQ blocks]
   + 2|F|(n − 2)                 [sub-blocks]
   + 2|F|                        [block boundaries]
   + (|F| − 1)                   [w-change cuts]
   ≤ 3n² (|F| ≤ n − 1).
6. The phase has ≤ 3n²(1 + X + O) + X + O value-changing transitions (the cut transitions are counted once each).
7. A value-preserving transition leaves Ωσ = Ξ unchanged, and Ωτ unchanged because τ is fixed. So R15 (d) bounds runs of them by
   4n(n − 1). □
Consequence (READING). With Lemma Φ (≤ 2n(n − 1) + 1 joint λ-phases; box 21, PROVED by the lane) and τ-changes ≤ d − 1, N5 on
o-cyclic 𝒞^1O makes polynomially many iterations if X and O are poly(n) per phase.
- What is not refereed:
  - Lemmas XW, EQ, FBL-N, NF, F1, F2;
  - this assembly;
  - the use of P-N5-XA-fixes §5 in step 4 outside its original setting (u* ≠ none). Step 4 gives the property that argument needs
    directly.
- Nothing here bounds X or O. X ≤ n on every named instance, but a climb reaches X = 49 at n 32 (N5-NH-box28.md §5c). There the
  crossings come in three waves, each in a different (w, u*)-run, so the per-run lemmas of §8-§9 do not bound X.

## 8. The (w, u*)-run table (READING, L-NEW): which P-N5-XA lemmas survive θ-changes
A (w, u*)-RUN is a maximal run of consecutive THR states in one phase with w and u* constant and u* ≠ none. θ may change, only
strictly below u* (box 27 Lemma UD). Each lemma below was signed for a θ-constant throttled stretch S. This is the place in each
proof where θ enters:
| lemma | survives θ-changes? | where θ enters the proof |
| --- | --- | --- |
| §1 setting (λ_W constant; u* on no route) | yes | per state: u* ∈ P(θ_k) Δ P(w) lies on o's honest play or W-play at k; λ_W = λ_Ξ on F, = c on R |
| Lemma C | yes | per state: P(θ_k) and P(w) agree on V* because u* is the top of their difference at every state of the run; monotonicity is R15 (a) |
| Lemma P^c / CR | yes | the induction uses Lemma C at k and k+1, (Cstrict), (F1) at each arena step, and a vacuous B-fallback (N-XA-1); θ's constancy is never used |
| Theorem XA and count | yes | step 4 uses only that u* tops P(θ_{E+1}) Δ P(w); step 5 uses Lemma C at L |
| FBL, strong gate form | yes | a per-state statement |
| FBF | NO | the induction needs Ξ_t(z) = Ξ_L(z) on R_t, i.e. θ_t = θ_L |
Theorem X does not use this table. Lemma FB-W (§9) does.

## 9. Lemma FB-W (PROVED, L-NEW, given the CR row of §8): post-freeze W-status evictees never re-enter
Let S be a (w, u*)-run with first state k_0. Let an S4c fallback at L ≥ k_0 + n − 1 switch x ∈ R_L to z* ∈ F_{L+1}. Suppose Ξ_L(z*)
has w's status at u* (u* ∈ P(Ξ_L(z*)) iff u* ∈ P(w)). Then x ∉ R_t for every later state t of S.
Proof.
- Two values with the same cycle node that agree above u* and differ at u* are ordered by their status at u*, and w's is the better
  status (w ▷ θ_t is decided at u*).
- For t ∈ S and v ∈ R_t \ {o}: Ξ_t(v) = ρ ⊕ θ_t (Lemma G (b)), and u* ∉ ρ (u* is on no route). So Ξ_t(v) has θ_t's status at u*,
  which is not w's.
- From k_0 + n − 1 on, COARSE(Ξ(v)) is constant for every v (CR in the run, §8).
- Ξ_{L+1}(z*) ⊵ Ξ_L(z*) (R15 (a)), and the two have the same coarse part. So they agree above u*, and Ξ_{L+1}(z*) also has w's
  status: a θ-status value would be strictly smaller.
- x is not its own cycle node (λ(x) = c ≠ x at L, fixed in the phase). So Ξ_{L+1}(x) = x ⊕ Ξ_{L+1}(z*) (V1), with w's status at u*
  (x ≠ u*, since x lies on its own route).
- For t > L: Ξ_t(x) ⊵ Ξ_{L+1}(x) with the same coarse part, so it has w's status too. Hence x ∉ R_t. □

## 10. Conjectures and open items
- OPEN (X): crossing transitions per phase are poly(n). OPEN (NH'): OTHER-touching transitions per phase are poly(n). By Theorem X
  these two carry N5 on o-cyclic 𝒞^1O.
- FALSE (FBRE-F), "no vertex evicted by a fallback at L ≥ k_0 + n − 1 re-enters R in that run".
  - Instance: experiments/new/box28/instances/fbref_n48.pg (n 48, sha1 414231a27ba3…, Oink zlk OK, strategies verified).
  - In one (w, u*)-run of 55 transitions, 10 vertices evicted at run index 48 ≥ 47 re-enter at index 54, after a θ-change at 53.
  - Lemma C and FB-W hold on the same run. All re-entering evictees have θ's status at u*.
- CONJECTURE (FBRE-1): a vertex re-enters after a fallback leave at most once per (w, u*)-run. DATA: max 1 everywhere, including a
  climb on exactly this quantity.
- Data and scripts: N5-NH-box28.md §6, §6.4 (eqcheck.py: XW, EQ, FBL-N, 0 failures), §5c (xcount.py, xclimb.py); code in
  experiments/new/box28/.
