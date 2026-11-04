# Draft RESULTS R109 (Lead; first fill 2026-11-04T17:39:10Z by date -u (subagent); on P-IDEAL-SLOT line L-3, docs/new/P-IDEAL-SLOT-line-L3.txt, l-new b261c3f9, sha1 0c51ce6da0a655c31112515c78cb0b5d22690168) — to CHECKER C121
FIRST FILL. Read at the origin heads fetched at the start of the fill (git fetch, then git ls-remote, 2026-11-04T17:21:20Z: l-new
b261c3f9, l-red e9938403, referee 241a8c14, referee-2 a6713a1a, checker 7982d57a; origin trunk b3f38e9d; local trunk 6712a8d5 = the
merge (--no-ff, octopus) of the l-new, referee and referee-2 heads into b3f38e9d, not pushed (the checker head 7982d57a is already an
ancestor of b3f38e9d, so the merge has three lane parents); the Lead's own commit f88c067a (17:21:21Z, «Lead: sweep 17:03Z; L-NEW 51
parked; log», docs/NOW.md and docs/agents/LEAD-STATE.md only) now sits on top of it; neither the merge nor f88c067a changes RESULTS
(sha1 60529d0d1ba6ad22f8ebc14c12491f9ea22323fa), GAPS (1d2e8c1bd526f88a309b9d24d813746837433df1), DECISIONS, DECISIONS-INDEX, TARGET.md
or CLAUDE.md (git diff --quiet b3f38e9d f88c067a, exit 0 each), and RESULTS and GAPS were last changed by the R108 landing commit
b3f38e9d): the packet and L-1 (e46e98a4; the packet unchanged at the l-new head b261c3f9, by cmp and sha1), L-2 and fixes entry 1
(6eb389a6), L-3 and fixes entry 2 (b261c3f9); REFEREE successor 23's docs/referee/R-P-IDEAL-SLOT.md (report 2a09dcf8, §C 3b8a9c77, §C
addendum 1 241a8c14; lines 1-132 and 1-160 unchanged at each later commit, by diff); REFEREE-2 successor 27's
docs/referee-2/R2-P-IDEAL-SLOT.md (cdf8e962, unchanged at a6713a1a) and R2-P-IDEAL-SLOT-L2.md (a3c0ec24; addendum 1 a6713a1a; lines 1-40
unchanged, by diff); the referees' tools and logs (REFEREE scratch/slot_probe.py and xinew_logs/slot_probe.txt; REFEREE-2
R2-P-IDEAL-SLOT/slot_check.py, lift_split_orig.json, lift_split_ctrl.json, no committed log); notes/L-NEW.md at b261c3f9 (l. 10-28,
47-48); docs/new/N5-SLOT-box158.md at 5e558a34 (its only commit); P-IDEAL-SEG at 8291ecf7 (for the copy diff of §0-§2);
experiments/new/check.sh at 5e558a34, e46e98a4, 6eb389a6 and b261c3f9; the instance experiments/new/box158/lift_max_d4_L13.json
(5e558a34) and its source experiments/new/box156/ext/max_d4_L13.json (= L-RED's experiments/red/r197/lag/max_d4_L13.json at c711987b, by
sha1); DECISIONS L41, L43; RESULTS R104 (title l. 9864, the model definition only), R105 (title l. 10155; body item (b) l. 10216), R108
(l. 10812-11028), Erratum E-2 (l. 11043-11069); GAPS l. 11; docs/checker/C118.md, C119.md, C120.md (7982d57a); notes/CHECKER.md at
7982d57a.
Re-runs (scratch, git archive of b261c3f9's experiments/new and docs/new): the commands of check.sh blocks w106, w107, w108 and w109 /
pin109, 2026-11-04T17:23:18Z-17:23:43Z, rc 0, output byte-equal to the blocks' expected strings and four PASS lines ((10)); my own
simulator and my own LIFT built from packet §5's text on the three champions, 17:24Z, rc 0; my split of segcheck.py's counts by degree,
17:25Z, rc 0 ((10)).
TRUNK STATUS AT THIS FILL (by script, git merge-base --is-ancestor against local trunk 6712a8d5 and origin trunk b3f38e9d): b261c3f9,
241a8c14, a3c0ec24 and a6713a1a are ancestors of local trunk 6712a8d5 (exit 0 each) and NOT of origin trunk b3f38e9d (exit 1 each);
5e558a34, e46e98a4, 6eb389a6, 16297185, 2a09dcf8, 3b8a9c77, cdf8e962, 8291ecf7, 19e0742f, 9a746361, 7982d57a, c711987b and the Lead
commits e16c12c5, f71e80ea and b5675488 are on both. The Lead pushes trunk before landing. C113 E-2 lesson: the body names these commits
on their branches only and makes NO statement about trunk. C113 E-1 lesson: the title is L-3 verbatim with no insertion. C114 Add. 1 E-1
lesson: the GAPS UPDATE head carries «<DATE>», filled at landing. C115 E-1 lesson: the premise route is checked against what RESULTS
records (G-4). C116 G-1, C118 §4 and C120 §4: the UPDATE rule of R105 is applied unchanged, with R107's step for the unlabelled DEAD
clause ((9)). C116 G-2: a name clash is settled by one body sentence (G-6; Honest limits (ix)). C117 E-1 / E-2 lessons: no sentence of
the entry says more than the line signs, DATA is scoped exactly as measured, and the instance is fully specified (here: lift_max_d4_L13
inline, with its start, the states s_0 … s_13, full sha1 and its repository path and source). C118 E-1 lesson: no status sentence that
goes stale; the entry calls nothing «pending» (the only «PENDING» is the title fill «checker PENDING», replaced at landing); RESULTS
R108 and Erratum E-2 are cited as landed text. C118 §3 / Erratum E-2 lesson: every DEFINITION in the title line is diffed against the
packet's definitions (G-2). C118 §5 DE37 ruling: a lane conjecture killed inside a landed line gets no Dead-ends row (14). C120 §5 G-9
RULE: «From the next line on, though, the C118 G-8 advice («name the statements a DATA count covers») is a check item. A line that
leaves it out gets an E-item.» (G-9: L-3 leaves it out). C120 §3 note: «Note: a «…» that is not a quotation should be avoided in later
lines» (G-8: L-3's SEG1-2D text in «…» is the line's own wording). In the body (title + entry), L-3 is the current line; L-1 and L-2
appear only in the line history.
to check: FLAGS FIRST (G-1 to G-14; G-9 is a CANDIDATE E-ITEM under C120's rule, which the line as frozen cannot meet; no other item is
REQUIRED from my side; no referee raised any of them as REQUIRED), then the CLEAN items and (0)-(14).
- G-9, DATA: THE C120 G-9 RULE IS NOT MET BY L-3 (CANDIDATE E-ITEM; for the Lead and CHECKER; the line cannot be changed in this draft).
  L-3's only DATA parenthesis: «(DATA: experiments/new/box158/lift.py and three.py on three lifted champions;
  experiments/new/box157/segcheck.py, 0 violations on 59 corpus runs and on 34,934 random runs (every start for N ≤ 8, the genome start
  otherwise))». Neither count names the statements it covers: «three lifted champions» names two tools and no statement (lift.py tests
  LIFT; three.py prints the segment data, which tests nothing), and «0 violations on 59 corpus runs and on 34,934 random runs» names
  segcheck.py and no statement. What the counts cover (my reading of the tools, and my split (10)): lift.py checks LIFT («SAME True») on
  max_d4_L13, max_d5_L15 and dd_d5_F14; three.py gives «cuts []» and seg1 = T on the three lifted genomes (DATA for SANDWICH's
  lower-bound construction and for the DEAD instance); segcheck.py checks SEG on all 59 + 34,934 runs (maximal intervals only) but
  SEG-ONCE only on the runs of genomes of largest degree ≤ 2, 55 of the 59 corpus runs and 1,936 of the 34,934 random runs, and it also
  checks COUNT and PROD, which are R108's LEVEL-PRODUCT, a statement R109 does not contain; nothing in the line's DATA tests SHIFT,
  SEG-CAP or SANDWICH (the referees' probes do: Data). Every number equals the tools' output (my re-run (10); REFEREE l. 83-87;
  REFEREE-2 l. 75-77, l. 107 «Scope tail and DATA ✓ (lift.py / three.py on three lifted champions; segcheck 59 / 34,934 runs).»). So
  there is no false number, but by C120 §5 («A line that leaves it out gets an E-item.») L-3 qualifies. TIMING (for the ruling): L-3 was
  committed 15:28:30Z (b261c3f9) and matched by both referees at 15:56Z (241a8c14 15:56:51Z; a6713a1a 15:56:42Z), all before C120
  (report «15:58Z by date -u», commit 7982d57a 15:59:22Z); L-1 (e46e98a4, 12:45:25Z) came after C118's advice (C118 §5, «For later
  lines: name the statements a DATA count covers.»). Whether «From the next line on» reaches a line frozen before the ruling is
  CHECKER's to say. OPTIONS for the Lead: (A) route a line L-4 now that changes only the DATA parenthesis, e.g. «(DATA: LIFT:
  experiments/new/box158/lift.py, the same run one level up, on three lifted champions (three.py: no level-0 step, seg1 = T); SEG on
  every run and SEG-ONCE on the runs of degree ≤ 2: experiments/new/box157/segcheck.py, 0 violations on 59 corpus runs (55 of degree ≤
  2) and on 34,934 random runs (1,936 of degree ≤ 2; every start for N ≤ 8, the genome start otherwise))» (my wording, for the lane to
  write; one byte test at each referee), then a second fill of this draft; or (B) send this draft to C121 and let CHECKER rule. My
  recommendation: (A) before C121 (C120's wording leaves little room for (B), and an E-item after C121 costs the same round plus a
  second CHECKER pass). The body states the per-statement split (Data; Honest limits (v)) either way.
- G-1, TITLE SHAPE AND SOURCE NOTE (note; no Lead insertion). L-3 contains «2026» once, as « (2026-11-04) — », the only « — » (by
  script), and ends with the source parenthesis «(P-IDEAL-SLOT, docs/new/P-IDEAL-SLOT.md with its fixes entry 1,
  docs/new/P-IDEAL-SLOT-fixes.md; L-NEW successor 51)». The title is "### R109 [refereed-only] " + L-3 + the fill ", CHECKER PASS
  (docs/checker/C121.md, checker PENDING)" (as R90-R108), nothing inserted. The source note names fixes entry 1 and not entry 2, which
  holds the L-2 → L-3 change (REFEREE-2 R2-P-IDEAL-SLOT-L2.md l. 47 «Optional only: the provenance tail still names «fixes entry 1»;
  entry 2 holds this change.»; not taken). Both entries are in the one file the note names, so the reader reaches entry 2 from it; the
  body names both (Object, Fixes). Like R107's and R108's, L-3 has no «(the model first stated in L-RED R178 §1)» attribution («R178» 0
  times in L-3 and in the packet); R104 carries it.
- G-2, DEFINITIONS DIFFED AGAINST THE PACKET (the C118 §3 / Erratum E-2 lesson; my own diff, by reading and by script where literal):
  every definition and every defined object in L-3 against packet §0-§6. (i) «T the number of steps of a run from a given start» = §0 l.
  39 («T := the number of steps.», the run from s_0, l. 29). (ii) «𝓛_d the genomes with levels 0, …, d − 1, exactly two movers with two
  options on every level, any number of movers with one option and none with more than two» = §4 l. 113-114 («𝓛_d is the class of
  IDEAL-ACYC genomes with levels 0, …, d − 1 and exactly two degree-2 movers on every level; any number of degree-1 movers may be added
  at any level, and no mover has degree ≥ 3»); IDEAL-ACYC is the line's «on acyclic Ξ-graphs»; the packet's «For d ≥ 1» (l. 113) is not
  in the line's definition (G-3 (iii)). (iii) «T*(d) the largest T over 𝓛_d and all starts» = §4 l. 114-117 (the supremum, finite by
  induction from T*(1) ≤ 2); T is integer-valued and bounded, so the supremum is a maximum (REFEREE l. 97-98, «largest» = sup; REFEREE-2
  l. 48-49 «(So «largest» in the line is a maximum.)»). (iv) SEG: «on an interval of steps without a move at levels ≤ l (l ≥ −1)» = §1
  l. 48 (Mv_t contains no mover of level ≤ l for every t ∈ [a, b], l ≥ −1); «freezing the movers of level ≤ l at their options at the
  state before the interval's first step (s_(a−1))» = §1 l. 49-50 (H, every mover of level ≤ l keeps only the option s_(a−1)(x) with its
  W-target, Ξ-target, β and gate); «reproduces the interval» = §1 l. 51 (the run of H from s_(a−1) has s_(a−1), s_a, …, s_b as its first
  b − a + 2 states); the run's start s_(a−1) is not spelled out after «reproduces» (REFEREE-2 optional P-1, l. 122-123; REFEREE-2
  counted it met by SLOT-L3: R2-P-IDEAL-SLOT-L2.md l. 21 «SEG (my P-1 = SLOT-L3): «at the state before the interval's first step
  (s_(a−1))» = §1. ✓»). (v) SEG-ONCE: «at degree ≤ 2 every mover of level l + 1 moves at most once in it» = §2 l. 72-73 (its whole-run
  case l = −1 is not stated in L-3; narrower, not wider). (vi) SHIFT: «if every level-0 mover has one option» = §3 l. 86; «lowering
  every level ≥ 1 by one, the level-0 movers staying at level 0» = l. 88; «every option of a mover of old level 1 loses its W-target and
  gets the gate g(w, k_w) · Γ + g(x, k), with w its old W-target, k_w the only option of w» = l. 89-90; «Γ larger than every gate»
  against l. 86-87 «Let Γ be an integer larger than every gate index of G.»: the line drops «integer» (my reading, raised by neither
  referee: the proof's two gate facts, distinct new gates and the lexicographic order of the pairs, use only 0 ≤ g(x, k) < Γ with
  integer gates, so they hold for any real Γ above every gate; the only effect of a non-integer Γ is non-integer new gate indices, which
  enter the model only through their order; precision note, not wider in substance); «every other field and the start unchanged» = l.
  91; «gives a genome with the same run from every start» = l. 92 («from every start its run is G's run, state for state»). (vii)
  SEG-CAP: «for d ≥ 2, in every run of 𝓛_d» = l. 124; «the number of steps before the first step moving a level-0 mover» = seg1 (l. 118,
  120: a LEVEL-0 STEP is a step whose movers include a level-0 mover; seg1 = T if there is none); «the number strictly between the first
  and the last such step» = mid (l. 121; 0 if fewer than 2); «the number after the last one» = tail (l. 122; 0 if none); «are each at
  most T*(d − 1)» = l. 124. (viii) LIFT: «raising every level of a genome by one» = l. 138; «adding two level-0 movers A, B with two
  options each (Ξ-target X and no W-target, four new ranks above all others, all of even parity, with the larger of each mover on its
  option 0, four new gates above all others, start option 0)» = l. 139-141, 143; «every option of a mover of old level 0 getting
  W-target A» = l. 142; «gives a genome in which A and B never move and whose run on the old movers is the old run, state for state» =
  l. 144-145; the old movers' start (G's start, l. 143) is implicit in «the old run» (G-3 (v)). (ix) SANDWICH: «T*(d − 1) ≤ T*(d) ≤ 3
  T*(d − 1) + 2» = l. 156; «the largest number of steps before the first level-0 step over 𝓛_d equals T*(d − 1)» = l. 157 («The supremum
  of seg1 over all runs of 𝓛_d equals T*(d − 1).»; attained, since T*(d − 1) is attained and LIFT carries it to seg1: REFEREE-2 l. 104
  «maxima exist»); the packet's «(d ≥ 2)» (l. 155) is not repeated in the SANDWICH clause (G-3 (iii)). (x) DEAD: SEG1-2D's text in «…»
  against §6 l. 168 «in every run of every 2-wide degree-2 ladder with d ≥ 2 levels (no degree-1 movers), seg1 ≤ 2d − 1»: the line drops
  «d ≥ 2» (harmless: at d = 1 every step moves a level-0 mover, so seg1 = 0 ≤ 1: REFEREE l. 100, REFEREE-2 l. 105-106) and «(no degree-1
  movers)» (implied by «2-wide degree-2 ladder», §0 l. 43: «exactly two movers per level, all of degree 2»); «on every … ladder» covers
  every run of it; so killing the line's form kills the packet's and conversely. (xi) the instance clause: «the 5-level ladder
  lift_max_d4_L13» = l. 171, 173 («a 2-wide degree-2 ladder with d = 5 levels and no degree-1 movers»); «L-RED R197's max_d4_L13 lifted
  one level» = l. 171-172 (built by box158/lift.py, LIFT's construction; my own LIFT from §5's text equals the file field for field
  (10)); «T 13 from its stored start, no level-0 step, 13 > 9» = l. 174-175; «sha1 33fec48f…» = check.sh pin109 (the packet's l. 172
  «sha1 of the instance: see §7.»: G-11 (iv)). (xii) «and by SANDWICH any bound on that number over 𝓛_d in terms of d is a bound on T*(d
  − 1)» = §6 l. 176 («any bound seg1 ≤ f(d) on 𝓛_d implies T*(d − 1) ≤ f(d)»); «over 𝓛_d» is entry 2's insertion (REFEREE-2 SL-L2).
  (xiii) the scope tail: «the upper recursion gives 3^d − 1» = l. 163; «CONJECTURE SLOT-TRADE is not claimed» = l. 134, 187; «degree ≥ 3
  for SEG-ONCE / SEG-CAP / SANDWICH are not covered» = l. 82, 113-114 (𝓛_d has no mover of degree ≥ 3), 163-164. ALL EQUAL, with the
  precision notes (iv), (vi) and (ix). Both referees diffed every definition: REFEREE «## 6. Line L-1 (every DEFINITION diffed against
  the packet)» (l. 95) and «Definitions in L-2, diffed against the packet:» (l. 141), and on L-3 «No definition changes.» (l. 174);
  REFEREE-2 «## Line L-1: clause by clause, every definition against the packet» (l. 95), «Everything else in L-2 MATCHES (definitions
  𝓛_d, T*(d), T; SEG-CAP; SANDWICH; DEAD data; scope tail; DATA; provenance).» (R2-P-IDEAL-SLOT-L2.md l. 31) and the L-3 byte test (l.
  45-46).
- G-3, STRICT SYMBOL TEST (notes; the referees' clause passes are clean on L-3, (7)). (i) «a» in «(s_(a−1))» is not bound in L-3:
  s_(a−1) is named as «the state before the interval's first step», so a is that step (packet §1 l. 48); s_t, the state after step t
  (s_0 the start), is §0's notation, as in R105's and R108's lines. (ii) «l» is bound («(l ≥ −1)»); «w», «k_w» and «Γ» are bound inside
  SHIFT; «X» is §0's exit (l. 28) and R104's. (iii) «d»: 𝓛_d and T*(d) are defined for a free d; SEG-CAP binds «for d ≥ 2»; SANDWICH and
  the DEAD's «over 𝓛_d» use T*(d − 1), which needs d ≥ 2 (𝓛_0 would hold no mover, and N ≥ 1); the packet states SANDWICH for d ≥ 2 (l.
  155); a reader of the line must take d ≥ 2 there from T*(d − 1); neither referee raised it. (iv) «level-0 step» (SANDWICH, DEAD) =
  «step moving a level-0 mover» (SEG-CAP's words; packet l. 118); «that number» in the DEAD = the number of steps before the first
  level-0 step. (v) LIFT's «the old run» = the run of the original genome from its start; the line gives the new start only for A and B
  («start option 0»); packet l. 143 «the start is G's start with A and B at option 0». (vi) «the IDEAL model», «level», «mover»,
  «option», «W-target», «Ξ-target», «rank», «parity», «gate», «step», «run», «start», «state», «Ξ-graph» are R104's model words (RESULTS
  l. 9864) and packet §0 (l. 26-44). (vii) «2-wide degree-2 ladder» = packet §0 l. 43 («d-level 2-wide ladder»). (viii) «three lifted
  champions» are not named in the line (Data names them). None is a claim clause's quantifier left free except (iii), whose reading is
  fixed by the packet and by T*(d − 1)'s domain.
- G-4, PREMISE ROUTE (the C115 E-1 class): CLEAN (my check). L-3's premise parenthesis: «premise: R104's definition of the model only,
  no theorem of R104 used; and RESULTS R105's LOCAL, key half only» (the same words as R108's line). What RESULTS records (by script):
  R105's title (l. 10155) contains «a key only on the states below its level» once, and the phrase occurs twice in RESULTS (R105's
  title, l. 10155; R108's Premise, l. 10909); R105's body item (b) (l. 10216) has it in the form «(c) key_s(x, k) = key_(s′)(x, k)
  whenever s and s′ agree on every mover of level < lev(x).». Uses: only inside the copied SEG (iii) (packet l. 62-63) and SEG-ONCE (l.
  78-79), and through them in SEG-CAP: REFEREE l. 29-30 «SHIFT uses no R105 item (it compares keys directly). SEG-CAP uses SEG, SEG-ONCE
  and SHIFT. LIFT uses no R105 item. SANDWICH uses SEG-CAP and LIFT.»; REFEREE-2 l. 26-27 «Used only inside the copied SEG / SEG-ONCE.
  SHIFT and LIFT compute keys directly from §0's recursive key definition (no premise needed).». R104's definition: packet §0 l. 26-44
  is P-IDEAL-SEG §0 verbatim (my diff (2); REFEREE-2 l. 24 «R104: §0 is byte-identical to P-IDEAL-SEG §0»), which both referees checked
  against R104's text for P-IDEAL-SEG (RESULTS R108, Premise). P-IDEAL-SEG is NOT a premise: packet l. 22-23 «P-IDEAL-SEG is NOT a
  premise: its §0-§2 are copied below.»; REFEREE-2 l. 28 «P-IDEAL-SEG is not a premise (copied, so no landing dependency): correct. No
  R106 / R107, no docs/lit.»; REFEREE l. 26 «P-IDEAL-SEG is not a premise. No docs/lit, no R106 or R107.». So RESULTS R108, which
  carries the same SEG and SEG-ONCE (G-14), is not a premise either. Packet l. 18-23: «Premises (LANDED only).»; «RESULTS R104
  (P-N5-REALIZE): ONLY its definition of the IDEAL model and of the Ξ-graph, restated in §0. No theorem of R104 is used.»; «Not used:
  RESULTS R106, R107, docs/lit, docs/sources, any other lane file. No outside source is cited.». The DEAD instance is a data file built
  by the lane's lift.py from L-RED R197's max_d4_L13 (the instance of RESULTS R107's DEAD), recomputed by both referees with their own
  simulators; it is an instance, not a premise. No unlanded result, no lit note and no lane file is a premise.
- G-5, RESULTS ERRATUM E-2 TO R105 DOES NOT BEAR ON R109 (note; the C118 G-5 question, answered no, as for R108). Erratum E-2 (RESULTS
  l. 11043-11069) corrects R105's CHAINED binder (U), TOP-MONO's RANK_t and KEYFLIP's moves(x). R109 uses none: packet l. 20-21 «U,
  CHAIN-BACK and the CHAINED binder (R105 Erratum E-2) are not used.»; by script, packet §0-§7 (l. 26-192) contain 0 times each of «U»
  (as a word), «CHAIN», «chained», «RANK», «KEYFLIP», «moves(x)», «π», «h_t», «ENC», «XI-NEW», «MONO», «RISE» and «INTERVAL», «TOP» once
  (as «TOPO», a counter name of check.py, l. 185), and cite R105 only at l. 62 and l. 79 (LOCAL's key half); L-3 contains «CHAIN» 0,
  «KEYFLIP» 0 and «moves(x)» 0 times. LOCAL is not among E-2's three definitions. No landing condition from E-2; the entry cites E-2
  once, as landed text (Premise).
- G-6, NAMES, SAME LABELS, OTHER MEANINGS (by script on RESULTS 60529d0d / GAPS 1d2e8c1b; note; C116 G-2's remedy applied). 0 times in
  RESULTS and GAPS: «SEG-CAP», «SEG1-2D», «SLOT-TRADE», «lift_max_d4_L13», «LIFT» (as a word), «𝓛», «C121», «box 158», «box158»,
  «N5-SLOT», «lift.py», «three.py», «DE37». Same names, other meanings: (a) «SANDWICH» 14 times in RESULTS (R99's Lemma SANDWICH, «for
  sequences x, y, z of one length in lexicographic order», l. 8596, and its citations in R99 and R101) and twice on GAPS l. 11 (R99's
  UPDATE and a later premise list); R109's SANDWICH is the two-sided recursion for T*, unrelated. (b) «R109» 6 times in RESULTS (l.
  5185-5391, in R85 and R86), always as L-RED's box R109 («L-RED's R109 topfix family», docs/red/R109-hn-topgate.md); after landing,
  «RESULTS R109» and «L-RED's R109» name different things. (c) «SHIFT» as a word 12 times in RESULTS (R81-R92), each the quote-check
  control «SHIFT=1», and «GATE-SHIFT» 8 times (R74's lemma); R109's SHIFT is the level-lowering lemma. (d) «T*(» 16 times (R16, R54,
  R57, R64, R65, R68, R70: T*(n, m, Δ, d_e) and kin, bounds of other procedures); R109's T*(d) is defined in its line. (e) «Γ» 20 times
  in RESULTS (R59; R104's game Γ(G)) and once on GAPS l. 11 (R104's UPDATE); R109's Γ is SHIFT's gate base, bound in the line. (f)
  «P-IDEAL-SLOT» 3 times and «SEG, SEG-ONCE» 3 times in RESULTS, all in R108's body (the REFEREE FYI item in R-P-IDEAL-SLOT.md; R108's
  own labels). Applied (C116 G-2): one body sentence, Honest limits (ix). No line change.
- G-7, L41 (the C109 E-1 class): not triggered (my reading; neither referee mentions L41). L-3 contains «referee-originated» 0 and
  «lane-authored» 0 times. The proofs are L-NEW successor 51's (packet l. 5 «Labels: PROVED (L-NEW 51, unrefereed) / DEAD / DATA /
  READING (not to sign).»). POINTS TO CHECK: (a) the line changes L-1 → L-2 → L-3 answer the referees' line items SLOT-L1, SLOT-L2,
  SLOT-L3 (REFEREE) and SL-L1, SL-L2 (REFEREE-2); they restate packet §3 and §5's constructions and §6's scope in the line and change no
  statement (fixes l. 36 «Every statement in L-2 is a signed statement of the packet (§1-§6). No statement or DATA change.»; l. 40-41
  «Applied; nothing else changed.»). (b) REFEREE-2's control instance lift_split_ctrl.json is a referee's control showing why LIFT needs
  one common W-target; it is not a proof step. (c) The DEAD instance is built by the lane from L-RED's genome. Nothing
  referee-originated is a premise or a proof step (my reading).
- G-8, L43 (DEADs) and the C120 «…» note: CLEAN on L43 (my reading; please rule); NOTE on «…». L-3's DEAD: «the lane conjecture SEG1-2D
  («on every 2-wide degree-2 ladder with d levels, the number of steps before the first level-0 step is at most 2d − 1») is false, by
  the 5-level ladder lift_max_d4_L13 (L-RED R197's max_d4_L13 lifted one level; T 13 from its stored start, no level-0 step, 13 > 9;
  sha1 33fec48f…)». L43 (DECISIONS l. 369-374) bars a lane DEAD of an ASYMPTOTIC statement («one with an unspecified constant») and asks
  for «a refereed proof, or one instance exceeding an EXPLICIT bound». SEG1-2D has the explicit bound 2d − 1 and no constant; the
  instance exceeds it (13 > 9 at d = 5), and both referees recomputed it with their own simulators and SIGNED the DEAD (REFEREE l. 16,
  l. 61-65, l. 71; REFEREE-2 l. 19, l. 64-69). The asymptotic route behind it («bound the first segments linearly in d», Lead brief box
  158; docs/new/N5-SLOT-box158.md l. 20 «DEAD (route)») does NOT enter the line as DEAD: the line's last clause, «by SANDWICH any bound
  on that number over 𝓛_d in terms of d is a bound on T*(d − 1)», is an implication from a signed statement (REFEREE l. 64 «The kill is
  robust: by SANDWICH, ANY bound seg1 ≤ f(d) on 𝓛_d gives T*(d − 1) ≤ f(d).»), not a DEAD. THE KILLED STATEMENT: the packet's precise
  form (§6 l. 167-168), «the precise form of the route «bound the first segments linearly in d»» (REFEREE l. 62-63: the «2d − 1» form is
  the packet's own reading of the Lead's route; «The lane notes (N5-SLOT-box158.md) carry no separate statement.»). THE C120 NOTE:
  «Note: a «…» that is not a quotation should be avoided in later lines (REFEREE-2 optional P-3).» L-3's SEG1-2D text in «…» is not a
  quotation: it is the line's wording of §6's form (G-2 (x)), the same pattern as R108's REPLAY text; L-1 was frozen at 12:45:25Z and
  the C120 note came at 15:58Z. Note only (C120 says «should be avoided», not an E-item); if an L-4 is routed for G-9, the guillemets
  could go at no cost. «polynomial» 1 time in L-3 («bounds nothing polynomially»); «linear» 0, «O(» 0.
- G-10, LEAD READINGS AND RULINGS AS ON FILE (the C111 E-1 class): CLEAN. L-3 cites no Lead reading and no ruling (by script: «Lead
  reading» 0, «L4» 0, «D1» 0). The lane works under D14 / D18 (packet l. 2 «L-NEW successor 51 (Opus 5.5), D14 / D18;»). The freeze was
  a Lead GO (packet l. 2-3 «Lead 2026-11-04 12:46Z: «Freeze P-IDEAL-SLOT as a short packet with line L-1, same form as before»»), not a
  DECISIONS entry; Lead commit e16c12c5 (12:43:44Z) «Lead: R203 d4, P-IDEAL-SEG REFEREE sign, box 158; routes; log». Fix rounds: fixes
  l. 2 «Lead routing 2026-11-04 13:23Z» (Lead commit f71e80ea, 13:12:25Z, «Lead: P-IDEAL-SEG signed; P-IDEAL-SLOT to referees; L-NEW 51
  park; log»), fixes l. 39 «Lead routing 2026-11-04 15:28Z» (Lead commit b5675488, 15:56:21Z, «Lead: SLOT L-3; C120 routed; sweep
  15:03Z; log»).
- G-11, STALE LANE TEXT (notes; nothing here lands). (i) Packet l. 11 calls P-IDEAL-SEG §1-§2 «not yet landed»: true at the freeze
  (12:45:25Z), superseded when P-IDEAL-SEG landed as RESULTS R108 (b3f38e9d, 16:53:20Z); the entry states R108's landing as a fact and
  repeats no status (G-14). (ii) Fixes l. 3 «REFEREE-2 27 had not reported at this push»: REFEREE-2's report cdf8e962 (13:17:15Z)
  precedes the push of 6eb389a6 (13:27:06Z); the lane had not seen it (notes l. 18-19 say the same at park); its items reached the lane
  through the Lead (fixes l. 39); no verdict affected. (iii) Packet l. 2 «Lead 2026-11-04 12:46Z» is after the freeze commit e46e98a4
  (12:45:25Z); fixes l. 2 «13:23Z» is after f71e80ea (13:12:25Z) and before 6eb389a6 (13:27:06Z); fixes l. 39 «15:28Z» is the minute of
  b261c3f9 (15:28:30Z) and before the Lead commit b5675488 (15:56:21Z) that records it; stamps not verifiable from the repository. (iv)
  Packet l. 172 «sha1 of the instance: see §7.»: §7 (l. 184) says «sha1 pins of this packet, its line L-1 and the instance» and prints
  no digest; the digest 33fec48f1a8f1c57891b7574d87cc6bbe5e3bd38 is in check.sh pin109 (l. 897-898), in L-3 (abbreviated) and in both
  referees' reports (REFEREE l. 6, REFEREE-2 l. 8). (v) Packet §7 l. 182-183 lists three.py's output for two lifted genomes; block w108
  runs three.py on all three (lift_dd_d5_F14 «d 6 T 14 cuts [] seg1 14», as REFEREE l. 84 notes). (vi) Packet §6 l. 169-170 (largest
  genome-start seg1 per d on the corpus) is lane DATA, not to sign: REFEREE l. 65 «I did not re-run it, and it is not to sign.»;
  REFEREE-2 l. 70-71 reproduced it. (vii) REFEREE-2's N-1 (l. 55-56): packet l. 152 «under any state, the W-chain of an old option ends
  at (A, 0)» holds for states with s(A) = 0, which are all states of the run; the argument needs only a common first entry (precision,
  not a gap; nothing of it is in L-3). (viii) The lane notebook has no «Dead ends» entry for SEG1-2D; it records the route's kill at
  notes l. 12-13 and l. 47-48, and docs/new/N5-SLOT-box158.md l. 20-22 (5e558a34).
- G-12, SHA1 PINS IN check.sh (the C110 F-1 / C116 G-3 class): present. experiments/new/check.sh at 5e558a34 (895 lines) adds block w108
  (l. 888-894: lift.py on max_d4_L13, max_d5_L15 and dd_d5_F14 into a temp directory, three.py on the three outputs; three «SAME True»
  and two grep -qxF strings); e46e98a4 (903 lines) adds w109 / pin109 (l. 895-902: box150/check.py and three.py on the instance; pins of
  the packet, L-1 and the instance); 6eb389a6 (903 lines) extends pin109 by L-2 55e74726 and fixes 44bf76e7; b261c3f9 (903 lines, sha1
  00e1fde4dbeb82969a23e3966fd114629c018b44) replaces the fixes pin by cae85ce1 and adds L-3 0c51ce6d (l. 897-899 changed). The instance
  sha1 33fec48f1a8f1c57891b7574d87cc6bbe5e3bd38 is tested in pin109 (l. 898); w108 regenerates the lifted max_d4_L13 in its temp
  directory, and in my re-run that file is byte-equal to the committed instance (sha1 33fec48f…, (10)). SEG / SEG-ONCE's DATA is block
  w106 (l. 873-879, R108's). Re-run at this fill from the archive of b261c3f9: four PASS lines ((10)).
- G-13, THE REFEREES' ROUNDS (note). L-1 (17236fb1): both SIGN all seven statements with no gap (REFEREE 2a09dcf8; REFEREE-2 cdf8e962);
  REFEREE required SLOT-L1 (SHIFT «removing one level») and SLOT-L2 (LIFT construction), optional SLOT-L3 (SEG's frozen state) (l.
  104-118); REFEREE-2 required SL-L1 (LIFT construction) and SL-L2 (the DEAD's «over 𝓛_d»), optional P-1 to P-3 (l. 108-125). L-2
  (55e74726, fixes entry 1): REFEREE «VERDICT: line L-2 MATCHES. All 7 statements stay SIGNED.» (3b8a9c77, l. 153); REFEREE-2 «Verdict
  on L-2: NOT YET. One word change (SL-L2) gives L-3; with it, MATCHES.» (a3c0ec24, R2-P-IDEAL-SLOT-L2.md l. 33). L-3 (0c51ce6d, fixes
  entry 2): REFEREE «VERDICT: line L-3 MATCHES. All 7 statements stay SIGNED.» (241a8c14, l. 175); REFEREE-2 «Verdict: L-3 MATCHES. All
  my items on P-IDEAL-SLOT are closed.» (a6713a1a, R2-P-IDEAL-SLOT-L2.md l. 48). Taken: SLOT-L1 = P-2, SLOT-L2 = SL-L1, SLOT-L3 = P-1
  (REFEREE-2 l. 21 of the L2 file), SL-L2. Not taken (optional): P-3 («with d ≥ 2 levels» in SEG1-2D) and REFEREE-2's addendum remark on
  the source note (G-1).
- G-14, SEG AND SEG-ONCE ARE ALSO RESULTS R108 (a), (b) (note; new for this entry). Packet §1-§2 are P-IDEAL-SEG §1-§2 verbatim (my
  diff: packet l. 26-83 against P-IDEAL-SEG l. 25-82 at 8291ecf7 differ only in the two headings «(carried verbatim from P-IDEAL-SEG
  §1)» / «§2)» against «(PROVED)»; REFEREE l. 27-28 «The only differences are the two headings» … «The text is IDENTICAL, so my
  P-IDEAL-SEG signatures apply unchanged.»; REFEREE-2 l. 29-30 «byte-identical to P-IDEAL-SEG (8291ecf7) §1-§2. My signatures there
  carry over.»). P-IDEAL-SEG landed as RESULTS R108 (b3f38e9d, 16:53Z, CHECKER C120 7982d57a) after both referees had signed these
  copies; R108's Claims (a) and (b) (RESULTS l. 10852, l. 10861) are the same two statements, from the same text. L-3 restates them in
  its own words with the label «(SEG, SEG-ONCE; restated in full from P-IDEAL-SEG)», and they are in R109 as restatements, not as new
  results; R109 does not cite R108 (the packet copies text and proofs instead, l. 22-23). L-3's wording differs from R108's line (it
  binds l ≥ −1, names the frozen state s_(a−1), says «reproduces the interval», and omits the whole-run case of SEG-ONCE); both equal
  the packet (G-2 (iv), (v); RESULTS R108 by C120 §3). Remedy: one body sentence (Claims), no line change.
- CLEAN AT L-3 (the pre-check against CHECKER's recurring items, by script on 0c51ce6d):
  C106 E-1 (old line as current): L-3 is the current line; no L-4 exists (docs/new/P-IDEAL-SLOT-line-L4.txt absent at the l-new head
  b261c3f9); L-1 and L-2 appear only in the line history.
  C113 E-1 (title «verbatim» after an insertion): no insertion; the title is byte-equal to prefix + L-3 + fill (Addendum (2)).
  C113 E-2 (trunk status that goes stale): the body has no trunk statement (header).
  C114 Add. 1 E-1 (UPDATE date): <DATE> placeholder.
  C115 E-1 (a premise route RESULTS records as not established): G-4, G-5 (R104's definition and R105's LOCAL key half are landed text;
  Erratum E-2 does not bear; R108 is not a premise).
  C110 F-1 / C116 G-3 (pins): G-12 (pins present and PASS).
  C111 E-1 (stale Lead-reading statements): G-10.
  C116 G-2 (name clash): G-6, one body sentence.
  C117 E-1 (a sentence wider than signed; DATA scope): G-2, G-9; the body's DATA sentences carry the start regime, the N ranges and the
  degree split per statement; no gloss is unlabelled.
  C117 E-2 (instance under-specified): the body inlines lift_max_d4_L13 (the JSON fields, the start, the states s_0 … s_13) with its
  full sha1, its path and its source.
  C118 E-1 (stale status sentence): no «pending» in the entry; RESULTS R108 and Erratum E-2 are cited as landed text.
  C118 §3 / Erratum E-2 lesson (definitions diffed): G-2.
  C120 §5 G-9 (DATA count without its statements): NOT CLEAN, G-9.
  C120 §3 note («…» that is not a quotation): NOTE, G-8.
  «|»: 0 in L-3, 0 in the entry block, 0 in the UPDATE (by script, Addendum (3)).
(0) PLACEMENT. R109 goes DIRECTLY AFTER R108's block. docs/RESULTS.md at local trunk 6712a8d5 (= origin trunk b3f38e9d for this file)
has sha1 60529d0d1ba6ad22f8ebc14c12491f9ea22323fa, 11,608 lines, last changed by b3f38e9d (R108's landing). «### R108» is l. 10812
(entry l. 10812-11028, l. 11029 blank); «**Erratum E-1**» is l. 11030; «**Erratum E-2**» is l. 11043; «## Dead ends (kept;» is l. 11071;
DE36 begins at l. 11592 and runs to l. 11608, the last line of the file. PROPOSED (R102's to R108's layout): insert R109's entry after
l. 11029 (R108's blank line), with one blank line after it, so the R-entries stay contiguous and both errata follow them. The errata's
line references lie before the insertion and do not move. "### R109" occurs 0 times in RESULTS and GAPS; «R109» occurs 6 times in
RESULTS, as L-RED's box R109 (G-6 (b)). GAPS has sha1 1d2e8c1bd526f88a309b9d24d813746837433df1, 23 lines, last changed by b3f38e9d. The
Lead re-checks (6) and (9) at landing only if RESULTS or GAPS change after b3f38e9d. R108's own landing followed its draft's simulation
exactly (RESULTS l. 10812-11028 equal R108-draft l. 413-629 with «checker 7982d57a)» filled, by script).
(1) TITLE. The title is the line file docs/new/P-IDEAL-SLOT-line-L3.txt (l-new b261c3f97c1f8a5716fd16ef43e3bc5fad2400db,
2026-11-04T15:28:30Z, the file's only commit, sha1 0c51ce6da0a655c31112515c78cb0b5d22690168; it is the l-new head), verbatim: one line,
no outer quotes, no final period, 3,081 characters (3,150 bytes plus the newline), 572 whitespace tokens, 27 / 27 parentheses (depth
never negative), two «…» (L-3's own, in «levels 0, …, d − 1» and «sha1 33fec48f…») and one guillemet pair (SEG1-2D's text). NO HEADING
MARKER, verified by script: the file begins «In the IDEAL model of RESULTS R104», with no «#» at its start, no "R??" and no lane tag.
NOTHING is stripped and NOTHING is inserted: the heading is the level-3 marker, then "R109 [refereed-only] ", then the file without its
newline, then the fill ", CHECKER PASS (docs/checker/C121.md, checker PENDING)" (as R90-R108, no space before the comma). C121 is the
next CHECKER file: docs/checker/ ends at C120.md on the checker head 7982d57a and on trunk (no C121.md on any fetched head, by git
ls-tree); notes/CHECKER.md at 7982d57a l. 6 reserves it: «C121 = R109 (P-IDEAL-SLOT) when routed.». L-3 holds one « — », its own date
parenthesis «(2026-11-04)» and no "|" (G-1). Built by script (scratch fill109.py: assert the sha1 0c51ce6d…, equality with the blob at
b261c3f9 and at the l-new head, one line, no marker, one « (2026-11-04) — », no "|"; prepend, append) and re-checked after writing this
file: equal, byte for byte. Heading: 3,160 characters, 3,229 bytes; sha1 of the heading line without its newline 4c8ce2da780b1648053ee5be25d3f922d083f6bc; it
is l. 466 and the only «### R» line of this file.
(2) LINE HISTORY: three lines. L-1 17236fb18d70c1e2968689108a74a1acac938bd5 (e46e98a4, frozen with the packet; 2,586 bytes, 461 tokens):
both referees required changes (G-13). L-2 55e74726f0c7e6c6e27f780b779788014cc97e29 (6eb389a6; 3,138 bytes, 570 tokens): fixes entry 1
lists 21 word-diff items (fixes l. 15-35); my own token diff L-1 → L-2 (difflib on whitespace tokens, scratch wdiff109.py) finds 21
non-equal hunks, the same 21, in the same order (REFEREE l. 140 «finds 21 hunks, equal to entry 1's 21 items. Nothing else differs.»;
REFEREE-2 R2-P-IDEAL-SLOT-L2.md l. 8-9). L-3 0c51ce6da0a655c31112515c78cb0b5d22690168 (b261c3f9; 3,150 bytes, 572 tokens): my diff L-2 →
L-3 finds one hunk, the insertion «over 𝓛_d», and L-2 with its single «any bound on that number in terms of d» replaced by «any bound on
that number over 𝓛_d in terms of d» equals L-3 byte for byte (True) (fixes l. 43; REFEREE l. 168; REFEREE-2 R2-P-IDEAL-SLOT-L2.md l.
45-46). No fixes entry changes a statement or a DATA count (fixes l. 36, l. 40-41). So the title is L-3, and L-1 / L-2 are history.
(3) THE LINE AT BOTH REFEREES. REFEREE successor 23, docs/referee/R-P-IDEAL-SLOT.md: report 2a09dcf8 (2026-11-04T13:15:02Z, new file,
132 lines, sha1 78e664c8a7eb05b5482a4dcb2a27421ec602c11e), §C 3b8a9c77 (13:50:44Z, 160 lines, sha1
6d6f3b5ad20245e4de765e634a106f4c8b1f281c), §C addendum 1 241a8c14 (15:56:51Z, 175 lines, sha1 b0cc2d7c5ce0e326a01ce0a510cca1cfec4e480e):
l. 175 «VERDICT: line L-3 MATCHES. All 7 statements stay SIGNED.». REFEREE-2 successor 27: docs/referee-2/R2-P-IDEAL-SLOT.md (cdf8e962,
13:17:15Z, new file, 129 lines, sha1 9a4d2d6018d5211bcaa55735c154951175b4e01d; unchanged at a6713a1a) and
docs/referee-2/R2-P-IDEAL-SLOT-L2.md (a3c0ec24, 14:38:07Z, new file, 40 lines, sha1 4b5bcde91cd8d63b7005bd0cd276f16e1bf44858; addendum 1
a6713a1a, 15:56:42Z, 48 lines, sha1 99573975e3d42024941da402dbccc03bba0a466f): l. 46 «SL-L2 MET.», l. 48 «Verdict: L-3 MATCHES. All my
items on P-IDEAL-SLOT are closed.». Both MATCH L-3.
(4) CLAIMS SIGNED = the seven statements below, each SIGN in BOTH referees' verdict tables (REFEREE "## 0. Verdicts" l. 8-18 of
R-P-IDEAL-SLOT.md; REFEREE-2 "## Verdicts" l. 11-21 of R2-P-IDEAL-SLOT.md), checked clause by clause against the packet, and «stay
SIGNED» through L-2 and L-3 (REFEREE l. 153, 175; REFEREE-2 L2 file l. 48); the cells are the reports' words:
| item (packet §, lines) | REFEREE (successor 23) | REFEREE-2 (successor 27) |
| --- | --- | --- |
| (a) Lemma SEG, copy (§1, l. 46-69; any degree) | l. 11 «SIGN: verbatim copies of P-IDEAL-SEG §0-§2, which I signed in R-P-IDEAL-SEG.md (19e0742f)» | l. 14 «**SIGN** (Opus 5.5, D12): byte-identical to P-IDEAL-SEG 8291ecf7 §1-§2 (signed in R2-P-IDEAL-SEG.md)» |
| (b) Lemma SEG-ONCE, copy (§2, l. 71-83; degree ≤ 2) | l. 11 (the same row) | l. 14 (the same row) |
| (c) Lemma SHIFT (§3, l. 85-110; any degree) | l. 12 «SIGN»; §2 l. 33-42 | l. 15 «**SIGN** (Opus 5.5, D12)»; l. 33-41 |
| (d) Corollary SEG-CAP with the finiteness of T* (§4, l. 112-134; 𝓛_d, d ≥ 2) | l. 13 «SIGN»; §2 l. 43-49 | l. 16 «**SIGN** (Opus 5.5, D12)»; l. 42-49 |
| (e) Lemma LIFT (§5, l. 137-154; any degree) | l. 14 «SIGN»; §2 l. 50-55 | l. 17 «**SIGN** (Opus 5.5, D12) (precision N-1)»; l. 50-58 |
| (f) Corollary SANDWICH (§5, l. 155-164; d ≥ 2) | l. 15 «SIGN»; §2 l. 56-60 | l. 18 «**SIGN** (Opus 5.5, D12)»; l. 59-62 |
| (g) DEAD SEG1-2D by lift_max_d4_L13 (§6, l. 166-178) | l. 16 «SIGN (recomputed independently, and the lift rebuilt by me from LIFT's text)»; §2 l. 61-65, §3 l. 68-74 | l. 19 «**SIGN** (Opus 5.5, D12): recomputed with my own simulator»; l. 63-72 |
Both, verbatim: REFEREE l. 128 «All 7 items SIGN, no proof gap.»; REFEREE-2 l. 128-129 «All seven items (SEG, SEG-ONCE, SHIFT, SEG-CAP,
LIFT, SANDWICH, DEAD SEG1-2D): SIGN (Opus 5.5, D12), REFEREE-2 successor 27, 2026-11-04 13:16Z (date -u). Gaps: none.».
Clause checks (L-3 against the packet; G-2): the setting = §0 l. 26-44 and §4 l. 113-117; SEG / SEG-ONCE = l. 48-51, 72-73; SHIFT = l.
86-92; SEG-CAP = l. 118-124; LIFT = l. 137-145; SANDWICH = l. 155-157; DEAD = l. 167-177. Nothing in L-3 is wider than signed (G-2 (vi)
is a precision note; REFEREE §C l. 152 and add. 1 l. 174; REFEREE-2 L2 file l. 31, l. 45-46).
Signed by both, NOT stated by L-3 as separate items: SEG's count «(so H takes at least b − a + 1 steps)» (l. 51) and SEG-ONCE's
whole-run case (l. 73) (both in RESULTS R108 (a), (b)); SEG-CAP's decomposition «So T = seg1 + mid + tail + (number of level-0 steps).»
(l. 123) and «there are at most 2 level-0 steps» (l. 119); T*(1) ≤ 2 (l. 115); LIFT's «in particular T(G^) = T(G)» (l. 144-145); §6's
remark that a linear seg1 bound is a linear bound on T* (l. 176-177, in the line as the SANDWICH implication). Not signed, so NOT
landed: packet §7 (machine checks, EXCLUDED, TARGET diff, READING; «DATA / READING (not to sign)», l. 16); §6's corpus table (l.
169-170, lane DATA); the fixes entries as text (they change the line only).
(5) OTHER TEXTS THE ENTRY DEPENDS ON: RESULTS R104's definition of the IDEAL model (title l. 9864; no R104 theorem); RESULTS R105's
LOCAL, key half (title l. 10155; body item (b) (c), l. 10216). Nothing else. RESULTS R108 carries the same SEG and SEG-ONCE and is not a
premise (G-14). The lane source docs/new/N5-SLOT-box158.md (packet l. 4 «Source: docs/new/N5-SLOT-box158.md §1 (box 158). This packet
governs») is history only; the DEAD instance is a data file ((10), G-2 (xi)); no lane file and no lit note is a premise (G-4).
(6) PREMISE LABELS (stale-label test; RESULTS at b3f38e9d's version, GAPS likewise). RESULTS labels in L-3 (by script): «R104» 3
(«RESULTS R104», «R104's definition», «theorem of R104»); «R105» 1 («RESULTS R105's LOCAL, key half only»); «R197» 1, an L-RED box
label, prefixed («L-RED R197's max_d4_L13»). R104 (l. 9864) exists and carries the definition. R105 (l. 10155) exists and carries LOCAL;
Erratum E-2 (l. 11043) governs the reading of three other R105 definitions and retires no label (G-5). «P-IDEAL-SEG» 1 (the copy label;
the packet of RESULTS R108, not cited as a premise). No Lead reading and no other RESULTS label is cited. G-N5-TIME open (GAPS l. 11).
(7) SYMBOL TEST of the title (my own strict test of every symbol of L-3; IN = bound in the line; else the carrier):
| symbol | where |
| --- | --- |
| IDEAL model, Ξ-graph, acyclic, mover, level, option, W-target, Ξ-target, X, rank, parity, gate, step, run, start, state | RESULTS R104 (the premise; packet §0) |
| LOCAL, key half | RESULTS R105 (the premise; G-4) |
| T, 𝓛_d, T*(d), l, Γ, w, k_w, A, B | IN |
| d | free in 𝓛_d and T*(d); «for d ≥ 2» in SEG-CAP; d ≥ 2 implicit in SANDWICH and the DEAD (G-3 (iii)) |
| s_(a−1), a | named as «the state before the interval's first step» (G-3 (i)) |
| level-0 step, that number | SEG-CAP's «step moving a level-0 mover»; the number of steps before the first one (G-3 (iv)) |
| the old run (LIFT) | the original genome's run from its start (G-3 (v)) |
| 2-wide degree-2 ladder; 5-level ladder | packet §0 l. 43; §6 l. 173 |
| SEG1-2D's text in «…» | the line's wording of §6 l. 168 (G-8) |
| lift_max_d4_L13, its stored start, sha1 33fec48f… | data objects (G-2 (xi); body Claims (g)) |
| L-RED R197 | attribution, prefixed |
| CONJECTURE SLOT-TRADE | named as not claimed (packet l. 134, 187) |
| DATA clause: lift.py, three.py, three lifted champions; segcheck.py, 59 / 34,934 runs | DATA, cited; statements not named (G-9) |
Agreeing tests: REFEREE §6 l. 95-118, §C l. 141-152, add. 1 l. 168-174; REFEREE-2 l. 95-107, L2 file l. 11-31, l. 42-48.
(8) FIXES AND STATUS NOTES (docs/new/P-IDEAL-SLOT-fixes.md, L-NEW successor 51, append-only, two entries, two commits): at b261c3f9 sha1
cae85ce1937948648fc2a24bb4ea7db639d96123, 43 lines; at 6eb389a6 (entry 1 only) sha1 44bf76e7bea59037ffe86ef434ae84c15891e2c4, 36 lines;
the first 36 lines at b261c3f9 have the sha1 44bf76e7… (by script; REFEREE l. 165-166). Header (l. 1-3): «(append-only; the packet
docs/new/P-IDEAL-SLOT.md and line L-1 stay frozen)», the routing of 13:23Z (G-11 (ii), (iii)). Entry 1 (l. 5-36): line L-2; «Applied:»
SLOT-L1 (SHIFT construction, l. 7-8), SLOT-L2 (LIFT construction, l. 9-11), SLOT-L3 (SEG's frozen state, l. 12), the provenance tail (l.
13); the 21-item word diff (l. 14-35); «No «|» in L-2. Every statement in L-2 is a signed statement of the packet (§1-§6). No statement
or DATA change.» (l. 36). Entry 2 (l. 38-43): line L-3; the routing of 15:28Z and REFEREE-2's SL-L2 (l. 39-41); «Applied; nothing else
changed.» (l. 40-41); the one-item word diff (l. 43). The packet file itself is unchanged since e46e98a4 (sha1 62901b5f… at e46e98a4 and
at b261c3f9).
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-3 states no CONJECTURE as claimed and kills nothing of RESULTS or GAPS (SEG1-2D and
SLOT-TRADE occur 0 times there). A line-11 UPDATE is proposed at the end, to go AFTER R108's UPDATE (GAPS at b3f38e9d: the last UPDATE
on l. 11 is R108's «UPDATE 2026-11-04 16:53Z: RESULTS R108 (P-IDEAL-SEG; CHECKER C120 7982d57a) [refereed-only] LANDED: …», ending
«G-N5-TIME stays open.» before the row's closing « |»; l. 11 holds 76 "|" and 43 «UPDATE 2026-»), as a pure insertion with one
separating space. BUILT FROM L-3 (scratch upd109.py: upd108.py's controls and procedure unchanged, upd100L3.py's build() unchanged).
CONTROLS (same script, same run, rc 0): R97's to R108's LANDED UPDATEs (GAPS l. 11 at b3f38e9d) rebuilt from their lines byte for byte
(True ×12; R108's from P-IDEAL-SEG L-1 at 8291ecf7 with head «UPDATE 2026-11-04 16:53Z: RESULTS R108 (P-IDEAL-SEG; CHECKER C120
7982d57a) [refereed-only] », 2,078 bytes, also equal to R108-draft l. 640 with <DATE> 2026-11-04, <HH:MM> 16:53, <checker> 7982d57a).
R109: R108's procedure unchanged (C118 §4: «Ruling: PASS. The rule is R105's / R106's, plus «a clause that carries its own lead-in stays
as it is».»; C120 §4 «This is the R107 rule unchanged.»): L-3's claim body ends with the unlabelled clause «; and DEAD: the lane
conjecture SEG1-2D … is a bound on T*(d − 1)» after the last labelled clause (SANDWICH); the procedure runs on L-3 with that clause cut
out (build()'s label move on the claim body plus a sentinel tail, start «and all starts: », 5 labels, each found once after it, in
order; « (2026-11-04) — » → «: »; the DATA parenthesis before the source parenthesis opened as «; DATA: …»; «; G-N5-TIME stays OPEN» and
«; not M3, not a step-4 pass, not a TARGET.md claim» dropped; the source parenthesis kept; «. G-N5-TIME stays open.» appended), and the
clause is put back verbatim between the moved «(SANDWICH)» and the tail's «: » (one occurrence, by script). One feature new to this
line: the first label, «(SEG, SEG-ONCE; restated in full from P-IDEAL-SEG)», contains «; ». build() finds each label as a whole string
and cuts each clause at the last «; » before the NEXT label, so the label moves as one unit behind its clause («… moves at most once in
it (SEG, SEG-ONCE; restated in full from P-IDEAL-SEG); at any degree, …»), and the SHIFT clause's inner «; every other field and the
start unchanged» stays inside its parenthesis (by script: each label once, behind its clause). The DEAD clause carries no label, so
nothing in it moves; its guillemet text stays. L-3 holds no "|", so no replacement list. Checked by script: one line, 0 "|", one
«<DATE>», one «<HH:MM>», one «<checker>», 3,184 bytes, 571 tokens; «2026-11-04» 0 times (the date parenthesis is dropped by the rule);
token multiset diff against L-3 = the head, the five moved labels, «(DATA:» opened, the two dropped scope sentences, « — » and the final
sentence (upd109.out). Head «UPDATE <DATE> <HH:MM>Z: RESULTS R109 (P-IDEAL-SLOT; CHECKER C121 <checker>) [refereed-only] »
(«P-IDEAL-SLOT» 0 times in GAPS); <DATE> = the landing date. The UPDATE inherits L-3's DATA wording, so G-9 applies to it as well; an
L-4 would be rebuilt by the same script.
(10) DATA of record = packet §7 (l. 180-192), NOT signed; L-3's DATA parenthesis states its counts. Re-run at this fill (scratch, git
archive of b261c3f9's experiments/new and docs/new; between e46e98a4 and b261c3f9 the files these blocks read are unchanged except
check.sh's pins (box158, box157, box150, box156/ext, box152, box14*, box139: git diff --stat lists only check.sh, box156/log and box159
under experiments/new); from experiments/new, as check.sh's «cd»), 2026-11-04T17:23:18Z-17:23:43Z, rc 0, outputs blocks.out, w108.out,
w109.out, pin109.out and w106.out:
- The blocks as written (check.sh l. 873-903 at b261c3f9, in a shell with its «set -euo pipefail» and «cd»), four PASS lines: «box 157
  SEG / SEG-ONCE / LEVEL-PRODUCT: 0 violations (59 + 34,934 runs; BADLEV=2 control fires): PASS», «P-IDEAL-SEG: REPLAY DEAD data on
  max_d5_L15 (segment t9-15 all new); pins packet 7fa84784, line L-1 a18f6f0c, fixes 2e3dd532: PASS», «box 158 LIFT: max_d4_L13 /
  max_d5_L15 / dd_d5_F14 lift one level up with the same run and seg1 = T: PASS», «P-IDEAL-SLOT: instance lift_max_d4_L13 (d 5, T 13,
  seg1 13, 0 violations); pins packet 62901b5f, line L-1 17236fb1, instance 33fec48f, line L-2 55e74726, fixes cae85ce1, line L-3
  0c51ce6d: PASS».
- w108 raw: «LIFT max_d4_L13.json T 13 -> T^ 13 levels 4 -> 5 SAME True», «LIFT max_d5_L15.json T 15 -> T^ 15 levels 5 -> 6 SAME True»,
  «LIFT dd_d5_F14.json T 14 -> T^ 14 levels 5 -> 6 SAME True», «lift_dd_d5_F14.json d 6 T 14 cuts [] seg1 14», «lift_max_d4_L13.json d 5
  T 13 cuts [] seg1 13», «lift_max_d5_L15.json d 6 T 15 cuts [] seg1 15»; the temp lifted files have sha1 33fec48f… (max_d4_L13),
  d15d1ca0… (max_d5_L15) and 89d7a3f1… (dd_d5_F14), each equal to the committed box158/lift_*.json.
- w109 raw: «TOTAL genomes 1 runs 1 steps 13 XSIM 0 TOPO 0 MONO 0 XINEW 0 RISE 0 CHAIN 0 KEYFLIP 0 DECR 0 TOPMONO 0 RBOUND 0 RESTR 0
  ICHARGE 0 REC 0 VIOL 0 (info REC148 0)», «lift_max_d4_L13.json d 5 T 13 cuts [] seg1 13». pin109: packet 62901b5f…, L-1 17236fb1…,
  instance 33fec48f…, L-2 55e74726…, fixes cae85ce1…, L-3 0c51ce6d… (full digests in pin109.out).
- w106 raw (SEG / SEG-ONCE data, R108's block): «SEGCHECK runs 59 steps 650 intervals 652 SEG 0 ONCE 0 COUNT 0 PROD 0 maxratio 0.3333»,
  «SEGCHECK runs 34934 steps 38676 intervals 57755 SEG 0 ONCE 0 COUNT 0 PROD 0 maxratio 1.0».
- My own simulator and my own LIFT (scratch mysim109.py, written from RESULTS R104's text and packet §0 / §5, β-SETS compared by the
  largest-rank β of the symmetric difference, keys under the new state level by level; no lane code imported), 17:24Z, rc 0, output
  mysim109.out: on max_d4_L13, max_d5_L15 and dd_d5_F14: each valid (acyclic, ranks and gates distinct, W one level down), T 13, 15, 14;
  my LIFT of each valid, the same T, the same old-mover states state for state, A and B fixed, a 2-wide degree-2 ladder with d = 5, 6,
  6. My LIFT of max_d4_L13 EQUALS the committed lift_max_d4_L13.json in every field N, lev, opts, gate, br, bp, start (True). On the
  committed instance: levels [1, 1, 2, 2, 3, 3, 4, 4, 0, 0], T 13, no level-0 step, seg1 13 > 9 = 2·5 − 1, old-mover states =
  max_d4_L13's run, A and B fixed; states and movers per step as in Claims (g).
- My split of segcheck.py's counts by degree (scratch split.py on the archive, 17:25:19Z-17:25:21Z, rc 0, split.out; the same numbers as
  R108's split at 6eb389a6): corpus 59 = 55 runs of degree ≤ 2 (N = 4..24; 483 steps, 499 intervals) + 4 of degree 3 (N = 9..24; 167
  steps, 153 intervals); random 34,934 = 1,936 runs of the 93 genomes of largest degree ≤ 2 (N = 1..10; 1,611 steps, 2,891 intervals) +
  32,998 runs of the 107 genomes of largest degree 3 or 4 (N = 1..9; 37,065 steps, 54,864 intervals). segcheck.py checks ONCE, COUNT and
  PROD only «if D <= 2».
- Word diffs and line metrics: scratch wdiff109.py / wdiff109.out ((2)).
NOT re-run: the referees' tools (docs/referee/scratch/slot_probe.py, xinew_probe.py; docs/referee-2/R2-P-IDEAL-SLOT/slot_check.py); I
read REFEREE's committed log (xinew_logs/slot_probe.txt at 2a09dcf8, unchanged at 241a8c14: seeds 1, 2 «'shift_bad': 0» and «'lift_bad':
0» with shift runs 2,647 + 2,643 and lift runs 3,000 + 3,000; seed 3 mut 1 «'shift_bad': 1007»), which equals REFEREE §3 l. 76-80;
REFEREE-2 committed no log for slot_check.py. The lane's §6 corpus table (l. 169-170): not re-run. check.sh's other blocks and
scripts/verify.sh: not run.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 packet l. 11 «not yet landed» (true at the freeze; R108 landed at
16:53Z; G-11 (i)). D-2 fixes l. 3 «REFEREE-2 27 had not reported at this push» against cdf8e962 (13:17:15Z) before 6eb389a6 (13:27:06Z)
(G-11 (ii)). D-3 the Lead stamps 12:46Z (packet l. 2), 13:23Z and 15:28Z (fixes l. 2, 39) against the commits e46e98a4 (12:45:25Z),
6eb389a6 (13:27:06Z), b261c3f9 (15:28:30Z) and the Lead commits e16c12c5, f71e80ea, b5675488 (G-11 (iii)). D-4 packet l. 172 points to
§7 for the instance sha1, which §7 does not print (G-11 (iv)). D-5 packet §7 l. 182-183 names three.py's output for two of the three
lifted files (G-11 (v)). D-6 packet l. 152 «under any state … ends at (A, 0)» (REFEREE-2 N-1; G-11 (vii)). D-7 REFEREE-2 l. 2-3
«Independent: docs/referee/ not read for this packet before this push.» with its push at 13:17:15Z, 2 min after REFEREE's report commit
13:15:02Z (independence as stated; REFEREE l. 2 «Independent: I did not read docs/referee-2/.»). D-8 REFEREE §C l. 137 gives the fixes
file at 6eb389a6 as «sha1 44bf76e7…, 36 lines» and add. 1 l. 165 «cae85ce1…, 43 lines»: both equal my measurement. D-9 L-3's «Γ larger
than every gate» against the packet's «integer» (G-2 (vi)). No discrepancy between a report and the lane files beyond these.
(12) Excluded: packet §7 (machine checks, EXCLUDED, TARGET diff, READING); CONJECTURE SLOT-TRADE (l. 134, 187; lane:
docs/new/N5-SLOT-box158.md l. 27 and box 159, docs/new/N5-TRADE-box159.md, not read for this entry beyond its existence); the segment
table and every READING of docs/new/N5-SLOT-box158.md (l. 187); §6's corpus table; the READING «SANDWICH pins the ladder growth question
to one trade-off» (l. 191-192); the referees' own probes and counts (DATA about the statements, not part of this entry beyond the Data
bullet); REFEREE-2's control instances (lift_split_*.json); fixes entries 1 and 2 as statements. Not part of this entry.
(13) Commits: lane (claude/l-new): 5e558a34 (2026-11-04T12:18:07Z; box 158 source docs/new/N5-SLOT-box158.md, box158/lift.py, three.py,
the three lifted files, check.sh block w108) → e46e98a4 (12:45:25Z; freeze: packet +192, L-1 +1, check.sh +8, block w109 / pin109) →
6eb389a6 (13:27:06Z; L-2 +1, fixes entry 1 +36, pin109 extended; also P-IDEAL-SEG fixes entry 1, not this entry's) → 16297185
(13:48:03Z; box 156 park notes; no P-IDEAL-SLOT file) → b261c3f9 (15:28:30Z; L-3 +1, fixes entry 2 +7, pin109 updated). The instance's
source: L-RED's experiments/red/r197/lag/max_d4_L13.json (claude/l-red c711987b, 2026-11-03T00:54:10Z), byte-equal to
experiments/new/box156/ext/max_d4_L13.json (l-new 6e24a889; sha1 f0735b61… each). REFEREE (claude/referee): 2a09dcf8 (13:15:02Z; report,
new file 132 lines, sha1 78e664c8…; scratch/slot_probe.py sha1 6670f55b737f187f567c9e7236abec7677ebc730, 34 lines;
xinew_logs/slot_probe.txt sha1 87ed1717212d914b8e5aa2620f13f71f7b76e322, 3 lines; it reuses scratch/xinew_probe.py, a4e7b4a9, sha1
592b304e0e377e6f7272dcc42879696a5c6eabee) → 3b8a9c77 (13:50:44Z; §C on L-2, +28 lines) → 241a8c14 (15:56:51Z; §C addendum 1 on L-3, +15
lines). REFEREE-2 (claude/referee-2): cdf8e962 (13:17:15Z; report, new file 129 lines, sha1 9a4d2d60…; R2-P-IDEAL-SLOT/slot_check.py,
154 lines, sha1 57cabd72f4c5f9cf49473346635f5c0ef9152cba; lift_split_orig.json sha1 14d8510e8917bbc7561ff46fb961d4e59426462d;
lift_split_ctrl.json sha1 3ab62fd896fdf58f95d4f65a764024f666bca085) → a3c0ec24 (14:38:07Z; L-2 file, new, 40 lines) → a6713a1a
(15:56:42Z; addendum 1, +8 lines). CHECKER: none yet for R109 (C121). Lead: e16c12c5 (GO), f71e80ea (fix round 1), b5675488 (L-3 round).
Trunk: see the header.
(14) Placement: see (0). DEAD-ENDS ROW: NONE (not drafted). R109 kills a lane conjecture (SEG1-2D) by an explicit refereed instance
inside its line. CHECKER C118 §5 confirmed «no row» for the same class (R107's LIN-156): «DE37: the Lead's «no row» is CONFIRMED.», with
the precedent «the lane statements killed inside landed lines, REP-LIN (R90), BIP-REL-1 (R95), frz32 (R100), fbg_K12 (R101)» «and odxi
(R103)» and «DE34-DE36 are candidate algorithms and a proof route, a different class.»; C120 §5 applied it to R108's REPLAY («Dead-ends
row: none, per C118 §5 (agreed by the Lead).»). SEG1-2D occurs 0 times in RESULTS and GAPS, so no fleet conjecture or route depends on
it; R109's line records the instance and its numbers, and the body inlines the instance (Claims (g)), so CLAUDE.md's «Record every dead
end with the exact obstruction and the instance that killed it.» is met inside RESULTS. The asymptotic route «bound the first segments
linearly in d» is not declared DEAD in the line (G-8); it is a lane route (docs/new/N5-SLOT-box158.md l. 20), not a fleet route in
RESULTS or GAPS, so it gets no row either (my reading; DE36's «route «bound LP»» was a refereed-proof route of the fleet, a different
class). The next free Dead-ends number stays DE37 («DE37» 0 times in RESULTS).
### R109 [refereed-only] In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of R104 used; and RESULTS R105's LOCAL, key half only), on acyclic Ξ-graphs, with T the number of steps of a run from a given start, 𝓛_d the genomes with levels 0, …, d − 1, exactly two movers with two options on every level, any number of movers with one option and none with more than two, and T*(d) the largest T over 𝓛_d and all starts: (SEG, SEG-ONCE; restated in full from P-IDEAL-SEG) on an interval of steps without a move at levels ≤ l (l ≥ −1), freezing the movers of level ≤ l at their options at the state before the interval's first step (s_(a−1)) reproduces the interval, and at degree ≤ 2 every mover of level l + 1 moves at most once in it; (SHIFT) at any degree, if every level-0 mover has one option, lowering every level ≥ 1 by one, the level-0 movers staying at level 0 (every option of a mover of old level 1 loses its W-target and gets the gate g(w, k_w) · Γ + g(x, k), with w its old W-target, k_w the only option of w and Γ larger than every gate; every other field and the start unchanged), gives a genome with the same run from every start; (SEG-CAP) for d ≥ 2, in every run of 𝓛_d the number of steps before the first step moving a level-0 mover, the number strictly between the first and the last such step, and the number after the last one are each at most T*(d − 1); (LIFT) at any degree, raising every level of a genome by one and adding two level-0 movers A, B with two options each (Ξ-target X and no W-target, four new ranks above all others, all of even parity, with the larger of each mover on its option 0, four new gates above all others, start option 0), every option of a mover of old level 0 getting W-target A, gives a genome in which A and B never move and whose run on the old movers is the old run, state for state; (SANDWICH) T*(d − 1) ≤ T*(d) ≤ 3 T*(d − 1) + 2, and the largest number of steps before the first level-0 step over 𝓛_d equals T*(d − 1); and DEAD: the lane conjecture SEG1-2D («on every 2-wide degree-2 ladder with d levels, the number of steps before the first level-0 step is at most 2d − 1») is false, by the 5-level ladder lift_max_d4_L13 (L-RED R197's max_d4_L13 lifted one level; T 13 from its stored start, no level-0 step, 13 > 9; sha1 33fec48f…), and by SANDWICH any bound on that number over 𝓛_d in terms of d is a bound on T*(d − 1) (2026-11-04) — a REDUCTION / two-sided recursion inside the IDEAL model; bounds nothing polynomially (the upper recursion gives 3^d − 1); the trade-off CONJECTURE SLOT-TRADE is not claimed; Ξ-cyclic genomes and degree ≥ 3 for SEG-ONCE / SEG-CAP / SANDWICH are not covered; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (DATA: experiments/new/box158/lift.py and three.py on three lifted champions; experiments/new/box157/segcheck.py, 0 violations on 59 corpus runs and on 34,934 random runs (every start for N ≤ 8, the genome start otherwise)) (P-IDEAL-SLOT, docs/new/P-IDEAL-SLOT.md with its fixes entry 1, docs/new/P-IDEAL-SLOT-fixes.md; L-NEW successor 51), CHECKER PASS (docs/checker/C121.md, checker PENDING)
- Object (L-NEW successor 51, Opus 5.5, D14 / D18; frozen, unchanged during review): packet P-IDEAL-SLOT, docs/new/P-IDEAL-SLOT.md, sha1
  62901b5f951598fb44426942b0fb1d999325625a, 192 lines (l-new freeze e46e98a4, 2026-11-04T12:45:25Z, the file's only commit; identical at
  b261c3f9). Both referees measured the sha1 (REFEREE l. 4 «docs/new/P-IDEAL-SLOT.md: sha1 62901b5f951598fb44426942b0fb1d999325625a, 192
  lines;»; REFEREE-2 l. 6 «docs/new/P-IDEAL-SLOT.md sha1 62901b5f951598fb44426942b0fb1d999325625a, 192 lines;»). Title (l. 1): «Packet
  P-IDEAL-SLOT (box 158): one level less (SHIFT), segment caps (SEG-CAP), one level more (LIFT); T*(d−1) ≤ T*(d) ≤ 3 T*(d−1) + 2 and max
  seg1 = T*(d−1) on 2-wide degree-2 ladders; DEAD: the linear first-segment bound SEG1-2D». Status (l. 5-6): «Not a TARGET.md claim.»
  «Every statement is about the IDEAL-ACYC model only. No polynomial bound is claimed anywhere. G-N5-TIME stays OPEN.» To sign: §1-§2
  SEG and SEG-ONCE (copies), §3 SHIFT, §4 SEG-CAP, §5 LIFT and SANDWICH, §6 the DEAD of SEG1-2D (table l. 9-16); §7 «DATA / READING (not
  to sign)». Sections: premises (l. 18-24), §0 the model (l. 26-44), §1 (l. 46-69), §2 (l. 71-83), §3 (l. 85-110), §4 (l. 112-134), §5
  (l. 136-164), §6 (l. 166-178), §7 machine check, EXCLUDED, TARGET diff, READING (l. 180-192). Source: «Source:
  docs/new/N5-SLOT-box158.md §1 (box 158). This packet governs: every proof below is written out in full here and» «is checked against
  this text only.» (l. 4-5).
  Fixes: docs/new/P-IDEAL-SLOT-fixes.md, append-only, entries 1 and 2 (6eb389a6 and b261c3f9; 43 lines, sha1
  cae85ce1937948648fc2a24bb4ea7db639d96123). They change the line only: entry 1 makes L-2 (REFEREE SLOT-L1, SLOT-L2, SLOT-L3), entry 2
  makes L-3 (REFEREE-2 SL-L2); «No statement or DATA change.» (l. 36); «Applied; nothing else changed.» (l. 40-41).
  The RESULTS line is L-3, 0c51ce6da0a655c31112515c78cb0b5d22690168 (docs/new/P-IDEAL-SLOT-line-L3.txt, l-new b261c3f9, the file's only
  commit). The title is L-3 verbatim, with nothing inserted (its date parenthesis «(2026-11-04)» and its source note are the line's own;
  the source note names fixes entry 1, and entry 2 is in the same file). Line history: L-1 (17236fb1, e46e98a4, frozen with the packet),
  L-2 (55e74726, 6eb389a6, fixes entry 1: SHIFT's and LIFT's constructions written out, SEG's frozen state named s_(a−1)), L-3 (fixes
  entry 2: «over 𝓛_d» in the DEAD clause); my own token diffs equal the entries' word diffs (21 hunks; 1 hunk). L-3 MATCHES at both
  referees: REFEREE (241a8c14) l. 175 «VERDICT: line L-3 MATCHES. All 7 statements stay SIGNED.»; REFEREE-2 (a6713a1a)
  R2-P-IDEAL-SLOT-L2.md l. 48 «Verdict: L-3 MATCHES. All my items on P-IDEAL-SLOT are closed.», after a byte test (l. 45-46: L-2 with
  its single «any bound on that number in terms of d» replaced «equals L-3 exactly (True)»). Both diffed every definition in the line
  against the packet (REFEREE l. 95 «every DEFINITION diffed against the packet», l. 141 «Definitions in L-2, diffed against the
  packet:»; REFEREE-2 l. 95 «clause by clause, every definition against the packet»). Optional items not taken: REFEREE-2 P-3 («with d ≥
  2 levels» in SEG1-2D) and its addendum remark that the source note names only fixes entry 1.
  Setting (packet §0, l. 26-44; RESULTS R104's model, the same §0 as RESULTS R108's packet): a genome G has N ≥ 1 movers x with levels
  lev(x) and deg(x) ≥ 1 options (x, k), each option with a W-target one level down (none at level 0), a Ξ-target (a mover or the exit
  X), a β with a distinct rank and a parity, and a distinct gate index; a start s_0 (l. 27-30); the Ξ-graph and IDEAL-ACYC (l. 31);
  chains, Ξ-values and the comparison (l. 32-34); A_s(x) (l. 35); keys (l. 36); the step under the NEW state's keys, level by level, and
  «T := the number of steps.» (l. 37-39); Mv_t, and «A mover of degree 1 has A_s(x) = {s(x)} always and never moves.» (l. 40); KP_s(x)
  at degree ≤ 2 (l. 41-42); «d-level 2-wide ladder: a genome with levels 0, …, d − 1, exactly two movers per level, all of degree 2 (N =
  2d).» (l. 43). The class 𝓛_d and T*(d) (§4 l. 113-117): «For d ≥ 1, 𝓛_d is the class of IDEAL-ACYC genomes with levels 0, …, d − 1 and
  exactly two degree-2 movers on every» «level; any number of degree-1 movers may be added at any level, and no mover has degree ≥ 3.
  T*(d) := the supremum of T over all» «genomes of 𝓛_d and all starts.»; T*(d) is finite (T*(1) ≤ 2 by SEG-ONCE, then SANDWICH's upper
  bound, whose proof uses SEG-CAP at d only; REFEREE l. 44-45 «The finiteness induction is not circular»), so the supremum is a maximum,
  the line's «largest». Notation of the line: s_t is the state after step t (s_0 the start); a LEVEL-0 STEP is a step whose movers
  include a level-0 mover (l. 118); seg1, mid and tail are the numbers of steps before the first, strictly between the first and the
  last, and after the last level-0 step (l. 120-122). The SANDWICH clause and the DEAD's «over 𝓛_d» are for d ≥ 2, the range on which
  T*(d − 1) is defined (packet l. 155).
- Claims signed (REFEREE successor 23 «(Opus 5.5, D15)», report 2a09dcf8, §C 3b8a9c77, §C addendum 1 241a8c14; REFEREE-2 successor 27
  «(Opus 5.5, D12/D19)», report cdf8e962, L-2 file a3c0ec24 with addendum 1 a6713a1a). Items (a)-(g) are SIGN in both verdict tables
  (REFEREE "## 0. Verdicts" l. 8-18 of R-P-IDEAL-SLOT.md; REFEREE-2 "## Verdicts" l. 11-21 of R2-P-IDEAL-SLOT.md), with no gap in either
  report (REFEREE l. 128 «All 7 items SIGN, no proof gap.»; REFEREE-2 l. 21 «Gaps: none.»), and stay SIGNED at L-3 (REFEREE l. 175;
  REFEREE-2 L2 file l. 48); the table is to-check (4). (a), (c) and (e) hold at ANY degree, (b) at degree ≤ 2, (d) and (f) on 𝓛_d
  (degree ≤ 2 by definition); (g) is one explicit instance. No item bounds a count polynomially; the upper recursion of (f) gives T*(d)
  ≤ 3^d − 1, an exponential bound. (a) and (b) are the same two statements as RESULTS R108 (a) and (b) (packet §1-§2 carried verbatim
  from P-IDEAL-SEG, the packet of R108); they are restated here, not proved anew, and R108 is not a premise of this entry.
  (a) Lemma SEG (§1, l. 46-69, carried verbatim from P-IDEAL-SEG §1; IDEAL-ACYC, any degree, any width): «Let l ≥ −1, and let [a, b] ⊆
      [1, T] be an interval of steps such that Mv_t contains no mover of level ≤ l for every t ∈ [a, b].»; «Let H be the genome G in
      which every mover x of level ≤ l keeps only the option s_(a−1)(x), with the same W-target, Ξ-target, β» «and gate.»; «Then the run
      of H from s_(a−1) has s_(a−1), s_a, …, s_b as its first b − a + 2 states (so H takes at least b − a + 1 steps).» (l. 48-51). Proof
      (l. 52-68): as in RESULTS R108 (a); its step (iii) uses RESULTS R105 (LOCAL), «a key only on the states below its level». Cells:
      REFEREE l. 11 «SIGN: verbatim copies of P-IDEAL-SEG §0-§2, which I signed in R-P-IDEAL-SEG.md (19e0742f)»; REFEREE-2 l. 14
      «**SIGN** (Opus 5.5, D12): byte-identical to P-IDEAL-SEG 8291ecf7 §1-§2 (signed in R2-P-IDEAL-SEG.md)».
  (b) Lemma SEG-ONCE (§2, l. 71-83, carried verbatim from P-IDEAL-SEG §2; degree ≤ 2, any width): «With l and [a, b] as in SEG: every
      mover x of level l + 1» moves at most once in [a, b] (the number of t ∈ [a, b] with x ∈ Mv_t is at most 1, l. 72-73); «In
      particular (l = −1, [a, b] = [1, T]) every level-0 mover moves at most once in the whole run.» (l. 73). Proof (l. 74-81): as in
      RESULTS R108 (b), with LOCAL's key half. Cells: as (a), the same rows.
  (c) Lemma SHIFT (§3, l. 85-110; IDEAL-ACYC, any degree, any width): «Let G be a genome in which every level-0 mover has degree 1. Let
      Γ be an integer larger» «than every gate index of G.» G↓: «every mover of level ≥ 1 has its level lowered by 1, and the level-0
      movers stay at level 0;» «every option (x, k) of a mover of old level 1 loses its W-target, and its gate becomes g′(x, k) := g(w,
      k_w) · Γ + g(x, k), where» «w := wt(x, k) and k_w is the only option of w;» «every other field (all other W-targets and gates, all
      Ξ-targets, β's, degrees) and the start are unchanged.»; «Then G↓ is an IDEAL-ACYC genome, and from every start its run is G's run,
      state for state.» (l. 86-92). Proof (l. 93-109): the new gates are distinct (g′ determines the pair (g(w, k_w), g(x, k)) as
      quotient and remainder by Γ; a new gate with g(w, k_w) = 0 equals the option's own old gate); W-targets still point one level
      down; the Ξ-data, hence values and A-sets, are unchanged; for an option at old level l ≥ 1 with W-chain o_0, …, o_l, «key^G_s(x,
      k) = (g(o_0), g(o_1), g(o_2), …, g(o_l)).» and «key^(G↓)_s(x, k) = (g′(o_1), g(o_2), …, g(o_l)), with g′(o_1) = g(o_0) · Γ +
      g(o_1).», and «Since 0 ≤ g(o_1) < Γ, g′(o_1) < g′(o_1′) iff (g(o_0), g(o_1)) < (g(o_0′), g(o_1′)) lexicographically.»; the
      degree-1 level-0 movers never move. «Does NOT claim: anything when some level-0 mover has degree ≥ 2.» (l. 110). No R105 item is
      used (REFEREE l. 29). The line's «Γ larger than every gate» leaves «integer» implicit; the two gate facts hold for any Γ above
      every gate (to-check G-2 (vi)). Cells: REFEREE «SIGN» (l. 12; §2 l. 33-42); REFEREE-2 «**SIGN** (Opus 5.5, D12)» (l. 15; l.
      33-41).
  (d) Corollary SEG-CAP (§4, l. 112-134; 𝓛_d, d ≥ 2): seg1, mid and tail as in the Setting, and «So T = seg1 + mid + tail + (number of
      level-0 steps).» (l. 123); «Statement (d ≥ 2). In every run of every genome of 𝓛_d: seg1, mid and tail are each ≤ T*(d − 1).» (l.
      124). Proof (l. 125-133): each count is the length of an interval [a, b] with no level-0 move; by SEG (l = 0) the genome H with
      the level-0 movers frozen at s_(a−1) runs from s_(a−1) through s_(a−1), …, s_b; every level-0 mover of H has degree 1, so SHIFT
      applies and «H↓ has the same run.»; «H↓ ∈ 𝓛_(d−1): its levels are 0, …, d − 2.» (its level 0 holds the two degree-2 movers of G's
      level 1 plus degree-1 movers); «So b − a + 1 ≤ T*(d − 1).». With it: at most 2 level-0 steps (SEG-ONCE, l = −1; l. 118-119) and
      the finiteness of T* (l. 115-117). «Does NOT claim: that the three counts can be ≈ T*(d − 1) at the same time (that is the open
      CONJECTURE SLOT-TRADE, not in this packet).» (l. 134). Cells: REFEREE «SIGN» (l. 13; §2 l. 43-49); REFEREE-2 «**SIGN** (Opus 5.5,
      D12)» (l. 16; l. 42-49).
  (e) Lemma LIFT (§5, l. 137-154; IDEAL-ACYC, any degree, any width): «Let G have levels 0, …, d − 1. Build G^:» «every mover of G has
      its level raised by 1;» «two new movers A, B of level 0 and degree 2 are added. Each of their four options has Ξ-target X and no
      W-target. Their β's get four» «new ranks above all ranks of G, all with even parity, the larger one of each mover on its option 0.
      Their gates are four new» «indices above all gates of G;» «every option of a mover of old level 0 gets W-target A;» «the start is
      G's start with A and B at option 0.»; «Then G^ is IDEAL-ACYC, A and B never move, and the run of G^ is G's run on the old movers,
      state for state; in particular T(G^) =» «T(G).» (l. 137-145). Proof (l. 146-154): validity; option 0 of A (and of B) carries the
      larger even rank, so it is strictly better under every state and A never moves; old chains never pass A or B; every old W-chain
      ends at A's option, so every old key gains the same first entry, «A common» «first entry does not change the order of two keys.».
      The common W-target A is essential: REFEREE l. 54-55 «This needs ALL old level-0 options to point to the SAME never-moving option,
      which the construction gives»; REFEREE-2's control lift_split_ctrl.json (l. 87-89: the old level-0 movers split between A and B, A
      and B still fixed, T 0 → 1). No R105 item is used (REFEREE l. 29). Cells: REFEREE «SIGN» (l. 14; §2 l. 50-55); REFEREE-2 «**SIGN**
      (Opus 5.5, D12) (precision N-1)» (l. 17; l. 50-58).
  (f) Corollary SANDWICH (§5, l. 155-164; d ≥ 2): «T*(d − 1) ≤ T*(d) ≤ 3 T*(d − 1) + 2.» and «The supremum of seg1 over all runs of 𝓛_d
      equals T*(d − 1).» (l. 156-157). Proof (l. 158-162): upper bound by SEG-CAP and the at most 2 level-0 steps; lower bound and seg1:
      for G ∈ 𝓛_(d−1) and any start, G^ ∈ 𝓛_d, «Its run has no level-0 step (A, B never move), so seg1 = T(G^) = T(G).»; «SEG-CAP gives
      sup seg1 ≤ T*(d − 1).». The supremum is attained (a genome of 𝓛_(d−1) with T = T*(d − 1), lifted), hence the line's «largest».
      «Does NOT claim: any polynomial bound (the upper recursion gives 3^d − 1); that T* is strictly increasing; anything off 𝓛_d for
      SANDWICH» «(LIFT itself holds for every genome).» (l. 163-164). Cells: REFEREE «SIGN» (l. 15; §2 l. 56-60); REFEREE-2 «**SIGN**
      (Opus 5.5, D12)» (l. 18; l. 59-62).
  (g) DEAD: CONJECTURE SEG1-2D (lane), in the packet's precise form (§6, l. 166-178). The killed statement (l. 167-168): «CONJECTURE
      SEG1-2D (lane; the precise form of the route «bound the first segments linearly in d», Lead brief box 158): «in every run of every
      2-wide degree-2 ladder with d ≥ 2 levels (no degree-1 movers), seg1 ≤ 2d − 1»». The line's wording drops «d ≥ 2» (at d = 1, seg1 =
      0) and «(no degree-1 movers)» (implied by «2-wide degree-2 ladder»), so it is the same statement. The instance lift_max_d4_L13, in
      full: experiments/new/box158/lift_max_d4_L13.json (claude/l-new 5e558a34, the file's only commit, unchanged at b261c3f9), sha1
      33fec48f1a8f1c57891b7574d87cc6bbe5e3bd38, 648 bytes, no trailing newline; built by experiments/new/box158/lift.py (LIFT's
      construction) from L-RED R197's genome max_d4_L13 (experiments/new/box156/ext/max_d4_L13.json, byte-equal to L-RED's
      experiments/red/r197/lag/max_d4_L13.json at claude/l-red c711987b, sha1 f0735b61312bdbfe1bb553496d7e9ee38681dcee; the instance of
      RESULTS R107's DEAD); box 139-150 JSON format (option = [W-target, Ξ-target (−1 = X), β index]; br / bp: rank / parity of β index;
      gate per option); the file's fields, verbatim: «"N": 10, "lev": [1, 1, 2, 2, 3, 3, 4, 4, 0, 0]»; «"opts": [[[8, 2, 0], [8, 3, 1]],
      [[8, 5, 2], [8, -1, 3]], [[0, 3, 4], [1, 4, 5]], [[0, 7, 6], [1, 1, 7]], [[2, 7, 8], [3, 6, 9]], [[2, -1, 10], [3, -1, 11]], [[4,
      7, 12], [5, 3, 13]], [[4, 1, 14], [5, 5, 15]], [[-1, -1, 16], [-1, -1, 17]], [[-1, -1, 18], [-1, -1, 19]]]»; «"gate": [[13, 15],
      [4, 14], [0, 9], [6, 1], [10, 11], [7, 12], [3, 8], [5, 2], [16, 17], [18, 19]]»; «"br": [9, 2, 11, 12, 5, 8, 0, 10, 1, 6, 14, 15,
      4, 7, 3, 13, 17, 16, 19, 18], "bp": [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0]»; «"start": [1, 1, 0, 0, 0, 1, 0,
      1, 0, 0], "xorder": [0, 2, 4, 6, 3, 7, 1, 5, 8, 9]». Movers 8 and 9 are A and B (level 0, both options to X, ranks 17 > 16 and 19
      > 18 on options 0 and 1, all even, gates 16-19 above the old 0-15); movers 0-7 are max_d4_L13's movers one level up, and the
      options of movers 0 and 1 (old level 0) have W-target 8 = A (REFEREE-2 l. 64-67). Packet l. 173-175: «It is a 2-wide degree-2
      ladder with d = 5 levels and no degree-1 movers.»; «The box 150 simulator runs it from its stored start: T = 13, the same states
      as max_d4_L13 on the old movers (lift.py: SAME True),» «and no level-0 step. So seg1 = 13 > 2·5 − 1 = 9.»; «So SEG1-2D is DEAD.»
      (l. 176). The run (my simulator, (10); option per mover 0..9): s_0 (1 1 0 0 0 1 0 1 0 0), s_1 (1 1 0 1 0 1 0 1 0 0), s_2 (1 1 0 1
      0 1 1 1 0 0), s_3 (1 1 0 1 1 1 1 0 0 0), s_4 (1 1 0 1 1 1 0 0 0 0), s_5 (1 1 1 1 1 1 0 0 0 0), s_6 (0 1 1 0 1 1 0 0 0 0), s_7 (0 1
      0 0 0 0 0 0 0 0), s_8 (0 0 0 0 0 0 0 1 0 0), s_9 (0 0 0 1 0 0 0 1 0 0), s_10 (0 0 0 1 0 0 1 1 0 0), s_11 (0 0 0 1 1 0 1 0 0 0),
      s_12 (0 0 0 1 1 0 0 0 0 0), s_13 (0 0 1 1 1 0 0 0 0 0); movers per step (3), (6), (4, 7), (6), (2), (0, 3), (2, 4, 5), (1, 7),
      (3), (6), (4, 7), (6), (2); movers 8 and 9 never move, so no step is a level-0 step and seg1 = T = 13. Cells: REFEREE «SIGN
      (recomputed independently, and the lift rebuilt by me from LIFT's text)» (l. 16; §2 l. 61-65; §3 l. 68-74: «T = 13, no level-0
      step, so seg1 = 13 > 2·5 − 1 = 9;», «its old-mover states equal max_d4_L13's run state for state.»); REFEREE-2 «**SIGN** (Opus
      5.5, D12): recomputed with my own simulator» (l. 19; l. 63-69: «My simulator: T 13, no level-0 step, seg1 13 > 2·5 − 1 = 9;»,
      «SEG1-2D FALSE. ✓»). With SANDWICH (packet l. 176): «More generally, by SANDWICH any bound seg1 ≤ f(d) on 𝓛_d implies T*(d − 1) ≤
      f(d).»; the line states this for bounds over 𝓛_d (entry 2; REFEREE add. 1 l. 171-172 «A bound on the narrower class of SEG1-2D
      (2-wide ladders without degree-1 movers) does not by itself bound T*(d − 1), which is defined over all of 𝓛_d.»). «Does NOT claim:
      anything about T*'s growth.» (l. 178).
  The RESULTS line (L-3) states (a)-(g) with their exact hypotheses, and nothing wider (to check (4), G-2).
- Premise: RESULTS R104's definition of the IDEAL model and of the Ξ-graph (no R104 theorem), and RESULTS R105's LOCAL, key half only:
  «a key only on the states below its level» (R105's title line; body item (b) in the form «(c) key_s(x, k) = key_(s′)(x, k) whenever s
  and s′ agree on every mover of level < lev(x).»), quoted verbatim by the packet where it is used (l. 20, 62-63, 79). L-3: «premise:
  R104's definition of the model only, no theorem of R104 used; and RESULTS R105's LOCAL, key half only». Uses: only inside the copied
  SEG (step (iii)) and SEG-ONCE, and through them in SEG-CAP and SANDWICH; SHIFT and LIFT compare keys from §0's recursive definition
  and use no R105 item (REFEREE l. 29-30; REFEREE-2 l. 26-27). Packet l. 20-23: «U, CHAIN-BACK and the CHAINED binder (R105 Erratum E-2)
  are not used.»; «Not used: RESULTS R106, R107, docs/lit, docs/sources, any other lane file. No outside source is cited. P-IDEAL-SEG is
  NOT a» «premise: its §0-§2 are copied below.»; both referees confirmed it (REFEREE l. 25-26; REFEREE-2 l. 26-28). So RESULTS Erratum
  E-2 to R105, which corrects R105's CHAINED binder, TOP-MONO's RANK_t and KEYFLIP's moves(x), does not bear on this entry, and RESULTS
  R108 (the same SEG and SEG-ONCE) is not a premise. The DEAD instance is a data file, recomputed by both referees with their own
  simulators (REFEREE «scratch/xinew_probe.py β-set simulator, written from R104's text»; REFEREE-2 «my own simulator»), and rebuilt
  from LIFT's text by REFEREE (l. 73-74) and by REFEREE-2 (l. 68-69 «my own LIFT of» «max_d4_L13 gives the same.»).
- L41 and L43. The proofs are L-NEW successor 51's (packet l. 5). The two fix rounds change the line only (SHIFT's and LIFT's
  constructions written out, SEG's frozen state named, «over 𝓛_d» in the DEAD clause), at the referees' request; the DEAD instance is
  the lane's lift of L-RED's genome; REFEREE-2's lift_split_ctrl.json is a control, not a proof step. Nothing referee-originated is a
  premise or a proof step of the entry (my reading; neither referee mentions L41). The DEAD (g) refutes a statement with the explicit
  bound 2d − 1 by one instance exceeding it (13 > 9), recomputed and SIGNED by both referees; the asymptotic route «bound the first
  segments linearly in d» is not declared DEAD here: the line states only SANDWICH's implication for bounds over 𝓛_d.
- Fixes (docs/new/P-IDEAL-SLOT-fixes.md, L-NEW successor 51, append-only; 6eb389a6 and b261c3f9; 43 lines, sha1
  cae85ce1937948648fc2a24bb4ea7db639d96123).
  - Entry 1 (l. 5-36, line L-2): «REQUIRED SLOT-L1 (SHIFT): «removing one level» → the packet §3 construction» (l. 7); «REQUIRED SLOT-L2
    (LIFT): the packet §5 construction» (l. 9); «OPTIONAL SLOT-L3 (SEG): «the interval's first state» → «the state before the interval's
    first step (s_(a−1))».» (l. 12); «The provenance tail names this fixes entry.» (l. 13); the word diff, 21 items (l. 14-35); «Every
    statement in L-2 is a signed statement of the packet (§1-§6). No statement or DATA change.» (l. 36). REFEREE §C (3b8a9c77, l.
    140-153): «finds 21 hunks, equal to entry 1's 21 items. Nothing else differs.», «SLOT-L1 is MET.», «SLOT-L2 is MET.», «SLOT-L3 is
    MET», «VERDICT: line L-2 MATCHES. All 7 statements stay SIGNED.». REFEREE-2 (a3c0ec24, R2-P-IDEAL-SLOT-L2.md l. 11-33): «## SL-L1
    (LIFT construction): MET» and «## SL-L2 (scope of the SANDWICH remark in the DEAD clause): NOT MET», with one insertion asked for.
  - Entry 2 (l. 38-43, line L-3): «In the DEAD clause, «any bound on that number in terms of d» → «any bound on that number over 𝓛_d in
    terms of d»: SANDWICH gives the implication only over 𝓛_d (packet §6). Applied; nothing else changed.» (l. 39-41); word diff: «after
    «… bound on that number»: insert «over 𝓛_d»» (l. 43). REFEREE add. 1 (241a8c14, l. 162-175): «My word diff L-2 → L-3: exactly one
    hunk, the insertion «over 𝓛_d» after «any bound on that number». This equals entry 2.»; «So REFEREE-2's SL-L2 is right, and L-2's
    wording overstated it.»; «No definition changes.». REFEREE-2 addendum 1 (a6713a1a, l. 42-48): the byte test True, «SL-L2 MET.».
  No fix changes a signed statement (to check (8)).
- Not signed: packet §7 (machine checks, EXCLUDED, TARGET diff, READING; «DATA / READING (not to sign)», l. 16), in particular its
  READING «SANDWICH pins the ladder growth question to one trade-off: T*(d) − T*(d − 1) is the extra room that the mid segment» «and the
  tail can add beyond a seg1 that already uses a full (d − 1)-run.» (l. 191-192); §6's corpus table «largest seg1 3, 5, 6, 9, 10 at d =
  3, 4, 5,» «6, 8» (l. 169-170, lane DATA). OPEN, not claimed: CONJECTURE SLOT-TRADE (the three counts of SEG-CAP cannot all be near
  T*(d − 1); l. 134, 187); any polynomial bound on T*; whether T* is strictly increasing (l. 163); anything off 𝓛_d for SANDWICH and
  SEG-CAP; Ξ-cyclic genomes; G-N5-TIME.
- Referee strengthening (NOT part of this entry; referee remarks and own checks):
  (i) REFEREE-2 l. 55-56 (N-1): the packet's «under any state, the W-chain of an old option ends at (A, 0)» holds for every state of the
      run (A never moves); «The argument needs only the common first entry, true under any state.»
  (ii) REFEREE-2 l. 57-58 and l. 87-89: the single W-target A is necessary; with the old level-0 movers split between A and B the run
       changes (lift_split_orig.json, N 3, T 0; lift_split_ctrl.json, T 1), though A and B still never move.
  (iii) REFEREE l. 79-80 and REFEREE-2 l. 79-80: replacing g′ by g(x, k) (REFEREE) or by g(w) + g (REFEREE-2) breaks SHIFT on random
        genomes (1,007 of 2,670 runs; 1,766 runs differ), so the Γ-encoding is what makes SHIFT work.
  (iv) REFEREE-2 l. 61-62: «the upper recursion gives T*(d) + 1 ≤ 3 (T*(d − 1) + 1), T*(1) ≤ 2 ⇒ T*(d) ≤ 3^d − 1. ✓».
  (v) REFEREE-2 l. 83-86: the whole SEG-CAP chain (freeze level 0, SHIFT, H↓ ∈ 𝓛_(d−1), the segment reproduced) checked on random 𝓛_d
      and the corpus: «38,444 runs, 37,312 segments, 0 violations».
- Honest limits: (i) A REDUCTION / two-sided recursion inside the IDEAL model: SANDWICH gives T*(d − 1) ≤ T*(d) ≤ 3 T*(d − 1) + 2, hence
  T*(d) ≤ 3^d − 1; it bounds nothing polynomially; G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim. (ii) SEG,
  SHIFT and LIFT hold at any degree; SEG-ONCE needs degree ≤ 2; SEG-CAP and SANDWICH are about 𝓛_d, whose movers have degree ≤ 2 and
  which allows degree-1 movers at every level; SHIFT needs every level-0 mover of degree 1; Ξ-cyclic genomes are not covered. (iii) The
  DEAD kills SEG1-2D, the packet's precise form (seg1 ≤ 2d − 1 on 2-wide degree-2 ladders), by one explicit instance (d = 5, T = 13, no
  level-0 step); the asymptotic route behind it is not declared DEAD; what the line adds is SANDWICH's implication: a bound on seg1 over
  𝓛_d in terms of d is a bound on T*(d − 1); a bound over the narrower class of ladders without degree-1 movers is not claimed to bound
  T*(d − 1). (iv) SEG-CAP bounds each of seg1, mid and tail by T*(d − 1); that they cannot all be large at once is CONJECTURE
  SLOT-TRADE, not claimed. (v) The DATA is per statement: lift.py checks LIFT on three lifted champions (max_d4_L13, max_d5_L15,
  dd_d5_F14) and three.py gives their seg1 = T; segcheck.py checks SEG on all 59 corpus and 34,934 random runs (maximal intervals only)
  and SEG-ONCE only on the runs of genomes of largest degree ≤ 2, 55 of the 59 corpus runs and 1,936 of the 34,934 random runs; the
  line's DATA parenthesis does not name these statements; SHIFT, SEG-CAP and SANDWICH are machine-checked only by the referees' own
  tools (Data). (vi) Every statement is about R104's IDEAL model on acyclic Ξ-graphs; nothing is said about a real N5 run or a parity
  game beyond what R104 already says (packet l. 188-190). (vii) Premises: RESULTS R104's definition and RESULTS R105's LOCAL, key half
  only; no other R105 item, so RESULTS Erratum E-2 to R105 does not bear on it; RESULTS R108 is not used. No lit note, no lane file, no
  outside source. No Lean. (viii) SEG and SEG-ONCE are RESULTS R108 (a), (b) again, restated in L-3's words; nothing new is claimed for
  them. (ix) Names: «SANDWICH» here is the T* recursion, not R99's Lemma SANDWICH on lexicographic sequences; «SHIFT» is not the
  quote-check control «SHIFT=1» nor R74's GATE-SHIFT; T*(d) is defined in the line and is not the T* of R16-R70; Γ is SHIFT's gate base,
  not R104's game Γ(G); «RESULTS R109» is not L-RED's box R109 (cited in R85 and R86). (x) The DEAD instance is the lane's LIFT of
  L-RED's witness max_d4_L13, used here only as a counterexample; its T is R104's number of steps.
- Data (DATA, not proof): experiments/new/box158/lift.py (l-new 5e558a34, sha1 86ca8442d7371eb865bedabaffca45c4330109f6, 21 lines;
  LIFT's construction, then both runs on the box 150 simulator and «SAME» iff the lifted run equals the old run on the old movers with
  A, B fixed) and experiments/new/box158/three.py (5e558a34, sha1 7382f097ffba08ba2b3ec5e4ec57be9736e0f7ea, 12 lines; the level-0 cuts
  and seg1, mid, tail), on the box 150 simulator experiments/new/box150/check.py (l-new 0ebddcf5, sha1
  019de0f7b36dcbd47743b3d27b4a1a93549d574b, 214 lines), wired into experiments/new/check.sh block w108 (l. 888-894) and block w109 /
  pin109 (l. 895-902 at b261c3f9, with sha1 pins of the packet, L-1, L-2, L-3, the fixes and the instance); and
  experiments/new/box157/segcheck.py (l-new 6273270f, sha1 1989263bd2b4961b5a12803a2e769b7f63fab92a, 50 lines; block w106, l. 873-879,
  as in RESULTS R108's Data); all tools unchanged at b261c3f9. Packet §7 (l. 181-186): «block w108: lift.py on max_d4_L13, max_d5_L15
  and dd_d5_F14 (SAME True each: lifted run = original on the old movers, A and B» «fixed)»; «the box 150 checker (check.py) on the
  instance gives» «XSIM 0, TOPO 0 and 0 violations.»; «SEG and SEG-ONCE: block w106 (segcheck.py; 59 corpus runs and 34,934 random runs,
  0 violations; BADLEV=2 fires).». Genome sets for segcheck.py (as in RESULTS R108): the corpus, 59 genomes, one run each from its
  stored start: 55 of largest degree 2 (N = 4..24) and 4 of degree 3 (N = 9..24; SEG only); experiments/new/box150/out/rand, 200 random
  genomes with N = 1..10, every start of those with N ≤ 8 and the genome start of the others (34,934 runs): 1,936 runs of its 93 genomes
  of largest degree ≤ 2 (SEG and SEG-ONCE) and 32,998 runs of its 107 genomes of largest degree 3 or 4 (SEG only).
  The blocks' outputs, reproduced by both referees and re-run for this draft (2026-11-04T17:23:18Z-17:23:43Z, from a `git archive` of
  b261c3f9's experiments/new and docs/new, rc 0, byte-equal to the blocks' expected strings): «LIFT max_d4_L13.json T 13 -> T^ 13 levels
  4 -> 5 SAME True», «LIFT max_d5_L15.json T 15 -> T^ 15 levels 5 -> 6 SAME True», «LIFT dd_d5_F14.json T 14 -> T^ 14 levels 5 -> 6 SAME
  True», «lift_max_d4_L13.json d 5 T 13 cuts [] seg1 13», «lift_max_d5_L15.json d 6 T 15 cuts [] seg1 15», «lift_dd_d5_F14.json d 6 T 14
  cuts [] seg1 14»; on the instance «TOTAL genomes 1 runs 1 steps 13 XSIM 0 TOPO 0 MONO 0 XINEW 0 RISE 0 CHAIN 0 KEYFLIP 0 DECR 0
  TOPMONO 0 RBOUND 0 RESTR 0 ICHARGE 0 REC 0 VIOL 0 (info REC148 0)»; «SEGCHECK runs 59 steps 650 intervals 652 SEG 0 ONCE 0 COUNT 0
  PROD 0 maxratio 0.3333»; «SEGCHECK runs 34934 steps 38676 intervals 57755 SEG 0 ONCE 0 COUNT 0 PROD 0 maxratio 1.0». REFEREE §4 l.
  82-88 («These are the expected strings.», «pin109: packet 62901b5f, L-1 17236fb1 and instance 33fec48f all EQUAL.»); REFEREE-2 l.
  75-77 («both PASS, exit 0»).
  REFEREE (successor 23; own docs/referee/scratch/slot_probe.py, sha1 6670f55b737f187f567c9e7236abec7677ebc730, on its β-set simulator
  xinew_probe.py; log xinew_logs/slot_probe.txt): «LIFT on 6,000 random genomes: 0 mismatches.»; SHIFT «on 5,290 random genomes, with
  level-0 movers made degree 1 and every old run compared state for state with the G↓ run: 0» «mismatches.»; control «Control MUT=1
  (SHIFT with g′ := g(x, k), dropping the level-0 gate): 1,007 of 2,670 mismatch.» (l. 75-80); the instance recomputed and the lift
  rebuilt (l. 68-74).
  REFEREE-2 (successor 27; own docs/referee-2/R2-P-IDEAL-SLOT/slot_check.py, sha1 57cabd72f4c5f9cf49473346635f5c0ef9152cba, «my
  simulator; SHIFT, LIFT, freeze, 𝓛_d generator all my own», no committed log): «SHIFT: 18,948 runs (random genomes with level 0 frozen
  to degree 1, degree ≤ 2 and ≤ 3, 4 starts each): 0 violations.», control 1,766 differing runs; «LIFT: 28,000 runs: 0 violations (old
  movers' run identical, A and B fixed).», control 4,984 differing runs; the SEG-CAP chain, the T decomposition and the ≤ 2 level-0
  steps on random 𝓛_d (d ≤ 8, 0-4 extra degree-1 movers), the 57 𝓛_d corpus files and T-climbs, «38,444 runs, 37,312 segments, 0
  violations» (l. 78-86); §6's corpus table «reproduced exactly» (l. 70-71); the instance recomputed (l. 63-69).
  No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-P-IDEAL-SLOT.md: successor 23's report 2a09dcf8cde246b36879ee5f1be8e7f79462a1cc
  (2026-11-04T13:15:02Z, new file, 132 lines, sha1 78e664c8a7eb05b5482a4dcb2a27421ec602c11e, with scratch/slot_probe.py and
  xinew_logs/slot_probe.txt): all seven SIGN (l. 11-16, 128); §C 3b8a9c777480d78867efd69e7f88f2d981898610 (13:50:44Z): «VERDICT: line
  L-2 MATCHES. All 7 statements stay SIGNED.» (l. 153); §C addendum 1 241a8c143c25277916c8eb35d58335afc90decf0 (15:56:51Z, 175 lines,
  sha1 b0cc2d7c5ce0e326a01ce0a510cca1cfec4e480e): «VERDICT: line L-3 MATCHES. All 7 statements stay SIGNED.» (l. 175).
  REFEREE-2 (successor 27): docs/referee-2/R2-P-IDEAL-SLOT.md cdf8e9627aadfc429eef26ef44df89aa0b7139a1 (2026-11-04T13:17:15Z, new file,
  129 lines, sha1 9a4d2d6018d5211bcaa55735c154951175b4e01d; with R2-P-IDEAL-SLOT/slot_check.py and the two control instances): every
  statement SIGN (l. 14-19, 128-129), «Gaps: none.» (l. 21); docs/referee-2/R2-P-IDEAL-SLOT-L2.md
  a3c0ec2448636334a657f6e363e7b7ec908e2c68 (14:38:07Z, new file, 40 lines) and its addendum 1 a6713a1a986c5a4c65169bfb5e9a8bb80b425f2a
  (15:56:42Z, 48 lines, sha1 99573975e3d42024941da402dbccc03bba0a466f): «SL-L2 MET.», «Verdict: L-3 MATCHES. All my items on
  P-IDEAL-SLOT are closed.» (l. 46, 48). Lane: freeze and L-1 e46e98a4964189f61164253c94513fb12c30b55f, L-2 and fixes entry 1
  6eb389a61e679ce6859d3af9ee9b4f4467cafa80, L-3 and fixes entry 2 b261c3f97c1f8a5716fd16ef43e3bc5fad2400db.
  INDEPENDENCE: REFEREE l. 2 «Independent: I did not read docs/referee-2/.»; REFEREE-2 l. 2-3 «Independent: docs/referee/ not read for
  this packet» «before this push.». REFEREE's report (13:15:02Z) precedes REFEREE-2's (13:17:15Z) by 2 min; neither cites the other's
  first report; each recomputed the instance with its own simulator written from R104's text and rebuilt the lift from LIFT's text.
  Differences, resolved: on L-1 both found LIFT's construction missing (REFEREE SLOT-L2 = REFEREE-2 SL-L1) and REFEREE's SLOT-L1 equals
  REFEREE-2's optional P-2; REFEREE-2 alone found the DEAD clause's scope (SL-L2), which REFEREE confirmed on L-3 («So REFEREE-2's SL-L2
  is right, and L-2's wording overstated it.», l. 172). Both SIGN the same seven statements with no gap and both MATCH L-3. No
  disagreement in substance.
- TARGET.md diff: TARGET.md §1-§3 define parity games («A parity game is G = (V, V_E, V_O, E, pr) with V finite»), the regions W_E, W_O,
  M4 (§2 «There is a deterministic algorithm A and a polynomial p such that for every parity game G, A on input G halts within» «p(n +
  m) steps and outputs the pair (W_E(G), W_O(G)).») and the word-RAM cost model; no statement of this entry mentions a parity game, a
  winning region, an algorithm's running time or a cost model (packet §7 l. 188-190 «Diff against TARGET.md: no statement mentions a
  parity game, a winning region, an algorithm's running time or a complexity class. Each» «is about the step sequence of the IDEAL model
  of RESULTS R104's definition. None is an M4 or M3 claim, none bounds anything» «polynomially, none is a gauntlet step.»; REFEREE §5 l.
  91-93 «Agreed with §7: not M4, not M3, not a gauntlet step. G-N5-TIME OPEN.»; REFEREE-2 l. 92-93 «SANDWICH is an exponential»
  «recursion inside the model. No M4 / M3 claim, no gauntlet step. G-N5-TIME OPEN. The packet's §7 diff is correct.»). The line (L-3)
  makes no M4 claim and no TARGET claim; its tail reads «a REDUCTION / two-sided recursion inside the IDEAL model» and «G-N5-TIME stays
  OPEN; not M3, not a step-4 pass, not a TARGET.md claim» (L-3, by script). Not a step-4 pass. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER R108's UPDATE of G-N5-TIME (GAPS at b3f38e9d, last changed by b3f38e9d: the last
UPDATE on l. 11 is R108's, «UPDATE 2026-11-04 16:53Z: RESULTS R108 (P-IDEAL-SEG; CHECKER C120 7982d57a) …», before the row's closing «
|»), built by script (upd109.py: upd100L3.py's build() unchanged for the label move, on the claim body with a sentinel tail as for R102
and R105-R108; the tail rule of (9) with R107's step for the unlabelled DEAD clause; to check (9)) only from the clauses of the title
line L-3: labels behind their clauses (the first label «(SEG, SEG-ONCE; restated in full from P-IDEAL-SEG)» moves as one unit); the DEAD
clause verbatim after (SANDWICH); « (2026-11-04) — » → «: »; the DATA parenthesis before the source parenthesis opened as «; DATA: …»;
«G-N5-TIME stays OPEN» and «not M3, not a step-4 pass, not a TARGET.md claim» dropped; the source parenthesis kept; «. G-N5-TIME stays
open.» at the end. The same script reproduces R97's to R108's LANDED UPDATEs (GAPS l. 11) byte for byte. L-3 holds no "|"; the UPDATE
holds none. <DATE> is the landing date (YYYY-MM-DD, by date -u at the landing commit; C114 Add. 1 E-1), <HH:MM> the landing time and
<checker> the CHECKER C121 commit, all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R109 (P-IDEAL-SLOT; CHECKER C121 <checker>) [refereed-only] LANDED: In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of R104 used; and RESULTS R105's LOCAL, key half only), on acyclic Ξ-graphs, with T the number of steps of a run from a given start, 𝓛_d the genomes with levels 0, …, d − 1, exactly two movers with two options on every level, any number of movers with one option and none with more than two, and T*(d) the largest T over 𝓛_d and all starts: on an interval of steps without a move at levels ≤ l (l ≥ −1), freezing the movers of level ≤ l at their options at the state before the interval's first step (s_(a−1)) reproduces the interval, and at degree ≤ 2 every mover of level l + 1 moves at most once in it (SEG, SEG-ONCE; restated in full from P-IDEAL-SEG); at any degree, if every level-0 mover has one option, lowering every level ≥ 1 by one, the level-0 movers staying at level 0 (every option of a mover of old level 1 loses its W-target and gets the gate g(w, k_w) · Γ + g(x, k), with w its old W-target, k_w the only option of w and Γ larger than every gate; every other field and the start unchanged), gives a genome with the same run from every start (SHIFT); for d ≥ 2, in every run of 𝓛_d the number of steps before the first step moving a level-0 mover, the number strictly between the first and the last such step, and the number after the last one are each at most T*(d − 1) (SEG-CAP); at any degree, raising every level of a genome by one and adding two level-0 movers A, B with two options each (Ξ-target X and no W-target, four new ranks above all others, all of even parity, with the larger of each mover on its option 0, four new gates above all others, start option 0), every option of a mover of old level 0 getting W-target A, gives a genome in which A and B never move and whose run on the old movers is the old run, state for state (LIFT); T*(d − 1) ≤ T*(d) ≤ 3 T*(d − 1) + 2, and the largest number of steps before the first level-0 step over 𝓛_d equals T*(d − 1) (SANDWICH); and DEAD: the lane conjecture SEG1-2D («on every 2-wide degree-2 ladder with d levels, the number of steps before the first level-0 step is at most 2d − 1») is false, by the 5-level ladder lift_max_d4_L13 (L-RED R197's max_d4_L13 lifted one level; T 13 from its stored start, no level-0 step, 13 > 9; sha1 33fec48f…), and by SANDWICH any bound on that number over 𝓛_d in terms of d is a bound on T*(d − 1): a REDUCTION / two-sided recursion inside the IDEAL model; bounds nothing polynomially (the upper recursion gives 3^d − 1); the trade-off CONJECTURE SLOT-TRADE is not claimed; Ξ-cyclic genomes and degree ≥ 3 for SEG-ONCE / SEG-CAP / SANDWICH are not covered; DATA: experiments/new/box158/lift.py and three.py on three lifted champions; experiments/new/box157/segcheck.py, 0 violations on 59 corpus runs and on 34,934 random runs (every start for N ≤ 8, the genome start otherwise) (P-IDEAL-SLOT, docs/new/P-IDEAL-SLOT.md with its fixes entry 1, docs/new/P-IDEAL-SLOT-fixes.md; L-NEW successor 51). G-N5-TIME stays open.

Addendum (subagent, for the Lead; does not land; written 2026-11-04T17:39:10Z by date -u). (1) FIRST FILL on line L-3 (l-new b261c3f9,
sha1 0c51ce6d…), to CHECKER C121. L-3 MATCHES at both referees (REFEREE 23 §C add. 1 241a8c14; REFEREE-2 27 addendum 1 a6713a1a); all
seven statements SIGN at both. NOT pushed; the only commit I made is the merge 6712a8d5 (the l-new, referee and referee-2 heads into
trunk b3f38e9d, as briefed; the checker head was already in b3f38e9d); the Lead's own commit f88c067a now sits on top of it (NOW.md,
LEAD-STATE.md; not mine); no tracked file edited; this file is new and untracked. The commits b261c3f9, 241a8c14, a3c0ec24 and a6713a1a
are on local trunk but not on origin trunk b3f38e9d at this fill (header): push trunk before landing. (2) TITLE l. 466 = "### R109
[refereed-only] " + L-3 without its newline + ", CHECKER PASS (docs/checker/C121.md, checker PENDING)", checked by script after the fill
(fill109.py, chk109.py): equal, byte for byte (True); the only «### R» heading of this file. (3) BODY l. 466-732 (title l. 466
to the last body line; 0 "|" in the range, by script); GAPS preamble l. 734-743 (its only "|" are the two inside the quoted
closing « |», as in R107's and R108's preambles); UPDATE l. 744 (one line, 0 "|", one <DATE>, one <HH:MM>, one <checker>; controls
True ×12: R97's-R108's landed UPDATEs). No Dead-ends row is drafted ((14)). A landing script in the shape of land108.py slices
d[465:732] for the entry and reads d[743] for the UPDATE. (4) RE-RUNS: check.sh blocks w106, w107, w108 and w109 / pin109
from a git archive of b261c3f9 (17:23:18Z-17:23:43Z, rc 0, byte-equal to the expected strings, four PASS lines); my own simulator and my
own LIFT on the three champions (17:24Z, rc 0; my LIFT of max_d4_L13 equals the committed instance field for field); my split of
segcheck.py's counts by degree (17:25Z, rc 0) ((10)). NOT RUN: the referees' tools (REFEREE's log read instead; REFEREE-2 has none), the
lane's §6 corpus table, the full check.sh, scripts/verify.sh. (5) QUOTE SWEEP: chk109.py (q104.py's rule as in chk107.py / chk108.py:
outermost guillemet quotes, whitespace joined, split at the ellipsis, parts of 6+ characters; sources: packet, L-1, L-2, L-3, fixes,
P-IDEAL-SEG at 8291ecf7, the referee files at their head commits (R-P-IDEAL-SLOT.md, R2-P-IDEAL-SLOT.md, R2-P-IDEAL-SLOT-L2.md),
REFEREE's log, notes/L-NEW.md at b261c3f9, docs/new/N5-SLOT-box158.md at 5e558a34, check.sh at b261c3f9, the lane tools, the instance
JSON, RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, NOW, TARGET.md, CLAUDE.md, C118, C119, C120, notes/CHECKER.md at 7982d57a, R108-draft,
my re-run outputs, the commit subjects cited): 603 outermost quotes, 531 parts of 6+ characters, every part found (0 not found); in the
title and body alone 201 quotes, 200 parts, 0 not found; GAPS preamble and UPDATE 10 quotes, 8 parts, 0 not found. Line-precise check of
the referee verdicts and other cited lines: 177 of 177 (source, cited line range, quote) triples found verbatim, whitespace-normalised,
inside the cited lines. Every sha1, line count and commit time cited was re-measured in this session (sha1sum, wc -l, cmp, git log -1 on
the commit), not copied from a report. (6) DISCREPANCIES: see (11) (D-1 to D-9; none affects a verdict) and G-1 to G-14 (notes). I found
no error in a signed statement. (7) FLAGS LEFT FOR THE LEAD AND CHECKER: G-9 is a CANDIDATE E-ITEM under C120 §5's rule (L-3's DATA
counts name no statement; L-3 predates the rule by 30 min; my recommendation: route an L-4 changing only the DATA parenthesis before
C121, then re-fill; wording suggested in G-9). Notes: G-8 (the C120 «…» note: SEG1-2D's text is the line's own wording; L43 clean), G-14
(SEG / SEG-ONCE are RESULTS R108 (a), (b) again), G-2 (vi) (Γ «integer» dropped), G-3 (iii) (d ≥ 2 implicit in SANDWICH and the DEAD),
G-1 (source note names fixes entry 1 only), G-6 («SANDWICH», «SHIFT», «R109», «T*», «Γ» elsewhere in RESULTS), G-11 (stale lane text).
(8) NOT VERIFIED: the Lead GO of 12:46Z (packet l. 2) and the routings of 13:23Z and 15:28Z (fixes l. 2, l. 39) are not in the
repository beyond the Lead commits e16c12c5, f71e80ea and b5675488; REFEREE-2's runs have no committed log; the referees' tools were not
re-run; L-RED R197's exactness claim on max_d4_L13 («exact max run at d 4 = 13», commit c711987b) is not used and not checked; the
lane's §6 corpus table is not re-run (not to sign). Scratch files (not committed) in
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r109: R109-template.md, fill109.py,
chk109.py / chk109.out, lp109.py, upd109.py / upd109.txt / upd109.out, land109.py / land109.out, mksim.py, runblocks.sh, blocks.out,
w106.out, w108.out, w109.out, pin109.out, mysim109.py / mysim109.out, split.py / split.out, wdiff109.py / wdiff109.out, the extracted
sources (pkt.md, seg_pkt.md, L1.txt, L2.txt, L3.txt, fixes.md, notes.md, lsremote.txt) and archb261/ (the archive). (9) LANDING
SIMULATION (land109.py, on in-memory copies of RESULTS and GAPS at local trunk): RESULTS 11,608 -> 11,876 lines, a pure insertion of 268
lines (the entry block with "checker PENDING)" filled, plus one blank line) directly after R108's block (R108 l. 10812-11028, blank l.
11029, byte-unchanged: True): True; R109 at l. 11030-11296, blank l. 11297, the next line (**Erratum E-1**) moves to l. 11298,
«**Erratum E-2**» to l. 11311, «## Dead ends» to l. 11339; order R108, R109, E-1, E-2, Dead ends: True; every other line byte-unchanged
(common prefix and suffix: True); 0 "|" inserted. GAPS: only l. 11 changes: True; new l. 11 = old l. 11 with its closing " |" replaced
by " " + the filled UPDATE + " |": True; "|" on l. 11 76 -> 76 (pipe count unchanged); «UPDATE 2026-» 43 -> 43 plus 1 UPDATE head with
the simulation year 2099; 23 -> 23 lines. Fill values used only for the simulation: <DATE> 2099-01-01, <HH:MM> 00:00, <checker> 0000000.
(10) THIS DRAFT'S SHA1: a file cannot state its own sha1. The sha1 of this file with the forty hex digits after the next colon replaced
by forty «0» characters is: e21aec4cd6ea616cdc4afcc51e5996b0e210b1f3. The file's actual sha1 and line count are in the hand-back to the
Lead (and re-measurable with sha1sum).
