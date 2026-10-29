# R118: CONJECTURE FRAME-STRETCH is false as stated: R106's mkr K m gives ONE τ-stretch of K(m+3) σ-changes (τ never changes) at n = 12K + 3m + 6. 1660 > n + m = 1213 at K = 20, m = 80 (explicit start; two engines state by state; Oink). DATA
L-RED successor 29 (Opus 5.5; D1/D18; Lead 19:22Z: "a direct kill of FRAME-STRETCH ... is a cheaper first target"). Written 2026-10-29
~19:40Z (date -u). Labels: DATA / READING / OPEN / DEAD. Not a TARGET.md claim. Nothing here is super-polynomial.
Target: L-NEW 34, claude/l-new 67f4a365, docs/new/N5-DW-box62.md §5: "CONJECTURE FRAME-STRETCH (OPEN): in N5, between consecutive
τ-changes, σ changes fewer than n + m times" (0 / 719 on S3 starts; max 0.66 (n + m)). The statement does not restrict the start.

## 1. The instances (DATA)
- Family: experiments/red/seg/mkr.py K m (R106, L-RED successor 25, unchanged), from its designed start. R106 §1: one fallback-free run,
  τ constant, λ constant, I_τ = ∅ at every state, of L = K(m + 3) − 1 transitions at n = 12K + 3m + 6.
- Tool: experiments/red/sf/tstretch.py. It runs n5b SPEC (L-COMP) with a trace and reports the longest stretch of σ-changes between
  consecutive τ-changes, against n + m (m = number of edges).
  | instance | n | edges | n + m | n5b iterations | second engine | τ-changes | longest τ-stretch | stretch / (n + m) | Oink zlk + strategies |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | seg/instances/mk_16_100 | 498 | 727 | 1225 | 1648 | n5.py (L-NEW driver, L-SI si.py): 1648 | 0 | 1648 | 1.345 | OK (n5.py's solution) |
  | seg/instances/mk_20_80 | 486 | 727 | 1213 | 1660 | xeng.py: state sequences IDENTICAL (1661 states) | 0 | 1660 | 1.369 | OK (n5b's solution) |
  | runquad_K8_m30_n192 (R106 pin) | 192 | 287 | 479 | 264 | (R106: identical) | 0 | 264 | 0.551 | (R106) |
  sha1 (12): mk_16_100.pg 49ba9a590b15, .start d0d0879eb883; mk_20_80.pg a8759b063c9f, .start 7be6c67a2605. Fallbacks are 0
  everywhere. check.sh gate: mkr.py 20 80 regenerates mk_20_80 byte for byte; tstretch.py on runquad_K3_m4_n54 (21 / 137).
- The ratio grows without bound. With m = cK, L ≈ cK² while n + m = O(K), so a single τ-stretch is Θ(n²).

## 2. S3 start (DATA, in progress)
- FRAME-STRETCH's data used S3 starts. R107's s3embed.py turns the designed start into the S3 default (one dummy per edge, priorities
  0..3; R107: s3quad_K8_m30 has the same 264 iterations and 0 τ-changes from S3).
- The dummies raise n + m to n + 3·edges, so a larger member is needed: mkr 40 160 embedded has n = 2413 and n + m = 5307, against
  L = 6519 (predicted ratio 1.23). The run is in flight; result in an addendum.

## 3. What dies, what stays (READING)
- DEAD as stated: FRAME-STRETCH (σ-changes per τ-stretch < n + m), from an explicit start. Its stated consequence #σ − 1 < (n + m)·#τ
  fails here (#τ = 0 changes, #σ = 1660 > n + m).
- Not touched:
  - a polynomial stretch bound (σ-changes per τ-stretch ≤ poly(n)). R106's run is quadratic.
  - L-NEW's structural conclusion: "N5 is polynomial whenever min(#σ, #τ) is", if restated with a poly(n) stretch bound.
  - Lemma FRAME-τ (Even cannot trigger its own frame change). On mkr, Even's run is long precisely without any frame change.
- Repair suggestion for L-NEW: FRAME-STRETCH_k, stretch ≤ (n + m)^k. The data now rule out k = 1. A τ-stretch is a run with τ
  fixed, the setting of the frozen run, so FRAME-STRETCH_k is close to a polynomial (FO*). Equivalence is not checked.

## DONE / FINDINGS / NEEDS
- DONE: tstretch.py; mk_16_100 and mk_20_80 pinned with two engines and Oink; check.sh gate; S3-embedded member in flight.
- FINDINGS: (1) DATA: one τ-stretch of 1660 σ-changes > n + m = 1213 (mk_20_80), 1648 > 1225 (mk_16_100); FRAME-STRETCH DEAD as
  stated, explicit start. (2) READING: the stretch is Θ(n²) on this family, so only a polynomial-exponent version can survive.
- NEEDS: none from the owner.
