# Referee packet P-N5-XA: a coarse valuation, frozen sets after fallbacks, and re-entries in throttled stretches (box 27)
L-NEW successor 9 (Opus 5.5, D15/D18). Written 2026-10-24 15:05Z-15:25Z (date -u) at the Lead's request (14:45Z).
Self-contained: definitions, statements, full proofs, and the location of every dependency.
Status: L-NEW's proofs, unrefereed. These are lemmas about the candidate N5 on a subclass. They are not a running-time bound, not a
TARGET.md claim, and not a step-4 pass. G-N5-TIME stays OPEN.
Standing ASSUMPTION: (h) at every state of the stretch considered. Nothing here covers states where (h) fails.
Lemmas: C (§2), FBL (§3), FBF (§4), CR (§5), XA (§6). Corollary (§7) is READING.

## 0. Objects and dependencies
- N5: docs/new/N5-ssi-global.md SPEC S1-S5. One iteration from (σ, τ):
  - S4a: σ' := the pointwise-optimal strategy of the one-player arena where Odd is fixed to τ and Even's x may use
    {σ(x)} ∪ Iσ(x);
  - S4b: Odd's symmetric step;
  - S4c: if σ' = σ and τ' = τ, a switch-all (the fallback) on Iσ, each vertex to its best edge by (Ξ-key, index); on Iτ if Iσ = ∅.
  Iσ := Even's improving edges for Ξσ (S2).
- Valuations: VJ00 (BRICS RS-00-48, pdf sha256 485a12de…), notation of docs/new/N5-phase-bound-box10.md §1.
  - A value is (c, P, ℓ). The order compares the reward of c first, then P by the most relevant vertex of the symmetric difference,
    then ℓ (longer is better iff c is odd).
  - (V1) If x is not its own cycle node: val(x) = x ⊕ val(succ x), and the path of val(succ x) avoids x.
  - (V2) If a ⊴ b and both paths avoid x (or the cycle nodes differ), then x ⊕ a ⊴ x ⊕ b, strictly if a ◁ b.
  - (F1) A pointwise optimum of a one-player arena dominates every strategy of the arena.
  - R17 Lemma P (§2 there) with cases A1, A2, B1, B2; R17 Theorem PH (§3).
  These are signed in RESULTS R17.
- R15 (a): Ξ_{k+1} ⊵ Ξ_k pointwise along any N5 run (RESULTS.md "### R15", claim (a)).
- Lemma W (docs/new/N5-time-box21.md §2.5, proved there): with τ fixed, every S4a (arena) step has W_{k+1} ⊵ W_k pointwise.
- Flat-case analysis. In a one-player game with valuation Ω, suppose the optimum of the arena {ρ(x)} ∪ J(x) is ρ itself. Then every
  edge (x, z) ∈ J that is Ω-improving is FLAT: x = λ(x), z lies in x's region, and switching it changes no value. This is
  docs/new/N5-1Oacyc-box24.md §3 Step 2 case (b), cases B1/B2 (signed in RESULTS R18 (c)). Its proof uses only (★) "Ω(x) ⊵ val_ρ̂(x)
  for ρ̂ = ρ[x → z]", which holds whenever ρ̂ is an arena strategy, plus the order.
- Packet P-N5-RE (docs/new/P-N5-RE-box26.md, pinned trunk 52c7261), Lemma G (a)-(c), SIGNED by REFEREE (docs/referee/R-N5-RE.md §1).
  REFEREE's note there: o's honest play and o's W-play avoid all of R_k \ {o}. Also PIECE (signed with gaps P-1, P-2) and RE (signed
  with gaps; (NC) not needed, §4.2 there).
- Class 𝒞^1O: exactly one Odd vertex o has out-degree > 1. R_k, F_k, π_v, θ_k := Ξ_k(o), w_k := W_k(o), (h) and the joint λ-phase are
  as in P-N5-RE §0.
- G_τ: the one-player game in which Odd is fixed to τ. W_k is its valuation of σ_k.

## 1. Setting: throttled stretches and the coarse valuation
- A THROTTLED STRETCH S is a run of states k_0, …, k_1 inside one joint λ-phase with:
  - τ, θ, w constant;
  - θ ◁ w;
  - (h) at every state.
  Fallbacks are allowed. Write c for the common cycle node of θ and w, by (h).
- W's cycle-node map is constant on S.
  - For v ∈ F_k it equals Ξ's (Lemma G (a)), which is constant in the joint λ-phase.
  - For v ∈ R_k it is c.
  - A vertex that changes side changes neither (both give the vertex's honest λ, which is fixed).
- u*: if P(θ) ≠ P(w), u* is the most relevant vertex of P(θ) Δ P(w). Since θ ◁ w with the same c, w is the better side at u*. If
  P(θ) = P(w), put u* := none.
  - Note: o ∉ P(θ) Δ P(w), because o lies on both plays.
  - u* lies on o's honest play or on o's W-play. By REFEREE's note on Lemma G (b), u* ∉ R_k \ {o}, so no route π_v contains u*.
- COARSE value: for v = (c', P, ℓ), COARSE(v) := (c', P ∩ V*), where V* := {vertices more relevant than u*}; V* := V if u* = none.
  The coarse order compares cycle-node rewards, then the most relevant vertex of the symmetric difference (inside V*).
  - (Cmono) a ⊴ b implies COARSE(a) ⪯ COARSE(b).
  - (Cstrict) COARSE(a) ≺ COARSE(b) implies a ◁ b.
  - (V1c), (V2c): (V1) and (V2) hold for COARSE with ⊕_c (x is added iff it is more relevant than the cycle node and lies in V*).
  - Proofs: case-by-case on which key decides. A difference decided by a vertex in V*, or by the cycle node, is seen by COARSE.
    Others are coarse ties. Prefixing adds x on both sides or on neither.

## 2. Lemma C (coarse values agree across frames and never decrease)
Statement. At every state k of S: COARSE(Ξ_k(v)) = COARSE(W_k(v)) for all v, and COARSE(Ξ_{k+1}(v)) ⪰ COARSE(Ξ_k(v)) along S, fallbacks
included.
Proof.
- v ∈ F_k: Ξ_k(v) = W_k(v) (Lemma G (a)).
- v ∈ R_k: by Lemma G (b), Ξ_k(v) = π_v ⊕ θ and W_k(v) = π_v ⊕ w. Both have cycle node c and path sets A_v ∪ P(θ) and A_v ∪ P(w),
  where A_v := {u ∈ π_v more relevant than c}, disjoint from P(θ) ∪ P(w). P(θ) and P(w) agree on V*, so the coarse parts agree.
- Monotonicity: R15 (a) and (Cmono). □

## 3. Lemma FBL (what a throttled fallback switches)
Statement. If the transition k → k+1 (k, k+1 ∈ S) is an S4c fallback, then every edge it switches is either:
- a LEAVE: x ∈ R_k, z ∈ F_k; or
- a flat edge (x, z) with x, z ∈ F_k, x = λ(x) and z in x's region, which changes no value.
Proof.
1. τ is constant on S, so the fallback is Even's (Iσ_k ≠ ∅), and S4a returned σ_k. So σ_k is the pointwise optimum of the arena
   A = {σ_k(x)} ∪ Iσ_k(x) in G_τ. By the flat-case analysis (valuation W_k, J = Iσ_k), every gate edge that is W-improving is flat.
2. Classify the gate edges (x, z) by sides.
   - R → R: honest-improving iff route-improving iff W-improving (Lemma G (c)). Flat would need x = λ(x), but λ(x) = c ≠ x for
     x ∈ R_k (an R-vertex on its own cycle would put o on its own honest cycle, against (h)). So there are none.
   - F → R: honest-improving means π_z ⊕ θ ▷ Ξ_k(σ_k(x)) = W_k(σ_k(x)) (σ_k(x) ∈ F_k), so π_z ⊕ w ⊵ π_z ⊕ θ ▷ W_k(σ_k(x)).
     The edge is W-improving, hence flat, which needs x = λ(x) and z's play to end at x. z's W-play ends at c, so x = c.
     - But then the fallback would switch c into R, and at k+1 o's W-play (o → τ(o) → … → c → z → … → o) would return to o. That
       violates (h) at k+1 ∈ S.
     So there are none.
   - F → F: honest-improving iff W-improving (Lemma G (a)), so flat.
   - R → F: these are the leaves (any W-status).
3. S4c switches each vertex with a gate edge to one of its gate edges. □

## 4. Lemma FBF (after a throttled fallback, R is frozen for the rest of the stretch)
Statement. Let L → L+1 be an S4c fallback inside S. Then for every state t ≥ L+1 of S:
- R_t ⊆ R_{L+1};
- every v ∈ R_t has the same path to o as at L, hence the same route value;
- in particular no vertex enters R at any transition of S after L.
Proof.
1. At L (by the proof of FBL) the gate has no R → R and no F → R edges. So for every edge (y, z) with z ∈ R_L:
   - if y ∈ F_L, then Ξ_L(z) ⊴ Ξ_L(σ_L(y)): not improving;
   - if y ∈ R_L, then Ξ_L(z) ⊴ Ξ_L(σ_L(y)): not route-improving.
2. Claim (by induction on t ≥ L): at every transition t → t+1 of S with t ≥ L, no switched edge (y, z) has z ∈ R_t ∪ {o}.
   Moreover R_{t+1} ⊆ R_t, and paths of R_{t+1}-vertices are unchanged.
   - Base t = L: FBL.
   - Assume it for all transitions in [L, t). Then R_t ⊆ R_L, and every v ∈ R_t has its L-path, so Ξ_t(v) = Ξ_L(v) (same path, same
     θ). Take a gate edge (y, z) at t with z ∈ R_t.
     - If σ_t(y) ∈ R_t: then y ∈ R_t and σ_t(y) = σ_L(y), with Ξ_t(σ_t(y)) = Ξ_L(σ_L(y)) ⊵ Ξ_L(z) = Ξ_t(z) by step 1. Not improving.
     - In every case Ξ_t(σ_t(y)) ⊵ Ξ_L(σ_L(y)).
       - If y never switched in [L, t), this is R15 (a) at σ_L(y).
       - Otherwise, each switch of y was on a gate edge (a new successor of strictly higher Ξ at that moment), and R15 (a) carries the
         values forward.
       - With step 1 (y ∈ F_L or y ∈ R_L alike), Ξ_t(σ_t(y)) ⊵ Ξ_L(σ_L(y)) ⊵ Ξ_L(z) = Ξ_t(z). Not improving.
       - The case σ_t(y) ∈ R_t above is the special case with no switch.
     So no gate edge at t points into R_t. Both S4a and S4c switch only gate edges.
   - Now R_{t+1} ⊆ R_t with unchanged paths. Let v ∈ R_{t+1}, with (t+1)-path v = p_0, …, p_m = o.
     - If some p_i switched at t, take the largest such i. Then p_{i+1}, …, p_m did not switch, so p_{i+1}'s t-path is its
       (t+1)-path, reaching o, i.e. p_{i+1} ∈ R_t ∪ {o}.
     - Then p_i switched to a vertex of R_t ∪ {o}, which is excluded above. (o is not Even; and a switch to o would be an edge into
       R.)
     - So no p_i switched, v's path is unchanged, and v ∈ R_t. □

## 5. Lemma CR (coarse R17: coarse values freeze after n − 1 transitions of S)
Notation. Ω_k := W_k (G_τ's valuation) and Ω^c_k := COARSE(Ω_k) = COARSE(Ξ_k) (Lemma C). For a simple path r = (x = r_0, …, r_L = u) of G_τ
to a vertex u with λ_{k_0}(u) = u, value(r) := (u, P(r), L), as in R17 §2. Paths may pass o and continue along τ(o).
Lemma P^c. For every j with k_0 + j ∈ S, every vertex x and every such r with L ≤ j: Ω^c_{k_0+j}(x) ⪰ COARSE(value(r)).
Proof by induction on j. Base j = 0: r = (u), and Ω_{k_0}(u) = (u, ∅, 0).
Step k → k+1 (k = k_0 + j). Write r = x → z → r', with r' simple from z, avoiding x, |r'| ≤ j. IH: Ω^c_k(z) ⪰ COARSE(value(r')).
Case A_c: Ω^c_k(z) ⪯ Ω^c_k(σ_k(x)).
- A1 (x ≠ λ_k(x)): COARSE(value(r)) = x ⊕_c COARSE(value(r')) ⪯ x ⊕_c Ω^c_k(σ_k(x)) = Ω^c_k(x) ⪯ Ω^c_{k+1}(x).
  - (V2c): r' avoids x, and σ_k(x)'s path avoids x by (V1). Or the cycle nodes differ, which coarse sees.
  - Then (V1c) and Lemma C.
- A2 (x = λ_k(x)): Ω_k(x) = (x, ∅, 0).
  - If x is better than u, Ω^c_k(x) ≻ COARSE(value(r)) by cycle node, and Lemma C carries it to k+1.
  - If x is worse than u, Ω_k(σ_k(x)) has cycle node x while value(r') has cycle node u. So COARSE(value(r')) ≻ Ω^c_k(σ_k(x)) ⪰
    Ω^c_k(z) ⪰ COARSE(value(r')), a contradiction.
Case B_c: Ω^c_k(z) ≻ Ω^c_k(σ_k(x)). By (Cstrict), Ξ_k(z) ▷ Ξ_k(σ_k(x)) and W_k(z) ▷ W_k(σ_k(x)). So (x, z) ∈ Iσ_k, and it is W-improving.
- (B-arena) The transition is an S4a step. σ̂ := σ_k[x → z] is an arena strategy, so by (F1), Ω_{k+1}(x) ⊵ val_σ̂(x) (fine, in G_τ). Let
  c' := λ_k(z) (W's cycle node) and π := z's σ_k-path to c'. Run R17's B1/B2 on the W-improving edge (x, z) in G_τ:
  - B1, x ∉ π, x not on c'’s cycle: val_σ̂(x) = x ⊕ Ω_k(z). By (Cmono), (V2c) (π and r' avoid x) and the IH,
    Ω^c_{k+1}(x) ⪰ x ⊕_c Ω^c_k(z) ⪰ x ⊕_c COARSE(value(r')) = COARSE(value(r)).
  - B1, x ∉ π, x on c'’s cycle: W-improvement means one of two things.
    - (α) P(π) ≠ ∅ with an even top. Then val_σ̂(x) has a cycle node better than c' = λ_k(x). By (F1), λ_{k+1}(x) ≠ λ_k(x) in W's
      map, contradicting §1 (W's cycle-node map is constant on S).
    - (β) P(π) = ∅, c' odd, longer. Then val_σ̂(x) = x ⊕ Ω_k(z), as in the first sub-case.
  - B2, x ∈ π: the σ̂-play from x is the cycle Z = x, z, π[z..x), with D := P(π[z..x)) ∪ ({x} if x is more relevant than c').
    - D ≠ ∅ with an even top, or D = ∅ with top(Z) ≠ c': val_σ̂(x) has a better cycle node, a contradiction as in (α).
    - D = ∅ and top(Z) = c': then c' = x (as in R17), so x is its own cycle node and Ω_k(z) has cycle node x. If x is better than u,
      Ω^c_{k+1}(x) ⪰ Ω^c_k(x) ≻ COARSE(value(r)). If x is worse than u, the IH gives Ω^c_k(z) ⪰ COARSE(value(r')), cycle node u
      against x, a contradiction.
- (B-fallback) The transition is an S4c fallback.
  - By FBL, (x, z) is a leave or a flat edge. It is not flat: for a flat edge, Ω(z) and Ω(σ(x)) have the same cycle node x and equal
    path sets (D = ∅ in the flat-case analysis), so they are coarse-equal, while (x, z) is coarse-strict. So x ∈ R_k and z ∈ F_k.
  - S4c switches x to z*, its gate edge with the best Ξ-key; z* ∈ F_k by FBL.
  - x ∈ R_k gives λ(x) = c ≠ x at k and at k+1 (joint phase).
  - (V1) at k+1: Ξ_{k+1}(x) = x ⊕ Ξ_{k+1}(z*), and that path avoids x.
  - R15 (a) and the choice of z*: Ξ_{k+1}(z*) ⊵ Ξ_k(z*) ⊵ Ξ_k(z).
  - Ξ_k(z)'s path avoids x, since z ∈ F_k and F-plays avoid R_k.
  - So (V2) on (Ξ_k(z), Ξ_{k+1}(z*)) gives Ξ_{k+1}(x) ⊵ x ⊕ Ξ_k(z). Taking COARSE (Lemma C, (V2c), IH): Ω^c_{k+1}(x) ⪰ COARSE(value(r)).
□
Lemma CR. Coarse values are constant on S from state k_0 + n − 1 on: for t ≥ k_0 + n − 1 in S, Ω^c_t = Ω^c_{k_0+n−1}.
Proof.
- Every simple path has ≤ n − 1 edges, so Lemma P^c at j = n − 1 gives Ω^c_{k_0+n−1}(x) ⪰ COARSE(value(r)) for every simple r from x
  to a k_0-cycle node.
- For t ≥ k_0 + n − 1, Ω_t(x) is the value of x's W-play, i.e. value(r_t) for the simple path r_t from x to λ_t(x) = λ_{k_0}(x) (§1),
  which is a k_0-cycle node. So Ω^c_t(x) = COARSE(value(r_t)) ⪯ Ω^c_{k_0+n−1}(x) ⪯ Ω^c_t(x) (Lemma C). □
Remark. When u* = none, COARSE is (c', P) (length dropped), and the proof is the same.

## 6. Theorem XA (re-entries after non-fallback leaves pay a strict coarse increase)
Statement. Assume u* ≠ none. Let x leave R at L, where the transition L → L+1 is an S4a step, not a fallback. Let x next re-enter R at
E > L, with all of L, …, E+1 in S. Then COARSE(Ξ_{E+1}(x)) ≻ COARSE(Ξ_L(x)).
Proof.
1. Lemma W (arena step, τ fixed): W_{L+1}(x) ⊵ W_L(x).
2. x ∈ F_{L+1}, so W_{L+1}(x) = Ξ_{L+1}(x) (Lemma G (a)). x ∈ R_L, so W_L(x) = π^L ⊕ w (Lemma G (b)).
3. R15 (a): Ξ_{E+1}(x) ⊵ Ξ_{L+1}(x). x ∈ R_{E+1}, so Ξ_{E+1}(x) = π^{E+1} ⊕ θ. Hence π^{E+1} ⊕ θ ⊵ π^L ⊕ w.
4. Suppose the coarse parts were equal: the same cycle node c and the same vertices in V*. Then the symmetric difference of the full
   path sets (A_{E+1} ∪ P(θ)) Δ (A_L ∪ P(w)) lies outside V*. It contains u*, because u* ∈ P(θ) Δ P(w) and u* is on no route (§1).
   So its top is u*, where w is better: π^L ⊕ w ▷ π^{E+1} ⊕ θ, contradicting step 3.
5. So the coarse parts differ, and by step 3 the difference is decided inside V* in favour of π^{E+1} ⊕ θ:
   COARSE(Ξ_{E+1}(x)) ≻ COARSE(π^L ⊕ w) = COARSE(π^L ⊕ θ) = COARSE(Ξ_L(x)) (Lemma C). □
Count. For one x the intervals (L, E+1] of successive such re-entries are disjoint, and each contains a strict coarse increase of x.
By Lemma CR all coarse increases on S lie in its first n − 1 transitions, at most one per vertex per transition. So S has at most
n(n − 1) such re-entries.

## 7. Corollary (READING; combines §3-§6 with PIECE, P-N5-RE §5, and the referees' repairs P-1, P-2)
In a throttled stretch S with u* ≠ none:
- All entries into R happen before S's first fallback (FBF). Re-entries there follow S4a leaves, so there are at most n(n − 1) of them
  (XA). First entries number at most n.
- So entries ≤ n + n(n − 1), and leaves ≤ entries + n.
- Each non-flat fallback contains a leave (FBL). Flat fallbacks change no value; R15 (d) bounds them.
- Between crossings and fallbacks, PIECE (inside one joint λ-phase, as P-2 requires) gives ≤ n − 2 value-changing transitions.
- Total: crossings, non-flat fallbacks and value-changing transitions of S are O(n³).

## 8. Data (DATA, not proof; experiments/new/box25/; instances checked with Oink zlk and harness verify.py)
- Lemma C and CR (coarsecheck.py --withfb): C1 (coarse Ξ = coarse W) and C2 (the last coarse change ≤ n − 1 into the stretch), 0
  failures:
  - on fts_best16, theta_tp32, returns_rt48, returns_ph64, theta_thf16, thetare_n, i1h_fts_best16;
  - in 8,000 random o-cyclic 𝒞^1O runs.
  Max index of the last coarse change: 10 (theta_tp32, n 32).
- FBL (fbedges.py): 77 of 77 switched edges at 36 throttled (h)-fallbacks are leaves, on the same instances plus fbh_drop9 and fbh_thr.
- FBF (fbfcheck.py): 0 entries and 0 route changes in 141 post-fallback transitions after 39 throttled fallbacks. The FB-RE climbs
  (fbreclimb.py) raised fallback leaves to 81 per run (n 48) with 0 re-entries.
- XA: no re-entry inside a throttled stretch occurs in the samples (crossings.py, coarsecheck.py), so XA's strictness is untested by
  data, like RE's in REFEREE's random samples. It rests on the proof.
