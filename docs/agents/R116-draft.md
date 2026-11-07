# Draft RESULTS R116 (Lead; first fill 2026-11-07T02:31:22Z by date -u (subagent) on P-IDEAL-MOVES line L-4, docs/new/P-IDEAL-MOVES-line-L4.txt, l-new fd5c163f, sha1 73c16d1e2b009ff2e3d774a904e4462be0874db1) — to CHECKER C129 — NOT LANDED; goes after the last landed R-entry before «**Erratum E-1**»: after R114 while R115 is not landed, after R115 once R115 has landed (both landing simulations: Addendum (9))
FIRST FILL (this text). Read at the origin heads fetched at 2026-11-07T02:09:48Z (git fetch, after the Lead push running at the start of
this fill had ended; pgrep empty) and re-fetched at 2026-11-07T02:29:42Z: l-new fd5c163f, then f55dac37 (fd5c163f holds fixes entry 3
and line L-4; the packet, L-1, L-2, L-3, L-4, the fixes, movescheck.py, movescheck.out, box150/check.py and the four instance files are
byte-equal at d86adc86 (where they exist), fd5c163f and f55dac37, by sha1 and git diff; f55dac37 adds L-NEW box 189,
docs/new/N5-REACH-box189.md and experiments/new/box189/, outside movescheck's box150-box187 corpus, and appends a block to
experiments/new/check.sh after l. 942, leaving l. 1-942 unchanged), referee 2fe03939 (docs/referee/R-P-IDEAL-MOVES.md §C add. 2), then
c011995c (a post-note on L50, l. 205-206; the commit also adds R-P-M2D-DEAD.md, another packet, not read for this entry), referee-2
88c0c6d6 (docs/referee-2/R2-P-IDEAL-MOVES.md Addendum 3), then 6924e140 (a post-note on L50, l. 172-174), checker 1c4ba1c3, then
2dd44fc1 (docs/checker/C128.md: R115 FAIL E-1..E-5, DATA wording, an L-3 with five replacements; C128.md was not on origin at the first
fetch); origin trunk 6ca995ed («Lead: L50 (MOVES-2D killed, triple-replayed; P-IDEAL-MOVES lands without status claim); R115 draft to
C128; L-COMP 10; log»), pushed. Local trunk = seven merges (--no-ff) into 6ca995ed: 3f765de8 (l-new fd5c163f), 0c2e3e49 (referee
2fe03939), bf06df78 (referee-2 88c0c6d6), 3e8d0bcb (l-new f55dac37), 1eb447f2 (checker 2dd44fc1), d7515bd2 (referee c011995c), 1cc33e15
(referee-2 6924e140); checker 1c4ba1c3 was already an ancestor; then the commit holding this file. Not pushed. fd5c163f, f55dac37,
2fe03939, c011995c, 88c0c6d6, 6924e140 and 2dd44fc1 are NOT ancestors of origin trunk 6ca995ed (git merge-base --is-ancestor); the Lead
pushes trunk before landing. The body makes NO statement about trunk (C113 E-2). RESULTS (sha1 555d41bd85b8ea52a1e57459c0a4fe0fcb7f6cc1,
13,306 lines), GAPS (sha1 3c4ff44d1b822110d9bfd0d1a2d8661ea6b5361e, 23 lines; l. 11 76 "|", 49 «UPDATE 2026-», the last one R114's),
TARGET.md, DECISIONS, DECISIONS-INDEX, NOW and CLAUDE.md are byte-equal at 6ca995ed and the local trunk (git diff, empty). Last commit
on RESULTS and GAPS: b6d1484b (2026-11-06T21:57:54Z, R114's landing). R115 (P-IDEAL-IM) is NOT landed at this fill: its draft
docs/agents/R115-draft.md (fc665614, sha1 bc98799907f0c5e6191c7dbcb04822a9b6f0f022, 808 lines) is at CHECKER C128, which FAILED it
(2dd44fc1, E-1..E-5); its second fill is still to come.
Sources read: the packet docs/new/P-IDEAL-MOVES.md (frozen d86adc86, 2026-11-06T21:11:22Z, sha1
5ce2947d1ee4dab317e5c06446b38f050146cafb, 202 lines; read in full), lines L-1 (d86adc86, sha1 819c58159100d77ec509348345cfd1a641a6f9e7,
4,313 bytes), L-2 (9995f5a2, f3692aaa033540ff0494b0aac6b2d524757d5c00, 4,495 bytes), L-3 (d7b96be8,
d3983c68cdda03e81fdaedec770af587f758d84e, 4,567 bytes) and L-4 (fd5c163f, 2026-11-07T01:16:07Z, sha1
73c16d1e2b009ff2e3d774a904e4462be0874db1, 4,598 bytes), the fixes file docs/new/P-IDEAL-MOVES-fixes.md (fd5c163f, sha1
510152dab3512980e5e739710f46ff14797edf87, 116 lines, 9,674 bytes; entries 1-3; read in full); experiments/new/box187/movescheck.py (sha1
8153717b8596b82a68c8b35c7ab76aabc765d7c2, 116 lines; read in full), movescheck.out (sha1 4874020973e02bf269b64624e4e7b110bb08ca24, 6
lines), experiments/new/box150/check.py (the simulator Gen; sha1 019de0f7b36dcbd47743b3d27b4a1a93549d574b; Gen read in full), the
instances experiments/new/box186/out/pass_d3_D3.json (8bca976438ca184bb8b8e4d5ecf3455f51809ff4), pass_d4_D4.json
(3bf6a4a48bc2df9fb8809306f8347ee280965b07), pass_d5_D5.json (16be2e594732ad0b21e2c84aa4cdbc62d143e7c4) and
experiments/new/box187/inst/m4_z4_r7.json (7c158e2f806df2d1984418902548cfc2cb243d75), experiments/new/check.sh block «P-IDEAL-MOVES» (l.
935-942 at fd5c163f; the file 943 lines, sha1 27d95e15ab5c87274583041f992a1e4aef9846a7), notes/L-NEW.md at fd5c163f (successor 57's
handover); REFEREE's docs/referee/R-P-IDEAL-MOVES.md (successor 24's report c82fac5c, successor 25's §C 72f4b2f3, §C add. 1 e7047ace, §C
add. 2 2fe03939, post-note c011995c; read in full); REFEREE-2's docs/referee-2/R2-P-IDEAL-MOVES.md (successor 29's report 38a2adb6, Add.
1 f71fdbdb, Add. 2 0fdc26d4, Add. 3 88c0c6d6, post-note 6924e140; read in full) with its tool directory docs/referee-2/R2-P-IDEAL-MOVES/
(listed, not re-run); RESULTS R104 (title l. 9864), R105 (l. 10155), R110 (l. 11323), R111 (l. 11598), R112 (l. 11909), R113 (l. 12152),
R114 (l. 12394-12695), Erratum E-1 (l. 12697), E-2 (l. 12710), Note E-3 (l. 12738), Dead ends (l. 12769); GAPS l. 11; DECISIONS L50 (l.
440-449) and DECISIONS-INDEX l. 45; docs/checker/C120.md-C127.md and C128.md (2dd44fc1, sha1 bc16269482429ea2f3b3cfc01730f5de555d1494,
135 lines; read in full); docs/agents/R114-draft.md (as landed) and R115-draft.md (the models of this draft).
Re-runs (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r116/, from a git
archive of fd5c163f's experiments/new and docs/new, nothing written into the repository): (a) check.sh block «P-IDEAL-MOVES»
(experiments/new/check.sh l. 1-6, the shebang, comments and «set» line, then a «cd» into the archive in place of l. 7, then l. 8 and l.
935-943; runw187.sh, w187.out), 2026-11-07T02:11:29Z-02:11:41Z, rc 0, the PASS line of (10); (b) my split of movescheck.py's counters
(g9split.py: the frozen source exec'd unchanged up to main(), its check_run re-run on its own corpus with the same counters, «RX 0 AGA 0
AGB 0 AGC 0 SWA 0 SWB 0 SWC 0 SWD 0 SWE 0 WPD 0» and «runs 63223 steps 140395 RXEQ 59502 segments 225917 windows 1288162 maxD 9»
reproduced; then my own measurements on the same 63,223 runs; my DATA, not lane DATA, not wired into check.sh),
2026-11-07T02:12:03Z-02:12:20Z, rc 0; (c) the DEAD-SEG files from their stored starts (deadstart.py, box150 Gen); (d) the line chain L-1
→ L-4 by the fixes entries' own replacement strings, the L-3 → L-4 token diff and the G-9 candidate lines (wdiff116.py); (e) the premise
quote test (prem116.py); (f) the UPDATE build with 18 controls (upd116.py); (g) the quote sweep, the stale-status grep and the two
landing simulations (chk116.py, sim116.py).
LESSONS APPLIED. C113 E-1: the title is L-4 verbatim with no insertion. C114 Add. 1 E-1: the UPDATE head carries «<DATE>». C115 E-1: the
premise route is checked against what RESULTS records (G-4; prem116.py, hits per quote, explained). C116 G-1, C118-C127 §4: the UPDATE
rule of R111 (sentinel_build111 with its default drops and the «(DATA, » opening, and R111's own DEAD-clause step for the unlabelled
DEAD clause), no new adaptation (G-U). C116 G-2: name clashes settled by one body sentence (G-6). C117 E-1 / E-2: no sentence wider than
signed; instances specified (G-9 (ii) flags one under-specified instance). C118 E-1: no stale status sentence (G-S, G-11). C118 §3 /
Erratum E-2: EVERY DEFINITION of L-4 diffed against the packet (G-2). C120 §5 / C121 §5 / C122 E-2 / C124 E-1 / C125 E-1 / C127 E-1 and
C128 E-1..E-5 (DATA wording: a label naming a narrower statement than the counted set, a check evaluated at another state than the
clause names, a count on a subset of the DATA head's set, the unit of a control count, a clause half without a counter): EVERY DATA
clause of L-4 tested against movescheck.py's counter code for unit, set and the scope of the statement it attaches to, and every clause
without a counter looked up in the no-DATA list (G-9; two clauses flagged, (i) and (ii), each with an exact replacement string). C122
G-0: parentheses balanced (G-1). C122 E-3: the source note names every proof-carrying file (G-1). C123 E-1: no lane label and no packet
name in the title before the claims (G-1). C123 E-2: no stale referee state (G-13). C119 E-1: every «referee X did Y» is checked against
that referee's file. L50: no status claim about MOVES-2D, and MOVES-2D not presented as a route (G-S).
to check: FLAGS FIRST (G-0 to G-14; the ones for the Lead or CHECKER: G-0 (number), G-9 (i) (DATA: «equality on 59,502» is counted for
an equality the line does not state; exact replacement), G-9 (ii) (DEAD-SEG: the starts of pass_d3_D3 and pass_d4_D4 are not in the
line, and their stored starts do not give D 3 and 4; exact replacement), G-S (MOVES-2D: no status claim, not a route; L50), G-P
(placement after R114 or after R115), G-U (the UPDATE: R111's DEAD-clause step, no new adaptation), G-C (overlap with landed R105, R111,
R113, R114)), then the CLEAN items and (0)-(14).
- G-0, THE CHECKER NUMBER. docs/checker/ ends at C128.md at checker 2dd44fc1 (C128 = R115: docs/agents/R115-draft.md l. 1, «to CHECKER
  C128»; NOW l. 2, «R115 draft fc665614 at CHECKER C128.»); docs/checker/C129.md does not exist; «C129» occurs 0 times in RESULTS and
  GAPS (by script); notes/CHECKER.md at 1c4ba1c3 l. 7 «NEXT (Lead 22:18Z): R115 (P-IDEAL-IM) when its L-2 MATCHES at both referees, then
  R116 (P-IDEAL-MOVES). Use C128, C129.». «R116» occurs 5 times in RESULTS, all L-RED's box R116 in the Dead-ends section (G-6). This
  draft uses C129 (title fill, UPDATE head, GAPS preamble).
- G-9, DATA (the C120 §5 / C121 §5 / C124 E-1 / C125 E-1 / C127 E-1 check item and the C128 DATA-wording class: unit, set and the scope
  of the statement each DATA clause attaches to, against movescheck.py's counter code, read by me in full at fd5c163f; movescheck.py
  line numbers). The five C128 kinds: (i) below is the kind of C128 E-1 / E-3 (the count is right, the statement it names is not the one
  counted); C128 E-2 does not recur (AGA reads π under s_(t−1) and KP under s_t, SWE the chain under s_(t−1), exactly as their clauses);
  C128 E-4 does not recur (movescheck.py has no control count and the line quotes none); C128 E-5 does not recur (every claim clause has
  a counter, a no-DATA entry or an arithmetic step from counted checks). Every figure of L-4's DATA parenthesis equals movescheck.out
  and my re-runs (a), (b): «208 in-tree 𝓛^R_d genome files» = the files is_lr() accepts among the JSON files under box150-box187 (l. 90
  glob «box1[5-8][0-9]/**/*.json», 150 ≤ box ≤ 187; by d: d 1: 2, d 2: 10, d 3: 73, d 4: 68, d 5: 40, d 6: 13, d 8: 2, total 208);
  «every start for d ≤ 5 and the stored start for d ≥ 6» = l. 96 (N ≤ 10: all 2^N starts, level-0 movers included); «63,223 runs» =
  «runs 63223». Clause by clause:
  - (i) REDUCE-XI (FLAG, E-candidate: the counter measures an equality the line does not state). «REDUCE-XI 0 violations on 63,223
    runs»: RX (l. 40) counts a run once if some t ∈ [2, T] has Mv_(t−1) ∩ Z = ∅ or T > 1 + Σ_(z ∈ Z) moves(z): exactly the two halves of
    L-4's REDUCE-XI clause, per run. MATCH (unit run, set 63,223, scope the line's two halves). «, equality on 59,502»: the only
    inequality of L-4's REDUCE-XI clause is «T ≤ 1 + Σ_(z ∈ Z) moves(z)», so the line reads as: T = 1 + Σ_(z ∈ Z) moves(z) on 59,502
    runs. The counter is RXEQ (l. 41, docstring l. 18 «Info: RXEQ = runs with T = 1 + #{t <= T-1 : Mv_t meets Z}»): runs with T ≥ 1 and
    T = 1 + #{t ∈ [1, T − 1] : Mv_t ∩ Z ≠ ∅}, the middle term of the packet's chain (packet l. 82 «T ≤ 1 + #{t ∈ [1, T − 1] : Mv_t ∩ Z ≠
    ∅} ≤ 1 + Σ_(z ∈ Z) moves(z)»), which L-4 does not state. On the same 63,223 runs, T = 1 + Σ_(z ∈ Z) moves(z) holds on 8,399 runs
    only (my count, g9split.py, «eq_sum 8399»; RXEQ reproduced, «eq_mid 59502»). So the clause attaches 59,502 to a statement whose
    equality holds on 8,399: the count is right, the statement it names is not the one counted (set and meaning; the C127 E-1 / C128
    class). The packet itself names it right (§6 l. 185-186 «equality T = 1 + #{t ≤ T − 1 : Mv_t ∩ Z ≠ ∅} on 59,502 runs»); L-1 dropped
    the formula, and neither referee flagged it (REFEREE §3 row «REDUCE-XI: step t − 1 moves a member of Z; T ≤ 1 + Σ moves(z) … RX (l.
    40: both) … MATCH» reads RX only; REFEREE-2 D-1 «the middle inequality is implied by the per-step form, not counted separately»).
    PROPOSED EXACT REPLACEMENT (the old string occurs once in L-4 and once in the UPDATE, by script): "REDUCE-XI 0 violations on 63,223
    runs, equality on 59,502" → "REDUCE-XI 0 violations on 63,223 runs, equality T = 1 + #{t ≤ T − 1 : Mv_t ∩ Z ≠ ∅} on 59,502" (the
    packet's own words; no "|", no parenthesis added; L-4 with it alone: sha1 4094ef917ea427d5dfe32cbf60295ade92bd8fef, 4,644 bytes, 71
    «(» / 71 «)»; the source note would also change if a fixes entry 4 is named in it). Alternative: drop «, equality on 59,502».
  - (ii) DEAD-SEG instance under-specified (FLAG, E-candidate, the C117 E-2 class; the clause is in the DEAD clause, not in the DATA
    parenthesis, but its numbers are machine numbers). L-4: «(experiments/new/box186/out/pass_d5_D5.json, 𝓛^R_5, start 0101010110: a
    Ξ-target of level 4 moves at steps 1-5 while LM = 0; also pass_d3_D3.json and pass_d4_D4.json, D 3 and 4 with LM 0)». The start is
    given for pass_d5_D5 only. movescheck.py runs all three from explicit starts (l. 108-110: «110100», «01010111», «0101010110»); the
    packet says so (l. 170 «the stored start of the .json is not used, the start is given explicitly»). From their STORED starts (000000
    and 00000000) pass_d3_D3 and pass_d4_D4 give runs of T 2 whose longest metronome segment of a mover of level ≥ 1 has D 1 (my
    deadstart.py: «stored start 000000 T 2 best D-2LM segment: D 1 mover 2 seg (2, 2) LM 0», «stored start 00000000 T 2 …»). So «D 3 and
    4 with LM 0» cannot be reproduced from the line. The kill for c ≤ 4 rests on pass_d5_D5 alone, whose start is given; the two others
    are supporting. PROPOSED EXACT REPLACEMENT (once in L-4, once in the UPDATE): "also pass_d3_D3.json and pass_d4_D4.json, D 3 and 4
    with LM 0" → "also pass_d3_D3.json from start 110100 and pass_d4_D4.json from start 01010111, D 3 and 4 with LM 0" (L-4 with (i) and
    (ii): sha1 e970fec2fedce5b83ca50ca5daaca2633774da5e, 4,682 bytes, 71 / 71). Optional, a note only: DEAD-LEV's file is run from its
    stored start, which the line does not say (m4_z4_r7's stored start 10111010 is the one movescheck.py uses, l. 111); "𝓛^R_4: a
    Ξ-target of level 2 moves 7 times" → "𝓛^R_4, stored start 10111010: a Ξ-target of level 2 moves 7 times" (with (i)-(ii): sha1
    82c5290b15d3c57ee743b12f43a8f9fc2eeed34c, 4,705 bytes).
  - AND-GATE: «0 on every (run, step, degree-2 mover)» = AGA (l. 49-51), per (run, t, x) over every mover (all of degree 2 on 𝓛^R_d),
    the iff of the clause with π from Gen.face (ENC integers) and KP from the keys under s_t: MATCH (1,298,948 triples, my count; no
    figure in the line). «every pair of consecutive moves (the min bound by arithmetic)» = AGB (l. 55-56), per consecutive pair (37,510
    pairs, my count): a π change in [t, t′ − 1] and a KP change in [t + 1, t′]; the bound moves(x) ≤ 1 + min(KF_x, PF_x) follows by
    arithmetic (disjoint windows; packet §2 (b)); labelled so (MV-L1). MATCH. «every change of π» = AGC (l. 52-54), per (run, t, x) with
    π_(s_t)(x) ≠ π_(s_(t−1))(x), v(x, b) rising strictly at t (235,189 changes, my count). MATCH.
  - WINDOW-DOUBLE: «bound 0 on 1,288,162 (window, level ≥ 1) pairs» = WPD (l. 82-86): every (a, b) with 0 ≤ a < b ≤ T and every j = 1..d
    − 1, the inequality F_W(j) ≤ 2 + 2F_W(j − 1) on W = [a + 1, b], with R113's flip as the change of the order of the keys of the
    current options (l. 46, Gen.keys). MATCH (unit, set, scope). «its BURST-2 case 0 on every maximal window without flips of the pair
    below» = SWD (l. 74-81), per maximal flip-free window of pair j − 1 (219,435 windows, my count); every such window W has F_W(j − 1)
    = 0, and BURST-2 for its sub-windows follows (F_W monotone in W); WPD also covers it. MATCH (note: the docstring l. 14 labels SWD
    «SEG-WINDOW (d) BURST-2», REFEREE-2 D-3). «the pass-through clause of WINDOW-DOUBLE … no separate DATA»: no counter (true).
  - SEG-WINDOW: «0 on all 225,917 metronome segments for its first three clauses and its last one» = SWA (l. 65: the pair l − 1 flips at
    every step of [a + 1, b]), SWB (l. 66-67, a conjunction with D ≤ 1 + LS + PT, which the line does not state; its zero covers «every
    step of [a + 1, b] moves a mover of level < l»), SWC (l. 68-69: D ≤ 3 + 2F_[a+1,b](l − 2), l ≥ 2; D ≤ 3, l = 1) and SWE (l. 70-72:
    at every t ∈ [a, b − 1] some y ∈ Gen.play(s_(t−1), x, s_(t+1)(x)), the movers of that chain after x, is in Mv_t), on every [a, b] of
    consecutive steps all moving one mover of level ≥ 1 (l. 59-63, all sub-segments, 225,917). MATCH, in L-4's clause order (REFEREE-2
    l. 105 ««first three clauses and its last one» = SWA, SWB, SWC, SWE in L-1's clause order»). «the 3-step clause of SEG-WINDOW: no
    separate DATA»: no counter (true).
  - «MOVES-EQUIV … no separate DATA»: no counter (true). «the four DEAD instances re-run» = the three «DEAD-SEG» lines and the
    «DEAD-LEV» line of movescheck.out (l. 101-113 of the tool). MATCH.
  - SCOPE (NOTE, the R114 G-9 (v) / R115 SCOPE precedent): REDUCE-XI is stated «at any degree and width» and AND-GATE «at any degree
    elsewhere»; their DATA is on the 208 𝓛^R_d files only (degree 2, two movers per level); the DATA head names that set.
  - CORPUS (NOTE): movescheck.py does not test Ξ-acyclicity (box150 Gen.face raises only on a cycle its chain walk meets). My
    depth-first search, ignoring the stored «xorder», finds all 208 files Ξ-acyclic; 206 carry an xorder and every one is a topological
    order; ranks and gates are distinct in all 208 (g9split.py «cyclic_files 0 dup_rank 0 dup_gate 0 … xorder_files 206 bad_xorder 0»).
  - No other clause of L-4's DATA parenthesis has a counter of a different unit, set or scope; every claim clause of L-4 without a
    counter is in the no-DATA list or follows by arithmetic from counted checks (the AND-GATE min bound, labelled; BURST-2 for
    sub-windows). The DEAD clauses are machine numbers of movescheck.py's DEAD lines (G-9 (ii) above).
- G-S, MOVES-2D (FLAG for the Lead and CHECKER; Lead reading L50, DECISIONS l. 440-449). L50 (2): «P-IDEAL-MOVES lands with a line that
  makes no status claim about MOVES-2D (fix round 3, L-4). Its signed items do not depend on MOVES-2D (both referees, 2026-11-07). The
  DEAD record is a separate entry.». L-4 names MOVES-2D three times: «(the lane conjecture MOVES-2D, not claimed here)» inside
  MOVES-EQUIV's conditional «would give T^R(d) ≤ 4d² − 4d + 3», and in the tail «MOVES-2D is not claimed (its status is not part of this
  result; …» with «so MOVES-2D is sufficient for a polynomial bound on T^R, and its necessity is not shown» (by script: «MOVES-2D» 3,
  «open» 0 times about it; REFEREE §C add. 2 l. 197 «After L-4 the line contains no «open» about MOVES-2D.»). The body makes NO status
  claim about MOVES-2D and does not present it as a route (REFEREE §C add. 2 l. 199 «RESULTS should not cite this line as a route via
  MOVES-2D.»): apart from describing the line and its history, its only sentences about it say that it is not claimed and that its
  status is not part of this result (Claims (b), Not signed, Honest limits (iii)); the body does not cite L50. The packet's status
  labels for it (l. 9 and l. 77-78) and its §6 lane DATA on it (l. 194-197) are not landed (Not signed; G-11). The line's sufficiency
  sentence is MOVES-EQUIV's conditional as signed, and both referees MATCHED it (REFEREE §C add. 2 l. 192-194; REFEREE-2 Add. 3 l.
  162-164). CHECKER: confirm no body sentence states or implies a status of MOVES-2D, and none presents it as a route.
- G-P, PLACEMENT (FLAG for the Lead). The entry goes after the last landed R-entry before «**Erratum E-1**»: at this fill R114 (R115 is
  not landed). The landing script finds the place by content (the line before «**Erratum E-1**», which must be blank and preceded by an
  R-entry) and asserts which R-entry precedes; the GAPS UPDATE is appended after the last UPDATE on l. 11 (R114's now, R115's once R115
  lands). Addendum (9) gives both simulations: (A) R116 after R114 on RESULTS / GAPS as they are; (B) R115 landed first from
  docs/agents/R115-draft.md as it stands (fc665614, the first fill that C128 failed; slice and UPDATE as its Addendum (3) states), then
  R116 after R115. R115's second fill will change its block length, not R116's block or UPDATE, which do not depend on R115's text. In
  both: a pure insertion, GAPS l. 11 "|" 76 → 76.
- G-U, THE UPDATE RULE (FLAG; no new adaptation). L-4 has five labelled clauses (REDUCE-XI, MOVES-EQUIV, AND-GATE, WINDOW-DOUBLE,
  SEG-WINDOW) and one unlabelled clause, «; and two lane conjectures are DEAD: …», before the date. The DEAD clause gets R111's
  DEAD-clause step (r111_proc of upd111b.py, unchanged in form: cut before the build, put back behind the last label «(SEG-WINDOW)»),
  with this line's separator «; and two lane conjectures are DEAD: » in place of R111's «; and DEAD: ». The DEAD clause holds one «; »
  inside its first parenthesis («while LM = 0; also pass_d3_D3.json»); it is cut out before build() runs, so build() never sees it.
  Everything else is R111's default call (sentinel_build111, the drops of «; G-N5-TIME stays OPEN» and «; not M3, not a step-4 pass, not
  a TARGET.md claim», the «(DATA, » opening, the source parenthesis kept, «. G-N5-TIME stays open.» appended). Cross-check: a direct
  build (each label behind its clause, the DEAD clause after «(SEG-WINDOW)», the tail opened and the two scope sentences dropped by
  string replacement) is equal (True). The default build without the DEAD step gives a different string (False), as for R111. If G-9 (i)
  / (ii) are taken, the same replacements apply once each to the UPDATE (by script; sha1s in Addendum (4)).
- G-2, DEFINITIONS DIFFED (my own diff; the C118 §3 / Erratum E-2 lesson). (o) Premise parenthesis = packet l. 21-40 (G-4). «T the
  number of steps of a run», «Mv_t the movers of step t», «moves(x) the number of steps t with x ∈ Mv_t» = §0 l. 61, 63 (moves with the
  E-2 (E2c) binder); «Z the set of movers that are the Ξ-target of some option» = l. 63-64; «KP_s(x) the option of x with the least key
  under s» = R113's notation (packet l. 38); «KF_x …» = l. 65; «π_s(x) its option of larger Ξ-value under s» = l. 66-68 («the option k
  of x with the larger v_s(x, k)»; larger Ξ-value and larger v are the same order by ENC, a premise); «PF_x …» = l. 68; «v_s(x, k) the
  integer value of option (x, k) under s (R105 ENC)» = l. 66; «on 𝓛^R_d (2d movers on levels 0, …, d − 1)» = R110's definition (l.
  32-34); «F_W(j) … (R113's flip)» = l. 69-71; «T^R(d) the largest T over 𝓛^R_d and all starts» = l. 77 (with the line's global «on
  acyclic Ξ-graphs»); «μ(d) …» = §1 l. 89-90; «a metronome segment … a set [a, b] of D consecutive steps each moving x» = l. 74; «LM the
  number of moves of the movers 2l − 2, 2l − 1 in it» = l. 75 («LM := Σ_(t ∈ [a, b]) #(Mv_t ∩ {u, w})»); «the pair (2l − 4, 2l − 3)» =
  the pair l − 2 of §4 (d). Both referees diffed them (REFEREE l. 82-83 «Definitions diffed against §0: T, Mv_t, moves (E2c), Z, KP_s,
  KF_x, π_s, PF_x, v_s, F_W(j), T^R(d), μ(d), metronome segment, LM all MATCH.»). Claims: REDUCE-XI = §1 l. 81-82; MOVES-EQUIV = l.
  89-91; AND-GATE = §2 l. 98-102 with (b)'s bound l. 101; WINDOW-DOUBLE = §3 l. 116-118; SEG-WINDOW = §4 l. 137-145 ((a), (b) second
  half, (c), (d) second half, (e) last sentence); DEAD = §5 l. 162-177.
  (i) NOTE. L-4's «μ(d) the largest moves(z) over 𝓛^R_d, all starts and all z ∈ Z of level ≥ 1» omits the packet's «(μ(1) := 0)» (l.
    90). At d = 1 the set is empty; the clause «μ(d) ≤ T^R(d) ≤ 3 + (2d − 2)μ(d)» at d = 1 reads T^R(1) ≤ 3 with the convention. No
    claim changes for d ≥ 2. Both referees MATCHED the definition (REFEREE-2 l. 48 «(μ(1) := 0 is consistent: at d = 1, T ≤ 1 + 2 =
    3.)»).
  (ii) NOTE. «T^R(d)» is defined in the line itself, in the words of R110's definition («T^R(d) the largest number of steps over 𝓛^R_d
    and all starts», R110's title l. 11323); the premise parenthesis lists «RESULTS R110's definition of 𝓛^R_d only». Same object,
    defined twice in the same words; nothing rests on R110 beyond 𝓛^R_d.
  (iii) NOTE. «window W = [a + 1, b] of steps» does not state 0 ≤ a < b ≤ T (packet l. 115). Every reading of a window in a run gives
    the same set.
  (iv) NOTE. The line's WINDOW-DOUBLE pass-through clause omits the packet's «Φ_j(s_(t−1)) = 1» (l. 116-117), which is equivalent to «2j
    and 2j + 1 are on different options before the step» on 2-wide ladders (one of two different options is c_j). The line's AND-GATE
    omits (a)'s second sentence (l. 99) and (b)'s window sentence (l. 100-101); SEG-WINDOW omits (a)'s «so D − 1 ≤ F_[a+1,b](l − 1)»,
    (b)'s «D ≤ 1 + LS + PT», (d)'s window-length form and (e)'s first sentence. All signed; not stated by L-4, so not landed as separate
    items.
- G-4, PREMISE ROUTE (the C115 E-1 class): CLEAN (prem116.py on RESULTS 555d41bd). L-4's premise parenthesis: «premise: R104's
  definition of the model only, no theorem of R104 used; RESULTS R105's ENC, LOCAL, MONO, XI-NEW and RISE only; RESULTS R110's
  definition of 𝓛^R_d only; and RESULTS R113's ALIGN and F0 only» = packet l. 21-40. Hits, whitespace normalised (packet l. 23-40, each
  «…» as quoted there): ENC with its label (265 characters) 3: R105's title l. 10155 (the source), R113's body l. 12254-12255 and R114's
  body l. 12546-12548 (both quote R105); LOCAL (107) 1, l. 10155; MONO (69) 3: l. 10155, R113 l. 12256, R114 l. 12548-12549 (quotes);
  XI-NEW (169) 2: l. 10155, R114 l. 12549-12550 (quote); RISE (136) 2: l. 10155, R114 l. 12550-12551 (quote); «at any degree» (13) 24
  lines in R105, R107-R111, R113, R114: in R105's title it occurs once (position 503, before «(ENC)» at 518 and before «and at degree ≤
  2 only» at 1751, so all five items stand «at any degree»; REFEREE-2 l. 30-31 «XI-NEW, RISE, ENC, LOCAL, MONO all before «and at degree
  ≤ 2 only», so at any degree»); R110's 𝓛^R_d wording (191) 4: R110's title l. 11323 (the source), R112 l. 12020-12021, R113 l.
  12257-12259, R114 (quotes of R110); R113's ALIGN (281) 1, R113's title l. 12152; F0 (64) 1, l. 12152; R113's notation «KP_s(x) the
  option of x with the least key under s» (50) 3: R111's title l. 11598, R113's title l. 12152, R114's title l. 12394 (each entry
  defines it in the same words; the packet takes it «as in R113»); «c_l(s) …» (90) 1, «γ_l(j) := …» (80) 1, «F(l) …» (61) 1, all R113's
  title. R104: the packet restates the definition in §0 (l. 47-61, «RESULTS R104's definition, as restated in P-IDEAL-ALIGN §0»); R104's
  own wording (861 characters, as quoted by P-TR3 §1, r115/R104Q.txt) 1 hit, R104's title l. 9864; REFEREE-2 l. 34-36 matched §0's step
  rule against it. Use: ENC, MONO in AND-GATE (c); LOCAL in SEG-WINDOW (e); XI-NEW, RISE in REDUCE-XI; ALIGN in WINDOW-DOUBLE and
  SEG-WINDOW; F0 in MOVES-EQUIV, WINDOW-DOUBLE (via (b)'s base) and SEG-WINDOW (c) at l = 1. Not used (packet l. 41-44): every other
  R105 item; R106-R112; R111's CASCADE; R113's KP-MOVE, PAIR-DOUBLE, MOVES, T-BOUND, PATH-RISE; R114 (packet l. 43, «the signed but not
  landed packet P-IDEAL-RISE (R114 draft: its MOVE-RISE is not used)»: R114 has since landed and is still not used; G-11). Erratum E-2
  does not bear (G-5). REFEREE l. 21-25 «Premise quotes are FOUND verbatim on b876c884:»; REFEREE-2 l. 28-30 «18/18 verbatim».
- G-C, OVERLAP WITH LANDED R105, R110-R114 (NOTE for the Lead and CHECKER; the brief's no-double-claim check; my reading). Nothing in
  L-4 is a clause of a landed entry restated as new, and nothing landed is claimed again; the body names each overlap once (Claims,
  Honest limits (viii)). (1) AND-GATE's «moves(x) ≤ 1 + min(KF_x, PF_x)» contains R105's KEYFLIP «moves(x) ≤ 1 + KF_x» (degree 2, with
  the E-2 (E2c) binder) and R113's KP-MOVE («(KP-MOVE) at any degree elsewhere, a mover x of degree 2 that moves at step t moves to
  KP_(s_t)(x), so moves(x) ≤ 1 + KF_x»); the PF_x half and the iff of (a) are new; R114's KEY degree-2 clause («a mover of degree 2 that
  moves at step t moves to KP_(s_t) and was not on it before») is the «only if» direction's KP part. (2) WINDOW-DOUBLE (b) on W = [1, T]
  is R113's PAIR-DOUBLE («(PAIR-DOUBLE) on 𝓛^R_d, F(l) ≤ 2F(l − 1) + 2 for 1 ≤ l ≤ d − 1»; packet l. 133 «W = [1, T] is PAIR-DOUBLE
  itself»); the window form is new. WINDOW-DOUBLE (a) is, on 𝓛^R_d, R111's CASCADE («at every step at which two distinct movers p, q of
  one level l flip, p or q moves, or l ≥ 1, neither moves, their current W-targets w_p ≠ w_q and (w_p, w_q) flips at the same step»; on
  𝓛^R_d the W-targets of 2j and 2j + 1 differ iff they are on different options), re-proved here from ALIGN (packet l. 41) and stated
  with «before the step»; the line restates it as a clause of WINDOW-DOUBLE, a restatement of a landed fact, not a new claim (CHECKER:
  note; the C116 / C125 precedent of naming such restatements in the body). (3) SEG-WINDOW's segment bounds are window forms of R113's
  MOVES («moves(x) ≤ 1 + F(l − 1)») and R111's LADDER («moves(x) ≤ 1 + F(lev(x) − 1)»), restricted to a segment. (4) AND-GATE (c) (a π
  change raises the new π option's value) is not R114's MOVE-RISE (a move raises cv of the mover) nor R111's RETURN (between two moves
  the other option's Ξ-target rises); different statements. (5) REDUCE-XI (T ≤ 1 + Σ_(z ∈ Z) moves(z)) is a counterpart of R114's
  RISE-EQUIV («T ≤ 1 + Σ_(x,k) R(x, k)»), counting moves of Ξ-targets instead of rises of options; R114's MOVE-RISE («R(x, k) ≥ moves(z)
  when the Ξ-target of (x, k) is the mover z») goes the other way, so neither implies the other. (6) MOVES-EQUIV uses only the
  definition of T^R(d); with R112 (T^R(3) = 8) and R113's T-BOUND (T^R(d) ≤ 2^(d+2) − 2d − 4) its lower half gives μ(d) ≤ those bounds;
  the line does not state that. (7) DEAD-LEV's 7 is the most R113 allows at level 2: R113's MOVES, PAIR-DOUBLE and F0 give moves ≤ 1 +
  F(1) ≤ 1 + 2F(0) + 2 ≤ 7 for a level-2 mover (REFEREE-2 F-4, l. 121-122); consistent, not claimed by the line.
- G-3, STRICT SYMBOL TEST (notes). s, t, x, z, k, j, l, a, b, W, D are bound in their clauses; «d» is free in 𝓛^R_d (each clause «on
  𝓛^R_d»); «N» does not occur; «μ» and «T^R» are defined in the line; «X» (the exit) is R104's; «ε» does not occur; «LM» is defined;
  «LS» and «PT» do not occur; «MOVES-2D» is named and glossed («a bound of 2d on the moves of every Ξ-target») and marked «not claimed»;
  «R113's flip» names R113's definition of a flip (R113's title: «a change between s_(t−1) and s_t of the order of the keys of their
  current options»).
- G-5, ERRATA (note). Erratum E-1 concerns R97-R100 counts. Erratum E-2 corrects R105's CHAIN-BACK binder (E2a), TOP-MONO's RANK_t (E2b)
  and KEYFLIP's moves(x) (E2c); L-4 uses R105's ENC, LOCAL, MONO, XI-NEW and RISE, none of them corrected, and defines moves(x) with the
  E2c binder (packet l. 29-31). Note E-3 concerns R110's CONDITIONAL DEAD; L-4 uses R110's definition of 𝓛^R_d only. Not bearing.
- G-6, NAMES (by script on RESULTS 555d41bd / GAPS 3c4ff44d; note; C116 G-2's remedy). 0 times in RESULTS and GAPS: «C129»,
  «P-IDEAL-MOVES», «REDUCE-XI», «MOVES-EQUIV», «AND-GATE», «WINDOW-DOUBLE», «SEG-WINDOW», «BURST-2», «DEAD-SEG», «DEAD-LEV»,
  «metronome», «movescheck», «pass_d5_D5», «m4_z4_r7», «PF_x», «μ(d)», «F_W(», «π_s». Same names, other meanings: «R116» 5 lines in
  RESULTS (l. 13252-13284, L-RED's box R116 in the Dead-ends section, e.g. «docs/red/R116-sf-exponential.md»); «LM» only inside
  «X_LM_s4a» (an older entry's counter name); «MOVES» is R113's lemma (MOVES) (moves(x) ≤ 1 + F(l − 1)), not MOVES-EQUIV; «MOVES-2D»
  occurs twice in RESULTS, both in R114 («the conjectures RISE-2D (…) and MOVES-2D are not claimed»): the same lane conjecture, not
  claimed there either; «(LOCAL)» is R105's (a premise, same meaning); «F(l)» is R113's (same meaning, F_W is its window form). One body
  sentence (Honest limits (vii)).
- G-7, L41 (the C109 E-1 class): not triggered (my reading). The proofs are L-NEW successor 57's (packet l. 2, 5-7); the fixes entries
  carry no proof («This entry carries no proof.», entries 1-3); the referees' simulators (REFEREE's t3r_sim.py, REFEREE-2's r2moves.py)
  are checking tools. Fix texts that came from referees are line wording only: R1 is «REFEREE-2's text verbatim» (entry 1, l. 26), R6 is
  REFEREE's MV-C1 text (entry 2, l. 69; REFEREE §C add. 1 l. 153-154), R8-R9 are the Lead's (entry 3, l. 100-101). Nothing
  referee-written is a proof step of the entry.
- G-8, THE SCOPE TAIL (NOTE). «a STRUCTURE / EQUIVALENCE statement inside the IDEAL model; bounds nothing polynomially; MOVES-2D is not
  claimed (its status is not part of this result; here μ(d) is shown equal to T^R(d) up to a factor 2d − 2 and an additive 3, so
  MOVES-2D is sufficient for a polynomial bound on T^R, and its necessity is not shown: a polynomial bound on T^R gives only μ
  polynomial); Ξ-cyclic genomes and genomes outside 𝓛^R_d (outside REDUCE-XI and AND-GATE) are not covered; G-N5-TIME stays OPEN; not
  M3, not a step-4 pass, not a TARGET.md claim»: true. «EQUIVALENCE» is MOVES-EQUIV («μ is polynomial in d iff T^R is»), an equivalence
  of two open statements, not a bound (fixes entry 1 l. 8-13, W-1 note). «shown equal to T^R(d) up to a factor 2d − 2 and an additive 3»
  reads «μ(d) ≤ T^R(d) ≤ 3 + (2d − 2)μ(d)». The sufficiency sentence is the conditional of MOVES-EQUIV (G-S). «outside REDUCE-XI and
  AND-GATE» keeps their any-degree scope apart. Both referees MATCHED the tail (REFEREE §C add. 2 l. 191-197; REFEREE-2 Add. 3 l.
  162-165).
- G-10, LEAD READINGS AND RULINGS (the C111 E-1 class): L-4 cites no Lead reading and no ruling (by script: «Lead reading» 0, «L50» 0).
  L50 (DECISIONS l. 440-449, DECISIONS-INDEX l. 45) governs this landing's scope (G-S); the entry does not cite it and states nothing
  about MOVES-2D beyond «not claimed» and «its status is not part of this result». Fixes entry 3 cites the ruling as «Lead reading,
  01:16Z» (l. 87), a relay stamp that precedes L50's DECISIONS stamp «2026-11-07 01:42Z by date -u» (D-1); both referees verified L-4
  without opening L50 (REFEREE §C add. 2 l. 182-184 «I could not open it: 6ca995ed is not an object in my fetch»; REFEREE-2 Add. 3 l.
  166-168 «I did not open L50; the verdict does not depend on it») and opened it afterwards in post-notes that keep their verdicts
  (REFEREE c011995c l. 205-206 «Its (2) agrees with the verdict above.»; REFEREE-2 6924e140 l. 172-174 «Addendum 3's verdict stands.»).
  D-6: REFEREE's post-note is stamped «02:4xZ», its commit c011995c is 2026-11-07T02:13:40Z. L49 (ISO scope of W-ONLY) does not bear: no
  W-ONLY, and MOVES-EQUIV is about T^R over all of 𝓛^R_d (REFEREE-2 l. 37-38).
- G-11, STALE LANE TEXT (notes; nothing here lands as current). (i) Packet l. 9 «CONJECTURE MOVES-2D and G-N5-TIME stay OPEN.» and l.
  77-78 «CONJECTURE MOVES-2D (lane, box 181, OPEN)»: the MOVES-2D labels are not used by this entry (fixes entry 3's wording note l.
  91-92 says so); the entry states no status for MOVES-2D (G-S). (ii) Packet l. 43 calls P-IDEAL-RISE «the signed but not landed packet»
  (R114 draft): R114 is landed (RESULTS l. 12394); it is still not a premise. (iii) Packet l. 47 «RESULTS R104's definition, as restated
  in P-IDEAL-ALIGN §0»: P-IDEAL-ALIGN is R113. (iv) Packet l. 181-182: check.sh pins «this packet, its line L-1, the tool, its output
  and the four instance files»; at fd5c163f it also pins the fixes file and L-2-L-4 (G-12). (v) Packet §6 l. 194-197 «Lane DATA (not to
  sign; from L-RED, not landed, …)» about moves of Ξ-targets: not in the entry.
- G-12, SHA1 PINS IN check.sh (the C110 F-1 / C116 G-3 class): present. Block «P-IDEAL-MOVES» (l. 935-942 at fd5c163f) compares
  movescheck.py's output with the frozen movescheck.out, asserts the counter line, the three DEAD-SEG lines and the DEAD-LEV line, and
  pins packet 5ce2947d, L-1 819c5815, tool 8153717b, output 48740209, instances 8bca9764 3bf6a4a4 16be2e59 7c158e2f, fixes 510152da, L-2
  f3692aaa, L-3 d3983c68, L-4 73c16d1e. It does not pin box150/check.py (Gen); a change to Gen would change the output and fail the
  diff.
- G-13, THE REFEREES' ROUNDS (note; state on file at this fill). L-1 (819c5815): REFEREE (c82fac5c) every item SIGN, L-1 «MATCHES;
  optional MV-L1» (verdict table l. 18); REFEREE-2 (38a2adb6) every item SIGN, no gap, L-1 «**MATCHES after W-1, W-2**» (l. 23). Round 1
  (fixes entry 1, 9995f5a2: W-1, W-2, W-3, MV-L1, L-2): REFEREE §C (72f4b2f3) «L-2 MATCHES the byte test.», «L-2 does NOT YET MATCH in
  meaning: one required replacement, MV-C1 above.» (l. 133-134); REFEREE-2 Add. 1 (f71fdbdb) «Verdict: fixes **CORRECT**; **L-2
  MATCHES**» (l. 136). Round 2 (fixes entry 2, d7b96be8: MV-C1 as R6, L-3): REFEREE §C add. 1 (e7047ace) «Verdict: fixes entry 2 is
  CORRECT. L-3 MATCHES the byte test and in meaning. All packet items stay SIGNED.» (l. 156); REFEREE-2 Add. 2 (0fdc26d4) «**MV-C1: I
  agree; it corrects my miss.**» (l. 143), «Verdict: entry 2 **CORRECT**; **L-3 MATCHES**» (l. 148). Round 3 (fixes entry 3, fd5c163f:
  R8-R10, L-4): REFEREE §C add. 2 (2fe03939) «Verdict: fixes entry 3 is CORRECT. L-4 MATCHES the byte test and in meaning. All packet
  items stay SIGNED.» (l. 204); REFEREE-2 Add. 3 (88c0c6d6) «Verdict: entry 3 **CORRECT**; **L-4 MATCHES** the packet with fixes entries
  1-3» (l. 171). Post-notes after L50 was pushed (REFEREE c011995c, REFEREE-2 6924e140): both opened L50 and keep their verdicts (G-10).
  Nothing is open at either referee: no gap was listed (REFEREE-2 l. 24 «No statement is REFUSED. No gap is listed»), and neither has an
  announced addendum.
- G-14, THE FIXES FILE (note). Three entries, append-only (each referee byte-checked the prefix: REFEREE §C add. 1 l. 140-141, §C add. 2
  l. 178-179; REFEREE-2 Add. 2 l. 139-140, Add. 3 l. 157-158; my check: each file at d7b96be8 / fd5c163f starts with the previous one).
  No entry changes a statement, a proof or DATA (entry 1 l. 6-7 «No statement, proof or DATA of the packet changes. The line changes
  only (L-2 below). This entry carries no proof.»; entries 2 and 3 the same in substance). Each gives its line as exact old → new
  strings, each found once (my wdiff116.py: L-1 with R1-R5 = L-2, L-2 with R6-R7 = L-3, L-3 with R8-R10 = L-4, all True). The source
  note names the file (G-1).
- G-T, THE TAG (note). «[refereed-only]»: every item is a hand proof signed by both referees; the two DEAD items rest on instances
  computed by machine (the lane's movescheck.py on box150 Gen) and recomputed by both referees with their own simulators (REFEREE §2,
  «my simulator t3r_sim.py; no lane code»; REFEREE-2 r2moves.py, «no lane code imported»). No Lean, no certificate.
- CLEAN AT L-4 (the pre-check against CHECKER's recurring items, by script on 73c16d1e):
  C106 E-1 (old line as current): L-4 is the current line; no L-5 exists (docs/new/P-IDEAL-MOVES-line-L5.txt absent at fd5c163f);
  L-1-L-3 appear only in the line history.
  C113 E-1 (title «verbatim» after an insertion): no insertion; the title is byte-equal to prefix + L-4 + fill (Addendum (2)).
  C113 E-2 (trunk status that goes stale): the body has no trunk statement (header).
  C114 Add. 1 E-1 (UPDATE date): <DATE> placeholder.
  C115 E-1 (premise route): G-4.
  C110 F-1 / C116 G-3 (pins): G-12.
  C111 E-1 (stale Lead-reading statements): G-10.
  C116 G-2 (name clash): G-6, one body sentence.
  C117 E-1 / E-2 (scope; instance under-specified): G-9 (ii) flagged (two DEAD-SEG starts); the instances named by path and sha1 in the
  body.
  C118 E-1 (stale status sentence): no status of MOVES-2D (G-S); R110-R114 named as landed; no sentence about R115.
  C118 §3 / Erratum E-2 lesson (definitions diffed): G-2.
  C120 §5 / C121 E-1 / C122 E-2 / C124 E-1 / C125 E-1 / C127 E-1 / C128 class (DATA unit, set and scope against the counter code): G-9;
  two clauses flagged ((i), (ii)).
  C122 G-0 (parentheses): 71 / 71, depth never negative (G-1).
  C122 E-3 (source note): CLEAN (G-1).
  C123 E-1 (lane label or packet name before the claims): none (G-1).
  C123 E-2 (stale referee state): G-13.
  «|»: 0 in L-4, 0 in the entry block, 0 in the UPDATE (by script, Addendum (3)).
- G-1, TITLE SHAPE AND SOURCE NOTE: CLEAN (my script). L-4 is one line, 4,428 characters, 4,598 bytes with the newline, 869 whitespace
  tokens, 71 «(» / 71 «)», depth never negative, final depth 0 (C122 G-0: met); 0 "|"; two guillemet pairs (the two DEAD conjectures);
  one « — », with its own date parenthesis «(2026-11-06)», «2026» once. It begins «In the IDEAL model of RESULTS R104»: no packet name
  and no lane label before the claims (C123 E-1: met); lane names occur inside the claims only as provenance («L-RED's
  experiments/red/r213/out/m4_z4_r7.json», as R110's and R112's «L-RED's R197 convention»), and the packet name and «L-NEW successor 57»
  only in the source note. Source note «(P-IDEAL-MOVES, docs/new/P-IDEAL-MOVES.md with its fixes entries 1-3,
  docs/new/P-IDEAL-MOVES-fixes.md; L-NEW successor 57)»: the packet carries every proof (l. 6-7 «This packet carries every proof in full
  and is checked against this text only; no other file carries a proof of a statement below.»); the fixes file carries none and is
  named. Every proof-carrying file is named (C122 E-3: met). The title is "### R116 [refereed-only] " + L-4 + the fill ", CHECKER PASS
  (docs/checker/C129.md, checker PENDING)", nothing inserted.
(0) PLACEMENT. R116 goes DIRECTLY AFTER the last landed R-entry, before «**Erratum E-1**» (G-P). docs/RESULTS.md at the local trunk (=
  origin trunk 6ca995ed for this file) has sha1 555d41bd85b8ea52a1e57459c0a4fe0fcb7f6cc1, 13,306 lines (wc -l), last changed by b6d1484b
  (R114's landing). «### R114» is l. 12394 (entry l. 12394-12695, l. 12696 blank); «**Erratum E-1**» is l. 12697; «**Erratum E-2**» is
  l. 12710; «**Note E-3**» is l. 12738; «## Dead ends (kept;» is l. 12769. PROPOSED (R102's to R115's layout): (A) while R115 is not
  landed, insert R116's entry after l. 12696 (R114's blank line), with one blank line after it; (B) once R115 has landed, insert it
  after R115's block and its blank line. Either way the R-entries stay contiguous and the errata and Note E-3 follow them. "### R116"
  occurs 0 times in RESULTS and GAPS. GAPS has sha1 3c4ff44d1b822110d9bfd0d1a2d8661ea6b5361e, 23 lines, last changed by b6d1484b.
(1) TITLE. The title is the line file docs/new/P-IDEAL-MOVES-line-L4.txt (l-new fd5c163f05dab991101fdb4e6da6a789f72bef73,
  2026-11-07T01:16:07Z, the file's only commit, sha1 73c16d1e2b009ff2e3d774a904e4462be0874db1, 4,598 bytes with the newline; byte-equal
  at the l-new head), verbatim: one line, no heading marker, no outer quotes, no final period. NOTHING is stripped and NOTHING is
  inserted: the heading is the level-3 marker, then "R116 [refereed-only] ", then the file without its newline, then the fill ", CHECKER
  PASS (docs/checker/C129.md, checker PENDING)" (as R90-R115). Built by script (fill116.py: assert the sha1 73c16d1e…, equality with the
  blob at fd5c163f and at the l-new head, one line, no marker, one « (2026-11-06) — », no "|"; prepend, append) and re-checked after
  writing this file (chk116.py): equal, byte for byte. Heading: 4,507 characters, 4,676 bytes; sha1 of the heading line without its
  newline 58a529893324b2d26f5af909f57e7b62e3c49152; it is l. 453 and the only «### R» line of this file.
(2) LINE HISTORY: four lines, each the previous one with exact replacements named in a fixes entry (my wdiff116.py applies the fixes
  entries' own old → new strings, each found once: True for each step). L-1 819c58159100d77ec509348345cfd1a641a6f9e7 (d86adc86, frozen
  with the packet; 4,313 bytes, 68 «(» / 68 «)»): REFEREE MATCHES with optional MV-L1; REFEREE-2 required W-1 and W-2, optional W-3. L-2
  f3692aaa (9995f5a2; 4,495 bytes, 71 / 71): fixes entry 1, R1 (W-1, REFEREE-2's text), R2 (W-2), R3 (W-3), R4 (MV-L1), R5 (source
  note). L-3 d3983c68 (d7b96be8; 4,567 bytes, 71 / 71): fixes entry 2, R6 (MV-C1, REFEREE §C: «not necessary» unproved), R7 (source
  note). L-4 73c16d1e (fd5c163f; 4,598 bytes, 71 / 71): fixes entry 3, R8 «(the open conjecture MOVES-2D)» → «(the lane conjecture
  MOVES-2D, not claimed here)», R9 «MOVES-2D is not claimed (it is an open conjecture; here» → «MOVES-2D is not claimed (its status is
  not part of this result; here», R10 the source note; my token diff L-3 → L-4 finds 5 hunks, all inside these three places. No
  replacement changes a statement or a hypothesis: R1 and R6 reword the tail's not-claimed sentence, R2 and R3 make two clause wordings
  exact against the packet (§3 (a), §4 (e)), R4 labels an arithmetic consequence inside the DATA parenthesis, R8 and R9 remove a status,
  R5, R7 and R10 are source notes. So the title is L-4, and L-1-L-3 are history.
(3) THE LINE AT BOTH REFEREES. REFEREE, docs/referee/R-P-IDEAL-MOVES.md: successor 24's report c82fac5c (2026-11-06T21:43:56Z, new file,
  91 lines, sha1 0e62923bfb05d4f1420762c375c94249df706904), successor 25's §C 72f4b2f3 (2026-11-06T23:54:36Z, 136 lines, d9b774fa…), §C
  add. 1 e7047ace (2026-11-07T00:34:14Z, 174 lines, c350dad5…), §C add. 2 2fe03939 (2026-11-07T01:45:22Z, 204 lines, sha1
  ad6cb02e6212ecc7c0a1e88407cef05d455a83a3), post-note c011995c (2026-11-07T02:13:40Z, 206 lines, sha1
  98338ae477a109f793fbb2447ee408c3154db463; each push keeps the previous file as its prefix, by script): «Verdict: fixes entry 3 is
  CORRECT. L-4 MATCHES the byte test and in meaning. All packet items stay SIGNED.» (l. 204). REFEREE-2,
  docs/referee-2/R2-P-IDEAL-MOVES.md: successor 29's report 38a2adb6 (2026-11-06T23:12:13Z, 122 lines, ddcbdc27…), Add. 1 f71fdbdb
  (23:54:08Z, 136 lines), Add. 2 0fdc26d4 (2026-11-07T00:34:22Z, 154 lines), Add. 3 88c0c6d6 (01:45:52Z, 171 lines, sha1
  a7677cbb2431394223ca0c5a954d3314f6ccef1b), post-note 6924e140 (2026-11-07T02:09:17Z, 174 lines, sha1
  5be0b2ee1c18ff7ae011d756ebd8181d3412d212; prefix-kept, by script): «Verdict: entry 3 **CORRECT**; **L-4 MATCHES** the packet with
  fixes entries 1-3 (Opus 5.5, D1). Statement verdicts unchanged (all SIGN).» (l. 171). Both MATCH L-4, each by its own byte test of
  R8-R10 on L-3.
(4) CLAIMS SIGNED = the items below, each SIGN in BOTH referees' verdict tables (REFEREE "## 0. Verdicts" l. 9-18; REFEREE-2 "##
  Verdicts" l. 13-25), unchanged in all later rounds (REFEREE l. 135, 156, 204; REFEREE-2 l. 136, 148, 171); the cells are the reports'
  words: §1 REDUCE-XI and Corollary MOVES-EQUIV: REFEREE l. 12 «SIGN»; REFEREE-2 l. 16-17 «**SIGN** (Opus 5.5, D1)». §2 AND-GATE
  (a)-(c): l. 13; l. 18. §3 WINDOW-DOUBLE (a), (b) incl. BURST-2: l. 14; l. 19. §4 SEG-WINDOW (a)-(e): l. 15; l. 20. §5 DEAD-SEG (c ≤ 4)
  and DEAD-LEV: REFEREE l. 16 «SIGN (instances recomputed with my own simulator)»; REFEREE-2 l. 21-22 «**SIGN** (Opus 5.5, D1)
  (recomputed by my own simulator)». No gap is open at either referee (REFEREE-2 l. 24; REFEREE lists none).
Clause checks (L-4 against the packet; G-2): REDUCE-XI = l. 81-82; MOVES-EQUIV = l. 89-91; AND-GATE = l. 98, 101, 102; WINDOW-DOUBLE =
l. 116-118; SEG-WINDOW = l. 137-145; DEAD = l. 162-177. Nothing in L-4 is wider than signed.
Signed by both, NOT stated by L-4 as separate items: AND-GATE (a)'s second sentence and (b)'s window sentence; WINDOW-DOUBLE (a)'s Φ_j
clause; SEG-WINDOW (a)'s D − 1 ≤ F_[a+1,b](l − 1), (b)'s D ≤ 1 + LS + PT, (d)'s window-length form and (e)'s π-change sentence (G-2
(iv)). Not signed, so NOT landed: §6 (DATA, lane DATA, EXCLUDED, TARGET diff; «DATA / READING (not to sign)», table l. 19).
(5) OTHER TEXTS THE ENTRY DEPENDS ON: RESULTS R104's definition of the IDEAL model (title l. 9864; no R104 theorem); RESULTS R105's ENC,
  LOCAL, MONO, XI-NEW and RISE (title l. 10155); RESULTS R110's definition of 𝓛^R_d (title l. 11323); RESULTS R113's ALIGN and F0 with
  its notation (title l. 12152). Nothing else for a signed statement. The DEAD items rest also on the machine computation of their runs
  (box150 Gen in movescheck.py; both referees' own simulators). The sources docs/new/N5-MOVES-box185.md and
  docs/new/N5-METRONOME-box186.md (packet l. 5-6) are history.
(6) PREMISE LABELS (stale-label test; RESULTS and GAPS at 6ca995ed's version). RESULTS labels in L-4 (by script): «R104» 3, «R105» 2,
  «R110» 1, «R113» 2. Each exists: R104 l. 9864, R105 l. 10155, R110 l. 11323, R113 l. 12152. No Lead reading and no other RESULTS label
  is cited. G-N5-TIME open (GAPS l. 11).
(7) SYMBOL TEST: G-3.
(8) FIXES AND STATUS NOTES (docs/new/P-IDEAL-MOVES-fixes.md, L-NEW successor 57, append-only, three entries, three commits): sha1
  510152dab3512980e5e739710f46ff14797edf87, 116 lines, 9,674 bytes. Entry 1 (l. 3-55; 9995f5a2, 2026-11-06T23:36:29Z), entry 2 (l.
  57-84; d7b96be8, 2026-11-07T00:16:43Z), entry 3 (l. 86-116; fd5c163f, 2026-11-07T01:16:07Z). Verdicts: REFEREE §C l. 93-136, §C add. 1
  l. 138-174, §C add. 2 l. 176-204; REFEREE-2 Add. 1 l. 124-136, Add. 2 l. 138-154, Add. 3 l. 156-171.
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-4 states no CONJECTURE as claimed («P-IDEAL-MOVES», «REDUCE-XI», «MOVES-EQUIV» occur 0
  times in GAPS); its two DEAD items are lane conjectures killed inside the line (no Dead-ends row, (14)). A line-11 UPDATE is proposed
  at the end, to go AFTER the last UPDATE on l. 11 (at this fill R114's «UPDATE 2026-11-06 21:57Z: RESULTS R114 (P-IDEAL-RISE; CHECKER
  C127 e3269b0b) [refereed-only] LANDED: …», ending «G-N5-TIME stays open.» before the row's closing « |»; R115's once R115 lands; l. 11
  holds 76 "|" and 49 «UPDATE 2026-»), as a pure insertion with one separating space. BUILT FROM L-4 (scratch upd116.py = r115/upd115.py
  l. 1-337 unchanged: its 18 controls, R97's to R114's LANDED UPDATEs rebuilt from their lines byte for byte (True ×18), and its state
  assertion that R114's UPDATE is the last on l. 11 (True); then R116). R116: the R111 procedure (sentinel_build111 of upd111.py,
  unchanged, default drops) on L-4 with the DEAD clause cut and put back behind «(SEG-WINDOW)» (G-U): 5 labels, each found once after
  the start «with LM the number of moves of the movers 2l − 2, 2l − 1 in it: », in order, moved behind their clauses; « (2026-11-06) — »
  → «: »; the DATA parenthesis before the source parenthesis opened as «; DATA, …»; «; G-N5-TIME stays OPEN» and «; not M3, not a step-4
  pass, not a TARGET.md claim» dropped; the source parenthesis kept; «. G-N5-TIME stays open.» appended. L-4 holds no "|", so no
  replacement list. Checked by script: one line, 0 "|", one «<DATE>», one «<HH:MM>», one «<checker>», 4,632 bytes, 4,465 characters, 868
  tokens, 70 «(» / 70 «)», balanced; «2026-11-06» 0 times; token multiset diff against L-4 = the head, the five moved labels, «(DATA,»
  opened, the two dropped scope sentences, « — » and the final sentence (upd116.out). Head «UPDATE <DATE> <HH:MM>Z: RESULTS R116
  (P-IDEAL-MOVES; CHECKER C129 <checker>) [refereed-only] » («P-IDEAL-MOVES» 0 times in GAPS); <DATE> = the landing date.
(10) DATA of record = packet §6 (l. 179-202), NOT signed; L-4's DATA parenthesis states its counts per statement, with the flags of G-9.
  Re-run at this fill: Re-runs (a)-(c) in the header (PASS; my splits).
- PASS line: «P-IDEAL-MOVES: movescheck 0 violations, 4 DEAD instances re-run (output = frozen movescheck.out); pins packet 5ce2947d,
  line L-1 819c5815, tool 8153717b, output 48740209, instances 8bca9764 3bf6a4a4 16be2e59 7c158e2f, fixes 510152da, line L-2 f3692aaa,
  line L-3 d3983c68, line L-4 73c16d1e: PASS» (rc 0).
- movescheck raw (byte-equal to movescheck.out; the block's diff and my g9split.py): «RX 0 AGA 0 AGB 0 AGC 0 SWA 0 SWB 0 SWC 0 SWD 0 SWE
  0 WPD 0», «INFO files 208 runs 63223 steps 140395 RXEQ 59502 segments 225917 windows 1288162 maxD 9», «DEAD-SEG
  box186/out/pass_d5_D5.json start 0101010110 z 9 level 4 Xi-target True T 5 moves of z at steps [1, 2, 3, 4, 5] LM 0», «DEAD-LEV
  box187/inst/m4_z4_r7.json start 10111010 mover 4 level 2 Xi-target True moves 7 T 8» (and the pass_d3_D3 / pass_d4_D4 lines: z 5,
  steps [1, 2, 3]; z 7, steps [1, 2, 3, 4]; LM 0).
- My splits (g9split.out, deadstart.out): G-9 (i), (ii) and the notes.
NOT re-run: the referees' simulators t3r_sim.py and r2moves.py (their reports and outputs read, not re-run); L-LOWER's, L-NEW box 188's
and L-RED's MOVES-2D material (not opened: not part of this entry); check.sh's other blocks and scripts/verify.sh.
(11) Discrepancies, recorded for CHECKER, no verdict affected (D-6 is in G-10): D-1 fixes entry 3 «Lead relay 01:16Z of fix round 3,
  Lead reading» (l. 86) against L50's DECISIONS stamp «2026-11-07 01:42Z by date -u» and its commit 6ca995ed (01:42:08Z): the relay
  preceded the written reading; the line's text does not depend on it (both referees). D-2 packet l. 2 «Lead brief BOX 187 (2026-11-06
  21:07Z)» and l. 4 «Written 2026-11-06 from 21:08Z» against the freeze d86adc86 (21:11:22Z): stamps of messages, not verifiable from
  the repository. D-3 REFEREE's optional MV-L1 (verdict table l. 18, «MATCHES; optional MV-L1») and REFEREE-2's D-2 / D-3 attribution
  notes: MV-L1 = REFEREE-2's D-2 first half (taken as R4); D-3 (SWD's docstring label) left in the frozen tool (fixes entry 1 l. 20-22).
  D-4 fixes entry 2 labels R6 «the Lead's text verbatim» (l. 69); REFEREE §C add. 1 l. 153-154: «The text is REFEREE 25's MV-C1, relayed
  by the Lead.». D-5 REFEREE's report is by successor 24, its §C and both addenda by successor 25 (l. 93, 138, 176): one referee lane,
  two successors.
(12) Excluded: packet §6 (DATA counts as statements, lane DATA, EXCLUDED readings, TARGET diff); MOVES-2D in every form (G-S); the
  readings of boxes 185-186; box 188 and later lane work. Not part of this entry.
(13) Commits: lane (claude/l-new): d86adc86 (2026-11-06T21:11:22Z; freeze: packet 5ce2947d (202 lines), L-1 819c5815, movescheck.py,
  movescheck.out, box187/inst/m4_z4_r7.json, check.sh block) → 9995f5a2 (2026-11-06T23:36:29Z; fixes entry 1, L-2, pins) → d7b96be8
  (2026-11-07T00:16:43Z; entry 2, L-3, pins) → fd5c163f (2026-11-07T01:16:07Z; entry 3, L-4, pins, handover; box 188 files, outside
  movescheck's corpus). REFEREE (claude/referee): c82fac5c → 72f4b2f3 → e7047ace → 2fe03939 → c011995c (post-note). REFEREE-2
  (claude/referee-2): 38a2adb6 → f71fdbdb → 0fdc26d4 → 88c0c6d6 → 6924e140 (post-note). CHECKER: docs/checker/ ends at C127 (1c4ba1c3).
  Trunk: see the header.
(14) Placement: see (0) and G-P. DEAD-ENDS ROWS: NONE (not drafted). R116 kills two lane conjectures («D ≤ 2·LM + c» for c ≤ 4; «every
  mover of level l moves at most 2(l + 1) times») by explicit refereed instances inside its line, as R111 did for PM and PMV (R111-draft
  (14): «CHECKER C118 §5 confirmed «no row» for lane conjectures killed inside a landed line»).

### R116 [refereed-only] In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of R104 used; RESULTS R105's ENC, LOCAL, MONO, XI-NEW and RISE only; RESULTS R110's definition of 𝓛^R_d only; and RESULTS R113's ALIGN and F0 only), on acyclic Ξ-graphs, with T the number of steps of a run, Mv_t the movers of step t, moves(x) the number of steps t with x ∈ Mv_t, Z the set of movers that are the Ξ-target of some option, KP_s(x) the option of x with the least key under s, KF_x the number of steps t with KP_(s_t)(x) ≠ KP_(s_(t−1))(x), for a mover x of degree 2 π_s(x) its option of larger Ξ-value under s and PF_x the number of steps t with π_(s_t)(x) ≠ π_(s_(t−1))(x), v_s(x, k) the integer value of option (x, k) under s (R105 ENC), on 𝓛^R_d (2d movers on levels 0, …, d − 1) F_W(j) the number of steps of a set W at which the pair (2j, 2j + 1) flips (R113's flip), T^R(d) the largest T over 𝓛^R_d and all starts, μ(d) the largest moves(z) over 𝓛^R_d, all starts and all z ∈ Z of level ≥ 1, and a metronome segment of a mover x of level l ≥ 1 a set [a, b] of D consecutive steps each moving x, with LM the number of moves of the movers 2l − 2, 2l − 1 in it: (REDUCE-XI) at any degree and width, for 2 ≤ t ≤ T step t − 1 moves a member of Z, so T ≤ 1 + Σ_(z ∈ Z) moves(z); (MOVES-EQUIV) on 𝓛^R_d, μ(d) ≤ T^R(d) ≤ 3 + (2d − 2)μ(d), so a bound of 2d on the moves of every Ξ-target (the lane conjecture MOVES-2D, not claimed here) would give T^R(d) ≤ 4d² − 4d + 3, and μ is polynomial in d iff T^R is; (AND-GATE) at any degree elsewhere, a mover x of degree 2 moves at step t iff s_(t−1)(x) ≠ π_(s_(t−1))(x) = KP_(s_t)(x), so moves(x) ≤ 1 + min(KF_x, PF_x), and when π(x) changes at step t to b the value v(x, b) rises strictly at t; (WINDOW-DOUBLE) on 𝓛^R_d, for 1 ≤ j ≤ d − 1 and every window W = [a + 1, b] of steps, a flip of the pair (2j, 2j + 1) at a step moving neither of them is a step at which the pair (2j − 2, 2j − 1) flips while 2j and 2j + 1 are on different options before the step, and F_W(j) ≤ 2 + 2F_W(j − 1), so F_W(j) ≤ 2 if F_W(j − 1) = 0; (SEG-WINDOW) on 𝓛^R_d, for a metronome segment [a, b] of a mover of level l ≥ 1, the pair (2l − 2, 2l − 1) flips at every step of [a + 1, b], every step of [a + 1, b] moves a mover of level < l, D ≤ 3 + 2F_[a+1,b](l − 2) for l ≥ 2 and D ≤ 3 for l = 1, every 3 consecutive steps of [a + 1, b] contain a flip of the pair (2l − 4, 2l − 3) for l ≥ 2, and at every step t ∈ [a, b − 1] some mover other than x on the chain under s_(t−1) of the option x takes at t + 1 moves at t; and two lane conjectures are DEAD: «D ≤ 2·LM + c» for c ≤ 4 (experiments/new/box186/out/pass_d5_D5.json, 𝓛^R_5, start 0101010110: a Ξ-target of level 4 moves at steps 1-5 while LM = 0; also pass_d3_D3.json and pass_d4_D4.json, D 3 and 4 with LM 0) and «every mover of level l moves at most 2(l + 1) times» (experiments/new/box187/inst/m4_z4_r7.json, a byte copy of L-RED's experiments/red/r213/out/m4_z4_r7.json, 𝓛^R_4: a Ξ-target of level 2 moves 7 times) (2026-11-06) — a STRUCTURE / EQUIVALENCE statement inside the IDEAL model; bounds nothing polynomially; MOVES-2D is not claimed (its status is not part of this result; here μ(d) is shown equal to T^R(d) up to a factor 2d − 2 and an additive 3, so MOVES-2D is sufficient for a polynomial bound on T^R, and its necessity is not shown: a polynomial bound on T^R gives only μ polynomial); Ξ-cyclic genomes and genomes outside 𝓛^R_d (outside REDUCE-XI and AND-GATE) are not covered; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (DATA, experiments/new/box187/movescheck.py on the 208 in-tree 𝓛^R_d genome files of experiments/new/box150 to box187, every start for d ≤ 5 and the stored start for d ≥ 6, 63,223 runs: REDUCE-XI 0 violations on 63,223 runs, equality on 59,502; AND-GATE 0 on every (run, step, degree-2 mover), every pair of consecutive moves (the min bound by arithmetic) and every change of π; WINDOW-DOUBLE's bound 0 on 1,288,162 (window, level ≥ 1) pairs and its BURST-2 case 0 on every maximal window without flips of the pair below; SEG-WINDOW 0 on all 225,917 metronome segments for its first three clauses and its last one; MOVES-EQUIV, the pass-through clause of WINDOW-DOUBLE and the 3-step clause of SEG-WINDOW: no separate DATA; the four DEAD instances re-run) (P-IDEAL-MOVES, docs/new/P-IDEAL-MOVES.md with its fixes entries 1-3, docs/new/P-IDEAL-MOVES-fixes.md; L-NEW successor 57), CHECKER PASS (docs/checker/C129.md, checker PENDING)
- Object (L-NEW successor 57, Opus 5.5, D14 / D18 / D20, box 187; frozen, unchanged during review): packet P-IDEAL-MOVES,
  docs/new/P-IDEAL-MOVES.md, sha1 5ce2947d1ee4dab317e5c06446b38f050146cafb, 202 lines (l-new freeze d86adc86, 2026-11-06T21:11:22Z;
  identical at fd5c163f). Both referees measured it (REFEREE l. 4 «packet 5ce2947d…, 202 lines»; REFEREE-2 l. 8
  «docs/new/P-IDEAL-MOVES.md sha1 5ce2947d1ee4dab317e5c06446b38f050146cafb, 202 lines»). Labels (l. 7-8): «Labels: PROVED (L-NEW 57,
  unrefereed) / DEAD (instance, machine-checked) / DATA / READING (not to sign).» To sign (table l. 13-18): §1 Lemma REDUCE-XI and
  Corollary MOVES-EQUIV, §2 Lemma AND-GATE, §3 Lemma WINDOW-DOUBLE, §4 Lemma SEG-WINDOW (PROVED); §5 DEAD-SEG and DEAD-LEV (DEAD,
  instances); §6 «DATA / READING (not to sign)». Sections: premises (l. 21-44), §0 the model and notation (l. 47-78), §1 (l. 80-94), §2
  (l. 96-112), §3 (l. 114-133), §4 (l. 135-159), §5 (l. 161-177), §6 (l. 179-202). Sources (l. 5-6): docs/new/N5-MOVES-box185.md §1, §2
  and docs/new/N5-METRONOME-box186.md §0, §1; «This packet carries every proof in full and is checked against this text only; no other
  file carries a proof of a statement below.» (l. 6-7).
  Fixes: docs/new/P-IDEAL-MOVES-fixes.md, append-only, three entries by L-NEW successor 57 (fd5c163f: 116 lines, sha1
  510152dab3512980e5e739710f46ff14797edf87). Entry 1 (9995f5a2): REFEREE-2's W-1, W-2, W-3 and REFEREE's MV-L1, line L-2. Entry 2
  (d7b96be8): REFEREE's MV-C1, line L-3. Entry 3 (fd5c163f): the status words of the not-claimed clause removed, line L-4. Each: «No
  statement, proof or DATA of the packet changes» (l. 6-7, 60, 89-90), and each «carries no proof».
  The RESULTS line is L-4, 73c16d1e2b009ff2e3d774a904e4462be0874db1 (docs/new/P-IDEAL-MOVES-line-L4.txt, l-new fd5c163f,
  2026-11-07T01:16:07Z, the file's only commit; 4,598 bytes). The title is L-4 verbatim, with nothing inserted (its date parenthesis
  «(2026-11-06)» and its source note are the line's own; the source note names the packet, which carries every proof, and the fixes
  file, which carries none). L-4's parentheses balance (71 «(» / 71 «)»). Line history: L-1 (819c5815, d86adc86, frozen with the
  packet); L-2 (f3692aaa, 9995f5a2, fixes entry 1: L-1 with exactly five replacements R1-R5: the tail's not-claimed sentence (W-1), the
  pass-through clause's «2j and 2j + 1 are on different options before the step» (W-2), SEG-WINDOW's last clause «moves at t» (W-3),
  «(the min bound by arithmetic)» in the DATA (MV-L1), the source note); L-3 (d3983c68, d7b96be8, fixes entry 2: R6, «so MOVES-2D is
  sufficient for a polynomial bound on T^R, and its necessity is not shown: a polynomial bound on T^R gives only μ polynomial» for the
  unproved «not necessary» (MV-C1), and R7, the source note); L-4 (73c16d1e, fd5c163f, fixes entry 3: R8 and R9 remove the status words
  from the not-claimed clause, R10 the source note). Each step is the previous line with exactly the named replacements, each old string
  found once (my script, True ×3; both referees by their own scripts). L-4 MATCHES at both referees: REFEREE (2fe03939) §C add. 2 l. 187
  «L-3 + R8..R10 = 4,598 B, sha1 73c16d1e…, byte-equal to L-4.», l. 204 «Verdict: fixes entry 3 is CORRECT. L-4 MATCHES the byte test
  and in meaning. All packet items stay SIGNED.»; REFEREE-2 (88c0c6d6) Add. 3 l. 161 «L-3 with R8-R10 applied == L-4 byte for byte ✓.»,
  l. 171.
  Both diffed every definition of L-1 against packet §0 (REFEREE l. 82-83; REFEREE-2 l. 104-105); L-2-L-4 change no definition and no
  claim.
- Claims signed (REFEREE successor 24 «(Opus 5.5, D15)», report c82fac5c, and successor 25, §C 72f4b2f3, §C add. 1 e7047ace, §C add. 2
  2fe03939; REFEREE-2 successor 29 «(Opus 5.5, D1/D18/D20)», report 38a2adb6, Addenda 1-3 f71fdbdb, 0fdc26d4, 88c0c6d6). Every item is
  SIGN in both verdict tables (REFEREE "## 0. Verdicts" l. 9-18 of R-P-IDEAL-MOVES.md; REFEREE-2 "## Verdicts" l. 13-25 of
  R2-P-IDEAL-MOVES.md), with no gap; they stand in all later rounds (REFEREE l. 135 «All packet items stay SIGNED.», l. 156, l. 204;
  REFEREE-2 l. 136, 148, 171 «Statement verdicts unchanged (all SIGN).»). Every item is about R104's IDEAL model on acyclic Ξ-graphs;
  (a) and (c) at any degree; (b), (d), (e), (f), (g) on 𝓛^R_d (RESULTS R110's 2-wide degree-2 ladders, levels 0, …, d − 1, movers 2l and
  2l + 1 on level l). Notation (packet §0 l. 61-78): T the number of steps; Mv_t := {x : s_t(x) ≠ s_(t−1)(x)}; moves(x) := #{t ∈ [1, T]
  : x ∈ Mv_t}, «(the binder of Erratum E-2 (E2c))»; Z the Ξ-target movers; KP_s(x) as in R113; KF_x and PF_x the numbers of steps at
  which KP(x), π(x) change; v_s(x, k) the integer of the β-set of the chain of (x, k) under s (R105 ENC); for degree 2, π_s(x) the
  option with the larger v_s(x, k) (well defined: each chain contains its own β and, by acyclicity, not the other); a flip of a pair of
  one level as in R113; F_W(j) the number of steps of W at which (2j, 2j + 1) flips; c_j(s) as in R113; a metronome segment of x a set
  [a, b] of consecutive steps all moving x, D := b − a + 1, and for x of level l ≥ 1 LM := Σ_(t ∈ [a, b]) #(Mv_t ∩ {2l − 2, 2l − 1});
  T^R(d) the largest T over 𝓛^R_d with acyclic Ξ-graph and all starts. Cells: see (4) above (one row per section, «SIGN» / «**SIGN**
  (Opus 5.5, D1)»).
  (a) Lemma REDUCE-XI (§1 l. 81-88) [IDEAL-ACYC, any degree, any number of movers per level; any run]: «Then Mv_(t−1) ∩ Z ≠ ∅ for every
    t with 2 ≤ t ≤ T. Hence T ≤ 1 + #{t ∈ [1, T − 1] : Mv_t ∩ Z ≠ ∅} ≤ 1 + Σ_(z ∈ Z) moves(z).». Proof: for t ≥ 2 a least-level mover h
    of step t exists; by R105 XI-NEW and RISE «some strict Ξ-descendant of h on its chain under s_(t−2) moved at step t − 1»; the last
    edge of a Ξ-path to it makes it a Ξ-target, so it lies in Z; t ↦ t − 1 is injective. Not claimed (l. 88): «that the moving Ξ-target
    is a least-level mover; any bound on moves; anything about Ξ-cyclic genomes».
  (b) Corollary MOVES-EQUIV (§1 l. 89-94) [𝓛^R_d, acyclic Ξ-graph]: with μ(d) the largest moves(z) over all such genomes, all starts and
    all z ∈ Z of level ≥ 1 (μ(1) := 0), «Then μ(d) ≤ T^R(d) ≤ 3 + (2d − 2)·μ(d).», and μ is bounded by a polynomial in d iff T^R is.
    Proof: moves(z) ≤ T; REDUCE-XI with F0 (the two level-0 movers move at most once each) and at most 2d − 2 movers of level ≥ 1. The
    line also keeps the packet's conditional (l. 90-91: a bound of 2d on the moves of every Ξ-target would give T^R(d) ≤ 4d² − 4d + 3);
    MOVES-2D is not claimed, and its status is not part of this result. Not claimed (l. 94) also: «that movers outside Z are bounded
    (they need not be, and REDUCE-XI does not need them)».
  (c) Lemma AND-GATE (§2 l. 96-112) [IDEAL-ACYC (any degree elsewhere); x a mover with deg(x) = 2; any run]: «(a) For t ∈ [1, T]: x ∈
    Mv_t iff s_(t−1)(x) ≠ π_(s_(t−1))(x) and π_(s_(t−1))(x) = KP_(s_t)(x).»; (b) between two consecutive moves of x, π(x) and KP(x) each
    change, «Hence moves(x) ≤ 1 + min(KF_x, PF_x).»; «(c) If π_(s_t)(x) = b ≠ π_(s_(t−1))(x), then v_(s_t)(x, b) > v_(s_(t−1))(x, b).».
    Proof: at degree 2 the A-set is {s(x)} or both options, and the step takes the key-least option under s_t; (c) by ENC and MONO (v of
    the old π option never falls). Its moves bound contains R105's KEYFLIP and R113's KP-MOVE bound moves(x) ≤ 1 + KF_x; the PF_x half
    and the iff are new. Not claimed (l. 112): «a bound on PF_x or KF_x; anything at deg(x) ≥ 3».
  (d) Lemma WINDOW-DOUBLE (§3 l. 114-133) [𝓛^R_d; 1 ≤ j ≤ d − 1; p := 2j, q := 2j + 1; 0 ≤ a < b ≤ T; W := [a + 1, b]]: (a) a flip of
    (p, q) at a step moving neither is a step at which the pair (2j − 2, 2j − 1) flips, with s_(t−1)(p) ≠ s_(t−1)(q); «(b) F_W(j) ≤ 2 +
    2·F_W(j − 1). In particular (BURST-2) if F_W(j − 1) = 0 then F_W(j) ≤ 2.». Proof: ALIGN's key-order formula and c_j's dependence on
    the pair below; a potential Φ_j summed over the window. On W = [1, T], (b) is RESULTS R113's PAIR-DOUBLE; the window form is new.
    Not claimed (l. 133): «anything beyond R113 PAIR-DOUBLE on the whole run (W = [1, T] is PAIR-DOUBLE itself); a polynomial bound».
  (e) Lemma SEG-WINDOW (§4 l. 135-159) [𝓛^R_d; x a mover of level l ≥ 1; any run; [a, b] a metronome segment of x; u := 2l − 2, w := 2l
    − 1]: «(a) The pair (u, w) flips at every step of [a + 1, b]; so D − 1 ≤ F_[a+1,b](l − 1).»; (b) D ≤ 1 + LS + PT, «and every step of
    [a + 1, b] moves some mover of level < l.»; «(c) If l ≥ 2: D ≤ 3 + 2·F_[a+1,b](l − 2). If l = 1: D ≤ 3.»; (d) for l ≥ 2 «every 3
    consecutive steps of [a + 1, b] contain a flip of the pair l − 2.»; (e) for every t ∈ [a, b − 1], π(x) changes at t, the value of
    x's option s_(t+1)(x) rises strictly at t, and «some mover of the chain of (x, s_(t+1)(x)) under s_(t−1), other than x, moves at
    t.». Proof: AND-GATE (b) on consecutive moves and ALIGN; WINDOW-DOUBLE on the segment's window; F0 at l = 1; R105 LOCAL for (e). Not
    claimed (l. 159): «that the movers of (b) or (e) are u or w; a bound on D polynomial in l (iterated, (c) gives 2^l-type bounds
    only)».
  (f) DEAD-SEG (§5 l. 162-172; DEAD, instances): «for a metronome segment of a mover of level l ≥ 1, D ≤ 2·LM + c» is false for every c
    ≤ 4. Instances (𝓛^R_d, Ξ-acyclic, the mover a Ξ-target), each run from the start given here, not from the file's stored start:
    experiments/new/box186/out/pass_d5_D5.json (sha1 16be2e594732ad0b21e2c84aa4cdbc62d143e7c4), 𝓛^R_5, start 0101010110: mover 9 (level
    4) moves at steps 1-5 (D 5), LM 0; pass_d4_D4.json (3bf6a4a48bc2df9fb8809306f8347ee280965b07), 𝓛^R_4, start 01010111: mover 7 (level
    3), steps 1-4 (D 4), LM 0; pass_d3_D3.json (8bca976438ca184bb8b8e4d5ecf3455f51809ff4), 𝓛^R_3, start 110100: mover 5 (level 2), steps
    1-3 (D 3), LM 0. Not claimed (l. 172): «that D − 2·LM is unbounded in d (DATA only: 3, 4, 5 at d = 3, 4, 5); anything about c ≥ 5».
  (g) DEAD-LEV (§5 l. 173-177; DEAD, instance): «on 𝓛^R_d every mover of level l moves at most 2(l + 1) times» is false:
    experiments/new/box187/inst/m4_z4_r7.json (sha1 7c158e2f806df2d1984418902548cfc2cb243d75; a byte copy of L-RED's claude/l-red
    experiments/red/r213/out/m4_z4_r7.json, l-red commit 4b61200d, same sha1), 𝓛^R_4, stored start 10111010: mover 4 (level 2, a
    Ξ-target) moves 7 > 6 = 2(2 + 1) times in a run of T 8 (at steps 1, 2, 3, 5, 6, 7, 8: REFEREE l. 52). The 7 is the most R113's
    MOVES, PAIR-DOUBLE and F0 allow at level 2 (REFEREE-2 F-4, l. 121-122).
  The RESULTS line (L-4) states (a)-(g) with their exact hypotheses and nothing wider; it gives the start of pass_d5_D5 and not those of
  pass_d3_D3 and pass_d4_D4.
- Premise: RESULTS R104's definition of the IDEAL model and of the Ξ-graph (no R104 theorem), restated in packet §0 (l. 47-61); RESULTS
  R105's five items, quoted verbatim by the packet (l. 23-29) «from its statement «at any degree»»: «(ENC) the Ξ-order of β-sets is the
  order of the integers Σ ±2^rank (+ for even parity), so, with ε(x, k) := ±2^rank(x, k) (+ for even parity), the value of option (x, k)
  is ε(x, k) plus the current value of its Ξ-target (ε(x, k) alone if the Ξ-target is the exit X)»; «(LOCAL) an option's value depends
  only on the states on its chain, a key only on the states below its level»; «(MONO) the current Ξ-value of every mover never decreases
  along a run»; «(XI-NEW) for t ≥ 2 every least-level mover h of step t moves to an option w ∉ A_(s_(t−2))(h) (A_s(h): h's current
  option under s and its options strictly better under s)»; «(RISE) that option's value rose strictly at step t − 1, and some strict
  Ξ-descendant of h on its chain under s_(t−2) moved at step t − 1»; each occurs once in R105's title (l. 10155), all five after «at any
  degree» and before R105's «and at degree ≤ 2 only», so at any degree (ENC and MONO are also quoted in R113's and R114's bodies, XI-NEW
  and RISE in R114's: hits 3, 1, 3, 2, 2, each explained by those quotations); RESULTS R110's definition of 𝓛^R_d, «the 2-wide degree-2
  ladders in L-RED's R197 convention (movers 2l and 2l + 1 on level l, all of degree 2, no other movers, option k of a mover of level l
  ≥ 1 W-pointing to mover 2(l − 1) + k)» (packet l. 32-34), found in R110's title (l. 11323; also quoted in R112's, R113's and R114's
  bodies); RESULTS R113's two items, «(ALIGN) on 𝓛^R_d, for 1 ≤ l ≤ d − 1 and every state s of a run, both movers 2l and 2l + 1 have
  KP_s = c_l(s), each of them that moves at step t moves to option c_l(s_t), and the order of their keys under s is [s(2l) = c_l(s)] if
  s(2l) ≠ s(2l + 1) and γ_l(j) if both are on option j» and «(F0) on 𝓛^R_d each level-0 mover moves at most once and F(0) ≤ 2», with
  R113's notation «KP_s(x) the option of x with the least key under s», «c_l(s) the option index k for which mover 2(l − 1) + k has the
  smaller current key under s», «γ_l(j) := [g(2l, j) < g(2l + 1, j)] with g(x, k) the gate index of option (x, k)» and «F(l) the number
  of steps at which the pair (2l, 2l + 1) flips», quoted verbatim by the packet (l. 35-40), each found once in R113's title (l. 12152;
  the KP_s(x) wording also defines KP in R111's and R114's titles, 3 hits). Whitespace normalised. L-4: «premise: R104's definition of
  the model only, no theorem of R104 used; RESULTS R105's ENC, LOCAL, MONO, XI-NEW and RISE only; RESULTS R110's definition of 𝓛^R_d
  only; and RESULTS R113's ALIGN and F0 only». Use: XI-NEW and RISE in REDUCE-XI; F0 in MOVES-EQUIV, WINDOW-DOUBLE and SEG-WINDOW (c);
  ENC and MONO in AND-GATE (c); ALIGN in WINDOW-DOUBLE and SEG-WINDOW; LOCAL in SEG-WINDOW (e). Not used (packet l. 41-44): every other
  R105 item; R106-R112; R111's CASCADE («§3 (a) re-proves the pass-through fact from ALIGN»); R113's KP-MOVE, PAIR-DOUBLE, MOVES,
  T-BOUND, PATH-RISE; RESULTS R114 (landed; its MOVE-RISE is not used). No machine premise is used by a signed proof; the DEAD items
  rest on computed runs (packet l. 44). Both referees byte-tested the quotes (REFEREE l. 21-25; REFEREE-2 l. 28-30 «18/18 verbatim»).
  Erratum E-2 does not bear: it corrects R105's CHAINED binder, TOP-MONO's RANK_t and KEYFLIP's moves(x), none of them a premise here
  (packet l. 29-31; REFEREE l. 25 «E-2 does not bear.»).
- L41 and L43. The proofs are L-NEW successor 57's (packet l. 2, 5-7); the fixes entries carry no proof; the referees' simulators are
  checking tools. Nothing referee-written is a proof step of the entry (my reading; neither referee mentions L41). The DEAD items kill
  lane conjectures by explicit instances recomputed by both referees; no candidate algorithm and no route is declared dead, so L43 does
  not bear.
- Fixes (docs/new/P-IDEAL-MOVES-fixes.md, append-only, L-NEW successor 57; the file at fd5c163f 116 lines, sha1
  510152dab3512980e5e739710f46ff14797edf87):
  - Entry 1 (l. 3-55; 9995f5a2, 2026-11-06T23:36:29Z): W-1 (required by REFEREE-2: L-1's «shown equivalent up to a factor 2d − 2 to a
    polynomial bound on T^R» overclaimed; the packet does not, l. 8-13); W-2 (required: «the two movers» → «2j and 2j + 1 … before the
    step»); W-3 (optional, taken: «moves at t»); MV-L1 (optional, REFEREE: «(the min bound by arithmetic)»); D-1-D-3 (REFEREE-2's §6
    attribution notes) without change; line L-2 by R1-R5 (l. 23-36). REFEREE §C l. 131-135; REFEREE-2 Add. 1 l. 128-136.
  - Entry 2 (l. 57-84; d7b96be8, 2026-11-07T00:16:43Z): MV-C1 (required by REFEREE §C: L-2's «sufficient, not necessary» claimed an
    unproved non-necessity); line L-3 by R6, R7 (l. 66-75). REFEREE §C add. 1 l. 149-156; REFEREE-2 Add. 2 l. 142-148.
  - Entry 3 (l. 86-116; fd5c163f, 2026-11-07T01:16:07Z): the line's not-claimed clause carries no status (l. 87-90); a wording note on
    the packet's status labels (l. 91-96); line L-4 by R8-R10 (l. 97-103). REFEREE §C add. 2 l. 185-204; REFEREE-2 Add. 3 l. 161-171.
  No fix changes a statement, a hypothesis, a proof or a DATA count; the fixes change only the line (its not-claimed tail, two clause
  wordings, one DATA label, the source note).
- Not signed: packet §6 (DATA; «DATA / READING (not to sign)», table l. 19), in particular its corpus counts as statements, its «Lane
  DATA» on the moves of Ξ-targets (l. 194-197) and its EXCLUDED list (l. 198-199); the packet's status labels (l. 9, l. 77-78). Not
  claimed: MOVES-2D (its status is not part of this result); that D − 2·LM is unbounded; DEAD-SEG for c ≥ 5. OPEN, not claimed: any
  polynomial bound on μ(d) or T^R(d); a polynomial bound on D in l; any statement for Ξ-cyclic genomes, or outside 𝓛^R_d beyond
  REDUCE-XI and AND-GATE; G-N5-TIME.
- Referee strengthening (NOT part of this entry; referee checks):
  (i) REFEREE (§2, own simulator t3r_sim.py, «no lane code»): the four DEAD instances recomputed, «All EQUAL to §5 and movescheck.out.»
    (l. 51), DEAD-LEV's steps «1, 2, 3, 5, 6, 7, 8» (l. 52); check.sh block at d86adc86 PASS (l. 54); the DATA rule clause by clause
    against movescheck.py (§3 l. 56-75).
  (ii) REFEREE-2 (own simulator r2moves.py, «written from R104's text»; l. 70-89): on the frozen corpus the same 208 files, 63,223 runs,
    140,395 steps, 225,917 segments and 1,288,162 windows, «0 mismatches» against the lane's Gen (l. 74-75); 21 counters, including RX2
    (the middle inequality), AGBm (the min bound), WDA (WINDOW-DOUBLE (a) «on 31,212 flips with no move of the pair»), MEQ (MOVES-EQUIV
    per run) and SWE1, SWE2 (SEG-WINDOW (e)'s first sentence), all 0 on the corpus and on 300 random acyclic 𝓛^R_d genomes (85,440 runs;
    l. 76-80); a negative control with keys under the old state firing on the key-side counters (l. 81-82); check.sh block at d86adc86,
    9995f5a2, d7b96be8 and fd5c163f PASS (l. 88-89, 135, 146-147, 169-170).
- Honest limits: (i) A STRUCTURE / EQUIVALENCE statement inside the IDEAL model: every step but the last moves a Ξ-target mover
  (REDUCE-XI), so on 2-wide ladders the run length and the largest number of moves of a Ξ-target of level ≥ 1 bound each other up to a
  factor 2d − 2 and an additive 3 (MOVES-EQUIV); a degree-2 mover moves exactly when its value preference differs from its option and
  agrees with its key preference, so its moves are bounded by the changes of either (AND-GATE); on 2-wide ladders a pair flips without
  moving only when the pair below flips, and the flips of a pair on any window at most double those below plus 2 (WINDOW-DOUBLE); a
  mover moving at consecutive steps forces a flip of the pair below at each inner step and is bounded through the flips two levels down
  (SEG-WINDOW); and two lane conjectures are false by explicit instances. It bounds nothing polynomially (iterated, SEG-WINDOW and
  WINDOW-DOUBLE give exponential bounds only); G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim. (ii) REDUCE-XI
  and AND-GATE are for acyclic genomes of any degree (AND-GATE for a degree-2 mover); MOVES-EQUIV, WINDOW-DOUBLE, SEG-WINDOW and the
  DEAD items are on 𝓛^R_d only; Ξ-cyclic genomes are not covered. (iii) MOVES-2D is named by the line only inside MOVES-EQUIV's
  conditional and as not claimed; it is not claimed here, and its status is not part of this result. MOVES-EQUIV's two inequalities and
  its equivalence do not use it (REFEREE §C add. 1 l. 162-163; REFEREE-2 Add. 2 l. 150-151). (iv) The DEAD items rest on four computed
  runs (box150 Gen in movescheck.py), each recomputed by both referees with their own simulators; the files are named by path and sha1,
  and pass_d3_D3, pass_d4_D4 and pass_d5_D5 are run from the starts given in (f), not from their stored starts. (v) The DATA is per
  statement, as the line's DATA parenthesis says, with these exact sets and units (movescheck.py, read by me): the 208 𝓛^R_d files under
  box150-box187 (all Ξ-acyclic by my own search), every start for d ≤ 5 and the stored start for d ≥ 6, 63,223 runs; REDUCE-XI per run
  (both halves), with the 59,502 runs counting T = 1 + #{t ≤ T − 1 : Mv_t ∩ Z ≠ ∅}, the middle term of the packet's chain, which the
  line does not state (T = 1 + Σ_(z ∈ Z) moves(z) holds on 8,399 runs, my count); AND-GATE per (run, step, mover), per consecutive pair
  of moves and per change of π; WINDOW-DOUBLE (b) per (window, level ≥ 1), 1,288,162, and BURST-2 per maximal window without flips of
  the pair below; SEG-WINDOW (a), (b) second half, (c) and (e) per metronome segment (all sub-segments), 225,917; MOVES-EQUIV,
  WINDOW-DOUBLE's pass-through clause and SEG-WINDOW's 3-step clause have no lane count; the AND-GATE moves bound follows by arithmetic
  from the pair count. (vi) Every statement is about R104's IDEAL model; nothing is said about a real N5 run or a parity game beyond
  what R104 already says. Premises: RESULTS R104's definition, R105's ENC, LOCAL, MONO, XI-NEW and RISE, R110's definition of 𝓛^R_d,
  R113's ALIGN and F0; R106-R109, R111, R112 and R114 are not used. No lit note, no lane file, no outside source. No Lean. Every proof
  is in docs/new/P-IDEAL-MOVES.md; the fixes file carries none; the line's source note names both. (vii) Names: «R116» here is this
  RESULTS entry, not L-RED's box R116 (RESULTS Dead-ends section, «docs/red/R116-sf-exponential.md»); «MOVES-EQUIV» is this corollary,
  not R113's lemma MOVES; «F_W(j)» is the window form of R113's F(j); «LM» is this packet's segment count; «(LOCAL)» is R105's item (a
  premise); «W-1», «W-2», «W-3», «D-1»-«D-3» (REFEREE-2) and «MV-L1», «MV-C1» (REFEREE) are this packet's referee labels; R1-R10 are the
  fixes entries' replacement labels. (viii) Overlaps with landed entries: AND-GATE's moves bound contains R105's KEYFLIP and R113's
  KP-MOVE bound moves(x) ≤ 1 + KF_x; WINDOW-DOUBLE (b) on the whole run is R113's PAIR-DOUBLE, and (a) is R111's CASCADE on 𝓛^R_d
  (re-proved from ALIGN), restated, not claimed as new; SEG-WINDOW's bounds are segment forms of R113's MOVES and R111's LADDER;
  REDUCE-XI is the counterpart, for moves of Ξ-targets, of R114's RISE-EQUIV for rises of options; none of these landed items is claimed
  again, and none is a premise except as listed.
- Data (DATA, not proof): experiments/new/box187/movescheck.py (l-new d86adc86, sha1 8153717b8596b82a68c8b35c7ab76aabc765d7c2, 116
  lines; deterministic, no arguments; simulator: box150/check.py's Gen, the lane's own implementation of R104's model), output frozen in
  experiments/new/box187/movescheck.out (sha1 4874020973e02bf269b64624e4e7b110bb08ca24, 6 lines); wired into experiments/new/check.sh
  block «P-IDEAL-MOVES» (l. 935-942 at fd5c163f: the output diff, the counter and DEAD lines, the sha1 pins of the packet, the four
  lines, the fixes, the tool, its output and the four instances). L-4's DATA parenthesis: «(DATA, experiments/new/box187/movescheck.py
  on the 208 in-tree 𝓛^R_d genome files of experiments/new/box150 to box187, every start for d ≤ 5 and the stored start for d ≥ 6,
  63,223 runs: REDUCE-XI 0 violations on 63,223 runs, equality on 59,502; AND-GATE 0 on every (run, step, degree-2 mover), every pair of
  consecutive moves (the min bound by arithmetic) and every change of π; WINDOW-DOUBLE's bound 0 on 1,288,162 (window, level ≥ 1) pairs
  and its BURST-2 case 0 on every maximal window without flips of the pair below; SEG-WINDOW 0 on all 225,917 metronome segments for its
  first three clauses and its last one; MOVES-EQUIV, the pass-through clause of WINDOW-DOUBLE and the 3-step clause of SEG-WINDOW: no
  separate DATA; the four DEAD instances re-run)». What each count covers (movescheck.py, read by me): RX per run, both halves of
  REDUCE-XI (63,223); RXEQ, «equality», per run with T ≥ 1: T = 1 + #{t ≤ T − 1 : Mv_t ∩ Z ≠ ∅} (59,502), not T = 1 + Σ_(z ∈ Z) moves(z)
  (8,399 runs, my count); AGA per (run, step, mover) (1,298,948, my count); AGB per consecutive pair of moves (37,510, my count); AGC
  per change of π (235,189, my count); WPD per (window, level ≥ 1) (1,288,162); SWD per maximal window without flips of the pair below
  (219,435, my count); SWA, SWB, SWC, SWE per metronome segment (225,917; SWB also checks D ≤ 1 + LS + PT, SWE checks the chain-mover
  clause only); the DEAD lines by explicit starts for the three pass_d* files and the stored start for m4_z4_r7. The block's output,
  reproduced by both referees (REFEREE l. 54; REFEREE-2 l. 88-89, 169-170) and re-run for this draft (2026-11-07T02:11:29Z from a `git
  archive` of fd5c163f's experiments/new and docs/new, rc 0, the PASS line; movescheck's output equal to movescheck.out). No signed
  statement uses any count; the DEAD items use the computed runs of their instances.
- Signatures: REFEREE docs/referee/R-P-IDEAL-MOVES.md: successor 24's report c82fac5cd204a5fae8a26b8f7ea6418aaa46d4c1
  (2026-11-06T21:43:56Z, new file, 91 lines, sha1 0e62923bfb05d4f1420762c375c94249df706904): every item SIGN, the DEAD instances
  recomputed, the DATA rule applied clause by clause, L-1 MATCHES with optional MV-L1 (l. 9-18, 46-75, 80-86); successor 25's §C
  72f4b2f365f208c226d8de0378b1cf0f23ec0d63 (2026-11-06T23:54:36Z, 136 lines): fixes entry 1 CORRECT, L-2 byte test MATCHES, MV-C1
  required (l. 93-136); §C add. 1 e7047ace216d29cfd3ff7327c8e50925667ef921 (2026-11-07T00:34:14Z, 174 lines): «Verdict: fixes entry 2 is
  CORRECT. L-3 MATCHES the byte test and in meaning. All packet items stay SIGNED.» (l. 156), with an answer to the Lead on what the
  signed items depend on (l. 157-168); §C add. 2 2fe03939d4e0ef804da9d0da5236b58458cf8861 (2026-11-07T01:45:22Z, 204 lines, sha1
  ad6cb02e6212ecc7c0a1e88407cef05d455a83a3): L-4's byte test and meaning, «Verdict: fixes entry 3 is CORRECT. L-4 MATCHES the byte test
  and in meaning. All packet items stay SIGNED.» (l. 204); a post-note c011995cd20c4e5e8d67293a2aa9fc049086aa926 (2026-11-07T02:13:40Z,
  206 lines, sha1 98338ae477a109f793fbb2447ee408c3154db463) keeps that verdict (l. 205-206). REFEREE-2
  docs/referee-2/R2-P-IDEAL-MOVES.md: successor 29's report 38a2adb649f7d7665678f63ec66d539c68cb1b6d (2026-11-06T23:12:13Z, 122 lines):
  every item SIGN, no gap, L-1 MATCHES after W-1 and W-2, D-1-D-3 notes, F-4 (l. 13-25, 91-122); Add. 1
  f71fdbdbd20d0e694959af77eb830b14891913e9 (23:54:08Z): fixes CORRECT, L-2 MATCHES (l. 124-136); Add. 2
  0fdc26d41c832ede95ccb0c8570e2007b928a0e8 (2026-11-07T00:34:22Z): entry 2 CORRECT, L-3 MATCHES, MV-C1 agreed (l. 138-154); Add. 3
  88c0c6d668eab005ccb2bf2da48be7973979fc72 (01:45:52Z, 171 lines, sha1 a7677cbb2431394223ca0c5a954d3314f6ccef1b): entry 3 CORRECT, L-4
  MATCHES (l. 156-171); a post-note 6924e140a5f8172d2979f603744c5c548b59a829 (02:09:17Z, 174 lines, sha1
  5be0b2ee1c18ff7ae011d756ebd8181d3412d212) keeps it (l. 172-174, «Addendum 3's verdict stands.»); its tools and outputs in
  docs/referee-2/R2-P-IDEAL-MOVES/ (r2moves.py, cmpgen.py, blk187*.out). Lane: freeze and L-1 d86adc8631573f843b6029a0ae11cb1cb9a80c93;
  fixes entries 1-3 and L-2-L-4 9995f5a2df76268665e17ae53dd03158a3a30fa2, d7b96be80d82db4792e339f7dd8c194f4eeb76d9,
  fd5c163f05dab991101fdb4e6da6a789f72bef73.
  INDEPENDENCE: REFEREE l. 2 «Independent: docs/referee-2/ was not opened on this packet.»; REFEREE-2 l. 2-3 «Independent: docs/referee/
  not read for this packet before this push.». REFEREE's report (21:43:56Z) precedes REFEREE-2's (23:12:13Z); neither cites the other's
  report; each recomputed the DEAD instances with its own simulator and re-ran the check.sh block. In the later rounds REFEREE read
  REFEREE-2's W texts only (§C l. 98 «REFEREE-2's report read for the required texts», l. 136 «I did not read docs/referee-2/ beyond the
  W-1..W-3 texts named above.»), and REFEREE-2 met MV-C1 through fixes entry 2 (Add. 2 l. 143). Differences, resolved: REFEREE-2 alone
  required W-1 and W-2 (line wording); REFEREE alone required MV-C1, which corrected W-1's text, and REFEREE-2 agreed («**MV-C1: I
  agree; it corrects my miss.**», l. 143). Both SIGN the same items, with no gap, and both MATCH L-4 (each by its own byte test).
- TARGET.md diff: TARGET.md §1-§3 define parity games («A parity game is G = (V, V_E, V_O, E, pr) with V finite»), the regions W_E, W_O,
  M4 (§2 «There is a deterministic algorithm A and a polynomial p such that for every parity game G, A on input G halts within») and the
  word-RAM cost model; no statement of this entry mentions a parity game, a winning region, an algorithm's running time or a cost model
  (packet l. 200-202 «Diff against TARGET.md: no statement mentions a parity game, a winning region, an algorithm's running time or a
  complexity class.»; REFEREE l. 78-79 «Not M3, not M4, not a gauntlet step.»). MOVES-EQUIV is an equivalence between two open
  statements («μ polynomial» and «T^R polynomial», fixes entry 1, W-1 note), not a bound. The line (L-4) makes no M4 claim and no TARGET
  claim; its tail reads «a STRUCTURE / EQUIVALENCE statement inside the IDEAL model» and «G-N5-TIME stays OPEN; not M3, not a step-4
  pass, not a TARGET.md claim» (L-4, by script). Not a step-4 pass. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER the last UPDATE of G-N5-TIME on l. 11 (GAPS at 6ca995ed: R114's, «UPDATE
2026-11-06 21:57Z: RESULTS R114 (P-IDEAL-RISE; CHECKER C127 e3269b0b) …»; R115's once R115 has landed), before the row's closing « |»,
built by script (upd116.py: r115/upd115.py l. 1-337 with its 18 controls, R97-R114, all landed, byte for byte, True; sentinel_build111
of upd111.py unchanged, default drops, the «(DATA, » opening; R111's DEAD-clause step for the DEAD clause (G-U); cross-checked against a
direct build: True) only from the clauses of the title line L-4: the five labels behind their clauses, the DEAD clause after
«(SEG-WINDOW)»; « (2026-11-06) — » → «: »; the DATA parenthesis before the source parenthesis opened as «; DATA, …»; «G-N5-TIME stays
OPEN» and «not M3, not a step-4 pass, not a TARGET.md claim» dropped; the source parenthesis kept; «. G-N5-TIME stays open.» at the end.
L-4 holds no "|"; the UPDATE holds none (4,632 bytes, 70 «(» / 70 «)»; sha1 of the line without newline, placeholders unfilled:
2820757a4e693b95733ea9335a0cf959c4ccefe4). <DATE> is the landing date (YYYY-MM-DD, by date -u at the landing commit; C114 Add. 1 E-1),
<HH:MM> the landing time and <checker> the CHECKER C129 commit, all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R116 (P-IDEAL-MOVES; CHECKER C129 <checker>) [refereed-only] LANDED: In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of R104 used; RESULTS R105's ENC, LOCAL, MONO, XI-NEW and RISE only; RESULTS R110's definition of 𝓛^R_d only; and RESULTS R113's ALIGN and F0 only), on acyclic Ξ-graphs, with T the number of steps of a run, Mv_t the movers of step t, moves(x) the number of steps t with x ∈ Mv_t, Z the set of movers that are the Ξ-target of some option, KP_s(x) the option of x with the least key under s, KF_x the number of steps t with KP_(s_t)(x) ≠ KP_(s_(t−1))(x), for a mover x of degree 2 π_s(x) its option of larger Ξ-value under s and PF_x the number of steps t with π_(s_t)(x) ≠ π_(s_(t−1))(x), v_s(x, k) the integer value of option (x, k) under s (R105 ENC), on 𝓛^R_d (2d movers on levels 0, …, d − 1) F_W(j) the number of steps of a set W at which the pair (2j, 2j + 1) flips (R113's flip), T^R(d) the largest T over 𝓛^R_d and all starts, μ(d) the largest moves(z) over 𝓛^R_d, all starts and all z ∈ Z of level ≥ 1, and a metronome segment of a mover x of level l ≥ 1 a set [a, b] of D consecutive steps each moving x, with LM the number of moves of the movers 2l − 2, 2l − 1 in it: at any degree and width, for 2 ≤ t ≤ T step t − 1 moves a member of Z, so T ≤ 1 + Σ_(z ∈ Z) moves(z) (REDUCE-XI); on 𝓛^R_d, μ(d) ≤ T^R(d) ≤ 3 + (2d − 2)μ(d), so a bound of 2d on the moves of every Ξ-target (the lane conjecture MOVES-2D, not claimed here) would give T^R(d) ≤ 4d² − 4d + 3, and μ is polynomial in d iff T^R is (MOVES-EQUIV); at any degree elsewhere, a mover x of degree 2 moves at step t iff s_(t−1)(x) ≠ π_(s_(t−1))(x) = KP_(s_t)(x), so moves(x) ≤ 1 + min(KF_x, PF_x), and when π(x) changes at step t to b the value v(x, b) rises strictly at t (AND-GATE); on 𝓛^R_d, for 1 ≤ j ≤ d − 1 and every window W = [a + 1, b] of steps, a flip of the pair (2j, 2j + 1) at a step moving neither of them is a step at which the pair (2j − 2, 2j − 1) flips while 2j and 2j + 1 are on different options before the step, and F_W(j) ≤ 2 + 2F_W(j − 1), so F_W(j) ≤ 2 if F_W(j − 1) = 0 (WINDOW-DOUBLE); on 𝓛^R_d, for a metronome segment [a, b] of a mover of level l ≥ 1, the pair (2l − 2, 2l − 1) flips at every step of [a + 1, b], every step of [a + 1, b] moves a mover of level < l, D ≤ 3 + 2F_[a+1,b](l − 2) for l ≥ 2 and D ≤ 3 for l = 1, every 3 consecutive steps of [a + 1, b] contain a flip of the pair (2l − 4, 2l − 3) for l ≥ 2, and at every step t ∈ [a, b − 1] some mover other than x on the chain under s_(t−1) of the option x takes at t + 1 moves at t (SEG-WINDOW); and two lane conjectures are DEAD: «D ≤ 2·LM + c» for c ≤ 4 (experiments/new/box186/out/pass_d5_D5.json, 𝓛^R_5, start 0101010110: a Ξ-target of level 4 moves at steps 1-5 while LM = 0; also pass_d3_D3.json and pass_d4_D4.json, D 3 and 4 with LM 0) and «every mover of level l moves at most 2(l + 1) times» (experiments/new/box187/inst/m4_z4_r7.json, a byte copy of L-RED's experiments/red/r213/out/m4_z4_r7.json, 𝓛^R_4: a Ξ-target of level 2 moves 7 times): a STRUCTURE / EQUIVALENCE statement inside the IDEAL model; bounds nothing polynomially; MOVES-2D is not claimed (its status is not part of this result; here μ(d) is shown equal to T^R(d) up to a factor 2d − 2 and an additive 3, so MOVES-2D is sufficient for a polynomial bound on T^R, and its necessity is not shown: a polynomial bound on T^R gives only μ polynomial); Ξ-cyclic genomes and genomes outside 𝓛^R_d (outside REDUCE-XI and AND-GATE) are not covered; DATA, experiments/new/box187/movescheck.py on the 208 in-tree 𝓛^R_d genome files of experiments/new/box150 to box187, every start for d ≤ 5 and the stored start for d ≥ 6, 63,223 runs: REDUCE-XI 0 violations on 63,223 runs, equality on 59,502; AND-GATE 0 on every (run, step, degree-2 mover), every pair of consecutive moves (the min bound by arithmetic) and every change of π; WINDOW-DOUBLE's bound 0 on 1,288,162 (window, level ≥ 1) pairs and its BURST-2 case 0 on every maximal window without flips of the pair below; SEG-WINDOW 0 on all 225,917 metronome segments for its first three clauses and its last one; MOVES-EQUIV, the pass-through clause of WINDOW-DOUBLE and the 3-step clause of SEG-WINDOW: no separate DATA; the four DEAD instances re-run (P-IDEAL-MOVES, docs/new/P-IDEAL-MOVES.md with its fixes entries 1-3, docs/new/P-IDEAL-MOVES-fixes.md; L-NEW successor 57). G-N5-TIME stays open.

Addendum (subagent, for the Lead; does not land; written 2026-11-07T02:31:22Z by date -u). (1) FIRST FILL on line L-4 (l-new fd5c163f,
sha1 73c16d1e…), to CHECKER C129. NOT pushed; my commits: the seven merges (--no-ff) 3f765de8 (l-new fd5c163f), 0c2e3e49 (referee
2fe03939), bf06df78 (referee-2 88c0c6d6), 3e8d0bcb (l-new f55dac37), 1eb447f2 (checker 2dd44fc1), d7515bd2 (referee c011995c), 1cc33e15
(referee-2 6924e140) and one commit holding this file. Push trunk before landing. (2) TITLE l. 453 = "### R116 [refereed-only] " + L-4
without its newline + ", CHECKER PASS (docs/checker/C129.md, checker PENDING)", checked by script (chk116.py): equal, byte for byte
(True); the only «### R» heading of this file; 71 + 1 «(» and 71 + 1 «)», balanced; no «[lane», no packet name before the claims. (3)
BODY l. 453-685 (python slice d[452:685]; 0 "|" in the range, by script); GAPS preamble l. 687-696 (two "|", both inside quotation
marks: the row's closing « |» and «holds no "|"»); UPDATE l. 697 (d[696]; one line, 0 "|", one each of <DATE>, <HH:MM>, <checker>; 4,632
bytes; sha1 2820757a4e693b95733ea9335a0cf959c4ccefe4 of the unfilled line without newline; controls True ×18: R97's-R114's landed
UPDATEs). No Dead-ends row is drafted ((14)). A landing script in the shape of R114's / R115's slices d[452:685] for the entry and reads
d[696] for the UPDATE, with «R116», «C129», and PREV = the R-entry right before «**Erratum E-1**» (R114 or R115), asserting that the
last UPDATE on GAPS l. 11 is PREV's. (4) RE-RUNS: listed in the header paragraph "Re-runs", (a)-(g). G-9 candidate lines (wdiff116.py,
if the Lead routes them; each old string found once in L-4 and once in the UPDATE): with (i) alone L-4 → sha1
4094ef917ea427d5dfe32cbf60295ade92bd8fef (4,644 bytes) and the UPDATE → 66bfdeac9a908c29032b1f2c6af23ce02f851200 (4,678 bytes); with (i)
and (ii) e970fec2fedce5b83ca50ca5daaca2633774da5e (4,682 bytes) / aed14306bd5e37d257c4c64cf4b1b17964ed884c (4,716 bytes); with (i), (ii)
and the optional DEAD-LEV start 82c5290b15d3c57ee743b12f43a8f9fc2eeed34c (4,705 bytes) / 806154ce34117192b152179606d6ad70a1258f6c (4,739
bytes); all 71 / 71 (UPDATE 70 / 70), 0 "|"; a fixes entry 4 naming itself in the source note would change these sha1s. NOT RUN: the
referees' simulators; scripts/verify.sh; the full check.sh. (5) QUOTE SWEEP (chk116.py: outermost guillemet quotes, whitespace joined,
split at the ellipsis, parts of 6+ characters; sources: the packet, L-1-L-4, the fixes, movescheck.py, movescheck.out, check.sh and
notes/L-NEW.md at fd5c163f, box150/check.py, both referee files at c011995c / 6924e140, notes/CHECKER.md at 1c4ba1c3, C128.md at
2dd44fc1, P-TR3.md at d3e3cde8 (the R104 wording), RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, NOW, TARGET.md, CLAUDE.md, C120-C127,
R111-, R114- and R115-draft at the local trunk, the commit subjects of the cited commits, my re-run outputs): 462 outermost quotes, 394
parts of 6+ characters, every part found (0 not found); in the title and body alone 114 quotes, 105 parts, 0 not found; GAPS preamble
and UPDATE 14 quotes, 10 parts, 0 not found. Line-precise: 92 of 92 (source, cited line range, quote) triples found verbatim,
whitespace-normalised, inside the cited lines. Every sha1, line count and commit time cited was re-measured in this session (sha1sum, wc
-l, git log -1). STALE STATUS in title and body (by script): «pending» 0 apart from the title fill «checker PENDING)»; «not yet» 0; «not
landed» 0; «unlanded» 0; «provisional» 0; «to follow» 0; «stays OPEN» / «stay OPEN» 2 (the title's own «G-N5-TIME stays OPEN» and the
TARGET.md diff's quotation of L-4's tail); «L-5» 0; «R115» 0; «MOVES-2D» 7 times, never with «DEAD», «killed», «false» or «refuted» (0);
L-1-L-3 only as history. (6) DISCREPANCIES: (11) D-1 to D-5. I found no error in a signed statement. (7) FLAGS FOR THE LEAD AND CHECKER:
G-0 (C129 free; C128 = R115, FAIL E-1..E-5 at 2dd44fc1), G-9 (i) (REDUCE-XI's «equality on 59,502» counts T = 1 + #{t ≤ T − 1 : Mv_t ∩ Z
≠ ∅}, not the line's T = 1 + Σ_(z ∈ Z) moves(z), which holds on 8,399 runs; exact replacement), G-9 (ii) (DEAD-SEG: no start for
pass_d3_D3 and pass_d4_D4, whose stored starts do not reproduce D 3 and 4; exact replacement), G-S (MOVES-2D: no status claim, not a
route), G-P (placement A or B), G-U (R111's DEAD-clause step); NOTES G-9 scope and corpus, G-2 (i)-(iv), G-C (overlaps), G-10 (L50
governs the landing scope; the body does not cite it). (8) NOT VERIFIED: the referees' simulator runs (their reports read, not re-run);
L50's MOVES-2D material (not opened, not used); scripts/verify.sh and the full check.sh were not run. (9) LANDING SIMULATIONS
(sim116.py, on in-memory copies of RESULTS and GAPS at the local trunk): (A) R115 NOT landed: RESULTS 13,306 -> 13,540 lines (wc -l), a
pure insertion of 234 lines (the entry block with "checker PENDING)" filled, plus one blank line) directly after R114's landed block
(R114 l. 12,394-12,695, blank l. 12,696, byte-unchanged: True; R110's to R113's blocks byte-unchanged: True): True; R116 at l.
12,697-12,929, blank l. 12,930, **Erratum E-1** moves to l. 12,931, Erratum E-2 to l. 12,944, Note E-3 to l. 12,972, the Dead ends
heading to l. 13,003; order R110, R111, R112, R113, R114, R116, E-1, E-2, E-3, Dead ends: True; every other line byte-unchanged (common
prefix and suffix: True); 0 "|" inserted. GAPS: only l. 11 changes: True; new l. 11 = old l. 11 with its closing " |" replaced by " " +
the filled UPDATE + " |": True; "|" on l. 11 76 -> 76; UPDATE 2026- heads 49 -> 49 plus 1 UPDATE head with the simulation year 2099,
directly after R114's and now the last on the line; 23 -> 23 lines (wc -l). (B) R115 landed first (from docs/agents/R115-draft.md as it
stands, sha1 bc987999…, its slice and UPDATE; fill 2099-01-04 00:00 1111111): RESULTS 13,306 -> 13,596 (R115, pure insertion: True) ->
13,830 lines, R116 a pure insertion of 234 lines directly after R115's block (R115 l. 12,697-12,985, blank l. 12,986, byte-unchanged:
True): True; R116 at l. 12,987-13,219, blank l. 13,220, **Erratum E-1** at l. 13,221, Erratum E-2 l. 13,234, Note E-3 l. 13,262, Dead
ends l. 13,293; order R110-R116, E-1, E-2, E-3, Dead ends: True; 0 "|" inserted. GAPS: only l. 11 changes: True; R116's filled UPDATE
appended after R115's, now the last on the line: True; "|" on l. 11 76 -> 76 -> 76; 23 -> 23 lines. Fill values used only for the
simulations: <DATE> 2099-01-05, <HH:MM> 00:00, <checker> 0000000. (10) THIS DRAFT'S SHA1: a file cannot state its own sha1. The sha1 of
this file with the forty hex digits after the next colon replaced by forty «0» characters is: ba7447b1b5238406715ab83a57117c723ddb0d0e. The file's actual sha1 and
line count are in the hand-back to the Lead (and re-measurable with sha1sum). Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r116/ (runw187.sh / w187.out,
tools/g9split.py / g9split.out, tools/deadstart.py / deadstart.out, tools/wdiff116.py / wdiff116.out, tools/prem116.py / prem116.out,
tools/upd116.py / upd116.out / upd116L4.txt, tools/fill116.py, R116-template.md, tools/chk116.py / chk116.final.out, tools/sim116.py /
sim116.final.out / sim116.summary, archfd5c/).
