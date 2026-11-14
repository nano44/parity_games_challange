# Draft RESULTS R131 (Lead; FIRST FILL by script (subagent) on P-N5-EXP line L-3 (a STAND-IN for the line of record L-4), docs/red-b/P-N5-EXP-line-L3.txt, claude/l-red-b 10dfedb6, sha1 fd9074a3b9961f59a1b64d5acdaa28529306ede9) — to CHECKER C148 — NOT LANDED; goes after R130 (RESULTS l. 16525 at trunk aeb90ac1), directly before the line-start «**Erratum E-1** (not a result» (l. 16725); its GAPS UPDATE on the row G-N5-TIME (GAPS l. 11), which then moves under «## Closed»
FIRST FILL (this text). Built by script in docs/agents/tools/r131/ (cfg.json: every input that can move; fetch.sh: the only network step;
  fill131.py; tools/*.py, tools/lanecheck.sh; build.sh; land131.py), untracked; nothing in the repository was added, committed, merged or
  pushed by the builder, and scripts/push.sh and scripts/verify.sh were not run. Read by git show at the heads of the fetch that fetch.txt
  records (Sat Nov 14 13:41:37 UTC 2026, by date -u; git ls-remote lines in the Addendum): claude/l-red-b
  10dfedb6574c9291011a5a7fbbdff261fe312d91, claude/referee 9ec40ff968ddc4a1c7f41a95d20aa6db6dbe40c3, claude/referee-2
  e643672d1343d414d9670066ec5564df78588beb, claude/l-si 8c06291418616eca059c9239bdf8d59aad4f320f, claude/l-comp
  dc6d831f7c56943a03070a9d268df2388565b438, claude/l-red c7ed9b8b6af43c4ae94a5fa15571193bc923eedc, trunk claude/vibrant-johnson-nxvvxo
  aeb90ac199aff97b7189666965d7fd7d7119cf29.
TRUNK: aeb90ac1 (2026-11-13T19:04:18Z). docs/RESULTS.md sha1 eecbd798b81ad431d1b753f5a7f92f3c63e56da1, 17,367 lines, 130 entries, last
  heading R130 at l. 16525, Erratum anchor l. 16725; docs/GAPS.md sha1 3fa61e1cf9ce48ab16ee6102c3ee145a7d7e0491, 23 lines, row G-N5-TIME l.
  11 (status open), Closed heading l. 13; TARGET.md sha1 a41d5e1a3d251b1e7c345c159651c08d76ad8165. land131.py works on the working tree and
  checks these anchors, not these sha1s.
LINE: L-3, docs/red-b/P-N5-EXP-line-L3.txt at claude/l-red-b 10dfedb6 (2026-11-13T19:17:36Z; L-RED-B successor 7: line L-3 (the line of
  record) and fixes entry 8 f …), sha1 fd9074a3b9961f59a1b64d5acdaa28529306ede9, 7,267 bytes, one line, parentheses 79 / 79, pipes 0.
  STAND-IN: the line of record will be L-4 (not on origin at the fetch); the second run changes cfg.json only (REPORT.txt).
PACKET: docs/red-b/P-N5-EXP.md FROZEN at 350d84eb (2026-11-13T12:55:07Z), sha1 c0449b17193f19619f33b366096762dfde27d542, 569 lines, 57,511
  bytes; byte-equal at 10dfedb6. FIXES: docs/red-b/P-N5-EXP-fixes.md at 10dfedb6, 1,180 lines, sha1
  013290889e9e08f58ae162baa0c2eb5082f4b135, entries 1-8.
REFEREES (git blame at the heads). REFEREE docs/referee/R-P-N5-EXP.md at 9ec40ff9 (784 lines): stage 1 l. 1-397 (c881709b
  2026-11-13T14:57:16Z), stage 2 l. 398-456 (ea09ae2e 2026-11-13T15:41:26Z), stage 3 l. 457-496 (7ca9c2b4 2026-11-13T15:44:37Z), stage 4 l.
  497-536 (577e8df9 2026-11-13T17:17:17Z), stage 4 addendum l. 537-542 (4cf6e1ff 2026-11-13T17:28:19Z), stage 5a l. 543-784 (31b28f2a
  2026-11-13T19:16:17Z). REFEREE-2 docs/referee-2/R2-P-N5-EXP.md at e643672d (633 lines): report l. 1-284 (33ff0e98 2026-11-13T14:17:17Z),
  Addendum 1 l. 285-320 (da20a307 2026-11-13T14:40:07Z), Addendum 2 l. 321-549 (f17a2708 2026-11-13T17:02:13Z), Addendum 3 l. 550-633
  (e643672d 2026-11-13T17:27:09Z); docs/referee-2/R2-box108.md (145 lines). Box 108: docs/si/box108-gk-proof.md at claude/l-si 8c062914.
OPEN SLOTS: the line of record L-4 (PENDING: stand-in L-3); fixes entry 9 (PENDING); REFEREE stage 5b (PENDING); REFEREE-2's line check
  (PENDING); and the checker token of the title. land131.py refuses to land while the draft holds the open-slot word anywhere but in that
  token.
CHECKS RUN AT THIS FILL (outputs verbatim in the Addendum): [lane] the lane's check.sh in a git archive with a negative control; [upd] the
  UPDATE builder with controls R128-R130 and five negative controls; [data] 32 DATA checks from the pinned outputs with a negative control;
  [prem] the premise entries at trunk; [shape] title, block, UPDATE, pipes, brackets, open-slot tokens, check_docs on a copy with a negative
  control; [lp] every quotation at its commit, file and lines, by a second implementation, with two negative controls; [sweep] every
  guillemet quotation of the file against the sources, with a negative control; [land] land131.py: refusal on this draft, refusal on a
  changed block, DRYRUN on a copy.
FLAGS FIRST (the builder's reading; nothing in the line or in any quoted text was changed; full list in REPORT.txt). G-LINE: the title
  stands on L-3, a stand-in for L-4. G-SLOTS: no referee has yet checked fixes entries 7 and 8 or any line after L-1; REFEREE-2's signature
  names entries 1-5, REFEREE's 1-6, the line's closing parenthesis names 1-7. G-K12 (wording inside the line): its correctness clause says
  "DATA for k ≤ 12" while its part (3) and REFEREE's table (stage 5a) have k = 13. G-R245 (note): the line gives L-RED 70's engine for k = 3
  … 8; R245 also carries k = 9, 10. G-STATUS (note): the line keeps its status phrase about two referees (Lead ruling, the form of R130).
  G-U: the UPDATE moves three labels, drops one scope string and keeps everything else, the obstruction clause and the L41 scope tail
  included. G-S: the Closed table of GAPS has an empty line inside it; the row is appended after its last row. G-NOW: land131.py changes one
  counter of docs/NOW.md; R130's landing changed two. G-1E-N3: the N5 half is conditional on R117 as landed and on SPEC's standing premise.
  G-5E: the first referee's stage 5a has four notes, N-5a to N-5d.

### R131 [refereed-only] DEAD-END packet for the candidate N5 (SPEC S1-S5 with FIX 1-4, from its default start S3), CONDITIONAL until two referees sign, in three parts: (1) UNCONDITIONAL (premise: RESULTS R104's definitions of the genome, IDEAL-ACYC, the X-chain order, the IDEAL step and L(G) only; no theorem of R104 used): (Theorem EXP-IDEAL, PROVED lane; its RESPONSE LEMMA in the prefix form LEMMA′ of fixes entry 4, with CAUSAL and STABLE in step form) for every k ≥ 3 the genome G_k of rule R (levels 0..k; unit j, 1 ≤ j ≤ k − 1, is a block pair u_j, v_j with an observer pair Y_j = (y_j, ȳ_j) and, for 2 ≤ j ≤ k − 2 only, an end-follower e_j and a second observer pair Y′_j = (y′_j, ȳ′_j), so the units 1 and k − 1 have four movers and the others seven; outside the units, the level-0 pair u_0, v_0 and the wires wv_j, 1 ≤ j ≤ k − 2, and wu_j, 2 ≤ j ≤ k − 2; all parities even, β-ranks by Ξ-depth with ties broken by β-id; generator experiments/red-b/gk.py) is in IDEAL-ACYC with N = 9k − 16 movers, M = 18k − 32 options (every mover has two) and k + 1 levels, its IDEAL run has exactly L(G_k) = 2^k − 2 steps and stops «stuck», and in it every mover of unit j (1 ≤ j ≤ k − 1) changes its option exactly 2^(j−1) times, v_0 once, u_0 and the wires never (11·2^(k−2) − 9 option changes in all); so R104's IDEAL-ACYC-POLY («there is a polynomial q such that L(G) ≤ q(N + M) for every G ∈ IDEAL-ACYC») is FALSE, already for genomes of degree 2 (N + M = 27k − 48); (2) PROVED-CONDITIONAL on RESULTS R117's Theorem REACH3 as landed (refereed-only; R117's standing premises, in the words of its title line: «with R104's premises as landed (1E-N3 = RESULTS R57 (b) in its two forms; RESULTS R24 (a) Lemma R and R24 (b)'s choice rule with RESULTS R103's bridge B and (R1) ruling; RESULTS R36 (c) Lemma P1 on the dual game) and RESULTS R15 (d) for termination only»): (Corollary EXP-N5) the N5 run of Γ3(G_k) from S3 (n = 135k − 230 vertices, m = 176k − 300 edges) has one FL run of length exactly 2^k − 2 and makes at least 2^k − 1 iterations, so no polynomial in n or in n + m = 311k − 530 bounds the number of iterations of N5 from S3; hence, through R117, N5 (SPEC S1-S5, default start S3) does not run in polynomial time, cannot pass gauntlet step 4 (TARGET.md §5), is a DEAD END as an M4 candidate, and G-N5-TIME is answered NO for N5 from S3; and, PROVED-CONDITIONAL on RESULTS R124's Corollary EXACT-L as landed (premise R117 (f), under SPEC's S1 tie-breaks, same standing premises): (Corollary EXP-N5′) N5 from S3 on Γ3(G_k) makes exactly 2^k + 1 iterations, with one fallback, at iteration 2^k − 1; obstruction RIPPLE (S4a's root-first key rule refuses an improving switch until the key order allows it, and on Γ3(G_k) this makes unit j + 1 respond twice in every response of unit j); (3) DATA (measured; every measured run is below n²: the largest, k = 13 (fixes entry 6, one engine), makes 8,193 iterations on n = 1,525 vertices, and 2^k − 1 > n² first at k = 23, n = 2,875, > n³ at k = 37, > n⁴ at k = 51, by arithmetic, not run; so the dead end rests on the proof of (1) and (2) and not on the DATA) (unit: one genome G_k, resp. one game Γ3(G_k); every counter named is a must-0 counter and is 0, every control fires): R104's eight membership clauses on G_3 … G_14 (b6member.py, member.out: viol 0); the IDEAL run equal state by state on three simulators, T = 2^k − 2, for k = 3 … 14 (b6sim.py, sim.out: ideq 0); the proof's facts and schedule against the run at every state and step for k = 3 … 14 (b6lemma.py, lemma.out: kfact, vfact, sched, tlen, rest, swk 0), and LEMMA′, CAUSAL and STABLE of fixes entry 4 at the 16,368 response windows of the runs for k = 3 … 14, at every triple (j, a, t) for k = 3 … 12, at every state of G_3 and G_4, and off the run (b6prefix.py, prefix_*.out: h1, h2, psched, aviol, pviol, dviol, loc, stviol, c0e0 0; the frozen wording of the lemma, as a control, fails at exactly k − 1 triples per k); N5 itself on Γ3(G_k), two engines and two Γ3 builders, for k = 3 … 12 (b6n5.py, n5.out and n5_k12.out: 2^k + 1 iterations, one fallback at iteration 2^k − 1, mover states equal to the model's; mism, wrong, wrong2, nonmover, engdiff, gdiff 0; winners equal to Zielonka's), and at k = 13 on one engine, the two Γ3 builders agreeing (fixes entry 6: b6n5ck.py, n5_k13.out: 8,193 = 2^13 + 1 iterations on n = 1,525 vertices, one fallback at iteration 8,191, mover states equal to the model's; mism, wrong, nonmover, gdiff 0; winners equal to Zielonka's; game experiments/red-b/data/b6b/pg/G_13_g3.pg), all files in experiments/red-b/data/b6b/out/; frozen instances Γ3(G_k) = experiments/red-b/data/b6b/pg/G_k_g3.pg, k = 3, …, 11 (175 to 1,255 vertices, 9 to 2,049 iterations), genomes of record experiments/red-b/data/b6b/G/G_k.json, k = 3, …, 14, at claude/l-red-b 350d84eb; independent replays, their counters in their own pinned outputs, cited, not re-run: L-COMP 22 BOX 48 (claude/l-comp dc6d831f: own generator, the model T = 2^k − 2 for k = 3 … 20, n5b on its own Γ3 builder 2^k + 1 iterations for k = 3 … 12, winners verified by Oink --tl and --zlk), L-RED 70 R245 (claude/l-red c7ed9b8b: own generator, the model for k = 3 … 12, its engine n5s237 for k = 3 … 8, verdict SURVIVES), REFEREE 35's pre-check (claude/referee 06ac891d: own simulator k = 3 … 15, own Γ3 builder and engine k = 3 … 12), REFEREE 36's first review (claude/referee c881709b: own generator and model k = 3 … 14, N5 on that lane's builder and engine for k = 3 … 9, games identical to this lane's files), REFEREE-2 41 (claude/referee-2 33ff0e98: own generator and model k = 3 … 16, own engine k = 3 … 11 with four solvers for the winners); NOT claimed: anything about N5 from other start pairs, about other S4a tie rules (DATA: N5′-xi makes 7 iterations on Γ3(G_4) and Γ3(G_6)) or about Howard's rule (DATA: at most 4 steps on the model), about any other candidate, or about parity games in general; N5's output on these games is correct (RESULTS R57 (b), Lemma OUT-G, under 1E-N3; DATA for k ≤ 12: winners = Zielonka's); TARGET.md §2 (M4) stays OPEN; not M3 or M4, not a TARGET.md claim; scope tail (Lead reading L41): CAUSAL and LEMMA′ of fixes entry 4 (4.3, 4.4) are referee-originated, stated and proved by REFEREE 36 (claude/referee c881709b, docs/referee/R-P-N5-EXP.md §5.3; its verdict on the RESPONSE LEMMA: «NOT SIGNED AS WRITTEN; SIGNED in the form LEMMA′ of §5.3 below»; after fixes entry 4, its stage 4, claude/referee 78515253, the same file §12: «RESPONSE LEMMA SIGNED as restated in fixes entry 4 (= LEMMA′ of §5.3 with CAUSAL and STABLE in step form).»), and are signed independently by REFEREE-2 42, in the form its signature sentence gives (claude/referee-2 f17a2708, docs/referee-2/R2-P-N5-EXP.md, Addendum 2 §A2.3: «REFEREE-2 signs 4.1 (S1)-(S4), 4.2 STABLE, 4.3 CAUSAL, 4.4 LEMMA′ with their proofs (4.2, 4.3, 4.5) and 4.6, as printed in docs/red-b/P-N5-EXP-fixes.md at claude/l-red-b 24f4d436 (sha1 9dc9179f…), (R3)'s range read as t − 1 ≤ τ < last (F-1).») (P-N5-EXP, docs/red-b/P-N5-EXP.md, with fixes entries 1-7, docs/red-b/P-N5-EXP-fixes.md; L-RED-B successors 5-7)., CHECKER PASS (docs/checker/C148.md, checker PENDING)
- Object (L-RED-B successor 5, D1 / D18 / D22 / D25, B6 attempt 2; frozen, unchanged during review): packet P-N5-EXP,
  docs/red-b/P-N5-EXP.md, sha1 c0449b17193f19619f33b366096762dfde27d542, 569 lines, 57,511 bytes (claude/l-red-b 350d84eb,
  2026-11-13T12:55:07Z, the file's only commit; identical at 10dfedb6). Both referees measured it (REFEREE «claude/l-red-b 350d84eb,
  docs/red-b/P-N5-EXP.md sha1 c0449b17193f19619f33b366096762dfde27d542, 569 lines» (l. 1); REFEREE-2 «docs/red-b/P-N5-EXP.md, sha1
  c0449b17193f19619f33b366096762dfde27d542, 569 lines, 57,511 B» (l. 3-4)). Its own status: «Status: a kill candidate; lane DATA + a lane
  proof. Nothing here is a result until both referees sign and CHECKER passes it (D1).» (l. 4). «To sign: §2 (Theorem EXP-IDEAL, Corollary
  EXP-N5), §4 (Lemma MEMBER), §5 (MOVE-2, K1-K4, V0-V4, WIRE), §6 (RESPONSE LEMMA, STABLE), §7 (the proofs). To check: §8 (where the start
  and the orders are used), §9 (DATA reproduction), §10. Not to sign: §9's numbers as statements (DATA), §11 (READING)» (l. 5-7). The
  object: rule R (packet §3) builds, for every k ≥ 3, a genome G_k of RESULTS R104's IDEAL model with levels 0..k and two options per mover
  («Counts: 2 + 2(k − 1) + (k − 3) + (k − 2) + (k − 3) + 2(k − 1) + 2(k − 3) = 9k − 16.» (l. 102)); generator experiments/red-b/gk.py (sha1
  5222f555f9572e5c92119a2bc1e16d02008a96c5 at the freeze commit; REFEREE-2 «generator experiments/red-b/gk.py, sha1
  5222f555f9572e5c92119a2bc1e16d02008a96c5 (192 lines, read in full)» (l. 4-5)). The claim attacked is the GAPS row G-N5-TIME, «N5
  SSI-GLOBAL makes polynomially many iterations (gauntlet step 4, running time)» (l. 11).
- Fixes: docs/red-b/P-N5-EXP-fixes.md, append-only («append-only; the packet docs/red-b/P-N5-EXP.md is never edited after its freeze commit
  350d84eb» (l. 1)), at claude/l-red-b 10dfedb6: 1,180 lines, 110,406 bytes, sha1 013290889e9e08f58ae162baa0c2eb5082f4b135, entries 1-8 by
  their headings (git blame: entry 1 l. 1-125 06d399c2 2026-11-13T14:03:12Z; entries 2-5 l. 126-829 24f4d436 2026-11-13T15:53:00Z; entry 6
  l. 830-881 0c8fdf9e 2026-11-13T16:43:45Z; entry 7 l. 882-1147 b1a93700 2026-11-13T19:11:57Z; entry 8 l. 1148-1180 10dfedb6
  2026-11-13T19:17:36Z); each stage of the file is a byte prefix of the next (asserted by script). At 24f4d436 it is the object of
  REFEREE-2's signature (829 lines, sha1 9dc9179fb08063cd59de25c5d3e16b0f8c693fbd), at 0c8fdf9e the object of REFEREE's (881 lines, sha1
  43a941eb6249f0278e342438f92293b7f7a4449e). Entry 1 (L-RED-B 5): «extra DATA, no change to any statement, proof or hypothesis» (l. 5); six
  DATA subsections 9.8-9.13, a pointer correction and the reproduction erratum 10.E (at the freeze commit the runner needs an absolute root;
  from entry 1 on it counts a failing stage and exits 1). Entries 2-5 (L-RED-B 6) answer the referees item by item: «What changes: the
  STATEMENTS of the RESPONSE LEMMA and of STABLE are replaced by the forms of entry 4 (the mathematics and every number stay); the LABELS of
  Corollary EXP-N5 and of the dead-end paragraph are fixed by entry 2; entry 3 adds a corollary; entry 5 is wording and records. Theorem
  EXP-IDEAL (a)-(c) is unchanged.» (l. 130-132). Entry 2 (labels): (a) UNCONDITIONAL, Theorem EXP-IDEAL (a)-(c) with its lemmas; (a′) «Let
  IDEAL-ACYC-POLY mean: there is a polynomial q such that L(G) ≤ q(N + M) for every G ∈ IDEAL-ACYC.» (l. 181), refuted by (b) alone; (b)
  Corollary EXP-N5 is «PROVED-CONDITIONAL on RESULTS R117's Theorem REACH3 AS LANDED [refereed-only].» (l. 190) and «it inherits R117's
  standing premises and adds none» (l. 191); (c) the dead-end sentences are read through R117, in full «under R117's Theorem REACH3 as
  landed, N5 (SPEC S1-S5) from its default start S3 makes at least 2^k − 1 iterations on Γ3(G_k), a game with n = 135k − 230 vertices and n
  + m = 311k − 530 vertices and edges; so N5 from S3 does not run in polynomial time, cannot pass gauntlet step 4, and G-N5-TIME is answered
  NO for N5 from S3.» (l. 211-213); (d) MEASURED: «So no measured run lies beyond an explicit polynomial bound of degree 2 or more, and the
  kill rests on the PROOF: (a) with R117 (and R124 for the exact count, entry 3).» (l. 221-223); (e) the correctness sentence is RESULTS R57
  (b), Lemma OUT-G, for every k and DATA for the k that were run. Entry 3: Corollary EXP-N5′, «For every k ≥ 3, N5 (SPEC S1-S5 with its FIX
  1-4 tie-breaks) from S3 on Γ3(G_k) makes EXACTLY L(G_k) + 3 = 2^k + 1 iterations, with exactly one fallback, at iteration 2^k − 1.» (l.
  256-258), with «The frozen Corollary EXP-N5 (at least 2^k − 1 iterations, by R117 alone) stays as frozen and is all the dead end needs.»
  (l. 273-274). Entry 4: the RESPONSE LEMMA restated: «The frozen STATEMENT of the RESPONSE LEMMA (l. 192-204) is REPLACED by 4.4 and the
  frozen statement of STABLE (l. 258) by 4.2; the frozen PROOF text (l. 205-257, 258-262) stays and is read as 4.5 says; Theorem EXP-IDEAL,
  its proof (§7, read as 4.6) and every other statement are unchanged.» (l. 314-316); «It does not write a third form: 4.3 and 4.4 ADOPT
  REFEREE 36's two statements word for word, 4.4 shows that REFEREE-2's PREFIX FORM is the same statement, and 4.5 gives the proof in the
  order both referees give.» (l. 318-320). Entry 5 (wording and records, «No statement changes. Each item: the referee's words, then the
  reading that completes or replaces the frozen words.» (l. 650)): 5.1 the rank clause read with its tie-break by β-id, 5.2 «step τ» (said
  once in 4.1 (S2)), 5.3 the text of §9.7's placeholder, 5.4 level widths, 5.5 genomes of record and raw files, 5.6 the mover order, 5.7 the
  JSON fields, 5.8 the other lanes' DATA with their commits, 5.9 two notes recorded. Entry 6: «N5 itself at k = 13 on one engine — extra
  DATA, no change to any statement, proof or hypothesis» (l. 831) (N5 at k = 13, engine 1, by the checkpointed driver b6n5ck.py). Entry 7
  (L-RED-B 7): REFEREE-2's F-1 to F-5 and REFEREE's stage 4, «two readings of entry 4, one of entry 5, the runner run_b6fix.sh repaired, one
  label, line L-2; no statement, proof, hypothesis or number changes» (l. 883): 7.1 «Accepted. Neither wording names the lower end of the
  range. Clause (R3) of 4.4 is to be READ, there and wherever it is cited:» (l. 935) «(R3) For T = last: if j ≥ 2, then s_τ(E(j)) = a for
  every τ with t − 1 ≤ τ < last, and E(j) moves to c at step last» (l. 937); 7.2 which frozen lines of §6 stay in force as definitions (a
  table of the frozen l. 191-204); 7.3 «READ the parenthesis as: (table: every Ξ-target is a u, v, y, ȳ, y′, ȳ′ or X).» (l. 1015); 7.4 the
  runner run_b6fix.sh repaired («every failure is counted, the last line ends «failures N», and the runner exits 1 if N > 0» (l. 1059); its
  test file ends «b6fixtest failed 0» (l. 1089)); 7.5 the two sentences of entry 2 (a′) labelled, «The lines L-1 and L-2 carry (i) only;
  neither names QUIET-KEY-1P, SW-POLY or P-N5-KEY1P.» (l. 1112); 7.6 guards, line L-2, pins. Entry 8: the line L-3 from L-2, «a record of
  the line only, no statement, proof, hypothesis or number changes» (l. 1149). Fixes entry 9 PENDING (the entry that records the line of
  record L-4; no referee has read it).
- The RESULTS line is L-3, fd9074a3b9961f59a1b64d5acdaa28529306ede9 (docs/red-b/P-N5-EXP-line-L3.txt, claude/l-red-b 10dfedb6,
  2026-11-13T19:17:36Z; 7,267 bytes, one line with its newline; 79 opening and 79 closing parentheses, no square bracket, no pipe character,
  6 guillemet quotations). The title is the line verbatim, with nothing inserted and nothing stripped (it has no date parenthesis and no
  dash separator; its status phrase, scope tail, source note and final full stop are the line's own: the landed form of R130). Its
  quotations are found verbatim by script: (1) R104's packet l. 75; (2) R104's packet l. 224; (3) RESULTS l. 13362; (4) REFEREE's report l.
  17; (5) REFEREE's report l. 522-523; (6) REFEREE-2's report l. 464-465. Its closing parenthesis names fixes entries 1-7 and L-RED-B
  successors 5-7. History of the line (the lane's builder experiments/red-b/b6line.py, named replacements, each old text exactly once): L-1
  (59c5309377eda882ba436ffe7eb03fbff598c7c8, 5,585 bytes, claude/l-red-b 24f4d436) was read by REFEREE-2 (Addendum 2 §A2.7: «Every clause
  that comes from this lane's review agrees with it» (l. 517), with three notes); L-2 = L-1 with REFEREE-2's L-a (the gloss of the units),
  L-b (R117's premises in the words of its title line), L-c (the L41 scope tail) and the Lead's L-d (k = 13 from entry 6), fixes 7.6: «L-2
  bytes 7267 (with its newline) lines 1 pipes 0 sha1 6e047c676e582484fe8eb87891764e8c1a7d9a18» (l. 1141); L-3 = L-2 with two replacements in
  the closing parenthesis, fixes entry 8: «L-3 bytes 7267 (with its newline) lines 1 pipes 0 sha1 fd9074a3b9961f59a1b64d5acdaa28529306ede9»
  (l. 1168). Line of record L-4 PENDING: this fill stands on L-3 as a stand-in; L-4 is to be L-3 with one clause changed (R124's Theorem
  ENDGAME-3-N5 named beside Corollary EXACT-L) and comes with fixes entry 9; no referee has read it.
- Claims signed (REFEREE successors 36 and 37, docs/referee/R-P-N5-EXP.md at claude/referee 9ec40ff9: stage 1 l. 1-397 c881709b, stage 2 l.
  398-456 ea09ae2e, stage 3 l. 457-496 7ca9c2b4, stage 4 l. 497-536 577e8df9, stage 4 addendum l. 537-542 4cf6e1ff, stage 5a l. 543-784
  31b28f2a; REFEREE-2 successors 41 and 42, docs/referee-2/R2-P-N5-EXP.md at claude/referee-2 e643672d: report l. 1-284 33ff0e98, Addendum 1
  l. 285-320 da20a307, Addendum 2 l. 321-549 f17a2708, Addendum 3 l. 550-633 e643672d). REFEREE's first table (§0, stage 1), row by row as
  the report prints it: Lemma MEMBER (§4) = Theorem EXP-IDEAL (a) → **SIGN** with E-3 [unconditional (R104's definitions only); E-3: §3's
  rank key is not injective on wire options for k ≥ 4; the generator's tie rule must be in rule R] (l. 13); Lemma MOVE-2 (§5) → **SIGN**, no
  gap [unconditional; none] (l. 14); V0-V4, K1-K4 (§5) → **SIGN** with E-4 [unconditional; E-4: the standing assumption must include «u_0 at
  option 0» (K1's C_0, V1's E_0)] (l. 15); Lemma WIRE (§5) → **SIGN**, no gap [unconditional; none] (l. 16); RESPONSE LEMMA (§6) → **NOT
  SIGNED AS WRITTEN; SIGNED in the form LEMMA′ of §5.3 below** [unconditional; E-1: (H2) is vacuous when the run has stopped and the lemma
  is then false (instance, every k); E-2: the induction applies the lemma for j + 1 before its (H2) is known. One restatement repairs both;
  every line of the packet's case analysis is correct and is the proof of LEMMA′] (l. 17); STABLE (§6) → **SIGN** with E-5 [unconditional;
  E-5: «its input is (b, b)» must read the key bit under s′ (as written it contradicts step t of the RESPONSE LEMMA)] (l. 18); Theorem
  EXP-IDEAL (b), (c) (§7) → **SIGN** (through LEMMA′) [unconditional: a statement about R104's IDEAL model; proof to cite LEMMA′ (E-1, E-2)]
  (l. 19); Corollary EXP-N5 (§2, §7) → **SIGN AS CONDITIONAL** [conditional on R117's premises as landed; P-1 (this lane's pre-check): the
  statement must carry R117's premises in R117's words] (l. 20); Dead end wording (§2) → **SIGN AS CONDITIONAL**, with P-1 and E-7
  [conditional on R117's premises (and R57 (b) for «CORRECT»); P-1; E-7: «N5 is CORRECT on these games» is DATA for k ≤ 11 and landed R57
  (b) for every k] (l. 21); §8 (where the start and the orders are used) → **CHECKED**, correct [a statement about the proof; none (O-2: a
  weaker rank condition suffices)] (l. 22); §9 DATA → reproduced on own tools: model side §3-§5, §8; N5 side §7 (same games as the lane's,
  vertex by vertex) [measured; E-6: §9.7 holds the unfilled placeholder `QUOTESUMMARY`] (l. 23); Quotes → 27 of 27 verbatim by own script; 4
  untagged citations verbatim [—; N-1] (l. 24); then «No statement is REFUSED. Nothing found changes L(G_k) = 2^k − 2, the counts of (c), or
  the Corollary's numbers.» (l. 25). After the fixes, REFEREE's table of what its signature covers (§13.0, stage 5a), row by row: Theorem
  EXP-IDEAL (a), (b), (c), with MEMBER, MOVE-2, V0-V4, K1-K4, WIRE (packet §2-§7; rule R read as entry 5.1; standing assumption entry 4.1
  (S1); §7 read as entry 4.6) → **SIGNED** (§0, §12) [unconditional: R104's definitions only] (l. 584); RESPONSE LEMMA = LEMMA′, with
  CAUSAL; STABLE in step form (entry 4 (4.2-4.5) = this report §5.3) → **SIGNED** (§12; referee-originated, L41: it also needs REFEREE-2's
  independent signature) [unconditional] (l. 585); «IDEAL-ACYC-POLY is false» (entry 2 (a′), its sentences on R104's model) → **SIGNED**
  [unconditional ((a)-(c) put into R104's definition of L)] (l. 586); Corollary EXP-N5 (at least 2^k − 1 iterations) (packet §2, §7 with
  entry 2 (b)) → **SIGNED as PROVED-CONDITIONAL** on RESULTS R117's Theorem REACH3 as landed [conditional: R117's standing premises, in
  R117's words] (l. 587); Corollary EXP-N5′ (exactly 2^k + 1 iterations, exactly one fallback, at iteration 2^k − 1) (entry 3) → **SIGNED as
  PROVED-CONDITIONAL** on RESULTS R124 (EXACT-L, ENDGAME-3-N5) and R117 (f) as landed [conditional: R117's premises and R124's own] (l.
  588); Dead-end paragraph (packet l. 61-71 read as entry 2 (c), (e)) → **SIGNED AS CONDITIONAL** on R117's premises, «for N5 from S3»; its
  arithmetic is unconditional; «CORRECT» is RESULTS R57 (b) for every k (under 1E-N3) and DATA for k ≤ 13 [conditional] (l. 589); DATA
  (packet §9; entries 1, 4.7, 5, 6) → MEASURED [premise-free; N5 itself: k ≤ 12 on two engines of the lane, k = 13 on one] (l. 590); its
  signature line: «**P-N5-EXP: SIGNED with fixes entries 1-6.** What the signature covers, by kind» (l. 580). REFEREE-2's table (§0 of its
  report), row by row: Theorem EXP-IDEAL (a) = Lemma MEMBER (§4) → **SIGN** [M-1 (the rank clause of rule R needs its tie-break in the
  text)] (l. 21); Lemma MOVE-2 (§5) → **SIGN** [—] (l. 22); V0, V1, V2, V3, V4 (§5) → **SIGN** [—] (l. 23); K1, K2, K3, K4, WIRE (§5) →
  **SIGN** [—] (l. 24); RESPONSE LEMMA (§6) → **SIGN the statement**; its proof has gap G-1, closed in §2.4 of this report by the PREFIX
  form [G-1, W-1] (l. 25); STABLE (§6) → **SIGN** [—] (l. 26); Theorem EXP-IDEAL (b), (c) (§7) → **SIGN** (through the RESPONSE LEMMA with
  G-1 closed) [G-1] (l. 27); Corollary EXP-N5 (§2, §7) → **SIGN as PROVED-CONDITIONAL on RESULTS R117, Theorem REACH3, as landed**
  (refereed-only, with R117's standing premises); the sizes n = 135k − 230 and m = 176k − 300 SIGN outright [W-2] (l. 28); «Dead end»
  paragraph (§2) → follows from the Corollary, so it carries the same condition; the wording must say so [W-2] (l. 29); §8 (where the start
  and the orders are used) → checked against the proofs of K1-K4 and V1-V4: every order listed is used where §8 says. The sentence «Nothing
  else … is free» was tested only as far as §3.1 goes (gate renumbering, the rank tie-break) [—] (l. 30); §9 DATA → reproduced on my own
  code, §3 (same numbers at every point I ran) [D-1] (l. 31); §10 → NOT run as written (the lane's script and archives); CHECKER's
  exact-commit re-run covers it [—] (l. 32); §11 → READING, not signed [—] (l. 33); then «No error was found in the mathematics. No
  counter-instance, no failing counter. The two listed items change no number.» (l. 35). Its table on the fixes file (Addendum 2, §A2.0),
  row by row: 1 (extra DATA, pointer correction, §10 erratum) (Addendum 1 A1.2) → **closed** for the runner A1.2 named: run_b6b.sh at
  24f4d436 takes a relative root and exits 1 when a stage fails (tests T1-T3, §A2.5). No statement, proof or hypothesis changes. New item
  F-4 (the NEW runner) (l. 337); 2 (unconditional / conditional / measured) (W-2, §4) → **closed**: (b) and (c) carry «PROVED-CONDITIONAL on
  RESULTS R117's Theorem REACH3 AS LANDED [refereed-only]» with R117's standing premises quoted from its title line; the dead-end sentences
  are to be read through R117's Theorem REACH3, and the NO is for N5 from S3 only. Note F-5 (l. 338); 3 (Corollary EXP-N5′) (Addendum 1
  A1.1) → **closed**: the exact count is a SEPARATE labelled corollary under R124 EXACT-L (premise R117 (f), SPEC's FIX 1-4 tie-breaks); the
  frozen lower bound through R117 alone is kept (l. 339); 4 (LEMMA′, CAUSAL, STABLE in step form) (G-1 (and W-1 in (S2))) → G-1 **closed**.
  L41: **I SIGN** 4.1 (S1)-(S4), 4.2, 4.3, 4.4 and the proofs 4.2, 4.3, 4.5, 4.6 as printed, with the reading F-1; the concordance claim
  «PREFIX FORM = LEMMA′ at τ_0 = T» is **correct** (§A2.4). Wording F-1, F-2 (l. 340); 5 (wording and records) (M-1, W-1, D-1) → **closed**
  (5.1, 5.2, 5.3); wording F-3. 5.4-5.9 answer other referees' items: read; where they quote this lane's report the quotes are verbatim;
  nothing in them contradicts it (l. 341); frozen guard (—) → **holds**: the packet's sha1 is c0449b17193f19619f33b366096762dfde27d542 at
  350d84eb and at 24f4d436; the fixes file at 06d399c2 (entry 1; sha1 4c692ab2…, 12,551 B) is a byte prefix of the file at 24f4d436 (`cmp -n
  12551`) (l. 342); its signature: «**P-N5-EXP: SIGNED with fixes entries 1-5.** The signature is §0's, with one correction (§A2.1): the
  statement of the RESPONSE LEMMA that I sign is entry 4's 4.4 (LEMMA′), not the frozen l. 192-204; STABLE is signed in 4.2's step form.
  Every other row of §0 stands as written. Items F-1 to F-5 are wording and tooling; none of them is a condition of the signature except the
  reading F-1.» (l. 344-346). REFEREE-2 on the two reviews together (Addendum 3): «No verdict differs after the fixes, and no number differs
  anywhere» (l. 582). No statement is REFUSED by either referee. The frozen statement of the RESPONSE LEMMA is signed by neither: both sign
  it in the restated form LEMMA′ of fixes entry 4 (L41, below). The joint gap map is in the Note bullet: every required item is closed by a
  fixes entry that the referee who raised it has checked, except what the open slots name (Signatures).
- Setting and scope, as both referees sign it. The objects are R104's IDEAL model on the genomes G_k (k ≥ 3), the games Γ3(G_k) of RESULTS
  R117, and N5 (SPEC S1-S5 with FIX 1-4) from its default start S3. Statements as signed (the packet with fixes entries 1-5 for both
  referees, entry 6 for REFEREE), by standing:
  (a) UNCONDITIONAL (R104's definitions only; no theorem, no SPEC premise, nothing about N5). Theorem EXP-IDEAL (a) = Lemma MEMBER: G_k is a
    genome of R104's class in IDEAL-ACYC with N = 9k − 16 movers, M = 18k − 32 options and k + 1 levels, the rank clause read with its
    tie-break by β-id (fixes 5.1). MOVE-2, V0-V4, K1-K4, WIRE under the standing assumption of fixes 4.1 (S1), every wire and u_0 at option
    0. The RESPONSE LEMMA as LEMMA′ (fixes 4.4) with CAUSAL (4.3) and STABLE in step form (4.2). Theorem EXP-IDEAL (b): L(G_k) = 2^k − 2 and
    the run stops «stuck»; (c): every mover of unit j changes its option exactly 2^(j−1) times, v_0 once, u_0 and the wires never,
    11·2^(k−2) − 9 changes in all. REFEREE «(1) Theorem EXP-IDEAL (a)-(c) SIGNED (unconditional), (b), (c) through LEMMA′» (l. 392) (l. 584;
    l. 585); REFEREE-2 «UNCONDITIONAL (mathematics about R104's DEFINITIONS, no theorem used): Theorem EXP-IDEAL (a), (b), (c) with its
    lemmas.» (l. 239) (l. 27; l. 464).
  (b) UNCONDITIONAL consequence inside the model: the statement that R104's packet names IDEAL-ACYC-POLY («Let IDEAL-ACYC-POLY mean: there
    is a polynomial q such that L(G) ≤ q(N + M) for every G ∈ IDEAL-ACYC.» (l. 224); docs/red/P-N5-REALIZE.md at trunk) is FALSE, already
    for genomes of degree 2: L(G_k) = 2^k − 2 against N + M = 27k − 48. REFEREE l. 586; REFEREE-2 «That IDEAL-ACYC-POLY is false follows
    from Theorem EXP-IDEAL (b) alone (L(G_k) = 2^k − 2 against N + M = 27k − 48): unconditional.» (l. 368-369). Not carried by the line and
    not part of this entry: the second sentence of fixes entry 2 (a′), on L-NEW's lane packet P-N5-KEY1P (Not signed, below).
  (c) PROVED-CONDITIONAL on RESULTS R117's Theorem REACH3 as landed [refereed-only], with R117's standing premises (Premise, below).
    Corollary EXP-N5: Γ3(G_k) has n = 135k − 230 vertices and m = 176k − 300 edges, and the N5 run of Γ3(G_k) from S3 has one FL run of
    length exactly 2^k − 2 and makes at least 2^k − 1 iterations; so no polynomial in n or in n + m = 311k − 530 bounds the number of
    iterations of N5 from S3. The dead-end sentence, as fixes entry 2 (c) reads it: through R117, N5 from S3 does not run in polynomial
    time, cannot pass gauntlet step 4, and G-N5-TIME is answered NO for N5 from S3. REFEREE l. 587 and l. 589; REFEREE-2 «PROVED-CONDITIONAL
    on RESULTS R117 as landed: Corollary EXP-N5's iteration bound, and with it the Dead-end paragraph» (l. 241); the sizes n and m are
    unconditional (REFEREE-2 signs them outright, its row l. 28).
  (d) PROVED-CONDITIONAL on RESULTS R124's Corollary EXACT-L and Theorem ENDGAME-3-N5 as landed [refereed-only] (premise R117 (f) = Theorem
    REACH3, so the premises of (c), with R124's own). Corollary EXP-N5′ (fixes entry 3): N5 from S3 on Γ3(G_k) makes exactly 2^k + 1
    iterations, with exactly one fallback, at iteration 2^k − 1. An addition: the dead end needs (c) only. REFEREE: statement «entry 3's
    **Corollary EXP-N5′, the STATEMENT, is SIGNED AS PROVED-CONDITIONAL on RESULTS R124 and R117 as landed**» (l. 537-538), statement and
    proof «I SIGN the corollary as PROVED-CONDITIONAL on RESULTS R124 (Corollary EXACT-L, Theorem ENDGAME-3-N5) and RESULTS R117 (f) as
    landed» (l. 570-571); REFEREE-2 «Status of the exact form: PROVED-CONDITIONAL on R124 and R117 as landed; no new premise beyond those
    two entries.» (l. 304) and, on entry 3, «**Addendum 1 A1.1 → entry 3: closed.**» (l. 375).
  (e) MEASURED (DATA, premise-free): the runs of the model and of N5 itself (Data, below). They test every step of the proof and the
    predictions of R117 and R124; they kill nothing by themselves (L43, below).
- Premise (landed RESULTS entries only; heading lines at trunk aeb90ac1 by script; none is later than R130). For (a), (b): RESULTS R104 (l.
  9864), DEFINITIONS ONLY (the genome, IDEAL-ACYC, the X-chain order, the IDEAL step, L(G)): packet «**R104, DEFINITIONS ONLY** (no theorem
  of R104 is used).» (l. 15); REFEREE «So «DEFINITIONS ONLY (no theorem of R104 is used)» is right; MEMBER c8 (acyclic) comes first and
  makes the X-chains finite. No circularity.» (l. 53-54). For (c): RESULTS R117 (l. 13362), Theorem REACH3 as landed, with its standing
  premises in R117's own words, its title line: «with R104's premises as landed (1E-N3 = RESULTS R57 (b) in its two forms; RESULTS R24 (a)
  Lemma R and R24 (b)'s choice rule with RESULTS R103's bridge B and (R1) ruling; RESULTS R36 (c) Lemma P1 on the dual game) and RESULTS R15
  (d) for termination only» (RESULTS l. 13362); these are 1E-N3 = RESULTS R57 (l. 2893) (b), RESULTS R24 (l. 1064) (a) and (b) with RESULTS
  R103 (l. 9641)'s bridge B, RESULTS R36 (l. 1717) (c) and RESULTS R15 (l. 624) (d), each a landed [refereed-only] entry; in R117's entry
  they are called [1E-N3], [RULE], [VJ-LOC], [TERM], and «Premises [1E-N3], [RULE], [VJ-LOC] as landed in R104: the correctness of S1's
  procedure stays SPEC's requirement, and the code's match to SPEC is DATA (R57 (b))» (l. 13543-13544). REACH3's one hypothesis on the
  genome is «for every G with an ACYCLIC Ξ-graph», met by Lemma MEMBER; its clause used is «so if L(G) ≥ 1, [0, L(G)] is one FL run of
  length exactly L(G) and the run makes at least L(G) + 1 iterations» (both in RESULTS l. 13362). For (d): RESULTS R124 (l. 15371), as
  landed, its title line: «premise RESULTS R117 (f); it uses SPEC's S1 tie-breaks, through REACH3's [RULE] choice: with another
  pointwise-optimal S4a choice the identity can fail» and «premises, all under the standing SPEC premise 1E-N3 of RESULTS R57 / R104 /
  R117». For the correctness sentence: RESULTS R57 (l. 2893) (b), Lemma OUT-G: «In particular, on every game N5 stops (R15 (d)) and SPEC
  S5's output there is correct. Standing premise, as in R51 (d): OUT-G concerns SPEC's Ξσ and σ̄; that S1's procedure realises an optimal σ̄
  is VJ00 §6 plus SPEC conformance, and the code's match to SPEC is DATA (R15 G-N5T-1) (1E-N3 = N-1E-1).» (l. 2914-2916). The premise 1E-N3
  is SPEC's standing requirement, not a theorem of the fleet: REFEREE «1E-N3 is the standing SPEC premise of every landed N5 result since
  R57» (l. 61). Not used: «NOT used: R105, R113, R120.» (l. 41); no theorem of R104; nothing of R125-R130. L-SI's box 108 is supporting
  evidence, not a premise (Referee strengthening).
- L41 and L43. The packet's proofs are L-RED-B successor 5's, with one referee-originated restatement: CAUSAL and LEMMA′ (and the standing
  paragraph and STABLE's step form) are REFEREE 36's (its §5.3, from l. 199, in stage 1), adopted word for word in fixes entry 4. Under L41
  («A proof written by one referee counts toward "two referees signed it with its gaps listed" (CLAUDE.md) when the author referee signs it
  in its report and the OTHER referee independently checks and signs it» (l. 356-357)) the author signs and the other referee signs
  independently: REFEREE «**NOT SIGNED AS WRITTEN; SIGNED in the form LEMMA′ of §5.3 below**» (l. 17), and after the fixes entry «**Verdict
  on entry 4: it closes E-1, E-2, E-4, E-5. RESPONSE LEMMA SIGNED as restated in fixes entry 4 (= LEMMA′ of §5.3 with CAUSAL and STABLE in
  step form).**» (l. 522-523); REFEREE-2 «**REFEREE-2 signs 4.1 (S1)-(S4), 4.2 STABLE, 4.3 CAUSAL, 4.4 LEMMA′ with their proofs (4.2, 4.3,
  4.5) and 4.6, as printed in docs/red-b/P-N5-EXP-fixes.md at claude/l-red-b 24f4d436 (sha1 9dc9179f…), (R3)'s range read as t − 1 ≤ τ <
  last (F-1).**» (l. 464-465), on the same text: «So the text I signed in §A2.3 IS the referee-originated text, and L41's two signatures are
  on the same statements» (l. 564-565) (REFEREE's own script: «fixes4: my §5.3 inside entry 4, white space normalised, the bold labels
  dropped: standing paragraph 1, CAUSAL 1, LEMMA′ 1 (1 = verbatim)» (l. 507)). The one condition of the second signature is the reading F-1
  of clause (R3), which the lane takes over in fixes 7.1; its confirmation by the statement's author is part of the open slot of REFEREE
  (Signatures). The line names both signatures in its scope tail. L43 (««DEAD» in a landing line needs a refereed proof, or one instance
  exceeding an EXPLICIT bound» (l. 371-372)): the DEAD rests on a PROOF, not on an instance: REFEREE «L43 («DEAD» needs a refereed proof or
  an instance beyond an explicit bound): the growth is PROVED for every k ≥ 3 (Theorem EXP-IDEAL (b), unconditional; this report signs it
  through LEMMA′); the DEAD of «N5 runs in polynomial time» then holds under R117's premises.» (l. 26-27); REFEREE-2 «They are far below
  every explicit polynomial bound (2^k − 1 < n² until k = 23, where a run would take 8.4 million iterations on 2,875 vertices): no measured
  instance «beyond an explicit bound» exists or is in reach of these engines. The kill rests on the proof.» (l. 247-249). By script from the
  pinned outputs: every measured run lies below n², n the number of vertices of Γ3(G_k): N5 itself for k = 3..13 (the largest, k = 13: 8,193
  iterations on n = 1,525, n² = 2,325,625) and the model alone to k = 20 (L-COMP 22: T = 1,048,574, where Γ3(G_20) would have n = 2,470, n²
  = 6,100,900); 2^k − 1 exceeds n² first at k = 23 (n = 2,875: 8,388,607 > 8,265,625), n³ at k = 37, n⁴ at k = 51, by exact integer
  arithmetic, not run. So the dead end rests on the proved growth (Theorem EXP-IDEAL for every k, put into R117), not on a measured
  instance, and every DATA clause below names its counter and unit.
- Not signed: the packet's §9 numbers as statements (DATA), §10 (reproduction; REFEREE-2 «NOT run as written (the lane's script and
  archives); CHECKER's exact-commit re-run covers it» (l. 32); REFEREE «the lane's run_b6b.sh and its simulators / engines (onep, one217,
  r187, n5v, n5b) were not run: my tools replace them» (l. 40-41)) and §11 (READING); the ablation rows of §9.6 («this variant is NOT
  covered by the proof» (l. 527)); the second sentence of fixes entry 2 (a′), that QUIET-KEY-1P and SW-POLY of L-NEW's lane packet
  P-N5-KEY1P are false, which holds only through that packet's Lemma IDEAL-1P, a lane lemma that is not landed (REFEREE-2 «A RESULTS line
  may carry the first sentence as unconditional and not the second; line L-1 does exactly that.» (l. 373-374); REFEREE «The sentence of
  entry 2 (a′) on L-NEW's packet (QUIET-KEY-1P and SW-POLY are false) is right as worded: it holds THROUGH L-NEW's Lemma IDEAL-1P (T_key(G)
  = L(G); packet P-N5-KEY1P, a frozen lane packet, signed by this lane in R-P-N5-KEY1P.md §2; not a landed result) and is not a statement of
  this packet.» (l. 591-593)); L-SI's box 108 as a result; R117's and R124's own proofs, which are landed and were not re-refereed here
  (REFEREE «R117's proofs were not re-refereed here (landed; successor 35 read them against G_k's features, §7)» (l. 40)); anything outside
  the packet's «**Not claimed.** Nothing about N5 from other start pairs; nothing about other tie rules (N5′-xi makes 7 iterations on
  Γ3(G_4) and Γ3(G_6), §9.4) or about Howard / switch-best (3 or 4 steps on the model); nothing about any other candidate or about parity
  games in general» (l. 72-74).
- Referee strengthening and supporting evidence (NOT part of this entry). (i) REFEREE 35's pre-check (docs/referee/R-GK-precheck.md at
  claude/referee 06ac891d, 2026-11-13T13:48:04Z; not a signature; written from the rule as relayed, without the packet): «no hypothesis of
  R104's class or of R117's proofs is violated by G_k» (l. 369). (ii) An INDEPENDENT proof of L(G_k) = 2^k − 2: L-SI successor 56's box 108
  (docs/si/box108-gk-proof.md, claude/l-si 8c062914, sha1 31b7c78c9b4941f083b86beb0e0fa513049dce22, 461 lines; «Labels: PROVED (L-SI lane,
  unrefereed) / DATA (counter, unit, set, scope) / OPEN.» (l. 7); «INDEPENDENCE: written from the Lead's rule (§1.2) and R104's definition
  (§1.1) only.» (l. 14)), by a closed form of the run and a 32-row table, with no response lemma. It was compared with the packet by REFEREE
  (stage 3: «Result of stage 3: no conflict between the two proofs; the verdicts of §0 stand.» (l. 496); «NOT refereed here: it is not my
  packet; its STEP table (32 transition classes) was not checked row by row.» (l. 465)) and checked by REFEREE-2 only
  (docs/referee-2/R2-box108.md at claude/referee-2 e643672d: «It is ONE referee's check of a lane proof. It is not a second signature on box
  108» (l. 13); «No gap was found in Lemma STEP or in Lemma MOVE. Three wording items (§1), none of them changes a statement.» (l. 43)). So
  it has ONE referee's check and is not a two-referee result: supporting evidence for (a), not a premise of anything here. (iii) Each
  referee rebuilt the family and re-ran the model and N5 with its own code (DATA counters for the cited replays, below); REFEREE stage 2
  also checked a unit against arbitrary delays of the unit above (its §10.2) and stage 5a compared the k = 13 game with its own builder's
  («pg13: G_13 pgonly N 101 M 202 n 1525 m 1988 maxprio 817 L 8190 PG 0 GEN35 0» (l. 712)).
- Honest limits: (i) Everything said about N5 is conditional: (c) on RESULTS R117 as landed and (d) on RESULTS R124 as landed, both
  [refereed-only], under the standing SPEC premise 1E-N3, which is not proved in the fleet; only (a) and (b), statements about R104's IDEAL
  model, are unconditional. (ii) It is a dead end for ONE candidate with ONE tie rule from ONE start: N5 (SPEC S1-S5 with FIX 1-4, S4a's
  root-first key rule) from its default start S3. Nothing is claimed about other start pairs, other tie rules (N5′-xi stops after 7
  iterations on Γ3(G_4) and Γ3(G_6): DATA), Howard's rule (at most 4 steps on the model: DATA), any other candidate, or parity games in
  general. (iii) No measured run lies beyond an explicit polynomial bound of degree 2 or more (L43, above): the largest N5 run has 8,193
  iterations, above n + m = 3,513 and below n² = 2,325,625. (iv) N5's ANSWER on these games is right: RESULTS R57 (l. 2893) (b), Lemma
  OUT-G, for every k (under 1E-N3), and DATA for the k that were run (winners equal to Zielonka's for k ≤ 12 on two engines and at k = 13 on
  one); what fails is the polynomial bound, not the answer. (v) The growth is exponential in k and n = 135k − 230, so the bound is «at least
  2^k − 1 = 2^((n + 230)/135) − 1 iterations»: a small base, a true exponential in n. (vi) The lane's tools were written by the lane; at k =
  13 one engine ran, not two. (vii) No Lean. (viii) No algorithm and no bound is claimed, and no novelty against the literature (not M3).
- Data (DATA, not proof; every clause names its counter and unit, L43): experiments/red-b/ at claude/l-red-b 10dfedb6, outputs in
  data/b6b/out/, pinned in 6 pin files (SHA1SUMS_b6b, SHA1SUMS_b6b_fixes1, SHA1SUMS_b6b_fixes2, SHA1SUMS_b6b_fixes3, SHA1SUMS_b6b_fixes4,
  SHA1SUMS_b6b_fixes5; 94 files, 0 sha1 mismatches against the git objects, by script) and checked by experiments/red-b/check.sh. Numbers
  below are read by script from the pinned outputs (tools/data.py, 32 checks). Membership (unit: one genome): R104's eight clauses, must-0
  counters c1-c8 and their sum viol, 0 on G_3..G_14 (member.out); 8 damaged copies of G_5 fire (member_ctrl.out). The IDEAL run (unit: one
  genome): must-0 counter ideq (three simulators, state by state) 0 and T = 2^k − 2 for k = 3..14 (sim.out). The proof's facts on the run
  (lemma.out, k = 3..14): must-0 counters kfact, vfact (unit: a (state, comparison) pair), sched (unit: a step), tlen, rest (unit: a
  genome), swk (unit: a mover) all 0; two controls fire (sched 19, kfact 25). LEMMA′, CAUSAL, STABLE of fixes entry 4 (b6prefix.py,
  prefix_*.out): must-0 counters h1, h2, psched, empty at 16,368 response windows and 376,836 (window, step) pairs of the runs for k =
  3..14; aviol 0 on 163,970 triples (j, a, t) for k = 3..12, where the windows are exactly the recursion's 2^(k−1) − 1; pviol 0 off the run
  (42,902 windows, 1,089 of them proper prefixes); dviol 0 on 28,000 driven windows (16,423 proper); loc 0 (CAUSAL as a function) on 81,000
  states and stviol 0 on 14,698 cases; c0e0, loc, stviol, pviol 0 on EVERY state of G_3 (512) and G_4 (65,536) with the wires and u_0 at
  option 0; the lemma as frozen, as a control, fails at exactly k − 1 triples per k (k = 3..8). Clause (R3) as read in fixes 7.1 (e7_r3.out,
  unit: a response window): r3in, r3move, r3rest 0 at 16,368 windows for k = 3..14. N5 itself (unit: one game Γ3(G_k); must-0 counters mism,
  wrong, nonmover, gdiff, and with two engines wrong2, engdiff): k = 3..11 (n5.out) and k = 12 (n5_k12.out) on two engines and two Γ3
  builders, iterations 9, …, 2,049, 4,097 = 2^k + 1 on n = 175, …, 1,255, 1,390 vertices, one fallback each; k = 13 on engine 1 only
  (n5_k13.out): 8,193 iterations on n = 1,525, one fallback after 8,190 S4a iterations. Sizes (size.out, size_k13.out): must-0 counter
  sizediff, n = 135k − 230 and m = 176k − 300 on the game files, k = 3..11 and 13. Strategies (TARGET.md §5, D2 change 5): must-0 counter
  badstrat (harness verifier) 0 for k = 3..10. Also 0: venab, kenab, movd (enab.out, k = 3..12), keep on 7,050 gate relabelings (perm.out),
  startdiff, padcyc, padp, fbpos (reach.out, R117's side lemmas on these games, k = 3..8). Frozen instances: data/b6b/pg/G_k_g3.pg, k =
  3..11 at 350d84eb (smallest: 175 vertices, 228 edges, 9 iterations), and k = 12, 13 from fixes entries 1 and 6; genomes of record
  data/b6b/G/G_k.json, k = 3..14. Re-run by the drafter in a git archive of 10dfedb6: experiments/red-b/check.sh exit 0, «red-b check PASS»;
  with one byte appended to the pinned n5_k13.out it prints «red-b: data/b6b fixes3 SHA1SUMS mismatch» and «red-b check FAILED» (negative
  control; restored).
- DATA counters for the replays the line cites, named here from their own reports (L43; cited, not re-run). L-COMP 22 BOX 48
  (experiments/comp/box48/README.md at claude/l-comp dc6d831f): the model, «C port: T_key = 2^k − 2 exactly for k = 3..20 (1,048,574 at k =
  20, N + M 492)» (l. 23); N5, «N5 on Γ3(G_k), k = 3..12 (n = 135k − 230 = 175 … 1,390): n5b spec 2^k + 1 iterations, 1 fallback; n5v spec
  the same (engdiff 0), first fallback at step 2^k − 2; wrong 0, verr 0; controls fire» (l. 25); the winners, «Oink --tl and --zlk:
  verified, winners = n5b's (owrong 0) for k = 3..12; control fires» (l. 26); its own reading: «Whether this is a kill of N5 rests on the
  referees' reading of R117 and of the family's general-k proof (L-RED-B's P-N5-EXP), not on this box.» (l. 34-35). L-RED 70 R245
  (docs/red/R245-kill-Gk.md at claude/l-red c7ed9b8b): «All rows as claimed (script line «ALL ROWS AS CLAIMED»): FL run 2^k − 2, first
  fallback at 2^k − 1, 2^k + 1 iterations, one fallback, every counter 0» (l. 42); its limit: «**What this file does NOT establish: T_key =
  2^k − 2 for every k (data to k = 12; the induction proof is owed elsewhere); N5 beyond k = 8; an independent Γ3 builder.**» (l. 6); it
  also carries N5 at k = 9 and k = 10 in two addenda (the line names k = 3 … 8 only). REFEREE 35's pre-check (06ac891d): «every k run (§4's
  table: k = 3..9 and the long runs listed there): 2^k + 1 iterations, exactly one fallback, at transition 2^k − 1; states 0..L are the
  standard states of the IDEAL run; every winner equals Zielonka's; 7 named counters 0; firing control for STD and FLFB» (l. 16). REFEREE 36
  (stage 1): the model «run: k 3..14; L 6 14 30 62 126 254 510 1022 2046 4094 8190 16382; Lform 0 stopform 0 swk 0 maxform 0 sumform 0
  nochange 0» (l. 267); N5 «n5: G_3 G_4 G_5 G_6 G_7 G_8 G_9; iterations 9 17 33 65 129 257 513; S3START 0 STD 0 FLFB 0 FLTAU 0 FLSIG 0
  LASTFB 0 WIN 0 EXACT 0 PG 0; PG compared on 7 games» (l. 301). REFEREE-2 41 (its §3.2-§3.4): counters tfail, stopfail, swfail, totfail 0
  for k = 3..16 and idfail 0 for k ≤ 12; N5 on its own engine with four solvers (its counters red, zl, zh, oink-zlk, oink-tl, lane, all 0
  for k = 3..11): «So on k = 3..11: the first fallback is transition 2^k − 1 (as REACH3 says: L(G) + 1), N5 makes 2^k + 1 iterations, and
  its answer is right.» (l. 206-207).
- Note (every item of both referees and of the pre-check, and how each was closed). REFEREE 36's items (its §9 table, l. 377 to 387): E-1
  ((H2) vacuous after the stop; the frozen lemma false at (j, a, t) = (1, 1, 2^k − 1)), E-2 (the induction uses the lemma for j + 1 before
  its hypothesis holds), E-4 (the standing assumption needs u_0 at option 0), E-5 (STABLE: key bit of the step) → fixes entry 4; REFEREE
  stage 4: «**E-1 CLOSED.**», «**E-2 CLOSED.**», «**E-4 CLOSED.**», «**E-5 CLOSED.**» (l. 510 to 520). E-3 (rank key not injective on wire
  options; tie rule by β-id) → 5.1, E-6 (the placeholder of §9.7) → 5.3, E-7 («CORRECT»: DATA or R57 (b)) and P-1 (R117's premises in the
  Corollary and the dead-end sentence) → entry 2, O-1 (optional: R124 for the exact count) → entry 3; REFEREE stage 5a: «**E-3 closed.**»,
  «**E-6 closed.**», «**P-1 closed.**», «**E-7 closed.**», «**O-1 closed.**» (l. 631 to 688). O-2 and N-1 (notes) → recorded in 5.9, no
  change. Stage 5a's own notes N-5a (a line range in fixes entry 2 (d) off by one), N-5b (the parenthesis of 5.1; the same point as
  REFEREE-2's F-3, read in fixes 7.3), N-5c (a count of quotes), N-5d (a remark on Remark 2): «### 13.7 Notes (no statement affected; the
  lane may take them into a later entry)» (l. 764). The pre-check's items (REFEREE 35): P-1 as above; P-2 (level width) → 5.4, M-1 (genome
  of record and raw files) → 5.5, M-2 (mover order) → 5.6, M-3 (JSON fields) → 5.7 («the pre-check items P-2, M-1, M-2, M-3 are answered
  with the right numbers» (l. 574)); P-3 (scope of a kill: N5 as specified) and P-4 (L43: the proof for every k) are met by the packet's
  «Not claimed» and by Theorem EXP-IDEAL. REFEREE-2's items: G-1 (= E-2) → entry 4, «G-1 **closed**.» (l. 340); M-1 (= E-3) «**M-1 → 5.1:
  closed.**» (l. 381); W-1 («step t») «**W-1 → 5.2 and 4.1 (S2): closed.**» (l. 386); W-2 (= P-1) «**W-2 and §4 → entry 2: closed.**» (l.
  361); D-1 (= E-6) «**D-1 → 5.3: closed.**» (l. 387); O-1 (its own Γ3 builder numbers the β block in gate order: about its tool, not the
  packet); Addendum 1 A1.1 (the exact count) → entry 3 and A1.2 (the runner erratum) «**Addendum 1 A1.2 → entry 1, 10.E: closed**» (l. 392);
  its self-correction §A2.1 («That row was wrong about the STATEMENT.» (l. 349)). Its items on the fixes file, F-1 (a reading: (R3)'s range,
  the one condition of its signature), F-2 and F-3 (wording), F-4 (the new runner exits 0 on a failing stage; «No DATA is affected» (l.
  397-398)), F-5 (a label inside (a′); no change asked) → fixes entry 7 (7.1-7.5), which neither referee has checked yet. Its line notes
  L-a, L-b, L-c on L-1 → line L-2 (fixes 7.6). Agreement of the two reviews (REFEREE-2 Addendum 3): «the same gap (E-2 = G-1) and the same
  rank tie (E-3 = M-1), placeholder (E-6 = D-1) and condition (P-1 = W-2) were found independently; E-1, E-4, E-5, E-7 are REFEREE 36's
  alone» (l. 629-631); on what was open between them: «Nothing that touches a statement.» (l. 623). Its three wording items S-1, S-2, S-3
  concern box 108, which is not part of this entry.
- Signatures: REFEREE docs/referee/R-P-N5-EXP.md at claude/referee 9ec40ff9 (784 lines, sha1 d5017ab5f382685cb9941273b893c31b2174c8a2):
  successor 36 wrote stages 1-4, successor 37 stage 5a: stage 1 l. 1-397 (c881709b 2026-11-13T14:57:16Z), stage 2 l. 398-456 (ea09ae2e
  2026-11-13T15:41:26Z), stage 3 l. 457-496 (7ca9c2b4 2026-11-13T15:44:37Z), stage 4 l. 497-536 (577e8df9 2026-11-13T17:17:17Z), stage 4
  addendum l. 537-542 (4cf6e1ff 2026-11-13T17:28:19Z), stage 5a l. 543-784 (31b28f2a 2026-11-13T19:16:17Z); the pre-check
  docs/referee/R-GK-precheck.md is successor 35's (06ac891d; not a signature). Its signature, the last line of the file: «**P-N5-EXP: SIGNED
  with fixes entries 1-6.**» (l. 784); on the restated lemma «**SIGNED** (§12; referee-originated, L41: it also needs REFEREE-2's
  independent signature)» (l. 585). REFEREE stage 5b PENDING (its §14: the line of record word by word, fixes entries 7 to 9, and its final
  signature line naming the line by its sha1; stage 5a ends «Stage 5b (line L-2, entry 7) waits for the commit.» (l. 782)). REFEREE-2
  docs/referee-2/R2-P-N5-EXP.md at claude/referee-2 e643672d (633 lines, sha1 3120251cbf27d2ebfc4749a620b4934b9a639099): successor 41 wrote
  the report and Addendum 1, successor 42 Addenda 2 and 3: report l. 1-284 (33ff0e98 2026-11-13T14:17:17Z), Addendum 1 l. 285-320 (da20a307
  2026-11-13T14:40:07Z), Addendum 2 l. 321-549 (f17a2708 2026-11-13T17:02:13Z), Addendum 3 l. 550-633 (e643672d 2026-11-13T17:27:09Z). Its
  signature: «P-N5-EXP: SIGNED with fixes entries 1-5.» (l. 548), with the L41 signature quoted above (l. 463), and on the first referee's
  text «LEMMA′ and CAUSAL in entry 4 are REFEREE 36's text word for word: L41 is met.» (l. 632). REFEREE-2 line check PENDING (its check of
  the line of record; its signature stands on fixes entries 1-5, and entries 6 to 8 and the lines after L-1 are later than its Addendum 3).
  Lane (claude/l-red-b): L-RED-B successor 5 (350d84eb packet FROZEN; 06d399c2 fixes entry 1), successor 6 (24f4d436 entries 2-5 and line
  L-1; 0c8fdf9e entry 6), successor 7 (b1a93700 entry 7 and line L-2; 10dfedb6 entry 8 and line L-3). CHECKER: C148, the token in the title.
- INDEPENDENCE: each referee wrote its verdict without reading the other's. REFEREE: «Independence: REFEREE-2's reports and L-SI's box 108
  (an independent proof of L(G_k) = 2^k − 2) were NOT read before §0-§9 were committed.» (l. 6-7); stage 4 «NOT read: docs/referee-2/ (the
  strings entry 4 quotes from it were matched by script only)» (l. 499-500); stage 5a «Independence: docs/referee-2/ was NOT read.» (l.
  556). REFEREE-2: «Independence: docs/referee/ and notes/REFEREE.md were NOT read on this object» (l. 9); Addendum 2 «Independence:
  docs/referee/R-P-N5-EXP.md and docs/referee/R-GK-precheck.md were NOT opened before this addendum was committed.» (l. 328); it opened the
  first referee's files only for Addendum 3: «Written after Addendum 2 was committed (f17a2708, 17:02:13Z) and its SHA sent to the Lead
  (17:03Z); only then were the first referee's files opened.» (l. 552-553), and «neither report cites the other» (l. 559). The same gap was
  found twice: «the SAME gap, found independently, with the same repair (LEMMA′ / PREFIX FORM; §A2.4: one lemma)» (l. 589). Disclosed: the
  first referee's lane wrote the pre-check («This lane's pre-check (successor 35, docs/referee/R-GK-precheck.md at 06ac891d) is prior work
  of this lane; it had not read the packet.» (l. 7-8)); the restated lemma is the first referee's own text, signed by its author and,
  independently, by REFEREE-2 (L41, above); when REFEREE-2 signed it, what it knew of the first report was what the fixes file quotes («What
  I know of the first referee's report is what entries 2-5 quote from it (22 tagged quotes; 5 of the pre-check).» (l. 329)). Each referee
  used its own generator, model and N5 engine: REFEREE «the lane's gk.py, onep.py, b6*.py are not imported» (l. 33-34); REFEREE-2 «No lane
  tool was imported by my checkers» (l. 9-10).
- TARGET.md diff: TARGET.md §2 (M4) asks for «There is a deterministic algorithm A and a polynomial p such that for every parity game G, A
  on input G halts within p(n + m) steps and outputs the pair (W_E(G), W_O(G)).» (l. 20-21); this entry claims no algorithm and no bound. It
  records that one candidate, N5 from S3, fails gauntlet step 4, the running-time half (TARGET.md §5: «4. Written correctness and
  running-time proofs, double-refereed with every gap listed.» (l. 45); CLAUDE.md: «Every algorithm claim runs the gauntlet in TARGET.md
  section 5. Failing any step makes it a dead end.» (l. 12)): through R117 as landed, its number of iterations on Γ3(G_k) is at least 2^k −
  1 on an input of n + m = 311k − 530 vertices and edges, and each iteration costs at least one step in TARGET.md §3's cost model («Word RAM
  with words of O(log(n + m)) bits» (l. 24); the packet: «an iteration costs at least one step» (l. 58)), so the bound is a LOWER bound on
  steps and needs no bit-cost argument (REFEREE-2: «it needs no bit-cost argument because it is a LOWER bound on steps» (l. 261)). The games
  are TARGET.md §1 games as they stand (REFEREE: «The Corollary's games are TARGET §1 games as they stand» (l. 44), largest priority 4M + 9
  ≤ n; REFEREE-2: «so no parameter is being held small» (l. 263)). Referees: REFEREE ««Not claimed» matches TARGET §2: the target stays
  open.» (l. 48); REFEREE-2 «No statement of the packet goes beyond TARGET.md.» (l. 263). It is not M3 and not M4 progress, not a TARGET.md
  claim and not a step-4 pass for any candidate: the question of TARGET.md stays open, in the line's words «TARGET.md §2 (M4) stays OPEN;
  not M3 or M4, not a TARGET.md claim».
- Status: DEAD END for the candidate N5 (SPEC S1-S5 with FIX 1-4, from its default start S3) as an M4 candidate: failure of gauntlet step 4
  (running time), PROVED-CONDITIONAL on RESULTS R117 as landed, on the unconditional Theorem EXP-IDEAL. Obstruction RIPPLE, in the line's
  words: «obstruction RIPPLE (S4a's root-first key rule refuses an improving switch until the key order allows it, and on Γ3(G_k) this makes
  unit j + 1 respond twice in every response of unit j)». The instance that kills it is the family Γ3(G_k), k ≥ 3, by the proof (frozen
  files for k = 3..13; the smallest has 175 vertices, 228 edges and 9 iterations); no single measured game exceeds n². GAPS G-N5-TIME is
  answered NO for N5 from S3 (through RESULTS R117 as landed, refereed-only): at landing its row takes this entry's UPDATE, its status
  becomes "closed" and it moves under the Closed table (Lead rulings G-U, G-S). No landed entry is changed: R117 and R124 are used as
  landed. Open slots of this fill, each marked by its word above: REFEREE stage 5b, REFEREE-2's line check, fixes entry 9, the line of
  record L-4; and the checker token in the title.

Proposed GAPS G-N5-TIME UPDATE (append-only), to go AFTER the last UPDATE on the row G-N5-TIME (GAPS l. 11 at trunk aeb90ac1; its last
UPDATE is R130's, «UPDATE 2026-11-13 10:06Z: RESULTS R130 (P-N5-WRAP; CHECKER C146 26e9d73c) [refereed-only] LANDED:» (l. 11)), as a pure
insertion with one separating space before the row's closing pipe. BUILT FROM THE LINE L-3 by tools/upd.py (updlib.build, the landed
procedure made generic: the same function rebuilds the landed UPDATEs of R128, R129, R130 byte for byte from their landed titles; four
negative controls refuse; Addendum [upd]): the three labels «(Theorem EXP-IDEAL, PROVED lane; its RESPONSE LEMMA in the prefix form LEMMA′
of fixes entry 4, with CAUSAL and STABLE in step form)», «(Corollary EXP-N5)», «(Corollary EXP-N5′)» are moved behind their clauses; the
scope words «; not M3 or M4, not a TARGET.md claim» are dropped (the landed drop of R130); the line's final full stop is stripped before the
ending; no pipe pair is needed (the line has no pipe). Lead ruling G-U (docs/agents/LEAD-STATE.md l. 3720): the UPDATE ends with the
sentence «G-N5-TIME is answered NO for N5 from S3 (through RESULTS R117 as landed, refereed-only).». Lead ruling G-S (same log line): «the
status cell of GAPS G-N5-TIME becomes «closed» and the row moves to «## Closed» (check_docs accepts only open / in-progress / closed; the
gap's question is answered NO)»; land131.py therefore sets the status cell of the row to "closed" and moves the whole row under the table of
«## Closed» (GAPS l. 13), as its last row. sha1 0eeeafed601596b4076c8760fe72f61bf776a81b of the line below without its newline and unfilled,
7414 bytes, 81 opening and 81 closing parentheses, 0 pipe characters. <DATE>, <HH:MM> and <checker> are the landing date, time and the
CHECKER commit of the PASS (C148), all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R131 (P-N5-EXP; CHECKER C148 <checker>) [refereed-only] LANDED: DEAD-END packet for the candidate N5 (SPEC S1-S5 with FIX 1-4, from its default start S3), CONDITIONAL until two referees sign, in three parts: (1) UNCONDITIONAL (premise: RESULTS R104's definitions of the genome, IDEAL-ACYC, the X-chain order, the IDEAL step and L(G) only; no theorem of R104 used): for every k ≥ 3 the genome G_k of rule R (levels 0..k; unit j, 1 ≤ j ≤ k − 1, is a block pair u_j, v_j with an observer pair Y_j = (y_j, ȳ_j) and, for 2 ≤ j ≤ k − 2 only, an end-follower e_j and a second observer pair Y′_j = (y′_j, ȳ′_j), so the units 1 and k − 1 have four movers and the others seven; outside the units, the level-0 pair u_0, v_0 and the wires wv_j, 1 ≤ j ≤ k − 2, and wu_j, 2 ≤ j ≤ k − 2; all parities even, β-ranks by Ξ-depth with ties broken by β-id; generator experiments/red-b/gk.py) is in IDEAL-ACYC with N = 9k − 16 movers, M = 18k − 32 options (every mover has two) and k + 1 levels, its IDEAL run has exactly L(G_k) = 2^k − 2 steps and stops «stuck», and in it every mover of unit j (1 ≤ j ≤ k − 1) changes its option exactly 2^(j−1) times, v_0 once, u_0 and the wires never (11·2^(k−2) − 9 option changes in all); so R104's IDEAL-ACYC-POLY («there is a polynomial q such that L(G) ≤ q(N + M) for every G ∈ IDEAL-ACYC») is FALSE, already for genomes of degree 2 (N + M = 27k − 48) (Theorem EXP-IDEAL, PROVED lane; its RESPONSE LEMMA in the prefix form LEMMA′ of fixes entry 4, with CAUSAL and STABLE in step form); (2) PROVED-CONDITIONAL on RESULTS R117's Theorem REACH3 as landed (refereed-only; R117's standing premises, in the words of its title line: «with R104's premises as landed (1E-N3 = RESULTS R57 (b) in its two forms; RESULTS R24 (a) Lemma R and R24 (b)'s choice rule with RESULTS R103's bridge B and (R1) ruling; RESULTS R36 (c) Lemma P1 on the dual game) and RESULTS R15 (d) for termination only»): the N5 run of Γ3(G_k) from S3 (n = 135k − 230 vertices, m = 176k − 300 edges) has one FL run of length exactly 2^k − 2 and makes at least 2^k − 1 iterations, so no polynomial in n or in n + m = 311k − 530 bounds the number of iterations of N5 from S3; hence, through R117, N5 (SPEC S1-S5, default start S3) does not run in polynomial time, cannot pass gauntlet step 4 (TARGET.md §5), is a DEAD END as an M4 candidate, and G-N5-TIME is answered NO for N5 from S3 (Corollary EXP-N5); and, PROVED-CONDITIONAL on RESULTS R124's Corollary EXACT-L as landed (premise R117 (f), under SPEC's S1 tie-breaks, same standing premises): N5 from S3 on Γ3(G_k) makes exactly 2^k + 1 iterations, with one fallback, at iteration 2^k − 1 (Corollary EXP-N5′); obstruction RIPPLE (S4a's root-first key rule refuses an improving switch until the key order allows it, and on Γ3(G_k) this makes unit j + 1 respond twice in every response of unit j); (3) DATA (measured; every measured run is below n²: the largest, k = 13 (fixes entry 6, one engine), makes 8,193 iterations on n = 1,525 vertices, and 2^k − 1 > n² first at k = 23, n = 2,875, > n³ at k = 37, > n⁴ at k = 51, by arithmetic, not run; so the dead end rests on the proof of (1) and (2) and not on the DATA) (unit: one genome G_k, resp. one game Γ3(G_k); every counter named is a must-0 counter and is 0, every control fires): R104's eight membership clauses on G_3 … G_14 (b6member.py, member.out: viol 0); the IDEAL run equal state by state on three simulators, T = 2^k − 2, for k = 3 … 14 (b6sim.py, sim.out: ideq 0); the proof's facts and schedule against the run at every state and step for k = 3 … 14 (b6lemma.py, lemma.out: kfact, vfact, sched, tlen, rest, swk 0), and LEMMA′, CAUSAL and STABLE of fixes entry 4 at the 16,368 response windows of the runs for k = 3 … 14, at every triple (j, a, t) for k = 3 … 12, at every state of G_3 and G_4, and off the run (b6prefix.py, prefix_*.out: h1, h2, psched, aviol, pviol, dviol, loc, stviol, c0e0 0; the frozen wording of the lemma, as a control, fails at exactly k − 1 triples per k); N5 itself on Γ3(G_k), two engines and two Γ3 builders, for k = 3 … 12 (b6n5.py, n5.out and n5_k12.out: 2^k + 1 iterations, one fallback at iteration 2^k − 1, mover states equal to the model's; mism, wrong, wrong2, nonmover, engdiff, gdiff 0; winners equal to Zielonka's), and at k = 13 on one engine, the two Γ3 builders agreeing (fixes entry 6: b6n5ck.py, n5_k13.out: 8,193 = 2^13 + 1 iterations on n = 1,525 vertices, one fallback at iteration 8,191, mover states equal to the model's; mism, wrong, nonmover, gdiff 0; winners equal to Zielonka's; game experiments/red-b/data/b6b/pg/G_13_g3.pg), all files in experiments/red-b/data/b6b/out/; frozen instances Γ3(G_k) = experiments/red-b/data/b6b/pg/G_k_g3.pg, k = 3, …, 11 (175 to 1,255 vertices, 9 to 2,049 iterations), genomes of record experiments/red-b/data/b6b/G/G_k.json, k = 3, …, 14, at claude/l-red-b 350d84eb; independent replays, their counters in their own pinned outputs, cited, not re-run: L-COMP 22 BOX 48 (claude/l-comp dc6d831f: own generator, the model T = 2^k − 2 for k = 3 … 20, n5b on its own Γ3 builder 2^k + 1 iterations for k = 3 … 12, winners verified by Oink --tl and --zlk), L-RED 70 R245 (claude/l-red c7ed9b8b: own generator, the model for k = 3 … 12, its engine n5s237 for k = 3 … 8, verdict SURVIVES), REFEREE 35's pre-check (claude/referee 06ac891d: own simulator k = 3 … 15, own Γ3 builder and engine k = 3 … 12), REFEREE 36's first review (claude/referee c881709b: own generator and model k = 3 … 14, N5 on that lane's builder and engine for k = 3 … 9, games identical to this lane's files), REFEREE-2 41 (claude/referee-2 33ff0e98: own generator and model k = 3 … 16, own engine k = 3 … 11 with four solvers for the winners); NOT claimed: anything about N5 from other start pairs, about other S4a tie rules (DATA: N5′-xi makes 7 iterations on Γ3(G_4) and Γ3(G_6)) or about Howard's rule (DATA: at most 4 steps on the model), about any other candidate, or about parity games in general; N5's output on these games is correct (RESULTS R57 (b), Lemma OUT-G, under 1E-N3; DATA for k ≤ 12: winners = Zielonka's); TARGET.md §2 (M4) stays OPEN; scope tail (Lead reading L41): CAUSAL and LEMMA′ of fixes entry 4 (4.3, 4.4) are referee-originated, stated and proved by REFEREE 36 (claude/referee c881709b, docs/referee/R-P-N5-EXP.md §5.3; its verdict on the RESPONSE LEMMA: «NOT SIGNED AS WRITTEN; SIGNED in the form LEMMA′ of §5.3 below»; after fixes entry 4, its stage 4, claude/referee 78515253, the same file §12: «RESPONSE LEMMA SIGNED as restated in fixes entry 4 (= LEMMA′ of §5.3 with CAUSAL and STABLE in step form).»), and are signed independently by REFEREE-2 42, in the form its signature sentence gives (claude/referee-2 f17a2708, docs/referee-2/R2-P-N5-EXP.md, Addendum 2 §A2.3: «REFEREE-2 signs 4.1 (S1)-(S4), 4.2 STABLE, 4.3 CAUSAL, 4.4 LEMMA′ with their proofs (4.2, 4.3, 4.5) and 4.6, as printed in docs/red-b/P-N5-EXP-fixes.md at claude/l-red-b 24f4d436 (sha1 9dc9179f…), (R3)'s range read as t − 1 ≤ τ < last (F-1).») (P-N5-EXP, docs/red-b/P-N5-EXP.md, with fixes entries 1-7, docs/red-b/P-N5-EXP-fixes.md; L-RED-B successors 5-7). G-N5-TIME is answered NO for N5 from S3 (through RESULTS R117 as landed, refereed-only).

Addendum (first fill) (built by script; for the Lead and CHECKER; does not land). The checks ran on the pass-1 draft
  docs/agents/tools/r131/out/draft.p1.md (sha1 7e53a2383d63bdabb26beb13f31a318315fb6071, 423 lines), which equals this file without this Addendum
  and its empty line (asserted by tools/mkadd.py). Outputs verbatim below, each line tagged with its file: [fetch] the record of fetch.sh (date
  -u, fetched heads, git ls-remote lines); [lane] tools/lanecheck.sh: the lane's check.sh in a git archive, with a negative control; [fill]
  fill131.py; [upd] tools/upd.py: the UPDATE and its controls; [data] tools/data.py: the DATA numbers from the pinned outputs; [prem]
  tools/prem.py: the premises at trunk; [shape] tools/shape.py; [lp] tools/lp.py: every quotation at its commit, file and lines; [sweep]
  tools/sweep.py: every guillemet quotation against the sources; [land] tools/landtest.py: land131.py as DRYRUN (refusals and a full dry run on a
  copy). In them a pipe character is printed as a broken bar and a guillemet as a single angle mark; lines are wrapped at 150 columns
  (continuation lines are indented under their tag). After this file was written, tools/shape.py, tools/lp.py, tools/sweep.py and
  tools/landtest.py ran again on it (out/post_*.out; results in REPORT.txt). Not run: scripts/verify.sh, scripts/push.sh, the referees' own
  replays, Oink, Lean, any N5 engine.
  [fetch] date Sat Nov 14 13:41:37 UTC 2026
  [fetch] fetch claude/l-red-b rc 0 head 10dfedb6574c9291011a5a7fbbdff261fe312d91
  [fetch] fetch claude/referee rc 0 head 9ec40ff968ddc4a1c7f41a95d20aa6db6dbe40c3
  [fetch] fetch claude/referee-2 rc 0 head e643672d1343d414d9670066ec5564df78588beb
  [fetch] fetch claude/l-si rc 0 head 8c06291418616eca059c9239bdf8d59aad4f320f
  [fetch] fetch claude/l-comp rc 0 head dc6d831f7c56943a03070a9d268df2388565b438
  [fetch] fetch claude/l-red rc 0 head c7ed9b8b6af43c4ae94a5fa15571193bc923eedc
  [fetch] fetch claude/checker rc 0 head 628b1e2cee43b6746a9a31fd233ebee5ee0ebb32
  [fetch] fetch claude/vibrant-johnson-nxvvxo rc 0 head aeb90ac199aff97b7189666965d7fd7d7119cf29
  [fetch] local HEAD da3b90de47e0dafca289e641e2ea0513a3dfdc88 branch claude/vibrant-johnson-nxvvxo
  [fetch] ls-remote rc 0
  [fetch] ls-remote 10dfedb6574c9291011a5a7fbbdff261fe312d91 refs/heads/claude/l-red-b
  [fetch] ls-remote 9ec40ff968ddc4a1c7f41a95d20aa6db6dbe40c3 refs/heads/claude/referee
  [fetch] ls-remote e643672d1343d414d9670066ec5564df78588beb refs/heads/claude/referee-2
  [fetch] ls-remote 8c06291418616eca059c9239bdf8d59aad4f320f refs/heads/claude/l-si
  [fetch] ls-remote dc6d831f7c56943a03070a9d268df2388565b438 refs/heads/claude/l-comp
  [fetch] ls-remote c7ed9b8b6af43c4ae94a5fa15571193bc923eedc refs/heads/claude/l-red
  [fetch] ls-remote 628b1e2cee43b6746a9a31fd233ebee5ee0ebb32 refs/heads/claude/checker
  [fetch] ls-remote aeb90ac199aff97b7189666965d7fd7d7119cf29 refs/heads/claude/vibrant-johnson-nxvvxo
  [fetch] rc 0
  [lane] archive of claude/l-red-b 10dfedb6: experiments/red-b, docs/red-b, experiments/new/box203/inst: 606 files
  [lane] check.sh: rc 0 ; last line: red-b check PASS
  [lane] negative control (one byte appended to data/b6b/out/n5_k13.out): rc 1 ; mismatch line printed 1 ; last line: red-b check FAILED
  [lane] restored: rc 0 ; last line: red-b check PASS
  [lane] lanecheck: PASS
  [fill] fill131: pass-1 draft 424 lines; block 363 lines (sha1 17b216c93c1f06b5dabc02e966c9135b040a1e9e); UPDATE sha1
  [fill]     0eeeafed601596b4076c8760fe72f61bf776a81b; quotations 171, located passages 139, line-internal 18; open-slot tokens in the block 5
  [upd] UPDATE of R131 built from line L-3 (docs/red-b/P-N5-EXP-line-L3.txt @ 10dfedb6): 7231 characters, 7414 bytes, sha1
  [upd]     0eeeafed601596b4076c8760fe72f61bf776a81b (without newline, unfilled)
  [upd]   pipes 0 ; parentheses 81 / 81 ; fill tokens <DATE> 1 <HH:MM> 1 <checker> 1
  [upd]   labels moved behind their clauses: 3 ; drops 1 ; pipe pairs 0
  [upd]   starts 'UPDATE <DATE> <HH:MM>Z: RESULTS R131 (P-N5-EXP; CHECKER C148 <checker>) [refereed-only] LANDED: DEAD-END packet for the '
  [upd]   ends   's 1-7, docs/red-b/P-N5-EXP-fixes.md; L-RED-B successors 5-7). G-N5-TIME is answered NO for N5 from S3 (through RESULTS R117 as
  [upd]     landed, refereed-only).'
  [upd]   ends with the ruled sentence, one checker token, 0 pipes, every label directly before its clause end: True
  [upd]   the body is a rearrangement of the line minus the drops (same multiset of non-space characters): True
  [upd] control R128: landed UPDATE rebuilt from its landed title by updlib.build: byte-equal True (labels 12, 12692 characters, sha1
  [upd]     18ac1ef32797f2505380357a2f59b52b703dd382)
  [upd] control R129: landed UPDATE rebuilt from its landed title by updlib.build: byte-equal True (labels 9, 7901 characters, sha1
  [upd]     18dd6c0882fca12f634a1e992634d873f7de7b30)
  [upd] control R130: landed UPDATE rebuilt from its landed title by updlib.build: byte-equal True (labels 3, 3666 characters, sha1
  [upd]     6f6feef02ad360da13e6918d546ddea7e2b111a6)
  [upd] negative control, an altered drop string: refused True
  [upd] negative control, an altered label: refused True
  [upd] negative control, an altered clause end: refused True
  [upd] negative control, an added pipe pair that is not in the line: refused True
  [upd] negative control, one changed byte of the line: a different UPDATE True
  [upd] upd: PASS
  [data] OK   member.out: G_3..G_14: member 1, viol and c1..c8 0, N = 9k - 16, M = 18k - 32, d = k + 1 on 12 lines
  [data] OK   member_ctrl.out: 8 damaged copies of G_5, each member 0 and viol >= 1
  [data] OK   sim.out: k = 3..14: T = TB = TC = 2^k - 2, ideq 0, stop stuck, maxsw 2^(k-2), sumsw 11*2^(k-2) - 9
  [data] OK   sim.out howard: Howard's rule on the model: at most 4 steps
  [data] OK   lemma.out: k = 3..14: kfact, vfact, sched, tlen, rest, swk 0; T = 2^k - 2; moves 11*2^(k-2) - 9
  [data] OK   lemma_ctrl.out: control 1 sched 19, control 2 kfact 25 (both fire)
  [data] OK   n5.out: k = 3..11: n = 135k - 230, T1p = F = 2^k - 2, its = its2 = 2^k + 1, fb = fb2 = 1, mism, wrong, nonmover, wrong2, engdiff, gdiff
  [data]     0, pg_sha1 = sha1 of the pinned game file
  [data] OK   n5_k12.out: k = 12: its = its2 = 4097 on n = 1390, one fallback, the six counters 0
  [data] OK   n5_k13.out: k = 13, engine 1 only: its 8193 on n = 1525, fb 1, F 8190, mism, wrong, nonmover, gdiff 0
  [data] OK   n5ck_check.out: the checkpointed driver on k = 3..8: the frozen values
  [data] OK   size.out sizes: nine .pg files: n = 135k - 230, m = 176k - 300, sizediff 0
  [data] OK   size.out bounds: the six 'first k' lines equal exact-integer recomputation: k = 23, 37, 51, 26, 41, 57
  [data] OK   size_k13.out: k = 13: n 1525, m 1988, sizediff 0; control fires
  [data] OK   prefix_run.out: k = 3..14: h1, h2, h2last, psched, empty 0 at 16368 windows, 376836 (window, step) pairs
  [data] OK   prefix_all.out: k = 3..12: aviol 0, windows = expected = 2^(k-1) - 1, 163970 triples
  [data] OK   prefix_ctrl.out: control 5 (the lemma as frozen), k = 3..8: fails at exactly k - 1 triples per k: 2 3 4 5 6 7
  [data] OK   prefix_off.out: pviol 0 on 42902 windows (1089 proper), 346644 steps
  [data] OK   prefix_drive.out: dviol 0 on 28000 driven windows (16423 proper), 190500 steps
  [data] OK   prefix_loc.out: loc 0 on 81000 states (78534 repeated triples)
  [data] OK   prefix_stable.out: stviol 0 on 14698 cases
  [data] OK   prefix_u0.out: c0e0 0 on 8,000 states per k, k = 3..6; with u_0 free the count is positive
  [data] OK   prefix_exh.out: every state of G_3 (512) and G_4 (65,536) with the wires and u_0 at 0: c0e0, loc, stviol, pviol 0
  [data] OK   strat.out, n5_clean.out: badstrat 0 for k = 3..8 (strat.out) and k = 3..10 (n5_clean.out)
  [data] OK   enab.out: k = 3..12: venab, kenab, movd 0
  [data] OK   perm.out: keep 0 on 7050 relabelings
  [data] OK   reach.out: k = 3..8: startdiff, padcyc, padp, fbpos 0
  [data] OK   pins: 94 pinned files of 6 pin files (SHA1SUMS_b6b, SHA1SUMS_b6b_fixes1, SHA1SUMS_b6b_fixes2, SHA1SUMS_b6b_fixes3, SHA1SUMS_b6b_fixes4,
  [data]     SHA1SUMS_b6b_fixes5): 0 mismatches
  [data] OK   e7_r3.out: k = 3..14: r3in, r3move, r3rest, litdiff 0 at 16368 windows (16356 with j >= 2)
  [data] OK   frozen pins: SHA1SUMS_b6b byte-equal at the freeze commit and at the head
  [data] OK   below n^2: N5 itself, k = 3..13: 2^k + 1 < n^2 at every k (k = 13: 8193 < 2325625); the model's k = 20: 1048574 < 6100900; 2^k - 1 > n^2
  [data]      first at k = 23 (n = 2875: 8388607 > 8265625)
  [data] OK   above n, n + m: 2^k + 1 > n from k = 11 and > n + m from k = 12
  [data] OK   genomes: G_3..G_14 (JSON): N = 9k - 16, deg 2, levels 0..k, all parities 0
  [data] negative control (its 8193 read as 8194 in n5_k13.out): failing checks ['n5_k13.out', 'pins']: fires True
  [data] data: 32 checks, 0 failed; PASS
  [prem] RESULTS at trunk aeb90ac1: 17367 lines, 130 entry headings, the last R130 at l. 16525
  [prem] OK   R104 [refereed-only] heading l. 9864, entry l. 9864-10154; item 'definitions only': its words 'IDEAL' in the entry: True
  [prem] OK   R117 [refereed-only] heading l. 13362, entry l. 13362-13606; item 'Theorem REACH3': its words 'Theorem REACH3' in the entry: True
  [prem] OK   R57 [refereed-only] heading l. 2893, entry l. 2893-2958; item '(b)': its words '(b)' in the entry: True
  [prem] OK   R24 [refereed-only] heading l. 1064, entry l. 1064-1112; item '(a)': its words '(a)' in the entry: True
  [prem] OK   R24 [refereed-only] heading l. 1064, entry l. 1064-1112; item '(b)': its words '(b)' in the entry: True
  [prem] OK   R103 [refereed-only] heading l. 9641, entry l. 9641-9863; item 'bridge B': its words 'bridge B' in the entry: True
  [prem] OK   R36 [refereed-only] heading l. 1717, entry l. 1717-1751; item '(c)': its words '(c)' in the entry: True
  [prem] OK   R15 [refereed-only] heading l. 624, entry l. 624-673; item '(d)': its words '(d)' in the entry: True
  [prem] OK   R124 [refereed-only] heading l. 15371, entry l. 15371-15594; item 'Corollary EXACT-L': its words 'Corollary EXACT-L' in the entry: True
  [prem] OK   R131 absent, R130 is the last entry heading
  [prem] OK   entries the line names as 'RESULTS R<n>': R15 R24 R36 R57 R103 R104 R117 R124; not landed: []; later than R130: []
  [prem] OK   other R-tokens of the line: R1 = R103's (R1) ruling, inside the quotation of R117's title line; R2 = the file name R2-P-N5-EXP.md of
  [prem]     REFEREE-2's report; R3 = clause (R3) of LEMMA', inside REFEREE-2's signature sentence; R245 = L-RED 70's report R245, not a RESULTS
  [prem]     entry; unexplained: []
  [prem] OK   the line's quotation of R117's standing premises (253 characters) is in R117's title line (l. 13362): True
  [prem] OK   R117's title line has '(Theorem REACH3)': True
  [prem] OK   R117's title line has 'for every G with an ACYCLIC Ξ-graph': True
  [prem] OK   R117's title line has 'the run makes at least L(G) + 1 iterations': True
  [prem] OK   R124's title line has 'Corollary EXACT-L': True
  [prem] OK   R124's title line has 'ENDGAME-3-N5': True
  [prem] OK   R124's title line has 'premise RESULTS R117 (f)': True
  [prem] OK   R124's title line has 'makes exactly L(G) + 3 iterations': True
  [prem] prem: PASS
  [shape] OK   title = heading + the line (git bytes, 7267 bytes, sha1 fd9074a3b9961f59a1b64d5acdaa28529306ede9) + the checker token: line L-3 of
  [shape]     docs/red-b/P-N5-EXP-line-L3.txt @ 10dfedb6
  [shape] OK   title: pipe characters 0
  [shape] OK   title: parentheses 80 / 80, square brackets 1 / 1, guillemets 6 / 6
  [shape] OK   title passes the label rule of scripts/check_docs.py
  [shape] OK   negative control: the title without its label fails that rule
  [shape] OK   block: 363 lines (title + 362), no empty line, every line a bullet or a continuation, widest 140
  [shape]      bullets: Object; Fixes; The RESULTS line is L-3, fd9; Claims signed; Setting and scope, as both r; Premise; L41 and L43. The packet's
  [shape]     pr; Not signed; Referee strengthening and su; Honest limits; Data; DATA counters for the replay; Note; Signatures; INDEPENDENCE;
  [shape]     TARGET.md diff; Status
  [shape] OK   block: pipe characters 0, tabs 0
  [shape] OK   open-slot tokens: block 5 (the title's checker token 1, other 4); whole draft 9
  [shape]      landable by this count: no (open slots)
  [shape] OK   UPDATE line = updlib.r131_update(the line): 7414 bytes, sha1 0eeeafed601596b4076c8760fe72f61bf776a81b
  [shape] OK   UPDATE: pipes 0, parentheses 81 / 81, fill tokens 1 1 1, ends with the ruled sentence
  [shape] OK   recorded hashes (out/hashes.json): block sha1 17b216c93c1f06b5dabc02e966c9135b040a1e9e (363 lines), UPDATE sha1
  [shape]     0eeeafed601596b4076c8760fe72f61bf776a81b
  [shape] OK   first line starts '# Draft RESULTS R131 ' and is not marked landed
  [shape] OK   layout: block at lines 45-407, empty line 408, proposal 409-422, UPDATE line 423
  [shape] shape: PASS
  [lp] lp (1) ledger: 328 entries (quotations with lines 126, quotations without 45, located passages 139, quotations inside the line 18); recorded
  [lp]     line range not among the matches of the second search: 0
  [lp]   10dfedb6 docs/red-b/P-N5-EXP-fixes.md 25
  [lp]   10dfedb6 docs/red-b/P-N5-EXP-line-L3.txt 18
  [lp]   10dfedb6 experiments/red-b/check.sh 3
  [lp]   350d84eb docs/red-b/P-N5-EXP.md 9
  [lp]   8c062914 docs/si/box108-gk-proof.md 2
  [lp]   9ec40ff9 docs/referee/R-GK-precheck.md 2
  [lp]   9ec40ff9 docs/referee/R-P-N5-EXP.md 138
  [lp]   aeb90ac1 CLAUDE.md 1
  [lp]   aeb90ac1 TARGET.md 3
  [lp]   aeb90ac1 docs/DECISIONS.md 2
  [lp]   aeb90ac1 docs/GAPS.md 4
  [lp]   aeb90ac1 docs/RESULTS.md 9
  [lp]   aeb90ac1 docs/agents/LEAD-STATE.md 3
  [lp]   aeb90ac1 docs/red/P-N5-REALIZE.md 4
  [lp]   c7ed9b8b docs/red/R245-kill-Gk.md 2
  [lp]   dc6d831f experiments/comp/box48/README.md 4
  [lp]   e643672d docs/referee-2/R2-P-N5-EXP.md 97
  [lp]   e643672d docs/referee-2/R2-box108.md 2
  [lp] lp (2) draft: 171 quotations outside the title and UPDATE lines, 12 in them; in the draft but not in the ledger 0; in the ledger but not in the
  [lp]      draft 0; 'q' entries not followed by their line numbers 0; title / UPDATE quotations not in the line 0
  [lp] negative control 1 (one ledger entry moved by one line): caught True
  [lp] negative control 2 (one letter of one quotation changed in a copy of the draft): caught True
  [lp] lp: PASS
  [sweep] sweep header: 2 quotations, 0 not found; control (one letter changed): 2 of 2 not found: ok
  [sweep] sweep title line: 6 quotations, 0 not found; control (one letter changed): 6 of 6 not found: ok
  [sweep] sweep entry block below the title: 161 quotations, 0 not found; control (one letter changed): 161 of 161 not found: ok
  [sweep] sweep proposal and UPDATE: 14 quotations, 0 not found; control (one letter changed): 14 of 14 not found: ok
  [sweep] sweep Addendum: 0 quotations, 0 not found; control (one letter changed): 0 of 0 not found: ok
  [sweep] sweep whole file: 183 quotations, 0 not found; control (one letter changed): 183 of 183 not found: ok
  [sweep] sweep: sources 19 (PKT FIX LINE REF1 PRE REF2 R2B B108 BOX48 R245 RES GAPS TARGET CLAUDE DEC LEAD R104P R130D CHK)
  [sweep] sweep: PASS
  [land] T1 the draft as it is (8 open-slot tokens besides the checker token; stand-in line True): rc 2, refused: as expected
  [land]    T1 land131: REFUSED: the draft holds the open-slot word 9 times; only the title's checker token may carry it (other lines: [26, 27, 98,
  [land]     112, 362, 368])
  [land] T2 satisfied copy (8 tokens replaced; hashes recomputed for the copy): rc 0
  [land]    T2 land131: DRYRUN into dry2, stamp 2099-01-13 00:00Z, checker 5555555
  [land]    T2   RESULTS: 17367 -> 17731 lines (+364 = block 363 + 1 empty); R131 at l. 16725-17087, the Erratum line moves l. 16725 -> l. 17089;
  [land]     pipes 1483 -> 1483 (title 0)
  [land]    T2   GAPS: 23 -> 23 lines; row G-N5-TIME l. 11 -> l. 23 (status open -> closed, under the closed table); row pipes 76 -> 76; file pipes
  [land]     198 -> 198; UPDATE 7414 bytes
  [land]    T2   GAPS row starts '¦ G-N5-TIME ¦ major ¦ L-NEW (L-LIT T22; referees later) ¦ closed ¦ N5 '
  [land]    T2   GAPS UPDATE starts 'UPDATE 2099-01-13 00:00Z: RESULTS R131 (P-N5-EXP; CHECKER C148 5555555) [refereed-only] LANDED:'
  [land]    T2   GAPS row ends '-B successors 5-7). G-N5-TIME is answered NO for N5 from S3 (through RESULTS R117 as landed, refereed-only). ¦'
  [land]    T2   NOW: R17-R130 -> R17-R131 (1 place)
  [land]    T2   scripts/check_docs.py on the copies: rc 0
  [land]    T2 land131: DRYRUN done (nothing in the repository was written)
  [land]    T2 sha1 of the results: RESULTS 9ed60ce103dda557ee261d8053057db5cf30324b GAPS 927ccf69eae28c0b49fe3f6b07c1e2178a64b962 NOW
  [land]     ad30d9d4b40a52310c50872174e8b9d2426db016
  [land]    T2 OK   RESULTS: one R131 heading at l. 16725, block l. 16725-17087, empty l. 17088, Erratum line l. 17089
  [land]    T2 OK   RESULTS: pure insertion (the 16724 lines before and the 644 lines after are unchanged), 17367 -> 17731 lines
  [land]    T2 OK   RESULTS: the inserted block is the copy's block with the checker token filled (checker 5555555) once, no open-slot word, no fill
  [land]     token)
  [land]    T2 OK   RESULTS: headings 131, the last two R130 R131; pipes 1483 -> 1483
  [land]    T2 OK   GAPS: the row is the old row with status closed and ' ' + UPDATE + ' ¦' appended, nothing else (239722 -> 246956 characters)
  [land]    T2 OK   GAPS: row l. 11 -> l. 23, below the closed heading (l. 12), the last table row of the file; every other line unchanged; 23 -> 23
  [land]     lines
  [land]    T2 OK   GAPS: check_docs cells of the row: id G-N5-TIME, severity major, owner present True, status closed; row pipes 76 -> 76
  [land]    T2 OK   GAPS: RESULTS UPDATEs on the row 60 -> 61, the last three R129 R130 R131
  [land]    T2 OK   NOW: 1 line(s) differ, 84 -> 84 lines; only the cfg replacements
  [land]    T2 OK   draft copy: first line ends with the landing note, the rest unchanged
  [land]    T2 OK   scripts/check_docs.py on the copies: rc 0
  [land]    T2 OK   negative control (the landed title without its label): check_docs rc 1, message names the entry True
  [land] T3 the copy with one letter of the block changed, T2's hashes: rc 2: land131: REFUSED: the draft's entry block (sha1
  [land]     00ed6a32fb56df73378ca83f9ed3cadf42f47009, 363 lines) is not the block build.sh recorded (sha1 1c4a2ae5422b6821cd77efc0e49397547f456ee8,
  [land]     363 lines)
  [land] T4 the copy with one more open-slot word in its header: rc 2: land131: REFUSED: the draft holds the open-slot word 2 times; only the title's
  [land]     checker token may carry it (other lines: [2])
  [land] landtest: PASS
