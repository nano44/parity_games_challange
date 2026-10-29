# Packet P-N5-VC (box 50): the number of N5 iterations is bounded by the VC dimensions of the visited strategy families (Theorem VC-BOUND, Sauer-Shelah), and conversely — every game
L-NEW successor 31 (Opus 5.5), D14 / D18, Lead reading L40. Lead's word 2026-10-29 11:19Z (message to L-NEW): «(a) Yes: freeze P-N5-VC with
your proposed RESULTS line, exactly as worded, plus these: - every symbol defined from SPEC / RESULTS (F_σ as sets of Even edges, m_σ, Φ_d);
- Sauer–Shelah proved in the packet (Pajor's form), no outside premise; - R15 (c), (d) and R80 (a) quoted with line numbers and a quote
check; - the converse dσ ≤ log2(I+1) proved; - the pinned VC-BOUND check with its expected output.» Written 2026-10-29 from 11:25Z (date -u).
FROZEN at push: later text goes into a fixes file.
What this is and is not, plainly:
- It is a REDUCTION. It bounds N5's iteration count by a polynomial in m whose degree is the VC dimension of the family of strategies
  that N5 visits, and it bounds that VC dimension by log2 of the iteration count. It does NOT bound the VC dimension. CONJECTURE VC-N5
  (dσ, dτ = O(1)) is OPEN.
- Not a TARGET.md claim; no running-time bound; G-N5-TIME stays open.
Labels: PROVED (L-NEW 31, unrefereed) / DATA / CONJECTURE / DEAD.
Source: docs/new/N5-VC-box50.md (working note). This packet governs.
Tools: experiments/new/box50/vcrun.py (counters, §3), vcclimb.py (kill search), mkstart.py, laps.py; logs experiments/new/box50/*.txt, out/.

## Proposed RESULTS line (as sent to the Lead 11:16:53Z, verbatim)
"N5 on every game: iterations I ≤ Φ_dσ(m_σ) + Φ_dτ(m_τ) − 2 with dσ, dτ the VC dimensions of the visited Even / Odd strategy families
(Theorem VC-BOUND; R15 (c), (d) + Sauer–Shelah, proof included), len(P) ≤ Φ_dσ(P)(m) − 1 per phase, and conversely dσ, dτ ≤ log2(I + 1):
a reduction; CONJECTURE VC-N5 (dσ, dτ = O(1)) OPEN."

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Lemma SS (Sauer-Shelah in Pajor's form) and Corollary SAUER | PROVED (to sign; elementary, self-contained) |
| §2 | Theorem VC-BOUND (a) execution, (b) phase / run, (c) converse | PROVED (to sign) |
| §2 | Corollary RANGE (polynomial / quasi-polynomial / necessity) | PROVED (to sign; arithmetic from §1-§2) |
| §3 | data, the pinned check | DATA (not to sign) |
| §4 | VC-N5; run VC ≤ 3 and ENT-RUN ≤ 4 | CONJECTURE (open), DEAD (not to sign; instances) |
- Premises (LANDED; quoted at trunk e3b435ab; checked by experiments/new/box49/quotecheck3.py, §3):
  - SPEC iteration: [Q docs/new/N5-ssi-global.md@e3b435ab:50] «S4 Iteration (one iteration = one pass with Iσ ∪ Iτ ≠ ∅; both steps computed from the SAME (σ, τ), applied together)»
  - SPEC S4c: [Q docs/new/N5-ssi-global.md@e3b435ab:56] «c. FALLBACK, if σ_new = σ and τ_new = τ»
  - RESULTS R15 (c): [Q docs/RESULTS.md@e3b435ab:637-639] «≺ is a strict partial order on strategies and every non-empty switch of improvements goes strictly up in ≺. Consequence: no strategy repeats in any VJ00 strategy-improvement run with any non-empty selection rule»
  - RESULTS R15 (d): [Q docs/RESULTS.md@e3b435ab:640-641] «(d) N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and changes at least one of them»
  - RESULTS R80 (a): [Q docs/RESULTS.md@e3b435ab:4405] «N5 on EVERY game, inside one phase: every transition of a phase changes Even's σ (Lemma EVERY-SWITCH)»
  - Phases: a phase is a maximal stretch of consecutive states on which λ_Ξ and τ are constant (the KEY of RESULTS R38 (a); λ_Ξ constant
    on a phase by definition, P-N5-OFFMONO-fixes F1). A run is a maximal stretch of a phase with no fallback transition inside it.

## 0. Definitions
- G = (V, E, Ω, owner) as in SPEC; Even = owner 0. E_σ := {(v, w) ∈ E : v Even, v has ≥ 2 distinct successors}; E_τ the same for Odd.
- For an Even strategy σ: σ^E := {(v, σ(v)) : v Even with ≥ 2 distinct successors} ⊆ E_σ. The map σ ↦ σ^E is injective (an Even vertex with
  one successor has one choice). τ^E ⊆ E_τ likewise.
- The execution: states 0, 1, …, I, with (σ_k, τ_k) the pair at state k (state 0 = the start, SPEC S3 or a given pair; state I = the
  stop, S5). I = the number of iterations (SPEC S4: «one iteration = one pass with Iσ ∪ Iτ ≠ ∅»).
- F_σ := {σ_k^E : 0 ≤ k ≤ I}, a family of subsets of E_σ; F_τ := {τ_k^E : 0 ≤ k ≤ I} ⊆ 2^{E_τ}. For a phase P (states a..b),
  F_σ(P) := {σ_k^E : a ≤ k ≤ b}; for a run S likewise; len(P) := b − a (transitions).
- For a family F of subsets of a finite set X: for A ⊆ X, F|_A := {S ∩ A : S ∈ F}; A is SHATTERED by F if |F|_A| = 2^{|A|}; sh(F) := the
  number of subsets of X shattered by F; VC(F) := max{|A| : A shattered} (VC(F) := −1 for F = ∅; for F ≠ ∅, ∅ is shattered, so VC ≥ 0).
- m(F) := |{x ∈ X : x lies in some but not every member of F}| (the varying ground set). dσ := VC(F_σ), m_σ := m(F_σ); dτ, m_τ likewise;
  dσ(P) := VC(F_σ(P)), m_σ(P) := m(F_σ(P)).
- Φ_d(m) := Σ_{i=0}^{d} C(m, i) for integers d ≥ 0, m ≥ 0 (C(m, i) = 0 for i > m; so Φ_d(m) = 2^m when d ≥ m). Φ_d(m) ≤ (m + 1)^d.

## 1. Lemma SS (Sauer-Shelah, Pajor's form; PROVED here, no outside premise)
Lemma SS. For every finite set X and every family F ⊆ 2^X: sh(F) ≥ |F|.
Proof. Induction on |X|. If X = ∅, then F ⊆ {∅}; if F = {∅}, ∅ is shattered (F|_∅ = {∅}, 2^0 = 1), so sh(F) = 1 = |F|; if F = ∅,
sh(F) = 0 = |F|. Let |X| ≥ 1, fix x ∈ X, X′ := X ∖ {x}, and put F0 := {S ∖ {x} : S ∈ F} and F1 := {S ∈ F : x ∉ S and S ∪ {x} ∈ F},
both families of subsets of X′.
- |F| = |F0| + |F1|: the map S ↦ S ∖ {x} sends F onto F0. The preimage of T ∈ F0 is {T, T ∪ {x}} ∩ F, which has two members exactly when
  T ∈ F1 and one otherwise.
- If T ⊆ X′ is shattered by F0, it is shattered by F. For B ⊆ T take S′ ∈ F0 with S′ ∩ T = B and S ∈ F with S ∖ {x} = S′. Since x ∉ T,
  S ∩ T = S′ ∩ T = B.
- If T ⊆ X′ is shattered by F1, then T ∪ {x} is shattered by F. For B ⊆ T ∪ {x} take S ∈ F1 with S ∩ T = B ∖ {x}. Both S and S ∪ {x}
  are in F, and S ∩ (T ∪ {x}) = B ∖ {x}, (S ∪ {x}) ∩ (T ∪ {x}) = (B ∖ {x}) ∪ {x}. One of the two equals B.
- The sets of the second kind contain x and those of the first kind do not, so they are distinct. By induction (|X′| < |X|),
  sh(F) ≥ sh(F0) + sh(F1) ≥ |F0| + |F1| = |F|. □
Corollary SAUER. If F ≠ ∅, |F| ≤ Φ_{VC(F)}(m(F)).
Proof. Let A be shattered. If x ∈ A lay in every member of F, every trace would contain x, so the trace A ∖ {x} would be missing. If x lay in
no member, the trace A would be missing. So A ⊆ X_var, the varying ground set (|X_var| = m(F)), and |A| ≤ VC(F). The shattered sets are
therefore among the subsets of X_var of size ≤ VC(F), of which there are Φ_{VC(F)}(m(F)). Lemma SS gives |F| ≤ sh(F) ≤ Φ_{VC(F)}(m(F)). □

## 2. Theorem VC-BOUND (PROVED, every game, every start)
(a) I ≤ (|F_σ| − 1) + (|F_τ| − 1) ≤ Φ_dσ(m_σ) + Φ_dτ(m_τ) − 2.
(b) For every phase P: len(P) = |F_σ(P)| − 1 ≤ Φ_dσ(P)(m_σ(P)) − 1; the same for every run S (len(S) = |F_σ(S)| − 1).
(c) Converse: dσ ≤ log2 |F_σ| ≤ log2(I + 1), dτ ≤ log2(I + 1), and dσ(P) ≤ log2(len(P) + 1) for every phase P.
Proof. (a) By R15 (d) every iteration applies a switch Switch_I with ∅ ≠ I ⊆ Iσ to σ and/or one with ∅ ≠ I ⊆ Iτ to τ, and changes
at least one of them. By R15 (c) a non-empty switch of improvements goes strictly up in the strict partial order ≺ (on G for σ, on G^d for
τ). So along the execution σ either stays the same or moves strictly up in ≺. Every move is strictly up and ≺ is a strict partial order
(transitive, irreflexive), so no σ-value can recur after it has been left. The states with a given σ-value therefore form one block of
consecutive states. Hence the number of transitions k → k + 1 with σ_{k+1} ≠ σ_k equals (number of distinct σ-values) − 1 = |F_σ| − 1,
using that σ ↦ σ^E is injective. The same holds for τ with |F_τ| − 1. Every iteration changes σ or τ (R15 (d)), so
I ≤ (|F_σ| − 1) + (|F_τ| − 1). Corollary SAUER (F_σ, F_τ ≠ ∅: state 0 exists) gives the second inequality.
(b) τ is constant on P (definition of a phase), and every transition of P changes σ (R80 (a)). With (a)'s block property, σ_a, …, σ_b are
pairwise distinct, so |F_σ(P)| = b − a + 1 = len(P) + 1. Corollary SAUER on F_σ(P). A run is a stretch of one phase, so the same
argument applies.
(c) If A is shattered by F, the 2^{|A|} traces S ∩ A (S ∈ F) are pairwise distinct, so |F| ≥ 2^{|A|} and VC(F) ≤ log2 |F|.
|F_σ| ≤ I + 1 because there are I + 1 states; likewise for F_τ and for F_σ(P) (|F_σ(P)| = len(P) + 1). □
Corollary RANGE (PROVED; arithmetic). Write d := max(dσ, dτ) and m := |E|.
- (i) If d ≤ c on a class of games, then I ≤ 2Φ_c(m) − 2 ≤ 2(m + 1)^c there. This is polynomial for fixed c.
- (ii) If d ≤ c·log2(n + 1), then I ≤ 2(m + 1)^{c·log2(n + 1)}, which is quasi-polynomial.
- (iii) If I ≤ p(n) on a class, then d ≤ log2(p(n) + 1) there. So polynomial N5 forces d = O(log n).
- (iv) An exponential family for N5, I ≥ 2^{n^ε}, has d ≥ n^ε / log2(m + 1) − 1 by (a), since 2^{n^ε} ≤ 2(m + 1)^d.
So d determines the order of I up to quasi-polynomial factors. The bounded form of d is sufficient for polynomiality; the logarithmic
form is necessary.
Remarks (not to sign). (1) VC-BOUND uses none of R82 / R83's hypotheses ((H4′_rel), GEN_W) and no REL-SPLIT. (2) READER-PROOF on SAME
runs: a reader (an Odd vertex without predecessors) adds no Even edge, and an Even anchor that never leaves its loop adds an edge
present in every member of F_σ; neither is in the varying ground set, so neither changes dσ. An Odd reader can change dτ if its τ moves.

## 3. DATA (not to sign) and the pinned check
- Counters (box50/vcrun.py): per run, phase, execution: VC of the σ-family; Sauer's inequality (SAUER_V); the identity of (b) (run_REPEAT,
  phase_REPEAT); σ- and τ-blocks of (a) (SIG_REPEAT, TAU_REPEAT); the inequality of (a) (VCB_V). "VC PASS" iff none fired.
  | corpus (log) | executions / phases / runs | run VC max | phase VC max | dσ max | dτ max | VC-BOUND violations |
  | --- | --- | --- | --- | --- | --- | --- |
  | alt_all, default starts (box50/vc_alt.txt) | 407 / 454 / 745 | 3 | 4 | 4 | 4 | 0 |
  | alt_all, pinned starts (box50/vc_alt_start.txt) | 410 / 457 / 921 | 3 | 4 | 4 | 4 | 0 |
  | 2,000 seeded random games n 8-40 (box50/vc_rand.txt) | 1,973 / 372 / 303 | 2 | 2 | 2 | 2 | 0 |
  Scaling families (box50/families.txt, oink_small.txt, oink_big.txt): runfam_K10..K100 (runs 99..291) run VC 3, 3, 3, 3, 3;
  ladderd0_k12/k24/k48 1; cxmig_k4/k8/k16 2; Oink counter_symsi N = 2..12, 16, 20 dσ ≤ 3; counter_rob N = 2..12 ≤ 3; counter_core / ortl
  / dp / m N = 2..12 1. Reader-proofness: runfam_K10 / rdr_K10 / anc_K10 dσ 3 / 3 / 3, run VC of σ̄ 1 / 4 / 4.
- Pinned check: experiments/new/check.sh, block "Box 50" (run by scripts/verify.sh). Expected output line:
  «box 50 VC: VC-BOUND 0 violations, runfam_K10 / anc_K10 dsig 3 (VCbar 1 -> 4), MUT bites, pins vpf3_vc4 (run VC 4) and ent1_vc6 (ENT 6,
  VC 3): PASS». It runs vcrun.py on runfam_K10 (expects VC PASS, dsig_max=3, run_VC_max=3, exec_VC_max=3), anc_K10 (VC PASS, dsig_max=3,
  run_VCbar_max=4), MUT=1 on runfam_K10 (exec_VC_max=4: the control bites), vpf3_vc4 (VC PASS, run_VC_max=4), ent1_vc6 (VC PASS,
  run_ENT_max=6, run_VC_max=3), and the sha1s of the two pins. The full first line for runfam_K10 (box50/families.txt) is:
  «dsig_max=3 dtau_max=0 exec_ENT_max=3 exec_VC_max=3 exec_VCbar_max=1 exec_len_max=100 execs=1 joint_VC_max=3 phase_ENT_max=3
  phase_VC_max=3 phase_VCbar_max=1 phase_len_max=99 phases=1 run_ENT_max=3 run_VC_max=3 run_VCbar_max=1 run_len_max=99 runs=1».
- Quote check: `python3 -I experiments/new/box49/quotecheck3.py docs/new/P-N5-VC-box50.md` prints QUOTES PASS with 5 quotes (quotes=5 bad=0); `--mut` must
  fail. Both are pinned in experiments/new/check.sh with this file's sha1.
- How loose Sauer is (DATA): long121_n40 makes 122 iterations, and the bound is 3,326,524 (pinned starts). xsn91_n48 makes 115, bound 14,901,219.

## 4. Not to sign: CONJECTURE VC-N5 and two dead constants
- CONJECTURE VC-N5: dσ, dτ = O(1) on every game (with RANGE (i): N5 polynomial). OPEN. DATA ≤ 4 (§3); kill climbs (box50/vcclimb.py,
  mutations from L-SI's runlin/growclimb.py and box43/climb.py) reach run VC 4 and execution VC 4, never 5, at n ≤ 96 / 120. Limit
  (READING): VC ≤ log2(len + 1) always, so finite data cannot separate O(1) from O(log n). Only the scaling families speak to it.
- DEAD: run VC ≤ 3 (the library maximum). Instance experiments/new/box50/out/vpf3_vc4.pg (n 48, sha1 1aef63fe…, S3 start in .start):
  the run [5, 27] shatters {(7, 20), (8, 0), (20, 19), (39, 32)}. Two engines agree (L-SI root/n5bcmp.py: n5b = n5x state sequences).
- DEAD: ENT-RUN ≤ 4 (each Even edge enters σ at most 4 times per run). Instance box50/out/ent1_vc6.pg (n 48, sha1 129e9df1…): the edge
  (24, 20) enters 6 times in the run [1, 18] (24: 20, 11, 20, 14, 20, 22, 20, 11, 20, 14, 20), while the run VC is 3; two engines agree.
- Not claimed: any bound on dσ, dτ; anything about TARGET.md.
