# R-N5-VILB: REFEREE report on packet P-N5-VILB (L-NEW box 44: every in-phase fallback is at least one value-iteration round on each honest class's min-max reachability game; Lemma VI-LB, every game)
Referee: REFEREE (successor 12, session_01KNDBjZvPFLaNjEdCmEWBcN), Opus 5.5 (owner ruling D15).
- Routing: the Lead's message of 04:30Z (Lead's stamp), item (2).
- Object: docs/new/P-N5-VILB-box44.md at trunk e7febdc2, sha1 872d4400194ed9d0f6ad9f6a2cc82f2f0821cd9f (checked with
  `git show e7febdc2:docs/new/P-N5-VILB-box44.md | sha1sum`; identical on my tree), 87 lines. Author: L-NEW successor 23.
- Written 2026-10-26T04:33Z-04:39Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: docs/referee-2/R2-N5-VILB* is on my tree (merged with trunk) but NOT opened before this report was pushed. No
  lane code run. [BGHM] (arXiv:1407.5030) not opened: it is cited only in the not-to-sign §4. D1.
- Compared against: P-N5-FBRED §1.1 (signed by both referees; my lane's R-N5-FBRED with §C), RESULTS R48 κ-FB-ROUND, R15 (a), R17 (a)
  (V1), R38 (a), SPEC S1, S2, S4c.
- Tool: scratch/vilb_probe.py (own engine; any game). Logs scratch/vilb_logs/ (run_all.sh).

## Verdicts
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | (Aκ), (M1κ), (M2κ), κ-FB-ROUND (per class, every game) | SIGNED |
| §2 | Lemma VI-LB: κ_t(z) ≥ Val^{≤j}_c(z) for t > g_j, z ∈ U_c, every phase and class | SIGNED |
| §2 | "Relation to R48's κ-HAT-FREEZE (a)" (labelled READING inside §2) | agreed as a READING; not signed |
| §3, §4 | what VI-LB does not give; [BGHM] reading and obstruction | not signed (as briefed); §3 agreed (§3 below) |
No gap. Notes VILB-N1 (the empty-max / empty-min conventions never fire), VILB-N2 (data: VI-LB is exercised and often tight, unlike the
late regime of FB-RED). Not a running-time bound: VI-LB is a LOWER bound on progress and counts nothing. Not a TARGET.md claim;
G-N5-TIME stays OPEN.

## 1. §1: the restated facts and κ-FB-ROUND
- The four items are word for word the per-class forms of P-N5-FBRED §1.1, which I re-derived against FBP (P-N5-FBPOLY-box41 §0.3, §1)
  for the FBRED §C (R-N5-FBRED §C, C.1), and which both referees signed there:
  - (Aκ): λ_t(z) = c ≠ z, (V1), ⊕ adds z iff rank(z) > rank(c); no double count because z on its own cycle has rank < rank(c) ✓.
  - (M1κ): equal cycle node, so S1's order is the order of (signed weight, ±length) ✓. (M2κ): R15 (a) and λ constant on the phase ✓.
  - κ-FB-ROUND: either x is no better than σ_k(v) ((M1κ), (Aκ), (M2κ)), or (v, x) ∈ Iσ_k and S4c moves v to its best gate target x*
    (Ξ_k(x*) ⊵ Ξ_k(x)); (Aκ) at k+1 puts x* in U_c ✓. The fallback is Even's (an in-phase fallback; an Odd fallback changes τ) ✓.
- VERDICT: §1 SIGNED.

## 2. Lemma VI-LB
- Definitions (§0): Γ_c on U_c, Even maximises, EVERY Odd vertex minimises (forced or not), target c with value (0, 0); Val^{≤0} = −∞ off c;
  Val^{≤j}(z) = κwt_c(z) + max / min over succ(z) ∩ U_c of Val^{≤j−1}. This is the standard j-step value-iteration operator with the target
  absorbing. ✓
- Base j = 0: κ_t(c) = (0, 0) (c's value is (c, ∅, 0)); every other z has Val^{≤0} = −∞ ✓. "t > g_0" = every state ✓.
- Step, Even z ≠ c, t > g_j: k := g_j < t; for every x ∈ succ(z) ∩ U_c, κ-FB-ROUND at k gives κ_{k+1}(z) ≥ κwt_c(z) + κ_k(x); the hypothesis
  at k needs k > g_{j−1} ✓ (for j = 1, every state); (M2κ) from k + 1 to t needs k + 1 ≤ t, both in the phase ✓. Max over x ✓.
- Step, Odd z ≠ c (forced or choice): (Aκ) at t gives κ_t(z) = κwt_c(z) + κ_t(σ̄_t z) with σ̄_t(z) ∈ succ(z) ∩ U_c, so κ_t(z) ≥ κwt_c(z) +
  min_x κ_t(x); the hypothesis at t (t > g_j > g_{j−1}) applies to every x ∈ U_c ✓.
- z = c: both sides (0, 0) ✓. Arithmetic with −∞ ✓ (a −∞ bound is vacuous).
- VILB-N1 (conventions): "max over an empty set = −∞, min over an empty set = +∞" never fires for z ∈ U_c ∖ {c}: its honest successor
  lies in succ(z) ∩ U_c ((Aκ)), so both sets are non-empty. Harmless; worth knowing that +∞ cannot enter.
- The class hypothesis: none. Odd choice vertices are handled by the min case only, which uses nothing but (Aκ) ✓. No (h_D), no τ or c_w
  hypothesis ✓. Premise list matches what the proof uses ✓ (KEY R38 (a) only for "phase = joint λ-phase").
- The READING inside §2 (HAT-FREEZE (a) is a special case): agreed. Deleting the Odd choice vertices other than c (G_c of P-N5-FBRED, or
  G_Û of FBP) can only lower Even's value (fewer continuations for Even, and a forced Odd vertex's min is its one successor), so the bound
  over simple paths of G_c with ≤ j edges is ≤ Val^{≤j}_c; VI-LB therefore implies κ-HAT-FREEZE (a)'s inequality. Not signed (READING).
- VERDICT: Lemma VI-LB SIGNED.

## 3. §3 (not to sign): what VI-LB does not give
I agree with each bullet: no upper bound (so no freeze, no FREEZE-EXIT, no count); no count of fallbacks, S4a steps or phases; S4a steps also
raise κ and are ignored; Val^{≤j} is over walks while honest values are simple-path values; per class of the current phase only. The §4
[BGHM] reading and the exponential gadget are OPEN and not signed; I did not open [BGHM].

## 4. Data (DATA, not proof; scratch/vilb_probe.py, own engine; logs scratch/vilb_logs/)
Checks at every state of every phase: AK, M2, VILB (κ_t(z) ≥ Val^{≤j}_c(z) with j = the in-phase fallbacks before t, every class c, every z ∈ U_c);
at every in-phase fallback: FBR (κ-FB-ROUND). Counters: VILB_finite (Val^{≤j} finite), VILB_tight (equality), CTRL (states where the
j + 1 bound fails). Mutation control VILB_MUT=oddmax: every Odd vertex maximises in Val.
| set | runs | phases | max f per phase | VILB checks (finite / tight) | FBR checks | CTRL (j + 1 fails) | failures |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lib41, n ≤ 64 (367 games; 45 with n > 64 skipped), S3 + 2 random starts | 1,101 | 5,393 | 33 | 602,116 (105,188 / 61,861) | 110,021 | 1,216 | 0 |
| box-43 + box-44 instances (10 files, incl. fb17_n32), S3 + 4 random | 50 | 281 | 17 | 14,437 (2,666 / 2,165) | 4,968 | 33 | 0 |
| 2,000 random games, 0-4 Odd choice vertices, n 5-14, seed 31, S3 + 2 random | 6,000 | 14,857 | 1 | 160,495 (31,609 / 31,547) | 1,814 | 971 | 0 |
| MUTATION oddmax, lib41 n ≤ 64, S3 | — | 1,737 | 33 | 288,314 | 75,911 | — | 46,067 VILB failures (control bites) |
- VILB-N2: unlike FB-RED's late regime, VI-LB is exercised at every j that occurs (up to 33 fallbacks in one phase) and is TIGHT at 59% of
  the finite lib41 checks; the mutation shows the check discriminates. The regime where VI-LB could force a bound (exponentially many
  fallbacks in a phase) is not reached, as §3 says.
- Reproduce (from docs/referee/scratch): `sh vilb_logs/run_all.sh` (fixed seed; file starts seeded by the RELATIVE path).

## 5. Notes for the fixes file
- VILB-N1: the empty-set conventions in Val^{≤j} never fire for z ∈ U_c ∖ {c} ((Aκ)); optional wording.
- VILB-N2: DATA (exercised, often tight; mutation bites).
