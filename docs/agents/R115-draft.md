# Draft RESULTS R115 (Lead; first fill 2026-11-07T01:03:12Z by date -u (subagent) on P-IDEAL-IM line L-2, docs/si/P-IDEAL-IM-line-L2.txt, l-si 4ee9fa78, sha1 8b7ccfb9a050955758452dc04fe5aafc58468680 (draft sha1 bc987999, CHECKER C128 2dd44fc1: FAIL E-1..E-5); SECOND FILL 2026-11-07T03:02:04Z by date -u (subagent) on P-IDEAL-IM line L-3, docs/si/P-IDEAL-IM-line-L3.txt, l-si 80d1422a, sha1 cf510950a7feaf3e8d5f3c316acc2601e2ed17e7) — to CHECKER C128 Add. 1 — NOT LANDED; goes after R114, before Erratum E-1
SECOND FILL (2026-11-07T03:02:04Z by date -u, subagent; for CHECKER C128 Add. 1). Read at the origin heads fetched at its start (git
fetch, 2026-11-07T03:01Z, no Lead push running, pgrep empty) and re-fetched at 2026-11-07T03:09:23Z: l-si 77d536f6 (its ancestor
80d1422a holds fixes entry 2 and line L-3; the packet, L-1, L-2, L-3, the fixes, experiments/si/box75/ (imcheck.py, imcheck.out,
check75.sh, mkL3.py, pins.sha1, pins_fix2.sha1, frame_P-IDEAL-IM.py), box64/, box68/, box70/ and experiments/si/check.sh are byte-equal
at 80d1422a and 77d536f6, git diff empty; 77d536f6 adds L-SI box 77 work and changes no P-IDEAL-IM file), referee 3fb22563 (0c2a7c5b, §C
add. 1 of R-P-IDEAL-IM.md, the L-3 round, then 3fb22563, which corrects that section's guessed header time to its commit time; the
file's l. 1-164 = bc2bdd5a's, by diff), referee-2 0a9e2a16 (Addendum 2 of R2-P-IDEAL-IM.md, the L-3 round; its l. 1-153 = 2e68c641's
file, by diff), checker 2dd44fc1 (docs/checker/C128.md, 2026-11-07T01:46:51Z, 135 lines, sha1 bc16269482429ea2f3b3cfc01730f5de555d1494;
already an ancestor of origin trunk); origin trunk 663c6447 («Lead: L-NEW 58 row; R116 draft to C129; IM L-3; P-M2D-DEAD and REACH
routing; log»), pushed, which holds the first-fill draft bc987999 (commit fc665614, an ancestor). Local trunk d6410595 = four merges
(--no-ff, none an ancestor of 663c6447 before) into 663c6447: 256e7461 (l-si 77d536f6), d06fff51 (referee 0c2a7c5b), 909706e4 (referee-2
0a9e2a16), d6410595 (referee 3fb22563, fetched after the first three merges); then the commit holding this file. Not pushed; 80d1422a,
0c2a7c5b, 3fb22563 and 0a9e2a16 are NOT ancestors of origin trunk 663c6447 (git merge-base --is-ancestor); the Lead pushes trunk before
landing. RESULTS (sha1 555d41bd85b8ea52a1e57459c0a4fe0fcb7f6cc1, 13,306 lines), GAPS (sha1 3c4ff44d1b822110d9bfd0d1a2d8661ea6b5361e, 23
lines), TARGET.md and CLAUDE.md are byte-equal at fc665614 and the local trunk (git diff, empty; last commit on RESULTS and GAPS:
b6d1484b, R114's landing). DECISIONS and DECISIONS-INDEX add only Lead reading L50 (2026-11-07 01:42Z; MOVES-2D killed, landing scope of
P-IDEAL-MOVES), which does not bear on this entry (the title, the entry and the UPDATE name neither MOVES-2D nor P-IDEAL-MOVES, by
script); docs/NOW.md and LEAD-STATE changed (resume points) and the entry cites no changed text of either. So the first fill's premise
checks and GAPS state stand (L-3's premise parenthesis is L-2's, by script), and Addendum 2 re-runs the landing simulation. New sources:
docs/checker/C128.md: FAIL E-1..E-5, all DATA wording (the first fill's G-9 (v), (iv), (iii), (ii), (i): LOCAL's set, BIT-CHAIN (i) at
the c-step images, the box 64 cross-check on 301 genomes, the NEG control's K-part count, BIT-CHAIN (ii) without a counter), every
E-item confirmed by the CHECKER's own instrumented runs (§3); RULING G-M / G-R (l. 65-75): a second, referee-owned RUP checker is «not
required», with the landing condition «if any referee file on origin at landing reports that a second checker REJECTS the proof, R115
does not land.»; note N-1 (l. 24-26: «every start» covers every start up to the level-0 states), N-2 (l. 39: the negated-bit control
fires by construction, «true as written»), N-3 (l. 90-91: IM is stated for degree-2 movers of any acyclic genome, its DATA is on ISO 𝓛^R
genomes); G-2 (ii) a note, with the recommended fixes-entry sentence «(Φ2) is R105 LOCAL (the proof of Lemma IM (a), l. 72, does not use
that y is unhappy)» (l. 76-81); G-10 (L49) PASS, G-C a note, G-U PASS, quotes 0 not found, placement PASS; L-3 = L-2 with the five
replacements R1-R5 of §5 (l. 103-114), expected L-3 sha1 cf510950… and rebuilt UPDATE sha1 39d9a292… (l. 115-118); the second-fill list
(l. 119-123). Line L-3, docs/si/P-IDEAL-IM-line-L3.txt (l-si 80d1422a, 2026-11-07T02:07:37Z, the file's only commit; sha1
cf510950a7feaf3e8d5f3c316acc2601e2ed17e7 with newline, 4,962 bytes, = C128 §5's value); fixes entry 2 (docs/si/P-IDEAL-IM-fixes.md l.
57-79 at 80d1422a, L-SI successor 41; file 79 lines, 6,919 bytes, sha1 e80dee09d73db36dd5b604814c171a04b5b42fc4, l. 1-55 = entry 1's
file, by script; the CHECKER's wording note for FRAME's proof at l. 72-73); REFEREE successor 25's byte test and DATA check of L-3
(docs/referee/R-P-IDEAL-IM.md §C add. 1, l. 166-192, 0c2a7c5b, 2026-11-07T02:30:13Z; header time corrected by 3fb22563; file sha1 at
3fb22563 60778fdab1c08d1a341e85979e65ea927ba6d12b, 192 lines: l. 191-192 «Verdict: fixes entry 2 is CORRECT. L-3 MATCHES, by the byte
test and in meaning, with the DATA rule clause by clause. All items stay SIGNED.»); REFEREE-2 successor 29's byte test and DATA check of
L-3 (docs/referee-2/R2-P-IDEAL-IM.md Addendum 2, l. 155-172, 0a9e2a16, 2026-11-07T02:31:16Z, file sha1
78545a522b0bce76bc74ba0f9f6f3485ce298343, 172 lines: l. 172 «Verdict: fixes entry 2 **CORRECT**; **L-3 MATCHES** (Opus 5.5, D1).
Statement verdicts unchanged.»). REFEREE successor 25's «R-P-IDEAL-IM Addendum 1» (ref_rup_del on the 2.4 GB proof): NOT on origin at
2026-11-07T03:09:23Z (claude/referee 3fb22563; R-P-IDEAL-IM.md has no such section; notes/REFEREE.md last changed at e1815909); PENDING,
optional by C128's ruling; no referee file on origin reports a second checker's verdict, accepting or rejecting, so the landing
condition is met at this fill. My byte test of L-3 (fill2/l3rel115.py, rc 0): the five old / new pairs parsed by script from C128 §5 l.
105-114 (wrapped lines joined by one space, outermost guillemets), each old string once in L-2 and once at its turn, L-2 with R1-R5 =
L-3 (True), L-3 byte-equal at 80d1422a and the l-si head (True); fixes entry 2's table (l. 67-71) carries the same five pairs (True); 86
«(» / 86 «)», depth never negative, 0 "|", 8 token hunks; and the G-9 check: every DATA clause L-3 states, 15 phrases each found once in
L-3's DATA parenthesis, against the frozen imcheck.out, compose.py's lines, my first-fill splits (imsplit.out, compsplit.out) and the
figures of C128 §3 and both referees' third rounds: all agree (True). Re-runs: the check.sh block «# box 75 (packet P-IDEAL-IM: …)» from
a git archive of 80d1422a's experiments/si and docs/si (check.sh l. 1-6 and l. 1237-1239; 2026-11-07T03:02:24Z-03:02:32Z, rc 0, «box 75
P-IDEAL-IM checks + witness + COMPOSE seed 68: PASS», «box 75 certified CNF regenerated: PASS», «si (box 75: P-IDEAL-IM): PASS»;
check75.sh at 80d1422a also re-makes L-3 by mkL3.py and compares it, fill2/runw75L3.sh, w75L3.out); the UPDATE rebuilt from L-3
(fill2/upd115b.py: upd115.py's 18 controls and R115 procedure unchanged, run on L-3; the controls' 58 output lines byte-equal to the
first fill's, cmp; it equals the first fill's UPDATE with C128 §5's R1-R5 parsed by script, True; sha1
39d9a2925c2c193193f3b0845b37919defa75a2b = C128 §5's, True); the quote sweep, the stale-status grep, the word diff and the landing
simulation (Addendum 2). Changed at this fill, and nothing else: this header line and this paragraph; the title (L-3); in the entry,
Object (fixes entry 2, the line of record L-3, L-2 moved into the line history, the L-3 byte tests, L-3 changes no definition), Claims
signed (the third rounds), (f) FRAME's proof sentence (C128 §4's wording, «(Φ2) is R105 LOCAL …»), «The RESULTS line (L-3)», What rests
on the machine (viii) (the state on origin at this fill and C128's ruling), Premise (L-3), L41 and L43 (entry 2 carries no proof), Fixes
(entry 2: the header, a note on F-3, two new bullets, the closing sentence), Not signed (the packet's table row behind E-1), Referee
strengthening (iii) (new), Honest limits (iii) and (iv) (C128's ruling; L-3's sets and units; N-1, N-3), Data (imcheck.py unchanged at
80d1422a, the box 64 cross-check's 301 genomes, check75.sh at 80d1422a, L-3's DATA parenthesis, N-2, the block re-run at 80d1422a),
Signatures (REFEREE §C add. 1 and the header-time correction, Addendum 1 PENDING, REFEREE-2 Addendum 2, the lane commit), INDEPENDENCE
(L-3; the third rounds), TARGET.md diff (L-3); the GAPS preamble and the UPDATE (rebuilt from L-3); the digest of Addendum
(10); Addendum 2 (new). The FIRST FILL text below (from FIRST FILL (this text) to (14)) and Addendum (1)-(9) are kept byte-unchanged as
the record of the fill on L-2: where they call L-2 the title line or the current line, quote L-2's DATA phrases as the line's, flag G-9
(i)-(v), G-2 (ii), G-M or G-R for a ruling or propose wordings for them, call REFEREE successor 25's Addendum 1 pending at e7047ace, or
give the first fill's line numbers, counts and UPDATE sha1, they describe draft bc987999 at 01:11Z; C128 ruled G-9 (i)-(v) E-5, E-4,
E-3, E-2, E-1, G-2 (ii) a note, G-M / G-R not required with the landing condition, G-U and G-10 PASS, used the number C128 (G-0), and
the entry block follows L-3.
EDIT AFTER THE SECOND FILL (2026-11-07T04:11:27Z by date -u, subagent, at the Lead's request; for CHECKER C128 Add. 1). REFEREE
successor 25's «R-P-IDEAL-IM Addendum 1» is on origin: claude/referee 47d6cfdfd70af78218ad369442e2e9d75aab06e6 (2026-11-07T03:38:06Z,
pushed behind 008039cc and f66942c1; fetched 2026-11-07T04:10:10Z by date -u, after no push.sh was running, pgrep empty), merged into
the local trunk as eed80482 (--no-ff), so the local trunk is 663c6447, the four merges 256e7461, d06fff51, 909706e4, d6410595, the
second-fill commit 3c428cde, the merge eed80482 and the commit holding this file. R-P-IDEAL-IM.md at 47d6cfdf: 224 lines, sha1
8754b6f9c06e7df86859d0cefb0169d66095064d, l. 1-192 = 3fb22563's, by diff; the addendum is l. 194-224, VERIFIED by REFEREE's own
ref_rup_del. Changed by this edit, and nothing else: this paragraph; in the entry, What rests on the machine (viii) (a second,
independent acceptance; drup.c stays the checker of record), Honest limits (iii) (the sentence that no second checker had accepted is
replaced by the acceptance) and the Signatures (Addendum 1 cited); the digest of Addendum (10). The title, L-3 and the UPDATE are
byte-unchanged (by script). The SECOND FILL paragraph above and Addendum 2 describe draft 6b56786d (3c428cde) at 03:14Z, when Addendum 1
was PENDING; they are kept as that record, and their line numbers, slice and counts are those of 6b56786d. For this file: the title is
l. 542 (= prefix + L-3 + fill: True, chk115c.py); the entry block is l. 542-915 (python slice d[541:915], 0 "|"), the GAPS preamble l.
917-928, the UPDATE l. 929 (d[928], sha1 39d9a292…, unchanged); a landing script slices d[541:915] and reads d[928]. Quote sweep
(chk115c.py: chk115b.py's rule and sources plus R-P-IDEAL-IM.md at 47d6cfdf and draft 6b56786d): 592 outermost quotes, 502 parts of 6+
characters, every part found (0 not found); in the title and body alone 185 quotes, 167 parts, 0 not found; GAPS preamble and UPDATE 14
quotes, 10 parts, 0 not found. Line-precise: 133 of 133 (source, cited line range, quote) triples found verbatim, whitespace-normalised,
inside the cited lines. Stale grep: «pending» 0 in the title and body apart from the title fill «checker PENDING)». Landing simulation
(sim115b.py, unchanged): RESULTS 13,306 -> 13,681 lines, a pure insertion of 375 lines after R114's block, R115 at l. 12,697-13,070,,
E-1 l. 13,072, E-2 l. 13,085, E-3 l. 13,113, Dead ends l. 13,144; GAPS only l. 11 changes, 76 «|» kept, the new UPDATE last: True.
FIRST FILL (this text). Read at the origin heads fetched at 2026-11-07T00:53:20Z (git fetch, after the Lead push running at the start of
this fill had ended; pgrep empty): l-si 91d40ec2 (its ancestor 4ee9fa78 holds fixes entry 1 and line L-2; the packet, L-1, L-2, the
fixes, experiments/si/box75/, box64/, box68/, box70/, box71/, box72/-box74/, unsat_regen.sh and UNSAT-LIST.txt are byte-equal at
4ee9fa78 and 91d40ec2, git diff empty; 91d40ec2 adds L-SI box 76 and appends its block to experiments/si/check.sh after l. 1239, leaving
l. 1-1239 unchanged), l-comp cf2e0e4f (experiments/comp/box27/log/lsi_q1_cert.txt and drup.c byte-equal at 39aec370 and cf2e0e4f),
referee e7047ace (docs/referee/R-P-IDEAL-IM.md last changed by bc2bdd5a, §C; e7047ace and its parents add R-P-IDEAL-MOVES text and
scratch/ref_rup_del.c), referee-2 f6bafb36 (merge of 2e68c641, the final R2-P-IDEAL-IM.md), checker 1c4ba1c3 (C127 CLOSED; docs/checker/
ends at C127.md); origin trunk 96f4d708 («Lead: sweep 00:02Z; L-SI 41 (box 76) and L-LOWER 3 (box L3) started; MOVES fix round 2 routed;
log»), pushed. Local trunk 9f1806f8 = five merges (--no-ff, none an ancestor of 96f4d708 before) into 96f4d708: 64164445 (l-si
91d40ec2), 16a4af14 (l-comp cf2e0e4f), 63ca6c68 (referee e7047ace), c873af44 (referee-2 f6bafb36), 9f1806f8 (checker 1c4ba1c3); then the
commit holding this file. Not pushed. 4ee9fa78, bc2bdd5a, 2e68c641 and e1815909 are NOT ancestors of origin trunk 96f4d708 (git
merge-base --is-ancestor); the Lead pushes trunk before landing. The body makes NO statement about trunk (C113 E-2). RESULTS (sha1
555d41bd85b8ea52a1e57459c0a4fe0fcb7f6cc1, 13,306 lines), GAPS (sha1 3c4ff44d1b822110d9bfd0d1a2d8661ea6b5361e, 23 lines; l. 11 76 "|", 49
«UPDATE 2026-», the last one R114's), TARGET.md, DECISIONS, DECISIONS-INDEX, NOW and CLAUDE.md are byte-equal at 96f4d708 and the local
trunk (git diff, empty). Last commit on RESULTS and GAPS: b6d1484b (2026-11-06T21:57:54Z, R114's landing).
Sources read: the packet docs/si/P-IDEAL-IM.md (frozen cb2b0c60, 2026-11-06T14:29:25Z, sha1 7bef94196bdc6069f254e19aab9ecef1f0f16b95,
279 lines, 24,188 bytes; read in full), line L-1 (cb2b0c60, sha1 493cac992f366a8efd5641f4c069813bf6e3f254, 4,448 bytes), fixes entry 1
(4ee9fa78, 2026-11-06T21:46:26Z, docs/si/P-IDEAL-IM-fixes.md, sha1 15edc7d1bfecdb4f1edf55b0eb861e6333d437ef, 55 lines, 4,290 bytes),
line L-2 (4ee9fa78, sha1 8b7ccfb9a050955758452dc04fe5aafc58468680, 4,615 bytes); experiments/si/box75/imcheck.py (sha1
f69e38ac59fb944c282f9b8660ac87b4f8171e91, 111 lines; read in full), imcheck.out (sha1 2b0e08a67e9c8b5bf48948cfb50752d815e477f5, 4
lines), the frozen encoder frame_P-IDEAL-IM.py (sha1 c3b3a232e8ba56b6c6ed64511e2a24d1842e1f62, 191 lines; =
experiments/si/box70/frame.py at 4ee9fa78, by sha1), check75.sh (sha1 1cf7966abaecd21a82aee9025ee62f27f0b180cc at 4ee9fa78, 23 lines;
0180d761… and 20 lines at cb2b0c60), pins.sha1 (sha1 ce33dc7e…, 2 lines: the encoder and the witness), experiments/si/box68/compose.py
(sha1 895d4026440bb5def5b84b159a31532908b5ef8c, 75 lines, its only commit b4404b06; read in full; there is no
experiments/si/box75/compose.py), experiments/si/box64/flipdp.py (Ext; sha1 c02e00f6…), box70/check70.sh, box70/log/3_t1_11.log,
experiments/si/unsat_regen.sh and UNSAT-LIST.txt (the line «m 3 t1 11 (box 70)»), experiments/si/check.sh block «# box 75 (packet
P-IDEAL-IM: …)» (l. 1237-1239 at 4ee9fa78; the file 1,239 lines, sha1 28f6cc178e52abe5802cae59405d5b5f67577b9e),
docs/si/N5-FRAME-box70.md §0; claude/l-comp experiments/comp/box27/log/lsi_q1_cert.txt (39aec370, 2026-11-06T07:00:36Z, 7 lines, sha1
caae5fe1e83017a08d7377c2ccccceb92032defc), experiments/comp/box27/drup.c (sha1 2d4b8eab8fe9e9035c396733bb400d9d6e7d2366) and
out/bfk_m2_part0-3.txt (557b045b); the witness experiments/si/box64/wit/kf1_d4_t10.json (sha1 1c0dc8cc5a8dd382e028d199f96f783f995b9a5a,
= claude/l-new experiments/new/box160/out/kf1_d4_t10.json); REFEREE successor 24's docs/referee/R-P-IDEAL-IM.md (report 0e24d8ca, §C
bc2bdd5a) and notes/REFEREE.md at e7047ace (successor 25's handover check); REFEREE-2 successor 28's docs/referee-2/R2-P-IDEAL-IM.md
(draft 7856e7a9, fix round 280d2313, final 2e68c641) with R2-P-IDEAL-IM/r2cstep.py and r2checks_seed75.out (listed, not re-run); RESULTS
R104 (title l. 9864), R105 (l. 10155), R110 (l. 11323), R111 (l. 11598), R112 (l. 11909), R113 (l. 12152), R114 (l. 12394-12695),
Erratum E-1 (l. 12697), E-2 (l. 12710), Note E-3 (l. 12738), Dead ends (l. 12769); GAPS l. 11; DECISIONS L49 (l. 432-438) and
DECISIONS-INDEX l. 44; docs/agents/LEAD-STATE.md (2026-11-06 entries to 2026-11-07 00:01Z); docs/checker/C120.md-C127.md;
docs/agents/R112-draft.md and R114-draft.md as landed (the models of this draft).
Re-runs (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r115, from a git
archive of 4ee9fa78's experiments/si and docs/si, nothing written into the repository): (a) check.sh block «# box 75 (packet P-IDEAL-IM:
…)» (experiments/si/check.sh l. 1-6, the shebang, comment, «set» and «cd» lines, then l. 1237-1239; runw75.sh, w75.out),
2026-11-07T00:55:25Z-00:55:33Z, rc 0, lines «box 75 P-IDEAL-IM checks + witness + COMPOSE seed 68: PASS», «box 75 certified CNF
regenerated: PASS», «si (box 75: P-IDEAL-IM): PASS» (python-sat 1.9.dev15 present, so the CNF regeneration ran: the frozen encoder
printed sha1 7e611c8bdf53a70a398e9e1ec3b220a1b79e2507); (b) my split of imcheck.py's counter sets (imsplit.py: the frozen source exec'd
unchanged with argv 400 75, its output equal to imcheck.out, True; then my own measurements on its own 404 genomes; my DATA, not lane
DATA, not wired into check.sh); (c) my split of compose.py's two counters (compsplit.py: compose.py's own functions exec'd unchanged,
its main loop replicated with seed 68; KPART and GPART reproduced exactly, 0 / 0 and 21,234 / 54,433); (d) box70/check70.sh from the
same archive (2026-11-07T00:56:59Z-00:57:02Z, rc 0, «box 70 frame m = 2 validation: PASS»); (e) the L-1 → L-2 token diff (wdiff115.py);
(f) the premise quote test (prem115.py); (g) the UPDATE build with 18 controls (upd115.py); (h) the quote sweep, the stale-status grep
and the landing simulation (chk115.py, sim115.py).
LESSONS APPLIED. C113 E-1: the title is L-2 verbatim with no insertion. C114 Add. 1 E-1: the UPDATE head carries «<DATE>». C115 E-1: the
premise route is checked against what RESULTS records (G-4; prem115.py, hits per quote). C116 G-1, C118-C127 §4: the UPDATE rule of R111
(sentinel_build111 with its default drops and the «(DATA, » opening, and the clause step for an unlabelled clause), one adaptation
flagged (G-U). C116 G-2: name clashes settled by one body sentence (G-6). C117 E-1 / E-2: no sentence wider than signed (two flags, G-2
(ii), G-9 (v)). C118 E-1: no stale status sentence; the one open referee item is marked as such and flagged (G-R). C118 §3 / Erratum
E-2: EVERY DEFINITION of L-2 diffed against the packet (G-2). C120 §5 / C121 §5 / C122 E-2 / C124 E-1 / C125 E-1 / C127 E-1: EVERY DATA
clause of L-2 tested against imcheck.py's and compose.py's counter code: unit, set, and the statement's scope (G-9; five clauses
flagged). C122 G-0: parentheses balanced (G-1). C122 E-3: the source note names every proof-carrying file (G-1). C123 E-1: no lane label
and no packet name in the title before the claims (G-1). C123 E-2: no stale referee state (G-13, G-R). C119 E-1: every «referee X did Y»
is checked against that referee's file. R112 / C123 §3 / C127 G-M: the machine item says exactly what rests on the machine: the encoder,
the CNF sha1, the solver, the proof sha1, the checker runs and the result (body «What rests on the machine»; G-M).
to check: FLAGS FIRST (G-0 to G-14; the ones for the Lead or CHECKER: G-0 (number), G-9 (i)-(v) (DATA: BIT-CHAIN (ii) not in the no-DATA
list, the C127 E-1 class; COMPOSE's «K's part» control count; the box 64 cross-check's genome set; BIT-CHAIN (i)'s state set; LOCAL (IM
(a))'s set), G-2 (ii) (FRAME's «(Φ2) is Lemma IM (a)» uses IM (a) outside its stated hypothesis), G-M (what rests on the machine: one
checker program, three runs; no independent checker finished), G-R (REFEREE successor 25's Addendum 1: PENDING), G-U (one UPDATE
adaptation), G-10 (L49 and COMPOSE-LB's W-ONLY), G-C (overlap with landed R105, R110, R111, R113, R114)), then the CLEAN items and
(0)-(14).
- G-0, THE CHECKER NUMBER. docs/checker/ ends at C127.md (C127 = R114); docs/checker/C128.md does not exist; «C128» occurs 0 times in
  RESULTS and GAPS; on the origin heads it occurs only in notes/CHECKER.md (l. 7 «NEXT (Lead 22:18Z): R115 (P-IDEAL-IM) when its L-2
  MATCHES at both referees, then R116 (P-IDEAL-MOVES). Use C128, C129.») and in docs/agents/LEAD-STATE.md (the 22:19Z resume point: «->
  CHECKER 19 C128»). «R115» occurs once in RESULTS, as L-RED's box R115 (G-6). This draft uses C128 (title fill, UPDATE head, GAPS
  preamble).
- G-9, DATA (the C120 §5 / C121 §5 / C124 E-1 / C125 E-1 / C127 E-1 check item: unit, set and the statement's scope of every count,
  against imcheck.py's and compose.py's counter code, read by me in full at 4ee9fa78). Every figure of L-2's DATA parenthesis equals
  imcheck.out, compose.py's output and my re-runs: «404 ISO genomes» = «genomes 404» (400 random from gen(m) with m ∈ {1, 2, 3}, i.e.
  𝓛^R_2: 131, 𝓛^R_3: 123, 𝓛^R_4: 146, plus 4 real m 3 pins of boxes 72-74 in 𝓛^R_4; all 404 ISO, Ξ-acyclic by my depth-first search and
  wired as 𝓛^R, by script); IM 31,208, LOCAL 250,248, independence 66,520, BIT-CHAIN 66,520 with the control 66,520, KEY-DIR 133,040,
  VALUE-MONO 133,040, frame step 24,184, the box 64 cross-check 18,944, the IM control 6,284 = imcheck.out l. 1-3; COMPOSE 0 / 0 and
  21,234 / 54,433 = compose.py's last line (my re-run (a) and split (c)). Counter by counter (imcheck.py line numbers):
  - «every start» (l. 64-65): every upper state, with the level-0 movers at (0, 0) («st = [0, 0] + list(up)»); under ISO the c-step on
    the levels ≥ 1 reads no level-0 state (A-sets: no chain passes 0 or 1; keys at level 1 are (κ^c_w, gate)), so «every start» is every
    upper start. Note.
  - IM (l. 92-96), once per state (the c = 0 pass, l. 83): per (state, z, y ≠ z) with y unhappy and on at least one chain of z; (b) if
    on both, (c) otherwise; the control counts (c) only, with the direction reversed. «once per state: IM (b), (c) 0 violations on
    31,208 checks, (c) with the direction reversed failing 6,284 times»: MATCH (unit, set). REFEREE §C l. 151; REFEREE-2 l. 106-107.
  - (v) LOCAL (l. 91) (FLAG, set wider than the named statement): per (state, z, y ≠ z) with y on neither chain of z, for ANY y, happy
    or unhappy. My split (imsplit.py): 125,124 of the 250,248 with y unhappy (IM (a)'s hypothesis, packet l. 66 «Let z ≠ y be movers of
    degree 2, s a state with y unhappy at s, and s′ := s ⊕ e_y.») and 125,124 with y happy. So «LOCAL (IM (a)) 0 on 250,248» counts the
    frame's (Φ2) (packet l. 192, no unhappiness hypothesis); as a count of IM (a) in its stated form the set is 125,124. The count is
    right for LOCAL; the parenthesis «(IM (a))» names a narrower statement. REFEREE-2 l. 106-107 «FRAME_LOCAL counts y on neither chain
    (any y).» saw it; neither referee asked for a change. Bears on G-2 (ii). CHECKER: note or E-item (one possible wording, not mine to
    choose and not a quotation: "LOCAL (IM (a)) 0 on 250,248" → "LOCAL (IM (a), any y off both chains) 0 on 250,248").
  - independence of s(z) (l. 86), once per state: per (state, upper mover z): MATCH (66,520).
  - (iv) BIT-CHAIN (i) (l. 76-79) (FLAG, set): per (state, c, level l = 1..m), the bits are computed from ns = the c-step of the state
    and compared with the keys under ns: BIT-CHAIN (i) is tested at the c-step image u′ of each (state, c), not at every state. My
    split: the 24,184 (genome, c, state) triples have 5,670 distinct images; the c-step is onto the upper states for 63 of the 808
    (genome, c) pairs. So «per state and both c: BIT-CHAIN (i) 0 on 66,520» is one check per (state, c, level), but on the 5,670 image
    states (counted with repetition), while BIT-CHAIN (i) is stated for «a state s». Its control «the negated bit failing 66,520 times»
    fires at every check that passes (l. 79, «(1 - b[l]) != kb»): exact, and equal to the count by construction. CHECKER: note or E-item
    (one possible wording, not mine to choose: "BIT-CHAIN (i) 0 on 66,520" → "BIT-CHAIN (i) at the c-step successor 0 on 66,520").
  - (i) BIT-CHAIN (ii) (FLAG, the C127 E-1 class: a clause half with no counter and not in the no-DATA list). L-2's BIT-CHAIN clause has
    two parts: (i) «satisfy b_l = [key(A_l) < key(B_l)] under R110's c-step keys» and (ii) «and a level-l mover prefers by key its
    option 0 iff b_(l−1) = 1». imcheck.py has no counter for (ii) (REFEREE-2 l. 108 «BITCHAIN tests (i) only: b_l = [key(A_l) <
    key(B_l)]. (ii) has no counter.»; fixes F-3 l. 43 «part (ii) is not counted separately; it enters KEY-DIR's prediction»). L-2's DATA
    names «BIT-CHAIN (i)» and its no-DATA list is «COMPOSE-LB and the T_∞ bound: no separate DATA», without (ii). (ii) does NOT follow
    by arithmetic from the counted checks (the C125 G-9 (iii) test): KEY-DIR's count implies the key preference only for the unhappy
    movers of the checked c-step images. REFEREE-2's W-1 required exactly this item: l. 128-129 «BIT-CHAIN (i) 0 on 66,520, the negated
    bit failing 66,520 times (BIT-CHAIN (ii): no separate DATA)»; L-2 carries «BIT-CHAIN (i)» but not «(BIT-CHAIN (ii): no separate
    DATA)», and REFEREE-2's fix round accepted it (l. 144 «BIT-CHAIN is now «(i)».», l. 153 «W-1 and W-2 are met.»). Per the brief the
    line is not changed here; CHECKER rules E-item or note. If E: one possible L-3 wording, not mine to choose and not a quotation: the
    old string "COMPOSE-LB and the T_∞ bound: no separate DATA" (once in L-2, by script) → "BIT-CHAIN (ii), COMPOSE-LB and the T_∞
    bound: no separate DATA" (or REFEREE-2's W-1 form at the BIT-CHAIN count).
  - KEY-DIR (l. 80-82), per (state, c, upper mover): «moves iff u(x) = b_(l−1) and C_x(u) ≠ b_(l−1), with the bits of u′»: MATCH
    (133,040). Its consequence «so the c-step depends on the gates only through c and the bits [g(A_l, k) < g(B_l, k)], l < m» has no
    counter of its own and is not in the no-DATA list; it follows from the counted FRAME_STEP check (the frame step reads the gates only
    through those bits, l. 104-106, and equals the c-step at every (state, c) of the 404 genomes) (NOTE, C125 G-9 (iii) class).
  - VALUE-MONO (l. 71-74), per (state, c, upper mover): no value falls, a moved mover's value rises: MATCH (133,040). Its «so in every
    c_t-step sequence, with any number of changes of c, no state repeats among the moving steps» follows by arithmetic on the checked
    genomes (every step of every c_t-step sequence is a checked (state, c) pair) (NOTE); «T_k(m) ≤ T_∞(m) ≤ 2^(2m) − 1» is in the
    no-DATA list («the T_∞ bound»). The packet's §7 l. 271 also lists «Not covered by DATA: NO-REPEAT beyond VALUE-MONO; Fact 0 (used by
    every check).»; L-2's no-DATA list does not name Fact 0, which the line uses only in a definition parenthesis («(the two values
    differ, Fact 0)»); imcheck.py's C() (l. 34) assumes it. NOTE.
  - frame step = c-step (l. 97-108), in the c = 0 pass for both c2: per (state, c2): MATCH (24,184 = 2 × 12,092 states); fixes F-3 l. 48
    describes it «once per state each»; L-2 lists it under «per state and both c»: the same set.
  - (iii) the box 64 cross-check XSTEP (l. 68-69) (FLAG, set): «if E is not None»: Ext(G) of box 64's flipdp asserts «both values of b_0
    must be realisable» and is None on 103 of the 404 genomes (my split: m 1: 39, m 2: 34, m 3: 30; the 4 pins pass), so the 18,944
    (state, c) checks are on 301 genomes (Σ 2 · 2^(2m) over them = 18,944, by script). «per state and both c: … own c-step = the box 64
    simulator 0 on 18,944»: count exact, set narrower than the DATA head «on 404 ISO genomes». CHECKER: note or E-item (one possible
    wording: "own c-step = the box 64 simulator 0 on 18,944" → "own c-step = the box 64 simulator 0 on 18,944 (the 301 genomes the
    simulator accepts)").
  - (ii) COMPOSE (compose.py l. 43-75) (FLAG, unit and meaning of the control count). Per pair: every start of K's and G's upper movers
    and both b_0 (one run each; my split: 41,056 runs, 37,816 composite steps, pairs (1, 1) 51, (1, 2) 48, (2, 1) 48, (2, 2) 53); in a
    run, bad[0] (KPART) counts a step where H's K-part differs from K's step (l. 54) and bad[1] (GPART) a step where H's G-part differs
    from G's step under the schedule (l. 58), each ending the run; after the run, each part counts once more if its state is not stuck
    (l. 63-64). «0 disagreements on 200 random pairs with (m′, m) ∈ {1, 2}²»: MATCH. NEG=1 (l. 56) negates only G's schedule; K's
    comparison (l. 53-54) does not read it. My split of the control: KPART 21,234 = 0 in-run K disagreements + 21,234 end-of-run counts
    of K's state not being stuck, each after a run cut by a G disagreement (K's state is then not advanced); GPART 54,433 = 30,113
    in-run + 24,320 end-of-run. So «the negated schedule disagreeing 21,234 times on K's part» counts no disagreement of K's part with
    K's c-step: it counts runs cut short by a G-part disagreement. The unit is counter increments (at most two per part per run), not
    «times» a part disagrees. REFEREE §C l. 148 and REFEREE-2 l. 140 re-measured the figures (EQUAL), not their meaning. CHECKER: note
    or E-item (one possible wording: "the negated schedule disagreeing 21,234 times on K's part and 54,433 times on G's" → "the negated
    schedule giving 54,433 G-part failures (30,113 in-run) and 21,234 end-of-run K-part failures of the cut runs").
  - COMPOSE's set: compose.py checks with box 64's Ext.step (the composite's IDEAL step with level 0 frozen at a configuration of the
    given b_0), not with an own c-step; the identity of Ext.step with R110's c-step is the XSTEP count on imcheck.py's genomes, not on
    compose.py's; pairs are redrawn when Ext rejects K, G or H (l. 71-73). NOTE.
  - «COMPOSE-LB and the T_∞ bound: no separate DATA»: true (no counter). FRAME's «so T_k(m) ≤ T^Φ_k(m) for every k» is not a finite
    check (T^Φ_k(m) is a supremum over all frame systems); per genome it follows from the counted frame-step check by the deletion
    argument (NOTE).
  - The encoder: «only the m = 2 cross-checks T^Φ_1(2) = 5 against L-COMP's exhaustive T_1(2) = 5»: check70.sh l. 9 runs box70/frame.py
    (byte-equal to the frozen encoder, sha1 c3b3a232…) on «2 t1 5» (SAT) and «2 t1 6» (UNSAT); my re-run (d) PASS; L-COMP's bfk.c
    records out/bfk_m2_part0-3.txt (557b045b) each print «T_1(2) 5». MATCH. The packet's source note for the L-COMP value, «(L-COMP box
    27 bfk.c, as quoted in docs/si/N5-FRAME-box70.md §0)» (l. 269-270), is loose: box70 §0 l. 26 says «the frame reproduces the exact
    enumeration values» and names neither L-COMP nor bfk.c (D-4).
  - SCOPE (NOTE): IM is stated for degree-2 movers of any acyclic genome and BIT-CHAIN / KEY-DIR on 𝓛^R_(m+1) without ISO; their DATA is
    on the 404 ISO 𝓛^R genomes, upper movers only (the R114 G-9 (v) / C125 PATH-RISE precedent).
- G-2, DEFINITIONS DIFFED (my own diff; the C118 §3 / Erratum E-2 lesson). (o) Premise parenthesis = packet l. 19-29 (G-4). «C_z(s) the
  option of a degree-2 mover z of larger value under s (the two values differ, Fact 0)» = §0 l. 55 with Fact 0 l. 58-63; «z unhappy at s
  iff s(z) ≠ C_z(s)» = l. 56; «s ⊕ e_y the state s with y switched» = l. 57; «A_l, B_l the movers 2l, 2l + 1» = l. 50; the BIT-CHAIN
  bits = §2 l. 97-100; «T^Φ_k(m) the largest number of moving frame steps with at most k bit changes» = §5 l. 196-197; the frame Φ_m's
  objects = §5 l. 185-195 (REFEREE l. 121-122 «Definitions diffed against §0 / §5: C_z, unhappy, ch_k, s ⊕ e_y, A_l / B_l, the BIT-CHAIN
  bits, T^Φ_k(m) and the frame's objects all MATCH.»; REFEREE-2 l. 121). Claims: IM = §1 l. 66-69; BIT-CHAIN = §2 l. 97-103; KEY-DIR =
  l. 119-127 (its consequence l. 126-127); VALUE-MONO = §3 l. 132-133 with NO-REPEAT l. 141-143; COMPOSE = §4 l. 148-161; COMPOSE-LB =
  l. 172-173; FRAME = §5 l. 199-202; MACHINE = §6 l. 221 with the trust items l. 222-243 and the witness l. 244-247.
  (i) NOTE. L-2's «ch_k(z, s) the movers on the chain of (z, k) under s» omits the packet's «(z, k) itself excluded» (l. 54 «ch_k(z, s)
    is the set of movers on the chain of (z, k) under s, (z, k) itself excluded.»); read literally L-2's ch_k contains z. Every use has
    y ≠ z (IM: «z ≠ y»; the frame's LOCAL and IM in the same sense), so no clause changes. Both referees MATCHED it.
  (ii) FLAG (C117 E-1 class, in the proof of a signed statement, not in the line). Theorem FRAME (i)'s proof says «(Φ2) is Lemma IM (a);
    (Φ3) is Lemma IM (b), (c).» (l. 207). (Φ2) is «(Φ2) LOCAL: if y ∉ ch_0(z, s) ∪ ch_1(z, s) then C_z(s ⊕ e_y) = C_z(s);» (l. 192), for
    EVERY y ≠ z; Lemma IM is stated only for «s a state with y unhappy at s» (l. 66). For y happy at s, (Φ2) is not an instance of IM
    (a) as stated. It is true: IM (a)'s proof (l. 71-72) uses only R105 LOCAL and never the unhappiness of y, and (Φ2) is R105 LOCAL
    directly (both chains of z avoid y). The frame encoder encodes (Φ2) for every y (REFEREE l. 74, «for y ≠ z: ¬on0 ∧ ¬on1 → C(z, s) =
    C(z, s ⊕ e_y)»), so the MACHINE item needs the wider form. Both referees passed the step (REFEREE l. 59 «(Φ2) by IM (a)»; REFEREE-2
    l. 53 «Φ2 = IM (a)»). FRAME's statement and the line are unaffected. CHECKER: note, or an E-item fixed by one fixes-entry sentence
    (e.g. that (Φ2) follows from R105 LOCAL for every y, as in the proof of IM (a)); not mine to choose.
  (iii) NOTE (G-3). «T_∞(m)» is used in L-2 («T_k(m) ≤ T_∞(m) ≤ 2^(2m) − 1») without a definition; packet §0 l. 50-51 «T_∞(m) is T_k(m)
    with no bound on the changes.».
  (iv) NOTE. «hence T_1(3) = 10»: T_1(3) is R110's supremum over the ISO genomes of 𝓛^R_4; the lower bound needs the witness to be ISO
    and in 𝓛^R_4 (REFEREE l. 100 «in 𝓛^R_4, ISO;»; REFEREE-2 l. 88 «kf1_d4_t10 is ISO and in 𝓛^R_4.»).
- G-M, WHAT RESTS ON THE MACHINE (FLAG for CHECKER; the R112 / C123 §3 item). The MACHINE clause is signed by both referees as a machine
  item (REFEREE l. 21 «SIGN as machine-certified; encoder (M1) audited FAITHFUL (§2 below); the Glucose proof regenerated
  byte-identically (my independent re-checks of it: addendum)»; REFEREE-2 l. 20 «**SIGN as machine-certified** (Opus 5.5, D12): encoder
  audited faithful; CNF and DRUP proof regenerated byte-identically; my drup.c build VERIFIED it; witness replayed; trust base = R112's
  (drup.c, an audited encoder)»). The body's «What rests on the machine» separates (i) PROVED (Theorem FRAME and its consequence), (ii)
  the ENCODER (premise, audited), (iii) the CNF (sha1 7e611c8b…, regenerated five times), (iv) the SOLVER (Glucose 4, not trusted), (v)
  the PROOF (sha1 32be84e4…, 2,388,304,251 bytes, regenerated byte-identically twice, not committed), (vi) the CHECKER (drup.c
  2d4b8eab…, three runs: L-COMP, REFEREE 24, REFEREE-2 28), (vii) the RESULT, (viii) what is NOT independent: unlike R112 (all 16 proofs
  also accepted by REFEREE's own ref_rup, R-P-TR3 Addendum 1), no checker program other than drup.c has accepted this proof at this fill
  (REFEREE 24's ref_rup lost to a restart, §C l. 164; REFEREE successor 25's Addendum 1 pending, G-R; REFEREE-2's r2rup.c «NOT
  FINISHED», l. 83), (ix) CORROBORATION (CaDiCaL 1.5.3, no proof, input sha1 not logged), (x) the WITNESS (not machine). REFEREE 24's
  drup.c run is stated in its committed report (§C l. 161-163) but its log was not committed (notes/REFEREE.md at e7047ace l. 43-44
  «(scratchpad im/drup.log, not committed; record it)»); L-COMP's and REFEREE-2's runs are stated with their counts in committed files
  (lsi_q1_cert.txt l. 4-6; R2-P-IDEAL-IM.md l. 81-82). The line's «with a DRUP proof accepted by the forward RUP checker drup.c of
  RESULTS R112 (sha1 2d4b8eab…; 6,531,220 lemmas; its correctness and the encoder's are premises)» is exact; it does not say who ran
  drup.c (the body does). The machine premise's files are named in the line (encoder path, CNF sha1, drup.c sha1), not in its source
  note (as R114 G-M (c); REFEREE-2 l. 126 «The source note names P-IDEAL-IM.md, the only file with proofs.»).
- G-R, REFEREE successor 25's «R-P-IDEAL-IM Addendum 1» (FLAG for the Lead and CHECKER): PENDING. Not on origin claude/referee at
  e7047ace (R-P-IDEAL-IM.md last changed by bc2bdd5a, 164 lines, sha1 4d19e9fa0808ecc010033c27b82d786da92e409f). On file:
  notes/REFEREE.md (e1815909) l. 10-12, successor 25's STEP 2: CNF regenerated EQUAL, «Glucose 4 proof generation running detached»,
  «write the addendum; push.»; its new checker docs/referee/scratch/ref_rup_del.c (e1815909, sha1 1af2ce03…, «RUP checker applying
  deletions, controls pass» in the commit subject; l. 13-16 its controls). No result of it is cited here and none is invented. The body
  says, in What rests on the machine (viii), that no second checker program has accepted the proof at this fill, and names Addendum 1 as
  the open referee item: a status sentence that goes stale when Addendum 1 lands. If Addendum 1 lands before R115, the Lead re-fills
  (viii) and the Signatures with its verdict (a second fill); if R115 lands first, the sentence must still be true at landing (CHECKER
  to confirm on the landing commit). REFEREE's SIGN does not wait for it: l. 21 signs «as machine-certified» on drup.c, with «my
  independent re-checks of it: addendum».
- G-U, THE UPDATE RULE, ONE ADAPTATION (FLAG). L-2 has seven labelled clauses (IM, BIT-CHAIN, KEY-DIR, VALUE-MONO, COMPOSE, COMPOSE-LB,
  FRAME) and one unlabelled clause, «; and MACHINE: …», before the date. (1) The MACHINE clause: the R110 / R111 / R114 clause step,
  unchanged in form (cut before the build, put back behind the last label «(FRAME)»). (2) ADAPTATION: «(COMPOSE-LB)» follows «, and »
  («… K's part of the new state, and (COMPOSE-LB) the number of steps …»), not «; »; build() ends a clause at the last «; » before the
  next label, which here lies before «(COMPOSE)», so the default build fails (upd115.py: AssertionError, also with step (1) alone).
  upd115.py makes the separator «; and » for the build and restores «, and » after it (one string replacement each way, each found
  once). Result: «… of the new state (COMPOSE), and the number of steps … at most T^R(m′ + m + 1) (COMPOSE-LB); every ISO genome …». The
  two scope prefixes «; on 𝓛^R_(m+1) with A_l, B_l the movers 2l, 2l + 1: » and «; under ISO: » stay in front of their clauses (build()
  keeps the text between a clause's last «; » and the next label), as R110's UPDATE keeps its text. Cross-check: a direct build (each
  label behind its clause with its own separator, the MACHINE clause after «(FRAME)», the tail opened and the two scope sentences
  dropped by string replacement) is equal (True). Everything else is R111's default call (drops, «(DATA, » opening, source parenthesis
  kept, «. G-N5-TIME stays open.»).
- G-4, PREMISE ROUTE (the C115 E-1 class): CLEAN (prem115.py on RESULTS 555d41bd). L-2's premise parenthesis: «premise: R104's
  definition of the model only, no theorem of R104 used; RESULTS R105's ENC and LOCAL; RESULTS R110's definitions of 𝓦_d, 𝓛^R_d, T^R(d),
  ISO, b_0, the c-step and T_k(m), and R110's W-ONLY in COMPOSE-LB only» = packet l. 19-29. Hits, whitespace normalised: ENC (259
  characters) 3: R105's title l. 10155 (the source), R113's body l. 12254-12255 and R114's body l. 12546-12548 (both quote R105
  verbatim); LOCAL (99 characters) 1, l. 10155; W-ONLY (94 characters) 1, R110's title l. 11323; R110's 𝓦_d / 𝓛^R_d / T^R(d) wording
  (packet l. 41-43, 364 characters) 2: R110's title l. 11323 (the source) and R112's body l. 12019-12022 (it quotes R110); R110's ISO /
  b_0 / c-step / T_k(m) wording (l. 43-48, 570 characters) 1, l. 11323. R104: the packet restates the definition in §0 (l. 32-40,
  «RESULTS R104's definition, as restated in RESULTS R105's entry»); R104's own wording (861 characters, as packet P-TR3 §1 l. 7-14
  quotes it) 1 hit, R104's title l. 9864; my diff of §0 l. 33-40 against it: the same objects (W-target of level lev(x) − 1, Ξ-target a
  mover or X, distinct ranks with parities, distinct gates; keys by the W-chain lowest level first under the new state; A-sets under the
  old state), the Ξ-order by ENC (R105, a premise). Use: ENC in Fact 0, IM, VALUE-MONO; LOCAL in IM (a), FRAME (Φ1), COMPOSE's A-sets;
  R110's definitions everywhere in §2-§6; W-ONLY in COMPOSE-LB's proof only (l. 177-178 and fixes F-1 l. 26-29). Not used: packet l.
  28-29 «Not used: any other item of R104-R112, any other RESULTS entry, docs/lit, any other lane file, any outside source.» (R113 and
  R114 are not named; neither is used). The machine premises are §6's encoder and drup.c (packet l. 28-29 «§6 rests in addition on two
  machine premises, named there.»). Erratum E-2 does not bear (G-5). REFEREE l. 26 «every quote is FOUND verbatim in RESULTS (1 hit
  each)»: for ENC and the 𝓦_d wording that holds with R110's / R105's context only (D-2); REFEREE-2 l. 24-25 «is a verbatim substring of
  docs/RESULTS.md on trunk (Python, wrap-normalised). W-ONLY is used in COMPOSE-LB only.».
- G-10, LEAD READINGS AND RULINGS (the C111 E-1 class; the brief's L49 check). L-2 cites no Lead reading and no ruling (by script: «Lead
  reading» 0, «L49» 0). Lead reading L49 (DECISIONS l. 432-438; DECISIONS-INDEX l. 44, active): «RESULTS R110 (IDEAL-FLIP) signs W-ONLY,
  T ≤ T_2(d−1) + 2, for ISO genomes of 𝓛^R_d only.». COMPOSE-LB uses W-ONLY on the composite H, which is ISO by construction (packet §4
  l. 157-158 «and its Ξ-graph is acyclic (the disjoint union of K's and G's, upper parts) and ISO»; F-1 l. 25 «By ISO the level-0
  options lie on no Ξ-chain of an upper option»), and only its step form (l. 177-178 «By R110 W-ONLY, every step of H's IDEAL run equals
  on the levels ≥ 1 the c-step with c = b_0 of the new state»). So the use is INSIDE ISO's scope: CLEAN under L49 (and under the quoted
  W-ONLY text, which reads «on 𝓦_d» without ISO; both readings cover it). No flag. The fixes relay «Lead fix round 1 (21:47Z).» (fixes
  l. 3-4) is a message, stamped after the lane commit 4ee9fa78 (21:46:26Z) (D-1).
- G-C, OVERLAP WITH LANDED R105, R110-R114 (NOTE for the Lead and CHECKER; the brief's no-double-claim check; my reading). Nothing in
  L-2 is a clause of a landed entry restated as new, and nothing landed is claimed again; the body names each overlap once (Claims (a),
  (c), (d), Honest limits (ix)). (1) IM (a) is R105 LOCAL applied to the two chains (a premise). (2) IM (b) also follows from RESULTS
  R111's MERGE («(MERGE) at any degree, for two distinct options k, k′ of x and a state s, v_s(x, k) − v_s(x, k′) depends only on the
  options under s of the movers of the two chains before their first common mover») with Fact 0: a y on both chains of z lies at or
  after their first common mover, so the difference of z's values does not change; R111 is not a premise; the packet proves (b)
  directly. (3) VALUE-MONO is the c-step form (any c, under ISO) of R105's MONO and R114's MOVE-RISE (both on the IDEAL run); not the
  same statement. (4) KEY-DIR at level 1 with c constant gives R110's NOW-ONCE for c_t-step sequences («and in a c_t-step sequence on an
  interval over which c_t is constant, every level-1 mover moves at most once»; R110 lists it under «no signed DATA»); L-2 does not
  state NOW-ONCE. (5) BIT-CHAIN (i) is the c-step analogue (keys (κ^c_w, gate) at level 1) of R113's ALIGN order clause and R114's KEY
  (IDEAL keys); not the same key rule, not the same statement. (6) COMPOSE, COMPOSE-LB, FRAME and T_1(3) = 10 are new («T_1(3)»,
  «COMPOSE-LB», «T^Φ» 0 times in RESULTS); R110's FLIP-1 (T_k(1) = 3) agrees with NO-REPEAT's 2^(2m) − 1 = 3 at m = 1. R111's RETURN and
  RENEW are not in this packet. R112 (T^R(3) = 8) is not used (COMPOSE-LB names T^R(m′ + m + 1) by R110's definition only).
- G-3, STRICT SYMBOL TEST (notes). s, t, x, y, z, k, l, c, u, u′, m, m′ are bound in their clauses; «m» is free in 𝓛^R_(m+1) (each
  clause «on 𝓛^R_(m+1)» or «for ISO genomes … of 𝓛^R_(m+1)»); «g(A_l, k)» is R110's gate notation g(x, k) (R110: «b_0(s) = 1 iff g(0,
  s(0)) < g(1, s(1))»); «key(A_l)» is the c-step key of A_l's current option (packet l. 96 key_s(x)); «c_*» is bound in COMPOSE;
  «flip-free» means no change of c (R110's T_0); «T_∞(m)» undefined in the line (G-2 (iii)); «Φ_m», «Φ_3», «T^Φ_k(m)» are defined in the
  line («the IM frame Φ_m (…)», «T^Φ_k(m) the largest number of moving frame steps with at most k bit changes»); «kf1_d4_t10» is named
  by path and sha1; «FLIP-ADD», «SUM_1», «PAIR-LIN» are named «not claimed» without definitions (FLIP-ADD and PAIR-LIN occur in RESULTS
  R110 / R111 / R113 as not-claimed conjectures; SUM_1 occurs 0 times in RESULTS; nothing rests on them); «Fact 0» is named in a
  parenthesis without its text (the text precedes it: «the two values differ»).
- G-5, ERRATA (note). Erratum E-1 concerns R97-R100 counts. Erratum E-2 corrects R105's CHAIN-BACK binder, TOP-MONO's RANK_t and
  KEYFLIP's moves(x); L-2 uses R105's ENC and LOCAL only (E-2: «Unaffected: R105's other definitions»). Note E-3 concerns R110's
  CONDITIONAL DEAD; L-2 uses R110's definitions and W-ONLY only. Not bearing.
- G-6, NAMES (by script on RESULTS 555d41bd / GAPS 3c4ff44d; note; C116 G-2's remedy). 0 times in RESULTS and GAPS: «C128»,
  «P-IDEAL-IM», «IM-G1», «VALUE-MONO», «NO-REPEAT», «BIT-CHAIN», «KEY-DIR», «COMPOSE-LB», «T^Φ», «Φ_m», «imcheck», «frame_P-IDEAL-IM»,
  «kf1_d4_t10», «T_1(3)», «T_∞», «C_z(s)», «ch_k», «unhappy», «SUM_1». Same names, other meanings: «R115» once in RESULTS, L-RED's box
  R115 (Dead-ends section, l. 13254, «(L-RED R115's fcN)»); «COMPOSE» 49 lines in RESULTS (R86's Theorem COMPOSE, Corollaries
  COMPOSE-RUN, COMPOSE-NM, COMPOSE-FREEZE on N5 λ-runs; GAPS l. 11 in R86's UPDATE) and «FRAME» 22 lines (R89's Lemma FRAME-τ,
  P-N5-FRAME, FRAME-STRETCH): different objects; «(LOCAL)» is R105's (premise, same meaning); «IM» is this lemma (improvement
  monotonicity), not R86's or any landed label. One body sentence (Honest limits (viii)).
- G-7, L41 (the C109 E-1 class): not triggered (my reading). The proofs are L-SI successors 39-40's (packet l. 2-4); F-1 adds one proof
  sentence to COMPOSE-LB, written by L-SI successor 40 (fixes l. 3) from REFEREE's IM-G1 note (fixes l. 31 «REFEREE noted the
  achievability («level-0 gates and ranks are free, no W-role, ISO»); this sentence states it.»): REFEREE l. 54-55 sketched the choice
  («Choose the ranks so that the started options are the better ones, and the gates so that b_0 = c.»); the lane wrote and owns the
  sentence. Neither referee mentions L41. The referees' cstep_probe.py, r2cstep.py, ref_rup / r2rup and drup.c runs are checking tools.
- G-8, THE SCOPE TAIL (NOTE). «a STRUCTURE / RELAXATION statement inside the IDEAL model; bounds nothing polynomially (VALUE-MONO's
  bound is exponential); the frame is a relaxation, no converse is claimed; FLIP-ADD, SUM_1 and PAIR-LIN are not claimed; degree ≥ 3,
  Ξ-cyclic genomes and genomes outside 𝓛^R are not covered except by IM (degree-2 movers of any acyclic genome); T_k(3) for k ≥ 2 is not
  claimed»: true; «outside 𝓛^R» keeps IM's any-genome scope apart; T_1(3) = 10 is a finite machine statement and bounds nothing
  polynomially. No DEAD, no CONDITIONAL, no L43 item. Both referees MATCHED the tail.
- G-11, STALE LANE TEXT (notes; nothing here lands as current). (i) Packet §6 (M3) l. 239-240 «(branch head fb9682a1 when read)»: l-comp
  is now cf2e0e4f; lsi_q1_cert.txt byte-equal. (ii) Fixes l. 14, IM-L1 «the re-check addendum has not landed; nothing to cite yet»:
  still true for REFEREE's independent checker (G-R); REFEREE's §C (bc2bdd5a, after the fixes) adds its drup.c re-run. (iii) Fixes l. 7
  cites REFEREE-2's «draft 7856e7a9»; the report of record is 2e68c641 (G-13). (iv) Packet l. 6 and the line: FLIP-ADD, PAIR-LIN and
  SUM_1 «stay OPEN» / «are not claimed»: lane conjectures; the entry states no status for them beyond «not claimed». (v) Packet §6 l.
  248-249: the k ≥ 2 frame UNSATs are «single-solver, without a checked proof»; not in the entry.
- G-12, SHA1 PINS IN check.sh (the C110 F-1 / C116 G-3 class): partial. check75.sh pins (pins.sha1) the frozen encoder c3b3a232 and the
  witness 1c0dc8cc; it compares imcheck.py's output with the frozen imcheck.out, asserts compose.py's two lines verbatim (fixes F-2 l.
  36), the witness's T = [5, 10] by flipdp, and the CNF sha1 7e611c8b… from the encoder. It does not pin the packet, L-1, L-2, the
  fixes, imcheck.py, imcheck.out or compose.py; a change to the tools would change their output and fail the diff or the assertions.
  C116 G-3 ruled pin absence NOT required before landing. Note.
- G-13, THE REFEREES' ROUNDS (note; state on file at this fill). L-1 (493cac99): REFEREE (0e24d8ca) every item SIGN, COMPOSE-LB «SIGN
  WITH GAP IM-G1», §6 «SIGN as machine-certified», L-1 «MATCHES, with optional IM-L1, IM-L2» (l. 19-23); REFEREE-2 (report of record
  2e68c641; its body first pushed as the draft 7856e7a9 and the fix round 280d2313, both headed «DRAFT IN PROGRESS» with the §6 verdict
  and the drup row open; 2e68c641 fills l. 1-2, l. 20 and l. 81-82 only, by diff) every item SIGN, N-1 a text note, L-1 «**MATCHES after
  W-1 and W-2 (required, DATA)**» (l. 21). Fix round (fixes entry 1, 4ee9fa78): F-1 (IM-G1 = N-1), F-2 (W-2), F-3 (W-1, IM-L2), L-2.
  Second round: REFEREE §C (bc2bdd5a) «F-1 (IM-G1): CORRECT. IM-G1 is CLOSED.» (l. 143), «Verdict: L-2 MATCHES. Fixes entry 1 is
  CORRECT. All items are SIGNED; IM-G1 is closed.» (l. 160); REFEREE-2 «**Fixes entry 1: CORRECT.**» (l. 137), «**Line L-2: MATCHES.**»
  (l. 145), «W-1 and W-2 are met.» (l. 153). Open at a referee: REFEREE's independent re-check (G-R) and REFEREE-2's r2rup addendum (l.
  86 «A new r2rup run is going; its result will be an addendum.»); neither conditions a SIGN.
- G-14, THE FIXES FILE (note). Fixes entry 1 adds one proof sentence (F-1, inside COMPOSE-LB's proof: «The rest of the proof is
  unchanged.», l. 30), re-measures COMPOSE's DATA (F-2: the old figures «are withdrawn», l. 38) and re-reads the tool (F-3); L-2 = L-1
  «with exactly three replacements, made by script» (l. 52), given by subject (l. 53-55), not as old / new strings. No statement
  changes. The source note names it (G-1).
- G-T, THE TAG (note; the R112 / R114 precedent). The MACHINE item is signed by both referees as machine-certified; the ledger's labels
  are formalized and refereed-only (RESULTS l. 2), and R112 (a machine statement) carries «[refereed-only]». Kept; the machine character
  is in the line («and MACHINE: …», «its correctness and the encoder's are premises») and in the body (What rests on the machine; Honest
  limits (iii)).
- CLEAN AT L-2 (the pre-check against CHECKER's recurring items, by script on 8b7ccfb9):
  C106 E-1 (old line as current): L-2 is the current line; no L-3 exists (docs/si/P-IDEAL-IM-line-L3.txt absent at 4ee9fa78 and at
  91d40ec2); L-1 appears only in the line history.
  C113 E-1 (title «verbatim» after an insertion): no insertion; the title is byte-equal to prefix + L-2 + fill (Addendum (2)).
  C113 E-2 (trunk status that goes stale): the body has no trunk statement (header).
  C114 Add. 1 E-1 (UPDATE date): <DATE> placeholder.
  C115 E-1 (premise route): G-4.
  C110 F-1 / C116 G-3 (pins): G-12.
  C111 E-1 (stale Lead-reading statements): G-10.
  C116 G-2 (name clash): G-6, one body sentence.
  C117 E-1 / E-2 (scope; instance under-specified): G-2 (ii) and G-9 (v) flagged; the witness named by path and sha1, the CNF and the
  proof by sha1.
  C118 E-1 (stale status sentence): one open item (G-R), marked; R110-R114 named as landed; no status of FLIP-ADD, SUM_1, PAIR-LIN
  beyond «not claimed».
  C118 §3 / Erratum E-2 lesson (definitions diffed): G-2.
  C120 §5 / C121 E-1 / C122 E-2 / C124 E-1 / C125 E-1 / C127 E-1 (DATA unit, set and scope against the counter code): G-9; five clauses
  flagged ((i)-(v)).
  C122 G-0 (parentheses): 81 / 81, depth never negative (G-1).
  C122 E-3 (source note): CLEAN (G-1), with G-M.
  C123 E-1 (lane label or packet name before the claims): none (G-1).
  C123 E-2 (stale referee state): G-13, G-R.
  C123 §3 / C127 G-M (machine items stated exactly): G-M.
  «|»: 0 in L-2, 0 in the entry block, 0 in the UPDATE (by script, Addendum (3)).
- G-1, TITLE SHAPE AND SOURCE NOTE: CLEAN (my script). L-2 is one line, 4,488 characters, 4,615 bytes with the newline, 811 whitespace
  tokens, 81 «(» / 81 «)», depth never negative, final depth 0 (C122 G-0: met); 0 "|"; one guillemet pair («T^Φ_1(3) ≥ 11»); one « — »,
  with its own date parenthesis «(2026-11-06)», «2026» once. It begins «In the IDEAL model of RESULTS R104»: no packet name and no lane
  label before the claims (C123 E-1: met); lane names occur inside the claims only as provenance («L-NEW's ISO genome kf1_d4_t10», as
  R110's and R112's «L-RED's R197 convention»), and the packet name and «L-SI successors 39-40» only in the source note. Source note
  «(P-IDEAL-IM, docs/si/P-IDEAL-IM.md with its fixes entry 1, docs/si/P-IDEAL-IM-fixes.md; L-SI successors 39-40)»: the packet carries
  every proof (l. 4 «Every proof is written out in full HERE, and this packet governs.»); the fixes file carries one proof sentence
  (F-1) and is named. Every proof-carrying file is named (C122 E-3: met); the machine files are in the MACHINE clause (G-M). The title
  is "### R115 [refereed-only] " + L-2 + the fill ", CHECKER PASS (docs/checker/C128.md, checker PENDING)", nothing inserted.
(0) PLACEMENT. R115 goes DIRECTLY AFTER R114's block. docs/RESULTS.md at the local trunk (= origin trunk 96f4d708 for this file) has
  sha1 555d41bd85b8ea52a1e57459c0a4fe0fcb7f6cc1, 13,306 lines (wc -l), last changed by b6d1484b (R114's landing). «### R114» is l. 12394
  (entry l. 12394-12695, l. 12696 blank); «**Erratum E-1**» is l. 12697; «**Erratum E-2**» is l. 12710; «**Note E-3**» is l. 12738; «##
  Dead ends (kept;» is l. 12769. PROPOSED (R102's to R114's layout): insert R115's entry after l. 12696 (R114's blank line), with one
  blank line after it, so the R-entries stay contiguous and the errata and Note E-3 follow them. "### R115" occurs 0 times in RESULTS
  and GAPS. GAPS has sha1 3c4ff44d1b822110d9bfd0d1a2d8661ea6b5361e, 23 lines, last changed by b6d1484b.
(1) TITLE. The title is the line file docs/si/P-IDEAL-IM-line-L2.txt (l-si 4ee9fa7839441cce59e45a0884f63e4be0cc139a,
  2026-11-06T21:46:26Z, the file's only commit, sha1 8b7ccfb9a050955758452dc04fe5aafc58468680, 4,615 bytes with the newline; byte-equal
  at the l-si head 91d40ec2), verbatim: one line, no heading marker, no outer quotes, no final period. NOTHING is stripped and NOTHING
  is inserted: the heading is the level-3 marker, then "R115 [refereed-only] ", then the file without its newline, then the fill ",
  CHECKER PASS (docs/checker/C128.md, checker PENDING)" (as R90-R114). Built by script (fill115.py: assert the sha1 8b7ccfb9…, equality
  with the blob at 4ee9fa78 and at the l-si head, one line, no marker, one « (2026-11-06) — », no "|"; prepend, append) and re-checked
  after writing this file (chk115.py): equal, byte for byte. Heading: 4,567 characters, 4,693 bytes; sha1 of the heading line without
  its newline 5cbfb7904f5f98462791c4dff73955172469212d; it is l. 456 and the only «### R» line of this file.
(2) LINE HISTORY: two lines. L-1 493cac992f366a8efd5641f4c069813bf6e3f254 (cb2b0c60, frozen with the packet, the file's only commit;
  4,448 bytes, 781 tokens, 78 «(» / 78 «)»): REFEREE MATCHES with optional IM-L1, IM-L2; REFEREE-2 required W-1 and W-2 (G-13). L-2
  8b7ccfb9 (4ee9fa78; 4,615 bytes, 811 tokens, 81 / 81): fixes entry 1 l. 51-55 names three replacements by subject (the DATA scope,
  F-3; the COMPOSE figures, F-2; the source note), with no old / new strings; my token diff (wdiff115.py, difflib on whitespace tokens)
  finds 11 non-equal hunks (9 tokens out, 39 in): hunks 1-6 the F-3 scope words («every start, both c:» → «every start; once per
  state:», «(c) with the direction reversed», «per state and both c:», «(i)» after BIT-CHAIN), hunks 7-10 the F-2 command, seed and
  figures, hunk 11 the source note; nothing else changes. Both referees tested L-2 the same way (REFEREE §C l. 154-159 «Every changed
  region lies in the three named places:» … «Nothing else changes.»; REFEREE-2 l. 146-152). No hunk changes a claim. So the title is
  L-2, and L-1 is history.
(3) THE LINE AT BOTH REFEREES. REFEREE successor 24, docs/referee/R-P-IDEAL-IM.md: report 0e24d8ca (2026-11-06T18:21:43Z, new file, 135
  lines, sha1 56486e8287c25fcb89e434471da107ddb29c0583), §C bc2bdd5a (2026-11-06T22:32:47Z, 164 lines, sha1
  4d19e9fa0808ecc010033c27b82d786da92e409f; l. 1-135 = 0e24d8ca's, by diff): «Verdict: L-2 MATCHES. Fixes entry 1 is CORRECT. All items
  are SIGNED; IM-G1 is closed.» (l. 160). REFEREE-2 successor 28, docs/referee-2/R2-P-IDEAL-IM.md: final 2e68c641 (2026-11-06T23:56:00Z,
  153 lines, sha1 32e8bde68f9e8dbf848d31f3bff0534d94f5c62b; on claude/referee-2 by the merge f6bafb36, 2026-11-07T00:19:40Z): «**Line
  L-2: MATCHES.**» (l. 145). Both MATCH L-2.
(4) CLAIMS SIGNED = the items below, each SIGN in BOTH referees' verdict tables (REFEREE "## 0. Verdicts" l. 11-23; REFEREE-2 "##
  Verdicts" l. 11-21), unchanged in their second rounds (REFEREE §C l. 160; REFEREE-2 l. 137-153); the cells are the reports' words:
  Fact 0 (packet §0 l. 58-63): REFEREE l. 14 «SIGN»; REFEREE-2 l. 14 «**SIGN** (Opus 5.5, D12)». (a) Lemma IM (a)-(c) (§1 l. 65-90): l.
  15 both. (b) BIT-CHAIN (i), (ii) and KEY-DIR (§2 l. 92-129): l. 16 both. (c) VALUE-MONO and NO-REPEAT (§3 l. 131-145): l. 17 both. (d)
  COMPOSE (i), (ii) (§4 l. 147-171): REFEREE l. 18 «SIGN»; REFEREE-2 l. 18 (one row with COMPOSE-LB). (e) COMPOSE-LB (§4 l. 172-182 with
  fixes F-1): REFEREE l. 19 «SIGN WITH GAP IM-G1 (the proof does not say how b_0 = c is obtained; one sentence)», CLOSED by F-1 (§C l.
  143); REFEREE-2 l. 18 «**SIGN** (Opus 5.5, D12); text note N-1 (COMPOSE-LB's level-0 gates)», F-1 «This is the sentence COMPOSE-LB
  needed.» (l. 139). (f) Theorem FRAME (i), (ii) (§5 l. 184-218): l. 20 REFEREE, l. 19 REFEREE-2. (g) MACHINE T^Φ_1(3) ≤ 10, hence
  T_1(3) = 10 (§6 l. 220-249): REFEREE l. 21; REFEREE-2 l. 20 (G-M). No gap is open at either referee (IM-G1 closed; G-R and REFEREE-2's
  r2rup addendum are re-checks, not gaps).
Clause checks (L-2 against the packet; G-2): IM = l. 66-69; BIT-CHAIN = l. 97-103; KEY-DIR = l. 119-127; VALUE-MONO = l. 132-133,
141-143; COMPOSE = l. 148-161; COMPOSE-LB = l. 172-173; FRAME = l. 185-202; MACHINE = l. 221-247. Nothing in L-2 is wider than signed
(G-2 (ii) is in FRAME's proof, not in a clause).
Signed by both, NOT stated by L-2 as separate items: Fact 0 (only as the parenthesis «(the two values differ, Fact 0)»), the «Reading
(OR)» of §1 (l. 84-85), FRAME (ii)'s T_∞ form «T_∞(m) ≤ T^Φ_∞(m)», FRAME's «Consequence» (l. 215-216; in the body). Not signed, so NOT
landed: §7 (DATA; the summary table's §7 row, l. 17, labels it DATA, «scoped per statement»), the k ≥ 2 frame UNSATs (l. 248-249), the
T_k(m) values for m ≥ 2 other than T_1(3).
(5) OTHER TEXTS THE ENTRY DEPENDS ON: RESULTS R104's definition of the IDEAL model (title l. 9864; no R104 theorem); RESULTS R105's ENC
  and LOCAL (title l. 10155); RESULTS R110's definitions and W-ONLY (title l. 11323). Nothing else for a signed statement. The MACHINE
  item rests also on the machine (What rests on the machine). The sources docs/si/N5-MECH-box69.md, N5-FLIPOR-box64.md,
  N5-REFUTE-box68.md, N5-FRAME-box70.md and N5-SUM1-box73.md (packet l. 2-4) are history.
(6) PREMISE LABELS (stale-label test; RESULTS and GAPS at 96f4d708's version). RESULTS labels in L-2 (by script): «R104» 3, «R105» 2,
  «R110» 4, «R112» 1 («drup.c of RESULTS R112», the checker's provenance, not a premise). Each exists: R104 l. 9864, R105 l. 10155, R110
  l. 11323, R112 l. 11909. No Lead reading and no other RESULTS label is cited. G-N5-TIME open (GAPS l. 11).
(7) SYMBOL TEST: G-3.
(8) FIXES AND STATUS NOTES (docs/si/P-IDEAL-IM-fixes.md, L-SI successor 40, append-only, one entry, one commit 4ee9fa78): sha1
  15edc7d1bfecdb4f1edf55b0eb861e6333d437ef, 55 lines, 4,290 bytes. Header l. 1-4. Entry 1 (l. 6-55): table l. 8-14; F-1 (l. 16-31); F-2
  (l. 33-38); F-3 (l. 40-49); Line (l. 51-55). Verdicts: REFEREE §C l. 137-160; REFEREE-2 l. 134-153.
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-2 states no CONJECTURE as claimed and kills nothing («P-IDEAL-IM», «COMPOSE-LB», «T_1(3)»
  occur 0 times in GAPS). A line-11 UPDATE is proposed at the end, to go AFTER R114's UPDATE (GAPS at 96f4d708: the last UPDATE on l. 11
  is R114's «UPDATE 2026-11-06 21:57Z: RESULTS R114 (P-IDEAL-RISE; CHECKER C127 e3269b0b) [refereed-only] LANDED: …», ending «G-N5-TIME
  stays open.» before the row's closing « |»; l. 11 holds 76 "|" and 49 «UPDATE 2026-»), as a pure insertion with one separating space.
  BUILT FROM L-2 (scratch upd115.py = r114/fill2/upd114b.py l. 1-315 unchanged (controls R97-R113; its l. 316, the state assertion that
  R113's UPDATE is the last on l. 11, is dropped because R114's now follows it), plus R114's control, plus R115). CONTROLS (same script,
  same run, rc 0): R97's to R114's LANDED UPDATEs (GAPS l. 11 at 96f4d708) rebuilt from their lines byte for byte (True ×18; R114's from
  P-IDEAL-RISE L-3 at 0548afaa through upd114b.py's R114 call with head «UPDATE 2026-11-06 21:57Z: RESULTS R114 (P-IDEAL-RISE; CHECKER
  C127 e3269b0b) [refereed-only] », 4,289 bytes filled, also equal to R114-draft l. 787 and to r114/fill2/upd114L3.txt with <DATE>
  2026-11-06, <HH:MM> 21:57, <checker> e3269b0b). R115: the R111 procedure (sentinel_build111 of upd111.py, unchanged, default drops) on
  L-2 with the MACHINE clause cut and put back behind «(FRAME)» and the «, and (COMPOSE-LB)» adaptation (G-U): 7 labels, each found once
  after the start «and s ⊕ e_y the state s with y switched: », in order, moved behind their clauses; « (2026-11-06) — » → «: »; the DATA
  parenthesis before the source parenthesis opened as «; DATA, …»; «; G-N5-TIME stays OPEN» and «; not M3, not a step-4 pass, not a
  TARGET.md claim» dropped; the source parenthesis kept; «. G-N5-TIME stays open.» appended. L-2 holds no "|", so no replacement list.
  Checked by script: one line, 0 "|", one «<DATE>», one «<HH:MM>», one «<checker>», 4,646 bytes, 4,522 characters, 810 tokens, 80 «(» /
  80 «)», balanced; «2026-11-06» 0 times; token multiset diff against L-2 = the head, the seven moved labels, «(DATA,» opened, the two
  dropped scope sentences, « — » and the final sentence (upd115.out). Head «UPDATE <DATE> <HH:MM>Z: RESULTS R115 (P-IDEAL-IM; CHECKER
  C128 <checker>) [refereed-only] » («P-IDEAL-IM» 0 times in GAPS); <DATE> = the landing date.
(10) DATA of record = packet §7 (l. 251-271), NOT signed; L-2's DATA parenthesis states its counts per statement, with the flags of G-9.
  Re-run at this fill: Re-runs (a)-(d) in the header (PASS; my splits).
- PASS lines: «box 75 P-IDEAL-IM checks + witness + COMPOSE seed 68: PASS», «box 75 certified CNF regenerated: PASS», «si (box 75:
  P-IDEAL-IM): PASS».
- imcheck raw (byte-equal to imcheck.out; check75.sh's diff -q and my imsplit.py): «genomes 404 checks {'IM': 31208, 'BITCHAIN': 66520,
  'KEYDIR': 133040, 'MONO': 133040, 'FRAME_LOCAL': 250248, 'FRAME_OWN': 66520, 'FRAME_STEP': 24184, 'XSTEP': 18944}», all violations 0,
  «negative controls fired {'IM': 6284, 'BITCHAIN': 66520, 'KEYDIR': 67100, 'MONO': 33586, 'FRAME_STEP': 20486}», «PASS». compose.py
  seed 68: «COMPOSE random pairs 200 KPART 0 GPART 0» and, with NEG=1, «COMPOSE random pairs 200 KPART 21234 GPART 54433» (asserted
  verbatim by check75.sh l. 16-17).
- My splits (imsplit.out, compsplit.out): G-9 (ii)-(v).
NOT re-run: Glucose 4 and drup.c on the 2.4 GB proof (both referees regenerated the proof; three drup.c runs are on file); CaDiCaL; the
referees' cstep_probe.py and r2cstep.py (their reports read); check71.sh; L-COMP's bfk.c (its committed outputs read); check.sh's other
blocks and scripts/verify.sh.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 fixes l. 3-4 «Lead fix round 1 (21:47Z).» against the lane commit
  4ee9fa78 (21:46:26Z), and packet l. 2 «Lead brief BOX 75 (2026-11-06 14:13Z)» against the freeze cb2b0c60 (14:29:25Z); stamps of
  messages, not verifiable from the repository. D-2 REFEREE l. 26 «(1 hit each)»: ENC has 3 hits and R110's 𝓦_d wording 2 on RESULTS
  555d41bd (R113 and R114 quote ENC, R112 quotes R110; at the report's trunk the R114 quote was not yet in RESULTS); 1 hit each with the
  source entry's context (G-4). D-3 REFEREE-2's report was first pushed as a draft (7856e7a9, 280d2313, «DRAFT IN PROGRESS»); its
  independence sentence is the final file's l. 2-3; REFEREE's report 0e24d8ca (18:21:43Z) precedes REFEREE-2's body 7856e7a9
  (21:44:03Z); REFEREE-2's first tools commit 0925d262 is 15:23:20Z. D-4 packet l. 269-270 cites L-COMP's T_1(2) = 5 «as quoted in
  docs/si/N5-FRAME-box70.md §0», which names neither L-COMP nor bfk.c (G-9, the encoder bullet); L-COMP's bfk records (557b045b) carry
  the value. D-5 L-COMP's CNF came from frame.py at 7523970f (sha1 128d6a39…; lsi_q1_cert.txt l. 2), not the frozen copy (c3b3a232…);
  the frozen copy adds only the XCUBE and DUMPONLY options (git diff), and both give sha1 7e611c8b… (G-M). D-6 the CaDiCaL run
  (box70/log/3_t1_11.log, 1ad6902d, 2026-11-05T18:31:59Z) logs «vars 20843 clauses 96580 -> UNSAT 1281.5s» but no CNF sha1; its frame.py
  (1ad6902d, sha1 1f650d8c…) differs from the frozen copy only by added modes and options (the t1 path unchanged, git diff); identity
  with 7e611c8b… is not checked by sha1.
(12) Excluded: packet §7 (DATA counts, as statements); the Reading (OR) of §1; FRAME (ii)'s T_∞ form; the k ≥ 2 frame UNSATs of
  UNSAT-LIST.txt; boxes 76- (later lane work). Not part of this entry.
(13) Commits: lane (claude/l-si): cb2b0c60 (2026-11-06T14:29:25Z; freeze: packet 7bef9419 (279 lines), L-1 493cac99, imcheck.py,
  imcheck.out, frame_P-IDEAL-IM.py, check75.sh, pins.sha1, check.sh block box 75) → 4ee9fa78 (2026-11-06T21:46:26Z; fixes entry 1, 55
  lines; L-2; check75.sh +3 lines: the COMPOSE assertions); the commits after it (50cd3f73, 306e4862, a3aeaf5a, 91d40ec2) change no
  P-IDEAL-IM file. L-COMP (claude/l-comp): 39aec370 (2026-11-06T07:00:36Z; lsi_q1_cert.txt). REFEREE (claude/referee): 0e24d8ca (report)
  → bc2bdd5a (§C, +29 lines); e1815909 (successor 25: scratch/ref_rup_del.c, notes). REFEREE-2 (claude/referee-2): 0925d262 (tools),
  7856e7a9 (body, draft), 280d2313 (fix round, draft), 2e68c641 (final), merged f6bafb36. CHECKER: docs/checker/ ends at C127
  (1c4ba1c3). Trunk: see the header.
(14) Placement: see (0). DEAD-ENDS ROWS: NONE (not drafted). R115 kills nothing.

### R115 [refereed-only] In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of R104 used; RESULTS R105's ENC and LOCAL; RESULTS R110's definitions of 𝓦_d, 𝓛^R_d, T^R(d), ISO, b_0, the c-step and T_k(m), and R110's W-ONLY in COMPOSE-LB only), on acyclic Ξ-graphs, with C_z(s) the option of a degree-2 mover z of larger value under s (the two values differ, Fact 0), z unhappy at s iff s(z) ≠ C_z(s), ch_k(z, s) the movers on the chain of (z, k) under s and s ⊕ e_y the state s with y switched: (IM) for degree-2 movers z ≠ y with y unhappy at s, C_z(s ⊕ e_y) = C_z(s) if y lies on neither or on both chains of z under s, and C_z(s ⊕ e_y) ∈ {C_z(s), k} if y lies only on the chain of (z, k); on 𝓛^R_(m+1) with A_l, B_l the movers 2l, 2l + 1: (BIT-CHAIN) for c ∈ {0, 1} and a state s, the bits b_0 := c and b_l := b_(l−1), 1 − b_(l−1) or [g(A_l, k) < g(B_l, k)] according as (s(A_l), s(B_l)) is (0, 1), (1, 0) or (k, k) satisfy b_l = [key(A_l) < key(B_l)] under R110's c-step keys, and a level-l mover prefers by key its option 0 iff b_(l−1) = 1; (KEY-DIR) in the c-step from u to u′ a mover x of level l ≥ 1 moves iff u(x) = b_(l−1) and C_x(u) ≠ b_(l−1), with the bits of u′, so the c-step depends on the gates only through c and the bits [g(A_l, k) < g(B_l, k)], l < m; under ISO: (VALUE-MONO) the c-step never lowers the current value of an upper mover and strictly raises it for every mover that moves, so in every c_t-step sequence, with any number of changes of c, no state repeats among the moving steps and T_k(m) ≤ T_∞(m) ≤ 2^(2m) − 1; (COMPOSE) for ISO genomes K of 𝓛^R_(m′+1) and G of 𝓛^R_(m+1) and their composite H of 𝓛^R_(m′+m+1) (G's upper levels above K's, G's level 0 dropped, G's ranks and gates above K's), H's c-step is K's c-step on K's movers and G's c_*-step on G's movers with c_* the bit b_(m′) of K's part of the new state, and (COMPOSE-LB) the number of steps of every such G-sequence driven by a flip-free c-step sequence of K is at most T^R(m′ + m + 1); (FRAME) every ISO genome of 𝓛^R_(m+1) gives, through its upper Ξ-targets, the table C and the bits [g(A_l, k) < g(B_l, k)], a system of the IM frame Φ_m (acyclic Ξ-targets on 2m upper movers, an arbitrary table C with C_z independent of s(z), LOCAL and IM, free key bits, and the BIT-CHAIN step) whose frame step with bit c is the genome's c-step, so T_k(m) ≤ T^Φ_k(m) for every k, T^Φ_k(m) the largest number of moving frame steps with at most k bit changes; and MACHINE: T^Φ_1(3) ≤ 10, hence T_1(3) = 10, by a Glucose 4 UNSAT of the frame CNF «T^Φ_1(3) ≥ 11» (sha1 7e611c8b…, regenerated by the frozen encoder experiments/si/box75/frame_P-IDEAL-IM.py, sha1 c3b3a232…, clause groups mapped to Φ_3 in the packet) with a DRUP proof accepted by the forward RUP checker drup.c of RESULTS R112 (sha1 2d4b8eab…; 6,531,220 lemmas; its correctness and the encoder's are premises), a second UNSAT by CaDiCaL 1.5.3 without a proof, and L-NEW's ISO genome kf1_d4_t10 of 𝓛^R_4 (experiments/new/box160/out/kf1_d4_t10.json, sha1 1c0dc8cc…; T_1 = 10 under two simulators) (2026-11-06) — a STRUCTURE / RELAXATION statement inside the IDEAL model; bounds nothing polynomially (VALUE-MONO's bound is exponential); the frame is a relaxation, no converse is claimed; FLIP-ADD, SUM_1 and PAIR-LIN are not claimed; degree ≥ 3, Ξ-cyclic genomes and genomes outside 𝓛^R are not covered except by IM (degree-2 movers of any acyclic genome); T_k(3) for k ≥ 2 is not claimed; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (DATA, experiments/si/box75/imcheck.py on 404 ISO genomes of 𝓛^R_2, 𝓛^R_3 and 𝓛^R_4, every start; once per state: IM (b), (c) 0 violations on 31,208 checks, (c) with the direction reversed failing 6,284 times; LOCAL 0 on 250,248 (y on neither chain, unhappy or not), among them IM (a) on the 125,124 with y unhappy; independence of s(z) 0 on 66,520; per state and both c: BIT-CHAIN (i) at the c-step image of the state 0 on 66,520 (5,670 distinct (genome, c, image) triples), the negated bit failing 66,520 times; KEY-DIR 0 on 133,040; VALUE-MONO 0 on 133,040; frame step = c-step 0 on 24,184; own c-step = the box 64 simulator 0 on 18,944, on the 301 genomes the box 64 simulator accepts; COMPOSE: experiments/si/box68/compose.py 200 68 (seed 68), 0 disagreements on 200 random pairs with (m′, m) ∈ {1, 2}², and NEG=1 compose.py 200 68, the negated schedule failing 54,433 times on G's part (30,113 steps and 24,320 end-of-run checks) and 21,234 times on K's (end-of-run checks after a failure on G's part only; K's steps do not use the schedule); BIT-CHAIN (ii), COMPOSE-LB and the T_∞ bound: no separate DATA; the encoder: only the m = 2 cross-checks T^Φ_1(2) = 5 against L-COMP's exhaustive T_1(2) = 5) (P-IDEAL-IM, docs/si/P-IDEAL-IM.md with its fixes entry 1, docs/si/P-IDEAL-IM-fixes.md; L-SI successors 39-40), CHECKER PASS (docs/checker/C128.md, checker PENDING)
- Object (L-SI successors 39-40, Opus 5.5, box 75; frozen, unchanged during review): packet P-IDEAL-IM, docs/si/P-IDEAL-IM.md, sha1
  7bef94196bdc6069f254e19aab9ecef1f0f16b95, 279 lines (l-si freeze cb2b0c60, 2026-11-06T14:29:25Z; identical at 4ee9fa78). Both referees
  measured the sha1 (REFEREE l. 5 «docs/si/P-IDEAL-IM.md: sha1 7bef94196bdc6069f254e19aab9ecef1f0f16b95, 279 lines;»; REFEREE-2 l. 6
  «docs/si/P-IDEAL-IM.md sha1 7bef94196bdc6069f254e19aab9ecef1f0f16b95, 279 lines;»). Items (summary table l. 8-17): §1 Lemma IM, §2
  BIT-CHAIN and KEY-DIR, §3 VALUE-MONO and NO-REPEAT, §4 COMPOSE and COMPOSE-LB, §5 Theorem FRAME (PROVED); §6 MACHINE («§5 + one solver
  UNSAT + a drup.c-checked proof»); §7 DATA. Sections: premises (l. 19-29), §0 the model and notation with Fact 0 (l. 31-63), §1 (l.
  65-90), §2 (l. 92-129), §3 (l. 131-145), §4 (l. 147-182), §5 (l. 184-218), §6 (l. 220-249), §7 (l. 251-271), §8 files (l. 273-279).
  Sources (l. 2-4): docs/si/N5-MECH-box69.md, N5-FLIPOR-box64.md, N5-REFUTE-box68.md, N5-FRAME-box70.md, N5-SUM1-box73.md; «Every proof
  is written out in full HERE, and this packet governs.» (l. 4).
  Fixes: docs/si/P-IDEAL-IM-fixes.md, append-only, two entries. Entry 1 (L-SI successor 40, 4ee9fa78, 2026-11-06T21:46:26Z; 55 lines,
  sha1 15edc7d1bfecdb4f1edf55b0eb861e6333d437ef): F-1 (REFEREE's IM-G1, REFEREE-2's N-1) one sentence in COMPOSE-LB's proof; F-2
  (REFEREE-2's W-2) the COMPOSE DATA re-measured with a named seed and command; F-3 (REFEREE-2's W-1, REFEREE's IM-L2) the DATA scopes
  checked against imcheck.py's counters; line L-2. Entry 2 (L-SI successor 41, 80d1422a, 2026-11-07T02:07:37Z; l. 57-79; the file then
  79 lines, 6,919 bytes, sha1 e80dee09d73db36dd5b604814c171a04b5b42fc4, its l. 1-55 = entry 1's file, by script): CHECKER C128 E-1..E-5
  answered by C128 §5's five replacements R1-R5 and line L-3, with the wording note C128 §4 recommended for Theorem FRAME's proof; «No
  statement, proof or hypothesis changes. This entry carries no proof.» (l. 63-64). «The packet file is not edited.» (l. 2).
  The RESULTS line is L-3, cf510950a7feaf3e8d5f3c316acc2601e2ed17e7 (docs/si/P-IDEAL-IM-line-L3.txt, l-si 80d1422a,
  2026-11-07T02:07:37Z, the file's only commit; 4,962 bytes). The title is L-3 verbatim, with nothing inserted (its date parenthesis
  «(2026-11-06)» and its source note are the line's own; the source note names the packet, which carries every proof, and the fixes
  file, which carries one proof sentence, F-1; the machine premise's files are named in the line's MACHINE clause). L-3's parentheses
  balance (86 «(» / 86 «)»). Line history: L-1 (493cac99, cb2b0c60, frozen with the packet); L-2 (8b7ccfb9, 4ee9fa78, fixes entry 1: L-1
  «with exactly three replacements, made by script» (l. 52), named by subject only: the DATA scope (F-3: once per state for IM, LOCAL
  and the independence of s(z), per state and both c for the rest, «BIT-CHAIN (i)»), the COMPOSE command, seed 68 and figures (F-2), and
  the source note naming the fixes file; my token diff finds 11 hunks, all inside these three places); L-3 (cf510950, 80d1422a, fixes
  entry 2: L-2 «with exactly R1-R5, made by experiments/si/box75/mkL3.py» (l. 78), the five replacements of CHECKER C128 §5 (E-1..E-5;
  C128 l. 105-114 = entry 2's table, l. 67-71, string for string, by my script), all inside the DATA parenthesis: R1 names the 250,248
  as LOCAL (y on neither chain, unhappy or not), among them IM (a) on the 125,124 with y unhappy; R2 puts BIT-CHAIN (i) at the c-step
  image of the state, 5,670 distinct (genome, c, image) triples; R3 puts the box 64 cross-check on the 301 genomes its simulator
  accepts; R4 splits the NEG control into 54,433 failures on G's part (30,113 steps and 24,320 end-of-run checks) and 21,234 on K's
  (end-of-run checks after a failure on G's part only); R5 adds BIT-CHAIN (ii) to the no-DATA list; L-2 with R1-R5 equals L-3 byte for
  byte, by my script, 8 token hunks). L-2 MATCHES at both referees, each after its own word diff: REFEREE (bc2bdd5a) §C l. 154-160,
  «Verdict: L-2 MATCHES. Fixes entry 1 is CORRECT. All items are SIGNED; IM-G1 is closed.»; REFEREE-2 (2e68c641) l. 145 «**Line L-2:
  MATCHES.**», l. 146-152. L-3 MATCHES at both referees, each after its own byte test against C128 §5 and its own instrumented copies of
  the counters: REFEREE successor 25 (0c2a7c5b) §C add. 1 l. 173-178 (byte test), l. 179-188 (the DATA rule, clause by clause), l.
  191-192 «Verdict: fixes entry 2 is CORRECT. L-3 MATCHES, by the byte test and in meaning, with the DATA rule clause by clause.»;
  REFEREE-2 successor 29 (0a9e2a16) Addendum 2 l. 159-160 (byte test), l. 161-169 (meaning against imcheck.py / compose.py), l. 172
  «Verdict: fixes entry 2 **CORRECT**; **L-3 MATCHES** (Opus 5.5, D1).».
  Both diffed every definition of the line against the packet (REFEREE l. 121-122 «Definitions diffed against §0 / §5: C_z, unhappy,
  ch_k, s ⊕ e_y, A_l / B_l, the BIT-CHAIN bits, T^Φ_k(m) and the frame's objects all MATCH.»; REFEREE-2 l. 121); L-2 changes no
  definition and no claim (the three replacements lie inside the DATA parenthesis and the source note); L-3 changes none either (R1-R5
  lie inside the DATA parenthesis; C128 §2 «No statement, definition, premise or proof changes.»).
- Claims signed (REFEREE successor 24 «(Opus 5.5, D15)», report 0e24d8ca, §C bc2bdd5a; REFEREE successor 25 (Opus 5.5, D15), §C add. 1
  0c2a7c5b; REFEREE-2 successor 28 «(Opus 5.5, D12/D20)», report of record 2e68c641; REFEREE-2 successor 29, Addendum 2 0a9e2a16). Every
  item is SIGN in both verdict tables (REFEREE "## 0. Verdicts" l. 11-23 of R-P-IDEAL-IM.md; REFEREE-2 "## Verdicts" l. 11-21 of
  R2-P-IDEAL-IM.md), COMPOSE-LB at REFEREE «SIGN WITH GAP IM-G1» until fixes F-1 (§C l. 143 «F-1 (IM-G1): CORRECT. IM-G1 is CLOSED.»),
  and MACHINE «SIGN as machine-certified» at both; they stand in both second rounds (REFEREE §C l. 160; REFEREE-2 l. 137, 145, 153) and
  in both third rounds, on CHECKER C128's fix round (REFEREE §C add. 1 l. 191-192 «All items stay SIGNED.»; REFEREE-2 Addendum 2 l. 172
  «Statement verdicts unchanged.»). Every item is about R104's IDEAL model on acyclic Ξ-graphs; (a) for movers of degree 2 of any such
  genome; (b) on 𝓛^R_(m+1) (RESULTS R110's 2-wide degree-2 ladders, levels 0, …, m, A_l := mover 2l, B_l := mover 2l + 1) with R110's
  c-step; (c), (d), (e), (f) on ISO genomes of 𝓛^R (R110's ISO: «ISO the property that no option has Ξ-target 0 or 1»); (g) on the ISO
  genomes of 𝓛^R_4 (m = 3). Notation (packet §0 l. 49-57): the UPPER movers are those of level ≥ 1; T_∞(m) is T_k(m) with no bound on
  the changes; v_s(x, k) the integer value of (x, k) under s (R105 ENC), cv_s(x) := v_s(x, s(x)), cv_s(X) := 0; ch_k(z, s) the set of
  movers on the chain of (z, k) under s, (z, k) itself excluded; C_z(s) the option of a degree-2 mover z with the larger value under s;
  z HAPPY at s iff s(z) = C_z(s), UNHAPPY otherwise; s ⊕ e_y the state s with y's option switched. Fact 0 (l. 58-63): «On an acyclic
  genome, for a mover z of degree 2 and any state s: v_s(z, 0) ≠ v_s(z, 1).» (the β of (z, 0) lies on its own chain and not on the chain
  of (z, 1); ENC is injective on sets with distinct ranks); hence A_s(z) = {s(z)} if z is happy and {0, 1} otherwise. Cells: REFEREE l.
  14 «SIGN»; REFEREE-2 l. 14 «**SIGN** (Opus 5.5, D12)».
  (a) Lemma IM (§1 l. 65-90) [IDEAL-ACYC; z ≠ y movers of degree 2; y unhappy at s; s′ := s ⊕ e_y]: «(a) If y ∉ ch_0(z, s) ∪ ch_1(z, s),
    then C_z(s′) = C_z(s).»; «(b) If y ∈ ch_0(z, s) ∩ ch_1(z, s), then C_z(s′) = C_z(s).»; «(c) If y lies in ch_k(z, s) and not in
    ch_(1−k)(z, s), then C_z(s′) ∈ {C_z(s), k}.». Proof: (a) by R105 LOCAL; y's switch raises cv(y) by δ > 0 (Fact 0; the new chain of y
    avoids y) and every chain through y by exactly δ (ENC along its prefix), so (b) both of z's values rise by δ and (c) only one does.
    (a) is R105 LOCAL on z's two chains, and (b) also follows from RESULTS R111's MERGE with Fact 0 (a y on both chains lies at or after
    their first common mover); R111 is not a premise; the packet proves (b) directly. Not claimed (l. 86-90): degree ≥ 3, simultaneous
    switches of several movers, any bound on the number of steps. Cells: REFEREE l. 15 «SIGN»; REFEREE-2 l. 15 «**SIGN** (Opus 5.5,
    D12)».
  (b) Lemma BIT-CHAIN and Corollary KEY-DIR (§2 l. 92-129) [G ∈ 𝓛^R_(m+1), m ≥ 1, c ∈ {0, 1}; keys as in R110's c-step: a level-1 option
    W-pointing to mover w keyed (κ^c_w, its own gate), a level-l ≥ 2 option keyed by the key of its W-target's option under the state,
    then its own gate]: for a state s, b_0 := c and for l = 1..m, b_l := b_(l−1) if (s(A_l), s(B_l)) = (0, 1), 1 − b_(l−1) if (1, 0),
    and «b_l := c_l(k) := [g(A_l, k) < g(B_l, k)] if s(A_l) = s(B_l) = k»; «(i) for l = 1..m, b_l = [key_s(A_l) < key_s(B_l)];» «(ii)
    for l = 1..m, a mover x of level l prefers by key its option 0 (key of (x, 0) < key of (x, 1) under s) iff b_(l−1) = 1.». KEY-DIR:
    «For a state u, let u′ be its c-step and b_l the bits of u′ (BIT-CHAIN with s = u′). A mover x of level l ≥ 1 moves (u′(x) ≠ u(x))
    iff u(x) = b_(l−1) and C_x(u) ≠ b_(l−1).», with the consequence that the c-step above level 0 depends on the gates only through c
    and the 2(m − 1) bits c_l(k), l = 1..m − 1 (l. 126-127). Proof: induction on l; at level 1 the keys compare at κ^c, at l ≥ 2 at the
    distinct prefixes; KEY-DIR by Fact 0 and (ii). BIT-CHAIN (i) is the c-step analogue of the key-order clauses of RESULTS R113's ALIGN
    and R114's KEY, which are about the IDEAL keys; KEY-DIR at level 1 with c constant gives RESULTS R110's NOW-ONCE for c_t-step
    sequences, which the line does not restate. Cells: REFEREE l. 16 «SIGN»; REFEREE-2 l. 16 «**SIGN** (Opus 5.5, D12)».
  (c) Lemma VALUE-MONO and Corollary NO-REPEAT (§3 l. 131-145) [G ∈ 𝓛^R_(m+1) with ISO, u a state, c ∈ {0, 1}, u′ the c-step of u]: «For
    every upper mover x: cv_(u′)(x) ≥ cv_u(x), with strict inequality if u′(x) ≠ u(x).»; NO-REPEAT: «In every c_t-step sequence of an
    ISO genome of 𝓛^R_(m+1) (any number of changes of c), the vector (cv(x))_x of the upper movers never decreases, and it strictly
    increases at every t with u_t ≠ u_(t−1). Hence no state repeats among the states with u_t ≠ u_(t−1), and T_k(m) ≤ T_∞(m) ≤ 2^(2m) −
    1.». Proof: induction along a topological order of the Ξ-graph (ISO keeps every upper chain among upper movers and X), ENC, and
    u′(x) ∈ A_u(x). It is the c-step form, for any c, of RESULTS R105's MONO and R114's MOVE-RISE (both on the IDEAL run); the bound is
    exponential. Cells: REFEREE l. 17 «SIGN»; REFEREE-2 l. 17 «**SIGN** (Opus 5.5, D12)».
  (d) Lemma COMPOSE (§4 l. 147-171) [K ∈ 𝓛^R_(m′+1), G ∈ 𝓛^R_(m+1), both ISO, m′, m ≥ 1; the composite H ∈ 𝓛^R_(m′+m+1): levels 0..m′
    are K, G's level-l mover becomes H's level-(m′ + l) mover keeping its Ξ-targets, β's and gates, G's level 0 dropped, G's ranks and
    gates raised above K's, R197 wiring; «H is in 𝓛^R_(m′+m+1) (two degree-2 movers per level, R197 W-wiring, distinct ranks and gates),
    and its Ξ-graph is acyclic (the disjoint union of K's and G's, upper parts) and ISO.»]: «(i) On K's upper movers, u′ is K's c-step
    of u restricted to K.»; «(ii) On G's movers, u′ is G's c_*-step of u restricted to G, where c_* := b_(m′) of u′ computed in K
    (BIT-CHAIN in K).». Proof: chains and rank orders stay inside each part (LOCAL), H's keys at levels ≤ m′ are K's, and H's bits above
    m′ run G's recursion from b_(m′) (BIT-CHAIN, KEY-DIR). Cells: REFEREE l. 18 «SIGN»; REFEREE-2 l. 18 (with (e)).
  (e) Corollary COMPOSE-LB (§4 l. 172-182 with fixes F-1 l. 16-31): «For every flip-free c-step sequence of K and the bit sequence
    c_*(t) := b_(m′) of K's part of u_t that it produces, the number of steps of G's c_*(t)-step sequence (from any start) is at most
    T^R(m′ + m + 1).». Proof: H's level-0 movers get both options with Ξ-target X and a start on their better option, so they never
    move; F-1: «Choose also the β ranks and gate indices of the four level-0 options as follows.» (the four smallest ranks and gates,
    ordered so that b_0(q) = c; «By ISO the level-0 options lie on no Ξ-chain of an upper option, so the A-sets of the upper movers are
    unchanged.»; R110's c-step does not read the level-0 gates); then «By R110 W-ONLY, every step of H's IDEAL run equals on the levels
    ≥ 1 the c-step with c = b_0 of the new state, which is constant since level 0 never moves.» (l. 177-178), and H's run counts every
    step of G's c_*-sequence, so its length is at most T^R(m′ + m + 1) by R110's definition. W-ONLY is used on the ISO genome H only
    (G-10). Cells: REFEREE l. 19 «SIGN WITH GAP IM-G1 (the proof does not say how b_0 = c is obtained; one sentence)», closed by F-1 (§C
    l. 143); REFEREE-2 l. 18 «**SIGN** (Opus 5.5, D12); text note N-1 (COMPOSE-LB's level-0 gates)», F-1 «This is the sentence
    COMPOSE-LB needed.» (l. 139).
  (f) Theorem FRAME (§5 l. 184-218) [the IM frame Φ_m (m ≥ 1): a frame system has the 2m upper movers A_l, B_l with two options each, a
    Ξ-target per option (an upper mover ≠ z or X) with an acyclic Ξ-graph, a table C: (z, s) ↦ C_z(s) ∈ {0, 1} on {0, 1}^(2m) and bits
    c_l(k) for l = 1..m − 1, with «(Φ1) C_z(s) does not depend on s(z);», «(Φ2) LOCAL: if y ∉ ch_0(z, s) ∪ ch_1(z, s) then C_z(s ⊕ e_y)
    = C_z(s);» and «(Φ3) IM: for y ≠ z unhappy at s (s(y) ≠ C_y(s)), clauses (b) and (c) of Lemma IM hold with this C.»; the frame step
    from s with bit c switches every level-l mover x with C_x(s) ≠ s(x) and C_x(s) = 1 − b_(l−1), level by level, with b_l from the NEW
    level-l states by the BIT-CHAIN recursion; T^Φ_k(m) the largest T with s_t ≠ s_(t−1) for t = 1..T and at most k changes of the
    bits]: «(i) For every ISO genome G of 𝓛^R_(m+1), the system Σ(G) satisfies (Φ1)-(Φ3), and its frame step with bit c equals G's
    c-step (on the levels ≥ 1) at every state.»; «(ii) Hence T_k(m) ≤ T^Φ_k(m) for every k ≥ 0, and T_∞(m) ≤ T^Φ_∞(m).». Proof: (Φ1) by
    acyclicity and LOCAL, (Φ2) is R105 LOCAL (the proof of Lemma IM (a), l. 72, does not use that y is unhappy; the packet's l. 207 says
    «(Φ2) is Lemma IM (a)», which fixes entry 2's wording note, l. 72-73, reads so, as CHECKER C128 §4 recommended), (Φ3) by IM (b),
    (c), the step by KEY-DIR; (ii) by deleting the identity steps, which does not increase the number of bit changes.
    Consequence (l. 215-216): «Every frame query «T^Φ_k(m) ≥ L» that is UNSAT gives T_k(m) ≤ L − 1.»; a SAT model is a frame system, not
    a genome. Not claimed: «that T^Φ_k(m) = T_k(m) in general (the frame is a relaxation; no converse is proved)» (l. 217). Cells:
    REFEREE l. 20 «SIGN»; REFEREE-2 l. 19 «**SIGN** (Opus 5.5, D12)».
  (g) MACHINE: T^Φ_1(3) ≤ 10, hence T_1(3) = 10 (§6 l. 220-249; a machine statement): «T^Φ_1(3) ≤ 10. With Theorem FRAME (ii): T_1(3) ≤
    10. With the witness below: T_1(3) = 10.» (l. 221); the upper bound by the UNSAT of the frame CNF «T^Φ_1(3) ≥ 11» certified by a
    DRUP proof accepted by drup.c, the lower bound by the ISO genome kf1_d4_t10 of 𝓛^R_4. «drup.c's correctness is a premise (as in
    R112). No drat-trim, no Lean.» (l. 243). Cells: REFEREE l. 21 «SIGN as machine-certified; encoder (M1) audited FAITHFUL (§2 below);
    the Glucose proof regenerated byte-identically (my independent re-checks of it: addendum)»; REFEREE-2 l. 20 «**SIGN as
    machine-certified** (Opus 5.5, D12): encoder audited faithful; CNF and DRUP proof regenerated byte-identically; my drup.c build
    VERIFIED it; witness replayed; trust base = R112's (drup.c, an audited encoder)».
  The RESULTS line (L-3) states (a)-(g) with their exact hypotheses and nothing wider.
- What rests on the machine (packet §6 l. 222-243; both referees' §6 checks): (i) PROVED (lane, signed): Theorem FRAME, so every UNSAT
  frame query «T^Φ_k(m) ≥ L» gives T_k(m) ≤ L − 1; and nothing else of (g). (ii) THE ENCODER, a premise, audited, not machine-checked:
  experiments/si/box75/frame_P-IDEAL-IM.py (sha1 c3b3a232e8ba56b6c6ed64511e2a24d1842e1f62, 191 lines; byte-equal to
  experiments/si/box70/frame.py at 4ee9fa78), run as «DUMP=<dir> DUMPONLY=1 python3 frame_P-IDEAL-IM.py 3 t1 11», writes a CNF
  satisfiable iff some frame system of Φ_3 has a frame run of 11 moving steps with at most one bit change; its clause groups are mapped
  to §5 in the packet's table (l. 226-235) and audited clause group by clause group by both referees (REFEREE §2 l. 64-85, «So the CNF
  is satisfiable iff T^Φ_1(3) ≥ 11.»; REFEREE-2 l. 58-74, «So the CNF is satisfiable iff some frame system of Φ_3 has a frame run of 11
  moving steps with ≤ 1 bit change.»). (iii) THE CNF: sha1 7e611c8bdf53a70a398e9e1ec3b220a1b79e2507, 20,843 variables, 96,580 clauses;
  regenerated by the frozen encoder by the lane (check75.sh l. 20-22; experiments/si/UNSAT-LIST.txt «m 3 t1 11 (box 70)»), by REFEREE
  (l. 86-87, «EQUAL to L-COMP's certified input (lsi_q1_cert.txt).»), by REFEREE-2 (l. 75-76), by REFEREE successor 25 (notes/REFEREE.md
  l. 10-11) and by this draft's re-run of the check.sh block; L-COMP generated it from the encoder at claude/l-si 7523970f (sha1
  128d6a39…; = the frozen copy without its XCUBE and DUMPONLY options) and certified that input (claude/l-comp
  experiments/comp/box27/log/lsi_q1_cert.txt l. 2-3). (iv) THE SOLVER, not trusted (it only writes the proof; a wrong proof is
  rejected): Glucose 4 through python-sat (pysat glucose4; pysat 1.9.dev15 at REFEREE-2): UNSAT in 2,157.5 s at L-COMP (lsi_q1_cert.txt
  l. 3), 2,174.6 s at REFEREE (l. 93), 2,398.8 s at REFEREE-2 (l. 77). (v) THE PROOF: DRUP, sha1
  32be84e4f8320fa5060545805f90d1c244378984, 2,388,304,251 bytes, with 6,435,900 deletion lines; not committed; regenerated
  byte-identically by REFEREE (l. 94-95, «BYTE-IDENTICAL to L-COMP's proof, so L-COMP's drup.c verdict applies to exactly this file.»)
  and by REFEREE-2 (l. 77-78). (vi) THE CHECKER, trusted: experiments/comp/box27/drup.c (sha1 2d4b8eab8fe9e9035c396733bb400d9d6e7d2366,
  L-COMP; the checker of record of RESULTS R112; forward RUP, deletions applied), audited sound by REFEREE (R-P-TR3 §1) and REFEREE-2
  (R2-P-TR3: audit and fuzzing), its correctness a premise. Three runs on this proof: L-COMP successor 9 (lsi_q1_cert.txt l. 4-6,
  39aec370: «lemmas checked 6531220, deletion lines 6435900 (applied; clauses removed 6435900)», «s VERIFIED (6531220 lemmas
  RUP-checked)»); REFEREE successor 24 on its own regenerated proof (§C l. 161-163, «s VERIFIED (6531220 lemmas RUP-checked)», 7,577 s;
  its log was not committed, notes/REFEREE.md l. 43-44); REFEREE-2 successor 28 with its own gcc -O2 build of 2d4b8eab on its own
  regenerated proof (l. 81-82, «s VERIFIED (6531220 lemmas RUP-checked)», «all 6,435,900 deletions matched, 132 m 39 s.»). (vii) RESULT:
  UNSAT of the CNF 7e611c8b…, certified by drup.c; with (ii) and (i): T^Φ_1(3) ≤ 10 and T_1(3) ≤ 10. (viii) A SECOND, INDEPENDENT
  ACCEPTANCE: drup.c stays the checker of record ((vi); the line names drup.c only), and a second checker program has also accepted this
  proof: REFEREE successor 25's «R-P-IDEAL-IM Addendum 1» (claude/referee 47d6cfdf, 2026-11-07T03:38:06Z; R-P-IDEAL-IM.md l. 194-224).
  It regenerated the CNF with the frozen encoder at cb2b0c60 (sha1 7e611c8b…, «p cnf 20843 96580», «EQUAL to §2 and to L-COMP's
  certified input.», l. 199-201) and the proof with Glucose 4 («UNSAT, 2,492.8 s», sha1 32be84e4…, «It is BYTE-IDENTICAL to L-COMP's
  proof and to successor 24's: a third independent regeneration.», l. 202-204), and checked it with its own checker
  docs/referee/scratch/ref_rup_del.c (successor 24's ref_rup.c with deletions applied; RUP only, no RAT; controls l. 211-215, run before
  the check): «s VERIFIED (6531220 lemmas RUP-checked, 6435900 deletions applied, 0 unmatched)», exit 0, wall 11,862 s (l. 216-217); the
  lemma count is drup.c's (l. 219-221). Its verdict (l. 222-224): «Independent of drup.c, it confirms MACHINE T^Φ_1(3) ≤ 10, given the
  encoder audited FAITHFUL in §2.» and «This addendum may be cited (C128 §4) as a second, independent proof check.». Both checkers take
  the encoder (ii) as given; ref_rup_del, like drup.c, is unverified C. The addendum records successor 24's drup.c run only as «Reported
  by successor 24 at park, log not preserved» (l. 195) and does not count it as its own check (l. 196-197). REFEREE successor 24's own
  ref_rup (deletions ignored) was lost to a container restart (§C l. 164 «My independent ref_rup (deletions ignored) was still running
  when this was written; it is handed to successor 25 (notes/REFEREE.md).»); REFEREE-2's r2rup.c «NOT FINISHED» (l. 83; l. 86 «A new
  r2rup run is going; its result will be an addendum.»), and REFEREE-2's Addendum 2 (0a9e2a16) reports no result of it. No referee file
  on origin (fetched 2026-11-07T04:10:10Z by date -u) reports a second checker REJECTING the proof. (R112's sixteen cube proofs were
  likewise also accepted by REFEREE's own ref_rup.) A second checker was not required (CHECKER C128 §4, ruling G-M / G-R, «RULING: not
  required.»); C128 §4 allows this citation, «If REFEREE 25's Addendum 1 (or REFEREE-2's r2rup) ACCEPTS before landing, the body may
  cite it (optional, by the Lead).», and keeps the landing condition «if any referee file on origin at landing reports that a second
  checker REJECTS the proof, R115 does not land.». (ix) CORROBORATION, not a certificate: CaDiCaL 1.5.3 through python-sat answered
  UNSAT (packet l. 236, «No proof.»;
  experiments/si/box70/log/3_t1_11.log «m 3 MODE t1 T 11 T2 0 NOIM 0 vars 20843 clauses 96580 -> UNSAT 1281.5s»; the CNF's sha1 was not
  logged, and its encoder was the box-70 frame.py of 1ad6902d, whose t1 path equals the frozen copy's, by git diff). (x) NOT MACHINE:
  the lower bound is one explicit genome, experiments/si/box64/wit/kf1_d4_t10.json (sha1 1c0dc8cc5a8dd382e028d199f96f783f995b9a5a, =
  claude/l-new experiments/new/box160/out/kf1_d4_t10.json), ISO, in 𝓛^R_4, with T_1 = 10 (bits 0000011111, one change) under the lane's
  box 64 flipdp.py (check75.sh l. 11-14: T = [5, 10]) and L-NEW's box 150 Gen through box71/replayk.py (packet l. 246-247), REFEREE's
  own c-step (l. 98-103: «T_1 = 10 from the stored start, by c = 0 for 5 changing steps and then c = 1.») and REFEREE-2's r2cstep.py (l.
  87-90: «T_0 = 5 and T_1 = 10 (start 011101, bits 0000011111)»). No formal verification, no Lean; REFEREE l. 104-105 «So T_1(3) = 10
  rests on: the hand-proved FRAME theorem (signed), the audited encoder, certified UNSAT, and a witness re-run by a third simulator. As
  in R112, it is machine-certified, not Lean.».
- Premise: RESULTS R104's definition of the IDEAL model and of the Ξ-graph (no R104 theorem), restated in packet §0 (l. 32-40); RESULTS
  R105's ENC and LOCAL, each quoted verbatim by the packet (l. 22-25: «(ENC) «the Ξ-order of β-sets is the order of the integers Σ
  ±2^rank (+ for even parity), so, with ε(x, k) := ±2^rank(x, k) (+ for even parity), the value of option (x, k) is ε(x, k) plus the
  current value of its Ξ-target (ε(x, k) alone if the Ξ-target is the exit X)»»; «(LOCAL) «an option's value depends only on the states
  on its chain, a key only on the states below its level»»), found in R105's title (l. 10155), ENC also quoted from there in R113's and
  R114's bodies; RESULTS R110's definitions of 𝓦_d, 𝓛^R_d, T^R(d), ISO, b_0(s), the c-step and T_k(m), quoted verbatim by the packet (§0
  l. 41-48), found in R110's title (l. 11323; its 𝓦_d / 𝓛^R_d / T^R(d) part also quoted in R112's body); and R110's W-ONLY, «on 𝓦_d
  every step of a run equals, on the levels ≥ 1, the c-step with c = b_0 of the new state» (packet l. 26-27), 1 hit (R110's title, l.
  11323), used in COMPOSE-LB's proof only. Whitespace normalised. L-3: «premise: R104's definition of the model only, no theorem of R104
  used; RESULTS R105's ENC and LOCAL; RESULTS R110's definitions of 𝓦_d, 𝓛^R_d, T^R(d), ISO, b_0, the c-step and T_k(m), and R110's
  W-ONLY in COMPOSE-LB only». Use: ENC in Fact 0, IM, VALUE-MONO; LOCAL in IM (a), FRAME's (Φ1) and (Φ2) and COMPOSE's A-sets; R110's
  definitions throughout §2-§6; W-ONLY on the ISO composite H in COMPOSE-LB (within the scope of Lead reading L49, «RESULTS R110
  (IDEAL-FLIP) signs W-ONLY, T ≤ T_2(d−1) + 2, for ISO genomes of 𝓛^R_d only.»). Not used: «any other item of R104-R112, any other
  RESULTS entry, docs/lit, any other lane file, any outside source» (packet l. 28); RESULTS R111's MERGE, R113 and R114 are not premises
  (Claims (a)-(c) name the overlaps). The machine premises are §6's encoder and drup.c (What rests on the machine). Both referees
  byte-tested the quotes against RESULTS (REFEREE l. 26-30; REFEREE-2 l. 24-26 «W-ONLY is used in COMPOSE-LB only.»). Erratum E-2 does
  not bear (it governs R105's CHAIN-BACK, TOP-MONO and KEYFLIP).
- L41 and L43. The proofs are L-SI successors 39-40's (packet l. 2-4); fixes F-1, one proof sentence, was written by L-SI successor 40
  after REFEREE's IM-G1 (REFEREE l. 54-55 sketched the choice; the lane wrote the sentence); the referees' simulators and checkers are
  checking tools. Nothing referee-written is a proof step of the entry (my reading; neither referee mentions L41). Fixes entry 2 (L-SI
  successor 41) carries no proof (l. 63-64). No DEAD item; L43 does not bear.
- Fixes (docs/si/P-IDEAL-IM-fixes.md, append-only; entry 1 by L-SI successor 40 at 4ee9fa78, 55 lines, sha1
  15edc7d1bfecdb4f1edf55b0eb861e6333d437ef, after REFEREE 0e24d8ca and REFEREE-2's draft 7856e7a9; entry 2 by L-SI successor 41 at
  80d1422a, l. 57-79, the file then 79 lines, sha1 e80dee09d73db36dd5b604814c171a04b5b42fc4, after CHECKER C128 2dd44fc1):
  - F-1 (l. 16-31, IM-G1 required by REFEREE; REFEREE-2's N-1): one sentence inserted in COMPOSE-LB's proof: the four level-0 options
    get the four smallest ranks and gates, ordered so that «g(0, q(0)) < g(1, q(1)) holds iff c = 1, i.e. b_0(q) = c (R110's definition
    of b_0).»; ISO keeps them off every upper chain; R110's c-step does not read their gates; movers 0 and 1 never move, so «R110 W-ONLY
    makes every step of H's IDEAL run the c-step with this c.»; «The rest of the proof is unchanged.» (l. 30). REFEREE §C l. 143-147
    «Complete and correct.»; REFEREE-2 l. 138-139.
  - F-2 (l. 33-38, W-2 required by REFEREE-2): «Command (from experiments/si/box68): `python3 compose.py 200 68` → «COMPOSE random pairs
    200 KPART 0 GPART 0».» and its NEG=1 control «COMPOSE random pairs 200 KPART 21234 GPART 54433»; both asserted verbatim by
    check75.sh; the packet's figures 6,786 / 16,853 «came from an unrecorded seed and smaller run, and are withdrawn.» (l. 38). REFEREE
    §C l. 148 (EQUAL); REFEREE-2 l. 140-142.
  - F-3 (l. 40-49, W-1 required by REFEREE-2; IM-L2 optional by REFEREE, taken): the DATA scopes against imcheck.py: per state and both
    c XSTEP, MONO, BITCHAIN (BIT-CHAIN (i); «part (ii) is not counted separately; it enters KEY-DIR's prediction»), KEYDIR; once per
    state FRAME_OWN, FRAME_LOCAL, IM, and FRAME_STEP for both c2; «Line L-2 states exactly these scopes.» (l. 49). REFEREE §C l.
    150-153; REFEREE-2 l. 143-144. F-3's «per state and both c» for BITCHAIN names the loop, not the state checked: the check is made at
    the c-step image of each state (C128 E-2), as L-3 now says (R2); its FRAME_LOCAL «(IM (a))» counts y on neither chain, unhappy or
    not (C128 E-1, R1).
  - Line L-2 (l. 51-55): L-1 «with exactly three replacements, made by script» (l. 52): the DATA scope (F-3), the COMPOSE figures (F-2),
    the source note.
  - Entry 2 (l. 57-75; CHECKER C128 E-1..E-5, all DATA wording): the five old / new pairs R1-R5 as a table (l. 65-71), equal to C128 §5
    (l. 105-114) string for string (my script; REFEREE §C add. 1 l. 174-175 «They equal the five pairs of entry 2's table, string for
    string.»); the wording note for Theorem FRAME's proof (l. 72-73): read «(Φ2) is Lemma IM (a)» as «(Φ2) is R105 LOCAL (the proof of
    Lemma IM (a), l. 72, does not use that y is unhappy)», the sentence C128 §4 (G-2 (ii)) recommended, not required; the scopes of
    R1-R3 are the CHECKER's measured counts (l. 74-75). Entry 2's source paragraph (l. 58-62) says that C128 itself was not opened at
    its writing (2dd44fc1 was then not on the remote) and that the pairs came from the Lead's relay «of C128 §4»; the pairs are C128
    §5's, and REFEREE confirmed them against C128 itself (l. 175 «the pairs are now confirmed against C128 itself»). REFEREE §C add. 1
    l. 189-191 (the wording note «is right»; «Verdict: fixes entry 2 is CORRECT.»); REFEREE-2 Addendum 2 l. 172 «Verdict: fixes entry 2
    **CORRECT**».
  - Line L-3 (l. 77-79): «docs/si/P-IDEAL-IM-line-L3.txt = L-2 with exactly R1-R5, made by experiments/si/box75/mkL3.py (each old string
    asserted to occur once);» sha1 cf510950…, 4,962 bytes, re-made and compared by check75.sh (80d1422a; pins_fix2.sha1 pins L-2, L-3,
    the fixes file and mkL3.py).
  - Not taken: REFEREE's optional IM-L1 (l. 14: «the re-check addendum has not landed; nothing to cite yet»).
  No fix changes a statement or a hypothesis; F-1 completes COMPOSE-LB's proof, F-2 and F-3 change DATA wording, L-2 changes the line's
  DATA parenthesis and source note only, entry 2 changes no statement, proof or hypothesis (one wording note on FRAME's proof), and L-3
  changes the DATA parenthesis only (R1-R5).
- Not signed: packet §7 (DATA; the summary table's §7 row, l. 17, labels it DATA, «scoped per statement»), in particular its table (l.
  254-263; its row «(Φ2) = Lemma IM (a)» with the count 250,248, l. 257, is the source of C128 E-1; L-3's DATA names the 250,248 as
  LOCAL, among them IM (a) on the 125,124 with y unhappy, R1), the COMPOSE figures and the encoder cross-checks at m = 2 (l. 264-270);
  the frame UNSATs for k = 2, 3, ∞ at m = 3 (l.
  248-249, «single-solver, without a checked proof»); the Reading (OR) of §1 (l. 84-85). Not claimed: the lane conjectures FLIP-ADD,
  SUM_1 and PAIR-LIN (the line: «not claimed»; this entry states no status for them). OPEN, not claimed: any polynomial bound on T_k(m)
  or T^R(d); a converse of FRAME (T^Φ_k(m) = T_k(m)); T_k(3) for k ≥ 2; T_1(m) for m ≥ 4; any statement for degree ≥ 3 or Ξ-cyclic
  genomes beyond IM's scope; G-N5-TIME.
- Referee strengthening (NOT part of this entry; referee checks):
  (i) REFEREE: its own c-step from R110's text (scratch/cstep_probe.py) on the witness (l. 98-103); check75.sh re-run at cb2b0c60 and
    4ee9fa78 (l. 108, §C l. 148-149); the imcheck.py counters read against the line (l. 109-113, «All EQUAL.»).
  (ii) REFEREE-2 (r2cstep.py `checks(75, 400)`, output r2checks_seed75.out; l. 97-102): 400 random ISO genomes of 𝓛^R_(m+1), m = 1-3,
    every upper state, both c, 0 violations: IM (a) on 105,010 cases, IM (b) on 4,164, IM (c) on 19,842; BIT-CHAIN (i) on 56,048;
    KEY-DIR and VALUE-MONO on 112,096 each; frame step = its c-step on 20,912; compose.py on 18 seeds, KPART 0 and GPART 0 each time (l.
    111).
  (iii) In CHECKER C128's fix round both referees ran instrumented copies of imcheck.py and compose.py (REFEREE successor 25:
    imcheck_ref25.py and compose_ref25.py on `git archive 4ee9fa78`, §C add. 1 l. 179-187; REFEREE-2 successor 29: fix2/imcheck_r2.py
    and fix2/compose_r2.py, read at 80d1422a, Addendum 2 l. 161-169): 125,124 of the 250,248 with y unhappy; 5,670 distinct (genome, c,
    image) triples (4,715 (genome, image) pairs); XSTEP on 301 of the 404 genomes; under NEG=1 K in-run 0, G in-run 30,113, K end-of-run
    21,234, G end-of-run 24,320; no counter for BIT-CHAIN (ii). C128 §3 measured the same and also checked BIT-CHAIN (i) at the states
    themselves and (ii) at the c-step images, 0 failures each (its DATA, not lane DATA).
- Honest limits: (i) A STRUCTURE / RELAXATION statement inside the IDEAL model: one improving switch of a degree-2 mover never lowers
  another degree-2 mover's preferred option except toward the chain it raises (IM); on 2-wide ladders under R110's c-step the key order
  is a bit chain (BIT-CHAIN) and a mover moves iff it is unhappy and on the bit's option (KEY-DIR); under ISO no c-step lowers a current
  value (VALUE-MONO), so no state repeats and T_k(m) ≤ 2^(2m) − 1; stacked ladders run as one (COMPOSE, COMPOSE-LB); every ISO ladder is
  a system of the IM frame, so frame UNSATs bound T_k(m) (FRAME); and T_1(3) = 10 by machine. It bounds nothing polynomially; G-N5-TIME
  stays open; not M3, not a step-4 pass, not a TARGET.md claim. (ii) IM is for degree-2 movers of any acyclic genome; BIT-CHAIN and
  KEY-DIR on 𝓛^R_(m+1); VALUE-MONO, COMPOSE, COMPOSE-LB and FRAME on ISO genomes of 𝓛^R only; Ξ-cyclic genomes and degree ≥ 3 are not
  covered. (iii) The MACHINE item is a machine statement: its upper bound rests on Theorem FRAME (proved), on the audited, not proved,
  encoder (sha1 c3b3a232…), and on the UNSAT of the CNF sha1 7e611c8b… certified by one DRUP proof (sha1 32be84e4…) accepted by drup.c
  (sha1 2d4b8eab…; unverified C, audited sound by both referees), run three times by three parties, and also accepted by a second,
  independent RUP checker, REFEREE's ref_rup_del (unverified C; Addendum 1, What rests on the machine (viii)), which C128 did not
  require (ruling G-M / G-R); no drat-trim, LRAT, formally verified checker or Lean. (iv) The DATA is per statement, as L-3's DATA
  parenthesis says (after CHECKER C128 E-1..E-5),
  with these exact sets and units (imcheck.py and compose.py, read by me): 404 ISO 𝓛^R genomes (400 random with m = 1, 2, 3 and 4 pins),
  every upper state with level 0 at (0, 0) (every start up to the level-0 states, C128 N-1); IM per (state, z, y) with y unhappy on a
  chain; LOCAL per (state, z, y) with y off both chains, happy or not (125,124 of the 250,248 with y unhappy, IM (a)'s hypothesis);
  independence per (state, mover); BIT-CHAIN (i) per (state, c, level), evaluated at the c-step image of the state (5,670 distinct
  (genome, c, image) triples); KEY-DIR and VALUE-MONO per (state, c, upper mover); the frame step per (state, c); the box 64 cross-check
  on the 301 genomes its simulator accepts; COMPOSE on 200 pairs, 41,056 runs, its NEG control failing 54,433 times on G's part (30,113
  steps and 24,320 end-of-run checks) and 21,234 times on K's, all end-of-run checks after a failure on G's part (K's steps do not use
  the schedule); BIT-CHAIN (ii), COMPOSE-LB and the T_∞ bound have no lane count; the DATA of IM, BIT-CHAIN and KEY-DIR is on ISO 𝓛^R
  genomes only, while IM is stated for degree-2 movers of any acyclic genome and BIT-CHAIN and KEY-DIR on all of 𝓛^R_(m+1) (C128 N-3).
  (v) Every statement is about
  R104's IDEAL model; nothing is said about a real N5 run or a parity game beyond what R104 already says. (vi) Premises: RESULTS R104's
  definition, R105's ENC and LOCAL, R110's definitions and W-ONLY (in COMPOSE-LB only); R106-R109 and R111-R114 are not used. No lit
  note, no lane file, no outside source; the machine premises (the encoder, drup.c) for (g) only. No Lean. (vii) Every proof is in
  docs/si/P-IDEAL-IM.md, with one sentence of COMPOSE-LB's proof in docs/si/P-IDEAL-IM-fixes.md (F-1); the line's source note names
  both; the machine premise's files are named in the line's MACHINE clause. (viii) Names: «R115» here is this RESULTS entry, not L-RED's
  box R115 (RESULTS Dead-ends section, «L-RED R115's fcN»); «COMPOSE» and «COMPOSE-LB» are this packet's lemma and corollary, not
  RESULTS R86's Theorem COMPOSE or its corollaries; «FRAME» is this theorem, not R89's Lemma FRAME-τ; «IM» is this lemma; «LOCAL» is
  R105's item (a premise) and the frame's (Φ2) named after it; «IM-G1», «IM-L1», «IM-L2» (REFEREE) and «W-1», «W-2», «N-1» (REFEREE-2)
  are this packet's referee labels; «Fact 0» is packet §0's. (ix) Overlaps with landed entries: IM (a) is R105 LOCAL on two chains; IM
  (b) also follows from R111's MERGE; VALUE-MONO is the c-step form of R105's MONO and R114's MOVE-RISE; KEY-DIR implies R110's NOW-ONCE
  for c_t-step sequences; BIT-CHAIN (i) is the c-step analogue of R113's ALIGN and R114's KEY; none of these landed items is claimed
  again, and none is a premise.
- Data (DATA, not proof): experiments/si/box75/imcheck.py (l-si cb2b0c60, unchanged at 4ee9fa78 and 80d1422a, sha1
  f69e38ac59fb944c282f9b8660ac87b4f8171e91, 111 lines; deterministic, `imcheck.py 400 75`; own c-step from R110's text, cross-checked
  against box 64's flipdp.py on the 301 genomes it accepts), output frozen in experiments/si/box75/imcheck.out (sha1
  2b0e08a67e9c8b5bf48948cfb50752d815e477f5, 4 lines); experiments/si/box68/compose.py (sha1 895d4026440bb5def5b84b159a31532908b5ef8c, 75
  lines, b4404b06); wired into experiments/si/box75/check75.sh (80d1422a, 28 lines; at 4ee9fa78 23 lines: pins of the encoder and the
  witness, imcheck.py against imcheck.out, the witness's T_1 by flipdp, compose.py's two lines verbatim, the CNF sha1 from the encoder;
  fixes entry 2 added pins_fix2.sha1 (L-2, L-3, the fixes file, mkL3.py) and L-3 re-made by mkL3.py and compared with L-3 and its sha1
  cf510950…), called by experiments/si/check.sh l. 1237-1239 (the same three lines at 80d1422a). L-3's DATA parenthesis: «(DATA,
  experiments/si/box75/imcheck.py on 404 ISO genomes of 𝓛^R_2, 𝓛^R_3 and 𝓛^R_4, every start; once per state: IM (b), (c) 0 violations on
  31,208 checks, (c) with the direction reversed failing 6,284 times; LOCAL 0 on 250,248 (y on neither chain, unhappy or not), among
  them IM (a) on the 125,124 with y unhappy; independence of s(z) 0 on 66,520; per state and both c: BIT-CHAIN (i) at the c-step image
  of the state 0 on 66,520 (5,670 distinct (genome, c, image) triples), the negated bit failing 66,520 times; KEY-DIR 0 on 133,040;
  VALUE-MONO 0 on 133,040; frame step = c-step 0 on 24,184; own c-step = the box 64 simulator 0 on 18,944, on the 301 genomes the box 64
  simulator accepts; COMPOSE: experiments/si/box68/compose.py 200 68 (seed 68), 0 disagreements on 200 random pairs with (m′, m) ∈ {1,
  2}², and NEG=1 compose.py 200 68, the negated schedule failing 54,433 times on G's part (30,113 steps and 24,320 end-of-run checks)
  and 21,234 times on K's (end-of-run checks after a failure on G's part only; K's steps do not use the schedule); BIT-CHAIN (ii),
  COMPOSE-LB and the T_∞ bound: no separate DATA; the encoder: only the m = 2 cross-checks T^Φ_1(2) = 5 against L-COMP's exhaustive
  T_1(2) = 5)». What each count covers (imcheck.py and compose.py, read by me): IM per (state, z, y) with y unhappy and on a chain of z
  (31,208; the control on (c) only); LOCAL per (state, z, y) with y on neither chain, any y (250,248, of them 125,124 with y unhappy);
  independence per (state, z) (66,520); BIT-CHAIN (i) per (state, c, level) at the c-step image (66,520 checks at 5,670 distinct
  (genome, c, image) triples; its control fires at every passing check, by construction, true as written, C128 N-2); KEY-DIR and
  VALUE-MONO per (state, c, upper mover) (133,040 each); the frame step per (state, c) (24,184); the box 64 cross-check per (state, c)
  on 301 of the 404 genomes (18,944); COMPOSE per (pair, start, b_0) run (41,056 runs; NEG: KPART 21,234 end-of-run counts after a
  G-part break, GPART 30,113 in-run + 24,320 end-of-run); the encoder's m = 2 values by check70.sh (box70/frame.py = the frozen encoder)
  and L-COMP's bfk.c records. BIT-CHAIN (ii), KEY-DIR's gate consequence and FRAME's «so T_k(m) ≤ T^Φ_k(m)» have no counter of their
  own. The block's outputs, reproduced by both referees (REFEREE l. 108 and §C l. 148-149; REFEREE-2 l. 109-111, 140) and re-run for
  this draft (first fill 2026-11-07T00:55:25Z from a `git archive` of 4ee9fa78's experiments/si, rc 0, the three PASS lines; second fill
  2026-11-07T03:02:24Z-03:02:32Z from a `git archive` of 80d1422a's experiments/si and docs/si, rc 0, the same three PASS lines,
  check75.sh now also re-making L-3 by mkL3.py; imcheck.py's output equal to imcheck.out; compose.py's two lines as asserted). No signed
  statement uses any count; the MACHINE item uses the certificate, not DATA (What rests on the machine).
- Signatures: REFEREE docs/referee/R-P-IDEAL-IM.md: successor 24's report 0e24d8ca07cb9142cb18ce4ba588bc3c0911a533
  (2026-11-06T18:21:43Z, new file, 135 lines, sha1 56486e8287c25fcb89e434471da107ddb29c0583): every item SIGN, COMPOSE-LB with gap
  IM-G1, §6 «SIGN as machine-certified» with the encoder audited FAITHFUL, the CNF regenerated and the Glucose proof regenerated
  byte-identically, L-1 MATCHES with optional IM-L1, IM-L2 (l. 11-23, 64-105, 119-135); §C bc2bdd5a56f3f9a792ee203845f31ea577418aa6
  (2026-11-06T22:32:47Z, 164 lines, sha1 4d19e9fa0808ecc010033c27b82d786da92e409f; l. 1-135 = 0e24d8ca's, by diff): «F-1 (IM-G1):
  CORRECT. IM-G1 is CLOSED.» (l. 143), F-2 re-measured EQUAL (l. 148), F-3 «CORRECT against imcheck.py.» (l. 150), its word diff of L-2
  (l. 154-159), «Verdict: L-2 MATCHES. Fixes entry 1 is CORRECT. All items are SIGNED; IM-G1 is closed.» (l. 160), and the certificate
  addendum: drup.c on its regenerated proof «s VERIFIED (6531220 lemmas RUP-checked)» (l. 161-163); successor 25's §C add. 1
  0c2a7c5bd207a9d0a79efc23f8720e69c04f38b1 (commit 2026-11-07T02:30:13Z; its header time, first written «2026-11-07T03:0xZ by date -u»,
  was corrected to «committed 2026-11-07T02:30Z (0c2a7c5b)» by 3fb22563, 2026-11-07T02:49:14Z, «REFEREE 25: correct guessed header times
  in four reports to their commit times», which changes only that line of this file; the file at 3fb22563: 192 lines, sha1
  60778fdab1c08d1a341e85979e65ea927ba6d12b; l. 1-164 = bc2bdd5a's, by diff): C128 opened and R1-R5 parsed from its §5, equal to entry
  2's table (l. 172-175), the byte test (l. 176-178), the DATA rule clause by clause with its own instrumented counters (l. 179-188),
  the wording note «is right» (l. 189-190), «Verdict: fixes entry 2 is CORRECT. L-3 MATCHES, by the byte test and in meaning, with the
  DATA rule clause by clause. All items stay SIGNED.» (l. 191-192). Successor 25's «R-P-IDEAL-IM Addendum 1»
  47d6cfdfd70af78218ad369442e2e9d75aab06e6 (commit 2026-11-07T03:38:06Z, header «date -u at writing 2026-11-07T03:38Z»; the file at
  47d6cfdf: 224 lines, sha1 8754b6f9c06e7df86859d0cefb0169d66095064d; l. 1-192 = 3fb22563's, by diff): the CNF and a byte-identical
  proof regenerated, its own ref_rup_del «s VERIFIED (6531220 lemmas RUP-checked, 6435900 deletions applied, 0 unmatched)», exit 0 (l.
  198-221); «Verdict: the Glucose 4 DRUP proof of the UNSAT of the §6 CNF is VERIFIED by my own RUP checker.» (l. 222); cited as a
  second, independent proof check, which C128's ruling G-M / G-R did not require (What rests on the machine (viii)). REFEREE-2
  docs/referee-2/R2-P-IDEAL-IM.md: successor 28's report of record 2e68c641ccac5342c7b4a38ef448f3f3c286c2d1
  (2026-11-06T23:56:00Z, 153 lines, sha1 32e8bde68f9e8dbf848d31f3bff0534d94f5c62b; on claude/referee-2 by the merge f6bafb36; earlier
  pushes of the same file: the draft body 7856e7a9 (21:44:03Z) and the fix round 280d2313 (22:18:02Z), both headed «DRAFT IN PROGRESS»;
  2e68c641 changes l. 1-2, l. 20 and l. 81-82 only, by diff), with R2-P-IDEAL-IM/r2cstep.py, r2checks_seed75.out and
  r2cstep_kf1_d4_t10.out: every item SIGN, N-1 a text note, §6 «**SIGN as machine-certified**», L-1 MATCHES after W-1 and W-2 (l. 11-21,
  57-95, 104-132); fix round 1: «**Fixes entry 1: CORRECT.**» (l. 137), «**Line L-2: MATCHES.**» after its word diff (l. 145-152), «W-1
  and W-2 are met.» (l. 153); r2rup.c NOT FINISHED (l. 83-86); successor 29's Addendum 2 0a9e2a16247d47306cb751979d3d4f155ea372f0
  (commit 2026-11-07T02:31:16Z, header stamp «2026-11-07 02:5xZ by date -u»; 172 lines, sha1 78545a522b0bce76bc74ba0f9f6f3485ce298343;
  l. 1-153 = 2e68c641's, by diff): R1-R5 taken from C128 §5 (l. 158), the byte test (l. 159-160), the meaning against imcheck.py /
  compose.py with its own instrumented copies (l. 161-169), its predecessor's miss recorded (l. 170-171), «Verdict: fixes entry 2
  **CORRECT**; **L-3 MATCHES** (Opus 5.5, D1). Statement verdicts unchanged.» (l. 172); it reports no r2rup result. Lane: freeze and L-1
  cb2b0c60f4202c008cebbb4be2bf1567de38a069, fixes entry 1 and L-2 4ee9fa7839441cce59e45a0884f63e4be0cc139a, fixes entry 2 and L-3
  80d1422a2b403c01e8aaaa79cdcd5341874166ef. Certificate record: L-COMP successor 9, claude/l-comp
  39aec370ca6e38c555ebfc5263b71061e1fdee9e (experiments/comp/box27/log/lsi_q1_cert.txt, sha1 caae5fe1e83017a08d7377c2ccccceb92032defc, 7
  lines). INDEPENDENCE: REFEREE l. 2-3 «Independent: I did not open or list docs/referee-2/ on this packet before this report was
  pushed.»; REFEREE-2 l. 2-3 «Independent: docs/referee/ not read for this packet before this push.». REFEREE's report (18:21:43Z)
  precedes REFEREE-2's first report body (7856e7a9, 21:44:03Z); neither cites the other's report; each audited the encoder clause group
  by clause group, regenerated the CNF and the proof on its own, ran drup.c on its own regenerated proof, and replayed the witness with
  its own c-step. In the second round REFEREE knew REFEREE-2's items only through the fixes entry (§C l. 142 «I know REFEREE-2's items
  (W-1, W-2) only through the entry.»). Differences, resolved: REFEREE's IM-G1 (a gap) and REFEREE-2's N-1 (a text note) name the same
  missing sentence, F-1; REFEREE-2 alone required W-1 and W-2 (DATA), REFEREE offered IM-L2 (the same scope point as W-1) and IM-L1 (not
  taken). Both SIGN the same items, and both MATCH L-2 (each by its own word diff) and L-3 (each by its own byte test against C128 §5
  and its own instrumented counters). The two third rounds were committed 63 s apart (02:30:13Z, 02:31:16Z), each parsing C128 §5
  itself; REFEREE-2 records as its predecessor's miss that its second round accepted the K's-part count without the unit / break
  analysis (l. 170-171). No disagreement in substance.
- TARGET.md diff: TARGET.md §1-§3 define parity games («A parity game is G = (V, V_E, V_O, E, pr) with V finite»), the regions W_E, W_O,
  M4 (§2 «There is a deterministic algorithm A and a polynomial p such that for every parity game G, A on input G halts within») and the
  word-RAM cost model; no statement of this entry mentions a parity game, a winning region, an algorithm's running time or a cost model
  (packet l. 6 «Not a TARGET.md claim. No polynomial bound. G-N5-TIME, FLIP-ADD, PAIR-LIN and SUM_1 stay OPEN.»; REFEREE §4 l. 116-117
  «Not M3, not M4, not a gauntlet step. G-N5-TIME OPEN.»; REFEREE-2 l. 117-118 «Not M3 / M4 / step 4; G-N5-TIME, FLIP-ADD, PAIR-LIN,
  SUM_1 OPEN.»). The solver and checker times are machine data, not a running-time claim. The line (L-3) makes no M4 claim and no TARGET
  claim; its tail reads «a STRUCTURE / RELAXATION statement inside the IDEAL model» and «G-N5-TIME stays OPEN; not M3, not a step-4
  pass, not a TARGET.md claim» (L-3, by script). Not a step-4 pass. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER R114's UPDATE of G-N5-TIME (GAPS at 96f4d708 and at this second fill's local
trunk, byte-equal: the last UPDATE on l. 11 is R114's, «UPDATE 2026-11-06 21:57Z: RESULTS R114 (P-IDEAL-RISE; CHECKER C127 e3269b0b) …»,
before the row's closing « |»), built by script (fill2/upd115b.py: upd115.py with its 18 controls (R97-R114, all landed, byte for byte,
True; printed exactly as at the first fill) and its R115 procedure unchanged, run on L-3; sentinel_build111 of upd111.py unchanged,
default drops, the «(DATA, » opening; the clause step applied to the MACHINE clause and one adaptation for «, and (COMPOSE-LB)» (G-U);
cross-checked against a direct build: True; equal to the first fill's UPDATE with C128 §5's R1-R5: True) only from the clauses of the
title line L-3: the seven labels behind their clauses, the MACHINE clause after «(FRAME)»; « (2026-11-06) — » → «: »; the DATA
parenthesis before the source parenthesis opened as «; DATA, …»; «G-N5-TIME stays OPEN» and «not M3, not a step-4 pass, not a TARGET.md
claim» dropped; the source parenthesis kept; «. G-N5-TIME stays open.» at the end. L-3 holds no "|"; the UPDATE holds none (4,993 bytes,
85 «(» / 85 «)»; sha1 of the line without newline, placeholders unfilled: 39d9a2925c2c193193f3b0845b37919defa75a2b, = C128 §5's). <DATE>
is the landing date (YYYY-MM-DD, by date -u at the landing commit; C114 Add. 1 E-1), <HH:MM> the landing time and <checker> the CHECKER
C128 commit, all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R115 (P-IDEAL-IM; CHECKER C128 <checker>) [refereed-only] LANDED: In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of R104 used; RESULTS R105's ENC and LOCAL; RESULTS R110's definitions of 𝓦_d, 𝓛^R_d, T^R(d), ISO, b_0, the c-step and T_k(m), and R110's W-ONLY in COMPOSE-LB only), on acyclic Ξ-graphs, with C_z(s) the option of a degree-2 mover z of larger value under s (the two values differ, Fact 0), z unhappy at s iff s(z) ≠ C_z(s), ch_k(z, s) the movers on the chain of (z, k) under s and s ⊕ e_y the state s with y switched: for degree-2 movers z ≠ y with y unhappy at s, C_z(s ⊕ e_y) = C_z(s) if y lies on neither or on both chains of z under s, and C_z(s ⊕ e_y) ∈ {C_z(s), k} if y lies only on the chain of (z, k) (IM); on 𝓛^R_(m+1) with A_l, B_l the movers 2l, 2l + 1: for c ∈ {0, 1} and a state s, the bits b_0 := c and b_l := b_(l−1), 1 − b_(l−1) or [g(A_l, k) < g(B_l, k)] according as (s(A_l), s(B_l)) is (0, 1), (1, 0) or (k, k) satisfy b_l = [key(A_l) < key(B_l)] under R110's c-step keys, and a level-l mover prefers by key its option 0 iff b_(l−1) = 1 (BIT-CHAIN); in the c-step from u to u′ a mover x of level l ≥ 1 moves iff u(x) = b_(l−1) and C_x(u) ≠ b_(l−1), with the bits of u′, so the c-step depends on the gates only through c and the bits [g(A_l, k) < g(B_l, k)], l < m (KEY-DIR); under ISO: the c-step never lowers the current value of an upper mover and strictly raises it for every mover that moves, so in every c_t-step sequence, with any number of changes of c, no state repeats among the moving steps and T_k(m) ≤ T_∞(m) ≤ 2^(2m) − 1 (VALUE-MONO); for ISO genomes K of 𝓛^R_(m′+1) and G of 𝓛^R_(m+1) and their composite H of 𝓛^R_(m′+m+1) (G's upper levels above K's, G's level 0 dropped, G's ranks and gates above K's), H's c-step is K's c-step on K's movers and G's c_*-step on G's movers with c_* the bit b_(m′) of K's part of the new state (COMPOSE), and the number of steps of every such G-sequence driven by a flip-free c-step sequence of K is at most T^R(m′ + m + 1) (COMPOSE-LB); every ISO genome of 𝓛^R_(m+1) gives, through its upper Ξ-targets, the table C and the bits [g(A_l, k) < g(B_l, k)], a system of the IM frame Φ_m (acyclic Ξ-targets on 2m upper movers, an arbitrary table C with C_z independent of s(z), LOCAL and IM, free key bits, and the BIT-CHAIN step) whose frame step with bit c is the genome's c-step, so T_k(m) ≤ T^Φ_k(m) for every k, T^Φ_k(m) the largest number of moving frame steps with at most k bit changes (FRAME); and MACHINE: T^Φ_1(3) ≤ 10, hence T_1(3) = 10, by a Glucose 4 UNSAT of the frame CNF «T^Φ_1(3) ≥ 11» (sha1 7e611c8b…, regenerated by the frozen encoder experiments/si/box75/frame_P-IDEAL-IM.py, sha1 c3b3a232…, clause groups mapped to Φ_3 in the packet) with a DRUP proof accepted by the forward RUP checker drup.c of RESULTS R112 (sha1 2d4b8eab…; 6,531,220 lemmas; its correctness and the encoder's are premises), a second UNSAT by CaDiCaL 1.5.3 without a proof, and L-NEW's ISO genome kf1_d4_t10 of 𝓛^R_4 (experiments/new/box160/out/kf1_d4_t10.json, sha1 1c0dc8cc…; T_1 = 10 under two simulators): a STRUCTURE / RELAXATION statement inside the IDEAL model; bounds nothing polynomially (VALUE-MONO's bound is exponential); the frame is a relaxation, no converse is claimed; FLIP-ADD, SUM_1 and PAIR-LIN are not claimed; degree ≥ 3, Ξ-cyclic genomes and genomes outside 𝓛^R are not covered except by IM (degree-2 movers of any acyclic genome); T_k(3) for k ≥ 2 is not claimed; DATA, experiments/si/box75/imcheck.py on 404 ISO genomes of 𝓛^R_2, 𝓛^R_3 and 𝓛^R_4, every start; once per state: IM (b), (c) 0 violations on 31,208 checks, (c) with the direction reversed failing 6,284 times; LOCAL 0 on 250,248 (y on neither chain, unhappy or not), among them IM (a) on the 125,124 with y unhappy; independence of s(z) 0 on 66,520; per state and both c: BIT-CHAIN (i) at the c-step image of the state 0 on 66,520 (5,670 distinct (genome, c, image) triples), the negated bit failing 66,520 times; KEY-DIR 0 on 133,040; VALUE-MONO 0 on 133,040; frame step = c-step 0 on 24,184; own c-step = the box 64 simulator 0 on 18,944, on the 301 genomes the box 64 simulator accepts; COMPOSE: experiments/si/box68/compose.py 200 68 (seed 68), 0 disagreements on 200 random pairs with (m′, m) ∈ {1, 2}², and NEG=1 compose.py 200 68, the negated schedule failing 54,433 times on G's part (30,113 steps and 24,320 end-of-run checks) and 21,234 times on K's (end-of-run checks after a failure on G's part only; K's steps do not use the schedule); BIT-CHAIN (ii), COMPOSE-LB and the T_∞ bound: no separate DATA; the encoder: only the m = 2 cross-checks T^Φ_1(2) = 5 against L-COMP's exhaustive T_1(2) = 5 (P-IDEAL-IM, docs/si/P-IDEAL-IM.md with its fixes entry 1, docs/si/P-IDEAL-IM-fixes.md; L-SI successors 39-40). G-N5-TIME stays open.

Addendum (subagent, for the Lead; does not land; written 2026-11-07T01:11:54Z by date -u). (1) FIRST FILL on line L-2 (l-si 4ee9fa78,
sha1 8b7ccfb9…), to CHECKER C128. NOT pushed; my commits: the five merges (--no-ff) 64164445 (l-si 91d40ec2), 16a4af14 (l-comp
cf2e0e4f), 63ca6c68 (referee e7047ace), c873af44 (referee-2 f6bafb36), 9f1806f8 (checker 1c4ba1c3) and one commit holding this file.
Push trunk before landing. (2) TITLE l. 456 = "### R115 [refereed-only] " + L-2 without its newline + ", CHECKER PASS
(docs/checker/C128.md, checker PENDING)", checked by script (chk115.py): equal, byte for byte (True); the only «### R» heading of this
file; 81 + 1 «(» and 81 + 1 «)», balanced; no «[lane», no packet name before the claims. (3) BODY l. 456-744 (python slice d[455:744]; 0
"|" in the range, by script); GAPS preamble l. 746-756 (two "|", both inside quotation marks: the row's closing « |» and «holds no
"|"»); UPDATE l. 757 (d[756]; one line, 0 "|", one each of <DATE>, <HH:MM>, <checker>; 4,646 bytes; sha1
761cec506cc1f466f75b2b66ae6d42bafa7e8a0e of the unfilled line without newline; controls True ×18: R97's-R114's landed UPDATEs). No
Dead-ends row is drafted ((14)). A landing script in the shape of R114's slices d[455:744] for the entry and reads d[756] for the UPDATE
(with «R115», «R114» as PREV, «C128», and the GAPS l. 11 assertion on «RESULTS R114 (P-IDEAL-RISE» as the last UPDATE). (4) RE-RUNS:
listed in the header paragraph "Re-runs", (a)-(h). NOT RUN: Glucose 4, drup.c and CaDiCaL on the m 3 query (their records and both
referees' runs read); the referees' tools; check71.sh; scripts/verify.sh; the full check.sh. (5) QUOTE SWEEP (chk115.py: the rule of
chk114b.py: outermost guillemet quotes, whitespace joined, split at the ellipsis, parts of 6+ characters; sources: the packet, L-1, L-2,
the fixes, imcheck.py, imcheck.out, frame_P-IDEAL-IM.py, pins.sha1, compose.py, box64/flipdp.py, check75.sh, check.sh, check70.sh,
box70/log/3_t1_11.log, N5-FRAME-box70.md, UNSAT-LIST.txt at 4ee9fa78, lsi_q1_cert.txt and bfk_m2_part0.txt on l-comp, both referee files
at bc2bdd5a / 2e68c641 and 280d2313, notes/REFEREE.md and notes/CHECKER.md at the fetched heads, P-TR3.md at d3e3cde8 (for the R104
quote), RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, NOW, LEAD-STATE, TARGET.md, CLAUDE.md, C120-C127, R112-draft, R114-draft at the local
trunk, the commit subjects of the cited commits, my re-run outputs): 489 outermost quotes, 411 parts of 6+ characters, every part found
(0 not found); in the title and body alone 144 quotes, 126 parts, 0 not found; GAPS preamble and UPDATE 14 quotes, 10 parts, 0 not
found. Line-precise: 101 of 101 (source, cited line range, quote) triples found verbatim, whitespace-normalised, inside the cited lines.
Every sha1, line count and commit time cited was re-measured in this session (sha1sum, wc -l, diff, git log -1). STALE STATUS in title
and body (by script): «pending» 2 apart from the title fill «checker PENDING)» (each the open REFEREE successor 25 Addendum 1, G-R);
«not yet» 0; «not landed» 1 (inside the quotation of fixes l. 14, IM-L1, history); «unlanded» 0; «provisional» 0; «to follow» 0; «stays
OPEN» / «stay OPEN» 3 (the title's own «G-N5-TIME stays OPEN» and, in the TARGET.md diff, the quotations of packet l. 6 and of L-2's
tail); «L-3» 0; L-1 only as history. (6) DISCREPANCIES: (11) D-1 to D-6. I found no error in a signed statement; one proof-text point
(G-2 (ii)). (7) FLAGS FOR THE LEAD AND CHECKER: G-0 (C128), G-9 (i) (BIT-CHAIN (ii) has no counter and is not in the no-DATA list; the
C127 E-1 class; REFEREE-2's own W-1 text had it), G-9 (ii) (COMPOSE's NEG «K's part» count: no K disagreement, end-of-run counts of cut
runs), G-9 (iii) (the box 64 cross-check on 301 of the 404 genomes), G-9 (iv) (BIT-CHAIN (i) at the c-step images only), G-9 (v) (LOCAL
(IM (a)) counts happy y too), G-2 (ii) (FRAME's «(Φ2) is Lemma IM (a)» outside IM's hypothesis), G-M (one checker program, three runs),
G-R (REFEREE successor 25's Addendum 1 PENDING: the body's (viii) and Signatures sentences go stale when it lands), G-U (the MACHINE
clause step and the «, and (COMPOSE-LB)» adaptation); NOTES G-10 (L49: CLEAN), G-C (overlaps). (8) NOT VERIFIED: REFEREE successor 24's
drup.c run (stated in its report, log not committed); the referees' Glucose regenerations and drup.c runs (their reports read, not
re-run); the identity of the CaDiCaL input with 7e611c8b… (not logged); L-NEW's box 150 replay of the witness (lane record); L-COMP's
bfk.c (outputs read, not re-run); scripts/verify.sh and the full check.sh were not run. (9) LANDING SIMULATION (sim115.py, on in-memory
copies of RESULTS and GAPS at the local trunk, R114 as landed): RESULTS 13,306 -> 13,596 lines (wc -l), a pure insertion of 290 lines
(the entry block with "checker PENDING)" filled, plus one blank line) directly after R114's landed block (R114 l. 12,394-12,695, blank
l. 12,696, byte-unchanged: True; R110's to R113's blocks byte-unchanged: True): True; R115 at l. 12,697-12,985, blank l. 12,986, the
next line (**Erratum E-1**) moves to l. 12,987, the Erratum E-2 line to l. 13,000, the Note E-3 line to l. 13,028, the Dead ends heading
to l. 13,059; order R110, R111, R112, R113, R114, R115, E-1, E-2, E-3, Dead ends: True; every other line byte-unchanged (common prefix
and suffix: True); 0 "|" inserted. GAPS: only l. 11 changes: True; new l. 11 = old l. 11 with its closing " |" replaced by " " + the
filled UPDATE + " |": True; "|" on l. 11 76 -> 76 (pipe count unchanged); UPDATE 2026- heads 49 -> 49 plus 1 UPDATE head with the
simulation year 2099, directly after R114's and now the last on the line; 23 -> 23 lines (wc -l). Fill values used only for the
simulation: <DATE> 2099-01-04, <HH:MM> 00:00, <checker> 0000000. (10) THIS DRAFT'S SHA1: a file cannot state its own sha1. The sha1 of
this file with the forty hex digits after the next colon replaced by forty «0» characters is: fc3916e1b8db06d97eaf8a61191865ca1cfc9133.
The file's actual sha1 and line count are in the hand-back to the Lead (and re-measurable with sha1sum). Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r115/ (runw75.sh / w75.out, w70.out,
imsplit.py / imsplit.out, compsplit.py / compsplit.out, wdiff115.py / wdiff115.out, prem115.py / prem115.out, upd115.py / upd115.out /
upd115L2.txt, fill115.py (template fill and line wrap), R115-template.md, chk115.py / chk115.final.out, sim115.py / sim115.final.out,
arch4ee9/).
Addendum 2 (subagent, for the Lead; does not land; written 2026-11-07T03:02:04Z by date -u). (1) SECOND FILL on line L-3 (l-si 80d1422a,
sha1 cf510950…), to CHECKER C128 Add. 1. NOT pushed; my commits: the four merges (--no-ff) 256e7461 (l-si 77d536f6), d06fff51 (referee
0c2a7c5b), 909706e4 (referee-2 0a9e2a16), d6410595 (referee 3fb22563) and one commit holding this file. (2) TITLE l. 523 = "### R115
[refereed-only] " + L-3 without its newline + ", CHECKER PASS (docs/checker/C128.md, checker PENDING)", checked by script (chk115b.py):
equal, byte for byte (True); the only «### R» heading of this file; 86 + 1 «(» and 86 + 1 «)», balanced; no «[lane», no packet name
before the claims. (3) BODY l. 523-883 (python slice d[522:883]; 0 "|"); GAPS preamble l. 885-896 (two "|", both inside quotation marks:
the row's closing « |» and «holds no "|"»); UPDATE l. 897 (d[896]; one line, 0 "|", one each of <DATE>, <HH:MM>, <checker>; 4,993 bytes;
sha1 39d9a2925c2c193193f3b0845b37919defa75a2b of the line without newline, computed on the UNFILLED form, as C128 §5 l. 117-118 states
it, «Rebuilt UPDATE (the same five replacements in d[756], line without newline, unfilled): sha1
39d9a2925c2c193193f3b0845b37919defa75a2b»: equal). A landing script slices d[522:883] for the entry and reads d[896] for the UPDATE
(with «R115», «R114» as PREV, «C128», and the GAPS l. 11 assertion on «RESULTS R114 (P-IDEAL-RISE» as the last UPDATE). (4) WHAT IS LEFT
TO FILL: only the title's «checker PENDING)» and the UPDATE's three placeholders, at landing. The one open referee item is REFEREE
successor 25's «R-P-IDEAL-IM Addendum 1» (ref_rup_del on the 2.4 GB proof): not on origin at 2026-11-07T03:09:23Z (claude/referee
3fb22563); optional by C128's ruling G-M / G-R. If it ACCEPTS before landing, the Lead may cite it in What rests on the machine (viii)
and the Signatures; if any referee file on origin at landing reports a second checker REJECTING the proof, R115 does not land (C128 l.
74). The body's two PENDING sentences go stale when it lands. (5) QUOTE SWEEP (chk115b.py: chk115.py's rule and sources, plus L-3, the
fixes, check75.sh, mkL3.py and pins_fix2.sha1 at 80d1422a, R-P-IDEAL-IM.md at 0c2a7c5b and 3fb22563, R2-P-IDEAL-IM.md at 0a9e2a16,
notes/REFEREE.md at 3fb22563, C128, the first-fill draft bc987999, the commit subjects of the new commits, my second-fill outputs): 575
outermost quotes, 486 parts of 6+ characters, every part found (0 not found); in the title and body alone 172 quotes, 154 parts, 0 not
found; GAPS preamble and UPDATE 14 quotes, 10 parts, 0 not found. Line-precise: 123 of 123 (source, cited line range, quote) triples
found verbatim, whitespace-normalised, inside the cited lines. (6) WORD DIFF bc987999 → this file (wd115b.py, difflib on whitespace
tokens, Addendum 2 left out): 24 line regions, 101 token hunks (127 tokens deleted, 3126 inserted), every hunk in a region listed in
the SECOND FILL paragraph. (7) STALE STATUS in title and body (by script): «pending» 2 apart from the title fill «checker PENDING)»,
both REFEREE successor 25's Addendum 1 (What rests on the machine (viii), Signatures), true at this fill; «not yet» 0; «not landed» 1
(the quotation of fixes l. 14, IM-L1, history); «unlanded» 0; «provisional» 0; «to follow» 0; «stays OPEN» / «stay OPEN» 3 (each about
G-N5-TIME, as at the first fill); L-2 named as the current line («RESULTS line is L-2», «title is L-2», «The RESULTS line (L-2)», «line
(L-2)», «L-2's DATA parenthesis», «(L-2, by script)», «L-2's parentheses», «title line L-2», «L-2 holds no», and L-2 with a colon before
the premise quote), by script in the title, the body, the GAPS preamble and the UPDATE: 0 times; the old strings of R1-R4 (C128 §5) 0
times there, and R5's old phrase only inside «BIT-CHAIN (ii), COMPOSE-LB and the T_∞ bound: no separate DATA»; «on K's part» 0; «L-2» 19
times in the title and body, every one history (the line history, the L-2 verdicts and word diffs, fixes entry 1, the pins, R1-R5's
base); MOVES-2D and P-IDEAL-MOVES 0 times in the title, the body and the UPDATE. (8) G-9 CHECK of L-3's DATA (l3rel115.py, rc 0): 15 of
15 DATA phrases, each once in L-3's DATA parenthesis, agree with the frozen imcheck.out, compose.py's two lines, my first-fill splits
(imsplit.out: 125,124 of the 250,248 with y unhappy, 5,670 distinct c-step images, Ext fails on 103 genomes so XSTEP runs on 301;
compsplit.out: K in-run 0, G in-run 30,113, K end-of-run 21,234, G end-of-run 24,320) and the figures of C128 §3 / §5, REFEREE §C add. 1
and REFEREE-2 Addendum 2: True. Every signed clause of L-3 has a counter of matching unit, set and scope or is in its no-DATA list
(BIT-CHAIN (ii), COMPOSE-LB, the T_∞ bound, the encoder's m = 2 cross-check named as such). (9) LANDING SIMULATION (sim115b.py:
sim115.py with the UPDATE's sha1 assertion 39d9a292…, otherwise unchanged, on in-memory copies of RESULTS and GAPS at the local trunk,
R114 as landed): RESULTS 13,306 -> 13,668 lines (wc -l), a pure insertion of 362 lines (the entry block with "checker PENDING)" filled,
plus one blank line) directly after R114's landed block (R114 l. 12,394-12,695, blank l. 12,696, byte-unchanged: True; R110's to R113's
blocks byte-unchanged: True): True; R115 at l. 12,697-13,057, blank l. 13,058, the next line (**Erratum E-1**) moves to l. 13,059, the
Erratum E-2 line to l. 13,072, the Note E-3 line to l. 13,100, the Dead ends heading to l. 13,131; order R110, R111, R112, R113, R114,
R115, E-1, E-2, E-3, Dead ends: True; every other line byte-unchanged (common prefix and suffix: True); 0 "|" inserted. GAPS: only l. 11
changes: True; new l. 11 = old l. 11 with its closing " |" replaced by " " + the filled UPDATE + " |": True; "|" on l. 11 76 -> 76 (pipe
count unchanged); UPDATE 2026- heads 49 -> 49 plus 1 UPDATE head with the simulation year 2099, directly after R114's and now the last
on the line; 23 -> 23 lines (wc -l). Fill values used only for the simulation: <DATE> 2099-01-04, <HH:MM> 00:00, <checker> 0000000. (10)
NOT VERIFIED: the referees' tools and C128's instrumented runs not re-run (their files read; my first-fill splits measure the same
figures); scripts/verify.sh and the full check.sh not run; Glucose 4, drup.c and CaDiCaL not run; the Lead's relay to L-SI (fixes l. 58)
is a message, not verifiable from the repository. (11) NOTES for the CHECKER, no verdict affected: (i) fixes entry 2 l. 58-60 says the
pairs were taken from the Lead's relay «of C128 §4» with C128 unopened; they are C128 §5's pairs (equal by script, l3rel115.py), and
REFEREE confirmed them against C128 itself (§C add. 1 l. 174-175). (ii) Header stamps: REFEREE's §C add. 1 first read «2026-11-07T03:0xZ
by date -u», after its commit time 02:30:13Z, and 3fb22563 (02:49:14Z) corrected it to «committed 2026-11-07T02:30Z (0c2a7c5b)»;
REFEREE-2's Addendum 2 header reads «2026-11-07 02:5xZ by date -u», after its commit time 02:31:16Z, uncorrected on origin at
2026-11-07T03:09:23Z; the body cites the commit times and quotes both stamps. (iii) L-3's source note still reads «with its fixes entry
1» and «L-SI successors 39-40», as C128 §5 requires (five replacements, nothing else changes; the R113 / R114 precedent); entry 2
carries no proof and is named in the body (Object, L41 and L43, Fixes, Signatures). (iv) REFEREE-2's Addendum 2 signs «(Opus 5.5, D1)»,
its earlier sections D12; quoted as written. (v) The body's FRAME proof sentence (Claims (f)) now uses C128 §4's wording; packet l. 207
is frozen and is read through fixes entry 2 l. 72-73. (vi) C128's notes N-1 and N-3 are recorded in Honest limits (iv), N-2 in Data.
(vii) The entry block grew from 289 to 361 lines (the third rounds, fixes entry 2, Referee strengthening (iii), the ruling in (viii)).
Scratch: /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r115/fill2/ (edit115b.py,
header1.txt, secondfill.raw / sf115.py / secondfill.txt, addendum2.raw / add2.py / addendum2.txt, l3rel115.py / l3rel115.out, upd115b.py
/ upd115b.out / upd115L3.txt, runw75L3.sh / w75L3.out, chk115b.py / chk115b.out, wd115b.py / wd115b.out, sim115b.py / sim115b.out,
R115-draft-bc987999.md, arch80d1/).
