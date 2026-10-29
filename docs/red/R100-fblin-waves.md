# R100: FB-LIN attack, box 1. Anatomy of the record (one detachment wave), a level-1 template, why a second wave over the same vertices does not come back, climbs
L-RED successor 24 (Opus 5.5; D14/D15/D18; Lead 2026-10-29 00:28Z: kill CONJECTURE FB-LIN, "at most n in-phase fallbacks in one phase"; find a
phase with f > n or a family where f/n grows). Written 2026-10-29 from 01:10Z (date -u). Labels (D18 / L40): DATA / READING / OPEN.
No kill. FB-LIN stands on everything tried here. What follows records the mechanism of the record, the one-wave template that reproduces it,
the design obstruction that stopped every two-wave design, and the climbs.

Tools (experiments/red/fb/): fbphase.py (f = in-phase fallbacks per phase, phases as phsw.py), dsl.py (hand constructions), lvl1.py (the
level-1 template), chainclimb.py (structured climb: fixed chain + mutable gadget), topo2.py (priority search on a fixed two-wave topology),
fbclimb.py (fixed-n climb for f, TAUSTAR start). Climb logs stay in the scratchpad (summarised in §4).

## 0. Setting
- N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md). In a phase τ is fixed; an in-phase fallback is Even's (FIX 3). S4a moves σ to Even's
  W-optimum against τ inside A(v) = {σ(v)} ∪ Iσ(v), where Iσ is read from Ξ (σ against Odd's best reply σ̄). S4c fires only when S4a and S4b
  change nothing, and then switches EVERY Even vertex with an improving edge to its (Ξ, index)-best improving edge.
- W_t := the valuation of the (σ_t, τ)-play. At every Odd vertex Ξ ⪯ W (σ̄ is Odd's best reply), so a switch v: cur → new that S4c makes
  and S4a refused satisfies Ξ(cur) ≺ Ξ(new) ⪯ W(new) ⪯ W(cur): the current route passes an Odd vertex g with σ̄(g) ≠ τ(g) (an open GATE).
- Theorem FB-C^K (docs/new/P-N5-FBCK-box49.md, lane-proved, one referee signature): f ≤ n_K·|𝒞^K_f(P)|. So f > n needs at least two
  K-configurations at fallback sources, and (since each fallback switches at least one Even vertex and a vertex can only be detached once per
  wave, below) SOME Even vertex switched by fallbacks under two configurations: vertex REUSE.
- TAUSTAR start (used in §3-§4): τ0 := the final τ of a pre-run from the same σ0. That τ is an SI fixpoint for Odd, so Iτ = ∅ at every
  state (Iτ depends on τ only), τ never moves, and the run is one phase until a cycle node of Ξσ changes. It is a legal N5 start pair
  (SPEC: "Optional start pair"); every reported count is re-run from the written full start.

## 1. DATA: the record is one detachment wave
| instance | n | f (max per phase) | anatomy |
| --- | --- | --- | --- |
| rise_fb38_n48 (red/so/instances, S3) | 48 | 37 = 0.77n (phase from state 4) | iterations 16-49: 34 consecutive fallbacks, each switching ONE vertex to the vertex switched one step earlier: 42→31, 12→42, 15→12, 44→15, … , 16→35, 45→16; σ̄(0) = 2 throughout |
| farrise25_n32 (red/so/instances, S3) | 32 | 25 = 0.78n | iterations 8-32: the same, 16→8, 21→16, 13→21, … , 1→18; then 4→1 (S4a), 8→0 (S4a) and σ̄(0): 4 → 11 |
- fbphase.py reproduces the library maxima (37, 25). τ is constant in both runs (farrise: Iτ = ∅ at every state, checked).
- Mechanism (farrise, vertex names as in the file). Gate 0 (Odd): τ(0) = 11 (Odd's loop, prio 18), σ̄(0) = 4 → 23 (odd 31), so Ξ(0) ≪ W(0).
  The chain vertices first all point at 10 → 0 (S4a, iteration 6: W-best). Source 8 (even 30) → 23. 16 → 8 is Ξ-improving (8 beats the
  gate route below 23) and W-worse (the W route of 10 avoids 23): S4a refuses, S4c takes it. Then each predecessor sees the same, one per
  fallback. The wave ends at 1; 4 → 1 (the gate's σ̄ branch now reads the detached chain) and 8 → 0 close the gate (σ̄(0) = 11 = τ(0)).
- Iτ = ∅ for the gate needs an Even escape on its σ̄ branch worth more than τ's branch, that the current σ cannot yet take: here
  4 → 1 → (chain, detached direction) → 8 → 0 → τ. The escape is realised exactly when the wave completes. That is why the gate closes then.

## 2. DATA: the level-1 template (lvl1.py) reproduces the record with f = m at n = m + 7
Vertices (priority): T (Odd sink loop, 1); q1 (Odd gate, 105; τ → T1, σ̄ → x1); T1 (Even → T, 120); x1 (Even, 104; → Y, c_m); Y (Odd → T,
131); s1 (Even, 126; → Z1, q1); Z1 (Odd → T, 129); chain c_i (Even, prio 2i + 1; → q1, c_{i−1}; c_0 = s1), start c_i → q1, x1 → Y, s1 → Z1,
τ(q1) = T1 (S3).
- Run (m = 8): iterations 1-8 are fallbacks c1 → s1, c2 → c1, …, c8 → c7; then x1 → c8 and s1 → q1 (S4a); σ̄(q1) = T1; stop. m = 30: f = 30,
  n = 37, iterations 32, one phase.
- The chain priorities must be ODD and above the sink's: with even chain priorities c_i → c_{i−1} is S4a-improving while c_{i−1} is still
  attached, and with chain priorities below the cycle node only lengths count (iteration-1 cascade). Both were observed (first drafts).
- So a single wave gives f = n − O(1), the same 0.78n shape as the library maxima. FB-LIN needs a SECOND wave over the same chain.

## 3. READING: why the second wave does not come back (design obstruction, not a theorem)
A second wave over the chain needs, after wave 1, (a) a NEW source s whose Ξ exceeds the chain's new values, and (b) for each chain vertex a
current route through an open gate (§0). Wave 1 changes only the chain, so (a) must come from a vertex that READS the chain (its value
rises when the chain's end detaches). Every design tried reduces to two inequalities on the same vertex set:
- SAFETY during wave 1: the reader must not see the chain as improving while the chain's end still routes back through the reader's own
  structure (the attached gate, or the source itself). Ξ-improvement of a switch that closes a cycle is decided by the parity of the
  cycle's top, so this says: the cycle through the reader is ODD-topped, i.e. a prefix weight p < 0.
- RISE after wave 1: the post-wave Ξ-improvement (re-attach to the reader's gate, or the chain end switching to the released source) compares
  the SAME prefix against the SAME tail (the chain's new value), so it needs p > 0 (up to chain vertices, whose priorities are the lowest and
  cannot flip the sign).
Concretely (signed weights w(v) = ±2^rank(v), a = w(c_m), all three designs below were also run with topo2.py / dsl.py drafts):
- (O-A) Re-attach to a gate G whose σ̄ branch reads the chain end through a reader r (r → {Y, c_m}, G → {T_G, r}). Non-attraction of G
  during wave 1 for attached c_i: g := w(G) + w(r) < w(q1) + w(x1) =: b + c. Trigger safety (r → c_m while c_m → q1 → x1 → Y): a + b + c < 0.
  Re-attach of c_m after wave 1: g + a > 0. Hence −a < g < b + c < −a. Contradiction.
- (O-B) Bidirectional chain (c_i → c_{i−1}, c_{i+1}) with a released top source: z (Odd) → {S, B_z}, S (Even) → {P, c_m}, c_m → z. With
  D := Ξ(B_z) − Ξ(c_{m−1}) (signed): release needs D < w(S) + a, wave 2 needs w(z) + D > 0, and safety (once c_m points at z, S → c_m closes
  the cycle c_m z S) needs a + w(z) + w(S) < 0. Contradiction. The variant with a LOCK instead (c_m never points at z during wave 1) needs
  Ξ(z) below the attached value, which forces P to be the gate's own poison Y; the lock then reads w(z) + w(S) < b + c and the trigger reads
  a + b + c < 0, with the same contradiction. z reading c_m directly (z → {c_m, B_z}): D < a and D > −w(z) with z above c_m. Contradiction.
- (O-C) Bidirectional chain with the top source z reading the top gate's reader x_T (z → {x_T, B_z}): the rank arithmetic forces
  w(z) + w(u) ∈ (2^r, 2^r + 2^s) for vertices of ranks other than r = rank(c_m) and r + 1 = rank(x_T); no such set exists.
- (O-D) Release by an Even-won cycle (the level-1 close, §2, releases the gate to its τ value, which is NOT bounded by the reader's value,
  because the held branch became an even-topped cycle). Top source z (Odd) → {S, B_z}, S (Even, even top) → {Y, c_m}, c_m → z: the wave-2
  step c_m → z closes z S c_m, Odd leaves S, and Ξ(z) jumps to B_z (any height). It fails on the lock: Ξ(z) = {z, S} ∪ Ξ(Y) must stay below
  c_m's attached value {q1, x1} ∪ Ξ(Y), so the top of {z, S, q1, x1} is odd in {z, S} (then z S c_m is odd-topped, no release) or even in
  {q1, x1} (then the trigger cycle {c_m, q1, x1} is even-topped, early trigger). Without the lock, c_m → z at the first fallback and the
  cycle z S c_m forms at once: wave 2 starts from the top while wave 1 runs from the bottom, and the two meet (each vertex switched once).
- What survives: W can be raised freely after wave 1 (W is not in the phase definition). An Even vertex t on the bottom gate's τ branch
  that reads c_m (t → {low, c_m}) turns W(q_B) into an Even-won W-cycle the moment wave 1 ends, so W(cur) ≥ W(new) holds for the whole of a
  downward wave 2 with no τ change. The obstruction is only on the Ξ side: the source.
- The same shape as L-SI's RUN-LIN obstruction (docs/si/N5-RUNLIN-box24.md §4, l-si: "the escape of the top level must be Ξ-closed"), which
  L-SI's runfam family circumvented for S4a waves with ONE Odd gate whose options are the two ends of a corridor (each σ̄ flip of the gate
  starts the next wave, runfam_K10: the corridor 37-48 is walked three times). The fallback analogue needs, in addition, W to favour the
  current direction at every wave. Not built (OPEN, §5).

## 4. DATA: climbs (no kill)
- chainclimb.py (fixed chain of m Even vertices + 14 mutable gadget vertices, seeded with the level-1 template, TAUSTAR, fitness = excess
  of f over m at m = 6 and m = 12; 4 seeds, ~5-25 min each): best f = m + 5 at both sizes (f(12) = 17 at n = 26). Extra gadget vertices add
  one fallback each; no slope above one per chain vertex, so no second wave. An earlier fitness (slope f(12) − f(6)) was gamed by breaking
  the m = 6 instance (f(6) = 0); replaced.
- topo2.py (priorities and optional edges on the two-wave topology of §3 (O-B), TAUSTAR): best f = 2 at m = 6 and 12.
- fbclimb.py (fixed n, fitness 1000 f + total fallbacks; mutations: priority, edge add / delete, Even start entry). Runs of 25-40 min (the
  first batch was cut at ~25-30 min by a container restart; the scratchpad survived):
  | seed | start | n | f at seed | best f | best f / n | shape of the best |
  | --- | --- | --- | --- | --- | --- | --- |
  | lvl1 + 14 spare vertices | TAUSTAR | 51 | 30 | 31 | 0.61 | one wave |
  | runfam_K10 (l-si) | TAUSTAR | 49 | 0 | 1 | 0.02 | runfam's waves are S4a waves; no fallback structure to grow |
  | rise_fb38_n48 | TAUSTAR / own (S3) | 48 | 35 / 37 | 37 / 37 | 0.77 | one wave (unchanged) |
  | farrise25_n32 | TAUSTAR / own (S3) | 32 | 25 / 25 | 25 / 25 | 0.78 | one wave (unchanged) |
  | pl130_n40 (R97) | own | 40 | 11 | 15 | 0.38 | short carries |
  | long121_n40 (R96-R98) | own | 40 | 8 | 25 | 0.63 | ONE wave: fallbacks at iterations 13-35 consecutive (23 in a row, phase of 36); long121's multi-carry structure is gone |
- Reading: f-climbs from every seed converge to the single-wave shape (f ≤ 0.78n). From long121 the climb trades the 8 reused carries for one
  long wave. No climb produced vertex reuse at scale. The climbs do not test the corridor-gate design of §5.
- Misread caught during the box: an interim look at the logs credited f = 31 to the farrise25 climb (it would have been 0.97n); `tail -q`
  had printed the lvl1 climb's line (n 51). Re-running fbphase.py on the saved farrise game gave 25. Every number above is re-run
  from the saved .pg / .start.

## 5. OPEN and next
- The fallback analogue of L-SI's runfam: one Odd gate whose options are the two ends of a corridor, so that each wave's arrival flips the
  gate (a new K-configuration) and starts the next wave; W must favour the current direction at every wave (the W-cycle device of §3 does
  this once). Not built.
- long121_n40 reuses fallback-switched vertices across configurations (23 → 4 at the fallbacks of iterations 6 and 56; 36 → 31 at 38, 56,
  68, 98), with long S4a stretches and σ̄ flips in between. So the §3 obstruction (only the chain changed since the last wave) does not cover
  designs where S4a cascades run between fallbacks. A carry cell that detaches Θ(n) vertices per carry is the open design.

## DONE / FINDINGS / NEEDS
- DONE: R100 (this file) with tools experiments/red/fb/ (fbphase.py, dsl.py, lvl1.py, chainclimb.py, topo2.py, fbclimb.py); check.sh pins
  lvl1 (f = 8 at m = 8) and fbphase.py's library maxima (37, 25). Pushes 674fb359, 469acd9c, and this one.
- FINDINGS:
  - The FB-LIN record (37 = 0.77n) and farrise25 (0.78n) are each ONE detachment wave under one configuration; a 7-vertex template gives
    f = m at n = m + 7 for every m.
  - A kill needs vertex reuse across two configurations. Four second-wave designs die on one inequality pair (in-wave safety p < 0, post-wave
    rise p > 0 on the same reader prefix): DESIGN OBSTRUCTION (READING), not a theorem.
  - W is not the obstacle: an Even reader on a gate's τ branch can turn W into an Even-won W-cycle after a wave, with τ fixed.
  - f-climbs from six seeds converge to the one-wave shape (max 0.78n); from long121 the climb gives up reuse for one long wave (8 → 25).
  - FB-LIN: no kill, CONJECTURE stands; data max unchanged at 0.78n.
- NEEDS: none from the owner.
