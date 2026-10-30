# R2-N5-FIXD-C: §C cross-map with REFEREE's report, and the check of REFEREE's Theorem SW-KEEP (REFEREE-2 successor 23, Opus 5.5, D15)
Inputs: my report docs/referee-2/R2-N5-FIXD.md (claude/referee-2 4a960ef9, pushed 16:2xZ, before I opened any docs/referee/ file for this
packet); REFEREE's report docs/referee/R-N5-FIXD.md at claude/referee 2c9d8040 (opened 16:34Z on the Lead's word) and its logs
docs/referee/scratch/fixd_logs/{sbcg,alt}.txt, run.sh, fixd_probe.py, core_probe.py (parse_start). Object unchanged: P-N5-FIXD-box91.md
@ l-new 5027c17c, sha1 2050e167; line ba09dd26; L-NEW 39's revision docs/new/P-N5-FIXD-box91-line-L1.txt @ l-new fe5c9e33 (sha1
7e99a4a9…, re-hashed here).
Owner rulings: D1 «Never downgrade the referee to save money.»; D18 «Clearly distinguish proven results from conjectures and open problems.»

## C.1 Verdicts side by side
| item | REFEREE | REFEREE-2 | joint |
| --- | --- | --- | --- |
| §1 premises, MON | CHECKED; Ξ_σ = Ωσ needs the R57 standing premise (FIXD-N2) | CHECKED (§2.1); I did not flag the premise | agree; FIXD-N2 is right (C.3) |
| §2 FIX-DEPTH, FIXD-MON | SIGNED | SIGNED | SIGNED by both, no gap |
| §3 PHASE-RED | SIGNED | SIGNED | SIGNED by both, no gap |
| §4 PHASE-RED′ (implication) | SIGNED | SIGNED | SIGNED by both, no gap |
| FLAT-SW | PROVED by REFEREE (SW-KEEP, §4b) | PROVED by REFEREE-2 (Lemma OWN, report §5) | two independent proofs; I SIGN SW-KEEP (C.4); REFEREE's check of OWN pending |
| §5 DATA | pins MATCH; totals «a few percent below», not reconciled | per game 1131 / 1132 = lane; N-1, N-2 | fully reconciled (C.2); my N-1 CORRECTED (C.2) |
| line ba09dd26 | FIXD-N1 free k; N2 premise; N3 data label; N4 citation | L-1 free k; L-2 clause-scope P; L-3 optional | C.3 |

Joint gap map for §2-§4: EMPTY. Nothing FALSE on either side.

## C.2 DATA: REFEREE's FLATTR 6460, my 6475, the lane's 6503 — reconciled to the run
Per game, N5, (K-rise, FLATTR), REFEREE's logs against my PERRUN output (missing count lines in REFEREE's logs read as 0):
- sbcg (719 games): 705 identical. The 14 others are exactly the games with n > 200 (dlc_d4, topfix_n10, switchbestexp_8, fc_8,
  s3quad_K8_m30, leanT_N32, tcL_N10, tcL_N12, tcR4_N8, tcS8_N9, gate_K64_n581, grow_K40_n373, pp_K48_n449, pp_K48_n449_dual): REFEREE's
  fixd_probe.py l. 115 skips them («if g.n > int(os.environ.get("MAXN", "200")): cnt["skip_big"] += 1; continue»), and run.sh's grep does
  not keep the skip counter, so they show «RC 0» and no counts. FLATTR 2801 − 2769 = 32 = switchbestexp_8 15 + fc_8 13 + leanT_N32 4.
- alt_all (413): 401 identical. The others: the same big games (tcpert, usplit; FLATTR 4 from leanT_N32); n3cov_lean and n3cov_phi, whose
  start files list only some vertices (REFEREE's parse_start rejects a partial start file and falls back to the best-reward start; the lane
  and I fill unlisted vertices with the best-reward choice; FLATTR 7 from n3cov_phi); and comp54_n80 (below).
- Reconciliation: lane 6503 − REFEREE 6460 = 43 = 32 (sbcg, n > 200) + 4 (alt, leanT_N32) + 7 (n3cov_phi); K-rise 9615 − 8750 = 865 = 644
  (sbcg) + 221 (alt). Every difference is a run-set choice. None is an engine disagreement. My answer to the Lead's question: my N-1 explains
  NONE of REFEREE's gap. On comp54_n80, REFEREE has 22 / 32, the same as the lane.
- **Correction of my N-1** (R2-N5-FIXD.md §4). comp54_n80.start does give the non-edge 11 → 51 at the FORCED vertex 11 (its only edge is
  11 → 11). REFEREE's parse_start replaces a forced vertex's move by its only edge (with a NOTE), and so runs a valid N5 run. Re-run here
  with the start file minus «11:51» (vertex 11 forced to 11): 55 iterations, K-rise 22, FLATTR 32, exactly the lane's numbers. The lane's
  n5x.start_pair copies 11 → 51 literally, but its counts equal those of the repaired run. So the lane's totals 9615 / 6503 ARE the
  totals of valid runs (the repaired start). My 9596 / 6475 came from my tool skipping the whole start file and using the default start.
  N-1 is withdrawn as a data correction. What remains is a note: the start file should be repaired at vertex 11, and the lane's reader
  should validate starts.
- N-2 (my) = FIXD-N3 (REFEREE): the same mislabel, the same reading (16183 = all in-phase transitions).
- Maxima agree on all three sides: FLATTR / phase 91, FLATSW 14, FLAT 69, 66 / 73 / 8 on nep92_n40. My engine also has the n > 200 games:
  s3quad_K8_m30 has the longest phase in the corpus, 263, with 0 violations.

## C.3 Line notes
- FIXD-N1 = my L-1 (free k). The same fix. Applied in revision L-1 (fe5c9e33): «k → k + 1» inserted, «an Even vertex x switched at k». Checked
  by token diff against ba09dd26 (7 replace / insert ops, all of them FIXD-N1, N2, N4, plus the header).
- FIXD-N2 (standing premise of R57): AGREE. I missed it. MON reads R15 (a) (a statement about VJ00's Ωσ) as a statement about Ξ_σ, and that
  needs S1's procedure to realise the pointwise optimum. Revision L-1 adds «under the standing SPEC premise of RESULTS R57». Lemma OWN does
  not need it (it reads the procedure directly), but its corollary uses R15 (a), so FLAT-SW via OWN also rests on it.
- FIXD-N4 (citation «R93 (a) (Fact LEX, COMMON PREFIX)»): AGREE. Applied in L-1.
- My L-2 (P in PHASE-RED′'s conclusion is bound only inside the hypothesis' parenthesis): REFEREE reads that «every phase P» quantifier as
  covering the conclusion (its §6, second pass). I keep L-2 as REQUIRED. As written, «(any phase P of any N5 run)» sits inside the antecedent,
  and the consequent's P has no binder of its own. The fix costs three words («then every phase P has»). It is NOT in revision L-1; the
  Lead routed it to L-NEW 39's next revision.
- L-3 (τ → τ_t): optional, unchanged.

## C.4 Theorem SW-KEEP (REFEREE §4b): SIGNED (Opus 5.5, D15)
Checked step by step from REFEREE's text, against R15 (a), the R57 standing premise (Ξ_σ ⊴ val(σ, π) for every positional Odd π), [LEX] /
COMMON PREFIX, and the definition of a play value.
- Fact F. In a positional pair the play from x is a lasso. If x is not its own cycle node, then either x is on the tail (and the play from
  σ(x) never returns to x), or x is on the cycle below its top c (and the play from σ(x) meets c before it comes back to x). Either way
  val(x) = x ⊕ val(σ(x)) with x ∉ Q(val(σ(x))). If x is its own cycle node, val(x) = (x, ∅, 0), and σ(x) lies on x's cycle, all of whose
  other vertices rank below x, so val(σ(x)) = (x, ∅, ℓ) (ℓ = 0 for a self-loop). ✓
- (1a) Own cycle node at exactly one of the two states: the first components differ. ✓ (1b) Neither state: both sides are x ⊕ ·, with x
  in neither path set and the same cycle node (the values are equal); x ⊕ · is injective there; so Ξ_σ′(e) = Ξ_σ(d) ◁ Ξ_σ(e) ⊴ Ξ_σ′(e)
  (improving edge; R15 (a)), a contradiction. ✓ (1c) remains. ✓
- (2) Ξ_σ(d) = (x, ∅, ℓ_d) ◁ Ξ_σ(e) ⊴ Ξ_σ′(e) = (x, ∅, ℓ′). The outer CS agree on n + 1 coordinates, so by COMMON PREFIX Ξ_σ(e) has cycle
  node x and empty path set. If π_e visited some x′ ∈ S ∖ {x} (before x or on x's cycle), x′'s (σ, σ̄_σ)-play would be a suffix of π_e, with
  cycle node x ≠ x′, against (1) for x′. (Under the theorem's hypothesis every x′ ∈ S keeps its value, so (1) applies to it.) ✓
- (3) Y := valuation of the (σ′, σ̄_σ)-plays. A play avoiding S is unchanged. Otherwise take x, the first S-vertex on π, and p the prefix
  before it (p avoids S). Under σ the play continues around x's cycle with top x: Ξ_σ(v) = (x, Q(p), |p|). Under σ′ the play is p, then
  x → e, then π_e up to x. On that stretch σ′ = σ (π_e avoids S ∖ {x} by (2) and stops at its first visit of x), and every vertex ranks
  below x (empty path set). So the cycle is x → e → … → x with top x, and Y(v) = (x, Q(p), |p|). This covers v ∈ S (p empty). ✓
- (4) Ξ_σ′ ⊴ Y (optimality of σ̄_σ′ against σ′: R57 premise), Y = Ξ_σ ⊴ Ξ_σ′ (R15 (a)): equality. ✓
- «Moreover» clause: it is (1). ✓ Corollary FLAT-SW: at a Ξ-changing transition σ changes by Switch_I with I ⊆ Iσ and one edge per vertex
  (R15 (d); for N5-LZC box 73 §4 (a)). If every switched vertex kept its value, SW-KEEP would give Ξ_{k+1} = Ξ_k. ✓ The conclusion holds at
  every Ξ-changing transition, in a phase or not. In a FLATTR transition the change is flat. ✓
- Premises: R15 (a), (d), the R57 standing premise, R93 (a) COMMON PREFIX. All landed. No gap.
- Relation to my proof: both proofs pass through the same dichotomy. In a Ξ-changing transition some switched vertex is not its own cycle
  node at both states. SW-KEEP reaches the «both states» case by play surgery plus optimality (R57). OWN reaches it by running S1's
  procedure. The strict-rise half is the same argument in both: SW-KEEP (1b) is R91 SW-IN's step. SW-KEEP needs no phase hypothesis, because
  case (1a) disposes of the mixed case directly; my corollary uses λ_Ξ constant on the phase. SW-KEEP is therefore slightly more general
  (every Ξ-changing transition of the run), which suits the revised line.
- Mechanical: my fixd_check.py checks the conclusion at every in-phase Ξ-changing transition (SWS / FSW, 0 violations, 1132 × 2 runs plus
  the n > 200 games). own_check.py tests OWN's hypothesis, which implies SW-KEEP's «both states» case.

## C.5 Lead reading for FLAT-SW (Lead 16:34Z)
Lead reading, quoted: «it counts as two-referee signed if EACH referee signs at least one proof the other also signs. You sign SW-KEEP, and
REFEREE checks your OWN-based proof (report §5).» My half is done: SW-KEEP SIGNED (C.4). For the revised line I propose citing SW-KEEP as the
proof of record. It needs no phase hypothesis and no reading of S1's procedure, and the premises it uses are those the line already carries
after FIXD-N2. Lemma OWN can stand as a second proof once REFEREE has checked it.

## DONE / FINDINGS / NEEDS
- DONE: this §C; per-game comparison against REFEREE's logs; the comp54_n80 re-run from the repaired start (55 / 22 / 32); token diff of
  revision L-1 (fe5c9e33, sha1 7e99a4a9).
- FINDINGS: (1) joint gap map §2-§4 EMPTY, all SIGNED by both. (2) SW-KEEP SIGNED by REFEREE-2. (3) REFEREE's 6460 vs the lane's 6503 is
  fully explained by run-set choices: REFEREE skips n > 200 (MAXN), and falls back to the best-reward start on partial start files. My N-1
  explains none of it. (4) My N-1 is WITHDRAWN as a correction: the lane's totals equal valid runs from the repaired comp54 start. Only a
  note remains (repair the start file at vertex 11; the lane's reader should validate starts). (5) Revision L-1 applies FIXD-N1 (= my L-1),
  N2 and N4 correctly. My L-2 is still open.
- NEEDS: Lead: send L-2 to L-NEW 39's next revision; once REFEREE signs OWN, ask for the revised line (PHASE-RED′ unconditional, citing
  SW-KEEP) for both referees to word-diff.
