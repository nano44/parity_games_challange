# R87: Lemma N3-LEVEL (P-N5-FLIP-box18 §6) attacked with an exact checker: no violation, proof re-derived, one PROVED corollary (N3-CHAIN), and why a ruler-pattern N3 family is the long-phase problem (L-RED successor 21, box 54; Lead GO 11:58Z; written 12:26Z, date -u)
Target: L-SI successor 14's Lemma N3-LEVEL in docs/si/P-N5-FLIP-box18.md (trunk d67fdb87, sha1 96a7e088 re-measured), and its READING
(§7, note §25): N3 flips of a pair are bounded by a ruler count above rank(top(C)), so a super-polynomial N3 family needs relay cycles
with LOW tops and high-level path-set changes reused in a ruler pattern. Labels per L40: PROVED (lane, unrefereed), DATA, READING.
Every game. Nothing here bounds N5. Not a TARGET.md claim. G-N5-TIME stays open.

## 0. Result
- **No kill.** 0 violations of N3-LEVEL, FLIP-COST (a) and the premise (SG) over every check below.
- The proof (§6, four cases h = q1, h ∈ p2, h ∈ p1, h = q2) was re-derived step by step. No gap found. The two places that need care
  both hold: (i) the honest play of a class vertex stays in U_c, so "first vertex of Q" (flipck) = "first vertex of Q_c ∪ {c}"
  (packet); (ii) in the h ∈ p1 and h = q2 cases, (SG) at q1 with cycle node c fixed makes weight(P(Ξ_{t2} q1)) > weight(P(Ξ_{t1} q1)),
  and ranks are injective (si.Engine: rank by (prio, v)), so the top differing rank decides; L′ = rank(h) with h even contradicts it.
- **Coverage gap closed.** L-SI's flipck.py N3LEV_V tests only flips with BOTH paths intact at BOTH times (and only the latest t1). The
  lemma claims more: p1 may be broken, and p2 must be intact at t1 only when h ∈ p2. My checker tests the frozen statement exactly.
- **PROVED corollary N3-CHAIN** (§2): time-disjoint N3 flips of one pair with tops at rank ≥ r number at most 2^{a_r} − 1. This is §7's
  READING made exact; it is polynomial only when a_r = O(log n).
- **READING** (§3): the "low tops" half of the counterexample shape already exists (mkpp: class top − rank(h) = 25 at K 12, 61 at K 48),
  and level reuse at a single Odd vertex inside one phase already exists (pftheta34, 𝒞^1O, RUND §20). What no known instance has is a
  phase much longer than n. So a super-polynomial N3 family is exactly a super-polynomial phase: target (1), R83 §2 routes (i)-(iii).

## 1. Checker and data (experiments/red/n3/; DATA)
- n3x.py (written from §1 and §6, not from flipck): phase = maximal run with (λ_Ξ, τ) constant; for each class c and q ∈ Q_c, the class
  exit path of σ̄_s(q)'s honest play up to Q_c ∪ {c}; EVERY flip (q1, q2, t1 < t2), every t1. Hypotheses: p1 ∩ p2 = ∅; h = top of
  C = q1·p1·q2·p2 has rank(h) > rank(c) and h even; h ∈ p2 ⇒ p2 intact at t1. Conclusion lev ≥ rank(h). Also FLIP-COST (a) at every
  flip and (SG) at every vertex of every in-phase transition. Trace = n5x.step (SPEC S1-S5; n5x.trace asserts equality with n5.run).
  MUT=1 demands lev > rank(h) (control).

| set | games | flips | hyp. hold | of which NOT both-intact (flipck never checks) | lev = rank(h) | violations |
| --- | --- | --- | --- | --- | --- | --- |
| pp_K12_n161 (R83 pin) | 1 | 60 | 60 | 0 | 0 | 0 |
| pp_K48_n449 (R83 pin) | 1 | 672 | 672 | 0 | 0 | 0 |
| leanT_N6, RS = 4 | 1 | 5 | 5 | 0 | 4 | 0 (MUT=1: 3 FAIL, as L-SI's control) |
| lib41 (experiments/new/box41/lib41.txt, n ≤ 64, S3 + RS 4) | 367 | 1,115 | 20 | 3 | 10 | 0 |
| random n 12-32, half random starts (n3rand.py seeds 11, 12; 20 min each) | 1,636,684 | 2,048 | 1,019 | 591 | 565 | 0 |
| climb (n3climb.py seed 2, from leanT_N6, 15 min) → n3cov_lean | 1 | 1,209 | 1,209 | 287 | 314 | 0 |
| climb (seed 3, from phi_flat_alive_n32) → n3cov_phi | 1 | 1,626 | 1,626 | 137 | 85 | 0 |
- (SG): 0 violations over 7.87 M vertex-transition checks. FLIP-COST: 0 over all 6,735 flips.
- Most lib41 flips (969 of 1,115) fail the hypothesis "top even and above c": by FLIP (b)/(c) these are N1 (p1 broken) or N2 flips.
- Climb fitness: (violations, #hyp flips not both-intact (capped 20), −min slack lev − rank(h)). Both climbs reached slack 0 within a
  minute and stayed there for 40-47 k evaluations: equality is common, a violation never appeared.
- Pins (experiments/red/n3/instances/; with .start = start pair):

| file | sha1 (.pg) | .start sha1 | n | iterations / fallbacks | Oink zlk |
| --- | --- | --- | --- | --- | --- |
| n3cov_lean.pg | bcf8dbf64cba48123dc7da849b179793257e13e1 | 9d3ab487 | 32 | 35 / 1 | exit 0 |
| n3cov_phi.pg | 50d416db9a5e4227681640e3871824e0476f09a2 | 0ee71ae7 | 48 | 31 / 3 | exit 0 |
  These are coverage pins (no kill), so no strategy cross-check is claimed beyond Oink solving them. experiments/red/check.sh pins
  hyp = 60 on pp_K12, PASS on n3cov_lean, and FAIL of the strict control on n3cov_lean.

## 2. Corollary N3-CHAIN (PROVED, lane, unrefereed; every game; P1, (SG) and N3-LEVEL as in the packet)
Statement. Fix a phase, a class c, a pair (q1, q2) and a rank r. Let (q1, q2, t1^i, t2^i), i = 1..m, be flips that satisfy N3-LEVEL's
hypotheses, with rank(h_i) ≥ r, and t1^1 < t2^1 ≤ t1^2 < t2^2 ≤ … ≤ t1^m < t2^m. Let a_r := #{v ∈ U_c : rank(v) ≥ r, rank(v) > rank(c)}.
Then m ≤ 2^{a_r} − 1.
Proof. Write X_s := P(Ξ_s q2) ⊆ U_c and π(X) := {v ∈ X : rank(v) ≥ r}.
- (monotone projection) By (SG) at q2, with q2's cycle node c fixed in the phase, the first κ component gives weight(X_s) ≤ weight(X_{s′})
  for s < s′, and distinct sets have distinct weights (injective ranks). If X_s ≠ X_{s′}, let L be their top differing rank. If L ≥ r,
  π(X_s), π(X_{s′}) differ with the same top difference L, so weight(π X_s) < weight(π X_{s′}). If L < r, the projections are equal.
  So s ↦ π(X_s) is non-decreasing in the weight order.
- (strict at each flip) N3-LEVEL gives lev_i ≥ rank(h_i) ≥ r, so X_{t1^i} and X_{t2^i} differ at a rank ≥ r: π(X_{t1^i}) < π(X_{t2^i}).
- So π(X_{t1^1}) < π(X_{t2^1}) ≤ π(X_{t1^2}) < … < π(X_{t2^m}): at least m + 1 distinct subsets of an a_r-element set, m + 1 ≤ 2^{a_r}. □
- Remark. Polynomial when a_r = O(log n) (the packet's "tops near the class top"). On mkpp the bound is 2^{26} at K 12 (h rank 135,
  class top 160) while each pair flips about K/2 times: the bound is far from the data there, because mkpp never reuses a level (§3).

## 3. Why the counterexample shape reduces to a long phase (READING)
- Each N3 flip changes Ξ(q2), so flips of a pair ≤ ρ_{q2} ≤ T, the phase length. A super-polynomial N3 family needs T super-polynomial.
- Data on the shape:
  - LOW tops: present. mkpp's flips (n3x -v on pp_K12): h has rank 135, class top 160; levels lev = 141, 143, …, 151 on q2 = 160 and
    142, …, 150 on q2 = 159, one fresh content level C_j per flip. At K 48 the gap is 61.
  - Level REUSE at one vertex in one phase: present. pftheta34_n32 (𝒞^1O; RUND §20): gate 0's path-set levels 28, 25, 24, 31, 25, 27,
    25, 24, 28, 29.
  - Long phases: absent. Longest phase / n (phlen.py): pftheta34 35/32 = 1.09; xsn29_n32 29/32 = 0.91; mkpp ≈ n/8; mkgate ≈ n/8.
- So the N3 view adds no new obstruction and no new route: ruler reuse is cheap, low tops are cheap, and the whole difficulty is a phase
  of length ω(n), which by R83 §2 needs (i) super-polynomially many unforbid-switches per run, (ii) many runs per phase, or (iii) many
  tie / length-only switches. This is target (1). Next: phase-length climbs (phclimb.py, running) and the release-without-content core.

## 4. Tools
- n3x.py (checker), n3rand.py (random search), n3climb.py (climber), phlen.py (longest phase), phclimb.py (long-phase climber).
- Logs (summaries) in experiments/red/n3/out/.
