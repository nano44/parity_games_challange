# N5 on two-player games: box 21, from R57's obstruction to a bound, and where it breaks
L-NEW successor 8 (Opus 5.5, D15). Lead GO 2026-10-23 23:05Z; started 23:06Z; first draft 23:20Z, §3.4 23:29Z, final §6 01:34Z Oct 24 (date -u).
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
- The canonical start shows it too (DATA, Oink-verified, §3.4): fts_best16 (n = 16).
  - Odd has ONE vertex with a choice, and S3's τ_0 is already optimal, so τ never moves.
  - 27 value-changing iterations fall in one joint λ-phase.
  - Odd's best reply σ̄, which defines Even's gate, makes TWO laps over four exits inside that phase, and Even vertices
    return (8 → 15 → 8 → 15 → 8).
  - Lapping is impossible for σ and τ (R15) but not for σ̄.
- On the class 𝒞^1O (one Odd choice vertex), Lemma G (§3.5, PROVED) locates the whole difference between honest gate and
  selection. They disagree only on edges ENTERING the reach set R of o, through one monotone scalar θ = Ξ(o).
  - The remaining statements are (SEG-1O) and (CH-1O) (§3.6), and both fail to follow from R17 at the same "trust-mode
    deadlock".
- Frozen runs split at changes of σ̄ (§3.7, DATA). Both factors can exceed linear:
  - fts_g29 (n 29): 66 steps in one phase, from 13 σ̄ changes with segments ≤ 10;
  - fts_best24 (n 24, canonical, τ frozen): 33 value-changing steps in ONE σ̄-segment, above n − 1.
  - So (FO*) is K9's decomposition with τ removed, and neither of its factors is bounded.
  - With R58's Theorem W (checked here, conditional on (P)), a long frozen run must also be wide.
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
DATA for (a) and Lemma R (sandwich_check.py, brute force over all strategies):
- 400 random games, n ≤ 6, 1,610 vertex checks, 0 mismatches.
- L_σ(v) equals the minimum over all τ' of V_{σ,τ'}(v).
- The dual valuation's triple, read with G's key, equals the maximum over all σ' of V_{σ',τ}(v).

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
DATA for (a)-(b) (blockcheck.py): 1,500 random plain N5 runs (n 3..14), 1,465 τ-constant blocks; every block's σ-sequence is a
prefix of F_τ from the block's first σ (0 mismatches).

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
Climb table: §6.

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

### 3.4 The canonical start, one Odd choice vertex (DATA, verified; 23:29Z by date -u)
experiments/new/box21/instances/fts_best16.pg (n = 16, sha1 5534245f603f496d1e6122d7be1fff81f05088fd), canonical N5 (best-reward
start, no start file).
- Odd has ONE vertex with a choice: vertex 5, priority 10, successors {2, 4, 5, 9, 14, 15}. S3's τ_0(5) = 9 is honest-optimal
  (Iτ_0 = ∅), so by Theorem B (c) the canonical run IS the frozen run, and τ never changes.
- n5.py: 28 iterations (2 fallbacks). Oink zlk OK, strategies verified. Joint λ-phases [1, 27]: 27 iterations in one phase, all
  value-changing (Ξσ and W change at every step). One-player bound: n − 1 = 15.
- Mechanism, seen in the trace. Odd's best reply σ̄(5), which defines Even's gate, runs through the exits
  9 → 14 → 15 → 4 → 2 → 14 → 15 → 4 → 2 → 9. That is TWO laps over four exits inside one λ-phase, with τ(5) = 9 fixed throughout.
  Even vertices return in the same phase:
  - 14: 8 → 15 → 8 → 15 → 8;
  - 3: 13 → 4 → 2 → 7 → 13 → 4 → 7 → 4 (7 switches);
  - 1: 1 → 10 → 15 → 4 → 15.
  This is the lapping that R57 §1 says N5 cannot have through τ (O1). Here it happens through σ̄, which R15 does not constrain
  (R15 says σ and τ never recur; σ̄ may).
- READING. The smallest class where (FO) is open is 𝒞^1O: games in which Odd has at most one vertex of out-degree > 1.
  - There C_τ ≤ d − 1, because τ is one choice at that vertex and never repeats (R15 (c): every τ change goes strictly up in
    ≺ on G^d). So by Theorem B, N5 is polynomial on 𝒞^1O ⇐ F_E is polynomial on 𝒞^1O.
  - Conversely, from every start pair (σ, τ*) with τ* honest-optimal, N5 IS the F_τ* run (Theorem B (c)).
  - The class is solvable in polynomial time by other means (d one-player games). A bound would be about N5 itself, as R17 is.
  - R17's argument does not cover the class (fts_best16).

### 3.5 Lemma G: on 𝒞^1O the gate differs from G_τ's only on edges ENTERING o's reach set (PROVED; DATA check)
Setting: o is the only Odd vertex with a choice, τ is fixed, σ is Even's current strategy. Let:
- R := {v : the σ-path from v reaches o} (o ∈ R);
- π_v := that path from v up to o, o excluded;
- π ⊕ a := (c(a), P(a) ∪ {u ∈ π : u more relevant than c(a)}, ℓ(a) + |π|), the prefix of R17 §1 along a whole path.
Hypothesis (h): o lies on no cycle of the (σ, σ̄)-play or of the (σ, τ)-play from o, and Ξ(o), W(o) have the same cycle node c.
(This holds throughout a joint λ-phase in which every vertex's cycle node is the same sink s, e.g. the 27-step phase of
fts_best16.)
(a) If v ∉ R, then Ξ(v) = W(v). The σ-path from v meets no Odd vertex with a choice before it closes, so the two plays coincide.
(b) If v ∈ R, then Ξ(v) = π_v ⊕ Ξ(o) and W(v) = π_v ⊕ W(o). The play from o avoids π_v; otherwise o would lie on a cycle,
    contradicting (h).
(c) For y, z ∈ R: Ξ(z) ▷ Ξ(y) ⇔ W(z) ▷ W(y).
    - Both comparisons see the same cycle node c. Their path-set difference is A_z Δ A_y, where A_v = {u ∈ π_v : u more relevant
      than c}; this set is disjoint from the paths of Ξ(o) and W(o).
    - Their length difference is |π_z| − |π_y|.
    - Neither depends on which value at o is used.
(d) For an Even x and z ≠ σ(x): (x, z) ∈ Iσ ⇔ (x, z) is improving in G_τ, with exactly two exceptions:
    - (d1) σ(x) ∉ R and z ∈ R (the edge ENTERS R): here (x, z) ∈ Iσ ⇒ improving in G_τ, but not conversely. The edge is withheld
      iff π_z ⊕ Ξ(o) ⊴ W(σ(x)) ◁ π_z ⊕ W(o).
    - (d2) σ(x) ∈ R and z ∉ R (the edge LEAVES R): improving in G_τ ⇒ (x, z) ∈ Iσ, but not conversely.
    Proof: (a)-(c), Ξ(o) ⊴ W(o) (Lemma S (b)), and prefix monotonicity (R17 (V2)) along π_z, with the same cycle node. □
Corollary.
- On 𝒞^1O, (H1) fails only on edges entering R, and only while Ξ(o) ◁ W(o), i.e. while Odd's best reply at o beats τ(o) against
  the current σ.
- At every state with Ξ(o) = W(o), the gate contains G_τ's improving edges, so Lemma PT's inclusion holds at that state.
- The throttle is ONE number: Ξ(o) = o ⊕ (the minimum honest value over o's exits outside R). It rises monotonically
  (R15 (a)). An edge into R opens once that minimum is high enough.
DATA (lemmaG.py):
- fts_best16: 28 states; 80 withheld edges, all of type (d1); 30 extra edges, all of type (d2).
- oneodd_c24 (n 24): 22 states satisfying (h); 82 withheld, all (d1); 2 extra, all (d2).
- R follows forced Odd vertices (out-degree 1). That was fixed in lemmaG.py before these counts; the random games have none.
- 2,000 random 𝒞^1O games (n 5..14, runs from (σ_0, τ*)): 2,246 states satisfying (h); 15 withheld, all (d1); 5 extra, all (d2).

### 3.6 𝒞^1O: what is left, and where the one-player induction stops (READING with DATA)
Fix a stretch of N5 iterations in which τ, θ := Ξ(o), w := W(o) and the joint λ-map are all constant, and (h) holds. By Lemma G, inside the
stretch:
- the gate is the improving set of the one-player game G^θ (o made a terminal of value θ);
- each step is the optimum of the one-player game G^w (o a terminal of value w ⊵ θ) over that gate.
The two games differ only in how attractive it is to route through o. So the run splits as:
    #iterations ≤ (#θ-changes + #w-changes + #τ-changes + #λ-changes + 1) · (longest (θ, w, τ, λ)-constant stretch),
with #τ-changes ≤ d − 1 (§3.4) and #λ-changes ≤ 2n(n − 1) (Lemma Φ). On 𝒞^1O it is therefore enough to prove:
- (SEG-1O) a (θ, w, τ, λ)-constant stretch has ≤ n − 1 value-changing steps (plus flat ones);
- (CH-1O) θ and w change poly(n) times.
Neither is proved.
DATA (theta.py, canonical runs):

| instance | n | iterations | θ-changes | (w or λ)-changes | Odd moves | longest (θ, w, τ, λ)-stretch |
| --- | --- | --- | --- | --- | --- | --- |
| fts_best16 | 16 | 28 | 10 | 2 | 0 | 11 |
| oneodd_c16 (climb_fix.py oneodd; sha1 827976e2…) | 16 | 36 | 11 | 18 | 2 | 5 |
| oneodd_c24 (climb_fix.py oneodd; sha1 559434eb…) | 24 | 44 | 5 | 14 | 1 | 11 |

The longest stretch is ≤ n − 1 in every case. On 𝒞^1O the length comes from the number of stretches, not from long stretches. A climb with fitness "longest stretch − (n − 1)" (climb_fix.py seg1o) is reported
in §6.
Where the R17 induction stops inside a stretch. Two different one-player inductions both fail, each at one edge type of Lemma G (d).
- (i) In W (G^w): Lemma P's Case B fails at a withheld entering edge (x, z) (type d1). Its repair would need the honest bound
  Ξ_k(z) ⪰ value(r') for z's o-avoiding continuation r'. Then "withheld" would give value(r') ⪯ π_z ⊕ θ ⊴ W(σ(x)), and Case A's
  argument would go through.
- (ii) In Ξ (G^θ): that honest bound fails exactly at z ∈ R in "trust mode". There z's W-optimal route goes through o (because of
  w) while its honest value π_z ⊕ θ is below its best o-avoiding route. N5 keeps z in R because the selection trusts τ.
- So x is withheld by z, and z stays in R until θ rises (the end of the stretch).
- (iii) A third attempt (00:05Z by date -u): a joint induction.
  - It carries, for o-paths r of ≤ k edges, "W_k(x) ⪰ π_r ⊕ θ" (W beats the HONEST value of every short o-path).
  - It adds, for z ∈ R_k, "z's route to o is at least as good as every o-path of ≤ k edges" (route progress). Route progress
    holds for R→R edges: Lemma G (c) makes them unthrottled, and the arena optimum is route-optimal among R-routes.
  - The withheld case of the first statement reduces to the second: π_{r'} ⊕ θ ⪯ π_z ⊕ θ ⊴ W(σ(x)).
  - It breaks one level down. The route of z may pass through y with y ∉ R_k because y's own entering edge is withheld. Then
    z cannot follow that route, and route progress fails for z. The throttle propagates along routes.
  - Recorded so that a successor does not repeat it.
- A proof of (SEG-1O) has to count such deadlocks. A proof of (CH-1O) has to bound the releases. This is the exact point where
  the one-player argument stops on the smallest two-player class.

### 3.7 With L-RED's Theorem W (R58 §2), and the σ̄-segment structure of frozen runs (written 23:44Z by date -u)
- Theorem W (R58 §2, L-RED, unrefereed): conditional on (P), VJ00 Lemma 5.8 "1 ⇒ 2", the same premise as R15 G-N5T-3.
  - Checked here line by line: Lemma 1 (equal improving sets ⇒ equal valuations, via (P) in G minus the common set), Lemma 2
    (R15's φ bounds a flat stretch), and the counting.
  - No gap found. It uses no property of the selection, so it applies verbatim to F_τ runs (R58 §7, Corollary W2).
  - So a super-polynomial frozen run needs gate width ≥ log(T/4n²)/log m_E at all but polynomially many moves.
- Widths on the long frozen runs (width.py; Even moves by |Iσ|):

  | instance | n | Even moves | width 1 / 2 / 3 / 4..8 / ≥ 9 | gated G_τ-improving edges refused |
  | --- | --- | --- | --- | --- |
  | fts_ph16 (σ_0, τ*) | 16 | 22 | 12 / 2 / 5 / 3 / 0 | 2 |
  | fts_best16 (canonical) | 16 | 28 | 11 / 2 / 10 / 3 / 2 | 12 |
  | fts_g29 (σ_0, τ*) | 29 | 66 | 11 / 17 / 8 / 19 / 11 | 15 |
  | oneodd_c24 (canonical) | 24 | 44 | 18 / 8 / 2 / 12 / 4 | 19 |

  - The growth climb's run (fts_g29) is no longer a narrow repair chain: 30 of 66 moves are at width ≥ 4.
- experiments/new/box21/instances/fts_g29.pg (n = 29, sha1 58b69e82e2981ace74603576ca7771ef933a9a54, start fts_g29.start; grow.py
  from fts_ph16), N5 from (σ_0, τ*):
  - 66 iterations (6 fallbacks), all in ONE joint λ-phase and all W-changing;
  - one-player bound n − 1 = 28;
  - Oink zlk OK, strategies verified. The plain run takes 18.
- Where the excess comes from (READING with DATA).
  - In a frozen run the only fresh coupling left is σ̄, Odd's best reply inside Even's honest valuation. While σ̄ = c is constant,
    the gate is the improving set of the one-player game G_c, and the selection is against τ*.
  - Split each phase at σ̄ changes. Segment lengths:
    - fts_ph16: [3, 14, 2, 1, 2], with 4 σ̄ changes;
    - fts_best16: [1, 1, 1, 2, 11, 4, 1, 2, 2, 3], with 9 changes;
    - fts_g29: max 10, with 13 changes.
    On these three every segment is ≤ n − 1, and the length comes from σ̄ changing often.
  - BUT segments can be long too. experiments/new/box21/instances/fts_best24.pg (n = 24, sha1
    af9ca6c63f91928718f121acc7722dd337780cfc; climb_fix.py bestph):
    - canonical start; Odd has two choice vertices (11, 12); S3's τ_0 is honest-optimal, so τ never moves;
    - 43 iterations (3 fallbacks), all in one joint λ-phase, all value-changing;
    - σ̄ changes ONCE. The first σ̄-segment has 33 value-changing Even moves (32 by phases.py, which counts the iteration
      that changes σ̄ in the next segment), above n − 1 = 23;
    - n5.py 43 iterations; Oink zlk OK, strategies verified.
    This is box 10's (SEG-LEN) failure (vc_g25: 26 > 24, with τ moving), now with τ frozen at the optimum and from the canonical
    start. Inside a σ̄-segment the gate is G_c's improving set (c = σ̄), the selection is against τ ≠ c, and the K1 stalls of
    box 10 §5 delay it.
  - So in frozen runs both factors can exceed linear: the number of σ̄ changes (fts_g29: 13) and the segment length
    (fts_best24: 33 > 23). This is K9's decomposition
    (N5-oneplayer-box7.md: iterations ≲ poly × (best-reply changes)) in its cleanest setting: τ is gone and σ̄ is the only
    opponent.
  - The open question for (FO*) is therefore the one box 11 left open (N5-brchanges-box11.md): how often can σ̄ change along
    Even's honest chain? It has no valuation-level invariant (box 11) and no width bound beyond Theorem W.
- Growth of the frozen-τ* phase excess (grow.py, fitness = phase length − (n − 1), vertices added on the way): see the table in
  §6. Phase length / n² falls from 0.086 (n 16) to 0.065 (n 43), and phase length / n rises from 1.4 to 2.8. That is a climb's
  envelope, not a family. Superlinear growth is NOT established.

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
- Update after R58 (L-RED successor 13; checked in §3.7). Given (P), Theorem W settles the BOUNDED-WIDTH part of the
  incompatibility: R-a + R-b at width O(1) gives poly(n) iterations, whatever the mechanism (R58 §5).
  - What remains on the ALT side is wide moves, where the mover has ω(1) honest improving edges and N5's optimum refuses most
    of them. That is L-RED's (STRETCH) + (K3).
  - On the FO side the same width condition holds (Corollary W2). The frozen-τ* runs above are not narrow (§3.7), and their
    excess comes from changes of σ̄.

## 5. OPEN statements, sharpest first
- (FO*) For every game and every honest-optimal τ*, the F_τ* run (= N5 from (σ, τ*)) has poly(n) iterations.
  - It is necessary for G-N5-TIME from start pairs, and for the canonical start whenever S3's τ_0 is honest-optimal
    (Theorem B (c)).
  - Smallest sub-question: a bound on W-changing arena steps per λ_W-phase. On fts_ph16 it is 22 > n − 1.
- (FO_1O) (FO) on 𝒞^1O (§3.4). It suffices there for N5 to be polynomial. The smallest open case; fts_best16 is the canonical
  instance. By §3.6 it follows from:
  - (SEG-1O) ≤ n − 1 value-changing steps per (θ, w, τ, λ)-constant stretch;
  - (CH-1O) θ = Ξ(o) and w = W(o) change poly(n) times.
  Both are DATA-consistent and unproved.
- (FO) The same for arbitrary frozen τ (needed for Theorem B with blocks).
- (ALT) C_τ ≤ poly(n) in N5 runs.
- (BR*) Along an F_τ* run, Odd's best reply σ̄ changes poly(n) times. DATA: 4 / 9 / 13 changes at n 16 / 16 / 29.
  - (BR*) alone does not give (FO*). The other factor, the σ̄-segment length, is not ≤ n − 1 (fts_best24: 33 > 23, frozen,
    canonical start).
  - A segment bound poly(n) is OPEN (SEG-LEN*).
  - (BR*) ∧ (SEG-LEN*) ⇒ (FO*).
- (WF) Fallback steps of F_τ are W-flat (DATA 52/52). FALSE: box 22 (docs/new/N5-1O-box22.md §3, i1h_fts_best16, n 11). Fallbacks strictly
  lower W, and a vertex returns inside one λ-phase.

## 6. Data and files
experiments/new/box21/ (read-only use of n5.py and si.py):
- n5x.py: trace (asserts equal counts with n5.run).
- fixtau.py: plain vs frozen-τ* vs Even switch-all.
- climb_fix.py: climbs, modes tstar, tstarph, bestph, oneodd, seg1o, tany. grow.py: growth climb on the phase excess.
- lemmaG.py: Lemma G check. theta.py: θ/w stretch analysis on 𝒞^1O. shrink.py: greedy shrinker.
- anal.py, phases.py, wtrace.py, lamw.py: per-step analysis and the Lemma P check.
- h1.py: random H1 rates. wmono.py: Lemma W data.
- segbatch.py: random segment and σ̄ statistics. width.py: gate widths. sandwich_check.py: brute-force check of Lemma S (a).
  blockcheck.py: check of Theorem B (a)-(b).
- instances/: h1_hand, fts_ph16, fts_g29 and fts_g43 (with start files, runs from (σ_0, τ*)); fts_best16, fts_best24 and
  fts_best39 (canonical); oneodd_c16 and oneodd_c24 (𝒞^1O, canonical).
- Every long instance below gives the same counts under L-COMP's independent n5b.py (--mode spec): fts_best16 28, fts_best24 43,
  fts_best39 78, oneodd_c24 44, fts_ph16 22, fts_g29 66, fts_g43 121, h1_hand 2. Every one is Oink zlk OK with strategies
  verified (check_sol2.py).

Long single λ-phases (DATA; "one-player bound" = n − 1; all iterations value-changing unless noted):

| instance | sha1 | n | start | iterations | longest joint λ-phase | σ̄ changes | longest σ̄-segment | source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fts_ph16 | 55a21ee5… | 16 | (σ_0, τ*) | 22 | 22 | 4 | 14 | climb_fix.py tstarph |
| fts_best16 | 5534245f… | 16 | canonical (1 Odd choice vertex) | 28 | 27 | 9 | 11 | climb_fix.py bestph |
| fts_best24 | af9ca6c6… | 24 | canonical (2) | 43 | 43 | 1 | 33 | climb_fix.py bestph |
| fts_g29 | 58b69e82… | 29 | (σ_0, τ*) | 66 | 66 | 13 | 10 | grow.py |
| fts_best39 | 2fdffe0a… | 39 | canonical (4) | 78 | 78 | 7 | 25 | grow.py GROW_FIT=bestph from fts_best24 |
| fts_g43 | 53689242… | 43 | (σ_0, τ*) | 121 | 121 | 16 | 19 | grow.py from fts_g29 |

- Growth-climb envelope, (σ_0, τ*), phase length at n: 22 / 16, 40 / 22, 50 / 25, 66 / 29, 86 / 33, 98 / 36, 101 / 36, 121 / 43.
- Canonical (τ_0 optimal), from fts_best24: 43 / 24, 47 / 26, 78 / 39.
- Fixed-size climbs (best fitness):
  - frozen-τ* total N5 iterations: 19 / 47 / 45 / 42 at n 10 / 16 / 24 / 32;
  - Even-only against an arbitrary frozen τ (not an N5 run): 22 / 26 at n 10 / 16;
  - 𝒞^1O canonical total: 36 / 51 at n 16 / 24;
  - 𝒞^1O σ̄ changes: 20 / 26 at n 16 / 24. At the mid-climb snapshot it was 19 changes in 19 iterations, i.e. about one per
    iteration, so this fitness tracks run length.
- Stretch climbs: (SEG-1O) seg1o at n 12 / 20, best stretch n − 2. Frozen σ̄-segment segfz at n 16: best segment n, i.e. one
  above n − 1, after 1.1 M mutations. Random frozen runs (segbatch.py, 1,500 general + 1,500 𝒞^1O, n 6..24): no segment above
  n − 1; at most 3-4 σ̄ changes.
- Lemma P in G_τ* on fts_g43 (lamw.py, stopped at step 23 because exhaustive path enumeration explodes): 689,376 violating pairs
  at step 23.
Frozen τ* on Friedmann's families (fixtau.py; N5 from (σ_0, τ*) vs plain N5 vs Even switch-all from σ_0):

| game | n | plain N5 | N5 from (σ_0, τ*) | Even switch-all from σ_0 |
| --- | --- | --- | --- | --- |
| switchallexp N 2..5 | 35/49/63/77 | 8/7/8/10 | 8/8/8/10 | 30/70/150/310 |
| switchbestexp N 2..5 | 60/85/110/135 | 32/41/47/55 | 13/19/25/31 | 61/141/301/621 |
| vc_g25 / seg_r16 | 25/16 | 27/16 | 4/4 | 3/6 |
| sym_h8_s1 / sym_h16_s1 | 16/32 | 25/55 | 4/6 | 5/13 |

Frozen τ* is linear on all of these. The long frozen runs come from climbs (§3.2 and the table above).
