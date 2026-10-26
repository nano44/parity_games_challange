# R2-N5-ENT: second-referee check of packet P-N5-ENT (L-SI box 11: FZ, BF, RB, WALK, CYC-EV, TEV-FB; ENT-X, NJB-A, D1, PL-S″ conditional on (P)). REFEREE-2 (successor 9), written 2026-10-25 14:0xZ-14:27Z (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-ENT (Lead GO 13:35Z by the Lead's stamp, after R2-N5-OUT). Object docs/si/P-N5-ENT-box11.md,
sha1 4fd22be79f7050a7f466288c76eea8bfe2f669d0. I checked the sha1 three ways: `git show 765e893:<file> | sha1sum`,
`git show origin/claude/l-si:<file> | sha1sum`, and on my tree. All three agree. The pin is trunk 765e893. The file has one commit,
3126857d.
Background read:
- SPEC S1-S5;
- RESULTS R15 (a); R19 (a); R25 (P-N5-FB §1: lev, COARSE_L, (C1)-(C4)); R29 (a), (c), (e), (f); R31 (c), (d), (f) with
  docs/si/P-N5-FBW-box9.md §0; R35 (a), (c), (d);
- P-N5-RL §5-§6 (MERGE, EV, EV+) and docs/si/P-N5-RL-fixes-box10.md (RL-1..4, the RL-fixes CYC-EV);
- my predecessor's R2-N5-RL (verdicts, §C, Addendum A) for EV / EV+'s status.
Independence:
- I read nothing in docs/referee/ or notes/REFEREE.md. REFEREE's R-N5-ENT (55a3f6f, per the Lead) is in my merged tree; I did not open
  it.
- No lane script (rb.py, straddle.py, nleq.py) was run or imported.
- Lane .pg files (L-RED's tev_cex_n40, tevlast_cex_n40, tevlast11_n40, tevlast7_n32 on trunk) are inputs only.
Tools: docs/referee-2/R2-N5-ENT/ (own code; it builds on R2-N5-OUT/out_check.py, R2-N5-FRZ/frz_check.py and R2-N5-RE/re_check.py):
- ent_check.py: the checks;
- rise_end.py: the record of how a scope run ends after a rise;
- ent_climb.py: the climbs;
- files.lst, run_all.sh, run_climbs.sh, totals.py, logs/, climb/, totals_logs.txt, totals_climb.txt.
Every game asserts exactly one Odd vertex with out-degree > 1.
Attribution. Traces: own (my N5, deterministic switch-all S4a optimum), rand (my N5, any S4a optimum), spec (experiments/new/n5.py's
state sequence, checked with my definitions). Each count below names its trace.
Labels: PROVED (L-SI succ. 6) = no (P); PROVED CONDITIONAL on (P). Nothing here is a running-time bound, a TARGET.md claim or a step-4
pass. G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §0 facts (Σ1)-(Σ6) | correct as written | Checked mechanically at every (Σ)-pair (§6) |
| §1 Lemma FZ | SIGN | — |
| §1 Lemma BF | SIGN | — |
| §2 Lemma RB | SIGN | — |
| §2 Corollary WALK (a)-(c) | SIGN | — |
| §3 Lemma CYC-EV | SIGN | N-ENT-1 (diff): this statement has a WEAKER hypothesis than the RL-fixes CYC-EV, which my predecessor signed in R2-N5-RL Addendum A: (Σ) + a rise, without M_k = L. The conclusion is the same, and the proof uses only (Σ4) M_k ≤ L (in RB). So the ENT form implies the RL-fixes form. The hypothesis is never reached ("Reachability" below) |
| §3 Proposition TEV-FB | SIGN | The hypothesis ((Σ) + a rise) is never reached in my data either ("Reachability" below, §6). Control: without a rise the threat's play meets Ev in 64 / 60 / 65 library (Σ)-pairs, so the rise is used |
| §4 Theorem ENT-X | SIGN CONDITIONAL ON (P) | EV+'s setting (P-N5-RL §6) is word for word the ENT setting, and its conclusion is the negation of TEV-FB's. EV+ is signed by both referees CONDITIONAL ON (P) (REFEREE-2: R2-N5-RL 30dc5f54, §C 88571b03). (P) = Lemma P1 (P-N5-P1), signed by both referees, not yet landed |
| §5 Corollary NJB-A | SIGN CONDITIONAL ON (P) | N-ENT-2 (precision): §7's "ENT-X and its corollaries have vacuous hypotheses everywhere" holds for ENT-X, CYC-EV and TEV-FB, but not for the corollaries. NJB-A's hypothesis (a block interval with r > M throughout) occurs 698 / 601 / 701 (own / rand / spec, library) times in my batch, and every such interval was clean. Only the dirty case is unreached |
| §5 Corollary D1 | SIGN CONDITIONAL ON (P) | — |
| §5 Corollary PL-S″ | SIGN CONDITIONAL ON (P) | — |
| §6 | not signed (as briefed) | — |
N-ENT-3 (status): §0's "REFEREE-2's report is pending" is stale. R2-N5-RL (30dc5f54), its §C (88571b03) and Addendum A (db9d66a8) are
all on trunk. Landing as R36 (P1) and R37 (RL) is queued at CHECKER (docs/NOW.md).
No statement is NOT SIGNED, and no gap is open. No counterexample turned up in 66,655 batch runs (2,655 library + 64,000 random) or in
62,036 climb runs (4 climbs, seeded with L-RED's TEV instances).
Reachability, the Lead's question. In my data (batch + climbs), no (Σ)-pair has a rise, as in the lane's data. CYC-EV, TEV-FB and ENT-X
therefore rest on their proofs alone.
- The nearest configurations: a rise after a fallback k0 with r > L does occur, 62 / 68 / 62 times in the library (L-RED's TEV instances among them). In every case the scope run has no
  further fallback after the rise (RECORD_rise_with_no_next_fallback_in_S). Neither "a later fallback of S, with r ≤ L reached before it"
  nor "a later fallback of S with r > L kept" (which is (Σ) + rise) occurred. The climbs (FIT rise, three seeds) reach 26,665 such rises, and again none is followed by a fallback of S.
  How S ends after the rise (rise_end.py, own trace, library, 62 rises; DATA): r drops to ≤ L 38 times, N5 stops 13 times, the λ-phase
  ends 6 times, and H2 fails at the next state 5 times.
  In all data, a scope run has no fallback at all after such a rise, whether or not r has dropped. This is stronger than ENT-X and
  unconditional in form, but it is a DATA observation, not a claim. It would make (Σ) + rise empty and CYC-EV / TEV-FB vacuous.
- The (Σ)-facts that CYC-EV and TEV-FB build on are exercised (FZ, BF, RB, WALK (a)-(c), 756 / 660 / 760 (Σ)-pairs; 698 / 601 / 701 of them have M_k = L, i.e. they are the ENT setting minus the rise), and they all hold.
- I found no argument that (Σ) + a rise is impossible without (P). Nothing in §1-§3 excludes M_k < L after a rise.

## 1. The setting (Σ) and its facts
- (Σ1): consecutive fallbacks of one scope run, so every transition in (k0, k) is an in-phase S4a step. ✓
- (Σ2): every state of [k0, k] is the source of a transition of S, so (h) holds there.
  - OFFGATE at k0 → k0+1 (R29 (c): gates at k0+1 into F_{k0+1} have level ≤ M_{k0} = L) gives (A_{k0+1}).
  - NL (iii) at each S4a step (k0 < s < k: (h) at s, r_s > L, (A_s)) gives (A_{s+1}). ✓
- (Σ3): NL (ii) gives R_s ⊆ R̄_{s+1}, so F_{s+1} ⊆ F_s on [k0+1, k].
  - FLAT-ALL (i) at k0 (M_{k0} = L ≥ 0, (h) at k0 and k0+1) gives F_{k0} ⊆ F_{k0+1}, so F_{k0+1} = F_{k0} ⊔ Ev.
  - Ev ⊆ R̄_{k0} ∖ {o}, since o ∉ F_{k0+1}. So Ev ∩ F_k = R_{k0} ∩ F_k. ✓
- (Σ4): CLS2 (R31 (c)). ✓
- (Σ5): under H1, o's honest cycle avoids o, and its vertices keep their successors in the (σ, τ)-graph. So c ∈ F at every state with H1.
  ✓
- (Σ6): COARSE_L(θ) is ⊴_L-monotone (R15 (a), (C1)). One strict step and (C3) give COARSE_L(θ_k) ≠ COARSE_L(θ_{k0}), with the cycle
  node c on all of S (w constant, H3). P(θ) ⊆ V_{>c}, so P(θ) ∩ V_{>L} = P(θ) ∩ H, and B ≠ A. ✓
- FLAT-ALL (ii) also keeps COARSE_L(θ) across k0 itself. So "a rise in (k0, k)" and "COARSE_L(θ_k) ≠ COARSE_L(θ_{k0})" are the same
  condition. ent_check.py checks this equivalence at every (Σ)-pair.

## 2. Lemmas FZ and BF: SIGN
- FZ.
  - Membership by (Σ3).
  - Across k0, FLAT-ALL (iii): COARSE_M is unchanged at every vertex with M = M_{k0} = L.
  - At each S4a step, NL (i) for v ∉ R̄_{s+1}, i.e. v ∈ F_{s+1} ⊇ F_k. Its hypotheses: (h) at s, r_s > L, (A_s). ✓
- BF.
  - At k0: v ∈ R_{k0} and Lemma G give Ξ_{k0}(v) = v ⊕ Ξ_{k0}(a) with cycle node c.
  - At k: FZ gives cycle node c for Ξ_k(v). v ≠ c, since c ∈ F_{k0} and v ∈ R_{k0}. So λ_k(v) ≠ v, and (P2) gives Ξ_k(v) = v ⊕ b_k(v).
  - v is not on its successor's pre-c path: a return to v before c makes v's play a cycle that either meets c before v or never meets c.
    ✓
  - (C4) with v ∉ P(x) gives P(x) ∩ V_{>L} = (P(Ξ v) ∩ V_{>L}) ∖ {v} at both states, and FZ equates the right-hand sides. The cycle node of
    b_k(v) is that of Ξ_k(v), namely c. ✓

## 3. Lemma RB and Corollary WALK: SIGN
- RB.
  - a ≠ σ_k(v), because σ_k(v) ∈ F_k (v ∈ F_k) and a ∈ R̄_k.
  - By R15 (a) and (C1), COARSE_L(Ξ_k a) ⊵_L COARSE_L(Ξ_{k0} a) = COARSE_L(b_k v) (BF).
  - If the inequality were strict, then Ξ_k(a) ⊴ b_k(v) is impossible: (C1) would give the reverse coarse inequality, and (C3) would make
    the two coarse values equal. So Ξ_k(a) ▷ b_k(v) at a level > L (C2). (v, a) is then a gate at k of level > L ≥ M_k (Σ4). ✓
- WALK (a): j exists, since a_{m+1} = o ∈ R̄_k.
  - v = a_{j−1} ∈ F_k: by minimality of j, or v = v0.
  - v ≠ o, since routes exclude o.
  - An Odd v would have a_j as its only successor and so lie in R̄_k. So v is Even, with σ_{k0}(v) = a_j. ✓
- WALK (b): RB at v. Lemma G at k0 and at k (a_j ∈ R̄ at both) gives the path part (π^s_{a_j} ∩ H) ⊔ (P(θ_s) ∩ H). The union is
  disjoint because π ⊆ R_s and P(θ_s) ⊆ {o} ∪ F_s. ✓
- WALK (c): π^{k0}_{a_j} ⊆ π^{k0}_{a_1}, so a low tail gives (π^k_{a_j} ∩ H) ⊔ B = A, hence B ⊆ A. ✓

## 4. Lemma CYC-EV and Proposition TEV-FB: SIGN
- CYC-EV.
  - Let v ∈ Ev ∩ F_k lie on C_k. v's honest play runs along C_k to its top c, so Ξ_k(v) = (c, ∅, ·).
  - FZ and Lemma G at k0 give (π_v^{k0} ∩ H) ⊔ A = ∅. So A = ∅ and v's whole k0-route is low.
  - WALK (c) from v0 = v gives B ⊆ ∅ = A, against (Σ6). ✓
  - C_k ⊆ F_k (H1), so no Ev vertex lies on C_k at all.
  - Diff with the RL-fixes CYC-EV (N-ENT-1): same conclusion, hypothesis (Σ) + rise instead of the ENT setting. The proof uses M_k ≤ L
    ((Σ4), inside RB), not M_k = L.
- TEV-FB.
  - The threat's play lies in F_k (H1; it avoids o). By CYC-EV an Ev vertex on it lies on the pre-c path, so i < N exists when the play
    meets Ev.
  - Step 1: f ∉ Ev by the choice of i, or because f = c. So f ∈ F_{k0} by (Σ3). An Odd e would have f as its k0-successor, inside R̄_{k0}.
    So e is Even. ✓
  - Step 2: FZ at f; P(Ξ_{k0} f) ⊆ F_{k0}; BF at e with b_k(e) = Ξ_k(f) (f = σ_k(e)). So (π_{u_e}^{k0} ∩ H) ⊔ A ⊆ F_{k0}, which forces
    π_{u_e} ∩ H = ∅ and o ∉ A.
    - o ∉ A gives o ∉ H in both cases. If rank o > rank c, then o ∈ P(θ_{k0}), so o ∉ H. Otherwise H ⊆ V_{>c} excludes o. ✓
  - Step 3: (P2) along o, p_0, …, p_i, none of which is c, then (C4) with o ∉ H, gives B = ({p_0, …, p_i} ∩ H) ∪ A ⊇ A. With B ≠ A,
    B ⊄ A. ✓
  - Step 4: e ∈ R_{k0} ∩ F_k, and its route after e is π_{u_e}^{k0}, which is low. WALK (c) gives B ⊆ A. Contradiction. ✓
- The packet's reading paragraph (TEV false at S4a states, tevlast_cex_n40) is a reading and is not signed. It agrees with my data: on
  tevlast_cex_n40 the rise after k0 is followed by no further fallback in S (§6), so no (Σ)-pair contains it.

## 5. Theorem ENT-X and the Corollaries: SIGN CONDITIONAL ON (P)
- ENT-X. EV+ (P-N5-RL §6) is stated in "THE ENT SETTING":
  - S is a scope run, and k0 < k are consecutive fallbacks with M_{k0} = M_k = L ≥ 0;
  - r > L on [k0+1, k];
  - there is a rise.
  This is (Σ) + rise + M_k = L, as the packet says. EV+'s conclusion "the σ_k-play of x_k meets Ev" is the negation of TEV-FB's. ✓
  - EV+'s status: SIGN CONDITIONAL ON (P) by both referees. Its chain: EV with RL-4's citation of the window gate's existence, then MERGE
    (c) at the finite level L, which is outside RL-2's ∞ case.
  - "Equivalently": by §1's last bullet, "no rise" is "COARSE_L(θ) constant on [k0, k]". ✓
- NJB-A. Suppose the interval is dirty.
  - PL (b) (R31 (f)): the first change j is an S4a step with lev(θ_j, θ_{j+1}) > M, so a rise at L = M.
  - Consecutive block fallbacks are consecutive fallbacks of S: a fallback g of S strictly between them has level ≤ M (CLS2 from f_i) and
    ≥ M (CLS2 to f_{i+1}), so g would be in the block.
  - With M_{f_i} = M_{f_{i+1}} = M, this is the ENT setting, which ENT-X excludes. ✓
- D1.
  - Fact R: r is non-increasing along S, including at the fallback transitions.
  - Three cases by r at f_i + 1 and at the later states of the interval.
  - Case 2 is clean by RDROP (R35 (a)): the first change of a dirty interval has r_j > M.
  - A straddling interval leaves r ≤ M at f_{i+1}, so every later interval of the block is in case 2.
  - So D_M ≤ 1. ✓
- PL-S″. PL (a) (R31 (f): N ≤ n_E(1 + D_M), every block of level ≥ 0) with D_M ≤ 1, summed over the ≤ n levels in {0, …, n − 1}. ✓
  - Level ∞ does not occur: FBW-S gives M_k ≤ max(r_k, −1) < ∞ under (h).
- (P) enters only through EV+. §1-§3 are unconditional, as the packet says.

## 6. Data (DATA, not proof)
- Batch (run_all.sh, logs/, totals_logs.txt): 295 𝒞^1O library files × 3 traces × 3 starts = 2,655 runs, 50,667 states; random 𝒞^1O
  (n 4-14 and 15-30): 22,000 own + 22,000 rand + 20,000 spec runs, 156,594 states. 893 / 893 logs end "RESULT OK violations=0"; there
  were no timeouts.
- (Σ)-pairs (library, own / rand / spec): 756 / 660 / 760, all without a rise. Per pair, every (Σ1)-(Σ6) fact held, including the
  equivalence "rise ⇔ B ≠ A" and COARSE_L(θ) constant across k0.
  - FZ: 19,672 / 17,389 / 19,821 vertices.
  - BF: 1,685 / 1,581 / 1,708, each with cycle node c and v off its successor's pre-c path.
  - RB: 1,025 / 931 / 1,035.
  - WALK (a), (b): 1,755 / 1,650 / 1,780; WALK (c) low-tail cases: 1,725 / 1,615 / 1,750.
  - 0 violations.
- On tev_cex_n40 my own trace gives 15 (Σ)-pairs, 16 RB and 19 WALK checks, the packet's §7 row. My BF count is 19 against the
  packet's 16 RB/BF: I count BF at every Even v ∈ R_{k0} ∩ F_k, and RB only when σ_{k0}(v) ∈ R̄_k.
- Controls.
  - In (Σ)-pairs WITHOUT a rise, the threat's play at k meets Ev 64 / 60 / 65 times. So TEV-FB's conclusion is not automatic in (Σ);
    the rise is what its proof uses. An Ev vertex on C_k never occurred without a rise either (0).
  - Mutation ENT_MUT=nor (the requirement r > L on [k0+1, k] dropped; own trace, 1 start per library file): 187 extra pairs, with 8
    violations of the no-leave fact (Σ3) on zcl_fb2_n32 and zcl_tp_n32 (experiments/si/xing/instances). The hypothesis carries NL's
    no-leave.
- Corollaries (library): 287 / 273 / 290 blocks of level ≥ 0, 1,013 / 792 / 1,015 intervals.
  - 698 / 601 / 701 intervals have r > M throughout, and all are clean (NJB-A).
  - 315 / 191 / 314 have r ≤ M from the start, and all are clean (RDROP).
  - Straddling intervals: 0. Dirty intervals: 0. So max D_M = 0, which is NJB itself on this data.
  - PL (a) and PL-S″ held: max block size 37 (= max fallbacks of level ≥ 0 per scope run), against 2·n·n_E.
  - Fallback levels never rose along a scope run (CLS2, rechecked).
- Climbs (run_climbs.sh, climb/, totals_climb.txt): four 1200 s climbs (FIT rise × 3 seeded with tevlast7_n32,
  tevlast_cex_n40 and tev_cex_n40; FIT blk seeded with tev_cex_n40; own and rand traces):
  - totals: 15,509 evaluations, 62,036 runs, 783,271 states, 0 violations;
  - 134,200 (Σ)-pairs, 122,272 of them with M_k = L, 0 with a rise;
  - FZ 3,381,651, BF 253,292, RB 179,506 and WALK 313,814 checks;
  - 42,461 blocks and 123,553 intervals: 122,272 with r > M throughout and 1,281 with r ≤ M from the start, all clean; 0 straddling;
    max D_M 0;
  - the threat meets Ev in a rise-free (Σ)-pair 2,384 times (control as above);
  - the climbs plateau at 4 rises per instance. Climbs are not families.
- Additional record: rise_end.py (above).

## 7. Notes for the lane (none blocks a signature)
- N-ENT-1: CYC-EV here generalises the RL-fixes CYC-EV (hypothesis without M_k = L). Say so in the RESULTS entry, so that the two
  signed statements are not read as different results.
- N-ENT-2: §7's "vacuous hypotheses everywhere" overstates the case for NJB-A / D1 / PL-S″. Their hypotheses (blocks and intervals with
  r > M) occur, and the data confirm them. Only the dirty / ENT case is unreached.
- N-ENT-3: §0's status of REFEREE-2's R2-N5-RL is stale (report 30dc5f54, §C 88571b03, Addendum A db9d66a8).

## §C. Comparison with REFEREE's R-N5-ENT (written 2026-10-25 14:36Z by date -u, after my report b7df84b8 was pushed)
Read: docs/referee/R-N5-ENT.md as on trunk (55a3f6f; 90 lines, no §C yet). No ENT fixes file exists yet (`ls docs/si | grep -i ent-fix`
is empty).
### C.1 Verdicts
They are identical:
- FZ, BF, RB, WALK (a)-(c), CYC-EV and TEV-FB: SIGN, with no (P);
- ENT-X, NJB-A, D1 and PL-S″: SIGN CONDITIONAL ON (P), with (P) entering only through EV+;
- §6 not signed.
No gap in either report, so the joint gap map is empty. Both reports name the same premises (R15, R19, R29, R31, R35) and EV+'s chain
EV ⇐ FREE-FREEZE ⇐ BL (c) ⇐ (P). Both note that TEV-RED is not used, and that with P1 landed §4-§5 become unconditional.
### C.2 Notes map
| REFEREE | REFEREE-2 | content | status |
| --- | --- | --- | --- |
| §2 "It uses a rise and (Σ4) only. It does not use M_k = L"; §1 "RB is the step that needs k to be a fallback state, through (Σ4)" | N-ENT-1 | CYC-EV / TEV-FB need (Σ) + rise, not M_k = L; so ENT's CYC-EV implies the RL-fixes CYC-EV | same content. REFEREE says it of TEV-FB, I say it of CYC-EV, and both proofs use M_k ≤ L only in RB. Agreed |
| §4 thin spot: "CYC-EV, TEV-FB, ENT-X and §5 have vacuous hypotheses in data" | N-ENT-2 | for §5 this is too strong: NJB-A's hypothesis (intervals with r > M throughout) occurs and holds (698 / 601 / 701 library; 122,272 climb), and D1's and PL-S″'s objects (blocks) occur (287 / 273 / 290). Only the dirty case, i.e. the ENT setting, is unreached | a wording difference, not a verdict. I keep N-ENT-2 as a note for the RESULTS entry's DATA line |
| — | N-ENT-3 | §0's REFEREE-2 status is stale | mine only (status) |
| §3 "There is no circularity: TEV-FB does not use EV+ or any (P) item" | §5 "(P) enters only through EV+. §1-§3 are unconditional" | the same point | agreed |
| disclosure: §1-§3 seen before as the RL fixes source (R-N5-RL Addendum A2) | (none) | independence | noted. My predecessor's R2-N5-RL Addendum A checked the RL-fixes CYC-EV. I re-checked the ENT text on its own (§2-§4) and diffed the two statements (N-ENT-1) |
### C.3 Data, side by side (DATA, not proof)
- tev_cex_n40, on independent engines: REFEREE 15 (Σ)-pairs, FZ 414, BF 19, RB 16, WALK 19; mine (own trace) 15 / 414 / 19 / 16 / 19.
  The counts are identical, and we explain the packet's single "RB / BF" column the same way (it counts RB).
- Both reports, and the lane: no (Σ)-pair with a rise anywhere.
- Mine only:
  - every rise after a fallback with r > L (62 library, 26,665 climb) is followed by NO further fallback of its scope run;
  - rise_end.py's breakdown of how S ends;
  - the control "without a rise, x_k's play meets Ev" (64 / 60 / 65);
  - the ENT_MUT=nor control.
  These are DATA only. The first suggests an unconditional route to "(Σ) + rise is empty", if someone can prove it.
### C.4 Joint state
All ten signable statements are signed by both referees (Opus 5.5, D15): six unconditional, four CONDITIONAL ON (P). No gap. Notes for
L-SI: N-ENT-1, N-ENT-2, N-ENT-3 (none blocks a signature).
### C.5 Addendum (written 2026-10-25 15:34Z by date -u): REFEREE's §C, and R36
- REFEREE's §C is now on origin/claude/referee (d6b8aef9; section "§C. Comparison with REFEREE-2", written 14:33Z). It agrees on the
  verdicts and gives an empty joint gap map.
  - It accepts N-ENT-1, N-ENT-2 and N-ENT-3.
  - On N-ENT-2 it corrects its own §4 to "vacuous only for CYC-EV, TEV-FB and ENT-X" and counts 654 clean (Σ)-pairs in its data. That
    removes the one wording difference of C.2.
  - Nothing in it changes my verdicts.
- Does RESULTS R36 lift CONDITIONAL ON (P)? Yes, for ENT-X, NJB-A, D1 and PL-S″.
  - Their only use of (P) is EV+ ⇐ EV ⇐ FREE-FREEZE ⇐ BL (c), and BL (c) applies (P) to the one-player game G_τ[F_k].
  - R36 (d) states Lemma P1 exactly for G[X], G_τ and G_τ[F_k] (RESULTS, R36 (d), "Hypothesis match").
  - EV+ has landed in R37.
  - So, with R36 and R37 landed, the four statements are signed without condition by me (Opus 5.5, D15). REFEREE's §C says the same.
  - No running-time bound follows; G-N5-TIME stays OPEN.
