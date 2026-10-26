# R79: Lemma REC-0 survives an exact step-by-step checker (no kill); epoch extremes N_ep 90 (n 40), len(E) 30 at |D_E| ≥ 2 (n 48), N_0 6 (n 24) (L-RED successor 20, box 46; Lead GO 08:17Z, date -u)
Target: Lemma REC-0, docs/new/P-N5-REC0-box45.md (FROZEN packet, l-new 18dd8c90, sha1 343239b5; source N5-NEP-box45.md §5 at l-new 40659d50,
sha1 ae2d49e6). Lead's order (a): attack REC-0 with an exact counter, and climb for long and many epochs (N_ep per phase; len(E) at
|D_E| ≥ 2). Labels per L40: DATA / READING. Every game. Nothing here bounds N5; G-N5-TIME stays open. Not a TARGET.md claim.

## 0. Result
- **No kill of REC-0.** 0 violations of the inequality, and 0 violations of any step of its proof checked separately, in about
  8.2 M runs plus 1,951,432 climb evaluations (table in §1). Every pinned instance is re-run with Oink: zlk regions equal, and Oink
  `-v --sol` accepts the written solution.
- **The Q-R17 point (the Lemma P step applied at a state of an N5 run): no counterexample.** STEP1 (level j at a D = ∅ state, then an
  S4a step to an all-unsplit state, gives level ≥ j + 1) was checked exactly 861,254 times; 316,066 of these were in exhaustive
  start-pair runs at n 4-6. STEP2 (persistence) and PREFIX were also checked at every eligible transition. 0 FAIL.
- **The bound is far from tight on data.** Max N_0 is 6 (n 24, f 0; the library's max was 5) against a bound of 2,234 there. Max kind-(iii)
  steps in one run is 5 (n − 1 = 23 allowed). Max t* − t is 3 (4n(n − 1) allowed).
- **A shortcut that FAILS (READING, recorded so nobody repeats it).** "No in-phase fallback has a D = ∅ source, so kind (i) is empty" is
  false. In random runs 34,748 of 37,053 in-phase Even fallbacks have a D = ∅ source; in the library, 54 of 1,073.
  - Mechanism: a gate that improves by length only, at the cycle node of its own cycle (a cycle-creating switch). S4a's optimum vs τ ties
    with σ there, so S4a changes nothing and S4c falls back.
  - Smallest pin: fbd0_n4. State 1 has D = ∅, gate (1, 2), Ξ(1) = (1, ∅, 0) and Ξ(2) = (1, ∅, 2). Vertex 1 has odd priority 3, so the
    longer path is better for Even.
  - So REC-0's f-term for kind (i) is needed as written.
- **Epoch extremes (Lead's (a); climbs, not distributions):**
  - N_ep 90 in one phase at n 40 (nep90_n40; the previous record was 80, nep80_n40);
  - N_ep 24 at n 20 with ONE Odd choice vertex (nep24_n20; N_ep > n in 𝒞^1O);
  - len(E) 30 for an epoch with |D_E| ≥ 2 at n 48 (lend2_30_n48; L-NEW's library max was ≤ 28);
  - N_0 6 at n 24 (n0_6_n24).
  None of these contradicts a fleet statement: there is no landed bound on N_ep, and none on len(E) at |D_E| ≥ 2.

## 1. Checker and data (experiments/red/rec0/; written from the packet's §0-§1 text, not from L-NEW's rec0.py)
- rec0_20.py (exact, per phase). The trace is o1_19.trace (own SPEC S1-S5 loop; matches n5.py, R75-R78).
  - W_k is computed from the (σ_k, τ_k) play and compared against si.Engine on G_τ at three states of every run (WVAL).
  - LEVEL(k) is the exact maximal j: M_j(x) is computed by enumerating simple paths of G_τ that end at a cycle node of λ (budgeted; on
    overflow the level checks of that phase are skipped and counted).
  - Checks: REC0 (the inequality); XIW (D = ∅ ⇒ Ξ = W, all-unsplit); BASE; STEP1; STEP2; WM; PREFIX; WLEB (W ⊴ B at all-unsplit
    states); SAT_B (Ξ = B on D = ∅ states ≥ t); SAT_span (t* − t ≤ 4n(n − 1)); KIND3 (≤ n − 1 per run before t); PRE (≤ (f + 1)(n + 1)
    epochs before t); EP0 (len(E) ≤ n + m at D_E = ∅, RESULTS R64); OUT (verify.py; Oink with --oink).
  - Reported: N_0, N_0/(f + 1), kind-(iii) per run, t* − t, epochs before and after t, N_ep, len(E) by |D_E|, and kind-(i) sources
    (fbD0).
- Drivers: rrec0_20.py (library / random), exrec0_20.py (random small games × EVERY start pair), climb20.py (objective = expression;
  improvements re-run with Oink), pin20.py.

| sample | runs | phases | level checks / STEP1 | FAIL | max N_0 | max kind-(iii)/run | max t* − t | max N_ep |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41 (412 files, n ≤ 64) × (S3 + 2 random), seeds 7, 8 | 2,202 | 10,845 | 13,782 / 3,844 (3,205 phases overflow) | 0 | 5 (w24b_thc24_final) | 4 | 3 | 50 (lev_l_x) |
| random n 4-9, \|Q\| ≥ 1, S3 + 3, seed 1, 60 s | 145,440 | 291,448 | 255,884 / 17,033 | 0 | 2 | 1 | 2 | 3 |
| random n 6-14, \|Q\| ≥ 2, S3 + 3, seed 2, 1,800 s | 2,383,140 | 5,722,358 | 4,634,406 / 353,456 | 0 | 2 | 1 | 2 | 4 |
| random n 6-16, \|Q\| ≥ 2, S3 + 3, seed 9, 900 s (fbD0 counted) | 1,023,068 | 2,526,897 | 2,059,048 / 170,855 | 0 | 2 | 1 | 2 | 4 |
| exhaustive: 116,340 random games n 4-6 × every start pair (≤ 3,000), seed 11 | 4,616,149 | — | 7,814,320 / 316,066 | 0 | 2 | 1 | 2 | 3 |
| climbs (§2), 8 runs | 1,951,432 evaluations | — | (levels off in climbs) | 0 | 6 | 5 | — | 90 |

## 2. Climbs (climb20.py; n fixed; mutations of priorities, successor sets, owners, start entries; pins from Oink re-runs only)
| objective | seed | evaluations | best (n) | pin |
| --- | --- | --- | --- | --- |
| N_ep | nep80_n40 + start (R76) | 60,542 | 87 (40) | nep87_n40 |
| N_ep | nep87_n40 | 45,691 | 90 (40) | nep90_n40 |
| N_ep | lev_l_n20 (L-SI), S3 | 236,142 | 24 (20), \|Q\| = 1 | nep24_n20 |
| N_ep | lev_l_n28 (L-SI), S3 | 146,703 | 25 (28) | — |
| 1000·len(E at \|D_E\| ≥ 2) + #such epochs | rho666_n48 + start (R76) | 71,056 | 30 (48), \|D_E\| ≤ 9 | lend2_30_n48 |
| 100·N_0 + kind-(iii) | w24b_thc24_final, S3 | 578,201 | N_0 6 (24), f 0 | n0_6_n24 |
| same | n0_6_n24 | 467,199 | 6 (no growth) | — |
| 1000·N_0 + f | fr39_q4_n48 + start (R76) | 345,898 | N_0 3 at f 1 (48) | — |

- Mechanism of n0_6_n24 (f = 0, one fallback-free run; Q = {5, 11, 21}). The configuration alternates ∅, {21}, ∅, {11}, ∅, {21}, ∅, {21},
  ∅, {11}, ∅. Each D = ∅ epoch is one state, and each of its exits is a kind-(iii) step (W-level + 1). This is exactly the pattern
  REC-0's step 5 charges to the W-level. Reaching n − 1 such steps in one run would show the linear term is needed. The climbs stop
  at 5.
- With f > 0 no climb got past N_0 = 3. The f-dependence of REC-0 is real in the proof (kind (i) is common, §0); on data it is not
  visible. Whether N_0 has an f-free bound stays OPEN (packet §2). The data neither refutes nor supports it beyond these maxima.

## 3. Pins (experiments/red/rec0/instances/; each .pg with .start.json; rec0_20 --oink: no FAIL, OUT_OINK OK)
| file | sha1 (.pg) | sha1 (.start.json) | what |
| --- | --- | --- | --- |
| nep90_n40.pg | 7348271ac0cbb0ef88a7d15eadc91e29d0fe68fa | 950dcce375febc8d02742435d2f3ef030f542dee | N_ep 90, n 40, \|Q\| 5, ITER 95, f 7 |
| nep87_n40.pg | 7ad51e7fbb20a2c7d1cd17d87d3190d73595bb32 | 00d3990c44037e28af76f80fc35f3a79d0c8ae6d | N_ep 87, n 40, \|Q\| 5, ITER 96, f 7 |
| nep24_n20.pg | dd7162124b53166028d0baf1d739a342f8ebd9b4 | 793d15f841b65ff143aa7e32217f283995bf4f1b | N_ep 24, n 20, \|Q\| 1 (𝒞^1O), 1 phase, f 0 |
| lend2_30_n48.pg | 1d68353cf15b02bcd7acabd7ff5fabb79d43a505 | 98634f05cd54a65fefe15244baca1a294038a6fb | len(E) 30 at \|D_E\| ≥ 2, n 48, \|Q\| 14 |
| n0_6_n24.pg | 603bae696a65984621475981623c0edb1709143f | d62fe58501c25609353ac389082f2ea7311621ea | N_0 6, f 0, kind-(iii) 5 in one run |
| fbd0_n4.pg | 8218bb0a90265c4fc943ab5803987ebfa963bb09 | 8d6c4613854207431f93ece9757b3719869558a2 | in-phase fallback from a D = ∅ state |
Reproduce: `python3 experiments/red/rec0/rec0_20.py file <x>.pg <x>.start.json --oink`.

## 4. READING (not to sign)
- REC-0's proof holds up step by step on this engine. The one point the packet flags (Q-R17) is exercised 861 k times without a
  failure, including at transitions whose next state has D ≠ ∅ (kind (iii), the step REC-0 needs).
- The two places where an attack could still bite are the premises, not the new argument: SN-PREFIX_D (a) and R15 (d). Both were
  checked here (PREFIX; SAT_span via t* − t), with 0 FAIL, but only on short phases (max t* − t = 3).
- Long and many epochs: N_ep reaches about 2.25n (90 at n 40) and exceeds n at |Q| = 1. len(E) at |D_E| ≥ 2 reaches 30 at n 48 (m about 100),
  below n + m. No superlinear growth was found by these climbs. They hold n fixed, so they do not measure a growth rate.
