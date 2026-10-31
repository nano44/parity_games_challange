# Draft RESULTS R99 (Lead, 2026-10-31 18:57:39Z by date -u, read in the same command as the fill of this file; subagent draft; packet, its §11 line draft, line files L-1 / L-2, fixes F0 + entries 1-6, REFEREE's R-N5-STAIR (report, STAIR-L8, §C, L-2 addendum) and REFEREE-2's R2-N5-STAIR, R2-N5-STAIR-L1, R2-N5-L2-confirm read at the origin heads fetched at the start of this draft, 2026-10-31 18:36Z (l-new a82e7c55, referee 45b63517, referee-2 cf5157fe, checker 68c5ea14; origin trunk eb33b45a, local trunk head 2640a8bc); L-NEW's box 107-111 pin blocks of experiments/new/check.sh re-run 2026-10-31 18:40:46Z-18:40:49Z (6903f1b3), three supporting blocks 18:40:49Z-18:40:56Z; DATA re-summed 2026-10-31 18:41:20Z) — to CHECKER C109; REBUILT on line L-3 for C109 Add. 1 (Lead, 2026-10-31 21:33:01Z by date -u; sources at local trunk a250e898; to check (R), Addendum 2) — LANDED in RESULTS Results 2026-10-31 23:12Z (CHECKER C109 Add. 1 81fdf7a5 PASS), after R98
At the rebuild, REFEREE-2 25's STAIR L-3 word diff (claude/referee-2 faa8dac9, docs/referee-2/R2-N5-STAIR-L3.md) is on origin
claude/referee-2 and on the local trunk head a250e898 (merge a20cf406, 21:23:35Z), NOT on origin trunk a8b42b38; every other commit cited
here is on both (cf5157fe is now on origin trunk). R98 is NOT landed (to check (0)). In the body (title + entry), sentences about an
earlier line revision say «at the L-1 object», «at the L-2 object» or «at the §11 draft»; every other sentence of the body describes L-3.
The to-check notes (0)-(14) and the FLAGS were written on L-2 and stand as history except where (R) says otherwise.
(R) REBUILD ON L-3 (for C109 Add. 1; the changes are listed in Addendum 2). CHECKER C109 (claude/checker 178b3e9e) FAILED the L-2 draft
on E-1, E-2, E-3; L-NEW's line L-3 (l-new 7dc1eb7c, docs/new/P-N5-STAIR-line-L3.txt, sha1 9db0b169aadcbc5f81b2c0157f124946bbf74ad9;
fixes entry 7, fixes sha1 6e45b0e0684d06ba9258a466d96bc9829e096218, 214 lines) applies them, and both referees MATCH it (REFEREE 21
d6da0e93, REFEREE-2 25 faa8dac9; body, line history (4)). D-1 to D-4 are RESOLVED by E-1 to E-3: D-1 by E-1 (L-3's tail carries the L41
clause, «referee-originated» once); D-3 by E-2 (L-3 has 0 «H_k»; the gloss reads «S4a's one-player arena at k», k bound by «at a
transition k → k + 1»); D-2 by E-3 option (i) (the DESC-LIN DEAD clause is dropped, Lead reading L43); D-4's clash of «c» is removed with
that clause (L-3 has 0 «c·n»; the «(c, ∅, 0)» precision, C109 N-2, stays optional and unapplied). Scan of L-3 (by script): 0 «DATA», 0
«both», 0 «corpus», 0 «games», 0 «DEAD», 0 «R162», 1 «referee» (in «referee-originated»), eight «every» (unchanged), no count of a data
set. L-3: 4,552 characters (4,683 bytes plus the newline), 899 whitespace tokens, fourteen "|", one «2026-10-31», no heading marker. The
heading is built as in (1) (scratch fill99L3.py: assert the sha1 9db0b169…, one line, no marker, one date, fourteen "|"; prepend «### R99
[refereed-only] », append the same fill) and re-checked after writing: equal, byte for byte; 4,630 characters, 4,761 bytes; sha1 without
its newline f52b2887afabc9dd8a250721dac4043e536c8c27, with it 386a509e95dee867a53eee443f8775ec8d8c8911. Where the notes below say L-2:
in (1) read L-3's figures here; (2)-(3) gain L-3 (body); (4) the twelve claim clauses are unchanged from L-2 to L-3 (the word diff
touches only the gloss, the tail and the count); (6) labels in L-3 (by script): «R57» 1, «R15» 1, «R89» 1, «R91» 1, «R93» 2, «R97» 1,
and no «R162»; (7) the rows H_k, the tail's c, DESC-LIN, L-RED R162 and cp_K are gone; (9) the UPDATE is rebuilt on L-3 (preamble
below the body); (14) the title states no DEAD. RESULTS and GAPS are unchanged at a250e898 (24280f52 / a0b8f8dd, last changed by
9777660f), so (0)'s line numbers stand; check.sh l. 562-591 is identical at a250e898.
to check: FLAGS FIRST, written on L-2 (RESOLVED at L-3, see (R)) (the C108 E-1 scan the Lead asked for: DATA clauses, «both referees», «every», counts; details in (7) D-1 to D-4).
- No DATA clause: L-2 has 0 «DATA», 0 «both», 0 «referee», 0 «corpus», 0 «games» and no count of any data set (by script). Its eight
  «every» are the global binder («every N5 run on every game, every W-run F = [p, q] of it, every transition k → k + 1 of F, every vertex v
  and every bit position b») and the signed statements of FIRST-GOOD («every change of W(v) on F») and RESET-ROOT («every reset of W(v)
  at k»). So the C108 E-1 pattern (a DATA sentence that overstates what the referees' tools checked) does NOT occur in this line.
- FLAG D-2 (the one evidence-bearing clause of the tail): «DESC-LIN (DESC_F ≤ c·n) DEAD (L-RED R162, claude/l-red 54832628: passive
  observers, cp_K)». It is literally what L-RED R162 says and names L-RED as its source; it claims no referee check. But the DEAD is
  LANE-LEVEL: R162 is not landed (RESULTS 0 «R162»); REFEREE did not re-run it (STAIR-L8 «I have not re-run R162; this item relies on the
  Lead's relay.», §C l. 199 «Entry 4 relies on R162 as reproduced by REFEREE-2 and L-NEW. I have not re-run it.»); REFEREE-2 re-ran ONE
  member of each family (cp_K4: n 192, DESC 388, DESC/n 2.02; suf_K4) and wrote «DESC grows past any c·n while |F| stays at 44: DESC-LIN
  is DEAD as R162 says.» — the growth in K (DESC/n 4.02, 6.02, 8.02 at K = 8, 12, 16) is R162's own table, not re-run by a referee, and
  only cp_K4 of the cp family is committed. A single cp_K4 does not by itself exceed a c·n bound. Precedent R90 / R95 put lane DEADs in
  titles the same way (one named instance each). CHECKER decides whether the clause stands as worded (it is a scope-tail word, not a signed
  item) or wants wording that says the DEAD is lane-level (R162; cp_K4 reproduced by REFEREE-2). Not changed by me: the title equals L-2.
- FLAG D-1 (Lead reading L41; not a DATA clause, but the same class: the scope tail must say what the record is): L-2 states COPY in BOTH
  directions, and DESC-COPY's proof needs the converse. The converse's proof text is REFEREE's G-ST-1 closing argument (R-N5-STAIR.md
  §6 l. 67-74), written independently also by REFEREE-2 (R2-N5-STAIR.md §3 l. 71-78) and adopted by fixes entry 1; both sign it. L41 asks
  that the scope tail «says the proof is referee-originated». L-2 has 0 «referee-originated» and neither referee asked for it (REFEREE §C
  l. 177-178 ✓; REFEREE-2 L1 l. 19 «✓ applied»). Compare R98's line, whose tail names G-ODD-1 (also written by both) as a referee-originated
  repair. Counter-reading: the same converse is lane-proved too, as Lemma COPY⁺ of L-NEW box 113 (fixes entry 1 l. 62-63, «lane level and
  not part of this packet»), not refereed here. CHECKER decides whether L41 needs a line L-3; the body records the repair and both
  signatures (G-ST-1 bullet, Honest limits (iv)).
- Soft spots, symbol test: D-3 H_k is free in L-2's R57 gloss (R96 / R97 define it in the title, L-2 nowhere); D-4 «c» in «DESC_F ≤
  c·n» is unbound and is also the cycle node of «(c, P, ℓ)»; «C-vertices keep the value (c, ∅, 0)» (REFEREE-2's optional precision, not
  applied).
(0) PLACEMENT, R98 PENDING. R99 goes after R98. R97 is LANDED (trunk 9777660f, 2026-10-31 07:02:34Z; CHECKER C107 449cb6fc PASS). R98
is NOT landed: its draft docs/agents/R98-draft.md (sha1 78a795621c64677b220b658e086c40343436bed1, 531 lines, last commit 753ae44e,
17:32:03Z) FAILED CHECKER C108 on E-1 (claude/checker 68c5ea14, 18:03:13Z: «A DATA sentence in a landed title must be literally true.»),
and L-SI's ODD line L-3 is coming (LEAD-STATE 18:36Z), so R98 lands with a later line. docs/RESULTS.md at the local trunk head 2640a8bc
(RESULTS identical at origin trunk eb33b45a) has sha1 24280f5226c8616b9de88ee16eaf86c727f4a135, 8,816 lines, last changed by 9777660f
(the R97 landing). «### R97» is l. 8032 (entry l. 8032-8294, l. 8295 blank); «## Dead ends (kept;» is l. 8296; «### R98» and «### R99»
occur 0 times; «R99» occurs twice in RESULTS, both L-RED's own R99 (l. 4504 «repaired them in R99», l. 4505
«docs/red/R99-start-erratum.md»), and 0 times in GAPS (sha1 a0b8f8dd4c0fa8538cd21e54ed2d3822f28d9182, 23 lines, last changed by
9777660f). Every RESULTS line number in these notes and in the entry is at 24280f52, BEFORE R98 (as R97's draft did while R96 was
pending); R98's insertion goes after l. 8295, so no RESULTS line number cited here moves. R99's entry goes after R98's entry and its blank
line, before «## Dead ends (kept;», with one blank line after it (R97's layout). The Lead RE-CHECKS (6) (labels and names, with R98 in)
and (9) (GAPS, after R98's UPDATE) at landing.
(1) TITLE. The title is the line file docs/new/P-N5-STAIR-line-L2.txt (l-new 6903f1b3f57f461088866070429e58ad272193fe,
2026-10-31T16:14:21Z, the file's only commit, sha1 44f56e96d41d45653c4b7bc2f140c587e8e407e6; identical at l-new head a82e7c55, at origin
trunk eb33b45a and at the local trunk head 2640a8bc; first on trunk by merge 1b159f51, 17:31:52Z), verbatim: one line, no outer quotes,
no final period, 4,452 characters (4,586 bytes plus the newline), 887 whitespace tokens. NO HEADING MARKER, verified by script: the file
begins «N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise», with no «#», no «R??» and no lane tag (Lead reading L41 «Lanes
write line files without a heading marker (C104 N-1).»; REFEREE-2 STAIR-L2). So, as in R95-R98, NOTHING is stripped: the heading is the
level-3 marker, then "R99 [refereed-only] ", then the file without its newline, then the fill. «2026-10-31» occurs exactly once in L-2, in
« (2026-10-31) — REDUCTIONS and EQUIVALENCES» (by script), so NO date is inserted (the R93-R98 rule). The line holds fourteen "|": «|V|»
once and «|F|» six times; they stay in the heading (R91, R93-R98 carry "|") and are replaced in the GAPS UPDATE only ((9)). The checker
fill ", CHECKER PASS (docs/checker/C109.md, checker PENDING)" is appended as in R90-R98 (no space before the comma); L-2 ends «…
entries 1-6)», so the heading ends «… entries 1-6), CHECKER PASS (…)». Built by script (scratch fill99.py: assert the sha1 44f56e96…,
one line, no marker, one «2026-10-31», fourteen "|"; prepend "### R99 [refereed-only] ", append the fill) and re-checked after writing
this file: equal, byte for byte. Heading: 4,530 characters, 4,664 bytes; sha1 of the heading line without its newline
5624be41bac8a5fdd088ffc7b32541c13826e1ca, with its newline e6ba97ef315102a4a41c50a15daea298faded232.
Title features shared with landed titles (no new precedent): the scope words «REDUCTIONS and EQUIVALENCES» (R95, RESULTS l. 7476); a lane
DEAD in the scope tail with the lane's note number (R90 «CONJECTURE REP-LIN is DEAD (L-RED R128, latew_K20_m32)», R95 «CONJECTURE
BIP-REL-1 is DEAD (L-RED R143, rel2_R2_n82, l-red 717f407a)»); a source parenthesis after the scope tail «(P-N5-STAIR,
docs/new/P-N5-STAIR-box112.md; L-NEW successors 41-42; fixes docs/new/P-N5-STAIR-fixes-box112.md entries 1-6)» (R97: «(P-N5-SRC,
docs/red/P-N5-SRC.md; L-RED successor 35; fixes docs/red/P-N5-SRC-fixes.md entries 1-5)»); landed entries cited by number (R57, R15,
R89, R91, R93, R97). NEW in a title, for CHECKER: (i) the DEAD names a FAMILY («cp_K») and a commit, not one instance with its sha1 (R90 /
R95 name one instance; D-2); (ii) a premise whose text is another lane's packet section, «[PLAY] := P-N5-SRC §2 (proof of RESULTS R97
PLAY-CAUSE^S)» (R98's draft title has the same kind, «(P-N5-SRC §2, the signed proof of RESULTS R97 PLAY-CAUSE^S)»; R98 is not landed);
(iii) no «referee-originated» clause although COPY's converse rests on a referee-written repair (D-1).
(2) LINE HISTORY: the packet's §11 draft (l. 178-188: a bulleted multi-line draft with the marker «R?? [refereed-only]», 189 whitespace
tokens; the line both reports reviewed) → L-1 d027f5d8 (docs/new/P-N5-STAIR-line-L1.txt, l-new 360d002f, 14:31:28Z, 4,414 characters,
880 tokens, fourteen "|", no marker, one date; with fixes F0 + entries 1-5) → L-2 44f56e96 (…-line-L2.txt, 6903f1b3, 16:14:21Z, 887
tokens; fixes entry 6). The §11 draft and L-1 are history, not the title. Each line file has one commit (git log on l-new). Word diffs
measured for this draft (difflib over whitespace tokens, scratch wdiff99.py):
- §11 draft → L-1: 189 → 880 tokens, 33 non-equal opcodes, 96 tokens in common: a REWRITE, not a token edit. Both referees checked L-1
  clause by clause: REFEREE §C l. 163-164 «L-1 is a rewrite rather than a token edit, so I checked it clause by clause against my
  STAIR-L1..L8, the signed statements, and the fixes entries.»; REFEREE-2 R2-N5-STAIR-L1.md l. 7 «L-1 is a rewrite, so I check it clause
  by clause against the signed items, not token by token.» Fixes F0's item map (l. 17-38) sends every referee item to its place in L-1.
- L-1 → L-2: 880 → 887 tokens, 3 non-equal opcodes: «it and» → «it,»; «F:» → «F, every vertex v and every bit position b:»; «1-5)» →
  «1-6)». = fixes entry 6 l. 154-156; = REFEREE §C addendum l. 205-206 (the same three, «Nothing else changed.»); = REFEREE-2
  R2-N5-L2-confirm.md l. 12-15 («(d027f5d8; 880 → 887 tokens): exactly the Lead's list, nothing else.»).
- §11 draft → L-2, by content (F0's map): the O-ARENA clause and [S4b-OPT] dropped (STAIR-L1 at both, L42); every symbol defined in the
  line (|F|, q, CS, A_k, N_F, β, TD_F, first-difference position, DESCENT; REFEREE STAIR-L2 to L5 and L7, REFEREE-2 STAIR-L3); the clause
  «(COPY, RESET-ROOT, DESC-COPY) resets and descents are copied from switched vertices» replaced by the signed statements of RESET-ROOT
  and DESC-COPY (REFEREE STAIR-L6 = REFEREE-2 STAIR-L4); COPY in both directions (G-ST-1 = P-1, entry 1); RESET-ROOT «before λ_W(v)»
  (P-2, entry 2); the converses of RESET-RED and STAIR (REFEREE's precision); Fact BIT and BW-ACC's «T1_F ≤ N_F ≤ |F|» stated; «HDEPTH is
  DEAD (hit_b6a_1)» dropped (REFEREE-2 STAIR-L5); «DESC-LIN is a CONJECTURE» → «DESC-LIN (DESC_F ≤ c·n) DEAD (L-RED R162, claude/l-red
  54832628: passive observers, cp_K)» (REFEREE STAIR-L8 = REFEREE-2 STAIR-L6, entry 4); the global binder (REFEREE STAIR-L7, then
  STAIR-L9 = REFEREE-2 STAIR-L1-1 in L-2); the source parenthesis. No inequality of a signed statement differs between the packet and L-2
  ((4) checks each clause).
(3) THE LINE AT BOTH REFEREES. L-2 (the title): REFEREE successor 21, docs/referee/R-N5-STAIR.md «### §C addendum: line revision L-2
(l-new 6903f1b3, docs/new/P-N5-STAIR-line-L2.txt, sha1 44f56e96d41d45653c4b7bc2f140c587e8e407e6; fixes sha1 52fd8b50…, entry 6) (16:43Z
2026-10-31 by date -u)» l. 204-209 (45b63517, 16:43:29Z, +7/−0): l. 206 «Both sha1s are re-hashed and match.»; l. 207-208 «STAIR-L9 is
met. v and b are now in the quantifier,»; l. 208 «No new symbol is introduced.»; l. 209 «Verdict on L-2: MATCHES (Opus 5.5, D15). No
REQUIRED change remains on the P-N5-STAIR line.» REFEREE-2 successor 24, docs/referee-2/R2-N5-L2-confirm.md §(2) l. 11-19 (cf5157fe,
16:43:27Z, new file, 19 lines, sha1 85d3a211503954ab4ffec91be08827122f0d0b49; its §(1) l. 4-9 is the ODD L-2 confirmation, not this
entry): l. 11 «(re-hashed: match)»; l. 16 «My STAIR-L1-1 (= REFEREE's STAIR-L9) is met:»; l. 17 «No new free symbol.»; l. 19
«**MATCHES** (Opus 5.5, D15). STAIR-L1-1 is CLOSED. All my STAIR line items are closed.»; l. 2 «Both written without opening REFEREE's
verdicts.» 45b63517 is on origin trunk (merge 1b159f51); cf5157fe is on the local trunk only (header): the Lead pushes trunk before landing.
L-1: REFEREE §C (ad4e7ebc, 15:17:13Z, +46/−0) l. 158-202: STAIR-L1..L8 met (l. 165-172); l. 186 «REMAINING free symbols: STAIR-L9
(REQUIRED).»; l. 201-202 «Verdict on L-1: does NOT yet match, only because of STAIR-L9 (v and b unquantified), a one-phrase insertion.
Everything else MATCHES (Opus 5.5, D15).» REFEREE-2 R2-N5-STAIR-L1.md (6f45b443, 15:17:35Z, new file, 57 lines): l. 54-55 «**DOES NOT
MATCH yet, one REQUIRED change STAIR-L1-1** (bind v and b in the global binder)», «Everything else MATCHES»; l. 32 «**I SIGN Entry 1's
repair** (Opus 5.5, D15).» The referees AGREE on L-1 (one required item, the same phrase): fixes entry 6 l. 159 «The two required
items are one change, and the fix phrase is identical in both reports. L-2 makes exactly that change.» REFEREE records v and b as its miss
at the §11 draft (§C l. 191-192 «It is my miss, not a change made by L-1.»); REFEREE-2's report did not list them either (its STAIR-L3
binds «q, CS, N_F, β, q_j») and raised them on L-1.
§11 draft: REFEREE l. 24 «REQUIRED CHANGES STAIR-L1 to STAIR-L7 (§10)» (the table row, not updated by a61a258b) and §10 l. 146 «It needs
STAIR-L1 to STAIR-L8.»; REFEREE-2 l. 26 «REQUIRED changes STAIR-L1 to L6 (§5)», l. 182 «Line draft: REQUIRED STAIR-L1 to STAIR-L6.»
LINE-ITEM NAMES CLASH: each referee numbers its own items. REFEREE STAIR-L1 = REFEREE-2 STAIR-L1 (O-ARENA, [S4b-OPT]); REFEREE STAIR-L2
(|F|), L3 (q, CS(v)), L4 (N_F, A), L5 (β, TD_F) and L7's «descent» ⊂ REFEREE-2 STAIR-L3; REFEREE STAIR-L6 = REFEREE-2 STAIR-L4 (state
RESET-ROOT and DESC-COPY); REFEREE STAIR-L8 = REFEREE-2 STAIR-L6 (DESC-LIN DEAD); REFEREE STAIR-L9 = REFEREE-2 STAIR-L1-1 (v, b); REFEREE-2
STAIR-L2 (no heading marker, one line) and STAIR-L5 (HDEPTH) are REFEREE-2's (REFEREE lists the marker as a precision, l. 143, and accepts
the HDEPTH drop, §C l. 181); REFEREE STAIR-L7's binding of F and k is REFEREE's. Fixes F0 l. 17-38 maps each. The entry writes «REFEREE
STAIR-Ln» / «REFEREE-2 STAIR-Ln».
(4) CLAIMS SIGNED = the items below, each SIGNED in BOTH referees' verdict tables (REFEREE "## Verdicts" l. 12-24 of R-N5-STAIR.md;
REFEREE-2 "## 1. Claims table" l. 11-27 of R2-N5-STAIR.md and its "## Verdict (Opus 5.5, D15)" l. 178-183), AND stated by L-2 (checked
clause by clause against the packet statements for this draft):
| item (packet §, lines) | REFEREE (successor 21) | REFEREE-2 (successor 24) |
| --- | --- | --- |
| (a) Lemma SANDWICH (§3, l. 51-55; statement l. 51-52) | l. 17 «SIGNED»; §3 l. 38 «SANDWICH ✓.» | l. 15 «SIGNED» / «none»; §3 l. 44-46; l. 179 |
| (b) Corollary FROZEN (§3, l. 56-63; statement l. 56-60) | l. 17 «Lemma SANDWICH; Corollary FROZEN (BW, AF, LS)»; §3 l. 42 | l. 16 «SIGNED» / «none»; §3 l. 47-51; l. 179 |
| (c) Lemma BW-ACC (§4, l. 67-78; statement l. 68-72) | l. 18 «SIGNED»; §4 l. 45-48 | l. 17 «SIGNED» / «none»; §3 l. 52-56; l. 179 |
| (d) Fact BIT, Lemmas BIT-ALT, FIRST-GOOD (§5, l. 86-91) | l. 19 «Fact BIT; Lemmas BIT-ALT, FIRST-GOOD; Theorem RESET-RED (equivalence)» «SIGNED»; §5 l. 51-57 | l. 18 «SIGNED» / «none»; §3 l. 57-64; l. 179 |
| (e) Theorem RESET-RED, an EQUIVALENCE (§5, l. 92-97; statement l. 92-93) | l. 19 (same row); §5 l. 58-59 | l. 19 «Theorem RESET-RED (both directions)» «SIGNED» / «none»; §3 l. 65-68 |
| (f) Lemma COPY (§6, l. 100-111; statement l. 101-107), in L-2's two-way form | l. 20 «SIGNED, with proof-text gap G-ST-1 closed here (§6). The statement is unaffected»; §6 l. 62-74; §C l. 177-178 | l. 20 «SIGNED» / «none (precision P-1)»; §3 l. 69-81; L1 l. 32 (entry 1's repair SIGNED) |
| (g) Corollary RESET-ROOT (§6, l. 112-117; statement l. 112-114), with «before λ_W(v)» | l. 21 «Corollaries RESET-ROOT, DESC-COPY» «SIGNED (DESC-COPY uses COPY's converse, G-ST-1)»; §6 l. 75-80; §C l. 179-180 | l. 21 «SIGNED» / «none (precision P-2)»; §3 l. 82-90; L1 l. 20 |
| (h) Corollary DESC-COPY (§6, l. 118-125; statement l. 118-121) | l. 21 (same row); §6 l. 81-84 | l. 22 «SIGNED» / «none»; §3 l. 91-94 |
| (i) Lemma ASC-RUN (§7, l. 128-133; statement l. 128-129) | l. 22 «Lemma ASC-RUN; Theorem STAIR (equivalence)» «SIGNED»; §7 l. 87-88 | l. 23 «SIGNED» / «none»; §3 l. 95-98 |
| (j) Theorem STAIR, an EQUIVALENCE (§7, l. 134-143; statement l. 135-138) | l. 22 (same row); §7 l. 89-93 | l. 24 «Theorem STAIR (both directions)» «SIGNED» / «none»; §3 l. 99-103 |
Both lists of signed items, verbatim: REFEREE l. 151 «Every item to sign (L42 list) is SIGNED. G-ST-1 (COPY's converse, used by
DESC-COPY) is closed here. Nothing is FALSE.»; REFEREE-2 l. 179 «SIGNED: SANDWICH, FROZEN, BW-ACC, BIT, BIT-ALT, FIRST-GOOD, RESET-RED,
COPY, RESET-ROOT, DESC-COPY, ASC-RUN and Theorem STAIR.»; fixes F0 l. 11 the same twelve.
Clause checks (L-2 against the packet): (a) the first sentence of l. 51-52 with «≤» for the lexicographic order of sequences; the «In
particular» consequence not stated. (b) the three monotonicities and the range of l. 56-60; LS is written out, not named. (c) l. 68-69's
bound; «T1_F ≤ N_F ≤ |F|» is l. 70-72 («Every W-constant transition is in N_F» and «Conversely N_F ≤ |F|»); the POLY reading not stated.
(d) l. 86 with «<_lex» spelled out; l. 90; l. 91 («β-bit» for «bit»). (e) l. 92-93. (f) WIDER THAN THE FROZEN STATEMENT, as signed: the
packet's COPY states one direction (l. 105-106 «Hence every flip of W(v) at k is a flip of W(z) at k in the same direction, and the
first-difference position map is strictly increasing.»); L-2 states «the same flips at k, in the same directions, through a strictly
increasing position map», which is fixes entry 1's repaired statement (l. 55-56), signed by REFEREE (§C l. 177-178 «That is G-ST-1's
repair (entry 1) ✓.») and REFEREE-2 (L1 l. 32; its own report §3 l. 76 «So the non-constant bits of v and z correspond bijectively and
in order,»). The hypothesis «has the same successor z at k and at k + 1», with L-2's «v's successor at k is σ_k(v) for Even v and τ(v)
for Odd v», is l. 101-102. (g) l. 112-114 with «before λ_W(v)» (P-2, entry 2) and «copied, through COPY,» (REFEREE §6 l. 79 «The reset
maps to a reset of W(y) (same direction, injective position map).»; REFEREE-2 §3 l. 86). (h) l. 120-121: «did not switch at any
transition from its previous change of W(v) on F to k» is «[k′, k] (k′ := v's previous change)»; «its successor at k» is z. (i) l. 129's
bound only; «q_(j+1)(v) ≠ q_j(v)» not stated. (j) l. 136 and l. 138's first inequality; the POLY reading and Ψ not stated. Nothing in L-2
is wider than signed; the one clause wider than the frozen statement, COPY's converse, is signed by both as entry 1's repair.
Signed by both, NOT stated by L-2, so NOT landed: SANDWICH's «In particular», ASC-RUN's q-inequality, the POLY readings, Ψ_k, π_v's
formula. Not signed, so NOT landed: O-ARENA ((L42), below); the A_k remark (l. 64-65 «Remark (not signed)»); Corollary RESET-STAIR (l.
144, «not a new count»; REFEREE §8 l. 96 lists «the RESET-STAIR remark» as not to sign); §8 DEADs and DATA, §9 erratum, §10 DESC-LIN.
L41 (D-1): the repair of G-ST-1 is referee-originated proof text: REFEREE wrote it as its closing argument (§6 l. 67-74, «(a proof-text
gap in COPY, CLOSED here; the statement is unaffected)»), REFEREE-2 wrote the same bijection independently (§3 l. 71-78; independence l.
4; 8afe203a 12:55:35Z, before REFEREE's 3c40dc18 13:15:00Z) and treated it as precision P-1; fixes entry 1 adopts it («Proof: the
packet's COPY proof, plus REFEREE's two constancy facts above.», l. 57). Signatures: REFEREE (its own report; §C l. 177-178) and REFEREE-2
(L1 l. 32 «**I SIGN Entry 1's repair** (Opus 5.5, D15).»). So both signatures and the joint gap map (G-ST-1 = P-1, CLOSED) exist and are
quoted in the body; what L41 also asks, «whose scope tail says the proof is referee-originated», L-2 does not do. Flagged, not changed.
(5) OTHER LANES' TEXTS THE ENTRY DEPENDS ON: [PLAY] (packet l. 36-37): the packet restates it in a fixed-cycle-node form,
«Φ(y; (c, P, ℓ)) = (c, P ∪ {y if y is more relevant than c}, ℓ + 1)», and cites P-N5-SRC §2 (l-red 0521fb82, §2 l. 56-82 per RESULTS
R97 (a), l. 8082), the proof both R97 referees signed; «P-N5-SRC §2» occurs 0 times in RESULTS. REFEREE l. 33-34 «needs y ≠ c. Every use
has y ∉ C (COPY), so it is fine.»; REFEREE-2 l. 38-39 «COPY satisfies this: v ∉ C, and z's W-path to c avoids v.» L-RED R162 (the
DEAD clause): docs/red/R162-desc.md @ 54832628 (the file's only commit, 160 lines, sha1 23a43c9a259856da5dd15328b979c7131606b85e; not
landed): l. 3 «DESC-LIN: DESC_F ≤ c·n for every W-run F.»; l. 18 «DEAD: DESC-LIN, in both readings.»; l. 20 «DESC = K·(n_base + 1) =
2.02n, 4.02n, 6.02n, 8.02n at K = 4, 8, 12, 16, i.e. ≈ n²/88.»; l. 23 «|F| does NOT grow.»; faithfulness l. 14 «on all three pins
suf_K4, suf_K8 and cp_K4». Only cp_K4 of the cp family is committed (experiments/red/desc/instances: cp_K4, suf_K4, suf_K8, later fbg and
sbq2 files); cp_K8-K16 are mkcopy.py outputs in R162's table. Start validity: L-RED's scan docs/red/D-ODD-1-starts.md (81a754cc) §(2)
«All other 131 start files are valid.» (its bad files are sbq2, fbg, n3 and n3/out starts, not desc/cp_K4 or suf_K). Reproductions:
REFEREE-2 §4b (cp_K4, suf_K4); L-NEW box 113 (check.sh l. 592-597 «cp_K4 switch-site U not passive-proof (388)», re-run PASS here,
(Data)). L-NEW's box notes are history only (packet l. 5-6 «This packet restates everything it uses; the notes are not needed to check
it.»).
(6) PREMISE LABELS (stale-label test; RESULTS at 24280f52 = trunk 2640a8bc). RESULTS labels in L-2 (by script): «R57» 1, «R15» 1, «R89» 1,
«R91» 1, «R93» 2, «R97» 1; «P-N5-SRC §2» is another lane's packet section; «R162» is L-RED's own numbering (written «L-RED R162»), not a
RESULTS label. Every RESULTS label exists and carries the named item:
- R57 (l. 2893): L-2's gloss «1E-N3: S1's procedure realises the pointwise optimum; for S4a at a transition k → k + 1, σ_(k+1) is the
  pointwise optimum of the one-player arena H_k» is verbatim R97's title (l. 8032, by script; R91 / R93 / R95 / R96 carry the «σ_new» or
  «σ_(t+1)» form with «H_t := S4a's arena at t» inside the gloss). R96 / R97 define H_k in their titles («H_k := S4a's arena at k (Even v
  keeps {σ_k(v)} ∪ Iσ_k(v), Odd follows τ)», l. 8032); L-2 does not (H_k occurs once in L-2; D-3). The S1 half is R57 (b) l. 2915-2916
  («that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance»); the S4a half is Lead reading L42's reading of R57
  («R57's standing SPEC premise (1E-N3) covers S1's procedure and S4a (σ_(k+1) is the pointwise optimum of H_k).»). No signed item uses
  it directly: REFEREE l. 35 «[1E-N3] is not used directly in §3-§7, only through R91.» L42 bites only on O-ARENA (withdrawn).
- R15 (l. 624): (a) Lemma A l. 631 («Ωσ ⊴ Ω_{Switch_I(σ)}»), (d) l. 640; the packet's [R15a] (l. 31) «Ξ_(k+1) ⊵ Ξ_k pointwise at every
  S4a step» (FROZEN's AF and LS; BW-ACC's W-constant step), as R96 / R97 read it; REFEREE l. 27 «[R15a] ✓ (as in R-N5-ODD §1).»
- R89 (l. 5854): «a W-run := a maximal run of consecutive states of one τ-stretch none of whose transitions is an S4c fallback or changes
  λ_W» (by script); L-2's gloss «(a maximal run of consecutive states of one τ-stretch none of whose transitions is an S4c fallback or
  changes λ_W, the cycle-node map of W)» is verbatim R96's and R97's (l. 7748, l. 8032). «W_k := the [S1-val] valuation of the (σ_k,
  τ)-plays» is verbatim R96 / R97; «[S1-val]» is R89's notation (l. 5854 «W_t := the [S1-val] valuation of the (σ_t, τ_t)-plays»).
- R91 (l. 6384): the title's «(Lemmas XW, W-MON, FB-W, OPT-OFF, W-SUCC) Ξ_t ⊴ W_t pointwise, W does not fall at an S4a step (read with
  τ_t)» (by script). On a W-run every transition is an S4a step with τ fixed: REFEREE l. 29-30, REFEREE-2 l. 33-34.
- R93 (l. 6972; (a) l. 7031-7036): Fact LEX with «CS(x) := (rew(c); s_{n−1}, …, s_0; ℓ̂)» (l. 7033) and «x ◁ y iff CS(x) < CS(y)
  lexicographically» (l. 7034), length 1 + n + 1 = n + 2 as L-2 says; REFEREE l. 31-32; REFEREE-2 l. 35-37 (citing R93's title).
- R97 (l. 8032, LANDED 9777660f): «(a) Lemma PLAY-CAUSE^S (§2, l. 56-82)» (l. 8082); [PLAY] is that proof (5).
- Name check against landed text (RESULTS / GAPS at 24280f52 / a0b8f8dd, by script, word boundaries): «SANDWICH», «BW-ACC», «Fact BIT»,
  «BIT-ALT», «FIRST-GOOD», «RESET-RED», «COPY», «RESET-ROOT», «DESC-COPY», «ASC-RUN», «STAIR», «DESC-LIN», «R162», «P-N5-STAIR», «BW_k»,
  «AF_k», «A_k», «N_F», «TD_F», «DESC_F», «WCT_F», «T1_F», «GOOD_F», «BAD_F», «DESCENT», «lcp» and «cp_K» occur 0 times in both.
  «FROZEN» occurs twice in RESULTS, neither a claim name (l. 5858 the status word «DRAFT → FROZEN»; l. 7554 «A FROZEN STRETCH Φ»); «BIT»
  5 times, each another lemma's name (Lemma BIT, l. 2567-2756); «RESET» once (l. 5014, the DATA count «RESET 133 of PCH 157»);
  «first-difference position» once (l. 8319, a Dead-ends row). «WCH_F» occurs 33 times in RESULTS and 13 in GAPS with the SAME meaning
  for WCH_F(z) (l. 6656 «WCH_F(z) those changing W(z)»; there WCH_F without argument is the W-changing transitions, L-2's WCT_F); «CS» is
  R93's. None is inside a claim of the title with a different meaning. AT LANDING: re-run the grep for «### R99» (0), «R99» (2, L-RED's)
  and the names above with R98 in.
(7) SYMBOL TEST of the title (my own strict test of every symbol of L-2, by hand; IN = bound in the line; else the carrier):
| symbol | where |
| --- | --- |
| N5, SPEC S1-S5, «Even», «Odd», S4a, S4c | SPEC (named) |
| standing SPEC premise of RESULTS R57; R15 (a), (d); R91; R93; [PLAY] | cited; see (5), (6) |
| R57 gloss: k, σ_(k+1); H_k | k, σ_(k+1) IN («for S4a at a transition k → k + 1»). H_k: NOT bound in L-2 (D-3) |
| run, states (σ_k, τ_k), transition k → k + 1, «y switches at k» | IN |
| n, V | IN («n := \|V\| (V the vertex set of the game)»); = TARGET.md §1 l. 8 «n = \|V\|» (REFEREE-2 l. 167) |
| values (c, P, ℓ), ⊴, ◁, ⊵, ▷ | IN («as in SPEC S1», «the SPEC S1 order (better for Even)») |
| Ξ_k | IN («Ξ_k := Ξ_{σ_k} (SPEC S1)») |
| W-run F = [p, q], τ-stretch, λ_W, τ, C, \|F\| | IN (R89's gloss; «C := {v : λ_W(v) = v} fixed on F»; «\|F\| := q − p») |
| W_k, [S1-val], «v's successor at k» | IN («for a state k of F, W_k := …»); [S1-val] R89's notation (6) |
| T1_F, WCT_F, WCH_F(v) | IN |
| CS(x), lcp, BW_k, AF_k, A_k, N_F | IN (CS «RESULTS R93 (a)'s coordinate sequence»; the rest defined) |
| β(x), r, sl, j | IN («for a value x = (c, P, ℓ), β(x) ∈ {0, 1}^(3n + 1) consists of …») |
| GOOD_F(v, b), BAD_F(v, b), RESET, TD_F | IN |
| first-difference position, DESCENT, DESC_F(v), DESC_F | IN |
| global binder: run, F, k, v, b | IN («for every N5 run on every game, every W-run F = [p, q] of it, every transition k → k + 1 of F, every vertex v and every bit position b») |
| SANDWICH: x, y, z | IN («for sequences x, y, z of one length») |
| FROZEN: end | IN («end its last state») |
| BW-ACC: M | IN («with M := n(n + 2) + 1») |
| Fact BIT: x, y | IN («for values x, y with one cycle node») |
| COPY: z; «C-vertices keep the value (c, ∅, 0)» | z IN («the same successor z»); c: the generic cycle node, read as each c ∈ C (REFEREE-2 L1 l. 49-50 precision, optional, not applied; D-4) |
| RESET-ROOT: y | IN («where y is the first Even vertex switched at k on v's (σ_(k+1), τ)-play before λ_W(v)») |
| scope tail: DESC-LIN, c, G-N5-TIME, M3, step-4, TARGET.md, L-RED R162, cp_K | DESC-LIN named with its statement; c NOT bound (D-4); GAPS l. 11, TARGET.md; R162 (5) |
Agreeing tests: REFEREE §C l. 182-185 (bound list; «end»), l. 186-190 (STAIR-L9), addendum l. 207-208; REFEREE-2 L1 §3 l. 39-51, L2
confirm l. 16-17. Neither lists H_k or the tail's c as bound or free.
DOUBTS for CHECKER (D-1 and D-2 are the FLAGS at the top; D-3, D-4 soft spots; no referee raised any of them as REQUIRED; no change
proposed by me):
D-1 L41 tail clause for G-ST-1's referee-originated repair absent ((4) «L41»).
D-2 the DEAD clause rests on lane-level evidence ((5); FLAGS).
D-3 H_k free in the R57 gloss. No claim of L-2 uses H_k; the gloss is a premise, not a claim. R96 / R97 define it; an L-3 could add «H_k
:= S4a's arena at k (Even v keeps {σ_k(v)} ∪ Iσ_k(v), Odd follows τ)» as R97 does.
D-4 «c» in the tail's «DESC_F ≤ c·n» (the conjecture's constant; the packet l. 176 and R162 l. 3 write it the same way) and the generic c
of «(c, ∅, 0)»; neither is inside a signed claim's inequality.
(8) FIXES AND STATUS NOTES (fixes file at 6903f1b3, sha1 52fd8b500266d6ca5615e239fb621f56249ff1f0, 159 lines; = l-new head a82e7c55 =
trunk; recorded under Fixes): F0 and entries 1-6, two commits, each +N/−0: 360d002f (14:31:28Z, new file, 136 lines, F0 + entries 1-5;
the file then sha1 f07676f47f51ba991015b4e43d4406da4add57a4, which both referees re-hashed: REFEREE §C l. 161, REFEREE-2 L1 l. 5) and
6903f1b3 (16:14:21Z, +23/−0, entry 6). The fixes file's quotes were checked for this draft by script: entry 1's REFEREE block (l. 42-49)
= R-N5-STAIR.md l. 67-74; entry 1's REFEREE-2 block (l. 51-53) = R2-N5-STAIR.md l. 79-81 and entry 2's (l. 67-69) = l. 88-90 (equal up
to the outer indentation); entry 6's REFEREE block (l. 141-145) = R-N5-STAIR.md l. 186-190; entry 6's REFEREE-2 block (l. 147-152) =
R2-N5-STAIR-L1.md l. 42-47. Entry 4 l. 127 «Reproduced by REFEREE-2 (R2-N5-STAIR §4b: cp_K4 DESC 388, suf_K4 DESC 28, |F| 44) and by L-NEW
box 113 (cp_K4 388).» = R2-N5-STAIR.md l. 135-136 and check.sh l. 594 (REFEREE-2 L1 l. 33 «Entry 4 (DESC-LIN DEAD): ✓, with my §4b
reproduction quoted correctly.»). F0 l. 14 gives L-1's sha1 as «sha1 in the commit message and the message to the Lead»; measured here
((2)). F0 l. 9 cites REFEREE-2's report as «claude/referee-2 f92b278a», the commit that ADDED STAIR-L6 and §4b; the report's first commit
is 8afe203a ((13)).
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-2 states no CONJECTURE (it reports DESC-LIN DEAD). A line-11 UPDATE is proposed at the end,
to go AFTER R98's UPDATE (PENDING: R98-draft l. 526, to be rebuilt from ODD L-3; at 2640a8bc the last UPDATE on l. 11 is R97's «UPDATE
2026-10-31 07:02Z: RESULTS R97 (P-N5-SRC; CHECKER C107 449cb6fc) …», ending «G-N5-TIME stays open.» before the row's closing « |»; l. 11
holds 76 "|"), as a pure insertion with one separating space. Built by script (scratch upd99.py) from L-2's clauses only, with R94's-R98's
construction: «LANDED: » + the title body with each clause label moved behind its clause; the scope tail « (2026-10-31) — REDUCTIONS and
EQUIVALENCES (X) (source)» → «: REDUCTIONS and EQUIVALENCES; X′ (source). G-N5-TIME stays open.», X′ = X minus «G-N5-TIME stays OPEN»
and «not M3, not a step-4 pass, not a TARGET.md claim»; the source parenthesis is KEPT, before the final sentence. CONTROLS (same script):
on SRC line L-5 (l-red a5340f2d) with R97's (r1)-(r5) and the stamp «2026-10-31 07:02Z» / «449cb6fc» it reproduces R97's landed UPDATE on
GAPS l. 11 byte for byte (4,179 bytes); on ODD line L-2 (l-si 6370a35f) with R98's (q1)-(q2) it reproduces R98-draft l. 526 byte for
byte (4,253 bytes). NEW for this line, for CHECKER: three clauses of L-2 carry an inner «; » (FROZEN «…; all three lie in [0, n(n +
2)]», COPY «…; C-vertices keep the value (c, ∅, 0) on F», RESET-ROOT «…; hence TD_F ≤ …»); the script moves each label to the END of its
whole clause (before the «; » that precedes the next label), so these second sentences stay before their label (R97 / R98 had no such
clause, so the controls cannot test it). The UPDATE must hold no "|"; L-2 holds fourteen, so these replacements were made, which are NOT
title text: (q1) «n := |V| (V the vertex set of the game)» → «n := the number of vertices of V (V the vertex set of the game)» (= R97's
(r1)); (q2) «|F| := q − p its number of transitions» → «q − p is its number of transitions»; (q3) each of the other five «|F|» → «the
number of transitions of F» (R93-R97 wording; gives «WCT_F := the number of transitions of F − T1_F»). Checked by script: one line, 0
"|", one «<HH:MM>», one «<checker>», 4,776 bytes, 915 tokens. The stamp is «UPDATE 2026-10-31 <HH:MM>Z» (C106 §6, E-2: the landing date;
if R99 lands later, the date is corrected at landing); <HH:MM> and <checker> are filled at landing.
(10) DATA of record = the packet's §8 DATA (l. 163-167). Re-summed for this draft (python3 -I, scratch sum99.py over the stored outputs in
a `git archive` of 6903f1b3: experiments/new/box111/desc_{sbcg,alt}.txt, box110/res_{sbcg,alt}.txt, box107/fin_{sbcg,alt}.txt;
2026-10-31 18:41:20Z by date -u, rc 0): 1,132 rows in each family (719 + 413), 0 parse errors; WT 14,028; T2 (BW rises) 13,633; T1 79,
T3 25, T4 291; WDEC 0, XDEC 0, BWDEC 0, AFDEC 0, LSDEC 0; WCT 13,949; RT (transitions with a reset) 12,985, ROOTRES 12,985; Σ WCH 66,857;
DESC 14,755; max DESC/n 3.139 (runfam_K40); VIOL 0 in desc and res, VB 0; TD 520,674. All equal the packet (l. 163-166: «BW rises at
13,633 transitions.», «Resets occur at 12,985 of 13,949 W-changing transitions, and RESET-ROOT holds 12,985 / 12,985.», «Σ_v WCH 66,857
against DESC 14,755, max 3.14·n per game. VIOL 0 for every bound above.») and REFEREE-2's table (l. 127). The stored outputs predate fixes
entry 3; entry 3 l. 114-115 says the two corpus games with invalid starts give identical desc5 lines on the repaired starts, «So every §8
corpus total stands.», and REFEREE-2 L1 l. 36-37 says its own totals were on the repaired form already. Pins: (Data).
(11) Discrepancies, recorded for CHECKER, no verdict affected: (i) REFEREE's verdict table row l. 24 still reads «REQUIRED CHANGES
STAIR-L1 to STAIR-L7 (§10)» after a61a258b added STAIR-L8 (+7/−3: §10, FINDINGS, NEEDS changed, the row not). (ii) Fixes F0 l. 9 cites
f92b278a for REFEREE-2's report; the report is 8afe203a (12:55:35Z, new file, 170 lines) + f92b278a (13:06:38Z, +15/−2: STAIR-L6, §4b,
the row and verdict «L5» → «L6»). (iii) |sl| bounds: REFEREE l. 55 «|sl| ≤ n − 1.», REFEREE-2 l. 61 «|sl| ≤ n.»; the packet's COPY proof
says «Lengths stay in [0, n].» (l. 111) while G-ST-1's end-bit fact needs «ℓ ≤ n − 1» (REFEREE l. 73); both are true (ℓ ≤ n − 1 for a path
to the first occurrence of c in an n-vertex game); no verdict depends on the difference. (iv) RESET-ROOT counts differ by definition:
packet «12,985 / 12,985» counts transitions, REFEREE-2 «ROOT checks 59,285» counts resets (l. 130), REFEREE «RESET-ROOT 23,907» on its own
656-game run set (l. 105). (v) The frozen packet still lists [S4b-OPT] (l. 28-30), O-ARENA as to sign (l. 7), §10's CONJECTURE DESC-LIN
and §8's sbq2 0-descents on the invalid start (l. 167); fixes entries 3-5 supersede each (the packet is never edited, fixes l. 2-3). (vi)
The referees' line-item names clash ((3)). (vii) REFEREE's run set (box 59 sbcg.lst ∪ alt_all.lst, MAXN 100, 656 analysed of 719, l. 103)
differs from REFEREE-2's (box 50b's 1,132, l. 121); VIOLATIONS 0 on both. (viii) box 111 stated STAIR with 3n + 2; the packet sharpens to
3n + 1 (l. 136-137); R162's lane STAIR-U keeps 3n + 2 (not this entry).
(12) Excluded: L-NEW box 113 (docs/new/N5-DESCSTAR-box113.md: COPY⁺, DESC-ROOT, ROOT-STAIR, ORIGIN-NEW, NEW-FUEL; fixes entry 4 l.
129-131 «NOT part of this packet; not to sign»), box 116 (a82e7c55) and the P-N5-ROOT packet (c4279144; REFEREE's R-N5-ROOT114,
d8a2f428); L-RED R162's STAIR-U and CONJECTURE DESC*-LIN, R163 (DESC*-LIN DEAD, weak form) and R164; HIER-RED, CARRIER / GATE,
NEW-EDGE / ARENA-RED, NO-LAG (packet l. 10-11); 360d002f's start-validation code (experiments/new/box21/n5x.py, box113/fixstart.py,
repaired starts) beyond what fixes entry 3 records. The referees' tools (docs/referee/scratch/stair_probe.py, stair_logs/;
docs/referee-2/R2-N5-STAIR/stair_check.py, logs/) are review tools. Not part of this entry.
(13) Commits: lane (claude/l-new): 9a58765f (12:15:58Z; freeze: packet +195, box111/tog6a_n32.start +2, notes) → 360d002f (14:31:28Z;
fixes F0 + entries 1-5 +136, L-1 +1, check.sh +3/−3, n5x.py +7, box113 fixstart.py and four repaired starts, box 113 notes +5) →
6903f1b3 (16:14:21Z; entry 6 +23/−0, L-2 +1). REFEREE on claude/referee: 3c40dc18 (13:15:00Z; report, new file 152 lines; stair_logs/;
also R-N5-ODD.md +2/−0) → a61a258b (13:41:23Z; +7/−3, STAIR-L8) → ad4e7ebc (15:17:13Z; §C, +46/−0) → 45b63517 (16:43:29Z; L-2 addendum,
+7/−0). REFEREE-2 on claude/referee-2: 8afe203a (12:55:35Z; report, new file 170 lines; logs) → f92b278a (13:06:38Z; +15/−2, STAIR-L6 and
§4b; r162_pins.txt) → 6f45b443 (15:17:35Z; R2-N5-STAIR-L1.md, new file 57 lines) → cf5157fe (16:43:27Z; R2-N5-L2-confirm.md, new file 19
lines; notes +1/−1). L-RED: 54832628 (12:27:20Z; R162). Trunk merges that brought each in (a merge «… into claude/vibrant-johnson-nxvvxo»
containing it whose first parent does not; the C107 test): 9a58765f → ae13d609 (12:38:31Z); 54832628 → e3285db7 (13:04:21Z); 8afe203a,
f92b278a, 3c40dc18 → edc78bcc (13:56:35Z); a61a258b → db4a5d6a (14:21:51Z); 360d002f → ddf7dd57 (15:16:25Z); ad4e7ebc → a95c42e7
(15:44:47Z); 6f45b443 → 7c455f40 (16:13:51Z); 6903f1b3, 45b63517 → 1b159f51 (17:31:52Z); cf5157fe → eeec4da6 (18:36:37Z, local trunk
only at this draft).
(14) Placement: after R98 (pending; at 24280f52 R97 is l. 8032-8294, l. 8295 blank, "## Dead ends (kept;" l. 8296; see (0)). No
Dead-ends row: no signed item kills a conjecture; DESC-LIN's DEAD is L-RED's (R162), named in the title as R90 / R95 name their lane
DEADs (neither has a Dead-ends row); the packet's §8 DEADs are lane DEADs (not to sign).

### R99 [refereed-only] N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum; for S4a at a transition k → k + 1, σ_(k+1) is the pointwise optimum of S4a's one-player arena at k); premises RESULTS R15 (a), (d), R91 (Lemmas XW, W-MON), R93 (Fact LEX) and [PLAY] := P-N5-SRC §2 (proof of RESULTS R97 PLAY-CAUSE^S)), with: a run is the sequence of states (σ_k, τ_k), a transition is written k → k + 1 (states k, k + 1), and an Even vertex y switches at k if σ_(k+1)(y) ≠ σ_k(y); n := |V| (V the vertex set of the game); values (c, P, ℓ) (cycle node, path set, length) as in SPEC S1, ⊴, ◁, ⊵, ▷ the SPEC S1 order (better for Even) and its strict and reverse forms; Ξ_k := Ξ_{σ_k} (SPEC S1); W-run F = [p, q] := RESULTS R89's (a maximal run of consecutive states of one τ-stretch none of whose transitions is an S4c fallback or changes λ_W, the cycle-node map of W), with τ and C := {v : λ_W(v) = v} fixed on F, and |F| := q − p its number of transitions; for a state k of F, W_k := the [S1-val] valuation of the (σ_k, τ)-plays, and v's successor at k is σ_k(v) for Even v and τ(v) for Odd v; T1_F := the transitions of F with W_(k+1) = W_k, WCT_F := |F| − T1_F, and WCH_F(v) := the transitions of F changing W(v); CS(x) := RESULTS R93 (a)'s coordinate sequence of a value x (length n + 2), and lcp the length of the longest common prefix; BW_k := Σ_v lcp(CS W_k(v), CS W_q(v)), AF_k := Σ_v lcp(CS Ξ_k(v), CS W_q(v)), A_k := Σ_v lcp(CS Ξ_k(v), CS W_k(v)), and N_F := the transitions of F at which BW does not rise and A does not fall; for a value x = (c, P, ℓ), β(x) ∈ {0, 1}^(3n + 1) consists of one bit per rank r from the most relevant down, [r ∈ P] if r has even priority and [r ∉ P] if odd, followed by the threshold bits [sl ≥ j] for j = −n, …, n, where sl := ℓ if c has odd priority and −ℓ if even; GOOD_F(v, b) (BAD_F(v, b)) := the transitions of F flipping bit b of β(W(v)) from 0 to 1 (from 1 to 0, a RESET), and TD_F := Σ_(v, b) BAD_F(v, b); the first-difference position of a change of W(v) is the least index at which β changes (0 = most significant), and a DESCENT of v at k is a change of W(v) at k whose first-difference position is strictly larger than that of v's previous change of W(v) on F; DESC_F(v) := v's descents on F and DESC_F := Σ_v DESC_F(v): for every N5 run on every game, every W-run F = [p, q] of it, every transition k → k + 1 of F, every vertex v and every bit position b: (Lemma SANDWICH) for sequences x, y, z of one length in lexicographic order, x ≤ y ≤ z implies lcp(x, z) = min(lcp(x, y), lcp(y, z)); (Corollary FROZEN) BW_k and AF_k are non-decreasing on [p, q], and on any run of S4a steps Σ_v lcp(CS Ξ_k(v), CS Ξ_end(v)) is non-decreasing, end its last state; all three lie in [0, n(n + 2)]; (Lemma BW-ACC) with M := n(n + 2) + 1, |F| ≤ (M + 1)·n(n + 2) + M·N_F, and T1_F ≤ N_F ≤ |F|; (Fact BIT) for values x, y with one cycle node, x ◁ y iff β(x) is lexicographically smaller than β(y); (Lemma BIT-ALT) GOOD_F(v, b) ≤ 1 + BAD_F(v, b); (Lemma FIRST-GOOD) every change of W(v) on F flips its first differing β-bit from 0 to 1; (Theorem RESET-RED, an EQUIVALENCE) WCT_F ≤ Σ_v WCH_F(v) ≤ n(3n + 1) + TD_F, so |F| ≤ T1_F + n(3n + 1) + TD_F, and TD_F ≤ (3n + 1)·n·WCT_F; (Lemma COPY) if v ∉ C has the same successor z at k and at k + 1, then β(W(v)) and β(W(z)) have the same flips at k, in the same directions, through a strictly increasing position map; C-vertices keep the value (c, ∅, 0) on F; (Corollary RESET-ROOT) every reset of W(v) at k is copied, through COPY, from a reset of W(y) at k, where y is the first Even vertex switched at k on v's (σ_(k+1), τ)-play before λ_W(v); hence TD_F ≤ n·Σ_k Σ_(y switched at k) (the resets of W(y) at k); (Corollary DESC-COPY) if v ∉ C has a descent at k and did not switch at any transition from its previous change of W(v) on F to k, then its successor at k has a descent at k; (Lemma ASC-RUN) WCH_F(v) ≤ (3n + 1)(1 + DESC_F(v)); (Theorem STAIR, an EQUIVALENCE) WCT_F ≤ n(3n + 1) + (3n + 1)·DESC_F, so |F| ≤ T1_F + n(3n + 1) + (3n + 1)·DESC_F, and DESC_F ≤ n·WCT_F (2026-10-31) — REDUCTIONS and EQUIVALENCES (no count is bounded here; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim; the proof of DESC-COPY uses COPY's converse, whose proof is referee-originated (G-ST-1 = P-1, written independently by REFEREE and REFEREE-2; docs/new/P-N5-STAIR-fixes-box112.md entry 1)) (P-N5-STAIR, docs/new/P-N5-STAIR-box112.md; L-NEW successors 41-42; fixes docs/new/P-N5-STAIR-fixes-box112.md entries 1-7), CHECKER PASS (docs/checker/C109.md, checker PENDING)
- Object (L-NEW successor 41, Opus 5.5, D14 / D18; frozen, unchanged during review): packet P-N5-STAIR, docs/new/P-N5-STAIR-box112.md,
  sha1 3177124132afc1896438d148d8fbd4b7e2eaee52, 195 lines (l-new freeze 9a58765f21677e143379166428b207a1dfdc4782,
  2026-10-31T12:15:58Z, the file's only commit; identical at l-new head a82e7c55 and at trunk; first on trunk by merge ae13d609,
  12:38:31Z). Both referees measured the sha1 at 9a58765f (REFEREE l. 3-4 «This equals the Lead's figure.»; REFEREE-2 l. 2 «(re-hashed:
  match)»). Scope (l. 3-4): «Scope: a REDUCTION / EQUIVALENCE. No count is bounded here; G-N5-TIME stays OPEN; DESC-LIN is a CONJECTURE;
  not M3, not a step-4 pass, not a TARGET.md claim.» (DESC-LIN's status: fixes entry 4 records L-RED R162 as a lane DEAD; entry 7 drops
  DESC-LIN from the line, Lead reading L43; Honest limits (iii)). To sign (l. 7-8): «To sign: §2
  O-ARENA; §3 SANDWICH, FROZEN; §4 BW-ACC; §5 BIT, BIT-ALT, FIRST-GOOD, RESET-RED; §6 COPY, RESET-ROOT, DESC-COPY; §7 ASC-RUN, Theorem
  STAIR.» (O-ARENA withdrawn by Lead reading L42, below). «Not to sign: §8 (DEAD ends, DATA), §9 (erratum), §10 (CONJECTURE DESC-LIN).»
  (l. 9). Sources (l. 5-6): L-NEW's box notes docs/new/N5-FINPOT-box107.md, N5-HDEPTH-box108.md, N5-WIDTH-box110.md, N5-STAIR-box111.md,
  «history only»; «This packet restates everything it uses; the notes are not needed to check it.» Sections: §1 setting, premises (l.
  13-38), §2 O-ARENA (l. 40-48), §3 SANDWICH, FROZEN (l. 50-65), §4 BW-ACC (l. 67-78), §5 bits, BIT-ALT, FIRST-GOOD, RESET-RED (l. 80-97),
  §6 COPY, RESET-ROOT, DESC-COPY (l. 99-125), §7 ASC-RUN, STAIR (l. 127-145), §8 DEAD ends and DATA (l. 147-168, not to sign), §9 erratum
  (l. 170-173), §10 CONJECTURE (l. 175-176), §11 RESULTS line draft (l. 178-188).
  The RESULTS line, history: (1) the packet's §11 draft (l. 178-188), the line both referees reviewed: REFEREE REQUIRED STAIR-L1 to
  STAIR-L8 (§10 l. 121-146; STAIR-L8 added by a61a258b; l. 146 «It needs STAIR-L1 to STAIR-L8.»); REFEREE-2 REQUIRED STAIR-L1 to STAIR-L6
  (§5 l. 141-167; l. 182 «Line draft: REQUIRED STAIR-L1 to STAIR-L6.»). Each referee numbers its own line items (to check (3)). At the §11
  draft, the clause «(COPY, RESET-ROOT, DESC-COPY) resets and descents are copied from switched vertices» was not what was signed
  (REFEREE-2 STAIR-L4 «is not what was signed»; REFEREE STAIR-L6 «is not a checkable statement»), and the line still carried O-ARENA and
  [S4b-OPT]. (2) L-1 d027f5d8 (docs/new/P-N5-STAIR-line-L1.txt, 360d002f; fixes F0 + entries 1-5), a rewrite checked clause by clause:
  REFEREE §C (ad4e7ebc) l. 201-202 «Verdict on L-1: does NOT yet match, only because of STAIR-L9 (v and b unquantified), a one-phrase
  insertion. Everything else MATCHES (Opus 5.5, D15).»; REFEREE-2 R2-N5-STAIR-L1.md (6f45b443) l. 54-55 «**DOES NOT MATCH yet, one
  REQUIRED change STAIR-L1-1** (bind v and b in the global binder)», «Everything else MATCHES». (3) L-2 44f56e96
  (docs/new/P-N5-STAIR-line-L2.txt, 6903f1b3; fixes entry 6) = L-1 with the quantifier extended, «every vertex v and every bit position
  b», and «1-6)» (STAIR-L9 = STAIR-L1-1). REFEREE 21 L-2: §C addendum (45b63517) l. 209 «Verdict on L-2: MATCHES (Opus 5.5, D15). No
  REQUIRED change remains on the P-N5-STAIR line.» REFEREE-2 24 L-2: R2-N5-L2-confirm.md (cf5157fe) l. 19 «**MATCHES** (Opus 5.5, D15).
  STAIR-L1-1 is CLOSED. All my STAIR line items are closed.» At the L-2 object the scope tail read «(no count is bounded here; DESC-LIN
  (DESC_F ≤ c·n) DEAD (L-RED R162, claude/l-red 54832628: passive observers, cp_K); G-N5-TIME stays OPEN; not M3, not a step-4 pass, not
  a TARGET.md claim)». CHECKER C109 (claude/checker 178b3e9e, docs/checker/C109.md, 19:33:56Z) FAILED the draft on L-2: l. 16 «## 2.
  Verdict: FAIL (E-1, E-2, E-3)»; E-1 (l. 39-48) «L-2 contains «referee-originated» 0 times.» (Lead reading L41); E-2 (l. 50-56) ««H_k»
  occurs once in L-2 and is defined nowhere in it.»; E-3 (l. 58-79) «D-4: «c» is unbound, and it is the cycle node of «(c, P, ℓ)»
  elsewhere in the line.», «D-2: DESC-LIN with an unspecified constant is an asymptotic statement. No finite instance kills it.»; l. 102
  «All three are line items, closed by one L-3.» (4) L-3 9db0b169aadcbc5f81b2c0157f124946bbf74ad9 (docs/new/P-N5-STAIR-line-L3.txt, l-new
  7dc1eb7c95c8f2fd44652516ba7535b84660b9fb, 2026-10-31T20:01:32Z, the file's only commit; identical at l-new head 7988e2f4 and at trunk;
  first on trunk by merge 83b5acc9, 20:27:53Z; fixes entry 7) = L-2 with exactly these changes (word diff by script; fixes entry 7 l.
  205-213): «the pointwise optimum of the one-player arena H_k)» → «the pointwise optimum of S4a's one-player arena at k)» (E-2); the
  clause «DESC-LIN (DESC_F ≤ c·n) DEAD (L-RED R162, claude/l-red 54832628: passive observers, cp_K); » dropped (E-3, CHECKER's option (i);
  Lead reading L43, docs/DECISIONS.md l. 369-374: «A lane DEAD of an ASYMPTOTIC statement (one with an unspecified constant, e.g.
  «DESC_F ≤ c·n») does not enter a RESULTS line as «DEAD»: it enters as DATA with its numbers and source commit, or not at all.»);
  «not a TARGET.md claim)» → «not a TARGET.md claim; the proof of DESC-COPY uses COPY's converse, whose proof is referee-originated (G-ST-1
  = P-1, written independently by REFEREE and REFEREE-2; docs/new/P-N5-STAIR-fixes-box112.md entry 1))» (E-1; L41); «entries 1-6» →
  «1-7». REFEREE 21 L-3: §C addendum 2 (d6da0e93) l. 212 «Word-diff against L-2 (44f56e96). Exactly the Lead's list, and nothing
  else:», l. 221 «Both sha1s are re-hashed and match.», l. 222 «Strict symbol test: no new symbol.», l. 224 «Verdict on L-3: MATCHES (Opus
  5.5, D15).» REFEREE-2 25 L-3: R2-N5-STAIR-L3.md (faa8dac9) l. 6 «Token diff L-2 → L-3: exactly four replacements, nothing else (byte
  test True; each source phrase occurs once in L-2)», l. 34 «**MATCHES** (Opus 5.5, D15). Nothing REQUIRED from me.» L-3 supersedes the
  earlier lines; the title is L-3 verbatim with its own date (to check (R)). Neither referee found a FALSE claim statement; every line item
  drops O-ARENA, binds or defines a symbol (at L-3: H_k removed from the R57 gloss), replaces the vague clause by the signed corollaries,
  carries a precision (COPY both ways, RESET-ROOT «before λ_W(v)», the two converses), or words the scope tail (HDEPTH dropped; DESC-LIN
  DEAD at L-1 and L-2, dropped at L-3 per L43; the L41 referee-originated clause added at L-3).
  Setting (packet §1, l. 13-38): N5 = SPEC S1-S5; a run is the sequence of states (σ_k, τ_k), a transition k → k + 1; values (c, P, ℓ)
  «are VJ valuations: cycle node, path set (vertices more relevant than c on the path to the first occurrence of c), length» (l. 15-16);
  Ξ_k := Ξ_{σ_k}; «W-run F = [p, q] := RESULTS R89's» (l. 19), with τ and C := {v : λ_W(v) = v} fixed on F; W_k, H_k, |F|, T1_F, WCT_F,
  WCH_F(v) (l. 21-24). Premises (l. 25-37): [1E-N3] (R57); [S4b-OPT] (NOT covered, L42; used only in §2); [R15a] (R15 (a), (d)); [XW],
  [W-MON] (R91) with «On a W-run: W_(k+1) ⊵ W_k for every transition k → k + 1 of F.» (l. 32-33); [LEX] (R93 Fact LEX; «Its length is n
  + 2.», l. 35); [PLAY] (P-N5-SRC §2, the proof of RESULTS R97 PLAY-CAUSE^S). Cells: REFEREE §1 premises «CHECKED against landed text:
  R15 (a)/(d) (l. 624); R57 1E-N3; R91 Lemmas XW, W-MON (l. 6384); R93 (a) Fact LEX (l. 7031-7034); [PLAY] = P-N5-SRC §2» (l. 15);
  REFEREE-2 §2 l. 29-41, each ✓. L-3's notation is the packet's: CS and lcp (§3 l. 56), BW_k, AF_k (l. 57-58), A_k (l. 64), N_F (l. 68),
  β, sl and the threshold bits (l. 83-85), GOOD_F, BAD_F, TD_F (l. 88-89), first-difference positions and DESCENT (l. 118-119).
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 21 (report 3c40dc18, STAIR-L8 a61a258b, §C ad4e7ebc, L-2 addendum
  45b63517, L-3 addendum 2 d6da0e93); REFEREE-2 successor 24 (report 8afe203a + f92b278a, R2-N5-STAIR-L1.md 6f45b443,
  R2-N5-L2-confirm.md cf5157fe) and successor 25 (R2-N5-STAIR-L3.md faa8dac9, the L-3 word diff)). Items
  (a)-(j) are SIGNED in both verdict tables (REFEREE "## Verdicts" l. 12-24 of R-N5-STAIR.md; REFEREE-2 "## 1. Claims table" l. 11-27 of
  R2-N5-STAIR.md and its "## Verdict" l. 178-183); the table is to-check (4). (a), (d) hold for sequences and values; (b), (c), (e)-(j)
  inside every W-run of every N5 run on every game. Premises LANDED (as L-3 names them): SPEC S1-S5; RESULTS R15 (a), (d); R91 (Lemmas
  XW, W-MON); R93 (Fact LEX, CS); R89's W-run; standing premise: RESULTS R57's SPEC premise in its 1E-N3 form, used only through R91
  (REFEREE l. 35); [PLAY] from P-N5-SRC §2, the signed proof of RESULTS R97 PLAY-CAUSE^S (to check (5), (6)). The code's match to SPEC is
  DATA (R15 G-N5T-1). No item bounds a count.
  (a) Lemma SANDWICH (§3, l. 51-55): «For sequences of one length in lexicographic order, x ⊴ y ⊴ z implies lcp(x, z) = min(lcp(x, y),
      lcp(y, z)). In particular lcp(x, z) ≤ lcp(y, z).» (l. 51-52); proof: on [0, i) with i := lcp(x, z), y agrees with both; at i, x_i <
      z_i and x_i ≤ y_i ≤ z_i. Cells: REFEREE «SIGNED» (l. 17; §3 l. 38-41 «SANDWICH ✓.»); REFEREE-2 «SIGNED», «none» (l. 15; §3 l. 44-46).
  (b) Corollary FROZEN (§3, l. 56-63): on F = [p, q], with every lcp on CS, «BW_k := Σ_v lcp(CS W_k(v), CS W_q(v)) is non-decreasing on
      [p, q];», «AF_k := Σ_v lcp(CS Ξ_k(v), CS W_q(v)) is non-decreasing on [p, q];», «on any run of S4a steps, LS_k := Σ_v lcp(CS
      Ξ_k(v), CS Ξ_end(v)) is non-decreasing, where end is the last state of that run.», «All three lie in [0, n(n + 2)].» (l. 57-60);
      proof: [W-MON] gives W_k ⊴ W_k′ ⊴ W_q, [R15a] with [XW] gives Ξ_k ⊴ Ξ_k′ ⊴ W_k′ ⊴ W_q, [R15a] alone Ξ_k ⊴ Ξ_k′ ⊴ Ξ_end; SANDWICH per
      vertex. Cells: REFEREE «SIGNED» (l. 17; §3 l. 42); REFEREE-2 «SIGNED», «none» (l. 16; §3 l. 47-51).
  (c) Lemma BW-ACC (§4, l. 67-78): «Let M := n(n + 2) + 1 and N_F := #{transitions of F at which BW does not rise and A does not fall}.
      Then |F| ≤ (M + 1)·n(n + 2) + M·N_F.» (l. 68-69), with «Every W-constant transition is in N_F» and «Conversely N_F ≤ |F|» (l.
      70-72); proof: the potential M·BW − A ∈ [−n(n + 2), M·n(n + 2)] gains ≥ 1 outside N_F and loses ≤ n(n + 2) in N_F; a W-constant
      transition keeps BW and does not lower A (SANDWICH). Cells: REFEREE «SIGNED» (l. 18; §4 l. 45-48); REFEREE-2 «SIGNED», «none» (l.
      17; §3 l. 52-56).
  (d) Fact BIT, Lemmas BIT-ALT and FIRST-GOOD (§5, l. 81-91): β as in the title (n parity-oriented rank bits, then the 2n + 1 threshold
      bits); «For values with the same cycle node, x ◁ y ⟺ β(x) <_lex β(y).» (l. 86); «GOOD_F(v, b) ≤ 1 + BAD_F(v, b). Proof: a 0/1
      sequence alternates.» (l. 90); «Every change of W(v) on F flips its first differing bit 0 → 1. Proof: [W-MON] and Fact BIT.» (l.
      91). Cells: REFEREE «SIGNED» (l. 19; §5 l. 51-57); REFEREE-2 «SIGNED», «none» (l. 18; §3 l. 57-64).
  (e) Theorem RESET-RED, an EQUIVALENCE (§5, l. 92-97): «WCT_F ≤ Σ_v WCH_F(v) ≤ n(3n + 1) + TD_F, so |F| ≤ T1_F + n(3n + 1) + TD_F.
      Conversely TD_F ≤ (3n + 1)·n·WCT_F.» (l. 92-93); proof: FIRST-GOOD and BIT-ALT per vertex; a change has ≤ 3n + 1 flips. Cells:
      REFEREE «SIGNED» (l. 19; §5 l. 58-59); REFEREE-2 «SIGNED», «none» (l. 19 «Theorem RESET-RED (both directions)»; §3 l. 65-68).
  (f) Lemma COPY (§6, l. 100-111), in L-3's two-way form (unchanged since L-1): for v ∉ C whose successor on both the (σ_k, τ)- and the (σ_(k+1), τ)-play is
      the same z (l. 101-102), «Then β(W_j(v)) = π_v(β(W_j(z))) for j = k, k + 1,» (l. 103), and β(W(v)) and β(W(z)) have the same flips
      at k, in the same directions, through a strictly increasing position map (fixes entry 1's statement, l. 55-56; the frozen packet
      states one direction, l. 105-106); «C-vertices have the constant value (c, ∅, 0) on F.» (l. 107); proof: [PLAY] gives W_j(v) =
      Φ(v; W_j(z)) on the fixed cycle node λ_W(v); v's own rank bit and z's one unmatched threshold bit are constant (G-ST-1, below). Cells:
      REFEREE «SIGNED, with proof-text gap G-ST-1 closed here (§6). The statement is unaffected» (l. 20; §6 l. 62-74); REFEREE-2 «SIGNED»,
      «none (precision P-1)» (l. 20; §3 l. 69-81). Two-way form: REFEREE §C l. 177-178 «That is G-ST-1's repair (entry 1) ✓.»; REFEREE-2
      R2-N5-STAIR-L1.md l. 32 «**I SIGN Entry 1's repair** (Opus 5.5, D15).»
  (g) Corollary RESET-ROOT (§6, l. 112-117): «Its first vertex y that is Even and switched at k (σ_(k+1)(y) ≠ σ_k(y)) exists, and β(W(y))
      has a reset at k.» (l. 113), read «… before λ_W(v)» (P-2, fixes entry 2 l. 71 «Its first vertex y BEFORE λ_W(v) that is Even and
      switched at k exists, and β(W(y)) has a reset at k.»), and «So TD_F ≤ n·Σ_k Σ_(y switched at k) (resets of W(y) at k).» (l. 114);
      proof: with no switched vertex the new play is the old one; COPY along the unswitched prefix; «C-vertices never change, so the
      prefix does not pass one before y.» (l. 117). Cells: REFEREE «SIGNED» (l. 21; §6 l. 75-80, l. 80 «At most n pairs (v, b) map to one
      (y, b′) per k, which gives the factor n.»); REFEREE-2 «SIGNED», «none (precision P-2)» (l. 21; §3 l. 82-90). «before λ_W(v)»:
      REFEREE §C l. 179-180 «This is consistent with my §6: y ∉ C, and a C-vertex before y is impossible ✓.»; fixes entry 2 l. 72 «The
      proof is unchanged: its last line already excludes C-vertices on the prefix.»
  (h) Corollary DESC-COPY (§6, l. 118-125): «If v has a descent at k, and v did not switch at any transition of [k′, k] (k′ := v's
      previous change), then its successor z has a descent at k.» (l. 120-121); proof: on [k′, k + 1] v's successor is z; every change of
      z in (k′, k) would be copied to v (COPY's CONVERSE, G-ST-1), so z's changes in [k′, k] are at k′ and k; the position map is strictly
      increasing. Cells: REFEREE «SIGNED (DESC-COPY uses COPY's converse, G-ST-1)» (l. 21; §6 l. 81-84); REFEREE-2 «SIGNED», «none» (l.
      22; §3 l. 91-94). Fixes entry 1 l. 61 «DESC-COPY's proof uses exactly this. Its statement is unchanged.»
  (i) Lemma ASC-RUN (§7, l. 128-133): «q_(j+1)(v) ≠ q_j(v), and between two descents the positions strictly decrease. So WCH_F(v) ≤ (3n +
      1)(1 + DESC_F(v)).» (l. 128-129); proof: after change j bit q_j is 1 (FIRST-GOOD); a next change at the same position would flip it 0
      → 1 again. Cells: REFEREE «SIGNED» (l. 22; §7 l. 87-88); REFEREE-2 «SIGNED», «none» (l. 23; §3 l. 95-98).
  (j) Theorem STAIR, an EQUIVALENCE (§7, l. 134-143): «Then WCT_F ≤ n(3n + 1) + (3n + 1)·DESC_F, with DESC_F := Σ_v DESC_F(v). Hence |F|
      ≤ T1_F + n(3n + 1) + (3n + 1)·DESC_F.» (l. 136); «Conversely DESC_F ≤ Σ_v WCH_F(v) ≤ n·WCT_F, so WRUN-POLY ⟺ (T1 + DESC)-POLY.» (l.
      138); proof: Ψ_k := Σ_v ψ_k(v) ∈ [0, n(3n + 1)] falls by ≥ 1 at every descent-free W-changing transition and rises by ≤ 3n per
      descent. Cells: REFEREE «SIGNED» (l. 22; §7 l. 89-93); REFEREE-2 «SIGNED», «none» (l. 24 «Theorem STAIR (both directions)»; §3 l.
      99-103).
  The RESULTS line (L-3) claims less than the reports in places (no SANDWICH «In particular», no ASC-RUN q-inequality, no POLY reading, no
  Ψ, no π_v formula) and, in one place, more than the frozen packet statement: COPY's converse, which both referees signed as fixes entry
  1's repair. Every claim clause L-3 states is one of (a)-(j); its scope tail states no claim (to check (4), (7)).
- G-ST-1 = P-1 (COPY's converse; a proof-text gap of the packet, CLOSED by a referee-originated repair; Lead reading L41):
  - The gap: DESC-COPY's proof uses «Every change of z in (k′, k) would be copied to v (COPY)» (l. 124), the converse of COPY's stated
    direction.
    REFEREE §6 l. 68-70 «COPY states only «every flip of W(v) is a flip of W(z)». π_v discards z's bit at v's own rank and one end bit of
    z's threshold block, so the converse needs both to be constant on F.» (guillemets nested as in the source).
  - The repair, written by each referee in its own report, independently (REFEREE l. 6 «Independence: I opened no docs/referee-2/ file for
    this packet.», 3c40dc18 13:15:00Z; REFEREE-2 l. 4 «Independence: written before opening any docs/referee/ file on STAIR.», 8afe203a
    12:55:35Z): REFEREE l. 71-74 «The rank bit is constant: v ∉ P(W_j(z)), because z's W-path visiting v before c would make v's W-play
    (v, then z's play) revisit v before reaching c, so the cycle would not contain c = λ_W(v).», «The end bit is constant: [ℓ(z) ≥ n] = 0
    if c is odd, and [−ℓ(z) ≥ −n] = 1 if c is even, since ℓ ≤ n − 1.», «So W(v) changes at a transition of COPY's hypothesis exactly when
    W(z) does, flip for flip.»; REFEREE-2 §3 l. 71-77 («v's own rank bit is constant: v ∉ P(z), and [v ∈ P(v)] depends only on v versus
    c.», «The one bit of z with no image is constant too: [sl(z) ≥ n] = 0 when ℓ(z) ≤ n − 1, and [sl(z) ≥ −n] = 1.», «So the non-constant
    bits of v and z correspond bijectively and in order,») and its precision P-1 (l. 79-81, «Suggest stating COPY as «β(W(v)) and
    β(W(z)) have the same flips, through an increasing position map».»).
  - Adopted: fixes entry 1 (l. 40-63; «G-ST-1 and P-1, one entry as the Lead asked»), the repaired statement (l. 55-56) and «Proof: the
    packet's COPY proof, plus REFEREE's two constancy facts above.» (l. 57). Signatures of the adopted text: REFEREE §C l. 177-178 «COPY
    is stated in both directions («the same flips at k, in the same directions, through a strictly increasing position map»). That is
    G-ST-1's repair (entry 1) ✓.»; REFEREE-2 R2-N5-STAIR-L1.md l. 32 «This is the bijection I checked in R2-N5-STAIR §3. **I SIGN Entry
    1's repair** (Opus 5.5, D15). DESC-COPY's statement is unchanged.»
  - Joint gap map: G-ST-1 = P-1, CLOSED (one argument, written by both, signed by both); nothing FALSE. REFEREE l. 151 «Every item to sign
    (L42 list) is SIGNED. G-ST-1 (COPY's converse, used by DESC-COPY) is closed here. Nothing is FALSE.»; REFEREE-2 l. 27 «Gap map:
    EMPTY.» and l. 181 «Gap map: EMPTY. Precisions P-1 (COPY's two directions) and P-2 (RESET-ROOT «before λ_W(v)»).» (it proved the
    converse inside its COPY check, so it did not list a gap); fixes F0 l. 13 «Gap map: REFEREE has G-ST-1 (closed by REFEREE); REFEREE-2's
    is EMPTY (precisions P-1, P-2).»
  - Lead reading L41: «A proof written by one referee counts toward "two referees signed it with its gaps listed" (CLAUDE.md) when the
    author referee signs it in its report and the OTHER referee independently checks and signs it; both signatures and the joint gap map
    are quoted in the RESULTS entry, whose scope tail says the proof is referee-originated.» Both signatures and the joint gap map are
    quoted above, and L-3's scope tail says it: «the proof of DESC-COPY uses COPY's converse, whose proof is referee-originated (G-ST-1 =
    P-1, written independently by REFEREE and REFEREE-2; docs/new/P-N5-STAIR-fixes-box112.md entry 1)» (C109 E-1; fixes entry 7). At the
    L-2 object the tail did not say it (C109 l. 42). Both referees confirm the clause on L-3: REFEREE §C addendum 2 l. 218-219 «This is
    correct under L41: I wrote G-ST-1, REFEREE-2 wrote P-1, and each signed the other's.»; REFEREE-2 25, R2-N5-STAIR-L3.md l. 26 «So
    «written independently by REFEREE and REFEREE-2» is right for my side. «referee-originated» is right as well, under L41.» (Signatures).
    The same converse is proved independently at lane level as Lemma COPY⁺ in L-NEW box 113 (fixes entry 1 l. 62-63; «That is lane level
    and not part of this packet.»), not refereed here and not used (C109 l. 44-45 «The counter-reading fails: L-NEW's COPY⁺ (box 113) is
    lane-level and unreviewed»).
- O-ARENA and [S4b-OPT] (NOT signed; Lead reading L42, docs/DECISIONS.md, 2026-10-31 12:37Z): «Premises not in R57. R57's standing SPEC
  premise (1E-N3) covers S1's procedure and S4a (σ_(k+1) is the pointwise optimum of H_k). It does NOT cover S4b:» … «A packet claim that
  needs an uncovered premise is not signed: it is moved to "not to sign" (or stated with the premise as an explicit hypothesis, labelled
  CONDITIONAL). Applied first to P-N5-STAIR (docs/new/P-N5-STAIR-box112.md sha1 31771241): O-ARENA is withdrawn from the to-sign list;
  nothing else in the packet uses it (L-NEW 41, 12:30Z).» Both referees: REFEREE l. 16 «NOT SIGNED (withdrawn by L42). Nothing in §3-§7
  uses O-ARENA or [S4b-OPT] (checked line by line)»; REFEREE-2 l. 14 «NOT SIGNED (withdrawn, L42)», l. 40-41 «§3-§7 use neither: grep,
  and a read of every proof. ✓», l. 180 «NOT SIGNED: O-ARENA (L42). Nothing else uses it.» Fixes entry 5 l. 134 «O-ARENA needs [S4b-OPT],
  which R57's premise does not cover (L42).», l. 136 «The packet's §1 premise list should be read without [S4b-OPT].» L-3 states neither.
- Fixes (docs/new/P-N5-STAIR-fixes-box112.md, L-NEW successor 42, APPEND-ONLY, F0 and entries 1-7, three commits each +N/−0: 360d002f
  (2026-10-31T14:31:28Z, new file, 136 lines, F0 + entries 1-5; the file then sha1 f07676f47f51ba991015b4e43d4406da4add57a4), 6903f1b3
  (16:14:21Z, +23/−0, entry 6; the file then sha1 52fd8b500266d6ca5615e239fb621f56249ff1f0, 159 lines) and 7dc1eb7c (20:01:32Z, +55/−0,
  entry 7, with L-3; sha1 6e45b0e0684d06ba9258a466d96bc9829e096218, 214 lines; = l-new head 7988e2f4 = trunk; the last commit touching
  the file)). Header (l. 2-3): the frozen packet «is NOT edited; every repair is here.» Each entry:
  - F0 (l. 6-38): reports, verdicts and the item map; «Both referees SIGN SANDWICH, FROZEN, BW-ACC, BIT, BIT-ALT, FIRST-GOOD, RESET-RED,
    COPY, RESET-ROOT, DESC-COPY, ASC-RUN and Theorem STAIR.» (l. 11); «O-ARENA is NOT signed (Lead reading L42: [S4b-OPT] is not covered by
    R57). Both checked that nothing else uses it.» (l. 12).
  - Entry 1 (l. 40-63): G-ST-1 and P-1, COPY in both directions (above).
  - Entry 2 (l. 65-72): P-2, RESET-ROOT «before λ_W(v)»; the proof is unchanged.
  - Entry 3 (l. 74-122): D-ODD-1 = F-1, a DATA defect (Honest limits (vi); Data).
  - Entry 4 (l. 124-131): DESC-LIN DEAD (L-RED R162); «Packet §10 is superseded. Theorem STAIR is unaffected: it is an EQUIVALENCE, not a
    bound.» (l. 128). History since entry 7: the R162 clause was in L-1 and L-2 and is not in L-3; R162 is recorded here as lane DATA
    (Honest limits (iii); Data), not as a line claim.
  - Entry 5 (l. 133-136): O-ARENA withdrawn (L42).
  - Entry 6 (l. 139-159): STAIR-L9 = STAIR-L1-1, both referees quoted verbatim; «Repair: line L-2 = L-1 with the quantifier extended» (l.
    153).
  - Entry 7 (l. 162-214): CHECKER C109 E-1..E-3 quoted verbatim (l. 163-204; l. 164-204 = C109 l. 39-79, by script); «Repair: line L-3 = L-2 with exactly
    three moves (Lead 20:03Z) and the entries count» (l. 205); «E-3, CHECKER's option (i), the Lead's choice: the clause «DESC-LIN (DESC_F
    ≤ c·n) DEAD (L-RED R162, claude/l-red 54832628: passive observers, cp_K); » is dropped.» (l. 209-210); «Fixes entry 4 is history: it
    records R162 as lane DATA / a lane DEAD and is not part of the line.» (l. 212); «Bookkeeping: «entries 1-6» → «entries 1-7». No other
    change.» (l. 213).
  No fix changes a signed statement except by the signed repair of entry 1 (COPY's converse added) and the precision of entry 2; entries
  4-7 word the line; entry 3 repairs pins and starts.
- Not signed: §1 (premises and notation; REFEREE «CHECKED against landed text», l. 15); O-ARENA and [S4b-OPT] (L42); the A_k remark (l.
  64-65), the O-ARENA «Reading» (l. 47-48) and Corollary RESET-STAIR (l. 144-145); §8 DEAD ends (a)-(e) and DATA, §9 erratum, §10 DESC-LIN
  (REFEREE §8 l. 96 «O-ARENA, the RESET-STAIR remark, §8 DEADs and DATA, the §9 erratum, and §10 DESC-LIN.»; REFEREE-2 l. 25 «not
  signed»). The lane DEADs of §8 (BW strict rise, ceiling potentials on a W-constant interval, «every σ-move raises Ξ or W», HDEPTH «h^W ≤
  2», descents at source events) are not landed here. The §9 erratum is agreed (REFEREE l. 97 «The erratum is right: W-MON is
  lexicographic, so lower bits may fall.»). OPEN, not claimed: whether T1_F, N_F, TD_F or DESC_F (or a repaired counted set) is
  polynomially bounded on W-runs; G-N5-TIME. No CONJECTURE is killed by a signed item, and L-3's scope tail states no DEAD; L-RED R162 on
  DESC-LIN is lane DATA, not landed (Honest limits (iii)).
- Referee strengthening (NOT part of this entry; remarks of one referee, remarks of both outside the verdict cells):
  (i) [PLAY]'s fixed-cycle-node form needs y ≠ c: REFEREE l. 33-34 «Every use has y ∉ C (COPY), so it is fine.»; REFEREE-2 l. 38-39.
  (ii) Fact BIT: REFEREE l. 53 «The threshold vector ([sl ≥ j])_(j = −n … n) is lex-increasing in sl: the first difference between sl <
      sl′ is at j = sl + 1, where sl′ has 1.»; REFEREE-2 l. 62 «β is injective on values with one cycle node. ✓»
  (iii) STAIR: REFEREE l. 90 «Ψ_p = n(3n + 1).», l. 91 «A first change counts as a fall (from 3n + 1 to ≤ 3n).»; REFEREE-2 l. 101 (the
      same, «a first change included»).
  (iv) Mutation controls (REFEREE l. 110-112): MUT 1 «(AF referenced to the moving W_k, the packet's remark A): bites, FROZEN_AF_V 33 on
      x31_rx48.»; MUT 2 «(β without parity orientation): bites, BIT_V 6,448 and FG_V 2,650.»
  (v) REFEREE-2's optional precision on L-1, «every c ∈ C keeps the value (c, ∅, 0) on F» (L1 l. 49-50), not applied («It stays
      optional.», L2 confirm l. 18).
- Honest limits: (i) REDUCTIONS and EQUIVALENCES: no count is bounded. BW-ACC moves |F| to N_F, RESET-RED to the resets TD_F, STAIR to
  the descents DESC_F, each up to T1_F (not in BW-ACC) and polynomial terms; the converses make RESET-RED and STAIR equivalences («WRUN-POLY ⟺ (T1 +
  DESC)-POLY», packet l. 138, not stated by L-3). G-N5-TIME stays open. (ii) Everything holds inside W-runs, which are not whole runs
  (R89). (iii) DESC-LIN (the packet's §10 CONJECTURE, «DESC_F ≤ c·n» for a constant c) is NOT settled here. L-RED R162 (54832628, not
  landed) reports it DEAD at LANE level (fixes entry 4): «Passive observer copies of obs (family cp_K) give DESC = K(n_base + 1) ≈ n²/88
  with |F| unchanged. Suffix observers kill the per-transition form.» (fixes l. 125-126). That DEAD was a clause of the line at L-1 and at
  the L-2 object; L-3 drops it (C109 E-3 option (i); Lead reading L43: a lane DEAD of an asymptotic statement «enters as DATA with its
  numbers and source commit, or not at all»), so R162 is recorded in this entry as lane DATA only, not as a line claim: R162's table
  (K = 4, 8, 12, 16; DESC/n 2.02, 4.02, 6.02, 8.02; desc2.py; xeng and Oink faithfulness on cp_K4, suf_K4, suf_K8 only); REFEREE-2 re-ran
  cp_K4 (DESC 388, n 192) and suf_K4 (DESC 28) with its own tool (§4b); L-NEW box 113 re-ran cp_K4 (388); REFEREE did not re-run it
  (STAIR-L8 «I have not re-run R162; this item relies on the Lead's relay.»). Only cp_K4 of the cp family is committed (to check (5)).
  Read as DATA: the counted set DESC_F of STAIR grows on cp_K while |F| does not, so STAIR's DESC_F route may not bound |F| by itself;
  no signed item depends on it. (iv) COPY's converse (the line's two-way COPY) and DESC-COPY's proof rest on the referee-originated
  repair G-ST-1 = P-1, written independently by REFEREE 21 and REFEREE-2 24 and signed by both (Lead reading L41; the G-ST-1 bullet);
  L-3's scope tail names it (C109 E-1; at the L-2 object it did not). (v) Premises: the standing premise R57 enters only through R91
  (REFEREE l. 35); [PLAY] comes from P-N5-SRC §2, landed in R97 only as PLAY-CAUSE^S's signed proof; L-3's R57 gloss reads «σ_(k+1) is
  the pointwise optimum of S4a's one-player arena at k» (C109 E-2; at the L-2 object it named H_k without defining it), with k bound by
  «for S4a at a transition k → k + 1» (REFEREE §C addendum 2 l. 213-214). The code's match to SPEC is DATA (R15 G-N5T-1). (vi) DATA DEFECT D-ODD-1 (REFEREE) = F-1 (REFEREE-2), fixes entry 3: the start file sbq2_K8_m16.start (sha1 98b0927a…) sets
  τ(242) := 243, a NON-EDGE (REFEREE-2 l. 172 «243 is not a successor of the Odd vertex 242 (succ(242) = 244, 246, …, 258).»; REFEREE l.
  116-118 «That start has the non-edge 242 → 243 (R-N5-ODD §7, D-ODD-1), so this DATA figure is unfaithful as pinned. It is not a signed
  item.»). Packet §8's «sbq2_K8_m16 (L-SI box 54, 70f485cd…; faithfulness per their lanes) have 0 descents» (l. 167) was measured on it;
  fixes l. 78 «was measured on a non-game. No signed item uses it.» Repair (fixes l. 79-103): n5x.start_pair now rejects a non-edge or a
  wrong-player entry for L-NEW's tools; the repaired start box113/inst/sbq2_K8_m16_fixed.start (sha1 83a57866…, 242:243 → 242:244) gives
  one W-run [1, 152], |F| 151, DESC 0, resets 151 / 151. The two corpus games with invalid starts (comp54_n80, n3cov_lean) were repaired
  with identical desc5 lines (l. 111-115, «So every §8 corpus total stands.»). No signed item uses sbq2. (vii) Counts are transitions and
  bit flips, not bit operations; no running-time bound. (viii) Not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open.
- Data (DATA, not proof): pinned (packet §8 l. 168: «box 107 FINPOT», «box 110 WIDTH», «box 111 STAIR»; also box 108, box 109).
  experiments/new/check.sh at 6903f1b3: sha1 c1d5e322b3f015db2968aaa57f28c1abd5588a82, 604 lines; box 107 l. 562-567, box 108 l.
  568-573, box 109 l. 574-579, box 110 l. 580-585, box 111 l. 586-591, identical at 9a58765f and at trunk 2640a8bc (diff of l. 562-591:
  none). The packet and line files are NOT sha1-pinned in L-NEW's check.sh (unlike L-SI's P-N5-ODD pins). Re-run for this draft from a
  `git archive` of 6903f1b3 (experiments/ and docs/new/; from experiments/new), l. 1-8 (set -euo pipefail, cd, tmp) plus l. 562-591,
  2026-10-31 18:40:46Z-18:40:49Z by date -u, rc 0; output the five lines «box 107 FINPOT: W-MON / O-ARENA hold (x31_rx48), BW-alone DEAD
  (17 T4), hierarchy depth 2 pays them; u23sw64 floor paid by the joint level; NOV 1 on tog6a: PASS», «box 108 HDEPTH: NEW-EDGE 0
  violations (x31_rx48, 295 W-changes), depth-2 carriers released by one new edge at a source event (49/49), ARENA-RED bound holds: PASS»,
  «box 109 HSEARCH: HDEPTH DEAD (hit_b6a_1 n 32 h^W 3, joint 2); hit_n16_1 unary-length depth 1: PASS», «box 110 WIDTH: hd_H40 depth 40
  with 0 resets; hit_b6a_1 resets all rooted at switches (34/34), RESET-RED and BIT-ALT hold: PASS», «box 111 STAIR: ASC-RUN holds; hd_H40
  descent-free (2420 vertex W-changes, 0 descents); hit_b6a_1 24 descents: PASS». Supporting blocks for fixes entries 3-4 (l. 191-210 box
  55, l. 514-519 box 99, l. 592-597 box 113; same archive, with GIT_DIR set to the repository because box 55's quote check runs `git show`),
  18:40:49Z-18:40:56Z, rc 0: «box 55 P-N5-SF: pcheck PASS on n3all_maxph_0 (fallback), switchbestexp_2 (SBC 4), n3cov_lean (LAM 4, SBC
  11), MUT bites; quotes PASS: PASS», «box 99 QRET: sbq2_K8_m16 returns all rooted at fresh entries, clock vertex 4's ticks root 45 = 3m - 3
  each: PASS», «box 113 DESCSTAR: SW-WIT, DESC-ROOT, ORIGIN-NEW, NEW-FUEL hold on 5 pins; frz32 3 old-edge relay root descents; lcount2
  T-type 1; cp_K4 switch-site U not passive-proof (388): PASS». (A first combined run without GIT_DIR stopped at box 55 with rc 1, «box 55
  P-N5-SF checks: FAILED», because `git show` has no repository inside an archive; the five box 107-111 lines had passed.) Oink NOT RUN for
  this draft (these blocks do not call it); packet §8 header «Oink 8fbf0a7 --zlk and --tl «solution verified» and equal to N5's regions»;
  REFEREE l. 115 «Oink 8fbf0a7 `--zlk --verify` verifies the solution on x31_rx48, u23sw64_n32, tog6a_n32, hit_b6a_1, hd_H40 and
  obs_K12_m24.»
  DATA OF RECORD (packet §8 l. 163-167; L-SI box 53's 1,132 games, 14,028 W-run transitions): BW rises at 13,633; resets at 12,985 of
  13,949 W-changing transitions, RESET-ROOT 12,985 / 12,985; Σ_v WCH 66,857 against DESC 14,755, max 3.14·n per game; VIOL 0 for every
  bound. Re-summed for this draft from the stored outputs: equal (to check (10)).
  REFEREE (successor 21; own docs/referee/scratch/stair_probe.py, rl_engine, «no lane code», l. 99): box 59 sbcg.lst ∪ alt_all.lst, 719
  games, MAXN 100, 656 analysed (l. 103): «950 W-runs, 7,401 transitions, WCT 7,361, Σ WCH 28,319, TD 159,730, DESC 6,584;» (l. 104);
  «checks: BIT 77,761, RESET-ROOT 23,907, DESC-COPY 2,447;» (l. 105); «VIOLATIONS 0 (stair_logs/sum.txt).» (l. 106); pins x31_rx48,
  u23sw64_n32, tog6a_n32, hit_b6a_1, hd_H40: «12 W-runs, VIOLATIONS 0.» (l. 108); L-NEW's blocks «box 107 FINPOT» to «box 111 STAIR» at
  9a58765f «run alone in a detached worktree: all PASS, EXIT 0.» (l. 113-114). Its checks (l. 101-102): FROZEN, BW-ACC, BIT, FIRST-GOOD,
  RESET-RED, RESET-ROOT, ASC-RUN, STAIR's bound, DESC-COPY.
  REFEREE-2 (successor 24; own docs/referee-2/R2-N5-STAIR/stair_check.py, «The lane's box107-111 tools are not imported.», l. 107):
  corpus 1,132 games (sbcg.lst 719, alt_all with start 94, start-less 319; table l. 122-127): 0 violations, and «Every total equals the
  lane's §8 DATA exactly:» (l. 128); «RESET-ROOT holds at every reset: ROOT checks 59,285, 0 violations;» (l. 130); «Random 300 games
  (seed 31, n 5-12, 4 starts): 0 violations.» (l. 131); pins hd_H40, hit_b6a_1, x31_rx48, u23sw64_n32, tog6a_n32, obs_K12_m24, «All pins:
  0 violations.» (l. 120); R162 pins (§4b) «cp_K4: one W-run [0, 44], n 192, |F| 44, WCH 3904, DESC 388.», «suf_K4: one W-run [0, 44], n
  103, |F| 44, DESC 28.» No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-STAIR.md (successor 21): report 3c40dc18533ac6457370017f508e64d4bb71955d (2026-10-31T13:15:00Z,
  new file, 152 lines, with docs/referee/scratch/stair_logs/; first on trunk by merge edc78bcc, 13:56:35Z): §1 CHECKED, §3-§7 SIGNED,
  O-ARENA NOT SIGNED; STAIR-L8 a61a258b2522bdd9e093a5db3139ada10be6aea1 (13:41:23Z, +7/−3; on trunk by db4a5d6a, 14:21:51Z); §C
  ad4e7ebc97a450028dd3ecd3fa8e1c2556bbf692 (15:17:13Z, +46/−0; on trunk by a95c42e7, 15:44:47Z): L-1 and the fixes checked (l. 158-202),
  «Verdict on L-1: does NOT yet match, only because of STAIR-L9» (l. 201); §C addendum 45b63517f1c59157ca231fec35c2d4e0c3cb8bc3
  (16:43:29Z, +7/−0; the file then 209 lines, sha1 c43308c59aaf24cbcd48483c469cce96cf13323a; on trunk by 1b159f51, 17:31:52Z): «Verdict
  on L-2: MATCHES (Opus 5.5, D15).» (l. 209); §C addendum 2 d6da0e9333c44a376292e99cfd2c3e7a468e021b (20:28:02Z, +15/−0, l. 211-224;
  the file now 224 lines, sha1 bd70a85f2f733982890dda189729ab79caeb4300, = referee head; on trunk by f3ef5852, 20:56:18Z): «Verdict on
  L-3: MATCHES (Opus 5.5, D15).» (l. 224). REFEREE-2 (successor 24): docs/referee-2/R2-N5-STAIR.md
  8afe203a02b74cf145f988728a7000fb2fbc04bd (12:55:35Z, new file, 170 lines; with R2-N5-STAIR/logs) and
  f92b278a234c7605cb051b4c617c552a709bced8 (13:06:38Z, +15/−2, STAIR-L6 and §4b; the file then 183 lines, sha1
  90ab040518b486045fcce56e31efb1ebe288a6f9, unchanged since; both on trunk by edc78bcc): every item but O-ARENA SIGNED (l. 11-27, l.
  178-183); R2-N5-STAIR-L1.md 6f45b443a02f574e501ac3b80970829cd41f2f01 (15:17:35Z, new file, 57 lines, sha1
  12db0de62c611c780e02b08af11709ce8ffea540, unchanged since; on trunk by 7c455f40, 16:13:51Z): STAIR-L1-1 REQUIRED, entry 1's repair
  SIGNED (l. 32); R2-N5-L2-confirm.md cf5157feafbf5d3fc7747a0875e216924b052f35 (16:43:27Z, new file, 19 lines, sha1
  85d3a211503954ab4ffec91be08827122f0d0b49, unchanged since; on trunk by eeec4da6, 18:36:37Z): §(2) «**MATCHES** (Opus 5.5, D15).
  STAIR-L1-1 is CLOSED. All my STAIR line items are closed.» (l. 19). REFEREE-2 (successor 25, a new successor; successor 24 wrote the
  reports above): docs/referee-2/R2-N5-STAIR-L3.md faa8dac9d846c4a00d52e0c4ce6e6d646de74a64 (20:28:55Z, new file, 39 lines, sha1
  5b29a17f9553485b9cf148dcda7269907d915581; the same commit adds R2-N5-ROOT114-L1.md +8, not this entry; = referee-2 head; on the local
  trunk by a20cf406, 21:23:35Z, NOT on origin trunk a8b42b38 at this rebuild): «**MATCHES** (Opus 5.5, D15). Nothing REQUIRED from me.»
  (l. 34).
  L41, REFEREE-ORIGINATED PROOF (G-ST-1 = P-1): both referees wrote COPY's converse independently, and each signed it. REFEREE-2's side:
  its report 8afe203a (12:55:35Z, before REFEREE's report 3c40dc18, 13:15:00Z) proves it in the COPY item, §3 l. 69-78 (the same lines at
  f92b278a); REFEREE-2 25 confirms the attribution on L-3, R2-N5-STAIR-L3.md l. 18-19 «My predecessor's report
  docs/referee-2/R2-N5-STAIR.md (claude/referee-2 f92b278a, committed 13:06:38Z) proves COPY's converse in its COPY item, l. 69-78.», l.
  22 «It concludes «the non-constant bits of v and z correspond bijectively and in order».», l. 26 «So «written independently by REFEREE
  and REFEREE-2» is right for my side. «referee-originated» is right as well, under L41.» REFEREE's side: §6 l. 67-74 in 3c40dc18 (written
  without opening docs/referee-2/, l. 6); §C addendum 2 l. 218-219 «This is correct under L41: I wrote G-ST-1, REFEREE-2 wrote P-1, and
  each signed the other's.» So L-3's tail clause «written independently by REFEREE and REFEREE-2» is confirmed by both.
  INDEPENDENCE: REFEREE l. 6 «Independence: I opened no docs/referee-2/ file for this packet.»; §C l. 162 «I opened no docs/referee-2/
  file. REFEREE-2's items are known to me only as the fixes file quotes them.» REFEREE-2 l. 4 «Independence: written before opening any
  docs/referee/ file on STAIR.»; R2-N5-STAIR-L1.md l. 8 «Written without opening REFEREE's verdict on L-1. The fixes file quotes REFEREE's
  report text, and I read those quotes.»; R2-N5-L2-confirm.md l. 2 «Both written without opening REFEREE's verdicts.» G-ST-1's repair was
  written by each referee before seeing the other's report (8afe203a 12:55:35Z; 3c40dc18 13:15:00Z). No review imported lane code (REFEREE
  l. 99; REFEREE-2 l. 107); the lane's scripts ran only as the pinned blocks (REFEREE l. 113-114). The two L-3 word diffs (d6da0e93,
  faa8dac9) carry no independence sentence; each re-hashed L-3 and diffed it against L-2 itself.
  Differences, resolved: G-ST-1 a gap for REFEREE, a precision (P-1) for REFEREE-2, the same argument, signed by both; the §11 draft's
  line items numbered differently (to check (3)); R162 re-run by REFEREE-2 only. On L-3: REFEREE-2 25 counts «four replacements» and «852
  → 865 words» (R2-N5-STAIR-L3.md l. 4, l. 6), REFEREE «Exactly the Lead's list» of four (l. 212-220); the same changes (this entry's own
  count, by whitespace token: 887 → 899, five non-equal opcodes, the gloss change being two). REFEREE-2 25 dates REFEREE's G-ST-1 to
  «claude/referee a61a258b, 13:41:23Z» (l. 24); the G-ST-1 text is already in 3c40dc18 (13:15:00Z; a61a258b, +7/−3, added STAIR-L8
  only). Both commits are after 8afe203a (12:55:35Z), so the attribution stands. No disagreement in substance; no ruling was needed.
- TARGET.md diff: «n := |V| (V the vertex set of the game)» is TARGET.md §1 l. 8's n («n = |V|, m = |E|, d = |pr(V)| ≤ n + 1.»), V
  TARGET's vertex set (l. 6); games are TARGET.md §1 games (REFEREE-2 l. 167 «Precision: n is bound fleet-wide by TARGET.md l. 8.»). The
  line (L-3) makes no M4 claim and no TARGET claim; its own scope clause reads «REDUCTIONS and EQUIVALENCES (no count is bounded here;
  G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim; the proof of DESC-COPY uses COPY's converse, whose proof is
  referee-originated (G-ST-1 = P-1, written independently by REFEREE and REFEREE-2; docs/new/P-N5-STAIR-fixes-box112.md entry 1))» (L-3
  verbatim, by script). REFEREE on L-3, §C addendum 2 l. 222-223 «The scope words REDUCTIONS / EQUIVALENCES, G-N5-TIME OPEN, not M3 and
  not a TARGET.md claim are unchanged.» REFEREE l. 144-145 «TARGET.md diff: «REDUCTIONS and EQUIVALENCES (no count is
  bounded here; DESC-LIN is a CONJECTURE; HDEPTH is DEAD (hit_b6a_1); G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md
  claim)» ✓. No algorithm claim.» (at the §11 draft); REFEREE-2 l. 160-161 «TARGET.md scope words: «REDUCTIONS and EQUIVALENCES (no count
  is bounded here; … G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim)» ✓.» and L1 l. 26 «TARGET.md scope words in
  the tail: ✓.» Not a claim of TARGET.md §1 or §2 (lemmas on lcp sums, oriented bits, resets and descents of W inside W-runs, and two
  equivalences between counts; no bound on a W-run, on a run or on running time; no algorithm claim); not a step-4 pass. GAPS G-N5-TIME:
  open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER R98's UPDATE of G-N5-TIME (PENDING: R98's draft is being rebuilt on ODD line
L-3; at a250e898, GAPS unchanged since 9777660f, the last UPDATE on l. 11 is R97's, «UPDATE 2026-10-31 07:02Z: RESULTS R97 (P-N5-SRC;
CHECKER C107 449cb6fc) …», before the row's closing « |»), built by script (upd99L3.py = upd99.py run on L-3) only from the clauses of
the title line L-3, with R94's-R98's construction (labels behind their clauses; the scope tail as in R95's-R98's UPDATE: the L41 clause
stays inside the scope words, before the source note, which is kept). L-3 has no DESC-LIN clause, so the UPDATE has none (C109 E-3). The
same script reproduces R97's landed UPDATE, R98-draft l. 526 at 78e946a6 and, run on L-2, this draft's previous l. 574 (a06b8884) byte
for byte. L-3 holds fourteen "|"; the UPDATE holds none: (q1) «n := |V| (V the vertex set of the
game)» → «n := the number of vertices of V (V the vertex set of the game)»; (q2) «|F| := q − p its number of transitions» → «q − p is its
number of transitions»; (q3) the other five «|F|» → «the number of transitions of F»; these replacements are not title text (to check
(9)). Date «2026-10-31» (the landing date; corrected at landing if later); time and CHECKER commit to be filled at landing:
UPDATE 2026-10-31 <HH:MM>Z: RESULTS R99 (P-N5-STAIR; CHECKER C109 <checker>) [refereed-only] LANDED: N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum; for S4a at a transition k → k + 1, σ_(k+1) is the pointwise optimum of S4a's one-player arena at k); premises RESULTS R15 (a), (d), R91 (Lemmas XW, W-MON), R93 (Fact LEX) and [PLAY] := P-N5-SRC §2 (proof of RESULTS R97 PLAY-CAUSE^S)), with: a run is the sequence of states (σ_k, τ_k), a transition is written k → k + 1 (states k, k + 1), and an Even vertex y switches at k if σ_(k+1)(y) ≠ σ_k(y); n := the number of vertices of V (V the vertex set of the game); values (c, P, ℓ) (cycle node, path set, length) as in SPEC S1, ⊴, ◁, ⊵, ▷ the SPEC S1 order (better for Even) and its strict and reverse forms; Ξ_k := Ξ_{σ_k} (SPEC S1); W-run F = [p, q] := RESULTS R89's (a maximal run of consecutive states of one τ-stretch none of whose transitions is an S4c fallback or changes λ_W, the cycle-node map of W), with τ and C := {v : λ_W(v) = v} fixed on F, and q − p is its number of transitions; for a state k of F, W_k := the [S1-val] valuation of the (σ_k, τ)-plays, and v's successor at k is σ_k(v) for Even v and τ(v) for Odd v; T1_F := the transitions of F with W_(k+1) = W_k, WCT_F := the number of transitions of F − T1_F, and WCH_F(v) := the transitions of F changing W(v); CS(x) := RESULTS R93 (a)'s coordinate sequence of a value x (length n + 2), and lcp the length of the longest common prefix; BW_k := Σ_v lcp(CS W_k(v), CS W_q(v)), AF_k := Σ_v lcp(CS Ξ_k(v), CS W_q(v)), A_k := Σ_v lcp(CS Ξ_k(v), CS W_k(v)), and N_F := the transitions of F at which BW does not rise and A does not fall; for a value x = (c, P, ℓ), β(x) ∈ {0, 1}^(3n + 1) consists of one bit per rank r from the most relevant down, [r ∈ P] if r has even priority and [r ∉ P] if odd, followed by the threshold bits [sl ≥ j] for j = −n, …, n, where sl := ℓ if c has odd priority and −ℓ if even; GOOD_F(v, b) (BAD_F(v, b)) := the transitions of F flipping bit b of β(W(v)) from 0 to 1 (from 1 to 0, a RESET), and TD_F := Σ_(v, b) BAD_F(v, b); the first-difference position of a change of W(v) is the least index at which β changes (0 = most significant), and a DESCENT of v at k is a change of W(v) at k whose first-difference position is strictly larger than that of v's previous change of W(v) on F; DESC_F(v) := v's descents on F and DESC_F := Σ_v DESC_F(v): for every N5 run on every game, every W-run F = [p, q] of it, every transition k → k + 1 of F, every vertex v and every bit position b: for sequences x, y, z of one length in lexicographic order, x ≤ y ≤ z implies lcp(x, z) = min(lcp(x, y), lcp(y, z)) (Lemma SANDWICH); BW_k and AF_k are non-decreasing on [p, q], and on any run of S4a steps Σ_v lcp(CS Ξ_k(v), CS Ξ_end(v)) is non-decreasing, end its last state; all three lie in [0, n(n + 2)] (Corollary FROZEN); with M := n(n + 2) + 1, the number of transitions of F ≤ (M + 1)·n(n + 2) + M·N_F, and T1_F ≤ N_F ≤ the number of transitions of F (Lemma BW-ACC); for values x, y with one cycle node, x ◁ y iff β(x) is lexicographically smaller than β(y) (Fact BIT); GOOD_F(v, b) ≤ 1 + BAD_F(v, b) (Lemma BIT-ALT); every change of W(v) on F flips its first differing β-bit from 0 to 1 (Lemma FIRST-GOOD); WCT_F ≤ Σ_v WCH_F(v) ≤ n(3n + 1) + TD_F, so the number of transitions of F ≤ T1_F + n(3n + 1) + TD_F, and TD_F ≤ (3n + 1)·n·WCT_F (Theorem RESET-RED, an EQUIVALENCE); if v ∉ C has the same successor z at k and at k + 1, then β(W(v)) and β(W(z)) have the same flips at k, in the same directions, through a strictly increasing position map; C-vertices keep the value (c, ∅, 0) on F (Lemma COPY); every reset of W(v) at k is copied, through COPY, from a reset of W(y) at k, where y is the first Even vertex switched at k on v's (σ_(k+1), τ)-play before λ_W(v); hence TD_F ≤ n·Σ_k Σ_(y switched at k) (the resets of W(y) at k) (Corollary RESET-ROOT); if v ∉ C has a descent at k and did not switch at any transition from its previous change of W(v) on F to k, then its successor at k has a descent at k (Corollary DESC-COPY); WCH_F(v) ≤ (3n + 1)(1 + DESC_F(v)) (Lemma ASC-RUN); WCT_F ≤ n(3n + 1) + (3n + 1)·DESC_F, so the number of transitions of F ≤ T1_F + n(3n + 1) + (3n + 1)·DESC_F, and DESC_F ≤ n·WCT_F (Theorem STAIR, an EQUIVALENCE): REDUCTIONS and EQUIVALENCES; no count is bounded here; the proof of DESC-COPY uses COPY's converse, whose proof is referee-originated (G-ST-1 = P-1, written independently by REFEREE and REFEREE-2; docs/new/P-N5-STAIR-fixes-box112.md entry 1) (P-N5-STAIR, docs/new/P-N5-STAIR-box112.md; L-NEW successors 41-42; fixes docs/new/P-N5-STAIR-fixes-box112.md entries 1-7). G-N5-TIME stays open.

Addendum 1 (subagent, for the Lead; does not land): (1) Both L-2 verdicts are on origin lane branches (claude/referee 45b63517,
claude/referee-2 cf5157fe); cf5157fe is on the local trunk 2640a8bc (merge eeec4da6) but NOT on origin trunk eb33b45a: push trunk before
landing. No placeholder token is left except <HH:MM> and <checker> in the UPDATE and «checker PENDING» in the title fill. (2) Quote sweep
(script q99.py, outermost «…», «\|» read as «|», whitespace joined, split at «…»): entry (title + body) l. 302-564: 193 quotes, 188 parts of 6+ characters, all 188 found in the sources (packet, fixes, L-1, L-2, R-N5-STAIR.md at 45b63517, R2-N5-STAIR.md at f92b278a, R2-N5-STAIR-L1.md at 6f45b443, R2-N5-L2-confirm.md at cf5157fe, R162-desc.md at 54832628, D-ODD-1-starts.md, DECISIONS.md, RESULTS, GAPS, TARGET.md, C106-C108, LEAD-STATE.md, R98-draft.md, P-N5-SRC.md at 0521fb82, check.sh at 6903f1b3, this draft's pin outputs and UPDATE); to-check notes l. 1-301: 316 quotes, 252 parts, 244 found, 8 not found, all this draft's own words or schemata, not quotes of a source («at the §11 draft», «### R99» twice, «… entries 1-6), CHECKER PASS (…)», «REFEREE STAIR-Ln», «REFEREE-2 STAIR-Ln», « (2026-10-31) — REDUCTIONS and EQUIVALENCES (X) (source)», «: REDUCTIONS and EQUIVALENCES; X′ (source). G-N5-TIME stays open.»); GAPS preamble and UPDATE l. 565-574: 9 quotes, 7 parts, all found. (3) Checked by script after the fill: l. 302 = «### R99 [refereed-only] » + L-2 without its newline + «, CHECKER PASS (docs/checker/C109.md, checker PENDING)» (True); l. 574 = upd99.py's output (True), 0 "|", one <HH:MM>, one <checker>; l. 565 blank; the only «### R» heading is l. 302. (4) NOT RUN / NOT DONE: Oink (the pinned blocks do not call it); R162's own pins and table (not re-run by me; REFEREE-2's §4b and L-NEW box 113's cp_K4 block are the reproductions, the latter re-run PASS here); REFEREE's and REFEREE-2's own tools (not re-run); L-NEW's box 113 repaired-start re-runs of fixes entry 3 (|F| 151, DESC 0 on sbq2_K8_m16_fixed.start: taken from the fixes file, not re-run; the box 99 block that pins that start passed). (5) For the Lead: FLAGS D-1 (L41 tail clause for G-ST-1) and D-2 (lane-level DEAD in the tail) are CHECKER questions; I did not change the line. If CHECKER asks for a line L-3, the title, the body's quotes of the line (TARGET.md diff, line history) and the UPDATE are rebuilt from it with the same scripts. Scratch scripts and outputs (not committed): wdiff99.py, upd99.py / upd99.txt, fill99.py, sum99.py, q99.py / q99.out, check_6903.sh, pin99a.out, pin99b.out, pin99.out, in the session scratchpad.

Addendum 2 (Lead, 2026-10-31 21:33:01Z by date -u, read in the same command as this addendum's write; for C109 Add. 1; does not land). The draft is rebuilt on P-N5-STAIR line L-3 (l-new 7dc1eb7c, sha1 9db0b169aadcbc5f81b2c0157f124946bbf74ad9; fixes entry 7, fixes sha1 6e45b0e0684d06ba9258a466d96bc9829e096218), which closes CHECKER C109 (claude/checker 178b3e9e) E-1, E-2 and E-3 (option (i), Lead reading L43); both referees MATCH L-3 (REFEREE 21 d6da0e93, R-N5-STAIR.md §C addendum 2 l. 211-224; REFEREE-2 25 faa8dac9, R2-N5-STAIR-L3.md). The L-2 version is kept unchanged in the scratchpad as R99-draft.L2.md (sha1 a06b8884…, 579 lines). Changes, at the new line numbers: (1) l. 1: the header gains «REBUILT on line L-3 for C109 Add. 1» with this stamp. (2) l. 2-6: the status sentence now names faa8dac9 (local trunk a250e898 only, NOT on origin trunk a8b42b38) and says that the body describes L-3, history sentences say «at the L-2 object», and the to-check notes are L-2 history except where (R) says otherwise. (3) l. 7-23: new to-check note (R): the rebuild, D-1..D-4 RESOLVED by E-1..E-3 (D-4's «c» clash removed with the clause), the L-3 scan and figures, the new heading figures, and what changes in notes (1)-(14). (4) l. 24: the FLAGS label says «written on L-2 (RESOLVED at L-3, see (R))». (5) l. 320, TITLE: «### R99 [refereed-only] » + L-3 without its newline + the unchanged fill (scratch fill99L3.py; equal, byte for byte; 4,630 characters, 4,761 bytes, 14 "|"). (6) l. 326-327, Object: DESC-LIN's status: entry 4 = lane DEAD, entry 7 drops it (L43). (7) l. 347-369, line history: L-2's old tail quoted as «at the L-2 object»; C109 l. 16 and E-1..E-3 quoted; new step (4) L-3 (commit, sha1, trunk merge 83b5acc9, fixes entry 7, the four changes, L43 quoted); REFEREE 21 and REFEREE-2 25 verdicts on L-3 quoted with their SHAs; «the title is L-3 verbatim»; the scope tail described as DEAD at L-1 and L-2, dropped at L-3, L41 clause added at L-3. (8) l. 377, 384, 408, 437, 439: «L-2» → «L-3» (notation; premises; COPY's two-way form «unchanged since L-1»; the line claims less; every claim clause). (9) l. 380-381, Claims signed: adds d6da0e93 and REFEREE-2 successor 25's faa8dac9. (10) l. 467-474, G-ST-1 bullet: L-3's tail clause quoted (C109 E-1); «At the L-2 object the tail did not say it»; both referees' L-3 confirmations of the clause quoted; COPY⁺ «not refereed here and not used» (C109 l. 44-45). (11) l. 482: «L-3 states neither». (12) l. 483-486, Fixes header: F0 + entries 1-7, three commits, 7dc1eb7c +55/−0, the file now 214 lines, sha1 6e45b0e0…. (13) l. 495-496: entry 4 marked history (R162 clause in L-1 and L-2, not in L-3; lane DATA). (14) l. 500-504: new entry 7 summary with quotes (l. 164-204 = C109 l. 39-79, by script). (15) l. 506: «entries 4-7 word the line». (16) l. 513-514, Not signed: no DEAD in L-3's tail; R162 is lane DATA. (17) l. 527-542, Honest limits: (i) «not stated by L-3»; (iii) rewritten: DESC-LIN not settled here; R162's DEAD was a line clause at L-1 and the L-2 object, dropped at L-3 (C109 E-3 (i), L43 quoted); R162 recorded as lane DATA (its table, the reproductions), no signed item depends on it; (iv) L-3's tail names the referee-originated repair; (v) L-3's gloss quoted, H_k only «at the L-2 object». (18) l. 591-594, Signatures: 45b63517 no longer called the referee head; §C addendum 2 d6da0e93 added (+15/−0, file 224 lines, sha1 bd70a85f…, trunk merge f3ef5852) with its verdict. (19) l. 601-614: cf5157fe now on trunk by eeec4da6 (origin too); REFEREE-2 25 faa8dac9 added (R2-N5-STAIR-L3.md, 39 lines, sha1 5b29a17f…, merge a20cf406, not on origin trunk) with its verdict; new paragraph «L41, REFEREE-ORIGINATED PROOF (G-ST-1 = P-1)»: both wrote the converse independently (8afe203a 12:55:35Z before 3c40dc18 13:15:00Z), REFEREE-2 25's confirmation (l. 18-19, 22, 26) and REFEREE's (l. 218-219) quoted. (20) l. 620-621: the two L-3 word diffs carry no independence sentence. (21) l. 623-627, Differences: four replacements / 852 → 865 words (REFEREE-2 25) against this draft's 887 → 899 whitespace tokens and five opcodes; REFEREE-2 25 dates REFEREE's G-ST-1 to a61a258b, but the text is already in 3c40dc18 (a61a258b added STAIR-L8 only); both after 8afe203a, so the attribution stands. (22) l. 630-634, TARGET.md diff: L-3's scope clause verbatim (by script) and REFEREE addendum 2 l. 222-223 quoted. (23) l. 642-648, GAPS preamble: built by upd99L3.py (= upd99.py on L-3; R98 control now against R98-draft at 78e946a6, because another agent is editing the working copy); no DESC-LIN clause; the L41 clause before the source note; GAPS at a250e898. (24) l. 652, UPDATE: rebuilt from L-3 by script. Controls in the same run: R97's landed UPDATE (True, 4,179 bytes), R98-draft l. 526 at 78e946a6 (True, 4,253 bytes), and L-2 → this draft's previous l. 574 (True, 4,776 bytes). Result: one line, 0 "|", one <HH:MM>, one <checker>, 4,873 bytes, 927 tokens; word diff against the old l. 574: «the» → «S4a's», «H_k);» → «at k);», the DESC-LIN clause → the L41 clause (position kept, before the source note), «1-6).» → «1-7).». Quote sweep after the rebuild (scratch q99L3.py = q99.py with L-3, fixes at 7dc1eb7c, R-N5-STAIR.md at d6da0e93 and 3c40dc18, R2-N5-STAIR-L3.md at faa8dac9, R2-N5-STAIR.md at 8afe203a, C109 at 178b3e9e and the new UPDATE added; R98-draft read at 78e946a6): entry (title + body) l. 320-640: 238 quotes, 232 parts of 6+ characters, all 232 found; to-check notes l. 1-319: 342 quotes, 262 parts, 256 found, 6 not found, all this draft's own words or schemata («at the §11 draft», «… entries 1-6), CHECKER PASS (…)», «REFEREE STAIR-Ln», «REFEREE-2 STAIR-Ln», and the two UPDATE schemata of (9)); GAPS preamble and UPDATE l. 641-652: 9 quotes, 7 parts, all found. A second check took 31 quotes added in this rebuild that cite a line (C109, DECISIONS L43, fixes entry 7, REFEREE addendum 2, R2-N5-STAIR-L3.md) and found each at its cited lines. NOT RUN / NOT DONE in this rebuild: the pins (unchanged: L-3 changes no claim and no pin; CHECKER re-ran box 110, 111 and 113 at 6903f1b3); Oink; the referees' tools. Scratch (not committed): fill99L3.py, upd99L3.py / upd99L3.txt, q99L3.py / q99L3.out, R99-draft.L2.md.
