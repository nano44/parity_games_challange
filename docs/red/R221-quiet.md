# R221 item 1: adversary vs L-NEW box 194 (LOC-GATE, QUIET, T-QUIET, UP-T, DEAD IN-BOUND) (L-RED successor 56)
Lead box 23:54Z 2026-11-07. Target: claude/l-new e9993378, docs/new/N5-LOC-box194.md (sha1 83814ef6ba622023fd6670fffb6111c1641b8422,
24,718 B, checked), tools experiments/new/box194/ (read only, NOT run, NOT imported). Referee files not read.
Labels: SURVIVES / BROKEN (frozen instance + sha1) / GAP / DATA (unit, set, scope, counter) / PROVED (lane, unrefereed). Nothing here is
a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).
Tools: experiments/red/r221q/ (own.py = R217's independent IDEAL-CYC run, as copied in R220; brute221.py, quiet221.py, bonly221.py,
ties221.py, in221.py, div221.py, trace221.py, ladclimb.py with SCORE=quiet). No L-NEW code is used for any check of box 194. The
exceptions are div221.py / trace221.py for (d): they run box 190 n5v.py and box 189 gamma3.py, which are the N5′-xi object itself.

## 0. Verdicts
| statement (box 194) | verdict | evidence |
| --- | --- | --- |
| §2 Lemma CN2 | SURVIVES | proof re-read; brute force: 0 cycle nodes of priority < 2 (§2) |
| §3 Lemma LOC-GATE | SURVIVES | proof re-read case by case; brute force over ALL Odd strategies: 0 failures (§2) |
| §3 Lemma LOC-K2 | SURVIVES | brute force: every pointwise-optimal τ has τ(K2) = K1 (§2) |
| §4 OVT-DV without [LOC] (and the list of [LOC]-only lane lemmas) | SURVIVES | follows from LOC-GATE; L-RED's TOP-DEC (d), HIDE-BUSY, CHAIN-SHIELD use [LOC] only at gates (my lemmas; I confirm the READING) |
| §6 Theorem QUIET | SURVIVES (one GAP, closed by §3 below) | proof re-read; 123 runs, 0 failures; longest quiet window W ≤ N (§4) |
| §6 Corollary T-QUIET | SURVIVES | (c): the class accounting is right (§5) |
| §6 Corollary UP-T | SURVIVES under [E-LEV] only, as stated | [E-LEV] is necessary for UP-B (R220 §3, NOUPC_{1,2,3} with EORD = rev) |
| §6 Corollary ASC-T | SURVIVES | HUB-ASC-G (SURVIVES, R220) + T-QUIET |
| §7 DEAD constant IN-BOUND | CONFIRMED | own count: RS2(L, 6) has IN = L + 1 for L = 4, 8, 16, 32 (§6) |
| (d) «IDEAL-CYC T bounds N5′-xi on Γ3» (§6 READING, not claimed by L-NEW) | GAP | holds only up to the first fallback and only via REACH3-CYC (CONDITIONAL); mover changes after the fallback on 3 frozen instances (§7) |
No BROKEN. New (PROVED, lane): Lemma B-ONLY (§3). It makes LOC-GATE's tie case and QUIET's E-classes vacuous, and it removes the
H_g / A_g terms of R219 GATE-POLY and R221 RHO-COUNT.

## 1. Premises: where they are landed (the Lead's (a) question)
Read in trunk docs/RESULTS.md (claude/vibrant-johnson-nxvvxo 16d582d2a), entry R118, l. 13607 ff.
- F3 and F4′: R118 (b) «Facts F1-F6 (§3 l. 68-83) with F4 REPLACED by F4′ (fixes l. 33-41): «if v ∉ Π(A) ∪ Π(B), then A ⊴ B ⇒ ext(v, A) ⊴
  ext(v, B), and A ◁ B ⇒ ext(v, A) ◁ ext(v, B).»». LANDED.
  - The extra clause («whenever v ranks below Λ(A) and Λ(B)») is not in the landed text.
  - Box 194 uses F4′ only at a gate g (LOC-GATE Case 1), and at x, g and a face (QUIET Q5). Gates and movers are never in a Π (CN2).
    The face is not in Π(Ω(z)), because it would lie on z's cycle, and not in the simple path's Π. So only the landed clause is
    used. The extra clause does NOT sneak in.
- DOM, STRICT: R118 (c), quoted verbatim in box 194 §6. LANDED.
- [OPT] (σ̄_t pointwise optimal at every vertex at once): not a numbered clause of R118. Box 194 cites its use inside R118 (b) F3's proof
  and RESULTS R21 (a)'s parenthetical. R118's own line says «Odd's optimal counterstrategy σ̄ (any fixed deterministic choice)».
  Whether «used in a signed proof» counts as landed is a Lead reading. Independent DATA: a pointwise optimum exists at every state of
  6,000 random genomes, and own.py's values equal it (§2).
- [XICYC-a] (Odd unrestricted at gates and K2 in IDEAL-CYC): R118 (a). LANDED.

## 2. LOC-GATE, LOC-K2, CN2 by brute force (brute221.py; DATA)
At every state σ_t of own.py's run, enumerate ALL positional Odd strategies (2^(M+1)), compute every vertex's VJ value, and take the
per-vertex ⊴-minimum. Then check:
- OPT: some strategy attains the minimum at every vertex at once, and its values equal own.py's;
- LOC: EVERY pointwise-optimal τ takes the ⊴-smaller face at every gate with unequal face values;
- K2: every pointwise-optimal τ has τ(K2) = K1;
- CN2: every cycle node has priority ≥ 2.
Unit: (state, gate) pairs; states. Set: 6,000 random Ξ-cyclic genomes (brute221.rgen, seeds 11 and 12, d 1-3, degree 2, M ≤ 10);
8,950 states, 56,934 (state, gate) pairs. Scope: IDEAL-CYC via own.build / own.VJ (own.py's Odd SI is not used for the optimum).
Counter: optfail 0, valfail 0, locfail 0, k2fail 0, cnlow 0, ties 0 (out/brute_r11.txt, out/brute_r12.txt).
Proof re-read: Cases 1, 2-i-a/b and 2-ii-a/b/c are complete. 2-ii-c uses dist_Q(q, Λ) > k(a), which is right because the arc from q to Λ
passes g and then a. No VJ00 improvement lemma is used. SURVIVES.

## 3. Lemma B-ONLY (PROVED, lane; new)
Statement. In IDEAL-CYC(G), for every genome G, every state t and every vertex v other than c_W and the e-vertices whose W-target is
c_W: Λ_t(v) is a β-vertex, K1, K2 or c_X. So it is less relevant than every e-vertex.
Proof.
- Let τ_β be Odd's strategy «β-face at every gate, K1 at K2». It is positional, and Odd is unrestricted at gates and K2 ([XICYC-a]).
- Under (σ_t, τ_β), an e-vertex is entered only from its gate, which τ_β never sends to it. So a play from any v other than an
  e-vertex meets no e-vertex. A play from an e-vertex meets only that one, at its first step, unless its W-target is c_W.
- Hence the cycle of every such play contains no e-vertex and not c_W. Its node is a β, K1, K2 or c_X, and its reward is below the
  reward of every e-vertex: e-vertices are even and above every β, K1, K2 and c_X ([DEF], E-DOM-ALL-d).
- By [OPT], Ω_t(v) ⊴ (v's value under (σ_t, τ_β)). The order compares rewards of Λ first. So reward(Λ_t(v)) is below the reward of
  every e-vertex and of c_W, which rules out Λ_t(v) being an e-vertex or c_W. ∎
DATA (bonly221.py; unit: (state, vertex) pairs; set: 170 runs = the §4 corpus + R221's ladder and adversarial climbs; scope: own.py):
359,866 pairs, 0 with Λ at or above an e-vertex; 0 gate ties.
Consequences (PROVED, lane):
- No gate ties. Suppose Ω(e_g) = Ω(β_g). By B-ONLY, Λ is below e_g, so e_g ∈ Π(e_g). Equal Π then needs e_g ∈ Π(β_g), so the
  β-play passes g and e_g, and then k(β_g) > k(e_g). So LOC-GATE's hypothesis «Ω(e_g) ≠ Ω(β_g)» always holds: σ̄_t(g) is the
  ⊴-smaller face at EVERY gate and EVERY state.
- QUIET: every class is a B-class, so (Q3) is vacuous and L can be (M + 1)(2M + 1)(N + 1). The N(n − 1) term is not needed.
- GAP in QUIET, closed here. (Q5) counts «G_C changes at most 2M times» and «a sub-window ends only at a flip, which needs a change of
  a β-face value». Both hold only if a gate never flips at a tie, while R118 lets σ̄ be «any fixed deterministic choice». With no
  gate ties (above) both statements hold as written. Without B-ONLY the repair would be to put both faces of a tied gate into G_C.
- R219 GATE-POLY: H_g = 0 at every gate (no shared cycle node above e_g). R221 RHO-COUNT: [BELOW] always holds, A_g = 0. So
  ρ_g ≤ (2M + 3)·F′_B(M) at every SET gate, with B the max ascents of y's plays.
- Λ takes at most M + 3 values per vertex (β's, K1, K2, c_X), not 2M + 3.

## 4. QUIET: data and the Bellman-Ford step (quiet221.py; DATA)
quiet221.py is my own implementation of classes, loud steps, windows, D^tot_E and the bound L = (M + 1)(2M + 1)(N + 1) + N(n − 1).
Unit: runs (and quiet windows inside them). Set: 123 runs: L-RED r217-r221 inst/ (LEAP_k64 and LEAP_k32 included), R221 climbs,
box 191 inst/ (DEAD_SEG2P_d4/d7/d9, cyc*), box 192 inst/ (rd2_*, rd3_*, rf_*, cR_d2_w8_R22, DEAD_SEGT_n20), L-SI box 81 / box 82 inst/
(claude/l-si 9574f538: H5_d20_F62, H6_d24_F126, L6Z_KILL238_d28, SL41_d28, rd*, rf_d4, RS2*, FPORT_n2, RSG_K4, HS2_d3). Scope: own.py.
Counter: W > L 0; T > Q + (Q + 1)L 0; Q > Σ_v (D^tot_E(v) − 1) 0; a vertex re-entering a class it had left (CONVEX) 0; a σ̄ flip on a quiet
step at a gate whose faces are in different classes (Q1) 0; E-class value changes > n − 1 in a window 0. Longest window: W ≤ N in
every run, with equality on DEAD_SEG2P_d4_N8 (W 8, N 8; box 191 inst, sha1 c8be0e60…, copied to r221q/inst). File out/quiet_corpus.txt.
Bellman-Ford step (Q5), re-read. G_C uses chosen faces only. DOM gives the first edge. F3 at g and at the face; induction + F1 for the
rest. F4′ at x, g (CN2) and at the face (it would lie on z's cycle). Boundary values are constant by the induction on |S| (e-faces into
(w, S ∖ {e})), and the exit and w are constant. A simple G_C-path has ≤ N movers. With B-ONLY there are no ties, so G_C changes ≤ 2M
times. I found no gap beyond the tie remark of §3. Quiet-window climbs (SCORE=quiet, goq.sh) are in §8.

## 5. (c) T-QUIET's accounting
- A class is (Λ, E). A Λ change with the same E is a class change, and it is counted. D^tot_E(v) counts distinct classes, i.e.
  Σ over Λ-intervals of D_E,I(v). This is exactly what HUB-ASC-G bounds per Λ-interval, so UP-T's product (#Λ-intervals)·F′ is
  right (with B-ONLY: ≤ M + 3 intervals).
- Convexity: with equal Λ, a value between two values of one class must have the same e-part. Otherwise the most relevant differing
  e decides both comparisons the same way, because every non-e above an e is c_W, K0 or K3, common to both or absent. So by F1 each
  class is one interval of states. DATA: CONVEX 0 (§4). Q ≤ Σ_v (D^tot_E(v) − 1) holds; DATA 0 failures.
- No double count and no missed count found.

## 6. DEAD constant IN-BOUND (in221.py; DATA)
Unit: distinct values of one vertex inside one maximal stretch of constant class. Set: RS2(L, 6) for L = 4, 8, 16, 32 (r217/rs2.py,
generated into r221q/out/; RS2_L8M6 = r217/inst). Scope: own.py. Counter: max distinct values = 6, 10, 18, 34 = L + 2, i.e. IN (changes)
= L + 1. CONFIRMED.

## 7. (d) Does IDEAL-CYC's T bound N5′-xi on Γ3? GAP (for the reading; box 194 does not claim it)
- Landed: R118 REACH3-CYC is CONDITIONAL. It needs P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3 and W3 for every genome. R117 signs ESC3
  and W3 only for acyclic Ξ-graphs; R117's line states S3-START and PAD only for acyclic Ξ-graphs. Under those premises, N5′-xi
  makes Howard steps at the movers only «until its first fallback». The equality «Γ3 mover sequences = IDEAL-CYC run, xi = T + 3» is
  context DATA in R118 (1,271 of 1,300 random genomes; the other 29 diverge at exact VJ ties), not a clause.
- DATA (div221.py; unit: genomes; set: 2,150 random Ξ-cyclic genomes, brute221.rgen with d 1-4, width 1-3, degree 2-3, seeds 1-3; scope:
  own.py vs box 191 idealcyc vs N5′-xi = box 190 n5v.py mode xi on box 189 gamma3.build(G, all pads)): own = idealcyc trajectory in all
  2,150. n5v's iteration count ≠ T + 3 in 11.
- Frozen (r221q/inst/SHA1SUMS; traces out/trace_DIV_*.txt):
  - DIV_2_493 (N 2; sha1 113a0e24…): IDEAL-CYC (0,0) → (0,1), T 1. Γ3: (0,0) → (0,2) → (0,1), fallback at iteration 3, then mover 0
    switches at iteration 5 → (1,1). xi 5. At state 0, options 1 and 2 of mover 1 tie exactly (own values).
  - DIV_2_583 (N 2; sha1 0302abaa…): IDEAL-CYC (0,2) → (0,0) → (0,1), T 2. Γ3: (0,2) → (0,1), fallback at iteration 2, then (1,1) at
    iteration 4. xi 4. Options 0 and 1 of mover 1 tie at state 0.
  - DIV_3_717 (N 12; sha1 1e4c0d16…): different from iteration 1; fallback at iteration 5; movers change again at iteration 7.
- Reading of the data:
  - Before the fallback, Γ3 follows a different Howard run (another tie choice). At DIV_2_493's state (0,2), option 1 is strictly
    better than option 2 in IDEAL-CYC, so the second Γ3 step is a strict Howard step. QUIET's proof uses DOM and STRICT only, and
    these hold for every tie rule that keeps the current option when it is among the best. So T-QUIET applies to that run as well,
    PROVIDED REACH3-CYC holds for the genome.
  - After the fallback, N5′-xi keeps changing movers (all three instances). Nothing in box 194 or R118 bounds those iterations.
- So UP-T bounds the pre-fallback part of N5′-xi on Γ3 for [E-LEV] genomes with bounded U(G), and only conditionally on REACH3-CYC's
  premises. It says nothing about N5′-xi's total iteration count, nor about N5. A packet P-N5-QUIET should state its scope as IDEAL-CYC
  (any Howard tie rule that keeps a best current option). The Γ3 transfer, if wanted, should be its own clause, with REACH3-CYC's
  conditions and «until the first fallback».

## 8. Quiet-window climbs (goq.sh; DATA)
SCORE=quiet: score = (QUIET-counter failures, longest quiet window W, T); ladclimb mutations (Ξ-cycles allowed). Unit: best genome of
one climb (2,500 iterations). Set: Q24, Q33, Q42, Q43 (random seeds, N 8, 9, 8, 12). Scope: own.py. Counter: quiet221.meas.
Best W = 4, 8, 7, 9 (W < N in all four); QUIET-counter failures 0. Together with §4 (max W = N on DEAD_SEG2P_d4_N8), no quiet window
longer than N has been seen; L (cubic) is far from tight, as box 194 says.

## 9. Recommendation
P-N5-QUIET can be frozen on LOC-GATE, LOC-K2, CN2, QUIET, T-QUIET, UP-T (under [E-LEV]) and ASC-T, with these changes:
1. Add B-ONLY, or note the tie case of (Q5) and repair it by putting both faces of a tied gate into G_C.
2. Optionally drop the N(n − 1) term of L.
3. Limit the scope to IDEAL-CYC; the Γ3 / N5′-xi reading per §7.
4. Name [OPT]'s landing as a Lead reading.

## 10. POST-FALLBACK (Lead 00:36Z, next target (a)): one fallback, then exactly 3 iterations (DATA; CONJECTURE ENDGAME-3)
Tools: experiments/red/r221p/ (post221.py logs every iteration of N5′-xi = box 190 n5v.step mode xi on Γ3(G) = box 189 gamma3.build(G,
all pads); rpost221.py random genomes; ladclimb.py SCORE=post). Phases = maximal runs of iterations between fallbacks.
- DATA. Unit: N5′-xi runs on Γ3. Set: 3,000 random Ξ-cyclic genomes (brute221.rgen; seeds 1, 2; d 1-5, width 1-3, degree 2-3) plus 137 runs
  of the §4 corpus and R221 climbs. Counter: (#fallbacks, iterations after the first fallback incl. it, mover changes among them).
  Every run: exactly 1 fallback, exactly 3 iterations from it to the end; mover changes 0 / 1 / 2 in 567 / 2,486 / 84 runs (random:
  558 / 2,362 / 80; corpus 9 / 124 / 4). τ never changes after the fallback (0 in all runs). Files r221p/out/rpost_{1,2}.txt,
  out/post_corpus.txt.
- Adversarial climbs (gop.sh; score = (#fallbacks, post-fallback iterations, post mover changes, xi); 700 iterations; N 8-10; 4 runs):
  best (1, 2 + fallback = 3, 2) in every run. No second fallback and no longer endgame was found.
- Mechanism (traces of rd3_d4, post_1_44, post_1_13; READING):
  - The fallback (S4c) applies σ-switches K0 → K1, sometimes with β → pad-to-K0 switches.
  - Next iteration: K1 → q, which closes the core cycle K0 K1 q with top K0 (even, top + 2), plus 0-1 mover switches.
  - Last iteration: every Even vertex that can reach the core does so (β → pad, movers, K3). Then neither side has an improving
    switch; Even wins all but one vertex (rd3_d4: 157 of 158).
  - So K0 → K1, improving from the start, is held back by S4a's arena step until the movers converge. The fallback releases it, and
    the game is then decided in two steps.
- CONJECTURE ENDGAME-3. On Γ3(G) for every genome G, N5′-xi has exactly one fallback, and terminates exactly 2 iterations after it. If it
  holds, N5′-xi's total iteration count on Γ3 = (pre-fallback iterations T3) + 3. With REACH3-CYC (CONDITIONAL) and T-QUIET / UP-T
  (box 194, SURVIVES), that count is polynomial for [E-LEV] genomes with bounded U(G).
- Not proved: a proof needs SPEC S4a / S4c's arena semantics at the core (why the arena step never applies K0 → K1 while some mover
  improves, and why the Even-top core cycle ends the game in one best-response step). Next step if the Lead wants it: write ENDGAME-3's
  proof from SPEC's text (docs/new/N5-ssi-global.md) with the K-gadget of R117.
- Instances: the 80 random genomes with 2 post-fallback mover changes are in r221p/out/post_*.json (not frozen as kills; no kill).

## 11. (i) BREAK ENDGAME-3 (Lead 01:12Z): no counterexample; the mechanism as a proof skeleton for L-NEW
Tools: r221p/spost221.py (structured families aimed at the core), gos.sh. Unit: N5′-xi runs on Γ3(G). Set: 1,800 genomes, 300 per family:
- esc: 70 % of the Ξ-targets are X, so many gates feed K.
- noesc: no X targets.
- deep: d 6-9, width 1-2.
- dense: degree 3-4.
- late: every mover starts at its option of LEAST final IDEAL-CYC value, so movers converge late.
- lvl0: 2-4 extra level-0 movers, degree 3-4.
Fixed seeds 61-66. Counter: (#fallbacks, post-fallback iterations, post-fallback mover changes, τ changes after the fallback).
Result: 0 hits. Every run is (1, 3, 0-2, 0) (out/spost_*.txt). With §10: 4,937 runs, 0 counterexamples. Nothing frozen (no kill).
Skeleton (each step with what the attempts could not violate; S4a = arena step, S4c = fallback, Is / It = improving switch sets of
σ / τ computed with the opponent's best response, as in box 190 n5v.step):
- E0. τ is constant on the whole run. Start τ = every gate on its e-pad, K2 → K2. It = ∅ at every iteration (rd3_d4 trace: 0 τ
  changes; 4,937 runs: 0 τ changes after the fallback). WHY is open: the dual improving set is empty at the S3 start and stays so. L-NEW
  should prove it from S3-START / TAU3 (R117).
- E1. K0 → K1 ∈ Is at every state, and S4a never applies it. Genome-independent; this is a READING with the reason, not a proof yet.
  - Under Odd's best response, K2 → r → K1, so K0 → K1 → s → K1 has Π = {K0} (even, top + 2). K0 → pA → K3 adds K3 (odd, top + 3).
    So K0 → K1 is improving.
  - S4a's arena evaluates against the CURRENT τ with K2 → K2. There K0 → pA → K3 → K2 ends in Λ = K2 (reward −3), better for Even than
    Λ = K1 (reward −5). So the arena keeps K0 → pA.
  - Hence K0 moves only at a fallback. No family changed this, and the late family (movers converging late) only shifts T3.
- E2. The first fallback happens exactly when the mover phase has converged, i.e. no σ-change at movers or β's in S4a. REACH3-CYC
  (CONDITIONAL) gives «Howard steps until the first fallback». S4c then applies Is: K0 → K1, plus β → pad switches that are already
  improving.
- E3. Next iteration: K1 → q becomes improving and the arena takes it. K0 K1 q is a cycle with top K0 (top + 2), which does not
  involve K2, so the current τ and the best response agree. 0-1 mover switches happen alongside.
- E4. Last iteration: every β → pad → K0 escape and the remaining mover / K3 switches are applied in one S4a step. After it Is = It = ∅.
  - The data says one step always suffices (4,937 / 4,937). The reason to prove: after E3, every improving σ-switch is an escape into
    the top cycle or a re-choice among c_W-plays under the fixed all-e τ.
  - Open sub-question for the proof: can an S4a step leave a NEW improving switch, i.e. a chain effect through an escaped β? None was
    seen, including deep (d ≤ 9) and dense (degree 4) genomes.
