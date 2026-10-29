# R124: the bounded third-factor try (Lead 22:57Z). A bidirectional reactor chain doubles mkr's λ-run (2K(m − 1), 1128 at n = 294, ≈ n²/77), but a λ-run > n² + n needs a third multiplicative factor, and the obstruction is the WAITING device, not re-arming: R120's Even observer already is a sub-clock that re-arms every pivot level at no extra cost. DATA + READING; OPEN
L-RED successor 31 (Opus 5.5; D1/D18; Lead 2026-10-29 22:57Z: "one bounded try at a third multiplicative factor, a λ-run longer than
n². A single λ-run > n²+n kills RUN-QUAD and PCH-QUAD-S at once. Stop at the first clear obstruction, and write it down"). Written
2026-10-29 from 23:22Z (date -u). Labels: DATA / READING / OPEN. Not a TARGET.md claim; G-N5-TIME OPEN; nothing here is super-quadratic.

## 1. DATA: the bidirectional chain (experiments/red/span/mkrb.py K m)
- mkr.py with two edits: b_j -> r_(j+1) (b_m -> h′) instead of b_j -> h′, and the h-side W-sinks escape through r_1 (G_i -> r_1).
- An h-rise runs down the chain as in mkr. An h′-rise now runs back UP, one reactor per step: r_j's b-option goes through r_(j+1), and
  while r_(j+1) is still on a it leads back through r_j, an Odd-won cycle (top a-marker), so r_j waits.
  | K | m | n | iterations (n5b SPEC) | mkr.py same K, m | longest Ξ λ-run | λ-run / n² |
  | --- | --- | --- | --- | --- | --- | --- |
  | 3 | 4 | 54 | 30 | 21 | 26 | 0.0089 |
  | 4 | 16 | 102 | 136 | 76 | not recorded | |
  | 8 | 32 | 198 | 528 | 280 | 496 (mkr: 279) | 0.0127 |
  | 12 | 48 | 294 | 1176 | not run | 1128 | 0.0131 |
- Fits (4 rows): iterations 2K(m + 1); longest λ-run 2K(m − 1) (the last up-wave runs after the run-end λ changes). 0 fallbacks. The
  Odd side (λ^U) has no change at all.
- Pin experiments/red/span/instances/bidir_K8_m32 (sha1 6e8467e7b3251f78c1583292a576714de119e6d2 / start a153a31b9a353ee3ee3d5b4785e9a19cff020fe6): n5b =
  n5.py state by state (xeng.py); Oink zlk OK, strategies verified (n5b solution). K = 12: Oink OK on the n5b solution.
- So the longest known single λ-run is ≈ n²/77 (R106 mkr: ≈ n²/144). A constant factor, no change of exponent.

## 2. READING: why constants cannot reach n² + n
- Clock × chain: K pivot levels at a vertices each, a chain of m reactors at b each, w waves per level (w = 1 mkr, 2 here). L ≈ w·K·m
  with aK + bm ≤ n, so L ≤ w·n²/(4ab). Here a ≈ 12, b = 3, w = 2: n²/72. Even a = b = 1 would need w ≥ 4 waves per level.
- Each wave carries one FRESH value (a new pivot level): a reactor flips only to a strictly better Ξ, so the same value cannot cross the
  same chain twice. More waves per level need more fresh values per level, i.e. more levels: w·K is the number of levels, and its cost is
  linear. A third factor needs levels that cost sub-linearly (a composite clock) AND a process that waits on each of them.

## 3. READING: re-arming is not the obstruction; waiting is
- Composite levels need a sub-clock that returns to its bottom after every outer tick. A gated sub-pivot g with options κ_k ⊕ (common
  source) cannot: its option ranking is fixed and Ξ_t(σ_t g) is monotone, so after the first outer level it sits at its top.
- But R120 §3's Even observer o_E (max over y_j -> r_j, q_j above the a-markers) IS a re-arming sub-clock. It climbs y_1 -> y_2 -> ...
  -> y_m during every wave and is back at its start after the flip (257 switches > n at n 231). Its options route to different sources
  (r_j) whose rank order rotates with the wave, and it costs nothing beyond the chain. The Odd observer has K·m monotone levels at cost
  K + m (R120). So sub-linear composite levels exist.
- What is missing is a process that WAITS on each composite level. An observer's levels arrive one per transition. A third factor needs
  each of them to trigger a full sub-wave (length p) before the next one arrives. That means gating the main chain's hops, and those
  gates are reused at every pivot level. That is exactly R108 §4's obstruction (a reused gate's closed option must W-follow h′, so its Ξ
  sits in h′'s band, the gated link's honest value drops into that band, and the chain's later comparisons or the readers' plays break).
  I found no way around it in this box. Per-(level, hop) gates avoid reuse but cost K·m vertices, which is the two-factor bound again.
- Routes not tried here (R108 §6): (A) τ-ticks, so that a reused gate may re-close at a phase boundary (W can fall only at a τ change,
  R108 §1); (B) length thresholds (equal path sets decided by play length); (C) a clock whose two "worlds" are the two parities of
  one digit.

## 4. Where this leaves the span targets (Lead record 22:57Z)
- RUN-QUAD (every λ-run ≤ n² + n) and PCH-QUAD-S hold on everything known; the best λ-run is ≈ n²/77.
- A kill of either needs a nested (three-factor) design. Re-arming sub-clocks are available (observers); the open problem is a reused
  waiting gate inside one phase, or route (A) across phases inside one λ-run.

## DONE / FINDINGS / NEEDS
- DONE: span/mkrb.py, pin bidir_K8_m32 (two engines, Oink), check.sh gate (K 3, m 4: 30 iterations), this note.
- FINDINGS:
  1. DATA: bidirectional chain, iterations 2K(m + 1), longest λ-run 2K(m − 1) (1128 at n 294, ≈ n²/77), fallback-free.
  2. READING: two-factor (clock × chain) designs give ≤ w·n²/(4ab); waves per level are bounded by fresh levels; a λ-run > n² + n
     needs a third factor.
  3. READING: re-arming composite sub-clocks exist (the Even observer); the obstruction is the reused waiting gate (R108 §4).
  4. OPEN: routes (A), (B), (C) of R108 §6.
- NEEDS: none from the owner.
