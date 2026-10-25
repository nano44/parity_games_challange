# R-N5-PFZ: REFEREE report on packets P-N5-PFZ and P-N5-PFZ-ext (box 39: FB-ROUND, P-FREEZE, LEN-TAIL, NO-CROSS-A, RISE′, BRK-POLY; P-FREEZE′, θ-LEN, BRK-POLY′)
Referee: REFEREE (successor 9, session_01VsZYJ8FiTSj5Kazk715ZP7), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: the Lead's messages of 15:34Z and 15:41Z (Lead's stamps): review PFZ and PFZ-ext as one unit, one report.
- Objects (sha1s checked with `git show <pin>:<path> | sha1sum`):
  - docs/new/P-N5-PFZ-box39.md at trunk 283bcb6, sha1 3c617e06f7b9c67d5d9cd865acd134f3a8aed071, 247 lines;
  - docs/new/P-N5-PFZ-ext-box39.md at trunk c61ecc4, sha1 b3702b1ba1849c6aa19cebd2c8fa57e02a318d2a, 87 lines.
  Author: L-NEW successor 18.
- Written 2026-10-25T15:52Z onward by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: I did not read docs/referee-2/R2-N5-PFZ*.md. D1: each statement treated as wrong until its proof checked.

## Verdicts
| packet § | statement | label | verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| PFZ §1 | Facts (A), (M1′), (M2′); Lemma FB-ROUND | PROVED | SIGNED |
| PFZ §2 | Theorem P-FREEZE (a), (b), (c) | PROVED | SIGNED |
| PFZ §3 | Corollary LEN-TAIL | PROVED | SIGNED |
| PFZ §4 | Corollary NO-CROSS-A (case A) | PROVED | SIGNED |
| PFZ §5 | Lemma RISE′ | PROVED | SIGNED |
| PFZ §6 | Theorem BRK-POLY (i), (ii), with its EPOCH consequence | PROVED | SIGNED |
| ext §1 | Theorem P-FREEZE′ (with LEN-TAIL′, NO-CROSS-A′) | PROVED | SIGNED |
| ext §2 | Lemma θ-LEN | PROVED | SIGNED |
| ext §3 | Theorem BRK-POLY′ (i)-(iii) | PROVED | (ii), (iii) SIGNED GIVEN (i). **(i) SIGNED WITH GAP PFZ-1**: the statement is true, but the proof omits the ρ_S P-changing transitions. Referee repair below; with it all of (i)-(iii) hold as stated |
| PFZ §7, ext §4 | P-epoch material (in PFZ), W-TIE, block lemmas, open items | not to sign | not signed |
- No (P). The labels are exact otherwise. Premises: (V1) (R17 (a)), R15 (a), (d), KEY (R38 (a)), FBL-N (ii), (iii) (R21 (c)), ACT (i)
  (R23 (b)), SPLIT, F-FLAT (R39 (a), (c)). All are landed. P-N5-NEB is not used (RISE′ is re-proved in full).
- VACUOUS IN DATA (lesson N-ENT-2): the post-freeze hypothesis "t > f_{|U|−1}" occurs only with |U| = 1 (28 epochs). So P-FREEZE (c),
  LEN-TAIL, NO-CROSS-A and the "j ≥ |U|" branch of BRK-POLY / BRK-POLY′ stand on their proofs. My climb toward |U| ≥ 3: §8.1.
- One gap (PFZ-1), with a repair. Notes PFZ-N1..N3.

## 1. FB-ROUND: checked
- (A):
  - λ_t(z) = c_θ ≠ z, so (V1) applies (also on the cycle: there P = ∅, and z's rank is below c_θ). next_t(z) has the same cycle node,
    so it is in U.
  - The "no double count" fill-in is correct: z ∈ P(Ξ next z) would put z on its own cycle, whose top is c_θ, hence rank z < rank c_θ.
- (M1′): with the same cycle node, the order compares P by its top differing vertex, which is the order of the signed weights.
  (M2′): R15 (a) with the cycle node c_θ constant in a phase. Correct.
- Case 1: (M1′) at k for x, σ_k v ∈ U, then (A), then (M2′).
- Case 2: S4c moves v to x* with Ξ_k x* ⊵ Ξ_k x; λ_{k+1}(v) = c_θ (phase), so (A) holds at k+1; then (M2′) and (M1′) (x*, x ∈ U, a
  phase constant).
- Correct. Indeed nothing about θ, H1, H2 or 𝒞^1O is used.

## 2. P-FREEZE: checked
- (b): z's honest play reaches c_θ (on its cycle) before any repetition, so its prefix up to the first terminal is a simple path of G_U:
  σ_t-edges into U at Even vertices, forced edges at Odd ones, and terminals are sinks. (A) along it gives
  M_t(z) = wt(p ∖ end) + M_t(end), with M_t(o) = wt(P(θ)) = M_Θ(o) and M_t(c_θ) = 0. Correct.
- (a): induction on j.
  - Odd z: the forced edge is next_t(z), (A), and the hypothesis at t > f_{j−1}.
  - Even z: the hypothesis at k = f_j ∈ Θ (k > f_{j−1}), FB-ROUND at the Θ-fallback k (its x ∈ U is a G_U-successor), and (M2′) from
    k+1 to t inside Θ.
  - wt(p ∖ end) = wt(z) + wt(p′ ∖ end), since p is simple. If f_j does not exist the claim is vacuous. Correct.
- (c): ≤ |U| − 1 edges on a simple path, so (a) with j = |U| − 1 and (b) give equality. The map S ↦ Σ_{v∈S} sgn(v)·2^rank(v) is
  injective on sets above c_θ (the top element of S Δ S′ dominates the difference). So P is determined. Correct.

## 3. LEN-TAIL: checked
- Post-freeze U-rises keep c_θ and P, so they are length rises.
- Ψ = Σ_z s_θ·ℓ(Ξ_t z) is non-decreasing (R15 (a), the order inside a fixed (c, P) is the length order) and rises by ≥ 1 at each U-rise.
- ℓ(Ξ_t z) ∈ [0, |U| − 1]: the play from z to c_θ is simple and lies in U by (A).
- Correct (both ends of each counted transition lie in Θ, as "transition of Θ" requires).

## 4. NO-CROSS-A: checked
- Route form: on 𝒞^1O the honest and (σ, τ)-graphs differ only at o. Under H1, o's honest play cannot meet π_z (it would run back to o).
  So Ξ_s(z) = π_z ⊕ θ_s and z ∈ U.
- SEP-o: o ∈ P(θ_s) (H1, case A), so o ∈ P(Ξ_s z) on R̄_s. On U ∩ F_s the honest play avoids o.
- Hence R̄_s = {z ∈ U : o ∈ P(Ξ_s z)} at H1 states, and P-FREEZE (c) at t and t+1 gives R̄_t = R̄_{t+1}. Correct.

## 5. RISE′: checked (same argument as P-N5-NEB §1, which I signed in R-N5-NEB; re-checked here from landed results)
- Step 0: FBL-N (iii) plus the target-o fill-in (λ_W(o) ∈ C_W ⊆ R̄_a under ¬H2). Correct.
- Step 1: ACT (i) at the entry k → k+1 (τ unchanged in S) and R15 (d). Correct.
- The case split: a θ-change in [a, t] is not at a (F-FLAT), so it lies in [a+1, t] ⊆ [a+1, k]. Correct.
- Step 2: no F → R̄ gate on [a, t], hence no entry (ACT (i)), hence R̄ does not grow. Correct.
- Step 3, (★):
  - y ∈ F_t: as in R-N5-NEB §1.
  - y ∈ R_t: SPLIT (a) makes t → t+1 a fallback, and it is Even because τ is constant. S4c's maximiser gives (★).
  - z ≠ o (θ constant on [t, t+1]). Correct.
- The hypothesis "no transition of [a, k) is an entry" is not needed (Step 2 derives what is used); harmless.

## 6. BRK-POLY: checked
- Window [a, k] with a the LAST eviction before the entry. It is a fallback (SPLIT (a): a non-fallback at an HN state does not evict)
  and Even (τ constant).
- Windows of distinct breaks are disjoint: the later break's eviction follows the most recent entry, which is at or after the earlier
  break's entry.
- RISE′ applies (no entry in (a, k); the eviction a is not an entry).
- Kind 1: distinct θ-changes (disjoint windows), both ends in S.
- Kind 2: a … t+1 lie in one θ-run Θ, and a → a+1 = f_j of Θ.
  - j ≤ |U| − 1: ≤ |U| − 1 per Θ.
  - j ≥ |U|: t ≥ f_j > f_{|U|−1}; the R̄-rise is a U-rise (R̄ ⊆ U at H1 states, §4), so LEN-TAIL counts it. Distinct breaks give
    distinct t.
  - Case A: the eviction would be a post-freeze crossing between H1 states, against NO-CROSS-A.
- S meets ≤ θ_S + 1 θ-runs. (i) and (ii) follow, and |U|² − 1 ≤ n² − 1. Correct.
- EPOCH consequence: X_S ≤ 2(n − 1)(B_S + 1) ≤ 2(n − 1)n²(θ_S + 1), f_S ≤ K(X_S + 1) + X_S, so O(n³K(θ_S + 1)). Correct. θ_S stays a
  parameter: no running-time bound for N5, as the packet says.

## 7. PFZ-ext: checked
- P-FREEZE′ (§1): I went through every use of θ in PFZ §1-§4.
  - It enters only through M_t(o) = wt(P(θ_t)), which is constant on a P-epoch, and through route form / SEP-o at single states.
  - FB-ROUND and (M2′) are θ-free. LEN-TAIL′ counts o's own length rises as U-rises.
  - Correct.
- θ-LEN (§2): with c_θ and P fixed, θ moves only in ℓ, monotonically. ℓ ∈ [1, |U| − 1]: o's play to c_θ is simple, in U, and has
  ≥ 1 edge when o ≠ c_θ. Correct.
- BRK-POLY′ (§3):
  - (ii), (iii) are the PFZ §6 window argument per P-epoch, plus (i). The algebra was checked: θ_S + (ρ+1)(|U|² − 1) ≤
    (ρ+1)(|U|² + |U| − 3) ≤ (ρ+1)(2n² − 1), and θ_S + (ρ+1)(|U| − 1) ≤ (ρ+1)(2|U| − 3) ≤ (ρ+1)(2n − 3), both GIVEN (i).
  - **GAP PFZ-1 in (i).**
    - θ_S counts every θ-change of S (PFZ §0: transitions with θ_{k+1} ≠ θ_k). A transition at which P(θ) changes is a θ-change.
    - θ-LEN bounds only the θ-changes INSIDE a P-epoch (both ends in Π). The proof "S meets ≤ ρ_S + 1 P-epochs; apply θ-LEN to each"
      therefore yields only θ_S ≤ ρ_S + (ρ_S + 1)·max(|U| − 2, 0). It misses the ρ_S boundary transitions.
    - Example of the slack: ρ_S = 1, |U| = 3 gives "(i) ≤ 2", while the proof gives only ≤ 3.
  - Referee repair (closes PFZ-1; (i)-(iii) then hold verbatim):
    - Let A := U ∖ {c_θ}, A_low := A ∩ V_{<c_θ}, A_high := A ∩ V_{>c_θ}, and let Q be o's path to c_θ (c_θ excluded).
    - Then ℓ(θ) = |Q|, Q ⊆ A, Q ∩ V_{>c_θ} = P(θ). Inside a P-epoch, ℓ = |P(θ)| + |Q ∩ A_low|, and Q ∩ A_low contains o iff o ∈ A_low.
      So a P-epoch has ≤ |A_low| − [o ∈ A_low] θ-changes (refined θ-LEN; it implies θ-LEN, since that is ≤ |U| − 2).
    - If ρ_S ≥ 1, P(θ) changes, and o's membership in P(θ) is fixed (o is always the first vertex of Q). So some u ∈ A_high ∖ {o}
      exists, and |A_low| − [o ∈ A_low] ≤ |U| − 3.
    - Hence θ_S ≤ ρ_S + (ρ_S + 1)(|U| − 3) ≤ (ρ_S + 1)(|U| − 2) when ρ_S ≥ 1. When ρ_S = 0, (i) is θ-LEN.
  - Data: the refined count holds at all 599 in-epoch θ-changes of my data (0 failures). Every phase in which P(θ) changes has a
    vertex of U ∖ {o, c_θ} above c_θ (0 failures). The stated (i) has 0 violations in data (it is true).
  - The packet's consequence O(n³K(ρ_S + 1)) and (ii)'s final (ρ_S + 1)(2n² − 1) hold even with the unrepaired
    (i′) θ_S ≤ ρ_S + (ρ_S + 1)max(|U| − 2, 0): ρ_S + (ρ_S + 1)(|U|² + |U| − 3) ≤ (ρ_S + 1)(n² + n − 2) ≤ (ρ_S + 1)(2n² − 1).
    Only (iii)'s final constant 2n − 3 (it would become 2n − 2) and (ii)'s middle term need the repair.

## Notes for the lane's fixes file
- PFZ-1 (gap, repair above): BRK-POLY′ (i)'s proof must count the P-changing transitions. Either adopt the refined θ-LEN above, or
  state (i′) θ_S ≤ ρ_S + (ρ_S + 1)max(|U| − 2, 0) and change (iii)'s final constant to 2n − 2.
- PFZ-N1 (wording): PFZ §6 cites "SPLIT" for "the eviction is a fallback"; the part used is SPLIT (a).
- PFZ-N2 (precision): RISE′'s hypothesis "no transition of [a, k) is an entry" is stronger than needed; Step 2 derives what is used.
- PFZ-N3 (status): P-N5-NEB is now signed by both referees (R-N5-NEB 40adbf1c; REFEREE-2 a4516df9 per the git log). The packet's
  "in review" no longer applies. It is not a premise anyway.

## 8. DATA (DATA, not proof; own code docs/referee/scratch/pfz_probe.py on rl_engine, no lane imports; logs docs/referee/R-N5-PFZ/)
- Files: lib37 + experiments/new/box37/instances + box38/instances + red/so/instances/pftheta*.pg: 278 C^1O games (159 skipped).
  Canonical start. Both epoch kinds (θ-runs; P-epochs). Exact Mopt / best-j by DFS over simple paths of G_U for |U| ≤ 13 (UMAX).

| check | θ-runs (PFZ) | P-epochs (ext) | failures |
| --- | --- | --- | --- |
| (A) additivity, states × z | 245,740 (per phase, shared) | — | 0 |
| FB-ROUND, fallback × v × x | 80,955 (shared) | — | 0 |
| epochs / with |U| > 13 (UB, (a) skipped) | 3,164 / 2,698 | 2,565 / 2,112 | — |
| P-FREEZE (b) UB checks / (a) checks | 4,681 / 571 | 4,681 / 577 | 0 |
| post-freeze epochs (|U| = 1 / 2 / ≥ 3); states | 28 / 0 / **0**; 76 | 28 / 0 / **0**; 76 | 0 |
| LEN-TAIL post-freeze U-rise transitions; NO-CROSS-A checks | 0; 0 | 0; 0 | 0 |
| θ-LEN: in-epoch θ-changes (stated bound; refined count) | — | 599 | 0; 0 |
| HN stretches / with ρ_S > 0; breaks (kind 1 / kind 2); RISE′ | 120 / 23; 16 (11 / 5); 16 | | 0 |
| BRK-POLY (i), (ii); BRK-POLY′ (i) stated, (i′), (ii), (iii) | all checked | | 0 |

- The counts agree in kind with the packet's §8: post-freeze only at |U| = 1, and breaks charged 11 kind 1 / 5 kind 2 against the
  packet's 10 / 5 (15 breaks). My file set adds red/so/pftheta*.pg and the box-37 instances.

### 8.1 Climb toward the post-freeze regime with |U| ≥ 3 (own code scratch/pfz_climb.py; logs scratch/pfz_logs/; 15 min × 4, 15:55-16:10Z)
- Score = max over θ-runs with |U| ≥ 3 of (#Even fallbacks in the run) − (|U| − 1). A score ≥ 1 is the post-freeze regime.
- Seeds: wd12_s1, nebc_cex_n14, neb_cex_n11, norise_state_n8. 6,479,637 mutants evaluated.
- Best excess −1 in all four walks: θ-runs came one fallback short of the freeze point, and none passed it. No post-freeze |U| ≥ 3
  θ-run was found.
- So P-FREEZE (c), LEN-TAIL, NO-CROSS-A and BRK-POLY's j ≥ |U| branch are untested beyond |U| = 1. They rest on their proofs, which
  I checked in full (§2-§4, §6).

## §C. Comparison with REFEREE-2 on P-N5-PFZ (main packet only): docs/referee-2/R2-N5-PFZ.md at referee-2 37e55fde (sha1 b124ecc6…, the same on origin/claude/referee-2)
Written 2026-10-25T16:33Z by date -u, after the Lead's word of 16:22Z (Lead's stamp) that 37e55fde is final. I opened R2-N5-PFZ only
after my report 85953433 was pushed. REFEREE-2 9 did not review P-N5-PFZ-ext (b3702b1b). The ext items, including my GAP PFZ-1, wait
for REFEREE-2 successor 10 and a later §C. (Opus 5.5, D15).
- Verdicts on P-N5-PFZ §1-§6: identical. Both referees sign FB-ROUND, P-FREEZE (a)-(c), LEN-TAIL, NO-CROSS-A, RISE′, BRK-POLY (i), (ii),
  and neither signs §7. No gap on either side for the main packet.
- Joint gap map (main packet): EMPTY.

| item | REFEREE-2 | REFEREE (mine) | outcome |
| --- | --- | --- | --- |
| (A)'s filled-in case "z ∈ P(Ξ next z)" | N-PFZ-1: the case cannot occur | my §1: it would put z on its own cycle below c_θ, so z ∉ P: the same conclusion (impossible) | agreed; wording note for the lane |
| BRK-POLY window = last eviction before the entry (P-N5-NEB uses the first eviction after the previous entry) | N-PFZ-2 | my §6 checked this window and its disjointness, without a note | agreed; worth one line if the RESULTS entries are merged |
| post-freeze regime "t > f_{|U|−1}" | N-PFZ-3: reached only with |U| ≤ 2 (|U| = 2 in 955,321 climb θ-runs); never with |U| ≥ 3 | |U| = 1 only in my data; my |U| ≥ 3 climb: best excess −1, never past | consistent; both rest P-FREEZE (c), LEN-TAIL, NO-CROSS-A and the late kind-2 branch on the proofs |
| "the eviction is a fallback" cites SPLIT | — (R2: "SPLIT (a)" used for RISE′'s case split) | PFZ-N1 | citation note stands |
| RISE′'s "no entry in [a, k)" stronger than needed | — (R2: the window convention makes it hold; checked) | PFZ-N2 | compatible; precision note stands |
| P-N5-NEB "in review" status | — | PFZ-N3 | stands |

- Data agree in kind (0 failures; FB-ROUND and P-FREEZE (a), (b) heavily exercised on both sides). R2 adds the |U| = 2 post-freeze
  regime (0 post-freeze U-rises there); I add the P-epoch (ext) checks.
- Pending: the ext §C (P-FREEZE′, θ-LEN, BRK-POLY′, GAP PFZ-1 and its repair) after REFEREE-2 10's report.

## §C-ext. Comparison with REFEREE-2 on P-N5-PFZ-ext: docs/referee-2/R2-N5-PFZ.md §X at referee-2 78896bfc (sha1 b0168708…, the same on trunk f090ec9e)
Written 2026-10-25T17:46Z by date -u by REFEREE successor 10 (session_01J4kmfDqtZdanh3RSCxChyD), after the Lead's word of 17:34Z (Lead's
stamp) that 78896bfc is final. The ext review above (§ ext, GAP PFZ-1, 85953433) is my predecessor's. I re-derived PFZ-1 and its repair
myself before writing this; I do not inherit them. (Opus 5.5, D15).

| item | REFEREE-2 (§X) | REFEREE | outcome |
| --- | --- | --- | --- |
| ext §1 P-FREEZE′ (LEN-TAIL′, NO-CROSS-A′) | SIGN | SIGNED | identical |
| ext §2 θ-LEN | SIGN | SIGNED | identical |
| ext §3 BRK-POLY′ (i) | NOT SIGNED as stated; SIGN (i′) θ_S ≤ ρ_S + (ρ_S + 1)·max(\|U\| − 2, 0); gap G-PFX-1 | SIGNED WITH GAP PFZ-1 + referee repair | same gap (G-PFX-1 = PFZ-1); labels differ only through the repair (below) |
| (ii) | SIGN B_S ≤ θ_S + (ρ_S + 1)(\|U\|² − 1) and the end bound (ρ_S + 1)(2n² − 1); middle bound needs + ρ_S | SIGNED GIVEN (i); "(ii)'s middle term needs the repair"; end bound holds with (i′) | identical in substance |
| (iii) | SIGN B_S ≤ θ_S + (ρ_S + 1)(\|U\| − 1); end bound (ρ_S + 1)(2n − 2) | SIGNED GIVEN (i); with (i′) the end constant becomes 2n − 2, with the repair 2n − 3 stands | identical in substance |
| Consequence O(n³·K·(ρ_S + 1)) | SIGN | holds with (i′) | identical |

- Joint gap map (ext): one row. **PFZ-1 = G-PFX-1**. Both referees found it independently. The proof bounds the θ-changes inside each
  P-epoch and misses the ρ_S transitions that join epochs. Both say (i) is not refuted by any data. Both say (i′), (ii)'s end bound and
  the Consequence hold as the proof stands.
- Reconciling the label on (i) (the Lead's ask).
  - REFEREE-2's fix list allows "or prove that the P-change transitions are paid by the epochs' slack. I see no such argument." My
    repair (R-N5-PFZ ext §3, above) is exactly such an argument. I re-checked it step by step:
    - Inside a P-epoch Π with o ≠ c_θ, c_θ and P(θ) are fixed. Q, o's honest path to c_θ (c_θ excluded), is simple in U and has
      ℓ(θ) = |Q| = |P(θ)| + |Q ∩ A_low|, with A_low := (U ∖ {c_θ}) ∩ V_{<c_θ}. Q always contains o. So |Q ∩ A_low| ranges over at most
      |A_low| + 1 − [o ∈ A_low] values.
    - θ-LEN's monotonicity (R15 (a), fixed c and P) therefore gives ≤ |A_low| − [o ∈ A_low] θ-changes inside Π (refined θ-LEN).
    - If ρ_S ≥ 1, P(θ) changes. o's membership in P(θ) is fixed, so P(θ) ∖ {o} ⊆ A_high ∖ {o} changes, and some u ∈ U ∖ {o, c_θ} lies
      above c_θ. Since o lies in exactly one of A_low, A_high: |A_low| − [o ∈ A_low] ≤ (|U| − 1) − 1 − 1 = |U| − 3.
    - So θ_S ≤ ρ_S + (ρ_S + 1)(|U| − 3) = (ρ_S + 1)(|U| − 2) − 1 when ρ_S ≥ 1. When ρ_S = 0, (i) is θ-LEN. That is (i) as stated.
  - My answer: yes. With this argument in the fixes file (refined θ-LEN + the "ρ_S ≥ 1 ⇒ a high u ≠ o" step), (i) as stated has a
    complete proof. REFEREE-2 can check that and sign (i), and then (iii)'s end constant 2n − 3 and (ii)'s middle bound stand as
    written. Until REFEREE-2 signs the repaired text, the jointly signed form is (i′) with (iii)'s end bound (ρ_S + 1)(2n − 2). That is
    what P-N5-RHO's HN-POLY uses (R-N5-RHO), so nothing downstream waits on this.
  - Lane: carry PFZ-1 in the PFZ fixes file as either (a) the repair above (proof of (i) as stated) or (b) (i′) + 2n − 2. Under (a),
    the landing of (i) as stated needs REFEREE-2's signature on the repair.
- Data:
  - REFEREE-2: 0 violations of (i) as stated in 8,415 batch stretches and 269,211 climb stretches (ρ_S up to 16). The climb aimed at
    θ_S > (ρ_S + 1)·max(|U| − 2, 0) and reached excess 0 at most.
  - Mine (predecessor): the refined count held at all 599 in-epoch θ-changes.
  - Today I ran pfz_probe.py on REFEREE-2's six saved climb outputs (docs/referee-2/R2-N5-PFZ/climb/best_*.pg; sha1 8ec62bb9, ab130853,
    0a42b9eb, 2d4474d1, cc0e7252, 8ddcf96f). 0 failures, including TLEN_refined, but 0 in-epoch θ-changes there, so they add nothing
    for the refined count (log scratch/pfz_logs/r2climbs_c.log).
  - Both sides: the post-freeze regime |U| ≥ 3 is never reached for P-FREEZE′ / LEN-TAIL′ / NO-CROSS-A′.
- No verdict of mine changes. (Opus 5.5, D15)
