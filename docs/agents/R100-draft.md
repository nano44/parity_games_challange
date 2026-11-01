# Draft RESULTS R100 (Lead, 2026-10-31 22:37:35Z by date -u, read in the same command as the fill of this file; subagent draft; packet, its frozen line 954af7be, line files L-1 / L-2, fixes F0 + entries 1-3, REFEREE's R-N5-ROOT114 (report, §C, L-2 addendum) and REFEREE-2's R2-N5-ROOT114, R2-N5-ROOT114-L1 (with Addendum 1), R2-N5-ROOT114-L2 read at the origin heads fetched at the start of this draft, 2026-10-31 22:19Z (l-new 401d283a, referee af9cd763, referee-2 3bb41a4c, checker 178b3e9e; origin trunk 6d653c3f, local trunk head f3c2df11); L-NEW's box 113 pin block of experiments/new/check.sh re-run 2026-10-31 22:23:00Z-22:23:01Z (7988e2f4), one supporting block 22:23:01Z-22:23:03Z; DATA re-summed 2026-10-31 22:23:23Z) — to CHECKER C110
The L-2 verdicts REFEREE af9cd763 and REFEREE-2 3bb41a4c are on origin lane branches and on the local trunk head f3c2df11 (merge
f1b1044e, 22:19:06Z), NOT on origin trunk 6d653c3f: the Lead pushes trunk before landing. Every other commit cited here is on both. R98 and
R99 are NOT landed (to check (0)); this packet's premises [COPY], [STAIR] and [FUEL-COUNT] are theirs. In the body (title + entry),
sentences about an earlier line revision say «at the frozen line» or «at the L-1 object»; every other sentence of the body describes L-2.
to check: FLAGS FIRST (the E-item pre-check of L-2 the Lead asked for, against C106 E-1, C108 E-1, C109 E-1 / E-2 / E-3 and L43; L-2 NOT
changed by me; details in (5)-(7) and D-1 to D-7). Three hits or near-hits (F-1 to F-3), two landing items (F-4, F-5), two classes clean.
- FLAG F-1, STALE PINS INSIDE THE LINE (the C106 E-1 class, a superseded revision cited as current; in the line, not in the body). L-2 cites
  «P-N5-STAIR (Lemma COPY in both directions and Theorem STAIR, as in its line L-2: l-new 6903f1b3, docs/new/P-N5-STAIR-line-L2.txt, sha1
  44f56e96d41d45653c4b7bc2f140c587e8e407e6)» and «β, first-difference positions, descents and DESC_F as in P-N5-STAIR's line L-2». STAIR
  L-2 is the line CHECKER C109 FAILED (178b3e9e); R99 lands STAIR line L-3 (9db0b169, l-new 7dc1eb7c; both referees MATCH). L-2 also cites
  «P-N5-ODD (Corollary FUEL-COUNT: l-si 0afc0d70a, docs/si/P-N5-ODD-box57.md §6, sha1 03eec41d, with its fixes entries 1-2)»; R98 lands
  ODD line L-3 (f83b169e, l-si 2f8e5b2e) with fixes F0 + entries 1-6. The CONTENT ROOT imports is unchanged: STAIR L-2 → L-3 touches only
  the R57 gloss, the DESC-LIN clause, the L41 clause and the entries count (R99-draft (R)); ODD fixes entries 3-6 are line revisions, the
  D-ODD-1 DATA defect, the (y, z) binder of FUEL-COUNT (ODD-L5) and the DATA clause. But the fix both referees wrote says what to cite once
  the premises land: REFEREE ROOT-L2 «Fix: cite each by its landed RESULTS label once it lands; until then, by commit and sha1»; REFEREE-2
  ROOT114-L2 «cite line L-2 (l-new 6903f1b3, sha1 44f56e96), or R-number once landed» and P-4 «cite P-N5-ODD by its landed R-number (R98
  draft at C108) or its current line, once landed», «optional; Lead decides». R100 lands after R98 and R99, so at landing the line cites by
  commit what RESULTS then holds as R98 / R99. CHECKER decides: accept the commit pins (content-identical; checked in (5)), or a line L-3
  citing RESULTS R99 (Lemma COPY, Theorem STAIR; β and descents) and RESULTS R98 (Corollary FUEL-COUNT).
- FLAG F-2, L41 (the C109 E-1 class; contested). L-2 has 0 «referee-originated». REFEREE-2 says none is needed: R2-N5-ROOT114.md l. 177
  «There is no referee-originated proof (L41), so no «referee-originated» tag is needed.», L1 l. 45 «no referee-originated proof (L41 tag
  not needed)»; REFEREE is silent. That is true of THIS packet's own proof text: F0 and both reports record no gap and no repair of a proof.
  But three proofs rest on referee-originated text of the premise packets: DESC-ROOT applies «[COPY] (both directions)» (packet l. 63),
  i.e. COPY's converse, whose proof is G-ST-1 = P-1 (the clause R99's line L-3 adds for DESC-COPY under C109 E-1); ORIGIN-NEW's Φ step is
  «as in [COPY]'s proof (G-ST-1)» (packet l. 97; REFEREE §4 l. 63 «as in G-ST-1»); FUEL-ROOT-STAIR uses FUEL-COUNT, whose proof carries
  the referee-originated repair G-ODD-2 (R98's title: «the proofs of FUEL-LEX and FUEL-COUNT carry referee-originated repairs»). C109 E-1
  was a same-packet use («DESC-COPY needs COPY's converse»); here the use is through a cited premise whose own landing line carries the
  clause, while the pin in L-2 is STAIR L-2, which does not (C109 l. 42 «L-2 contains «referee-originated» 0 times.»). CHECKER decides
  whether L41 reaches through a premise; if yes, a line L-3 adds a tail clause naming G-ST-1 = P-1 and G-ODD-2.
- FLAG F-3, «root descent» UNDEFINED (the C109 E-2 class). The tail's DEAD clause reads «every root descent is a fuel re-route»; «root
  descent» occurs once in L-2 and is defined nowhere in it. L-2 defines descents «of type R» and uses «R-descent» (twice). REFEREE's L-2
  addendum reads the clause as R-descents (l. 202 «every R-descent of every W-run is a fuel re-route»; l. 203 «its terms (R-descent, fuel
  re-route) are defined in the line»), REFEREE-2 L2 l. 12 «No free symbol». A one-token move «root descent» → «R-descent» would close it.
- FLAG F-4, NAME CLASH «P-N5-ROOT» (landing item). RESULTS R74 already uses the name for ANOTHER packet: l. 3878 «packet P-N5-ROOT,
  docs/si/P-N5-ROOT-box20.md» (L-SI box 20, l-si freeze ced5cf27); GAPS l. 11 carries «RESULTS R74 (P-N5-ROOT + addendum; CHECKER C83)».
  «P-N5-ROOT» occurs 3 times in RESULTS (all R74) and once in GAPS. The title's source parenthesis names the file («(P-N5-ROOT,
  docs/new/P-N5-ROOT-box114.md; …)»), which disambiguates; the UPDATE head «RESULTS R100 (P-N5-ROOT; CHECKER C110 <checker>)» does not.
  Suggestion (not applied; the Lead's form kept): RESULTS R100 (P-N5-ROOT box 114; ...). Both referees name their files ...114 for this
  reason (REFEREE l. 6-7; REFEREE-2 l. 3). The earlier REFEREE report on R74's packet is docs/referee/R-N5-ROOT.md, first commit 619fccf2
  (2026-10-26, REFEREE's report, not the packet).
- FLAG F-5, UPDATE DATE (landing item, C106 E-2). The stamp is «UPDATE 2026-10-31 <HH:MM>Z»; this draft is written after 22:19Z. If R100
  lands on 2026-11-01 or later, the date is corrected at landing.
- CLEAN: C108 E-1 (DATA): L-2 has 0 «DATA», 0 «corpus», 0 «games», 0 «referee», no count of a data set; its one «both» is «Lemma COPY in
  both directions». C109 E-3 / L43 (asymptotic DEADs): 0 «R162», 0 «R163», 0 «DESC-LIN», 0 «DESC*», 0 «c·n», 0 «O(», 0 «linear»; the
  one DEAD left, «every root descent is a fuel re-route» DEAD (frz32: old-edge relays), is a universal statement with no constant,
  refuted by one instance exceeding an explicit bound (R^old_F = 3 > 0 on frz32), reproduced by both referees' own engines and accepted
  by both under L43 (body, Not signed; (7) D-6).
- Soft spots of the strict symbol test, no referee raised them: D-2 «λ_W» (once; carried by the label R89 only), D-3 «V» unglossed (R96
  precedent), D-4 Σ_(y,z) rebinding y, z, D-5 N_F(y, z) beside R99's N_F (BW-ACC), «KEY» beside R38 (a)'s KEY, «RELAY» beside R71 / R72's
  RELAY events, D-7 frz32 named without path, commit or sha1 (REFEREE's optional precision).
(0) PLACEMENT, R98 AND R99 PENDING. R100 goes after R99. R97 is LANDED (trunk 9777660f, 2026-10-31 07:02:34Z; CHECKER C107 449cb6fc
PASS). R98 and R99 are NOT landed: their drafts docs/agents/R98-draft.md (sha1 201be10ddf82c9172ae2f57705223a9c0ebadbe8, 639 lines) and
docs/agents/R99-draft.md (sha1 c0f34f8d1c306681ce2378bccd54c2b3db30af29, 659 lines), both last changed by 6d653c3f (21:51:04Z), are
rebuilt on ODD L-3 / STAIR L-3 for CHECKER C108 Add. 1 / C109 Add. 1 (not yet run: checker head 178b3e9e). docs/RESULTS.md at the local
trunk head f3c2df11 (identical at origin trunk 6d653c3f) has sha1 24280f5226c8616b9de88ee16eaf86c727f4a135, 8,816 lines, last changed by
9777660f (the R97 landing). «### R97» is l. 8032 (entry l. 8032-8294, l. 8295 blank); «## Dead ends (kept;» is l. 8296; «### R98»,
«### R99», «### R100» and «R100» occur 0 times in RESULTS and in GAPS (sha1 a0b8f8dd4c0fa8538cd21e54ed2d3822f28d9182, 23 lines, last
changed by 9777660f). Every RESULTS line number here and in the entry is at 24280f52, BEFORE R98 (as R99's draft did while R98 was
pending); R98's and R99's insertions go after l. 8295, so no RESULTS line number cited here moves. R100's entry goes after R99's entry and
its blank line, before «## Dead ends (kept;», with one blank line after it (R97's layout). R100 cannot land before both: its premises
[COPY], [STAIR] (P-N5-STAIR = R99) and [FUEL-COUNT] (P-N5-ODD = R98) are signed but not landed (REFEREE l. 10-12; REFEREE-2 l. 27). The
Lead RE-CHECKS (6) (labels and names, with R98 and R99 in), (9) (GAPS, after R98's and R99's UPDATEs) and F-1 at landing.
(1) TITLE. The title is the line file docs/new/P-N5-ROOT-line-L2.txt (l-new 7988e2f45a47e2a50a121773ea1f47874cfce086,
2026-10-31T20:57:08Z, the file's only commit, sha1 c9c6b3801ed9cc3cb5017f240d8e0d0f2610efba; identical at l-new head 401d283a,
at origin trunk 6d653c3f and at the local trunk head f3c2df11; first on trunk by merge a20cf406, 21:23:35Z), verbatim: one line, no outer
quotes, no final period, 4,290 characters (4,466 bytes plus the newline), 869 whitespace tokens. NO HEADING MARKER, verified by script: the
file begins «N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise», with no «#», no «R??» and no lane tag (Lead reading L41 «Lanes
write line files without a heading marker (C104 N-1).»). So, as in R95-R99, NOTHING is stripped: the heading is the level-3 marker, then
"R100 [refereed-only] ", then the file without its newline, then the fill. «2026-10-31» occurs exactly once in L-2, in « (2026-10-31) —
REDUCTIONS and EQUIVALENCES» (by script), so NO date is inserted (the R93-R99 rule). The line holds twelve "|": «|V|» once and «|F|» five
times; they stay in the heading (R91, R93-R99 carry "|") and are replaced in the GAPS UPDATE only ((9)). The checker fill ", CHECKER PASS
(docs/checker/C110.md, checker PENDING)" is appended as in R90-R99 (no space before the comma); L-2 ends «… entries 1-3)», so the heading
ends «… entries 1-3), CHECKER PASS (…)». Built by script (scratch fill100.py: assert the sha1 c9c6b380…, equality with the working-tree
file, one line, no marker, one «2026-10-31», twelve "|"; prepend "### R100 [refereed-only] ", append the fill) and re-checked after
writing this file: equal, byte for byte. Heading: 4,369 characters, 4,545 bytes; sha1 of the heading line without its newline
1eeda61e33e54941646c50f52e20d7d2876869cd, with its newline b239c54e0e4f1237d4b85091fca842776b510e76; it is l. 312.
Title features shared with landed titles (no new precedent): the scope words «REDUCTIONS and EQUIVALENCES» (R95, R99-draft); a lane DEAD
in the scope tail naming its instance (R90 «CONJECTURE REP-LIN is DEAD (L-RED R128, latew_K20_m32)», R95 «CONJECTURE BIP-REL-1 is DEAD
(L-RED R143, rel2_R2_n82, l-red 717f407a)»); a source parenthesis after the scope tail (R96, R97); landed entries cited by number (R57,
R15, R91, R93, R97, R89); a premise whose text is another lane's packet section, «P-N5-SRC §2 (proof of RESULTS R97 PLAY-CAUSE^S)» (R98 /
R99 drafts, not landed); guillemets inside a title (R98-draft, C108 N-2). NEW in a title, for CHECKER: (i) premises cited by lane commit +
sha1 of packets that land as R98 / R99 BEFORE this entry (F-1); (ii) one premise restricted to one claim, «and, for (Corollary
FUEL-ROOT-STAIR) only, P-N5-ODD (…)»: the label occurs twice in the line, once in that premise and once as the claim label ((9)).
(2) LINE HISTORY: the frozen line docs/new/P-N5-ROOT-line.txt (sha1 954af7be0e7771edade79a5f5e936e4ab46bcbda, committed with the packet in
ed2fdaf2, 14:53:59Z; 3,642 characters, 736 tokens, twelve "|", no marker, one date; the line both reports reviewed) → L-1 a41df25b
(docs/new/P-N5-ROOT-line-L1.txt, l-new be131555, 19:32:23Z, 4,364 characters, 881 tokens; fixes F0 + entries 1-2) → L-2 c9c6b380
(…-line-L2.txt, 7988e2f4, 20:57:08Z, 869 tokens; fixes entry 3). The frozen line and L-1 are history, not the title. Each line file has one
commit (git log on l-new). Word diffs measured for this draft (difflib over whitespace tokens, scratch wdiff100.py):
- frozen → L-1: 736 → 881 tokens, 20 non-equal opcodes, 716 tokens in common: a token edit, every change one of: the STAIR pin «as in its
  line L-1, docs/new/P-N5-STAIR-line-L1.txt)» → «as in its line L-2: l-new 6903f1b3, docs/new/P-N5-STAIR-line-L2.txt, sha1
  44f56e96d41d45653c4b7bc2f140c587e8e407e6)» and «… DESC_F as in P-N5-STAIR's line L-2» (ROOT-L2 = ROOT114-L2); the ODD pin (ROOT-L2,
  P-4); «with k → k + 1 a transition of F,» in ROOT CHANGE (ROOT114-L1); the KEY, the key of a fuel re-route and HC_F with «at a
  transition ≤ u» (ROOT-L3 = P-3); the binder «, every vertex v, every Even y, every vertex z and every transition k → k + 1 of F»
  (ROOT-L1); «previous change of W(v) at k′»; «if y switches» (the word «Even» moved to the binder); ROOT-SPLIT «if (y, k) is a root
  change and k − 1 ∈ F, then (y, k) is …»; the tail clause «DESC*-LIN DEAD in the weak form (L-RED R163);» (REFEREE's optional precision,
  §8 l. 127); «L-NEW successor 42; fixes docs/new/P-N5-ROOT-fixes-box114.md entries 1-2)». = REFEREE §C l. 150-160 («Every change maps to
  entry 1 (my ROOT-L1..L3) or entry 2 (REFEREE-2's ROOT114-L1 / L2), and nothing else changed, except the new R163 tail clause (below).»);
  = REFEREE-2 R2-N5-ROOT114-L1.md l. 8-26 (ten items, «every change, nothing else»).
- L-1 → L-2: 881 → 869 tokens, 2 non-equal opcodes: «DESC-LIN DEAD (L-RED R162); DESC*-LIN DEAD in the weak form (L-RED R163);» deleted;
  «1-2)» → «1-3)». = fixes entry 3 l. 121-122 («word-diff vs a41df25b is exactly [-DESC-LIN DEAD (L-RED R162); DESC*-LIN DEAD in the weak
  form (L-RED R163);-] and [-1-2)-]{+1-3)+}»); = REFEREE addendum l. 197-198 («Nothing else changed. The sha1 is re-hashed and
  matches.»); = REFEREE-2 R2-N5-ROOT114-L2.md l. 4-8 («Nothing else. Byte test True»).
- frozen → L-2, by content: the k = q boundary excluded (ROOT114-L1); v, y, z, k bound (ROOT-L1); STAIR and ODD pinned (ROOT-L2,
  ROOT114-L2); KEY and HC_F defined (ROOT-L3, P-3); the frozen tail's «DESC-LIN DEAD (L-RED R162)» dropped (L43); the source note «fixes …
  entries 1-3». No inequality of a signed statement differs between the packet and L-2 ((4) checks each clause).
(3) THE LINE AT BOTH REFEREES. L-2 (the title): REFEREE successor 21, docs/referee/R-N5-ROOT114.md «### §C addendum: line revision L-2
(l-new 7988e2f4, docs/new/P-N5-ROOT-line-L2.txt, sha1 c9c6b3801ed9cc3cb5017f240d8e0d0f2610efba; fixes entry 3) (21:24Z 2026-10-31 by
date -u)» l. 196-207 (af9cd763, 21:24:55Z, +13/−0): l. 199 «ROOT-L4 and ROOT-L5 are met, by removal, in line with the Lead's ruling
L43.»; l. 207 «Verdict on L-2: MATCHES (Opus 5.5, D15). No REQUIRED change remains on the P-N5-ROOT line.» REFEREE-2 successor 25,
docs/referee-2/R2-N5-ROOT114-L2.md (3bb41a4c, 21:24:48Z, new file, 19 lines, sha1 e486277c1e6e49593a40bc7a8c9e9495678fbd5d): l. 2
«(re-hashed: match)»; l. 10 «No R162, R163, DESC-LIN or DESC* text remains, so L43 is met.»; l. 14 «Verdict: **MATCHES** (Opus 5.5,
D15). All my ROOT line items are closed.» Both commits are on the local trunk only (header).
L-1: REFEREE §C (74025e44, 20:01:05Z, +51/−0) l. 145-194: l. 161 «ROOT-L1 ✓, ROOT-L2 ✓, ROOT-L3 ✓.»; l. 193-194 «Verdict on L-1: does
NOT yet match. It needs ROOT-L4 (define and pin DESC-LIN / DESC*-LIN) and ROOT-L5 (R163 as DATA, not DEAD). Everything else MATCHES (Opus
5.5, D15).» REFEREE-2 R2-N5-ROOT114-L1.md (83c1838f, 20:00:13Z, new file, 56 lines): l. 51 «**MATCHES** (Opus 5.5, D15). All my ROOT line
items are closed.»; its Addendum 1 (faa8dac9, 20:28:55Z, +8/−0, l. 58-64), after L43: l. 61 «So I agree with REFEREE's ROOT-L4 / L5
(74025e44): drop both, or restate them as DATA with numbers.» The referees AGREE on L-1 after Addendum 1 (two REQUIRED items, one move:
drop both clauses).
Frozen line: REFEREE l. 25 «REQUIRED CHANGES ROOT-L1 to ROOT-L3 (§8)», l. 134 «Verdict: the line does NOT yet match. It needs ROOT-L1 to
ROOT-L3.»; REFEREE-2 l. 183 «Verdict on the line: **REQUIRED** (ROOT114-L1, ROOT114-L2). Then a word-diff of the revision.»
LINE-ITEM NAMES: each referee numbers its own items. REFEREE ROOT-L1 (bind v, k, k′, y, z) ⊃ REFEREE-2 ROOT114-L1 (bind k to transitions of
F, with the k = q counterexample; REFEREE §C l. 167-168 «My ROOT-L1 fix (binding k to the transitions of F) would have excluded the
case, but I did not see that the unbound reading is false at k = q. REFEREE-2 found that.»); REFEREE ROOT-L2 = REFEREE-2 ROOT114-L2 (STAIR
pin) + P-4 (ODD pin); REFEREE ROOT-L3 ⊃ REFEREE-2 P-3 («at a transition ≤ u»; REFEREE also the key); REFEREE ROOT-L4 / ROOT-L5 (L-1's
R162 / R163 clauses) = REFEREE-2 L1 Addendum 1. REFEREE-2's P-1 (NEW-FUEL with k unbound) and P-2 (R91 OPT-OFF) are recorded, not
applied (fixes entry 2 l. 86-88). Fixes F0 l. 13-18 maps REFEREE's items; entry 2 l. 74-88 REFEREE-2's.
(4) CLAIMS SIGNED = the items below, each SIGNED in BOTH referees' verdict tables (REFEREE "## Verdicts" l. 15-25 of R-N5-ROOT114.md;
REFEREE-2 "## 1. Claims table" l. 18-27 of R2-N5-ROOT114.md and its FINDINGS l. 189-190), AND stated by L-2 (checked clause by clause
against the packet statements for this draft):
| item (packet §, lines) | REFEREE (successor 21) | REFEREE-2 (successor 25) |
| --- | --- | --- |
| (a) Lemma DESC-ROOT with its counting (§2, l. 47-76; statement l. 53-57, counting l. 75-76) | l. 19 «SIGNED»; §2 l. 27-40 | l. 21 «**SIGNED**»; §3.1 l. 72-84 |
| (b) Theorem ROOT-STAIR, an EQUIVALENCE (§3, l. 78-82; statement l. 79-80) | l. 20 «SIGNED»; §3 l. 42-45 | l. 22 «**SIGNED**»; §3.2 l. 86-89 |
| (c) Lemma ORIGIN-NEW (§4, l. 84-100; statement l. 89-90) | l. 21 «SIGNED. The R15 A/B step was checked with special care (§4)»; §4 l. 47-66 | l. 23 «**SIGNED**, for k → k + 1 a transition of F (the packet's §1 setting)»; §3.3 l. 91-114 |
| (c′) Corollary RELAY (§4, l. 101) | l. 21 (same row); §4 l. 67 «RELAY is the contrapositive ✓.» | l. 24 «**SIGNED** (same reading)» |
| (d) Lemma NEW-FUEL (§5, l. 104-113; statement l. 104-106) | l. 22 «SIGNED»; §5 l. 70-75 | l. 25 «**SIGNED**»; §3.4 l. 116-122 |
| (e) Corollary ROOT-SPLIT (§5, l. 114-116) | l. 22 (same row); §5 l. 76 | l. 26 «**SIGNED**, for k a transition of F»; §3.5 l. 124-126 |
| (f) Corollary FUEL-ROOT-STAIR (§6, l. 118-127; statement l. 121-122) | l. 23 «SIGNED (conditional on [FUEL-COUNT] landing)»; §6 l. 78-81 | l. 27 «**SIGNED**»; §3.5 l. 127-130 |
Both lists, verbatim: REFEREE FINDINGS l. 139 «Every item to sign is SIGNED, with no gap.»; REFEREE-2 l. 189-190 «DESC-ROOT, ROOT-STAIR,
ORIGIN-NEW, RELAY, NEW-FUEL, ROOT-SPLIT and FUEL-ROOT-STAIR are all SIGNED (Opus 5.5, D15). There is no gap in the packet.»; fixes F0 l.
8-9 the same items for REFEREE. The packet's own to-sign list (l. 8-9) names the six; RELAY is signed by both as part of §4.
Clause checks (L-2 against the packet): (a) the walk, «x_j ∉ C», the descent at k with previous change k′ and «of type R, T or S» are l.
54-56; the counting is l. 76; «If (v, k) is itself of type R, T or S, then j = 0.» (l. 57) is not stated. (b) l. 79's bound; the converse
as «R_F + S_F ≤ n·WCT_F, TS_F ≤ n·|F|» (the packet's middle term «≤ DESC_F» and the family reading, l. 80, not stated). (c) l. 89's first
sentence, with the root change carrying «k → k + 1 a transition of F» (ROOT114-L1; REFEREE-2 signs ORIGIN-NEW «for k → k + 1 a transition
of F»); its «In particular» (l. 89-90) not stated. (c′) RELAY is not stated by name; its content is ROOT-SPLIT's «or a relay entering by an
edge of H_(k−1)». (d) l. 104-106; «Even» comes from the binder (REFEREE-2 L1 l. 22 «y is Even by the binder.»). (e) l. 114-115; l. 116's
split «R_F = R^fuel_F + R^old_F» is L-2's definition «R^fuel_F := R_F − R^old_F». (f) l. 121-122 with l. 127 («the sums over Even edges
(y, z) with N_F(y, z) ≥ 1»); HC_F as fixes entry 1 l. 41-45 (= packet l. 119-120 with the key written out). Nothing in L-2 is wider than
signed; the narrowing of ORIGIN-NEW / ROOT-SPLIT to transitions of F is the reading both signed (REFEREE §C l. 165 «My §4 proof uses W-MON
«on F», so it signs the statement for k → k + 1 ∈ F only, the same reading as REFEREE-2's.»).
Signed by both, NOT stated by L-2, so NOT landed: DESC-ROOT's «j = 0» clause; ROOT-STAIR's «≤ DESC_F» and family reading; ORIGIN-NEW's «In
particular»; RELAY by name. Not signed, so NOT landed: §7 DEADs and DATA, §8 READING (packet l. 10).
(5) OTHER LANES' TEXTS THE ENTRY DEPENDS ON (all signed by both referees of their packets, none landed at this draft):
- P-N5-STAIR ([COPY] both directions, [STAIR]; β, first-difference positions, descents, DESC_F): L-2 pins STAIR line L-2 (6903f1b3,
  44f56e96). Content check for F-1 (by script): COPY's two-way statement «if v ∉ C has the same successor z at k and at k + 1, then β(W(v))
  and β(W(z)) have the same flips at k, in the same directions, through a strictly increasing position map; C-vertices keep the value (c,
  ∅, 0) on F», Theorem STAIR's bounds, and the β / first-difference / DESCENT / DESC_F definitions occur verbatim in STAIR L-2 AND in STAIR
  L-3 (9db0b169), i.e. in R99-draft's title. The packet's [COPY] and [STAIR] (l. 39-43) restate them. REFEREE l. 18 «[COPY] / [STAIR] as
  signed»; REFEREE-2 §0 l. 12 «P-N5-STAIR (l-new 9a58765f, docs/new/P-N5-STAIR-box112.md) §1 and §6: COPY with the fixed map π_v; C
  constant.»
- P-N5-ODD ([FUEL-COUNT]; the fuel re-route; the key): L-2 pins «l-si 0afc0d70a, docs/si/P-N5-ODD-box57.md §6, sha1 03eec41d» (re-hashed
  here: 03eec41d3bfc63a6945d0f30d831a46f14e46b84, 146 lines; = C108 l. 12). §6 l. 114-115 «Corollary FUEL-COUNT. Let N be the number of fuel
  re-routes of (y, z) in F, and HC the number of transitions u of F at which Ξ(z) changes at a key strictly greater than the key of the
  last fuel re-route of (y, z) at a transition ≤ u. Then N ≤ n(n + 2)(HC + n).»; R98-draft's title (ODD L-3) states the same, in content, with «for
  every pair (y, z)» (ODD-L5), and the same fuel re-route and key. REFEREE l. 18 «[FUEL-COUNT] as signed with fixes entries 1-2»; REFEREE
  §5 l. 75 «The fuel re-route matches P-N5-ODD §6's definition word for word.»; REFEREE-2 §3.4 l. 122 «The conclusion together with the
  hypotheses is P-N5-ODD §6's fuel re-route definition, word for word.»
- P-N5-SRC §2 ([PLAY], Φ): used in ORIGIN-NEW's proof (packet l. 98 «So Φ(y; ·) (P-N5-SRC §2, [PLAY]) is order-preserving on them.»); the
  packet's §1 premise list does NOT list [PLAY] (discrepancy (11)(iii)); L-2 lists «P-N5-SRC §2 (proof of RESULTS R97 PLAY-CAUSE^S)». R97
  (a) is «Lemma PLAY-CAUSE^S (§2, l. 56-82)» (RESULTS l. 8082), the proof both R97 referees signed; «P-N5-SRC §2» occurs 0 times in
  RESULTS.
- L-RED R162 / R163: in the frozen packet's scope (l. 5) and in the frozen line / L-1 tails; dropped at L-2 (L43). Not used by any proof.
(6) PREMISE LABELS (stale-label test; RESULTS at 24280f52 = trunk f3c2df11). RESULTS labels in L-2 (by script): «R57» 1, «R15» 1, «R91»
1, «R93» 1, «R97» 1, «R89» 1; «P-N5-SRC §2», «P-N5-STAIR» (3), «P-N5-ODD» (3) are lane packet names. Every RESULTS label exists and carries
the named item:
- R57 (l. 2893): L-2's gloss «1E-N3: S1's procedure realises the pointwise optimum; for S4a at a transition k → k + 1, σ_(k+1) is the
  pointwise optimum of the one-player arena H_k» is verbatim in R97's title (l. 8032, by script), and L-2 defines H_k in the gloss («H_k :=
  S4a's arena at k (Even y keeps {σ_k(y)} ∪ Iσ_k(y), Odd follows τ_k)»; R97: «H_k := S4a's arena at k (Even v keeps {σ_k(v)} ∪ Iσ_k(v),
  Odd follows τ)»). The S4a half is Lead reading L42's reading of R57 («R57's standing SPEC premise (1E-N3) covers S1's procedure and S4a
  (σ_(k+1) is the pointwise optimum of H_k).»); ORIGIN-NEW uses it directly at the S4a step k − 1 → k (REFEREE §4 l. 52 «[1E-N3] at the S4a
  step k − 1 → k makes σ_k pointwise optimal in G′»), which L42 covers.
- R15 (l. 624): (a) Lemma A l. 631-632 («for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}»), (b)
  Lemma B l. 633-634 («every (v, w) ∈ I is a length-only switch at a cycle node: Λσ(v) = v»), (d) l. 640. REFEREE l. 18 «R15 (a), (b),
  (d) at l. 624»; REFEREE-2 §0 l. 14-15. (a) and (b) are ORIGIN-NEW's A / B step; (d) gives Ξ_(k+1) ⊵ Ξ_k (NEW-FUEL's Claim).
- R91 (l. 6384): «(Lemmas XW, W-MON, FB-W, OPT-OFF, W-SUCC) Ξ_t ⊴ W_t pointwise, W does not fall at an S4a step (read with τ_t)» (by
  script); (b) Lemma W-MON l. 6450-6451. L-2 cites «R91 (Lemma W-MON)». OPT-OFF ((d), l. 6455-6457) is REFEREE-2's P-2 for ORIGIN-NEW's
  first step (§3.3 l. 100-101), recorded in fixes entry 2 l. 87-88 and not in the line («The line's premise list cites R15 (a), (b) and
  [1E-N3], which give OPT-OFF's content.»). RESULTS also has R90 (a)'s different Lemma OPT-OFF (R91 (d) says so); the line cites neither.
- R93 (l. 6972; (a) l. 7031-7036): Fact LEX, «x ◁ y iff CS(x) < CS(y) lexicographically»; the packet uses it for linearity of ⊴ (l. 38
  «in particular it is LINEAR on values»).
- R89 (l. 5854): «a W-run := a maximal run of consecutive states of one τ-stretch none of whose transitions is an S4c fallback or changes
  λ_W»; «λ_W its cycle-node map» (by script). L-2 writes «W-run F = [p, q] := RESULTS R89's» without the gloss (R97 / R99-draft carry it;
  D-2). «[S1-val]» is R89's notation.
- R97 (l. 8032, LANDED 9777660f): «(a) Lemma PLAY-CAUSE^S (§2, l. 56-82)» (l. 8082); [PLAY] is that proof ((5)).
- Name check against landed text (RESULTS / GAPS at 24280f52 / a0b8f8dd, by script, word boundaries): «DESC-ROOT», «ROOT-STAIR»,
  «ORIGIN-NEW», «NEW-FUEL», «ROOT-SPLIT», «FUEL-ROOT-STAIR», «ROOT CHANGE», «ORIGIN», «TIE SWITCH», «HC_F», «R^old», «R^fuel», «N_F»,
  «TS_F», «R_F», «T_F», «S_F», «fuel re-route», «FUEL-COUNT», «COPY», «STAIR», «DESC_F», «COPIED», «R-descent», «root descent», «frz32»,
  «H_(k−1)» and «s_k» occur 0 times in both. «RELAY» occurs 11 times in RESULTS and twice in GAPS, as R71 / R72's «RELAY ρ event» (e.g.
  l. 3757) and E-RELAY (l. 3601), a different object; «KEY» 24 times in RESULTS, R38 (a)'s KEY (λ_Ξ and τ constant on a phase), a
  different object (D-5). «P-N5-ROOT» 3 times in RESULTS and once in GAPS, all R74's packet (F-4). AT LANDING, with R98 and R99 in:
  «N_F» (R99's BW-ACC count, a different object), «fuel re-route», «key», «HC», «FUEL-COUNT» (R98's, the same objects), «COPY»,
  «STAIR», «DESC_F», «DESCENT» (R99's, the same objects); re-run the grep for «### R100» (0) and «R100» (0).
(7) SYMBOL TEST of the title (my own strict test of every symbol of L-2, by hand; IN = bound in the line; else the carrier):
| symbol | where |
| --- | --- |
| N5, SPEC S1-S5, «Even», «Odd», S4a, SPEC S2 | SPEC (named) |
| R57 gloss: k, σ_(k+1), H_k, y, τ_k, Iσ_k(y) | k IN («for S4a at a transition k → k + 1»); H_k IN («H_k := S4a's arena at k (…)»); y the gloss's own letter; Iσ_k defined later in the line (D-6) |
| premises R15 (a), (b), (d); R91; R93; P-N5-SRC §2; P-N5-STAIR (pinned); P-N5-ODD (pinned) | cited; see (5), (6); F-1 |
| run, states (σ_k, τ_k), transition k → k + 1, «y switches at k» | IN |
| n, V | n IN («n := \|V\|»); V not glossed (D-3); = TARGET.md §1 l. 8 «n = \|V\|» |
| values, ⊴, ◁, ⊵, ▷ | «as in SPEC S1» |
| Ξ_k, Iσ_k | IN («Ξ_k := Ξ_{σ_k}»; «Iσ_k := Even's improving edges at k (SPEC S2: …)») |
| W-run F = [p, q], τ, λ_W, C, \|F\| | F by R89's label; λ_W only through R89 (D-2); C, \|F\| IN |
| W_k, [S1-val], s_k(v), T1_F, WCT_F | IN; [S1-val] R89's notation |
| β, first-difference positions, descents, DESC_F | by STAIR L-2's pin (F-1) |
| types R, T, S, COPIED; R_F, T_F, S_F; t | IN («a descent (x, k) of x with previous change of W(x) at k′ is of type R if …») |
| TIE SWITCH, TS_F | IN |
| ROOT CHANGE, ORIGIN, RELAY | IN («a ROOT CHANGE is a pair (y, k) with k → k + 1 a transition of F, …») |
| FUEL RE-ROUTE, N_F(y, z) | IN (as in P-N5-ODD §6, written out); N_F name beside R99's (D-5) |
| KEY, a → b, r, r′, key of a fuel re-route, HC_F(y, z), u | IN |
| R^old_F, R^fuel_F, R-descent | IN (R-descent = descent of type R) |
| global binder: run, F, v, y, z, k | IN («for every N5 run on every game and every W-run F = [p, q] of it, every vertex v, every Even y, every vertex z and every transition k → k + 1 of F») |
| DESC-ROOT: k′, j, x_i, x_j | IN |
| FUEL-ROOT-STAIR: Σ_(y,z) | IN («the sums over Even edges (y, z) with N_F(y, z) ≥ 1»); rebinds y, z (D-4) |
| scope tail: «root descent», frz32, G-N5-TIME, M3, step-4, TARGET.md | «root descent» NOT defined (F-3); frz32 unpinned (D-7); GAPS l. 11, TARGET.md |
Agreeing tests: REFEREE §8 l. 128-131 (token pass), §C l. 169-170 («Strict symbol test on the new tokens: KEY, a, b, r, r′, u, HC_F, the
pinned citations and v / y / z / k are bound.»); REFEREE-2 §5 l. 178-181, L1 l. 38-42 («No free symbol.»), L2 l. 12. Neither lists
«root descent» or λ_W.
DOUBTS for CHECKER (D-1 is F-3; no referee raised any as REQUIRED; no change proposed by me):
D-1 «root descent» undefined (F-3).
D-2 «λ_W» occurs once, «C := {v : λ_W(v) = v}», defined only by RESULTS R89's title; R97 / R99-draft gloss R89's W-run in the title.
D-3 «V» in «n := |V|» unglossed (R96, RESULTS l. 7748, has «n := |V|,» unglossed: a landed precedent; R97 / R99 gloss it).
D-4 Σ_(y,z) rebinds the binder's y and z (REFEREE-2 L1 l. 40 «a harmless shadowing»).
D-5 names: N_F(y, z) (fuel re-routes of a pair) beside R99's N_F (BW-ACC's transitions), once R99 lands; «KEY» beside R38 (a)'s KEY;
«RELAY» beside R71 / R72's RELAY events. Different arity or context; none inside a claim with the other meaning.
D-6 Iσ_k(y) (a section of an edge set) is used in the R57 gloss before Iσ_k is defined (C106 N-5 left «Even keeps σ_t ∪ Iσ_t» as R93's
wording).
D-7 the DEAD's instance is named «frz32» only; REFEREE addendum l. 206 «Precision (optional): name the pin as
«red/n5inj/instances/frz32 with its start», with its sha1.» (not applied: L-2 predates it). The files: red/n5inj/instances/frz32.pg
(sha1 b251897c9db09cb339a32ac37f8408b8f63fa3b2) and frz32.start (4adb74f1b754dda97af9f33b832ca09dccbfc7fa) at 7988e2f4 (Data).
(8) FIXES AND STATUS NOTES (fixes file at 7988e2f4, sha1 8e08a8c00be8e235a5210986da1949aa83f85c93, 122 lines; = l-new head 401d283a =
trunk; recorded under Fixes): F0 and entries 1-3, three commits, each +N/−0: c4279144 (16:32:58Z, new file, 46 lines, F0 + entry 1; the
file then sha1 ddc3a7d7…), be131555 (19:32:23Z, +42/−0, entry 2, with L-1; the file then sha1 5f144b41a4d37fac05fa39c9113a4a801b9e2dbe,
88 lines, which REFEREE re-hashed, §C l. 148) and 7988e2f4 (20:57:08Z, +34/−0, entry 3, with L-2). The fixes file's quotes were checked
for this draft by script (fxq100.py): entry 1's REFEREE block (l. 22-34) = R-N5-ROOT114.md l. 113-125; entry 2's REFEREE-2 block (l. 53-72)
= R2-N5-ROOT114.md l. 41-60; entry 3's ROOT-L4 block (l. 95-99) = l. 171-175, its ROOT-L5 blocks (l. 101-102, l. 104-107) = l. 176-177 and
l. 182-185; its C109 blocks (l. 109, l. 111-113) = C109.md l. 58 and l. 72-74; its L43 clause (l. 114) = DECISIONS.md l. 374. REFEREE §C l.
191-192 «Entry 1 quotes my ROOT-L1..L3 ✓.», «Entry 2 quotes REFEREE-2 verbatim ✓.»
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-2 states no CONJECTURE. A line-11 UPDATE is proposed at the end, to go AFTER R98's and
R99's UPDATEs (PENDING: R98-draft and R99-draft at 6d653c3f; at f3c2df11 the last UPDATE on l. 11 is R97's «UPDATE 2026-10-31 07:02Z:
RESULTS R97 (P-N5-SRC; CHECKER C107 449cb6fc) …», ending «G-N5-TIME stays open.» before the row's closing « |»; l. 11 holds 76 "|"), as a
pure insertion with one separating space. Built by script (scratch upd100.py = upd99L3.py's build rule, with one generalisation: the
claim labels are searched after the binder's colon «every transition k → k + 1 of F: », because «(Corollary FUEL-ROOT-STAIR)» occurs
twice in L-2, once inside the premise «and, for (Corollary FUEL-ROOT-STAIR) only, P-N5-ODD (…)»; that premise occurrence is NOT moved).
Construction (R94's-R99's): «LANDED: » + the title body with each clause label moved behind its clause; the scope tail « (2026-10-31) —
REDUCTIONS and EQUIVALENCES (X) (source)» → «: REDUCTIONS and EQUIVALENCES; X′ (source). G-N5-TIME stays open.», X′ = X minus «G-N5-TIME
stays OPEN» and «not M3, not a step-4 pass, not a TARGET.md claim»; the source parenthesis is KEPT. CONTROLS (same script, same run):
R97's landed UPDATE from SRC L-5 (l-red a5340f2d) byte for byte (True, 4,179 bytes); R99-draft's UPDATE from STAIR L-3 at 6d653c3f (True,
4,873 bytes); R98-draft's UPDATE from ODD L-3 at 6d653c3f (True, 4,263 bytes). DESC-ROOT's inner «; hence DESC_F ≤ …» stays before its
label (the script moves each label to the end of its whole clause, as for R99's COPY / RESET-ROOT). The UPDATE must hold no "|"; L-2
holds twelve, so these replacements were made, which are NOT title text: (q1) «n := |V|» → «n := the number of vertices of the game»
(= R98's (q1)); (q2) «|F| := q − p,» → «q − p is its number of transitions,» (R99's (q2) form); (q3) «TS_F ≤ n·|F|» → «TS_F ≤ n times the
number of transitions of F» (NEW: n·the number ... would misread); (q4) each of the other three «|F|» → «the number of transitions of F»
(R93-R99 wording). Checked by script: one line, 0 "|", one «<HH:MM>», one «<checker>», 4,667 bytes, 899 tokens. The stamp is «UPDATE
2026-10-31 <HH:MM>Z» (the landing date; F-5); <HH:MM> and <checker> are filled at landing. The head keeps «(P-N5-ROOT; …)» (F-4).
(10) DATA of record = the packet's §7 DATA (l. 138-142). Re-summed for this draft (python3 -I, scratch sum100.py over the stored outputs in
a `git archive` of 7988e2f4: experiments/new/box113/d5_sbcg.txt (719 rows) and d5_alt.txt (413), added by f18315ce; 2026-10-31 22:23:23Z by
date -u, rc 0): 1,132 rows, 0 parse errors; WT 14,028; WCT 13,949; DESC 14,755 = DR 7,606 + DS 932 + DT 1 + COPIED 6,216; TIESW 397; DMISS
0, ROOTMISS 0; ORIGCH 25,679, ONVIOL 0; NFSW 27,539, NFVIOL 0; RD_OLDEDGE 47, RD_NEW = RD_FUEL 7,559, RD_NEWNOTFUEL 0. All equal the packet
(l. 139-142: «DESC 14,755: R 7,606, S 932, T 1, COPIED 6,216; TS 397. DESC-ROOT misses 0.», «Origin root changes 25,679, ORIGIN-NEW
violations 0.», «New-edge switches with k − 1 ∈ F 27,539, NEW-FUEL violations 0.», «R^old 47.») and REFEREE-2's table (l. 140-148,
«R^fuel 7,559»). The two corpus games with invalid starts: packet l. 143-144 «On repaired starts (experiments/new/box113/inst/*_fixed.start)
their lines are identical.» Pins: (Data).
(11) Discrepancies, recorded for CHECKER, no verdict affected: (i) fixes entry 3 l. 119-120 places frz32 in «packet §1»; it is packet §7
(a), l. 133-134; its «Neither referee flagged it.» predates both L-2 verdicts, which accept it. (ii) Fixes entry 3 l. 100 labels its
ROOT-L5 quote «l. 176-192, first and last bullets»; the second quoted bullet is l. 182-185 («Fix, either:»), not the last bullet (l.
186-189, R162). (iii) The packet's §1 premise list (l. 31-45) omits [PLAY], which §4's proof uses (l. 98); L-2 lists P-N5-SRC §2; neither
referee's premise row names [PLAY] (REFEREE l. 18; REFEREE-2 §0 l. 11-16), both check the Φ step (REFEREE §4 l. 62-65; REFEREE-2 §3.3 l.
106-111). (iv) REFEREE-2 §3.3 l. 100-101 calls «a pointwise-optimal Even strategy ρ has Ω_ρ(c) ⊴ Ω_ρ(ρ(v)) for every edge (v, c) at every
Even v that is not its own Ω_ρ-cycle node» «R91 Lemma OPT-OFF verbatim»; R91's title has «(R17 (a) (F1)) with Ω_ρ its [S1-val]
valuation» after «ρ», dropped without an ellipsis. (v) REFEREE-2 L2 l. 11 «The Lead (21:25Z) agrees with my reading» in a file headed
«written 2026-10-31 21:24Z by date -u» and committed 21:24:48Z (3bb41a4c); LEAD-STATE's 21:24Z entry already records «frz32 universal
DEAD allowed». (vi) Word counts: REFEREE-2 L1 l. 3 «697 → 837 words», fixes entry 3 l. 122 «837 → 825 words»; this draft's whitespace
tokens 736 → 881 → 869 ((2)); the same changes. (vii) The packet's [R15] (a) reads «for a non-empty set I of improvements of σ» (l. 34);
R15 (a) says «non-empty unambiguous»; the use is a single edge (REFEREE §4 l. 59 «a non-empty unambiguous improvement set»). (viii) The
packet §7 «Pins (check.sh «box 113 DESCSTAR»)» lists fbg_K4_m6_m48 (l. 146-147), but no check.sh block runs it; its figures rest on the
stored box113/out_fbg_K4_m6_m48.txt (DESC 640, RD 210, CPD 430; 9e4aefa6) and REFEREE-2's re-run (§4 l. 159). (ix) REFEREE's run set
(719 games, MAXN 100, 656 analysed, l. 102) differs from the packet's and REFEREE-2's 1,132; VIOLATIONS 0 on both. (x) REFEREE's premise
row (l. 18) and FINDINGS l. 141 make DESC-ROOT and ROOT-STAIR conditional on P-N5-STAIR, not only FUEL-ROOT-STAIR (body, Premises).
(12) Excluded: L-NEW box 113's lane items not in this packet (docs/new/N5-DESCSTAR-box113.md: COPY⁺, SW-WIT; its DEAD (c) «U = the switch
sites …», packet §7 (c), which REFEREE-2 did not re-run as a DEAD, §4 l. 162); L-RED R162 / R163 (lane; dropped from the line, L43);
L-NEW boxes 115-118; REFEREE-2's BND_* probes and bnd.py (review tools; their ROOT114-L1 counts are in the body); REFEREE's and
REFEREE-2's tools (docs/referee/scratch/root114_probe.py, root114_logs/; docs/referee-2/R2-N5-ROOT114/root_check.py, oink_pins.py,
logs/). Not part of this entry.
(13) Commits: lane (claude/l-new): 9e4aefa6 (13:40:21Z; box 113 note, desc3 / desc4, instances incl. w_re3_1, cp_K4, fbg) → f18315ce
(14:03:02Z; box 113b, desc5.py, d5_sbcg.txt / d5_alt.txt, check.sh +3/−3) → ed2fdaf2 (14:53:59Z; freeze: packet +158, frozen line +1) →
c4279144 (16:32:58Z; fixes F0 + entry 1, +46) → be131555 (19:32:23Z; entry 2 +42, L-1 +1) → 7988e2f4
(20:57:08Z; entry 3 +34, L-2 +1). REFEREE on claude/referee: d8a2f428 (15:41:34Z; report, new file 143
lines; root114_logs/) → 74025e44 (20:01:05Z; §C, +51/−0) → af9cd763 (21:24:55Z; L-2 addendum, +13/−0). REFEREE-2 on claude/referee-2:
d1c493fb (18:45:09Z; report, new file 198 lines; R2-N5-ROOT114/ tools and logs) → 83c1838f (20:00:13Z; R2-N5-ROOT114-L1.md, new file 56
lines) → faa8dac9 (20:28:55Z; its Addendum 1, +8/−0; the same commit adds R2-N5-STAIR-L3.md) → 3bb41a4c (21:24:48Z; R2-N5-ROOT114-L2.md,
new file 19 lines). Trunk merges that brought each in (a merge «… into claude/vibrant-johnson-nxvvxo» containing it whose first parent
does not; the C107 test, scratch firsttrunk.py): 9e4aefa6, f18315ce → db4a5d6a (14:21:51Z); ed2fdaf2 → ddf7dd57 (15:16:25Z); d8a2f428 →
7c455f40 (16:13:51Z); c4279144 → 1b159f51 (17:31:52Z); d1c493fb → c93d8ddb (19:31:36Z); be131555 → ce1a6e2f (20:00:30Z); 74025e44 →
83b5acc9 (20:27:53Z); 83c1838f, faa8dac9, 7988e2f4 → a20cf406 (21:23:35Z); af9cd763, 3bb41a4c → f1b1044e (22:19:06Z, local trunk only at
this draft).
(14) Placement: after R99 (pending; at 24280f52 R97 is l. 8032-8294, l. 8295 blank, "## Dead ends (kept;" l. 8296; see (0)). No Dead-ends
row: no signed item kills a conjecture; the DEAD «every root descent is a fuel re-route» is L-NEW's lane DEAD (packet §7 (a), not to
sign), named in the title as R90 / R95 name their lane DEADs (neither has a Dead-ends row), and reproduced by both referees.
### R100 [refereed-only] N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum; for S4a at a transition k → k + 1, σ_(k+1) is the pointwise optimum of the one-player arena H_k, H_k := S4a's arena at k (Even y keeps {σ_k(y)} ∪ Iσ_k(y), Odd follows τ_k)); premises RESULTS R15 (a), (b), (d), R91 (Lemma W-MON), R93 (Fact LEX), P-N5-SRC §2 (proof of RESULTS R97 PLAY-CAUSE^S), P-N5-STAIR (Lemma COPY in both directions and Theorem STAIR, as in its line L-2: l-new 6903f1b3, docs/new/P-N5-STAIR-line-L2.txt, sha1 44f56e96d41d45653c4b7bc2f140c587e8e407e6) and, for (Corollary FUEL-ROOT-STAIR) only, P-N5-ODD (Corollary FUEL-COUNT: l-si 0afc0d70a, docs/si/P-N5-ODD-box57.md §6, sha1 03eec41d, with its fixes entries 1-2)), with: a run is the sequence of states (σ_k, τ_k), a transition is written k → k + 1, and an Even vertex y switches at k if σ_(k+1)(y) ≠ σ_k(y); n := |V|; values, ⊴, ◁, ⊵, ▷ as in SPEC S1; Ξ_k := Ξ_{σ_k} and Iσ_k := Even's improving edges at k (SPEC S2: {(y, z) : z ≠ σ_k(y), Ξ_k(z) ▷ Ξ_k(σ_k(y))}); W-run F = [p, q] := RESULTS R89's, with τ and C := {v : λ_W(v) = v} fixed on F, |F| := q − p, W_k the [S1-val] valuation of the (σ_k, τ)-plays, s_k(v) := σ_k(v) for Even v and τ(v) for Odd v, T1_F := the transitions of F with W_(k+1) = W_k and WCT_F := |F| − T1_F; β, first-difference positions, descents and DESC_F as in P-N5-STAIR's line L-2; a descent (x, k) of x with previous change of W(x) at k′ is of type R if x switches at k, of type T if not and x switches at some t with k′ < t < k, of type S if x switches at k′ and at no transition of (k′, k], and COPIED otherwise; R_F, T_F, S_F := the descents of F of each type; a TIE SWITCH is a pair (y, t) with y switching at t and W(y) unchanged at t, TS_F their number on F; a ROOT CHANGE is a pair (y, k) with k → k + 1 a transition of F, y switching at k and W(y) changing at k, an ORIGIN if W(σ_(k+1)(y)) does not change at k and a RELAY otherwise; a FUEL RE-ROUTE of (y, z) at k is as in P-N5-ODD §6 (y switches to z at k, k − 1 ∈ F, (y, z) ∉ H_(k−1), Ξ_(k−1)(z) ≠ Ξ_k(z)), N_F(y, z) their number on F; the KEY of a change a → b of Ξ(z) is (2, 0) if the cycle node changes, else (1, r) with r the top rank of the difference of the path sets, else (0, 0), ordered (0, 0) < (1, r) < (1, r′) < (2, 0) for r < r′, and the key of a fuel re-route of (y, z) at k is the key of the change Ξ_(k−1)(z) → Ξ_k(z); HC_F(y, z) := the number of transitions u of F at which Ξ(z) changes with a key strictly greater than the key of the last fuel re-route of (y, z) at a transition ≤ u; R^old_F := the R-descents (y, k) with (y, σ_(k+1)(y)) ∈ H_(k−1), and R^fuel_F := R_F − R^old_F: for every N5 run on every game and every W-run F = [p, q] of it, every vertex v, every Even y, every vertex z and every transition k → k + 1 of F: (Lemma DESC-ROOT) if v has a descent at k with previous change of W(v) at k′, and j is the least index with x_j ∈ C or x_j switching at a transition of [k′, k] along x_0 := v, x_(i+1) := s_(k+1)(x_i), then x_j ∉ C and x_j has a descent at k with previous change at k′, of type R, T or S; hence DESC_F ≤ n·(R_F + T_F + S_F) and T_F ≤ TS_F; (Theorem ROOT-STAIR, an EQUIVALENCE) |F| ≤ T1_F + n(3n + 1) + (3n + 1)·n·(R_F + S_F + TS_F), and R_F + S_F ≤ n·WCT_F, TS_F ≤ n·|F|; (Lemma ORIGIN-NEW) if (y, k) is an origin root change and k − 1 ∈ F, then (y, σ_(k+1)(y)) ∉ H_(k−1); (Lemma NEW-FUEL) if y switches at k to z, k − 1 ∈ F and (y, z) ∉ H_(k−1), then Ξ_(k−1)(z) ≠ Ξ_k(z), so (y, z) is a fuel re-route at k; (Corollary ROOT-SPLIT) if (y, k) is a root change and k − 1 ∈ F, then (y, k) is a fuel re-route or a relay entering by an edge of H_(k−1), and every R-descent has k − 1 ∈ F; (Corollary FUEL-ROOT-STAIR) R^fuel_F ≤ Σ_(y,z) N_F(y, z) ≤ Σ_(y,z) n(n + 2)(HC_F(y, z) + n), so |F| ≤ T1_F + n(3n + 1) + (3n + 1)·n·(n(n + 2)·Σ_(y,z) (HC_F(y, z) + n) + R^old_F + S_F + TS_F), the sums over Even edges (y, z) with N_F(y, z) ≥ 1 (2026-10-31) — REDUCTIONS and EQUIVALENCES (no count is bounded here; «every root descent is a fuel re-route» DEAD (frz32: old-edge relays); G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim) (P-N5-ROOT, docs/new/P-N5-ROOT-box114.md; L-NEW successor 42; fixes docs/new/P-N5-ROOT-fixes-box114.md entries 1-3), CHECKER PASS (docs/checker/C110.md, checker PENDING)
- Object (L-NEW successor 42, Opus 5.5, D14 / D18; frozen, unchanged during review): packet P-N5-ROOT (box 114; not RESULTS R74's
  P-N5-ROOT, L-SI box 20), docs/new/P-N5-ROOT-box114.md, sha1 f06f493ebd31e886517959abb13f7724f2e2f819, 158 lines (l-new freeze
  ed2fdaf2, 2026-10-31T14:53:59Z, the file's only commit; identical at l-new head 401d283a and at trunk; first on trunk by merge
  ddf7dd57, 15:16:25Z). Both referees measured the sha1 at ed2fdaf2 (REFEREE l. 3-5 «Both equal the Lead's figures.»; REFEREE-2 l. 8
  «Re-hashed: match»). Scope (l. 3-5): «Scope: a REDUCTION / EQUIVALENCE inside W-runs.», «No count is bounded here. G-N5-TIME stays OPEN.
  This is not M3, not a step-4 pass and not a TARGET.md claim.», «DESC-LIN is DEAD (L-RED R162). DESC*-LIN is DEAD in the weak form (L-RED
  R163, as relayed by the Lead 14:47Z).» (the last sentence is lane history; L-2 drops both, Lead reading L43; Honest limits (iii)). To
  sign (l. 8-9): «To sign: §2 Lemma DESC-ROOT; §3 Theorem ROOT-STAIR; §4 Lemma ORIGIN-NEW; §5 Lemma NEW-FUEL and Corollary ROOT-SPLIT; §6
  Corollary FUEL-ROOT-STAIR.» «Not to sign: §7 (DEAD ends, DATA), §8 (READING).» (l. 10). Source note (l. 6-7): L-NEW's box note
  docs/new/N5-DESCSTAR-box113.md «(history only)»; «This packet restates everything it uses; the note is not needed to check it.»
  Sections: §1 setting, premises (l. 13-45), §2 DESC-ROOT (l. 47-76), §3 ROOT-STAIR (l. 78-82), §4 ORIGIN-NEW and RELAY (l. 84-101), §5
  NEW-FUEL and ROOT-SPLIT (l. 103-116), §6 FUEL-ROOT-STAIR (l. 118-127), §7 DEAD ends and DATA (l. 129-147, not to sign), §8 READING (l.
  149-153, not to sign).
  The RESULTS line, history: (1) the frozen line docs/new/P-N5-ROOT-line.txt (sha1 954af7be…, committed with the packet), the line both
  referees reviewed: REFEREE REQUIRED ROOT-L1 to ROOT-L3 (§8 l. 111-134: v, k, k′, y, z unbound; STAIR and ODD cited without commit or
  sha1; «key» undefined and «at a transition ≤ u» dropped); REFEREE-2 REQUIRED ROOT114-L1 and ROOT114-L2 (l. 34-35, l. 183). At the frozen
  line, ORIGIN-NEW and ROOT-SPLIT read k free over states with k − 1 ∈ F, and as worded they were FALSE at k = q (ROOT114-L1, below);
  the tail carried «DESC-LIN DEAD (L-RED R162)». (2) L-1 a41df25b (docs/new/P-N5-ROOT-line-L1.txt, be131555; fixes F0 + entries 1-2), a
  token edit: REFEREE §C (74025e44) l. 161 «ROOT-L1 ✓, ROOT-L2 ✓, ROOT-L3 ✓.», l. 193-194 «Verdict on L-1: does NOT yet match. It needs
  ROOT-L4 (define and pin DESC-LIN / DESC*-LIN) and ROOT-L5 (R163 as DATA, not DEAD). Everything else MATCHES (Opus 5.5, D15).»; REFEREE-2
  R2-N5-ROOT114-L1.md (83c1838f) l. 51 «**MATCHES** (Opus 5.5, D15). All my ROOT line items are closed.», and its Addendum 1 (faa8dac9)
  after L43, l. 61 «So I agree with REFEREE's ROOT-L4 / L5 (74025e44): drop both, or restate them as DATA with numbers.» At the L-1 object
  the scope tail read «(no count is bounded here; DESC-LIN DEAD (L-RED R162); DESC*-LIN DEAD in the weak form (L-RED R163); «every root
  descent is a fuel re-route» DEAD (frz32: old-edge relays); G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim)». (3)
  L-2 c9c6b3801ed9cc3cb5017f240d8e0d0f2610efba (docs/new/P-N5-ROOT-line-L2.txt, l-new 7988e2f4, 2026-10-31T20:57:08Z, the file's only
  commit; identical at l-new head 401d283a and at trunk; first on trunk by merge a20cf406, 21:23:35Z; fixes entry 3) = L-1 with exactly
  these changes (word diff by script; fixes entry 3 l. 116-122): «DESC-LIN DEAD (L-RED R162); DESC*-LIN DEAD in the weak form (L-RED R163);»
  dropped (ROOT-L4, ROOT-L5; CHECKER C109 E-3's move (i), applied to both; Lead reading L43, docs/DECISIONS.md l. 369-374: «A lane DEAD of an
  ASYMPTOTIC statement (one with an unspecified constant, e.g. «DESC_F ≤ c·n») does not enter a RESULTS line as «DEAD»: it enters as DATA
  with its numbers and source commit, or not at all.»); «entries 1-2)» → «1-3)». REFEREE 21 L-2: §C addendum (af9cd763) l. 197-198 «Nothing
  else changed. The sha1 is re-hashed and matches.», l. 207 «Verdict on L-2: MATCHES (Opus 5.5, D15). No REQUIRED change remains on the
  P-N5-ROOT line.» REFEREE-2 25 L-2: R2-N5-ROOT114-L2.md (3bb41a4c) l. 7 «Nothing else. Byte test True», l. 14 «Verdict: **MATCHES** (Opus
  5.5, D15). All my ROOT line items are closed.» L-2 supersedes the earlier lines; the title is L-2 verbatim with its own date (to check
  (1)). Neither referee found a FALSE claim statement in the packet; every line item binds a symbol (v, y, z, k; k to transitions of F),
  pins a citation, defines a term (KEY, HC_F), or words the scope tail (the R162 / R163 DEADs dropped at L-2 per L43; the frz32 DEAD kept).
  Setting (packet §1, l. 13-45): N5 = SPEC S1-S5; a run is the sequence of states (σ_k, τ_k), a transition k → k + 1; values (c, P, ℓ)
  and ⊴ ◁ ⊵ ▷ are SPEC S1's; Ξ_k := Ξ_{σ_k}; Iσ_k (SPEC S2); «H_k := S4a's arena at k: Even y keeps {σ_k(y)} ∪ Iσ_k(y), and Odd follows
  τ_k.» (l. 18); «W-run F = [p, q] := RESULTS R89's» (l. 19), with «On F, τ and C := {v : λ_W(v) = v} are fixed, and every transition is an
  S4a step with τ fixed.» (l. 20); W_k, s_k, switches, |F|, T1_F, WCT_F (l. 21-23); β, first-difference positions, DESCENT, DESC_F «as in
  P-N5-STAIR» (l. 24-30). Premises (l. 31-45): [1E-N3] (R57); [R15] (a), (b), (d); [W-MON] (R91); [LEX] (R93 (a)); [COPY] «P-N5-STAIR Lemma
  COPY in BOTH directions, as signed by both referees with fixes entry 1 (G-ST-1 / P-1)» (l. 39); [STAIR] (l. 43); [FUEL-COUNT] «It is used
  ONLY in §6.» (l. 45). REFEREE's premise row: «CHECKED: R15 (a), (b), (d) at l. 624 (Lemma B's text is «every (v, w) ∈ I is a length-only
  switch at a cycle node: Λσ(v) = v»); R57 1E-N3; R91 W-MON; R93 (a) LEX; [COPY] / [STAIR] as signed; [FUEL-COUNT] as signed with fixes
  entries 1-2» (l. 18); REFEREE-2 §0 l. 11-16 «Premises opened, at the commits named». L-2's notation is the packet's, with the types
  (§2 l. 48-52), tie switches (l. 75-76), ROOT CHANGE / ORIGIN / RELAY (§4 l. 85-88), the fuel re-route (§5 l. 105-106), N_F and HC_F (§6
  l. 119-120), and R^old_F (§5 l. 116).
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 21 (report d8a2f428, §C 74025e44, L-2 addendum af9cd763); REFEREE-2
  successor 25 (report d1c493fb, R2-N5-ROOT114-L1.md 83c1838f with Addendum 1 faa8dac9, R2-N5-ROOT114-L2.md 3bb41a4c)). Items (a)-(f),
  and RELAY (c′), are SIGNED in both verdict tables (REFEREE "## Verdicts" l. 15-25 of R-N5-ROOT114.md; REFEREE-2 "## 1. Claims table" l.
  18-27 of R2-N5-ROOT114.md); the table is to-check (4). All hold inside every W-run of every N5 run on every game, for transitions k → k +
  1 of F. Premises LANDED (as L-2 names them): SPEC S1-S5; RESULTS R15 (a), (b), (d); R91 (Lemma W-MON); R93 (Fact LEX); R89's W-run;
  standing premise: RESULTS R57's SPEC premise in its 1E-N3 form, used directly by ORIGIN-NEW at the S4a step k − 1 → k (Lead reading
  L42 covers S4a); [PLAY] from P-N5-SRC §2, the signed proof of RESULTS R97 PLAY-CAUSE^S. Premises SIGNED BUT NOT LANDED at this draft,
  pinned in L-2 by commit and sha1: P-N5-STAIR's Lemma COPY (both directions) and Theorem STAIR, and its β / descent definitions (landing as
  R99); P-N5-ODD's Corollary FUEL-COUNT, the fuel re-route and the key (landing as R98); R100 lands after both (to check (0), F-1). The
  code's match to SPEC is DATA (R15 G-N5T-1). No item bounds a count.
  (a) Lemma DESC-ROOT, with its counting (§2, l. 47-76): types (l. 48-52) «R (ROOT) if x switched at k;», «T (TIE) if not R, and x switched
      at some t with k′ < t < k;», «S (STALE) if x switched at k′ and at no transition of (k′, k];», «COPIED otherwise (x switched at no
      transition of [k′, k]).»; statement (l. 53-57): «Walk x_0 := v, x_(i+1) := s_(k+1)(x_i), and let j be the least index such that x_j ∈
      C or x_j switched at some transition of [k′, k].», «Then x_j ∉ C, and x_j has a descent at k whose previous change is at k′.», «The
      descent (x_j, k) is of type R, T or S.»; counting (l. 75-76): «DESC_F ≤ n·(R_F + T_F + S_F) and T_F ≤ TS_F.»; proof: the walk follows
      v's (σ_(k+1), τ)-play; for i < j, x_i has the successor x_(i+1) at every state k′, …, k + 1; [COPY] in both directions along the
      walk gives one strictly increasing composite map π with q(v) = π(q(x_j)); at most n vertices v map to one (x, k), and a T-descent has
      a tie switch in its window. Cells: REFEREE «SIGNED» (l. 19; §2 l. 27-40, l. 31 «[COPY] in both directions (P-N5-STAIR G-ST-1 / P-1)
      makes W(v) change exactly when W(x_j) does,»); REFEREE-2 «**SIGNED**» (l. 21; §3.1 l. 72-84, l. 77 «So the composite π is the same at
      k′ and at k. That is the point the strict inequality q_k(x_j) > q_(k′)(x_j) needs, and it holds.»).
  (b) Theorem ROOT-STAIR, an EQUIVALENCE (§3, l. 78-82): «Statement. |F| ≤ T1_F + n(3n + 1) + (3n + 1)·n·(R_F + S_F + TS_F). Conversely R_F
      + S_F ≤ DESC_F ≤ n·WCT_F, and TS_F ≤ n·|F|.» (l. 79); «Hence, over any family of runs, |F| is polynomially bounded iff T1_F + R_F +
      S_F + TS_F is.» (l. 80, not stated by L-2); proof: §2 and [STAIR]; at most n vertices switch per transition. Cells: REFEREE «SIGNED»
      (l. 20; §3 l. 42-45 «The equivalence over families is ✓.»); REFEREE-2 «**SIGNED**» (l. 22; §3.2 l. 86-89).
  (c) Lemma ORIGIN-NEW (§4, l. 84-100): «A ROOT CHANGE is a pair (y, k) with y switched at k and W(y) changing at k.» (l. 86), «With z :=
      σ_(k+1)(y), the root change is an ORIGIN if W(z) does not change at k.» (l. 87); «Statement. Let (y, k) be an origin root change with
      k − 1 ∈ F. Then (y, z) ∉ H_(k−1).» (l. 89), in L-2 with «k → k + 1 a transition of F» in the root change (ROOT114-L1, below); proof:
      G′ := the one-player game on H_(k−1) with Odd fixed to τ; σ_k is its pointwise optimum [1E-N3]; y ∉ C, so y is not its own cycle
      node in G′; an improvement (y, z) of σ_k in G′ would give Ω′ ⊵ W_k (R15 (a)) and Ω′ ≠ W_k (R15 (b)), against optimality, so W_k(z) ⊴
      W_k(z0) ([LEX]); Φ(y; ·) is order-preserving on the two values ([PLAY]); with the origin and [W-MON], W(y) does not change. Cells:
      REFEREE «SIGNED. The R15 A/B step was checked with special care (§4)» (l. 21; §4 l. 47-66; l. 56-57 «So λ_W(y) ≠ y, y is not an own
      cycle node in G′, and R15 (b)'s exception does not apply. L-NEW's claim «a root change is never at C» is exactly this, and it is
      correct.»); REFEREE-2 «**SIGNED**, for k → k + 1 a transition of F (the packet's §1 setting)» (l. 23; §3.3 l. 91-114, «checked with
      special care, as the Lead asked»; l. 100-101: «This is RESULTS R91 Lemma OPT-OFF verbatim» (P-2)).
  (c′) Corollary RELAY (§4, l. 101): «A root change (y, k) with k − 1 ∈ F that enters by an edge of H_(k−1) is a relay: W(σ_(k+1)(y))
      changes at k.» Not stated by name in L-2 (its content is in ROOT-SPLIT). Cells: REFEREE l. 21 (with ORIGIN-NEW), §4 l. 67 «RELAY is
      the contrapositive ✓.»; REFEREE-2 «**SIGNED** (same reading)» (l. 24).
  (d) Lemma NEW-FUEL (§5, l. 104-113): «NEW-FUEL statement. Let Even y switch at k to z := σ_(k+1)(y), with k − 1 ∈ F and (y, z) ∉
      H_(k−1). Then Ξ_(k−1)(z) ≠ Ξ_k(z).» (l. 104); proof: (y, z) ∈ Iσ_k (S4a picks in H_k(y)); Ξ_(k−1)(z) ⊴ Ξ_(k−1)(z1) ([LEX]); Claim
      Ξ_k(z0) ⊵ Ξ_(k−1)(z1) by R15 (d); equality Ξ_k(z) = Ξ_(k−1)(z) would contradict Ξ_k(z) ▷ Ξ_k(z0). Cells: REFEREE «SIGNED» (l. 22; §5
      l. 70-75); REFEREE-2 «**SIGNED**» (l. 25; §3.4 l. 116-122; P-1 l. 62-68: it holds even with k unbound).
  (e) Corollary ROOT-SPLIT (§5, l. 114-116): «Corollary ROOT-SPLIT. Every root change (y, k) with k − 1 ∈ F is a fuel re-route (new edge,
      §5) or a relay through an old edge (§4).» (l. 114), «Every R-descent has k − 1 ∈ F, since its previous change is at some k′ < k with
      k′ ≥ p.» (l. 115); in L-2 for a root change at a transition of F. Cells: REFEREE «SIGNED» (l. 22; §5 l. 76 «ROOT-SPLIT ✓: new edge ⇒
      NEW-FUEL; old edge ⇒ ORIGIN-NEW's contrapositive (relay).»); REFEREE-2 «**SIGNED**, for k a transition of F» (l. 26; §3.5 l. 124-126).
  (f) Corollary FUEL-ROOT-STAIR (§6, l. 118-127): «Statement. R^fuel_F ≤ Σ_(y,z) N_F(y, z) ≤ Σ_(y,z) n(n + 2)(HC_F(y, z) + n).» with the
      bound on |F| (l. 121-122) and «The sum is over the Even edges (y, z) with N_F(y, z) ≥ 1.» (l. 127); proof: distinct fuel R-descents
      are distinct fuel re-routes; [FUEL-COUNT] gives N_F(y, z) ≤ n(n + 2)(HC_F(y, z) + n); insert into §3. HC_F in L-2 is fixes entry 1's
      ROOT-L3 wording (l. 41-45), «This is P-N5-ODD §6's definition, verbatim in content.» Cells: REFEREE «SIGNED (conditional on
      [FUEL-COUNT] landing)» (l. 23; §6 l. 78-81); REFEREE-2 «**SIGNED**» (l. 27, note «Conditional on [FUEL-COUNT] and on [COPY] / [STAIR],
      which both referees signed and which have not landed yet»; §3.5 l. 127-130).
  The RESULTS line (L-2) claims less than the reports in places (no «j = 0» clause, no family reading, no «In particular» of ORIGIN-NEW,
  RELAY not by name) and nowhere more: every claim clause L-2 states is one of (a)-(f); its scope tail states one lane DEAD and no claim
  (to check (4), (7)).
- Premises from unlanded packets (status; REFEREE l. 10-12 «Premise status: [COPY], [STAIR] (P-N5-STAIR) and [FUEL-COUNT] (P-N5-ODD) are
  signed by both referees, but neither line has landed.», «So this packet's results are conditional on those two landings.»; FINDINGS l.
  141 «FUEL-ROOT-STAIR is conditional on P-N5-ODD landing; DESC-ROOT and ROOT-STAIR are conditional on P-N5-STAIR landing.»). ORIGIN-NEW
  and ROOT-SPLIT also use [COPY] (y ∉ C by its second clause; the path-set step «as in [COPY]'s proof (G-ST-1)», packet l. 97); NEW-FUEL
  uses none of the three. L-2 pins the premises by commit and sha1 (STAIR line L-2, 6903f1b3 / 44f56e96; ODD §6, 0afc0d70a / 03eec41d
  with fixes entries 1-2), per ROOT-L2's «until then, by commit and sha1»; the statements it imports are verbatim in R99-draft's title (STAIR
  L-3) and, for FUEL-COUNT, in R98-draft's title (ODD L-3) up to the binder «for every pair (y, z)» (to check (5)). R100 lands after R98 and
  R99, so at landing every premise is landed; L-2 still cites the lane commits, not the R-numbers (F-1).
- ROOT114-L1 (the boundary k = q; a line item at the frozen line, not a packet gap): REFEREE-2 l. 45-46 «Here F = [p, q] is a set of
  states. With k = q, the state k − 1 = q − 1 lies in F, but the transition q → q + 1 is not a transition of F. It is the cut: an S4c
  fallback, a λ_W change, or a τ change.»; counterexample (l. 48-53): experiments/new/box113/inst/w_re3_1.pg (sha1 c59735b4…) with its
  start (3614ad94…), «The W-run is F = [2, 6]. Transition 6 → 7 is an S4c fallback (τ unchanged, λ_W unchanged).», «k = 6, y = 12, z = 29»,
  «k − 1 = 5 ∈ F, and (12, 29) ∈ H_5.», «So ORIGIN-NEW as worded fails. ROOT-SPLIT as worded fails too: the change is not a fuel re-route
  (the edge is old) and not a relay.»; size (l. 55-56) «there are 2,977 such boundary origins with an old edge on the corpus (logs/corpus_totals.txt:
  BND_ONEW_FAILS_fb 2,394, BND_ONEW_FAILS_lamW 583) and 42 on the pins.»; «Fix (wording only; the packet's proofs are unchanged)» (l. 57).
  REFEREE §C l. 162 «REFEREE-2's boundary point (entry 2, ROOT114-L1; quoted counterexample w_re3_1, k = q = 6, an S4c cut) is correct.»,
  l. 165-166 «My root114_probe loops only over transitions of F, so it never tested the cut.» Repair: fixes entry 2 l. 75-81 (the binder
  quantifies «every transition k → k + 1 of F»; a ROOT CHANGE carries «with k → k + 1 a transition of F»; «The packet's proofs are
  unchanged.»). Closed: REFEREE §C l. 168 «L-1's «k → k + 1 a transition of F» inside ROOT CHANGE, plus the binder, settles it ✓.»;
  REFEREE-2 L1 l. 29-33 («**ROOT114-L1 is closed.**», «ORIGIN-NEW and ROOT-SPLIT now say exactly what I signed (k → k + 1 in F, k − 1 ∈
  F).»). The frozen packet's §4 is to be read «with «k → k + 1 a transition of F», as REFEREE-2 asks» (fixes entry 2 l. 81). Joint gap
  map: EMPTY (REFEREE FINDINGS l. 139 «with no gap»; REFEREE-2 l. 29 «No claim is FALSE as the packet states it. There is no gap in the
  packet.»).
- L41 (referee-originated proofs): no proof text of THIS packet is referee-originated (REFEREE-2 §5 l. 177 «There is no referee-originated
  proof (L41), so no «referee-originated» tag is needed.»; L1 l. 45; REFEREE: no gap, no repair). The premises carry referee-originated
  repairs in their own packets: COPY's converse (G-ST-1 = P-1, P-N5-STAIR fixes entry 1), which DESC-ROOT applies («Apply [COPY] (both
  directions) to each pair (x_i, x_(i+1)) at each transition of [k′, k].», packet l. 63) and whose rank-bit argument ORIGIN-NEW's Φ step
  reuses (l. 97); FUEL-COUNT's G-ODD-2 repair (P-N5-ODD fixes entry 2), used by FUEL-ROOT-STAIR. L-2's scope tail does not name them
  (FLAG F-2); R99-draft's and R98-draft's titles do.
- Fixes (docs/new/P-N5-ROOT-fixes-box114.md, L-NEW successors 42 / 43, APPEND-ONLY, F0 and entries 1-3, three commits each +N/−0: c4279144
  (2026-10-31T16:32:58Z, new file, 46 lines, F0 + entry 1), be131555 (19:32:23Z, +42/−0, entry 2, with L-1; the file then sha1
  5f144b41a4d37fac05fa39c9113a4a801b9e2dbe, 88 lines) and 7988e2f4 (20:57:08Z, +34/−0, entry 3, with L-2; sha1
  8e08a8c00be8e235a5210986da1949aa83f85c93, 122 lines; = l-new head 401d283a = trunk; the last commit touching the file)). Header (l. 2-3):
  the frozen packet and line are «NOT edited.» Each entry:
  - F0 (l. 6-18): REFEREE 21's report d8a2f428 «SIGNS DESC-ROOT (with its counting), ROOT-STAIR, ORIGIN-NEW with RELAY («the R15 A/B step
    was checked with special care»), NEW-FUEL with ROOT-SPLIT, and FUEL-ROOT-STAIR (conditional on [FUEL-COUNT] landing). No gap.» (l.
    8-9); the item map (l. 13-18).
  - Entry 1 (l. 20-45): ROOT-L1, ROOT-L2, ROOT-L3 quoted verbatim; repairs: the binder, the pins «until then» by commit and sha1, HC_F and
    the key («This is P-N5-ODD §6's definition, verbatim in content.», l. 46).
  - Entry 2 (l. 49-88): REFEREE-2 25's report d1c493fb, «REFEREE-2 SIGNS every item, with no packet gap. ORIGIN-NEW's R15 A / B step is
    sound (it is landed R91 Lemma OPT-OFF).» (l. 50); ROOT114-L1 quoted verbatim with the boundary counterexample; repairs in L-1 (l.
    74-88); P-1, P-2 recorded, not applied.
  - Entry 3 (l. 90-122): REFEREE ROOT-L4 / ROOT-L5, CHECKER C109 E-3 and Lead reading L43 quoted; «Both clauses are DROPPED (C109 E-3 move
    (i), applied to both; no statement of the line uses them).» (l. 116); «The packet body (frozen, f06f493e) keeps R162 / R163 as lane
    history; it is not edited.» (l. 118); the kept frz32 DEAD (l. 119-120).
  No fix changes a signed statement: entries 1-3 bind, pin, define and word the line (REFEREE-2 l. 57 «Fix (wording only; the packet's
  proofs are unchanged)»).
- Not signed: §1 (premises and notation; REFEREE «CHECKED», l. 18); §7 DEAD ends and DATA and §8 READING (packet l. 10; REFEREE l. 24
  «not to sign. The pins re-run and agree (§7)»). The lane DEADs of §7: (a) «Every root descent is a fuel re-route» (without «new edge»)
  (l. 133), killed by red/n5inj/instances/frz32 with its start, «3 R-descents entering by old edges (k 3: 2 → 17; k 7: 17 → 5 and 13 → 5),
  all relays» (l. 133-134); (b) «T_F = 0» (l. 135), lcount2_n23 T_F = 1; (c) the switch-site witness set (l. 136-137). Of these, L-2's
  scope tail names (a) only: «every root descent is a fuel re-route» DEAD (frz32: old-edge relays). Both referees reproduced the instance
  with their own engines (REFEREE §7 l. 92 «frz32: R 21, S 2, ROLD 3, NF 44, ON 44;»; REFEREE-2 §4 l. 161 «frz32's 3 old-edge relay
  R-descents (§7 DEAD (a)) are reproduced.») and both accept the clause under L43: REFEREE addendum l. 200-203 «The remaining clause «every
  root descent is a fuel re-route» DEAD (frz32: old-edge relays). I AGREE with REFEREE-2 that it is allowed under L43.», «The statement is
  universal, with no constant: every R-descent of every W-run is a fuel re-route.», «One instance refutes it, and its terms (R-descent,
  fuel re-route) are defined in the line.»; REFEREE-2 L1 Addendum 1 l. 62-63 «The clause «every root descent is a fuel re-route» DEAD
  (frz32) is a universal statement refuted by one instance, not an asymptotic one. I read it as allowed under L43 as worded (Lead
  decides).», L2 l. 11. L43's test («one instance exceeding an EXPLICIT bound»): frz32 has R^old_F = 3 where the statement says R^old_F =
  0. The clause says «root descent», L-2 defines «R-descent» (FLAG F-3). OPEN, not claimed: whether HC_F, R^old_F, S_F or TS_F is
  polynomially bounded on W-runs (packet §8 l. 153 «The open terms are HC (higher-key Ξ-changes at fuel targets), R^old, S and TS.»);
  G-N5-TIME. The §8 READING (l. 150-152, «The chain descents → R-descents → fuel re-routes closes, through FUEL-COUNT's HC, into the
  landed XI-CH-POLY core (RESULTS R95, XI-RUN).») is not landed.
- Referee strengthening (NOT part of this entry; remarks of one referee, or of both outside the verdict cells):
  (i) ORIGIN-NEW is RESULTS R91's Lemma OPT-OFF applied to G′ (REFEREE-2 P-2, §3.3 l. 100-101; fixes entry 2 l. 50, l. 87-88).
  (ii) NEW-FUEL holds with k unbound, via R15 (d) (REFEREE-2 P-1, l. 62-68: «833 new-edge switches at the transition leaving a W-run
       (BND_newedge_*), and 0 NEW-FUEL failures among them»).
  (iii) «**Is a root change ever at C?** No.» (REFEREE-2 §3.3 l. 103); «The packet does not need «z ∉ C».» (l. 105).
  (iv) Mutation controls (REFEREE §7 l. 98-101): «MUT 1 (NEW-FUEL for every switch): NF_V 6.», «MUT 2 (DESC-ROOT stops only at a vertex
       switched at k): DR_V 5, DR0_V 7.», «MUT 3 (DEAD (a), «every R-descent enters by a new edge»): OLDEDGE_V 5.»; REFEREE-2 l. 168 «The
       tool bites: the BND probes find the 2,977 corpus and 42 pin boundary failures of ORIGIN-NEW-as-worded (ROOT114-L1). So ONEW is not
       vacuous.»
  (v) REFEREE's optional precision on L-2, frz32 with path and sha1 (addendum l. 206), not applied (D-7).
- Honest limits: (i) REDUCTIONS and EQUIVALENCES: no count is bounded. DESC-ROOT moves descents to R-, T- and S-descents (T to tie
  switches), ROOT-STAIR moves |F| to T1_F + R_F + S_F + TS_F, ROOT-SPLIT and NEW-FUEL move R_F to fuel re-routes and old-edge relays, and
  FUEL-ROOT-STAIR moves fuel re-routes to HC_F; each up to polynomial factors. G-N5-TIME stays open. (ii) Everything holds inside W-runs,
  for transitions k → k + 1 of F, which are not whole runs (R89); at the cut k = q the statements are false as the frozen line worded them
  (ROOT114-L1: w_re3_1; 2,977 corpus boundary origins), and L-2 excludes it. (iii) DESC-LIN and DESC*-LIN are NOT settled here. L-RED
  R162 (DESC-LIN) and R163 (DESC*-LIN, the weak form) are lane work; their DEAD clauses were in the frozen line (R162) and the L-1 object
  (both) and are dropped at L-2 (REFEREE ROOT-L4 / ROOT-L5; C109 E-3 move (i); Lead reading L43: a lane DEAD of an asymptotic statement
  «enters as DATA with its numbers and source commit, or not at all»). This entry records neither as a claim. REFEREE §C l. 180 «Finite
  data refute only c < 2.23.» (on R163). (iv) Premises: [COPY], [STAIR] and [FUEL-COUNT] are signed but not landed at this draft; R100
  lands after R98 and R99; the line pins them by lane commit and sha1 (F-1). COPY's converse and FUEL-COUNT's proof rest on
  referee-originated repairs of their packets (G-ST-1 = P-1; G-ODD-2), named in those packets' lines, not in L-2's tail (F-2). (v) The
  standing premise R57 (1E-N3) is used DIRECTLY by ORIGIN-NEW at an S4a step (covered by Lead reading L42); R15 (a), (b) give the optimum
  argument away from own cycle nodes, and y ∉ C makes y no own cycle node (REFEREE §4 l. 56; REFEREE-2 §3.3 l. 98). The code's match to
  SPEC is DATA (R15 G-N5T-1). (vi) Counts are transitions, descents and switches, not bit operations; no running-time bound. (vii) Not M3,
  not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open.
- Data (DATA, not proof): pinned (packet §7 l. 145 «Pins (check.sh «box 113 DESCSTAR»): w_re3_1, hit_b6a_1, frz32, lcount2_n23, cp_K4.»).
  experiments/new/check.sh at 7988e2f4: sha1 8e854867a5012fb9ea88557396f43d20231dad09, 616 lines; the box 113 block is l. 592-597,
  identical at ed2fdaf2 (the freeze), at l-new head 401d283a and at trunk f3c2df11 (diff of l. 592-597: none); there is no separate box 114
  block. The packet and line files are NOT sha1-pinned in L-NEW's check.sh (C109 N-1). Re-run for this draft from a `git archive` of
  7988e2f4 (experiments/ and docs/new/; from experiments/new; GIT_DIR set to the repository, as for the R99 draft), l. 1-8 (set -euo
  pipefail, cd, tmp) plus l. 592-597, 2026-10-31 22:23:00Z-22:23:01Z by date -u, rc 0; output the line «box 113 DESCSTAR: SW-WIT,
  DESC-ROOT, ORIGIN-NEW, NEW-FUEL hold on 5 pins; frz32 3 old-edge relay root descents; lcount2 T-type 1; cp_K4 switch-site U not
  passive-proof (388): PASS». The block greps «DESC5 frz32.pg n 32 NFSW 44 NFVIOL 0 ORIGCH 44 ONVIOL 0 RD_K1 21 RD_NEWNOTFUEL 0 RD_OLDEDGE
  3 RD_NEW 18 RD_FUEL 18» (frz32: 3 R-descents by old edges, the DEAD's instance), «DESC5 lcount2_n23.pg n 23 NFSW 5 NFVIOL 0 ORIGCH 4
  ONVIOL 0 RD_K1 1 RD_NEWNOTFUEL 0 RD_OLDEDGE 0 RD_NEW 1 RD_FUEL 1 MAXRD_V 1 MAXRD_PAIR 1 DR 1 DT_ 1 DS 1», «DR 11 DT_ 0 DS 2 DMISS 0»
  (w_re3_1), «DR 17 DT_ 0 DS 1 DMISS 0» (hit_b6a_1) and five «ONVIOL 0 », «NFVIOL 0 », «DMISS 0 », «ROOTMISS 0 ». Supporting block for
  the repaired start of packet §7 (l. 190-210, box 55, which runs n3cov_lean on box113/inst/n3cov_lean_fixed.start; same archive),
  22:23:01Z-22:23:03Z, rc 0: «box 55 P-N5-SF: pcheck PASS on n3all_maxph_0 (fallback), switchbestexp_2 (SBC 4), n3cov_lean (LAM 4, SBC 11),
  MUT bites; quotes PASS: PASS». Pin files at 7988e2f4 (sha1): frz32.pg b251897c…, frz32.start 4adb74f1…; w_re3_1.pg c59735b4…,
  w_re3_1.start 3614ad94…; lcount2_n23.pg dd9847c6…, .start 7d3626aa…; cp_K4.pg db621f0a…, .start 4c8694a8…; hit_b6a_1.pg ff1cd2f9…,
  .start 89ae7c5b…; desc5.py 148caea6…. Oink NOT RUN for this draft (the block does not call it); REFEREE l. 109 «Oink 8fbf0a7 `--zlk
  --verify` verifies the solution on frz32, lcount2_n23, w_re3_1 and cp_K4.»; REFEREE-2 §4 l. 165 «It runs `oink --zlk -v` on each pin,
  and Oink reports «verified» on every one.»
  DATA OF RECORD (packet §7 l. 138-142; L-SI box 53's 1,132 games, 14,028 W-run transitions): DESC 14,755 = R 7,606 + S 932 + T 1 + COPIED
  6,216; TS 397; DESC-ROOT misses 0; origin root changes 25,679, ORIGIN-NEW violations 0; new-edge switches with k − 1 ∈ F 27,539, NEW-FUEL
  violations 0; R^old 47. Re-summed for this draft from the stored outputs: equal (to check (10)).
  REFEREE (successor 21; own docs/referee/scratch/root114_probe.py, «no lane code», l. 83): 719 distinct games, MAXN 100, 656 analysed
  (l. 102): «950 W-runs, 7,401 transitions;» (l. 103); «6,584 descents = R 3,693 + T 1 + S 443 + COPIED 2,447, every one walked by DR; TS
  201; ROLD 32;» (l. 104); «ON 11,251 origin root changes, NF 11,884 new-edge switches;» (l. 105); «VIOLATIONS 0.» (l. 106); pins (l.
  92-97) each equal to the lane's desc5 line, cp_K4 «R 388 (all descents), NF 3,177, ON 3,177»; «VIOLATIONS 0 on all five» (l. 97);
  L-NEW's block «box 113 DESCSTAR» at ed2fdaf2 «run alone in a detached worktree: PASS, EXIT 0.» (l. 108).
  REFEREE-2 (successor 25; own docs/referee-2/R2-N5-ROOT114/root_check.py, «The lane's box113/*.py is not imported.», l. 135): corpus
  1,132 games (l. 137), «RESULT PASS, 0 violations, in all three.» (l. 138); table l. 140-148, every row equal to the packet's §7
  («14,755 / 7,606 / 932 / 1 / 6,216», «25,679 (30,488 − 4,809 at k = p), 0», «27,539, 0», «47 (R^fuel 7,559)»); OPTOFF «695,167 checks,
  0 violations» (l. 113); pins (l. 152-159) incl. fbg_K4_m6_m48 on its fixed start «DESC 640, COPIED 430, R 210 = R^fuel 210, R^old 0».
  No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-ROOT114.md (successor 21): report d8a2f42862f34de9015aa4654dfd2a82896f93c0 (2026-10-31T15:41:34Z, new file, 143 lines, with
  docs/referee/scratch/root114_logs/; first on trunk by merge 7c455f40, 16:13:51Z): §1 CHECKED, §2-§6 SIGNED, no gap, line REQUIRED
  ROOT-L1..L3; §C 74025e44f7828a29f9961bfd5b92f6030bd5d713 (20:01:05Z, +51/−0; the file then 194 lines, sha1 611c29b3…; on trunk by 83b5acc9, 20:27:53Z): L-1 and the fixes
  checked (l. 145-194), «Verdict on L-1: does NOT yet match.» (l. 193); §C addendum af9cd763845d6bbbe7d90751a418ff9f5515ee0a (21:24:55Z, +13/−0, l. 196-207; the file now
  207 lines, sha1 fdd7d78cc01e17c5b92e16b5d0df5b4363a36465, = referee head; on the local trunk by f1b1044e, 22:19:06Z, NOT on origin trunk
  6d653c3f): «Verdict on L-2: MATCHES (Opus 5.5, D15).» (l. 207). REFEREE-2 (successor 25): docs/referee-2/R2-N5-ROOT114.md d1c493fb982abe4a83b683958a962b727d76cb1e
  (18:45:09Z, new file, 198 lines, sha1 a9654fae64db91b48c0d07a4d2fc4ea25ddca349, unchanged since; with R2-N5-ROOT114/ tools and logs; on
  trunk by c93d8ddb, 19:31:36Z): every item SIGNED (l. 21-27, l. 189-190); R2-N5-ROOT114-L1.md 83c1838f4c6de2366e39133f88651190b7b3c86c (20:00:13Z, new file, 56 lines)
  + Addendum 1 faa8dac9d846c4a00d52e0c4ce6e6d646de74a64 (20:28:55Z, +8/−0; the file now 64 lines, sha1 ab8059056ffd3132d13836c799ce6ebef6625612; both on trunk by a20cf406,
  21:23:35Z): ROOT114-L1 / L2 closed, «**MATCHES** (Opus 5.5, D15).» (l. 51), L43 agreement (l. 58-64); R2-N5-ROOT114-L2.md 3bb41a4c85f3e2233660561a2711ed07e98f781d
  (21:24:48Z, new file, 19 lines, sha1 e486277c1e6e49593a40bc7a8c9e9495678fbd5d, = referee-2 head; on the local trunk by f1b1044e, NOT on
  origin trunk): «Verdict: **MATCHES** (Opus 5.5, D15). All my ROOT line items are closed.» (l. 14). Lane: freeze ed2fdaf2a831d963dc3d5078cf66b02e1fd9f35b,
  L-1 be131555d8779fac85095e146a1c5ded25cf59fb, L-2 7988e2f45a47e2a50a121773ea1f47874cfce086.
  INDEPENDENCE: REFEREE l. 8 «Independence: I opened no docs/referee-2/ file for this packet.»; §C l. 149 «I opened no docs/referee-2/ file.
  REFEREE-2's items are known to me only as fixes entry 2 quotes them.» REFEREE-2 l. 4-5 «Independence: written without opening
  docs/referee/ (REFEREE's d8a2f428) or docs/new/P-N5-ROOT-fixes-box114.md (c4279144). I read both only after this report is pushed.»
  REFEREE wrote first (d8a2f428 15:41:34Z), REFEREE-2 later (d1c493fb 18:45:09Z). The L-1 and L-2 word diffs (83c1838f, 3bb41a4c;
  74025e44, af9cd763) each re-hashed the object and diffed it against its predecessor itself; REFEREE-2's L-1 and L-2 files carry no
  independence sentence. No review imported lane code (REFEREE l. 83; REFEREE-2 l. 135); the lane's script ran only as the pinned block
  (REFEREE l. 108).
  Differences, resolved: ROOT114-L1 found by REFEREE-2 only (REFEREE §C l. 167-168, quoted in to-check (3)); line items numbered
  differently (to check (3)); R163's DEAD: REFEREE made ROOT-L5 REQUIRED at the L-1 object, REFEREE-2 MATCHED L-1 before L43 and agreed in
  its Addendum 1; both MATCH L-2. No disagreement in substance; no ruling was needed beyond L43.
- TARGET.md diff: «n := |V|» is TARGET.md §1 l. 8's n («n = |V|, m = |E|, d = |pr(V)| ≤ n + 1.»), V TARGET's vertex set (l. 6); games
  are TARGET.md §1 games (REFEREE-2 §5 l. 172 «Subject: «N5 on EVERY game» uses TARGET §1's games and n := |V|.»). The line (L-2) makes no
  M4 claim and no TARGET claim; its own scope clause reads «REDUCTIONS and EQUIVALENCES (no count is bounded here; «every root descent is
  a fuel re-route» DEAD (frz32: old-edge relays); G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim)» (L-2 verbatim,
  by script). REFEREE §8 l. 132-133 «TARGET.md diff: «REDUCTIONS and EQUIVALENCES (no count is bounded here; …; G-N5-TIME stays OPEN; not
  M3, not a step-4 pass, not a TARGET.md claim)» ✓. No algorithm claim.» (at the frozen line); REFEREE-2 §5 l. 175-176 «This is
  consistent with TARGET §2 (M4 untouched) and §4 (nothing is presented as M3/M4). The DEAD clauses name their instances.», «There is no
  asymptotic word («O(1)», «linear», «unbounded») backed only by fixed pins.»; REFEREE-2 L2 l. 12-13 «The scope words are unchanged:
  REDUCTIONS / EQUIVALENCES, G-N5-TIME OPEN, not M3, not a step-4 pass, not a TARGET.md claim.» Not a claim of TARGET.md §1 or §2 (lemmas on
  descents, root changes and fuel re-routes inside W-runs, and two reductions between counts; no bound on a W-run, on a run or on running
  time; no algorithm claim); not a step-4 pass. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER R98's and R99's UPDATEs of G-N5-TIME (PENDING: R98-draft and R99-draft at
6d653c3f; at f3c2df11, GAPS unchanged since 9777660f, the last UPDATE on l. 11 is R97's, «UPDATE 2026-10-31 07:02Z: RESULTS R97 (P-N5-SRC;
CHECKER C107 449cb6fc) …», before the row's closing « |»), built by script (upd100.py; upd99L3.py's rule, labels searched after the
binder) only from the clauses of the title line L-2, with R94's-R99's construction (labels behind their clauses; the scope tail as in
R95's-R99's UPDATE: the lane DEAD stays inside the scope words, before the source note, which is kept). The same script reproduces R97's
landed UPDATE, R99-draft's and R98-draft's UPDATEs at 6d653c3f byte for byte. L-2 holds twelve "|"; the UPDATE holds none: (q1) «n :=
|V|» → «n := the number of vertices of the game»; (q2) «|F| := q − p,» → «q − p is its number of transitions,»; (q3) «TS_F ≤ n·|F|» →
«TS_F ≤ n times the number of transitions of F»; (q4) the other three «|F|» → «the number of transitions of F»; these replacements are not
title text (to check (9)). Date «2026-10-31» (the landing date; corrected at landing if later, F-5); time and CHECKER commit to be filled
at landing; head «(P-N5-ROOT; …)» as briefed (F-4):
UPDATE 2026-10-31 <HH:MM>Z: RESULTS R100 (P-N5-ROOT; CHECKER C110 <checker>) [refereed-only] LANDED: N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum; for S4a at a transition k → k + 1, σ_(k+1) is the pointwise optimum of the one-player arena H_k, H_k := S4a's arena at k (Even y keeps {σ_k(y)} ∪ Iσ_k(y), Odd follows τ_k)); premises RESULTS R15 (a), (b), (d), R91 (Lemma W-MON), R93 (Fact LEX), P-N5-SRC §2 (proof of RESULTS R97 PLAY-CAUSE^S), P-N5-STAIR (Lemma COPY in both directions and Theorem STAIR, as in its line L-2: l-new 6903f1b3, docs/new/P-N5-STAIR-line-L2.txt, sha1 44f56e96d41d45653c4b7bc2f140c587e8e407e6) and, for (Corollary FUEL-ROOT-STAIR) only, P-N5-ODD (Corollary FUEL-COUNT: l-si 0afc0d70a, docs/si/P-N5-ODD-box57.md §6, sha1 03eec41d, with its fixes entries 1-2)), with: a run is the sequence of states (σ_k, τ_k), a transition is written k → k + 1, and an Even vertex y switches at k if σ_(k+1)(y) ≠ σ_k(y); n := the number of vertices of the game; values, ⊴, ◁, ⊵, ▷ as in SPEC S1; Ξ_k := Ξ_{σ_k} and Iσ_k := Even's improving edges at k (SPEC S2: {(y, z) : z ≠ σ_k(y), Ξ_k(z) ▷ Ξ_k(σ_k(y))}); W-run F = [p, q] := RESULTS R89's, with τ and C := {v : λ_W(v) = v} fixed on F, q − p is its number of transitions, W_k the [S1-val] valuation of the (σ_k, τ)-plays, s_k(v) := σ_k(v) for Even v and τ(v) for Odd v, T1_F := the transitions of F with W_(k+1) = W_k and WCT_F := the number of transitions of F − T1_F; β, first-difference positions, descents and DESC_F as in P-N5-STAIR's line L-2; a descent (x, k) of x with previous change of W(x) at k′ is of type R if x switches at k, of type T if not and x switches at some t with k′ < t < k, of type S if x switches at k′ and at no transition of (k′, k], and COPIED otherwise; R_F, T_F, S_F := the descents of F of each type; a TIE SWITCH is a pair (y, t) with y switching at t and W(y) unchanged at t, TS_F their number on F; a ROOT CHANGE is a pair (y, k) with k → k + 1 a transition of F, y switching at k and W(y) changing at k, an ORIGIN if W(σ_(k+1)(y)) does not change at k and a RELAY otherwise; a FUEL RE-ROUTE of (y, z) at k is as in P-N5-ODD §6 (y switches to z at k, k − 1 ∈ F, (y, z) ∉ H_(k−1), Ξ_(k−1)(z) ≠ Ξ_k(z)), N_F(y, z) their number on F; the KEY of a change a → b of Ξ(z) is (2, 0) if the cycle node changes, else (1, r) with r the top rank of the difference of the path sets, else (0, 0), ordered (0, 0) < (1, r) < (1, r′) < (2, 0) for r < r′, and the key of a fuel re-route of (y, z) at k is the key of the change Ξ_(k−1)(z) → Ξ_k(z); HC_F(y, z) := the number of transitions u of F at which Ξ(z) changes with a key strictly greater than the key of the last fuel re-route of (y, z) at a transition ≤ u; R^old_F := the R-descents (y, k) with (y, σ_(k+1)(y)) ∈ H_(k−1), and R^fuel_F := R_F − R^old_F: for every N5 run on every game and every W-run F = [p, q] of it, every vertex v, every Even y, every vertex z and every transition k → k + 1 of F: if v has a descent at k with previous change of W(v) at k′, and j is the least index with x_j ∈ C or x_j switching at a transition of [k′, k] along x_0 := v, x_(i+1) := s_(k+1)(x_i), then x_j ∉ C and x_j has a descent at k with previous change at k′, of type R, T or S; hence DESC_F ≤ n·(R_F + T_F + S_F) and T_F ≤ TS_F (Lemma DESC-ROOT); the number of transitions of F ≤ T1_F + n(3n + 1) + (3n + 1)·n·(R_F + S_F + TS_F), and R_F + S_F ≤ n·WCT_F, TS_F ≤ n times the number of transitions of F (Theorem ROOT-STAIR, an EQUIVALENCE); if (y, k) is an origin root change and k − 1 ∈ F, then (y, σ_(k+1)(y)) ∉ H_(k−1) (Lemma ORIGIN-NEW); if y switches at k to z, k − 1 ∈ F and (y, z) ∉ H_(k−1), then Ξ_(k−1)(z) ≠ Ξ_k(z), so (y, z) is a fuel re-route at k (Lemma NEW-FUEL); if (y, k) is a root change and k − 1 ∈ F, then (y, k) is a fuel re-route or a relay entering by an edge of H_(k−1), and every R-descent has k − 1 ∈ F (Corollary ROOT-SPLIT); R^fuel_F ≤ Σ_(y,z) N_F(y, z) ≤ Σ_(y,z) n(n + 2)(HC_F(y, z) + n), so the number of transitions of F ≤ T1_F + n(3n + 1) + (3n + 1)·n·(n(n + 2)·Σ_(y,z) (HC_F(y, z) + n) + R^old_F + S_F + TS_F), the sums over Even edges (y, z) with N_F(y, z) ≥ 1 (Corollary FUEL-ROOT-STAIR): REDUCTIONS and EQUIVALENCES; no count is bounded here; «every root descent is a fuel re-route» DEAD (frz32: old-edge relays) (P-N5-ROOT, docs/new/P-N5-ROOT-box114.md; L-NEW successor 42; fixes docs/new/P-N5-ROOT-fixes-box114.md entries 1-3). G-N5-TIME stays open.

Addendum 1 (subagent, for the Lead; does not land): (1) Both L-2 verdicts are on origin lane branches (claude/referee af9cd763,
claude/referee-2 3bb41a4c) and on the local trunk f3c2df11 (merge f1b1044e) but NOT on origin trunk 6d653c3f: push trunk before landing.
No placeholder token is left except <HH:MM> and <checker> in the UPDATE and «checker PENDING» in the title fill. (2) Quote sweep (script q100.py, outermost «…», «\|» read as «|», whitespace joined, split at «…»; sources: packet, fixes, the three line files, R-N5-ROOT114.md at af9cd763, R2-N5-ROOT114.md at d1c493fb, R2-N5-ROOT114-L1.md at faa8dac9, R2-N5-ROOT114-L2.md at 3bb41a4c, DECISIONS.md, RESULTS, GAPS, TARGET.md, C106, C108, C109, LEAD-STATE.md, R98-draft.md and R99-draft.md at 6d653c3f, P-N5-ODD-box57.md at 0afc0d70a, STAIR L-2 / L-3, check.sh at 7988e2f4, this draft's pin outputs and UPDATE, trunk commit subjects): entry (title + body) l. 312-565: 185 quotes, 183 parts of 6+ characters, all 183 found; to-check notes l. 1-311: 312 quotes, 255 parts, 252 found, 3 not found, all this draft's own words («### R100» twice, which occurs 0 times by design, and the heading schema «… entries 1-3), CHECKER PASS (…)»); GAPS preamble and UPDATE l. 567-577: 13 quotes, 11 parts, all found; this Addendum: 4 parts, 2 not found (the heading's own prefix and fill). Found only in R98-draft / R99-draft or commit subjects (checked by hand): «at the frozen line», «at the L-1 object» (this draft's convention), the two UPDATE schemata of (9) (R99-draft's), «… into claude/vibrant-johnson-nxvvxo» (merge subjects), and «the proofs of FUEL-LEX and FUEL-COUNT carry referee-originated repairs» (also in docs/si/P-N5-ODD-line-L3.txt at 2f8e5b2e, by grep). A line check (qline100.py) took the 205 quotes preceded by an «l. N» and found each at or near its cited lines; its 39 heuristic misses were read by hand: each is a first-occurrence or nearest-«l.» artefact (e.g. «**SIGNED**» rows), none a wrong line. (3) Checked by script after the fill: l. 312 = «### R100 [refereed-only] » + L-2 without its
newline + «, CHECKER PASS (docs/checker/C110.md, checker PENDING)» (True); l. 577 = upd100.py's output (True), 0 "|", one <HH:MM>, one
<checker>; l. 566 blank; the only «### R» heading is l. 312; entry (title + body) l. 312-565, GAPS preamble l. 567-576,
UPDATE l. 577. (4) NOT RUN / NOT DONE: Oink (the pinned block does not call it); the referees' own tools (not re-run);
REFEREE-2's BND probes (the 2,977 / 42 boundary counts are taken from its report, not re-run); fbg_K4_m6_m48 (no check.sh block; stored
output read only); the packet's corpus re-run (the stored desc5 outputs were re-summed, not regenerated); R98's and R99's landing state
(both PENDING at C108 / C109 Add. 1). (5) For the Lead: FLAGS F-1 (stale STAIR / ODD pins at landing), F-2 (L41 through premises) and F-3
(«root descent») are CHECKER questions; F-4 (P-N5-ROOT name clash with R74) and F-5 (UPDATE date) are landing items. I did not change the
line. If CHECKER asks for a line L-3, the title, the body's quotes of the line (TARGET.md diff, line history) and the UPDATE are rebuilt
from it with the same scripts. Scratch scripts and outputs (not committed), in /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad:
wdiff100.py, upd100.py / upd100.txt, fill100.py, sum100.py, fxq100.py, q100.py / q100.out, pin100a.sh / pin100a.out, pin100b.sh /
pin100b.out, pin100.time, check_7988.sh, arch7988/.
