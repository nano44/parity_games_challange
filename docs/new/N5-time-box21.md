# N5 on two-player games: box 21, from R57's obstruction to a bound, and where it breaks
L-NEW successor 8 (Opus 5.5, D15). Lead GO 2026-10-23 23:05Z; started 23:06Z; this draft 23:20Z (date -u).
Status: proof attempt on GAPS G-N5-TIME. Every statement is labelled PROVED, READING or OPEN; DATA is labelled as such.
Not refereed. No polynomial bound is claimed. G-N5-TIME stays OPEN.
Object: N5 = docs/new/N5-ssi-global.md SPEC S1-S5 (code experiments/new/n5.py, run unmodified). Sources: Vöge-Jurdziński BRICS
RS-00-48 (pdf sha256 485a12de…, as in RESULTS R15/R17); R57 = docs/red/R57-n5-lanes.md (L-RED successor 12).

## 0. Result in one paragraph
- A bound would need two statements; neither is proved.
  - (FO) Fixed opponent: N5's Even moves while Odd's τ stays constant are polynomially many.
  - (ALT) Alternation: Odd's τ changes polynomially often.
  - With both, N5 is polynomial (Theorem B, §2.4, PROVED). R57's O1-O4, and the brief's route "(R-a) and (R-b) are
    incompatible", address (ALT) only.
- (FO) is not settled by RESULTS R17, even when τ is frozen at Odd's OPTIMAL strategy τ*. Two reasons:
  - Even's gate is honest, i.e. computed against Odd's fresh best reply σ̄. Even's selection is against τ*.
  - R17's proof transfers exactly when the gate contains every edge that is improving against τ* (Lemma PT, §2.6, PROVED).
- That inclusion is FALSE (§3.1):
  - a 9-vertex hand instance;
  - 131 of 4,504 such edges on random runs (DATA);
  - 8 such edges at once on fts_ph16.
- On fts_ph16 (n = 16) the R17 conclusion itself fails for a genuine N5 run from (σ_0, τ*) (DATA, Oink-verified, §3.2):
  - 22 value-changing iterations in ONE joint λ-phase, against the one-player bound n − 1 = 15;
  - Lemma P (one-player, in G_τ*) is violated at 18 of the 22 steps (steps 4-21).
- Consequence for the obstruction (READING, §3.3): R57's requirement (R-a), counters in BOTH strategies, is not necessary for a
  kill. A single Even counter can live in Even's gate, whose best-replier σ̄ IS fresh every iteration, while τ = τ* never moves.
  So "(R-a) ∧ (R-b) incompatible", even if proved, would not bound N5. The open core is (FO*) (§5).

## 1. Setting and notation
- V_{σ,τ}(v): the S1 valuation (c, P, ℓ) of the play from v under the pair (σ, τ). Order ⊴ = Even's order of S1.
- L_σ := Ξσ (Even's honest valuation, against σ̄). Iσ is Even's gate: edges (v, w) with Ξσ(w) ▷ Ξσ(σ(v)).
- U_τ := Odd's honest valuation Ξ^d_τ on G^d, read in G's order (Lemma R).
- A(σ) := Even's arena in S4a: v may use {σ(v)} ∪ {w : (v, w) ∈ Iσ}. Odd is fixed to τ.
- W_k := V_{σ_k, τ}: the play values against a fixed τ, i.e. values in the one-player game G_τ.
- Frozen dynamics F_τ (Even only; τ fixed; stops when Iσ = ∅):
  - σ' := the S4a step against τ;
  - if σ' = σ: σ' := the S4c Even switch-all on Iσ ("fallback step"; otherwise an "arena step").
- H_k := R17's one-player arena in G_τ: x may use {σ_k(x)} ∪ {z : W_k(z) ▷ W_k(σ_k(x))}.

## 2. PROVED statements
### 2.1 Lemma R (the dual order is the reverse order)
For plays t1, t2 of G (equivalently of G^d, the same vertex sequences): t1 is better than t2 in G^d's S1 order iff t1 is worse
than t2 in G's S1 order.
Proof (from S1 alone).
- G^d has Ω + 1, so rank^d = rank: the sort key (Ω + 1, v) orders V exactly as (Ω, v). Also p'^d(v) = 2·rank(v) + 1 − (Ω(v) mod 2).
- Relevance (p' order) is the rank order in both games, so a play has the same triple (c, P, ℓ) in G and G^d.
- Cycle nodes. In G, the G-even nodes are positive and increase with rank; the G-odd nodes are negative and decrease with rank.
  In G^d the G-odd nodes are positive and increase with rank, and the G-even nodes are negative and decrease with rank. Each of
  the three comparison cases (both G-even, both G-odd, mixed) reverses.
- Path sets. The sign of each 2^rank term is the parity of Ω, which flips, so weight^d = −weight.
- Length. "Longer is better iff c is odd" flips with c's parity. □

### 2.2 Lemma S (sandwich; N5's step is a gated best response)
(a) L_σ(v) = min over τ' of V_{σ,τ'}(v), and U_τ(v) = max over σ' of V_{σ',τ}(v), pointwise.
- The first is VJ00 (11) (σ̄ is a best counter-strategy, pointwise; R17 (F1)).
- The second is the same fact on G^d, read through Lemma R.
(b) Hence L_{σ_k} ⊴ V_{σ_k,τ_k} ⊴ U_{τ_k}. L_{σ_k} is non-decreasing in k and U_{τ_k} is non-increasing, both pointwise:
RESULTS R15 (a) on G and on G^d, with Lemma R.
(c) Arena steps.
- σ_{k+1} maximises V_{·,τ_k} pointwise over A(σ_k) (R17 (F1), on the one-player arena). So V_{σ_{k+1},τ_k} ⊵ V_{σ,τ_k} for every
  σ ∈ A(σ_k), in particular for σ_k itself.
- If A(σ_k) contains a best reply to τ_k, then V_{σ_{k+1},τ_k} = U_{τ_k}.
- Odd's step is symmetric: τ_{k+1} minimises V_{σ_k,·} over Odd's arena.
(d) N5's Even step dominates SSI's Even step against τ_k, in the order of play values against τ_k: V_{σ^N5_{k+1},τ_k} ⊵
V_{σ^SSI_{k+1},τ_k} pointwise.
- SSI's switched strategy (Iσ ∩ τ̄_k) lies in A(σ_k). This is the value form of K6 (N5-dlm-box5.md §4).
- It says nothing about iteration counts. □

### 2.3 Lemma Φ (joint λ-phases)
Each vertex's cycle node in L_σ changes at most n − 1 times in a run. The same holds for the cycle node in Ξ^d_τ.
So a run has at most 2n(n − 1) + 1 joint λ-phases.
Proof.
- By R15 (a), L_{σ_{k+1}} ⊵ L_{σ_k}, and the cycle-node reward is the first key component, so it never decreases.
- Rewards are injective on vertices, so each change of cycle node strictly increases it.
- The same argument applies on G^d. □
(This is R17's phase count, now for both players' honest valuations.)

### 2.4 Theorem B (block decomposition)
Let C_τ be the number of N5 iterations that change τ. Let F_E(G) be the maximum length of an F_τ run, over all Odd strategies
τ and all starting σ.
(a) If τ_{k+1} = τ_k, then σ_{k+1} = F_{τ_k}(σ_k).
- If Iσ ≠ ∅, S4a computes the same σ', and S4c falls back on Even exactly when F does. (When σ' = σ and τ' = τ, S4c switches Even
  because Iσ ≠ ∅.)
- If Iσ = ∅, the iteration needs Iτ ≠ ∅. Then either S4b changes τ, or S4c falls back on Odd and changes τ. Either way
  τ_{k+1} ≠ τ_k.
(b) So every maximal τ-constant block is a prefix of an F_τ run, followed by one τ-changing iteration. Hence:
    N5 iterations ≤ (C_τ + 1)·(F_E + 1),
and symmetrically ≤ (C_σ + 1)·(F_O + 1).
(c) If τ_0 is honest-optimal (Iτ_0 = ∅), then τ never changes (Iτ depends on τ alone, S2 on G^d), and the N5 run IS the F_{τ_0}
run, step for step.
Corollary.
- N5 is polynomial ⇐ (FO) F_E ≤ poly(n) ∧ (ALT) C_τ ≤ poly(n).
- An N5 run from a start pair (σ_0, τ*) with τ* honest-optimal is super-polynomial ⇔ the F_τ* run is.
- With τ* equal to S3's best-reward start τ_0, that is the canonical run. □

### 2.5 Lemma W (W along a frozen run)
In an F_τ run:
- every arena step has W_{k+1} ⊵ W_k pointwise (R17 (F1)/(F2): σ_k ∈ A(σ_k));
- every fallback step has W_{k+1} ⊴ W_k pointwise. A fallback fires only when the VJ procedure returns σ_k as the arena optimum,
  and S4c's strategy lies in A(σ_k), so (F1) gives domination by σ_k.
DATA: in 1,500 random games (n 4..12, 969 steps from (σ_0, τ*), 52 of them fallbacks), W never decreased. So the fallbacks were
W-flat (wmono.py). That W-flatness of fallbacks is OPEN.

### 2.6 Lemma PT (R17 transfers exactly when the gate contains G_τ's improving edges)
Let ρ_0, …, ρ_k be consecutive ARENA steps of an F_τ run, all in one λ_W-phase (λ_W = cycle nodes of W, i.e. of the one-player
game G_τ). Suppose A(ρ_j) ⊇ H_j for each j < k. Then R17's Lemma P holds in H = G_τ: W_k(x) ⪰ value(r) for every simple path
r of ≤ k edges from x to a cycle node of ρ_0. Hence (R17 Theorem PH, first half) at most n − 1 W-changing arena steps per such
stretch.
Proof: R17's proof (N5-phase-bound-box10.md §2) word for word. Its "Facts used: (F1), (F2). Nothing else about the rule is used."
- Case A uses only the order and (F2), which holds by Lemma W.
- Case B needs ρ̂ = ρ_j[x → z] to lie in the arena when (x, z) is improving in G_τ. That is the hypothesis A(ρ_j) ⊇ H_j.
- (F1) for the optimum of the larger arena gives Ω_{j+1}(x) ⪰ val_ρ̂(x), as there. □
So the ONLY place where the one-player argument needs the rule is the inclusion "every G_τ-improving edge is honest-improving".
Call it (H1).

## 3. Where it breaks: (H1) is false, and so is the conclusion of Lemma P, against the optimal opponent
### 3.1 (H1) is false (PROVED by instance; DATA on rates)
- Hand instance experiments/new/box21/instances/h1_hand.pg with start h1_hand.start. Vertices (priority, owner):
  - x (0, E) → {b, z}; b (0, E) → t4; z (0, E) → o; o (0, O) → {t6, y}; y (0, E) → {t1, t10};
  - t_p (priority p) self-loops.
  - τ*(o) = t6; Iτ* = ∅, checked.
  - σ: x → b, y → t1.
  - Against τ*: W(z) = (t6, ∅, 2) ▷ W(b) = (t4, ∅, 1), so (x, z) is G_τ*-improving.
  - Honestly, σ̄(o) = y punishes, because y → t1 is Even's own bad choice: Ξ(z) = (t1, ∅, 3) ◁ Ξ(b). So (x, z) is NOT in Iσ.
  - N5 first repairs y (y → t10), then takes (x, z): one step of delay.
- Mechanism. If (x, z) is improving against τ* but not honestly, then Ξ(z) ◁ Ξ(σ(x)) ⊴ W(σ(x)) ◁ W(z). So z is EXPLOITABLE (Ξ(z) ≠ W(z)):
  σ̄ deviates from τ* on z's play, because Even plays badly somewhere downstream. The edge opens only after that repair.
  Repairs can chain: x waits for y, y waits for y', …
- Random runs (h1.py, 3,000 games, n 5..14, N5 from (σ_0, τ*)): 131 of 4,504 G_τ*-improving edges were outside the gate.
  An earlier 400-game sample (n 4..10) had 0 of 322; the violations need n ≳ 10.
- fts_ph16 (§3.2): 8 G_τ*-improving edges outside the gate at the start, and some at every state until the last two.

### 3.2 R17's conclusion fails against τ* (DATA, verified)
experiments/new/box21/instances/fts_ph16.pg (n = 16, sha1 55a21ee52e59cd13aa307080be902d2cb0f095fa), start file fts_ph16.start.
- The start pair is (σ_0 = best-reward, τ* = the final τ of the plain N5 run); Iτ* = ∅, so Odd never moves.
- n5.py from that start pair: 22 iterations (3 fallbacks). Oink zlk OK, strategies verified (check_sol2.py).
- The plain run takes 12 iterations.
- All 22 iterations lie in ONE joint λ-phase (cycle node 8 for every vertex, honest and W). All 22 are value-changing: Ξσ changes
  at each one, and W changes at each one.
- One-player bound (R17 Theorem PH): n − 1 = 15.
- Lemma P in G_τ*, checked over all simple paths (lamw.py): violated at 18 of the 22 steps, steps 4-21 (139 violating
  (x, path) pairs at step 15). Example at step 20: vertex 1 is below a 3-edge path to the cycle node 8.
- The R17 count measured on σ̄-segments (box 10's measure) gives segments of [3, 14, 2, 1, 2]. So the excess is not a σ̄-segment
  effect. Every segment is ≤ 15; the excess comes from the gate across segments.
Climb table (climb_fix.py, fitness = max N5 iterations inside one joint λ-phase of the run from (σ_0, τ*); filled at the box end):
see §6.

### 3.3 What this does to R57's obstruction (READING)
- O1 (no lapping) and O2's formal core (Iτ is a function of τ alone) are PROVED facts (R15, S2).
- O2's conclusion "from then on N5 is Even against a fixed τ: a one-player-type run" is not a one-player run.
  - The gate is computed against σ̄, Odd's FRESH best reply, which changes with σ.
  - The selection is against τ.
  - R17 needs the gate to contain G_τ's improving edges (Lemma PT), and it does not (§3.1).
- O3's premise "each flip must be an honest improvement of the OPPONENT" concerns τ. But the fresh best-replier that Friedmann's
  counters need exists inside Even's own valuation even when τ is frozen.
- So a super-polynomial N5 run needs (ALT fails) OR (FO fails), by Theorem B. (R-a) ∧ (R-b) is a requirement for the first
  branch only. The second branch needs NO counter in τ: τ = τ* honest-optimal and frozen, with an Even counter throttled
  through σ̄.
- (R-b) has an analogue there:
  - the gate must withhold every jump-ahead switch that would be profitable against τ*;
  - by §3.1, an edge can be withheld only while its head z is exploitable (Ξ(z) ≠ W(z)), i.e. while some Even choice downstream
    of z is bad against σ̄.

## 4. The (ALT) side: R-a, R-b
- Formal (R-a): C_τ (Odd's changes) super-polynomial. With Theorem B, a kill on this branch needs C_τ super-polynomial while
  every block is short.
- R57's per-vertex data (§6 of R57) and its symmetric climbs fit this: returns occur, and counts stay linear.
- Attempted incompatibility proof (OPEN, where it stops).
  - Lemma S gives two monotone envelopes L_σ ↑ and U_τ ↓ around the actual play values.
  - An Odd return at u (a → b → a) needs Ξτ(a) and Ξτ(b) to cross twice. Both rise (Odd order), and nothing bounds how often
    two rising sequences in an exponential-size order can cross.
  - The coupling is only through the selection (Lemma S (c)): Odd's step is a gated best reply to σ_k.
  - For a bounded number of crossings one would need a joint potential that rises at every Odd return. The natural candidates
    are V_{σ_k,τ_k}, L, U and the gap U − L. L and U are monotone but count value changes, and there can be exponentially many.
    V_{σ_k,τ_k} is not monotone: Even's and Odd's steps pull it in opposite directions in the same iteration.
  - So no route from O1-O4 to a bound on C_τ is in sight. And by §3 such a bound would not suffice anyway without (FO).

## 5. OPEN statements, sharpest first
- (FO*) For every game and every honest-optimal τ*, the F_τ* run (= N5 from (σ, τ*)) has poly(n) iterations.
  - It is necessary for G-N5-TIME from start pairs, and for the canonical start whenever S3's τ_0 is honest-optimal
    (Theorem B (c)).
  - Smallest sub-question: a bound on W-changing arena steps per λ_W-phase. On fts_ph16 it is 22 > n − 1.
- (FO) The same for arbitrary frozen τ (needed for Theorem B with blocks).
- (ALT) C_τ ≤ poly(n) in N5 runs.
- (WF) Fallback steps of F_τ are W-flat (DATA 52/52).

## 6. Data and files
experiments/new/box21/ (read-only use of n5.py and si.py):
- n5x.py: trace (asserts equal counts with n5.run).
- fixtau.py: plain vs frozen-τ* vs Even switch-all.
- climb_fix.py: climbs, modes tstar, tstarph, bestph, tany.
- anal.py, phases.py, wtrace.py, lamw.py: per-step analysis and the Lemma P check.
- h1.py: random H1 rates. wmono.py: Lemma W data.
- instances/: h1_hand, fts_ph16, plus starts.
Frozen τ* on Friedmann's families (fixtau.py; N5 from (σ_0, τ*) vs plain N5 vs Even switch-all from σ_0):

| game | n | plain N5 | N5 from (σ_0, τ*) | Even switch-all from σ_0 |
| --- | --- | --- | --- | --- |
| switchallexp N 2..5 | 35/49/63/77 | 8/7/8/10 | 8/8/8/10 | 30/70/150/310 |
| switchbestexp N 2..5 | 60/85/110/135 | 32/41/47/55 | 13/19/25/31 | 61/141/301/621 |
| vc_g25 / seg_r16 | 25/16 | 27/16 | 4/4 | 3/6 |
| sym_h8_s1 / sym_h16_s1 | 16/32 | 25/55 | 4/6 | 5/13 |

Frozen τ* is linear on all of these; the long frozen runs come from climbs (§3.2).
