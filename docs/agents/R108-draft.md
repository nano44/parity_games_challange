# Draft RESULTS R108 (Lead; first fill 2026-11-04T15:16:49Z by date -u (subagent); on P-IDEAL-SEG line L-1, docs/new/P-IDEAL-SEG-line-L1.txt, l-new 8291ecf7, sha1 a18f6f0c61d6d5f33adc61519d94252dd5ba9721) — to CHECKER C120 — LANDED in RESULTS 2026-11-04 16:53Z (CHECKER C120 7982d57a PASS), after R107, before Erratum E-1
FIRST FILL. Read at the origin heads fetched at the start of the fill (git fetch, then git ls-remote, 2026-11-04T14:57:49Z: l-new
16297185, l-red 0f7508cf, referee 3b8a9c77, referee-2 cdf8e962, checker 914d073f; origin trunk 6f1be9e2; local trunk dee561d2 = the
merge (--no-ff) of the l-new, referee and referee-2 heads into 6f1be9e2, not pushed (the checker head 914d073f is already an ancestor of
6f1be9e2, so the merge has three lane parents); the merge changes no Lead file, so RESULTS (sha1
99dc21851af915d9da184104150520ba88e77947), GAPS (6dda337214c2bc16bd30525c286038f5b5be945c), DECISIONS, DECISIONS-INDEX, NOW and
TARGET.md are byte-equal at dee561d2 and 6f1be9e2 (git diff --quiet, exit 0), and RESULTS and GAPS were last changed by the R107 landing
commit 6f1be9e2): the packet and L-1 (8291ecf7; both unchanged at the l-new head 16297185, by cmp and sha1), fixes entry 1 (6eb389a6;
unchanged at 16297185); REFEREE successor 23's docs/referee/R-P-IDEAL-SEG.md (19e0742f, unchanged at 3b8a9c77) and its FYI item on fixes
entry 1 in docs/referee/R-P-IDEAL-SLOT.md §C (3b8a9c77, l. 155-160); REFEREE-2 successor 27's docs/referee-2/R2-P-IDEAL-SEG.md
(9a746361, unchanged at cdf8e962); the referees' tools and logs (REFEREE scratch/seg_probe.py and xinew_logs/seg_probe.txt; REFEREE-2
R2-P-IDEAL-SEG/seg_check.py, no committed log); notes/L-NEW.md at 6eb389a6 (l. 4-26, 40-44); docs/new/N5-SEG-box157.md at 6273270f (its
only commit; unchanged at 8291ecf7 and 16297185); experiments/new/check.sh at 6273270f, 8291ecf7 and 6eb389a6; the instance
experiments/new/box157/max_d5_L15.json and L-RED's experiments/red/r202/max_d5_L15.json at 05c48415 and at the l-red head 0f7508cf
(fetched, not merged); DECISIONS L41, L43; RESULTS R104 (title l. 9864, the model definition only), R105 (title l. 10155; body item (b)
l. 10214-10216), R107 (l. 10593-10810), Erratum E-2 (l. 10825-10851); GAPS l. 11; docs/checker/C117.md, C118.md, C119.md (914d073f).
Re-runs (scratch, git archive of 6eb389a6's experiments and docs/new): the commands of check.sh blocks w106 and w107 / pin107,
2026-11-04T14:59:57Z-15:00:13Z, rc 0, output byte-equal to the blocks' expected strings and two PASS lines ((10)); my own simulator on
the instance and my own split of the DATA by degree, 15:06Z, rc 0 ((10)).
TRUNK STATUS AT THIS FILL (by script, git merge-base --is-ancestor against local trunk dee561d2 and origin trunk 6f1be9e2): 6273270f,
8291ecf7, 6eb389a6, 16297185, 19e0742f, 2a09dcf8, 3b8a9c77, 9a746361 and cdf8e962 are ancestors of local trunk dee561d2 (exit 0 each)
and NOT of origin trunk 6f1be9e2 (exit 1 each); 914d073f (C118 / C119 Add. 1), 18c288c6 and f71e80ea (Lead) are on both; 05c48415
(l-red) is on neither. The Lead pushes trunk before landing. C113 E-2 lesson: the body names these commits on their branches only and
makes NO statement about trunk. C113 E-1 lesson: the title is L-1 verbatim with no insertion. C114 Add. 1 E-1 lesson: the GAPS UPDATE
head carries «<DATE>», filled at landing. C115 E-1 lesson: the premise route is checked against what RESULTS records (G-4). C116 G-1 and
C118 §4: the UPDATE rule of R105 is applied unchanged, with R107's step for the unlabelled DEAD clause ((9)). C116 G-2: a name clash is
settled by one body sentence (G-6; Honest limits (viii)). C117 E-1 / E-2 lessons: no sentence of the entry says more than the line
signs, DATA is scoped exactly as measured, and the instance is fully specified (here: max_d5_L15 inline, with its start, the states s_0
… s_15, full sha1 and both repository paths). C118 E-1 lesson: no status sentence that goes stale; the entry calls nothing «pending»
(the only «PENDING» is the title fill «checker PENDING», replaced at landing), and Erratum E-2 is cited as landed text. C118 §3 /
Erratum E-2 lesson: every DEFINITION in the title line is diffed against the packet's definitions (G-2). C118 §5 G-8: «For later lines:
name the statements a DATA count covers.» (G-9: L-1 does not; the body does). C118 §5 DE37 ruling: a lane conjecture killed inside a
landed line gets no Dead-ends row (14). In the body (title + entry), L-1 is the current and only line.
to check: FLAGS FIRST (G-1 to G-13; none REQUIRED from my side; no referee raised any of them as REQUIRED; G-9 is the one CHECKER may
want to rule on), then the CLEAN items and (0)-(14).
- G-1, TITLE SHAPE AND SOURCE NOTE (note; no Lead insertion). L-1 contains «2026» once, as « (2026-11-04) — », the only « — » (by
  script), and ends with the source parenthesis «(P-IDEAL-SEG, docs/new/P-IDEAL-SEG.md; L-NEW successor 51)». The title is "### R108
  [refereed-only] " + L-1 + the fill ", CHECKER PASS (docs/checker/C120.md, checker PENDING)" (as R90-R107), nothing inserted. The
  source note names no fixes file. That is right for this line: fixes entry 1 changes neither the line nor a signed statement (fixes l.
  3 «Neither touches line L-1 or a signed statement.», l. 20 «Line L-1 is unchanged. No statement or DATA count changes.»), the C117 §6
  G-1 case («G-1 (the source note names no fixes file): note, NOT required.»), not R107's (whose fixes entry 1 re-proved two items).
  Like R107's, L-1 has no «(the model first stated in L-RED R178 §1)» attribution («R178» 0 times in L-1 and in the packet); R104
  carries it.
- G-2, DEFINITIONS DIFFED AGAINST THE PACKET (the C118 §3 / Erratum E-2 lesson; my own diff, by reading and by script where literal):
  every definition and every defined object in L-1 against packet §0-§4: (i) «N movers» = §0 l. 26. (ii) «T the number of steps of a run
  from a given start» = §0 l. 37-38 («T := the number of steps.», the run from the start s_0, l. 28). (iii) «Mv_t the movers of step t»
  = §0 l. 39 («Mv_t := {x : s_t(x) ≠ s_(t−1)(x)}»). (iv) «C_l the number of steps whose movers include one of level at most l (C_(−1) :=
  0)» = §3 l. 86 (the steps t ∈ [1, T] whose Mv_t contains a mover of level ≤ l; «C_(−1) := 0»). (v) «n_l the number of movers of level
  l with two options» = §3 l. 86-87 («n_l := the number of degree-2» «movers of level l»). (vi) «on acyclic Ξ-graphs» = IDEAL-ACYC (§0
  l. 30); «any number of movers per level» = §0 l. 43 «No width hypothesis is made in §1-§3: every level may hold any number of
  movers.». (vii) SEG's interval hypothesis «no step of an interval [a, b] of steps moves a mover of level at most l» = §1 l. 47 («Mv_t
  contains no mover of level ≤ l for every t ∈ [a, b]», [a, b] ⊆ [1, T]); SEG's genome «the genome in which every mover of level at most
  l keeps only its option at s_(a−1)» = §1 l. 48-49 (the kept option with «the same W-target, Ξ-target, β» «and gate»; the line's «keeps
  only its option» keeps that option's record); «runs from s_(a−1) through exactly the states s_(a−1), …, s_b first» = §1 l. 50 («has
  s_(a−1), s_a, …, s_b as its first b − a + 2 states»). (viii) SEG-ONCE «on such an interval every mover of level l + 1 moves at most
  once» = §2 l. 71-72; «so every level-0 mover moves at most once in a whole run» = l. 72 (l = −1, [a, b] = [1, T]). (ix)
  LEVEL-PRODUCT's three forms = §3 l. 88-89; «the product over all levels l of (n_l + 1)» = «Π_(l = 0..top) (n_l + 1), with top the
  largest level» (levels are contiguous, REFEREE-2 l. 50-51 «Levels are contiguous (W-targets one level» «down)»). (x) «a d-level ladder
  with two movers of degree 2 per level» against §0 l. 42 «d-level 2-wide ladder: a genome with levels 0, …, d − 1, exactly two movers
  per level, all of degree 2 (N = 2d).»: the line's words also admit extra degree-1 movers; then n_l = 2 still and the bound follows
  from the signed product form (REFEREE l. 95-96 «The line's form also admits extra degree-1 movers, and the bound still holds for them
  (n_l counts degree-2 movers only)»; REFEREE-2 P-1, l. 112-113, «this is precision only»). So the clause is not wider than signed. (xi)
  REPLAY's guillemet text in L-1 = §4 l. 107-109 (REFEREE l. 97-98: «before that interval» = j < a; REFEREE-2 l. 107: «follows a level-0
  move» = a ≥ 2 with step a − 1 a level-0 move). (xii) the instance clause: «5-level 2-wide ladder» = §4 l. 111-112; «from its stored
  start» = the JSON field "start" [0, 0, 1, 1, 0, 0, 0, 0, 1, 0] (l. 112); «N 10, T 15» = l. 111-112; «level-0 moves only at steps 7 and
  8» = l. 118; «s_9 is new above level 0» = l. 119-120 (no s_j with j ≤ 8 agrees with s_9 on movers 2..9, the movers of level ≥ 1);
  «sha1 ba963ace…» = l. 111. ALL EQUAL. Both referees did the same diff under the new rule: REFEREE §5 «## 5. Line L-1 (with the new
  rule: every DEFINITION diffed against the packet)» (l. 88-110); REFEREE-2 «## Line L-1: clause by clause, every definition against the
  packet» (l. 91-110).
- G-3, STRICT SYMBOL TEST (notes; both referees' binder passes are clean on L-1, (7)). (i) «s_(a−1)», «s_b», «s_9» (the state after step
  t, s_0 the start) are not bound in L-1; they are packet §0's (l. 36-39) and R105's notation (R105's line uses s_(t−2)); R107's line
  has the same gap (R107 draft G-2 (i)); neither referee raised it. (ii) «l» in SEG is free: «for every l ≥ −1» is implicit (REFEREE
  optional SEG-L1, l. 108-109 «SEG's «level at most l» leaves l unbound in the line. The packet has l ≥ −1»; REFEREE-2 optional P-2, l.
  114, and l. 98-99 «(l ≥ −1» «implicit; any l works)»); SEG-ONCE's «on such an interval» refers back to SEG's l and [a, b];
  LEVEL-PRODUCT binds its own l («for every l ≥ −1»). Not taken (no L-2). (iii) «Mv_t» is bound in L-1 and not used again (1 occurrence,
  by script); harmless. (iv) «a level-0 move» = a step whose movers include a level-0 mover; «above level 0» and «on all movers of level
  ≥ 1» = on the movers of level ≥ 1 (packet l. 109, 119). (v) «d» is bound by «a d-level ladder». (vi) «IDEAL-ACYC» inside REPLAY's
  guillemets is R104's name for the model on acyclic Ξ-graphs («IDEAL-ACYC» occurs in RESULTS R104's body; packet l. 30). (vii) «the
  IDEAL model», «level», «mover», «option», «degree», «step», «run», «start», «state» are R104's model words (RESULTS l. 9864) and
  packet §0 (l. 26-39). None is a claim clause's quantifier left free except (ii), whose reading is fixed by the packet and by both
  referees.
- G-4, PREMISE ROUTE (the C115 E-1 class): CLEAN (my check). L-1's premise parenthesis: «premise: R104's definition of the model only,
  no theorem of R104 used; and RESULTS R105's LOCAL, key half only». What RESULTS records (by script): R105's title (l. 10155) contains
  «(LOCAL) an option's value depends only on the states on its chain, a key only on the states below its level» once, and «a key only on
  the states below its level» occurs once in RESULTS (REFEREE l. 26-27 «It is FOUND verbatim in the landed R105 line on trunk» «18c288c6
  (grep -F: 1 hit).»; REFEREE-2 l. 24 «grepped verbatim in the landed R105 statement (1 hit)»; the same at 18c288c6 and at 6f1be9e2, by
  script). R105's body item (b) (RESULTS l. 10214-10216) has the key half in the form «(c) key_s(x, k) = key_(s′)(x, k) whenever s and
  s′ agree on every mover of level < lev(x).»; the packet quotes the line form only (packet l. 61-62, 77-78). Uses: SEG (iii) and
  SEG-ONCE (and LEVEL-PRODUCT through SEG-ONCE): REFEREE l. 28 «The key half is all that is used: in SEG (iii), SEG-ONCE, and (through
  SEG-ONCE) LEVEL-PRODUCT.»; REFEREE-2 l. 24-25. SEG (i) uses no value half of LOCAL: REFEREE l. 29-30 «SEG (i) does not use LOCAL.» …
  «(the M2-G1 trap does not arise)». KP_s(x) is the packet's own definition (§0 l. 40-41), not a citation of R105's KP_s(x) or KEYFLIP
  (REFEREE-2 l. 22-23 «KP_s(x) for» «degree 2 (own definition, keys of distinct options differ in the gate)»); the lane source's remark
  «(This is the KEYFLIP argument of RESULTS R105 with KF = 0 on the stretch.)» (docs/new/N5-SEG-box157.md l. 76) is not in the packet
  and is history only. R104's definition: title l. 9864; REFEREE l. 25 «§0 restates it, and the restatement agrees clause by clause with
  R104 and with R105 §0.»; REFEREE-2 l. 21-23 (the same restatement as in P-IDEAL-M2 §0, checked against R104's text; «No R104 theorem
  used.»). Packet l. 18-22: «Premises (both LANDED).»; «RESULTS R104 (P-N5-REALIZE): ONLY its definition of the IDEAL model and of the
  Ξ-graph, restated in §0. No theorem of R104 is used.»; «RESULTS R105 (P-IDEAL-RED): only item LOCAL, key half, quoted verbatim from
  the R105 statement where it is used. No other R105 item» «is used.»; «Not used: RESULTS R106, R107, docs/lit, docs/sources, any other
  lane file. No outside source is cited.» REFEREE l. 33 «No docs/lit, no docs/sources, no R106 or R107.»; REFEREE-2 l. 26-27 «No other
  R105 item, no U / CHAIN-BACK / E-2, no R106 / R107, no docs/lit: confirmed by reading every» «proof step.» The DEAD instance is a data
  file (L-RED R202's witness, copied into experiments/new/box157/), recomputed by both referees with their own simulators; it is an
  instance, not a premise. No unlanded result, no lit note and no lane file is a premise.
- G-5, RESULTS ERRATUM E-2 TO R105 DOES NOT BEAR ON R108 (note for CHECKER; the C118 G-5 question, answered no). Erratum E-2 (LANDED,
  RESULTS l. 10825-10851, 6f1be9e2; C119 PASS) corrects three definitions in R105's title line: (E2a) CHAIN-BACK's chained binder (U),
  (E2b) TOP-MONO's RANK_t, (E2c) KEYFLIP's moves(x). R108 uses none of them: packet l. 20-21 «U, CHAIN-BACK and the CHAINED binder (R105
  Erratum E-2, at CHECKER C119) are not used.»; by script, packet §0-§4 (l. 25-124) contain 0 times each of «U» (as a word), «CHAIN»,
  «chained», «RANK», «KEYFLIP», «moves(x)», «π», «h_t», «ENC», «XI-NEW», «MONO», «RISE», «TOP» and «INTERVAL», and cite R105 only at l.
  61 and l. 78 (LOCAL's key half); L-1 contains «CHAIN» 0, «KEYFLIP» 0 and «moves(x)» 0 times; REFEREE l. 31 «U, CHAIN-BACK and CHAINED
  are not used. I grepped the proofs and found no use. So R105's erratum E-1 does not touch this packet.»; REFEREE-2 l. 26 «no U /
  CHAIN-BACK / E-2». LOCAL is not among E-2's three definitions. So unlike R107 (C118 G-5: «E-2 must land before R107 or in the same
  commit»), R108 has no landing condition from E-2, and the entry needs no E-2 sentence beyond one premise remark (Premise). Names:
  REFEREE's «R105's erratum E-1» (l. 31) and «R105 E-1» (l. 121) are its own name for the CHAINED defect (REFEREE 685a47de «R105-E1»),
  which is RESULTS Erratum E-2 (E2a); REFEREE l. 32 «The erratum is drafted for C119 (trunk d08df7c8). It is not yet in docs/RESULTS.md
  at 18c288c6.» was true at 18c288c6 and is history (E-2 landed in 6f1be9e2, 13:41:15Z, after the report 12:17:57Z); the entry says
  nothing about E-2's status.
- G-6, NAMES, SAME LABELS, OTHER MEANINGS (by script on RESULTS 99dc2185 / GAPS 6dda3372; note; C116 G-2's remedy applied). 0 times in
  RESULTS and GAPS: «P-IDEAL-SEG», «SEG-ONCE», «LEVEL-PRODUCT», «REPLAY» (and «replay» in any case), «max_d5_L15», «R202», «R108»,
  «C120», «box 157», «box157», «segcheck», «N5-SEG», «3^d», «n_l», «C_l», «d-level», «DE37». Same names, other meanings: (a) «SEG» 41
  times in RESULTS as a word, all in R83 (l. 4774-4939: «SEG(S)», the number of maximal REL-admissible segments of a run S) and in R87's
  DATA (l. 5586-5600, a check counter «SEG» of the L-SI N5-SF tool), and 3 times on GAPS l. 11, in R83's UPDATE («|S| ≤ SEG(S)·n − 1»,
  «CONJECTURE SEG-RUN (SEG = O(n)) stays OPEN»); R108's «SEG» is a lemma label about level-frozen stretches of IDEAL runs, unrelated to
  SEG(S) and to CONJECTURE SEG-RUN, which it neither uses nor settles. (b) «2-wide ladder» / «2-wide-ladder»: R105 (l. 10155, 10326)
  names «the 2-wide-ladder identity KF_x = F_(lev(x)−1)» as not covered; R108's 2-wide ladder is packet §0's definition (l. 42), the
  same family of genomes, and R108 says nothing about that identity. (c) «IDEAL-ACYC-POLY» (5 times in RESULTS, R104 (k) and DE36) is
  not used by L-1. (d) R105's Lemma INTERVAL-RESTRICT is also a restriction lemma («the genome in which every mover with π ≥ p keeps
  only its option at the interval's first state runs exactly those states as a prefix of its run from that state», R105's title) but
  freezes by π on TOP_k-constant intervals at degree ≤ 2; SEG freezes by level, at any degree; the packet does not cite it (packet l.
  20-21) and neither referee mentions it (my reading: two separate statements; neither is used for the other). Applied (C116 G-2): one
  body sentence, Honest limits (viii). No line change.
- G-7, L41 (the C109 E-1 class): not triggered (my reading; neither referee mentions L41). L-1 contains «referee-originated» 0 and
  «lane-authored» 0 times. The proofs are L-NEW successor 51's (packet l. 5 «Labels: PROVED (L-NEW 51, unrefereed) / DEAD / DATA /
  READING (not to sign).»). POINTS TO CHECK: (a) fixes entry 1 answers REFEREE-2's F-1 and F-2 (findings on the §5 DATA remark and on
  the §4 quote of the lane proposal, REFEREE-2 l. 77-84); both corrections are the lane's text and change no statement («Line L-1 is
  unchanged. No statement or DATA count changes.», fixes l. 20). (b) No line change was made; REFEREE's SEG-L1 and REFEREE-2's P-1 to
  P-4 are optional and not taken. (c) The DEAD instance is L-RED's (another lane), not a referee's. Nothing referee-originated is a
  premise or a proof step (my reading).
- G-8, L43 (DEADs): CLEAN (my reading; please rule). L-1 has one DEAD: «and DEAD: the lane conjecture REPLAY («in every degree-≤-2
  IDEAL-ACYC run, every state inside a maximal interval of steps without a level-0 move that follows a level-0 move agrees on all movers
  of level ≥ 1 with some state before that interval») is false, by L-RED R202's 5-level 2-wide ladder max_d5_L15 from its stored start
  (N 10, T 15; level-0 moves only at steps 7 and 8; s_9 is new above level 0; sha1 ba963ace…)». L43 (DECISIONS l. 369-374) bars a lane
  DEAD of an ASYMPTOTIC statement («one with an unspecified constant») and asks for «a refereed proof, or one instance exceeding an
  EXPLICIT bound». REPLAY is a universal statement with no constant and no bound; its refutation is one explicit instance on which both
  referees recomputed the run and the failure at t = 9 with their own simulators and SIGNED the DEAD (REFEREE l. 15 «SIGN (recomputed
  independently)», l. 61-67; REFEREE-2 l. 16, l. 57-60, l. 108 «L43: universal finite statement killed by an explicit instance with its
  numbers. ✓»). So the DEAD rests on a refereed refutation by an explicit instance; L43's asymptotic bar does not apply. THE KILLED
  STATEMENT: the packet's precise form (§4 l. 107-109), which the lane's proposal implies: REFEREE l. 57-59 «It is IMPLIED by the lane»
  «proposal (docs/new/N5-SEG-box157.md l. 24: «after a level-0 reset, the next segment is a sub-run of a segment already seen»): a»
  «sub-run only revisits states already seen above level 0.»; REFEREE-2 l. 54-55 «It is implied by the proposal «the next segment is a
  sub-run of a segment already seen» when states are» «compared above level 0, so killing it kills the proposal in that reading.» L-1's
  guillemet text is the line's own paraphrase of §4's precise form, not a quote of a lane file (REFEREE-2 optional P-3, l. 115 «the
  REPLAY text in «…» is the line's own paraphrase of §4's precise form, not a quote; guillemets could be dropped.»; not taken); both
  referees found it equal to §4 (G-2 (xi)). The packet's own quote of the proposal (§4 l. 105-106) was not verbatim (REFEREE-2 F-2);
  fixes entry 1 replaces it by the verbatim source text (fixes l. 13-19); the killed statement itself is unchanged (fixes l. 19). Other
  «replay» readings are not claimed (packet l. 124). «polynomial» 1 time in L-1 («bounds nothing polynomially»); «EXPONENTIAL» once («an
  EXPONENTIAL count bound»); «linear» 0, «O(» 0.
- G-9, DATA vs READING and the DATA scope (the C108 E-1 / C117 E-1 class; C118 §5 G-8): no overclaim found, ONE SCOPE NOTE (my reading;
  for CHECKER to rule). L-1 has one DATA parenthesis: «(DATA: 0 violations on 59 corpus runs with 652 intervals and on 34,934 random
  runs (every start for N ≤ 8, the genome start otherwise) with 57,755 intervals, experiments/new/box157/segcheck.py)». Every number
  equals the tool's output (my re-run (10); REFEREE l. 71-74; REFEREE-2 l. 65-68, 72-73). The start regime is stated exactly (the C117
  E-1 lesson met). THE NOTE: the line does not name the statements behind «0 violations» (C118 §5 G-8 «For later lines: name the
  statements a DATA count covers.», a report written before this freeze: C118 11:17Z, freeze 8291ecf7 11:48:36Z). segcheck.py checks SEG
  on every run but SEG-ONCE (ONCE), LEVEL-PRODUCT's per-level form (COUNT) and its product form (PROD) only on genomes of largest degree
  ≤ 2 (segcheck.py «if D <= 2:»; packet l. 136-137 «At» «degree 3 only SEG is checked.», said there for the corpus only). My split
  (scratch split.out, 15:06Z, rc 0): of the 59 corpus runs, 55 are of degree ≤ 2 (N = 4..24; 483 steps, 499 intervals) and 4 are the
  degree-3 genomes of box139/genomes (N = 9..24; 167 steps, 153 intervals; SEG only); of the 34,934 random runs, 1,936 are runs of the
  93 genomes of largest degree ≤ 2 (one of degree 1, 92 of degree 2; N = 1..10; 1,611 steps, 2,891 intervals; all four checks) and
  32,998 are runs of the 107 genomes of largest degree 3 (61) or 4 (46) (N = 1..9; 37,065 steps, 54,864 intervals; SEG only). So
  SEG-ONCE and LEVEL-PRODUCT are machine-checked by the lane on 55 + 1,936 runs, not on 59 + 34,934. Literally the line is exact:
  SEG-ONCE and LEVEL-PRODUCT are stated at degree ≤ 2 only, so a degree-≥-3 run has nothing of theirs to violate, and «0 violations» is
  true for every run counted. But a reader who takes «0 violations … on 34,934 random runs» as 34,934 tests of the degree-≤-2 statements
  overreads it. REFEREE-2 raised the scope as optional P-4 (l. 116 «DATA: «0 violations … (at degree 3 only SEG is checked)», as packet
  §5 says.»), not taken; neither referee stated the 1,936. My recommendation: NO line change (no signed statement uses a count; both
  referees accepted the DATA clause: REFEREE l. 106-107 «DATA» «(numbers equal to my w106 re-run). All MATCH.»; REFEREE-2 l. 109-110
  «segcheck.py ✓ (reproduced)»); the body's Data and Honest limits (v) state the split per statement. If CHECKER rules otherwise, the
  remedy is a line L-2 taking REFEREE-2's P-4 (one referee round). Other notes: (i) SEG is machine-checked on maximal intervals only
  (segcheck.py; packet l. 130); REFEREE-2's own tool checks every sub-interval (l. 41, 70-72: «12,175 sub-intervals» on the corpus).
  (ii) «maxratio 1.0» on the random runs comes from genomes with at most one degree-2 mover (packet l. 140 as corrected by fixes entry
  1, F-1; my count: 13 distinct ratio-1 genomes, r150_049.json with none and 12 with one; largest ratio with two degree-2 movers 0.6667,
  = REFEREE-2 l. 79 «{0: 1.0, 1: 1.0, 2: 0.6667, …}»). (iii) REFEREE's own probe is weak by its own account (l. 81 «My random runs are
  short (T ≤ 4), so this DATA is weak.»). No signed statement uses a count.
- G-10, LEAD READINGS AND RULINGS AS ON FILE (the C111 E-1 class): CLEAN. L-1 cites no Lead reading and no ruling (by script: «Lead
  reading» 0, «L4» 0, «D1» 0). The lane works under D14 / D18 (packet l. 2 «L-NEW successor 51 (Opus 5.5), D14 / D18;»). The freeze was
  a Lead GO (packet l. 2 «Lead 2026-11-04 11:49Z: «(a) freeze P-IDEAL-SEG for both referees, in the same form as P-IDEAL-M2»»), not a
  DECISIONS entry; the Lead commit 18c288c6 (11:46:48Z) has the subject «Lead: box 157 SEG/LEVEL-PRODUCT; P-IDEAL-SEG GO; R203 routed;
  log». The fix round: fixes l. 2 «Lead routing 2026-11-04 13:14Z»; Lead commit f71e80ea (13:12:25Z) «Lead: P-IDEAL-SEG signed;
  P-IDEAL-SLOT to referees; L-NEW 51 park; log».
- G-11, STALE LANE TEXT (notes; nothing here lands). (i) Packet l. 140 «(reached only by genomes with one degree-2 mover)»: false
  (REFEREE-2 F-1), corrected by fixes entry 1 (fixes l. 6-12), my count agrees (G-9 (ii)). (ii) Packet l. 105-106, the quote of the box
  157 proposal: not verbatim (REFEREE-2 F-2), corrected by fixes entry 1 (fixes l. 13-19). (iii) The lane source
  docs/new/N5-SEG-box157.md l. 23 «It reaches 1 only on trivial random genomes (one degree-2 mover).» has the same overreach as (i) and
  is not corrected there (history only; the packet with its fixes governs: packet l. 4 «This packet governs»). (iv) N5-SEG-box157.md l.
  16-17 compares LEVEL-PRODUCT with R105's EXACT-ENERGY («so LEVEL-PRODUCT is never worse than EXACT-ENERGY at degree 2»); the packet
  keeps only the arithmetic Remark (l. 99-100, «not to sign»); nothing of it lands. (v) Packet l. 2 «Lead 2026-11-04 11:49Z» is after
  the freeze commit 8291ecf7 (11:48:36Z); fixes l. 2 «13:14Z» is after the Lead commit f71e80ea (13:12:25Z) and before the fixes commit
  6eb389a6 (13:27:06Z); stamps not verifiable from the repository, no verdict affected. (vi) Packet l. 3 «Written 2026-11-04 (date -u:
  see the commit).»: the freeze commit 8291ecf7 has committer date 2026-11-04T11:48:36Z. (vii) Packet l. 110 places the instance at
  «claude/l-red 05c48415»: that is the file's only l-red commit (09:04:24Z, subject «L-RED R202: d 5 T >= 15 SAT (xmax, 2092 s), witness
  max_d5_L15 (replay L 15 opt), pin max_d5_L15_n96 …»), byte-equal at the l-red head 0f7508cf (sha1 ba963ace… each). (viii) The lane
  notebook has no «Dead ends» section entry for REPLAY; it records the kill at notes l. 9 «REPLAY DEAD (max_d5_L15)» and l. 41-42, and
  in docs/new/N5-SEG-box157.md l. 24-34 and l. 97 «DEAD: REPLAY (max_d5_L15)» (6273270f).
- G-12, SHA1 PINS IN check.sh (the C110 F-1 / C116 G-3 class): present. experiments/new/check.sh at 6273270f (880 lines) adds block w106
  (l. 873-879: three segcheck.py runs, three grep -qxF strings and the instance sha1 test); 8291ecf7 (888 lines) adds w107 / pin107 (l.
  880-887: seg.py on the instance, its three strings, the instance sha1, and pins of the packet and L-1); 6eb389a6 (903 lines) extends
  pin107 by the fixes («P-IDEAL-SEG: REPLAY DEAD data on max_d5_L15 (segment t9-15 all new); pins packet 7fa84784, line L-1 a18f6f0c,
  fixes 2e3dd532: PASS», l. 882-884 changed) and adds the P-IDEAL-SLOT blocks (l. 888-903, not this entry's); check.sh is unchanged from
  6eb389a6 to the l-new head 16297185 (same sha1). Re-run at this fill from the archive of 6eb389a6: both PASS lines ((10)). The
  instance sha1 ba963aceabeb35d95f9c47d80d1d0e87b87baf21 is tested in w106 (l. 875) and w107 (l. 883).
- G-13, THE REFEREES' ROUNDS (note). Both referees SIGN all four statements with no gap and MATCH L-1 on their first reports (REFEREE
  19e0742f; REFEREE-2 9a746361). Optional items raised and not taken: REFEREE SEG-L1 («(l ≥ −1)»); REFEREE-2 P-1 (ladder «with exactly
  two movers per level, both of degree 2»), P-2 (= SEG-L1), P-3 (REPLAY guillemets), P-4 (DATA degree note, G-9). REFEREE-2's findings
  F-1 and F-2 (not in the line, not in a signed statement) are answered by fixes entry 1 (6eb389a6). REFEREE checked entry 1 in an FYI
  item of its P-IDEAL-SLOT §C (3b8a9c77, docs/referee/R-P-IDEAL-SLOT.md l. 155-160): «F-1 is CORRECT.», «F-2 is CORRECT.», «Neither fix
  touches a signed statement or line L-1. P-IDEAL-SEG L-1 stays MATCHED.» REFEREE-2 has no committed check of entry 1 at the referee-2
  head cdf8e962 (git ls-tree: docs/referee-2/ has R2-P-IDEAL-SEG.md, R2-P-IDEAL-SEG/seg_check.py, R2-P-IDEAL-SLOT.md and
  R2-P-IDEAL-SLOT/, no R2-P-IDEAL-SLOT-L2.md and no other file naming P-IDEAL-SEG-fixes). Entry 1 corrects exactly REFEREE-2's two
  findings (F-1: the zero-mover case; F-2: the verbatim l. 24 text), and REFEREE-2 wrote that neither touches a signature (l. 80 «A
  fixes-file correction suffices.»; l. 83-84 «The killed statement is the explicit precise form, so nothing changes.»). My reading: the
  signatures do not depend on entry 1, so no second confirmation is needed for landing; if REFEREE-2 commits one before landing, the
  Lead may add one clause to the body's Fixes bullet (optional). The body makes no statement about REFEREE-2's view of entry 1 beyond
  its findings.
- CLEAN AT L-1 (the pre-check against CHECKER's recurring items, by script on a18f6f0c):
  C106 E-1 (old line as current): L-1 is the only line; no L-2 exists (docs/new/P-IDEAL-SEG-line-L2.txt absent at the l-new head
  16297185).
  C113 E-1 (title «verbatim» after an insertion): no insertion; the title is byte-equal to prefix + L-1 + fill (Addendum (2)).
  C113 E-2 (trunk status that goes stale): the body has no trunk statement (header).
  C114 Add. 1 E-1 (UPDATE date): <DATE> placeholder.
  C115 E-1 (a premise route RESULTS records as not established): G-4, G-5 (R104's definition and R105's LOCAL key half are landed text;
  Erratum E-2 does not bear).
  C110 F-1 / C116 G-3 (pins): G-12 (pins present and PASS).
  C111 E-1 (stale Lead-reading statements): G-10.
  C116 G-2 (name clash): G-6, one body sentence.
  C117 E-1 (a sentence wider than signed; DATA scope): G-2 (x), G-9; the body's DATA sentences carry the start regime, the N ranges and
  the degree split per statement; no gloss is unlabelled.
  C117 E-2 (instance under-specified): the body inlines max_d5_L15 (the JSON fields, the start, the states s_0 … s_15) with its full
  sha1 and both paths.
  C118 E-1 (stale status sentence): no «pending» in the entry; Erratum E-2 is cited as landed text (Premise).
  C118 §3 / Erratum E-2 lesson (definitions diffed): G-2.
  «|»: 0 in L-1, 0 in the entry block, 0 in the UPDATE (by script, Addendum (3)).
(0) PLACEMENT. R108 goes DIRECTLY AFTER R107's block. docs/RESULTS.md at local trunk dee561d2 (= origin trunk 6f1be9e2 for this file)
has sha1 99dc21851af915d9da184104150520ba88e77947, 11,390 lines, last changed by 6f1be9e2 (R107's landing with Erratum E-2). «### R107»
is l. 10593 (entry l. 10593-10810, l. 10811 blank); «**Erratum E-1**» is l. 10812; «**Erratum E-2**» is l. 10825; «## Dead ends (kept;»
is l. 10853; DE36 is l. 11374-11390, the last lines of the file. PROPOSED (R102's to R107's layout): insert R108's entry after l. 10811
(R107's blank line), with one blank line after it, so the R-entries stay contiguous and both errata follow them. The E-1 erratum's line
references (l. 7963-9195) and E-2's (l. 10155, 10229-10230, 10248) lie before the insertion and do not move. "### R108" occurs 0 times
in RESULTS and GAPS, «R108» 0 times. GAPS has sha1 6dda337214c2bc16bd30525c286038f5b5be945c, 23 lines, last changed by 6f1be9e2. The
Lead re-checks (6) and (9) at landing only if RESULTS or GAPS change after 6f1be9e2.
(1) TITLE. The title is the line file docs/new/P-IDEAL-SEG-line-L1.txt (l-new 8291ecf7d41bdc6fa31070c92f291d488d308519,
2026-11-04T11:48:36Z, the file's only commit, sha1 a18f6f0c61d6d5f33adc61519d94252dd5ba9721; identical at the l-new head 16297185),
verbatim: one line, no outer quotes, no final period, 2,004 characters (2,044 bytes plus the newline), 372 whitespace tokens, 20 / 20
parentheses (depth never negative), two «…» (L-1's own, in «s_(a−1), …, s_b» and «sha1 ba963ace…») and one guillemet pair (REPLAY's
text). NO HEADING MARKER, verified by script: the file begins «In the IDEAL model of RESULTS R104», with no «#» at its start, no "R??"
and no lane tag. NOTHING is stripped and NOTHING is inserted: the heading is the level-3 marker, then "R108 [refereed-only] ", then the
file without its newline, then the fill ", CHECKER PASS (docs/checker/C120.md, checker PENDING)" (as R90-R107, no space before the
comma). C120 is the next CHECKER file: docs/checker/ ends at C119.md on the checker head 914d073f and on trunk (no C120 on any fetched
head, by git ls-tree); notes/CHECKER.md's last resume point (11:17Z) names C118 and C119 and no later number. L-1 holds one « — », its
own date parenthesis «(2026-11-04)» and no "|" (G-1). Built by script (scratch fill108.py: assert the sha1 a18f6f0c…, equality with the
blob at 8291ecf7 and at the l-new head, one line, no marker, one « (2026-11-04) — », no "|"; prepend, append) and re-checked after
writing this file: equal, byte for byte. Heading: 2,083 characters, 2,123 bytes; sha1 of the heading line without its newline
17ef0db084e3d8d02cd4aca586081edc5e9510bd; it is l. 413 and the only «### R» line of this file.
(2) LINE HISTORY: one line. L-1 a18f6f0c (docs/new/P-IDEAL-SEG-line-L1.txt, 8291ecf7, frozen with the packet; 2,044 bytes, 372 tokens)
MATCHES at both referees on their first reports; no fixes entry changes it (fixes l. 3, 20); no L-2 exists. Optional line items raised
and not taken: REFEREE SEG-L1; REFEREE-2 P-1 to P-4 (G-13). So there is no word diff to check; the title is the frozen L-1.
(3) THE LINE AT BOTH REFEREES. REFEREE successor 23, docs/referee/R-P-IDEAL-SEG.md (19e0742f, 2026-11-04T12:17:57Z, new file, 122 lines,
sha1 8f7815d658dca305d7dd88af5b39dfeb2c7b9f95; unchanged at 3b8a9c77): verdict row «MATCHES (definition diff done; one optional
precision SEG-L1)» (l. 17), l. 110 «VERDICT: line L-1 MATCHES.»; after fixes entry 1, docs/referee/R-P-IDEAL-SLOT.md l. 160 «Neither fix
touches a signed statement or line L-1. P-IDEAL-SEG L-1 stays MATCHED.» (3b8a9c77, 13:50:44Z; the file 160 lines, sha1
6d6f3b5ad20245e4de765e634a106f4c8b1f281c). REFEREE-2 successor 27, docs/referee-2/R2-P-IDEAL-SEG.md (9a746361, 2026-11-04T12:31:18Z, new
file, 119 lines, sha1 296015a81b765530a0259702cb93b12b0178b986; unchanged at cdf8e962): verdict row «**MATCHES** (optional P-1 to P-4)»
(l. 17), l. 119 «Gaps: none. Line L-1: MATCHES.». Both MATCH L-1.
(4) CLAIMS SIGNED = the four statements below, each SIGN in BOTH referees' verdict tables (REFEREE "## 0. Verdicts" l. 9-17 of
R-P-IDEAL-SEG.md; REFEREE-2 "## Verdicts" l. 10-18 of R2-P-IDEAL-SEG.md), checked clause by clause against the packet; the cells are the
reports' words:
| item (packet §, lines) | REFEREE (successor 23) | REFEREE-2 (successor 27) |
| --- | --- | --- |
| (a) Lemma SEG (§1, l. 45-68; any degree) | l. 12 «SIGN»; §2 l. 36-44 | l. 13 «**SIGN** (Opus 5.5, D12)»; l. 30-41 |
| (b) Lemma SEG-ONCE (§2, l. 70-82; degree ≤ 2) | l. 13 «SIGN»; §2 l. 45-49 | l. 14 «**SIGN** (Opus 5.5, D12)»; l. 42-46 |
| (c) Corollary LEVEL-PRODUCT (§3, l. 84-102; degree ≤ 2; with the ladder form) | l. 14 «SIGN»; §2 l. 50-55 | l. 15 «**SIGN** (Opus 5.5, D12)»; l. 47-51 |
| (d) DEAD REPLAY, precise form, by max_d5_L15 (§4, l. 104-124) | l. 15 «SIGN (recomputed independently)»; §2 l. 56-68 | l. 16 «**SIGN** (Opus 5.5, D12): recomputed with my own simulator»; l. 52-62 |
Both, verbatim: REFEREE l. 119 «SEG, SEG-ONCE, LEVEL-PRODUCT and DEAD REPLAY: all SIGN, no gap.»; REFEREE-2 l. 119 «All four statements:
SIGN (Opus 5.5, D12), REFEREE-2 successor 27, 2026-11-04 (date -u stamp in the header). Gaps: none. Line L-1: MATCHES.»
Clause checks (L-1 against the packet; G-2): the setting = §0 l. 26-43 and §3 l. 86-87; SEG = l. 47-50; SEG-ONCE = l. 71-72;
LEVEL-PRODUCT = l. 88-89; DEAD = l. 105-122 (precise form l. 107-109; instance l. 110-112; t = 9 l. 118-120). Nothing in L-1 is wider
than signed (G-2 (x): the ladder clause follows from the signed product form; REFEREE l. 105 «All MATCH the packet.»; REFEREE-2 l. 109
«Scope tail = §1-§5 «Does NOT claim» and §5 ✓.»).
Signed by both, NOT stated by L-1 as separate items: SEG's count «(so H takes at least b − a + 1 steps)» (l. 50; REFEREE l. 44); §4's
«Also on the same run: the interval [9, 15] has length 7, longer than the only earlier such interval [1, 6] (length 6).» (l. 123) and
«In fact every one of s_9 … s_15 is new above level 0» (l. 121; REFEREE l. 67; REFEREE-2 l. 59); the §4 «Does NOT claim» parenthetical
on max_d4_L13 (l. 124; REFEREE-2 l. 61-62 «TRUE»). Not signed, so NOT landed: packet §5 (machine check, EXCLUDED, TARGET diff, READING;
«DATA / READING (not to sign)», l. 16); the §3 Remark (l. 99-100, «not to sign»; REFEREE l. 55 «is correct, and it is not to sign»);
fixes entry 1 as text (two text corrections outside the signed statements).
(5) OTHER TEXTS THE ENTRY DEPENDS ON: RESULTS R104's definition of the IDEAL model (title l. 9864; no R104 theorem); RESULTS R105's
LOCAL, key half (title l. 10155; body item (b) (c), l. 10216). Nothing else. The lane source docs/new/N5-SEG-box157.md §1 (packet l. 4
«Source: docs/new/N5-SEG-box157.md §1 (box 157). This packet governs») is history only; the DEAD instance is a data file ((10), G-11
(vii)); no lane file and no lit note is a premise (G-4).
(6) PREMISE LABELS (stale-label test; RESULTS at 6f1be9e2's version, GAPS likewise). RESULTS labels in L-1 (by script): «R104» 3
(«RESULTS R104», «R104's definition», «theorem of R104»); «R105» 1 («RESULTS R105's LOCAL, key half only»); «R202» 1, an L-RED box
label, prefixed («L-RED R202's 5-level 2-wide ladder»). R104 (l. 9864) exists and carries the definition. R105 (l. 10155) exists and
carries LOCAL; its own premise is R104's definition only. Erratum E-2 (l. 10825) governs the reading of three other R105 definitions and
retires no label (G-5). No Lead reading and no other RESULTS label is cited; R106 and R107 are not used. G-N5-TIME open (GAPS l. 11).
(7) SYMBOL TEST of the title (my own strict test of every symbol of L-1; IN = bound in the line; else the carrier):
| symbol | where |
| --- | --- |
| IDEAL model, Ξ-graph, acyclic, mover, level, option, degree, step, run, start, state, IDEAL-ACYC | RESULTS R104 (the premise; packet §0) |
| LOCAL, key half | RESULTS R105 (the premise; G-4) |
| N, T, Mv_t, C_l, C_(−1), n_l, [a, b], d | IN |
| l (SEG) | implicit «for every l ≥ −1» (packet l. 47; G-3 (ii); optional SEG-L1 / P-2) |
| l (LEVEL-PRODUCT) | IN («for every l ≥ −1») |
| s_(a−1), s_b, s_9 | the state after step t (packet §0 l. 36-39; G-3 (i)) |
| level-0 move, above level 0 | a step moving a level-0 mover; on the movers of level ≥ 1 (packet l. 107-109, 119; G-3 (iv)) |
| d-level ladder with two movers of degree 2 per level; 5-level 2-wide ladder | packet §0 l. 42 (G-2 (x)) |
| REPLAY's text in «…» | the line's paraphrase of §4 l. 107-109 (G-8) |
| max_d5_L15, its stored start, sha1 ba963ace… | data objects (G-2 (xii); body Object) |
| L-RED R202 | attribution, prefixed |
| DATA clause: 59 / 34,934 runs, 652 / 57,755 intervals; segcheck.py | DATA, cited (G-9) |
Agreeing tests: REFEREE §5 l. 88-110; REFEREE-2 l. 91-116.
(8) FIXES AND STATUS NOTES (docs/new/P-IDEAL-SEG-fixes.md, L-NEW successor 51, append-only, one entry, one commit): at 6eb389a6 sha1
2e3dd53211b44ca752611aadf4f30e5a0e7c165f, 20 lines (unchanged at the l-new head 16297185; REFEREE's FYI item checked this version:
R-P-IDEAL-SLOT.md l. 155 «docs/new/P-IDEAL-SEG-fixes.md sha1 2e3dd532, 20 lines»). Header (l. 1-3): «(append-only; the packet
docs/new/P-IDEAL-SEG.md and line L-1 stay frozen)», the routing. Entry 1 (l. 5-20, «REFEREE-2 F-1, F-2»): F-1 (l. 6-12) replaces packet
l. 140's parenthesis by «(reached only by genomes with at most one degree-2» «mover, e.g. r150_049.json with none: T 0, product 1)»; F-2
(l. 13-19) replaces packet l. 105-106's quote by «(docs/new/N5-SEG-box157.md l. 24: «after a level-0 reset, the next segment is a
sub-run of a segment already seen»; the reading «no new states above» is my paraphrase)», the killed statement unchanged (l. 19). No fix
changes a signed statement or L-1 (l. 20). The packet file itself is unchanged since 8291ecf7 (sha1 7fa84784… at 8291ecf7 and at
16297185).
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-1 states no CONJECTURE and kills nothing of RESULTS or GAPS (REPLAY occurs 0 times
there). A line-11 UPDATE is proposed at the end, to go AFTER R107's UPDATE (GAPS at 6f1be9e2: the last UPDATE on l. 11 is R107's «UPDATE
2026-11-04 13:41Z: RESULTS R107 (P-IDEAL-M2; CHECKER C118 914d073f) [refereed-only] LANDED: …», ending «G-N5-TIME stays open.» before
the row's closing « |»; l. 11 holds 76 "|" and 42 «UPDATE 2026-»), as a pure insertion with one separating space. BUILT FROM L-1
(scratch upd108.py: upd107.py's controls and procedure unchanged, upd100L3.py's build() unchanged). CONTROLS (same script, same run, rc
0): R97's to R107's LANDED UPDATEs (GAPS l. 11 at 6f1be9e2) rebuilt from their lines byte for byte (True ×11; R107's from P-IDEAL-M2 L-2
at 4d244698 with head «UPDATE 2026-11-04 13:41Z: RESULTS R107 (P-IDEAL-M2; CHECKER C118 914d073f) [refereed-only] », 2,647 bytes, also
equal to R107-draft l. 603 with <DATE> 2026-11-04, <HH:MM> 13:41, <checker> 914d073f). R108: R107's procedure unchanged (C118 §4:
«Ruling: PASS. The rule is R105's / R106's, plus «a clause that carries its own lead-in stays as it is».»): L-1's claim body ends with
the unlabelled clause «; and DEAD: the lane conjecture REPLAY … sha1 ba963ace…)» after the last labelled clause (LEVEL-PRODUCT); the
procedure runs on L-1 with that clause cut out (build()'s label move on the claim body plus a sentinel tail, start «with two options: »,
3 labels, each found once after it, in order; « (2026-11-04) — » → «: »; the DATA parenthesis before the source parenthesis opened as «;
DATA: …»; «; G-N5-TIME stays OPEN» and «; not M3, not a step-4 pass, not a TARGET.md claim» dropped; the source parenthesis kept; «.
G-N5-TIME stays open.» appended), and the clause is put back verbatim between the moved «(LEVEL-PRODUCT)» and the tail's «: » (one
occurrence, by script). The DEAD clause carries no label, so nothing in it moves; its guillemet text stays. L-1 holds no "|", so no
replacement list. Checked by script: one line, 0 "|", one «<DATE>», one «<HH:MM>», one «<checker>», 2,077 bytes, 371 tokens;
«2026-11-04» 0 times (the date parenthesis is dropped by the rule); token multiset diff against L-1 = the head, the three moved labels,
«(DATA:» opened, the two dropped scope sentences, « — » and the final sentence (upd108.out). Head «UPDATE <DATE> <HH:MM>Z: RESULTS R108
(P-IDEAL-SEG; CHECKER C120 <checker>) [refereed-only] » («P-IDEAL-SEG» 0 times in GAPS and RESULTS); <DATE> = the landing date.
(10) DATA of record = packet §5 (l. 126-152) with fixes entry 1 F-1 for l. 140, NOT signed; L-1's DATA parenthesis states its counts.
Re-run at this fill (scratch, git archive of 6eb389a6's experiments and docs/new; between 8291ecf7 and 6eb389a6 the files the blocks
read are unchanged (box157, box150, box139, box14*, box152, box153, box156/ext, by git diff --stat) and check.sh changes only l. 882-884
(pin107 extended) and l. 888-903 (P-IDEAL-SLOT); from experiments/new, as check.sh's «cd»), 2026-11-04T14:59:57Z-15:00:13Z, rc 0,
outputs w106.out, w107.out, pin107.out and blocks.out:
- w106: «SEGCHECK runs 59 steps 650 intervals 652 SEG 0 ONCE 0 COUNT 0 PROD 0 maxratio 0.3333», «SEGCHECK runs 34934 steps 38676
  intervals 57755 SEG 0 ONCE 0 COUNT 0 PROD 0 maxratio 1.0» and the BADLEV=2 control «SEGCHECK runs 59 steps 650 intervals 652 SEG 0
  ONCE 112 COUNT 0 PROD 0 maxratio 0.3333»: byte-equal to the block's grep -qxF strings.
- w107: «max_d5_L15.json N 10 T 15 L 0 cuts [7, 8]», «  seg t1-6 len 6 NEWSTATES 6 REPLAY False: [(5,), (9,), (7,), (6, 8), (9,),
  (4,)]», «  CUT t7: (0, 2, 3)», «  CUT t8: (1,)», «  seg t9-15 len 7 NEWSTATES 7 REPLAY False: [(4,), (6, 7, 8, 9), (5,), (3,), (7,),
  (6, 9), (4,)]»: the block's three strings found (grep -qxF / grep -qF). pin107: packet 7fa84784…, L-1 a18f6f0c…, fixes 2e3dd532…,
  instance ba963ace… (sha1sum, full digests in pin107.out).
- The blocks as written (l. 873-887 at 6eb389a6, inside a shell with check.sh's «set -euo pipefail» and «cd»): «box 157 SEG / SEG-ONCE /
  LEVEL-PRODUCT: 0 violations (59 + 34,934 runs; BADLEV=2 control fires): PASS» and «P-IDEAL-SEG: REPLAY DEAD data on max_d5_L15
  (segment t9-15 all new); pins packet 7fa84784, line L-1 a18f6f0c, fixes 2e3dd532: PASS».
- My own simulator (scratch mysim.py, written from RESULTS R104's text and packet §0, β-SETS compared by the largest-rank β of the
  symmetric difference, keys under the new state level by level; no lane code imported), 15:0xZ, rc 0, output mysim.out: the instance is
  acyclic, ranks and gates distinct, every W-target one level down, every mover of degree 2, two movers on each of levels 0-4; from the
  stored start T 15, and the states s_0 … s_15 equal packet §4 l. 114-117 state for state (by script); movers per step «[(5,), (9,),
  (7,), (6, 8), (9,), (4,), (0, 2, 3), (1,), (4,), (6, 7, 8, 9), (5,), (3,), (7,), (6, 9), (4,)]» (= REFEREE-2 l. 58-59); level-0 steps
  [7, 8]; new above level 0 at t = 9, …, 15; s_9 above level 0 (0, 0, 0, 1, 1, 1, 0, 0); C_(−1), …, C_4 = 0, 2, 3, 8, 13, 15 and every
  COUNT inequality holds; T + 1 = 16 ≤ 243 = 3^5.
- My split of the DATA by degree (scratch split.py and ratio.py on the archive, 15:06:15Z-15:06:18Z, rc 0, split.out): see G-9. Corpus
  59 = 55 (degree ≤ 2) + 4 (degree 3); random 34,934 = 1,936 (degree ≤ 2) + 32,998 (degree 3 or 4); intervals 652 = 499 + 153 and 57,755
  = 2,891 + 54,864; ratio 1 on the random runs only for r150_049.json (no degree-2 mover) and 12 genomes with one; corpus largest ratio
  0.3333.
- Code read (not run separately): segcheck.py builds H with box150/check.py restrict() («movers in keep get the single option sa(x)
  (same option record, gate, beta); start sa», l. 103), runs it from s_(a−1) with a step cap of T + 5, and compares its first b − a + 2
  states with s_(a−1), …, s_b; ONCE, COUNT and PROD run only «if D <= 2» (D the largest degree of the genome).
NOT re-run: the referees' tools (docs/referee/scratch/seg_probe.py; docs/referee-2/R2-P-IDEAL-SEG/seg_check.py); I read REFEREE's
committed log (xinew_logs/seg_probe.txt at 19e0742f: seeds 1, 2 «'runs': 3000» each, steps 3,118 + 3,121, «'once': 0, 'count': 0,
'prod': 0», «'maxT': 4» and «'maxT': 3»; seed 3 mut 1 «'once': 1»), which equals REFEREE §3 l. 79-81; REFEREE-2 committed no log for
seg_check.py. check.sh's other blocks and scripts/verify.sh: not run.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 REFEREE calls the CHAINED defect «R105's erratum E-1» / «R105 E-1»
(l. 31, 121); in RESULTS it is Erratum E-2 (E2a) (G-5). D-2 REFEREE l. 32 «It is not yet in docs/RESULTS.md at 18c288c6.»: true at
18c288c6, superseded by 6f1be9e2 (G-5). D-3 the packet's DATA remark at l. 140 and the lane source l. 23 overstate the ratio-1 genomes
(F-1; G-11 (i), (iii)). D-4 the packet's quote of the lane proposal at l. 105-106 is not verbatim (F-2; G-11 (ii)). D-5 the Lead stamps
11:49Z (packet l. 2) and 13:14Z (fixes l. 2) vs the commits 8291ecf7 (11:48:36Z) and f71e80ea (13:12:25Z) (G-11 (v)). D-6 REFEREE-2 l.
75 «the 55 degree-2 box-14x/15x corpus genomes»: the 55 degree-≤-2 corpus genomes include box156/ext (3) and box157/max_d5_L15 (my
split), not only boxes 14x / 15x; a looseness in the report's words, no count affected. D-7 REFEREE-2 l. 2 «Independent: docs/referee/
not read before this push.» with its push at 12:31:18Z, after REFEREE's report commit 12:17:57Z (independence as stated by REFEREE-2;
REFEREE l. 2 «Independent: I did not read docs/referee-2/.»). D-8 REFEREE checked fixes entry 1 inside its P-IDEAL-SLOT report
(R-P-IDEAL-SLOT.md §C, «### FYI item»), not in R-P-IDEAL-SEG.md (G-13). D-9 the packet's SEG-ONCE proof (§2 l. 76-79) argues with the
packet's own KP and LOCAL's key half; the lane source calls it «the KEYFLIP argument of RESULTS R105» (N5-SEG-box157.md l. 76); the
packet governs (G-4).
(12) Excluded: packet §5 (DATA, EXCLUDED list, TARGET diff, READING); the §3 Remark (Π_l (n_l + 1) ≤ 2^(Σ_l n_l)); the slot-filling
reading and the L-RED target R203 (packet l. 143; L-RED's R203 witness at 0f7508cf is not read for this entry); the «pattern replay»
observations on max_d4_L13 / g4_L12 / x3_L8 (l. 144); every READING of docs/new/N5-SEG-box157.md (l. 145), including its comparison with
EXACT-ENERGY; the referees' own random and climb counts (DATA about the statements, not part of this entry beyond the Data bullet);
fixes entry 1 as a statement; P-IDEAL-SLOT (which carries SEG and SEG-ONCE as copies, REFEREE R-P-IDEAL-SLOT.md l. 11, and is a separate
packet). Not part of this entry.
(13) Commits: lane (claude/l-new): e132d498 (2026-11-04T11:05:05Z; «L-NEW box 157 (pre-GO, DATA): seg.py, level-0 segmentation / replay
test of ladder champions») → 6273270f (11:25:28Z; box 157 source docs/new/N5-SEG-box157.md, segcheck.py, the instance copy, check.sh
block w106) → 8291ecf7 (11:48:36Z; freeze: packet +152, L-1 +1, check.sh +8, block w107 / pin107) → 6eb389a6 (13:27:06Z; fixes +20,
pin107 extended; also P-IDEAL-SLOT files, not this entry's) → 16297185 (13:48:03Z; box 156 park notes; no P-IDEAL-SEG file). The
instance file: l-red 05c48415 (2026-11-04T09:04:24Z), unchanged at the l-red head 0f7508cf; l-new copy 6273270f. REFEREE
(claude/referee): 19e0742f (12:17:57Z; report, new file 122 lines, sha1 8f7815d6…; scratch/seg_probe.py sha1
8492ee53c71c9b224c8aed3ca2b5c5fc8853af78, xinew_logs/seg_probe.txt sha1 7389f8aad82a4a17f490bb88c4c3d6a29a935e5d) → 2a09dcf8 (13:15:02Z;
P-IDEAL-SLOT report) → 3b8a9c77 (13:50:44Z; P-IDEAL-SLOT §C with the FYI item on P-IDEAL-SEG fixes entry 1, +28 lines). REFEREE-2
(claude/referee-2): 9a746361 (12:31:18Z; report, new file 119 lines, sha1 296015a8…; R2-P-IDEAL-SEG/seg_check.py, 117 lines, sha1
2a5915be3a6fe14da92223f162e0022e86a4e224) → cdf8e962 (13:17:15Z; P-IDEAL-SLOT report). CHECKER: C118 / C119 Add. 1 PASS (914d073f); none
yet for R108 (C120). Lead: 18c288c6 (GO), f71e80ea (signed, fix round). Trunk: see the header.
(14) Placement: see (0). DEAD-ENDS ROW: NONE (not drafted). R108 kills a lane conjecture (REPLAY) by an explicit refereed instance
inside its line. CHECKER C118 §5 confirmed «no row» for the same class (R107's LIN-156): «DE37: the Lead's «no row» is CONFIRMED.», with
the precedent «the lane statements killed inside landed lines, REP-LIN (R90), BIP-REL-1 (R95), frz32 (R100), fbg_K12 (R101)» «and odxi
(R103)» and «DE34-DE36 are candidate algorithms and a proof route, a different class.». REPLAY occurs 0 times in RESULTS and GAPS, so no
fleet conjecture or route depends on it; R108's line records the instance and its numbers, and the body inlines the instance (Object,
Claims (d)), so CLAUDE.md's «Record every dead end with the exact obstruction and the instance that killed it.» is met inside RESULTS.
The next free Dead-ends number stays DE37 («DE37» 0 times in RESULTS).
### R108 [refereed-only] In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of R104 used; and RESULTS R105's LOCAL, key half only), on acyclic Ξ-graphs, any number of movers per level, with N movers, T the number of steps of a run from a given start, Mv_t the movers of step t, C_l the number of steps whose movers include one of level at most l (C_(−1) := 0) and n_l the number of movers of level l with two options: (SEG) at any degree, if no step of an interval [a, b] of steps moves a mover of level at most l, then the genome in which every mover of level at most l keeps only its option at s_(a−1) runs from s_(a−1) through exactly the states s_(a−1), …, s_b first; and at degree ≤ 2 only: (SEG-ONCE) on such an interval every mover of level l + 1 moves at most once, so every level-0 mover moves at most once in a whole run; (LEVEL-PRODUCT) C_(l+1) + 1 ≤ (C_l + 1)(n_(l+1) + 1) for every l ≥ −1, hence T + 1 ≤ the product over all levels l of (n_l + 1), and T ≤ 3^d − 1 on a d-level ladder with two movers of degree 2 per level; and DEAD: the lane conjecture REPLAY («in every degree-≤-2 IDEAL-ACYC run, every state inside a maximal interval of steps without a level-0 move that follows a level-0 move agrees on all movers of level ≥ 1 with some state before that interval») is false, by L-RED R202's 5-level 2-wide ladder max_d5_L15 from its stored start (N 10, T 15; level-0 moves only at steps 7 and 8; s_9 is new above level 0; sha1 ba963ace…) (2026-11-04) — an EXPONENTIAL count bound and a restriction lemma inside the IDEAL model; bounds nothing polynomially; degree ≥ 3 is not covered by SEG-ONCE or LEVEL-PRODUCT; Ξ-cyclic genomes are not covered; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (DATA: 0 violations on 59 corpus runs with 652 intervals and on 34,934 random runs (every start for N ≤ 8, the genome start otherwise) with 57,755 intervals, experiments/new/box157/segcheck.py) (P-IDEAL-SEG, docs/new/P-IDEAL-SEG.md; L-NEW successor 51), CHECKER PASS (docs/checker/C120.md, checker PENDING)
- Object (L-NEW successor 51, Opus 5.5, D14 / D18; frozen, unchanged during review): packet P-IDEAL-SEG, docs/new/P-IDEAL-SEG.md, sha1
  7fa847843cb950e87dac38bf3d612effd5a9834e, 152 lines (l-new freeze 8291ecf7, 2026-11-04T11:48:36Z, the file's only commit; identical at
  16297185). Both referees measured the sha1 (REFEREE l. 4 «docs/new/P-IDEAL-SEG.md: sha1 7fa847843cb950e87dac38bf3d612effd5a9834e, 152
  lines;»; REFEREE-2 l. 5 «docs/new/P-IDEAL-SEG.md sha1 7fa847843cb950e87dac38bf3d612effd5a9834e, 152 lines»). Title (l. 1): «Packet
  P-IDEAL-SEG (box 157): stretches without low-level moves (SEG, SEG-ONCE) and the level-product bound T + 1 ≤ Π_l (n_l + 1) at degree ≤
  2 (LEVEL-PRODUCT); DEAD: REPLAY». Status (l. 5-7): «Not a TARGET.md claim.» «Every statement is about the IDEAL-ACYC model only. No
  polynomial bound is claimed anywhere: LEVEL-PRODUCT is an EXPONENTIAL bound.» «G-N5-TIME stays OPEN.» To sign: §1 Lemma SEG, §2 Lemma
  SEG-ONCE, §3 Corollary LEVEL-PRODUCT, §4 the DEAD of REPLAY (table l. 9-16); §5 «DATA / READING (not to sign)». Sections: premises (l.
  18-23), §0 the model (l. 25-43), §1 (l. 45-68), §2 (l. 70-82), §3 (l. 84-102), §4 (l. 104-124), §5 machine check, EXCLUDED, TARGET
  diff, READING (l. 126-152). Source: «Source: docs/new/N5-SEG-box157.md §1 (box 157). This packet governs: every proof below is written
  out in full here and is» «checked against this text only.» (l. 4-5).
  Fixes: docs/new/P-IDEAL-SEG-fixes.md, fixes entry 1 (append-only; one commit, 6eb389a6; 20 lines, sha1
  2e3dd53211b44ca752611aadf4f30e5a0e7c165f). Entry 1 makes two text corrections outside the signed statements (REFEREE-2 F-1: the §5
  DATA remark; F-2: the §4 quote of the lane proposal): «Line L-1 is unchanged. No statement or DATA count changes.» (l. 20). The packet
  read with entry 1 is the text of record.
  The RESULTS line is L-1, a18f6f0c61d6d5f33adc61519d94252dd5ba9721 (docs/new/P-IDEAL-SEG-line-L1.txt, l-new 8291ecf7, frozen with the
  packet, the file's only commit). The title is L-1 verbatim, with nothing inserted (its date parenthesis «(2026-11-04)» and its source
  note are the line's own). L-1 MATCHES at both referees: REFEREE (19e0742f) l. 110 «VERDICT: line L-1 MATCHES.», and after fixes entry
  1 «Neither fix touches a signed statement or line L-1. P-IDEAL-SEG L-1 stays MATCHED.» (docs/referee/R-P-IDEAL-SLOT.md l. 160,
  3b8a9c77); REFEREE-2 (9a746361) l. 119 «Gaps: none. Line L-1: MATCHES.». Both diffed every definition in L-1 against the packet
  (REFEREE §5 l. 88 «with the new rule: every DEFINITION diffed against the packet»; REFEREE-2 l. 91 «clause by clause, every definition
  against the packet»). Optional line items not taken: REFEREE SEG-L1 and REFEREE-2 P-2 (bind «l ≥ −1» in SEG), REFEREE-2 P-1 (ladder
  wording), P-3 (REPLAY's guillemets), P-4 (DATA degree note).
  Setting (packet §0, l. 25-43; RESULTS R104's model in R105's notation): a genome G has N ≥ 1 movers x with levels lev(x) and deg(x) ≥
  1 options (x, k), M := Σ deg(x), each option with a W-target one level down (none at level 0), a Ξ-target (a mover or the exit X), a β
  with a distinct rank and a parity, and a distinct gate index; a start s_0 (l. 26-29); the Ξ-graph and IDEAL-ACYC (l. 30); chains,
  Ξ-values and the comparison (l. 31-33); A_s(x) (l. 34); keys (l. 35); the step under the NEW state's keys, level by level, and «T :=
  the number of steps.» (l. 36-38); Mv_t, the movers of step t (nonempty for t ∈ [1, T]), and «A mover of degree 1 has A_s(x) = {s(x)}
  always and never moves.» (l. 39); at degree ≤ 2, KP_s(x) := the option of x with the smaller key under s, and «If x ∈ Mv_t, both
  options lie in A_(s_(t−1))(x), and the step rule gives s_t(x) = KP_(s_t)(x).» (l. 40-41); «d-level 2-wide ladder: a genome with levels
  0, …, d − 1, exactly two movers per level, all of degree 2 (N = 2d).» (l. 42); «No width hypothesis is made in §1-§3: every level may
  hold any number of movers.» (l. 43). Notation of the line: s_t is the state after step t (s_0 the start); C_l and n_l are defined in
  §3 (Claims (c)).
- Claims signed (REFEREE successor 23 «(Opus 5.5, D15)», report 19e0742f; REFEREE-2 successor 27 «(Opus 5.5, D12/D19)», report
  9a746361). Items (a)-(d) are SIGN in both verdict tables (REFEREE "## 0. Verdicts" l. 9-17 of R-P-IDEAL-SEG.md; REFEREE-2 "##
  Verdicts" l. 10-18 of R2-P-IDEAL-SEG.md), with no gap in either report (REFEREE l. 119 «SEG, SEG-ONCE, LEVEL-PRODUCT and DEAD REPLAY:
  all SIGN, no gap.»; REFEREE-2 l. 18 «Gaps: none.»); the table is to-check (4). (a) holds for every IDEAL genome with an acyclic
  Ξ-graph at ANY degree, (b) and (c) at degree ≤ 2 only, all at any width; (d) is one explicit instance. No item bounds a count
  polynomially; (c) is an exponential bound.
  (a) Lemma SEG (§1, l. 45-68; IDEAL-ACYC, any degree, any width): «Let l ≥ −1, and let [a, b] ⊆ [1, T] be an interval of steps such
      that Mv_t contains no mover of level ≤ l for every t ∈ [a, b].»; «Let H be the genome G in which every mover x of level ≤ l keeps
      only the option s_(a−1)(x), with the same W-target, Ξ-target, β» «and gate.»; «Then the run of H from s_(a−1) has s_(a−1), s_a, …,
      s_b as its first b − a + 2 states (so H takes at least b − a + 1 steps).» (l. 47-50). Proof (l. 51-67): H is an IDEAL-ACYC genome
      (its options are options of G, its Ξ-graph a subgraph); by induction on t ∈ [a, b], (i) the chain of every option of a non-frozen
      mover is the same option sequence in H and G, so the Ξ-values and A_s agree; (ii) a frozen mover has a single available option;
      (iii) level by level the keys under the two new states are equal by RESULTS R105 (LOCAL), «a key only on the states below its
      level», so H's new state is s_t; (iv) H passes both stop tests. «Does NOT claim: anything about H's run after state s_b; any count
      bound.» (l. 68). Cells: REFEREE «SIGN» (l. 12; §2 l. 36-44, «Correct.»); REFEREE-2 «**SIGN** (Opus 5.5, D12)» (l. 13; l. 30-41).
  (b) Lemma SEG-ONCE (§2, l. 70-82; degree ≤ 2, any width): «With l and [a, b] as in SEG: every mover x of level l + 1» moves at most
      once in [a, b] (the number of t ∈ [a, b] with x ∈ Mv_t is at most 1, l. 71-72); «In particular (l = −1, [a, b] = [1, T]) every
      level-0 mover moves at most once in the whole run.» (l. 72). Proof (l. 73-80): two consecutive moves of x in [a, b] go b′ → a′ →
      b′; a′ = KP_(s_(t1))(x) and b′ = KP_(s_(t2))(x); KP_s(x) reads only movers of level < lev(x) = l + 1 (RESULTS R105 (LOCAL), «a key
      only on the states below its level»), which do not move in [a, b]; so a′ = b′, a contradiction. «Does NOT claim: anything at
      degree ≥ 3 (the proof uses that a mover with two options must return to the option it left); any bound» «on moves at levels ≥ l +
      2 inside [a, b].» (l. 81-82). Cells: REFEREE «SIGN» (l. 13; §2 l. 45-49); REFEREE-2 «**SIGN** (Opus 5.5, D12)» (l. 14; l. 42-46).
  (c) Corollary LEVEL-PRODUCT (§3, l. 84-102; degree ≤ 2, any width): «C_(−1) := 0»; for l ≥ 0, C_l := the number of steps t ∈ [1, T]
      whose Mv_t contains a mover of level ≤ l; «n_l := the number of degree-2» «movers of level l.» (l. 86-87). «Then C_(l+1) + 1 ≤
      (C_l + 1)(n_(l+1) + 1) for every l ≥ −1. Hence T + 1 ≤ Π_(l = 0..top) (n_l + 1), with top the largest level.» (l. 88); «On a
      d-level 2-wide ladder: T ≤ 3^d − 1.» (l. 89). Proof (l. 90-98): the C_l steps cut [1, T] into at most C_l + 1 maximal intervals; a
      step counted by C_(l+1) and not by C_l moves a degree-2 mover of level l + 1, at most once per interval for each of the n_(l+1)
      such movers (SEG-ONCE); «Every step moves some mover, so T = C_top.»; induction from C_(−1) + 1 = 1. «Does NOT claim: any
      polynomial bound (the bound is exponential in the number of levels holding a degree-2 mover); tightness; anything» «at degree ≥
      3.» (l. 101-102). The line's ladder clause («on a d-level ladder with two movers of degree 2 per level») also admits extra
      degree-1 movers; the bound holds for them by the product form (n_l = 2): REFEREE l. 95-96, REFEREE-2 l. 112-113 (P-1). Cells:
      REFEREE «SIGN» (l. 14; §2 l. 50-55); REFEREE-2 «**SIGN** (Opus 5.5, D12)» (l. 15; l. 47-51).
  (d) DEAD: CONJECTURE REPLAY (lane), in the packet's precise form (§4, l. 104-124). The killed statement (l. 107-109): «For every
      degree-≤-2 IDEAL-ACYC run and every maximal interval [a, b] of steps none of which moves a level-0 mover, with a ≥ 2» «(so step a
      − 1 moves a level-0 mover):» «every state s_t with t ∈ [a, b] agrees, on every mover of level ≥ 1, with some state s_j with j <
      a.». It is the precise form of the lane's box 157 proposal (fixes entry 1, F-2: «(docs/new/N5-SEG-box157.md l. 24: «after a
      level-0 reset, the next segment is a sub-run of a segment already seen»; the reading «no new states above» is my paraphrase)»),
      which implies it when states are compared above level 0 (REFEREE l. 57-60; REFEREE-2 l. 53-55). The instance max_d5_L15, in full:
      L-RED R202's witness, experiments/red/r202/max_d5_L15.json (claude/l-red 05c48415, the file's only commit, unchanged at 0f7508cf;
      L-RED pin max_d5_L15_n96), copied byte for byte to experiments/new/box157/max_d5_L15.json (claude/l-new 6273270f), sha1
      ba963aceabeb35d95f9c47d80d1d0e87b87baf21, 657 bytes, no trailing newline; box 139-150 JSON format (as for max_d4_L13 in RESULTS
      R107, Claims (g): option = [W-target, Ξ-target (−1 = X), β index]; br / bp: rank / parity of β index; gate per option); the file's
      fields, verbatim: «"N": 10, "lev": [0, 0, 1, 1, 2, 2, 3, 3, 4, 4], "deg": 2»; «"opts": [[[-1, 1, 0], [-1, 4, 1]], [[-1, -1, 2],
      [-1, 2, 3]], [[0, -1, 4], [1, -1, 5]], [[0, -1, 6], [1, 5, 7]], [[2, 1, 8], [3, 9, 9]], [[2, 8, 10], [3, -1, 11]], [[4, 4, 12],
      [5, 7, 13]], [[4, 4, 14], [5, 9, 15]], [[6, -1, 16], [7, 2, 17]], [[6, 8, 18], [7, 3, 19]]]»; «"gate": [[3, 1], [2, 0], [4, 7],
      [5, 6], [9, 11], [8, 10], [13, 14], [12, 15], [17, 18], [16, 19]]»; «"br": [9, 10, 2, 0, 19, 18, 17, 1, 11, 4, 6, 7, 13, 15, 14,
      16, 5, 8, 3, 12], "bp": [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1]»; «"start": [0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
      "xorder": [6, 7, 0, 4, 9, 3, 5, 8, 1, 2]». Packet l. 111-112: «It is a 5-level 2-wide ladder (N 10,» «degree 2). Run from its
      stored start [0, 0, 1, 1, 0, 0, 0, 0, 1, 0] with the box 150 simulator: T = 15.». The run (l. 113-117; option per mover 0..9,
      levels [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]): «s_0 (0 0 1 1 0 0 0 0 1 0), s_1 (0 0 1 1 0 1 0 0 1 0), s_2 (0 0 1 1 0 1 0 0 1 1), s_3 (0 0
      1 1 0 1 0 1 1 1);» «s_4 (0 0 1 1 0 1 1 1 0 1), s_5 (0 0 1 1 0 1 1 1 0 0), s_6 (0 0 1 1 1 1 1 1 0 0), s_7 (1 0 0 0 1 1 1 1 0 0);»
      «s_8 (1 1 0 0 1 1 1 1 0 0), s_9 (1 1 0 0 0 1 1 1 0 0), s_10 (1 1 0 0 0 1 0 0 1 1), s_11 (1 1 0 0 0 0 0 0 1 1);» «s_12 (1 1 0 1 0 0
      0 0 1 1), s_13 (1 1 0 1 0 0 0 1 1 1), s_14 (1 1 0 1 0 0 1 1 1 0), s_15 (1 1 0 1 1 0 1 1 1 0).». «The level-0 movers 0 and 1 move
      only at steps 7 and 8. So [9, 15] is a maximal interval with no level-0 move, and a = 9 ≥ 2.» (l. 118); «s_9 restricted to movers
      2..9 is (0 0 0 1 1 1 0 0). No s_j with j ≤ 8 has it: s_0 … s_6 have (1 1 …) on movers 2, 3; s_7 and s_8» «have (0 0 1 1 1 1 0 0).
      So REPLAY fails at t = 9.» (l. 119-120); «So REPLAY is DEAD.» (l. 122). «Does NOT claim: anything about other «replay» readings
      (e.g. repetition of mover sets, which does occur in max_d4_L13).» (l. 124). Cells: REFEREE «SIGN (recomputed independently)» (l.
      15; §2 l. 56-68: «T = 15. The states s_0 … s_15 EQUAL the packet's §4 list, state for state.», «All seven states s_9 … s_15 are
      new above level 0 (none equals any s_j, j ≤ 8, on movers 2..9). REPLAY fails at t = 9.»); REFEREE-2 «**SIGN** (Opus 5.5, D12):
      recomputed with my own simulator» (l. 16; l. 52-62: «T 15 and states s_0 … s_15» «IDENTICAL to packet §4 (all 16 compared)»,
      «REPLAY FAILS at t = 9. ✓»).
  The RESULTS line (L-1) states (a)-(d) with their exact hypotheses, and nothing wider (to check (4), G-2).
- Premise: RESULTS R104's definition of the IDEAL model and of the Ξ-graph (no R104 theorem), and RESULTS R105's LOCAL, key half only:
  «a key only on the states below its level» (R105's title line; body item (b) in the form «(c) key_s(x, k) = key_(s′)(x, k) whenever s
  and s′ agree on every mover of level < lev(x).»), quoted verbatim by the packet where it is used (REFEREE l. 26-27, REFEREE-2 l. 24,
  each «1 hit»). L-1: «premise: R104's definition of the model only, no theorem of R104 used; and RESULTS R105's LOCAL, key half only».
  Uses: SEG (iii) and SEG-ONCE, and LEVEL-PRODUCT through SEG-ONCE (REFEREE l. 28); SEG (i) argues directly and uses no value half of
  LOCAL (REFEREE l. 29-30). KP_s(x) is defined in packet §0 (l. 40-41), not cited from R105. Packet l. 20-22: «No other R105 item» «is
  used.»; «U, CHAIN-BACK and the CHAINED binder» … «are not used.»; «Not used: RESULTS R106, R107, docs/lit, docs/sources, any other
  lane file. No outside source is cited.»; both referees confirmed it by reading every proof step (REFEREE l. 31, 33; REFEREE-2 l.
  26-27). So RESULTS Erratum E-2 to R105, which corrects R105's CHAINED binder, TOP-MONO's RANK_t and KEYFLIP's moves(x), does not bear
  on this entry. The DEAD instance is a data file, recomputed by both referees with their own simulators (REFEREE
  scratch/xinew_probe.py, «my β-set simulator written from R104's text»; REFEREE-2 «My simulator (written from R104's text, β-SETS)»).
- L41 and L43. The proofs are L-NEW successor 51's (packet l. 5). Fixes entry 1 corrects two text items outside the signed statements,
  raised by REFEREE-2 (F-1, F-2); no line change was made; the instance is L-RED's. Nothing referee-originated is a premise or a proof
  step of the entry (my reading; neither referee mentions L41). The DEAD (d) refutes a universal statement with no constant by one
  explicit instance, recomputed and SIGNED by both referees: REFEREE-2 l. 108 «L43: universal finite statement killed by an explicit
  instance with its numbers. ✓».
- Fixes (docs/new/P-IDEAL-SEG-fixes.md, L-NEW successor 51, append-only, fixes entry 1; 6eb389a6, 20 lines, sha1
  2e3dd53211b44ca752611aadf4f30e5a0e7c165f).
  - Entry 1 (l. 5-20, «REFEREE-2 F-1, F-2»): «two text corrections outside the signed statements» (l. 5). F-1 (packet §5, l. 140): «The
    parenthesis is false. box150/out/rand/r150_049.json has degree ≤ 2 and NO degree-2 mover» «(N 1, one option). There T = 0 and Π (n_l
    + 1) = 1, so the ratio is 1 as well.» (l. 6-7); new text «Largest (T + 1) / Π (n_l + 1): 1/3 on the corpus, 1 on the random runs
    (reached only by genomes with at most one degree-2» «mover, e.g. r150_049.json with none: T 0, product 1).» (l. 9-10); «No DATA
    count changes.» (l. 12). F-2 (packet §4, l. 105-106): the quote of the box 157 proposal is made verbatim to
    docs/new/N5-SEG-box157.md l. 24 and the added words are labelled a paraphrase (l. 13-18); «The killed statement itself (the two
    bullets of §4 «For every degree-≤-2 …» and «every state s_t …») is unchanged.» (l. 19). «Line L-1 is unchanged. No statement or DATA
    count changes.» (l. 20). REFEREE (docs/referee/R-P-IDEAL-SLOT.md §C, «### FYI item: P-IDEAL-SEG fixes entry 1», 3b8a9c77, l.
    155-160): «F-1 is CORRECT. box150/out/rand/r150_049.json at 6eb389a6 has N 1 and degrees [1].», «F-2 is CORRECT.», «Neither fix
    touches a signed statement or line L-1.» REFEREE-2 raised both (R2-P-IDEAL-SEG.md l. 77-84: «A fixes-file correction suffices.»;
    «The killed statement is the explicit precise form, so nothing changes.»).
  No fix changes a signed statement (to check (8)).
- Not signed: packet §5 (machine check, EXCLUDED, TARGET diff, READING; «DATA / READING (not to sign)», l. 16), in particular its
  READING «LEVEL-PRODUCT locates all super-linear room of degree-2 runs in the «reset slots» C_(l+1) − C_l ≤ (C_l + 1) n_(l+1).» «A
  polynomial bound needs most slots to stay empty; an exponential family must fill them level after level. Neither is claimed.» (l.
  151-152); the §3 Remark «Π_l (n_l + 1) ≤ 2^(Σ_l n_l), with equality iff every n_l ≤ 1» (l. 99, «not to sign»); the segment-length
  comparison on max_d5_L15 (l. 123). OPEN, not claimed: any polynomial bound on T at degree ≤ 2; tightness of LEVEL-PRODUCT (l. 101);
  SEG-ONCE and LEVEL-PRODUCT at degree ≥ 3 (l. 81, 102); Ξ-cyclic genomes; other «replay» readings (l. 124); G-N5-TIME.
- Referee strengthening (NOT part of this entry; referee remarks and own checks):
  (i) REFEREE-2 l. 41: «Holds for ANY interval satisfying the hypothesis (not only maximal ones): my tool checks every sub-interval.»
      (SEG as stated already allows any interval; the lane tool checks maximal ones only.)
  (ii) REFEREE-2 l. 38-40 spells out SEG's stop-test step (iv), starting from «Mv_t ≠ ∅ contains no frozen mover».
  (iii) REFEREE-2 l. 45-46: at l = −1, «level-0 keys are single gates, constant: each level-0 mover moves at» «most once.»
  (iv) REFEREE l. 99: «A stricter reading of «before» (j < a − 1) gives a STRONGER conjecture, which the same instance also kills.»
  (v) Negative controls: the lane's BADLEV=2 (ONCE tested at level l + 2) gives «ONCE 112» on the corpus (packet l. 139; REFEREE-2 l. 72
      «= lane»); REFEREE's control (seed 3) gives 1 violation (l. 80).
- Honest limits: (i) An EXPONENTIAL count bound and a restriction lemma inside the IDEAL model: LEVEL-PRODUCT bounds T + 1 by Π_l (n_l +
  1), which is 3^d on a d-level 2-wide ladder; it bounds nothing polynomially; G-N5-TIME stays open; not M3, not a step-4 pass, not a
  TARGET.md claim. (ii) SEG holds at any degree; SEG-ONCE and LEVEL-PRODUCT need degree ≤ 2 (a moving mover with two options must return
  to the option it left); Ξ-cyclic genomes are not covered. (iii) The DEAD kills the packet's precise form of REPLAY (states compared on
  the movers of level ≥ 1, earlier states j < a), by one explicit instance (N = 10, T = 15, failure at t = 9); the lane's proposal
  «after a level-0 reset, the next segment is a sub-run of a segment already seen» is killed in that reading (REFEREE l. 57-60;
  REFEREE-2 l. 54-55 «in that reading»); other «replay» readings, such as repetition of mover sets, are not claimed (packet l. 124).
  (iv) SEG says nothing about H's run after s_b and gives no count (packet l. 68). (v) The DATA (0 violations) is per statement:
  segcheck.py checks SEG on all 59 corpus and 34,934 random runs (maximal intervals only), but SEG-ONCE and LEVEL-PRODUCT only on the
  runs of genomes of largest degree ≤ 2: 55 of the 59 corpus runs and 1,936 of the 34,934 random runs; REFEREE-2's own tool adds SEG on
  every sub-interval and further degree-2 and degree-3 sets (Data). (vi) Every statement is about R104's IDEAL model on acyclic
  Ξ-graphs; nothing is said about a real N5 run or a parity game beyond what R104 already says (packet l. 147-150). (vii) Premises:
  RESULTS R104's definition and RESULTS R105's LOCAL, key half only; no other R105 item, so RESULTS Erratum E-2 to R105 does not bear on
  it. No lit note, no lane file, no outside source. No Lean. (viii) Names: «SEG» here is a lemma label; it is not R83's segment count
  SEG(S) nor CONJECTURE SEG-RUN (GAPS l. 11), which this entry neither uses nor settles; the 2-wide ladder is packet §0's family (R105's
  «2-wide-ladder identity KF_x = F_(lev(x)−1)» is not used); SEG is not R105's INTERVAL-RESTRICT, which freezes movers by π at degree ≤
  2. (ix) The DEAD instance is L-RED's witness, used here only as a counterexample; its T is R104's number of steps.
- Data (DATA, not proof): experiments/new/box157/segcheck.py (l-new 6273270f, sha1 1989263bd2b4961b5a12803a2e769b7f63fab92a, 50 lines;
  for every level l ∈ {−1, …, top − 1} and every maximal interval of steps without a level-≤-l move: SEG at any degree, and ONCE, COUNT
  and PROD at largest degree ≤ 2) and experiments/new/box157/seg.py (l-new e132d498, sha1 12782e78b2bc07a3b40269872ede1bbdafc56662, 32
  lines; the segment data of §4), both on the box 150 simulator experiments/new/box150/check.py (l-new 0ebddcf5, sha1
  019de0f7b36dcbd47743b3d27b4a1a93549d574b, 214 lines; H built by its restrict()), wired into experiments/new/check.sh blocks w106 (l.
  873-879) and w107 / pin107 (l. 880-887 at 6eb389a6) with sha1 pins of the packet, L-1, the fixes and the instance; all three tools
  unchanged at 6eb389a6 and 16297185. Genome sets: the corpus, 59 genomes, one run each from its stored start: 55 of largest degree 2
  with N = 4..24 (boxes 140-153, box156/ext max_d4_L13, dbl_d3_F6, dbl_d4_F10, and box157/max_d5_L15) and the 4 degree-3 genomes of
  box139/genomes with N = 9..24 (SEG only); experiments/new/box150/out/rand, 200 random genomes with N = 1..10, every start of those
  with N ≤ 8 and the genome start of the others (34,934 runs, ALL=1 ALLN=8): 1,936 runs of its 93 genomes of largest degree ≤ 2 (N =
  1..10; all four checks) and 32,998 runs of its 107 genomes of largest degree 3 or 4 (N = 1..9; SEG only). Packet §5 (l. 135-141, with
  fixes entry 1 for l. 140): «DATA: 0 violations on 59 corpus runs (652 intervals).»; «DATA: 0 violations on 34,934 random runs:
  box150/out/rand, every start for N ≤ 8, the genome start otherwise; 57,755 intervals.»; «Negative control BADLEV=2 (ONCE tested at
  level l + 2): ONCE 112 on the corpus.»; «Largest (T + 1) / Π (n_l + 1): 1/3 on the corpus, 1 on the random runs (reached only by
  genomes with at most one degree-2» «mover, e.g. r150_049.json with none: T 0, product 1).»
  The blocks' outputs, reproduced by both referees and re-run for this draft (2026-11-04T14:59:57Z-15:00:13Z, from a `git archive` of
  6eb389a6's experiments, rc 0, byte-equal to the blocks' expected strings): «SEGCHECK runs 59 steps 650 intervals 652 SEG 0 ONCE 0
  COUNT 0 PROD 0 maxratio 0.3333»; «SEGCHECK runs 34934 steps 38676 intervals 57755 SEG 0 ONCE 0 COUNT 0 PROD 0 maxratio 1.0»; BADLEV=2
  «SEGCHECK runs 59 steps 650 intervals 652 SEG 0 ONCE 112 COUNT 0 PROD 0 maxratio 0.3333»; «max_d5_L15.json N 10 T 15 L 0 cuts [7, 8]»,
  «seg t1-6 len 6 NEWSTATES 6 REPLAY False», «seg t9-15 len 7 NEWSTATES 7 REPLAY False». REFEREE §3 l. 70-77 («The output equals
  check.sh's three expected strings verbatim:», «These are the expected strings.», «pin107: packet 7fa84784, L-1 a18f6f0c and instance
  ba963ace all EQUAL.»); REFEREE-2 l. 65-68 («both PASS, exit 0.»).
  REFEREE (successor 23; own docs/referee/scratch/seg_probe.py, sha1 8492ee53c71c9b224c8aed3ca2b5c5fc8853af78, on its β-set simulator;
  log xinew_logs/seg_probe.txt): «6,000 random degree-≤-2 runs (seeds 1, 2): SEG-ONCE per maximal interval and every level 0,
  LEVEL-PRODUCT per level 0, PROD 0.», control «Control (ONCE tested at level l + 2), seed 3: 1 violation.», and «My random runs are
  short (T ≤ 4), so this DATA is weak.» (l. 79-81); the instance recomputed, T = 15, states equal (l. 61-68).
  REFEREE-2 (successor 27; own docs/referee-2/R2-P-IDEAL-SEG/seg_check.py, sha1 2a5915be3a6fe14da92223f162e0022e86a4e224, «lane
  restrict()/segcheck not imported», no committed log): SEG on every sub-interval, ONCE, COUNT, PROD, the ladder bound, T = C_top and
  the interval count; the corpus «runs 59, steps 650, intervals 652 (= lane), 12,175 sub-intervals; 0 violations»; box150/out/rand «runs
  34,934, steps 38,676, intervals 57,755 (= lane); 0 violations»; beyond the lane, «18,584 runs, 694 2-wide ladders» of random degree-2
  ladder genomes, degree 3 (SEG only) «55,964 runs, 91,682 sub-intervals», «climbs on 60 degree-3/4 genomes: 18,060 runs», and climbs of
  T on the corpus «33,220 runs, 240,850 intervals, max T 27, ladder ratio (T + 1) / 3^d at most 0.4545. All 0 violations.» (l. 69-76);
  the instance recomputed (l. 56-60).
  No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-P-IDEAL-SEG.md: successor 23's report 19e0742fd7cc475249fe245fcce5ff2b413e56d4
  (2026-11-04T12:17:57Z, new file, 122 lines, sha1 8f7815d658dca305d7dd88af5b39dfeb2c7b9f95, with scratch/seg_probe.py and
  xinew_logs/seg_probe.txt): SEG, SEG-ONCE, LEVEL-PRODUCT and DEAD REPLAY SIGN (l. 12-15, 119), «VERDICT: line L-1 MATCHES.» (l. 110);
  its FYI item on fixes entry 1 in docs/referee/R-P-IDEAL-SLOT.md §C, 3b8a9c777480d78867efd69e7f88f2d981898610 (2026-11-04T13:50:44Z, l.
  155-160): F-1 and F-2 «CORRECT», L-1 «stays MATCHED».
  REFEREE-2 (successor 27): docs/referee-2/R2-P-IDEAL-SEG.md 9a746361a58dad52af68eb02f55d1f87a7c0e9ce (2026-11-04T12:31:18Z, new file,
  119 lines, sha1 296015a81b765530a0259702cb93b12b0178b986; with R2-P-IDEAL-SEG/seg_check.py): every statement SIGN (l. 13-16, 119),
  «Gaps: none.» (l. 18), «Line L-1: MATCHES.» (l. 119), findings F-1 and F-2 (l. 77-84). Lane: freeze and L-1
  8291ecf7d41bdc6fa31070c92f291d488d308519, fixes entry 1 6eb389a61e679ce6859d3af9ee9b4f4467cafa80.
  INDEPENDENCE: REFEREE l. 2 «Independent: I did not read docs/referee-2/.»; REFEREE-2 l. 2 «Independent: docs/referee/ not read before
  this push.». REFEREE's report (12:17:57Z) precedes REFEREE-2's (12:31:18Z) by 13 min; neither cites the other's. Each referee
  recomputed the instance with its own simulator written from R104's text.
  Differences, resolved: REFEREE alone raised SEG-L1 (= REFEREE-2 P-2); REFEREE-2 alone raised P-1, P-3, P-4 and the findings F-1, F-2
  (answered by fixes entry 1, which REFEREE checked as CORRECT). Both SIGN the same four statements with no gap and both MATCH L-1. No
  disagreement in substance.
- TARGET.md diff: TARGET.md §1-§3 define parity games («A parity game is G = (V, V_E, V_O, E, pr) with V finite»), the regions W_E, W_O,
  M4 (§2 «There is a deterministic algorithm A and a polynomial p such that for every parity game G, A on input G halts within» «p(n +
  m) steps and outputs the pair (W_E(G), W_O(G)).») and the word-RAM cost model; no statement of this entry mentions a parity game, a
  winning region, an algorithm's running time or a cost model (packet §5 l. 147-150 «No statement mentions a parity game, a winning
  region, an algorithm's running time or a complexity class. Each is about the step» «sequence of the IDEAL model of RESULTS R104's
  definition.», «None is an M4 or M3 claim, none bounds anything polynomially, and none is a gauntlet step.»; REFEREE §4 l. 84-86
  «Agreed with §5: not M4, not M3, not a gauntlet step. G-N5-TIME OPEN.»; REFEREE-2 l. 87-89 «The packet's §5 diff is correct.»).
  LEVEL-PRODUCT is an exponential bound inside the model, «not a» «claim about any algorithm» (REFEREE-2 l. 88-89); the DEAD «refutes a
  lane conjecture about the model» (REFEREE l. 85). The line (L-1) makes no M4 claim and no TARGET claim; its tail reads «an EXPONENTIAL
  count bound and a restriction lemma inside the IDEAL model» and «G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md
  claim» (L-1, by script). Not a step-4 pass. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER R107's UPDATE of G-N5-TIME (GAPS at 6f1be9e2, last changed by 6f1be9e2: the last
UPDATE on l. 11 is R107's, «UPDATE 2026-11-04 13:41Z: RESULTS R107 (P-IDEAL-M2; CHECKER C118 914d073f) …», before the row's closing «
|»), built by script (upd108.py: upd100L3.py's build() unchanged for the label move, on the claim body with a sentinel tail as for R102
and R105-R107; the tail rule of (9) with R107's step for the unlabelled DEAD clause; to check (9)) only from the clauses of the title
line L-1: labels behind their clauses; the DEAD clause verbatim after (LEVEL-PRODUCT); « (2026-11-04) — » → «: »; the DATA parenthesis
before the source parenthesis opened as «; DATA: …»; «G-N5-TIME stays OPEN» and «not M3, not a step-4 pass, not a TARGET.md claim»
dropped; the source parenthesis kept; «. G-N5-TIME stays open.» at the end. The same script reproduces R97's to R107's LANDED UPDATEs
(GAPS l. 11) byte for byte. L-1 holds no "|"; the UPDATE holds none. <DATE> is the landing date (YYYY-MM-DD, by date -u at the landing
commit; C114 Add. 1 E-1), <HH:MM> the landing time and <checker> the CHECKER C120 commit, all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R108 (P-IDEAL-SEG; CHECKER C120 <checker>) [refereed-only] LANDED: In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of R104 used; and RESULTS R105's LOCAL, key half only), on acyclic Ξ-graphs, any number of movers per level, with N movers, T the number of steps of a run from a given start, Mv_t the movers of step t, C_l the number of steps whose movers include one of level at most l (C_(−1) := 0) and n_l the number of movers of level l with two options: at any degree, if no step of an interval [a, b] of steps moves a mover of level at most l, then the genome in which every mover of level at most l keeps only its option at s_(a−1) runs from s_(a−1) through exactly the states s_(a−1), …, s_b first (SEG); and at degree ≤ 2 only: on such an interval every mover of level l + 1 moves at most once, so every level-0 mover moves at most once in a whole run (SEG-ONCE); C_(l+1) + 1 ≤ (C_l + 1)(n_(l+1) + 1) for every l ≥ −1, hence T + 1 ≤ the product over all levels l of (n_l + 1), and T ≤ 3^d − 1 on a d-level ladder with two movers of degree 2 per level (LEVEL-PRODUCT); and DEAD: the lane conjecture REPLAY («in every degree-≤-2 IDEAL-ACYC run, every state inside a maximal interval of steps without a level-0 move that follows a level-0 move agrees on all movers of level ≥ 1 with some state before that interval») is false, by L-RED R202's 5-level 2-wide ladder max_d5_L15 from its stored start (N 10, T 15; level-0 moves only at steps 7 and 8; s_9 is new above level 0; sha1 ba963ace…): an EXPONENTIAL count bound and a restriction lemma inside the IDEAL model; bounds nothing polynomially; degree ≥ 3 is not covered by SEG-ONCE or LEVEL-PRODUCT; Ξ-cyclic genomes are not covered; DATA: 0 violations on 59 corpus runs with 652 intervals and on 34,934 random runs (every start for N ≤ 8, the genome start otherwise) with 57,755 intervals, experiments/new/box157/segcheck.py (P-IDEAL-SEG, docs/new/P-IDEAL-SEG.md; L-NEW successor 51). G-N5-TIME stays open.

Addendum (subagent, for the Lead; does not land; written 2026-11-04T15:16:49Z by date -u). (1) FIRST FILL on line L-1 (l-new 8291ecf7,
sha1 a18f6f0c…), to CHECKER C120. L-1 MATCHES at both referees (REFEREE 23 19e0742f, and «stays MATCHED» after fixes entry 1 at
3b8a9c77; REFEREE-2 27 9a746361). NOT pushed; the only commit made is the merge dee561d2 (the l-new, referee and referee-2 heads into
trunk 6f1be9e2, as briefed; the checker head was already in 6f1be9e2); no tracked file edited; this file is new and untracked. The
commits 6273270f, 8291ecf7, 6eb389a6, 16297185, 19e0742f, 2a09dcf8, 3b8a9c77, 9a746361 and cdf8e962 are on local trunk dee561d2 but not
on origin trunk 6f1be9e2 at this fill (header): push trunk before landing. (2) TITLE l. 413 = "### R108 [refereed-only] " + L-1
without its newline + ", CHECKER PASS (docs/checker/C120.md, checker PENDING)", checked by script after the fill (fill108.py,
chk108.py): equal, byte for byte (True); the only «### R» heading of this file. (3) BODY l. 413-629 (title l. 413 to the last
body line; 0 "|" in the range, by script); GAPS preamble l. 631-639 (its only "|" are the two inside the quoted closing « |», as
in R107's preamble); UPDATE l. 640 (one line, 0 "|", one <DATE>, one <HH:MM>, one <checker>; controls True ×11: R97's-R107's landed
UPDATEs). No Dead-ends row is drafted ((14)). A landing script in the shape of land107.py slices d[412:629] for the entry and
reads d[639] for the UPDATE. (4) RE-RUNS: check.sh blocks w106 and w107 / pin107 from a git archive of 6eb389a6
(14:59:57Z-15:00:13Z, rc 0, byte-equal to the expected strings, two PASS lines); my own simulator on the instance and my split of the
DATA by degree (15:0xZ, rc 0) ((10)). NOT RUN: the referees' tools (REFEREE's log read instead; REFEREE-2 has none), the full check.sh,
scripts/verify.sh. (5) QUOTE SWEEP: chk108.py (q104.py's rule as in chk107.py: outermost guillemet quotes, whitespace joined, split at
the ellipsis, parts of 6+ characters; sources: packet, L-1, fixes, the referee files at their head commits (R-P-IDEAL-SEG.md,
R-P-IDEAL-SLOT.md, R2-P-IDEAL-SEG.md), REFEREE's log, the referees' tools, notes/L-NEW.md at 6eb389a6, docs/new/N5-SEG-box157.md at
6273270f, check.sh at 8291ecf7 and 6eb389a6, the lane tools, the instance JSON, RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, NOW,
TARGET.md, CLAUDE.md, C117, C118, C119, notes/CHECKER.md, R107-draft, my re-run outputs, the commit subjects cited): 538 outermost
quotes, 481 parts of 6+ characters, every part found (0 not found); in the title and body alone 171 quotes, 173 parts, 0 not found; GAPS
preamble and UPDATE 9 quotes, 7 parts, 0 not found. Line-precise check of the referee verdicts and other cited lines: 182 of 182
(source, cited line range, quote) triples found verbatim, whitespace-normalised, inside the cited lines. Every sha1, line count and
commit time cited was re-measured in this session (sha1sum, wc -l, cmp, git log -1 on the commit), not copied from a report. (6)
DISCREPANCIES: see (11) (D-1 to D-9; none affects a verdict) and G-1 to G-13 (notes). I found no error in a signed statement and no
mismatch between a report and the lane files beyond D-6. (7) FLAGS LEFT FOR CHECKER: none REQUIRED from my side. Notes: G-9 (DATA per
statement: SEG-ONCE and LEVEL-PRODUCT are machine-checked on 55 + 1,936 runs, while the line's counts are 59 + 34,934; recommended: no
line change, body states the split; CHECKER rules), G-8 (L43 for a non-asymptotic universal statement; the killed form is the packet's
precise form), G-5 (Erratum E-2 does not bear; no landing condition), G-13 (REFEREE-2 has no committed check of fixes entry 1 at
cdf8e962), G-2 (x) (ladder wording admits degree-1 extras, covered by the product form), G-3 (s_t and SEG's l unbound in L-1), G-6
(«SEG» names). (8) NOT VERIFIED: the Lead GO of 11:49Z (packet l. 2) and the routing of 13:14Z (fixes l. 2) are not in the repository
beyond the Lead commits 18c288c6 and f71e80ea; REFEREE-2's runs have no committed log; the referees' tools were not re-run; L-RED R202's
exactness claim («T >= 15 SAT», «replay L 15 opt») is not used and not checked; whether REFEREE-2 will confirm fixes entry 1 (not
committed at this fill). Scratch files (not committed) in
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r108: R108-template.md, fill108.py,
chk108.py / chk108.out, lp108.py, upd108.py / upd108.txt / upd108.out, land108.py / land108.out, mksim.py, runall.sh, runblocks.sh,
blocks.out, w106.out, w107.out, pin107.out, mysim.py / mysim.out, split.py / ratio.py / split.out, the extracted sources (pkt.md,
fixes.md, L1.txt, ref.md, refslot.md, r2.md, notes.md, box157.md, cs_*.txt, gitlog.txt, lsremote.txt) and arch6eb3/ (the archive). (9)
LANDING SIMULATION (land108.py, on in-memory copies of RESULTS and GAPS at local trunk dee561d2): RESULTS 11,390 -> 11,608 lines, a pure
insertion of 218 lines (the entry block with "checker PENDING)" filled, plus one blank line) directly after R107's block (R107 l.
10593-10810, blank l. 10811, byte-unchanged: True): True; R108 at l. 10812-11028, blank l. 11029, the next line (**Erratum E-1**) moves
to l. 11030, «**Erratum E-2**» to l. 11043, «## Dead ends» to l. 11071; order R107, R108, E-1, E-2, Dead ends: True; every other line
byte-unchanged (common prefix and suffix: True); 0 "|" inserted. GAPS: only l. 11 changes: True; new l. 11 = old l. 11 with its closing
" |" replaced by " " + the filled UPDATE + " |": True; "|" on l. 11 76 -> 76 (pipe count unchanged); «UPDATE 2026-» 42 -> 42 plus 1
UPDATE head with the simulation year 2099; 23 -> 23 lines. Fill values used only for the simulation: <DATE> 2099-01-01, <HH:MM> 00:00,
<checker> 0000000. (10) THIS DRAFT'S SHA1: a file cannot state its own sha1. The sha1 of this file with the forty hex digits after the
next colon replaced by forty «0» characters is: f31e82e3ef0a012ae4df319f396ce1fb8979b667. The file's actual sha1 and line count are in
the hand-back to the Lead (and re-measurable with sha1sum).
