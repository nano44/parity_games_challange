# R-N5-ACCEL: REFEREE report on packet P-N5-ACCEL (L-NEW box 44: in a phase, switches are paid by simple-path value levels (ACCEL); inside an epoch of Odd's best response N5 freezes like one-player SI (EPOCH); every game)
Referee: REFEREE (successor 12, session_01KNDBjZvPFLaNjEdCmEWBcN), Opus 5.5 (owner ruling D15).
- Routing: the Lead's message of 04:30Z (Lead's stamp), item (3).
- Object: docs/new/P-N5-ACCEL-box44.md at trunk e7febdc2, sha1 301f0be0fa2b2240bba59b347dfbee8426b8dba3 (checked with
  `git show e7febdc2:docs/new/P-N5-ACCEL-box44.md | sha1sum`; identical on my tree), 104 lines. Author: L-NEW successor 23.
- Written 2026-10-26T04:42Z-04:46Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: docs/referee-2/R2-N5-ACCEL* is on my tree but NOT opened before this report was pushed. No lane code run
  (experiments/new/box44/sgcheck.py, epoch.py). D1.
- Compared against: RESULTS R19 (d) (SG), R15 (a), (d), R17 (a) (V1), R38 (a), (f); P-N5-FBRED §1.1, §2 CN-ONLY_D (signed by both, R56);
  P-N5-VILB §1 (my R-N5-VILB); SPEC S1, S2, S4a, S4c.
- Tool: scratch/accel_probe.py (own engine; any game). Logs scratch/accel_logs/ (run_all.sh).

## Verdicts
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′); κ-FB-ROUND; CN-ONLY_D (restated with proofs) | SIGNED (= R56's signed forms) |
| §2 | Lemma ACCEL (a) κ_t(z) ∈ K_c(z); (b) switching transitions ≤ N_K; (c) f ≤ 1 + N_K | SIGNED |
| §3 | Lemma EPOCH (a) freeze per epoch; (b) no non-cycle-node switch after e_{n−1}, frozen part ≤ 4n(n − 1) + 1 transitions; (c) f ≤ 1 + n·N_ep | SIGNED |
| §4 | limits, the σ̄|Q-repeat instance, data | not signed (as briefed); repeat instance re-run on my engine (§4 below) |
No gap. Notes ACCEL-N1 (R19 (d) (SG) checked "on all games"; inside a phase it follows from §1's facts alone), ACCEL-N2 (EPOCH (b)
identifies Ξ with R15's Ω_σ), ACCEL-N3 (data: EPOCH's frozen regime is vacuous in all data, mine included). Neither lemma is a
polynomial bound (|K_c(z)| and N_ep can be exponential, §4). Not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. §1
- (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′) and κ-FB-ROUND are the per-class forms signed by both referees in P-N5-FBRED §1.1 (RESULTS R56 (a))
  and in P-N5-VILB §1 (my R-N5-VILB §1); I re-derived them against FBP for the FBRED §C. (SP′) is stated here as "prefix up to c (or up to
  its first vertex of any set containing c) is simple": a lasso whose cycle contains c ✓.
- CN-ONLY_D is P-N5-FBRED §2's text with (2)'s two cases and (3) (R56; my R-N5-FBRED §C, C.1, where I re-derived case (2) with q). ✓
- VERDICT: §1 SIGNED.

## 2. Lemma ACCEL
- (a): z = c: K_c(c) ∋ (0, 0) = κ_t(c) ((A0κ)). z ≠ c: the honest prefix from z to c is a simple path ((SP′)), all its vertices in U_c ((Aκ)),
  its edges G-edges, so it is a simple path of G[U_c]; summing (Aκ) along it gives κ_t(z) = κwt_c(prefix ∖ {c}) ∈ K_c(z) ✓.
- (b): (SG) is RESULTS R19 (d)'s key step, landed verbatim as "at any N5 transition a switched Even vertex y with λ_L(y) ≠ y gains strictly
  (on all games, not only 𝒞^1O)" (docs/RESULTS.md, R19 (d)) ✓. ACCEL-N1: inside a phase I re-derived it from §1 alone. A switched Even y
  moves to a gate target z (S4a: its arena keeps only σ(y) and gate targets, A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ}; S4c: the best gate target), so
  Ξ_L(z) ▷ Ξ_L(σ_L y). λ is constant on the phase and λ(y) = c ≠ y, so (Aκ) at L and L+1 puts σ_L(y), z in U_c and gives κ_{L+1}(y) =
  κwt_c(y) + κ_{L+1}(z) ≥ κwt_c(y) + κ_L(z) > κwt_c(y) + κ_L(σ_L y) = κ_L(y) ((M2κ), (M1κ)) ✓. With (M2κ) and (a), κ(y) rises strictly at each of
  y's switches within the finite set K_c(y), so y switches at ≤ |K_c(y)| − 1 transitions; charging each switching transition to one
  switched y gives ≤ N_K ✓.
- (c): ≤ 1 fallback with S = ∅ (CN-ONLY_D); a fallback with S ≠ ∅ switches an Even y ∉ T, so y ∉ C, λ(y) ≠ y, and it is one of (b)'s
  transitions ✓.
- VERDICT: ACCEL (a)-(c) SIGNED.

## 3. Lemma EPOCH
- Epoch: maximal run of states of the phase with σ̄|Q constant; non-Q Odd vertices are forced, so σ̄ is constant on E ✓. e_j: in-phase
  fallbacks with source in E (the source-state convention, FBRED-N1) ✓.
- (a) lower bound, induction on j: base p = (c) ✓. Odd z on p: p is a path of G_E, so x = σ̄_E(z) = next_t(z) for t ∈ E; (Aκ) and the
  hypothesis at t ✓. Even z: k := e_j < t, k ∈ E, k > e_{j−1}; k + 1 ≤ t and E is a run of consecutive states, so k + 1 ∈ E; κ-FB-ROUND at k
  (x ∈ U_c), the hypothesis at k, (M2κ) from k + 1 to t ✓. Upper bound: z's honest prefix at t ∈ E is a simple path of G_E[U_c] (Even edges
  σ_t, which G_E keeps; Odd edges σ̄_t = σ̄_E) ✓, so κ_t(z) ≤ opt_E(z). Simple paths in U_c have ≤ |U_c| − 1 ≤ n − 1 edges, so after e_{n−1}
  the two bounds meet: κ_t = opt_E on every class; λ is constant and κ determines P ((INJ)) and ℓ, so Ξ is constant there ✓.
- (b) a switch of an Even z with λ(z) ≠ z at t → t + 1 (both in E, t > e_{n−1}) would give κ_{t+1}(z) > κ_t(z) = opt_E(z) ≥ κ_{t+1}(z) ((SG),
  (a) at t and t + 1) ✓. ACCEL-N2: "Ξ = Ω_σ" identifies SPEC's Ξσ with VJ00's Ω_σ in R15 (d); that holds on every game (VJ00 (11); my
  R-N5-1E §1, both referees on P-N5-1E). Ω_τ is constant because τ is constant on a phase ✓. R15 (d) (landed): "at most 4n(n−1) consecutive
  N5 iterations leave both Ωσ and Ωτ unchanged" ✓; plus the transition leaving E ✓.
- (c) per epoch: ≤ n − 1 fallbacks e_1..e_{n−1}; a later fallback with both ends in E switches only cycle nodes ((b)), so S = ∅, and there
  is ≤ 1 such in the whole phase (CN-ONLY_D); ≤ 1 fallback is E's last transition. So f ≤ n·N_ep + 1 ✓. Every in-phase fallback has its
  source in exactly one epoch ✓.
- VERDICT: EPOCH (a)-(c) SIGNED.

## 4. Data (DATA, not proof; scratch/accel_probe.py, own engine; logs scratch/accel_logs/)
Checks: SG at every in-phase transition; EPC (EPOCH (c)) per phase; EPB (EPOCH (b)) where its hypothesis holds; and for n ≤ 12 (simple paths
enumerated): ACA (κ_t ∈ K_c), ACB / ACC (N_K), EPA (both bounds of EPOCH (a) at every state of every epoch). Counters: EPA_tight (lower
bound attained), CTRL (the j + 1 lower bound fails), CN_switch (switched Even cycle nodes).
| set | runs | phases | max f | SG checks | max switching transitions / phase | max epochs / phase | ACA / EPA checks (n ≤ 12) | EPB hypothesis met | failures |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41, n ≤ 64 (367 games; 67 with n ≤ 12), S3 + 2 random | 1,101 | 5,393 | 33 | 22,577 | 112 | 50 | 6,004 / 6,004 (tight 1,150) | 0 | 0 |
| box-43/44 instances + lap_n6_s1_110421, S3 + 4 random | 55 | 292 | 17 | 489 | 44 | 17 | 748 / 748 (tight 191) | 0 | 0 |
| 2,000 random games, 0-4 Odd choice vertices, n 4-12, seed 41, S3 + 2 random | 6,000 | 14,265 | 1 | 1,127 | 3 | 3 | 129,458 / 129,458 (tight 28,685) | 0 | 0 |
- My engine reproduces the packet's maxima, 112 switching transitions and 50 epochs in one phase (lib41).
- The σ̄|Q-repeat instance (§4, not signed), experiments/new/box25/laps/lap_n6_s1_110421.pg, sha1 4f4fe69c51e1c6f170c9c732feca025da70e7edb
  (checked): from S3, one phase (λ ≡ 5, τ(2) = 0), σ̄_t(2) = 0, 4, 0 at states 0, 1, 2 — exactly as stated; 3 epochs in that phase.
- CN_switch: 410 switches of Even cycle nodes, none raises κ (κ(c) = (0, 0) is constant, (A0κ)); so (SG)'s hypothesis λ(y) ≠ y cannot be
  dropped, and ACCEL (b) rightly does not count those transitions.
- ACCEL-N3 (vacuity, honest): no epoch in any of my samples reaches n − 1 fallbacks (EPB hypothesis met 0 times), so EPOCH (a)'s freeze
  conclusion and EPOCH (b) are never exercised; they rest on their proofs (the packet says the same). EPOCH (a)'s two inequalities and
  EPOCH (c), ACCEL (a)-(c) and SG are exercised.
- Reproduce (from docs/referee/scratch): `sh accel_logs/run_all.sh` (fixed seed; file starts seeded by the RELATIVE path).

## 5. Notes for the fixes file
- ACCEL-N1: (SG) is landed "on all games" (R19 (d)); inside a phase it also follows from (Aκ), (M1κ), (M2κ) and "switches go along gates"
  (S4a's arena, S4c): an optional one-line proof would make the packet self-contained.
- ACCEL-N2: EPOCH (b) uses Ξ = R15's Ω_σ (VJ00 (11), every game); one clause.
- ACCEL-N3: DATA (frozen regime vacuous).
