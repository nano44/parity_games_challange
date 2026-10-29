# R107: the mkr family from the S3 default start. On mkr as built, the S3 start ends in 3 iterations. Embedded so that S3 lands on the designed start (s3embed.py), N5 makes 4K² + 3K iterations from the S3 DEFAULT START at n = 60K + 13 (≈ n²/900). Pin s3quad_K8_m30: 264 iterations at n 479.
L-RED successor 26 (Opus 5.5; D15/D18; Lead 2026-10-29 11:07Z STEP 1: «(a3) the S3 DEFAULT start: run length, phases, longest
fallback-free run ... (b) per-vertex switch counts inside the long run ... (c) total N5 iterations to termination (explicit start and S3
start), and the number of phases and runs. Report these as R107 (DATA) with the S3 result stated plainly, whichever way it goes»).
Written 2026-10-29 (date -u stamps in the commit). Labels: DATA / READING / OPEN. Not a TARGET.md claim. G-N5-TIME stays OPEN: every
count here is polynomial (quadratic).

## Summary
| item | label |
| --- | --- |
| mkr.py K 4K as built (R106), S3 DEFAULT start: 3 iterations, 0 fallbacks, 4 phases, longest run 0, at every K = 2..14. S3 puts h on its top option C_K and h′ on Cp_K at once, so the designed climb does not occur. **On the family as built, the quadratic run needs the explicit start.** | DATA |
| s3embed.py: a dummy vertex on every edge. Priorities 0..3 sit below every cycle node, so dummies never enter a path set and every play length doubles. The dummy priorities steer SPEC S3 to the designed start. From the S3 DEFAULT start, the embedded mkr K 4K runs exactly the R106 run: 4K² + 3K iterations, 1 fallback-free run of 4K² + 3K − 1 transitions, 2 phases, 0 fallbacks, at n = 60K + 13. | DATA |
| pin s3quad_K8_m30 (embedded runquad_K8_m30_n192): 264 iterations from S3 at n 479. Two engines: identical state sequences. Oink zlk OK, both strategies verified, for both engines' outputs. | DATA |
| (b) inside the long run: max switches of one vertex = 2K − 1 (reactor r_1); max Ξ-changes of one vertex = 2K − 1; Σ_v switches(v) = 8K² − 1 (≥ run length 4K² + 3K − 1); L-SI's per-vertex bound switches(v) ≤ Σ_succ (Ξ-changes + 1) holds at every vertex, tight to slack 1 at h | DATA |
| the caveat of R105/R106 ("explicit start only") is removed for R106's family: N5's TOTAL iteration count from SPEC S3 is Ω(n²) on an explicit family | DATA |

## 1. The script and the definitions (experiments/red/seg/r107.py)
- r107.py GAME START|S3. It runs L-COMP's n5b in SPEC mode. With "S3" it passes no start, so SPEC S3 / n5b's best-reward start is used.
- It also runs the second engine: L-NEW's experiments/new/n5.py driver on L-SI's si.py valuations, with no start for S3. It compares
  the full (σ, τ) state sequences, as xeng.py does.
- PHASE: τ, λ_σ (cycle nodes of Ξ_σ on G) and λ_τ (cycle nodes of Ξ_τ on G^d) all constant. This is the definition of
  experiments/red/sel/phsw.py and RESULTS R21 ff.
- RUN: segchk.py's definition: τ and the honest λ constant, and no fallback inside.
- Per-vertex counts inside the longest run [a, b]:
  - switches(v) = #{t ∈ [a, b): σ_t(v) ≠ σ_{t+1}(v)};
  - Ξ-changes(w) = #{t: Ξ_t(w) ≠ Ξ_{t+1}(w)}. Ξ is monotone, so these are rises;
  - slack(v) = Σ_{w ∈ succ(v)} (Ξ-changes(w) + 1) − switches(v), over Even v with ≥ 2 distinct successors.

## 2. (a3) + (c): mkr.py K m = 4K as built (R106 generator, unchanged)
| K | m | n | explicit start: iterations / fallbacks / phases / runs / longest run | S3 default: iterations / fallbacks / phases / runs / longest run | engines |
| --- | --- | --- | --- | --- | --- |
| 2 | 8 | 54 | 22 / 0 / 2 / 2 / 21 | 3 / 0 / 4 / 4 / 0 | identical (both starts) |
| 3 | 12 | 78 | 45 / 0 / 2 / 2 / 44 | 3 / 0 / 4 / 4 / 0 | identical |
| 4 | 16 | 102 | 76 / 0 / 2 / 2 / 75 | 3 / 0 / 4 / 4 / 0 | identical |
| 5 | 20 | 126 | 115 / 0 / 2 / 2 / 114 | 3 / 0 / 4 / 4 / 0 | identical |
| 6 | 24 | 150 | 162 / 0 / 2 / 2 / 161 | 3 / 0 / 4 / 4 / 0 | identical |
| 7 | 28 | 174 | 217 / 0 / 2 / 2 / 216 | 3 / 0 / 4 / 4 / 0 | identical |
| 8 | 32 | 198 | 280 / 0 / 2 / 2 / 279 | 3 / 0 / 4 / 4 / 0 | identical |
| 9 | 36 | 222 | 351 / 0 / 2 / 2 / 350 | 3 / 0 / 4 / 4 / 0 | identical |
| 10 | 40 | 246 | 430 / 0 / 2 / 2 / 429 | 3 / 0 / 4 / 4 / 0 | identical |
| 11 | 44 | 270 | 517 / 0 / 2 / 2 / 516 | 3 / 0 / 4 / 4 / 0 | identical |
| 12 | 48 | 294 | 612 / 0 / 2 / 2 / 611 | 3 / 0 / 4 / 4 / 0 | identical |
| 13 | 52 | 318 | 715 / 0 / 2 / 2 / 714 | 3 / 0 / 4 / 4 / 0 | identical |
| 14 | 56 | 342 | 826 / 0 / 2 / 2 / 825 | 3 / 0 / 4 / 4 / 0 | identical |
- Explicit start: iterations = 4K² + 3K. The second phase and second run are the single final state after the λ change at the run's end
  (R106 §2, t = 20 for K 3 m 4).
- **The S3 start, stated plainly.** S3 gives h → C_K (h's top option) and h′ → Cp_K. τ(C_i) and τ(Cp_i) start on the honest escapes Bq_i.
  - The trace for K 3 m 12, at the vertices that matter:
    - state 0: h C3, h′ Cp0;
    - state 1: h′ → Cp3;
    - state 2: w1, u1 → T1, Tp1 and τ(Cp_i) → MPp_i;
    - state 3: τ(C_i) → MP_i. This is the final state.
  - No reactor ever moves. The family's quadratic run needs the designed start, in which both pivots sit at the bottom of their
    ladders and every τ(C_i) is on the W-route.

## 3. (a3) repaired: an embedding whose S3 start IS the designed start (experiments/red/seg/s3embed.py)
**Construction.** G ↦ G′:
- every edge (v, w) becomes v → d_vw → w, with a fresh one-successor dummy d_vw (owner Odd; irrelevant, one successor);
- every original priority is shifted by +4, so parities are kept;
- dummy priorities are 0..3:
  - Even v: 2 on the start edge, 1 elsewhere;
  - Odd v: 3 on the start edge, 0 elsewhere;
  - one-successor v: 2 or 3.

**Why it preserves the run (READING; checked as DATA below).**
- Every cycle of G′ is the image of a cycle of G, and its top is an original vertex. Dummies lie below every cycle node, so they
  never enter a path set (S1).
- Every play of G′ is the image of a play of G with exactly one dummy per edge. Its length is 2 × the old length, so every length
  comparison (longest or shortest, ties) keeps its outcome.
- S1's DFS / BFS tie rules follow successor-list order. s3embed keeps each vertex's successor order, and the dummies have one
  successor each.
- S3 (SPEC: Even maximises (r(w), ±w), r = Ω if even else −Ω; Odd the same on G^d with Ω + 1):
  - an Even vertex's successors are its dummies, and r = 2 beats r = −1;
  - an Odd vertex's dummies have dual priorities 4 (start edge) and 1, and r = 4 beats r = −1.
  - So S3's σ and τ are the images of the designed start.
- n′ = n + Σ_v |succ(v)|. For mkr K 4K, n′ = 60K + 13.

**DATA (r107.py on G′ from S3; "same as image" = the n5b S3 trace equals the n5b trace from the image of mkr's explicit start).**
| K | m | n′ | S3 iterations / fallbacks / phases / runs / longest run | n5.py iterations, states identical | same as image |
| --- | --- | --- | --- | --- | --- |
| 2 | 8 | 133 | 22 / 0 / 2 / 2 / 21 | 22, True | True |
| 3 | 12 | 193 | 45 / 0 / 2 / 2 / 44 | 45, True | True |
| 4 | 16 | 253 | 76 / 0 / 2 / 2 / 75 | 76, True | True |
| 5 | 20 | 313 | 115 / 0 / 2 / 2 / 114 | 115, True | True |
| 6 | 24 | 373 | 162 / 0 / 2 / 2 / 161 | 162, True | True |
| 7 | 28 | 433 | 217 / 0 / 2 / 2 / 216 | 217, True | True |
| 8 | 32 | 493 | 280 / 0 / 2 / 2 / 279 | 280, True | True |
| 9 | 36 | 553 | 351 / 0 / 2 / 2 / 350 | 351, True | True |
| 9-14 | | | running at this push; an addendum will add these rows | | |
- Every row reproduces §2's explicit-start count exactly (iterations 4K² + 3K). So N5's total iteration count FROM THE S3 DEFAULT
  START on this explicit family is 4K² + 3K at n′ = 60K + 13, i.e. ≈ n′²/900.

**Pins (experiments/red/seg/instances/; check.sh gates the small one).**
| pin | sha1 | n | from S3: n5b / n5.py | Oink (zlk + both strategies) |
| --- | --- | --- | --- | --- |
| s3quad_K3_m4.pg (= s3embed of runquad_K3_m4_n54) | 675778af8ea65724a053fe1e4cbbf8b8fe33f8ad | 137 | 21 / 21 iterations, 0 fallbacks, states identical | OK on both outputs |
| s3quad_K8_m30.pg (= s3embed of runquad_K8_m30_n192) | 9576333116f710a7576eb8c3055908e497f09b85 | 479 | 264 / 264 iterations, 0 fallbacks, states identical; longest run 263, 2 phases | OK on both outputs |
- The `.image.start` files (sha1 498cfa1e…, 3a0f3932…) are for checking only. The pins need no start.

## 4. (b): per-vertex counts inside the long run (mkr K 4K, explicit start; the same numbers on the embedded games from S3 where measured: K 7, 8 and the K8 m30 pin)
| K | n | run L | max_v switches(v) (vertex) | switchers | Σ_v switches(v) | max_w Ξ-changes(w) | min_v slack (vertex) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 54 | 21 | 3 (r1) | 13 | 31 | 3 | 1 (h) |
| 3 | 78 | 44 | 5 (r1) | 19 | 71 | 5 | 1 (h) |
| 4 | 102 | 75 | 7 (r1) | 25 | 127 | 7 | 1 (h) |
| 5 | 126 | 114 | 9 (r1) | 31 | 199 | 9 | 1 (h) |
| 6 | 150 | 161 | 11 (r1) | 37 | 287 | 11 | 1 (h) |
| 7 | 174 | 216 | 13 (r1) | 43 | 391 | 13 | 1 (h) |
| 8 | 198 | 279 | 15 (r1) | 49 | 511 | 15 | 1 (h) |
| 9 | 222 | 350 | 17 (r1) | 55 | 647 | 17 | 1 (h) |
| 10 | 246 | 429 | 19 (r1) | 61 | 799 | 19 | 1 (h) |
| 11 | 270 | 516 | 21 (r1) | 67 | 967 | 21 | 1 (h) |
| 12 | 294 | 611 | 23 (r1) | 73 | 1151 | 23 | 1 (h) |
| 13 | 318 | 714 | 25 (r1) | 79 | 1351 | 25 | 1 (h) |
| 14 | 342 | 825 | 27 (r1) | 85 | 1567 | 27 | 1 (h) |
- max switches(v) = 2K − 1 ≈ n/12, at the reactor r_1. Every reactor flips once per pivot step. Σ_v switches(v) = 8K² − 1 ≈ 2 × L.
  A flip of the chain is one transition with m switches; a wave is m transitions with one switch each.
- L-SI's per-vertex inequality switches(v) ≤ Σ_{w ∈ succ(v)} (Ξ-changes(w) + 1) holds at every vertex at every K. The minimum slack is
  1, at the pivot h.
- max Ξ-changes = 2K − 1, linear in n. So a run-length bound of the form L ≤ Σ_v switches(v) ≤ Σ_v Σ_succ (Ξ-changes + 1) gives only
  O(n² · deg) here. That is consistent with the quadratic count, and it says nothing beyond it.

## 5. What this means for N5 (READING)
- R106's quadratic run is not an artefact of the explicit start. Up to the embedding (a constant factor 2.5 in n), N5 from its own S3
  start makes Θ(n²) iterations on an explicit family. The longest run and longest phase are Θ(n²) as well.
- G-N5-TIME is not touched: quadratic is polynomial. What this rules out is any O(n)-iteration (or O(n)-per-phase) bound for N5 from
  S3 on general games.
- s3embed.py is generic. Any explicit-start pin can be carried to an S3-start instance at a factor ≤ 1 + maxdeg in n. The run is kept
  whenever the start pair is a valid N5 state. The equality is checked per instance, as "same as image", not assumed.
- Toward (a2) (OPEN): within one run every vertex's Ξ-changes are bounded by the number of pivot steps, here by the number of gates
  (Θ(n)). A super-quadratic run needs a vertex with super-linearly many Ξ-changes, i.e. a source whose value climbs through many path
  sets at polynomial cost (a counter). STEP 2 works on that.

## 6. Concordance with R106's addendum (successor 25, l-red 011c6e3e, pushed while this note was in review)
- successor 25's whole.py reports the same iteration counts at every shared row (S3: 3; designed start: 22 / 76 / 162 / 280 / 264) and the same
  per-vertex maxima (2K whole, 2K − 1 in the run).
- Phase counts differ by definition only. whole.py cuts phases at τ changes only, giving "1 phase" (designed start) and "3 phases" (S3).
  r107.py cuts at changes of τ, λ_σ or λ_τ (phsw.py's definition), and counts the final state after the λ-changing last transition as
  its own (empty) phase: 2 and 4.
- New here, beyond the addendum: the S3 question it left OPEN ("whether some prefix leads N5 from S3 into the designed start") is
  answered for this family by s3embed.py (§3). The run is reached from S3 with no prefix at all, at a factor 2.5 in n.

## DONE / FINDINGS / NEEDS
- DONE: r107.py; s3embed.py; pins s3quad_K3_m4 (check.sh gate) and s3quad_K8_m30; the tables above. Every row was run on both engines;
  Oink was run on the two pins.
- FINDINGS:
  1. DATA: mkr as built: the S3 default start gives 3 iterations (all K). The quadratic run needed the designed start.
  2. DATA: embedded mkr (s3embed): from the S3 DEFAULT start, 4K² + 3K iterations at n = 60K + 13 (≈ n²/900). It is one
     fallback-free run, 2 phases, and the same as the explicit-start run. Pin s3quad_K8_m30: 264 iterations at n 479, two engines,
     Oink OK.
  3. DATA: max per-vertex switches and Ξ-changes in the run = 2K − 1; Σ switches = 8K² − 1; switches(v) ≤ Σ_succ (Ξ-changes + 1)
     holds everywhere (min slack 1).
- NEEDS: none from the owner.
