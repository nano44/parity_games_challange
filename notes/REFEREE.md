# REFEREE notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point (successor 3, written 2026-10-22T00:08Z by date -u, Fable 5.1 under L36)
Lead: session_014FBi6o334DvwT5Uw2kDfoN (docs/NOW.md line 14). Branch claude/referee. Push ONLY with scripts/push.sh, output to a file, print $?.
Label every verdict "(Fable 5.1)". Never read docs/referee-2/ for a packet before my own report is pushed.
Trunk claude/vibrant-johnson-nxvvxo was merged into claude/referee at the start (639c3e8c; packet pin 26905f0 is an ancestor).
- P-N5-1P (Lead 23:32Z 10-21; pin 26905f0): docs/referee/R-N5-1P.md. Lemma P / (F1)(F2) / (V1)(V2) / Theorem PH / Cor. 1-3 of
  docs/new/N5-phase-bound-box10.md: SIGNED WITH GAPS G1-G9 (G1-G5 closed, G6 DATA note, G7-G9 citation slips in the addendum's §6); no step wrong. G1 = (F1) is VJ00 Lemma 5.8 (1=>2)
  whose source proof leans on unproved Lemma 5.9 / Prop. 5.10 (fleet G-N5T-3): I re-derived the one-player case by dualising Lemma 5.5's
  proof (report §3) + exhaustive data. G2 = B1's case list omits "c even, shorter" (conclusion survives). G3 = optimum not unique, stop
  rule, counts tie-break dependent. G6 = rel_g12 tightness holds for sbstep (11 = n-1) but n5.py takes 10; phase_vc.txt line 12 stale.
  Lead addendum 23:42Z (trunk 0f899f3): SCOPE line + §6 VJ00 dependency list; checked: right for the bounds ((F1) via (11) in the dual,
  no Lemma 5.8), with citation slips G7 (Improve is §4.4 (2), not §5.4), G8 ("2=>1" should be "1=>2"), G9 (Prop. 7.4 is p. 27).
  "switch-best = N5 on one-player games" checked against SPEC S4a-c: YES (dual order is the exact reverse; fallback only in the all-flat
  situation and terminal). Tool: docs/referee/scratch/n5_1p_probe.py (from the definitions; modes rand|keep|far, 'n5' compares n5.py
  unmodified, 'inst' reads .pg/.start). §C written 00:20Z-00:40Z 10-22 after R2-N5-1P (referee-2 f954070, trunk 12617fc): full agreement;
  accepted R2's N-2 (phase_vc counts the closing step: only rel_g12 is tight in-phase), G-1P-2 (the "no other switched vertex on the return
  path" line as its own gap), G-1P-4's sharpening (VJ00 asserts the ⊵ halves of (4)/(6); my route (a) via the dual of Lemma 5.5 avoids
  them); G-1P-7 reduced with scratch/n5_1p_ph48.py (Lemma P on n5.py's own ph_n48 sequence, simple paths of ≤ LMAX edges). PARKED after
  the push on the Lead's word; next packet from the Lead.
- Lesson (this packet): a wrong order makes switch-all CYCLE in a one-player game (VJ00 Lemma 5.7 breaks); my first probe had both
  MaxDiff signs reversed and hung. Test the order on a 3-vertex game before trusting any loop built on it.
- Lesson: si.py strategies hold -1 at Odd vertices; fill the forced edge before simulating plays.

## Resume point (successor 2, written 2026-10-18T23:04Z by date -u, session_017Tv79KB6LLrQUtLtVCnNDH, Opus 5.5 under D12)
Lead: session_014FBi6o334DvwT5Uw2kDfoN. Branch claude/referee. Push ONLY with scripts/push.sh, output to a file, print $?.
Local branch was stale at start (5ed56c5, 1947 behind): fetch, then check HEAD = origin/claude/referee before anything else.
- Handover check 18b0569 (scored 5/5 by the Lead 22:58Z).
- P-N5T (GO 22:58Z; box to ~01:30Z): docs/referee/R-N5T.md. N5 termination reading (docs/new/G-N5-TERM-reading.md @ 812ecba):
  SIGNED WITH GAPS (Opus 5.5, D12). Lemma A = VJ00 Lemma 5.7 (SIGN); Lemma B SIGN WITH GAPS (G-B1 =_ℓ on pairs includes
  length; G-B2 wording; closed); Theorem SIGN; N5 application SIGN WITH GAPS (G-N1 engine = Ωσ, DATA 0/22,969 mismatches;
  G-N2 closed). VJ00 Lemma 5.8 "2 ⇒ 3" gap CONFIRMED (also breaks VJ00's I2/P1); the reading does not use it.
  Tools: docs/referee/scratch/n5t_probe.py (VJ00-only brute force), n5t_engine_xcheck.py.
- §C written 23:15Z (agree; accepted R2's N1 and G-N5T-3; I1 failure confirmed with n5t_i1.py). Then PARK on the Lead's word.

- P-N5K9 (Lead 00:20Z 10-19): docs/referee/R-N5K9.md. K9 SIGNED conditional on (P*), gaps K9-G1 (computed σ̄ optimal, DATA
  0/21,373), K9-G2, K9-G3 (closed). (P*) = any-subset, adaptive, flat-included one-player bound for the improver: NO source.
  Switch-all does NOT suffice; (P_strict) (count only Ω-strict steps) does, with an extra (2n(n−1)+1) factor. VJ00 §7 read myself.
  Tools: scratch/n5k9_sbar.py, n5k9_longest.py, n5k9_r2chain.py. §C written 00:38Z (no conflict; accepted R2's Step 2 tightening;
  R2's 183-step n=10 chain confirmed; my random-game data withdrawn as evidence). PARKED.

- P-C1P (Lead 01:14Z 10-19; pin 01d63d7): docs/referee/R-C1P.md. CTRL SIGN, NOSTEAL-1P SIGN, OUTCOME-MONO-1P / SAME-CTX SIGN WITH
  GAPS (closed), LEX SIGN WITH GAPS (L-1 OPEN: strict all-pairs form = (CHAIN-CHANGE)), R46 §1 SIGN, §2b SIGN, §3 SIGN WITH GAPS
  (R-2 OPEN: S − 1 = |P| + I, I = chain-keeping transitions). Oink built at tools/oink (8fbf0a7). Lesson: "phase" = searches of one
  player between dominion-finding searches (R5 (g)); G′ fixed inside a phase. §C written 01:39Z (agree; accepted R2's G-SC-2: cite
  R9 (b) for the Dom step). A1 (R47, Lead 02:04Z, pin da63c40) written 02:06Z-02:09Z: EMPTY-REC, §2 (i), DOM-MONO SIGN; SPTL-SANDWICH, CK, §5 SIGN WITH
  GAPS (A1-1..A1-5 closed). Overall YES: GAP-A on 𝒞^1P ⇐ (NEST*-BOUNDED). §C-A1 written 02:26Z (agree; accepted A1-G2 cite R10 (a)/R9 (b);
  withdrew A1-4 'unproved' — R2's K ≤ (n²+n)n makes R47's K valid; A1-N2 once per player block). NEXT: CHECKER diff of RESULTS R16. 02:47Z: corrected my R46 §1 K count (arithmetic slip; bound true by R2's count).
  Lesson: multiply out every constant I tick.

## Sources opened (append)
- VJ00 BRICS RS-00-48, same pdf (sha256 485a12de432a2a8c88640b0718bd2042d855fa86d6a82092a0d538fd41ba9e65), re-downloaded and opened
  2026-10-21 23:40Z by date -u (successor 3, Fable 5.1): §4.1 (play values), §4.2 (order, MaxDiff), §4.3-4.5 (multisets, ⊕), §5.1 (3)-(10),
  §5.2 Prop. 5.1, Lemma 5.2, §5.3 Props. 5.3, 5.4, 5.6 (proof read), Lemma 5.5 (proof read in full), §5.4 Lemma 5.7, §5.5 Lemma 5.8 (proof
  read: 1=>2 uses Lemma 5.9 "proved similarly to Lemma 5.5" and Prop. 5.10, both without proof), §5.6, §6 Prop. 6.1 end, Thm 6.2, §7
  Prop. 7.4 (p. 27, no proof, no rule named), Claim 7.2.
- VJ00 = Vöge & Jurdziński, BRICS RS-00-48 (Dec 2000), https://www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf, sha256 485a12de432a2a8c..
  (opened 2026-10-18 between 22:59Z and 23:04Z by date -u): §3 postulates P1/P2/I1/I2; §4.1-4.5; §5.1 (3)-(11); Prop. 5.1, 5.3, 5.4, 5.6, 5.10; Lemmas 5.2,
  5.5, 5.7, 5.8, 5.9; §6 Prop. 6.1.


## Resume point (LANE-RESTART step 1; written 2026-10-18T01:25Z by session_01M28EFY9Ysyqj67kXt3YSje, Opus 5.5 under D12; context ~520k)
Lead: session_014FBi6o334DvwT5Uw2kDfoN. Branch claude/referee. Push ONLY with scripts/push.sh, output redirected to a file, print $?.
Rebuild Oink first (scripts/setup_oink.sh; tools/ is gitignored). Label every verdict "(Opus 5.5, D12)" while D12/L33 holds.
Independence: never read docs/referee-2/R2-Px.md before your own R-Px.md is pushed; then add §C. R2 files can land on
claude/referee-2 before trunk: read them there if the Lead says they exist.

### DONE (this session, packets 6-11; every report has a §C comparison with REFEREE-2)
- a13ad2f handover check (5/5). R-P6 9f77ff9 (+§C ad4be01). R-P7 299bc58 (+§C 1abe1d7, §C2 876c06e). R-P8 fe4be51 (+§C c0edb9c).
  R-P9 72313f3 (+§C 3785d3f). R-P10 a09a89d (+§C 434a552). R-P11 fc86762 (+§C abc5185). Landed as RESULTS R9-R13 (R14 pending CHECKER).
- Current joint state of GAP-A (A_DTL, given STR-DET): S−1 ≤ Σ_{R∈C_bv} #fired⁺(R) + n(|C_T|+|C_Dom|) + 1 (R2-P11 N11-b1, confirmed in
  R-P11 §C). So GAP-A ⇔ (CTX⁺) ∧ (FIRED⁺-R) up to polynomial factors (an equivalence, not a reduction). Alternative per-context
  route: (EXIT_c) (R-P10; F_R ≤ 3(c+1)(|R|+1)|R|²). All premises DATA only.

### IN FLIGHT
- None (parked 01:26Z 2026-10-18 on the Lead's instruction).

### NEEDS
- L-ALG (via Lead): open wording fixes from my reports: G9-b1 notation and N9-b1 cite (R-P9); V=∅ stop convention in §23q (R-P10
  G10-a1, with R2's fixed σ set); N11-a1 / G11-a1 citations in §23s (R-P11).
- Lead: successor from this notebook under LANE-RESTART.

### Session log (packets 6-11)
- Handover check a13ad2f (docs/agents/handover-checks/REFEREE.md), scored 5/5 by the Lead.
- R-P6.md (packet 6; pin 8ff4085; pushed 9f77ff9 13:17Z): §22f SIGN WITH GAPS (G6-a1 F_R must count every non-rise incl. Π-blind e*,
  closed; G6-a2 Dom term and +1, closed). §22j SIGN WITH GAPS (G6-b1 Dom step pushes only the top: base-triggered closure,
  monotone in T, closed; G6-b2 Dom input NOT fixed by (R, X): |C_Dom| counts inputs, OPEN inside (CTX⁺)). (c) SIGN.
  Tool docs/referee/scratch/p6probe.py (needs experiments/dtl-bench on the path for stdsort).
- R-P6 §C (ad4be01): full agreement with R2-P6 (G6-a1 = G-F1; R2's R-I = my Dom input).
- R-P7.md (packet 7; pin d461a76): EXACT SIGN WITH GAPS (G7-a1 line 137->138-139, G7-a2 remaining-instances step; closed),
  PREFIX-MONO-X SIGN (absorbed case closes with EXACT's closedness, which does not need τ processed in run 2), corollary
  SIGN WITH GAPS (G7-c1 Π-blind e* via POS-FALL+C4, closed; G7-c2 necessary not sufficient). fallv_viol_n28: both falls at
  new steals; same tangle stolen at both. (FALL) <= (NS-COUNT). Tool docs/referee/scratch/p7probe.py.
- R-P7 §C (1abe1d7): agree with R2-P7; ACCEPTED R2's G-P7-c2 (e*-pairs need not be consecutive visits; F_R <= 3 N_R) and
  corrected my R-P6 A4 (factor 2 in R9's per-context budget). Lesson: never assume a context is visited once per search.
- R-P8.md (packet 8; pin a907c46): EXACT* SIGN (corollary of EXACT), PREFIX-MONO-X* SIGN, corollary SIGN WITH GAPS (G8-1
  factor 3), §22u chain valid as conditional with factor 3. Tool docs/referee/scratch/p8probe.py.
- R-P7 §C2 (876c06e): R9 constants; Lead keeps the doubled display of record (16:08Z); my tighter STR-DET constants noted, single
  signature. R-P8 §C (c0edb9c): full agreement with R2-P8 (STEAL-ONCE*, G8-2 accepted). Standing by, nothing in flight (16:09Z).
- R-P9.md (packet 9; pin c5e2b4d): (a) SIGN; CHARGE SIGN WITH GAPS (G9-b1 notation P(τ)=P(τ⁺), G9-b2 short visits; G23g-1/2
  checked); depth/counting SIGN WITH GAPS (G9-c1 needs FIRED-R; constant D only); stealonce_viol_n76 confirmed. Tool p9charge.py.
- R-P9 §C: agreement with R2-P9; my N9-a1 WITHDRAWN (R2-P8 §7 was added after I read R2-P8). Lesson: re-fetch a
  referee-2 file before saying a section does not exist.
- R-P10.md (packet 10; pin 1100f3a): ENTRY-CHARGE SIGN WITH GAPS (G10-a1 one prefix convention incl. V=∅ stop; step 2
  fan-out < |R| checked hard: 143/146/165-172), C1/C2/C3 SIGN (C1 = reformulation; N10-b1). Tool p10entry.py.
- R-P10 §C (434a552): agree; fixed σ set accepted; R2 shorter route F_R ≤ 3(X_R+(|R|+1)|R|²) confirmed.
- R-P11.md (packet 11; pin 5909724): CHANGE-NEW SIGN WITH GAPS (N11-a1 STR-DET not needed; G11-a1 threshold via Lemma 1.2);
  corollary SIGN; honest limit: GAP-A ⇔ (CTX⁺) ∧ (FIRED⁺-R) (equivalence). Tool p11probe.py.
- R-P11 §C: agree with R2-P11; R2's N11-b1 confirmed (#e*-at-R ≤ D_R ≤ #fired⁺(R) given STR-DET; H drops out of R9).
  Box done; Lead plans a successor before any further packet.
- Lesson: Lemma 1.2 assumes Q = Z_0; Dom (878-890, 962-991) and bv regions push only the top. Check the push pattern.

## HANDOVER (parked 2026-10-17 ~12:20Z on the Lead's instruction; context ~520k; produced on Opus 5.5 under D12/L33)
Resume point. Successor REFEREE: read CLAUDE.md, docs/NOW.md (Lead session_014FBi6o334DvwT5Uw2kDfoN), then my reports below.
- Push only with scripts/push.sh; redirect its output to a file and print $?. Read the notification queue before every push.
- Rebuild Oink first with scripts/setup_oink.sh (tools/ is gitignored).
- Label every verdict "(Opus 5.5, D12)".
- Do not read docs/referee-2/ for a packet until your own report for it is pushed.
Packets done today (all on claude/referee; every report has a §C comparison with REFEREE-2 where the Lead asked):
- R-STEP5.md (Step 5 of GAP-C; pin 8f41be8): KT, NT-f, FM/WM, (YZ) reading, (YZ)<=(ACYC), P-KT. All signed, gaps closed.
- R-PROVED2.md (packet 2; pin 43d63b0): SCC1, B-thr ("(a) always", F-b3), Theorem A, O0/O1, OPP-EXIT, K0, phases<=D+2,
  FDL, DV*-MONO, LRN budget, (SPP)=>bound. §C/§C5 hold the comparisons. The G-h1 "closed" there is now conditional on
  (STR-DET) (R-P4 §C1).
- R-P3.md (packet 3; pin 6e0082f): K5' and (α) with Up(Str) REJECTED after the comparison (REFEREE-2's configuration;
  my G-a1/G-a2 step was wrong: old tangle vertices keep their region strategy, 169). K5''/(α) with Dep(Str) SIGNED; gap
  G-α1 in R2's ⇔ form. O-P SIGN (given YZ). GAP-A first step SIGN (round r).
- R-P4.md (packet 4; pin 44d1428): S0, PREFIX-MONO, POS-FALL, ROOT-BOUND SIGN. §22e SIGN WITH GAPS with G-e1 (e* in Dom
  via an X-straddle) and G-STR OPEN. §C: G-STR holds; it cannot arise for e* in the root best_vertices call.
Open gaps I hold (for GAPS.md):
- (ACYC) (Step 5).
- G-e1/G-DOM (§22e: first difference in Dom).
- G-STR, i.e. (STR-DET) (FDL alignment and counting after the first sptl).
- (CTX), (DIRTY), (SPP).
- The (α) shape (SKETCH).
- GAP-A beyond round r.
Lessons:
- Twice my set-level arguments missed strategy-level (str) effects: R-P3 (a) and G-STR. When a proof step reasons about
  what a ψ-play or an extraction does, check which line wrote str (89 / 171 / 73) for every vertex involved.
- REFEREE-2 caught both. Its configurations were correct.
Tools (docs/referee/scratch/): step5_probe.py, bthr_probe.py, fdl_random.py (all subclass experiments/alg dtl_pyref/dtl_step5).
- R-P5.md (packet 5; pin f920dc2, 12:36Z): Lemma STR-DET SIGNED (gaps W-a1 wording, G-a2 Case A argued by Dom closure).
  G-STR CLOSED; FDL R5 (h) holds on the reduced log; R-P4 §C's STR-DET condition withdrawn. Open in §22e: (CTX),
  (DIRTY)/(FALL), G-e1/G-DOM.
Nothing in flight (parked again 12:38Z).

## Resume point (successor session, 2026-10-14 ~23:50Z)
I am the successor REFEREE (spawned 23:15Z, replacing the session parked at f179ae0). Lead: session_014FBi6o334DvwT5Uw2kDfoN
(send_message, first line "From REFEREE (<UTC from `date -u`>):"). Branch claude/referee, trunk merged in
(origin/claude/vibrant-johnson-nxvvxo). Push only via `scripts/verify.sh && git push -u origin claude/referee`; Oink built with
scripts/setup_oink.sh (~1 min; rebuild after every restart, tools/ is gitignored).
Tasks done: R-L1 (L-LOWER L1 at 8fcc0f2; CHANGES, 9 findings; report 2026-10-14-L1-statement-check.md, pushed 9b01cbb,
reported 23:43Z) and T-A1 first-referee check (L-ATTR TA1-proof.md at d5d6396, then re-checked at 4478b84 per the Lead's 23:42Z retarget;
then SIGNED OK at 57a1515 (signature block at the end of the report, gaps G1-G11); report 2026-10-14-TA1-proof-check.md; tools
ta1check.py, ta1probe.py). R2's report (docs/referee-2/R2-TA1.md) read only after my derivation; it agrees on every point. T-A1 signed OK at l-attr 57a1515 (G11 answer for the CHECKER appended). R-L1b (L-LOWER v2 + Lemma 2.1' + Theorem B at
l-lower b1abae0): CHANGES with one one-line finding; report 2026-10-15-L1b-check.md; tool l1bcheck.py (types over all
one-player Büchi games n <= 4, exhaustive B_1 lower bounds n <= 3, lane witnesses on my quotient). R-psolC (L-ATTR psolC fidelity, l-attr 02174e2): FAITHFUL, DE3 recordable; report docs/referee/R-psolC.md; tool
psolccheck.py (my own psolC from DTR15-4 Defs 1-2/Thm 1/Fig. 5, full product, both A1 readings). R-TL2 (second referee read of L-RED's transfer lemma, l-red 0d50d4a): OK with fixes; report docs/referee/R-TL2.md; tool
tl2check.py (my own G from FHZ Table 1, my own P, Friedmann valuation, exhaustive over all trees, RF vs RAR lockstep).
Nothing in flight.
Coming (per the Lead's brief): the L1 proof work / experiments/lower from L-LOWER; SL8-min / T3 from L-STRUCT; second referee
for the L4+T3 package is a SEPARATE session, not me.

## Resume point of the predecessor (kept for the record; HANDOVER, parked 2026-10-14 ~21:50Z on the Lead's instruction; context ~680k)
You are the successor REFEREE. Read CLAUDE.md, TARGET.md (v1.0 frozen), docs/NOW.md (Lead session id; it was
session_014FBi6o334DvwT5Uw2kDfoN), docs/agents/LANE-RESTART.md (the five handover-check questions), docs/referee/README.md,
then every report in docs/referee/ (eight so far). Branch claude/referee; push only via `scripts/verify.sh && git push -u
origin claude/referee`; messages to the Lead with the claude-code-remote send_message tool, first line "From REFEREE
(<UTC time from `date -u`>):" (my own first lines drifted ahead of UTC; use the clock). Build Oink first
(`scripts/setup_oink.sh`, ~1 min) so the gate's smoke step runs; `pip install python-sat` for wsepsat.py.
Last actions: L4 (docs/struct/L4-proof.md) signed OK as FIRST referee at claude/l-struct 50dc28b (referee 9bf5301);
handover written (this commit). No work in flight; nothing routed.

State of every claim I refereed (report file in docs/referee/, verdict, status):
| claim | report | verdict | status |
| --- | --- | --- | --- |
| arXiv 2511.03752 v1 (M2) | 2026-10-14-arxiv-2511.03752.md | BROKEN (Theorem 2 false; cex1, cex2) | M2 closed on trunk; AM1-AM9 faithfulness OK |
| L-COMP PGSolver ports (generators, pgsolver_si.py) | 2026-10-14-pgsolver-ports.md | OK; bare SI loop = PGSolver -dgo -dsd -dlo -dsg | done |
| L-LIT T4 §3(c) lasso observation | 2026-10-14-T4-3c-lasso.md | OK, 3 strengthenings, 1 citation nit | done |
| L-COMP gauntlet bench (experiments/) | 2026-10-14-harness-review.md | CHANGES then OK at l-comp e70a2a9 | landed |
| L-STRUCT S1 C1 (w(2,6)=3<4=s(2,6)) | 2026-10-14-S1-C1-weak-separators.md | OK; side claim BROKEN (= plant P1); Lemma 2(b) CHANGES | findings to L-STRUCT |
| L-STRUCT S2 (T1/T2) + L-COMP T1 refutation | 2026-10-14-S2-statement-check.md | T1 REFUTED at (2,10), verified; T2 CHANGES | findings 1-4 to L-STRUCT |
| L-STRUCT S3 (diagonal, T3, L4, H1) | 2026-10-14-S3-statement-check.md | CHANGES, all applied (a67bd78); delta OK | done; T3 proof not yet seen |
| L-STRUCT L4 proof | 2026-10-14-L4-proof-check.md | CHANGES then OK, first referee, at 50dc28b | awaits SECOND referee |
| L-LOWER L1 statement (SLP model, Lemmas 1.5/1.6/2.1/2.3, Transfers 2.2/2.4, T-L1) | 2026-10-14-L1-statement-check.md | CHANGES (9 findings: d vocabulary, game-class corner, Lemma 2.3 rests on unproved Remark 2.5, cited experiments/lower absent at 8fcc0f2, ω(n) gloss weaker than ω(n), 3 model differences, nits) | findings to L-LOWER via Lead; every re-derived claim holds |
| L-ATTR T-A1 (psolB complete <=> PA**; PA** => psolQ complete; Cor. 1-2, Prop. 3) | 2026-10-14-TA1-proof-check.md | CHANGES (theorem and both proofs hold; at 4478b84 open: F1 misstated, T-A1' needs HKP Thm 4, Büchi recolouring, 'stable' gloss); first referee | SIGNED OK as first referee at l-attr 57a1515 (all findings applied; G1-G11 listed, G10 open as HKP dependency) |
| L-LOWER L1 v2 + Lemma 2.1' + Theorem B (b1abae0) | 2026-10-15-L1b-check.md | CHANGES (findings 1-9 applied; Lemma 2.1' OK; Theorem B OK, Claim 3 misses the case t<t'<a; B_1(1..4) = 0,2,4,6 confirmed independently) | findings to L-LOWER |
| L-ATTR psolC fidelity (DTR15-4; 02174e2) | R-psolC.md | FAITHFUL (A1: literal reading is the chapter's; Example 3 (ii) is a slip; instance and tc N=2 undecided under both readings; 3 nits) | DE3 can be recorded |
| L-RED transfer lemma (FHZ G_{n,r,s,t} RF = RAR on sink parity P; 0d50d4a) | R-TL2.md | OK with fixes (lemma true; case (2) misses the chain-vertex sub-case; loose constant in (1)/(3); S1 tie/start conditions to cite); second referee | RESULTS candidate if R2 agrees; L-LIT novelty + CHECKER |

## Queue / open items
- L4 second referee (not me; a second, independent referee): the gap list G1-G6 in the L4 report is the checklist. What
  the second referee must re-derive: Lemma L4.1 (a)-(d) (Parys-Wiacek conversion H', words p.w, cycle multisets,
  q1 = delta(q0,1) != bottom via 1.2^w, A' = (Q,q1,delta)), L4.2, the chain in Theorem L4, the constants of L4.3
  (d' = 2 floor(sqrt n /2), a0, b0; the fixed step uses floor >= ceil - 1), L4.4's class (i)-(iii) from S2 §3(c), and the
  black-box use of CDFJLP Thm 5.1 (E convention, non-rejecting states, deterministic ⊆ non-deterministic, binomial form
  needs no side condition). My S3 "delta" section records the alternative split-G_t route, not written up.
- Coming (per the Lead): SL8-t and T3 (S3 §2: w^V(n,d) = s^V(n,d) for 1 <= d <= n+1). For T3: cells I confirmed with my
  own SAT: (1,1), (2,2), (2,3), (3,3), (3,4), (4,4) all w = s; obstruction to "prune the even-used part": the committed
  weak_V_n3_d3.json has an odd cycle among its even-used transitions (my check, S3 delta); route R2's L5' must be about
  all paths P and all foldings (S3 §4b). A (4,5) V or (5,5) V cell with w < s would refute T3; my enumeration is too
  slow for n = 5 (use L-COMP's LRAT-checked cells, then verify any SAT witness with wsepref.py over all graphs).
- Minor, not routed: diff of the PGSolver ports against the real binary with -dgo -dsd -dlo -dsg (owner Q4);
  s^V(4,6) = 10 (L-STRUCT) and w^E(4,6) >= 8 (L-COMP, LRAT) are not re-verified by me.
- Findings I routed whose application I have not seen: S2 findings 1-4, S1 findings 1-3 (Lead said L-STRUCT has them),
  T4 finding 4 (CDFJLP multiplicity wording, to L-LIT), ports cosmetic nits (to L-COMP).

## My tools (docs/referee/scratch/; all throwaway, run with `python3 -I`; every SAT answer is re-checked by brute force)
- aiayn.py: faithful implementation of 2511.03752 Algorithm 1 under all 16 readings of its ambiguities, a min-parity
  Zielonka, .pg read/write with min<->max conversion, random counterexample search. `--pg FILE --trace`, `--all-readings`,
  `--search N`. cex1-/cex2-minparity.pg are the counterexamples (paper's convention); *-maxparity.pg are the twins for
  Oink/PGSolver; *.sol are Oink's verified answers (Even wins all four vertices on both).
- harness_faults.py: four planted-fault solvers (winner swap, strategy leaving region, in-region losing cycle, min-parity
  convention) run through L-COMP's compare.py; needs a checkout of experiments/harness.
- sitest_run.py: execution check of pgsolver_si.py / pgsolver_port.py against Oink (paths point at my scratchpad; adjust).
- wsepref.py: brute-force checker for weak/strong (n,d)-separators (S1 D1-D5) over ALL graphs: conventions V (any small n),
  S (n <= 2 cheap, n = 3 is 7^9), E (n = 2, d = 6 via graphs_E2); prune, cycle_class, accepts_all (W1), rejects_all (W2),
  strong_S2 (S2); CFGO universal-tree recursions f_upper/g_lower. CLI: `witness n conv [strong]`, `json FILE n conv`,
  `utrees`, `k2` (all 531,441 two-state automata, V, n <= 2, d = 6).
- wsepE2.py (d = 6: all 16,777,216 edge-labelled multigraphs on 2 vertices, several automata at once) and wsepE2d.py
  (any d: all (A,B) cross-label-set pairs with saturated same-parity loops; sound by monotonicity of W1/W2).
- wsepsat.py: my own SAT encoding (pysat CaDiCaL 1.5.3; one-hot transitions, closure variables per graph, thermometer
  ranks for W2 and for S2 on all states, no symmetry breaking) over inclusion-maximal even/odd graphs computed by brute
  force (V: one labelling per vertex-permutation orbit; S). `wsepsat.py n d V|S weak|strong k`. Timings: n <= 3 seconds;
  n = 4, d = 4: ~11 min per cell (enumeration dominates), weak k = 6 took 24 min; n = 4, d = 6 strong k = 6 timed out at
  25 min. Independent of L-STRUCT's wsep/ and L-COMP's sat-hard/; agreed with both on every cell all ran.
- slpcheck.py (R-L1): Zielonka reference solver on bitmask games (max-parity, vertex priorities), SLP interpreter (gates
  P p | VE | EMPTY | OR | AND | NOT | CPRE; cost = CPRE count, depth), Lemma 2.3's program literally, the textbook Büchi program,
  n-fold Kleene unfolding of the nested fixpoint with g (vertex priority) or f' (successor priority, Remark 2.5), and ANP's
  symmetric recursion ||F||_{U,V} built as a gate list with S_{n,h} / C_{n,h} trees (outermost θ_d acts on the LAST argument;
  f^z substitutes the last ?). Exhaustive games for n <= 3, one-player n = 4; random beyond. `python3 -I slpcheck.py [quick]`;
  full run ~15 min. A non-universal tree makes ANP fail (sanity). All lane programs: 0 mismatches.
- ta1check.py (T-A1): my own psolB/psolQ from HKP Figs. 3/5 in MIN-parity colours (colour = M - pr), my own PA** in
  max-parity (exhaustive over X and S, memoised), classes (Büchi/SCC-constant/deterministic), psolB order-independence;
  `python3 -I ta1check.py [quick]` (2 min full). ta1probe.py: F2, F6 (all X ⊆ W_p, all d), Lemma 0 on small games.
- l1bcheck.py (R-L1b): all one-player Büchi games with <= n vertices as one union (3.2M pointed games at n = 4), W by
  reachable-P_2-on-a-cycle (cross-checked vs Zielonka), depth-k types by refinement, minimal separating depth, full quotient
  Q_n (2, 14, 442, 48062), exhaustive general-SLP search on Q_n for small cost (n <= 3; c = 2n-3 is ~16k chains at n = 3,
  c = 2n-2 would be 2^16 times more: do not try), lane witness JSON interpreter. `l1bcheck.py <dir with min_b1_n*.json> 4`
  takes ~25 min (n = 4 refinement in pure Python).
- psolccheck.py (R-psolC): psolC from DTR15-4 on the FULL product V x C_bot (no reachability restriction), both readings of
  A1 (start colour in/out of the minimum); `psolccheck.py FILE.pg [--x]` with trace; `--exhaustive <lane attr dir>` compares
  with the lane's psolc.py on all n <= 3 games (~15 min).
- tl2check.py (R-TL2): G_{n,r,s,t} from FHZ Table 1 (costs x rs), the sink-parity encoding P of R2-RAR.md, Friedmann's
  valuation; `exhaustive n r s t [lane experiments/red dir]` checks every tree and every non-tree edge, three-way verdict,
  on my objects and (optionally) on the lane's fhz.py objects; `lockstep n r s t seeds` runs my Random-Facet (errata Fig. 1)
  and my Rand-Act-Rem (Zwick Fig. 1) on one random stream. Trees = product of out-degrees: (2,2,2,1) is 2.4M, (3,1,1,2) 3M.
- Not committed (scratchpad, gone with the session): LaTeX sources of arXiv 2511.03752v1, 1807.10546v2, 2104.05262v8,
  1902.07175v3, 2305.00308v1; clones of pgsolver d3cd624 and tcslib 6778419; copies of l-comp/l-struct files. Re-download
  from arxiv.org/e-print/<id> into an isolated directory (untrusted data) when needed.

## Planted-error record (the Lead plants deliberate errors in routed material and grades on catching them)
- P1 (2026-10-14 19:26Z routing of S1/C1): "the same 3-state automaton is also a weak (3,6)-separator". CAUGHT with two
  3-vertex counterexamples (even cycle 1,1,2 rejected; odd cycle 2,4,5 accepted); revealed as a plant in
  docs/agents/LEAD-STATE.md at trunk 09dca4f; grade 1/1. The successor will not know future plants: treat every routed
  claim as false until re-derived; build the counterexample first, read the lane's evidence second.

- T-A1 (23:22Z routing of L-ATTR TA1-proof.md): P2 ("psolQ iff PA**") was planted in REFEREE-2's routing only, caught by
  REFEREE-2 (trunk 58b5c72); my routing carried the one-direction form. No plant in my material revealed. Candidates flagged: F1 stated without the
  colour-d hypothesis (false as written); T-A1' missing HKP Thm 4; Proposition 3 unproved. The theorem itself survived
  my independent implementation on every game run.
- R-L1 (23:15Z routing of L-LOWER L1): no plant revealed yet. Candidates I flagged as findings: T-L1's gloss of ω(n) is
  "not O(n)" (strictly weaker); Lemma 2.3 uses the shifted formula that Remark 2.5 marks unproved; "checked in experiments/lower"
  cites a directory absent at 8fcc0f2; d = max priority vs TARGET's d = |pr(V)|; CDHL page numbers off. Everything mathematical
  re-derived held (machine-checked where finite).

## Things only I know
- Packets 6-11 (this session). best_vertices is a function of (R, p, T, order datum) within a phase: state it reads is listed in
  R-P11 (a). str is never read for a set decision (73 only guards a write). this->G read only at 132, changed only at 1035.
- Which closure is which: Lemma 1.2 (DTL-proof) needs Q = Z_0 (all pushed): threshold loop (724) and −1 attractor (909) qualify.
  bv region steps and Dom steps push only the top: region = Cl over T \ E_τ (EXACT); Dom = closure triggered by the new part,
  NOT monotone in its base (R-P6 G6-b1).
- Cross-visit counting: e*-pairs are NOT consecutive visits (a context can recur within a search). Use the endpoint device
  (R-P7 §C2): along e*-endpoints T is non-decreasing, and overlaps lie where T is constant (STR-DET (c)).
- Visit alignment: missing rounds = repeat last round after "no candidates" (716/765), empty after V=∅ (768-771); steps range
  over ALL p-vertices τ of R (R2-P10's fixed σ set).
- Probes p6..p11 in docs/referee/scratch/ subclass experiments/alg/dtl_pyref.DTL and need experiments/dtl-bench on sys.path
  (stdsort). My pyref internal ids differ from dtl_rootmono's (e.g. tops 31/74 vs 18/66 on stealonce_viol_n76).
- Corpus I used: experiments/alg/instances (138 files); full runs take ~5-10 min per order per probe; run both orders in the
  background with until-loops on the output file (pgrep -f matches its own shell).
- R-TL2: FHZ's "zero-edges" are the COSTLY edges (superscript 0 = counter bit 0); B_0 = any tree of them. The transfer lemma
  needs only B and e, not F. The one real structural fact: before merging, the two prefixes sit at u_i and w_i (the only
  entry points) at every level; equal classes from one vertex land on one vertex (merge), so a tie at the divergence level
  ends the comparison, and the (C_u, C_w) small-offset difference can occur only at the merge level. P has priority-0
  vertices below the sink, so Friedmann's 1-sink identity "length = |path set|" does NOT hold in P; lengths are compared
  separately and ties need the relay-per-copy design.
- R-psolC: DTR15-4 (sha256 a7b61fe3...9cd6) is min-parity; Example 3 step (ii) drops the start colour from the prefix minimum,
  contradicting Def. 1, Def. 2, Thm 1's proof and Lemma 2's proof (all include it). Both readings are sound; literal decides
  more. psolc_min_n4_m6.pg: Odd wins all, psolC's player-1 fixpoint goes {v0,v2,v3} -> {v2,v3} -> {v2} -> {} under both
  readings; the parity of the decisive minimum (2 at v0 via v1) is the same with or without the start colour.
- R-L1b: minimal program depth on one-player Büchi is exactly 2n-2 for n <= 4 (my types), Theorem B gives 2n-1; B_1(4) = 6
  follows from Lemma 2.1' + the lane's witness without any SAT. The exhaustive chain search is fully general for SLPs.
- T-A1: F6's equality MAttr^{G'}(X,d) = MAttr^{W_p(G')}(X,d) holds for EVERY X ⊆ W_p (q keeps the play in W_q), not only
  fatal X; the "only if" needs only W ⊆ R from F1. L1's rank induction has no rank 0 (X external). T-A1' silently needs
  HKP Thm 4. The "if" proof is order-free, so T-A1 holds for psolB under any colour order. HKP Fig. 4(a) edges (from the
  png): v0↔v1, v1↔v2, v2↔v3, v3↔v4, colours 3,2,0,2,3, squares v1, v3. PA ⊆ PA* has no proof anywhere (data only).
- R-L1: ANP's recursion ||F||_{U,V} is straight-line; Lemma 3.6 (worklist) is adaptive; a Jacobi round-robin on Algorithm 1's
  |V| equations is non-adaptive at |V|(1 + n|V|) queries. CDHL's O(1)-bit step for Reduction 3.9 is NOT in their text (they
  say "same argument as Theorem 3.2"); it is one bit per party about the loop at v_max (Pre) / v_min (Post). CDHL printed
  page = physical page − 1. ANP cite Emerson–Jutla 1991 ([10]) for "Expression (1) = winning region". The shifted Büchi
  formula νZ.μY.Cpre((P_2∩Z) ∪ (P_1∩Y)) is correct (rank argument in the report §3) and exhaustively checked for n <= 3.
  The matrix-vector query model (Sun–Woodruff–Yang–Zhang ICALP 2019, arXiv 1906.05736) is the adjacent framework nobody in
  the fleet has opened; with named singleton queries n queries read the adjacency matrix, so ω(n) must come from anonymity.
- 2511.03752 is MIN-parity; PGSolver/Oink are MAX-parity; convert p -> M - p (M even >= max p). On cex1 the max-parity
  reading of the same numbers coincides with the algorithm's wrong output: never check a min-parity run against Oink on
  the unconverted file. The paper's theorem numbers follow a shared counter (Lemma 1 Zielonka, Theorem 2 dominion,
  Lemma 3 minimal dominion, Lemma 4 progress, Theorem 5 correctness); the false sentence is tex:332.
- L-COMP's strategy-improvement port is the bare loop = PGSolver with -dgo -dsd -dlo -dsg (pgsolver.ml:102-116), not the
  default binary with universal_solve preprocessing; any M1 sentence quoting PGSolver counts must say so.
- CDFJLP (1807.10546v2): Thm 5.1 is an E-convention theorem (G_t has one self-loop per even priority at each vertex),
  counts non-rejecting states (tree decomposition on non-rejecting states; leaves inject there), and its binomial form
  comes from Thm 2.3 "for all positive integers" with no side condition; the "d <= n" is only for the closed form. The
  embedding claim (§5) uses only a run on alpha_t avoiding rejecting states plus the tree decomposition from strongness.
  CDFJLP never fixes whether parallel edges may carry distinct priorities (T4 finding 4). CFGO (2104.05262v8): Thm 4.1 =
  saturation.tex thm:main; parity §6 lemma numbering: 6.1 (line 13), Thm 6.2, 6.3 (68), 6.4 (145), 6.5 (165), 6.6 (197),
  6.7 (225), 6.8 (266), Thm 6.9 (287), Prop 6.10 (304), Prop 6.11 (374); universal-tree sizes f = g: (2,3) 4, (2,4) 5,
  (3,3) 7, (4,2) 8, (4,3) 13. KV (1902.07175v3): alphabet (vertex, priority), eventually-always q_accept, graphs = S
  convention, Thm 2 time-bounded.
- S1 Lemma 2(b) repair differs by convention: E = self-loop labelled 2 at the end of the non-zero part; V = fresh vertex
  labelled 2 (a 0-vertex was removed), n >= 2.
- T1 (one tree level) died at (2,10): w = 4 < 5 = s(2,8) in E, S, V (my exhaustive checks); it held at (2,6), (2,8) and
  L-COMP's w^E(4,6) >= 8 supports it there. The weak < strong cells all have d >= n+3.
- The probe automaton that exhibits the restriction dead end for (3,6) V (6 states, odd cycle of maximum 3) is listed in
  the S2 report §5; the committed weak_V_n3_d6.json is NOT such an instance (its restriction to Sigma_4 is strong).
- My timestamps in messages to the Lead ran ahead of UTC (I estimated instead of reading the clock); the SHAs are the
  record. L-STRUCT had the same issue (S3 §5).
- The split-G_t observation (S3 delta, finding 8): one copy per out-letter gives c = d and monotonicity in d then gives
  L4; L-STRUCT used L-LIT's Claim R instead (same bound form). If a self-contained proof is ever wanted, that is the route;
  I did not write it (referees do not write proofs for lanes).

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| arXiv:1410.7530 (FHZ, Random-Facet shortest paths; LaTeX source + PDF) | Table 1 + zero/one-edge convention (Actual-Construction.tex 28-66, 101-104), B_0 (144-152), Def. functional (156), Def. B_F (234), RF pseudocode and shortest-path reading (RandomFacet.tex 47-50, 70-86, 181-195), Thm 6.3 = thm:main (Lower-RandomFacet.tex 118-142), parameters (706, 760-763), introduction.tex 24-26, abstract | 2026-10-15 | R-TL2 |
| arXiv:1410.7871 (FHZ errata) | §1 (RF vs RF*, "main result of [1] flawed", RF* bound stands), §2 Fig. 1 pseudocode, p.4 "similar examples for parity games" | 2026-10-15 | R-TL2 |
| arXiv:2607.06334 (Zwick, Rand-Act-Rem) | §2 AUSO and orientation, §3 VAL and improving switch, Appendix D Fig. 1, related work p.~1040 | 2026-10-15 | R-TL2; PDF |
| arXiv:1106.0778 (Friedmann, LMCS 2011) | §3 node valuations (set order by max of symmetric difference; length order by cycle-node parity), §5 1-sink games and Lemma 5.1 | 2026-10-15 | R-TL2; PDF |
| Imperial DTR 2015/4 (HKP, psolC; sha256 a7b61fe3...9cd6) | §2 p.3, Def. 1 p.4, Def. 2 + Thm 1 pp.5-6, Cor. 1, Lemma 2 + proof, (2), Lemma 3, Fig. 4 remark, Fig. 5 p.9, Thm 2 pp.8-9, Example 3 + Fig. 6 pp.10-11 (rendered), Thm 4 p.12 | 2026-10-15 | R-psolC; MIN-parity; PDF via pdftotext + pdftoppm |
| arXiv:1405.0386v2 (HKP, Fatal Attractors) | archiv.tex/PDF: §2, Defs 1–8, Thm 1, Thm 2 + proof, Lemma 1, Fig. 3 (tex:728–747), Ex. 5 + Fig. 4(a) png, Def. 6 (tex:942–948), Fig. 5 (tex:970–997), Thm 4 + proof, Thm 5, Thm 6 statement, Thm 7/8 + proofs, Lemma 5 + proof, external-target remark tex:528–536 | 2026-10-14 | T-A1; MIN-parity |
| arXiv:1711.09148v1 (CDHL, SODA 2018) | arxiv.tex: §2 model 466–517 (Thm 2.1 th:lbdisj), Reduction 3.9 red:buchi 759–765, Thm 3.10 thm:buchi 803–814 and proof 1223–1241, Lemma 3.4 lem:scc2 615–665, Prop 4.2 lem:objectives_ub 1023–1044, intro 284–286 ("2n one-step operations"); theorem numbering from the shared counter, confirmed in the PDF | 2026-10-14 | R-L1; LaTeX source + PDF, isolated dir |
| LIPIcs.CSL.2021.9 (ANP, DOI 10.4230/LIPIcs.CSL.2021.9) | §2 (f_{A,B}, trees, Prop 2.5), §3.1 cases (1)–(3), Lemmas 3.1, 3.2, Remark 3.3; §3.2 Algorithm 1, Lemmas 3.4–3.6, Cor 3.7; §3.3; Thm 5.1; Remark 5.5; intro p.9:2–9:3 ([10] Emerson–Jutla for Expression (1) = winning region) | 2026-10-14 | R-L1; DROPS PDF via pdftotext |
| arXiv:2305.00308v1 (Parys–Wiącek) | improved-parity.tex lines 86-87 (edge-to-vertex priority conversion remark), 368 (necessity proof does not apply) | 2026-10-15 | LaTeX source; L4 attribution quotes |
| arXiv:2104.05262v8 (CFGO, LMCS 2022) | preliminaries (graphs, automata, neutral letter), reductions (separating automata, universal graphs), saturation Thm 4.1, parity §6: Lemma 6.1, Thm 6.2, Lemmas 6.4-6.8, Thm 6.9, Props 6.10/6.11 | 2026-10-14 | LaTeX source; S1 conventions and F2 |
| arXiv:1902.07175v3 (Kozachinskiy-Vyalyi) | §1.2 separation approach, §2.1 separation automata and game graphs, Thm 2 | 2026-10-14 | LaTeX source; S1 F5 / Lemma 3 |
| arXiv:1807.10546v2 (Czerwiński et al., universal trees inside separating automata) | the-separation-approach.tex (languages of play encodings; safety automata; (n,d)-separators, strong separators); intro.tex 161-166 (separator) | 2026-10-14 | definitions for the T4 §3(c) check; LaTeX source |
| github.com/tcsprojects/tcslib 6778419 | src/data/tcsgraph.ml 8-226, tcsset.ml 132-166/284-287/426, tcslist.ml 35-42, tcsarray.ml 48-52, tcsbasedata.ml 181-227 | 2026-10-14 | helpers used by stratimpralgs.ml |
| github.com/tcsprojects/pgsolver d3cd624 | solvers/stratimpralgs.ml 54-199, 441-669, 693-696; solvers/switch_globally_best.ml 1-119; paritygame/transformations.ml 271-320, 338-413; paritygame/univsolve.ml 23-66, 267-780; apps/pgsolver/pgsolver.ml 102-116 | 2026-10-14 | strategy improvement originals of pgsolver_si.py |
| github.com/tcsprojects/pgsolver d3cd624 | recursiveladder.ml 13-46; policyiter/generators/switchallexp.ml 30-66, switchbestexp.ml 34-74; policyiter/stratimprgenerators.ml 7-47; paritygame.ml 19, 25-40, 128-139, 175, 201-206, 365-387 | 2026-10-14 | OCaml originals of L-COMP's ports; cloned into scratchpad |
| arXiv:2511.03752v1 | whole paper: Sec. 2 defs, Sec. 3 (A*, A', A^k, Thm 1, Lemma 2, Alg. 1, Lemma 3, Thm 4, 5, 6) | 2026-10-14 | PDF + LaTeX source (main.tex); 4 pages; only v1 exists |

## Dead ends
(none)
