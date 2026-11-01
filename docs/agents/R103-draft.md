# Draft RESULTS R103 (Lead; first fill 2026-11-01T22:23:49Z by date -u (subagent); on ANCHOR line L-2, docs/new/P-N5-ANCHOR-line-L2.txt, l-new 709798f3, sha1 1371f900c5d6eb89b4c0b947cf811185a69966e2) — to CHECKER C114
Read at the origin heads fetched at the start of the fill, 2026-11-01 before 22:05Z (l-new 2e1322eb, referee e002db99, referee-2 dc7db0e7,
checker a48ce78e, l-red 436fe6e9; origin trunk b899d68d; local trunk head 24f0cb56, a Lead commit not pushed at the fill, with RESULTS,
GAPS, DECISIONS and DECISIONS-INDEX byte-equal to origin trunk): packet f009a9a1, frozen line, L-1 (6bcf5529), L-2 and fixes entries 1-2
(709798f3); REFEREE successor 22's docs/referee/R-N5-ANCHOR.md (report 732198a9, §C on L-1 0647ff33, §C addendum 1 on L-2 e002db99);
REFEREE-2 successor 25's docs/referee-2/R2-N5-ANCHOR.md (b431ec81) and R2-N5-ANCHOR-L1.md (f6b60cfc; Addendum 1 on L-2 dc7db0e7); the L44
checks of R24 that L46 rests on (REFEREE docs/referee/R-R24-L44.md 472f0dcd with Addendum 1 at 732198a9; REFEREE-2
docs/referee-2/R2-R24-L44.md d96d2f9e); RESULTS R102 and the Erratum E-1 paragraph read LANDED (trunk 3ad13dec). Re-runs (scratch, git
archive of 709798f3): check.sh blocks "box 132 ANCHOR", "box 133 ODXI", "box 134 P-N5-ANCHOR pins" 22:07:08Z, rc 0; box133/ and
box134/pincheck.sh (Oink 8fbf0a7 --zlk / --tl, n5b) 22:07:15-22:07:16Z, rc 0, output equal to the stored pincheck.txt files; packet §7
DATA re-summed 22:07:31Z, rc 0, and re-computed on all 813 distinct lines 22:09:16-22:10:26Z, rc 0 (813 of 813 byte-identical).
TRUNK STATUS AT THIS FILL (by script, git merge-base --is-ancestor): f009a9a1, 6bcf5529, 709798f3, 732198a9, 0647ff33, e002db99, b431ec81,
f6b60cfc, dc7db0e7, 472f0dcd, d96d2f9e and l-red a612b0a5 are NOT on the local trunk (24f0cb56) nor on origin trunk (b899d68d); the
Lead merges claude/l-new, claude/referee and claude/referee-2 and pushes trunk before landing. L46 (de75072a) and its Amendment
(165dda1e) are on trunk. C113 E-2 lesson: the body names these commits on their branches only and makes NO statement about trunk, so no
body sentence depends on when the merge happens. C113 E-1 lesson: the title is L-2 verbatim with no insertion (L-2 carries its own date),
and the body says exactly that. In the body (title + entry), sentences about earlier line revisions say "at the frozen line" or "at L-1";
every other sentence describes L-2.
to check: FLAGS FIRST. G-1 is the title-shape item; G-2 the strict symbol test; G-3 the L46 citation form; G-4 the Lead readings as on
file; G-5 L41 (the C109 E-1 class), the item I would look at first; G-6 L43; G-7 DATA vs READING; G-8 stale lane text; G-9 names. No
referee raised any of them as REQUIRED, except REFEREE's optional ANC-P4 (G-2 (vii)); I changed nothing in the line. CLEAN items follow.
- FLAG G-1, TITLE SHAPE (note; no Lead insertion). L-2 contains «2026» once, as « (2026-11-01) — », the only « — » (by script), and ends
  with a source parenthesis «(P-N5-ANCHOR, docs/new/P-N5-ANCHOR-box134.md with its fixes entry 1, docs/new/P-N5-ANCHOR-fixes-box134.md;
  L-NEW successors 45-46)», the shape of R101's «(P-N5-GATE, docs/new/P-N5-GATE-box120.md with its fixes entry 1,
  docs/new/P-N5-GATE-fixes-box120.md; L-NEW successors 43-44)». All 23 landed titles R80-R102 carry a "(YYYY-MM-DD)" date; R92 and
  R95-R101 name a P-N5 packet in their title (R102 does not) (by script over the «### R» headings). So the title is "### R103
  [refereed-only] " + L-2 + the fill, nothing inserted (R102's G-1 insertion is not needed here). Two notes for CHECKER: (a) the source
  note says «with its fixes entry 1» while the fixes file at 709798f3 has entries 1-2 and L-2 is entry 2's output; entry 2 changes the
  line only (fixes l. 50 «The packet's §1 [RULE] already defines κ_j the same way; no packet change.», l. 51-52 «nothing else changes»),
  so the packet text of record is the packet with entry 1. Neither referee raised it (REFEREE §C addendum 1 l. 172 «Diff against L-1: one
  insertion and nothing else.»; REFEREE-2 L1 Add. 1 l. 54 «Nothing else changed.»). A change to «entries 1-2» would be a line change (an
  L-3 with both referees' word diffs), not a Lead edit. (b) «L-NEW successors 45-46»: boxes 130-131 are successor 45's (l-new d4024537,
  dc8c555c), boxes 132-134 and the freeze successor 46's (git log subjects); the packet's l. 1 «a referee packet from L-NEW boxes 130-133».
- FLAG G-2, STRICT SYMBOL TEST (the C109 E-2 class; soft, CHECKER decides). Both referees' binder tests pass and κ is now bound: REFEREE §7
  l. 123 «Definitions: FL run, ℓ, CN, T_x, T_c, ℓ*, ODIFF_j, gating data, epoch, GCH and CAP are bound.»; §C addendum 1 l. 176 «**ANC-L3
  met.** κ is bound. c is bound in the same clause.»; REFEREE-2 §6 l. 143-144 «Binder: FL run, a, b, j, s0, x, h, y, c bound in their
  clauses. CN, T_x, T_c, ℓ*, ODIFF_j, gating data, epoch, GCH and CAP are»; L1 Add. 1 l. 56 «κ is defined. c is bound inside the
  parenthesis, and x is the rule's vertex.», l. 58 «No new free symbol.» My stricter test ((7) below) finds, NOT glossed in L-2:
  (i) «Iσ_(j−1)(y)» in the 1E-N3 gloss (packet §1 l. 19 «Iσ_j := SPEC S2's improving set of σ_j.»). R95-R102's titles that use Iσ gloss
  it; R87, R89, R91 and R92 use it with no "improving" gloss (by script).
  (ii) «Ξ_j» and «σ̄_j» (packet §1 l. 18). REFEREE §7 l. 121 «Optional: ANC-P1 (cite R57 only for the S4a premise); «Ξ_j» / «σ̄_j» could
  be glossed «(SPEC S1 at σ_j)»; «level» = ℓ.» Only ANC-P1 was taken (fixes 1.5). σ̄ occurs without a "counterstrategy" gloss in 18
  landed titles (R27-R102, by script); C113 N-4 accepted σ̄ for R102. R101's title uses Ξ without a gloss.
  (iii) «⊕» in T_x (packet §1 l. 17 «Values, ⊴, ◁, ▷ and ⊕ (prepending a vertex to a play's value) are as in SPEC S1.»). R93 and R96, the
  landed titles with ⊕, define it; L-2 would be the first title with an unglossed ⊕ (by script).
  (iv) n and m in «≤ n + m» (packet §1 l. 14 «n := |V|, m := |E|»). A loose pattern ("n" as a word, no "n :=") matches 43 landed titles,
  R16-R95 (not read by hand).
  (v) «level» in ℓ*'s definition and in the PREFIX clause (= ℓ; REFEREE l. 121, above).
  (vi) the count «FL» in the tail «neither FL nor GCH is bounded here» (packet §5 l. 114 «FL := b − a»); the claim clauses say «b − a − 1»
  and «FL runs are polynomially long», so the count is named only in the scope words.
  (vii) the vertex x of the rule clause: REFEREE's optional ANC-P4 (e002db99, l. 178-180): ««x» in «x's W′-cycle node» and «x occurs on
  its play» refers to «every Even vertex that is not its own W′-cycle node», which is not named.», «The referent is unambiguous. «every
  Even vertex x that is not …» would bind it.», «This is left to CHECKER / the Lead.» LISTED AS ASKED; the line is not changed (a change needs an
  L-3). The same «x» is also unquantified in the FL-TIGHT clause «σ_j(x) ∈ T_x at every state» (packet l. 55 «σ_j(x) ∈ T_x for every
  Even x and every state j ∈ [a, b]»; for x ∈ CN the line's T_c is meant); my observation, raised by no referee.
  (viii) «W′» is used («not its own W′-cycle node») before «W′ := the arena optimum» in the same parenthesis.
  (ix) «fixes §2.3» is §2.3 of R24's fixes file docs/new/P-N5-U1-fixes-box31.md (REFEREE R-R24-L44.md l. 4 «its fixes
  docs/new/P-N5-U1-fixes-box31.md (sha1 88675ab7…, §1.1, §1.2, §2.1-§2.3, §7.1-§7.3)», l. 13), not the ANCHOR fixes file named in the
  tail (sections 1.1-1.5 and 2.1); the words are CF-1's (R-R24-L44.md l. 67).
  (x) «(R1)» is the packet's item name (§1 l. 49); the line's preceding words state it («applied at every Even vertex … including
  non-movers»). R26's body uses «P-N5-NH (R1)» for another object (RESULTS l. 1175), and REFEREE-2's L44 check lists «(R1)-(R4) from
  P-N5-NH §3» among the objects of R24's Setting (R2-R24-L44.md l. 19).
  None is a claim clause's quantifier except (vii); every claim clause's own variables (y, h, A, s0, x in FL-ANCHOR, c) are bound.
- FLAG G-3, THE L46 CITATION FORM (note). L-2: «with RESULTS R24 (a) Lemma R and R24 (b)'s choice rule (TB proof steps 1, 3-5; fixes
  §2.3) with bridge B, whose proof uses no 𝒞^1O hypothesis (Lead reading L46)». L46 (docs/DECISIONS.md l. 392-401): «a citing line states
  it as «R24 (a) Lemma R and R24 (b)'s choice rule (TB proof steps 1, 3-5) with bridge B; its proof uses no 𝒞^1O hypothesis» (REFEREE
  CF-1)». CF-1 itself (R-R24-L44.md l. 67-68): «cite «R24 (a) Lemma R and R24 (b)'s choice rule (TB proof steps 1, 3-5; fixes §2.3), with
  bridge B», with «its proof uses no 𝒞^1O hypothesis» per L44.» Differences: «; fixes §2.3» (CF-1's, not L46's) and «, whose proof»
  for «; its proof». «whose» can be read as bridge B's proof; both readings are true (bridge B is proved in the packet on every game, §2
  l. 61-65; R24 (a)/(b) are class-free by both L44 checks). The frozen line already had «whose» (by script). Both referees accept the
  form: REFEREE §1 l. 28-29 (the packet's citation) «is my CF-1 (R-R24-L44.md §3, 472f0dcd), word for word ✓. Bridge B is signed here
  (§2), as CF-1 required ✓.»; REFEREE-2 §6 l. 142 «L46's citation form is used.» L44's rule «the entry quotes both confirmations» is met
  in the body (Premises), from the two L44 files (not on trunk at this fill; G-8 of the header).
- FLAG G-4, LEAD READINGS AS ON FILE (the C111 E-1 class; my check). RESULT: CLEAN.
  L46 + Amendment (DECISIONS l. 392-406; index l. 39 «active»): the Amendment (165dda1e, 17:35:28Z) precedes L-1 (17:51:22Z). L-2's
  «where an option is a corner when x occurs on its play before its cycle node (vacuous for fully W′-optimal options)» is the Amendment's
  (2) («h occurs on the option's play BEFORE that play's cycle node») with REFEREE-2's vacuity («the clause is vacuous on fully W′-optimal
  options»); «the κ-least FULLY W′-optimal option, W′ := the arena optimum» is L46's «tied» («fully optimal under W′ = H_k's arena optimum
  (W′(z) ⊕ h = W′(h)), not under W_k»). L46's «Not covered: R24 (c)-(e).»: L-2 cites (a) and (b) only (by script: «R24 (c)», «(d)»,
  «(e)» 0 times). The Amendment's attribution (1) is not restated in L-2.
  L44 (l. 376-381): (i) the statements of R24 (a) and (b) carry no class hypothesis, (ii) both referees confirm that the signed proofs use
  none. L46 records both confirmations before any citing packet and allows «A citing packet may quote both confirmations as L44's (ii);
  its own referees still check how the items are used.»
  L42 / L45: the premise is R57's 1E-N3 in its S4a form only (ANC-P1 took «/ R102» out, fixes 1.5 l. 31-32); L42 (DECISIONS l. 363) «covers S1's procedure
  and S4a (σ_(k+1) is the pointwise optimum of H_k)» and is indexed «active (S4b part lifted by L45)»; REFEREE §1 l. 26-27 «FL runs keep
  τ, so S4b (R102, L45) is never used.» The titles of R91, R93, R95-R97 and R99-R101 carry an S4a «one-player arena» gloss (by script).
- FLAG G-5, L41 AND R17 (F1) (the C109 E-1 class; CHECKER decides; the item I would look at first). L-2 contains «referee-originated» 0
  and «lane-authored» 0 times. The packet's proofs are L-NEW's (successor 46), and both referees say no proof here is referee-originated:
  REFEREE l. 4 «L41 (lane-authored proofs; nothing here is referee-originated)»; REFEREE-2 §6 l. 142 «L41: no referee-originated proof
  (G-ANC-1's closure is a reading of signed items).»; §3 l. 64 «This uses R24 (a)/(b) as signed, so it is no new proof (L41 is not
  triggered).» The (R1) ruling and G-ANC-1's vacuity argument are referee readings of signed items, credited «(both referees)» in L-2.
  THE POINT TO CHECK: the cited «TB proof steps 1, 3-5» include step 1, and TB's step 1 cites R17 (F1): P-N5-U1 packet §2 l. 63-64
  «σ_{k+1} is the optimiser's counterstrategy of one call Engine.evaluate on the dual of H_k (n5.py S4a). So W'(x) = W*_{H_k}(x),», «the
  H_k-optimal value, for every x. σ_k is a strategy of H_k, so W*_{H_k} ⊵ W_k pointwise by (F1).»; REFEREE-2 R2-R24-L44.md l. 45-46
  «Step 1: SPEC S4a (σ_(k+1) is the dual-Odd choice of one S1 call on dual(H_k)), and R17 (F1) on the one-player arena H_k (Odd fixed
  to», «τ_k).» R17 (a) (RESULTS l. 738-740) records «(F1) has two independent derivations: REFEREE via the dual of VJ00 Lemma 5.5's
  proof,» «REFEREE-2 via VJ00 (11) in the dual game plus the "⊵" halves of (4)/(6), which VJ00 asserts and REFEREE-2 derived.» R101's
  landed title carries for exactly this premise «the premises R17 (F1) and R18 (d) Lemma S (a) rest on derivations written by REFEREE and
  REFEREE-2 (R17 (a))», added after C109 E-1 (C111 G-3: «C109 E-1 failed because the clause was absent, not because a word was
  missing.»). L-2 has no such clause. My reading (not a referee statement): the choice form needs only step 1's first half (σ_j is the
  S1 output, W′ = the arena optimum, i.e. 1E-N3); the (F1) half («W*_{H_k} ⊵ W_k») feeds TB's step 2 (the mover's strict decrease), which
  the citation leaves out, and FL-OPT gets W_(j−1) = W*_j from flatness, not from (F1). TB-1 / G-TB-1 (R24 (b) «closed by an (F1)-only
  case proof») sit in step 2 too (REFEREE-2 R2-R24-L44.md l. 47-49). Neither ANCHOR referee raised it. If CHECKER finds (F1) used, the
  move is an L-3 tail clause, e.g. "R24 (b)'s TB step 1 cites R17 (F1), whose derivations were written by REFEREE and REFEREE-2 (R17
  (a))" (my wording), with both referees' word diffs.
- FLAG G-6, L43 (DEADs). CLEAN. L-2's DEAD is «Ξ at ODIFF vertices is constant inside an FL run», an explicit bound (0 changes), killed
  by four hashed instances. L-2 contains «O(» 0, «c·n» 0, «linear» 0, «unbounded» 0 times; «polynomially» 2 times, both inside the
  EQUIVALENCE clause (Corollary FL-GCH), not in a DEAD. The packet heading's «(or O(1))» was dropped (fixes 1.5 l. 40-42), as both
  referees asked: REFEREE l. 112-113 «ANC-P3 (precision, L43): the packet §6 heading kills «constant (or O(1))». A finite instance cannot
  kill «O(1)». The line correctly», «states only «constant».»; REFEREE-2 §6 l. 141 «The DEAD is at an explicit bound («constant») with
  named, hashed instances (L43). No asymptotic word.»
- FLAG G-7, DATA vs READING (the C108 E-1 class). CLEAN. L-2 has NO corpus DATA clause (by script: «813» 0, «corpus» 0, «DATA» 0). Its
  numbers are the DEAD's instance counts (5 at gate 33; 43 on odxi_many_n32; n = 37), signed as instance checks by both referees and
  reproduced by their own code. The packet's §7 is «DATA (not to sign)» on «the 813 distinct (game, start) pairs» (= RESULTS Erratum E-1's
  «1,132 lines = 813 distinct (game, start) pairs on 719 distinct games»); §8 is «READING (not to sign)». The body labels both. The
  «ODIFF Ξ-changes 2» row has two conventions (REFEREE-2's N-ANC-2; fixes 1.5 l. 38-39): 2 at the source state, 13 at either state.
- FLAG G-8, STALE LANE TEXT (notes; nothing here lands). (i) fixes header l. 3 «The corrected line is docs/new/P-N5-ANCHOR-line-L1.txt
  (line L-1).» (append-only header; entry 2 l. 51 names L-2). (ii) fixes l. 20 «L46 is amended the same way (Lead, DECISIONS 17:3xZ);
  this entry follows it.» (minute unfilled; the Amendment is 17:35Z). (iii) fixes entry 2 l. 45-46 «(relayed 19:37Z)» and l. 50 «per the
  Lead 19:37Z» while 709798f3 is 19:35:59Z (the Lead's GO commit fe248064 is 19:35:46Z); the Lead's message is not in the repository (not
  verified). (iv) packet l. 37 «(RESULTS R57; R102 S4B-OPT under Lead reading L45)», l. 45-46 (the corner clause), l. 49-51 ((R1) «for
  the referees to RULE on») and §6's heading are superseded by fixes 1.5, 1.1, 1.2 and 1.5. The body quotes the superseded text only as
  history.
- FLAG G-9, NAMES (note; by script on RESULTS 84ec80fe / GAPS 50ce0e88). 0 times in both: "R103", «P-N5-ANCHOR», «FL-ANCHOR», «FL-TIGHT»,
  «FL-OPT», «FL-GCH», «bridge B», «ODIFF», «odxi», «gating data», «FL run», «ℓ*», «L46». Substrings only: «Lemma PREFIX» 4 times in RESULTS,
  all longer names (PREFIX-MONO, PREFIX-MONO-X, PREFIX-MONO-X*, PREFIX-MON); «CIRC» 12, all inside CIRCLE / CIRCLE′ (R92);
  «GCH» 2 (ORIGCH in R100), "CIRC" as a whole word 0. Same letters, other meanings, bound in their own entries: «CAP» (R25 and others), «T_c» (R13, R14, R75,
  R102), «W′» (R64, R79, R93), «κ» (329 times), «(R1)» (R22, R26, R67, R92, R93, R97). L-2 binds its own CAP, T_c, W′, κ.
- CLEAN AT L-2 (the pre-check against CHECKER's recurring items, by script on 1371f900):
  C106 E-1 (old line as current): the title is L-2; the frozen line and L-1 occur in the body only in history sentences.
  C113 E-1 (title "verbatim" after an insertion): no insertion; the body says «verbatim» and the title is byte-equal to L-2 + prefix + fill.
  C113 E-2 (trunk status that goes stale): the body has no trunk statement (header).
  C110 F-1 (stale pins vs landed labels): every file L-2 pins by sha1 prefix (odxi_n37.pg / .start; the three R179 instances) has the
  pinned sha1 at f009a9a1, 709798f3 and the l-new head 2e1322eb, and the three R179 files equal l-red a612b0a5's pins.sha1 (by script).
  The premises are landed labels (R57; R24 (a), (b)) and Lead readings on file (L46, L42); no lane packet and no unlanded result is a
  premise; L-RED R179 and L-COMP's n5b are named as instance sources and checkers only.
  C111 E-1 (stale Lead-reading statements): G-4.
- Soft spots, no referee raised them as REQUIRED (details in (11)): D-1 REFEREE's ODIFF Ξ-change count on odxi_n37 lists states «(states 2,
  3, 5, 6, 7)», REFEREE-2 and the lane give the count 5 only; D-2 REFEREE ran Oink --zlk only («I did not re-run --tl or n5b; that is the
  lane's pin.»); D-3 the packet's §7 lists two pins (u23sw64_n32, cw11_n24) with 12-hex prefixes only; D-4 the L44 files and l-red
  a612b0a5 are not on trunk (header).
(0) PLACEMENT. R103 goes DIRECTLY AFTER R102 and BEFORE «**Erratum E-1**». docs/RESULTS.md at origin trunk b899d68d (= local trunk
24f0cb56) has sha1 84ec80fef8d2f28a01a6125bae2761088b90c1bb, 10,174 lines, last changed by 3ad13dec (R102's landing). «### R102» is l.
9478 (entry l. 9478-9639, l. 9640 blank); «**Erratum E-1**» is l. 9641 (paragraph l. 9641-9652, l. 9653 blank); «## Dead ends (kept;» is
l. 9654. PROPOSED (R102's layout, C113 §7): insert R103's entry after l. 9640 (R102's blank line) and before «**Erratum E-1**», with one
blank line after it, so the R-entries stay contiguous and the erratum closes the Results section. The erratum's line references (l.
7963-9195) lie before the insertion and do not move. "### R103" and "R103" occur 0 times in RESULTS and in GAPS (sha1
50ce0e883c1510ae416c0d91e24c36bdc23f4a3e, 23 lines, last changed by 3ad13dec). The Lead re-checks (6) and (9) at landing only if RESULTS
or GAPS change after 84ec80fe / 50ce0e88.
(1) TITLE. The title is the line file docs/new/P-N5-ANCHOR-line-L2.txt (l-new 709798f3bd01683d37259fda3289b68624258127,
2026-11-01T19:35:59Z, the file's only commit, sha1 1371f900c5d6eb89b4c0b947cf811185a69966e2; identical at the l-new head 2e1322eb),
verbatim: one line, no outer quotes, no final period, 3,522 characters (3,675 bytes plus the newline), 675 whitespace tokens, 59 / 59
parentheses, one «…» pair. NO HEADING MARKER, verified by script: the file begins «N5 on EVERY game (SPEC S1-S5, under the standing SPEC
premise of RESULTS R57», with no «#» at its start, no "R??" and no lane tag (L41 «Lanes write line files without a heading marker»).
NOTHING is stripped and NOTHING is inserted: the heading is the level-3 marker, then "R103 [refereed-only] ", then the file without its
newline, then the fill ", CHECKER PASS (docs/checker/C114.md, checker PENDING)" (as R90-R102, no space before the comma). L-2 holds one
date and no "|" (G-1). Built by script (scratch fill103.py: assert the sha1 1371f900…, equality with the blob at 709798f3 and at
2e1322eb, one line, no marker, one « (2026-11-01) — », no "|"; prepend, append) and re-checked after writing this file: equal, byte for
byte. Heading: 3,601 characters, 3,754 bytes; sha1 of the heading line without its newline aeb65fb46976874290b7b30cf0a0533132cf90a7; it is l. 316.
(2) LINE HISTORY: the frozen line docs/new/P-N5-ANCHOR-line.txt (sha1 7f140d0c7711aa6c49c10d2d47ae9aaf707590bc, committed with the
packet in f009a9a1, 2026-11-01T15:37:23Z; 2,979 characters, 578 tokens; the line both reports reviewed) → L-1 baad574d (6bcf5529,
17:51:22Z; 3,323 characters, 637 tokens; fixes entry 1) → L-2 1371f900 (709798f3, 19:35:59Z; fixes entry 2). Each line file has one
commit. Word diffs measured (difflib over whitespace tokens, scratch wdiff103.py):
- frozen → L-1: 7 non-equal opcodes, 565 tokens in common, i.e. six changes: (1) «RESULTS R57 / R102» → «RESULTS R57» (ANC-P1); (2) «not
  its own W-cycle node» → «… W′-cycle node,» (P-ANC-3); (3) «(item (R1), referees to rule)),» → «((R1) holds as a consequence of R24 (a)
  and (b)'s choice rule (both referees)); a tie-break chooses the κ-least FULLY W′-optimal option, W′ := the arena optimum, where an
  option is a corner when x occurs on its play before its cycle node (vacuous for fully W′-optimal options)),» (ANC-L1 = ANCHOR-L1;
  ANCHOR-L2; ANC-1 / G-ANC-1 wording); (4) «not in CN;» → «not in CN (1 if none);» (P-ANC-2); (5) «afterwards each Even c ∈ CN moves at
  most #T_c − 1 times,» → «at transitions j ≥ s0 + ℓ* each Even c ∈ CN moves at most #T_c − 1 times in the epoch,» (ANC-L2; two opcodes);
  (6) the source note gains «with its fixes entry 1, docs/new/P-N5-ANCHOR-fixes-box134.md». = REFEREE §C l. 146-160 (seven items; its 3 +
  4 = my (3)), l. 161 «Nothing else changed.»; = REFEREE-2 L1 l. 8-25 (six items), l. 25 «Nothing else changed. The DEAD clause, CIRC,
  FL-GCH and the scope tail are token-identical.»
- L-1 → L-2: 2 insert opcodes, 637 tokens in common = ONE insertion after «the κ-least FULLY W′-optimal option»: «(κ := the vertex index
  if x's W′-cycle node c is odd, and the root-first key, i.e. the indices of the play path from c to the option, c excluded, compared
  lexicographically, if c is even; packet §1)» (ANC-L3 = ANCHOR-L1-1). Byte test True: L-1 with exactly this insertion (anchor once in
  L-1) equals L-2. = REFEREE §C addendum 1 l. 172-174; = REFEREE-2 L1 Add. 1 l. 51-54 («Byte test True: L-1 with exactly this insertion
  equals L-2. Nothing else changed.»).
No inequality of a signed statement differs between the frozen line and L-2: the changes re-cite the premise, state the (R1) ruling and
the tie set, bind ℓ* and κ, anchor the cycle-node count as packet §4 (ii) states it, and add the fixes file to the source note.
(3) THE LINE AT BOTH REFEREES. L-2 (the title): REFEREE successor 22, docs/referee/R-N5-ANCHOR.md «### §C addendum 1 (2026-11-01T21:05Z by
date -u): word-diff of line L-2» l. 169-181 (e002db99, 21:05:44Z, +14): l. 176 «**ANC-L3 met.**», l. 181 «Verdict: line L-2 **MATCHES**
(ANC-1, ANC-L1, ANC-L2, ANC-L3 all met).» REFEREE-2 successor 25, docs/referee-2/R2-N5-ANCHOR-L1.md «## Addendum 1 (2026-11-01 21:05Z by
date -u): line L-2» l. 48-59 (dc7db0e7, 21:05:22Z, +13): l. 55 «**ANCHOR-L1-1 is closed.**», l. 59 «Verdict: **MATCHES** (Opus 5.5,
D15). All my ANCHOR line items are closed.»
L-1: REFEREE §C (0647ff33) l. 166-167 «Verdict: line L-1 **does NOT yet match**. One REQUIRED item, **ANC-L3** (define κ). ANC-L1 and
ANC-L2 are met. ANC-1 is met in the», «fixes file.»; REFEREE-2 L1 (f6b60cfc) l. 37 «**Does not yet MATCH**: ANCHOR-L1-1, defining κ, is
REQUIRED.» Frozen line: REFEREE l. 21 «**REQUIRED ANC-L1** ((R1) wording) and **ANC-L2** («afterwards» unanchored) (§7)»; REFEREE-2 §6 l. 145
«Verdict on the line: **REQUIRED** (ANCHOR-L1, ANCHOR-L2).» The two referees found the same items at each step (ANC-L1 = ANCHOR-L1; ANC-L3
= ANCHOR-L1-1; fixes l. 47 «ANCHOR-L1-1 (REFEREE-2) = ANC-L3 (REFEREE)»), plus REFEREE's ANC-L2 and REFEREE-2's ANCHOR-L2, each taken at
L-1. Both MATCH L-2.
LINE-ITEM NAMES: REFEREE ANC-1 (REQUIRED, packet wording), ANC-L1, ANC-L2, ANC-L3 (REQUIRED, line), ANC-P1, ANC-P2, ANC-P3, ANC-P4
(optional); REFEREE-2 G-ANC-1 (closed gap), ANCHOR-L1, ANCHOR-L2, ANCHOR-L1-1 (REQUIRED, line), P-ANC-2, P-ANC-3 (optional), N-ANC-1,
N-ANC-2 (notes). ANC-P4 is the only one not taken (G-2 (vii)).
(4) CLAIMS SIGNED = the items below, each SIGNED in BOTH referees' verdict tables (REFEREE "## 0. Verdicts" l. 7-21 of R-N5-ANCHOR.md;
REFEREE-2 "## 1. Verdict table" l. 13-24 of R2-N5-ANCHOR.md), AND stated by L-2 (checked clause by clause against the packet):
| item (packet §, lines) | REFEREE (successor 22) | REFEREE-2 (successor 25) |
| --- | --- | --- |
| (a) Lemma FL-TIGHT (§2, l. 55-58) | l. 12 «**SIGNED**»; §2 l. 54-55 | l. 16 «**SIGNED**»; §3 l. 69-71 |
| (b) Lemma FL-OPT (§2, l. 59-60) | l. 13 «**SIGNED**»; §2 l. 56 | l. 17 «**SIGNED**»; §3 l. 72 |
| (c) Lemma bridge B (§2, l. 61-65; fixes 1.1 l. 17-18) | l. 14 «**SIGNED** with ANC-1 (wording: «h occurs on neither play before its cycle node»)»; §2 l. 57-58 | l. 18 «**SIGNED**»; §3 l. 73-75 |
| (d) Lemma PREFIX (a)-(c) (§3, l. 67-79) | l. 15 «**SIGNED**»; §3 l. 60-66 | l. 19 «**SIGNED**»; §3 l. 76-79 |
| (e) Theorem FL-ANCHOR (i)-(iii) (§4, l. 81-111) | l. 16 «**SIGNED**, given ANC-1»; §4 l. 68-81 | l. 20 «**SIGNED**, with G-ANC-1 (a proof-text gap at the corner clause of [RULE], closed in §3 below by R24 (a)/(b) as signed; no new proof)»; §3 l. 80-94 |
| (f) Lemma CIRC (§5, l. 114-118; fixes 1.5 l. 33-34) | l. 17 «**SIGNED** (precision ANC-P2: the range of j in the finer form)»; §5 l. 84-86 | l. 21 «**SIGNED**»; §3 l. 96-97 |
| (g) Corollary FL-GCH, EQUIVALENCE (§5, l. 119-124) | l. 18 «**SIGNED**»; §5 l. 87 | l. 22 «**SIGNED**»; §3 l. 96-97 |
| (h) DEAD (§6, l. 126-141; heading fixes 1.5 l. 40-42) | l. 19 «**SIGNED** (4 pins re-run by my engine, §6).»; §6 l. 89-104 | l. 23 «**SIGNED** (instance checks: all four pins re-run with my own code and Oink).»; §3 l. 98-101, §4 l. 107-116 |
RULED (not a signed claim; the line states it as the referees' ruling): (R1) (§1, l. 49-51): REFEREE l. 10 «**RULED: covered.** No
separate premise (§1)», §1 l. 30-35; REFEREE-2 l. 24 «**(R1) HOLDS** as a consequence of the cited items; it is not an extra premise (§2
below)», §2 l. 26-44. Both, verbatim: REFEREE l. 23 «No gap in the mathematics.», FINDINGS l. 132 «Every to-sign item is SIGNED, with no
gap: FL-TIGHT, FL-OPT, bridge B, PREFIX, FL-ANCHOR, CIRC, FL-GCH, and the DEAD.»; REFEREE-2 FINDINGS l. 150-151 «Signed (Opus 5.5, D15):
FL-TIGHT, FL-OPT, bridge B, PREFIX, FL-ANCHOR (i)-(iii), CIRC, FL-GCH, and the §6 DEAD (instances). There is», «no open gap.» The
packet's to-sign list (l. 8-9) names exactly (a)-(h) and (R1) «To rule on».
Clause checks (L-2 against the packet): (a) «σ_j(x) ∈ T_x at every state» = l. 55 with «for every Even x» left implicit (G-2 (vii));
(b) «σ_(j−1) is a pointwise optimum of the arena at every FL transition j» = l. 59 («H_(j−1)» = the 1E-N3 gloss's arena); (c) «every
Even h ∉ CN has σ_(j−1)(h) and σ_j(h) fully optimal in that arena» = l. 61-62 minus «o, w ∈ TIE_j(h) ⊆ T_h» (narrower); (d) the three
PREFIX clauses = (a)-(c) of l. 70-74, with «a function of that prefix and Ξ_j(A)» for «F(p_0 … p_(k−1), Ξ_j(A)) for a fixed function F»;
(e) «moves only at transitions j with j − s0 ≤ ℓ(x) − 1» = (i) l. 83 read per vertex, «at transitions j ≥ s0 + ℓ* each Even c ∈ CN
moves at most #T_c − 1 times in the epoch» = (ii) l. 84 (ANC-L2), the two bounds = (iii) l. 85; (f) «GCH ≤ b − a − 1» = CIRC's first
claim (l. 114, FL := b − a), the finer form not stated; (g) «over any family of runs, FL runs are polynomially long if and only if GCH
is polynomially bounded» = l. 119-120 «So over any family of runs, FL-POLY ⟺ GCH-POLY.»; (h) the DEAD clause = §6 with fixes 1.5's
heading. The [RULE] premise clause = §1 l. 42-48 with fixes 1.1, 1.3, 1.5 and entry 2. Nothing in L-2 is wider than signed or ruled.
Signed by both, NOT stated by L-2, so NOT landed: TIE_j(h) ⊆ T_h in bridge B; CIRC's finer form; §4 (i)'s per-level constancy
statement in its packet form. Not signed, so NOT landed: §7 DATA, §8 READING.
(5) OTHER TEXTS THE ENTRY DEPENDS ON: the premises RESULTS R57 (1E-N3, S4a form, as L42 reads it), R24 (a) Lemma R and R24 (b)'s TB
proof (packet P-N5-U1, docs/new/P-N5-U1-box31.md §2, and its fixes §2.3) read class-free by L46 under L44, with both L44 checks
(R-R24-L44.md 472f0dcd + Addendum 1 at 732198a9; R2-R24-L44.md d96d2f9e); SPEC S1-S5 (docs/new/N5-ssi-global.md). No lane packet is a
premise. Instance sources: L-NEW box 133 (odxi_n37, l-new 14bd8d23) and L-RED R179 (l-red a612b0a5). History only: docs/new/
N5-FLAT-box130.md, N5-CANON-box131.md, N5-ANCHOR-box132.md, N5-ODXI-box133.md (packet l. 6-7 «This packet restates everything it uses;
the notes are not needed to check it.»).
(6) PREMISE LABELS (stale-label test; RESULTS at 84ec80fe, GAPS at 50ce0e88). RESULTS labels in L-2 (by script): «R57» 1, «R24» 3 («R24
(a) Lemma R», «R24 (b)'s choice rule», «R24 (a) and (b)'s choice rule»); no other RESULTS label («R179» is L-RED's box label, «L-RED
R179's»; landed precedent R96's title «(L-RED R143's upward heads)»). Each exists and carries the named item:
- R57 (l. 2893): the standing SPEC premise 1E-N3 (l. 2915-2916 «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC
  conformance»), read for S4a by L42; landed S4a glosses in the titles of R91, R93, R95-R97 and R99-R101 (R101 «σ_(k+1) is a pointwise optimum of the one-player
  arena in which Even y keeps {σ_k(y)} ∪ Iσ_k(y) and Odd follows τ_k»). L-2's gloss is R101's with k → j − 1 and «at a non-fallback
  transition».
- R24 (l. 1064): heading «N5 on one-Odd-choice games»; (a) Lemma R l. 1073-1077 («every FULLY optimal successor of x (equal in cycle
  node, path set and length) survives»); (b) Lemma TB l. 1078-1081 («Tie-breaks equal SPEC S1 (iv) / FIX 4 exactly»). The class word is
  in the heading and Setting only; L46 (both L44 checks) reads (a), (b) class-free; (c)-(e) are not cited (G-4).
- Lead readings: L46 with its Amendment, L44 (inside L46), L42 (S4a part); L41, L43 as rules. All «active» in the index (l. 34-39).
- G-N5-TIME open (GAPS l. 11). R102 (P-N5-S4B) is NOT cited (ANC-P1). No label is retired by a later entry.
(7) SYMBOL TEST of the title (my own strict test of every symbol of L-2, by hand; IN = bound in the line; else the carrier):
| symbol | where |
| --- | --- |
| N5, SPEC S1-S5, Even, Odd | SPEC (named) |
| R57, 1E-N3; R24 (a) Lemma R, R24 (b) choice rule, TB, «fixes §2.3»; L46; (R1) | cited (G-2 (ix), (x)) |
| j, transition j − 1 → j, σ_j, τ_(j−1), y (1E-N3 gloss) | IN («at a non-fallback transition j − 1 → j»; «Even y keeps») |
| Iσ_(j−1)(y) | not glossed (G-2 (i)) |
| W′, W′-cycle node | IN («W′ := the arena optimum»), used before its «:=» (G-2 (viii)) |
| κ, c | IN (the κ parenthesis) |
| x (rule clause) | not named (ANC-P4, G-2 (vii)) |
| corner, «FULLY W′-optimal» | IN / R24 (a)'s «FULLY optimal» |
| FL run, a, b, j, W, τ, σ | IN («an FL run is a maximal set of consecutive transitions j − 1 → j (j = a + 1, …, b)») |
| ℓ(v), CN, T_x, T_c, ℓ*, # | IN |
| ⊕, succ, level | not glossed (G-2 (iii), (v)); succ standard |
| ODIFF_j, gating data, epoch, GCH, CAP | IN |
| σ̄_j, Ξ_j | not glossed (G-2 (ii)) |
| n, m | not glossed (G-2 (iv)) |
| FL-TIGHT's x | not quantified (G-2 (vii)) |
| h, y, A, s0, x (FL-ANCHOR), c (FL-ANCHOR) | IN (each in its clause) |
| FL (the count, tail) | not defined (G-2 (vi)) |
| tail: file paths, sha1 prefixes, n = 37, gate 33, [1, 9], 35: 34 → 33 at 5 → 6, 𝒞^1O, Oink 8fbf0a7, n5b | cited; files by path (Data) |
Agreeing tests: REFEREE §7 l. 123, §C addendum 1 l. 176-180; REFEREE-2 §6 l. 143-144, L1 Add. 1 l. 56-58. Neither lists the G-2 items
other than ANC-P4 (x) and REFEREE's optional gloss of Ξ_j / σ̄_j / «level» (l. 121).
(8) FIXES AND STATUS NOTES (docs/new/P-N5-ANCHOR-fixes-box134.md at 709798f3, sha1 3895b1dd228b786b389d03d9b0fc4dd31bdfa790, 52 lines;
= l-new head 2e1322eb; two commits: 6bcf5529 (entry 1, 42 lines, sha1 4cff05c1…) and 709798f3 (entry 2, +10); author L-NEW successor
46 (l. 2)). Entry 1 (l. 7-42): 1.1 ANC-1 = G-ANC-1 (corner wording, REQUIRED) with bridge B's repair; 1.2 ANC-L1 = ANCHOR-L1 ((R1) ruling
in the line); 1.3 ANCHOR-L2 (ties); 1.4 ANC-L2 (anchor); 1.5 optional items ANC-P1, ANC-P2, P-ANC-2, P-ANC-3, N-ANC-2, the §6 heading
(ANC-P3 = N-ANC-1). Entry 2 (l. 44-52): 2.1 ANCHOR-L1-1 = ANC-L3 (κ). REFEREE §C l. 162-165 checks entry 1 («1.2-1.4 match the line
changes.»); §C addendum 1 l. 170-171 names entry 2.1. No fix changes a signed inequality: 1.1 re-words a definition (vacuous on the tie
set) and one proof sentence; 1.2-1.4 and 2.1 are line text; 1.5 cites R57 only, states CIRC's j-range, a DATA convention and a heading.
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-2 states no CONJECTURE and kills none of RESULTS or GAPS. A line-11 UPDATE is proposed at
the end, to go AFTER R102's UPDATE (GAPS at 50ce0e88: the last UPDATE on l. 11 is R102's «UPDATE 2026-11-01 10:09Z: RESULTS R102 (P-N5-S4B;
CHECKER C113 c5c0ab5f) [refereed-only] LANDED: …», ending «G-N5-TIME stays open.» before the row's closing « |»; l. 11 holds 76 "|" and 37
«UPDATE 2026-»), as a pure insertion with one separating space. Built by script (scratch upd103.py: upd100L3.py's build() unchanged, as
upd101.py / upd102.py). L-2 has R101's shape (« (2026-11-01) — » and a source parenthesis), so build() takes it directly: labels moved
behind their clauses (searched after the binder's colon «for every FL run of every N5 run on every game, »), " (date) — " → «: », the
scope parenthesis opened into the tail minus «G-N5-TIME stays OPEN» and «not M3, not a step-4 pass, not a TARGET.md claim», the source
parenthesis kept, «. G-N5-TIME stays open.» appended. L-2 holds no "|", so no replacement list. CONTROLS (same script, same run): R97's,
R98's, R99's, R100's, R101's and R102's LANDED UPDATEs (GAPS l. 11 at 50ce0e88) rebuilt from their lines byte for byte (True ×6; 4,179,
4,260, 4,870, 4,768, 3,692 and 2,739 bytes; R102's by upd102.py's sentinel path, also equal to R102-draft l. 455). Checked by script: one
line, 0 "|", one «<HH:MM>», one «<checker>», 3,712 bytes, 674 tokens. Head «UPDATE 2026-11-01 <HH:MM>Z: RESULTS R103 (P-N5-ANCHOR; CHECKER
C114 <checker>) [refereed-only] » («P-N5-ANCHOR» 0 times in GAPS and RESULTS); <HH:MM> and <checker> are filled at landing (if R103 lands
after 2026-11-01, the head's date is corrected; the date inside the line is dropped by the rule).
(10) DATA of record = packet §7 (l. 143-156), NOT signed and NOT in L-2. Re-summed for this draft (python3 -I, scratch sum103.py over the
stored box132/a_corpus.txt (sha1 3c7072b2…, 813 rows) and box133/o_corpus.txt (cb2b6961…, 813 rows) in the git archive of 709798f3;
22:07:31Z, rc 0): the row keys are exactly the 813 distinct lines of corpus_fixed.lst (d6ed7557…; 1,132 lines, 813 distinct, 719
distinct .pg); RUNS 20, FL 42, EPOCHS 23; VIOL 0, LVLVIOL 0, EPVIOL 0, BOUNDVIOL 0; GCH 3 (XIB 0, SBB 0, CYB 3; all on cw11_n24);
XICH_ODIFF 2 (nep22f_n64, with and without start), GATEREL 0 (= packet §7 l. 149-152). Re-computed beyond the re-sum (scratch
samp103.py, seeded sample of 30, 22:07:46-22:08:09Z; full103.py, all 813 distinct lines with box132/anchor.py and box133/odxi.py, 4
workers, 22:09:16-22:10:26Z, rc 0): «full 813: equal 813 of 813» (every stored row byte-identical to the fresh output). No signed
statement uses any count.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 REFEREE's table (l. 95) gives the five odxi_n37 changes «(states 2, 3,
5, 6, 7)»; the lane (ODXI «XICH_ODIFF 5») and REFEREE-2 (l. 111 «gate 33: 5 changes») give the count only. D-2 REFEREE l. 106 «I did not
re-run --tl or n5b; that is the lane's pin.»; REFEREE-2 l. 116 ran «Oink 8fbf0a7 `--zlk -v`» only; the --tl and n5b checks are the
lane's pins (re-run here, Data). D-3 packet §7 l. 154 pins u23sw64_n32 and cw11_n24 by 12-hex prefixes («18b46837d2f0…»,
«5c6dcf2d9668…»); check.sh's box 132 block runs both. D-4 REFEREE-2's corpus figures (l. 117-125) are on its own N5 loop, REFEREE's
(l. 107-110) on random games with 2-5 Odd choice vertices: different objects, both 0 violations. D-5 REFEREE's CAP bound «CAP ≤ (n − 2)
+ m ≤ n + m» (l. 81) and REFEREE-2's «ℓ* ≤ n − 1 and Σ(|T_c| − 1) ≤ m» (l. 94) are sharper than the line's «≤ n + m»; not used.
(12) Excluded: L-NEW boxes 130-133 notes and box 134's COMPARE-W / CYC-MONO / FL-ANCHOR′ (6f630331), boxes 135-136 (2ee388a7, 15d35408)
and box 137 (2e1322eb, L-NEW successor 47: «Proposition KCH-GCH (KCH-POLY <=> GCH-POLY <=> FL-POLY)», lane-level, unreviewed); the
packet's §8 READING; the referees' tools (docs/referee/scratch/anchor_probe.py, tbcf_probe.py, anchor_logs/, tbcf_logs/;
docs/referee-2/R2-N5-ANCHOR/anchor_check.py, logs/). Not part of this entry.
(13) Commits: lane (claude/l-new): f009a9a1 (2026-11-01T15:37:23Z; freeze: packet +162, frozen line +1, R179 instances copied, box134
pincheck, check.sh «box 134 P-N5-ANCHOR pins» +6) → 6bcf5529 (17:51:22Z; fixes entry 1 +42, L-1 +1) → 709798f3 (19:35:59Z; fixes entry
2 +10, L-2 +1). Instances: odxi_n37 l-new 14bd8d23 (12:39:33Z, box 133, check.sh «box 133 ODXI»); «box 132 ANCHOR» 46ddf9ce
(11:51:28Z); R179 l-red a612b0a5 (13:14:12Z). REFEREE (claude/referee): 732198a9 (16:41:33Z; report, new file 139 lines, sha1
3455491c…; R-R24-L44.md Addendum 1 +11; scratch/anchor_probe.py, anchor_logs/, tbcf_probe.py CORNER=pre, tbcf_logs/pre_*) → 0647ff33
(18:36:59Z; §C, +28, 167 lines) → e002db99 (21:05:44Z; §C addendum 1, +14; the file now 181 lines, sha1 9da095f5…; = referee head).
REFEREE-2 (claude/referee-2): b431ec81 (16:41:38Z; report, new file 160 lines, sha1 c40e477b…, unchanged since; R2-N5-ANCHOR/ tool and
logs) → f6b60cfc (18:36:46Z; R2-N5-ANCHOR-L1.md, new file 46 lines) → dc7db0e7 (21:05:22Z; Addendum 1 +13; 59 lines, sha1 e52e2557…; =
referee-2 head). L44 checks: 472f0dcd (REFEREE, 12:38:01Z), d96d2f9e (REFEREE-2, 12:35:21Z). Lead: de75072a (13:33:00Z; L46), 165dda1e
(17:35:28Z; L46 Amendment). Trunk: see the header (the lane and referee commits are not on trunk at this fill).
(14) Placement: see (0). No Dead-ends row: L-2's DEAD «Ξ at ODIFF vertices is constant inside an FL run» is the packet's own §6 item,
signed as an instance check and named in the title, as R90 / R95 / R100 / R101 name theirs (none has a Dead-ends row; R101-draft (14)).
It kills no conjecture of RESULTS or GAPS. The Lead decides on a row.
### R103 [refereed-only] N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: at a non-fallback transition j − 1 → j, σ_j is a pointwise optimum of the one-player arena in which Even y keeps {σ_(j−1)(y)} ∪ Iσ_(j−1)(y) and Odd follows τ_(j−1)), with RESULTS R24 (a) Lemma R and R24 (b)'s choice rule (TB proof steps 1, 3-5; fixes §2.3) with bridge B, whose proof uses no 𝒞^1O hypothesis (Lead reading L46), applied at every Even vertex that is not its own W′-cycle node, including non-movers ((R1) holds as a consequence of R24 (a) and (b)'s choice rule (both referees)); a tie-break chooses the κ-least FULLY W′-optimal option (κ := the vertex index if x's W′-cycle node c is odd, and the root-first key, i.e. the indices of the play path from c to the option, c excluded, compared lexicographically, if c is even; packet §1), W′ := the arena optimum, where an option is a corner when x occurs on its play before its cycle node (vacuous for fully W′-optimal options)), with: an FL run is a maximal set of consecutive transitions j − 1 → j (j = a + 1, …, b) that are not fallbacks, keep τ, change σ and keep the valuation W of the (σ, τ)-play at every vertex; ℓ(v) := the length component of W(v), CN := {v : ℓ(v) = 0}, T_x := {y ∈ succ(x) : x ⊕ W(y) = W(x)} for Even x ∉ CN, T_c := {y ∈ succ(c) : the cycle node of W(y) is c} for Even c ∈ CN, ℓ* := the largest level of an Even vertex not in CN (1 if none); ODIFF_j := {o Odd : σ̄_j(o) ≠ τ(o)}; the gating data at state j is (σ̄_j, Ξ_j on ODIFF_j, Ξ_j on CN), an epoch is a maximal set of consecutive transitions of the run whose source states carry the same gating data, GCH := the number of states j with a < j ≤ b − 1 at which the gating data changes, CAP := (ℓ* − 1) + Σ_(Even c ∈ CN) (#T_c − 1) ≤ n + m (# = number of elements): for every FL run of every N5 run on every game, (Lemmas FL-TIGHT, FL-OPT, bridge B) σ_j(x) ∈ T_x at every state, σ_(j−1) is a pointwise optimum of the arena at every FL transition j, and every Even h ∉ CN has σ_(j−1)(h) and σ_j(h) fully optimal in that arena; (Lemma PREFIX) for y ∉ CN the Ξ_j-play from y equals the W-play up to the first vertex A of ODIFF_j ∪ CN, its vertices before A other than y have level < ℓ(y), and Ξ_j(y) is a function of that prefix and Ξ_j(A); (Theorem FL-ANCHOR) in an epoch with first source state s0, an Even vertex x ∉ CN moves only at transitions j with j − s0 ≤ ℓ(x) − 1, at transitions j ≥ s0 + ℓ* each Even c ∈ CN moves at most #T_c − 1 times in the epoch, the epoch has at most CAP transitions, and the run has at most CAP·(1 + GCH) transitions; (Lemma CIRC) GCH ≤ b − a − 1; hence (Corollary FL-GCH, an EQUIVALENCE) over any family of runs, FL runs are polynomially long if and only if GCH is polynomially bounded (2026-11-01) — REDUCTIONS and an EQUIVALENCE only (neither FL nor GCH is bounded here; charging gating changes to moves is circular; «Ξ at ODIFF vertices is constant inside an FL run» DEAD: experiments/new/box133/odxi_n37.pg (83f263c1…) with odxi_n37.start (e2ed6715…), n = 37, 5 Ξ-changes at the ODIFF gate 33 inside FL run [1, 9], one of which releases the FL move 35: 34 → 33 at 5 → 6, and L-RED R179's odxi_min_n12 (51661a75…, 𝒞^1O), odxi_lasso_n13 (5cf18798…), odxi_many_n32 (42094483…, 43 ODIFF Ξ-changes), all checked against Oink 8fbf0a7 --zlk / --tl and L-COMP's n5b; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim) (P-N5-ANCHOR, docs/new/P-N5-ANCHOR-box134.md with its fixes entry 1, docs/new/P-N5-ANCHOR-fixes-box134.md; L-NEW successors 45-46), CHECKER PASS (docs/checker/C114.md, checker PENDING)
- Object (L-NEW successor 46, Opus 5.5, D14 / D18; frozen, unchanged during review): packet P-N5-ANCHOR (box 134),
  docs/new/P-N5-ANCHOR-box134.md, sha1 ad97ad88acb453579f9381bf71d211df4ef4fe3e, 162 lines (l-new freeze f009a9a1, 2026-11-01T15:37:23Z,
  the file's only commit; identical at 6bcf5529, 709798f3 and the l-new head 2e1322eb). Both referees measured the sha1 (REFEREE l. 2-3
  «Packet claude/l-new f009a9a1, docs/new/P-N5-ANCHOR-box134.md (sha1 ad97ad88…,», «162 lines)»; REFEREE-2 §0 l. 6 «sha1
  ad97ad88acb453579f9381bf71d211df4ef4fe3e, 162 lines. Re-hashed: match.»). Title (l. 1): «P-N5-ANCHOR (box 134): inside one W-flat run,
  N5 settles level by level between gating changes; FL-POLY ⟺ GCH-POLY — a referee packet from L-NEW boxes 130-133». Scope (l. 3-5):
  «Scope: REDUCTIONS / EQUIVALENCE and one DEAD with explicit instances.», «No count is bounded here: neither FL nor GCH is bounded.»,
  «G-N5-TIME stays OPEN. This is not M3, not a step-4 pass and not a TARGET.md claim.» To sign (l. 8-9): «§2 Lemmas FL-OPT, FL-TIGHT,
  bridge B; §3 Lemma PREFIX; §4 Theorem FL-ANCHOR; §5 Corollary FL-GCH (the equivalence) and Lemma», «CIRC; §6 the DEAD (instance
  checks). To rule on: §1 item (R1).»; «Not to sign: §7 (DATA), §8 (READING).» (l. 10). Sections: §1 setting and premises (l. 13-52), §2
  FL-OPT, FL-TIGHT, bridge B (l. 54-65), §3 PREFIX (l. 67-79), §4 FL-ANCHOR (l. 81-111), §5 CIRC and FL-GCH (l. 113-124), §6 the DEAD (l.
  126-141), §7 DATA (l. 143-156), §8 READING (l. 158-162).
  The RESULTS line, history: (1) the frozen line docs/new/P-N5-ANCHOR-line.txt (sha1 7f140d0c…, committed with the packet), the line both
  reports reviewed: REFEREE REQUIRED ANC-L1 and ANC-L2 (l. 21, §7 l. 115-120); REFEREE-2 REQUIRED ANCHOR-L1 and ANCHOR-L2 (§5 l. 131-132,
  §6 l. 145). At the frozen line the rule clause read «applied at every Even vertex that is not its own W-cycle node including
  non-movers (item (R1), referees to rule)», the premise cited «RESULTS R57 / R102», and the cycle-node count read «afterwards each Even c
  ∈ CN moves at most #T_c − 1 times». (2) L-1 (docs/new/P-N5-ANCHOR-line-L1.txt, sha1 baad574d…, l-new 6bcf5529, 2026-11-01T17:51:22Z;
  fixes entry 1): six changes (word diff by script; to check (2)): R57 only (ANC-P1); «W′-cycle node» (P-ANC-3); the (R1) ruling, the
  tie set and the corner clause (ANC-L1 = ANCHOR-L1, ANCHOR-L2, ANC-1 / G-ANC-1); «(1 if none)» (P-ANC-2); the anchored cycle-node count
  (ANC-L2); the fixes file in the source note. At L-1 both referees found κ free: REFEREE §C l. 154 «**But κ is now a FREE symbol.**»
  (ANC-L3); REFEREE-2 L1 l. 28 «**ANCHOR-L1-1 (REQUIRED, one phrase): κ is undefined in the line.**» (3) L-2
  1371f900c5d6eb89b4c0b947cf811185a69966e2 (docs/new/P-N5-ANCHOR-line-L2.txt, l-new 709798f3, 2026-11-01T19:35:59Z, the file's only
  commit; fixes entry 2) = L-1 with exactly one insertion, κ's definition «(κ := the vertex index if x's W′-cycle node c is odd, and the
  root-first key, i.e. the indices of the play path from c to the option, c excluded, compared lexicographically, if c is even; packet
  §1)». REFEREE §C addendum 1 (e002db99) l. 172 «Diff against L-1: one insertion and nothing else.», l. 181 «Verdict: line L-2
  **MATCHES** (ANC-1, ANC-L1, ANC-L2, ANC-L3 all met).» REFEREE-2 R2-N5-ANCHOR-L1.md Addendum 1 (dc7db0e7) l. 54 «Byte test True: L-1
  with exactly this insertion equals L-2. Nothing else changed.», l. 59 «Verdict: **MATCHES** (Opus 5.5, D15). All my ANCHOR line items
  are closed.»
  L-2 supersedes the frozen line and L-1; the title is L-2 verbatim, with nothing inserted (its date « (2026-11-01)» is the line's own;
  to check (1)). Neither referee found a FALSE claim statement in the packet; every line item states a ruling, binds a symbol, anchors a
  count as the packet does, or re-cites a premise.
  Setting (packet §1, l. 13-35): N5 = SPEC S1-S5 «on an arbitrary game G, n := |V|, m := |E|.» (l. 14); a run is the sequence of states
  (σ_k, τ_k); «A transition j − 1 → j is a FALLBACK if S4c fired at it.» (l. 16); «Ξ_j := the valuation of σ_j under Odd's optimal
  counterstrategy σ̄_j. W_j := the valuation of the (σ_j, τ_j)-play.» (l. 18); an FL RUN (l. 20-25) is a maximal set of consecutive
  transitions j − 1 → j (j = a + 1..b) each not a fallback, with τ_j = τ_(j−1), σ_j ≠ σ_(j−1) and W_j = W_(j−1) at every vertex, «Its
  states are a..b, and W := W_a = … = W_b.»; LEVEL ℓ(v), CN, T_x, T_c, ℓ* (l. 26-31); ODIFF_j, the GATING DATA G_j, EPOCH, GCH and CAP (l.
  32-35), «CAP := (ℓ* − 1) + Σ_(c ∈ CN Even) (|T_c| − 1) ≤ n + m.» L-2's notation is the packet's, with #T_c for |T_c|, «the gating data
  at state j» for G_j, and «source states» for the packet's «GATING STATES j − 1».
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 22 (report 732198a9; §C on L-1 0647ff33; §C addendum 1 on L-2
  e002db99); REFEREE-2 successor 25 (report b431ec81; R2-N5-ANCHOR-L1.md f6b60cfc, Addendum 1 dc7db0e7)). Items (a)-(h) are SIGNED in both
  verdict tables (REFEREE "## 0. Verdicts" l. 7-21 of R-N5-ANCHOR.md; REFEREE-2 "## 1. Verdict table" l. 13-24 of R2-N5-ANCHOR.md); the
  table is to-check (4). All hold for every FL run of every N5 run on every game, under the premises below. No item bounds a count.
  (a) Lemma FL-TIGHT (§2, l. 55-58): «In an FL run, σ_j(x) ∈ T_x for every Even x and every state j ∈ [a, b].»; proof: for x ∉ CN, (V1)
      gives W_j(x) = x ⊕ W_j(σ_j(x)) with W_j = W; for x ∈ CN the play from σ_j(x) returns to x. Cells: REFEREE «**SIGNED**» (l. 12; l.
      54 «FL-TIGHT ✓.»); REFEREE-2 «**SIGNED**» (l. 16; §3 l. 69-71).
  (b) Lemma FL-OPT (§2, l. 59-60): «At an FL transition j, σ_(j−1) is a pointwise optimum of H_(j−1).»; proof (l. 60): «σ_(j−1) is a
      strategy of H_(j−1), since σ_(j−1)(y) ∈ R_j(y). Its valuation is W_(j−1) = W_j = W*_j.» Cells: REFEREE «**SIGNED**» (l. 13; l. 56
      «FL-OPT ✓. σ_(j−1) ∈ H_(j−1), and its value W_(j−1) = W_j = W*_j, the pointwise optimum.»); REFEREE-2 «**SIGNED**» (l. 17; l. 72).
  (c) Lemma bridge B (§2, l. 61-65, with fixes 1.1 l. 17-18): «At an FL transition j, let h be Even with h ∉ CN, o := σ_(j−1)(h) and w
      := σ_j(h) (w = o allowed). Then o and w are», «fully W′-optimal at h, and o, w ∈ TIE_j(h) ⊆ T_h.»; the proof's first sentence
      reads «h ∉ CN, so h occurs on neither play before its cycle node (V1); the values below are therefore h ⊕ (the option's value).»
      (fixes 1.1). Cells: REFEREE «**SIGNED** with ANC-1 (wording: «h occurs on neither play before its cycle node»)» (l. 14; §2 l.
      57-58); REFEREE-2 «**SIGNED**» (l. 18; §3 l. 73-75).
  (d) Lemma PREFIX (§3, l. 67-79): for a state j of an FL run and y ∉ CN, with A the first vertex of ODIFF_j ∪ CN on the W-play from y
      (within ℓ(y) steps), «(a) Up to A, the Ξ_j-play from y coincides with the W-play from y.», «(b) Every vertex of the prefix p_0 =
      y, …, p_(k−1) other than y has level < ℓ(y),», «(c) Ξ_j(y) = F(p_0 … p_(k−1), Ξ_j(A)) for a fixed function F.» Cells: REFEREE
      «**SIGNED**» (l. 15; §3 l. 60-66, l. 64 «(c) ✓: I checked the case where A's Ξ-play re-enters the prefix.»); REFEREE-2 «**SIGNED**»
      (l. 19; §3 l. 76-79).
  (e) Theorem FL-ANCHOR (§4, l. 81-111), «on §1 premises, [RULE], and (R1) as ruled» (l. 81): for an epoch with first gating state s0
      and last state s1, «(i) For every ℓ ≥ 1, σ_j restricted to the Even vertices ∉ CN of level ≤ ℓ is constant for j ∈ [s0 + ℓ − 1,
      s1].», «(ii) After j = s0 + ℓ* − 1 only cycle nodes move, and each Even c ∈ CN moves at most |T_c| − 1 times in the epoch after that
      point.», «(iii) The epoch has at most CAP transitions. The run has at most CAP · (1 + GCH) transitions.»; proof of (i) by induction
      on ℓ through PREFIX, [RULE] and (R1), with «TIE_j(x) = R_j(x) ∩ T_x (bridge B and W′ = W)» (l. 95, now under fixes 1.1's
      before-cycle-node reading, l. 19) and f_x idempotent; (ii) a strict ▷-chain in ξ(T_c), «No rule at cycle nodes is used.» (l. 105);
      (iii) counting. Cells: REFEREE «**SIGNED**, given ANC-1» (l. 16; §4 l. 68-81, l. 77 «κ is injective: an index, or a root-first key
      of equal length ending in y.»); REFEREE-2 «**SIGNED**, with G-ANC-1 (a proof-text gap at the corner clause of [RULE], closed in §3
      below by R24 (a)/(b) as signed; no new proof)» (l. 20; §3 l. 80-94).
  (f) Lemma CIRC (§5, l. 114-118): «GCH ≤ FL − 1, where FL := b − a.» (the line states «GCH ≤ b − a − 1»); the finer form with fixes
      1.5's range «#{j ∈ [a + 1, b] : Ξ_j(v) ≠ Ξ_(j−1)(v)}» is not in L-2. Cells: REFEREE «**SIGNED** (precision ANC-P2: the range of j
      in the finer form)» (l. 17; §5 l. 84-86); REFEREE-2 «**SIGNED**» (l. 21; §3 l. 96-97).
  (g) Corollary FL-GCH, an EQUIVALENCE (§5, l. 119-124): «For every FL run, GCH ≤ FL − 1 and FL ≤ CAP · (1 + GCH) with CAP ≤ n + m. So
      over any family of», «runs, FL-POLY ⟺ GCH-POLY.»; «Neither side is bounded here.» (l. 121); «Charging gating changes to the moves
      that cause them is CIRCULAR: substituting CIRC into §4 (iii) gives a vacuous bound.» (l. 122). Cells: REFEREE «**SIGNED**» (l. 18;
      l. 87 «It is an EQUIVALENCE and bounds neither side. «circular» is correctly flagged.»); REFEREE-2 «**SIGNED**» (l. 22; l. 96-97
      «Both directions of the equivalence are correct, and the circularity remark is right.»).
  (h) the DEAD (§6, l. 126-141; heading as fixes 1.5 l. 40-42 «DEAD: «Ξ at ODIFF vertices is constant inside an FL run»»): instance 1
      (l. 129-133) experiments/new/box133/odxi_n37.pg (sha1 83f263c1a4d0377041cd047c6adfc0343e68f02e) with odxi_n37.start
      (e2ed671588c71e8044ea8b4f7062baae918bec42), «In FL run [1, 9], Ξ at the ODIFF gate 33 changes 5 times.», «One change releases the
      FL move 35: 34 → 33 at transition 5 → 6, with W(35) unchanged.»; L-RED R179's instances (l. 134-140, «claude/l-red a612b0a5,
      copied read-only into experiments/new/box134/inst/»): odxi_min_n12 (51661a75a4ecef2225c970b8007faa9d0af2ee04, start
      91ae8cad39b2cbec6f28c671c59e9ab1dd3f6d62; «𝒞^1O, ODIFF 1. One FL transition.»), odxi_lasso_n13
      (5cf187982d72f49e61bcbbbae68d612ec1912755, start c2a4e074f89270b550321b55a79ae5811d26aa4a; «one FL transition. Lasso type: same
      cycle node, same length, path-set weight»), odxi_many_n32 (42094483eefdca2977396f563da134e09ce4839b, start
      c7565702c35945983b69b4981306e82e434bedb0; «3 FL runs, 8 transitions, 43 ODIFF Ξ-changes over run states, 4 gating changes.»); pins
      (l. 127-128) «Oink 8fbf0a7 --zlk and --tl verified, regions agree (box107/pinwin.py); n5b identical state by state;». Cells:
      REFEREE «**SIGNED** (4 pins re-run by my engine, §6).» (l. 19; table l. 93-98, own engine: odxi_n37 «**5, all at gate 33**»,
      odxi_many_n32 «**22 + 11 + 10 = 43**»; release l. 100-104; l. 105 «Oink 8fbf0a7 --zlk -v on all four pins: «verifying solution»
      completed, and my engine's final regions equal Oink's»); REFEREE-2 «**SIGNED** (instance checks: all four pins re-run with my own
      code and Oink).» (l. 23; table l. 109-114; l. 116 «Oink 8fbf0a7 `--zlk -v` on all four (logs/oink_pins.txt): «verified», and the
      regions equal N5's.»; §3 l. 99 «The killed statement «constant» is an explicit bound (0 changes) and is killed by instances.»).
  The RESULTS line (L-2) states (a)-(h) as signed and the (R1) ruling, and nothing wider: bridge B without «TIE_j(h) ⊆ T_h», CIRC without
  its finer form, FL-ANCHOR (i) per vertex (to check (4)). Its tail states the scope words, the circularity remark and the DEAD with its
  instances.
- Premise 1E-N3 (S4a form). L-2: «under the standing SPEC premise of RESULTS R57 (1E-N3: at a non-fallback transition j − 1 → j, σ_j is a
  pointwise optimum of the one-player arena in which Even y keeps {σ_(j−1)(y)} ∪ Iσ_(j−1)(y) and Odd follows τ_(j−1))». R57 (b)
  (RESULTS l. 2915-2916): «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance, and the code's match to SPEC is
  DATA (R15 G-N5T-1) (1E-N3 = N-1E-1).» Lead reading L42 (docs/DECISIONS.md l. 362-367; index «active (S4b part lifted by L45)»): «R57's
  standing SPEC premise (1E-N3) covers S1's procedure and S4a (σ_(k+1) is the pointwise optimum of H_k).» REFEREE §1 l. 26-27 «[1E-N3]:
  the S4a form (σ_j is a pointwise optimum of H_(j−1)) is RESULTS R57's standing premise, which covers S4a. FL runs keep τ, so», «S4b
  (R102, L45) is never used.» R102 is not cited (ANC-P1; fixes 1.5 l. 31-32 «FL keeps τ, so R102's S4B-OPT is not used.»).
- Premise R24 (a) Lemma R and R24 (b)'s choice rule, class-free by Lead reading L46 under L44. R24's heading names one-Odd-choice games
  and its Setting 𝒞^1O; (a) Lemma R: «every FULLY optimal successor of x (equal in cycle node, path set and length) survives, so» «the
  length step chooses among exactly the fully optimal edges (FIX 4 order).»; (b) Lemma TB with «Tie-breaks equal SPEC S1 (iv) / FIX 4
  exactly» (RESULTS l. 1073-1081). L46 (docs/DECISIONS.md l. 392-401, 2026-11-01 13:32Z): «RESULTS R24 (a) Lemma R and R24 (b) Lemma TB
  are class-free under L44 (i)-(ii): both referees confirmed, independently and before any citing packet, that the statements carry no
  class hypothesis and that the signed proofs use none;», «Not covered: R24 (c)-(e).» Amendment to L46 (l. 402-406, 17:35Z): «(2)
  wording: «corner» means that h occurs on the option's play BEFORE that play's cycle node (REFEREE R-R24-L44.md Addendum 1; ANC-1 on
  P-N5-ANCHOR);», «REFEREE-2 (R2-N5-ANCHOR G-ANC-1) shows the clause is vacuous on fully W′-optimal options.» L44 (l. 376-381) asks that
  «the citing line says so («its proof uses no 𝒞^1O hypothesis») and the entry quotes both confirmations.» The two confirmations:
  REFEREE docs/referee/R-R24-L44.md (472f0dcd) l. 91 «1. R24 (a) Lemma R (fully optimal form): CLASS-FREE. No step uses 𝒞^1O.», l. 92
  «2. R24 (b) Lemma TB as signed: CLASS-FREE. The statement already says «any game»; (F1) is used on the one-player arena H_k, which is»,
  l. 94 «3. The choice form is class-free but is not R24 (b)'s statement. Cite it as Lemma R + TB proof steps 1, 3-5 + bridge B (CF-1).»;
  REFEREE-2 docs/referee-2/R2-R24-L44.md (d96d2f9e) l. 77 «R24 (a) Lemma R: **CLASS-FREE**. L44 (i) and (ii) hold.», l. 78 «R24 (b) Lemma
  TB, including its choice form: **CLASS-FREE**. L44 (i) and (ii) hold.» The ANCHOR referees checked the use: REFEREE §1 l. 28-29 (CF-1
  «word for word ✓»; «Bridge B is signed here (§2), as CF-1 required ✓.»); REFEREE-2 §0 l. 9 «My L44 check docs/referee-2/R2-R24-L44.md
  (d96d2f9e).», §3 l. 47-49 («This is the form my L44», «precision asked for («tied under W′, not under W_k»). ✓», «At an FL transition
  W′ = W_j = W (FL-OPT), so TIE_j(x) = R_j(x) ∩ T_x, as §4 uses. ✓»), §6 l. 142 «L46's citation form is used.» L-2 carries the L44 words
  as «whose proof uses no 𝒞^1O hypothesis (Lead reading L46)» (draft G-3). The cited TB step 1 uses R17 (F1) (draft G-5; for CHECKER).
- (R1), RULED by both referees. Packet §1 l. 49-51: «[RULE] is applied at EVERY Even x ∉ CN of an FL transition, including x with
  σ_j(x) = σ_(j−1)(x).» REFEREE §1 l. 30-33: «(R1), RULED **covered**.», «So (R1) is no extra premise. It is the same citation.»;
  REFEREE-2 §2 l. 35 «None of these steps uses «v switched». The mover hypothesis enters TB only at step 2, which shows the OLD option
  σ_k(v) is optimal, and», l. 38-39 «So (R1) is a consequence of the cited», «items, not a further premise.» Fixes 1.2 (l. 22-23): «It
  is no longer an open item. Line L-1 states the ruling.» L-2: «((R1) holds as a consequence of R24 (a) and (b)'s choice rule (both
  referees))». The ruling is a reading of the cited items by both referees, not a lane claim and not a new proof (draft G-5).
- Corner clause (ANC-1 = G-ANC-1). REFEREE §1 l. 36-49 (REQUIRED, wording): read with the full lasso, the clause «excludes σ_j(x) itself
  whenever x ∉ CN lies on its own W-cycle»; fix «define a corner as «x occurs on y's play before y's cycle node».» REFEREE-2 §3 l. 50-65
  (closed): «Hence «outside the rule» is vacuous on TIE: the rule covers every fully W′-optimal option.» Fixes 1.1 (l. 9-19) keeps the
  before-cycle-node definition with the vacuity remark, «So TIE_j(x) is the set of ALL fully W′-optimal options of x.» L-2: «where an
  option is a corner when x occurs on its play before its cycle node (vacuous for fully W′-optimal options)». REFEREE §C l. 153 «The
  corner clause is in my ANC-1 form, and «vacuous» is correct».
- L41 and L43. The proofs are the packet's own (L-NEW successor 46). REFEREE l. 4 «L41 (lane-authored proofs; nothing here is
  referee-originated)»; REFEREE-2 §6 l. 142 «L41: no referee-originated proof (G-ANC-1's closure is a reading of signed items).» The DEAD
  is at an explicit statement with hashed instances (L43): REFEREE §7 l. 125 «The DEAD is explicit, with numbers that equal mine (L43
  ✓).»; REFEREE-2 §6 l. 141. Whether L-2 needs an L41 clause for R17 (F1) inside TB's step 1 is for CHECKER (draft G-5).
- Fixes (docs/new/P-N5-ANCHOR-fixes-box134.md, L-NEW successor 46, append-only, entries 1-2; at 709798f3 52 lines, sha1
  3895b1dd228b786b389d03d9b0fc4dd31bdfa790). Header (l. 1-2): «repairs to the frozen packet docs/new/P-N5-ANCHOR-box134.md (sha1
  ad97ad88acb453579f9381bf71d211df4ef4fe3e) and its line», «The packet and docs/new/P-N5-ANCHOR-line.txt stay frozen.»
  - Entry 1 (l. 7-42, «after both reports»): 1.1 ANC-1 = G-ANC-1 (corner; bridge B's sentence; «L46 is amended the same way»); 1.2 ANC-L1
    = ANCHOR-L1 ((R1) «RULED COVERED by both referees»); 1.3 ANCHOR-L2 (ties); 1.4 ANC-L2 (anchor); 1.5 optional: ANC-P1 «Line L-1 cites
    R57 only.», ANC-P2 (CIRC's j-range), P-ANC-2 / P-ANC-3, N-ANC-2 («Both conventions are stated.»), the §6 heading «An O(1) bound is not
    a statement an instance can kill.»
  - Entry 2 (l. 44-52, «after both referees' word-diffs of L-1»): 2.1 ANCHOR-L1-1 = ANC-L3 (κ defined at first use); «Line L-2:
    docs/new/P-N5-ANCHOR-line-L2.txt = L-1 with this parenthesis inserted after «the κ-least FULLY W′-optimal option»; nothing», «else
    changes.»
  No fix changes a signed inequality (to check (8)).
- Not signed: §1 (premises, notation; (R1) is ruled, not signed); §7 DATA (packet l. 143 «## 7. DATA (not to sign)»); §8 READING (l. 158
  «## 8. READING (not to sign)»). OPEN, not claimed: any bound on FL or on GCH; any bound on N5's iteration count; G-N5-TIME.
- Referee strengthening (NOT part of this entry; remarks of one referee):
  (i) REFEREE §5 l. 85 «The finer form ✓, but trivially so: at most one change per vertex per transition.»; REFEREE-2 l. 96 «The finer
      bound is trivial (≤ one change per vertex per transition).»
  (ii) Sharper CAP bounds: REFEREE l. 81 «CAP ≤ (n − 2) + m ≤ n + m.»; REFEREE-2 l. 94 «CAP ≤ n + m: ℓ* ≤ n − 1 and Σ(|T_c| − 1) ≤ m.»
  (iii) Own-engine checks beyond the pins: REFEREE's tbcf_probe.py CORNER=pre on random games with 2-5 Odd choice vertices (l. 107-110,
       «0 violations; 41 even ties with κ-min ≠ index-min, all following κ»); REFEREE-2's RULE checks on the corpus (l. 40-43, «729,730
       non-mover and 42,644 mover checks;», «0 violations.»; l. 61 «Data: 18,102 rule checks with a corner option in TIE on the corpus
       (157 on the pins, 205 on random games), 0 violations.»).
- Honest limits: (i) REDUCTIONS and an EQUIVALENCE only: neither FL nor GCH is bounded here; G-N5-TIME stays open; not M3, not a step-4
  pass, not a TARGET.md claim. (ii) Charging gating changes to the moves that cause them is circular (CIRC into FL-ANCHOR (iii) gives a
  vacuous bound); the open part is in-run gating changes (packet l. 123-124 «The CDAG-type blow-up (box 130) can», «come only from in-run
  gating changes.»). (iii) Premises: RESULTS R57's 1E-N3 in its S4a form (L42), R24 (a) and R24 (b)'s choice rule read class-free by
  L46 under L44, with bridge B signed here; (R1) is the referees' ruling on that citation. As for every landed N5 result, the correctness
  of S1's procedure stays SPEC's requirement (R57 (b)). (iv) The DEAD kills only «constant»; an O(1) or any other asymptotic bound on Ξ-
  changes at ODIFF vertices is NOT killed (L43; fixes 1.5). (v) The packet's DATA is thin: 20 FL runs, 42 FL transitions, 23 epochs on the
  813 distinct pairs; gating changes only on cw11_n24 (3, at a W-cycle node); 2 ODIFF Ξ-changes (13 under the either-state convention).
  (vi) The rule clause's vertex «x» is not named (REFEREE's optional ANC-P4).
- Data (DATA, not proof): pinned. experiments/new/check.sh at 709798f3 (sha1 5d261b96d71ddb65769f4618fc1ac9c2b8d649e9, 736 lines; the
  three blocks unchanged since they were added): «box 132 ANCHOR» l. 700-705 (46ddf9ce), «box 133 ODXI» l. 706-711 (14bd8d23), «box 134
  P-N5-ANCHOR pins» l. 712-717 (f009a9a1). Re-run for this draft from a `git archive` of 709798f3 (experiments/ and docs/new/; from
  experiments/new; GIT_DIR set to the repository), l. 1-7 (shebang, set -euo pipefail, cd) plus l. 700-717, 2026-11-01 22:07:08Z by date
  -u (start and end in the same second), rc 0: «box 132 ANCHOR: u23sw64_n32 FL run of 8 = one epoch, level timing holds; cw11_n24 3
  gating changes (Xi at a W-cycle node), 7 cycle-node moves: PASS»; «box 133 ODXI: odxi_n37 Xi at ODIFF gate 33 changes 5 times inside
  the FL run [1, 9] and releases the FL move 35: 34 -> 33 at 5 -> 6: PASS»; «box 134 P-N5-ANCHOR pins: odxi_many_n32 (R179) 8 FL
  transitions, 4 gating changes, FL-ANCHOR items hold; odxi_min_n12 one ODIFF Xi-change in its FL run: PASS». The box 133 block requires
  «ODXI odxi_n37.pg n 37 RUNS 1 FL 8 XICH_ODIFF 5 GATEREL 1 EX [(1, 6, 35, 34, 33, 33)]»; the box 134 block requires odxi_many_n32's
  «RUNS 3 FL 8 EPOCHS 7 GCH 4 VIOL 0» line and «ODXI odxi_min_n12.pg n 12 RUNS 1 FL 1 XICH_ODIFF 1 GATEREL 0».
  Oink / n5b pins (not in check.sh; box133/pincheck.sh and box134/pincheck.sh from the same archive, Oink 8fbf0a7 = tools/oink/src HEAD,
  22:07:15-22:07:16Z, rc 0 each): for all four instances «--zlk verified» and «--tl verified», PINWIN «AGREE True», «identical state
  sequences: True»; odxi_lasso_n13 «ODXI odxi_lasso_n13.pg n 13 RUNS 1 FL 1 XICH_ODIFF 1 GATEREL 0», odxi_many_n32 «ODXI odxi_many_n32.pg
  n 32 RUNS 3 FL 8 XICH_ODIFF 43 GATEREL 0»; the output equals the stored box133/pincheck.txt (14bd8d23) and box134/pincheck.txt
  (f009a9a1) line for line. Pin files: sha1 as in (h) above, equal at f009a9a1, 709798f3 and 2e1322eb; the R179 copies equal l-red
  a612b0a5's experiments/red/r179/instances/pins.sha1.
  DATA OF RECORD (packet §7, «On the 813 distinct (game, start) pairs of experiments/si/anc58/corpus_fixed.lst (RESULTS Erratum E-1;»):
  FL runs / transitions / epochs 20 / 42 / 23; violations of §4 (i) timing, level targets, epoch ≤ CAP, run ≤ CAP (1 + GCH) 0 / 0 / 0
  / 0; gating changes Ξ at ODIFF / σ̄ / Ξ at cycle node only 0 / 0 / 3 (cw11_n24); ODIFF Ξ-changes over all run states 2 («both at the
  last state of nep22f_n64's one-transition run, with and without start file»); «[RULE] DATA (box 131, the same corpus): BFS-key rule 666
  / 666 (c even, non-corner), index rule 8 / 8 (c odd).»; L-RED R177 «435 flat non-corner moves, 0 violations.» Re-summed and
  re-computed: equal (to check (10)). Convention (fixes 1.5 l. 38-39): ODIFF read at the source state j − 1 gives 2; at either state, 13
  (REFEREE-2's count, l. 125, l. 136).
  REFEREE (successor 22; own docs/referee/scratch/anchor_probe.py, «own engine rl_engine, no lane code», l. 90): table l. 93-98 (all four
  pins, 0 violations); l. 111 «Packet §7 is labelled DATA, on the 813 distinct pairs (E-1) ✓.»
  REFEREE-2 (successor 25; own docs/referee-2/R2-N5-ANCHOR/anchor_check.py, l. 104): pins table l. 109-114; corpus l. 117-118 «the 813
  distinct (game, start) pairs of anc58/corpus_fixed.lst (logs/cfu_*.txt, logs/corpus_totals.txt).», «RESULT PASS, 0 violations.»;
  table l. 120-125 («20 / 42 / 23 | 20 / 42 / 23»).
  No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-ANCHOR.md: successor 22's report 732198a9e0e50035c96b73ff8b8b8c09a93f38a6 (2026-11-01T16:41:33Z,
  new file, 139 lines, sha1 3455491c3429647f8be7678149d7bc5c1ccc12a4, with scratch/anchor_probe.py, anchor_logs/, tbcf_probe.py and
  tbcf_logs/pre_*): FL-TIGHT, FL-OPT, bridge B, PREFIX, FL-ANCHOR, CIRC, FL-GCH and the DEAD SIGNED, no gap, (R1) RULED covered, ANC-1
  and line items ANC-L1, ANC-L2 REQUIRED; §C 0647ff337a83eebc73918410f1ee39bc5e1cb75e (18:36:59Z, +28, l. 141-167): L-1 «does NOT yet
  match» (ANC-L3); §C addendum 1 e002db99686cf69c11b5eece3cd1f8cb75901466 (21:05:44Z, +14, l. 169-181; the file now 181 lines, sha1
  9da095f53c7a3db09b67fb68c97e27178087307d): «Verdict: line L-2 **MATCHES** (ANC-1, ANC-L1, ANC-L2, ANC-L3 all met).» (l. 181).
  REFEREE-2 (successor 25): docs/referee-2/R2-N5-ANCHOR.md b431ec8138182d8c69ff2c4c4701720b9890591b (16:41:38Z, new file, 160 lines, sha1
  c40e477b5291c78f77c798d05b0c4a2ded521368, unchanged since; with R2-N5-ANCHOR/anchor_check.py and logs/): every item SIGNED (l. 16-23,
  l. 150-151), (R1) HOLDS (l. 24), line REQUIRED ANCHOR-L1, ANCHOR-L2 (l. 145); R2-N5-ANCHOR-L1.md f6b60cfc8cd2aceb6165b1c60b4a85231c0a18ae
  (18:36:46Z, new file, 46 lines): L-1 «**Does not yet MATCH**» (ANCHOR-L1-1); Addendum 1 dc7db0e76a81217edcaa011ea3805a56928f0fc0
  (21:05:22Z, +13; 59 lines, sha1 e52e2557cba8bec5df4aedd58c5fb669fdba1b42): «Verdict: **MATCHES** (Opus 5.5, D15). All my ANCHOR line
  items are closed.» (l. 59). Lane: freeze f009a9a183156a0bbb36cb3c0c1f0101859e024d, L-1 and fixes entry 1
  6bcf55296efe81643f4eca57ff3c1080a17eb89d, L-2 and fixes entry 2 709798f3bd01683d37259fda3289b68624258127.
  INDEPENDENCE: REFEREE l. 3 «Written before reading docs/referee-2/ on this packet.»; §C l. 145 «REFEREE-2's report (R2-N5-ANCHOR.md,
  referee-2 b431ec81) was read only now, after mine (732198a9).» REFEREE-2 l. 3 «Independence: written without opening docs/referee/ for
  this packet, and without reading the lane's box130-134 scripts.»; L1 l. 5-6 «I have now also read REFEREE's R-N5-ANCHOR.md, to check
  the», ««(both referees)» attribution only.» The two reports were committed 5 s apart (16:41:33Z, 16:41:38Z). Neither review imported
  lane code (REFEREE l. 90; REFEREE-2 l. 3).
  Differences, resolved: the corner clause found by both (ANC-1, REQUIRED wording; G-ANC-1, a closed proof-text gap); REFEREE also
  REQUIRED ANC-L2 (the anchor), REFEREE-2 also ANCHOR-L2 (the tie set); κ's freedom found by both at L-1. Both SIGN the same eight items
  with no gap, both rule (R1) covered, and both MATCH L-2. No disagreement in substance.
- TARGET.md diff: «N5 on EVERY game» = every TARGET.md §1 game («A parity game is G = (V, V_E, V_O, E, pr) with V finite»; «every vertex
  has at least one successor (self-loops allowed)»). The line (L-2) makes no M4 claim and no TARGET claim; its tail reads «REDUCTIONS and
  an EQUIVALENCE only (neither FL nor GCH is bounded here;» and «G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim»
  (L-2, by script). REFEREE §7 l. 127 «TARGET.md diff: no bound, no algorithm claim.»; REFEREE-2 §6 l. 139-140
  «This is consistent with TARGET §2 and §4.» Not a claim of TARGET.md §1 or §2 (a reduction of FL-run length to gating changes inside
  N5 runs, an equivalence of their polynomiality, and one refuted constancy statement; no bound on a run or on running time; no
  algorithm claim); not a step-4 pass. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER R102's UPDATE of G-N5-TIME (GAPS at 50ce0e88, last changed by 3ad13dec: the last
UPDATE on l. 11 is R102's, «UPDATE 2026-11-01 10:09Z: RESULTS R102 (P-N5-S4B; CHECKER C113 c5c0ab5f) …», before the row's closing « |»),
built by script (upd103.py: upd100L3.py's build() unchanged; labels searched after the binder; to check (9)) only from the clauses of the
title line L-2: labels behind their clauses; « (2026-11-01) — » → «: »; «G-N5-TIME stays OPEN» and «not M3, not a step-4 pass, not a
TARGET.md claim» dropped from the tail; the source parenthesis kept; «. G-N5-TIME stays open.» at the end. The same script reproduces
R97's to R102's LANDED UPDATEs (GAPS l. 11) byte for byte. L-2 holds no "|"; the UPDATE holds none. Date «2026-11-01» (the landing date;
corrected at landing if later); time and CHECKER commit to be filled at landing:
UPDATE 2026-11-01 <HH:MM>Z: RESULTS R103 (P-N5-ANCHOR; CHECKER C114 <checker>) [refereed-only] LANDED: N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: at a non-fallback transition j − 1 → j, σ_j is a pointwise optimum of the one-player arena in which Even y keeps {σ_(j−1)(y)} ∪ Iσ_(j−1)(y) and Odd follows τ_(j−1)), with RESULTS R24 (a) Lemma R and R24 (b)'s choice rule (TB proof steps 1, 3-5; fixes §2.3) with bridge B, whose proof uses no 𝒞^1O hypothesis (Lead reading L46), applied at every Even vertex that is not its own W′-cycle node, including non-movers ((R1) holds as a consequence of R24 (a) and (b)'s choice rule (both referees)); a tie-break chooses the κ-least FULLY W′-optimal option (κ := the vertex index if x's W′-cycle node c is odd, and the root-first key, i.e. the indices of the play path from c to the option, c excluded, compared lexicographically, if c is even; packet §1), W′ := the arena optimum, where an option is a corner when x occurs on its play before its cycle node (vacuous for fully W′-optimal options)), with: an FL run is a maximal set of consecutive transitions j − 1 → j (j = a + 1, …, b) that are not fallbacks, keep τ, change σ and keep the valuation W of the (σ, τ)-play at every vertex; ℓ(v) := the length component of W(v), CN := {v : ℓ(v) = 0}, T_x := {y ∈ succ(x) : x ⊕ W(y) = W(x)} for Even x ∉ CN, T_c := {y ∈ succ(c) : the cycle node of W(y) is c} for Even c ∈ CN, ℓ* := the largest level of an Even vertex not in CN (1 if none); ODIFF_j := {o Odd : σ̄_j(o) ≠ τ(o)}; the gating data at state j is (σ̄_j, Ξ_j on ODIFF_j, Ξ_j on CN), an epoch is a maximal set of consecutive transitions of the run whose source states carry the same gating data, GCH := the number of states j with a < j ≤ b − 1 at which the gating data changes, CAP := (ℓ* − 1) + Σ_(Even c ∈ CN) (#T_c − 1) ≤ n + m (# = number of elements): for every FL run of every N5 run on every game, σ_j(x) ∈ T_x at every state, σ_(j−1) is a pointwise optimum of the arena at every FL transition j, and every Even h ∉ CN has σ_(j−1)(h) and σ_j(h) fully optimal in that arena (Lemmas FL-TIGHT, FL-OPT, bridge B); for y ∉ CN the Ξ_j-play from y equals the W-play up to the first vertex A of ODIFF_j ∪ CN, its vertices before A other than y have level < ℓ(y), and Ξ_j(y) is a function of that prefix and Ξ_j(A) (Lemma PREFIX); in an epoch with first source state s0, an Even vertex x ∉ CN moves only at transitions j with j − s0 ≤ ℓ(x) − 1, at transitions j ≥ s0 + ℓ* each Even c ∈ CN moves at most #T_c − 1 times in the epoch, the epoch has at most CAP transitions, and the run has at most CAP·(1 + GCH) transitions (Theorem FL-ANCHOR); GCH ≤ b − a − 1 (Lemma CIRC); hence over any family of runs, FL runs are polynomially long if and only if GCH is polynomially bounded (Corollary FL-GCH, an EQUIVALENCE): REDUCTIONS and an EQUIVALENCE only; neither FL nor GCH is bounded here; charging gating changes to moves is circular; «Ξ at ODIFF vertices is constant inside an FL run» DEAD: experiments/new/box133/odxi_n37.pg (83f263c1…) with odxi_n37.start (e2ed6715…), n = 37, 5 Ξ-changes at the ODIFF gate 33 inside FL run [1, 9], one of which releases the FL move 35: 34 → 33 at 5 → 6, and L-RED R179's odxi_min_n12 (51661a75…, 𝒞^1O), odxi_lasso_n13 (5cf18798…), odxi_many_n32 (42094483…, 43 ODIFF Ξ-changes), all checked against Oink 8fbf0a7 --zlk / --tl and L-COMP's n5b (P-N5-ANCHOR, docs/new/P-N5-ANCHOR-box134.md with its fixes entry 1, docs/new/P-N5-ANCHOR-fixes-box134.md; L-NEW successors 45-46). G-N5-TIME stays open.

Addendum 1 (subagent, for the Lead; does not land; written 2026-11-01T22:23:49Z by date -u). (1) BUILT ON LINE L-2 (l-new 709798f3, sha1 1371f900…),
the line both referees MATCH (REFEREE 22 e002db99; REFEREE-2 25 dc7db0e7). NOT committed, NOT pushed; no other tracked file edited. The
lane and referee commits are not on trunk at this fill: merge claude/l-new, claude/referee, claude/referee-2 and push trunk before
landing. (2) TITLE l. 316 = "### R103 [refereed-only] " + L-2 without its newline + ", CHECKER PASS (docs/checker/C114.md, checker
PENDING)", checked by script after the fill (fill103.py): equal, byte for byte (True); the only «### R» heading of this file. (3) BODY l.
316-537; GAPS preamble l. 539-545; UPDATE l. 546 (one line, 0 "|", one <HH:MM>, one <checker>; controls True ×6: R97's-R102's
landed UPDATEs). (4) PINS: from a git archive of 709798f3 (experiments/, docs/new/), from experiments/new, GIT_DIR set: check.sh l. 1-7
+ 700-717 (box 132, box 133, box 134 pins) 22:07:08Z, rc 0, three PASS lines; box133/ and box134/pincheck.sh (Oink 8fbf0a7 --zlk / --tl,
pinwin, n5b, anchor, odxi) 22:07:15-22:07:16Z, rc 0 each, equal to the stored pincheck.txt; DATA re-sum 22:07:31Z, rc 0; re-computation
of all 813 distinct lines 22:09:16-22:10:26Z, rc 0, 813 of 813 equal. (5) QUOTE SWEEP: q103.py (q102.py's rule: outermost guillemet quotes, whitespace joined, split at the ellipsis, parts of 6+ characters; sources: packet at f009a9a1, frozen line, L-1, L-2, fixes at 709798f3, R-N5-ANCHOR.md at e002db99, R2-N5-ANCHOR.md at b431ec81, R2-N5-ANCHOR-L1.md at dc7db0e7, R-R24-L44.md at e002db99, R2-R24-L44.md at d96d2f9e, P-N5-U1-box31.md, RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, TARGET.md, SPEC, NOW, C109, C111, C113, check.sh and both pincheck.txt at 709798f3, my pin / Oink / sample / full outputs, my UPDATE and word diff, commit subjects): to-check notes l. 1-315: 271 quotes, 233 parts, all found; entry (title + body) l. 316-537: 200 quotes, 202 parts, all found, none found only in my own outputs or commit subjects; GAPS preamble and UPDATE l. 539-546: 9 quotes, 7 parts, all found; this Addendum: 9 quotes, 4 parts, all found. Found only in my own outputs (to-check notes only, by design): the UPDATE head, the full re-computation's result line, and box 137's commit subject. Line check: 167 quotes preceded by an l. N, 20 heuristic misses, read by hand: 16 verdict-table cells (the regex takes the packet's or section's line range before the cell's own line number) and four quotes whose l. N names the neighbouring object (L-2's words after the packet's l. 70-74 and l. 85; packet l. 61 after fixes l. 17-18; the index's words after DECISIONS l. 362-367); none a wrong line. Attribution spot check (scratch, 123 (source, line, phrase) triples over the referee files, packet, fixes, L44 files, DECISIONS and P-N5-U1): 121 at the named line; REFEREE's CF-1 sentence is at l. 29, inside the cited range l. 28-29; one triple was my own wrong probe (DECISIONS l. 356, not a citation of the draft). (6) FLAGS FOR CHECKER (no referee made
any REQUIRED): G-1 title shape (no insertion; «with its fixes entry 1»); G-2 unglossed Iσ, Ξ_j, σ̄_j, ⊕, n, m, «level», «FL», x (ANC-P4
and FL-TIGHT), W′ before its «:=», «fixes §2.3», «(R1)»; G-3 «, whose proof» / «; fixes §2.3» against L46's form; G-4 Lead readings
CLEAN; G-5 L41 and R17 (F1) inside TB step 1 (C109 E-1 class; the one I would check first); G-6 L43 CLEAN; G-7 DATA CLEAN; G-8 stale
lane text; G-9 names; soft spots D-1 to D-5. (7) NOT RUN / NOT DONE: the referees' own tools (not re-run); the packet §7 [RULE] DATA
(box 131) and L-RED R177 figures (quoted, not re-run); check.sh's other blocks and scripts/verify.sh (not run); scripts/check_docs.py
(not run, not needed for a draft); the Lead's 19:37Z relay (G-8 (iii)) not found. Scratch files (not committed) are in
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad: R103-template.md, assemble103.py,
fill103.py, upd103.py / upd103.txt / upd103.out, wdiff103.py / wdiff103.out, sum103.py, samp103.py / samp103.out, full103.py /
full103.out, pin103.time / pin103.out (arch7097/experiments/new/pin103.sh), oinkpin103.time / oinkpin103.out, q103.py / q103.out,
r103src/, arch7097/.
