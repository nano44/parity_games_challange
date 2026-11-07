# Draft RESULTS DE37 (Lead; first fill 2026-11-07T06:09:58Z by date -u (subagent); on P-M2D-DEAD line L-3, docs/lower/P-M2D-DEAD-line-L3.txt, l-lower afc85c57, sha1 4c056511a9305815c756ad858d9ca4ed5977edcf) — to CHECKER C131 — NOT LANDED; to append after DE36 as the last lines of RESULTS «## Dead ends»; no GAPS change
FIRST FILL. Read at the origin heads fetched 2026-11-07 05:20Z-06:10Z by date -u (claude/l-lower afc85c57, claude/l-red b14066e1,
claude/referee 70ec6882, claude/referee-2 59bfa452 (successor 30's Addendum 2; 05:20:03Z), claude/checker 2603f321, claude/l-new and
claude/l-si as fetched); trunk 5ec57d84 (R115 landed): RESULTS sha1 0ea360253a0e102ecf5750e187233ab750d0af04 (13,681 lines; DE36 ends at l.
13681, the last line), GAPS 19da0f5180dff9e1f90b72222b6118091adb50d4 (23 lines). Objects re-hashed by me (sha1sum of git show): packet
docs/lower/P-M2D-DEAD.md 3ca5b9fae6216511f6d45e00c3084c1f577cbfaa at 87fcdf73 and at afc85c57 (cmp equal); fixes
docs/lower/P-M2D-DEAD-fixes.md f5b3f78ac37451fbd48ef7d6e3f3619438f35437 (49 lines, entries 1-2) and line L-3
docs/lower/P-M2D-DEAD-line-L3.txt 4c056511a9305815c756ad858d9ca4ed5977edcf (one line) at afc85c57; L-1
1dec8b4da3be767d4cffeb2f37fdd2f017cb10e6 and L-2 8ca7bcca624b6bc9ca6ee92eb46457608efbe051 (both superseded; these are file sha1s, not
commits); KILL_M2D_d6_mu13.json 5301c716f68f219bda2806f29b317c94e0ed5df0 and KILL_M2D_d8_mu21.json d96c2b3657e79c410b180580d829366cbecc9ea4
at afc85c57; p_m2d_check.py 981398ef02b79e429656355f1f6db307dde04362 at afc85c57 (REFEREE and REFEREE-2 ran 9e0e0d12… at 87fcdf73; the later
version adds the L-1/L-2/L-3/fixes pins); L-RED replay.out 4492ee284db25cb8cefc9702c1a343352e4b4ab3 (7,591 B) at 6e743ab1; P-IDEAL-MOVES.md
5ce2947d1ee4dab317e5c06446b38f050146cafb and N5-RISEPROOF-box181.md c8a5ad0e3a82fd865895ea66f131a5d07d2d0f41 at d86adc86; P-IDEAL-MOVES line
L-5 a42257cb159b2e51128c2334062d44edb97661f6 at the l-new head; REFEREE docs/referee/R-P-M2D-DEAD.md at 70ec6882
dca5fc519ca262306db00afc4f953a6df9269a05 (177 lines: report c011995c l. 1-116, §C 008039cc l. 118-154, §C add. 1 70ec6882 l. 156-177);
REFEREE-2 docs/referee-2/R2-P-M2D-DEAD.md at 59bfa452 0071e5c69ac2cf4c1408689b8dbf2fd2188cd6f6 (121 lines: report 6eba8b93 l. 1-77, Addendum
1 5c8aea53 l. 79-97, Addendum 2 59bfa452 l. 99-121; l. 1-97 byte-equal to 5c8aea53's file). Read: L-NEW box 188 at 6d043927 and 42427d9e;
L-SI docs/si/N5-TROPICAL-box76.md at 0803d551 (§8, l. 167-170); DECISIONS L50 (l. 440-449); RESULTS R104 (l. 9864), R110 (l. 11323), R114
(l. 12394, MOVE-RISE; l. 12593); docs/agents/DE35-draft.md, R106-draft.md (DE36 part), C98, C117, C120-C129. Re-runs: (1) the check block
from git archive afc85c57 (experiments/ and docs/lower/), in experiments/lower: `python3 -I l3/p_m2d_check.py --table`,
2026-11-07T05:22:06Z, rc 0, «P-M2D-DEAD CHECK PASS», per-step tables character-equal to packet §2; (2) my own transcription of the R104 step
rule (scratch tools/own.py; it follows the same rule as p_m2d_check.py's run2, so it is a re-measurement, not an independent
implementation): Ξ-targets, ISO, Ξ-acyclicity, the R110 wiring, T, moves(z) and the steps at which the key order of z's two options changes:
d 6 «[2, …, 13]», d 8 «[1, …, 13, 17, …, 24]», 12 and 21 changes, equal to L-3's obstruction clause and to both referees' measurements.
TRUNK STATUS AT THIS FILL: 87fcdf73, 8938e403, afc85c57, c011995c, 008039cc, 70ec6882, 6eba8b93, 5c8aea53, 59bfa452 and 6e743ab1 are named
in the entry on their branches only; the entry makes no statement about trunk (C113 E-2 lesson). The merges committed with this draft put
the l-lower, l-red, referee, referee-2 and checker heads on local trunk; the Lead pushes trunk before landing.
to check: FLAGS (G-1 to G-9; G-4 is a landing condition), then the DATA CHECK, then the ENTRY (the block that lands), then the Addendum
(re-runs, sweeps, landing simulation).
- G-1, FORM AND PLACE. As DE35 (C98) and DE36 (C117): one list item «- DE37 (<DATE>): …» in «## Dead ends», appended after DE36 as the last
  lines of RESULTS (DE36 is l. 13665-13681 at trunk 5ec57d84 and is the last line of the file; DE entries have no blank line between them,
  C98 Add. 2). <DATE> is the landing date by date -u (C114 Add. 1 E-1); no other placeholder; 0 «|». A dead-end entry is Lead text in DE35 /
  DE36 form, not a «### R» heading, so it is not L-3 verbatim; every clause of L-3 is carried (G-6).
- G-2, NUMBERS. «DE37» occurs 0 times in RESULTS; C118 §5 and C129 §4 used it only to say no row is due for lane conjectures killed inside a
  landed line («DE37» stays free). This is the separate DEAD record of Lead reading L50 (2) («The DEAD record is a separate entry.»), so it
  takes DE37. C131: docs/checker/ holds C1-C129 at origin claude/checker 2603f321 (no C130, no C131 file, no commit subject naming C130 or
  C131); C131 is free.
- G-3, GAPS. No GAPS change. DE30-DE35 landed with an empty GAPS diff (C98 Add. 2: «The GAPS diff is EMPTY»); DE36's GAPS l. 11 UPDATE was
  R106's, landed with R106. «MOVES-2D» occurs 0 times in GAPS; G-N5-TIME stays OPEN and its row does not change.
- G-4, LANDING ORDER (REQUIRED condition, my reading). The entry names «RESULTS R116» (one sentence). R116 is not landed at trunk 5ec57d84
  (C129 FAIL E-1/E-2; line L-5 a42257cb). DE37 lands after R116. If the Lead must land DE37 first, replace exactly the sentence «RESULTS
  R116 (P-IDEAL-MOVES) states in Corollary MOVES-EQUIV that MOVES-2D would give T^R(d) ≤ 4d² − 4d + 3; with MOVES-2D false that implication
  is vacuous, while MOVES-EQUIV's μ(d) ≤ T^R(d) ≤ 3 + (2d − 2)μ(d) and R116's other signed statements do not depend on MOVES-2D (Lead
  reading L50 (2)).» by «Corollary MOVES-EQUIV of P-IDEAL-MOVES (§1, claude/l-new d86adc86) states that MOVES-2D implies T^R(d) ≤ 4d² − 4d +
  3; with MOVES-2D false that implication is vacuous, while MOVES-EQUIV's μ(d) ≤ T^R(d) ≤ 3 + (2d − 2)μ(d) and P-IDEAL-MOVES's other signed
  statements do not depend on MOVES-2D (Lead reading L50 (2)).» (the quote sweep of the Addendum covers both forms). Source of the
  implication: P-IDEAL-MOVES §1 l. 89-91 (MOVES-EQUIV, «In particular MOVES-2D implies T^R(d) ≤ 4d² − 4d + 3»); L-5 words it «(the lane
  conjecture MOVES-2D, not claimed here) would give T^R(d) ≤ 4d² − 4d + 3». The vacuity is logic (a false premise), not DATA.
- G-5, RISE-2D NOT TAKEN (note; the Lead decides). RESULTS R114's signed MOVE-RISE («R(x, k) ≥ moves(z) when the Ξ-target of (x, k) is the
  mover z», at any degree) with instance (a) gives R(4, 1) ≥ 13 > 12 = 2d, so R114's lane conjecture RISE-2D («every option of a run on
  𝓛^R_d rises at most 2d times») fails on the same genome (my reading; not refereed). The entry keeps the Lead's scope (it kills MOVES-2D
  only) and says «nothing about RISE-2D», as packet §7 does. If wanted, a separate line needs both referees.
- G-6, L-3 CLAUSES CARRIED. Statement and origins (with fixes entry 1 N-1: P-IDEAL-MOVES §0's words quoted, box 181's own words quoted
  separately); both instances with sha1, 𝓛^R_d, Ξ-acyclic, not ISO, stored start, T, mover, level, Ξ-source option, the count (PM-L2 applied
  to both); obstruction verbatim from L-3 with its label «a description, no separate DATA» (PM-L1); the three L-LOWER implementations, XSIM
  0, movescheck counters with their run set (PM-L3); L-NEW box 188, L-SI 41 with commit and file (PM-L4), L-RED 52 with 6e743ab1 replay.out
  (PM-C1, W-1′), both referees' simulators (W-1); «MOVES-EQUIV is unaffected» (as the R116 sentence); the NOT-claims (T^R(d), growth of μ, d
  ≤ 5, G-N5-TIME). Added beyond L-3: the ISO scope from L50 (1), the ISO witnesses (option (0, 0), option (10, 1)), the steps at which z
  moves, the membership and check-block results, the referee verdict commits, the R116 sentence, RISE-2D / N5 / TARGET.md / L3-families
  NOT-claims.
- G-7, STALE STATUS. No «pending», «not yet», «CANDIDATE» or trunk sentence in the entry (script, Addendum). L50 (1)'s interim label «DEAD
  (lane, triple-replayed)» is superseded by the refereed DEAD SIGN at both referees with L-3 MATCHES; the entry does not repeat the interim
  label. Box 188's draft L-4 for P-IDEAL-MOVES (its §1) and the 42427d9e «REC_d10_tower» replay are not cited.
- G-8, REPLAY POINTERS. L-NEW box 188: the «REPRODUCED (both)» answer is at 6d043927 (l. 8); 42427d9e adds §3 (the ISO reading;
  REC_d10_tower). L-SI 41 replays all nine L-LOWER genomes; the entry quotes its sentence only. L-RED replay.out holds the two quoted lines
  twice (§3 and §4, the renumbered copies). REFEREE-2's replay tool is r2moves.py class G (R2-P-IDEAL-MOVES) driven by
  R2-P-M2D-DEAD/r2m2d.py (r2m2d.out); REFEREE's is scratch/t3r_sim.py driven by scratch/m2d_replay.py.
- G-9, movescheck RUN SET. «0 on both stored-start runs and on all 4,096 starts of the d 6 genome» is L-3's PM-L3 text. The counter is
  experiments/lower/l3/xcheck.py (L-NEW movescheck.py check_run); its output is not a committed file at afc85c57; REFEREE §4 re-ran it (l.
  65-68, «SIM-MISMATCH 0»), and REFEREE-2's r2moves counters (a superset of movescheck's) are 0 on all 4,096 d 6 starts and the d 8
  stored-start run (Addendum 1). I did not re-run xcheck.py.
DATA CHECK (the C120-C129 rule: every count or measured clause of the entry has a counter of matching unit, set and scope, or is in a
no-DATA list). Clause → counter (unit; set; scope) → verdict:
- (a)/(b) «𝓛^R_6» / «𝓛^R_8», «Ξ-acyclic», «not ISO» → memcheck.py rows (ii), (iv), (iii) (per genome; the two files; R110 wiring, DFS on the
  Ξ-graph, «no option has Ξ-target 0 or 1»), memcheck.out «ALL PASS» for both; referees' own membership code (REFEREE §3 table, REFEREE-2
  (2) table); my own.py → MATCH.
- «option (0, 0) has Ξ-target 1» / «option (10, 1) has Ξ-target 1» → REFEREE-2 (2) table l. 37 (per option; all options; one genome each);
  own.py lists exactly these options with Ξ-target 0 or 1 → MATCH.
- stored starts, «T 13» / «T 24» → p_m2d_check.py (T = steps of the run from G["start"]; asserted against the pins), REFEREE §4, REFEREE-2
  (3), replay.out «T 13» / «T 24» → MATCH.
- «mover 8 of level 4, the Ξ-target of option (4, 1)» / «mover 15 of level 7, the Ξ-target of option (0, 0)» → memcheck (vii) («Xi-target:
  True»), REFEREE §4 column «options with Ξ-target z» ((4, 1); (0, 0): exactly one option each), own.py → MATCH.
- «moves at every step 1-13», «moves at steps 1-13 and 17-24», «moves(8) = 13», «moves(15) = 21» → p_m2d_check.py mv (unit: steps t ∈ [1, T]
  with s_t(z) ≠ s_(t−1)(z), the §0 binder; one run, the stored start; asserted 13 and 21), the --table output (step lists), REFEREE §4
  «steps moving z» column, REFEREE-2 (3) → MATCH. «> 12 = 2d», «> 16 = 2d»: arithmetic.
- Membership «rows (i)-(vii) ALL PASS on both» → memcheck.out (two «ALL PASS» blocks for these files; the file has nine) → MATCH.
- check block «P-M2D-DEAD CHECK PASS» with «sha1 pins, … agree state for state, memcheck» → p_m2d_check.py asserts S1 == S2 (whole state
  sequences), the two sha1 pins, «ALL PASS» from memcheck.py; my re-run rc 0 → MATCH.
- «sim.py equals L-NEW's box150 Gen state for state» → packet §5, REFEREE §4 (xcheck.py, «sim.py = L-NEW Gen state for state»), memcheck
  (vii) (moves by sim.py = by box150 Gen) → MATCH (lane DATA, referee-re-run).
- «XSIM 0 against box139 paths.py» on both files → packet §5 (lane), L-RED replay.out «box150 … XSIM 0» on each of the nine genomes → MATCH
  (not re-run by me or by REFEREE, who says so, §5).
- «movescheck counters are 0 on both stored-start runs and on all 4,096 starts of the d 6 genome» → xcheck.py (G-9); REFEREE §4 l. 65-68
  (same set, re-run) → MATCH (output file not committed: G-9).
- Independent replays: each quoted from its committed file; box 188 «REPRODUCED (both)» (both instances), L-SI «Every (d, T, mover, moves)
  of the README table is reproduced» (nine genomes, a superset), L-RED's two lines (one per instance), referees' per-step tables «equal the
  packet's §2 tables» (REFEREE §4 l. 62, REFEREE-2 (3) l. 47) → MATCH.
- Obstruction: labelled «a description, no separate DATA» (L-3); its flip-step numbers are re-measured by REFEREE (§5 PM-L1, l. 83-86),
  REFEREE-2 (Addendum 1, l. 85-86) and my own.py (12 changes at d 6, 21 at d 8) → MATCH. «upward Ξ-options»: REFEREE-2 (2) counts 11 and 12
  upward options → MATCH.
- R116 sentence: logic and cited text, no count → no DATA needed.
- NOT-claims: no counts → no DATA needed.
Result: every measured clause has a counter of matching unit, set and scope; no clause needs a no-DATA entry beyond L-3's own label on the
  obstruction.

ENTRY (the next block up to the blank line; lands verbatim with <DATE> filled):
- DE37 (<DATE>): lane CONJECTURE MOVES-2D, as worded in P-IDEAL-MOVES §0 (claude/l-new d86adc86, docs/new/P-IDEAL-MOVES.md l. 77-78) «on
  𝓛^R_d every z ∈ Z moves at most 2d times in every run», with «moves(x) := #{t ∈ [1, T] : x ∈ Mv_t}» and Z the movers that are the Ξ-target
  of some option (same §0, l. 63), first stated in L-NEW box 181 (d86adc86, docs/new/N5-RISEPROOF-box181.md l. 20-21) as «on 𝓛^R_d, every
  mover that is the Ξ-target of some option moves at most 2d times», and stated on all of 𝓛^R_d, not on ISO genomes only (Lead reading L50
  (1), docs/DECISIONS.md), is DEAD by two measured instances. Refereed: DEAD SIGN by REFEREE 25 (docs/referee/R-P-M2D-DEAD.md c011995c) and
  by REFEREE-2 29 (docs/referee-2/R2-P-M2D-DEAD.md 6eba8b93), each on its own simulator; line L-3 MATCHES at both (REFEREE §C add. 1
  70ec6882; REFEREE-2 Addendum 2 59bfa452). Packet P-M2D-DEAD (L-LOWER successor 3; docs/lower/P-M2D-DEAD.md, frozen at claude/l-lower
  87fcdf73) with fixes entries 1-2 (docs/lower/P-M2D-DEAD-fixes.md) and line L-3 (docs/lower/P-M2D-DEAD-line-L3.txt), both at claude/l-lower
  afc85c57. Instances (experiments/lower/l3/kill/, each run from its stored start): (a) KILL_M2D_d6_mu13.json (sha1
  5301c716f68f219bda2806f29b317c94e0ed5df0): 𝓛^R_6, Ξ-acyclic, not ISO (option (0, 0) has Ξ-target 1); stored start 000000001101; T 13;
  mover 8 of level 4, the Ξ-target of option (4, 1), moves at every step 1-13: moves(8) = 13 > 12 = 2d. (b) KILL_M2D_d8_mu21.json (sha1
  d96c2b3657e79c410b180580d829366cbecc9ea4): 𝓛^R_8, Ξ-acyclic, not ISO (option (10, 1) has Ξ-target 1); stored start 1101101001010010; T 24;
  mover 15 of level 7, the Ξ-target of option (0, 0), moves at steps 1-13 and 17-24: moves(15) = 21 > 16 = 2d. Membership (DATA; R104's
  IDEAL genome, R110's 𝓛^R_d, Ξ-acyclicity, the binder of moves): experiments/lower/l3/memcheck.py rows (i)-(vii) ALL PASS on both
  (experiments/lower/l3/kill/memcheck.out), and both referees' own membership code from the RESULTS text (REFEREE §3; REFEREE-2 (2)).
  Replays (DATA): the check block experiments/lower/l3/p_m2d_check.py (experiments/lower/check.sh; sha1 pins, L-LOWER's sim.py and an inline
  second implementation with literal β-sets agree state for state, memcheck) ends «P-M2D-DEAD CHECK PASS»; L-LOWER's sim.py equals L-NEW's
  box150 Gen state for state, trunk experiments/new/box150/check.py on both files gives XSIM 0 against box139 paths.py (L-LOWER; also in
  L-RED's replay.out), and the P-IDEAL-MOVES movescheck counters are 0 on both stored-start runs and on all 4,096 starts of the d 6 genome
  (experiments/lower/l3/xcheck.py, re-run by REFEREE §4). Independent replays: L-NEW box 188 (claude/l-new 6d043927,
  docs/new/N5-KILLREPLAY-box188.md, «## 0. Answer: REPRODUCED (both)»; its addendum 42427d9e on the ISO reading); L-SI 41 (claude/l-si
  0803d551, docs/si/N5-TROPICAL-box76.md §8: «Every (d, T, mover, moves) of the README table is reproduced»); L-RED 52 (claude/l-red
  6e743ab1, experiments/red/r214/lower3/replay.out, sha1 4492ee28…: «max mover 8 lev 4 Xi-target 1 moves 13 2d 12 >2d» and «max mover 15 lev
  7 Xi-target 1 moves 21 2d 16 >2d»); REFEREE 25's simulator (docs/referee/scratch/t3r_sim.py with m2d_replay.py) and REFEREE-2 29's
  (docs/referee-2/R2-P-IDEAL-MOVES/r2moves.py with R2-P-M2D-DEAD/r2m2d.py), whose per-step tables equal the packet's §2 tables. Obstruction
  (line L-3; a description, no separate DATA): a metronome reading the key order of the pair one level below it, which flips at steps 2-13
  (d 6) and 1-13, 17-24 (d 8), fed by laps that the levels above level 1 replay between the level-0 moves (upward Ξ-options); the flip steps
  were re-measured by both referees (REFEREE §5 PM-L1; REFEREE-2 Addendum 1). RESULTS R116 (P-IDEAL-MOVES) states in Corollary MOVES-EQUIV
  that MOVES-2D would give T^R(d) ≤ 4d² − 4d + 3; with MOVES-2D false that implication is vacuous, while MOVES-EQUIV's μ(d) ≤ T^R(d) ≤ 3 +
  (2d − 2)μ(d) and R116's other signed statements do not depend on MOVES-2D (Lead reading L50 (2)). Not claimed: nothing about T^R(d) or the
  growth of μ; no polynomial or super-polynomial bound; nothing at d ≤ 5 (MOVES-2D there is lane DATA or open: packet §7, fixes entry 1
  N-2); nothing about RISE-2D, N5, real parity games or TARGET.md; the lane lemmas of docs/lower/L3-families.md are not used. G-N5-TIME
  stays OPEN.

Addendum (subagent, for the Lead; does not land; written 2026-11-07T06:1xZ by date -u). (1) FIRST FILL on line L-3 (l-lower afc85c57), to
CHECKER C131. L-3 MATCHES at REFEREE (§C add. 1 70ec6882, l. 177 «Verdict: fixes entry 2 is CORRECT. L-3 MATCHES, by the byte test and in
meaning. DEAD stays SIGNED.») and at REFEREE-2 (Addendum 2 59bfa452 by successor 30, l. 120-121 «Verdict: entry 2 **CORRECT**; **L-3
MATCHES** the packet with fixes entries 1-2, in bytes and in meaning»; its own replay r2m2d9.py on all nine genomes, «ROWS EQUAL 9 / 9»
against replay.out). (2) ENTRY: draft l. 107-139 (d[106:139]), 33 lines, the only line of the draft that starts with the DE37 label; one
<DATE>; 0 «|»; 58 «(» / 58 «)», depth never negative (script); no «pending», «not yet», «CANDIDATE», «PENDING» (script). Block sha1
(unfilled, with a final newline): 5eef2001c67b082c88ca2e4228165700bbb10ca7. (3) RE-RUNS: the check block from git archive afc85c57
(2026-11-07T05:22:06Z, rc 0, «P-M2D-DEAD CHECK PASS», «P-M2D-DEAD line files L-1, L-2, L-3 and fixes (entries 1, 2) pinned»); my own.py
(05:2xZ, rc 0). NOT RUN: xcheck.py, box150/check.py, the referees' and the other lanes' tools (their committed outputs and reports read
instead), scripts/verify.sh, the full experiments/lower/check.sh. (4) QUOTE SWEEP (tools/quotes.py: outermost guillemet quotes, whitespace
joined, split at the ellipsis, parts of 6+ characters; sources: packet, fixes, L-1, L-2, L-3, the two kill README/memcheck.out files at
afc85c57, my check-block output, P-IDEAL-MOVES.md, box 181, box 188 at 6d043927 and 42427d9e, L-SI box76 at 0803d551, L-RED replay.out,
P-IDEAL-MOVES L-5, both referee files at their heads, trunk RESULTS, GAPS, DECISIONS, C98, C118, C129, this draft's entry and flag G-4 for
the self-quotes): entry 8 quotes, 8 parts, 0 not found; whole draft 94 quotes, 80 parts, 1 not found: G-4's proposed replacement sentence
(new text, not a quote). (5) LANDING SIMULATION (tools/land.py on RESULTS at trunk 5ec57d84, <DATE> → 2099-01-01 for the simulation only):
RESULTS 13,681 → 13,714 lines, a pure append of the 33 entry lines after DE36's last line (l. 13681), prefix byte-unchanged: True; DE37 at
l. 13682-13714; «## Dead ends» stays at l. 13144; 0 «|» added; «DE37» 0 times in RESULTS before. GAPS unchanged (no UPDATE). After R116
lands (inserted before «**Erratum E-1**», above «## Dead ends»), the append is unchanged: DE37 still follows DE36 at the end of the file.
(6) NOT VERIFIED: the movescheck counters on the 4,096 d 6 starts and XSIM 0 (lane DATA, re-run by REFEREE and L-RED respectively, not by
me); L-NEW's mv.c and all-starts logs of box 188; L-SI's replay77.out (its sentence quoted, the file not opened); the referees' own tools
(reports read); whether R116 lands before DE37 (G-4); the RISE-2D consequence of G-5 (my reading only). (7) THIS DRAFT'S SHA1: a file cannot
state its own sha1; the actual sha1 and line count are in the hand-back to the Lead (re-measurable with sha1sum).
