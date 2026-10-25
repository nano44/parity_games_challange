# Referee packet P-N5-PFZ-ext: the freeze holds on P-epochs (P(θ) constant), θ-changes inside a P-epoch are length-only, and breaks per HN stretch are polynomial in the number ρ_S of P(θ)-changes (P-FREEZE′, LEN-TAIL′, NO-CROSS-A′, θ-LEN, BRK-POLY′) (box 39)
L-NEW successor 18 (Opus 5.5, D15/D18, L37/L40), session_01BhkSHzG2cPM2Rdbj5Y2NJV. Written 2026-10-25 15:2xZ by date -u. Frozen at this
commit: corrections go in a fixes file, never here.
- Why a second file. The Lead's message of 15:19Z (Lead's stamp) asked P-N5-PFZ to hold the working doc's §12 as well. It crossed my
  freeze of P-N5-PFZ (docs/new/P-N5-PFZ-box39.md, l-new c9f9caa1, sha1 3c617e06f7b9c67d5d9cd865acd134f3a8aed071, reported 15:21Z). That
  file is frozen, so §12 is packaged here as a companion. It is meant to be reviewed together with P-N5-PFZ, and it uses P-N5-PFZ's
  notation, facts and proofs by section number.
- Source: docs/new/N5-RW-box39.md §12 (working doc, l-new b1439f57).
- Labels (D18/L40): PROVED (L-NEW succ. 18, unrefereed), OPEN, DATA. Scope as in P-N5-PFZ: the candidate N5 on 𝒞^1O inside one phase;
  not a running-time bound, not a TARGET.md claim, not a step-4 pass; G-N5-TIME stays OPEN. No (P).

## To sign, and what is not to sign
| § | statement | label | depends on |
| --- | --- | --- | --- |
| §1 | Theorem P-FREEZE′ (P-FREEZE on P-epochs), with LEN-TAIL′ and NO-CROSS-A′ | PROVED | P-N5-PFZ §1-§4 |
| §2 | Lemma θ-LEN | PROVED | R15 (a), (V1) |
| §3 | Theorem BRK-POLY′ | PROVED | P-N5-PFZ §5 (RISE′), §6's window argument; §1, §2 here |
- NOT TO SIGN (OPEN): ρ per phase (the number of P(θ)-changes in a phase); W-TIE steps (working doc §4); everything listed as OPEN in
  P-N5-PFZ §7.

## 0. Definitions (in addition to P-N5-PFZ §0)
- A P-EPOCH is a maximal run Π of consecutive states of one phase with P(θ) constant. θ's length may change inside Π. Every θ-run lies
  inside one P-epoch.
- On Π put M_Π(o) := wt(P(θ)), constant on Π, and M_Π(c_θ) := 0. Mopt_Π is Mopt of P-N5-PFZ §0 with these terminal values.
  f_1 < f_2 < … are the in-phase Even S4c fallback transitions of Π.
- ρ_S := the number of transitions of the HN stretch S at which P(θ) changes. θ_S, B_S, U, M, wt, G_U, U-rise, R̄-rise are as in
  P-N5-PFZ §0.

## 1. Theorem P-FREEZE′ (PROVED, L-NEW succ. 18; 𝒞^1O)
Statement. P-N5-PFZ §2 (a)-(c), §3 (LEN-TAIL) and §4 (NO-CROSS-A) hold verbatim with the θ-run Θ replaced by a P-epoch Π, M_Θ by M_Π and
Mopt_Θ by Mopt_Π.
Proof. Go through the uses of "θ constant" in P-N5-PFZ §1-§4.
- §1 FB-ROUND does not use θ at all.
- §2 (b) uses θ only in M_t(o) = wt(P(θ_t)) = M_Θ(o), which holds on Π by the definition of a P-epoch.
- §2 (a)'s base uses M_t(z) = M_Θ(z) for terminals z, again only M_t(o) = wt(P(θ_t)).
- §2 (c) is (a) + (b).
- §3 LEN-TAIL uses P-FREEZE (c) and R15 (a). o ∈ U may itself make a length rise (a θ-change inside Π); it is a U-rise like any other.
- §4 NO-CROSS-A uses the route form and SEP-o at each single H1 state s, with θ_s at that state, and P-FREEZE (c). No constancy of θ
  enters. □

## 2. Lemma θ-LEN (PROVED, L-NEW succ. 18)
Statement. A P-epoch Π has at most max(|U| − 2, 0) θ-changes.
Proof.
- If o = c_θ, then θ = (c_θ, ∅, 0) is constant.
- Otherwise θ = (c_θ, P, ℓ) with c_θ (a phase constant) and P (constant on Π) fixed. So θ's order on Π is the order of ℓ in the
  direction s_θ (P-N5-PFZ §3), and θ is monotone (R15 (a)). Each θ-change therefore moves ℓ strictly in one direction.
- ℓ(θ) is the length of o's honest play to c_θ, a simple path in U (P-N5-PFZ §2 (b)) of ≥ 1 edge. So ℓ ∈ [1, |U| − 1], and at most
  |U| − 2 strict moves fit. □

## 3. Theorem BRK-POLY′ (PROVED, L-NEW succ. 18; 𝒞^1O)
Statement. For every HN stretch S of a phase, for any τ(o) and any c_w:
- (i) θ_S ≤ (ρ_S + 1)·max(|U| − 2, 0);
- (ii) B_S ≤ θ_S + (ρ_S + 1)(|U| − 1 + |U|(|U| − 1)) ≤ (ρ_S + 1)(|U|² + |U| − 3) ≤ (ρ_S + 1)(2n² − 1);
- (iii) in case A, B_S ≤ θ_S + (ρ_S + 1)(|U| − 1) ≤ (ρ_S + 1)(2n − 3) (for |U| ≥ 2; B_S = 0 if |U| = 1, as then o = c_θ and H1 fails).
Proof.
- (i) S meets at most ρ_S + 1 P-epochs; apply θ-LEN to each.
- (ii), (iii). Take the windows [a, k] of the breaks and their kinds as in P-N5-PFZ §6 (RISE′, P-N5-PFZ §5).
  - Kind 1 (a θ-change in [a+1, k]): ≤ θ_S, since windows are disjoint.
  - Kind 2 (θ constant on [a, t+1], an R̄-rise at t → t+1): a, …, t+1 lie in one θ-run, hence in one P-epoch Π, and the eviction
    a → a+1 is a fallback transition f_j of Π.
    - j ≤ |U| − 1: ≤ |U| − 1 per P-epoch (distinct evictions).
    - j ≥ |U|: t > f_{|U|−1}, so by LEN-TAIL′ (§1) ≤ |U|(|U| − 1) per P-epoch. In case A there are none (NO-CROSS-A′, as in P-N5-PFZ §6).
  - Sum over the ≤ ρ_S + 1 P-epochs and use (i) for θ_S. |U| ≤ n. □
- Consequence (PROVED, with RESULTS R39 (b) EPOCH). Crossings and fallbacks per HN stretch are O(n³·K·(ρ_S + 1)): polynomial in n and
  ρ_S, for every τ(o) and every c_w. The residual for HN stretches is ρ (P(θ)-changes): strict increases of θ's path set, not of its
  length.

## 4. Not to sign (OPEN)
- ρ per phase. Not bounded here. PF-THETA's linear form is FALSE (experiments/red/so/instances/pftheta_cex_n32.pg); a polynomial form
  for θ-changes or for P(θ)-changes is OPEN.
- W-TIE steps (working doc §4). OPEN.
- HN stretches per phase for τ(o) ≠ o, OTHER states, and S4a steps between fallbacks: OPEN, as in P-N5-PFZ §7.

## 5. Data (DATA; which hypotheses occur)
Scripts experiments/new/box39/pfreeze.py and pfzdata.py, both with env PFZ_KEY=P (P-epochs). Instances as in P-N5-PFZ §8 (library 270
𝒞^1O files, box-37/38 instances; pfreeze.py also box-39 climb outputs). Canonical start.
- pfreeze.py: 872 P-epochs with > 1 state, 4,749 transitions, 704 fallbacks.
  - FB-ROUND failures 0. Freeze failures (a P-change on U after the (|U| − 1)-th fallback of a P-epoch) 0.
  - θ-LEN failures (θ-changes > |U| in a P-epoch) 0. Post-freeze crossings 0, breaks 0.
  - Max θ-changes in one P-epoch: 11 (pftheta_cex_n32.pg, n 32, |U| 32).
- pfzdata.py: 857 P-epochs; 288 of them contain θ-changes (520 θ-changes in all, every one length-only by definition). θ-LEN checked
  against max(|U| − 2, 0): 0 failures. θ-LEN is exercised; it is not vacuous.
  - FB-ROUND: case 1 69,178, case 2 1,939, failures 0.
  - P-FREEZE′ (a) direct checks (|U| ≤ 18): 3,865, failures 0.
  - Post-freeze regime: as in P-N5-PFZ §8. Only 10 P-epochs reach |U| − 1 fallbacks, all with |U| = 1, so LEN-TAIL′ and NO-CROSS-A′ are
    exercised only trivially.
  - BRK-POLY′ charging: 15 breaks; kind 1: 10; kind 2 early: 5; kind 2 post-freeze: 0.
