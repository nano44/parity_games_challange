# Referee packet P-N5-1O: N5 solves one-Odd-choice parity games in polynomial time (iterations, bit cost per iteration, output correctness) — a subclass result, not a TARGET.md claim
Author: L-SI successor 10 (Opus 5.5; D15, D18, L37, L40), session_01PBqfsNWMhTPn7yNJ8C18HP. Written at the Lead's request of 23:40Z
(Lead's stamp). DRAFT until the Lead says RESULTS R50 (P-N5-KW) has landed; FROZEN once its sha1 is reported. Stamp: the commit (date -u).
- Labels (D18 / L40): PROVED (L-SI 10, from landed results only) / READING / DATA. D1: wrong until checked.
- Scope: the candidate N5 (SPEC S1-S5, docs/new/N5-ssi-global.md) on 𝒞^1O, the games in which exactly one Odd vertex o has out-degree > 1.
  𝒞^1O is polynomial by other means (e.g. Odd has ≤ d_o positional strategies), so the value here is the METHOD. This is NOT a TARGET.md
  §2 claim, which is about all parity games (TARGET.md §4: "Polynomial only on a restricted class" does not count as M4).

## 0. What to sign
| § | statement | label | to sign |
| --- | --- | --- | --- |
| §2 | Theorem 1O-POLY: from any start pair, N5 makes ≤ P(n, m, d_o, Δ) iterations, P explicit | PROVED | yes |
| §3 | Lemma BIT: one N5 iteration, and the final output step, cost O(n³(n + m)) word operations on O(log(n + m))-bit words and O(n)-bit vectors, i.e. polynomially many bit operations | PROVED | yes |
| §4 | Lemma OUT: at N5's stop (Iσ = ∅), SPEC S5's output is the pair of winning regions with positional winning strategies (𝒞^1O) | PROVED | yes |
| §5 | Corollary 1O-TIME: on 𝒞^1O, N5 from any start pair outputs (W_E, W_O) and positional winning strategies in time polynomial in n + m at bit cost | PROVED | yes |
| §6 | gauntlet status for the subclass | READING | no |
| §7 | MIRROR's extension to 𝒞^1E (P-N5-DUAL, in review); the frontier | READING | no |

## 1. Cited landed results (exact statement text and hypotheses)
| result | statement (as in docs/RESULTS.md) | class | start pair |
| --- | --- | --- | --- |
| R15 (c), (d) | (c) "≺ is a strict partial order on strategies and every non-empty switch of improvements goes strictly up in ≺"; (d) "every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and changes at least one of them … Hence no (σ, τ) state repeats and N5 terminates" | every game | any (SPEC) |
| R47 (b) Φ-1O | "(a) along any N5 run τ changes at most d − 1 times …; (b) a run has at most n(n − 1) + d phases" (d := deg(o); phase := maximal run with (λ, τ) constant) | 𝒞^1O | any run |
| R48 (i) FB-POLY | "with f the number of in-phase Even S4c fallbacks of a phase of N5 on 𝒞^1O, (a) if o ≠ c_θ, … f ≤ 1 + (|U| − 2)(|succ(o) ∩ Û| + |U|) ≤ 1 + (n − 2)(2n − 1); (b) if |U| = 2, f ≤ 1; (c) if o = c_θ, f ≤ |U|" | 𝒞^1O, every phase | any |
| R50 Corollary PHASE (P-N5-KW §8 with fixes) | "Let a phase on 𝒞^1O have f fallback transitions. Then its transitions number T ≤ (m − n + 1)(T_rel + 1)", with T_rel ≤ S_o + N_Ξ, N_Ξ ≤ f + (N_st − 1) + (X + 1)(n − 1) + (N_st + f)·3Δn⁴, N_st ≤ 1 + X + Θ + W_ch, and X, Θ, S_o, W_ch bounded by landed R30 (c), R34 (e), (f), R27 (g), R24 (e), R22 (a) as listed there; CONDITIONAL on f only | 𝒞^1O, every phase | any |
| R36 (c) Lemma P1 | "if σ is a positional Even strategy of a one-player game H with no improving edge (no Even edge (x, y) with V_σ(y) ▷ V_σ(σ(x))), then V_σ(v) ⊵ V_{σ′}(v) for every positional Even strategy σ′ and every vertex v" (one-player: every non-Even vertex has one successor; V_σ the play valuation) | any one-player game | — |
| R21 (a) Lemma XW | "Ξ_k ⊴ W_k pointwise at every state (Odd's best reply σ̄_k is pointwise optimal in G_{σ_k})" | 𝒞^1O | any |
- SPEC (docs/new/N5-ssi-global.md) is the object, not a cited result: S1 (valuations and the procedure, with Q1-Q4 and FIX 2-4), S2, S3, S4,
  S5. Code: experiments/si/si.py Engine.evaluate (l. 78-205), experiments/new/n5.py run().

## 2. Theorem 1O-POLY (PROVED)
Statement. Let G ∈ 𝒞^1O with n vertices, m edges, d_o := deg(o), Δ := max out-degree. From any start pair, N5 stops after at most
    ITER ≤ (n(n − 1) + d_o)·(T* + 1)
iterations, where T* is R50's bound with f := F := 2n² and the landed bounds of R50's chain:
    T_H := n² + 2n − 1;  X_SN := 13(d_o + 1)n³(F + 1 + T_H) + T_H;  X := (F + 1)(n − 1) + F + X_SN;
    Θ := (n − 1) + n(X + 1) + X;  S_o := d_o(Θ + 1);  W_ch := (F + X + 1)n²;  N_st := 1 + X + Θ + W_ch;
    N_Ξ := F + N_st + (X + 1)(n − 1) + (N_st + F)·3Δn⁴;  T* := (m − n + 1)(S_o + N_Ξ + 1).
So ITER = O(m·Δ·d_o·n¹³) ⊆ O(n¹⁸), a polynomial P(n, m, d_o, Δ).
Proof.
1. Every iteration is a transition: it changes σ or τ (R15 (d)). So ITER is the number of transitions of the run; it is finite (R15 (d)).
2. The states split into at most n(n − 1) + d_o phases (R47 (b)). A transition either has both ends in one phase, or ends a phase; the
   latter number ≤ (#phases − 1).
3. In each phase, f ≤ max(1 + (n − 2)(2n − 1), |U|, 1) ≤ 2n² = F (R48 (i) (a)-(c); |U| ≤ n). Every bound in R50's chain is non-decreasing
   in f, so the phase has ≤ T* transitions (R50).
4. So ITER ≤ (#phases)·T* + (#phases − 1) ≤ (n(n − 1) + d_o)(T* + 1).
5. Orders: X_SN, X = O(d_o n⁵); Θ, S_o = O(d_o² n⁶) ⊆ O(d_o n⁷); W_ch, N_st = O(d_o n⁷); N_Ξ = O(Δ d_o n¹¹); T* = O(m Δ d_o n¹¹); times
   O(n²) phases. With d_o, Δ ≤ n and m ≤ n², O(n¹⁸). □
- The bound is loose and unoptimised (R47's data: at most 30 phases in any run; no iteration-count growth law is claimed here).

## 3. Lemma BIT (PROVED): one iteration costs polynomially many bit operations
Model: TARGET.md §3 (word RAM, words of O(log(n + m)) bits; numbers longer than a word cost their bit length).
Representation (SPEC S1, Q1): a valuation is (cycle node, path set, length) = (a vertex index, an n-bit vector, an integer in [0, n]).
- No big integers are needed. Two valuations are compared by the rewards of their cycle nodes, then by the top differing bit of the path sets
  (Q1: equivalent to SPEC's signed-weight phrase), then by the length. That costs O(n) bit operations.
- si.py compares through the n-bit signed weight Σ ±2^rank; that is an n-bit integer, so also O(n) bits per comparison and O(n²) per weight
  (cached). Either way, n-bit, not unbounded.
Statement. With n, m as above and priorities already ranked (rank(v) = position of v in V sorted by (Ω(v), v), S1; O(n log n) word
operations once), one evaluation of SPEC S1's procedure (si.py Engine.evaluate) costs O(n³(n + m)) word operations, counting an
operation on an n-bit vector as O(n) word operations. One N5 iteration (SPEC S4: two evaluations, Iσ and Iτ, at most two restricted
evaluations, the S4c fallback) and the final output (S5: one evaluation) cost O(n³(n + m)) word operations too.
Proof. By the steps of S1 for one evaluation (si.py l. 86-204):
- Graph set-up (successor / predecessor lists of G_σ): O(n + m).
- The outer loop runs over the n vertices v in reward order. For each v:
  - (i) the cycle test: one DFS over alive vertices of lower rank, O(n + m);
  - (ii) R := the alive vertices reaching v: one reverse search, O(n + m); the restricted lists hs, hp: O(n + m).
  - (iii) for each u ∈ R ranked above v (≤ n of them):
    - one search for M, O(n + m);
    - ≤ n path-set updates (setting bit rank(u) in an n-bit vector: O(n) bit operations each, so O(n²));
    - edge deletions: each restricted edge is removed at most once per u, at O(Δ) per removal (list remove), so O(m·Δ) ⊆ O(n·m).
    - Per u this is O(n(n + m)); per v, O(n²(n + m)).
  - (iv) lengths: memoised longest path (each vertex computed once; the "state" guard makes the recursion halt even if a cycle were
    present, si.py l. 157-160; Q3 shows it is not), or BFS: O(n + m). Lengths are ≤ n.
  - (v) the cycle node's own choice: one DFS, O(n + m).
  - (vi) assignment: ≤ n valuations, each copying an n-bit vector: O(n²).
- Total per evaluation: n · O(n²(n + m)) = O(n³(n + m)) word operations (the n-bit vector operations included at O(n) each).
- One iteration (n5.py run(); SPEC S4):
  - two evaluations (G and G^d; G^d has the same n, m);
  - Iσ and Iτ: ≤ m comparisons, O(n) each;
  - each restricted arena: built in O(n + m), evaluated once (n ≤ n, edges ≤ m);
  - the S4c fallback: ≤ m comparisons;
  - the termination test (Iσ = Iτ = ∅).
  - Total O(n³(n + m)).
- The start (S3: O(m) comparisons of ranks) and the output (S5: one evaluation, then reading the parity of each cycle node and the strategy
  entries) are within the same bound.
- Every number other than the n-bit path vectors is an index, a rank, a reward (|p′| ≤ 2n + 1) or a length ≤ n: one word. □
- Remark. VJ00 (BRICS RS-00-48) Theorem 6.2 states O(n·m) per improvement step for its own shared-work procedure. si.py does not reach
  that; Lemma BIT bounds the procedure as specified and implemented. Not needed for polynomiality.

## 4. Lemma OUT (PROVED): the stop is correct
Statement. Let G ∈ 𝒞^1O, and let N5 stop at state (σ, τ) (SPEC S5: Iσ = Iτ = ∅). Put λ(v) := the cycle node of Ξσ(v), W := {v : Ω(λ(v))
even}, and σ̄ := Odd's best reply computed by S1 at this state. Then W = W_E(G) and V \ W = W_O(G); σ wins for Even from every v ∈ W against
every (history-dependent) Odd strategy; σ̄ wins for Odd from every v ∉ W against every Even strategy.
Proof.
1. A one-player cycle fact. Let H be a game graph in which one player's choices are fixed, so only the other player moves. If some infinite
   play of H from v has max-parity outcome p (the highest priority seen infinitely often), then some positional strategy of the mover
   gives a play from v whose play value has a cycle node of priority parity p.
   - The vertices seen infinitely often induce a strongly connected subgraph D containing a vertex t of priority p, with all priorities in D
     at most p. Take the top-ranked such t (its parity is p's).
   - Inside D there is a simple cycle C through t. Every vertex of C has priority ≤ p, so t is C's top and C's cycle node.
   - Take a shortest path from v to C. The mover's positional strategy follows that path, then C. Its play is this lasso, with cycle node t.
2. Even's side. Let v ∈ W, so reward(λ(v)) > 0 (λ(v) even).
   - By R21 (a), σ̄ is pointwise optimal for Odd in G_σ: for every positional Odd strategy τ′, val(σ, τ′)(v) ⊵ Ξσ(v).
   - Valuations compare cycle-node rewards first, so the cycle node of val(σ, τ′)(v) has reward ≥ reward(λ(v)) > 0: it is even.
   - If some play consistent with σ from v had an odd outcome, step 1 in H := G_σ (Odd moves) would give a positional τ′ with an odd cycle
     node at v. Contradiction. So every play consistent with σ from v is won by Even.
3. Odd's side. Let v ∉ W, so reward(λ(v)) < 0.
   - H := G_σ̄ (Odd fixed to σ̄) is a one-player game. σ's play valuation there is the (σ, σ̄)-play value, which is Ξσ (SPEC S1; VJ00 (11),
     Ω_σ = Θ_{σσ̄}, as used for R21 (a)). So σ's improving edges in H are exactly Iσ (S2, the same values), and Iσ = ∅ at the stop.
   - R36 (c) gives V_{σ′} ⊴ V_σ = Ξσ at v for every positional Even σ′ of H. So the cycle node of (σ′, σ̄)'s play from v has reward
     ≤ reward(λ(v)) < 0: it is odd.
   - If some play consistent with σ̄ from v had an even outcome, step 1 in H gives a positional σ′ with an even cycle node at v.
     Contradiction. So every play consistent with σ̄ from v is won by Odd.
4. Steps 2-3 show W ⊆ W_E and V \ W ⊆ W_O. Since W_E ∩ W_O = ∅, W = W_E and V \ W = W_O.
   - SPEC S5 outputs σ on W and σ̄ on V \ W. A σ-play from v ∈ W never enters u ∈ V \ W. Otherwise Odd could steer the play to u and
     then play σ̄. From u the (σ, σ̄)-play ends in the odd cycle of λ(u), so this σ-consistent play from v has an odd outcome, against
     step 2.
   - Likewise a σ̄-play from V \ W never enters W: from w ∈ W the (σ, σ̄)-play ends in the even cycle of λ(w), against step 3.
   - So the restricted strategies are well defined on their regions and winning. □
- This removes, ON 𝒞^1O, R15's outside gap G-N5T-3 ("output correctness at S5 rests on VJ00 Lemma 5.8 '1 ⇒ 2'").
  - The proof uses only R36 (c) (one-player games) and R21 (a), which give the needed half of Lemma 5.8.
  - READING (not to sign): R21 (a)'s parenthetical is a general fact about S1's σ̄ (VJ00 (11)), so the same argument would work on every
    game. A referee should confirm R21 (a)'s proof does not use 𝒞^1O before that reading is used.

## 5. Corollary 1O-TIME (PROVED)
On 𝒞^1O, N5 from any start pair (the S3 start included) outputs W_E(G), W_O(G) and positional winning strategies for both players after
≤ ITER iterations (§2), each costing O(n³(n + m)) word operations (§3). With the output step and the O(n log n) priority ranking, the
total is O(ITER · n³(n + m)) = poly(n + m) word operations on O(log(n + m))-bit words, i.e. polynomial time at bit cost (TARGET.md §3).
- Input: TARGET.md §1's encoding. Priorities are ranked by sorting. The class test (exactly one Odd vertex of out-degree > 1) costs O(n + m).
- Correctness: Lemma OUT. Termination and the bound: Theorem 1O-POLY.

## 6. Gauntlet status (READING; TARGET.md §5; for the SUBCLASS 𝒞^1O only)
| step | status for N5 on 𝒞^1O |
| --- | --- |
| 1 exact pseudocode and one implementation | done: SPEC (docs/new/N5-ssi-global.md), experiments/new/n5.py on si.py |
| 2 agreement with Zielonka (10,000 random games, hard families), growth plotted | done for N5 on general games (L-NEW STEP-2 report, R15 "Gauntlet"); the 𝒞^1O runs are a subset. Second implementation: L-COMP (in progress per R15) |
| 3 barrier statement, L-LIT sign-off | done for N5 (L-LIT T20, with caveats, per R15); not specific to 𝒞^1O |
| 4 correctness and running-time proofs, double-refereed | running time: this packet + landed R15, R47, R48, R50; correctness: Lemma OUT (this packet). Lean: NOT done (needed only for an M4 claim; not applicable) |
| 5 CHECKER on the exact commit, owner told | after the referees |
- What this does NOT do:
  - It makes no TARGET.md §2 claim: the class is restricted (TARGET §4, first bullet), and polynomial by simpler means.
  - It says nothing about games with ≥ 2 Odd choice vertices, where Φ-1O's τ-count (d − 1) fails as a bound and FB-POLY, X, KW use 𝒞^1O
    throughout.
  - It does not give positional strategies from τ (S5 outputs σ̄, as SPEC says).

## 7. Not to sign (READING)
- MIRROR / 𝒞^1E (P-N5-DUAL, L-NEW 22, in review): the dual class (one Even choice vertex) by the symmetric argument. Not used here.
- Frontier: games with two or more choice vertices of each player, 𝒞^(≥2E,≥2O) (L-NEW 22's map). There, the phase count (τ-chains of
  length up to h(≺_{G^d})) and every 𝒞^1O-specific lemma (FB-POLY, FRZ-U's R, KW) need new arguments. Nothing here transfers as proved.
