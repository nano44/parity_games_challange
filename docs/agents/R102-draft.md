# Draft RESULTS R102 (Lead; first fill 2026-11-01T06:35:47Z by date -u, read in the same command as the fill of this file (subagent); on S4B line L-1, — LANDED in RESULTS 2026-11-01 10:09Z (CHECKER C113 c5c0ab5f PASS), after R101, before Erratum E-1
docs/si/P-N5-S4B-line-L1.txt (l-si 96fb62cb3, sha1 95373010d54c69907308d224fa1111127055b8f5); packet, frozen line f8559b5e, L-1, fixes F0
+ entries 1-5, REFEREE's R-N5-S4B (successor 22's report 062cd734 and §C 2e6467fd) and REFEREE-2's R2-N5-S4B (1b9ef2e1) and
R2-N5-S4B-L1 (0e8ae566) read at the origin heads fetched at the start of the fill, 2026-11-01 before 06:24Z (l-si 96fb62cb, referee
2e6467fd, referee-2 0e8ae566, checker d53e1d4f; origin trunk 6d5dd3cd; local trunk head 6d5dd3cd at the start and 316f7d14 at the fill,
which changes neither RESULTS, GAPS nor DECISIONS); RESULTS R101 and the Erratum E-1 paragraph read LANDED (trunk 110e380b / 6d5dd3cd);
L-SI's box 63, «P-N5-S4B pinned» and L-1 pin blocks of experiments/si/check.sh re-run from a git archive of 96fb62cb3 2026-11-01
06:24:49Z, rc 0; the sym_h8_s1 mutation control 06:26:26Z, rc 0; DATA re-summed 06:25:01Z) — to CHECKER C113
REFEREE successor 22's §C (2e6467fd, the L-1 verdict) is on origin claude/referee only, NOT on the local trunk (316f7d14) nor on origin
trunk 6d5dd3cd: the Lead merges claude/referee and pushes trunk before landing. Every other commit cited here is on both (by script,
firsttrunk.py). C112 is a separate erratum check; this entry goes to C113. In the body (title + entry), sentences about the earlier line
revision say «at the frozen line»; every other sentence of the body describes L-1.
LEAD DECISION G-1 (2026-11-01T06:45:18Z, date -u): the Lead inserts « (2026-11-01)» into the title immediately before « — a premise result», as R88's and R90's drafts did before « — a REDUCTION» (R88-draft l. 5, R90-draft l. 9); nothing else in the line changes, and no packet name is added (the body and the GAPS UPDATE name P-N5-S4B). The UPDATE line is unchanged (R94-R101 rule drops the date). CHECKER: the title must equal «### R102 [refereed-only] » + L-1 with that one insertion + the checker fill. R99's landed L42-era sentences about [S4b-OPT] are not edited (true when landed; R102 records L45).
to check: FLAGS FIRST. G-1 is a title-shape item; G-2 is the L45 check the Lead asked for (the C111 E-1 class); G-3 to G-5 are what the
pre-check of L-1 against CHECKER's recurring E-items (C106 E-1, C108 E-1, C109 E-1 / E-2, L43, C110 F-1, C111 E-1) raised. No referee
raised any of them as REQUIRED; I changed nothing in the line. The CLEAN items follow the flags; soft spots D-1 to D-8.
- FLAG G-1, A TITLE WITH NO DATE AND NO SOURCE NOTE (CHECKER decides). L-1 contains «2026» 0 times and «P-N5-S4B» 0 times (by script).
  Every landed title R80-R101 carries a "(YYYY-MM-DD)" date, and R90, R92 and R95-R101 name their packet (by script over the «### R»
  headings of RESULTS). R102 would be the first landed title since at least R80 with no date, and the first since R94 with no packet name
  or source path. The line's tail is « — a premise result under 1E-N3 only, lane-authored (L-SI; not referee-originated): …», with no
  final source parenthesis (R101's ends «(P-N5-GATE, docs/new/P-N5-GATE-box120.md with its fixes entry 1, docs/new/P-N5-GATE-fixes-box120.md;
  L-NEW successors 43-44)»). Precedent for a Lead-side date: R88's and R90's drafts inserted the date immediately before « — a REDUCTION»
  (docs/agents/R88-draft.md l. 5, R90-draft.md l. 9); R91-R101 kept the line's own date. NOT APPLIED: the Lead's instruction for this
  draft is title = prefix + L-1 + fill (checked by script, (1)). If CHECKER asks: (a) a date « (2026-11-01)» goes immediately before « — a
  premise result» (one « — » in L-1; the R88 / R90 rule), and the UPDATE is unchanged except that the builder then splits at that date;
  (b) a source note needs a line L-2 from L-SI (PARKED, docs/NOW.md l. 45), e.g. "(P-N5-S4B, docs/si/P-N5-S4B-box63.md with
  docs/si/P-N5-S4B-fixes.md; L-SI successor 38)" (my wording). The packet's identity is in the body (Object) and in the UPDATE head.
  Neither referee raised either point (REFEREE §5 l. 110-117 and §C l. 148-157; REFEREE-2 §5 l. 87-95 and L1 l. 6-18).
- FLAG G-2, L45 AS NOW ON FILE (the C111 E-1 class; the Lead's check). RESULT: L-1 STATES L45 ACCURATELY. L-1: «(1E-N3: «that S1's
  procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance», RESULTS R57 (b)), read on every game input of S1's procedure (Lead
  reading L45, lifting L42's S4b restriction): for every finite game graph G* …». On file, docs/DECISIONS.md l. 383-390 (322922ec,
  2026-11-01T04:10:34Z): «Lead reading L45 (2026-11-01 04:10Z by date -u):», «S4b is covered by R57's 1E-N3. L42's restriction («R57
  covers S1 and S4a only; [S4b-OPT] not covered») is LIFTED for S4b: S4b runs S1's», «L42 stays in force for any premise other than S1's
  procedure on a valid input.» docs/DECISIONS-INDEX.md l. 35 (L42) «active (S4b part lifted by L45)»; l. 38 (L45) «Lead reading: L42's
  S4b restriction lifted; S4b runs S1's procedure on H′, covered by R57 1E-N3 (P-N5-S4B signed by both referees) | active». So «lifting
  L42's S4b restriction» = «LIFTED for S4b» and the index's «S4b part lifted by L45»; «read on every game input of S1's procedure» is not
  wider than L45's last sentence («S1's procedure on a valid input»), and Lemma S4B-OPT uses it only at G* := H′_k (packet §2 (ii) l. 38).
  L42 stays active for every other premise (index l. 35), and L-1 does not say otherwise. The R57 (b) quote is verbatim (RESULTS l.
  2915-2916, by script). Both referees checked L45 on trunk: REFEREE §C l. 137 «L45 is on trunk (68d50c8f, docs/DECISIONS.md l. 383-390)
  with that content.»; REFEREE-2 L1 l. 10 «L45 is on trunk (docs/DECISIONS.md l. 383, «Lead reading L45 (2026-11-01 04:10Z …)»).».
  TIMING: L45 (322922ec, 04:10:34Z) is on trunk 1 min 54 s before L-1 (96fb62cb, 04:12:28Z) but is not an ancestor of 96fb62cb (l-si's
  last trunk merge is 9e92ebea, 03:44:27Z); fixes F0 l. 11 says «The Lead reports Lead reading L45 (docs/DECISIONS.md, being pushed by the
  Lead at the time of writing)», a lane-file status sentence that is now stale (L45 is on file) and does not land.
  LANDED TEXT WRITTEN UNDER L42 (not edited by R102; the Lead decides on a note): R99's body l. 8649 «[S4b-OPT] (NOT covered, L42; used
  only in §2)» and l. 8751-8758 (O-ARENA withdrawn, «which R57's premise does not cover (L42).»); R98's body l. 8361 cites L42 for
  another premise. They state L42 as it stood at R99's landing (2026-10-31 23:12Z). L45's effect sentence covers them: «lemmas that used
  [S4b-OPT] / [S4b-KEEP] (e.g. O-ARENA, withdrawn from P-N5-STAIR under L42) are as conditional as every landed N5 result, i.e. on R57's
  SPEC premise only; they still need their own referee review to land.» R102 lands neither O-ARENA nor any use of S4B-KEEP. R101's
  body («Lead reading L42 covers S4a; no item uses S4b optimality») stays true.
- FLAG G-3, NEW IN A TITLE (note; no precedent needed by a rule): (i) a numbered Lead reading cited in a title (R80-R101 titles: 0
  «Lead reading L», by script); it is REFEREE's prescribed form, §5 l. 103 «… 1E-N3, read on every game input of S1's procedure (Lead
  reading L4x, lifting L42): for every finite game graph G* …»; (ii) «lane-authored» in a title (first; R94's L41 tail says the
  opposite case, «referee-originated»); (iii) two referee files cited by path and section in the title, docs/referee-2/R2-N5-1E.md §2 and
  docs/referee-2/R2-N5-S4B.md §2 (R95's title cites one docs/referee path, by script); (iv) a DATA clause with a corpus count in the
  title (R86, R97 and R98 have «DATA» in their titles).
- FLAG G-4, STRICT SYMBOL TEST (the C109 E-2 class; soft, CHECKER decides). (i) «σ̄» occurs once in L-1, inside the verbatim R57 (b)
  quote; it is not glossed in the line. It is SPEC S1's symbol («Ξσ = valuation of every vertex under σ and Odd's OPTIMAL
  counterstrategy σ̄», SPEC l. 32) and R57's Setting's (RESULTS l. 2900-2901 «Ξσ: Even's honest valuation of σ against S1's optimal Odd
  counterstrategy σ̄»); L-1 names SPEC S1-S5. (ii) «G» in «G's priorities», «G^d» and «priorities of G» is not named beyond «N5 on
  EVERY game» (= R101's G-4, a note in C111). (iii) «pointwise optimum» (twice) is not defined in L-1; Lemma S4B-OPT's inequality states it
  for H′_k, and SPEC S1 defines «OPTIMAL» as «minimising this order at every vertex at once». The referees' binder tests pass: REFEREE §5
  l. 111-112 «Binders: G*, σ* bound in the 1E-N3 clause; k, ρ, x in the lemma; H′_k, τ_new,k, val, ⊴, Odd fallback and τ-stretch
  transition are defined; no free symbol.» (the frozen line), §C l. 151 «Binders unchanged (G*, σ*; k, ρ, x).»; REFEREE-2 §5 l. 92-94
  «G* and σ* are bound inside the 1E-N3 gloss. No free symbol.» (the frozen line, which had no σ̄). σ̄ entered at L-1, inside the quote
  REFEREE §C l. 135 checked («verbatim»).
- FLAG G-5, NAMES (note). «S4B-OPT» and «S4B-KEEP» occur 0 times in RESULTS and GAPS; «S4b-OPT» (lower-case b) occurs 8 times in
  RESULTS, all as L42's / R99's bracketed premise name «[S4b-OPT]» (l. 8616-8758). L42 defines it as «S4b's τ' is a pointwise optimum
  of O(τ) against the old σ», with P-N5-STAIR's O(τ) = τ ∪ Iτ (docs/new/P-N5-STAIR-box112.md l. 181 «(Lemma O-ARENA) W_k is σ_k's
  best-response value with Odd restricted to O(τ) = τ ∪ Iτ;»): the first half of Lemma S4B-OPT in other notation, as L45's effect
  sentence reads it («lemmas that used [S4b-OPT] / [S4b-KEEP]»; my reading, not a referee statement). «τ-stretch transition» occurs 0
  times; R89's «τ-stretch» (a maximal run of consecutive states with τ constant) is consistent with L-1's «a transition k → k + 1 with
  τ_(k+1) = τ_k». «Odd fallback» occurs 3 times in RESULTS (l. 2581, 5131, 5341), each an S4c fallback on Odd's side (the same object).
- CLEAN AT L-1 (the same pre-check, by script on 95373010):
  C106 E-1 (stale body / old line as current): the title is L-1; the body describes L-1 as current, the frozen line only in history
  sentences («at the frozen line»); the old counts 7,772 / 6,719 / 1,053 / 290,345 / 36 occur in the body only as the frozen line's,
  the packet §4's, REFEREE-2's report's and the re-sum's with-repeats row.
  C108 E-1 (DATA overclaims): L-1's DATA clause states the de-duplicated counts of the lane's enumeration («5,058 states … among the
  5,726 states … of the 813 distinct game/start lines», «(a list of 1,132 lines with 319 exact repeats; counts de-duplicated; 668
  states not enumerated)»), equal to my re-sum of the stored output (Data), to REFEREE's reading of the lane file (§4 l. 80) and to
  REFEREE-2's own tool on the 813 lines (L1 l. 25-29). It claims no referee check. The mutation-control clause names two instances and no
  number; the lane's 215 (check.sh) and 677 (my re-run) bite, and both referees' own tools bite on both (REFEREE §4 l. 90; REFEREE-2 §4 l.
  82). CONSISTENT WITH THE ERRATUM: RESULTS «**Erratum E-1**» (l. 9478-9489) reads «1,132 lines = 813 distinct (game, start) pairs on 719
  distinct games; the 319 start-less lines of alt_all.lst are each an exact repeat of an sbcg.lst run» and ends «Later lines state
  de-duplicated counts (P-N5-S4B line L-1: 813 distinct game/start lines).» L-1's «813 distinct», «1,132 lines» and «319 exact repeats»
  are those figures; L-1 is the first landing line stating them. «games» 0 times in L-1; «corpus» once («corpus_fixed.lst», a file name).
  C109 E-1 / L41 (referee-originated clause): L-1 contains «referee-originated» once, «lane-authored (L-SI; not referee-originated)»
  (unchanged from the frozen line). The proofs are the packet's (§2 l. 35-43, §3 l. 51-52), written by L-SI successor 38 (l. 2); no
  referee repaired a proof (both: no gap). REFEREE §5 l. 115 «L41: «lane-authored (L-SI; not referee-originated)». L43: no DEAD.»;
  REFEREE-2 §5 l. 91 «No DEAD (L43). No referee-originated proof (L41).»; REFEREE §C l. 152-153 (unchanged ✓). Two L-1 WORDINGS came
  from referees: «read on every game input of S1's procedure» (REFEREE's S4B-L1 example) and «confirmed for arena inputs in
  docs/referee-2/R2-N5-S4B.md §2» (REFEREE-2's P-1). They are line wording and a citation, not proofs (L41 is about proofs), and the
  second says whose confirmation it is.
  L43 (asymptotic DEADs): «DEAD» 0, «O(» 0, «c·n» 0, «linear» 0, «unbounded» 0 in L-1; the packet has no DEAD (§5 (c) l. 79).
  C110 F-1 (stale pins vs landed labels): the one commit pinned in L-1, l-si 9521f2e72bf049e71de7eadec7853d99227b9dc7, is the only commit
  of experiments/si/anc58/s4bopt.py (sha1 6c4e852b… at 9521f2e7 = 68fa3661 = 96fb62cb = trunk) and of anc58/s4bopt_corpus.txt (d7e181d2…,
  unchanged since); corpus_fixed.lst (d6ed7557…) is unchanged at 68fa3661, 96fb62cb and trunk. The premises are landed labels: RESULTS
  R57 (b) (1E-N3) and R15's G-N5T-1, plus SPEC text; no lane packet and no unlanded result is a premise. The two referee files are cited
  at their current versions: R2-N5-1E.md (last changed bd68d39d, 2026-10-26; §2 l. 55-61, N-1E-1 at l. 56) and R2-N5-S4B.md (its only
  commit 1b9ef2e1, = referee-2 head = trunk).
  C111 E-1 (stale Lead-reading statements): G-2; L-1 cites L45 and L42 as now on file. The body below says L42 is «active (S4b part
  lifted by L45)».
- Soft spots, no referee raised them as REQUIRED (details in (7)): D-1 «Iσ_k» beside «I_τ_k» (packet notation); D-2 «SPEC text S4c,
  S4d, FIX 3» (FIX 3 is SPEC file text, not an S-label); D-3 the sym_h8_s1 mutation control is not pinned in check.sh; D-4 the packet's
  S4b quote writes «H′» where SPEC has «H'»; D-5 a dropped clause in a fixes-file quote; D-6 REFEREE-2 L1 l. 13's quote of the frozen
  line; D-7 REFEREE-2's report counts with repeats; D-8 the packet header's «02:24Z».
(0) PLACEMENT, R101 LANDED. R102 goes after R101. R101 (P-N5-GATE box 120) LANDED at trunk 110e380b (2026-11-01 05:29Z; CHECKER C111 Add.
1 d53e1d4f PASS); the Erratum E-1 paragraph followed (110e380b), re-headed as a bold paragraph by 6d5dd3cd (05:55Z). docs/RESULTS.md at
origin trunk 6d5dd3cd (identical at the local trunk head 316f7d14) has sha1 bd992a19cd9bb5fbb49e59a87426d3c406191716, 10,011 lines, last
changed by 6d5dd3cd. «### R101» is l. 9251 (entry l. 9251-9476, l. 9477 blank); «**Erratum E-1**» is l. 9478 (paragraph l. 9478-9489,
l. 9490 blank); «## Dead ends (kept;» is l. 9491. "### R102", "R102" occur 0 times in RESULTS and in GAPS (sha1
e3d8fcc962dc87162a2f8618d4ac9c78231f92a0, 23 lines, last changed by 110e380b); «P-N5-S4B» occurs once in RESULTS (the Erratum's last
sentence, l. 9489) and 0 times in GAPS, so no name clash (unlike R100's F-4). PROPOSED (the Lead's preference): R102's entry goes
DIRECTLY AFTER R101, i.e. after l. 9477 (R101's blank line) and BEFORE «**Erratum E-1**», with one blank line after it, so the R-entries
stay contiguous and the erratum paragraph closes the Results section. The erratum's own line numbers (l. 7963-9195, all in R96-R100) lie
before the insertion and do not move. (Alternative: after the erratum's blank line l. 9490, before «## Dead ends»; the erratum text needs
no change either way.) The Lead re-checks (6) and (9) at landing only if RESULTS or GAPS change after bd992a19 / e3d8fcc9.
(1) TITLE. The title is the line file docs/si/P-N5-S4B-line-L1.txt (l-si 96fb62cb37200773fe1b5211843af7986c82337e, 2026-11-01T04:12:28Z,
the file's only commit, sha1 95373010d54c69907308d224fa1111127055b8f5; identical at the l-si head and at trunk; first on trunk by merge
cfde8a92, 05:02:35Z), verbatim: one line, no outer quotes, no final period, 2,600 characters (2,691 bytes plus the newline), 448
whitespace tokens. NO HEADING MARKER, verified by script: the file begins «N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise
of RESULTS R57», with no «#», no «R??» and no lane tag (L41 «Lanes write line files without a heading marker (C104 N-1).»). So NOTHING is
stripped: the heading is the level-3 marker, then "R102 [refereed-only] ", then the file without its newline, then the fill. L-1 holds
NO date and NO "|" (by script); the Lead inserts « (2026-11-01)» before « — a premise result» (G-1 decision, below). The checker fill ", CHECKER PASS (docs/checker/C113.md, checker PENDING)" is
appended as in R90-R101 (no space before the comma); L-1 ends «(experiments/si/anc58/s4bopt.py, l-si
9521f2e72bf049e71de7eadec7853d99227b9dc7)», so the heading ends "… 9521f2e72bf049e71de7eadec7853d99227b9dc7), CHECKER PASS (…)". Built by
script (scratch fill102.py: assert the sha1 95373010…, equality with the working-tree file and with the blob at 96fb62cb, one line, no
marker, no «2026», no "|"; prepend "### R102 [refereed-only] ", append the fill) and re-checked after writing this file: equal, byte for
byte. Heading: 2,679 characters, 2,770 bytes; sha1 of the heading line without its newline 8494813eeae2b47efaf6efadd6659c835442930e; it is l. 283.
(2) LINE HISTORY: the frozen line docs/si/P-N5-S4B-line.txt (sha1 f8559b5e539a461a0fac89a5a9bf6f4432721c74, committed with the packet in
68fa3661, 2026-11-01T02:23:22Z; 2,255 characters, 391 tokens, no "|", no marker, no date; the line both reports reviewed) → L-1 95373010
(docs/si/P-N5-S4B-line-L1.txt, l-si 96fb62cb, 04:12:28Z, 2,600 characters, 448 tokens; fixes F0 + entries 1-5). The frozen line is
history, not the title. Each line file has one commit (git log on l-si). Word diff measured (difflib over whitespace tokens, scratch
wdiff102.py): 391 → 448 tokens, 9 non-equal opcodes, 380 tokens in common, grouped into exactly five changes:
- (1) the 1E-N3 gloss opens with R57 (b)'s words and the L45 reading: inserted ««that S1's procedure realises an optimal σ̄ is VJ00 §6
  plus SPEC conformance», RESULTS R57 (b)), read on every game input of S1's procedure (Lead reading L45, lifting L42's S4b
  restriction):» (REFEREE S4B-L1; fixes entry 1);
- (2) «G*; scope as signed by REFEREE-2,» → «G* (the setting of VJ00 and of S1 as in» (S4B-L1; entry 1, third bullet);
- (3) «hypothesis»)),» → «hypothesis», confirmed for arena inputs in docs/referee-2/R2-N5-S4B.md §2)),» (REFEREE-2 P-1; entry 5);
- (4) «(SPEC S4c, S4d, FIX 3)» → «(SPEC text S4c, S4d, FIX 3)» (REFEREE S4B-P1; entry 3);
- (5) the DATA counts de-duplicated: «6,719» → «5,058», «7,772» → «5,726», «1,132-game corpus» → «813 distinct game/start lines of»,
  «(1,053» → «(a list of 1,132 lines with 319 exact repeats; counts de-duplicated; 668» (REFEREE S4B-L2; entry 2).
= REFEREE §C l. 134 («Five changes, the ones the Lead listed. Nothing else changed:»), items 1-5 l. 135-147 (its item 2 = my (2), its 3
= my (3)); = REFEREE-2 R2-N5-S4B-L1.md l. 6-18 («Token diff: every change, nothing else», four items: its item 2 = my (2) + (3)), l. 18
«Nothing else changed. The Lemma and Corollary statements, the binder and the scope tail are token-identical.» No inequality of a signed
statement differs between the frozen line and L-1: (1)-(3) re-attribute the premise, (4) adds one word, (5) changes DATA counts.
(3) THE LINE AT BOTH REFEREES. L-1 (the title): REFEREE successor 22, docs/referee/R-N5-S4B.md «## §C (successor 22, 2026-11-01T05:03Z by
date -u; Opus 5.5, D15): word-diff of line L-1» l. 131-157 (2e6467fd, 05:03:24Z, +28/−0): l. 138 «**S4B-L1 met.**», l. 147 «**S4B-L2
met.**», l. 157 «Verdict: line L-1 **MATCHES**. S4B-L1 and S4B-L2 are met.» REFEREE-2 successor 25, docs/referee-2/R2-N5-S4B-L1.md
(0e8ae566, 05:04:43Z, new file, 42 lines, sha1 2252e92e78dca736cf52844718b24bb05dd29754): l. 2 «(re-hashed: match)»; l. 31 «The DATA
clause is exact.»; l. 34 «**MATCHES** (Opus 5.5, D15). Nothing REQUIRED.» 2e6467fd is on origin claude/referee only (header); 0e8ae566
is on both (merge d9906071, 05:28:33Z).
Frozen line: REFEREE successor 22's report (062cd734) table l. 14 «**REQUIRED S4B-L1** (attribution of the quantified 1E-N3 form) and
**S4B-L2** (DATA counts include 319 repeated list lines; §5)»; REFEREE-2 25 (1b9ef2e1) §5 l. 95 «Verdict on the line: **MATCHES** (Opus
5.5, D15). The optional P-1 wording is in §2 (b).» So the referees DIFFERED on the frozen line (REFEREE two REQUIRED items, REFEREE-2
MATCHES with one optional precision); REFEREE-2 wrote first (02:53:38Z, before REFEREE's 03:19:48Z) and did not see the 319 repeats
then (its §4 table l. 74-78 reproduces the with-repeats counts); in L1 l. 21-22 it measures them («All 319 are the start-less alt_all
lines, each an exact repeat of a box59/sbcg.lst line.») and in l. 25-31 reproduces L-1's counts. Both MATCH L-1.
LINE-ITEM NAMES: REFEREE S4B-L1, S4B-L2 (REQUIRED), S4B-P1, S4B-P2 (optional precisions); REFEREE-2 P-1 (optional). Fixes F0 l. 12-13 and
entries 1-5 map each; S4B-P2 needs no line change (entry 4 l. 50 «No line change: the line does not restate that step.»; REFEREE §C l.
143-144 «S4B-P2 (the S2 citation) is a proof-text precision. It is not needed in the line and stays with the fixes file entry 4.»).
(4) CLAIMS SIGNED = the items below, each SIGNED in BOTH referees' verdict tables (REFEREE "## 0. Verdicts" l. 7-14 of R-N5-S4B.md;
REFEREE-2 "## 1. Claims table" l. 14-18 of R2-N5-S4B.md), AND stated by L-1 (checked clause by clause against the packet statements):
| item (packet §, lines) | REFEREE (successor 22) | REFEREE-2 (successor 25) |
| --- | --- | --- |
| (a) Lemma S4B-OPT (§2, l. 32-46; statement l. 33-34) | l. 10 «**SIGNED** (precision S4B-P1)»; §2 l. 45-57 | l. 17 «**SIGNED**»; §3 l. 51-57 |
| (b) Corollary S4B-KEEP (§3, l. 48-53; statement l. 49-50) | l. 11 «**SIGNED** (precision S4B-P2)»; §3 l. 59-62 | l. 18 «**SIGNED**»; §3 l. 58-60 |
Both, verbatim: REFEREE l. 16 «No gap in the mathematics.», FINDINGS l. 123 «Lemma S4B-OPT and Corollary S4B-KEEP are SIGNED, with no
gap.»; REFEREE-2 l. 20 «No gap. The premise is 1E-N3 alone, read as in §2 below.», FINDINGS l. 100 «Lemma S4B-OPT and Corollary
S4B-KEEP are SIGNED (Opus 5.5, D15), with no gap. The line MATCHES.»; fixes F0 l. 5 «Both referees SIGNED Lemma S4B-OPT and Corollary
S4B-KEEP with no gap:». The packet's to-sign table (l. 9-14) names exactly these two; §4 is «DATA, NOT to sign».
Clause checks (L-1 against the packet): (a) l. 33-34 verbatim up to «:» → «,» and «Moreover» → «and», with «(SPEC text S4c, S4d, FIX 3)»
appended (S4B-P1); the setting's H′_k and τ_new,k (l. 28) written out in L-1 as «SPEC S4b's arena at k (Odd v keeps the edges to
{τ_k(v)} ∪ {w : (v, w) ∈ I_τ_k}, Even v keeps the edge to σ_k(v), priorities of G)» and «SPEC S4b's output at k» (= SPEC S4b, l.
54-55, with A(v) written out); «Odd fallback» (l. 29) and «τ-stretch transition» (l. 29-30) as in the packet. (b) l. 49-50 verbatim up
to «:» → «,» and «Hence» → «so». The packet's [1E-N3] form (l. 20-22, «satisfies val(σ*, ρ*)(x) ⊴ val(σ*, ρ)(x) for every positional
Odd strategy ρ of G* and every vertex x») is L-1's «is a pointwise optimum against σ* in G*». Nothing in L-1 is wider than signed.
Signed by both, NOT stated by L-1, so NOT landed: none of the claims; the Remark (no dual) (l. 44-46) is not stated (REFEREE-2 l. 61
«Remark (no dual) is correct. Not to sign.»). Not signed, so NOT landed: §4 DATA (only as the title's DATA clause, «not part of the
claim»), §5 (the line draft and its pre-check).
(5) OTHER TEXTS THE ENTRY DEPENDS ON: the premise is R57 (b)'s 1E-N3 (a landed label) read by Lead reading L45; SPEC S1-S5 (with FIX 3),
docs/new/N5-ssi-global.md; N-1E-1 (docs/referee-2/R2-N5-1E.md §2, l. 56-61, REFEREE-2 successor 13, ceed1f63 / bd68d39d, the R57 review)
and REFEREE-2's R2-N5-S4B.md §2 (b) as cited setting statements. No lane packet is a premise. The working note docs/si/N5-S4B-box63.md is
history (packet l. 4 «Working note: docs/si/N5-S4B-box63.md (this packet governs).»).
(6) PREMISE LABELS (stale-label test; RESULTS at bd992a19 = origin trunk 6d5dd3cd = trunk 316f7d14). RESULTS labels in L-1 (by script):
«R57» 2 (the premise, «RESULTS R57 (b)»), «R15» 1 («R15 G-N5T-1»); no other R-label. Each exists and carries the named item:
- R57 (l. 2893): (b) Lemma OUT-G's standing-premise sentence, l. 2915-2916 «Standing premise, as in R51 (d): OUT-G concerns SPEC's Ξσ and
  σ̄; that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance, and the code's match to SPEC is DATA (R15 G-N5T-1)
  (1E-N3 = N-1E-1).» L-1's quote is the middle clause, verbatim (by script). REFEREE §1 l. 19-22 reads «Optimal» as SPEC S1's own word.
- R15 (l. 624): limit (ii) «G-N1 = G-N5T-1 (DATA, code link)» (l. 645); signatures l. 668-669 («G-N1 = G-N5T-1 (DATA, both sides)»).
- SPEC (docs/new/N5-ssi-global.md): S1 (l. 25-46; σ̄, value order «better for Even», l. 30-32), S2 (l. 47, «Iτ the same on G^d for τ»),
  S4b (l. 54-55), S4c (l. 56-57), S4d (l. 58), FIX 3 (l. 88). Landed as premises before: e.g. RESULTS R68 «SPEC (S2, S4a, S4c with FIX
  3)»; «S4d» 3 times and «FIX 3» 18 times in RESULTS (by script). L-1 calls S4c, S4d, FIX 3 «SPEC text» (S4B-P1: «These are SPEC text,
  not premises.»).
- VJ00 §6: the opened source's algorithm section (Vöge-Jurdziński, BRICS RS-00-48; RESULTS R15 and R57 (a) cite it), inside R57 (b)'s
  words.
- Lead readings: L45 (G-2) and L42 (index «active (S4b part lifted by L45)»); L41 for «not referee-originated».
- Name check against landed text (RESULTS / GAPS at bd992a19 / e3d8fcc9; by script): «S4B-OPT», «S4B-KEEP», «H′_k», «τ_new,k»,
  «I_τ_k», «G*», «τ-stretch transition», «s4bopt», «L45», "### R102" and "R102" occur 0 times in both; «P-N5-S4B» once in RESULTS (the
  Erratum, about this line) and 0 in GAPS; «corpus_fixed.lst» once in RESULTS (the Erratum); «R2-N5-S4B» once in RESULTS (the Erratum);
  «σ*» 16 times in RESULTS and 3 in GAPS, other entries' bound letters; «S4b-OPT» 8 (G-5); «Odd fallback» 3 (G-5); «1E-N3» 74 / 10;
  «N-1E-1» 4 in RESULTS.
(7) SYMBOL TEST of the title (my own strict test of every symbol of L-1, by hand; IN = bound in the line; else the carrier):
| symbol | where |
| --- | --- |
| N5, SPEC S1-S5, «Even», «Odd», S1's procedure, SPEC S2, S4b, S4c, S4d, FIX 3 | SPEC (named) |
| R57, 1E-N3, R57 (b), σ̄, VJ00 §6 | cited; σ̄ inside the verbatim quote (G-4 (i)) |
| Lead reading L45, L42 | docs/DECISIONS.md (G-2) |
| G*, σ* | IN («for every finite game graph G* … and every Even strategy σ* of G*») |
| G, G^d | not glossed (G-4 (ii)); G^d is SPEC S1's dual («Odd's side: everything on the DUAL game G^d») |
| run, states (σ_k, τ_k), k | IN («a run is the sequence of states (σ_k, τ_k)»; k «at state k») |
| Iσ_k, I_τ_k | IN («N5's Even and Odd improving edges at state k (SPEC S2, the latter on G^d)»; D-1) |
| H′_k, v, w | IN («for a state k with I_τ_k ≠ ∅, H′_k is SPEC S4b's arena at k (…)»); v, w the arena gloss's own letters |
| τ_new,k | IN («SPEC S4b's output at k») |
| val, σ, ρ, x, ⊴ | IN («val(σ, ρ)(x) is the SPEC S1 value of the (σ, ρ)-play from x and ⊴ is SPEC S1's order (better for Even)») |
| Odd fallback, τ-stretch transition | IN |
| S4B-OPT: k, ρ, x | IN («for every state k of every N5 run with I_τ_k ≠ ∅, every positional Odd strategy ρ of H′_k and every vertex x») |
| S4B-KEEP: k | IN («at every τ-stretch transition k → k + 1 with I_τ_k ≠ ∅») |
| «pointwise optimum», «pointwise-optimal» | not defined in the line (G-4 (iii)) |
| tail: R15 G-N5T-1, file paths, l-si 9521f2e7…, lcount2_n23, sym_h8_s1 | cited; files by path (Data) |
Agreeing tests: REFEREE §5 l. 111-112, §C l. 151; REFEREE-2 §5 l. 92-94. Neither lists σ̄, G or «pointwise optimum» (G-4).
DOUBTS for CHECKER (no referee raised any as REQUIRED; no change proposed by me):
D-1 «Iσ_k» beside «I_τ_k» (packet §1 l. 27); SPEC writes Iσ, Iτ (l. 47). A notational asymmetry, no ambiguity.
D-2 «(SPEC text S4c, S4d, FIX 3)»: FIX 3 is text of the SPEC file (l. 88 «FIX 3 (S4c, A7). In a fallback iteration with Iσ ≠ ∅ only σ
  changes (τ_new = τ); n5.py l. 61-62. Odd falls back only if Iσ = ∅.»), not an S-label; as in landed premises (R68).
D-3 The DATA clause's mutation control: check.sh pins only lcount2_n23's (l. 1184-1185, «OPTV 215 »); sym_h8_s1's 677 (packet §4 l. 65)
  has no check.sh block, and anc58/inst/sym_h8_s1_default.start (sha1 c71d5a46b8e73b8219be41bca1e67d15eb042006) is in no sha1 pin list
  (box 62 pins sym_h8_s1.pg only, l. 1170). My re-run from the 96fb62cb archive: MUT=1 «OPTV 677», unmutated «OPTV 0» (Data). The
  clause gives no number, so it is not wider than the record.
D-4 The packet's §1 [S4b] quote (l. 23-24) writes «H′» (U+2032) where SPEC l. 54-55 has «H'» (ASCII); otherwise verbatim. Not in L-1.
D-5 Fixes entry 2 l. 26-28 quotes REFEREE §5 ending «The same change applies to the packet's §4.»; REFEREE l. 109 reads «The same change
  applies to the packet's §4 (fixes file).» (two words dropped without an ellipsis). The other 18 REFEREE / REFEREE-2 / RESULTS quote
  parts of the fixes file are found verbatim (scratch fxq102.py; the remaining 5 parts quote L-1, the packet or check.sh).
D-6 REFEREE-2 L1 l. 13 writes «; scope signed by REFEREE-2,» for the frozen line's «; scope as signed by REFEREE-2,»; its item 2 is
  otherwise right, and REFEREE §C l. 139 quotes it correctly.
D-7 REFEREE-2's report (1b9ef2e1) §4 l. 68 says «1,132 games» and its table l. 74-78 has the with-repeats counts; REFEREE §C l. 155-156
  notes the same for REFEREE-2's §2 (a) (its l. 31): «It is a DATA count in a report, not a signed item.» Not in L-1; the Erratum E-1 class.
D-8 The packet header l. 2 quotes the Lead at «02:24Z» while the freeze commit 68fa3661 is 02:23:22Z; I did not find the Lead's message
  in the repository (not verified).
(8) FIXES AND STATUS NOTES (fixes file at 96fb62cb, sha1 833ccf57d9d246b07e6d11a99257a32ae2c86412, 60 lines, the file's only commit; =
l-si head = trunk; recorded under Fixes): F0 and entries 1-5, one commit 96fb62cb (2026-11-01T04:12:28Z, with L-1 and the check.sh L-1
block), author L-SI successor 38 (l. 2 «L-SI successor 38. Started 2026-11-01 from 04:1xZ (date -u; see commit), after the Lead's 04:13Z
message.»; the minute is unfilled and «04:13Z» is after the commit's 04:12:28Z, a note). REFEREE §C l. 132-147 checks the five changes
item by item; REFEREE-2 L1 l. 6-18 checks the token diff.
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-1 states no CONJECTURE. A line-11 UPDATE is proposed at the end, to go AFTER R101's UPDATE
(GAPS at e3d8fcc9: the last UPDATE on l. 11 is R101's «UPDATE 2026-11-01 05:28Z: RESULTS R101 (P-N5-GATE; CHECKER C111 d53e1d4f)
[refereed-only] LANDED: …», ending «G-N5-TIME stays open.» before the row's closing « |»; l. 11 holds 76 "|" and 36 «UPDATE 2026-»), as a
pure insertion with one separating space. Built by script (scratch upd102.py: upd100L3.py's build() unchanged, read from that file).
L-1 has no " (date) — " and no source parenthesis, so build()'s tail rule cannot take it: the LABEL MOVE is build()'s, run on L-1's claim
body (labels searched after the binder's colon «a τ-stretch transition is a transition k → k + 1 with τ_(k+1) = τ_k: »), and the TAIL
RULE is R94's-R101's without a date and a source parenthesis: « — » → «: » (as " (date) — " → «: »); the tail kept in order, minus «;
G-N5-TIME stays open» and «; not M3, not a step-4 pass, not a TARGET.md claim»; closed by «. G-N5-TIME stays open.». The tail keeps the
lane-authored / L41 clause, «it bounds no count» and the DATA clause, as R97's and R98's landed UPDATEs keep their DATA. CONTROLS (same
script, same run): R97's, R98's, R99's, R100's and R101's LANDED UPDATEs (GAPS l. 11 at e3d8fcc9) from SRC L-5 (l-red a5340f2d), ODD L-3
(l-si 2f8e5b2e), STAIR L-3 (l-new 7dc1eb7c), ROOT L-3 (l-new 4cac9dc5) and GATE L-1 (l-new afb8b99e), byte for byte (True ×5; 4,179,
4,260, 4,870, 4,768 and 3,692 bytes). L-1 holds no "|", so no replacement is made. Checked by script: one line, 0 "|", one «<HH:MM>», one
«<checker>», 2,739 bytes, 448 tokens. Head «UPDATE 2026-11-01 <HH:MM>Z: RESULTS R102 (P-N5-S4B; CHECKER C113 <checker>) [refereed-only] »
(«P-N5-S4B» 0 times in GAPS; once in RESULTS, the erratum about this line); <HH:MM> and <checker> are filled at landing (if R102 lands
after 2026-11-01, the date is corrected).
(10) DATA of record = L-1's DATA clause = fixes entry 2 l. 31-35, superseding packet §4 l. 61-64 (fixes l. 38-39). Re-summed for this
draft (python3 -I, scratch sum102.py over the stored experiments/si/anc58/s4bopt_corpus.txt in the git archive of 96fb62cb, 1,132 rows,
keeping the first row of each distinct argument line, as check.sh's L-1 block does; 2026-11-01 06:25:01Z by date -u, rc 0): distinct 813
rows, STATES 5,726, CHECKED 5,058, SKIPPED 668, RHOS 213,311, OPTV 0, TAUNEW_EQ_RUN 5,697, ODDFB 29, S4ACHK 11,326, S4AV 0 (= fixes l.
31-35, = L-1); with repeats 1,132 rows, 7,772 / 6,719 / 1,053 / 290,345 / 0 / 7,736 / 36 / 16,430 / 0 (= packet §4 l. 61-64, = check.sh
box 63 l. 1188). No signed statement uses any count.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-4 to D-8 above; and (i) REFEREE §4 l. 72 uses CAP = 4,096 (ENUM 5,166
states, 490 over CAP) and the lane CAP 1,024, so REFEREE's ENUM counts are not the line's; its per-line comparison (l. 78-81) is of states
and fallbacks, and its distinct-line totals (l. 80) are read from the lane's file. (ii) REFEREE's and REFEREE-2's mutation units are
(state, ρ) pairs, the lane's (state, ρ, vertex) triples (REFEREE l. 90-91; REFEREE-2 l. 84). (iii) REFEREE ran 811 of the 813 distinct
lines (l. 75-76, «2 lines of gate_K64_n581, n 581 > MAXN»); REFEREE-2 ran all 813 (L1 l. 23). (iv) REFEREE-2 L1 l. 3 «376 → 432 words»;
my whitespace tokens 391 → 448 ((2)); the same changes.
(12) Excluded: L-SI boxes 59-62 and the working note docs/si/N5-S4B-box63.md; the packet's §5 pre-check; O-ARENA and any use of
S4B-KEEP in other packets (L45's effect sentence: own review needed); REFEREE's and REFEREE-2's tools (docs/referee/scratch/s4b_probe.py,
s4b_logs/; docs/referee-2/R2-N5-S4B/s4b_check.py, logs/). Not part of this entry.
(13) Commits: lane (claude/l-si): 9521f2e7 (2026-11-01T01:37:42Z; box 63, s4bopt.py, s4bopt_corpus.txt, check.sh box 63 block) →
68fa3661 (02:23:22Z; freeze: packet +81, frozen line +1, check.sh «P-N5-S4B pinned») → 96fb62cb (04:12:28Z; fixes F0 + entries 1-5 +60,
L-1 +1, check.sh L-1 block). REFEREE on claude/referee: 062cd734 (03:19:48Z; successor 22's report, new file 129 lines, sha1
43fe325df2a0abeeaa6e3f2923dd7ac4b402fb9c; scratch/s4b_probe.py, s4b_logs/) → 2e6467fd (05:03:24Z; §C on L-1, +28/−0; the file now 157
lines, sha1 285d860f9df68b82d7ae0cd9ca539b15ae182334). REFEREE-2 on claude/referee-2: 1b9ef2e1 (02:53:38Z; report, new file 107 lines,
sha1 b0c42cc8beb12782822d2d2d2aff053c11ca0dd3; R2-N5-S4B/ tool and logs) → 0e8ae566 (05:04:43Z; R2-N5-S4B-L1.md, new file 42 lines).
Lead: 322922ec (04:10:34Z; L45). Trunk merges that brought each in (the first first-parent trunk commit containing it; scratch
firsttrunk.py): 9521f2e7 → 83d99f04 (02:21:17Z); 68fa3661 → d734f419 (02:50:19Z); 1b9ef2e1 → e7c0e191 (03:44:26Z); 062cd734 → 2c497bba
(04:10:15Z); 96fb62cb → cfde8a92 (05:02:35Z); 0e8ae566 → d9906071 (05:28:33Z); 2e6467fd → NOT on trunk at this fill.
(14) Placement: see (0). No Dead-ends row: L-1 states no DEAD and kills no conjecture of RESULTS or GAPS.
### R102 [refereed-only] N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance», RESULTS R57 (b)), read on every game input of S1's procedure (Lead reading L45, lifting L42's S4b restriction): for every finite game graph G* with G's priorities and a successor at every vertex and every Even strategy σ* of G*, the Odd strategy that S1's procedure outputs for σ* on G* is a pointwise optimum against σ* in G* (the setting of VJ00 and of S1 as in docs/referee-2/R2-N5-1E.md §2, note N-1E-1: «every finite game graph with a successor at each vertex … no class hypothesis», confirmed for arena inputs in docs/referee-2/R2-N5-S4B.md §2)), with: a run is the sequence of states (σ_k, τ_k); Iσ_k and I_τ_k are N5's Even and Odd improving edges at state k (SPEC S2, the latter on G^d); for a state k with I_τ_k ≠ ∅, H′_k is SPEC S4b's arena at k (Odd v keeps the edges to {τ_k(v)} ∪ {w : (v, w) ∈ I_τ_k}, Even v keeps the edge to σ_k(v), priorities of G) and τ_new,k is SPEC S4b's output at k; val(σ, ρ)(x) is the SPEC S1 value of the (σ, ρ)-play from x and ⊴ is SPEC S1's order (better for Even); an Odd fallback is a SPEC S4c iteration with Iσ_k = ∅; a τ-stretch transition is a transition k → k + 1 with τ_(k+1) = τ_k: (Lemma S4B-OPT) for every state k of every N5 run with I_τ_k ≠ ∅, every positional Odd strategy ρ of H′_k and every vertex x, val(σ_k, τ_new,k)(x) ⊴ val(σ_k, ρ)(x), and τ_(k+1) = τ_new,k unless k → k + 1 is an Odd fallback (SPEC text S4c, S4d, FIX 3); (Corollary S4B-KEEP) at every τ-stretch transition k → k + 1 with I_τ_k ≠ ∅, τ_k = τ_new,k, so τ_k is a pointwise-optimal Odd strategy of H′_k against σ_k (2026-11-01) — a premise result under 1E-N3 only, lane-authored (L-SI; not referee-originated): the correctness of S1's procedure (VJ00 §6) stays SPEC's requirement and the code's conformance stays DATA (R15 G-N5T-1); it bounds no count; G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim; DATA, not part of the claim: an enumeration of every positional Odd strategy of H′_k found no violation at the 5,058 states with at most 1,024 such strategies among the 5,726 states with I_τ_k ≠ ∅ of the 813 distinct game/start lines of experiments/si/anc58/corpus_fixed.lst (a list of 1,132 lines with 319 exact repeats; counts de-duplicated; 668 states not enumerated), and a mutation control (τ_k in place of τ_new,k) is detected on experiments/red/h3/instances/lcount2_n23 and experiments/red/n5/instances/sym_h8_s1 (experiments/si/anc58/s4bopt.py, l-si 9521f2e72bf049e71de7eadec7853d99227b9dc7), CHECKER PASS (docs/checker/C113.md, checker PENDING)
- Object (L-SI successor 38, Opus 5.5, D18; frozen, unchanged during review): packet P-N5-S4B (L-SI box 63), docs/si/P-N5-S4B-box63.md,
  sha1 f1b65da522d927406a403ae5d023bb48ac73d022, 81 lines (l-si freeze 68fa3661, 2026-11-01T02:23:22Z, the file's only commit; identical
  at 96fb62cb, at the l-si head and at trunk; first on trunk by merge d734f419, 02:50:19Z). Both referees measured the sha1 at 68fa3661
  (REFEREE l. 2 «docs/si/P-N5-S4B-box63.md (sha1 f1b65da5…, 81»; REFEREE-2 §0 l. 6 «Re-hashed: match.»). Title (l. 1): «S4b's new τ is
  Odd's pointwise optimum against σ in S4b's arena, under R57's standing premise 1E-N3 alone. So a τ kept at a τ-stretch transition is
  that optimum. A premise result: it bounds no count». Status (l. 5-6): «Status: lane-authored (L-SI), not referee-originated (L41 does
  not apply). No count is bounded. G-N5-TIME stays OPEN. Not M3, not a», «step-4 pass, not a TARGET.md claim.» To sign (l. 9-14): §2
  Lemma S4B-OPT and §3 Corollary S4B-KEEP «PROVED (to sign)»; §4 «DATA, NOT to sign». Sections: §1 setting and premises (l. 16-30), §2
  Lemma S4B-OPT with its proof (i)-(iv) and a Remark (l. 32-46), §3 Corollary S4B-KEEP (l. 48-53), §4 DATA (l. 55-71), §5 the RESULTS line
  draft and the drafter's pre-check (l. 73-81).
  The RESULTS line, history: (1) the frozen line docs/si/P-N5-S4B-line.txt (sha1 f8559b5e…, committed with the packet), the line both
  reports reviewed: REFEREE 22 REQUIRED S4B-L1 and S4B-L2 (table l. 14, §5 l. 97-109); REFEREE-2 25 MATCHES with optional P-1 (§5 l.
  95). At the frozen line the premise read «under the standing SPEC premise of RESULTS R57 (1E-N3: for every finite game graph G* …;
  scope as signed by REFEREE-2, docs/referee-2/R2-N5-1E.md §2, note N-1E-1: …)», which REFEREE found states «a quantified form R57 does
  not state» while L42 was active (§5 l. 98-101), and the DATA clause counted the 1,132-line list with its 319 repeats (§5 l. 105-107).
  (2) L-1 95373010d54c69907308d224fa1111127055b8f5 (docs/si/P-N5-S4B-line-L1.txt, l-si 96fb62cb, 2026-11-01T04:12:28Z, the file's only
  commit; first on trunk by merge cfde8a92, 05:02:35Z; fixes F0 + entries 1-5) = the frozen line with exactly five changes (word diff by
  script; to check (2)): R57 (b)'s words quoted and the G*-form introduced by Lead reading L45 (S4B-L1); N-1E-1 cited as «the setting of
  VJ00 and of S1» (S4B-L1); «confirmed for arena inputs in docs/referee-2/R2-N5-S4B.md §2» (REFEREE-2 P-1); «SPEC text S4c, S4d, FIX 3»
  (S4B-P1); the DATA counts de-duplicated (S4B-L2). REFEREE 22 L-1: §C (2e6467fd) l. 134 «Five changes, the ones the Lead listed. Nothing
  else changed:», l. 157 «Verdict: line L-1 **MATCHES**. S4B-L1 and S4B-L2 are met.» REFEREE-2 25 L-1: R2-N5-S4B-L1.md (0e8ae566) l. 18
  «Nothing else changed. The Lemma and Corollary statements, the binder and the scope tail are token-identical.», l. 34 «**MATCHES** (Opus
  5.5, D15). Nothing REQUIRED.»
  L-1 supersedes the frozen line; the title is L-1 verbatim with the date « (2026-11-01)» inserted before « — a premise result» (Lead decision G-1; to check (1)). Neither referee found a FALSE claim statement in the packet;
  every line item re-attributes the premise, adds a citation or a word, or corrects the DATA counts.
  Setting (packet §1, l. 16-30): N5 = SPEC S1-S5 (l. 7 «Object: N5 only (SPEC S1-S5, docs/new/N5-ssi-global.md, with Q1-Q4 and FIX
  1-4).»); [1E-N3] (l. 17-22) in the form «for every finite game graph G* (the priorities of G, a successor at every vertex) and every
  Even strategy σ* of G*, the Odd strategy ρ* that S1's procedure outputs for σ* on G* satisfies val(σ*, ρ*)(x) ⊴ val(σ*, ρ)(x) for
  every positional Odd strategy ρ of G* and every vertex x.»; [S4b] (l. 23-24); [S4c / S4d / FIX 3] (l. 25-26); notation (l. 27-30):
  runs, Iσ_k and I_τ_k, H′_k and τ_new,k «For a state k with I_τ_k ≠ ∅», val, ⊴, «An Odd fallback is an S4c iteration with Iσ_k = ∅.»,
  «A τ-stretch transition is a transition k → k + 1 with τ_(k+1) = τ_k.» L-1's notation is the packet's, with H′_k written out.
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 22 (report 062cd734, §C on L-1 2e6467fd); REFEREE-2 successor 25
  (report 1b9ef2e1, R2-N5-S4B-L1.md 0e8ae566)). Items (a)-(b) are SIGNED in both verdict tables (REFEREE "## 0. Verdicts" l. 7-14 of
  R-N5-S4B.md; REFEREE-2 "## 1. Claims table" l. 14-18 of R2-N5-S4B.md); the table is to-check (4). Both hold for every N5 run on every
  game. Premise: RESULTS R57 (b)'s standing SPEC premise 1E-N3, read on every game input of S1's procedure by Lead reading L45 (below);
  SPEC S1, S2, S4b, S4c, S4d and FIX 3 are SPEC text, not premises (S4B-P1). The code's match to SPEC is DATA (R15 G-N5T-1). No item
  bounds a count.
  (a) Lemma S4B-OPT (§2, l. 32-46): statement (l. 33-34) «For every state k of every N5 run with I_τ_k ≠ ∅, every positional Odd strategy
      ρ of H′_k and every vertex x:», «val(σ_k, τ_new,k)(x) ⊴ val(σ_k, ρ)(x). Moreover τ_(k+1) = τ_new,k unless k → k + 1 is an Odd
      fallback.»; proof (l. 36-43): (i) H′_k is a finite game graph with G's priorities and a successor at every vertex; (ii) «[1E-N3] with
      G* := H′_k and σ* := σ_k»; (iii) «A value depends only on the play and the priorities (SPEC S1).»; (iv) S4d, S4c and FIX 3. Cells:
      REFEREE «**SIGNED** (precision S4B-P1)» (l. 10; §2 l. 45-57; l. 47 «(ii) ✓. By §1 this is 1E-N3 on (H′_k, σ_k).»); REFEREE-2
      «**SIGNED**» (l. 17; §3 l. 51-57; l. 52 «§2 (ii) is 1E-N3 with G* := H′_k, σ* := σ_k. ✓»).
  (b) Corollary S4B-KEEP (§3, l. 48-53): statement (l. 49-50) «At every τ-stretch transition k → k + 1 with I_τ_k ≠ ∅: τ_k = τ_new,k.
      Hence τ_k is a pointwise-optimal Odd strategy of», «H′_k against σ_k.»; proof (l. 51-52): an Odd fallback changes τ (S4c, with
      SPEC S2's «w ≠ σ(v)» read on G^d, S4B-P2), so it is not a τ-stretch transition, and (a) applies; l. 53 «(If I_τ_k = ∅, S4b does
      not run and H′_k is not defined; the statement is about I_τ_k ≠ ∅ only.)» Cells: REFEREE «**SIGNED** (precision S4B-P2)» (l. 11;
      §3 l. 59-62, l. 61 «So τ_(k+1) ≠ τ_k, and an Odd fallback is never a τ-stretch transition. §2 then gives τ_k = τ_(k+1) =
      τ_new,k.»); REFEREE-2 «**SIGNED**» (l. 18; §3 l. 58-60).
  The RESULTS line (L-1) states both claims as signed and nothing more; its tail states the premise status, L41's «not
  referee-originated», the scope words and a DATA clause «not part of the claim» (to check (4), (7)).
- Premise 1E-N3 on S4b's arena, and Lead reading L45. R57 (b) (RESULTS l. 2915-2916): «that S1's procedure realises an optimal σ̄ is
  VJ00 §6 plus SPEC conformance, and the code's match to SPEC is DATA (R15 G-N5T-1) (1E-N3 = N-1E-1).» REFEREE §1 (l. 18-39, «The key
  check»): l. 31-32 «H′_k is a valid input: the same V, Ω and owners as G, E′ ⊆ E, and every vertex has a successor (σ_k(v) for Even v,
  τ_k(v) ∈ A(v) for Odd v). It is a parity game in SPEC's sense.», l. 33 «So S4b's call is an instance of 1E-N3, the premise about S1's
  procedure on a game input. It is no further from G than S4a's call.», l. 37-39 «Conclusion: the restriction in L42 («covers S1's
  procedure and S4a … does NOT cover S4b») cannot be derived from 1E-N3's wording or SPEC. It recorded which instances had been named.»,
  «Recording this as a Lead reading is the Lead's decision. My finding supports it.» REFEREE-2 §2 (l. 22-48): l. 23 «**(a) Does SPEC S4b
  run exactly S1's procedure on H′?** Yes.», l. 37-38 «The second item, 1E-N3, is a requirement on the procedure for its input graph.
  VJ00 §6's algorithm is stated in that same setting, so it covers any finite game graph with a successor at each vertex.», l. 47-48 «So
  lifting L42's S4b restriction by a Lead reading is consistent with my signature. The premise used is 1E-N3 applied to H′_k, exactly as
  it is applied to S4a's dual arena.» The Lead then recorded Lead reading L45 (docs/DECISIONS.md l. 383-390, 2026-11-01 04:10Z):
  «S4b is covered by R57's 1E-N3. L42's restriction («R57 covers S1 and S4a only; [S4b-OPT] not covered») is LIFTED for S4b: S4b runs
  S1's procedure on the restricted game H′_k (same V, Ω, owners; E′ ⊆ E; a successor at every vertex; «S1 procedure on H', not dual»),
  which is an input of the kind 1E-N3 / N-1E-1 speaks of (R57 (b): «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC
  conformance»).», with its grounds «P-N5-S4B (l-si 68fa36619) Lemma S4B-OPT and Corollary S4B-KEEP, SIGNED by REFEREE (062cd734) and
  REFEREE-2 (1b9ef2e1), both stating that 1E-N3 covers S4b and that the lift is consistent with their signatures.» and «L42 stays in
  force for any premise other than S1's procedure on a valid input.» L42 (l. 362-367) is now indexed «active (S4b part lifted by L45)»
  (docs/DECISIONS-INDEX.md l. 35). L-1 cites both as on file (draft G-2). The lift is a Lead reading, not a signed statement; the
  signatures are of S4B-OPT and S4B-KEEP under 1E-N3, and each referee's report states that the lift is consistent with it (above).
  Effect recorded in L45 (not part of this entry): «lemmas that used [S4b-OPT] / [S4b-KEEP] (e.g. O-ARENA, withdrawn from P-N5-STAIR under
  L42) are as conditional as every landed N5 result, i.e. on R57's SPEC premise only; they still need their own referee review to land.»
  R99's body (l. 8649, l. 8751-8758) records [S4b-OPT] as «NOT covered» under L42 at R99's landing; R102 does not edit it (draft G-2).
- L41: not applicable. The proofs are the packet's own (L-SI successor 38); packet l. 5 «Status: lane-authored (L-SI), not
  referee-originated (L41 does not apply).»; L-1 «lane-authored (L-SI; not referee-originated)». REFEREE §5 l. 115 «L41:
  «lane-authored (L-SI; not referee-originated)». L43: no DEAD.»; REFEREE-2 §5 l. 91 «No DEAD (L43). No referee-originated proof
  (L41).» The coverage reading of 1E-N3 for arena inputs is confirmed by both referees (above) and recorded by the Lead as L45; L-1 names
  REFEREE-2's confirmation by file and section.
- Fixes (docs/si/P-N5-S4B-fixes.md, L-SI successor 38, append-only, F0 and entries 1-5, one commit 96fb62cb (2026-11-01T04:12:28Z, new
  file, 60 lines, sha1 833ccf57d9d246b07e6d11a99257a32ae2c86412; = l-si head = trunk)). Header (l. 1): «the frozen packet
  docs/si/P-N5-S4B-box63.md, sha1 f1b65da522d927406a403ae5d023bb48ac73d022, is never edited». Each entry:
  - F0 (l. 4-13): both referees' signatures quoted (l. 6-10); L45 (l. 11); «Changes: the RESULTS line only (line L-1, entries 1-2).
    Entries 3-5 record the optional precisions. The packet's §4 counts are» «superseded by entry 2.» (l. 12-13).
  - Entry 1 (l. 15-23), S4B-L1 (REQUIRED): R57 (b) quoted verbatim, «read on every game input of S1's procedure (Lead reading L45,
    lifting L42's S4b restriction)», N-1E-1 «now as the setting of VJ00 and of S1 rather than as REFEREE-2's signed scope of R57» (l.
    23).
  - Entry 2 (l. 25-39), S4B-L2 (REQUIRED): the distinct counts re-derived from the lane's own output (l. 29-36), «These agree with
    REFEREE's figures.» (l. 36); the packet's §4 counts superseded (l. 38-39); «The mutation-control figures (lcount2_n23 215, sym_h8_s1
    677) are per instance and unaffected.» (l. 39).
  - Entry 3 (l. 41-45), S4B-P1: «Accepted.»; «The only premise is 1E-N3.» (l. 44-45); L-1 «SPEC text S4c, S4d, FIX 3».
  - Entry 4 (l. 47-50), S4B-P2: «Accepted.»; no line change.
  - Entry 5 (l. 52-56), REFEREE-2 P-1: «Accepted. Line L-1 adds «confirmed for arena inputs in docs/referee-2/R2-N5-S4B.md §2».» (l. 56).
  No fix changes a signed statement: entries 1, 3, 5 re-word the premise citation, entry 2 corrects DATA counts, entry 4 is a proof-text
  citation (REFEREE §C l. 134-147; REFEREE-2 L1 l. 6-18).
- Not signed: §1 (premises and notation); §4 DATA (packet l. 14 «DATA, NOT to sign»); the Remark (no dual) (REFEREE-2 l. 61). L-1's
  DATA clause is marked «DATA, not part of the claim». OPEN, not claimed: any bound on N5's iteration count; G-N5-TIME.
- Referee strengthening (NOT part of this entry; remarks of one referee):
  (i) REFEREE §2 l. 47-48 «Note that 1E-N3 gives pointwise optimality against positional Odd strategies by SPEC S1's definition of
       «optimal» alone; (VJ) (R57 (a)) is not needed for the form the packet uses.»
  (ii) REFEREE §1 l. 33-36: S4b's call is closer to 1E-N3 than S4a's, which calls S1 on the DUAL of a restricted arena («S4b's call needs
       neither the dual nor the read-back to G.»); REFEREE-2 §2 l. 40-41 the same comparison.
  (iii) Own-engine checks beyond the lane's: REFEREE's LOC one-switch deviation test at every state, uncapped («LOC (32,469
       deviations)», §4 l. 76), and ENUM at CAP = 4,096; REFEREE-2's KEEP checks («KEEP 2,976», L1 l. 29).
- Honest limits: (i) A premise result: it bounds no count; G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim. (ii)
  It rests on R57 (b)'s standing premise 1E-N3 (S1's procedure realises an optimal counterstrategy, VJ00 §6 plus SPEC conformance), read
  on S4b's arena inputs by Lead reading L45; the correctness of S1's procedure stays SPEC's requirement, as for every landed N5 result.
  (iii) The code's conformance to SPEC is DATA (R15 G-N5T-1); the corpus check tests the code (n5x / si.py), not SPEC (packet §4 l. 71).
  (iv) The DATA enumeration covers only states whose arena has at most 1,024 Odd strategies (5,058 of 5,726; 668 not enumerated). (v)
  L45 lifts L42 only for S1's procedure on a valid input; every other premise stays under L42, and lemmas that used [S4b-OPT] /
  [S4b-KEEP] elsewhere (e.g. O-ARENA) still need their own referee review. (vi) The title's date « (2026-11-01)» is Lead-inserted (G-1 decision); the title has no source note.
- Data (DATA, not proof): pinned. experiments/si/check.sh at 96fb62cb (the L-1 commit): sha1 e49cf25efed32a5042efeff796ec9634f0aa5ef2, 1,206
  lines (= trunk); the box 63 block is l. 1181-1189 (added by 9521f2e7), the «P-N5-S4B pinned» block l. 1190-1193 (added by 68fa3661: the
  packet's and the frozen line's sha1), the L-1 block l. 1194-1206 (added by 96fb62cb: L-1's sha1 and the distinct-line counts). Re-run
  for this draft from a `git archive` of 96fb62cb3 (experiments/ and docs/si/; from experiments/si; GIT_DIR set to the repository), l.
  1-6 (shebang, set -euo pipefail, cd) plus l. 1181-1206, 2026-11-01 06:24:49Z by date -u (start and end in the same second), rc 0;
  output: «si (box 63: S4B-OPT): PASS»; «si (P-N5-S4B pinned): PASS»; «si (P-N5-S4B L-1 pinned, distinct counts): PASS». The box 63 block
  greps «STATES 6 CHECKED 6 SKIPPED 0 RHOS 46 OPTV 0 TAUNEW_EQ_RUN 6 » and «S4AV 0» on lcount2_n23 with its start, «OPTV 215 » under
  MUT=1, 1,132 corpus rows and the with-repeats totals «7772 6719 0 36 7736»; the L-1 block requires «813 5726 5058 668 213311 0 29 0».
  Supporting run (the DATA clause's second mutation instance; no check.sh block, D-3), same archive, 06:26:26Z, rc 0: MUT=1 «S4BOPT
  sym_h8_s1.pg STATES 25 CHECKED 25 SKIPPED 0 RHOS 302 OPTV 677 TAUNEW_EQ_RUN 9 ODDFB 0 S4ACHK 19 S4AV 0»; unmutated «OPTV 0
  TAUNEW_EQ_RUN 25». Pin files (sha1 at 96fb62cb = trunk): lcount2_n23.pg dd9847c6b19cb9f44af73bcc23de7ca2aca9a14c, lcount2_n23.start
  7d3626aa4a6a80d59878fa442886473505390c17, sym_h8_s1.pg f87fee647f1c8b57f3466c0b68e7e284e3d559d3 (box 62's pin list, l. 1166-1170);
  sym_h8_s1_default.start c71d5a46b8e73b8219be41bca1e67d15eb042006 (not pinned, D-3); corpus_fixed.lst
  d6ed7557a39952563858a8fd402c55b431cd68e2 (1,132 lines, 813 distinct, 719 distinct .pg, 319 repeated lines; by sort / uniq).
  DATA OF RECORD (L-1; fixes entry 2 l. 31-35): 813 distinct game/start lines; 5,726 states with I_τ ≠ ∅; 5,058 enumerated, 668 not
  enumerated; 213,311 strategies compared, OPTV 0; τ_(k+1) = τ_new at 5,697 states, 29 Odd fallbacks; S4a control 11,326 states, S4AV 0.
  Re-summed: equal (to check (10)). With repeats (the packet's §4, superseded): 7,772 / 6,719 / 1,053 / 290,345 / 36 / 16,430.
  REFEREE (successor 22; own docs/referee/scratch/s4b_probe.py, «own engine rl_engine; no lane code», l. 65): «The list has 1,132 lines,
  but only **813 distinct** «pg [start]» lines (319 exact repeats; 719 distinct .pg files).» (l. 75); «I found **0 violations**: NEXT,
  ODDFB, KEEP, LOC (32,469 deviations) and ENUM (5,166» «states, 576,663 strategies; 490 states over CAP).» (l. 76-77); «Per line, my
  counts equal the lane's» (l. 78); own run errors corrected before comparison (l. 82-87, 92-95).
  REFEREE-2 (successor 25; own docs/referee-2/R2-N5-S4B/s4b_check.py, «The lane's anc58/s4bopt.py is not imported.», l. 67): report §4
  (with repeats; l. 72-79) «RESULT PASS, 0 violations, in all four.» (l. 70); L1 (de-duplicated; l. 20-31) «My s4b_check.py on the 813
  distinct lines» (l. 23), table l. 25-29 («5,726 | 5,726», «5,058 / 668 | 5,058 / 668», «0 (213,311 strategies; 29 Odd fallbacks; KEEP
  2,976)»).
  No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-S4B.md: successor 22's report 062cd7345f29e6f6ab031934b11ec8b1b057665c (2026-11-01T03:19:48Z, new
  file, 129 lines, sha1 43fe325df2a0abeeaa6e3f2923dd7ac4b402fb9c, with docs/referee/scratch/s4b_probe.py and s4b_logs/; first on trunk by
  merge 2c497bba, 04:10:15Z): S4B-OPT and S4B-KEEP SIGNED, no gap, line REQUIRED S4B-L1 and S4B-L2; §C
  2e6467fd281e2ff898b733dfa506effeed75b29f (05:03:24Z, +28/−0, l. 130-157; the file now 157 lines, sha1
  285d860f9df68b82d7ae0cd9ca539b15ae182334, = referee head): «Verdict: line L-1 **MATCHES**. S4B-L1 and S4B-L2 are met.» (l. 157).
  2e6467fd is first on trunk by merge 3ad52bc6 (06:52:33Z). REFEREE-2 (successor 25): docs/referee-2/R2-N5-S4B.md
  1b9ef2e1017d9cf4aad53492a1dd259694ff265a (02:53:38Z, new file, 107 lines, sha1 b0c42cc8beb12782822d2d2d2aff053c11ca0dd3, unchanged since;
  with R2-N5-S4B/ tool and logs; on trunk by e7c0e191, 03:44:26Z): both SIGNED (l. 17-18, l. 100), line MATCHES (l. 95);
  R2-N5-S4B-L1.md 0e8ae566deb15706a581b29970fd5fb0297b2f97 (05:04:43Z, new file, 42 lines, sha1 2252e92e78dca736cf52844718b24bb05dd29754,
  = referee-2 head for this file; on trunk by d9906071, 05:28:33Z): «**MATCHES** (Opus 5.5, D15). Nothing REQUIRED.» (l. 34). Lane: freeze
  68fa366198cffba1329228fd74b4e857ea140501, L-1 and fixes 96fb62cb37200773fe1b5211843af7986c82337e.
  INDEPENDENCE: REFEREE l. 3 «Written before reading any REFEREE-2 report on this packet (none in my tree).»; §C l. 141 «Read now, after
  my report: R2-N5-S4B §2 (b) says this (its P-1), at referee-2 1b9ef2e1.» REFEREE-2 l. 3 «Independence: written without opening
  docs/referee/ for this packet.» REFEREE-2's report (02:53:38Z) precedes REFEREE's (03:19:48Z) by 26 minutes. Neither review imported lane
  code (REFEREE l. 65; REFEREE-2 l. 67).
  Differences, resolved: S4B-L1 and S4B-L2 found by REFEREE only (REFEREE-2 had MATCHED the frozen line); REFEREE-2 measured the repeats
  itself in L1 (l. 21-22) and reproduced L-1's counts. Both SIGN the same two items with no gap and both MATCH L-1. No disagreement in
  substance.
- TARGET.md diff: «N5 on EVERY game» = every TARGET.md §1 game («A parity game is G = (V, V_E, V_O, E, pr) with V finite»; «every vertex
  has at least one successor (self-loops allowed)»); G* and H′_k are such games on G's vertices (REFEREE §1 l. 31-32). The line (L-1)
  makes no M4 claim and no TARGET claim; its tail reads «it bounds no count; G-N5-TIME stays open; not M3, not a step-4 pass, not a
  TARGET.md claim» (L-1, by script). REFEREE §5 l. 117 «TARGET.md diff: no claim against §2 or §4. The result is a premise lemma, no
  polynomial bound, no unit-cost arithmetic.»; §C l. 154 «No DEAD (L43). TARGET.md diff ✓.»; REFEREE-2 §5 l. 88-89 «This is consistent
  with TARGET §2 and §4.» Not a claim of TARGET.md §1 or §2 (optimality of S4b's Odd step against σ in its arena, and its consequence at
  τ-stretch transitions; no bound on a run or on running time; no algorithm claim); not a step-4 pass. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER R101's UPDATE of G-N5-TIME (GAPS at e3d8fcc9, last changed by 110e380b: the last
UPDATE on l. 11 is R101's, «UPDATE 2026-11-01 05:28Z: RESULTS R101 (P-N5-GATE; CHECKER C111 d53e1d4f) …», before the row's closing « |»),
built by script (upd102.py: upd100L3.py's build() for the label move, labels searched after the binder; the tail rule of R94-R101 without
a date and a source parenthesis, to check (9)) only from the clauses of the title line L-1: labels behind their clauses; « — » → «: »;
«; G-N5-TIME stays open» and «; not M3, not a step-4 pass, not a TARGET.md claim» dropped from the tail; «. G-N5-TIME stays open.» at the
end. The same script reproduces R97's, R98's, R99's, R100's and R101's LANDED UPDATEs (GAPS l. 11) byte for byte. L-1 holds no "|"; the
UPDATE holds none and no replacement is made. Date «2026-11-01» (the landing date; corrected at landing if later); time and CHECKER commit
to be filled at landing:
UPDATE 2026-11-01 <HH:MM>Z: RESULTS R102 (P-N5-S4B; CHECKER C113 <checker>) [refereed-only] LANDED: N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance», RESULTS R57 (b)), read on every game input of S1's procedure (Lead reading L45, lifting L42's S4b restriction): for every finite game graph G* with G's priorities and a successor at every vertex and every Even strategy σ* of G*, the Odd strategy that S1's procedure outputs for σ* on G* is a pointwise optimum against σ* in G* (the setting of VJ00 and of S1 as in docs/referee-2/R2-N5-1E.md §2, note N-1E-1: «every finite game graph with a successor at each vertex … no class hypothesis», confirmed for arena inputs in docs/referee-2/R2-N5-S4B.md §2)), with: a run is the sequence of states (σ_k, τ_k); Iσ_k and I_τ_k are N5's Even and Odd improving edges at state k (SPEC S2, the latter on G^d); for a state k with I_τ_k ≠ ∅, H′_k is SPEC S4b's arena at k (Odd v keeps the edges to {τ_k(v)} ∪ {w : (v, w) ∈ I_τ_k}, Even v keeps the edge to σ_k(v), priorities of G) and τ_new,k is SPEC S4b's output at k; val(σ, ρ)(x) is the SPEC S1 value of the (σ, ρ)-play from x and ⊴ is SPEC S1's order (better for Even); an Odd fallback is a SPEC S4c iteration with Iσ_k = ∅; a τ-stretch transition is a transition k → k + 1 with τ_(k+1) = τ_k: for every state k of every N5 run with I_τ_k ≠ ∅, every positional Odd strategy ρ of H′_k and every vertex x, val(σ_k, τ_new,k)(x) ⊴ val(σ_k, ρ)(x), and τ_(k+1) = τ_new,k unless k → k + 1 is an Odd fallback (SPEC text S4c, S4d, FIX 3) (Lemma S4B-OPT); at every τ-stretch transition k → k + 1 with I_τ_k ≠ ∅, τ_k = τ_new,k, so τ_k is a pointwise-optimal Odd strategy of H′_k against σ_k (Corollary S4B-KEEP): a premise result under 1E-N3 only, lane-authored (L-SI; not referee-originated): the correctness of S1's procedure (VJ00 §6) stays SPEC's requirement and the code's conformance stays DATA (R15 G-N5T-1); it bounds no count; DATA, not part of the claim: an enumeration of every positional Odd strategy of H′_k found no violation at the 5,058 states with at most 1,024 such strategies among the 5,726 states with I_τ_k ≠ ∅ of the 813 distinct game/start lines of experiments/si/anc58/corpus_fixed.lst (a list of 1,132 lines with 319 exact repeats; counts de-duplicated; 668 states not enumerated), and a mutation control (τ_k in place of τ_new,k) is detected on experiments/red/h3/instances/lcount2_n23 and experiments/red/n5/instances/sym_h8_s1 (experiments/si/anc58/s4bopt.py, l-si 9521f2e72bf049e71de7eadec7853d99227b9dc7). G-N5-TIME stays open.

Addendum 1 (subagent, for the Lead; does not land; written 2026-11-01T06:35:47Z by date -u). (1) BUILT ON LINE L-1 (l-si 96fb62cb, sha1 95373010…),
the line both referees MATCH (REFEREE 22 2e6467fd; REFEREE-2 25 0e8ae566). NOT committed, NOT pushed; no other file edited. 2e6467fd is
on origin claude/referee only: merge it and push trunk before landing. (2) TITLE l. 283 = "### R102 [refereed-only] " + L-1
without its newline + ", CHECKER PASS (docs/checker/C113.md, checker PENDING)", checked by script after the fill (fill102.py): equal, byte
for byte (True); the only «### R» heading of this file. (3) BODY l. 283-444; GAPS preamble l. 446-453; UPDATE l. 454 (one
line, 0 "|", one <HH:MM>, one <checker>; controls True ×5: R97's-R101's landed UPDATEs). (4) PINS: from a git archive of 96fb62cb3
(experiments/, docs/si/), from experiments/si, GIT_DIR set: check.sh l. 1-6 + 1181-1206 (box 63, «P-N5-S4B pinned», L-1) 06:24:49Z, rc
0, three PASS lines; MUT=1 / unmutated s4bopt.py on sym_h8_s1 06:26:26Z, rc 0 (677 / 0); DATA re-sum 06:25:01Z, rc 0 (813 distinct
rows: 5,726 / 5,058 / 668 / 213,311 / 0 / 5,697 / 29 / 11,326 / 0). (5) QUOTE SWEEP: q102.py (q101.py's rule: outermost guillemet quotes, whitespace joined, split at the ellipsis, parts of 6+ characters; sources: packet at 68fa3661, frozen line, L-1, fixes, R-N5-S4B.md at 2e6467fd, R2-N5-S4B.md at 1b9ef2e1, R2-N5-S4B-L1.md at 0e8ae566, R2-N5-1E.md, RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, TARGET.md, SPEC, P-N5-STAIR-box112.md, NOW, C109-C111, check.sh at 96fb62cb, my pin / mutation / re-sum outputs, my UPDATE and word diff, commit subjects): to-check notes l. 1-282: 246 quotes, 200 parts, all found; entry (title + body) l. 283-444: 111 quotes, 114 parts, all found, none found only in my own outputs or commit subjects; GAPS preamble and UPDATE l. 446-454: 10 quotes, 8 parts, all found; this Addendum: 6 quotes, 5 parts, all found. Found only in my own UPDATE (by design): the UPDATE head (to-check (9)). My own wordings and patterns are in double quotes, not guillemets. Line check: 108 quotes preceded by an l. N, 6 heuristic misses, read by hand: four verdict-table cells (the regex takes the packet's line range before a referee cell), REFEREE's l. 155-156 note after "its l. 31", and REFEREE l. 75 after "l. 65"; none a wrong line. (6) FLAGS FOR CHECKER IN L-1 (no referee
made any REQUIRED): G-1 no date and no source note in the title; G-2 L45 stated accurately (CLEAN), with R99's L42-era body sentences
noted; G-3 first Lead reading / «lane-authored» / referee paths in a title; G-4 σ̄, G, «pointwise optimum» unglossed; G-5 «S4B-OPT»
beside L42's «[S4b-OPT]»; soft spots D-1 to D-8. Found none of: DATA overclaim (consistent with Erratum E-1), asymptotic DEAD, stale pin,
old line as current, missing L41 clause. (7) NOT RUN / NOT DONE: the corpus re-run (the stored s4bopt_corpus.txt was re-summed, not
re-computed); the referees' own tools (not re-run); check.sh's other blocks and scripts/verify.sh (not run); the Lead's 02:24Z message
(D-8) not found. Scratch files (not committed) are in
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad: R102-template.md, assemble102.py,
fill102.py, upd102.py / upd102.txt, wdiff102.py / wdiff102.out, sum102.py / sum102.out, fxq102.py, q102.py / q102.out, pin102.time /
pin102.out (arch96fb/experiments/si/pin102.sh), mut102.time / mut102.out, si_check_96fb.sh, ft102.out, arch96fb/.
