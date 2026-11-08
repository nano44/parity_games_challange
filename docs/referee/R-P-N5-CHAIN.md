# R-P-N5-CHAIN: first referee report on packet P-N5-CHAIN (L-NEW successor 64)
REFEREE successor 29 (Opus 5.5, D15). date -u at writing 2026-11-08T09:15Z. Independent: docs/referee-2/ not read; L-RED's R224-chain.md not read
before this verdict was written (see §8 for the comparison afterwards). Draft notes (DRAFT, d49281a7) were written on box 196 before the
freeze; this report replaces them and is against the frozen text.

## 0. Verdicts
| statement | packet label | verdict |
| --- | --- | --- |
| ESC3-ALL, W3-ALL, Theorem REACH3-ALL (§3) | PROVED, every genome | SIGN |
| Facts F1, F3, F4′, F5, F6, DOM, STRICT, F2, CYC on HOW3(G) (§4) | PROVED, every genome | SIGN |
| CN2-3, LOC-GATE3, LOC-K2-3, B-ONLY3, NO-TIE3 (§5) | PROVED, every genome | SIGN |
| Theorem QUIET3, Corollary T-QUIET3 (§6) | PROVED, every genome | SIGN |
| E-MON3, CHAIN-DECOMP3 (§7) | PROVED, every genome | SIGN |
| Corollary HUB-ASC-G3 (§7) | PROVED, CONDITIONAL on P-N5-ASC §4 (R121) | SIGN as conditional on P-N5-ASC §4 |
| UP-JUMP3, UP-B3 (§7) | PROVED under HYPOTHESIS [E-LEV] | SIGN under HYPOTHESIS [E-LEV] |
| Theorem CHAIN3 (§8) | PROVED under HYPOTHESIS [E-LEV], CONDITIONAL on P-N5-END (ENDGAME-3) and P-N5-ASC §4 | SIGN with that label (it lands only after P-N5-END and R121 land) |
| DEAD RUN-TRANSFER (§8) | DEAD, instance RT_n1 | CONFIRMED (own engine: exact tie in both games) |
| §9 DATA / line L-1 | not to sign | DATA replayed EQUAL / all 0 with my own engine; L-1 NOT YET: CL-1 required (§5); packet note CN-1 for the fixes entry |
- No GAP in any proof. My draft's CH-1 ([OPT] source), CH-2 ([E-LEV] a hypothesis) and CH-4 (conditional label) are answered in the
  frozen text (§1 [OPT], [E-LEV]; To-sign table; CHAIN3's heading). CH-3 (bit cost) is now a READING. CH-5: see CL-1.
- Every row is under the standing SPEC premise 1E-N3 (R57 (b)), as the packet says, which is the convention of R104 / R117.

## 1. Objects
- claude/l-new 93531b03 (packet) and 71b75424 (L-1), both ancestors of origin/claude/l-new (checked).
  - docs/new/P-N5-CHAIN.md: sha1 6e613ba762b6ecf67247ef6d8674b4c960013039, 38,551 B, 348 lines. Unchanged at 71b75424.
  - L-1 docs/new/P-N5-CHAIN-line-L1.txt: sha1 bd152dd9c71ea47dbc7fa6655a9a18a87908781a, 8,124 B, one line, 158 «(» = 158 «)», no «|».
  - Both EQUAL to the Lead's check.
- experiments/new/box196/chain.pins at 71b75424: 51 rows, all match.
- check196.sh re-run at 71b75424: see §4 (D).

## 2. Premises (§1), by my own script
- scratch/chain_quotes.py, joined lines, fragments split at «…»; trunk sources by git show; lane packets at their frozen / line commits.
  - §1: 22 of 22 quotes found verbatim (chain_logs/quotes_sec1.out).
  - L-1: 3 of 3 (quotes_L1.out).
- [ASC]'s constants F′_0 = 1 + M(M + 1)/2 and F′_B = (M² + 3M + 1)(1 + M·F′_(B−1)²): P-N5-ASC l. 151-152 (e28e962d). EQUAL.
- [OPT]: R118's σ̄ / R21 (a) for HOW3's σ̄_t, a defined object. [1E-N3] is used only for the SPEC procedure's outputs (S4a's arena,
  REACH3-ALL). This is the split my predecessor ruled for P-N5-QUIET (QT-L1) and I ruled for P-N5-END (§2.2). CORRECT.
- [E-LEV]: a HYPOTHESIS, used only by UP-JUMP3, UP-B3 and CHAIN3. CORRECT (QT-L3).
- [END] (P-N5-END ENDGAME-3; my SIGN, R-P-N5-END) and [ASC] §4 (R121 pending) are unlanded lane packets, and the labels say so.
  P-N5-QUIET is a template only: §5-§6 re-prove each step on Γ3, checked in §3 below.
- [TERM] R15 (a) for F1, replacing R118 (b): the Howard switch set is a non-empty unambiguous set of improvements of σ_t in Γ3 (valuation
  on the full game, non-movers fixed by σ_t). CORRECT.

## 3. Proofs, each step re-derived (the frozen text; my draft's derivations of box 196 carried over and re-checked)
- (R), (P), (E-DOM), (Core) (§2): from [DEF] and [G3]. (P) needs: every cycle inside the core contains K0, K1 or K3 except K2's loop
  (Ω 3); a cycle through a mover passes a face of Ω ≥ 6 (e or β); c_X has no in-edge but its loop. CORRECT.
- ESC3-ALL: in H, every play from xt(g) leaves each gate by pe (τ), descends one level per e-step and ends at c_W (even); pb_g leads into
  the core and ends in an odd cycle. β_g is on no H-cycle (pβ_g its only in-edge, entered only from a gate, which plays pe in H). So the
  optimum and TIE(β_g) = {xt(g)}; TIE(K0) = {pA} (node K2 vs K1); K1, K3 have A = {σ} (only (K0, K1) is improving, K3 (b)). CORRECT.
  No Ξ-property is used: the Ξ-edge β_g → xt(g) is named only as an edge.
- W3-ALL: lengths 5ℓ + 5 / 4 / 3 / 2 / 1; every H-play from a pad of x has length 5ℓ + 4 and node c_W whatever the lower choices; x on no
  H-cycle; TIE(x) = A(x). CORRECT.
- REACH3-ALL: the induction is R118 (k)'s (P-N5-XICYC §7) with ESC3-ALL and W3-ALL. A(x) contains every strictly better successor, so
  the Ξσ-best element of TIE(x) = A(x) is ⊴-best: a Howard step; ties are kept because A(x) = {σ(x)} when nothing is strictly better. At T3,
  σ_new = σ, τ_new = τ, Iσ ∋ (K0, K1): S4c fires. CORRECT. Remark (N5 not Howard): consistent with R-P-N5-END §4 (C).
- §4 facts: F1 by R15 (a) (Howard switches exactly the strictly improving movers, one each); F3, F4′, F2 from [VJ]; F5 by definition;
  F6 from (P); DOM and STRICT as written (x ∉ any Π by CN2-3). CYC: possible nodes are the M e's, M β's, c_W, K1, K2 (c_X only for c_X).
  CORRECT.
- CN2-3, LOC-GATE3 (P-N5-QUIET §3's case analysis; on Γ3 it needs only [OPT], F3, F4′ and «g not a cycle node, in no Π»), LOC-K2-3
  (σ̄(K2) = r; Ω(r) = (K1, ∅, 1) ◁ (K1, ∅, 2) = Ω(K2), node odd), B-ONLY3 (under τ_β the only e-vertex a play can meet is at its start;
  reward(Λ_t(v)) ≤ that node's reward, which is below every e's; so Λ_t(v) is not an e, c_W or K0, K3 is never a node, and by (E-DOM) Λ_t(v)
  is less relevant than every e), NO-TIE3 (k(pβ_g) > k(pe_g) when e_g ∈ both Π's). CORRECT.
- QUIET3 / T-QUIET3: every substitution in (Q1)-(Q6) checked against P-N5-QUIET §4 (559cdffc l. 128-163):
  - (Q2) CN2-3 covers the pad m.
  - (Q4) pβ_g → β_g → z with one class; pe_g → e_g → y. The exit through pb_g is constant by LOC-K2-3.
  - (Q5) the e-face value is ext(pe, ext(e, Ω(y))). «Flips at most once» holds by NO-TIE3: the β-face only rises against a constant
    e-face. Bellman-Ford needs F3 / F4′ at m, g, the face pad and the face, none in Π.
  - (Q3) / (Q6) with n3, so L3 as stated.
  - No step uses the tie rule.
  - CORRECT.
- E-MON3, CHAIN-DECOMP3: as P-N5-ASC §3, with (Core) (K0, K3 both or neither) and CN2-3 (pads not in Π); e → W-target is unpadded.
  CORRECT.
- HUB-ASC-G3: P-N5-ASC §5's reduction to CS(M_w) (items active on intervals by F1 / F2; forest by CHAIN-DECOMP3; lex-monotone by E-MON3;
  M² + 3M + 1 levels), then [ASC] §4. Whole run ≤ 2M + 3 nodes (CYC). CORRECT, given [ASC] §4.
- UP-JUMP3: b = e_(x′,k′) with x′ on the play (e's only in-path is x′ → m → g → pe → e); [E-LEV] contrapositive gives lev(x′) ≥ ℓ; levels
  change only at e-steps (−1) and Ξ-steps; a β → pb step never returns. So the first step reaching a level ≥ ℓ is an upward Ξ-step from the
  β's own mover. UP-B3: segments are disjoint parts of the prefix, and each β has one Ξ-edge. CORRECT.
- CHAIN3: REACH3-ALL (F = T3 + 1) + [END] (total F + 2) + T-QUIET3 + UP-B3 / HUB-ASC-G3. The arithmetic and the size remark
  (n3 vertices, priorities below top + 4 = O(M)) are CORRECT. deg_M F′_B = 5·2^B − 3 (my own count; the packet leaves it as a READING).
- DEAD RUN-TRANSFER: own engine on RT_n1 (chain_logs/rt_n1.out): at state 0 options 1 and 2 have equal values in Γ (c_W node, P = ∅,
  length 4 / 4) and in Γ3 (8 / 8), cmp = 0 in both. So the run depends on the tie rule; my tie rule gives 2 / 2. The packet's T3 = 1
  under SPEC's root-first tie is not re-run by me. The DEAD conclusion «T_CYC is not one number» holds. CONFIRMED.

## 4. Replays with my own code (scratch/chain_replay.py; chain_logs/)
- (A) HOW3 engine:
  - My Γ3 builder (xicyc_replay.build, pad=True); non-movers frozen at the standard state; Odd by my VJ best reply; Howard steps with my
    tie rule.
  - Counters: CN2-3, NO-TIE3, LOC-GATE3, LOC-K2-3, B-ONLY3, QUIET3 (wfail, Tfail, crossflip), T-QUIET3's second bound (tqfail), E-MON3,
    CHAIN-DECOMP3, UP-JUMP3, UP-B3, CYC's 2M + 3.
  - REACH3-ALL on my N5′-xi engine (end_replay.py, mode xi): nonstd, nohoward, fbpos.
  - Genomes: own generator (rand, selfl, deep, wide, acyc × 400, seed 2961) plus the 61 pinned genome files of box189 and box191-196.
  - 2,061 runs, 1,580 of them Ξ-cyclic: every counter 0. Max T 129, max W 32: EQUAL to §9's maxima (chain_logs/sweep.out).
- (B) Controls fire:
  - ctrl1 (L3 := 0, U := −1): wfail 22, Tfail 21, upfail 23,455 in 100 runs.
  - ctrl2 (LOC-GATE3 order reversed): locfail 2,795. (CTRL=2 also starts my N5′-xi engine off S3, so nonstd / fbpos / e0fail fire there
    too.)
  - tqfail has no firing control in my replay either. As in the packet, it is not cited as a fail counter.
- (C) RT_n1 tie: above.
- (D) The lane's check196.sh at 71b75424, re-run in a detached worktree: byte-identical to check196.out (17 lines, 1 min 49 s;
  chain_logs/check196_rerun.out).

## 5. DATA rule on L-1, clause by clause; required change
| clause | pinned output | verdict |
| --- | --- | --- |
| unit, tool, scope, families | qt3_196.py, check196.sh | OK |
| set: 8 × 500 × seeds 1961, 1962 = 8,000 runs + 58 pinned genomes | sweep196.out: 16 family rows; 57 genome rows + RT_n1 (rd3_d4 twice, from box192 and box194; DEAD_SEGT_n20 «skipped», not a genome) | OK |
| REACH3-ALL ... UP-B3 counters 0 with units | sweep196.out, every row | OK |
| longest quiet window 32 (RS2_L32M6); max ascents 4; max T3 129 (LEAP_k64) | sweep196.out | EQUAL |
| controls: ctrl1 wfail 32, Tfail 22, upfail 26,477 in 50 runs; ctrl2 locfail 3,320; ctrl3 bonly 2,269; spec nohoward 599 / 911 | check196.out (ctrl1-3: rand, seed 1963, 50 runs) and sweep196.out (spec: seed 1963, 200 runs) | numbers EQUAL; the set of the controls and of the spec rows is not named → CL-1 |
| «controls fire (every fail counter has one)» | ties (NO-TIE3's counter) is 0 in every ctrl / spec row and is not among ctrl196's five injected counters (nonstd, cnlow, k2fail, crossflip, emon; grep: 0 occurrences of «ties» in ctrl196.py / ctrl196.out) | FALSE as worded → CL-1 |
| 75 of 75 (15 genomes × 5 counters) | ctrl196.out: 15 «CTRL224» rows | EQUAL |
| tdiff 100 of the 8,000 runs | sum of the xi family rows of sweep196.out | EQUAL |
| L-RED R223-reach / R224-chain cited, not re-run | labelled so | OK |
| scope: not M3 / M4 / step 4; G-N5-TIME OPEN; CANDIDATE (D1) | | OK |
- CL-1 (required; one span, scratch/chain_linefix.py):
  - old «controls fire (every fail counter has one): ctrl1 (L3 := 0, U(G) := −1) wfail 32, Tfail 22, upfail 26,477 in 50 runs; ctrl2
    (order reversed) locfail 3,320; ctrl3 (no excluded vertex) bonly 2,269; spec mode nohoward 599 (rand, 200 runs) and 911 (dense, 200
    runs);»
  - new «controls fire (every fail counter except ties, NO-TIE3's counter, which has none): ctrl1 (L3 := 0, U(G) := −1) wfail 32,
    Tfail 22, upfail 26,477; ctrl2 (order reversed) locfail 3,320; ctrl3 (no excluded vertex) bonly 2,269 (each control on 50 runs,
    family rand, seed 1963, check196.out); spec mode, seed 1963 (data/sweep196.out), nohoward 599 (rand, 200 runs) and 911 (dense, 200
    runs);»
  - The old string occurs once in L-1. L-1 + CL-1: sha1 e481d260884807424c545bd3f3cdd7fbfb25f05c, 8,248 B, one line, 160 «(» = 160
    «)» (chain_logs/linefix.out).
  - Form B, also acceptable: add a firing control for ties (e.g. a fault that equalises the two face values in the counter's view, as
    ctrl196 does for the other five) and keep «every fail counter has one».
- CN-1 (for the fixes entry; the packet is frozen): §9's «(each fail counter of §5-§7 has a firing control: …)» is false for ties in the
  same way. The fixes entry should say so (or add the control, Form B).
- Optional CO-1: L-1 says «each PROVED (every genome)» before a list that includes HUB-ASC-G3 (conditional), UP-JUMP3 / UP-B3 (under
  [E-LEV]) and CHAIN3. Each later item names its own condition, so it is not false, but «each PROVED (every genome; conditions as named
  below)» would read better.

## 6. TARGET.md diff
- TARGET.md §2 (M4): polynomial on EVERY parity game. §4: «Polynomial only on a restricted class» is not M4; «Correctness or running time
  resting on an unproved conjecture …» is not M4.
- CHAIN3 is an iteration bound for one algorithm on {Γ3(G) : U(G) ≤ B} under a HYPOTHESIS and two unlanded premises. The packet says «Not
  M3, not M4, not a step-4 pass. G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1)». CORRECT.
- D1: nothing here is an algorithm claim on general games.

## 7. Landing order
CHAIN3 and HUB-ASC-G3 can land only after R121 (P-N5-ASC) and, for CHAIN3, after P-N5-END lands. The other rows (§3-§7 without
HUB-ASC-G3) depend on landed RESULTS only (R15, R57, R104, R117, R118, R21) and can land on their own.

## 8. After the verdict: L-RED 58 R224-chain (context, not a signature)
- Read after §0-§7 were written: docs/red/R224-chain.md at claude/l-red e7937985.
- Its verdict is the same: every statement SURVIVES. CHAIN3 «follows exactly». DEAD RUN-TRANSFER AGREE.
- It reads §4 (E-MON3 … UP-B3) «not re-derived line by line». I re-derived them (§3 above).
- Its §5 builds controls for «the five uncontrolled counters» (nonstd, cnlow, k2fail, crossflip, emon), the box's own list. That list
  does not contain ties, which also has no control. So L-RED's and the packet's «every fail counter has one» both miss it: my CL-1 / CN-1.
- Nothing in R224 changes a verdict here.

## 9. Tools and outputs (committed, docs/referee/scratch/)
chain_replay.py, chain_quotes.py, chain_linefix.py, end_replay.py (hook); chain_logs/: sweep.out, quotes_sec1.out, quotes_L1.out,
linefix.out, rt_n1.out, L1.txt, P-N5-CHAIN.md (the frozen packet, copied for the quote script), check196_rerun.out.
