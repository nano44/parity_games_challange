# R-N5-GCX: REFEREE report on packet P-N5-GCX (L-SI box 21: Lemma MIG-SPLIT, Corollary UL-RED, Lemmas ABS-HEIGHT, ABS-TIE, LOC)
Referee: REFEREE (successor 16), Opus 5.5 (owner ruling D15). FIRST referee (Lead brief to successor 16, item (3); Lead GO 18:25Z by date -u).
- Object and pin: docs/si/P-N5-GCX-box21.md, sha1 5a91bebbc34f14be147da38adc1a6202407c70c2, 105 lines, author L-SI successor 17: the same
  sha1 on my tree and at the l-si freeze 02240121 (an ancestor of HEAD). Its quote base 7d87f9be.
- Written 2026-10-26T18:40Z-18:47Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ file on GCX on my tree, on trunk or on origin/claude/referee-2 at my fetches (re-listed in
  the same turns; 0 / 0 / 0 at 18:38Z and 18:45Z). No lane code run (experiments/si/root/gcx.py, abscyc.py, common.py, L-RED's ulx.py, mkcx.py,
  mkreader.py neither executed nor imported; lane instances and start files read as data). D1.
- Premises read against their text: RESULTS R62 setting (W_k = the valuation of σ_k in G_τ, i.e. the (σ_k, τ)-play value; l. 3273-3276) and
  (b) TC-CLASS (l. 3282-3283); R55 setting (D_k, u(v) = first D_k-vertex of the (σ_k, τ_k)-play; l. 2786-2787); phase = λ_Ξ and τ constant
  (R38 (a) KEY, as R55 cites); R67 setting (FORBIDDEN at k, U(S); l. 3451-3458) and (f) CHARGE-U with N-RUND-5 (U(S) depends on L);
  P-N5-ROOT-box20.md §3 FREEZE-A (a)-(c) (for the §5 READING only).
- Quotes: all 5 "[Q path@commit:lines] «…»" quotes verbatim at 7d87f9be (my scratch/flip_quotes.py: QUOTES 5 FAILED 0).
- Tools (own, docs/referee/scratch/): gcx_probe.py (own engine rl_engine, SPEC; checks in §6), abs_model.py (own simulator of the model
  ABS, written from §4's text), loc_cex.py (the LOC counterexample), gcx_literal.py (the interval-level reading of §1). Logs gcx_logs/.

## Verdicts (sign-off line per item)
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §2 | Lemma MIG-SPLIT, with its Consequence | SIGNED (Consequence: with RESULTS R62 (b) TC-CLASS added to the premises, GCX-N2) |
| §3 | Corollary UL-RED (a), (b), CONDITIONAL on CONJECTURE UL_G | SIGNED, under the transition-local reading of "global C-interval" (GCX-N1); a REDUCTION: UL_G is a CONJECTURE and K(S) is not bounded |
| §4 | Lemma ABS-HEIGHT (acyclic model, basic tie rule) | SIGNED (in the model) |
| §4 | Lemma ABS-TIE (acyclic model, any deterministic tie rule) | SIGNED (in the model) |
| §4 | Lemma LOC | SIGNED for the basic tie rule (more generally, any rule that keeps the current choice when it is a maximiser). NOT SIGNED as stated: its parenthetical "(cyclic model; basic or any deterministic rule)" is FALSE for "any deterministic rule" (gap G-GCX-1, one-vertex counterexample, §4) |
| §4 | Remarks MONO, MONO-SUCC, NO-RETURN | CHECKED (true in the model; MONO's N-half needs "pointwise maximal" read as pointwise greatest, GCX-N4); not to-sign items |
| §5 | READING (pure C-interval = model), CONJECTURES UL_C / UL_G / FINAL-EACH / ABS-CYC, data | not signed (as briefed); data and the effect of the L-RED kills in §5 below |
One gap: G-GCX-1 (LOC's "any deterministic rule"). Notes GCX-N1..N5. Nothing here bounds N5's running time; no bound on K(S); not a
TARGET.md claim; G-N5-TIME stays OPEN.

## 1. MIG-SPLIT, re-derived (parentheticals checked one by one)
Claims inside the statement, each checked:
- (M1) "u′ ≠ u, since z ∉ R_u(t) ∪ A_t" ✓. z ∉ A_t: z's play at t meets D_t, so u′ (= u_t(z) of R55) exists; z ∉ R_u(t): u′ ≠ u. Data:
  MS_up (u′ missing or = u) 0 failures.
- (M2) "(z included)" in π ✓, and it is NEEDED: in L-RED R93's cxmig_k family the only switching Even vertex on π is z itself, at every
  X-migration (28/28 at the given starts; 83 of the 89 (S) cases on the 1,140-file library); my MUT=2 (z excluded from π) fails 28/28 there.
- (M3) "in case (S) z's play changes" ✓. Take the FIRST switching Even vertex w on π (the packet says "some"; the first one is what the
  argument needs): the (t+1)-play from z follows π up to w (unswitched Even vertices, Odd vertices on τ, τ constant on the phase), and leaves
  w on a different edge. Data: MS_Splay 0 failures.
- Proof ✓. One harmless wording point: "The Odd vertices of π are not in D_t, so they follow τ" — on the (σ, τ)-play every Odd vertex follows
  τ, in D_t or not; what the proof uses is τ_{t+1} = τ_t (phase). The contradiction step ✓: the first D_{t+1}-vertex of z's (t+1)-play is u′ or
  a vertex of π; u ∉ π (π has no D_t-vertex, u ∈ DD_t ⊆ D_t) and u′ ≠ u, so z ∉ R_u(t+1).
- Consequence ✓ with one premise added (GCX-N2): "(its W-play)" = z's (σ_t, τ)-play ✓ (R62 setting: W_k is σ_k's valuation in G_τ). Case (L)
  gives a vertex u′ of D_t leaving D at t → t+1; that u′ lies in U_c is RESULTS R62 (b) TC-CLASS (λ_Ξ(u(v)) = λ_Ξ(v), v = z ∈ R_D), not a
  definition. Data: MS_tcclass 0 failures; MSC (the Consequence's inequality per run and per gate) 0 failures.

## 2. UL-RED, re-derived
- (U1) Reading of "global C-interval" (GCX-N1). §1 says "a maximal sub-interval of S on which ... every Δ_t(u), u ∈ DD_t, is constant". Read
  at the INTERVAL level (all values of Δ(u) over the states of the interval at which u ∈ DD equal), maximal intervals can OVERLAP, and the
  proof's step "There are ≤ K(S) + 1 global C-intervals" fails: on long121_n40 (experiments/red/n3/instances, sha1 c667c085, its .start
  d750664a), the sub-run S = [31, 37] (fallback-free, one phase, λ_W constant) has gate u = 1 in DD at 31-32 and 35-37, not at 33-34, with
  Δ_32(1) ≠ Δ_35(1); under the interval reading its maximal global C-intervals are [31, 34] and [33, 37], K = 0, and 2 > K + 1
  (scratch/gcx_literal.py). Read TRANSITION-LOCALLY (a transition t → t+1 is in a global C-interval iff for every c: A^c_{t+1} ⊆ A^c_t,
  D_{t+1} = D_t, and Δ_t(u) = Δ_{t+1}(u) for u ∈ DD_t ∩ DD_{t+1}; optionally also DD_t = DD_{t+1}), the maximal intervals are the maximal runs
  of good transitions, separated by the K(S) cut transitions, so there are ≤ K(S) + 1 of them ✓. This is the reading §3's Scope line states
  ("the transitions at which some class's A grows, D changes, or a D-direct offset changes"). SIGNED under it; the fixes file should state it.
- (U2) (a) ✓: a U event is one Even vertex's switch at one transition, so ≤ n_E per transition ✓; every transition of S is a cut (≤ K(S),
  each ≤ n_E events) or lies in exactly one maximal interval [a, b] ✓, and UL_G admits U events only at k′ ∈ [a, a + n − 2], ≤ n − 1
  transitions ✓. Total ≤ n_E((n − 1)(K + 1) + K) ✓.
- (U3) (b) ✓: CHARGE-U (quote verbatim, l. 3485-3486) is stated for runs with (ii) only, at level L with U(S) at the same L (N-RUND-5); here
  both are at L = −1 ✓; substitute (a) ✓.
- (U4) "(a CONJECTURE, §5)" ✓ labelled; UL-RED is an implication from it. "(hypothesis (ii) only)" is the R67 quote ✓. Scope "K(S) is not
  bounded here" ✓.
- Data (both local readings R1 / R2; 0 failures of ULa, ULb; UL_G itself held in every run, so no ULa_noULG case arose): see §6.

## 3. ABS-HEIGHT and ABS-TIE, re-derived (in the model)
- Model ✓ as written. In the acyclic model every strategy is valid, the pointwise optimum N* exists (reverse topological DP) and is greatest,
  and a valid arena strategy is pointwise optimal iff each s′(v) is an N*-maximiser over Al_s(v) ✓ ("successors' optimal values do not
  depend on v").
- ABS-HEIGHT ✓. Settled v: case y1 = s_t(v) gives Al_{t+1}(v) = Al_t(v) (M unchanged on successors) ✓; case y1 ≠ s_t(v) gives M_t(y1) >
  M_t(s_t v), so Al_{t+1}(v) ⊆ Al_t(v) ✓; N unchanged on successors, y1 is still a maximiser and the basic rule keeps it ✓; from t + 1 the
  first case recurs ✓; v's M, N = w(v) + successor values, constant from t + 1 ✓. Base (all successors terminal): settled from 0 ✓. Induction
  ✓. Parentheticals: "(height: longest path to a terminal, in vertices)" ✓ (a vertex with only terminal successors has height 1 and is
  constant from state 1); "≤ n" ✓; "(acyclic; basic tie rule)": BOTH needed — the one-vertex game of §4 below is acyclic and, under the
  "anti" or "sizedep" rule, is fixed only after 2 steps at height 1.
- ABS-TIE ✓. For settled v a change goes to y ∈ Al(v) ∖ {s(v)}: M(s(v)) rises strictly and s(v) leaves the arena ✓; the arena maximum of N is
  attained at the new choice ✓; a step without change at v repeats R's inputs (arena, successor values, current choice), so v is constant
  from then on ✓; so ≤ 1 + (deg(v) − 1) changes, consecutive, v constant from t + deg(v) ✓; induction gives t_v = deg(v) + max_y t_y ≤ Σ deg
  along a path ≤ m ✓ (m counts the edges out of V). "(at the new choice)" ✓. The proof needs R to depend only on (arena, the arena's
  values, current choice), which is the model's definition of a rule ✓.
- Data (abs_model.py; 0 failures): acyclic, n 2-8, 10,000 random games × 6 rules = 60,000 runs (logs abs_acyc_4000_s11, abs_acyc_6000_s13):
  HEIGHT 20,000 checks (rules basic, basicM), max (fix time − height) = 0, i.e. the bound is attained; TIE
  60,000 checks plus every vertex's t_v; 15 runs (rules anti, hash, sizedep) are fixed later than their height, so ABS-TIE's weaker bound
  is needed for general rules.

## 4. LOC: SIGNED for the basic rule; "any deterministic rule" is FALSE (gap G-GCX-1)
- Proof for the basic rule ✓. Viability argument ✓: substituting a viable arena successor y at v alone keeps every play finite and adds
  w(v) + N(y) − N(v) at v and at every vertex whose play passes v, so a maximal (a fortiori greatest) s′ has s′(v) an N-maximiser over the
  viable arena successors; a non-viable y closes a cycle through v ✓. With none of the three changes, ABS-HEIGHT's case analysis runs on the
  viable successors ✓, and y1 = s_{t+1}(v) is a maximiser at step t + 1, so a rule that KEEPS the current choice when it is a maximiser
  returns y1 ✓.
- "(cyclic model; basic or any deterministic rule)": FALSE for "any". In the case y1 ≠ s_t(v) the arena shrinks and the current choice
  changes, so R's inputs change and a deterministic rule may pick another maximiser. Counterexample (scratch/loc_cex.py, acyclic, so in the
  cyclic model too): one non-terminal v, w(v) = 0, terminal successors a (h 0, T 0), b (h 1, T 5), c (h 2, T 5), s_0(v) = a. Step 0: arena
  {a, b, c}, maximisers {b, c}. Rule "anti" (a maximiser other than the current choice if one exists, lowest index) or "sizedep" (smallest-M
  maximiser on an arena of ≥ 3 vertices, else largest-M) picks b. Step 1: arena {b, c} (M(c) > M(b)), maximisers {b, c}; both rules pick c.
  So s_2(v) = c ≠ b = s_1(v), while every successor is a terminal (M, N constant, always viable). The basic rule and "lowest index" keep b.
- Random data (abs_model.py, cyclic model, n 2-7; 7,000 games × 6 rules; runs stop where no greatest strategy exists, as the model
  restricts; logs abs_cyc_3000_s12, abs_cyc_4000_s14): LOC fails for anti 26 / sizedep 43 / a hash-based rule 18 times, and never for basic,
  basicM (keep, else largest M) or lowest index (5,705 checks for those three); acyclic 10,000 games: anti 96 / sizedep 168 / hash 62
  failures, basic, basicM, lowidx 0 of 6,484.
- Repair (for the fixes file): restrict LOC to tie rules with KEEP ("R returns the current choice whenever the current choice is a
  maximiser"), or to rules that are current-independent and consistent under contraction (if R picks y from X and y ∈ X′ ⊆ X with the same
  values, R picks y from X′; then the case y1 ≠ s_t(v) also returns y1). Which kind N5's tie rule is stays OPEN, as §5 (ii) says.
- What G-GCX-1 touches: LOC alone. ABS-HEIGHT is stated for the basic rule; ABS-TIE's proof does not use LOC. LOC is a tool for the OPEN lift
  (§5), not used by any signed item.

## 5. The §5 READING, and what the L-RED kills touch (not signed; data and readings)
- Lead question: which GCX items do R91 (UL_C DEAD) and R93 (C-ONCE_X DEAD) touch?
  - R91 (docs/red/R91-ulc-reader.md, reader_L): touches NO signed item. UL-RED's premise is UL_G, not UL_C. Re-measured with my engine at the
    given starts: reader_L10 / L20 / L40 (sha1 31644312 / c9f3c948 / cb6b7c76) run 13 / 23 / 43 iterations, one fallback-free phase, global
    C-interval [0, L + 1] (K = 0), one U event at index L = 10 / 20 / 40 against UL_G's threshold n − 1 = 35 / 55 / 95. UL_G holds there with
    slack L + 15, as R91 §3 says.
  - R93 (docs/red/R93-conce-x-ladder.md at l-red 18624c0b, cxmig_k): touches NO signed item. C-ONCE_X was a lane conjecture, not in the packet's
    claims. It is a positive test of MIG-SPLIT: cxmig_k4 / k8 / k16 (sha1 a3893ea4 / 4fa6ee8f / 9f29476d) run 12 / 16 / 24 iterations and
    vertex x makes 4 / 8 / 16 X-migrations; every one is case (S) with x itself the switcher (the "(z included)" parenthetical, (M2)). X_u per
    gate is 1, so MIG-SPLIT's per-gate Consequence is untouched. It also does not contradict the §5 READING: the pure interval ends before its
    freeze time a + |A_a| − 1 (FREEZE-A (b)), and every one of its X-migrations lies inside that freeze window (RD_xlate 0).
- READING (pure C-interval = model), not signed. One step of it can be checked from landed or signed text: once A has frozen (FREEZE-A (b);
  its hypotheses, S4a steps and A non-increasing, hold on a global C-interval), M(τ u) is constant for a D-direct gate u (τ u ∈ A), and Δ(u) is
  constant by the interval's definition, so h_u = wt(u) + M(σ̄ u) = wt(u) + M(τ u) − Δ(u) is constant (GCX-N3). The rest (S4a on U_c is the
  model's step, the W-values are the model's N) is not checked here. Data (§6): in every pure R1-interval past its freeze time, M(σ̄_t u) is
  constant (RD_hvar 0) and no X-migration happens after the freeze (RD_xlate 0). Thin: 13 pure intervals pass their freeze time.

## 6. Data (own engine; DATA, not proof; 0 failures of every signed check)
Checks (scratch/gcx_probe.py): MS (MIG-SPLIT at every in-phase S4a transition, every class, every X-migration; (L)/(S) classified), MSC (the
Consequence per maximal fallback-free run and per gate), UL (U(S) at L = −1 per run with (ii); global C-intervals under R1 and R2; ULG = UL_G
as data; ULa, ULb; R3 = re-entry of a gate into DD with a different Δ inside one R1-interval), RD (the §5 READING, data only).
| set (log in gcx_logs/) | N5 runs | MS checks (L only / S only / both) | MSC | UL runs (U events; inside an R1-interval) | max K (R1) | failures |
| --- | --- | --- | --- | --- | --- | --- |
| lib 1,140 files (fbc_lib.txt, n ≤ 40; S3 + given start + 2 random) lib1140_rs2 | 2,739 | 223 (134 / 84 / 5) | 89 | 2,396 (1,820; 952) | 19 | 0 |
| lib41 (experiments/new/box41, n ≤ 64; S3 + 2 random) lib41_rs2 | 1,130 | 30 (3 / 27 / 0) | 5 | 1,306 (1,442; 737) | 20 | 0 |
| L-RED ul instances (reader, ladderd0, ladderent, cxmig; given + S3 + 2 random) red_ul_s3rs2 | 48 | 40 (0 / 40 / 0) | 40 | 56 (3; 3) | 48 | 0 |
| random 𝒞^kO, n 4-14, k ≤ 4 (seed 161) rand3000_s161 | 9,000 | 1 (1 / 0 / 0) | 1 | 1,513 (0; 0) | 2 | 0 |
| random 𝒞^kO, n 14-26, k ≤ 10 (seed 163) rand1500_n14-26_s163 | 4,500 | 0 | 0 | 1,157 (0; 0) | 1 | 0 |
- UL_G (DATA on the conjecture): the latest U event inside an R1-interval sits at index n − 1 − 10 (lib1140 and lib41); the longest R1-interval
  has n − 1 transitions (frzgap0_n4, n = 4, from experiments/red/h3), n − 2 on lib41. R3 (the reading point of GCX-N1) occurs twice, both
  on long121_n40 (class 11, gate 1, intervals [31, 37] and [91, 97]).
- Controls (each bites): MUT=1 (accept only case (L)) fails 28/28 on the L-RED instances; MUT=2 (z excluded from π) fails 28/28 there;
  MUT=4 (UL_G threshold 0) fails on all 3 reader runs. MUT=3 (drop the +K term of (a)) does not bite: the bound is far from tight in data.
- Engine agreement with the lanes: reader_L and cxmig_k iteration counts, U-event index, interval [0, L + 1] and per-vertex X-migration
  counts equal L-RED's tables.

## 7. Notes (for the fixes file; none changes a SIGNED statement except G-GCX-1's restriction of LOC)
- GCX-N1 (definition): state the transition-local reading of "global C-interval" (U1); under the interval-level reading the count step of
  UL-RED (a) fails on long121_n40 [31, 37].
- GCX-N2 (premise): the Consequence of MIG-SPLIT uses RESULTS R62 (b) TC-CLASS (u′ ∈ U_c); §0's "SPEC (definitions only)" should list it.
  Also the proof's "not in D_t, so they follow τ" should read "follow τ, constant on the phase".
- GCX-N3 (READING support): the constancy of h_u in the §5 READING follows from FREEZE-A (b) for τ u plus the constant Δ(u); the packet could
  say so. The model identification itself stays a READING.
- GCX-N4 (model): MONO's N-half (N non-decreasing) needs "pointwise maximal" read as pointwise GREATEST (s is itself a valid arena strategy);
  LOC's viability step works for either reading. In the cyclic model a rule's simultaneous keeps can close a zero-weight tight cycle; my
  simulator never met one (RULEINVALID 0).
- GCX-N5 (data): ABS-HEIGHT's bound is attained (fix time = height) in random acyclic models; ABS-TIE's weaker bound is needed for some
  deterministic rules (15 runs fixed after their height).

## 8. TARGET.md diff
Not a claim of TARGET.md §1 / §2 (no algorithm, no running-time bound; the §4 lemmas are about an abstract model, UL-RED is conditional on a
conjecture with K(S) unbounded). G-N5-TIME: open.

DONE: this report. FINDINGS: G-GCX-1 (LOC false for "any deterministic rule"); GCX-N1..N5. NEEDS: Lead: route G-GCX-1 and the notes to L-SI's
fixes file; §C against REFEREE-2 on your word.

## §C. Comparison with REFEREE-2 (written 2026-10-28T21:47Z by date -u, after the Lead's word of 21:43Z; REFEREE-2's report
docs/referee-2/R2-N5-GCX.md, report fe04ca32 and its §C fc63f1f1 on trunk 5da4017d, opened only after this report was pushed at e01bdec6)
Written by REFEREE successor 16, the author of this report. Every verdict is labelled (Opus 5.5, D15).
### Verdicts
| item | REFEREE (e01bdec6) | REFEREE-2 (fe04ca32) | joint |
| --- | --- | --- | --- |
| §2 MIG-SPLIT and Consequence | SIGNED (GCX-N2: u′ ∈ U_c via TC-CLASS) | SIGN (N-GCX-1: u′ ∈ U_c, one-clause proof) | SIGNED |
| §3 UL-RED (a), (b), conditional on UL_G | SIGNED under the transition-local reading (GCX-N1) | SIGN as an implication; transition-local reading needed (N-GCX-2) | SIGNED, transition-local reading |
| §4 ABS-HEIGHT, ABS-TIE | SIGNED | SIGN | SIGNED |
| §4 LOC | SIGNED for the basic (keep) rule; "any deterministic rule" FALSE (G-GCX-1) | SIGN for the basic rule; "any deterministic rule" FALSE (G-GCX-1); repaired LOC′ signed | SIGNED for keep rules; G-GCX-1 joint; LOC′ SIGNED (below) |
| §4 Remarks MONO, MONO-SUCC, NO-RETURN | CHECKED (GCX-N4: greatest) | SIGN | CHECKED |
Verdicts identical. Joint gap map: {G-GCX-1}, found independently with the same one-vertex model. Both counterexamples use terminals
h 0 / 1 / 2, T 0 / 5 / 5, and a rule that leaves a current maximiser.
### G-GCX-1: the two repairs
- Mine: LOC as stated for rules that KEEP the current choice when it is a maximiser, or for current-independent rules consistent under
  contraction.
- REFEREE-2's LOC′, for every deterministic rule: "… or s_{t+1}(v) ≠ s_t(v)". I checked the proof: if no successor changes and s_{t+1}(v) =
  s_t(v), then the arena (same current choice, same M on the successors), the N-values and the viable set repeat. So R's inputs repeat, and
  so does its output. I also checked it on my simulator (abs_model.py, the four GCX logs' seeds, acyclic and cyclic): 25,503 change events,
  LOC failing 122 / 211 / 80 times under anti / sizedep / hash, LOC′ failing 0 times under all six rules.
- I SIGN LOC′. The repairs are compatible; the fixes file can carry both.
### Notes, matched
| REFEREE | REFEREE-2 | joint |
| --- | --- | --- |
| GCX-N1 (transition-local reading; interval-level reading breaks UL-RED (a)'s count on long121_n40 [31, 37]) | N-GCX-2 (same; the working note's "(so DD_c is constant too)") | same note; my instance makes it concrete |
| GCX-N2 (u′ ∈ U_c: R62 (b) TC-CLASS; wording "follow τ, constant on the phase") | N-GCX-1 (the same, by the honest play and W-play agreeing up to the first D-vertex) | same note; either a citation or the clause |
| GCX-N3 (§5 READING: h_u constancy from FREEZE-A (b) + constant Δ) | — (READING not reviewed) | REFEREE's note |
| GCX-N4 (MONO's N-half needs "greatest") | read as greatest without saying so | same |
| GCX-N5 (ABS-HEIGHT attained; ABS-TIE needed for general rules) | the same data | same |
| my §3 "≤ 1 + (deg(v) − 1) changes, v constant from t + deg(v)" | N-GCX-3 (constant from t + deg(v) − 1) | ACCEPTED: each change, the first included, removes the old choice from an arena of size ≤ deg(v), so ≤ deg(v) − 1 changes. My count was loose by one; no verdict depends on it |
| — | N-GCX-4 (thin data), N-GCX-5 (independence) | ACCEPTED |
### Data
Both engines, 0 failures of every signed check. Both reproduce the reader_L index L in [0, L + 1], nep90 / nep76 migrations all case (L), and
cxmig_k all case (S). UL_G holds in every run for both. LOC fails only under non-keep rules, in both simulators. Nothing open between the
referees on GCX.
