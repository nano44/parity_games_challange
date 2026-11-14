# R178 The idealised two-face model: no super-linear FL family found (best 2.7 FL steps per Even vertex; growth by levels is additive); the earlier "about 3d" was a search artefact; structural fact for the proof side: Lemma XI-NEW (the least-level mover of every FL step after the first has a NEWLY Ξ-available option), PROVED (lane), with the reduction of IDEAL-LIN to counting those events (L-RED successor 42)
Started 2026-11-01 12:06Z (Lead GO R178 = (a), date -u). Brief: «beat about 3d FL transitions in the idealised two-face model at
d = 3-4 … If the search plateaus at about 3d, state the exact structural reason in the form a proof could use … Report the model's
assumptions precisely (what is held fixed by fiat), so L-NEW can state IDEAL-LIN against the same model.» Labels: PROVED (lane), DATA,
READING. Not a TARGET.md claim. G-N5-TIME stays OPEN. Nothing here is a kill: the model fixes two Odd strategies by fiat.

## 0. Answer
- Not beaten in the sense asked. «About 3d» was under-searched: 10× longer climbs raise d = 4 (width 3, 12 Even vertices) from 22 to 32
  FL steps. But every family stays linear in the number n_E of moving Even vertices:
  - best ratio FL / n_E = 2.67 (32 at 12);
  - d = 6: 42 at 18; d = 8: 54 at 24;
  - growing the d = 4 champion level by level ADDS a constant: on top 32 → 39 → 46 → 52 → 64 (12 → 24 vertices); at the bottom
    32 → 31 → 33 → 41 → 48.
- The champions do show counter-like replays: a move of a bottom (most significant κ digit) vertex is followed by a replay of an upper
  sub-sequence (§3). In the traces I read the replay does not recurse, and the gain per level is bounded in all data.
- Structural fact for the proof side: Lemma XI-NEW (PROVED, lane; §2). At every FL step t ≥ 2, the mover of least W-level has a new
  option that was NOT in the previous arena. So a step can never be caused by κ alone.
  - Hence FL ≤ 1 + #{steps t: the least-level mover's new option was not Ξ-better than its current one at t − 2}. IDEAL-LIN reduces to
    bounding these «fresh availability» events.
  - Each such event needs a strict Ξ-rise, at step t − 1, of that face, caused by a mover on the face's Ξ-play.
  - DATA: 0 violations in 3,017 model genomes (5,958 steps) and in the corpus FL runs (§4).
- The model, stated precisely so that L-NEW can use the same object (IDEAL model, §1).

## 1. The IDEAL model (what is held fixed by fiat)
- Vertices.
  - Even "movers" x_1..x_N, each with options k = 1..deg(x). Option k is an Odd gate g_(x,k).
  - Each gate has a W-face (an edge to its W-target wt(x,k) ∈ {movers} ∪ {c_W}) and a Ξ-face (an edge to an Even vertex β_(x,k), whose
    single edge goes to xt(x,k) ∈ {movers} ∪ {c_X}).
  - Priorities: movers 0, gates 1, c_X 2 (even self-loop), c_W top even self-loop, β_(x,k) = 4 + 2·rank + parity (distinct ranks, free
    parities). In the fast simulators c_X = c_W = T (priority 2); that changes nothing, since no Ξ-play reaches c_W and W-values tie anyway.
- Fixed by fiat for the whole run: τ(g) = W-face and σ̄(g) = Ξ-face at every gate.
  - Not checked: that S4b keeps τ (I_τ = ∅), and that Odd's optimal counterstrategy to every σ of the run is the Ξ-face.
  - That is the stabiliser question (R175 §3 (ii); R177 §5).
- W is graded: wt(x,k) has level(x) − 1 (level 0 → c_W).
  - Every W-value is (c_W, ∅, 2·level), so all options tie, every step is W-flat (FL), and the W-cycle node is even.
  - So the tie-break is TB-even (RESULTS R24 (b)): the lex-min root-first key. Here key(x via k) = key(wt(x,k)) followed by the gate
    index of (x,k). The mover indices add nothing, since a gate determines its owner.
- Ξ = the one-player VJ valuation in G_X (gates on their Ξ-faces), compared as si.py Engine.key.
  - fastabs: G_X acyclic (a topological xorder, xt later than x), so Ξ = the signed weight of the β-ranks on the play.
  - fastcyc: arbitrary, values read off the lasso.
- Step = S4a with those faces:
  - A_j(x) = {σ_j(x)} ∪ {k : Ξ_j(face k) ▷ Ξ_j(face σ_j(x))};
  - σ_(j+1) = the S1 optimum of G_W restricted to A_j, equal to TB's lex-min tree (abs177 uses the si.py engine; fastabs and fastcyc
    are equal to it on 200 + 300 random genomes and all champions, 0 mismatches).
  - The run stops at I = ∅, or at σ_(j+1) = σ_j with I ≠ ∅, which would be an S4c fallback in N5 (FB=1 applies it and continues).
- CONJECTURE IDEAL-LIN: in this model a fallback-free run has O(n_E) steps (data constant ≤ 2.7).

## 2. Lemma XI-NEW (PROVED, lane)
Statement.
- IDEAL model: at every step t ≥ 2 of a fallback-free run, let h be a mover of least W-level among the vertices that move at step t
  (state t − 1 → t), and w its new option. Then w ∉ A_(t−2)(h).
- Real N5: the same holds in an FL run of a TWO-FIX window (τ, σ̄ constant, W unchanged, no fallback), at every transition except the
  run's first, for a least-W-length mover h that is not a corner.

Proof.
1. Every vertex on the W-play prefixes of h's options has smaller W-level (graded), so none of them moves at step t (h is least).
   Hence key_t(z) = key_(t−1)(z) for every option z of h: keys read only σ along those prefixes.
2. Suppose w ∈ A_(t−2)(h). At step t − 1, h chose σ_(t−1)(h) = o, the key_(t−1)-least option of A_(t−2)(h) (TB). Since w ≠ o, we
   get key_(t−1)(w) > key_(t−1)(o).
3. By step 1 then key_t(w) > key_t(o). But h moves from o to w at step t, so TB gives key_t(w) < key_t(o). Contradiction. □
- Real-game remarks.
  - Step 1 uses that the W-play prefixes of h's options have W-lengths below h's, and that no mover of smaller length exists.
  - A corner mover of least length is excluded by hypothesis (TB does not apply to it).
  - The first transition of a run is excluded because A_(t−2) belongs to the previous regime.
- Consequences (PROVED, lane):
  - (i) No step consists of κ-only moves. So FL ≤ 1 + E, where E counts fresh-availability events at least-level movers.
  - (ii) An event at (t, h, w) needs face(h, w) to rise strictly at step t − 1:
    - w ∉ A_(t−2)(h): face(w) ⊴ face(σ_(t−2) h) at state t − 2;
    - w ∈ A_(t−1)(h): face(w) ▷ face(σ_(t−1) h) ⊵ face(σ_(t−2) h) at state t − 1 (Ξ is monotone, and h only moves upward).
    - So some vertex on face(h, w)'s Ξ-play moved at step t − 1.
  - (iii) D acyclic gives CASC-G (R177) again: E ≤ height.
- What a proof of IDEAL-LIN must still bound (READING): with D cyclic, the backward cause chain t ← t − 1 ← … runs through Ξ-edges
  (to xorder-later vertices) and through κ-edges (to W-lower vertices, inside a step), so it can loop. A potential has to charge each
  fresh-availability event to a face whose Ξ-rank relative to its owner's current face goes up, and show that each (vertex, option)
  pair is charged O(1) times per … (open). The counting bound alone (crossings of monotone sequences) is not enough: on a grid of
  orders it allows super-polynomial growth (R177 §5 computation).

## 3. DATA
- Climbs (red/r177/fastabs.py, fastcyc.py; logs and genomes in red/r178/out/):

| model | d | W | deg | n_E | iterations × restarts | best FL steps | FL / n_E |
| --- | --- | --- | --- | --- | --- | --- | --- |
| acyclic | 2 | 3 | 3 | 6 | 40k × 6 | 8 | 1.33 |
| acyclic | 3 | 3 | 3 | 9 | 400k × 4 | 17 | 1.89 |
| acyclic | 3 | 4 | 4 | 12 | 40k × 4 | 18 | 1.50 |
| acyclic | 4 | 3 | 3 | 12 | 40k × 4 / 400k × 3 | 22 / 32 | 1.83 / 2.67 |
| acyclic | 5 | 3 | 3 | 15 | 30k × 3 | 21 | 1.40 |
| acyclic | 6 | 3 | 3 | 18 | 400k × 3 | 42 | 2.33 |
| acyclic | 8 | 3 | 3 | 24 | 300k × 2 | 54 | 2.25 |
| Ξ-cycles allowed | 2 | 2 | 2 | 4 | 60k × 6 | 5 | 1.25 |
| Ξ-cycles allowed | 3 | 2 | 2 | 6 | 60k × 4 | 10 | 1.67 |
| Ξ-cycles allowed | 4 | 3 | 3 | 12 | 60k × 3 | 31 | 2.58 |
| grow on top from the d 4 champion (150k per level) | 5-8 | 3 | 3 | 15 / 18 / 21 / 24 | | 39 / 46 / 52 / 64 | 2.6 / 2.6 / 2.5 / 2.7 |
| grow at the bottom | 5-8 | 3 | 3 | 15 / 18 / 21 / 24 | | 31 / 33 / 41 / 48 | 2.1 / 1.8 / 2.0 / 2.0 |

- The d = 4 champion (r178/out/big_d4_k3_W3.json, 32 steps, 57 moves):
  - per-vertex moves by level: [2, 1, 2] / [5, 5, 5] / [4, 6, 10] / [2, 7, 8];
  - bottom moves at steps 1, 12, 14, 18, 21;
  - steps 23-28 replay steps 4-9 (same movers, same option changes), after the bottom moves at 14, 18 and 21 reset the keys of the
    vertices above them. That is the counter mechanism.
  - READING (from this trace only): the replayed segment 23-28 contains no bottom move, so it is not itself a replay of a replay.
- Causes (r178/cause.py): in every champion (up to 64 steps / 119 moves), 27-35 % of moves are «κ-moves» (the new option was already available one step earlier),
  and 0 steps consist only of κ-moves (XI-NEW predicts that).
- XI-NEW checks:
  - model: 3,017 genomes (17 champions + 3,000 lightly climbed random ones), 5,958 steps, 0 violations;
  - real N5: red/r178/xinew.py on the 813 distinct corpus pairs (runcorp.sh, c_corpus.txt), see §4.

## 4. Real-game check of XI-NEW (corpus)
- red/r178/xinew.py on the 813 distinct pairs (RESULTS Erratum E-1; runcorp.sh → c_corpus.txt, 0 errors): 37 FL transitions inside FL
  runs, 19 of them past a run's first transition with a non-corner least-length mover: 0 violations. 3 had only corner movers at the
  least length (not covered). Thin, because corpus FL runs are short (≤ 8).
- Pins u23sw64_n32 (checked 7, 0 violations) and u2flat73_n32 (checked 4, 0 violations); their start, Oink and xeng checks are in R177 §1.

## 5. Next
- Proof side (L-NEW 46 box 132): IDEAL-LIN ⇐ a bound on fresh-availability events (XI-NEW (i), (ii)). The champions' one-level replay
  is the pattern to rule out recursively.
- L-RED: a two-level replay (a replayed segment that itself contains a bottom-triggered replay) would be the first super-linear
  sign. Grow-and-climb never produced one; designing it by hand is the next attack, then stabilisers.
