# Box 137 N5-REL: the Ξ-side «release once per key change» does not exist in the briefed form; KCH-POLY ⟺ GCH-POLY; ceiling, coalescence, c-world deficit and double-pull lemmas
L-NEW successor 47, 2026-11-01 (date -u: see the commit). Lead brief 21:08Z, STEP 1. Labels: PROVED (lane), CONJECTURE, READING,
DATA, DEAD (with the instance). G-N5-TIME stays OPEN. Not a TARGET.md claim, not M3, not a step-4 pass.
Premises and notation: the frozen packet P-N5-ANCHOR (f009a9a1) §1-§2 (FL run [a, b], W, ℓ, CN, T_x, ODIFF, gating data, epoch, GCH,
CAP, [1E-N3], [RULE] with κ_j, (R1) as ruled by both referees, FL-TIGHT, bridge B, PREFIX, FL-ANCHOR); L-RED R183 (OVT-KEY, KEY-CHARGE,
DEPTH, B_x, KCH_x) and R186 (claude/l-red 2799b309). VJ = Ξ_(j−1) ⊴ Ξ_j pointwise (RESULTS R15 (a)). One more premise:
- [PW] σ̄_j is an optimal counter-strategy in VJ00's sense: the valuation Ξ_j it gives is ⊴ the valuation of (σ_j, τ′) at EVERY vertex,
  for every Odd strategy τ′ (VJ00 = Jurdziński-Vöge, BRICS RS-00-48, §5, opened: notes/L-NEW.md «Sources opened»; the si.py engine's
  evaluate computes it). Used only in §2.

## 0. Answer
- The briefed lemma («between two consecutive moves of x in one FL run, some vertex below x changes W-tight key in a way that cannot
  recur without a σ̄- or τ-change, or a CN shortcut») is DEAD as a general statement:
  - ret2_n37 (§4): ONE FL run of 7 transitions that is ONE epoch (σ̄, τ, Ξ on ODIFF, Ξ on CN all constant; GCH 0; no CN move).
  - Inside it, vertex 36 makes the move 33 → 31 at transitions 2 and 6 (and 31 → 33 at 4), and the chooser x = 15 (level 10)
    moves 2 → 36 → 8 → 2 → 36 → 8 → 2 (transitions 2, 3, 4, 6, 7, 8), each move released by such a repeated join below it.
  - What never recurs is the key VALUE (KEY-MON, box 106 / FL-CANON (b)); its range is exponential. A coarser event type (a move,
    or (vertex, old option, new option)) recurs with no gating change.
- PROVED (lane), §1: moves_run(x) ≤ min{(|T_x| − 1)(1 + KCH_x), (ℓ(x) − 1)(1 + GCH)} for Even x ∉ CN. Hence KCH_x ≤ n·ℓ*·(1 + GCH),
  and [KCH_x ≤ poly for all x, and CNONLY ≤ poly] ⟺ FL-POLY ⟺ GCH-POLY. So «KCH_x ≤ poly» is the packet's equivalence restated; the
  DEPTH multiplication (Δn)^(ℓ*−1) is never realised inside an epoch (there each vertex moves ≤ ℓ(x) − 1 times).
  - A per-x «O(1) releases per key change» would not help either: R186's recursion with any constant C gives (Cn)^(ℓ*−1).
- Where σ̄-optimality stops (READING, §5): σ̄ enters the FL dynamics only through the gating data (FL-ANCHOR's proof). So any Ξ-side
  control of releases is a statement about gating changes, i.e. GCH-POLY itself, which CIRC makes circular. The in-run structure that
  σ̄-optimality does give is monotone and bounded (Lemma CEIL / SAT-MONO, §2), and it is never spent in the data: 0 saturation events in
  every corpus FL run (all gating changes happen strictly inside the unsaturated band).
- Also DEAD: CONJECTURE-candidate RET-1 («each option is re-entered at most once per FL run»; corpus RETMAX 1 on 813 pairs and on 11
  pins, including L-RED's adversarial ovk_n37 with 37 returns). ret2_n37 re-enters option 2 of x = 15 twice. The adversarial climbs
  (§4) reach RETMAX 2, MOVMAX 7.
- PROVED (lane), new tools for the proof side: CEIL, SAT-MONO, SAT-FREEZE, BAND (§2), SYNC (§3), C-WORLD and DEFICIT (§3), DOUBLE-PULL
  (§3). DATA: 0 violations of every checked item on 813 distinct pairs and all pins.
- Recipe for L-RED: §6 (make ret2_n37's carry a gating event, then nest the lap gadget).

## 1. Proposition KCH-GCH (PROVED, lane)
Let x ∉ CN be Even with level ℓ(x) in an FL run [a, b].
- (a) moves_run(x) ≤ (ℓ(x) − 1)(1 + GCH).
  - Proof: by FL-ANCHOR (i), inside an epoch with first gating state s0, x moves only at transitions j ≤ s0 + ℓ(x) − 1, i.e. at most
    ℓ(x) − 1 times; the run has at most 1 + GCH epochs. ∎
- (b) moves_run(x) ≤ min{(|T_x| − 1)(1 + KCH_x), (ℓ(x) − 1)(1 + GCH)}: (a) and R183 KEY-CHARGE.
- (c) KCH_x ≤ Σ_(v ∈ B_x) moves_run(v) ≤ |B_x| (ℓ(x) − 2)(1 + GCH) ≤ n ℓ* (1 + GCH) (R183's KCH_x bound, then (a); levels in B_x are
  < ℓ(x)).
- (d) Equivalence. FL ≤ Σ_(x ∉ CN) moves_run(x) + CNONLY (every FL transition has a mover); with KEY-CHARGE, [∀x KCH_x ≤ poly and
  CNONLY ≤ poly] ⇒ FL-POLY. FL-POLY ⇒ GCH-POLY (CIRC) ⇒ KCH-POLY by (c). FL ≤ CAP (1 + GCH) closes the circle. ∎
- (e) Per-x constant releases do not suffice: if moves_run(x) ≤ C (1 + KCH_x) with C constant, R186's recursion still gives
  μ_ℓ ≤ C (1 + n μ_(ℓ−1)) ≤ (2Cn)^(ℓ−1). A polynomial needs a GLOBAL charge (each lower move pays O(1) moves summed over all vertices
  above it), and by (d) such a charge is equivalent to a GCH bound.

## 2. Lemmas CEIL, SAT-MONO, SAT-FREEZE, BAND (PROVED, lane)
Setting: an FL run [a, b]; W = W_a = … = W_b, τ = τ_a.
- Lemma CEIL. Ξ_j(v) ⊴ W(v) for every vertex v and state j ∈ [a, b]. For Even x ∉ CN all y ∈ T_x have the same value W(y) =: W⁻_x, so
  Ξ_j(y) ⊴ W⁻_x on T_x.
  - Proof. [PW] with τ′ = τ_j = τ: Ξ_j ⊴ valuation of (σ_j, τ) = W_j = W. For y, y′ ∈ T_x: x ⊕ W(y) = W(x) = x ⊕ W(y′), x lies on neither
    W-play (x ∉ CN, V1), and ⊕ by a vertex off both plays is injective (same cycle node, length + 1, relevant set ∪ {x} or unchanged
    for both). So W(y) = W(y′). ∎
- Lemma SAT-MONO. SAT_j := {v : Ξ_j(v) = W(v)} is non-decreasing on [a, b].
  - Proof. v ∈ SAT_(j−1): W(v) = Ξ_(j−1)(v) ⊴ Ξ_j(v) ⊴ W(v) (VJ, CEIL). ∎
- Corollary SAT-FREEZE. If x ∉ CN and σ_(j−1)(x) =: z ∈ SAT_(j−1), x does not move at j or at any later transition of the run.
  - Proof. A move needs y ∈ T_x with Ξ_(j−1)(y) ▷ Ξ_(j−1)(z) = W⁻_x, against CEIL. z stays x's option and stays saturated (SAT-MONO). ∎
- Corollary BAND. Let x ∉ CN move at t_1 < t_2 < … < t_M and v_i := Ξ_(t_i − 1)(σ_(t_i)(x)). Then v_1 ◁ v_2 ◁ … ◁ v_M ⊴ W⁻_x.
  - Proof. z := σ_(t_i)(x) is x's option on [t_i, t_(i+1) − 1]. v_(i+1) ▷ Ξ_(t_(i+1) − 1)(z) (the move is improving: S2) ⊵ Ξ_(t_i − 1)(z)
    (VJ) = v_i. CEIL for the bound. ∎
- Reading: an FL run lives in the unsaturated band below W, and saturation is a potential of size ≤ n per run. DATA: SATGAIN 0 in all 20
  corpus FL runs and in 10 of 11 pins (odxi_min_n12: 11, at its last state; cwmov2_n57: 2). The band, not the potential, is where the
  runs happen.

## 3. Lemmas SYNC, C-WORLD, DEFICIT, DOUBLE-PULL (PROVED, lane)
- Lemma SYNC (coalescence; on [RULE] and (R1)). Let x ≠ x′ be Even, ∉ CN, with T_x = T_x′, and σ_(j−1)(x) = σ_(j−1)(x′) at an FL
  transition j. Then σ_j(x) = σ_j(x′), and so at every later transition of the run.
  - Proof. Bridge B: TIE_j(x) = R_j(x) ∩ T_x = ({z} ∪ {y ∈ T_x : Ξ_(j−1)(y) ▷ Ξ_(j−1)(z)}) ∩ T_x, the same set for x′. T_x = T_x′ gives
    the same W-cycle node c, hence the same case of κ_j; κ_j(y) (the index of y, or the root-first key of y from c) does not depend on the
    chooser. [RULE] at both (R1 covers a non-mover) gives the same κ_j-least element. Induction on j. ∎
  - Consequence for constructions: two choosers with the same option set that ever share an option are merged for the rest of the run.
    A ladder that needs two strands to stay apart must give them different option sets.
- Lemma C-WORLD. Let j be a state of an FL run, y ∉ CN ∪ ODIFF_j, A the first vertex of ODIFF_j ∪ CN on y's W-play under σ_j, and let
  the cycle node of Ξ_j(A) be c, the W-cycle node of y. Then, with relevant sets as sets and ℓ the W-level,
  Ξ_j(y) = (c, (W(y).rel \ W(A).rel) ∪ Ξ_j(A).rel, ℓ(y) − ℓ(A) + len Ξ_j(A)).
  - Proof. PREFIX (c), second case (c is not on the prefix P = y … A⁻, all of level ≥ 1): Ξ_j(y) = (c, rel_c(P) ∪ Ξ_j(A).rel, |P| +
    len Ξ_j(A)). The same formula for W (the W-play from y is P followed by A's W-play, cycle node c) gives W(y).rel = rel_c(P) ⊔ W(A).rel
    (disjoint: a W-play does not revisit P before c) and ℓ(y) = |P| + ℓ(A). ∎
  - So in the c-world, Ξ(y) depends on the tight path from y only through WHICH gate A it reaches first: a move on y's prefix that
    keeps A leaves Ξ(y) unchanged.
- Corollary DEFICIT. For A ∈ ODIFF_j ∪ CN with Ξ_j(A) of cycle node c(A) := its W-cycle node put D_j(A) := wt(W(A).rel) − wt(Ξ_j(A).rel)
  ≥ 0 (wt = Friedmann's signed weight, si.py Engine.weight) and λ_j(A) := len Ξ_j(A) − ℓ(A). For Even x ∉ CN and y, z ∈ T_x both in the
  c-world with first gates A_y, A_z: Ξ_j(y) ▷ Ξ_j(z) ⟺ D_j(A_y) < D_j(A_z), or equal and λ_j(A_y) better than λ_j(A_z) by the parity of
  c (longer is better for c odd).
  - Proof. W(y) = W(z) (CEIL); wt is additive over disjoint sets, so wt(Ξ_j(y).rel) = wt(W⁻_x.rel) − D_j(A_y), and len Ξ_j(y) =
    ℓ(y) + λ_j(A_y). Same cycle node c: compare weight, then length. ∎
  - Closure: if a mover's old option is in the c-world, so is its new option (cycle-node rewards: rew(c) ≤ rew of the new option's Ξ-cycle
    node ≤ rew(c) by S2 and CEIL; rewards are injective).
  - READING: in the c-world the FL face is strategy improvement for the minimiser of a deterministic two-player total-cost game with
    STATIC integer edge costs (an Odd deviation from τ(A) to s costs wt(W(τ(A)).rel) − wt(W(s).rel), lengths likewise), where the
    minimiser's arena is the layered tight DAG and its rule is [RULE]; D is the max-plus value. No lane result bounds that game's SI.
  - DATA: CW (option-states in the c-world) 314 on the corpus, formula exact (CWVIOL 0). FL moves in the c-world: 0 / 168 on the corpus,
    2 / 32 on cwmov2_n57 (climb mutant, §4), DEFICIT holds on both (DEFVIOL 0). So «FL moves never happen in the c-world» is not
    conjectured.
- Lemma DOUBLE-PULL. Let y ∈ T_x and let some Even vertex on y's W-path move at FL transition j; let v be the one nearest to y, Q the
  path y … v (unchanged at j: no Even vertex of Q other than v moves, Odd follows τ). If Q contains no ODIFF_(j−1) ∪ ODIFF_j vertex and
  (NC) no vertex of Q ∪ {v} lies on the Ξ_(j−1)- or Ξ_j-plays of v's old and new options, then K_j(y) < K_(j−1)(y) (root-first key)
  AND Ξ_j(y) ▷ Ξ_(j−1)(y).
  - Proof. Key: K(y) = K(v) followed by Q's vertices; K_j(v) < K_(j−1)(v) because v moved (KEY-MON: strict at movers, non-increasing
    below). Value: with no ODIFF on Q, the Ξ-plays from y at j − 1 and j are Q followed by v's Ξ-play (PREFIX (a)); v's move is improving,
    so Ξ_j(v) = v ⊕ Ξ_j(y_v) ⊵ v ⊕ Ξ_(j−1)(y_v) ▷ v ⊕ Ξ_(j−1)(o_v) = Ξ_(j−1)(v) (VJ; ⊕ monotone off the plays, (NC)); prepending the fixed
    path Q is strictly monotone under (NC). ∎
  - So above the first gate, one lower move is at once a key release and a Ξ-release of y for every chooser that has y as an option.
    The Ξ side puts no brake on «release per key change» there; only the gates (and the c-world, where prefix moves are Ξ-invisible
    unless they change the first gate) do.

## 4. DATA, the pins, the climbs
Tools: experiments/new/box137/rel.py (all checks; run detection = box132/anchor.py), anat.py (anatomy of double re-entries),
climb137.py (adversarial climb, score 10^6 RETMAX + 10^3 MOVMAX + RET; a mutant that breaks a lemma check is written out and stops the
climb), runcorp.sh (corpus), pincheck.sh (pins). L-RED's pins copied read-only into box137/inst/ (sha1 = claude/l-red 2799b309
pins.sha1 files, also copied; 18 / 18 OK).

| set | FL runs | FL | non-CN moves | returns | RETMAX | MOVMAX | CEIL / SATDEC / FROZ / SYNC / CW / CHAIN / DEF viol. | SYNC cases | CW states | c-world moves | SATGAIN | CN moves |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| corpus, 813 distinct pairs (E-1) | 20 | 42 | 168 | 39 | 1 | 6 | 0 each | 432 | 314 | 0 | 0 | 13 |
| odxi_n37 (box 133) | 1 | 8 | 65 | 31 | 1 | 6 | 0 each | 16 | 0 | 0 | 0 | 0 |
| ovk_n37 (R183 adversarial pin) | 1 | 7 | 67 | 37 | 1 | 5 | 0 each | 85 | 0 | 0 | 0 | 0 |
| chain_k16_n81 / cnmov_k8_n57 (R183 / R184) | 1 / 1 | 7 / 7 | 52 / 49 | 17 / 17 | 1 / 1 | 5 / 5 | 0 each | 14 / 14 | 0 / 0 | 0 | 0 | 0 / 6 |
| dcyc3_n48 / d2cyc4_n72 (R184 / R185) | 1 / 1 | 3 / 4 | 3 / 4 | 0 | 0 | 1 | 0 each | 15 / 68 | 12 / 170 | 0 | 0 | 0 |
| odxi_many / odxi_min / odxi_lasso (R179) | 3 / 1 / 1 | 8 / 1 / 1 | 15 / 1 / 1 | 2 / 0 / 0 | 1 / 0 / 0 | 2 / 1 / 1 | 0 each | 40 / 2 / 2 | 12 / 10 / 4 | 0 | 0 / 11 / 0 | 0 |
| big_d3 / big_d4 / cyc_d2 (R183 IDEAL realisations) | 0 | 0 | – | – | – | – | 0 each | – | – | – | – | – |
| ret2_n37 (this box, pin) | 1 | 7 | 74 | 44 | 2 | 6 | 0 each | 98 | 0 | 0 | 0 | 0 |
| cwmov2_n57 (this box, pin) | 2 | 6 | 32 | 14 | 1 | 4 | 0 each | 113 | 102 | 2 | 2 | 0 |

- The corpus counts reproduce R183 / box 134 exactly (20 runs, 42 FL, 168 non-CN moves, 39 returns, 13 CN moves).
- Pins (box137/pincheck.txt): ret2_n37.pg (sha1 7058d2c222ee…, start ret2_n37_default.start 23efa9d2e29c…) and cwmov2_n57.pg
  (8360cc48125c…, start a8040ea960f1…). Default best-reward starts written out by start_pair, validated by the strict start check
  (N5X_STRICT_START=1). Each: Oink 8fbf0a7 --zlk and --tl solutions verified, regions agree with N5 (box107/pinwin.py), n5b state by
  state identical (si/root/n5bcmp.py), rel.py and anchor.py lines as in check.sh «box 137 REL».
- ret2_n37 (climb137.py from ovk_n37, seed 1; snapshot of the climb file taken right after its first RETMAX-2 improvement, IT 9477): FL run [1, 8], one epoch, GCH 0, ODIFF = {27} constant, σ̄ constant.
  x = 15 (level 10, T_x = {2, 8, 36}, Ξ-cycle node 27, W-cycle node 13): options over states 1-8: 2, 36, 8, 2, 2, 36, 8, 2 → moves 2 → 36 (j 2), 36 → 8
  (3), 8 → 2 (4), 2 → 36 (6), 36 → 8 (7), 8 → 2 (8). Lower vertices over states 1-8: 36: 33 31 31 33 33 31 31 31; 8: 34 25 25 34 34 25
  25 25; 2: 6 35 16 6 6 35 16 16; 31, 25, 33: 14|11 → 4 → back → 4. Root-first keys of x strictly decrease at every move (lap 1 at
  positions 8-9, the carry at position 2 (7 → 1) at j 4, lap 2 at positions 8-9 again). anat.py prints the full table.
- Climbs (4 cores, ≤ 40 min each; every climb process imported rel.py at its start, i.e. BEFORE the DEFVIOL sign fix): from ovk_n37
  (seed 1): RETMAX 2, MOVMAX 6, RET 45; from odxi_n37 (seed 2): RETMAX 2, MOVMAX 7, RET 49; from cnmov_k8_n57 (seed 3): RETMAX 1,
  MOVMAX 5; from odxi_many_n32 (seed 4, ended by the 40-min timeout): RETMAX 1, MOVMAX 4. Climbs 1-3 stopped at a mutant flagged only by the old DEFVIOL
  sign (c-world moves 3 / 2 / 2). Re-run with the fixed rel.py, each of the three mutants (out/*.viol) passes every check, DEFVIOL 0.
  cwmov2_n57 is the seed-3 mutant. Logs: box137/out/c1-c4.log.

## 5. The exact place (READING, on §1-§3 and the packet)
- Inside an epoch, every Ξ-value FL-ANCHOR uses is a function of the gating data and of σ below (its proof of (i)). So σ̄ influences a
  release only through a gating change. A «release once per key change» argument therefore has two parts:
  - (in-epoch) the settling after a gating change: bounded by FL-ANCHOR (each x ≤ ℓ(x) − 1 moves, epoch ≤ CAP). Key-change events DO
    recur here (ret2_n37), so no non-recurrence statement holds at this granularity; the count is by levels, not by events.
  - (across epochs) the number of gating changes, GCH. Every new epoch is opened by an in-run Ξ-rise at a gate or cycle node caused by
    an FL move of the same run (packet §8, R178 XI-NEW). This is the circular part (CIRC).
- σ̄-optimality supplies, inside the run: VJ monotonicity, the ceiling Ξ ⊴ W (CEIL), the saturation potential (SAT-MONO, ≤ n events per
  run), coalescence (SYNC, from [RULE]), and in the c-world the max-plus form of Ξ (DEFICIT). None bounds the number of strict Ξ-rises
  of a gate inside the unsaturated band: a gate's Ξ can rise once per move on its Ξ-play, and that play may run through tight paths
  ABOVE the choosers it releases (feedback). The failing step is exactly: «a gate's Ξ rises O(1) times per run» — false on odxi_n37
  (5 rises at gate 33 in one run, box 133), and nothing in σ̄-optimality forbids more.
- What a proof would need: a potential on the gates' positions inside their bands that every gating change spends and that in-epoch
  settling cannot refill. SAT-MONO is the only such potential found, and the data never spend it.

## 6. Recipe for L-RED (the lap gadget of ret2_n37, iterated)
- Lap: chooser x with k options y_1 … y_k (here 3) whose W-paths each pass a «joiner» (31, 25, 16) that can switch into the subtree of
  one attractor a (here 4); joiner indices decreasing in the order the joins happen, so each join makes the joined option key-smaller
  than x's current one; joins staggered by Ξ (one per transition) so that each join is also a Ξ-release of the joined option
  (DOUBLE-PULL); x then moves k times per lap.
- Carry: a root-side key drop (here level 2: 7 → 1) that moves the attractor's branch and resets the joiners (36: 31 → 33, 8: 25 → 34,
  2: 16 → 6), after which the lap repeats. In ret2_n37 the carry is in-epoch settling, so laps ≤ ℓ.
- Next step (target: many epochs, GCH growing): make the carry a GATING event. Put an ODIFF gate g on the level-2 branch whose σ̄-face
  reads the chooser (or the top of the lap), so that the lap's end raises Ξ(g) and opens a new epoch whose settling carries again.
  Then nest: let the attractor a be the chooser of a lower lap gadget, so laps of x = moves of a. Score: GCH and moves of the top chooser
  per FL run against n.
- Constraints to respect (lemmas above): keep every gate unsaturated for the whole run (SAT-MONO / SAT-FREEZE: a saturated option
  freezes its chooser for the run); give choosers distinct option sets (SYNC); stay above the first gate or change first gates in the
  c-world (C-WORLD: prefix moves that keep the first gate are Ξ-invisible there).

## 7. Status
- PROVED (lane): Proposition KCH-GCH (a)-(e); CEIL (on [PW]), SAT-MONO, SAT-FREEZE, BAND; SYNC (on [RULE] + (R1)); C-WORLD, DEFICIT with
  closure; DOUBLE-PULL (under (NC)).
- DEAD: the briefed release lemma (ret2_n37: the move 36: 33 → 31 recurs inside one epoch, GCH 0); RET-1 (ret2_n37: option 2 of x = 15
  re-entered twice in one FL run).
- CONJECTURE: none new. READING: §3 (total-cost SI cast of the c-world), §5, §6. DATA: §4.
- G-N5-TIME: OPEN. The FL face is exactly as open as GCH (Proposition KCH-GCH (d), packet Corollary FL-GCH).
