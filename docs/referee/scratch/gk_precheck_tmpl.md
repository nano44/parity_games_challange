# R-GK-precheck: REFEREE pre-check of the kill candidate G_k against N5 (NOT a signature)
REFEREE successor 35; header time @@HEADER_TIME@@ (date -u, by command substitution). Lead order: WORK item 1 of the start brief.
This is a PRE-CHECK: a rebuild from the rule's text, a membership check against R104's packet text, an own measurement of L(G_k) and of
N5 on Γ3(G_k), and a line-by-line reading of R117's proofs for a hypothesis that G_k violates. It signs nothing. The proof of
L(G_k) = 2^k − 2 for all k (Theorem EXP-IDEAL of the coming packet P-N5-EXP) was NOT available and is NOT checked here.
Not read before or during this work: any file of claude/l-red-b, of docs/referee-2/ on G_k, and the lanes' simulators and builders
(onep.py, one217, r187 ideal.traj, the C port, gamma3.build, eng3, own34.build, n5v, n5b, n5s237). Prior work of this lane that I did
read: docs/referee/R-P-N5-REACH.md (REFEREE 25/26 on R117) and docs/referee/scratch/rl_engine.py (REFEREE 8's own N5 engine, used in §4, §6).

## 0. Result of the pre-check
| # | check | result |
| --- | --- | --- |
| 1 | rebuild of G_k from the rule's text (Appendix A), own code | byte-equal to the lane's JSON on the four sha1 pins the Lead gave (G_3, G_4, G_8, G_10), at the first run (§1) |
| 2 | membership in R104's class, packet §2 clause by clause, and Ξ-acyclicity | HOLDS for every k ≥ 3 by reading the rule (§2.2), and by machine for k = 3..15 (§2.1), for the genome WITH the order-preserving gate renumbering; three points for Lemma MEMBER's wording (M-1..M-3) |
| 3 | L(G_k) on an IDEAL simulator written from R104 packet §2 only | L(G_k) = 2^k − 2 and max_x sw(x) = 2^(k−2) for k = 3..15, stop «stuck» (§3); the simulator first reproduced the landed L of 21 landed genomes |
| 4 | N5 (SPEC, from S3) on Γ3(G_k): own Γ3 builder, this lane's own engine, own Zielonka | every k run (§4's table: k = 3..9 and the long runs listed there): 2^k + 1 iterations, exactly one fallback, at transition 2^k − 1; states 0..L are the standard states of the IDEAL run; every winner equals Zielonka's; 7 named counters 0; firing control for STD and FLFB |
| 5 | R117's proofs of Theorem REACH3 and Corollary REAL-IDEAL-S3 (P-N5-REACH §0, §3-§8, fixes entries 1-3), line by line, against wires, exit targets, level-0 movers on the exit, all-even parities, level width, upward Ξ-targets, shared targets | NO hypothesis found that G_k violates (§5). REACH3's hypotheses on the genome are exactly «G ∈ IDEAL-ACYC»; none of the listed features is excluded by [DEF] or used against in any step |
| 6 | the lemmas of P-N5-REACH §6 and REACH3's induction step, one N5 transition from the standard state of an ARBITRARY mover state of G_k | 8 named counters 0 on 60 states per k, k = 3..12; the firing control (e-indices in reversed gate order) fires STEP on every state (§6) |
| 7 | does the kill follow? | NOT YET, and not from this pre-check: by Lead reading L43 a «DEAD» of the asymptotic statement needs L(G_k) super-polynomial PROVED for all k (or an instance beyond an explicit bound). What is measured is DATA: L = 2^k − 2 for k ≤ 15 (IDEAL), 2^k + 1 iterations for the k of §4's table (N5 itself). The implication «EXP-IDEAL for all k ⇒ N5 from S3 makes at least 2^k − 1 iterations on a game of 135k − 230 vertices» is landed text (R117) and I found no gap in applying it to G_k; it carries R117's premises (P-1) |

Findings to carry into the review of P-N5-EXP (details in §7): P-1 (premises of the corollary), P-2 («up to 8 movers on a level» is 9 for
k ≥ 6), M-1..M-3 (Lemma MEMBER's wording), P-3 (scope of a kill: N5 as specified, SPEC S4a's rule; nothing about other candidates).

## 1. Rebuild (check 1)
- Input: the rule as relayed by the Lead (message of 12:41Z, 2026-11-13; Appendix A, verbatim). Code: scratch/gk_build.py, written from
  that text only: `movers(k)` (file order), `raw(k)` (the JSON form: keys N, lev, deg, opts, gate, br, bp, start; gate = 100·level + eps),
  `genome(k)` (my simulator's form, gates renumbered order-preservingly onto 0..M − 1).
- My reading of the rule's compressed clauses, each confirmed by the sha1 match:
  - «same W» (v_j, e_j) = «option o: W → member o of (u_(j−1), v_(j−1))»; «same W as y_j» (yb_j) and «same W» (ypb_j) = the W-targets
    of y_j resp. yp_j, option by option;
  - «(top: …)» applies to j = k − 1: y_(k−1), yb_(k−1) have W → u_(k−1) (option 0), v_(k−1) (option 1), eps (20, 21) resp. (22, 23);
  - exit and «no W-target» are −1 in the JSON; «deg» is the scalar 2; br[b] = the position of β-id b in the order by
    (2k + 5 − dep, dl, β-id), ascending, so a smaller dep is a larger rank;
  - dep: u_0, v_0: 0; y_j, yb_j: 2j − 1; u_j, v_j, yp_j, ypb_j: 2j; e_j: 2j + 1; wv_j, wu_j: 2k + 5.
- Result (scratch/gk_logs/sha.out):

@@TABLE_SHA@@

## 2. Membership in R104's class (check 2)
### 2.1 By machine, k = 3..15 (scratch/gk_member.py, log gk_logs/member.out)
R104's packet §2 (docs/red/P-N5-REALIZE.md, sha1 067f06b6…, l. 52-60) read clause by clause; `gk_ideal.check_def` has one test per clause
and `xi_acyclic` tests «G is in IDEAL-ACYC iff its Ξ-graph is ACYCLIC (self-loops count as cycles)»:
1. «movers x = 0, …, N − 1, each with a level lev(x) ∈ {0, …, d − 1}»;
2. «options k = 0, …, deg(x) − 1; M := Σ_x deg(x)»;
3. «a W-target wt(x, k), which is a mover of level lev(x) − 1 if lev(x) ≥ 1 and «none» if lev(x) = 0 (GRADED)»;
4. «a Ξ-target xt(x, k) ∈ {movers} ∪ {X}»;
5. «a β-id b(x, k) (a bijection onto 0..M − 1)»;
6. «a gate index gate(x, k), a bijection of the options onto 0..M − 1» (true for the renumbered genome only, M-1);
7. «per β-id b: a rank br(b) (a bijection onto 0..M − 1)»;
8. «a parity bp(b) ∈ {0, 1}»;
9. «a start s_0 (an option per mover)».

@@TABLE_MEMBER@@

### 2.2 For every k ≥ 3, by reading the rule (my own argument; a pre-check, not a signed lemma)
- Count: 2k (u, v) + (k − 3) (e) + (k − 2) (wv) + (k − 3) (wu) + 2(k − 1) (y, yb) + 2(k − 3) (yp, ypb) = 9k − 16 movers, degree 2, M = 18k − 32.
- GRADED: u_j, v_j, e_j (level j) → u_(j−1), v_(j−1) (level j − 1); wv_j, wu_j (level j + 1) → v_j, u_j (level j); y_j, yb_j, j ≤ k − 2
  (level j + 2) → wv_j (level j + 1; exists for 1 ≤ j ≤ k − 2) and E(j + 1) = e_(j+1) (level j + 1; exists for 2 ≤ j + 1 ≤ k − 2) or
  u_(k−1) for j = k − 2 (level k − 1 = j + 1); y_(k−1), yb_(k−1) (level k) → u_(k−1), v_(k−1) (level k − 1); yp_j, ypb_j, 2 ≤ j ≤ k − 2
  (level j + 2) → wu_j (level j + 1; exists for 2 ≤ j ≤ k − 2) and E(j + 1). u_0, v_0: level 0, no W-target. Levels 0..k: d = k + 1.
- Ξ-ACYCLIC: every Ξ-edge lowers dep by exactly 1: u_j, v_j (2j) → y_j, yb_j (2j − 1); y_j, yb_j (2j − 1) → u_(j−1), v_(j−1) (2j − 2);
  e_j (2j + 1) → yp_j, ypb_j (2j); yp_j, ypb_j (2j) → y_j, yb_j (2j − 1); u_0, v_0 and the wires have only exit options. No self-loop.
- Bijections: β-id 2i + o; br is a position in a total order (ties by β-id); the gate values 100·level + eps are pairwise distinct: at
  level 0 the eps are 2, 5, 3, 1; at a level ℓ ≥ 1 the movers are among u_ℓ (2, 3), v_ℓ (4, 5), e_ℓ (0, 1), wv_(ℓ−1) (6, 7), wu_(ℓ−1)
  (8, 9), y_(ℓ−2) (10, 11), yb_(ℓ−2) (12, 13), yp_(ℓ−2) (14, 15), ypb_(ℓ−2) (16, 17), and at level k also y_(k−1) (20, 21), yb_(k−1)
  (22, 23); all eps < 100. So the renumbering by sorted value is a bijection onto 0..M − 1 and preserves every comparison of two gate
  values; R104's IDEAL step compares gate values only (lexicographic keys), so the IDEAL run is the same (counter RENUM 0, §6).
- Parities all 0, starts given. So G_k (renumbered) ∈ IDEAL-ACYC for every k ≥ 3.

## 3. L(G_k) on my own IDEAL simulator (check 3)
- scratch/gk_ideal.py, written from R104 packet §2 l. 61-77 only: `bset` (the X-chain's β-ids), `better` (Fact X's rule: the β-id of
  largest rank in the symmetric difference; parity 0 and in the first set, or parity 1 and in the second), `avail` (A_s(x)), `step` (level
  by level, lexicographically least key, key = key of the W-target under the NEW state followed by the own gate; «opt» / «stuck»), `run`.
- Faithfulness first (CLAUDE.md, «Traps»): on 21 landed genomes the simulator returns the landed L (log gk_logs/val_ideal.out):

@@TABLE_VAL_IDEAL@@

- G_k (log gk_logs/member.out; sw(x) := the number of steps at which mover x changes its option):

@@TABLE_L@@

- Per mover (scratch/gk_static.py, log gk_logs/static.out, k = 3..9): no wire ever moves, u_0 never moves, v_0 moves once (at step 1),
  and every other mover with index j (u_j, v_j, e_j, y_j, yb_j, yp_j, ypb_j) changes its option exactly 2^(j−1) times. DATA; it shows
  where the doubling sits. gk_trace.py / gk_trace2.py print the runs (log gk_logs/trace_3_4.out for k = 3, 4).

## 4. N5 itself on Γ3(G_k) (check 4)
- Game: scratch/gk_gamma3.py, written from R104 packet §3.1 (Γ(G): indices, owners, priorities, edges) and P-N5-REACH §3 (the 4M + 4
  pads, their order and priorities; the standard state) only. Engine: scratch/rl_engine.py (REFEREE 8, written from SPEC S1-S5, FIX 1-4,
  Q1-Q4; no lane code), default start = SPEC S3. Winners: my own recursive Zielonka (gk_reach.py). IDEAL states: gk_ideal.py.
- Named counters (gk_reach.py; each must be 0): S3START (state 0 is not the standard state for s_0), STD (a state j ≤ L is not the
  standard state for s_j; unit: states), FLFB (a transition 1..L is a fallback), FLTAU (τ changes at a transition 1..L), FLSIG (σ
  unchanged at a transition 1..L), LASTFB (transition L + 1 is not a fallback), WIN (vertices where N5's winner differs from Zielonka's).
- Firing control (`gk_n5.py 3 6 revE`, log gk_logs/n5_ctl.out): the same games with the e-vertices' indices in REVERSED gate order
  (gk_gamma3.build3_revE). STD and FLFB must fire and WIN must stay 0:

@@LOG_CTL@@

  Reading of the control (DATA): with the key order reversed the run is 6 iterations long for every k = 3..6. The long run rests on
  the order of the root-first keys, i.e. on SPEC's S4a rule (P-3).
- Faithfulness first: on the 14 genomes of R117's corpus C14 my builder and the engine give R117's landed numbers (iterations = L + 3,
  one fallback at L + 1; log gk_logs/val_reach.out against experiments/new/box189/reachcheck.out «C14 …» lines):

@@TABLE_VAL_REACH@@

- G_k (logs gk_logs/n5_3_9.out, gk_logs/n5_10.out …):

@@TABLE_N5@@

- TARGET.md §1 on Γ3(G_k): every vertex has a successor; the largest priority is top + 3 = 4M + 9 = 72k − 119 ≤ n3 = 135k − 230
  (asserted by gk_lemck.py: «max priority» column of §6), so the games are games of TARGET.md §1 without compression.

## 5. Reading of R117's proofs against G_k (check 5)
Text read: docs/new/P-N5-REACH.md (sha1 b7bd6937…, frozen; RESULTS R117) §0, §1, §3-§8 with docs/new/P-N5-REACH-fixes.md entries 1-3,
and for [DEF] docs/red/P-N5-REALIZE.md §2, §3.1 with docs/red/P-N5-REALIZE-fixes.md entries 1-3 (entries change no definition of the
genome; REALIZE entry 2 makes the e-index order essential; REACH entry 1 N-3 notes that §13's priority bound uses β-ranks 0..M − 1,
which G_k has). §2 (NO-REACH) and §9 (DEAD SUBDIV) are not used by REACH3 or the Corollary.

Features of G_k looked for in every step (numbers from my rebuild, §2.1):
- (F1) WIRES: wv_j (k − 2 of them) and wu_j (k − 3): two options with the SAME W-target and both Ξ-targets the exit X;
- (F2) LEVEL-0 MOVERS ON THE EXIT: u_0, v_0, both options exit, no W-target;
- (F3) ALL PARITIES EVEN: bp ≡ 0, so every Ω(β) = 6 + 2·br is even;
- (F4) WIDTH: up to 9 movers on one W-level (k ≥ 6); two movers at level 0;
- (F5) UPWARD Ξ-TARGETS: u_j, v_j, e_j (level j) have Ξ-targets at level j + 2 (or k); y, yb, yp, ypb have Ξ-targets at lower or equal levels;
- (F6) SHARED TARGETS: u_j, v_j, e_j have the same pair of W-targets; several movers have the same Ξ-targets; in-degrees > 1 in both graphs;
- (F7) GATE VALUES not 0..M − 1 as generated (renumbered, M-1); (F8) the IDEAL run stops «stuck», not «opt».

| step of R117 | what the step uses of the genome | G_k |
| --- | --- | --- |
| §1 [DEF] (R104's definitions; R104 packet §2) | per option: one W-target one level down (none at level 0), one Ξ-target (a mover or X), distinct β-rank with a parity, distinct gate index; a start; Ξ-graph acyclic. No clause asks for distinct W-targets of one mover, for a mover Ξ-target, for an odd parity, for a width, or for Ξ-targets below the mover | (F1)-(F6) are all inside [DEF]; (F7): the renumbered genome is the member (M-1) |
| §0 Fact X | acyclicity: the chain of (x, k′) never contains b(x, k) | wires and u_0, v_0: B_s(x, 0) = {b(x, 0)} ≠ {b(x, 1)} = B_s(x, 1); the proof's sentence covers a chain that ends at its first option |
| §3 Γ3(G), pads, transport | one pad per edge of the listed kinds; indices appended in the stated order | two options with one W-target still have two gates, two e-vertices, two pads each; nothing merges |
| §4 S3-START | mover: its pads are all even and exactly one has Ω 2; β_g with a mover target: Ω 0 against pb_g's Ω 1; β_g with target X: one successor; gates, core: no genome data | holds for every genome; (F3) plays no role: no vertex has a β among two successors (pβ_g → β_g is a single edge) |
| §5 PAD | Ω(e), Ω(β) ≥ 6; a gate is left only towards e or β | (F3): Ω(β) = 6 + 2·br ≥ 6 |
| §6.1 K3 | the core only (with fixes entry 1's reply for «every genome») | no genome data |
| §6.2 PLAY3 | acyclicity (the chain is finite, repeats no mover, meets no e-vertex); rank(β) > rank(K1), i.e. Ω(β) ≥ 6 > 5 | (F1), (F2): the chain of a gate with target X is that gate alone: β_g → pb_g → K0 …; (b) is the level-0 case, (c) lev ≥ 1 with any W-target |
| §6.3 SBAR3 (i) | lev ≥ 1: e_g is in the P-set of pe_g's play and not of pβ_g's, is even and outranks every β: decided by e_g alone, whatever the two β-sets are; lev = 0: cycle node c_W against K1 | (F1): a wire's gate has lev ≥ 2: decided by e_g. (F2): the lev-0 case. (F3): only Ω(e) even and above every Ω(β) is used (eb = the least even number > bmax) |
| §6.3 (ii), (iii) | [VJ-LOC], [1E-N3] P1; uniqueness by the cycle node or by e_g ∈ P | no genome data beyond (i) |
| §6.4 TAU3 | GRADED (every play from pe_g under τ ends in c_W's loop) and the escape pad pb_g → K0 at EVERY gate | (F5) is the case the escape exists for (R104 packet l. 159-160); G_k is graded; no hypothesis on the direction of Ξ-targets |
| §6.5 ESC3 | GRADED (H-plays from xt(g) end at c_W); β_g with target X has one successor | (F1), (F2): one successor; (F5): no level comparison between g's owner and xt(g) is made |
| §6.6 W3 | GRADED: five steps per level, values depend on lev only; W(β_g) = (c_W, ∅, 5·lev(xt(g)) + 6) for a mover target | (F4), (F6): no width or injectivity; (F1): both options of a wire have W* = (c_W, ∅, 5ℓ + 4), so TIE(x) = R(x) |
| §6.7 KEY3 (a) | Fact X, rank order of β = br order, Ω-parity of β = bp | (F3): the comparison direction is [DEF]'s «better if its parity is even»; with bp ≡ 0 the option whose set holds the top β of the difference is better, in the game and in the model alike |
| §6.7 KEY3 (b) INDEX | block i of the root-first sequence is a function of the gate g_i; first difference at e_(g_i) vs e_(g′_i); e-indices follow gate indices; equal lengths 5ℓ + 4 | (F1): g_j = g′_j for all j < ℓ and the difference is at the option's own gate, i = ℓ: inside the sentence «if g_j = g′_j for j < i and g_i ≠ g′_i». (F6): equal W-targets of different movers are equal blocks. (F7): e-indices are allocated in gate-index order of the RENUMBERED genome, the same order as the raw values |
| §7 REACH3, step j < L | TAU3, ESC3, [1E-N3] P2, W3 (iii), [RULE] at every mover level by level, KEY3 (a), (b) | only «G ∈ IDEAL-ACYC» |
| §7 step L | «either A(x) = {s_L(x)} at every x, or the IDEAL choice is s_L itself» | (F8): the «stuck» branch |
| §8 Corollary (b) | a family in IDEAL-ACYC with L super-polynomial in N + M; n = N + 7M + 10 | N + M = 27k − 48, n3 = 135k − 230; with L(G_k) = 2^k − 2 for all k (NOT checked here) N5 from S3 makes at least 2^k − 1 iterations |

Reading notes.
- R-1. [RULE] (R24 (a) Lemma R, R24 (b)'s choice rule with R103's bridge B) is a premise of R117, used at every mover; its form needs the
  W′-cycle node of the mover to be EVEN and different from the mover: here c_W (W3 (iii)). I did not re-open R24 / R103's proofs; on
  G_k the conclusion of the rule is what the STEP counter of §6 tests on 60 arbitrary standard states per k (k = 3..12), and the STD
  counter of §4 on every state of the runs.
- R-2. No step of §3-§8 has a hypothesis that depends on the size of the genome (levels, width, M); the only k-dependent quantities in
  the proofs are lengths (5ℓ + 4 etc.) and priorities (top + 3 = 4M + 9 ≤ n3).
- R-3. What the reading does NOT cover: the correctness of R117's proofs themselves beyond what REFEREE 25/26 and REFEREE-2 signed
  (I re-read every step and found nothing new); the premises [1E-N3], [RULE], [VJ-LOC] (P-1).

## 6. The lemmas of P-N5-REACH §6 on arbitrary standard states of G_k (check 6)
- scratch/gk_lemck.py: for a mover state s (half of them uniformly random option vectors, half states of the IDEAL run with 0-3 random
  flips), the standard state of Γ3(G_k) for s is built (P-N5-REACH §3 «Transport») and ONE N5 transition (SPEC S4a-S4c, written out
  again on rl_engine's S1) is computed from it. Counters (must be 0; unit: standard states): SBAR (σ̄ ≠ pβ_g at a gate, or σ̄(K2) ≠ r),
  TAU (Iτ ≠ ∅), ESC0 ((K0, K1) ∉ Iσ), ESC (σ_new ≠ σ at an Even non-mover), W (the (σ, τ)-play value at a mover ≠ (c_W, ∅, 5·lev + 5)),
  XI (Ξσ(m_(x,k)) has a cycle node ≠ K1 or a path set ≠ B_s(x, k) ∪ {K0, K3}), AV ({σ(x)} ∪ Iσ(x) ≠ {m_(x,k) : k ∈ A_s(x)}), STEP (σ_new
  at the movers ≠ the standard state of the IDEAL step of s, or τ changed, or a fallback; when the IDEAL run stops at s: no fallback).
- Firing control «revE»: the same game with the e-vertices' indices in REVERSED gate order (the failing construction of P-N5-REALIZE fixes
  entry 2). Only STEP may fire, and it must.

@@TABLE_LEMCK@@

- RENUM and PERM (scratch/gk_perm.py, log gk_logs/perm.out): RENUM = states of the IDEAL run with the raw gate values that differ from
  the run with the renumbered gates (must be 0); PERM = N5 from S3 on Γ3 of G_k with the MOVERS renumbered by a random permutation (all
  mover indices and the option order of the β-vertices change): the counters of §4 must stay 0 and the count 2^k + 1.

@@TABLE_PERM@@

- Not controlled: SBAR, TAU, ESC0, ESC, W, XI, AV (gk_lemck.py) and S3START, FLTAU, FLSIG, LASTFB, WIN (gk_reach.py) have no firing
  control in this pre-check; STEP (§6), STD and FLFB (§4) have one (revE). The review of P-N5-EXP should add controls for the counters
  its DATA clauses rest on (ideas: TAU: drop the escape pads pb_g; AV: build the game with a different β-rank order than the model;
  W: a non-graded mutant).

### 6b. An abstract bit model of the run (my own derivation of the static comparison facts; a tool for the review of P-N5-EXP)
- scratch/gk_abs.py (its docstring states the rules): the movers other than the wires as bits; from the old state the Ξ-winners
  Wn(j) (of u_j, v_j), z(j) (of y_j, yb_j), z′(j) (of yp_j, ypb_j) and each mover's Ξ-preferred option; from the new state, level by
  level, the key-winner kap(j) of (u_j, v_j) and each mover's key-least option; a mover switches iff its other option is Ξ-preferred
  and key-least. Derived by hand from the rule (ranks fall with dep, all parities even, so two chains are compared from the exit end
  backwards; keys are compared from level 0 upwards). It is NOT the lane's statement of its facts K1-K4 / V0-V4 / WIRE, which I have
  not read; the successor should compare the two.
- Tests (must be 0): ABS = state bits that differ from the genome simulator along the whole run; PREF = (state, mover) pairs where
  «the other option is strictly Ξ-better» differs (log gk_logs/abs.out); on 2,000 ARBITRARY states per k (wires at option 0): ABS1 =
  states whose IDEAL step differs from the abstract step, PREF1 as PREF, WIRE = states where a wire has a second available option
  (log gk_logs/abs_rand.out):

@@LOG_ABS@@

@@LOG_ABSRAND@@

## 7. Findings (for the Lead and for the review of P-N5-EXP)
- P-1 (premises; wording of Corollary EXP-N5). R117 is «PROVED on [DEF], [SPEC], [1E-N3], [RULE], [VJ-LOC], [TERM]»: the standing SPEC
  premise 1E-N3 («that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance») is a premise of every landed N5 result,
  R117 included. So «N5 from S3 makes at least 2^k − 1 iterations on Γ3(G_k) for every k» can be stated only with R117's premises, in
  R117's words; the measured runs (§4) are premise-free DATA (the engines execute SPEC). The packet should say which of the two each
  clause is.
- P-2 (the brief's «up to 8 movers on a level»): my rebuild has 9 movers on a level for every k ≥ 6 (levels 4..k − 2: u, v, e, wv, wu,
  y, yb, yp, ypb); 4, 6, 8 for k = 3, 4, 5. No step of R104 / R117 depends on the width, so nothing follows, but a number in the packet
  should be the measured one.
- M-1 (Lemma MEMBER). The genome «as generated» (gate = 100·level + eps) is NOT in R104's class (clause 6: a bijection onto 0..M − 1,
  and Γ(G)'s gate vertices have index N + gate(x, k)). The member is the order-preservingly renumbered genome; the sha1 pins are of the
  raw JSON. Lemma MEMBER should name the renumbered genome as the object, and say that the IDEAL run is unchanged (keys compare gate
  values only) and that Γ(G), Γ3(G) are built from the renumbered one.
- M-2. The file's mover order fixes the mover indices and the option order of the β-vertices in Γ(G_k). By REACH3's proof these never
  decide; PERM (4 random mover orders per k, k = 3..6) is DATA for it. The packet's DATA should say which mover order its games use.
- M-3. «deg» is the scalar 2 in the JSON and «pi», «cyc» of the older genome files are absent: a loader that expects a list or the old
  keys must not be reused silently (mine reads `opts` only).
- P-3 (scope of a kill). What the family can kill, once EXP-IDEAL is proved for all k: the iteration bound for N5 AS SPECIFIED (SPEC
  S1-S5 with S4a's rule, the root-first key of R24 (b)), from its default start, on TARGET.md §1 games. It says nothing by itself about
  N5′-xi or any other tie rule; the IDEAL model is R104's model of S4a's rule.
- P-4 (L43). Everything measured here is DATA. The asymptotic statement needs the proof of L(G_k) = 2^k − 2 (or any super-polynomial
  lower bound) for ALL k; I will review it step by step when the packet is frozen. For that review my simulator can test each
  claimed static fact, rest state and response step for k ≤ 15 in seconds.

## 8. Tools and logs (docs/referee/scratch/)
- gk_build.py (the rule), gk_ideal.py (R104 packet §2), gk_gamma3.py (Γ(G), Γ3(G), standard states), gk_reach.py (replay of REACH3 with
  counters; own Zielonka), gk_member.py, gk_n5.py, gk_lemck.py, gk_perm.py, gk_trace.py, gk_trace2.py, gk_static.py, gk_abs.py, gk_abs_rand.py, gk_abs_trace.py (§6b), gk_tables.py (builds the tables
  of this report from the logs; template gk_precheck_tmpl.md; the rule's text gk_rule.txt), gk_run.sh (regenerates the logs: `bash gk_run.sh quick`, `bash gk_run.sh n5`); logs in gk_logs/.
- Oink is not built in this container (verify's Oink step NOT RUN); the Zielonka used is my own (gk_reach.py), a plain recursive
  implementation, not Oink's.

## Appendix A. The rule, as relayed by the Lead (message of 12:41Z, 2026-11-13; quoted in full; not my text)
@@RULE@@

## DONE / FINDINGS / NEEDS
- DONE: checks 1-6 of §0 (rebuild byte-equal on 4 pins; membership for every k by reading and for k = 3..15 by machine; L(G_k) =
  2^k − 2 for k = 3..15 on my simulator; N5 on Γ3(G_k) as in §4; R117 read line by line against (F1)-(F8); lemma counters with a
  firing control).
- FINDINGS: no hypothesis of R104's class or of R117's proofs is violated by G_k; P-1 (premises), P-2 (9 movers on a level), M-1..M-3
  (Lemma MEMBER), P-3 (scope), P-4 (L43: the kill needs EXP-IDEAL proved for all k; not seen yet).
- NEEDS: Lead: the freeze SHA of P-N5-EXP for the first review (item 2).
