# Referee packet P-N5-RE: four lemmas on N5 inside a τ-fixed joint λ-phase of a one-Odd-choice game (box 26)
L-NEW successor 9 (Opus 5.5, D15). Written 2026-10-24 ~14:00Z (date -u) at the Lead's request (13:52Z). Self-contained: definitions,
statements, full proofs, and the exact location of every dependency.
Status: L-NEW's proofs, unrefereed. These are lemmas about the candidate N5 on a subclass. They are not a running-time bound, not a
TARGET.md claim, and not a step-4 pass. G-N5-TIME stays OPEN. The packet uses one standing ASSUMPTION, (h) below. Lemma RE carries
one explicit hypothesis, (NC).

## 0. Objects and dependencies (exact locations)
- N5 = docs/new/N5-ssi-global.md, SPEC S1-S5. Code: experiments/new/n5.py. One iteration from (σ, τ):
  - S4a: σ' := the pointwise-optimal strategy of the one-player arena in which Odd is fixed to τ and Even's x may use
    {σ(x)} ∪ {z : (x, z) ∈ Iσ};
  - S4b: the symmetric Odd step;
  - S4c: if σ' = σ and τ' = τ, a switch-all ("fallback") on Iσ, or on Iτ if Iσ = ∅.
  Iσ is Even's set of improving edges with respect to Ξσ (S2).
- Valuations (VJ00 = Vöge-Jurdziński, BRICS RS-00-48, pdf sha256 485a12de…, §4-§5; notation of docs/new/N5-phase-bound-box10.md
  §1). A value is (c, P, ℓ): the cycle node c, the set P of path vertices more relevant than c, and the length ℓ.
  - (V1) If x is not its own cycle node, val(x) = x ⊕ val(succ(x)), and the path from succ(x) to c avoids x.
  - (V2) Prefix monotonicity: if a ⊴ b and both paths avoid x (or the cycle nodes differ), then x ⊕ a ⊴ x ⊕ b, strictly if a ◁ b.
  - (F1) The optimum of a one-player arena dominates every strategy of that arena pointwise.
  (V1), (V2) and (F1) are at docs/new/N5-phase-bound-box10.md §1 (signed in RESULTS R17).
- Ξσ = Even's honest valuation (against Odd's pointwise-optimal reply σ̄). R15 (a): along any N5 run, Ξ_{k+1} ⊵ Ξ_k pointwise.
  RESULTS.md "### R15", claim (a) (VJ00 Lemma 5.7).
- W_k := V_{σ_k,τ_k}, the value of the (σ_k, τ_k)-play. Lemma S (b): Ξ_k ⊴ W_k pointwise. docs/new/N5-time-box21.md §2.2; signed in
  RESULTS R18 (d).
- R17 Lemma P and Theorem PH: docs/new/N5-phase-bound-box10.md §2-§3. Corollary 2 holds from ANY start strategy: RESULTS R17 (e),
  and both referees in R18 (c).
- Class 𝒞^1O: exactly one Odd vertex o has out-degree > 1; every other Odd vertex is forced.
- R_k := {v : the (σ_k, τ_k)-path from v reaches o}, following forced Odd edges and τ_k at o; o ∈ R_k. F_k := V \ R_k.
  π_v := v's path to o, o excluded.
- θ_k := Ξ_k(o) and w_k := W_k(o).
- A joint λ-phase is a maximal run of states in which the cycle-node maps of Ξσ and of Odd's dual valuation are constant
  (docs/new/N5-time-box21.md §2.3).
- ASSUMPTION (h) at state k (docs/new/N5-time-box21.md §3.5): the honest play from o (under (σ_k, σ̄_k)) and the W-play from o (under
  (σ_k, τ_k)) do not return to o, and Ξ_k(o), W_k(o) have the same cycle node.

## 1. Lemma G (a)-(c) (L-NEW box 21 §3.5, restated with proof; this packet depends on it)
Assume (h) at state k, and write c for the common cycle node of θ_k and w_k.
- (a) If v ∈ F_k, then Ξ_k(v) = W_k(v).
  Proof: the σ_k-path from v meets no Odd vertex with a choice before it closes (it never reaches o), so the plays under σ̄_k and
  τ_k coincide. □
- (b) If v ∈ R_k, then Ξ_k(v) = π_v ⊕ θ_k and W_k(v) = π_v ⊕ w_k, where ⊕ along a path is iterated (V1).
  Proof: both plays follow π_v to o and then o's continuation. By (h) that continuation does not return to o. It also avoids π_v,
  since any vertex of π_v reaches o, so meeting one would return the play to o. Apply (V1) along π_v. □
- (c) For y, z ∈ R_k: π_y ⊕ T ⊴ π_z ⊕ T holds for T = θ_k iff it holds for T = w_k. Call this the ROUTE ORDER: y's route ⊴ z's
  route.
  Proof: both terminals have the cycle node c. π_y ⊕ T = (c, A_y ∪ P(T), |π_y| + ℓ(T)), with A_v := {u ∈ π_v : u more relevant
  than c}. The set A_v is disjoint from P(T) (by (b)). The symmetric difference is A_y Δ A_z and the length difference is
  |π_y| − |π_z|, whichever T is used. □

## 2. Lemma Wo (w is non-decreasing)
Statement. Let k → k+1 be an N5 transition with τ_{k+1} = τ_k and (h) at k and at k+1. Then w_{k+1} ⊵ w_k.
Proof. Let b := τ(o). By (h) the W-play from o does not return to o, so b's (σ_j, τ)-path does not reach o and b ∈ F_j, for
j = k, k+1. By Lemma G (a), W_j(b) = Ξ_j(b). The vertex o is not its own cycle node (its W-play does not return to it), so
w_j = o ⊕ W_j(b) = o ⊕ Ξ_j(b) by (V1). By R15 (a), Ξ_{k+1}(b) ⊵ Ξ_k(b). Both paths avoid o, so (V2) gives
w_{k+1} ⊵ w_k. □

## 3. Lemma RM (routes never decrease while θ is constant)
Statement. Let k → k+1 lie in one joint λ-phase, with τ_{k+1} = τ_k, θ_{k+1} = θ_k =: θ, and (h) at k and at k+1. If
x ∈ R_k ∩ R_{k+1}, then π_x^{k+1} ⊕ θ ⊵ π_x^k ⊕ θ, i.e. x's route does not decrease in the route order of Lemma G (c).
Proof. By Lemma G (b), Ξ_j(x) = π_x^j ⊕ θ for j = k, k+1. By R15 (a), Ξ_{k+1}(x) ⊵ Ξ_k(x). Both sides have the terminal θ with cycle
node c, so the comparison is the route comparison of Lemma G (c). □

## 4. Lemma RE (re-entries strictly improve the route, or θ changed)
Statement. Inside one joint λ-phase with τ constant, let x ∈ R_L, x ∉ R_{L+1} (a LEAVE at L), x ∉ R_j for L < j ≤ E, and x ∈ R_{E+1}
(the next RE-ENTRY). Assume (h) at L and at E+1, and hypothesis (NC) below. Then:
  if θ_{E+1} = θ_L, then π_x^{E+1} ⊕ θ_L ▷ π_x^L ⊕ θ_L (a strict route improvement).
Hypothesis (NC), the only residue of the earlier gap G26-1:
- Let y be the first vertex of π_x^L whose successor changes at L → L+1 (y = x if x itself switched). Then NOT both of:
  - (i) y's new play closes a cycle through y;
  - (ii) Ξ_L(y) has an empty path set above c (no vertex of y's honest path, o and θ's path included, is more relevant than c).
- §6 shows that every other case is handled. DATA: no counterexample (class OTHER = 0 in every sample, box 26 §1).
Proof.
1. A first vertex y exists. The L-path of x reaches o and the (L+1)-path does not, so some vertex on π_x^L switched. Odd's τ is
   fixed, and o's continuation does not matter for membership.
2. Strict gain at y: Ξ_{L+1}(y) ▷ Ξ_L(y).
   - y ∈ R_L, so y is not its own cycle node at L. Otherwise y would lie on its own cycle while its play reaches o, putting o on the
     cycle of o's honest play, against (h). The cycle nodes are constant in the phase, so this also holds at L+1.
   - y switched on a gate edge (y, z). In an S4a step, the arena admits only {σ(y)} ∪ Iσ(y). In an S4c step, the switched edges lie
     in Iσ. In both cases Ξ_L(z) ▷ Ξ_L(σ_L(y)).
   - Case NOT (i): y's new play does not close a cycle through y, so the paths of Ξ_{L+1}(z), Ξ_L(z) and Ξ_L(σ_L(y)) avoid y.
     Then Ξ_{L+1}(y) = y ⊕ Ξ_{L+1}(z) by (V1), then ⊵ y ⊕ Ξ_L(z) by R15 (a) and (V2), then ▷ y ⊕ Ξ_L(σ_L(y)) = Ξ_L(y) by strict
     (V2) and (V1).
     - Caveat: if z's L-path passed y, then z ∈ R_L and y's new play would cycle back through y, which is case (i). So the
       avoidance holds in this case.
   - Case (i) and NOT (ii): y's new play closes a cycle C through y. The cycle node of y is still c (the phase), so c ∈ C and c is
     the top of C. Hence Ξ_{L+1}(y) = (c, ∅, ℓ'). Also Ξ_L(y) = (c, P_L, ℓ_L) with P_L ≠ ∅ (NOT (ii)).
     - By R15 (a), Ξ_{L+1}(y) ⊵ Ξ_L(y). Comparing the path sets: ∅ ⊵ P_L, so the most relevant vertex of P_L is odd, and then
       ∅ ▷ P_L strictly.
     So Ξ_{L+1}(y) ▷ Ξ_L(y).
3. Strict gain at x: Ξ_{L+1}(x) ▷ Ξ_L(x).
   - If y = x, this is step 2.
   - Otherwise the prefix of π_x^L from x up to y is unchanged at L+1, and its vertices are in R_L, so none is its own cycle node.
     Repeated (V1) and strict (V2) along the prefix give the claim. The prefix avoids y's new play: otherwise x's new play would pass
     a prefix vertex twice.
4. Monotone between: Ξ_{E+1}(x) ⊵ Ξ_{L+1}(x) by R15 (a), applied E − L times.
5. Conclude. By Lemma G (b) at L and at E+1, Ξ_L(x) = π_x^L ⊕ θ_L and Ξ_{E+1}(x) = π_x^{E+1} ⊕ θ_{E+1}. With θ_{E+1} = θ_L,
   steps 3-4 give π_x^{E+1} ⊕ θ_L ▷ π_x^L ⊕ θ_L. □
Corollary RE (counting).
- Suppose that inside a joint λ-phase, (h) holds at every leave and re-entry state and (NC) holds at every leave.
- Then each re-entry of x is either a strict route improvement over x's last leave (class ROUTE) or has a θ-change in its interval
  (L, E+1].
- The leave-to-re-entry intervals of one vertex are disjoint. So the non-ROUTE re-entries of x number at most #θ-changes in the
  phase, and:
      #re-entries in the phase ≤ n · #θ-changes + #ROUTE re-entries. □

## 5. Lemma PIECE (between crossings, N5 is two independent one-player R17 runs)
Statement. Let a stretch of transitions k_0 → … → k_1 lie in one joint λ-phase with:
- τ, θ, w constant;
- (h) at every state;
- no S4c fallback;
- R_k = R_{k_0} =: R for every state of the stretch (no crossing).
Let F := V \ R. Then the stretch has at most (|R| − 1) + (|F| − 1) ≤ n − 2 transitions at which some Ξ_k(v) or W_k(v) changes.
Proof.
1. Closure. For v ∈ R, every vertex of π_v^k reaches o, so lies in R. For v ∈ F, every vertex of v's play avoids o, so lies in F.
   This holds at every state of the stretch.
2. Two games.
   - The ROUTE GAME 𝓡: vertices R ∪ K, where K is o's W-continuation at state k_0 (a path in F from τ(o) to its cycle), frozen.
     Even's edges inside R go R → R; the forced Odd vertices of R keep their edges; o keeps the edge τ(o).
     - Plays of 𝓡 either reach o and then follow K, or cycle inside R.
     - A play through o has the value π ⊕ w, by (V1) and (h). Under the real strategies o's continuation may change inside the
       stretch, but its value w is constant, so 𝓡's values do not change.
     - By Lemma G (b), W_k|R is the 𝓡-valuation of σ_k|R. By Lemma G (c), comparisons of R-vertices' routes are the same for
       the terminal θ or w.
   - The O-FREE GAME 𝓕: the subgame G[F] with Even's edges F → F. Its plays are o-free, and W_k|F = Ξ_k|F is its valuation (Lemma G (a)).
   Both are one-player games for Even.
3. Gates.
   - For x, z ∈ R: (x, z) ∈ Iσ_k iff π_z ⊕ θ ▷ π_{σ(x)} ⊕ θ, iff (x, z) is 𝓡-improving (Lemma G (b), (c)).
   - For x, z ∈ F: (x, z) ∈ Iσ_k iff W_k(z) ▷ W_k(σ(x)), iff (x, z) is 𝓕-improving (Lemma G (a)).
4. Steps. At each transition of the stretch, σ_{k+1} is the S4a arena optimum against τ (there are no fallbacks), and no vertex crosses.
   - For x ∈ F: x's play under σ_{k+1} stays in F. The restriction σ_{k+1}|F is an arena strategy of 𝓕's arena
     A_k^𝓕(x) = {σ_k(x)} ∪ (Iσ_k(x) ∩ F).
   - For every strategy ρ of that F-arena, extend it by σ_{k+1} on R. This is a strategy of the S4a arena whose values on F are ρ's
     𝓕-values (F is closed). By (F1) for the S4a arena, W_{k+1}(x) ⊵ val_ρ(x). Since σ_{k+1}|F is itself such a ρ, it is the
     pointwise optimum of the F-arena.
   - For x ∈ R the same argument, with o as terminal (Lemma G (b), (c) and the common terminal w), shows that σ_{k+1}|R is the pointwise
     optimum of 𝓡's arena A_k^𝓡(x) = {σ_k(x)} ∪ (Iσ_k(x) ∩ R).
   So σ_k|F (respectively σ_k|R) runs R17's switch-best (arena-optimum) rule on 𝓕 (respectively 𝓡), from the start strategy at k_0.
5. Count. R17 Theorem PH (docs/new/N5-phase-bound-box10.md §3), valid from any start (R17 Corollary 2), gives the following.
   - In one λ-phase of a one-player game with N vertices, at most N − 1 transitions change a value.
   - In 𝓕 the cycle nodes are those of Ξ on F, constant in the joint phase. In 𝓡 every play ends at the terminal, so there is one
     phase.
   - A transition that changes some value changes a 𝓡-value or a 𝓕-value. So there are at most (|R| − 1) + (|F| − 1) such
     transitions. □
Consequence (READING). In a stretch with τ, θ, w constant and (h), each fallback-free run between crossings is a piece. So
    #value-changing transitions ≤ (n − 1) · (#crossing transitions + #fallbacks + 1).

## 6. What is not covered
- States where (h) fails: e.g. τ(o) closing a cycle at o (box 25 §3, wdrop_cyc).
- The number of θ-changes per phase (CYC), crossings per (θ, w)-stretch (XING), and fallbacks per phase (FB-1O). These are OPEN.
- Hypothesis (NC): the case "y's new play closes a cycle C ∋ y with top c, and Ξ_L(y) has an empty path set above c". Here
  Ξ_{L+1}(y) = (c, ∅, ℓ') may equal Ξ_L(y) if the lengths agree.
  - Then the leave is a "flat" leave, and RE's strictness can fail.
  - An argument that excludes it, or an instance that exhibits it, would settle (NC). None is known.

## 7. Data (DATA, not proof; experiments/new/box25/; every instance checked with Oink zlk and harness verify.py)
- RM (routemono.py): 0 route decreases at (h)-states on fts_best16, theta_tp32, returns_rt48, returns_ph64, tr20_s4, i1h_fts_best16,
  and in two samples of 6,000 random o-cyclic 𝒞^1O games. All 96 decreases seen are at non-(h) states.
- RE (reentry.py): class OTHER (no strict gain and no θ/w rise) 0 in all samples. THETA re-entries (route identical, θ rose, w fixed)
  occur, e.g. thetare_n.pg (n 11, sha1 64698459…), so the θ-alternative in RE is needed.
- PIECE (piececheck.py): 0 violations of "≤ n − 2". Longest piece 10 (theta_tp32, n 32; rtt24, n 24).
- Wo (wocheck.py): 0 decreases of w over 5,341 pairs of consecutive (h)-states with τ fixed (random o-cyclic 𝒞^1O, n 4-16,
  seeds 141 canonical and 142 random starts), and 0 on fbh_drop9, i1h_fts_best16 and returns_rt48.
  - The W-drops of box 25 §3 are at vertices other than o. Under (h) at consecutive states, b ∈ F, so w = o ⊕ Ξ(b).
