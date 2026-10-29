# N5-VC (box 50): VC dimension of the visited strategy families. Theorem VC-BOUND (a hypothesis-free reduction); CONJECTURE VC-N5
L-NEW successor 31 (Opus 5.5; D14, D18, Lead reading L40). Lead's brief 2026-10-29 09:59Z, BOX 50: «one NOVEL route to SEG-RUN or to a
reader-proof replacement for G in REL-SPLIT. Bring in one tool from an area not yet used on N5 in this repo ... State in one line the exact
N5 object it would bound, test that statement on data ... BEFORE writing a proof, and kill it yourself if the data says so.»
This is a working note. It is unrefereed and not frozen, and it is not a TARGET.md claim. Nothing here bounds N5's running time, so G-N5-TIME stays OPEN.
Labels: PROVED (lane) / CONJECTURE / OPEN / DATA / ASSUMPTION / READING / DEAD. Counts are TRANSITIONS (iterations).
Tools: experiments/new/box50/ (vcrun.py measures; vcclimb.py kill search). Outputs: box50/*.txt, box50/out/.

## 0. The tool, and why it is new here
- Tool: the Vapnik-Chervonenkis dimension of a set system and the Sauer-Shelah lemma (learning theory / extremal set theory).
- Novelty check (2026-10-29 10:0xZ): `grep -rli "VC.dim\|shatter"` over docs/new, docs/si and docs/lit returns 0 files. Sperner/LYM, submodularity and
  order dimension also return 0. The other candidates in the brief are already used here: USO (docs/lit/T28 §5, N8d), Tarski (T28 §9),
  tropical (T28 §7, N9, N5-READER §3), matroid (N5-READER §3 reading), discounted-MDP / Post-Ye (L-SI N5-OR-lens, N1).
- One-line N5 object: **dσ := the VC dimension of F_σ := {σ_t : t a state of the N5 execution}, each σ_t read as its set of Even edges
  (v, σ_t(v)) (and dτ for τ on Odd edges); the claim is dσ, dτ = O(1), which by Sauer-Shelah bounds the number of iterations by
  O(m^{dσ} + m^{dτ}).** The same for one run or one phase (F_σ(S) := {σ_t : t ∈ S}).
- How it replaces G and SEG: it needs no REL-SPLIT, no (H4′_rel) and no GEN_W. It counts STRATEGIES, not σ̄-changes. So readers (Odd, no predecessors)
  and Even anchors that never leave their loop cannot raise dσ: on a SAME run they add no σ-coordinate that varies (§3 DATA: rdr_K10 and
  anc_K10 have dσ = 3 = runfam_K10's, while the σ̄-family's VC goes 1 → 4).

## 1. Definitions
- E_σ := {(v, w) ∈ E : v Even, |succ(v)| ≥ 2}; σ ↦ σ^E := {(v, σ(v)) : v Even, |succ(v)| ≥ 2} ⊆ E_σ (injective on Even strategies,
  vertices of out-degree 1 have one strategy). The same with Odd for τ.
- For a family F of subsets of a ground set X and A ⊆ X: F|_A := {S ∩ A : S ∈ F}; A is SHATTERED by F if |F|_A| = 2^{|A|}; VC(F) := max
  |A| over shattered A (∅ is always shattered if F ≠ ∅). Φ_d(m) := Σ_{i=0}^{d} C(m, i) ≤ (em/d)^d.
- m(F) := |{x ∈ X : x lies in some but not all members of F}| (the varying ground set).

## 2. PROVED (lane)
- Lemma SS (Sauer-Shelah, Pajor's form; proof given here, not cited as a premise). Every finite family F on a finite X shatters at least |F|
  subsets of X. Hence |F| ≤ Φ_{VC(F)}(m(F)).
  Proof. Induction on |X|. |X| = 0: F ⊆ {∅}, and ∅ is shattered when F ≠ ∅. Step: fix x ∈ X; F0 := {S ∖ {x} : S ∈ F}, F1 := {S ∈ F : x ∉ S,
  S ∪ {x} ∈ F}, both families on X ∖ {x}; |F| = |F0| + |F1| (the map S ↦ S ∖ {x} is 2-to-1 exactly on the pairs counted by F1). If T ⊆ X ∖ {x} is
  shattered by F0, it is shattered by F. If T is shattered by F1, then T ∪ {x} is shattered by F (for B ⊆ T, both S and S ∪ {x} with S ∩ T = B
  are in F). The sets of the first kind avoid x, those of the second contain it, so F shatters at least sh(F0) + sh(F1) ≥ |F0| + |F1| = |F|
  sets. For the bound: every shattered set lies in the varying ground set (a set containing an element in all or in no member is not
  shattered), and has size ≤ VC(F). □
- Theorem VC-BOUND (every game, every start). Let I be the number of N5 iterations (SPEC S4) and F_σ, F_τ the families of Even / Odd
  strategies over all states of the execution. Then I ≤ |F_σ| + |F_τ| − 2 ≤ Φ_{dσ}(m_σ) + Φ_{dτ}(m_τ) − 2, with dσ := VC(F_σ^E), m_σ :=
  m(F_σ^E), and dτ, m_τ the same for τ. The same holds per phase P (τ constant): len(P) ≤ |F_σ(P)| − 1 ≤ Φ_{dσ(P)}(m_σ(P)) − 1, and per run.
  Proof. RESULTS R15 (d) (landed): «N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ to
  Odd's τ (on G^d), and changes at least one of them». RESULTS R15 (c): «every non-empty switch of improvements goes strictly up in ≺».
  So along the execution σ stays the same or moves strictly up in the strict partial order ≺. Its values are therefore pairwise distinct
  and each one occupies a single block of consecutive states, and the number of σ-changing iterations is |F_σ| − 1. Likewise for τ on G^d.
  Every iteration is counted at least once, so I ≤ (|F_σ| − 1) + (|F_τ| − 1). Lemma SS gives the rest (σ ↦ σ^E is injective).
  Per phase: τ is constant on a phase, and RESULTS R80 (a) (EVERY-SWITCH): «every transition of a phase changes Even's σ», so
  len(P) = |F_σ(P)| − 1. For a run S, which is a stretch of one phase, the same holds. □
- Corollary (two-sided). (a) If dσ, dτ ≤ c on a class, N5 makes ≤ 2Φ_c(m) = O(m^c) iterations there (POLYNOMIAL for fixed c).
  (b) Conversely, a shattered set A needs 2^{|A|} distinct members, so dσ ≤ log2 |F_σ| ≤ log2(I + 1). So if N5 makes ≤ p(n) iterations,
  then dσ, dτ ≤ log2(p(n) + 1) = O(log n). (c) If dσ, dτ = O(log n), N5 makes m^{O(log n)} iterations (quasi-polynomial).
  READING: so up to quasi-polynomial factors, the VC dimension of the visited strategy family IS the N5 iteration question. A
  constant bound is a sufficient strengthening. Any exponential family for N5 must make dσ or dτ grow like n^{Ω(1)}/log m, i.e. it must
  run a binary counter on many σ- (or τ-) edges (a shattered set).
- Lemma ENT (elementary). If along the time-ordered states of a stretch every edge of A enters σ^E at most k times, then |F|_A| ≤ 1 + 2k|A|,
  so 2^{VC} ≤ 1 + 2k·VC. Also the stretch has at most Σ_e ENT(e) transitions (each transition switches some Even vertex, i.e. some edge enters).
  Proof: restricted to A, the trace changes only when an edge of A enters or leaves, at most 2k|A| times. The count: every in-phase S4a
  transition changes σ (EVERY-SWITCH, RESULTS R80 (a)), and a switch at v is an entry of the edge (v, σ_{t+1}(v)). □
  So a per-edge entry bound gives a LINEAR-in-m run bound directly. VC-N5 is strictly weaker, since it allows edges that re-enter
  without bound as long as no 2^d patterns appear on d edges.

## 3. DATA (experiments/new/box50/vcrun.py; engine n5x via L-SI's experiments/si/root/common.rows, read-only)
Per scope: run = maximal fallback-free stretch of a phase; phase = (λ_Ξ, τ) constant; exec = the whole execution. "VC" is VC({σ_t}^E) on
the scope. dσ / dτ are the whole-execution VCs of the σ- and τ-families. "VCbar" is the same for σ̄ (Odd's best replies; NOT reader-proof).
ENT is the most entries of one Even edge into σ (the first state counts as an entry). VC-BOUND is checked per execution (VCB_V). The script
also checks that σ never repeats except across τ-only iterations (SIG_REPEAT, TAU_REPEAT, and run_REPEAT / phase_REPEAT by
EVERY-SWITCH) and checks Sauer's inequality per scope. "VC PASS" means none of these fired.
| corpus (log) | executions / phases / runs | run VC max | phase VC max | dσ max | dτ max | run ENT max | VC-BOUND violations | longest run / phase / exec |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alt_all, default starts (vc_alt.txt) | 407 / 454 / 745 | 3 | 4 | 4 | 4 | 4 | 0 | 68 / 112 / 115 |
| alt_all, pinned starts (vc_alt_start.txt) | 410 / 457 / 921 | 3 | 4 | 4 | 4 | 4 | 0 | 71 / 121 / 122 |
| 2,000 seeded random games, n 8-40 (vc_rand.txt, `--rand 2000 50`) | 1,973 / 372 / 303 | 2 | 2 | 2 | 2 | 1 | 0 | 3 / 3 / 10 |
- Scaling families (families.txt). These are the only data that speak to O(1) against O(log n), because VC ≤ log2(len + 1) always:
  | family | run lengths | run VC | dσ |
  | --- | --- | --- | --- |
  | runfam_K10, K20, K40, K60, K100 (L-SI RUN-LIN killer family, n 49-139) | 99, 124, 171, 211, 291 | 3, 3, 3, 3, 3 | 3 |
  | ladderd0_k12, k24, k48 (L-RED; one Even vertex switches 48 times in one segment) | 13, 25, 49 | 1, 1, 1 | 1 |
  | cxmig_k4, k8, k16 | 12, 16, 24 | 2, 2, 2 | 2 |
  | Oink counter_symsi N = 2..12, 16, 20 (whole executions 13..94 iterations) | | | 2, 2, 3, 3, 3, 3; 3, 3 |
  | Oink counter_rob N = 2..12; counter_core, counter_ortl, counter_dp, counter_m N = 2..12 | | | 2, 2, 3, 3, 3, 3; all 1 |
  (oink_small.txt, oink_big.txt; games from tools/oink/build generators at the pinned 8fbf0a7, default S3 start.)
- Reader-proofness (DATA, as §0 predicts): runfam_K10 / rdr_K10 (+ 25 Odd readers) / anc_K10 (+ 25 Even anchors), the same run of 99:
  dσ = 3, 3, 3; σ̄-family VC (run) 1, 4, 4; dτ 0, 1, 1 (the readers' τ changes once). G was 9 → 91 on the same instances (GRUN §3).
- MUT control (vc_mut_K10.txt: a d-set counts as shattered at 2^d − 1 traces): exec VC 3 → 4 on runfam_K10. The control bites.
- Two engines on the climbed pins (§4): L-SI's root/n5bcmp.py (L-COMP's n5b, SPEC mode) gives state sequences identical to n5x on
  vpf3_vc4 and ent1_vc6, with the start written by box50/mkstart.py (the S3 start).
- How loose Sauer is here: on long121_n40 the execution has 122 iterations against the bound Φ_4(95) + Φ_dτ − 2 = 3,326,524. On xsn91_n48,
  115 against 14,901,219. VC-BOUND is a polynomial REDUCTION, not a good estimate.

## 4. Kill search (box50/vcclimb.py; mutations: L-SI runlin/growclimb.py clone + box43 climb.mutate, read-only; logs out/*.log)
Score: 100·VC + SH, where SH = the most traces on a (VC + 1)-set extending a shattered VC-set, plus a tie count. SCOPE=exec uses the
execution's joint (σ, τ) family. SCOPE=ent uses run ENT.
| climb | seed | NMAX | steps | result |
| --- | --- | --- | --- | --- |
| vk10 (run VC) | runfam_K10 | 64 | 3,000 | VC 3 (no gain) |
| vpf, vpf2, vpf3 (run VC) | pftheta34_n32 | 48 | 3,000 / stopped by me (last gain at step 429) / 20,000 | 3, 3, **4** (vpf3_vc4, n 48, run [5, 27] of 22, step ~5,600); 5-sets reach 22 of 32 traces |
| vpf4 (run VC) | vpf3_best | 96 | running at writing | 4, 5-sets 22.8 of 32 |
| vsym, vsym2 (exec joint VC) | counter_symsi_6 | 80 / 120 | 3,000 / running | 4 (vsym_vc4, n 80); 5-sets 24 of 32 |
| ent1, ent2 (run ENT) | pftheta34_n32, ent1_best | 48 / 96 | 20,000 each | **ENT 6** (ent1_vc6, n 48, run [1, 18] of 17; run VC 3), ENT 6 at n 96 (no gain) |
- DEAD: CONJECTURE VC-RUN with the library constant (run VC ≤ 3). Killed by box50/out/vpf3_vc4.pg (n 48, sha1 1aef63fe…; .start = S3 start):
  the run [5, 27] shatters {(7, 20), (8, 0), (20, 19), (39, 32)}. It is two-engine (§3). The O(1) form survives (no 5 at n ≤ 96 / 120).
- DEAD: ENT-RUN with the library constant 4. Killed by box50/out/ent1_vc6.pg (n 48, sha1 129e9df1…): Even vertex 24's successor along the run
  [1, 18] is 20, 11, 11, 20, 14, 14, 20, 22, 22, 20, 11, 11, 20, 14, 14, 20, 20, 20. The edge (24, 20) is entered 6 times (and so are 5 clones
  of 24), and the run's VC is 3. Obstruction: a vertex can return to a hub option after every detour, in a lap that repeats inside one run.
- Anatomy (vpf3_vc4, READING): the run [5, 27] repeats a LAP. The Even switches of transitions 7-12 recur at 20-27: 7: 20 ↔ 21; 21: 7 ↔ 26;
  20: 19 ↔ 7; 26, 39, 45: 6 → 32; 27, 32, 35, 44: 6 → 15. The stretch 13-19 between the laps differs, and the strategies never repeat. The
  4-shattering is made by two laps of oscillating vertices with different phases plus the in-between stretch. Laps inside one
  fallback-free run are where a counter would have to live: k laps nested inside each other would shatter about k edges.

## 5. What a proof would need (READING)
- Per run, by Lemma ENT, VC ≤ max{d : 2^d ≤ 1 + 2·ENT·d}, so a constant ENT bound would give constant VC AND |S| ≤ ENT·m directly.
  But ENT grows under climbs (4 → 6). VC is the weaker target: it allows unbounded returns as long as they are not independently scheduled.
- A proof of VC = O(1) would have to show that oscillations of different Even vertices inside one run (or phase) are not INDEPENDENT. A
  2^d pattern needs d oscillators whose relative phases run through every combination. The lemmas in hand (W-STICK, H-STICK, SINK-STEP,
  RESULTS R83) constrain final switches inside one REL segment. They say nothing about returns across segments, which is where the
  laps of vpf3_vc4 and ent1_vc6 sit.
- Disjoint unions (READING, one test): if a fallback-free component could toggle an edge with any prescribed schedule of length L, a
  union of log L such components would shatter log L edges. That would give VC = Θ(log n) with polynomial N5. VC-N5 would then be false
  while N5 stays polynomial, and the route would give only a quasi-polynomial bound. The one union tested (vpf3_vc4 ⊎ ent1_vc6,
  box50/dunion.py) had run VC 4, i.e. it did not add. A union keeps lockstep only while every component is fallback-free with τ fixed; a
  fallback in one component waits for the other (S4c fires only when both are stuck). So unions are not free products under N5. OPEN.
- So the honest status: VC-BOUND turns the iteration question into a question about the VC dimension of the visited strategy family,
  exactly up to quasi-polynomial factors (Corollary (b), (c)). The constant form is CONJECTURE VC-N5 / VC-RUN, OPEN with DATA ≤ 4. The log form
  is necessary for polynomial N5 and sufficient only for quasi-polynomial.

## DONE / FINDINGS / NEEDS
- DONE: this note; tools experiments/new/box50/ (vcrun.py, vcclimb.py, dunion.py, mkstart.py); logs vc_alt.txt, vc_alt_start.txt,
  vc_rand.txt, vc_mut_K10.txt, families.txt, oink_small.txt, oink_big.txt, out/*.log; pins out/vpf3_vc4.{pg,start}, out/ent1_vc6.{pg,start}
  (plus out/vsym_vc4.pg and the climbs' _best / _last files); experiments/new/check.sh block "Box 50".
- FINDINGS: (1) PROVED (lane) Theorem VC-BOUND: I ≤ Φ_dσ(m_σ) + Φ_dτ(m_τ) − 2 on every game (R15 (c), (d) + Lemma SS, proof given),
  len(P) ≤ Φ_dσ(P)(m) − 1 per phase (R80 (a)). Conversely dσ, dτ ≤ log2(I + 1). It is reader-proof and needs no REL-SPLIT hypotheses. A reduction.
  (2) CONJECTURE VC-N5 (dσ, dτ = O(1)), which would make N5 polynomial: OPEN. DATA: ≤ 3 per run, ≤ 4 per phase and execution on 817 library
  executions and 2,000 random games; flat on every scaling family; climbs reach 4 (run) and 4 (exec), no 5. (3) DEAD: run VC ≤ 3
  (vpf3_vc4) and ENT-RUN ≤ 4 (ent1_vc6: one edge entered 6 times in a run of 17, a repeated lap). (4) READING: the data cannot
  separate O(1) from O(log n), and the log form gives only quasi-polynomial.
- NEEDS: none from the owner.
