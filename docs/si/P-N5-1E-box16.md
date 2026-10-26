# Referee packet P-N5-1E: N5 solves one-Even-choice parity games in polynomial time from any start pair, and N5's output at its stop is correct on every game (Lemma OUT-G) — a subclass result for the time bound, not a TARGET.md claim
Author: L-SI successor 11 (Opus 5.5; D15, D18, L37, L40), session_01FchPxfEZ9Fo56WrCZTvnXS. Written at the Lead's request of 01:5xZ and its
GO of 02:21Z (Lead's stamps). DRAFT: not frozen. It is frozen on the Lead's word after P-N5-DUAL lands (RESULTS R54). Repairs after the
freeze go to a NEW fixes file. Stamp: the commit (date -u).
- Labels (D18 / L40): PROVED (L-SI 11, from landed or signed results only) / READING / DATA. D1: wrong until checked.
- Scope.
  - Time bound: the candidate N5 (SPEC S1-S5 with Q1-Q4 and FIX 1-4, docs/new/N5-ssi-global.md) on 𝒞^1E, the games in which exactly one
    Even vertex e has out-degree > 1. Odd may have any number of choice vertices.
  - 𝒞^1E is polynomial by other means (Even has ≤ d_e positional strategies, and each leaves a one-player game). So the value of the time
    bound is the METHOD. It is NOT a TARGET.md §2 claim (TARGET.md §4: "Polynomial only on a restricted class" does not count as M4).
  - Lemma OUT-G (output correctness) is stated and proved for EVERY parity game. It is a correctness lemma for N5, not a running-time
    bound and not a TARGET.md claim. G-N5-TIME stays OPEN for general games.

## 0. What to sign
| § | statement | label | to sign |
| --- | --- | --- | --- |
| §2 | Lemma OUT-G (every game): if Iσ = ∅, then SPEC S5's output at σ is the pair of winning regions with positional winning strategies. So N5's output at its stop is correct on every game | PROVED | yes |
| §3 | Lemma BIT-G (every game): RESULTS R51 (c)'s cost bound holds on every game; its proof has no class step | PROVED (class audit of R51 (c)'s proof) | yes |
| §4 | Theorem 1E-POLY: on 𝒞^1E, from any start pair, N5 makes ≤ (n(n − 1) + d_e)(T*(n, m, Δ, d_e) + 1) = O(m·Δ·d_e·n¹³) ⊆ O(n¹⁷) iterations | PROVED (from R51 + P-N5-DUAL) | yes |
| §5 | Corollary 1E-TIME: on 𝒞^1E, N5 from any start pair outputs (W_E, W_O) and positional winning strategies in time polynomial in n + m at bit cost | PROVED | yes |
| §6 | gauntlet status; what OUT-G does for R15's G-N5T-3 | READING | no |
| §7 | DATA (experiments/si/out16/) | DATA | no |

## 1. Cited results (exact statement text and hypotheses)
| result | statement (as landed or signed) | class | start pair |
| --- | --- | --- | --- |
| R15 (c), (d) | (c) "≺ is a strict partial order on strategies and every non-empty switch of improvements goes strictly up in ≺"; (d) "every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and changes at least one of them … Hence no (σ, τ) state repeats and N5 terminates" | every game | any (SPEC) |
| R36 (c) Lemma P1 | "if σ is a positional Even strategy of a one-player game H with no improving edge (no Even edge (x, y) with V_σ(y) ▷ V_σ(σ(x))), then V_σ(v) ⊵ V_{σ′}(v) for every positional Even strategy σ′ and every vertex v" (one-player: every non-Even vertex has one successor; V_σ the play valuation) | every one-player game | — |
| R18 (d) Lemma S (a) | "(a) L_σ is the pointwise minimum of V_{σ,τ'} over Odd's strategies τ' and U_τ the pointwise maximum of V_{σ',τ} over Even's σ' (VJ00 (11) on G and on G^d)" (L_σ := Ξσ, docs/new/N5-time-box21.md §1) | signed in 𝒞^1O; proof game-general (N-1O-4) | — |
| R21 (a) Lemma XW | "Ξ_k ⊴ W_k pointwise at every state (Odd's best reply σ̄_k is pointwise optimal in G_{σ_k})" | signed in 𝒞^1O; the parenthetical is game-general (N-1O-4) | any |
| VJ00 (11) | BRICS RS-00-48 (Vöge, Jurdziński, Dec 2000), §5.2, p. 16: "Ωσ = Θσσ̄ (11). Hence by definition of Ωσ we get that Θσσ̄ ⊴ Θστ, for all strategies τ for player ⊖. In other words, σ̄ is a best counter-strategy against σ." With §4.3 (p. 12): "Ωσ(v) = min⊴ {Θ(P) : P ∈ Playsσ(v)}" | VJ00 §2: "finite parity game graphs … every vertex has at least one out-going edge" | — |
| R51 (a), (b), (c) | (a) Theorem 1O-POLY: "for G ∈ 𝒞^1O and any start pair (the S3 start included), N5 stops after at most ITER ≤ (n(n − 1) + d_o)·(T* + 1) iterations, where T* is R50 (h)'s bound with f := F := 2n² (R48 (i) gives f ≤ 2n² in every phase; every term of R50 (h)'s chain is non-decreasing in f) … and n(n − 1) + d_o is R47 (b)'s phase count"; (b) start-freeness of every result the chain cites; (c) Lemma BIT (quoted in §3) | 𝒞^1O | any |
| P-N5-DUAL (R54, landing) | Lemma DUAL, first sentence: "For every game G and start pair (σ_0, τ_0): the N5 run on G from (σ_0, τ_0) is the mirror of the N5^OF run on G^d from (τ_0, σ_0) (same length, state k ↦ mirror of state k)". Theorem MIRROR (a), (b), (c), quoted in §4 | DUAL every game; MIRROR 𝒞^1E / 𝒞^1O | any |
- P-N5-DUAL is SIGNED by both referees: REFEREE R-N5-DUAL, referee cdb187c7, §C 78db369b; REFEREE-2 R2-N5-DUAL, referee-2 73c2b4a1, §C
  253fe5c5. Its only gap is DUAL-1 = N-DUAL-1, the wording of Lemma DUAL's SECOND sentence, repaired in docs/new/P-N5-DUAL-fixes-box43.md
  (l-new 478dd6e1). This packet uses only the FIRST sentence, MIRROR (a)-(c) and their proofs.
- T*(n, m, Δ, d) is R51 (a)'s T* written as a function of the game's parameters (P-N5-1O §2, verbatim):
  T_H := n² + 2n − 1;  X_SN := 13(d + 1)n³(F + 1 + T_H) + T_H;  X := (F + 1)(n − 1) + F + X_SN;  Θ := (n − 1) + n(X + 1) + X;
  S_o := d(Θ + 1);  W_ch := (F + X + 1)n²;  N_st := 1 + X + Θ + W_ch;  N_Ξ := F + N_st + (X + 1)(n − 1) + (N_st + F)·3Δn⁴;
  T* := (m − n + 1)(S_o + N_Ξ + 1), with F := 2n².
- SPEC (docs/new/N5-ssi-global.md) is the object, not a cited result. The code (experiments/si/si.py Engine.evaluate,
  experiments/new/n5.py run()) implements SPEC. It is DATA, not proof.

## 2. Lemma OUT-G (PROVED, every game): a stop without Even improving edges outputs the solution
Statement. Let G be any parity game (TARGET.md §1: V finite, every vertex has a successor) and σ a positional Even strategy with Iσ = ∅
(SPEC S2). Put λ(v) := the cycle node of Ξσ(v), W := {v : Ω(λ(v)) even}, and σ̄ := S1's Odd counterstrategy at σ. Then:
- W = W_E(G) and V ∖ W = W_O(G);
- σ wins for Even from every v ∈ W against every (history-dependent) Odd strategy;
- σ̄ wins for Odd from every v ∉ W against every (history-dependent) Even strategy;
- σ restricted to W and σ̄ restricted to V ∖ W are well defined on their regions.
In particular, on every game N5 stops (R15 (d)) at a state with Iσ = Iτ = ∅, and SPEC S5's output there is correct.
Iτ = ∅ is not used.

Premises (no class hypothesis in any of them).
- (VJ) For every game G, every positional σ and every positional Odd strategy τ′: Ξσ(v) ⊴ V_{σ,τ′}(v) at every v. Here V_{σ,τ′}(v) is S1's
  valuation (c, P, ℓ) of the (σ, τ′)-play from v.
  - SPEC S1 DEFINES Ξσ as "valuation of every vertex under σ and Odd's OPTIMAL counterstrategy σ̄ (minimising this order at every vertex
    at once)", with σ̄ computed by VJ00's procedure.
  - VJ00 (11) is the source. Its setting is every finite game graph with a successor at each vertex (§2), so it holds with no class
    hypothesis. It gives Θσσ̄ ⊴ Θστ for every Odd τ, with σ̄ VJ00's successor-minimiser (§5.2, p. 14-16; proof: Prop. 5.1 from (3), (6), (8),
    (9) of §5.1, and Lemma 5.2).
  - Any pointwise-optimal positional σ̄′ has the same valuation, Θσσ̄′ = Ωσ. Indeed Θσσ̄′ ⊴ Θσσ̄ = Ωσ by optimality, and Ωσ ⊴ Θσσ̄′
    because Ωσ(v) is the minimum over all plays from v consistent with σ (§4.3).
    So SPEC's Ξσ equals VJ00's Ωσ whichever optimal σ̄ S1's tie-breaks pick.
  - In the fleet's record, the same statement is R18 (d) Lemma S (a) ("L_σ is the pointwise minimum of V_{σ,τ'} over Odd's strategies τ'";
    proof "VJ00 (11)") and R21 (a)'s parenthetical. Both were signed with the setting 𝒞^1O. Both referees judged the proof game-general:
    - N-1O-4, accepted by both referees' §Cs of R-N5-1O;
    - REFEREE §C of R-N5-DUAL, C.2: "Lemma OUT's proof uses R36 (c) (every one-player game) and R21 (a)'s parenthetical, whose proof is
      game-general … I see no 𝒞^1O step in it."
    This packet asks the referees to SIGN (VJ) on every game, as the premise of OUT-G, with VJ00 (11) as its source.
  - The remaining link, that S1's procedure computes an optimal σ̄, is SPEC's own requirement. Every landed N5 result uses it.
    The code's match is DATA (R15 G-N5T-1; R15 (ii): si.py agrees with a VJ00 brute force on both sides).
- (P1) R36 (c), on every one-player game.
- SPEC S1 (the valuation, its order, rewards), S2 (Iσ), S5 (the output).

Proof.
0. Rewards. reward(c) = p′(c) = 2·rank(c) ≥ 0 if Ω(c) is even, and −p′(c) = −(2·rank(c) + 1) ≤ −1 if Ω(c) is odd (SPEC S1). So a cycle
   node is even iff its reward is ≥ 0. (This is P-N5-1O's OUT-1 = N-1O-1 repair, built in.)
1. A one-player cycle fact (any game graph). Let H be a game graph in which one player's choices are fixed, so only the other player (the
   mover) chooses. If some infinite play of H from v has max-parity outcome of parity p, then some positional strategy of the mover gives
   a play from v whose valuation has a cycle node of parity p.
   - Let D be the vertices seen infinitely often and q the highest priority among them, so q has parity p. D induces a strongly connected
     subgraph of H (the play moves inside D from some point on). Let t be the top-ranked vertex of D with priority q.
   - Inside D there is a simple cycle C through t. Every vertex of C has rank ≤ rank(t), so t is C's most relevant vertex.
   - Take a shortest path π in H from v to C; it meets C only at its end. Let the mover follow π, then C, and play arbitrarily elsewhere.
     This is positional: π ∪ C visits each vertex once, and the fixed player's moves on π and C are H's own edges.
   - The play from v is the lasso π·C^ω, and its cycle node is t (S1: "the most relevant (max p′) vertex of the cycle the play ends in"),
     which has parity p.
2. Even's side; holds for every σ. Let v ∈ W, so reward(λ(v)) ≥ 0 (step 0).
   - By (VJ), for every positional Odd τ′, V_{σ,τ′}(v) ⊵ Ξσ(v). The order compares cycle-node rewards first, so the cycle node of
     V_{σ,τ′}(v) has reward ≥ reward(λ(v)) ≥ 0: it is even (step 0).
   - Suppose some play from v consistent with σ (Odd history-dependent) had an odd outcome. Step 1 in H := G_σ, where Even is fixed to σ
     and Odd moves, gives a positional τ′ whose (σ, τ′)-play from v has an odd cycle node. That contradicts the previous line.
   - So σ wins every play from v: W ⊆ W_E(G), with σ as the witness.
3. Odd's side; uses Iσ = ∅. Let v ∉ W, so reward(λ(v)) ≤ −1.
   - H := G_σ̄ (Odd fixed to σ̄) is a one-player game in R36's sense: every non-Even vertex has one successor. σ is a positional Even strategy
     of H.
   - σ's play valuation in H is the valuation of the (σ, σ̄)-play. That is Ξσ, by SPEC S1's definition ("valuation of v under (σ, σ̄)" is the
     (c, P, ℓ) of the play from v).
   - So σ's improving edges in H, in R36's sense ("Even edge (x, y) with V_σ(y) ▷ V_σ(σ(x))"), are exactly SPEC S2's Iσ: the Even edges of H
     are G's, and V_σ = Ξσ. Iσ = ∅ by hypothesis.
   - R36 (c) gives V_{σ′}(v) ⊴ V_σ(v) = Ξσ(v) for every positional Even σ′ of H. So the cycle node of the (σ′, σ̄)-play from v has reward
     ≤ reward(λ(v)) ≤ −1: it is odd.
   - Suppose some play from v consistent with σ̄ had an even outcome. Step 1 in H gives a positional σ′ with an even cycle node at v,
     contradicting the previous line.
   - So σ̄ wins every play from v: V ∖ W ⊆ W_O(G), with σ̄ as the witness.
4. Regions and restriction.
   - Steps 2-3 give W ⊆ W_E and V ∖ W ⊆ W_O. W_E ∩ W_O = ∅: if both players had a strategy winning every consistent play from v, the
     one play consistent with both would be won by both. So W = W_E and V ∖ W = W_O. Determinacy is not assumed; it follows.
   - A σ-consistent play from v ∈ W never enters u ∈ V ∖ W. Otherwise Odd steers the play to u and then follows σ̄. From u the (σ, σ̄)-play
     ends in the cycle of λ(u), whose most relevant vertex has odd priority. The whole play is consistent with σ and has an odd outcome,
     against step 2.
   - Likewise a σ̄-consistent play from v ∉ W never enters w ∈ W. From w the (σ, σ̄)-play ends in the even cycle of λ(w), against step 3.
   - So σ on W and σ̄ on V ∖ W (SPEC S5) are winning strategies on their regions, and plays under them stay in the region. □
- Class audit, per step (Lead 02:49Z): every cited item, and its class.
| step | what it cites | class of the cited item |
| --- | --- | --- |
| 0 | SPEC S1 definition: rank, p′, reward | a definition on every game |
| 1 | nothing cited: finite-graph argument (inf set strongly connected; simple cycle through its top; shortest path to it) | any finite game graph |
| 2 | (VJ): SPEC S1 definition of Ξσ (optimal σ̄); its source VJ00 (11) (§5.2, Prop. 5.1, Lemma 5.2, p. 16); carried in the record as R18 (d) Lemma S (a) and R21 (a)'s parenthetical; and step 1 on G_σ | VJ00 (11): every finite game (VJ00 §2). R18 (d) S (a), R21 (a): signed in 𝒞^1O, proofs game-general (N-1O-4; REFEREE §C DUAL C.2); this packet asks to sign (VJ) on every game |
| 3 | R36 (c) on H := G_σ̄; SPEC S1 definition (Ξσ = valuation of the (σ, σ̄)-play); SPEC S2 definition (Iσ); step 1 on G_σ̄ | R36 (c): every one-player game; G_σ̄ is one-player for every G |
| 4 | steps 2-3; SPEC S1 definition (cycle node = most relevant vertex of the cycle); SPEC S5 (the output) | definitions; no class |
- Not used anywhere: the number of choice vertices of either player, Iτ, any N5 run property except "Iσ = ∅ at the stop", R21 (a)'s main
  inequality Ξ_k ⊴ W_k, and R18 (d) Lemma S (b)-(d).
- Relation to P-N5-1O §4 (RESULTS R51 (d)): the same proof, with these changes:
  - the class hypothesis is dropped;
  - OUT-1 is built in (step 0);
  - (VJ) is cited from its source, VJ00 (11), as N-1O-4 advised, beside R18 (d) S (a) and R21 (a);
  - the observation that Iτ = ∅ is not needed;
  - a proof that W_E ∩ W_O = ∅.
  P-N5-1O §4's READING "the same proof gives S5's correctness on every game" becomes this lemma.

## 3. Lemma BIT-G (PROVED, every game): R51 (c) holds on every game
Statement (RESULTS R51 (c), with "on 𝒞^1O" dropped): with valuations stored as (a vertex, an n-bit path-set vector indexed by rank, a length
≤ n), compared by cycle-node reward, then the top differing bit, then length (SPEC S1, Q1), one N5 iteration and the final output step cost
O(n³(n + m)) word operations on O(log(n + m))-bit words and O(n)-bit vectors on every parity game; no big integers. REFEREE-2's N-1O-3:
O(n(n + m)) words plus O(n²) vector bits per S1 run; the stated bound is loose.
Proof. P-N5-1O §3's proof (with BIT-N1: S1 (iv)'s recursion is memoised), read for class use, line by line:
- Representation and comparison (Q1): about SPEC's valuations on any game.
- One S1 run: the loop over cycle nodes, steps (i)-(vi), each a DFS, reverse search, restricted-graph search, longest path (Q3: the
  restricted graph minus v is acyclic on every game, by Q3's own argument, which cites only S1's loop order and VJ00 §6 Prop. 6.1 clause 4),
  BFS, or vector copy. Every step is on an arbitrary arena (G_σ, its restrictions, or a dual arena with the same n, m).
- One N5 iteration: ≤ 4 S1 runs (Ξσ on G, Ξτ on G^d, the S4a and S4b arenas) plus O(m·n) bits for S2 and S4c. S3 (FIX 1): O(m) comparisons.
  S5: one S1 run plus O(n).
- No step names o, d_o, 𝒞^1O, or any count of choice vertices. So the proof holds verbatim on every game. □

## 4. Theorem 1E-POLY (PROVED): N5 on 𝒞^1E from any start pair
Statement. Let G ∈ 𝒞^1E with n vertices, m edges, Δ := max out-degree, e its Even choice vertex and d_e := deg(e). From any start pair
(the S3 start included), N5 stops after at most
    ITER ≤ (n(n − 1) + d_e)·(T*(n, m, Δ, d_e) + 1) = O(m·Δ·d_e·n¹³)
iterations. With m ≤ n² and Δ, d_e ≤ n: ITER ≤ (n(n − 1) + d_e)(L(n) + 1) = O(n¹⁷), L(n) := T*(n, n², n, n) = O(n¹⁵).
Cited text of P-N5-DUAL §1 (signed, both referees), verbatim:
- MIRROR (a): "On 𝒞^1E, along any N5 run σ changes at most d_e − 1 times, and the run has at most n(n − 1) + d_e dual phases."
- MIRROR (b): "Hypothesis (H-OF), NOT proved here: there is L(n) such that for every 𝒞^1O game with n vertices and every start pair, the
  FIRST phase of the N5^OF run from that start pair has at most L(n) transitions. Under (H-OF), N5 on every 𝒞^1E game with n vertices,
  from every start pair, makes at most (n(n − 1) + d_e)(L(n) + 1) iterations."
- MIRROR (c): "(H-OF) follows from (H-N5): 'for every 𝒞^1O game with n vertices and every start pair, the first phase of the N5 run has at
  most L(n) transitions'."
Proof.
1. (H-N5), per game. Let H ∈ 𝒞^1O with parameters (n, m, Δ, d_o). Every phase of every N5 run on H, from every start pair, has at most
   T*(n, m, Δ, d_o) transitions. This is step 3 of R51 (a)'s proof (P-N5-1O §2, step 3):
   - f ≤ 2n² = F in every phase, by R48 (i) (a)-(c);
   - R50 (h)'s chain is non-decreasing in f;
   - this holds from every start pair by R51 (b) (start-freeness: R-N5-START with Addendum 1, R2-N5-1O §3).
   The first phase of the run from a start pair x is a phase of that run, so it has ≤ T*(n, m, Δ, d_o) transitions.
2. Monotonicity. T*(n, m, Δ, d) is non-decreasing in m, Δ and d: every term of the chain is a sum of products of non-negative quantities,
   and m − n + 1 ≥ 1 because every vertex has a successor (m ≥ n). So for every 𝒞^1O game on n vertices,
   T*(n, m, Δ, d_o) ≤ T*(n, n², n, n) = L(n). This was checked by REFEREE in R-N5-DUAL §C C.2.
   So (H-N5) holds with L(n). By MIRROR (c), (H-OF) holds with the same L(n). By MIRROR (b), ITER ≤ (n(n − 1) + d_e)(L(n) + 1).
   This gives the uniform form.
3. Parameter form. MIRROR (b)'s proof applies (H-OF) to ONE game only, G^d. Put L := T*(n, m, Δ, d_e).
   - Per-game quantities of G^d substituted into R51 (a)'s T* (Lead 02:49Z):
     | R51 (a) parameter (of a 𝒞^1O game) | value for G^d | why |
     | --- | --- | --- |
     | n = \|V\| | n (G's) | G^d has the same vertex set (DUAL §0: "same ids and successor lists") |
     | m = #edges | m (G's) | same successor lists |
     | Δ = max out-degree | Δ (G's) | same successor lists |
     | o, d_o = deg(o) | o := e, d_o(G^d) = d_e | owners swapped: G^d's Odd choice vertices are G's Even choice vertices, so G^d ∈ 𝒞^1O with o = e |
     | f (in-phase fallbacks), F := 2n² | F = 2n² | R48 (i), inside R51 (a)'s step 3; depends on n only |
     Nothing else of the game enters T*. R51 (a)'s phase count n(n − 1) + d_o is NOT used; the phase count here is MIRROR (a)'s.
   - Step 1 bounds every N5 phase of every run on G^d, from every start pair, by L. So the first N5 phase from every state of G^d is ≤ L.
   - MIRROR (c)'s proof is per game and per state x: the first N5^OF phase from x on G^d is a prefix of the first N5 phase from x, or
     equal to it. So it is also ≤ L.
   - MIRROR (b)'s proof is also per game:
     - by Lemma DUAL (first sentence), the N5 run on G is the mirror of the N5^OF run on G^d;
     - the dual phases of the former are the phases of the latter, and there are ≤ n(n − 1) + d_e of them (MIRROR (a));
     - each is the first N5^OF phase from its first state (N5^OF is memoryless), so it has ≤ L transitions;
     - there are ≤ n(n − 1) + d_e − 1 boundary transitions.
   - Every iteration is a transition (R15 (d)). So ITER ≤ (n(n − 1) + d_e)(L + 1).
   - Where monotonicity of T* is used:
     - parameter form (this step): only in f, inside R51 (a)'s step 3 (f ≤ F; R50 (h)'s chain non-decreasing in f, as R51 (a) states);
     - uniform form (step 2): also in m, Δ and d, to replace G^d's (m, Δ, d_e) by (n², n, n).
4. Orders. T* = O(m·Δ·d·n¹¹) (P-N5-1O §2 step 5, with d for d_o). So ITER = O(n² · m·Δ·d_e·n¹¹) = O(m·Δ·d_e·n¹³). With m ≤ n² and
   Δ, d_e ≤ n this is O(n¹⁷), and L(n) = O(n¹⁵) (REFEREE-2 N-DUAL-3). □
- 𝒞^1O ∩ 𝒞^1E (one choice vertex per player) is covered twice; either bound holds.
- The bound is loose and unoptimised. It is not a growth law. DATA (§7): at most 7 iterations on 4,016 𝒞^1E runs (n 4-30).

## 5. Corollary 1E-TIME (PROVED)
On 𝒞^1E, N5 from any start pair (the S3 start included) does the following:
- It outputs W_E(G), W_O(G) and positional winning strategies for both players: σ on W_E, σ̄ on W_O (Lemma OUT-G).
- It does so after ≤ ITER iterations (Theorem 1E-POLY), each costing O(n³(n + m)) word operations (Lemma BIT-G).
- With the output step and the O(n log n) priority ranking, the total is O(ITER · n³(n + m)) = poly(n + m) word operations on
  O(log(n + m))-bit words, i.e. polynomial time at bit cost (TARGET.md §3).
- Input: TARGET.md §1's encoding. The class test (exactly one Even vertex of out-degree > 1) costs O(n + m).

## 6. Not to sign (READING)
- G-N5T-3 (RESULTS R15 (iii): "N5's output correctness at S5 rests on VJ00 Lemma 5.8 '1 ⇒ 2', which uses VJ00's unproved Lemma 5.9 and
  Prop. 5.10").
  - If OUT-G is signed, the output-correctness half of gauntlet step 4 holds for N5 on EVERY game. Its premises are VJ00 (11) (§5.2,
    proved in VJ00 from §5.1) and R36 (c), not Lemma 5.8, 5.9 or Prop. 5.10.
  - R51 (d) already closed G-N5T-3 on 𝒞^1O. Whether to close the gap row is the Lead's and the referees' call.
  - The running-time half stays OPEN for general games (G-N5-TIME).
- Gauntlet status for the SUBCLASS 𝒞^1E (TARGET.md §5):
  - steps 1-3: as R51's table; N5 is the same object.
  - step 4: running time by this packet with R51 and P-N5-DUAL; correctness by OUT-G.
  - Lean: not done, and not needed (not an M4 claim).
  - step 5: after the referees.
- Scope (as P-N5-DUAL §1, READING): 𝒞^1E contains games with arbitrarily many Odd choice vertices, so the polynomial bound covers a class
  where Odd's positional strategies are exponentially many. Even's are ≤ d_e, so the class is still polynomial by other means.
- Frontier: games with two or more choice vertices for each player, 𝒞^(≥2E,≥2O), where every known exponential strategy-improvement
  family lies (L-NEW 22, DATA). Nothing here transfers there as proved: MIRROR (a)'s σ-count and the whole 𝒞^1O chain fail as bounds.
- Honest limits:
  - (i) The time bound is for a SUBCLASS that is polynomial by other means.
  - (ii) It rests on R51 and everything R51 cites (R15, R18 (d), R21, R36, R47, R48, R50), and on P-N5-DUAL (R54, landing).
  - (iii) The objects are SPEC's N5 and SPEC's S1. That S1's procedure computes an optimal counterstrategy is SPEC's requirement, sourced in
    VJ00. The code's match to SPEC is DATA (R15 G-N5T-1).
  - (iv) The data are thin for long runs: random 𝒞^1E runs are short.

## 7. Data (DATA, not proof): experiments/si/out16/outcheck.py
Own checker, with N5 from experiments/new/n5.py run() (read-only import) and own Zielonka. At each stop it checks from definitions:
- (Z) W = Zielonka's W_E;
- (SE) σ on W's Even vertices keeps every play in W, with no odd-top cycle;
- (SO) the same for σ̄ on V ∖ W;
- (B) on 𝒞^1E, ITER ≤ the §4 bound.
Starts: S3 for even-numbered games, random start pairs for odd-numbered ones; lib41 from S3 and one random pair.
| set | runs | 𝒞^1E runs | violations | max ITER |
| --- | --- | --- | --- | --- |
| random, any class, n 4-14 (seed 11) | 3,000 | 368 | 0 | 7 |
| random 𝒞^1E, n 4-14 (seed 12) | 3,000 | 3,000 | 0 | 6 |
| random 𝒞^1E, n 15-30 (seed 13) | 1,000 | 1,000 | 0 | 7 |
| experiments/new/box41/lib41.txt (412 files, any class), S3 + 1 random | 824 | 16 | 0 | 115 |
| mutation control MUT=1 (output read at the START pair), any class, n 4-14 (seed 14) | 1,000 | 130 | 773 (must fail; it does) | — |
Logs: experiments/si/out16/logs/. Reproduce: `python3 -I experiments/si/out16/outcheck.py --rand 3000 4 14 11 any` (and the other rows'
arguments in experiments/si/out16/README.md); each row runs in about a minute.
