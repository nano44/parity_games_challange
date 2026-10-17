# C6: landing gate for RESULTS R6 (packet 3: K5'', (α) with Dep(Str), K6 closed case, Lemma O-P, GAP-A first step) — CHECKER, 2026-10-17

Target: docs/agents/R6-draft.md at trunk cf094ab (not edited). Branch: origin/claude/checker confirmed an ancestor of the
local branch, then trunk cf094ab merged by merge commit.
Sources:
- GAP-C.md §18l/§18n/§18p at the pin 6e0082f.
- GAP-C.md §18q at l-alg 89f0f4e.
- docs/referee/R-P3.md: e3f3256, and §C at 87f1043, 10:56:46Z.
- docs/referee-2/R2-P3.md: d555ebf, and §6 at f25feaf, 10:56:11Z.
- Code: Oink 8fbf0a7.

## Verdict: PASS (no required fix; recommended citation fixes N-1, N-2; notes N-3..N-6)
| check | verdict |
| --- | --- |
| 1 statement diff (a)-(e) and the five named points | PASS (N-1, N-2 citations) |
| 2 verdict quotes and independence | PASS (N-3, N-4) |
| 3 gap union; "closed" only for G-R6-1..5 | PASS (N-5) |
| 4 re-runs | PASS: REFEREE-2 probe corpus part identical; kin_viol_n29 8 iterations, verified |

## 1. Statement diff
| item | source | signed | draft | |
| --- | --- | --- | --- | --- |
| (a) K5'' | §18q (89f0f4e): Dep(Str) definition, "K5'' (SIGNED by both): A_< \ Reg ⊆ Dep(Str)" | REFEREE §C2 SIGN; REFEREE-2 §1 SIGN; (i'), (ii) signed by both (REFEREE §C1 "remain signed"; REFEREE-2 table) | Dep(Str) "(rescue witnesses; for a fired tangle, its escapes and its old vertices outside Reg)", "A_< \ Reg ⊆ Dep(Str)", Consequence "Z_k open ⇒ τ_k has a successor in A_< \ Reg ⊆ Dep(Str) ≠ ∅", "(i') and (ii) ... signed too" | OK. "old vertices outside Reg" means §18q's "vertices of t' already in A_< \ Reg" |
| (b) (α), ⇒ only | §18q "(α), ⇒ form (SIGNED by both; this is all that K6 and the S-step reduction use)" | REFEREE §C3: ⇒ SIGN, ⇔ SIGN WITH GAPS (G-α1); REFEREE-2: SIGN of the ⇔ form, which contains ⇒ | "direction ⇒ ... This is the direction used by K6 and the S step"; G-R6-5 "R6 signs only the ⇒ form" | OK, only the ⇒ form |
| (c) K6 closed case | §18n / DTL-proof K6 note; §18q wording (G-b1, R-b) | REFEREE: SIGN WITH GAPS (G-b1, R-b closed); REFEREE-2: SIGN | "new tangle, a dominion, or a (β') duplicate with no escape in R. It uses neither K5 (i)/(iii) nor K5'" | OK. It does use K5 (ii) for an opponent τ_k (REFEREE (b)); the draft does not deny that |
| (d) O-P given (YZ) | GAP-C §18l line 843 at 6e0082f: "Lemma O-P (PROVED given (YZ)). A depth-0 P piece creates no orphan." | REFEREE (c) SIGN, "conditional on (YZ), as stated"; REFEREE-2 (c) SIGN | "Lemma O-P, given (YZ) (GAP-C §18j/§18l): a depth-0 P piece creates no orphan" | OK; conditional on (YZ). N-1: §18j has no O-P |
| (e) GAP-A first step, round r | GAP-C §18p at 6e0082f ("GAP-A angle, first step (10:38Z)") | REFEREE (d) "SIGN, for round r only"; REFEREE-2 (d) SIGN, "(d) SIGN, for round r only" (§6), "rounds r' > r are open" (§5) | "round r only ... rescue set of s+1 contains that of s, and V_{r+1}(s+1) ⊇ V_{r+1}(s)" | OK, round r only. N-2: the cited GAP-A-M §22 is not at the pin |
The Lead's named points:
- (b) is ⇒ only: yes.
- (e) covers round r only: yes ("round r only"; Scope: "the later-round step is open").
- (d) is conditional on (YZ): yes, in (d) and in G-R6-6 "(YZ) ... follows from the OPEN hypothesis (ACYC)".
- "Refuted proof step" paragraph: it claims a refuted proof step only. It says "(both referees, no instance, no run shown)"
  and "Whether the Up(Str) statement itself is false is open". This matches REFEREE-2 §6 ("this is a refuted proof step,
  not a refuted statement") and REFEREE §C1 ("Neither of us built an instance. The step is still refuted as a proof
  step"). The configuration t' = {x, y, u, o}, the code anchors (169, 73) and the play x → y → {x, u} match both reports.
- Scope names DE13 ("after DE13 the S and T steps must be restated") and DE14 ("RMONO (all rounds) is FALSE (DE14)"). Both
  entries exist in RESULTS.md on trunk (lines 257, 267).
All PASS.

## 2. Verdict quotes and independence
- REFEREE (final table plus §C): (a) "K5' (iii')/Consequence with Up(Str) REJECT; K5'' with Dep(Str) SIGN"; (b) "(α) with
  Up(Str) REJECT; (α) with Dep(Str): ⇒ SIGN, ⇔ SIGN WITH GAPS (G-α1); K6 closed case SIGN WITH GAPS (G-b1 wording, closed;
  R-b)"; (c) O-P SIGN; (d) SIGN, round r only. The draft's REFEREE line matches.
- REFEREE-2 (table plus §6, "Final verdicts ... unchanged"): (a) REJECT of the step, (i'), (ii) SIGN, K5'' SIGN; (b) Up(Str)
  REJECT as written, Dep(Str) SIGN, K6 closed case SIGN; (c) SIGN; (d) SIGN (round r only, §6). The draft's REFEREE-2 line
  matches.
- Independence:
  - REFEREE: "I did not read docs/referee-2/R2-P3.md before pushing this"; §C: "I read R2-P3 after my report was pushed
    (e3f3256)".
  - REFEREE-2: "docs/referee/R-P3.md was not read before this report was pushed"; §6 read e3f3256 after d555ebf.
  - Correct.
- N-3 (labels). REFEREE numbers its items (a) K5', (b) (α)+K6, (c) O-P, (d) GAP-A. REFEREE-2 uses the same four. The draft
  renumbers them: (c) K6, (d) O-P, (e) GAP-A. In the Signatures line "(d) O-P" and "(e)" therefore follow the draft's
  labels, not the reports' (REFEREE's "(c)" and "(d)"). The content is right. Suggest "(draft labels)" or the reports'
  labels in brackets.
- N-4 ("After comparison both reports agree on every item"). The agreement is reached in REFEREE §C (87f1043, 10:56:46Z),
  which withdraws REFEREE's SIGN.
  - REFEREE-2 §6 (f25feaf, 10:56:11Z) was written against e3f3256 and still records the disagreement on (a)/(b).
  - One labelling difference remains on the ⇔ form of (α): REFEREE-2 SIGN, REFEREE SIGN WITH GAPS (G-α1, raised after
    REFEREE-2's §6).
  - On everything R6 signs the two agree. Suggest "agree on every item R6 signs (REFEREE §C)".

## 3. Gap union
| referee item | draft |
| --- | --- |
| REFEREE G-a1, G-a2 (= REFEREE-2's two K5'' sub-cases) | G-R6-1 |
| REFEREE R-a (= REFEREE-2 note: "Z_k ∪" vacuous; Str inside A_<) | G-R6-2 |
| REFEREE G-b1 (= REFEREE-2 wording note, "G' \ R at depth > 0"; O0) | G-R6-3 |
| REFEREE R-b (W[τ_k] does not block extraction) | G-R6-4 |
| REFEREE G-α1 (⇔ form, p-owned τ_k) | G-R6-5 |
| REFEREE open point 1, REFEREE-2 §5: O-P conditional on (YZ)/(ACYC) | G-R6-6 |
| REFEREE open point 3, REFEREE-2 §5: GAP-A rounds r' > r open | (e) and Scope |
| REFEREE-2 §5: the Up(Str) correction to go into GAP-C §18n, the K6 note, and the citations of (α) | done: §18q "Citations updated to the Dep(Str) form: §2 rows ..., §17 Step 1, §18l Reduction, §18p ledger, DTL-proof.md K5 and K6 notes, C6-DTLhat.md" |
| both: nothing Lean-checked | G-R6-6 |
| REFEREE open point 2: "K6's open case, the 'Orphan analysis' and 'Route' are SKETCH" | not named (N-5) |
| REFEREE-2 §5: "T-piece orphans are open" | not named (N-5). O-P is stated for P pieces only, so this is not an overstatement |
- "Closed" covers G-R6-1..5 only: "G-R6-1..5 are closed in the reports and imported into the author's text at l-alg
  89f0f4e; G-R6-6 lists dependencies and open hypotheses". Correct.
- I checked the import at 89f0f4e §18q: Dep(Str) with the non-straddling sub-cases (G-R6-1), R-a, G-b1 and R-b wording,
  and the G-α1 fix.
- N-5 (recommended). Add to G-R6-6:
  - "K6's open case ((α) shape), its Orphan analysis and Route: SKETCH, not signed (REFEREE open point 2)";
  - "orphans created by T pieces: open (REFEREE-2 §5)".
  Optionally list the signed dependencies that (d) and (e) use: NT-f/FM (R4), Lemma 1.5a, FDL (R5 (h)).

## 4. Re-runs
- REFEREE-2 docs/referee-2/R2-P3/ @ d555ebf:
  - Build: dtl_probe3.patch on Oink 8fbf0a7. Its removed lines are the same counter-only rewrites as R2-PROVED2's. Release
    build.
  - Run: corpus at d555ebf (254 .pg), 2 in-orders × relabel seeds 0-1, with R2-STEP5's run.sh, paths only changed.
  - Result: runs 1014, no-probe-line 0; {'m1': 35300, ..., 'P': 19102, 'P0': 14074, 'yz_viol': 0, 'dom_str': 2,
    'tangles': 14283, 'dup': 6, 'dup_same': 0, 'k5st': 2550, 'k5nonempty': 0, 'k5str': 0, 'k5incl': 0, 'k5open': 0,
    'k5cons': 0, 'orphP': 0, 'orphP0': 0}.
  - Identical to the corpus line of probe3_results.txt.
  - Not re-run: the random part (6,000 runs).
- Pinned Oink 8fbf0a7 on experiments/red/carry/instances/kin_viol_n29.pg (trunk blob 15ac712), `--dtl --no-single
  --no-wcwc --no-loops -v`: "found 2 dominions and 15 tangles; solved in 8 iterations; solution verified (13 strategies)",
  exit 0. Matches RESULTS DE13.

## Notes
- N-1 (recommended). (d) cites "GAP-C §18j/§18l". At 6e0082f, §18j is "The S step: DATA" and contains no Lemma O-P. The
  lemma is in §18l (line 843), which both referees cite. Use "§18l".
- N-2 (recommended). (e) cites "GAP-C §18p; GAP-A-M §22".
  - GAP-A-M §22 does not exist at the pin 6e0082f. It first appears at l-alg 89f0f4e: "Box 7 ... the root call across
    consecutive searches".
  - It is not what the referees signed, and it is where RMONO is refuted (DE14).
  - Cite "GAP-C §18p at 6e0082f" for the signed step, and GAP-A-M §22 only as context.
- N-6. "Packet pinned at trunk 6e0082f (docs/alg/GAP-C.md §18l, §18n, §18p; DTL-proof.md K5/K6)" omits §18j. That is
  consistent with N-1.

## Fix list (none required)
Recommended: N-1 (§18l), N-2 (§22 citation), N-5 (two open items). Optional: N-3 (labels), N-4 ("every item R6 signs").
The draft may land as written. If the Lead applies the recommended fixes, a re-diff of the text only is needed.
