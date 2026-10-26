# R2-N5-ACCEL: second-referee check of packet P-N5-ACCEL (L-NEW box 44: Lemma ACCEL (a)-(c), Lemma EPOCH (a)-(c), every game). REFEREE-2 (successor 13), written 2026-10-26 03:5xZ-04:0xZ (date -u)
Signature: (Opus 5.5, D15). Lead's order 03:54Z (its stamp), item (2).
Object: docs/new/P-N5-ACCEL-box44.md, `git show e7febdc2:docs/new/P-N5-ACCEL-box44.md | sha1sum` -> 301f0be0fa2b2240bba59b347dfbee8426b8dba3
(= the Lead's pin; = my tree), 104 lines (L-NEW successor 23, frozen at l-new e9eaaaaf). No fixes file.
Background read: RESULTS R15 (a), (d), R19 (d) (the (SG) key step, l. 850-856), R38 (a), (f); SPEC S1, S2, S4a, S4c, FIX 3; my R2-N5-FBRED
(§1 facts, CN-ONLY_D), R2-N5-VILB.
Independence: no docs/referee/ ACCEL file (`ls docs/referee | grep -i accel` -> empty at 03:54Z); none opened. No lane script run.
Tools (own code): docs/referee-2/R2-N5-VILB/va_check.py (shared; R2-N5-ACCEL/README.md points there), logs/, climb/.
Labels: PROVED (L-NEW 23). Every game. Neither lemma gives a polynomial bound; G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | notes |
| --- | --- | --- |
| §1 facts, κ-FB-ROUND, CN-ONLY_D (restated) | SIGN | = P-N5-FBRED §1.1 / §2 (signed in R2-N5-FBRED) |
| §2 Lemma ACCEL (a), (b), (c) | SIGN | N-ACC-1 ((SG)'s scope verified) |
| §3 Lemma EPOCH (a), (b), (c) | SIGN | N-ACC-2 (EPOCH (a)'s per-class consequence, reached in data); N-ACC-3 (global regime not reached; climbs) |
| §4 | not signed (as briefed) | the σ̄|Q-repeat DATA confirmed independently |
No gap. No (P). TARGET.md diff: not a claim of TARGET.md §2.

## 1. Premises
- N-ACC-1 ((SG), the Lead's item): RESULTS R19 (d), proof of Lemma RE, verbatim: "key step (SG) — at any N5 transition a switched Even vertex y
  with λ_L(y) ≠ y gains strictly (on all games, not only 𝒞^1O) (Ξ_{L+1}(z) ⊵ Ξ_L(z) ▷ Ξ_L(σ_L y), then one strict (V2))". The scope "on all
  games" is in the signed text, and the proof uses only R15 (a), the gate (S4a / S4c switch along gates), (V1) at L + 1 (λ_{L+1}(y) =
  λ_L(y) ≠ y inside a phase) and strict (V2): no one-Odd step ✓. Data: 51,331 switches checked, all strict.
- R15 (d) "at most 4n(n − 1) consecutive N5 iterations leave both Ωσ and Ωτ unchanged" ✓ (every game). R38 (f) CN-LAST every game ✓.

## 2. Lemma ACCEL: SIGN
- (a) ✓: the honest prefix of z to c is a simple path of G[U_c] ((SP′); its edges are G-edges inside U_c), and (Aκ) along it gives
  κ_t(z) = κwt_c(prefix ∖ {c}) ∈ K_c(z); z = c gives (0, 0) ∈ K_c(c).
- (b) ✓: a switched Even y with λ(y) ≠ y at an in-phase transition gains strictly ((SG); (M1κ) turns it into κ_{t+1}(y) > κ_t(y)); κ(y) never
  decreases in the phase ((M2κ)) and takes values in the finite set K_c(y); so y switches at ≤ |K_c(y)| − 1 transitions; each counted
  transition is charged to one such y.
- (c) ✓: ≤ 1 fallback with S = ∅ (CN-ONLY_D); a fallback with S ≠ ∅ switches an Even y ∉ T, so y ∉ C, λ(y) ≠ y, counted in (b).

## 3. Lemma EPOCH: SIGN
- An epoch (σ̄|Q constant) has σ̄ constant (Odd vertices outside Q have one successor) ✓; G_E fixes every Odd vertex to σ̄_E ✓.
- (a) lower bound ✓: induction on j; Odd z: next_t(z) = σ̄_E(z) = x on E (the path is in G_E); Even z: k := e_j ∈ E, k > e_{j−1}, k + 1 ≤ t and
  k + 1 ∈ E because E is a run of consecutive states with k, t ∈ E; κ-FB-ROUND at k, the hypothesis at k, (M2κ). Upper bound ✓: the honest
  play at t ∈ E is a simple path of G_E[U_c] ((SP′)). Freeze ✓: simple paths in U_c have ≤ |U_c| − 1 ≤ n − 1 edges, so after e_{n−1} the
  bounds meet; κ determines Ξ inside a class (cycle node fixed; (INJ) for P; s_c·ℓ for ℓ), so Ξ is constant on that part of E.
  - N-ACC-2: the same argument gives the per-class freeze κ_t = opt_E on U_c once j ≥ |U_c| − 1 (it is (a)'s lower bound at j = |U_c| − 1
    plus the upper bound). That consequence IS reached in data (18,251 checks outside the climbs, 38,213 in them), unlike the global one.
- (b) ✓: a switch of an Even z with λ(z) ≠ z at t → t+1 inside E after e_{n−1} gives κ_{t+1}(z) > κ_t(z) = opt_E(z) ≥ κ_{t+1}(z) ((SG), (a) at t
  and t + 1): impossible. After e_{n−1}, Ξ (= Ω_σ) is constant on E and Ω_τ is constant (τ constant on the phase), so R15 (d) bounds the
  consecutive transitions inside E by 4n(n − 1); plus the one leaving E ✓.
- (c) ✓: per epoch, ≤ n − 1 fallbacks e_1 … e_{n−1}, then fallbacks inside E switch only cycle nodes ((b)), so have S = ∅ (switched vertices
  in C ⊆ T): ≤ 1 per phase (CN-ONLY_D); ≤ 1 fallback is E's last transition. f ≤ n·N_ep + 1 ✓.

## 4. DATA (va_check.py; own definitions; S3 + random starts)
| set | runs | phases | SG checks | ACC phases checked (n ≤ 11) | EPOCH (a) checks / per-class freeze checks | max epochs per phase | max (epoch fallbacks − (n − 1)) | violations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41.txt × 3 | 1,236 | 7,168 | 23,201 | 349 | 3,938 / 81 | 50 (lev_l_x.pg) | −1 (n3all_maxph_0, n 3) | 0 |
| R2-N5-KW/files.lst × 2 | 1,006 | 4,121 | 25,063 | 463 | 5,708 / 129 | 53 (rise_thin51_n40) | −1 | 0 |
| box-43/44 instances × 5 | 50 | 272 | 480 | 74 | 719 / 17 | 17 (dch16_n44) | −5 | 0 |
| random 𝒞^kO n 4-12 | 20,000 | 49,411 | 2,587 | 43,117 | 353,711 / 18,024 | 3 | −2 | 0 |
| climbs, objective max (epoch fallbacks − (n − 1)), n 4-7, 4 × 3,000 steps | 47,996 | 100,875 | 4,827 | 100,875 | 662,903 / 38,213 | 2 | −2 (best of four: −2, −3, −3, −5) | 0 |
Checked on every phase: SG, ACC (b) (transitions and per-vertex counts against N_K and |K_c(z)| − 1) and (c) (f ≤ 1 + N_K), EPOCH (c) (f ≤ 1 +
n·N_ep); for n ≤ 11 ACC (a) (κ_t ∈ K_c(z), by simple-path enumeration) and EPOCH (a) (both bounds, every j) with the per-class freeze. Max
|K_c(z)| 53. σ̄|Q repeats inside a phase: 203 phases (lib41) and 187 (my 𝒞^1O files) — the packet's §4 DATA claim, confirmed by my own engine.
Mutation controls (lib41, S3): sg (strict gain asked to fail) 12,653; kk (ACC (b) with N_K − 2) 61 — both bite; ep (EPOCH (c) with n − 1 per
epoch) does not bite: f stays far below n·N_ep in all data.
- N-ACC-3 (the Lead's request): EPOCH (a)'s global freeze (after e_{n−1}) and EPOCH (b) need an epoch with ≥ n − 1 in-phase fallbacks. NO run
  reaches one: the best is 1 short (n = 3) in the library and 2 short after four hill climbs on small games (47,996 checked runs). So I could
  NOT build a test that reaches EPOCH (a)/(b)'s global regime; they rest on their proofs (checked above). Their per-class form (N-ACC-2) is
  exercised and holds.

## 5. Notes
- N-ACC-1: (SG) is landed "on all games" (R19 (d)) and its proof has no one-Odd step.
- N-ACC-2: EPOCH (a) also gives the per-class freeze at |U_c| − 1 epoch fallbacks; worth one line in a fixes file (it is the form the data reach).
- N-ACC-3 (DATA): EPOCH (a)/(b)'s global regime is not reached by data or by my climbs.
