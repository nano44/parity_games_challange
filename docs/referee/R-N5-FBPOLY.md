# R-N5-FBPOLY: REFEREE report on packet P-N5-FBPOLY (box 41: κ-FB-ROUND, κ-HAT-FREEZE, κ-PFZ, κ-Y-FORM, EXIT-SWITCH, FREEZE-EXIT, CN-ONLY, THETA-AFTER, Theorem FB-POLY)
Referee: REFEREE (successor 10, session_01J4kmfDqtZdanh3RSCxChyD), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: the Lead's message of 18:51Z (Lead's stamp): after NEEDB; "the most consequential packet in the queue ... check it with
  special care".
- Object: docs/new/P-N5-FBPOLY-box41.md at trunk 42d8c3a9, sha1 de244dcd3592b04eca2080a0efe10a7c0b2e5301 (checked with
  `git show 42d8c3a9:docs/new/P-N5-FBPOLY-box41.md | sha1sum`; identical on my tree), 288 lines. Author: L-NEW successor 20.
- Written 2026-10-25T18:57Z-19:46Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: I did not read any docs/referee-2/R2-N5-FBPOLY* file. D1: each statement treated as wrong until its proof was
  checked line by line. Tools: own engine (scratch/rl_engine.py), new probe scratch/fbpoly_probe.py and climb scratch/fbpoly_climb.py;
  no lane code (fbpoly.py not run).
- Premises re-read in their landed text: FBL-N (ii) (P-N5-X §3 l. 78: "every gate edge (x, z) with x ∈ F_k is flat for W_k: x = λ_W(x),
  and λ_W(z) = x"; RESULTS R21 (c)); CN-LAST (RESULTS R38 (f)); (V1), R15 (a), Lemma S (a), G (a), KEY; SPEC S1, S2, S4c (FIX 3).

## Verdicts
| § | statement | label | verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| §0.3 | facts (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (HP), (SP′), (YB) | used | checked (note FBP-N2 on (YB)) |
| §1 | Lemma κ-FB-ROUND | PROVED | SIGNED |
| §1 | Lemma κ-HAT-FREEZE (a)-(c) | PROVED | SIGNED |
| §1 | Lemma κ-PFZ | PROVED | SIGNED |
| §1 | Lemma κ-Y-FORM | PROVED | SIGNED |
| §2 | Lemma EXIT-SWITCH | PROVED | SIGNED |
| §3 | Lemma FREEZE-EXIT | PROVED | SIGNED |
| §4 | Lemma CN-ONLY | PROVED | SIGNED |
| §5 | Lemma THETA-AFTER | PROVED | SIGNED |
| §6 | Theorem FB-POLY (a) first bound f ≤ 1 + (|U| − 2)(deg_U(o) + |U|) | PROVED | SIGNED |
| §6 | Theorem FB-POLY (a) final bound ≤ 1 + (n − 2)(2n − 1) | PROVED | SIGNED WITH GAP FBP-1 (one line; repair below; the bound is true) |
| §6 | Theorem FB-POLY (b) | PROVED | SIGNED WITH GAP FBP-2 (the proof covers only o ≠ c_θ; repair below; the statement is true) |
| §6 | Theorem FB-POLY (c), (d) | PROVED | SIGNED |
| §7, §8; §6 Remarks | FB-CAP, (FB-CAP-1), (FB-CAP-2), data, readings | not to sign | not signed |
- No (P). No hypothesis on H1, H2, H3, τ(o), c_w or N_HN, as claimed. The phase, 𝒞^1O and SPEC S4c are used.
- Landed premises only: (V1), R15 (a), R18 (d) Lemma S (a), R19 (a), R21 (c) FBL-N (ii), R38 (a), (f). The PFZ / RHO items are
  re-proved here in κ form, so the packet does not depend on those two packets' landing. I checked the re-proofs (§1).
- Two gaps, FBP-1 and FBP-2, both in the final bookkeeping of §6, both closed by the repairs below. Notes FBP-N1..N4.
- UNTESTED BY DATA (lesson N-ENT-2; my data, §8): the regime of FREEZE-EXIT and THETA-AFTER (a fallback g_j with j ≥ |U| − 1 at
  |U| ≥ 3, o ≠ c_θ). It is NOT reached in my
  data either. My climbs (3.82M candidates) plateau one fallback short (f = |U| − 2 at |U| ≥ 3). So FREEZE-EXIT, THETA-AFTER and FB-POLY (a)
  beyond |U| − 2 fallbacks rest on their proofs, which I checked line by line. The lemmas under them (κ-HAT-FREEZE, κ-PFZ, EXIT-SWITCH,
  CN-ONLY) are exercised millions of times with 0 failures (§8).

## 1. The κ-freeze lemmas: checked
- (Aκ) is (A) with the length coordinate. (V1) adds 1 to ℓ, also when next(z) = c_θ (ℓ(c_θ) = 0) and when z lies on c_θ's cycle (z ≠ c_θ).
  (M1κ) is S1 with equal rewards. (M2κ) is R15 (a) through (M1κ).
- κ-FB-ROUND is FB-ROUND (signed by both referees in P-N5-PFZ) with κ. The second case uses S4c's choice: x* maximises (Ξ_k(w), w) over the
  gate targets, so Ξ_k(x*) ⊵ Ξ_k(x). x*, x ∈ U at k, so (M1κ) applies. Correct.
- κ-HAT-FREEZE: the induction of HAT-FREEZE (signed in R-N5-RHO §2), coordinatewise in κ. (b) sums κwt over q ∖ {c_θ}: the length
  coordinate is |q| − 1 edges, which is ℓ(Ξ_t z). Correct.
- κ-PFZ:
  - Base z = o.
  - Odd step: (Aκ) at t.
  - Even step: the hypothesis at k = f^Θ_j uses κ_k(o) = κ(θ_Θ), which holds because k ∈ Θ. κ-FB-ROUND at k, then (M2κ) from k + 1 ∈ Θ
    to t. (k + 1 ∈ Θ because k < k + 1 ≤ t and Θ is a run of consecutive states.)
  - x = o is the 0-edge base; x = c_θ is not a vertex of G_U^o.
  - Correct.
- κ-Y-FORM is Y-FORM (signed in R-N5-RHO §1) in κ. κ(o ⊕ Ξ_t y) = κwt(o) + κ_t(y), because o ∉ P(Ξ_t y) and the length is + 1. Correct.

## 2. EXIT-SWITCH: checked
- Steps outside S_U ∪ T agree at k and k + 1. Even vertices keep σ, since S4c changes only gate sources, and the Odd vertices ≠ o are
  forced. For w ∈ S_U, x*_w ∈ U by (Aκ) at k + 1, using λ_{k+1}(w) = c_θ ≠ w (in-phase).
- The contradiction:
  - Suppose every u ∈ S_U has its honest k-play from x*_u visit u before T. Every such play does visit T: c_θ by (SP′), or x*_u ∈ T.
  - So the first vertex of S_U ∪ T on it lies in S_U, and x*_u ∉ T.
  - The k + 1-play from v ∈ S_U therefore moves from S_U-vertex to S_U-vertex along unchanged steps, never meeting T. That contradicts
    (SP′) at k + 1.
  - The argument needs the k + 1-play to stay in U, which (Aκ) at k + 1 gives (U is a phase constant).
  - Correct.
- For the chosen u, the k-play from x*_u up to its first T-vertex e is simple ((SP′); the lasso argument) and avoids u, so p_u is simple.
  It lies in G_Û (e = c_θ) or G_U^o (e = o): u → x*_u is an Even edge into U ∖ {the other terminal}, and the remaining steps are σ_k-edges
  or forced edges inside U ∖ T. The κ identity is (Aκ) along the play. Correct.

## 3. FREEZE-EXIT: checked
- Both graphs have |U| − 1 vertices, so p_u has ≤ |U| − 2 edges. u switched through a gate, so κ_k(x*_u) > κ_k(σ_k u) ((M1κ), both in U).
- e = c_θ: k = g_j > g_{|U|−2}, so κ-HAT-FREEZE (a) applies at the state k with p_u. This gives κ_k(u) ≥ κwt(u) + κ_k(x*_u), using
  κ_k(c_θ) = (0, 0).
- e = o: k = f^Θ_i > f^Θ_{|U|−2}, with k ∈ Θ. κ-PFZ at the state k gives the same inequality, now with + κ_k(o).
- Then (Aκ) at u (next_k(u) = σ_k(u)) gives κ_k(σ_k u) ≥ κ_k(x*_u): a contradiction. Correct.
- The proof shows more than the statement. At a fallback with j ≥ |U| − 1, no switched u ∈ U ∖ T is of kind c_θ. At the i-th
  fallback of a θ-run with i ≥ |U| − 1, none is of kind o. This per-vertex form is what my probe checks (FE, §8).

## 4. CN-ONLY: checked
- (1):
  - A switched y ∉ U has an honest play that never visits o ((HP) (ii), contrapositive). So y ∈ F_k ((HP) (i)).
  - FBL-N (ii) (Even fallback, τ unchanged) gives y = λ_W(y), and G (a) gives λ_W = λ_k off R̄.
  - y = c_θ is a cycle node, and o is Odd. Correct.
- (2), the four sub-cases:
  - σ_k(y) lies on y's own honest cycle, topped by y, so P = ∅.
  - For y ≠ c_θ, λ_k^{-1}(y) ⊆ F_k ∖ U, and its non-cycle-node vertices have no gate (FBL-N (ii) again), so they do not switch. The
    k + 1-play from x*_y repeats the k-play to y. y tops the new cycle, so P(Ξ_k x*_y) = ∅.
  - For y = c_θ with the play meeting c_θ first, the same argument works inside U ∖ T (S_U = ∅).
  - For y = c_θ with the play meeting o first, π ∪ {o} lies on c_θ's honest cycle at k + 1. So:
    - ¬H1 at k + 1, M_{k+1}(o) = 0 (YB), and wt = 0 on π;
    - M_k(x*_y) = M_k(o) ≤ M_{k+1}(o) = 0;
    - the gate gives ≥ 0;
    - hence P = ∅ (INJ).
  - Correct.
- (3): the sandwich Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ Ξ_k(x*_y) (S4c picks the maximum), reward injectivity, and (INJ). So every gate has level −1
  and a cycle-node tail. CN-LAST applies, and k + 1 is the phase's last state. At most one per phase. Correct.

## 5. THETA-AFTER: checked
- κ(o) is non-decreasing on the phase (M2κ) and determines θ (fixed cycle node, (INJ), ℓ).
- Past g_{|U|−2}:
  - H1 states take values in V_H (κ-Y-FORM, κ-HAT-FREEZE (c) on Y_t ⊆ F_t ∩ U);
  - ¬H1 states take values in V_N ((YB), o ≠ c_θ).
- So there are ≤ |V_H| + |U| − 2 changes, and the θ-runs meeting those states number at most one more. Correct.
- FBP-N1 (precision, feeds FBP-1): V_H ranges over y with κoptÛ(y) defined, i.e. y ∈ Û = U ∖ {o}. So |V_H| ≤ |succ(o) ∩ Û| ≤ |U| − 1,
  which can be smaller than deg_U(o) = |succ(o) ∩ U| when o has a self-loop. The stated bound holds either way.

## 6. FB-POLY: checked, with GAPS FBP-1 and FBP-2
- (a), first bound:
  - The split is exhaustive: S_U = ∅ (≤ 1, CN-ONLY); S_U ≠ ∅ with j ≤ |U| − 2; S_U ≠ ∅ with j ≥ |U| − 1.
  - In the last class, FREEZE-EXIT's contrapositive gives i ≤ |U| − 2 in its θ-run, and that θ-run contains the state g_j > g_{|U|−2}.
    THETA-AFTER's hypothesis holds, since there are ≥ |U| − 1 fallbacks. So there are at most deg_U(o) + |U| − 1 such θ-runs, each with
    ≤ |U| − 2 qualifying fallbacks.
  - The sum is 1 + (|U| − 2)(deg_U(o) + |U|). Correct.
- **GAP FBP-1** (the final bound in (a)):
  - "deg_U(o) ≤ n − 1" is false when o has a self-loop and succ(o) ⊇ U = V. Then deg_U(o) = n, and 1 + (|U| − 2)(deg_U(o) + |U|) =
    1 + (n − 2)·2n > 1 + (n − 2)(2n − 1).
  - Repair (one line): by FBP-N1, THETA-AFTER holds with |succ(o) ∩ Û| ≤ n − 1 in place of deg_U(o). So f ≤ 1 + (|U| − 2)(|succ(o) ∩ Û|
    + |U|) ≤ 1 + (n − 2)(2n − 1). Alternatively, state the final bound as 1 + 2n(n − 2).
  - The polynomial conclusion is unaffected.
- **GAP FBP-2** ((b)):
  - The proof "U = {o, c_θ}" assumes o ≠ c_θ. If o = c_θ and |U| = 2, then U = {o, v}, U ∖ T = {v}, and (c) gives only f ≤ 2.
  - Repair (the statement is true):
    - At any state of the phase, next(v) ∈ U = {o, v} (Aκ), and next(v) ≠ v, because a self-loop would make v its own cycle node, while
      λ(v) = o.
    - So next(v) = o at every state. A switched Even v would need x*_v ∈ U ∖ {σ_k(v)} = {v} (Aκ at k + 1), which is impossible for the
      same reason.
    - So S_U = ∅ at every fallback, and (d) gives f ≤ 1.
  - Alternatively, restrict (b) to o ≠ c_θ: then it is (a) with |U| = 2.
  - Data: phases with o = c_θ and |U| = 2: 4 (library) and 19 (library with random starts); f ≤ 1 in all of them, 0 failures.
- (c):
  - T = {o}, and θ = (o, ∅, 0) throughout, so there is one θ-run.
  - EXIT-SWITCH works with T = {o}: (SP′) needs only "the play visits c_θ = o".
  - κ-PFZ works in G_U with κ(θ) = (0, 0), and paths have ≤ |U| − 1 edges.
  - So the i-th fallback with i ≥ |U| has S_U = ∅. That leaves ≤ |U| − 1 fallbacks with S_U ≠ ∅, plus ≤ 1. Correct.
- (d) is CN-ONLY.
- FBP-N2 (wording): §0.3 (SP′) states simplicity "up to the first visit of T". (YB) uses it from z = o ∈ T, where that prefix is trivial.
  The lasso argument in (SP′)'s proof does give "o's honest path to c_θ is simple", which is what (YB) needs. Say so.
- FBP-N3 (scope, agreeing with the packet): FB-POLY bounds f per phase only. The consequences in the Remarks (f removed from SCOPE-COUNT,
  EPOCH and X-SN-PHASE) are READINGS for the Lead and not signed here. G-N5-TIME stays OPEN.

## 7. Not signed
- §7: CONJECTURE FB-CAP (open for |U| ≥ 3; my data: f − max(1, |U| − 2) ≤ 0 in every phase with |U| ≥ 3, and the
  climbs aimed at f ≥ |U| − 1 found none), (FB-CAP-1), (FB-CAP-2), and the EXIT-SWITCH sub-question.
  §8 data. §6 Remarks.
- Nothing here is a running-time bound for N5, a TARGET.md claim or a step-4 pass.

## 8. Data (DATA, not proof)
Tools: docs/referee/scratch/fbpoly_probe.py, fbpoly_climb.py (own code on rl_engine; checks listed in the probe header). Logs:
docs/referee/scratch/fbpoly_logs/.
- (L) P-N5-RHO's 412-file list (253 𝒞^1O), SPEC S3's start (fbpoly_logs/lib.log):
  - 990 phases, 660 fallbacks: 21 with S_U = ∅, 639 with S_U ≠ ∅.
  - Switched vertices of U ∖ T by kind: c_θ-first 1,509, o-first 28, loop 0.
  - κ-HAT-FREEZE (a) 531 exact checks; κ-PFZ 331; max f per phase 33 (experiments/si/xing/instances/ccl_w48_n48.pg, |U| 48).
  - 0 failures.
  - These are exactly the packet's §8 (L) figures (660 / 21 / 639 / 1,509 / 28 / 0 / KH 531; my κ-PFZ count differs from its 395 by the
    counting convention: I check per θ-run only for j ≤ min(#fallbacks of the run, |U| − 2)).
- (L) with 4 random start pairs per game (1,012 extra runs; fbpoly_logs/lib_rand4.log):
  - 5,240 phases, 1,313 fallbacks: S_U = ∅ 89 (CN-ONLY, each followed by the phase's last state), S_U ≠ ∅ 1,224.
  - Kinds: c_θ-first 2,596, o-first 39, loop 0.
  - KH 1,060, KHC 20, KP 687. THETA-AFTER in 135 phases (10 with |U| ≥ 3), max 0 θ-changes after the freeze.
  - 0 failures.
- Named: ccl_w48_n48.pg, beta2_n11.pg and experiments/new/box40/out/*.pg: 45 fallbacks, f_max 33, 0 failures.
- Climbs (fbpoly_climb.py, 45 min each; score f − (|U| − 1) over phases with o ≠ c_θ and |U| ≥ 3; seeds rhc_rhc_oneodd_c16_2_5.pg (21),
  rhc_pure_22_6.pg (22), beta2_n11.pg (23); fbpoly_logs/climb_{21,22,23}.log):
  - 3,822,173 candidates; 2,815,066 of them at score ≥ −1 were fully checked.
  - CN-ONLY 2,815,066 cases, κ-HAT-FREEZE (a) 4,646,931, κ-HAT-FREEZE (c) 3,140,099, κ-PFZ 1,197,169 exact checks; THETA-AFTER in
    2,815,066 phases with |U| ≥ 3.
  - 0 failures.
  - Best score −1 in all three: no phase with a fallback g_j, j ≥ |U| − 1, at |U| ≥ 3. FREEZE-EXIT's and THETA-AFTER's regime and an FB-CAP
    violation are not reached.
- FBP-N4 (data): the per-vertex form of FREEZE-EXIT (no c_θ-kind switch at j ≥ |U| − 1; no o-kind switch at i ≥ |U| − 1) held at every
  switched vertex. Its hypotheses never occur, so this adds nothing beyond the proof. EXIT-SWITCH's "loop" kind never occurs (0 of
  2,635 switched vertices of U ∖ T in the (L)+random-starts run, which includes the canonical runs).
