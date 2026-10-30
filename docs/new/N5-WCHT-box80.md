# N5-WCHT (box 80): D18 on [P-WCHτ]. The W-side structure alone (lex-monotone W, one-player optimal steps, fixed λ_W, private-prefix payment) allows 2^k values at one vertex (ladder_k, n = 2k + 2). Any proof must use the Ξ-offer rule; Lemma TWIN-SYNC is the first piece of it
L-NEW successor 37 (Opus 5.5), D14 / D18, Lead reading L40. Lead brief (after 08:52Z), TASK 2: «D18 on [P-WCHτ] itself. Per-vertex W is
lex-monotone (cycle node, path-set bit vector, length) inside a W-run, and every strict W-rise of v needs a switch on v's private prefix
(L-RED's PREFIX / TWO-SOURCE, l-red 1c8d8667 notes "Successor 32 PARK"). So bound the number of distinct monotone values a vertex can take
under that prefix constraint, with an import from combinatorics on monotone sequences / sorting networks / VC-type bounds, or your own idea.
Proof or exact obstruction with an instance.» Written 2026-10-30 from ~09:25Z (date -u). Working note, unrefereed, not a TARGET.md claim.
G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Definitions as in docs/new/P-N5-WCH-box79.md §1 (W_t, W-run, λ_W, [S1-ord], Fact LEX, S4a step, H_t, A(v)). [P-WCHτ](w): every τ-stretch S
  and vertex e have WCH_S(e) ≤ w(n) (P-N5-WCH §1).
- Source read: l-red 1c8d8667 (= trunk) docs/red/R132-reader-tree.md §2 (Lemmas TWO-SOURCE, PREFIX, the 2-wide LADDER remark: «there is no
  counting obstruction. The obstruction is dynamic … a flip at level j needs a DESYNCHRONISATION at level j − 1»). Lane proofs there, not
  landed; used as the question, not as a proof step.
- Tools: experiments/new/box80/ladder.py (builds ladder_k, finds the schedule by exhaustive DP, verifies it with the fleet's valuation engine
  experiments/si/si.py Engine). Instances experiments/new/box80/inst/ladder_K.pg + ladder_K.seq, K = 2, 3, 4, 5, 6, 8.

## 1. The relaxation R0, and why a W-side bound is impossible
R0 is what the Lead's question gives a proof to work with, inside one W-run F (τ fixed, no S4c, λ_W fixed):
- (R0-a) W is pointwise non-decreasing along F (R91 W-MON);
- (R0-b) each step σ_t → σ_{t+1} is the pointwise one-player optimum of an arena that contains σ_t (S4a: H_t = σ_t ∪ Iσ_t);
- (R0-c) λ_W is constant;
- (R0-d) consequences of (a)-(c): PREFIX (an order flip between two options needs a switch on a private prefix) and TWO-SOURCE.
R0 says nothing about WHICH edges are offered: in N5 the offers are Iσ_t, fixed by Ξ_t; in R0 they are arbitrary.

### 1.1 Proposition LADDER (PROVED, lane; with DATA verification)
- The game ladder_k (one-player: every vertex is Even; n = 2k + 2). Vertex 0 is a sink with a self-loop and priority 0. For j = 1..k and
  b ∈ {0, 1}, u(j, b) has priority 2(2(k − j) + b) + 2: all priorities are even and distinct, a deeper level (smaller j) is more relevant,
  and copy 1 is above copy 0 in its level. Level 1 goes to the sink; u(j, b) for j ≥ 2 has successors {u(j − 1, 0), u(j − 1, 1)}. The top
  T has priority 1 and successors {u(k, 0), u(k, 1)}.
- Statement. For every k ≥ 1 there is a sequence of single switches σ_0 → σ_1 → … (σ_0: every vertex takes copy 0), each switching one
  vertex v to a W_t-improving successor (W_t(w) ▷ W_t(σ_t v); the new strategy is then the pointwise optimum of σ_t ∪ {(v, w)}, R15 (a)),
  such that W is pointwise non-decreasing, λ_W ≡ 0, and W(T) takes all 2^k values of its path sets in increasing order: 2^k − 1 strict
  rises at one vertex, n = 2k + 2. Each step is one improving switch, so (R0-a)-(R0-d) all hold.
- Values. Every play ends in the sink, more relevant vertices are all of the ladder, and two plays from one vertex have equal length. By
  Fact LEX the path from a vertex is compared by the deepest level where the copies differ, and copy 1 wins there (even, higher rank). So
  the value of u(j + 1, ·) pointing at u(j, b) is the binary number 2x_b + b, x_b the number of u(j, b)'s own below-path (deepest level =
  most significant bit), plus the reader's own fixed marker.
- Proof (induction on the level, a LEAD-FOLLOW schedule). Claim C(j): with switches only at levels 2..j, the pair (x_0, x_1) of the two
  level-j vertices can be driven through (0, 0), (1, 0), (1, 1), (2, 1), (2, 2), …, (N_j − 1, N_j − 1), N_j = 2^{j−1}, each change one
  improving switch, all values monotone. C(1) holds with N_1 = 1 (no switch). Assume C(j). The two readable values for level j + 1 are
  {2x_0, 2x_1 + 1}, two consecutive integers in every state of C(j)'s schedule: {2x, 2x + 1} when x_0 = x_1 = x, {2x + 2, 2x + 1} when
  x_0 = x + 1, x_1 = x. Run the readers A := u(j + 1, 0) (leader) and B := u(j + 1, 1) (follower): while the window is {r, r + 1}, A switches
  to the vertex showing r + 1, then B does (each switch is a strict rise of the switcher: improving); then C(j) advances the vertex that
  NEITHER reader points to (both now sit on the one showing r + 1), so no reader's value moves except by its own switch. The readers' pair
  goes (0, 0), (1, 0), (1, 1), (2, 1), …, (2N_j − 1, 2N_j − 1): that is C(j + 1) with N_{j+1} = 2N_j. At the top, T is a single reader of
  level k and reads 0, 1, …, 2N_k − 1 = 2^k − 1 the same way. Every switch is improving at its vertex, and in a one-player game an
  improving switch makes W pointwise non-decreasing (R15 (a)). □
- DATA (ladder.py; the schedule is found by an exhaustive DP over all states, i.e. it is a LONGEST one, then replayed on the .pg with the
  fleet's Engine): k = 2, 3, 4, 5, 6, 8: T-rises 3, 7, 15, 31, 63, 255 = 2^k − 1 (n 6, 8, 10, 12, 14, 18); 0 non-improving switches;
  0 monotonicity violations; cycle nodes {0}. The DP optimum equals 2^k − 1, so the lead-follow schedule is optimal there.
  experiments/new/box80/inst/ladder_8.pg + ladder_8.seq (749 switches) is the pinned instance.

### 1.2 DEAD, and the exact obstruction
- DEAD: "a polynomial bound on per-vertex W-changes in a W-run from (R0-a)-(R0-d)". Instance: ladder_k, 2^k − 1 W-rises at T in one
  relaxed W-run, n = 2k + 2 (pinned ladder_8: 255 at n = 18).
- Exact obstruction. PREFIX charges each flip of a reader to a switch on a private prefix, and TWO-SOURCE asks for two rising streams. The
  ladder meets both with ONE shared lower ladder: the two level-j vertices are the two streams, and they stay one step apart (lead-follow),
  so the readable window {2x_0, 2x_1 + 1} always holds two consecutive values. Each level doubles: N_{j+1} = 2N_j. The counting is the
  2-wide ladder of R132 §2, now with a proof that R0 realises it at every k.
- Imports, as templates only (none opened, none cited as a result):
  - monotone-sequence bounds (Erdős–Szekeres / Dilworth type) bound monotone SUBsequences of arbitrary sequences; here the whole
    sequence is monotone, so they give nothing;
  - VC / Sauer–Shelah type bounds count a family of sets by its VC dimension; T's path sets in ladder_k shatter the k level choices
    (all 2^k occur), VC dimension k = Θ(n), so a shatter-function bound is exponential;
  - sorting networks: the lead-follow pair is an odd-even transposition of two counters; it is the doubling, not a bound.
  So no bound on DISTINCT MONOTONE VALUES can come from W's side. A proof of [P-WCHτ] must use the offer rule Iσ_t (Ξ).

## 2. What N5 has that R0 lacks: Lemma TWIN-SYNC (PROVED, lane; N5, every game)
- Statement. Let t → t + 1 be an S4a step, τ := τ_t, W′ := W^τ_{t+1}. Let v, v′ be Even with succ(v) = succ(v′) and σ_t(v) = σ_t(v′),
  both not their own W′-cycle node at t + 1. Then W′(σ_{t+1} v) = W′(σ_{t+1} v′).
- Proof. Put d := σ_t(v) = σ_t(v′). [S4a]: A(v) = {d} ∪ {w : (v, w) ∈ Iσ_t} and [S2]: (v, w) ∈ Iσ_t iff w ∈ succ(v), w ≠ d and
  Ξ_t(w) ▷ Ξ_t(d). The same holds for v′, so A(v) = A(v′). H_t's edges at v are A(v). RESULTS R90 (a) (ii) (OPT-OFF) at v: W′(y) ⊴
  W′(σ_{t+1} v) for every y ∈ A(v), in particular y = σ_{t+1}(v′) ∈ A(v′) = A(v). Symmetrically at v′. □
- Consequence for ladders. In ladder_k (or any game where a level's two copies have one successor set) the lead step «A switches while B,
  on the same successor, stays» cannot be an N5 S4a step: the offer is the same for both, and both end on W′-equal successors. Their values
  are then marker ⊕ (the same successor value), whose order is fixed by the markers: the next level never flips. So N5 must desynchronise
  through DIFFERENT current successors (an earlier lag) or DIFFERENT successor sets (a gate): exactly R132's "desynchronising gate".
- DATA: N5 itself on ladder_4 / ladder_8 from the all-copy-0 start: 1 iteration, W(T) takes 2 values (one-player: S4a takes the global
  optimum; RESULTS R17).
- Corollary (PROVED, lane). Under N5, the relation "same successor set and same current successor" between two Even vertices, once it
  holds at t, gives W′-equal successors at t + 1; with N5-LZC's keep rule (P-N5-WCH §7.1) both keep or both switch to W*-equal targets.
  (Not iterated here: equal successor values do not give equal Ξ of the successors, so a later offer can differ. That is where a
  desynchronising gate enters.)

## 3. READING and the next target (CONJECTURE, stated precisely)
- Every route to [P-WCHτ] must constrain the OFFERS. The offers in a W-run are Iσ_t = {(v, w) : Ξ_t(w) ▷ Ξ_t(σ_t v)}: one global potential
  Ξ_t, pointwise non-decreasing (R15), below W_t (XW). Call R1 the relaxation "R0 plus: offers are {(v, w) : X_t(w) ▷ X_t(σ_t v)} for some
  pointwise non-decreasing X_t ⊴ W_t, and σ_{t+1} is the one-player optimum of σ_t ∪ offers" (X free otherwise).
- CONJECTURE R1-POLY (OPEN, the precise next target): in R1, every vertex's W changes at most poly(n) times in a W-run. If FALSE (an R1
  ladder with an X schedule), the instance tells exactly what Ξ must do, and that is a design spec for L-RED (Ξ's freedom comes only from
  Odd choice vertices where σ̄ ≠ τ, P-N5-WCH's TXC sources SBAR / WIT). If TRUE, [P-WCHτ] reduces to "Ξ is an R1 schedule", which it is.
- What is NOT done: R1-POLY is untested (the X schedule space is large; a search needs a bounded X alphabet, e.g. X-ranks per vertex). No
  N5 instance with super-linear WCH_F(e) is known (DATA max per (W-run, edge) returns 17 at n 210, P-N5-WCH §8.4).

## DONE / FINDINGS / NEEDS
- DONE: experiments/new/box80/ladder.py; inst/ladder_{2,3,4,5,6,8}.pg + .seq; this note; check.sh "box 80" (ladder_6 replay).
- FINDINGS:
  1. PROVED (lane) Proposition LADDER, with DATA: under the W-side structure alone (monotone W, one-player-optimal steps, λ_W fixed,
     PREFIX / TWO-SOURCE) one vertex takes 2^k values in one relaxed W-run, n = 2k + 2 (ladder_8: 255 rises at n = 18; DP-optimal).
  2. DEAD: a bound on distinct monotone W-values from R0. Exact obstruction: lead-follow pairs on a shared lower ladder double per level;
     monotone-sequence and VC-type imports give nothing (the family shatters Θ(n) choices).
  3. PROVED (lane) Lemma TWIN-SYNC (N5, every game): two Even vertices with one successor set and one current successor get W′-equal
     successors at an S4a step. This is the first offer-side constraint; it kills the ladder's lead step for twins.
  4. CONJECTURE R1-POLY (open): the precise next target (offers from one monotone potential X ⊴ W).
- NEEDS: none from the owner.
