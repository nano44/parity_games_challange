# R187 Real-game W-ladders: neither σ̄-optimality nor τ-stability kills the second release. Theorem REALIZE (PROVED, lane): every IDEAL genome with an acyclic Ξ-graph runs state-for-state as ONE real N5 FL run (gadgets fix σ̄ and τ by fact, checked at every state). Real L_FL 32 at n 126 and 64 at n 246 (was ≤ 8); key changes release up to 6 next-level moves; the first ACTIVE D″-cyclic stretch (32 transitions). No compounding: per-level growth stalls, L_FL linear in n (DATA) (L-RED successor 44)
Started 2026-11-01 21:06Z (Lead brief, STEP 1 = R187; date -u). Brief: «Build a real-game W-ladder (depth ℓ* ≥ 3) in which a key change at
level j releases ≥ 2 moves at level j + 1 inside one FL run. Use gates whose σ̄ IS Odd's best reply throughout (check it at every state).
Score: KCH product along the ladder and L_FL, against n. If it is impossible, give the exact obstruction: which of σ̄-optimality or
τ-stability kills the second release.»
Labels: PROVED (lane), DATA, READING, OPEN. Notation: frozen packet P-N5-ANCHOR (f009a9a1) §1-§2; R177 (TB), R178 §1 (IDEAL model),
R183 (OVT-KEY, KEY-CHARGE), box 136 (D″, CASC-M″). Not a TARGET.md claim. G-N5-TIME stays OPEN. No kill.

## 0. Answer
- The ladder exists in the real game (§2). σ̄-optimality and τ-stability do not kill the second release: both can be enforced by
  gadgets, for every IDEAL genome whose Ξ-graph is acyclic (Theorem REALIZE, §1, PROVED, lane; checked by script on 7 champions and
  60 random genomes: σ̄ = Ξ-face and τ = W-face at every gate at every state, W unchanged, no fallback, mover states equal to IDEAL's).
  - Pin stab_d4_n126 (R178 champion big_d4_k3_W3 realised): ONE real FL run of 32 transitions, ℓ* = 4 mover levels, CROSS 37,
    FVCH 32, 34 returns, OVT-KEY / KEY-CHARGE 0 violations. Key changes at level j release ≥ 2 moves at level j + 1 in 3 / 5 / 3
    segments (j = 0 / 1 / 2), up to 6 in one segment; one mover moves twice inside one key-stretch (= |T_x| − 1, OVT-KEY tight) 9 times.
  - Pin stab_g24_n246 (grow_top_N24): one real FL run of 64 transitions, d 8.
  - Both pass startck, Oink --zlk + verify (OINK OK), Oink --tl + verify, xeng (n5b and n5.py: identical state sequences).
- R183 §2's «R178's IDEAL champions as real games: 0 FL runs» was the NAIVE realisation (gate → {W-target, β}). It does not mean the
  graded shape is unrealisable; it is realisable exactly.
- Reduction (Corollary REAL-IDEAL, §1): if real FL runs are polynomial in n from every start pair, IDEAL runs on acyclic Ξ-graphs are
  polynomial in n_E·deg. So the IDEAL question (CONJECTURE IDEAL-LIN, R178) is a NECESSARY part of FL-POLY, not a model artefact.
  Conversely, a super-polynomial IDEAL-ACYC family is a real N5 family (given start pair) with super-polynomial FL runs.
- What does not happen: compounding. The KCH product along the ladder stays flat (§2): per-level moves grow 5 → 15 → 20 → 17
  (d 4) and plateau near 10 per mover at d 8; KCH_x climbs to 63 but the top movers move only 5-10 times. L_FL / n ≈ 0.25 on every
  realised champion (linear).
- Where the bottleneck is (DATA, §3): at levels ≥ 1, moves ≈ fresh-availability events (AVN, R178 XI-NEW's currency): a mover moves
  about once per new Ξ-overtake among its options, and AVN per mover stays ≤ 13 while KCH grows. The binding side is Ξ, not the key.
- The real ladder's stretch is D″-CYCLIC (L-NEW's own dmerge2.py, with and without DOM): the first active D″-cycle (box 136 §3 (1):
  none observed; R185's were inert, stretches ≤ 4). CASC-M″ is not violated (its hypothesis fails). A Ξ-face reading the same or an
  upper level is what closes the cycle; if every Ξ-face read only lower levels, D″ is graded and CASC-M″ / FL-ANCHOR give
  L ≤ ℓ* + 1 (DATA: DOWN-class climbs T ≤ d exactly, §2).
- Per-state D″ is cyclic at every state of this stretch (33 / 33, also restricted to vertices that can move), and of R185's two
  stretches: the per-state route for CASC-M″ is dead on data (§2; ERRATUM to R185 §1's reading).
- Item 2 (CN shortcut / up alternation at one cycle node, §6): it EXISTS and repeats. Pin cn_d4_n126: the W-cycle node c moves 18
  times in one FL run of 33 (10 up, 8 shortcuts, 13 direction changes, 11 returns); cn_g24_n246: 22 moves in one FL run of 64
  (19 direction changes, 14 returns). CN-UP holds (cnidx DOWN_NOSHORT 0) but does not bound it. Growth with n: linear so far (DATA).

## 1. Theorem REALIZE (PROVED, lane)
Input: an IDEAL genome (R178 §1, fastcyc format: movers x with level lev(x), options k with W-target wt (a mover of level lev(x) − 1,
or none at level 0), Ξ-target xt (a mover, or «X»), β-rank and parity, gate indices, start option) whose Ξ-graph (x → xt over all
options) is ACYCLIC. Output: the STAB+K+ESC game (experiments/red/r187/stab.py, build(G, 0, kgad=True, esc=True)):
- mover x: Even, priority 0, edges to its gates; gate g = (x, k): Odd, priority 1, edges {e_g, β_g};
- W-face: e_g (Even, single edge to wt or c_W), EVEN priority above every β, rising with lev(x); c_W even self-loop above all e;
- Ξ-face: β_g (Even, priority 6 + 2·rank + parity) with edges {xt, u} (ESC; only {u} if xt = «X»);
- K (the stuck core, found by findk.py): vertices u = K0 (Even, prio c_W + 2), K1 (Even, prio 5), K2 (Odd, prio 3), K3 (Even,
  prio c_W + 3); edges K0 → {K1, K3}, K1 → {K0, K1}, K2 → {K1, K2}, K3 → {K1, K2}.
- START: σ = genome start at movers, β_g → xt, K0 → K3, K1 → K1, K3 → K2, single edges elsewhere; τ = e_g at every gate, K2 → K2.
- Indices: movers, gates (genome gate indices), β, then e in gate-index order, c_X (unused), c_W, K. n = N + 3M + 6 (M = Σ deg).
Claim. While the IDEAL run (R178 §1, fastcyc / r187/ideal.py) moves, every real N5 transition is an FL transition with:
σ̄ = β-face at every gate (and Odd's K-choice K2 → K1), τ unchanged, W unchanged, no fallback, and the movers' choices equal to IDEAL's.
When the IDEAL run stops (stuck), the real run takes an S4c fallback.

Proof (state j; assume the claim up to j).
1. σ̄. Under σ_j with Odd on β-faces, every Ξ-play from a β-face goes forward in the acyclic Ξ-graph, so it ends at u; from u it follows
   K0 → K3 → K2 → K1 (Odd's K2 → K1: the odd self-loop of priority 5 beats priority 3) and ends at the cycle K1. So every such play
   has cycle node K1 and its path set contains the common suffix {K0, K3}.
   - Gate g of a level-0 mover: the e-face reaches c_W (even cycle) and the β-face reaches K1 (odd cycle): β is strictly better for
     Odd (cycle reward first).
   - Gate g of a level ≥ 1 mover: the e-face play is e_g → wt → σ(wt) → (β-face) … → K1. Both faces end at K1. The symmetric
     difference of the path sets above K1 contains e_g (no Ξ-play uses an e-face, so e_g is only on the e-side) and otherwise only
     β-vertices, all less relevant than e_g. e_g is even, so the e-face is strictly better for Even: β is strictly better for Odd.
   - So the β-strategy has no Odd-improving switch in its own valuation; for a fixed σ that makes it Odd's optimal counterstrategy
     (VJ00 local optimality), and the strict preferences make the choice unique. Hence σ̄_j = β-face at every gate.
2. τ. Iτ at a gate g: in the τ-world (τ fixed, Even's best reply) the e-face reaches only W-faces and pads, so its value is
   (c_W, ∅, length): every vertex on it is below c_W. The β-face lets Even take β → u and then the cycle K0 ↔ K1, whose node K0 is an
   EVEN vertex above c_W. So the β-face is strictly better for Even and is not Odd-improving. Hence A_τ(g) = {e_g}. K is closed and
   stuck (findk.py: S4a keeps σ_K and S4b keeps τ_K), so S4b keeps K2 → K2. τ_(j+1) = τ_j.
3. σ. S4a: Even's optimum against τ in the arena of current + improving options.
   - e-vertices: single edge.
   - β_g (if its switch to u is improving): under τ, xt reaches c_W (even), while u reaches K's W-world cycle K2 (odd), even with K's
     arena options, because K is stuck. So β_g stays on xt.
   - K: stuck, closed.
   - Movers: every option has W = (c_W, ∅, H(lev)) (graded, no vertex above c_W on W-plays), so every available option is fully
     W-optimal and none is a corner (W-plays go strictly down). By [RULE] (RESULTS R24 (b), TB-even), x takes the κ-least
     available option, κ = root-first key.
   - Two options' root-first sequences first differ at the e-vertices of the first differing gates from the bottom (a gate fixes its
     owner), and e is allocated in gate-index order. So κ = the IDEAL key (tuple of gate indices).
   - Availability: Ξ_j(g) for a gate is the β-face value. Two options' X-plays never merge before β_a or β_b (acyclic: the play from
     x's option cannot return to x), so their path sets differ above K1, and the order is the path-set order of the β-ranks and
     parities, i.e. IDEAL's (fastcyc key; the common K-suffix cancels; lengths never decide).
   - So σ_(j+1) on movers = the IDEAL step, and σ is unchanged elsewhere.
4. W and FL. W(x) = (c_W, ∅, H(lev(x))) for every mover whatever σ is; W(β_g) = W(xt); K unchanged. So W_(j+1) = W_j. If the IDEAL
   step changes σ, the transition is not a fallback, τ is unchanged and W is unchanged: an FL transition. If the IDEAL run is stuck
   (σ_new = σ), S4a and S4b keep (σ, τ) while I_σ ≠ ∅, so S4c fires. ∎
- Premises used: SPEC S1-S5, VJ00 local optimality of a one-player counterstrategy, [RULE] (RESULTS R24 (b), as in the frozen packet).
- Not covered: Ξ-graphs with cycles. There Odd's reply can genuinely differ: R167's self-referential gate, where x's Ξ-face returns
  through x's own gate (CLASS=full, ESC on: FAITHFUL < IDEAL length in 21 / 30 random genomes, σ̄ ≠ Ξ-face from the first state in the ones inspected; t3.py shows the returning play).
- Corollary REAL-IDEAL. For every acyclic IDEAL genome there is a real game of size N + 3M + 6 and a start pair whose N5 run has an
  FL run as long as the IDEAL run. So FL-POLY (per start pair) ⇒ IDEAL-ACYC-POLY.

## 2. DATA
Real runs (realck.py: FAITHFUL = IDEAL length and mover states equal, for all rows; per-level statistics from rel.py on the trajectory):

| genome (R178) | n | movers | d | real L_FL | moves per level M | μ_ℓ (max moves of one mover) | max KCH_x per level | D2 (segments with ≥ 2 next-level moves) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| big_d3_k3_W3 | 96 | 9 | 3 | 17 | 5, 11, 17 | 2, 5, 7 | 0, 5, 12 | 3, 6 |
| big_d4_k3_W3 (pin stab_d4_n126) | 126 | 12 | 4 | 32 | 5, 15, 20, 17 | 2, 5, 10, 8 | 0, 4, 17, 25 | 3, 5, 3 |
| big_d6_k3_W3 | 186 | 18 | 6 | 42 | 6, 11, 11, 14, 18, 20 | 2, 5, 4, 7, 9, 9 | 0, 6, 14, 20, 29, 33 | 3, 2, 3, 5, 5 |
| big_d8_k3_W3 | 246 | 24 | 8 | 54 | 5, 11, 12, 16, 23, 14, 14, 13 | 2, 5, 7, 8, 9, 9, 6, 5 | 0, 5, 11, 18, 25, 41, 47, 52 | 5, 4, 3, 6, 3, 3, 1 |
| grow_top_N15 | 156 | 15 | 5 | 39 | 5, 14, 21, 17, 9 | 2, 5, 11, 8, 4 | 0, 4, 16, 26, 34 | 3, 5, 2, 1 |
| grow_top_N24 (pin stab_g24_n246) | 246 | 24 | 8 | 64 | 5, 13, 20, 22, 10, 21, 17, 11 | 2, 5, 10, 10, 5, 9, 10, 6 | 0, 5, 18, 27, 38, 44, 55, 63 | 3, 5, 3, 1, 6, 2, 3 |
| grow_bottom_N24 | 246 | 24 | 8 | 48 | 4, 11, 13, 18, 15, 15, 12, 12 | 2, 6, 5, 8, 7, 7, 7, 6 | 0, 4, 10, 19, 28, 33, 41, 46 | 3, 4, 4, 2, 2, 1, 1 |
- Score asked («KCH product along the ladder»): the growth factor μ_ℓ / μ_(ℓ−1) is > 1 only on the first two or three levels (2 → 5 →
  10) and ≤ 1 above; DEPTH's recursion (Δ − 1)(1 + n·μ_(ℓ−1)) is far from tight: at the top, moves / (1 + KCH) = 6 / 64.
- L_FL / n = 0.18 / 0.25 / 0.23 / 0.22 / 0.25 / 0.26 / 0.20: linear (DATA). The previous real maximum was L_FL 8 (R181, R183).
- Pins (r187/instances, pins.sha1): stab_d4_n126 (ovtkey: MOVES 57 RETURNS 34 RET_IN 0 OVER 0 KBOUND 0 FL 32 CNONLY 0; fvch: L 32,
  FVCH 32, CROSS 37, SBCH 0, CNCH 0, BVIOL 0), stab_g24_n246 (MOVES 119 RETURNS 75 … FL 64). N5: 35 iterations, 1 fallback (the
  IDEAL stop) for stab_d4.
- L-NEW dmerge2.py (box 136, run in a scratch copy of claude/l-new experiments/new) on stab_d4_n126: «RUNS 1 FL 32 ACYC 0 CYC 1 …
  MAXL 32 SELFL 0 CNMOV 0», the same with STRETCH=1, and with STRETCH=1 DOM=1 (DOMCUT 1262, still CYC 1).
- Per-state D″ (the R185 §4 proof-side suggestion «CASC-M″ with a per-state D″»): r187/mkdm2state.py patches a copy of dmerge2.py
  (read-only source) to build D″ from the edges of ONE state, and with PRUNE=1 keeps only vertices with |T_x| ≥ 2 (a vertex with one
  tight option is constant on the run by FL-TIGHT, so edges into it are not dependencies; dmerge2 already adds x → every Even vertex on
  a segment, so no path is lost). STRETCH=1 DOM=1:

| instance | stretch | per-state D″ cyclic | pruned per-state cyclic | a per-state cycle (pruned) | union cycle (pruned) |
| --- | --- | --- | --- | --- | --- |
| stab_d4_n126 | [0, 32] | 33 / 33 | 33 / 33 | movers 0 → 6 → 1 → 0 (levels 0, 2, 0) | 0 ↔ 9 (levels 0, 3) |
| d2cyc4_n72 (R185) | [6, 10] | 5 / 5 | 5 / 5 | 1 ↔ 13 | 1 ↔ 13 |
| dcyc3_n48 (R185) | [6, 9] | 4 / 4 | 4 / 4 | 11 ↔ 20 | 11 ↔ 20 |
  - So the per-state route is dead on data: every D″-cyclic stretch known is cyclic at every one of its states. R185 §1's reading
    («time-resolved D″ would be acyclic» on dcyc3) is wrong; ERRATUM added there.
  - In stab_d4 the per-state cycle is mover 0 reading mover 6 (level 2) through a Ξ-face (an upward read), 6 reading 1 through its
    W-key, 1 reading 0: the mutual feeding the IDEAL model has by design.
- Random checks (realck.py --rand, t2.py): ACYC class 20 + 40, DOWN class 60: all equal, FAITHFUL = IDEAL length.
- Climbs (climb.py, 60,000 mutations each on the IDEAL simulator, which equals the real run by REALIZE):
  - DOWN class (every Ξ-target of strictly lower level, or «X»): best T = d exactly at d 3-6 (W 2 / 3): the CASC-M″ / FL-ANCHOR
    height bound, since D″ is then graded.
  - ACYC class from random starts: best 9 / 15 / 13 / 11 at (d, W, deg) = (4, 2, 2) / (4, 3, 3) / (5, 2, 3) / (6, 2, 2), below the
    R178 champions (which are ACYC and were climbed 10× longer).

## 3. Where compounding stops (DATA + READING)
- Per mover: AVN_x := transitions at which A(x) gains an option not available at the previous state (R178 Lemma XI-NEW: the least-level
  mover of every step after the first has one). Max AVN per level, big_d4: 5, 12, 10, 8; grow_top_N24: 2, 8, 9, 13, 5, 10, 9, 4.
  Moves at levels ≥ 1 track AVN (big_d4 level sums: AVN 23 / 17 / 15 vs moves 15 / 20 / 17).
- So at the top the key changes are plentiful (KCH 25-63) and do not release: a release needs a fresh Ξ-overtake among the mover's
  options, and those stay O(10) per mover. The missing statement is on the Ξ side, as R183 §4 / R186 §1 said, but now with σ̄ and τ
  removed as excuses: it must hold in the IDEAL-ACYC model itself.
- READING (the shape a counter would need): bottom movers have static keys (level 0: ≤ deg − 1 moves, FL-IDX-like), so fast «bits»
  must sit high in W-level. Each re-release of a high mover needs a strict Ξ-rise of one of its options past the current one, and Ξ is
  monotone. So the options' Ξ-plays must pass a Ξ-counter (movers whose choices raise the play's path set like a binary number 2^d
  times). Its low bits must reset while their own Ξ still rises (VJ), so a bit's two options must read different downstream vertices.
  No such Ξ-counter appeared in any search; R180's z3 bound (d 2: max 4 vs TB's 8) is the only exact data.

## 4. Files (experiments/red/r187/)
- stab.py (builder), stabrun.py (per-state TAU / SBAR / FB / WEQ check), ideal.py (IDEAL trajectory = r178/fastcyc rule),
  t2.py / realck.py (real vs IDEAL), rel.py (M, DREL, D2, KCH, AVN), table.py, findk.py (stuck-core search), downgen.py (DOWN / ACYC
  genomes), climb.py, dbg.py / t3.py (the two failure diagnoses: odd e-priorities; Ξ-cycles), pinck.sh (startck, zlk + verify, tl +
  verify, xeng). check.sh block «R187 REALIZE».

## 5. Next (Lead decides)
- Attack (me): a Ξ-counter inside IDEAL-ACYC (§3 shape), now worth building because anything found is a real family. Exact search
  for d = 3 in the ACYC model (R180's bmc.py restricted to acyclic Ξ, bit-vector encoding).
- Proof side (L-NEW): box 137's lemma cannot use σ̄-optimality or τ-stability beyond what IDEAL-ACYC already has; it must bound AVN (fresh
  Ξ-overtakes per mover) in IDEAL-ACYC, or count them against something monotone. DOWN-type stretches are already covered by CASC-M″.

## 6. Item 2: shortcut / up alternation at one W-cycle node (DATA; added after the first push)
- Construction (croot.py): the STAB+K+ESC game with the sink c_W replaced by an Even vertex c of the same top even priority whose
  options are ladder MOVERS. Every mover's W-play now returns to c, so c is the only W-cycle node; c's moves do not change W (every
  vertex keeps its length to c). A shortcut = an option of c below c's current option on its W-path (R185 Lemma CN-UP). c's
  availability reads the movers' Ξ; its choice is S1's cycle-node DFS rule over the current W-tree, which the ladder keeps changing.
- Climbs (cclimb.py: genome, c's option set and start; score = direction changes of c inside one FL run):

| seed (R178) | n | best FL run | c's moves in it | up / shortcut | direction changes | returns |
| --- | --- | --- | --- | --- | --- | --- |
| fl_d3_k4_W4 | 162 | 6 | 6 | 4 / 2 | 4 | 1 |
| big_d3_k3_W3 | 96 | 12 | 9 | 4 / 5 | 5 | 5 |
| big_d4_k3_W3 (pin cn_d4_n126) | 126 | 33 | 18 | 10 / 8 | 13 | 11 |
| big_d6_k3_W3 | 186 | 33 | 17 | 10 / 7 | 12 | 9 |
| grow_top_N24 (pin cn_g24_n246) | 246 | 64 | 22 | 12 / 10 | 19 | 14 |
- R185's cnidx.py on the pins (all FL runs of the N5 run): cn_d4 CNMOVES 19, UP 10, DOWN 9, RET 11, DOWN_NOSHORT 0; cn_g24 CNMOVES 23,
  UP 12, DOWN 11, RET 14, DOWN_NOSHORT 0. ovtkey: KBOUND 0, CNONLY 3 / 2. Both pins pass startck, Oink --zlk + verify, --tl + verify,
  xeng.
- READING: c moves alongside ladder moves (CNONLY ≤ 3): c's moves ride on the ladder's, about L_FL / 3 here. So CN-UP's open case is
  real and unbounded by |T_c|, but in these games it is charged to non-CN moves; a CNONLY bound per FL run is still the open item.
