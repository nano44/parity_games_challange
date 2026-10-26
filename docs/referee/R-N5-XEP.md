# R-N5-XEP: REFEREE report on packet P-N5-XEP (L-NEW box 44: R-STICK_D, SN-PREFIX_D, Fact D-EPOCH, Lemma X-EP; every game)
Referee: REFEREE (successor 12, session_01KNDBjZvPFLaNjEdCmEWBcN), Opus 5.5 (owner ruling D15).
- Routing: the Lead's messages of 05:2xZ and 05:30Z (Lead's stamps).
- Object: docs/new/P-N5-XEP-box44.md at trunk 8460897d, sha1 237dd5eb31f60f19ef70099dc9351532e88b56f8 (checked with
  `git show 8460897d:docs/new/P-N5-XEP-box44.md | sha1sum`; identical on my tree), 88 lines. Author: L-NEW successor 23.
- Written 2026-10-26T05:33Z-05:35Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ XEP file on my tree; none opened. No lane code run (experiments/new/box44/rstick.py,
  randstarts.py). D1.
- Premises checked against the landed text: RESULTS R55 (a) G_D (a) ("for every state k and every v ∈ F_D, Ξ_k(v) = W_k(v)", no
  hypothesis; its premise list confirms R21 (a) XW and R18 (d) Lemma S (c) "⇒" game-general, both referees); R23 (g) WM ("inside a phase,
  W_{k+1} ⊵ W_k pointwise at every transition that is not an S4c fallback"), with its proof in docs/si/P-N5-Z-box5.md §8 (S4a's σ_{k+1}
  maximises V_{·,τ_k} over the arena by R18 (d) S (c); σ_k is in the arena; so W_{k+1} ⊵ W_k): no one-Odd step, so WM holds on every game
  (XEP-N2); SPEC S1 (injective rewards; cycle nodes first); R38 (a). In review when the packet was written, now signed by both referees:
  P-N5-ACCEL EPOCH (b) (my R-N5-ACCEL with §C) and P-N5-FBK ALT with its N_ep corollary (my R-N5-FBK with §C).
- Tool: scratch/xep_probe.py (own engine; any game; random start pairs as asked). Logs scratch/xep_logs/ (run_all.sh).

## Verdicts
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | Lemma R-STICK_D (in-phase S4a transition: a split v ∈ R_D(s) lies in R_D(s+1)) | SIGNED (XEP-N1) |
| §2 | Corollary SN-PREFIX_D (a) unsplit prefix, (b) ≤ 1 membership change after it, (c) X_D ≤ (f + 1)n + f + X_SN^D | SIGNED (XEP-N1: (c) is loose) |
| §3 | Fact D-EPOCH | SIGNED |
| §4 | Lemma X-EP, and its form with ALT (conditional on P-N5-ACCEL EPOCH (b), P-N5-FBK ALT, as cited) | SIGNED (a REDUCTION: residual X_SN^pre OPEN) |
| §5 | qc_toggle instance, X_SN^pre, data | not signed (as briefed); qc_toggle re-run on my engine |
No gap. Notes XEP-N1 (sharpening: inside an S4a run no crossing has only split changers), XEP-N2 (WM's class), XEP-N3 (DATA). X-EP is a
reduction (crossings given N_ep and X_SN^pre); not a running-time bound. Not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. R-STICK_D
- Suppose v split at s, v ∈ F_D(s+1); c := λ(v) (constant on the phase), c′ := λ_{W,s}(v) ≠ c. G_D (a) at s+1: W_{s+1}(v) = Ξ_{s+1}(v), cycle
  node c. WM (S4a, in phase): W_{s+1}(v) ⊵ W_s(v); different cycle nodes, injective rewards, so rew(c) > rew(c′). XW at s: Ξ_s(v) ⊴ W_s(v), so
  rew(c) < rew(c′). Contradiction ✓. No class step (per vertex) ✓.
- XEP-N1 (part 1): the qualifier "v ∈ R_D(s)" is automatic: if v ∈ F_D(s), G_D (a) at s gives Ξ_s(v) = W_s(v), so v is unsplit. Hence every
  split vertex lies in R_D(s) and, at an S4a transition, in R_D(s+1).
- VERDICT: SIGNED.

## 2. SN-PREFIX_D
- (a) WM along the run: W(v) non-decreasing, so rew(λ_W(v)) non-decreasing (S1 compares rewards first) ✓; XW: rew(λ_W(v)) ≥ rew(λ(v)), equality
  iff λ_W(v) = λ(v) (injective) ✓; λ(v) constant ✓. Once split, split for the rest of the run ✓.
- (b) after the prefix v is split, so (R-STICK_D) it never leaves R_D; at most one change ✓.
- (c) ≤ f + 1 S4a runs; a crossing inside a run with only split changers has an entering split vertex, and each vertex enters at most once
  after its prefix, so ≤ n per run; the rest are fallbacks (≤ f) or in X_SN^D ✓. The bound is correct.
- XEP-N1 (part 2, sharpening; not needed): by part 1 a split vertex at s is already in R_D(s) and stays at s+1, so inside an S4a run NO
  crossing has only split changers; hence X_D ≤ f + X_SN^D, and in X-EP the n·n term per epoch can be dropped. DATA: of 3,222 lib41
  crossings (S3), 120 have only split changers, and all 120 are fallback transitions (my probe's ALLSPLIT_S4A check: 0 at S4a transitions).
- VERDICT: SIGNED.

## 3. D-EPOCH
- τ constant on a phase; an Odd vertex of out-degree 1 has σ̄ = τ, so D_s = {u ∈ Q : σ̄_s(u) ≠ τ(u)} ✓; it changes only where σ̄|Q changes ✓;
  on an epoch D and σ̄ are constant, the honest frame is G_E and the W-frame G_τ, differing exactly at D ✓. VERDICT: SIGNED.

## 4. X-EP
- Every crossing is an in-phase transition, at an epoch boundary (≤ N_ep − 1) or with both ends in one epoch E ✓.
- Both ends in E, source > e_{n−1}: EPOCH (b) (P-N5-ACCEL §3, signed): that part of E has ≤ 4n(n − 1) + 1 transitions ✓.
- Both ends in E, source ≤ e_{n−1} (all of E if fewer than n − 1 fallbacks): ≤ n − 1 fallback transitions and ≤ n S4a runs; per run ≤ n
  crossings with only split changers (SN-PREFIX_D (a), (b); in fact 0, XEP-N1); the rest are X_SN^pre(E) by definition ✓.
- Sum: (N_ep − 1) + Σ_E [(4n(n − 1) + 1) + (n − 1) + n² + X_SN^pre(E)] = (N_ep − 1) + N_ep(n² + n + 4n(n − 1)) + Σ_E X_SN^pre(E) ✓.
- With ALT (P-N5-FBK §4 corollary, signed by both): N_ep ≤ 1 + Σ_q (ρ_q + tie_q + nc_q + cyc_q) ✓, so X_D = O(n²)(1 + ρ + ties + non-clean +
  cycle-node changes) + Σ X_SN^pre ✓.
- VERDICT: SIGNED, as a reduction; X_SN^pre is OPEN (§5, not signed).

## 5. Data (DATA, not proof; scratch/xep_probe.py, own engine; logs scratch/xep_logs/)
Checks: premises GDA (G_D (a)) and WM at every state / in-phase non-fallback transition; SPLITR (split ⇒ ∈ R_D, XEP-N1); RSTICK; SNPA; SNC;
DEP; XEP. Crossing classes: boundary / after the epoch freeze / pre-freeze with an unsplit changer (X_SN^pre) / pre-freeze, only split
changers (ALLSPLIT; at S4a transitions predicted 0).
| set | runs | phases | RSTICK | WM | crossings (boundary / after freeze / X_SN^pre / all-split) | max X_D | max epochs | failures |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41, all 412 games, S3 | 412 | 2,335 | 14,253 | 220,486 | 3,222 (1,269 / 0 / 1,833 / 120, all 120 at fallbacks) | 99 | 50 | 0 |
| lib41, n ≤ 64, S3 + 4 random | 1,835 | 9,032 | 31,413 | 607,387 | 8,010 (3,894 / 0 / 3,863 / 253) | 99 | 50 | 0 |
| box-43/44 instances + qc_toggle, S3 + 4 random | 55 | 290 | 649 | 5,893 | 112 (36 / 0 / 76 / 0) | 27 | 17 | 0 |
| 3,000 random games, 0-4 Odd choice vertices, n 4-14, seed 72, S3 + 2 random | 9,000 | 21,820 | 66 | 16,421 | 137 (102 / 0 / 33 / 2) | 3 | 3 | 0 |
- The "all 120 at fallbacks" check (ALLSPLIT_S4A) was added after the other batches ran; it was run on the first row (all of lib41, S3)
  only. The all-split counts in the other rows (253, 0, 2) are not split by transition type.
- My engine reproduces the packet's §5 lib41 (S3) figures exactly: R-STICK_D 14,253 checks; 3,222 crossings = 1,269 at epoch boundaries +
  1,953 inside epochs, 0 after a freeze, 1,833 unsplit pre-freeze (the other 120 are fallback crossings with only split changers).
- qc_toggle (experiments/new/box44/instances/qc_toggle.pg, sha1 27850ecc3d9e660aefa6a3401d6af0cfc2b3317c, checked): n 5, Q = {0, 2, 3, 4};
  from S3 one S4a transition, one phase, λ ≡ 4 (an Odd choice vertex), D = {0}, σ(1): 2 → 0, vertex 1 unsplit (λ_W = λ = 4) and enters R_D:
  one X_SN^pre crossing — exactly as stated.
- XEP-N3 (vacuity): no epoch reaches n − 1 fallbacks ("after freeze" = 0 everywhere), so EPOCH (b)'s term is vacuous in data, as the packet
  says. Everything else is exercised. The premises G_D (a) and WM hold at 1.58M / 0.85M checks.
- Reproduce (from docs/referee/scratch): `sh xep_logs/run_all.sh` (fixed seed; file starts seeded by the RELATIVE path).

## 6. Notes for the fixes file
- XEP-N1: optional sharpening: split ⇒ ∈ R_D (G_D (a)); inside an S4a run no crossing has only split changers, so X_D ≤ f + X_SN^D and the
  n² term per epoch in X-EP can be dropped. The stated bounds are correct.
- XEP-N2: WM (R23 (g)) is signed under a 𝒞^1O setting line; its proof (P-N5-Z §8: R18 (d) S (c) "⇒" + σ_k in the arena) is game-general;
  a landing note may record it.
- XEP-N3: DATA.

## §C. Comparison with REFEREE-2 (REFEREE successor 12; written 2026-10-26T05:57Z by date -u; (Opus 5.5, D15))
- Routing: the Lead's message of 05:54Z (Lead's stamp), item (1). Objects: this report (62f4bd2c; §1-§6 above unchanged) and
  docs/referee-2/R2-N5-XEP.md (referee-2 fd43a69f, successor 14), opened after 62f4bd2c was pushed. Same pinned text (sha1 237dd5eb…).

### C.1 Verdicts side by side
| § | statement | REFEREE (62f4bd2c) | REFEREE-2 (fd43a69f) | joint |
| --- | --- | --- | --- | --- |
| §1 | R-STICK_D | SIGNED (XEP-N1) | SIGN (N-XEP-1) | signed |
| §2 | SN-PREFIX_D (a)-(c) | SIGNED (XEP-N1: (c) loose) | SIGN (N-XEP-1: (b) "never", (c) sharper) | signed |
| §3 | D-EPOCH | SIGNED | SIGN | signed |
| §4 | X-EP | SIGNED (reduction; cond. EPOCH (b)) | SIGN (cond. EPOCH (b)) | signed |
| §4 | "With ALT" line | SIGNED (cond. ALT) | SIGN as an inequality (cond. ALT); last clause a READING (N-XEP-2) | inequality signed; last clause a READING (we accept N-XEP-2) |
| §5 | data, qc_toggle, X_SN^pre | not signed | not signed | not signed |
No disagreement; no gap in either report.

### C.2 Joint note map
| REFEREE | REFEREE-2 | relation | joint status |
| --- | --- | --- | --- |
| XEP-N1 (split ⇒ ∈ R_D by G_D (a); no all-split crossing inside S4a runs; X_D ≤ f + X_SN^D) | N-XEP-1 (same; also: SN-PREFIX_D (b)'s "at most once" is "never") | SAME | optional sharpening |
| XEP-N2 (WM game-general: P-N5-Z §8 proof, R55's S (c) confirmation) | §1 premises (same: WM's proof in N5-X-box4 §8, RESULTS l.1134 "transferred to every game by (F1) in G_τ"; XW = (VJ) at τ′ := τ_k, signed on every game in P-N5-1E) | SAME conclusion, two routes | landing note |
| — (I signed the line without separating its last clause) | N-XEP-2 (the clause "charged to the quantity that also bounds fallbacks (R56 (f))" is a READING: R56 (f) bounds f by ρ alone; ties, non-clean and cycle-node changes are extra quantities) | ACCEPTED: correct; the inequality is what is signed | landing entry: inequality signed, last clause READING |
| XEP-N3 (DATA: EPOCH (b)'s term vacuous) | §5 (same; best −1) | SAME | DATA |

### C.3 Data
| item | REFEREE | REFEREE-2 | agree? |
| --- | --- | --- | --- |
| lib41 S3 crossings | 3,222 = 1,269 + 1,833 + 120 (all 120 at fallbacks) | 3,222 = 1,269 / 1,953 inside / 0 after freeze; 1,833 X_SN^pre | YES, exactly (and both match the packet) |
| all-split crossings occur only at fallbacks | lib41 S3: 120 of 120 at fallbacks | lib41 × 3: 178, all at fallbacks | YES |
| other sets | lib41 n ≤ 64 × 5, box-43/44 × 5, 3,000 random × 3 | 𝒞^1O files, lib2o, box-43/44, 10,000 random × 2 | YES (0 failures in both) |
| controls | — | rstick_all 6,444, xsn0 607 bite | — |
