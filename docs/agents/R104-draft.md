# Draft RESULTS R104 (Lead; first fill 2026-11-02T07:14:23Z by date -u (subagent); on REALIZE line L-1, docs/red/P-N5-REALIZE-line-L1.txt, l-red 02dfc35c, sha1 1d72ee310b9b4af252724e06a181221a9c2828ec) — to CHECKER C115
Read at the origin heads fetched at the start of the fill, 2026-11-02 before 07:00Z (l-red 03255d5d, referee 5cc6be95, referee-2 4db41c9d,
checker ec62f84d; origin trunk 40af7329; local trunk head e26f08a6, a Lead commit (NOW, LEAD-STATE) not pushed at the fill, with
RESULTS, GAPS, DECISIONS and DECISIONS-INDEX byte-equal to origin trunk): packet and frozen line (e609c5d2), L-1 and fixes entry 1
(02dfc35c), fixes entry 2 (c28583b3, = the fixes file at 03255d5d); REFEREE successor 22's docs/referee/R-N5-REALIZE.md (report
05b865e0, §C on L-1 5cc6be95); REFEREE-2 successor 26's docs/referee-2/R2-N5-REALIZE.md (report 0188fc66, notebook stamp bcd43b5a;
Addendum 1 a22cf5d8, notebook a2070483) and R2-N5-REALIZE-L1.md (c9eafef4; merge 4db41c9d); C113 and C114 (claude/checker ec62f84d);
RESULTS R15, R24, R36, R57, R67, R102, R103 and the L44 files of R24 (on trunk). Re-runs (scratch, git archive of l-red 03255d5d,
experiments/ and docs/red/, Oink 8fbf0a7 = tools/oink/src HEAD linked in): experiments/red/check.sh l. 1-7 + the «R187 REALIZE» block
l. 710-719 + the «P-N5-REALIZE» block l. 733-746, GIT_DIR set, 07:00:48-07:01:16Z, rc 0; r187/pinck.sh on the four pins and lemck /
realck outputs 07:01:25-07:01:31Z, rc 0 each; the §6 Ξ-cyclic DATA (t2.py CLASS=full) and the two other --rand rows 07:01:47-07:01:48Z.
TRUNK STATUS AT THIS FILL (by script, git merge-base --is-ancestor): e609c5d2, 02dfc35c, c28583b3, 03255d5d, 05b865e0, 5cc6be95,
0188fc66, bcd43b5a, a22cf5d8, a2070483, c9eafef4 and 4db41c9d are NOT on the local trunk (e26f08a6) nor on origin trunk (40af7329); the
Lead merges claude/l-red, claude/referee and claude/referee-2 and pushes trunk before landing. On trunk: L46 (de75072a), its Amendment
(165dda1e), the L44 checks (472f0dcd, d96d2f9e), R103's landing (e89c772e) and the GAPS date fix (92314793). C113 E-2 lesson: the body
names these commits on their branches only and makes NO statement about trunk. C113 E-1 lesson: the title is L-1 verbatim with no
insertion (L-1 carries its own date parenthesis and source note), and the body says exactly that. C114 Add. 1 E-1 lesson: the GAPS
UPDATE head carries «<DATE>», filled with the landing date at landing (G-11). In the body (title + entry), sentences about the frozen line
say «at the frozen line»; every other sentence describes L-1 or the packet as repaired by its fixes.
to check: FLAGS FIRST. G-1 is the title-shape item; G-6 ([VJ-LOC] and RESULTS R36) is the item I would look at first; G-2 the strict
symbol test; G-3 the L46 / bridge B / R103 citation; G-4 the Lead readings as on file; G-5 L41; G-7 DATA vs READING; G-8 L43; G-9 stale
lane text; G-10 names and stale labels; G-11 the UPDATE date placeholder; G-12 TARGET.md priorities. No referee raised any of them as
REQUIRED; I changed nothing in the line. CLEAN items follow.
- FLAG G-1, TITLE SHAPE (note; no Lead insertion; CHECKER / Lead decide). By script over the 24 landed «### R» headings R80-R103: every
  one carries a date parenthesis of the bare form "(YYYY-MM-DD)" before its single ") — "; «revision» occurs in none. L-1 carries its
  date as «(2026-11-02; revision L-1 2026-11-02)» (the only « — » of L-1, by script; fixes l. 56 «Date tag «(2026-11-02; revision L-1
  2026-11-02)».»; REFEREE §C l. 168 and REFEREE-2 L1 table row 8 accept it). The text is true and does not go stale; it is a shape that
  no landed title has. PACKET NAMED: yes, the source note is «(P-N5-REALIZE, docs/red/P-N5-REALIZE.md; L-RED successors 44-45)». FIXES
  FILE NOT NAMED: R96-R101 and R103 name their fixes file in the title (by script, e.g. R103 «(P-N5-ANCHOR, docs/new/P-N5-ANCHOR-box134.md
  with its fixes entry 1, docs/new/P-N5-ANCHOR-fixes-box134.md; L-NEW successors 45-46)»); L-1 does not, although the packet's own
  header says «Where an entry and the frozen packet differ, the entry governs.» (fixes l. 3) and entry 1 changes the packet's reading
  (G-REAL-1, REAL-P1, REAL-P2, REAL-P3). The body names the fixes file and says the entries govern. I inserted nothing: the date and the
  packet are present, and a change to either the date shape or the source note is a line change (an L-2 with both referees' word
  diffs), not a Lead edit, unless the Lead rules an insertion as for R102 (C113 E-1 then requires the body to say so). «L-RED successors
  44-45»: the proof is successor 44's (packet l. 5-6 «docs/red/R187-ladder.md §1» «(l-red 436fe6e9; proof by successor 44)»), the packet
  and both fixes entries successor 45's (git log subjects).
- FLAG G-2, STRICT SYMBOL TEST (the C109 E-2 class; soft, CHECKER decides). Both referees' binder tests pass: REFEREE-2 §6 l. 190-191
  «Binder pass: N, M, lev, s, L(G), n, p are bound; u = K0 and «top» are defined inside the», «game description.»; REFEREE §4 l. 111
  (optional) ««top» is defined only implicitly», taken at L-1. My stricter test ((7) below) finds, NOT glossed in L-1:
  (i) «xt» in «(xt, s(xt))» and in «x → xt(x, k)»: the line says «a Ξ-target that is a mover or X» but never names it xt (packet §2 l.
      55 «a Ξ-target xt(x, k) ∈ {movers} ∪ {X}»); the referent is unambiguous.
  (ii) «X» is used as a value («a mover or X», «up to the first Ξ-target X», «u when the target is X») and never described (packet: the
      exit to the core u).
  (iii) «u» is used («with edges to the Ξ-target and to u, or to u alone») before «a closed core u = K0» in the same parenthesis (the
      R103 «W′» class, C114 G-2: «W′ is used before its «:=» in the same parenthesis.»).
  (iv) «Iσ(y)», «σ̄», «τ̄» and «σ_new» in the 1E-N3 gloss: Iσ is unglossed (12 landed titles use it, R87-R103; C114 G-2 accepted it);
      σ̄ occurs in 24 landed titles; τ̄ in 2 (R85, R89); σ_new in 3 (R91, R93, R95) (by script). «σ̄» is inside R57 (b)'s quoted words.
  (v) «the root-first key comparison»: L-1 does not state the tie-break that the cited «R24 (b)'s choice rule» uses (R103's title does:
      «the root-first key, i.e. the indices of the play path from c to the option, c excluded, compared lexicographically»); packet §1
      l. 44-46 states κ_j. The line names the comparison only to say that it depends on the vertex indices.
  (vi) «deg(x)» in «M := Σ deg(x) options (x, k)» (= the number of options of x; packet l. 53 «options k = 0, …, deg(x) − 1»).
  (vii) «bridge B» (G-3).
  (viii) «e of even priority above every β»: the exact e-priorities (packet l. 88-89, by (lev, gate index)) are not in the line; both
      referees say only «even and above every β» is used: REFEREE §2 l. 77-78 «(e's» «PRIORITY order by (lev, gate index) is not used by any
      lemma; only «even and above every β» is.)»; REFEREE-2 §4 l. 132-133 «My MUT=eprio control (random even e-priorities above every β,
      repeats» «allowed): 0 violations.» The β-vertices' own index order is left to «(packet §3.1)»: REFEREE-2 L1 l. 50 «The β-vertices'
      own order is left to «(packet §3.1)». I checked that it is immaterial» (MUT=border, 0 violations).
  (ix) «super-polynomial» / «super-polynomially long»: first landed title with the word (0 of R1-R103, by script); its meaning is the
      negation of the stated «at most p(n) for a nondecreasing polynomial p»; REFEREE-2 §4 l. 145 «(b): N + M ≤ n ≤ 3(N + M) + 6, so
      «super-polynomial in N + M» transfers to n. ✓». The line does not say in which size the FL runs are super-polynomially long (n).
  (x) «the 7 R178 champions», «2 R188 genomes» (G-10).
  None is a claim clause's quantifier; every claim clause's own variables (G, s, x, k, N, M, L(G), n, p) are bound.
- FLAG G-3, THE L46 CITATION, «bridge B» AND RESULTS R103 (note). L-1: «with RESULTS R24 (a) Lemma R and R24 (b)'s choice rule (TB proof
  steps 1, 3-5; fixes §2.3) with bridge B, whose proof uses no 𝒞^1O hypothesis (Lead reading L46 and its amendment)». This is R103's
  landed citing line word for word plus «and its amendment» (by script; packet l. 40-42 «Citing line, verbatim as in» «RESULTS R103»;
  REFEREE-2 table l. 37 «citing line verbatim = RESULTS R103's.»). C114 G-3 PASSED that form for R103 («; fixes §2.3», «, whose proof»).
  Three notes: (a) «bridge B» is R103's landed lemma (RESULTS R103 title «(Lemmas FL-TIGHT, FL-OPT, bridge B)»), but L-1 never names
  «R103» (by script: 0 times), and «bridge B» occurs in no other landed title. (b) In THIS packet bridge B is not used: Lemma W (iii)
  gives its conclusion for every arena option (packet l. 47-49; fixes l. 16-22, REFEREE REAL-P1: «the bridge-B part of the citation is
  redundant here; the citation of RESULTS R24 (a) Lemma R and R24 (b)'s choice rule (TB proof steps 1, 3-5) is» «ESSENTIAL»). L46 asks
  that «bridge B (flat + non-corner ⇒ the old option is fully optimal) is» «signed in the citing packet»; REFEREE-2 table l. 37: «Bridge
  B's conclusion is Lemma W (iii), signed here, which is what L46 asks of a citing packet». (c) The packet's [RULE] also takes from
  R103 the (R1) ruling («Non-movers are covered ((R1) ruled «covered», RESULTS R103).», packet l. 46), which REALIZE's mover step uses at
  movers that keep their option; L-1 does not state the rule's domain («every Even x that is not its own W′-cycle node», packet l.
  42; R103's title «applied at every Even vertex that is not its own W′-cycle node, including non-movers») and does not cite R103.
  Neither referee asked for R103 in the line; REFEREE-2 opened it (§0 l. 17 «R103 (citing line, (R1), FL definition, bridge B)»). A
  change is an L-2. L44's rule «the entry quotes both confirmations» is met in the body (Premises), from the two L44 files.
- FLAG G-4, LEAD READINGS AS ON FILE (the C111 E-1 class; my check). RESULT: CLEAN, with one note.
  L45 (DECISIONS l. 383-390; index l. 38 «active»): L-1's «read on every valid input of S1's procedure (Lead reading L45, RESULTS R102)»
  matches L45's «L42 stays in force for any premise other than S1's procedure on a valid input.» and R102's landed title «read on every
  game input of S1's procedure (Lead reading L45, lifting L42's S4b restriction)». The quoted R57 (b) words are verbatim RESULTS l.
  2915-2916 (and R102's title).
  L42 (l. 362-367; index «active (S4b part lifted by L45)»): L42 names S4a as «σ_(k+1) is the pointwise optimum of H_k»; L-1's second form
  is «S4a's σ_new, S1's output on the dual of the one-player arena …, is a pointwise optimum of that arena, before S4c». NOTE: the
  «before S4c» reading (σ_new at a transition that may turn out to be a fallback; REFEREE-2 G-REAL-1 (b)) is not L42's words; it is
  covered by L45's «S1's procedure on a valid input» (dual(H) is a game graph with a successor at every vertex) and by R102's statement
  «for every finite game graph G* … the Odd strategy that S1's procedure outputs for σ* on G* is a pointwise optimum against σ* in G*»
  read on dual(H) (REFEREE-2 §2 l. 60-63). The two-forms precedent is landed: R67 (RESULTS l. 3461-3463) «the standing SPEC premise
  1E-N3 (RESULTS R57) in two forms (N-RUND-1,» «REFEREE-2; accepted by REFEREE): P1, S1's σ̄_k is Odd's pointwise optimum in G_{σ_k}».
  L46 + Amendment (l. 392-406; index «active»): L-1 cites (a) and (b) only (by script: «R24 (c)», «(d)», «(e)» 0 times); «and its
  amendment» names the Amendment (corner wording), which the packet uses («an option» «being a corner (outside the rule) when x occurs
  on its play BEFORE that play's cycle node», packet l. 43-44); Lemma W (iii) makes it vacuous here («none is» «a corner», l. 180-181).
  L44 (l. 376-381): through L46; both confirmations quoted in the body. L41, L43: G-5, G-8.
- FLAG G-5, L41 (the C109 E-1 class; CHECKER decides). L-1 contains «referee-originated» 0 and «lane-authored» 0 times (R102's title has
  «lane-authored (L-SI; not referee-originated)»). The proofs are L-RED's (successor 44, R187 §1; successor 45, the packet). Both
  referees: REFEREE l. 4 «L41 (lane-authored; nothing referee-originated)», §4 l. 111-112 «the line has no «lane-authored» label» «(L41
  needs none here, since nothing is referee-originated).»; REFEREE-2 table l. 34 «No new proof; L41 not triggered», §6 l. 191 «L41:
  nothing referee-originated.» THREE POINTS TO CHECK: (a) G-REAL-1 (REFEREE-2 §2) is closed by landed items (R57 (b) under L45 / R102;
  R103's (R1) ruling), «a second time directly from SPEC S1's text (§3 below)» (table l. 34). REFEREE-2 §3 («A direct reading of S4a in
  the standard state (my check of REALIZE's σ-step; no premise)», l. 72) is a referee-written argument; the fixes record it as an
  alternative («REFEREE-2 §3 also closes (b) directly from SPEC S4a's text; no change to any lemma.», fixes l. 44) and REFEREE-2 L1 l.
  70 «my §3 direct trace is an alternative at standard states, not needed». The entry does not rest on it (my reading). (b) REAL-P3
  (finiteness of L(G)): the packet's own argument (l. 76-77 «finite: it is an FL run of a real N5 run by» «Theorem REALIZE, and N5
  terminates, RESULTS R15») gains REFEREE's non-circularity clause in fixes l. 26-28; REFEREE-2 made the same remark independently (§4
  l. 139). A clarifying clause, not a proof step (my reading). (c) R17 (F1) inside «TB proof steps 1, 3-5»: the same citation as R103;
  C114 §4 ruled G-5 for R103 NOT REQUIRED («The cited steps do not need (F1) for the choice form.»); here bridge B is not used at all
  (G-3 (b)), so TB step 2 and (F1) are a fortiori outside the proof.
- FLAG G-6, [VJ-LOC] AND RESULTS R36 (the item I would look at first; my reading, raised by no referee). L-1 cites «VJ00 local
  optimality (BRICS RS-00-48 Lemma 5.8 «1 ⇒ 2», the direction that holds, applied to Odd's one-player game against a fixed σ)». In
  RESULTS this lemma's status is: R15 (iii) (l. 649-650) «G-N5T-3 (outside the packet): N5's output correctness at S5 rests on VJ00
  Lemma 5.8 "1 ⇒ 2", which uses VJ00's» «unproved Lemma 5.9 and Prop. 5.10; not re-derived by either referee»; R36 (c) Lemma P1 (l.
  1730-1732) proves it on ONE-PLAYER games («if σ is a positional Even strategy of a one-player game H with no improving edge»), and R36
  (d) / Reading (l. 1734-1738) «P1 discharges (P) for one-player games only. It does NOT discharge the two-player VJ00» «Lemma 5.8 (R15's
  G-N5T-3).» The packet applies the lemma on G^d to Γ_σ, «where Odd is the only player» (l. 37-38): a one-player game of G^d (R36's
  «A ONE-PLAYER game» «is a game in which every non-Even vertex has one successor», l. 1723-1724, with G^d's owners). So the use is
  covered by the landed R36 (c), plus 1E-N3's P1 form for «φ_(σ,ρ) = Ξσ» (REFEREE-2 G-REAL-1 (a)). Both referees instead rest it on L-LIT
  T21 (c) («Unaffected: a stop with no improvement is optimal: BRICS Lemma 5.8 "1 ⇒ 2"», REFEREE l. 8, REFEREE-2 l. 18-19), which
  concerns the I1 / I2 failures, not 5.8's dependence on 5.9 / 5.10. Neither cites R36 or G-N5T-3 (by script: «R36» 0, «G-N5T-3» 0 in
  both reports). The line's «the direction that holds» is true for the one-player use; whether the line should name RESULTS R36 (c)
  (an L-2) or the body's premise note suffices is for CHECKER. The body states the R36 route as my reading, not as a referee statement.
- FLAG G-7, DATA vs READING (the C108 E-1 class). CLEAN, with one note. L-1's DATA clause is labelled («DATA: per-lemma checks …»),
  every number in it is reproduced (REFEREE-2 §6 l. 202-203 «Every number is reproduced»; my re-runs, (10)). NOTE: «random Ξ-cyclic
  genomes do mismatch» stands in the scope words BEFORE the «DATA:» label; it is packet §6's DATA (l. 235-236 «seed 187 d 3:» «14 / 30
  equal (16 mismatches); seed 188 d 4: 20 mismatches of 30»), an existential statement about finitely many seeded instances, reproduced
  by REFEREE-2 (l. 178 «σ̄ ≠ β at some gate already at state 0 in 134», of 294) and by me. Packet §7's «every IDEAL-ACYC run found is
  LINEAR in N» (l. 265) and §8 are READING, NOT in L-1 (by script: «linear» 0, «LINEAR» 0); REFEREE-2 N-2 (l. 207-209) flags «LINEAR»
  as an asymptotic word on 7 genomes, which costs nothing while it stays out of the line.
- FLAG G-8, L43 (DEADs). CLEAN. L-1 has no DEAD (by script: «DEAD» 0, «O(» 0, «linear» 0). «polynomial» occurs 3 times, all inside the
  Corollary's own hypotheses and conclusion. REFEREE §4 l. 119 «No DEAD (L43 ✓).»; REFEREE-2 §6 l. 191 «L43: no DEAD clause.»
- FLAG G-9, STALE LANE TEXT (notes; nothing here lands). (i) fixes entry 2 l. 59-60 «(as» «relayed by the Lead 05:31Z)» while c28583b3
  (entry 2) is 05:28:56Z; the Lead's message is not in the repository (not verified). (ii) Neither referee read entry 2: REFEREE §C l.
  153-154 «The fixes file is» «docs/red/P-N5-REALIZE-fixes.md (sha1 864cad59…), entry 1.» (5cc6be95, 05:57Z); REFEREE-2 L1 l. 11 (the
  fixes row «864cad5978cb79f7c73c6ba99cff8202fe34cc5b») and §3 «Fixes entry 1 (864cad59)» (c9eafef4, 05:58Z). Entry 2 changes nothing:
  it records REFEREE-2 Addendum 1 and says «Line L-1 (1d72ee31) already carries it;» «no further line change.» (l. 62-63). (iii) Packet
  l. 33 «(RESULTS R57; R102 S4B-OPT under Lead reading L45)», l. 47-49 and l. 277-278 (bridge B «is not needed in the proof»), l. 204-205 «[0, L] is ONE FL run» and
  l. 76-77 are superseded by fixes entry 1 (G-REAL-1, REAL-P1, REAL-P2, REAL-P3). The body quotes the superseded text only as history.
  (iv) Packet l. 2 «Frozen 2026-11-02 (date -u: see the commit)»: the freeze commit is e609c5d2, 2026-11-02T02:46:02Z.
- FLAG G-10, NAMES AND STALE LABELS (by script on RESULTS f24f7046 / GAPS 5fdcfb9e). (a) «R104» occurs 2 times in RESULTS, both as
  «L-RED's R104 (docs/red/R104-counting-gate.md» (l. 5012-5013, inside R84's body), a lane box label; after landing «R104» names
  both. (b) L-1's DATA clause writes «the 7 R178 champions» and «2 R188 genomes» without «L-RED» (the line's first mention is «L-RED
  R178 §1»); RESULTS has no R178 / R188, so a reader can mistake them for RESULTS labels (landed precedent prefixes lane boxes: «L-RED
  R143» in R96, «L-RED R179» in R103). (c) 0 times in RESULTS and GAPS: «P-N5-REALIZE», «REALIZE», «REAL-IDEAL», «IDEAL», «Fact DUAL»,
  «Fact X», «SBAR», «Lemma TAU», «Lemma ESC», «Lemma KEY», «VJ-LOC», «genome». Same names, other meanings (body only; L-1 names only
  Theorem REALIZE and Corollary REAL-IDEAL): «Lemma K» (Dead ends, l. 9988), «Lemma W» (R5, G-R5-7), «Lemma PLAY-CAUSE» (R96, R97) as
  a superstring of «Lemma PLAY». (d) RESULTS labels in L-1 (by script): R57 (2), R102 (1), R24 (2); none retired by a later entry.
- FLAG G-11, THE UPDATE DATE (C114 Add. 1 E-1). The UPDATE head is «UPDATE <DATE> <HH:MM>Z: RESULTS R104 (P-N5-REALIZE; CHECKER C115
  <checker>) [refereed-only] »: <DATE> is the landing date, <HH:MM> and <checker> are filled at landing. PRECEDENT HARDCODED THE DATE:
  R103-draft l. 546 «UPDATE 2026-11-01 <HH:MM>Z: RESULTS R103» (landed 2026-11-02, so GAPS needed 92314793; C114 Add. 1 «Move: in GAPS l.
  11, «UPDATE 2026-11-01 00:24Z: RESULTS R103» → «UPDATE 2026-11-02 00:24Z: RESULTS R103».»); R102-draft l. 455 «UPDATE 2026-11-01
  <HH:MM>Z: RESULTS R102» (landed the same day, so correct). The controls below fill the landed values.
- FLAG G-12, TARGET.md PRIORITIES (note). Γ(G)'s priorities reach 4M + 9 (packet l. 222 «every» «Ω ≤ 4M + 9»), which can exceed n = N
  + 3M + 6; TARGET.md l. 7 «pr : V → {0, 1, ..., n}» with l. 10 «Games with arbitrary natural priorities are first compressed to {0..n}
  by sorting, preserving order and parity». Compression keeps the rank order, the parities and the indices, so the N5 run is the same
  (my reading); the corollary's size bound is in n and in N + M, not in the priority range. No referee raised it.
- CLEAN AT L-1 (the pre-check against CHECKER's recurring items, by script on 1d72ee31):
  C106 E-1 (old line as current): the title is L-1; the frozen line occurs in the body only in history sentences.
  C113 E-1 (title «verbatim» after an insertion): no insertion; the body says «verbatim» and the title is byte-equal to prefix + L-1 + fill.
  C113 E-2 (trunk status that goes stale): the body has no trunk statement (header).
  C114 Add. 1 E-1 (UPDATE date): <DATE> placeholder (G-11).
  C110 F-1 (stale pins vs landed labels): the four pins L-1 names by sha1 prefix have the pinned full sha1 at e609c5d2 and at 03255d5d
  (by script, (10)); check.sh pins the packet, the frozen line and L-1 by sha1 (l. 734-737).
  C111 E-1 (stale Lead-reading statements): G-4.
  The premises are landed labels (R57; R102; R24 (a), (b); R103 through the citing line) and Lead readings on file (L45, L46); no
  unlanded result is a premise; L-RED R178 (the IDEAL model) is restated in the line and in packet §2.
- Soft spots, no referee raised them as REQUIRED (details in (11)): D-1 packet §7 says the check.sh block runs «the pins»; the
  «P-N5-REALIZE» block runs the two R188 pins, the two stab pins run in the «R187 REALIZE» block; D-2 REFEREE did not check the mover
  states against IDEAL nor re-run Oink / n5b (l. 135-136); D-3 the §7 random rows: check.sh runs --rand 20 4 187 only; D-4 REFEREE-2's
  boundary probes (L = 0 in 428 genomes) and the fixes' REAL-P2 case.
(0) PLACEMENT. R104 goes DIRECTLY AFTER R103 and BEFORE «**Erratum E-1**». docs/RESULTS.md at origin trunk 40af7329 (= local trunk
e26f08a6) has sha1 f24f70464d0100f20b2ebdcfa0b60a78d6909d37, 10,397 lines, last changed by e89c772e (R103's landing). «### R103» is l.
9641 (entry l. 9641-9862, l. 9863 blank); «**Erratum E-1**» is l. 9864; «## Dead ends (kept;» is l. 9877. PROPOSED (R102's and R103's
layout, C113 §7, C114 §7): insert R104's entry after l. 9863 (R103's blank line) and before «**Erratum E-1**», with one blank line after
it, so the R-entries stay contiguous and the erratum closes the Results section. The erratum's line references (l. 7963-9195) lie
before the insertion and do not move. "### R104" occurs 0 times in RESULTS and GAPS («R104» 2 times in RESULTS as L-RED's box label,
G-10); GAPS has sha1 5fdcfb9ef3b32bf7dcda1ca7c3e77aed78fe8bf0, 23 lines, last changed by 92314793. The Lead re-checks (6) and (9) at
landing only if RESULTS or GAPS change after f24f7046 / 5fdcfb9e.
(1) TITLE. The title is the line file docs/red/P-N5-REALIZE-line-L1.txt (l-red 02dfc35cb9804d171b1db809d4bd79713255b8ec,
2026-11-02T05:04:18Z, the file's only commit, sha1 1d72ee310b9b4af252724e06a181221a9c2828ec; identical at c28583b3 and at 03255d5d),
verbatim: one line, no outer quotes, no final period, 4,478 characters (4,578 bytes plus the newline), 835 whitespace tokens, 57 / 57
parentheses (depth never negative), two «…» pairs. NO HEADING MARKER, verified by script: the file begins «N5 (SPEC S1-S5 from a GIVEN
start pair», with no «#» at its start, no "R??" and no lane tag (L41 «Lanes write line files without a heading marker»). NOTHING is
stripped and NOTHING is inserted: the heading is the level-3 marker, then "R104 [refereed-only] ", then the file without its newline,
then the fill ", CHECKER PASS (docs/checker/C115.md, checker PENDING)" (as R90-R103, no space before the comma). L-1 holds one « — »,
its own date parenthesis «(2026-11-02; revision L-1 2026-11-02)» and no "|" (G-1). Built by script (scratch fill104.py: assert the sha1
1d72ee31…, equality with the blob at 02dfc35c and at 03255d5d, one line, no marker, one « (2026-11-02; revision L-1 2026-11-02) — », no
"|"; prepend, append) and re-checked after writing this file: equal, byte for byte. Heading: 4,557 characters, 4,657 bytes; sha1 of the
heading line without its newline f9064150cd23cb7d1336e602230ef962232266e1; it is l. 359.
(2) LINE HISTORY: the frozen line docs/red/P-N5-REALIZE-line.txt (sha1 53dd6e9fd727a6ff2d5e49648366f28d7398e9d9, committed with the
packet in e609c5d2, 2026-11-02T02:46:02Z; 3,742 characters, 698 tokens; the line both reports reviewed) → L-1 1d72ee31 (02dfc35c,
05:04:18Z; 4,478 characters, 835 tokens; fixes entry 1). Each line file has one commit. Word diff measured (difflib over whitespace
tokens, scratch wdiff104.py): 14 non-equal opcodes, 675 tokens in common, i.e. six changes: (1) the 1E-N3 gloss «at a non-fallback
transition j − 1 → j, σ_j is a pointwise optimum of the one-player arena in which Even y keeps {σ_(j−1)(y)} ∪ Iσ_(j−1)(y) and Odd
follows τ_(j−1)» → R57 (b)'s words, «read on every valid input of S1's procedure (Lead reading L45, RESULTS R102), used in two forms»
(REFEREE-2 REAL-L1); (2) «compared by the β of largest rank in the symmetric difference and its parity;» → «… symmetric difference:
the option whose set contains that β is the better one if its parity is even and the worse one if odd;» (REFEREE-2 REAL-L2); (3) «top»
defined and the vertex-index layout added (REFEREE REAL-L1 and REFEREE's optional «top»); (4) «β → its Ξ-target (u when the target is
X)» (REFEREE-2 P-1); (5) «so, if L(G) ≥ 1, [0, L(G)]» and «(no FL run if L(G) = 0)» (REAL-P2, both); (6) the date tag «(2026-11-02;
revision L-1 2026-11-02)». = fixes l. 50-56 (six items); = REFEREE §C l. 156 «Exactly the six listed changes. Nothing else changed:»;
= REFEREE-2 L1 l. 22-35 (eight rows = the six items, «its items 1 to 6 are my rows 1, 2, 3+4, 5, 6+7 and 8.»), l. 20-21 «Byte test:
start from the frozen line, apply exactly the 8 replacements below, each of whose old phrases occurs exactly once,» «and compare with
L-1: **True**.»
No inequality of a signed statement differs between the frozen line and L-1: the changes re-cite the premise in both forms, state the
order's direction and the index layout that Lemma KEY uses, define «top», make the start and the L(G) = 0 case explicit, and tag the
date.
(3) THE LINE AT BOTH REFEREES. L-1 (the title): REFEREE successor 22, docs/referee/R-N5-REALIZE.md «## §C (2026-11-02T05:57Z by date -u,
successor 22; Opus 5.5, D15): word-diff of line L-1» l. 152-172 (5cc6be95, 05:57:19Z, +22): l. 163 «**My REAL-L1: met.**», l. 172
«Verdict: line L-1 **MATCHES**.» REFEREE-2 successor 26, docs/referee-2/R2-N5-REALIZE-L1.md (c9eafef4, 05:58:52Z, new file, 85 lines):
l. 2 «Verdict: **MATCHES**.», l. 77 «**MATCHES.** L-1 (1d72ee31) differs from the frozen line (53dd6e9f) by exactly the six listed
items. The three REQUIRED items are met.», l. 78 «My signatures in R2-N5-REALIZE.md stand for the packet read with fixes entry 1.»
Frozen line: REFEREE l. 26 «**REQUIRED REAL-L1** (the e-index order is missing from the line's Γ(G))»; REFEREE-2 table l. 40
«**REQUIRED**: REAL-L1 (1E-N3 gloss), REAL-L2 (parity direction of the IDEAL order). Precision P-1, P-2». REFEREE-2 Addendum 1
(a22cf5d8) l. 228 «**REFEREE REAL-L1 (e-index order missing from the line): I AGREE, REQUIRED. I missed it.**», with a failing instance
(l. 229-234: MUT=eorder, «KEYB 33, IDEAL 20 on big_d4_k3_W3 and grow_top_N24, first at state 0, mover x = 2»), and l. 247 «**Joint line
list:** REFEREE REAL-L1 (e-index order) + my REAL-L1 (1E-N3 gloss) + my REAL-L2 (parity direction)». REFEREE did not comment on
REFEREE-2's two REAL items before §C; its §C checks them as met (l. 157-162). Both MATCH L-1.
LINE-ITEM NAMES: both referees used «REAL-L1» for different items (fixes l. 7 «Both used the label «REAL-L1»; here they are named by
referee.»). REFEREE REAL-L1 (REQUIRED, e-index order), REAL-P1, REAL-P2, REAL-P3 (optional), «top» (optional); REFEREE-2 G-REAL-1
(minor, closed), REAL-L1 (REQUIRED, 1E-N3 gloss), REAL-L2 (REQUIRED, parity direction), P-1, P-2 (optional), N-1, N-2, N-3 (notes).
All REQUIRED items and P-1, P-2, REAL-P2, «top» are in L-1; REAL-P1, REAL-P3 and G-REAL-1 are packet readings in fixes entry 1.
(4) CLAIMS SIGNED = the items below, each SIGNED in BOTH referees' verdict tables (REFEREE "## 0. Verdicts" l. 10-26 of R-N5-REALIZE.md;
REFEREE-2 "## 1. Verdict table" l. 22-40 of R2-N5-REALIZE.md), checked clause by clause against the packet:
| item (packet §, lines) | REFEREE (successor 22) | REFEREE-2 (successor 26) |
| --- | --- | --- |
| (a) Fact DUAL (§1, l. 25-28) | l. 13 «**SIGNED**»; §1 l. 31-33 | l. 25 «**SIGNED**»; §4 l. 91-97 |
| (b) Fact X (§2, l. 66-70) | l. 14 «**SIGNED**»; §1 l. 34-36 | l. 26 «**SIGNED**»; §4 l. 98-102 |
| (c) Lemma K (a)-(d) (§3.2, l. 101-117) | l. 15 «**SIGNED**»; §2 l. 43-47 | l. 27 «**SIGNED** ((c) uses P1 on G^d, see G-REAL-1 (a))»; §4 l. 103-108 |
| (d) Lemma PLAY (a)-(c) (§3.3, l. 119-131) | l. 16 «**SIGNED**»; §2 l. 48-51 | l. 28 «**SIGNED**»; §4 l. 109-112 |
| (e) Lemma SBAR (§3.4, l. 133-149) | l. 17 «**SIGNED** ([VJ-LOC] used only in the «1 ⇒ 2» direction ✓)»; §2 l. 52-59 | l. 29 «**SIGNED**, with G-REAL-1 (a) (P1 used, not named in §1; covered by the landed 1E-N3)»; §4 l. 113-116 |
| (f) Lemma TAU (§3.5, l. 151-160) | l. 18 «**SIGNED**»; §2 l. 60-62 | l. 30 «**SIGNED** (P1 on G^d, G-REAL-1 (a)); its proof uses no acyclicity»; §4 l. 117-120 |
| (g) Lemma ESC (§3.6, l. 162-171) | l. 19 «**SIGNED**»; §2 l. 63-66 | l. 31 «**SIGNED**»; §4 l. 121-122 |
| (h) Lemma W (i)-(iii) (§3.7, l. 173-184) | l. 20 «**SIGNED**»; §2 l. 67-71 | l. 32 «**SIGNED**»; §4 l. 123-126 |
| (i) Lemma KEY (a), (b) (§3.8, l. 186-200) | l. 21 «**SIGNED** (KEY (b) needs the e-index layout; see REAL-L1)»; §2 l. 72-78 | l. 33 «**SIGNED**»; §4 l. 127-133 |
| (j) Theorem REALIZE (§4, l. 202-218; fixes l. 23-28) | l. 22 «**SIGNED** (the IDEAL stop is an S4c fallback ✓; precisions REAL-P2, REAL-P3)»; §3 l. 81-90 | l. 34 «**SIGNED**, with G-REAL-1 (b)» (closed, «No new proof; L41 not triggered»); §2 l. 55-65, §3 l. 72-88, §4 l. 134-140 |
| (k) Corollary REAL-IDEAL (a), (b) (§5, l. 220-229) | l. 23 «**SIGNED**»; §3 l. 91-95 | l. 35 «**SIGNED**»; §4 l. 141-146 |
Both, verbatim: REFEREE l. 28 «No gap in the mathematics.», FINDINGS l. 143-144 «Every to-sign item is SIGNED, with no gap: Facts DUAL
and X, Lemmas K, PLAY, SBAR, TAU, ESC, W, KEY, Theorem REALIZE (the IDEAL» «stop is an S4c fallback) and Corollary REAL-IDEAL (a),
(b).»; REFEREE-2 l. 42 «Joint gap map on my side: G-REAL-1, minor, a proof-text / premise-statement gap, CLOSED by landed items. Nothing
is open on the signed items.», Addendum 1 l. 227 «Verdicts agree: every to-sign item SIGNED by both; no gap in the mathematics.» The
packet's to-sign list (l. 7) names §3's seven lemmas, §4 and §5; Facts DUAL and X (§1, §2, «used in Lemma TAU», «used in Lemma KEY»)
are not in it, and both referees signed them in their tables (rows (a), (b)). Also checked by both, NOT signed items: [VJ-LOC] used
only as «1 ⇒ 2» (REFEREE l. 17, REFEREE-2 l. 36); [RULE] (REFEREE l. 24, REFEREE-2 l. 37); §6 scope, §7 DATA (REFEREE l. 25,
REFEREE-2 l. 38-39).
Clause checks (L-1 against the packet): the genome clause = §2 l. 52-58 with «a distinct β-rank with a parity» for the bijection br and
bp, «a distinct gate index» for gate; the Ξ-value and its order = §2 l. 61-70 (Fact X, with the direction of REAL-L2); the IDEAL step =
l. 71-76 («among its current option and the options with a strictly better Ξ-value» = A_s(x); «the run stops when nothing is available
or nothing changes» = «opt» / «stuck»); the Ξ-graph = l. 59-60 (with «ACYCLIC» = IDEAL-ACYC); Γ(G) = §3.1 l. 83-95 with e-priorities
reduced to «even … above every β» (G-2 (viii)), the start = l. 96-97; Theorem REALIZE = §4 l. 203-205 with fixes REAL-P2 (l. 23-25),
where «Odd's optimal counterstrategy on the β-face at every gate» = SBAR (without σ̄(K2) = K1), «τ unchanged (no Odd-improving edge)»
= TAU, «σ unchanged off the movers» = ESC, «the valuation … unchanged at every vertex» = W (i); Corollary REAL-IDEAL = §5 (a) with
«p(3(N + M) + 6)» = q(N + M), q(t) := p(3t + 6), and (b) «from the stated start pairs». Nothing in L-1 is wider than signed.
Signed by both, NOT stated by L-1 as separate items, so landed only as the proof's lemmas named in the body: Facts DUAL, X; Lemmas K,
PLAY, SBAR, TAU, ESC, W, KEY (their conclusions SBAR, TAU, ESC, W (i) appear inside REALIZE's clause); the size bounds of §5 («every Ω ≤
4M + 9», «6M + 10 edges»). Not signed, so NOT landed: §7 DATA (DATA clause only), §8 READING.
(5) OTHER TEXTS THE ENTRY DEPENDS ON: the premises RESULTS R57 (1E-N3, both forms, read on every valid input by L45, as R102 reads it),
R24 (a) Lemma R and R24 (b)'s TB proof (packet P-N5-U1, docs/new/P-N5-U1-box31.md §2, fixes §2.3) read class-free by L46 under L44
with both L44 checks (R-R24-L44.md 472f0dcd + Addendum 1 at 732198a9; R2-R24-L44.md d96d2f9e), R103 (the citing line, bridge B, (R1)),
VJ00 Lemma 5.8 «1 ⇒ 2» on a one-player game (R36 (c), G-6), R15 (termination, for L(G)'s finiteness); SPEC S1-S5
(docs/new/N5-ssi-global.md). No lane packet is a premise. The IDEAL model is L-RED R178 §1 (docs/red/R178-ideal.md, l-red e03b15a6),
restated in packet §2 («this packet restates everything it uses and governs where they differ», l. 5). Instance sources: L-RED R187
(stab pins, r187/stab.py) and R188 (x3_L8, g4_L12). History only: docs/red/R187-ladder.md §1 (l-red 436fe6e9), R178-ideal.md §1,
R188-xicounter.md.
(6) PREMISE LABELS (stale-label test; RESULTS at f24f7046, GAPS at 5fdcfb9e). RESULTS labels in L-1 (by script): «R57» 2 («RESULTS R57
(1E-N3», «RESULTS R57 (b)»), «R102» 1, «R24» 2 («R24 (a) Lemma R», «R24 (b)'s choice rule»); «R178» 2 and «R188» 1 are L-RED box
labels (G-10). Each RESULTS label exists and carries the named item:
- R57 (l. 2893): (b) l. 2915-2916 «that S1's procedure realises an optimal σ̄ is VJ00 §6» «plus SPEC conformance, and the code's match to
  SPEC is DATA (R15 G-N5T-1) (1E-N3 = N-1E-1).» The two-forms reading is landed in R67 (l. 3461-3463) and in R102's statement.
- R102 (l. 9478): its title «read on every game input of S1's procedure (Lead reading L45, lifting L42's S4b restriction): for every
  finite game graph G* with G's priorities and a successor at every vertex and every Even strategy σ* of G*, the Odd strategy that S1's
  procedure outputs for σ* on G* is a pointwise optimum against σ* in G*». L-1 cites it for the reading only; S4B-OPT itself is not used
  (REFEREE l. 39 «S4b is never run (Iτ = ∅), so R102 / L45 is not needed.»: REFEREE reads 1E-N3 as covering S1's σ̄ directly).
- R24 (l. 1064): (a) Lemma R l. 1073-1077; (b) Lemma TB l. 1078-1081 («Tie-breaks equal SPEC S1 (iv) / FIX 4 exactly»). The class word
  is in the heading and Setting only; L46 reads (a), (b) class-free; (c)-(e) are not cited.
- Not in L-1 but used through it: R103 (l. 9641; G-3), R36 (l. 1717; G-6), R15 (l. 624; termination).
- Lead readings: L45, L46 with its Amendment, L44 (inside L46), L42 (S4a part); L41, L43 as rules. All «active» in the index (l. 34-39).
- G-N5-TIME open (GAPS l. 11). No label is retired by a later entry.
(7) SYMBOL TEST of the title (my own strict test of every symbol of L-1, by hand; IN = bound in the line; else the carrier):
| symbol | where |
| --- | --- |
| N5, SPEC S1-S5, S4a, S4c, S3, Even, Odd | SPEC (named) |
| R57 (b), 1E-N3, L45, R102; R24 (a) Lemma R, R24 (b) choice rule, TB, «fixes §2.3»; L46 and its amendment | cited (G-3, G-4) |
| bridge B | cited, source not named (G-3) |
| VJ00, BRICS RS-00-48 Lemma 5.8 «1 ⇒ 2» | literature (G-6) |
| σ̄, τ̄, σ_new, Iσ(y), σ, τ, y (1E-N3 gloss) | SPEC names, not glossed (G-2 (iv)); y IN |
| L-RED R178 §1, IDEAL model, IDEAL genome G | IN (the genome clause) |
| N, x, lev(x), M, (x, k), W-target, Ξ-target, β-rank, parity, gate index, start | IN |
| deg(x) | not glossed (G-2 (vi)) |
| s, Ξ-value, chain, β | IN |
| xt, X | not glossed (G-2 (i), (ii)) |
| key, IDEAL step, L(G), Ξ-graph, ACYCLIC | IN |
| Γ(G), n, gates, W-face e, Ξ-face β, c_W, top, K0-K3, u | IN; u used before «u = K0» (G-2 (iii)) |
| the root-first key comparison | R24 (b)'s rule, not glossed (G-2 (v)) |
| N5 run, states, IDEAL states, fallback, FL run | IN («one FL run (a maximal set of consecutive non-fallback transitions …)») |
| p, n-vertex game, polynomial, super-polynomial | IN (G-2 (ix)) |
| 𝒞^1O | as in R103's title |
| tail: L 17 to 64, R178 / R188 (G-10), pin names and sha1 prefixes, L_FL, Oink 8fbf0a7, --zlk / --tl, verify, two N5 engines | DATA, cited |
Agreeing tests: REFEREE §4 l. 111-118, §C l. 169; REFEREE-2 §6 l. 190-191. Neither lists the G-2 items.
(8) FIXES AND STATUS NOTES (docs/red/P-N5-REALIZE-fixes.md, L-RED successor 45, append-only, two entries): at 02dfc35c sha1
864cad5978cb79f7c73c6ba99cff8202fe34cc5b, 56 lines (entry 1; both referees checked this version); at c28583b3 sha1
72c687a0944d0acf8402686159dc368022d2ba90, 64 lines (+8, entry 2; = 03255d5d). Header (l. 1-3): «P-N5-REALIZE fixes (append-only; the
frozen packet 067f06b6 and line 53dd6e9f are never edited)», «Where an entry and the frozen packet differ, the entry governs.»
Entry 1 (l. 5-56): REFEREE REAL-L1 (line), REAL-P1 (packet reading: bridge B redundant, Lemma R + TB essential), REAL-P2 (L(G) = 0, §4,
§5 and line), REAL-P3 (finiteness clause, §2); REFEREE-2 REAL-L1 (line), REAL-L2 (line), G-REAL-1 (§1 [1E-N3] in two forms; [RULE] on
σ_new), P-1 (line), P-2 (= REAL-P2), N-2 (ratio 0.177-0.260), N-1 (noted); «Line L-1 …: the changes against 53dd6e9f, nothing else»
(six items). Entry 2 (l. 58-64): REFEREE-2 Addendum 1's failing instance for REFEREE REAL-L1, «no further line change», the joint
REQUIRED list «all in L-1». No fix changes a signed inequality: G-REAL-1 widens the premise's stated form to what the proof uses (both
forms are R57 (b) under L45); REAL-P1 corrects a remark; REAL-P2 states the empty case; REAL-P3 adds a clause; the line items add text the
packet already has (§2 Fact X, §3.1).
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-1 states no CONJECTURE and kills none of RESULTS or GAPS (packet §8 «CONJECTURE IDEAL-LIN,
R178, open» is L-RED's, not in GAPS: «IDEAL» 0 times). A line-11 UPDATE is proposed at the end, to go AFTER R103's UPDATE (GAPS at
5fdcfb9e: the last UPDATE on l. 11 is R103's «UPDATE 2026-11-02 00:24Z: RESULTS R103 (P-N5-ANCHOR; CHECKER C114 da67696a) [refereed-only]
LANDED: …», ending «G-N5-TIME stays open.» before the row's closing « |»; l. 11 holds 76 "|" and 38 «UPDATE 2026-»), as a pure insertion
with one separating space. Built by script (scratch upd104.py: upd100L3.py's build() unchanged, as upd101.py-upd103.py). L-1 has R101's
and R103's shape (one date parenthesis before « — » and a source parenthesis), so build() takes it directly, with the whole date text
«2026-11-02; revision L-1 2026-11-02» as its date argument: labels moved behind their clauses (searched after the binder «for every G
whose Ξ-graph is ACYCLIC, »), « (date) — » → «: », the scope parenthesis opened into the tail minus «G-N5-TIME stays OPEN» and «not M3,
not a step-4 pass, not a TARGET.md claim», the source parenthesis kept, «. G-N5-TIME stays open.» appended. L-1 holds no "|", so no
replacement list. CONTROLS (same script, same run, 2026-11-02T07:14:17Z, rc 0): R97's, R98's, R99's, R100's, R101's, R102's and R103's LANDED UPDATEs (GAPS
l. 11 at 5fdcfb9e) rebuilt from their lines byte for byte (True ×7; 4,179, 4,260, 4,870, 4,768, 3,692, 2,739 and 3,709 bytes; R102's by
upd102.py's sentinel path, also equal to R102-draft l. 455; R103's also equal to R103-draft l. 546 with «2026-11-01» → «2026-11-02»,
00:24 and da67696a). Checked by script: one line, 0 "|", one «<DATE>», one «<HH:MM>», one «<checker>», 4,587 bytes, 831 tokens; the
date parenthesis and «revision» are dropped by the rule (0 times). Head «UPDATE <DATE> <HH:MM>Z: RESULTS R104 (P-N5-REALIZE; CHECKER
C115 <checker>) [refereed-only] » («P-N5-REALIZE» 0 times in GAPS and RESULTS); <DATE> = the landing date (G-11).
(10) DATA of record = packet §7 (l. 241-266), NOT signed; L-1's DATA clause states its counts. Re-run for this draft (scratch, git
archive of 03255d5d; outputs pin104.out, pinok104.out, scope104.out):
- check.sh «R187 REALIZE» (l. 710-719) and «P-N5-REALIZE» (l. 733-746) blocks with l. 1-7, 07:00:48-07:01:16Z, rc 0 (the blocks are
  silent on success): the frozen sha1s of the packet, the frozen line and L-1; the R187 and R188 pin sha1s; lemck on the 7 champions
  and the 2 R188 genomes, «LEMCK random ACYC d 4 games 20 L 1-2 sum 24 viol SBAR 0 TAU 0 ESC 0 W 0 AV 0 KEY 0 FB 0», «--perturb 60 189»
  («sum 1011», 0 violations); realck «REALCK big_d4_k3_W3.json IDEAL 32 stuck FAITHFUL 32 EQUAL True», «REALCK grow_top_N24.json
  IDEAL 64 stuck FAITHFUL 64 EQUAL True», 20 / 20 random equal; ovtkey on both stab pins; the four Oink pins.
- r187/pinck.sh on the four pins, 07:01:25-07:01:31Z, rc 0 each: «PIN OK stab_d4_n126.pg (startck, zlk+verify, tl+verify, xeng)», and the
  same for stab_g24_n246, x3_L8_n48, g4_L12_n62. The eight pin files have the packet's full sha1s (§7 l. 260-263; by sha1sum).
- The other two random rows of §7: «LEMCK random ACYC d 3 games 20 L 0-2 sum 19 viol SBAR 0 TAU 0 ESC 0 W 0 AV 0 KEY 0 FB 0», «LEMCK
  random ACYC d 5 games 20 L 0-2 sum 20 viol SBAR 0 TAU 0 ESC 0 W 0 AV 0 KEY 0 FB 0» (= §7's «sums 19 / 24 / 20»).
- §6 Ξ-cyclic DATA, t2.py CLASS=full: seed 187 d 3 «games 30 equal (states and FAITHFUL = IDEAL steps) 14»; seed 188 d 4: 20 MISMATCH
  lines (= packet l. 235-236).
NOT re-run: the referees' tools (realize_probe.py, realize_check.py); §7's z3 maxima (z3 is not installed here; packet l. 266; REFEREE-2
N-3 did not re-run them either); check.sh's other blocks and scripts/verify.sh.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 packet l. 264 «check.sh block «P-N5-REALIZE» runs the champion rows, the
R188 rows, --rand 20 4 187, --perturb 60 189, the frozen sha1s, and the pins.»: the block's pinck loop covers the R188 pins only; the
stab pins are run by the «R187 REALIZE» block (l. 719), which was in check.sh before the freeze. D-2 REFEREE l. 135-136 «I did NOT
check that the mover states equal the IDEAL ones» and «I did not re-run Oink or n5b on these pins.»; REFEREE-2 did both (l. 159-163,
l. 185-186). D-3 check.sh runs one of §7's three --rand rows (re-run here, (10)). D-4 REFEREE-2's «N5 iterations 35 / 67 / 11 / 15» «=
L + 3» (l. 186-187) counts the whole run on its own loop, including the fallback at L + 1 and what follows it; REALIZE says nothing
after transition L + 1; consistent.
D-5 REFEREE-2 N-2: «L / n ≈ 0.2-0.26» is 0.177-0.260 (fixes l. 47); not in L-1.
(12) Excluded: L-RED R189 (LAG, NEST-DEAD, 8192e194, 81988332), R190 (612fb565, 24e6fd69, 03255d5d: lane-level, unreviewed); R187 §2-§5
and R188's z3 maxima; the packet's §7 «What the data says about L» and §8 READING; the referees' tools (docs/referee/scratch/
realize_probe.py, realize_logs/; docs/referee-2/R2-N5-REALIZE/realize_check.py, logs/). Not part of this entry.
(13) Commits: lane (claude/l-red): e609c5d2 (2026-11-02T02:46:02Z; freeze: packet +278, frozen line +1, r189/lemck.py, check.sh
«P-N5-REALIZE» block) → 02dfc35c (05:04:18Z; fixes entry 1 +56, L-1 +1, check.sh L-1 pin) → c28583b3 (05:28:56Z; fixes entry 2 +8).
Proof source: R187 §1 (l-red 436fe6e9, successor 44). REFEREE (claude/referee): 05b865e0 (03:36:42Z; report, new file 150 lines, sha1
fac7235e…; scratch/realize_probe.py, realize_logs/) → 5cc6be95 (05:57:19Z; §C, +22; the file now 172 lines, sha1 2bd76500…).
REFEREE-2 (claude/referee-2): 0188fc66 (04:19:26Z; report, new file 224 lines, sha1 48f776ea…; R2-N5-REALIZE/realize_check.py, logs/;
bcd43b5a 04:19:42Z notebook stamp) → a22cf5d8 (04:51:46Z; Addendum 1, +24; 248 lines, sha1 f6a67e84…; a2070483 04:51:54Z notebook) →
c9eafef4 (05:58:52Z; R2-N5-REALIZE-L1.md, new file 85 lines, sha1 638ed460…; MUT=border control) → 4db41c9d (05:58:59Z; merge of
trunk). Lead: de75072a (L46), 165dda1e (L46 Amendment), 322922ec (L45). Trunk: see the header.
(14) Placement: see (0). No Dead-ends row: L-1 has no DEAD; «random Ξ-cyclic genomes do mismatch» is a scope statement with DATA, not a
killed conjecture. It kills no conjecture of RESULTS or GAPS. The Lead decides on a row (none proposed).
### R104 [refereed-only] N5 (SPEC S1-S5 from a GIVEN start pair, under the standing SPEC premise of RESULTS R57 (1E-N3: «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance», RESULTS R57 (b), read on every valid input of S1's procedure (Lead reading L45, RESULTS R102), used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima; and S4a's σ_new, S1's output on the dual of the one-player arena in which Even y keeps {σ(y)} ∪ Iσ(y) and Odd follows τ, is a pointwise optimum of that arena, before S4c), with RESULTS R24 (a) Lemma R and R24 (b)'s choice rule (TB proof steps 1, 3-5; fixes §2.3) with bridge B, whose proof uses no 𝒞^1O hypothesis (Lead reading L46 and its amendment), and with VJ00 local optimality (BRICS RS-00-48 Lemma 5.8 «1 ⇒ 2», the direction that holds, applied to Odd's one-player game against a fixed σ)) realises the IDEAL model of L-RED R178 §1 on acyclic Ξ-graphs: an IDEAL genome G has N movers x with levels lev(x), M := Σ deg(x) options (x, k), each with a W-target of level lev(x) − 1 (none at level 0), a Ξ-target that is a mover or X, a distinct β-rank with a parity, a distinct gate index, and a start; under a state s the Ξ-value of option (x, k) is the set of β's on its chain (x, k), (xt, s(xt)), … up to the first Ξ-target X, compared by the β of largest rank in the symmetric difference: the option whose set contains that β is the better one if its parity is even and the worse one if odd; an IDEAL step moves every mover to the lexicographically least key (gate indices of the chain of W-targets under the new state, lowest level first) among its current option and the options with a strictly better Ξ-value, and the run stops when nothing is available or nothing changes, L(G) := its number of steps; the Ξ-graph has an edge x → xt(x, k) for every option with a mover as Ξ-target; for every G whose Ξ-graph is ACYCLIC, the game Γ(G) on n = N + 3M + 6 vertices (Even movers of priority 0; Odd gates of priority 1 with a W-face e and a Ξ-face β; β of priority 6 + 2·rank + parity with edges to the Ξ-target and to u, or to u alone; e of even priority above every β with one edge to the W-target or to the top even self-loop c_W; an unused even self-loop of priority 2; c_W's priority top is the least even number at least 2 above every other priority so far; a closed core u = K0 (Even, top + 2) → {K1, K3}, K1 (Even, 5) → {K0, K1}, K2 (Odd, 3) → {K1, K2}, K3 (Even, top + 3) → {K1, K2}; vertex indices: movers, gates in gate-index order, β-vertices, e-vertices in the order of their gates' gate indices, the unused loop, c_W, K0 to K3 (packet §3.1), on which the root-first key comparison depends) with start σ = the genome start at movers, β → its Ξ-target (u when the target is X), K0 → K3, K1 → K1, K3 → K2, τ = e at every gate and K2 → K2, has (Theorem REALIZE) an N5 run whose states 0, …, L(G) carry the IDEAL states at the movers, Odd's optimal counterstrategy on the β-face at every gate (strict local preference), τ unchanged (no Odd-improving edge), σ unchanged off the movers, the valuation of the (σ, τ)-play unchanged at every vertex, no fallback before state L(G) and a fallback at transition L(G) + 1, so, if L(G) ≥ 1, [0, L(G)] is one FL run (a maximal set of consecutive non-fallback transitions that keep τ, change σ and keep that valuation everywhere) of length exactly L(G) (no FL run if L(G) = 0); hence (Corollary REAL-IDEAL) if every FL run of N5 from every start pair on every n-vertex game has length at most p(n) for a nondecreasing polynomial p, then L(G) ≤ p(3(N + M) + 6) for every acyclic G, and a family of acyclic genomes with L super-polynomial in N + M is a family of real games with super-polynomially long FL runs from the stated start pairs (2026-11-02; revision L-1 2026-11-02) — a REDUCTION / NECESSITY statement only (no count is bounded; Ξ-cyclic genomes are not covered, and random Ξ-cyclic genomes do mismatch; nothing about N5's default start S3; the converse is not claimed; DATA: per-lemma checks with 0 violations on the 7 R178 champions (L 17 to 64), 2 R188 genomes, 60 random and 60 perturbed acyclic genomes; pins stab_d4_n126 (06f81991…, L_FL 32), stab_g24_n246 (55295dd8…, L_FL 64), x3_L8_n48 (158ca15d…), g4_L12_n62 (658f4e23…), each with a validated start and checked against Oink 8fbf0a7 --zlk / --tl with verify and two N5 engines; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim) (P-N5-REALIZE, docs/red/P-N5-REALIZE.md; L-RED successors 44-45), CHECKER PASS (docs/checker/C115.md, checker PENDING)
- Object (L-RED successor 45, Opus 5.5, D1 / D18; frozen, unchanged during review): packet P-N5-REALIZE, docs/red/P-N5-REALIZE.md, sha1
  067f06b6c67969adf346621b4a92b253491ab2b9, 278 lines (l-red freeze e609c5d2, 2026-11-02T02:46:02Z, the file's only commit; identical
  at 02dfc35c, c28583b3 and 03255d5d; sha1 pinned in experiments/red/check.sh). Both referees measured the sha1 (REFEREE l. 2-3
  «Packet claude/l-red e609c5d2, docs/red/P-N5-REALIZE.md (sha1 067f06b6…, 278», «lines)»; REFEREE-2 §0 l. 11-12
  «sha1 067f06b6c67969adf346621b4a92b253491ab2b9,» «278 lines. Re-hashed: match.»). The proof is L-RED successor 44's R187 §1 (packet l.
  5-6, «proof by successor 44»), restated and governed by the packet. Title (l. 1): «P-N5-REALIZE: every IDEAL genome with an ACYCLIC
  Ξ-graph runs, state for state, as ONE real N5 FL run of the STAB+K+ESC game of size N + 3M + 6 (Theorem REALIZE)». Status (l. 4):
  «Status: a REDUCTION / NECESSITY statement. It bounds NOTHING. G-N5-TIME stays OPEN. Not M3, not a step-4 pass, not a TARGET.md
  claim.» To sign (l. 7-8): «To sign: §3 Lemmas K, PLAY, SBAR, TAU, ESC, W, KEY; §4 Theorem REALIZE; §5 Corollary REAL-IDEAL. To check: §6
  (scope), §7 (DATA» «reproduction). Not to sign: §7 numbers as statements (DATA), §8 (honest limits, READING).» Sections: §1 setting
  and premises (l. 13-49), §2 the IDEAL model and IDEAL-ACYC (l. 51-79), §3 the construction and the lemmas (l. 81-200), §4 Theorem
  REALIZE (l. 202-218), §5 Corollary REAL-IDEAL (l. 220-229), §6 scope (l. 231-239), §7 DATA (l. 241-266), §8 honest limits (l. 268-278).
  Fixes: docs/red/P-N5-REALIZE-fixes.md (append-only; entry 1 at 02dfc35c, entry 2 at c28583b3, sha1 72c687a0…, 64 lines); «Where an
  entry and the frozen packet differ, the entry governs.» (l. 3). The packet read with its fixes is the text of record.
  The RESULTS line, history: (1) the frozen line docs/red/P-N5-REALIZE-line.txt (sha1 53dd6e9f…, committed with the packet), the line
  both reports reviewed: REFEREE REQUIRED REAL-L1 (the e-index order, l. 26, §4 l. 106-110); REFEREE-2 REQUIRED REAL-L1 (the 1E-N3
  gloss) and REAL-L2 (the direction of the IDEAL order) (l. 40, §6 l. 193-198), and in its Addendum 1 also REFEREE's REAL-L1, with a
  failing instance (l. 228-234). At the frozen line the 1E-N3 gloss read «at a non-fallback transition j − 1 → j, σ_j is a pointwise
  optimum of the one-player arena in which Even y keeps {σ_(j−1)(y)} ∪ Iσ_(j−1)(y) and Odd follows τ_(j−1)», the order read «compared by
  the β of largest rank in the symmetric difference and its parity», and Γ(G) had no vertex indices. (2) L-1
  1d72ee310b9b4af252724e06a181221a9c2828ec (docs/red/P-N5-REALIZE-line-L1.txt, l-red 02dfc35c, 2026-11-02T05:04:18Z, the file's only
  commit; fixes entry 1; sha1 pinned in check.sh) = the frozen line with exactly six changes (fixes l. 50-56): R57 (b)'s words in two
  forms; the direction of the order; «top» and the vertex-index layout; the start at β; the L(G) = 0 case; the date tag. REFEREE §C
  (5cc6be95) l. 156 «Exactly the six listed changes. Nothing else changed:», l. 172 «Verdict: line L-1 **MATCHES**.» REFEREE-2
  R2-N5-REALIZE-L1.md (c9eafef4) l. 20-21 «Byte test:» «start from the frozen line, apply exactly the 8 replacements below», «and
  compare with L-1: **True**.», l. 77 «**MATCHES.** L-1 (1d72ee31) differs from the frozen line (53dd6e9f) by exactly the six listed
  items. The three REQUIRED items are met.» Fixes entry 2 (c28583b3) records REFEREE-2 Addendum 1 and changes no line text.
  L-1 supersedes the frozen line; the title is L-1 verbatim, with nothing inserted (its date parenthesis «(2026-11-02; revision L-1
  2026-11-02)» and its source note are the line's own; to check (1)). Neither referee found a FALSE claim statement in the packet; every
  line item states the premise in the form the proof uses, states a direction or an index layout the packet already has, or makes a
  case explicit.
  Setting (packet §1-§2): N5 = SPEC S1-S5 «on a parity game Γ = (V, E, Ω, owner), n := |V|, run from a GIVEN start» «pair (σ_0, τ_0)
  (SPEC: «Optional start pair»).» (l. 14-15); a transition is a FALLBACK «if S4c fired at it» (l. 16); values (c, P, ℓ) and the order ⊳
  as in SPEC S1 (l. 17-22); «Ξ_j := Ξσ_j (σ_j with Odd's OPTIMAL counterstrategy σ̄_j, minimising the order at every vertex at once, SPEC
  S1).» (l. 23); an FL run (l. 29-30) is «a maximal set of consecutive transitions j = a + 1, …, b, each of which is not a fallback, keeps
  τ» «(τ_j = τ_(j−1)), changes σ (σ_j ≠ σ_(j−1)) and keeps W (W_j = W_(j−1) at every vertex). Its length is b − a.» (as in RESULTS R103).
  The IDEAL model (§2, l. 51-79; L-RED R178 §1): a genome G with movers x of level lev(x), options (x, k), W-targets wt one level down
  (GRADED), Ξ-targets xt ∈ {movers} ∪ {X}, β-ids with rank br and parity bp, gate indices and a start s_0; the X-chain of an option and
  its β-set B_s(x, k) (l. 61-63); «G is in IDEAL-ACYC iff its» «Ξ-graph is ACYCLIC (self-loops count as cycles).» (l. 59-60); the IDEAL
  step (l. 71-76) with availability A_s(x), the lexicographically least key, and the stops «opt» and «stuck»; L(G) := the number of IDEAL
  steps from s_0. The game Γ(G) (§3.1, l. 82-99; experiments/red/r187/stab.py, build(G, 0, kgad=True, esc=True)): movers (Even, Ω 0),
  gates g = (x, k) (Odd, Ω 1, edges {e_g, β_g}), β_g (Even, Ω 6 + 2·br + bp, edges {xt(g), u} or {u}), e_g (Even, even Ω above every β,
  one edge to wt(g) or c_W), c_X (Ω 2, unused), c_W (top), the closed core K = (K0, K1, K2, K3) with u := K0; indices «movers, gates in
  gate-index order, β-vertices, e-vertices in the order of their gates' gate indices, the unused loop, c_W, K0 to K3» (L-1; packet l.
  84-92); start (σ_0, τ_0) (l. 96-97). A STANDARD STATE for a mover state s is (σ^s, τ_0) (l. 98).
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 22 (report 05b865e0; §C on L-1 5cc6be95); REFEREE-2 successor 26
  (report 0188fc66; Addendum 1 a22cf5d8; R2-N5-REALIZE-L1.md c9eafef4)). Items (a)-(k) are SIGNED in both verdict tables (REFEREE "## 0.
  Verdicts" l. 10-26 of R-N5-REALIZE.md; REFEREE-2 "## 1. Verdict table" l. 22-40 of R2-N5-REALIZE.md); the table is to-check (4). All
  hold for every IDEAL genome with an ACYCLIC Ξ-graph and its game Γ(G) from the start (σ_0, τ_0), under the premises below. No item
  bounds a count.
  (a) Fact DUAL (§1, l. 25-28): «The order of G^d is the REVERSE of the order of Γ»; «So Iτ(v) = {w ≠ τ(v) : Ξτ(w) ◁ Ξτ(τ(v))} (strictly
      better for Odd in Γ's order),» «and τ̄ maximises Γ's order at every vertex.» Cells: REFEREE «**SIGNED**» (l. 13; §1 l. 31-33);
      REFEREE-2 «**SIGNED**» (l. 25; §4 l. 91-97).
  (b) Fact X (§2, l. 66-70): «For IDEAL-ACYC and two options k ≠ k' of ONE mover x, B_s(x, k) ≠ B_s(x, k')»; «(x, k) ▷_s (x, k') iff the
      β-id of LARGEST rank in B_s(x, k) Δ B_s(x, k') has parity 0 and lies in B_s(x, k), or has parity 1 and lies» «in B_s(x, k').
      Lengths never decide.» Cells: REFEREE «**SIGNED**» (l. 14; §1 l. 34-36); REFEREE-2 «**SIGNED**» (l. 26; §4 l. 98-102).
  (c) Lemma K, the stuck core (§3.2, l. 101-117), in every standard state: «(a) Ξσ on K: K1 ↦ (K1, ∅, 0); K2 ↦ (K1, ∅, 1); K3 ↦ (K1,
      {K3}, 2); K0 ↦ (K1, {K0, K3}, 3)»; «(b) Iσ ∩ K = {(K0, K1)}.»; «(c) Iτ ∩ K = ∅»; «(d) In S4a's arena H, every play from u ends in an
      ODD cycle (node K1 or K2), and the pointwise optimum keeps σ on K.» Cells: REFEREE «**SIGNED**» (l. 15; §2 l. 43-47); REFEREE-2
      «**SIGNED** ((c) uses P1 on G^d, see G-REAL-1 (a))» (l. 27; §4 l. 103-108).
  (d) Lemma PLAY (§3.3, l. 119-131): with ρ «β_g at every gate, K1 at K2» and φ := φ_(σ,ρ), «(a) the (σ, ρ)-play from β_g follows the
      X-chain of g», «So φ(β_g) = (K1, B(g) ∪ {K0, K3}, ℓ_g) for some length ℓ_g»; «(b) for lev(x) = 0: the play from e_g is e_g → c_W,
      φ(e_g) = (c_W, ∅, 1);»; (c) for lev(x) ≥ 1, «φ(e_g) = (K1, {e_g} ∪ B(g') ∪ {K0, K3}, ℓ_(g') + 3).» Cells: REFEREE «**SIGNED**» (l.
      16; §2 l. 48-51); REFEREE-2 «**SIGNED**» (l. 28; §4 l. 109-112).
  (e) Lemma SBAR (§3.4, l. 133-149): «In every standard state, σ̄ = ρ: σ̄(g) = β_g at every gate g and σ̄(K2) = K1. Hence Ξσ = φ.» (strict
      local preference (i), [VJ-LOC] (ii), uniqueness against SPEC's σ̄ (iii)). Cells: REFEREE «**SIGNED** ([VJ-LOC] used only in the
      «1 ⇒ 2» direction ✓)» (l. 17; §2 l. 52-59); REFEREE-2 «**SIGNED**, with G-REAL-1 (a) (P1 used, not named in §1; covered by the
      landed 1E-N3)» (l. 29; §4 l. 113-116).
  (f) Lemma TAU (§3.5, l. 151-160): «In every standard state, Iτ = ∅. So S4b leaves τ unchanged (τ_new = τ).» Cells: REFEREE «**SIGNED**»
      (l. 18; §2 l. 60-62); REFEREE-2 «**SIGNED** (P1 on G^d, G-REAL-1 (a)); its proof uses no acyclicity» (l. 30; §4 l. 117-120).
  (g) Lemma ESC (§3.6, l. 162-171): «In every standard state: Iσ ≠ ∅ (it contains (K0, K1)), and every pointwise optimum of S4a's arena H
      has σ_new(β_g) = σ(β_g) at every β,» «σ_new = σ on K, and σ_new = σ on e, c_X, c_W (single edges).» Cells: REFEREE «**SIGNED**» (l.
      19; §2 l. 63-66); REFEREE-2 «**SIGNED**» (l. 31; §4 l. 121-122).
  (h) Lemma W (§3.7, l. 173-184), in every standard state and for every s: (i) «W(x) = (c_W, ∅, 3·lev(x) + 3)» at movers, with the gate,
      e and β values of l. 175-176, «Hence W is the SAME for every» «standard state.»; (ii) «W*(y) = (c_W, ∅, 3ℓ + 2) for every gate y of a
      level-ℓ mover»; (iii) «For every mover x: x's W′-cycle node is c_W (even, ≠ x); every option y ∈ R(x) is FULLY W′-optimal (W*(x) =
      x ⊕ W*(y)); none is» «a corner», «So TIE(x) = R(x).» Cells: REFEREE «**SIGNED**» (l. 20; §2 l. 67-71); REFEREE-2 «**SIGNED**» (l.
      32; §4 l. 123-126).
  (i) Lemma KEY (§3.8, l. 186-200), in every standard state, for every mover x: «(a) R(x) = {σ(x)} ∪ Iσ(x) is the set of gates (x, k) with
      k ∈ A_s(x).»; «(b) For y, y' ∈ R(x) and any Even strategy σ' that agrees with σ^(s') on movers of level < lev(x) (any s'), the
      root-first keys» «κ(y), κ(y') under (σ', τ_0) compare as the IDEAL keys key_(s')(x, k), key_(s')(x, k').» KEY (b) uses that
      «e-indices follow gate indices» (l. 199). Cells: REFEREE «**SIGNED** (KEY (b) needs the e-index layout; see REAL-L1)» (l. 21; §2
      l. 72-78); REFEREE-2 «**SIGNED**» (l. 33; §4 l. 127-133).
  (j) Theorem REALIZE (§4, l. 202-218, with fixes REAL-P2, l. 23-25): «Let G ∈ IDEAL-ACYC with IDEAL run s_0 → s_1 → … → s_L (L = L(G)) and
      Γ(G) with start (σ_0, τ_0) (§3.1). Then the N5 run of Γ(G) from» «(σ_0, τ_0) has states (σ^(s_j), τ_0) for j = 0, …, L; transitions
      1, …, L are FL transitions; transition L + 1 is a fallback.»; fixes: «if L(G) ≥ 1, [0, L(G)] is one FL run of length L(G); if L(G)
      = 0, transition 1 is a fallback and there is no FL» «run». Proof by induction on j through TAU, ESC, [1E-N3], W (iii), [RULE] and
      KEY; the IDEAL stop is an S4c fallback. Cells: REFEREE «**SIGNED** (the IDEAL stop is an S4c fallback ✓; precisions REAL-P2,
      REAL-P3)» (l. 22; §3 l. 81-90); REFEREE-2 «**SIGNED**, with G-REAL-1 (b)» (l. 34), «Closed by landed items (§2 below), and a
      second time directly from SPEC S1's text (§3 below). No new proof; L41 not triggered» (§2 l. 55-65, §3 l. 72-88, §4 l. 134-140).
  (k) Corollary REAL-IDEAL (§5, l. 220-229): size «Γ(G) has n = N + 3M + 6 vertices and at most M (movers) + 2M (gates) + 2M (β) + M (e)
      + 2 + 8 = 6M + 10 edges; every» «Ω ≤ 4M + 9»; «(a) NECESSITY.» «FL-POLY ⇒ IDEAL-ACYC-POLY, with q(t) := p(3t + 6): by Theorem REALIZE,
      L(G) is the length of an FL run of Γ(G) from (σ_0, τ_0).»; «(b) TRANSFER. If (G_i) ⊆ IDEAL-ACYC has L(G_i) super-polynomial in N_i +
      M_i, then (Γ(G_i), (σ_0, τ_0)_i) is a family of real games» «of size n_i = N_i + 3M_i + 6 whose N5 runs FROM THOSE START PAIRS
      contain one FL run of length L(G_i), hence ≥ L(G_i) iterations:» «super-polynomial in n_i.»; «Not claimed: the converse
      (IDEAL-ACYC-POLY ⇒ FL-POLY); anything about the S3 default start; anything for Ξ-cyclic genomes.» Cells: REFEREE «**SIGNED**» (l.
      23; §3 l. 91-95); REFEREE-2 «**SIGNED**» (l. 35; §4 l. 141-146).
  The RESULTS line (L-1) states (j) and (k) and nothing wider (to check (4)); (a)-(i) are the signed lemmas of its proof. Its tail states
  the scope words, the DATA and the pins.
- Premise 1E-N3, both forms. L-1: «under the standing SPEC premise of RESULTS R57 (1E-N3: «that S1's procedure realises an optimal σ̄ is
  VJ00 §6 plus SPEC conformance», RESULTS R57 (b), read on every valid input of S1's procedure (Lead reading L45, RESULTS R102), used in
  two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima; and S4a's σ_new, S1's output on the dual of the one-player arena in
  which Even y keeps {σ(y)} ∪ Iσ(y) and Odd follows τ, is a pointwise optimum of that arena, before S4c)». R57 (b) (RESULTS l. 2915-2916):
  «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance, and the code's match to SPEC is DATA (R15 G-N5T-1)
  (1E-N3 = N-1E-1).» Lead reading L45 (docs/DECISIONS.md l. 383-390; index «active»): «L42 stays in force for any premise other than
  S1's procedure on a valid input.» Lead reading L42 (l. 362-367; index «active (S4b part lifted by L45)»): «R57's standing SPEC premise
  (1E-N3) covers S1's procedure and S4a (σ_(k+1) is the pointwise optimum of H_k).» The two-forms reading is landed in R67 (l. 3461-3463).
  The packet's frozen §1 stated only the S4a form at non-fallback transitions; REFEREE-2 G-REAL-1 (§2 l. 44-70): «(a) P1 is used but not
  named.» (SBAR (ii), (iii); TAU and K (c) through Fact DUAL) and «(b) σ_new before S4c.» (REALIZE's step applies [1E-N3] and [RULE] to
  σ_new before the transition is known to be non-fallback), «CLOSED by landed items» (l. 42): R57 (b) on every valid input (L45, R102),
  and for (b) R102's statement read on dual(H) and R103's (R1) ruling («TB steps 1, 3-5 describe the output of one S1 call on dual(H)», l.
  64). Fixes entry 1 (l. 38-44) reads §1 that way («ACCEPTED as a correction of §1's wording only.», l. 40). REFEREE l. 39 «[1E-N3] ✓ for S4a (R57) and for S1's σ̄ (SBAR (iii)).» As for
  every landed N5 result, the correctness of S1's procedure stays SPEC's requirement and the code's conformance stays DATA (R57 (b)).
- Premise R24 (a) Lemma R and R24 (b)'s choice rule, class-free by Lead reading L46 under L44. L-1: «with RESULTS R24 (a) Lemma R and
  R24 (b)'s choice rule (TB proof steps 1, 3-5; fixes §2.3) with bridge B, whose proof uses no 𝒞^1O hypothesis (Lead reading L46 and its
  amendment)», R103's landed citing line plus «and its amendment». L46 (docs/DECISIONS.md l. 392-401): «RESULTS R24 (a) Lemma R and R24
  (b) Lemma TB are class-free under L44 (i)-(ii)»; «Not covered: R24 (c)-(e).» Amendment (l. 402-406): «(2) wording: «corner» means
  that h occurs on the option's play BEFORE that play's cycle node». L44 (l. 376-381) asks that «the citing line says so («its proof
  uses no 𝒞^1O hypothesis») and the entry quotes both confirmations.» The two confirmations: REFEREE docs/referee/R-R24-L44.md (472f0dcd)
  l. 91 «1. R24 (a) Lemma R (fully optimal form): CLASS-FREE. No step uses 𝒞^1O.», l. 92 «2. R24 (b) Lemma TB as signed: CLASS-FREE. The
  statement already says «any game»; (F1) is used on the one-player arena H_k, which is»; REFEREE-2 docs/referee-2/R2-R24-L44.md
  (d96d2f9e) l. 77 «R24 (a) Lemma R: **CLASS-FREE**. L44 (i) and (ii) hold.», l. 78 «R24 (b) Lemma TB, including its choice form:
  **CLASS-FREE**. L44 (i) and (ii) hold.» The REALIZE referees checked the use: REFEREE l. 4 «L46 (the [RULE] citation)», §3 l. 97-99
  (REAL-P1: «The» «citation of R24 (a) Lemma R + TB steps 1, 3-5 is NOT redundant: it gives «σ_new(x) is the κ-least element of TIE(x)»,
  which no lemma» «of the packet proves.»); REFEREE-2 table l. 37 «citing line verbatim = RESULTS R103's. Bridge B's conclusion is Lemma
  W (iii), signed here, which is what L46 asks of a citing packet». The packet's form (§1 l. 42-46): «σ_j(x) is the κ_j-least element of
  TIE_j(x)», read by fixes G-REAL-1 as «σ_new(x) (= σ_j(x) at a» «non-fallback transition)», at every Even x that is not its own
  W′-cycle node, «Non-movers are covered ((R1) ruled «covered», RESULTS R103).» (l. 46). Bridge B (RESULTS R103) is cited as CF-1 asks;
  its conclusion is Lemma W (iii) here (fixes REAL-P1, l. 16-22), so the entry does not use bridge B's FL hypothesis (draft G-3).
- Premise [VJ-LOC]. L-1: «with VJ00 local optimality (BRICS RS-00-48 Lemma 5.8 «1 ⇒ 2», the direction that holds, applied to Odd's
  one-player game against a fixed σ)». Packet l. 36-39: «[VJ-LOC] VJ00 local optimality: BRICS RS-00-48 Lemma 5.8 «1 ⇒ 2» (no improving
  switch ⇒ optimal), the direction that HOLDS (RESULTS» «R15 side finding; L-LIT docs/lit/T21-VJ00-check.md (c) «Unaffected»).», used
  only in SBAR (ii). REFEREE l. 37-38: «SBAR (ii) uses «no Odd-improving switch for ρ ⇒ φ_(σ,ρ) = Ξσ»: Lemma 5.8 «1 ⇒ 2» in G^d's
  one-player game Γ_σ.», «The failing «2 ⇒ 1» (an improvement at a maximum) is not used anywhere.»; REFEREE-2 table l. 36 «only «1 ⇒ 2»
  is used (SBAR (ii))». L-LIT T21 (c): «a stop with no improvement is optimal: BRICS Lemma 5.8 "1 ⇒ 2"» under «Unaffected (both
  versions):». Draft reading (Lead; not a Lead reading on file in DECISIONS, and not a referee statement; draft G-6): on a one-player game this direction is RESULTS R36 (c) Lemma P1 («if σ
  is a positional Even strategy of a one-player game H with no improving edge»), applied on G^d to Γ_σ; R15 (iii)'s G-N5T-3 (Lemma 5.8
  on two-player games, resting on VJ00's Lemma 5.9 and Prop. 5.10) is not used.
- L41 and L43. The proofs are L-RED's (successor 44, R187 §1; successor 45, the packet and its fixes). REFEREE l. 4 «L41 (lane-authored;
  nothing referee-originated)»; REFEREE-2 table l. 34 «No new proof; L41 not triggered», §6 l. 191 «L41: nothing referee-originated.»
  G-REAL-1 is closed by landed items; REFEREE-2 §3's direct trace of S4a at standard states is a second closure that the entry does not
  rest on (fixes l. 44; REFEREE-2 L1 l. 70 «not needed»). No DEAD (L43): REFEREE §4 l. 119 «No DEAD (L43 ✓).»; REFEREE-2 §6 l. 191 «L43:
  no DEAD clause.»
- Fixes (docs/red/P-N5-REALIZE-fixes.md, L-RED successor 45, append-only, entries 1-2; at c28583b3 64 lines, sha1
  72c687a0944d0acf8402686159dc368022d2ba90; entry 1 alone at 02dfc35c, sha1 864cad59…, the version both referees checked).
  - Entry 1 (l. 5-56, «REFEREE 22 … and REFEREE-2 26 …; one revision, line L-1»): REFEREE REAL-L1 (line: vertex indices, «top»);
    REAL-P1 (§1 [RULE] and §8: bridge B part redundant, Lemma R + TB «ESSENTIAL»); REAL-P2 (§4, §5: «if L(G) = 0, transition 1 is a
    fallback and there is no FL» «run (the corollary is unaffected: L(G) = 0 needs no bound)»); REAL-P3 (§2: «this is not circular,
    since the induction does not assume finiteness»); REFEREE-2 REAL-L1 (line: R57 (b), both forms), REAL-L2 (line: direction), G-REAL-1
    («ACCEPTED as a correction of §1's wording only.»), P-1, P-2, N-2, N-1. «Line L-1 …: the changes against 53dd6e9f, nothing else» (l.
    50-56).
  - Entry 2 (l. 58-64, «REFEREE-2 Addendum 1»): «So REAL-L1 is» «substantive, not cosmetic: Lemma KEY (b) needs the gate-index order of
    e-indices (packet §3.1). Line L-1 (1d72ee31) already carries it;» «no further line change.»; «Joint REQUIRED list, all in L-1».
  No fix changes a signed inequality (to check (8)).
- Not signed: §6 scope (checked); §7 DATA (packet l. 241 «## 7. DATA (labelled DATA; reproduction, not proof).»); §8 READING (l. 268
  «## 8. Honest limits (READING)»). OPEN, not claimed: any bound on L(G) (CONJECTURE IDEAL-LIN is L-RED's, open, packet l. 269); FL-POLY;
  any bound on N5's iteration count; G-N5-TIME.
- Referee strengthening (NOT part of this entry; remarks of one referee):
  (i) REFEREE-2 §3 l. 72-88: S4a's σ_new at a standard state read directly off SPEC S1's procedure on dual(H) (K0 first, c_W second, BFS
      from c_W, K2 later): «So REALIZE's σ-step holds at every standard state from SPEC's text alone, whatever S4c does afterwards.»
  (ii) REFEREE-2 controls: MUT=eprio (e-priorities, 0 violations), MUT=border (β indices, 0 violations; L1 l. 50-53), MUT=noesc (TAU
       fires), MUT=eorder (KEYB 33, IDEAL 20: the e-index order matters); BF=11 «490,800 Odd strategies at 392 states» (l. 166), 0
       violations; random ACYC «1,160» genomes, perturbed «200» (l. 164-165), 0 violations.
  (iii) REFEREE-2 N-1 (l. 206): «Lemma TAU and K (c) do not use acyclicity.»; data (table l. 30): «I_τ = ∅ at state 0 on all 294
        Ξ-cyclic probes».
  (iv) REFEREE §5 (l. 121-138): own engine rl_engine on the four pins, «FL runs of 8 / 12 / 32 / 64 from state 0, a fallback right
       after, and 0 lemma violations» (l. 149).
- Honest limits: (i) a REDUCTION / NECESSITY statement only: no count is bounded; it does not say IDEAL-ACYC runs are long or short;
  G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim. (ii) ACYCLIC Ξ-graphs only: every use of acyclicity is listed in
  packet §6 (Lemma PLAY (a), Fact X, and through them SBAR, KEY); «Ξ-CYCLES ARE NOT COVERED.» (l. 234), and random Ξ-cyclic genomes do
  mismatch (DATA, packet l. 235-236: 16 of 30 and 20 of 30 mismatches; REFEREE-2 134 of 294). Also outside: non-graded genomes, pads > 0,
  any start other than (σ_0, τ_0) (l. 238-239). (iii) (b) gives real games only FROM THE GIVEN START PAIRS; «whether N5's default start S3
  reaches such a state is not» «addressed.» (l. 272-273); the converse IDEAL-ACYC-POLY ⇒ FL-POLY is not claimed. (iv) Premises: RESULTS
  R57's 1E-N3 in both forms (L45, R102), R24 (a) and R24 (b)'s choice rule read class-free by L46 under L44 with R103's citing line and
  (R1) ruling, VJ00 Lemma 5.8 «1 ⇒ 2» on a one-player game (draft G-6); as for every landed N5 result, the correctness of S1's procedure
  stays SPEC's requirement (R57 (b)). No Lean. (v) Inside IDEAL-ACYC, σ̄ and τ are fixed by the gadgets (SBAR, TAU), so a proof of
  FL-POLY must bound L on IDEAL-ACYC without help from σ̄-optimality or τ-stability there (packet §8, READING). (vi) The line's
  description of Γ(G) leaves the β-vertex order and the exact e-priorities to packet §3.1; both are immaterial by the referees' controls
  (MUT=border, MUT=eprio), while the e-index order is what Lemma KEY (b) needs and the line states it.
- Data (DATA, not proof): pinned. experiments/red/check.sh at 03255d5d (sha1 fbbeb3e05b072dfa299857500886647d291d949d, 747 lines): block
  «P-N5-REALIZE» l. 733-746 (e609c5d2, L-1 pin at 02dfc35c) with the frozen sha1s of the packet and the frozen line and the sha1 of L-1
  (l. 734-737), the R188 pin sha1s, lemck on the 7 R178 champions and the 2 R188 genomes, --rand 20 4 187, --perturb 60 189 and pinck
  on the two R188 pins; block «R187 REALIZE» l. 710-719 (successor 44) with realck, ovtkey and pinck on the two stab pins. Re-run for this
  draft from a `git archive` of 03255d5d (experiments/ and docs/red/; from experiments/red; GIT_DIR set to the repository; Oink 8fbf0a7
  linked in), l. 1-7 plus l. 710-719 and l. 733-746, 2026-11-02 07:00:48-07:01:16Z by date -u, rc 0 (the blocks print nothing on
  success). Lane outputs re-printed, 07:01:25-07:01:31Z: «PIN OK stab_d4_n126.pg (startck, zlk+verify, tl+verify, xeng)» and the same
  for stab_g24_n246, x3_L8_n48 and g4_L12_n62 (rc 0 each); «LEMCK x3_L8.json L 8 stuck viol SBAR 0 TAU 0 ESC 0 W 0 AV 0 KEY 0 FB 0»,
  «LEMCK g4_L12.json L 12 stuck viol SBAR 0 TAU 0 ESC 0 W 0 AV 0 KEY 0 FB 0»; «REALCK big_d4_k3_W3.json IDEAL 32 stuck FAITHFUL 32 EQUAL
  True», «REALCK grow_top_N24.json IDEAL 64 stuck FAITHFUL 64 EQUAL True».
  Pins (packet §7 l. 258-263; sha1 re-taken at 03255d5d): stab_d4_n126 (r178/out/big_d4_k3_W3.json; n 126, L_FL 32; .pg
  06f81991e8140f0cd851b2ff107776dfc92bcfcb, .start 337b01154e2119ccd344d323410a201fae398e58), stab_g24_n246 (grow_top_N24.json; n 246,
  L_FL 64; 55295dd859fc632196e23127dd2d3dc8426d4607, 3cd50ed19ebfce8735a8d32ba29983ddfd41dbb9), x3_L8_n48 (r188 x3_L8.json; n 48, L_FL
  8; 158ca15db07ff2080239bf4fc35af14c814e5336, f07be77086026f975a7d245a48441f550b6a8e08), g4_L12_n62 (g4_L12.json; n 62, L_FL 12;
  658f4e23ca3c6bb7daccf790007c2ba856abb848, 9f3e1f92f8998c49cd06864d3595f28a208f4d55). pinck = startck (validated start pair), Oink
  8fbf0a7 --zlk + verify (regions = N5's), --tl + verify, xeng (n5b and n5.py: identical states).
  DATA OF RECORD (packet §7, l. 247-254): lemck (per state of the REAL run: SBAR, TAU, ESC, W, AV, KEY, FB) 0 violations on the 7 R178
  champions (L 17 / 32 / 42 / 54 / 39 / 64 / 48, all «stuck»), the R188 genomes x3_L8, g4_L12 (L 8 / 12), 60 random acyclic genomes
  (--rand 20 3 451, 20 4 187, 20 5 452; sums 19 / 24 / 20) and 60 perturbed champions (sum 1011); realck: «FAITHFUL equal, EQUAL True»
  on the champions and 20 / 20 equal on each --rand row. Re-run here: the check.sh rows and the two other --rand rows (sums 19, 20; 0
  violations). Scope DATA (§6, l. 235-236), re-run here: t2.py CLASS=full seed 187 d 3 «games 30 equal (states and FAITHFUL = IDEAL
  steps) 14», seed 188 d 4: 20 MISMATCH lines.
  REFEREE (successor 22; own docs/referee/scratch/realize_probe.py, «rl_engine only», l. 122): table l. 128-133 (the four pins: L_FL 8 /
  12 / 32 / 64, fallback at L + 1, 0 violations).
  REFEREE-2 (successor 26; own docs/referee-2/R2-N5-REALIZE/realize_check.py, its builder compared byte for byte with the four pins):
  table l. 161-167 (9 lane genomes, 1,160 random, 200 perturbed, BF=11, MUT=eprio: 0 violations); lane re-runs l. 180-187 (lemck,
  realck, t2.py, pinck «PIN OK (startck, zlk+verify, tl+verify, xeng)», own Oink comparison «regions equal and verified on all four»).
  No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-REALIZE.md: successor 22's report 05b865e0d3a1dec5015143de91026b5a8f7cc870 (2026-11-02T03:36:42Z,
  new file, 150 lines, sha1 fac7235ee7f9151fe5d0d869c74ee64e080cd947, with scratch/realize_probe.py and realize_logs/): Facts DUAL, X,
  Lemmas K, PLAY, SBAR, TAU, ESC, W, KEY, Theorem REALIZE and Corollary REAL-IDEAL SIGNED, «No gap in the mathematics.» (l. 28), line
  REQUIRED REAL-L1; §C 5cc6be955e2d9f9b298b4bdf9ff3a219e9e797f9 (05:57:19Z, +22, l. 152-172; the file now 172 lines, sha1
  2bd76500b23b86986317c74f517971fdc221c19f): «Verdict: line L-1 **MATCHES**.» (l. 172).
  REFEREE-2 (successor 26): docs/referee-2/R2-N5-REALIZE.md 0188fc66fe9ef2ede96689c532dc7b6e6e32d307 (04:19:26Z, new file, 224 lines,
  sha1 48f776eae7d795ff0ac5721ffe09dc0d4cbfa614; with R2-N5-REALIZE/realize_check.py and logs/): every item SIGNED (l. 25-35, l. 218),
  G-REAL-1 minor and closed (l. 42), line REQUIRED REAL-L1, REAL-L2 (l. 40); Addendum 1 a22cf5d81a7248a8039f6fbff35f5597448401e8
  (04:51:46Z, +24; 248 lines, sha1 f6a67e8464981b7b4ba05c087f1e17488dc27b4d): «Verdicts agree: every to-sign item SIGNED by both; no gap
  in the mathematics.» (l. 227), REFEREE REAL-L1 agreed REQUIRED with a failing instance; R2-N5-REALIZE-L1.md
  c9eafef45a69570ea979228fb2b3d7c410c9bfbe (05:58:52Z, new file, 85 lines, sha1 638ed4608592bbdfe39d20acd014f3434660af2f): «Verdict:
  **MATCHES**.» (l. 2). Lane: freeze e609c5d2c689e87c1dc658e5e65a956fe0478222, L-1 and fixes entry 1
  02dfc35cb9804d171b1db809d4bd79713255b8ec, fixes entry 2 c28583b345a170b580d7a2233ce5d5fc40a8a161.
  INDEPENDENCE: REFEREE l. 3 «Written before reading docs/referee-2/ on this packet.»; REFEREE-2 l. 4 «I wrote this without opening
  docs/referee/ for this packet. At 04:03Z, `git ls-tree` on origin/claude/referee listed 0 files matching «realize».», l. 5 «I did not
  import any lane script.», l. 6-7 (read r187/stab.py build() for the JSON field order only; «My builder is written» «from packet §3.1»);
  Addendum 1 l. 226 «read after my push bcd43b5a». REFEREE's report (03:36:42Z) precedes REFEREE-2's (04:19:26Z) by 43 min.
  Differences, resolved: REFEREE alone found the e-index gap (REAL-L1), REFEREE-2 agreed with a failing instance (Addendum 1); REFEREE-2
  alone found G-REAL-1, REAL-L1 (gloss) and REAL-L2 (direction), which REFEREE's §C checks as met. Both SIGN the same eleven items with no
  gap, and both MATCH L-1. No disagreement in substance.
- TARGET.md diff: «on every n-vertex game» = every TARGET.md §1 game («A parity game is G = (V, V_E, V_O, E, pr) with V finite»; «every
  vertex has at least one successor (self-loops allowed)»); Γ(G) is such a game (every vertex has a successor; its priorities, up to
  4M + 9, are compressed as TARGET.md l. 10 allows, draft G-12). The line (L-1) makes no M4 claim and no TARGET claim; its tail reads «a
  REDUCTION / NECESSITY statement only (no count is bounded;» and «G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim»
  (L-1, by script). REFEREE §4 l. 119 «TARGET.md diff: no bound, no algorithm claim.» Not a claim of TARGET.md §1 or §2 (a reduction of
  IDEAL-ACYC run lengths to the length of one real N5 FL run, from a given start pair; no bound on a run or on running time; no algorithm
  claim); not a step-4 pass. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER R103's UPDATE of G-N5-TIME (GAPS at 5fdcfb9e, last changed by 92314793: the last
UPDATE on l. 11 is R103's, «UPDATE 2026-11-02 00:24Z: RESULTS R103 (P-N5-ANCHOR; CHECKER C114 da67696a) …», before the row's closing « |»),
built by script (upd104.py: upd100L3.py's build() unchanged; labels searched after the binder; to check (9)) only from the clauses of the
title line L-1: labels behind their clauses; « (2026-11-02; revision L-1 2026-11-02) — » → «: »; «G-N5-TIME stays OPEN» and «not M3, not
a step-4 pass, not a TARGET.md claim» dropped from the tail; the source parenthesis kept; «. G-N5-TIME stays open.» at the end. The same
script reproduces R97's to R103's LANDED UPDATEs (GAPS l. 11) byte for byte. L-1 holds no "|"; the UPDATE holds none. <DATE> is the
landing date (YYYY-MM-DD, by date -u at the landing commit; C114 Add. 1 E-1), <HH:MM> the landing time and <checker> the CHECKER C115
commit, all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R104 (P-N5-REALIZE; CHECKER C115 <checker>) [refereed-only] LANDED: N5 (SPEC S1-S5 from a GIVEN start pair, under the standing SPEC premise of RESULTS R57 (1E-N3: «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance», RESULTS R57 (b), read on every valid input of S1's procedure (Lead reading L45, RESULTS R102), used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima; and S4a's σ_new, S1's output on the dual of the one-player arena in which Even y keeps {σ(y)} ∪ Iσ(y) and Odd follows τ, is a pointwise optimum of that arena, before S4c), with RESULTS R24 (a) Lemma R and R24 (b)'s choice rule (TB proof steps 1, 3-5; fixes §2.3) with bridge B, whose proof uses no 𝒞^1O hypothesis (Lead reading L46 and its amendment), and with VJ00 local optimality (BRICS RS-00-48 Lemma 5.8 «1 ⇒ 2», the direction that holds, applied to Odd's one-player game against a fixed σ)) realises the IDEAL model of L-RED R178 §1 on acyclic Ξ-graphs: an IDEAL genome G has N movers x with levels lev(x), M := Σ deg(x) options (x, k), each with a W-target of level lev(x) − 1 (none at level 0), a Ξ-target that is a mover or X, a distinct β-rank with a parity, a distinct gate index, and a start; under a state s the Ξ-value of option (x, k) is the set of β's on its chain (x, k), (xt, s(xt)), … up to the first Ξ-target X, compared by the β of largest rank in the symmetric difference: the option whose set contains that β is the better one if its parity is even and the worse one if odd; an IDEAL step moves every mover to the lexicographically least key (gate indices of the chain of W-targets under the new state, lowest level first) among its current option and the options with a strictly better Ξ-value, and the run stops when nothing is available or nothing changes, L(G) := its number of steps; the Ξ-graph has an edge x → xt(x, k) for every option with a mover as Ξ-target; for every G whose Ξ-graph is ACYCLIC, the game Γ(G) on n = N + 3M + 6 vertices (Even movers of priority 0; Odd gates of priority 1 with a W-face e and a Ξ-face β; β of priority 6 + 2·rank + parity with edges to the Ξ-target and to u, or to u alone; e of even priority above every β with one edge to the W-target or to the top even self-loop c_W; an unused even self-loop of priority 2; c_W's priority top is the least even number at least 2 above every other priority so far; a closed core u = K0 (Even, top + 2) → {K1, K3}, K1 (Even, 5) → {K0, K1}, K2 (Odd, 3) → {K1, K2}, K3 (Even, top + 3) → {K1, K2}; vertex indices: movers, gates in gate-index order, β-vertices, e-vertices in the order of their gates' gate indices, the unused loop, c_W, K0 to K3 (packet §3.1), on which the root-first key comparison depends) with start σ = the genome start at movers, β → its Ξ-target (u when the target is X), K0 → K3, K1 → K1, K3 → K2, τ = e at every gate and K2 → K2, has an N5 run whose states 0, …, L(G) carry the IDEAL states at the movers, Odd's optimal counterstrategy on the β-face at every gate (strict local preference), τ unchanged (no Odd-improving edge), σ unchanged off the movers, the valuation of the (σ, τ)-play unchanged at every vertex, no fallback before state L(G) and a fallback at transition L(G) + 1, so, if L(G) ≥ 1, [0, L(G)] is one FL run (a maximal set of consecutive non-fallback transitions that keep τ, change σ and keep that valuation everywhere) of length exactly L(G) (no FL run if L(G) = 0) (Theorem REALIZE); hence if every FL run of N5 from every start pair on every n-vertex game has length at most p(n) for a nondecreasing polynomial p, then L(G) ≤ p(3(N + M) + 6) for every acyclic G, and a family of acyclic genomes with L super-polynomial in N + M is a family of real games with super-polynomially long FL runs from the stated start pairs (Corollary REAL-IDEAL): a REDUCTION / NECESSITY statement only; no count is bounded; Ξ-cyclic genomes are not covered, and random Ξ-cyclic genomes do mismatch; nothing about N5's default start S3; the converse is not claimed; DATA: per-lemma checks with 0 violations on the 7 R178 champions (L 17 to 64), 2 R188 genomes, 60 random and 60 perturbed acyclic genomes; pins stab_d4_n126 (06f81991…, L_FL 32), stab_g24_n246 (55295dd8…, L_FL 64), x3_L8_n48 (158ca15d…), g4_L12_n62 (658f4e23…), each with a validated start and checked against Oink 8fbf0a7 --zlk / --tl with verify and two N5 engines (P-N5-REALIZE, docs/red/P-N5-REALIZE.md; L-RED successors 44-45). G-N5-TIME stays open.

Addendum 1 (subagent, for the Lead; does not land; written 2026-11-02T07:14:23Z by date -u). (1) BUILT ON LINE L-1 (l-red 02dfc35c, sha1 1d72ee31…), the
line both referees MATCH (REFEREE 22 5cc6be95; REFEREE-2 26 c9eafef4). NOT committed, NOT pushed; no other tracked file edited. The lane
and referee commits are not on trunk at this fill: merge claude/l-red, claude/referee, claude/referee-2 and push trunk before landing.
(2) TITLE l. 359 = "### R104 [refereed-only] " + L-1 without its newline + ", CHECKER PASS (docs/checker/C115.md, checker
PENDING)", checked by script after the fill (fill104.py): equal, byte for byte (True); the only «### R» heading of this file. (3) BODY
l. 359-593; GAPS preamble l. 595-602; UPDATE l. 603 (one line, 0 "|", one <DATE>, one <HH:MM>, one <checker>; controls
True ×7: R97's-R103's landed UPDATEs). (4) PINS: from a git archive of 03255d5d (experiments/, docs/red/), from experiments/red, GIT_DIR
set: check.sh l. 1-7 + 710-719 + 733-746 07:00:48-07:01:16Z, rc 0; pinck on the four pins and lemck / realck re-prints 07:01:25-07:01:31Z,
rc 0 each; t2.py CLASS=full and the two other --rand rows 07:01:47-07:01:48Z (equal to the packet's numbers). (5) QUOTE SWEEP: q104.py (q103.py's rule: outermost guillemet quotes, whitespace joined, split at the ellipsis, parts of 6+ characters; sources: packet, frozen line at e609c5d2, L-1 at 02dfc35c, fixes at c28583b3, R-N5-REALIZE.md at 5cc6be95, R2-N5-REALIZE.md at a22cf5d8, R2-N5-REALIZE-L1.md at c9eafef4, both L44 files, T21, RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, TARGET.md, SPEC, NOW, R102-draft, R103-draft, C113, C114, check.sh at 03255d5d, my pin / pinck / scope outputs, my UPDATE and word diff, commit subjects): to-check notes l. 1-358: 358 quotes, 315 parts, all found; entry (title + body) l. 359-593: 199 quotes, 195 parts, all found; GAPS preamble and UPDATE l. 595-603: 9 quotes, 6 parts, all found; this Addendum: all found. Found only in my own outputs: the UPDATE head and <DATE> (to-check notes), and two re-run output lines quoted in the entry's Data bullet as my re-run (the pinck line of stab_d4_n126 and the t2.py seed 187 line), as labelled there. Line check: 153 quotes preceded by an l. N, 30 heuristic misses, read by hand: 17 verdict-table cells (the regex takes the packet's or section's line range before the cell's own line number), the DECISIONS-INDEX status words after DECISIONS line ranges, L-1 phrases after the packet's line ranges in the clause checks, the check.sh block names after the line ranges, and the RESULTS name hits in G-10 and (0); none a wrong line.
(6) FLAGS FOR CHECKER (no referee made any REQUIRED): G-1 title shape («revision» in the date parenthesis; fixes file not named); G-2
unglossed xt, X, u before «u = K0», Iσ / σ̄ / τ̄ / σ_new, the root-first key, deg, e-priorities, «super-polynomial»; G-3 «bridge B» and
(R1) without «R103» in the line; G-4 Lead readings CLEAN («before S4c» via L45 / R102); G-5 L41 (G-REAL-1 closures, REAL-P3, R17 (F1));
G-6 [VJ-LOC] = RESULTS R36 (c) on a one-player game, not named (the one I would check first); G-7 DATA («random Ξ-cyclic genomes do
mismatch» before the DATA label); G-8 L43 CLEAN; G-9 stale lane text (entry 2's 05:31Z; entry 2 read by no referee); G-10 names («R104»
as L-RED's box label in RESULTS; unprefixed R178 / R188); G-11 <DATE> (R103 / R102 precedent hardcoded the date); G-12 priorities above
n. (7) NOT RUN / NOT DONE: the referees' own tools (not re-run); the §7 z3 maxima (z3 not installed); check.sh's other blocks and
scripts/verify.sh (not run); scripts/check_docs.py (not run; the heading carries «[refereed-only]»); the Lead's 05:31Z relay (G-9 (i))
not found. Scratch files (not committed) are in /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad:
R104-template.md, assemble104.py, fill104.py, upd104.py / upd104.txt / upd104.out, wdiff104.py / wdiff104.out, pin104.out, pinok104.out,
scope104.out, q104.py / q104.out, arch03255/ (with experiments/red/pin104.sh).
