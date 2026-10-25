# R2-N5-NEB: second-referee check of packet P-N5-NEB (L-NEW box 38: RISE, HIGH-RISE, NO-ENTRY-A′, CASE-B-LEN′, LOW-RISE′, Theorem BRK, Corollary OUT-1). REFEREE-2 (successor 9), written 2026-10-25 14:4xZ-15:06Z (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-NEB (Lead queue 14:03Z by the Lead's stamp). Object docs/new/P-N5-NEB-box38.md, sha1
ba15e51fb02471207b11ecd64e9687a23fe8a744. I checked the sha1 three ways: `git show 314d220:<file> | sha1sum`,
`git show origin/claude/l-new:<file> | sha1sum`, and on my tree. All three agree. The pin is trunk 314d220. The file has one commit,
8ca35711.
Background read:
- P-N5-OUT and my R2-N5-OUT (SPLIT, F-FLAT, EPOCH, NE-COUNT (c), now signed by both referees; the fixes file
  docs/new/P-N5-OUT-fixes-box37.md, whose §1 points at NEB §3-§4);
- RESULTS R15, R17 (a), R21 (a), (c), R23 (a), (b), R34 (e); P-N5-SCOPE KEY, FB-INT;
- the box-38 working notes N5-NEB-box38.md §Summary/§1 and N5-TAUW-box38.md lines 1-40 (read for R2-N5-OUT §7).
Independence:
- I read nothing in docs/referee/ about this packet; `ls docs/referee | grep -i neb` is empty on my tree.
- No lane script (inv2.py, lowrise.py, statesamp.py, …) was run or imported.
- Lane .pg files are inputs only.
Tools: docs/referee-2/R2-N5-NEB/ (own code on R2-N5-OUT/out_check.py):
- neb_check.py: the checks, plus mode chain;
- neb_climb.py: the climbs;
- files.lst, run_all.sh, run_climbs.sh, totals.py, logs/, climb/, totals_logs.txt, totals_climb.txt.
Traces: own / rand / spec, as in R2-N5-OUT; every count names its trace. Every game asserts exactly one Odd vertex with out-degree > 1.
Labels: PROVED (L-NEW succ. 17). Nothing here is a running-time bound, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN, and
θ-changes are a parameter.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §0 chain rule (filled in) | correct | Re-proved in §1 below. Checked on 187,474 (batch) + 93,808 (test) random strict triples, 0 failures |
| §1 Lemma RISE | SIGN | — |
| §2 Lemma HIGH-RISE | SIGN | — |
| §3 Theorem NO-ENTRY-A′ | SIGN | N-NEB-1 (citation, = N-OUT-2 / OUT-R1, already forwarded by the OUT fixes file §1): BASE (ii) ends "against Step (K)", which R23 (a) states "inside a phase", and a + 1 may leave S. FBL-N (i) + F1 is what is used. Case 1′ (v on C_W, new here) is checked line by line in §3 |
| §4 Lemma CASE-B-LEN′ | SIGN | N-NEB-1 likewise |
| §5 Lemma LOW-RISE′ | SIGN | N-NEB-2 (precision, optional): the proof of (b) does not use (i) at t+1, so (b) holds even at the first failure of (i). BRK uses (b) only at states where (i) holds, so nothing depends on this |
| §6 Theorem BRK (a)-(d) | SIGN | — |
| §7 Corollary OUT-1 | SIGN | Arithmetic checked: D(θ_S + 1) − 1 = θ_S + (n − 2)²(θ_S + 1) |
| §8 | not signed (as briefed) | The FALSE records reproduce on my traces (R2-N5-OUT §7, §C.4): nebc_cex_n14 and tauw_A/B_cex_n24 |
N-NEB-3 (status): the dependency rows SPLIT, F-FLAT, EPOCH and NE-COUNT (c) read "IN REVIEW". P-N5-OUT is now signed by both referees
(REFEREE fa08687 + §C a8b8ef3; REFEREE-2 dfcaae67 + §C 2a9e8db0), with fixes file 640a5db2.
No statement is NOT SIGNED, and no gap is open. No counterexample turned up in 66,655 batch runs or in 501,892 climb runs (4 climbs).

## 1. §0: the chain rule and the equivalences
- Chain rule for x ◁ y ◁ w.
  - If either level is ∞: rewards increase weakly along the chain and strictly at an ∞ step, so the cycle nodes of x and w differ, and
    lev(x, w) = ∞.
  - Both finite and different, ℓ1 > ℓ2: x and w agree above ℓ1 and differ at ℓ1 (y agrees with w there). ℓ1 = −1 cannot occur with
    ℓ2 < ℓ1.
  - Both equal to a vertex rank: y would hold u exactly when x and w do not. Both steps are then decided at u in Even's favour, which
    forces opposite memberships. Impossible.
  - Both −1: the lengths move monotonically, so x and w differ in length only.
  - So lev(x, w) = max. ✓
- ≡_B (threshold 0) means the same cycle node and the same P. (T1)-(T3) hold verbatim, since the comparison above level −1 sees only
  (c, P). ✓
- Route form, SEP-o (independent of τ(o)), and "F-values avoid R̄": as in R2-N5-OUT §5. ✓
- (iii+): x = λ_W(o) ∈ C_W ⊆ R̄. ✓

## 2. Lemma RISE and Lemma HIGH-RISE: SIGN
- No entry on [a, t+1]: no F → R̄ gate at a..t, every switched edge is a gate, and ACT (i) applies. ✓
- (★) for the gate (y, z) at t+1, with q = σ_{t+1}(y):
  - y ∈ F_t: (y, z) is not a gate at t, since z ≠ σ_t(y) ∈ F_t. So Ξ_t(z) ⊴ Ξ_t(σ_t y) ⊴ Ξ_t(q) ⊴ Ξ_{t+1}(q).
  - y ∈ R_t: SPLIT (a) makes t → t+1 a fallback (t, t+1 ∈ S, HN at t). Either Ξ_t(z) ⊴ Ξ_t(σ_t y), or (y, z) is a gate at t and S4c's
    choice gives Ξ_t(q) ⊵ Ξ_t(z).
  - The split y ∈ F_t ∪ R_t is complete: F_t ⊆ F_{t+1}, and y ≠ o.
  - θ constant gives z ≠ o. ✓
- HIGH-RISE: both steps of (★) separate o's membership (SEP-o at t and at t+1), so each has level ≥ rank(o). The chain rule takes the
  max. ✓
- The proof works for every F → R̄ gate at t+1, not just one. My checker tests all of them.

## 3. Theorem NO-ENTRY-A′: SIGN
- W at a.
  - c_w = o under ¬H2 gives w = (o, ∅, 0).
  - XW, c_θ ≠ o and case A give Ω(o) even.
  - For r ∈ R̄_a, r's W-play reaches o after π_r (possibly along a stretch of C_W below o) and then cycles with node o. So
    W_a(r) = (o, π_r ∩ V_{>o}, |π_r|). ✓
- BASE (ii): D, its top u (rank u > rank o), and the same top on the W side, exactly as R2-N5-OUT §5. Then the cases:
  - Case 1 (v ∉ π_z, v ∉ C_W): neither z's play nor C_W passes v, so the switched W(v) is v ⊕ W_a(z) ▷ v ⊕ W_a(σ_a v) = W_a(v). ✓
  - Case 1′ (v ∉ π_z, v = c_i ∈ C_W ∖ {o}), new here:
    - π_{σ_a v} = c_{i+1} … c_m.
    - π_z can join C_W only at some c_j with j > i; a join at j ≤ i would pass v.
    - After the switch, o's W-play itself runs through v. So the new cycle Z = {o, c_1, …, c_i} ∪ π_z contains o, z and π_z.
    - u ∈ π_z (π_{σ_a v} lies below o), so Ω(u) is even. Every vertex of C_W is below o < u, and a vertex of π_z above u would lie in D.
      So the top of Z is u, and reward(u) > p′(o) = reward(o). ✓
    - This case is the reason the hypothesis is c_w = o. If c_w ≠ o, C_W's top above o can outrank u, and the cycle node is no longer u.
      tauw_A_cex_n24 is that case.
  - Case 2 (v ∈ π_z): the cycle v → z → q → v is topped by u (v and anything below c_θ are under u). v may lie on C_W here; the argument
    does not use that. ✓
  - The cases are exhaustive, and v ≠ o.
- STEP: verbatim R2-N5-OUT §5's STEP. It uses only SEP-o, (V1), R15, ACT (i) and INV. None of these involves W, τ(o) or c_w. ✓
- "No R̄-rise on [a, b] is high": Ξ_t(z) ≡_o Ξ_{t+1}(z) on R̄_{t+1}. ✓

## 4. Lemma CASE-B-LEN′: SIGN
- Case B gives Ω(c_θ) odd. A non-empty D has top u above c_θ, hence above o, and the same W-side top. Cases 1 and 2 are as before.
- Case 1′: π_{σ_a v} ⊆ C_W lies below o < u, so u ∈ π_z is even. Z's top is u, and p′(u) > p′(o) ≥ reward(o) holds for either parity of
  o. ✓
- So D = ∅ and lev = −1. The odd c_θ makes the longer route the better one. ✓

## 5. Lemma LOW-RISE′: SIGN (N-NEB-2)
- INV_B(a): (i) is FBL-N (iii) + (iii+), and (ii_B) is §4. ✓
- (a): the value claim with ≡_B. A switched z uses (ii_B) at t, and the case lev = −1 lies inside ≡_B. No entry follows from (i) at
  a..t. ✓
- (b): the argument of STEP (ii) at threshold 0. It uses the value claim and (ii_B) at t, not (i) at t+1 (N-NEB-2). ✓
- (c):
  - RISE's hypotheses hold, since (i) holds on [a, t] and fails at t+1.
  - (★), (a) and (T2) give Ξ_{t+1}(q) ≡_B Ξ_t(z) ≡_B Ξ_{t+1}(z).
  - So P(Ξ_{t+1} z) = P(Ξ_{t+1} q) ⊆ F_{t+1}, which kills π_z ∩ V_{>c_θ}.
  - In case B, o ∉ P(θ), and P(θ) ⊆ F. So both values lie in C_θ, and the rise is low. ✓

## 6. Theorem BRK: SIGN
- The eviction is a fallback (SPLIT). The entry needs an F → R̄ gate at k (ACT (i)). j0 ≠ a (F-FLAT).
- t+1 is the first state after a with an F → R̄ gate. It exists, since state k has one, and it lies in (a, k], since a has none.
- θ constant on [a, t+1]:
  - case A with c_w(a) = o contradicts §3, so a θ-change exists in (a, t] ⊆ (a, k];
  - case B with c_w(a) = o: §5 (c), with INV_B(s) on [a, t] by induction using (b) and the minimality of t+1, gives a low rise;
  - otherwise §1 gives a rise, high in case A by §2.
- Charges: distinct breaks have disjoint [a, k], so distinct charged transitions. A transition counted in two terms only loosens (d). ✓
- LR_S:
  - C_θ is a ≡_B class, hence an interval (T2), and Ξ is monotone. A vertex that leaves C_θ upward never returns, and inside C_θ its
    length moves one way.
  - o (value θ) and c_θ (value (c_θ, ∅, 0), constant) never rise.
  - The lengths of the other ≤ n − 2 vertices lie in [1, n − 1], so each has ≤ n − 2 low rises per θ-run, and there are ≤ θ_S + 1 runs.
    ✓
- The special cases of (d) follow: with c_w = o at every eviction state, RW_S = 0, and in case A every break has a θ-change. ✓

## 7. Corollary OUT-1: SIGN
- With τ(o) = o, c_w = o at every state (C_W = {o}). So B_S ≤ D(θ_S + 1) − 1, and EPOCH gives X_S ≤ 2(n − 1)D(θ_S + 1).
- f_HN ≤ Σ_S (f_S + 1) = Σ_S (K + 1)(X_S + 1), and Σ_S θ_S ≤ θ_ph.
- N_HN ≤ ⌊T_ph/2⌋ + 1 by NE-COUNT (c), which is signed.
- Both bounds follow. ✓

## 8. Data (DATA, not proof)
- Batch (run_all.sh, logs/, totals_logs.txt): 295 𝒞^1O library files × 3 traces × 3 starts = 2,655 runs, 50,667 states; random 𝒞^1O:
  22,000 own + 22,000 rand + 20,000 spec runs, 156,575 states. 894 / 894 logs end "RESULT OK violations=0" (one of them is the chain
  mode); there were no timeouts.
- Fallback bases (HN states with an in-phase Even fallback), library, own / rand / spec:
  | class | bases | proved claim checked | INV (§3) outside the proved class |
  | --- | --- | --- | --- |
  | case A, c_w = o, τ(o) = o | 124 / 141 / 126 | NO-ENTRY-A′ (= NO-ENTRY-A) | — |
  | case A, c_w = o, τ(o) ≠ o (new in this packet) | 26 / 20 / 28 | NO-ENTRY-A′ | — |
  | case B, c_w = o, τ(o) = o | 18 / 23 / 23 | CASE-B-LEN′, LOW-RISE′ | fails 0 / 0 / 1 (nebc, SPEC) |
  | case B, c_w = o, τ(o) ≠ o | 5 / 4 / 0 | CASE-B-LEN′, LOW-RISE′ | fails 1 / 1 / 0 (nebc, own / rand) |
  | case A, c_w ≠ o | 4 / 4 / 5 | RISE, HIGH-RISE only | fails 3 / 2 / 4 |
  | case B, c_w ≠ o | 11 / 12 / 11 | RISE only | fails 5 / 3 / 5 |
  - The proved class never fails: NEA2 walks 1,167 / 1,384 / 1,187 steps, LOW2 walks 71 / 86 / 71 steps.
  - The INV failures sit exactly outside it (c_w ≠ o, or §3's INV in case B). They are the controls: the hypotheses c_w = o and case A
    are used.
- RISE: 9 / 6 / 9 first F → R̄ gate states after a base. (★) held for every gate there. HIGH-RISE: 4 / 3 / 4 case-A rises, all at a
  level ≥ rank(o). LOW-RISE′ (c): 1 / 1 / 1 first INV_B (i) failures (nebc_cex_n14), each with a low rise at the gate's z.
- CASE-B-LEN′: 4 / 4 / 4 R → R̄ gates at case-B c_w = o bases, all of level −1 with the longer route.
- BRK, breaks by class (library):
  - case A, c_w = o: 12 / 12 / 12;
  - case B, c_w = o: 4 / 4 / 4;
  - case A, c_w ≠ o: 2 / 2 / 2;
  - case B, c_w ≠ o: 4 / 2 / 4.
  Every break was charged as in (a)-(c); 7 / 5 / 7 were paid by a rise rather than a θ-change. (d)'s inequality, the LR_S bound and the
  c_w = o special cases held in every stretch.
- OUT-1: 96 / 87 / 97 τ(o) = o phases with an HN state; both bounds held.
- Random games add only 9 bases (all case B) and no break. The library carries the content.
- Totals-script trap (mine, fixed before any number above was taken): my first totals.py regex dropped counter names containing "!"
  (e.g. "bases_caseA_cw!=o_tau!=o"). A summary that silently skips keys is the checker trap of my handover list, so I fixed the regex
  and re-summed. The per-file logs were always complete.
- Climbs (run_climbs.sh, climb/, totals_climb.txt): four 1200 s climbs (FIT brk seeded with nebc_cex_n14 and
  tauw_A_cex_n24; FIT cwo seeded with tauw_B_cex_n24 and nebc_cex_n14; own and rand traces):
  - totals: 125,473 evaluations, 501,892 runs, 3,528,456 states, 0 violations;
  - bases by class:
    - case A, c_w = o: 270 (τ(o) = o) + 18,324 (τ(o) ≠ o);
    - case B, c_w = o: 8,579 + 468,671;
    - case A, c_w ≠ o: 69,088;
    - case B, c_w ≠ o: 12,570;
  - NO-ENTRY-A′ walks: 52,899 steps; LOW-RISE′ walks: 1,423,808 steps, with 31,951 first INV_B (i) failures, each with a low rise;
    CASE-B-LEN′: 1,890,935 gates; RISE: 79,378 cases; HIGH-RISE: 223,685; all hold;
  - breaks: 3 (A, c_w = o), 31,167 (B, c_w = o), 45,587 (A, c_w ≠ o), 94 (B, c_w ≠ o). All are charged as in BRK (a)-(c) and (d)
    holds. 66,892 were paid by a rise; max LR_S 7;
  - controls: §3's INV fails 47,914 times at case-A c_w ≠ o bases and 32,155 times at case-B bases, where it is not claimed. So both the
    c_w = o hypothesis and the case split carry weight;
  - climbs are not families.

## 9. Notes for the lane (none blocks a signature)
- N-NEB-1: §3 BASE and §4 cite Step (K) "inside a phase". Use FBL-N (i) + F1 (the OUT fixes file §1 already says so for NEB).
- N-NEB-2 (optional): LOW-RISE′ (b) holds without (i) at t+1; it could be stated so. Nothing depends on it.
- N-NEB-3: the P-N5-OUT dependency rows are stale ("IN REVIEW"); both referees have signed, and the fixes file is 640a5db2.

## §C. Comparison with REFEREE's R-N5-NEB (written 2026-10-25 16:12Z by date -u, after my report a4516df9 was pushed and merged)
Read: docs/referee/R-N5-NEB.md on trunk (REFEREE successor 9, report 40adbf1c).
- Verdicts are identical. Both sign RISE, HIGH-RISE, NO-ENTRY-A′, CASE-B-LEN′, LOW-RISE′, BRK (a)-(d) and OUT-1; both find §0's filled-in
  steps correct. Neither signs §8. No gap in either report, so the joint gap map is empty.
- Notes map:
| REFEREE | REFEREE-2 | content | status |
| --- | --- | --- | --- |
| NEB-R1 | N-NEB-1 | Step (K) cited "inside a phase" in §3 BASE / §4; FBL-N (i) + F1 suffices | same; agreed |
| NEB-N1 | — | §6 "SPLIT (b): an S4a step does not evict" should be SPLIT (a) | ACCEPTED; my miss (my §6 wrote "SPLIT" without checking the letter). The packet text says (b) |
| NEB-N2 | (in my §6: "since a has none") | §6 must state that a itself has no F → R̄ gate (FBL-N (iii) + (iii+)) for §1's hypothesis on [a, t] | ACCEPTED. I used the line in my check but did not flag its absence from the packet |
| NEB-N3 | (in my §6: "o (value θ) and c_θ never rise") | "Values in C_θ belong to vertices z ∉ {o, c_θ}" is false as written (θ ∈ C_θ); intended "low rises are at z ∉ {o, c_θ}" | ACCEPTED; my check used the intended form, and I should have flagged the wording |
| NEB-N4 | N-NEB-3 | stale statuses: REFEREE's for KEY / FB-INT (now R38), mine for the P-N5-OUT rows (now R39) | both stand |
| NEB-N5 | — | §9 base totals not reproduced by the stated command | data note; accepted (I did not run the lane's scripts) |
| NEB-B1 | — | CONJECTURE BAND (§8, not to sign) FALSE in three forms, incl. band_base_cex.pg | record; accepted, not checked by me |
| — | N-NEB-2 | LOW-RISE′ (b) does not need (i) at t+1 (optional) | mine only |
- Data: both found 0 failures.
  - REFEREE's lib37 alone has 0 RISE events. My library (lib37 ∪ tracked 𝒞^1O files ∪ box38 instances, 3 starts each) has 9 / 6 / 9.
    Both reports' climbs exercise every proved class.
  - REFEREE's climbs also probe BAND (not signed).
- Joint state: all signable statements of P-N5-NEB are signed by both referees (Opus 5.5, D15), with no (P) and no gap. Fixes-file
  lines for L-NEW: NEB-R1 = N-NEB-1, NEB-N1..N5, N-NEB-2, N-NEB-3, and the NEB-B1 record.
