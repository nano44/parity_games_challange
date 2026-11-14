# Box 139 N5-IDEAL: in IDEAL-ACYC every mover moves fewer times than both its number of Ξ-path values and its number of W-path keys (Proposition PATHS); so IDEAL-ACYC-POLY holds whenever every mover has logarithmic Ξ-depth or logarithmic W-level; D‴ is cyclic on stab_d4, so CASC-M‴ does not apply; a super-polynomial family needs a synchronised double counter
L-NEW successor 47, 2026-11-01 (date -u: see the commit). Lead GO 23:32Z (box 139: prove IDEAL-ACYC-POLY). Labels: PROVED (lane), CONJECTURE,
READING, DATA, DEAD, OPEN. G-N5-TIME stays OPEN. Not a TARGET.md claim.
Model: L-RED R178 §1 (claude/l-red 417d7fa6, docs/red/R178-ideal.md), with the Ξ-graph acyclic (IDEAL-ACYC).
- Movers x with level lev(x). Option k is a gate with a W-target wt (a mover of level lev(x) − 1, or c_W at level 0) and a Ξ-target xt (a
  mover, or the sink T), and a β of priority 4 + 2·rank + parity.
- τ = W-face and σ̄ = Ξ-face at every gate, by fiat. All W-values tie.
- Rule:
  - A_t(x) = {σ_t(x)} ∪ {k : face_t(k) ▷ face_t(σ_t(x))}, with face_t(k) the one-player valuation of the gate in G_X;
  - σ_(t+1)(x) = the root-first-key-least element of A_t(x), keys read from σ_(t+1) bottom-up;
  - a stuck step (σ_(t+1) = σ_t with I ≠ ∅) is the S4c fallback that ends the FL run.
- L-RED R187 Theorem REALIZE makes every IDEAL-ACYC run a real N5 FL run, so IDEAL-ACYC-POLY is necessary for N5-POLY.
Notation: Δ := max deg; t(x) := Ξ-depth of x (0 if every option's xt is T, else 1 + max t(xt)); VX(x) := number of distinct values of
Ξ-paths from x; VW(x) := number of distinct root-first keys of W-paths from x.

## 0. Answer
- First check (asked): D‴ is CYCLIC on stab_d4_n126. Its one S-stretch [0, 32] has the cycle 0 → 2 → 9 → 0 (Even movers only; dmerge3.py
  SHOWCYC=1). So CASC-M‴ and GATE-LEX (box 138) do not apply to the IDEAL ladders.
  - This agrees with R187: D″ is cyclic there too, and per-state D″ is cyclic at 33 / 33 states.
- PROVED (lane), Proposition PATHS (§1). In every IDEAL-ACYC run, for every mover x:
  - (a) x's current face value is non-decreasing, strictly increasing at each move of x, and always the value of a Ξ-path from x;
  - (b) x's root-first key is non-increasing, strictly decreasing at each move of x, and always the key of a W-path from x.
  - Hence moves(x) ≤ min{VX(x), VW(x)} − 1 ≤ min{Δ^(t(x)+1), Δ^(lev(x)+1)} − 1, and the run has ≤ Σ_x (min{VX, VW} − 1) steps.
- Corollary LOG-DEPTH (PROVED, lane). If every mover has min{t(x), lev(x)} ≤ c·log_Δ n, the run has ≤ n^(c+1) Δ steps. IDEAL-ACYC-POLY
  holds on that subclass. In particular it holds for bounded Ξ-depth (any W-depth) and for bounded W-depth (any Ξ-graph).
- Real-game corollary (PROVED, lane, on box 106 KEY-MON / FL-CANON (b) and FL-TIGHT). In a real FL run, an Even x ∉ CN moves ≤ π_W(x) − 1
  times. π_W(x) is the number of tight W-paths from x to its W-cycle node (c even), or |T_x| (c odd, FL-IDX). This sharpens R183 DEPTH's
  (Δn)^(ℓ*−1) to a path count, and it is polynomial for ℓ* = O(log n) at bounded tight out-degree.
- Exact obstruction (READING, §3). A super-polynomial IDEAL-ACYC family must contain movers whose Ξ-depth AND W-level are both ω(log n).
  It must drive each such mover through super-polynomially many strictly increasing Ξ-path values and, at the same moves, strictly
  decreasing W-keys: a synchronised double counter. The monotone orders alone cannot exclude it (R178 §2: crossings of monotone
  sequences on a grid of orders allow super-polynomial growth). Recipe for L-RED in §3.
- DATA (§2): on R178's champions (big_d3, big_d4, big_d8, grow_top_N24) both monotonicities hold at every step (0 violations), and the bound
  holds. It is tight only at level-0 movers (2 moves, 3 keys). The top movers make ≤ 10 moves against VX up to 8,799 and VW up to 6,561.
- IDEAL-ACYC-POLY itself: OPEN. Its whole difficulty is now the case «Ξ-depth and W-level both super-logarithmic at the same mover».

## 1. Proposition PATHS (PROVED, lane)
Setting: an IDEAL-ACYC run σ_0, σ_1, … up to its stop. G_X under σ_t is a functional graph that is acyclic (the Ξ-graph is acyclic), so
every value is (rew(T), w, len). w is the signed weight Σ ±2^(prio β) over the β's on the path, + for even priority. Values compare as
si.py Engine.key (R178 §1).
- Lemma VAL-MONO. face_(t+1)(v, k) ⊵ face_t(v, k) for every gate, and cur_(t+1)(x) ▷ cur_t(x) for every mover x that moves at step
  t → t + 1, where cur_t(x) := face_t(x, σ_t(x)). Also cur_(t+1)(x) ⊵ cur_t(x) for every mover.
  - Proof by induction down a topological order of the Ξ-graph (xt after x).
    - face(v, k) = β_k ⊕ val(xt), with val(T) constant and val(y) = y ⊕ gate ⊕ face(y, σ(y)) for a mover y. ⊕ by a fixed vertex adds a
      constant to w (or 0) and 1 to len, so it preserves ⊴ and ◁.
    - For xt_k later in the order, val_(t+1)(xt_k) ⊵ val_t(xt_k) by induction, hence face_(t+1)(v, k) ⊵ face_t(v, k).
    - If x moves at t → t + 1 to k ∈ A_t(x) \ {σ_t(x)}: cur_(t+1)(x) = face_(t+1)(x, k) ⊵ face_t(x, k) ▷ face_t(x, σ_t(x)) = cur_t(x).
    - If x does not move: cur_(t+1)(x) = face_(t+1)(x, σ_t(x)) ⊵ cur_t(x).
    - So val_(t+1)(x) ⊵ val_t(x) as well, which closes the induction. ∎
- Lemma KEY-MONO (the IDEAL form of box 106 KEY-MON / R183 OVT-KEY step 2). key_t(x), the root-first key of x's current option read
  from σ_t, is non-increasing and strictly decreasing at each move of x.
  - Proof by induction on lev.
    - key_t(x) = key_t(wt(x, σ_t(x))) · gate(x, σ_t(x)), with key of c_W empty.
    - σ_(t+1)(x) is the key-least element of A_t(x) ∋ σ_t(x), with keys read from σ_(t+1). So key_(t+1)(x) ≤ key_(t+1) via σ_t(x), and
      that equals key_(t+1)(wt) · gate ≤ key_t(wt) · gate = key_t(x) (induction; equal-length sequences).
    - Keys are injective (the last gate index determines the option), so the inequality is strict when x moves. ∎
- Proposition. cur_t(x) is the value of the Ξ-path x → σ_t(x) → … from x, so it lies in the value set of Ξ-paths from x, which has size
  VX(x). key_t(x) is the key of a W-path from x, a set of size VW(x). Both sequences are strictly monotone at moves (the lemmas above), so
  moves(x) ≤ min{VX(x), VW(x)} − 1.
  - Counting paths: VX(x) ≤ Σ_k VX(xt_k) ≤ Δ^(t(x)+1), and VW(x) ≤ Δ^(lev(x)+1).
  - Every non-stuck step moves at least one mover, so steps ≤ Σ_x (moves(x)) ≤ Σ_x (min{VX(x), VW(x)} − 1). ∎
- Corollary LOG-DEPTH: immediate. Since lev(x) ≤ d and t(x) ≤ N, the bound is polynomial as soon as, at each mover, one of the two depths
  is O(log n).
- Real FL runs (PROVED, lane): the same W-side argument holds verbatim on the tight W-DAG (keys of tight paths, FL-TIGHT; KEY-MON strict at
  movers; c odd: index order, ≤ |T_x| − 1). The Ξ-side has no polynomial value set in the real game: values are play values under
  varying σ̄, a set of up to exponential size even at bounded W-depth. So only the W-side corollary transfers.

## 2. DATA
Tool: experiments/new/box139/paths.py. Values come from fastcyc_r178.py, a read-only copy of claude/l-red experiments/red/r178/fastcyc.py
(sha1 cee2192f9711…, identical to the l-red file at 417d7fa6). The step rule is r187/ideal.py traj, re-implemented. Genomes are copied
read-only from claude/l-red experiments/red/r178/out/ into box139/genomes/.

| genome (R178) | movers | steps | stop | moves | max moves of one mover | max VX | max VW | value / key monotonicity violations | bound violations | max moves / (min{VX, VW} − 1) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| big_d3_k3_W3 | 9 | 17 | stuck | 33 | 7 | 89 | 27 | 0 / 0 | 0 | 1.0 (level 0) |
| big_d4_k3_W3 (= R187 pin stab_d4_n126) | 12 | 32 | stuck | 57 | 10 | 833 | 81 | 0 / 0 | 0 | 1.0 (level 0) |
| big_d8_k3_W3 | 24 | 54 | stuck | 108 | 9 | 3,665 | 6,561 | 0 / 0 | 0 | 1.0 (level 0) |
| grow_top_N24 (= R187 pin stab_g24_n246) | 24 | 64 | stuck | 119 | 10 | 8,799 | 6,561 | 0 / 0 | 0 | 1.0 (level 0) |
- The steps equal R187's real L_FL (32, 64, 17, 54), and the moves equal R187's (57, 119).
- dmerge3.py on stab_d4_n126 (L-RED pin copied read-only into box139/inst/, 8 / 8 sha1 OK against l-red pins.sha1): «SSTRETCHES 1 FL 32
  ACYC 0 CYC 1 … SBIN 0 TIES 0», cycle 0 → 2 → 9 → 0.

## 3. The exact obstruction and a recipe for L-RED (READING)
- From PATHS, a mover with M moves needs VX(x) > M and VW(x) > M, so Ξ-depth ≥ log_Δ M and W-level ≥ log_Δ M. Moreover, its M moves pick
  M Ξ-path values in strictly increasing order and, at the same moves, M W-keys in strictly decreasing order.
- Each move of x needs (as in R178 XI-NEW):
  - a fresh Ξ-overtake among its options, caused by moves on the overtaking option's Ξ-play (Ξ-side, upward in the Ξ-order); and
  - the new option key-smaller than the current one at that moment, caused by W-key drops below (W-side, downward in level).
  So the counter must run on BOTH sides and in step. A Ξ-only counter leaves the keys static and x stops after < VW moves; a W-only counter
  (LADDERBF) needs availability that only a Ξ-counter supplies.
- Recipe (an IDEAL-ACYC genome shape, all movers in one W-ladder):
  - W side: R177 LADDERBF's 2-wide ladder (levels 1..d, two movers per level, options through gates to both movers one level down).
  - Ξ side: every mover's two Ξ-targets point UP the ladder (to the two movers of a higher level, acyclic by level). β ranks are allotted
    so that a lower level's Ξ-face weight dominates all higher ones, which makes the values of a mover's two options a binary number in
    the choices above it.
  - Then a key drop at level j (W side) must coincide with a Ξ-overtake at level j, fed from level > j. That is exactly the upward read
    that closes stab_d4's D-cycle (0 → 2 → 9 → 0).
  - Score: moves of the top-level movers against 2^d. PATHS caps a level-j mover at 2^(j+1) − 1 on the W side, which is LADDERBF's
    per-mover count, so LADDERBF is the target to match.
- Proof side, if the recipe fails: the next statement to try is a JOINT bound. Along x's moves the pair (Ξ-path, W-path) changes with value
  ↑ and key ↓, and x's options read lower movers on the W side and higher movers on the Ξ side. A potential mixing Ξ-topological level
  and W-level (Lead's suggestion) has to exploit that the two sides are read in opposite directions of one acyclic order. PATHS uses each
  side separately and so cannot see this.

## 4. Status
- PROVED (lane): Lemma VAL-MONO, Lemma KEY-MONO, Proposition PATHS, Corollary LOG-DEPTH (IDEAL-ACYC); the real-FL W-side corollary
  (moves of x ∉ CN ≤ π_W(x) − 1).
- DATA: §2 (0 violations; bound tight only at level 0). D‴ cyclic on stab_d4_n126.
- OPEN: IDEAL-ACYC-POLY when some movers have super-logarithmic Ξ-depth and W-level. READING: §3. CONJECTURE: none new (IDEAL-LIN stays
  R178's).
