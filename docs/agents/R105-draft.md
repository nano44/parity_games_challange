# Draft RESULTS R105 (Lead; first fill 2026-11-04T01:08:55Z by date -u (subagent); on P-IDEAL-RED line L-2, docs/new/P-IDEAL-RED-line-L2.txt, l-new ffeb9736, sha1 65ba7ca7fd6d4cb6b0de1d1c918ec181ff78fbe5) — to CHECKER C116 — LANDED in RESULTS 2026-11-04 02:59Z (CHECKER C116 e85c3bb2 PASS), after R104, before Erratum E-1
FIRST FILL. Read at the origin heads fetched at the start of the fill (git fetch, then git ls-remote, 2026-11-04T00:47:11Z: l-new
4f6b6d6e, referee 0d2fef9f, referee-2 f81c6e57, checker 0dd31142; origin trunk 5f27819f; local trunk c1077737, one Lead commit not
pushed, which changes only docs/NOW.md and three docs/agents/ files, so RESULTS (3398c652), GAPS (3398c652), DECISIONS and
DECISIONS-INDEX (8c37ab0b) and TARGET.md are byte-equal to origin trunk): the packet (0ebddcf5), fixes entry 1 and L-1 (b115ff3a), fixes
entry 2 and L-2 (ffeb9736; the packet, the fixes and L-2 unchanged at the l-new head 4f6b6d6e, by cmp); REFEREE successor 23's
docs/referee/R-P-IDEAL-RED.md (report a71540d5, §C d8f25ef2, §C addendum 1 0d2fef9f) and its pre-check docs/referee/R-XI-NEW-precheck.md
(a4e7b4a9); REFEREE-2 successor 26's docs/referee-2/R2-P-IDEAL-RED.md (2f9b6f5c), R2-P-IDEAL-RED-L1.md (ca757330) and
R2-P-IDEAL-RED-L2.md (f81c6e57); notes/L-NEW.md at ffeb9736 (l. 17-30, box 150); DECISIONS D14, D18, D19 with Lead reading L47;
RESULTS R104 (title l. 9864, the model definition only). Re-runs (scratch, git archive of 0ebddcf5's experiments/new): the three
commands of check.sh block w99, 2026-11-04T00:49:10Z-00:49:35Z, rc 0, output byte-equal to the block's expected strings; check.py on the
200 random genomes from their default starts and with NEG=1, NEG=2, 2026-11-04T01:05:00Z, rc 0, output extra.out (the referees'
figures, (10)).
TRUNK STATUS AT THIS FILL (by script, git merge-base --is-ancestor against local trunk c1077737 and origin trunk 5f27819f): 0ebddcf5,
b115ff3a, ffeb9736, 4f6b6d6e, a4e7b4a9, a71540d5, d8f25ef2, 0d2fef9f, 2f9b6f5c, ca757330 and f81c6e57 are NOT on either trunk (exit 1
each). The Lead merges claude/l-new, claude/referee and claude/referee-2 and pushes trunk before landing. C113 E-2 lesson: the body
names these commits on their branches only and makes NO statement about trunk. C113 E-1 lesson: the title is L-2 verbatim with no
insertion (L-2 carries its own date parenthesis and source note). C114 Add. 1 E-1 lesson: the GAPS UPDATE head carries «<DATE>»,
filled with the landing date at landing. C115 E-1 lesson: the premise route is checked against what RESULTS records (G-4 below). In
the body (title + entry), L-2 is the current line; sentences about the earlier line say «at L-1».
to check: FLAGS FIRST (G-1 to G-10; none REQUIRED from my side; no referee raised any of them as REQUIRED), then the CLEAN items and
(0)-(14).
- G-1, TITLE SHAPE AND SOURCE NOTE (note; no Lead insertion). L-2 contains «2026» once, as « (2026-11-03) — », the only « — » (by
  script), and ends with the source parenthesis «(P-IDEAL-RED, docs/new/P-IDEAL-RED.md with its fixes entry 1,
  docs/new/P-IDEAL-RED-fixes.md; L-NEW successor 50)», the shape of R101's and R103's source notes. The title is "### R105
  [refereed-only] " + L-2 + the fill ", CHECKER PASS (docs/checker/C116.md, checker PENDING)" (as R90-R104), nothing inserted. NOTE: the
  source note says «with its fixes entry 1» while the fixes file at ffeb9736 holds entries 1-2. Entry 2 is L-2's word diff and changes
  the line only (fixes l. 71 «line L-1 is left unchanged. Packet and entry 1 unchanged.»), so the packet text of record is the packet
  with entry 1 (entry 1 l. 66-67: «Signed by both referees: every statement of the packet, with F-1 and F-2 in place (U-EQ with F-1).
  Nothing else changes.»). REFEREE-2 L2 l. 51-52 accepts it («That is acceptable.»), with the optional wording «fixes entries 1-2»
  (l. 52, l. 64); REFEREE §C addendum 1 l. 290 checks «L-2 against packet + fixes (entries 1-2)». The same note was ruled for R103
  (R103-draft G-1 (a): «with its fixes entry 1» with entries 1-2 on file). The body follows REFEREE-2's optional note: it describes the
  source as «fixes entries 1-2» wherever the body speaks (Object, Fixes); only the title keeps L-2's words.
- G-2, STRICT SYMBOL TEST (notes; both referees' binder passes are clean on L-2, (7)). (i) «unstable» (TOP-MONO, RANK-BOUND, the
  TOP_k clause) is not glossed in L-2; packet §0 l. 46 «x is UNSTABLE at s iff c_s(x) ≥ 1», and c_s(x) is bound in the line's
  parenthesis («c_s(x) the number of options of x strictly better than its current one»). (ii) «moves(x)» (KEYFLIP) is not glossed;
  packet l. 59 «moves(x) := |{t : x ∈ Mv_t}|», plain (the number of steps at which x moves). (iii) «strict Ξ-descendant» (RISE)
  is not glossed; packet l. 39 «A strict Ξ-descendant of x is a mover reachable from x by a nonempty Ξ-path.» (iv) «a» in «step a +
  j» (INTERVAL-RESTRICT) is not named: REFEREE §C addendum 1 l. 288-289 (optional only) «The only reading is «a = the index of the
  interval's first state»». (v) «n» in RECURSION is bound locally («U*(n) the largest U over degree-≤-2 genomes with at most n
  degree-2 movers»), not RESULTS' usual n := |V|. (vi) «D the largest degree» omits the packet's «D := max_x deg(x) ≥ 2» (l. 152);
  REFEREE-2 table l. 41 «**SIGN** (D ≥ 2 as stated; D = 1 gives T = 0 trivially)»: at D = 1 no mover moves, T = 0 and D^N − 1 = 0,
  so the line's clause holds as stated. (vii) The (KEYFLIP) clause carries KF-EQ's content («so T ≤ N + KF and KF ≤ N T (T polynomial
  iff KF is)»); KF-EQ has no label of its own in L-2 (REFEREE §C (b) l. 225 «KEYFLIP (with KF-EQ)»). (viii) RECURSION in L-2 states the
  packet's third bullet only (REFEREE-2 L1 table: «bullet 1 not stated; a subset is fine»). (ix) LOCAL in L-2 («an option's value
  depends only on the states on its chain, a key only on the states below its level») is the informal form of packet (a)-(c);
  REFEREE §C (b) l. 224 and REFEREE-2 L1's table (row LOCAL, ✓) match it. None is a claim clause's quantifier left free.
- G-3, NAMES, SAME LABELS, OTHER MEANINGS (by script on RESULTS 3398c652 / GAPS 3398c652; note; the line cannot change without an
  L-3). 0 times in RESULTS and GAPS: «P-IDEAL-RED», «R105», «XI-NEW», «CHAIN-BACK», «U-EQ», «KEYFLIP», «KF-EQ», «DECREMENT»,
  «EXACT-ENERGY», «RANK-BOUND», «INTERVAL-RESTRICT», «INTERVAL-CHARGE», «RECURSION», «(ENC)», «(LOCAL)», «(RISE)», «KF_x», «TOP_k»,
  «U*(n)»; «ENC» 0 times as a word. Same names, other meanings: «TOP-MONO» 4 times in RESULTS (R84: l. 4941 title «the Δ form of
  TOP-MONO is DEAD», l. 4987, 5019, 5058) and once in GAPS l. 11 (R84's UPDATE), a DEAD Δ form on real N5 runs, not this IDEAL
  statement; «Lemma MONO» in R25 (c) (l. 1130) and «(MONO)» in R77 (l. 4197), other items; «Lemma RISE» in R42 (a) and RISE′ in R44,
  other items. After landing, «TOP-MONO», «MONO» and «RISE» name two things; in L-2 they sit inside «In the IDEAL model of RESULTS
  R104», which scopes them (precedent: R104's G-10 (c), «Lemma K», «Lemma W», body only). Proposed: a note, no line change.
- G-4, PREMISE ROUTE (the C115 E-1 class): CLEAN (my check). L-2's premise parenthesis: «premise: R104's definition of the model only,
  no theorem of R104 used». The packet (l. 22-25): «LANDED: RESULTS R104 (P-N5-REALIZE), ONLY its definition of the IDEAL model and
  of the Ξ-graph, restated in §0 below. No theorem» «of R104 (REALIZE, REAL-IDEAL) is used. No other RESULTS entry is used.»; «Not
  used: L-RED R178 (its Lemma XI-NEW is re-proved in full in §3; the lane text is not a premise), docs/lit, docs/sources, any» «other
  lane file. No outside source is cited.» Both referees checked it: REFEREE §1 l. 36 «The packet declares a single premise: RESULTS
  R104's DEFINITION of the IDEAL model and of the Ξ-graph. No theorem of R104 is used.», l. 41 (no reference inside a proof), l. 42
  «No docs/lit premise is used (lesson C115 E-1).», l. 46-56 (§0 against R104 clause by clause, «All agree.»); REFEREE-2 §0 l. 11
  «**Premise route ✓.** The only premise is RESULTS R104's DEFINITION of the IDEAL model and the Ξ-graph.», l. 19 «No theorem of R104
  is used. No other RESULTS entry is used. Nothing comes from docs/lit, docs/sources or a lane file.», l. 21 «The C115 E-1 lesson is
  respected.» L-RED R178 appears in L-2 only as an attribution, «(the model first stated in L-RED R178 §1)» (REFEREE optional L-1f;
  REFEREE §C addendum 1 l. 276-277 «It is an attribution, and the premise clause» «still reads «R104's definition of the model only»»;
  REFEREE-2 L1 l. 67-68 «is R104's own attribution of the» «model, not a premise ✓.»). The R104 definition is landed text (RESULTS
  l. 9864, title); no unlanded result, no lit note and no lane file is a premise. My own grep (by script) of the packet: «docs/lit»
  once (l. 24, the «Not used» list), «R178» 4 times (l. 24, 96, 115, 247: the «Not used» list,
  the §3 heading, §3's «Does NOT claim» line and §9's EXCLUDED list), none inside a «Proof.» block (l. 67-70, 81-84, 90-93, 99-105,
  110-114, 122-125, 134-137, 147-151, 154-155, 164-167, 171-173, 183-201, 204-209, 219-226), as REFEREE l. 38-41 says.
- G-5, L41 (the C109 E-1 class): not triggered (my reading; neither referee mentions L41). L-2 contains «referee-originated» 0 and
  «lane-authored» 0 times. The proofs are L-NEW successor 50's (packet l. 5 «Labels: PROVED (L-NEW 50, unrefereed) / DATA / READING.»).
  THREE POINTS TO CHECK: (a) F-1's corrected inequality «U ≤ max(T − 1, 0)» was suggested by both referees (REFEREE U-1 l. 89 «Fix: «U
  ≤ max(T − 1, 0)», or «for T ≥ 1».»; REFEREE-2 N-1 l. 139); its justification is one count from the packet's own definition, written
  by the lane in F-1's Reason (fixes l. 13 «Reason: U counts unchained steps in [2, T], so U ≤ T − 1 when T ≥ 1 and U = 0 when T =
  0.»). A statement correction, not a referee-originated proof (my reading). (b) F-2's remark (all-option monotonicity) is REFEREE's
  IR-1 argument, but it is «Remark (not a signed statement)» (fixes l. 20) and is NOT in L-2 (REFEREE §C (b) l. 230, REFEREE-2 L2 l.
  45). (c) MONO, the lemma XI-NEW's RISE needs, closes REFEREE's pre-check gap XI-G1 with «the same induction as my pre-check §3»
  (REFEREE l. 142); the packet's proof is the lane's (§2 l. 90-93), and REFEREE-2 checked it independently (§2 l. 61-64). REFEREE wrote
  the same induction in its pre-check (§3 l. 68-76, a4e7b4a9, 20:23:37Z), after the packet's freeze (19:30:17Z), which already
  carried MONO's proof; the lane notebook records MONO as its own finding (notes l. 22-23 «XI-NEW (ii)'s «Xi is
  monotone» needs Lemma MONO (current value of every mover never falls); proved by» «induction in reverse pi with the integer
  encoding ENC»). Not referee-originated (my reading).
- G-6, L43 (DEADs): CLEAN. L-2 has no DEAD (by script: «DEAD» 0, «O(» 0, «linear» 0). «polynomial» 3 times: «T is polynomial in N + M
  iff U is» (U-EQ), «(T polynomial iff KF is)» (KEYFLIP / KF-EQ), «bounds nothing polynomially» (tail). The clause «degree ≤ 2 is needed
  for KEYFLIP and TOP-MONO (DATA, REFEREE-2 N-2)» is a DATA clause on explicit failing runs, not an asymptotic DEAD: REFEREE-2 L1 l.
  65-66 «these» «are explicit failing instances, so L43 is not triggered.» NOTE: the clause names its source but no number and no
  instance file; the counts are in fixes F-4 (l. 60-63) and REFEREE-2 N-2 (l. 141-146), and REFEREE reproduced the effect on its own
  genomes (§C l. 215-216). The KEYFLIP count uses an extension of KP to degree ≥ 3 («KP := the key-least option», N-2 l. 142), since
  the packet defines KP for deg(x) = 2 only (l. 131).
- G-7, DATA vs READING (the C108 E-1 class): CLEAN. L-2's DATA parenthesis «(DATA: 0 violations of every inequality on 46 corpus
  genomes and 75,518 all-start runs of 200 random genomes, experiments/new/box150/check.py)» is packet §9's DATA (l. 240-243),
  reproduced by both referees (REFEREE §5 l. 150-154 «MATCHES.»; REFEREE-2 §4 l. 165-168) and by me ((10)). «every inequality» means
  every inequality where it is stated (REFEREE §C (b) l. 234: check.py runs the degree-≤-2 checks only on degree-≤-2 genomes). Packet
  §9's READING (l. 259-261) is not in L-2 (by script: «READING» 0, «refereed place» 0).
- G-8, LEAD READINGS AND RULINGS AS ON FILE (the C111 E-1 class): CLEAN. L-2 cites no Lead reading and no ruling (by script:
  «Lead reading» 0, «L4» 0, «D1» 0). The lane works under D14 / D18 (packet l. 2) and D19 / L47 (NOW roster «D14/D18/D19»; REFEREE-2 l.
  2 «Owner D19 / Lead reading L47.»). L47 (DECISIONS l. 411-419; index «active»): «L-NEW successor 50 starts with» «(a) freezing packet
  P-IDEAL-RED (CHAIN-BACK + KEYFLIP, R178 XI-NEW proof carried) for the referees» (l. 415-416), «(3) Gates: when P-IDEAL-RED is frozen,
  a fresh REFEREE successor (REFEREE 22 is at ~474k) and REFEREE-2 26 review it; CHECKER 16 lands it.» (l. 419). The packet carries the
  XI-NEW proof in full (§3) and does not rest on R178 (G-4). D18's «Clearly distinguish proven results from conjectures and open
  problems.» (DECISIONS l. 333): the packet labels PROVED / DATA / READING (l. 5), every CONJECTURE is EXCLUDED (l. 252), REFEREE-2 §4
  l. 171-174 («**D18 labels.**»).
- G-9, STALE LANE TEXT (notes; nothing here lands). (i) The fixes file's heading (l. 1) still reads «# P-IDEAL-RED fixes, entry 1
  (fix round after REFEREE 23 and REFEREE-2 26)» while it holds entry 2 at l. 70-83 («## Entry 2 (line L-2; REFEREE L-1a/b/d/e +
  REFEREE-2 L-R1/R2/R3, routed by the Lead 23:40Z)»); append-only is kept (REFEREE-2 L2 l. 14 «shows 0 deleted lines, and 15 added lines
  (entry 2)»). (ii) Packet l. 94 («Does NOT claim: that any non-current option's value is monotone (it is not in general)») is
  superseded by F-2; packet l. 126 by F-1; l. 169-170, 181, 223-225 by F-3; l. 251 gains F-4's DATA item. The body quotes the superseded
  text only as history. (iii) Packet l. 2-3 «Written» «2026-11-03 (date -u: see the commit).»: the freeze commit is 0ebddcf5, committer
  date 2026-11-03T19:30:17Z (author 19:30:03Z). (iv) F-4's middle numbers (2,473 and 78,579) are REFEREE-2's runs with every start for N
  ≤ 9 (74,495 runs), not the packet's 75,518-run set; REFEREE-2
  L1 l. 35-36 (optional O-2) asks for «the packet's 200 random genomes, every start for N ≤ 9»; entry 2 did not take O-2 (it is not a
  line item); F-4 is not in L-2.
- G-10, NO SHA1 PIN IN check.sh (note; the C110 F-1 class). experiments/new/check.sh at ffeb9736 (835 lines) and at 4f6b6d6e
  (841 lines) pins neither the packet, L-1, L-2 nor the fixes by sha1 (by grep: «06f2c186», «44d0287a», «65ba7ca7», «727b6f0c»,
  «2e8c3630» 0 times at each); R104's experiments/red/check.sh did. The sha1s here rest on both referees' re-hashes (REFEREE §C addendum
  1 l. 268-273; REFEREE-2 L2 table l. 9-12) and on mine ((1), (8)). Block w99 (l. 814-819; sha1 of those six lines
  d882719a3119a803029ed487e579eb6fdd052109) and box150/check.py (sha1 019de0f7b36dcbd47743b3d27b4a1a93549d574b, 214 lines) are
  byte-equal at 0ebddcf5, b115ff3a, ffeb9736 and 4f6b6d6e.
- CLEAN AT L-2 (the pre-check against CHECKER's recurring items, by script on 65ba7ca7):
  C106 E-1 (old line as current): the title is L-2; L-1 occurs in the body only in «at L-1» sentences and in the line history.
  C113 E-1 (title «verbatim» after an insertion): no insertion; the title is byte-equal to prefix + L-2 + fill (Addendum (2)).
  C113 E-2 (trunk status that goes stale): the body has no trunk statement (header).
  C114 Add. 1 E-1 (UPDATE date): <DATE> placeholder.
  C115 E-1 (a premise route RESULTS records as not established): G-4.
  C110 F-1 (stale pins vs landed labels): G-10 (no pins; sha1s re-taken by me and both referees).
  C111 E-1 (stale Lead-reading statements): G-8.
  «|»: 0 in L-2, 0 in the entry block, 0 in the UPDATE (by script, Addendum (3)).
(0) PLACEMENT. R105 goes DIRECTLY AFTER R104 and BEFORE «**Erratum E-1**». docs/RESULTS.md at trunk c1077737 (= origin 5f27819f for
this file) has sha1 59c7a38392fd9bf0513002754d969a45ba49138f, 10,688 lines, last changed by 3398c652 (R104's landing). «### R104» is l.
9864 (entry l. 9864-10153, l. 10154 blank); «**Erratum E-1**» is l. 10155; «## Dead ends (kept;» is l. 10168. PROPOSED (R102's to
R104's layout): insert R105's entry after l. 10154 (R104's blank line) and before «**Erratum E-1**», with one blank line after it, so
the R-entries stay contiguous and the erratum closes the Results section. The erratum's line references (l. 7963-9195) lie before the
insertion and do not move. "### R105" occurs 0 times in RESULTS and GAPS, «R105» 0 times (G-3). GAPS has sha1
3cde26690f95f516e00f08ecb56e26106651f5a7, 23 lines, last changed by 3398c652. The Lead re-checks (6) and (9) at landing only if RESULTS
or GAPS change after 3398c652.
(1) TITLE. The title is the line file docs/new/P-IDEAL-RED-line-L2.txt (l-new ffeb973670db02b59e6c89f406481979fc94121c,
2026-11-03T23:39:27Z, the file's only commit, sha1 65ba7ca7fd6d4cb6b0de1d1c918ec181ff78fbe5; identical at the l-new head 4f6b6d6e),
verbatim: one line, no outer quotes, no final period, 3,655 characters (3,773 bytes plus the newline), 704 whitespace tokens, 74 / 74
parentheses (depth never negative), no «…». NO HEADING MARKER, verified by script: the file begins «In the IDEAL model of RESULTS
R104», with no «#» at its start, no "R??" and no lane tag (L41 «Lanes write line files without a heading marker»). NOTHING is
stripped and NOTHING is inserted: the heading is the level-3 marker, then "R105 [refereed-only] ", then the file without its newline,
then the fill ", CHECKER PASS (docs/checker/C116.md, checker PENDING)" (as R90-R104, no space before the comma; C116 is the next
CHECKER file, NOW roster «next C116»). L-2 holds one « — », its own date parenthesis «(2026-11-03)» and no "|" (G-1). Built by script
(scratch fill105.py: assert the sha1 65ba7ca7…, equality with the blob at ffeb9736 and at the l-new head, one line, no marker, one «
(2026-11-03) — », no "|"; prepend, append) and re-checked after writing this file: equal, byte for byte. Heading: 3,734
characters, 3,852 bytes; sha1 of the heading line without its newline
d45097cd5b3787a8488a0db50e24185705d67aad; it is l. 346 and the only «### R» line of this file.
(2) LINE HISTORY: there is no frozen line (0ebddcf5 committed the packet, box150/ and check.sh only; a file
docs/new/P-IDEAL-RED-line.txt does not exist at any commit: git log --all on that path is empty). L-1
44d0287a5d304aa5342b8cd98c6cbccb9e8af6b3 (b115ff3a, 2026-11-03T22:30:34Z; 3,375 bytes, 620 tokens; with fixes entry 1; REFEREE §C NOT
YET (L-1a, b, d, e), REFEREE-2 L1 does NOT match yet (L-R1 to L-R3)) → L-2 65ba7ca7 (ffeb9736, 23:39:27Z; 3,774 bytes, 704 tokens; fixes
entry 2). Each line file has one commit. L-1 → L-2 (scratch wdiff105.py, output wdiff105.out): difflib over whitespace tokens, 10
non-equal opcodes, 613 tokens in common; L-1 with entry 2's ten changes (each old phrase found once, with its context) equals L-2: True.
The ten changes (fixes l. 74-83): (1) «(L-RED» → «(the model first stated in L-RED» (REFEREE optional L-1f); (2), (3) ENC: «so, with
ε(x, k) := ±2^rank(x, k) (+ for even parity),» and «(ε(x, k) alone if the Ξ-target is the exit X)» (REFEREE L-1a = REFEREE-2 L-R1,
REQUIRED); (4) XI-NEW: «(A_s(h): h's current option under s and its options strictly better under s)» (L-1b = L-R2, REQUIRED); (5) RISE:
«under s_(t−2)» (REFEREE optional L-1c = REFEREE-2 O-1); (6) CHAIN-BACK: «steps t ∈ [2, T];» (REFEREE L-1d, REQUIRED); (7) TOP-MONO:
«(padded with −1 to length k)» (optional L-1g); (8), (9) RANK-BOUND: «for k ≥ 1,» and «(R := 0 if U = 0)» (optional L-1h); (10)
INTERVAL-RESTRICT: «from the interval's third state on (step a + j of the run against step j of the restricted run, for j ≥ 2)» (L-1e =
L-R3, REQUIRED). = REFEREE §C addendum 1 l. 274-275 «my own word diff (split on blanks, diff) gives exactly 10 hunks. They equal entry
2's list and nothing else» «differs:»; = REFEREE-2 L2 l. 17-18 «L-1 with exactly the 9 replacements below, each old phrase» «occurring
once, equals L-2: **True**.», l. 31 «So L-2 = L-1 + the four REQUIRED changes (L-R1, L-R2, REFEREE L-1d, L-R3) + the optional items 5-8,
and nothing else.» (REFEREE-2 counts «9 replacements» in 8 table rows; my test uses entry 2's 10 hunks; same result.) The wording of (4)
is not REFEREE-2's L1 proposal («h's option under s»,
L1 l. 78) but adds «current»; REFEREE-2 L2 table l. 24 «(«current» added: better than my wording; = §0's A_s)».
No inequality of a signed statement differs between L-1 and L-2: every change adds a binder (ε, A_s, the range of U), a scope (the
label agreement from the third state on; RISE's chain under s_(t−2)), the pad of TOP_k, R := 0, or an attribution wording.
(3) THE LINE AT BOTH REFEREES. L-2 (the title): REFEREE successor 23, docs/referee/R-P-IDEAL-RED.md «## §C addendum 1
(2026-11-04T00:09Z by date -u, successor 23; Opus 5.5, D15): line L-2» l. 267-295 (0d2fef9f, 2026-11-04T00:09:07Z, +30; the file now
295 lines, sha1 b5d3801e925ec8f5ae85185a656097b203514a2c; l. 1-265 unchanged from d8f25ef2, byte prefix): l. 295 «VERDICT: line L-2
MATCHES. All 16 statements are SIGNED with fix entry 1 in place.» REFEREE-2 successor 26, docs/referee-2/R2-P-IDEAL-RED-L2.md
(f81c6e57, 2026-11-04T00:09:46Z, new file, 64 lines, sha1 644feeee1479b30398d1c7ebd3601c025a17dfdb): l. 2 «Verdict: **MATCHES**.»,
l. 55 «**MATCHES.**», l. 56 «L-2 (65ba7ca7) = L-1 + exactly the four required changes + the optional items 5-8 (byte test True).»,
l. 57 «It matches the packet read with fixes entries 1-2. Every clause is a signed statement with its exact hypotheses.»
At L-1: REFEREE «## §C (2026-11-03T23:02Z by date -u, successor 23; Opus 5.5, D15): fix round entry 1 and line L-1» l. 194-265
(d8f25ef2, 23:02:24Z, +73; 265 lines, sha1 8f1c9a472169a7a1dee9e5a08a0a42678885d23c; l. 1-192 unchanged from a71540d5, byte prefix): l.
263-264 «Line L-1: NOT YET. It matches once L-1a, L-1b, L-1d and L-1e are applied. L-1c and L-1f to L-1h are optional. No other
change is» «needed.»; REFEREE-2 R2-P-IDEAL-RED-L1.md (ca757330, 23:03:25Z, new file, 92 lines, sha1
522315c3f623c037566b19c175bccaf276e7176e): l. 3-4 «Verdict: fixes **CORRECT**; line L-1 **does NOT match yet**: three exact word
changes are REQUIRED (L-R1 to L-R3, all binder /» «scope wording, §3).» Both MATCH L-2.
LINE-ITEM NAMES: REFEREE L-1a (ENC ε and exit, REQUIRED), L-1b (A, REQUIRED), L-1c (RISE, optional), L-1d (U's range, REQUIRED), L-1e
(label scope, REQUIRED), L-1f (R178 attribution, optional), L-1g (TOP_k pad, optional), L-1h (RANK-BOUND k ≥ 1, R := 0, optional);
REFEREE-2 L-R1 (= L-1a), L-R2 (= L-1b), L-R3 (= L-1e), O-1 (= L-1c), O-2 (F-4 wording, not a line item). Entry 2 «Taken: REQUIRED 1
(ENC: ε defined, exit case), 2 (XI-NEW: A defined), 3 (CHAIN-BACK: U over t ∈ [2, T]), 4 (INTERVAL-RESTRICT: labels from the third
state on); OPTIONAL 5 (RISE: chain under s_(t−2)), 6 (R178 not read as a source), 7 (TOP_k padding), 8 (RANK-BOUND: k ≥ 1, R := 0 if U
= 0).» (fixes l. 72). All REQUIRED items and all optional line items are in L-2.
(4) CLAIMS SIGNED = the sixteen items below, each SIGN in BOTH referees' verdict tables (REFEREE "## 0. Verdicts" l. 10-29 of
R-P-IDEAL-RED.md at a71540d5; REFEREE-2 "## 1. Verdict table" l. 28-47 of R2-P-IDEAL-RED.md at 2f9b6f5c), checked clause by clause
against the packet and its fixes; the cells are the original reports' words (row (g) after F-1: see below the table):
| item (packet §, lines) | REFEREE (successor 23) | REFEREE-2 (successor 26) |
| --- | --- | --- |
| (a) Lemma ENC (§1, l. 64-74) | l. 13 «SIGN»; §2 l. 59-61 | l. 31 «**SIGN**»; §2 l. 52-56 |
| (b) Lemma LOCAL (a)-(c) (§1, l. 75-85) | l. 14 «SIGN»; §2 l. 62-65 | l. 32 «**SIGN**»; §2 l. 57-60 |
| (c) Lemma MONO (§2, l. 88-94; fixes F-2) | l. 15 «SIGN» with «REQUIRED text fix IR-1»; §2 l. 66-75 | l. 33 «**SIGN**»; §2 l. 61-64 |
| (d) Lemma XI-NEW (§3, l. 97-105) | l. 16 «SIGN»; §2 l. 76-79 | l. 34 «**SIGN** (acyclicity indeed unused)»; §2 l. 65-71 |
| (e) Corollary RISE (a)-(c) (§3, l. 106-115) | l. 17 «SIGN»; §2 l. 80-83 | l. 35 «**SIGN**»; §2 l. 72-76 |
| (f) Theorem CHAIN-BACK (i), (ii) (§4, l. 118-125) | l. 18 «SIGN»; §2 l. 84-86 | l. 36 «**SIGN**»; §2 l. 77-81 |
| (g) Corollary U-EQ (§4, l. 126-128; fixes F-1) | l. 19 «SIGN WITH GAP U-1»; §2 l. 87-90 | l. 37 «**SIGN** with precision N-1»; §2 l. 82-84 |
| (h) Lemma KEYFLIP (§5, l. 131-137) | l. 20 «SIGN»; §2 l. 91-93 | l. 38 «**SIGN**»; §2 l. 85-90 |
| (i) Corollary KF-EQ (§5, l. 138-141) | l. 21 «SIGN»; §2 l. 94 | l. 39 «**SIGN**»; §2 l. 91-93 |
| (j) Lemma DECREMENT (a)-(c) (§6, l. 144-151) | l. 22 «SIGN»; §2 l. 95-98 | l. 40 «**SIGN**»; §2 l. 94-98 |
| (k) Corollary EXACT-ENERGY (§6, l. 152-157) | l. 23 «SIGN»; §2 l. 99-101 | l. 41 «**SIGN** (D ≥ 2 as stated; D = 1 gives T = 0 trivially)»; §2 l. 99-102 |
| (l) Corollary TOP-MONO (§7, l. 160-167) | l. 24 «SIGN»; §2 l. 102-104 | l. 42 «**SIGN**»; §2 l. 103-107 |
| (m) Corollary RANK-BOUND (§7, l. 168-174; fixes F-3 P-1) | l. 25 «SIGN», «optional P-1 (the R = 0 case)»; §2 l. 105-109 | l. 43 «**SIGN**»; §2 l. 108-111 |
| (n) Lemma INTERVAL-RESTRICT (i)-(iii) (§8, l. 177-201; fixes F-3 P-2) | l. 26 «SIGN», «optional P-2»; §2 l. 110-118 | l. 44 «**SIGN**»; §2 l. 112-121 |
| (o) Corollary INTERVAL-CHARGE (§8, l. 202-209) | l. 27 «SIGN»; §2 l. 119-122 | l. 45 «**SIGN**»; §2 l. 122-126 |
| (p) Corollary RECURSION (§8, l. 210-230; fixes F-3 P-3) | l. 28 «SIGN», «optional P-3»; §2 l. 123-132 | l. 46 «**SIGN**» («all three bullets»); §2 l. 127-136 |
Both, verbatim: REFEREE l. 133 «None of §2's checks found a hole in a proof. The only false text is IR-1 (a remark) and U-1 (an edge
case of one inequality).», FINDINGS l. 188 «15 statements SIGN, 1 SIGN WITH GAP (U-EQ: U-1, the T = 0 edge case).»; REFEREE-2 l. 49
«No gap. One precision (N-1), two notes (N-2, N-3).», DONE l. 177 «all 16 statements SIGNED (U-EQ with precision N-1).»
ROW (g) AFTER F-1: REFEREE §C (d8f25ef2) l. 202-204 «F-1 = U-1: CLOSED.», «U-EQ is now SIGNED without gap.», l. 218 «After entry 1,
my verdicts: all 16 statements SIGNED, U-EQ included.»; REFEREE-2 L1 (ca757330) l. 20 «**F-1 (U-EQ, REQUIRED) ✓.**». ROW (c) AFTER
F-2: REFEREE §C l. 205-209 «F-2 = IR-1: CLOSED.»; REFEREE-2 L1 l. 21 «**F-2 (MONO «Does NOT claim», REQUIRED, REFEREE IR-1) ✓, and it is
my miss.**». F-2 changes no statement: it deletes a false «Does NOT claim» parenthetical (packet l. 94) and adds an unsigned remark.
Clause checks (L-2 against the packet and its fixes): the setting parenthesis = §0 l. 29-61 (N, M, T = R104's L(G) l. 54, h_t and y_t
l. 58, c_s(x) l. 46, KP_s(x) l. 131, π l. 37-39, «any number of movers per level» = l. 60 «No width hypothesis is made anywhere»);
ENC = §1 l. 64-66 with the consequence l. 71-73 (as integers; F-2's remark is not used); LOCAL = l. 76-80; MONO = l. 88-89 (current
values only); XI-NEW = l. 97-98 with A_s of l. 45; RISE = (a), (b) of l. 107-108 with the chain under s_(t−2); CHAIN-BACK = l. 118-121;
U-EQ = F-1 (fixes l. 12); DECREMENT = l. 145-146; EXACT-ENERGY = l. 152-153; «at degree ≤ 2 only»: KEYFLIP = l. 133 with KF-EQ l.
138-139, TOP-MONO = l. 160-163, RANK-BOUND = l. 168-170 with F-3 P-1, INTERVAL-RESTRICT = (i)-(iii) of l. 177-182 with F-3 P-2,
INTERVAL-CHARGE = l. 202-203, RECURSION = the third bullet l. 216-218. Nothing in L-2 is wider than signed (REFEREE §C (b) l. 228-229
«The degree split is exact.»; REFEREE §C addendum 1 l. 291-292).
Signed by both, NOT stated by L-2 as separate items: KF-EQ (inside the KEYFLIP clause, G-2 (vii)); RISE (c) (π(z) > π(h)); RECURSION's
first two bullets; ENC's statement for arbitrary finite sets of β's is stated in L-2 as the order of integers. Not signed, so NOT
landed: F-2's remark, §9 DATA (DATA clause only), §9 READING.
(5) OTHER TEXTS THE ENTRY DEPENDS ON: the premise RESULTS R104's definition of the IDEAL model and of the Ξ-graph (title l. 9864; no
R104 theorem); nothing else. The XI-NEW pre-check (REFEREE a4e7b4a9) is history: «This is a PRE-CHECK of a lane lemma (Lead brief,
STEP 1), NOT» «a signature.» (l. 2-3); its gap XI-G1 is CLOSED by MONO and XI-G2 is EXCLUDED (REFEREE §4 l. 142-145). The lane
sources docs/new/N5-IDEAL-STATE.md §6 and boxes 144, 147, 148, 149 (packet l. 4) and L-RED R178 are history only; no lane file and no
lit note is a premise (G-4).
(6) PREMISE LABELS (stale-label test; RESULTS at 3398c652, GAPS at 3398c652). RESULTS labels in L-2 (by script): «R104» 3 («RESULTS
R104», «R104's definition», «theorem of R104»); «R178» 1, an L-RED box label, prefixed («L-RED R178 §1»). R104 (l. 9864) exists and
carries the definition («an IDEAL genome G has N movers x with levels lev(x), M := Σ deg(x) options (x, k), each with a W-target of
level lev(x) − 1 (none at level 0), a Ξ-target xt(x, k), a mover or the exit X, a distinct β-rank with a parity, a distinct gate
index, and a start»; «the Ξ-graph has an edge x → xt(x, k) for every option with a mover as Ξ-target»). No Lead reading and no other
RESULTS label is cited. No label is retired by a later entry. G-N5-TIME open (GAPS l. 11).
(7) SYMBOL TEST of the title (my own strict test of every symbol of L-2; IN = bound in the line; else the carrier):
| symbol | where |
| --- | --- |
| IDEAL model, Ξ-graph, acyclic, mover, level, option, key, chain, β-sets, rank, parity, Ξ-target, exit X, state, step, run | RESULTS R104 (the premise) |
| π, N, M, T, h_t, y_t, c_s(x), KP_s(x) | IN (the premise parenthesis) |
| ε(x, k), A_s(h), chained, U, KF_x, TOP_k, RANK_t, R, D, U*(n), n | IN |
| unstable, moves(x), strict Ξ-descendant | not glossed (G-2 (i)-(iii); packet l. 46, 59, 39) |
| a (in «step a + j») | not named (G-2 (iv), REFEREE optional) |
| C(N, j), #, lexicographically | plain |
| L-RED R178 §1 | attribution, prefixed |
| DATA tail: 46 corpus genomes, 75,518 all-start runs, 200 random genomes, experiments/new/box150/check.py | DATA, cited |
Agreeing tests: REFEREE §C (b) l. 221-237 and §C addendum 1 l. 274-294; REFEREE-2 L1 §2 (binder pass, l. 40-69) and L2 §2 (l. 34-52).
(8) FIXES AND STATUS NOTES (docs/new/P-IDEAL-RED-fixes.md, L-NEW successor 50, append-only, two entries): at b115ff3a sha1
727b6f0ca8083dc53715a6eb5c3c816909412c43, 68 lines (entry 1; both referees checked this version at L-1: REFEREE §C l. 196 «sha1
727b6f0c…, 68 lines»; REFEREE-2 L1 table l. 12 «= Lead ✓»); at ffeb9736 sha1 2e8c3630b16cf6cd33564433da62c0fbba1f1f4e, 83 lines (+15,
entry 2 at l. 70-83; its first 68 lines have sha1 727b6f0c…, by script; both referees checked this version at L-2: REFEREE §C addendum
1 l. 270-271, REFEREE-2 L2 table l. 12). Header (l. 2-6): «Packet: docs/new/P-IDEAL-RED.md at 0ebddcf5 (sha1
06f2c18609e355a1e62c138c420bd49dc401cae4),» «NOT edited.»; «Where a fix is applied, the packet reads with the new text in place of the
old. No other» «change.»
Entry 1 (l. 1-68): F-1 (REQUIRED; REFEREE U-1 = REFEREE-2 N-1; U-EQ at T = 0); F-2 (REQUIRED; REFEREE IR-1; MONO's «Does NOT claim»
line); F-3 (optional wording; REFEREE P-1, P-2, P-3); F-4 (optional; REFEREE-2 N-2, DATA in §9); «Status after this entry» (l. 66-68).
Entry 2 (l. 70-83): L-2 and its ten-hunk word diff. No fix changes a signed inequality except F-1, which corrects U-EQ's edge case at T
= 0 to what the proof gives (U counts unchained steps in [2, T]); F-2 deletes a false remark; F-3 states a trivial case, an
identification the proof uses, and a count's name; F-4 adds DATA.
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-2 states no CONJECTURE and kills nothing of RESULTS or GAPS (the packet's CONJECTURES
U-LIN, DELAY-LIN, DELSTEP-LIN, UP-LIN are lane conjectures, EXCLUDED, l. 252, and occur 0 times in RESULTS and GAPS). A line-11
UPDATE is proposed at the end, to go AFTER R104's UPDATE (GAPS at 3398c652: the last UPDATE on l. 11 is R104's «UPDATE 2026-11-02
11:22Z: RESULTS R104 (P-N5-REALIZE; CHECKER C115 7c3c413f) [refereed-only] LANDED: …», ending «G-N5-TIME stays open.» before the row's
closing « |»; l. 11 holds 76 "|" and 39 «UPDATE 2026-»), as a pure insertion with one separating space. BUILT FROM L-2 (scratch
upd105.py: upd104L2.py's controls and upd100L3.py's build() unchanged). CONTROLS (same script, same run, rc 0): R97's to R104's LANDED
UPDATEs (GAPS l. 11 at 3398c652) rebuilt from their lines byte for byte (True ×8; R104's from REALIZE L-2 at c374be8f with head «UPDATE
2026-11-02 11:22Z: RESULTS R104 (P-N5-REALIZE; CHECKER C115 7c3c413f) [refereed-only] », 4,833 bytes, also equal to R104-draft l. 730
with <DATE> 2026-11-02, <HH:MM> 11:22, <checker> 7c3c413f). R105: L-2's tail has a new shape (no single scope parenthesis: «a REDUCTION
/ EQUIVALENCE statement inside the IDEAL model; bounds nothing polynomially (EXACT-ENERGY and RECURSION are exponential bounds; …); …;
G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (DATA: …) (P-IDEAL-RED, …)»), so build() would take the
«(EXACT-ENERGY and RECURSION …)» parenthesis as the scope and fail its own asserts. The label move is build()'s, unchanged, run (as
upd102.py did for R102) on the claim body plus a sentinel tail, with start «at any degree: » (15 labels, each found once after it, in
order). Tail rule (R102's and R104's rules on this shape; to check): « (2026-11-03) — » → «: »; the DATA parenthesis before the source
parenthesis opened as «; DATA: …» (R102's and R104's landed UPDATEs carry «; DATA…» in the open); «; G-N5-TIME stays OPEN» and «; not
M3, not a step-4 pass, not a TARGET.md claim» dropped; the source parenthesis kept; «. G-N5-TIME stays open.» appended. L-2 holds no
"|", so no replacement list. Checked by script: one line, 0 "|", one «<DATE>», one «<HH:MM>», one «<checker>», 3,806 bytes, 703
tokens; «2026-11-03» 0 times (the date parenthesis is dropped by the rule). Head «UPDATE <DATE> <HH:MM>Z: RESULTS R105 (P-IDEAL-RED;
CHECKER C116 <checker>) [refereed-only] » («P-IDEAL-RED» 0 times in GAPS and RESULTS); <DATE> = the landing date.
(10) DATA of record = packet §9 (l. 233-245), NOT signed; L-2's DATA parenthesis states its counts. Re-run at this fill (scratch, git
archive of 0ebddcf5's experiments/new; box150/, box139/ and the box14* inputs have no diff between 0ebddcf5 and 4f6b6d6e, by git diff
--stat; from experiments/, as check.sh's «cd ..»), 2026-11-04T00:49:10Z-00:49:35Z, rc 0, output w99.out:
- «TOTAL genomes 46 runs 46 steps 386 XSIM 0 TOPO 0 MONO 0 XINEW 0 RISE 0 CHAIN 0 KEYFLIP 0 DECR 0 TOPMONO 0 RBOUND 0 RESTR 0 ICHARGE
  0 REC 0 VIOL 0 (info REC148 0)» and «TOTAL genomes 200 runs 75518 steps 93963 XSIM 0 TOPO 0 MONO 0 XINEW 0 RISE 0 CHAIN 0 KEYFLIP 0
  DECR 0 TOPMONO 0 RBOUND 0 RESTR 0 ICHARGE 0 REC 0 VIOL 0 (info REC148 0)»: byte-equal to the block's two grep -qxF strings (l. 815);
  NEG=3: «TOTAL genomes 200 runs 200 steps 138 XSIM 8 TOPO 0 MONO 0 XINEW 6 RISE 3 CHAIN 0 KEYFLIP 0 DECR 0 TOPMONO 0 RBOUND 0 RESTR 0
  ICHARGE 0 REC 0 VIOL 17 (info REC148 0)» (matches the block's «XINEW [1-9]» test). The corpus glob expands to 46 files.
- Also re-run (same archive, 2026-11-04T01:05:00Z, rc 0, output extra.out): default starts «TOTAL genomes 200 runs 200 steps
  132 … VIOL 0» (= REFEREE l. 166 «132 steps»); NEG=1 «XSIM 168 … VIOL 168»; NEG=2 «XSIM 98 TOPO 0 MONO 93 XINEW 0 RISE 0 CHAIN 0
  KEYFLIP 0 DECR 66 TOPMONO 101 RBOUND 0 RESTR 5 … VIOL 363» (= REFEREE-2 l. 169 «NEG=1 (XSIM 168) and NEG=2 (MONO 93, DECR 66, TOPMONO
  101, RESTR 5) fire»).
NOT re-run: the referees' tools (docs/referee/scratch/xinew_probe.py, deg3_probe.py; docs/referee-2/R2-P-IDEAL-RED/ideal_check.py); I
read their committed logs (REFEREE-2 logs/run1.log, run2.log at 2f9b6f5c; REFEREE xinew_logs/deg3_probe.txt at d8f25ef2) and they equal
the reports' numbers (Data in the body). box150/rand.py (the generator) was not re-run; the 200 JSONs are committed. check.sh's other
blocks and scripts/verify.sh: not run.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 the source note «with its fixes entry 1» vs entries 1-2 on file
(G-1).
D-2 REFEREE-2 L2 l. 17 «the 9 replacements» against 8 table rows and 10 hunks (REFEREE's and entry 2's count); counting only, the byte
test is True either way ((2)). D-3 F-4's middle numbers are on 74,495 runs, not 75,518 (G-9 (iv)); REFEREE-2 l. 170 explains the cap
(«my all-start cap is N ≤ 9 (ALLN) and the lane's is N ≤ 10»). D-4 REFEREE's degree-≥3 counts (2,950 runs; 343 / 8,105) differ from
REFEREE-2's because the genomes differ (REFEREE §C l. 217 «My counts differ from REFEREE-2's because the genomes differ.»). D-5 the
fixes file heading names entry 1 only (G-9 (i)). D-6 REFEREE-2 L1's L-R2 wording («h's option under s») vs L-2 («h's current option
under s»), accepted by REFEREE-2 L2 l. 24. D-7 REFEREE-2 l. 172 «(refereed by me; the second referee is pending)» was pushed 48 s after
REFEREE's report (20:47:29Z vs 20:46:41Z) and before REFEREE-2 read it (L1 l. 15); stale by now, both sign. D-8 the pre-check
(a4e7b4a9, written «2026-11-03T20:01Z by date -u», l. 2) says «P-IDEAL-RED is not frozen yet.» (l. 3), while the freeze commit
0ebddcf5 is 19:30:17Z (the Lead's routing commit 2799f0dd, «P-IDEAL-RED frozen and routed to both referees», is 21:04:53Z);
REFEREE l. 7 «My pre-check of the lane lemma (docs/referee/R-XI-NEW-precheck.md, a4e7b4a9) was written before the packet.» reads as
before REFEREE received the packet (my reading); the pre-check is history and no verdict rests on it.
(12) Excluded: L-NEW boxes 151-152 (NEST-BARE, E_min, PMDIFF, STABLE-PATH; lane-level, unreviewed; 76903103, e40bae1f, 4f6b6d6e);
docs/new/N5-IDEAL-STATE.md and boxes 144-149 (lane sources, packet l. 4); every item packet §9 EXCLUDES (l. 246-252: R178's real-N5
XI-NEW, the 2-wide ladder identity and «IDEAL-ACYC-POLY ⟺ Σ_l F_l poly», box 148's opening dichotomy, box 147's degree-D TOP forms,
every CONJECTURE and DEAD item of N5-IDEAL-STATE §2-§3); the box-148 form of RECURSION (l. 227-228, not claimed); F-2's remark; §9
READING; the referees' tools. Not part of this entry.
(13) Commits: lane (claude/l-new): 0ebddcf5 (2026-11-03T19:30:17Z; freeze: packet +261, box150/check.py +214, box150/rand.py, the 200
genomes, check.sh block w99 +6, notebook +29) → b115ff3a (22:30:34Z; fixes entry 1 +68, L-1 +1) → ffeb9736 (23:39:27Z; fixes entry 2
+15, L-2 +1); later 4f6b6d6e (2026-11-04T00:19:54Z; box 152; no P-IDEAL-RED file touched). REFEREE (claude/referee): 798f9308
(19:59:51Z; successor 23 handover check) → a4e7b4a9 (20:23:37Z; XI-NEW pre-check, new file 112 lines, sha1 67f57485…; scratch
xinew_probe.py, xinew_logs/) → a71540d5 (20:46:41Z; report, new file 192 lines, sha1 63f0d0c7…; scratch xinew_lane.py, logs) →
d8f25ef2 (23:02:24Z; §C, +73; 265 lines, sha1 8f1c9a47…; scratch deg3_probe.py) → 0d2fef9f (2026-11-04T00:09:07Z; §C addendum 1, +30;
295 lines, sha1 b5d3801e…). REFEREE-2 (claude/referee-2): 2f9b6f5c (2026-11-03T20:47:29Z; report, new file 183 lines, sha1
d90a74bd…; R2-P-IDEAL-RED/ideal_check.py, logs/) → ca757330 (23:03:25Z; R2-P-IDEAL-RED-L1.md, new file 92 lines, sha1 522315c3…) →
f81c6e57 (2026-11-04T00:09:46Z; R2-P-IDEAL-RED-L2.md, new file 64 lines, sha1 644feeee…). R2-P-IDEAL-RED.md is unchanged at f81c6e57
(sha1 d90a74bd…, by cmp). Lead: 8c37ab0b (D19 + L47). CHECKER: none yet (C116). Trunk: see the header.
(14) Placement: see (0). DEAD-ENDS ROW: none proposed; the Lead decides. L-2 has no DEAD and kills no conjecture of RESULTS or GAPS. The
lane reported three corrections of its own lane statements while re-proving (notes/L-NEW.md l. 22-26 at 0ebddcf5 and ffeb9736): (1)
«XI-NEW (ii)'s «Xi is monotone» needs Lemma MONO» (a missing step in L-RED R178's lane proof, REFEREE's XI-G1; closed by MONO, nothing
killed); (2) «Box 148 recursion «U*(n) <= sum_(p<n)(U*(p)+1)» omits» «the boundary steps» (a gap in a lane proof; the box-148 form is
«unviolated on data (REC148 0), not claimed» (notes l. 24; packet l. 227-228 «The box 148 form is not violated on the data (§9,
REC148 0) but is NOT claimed.»); nothing refuted); (3) «Box 147 / 148 «any degree» for TOP-MONO /
INTERVAL-RESTRICT is wrong as stated (an unstable mover may stay unstable after a» «move at degree >= 3); packet restricts them to
degree <= 2.» Of the three, only (3) is a refuted statement, and only for TOP-MONO is a failure counted: REFEREE-2 N-2 «TOP-MONO
failing: X_TOP_deg3, 21 / 78,579 / 23,151» (l. 144) and REFEREE «TOP-MONO fails 8,105 times» (§C l. 215-216); no count or instance is
given for INTERVAL-RESTRICT at degree ≥ 3 (REFEREE-2's table l. 159 has «— (degree 3)» for restricted intervals on the champions;
run2.log reports «restr_intervals 439» and «VIOLATIONS 0» on its degree-≤-4 set; whether RESTR runs on its degree-≥3 genomes is not
stated). KEYFLIP's degree-≥3 failures (35 / 2,473 / 696; 343) test an extension of KP (G-6). WHY NO ROW (proposal): (a) the refuted
forms are lane statements of boxes 147 / 148 that never entered a packet, a line or RESULTS; the packet EXCLUDES them (l. 251) and
states the hypothesis; (b) a Dead-ends row needs «the exact obstruction or counterexample and the instance that killed it» (RESULTS l.
10168): the obstruction is named (packet l. 251, «when an unstable mover stays unstable after a move»), but no instance file is named in
the packet, the fixes or either report (the champions are named as a set, «7 R178 champions»); (c) the lane notebook records the
corrections (l. 22-26); it names the obstruction of (3) but no instance either, so CLAUDE.md's «Record every dead end with the exact
obstruction and the instance that killed it» is met for (3) only through the referees' counts. IF the Lead wants a row, it needs from
L-NEW or REFEREE-2 one named degree-3 genome and step at which TOP-MONO's tuple does not fall although RANK_t ≤ k (or rises), re-checked
by a referee.
### R105 [refereed-only] In the IDEAL model of RESULTS R104 (the model first stated in L-RED R178 §1), on acyclic Ξ-graphs (premise: R104's definition of the model only, no theorem of R104 used; any number of movers per level; π any topological order of the Ξ-graph, N movers, M options, T steps of a run, h_t a least-level mover of step t, y_t the largest-π mover of step t, c_s(x) the number of options of x strictly better than its current one, KP_s(x) the key-preferred option under the keys of s), at any degree: (ENC) the Ξ-order of β-sets is the order of the integers Σ ±2^rank (+ for even parity), so, with ε(x, k) := ±2^rank(x, k) (+ for even parity), the value of option (x, k) is ε(x, k) plus the current value of its Ξ-target (ε(x, k) alone if the Ξ-target is the exit X); (LOCAL) an option's value depends only on the states on its chain, a key only on the states below its level; (MONO) the current Ξ-value of every mover never decreases along a run; (XI-NEW) for t ≥ 2 every least-level mover h of step t moves to an option w ∉ A_(s_(t−2))(h) (A_s(h): h's current option under s and its options strictly better under s); (RISE) that option's value rose strictly at step t − 1, and some strict Ξ-descendant of h on its chain under s_(t−2) moved at step t − 1; (CHAIN-BACK) if step t ≥ 2 is chained (h_(t−1) lies on the chain under s_(t−2) of the option h_t takes), then π(h_t) < π(h_(t−1)), and T ≤ N (1 + U) with U the number of unchained steps t ∈ [2, T]; (U-EQ) U ≤ max(T − 1, 0), so T is polynomial in N + M iff U is; (DECREMENT) c(y_t) ≥ 1 before step t, c(y_t) falls at step t, and no mover with π > π(y_t) changes its option or its c; (EXACT-ENERGY) with D the largest degree, Σ_x c(x) D^π(x) falls at every step, so T ≤ D^N − 1; and at degree ≤ 2 only: (KEYFLIP) moves(x) ≤ 1 + KF_x with KF_x the number of steps at which KP(x) changes, so T ≤ N + KF and KF ≤ N T (T polynomial iff KF is); (TOP-MONO) for every k ≥ 1, the tuple TOP_k of the k largest π of unstable movers (padded with −1 to length k) falls lexicographically at step t iff RANK_t := 1 + #(unstable movers above y_t before the step) ≤ k, and is unchanged otherwise; (RANK-BOUND) for k ≥ 1, #(steps with RANK ≤ k) ≤ Σ_(j ≤ k) C(N, j) − 1, so U ≤ Σ_(j ≤ R) C(N, j) − 1 with R the largest RANK over unchained steps (R := 0 if U = 0); (INTERVAL-RESTRICT) on an interval of states where TOP_k is constant with k-th entry p, every mover of every interior step has π < p, the genome in which every mover with π ≥ p keeps only its option at the interval's first state runs exactly those states as a prefix of its run from that state, and chained / unchained labels agree from the interval's third state on (step a + j of the run against step j of the restricted run, for j ≥ 2); (INTERVAL-CHARGE) for r ≥ 2, #(steps with RANK = r) ≤ (N − r + 1)(1 + #(steps with RANK ≤ r − 1)); (RECURSION) with U*(n) the largest U over degree-≤-2 genomes with at most n degree-2 movers, U*(n) ≤ n + Σ_(p < n) (U*(p) + 1) (2026-11-03) — a REDUCTION / EQUIVALENCE statement inside the IDEAL model; bounds nothing polynomially (EXACT-ENERGY and RECURSION are exponential bounds; no bound on U or KF is claimed); degree ≤ 2 is needed for KEYFLIP and TOP-MONO (DATA, REFEREE-2 N-2); Ξ-cyclic genomes, the real-N5 form of XI-NEW and the 2-wide-ladder identity KF_x = F_(lev(x)−1) are not covered; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (DATA: 0 violations of every inequality on 46 corpus genomes and 75,518 all-start runs of 200 random genomes, experiments/new/box150/check.py) (P-IDEAL-RED, docs/new/P-IDEAL-RED.md with its fixes entry 1, docs/new/P-IDEAL-RED-fixes.md; L-NEW successor 50), CHECKER PASS (docs/checker/C116.md, checker PENDING)
- Object (L-NEW successor 50, Opus 5.5, D14 / D18 / D19; frozen, unchanged during review): packet P-IDEAL-RED, docs/new/P-IDEAL-RED.md,
  sha1 06f2c18609e355a1e62c138c420bd49dc401cae4, 261 lines (l-new freeze 0ebddcf5, 2026-11-03T19:30:17Z, the file's only commit;
  identical at b115ff3a, ffeb9736 and 4f6b6d6e). Both referees measured the sha1 (REFEREE l. 3 «Object: claude/l-new 0ebddcf5,
  docs/new/P-IDEAL-RED.md, sha1 06f2c18609e355a1e62c138c420bd49dc401cae4, 261 lines.»; REFEREE-2 §0 l. 9-10 «sha1
  06f2c18609e355a1e62c138c420bd49dc401cae4,» «261 lines. Re-hashed: match.»). Title (l. 1): «Packet P-IDEAL-RED (box 150): reductions
  inside the IDEAL-ACYC model (MONO, XI-NEW, CHAIN-BACK, KEYFLIP, DECREMENT, TOP-MONO, RANK-BOUND, INTERVAL-RESTRICT, INTERVAL-CHARGE,
  RECURSION)». Status (l. 5-6): «Labels: PROVED (L-NEW 50, unrefereed) / DATA / READING.» «Not a TARGET.md claim. Every statement is
  about the IDEAL-ACYC model only. No polynomial bound is claimed anywhere. G-N5-TIME stays OPEN.» To sign: the sixteen statements of
  §1-§8 (table l. 8-19); §9 «DATA / READING (not to sign)». Sections: §0 the model (l. 28-61), §1 ENC and LOCAL (l. 63-85), §2 MONO (l.
  87-94), §3 XI-NEW and RISE (l. 96-115), §4 CHAIN-BACK and U-EQ (l. 117-128), §5 KEYFLIP and KF-EQ (l. 130-141), §6 DECREMENT and
  EXACT-ENERGY (l. 143-157), §7 TOP-MONO and RANK-BOUND (l. 159-174), §8 INTERVAL-RESTRICT, INTERVAL-CHARGE and RECURSION (l. 176-230),
  §9 machine check, exclusions, TARGET diff (l. 232-261). «This packet governs: every» «proof below is written out in full here and is
  checked against this text only.» (l. 4-5).
  Fixes: docs/new/P-IDEAL-RED-fixes.md, fixes entries 1-2 (append-only; entry 1 at b115ff3a, 68 lines, sha1 727b6f0c…; entry 2 at
  ffeb9736, 83 lines, sha1 2e8c3630b16cf6cd33564433da62c0fbba1f1f4e, whose first 68 lines are entry 1 unchanged); «Where a fix is
  applied, the packet reads with the new text in place of the old. No other» «change.» (l. 5-6). Entry 2 changes the line only
  («line L-1 is left unchanged. Packet and entry 1 unchanged.», l. 71). The packet read with its fixes is the text of record.
  The RESULTS line is L-2, 65ba7ca7fd6d4cb6b0de1d1c918ec181ff78fbe5 (docs/new/P-IDEAL-RED-line-L2.txt, l-new ffeb9736,
  2026-11-03T23:39:27Z, the file's only commit; fixes entry 2). The title is L-2 verbatim, with nothing inserted (its date parenthesis
  «(2026-11-03)» and its source note are the line's own; the source note names «fixes entry 1», and REFEREE-2 L2 l. 51-52 reads it:
  «Entry 2 holds just this line's word diff, so nothing in the packet's reading» «changes. That is acceptable.»). L-2 MATCHES at both
  referees: REFEREE §C addendum 1 (0d2fef9f) l. 295 «VERDICT: line L-2 MATCHES. All 16 statements are SIGNED with fix entry 1 in
  place.»; REFEREE-2 R2-P-IDEAL-RED-L2.md (f81c6e57) l. 2 «Verdict: **MATCHES**.», l. 57 «It matches the packet read with fixes entries
  1-2. Every clause is a signed statement with its exact hypotheses.»
  L-2 differs from the line at L-1 by exactly the ten word changes of fixes entry 2 (l. 73-83): ε defined and the exit case in ENC;
  A_s defined in XI-NEW; RISE's chain «under s_(t−2)»; U over «steps t ∈ [2, T]»; the pad of TOP_k; «for k ≥ 1» and «R := 0 if U = 0»
  in RANK-BOUND; INTERVAL-RESTRICT's labels «from the interval's third state on»; the R178 attribution worded «the model first stated
  in». REFEREE §C addendum 1 l. 274-275: «gives exactly 10 hunks. They equal entry 2's list and nothing else» «differs:»; REFEREE-2 L2
  l. 56 «L-2 (65ba7ca7) = L-1 + exactly the four required changes + the optional items 5-8 (byte test True).»
  History. At L-1 (44d0287a5d304aa5342b8cd98c6cbccb9e8af6b3, docs/new/P-IDEAL-RED-line-L1.txt, l-new b115ff3a, 2026-11-03T22:30:34Z,
  with fixes entry 1; the first line of this packet), REFEREE §C (d8f25ef2) l. 263 «Line L-1: NOT YET. It matches once L-1a, L-1b,
  L-1d and L-1e are applied.» and REFEREE-2 R2-P-IDEAL-RED-L1.md (ca757330) l. 3 «line L-1 **does NOT match yet**: three exact word
  changes are REQUIRED»: at L-1 ε and A were not defined in the line and ENC's exit case was missing (REFEREE L-1a, L-1b = REFEREE-2
  L-R1, L-R2), U's range was not bound (REFEREE L-1d; REFEREE-2 L2 l. 63 «I concur with REFEREE L-1d, which I had missed in L-1
  (unbound range of U).»), and «labels agree there» overstated INTERVAL-RESTRICT (iii) (L-1e = L-R3). Neither referee found a hole in a
  proof; the packet's false texts were U-EQ's «U ≤ T − 1» at T = 0 (REFEREE U-1 = REFEREE-2 N-1) and a false «Does NOT claim» remark in
  MONO (REFEREE IR-1), both fixed in entry 1 (F-1, F-2).
  Setting (packet §0, l. 28-61; RESULTS R104's definition restated): a genome G has N movers x (N ≥ 1) with levels lev(x) and deg(x) ≥
  1 options (x, k), M := Σ deg(x); each option has a W-target of level lev(x) − 1 (none at level 0), a Ξ-target (a mover or the exit
  X), a β with a rank rk(x, k) and a parity par(x, k) (ranks distinct) and a gate index (distinct); and a start s_0 (l. 29-35). The
  Ξ-graph and IDEAL-ACYC (l. 37-39), with a topological order π: «Every statement holds for every» «such π.» (l. 38-39). Under a state
  s: the chain and the Ξ-value Ξ_s(x, k) (l. 40-44); cur_s(x), A_s(x) := {s(x)} ∪ {k : Ξ_s(x, k) ▷ cur_s(x)}, c_s(x) := the number of
  elements of A_s(x) minus 1, «x is UNSTABLE at s iff c_s(x) ≥ 1» (l. 45-46); keys under s, gate indices of the W-target chain,
  lowest level first (l. 47-50). The step (l. 51-55) moves every mover to the key-least option of its availability set under the OLD
  state, keys read under the NEW state, root-first; «T := the number of steps (R104's L(G)).» (l. 54). Mv_t, h_t (a least-level mover of
  Mv_t, «any fixed tie rule works»), y_t (the largest-π mover of Mv_t) and moves(x) (l. 56-59). «Degree ≤ 2» means deg(x) ≤ 2 for every
  mover; «No width hypothesis is made anywhere» (l. 60).
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 23 (report a71540d5; §C on fixes entry 1 and L-1 d8f25ef2; §C
  addendum 1 on L-2 0d2fef9f); REFEREE-2 successor 26 (report 2f9b6f5c; R2-P-IDEAL-RED-L1.md ca757330; R2-P-IDEAL-RED-L2.md
  f81c6e57)). Items (a)-(p) are SIGN in both verdict tables (REFEREE "## 0. Verdicts" l. 10-29 of R-P-IDEAL-RED.md; REFEREE-2 "## 1.
  Verdict table" l. 28-47 of R2-P-IDEAL-RED.md), U-EQ with fixes F-1, and both verdicts stand on fixes entry 1 (REFEREE §C l. 218 «After
  entry 1, my verdicts: all 16 statements SIGNED, U-EQ included.»; REFEREE-2 L1 l. 89 «F-1 to F-4 are correct.»); the table is to-check
  (4). All hold for every IDEAL genome with an acyclic Ξ-graph (any width, π any topological order, any fixed tie rule for h_t) and for
  every step of its IDEAL run; (a)-(g), (j) and (k) at any degree;
  (h), (i) and (l)-(p) at degree ≤ 2 only. No item bounds a count polynomially.
  (a) Lemma ENC (§1, l. 64-74): «Put ε(x, k) := (−1)^par(x, k) · 2^rk(x, k) and, for a finite set P of β's,» «e(P) := Σ_(β ∈ P) ε(β).
      Then for P ≠ Q: P ▷ Q ⟺ e(P) > e(Q).»; consequence (l. 72): «v_s(x, k) = ε(x, k) if xt(x, k) = X, and v_s(x, k) = ε(x, k) +
      v_s(y, s(y)) with y = xt(x, k) otherwise.» Cells: REFEREE «SIGN» (l. 13; §2 l. 59-61); REFEREE-2 «**SIGN**» (l. 31; §2 l. 52-56).
  (b) Lemma LOCAL (§1, l. 75-85): «(a) If two states s, s′ agree on every mover of the chain of (x, k) under s other than x, then the
      chains of (x, k) under s and s′» «are equal and Ξ_s(x, k) = Ξ_(s′)(x, k).»; (b) the same for every k when s, s′ agree on every
      strict Ξ-descendant of x; «(c) key_s(x, k) = key_(s′)(x, k) whenever s and s′ agree on every mover of level < lev(x).» Cells:
      REFEREE «SIGN» (l. 14; §2 l. 62-65); REFEREE-2 «**SIGN**» (l. 32; §2 l. 57-60).
  (c) Lemma MONO (§2, l. 88-94, with fixes F-2): «For every step t and every mover x: cv_(s_t)(x) ≥ cv_(s_(t−1))(x), i.e.» «the
      current Ξ-value of every mover never gets worse along a run.» F-2 (fixes l. 16-25) deletes the false parenthetical of l. 94 and
      adds an unsigned remark, not in L-2. Cells: REFEREE «SIGN», with «REQUIRED text fix IR-1: the «Does NOT claim» parenthetical is
      false» (l. 15; §2 l. 66-75), and «F-2 = IR-1: CLOSED.» (§C l. 205); REFEREE-2 «**SIGN**» (l. 33; §2 l. 61-64).
  (d) Lemma XI-NEW (§3, l. 97-105): «Let 2 ≤ t ≤ T, let h be ANY mover of» «least level in Mv_t, and w := s_t(h). Then w ∉
      A_(s_(t−2))(h).» (acyclicity is not used). Cells: REFEREE «SIGN» (l. 16; §2 l. 76-79); REFEREE-2 «**SIGN** (acyclicity indeed
      unused)» (l. 34; §2 l. 65-71).
  (e) Corollary RISE (§3, l. 106-115): «(a) v_(s_(t−1))(h, w) > v_(s_(t−2))(h, w): the value of option (h, w) rose strictly at step t
      − 1;»; «(b) the set Z_t of movers z ≠ h on the chain of (h, w) under s_(t−2) with z ∈ Mv_(t−1) is nonempty;»; «(c) every z ∈
      Z_t is a strict Ξ-descendant of h, so π(z) > π(h).» Cells: REFEREE «SIGN» (l. 17; §2 l. 80-83); REFEREE-2 «**SIGN**» (l. 35; §2
      l. 72-76).
  (f) Theorem CHAIN-BACK (§4, l. 118-125): a step t ∈ [2, T] is CHAINED iff h_(t−1) lies on the chain of (h_t, s_t(h_t)) under
      s_(t−2), U := the number of unchained steps (l. 118-119); «(i) If step t is chained, then π(h_t) < π(h_(t−1)).» «(ii) T ≤ N (1
      + U).» Cells: REFEREE «SIGN» (l. 18; §2 l. 84-86); REFEREE-2 «**SIGN**» (l. 36; §2 l. 77-81).
  (g) Corollary U-EQ (§4, l. 126-128, as fixed by F-1, fixes l. 12): «Corollary U-EQ. U ≤ max(T − 1, 0) and T ≤ N (1 + U). So for any
      family of IDEAL-ACYC runs: T is bounded by a polynomial in N + M iff U is.» Cells: REFEREE «SIGN WITH GAP U-1» (l. 19; §2 l.
      87-90), CLOSED by F-1 (§C l. 202-204 «U-EQ is now SIGNED without gap.»); REFEREE-2 «**SIGN** with precision N-1» (l. 37; §2 l.
      82-84), «**F-1 (U-EQ, REQUIRED) ✓.**» (L1 l. 20).
  (h) Lemma KEYFLIP (§5, l. 131-137; degree ≤ 2): KF_x := the number of steps at which KP(x), the option of x with the smaller key,
      changes (l. 131-132); «moves(x) ≤ 1 + KF_x for every mover x.» (l. 133). Cells: REFEREE «SIGN» (l. 20; §2 l. 91-93); REFEREE-2
      «**SIGN**» (l. 38; §2 l. 85-90).
  (i) Corollary KF-EQ (§5, l. 138-141; degree ≤ 2): «T ≤ Σ_x moves(x) ≤ N + KF, and KF ≤ N · T (each KF_x ≤ T).» Cells: REFEREE
      «SIGN» (l. 21; §2 l. 94); REFEREE-2 «**SIGN**» (l. 39; §2 l. 91-93).
  (j) Lemma DECREMENT (§6, l. 144-151): with y := y_t, «(a) c_(s_(t−1))(y) ≥ 1; (b) c_(s_t)(y) < c_(s_(t−1))(y); (c) c_(s_t)(x) =
      c_(s_(t−1))(x) and s_t(x) = s_(t−1)(x) for every x» «with π(x) > π(y).» Cells: REFEREE «SIGN» (l. 22; §2 l. 95-98); REFEREE-2
      «**SIGN**» (l. 40; §2 l. 94-98).
  (k) Corollary EXACT-ENERGY (§6, l. 152-157): «Let D := max_x deg(x) ≥ 2 and E(s) := Σ_x c_s(x) · D^π(x). Then E(s_t) < E(s_(t−1))
      at every step.» «Hence T ≤ E(s_0) ≤ D^N − 1.» An exponential bound. Cells: REFEREE «SIGN» (l. 23; §2 l. 99-101); REFEREE-2
      «**SIGN** (D ≥ 2 as stated; D = 1 gives T = 0 trivially)» (l. 41; §2 l. 99-102).
  (l) Corollary TOP-MONO (§7, l. 160-167; degree ≤ 2): with S(s) the unstable set, TOP_k(s) the k largest π on S(s), padded with −1,
      and RANK_t := 1 + #(movers of S(s_(t−1)) above π(y_t)) (l. 160-161): «For every k ≥ 1 and step t: if RANK_t ≤ k then TOP_k(s_t)
      < TOP_k(s_(t−1)); if RANK_t > k then» «TOP_k(s_t) = TOP_k(s_(t−1)).» Cells: REFEREE «SIGN» (l. 24; §2 l. 102-104); REFEREE-2
      «**SIGN**» (l. 42; §2 l. 103-107).
  (m) Corollary RANK-BOUND (§7, l. 168-174, with fixes F-3 P-1; degree ≤ 2): for every k ≥ 1, the number of steps t with
      RANK_t ≤ k is at most Σ_(j=0..k) C(N, j) − 1 (l. 168); with R := the largest RANK_t over the unchained steps («R := 0 if U =
      0; that case is trivial, not an instance of k ≥ 1», fixes l. 34), U ≤ Σ_(j=0..R) C(N, j) − 1. Cells: REFEREE «SIGN», «optional P-1
      (the R = 0 case)» (l. 25; §2 l. 105-109); REFEREE-2 «**SIGN**» (l. 43; §2 l. 108-111).
  (n) Lemma INTERVAL-RESTRICT (§8, l. 177-201, with fixes F-3 P-2; degree ≤ 2): on [a, b) with TOP_k(s_t) = TOP_k(s_a) for a ≤ t < b
      and p := the k-th entry of TOP_k(s_a), «(i) For every step t with a < t < b, every mover x ∈ Mv_t has π(x) < p.»; (ii) the
      genome H in which every mover with π(x) ≥ p keeps only its option s_a(x), with start s_a, is an IDEAL-ACYC genome of degree ≤ 2
      whose first b − a states are s_a, …, s_(b−1) (F-3 P-2: «(a trimmed mover's single option is identified with its option s_a(x)
      of G, which it keeps at every state of [a, b) by (i)).»); «(iii) For a + 2 ≤ t < b, step t of G's run is chained iff step t − a
      of H's run is chained.» Cells: REFEREE «SIGN», «optional P-2 (option identification between G and H)» (l. 26; §2 l. 110-118);
      REFEREE-2 «**SIGN**» (l. 44; §2 l. 112-121).
  (o) Corollary INTERVAL-CHARGE (§8, l. 202-209; degree ≤ 2): «For every r ≥ 2:», the number of steps t with RANK_t = r is
      at most (N − r + 1) · (1 + the number of steps t with RANK_t ≤ r − 1) (l. 203). Cells: REFEREE «SIGN» (l. 27; §2 l.
      119-122); REFEREE-2 «**SIGN**» (l. 45; §2 l. 122-126).
  (p) Corollary RECURSION (§8, l. 210-230, with fixes F-3 P-3; degree ≤ 2): with n := the number of degree-2 movers and U*(n) := the
      largest U over all degree-≤-2 IDEAL-ACYC genomes with at most n degree-2 movers and all their starts (finite by EXACT-ENERGY),
      «U*(n) ≤ n + Σ_(p=0..n−1) (U*(p) + 1).» (l. 216-218); its first bullet bounds U(G) by the U of the restricted runs on
      the maximal TOP_1-constant intervals, its second orders their entries p_i.
      The box-148 form without the boundary steps is «NOT claimed» (l. 227-228). Cells: REFEREE «SIGN», «optional P-3 (the index of
      the sum is a count, not a position)» (l. 28; §2 l. 123-132); REFEREE-2 «**SIGN**» for «Corollary RECURSION (degree ≤ 2), all
      three bullets» (l. 46; §2 l. 127-136).
  Both, verbatim: REFEREE l. 133 «None of §2's checks found a hole in a proof. The only false text is IR-1 (a remark) and U-1 (an edge
  case of one inequality).»; REFEREE-2 l. 49 «No gap. One precision (N-1), two notes (N-2, N-3).» The RESULTS line (L-2) states
  (a)-(p) with KF-EQ inside KEYFLIP's clause and RECURSION's third bullet, and nothing wider (to check (4)); REFEREE §C addendum 1 l.
  291-292 «Every clause is a signed statement with its exact hypotheses: acyclic Ξ-graphs; any degree for ENC to EXACT-ENERGY; degree ≤
  2» «for KEYFLIP to RECURSION; any width.»
- Premise: RESULTS R104's DEFINITION of the IDEAL model and of the Ξ-graph, and nothing else. L-2: «premise: R104's definition of the
  model only, no theorem of R104 used». Packet l. 22-25: «LANDED: RESULTS R104 (P-N5-REALIZE), ONLY its definition of the IDEAL model
  and of the Ξ-graph, restated in §0 below. No theorem» «of R104 (REALIZE, REAL-IDEAL) is used. No other RESULTS entry is used.»;
  «Not used: L-RED R178 (its Lemma XI-NEW is re-proved in full in §3; the lane text is not a premise), docs/lit, docs/sources, any»
  «other lane file. No outside source is cited.» REFEREE §1 l. 36 «The packet declares a single premise: RESULTS R104's DEFINITION of
  the IDEAL model and of the Ξ-graph. No theorem of R104 is used.», l. 42 «No docs/lit premise is used (lesson C115 E-1).», l. 43-45
  (the dependency order «has no cycle»), l. 46-56 (§0 against R104's statement clause by clause, «All agree.»); REFEREE-2 §0 l. 11
  «**Premise route ✓.** The only premise is RESULTS R104's DEFINITION of the IDEAL model and the Ξ-graph.», l. 17-18 «Two additions are
  not R104 data but harmless: a topological order π, and the tie rule for h_t.», l. 19 «No theorem of R104 is used. No other RESULTS
  entry is used. Nothing comes from docs/lit, docs/sources or a lane file.» L-RED R178 is named in L-2 only as the model's first
  statement, an attribution (REFEREE-2 L1 l. 67-68 «is R104's own attribution of the» «model, not a premise ✓.»). Lemma XI-NEW, a lane
  lemma of L-RED R178, is re-proved in full in packet §3; REFEREE's pre-check of the lane text (docs/referee/R-XI-NEW-precheck.md,
  a4e7b4a9) is history, and its gap XI-G1 (monotonicity used, not proved) is closed by MONO (REFEREE l. 142 «XI-G1 (monotonicity proof
  missing in R178): CLOSED by §2 MONO, the same induction as my pre-check §3.»), its XI-G2 (R178's real-N5 half) is EXCLUDED (l. 143).
- L41 and L43. The proofs are L-NEW successor 50's (packet l. 5). F-1's corrected inequality, suggested by both referees (U-1, N-1), is
  justified in the fix by a count from the packet's definition (fixes l. 13); F-2's remark is unsigned and not in L-2. Nothing
  referee-originated is a premise or a proof step of the entry (my reading; neither referee mentions L41). No DEAD (L43): L-2's «degree
  ≤ 2 is needed for KEYFLIP and TOP-MONO (DATA, REFEREE-2 N-2)» is DATA on explicit failing runs, REFEREE-2 L1 l. 65-66 «these» «are
  explicit failing instances, so L43 is not triggered.»
- Fixes (docs/new/P-IDEAL-RED-fixes.md, L-NEW successor 50, append-only, fixes entries 1-2; at ffeb9736 83 lines, sha1
  2e8c3630b16cf6cd33564433da62c0fbba1f1f4e, the version both referees checked for L-2; entry 1 alone at b115ff3a, sha1 727b6f0c…, the
  version both referees checked at L-1).
  - Entry 1 (l. 1-68, «fix round after REFEREE 23 and REFEREE-2 26»): F-1 (REQUIRED; REFEREE U-1 = REFEREE-2 N-1): U-EQ «U ≤ max(T −
    1, 0)» (l. 12); F-2 (REQUIRED; REFEREE IR-1): MONO's false «Does NOT claim» parenthetical replaced by «Remark (not a signed
    statement): every option's value is non-decreasing too» (l. 20) and «Does NOT claim: anything on Ξ-cyclic genomes.» (l. 22);
    F-3 (optional wording; REFEREE P-1, P-2, P-3): RANK-BOUND's R = 0 case, INTERVAL-RESTRICT's option identification, RECURSION's
    count n_i; F-4 (optional; REFEREE-2 N-2): a DATA item in §9 on degree ≥ 3 genomes. REFEREE §C l. 265 «The fixes: entry 1 CLOSES U-1
    and IR-1, and P-1 to P-3 are correct. All 16 statements are SIGNED.»; REFEREE-2 L1 l. 3 «Verdict: fixes **CORRECT**».
  - Entry 2 (l. 70-83, «line L-2; REFEREE L-1a/b/d/e + REFEREE-2 L-R1/R2/R3»): L-2 and its word diff against L-1, ten hunks; «Packet
    and entry 1 unchanged.» (l. 71).
  No fix changes a signed inequality other than F-1's correction of U-EQ at T = 0 (to check (8)).
- Not signed: F-2's remark («Remark (not a signed statement)», fixes l. 20); §9 machine check, exclusions and TARGET diff (packet l. 19
  «DATA / READING (not to sign)»); §9 READING (l. 259-261). OPEN, not claimed: any bound on U, KF or T beyond EXACT-ENERGY's and
  RECURSION's exponential ones (packet l. 127 «Does NOT claim: any bound on U (CONJECTURE U-LIN of N5-IDEAL-STATE §3 is NOT part of this
  packet), any bound on T»); every CONJECTURE of N5-IDEAL-STATE §3 (EXCLUDED, l. 252); G-N5-TIME.
- Referee strengthening (NOT part of this entry; remarks of one referee):
  (i) REFEREE §2 l. 69-75 (IR-1) and §C l. 207-208: every option's value, not only the current one, is non-decreasing along a run
      («The new Remark is TRUE: ENC's recursion plus MONO on the Ξ-target, which is my report's §2 argument.»); unsigned (F-2).
  (ii) REFEREE-2 N-3 (l. 147-148): «Every statement holds for every such π» and «any fixed tie rule works» are tested under 3 random
       topological orders per genome and both tie rules, 0 violations.
  (iii) REFEREE-2 N-2 and REFEREE §C (F-4): the degree ≤ 2 hypotheses of KEYFLIP and TOP-MONO are needed on the data (Data below), while
       ENC, LOCAL, MONO, XI-NEW, RISE, CHAIN-BACK, DECREMENT and EXACT-ENERGY show 0 violations at every degree (N-2 l. 145-146).
  (iv) REFEREE §2 l. 77-78 and REFEREE-2 table l. 34: XI-NEW's proof does not use acyclicity.
- Honest limits: (i) a REDUCTION / EQUIVALENCE statement inside the IDEAL model only: it bounds nothing polynomially; EXACT-ENERGY (T ≤
  D^N − 1) and RECURSION are exponential bounds; no bound on U or KF is claimed; G-N5-TIME stays open; not M3, not a step-4 pass, not a
  TARGET.md claim. (ii) Every statement is about the step sequence of R104's IDEAL model on acyclic Ξ-graphs; nothing is said about a
  real N5 run or a parity game. The only link to N5 is R104's own Corollary REAL-IDEAL, which this entry neither uses nor restates
  (packet l. 256-258; REFEREE §6 l. 176 «The only link to the fleet question is R104's own Corollary REAL-IDEAL, which this packet does
  not use or restate.»). (iii) Not covered: Ξ-cyclic genomes; R178's real-N5 form of XI-NEW («needs the TWO-FIX window and the corner
  exclusion; not written here as a complete proof», packet l. 247); the 2-wide ladder identity KF_x = F_(lev(x)−1) (l. 248-249); box
  148's opening dichotomy (l. 250); box 147's degree-D TOP forms (l. 251); every CONJECTURE of N5-IDEAL-STATE §3 (l. 252). (iv) KEYFLIP,
  KF-EQ, TOP-MONO, RANK-BOUND, INTERVAL-RESTRICT, INTERVAL-CHARGE and RECURSION hold at degree ≤ 2 only; at degree ≥ 3 KEYFLIP (with KP
  read as the key-least option) and TOP-MONO fail on the data (DATA below; packet l. 141 «there a mover may move twice without a key
  flip, to a key-smaller option that becomes available later»). (v) The equivalences of growth classes (U-EQ, KF-EQ) move the open
  question from T to U or KF; they do not decide it. (vi) ENC's integers and EXACT-ENERGY's weights are proof devices, not computed
  quantities (REFEREE §6 l. 175 «EXACT-ENERGY's integers and ENC's 2^rk are proof devices, not computed quantities. TARGET §3 (bit
  cost) is not engaged.»). (vii) Premise: RESULTS R104's definition only; no R104 theorem, no lit note, no lane file. No Lean.
- Data (DATA, not proof): experiments/new/box150/check.py (l-new 0ebddcf5, sha1 019de0f7b36dcbd47743b3d27b4a1a93549d574b, 214 lines;
  unchanged at b115ff3a, ffeb9736, 4f6b6d6e), wired into experiments/new/check.sh block w99 (l. 814-819, unchanged at those commits).
  Packet §9 (l. 233-245): its own simulator of §0 (Ξ-values through ENC's integers, keys under the new state), cross-checked against
  box139/paths.py run() (XSIM); per run the violations of every packet inequality where it is stated; «0 violations of every check on
  the 46 corpus genomes of boxes 140-149» (with the L-RED R188 pins x3_L8, g4_L12 and the L-RED R189 pins lag1, lag1u, lag2c_d4,
  nest_d3_L4 as IDEAL genomes; 386 steps) «and on 75,518 runs = every start of 200 random» «IDEAL-ACYC genomes (box150/rand.py seed 150;
  width 1-3, depth 1-4, degree 1-4: 107 of them have a mover of degree 3 or 4; 93,963» «steps). REC148 0 everywhere.» (l. 240-243).
  Negative controls (l. 244-245): «NEG=3 on the» «random genomes: XINEW 6, RISE 3, XSIM 8».
  The block's three outputs, reproduced by both referees and re-run for this draft (2026-11-04T00:49:10Z-00:49:35Z, from a `git
  archive` of 0ebddcf5's experiments/new, rc 0, byte-equal to the block's expected strings): «TOTAL genomes 46 runs 46 steps 386 XSIM 0
  TOPO 0 MONO 0 XINEW 0 RISE 0 CHAIN 0 KEYFLIP 0 DECR 0 TOPMONO 0 RBOUND 0 RESTR 0 ICHARGE 0 REC 0 VIOL 0 (info REC148 0)»; «TOTAL
  genomes 200 runs 75518 steps 93963 XSIM 0 TOPO 0 MONO 0 XINEW 0 RISE 0 CHAIN 0 KEYFLIP 0 DECR 0 TOPMONO 0 RBOUND 0 RESTR 0 ICHARGE 0
  REC 0 VIOL 0 (info REC148 0)»; NEG=3 «TOTAL genomes 200 runs 200 steps 138 XSIM 8 TOPO 0 MONO 0 XINEW 6 RISE 3 CHAIN 0 KEYFLIP 0 DECR
  0 TOPMONO 0 RBOUND 0 RESTR 0 ICHARGE 0 REC 0 VIOL 17 (info REC148 0)». REFEREE §5 l. 150 «Command: block w99 of
  experiments/new/check.sh, verbatim, run in a detached worktree of 0ebddcf5 (15 s).», l. 154 «All three equal the packet's §9 and the
  check.sh expected strings. MATCHES.»; REFEREE-2 §4 l. 165-168 (the same three lines «at 0ebddcf5»), l. 169 «also NEG=1 (XSIM 168) and
  NEG=2 (MONO 93, DECR 66, TOPMONO 101, RESTR 5) fire.»
  REFEREE (successor 23; own docs/referee/scratch/xinew_probe.py, sha1 592b304e0e377e6f7272dcc42879696a5c6eabee, «written from R104's
  TEXT», l. 161; it compares β-sets directly, so it also tests ENC): «On the 46 corpus genomes: per-file N and T EQUAL to check.py's on
  all 46 (max T 26, total 386).» (l. 164), «XI-NEW 0, all-option monotonicity 0, RISE strict rise 0.» (l. 165), «On the 200 random
  genomes from their stored starts: 132 steps, 0 / 0 / 0.» (l. 166); pre-check (a4e7b4a9) l. 97 «MUT 0, BIG=1, seeds 2-4: 4,500
  genomes, 1,925 checked steps (L up to 5), 0 violations, 0 monotonicity failures, 0 missing rises.»; degree ≥ 3 (deg3_probe.py, sha1
  88b7e346a9296864e9cd25a1f306e2ba457963ad; §C l. 215-216): «on 2,950 random degree-≥3 runs, KEYFLIP with KP = the key-least option
  fails» «343 times and TOP-MONO fails 8,105 times.» «Limit: the runs are short (T ≤ 26). The signatures rest on the proofs, and the
  DATA is a consistency check.» (l. 168).
  REFEREE-2 (successor 26; own docs/referee-2/R2-P-IDEAL-RED/ideal_check.py, sha1 3162722113d185663b3c964fce2db4f6fc4262b1, «written
  from the packet text», l. 152; logs/run1.log, run2.log): table l. 156-162, 0 violations on the 46 corpus genomes (386 steps, 15,699
  restricted intervals run), the 7 L-RED R178 champions (degree 3; 296 steps), the lane's 200 random genomes with every start for N ≤ 9
  (74,495 runs, 92,837 steps), its own 300 degree-≤-2 genomes (2,758 runs) and 200 degree-≤-4 genomes (33,104 runs); DONE l. 177-178
  «My own checker gives 0 violations on 110,410 runs, and its control fires.» (NEG=old: XINEW 6 on the lane's random genomes, 85 on the
  corpus, l. 164). Degree ≥ 3 (N-2, l. 141-146): «the KEYFLIP inequality with KP := the key-least option failing: X_KEYFLIP_deg3, 35 on
  the 7 R178 champions (degree 3), 2,473 on the» «lane's all-start runs, 696 on mine;», «TOP-MONO failing: X_TOP_deg3, 21 / 78,579 /
  23,151.»; the logs at 2f9b6f5c print these numbers.
  No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-P-IDEAL-RED.md: successor 23's report a71540d510c36d0dd8f4cf4497c23753c5251ac4
  (2026-11-03T20:46:41Z, new file, 192 lines, sha1 63f0d0c7bb9f3918dfddf7e33cd0650ff752756a, with scratch/xinew_lane.py and
  xinew_logs/): 15 statements SIGN, U-EQ SIGN WITH GAP U-1, REQUIRED IR-1 (l. 188-189); §C d8f25ef2a41eb4a61623ba966124d4252db11ce6
  (23:02:24Z, +73, l. 194-265; 265 lines, sha1 8f1c9a472169a7a1dee9e5a08a0a42678885d23c, with scratch/deg3_probe.py): fixes entry 1
  CLOSES U-1 and IR-1, all 16 SIGNED, at L-1 «Line L-1: NOT YET.» (l. 263); §C addendum 1 0d2fef9f8226a5dbf612a5e1529ee4707a214f96
  (2026-11-04T00:09:07Z, +30, l. 267-295; the file now 295 lines, sha1 b5d3801e925ec8f5ae85185a656097b203514a2c): «VERDICT: line L-2
  MATCHES.» (l. 295). Pre-check docs/referee/R-XI-NEW-precheck.md a4e7b4a98731e6696ae68e8d865b261b6fa76709 (2026-11-03T20:23:37Z, new
  file, 112 lines, sha1 67f57485a5f9104f3b6cbec8dbac6e2a1e30869e; not a signature).
  REFEREE-2 (successor 26): docs/referee-2/R2-P-IDEAL-RED.md 2f9b6f5c47ed775c43ae034c6753e0ee7d9f45f4 (2026-11-03T20:47:29Z, new file,
  183 lines, sha1 d90a74bdee2f29c323c5340eb995923c3330d773; with R2-P-IDEAL-RED/ideal_check.py and logs/): all 16 statements SIGN (l.
  31-46), «No gap.» (l. 49), U-EQ precision N-1; R2-P-IDEAL-RED-L1.md ca757330c8f408c35a9bf7bbc6558e49c07373be (23:03:25Z, new file, 92
  lines, sha1 522315c3f623c037566b19c175bccaf276e7176e): fixes «**CORRECT**», L-1 not yet (L-R1 to L-R3) (l. 3-4); R2-P-IDEAL-RED-L2.md
  f81c6e5775005b1cfad42eb7ec22099641960f55 (2026-11-04T00:09:46Z, new file, 64 lines, sha1 644feeee1479b30398d1c7ebd3601c025a17dfdb):
  «Verdict: **MATCHES**.» (l. 2) for L-2. Lane: freeze 0ebddcf5bc4f11fedd18b5cefffc78ff90464be9, fixes entry 1 and L-1
  b115ff3ab0ce89de8b19d2d6982640399ad268e3, fixes entry 2 and L-2 ffeb973670db02b59e6c89f406481979fc94121c.
  INDEPENDENCE: REFEREE l. 2 «Independent: I did not read docs/referee-2/.», §C l. 214 «F-4 (REFEREE-2 N-2 DATA, unsigned, §9): I did
  not read docs/referee-2/ for it.»; REFEREE-2 l. 4 «I opened nothing in docs/referee/. At 20:46Z, a names-only `git ls-tree` on
  origin/claude/referee found 0 files matching this packet.», l. 5 «My checker imports no lane code.»; REFEREE-2 L1 l. 15-16 read
  REFEREE's report «After my report was pushed (2f9b6f5c)». REFEREE's report (20:46:41Z) precedes REFEREE-2's (20:47:29Z) by 48 s;
  the two §C rounds are 61 s apart at L-1 (23:02:24Z, 23:03:25Z) and 39 s apart at L-2 (00:09:07Z, 00:09:46Z), and neither L-2 file
  cites the other's L-2 verdict (REFEREE-2 L2 names REFEREE's L-1d, a §C item at L-1).
  Differences, resolved: REFEREE alone found IR-1 (REFEREE-2 L1 l. 21 «and it is my miss.») and L-1d (REFEREE-2 L2 l. 63 «I concur»);
  REFEREE-2 alone recorded the degree ≥ 3 DATA (N-2), which REFEREE reproduced on its own genomes (§C l. 214-217); both found U-1 = N-1.
  Both SIGN the same sixteen statements with no gap after entry 1, and both MATCH L-2. No disagreement in substance.
- TARGET.md diff: TARGET.md §1-§3 define parity games («A parity game is G = (V, V_E, V_O, E, pr) with V finite»), the regions W_E,
  W_O, M4 (§2 «There is a deterministic algorithm A and a polynomial p such that for every parity game G, A on input G halts within»
  «p(n + m) steps and outputs the pair (W_E(G), W_O(G)).») and the word-RAM cost model; no statement of this entry mentions a parity
  game, a winning region, an algorithm's running time or a cost model (packet §9 l. 253-258; REFEREE §6 l. 170-177 «Agreed with the
  packet's §9 diff: not M4, not M3, not a gauntlet step. G-N5-TIME OPEN.»; REFEREE-2 §0 l. 22-26 «So nothing is an M3 / M4 claim or a
  gauntlet step. The packet's own §9 diff is correct. G-N5-TIME stays OPEN.»). The line (L-2) makes no M4 claim and no TARGET claim;
  its tail reads «a REDUCTION / EQUIVALENCE statement inside the IDEAL model; bounds nothing polynomially» and «G-N5-TIME stays OPEN;
  not M3, not a step-4 pass, not a TARGET.md claim» (L-2, by script). Not a step-4 pass. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER R104's UPDATE of G-N5-TIME (GAPS at 3398c652, last changed by 3398c652: the last
UPDATE on l. 11 is R104's, «UPDATE 2026-11-02 11:22Z: RESULTS R104 (P-N5-REALIZE; CHECKER C115 7c3c413f) …», before the row's closing
« |»), built by script (upd105.py: upd100L3.py's build() unchanged for the label move, on the claim body with a sentinel tail as for
R102; the tail rule of (9); to check (9)) only from the clauses of the title line L-2: labels behind their clauses; « (2026-11-03) — »
→ «: »; the DATA parenthesis opened as «; DATA: …»; «G-N5-TIME stays OPEN» and «not M3, not a step-4 pass, not a TARGET.md claim»
dropped; the source parenthesis kept; «. G-N5-TIME stays open.» at the end. The same script reproduces R97's to R104's LANDED UPDATEs
(GAPS l. 11) byte for byte. L-2 holds no "|"; the UPDATE holds none. <DATE> is the landing date (YYYY-MM-DD, by date -u at the landing
commit; C114 Add. 1 E-1), <HH:MM> the landing time and <checker> the CHECKER C116 commit, all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R105 (P-IDEAL-RED; CHECKER C116 <checker>) [refereed-only] LANDED: In the IDEAL model of RESULTS R104 (the model first stated in L-RED R178 §1), on acyclic Ξ-graphs (premise: R104's definition of the model only, no theorem of R104 used; any number of movers per level; π any topological order of the Ξ-graph, N movers, M options, T steps of a run, h_t a least-level mover of step t, y_t the largest-π mover of step t, c_s(x) the number of options of x strictly better than its current one, KP_s(x) the key-preferred option under the keys of s), at any degree: the Ξ-order of β-sets is the order of the integers Σ ±2^rank (+ for even parity), so, with ε(x, k) := ±2^rank(x, k) (+ for even parity), the value of option (x, k) is ε(x, k) plus the current value of its Ξ-target (ε(x, k) alone if the Ξ-target is the exit X) (ENC); an option's value depends only on the states on its chain, a key only on the states below its level (LOCAL); the current Ξ-value of every mover never decreases along a run (MONO); for t ≥ 2 every least-level mover h of step t moves to an option w ∉ A_(s_(t−2))(h) (A_s(h): h's current option under s and its options strictly better under s) (XI-NEW); that option's value rose strictly at step t − 1, and some strict Ξ-descendant of h on its chain under s_(t−2) moved at step t − 1 (RISE); if step t ≥ 2 is chained (h_(t−1) lies on the chain under s_(t−2) of the option h_t takes), then π(h_t) < π(h_(t−1)), and T ≤ N (1 + U) with U the number of unchained steps t ∈ [2, T] (CHAIN-BACK); U ≤ max(T − 1, 0), so T is polynomial in N + M iff U is (U-EQ); c(y_t) ≥ 1 before step t, c(y_t) falls at step t, and no mover with π > π(y_t) changes its option or its c (DECREMENT); with D the largest degree, Σ_x c(x) D^π(x) falls at every step, so T ≤ D^N − 1 (EXACT-ENERGY); and at degree ≤ 2 only: moves(x) ≤ 1 + KF_x with KF_x the number of steps at which KP(x) changes, so T ≤ N + KF and KF ≤ N T (T polynomial iff KF is) (KEYFLIP); for every k ≥ 1, the tuple TOP_k of the k largest π of unstable movers (padded with −1 to length k) falls lexicographically at step t iff RANK_t := 1 + #(unstable movers above y_t before the step) ≤ k, and is unchanged otherwise (TOP-MONO); for k ≥ 1, #(steps with RANK ≤ k) ≤ Σ_(j ≤ k) C(N, j) − 1, so U ≤ Σ_(j ≤ R) C(N, j) − 1 with R the largest RANK over unchained steps (R := 0 if U = 0) (RANK-BOUND); on an interval of states where TOP_k is constant with k-th entry p, every mover of every interior step has π < p, the genome in which every mover with π ≥ p keeps only its option at the interval's first state runs exactly those states as a prefix of its run from that state, and chained / unchained labels agree from the interval's third state on (step a + j of the run against step j of the restricted run, for j ≥ 2) (INTERVAL-RESTRICT); for r ≥ 2, #(steps with RANK = r) ≤ (N − r + 1)(1 + #(steps with RANK ≤ r − 1)) (INTERVAL-CHARGE); with U*(n) the largest U over degree-≤-2 genomes with at most n degree-2 movers, U*(n) ≤ n + Σ_(p < n) (U*(p) + 1) (RECURSION): a REDUCTION / EQUIVALENCE statement inside the IDEAL model; bounds nothing polynomially (EXACT-ENERGY and RECURSION are exponential bounds; no bound on U or KF is claimed); degree ≤ 2 is needed for KEYFLIP and TOP-MONO (DATA, REFEREE-2 N-2); Ξ-cyclic genomes, the real-N5 form of XI-NEW and the 2-wide-ladder identity KF_x = F_(lev(x)−1) are not covered; DATA: 0 violations of every inequality on 46 corpus genomes and 75,518 all-start runs of 200 random genomes, experiments/new/box150/check.py (P-IDEAL-RED, docs/new/P-IDEAL-RED.md with its fixes entry 1, docs/new/P-IDEAL-RED-fixes.md; L-NEW successor 50). G-N5-TIME stays open.

Addendum (subagent, for the Lead; does not land; written 2026-11-04T01:08:55Z by date -u). (1) FIRST FILL on line L-2 (l-new ffeb9736,
sha1 65ba7ca7…), to CHECKER C116. L-2 MATCHES at both referees (REFEREE 23 §C addendum 1 0d2fef9f; REFEREE-2 26 R2-P-IDEAL-RED-L2.md
f81c6e57). NOT committed, NOT pushed; no tracked file edited; this file is new and untracked. The commits 0ebddcf5, b115ff3a, ffeb9736,
a4e7b4a9, a71540d5, d8f25ef2, 0d2fef9f, 2f9b6f5c, ca757330 and f81c6e57 are not on trunk at this fill (header): merge claude/l-new,
claude/referee and claude/referee-2 and push trunk before landing. (2) TITLE l. 346 = "### R105 [refereed-only] " + L-2 without its
newline + ", CHECKER PASS (docs/checker/C116.md, checker PENDING)", checked by script after the fill (fill105.py, chk105.py): equal,
byte for byte (True); the only «### R» heading of this file. (3) BODY l. 346-590 (title l. 346 to the last body line; 0 "|" in
the range, by script); GAPS preamble l. 592-599; UPDATE l. 600 (one line, 0 "|", one <DATE>, one <HH:MM>, one <checker>;
controls True ×8: R97's-R104's landed UPDATEs). A landing script in the shape of land104.py slices d[345:590] for the entry and
reads d[599] for the UPDATE. (4) RE-RUNS: check.sh block w99's three commands from a git archive of 0ebddcf5 (00:49:10Z-00:49:35Z,
rc 0, byte-equal to the expected strings), plus default starts, NEG=1, NEG=2 (01:05:00Z, rc 0) ((10)). NOT RUN: the referees' tools
(logs read instead), box150/rand.py, the full check.sh, scripts/verify.sh. (5) QUOTE SWEEP: chk105.py (q104.py's rule: outermost
guillemet quotes, whitespace joined, split at the ellipsis, parts of 6+ characters; sources: packet, L-1, L-2, fixes at ffeb9736, the
three referee files at their head commits, the pre-check, notes/L-NEW.md at ffeb9736, check.sh at 0ebddcf5, RESULTS, GAPS, DECISIONS,
NOW, TARGET.md, CLAUDE.md, R103-draft, w99.out, extra.out, the Lead commit subject of 2799f0dd and the referees' logs): 536 outermost
quotes, 473 parts of 6+ characters, every part found (0 not found). Line-precise check of the referee verdicts and other cited lines:
179 of 179 (source, cited line range, quote) triples found verbatim, whitespace-normalised, inside the cited lines (verdict cells,
verdict lines, packet statements, fixes, notes, DECISIONS, RESULTS, TARGET.md, check.sh). Every sha1, line count and commit time cited
was re-measured in this session (sha1sum, wc -l, cmp, git log -1 on the commit), not copied from a report. (6) DISCREPANCIES: see (11)
(D-1 to D-8; none affects a verdict) and G-1 to G-10 (notes). I found no error in a signed statement and no mismatch between a report
and the lane files. (7) FLAGS LEFT FOR CHECKER: none REQUIRED from my side. Notes: G-1 (source note «fixes entry 1»), G-2 (unglossed
«unstable», «moves(x)», «strict Ξ-descendant», unnamed «a»), G-3 («TOP-MONO», «MONO», «RISE» also name other RESULTS items), G-5 (L41
not triggered, my reading; neither referee addresses L41), G-6 (the «needed» DATA clause carries no number), G-10 (no sha1 pin in
check.sh), the new UPDATE tail rule ((9)), the Dead-ends proposal ((14)). (8) NOT VERIFIED: the Lead's routing messages (fixes l. 4
«Routed by the Lead 21:44Z / 21:50Z», l. 70 «routed by the Lead 23:40Z») are not in the repository; the referees' tools were not re-run;
I did not open docs/new/N5-IDEAL-STATE.md or the box 147 / 148 notes (history only). Scratch files (not committed) in
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r105: R105-template.md, fill105.py,
chk105.py / chk105.out, upd105.py / upd105.txt / upd105.out, wdiff105.py / wdiff105.out, w99.out, extra.out, the extracted sources
(pkt.md, fixes.md, fixes1.md, L1.txt, L2.txt, ref_*.md, r2*.md, pre.md, notes.md, checksh.txt, run1.log, run2.log, deg3.txt, gitlog.txt)
and arch0ebd/ (the archive).
(9) THIS DRAFT'S SHA1: a file cannot state its own sha1. The sha1 of this file with the forty hex digits after the next colon
replaced by forty «0» characters is: 1619c8b0af6d2715f075e52e1987460f52c2b890. The file's actual sha1 and line count are in the
hand-back to the Lead (and re-measurable with sha1sum).
