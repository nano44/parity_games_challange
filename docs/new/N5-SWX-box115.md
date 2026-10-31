# N5-SWX (box 115): N5 on switchallexp_N — the 2^N mechanism breaks at S4a's arena optimum, not at τ or the W-run; one level up (switchbestexp) it is τ that breaks it
L-NEW successor 42, 2026-10-31 (date -u: after 15:18Z). Lead brief 15:18Z (box 115): run N5 on L-SI's switchallexp_N (N = 2..8), find
which S-step stops the 2^N mechanism, measure W-runs and re-routes, and turn the breaking step into a lemma.
Labels: PROVED (lane), DATA, READING, OPEN. No count is bounded here. G-N5-TIME stays OPEN. This is not M3 and not a TARGET.md claim.

## 0. Answer
- DATA (faithful; §3). N5 on switchallexp_N, N = 2..8:
  - 8, 7, 8, 10, 12, 14, 16 iterations (2N for N ≥ 4), 0 fallbacks, N τ-moves;
  - ONE W-run of N − 1 transitions (N ≥ 4);
  - every Even pair entered ≤ 2 times and fuel-re-routed ≤ 1 time in the whole run (≤ 2 at N = 2).
  - Classical switch-all SI on the same engine reproduces L-SI box 58: 10·2^N − 10 iterations, one pair (the lane edge b_N → b_(N−1))
    fuel-re-routed 2^N times.
- The breaking step is S4a's ARENA OPTIMUM. It is not τ, not the fixed τ of a W-run, and not S4b. DATA, ablations of §2:
  - ARSB = S4a's step with Odd fixed to σ̄_k in place of τ (no τ at all) collapses the family like N5: 2N iterations, pair fuel 1.
  - SAT = Even switch-all with Odd's τ and S4b (N5's loop with S4a replaced by switch-all) keeps the full 2^N: 10·2^N − 10 up to
    N = 6, then 1,243 and 2,486 at N = 7, 8, with pair fuel 64 / 125 / 250 at N = 6 / 7 / 8.
  - So on this family «fixed τ and constant λ_W of a W-run» (L-SI box 58 §5's suggestion) is not needed. The one-player optimum over
    the improvement arena suffices.
- The mechanism (DATA + READING, §4):
  - Under SI the counter head s moves bit by bit, and every head move resets the delay lane b_0 … b_(2N−1) to s. The lane then re-climbs
    one vertex per iteration.
  - Under N5 (and ARSB), at state 2 s jumps straight to the TOP bit. The lane is built once and is never reset.
  - The SI moves that the arena optimum never makes are «stale» moves, i.e. moves that do not attain the arena optimum: 37 / 121 / 335
    at N = 2 / 3 / 4. They sit at the bit gadgets e_i (whose arena optimum closes the cycle e_i → h_i), at d, at the lane b_0 / b_1 and at
    f / g. 0 of them are at s.
- PROVED (lane) Lemma STALE-FREE (§1): N5 never makes a stale move. At every S4a step, every switched Even y that is not its own
  cycle node in the new (σ_(k+1), τ_k)-valuation attains the arena optimum: no edge of H_k(y) beats σ_(k+1)(y).
  - In particular, pattern X of switchallexp (a move that misses the arena optimum) cannot occur in N5, inside a W-run or outside.
- One level up (DATA, §5): Friedmann's switch-best family H_n (the port's switchbestexp, built against Schewe's globally optimal rule,
  Friedmann 1106.0778 Thm 8.4 as opened by L-LIT T20 / T37).
  - ARSB grows: 58, 135, 258, 364, 412 iterations at N = 2..6, max pair fuel 4 → 21. My ARSB is not a checked implementation of Schewe's
    rule, so the growth is DATA only.
  - N5 stays near-linear: 32, 41, 47, 55, 62 iterations, 2 W-runs, longest 18 → 44 transitions, max pair fuel 3 / 4 per run and 2 per
    W-run.
  - READING: on switchbestexp it is τ (N5's use of Odd's CURRENT strategy in S4a, in place of the optimal σ̄) that breaks the growth.
    That is the N5-specific structure L-SI box 58 asked for. STALE-FREE alone cannot be the polynomial property, because ARSB is
    stale-free too.

## 1. Lemma STALE-FREE — PROVED (lane)
- Setting.
  - S4a at a transition k → k + 1 of an N5 run: H_k := {σ_k(v)} ∪ Iσ_k(v) for Even v, Odd fixed to τ_k.
  - G′_k := the one-player game on H_k. val′ := the VJ00 valuation of G′_k (Odd has the single choice τ_k), so val′_σ is the
    (σ, τ_k)-valuation.
- Premises:
  - [1E-N3] (RESULTS R57): σ_(k+1) is the pointwise optimum of G′_k.
  - RESULTS R15 (a) Lemma A and (b) Lemma B (VJ00 Lemma 5.7 and its equality case; valid in any game, so in G′_k).
  - [LEX] (RESULTS R93): the order is linear.
- Statement. Let y be Even with Λ′(y) ≠ y, where Λ′ is the cycle-node map of val′_(σ_(k+1)). Then for every z ∈ H_k(y):
  val′_(σ_(k+1))(z) ⊴ val′_(σ_(k+1))(σ_(k+1)(y)). Equivalently, (y, z) is not an improvement of σ_(k+1) in G′_k.
- Proof.
  - If z ∈ H_k(y) had val′(z) ▷ val′(σ_(k+1)(y)), then {(y, z)} would be an improvement of σ_(k+1) in G′_k.
  - By R15 (a), switching it gives a valuation ⊵ val′_(σ_(k+1)) pointwise.
  - By R15 (b), equality everywhere would force Λ′(y) = y. So the switch is strictly better at some vertex, against the pointwise
    optimality of σ_(k+1) [1E-N3].
  - The order is linear [LEX], so «not ▷» means ⊴. □
- Remarks.
  - The own-cycle-node exception is necessary. «A maximum has no improvement» fails there: RESULTS R15's side finding and the R-N5-LP DF
    refutation (df_cex.pg). STALE-FREE excludes exactly that case.
  - The same proof holds with σ̄_k for τ_k (ARSB). This is why ARSB is stale-free too.
- Definition used in the DATA. A switch-all move y → z at k is STALE if, in the arena H_k with Odd fixed to σ̄_k, the arena-optimal strategy
  redirected at y to z gives y a strictly worse value than the arena optimum. (box115/stale.py; for SI the reply is σ̄_k because that is
  the reply SI improves against.)

## 2. Ablations (box115/abl.py; one VJ engine; DATA)
| N | SI iters / pair fuel | ARSB | SAT | N5 |
| --- | --- | --- | --- | --- |
| 2 | 30 / 4 | 8 / 1 | 30 / 4 | 8 / 2 |
| 3 | 70 / 8 | 8 / 1 | 70 / 8 | 7 / 1 |
| 4 | 150 / 16 | 8 / 1 | 150 / 16 | 8 / 1 |
| 5 | 310 / 32 | 10 / 1 | 310 / 32 | 10 / 1 |
| 6 | — | 12 / 1 | 630 / 64 | 12 / 1 |
| 7 | — | 14 / 1 | 1,243 / 125 | 14 / 1 |
| 8 | — | 16 / 1 | 2,486 / 250 | 16 / 1 |
- SI = si.py rule_switch_all from the best-reward start (L-SI box 58's driver; equal iteration and pair counts: 30 / 70 / 150 / 310,
  pairs (17, 15), (19, 17), (21, 19), (23, 21)).
- SAT uses τ only through S4b, plus an S4c-style τ fallback. Its τ moves only N times.

## 3. N5 on switchallexp_N (box115/swx.py; faithful)
| N | n | iters | fallbacks | τ-moves | W-runs / longest | max ENT / FR (run) | max FR in one W-run |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 35 | 8 | 0 | 2 | 1 / 5 | 2 / 2 | 1 |
| 3 | 49 | 7 | 0 | 3 | 1 / 3 | 2 / 1 | 1 |
| 4 | 63 | 8 | 0 | 4 | 1 / 3 | 2 / 1 | 1 |
| 5 | 77 | 10 | 0 | 5 | 1 / 4 | 2 / 1 | 1 |
| 6 | 91 | 12 | 0 | 6 | 1 / 5 | 2 / 1 | 1 |
| 7 | 105 | 14 | 0 | 7 | 1 / 6 | 2 / 1 | 1 |
| 8 | 119 | 16 | 0 | 8 | 1 / 7 | 2 / 1 | 1 |
- Instances: box115/inst/switchallexp_N.pg from `hard-families/pgsolver_port.py switchallexp N`. N = 2..6 are byte-identical to L-SI's
  pins (si/anc58/inst/pins.sha1). N = 7 is ff46e32f…, N = 8 is 18c24624….
- Starts box115/inst/*.start = n5x's default (valid).
- Faithfulness for every N: n5b SPEC = xeng «state sequences identical: True», and Oink 8fbf0a7 --zlk winners equal N5's with verify OK
  («OINK OK»).

## 4. The mechanism (traces; READING)
- switchallexp_2, SI:
  - s = vertex 1 moves p → k0 at 5, k1 at 15, k0 at 23, …;
  - every head move is followed by t → s and the whole lane b_0 … b_3 → s (iterations 6, 16, 24);
  - then b_2 → b_1 and b_3 → b_2 re-climb one step per iteration (8-11, 18-21, …).
  - So the lane pair is re-entered once per counter increment: 2^N.
- switchallexp_2 / _4, N5:
  - s moves p → k1 (resp. k3, the top bit) at state 1 → 2;
  - the lane climbs once (b_(i+1) → b_i, one per iteration) and is never reset;
  - s moves to its final bit at the end.
- Stale moves of SI (stale.py, N = 2): e_i 20, d 3, b_0 3, b_1 3, f_0 3, g_0 3, l_0 1, r_0 1. The arena optimum at e_i is h_i, which closes
  the bit cycle.
  - In 19 / 37 (N = 2), 72 / 121 (N = 3) and 218 / 335 (N = 4) of the stale moves the optimal edge closes a cycle through y (si.py
    cycle_creating).
  - So «stale = cycle-closing» is only partly true. That characterisation is OPEN, and not needed for STALE-FREE.

## 5. One level up: switchbestexp_N (DATA; N5 faithful as in §3)
| N | n | SI iters | ARSB iters / pair fuel | N5 iters | N5 W-runs / longest | N5 max FR run / W-run |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 60 | 61 | 58 / 4 | 32 | 2 / 18 | 3 / 2 |
| 3 | 85 | 141 | 135 / 8 | 41 | 2 / 26 | 3 / 2 |
| 4 | 110 | 301 | 258 / 14 | 47 | 2 / 31 | 3 / 2 |
| 5 | 135 | 621 | 364 / 19 | 55 | 2 / 38 | 3 / 2 |
| 6 | 160 | — | 412 / 21 | 62 | 2 / 44 | 4 / 2 |
- switchbestexp_2 is byte-identical to new/box54/out/switchbestexp_2.pg (b3d5bc29…, pinned in check.sh «box 55»).
- READING: ARSB grows superlinearly at N ≤ 5 but not as a clean doubling (412 at N = 6). Whether a faithful Schewe rule doubles here
  is for L-LIT / L-COMP (Friedmann's Thm 8.4 counts are not re-checked here). N5's W-runs grow linearly (≈ 6N + 8).

## 6. What this means for the proof side (READING)
- Two separations, each on a published family:
  - switch-all → arena optimum: STALE-FREE, PROVED (lane);
  - arena optimum against σ̄ → arena optimum against τ: OPEN as a lemma, DATA on switchbestexp.
- A proof of G-N5-TIME must use the second: the arena optimum is taken against τ, and τ moves only by S4b.
  - L-SI's ANCESTRY / FUEL lemmas and my P-N5-ROOT lemmas use [R15a], [1E-N3], [PLAY] and [IMP].
  - [1E-N3] holds for ARSB as well, with σ̄ for τ.
  - So none of them separates N5 from ARSB.
  - The W-run notions (W, H_k against τ, ORIGIN-NEW's use of W-MON) do use τ, and that is where the next lemma has to live.
- Next (for the Lead):
  - (a) L-RED: rebuild Friedmann's switch-best mechanism INSIDE one N5 W-run, i.e. with τ fixed (the attack);
  - (b) proof side: what does fixing τ to the current S4b optimum, rather than σ̄, forbid in switchbestexp's carry? Trace the carry of
    ARSB at N = 3 against N5 (the first divergence) — not done in this box.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box115/ (swx.py, abl.py, stale.py, inst/ switchallexp_2..8 and switchbestexp_2..6 with default starts);
  check.sh pin «box 115 SWX».
- FINDINGS:
  - DATA: N5 on switchallexp_N runs 2N iterations, one W-run of N − 1 transitions, pair fuel ≤ 1, faithful.
  - The 2^N breaks at S4a's arena optimum (ARSB collapses it; SAT with τ keeps 2^N).
  - PROVED (lane) STALE-FREE.
  - On switchbestexp, ARSB grows while N5 stays linear, so τ is the separating ingredient there (READING / DATA).
- NEEDS: Lead: route (a) and (b) of §6.
