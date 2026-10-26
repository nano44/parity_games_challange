# R2-N5-XEP: second-referee check of packet P-N5-XEP (L-NEW box 44: R-STICK_D, SN-PREFIX_D (a)-(c), Fact D-EPOCH, Lemma X-EP; every game). REFEREE-2 (successor 14), written 2026-10-26 05:3xZ-05:5xZ (date -u)
Signature: (Opus 5.5, D15). Lead's order 05:20Z (its stamp), queue item 1.
Object: docs/new/P-N5-XEP-box44.md, `git show 8460897d:docs/new/P-N5-XEP-box44.md | sha1sum` -> 237dd5eb31f60f19ef70099dc9351532e88b56f8
(= the Lead's pin; = my tree), 88 lines (L-NEW successor 23). No fixes file.
Background read (texts): RESULTS R55 (setting, (a)), R21 (a) XW, R23 (g) WM and RESULTS l. 1134 (WM "transferred to every game by (F1) in
G_τ (G-FB-3)"), R38 (a); WM's proof (docs/si/N5-X-box4.md §8); P-N5-ACCEL §3 (EPOCH (b); both referees signed, §Cs done), P-N5-FBK §4 (ALT;
my R2-N5-FBK); SPEC S1, S4a, S4c.
Independence: no docs/referee/ XEP file (`git ls-tree --name-only` on trunk and origin/claude/referee: none); none opened. The lane's
rstick.py / randstarts.py not run or imported.
Tools (own code, docs/referee-2/R2-N5-XEP/): xep_check.py (succ. 13's SPEC loop; W_k by si.Engine on G_τ), run_all.sh, logs/. Random start
pairs used throughout, as the Lead asked (runs #1, #2, … are random pairs; #0 is S3).
Labels: PROVED (L-NEW 23), every game. X-EP is a REDUCTION (crossings given N_ep and the residual X_SN^pre); its ALT line is conditional on
P-N5-FBK's ALT (signed by me; REFEREE pending) and §4 on P-N5-ACCEL's EPOCH (b) (signed by both). G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | notes |
| --- | --- | --- |
| §1 Lemma R-STICK_D | SIGN | N-XEP-1 (its R_D(s) hypothesis is automatic) |
| §2 SN-PREFIX_D (a) | SIGN | — |
| §2 SN-PREFIX_D (b) | SIGN | N-XEP-1 (in fact no change at all after the prefix) |
| §2 SN-PREFIX_D (c) | SIGN | N-XEP-1 (sharper: X_D ≤ f + X_SN^D) |
| §3 Fact D-EPOCH | SIGN | — |
| §4 Lemma X-EP | SIGN (conditional on P-N5-ACCEL EPOCH (b)) | — |
| §4 "With ALT" line | SIGN as an inequality (conditional on P-N5-FBK ALT); its last clause is a READING | N-XEP-2 |
| §5 | not signed (as briefed) | crossing counts reproduced exactly (§5) |
No gap. No (P). TARGET.md diff: no TARGET.md object claimed; a reduction of crossings per phase.

## 1. Premises
- R55 (a), landed (no hypothesis): "for every state k and every v ∈ F_D, Ξ_k(v) = W_k(v)" ✓ (RESULTS l. 2798). R_D / F_D as in R55's setting
  (vertices whose (σ_k, τ_k)-play meets D_k) ✓.
- R21 (a) XW and R23 (g) WM are signed under a 𝒞^1O setting line. XW: Ξ_k ⊴ W_k is (VJ) applied to τ′ := τ_k, which both referees signed
  on every game (P-N5-1E, R2-N5-1E §2 and §C) ✓. WM: its proof (N5-X-box4 §8) is "σ_{k+1} is an optimal strategy of the one-player arena
  (Even restricted to {σ_k(v)} ∪ Iσ(v), Odd fixed to τ); an optimal one-player strategy dominates every arena strategy pointwise; σ_k is
  an arena strategy". τ constant is part of the phase key on every game, and S4a computes exactly that arena optimum (SPEC S4a; also the
  Runner I use). No one-Odd step ✓; RESULTS l. 1134 records the same transfer (G-FB-3) ✓.
- EPOCH (b) (P-N5-ACCEL §3) as cited ✓; ALT's N_ep corollary (P-N5-FBK §4) as cited ✓.

## 2. R-STICK_D and SN-PREFIX_D: SIGN
- R-STICK_D ✓. v split at s: c := λ(v) ≠ c′ := λ_{W,s}(v). If v ∈ F_D(s+1): R55 (a) at s+1 gives W_{s+1}(v) = Ξ_{s+1}(v), cycle node c. WM at the
  in-phase S4a transition: W_{s+1}(v) ⊵ W_s(v); different cycle nodes, injective rewards, so rew(c) > rew(c′). XW at s: Ξ_s(v) ⊴ W_s(v) with
  cycle nodes c, c′: rew(c) < rew(c′). Contradiction ✓.
  - N-XEP-1: the hypothesis "v ∈ R_D(s)" is automatic: R55 (a) at s gives Ξ_s = W_s on F_D(s), so every split vertex lies in R_D(s). Hence:
    (i) at an S4a transition no split vertex changes R_D-membership at all (it cannot enter, being already in, and cannot leave, by
    R-STICK_D); (ii) SN-PREFIX_D (b) holds with "at most once" replaced by "never"; (iii) every crossing at an S4a transition has a
    membership-changing vertex unsplit at its source, so §2 (c)'s n·(f + 1) term can be dropped: X_D ≤ f + X_SN^D. The packet's statements
    are true as written (weaker). DATA: 0 changes after the prefix in every sample; X_D ≤ f + X_SN^D holds everywhere (§5).
- (a) ✓: WM along the run makes rew(λ_W(v)) non-decreasing (the order compares rewards first); XW gives rew(λ_W(v)) ≥ rew(λ(v)) with equality
  iff unsplit; λ(v) constant; so split is absorbing within the run.
- (b) ✓ (and N-XEP-1 (ii)).
- (c) ✓: ≤ f + 1 S4a runs; per run, crossings whose changers are all split: ≤ n (in fact 0, N-XEP-1); fallback transitions ≤ f; the rest
  are in X_SN^D.

## 3. D-EPOCH: SIGN
τ is constant on a phase; an Odd vertex of out-degree 1 has σ̄ = τ, so D_s ⊆ Q and D changes only where σ̄|Q does ✓. On an epoch σ̄ is
constant (non-Q Odd vertices are forced), so the honest frame is the one-player game G_E and the W-frame G_τ; they differ exactly on D ✓.
An Odd choice vertex that is a cycle node has σ̄ constant on each epoch ✓ (it is in Q).

## 4. X-EP: SIGN (conditional on EPOCH (b))
- Every in-phase transition is an epoch boundary (σ̄|Q changes: ≤ N_ep − 1 of them) or has both ends in one epoch ✓.
- Inside E after e_{n−1}: EPOCH (b) bounds that part of E by 4n(n − 1) + 1 transitions ✓.
- Inside E up to e_{n−1}: ≤ n − 1 fallback transitions and ≤ n S4a runs; per run ≤ n crossings with only split changers (SN-PREFIX_D (a),
  (b); in fact 0); the rest in X_SN^pre(E) ✓ (a fallback crossing with an unsplit changer is counted twice; only loosens).
- Sum ✓: (N_ep − 1) + Σ_E [(4n(n − 1) + 1) + (n − 1) + n² + X_SN^pre(E)] = (N_ep − 1) + N_ep(n² + n + 4n(n − 1)) + Σ_E X_SN^pre(E).
- N-XEP-2 ("With ALT" line): substituting ALT's N_ep ≤ 1 + Σ_q(ρ_q + tie_q + nc_q + cyc_q) gives the stated O(n²)·(1 + ρ + ties + non-clean +
  cycle-node changes) + Σ_E X_SN^pre(E) ✓ (conditional on FBK's ALT). The clause "charged to the quantity that also bounds fallbacks (R56 (f))"
  is a READING: R56 (f) bounds f by ρ alone; ties, non-clean and cycle-node changes are additional quantities, not R56's.

## 5. DATA (xep_check.py; own definitions; S3 (#0) and random start pairs (#1, #2, …))
| set | runs | phases | crossings X_D | at epoch boundaries / inside epochs / after an epoch freeze | X_SN^pre | crossings at fallbacks | max X_D / max N_ep | violations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41.txt, S3 + 2 random | 1,236 | 7,136 | 5,633 | 2,617 / 3,016 / 0 | 2,838 | 991 | 99 (xsn91_n48) / 50 | 0 |
| lib41.txt, S3 only | 412 | 2,335 | 3,222 | 1,269 / 1,953 / 0 | 1,833 | 686 | 99 / 50 | 0 |
| R2-N5-KW/files.lst (503 𝒞^1O), S3 + 2 random | 1,509 | 6,295 | 8,755 | 3,269 / 5,486 / 0 | 5,162 | 2,521 | 99 / 53 | 0 |
| lib2o_noref.lst (41 𝒞^2O), S3 + 3 random | 164 | 479 | 216 | 56 / 160 / 0 | 160 | 47 | 21 / 8 | 0 |
| box-43/44 instances, S3 + 5 random | 60 | 328 | 106 | 46 / 60 / 0 | 60 | 35 | 27 / 17 | 0 |
| 10,000 random 𝒞^kO n 4-12, 2 random pairs each | 20,000 | 49,449 | 351 | 291 / 60 / 0 | 60 | 12 | 2 / 3 | 0 |
Checks on every run: GDA (R55 (a) frames), SPLITR, RSTICK, SNPA, SNPB, SNPC and the sharper SNPC2, DEP, XEP; 0 violations.
- Reproduction: lib41 from S3 gives 3,222 crossings = 1,269 at epoch boundaries + 1,953 inside epochs, 0 after an epoch freeze, 1,833 X_SN^pre
  — EXACTLY the packet's §5 counts (the lane's code not run).
- N-XEP-1 in data: SNPB's changes after the unsplit prefix are 0 in every sample; SNPC2 (X_D ≤ f + X_SN^D) holds everywhere; the crossings
  without an unsplit changer (e.g. lib41: 5,633 − 5,455 = 178) all occur at fallback transitions (991).
- Mutation controls (lib41 × 3): rstick_all (R-STICK asked for UNSPLIT vertices too) fails 6,444 times — the split hypothesis is needed;
  xsn0 (SNPC2 without X_SN^D) fails 607 times — the residual is real (X_SN^pre is the bulk of the inside-epoch crossings).
- Not reached: no epoch reaches n − 1 fallbacks (best −1), so EPOCH (b)'s term of X-EP is vacuous in data (as the packet says); X-EP's bound
  is then carried by its N_ep and X_SN^pre terms, which are exercised.
- Reproduce: `sh docs/referee-2/R2-N5-XEP/run_all.sh` (≈ 80 s); `XP_MUT=rstick_all|xsn0` for the controls.

## 6. Notes
- N-XEP-1: every split vertex is in R_D (R55 (a)); so split vertices never change R_D-membership at S4a transitions, SN-PREFIX_D (b)'s
  "at most once" is "never", and §2 (c) sharpens to X_D ≤ f + X_SN^D. Optional; the packet's forms are true.
- N-XEP-2: the "With ALT" inequality is signed conditional on FBK's ALT; its last clause (charged to R56 (f)'s quantity) is a READING.
- DATA: the packet's §5 crossing counts are reproduced exactly; X_SN^pre carries most inside-epoch crossings; EPOCH (b)'s term is unreached.
