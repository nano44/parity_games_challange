# Box 11 (c): the best-reply-change count (K9's factor) has no simple invariant; three candidates killed with instances (L-NEW successor 4, Fable 5.1; written 2026-10-21 23:43Z by date -u)
Target: G-N5-TIME via K9 (N5-oneplayer-box7.md §3): #iterations ≤ (per-segment bound) × (2 + changes of σ̄ + changes of τ̄), where σ̄_k = Odd's VJ
best reply to σ_k and τ̄_k = Even's best reply to τ_k. Box 10 bounded the per-segment part only for one-player games (N5-phase-bound-box10.md;
(P-N5) false in two-player runs). This box looks for an invariant that bounds the number of best-reply changes. Status: NONE found; the
three natural candidates are FALSE on the lane's instances; on climbed instances #changes ≈ #iterations, so K9's factor is not smaller than
the quantity it should bound. Tools: experiments/new/br/ (brstruct.py, brtrace.py, brphase.py, br_climb.py; outputs in br/*.txt, br/logs/).

## 1. Trivial bounds, and why the factorisation is not informative on data
- σ̄_k is a function of σ_k and τ̄_k of τ_k, so σ̄ changes only at Even moves and τ̄ only at Odd moves: changes(σ̄) + changes(τ̄) ≤ 2·#iterations.
- K9's other direction needs a per-segment bound (Even moves between two σ̄ changes). Data (br/brstruct_lane.txt, brstruct_lane2.txt):
  ch_n64 (n = 64): 40 iterations, 29 + 21 = 50 changes; ch_n16: 16 iterations, 23 changes; the box-9 tails: 60-76 iterations, 35-45 changes.
  So on the adversarial instances the best replies change at almost every iteration; bounding the changes IS bounding the run.

## 2. Three candidate invariants, all FALSE (instances)
(BR-NR-vertex) "a vertex's best reply never returns to a successor it used earlier" would give changes ≤ Σ_v (deg(v) − 1) ≤ m − n. FALSE:
  per-vertex revisits are common: τ̄ at one Even vertex revisits 20 times on sg5.pg (n = 38, sha1 d0d0ba63…), 14 on sc24g.pg (n = 25,
  sha1 4914fa60…); σ̄ at one Odd vertex revisits 9 times on sbe2_s21.pg (n = 60, sha1 9a0e32591bce…). Climb (br_climb.py FIT=rev): 11 revisits
  of one vertex at n = 16 (instances/br11/rev_r16.pg, log br/logs/rev_r16.log; final numbers §4).
(BR-NR-global) "the whole vector σ̄ (or τ̄) never returns to an earlier state" (Lemma NR's analogue; Lemma NR itself says σ and τ never return,
  RESULTS R15 (c)+(d)). FALSE: sbe2_s21.pg has 15 σ̄ changes among only 4 distinct σ̄ states (12 global returns); sg5: τ̄ 6 global returns;
  climb FIT=glob: 10 global returns at n = 16 (instances/br11/glob_r16.pg).
(BR-λ) "a best reply changes only when a cycle node of the honest valuation changes" would give ≤ n(n − 1) + 1 changes. FALSE (brphase.py,
  br/brphase.txt): over 7 instances, 96 σ̄ changes of which 48 come with any change of λ(Ξσ) and 31 with a λ change at a switched vertex;
  τ̄: 127 / 50 / 31; sbe2_s21: 15 σ̄ changes, 1 λ change. So best replies flip inside λ-phases, by path-set and length leapfrogs, exactly the
  freedom CDAG_n exhibits (N5-K9-Pstrict-counter.md).
Since Ξσ is pointwise monotone for Even, a flip of σ̄(o) between successors w, w' is an order flip of two monotone chains; nothing in the
valuation order bounds how often two monotone chains cross (the P-set component of CDAG crosses 2^n times). A bound must come from N5's
step, not from the valuation.

## 3. The toggle mechanism (sbe2_s21.pg, n = 60, sha1 9a0e32591bce…; br/brtrace_sbe2_s21.txt)
- Odd NEVER moves in this run (37 iterations, τ constant, 0 fallbacks), so every iteration is Even's optimum in G_τ over the honestly gated
  arena: the Even-only dual of box 9's frozen-σ tail.
- σ̄ takes 4 states A-D that differ at two Odd vertices only (44: 39/40; 47: 43/37) and toggles A→B→C→D→D→C→D→D→C→C→C→A→A→A→C…: 15 changes,
  12 returns. Even vertices revisit targets along the way (vertex 4: 5→1→5→1→5), while the honest Ξσ rises monotonically.
- So the gate (honest improvements against a toggling σ̄) and the optimiser (against the fixed τ) disagree repeatedly; this is the mechanism
  that defeats Lemma P's Case B in two-player runs (K1 stalls, N5-phase-bound-box10.md §5), seen from the best-reply side. The run is still
  short (37 iterations at n = 60), and climbs for more returns stay small (§4).

## 4. Conclusion for the Lead's conditional
(c) yields no usable invariant: the count of best-reply changes is as large as the run on the adversarial instances, and every structural
restriction tried (no per-vertex revisit, no global return, change only with a λ change) fails with pinned instances. Route (b) (a two-player
per-segment potential mixing honest Ξσ with V_{σ,τ_k}) was therefore not started in this box, per the Lead's condition.
- Final climb numbers (23:49Z by date -u; br/logs/*.log, instances pinned in br/box11_instances.sha1, every improved best re-run through n5.run,
  regions = Zielonka, verify.py OK): total changes σ̄ + τ̄ = 65 in 46 iterations at n = 33 (ch_g16.pg, sha1 a0df9895…: 36 + 29; changes ≈ 1.4 ×
  iterations); max revisits of one vertex's best reply 16 at n = 24 (rev_r24.pg, sha1 ed28bad8…; σ̄ at one Odd vertex changes 19 times among
  ≤ 4 successors), 12 at n = 16, 10 at n = 21; global returns of σ̄: 26 in 34 changes at n = 60 (glob_sbe.pg, sha1 28a3b3d8…, seeded from
  sbe2_s21; Odd still never moves), 10 at n = 16. All runs ≤ 46 iterations: the structure that breaks the invariants does not lengthen the runs.
