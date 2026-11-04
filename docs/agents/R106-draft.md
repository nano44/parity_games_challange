# Draft RESULTS R106 (Lead; first fill 2026-11-04T05:01:27Z by date -u (subagent); on P-IDEAL-CUBE line L-2, docs/new/P-IDEAL-CUBE-line-L2.txt, l-new a0bb2694, sha1 449421e4cfaedbef577f68720fab4924111cd170) — to CHECKER C117
FIRST FILL. Read at the origin heads fetched at the start of the fill (git fetch, then git ls-remote, 2026-11-04T04:43:31Z: l-new
a0bb2694, l-red 39588215, referee 3c3185d8, referee-2 993c1710, checker 49f85ffc; origin trunk 8b31b166; local trunk 58198d07 = the
merge 3f4ea5aa of those five heads plus one Lead commit, neither pushed; 58198d07 changes only docs/NOW.md and three docs/agents/ files,
so RESULTS (sha1 8309502865f8caa43403f415a5e0dd757a0c0ad1), GAPS (bc53d0789e3528366ebc9bc9e10b04f1a114639a), DECISIONS, DECISIONS-INDEX
and TARGET.md are byte-equal at 58198d07, 3f4ea5aa, origin trunk 8b31b166 and the R105 landing commit 91c1464f (same blob ids)): the
packet and L-1 (d97555d4), fixes entries 1-2 and L-2 (a0bb2694; the packet, L-1, the fixes and L-2 unchanged at the l-new head a0bb2694,
by cmp and sha1); REFEREE successor 23's docs/referee/R-P-IDEAL-CUBE.md (report 5ef7bf47, §C 3c3185d8); REFEREE-2 successor 26's
docs/referee-2/R2-P-IDEAL-CUBE.md (0787732b) and R2-P-IDEAL-CUBE-L2.md (993c1710); the referees' logs (REFEREE
scratch/xinew_logs/cube_probe.txt, cube_gateT.txt; REFEREE-2 R2-P-IDEAL-CUBE/logs/run1.log, control.log); notes/L-NEW.md at a0bb2694 (l.
11-17, 26, 54-67); experiments/new/check.sh at d97555d4, abe2b94c and a0bb2694; DECISIONS D14, D18, D19, L43, L41; RESULTS R104 (title
l. 9864, the model definition only) and R105 (title l. 10155; body l. 10155-10399); docs/checker/C116.md (49f85ffc). Re-runs (scratch,
git archive of a0bb2694's experiments/new and docs/new): the commands of check.sh blocks w102, w103 and the P-IDEAL-CUBE pin block,
2026-11-04T04:46:17Z-04:46:47Z, rc 0, output byte-equal to the blocks' expected strings and PASS lines ((10)); my own gate-order probe
on ladder.py's L_K, 2026-11-04T04:51:46Z, rc 0 ((10)).
TRUNK STATUS AT THIS FILL (by script, git merge-base --is-ancestor against local trunk 58198d07 and origin trunk 8b31b166): d97555d4,
abe2b94c, a0bb2694, 5ef7bf47, 3c3185d8, 0787732b, 993c1710 and 49f85ffc are ancestors of local trunk 58198d07 (exit 0 each) and NOT of
origin trunk 8b31b166 (exit 1 each); 43125a61, 91c1464f and e85c3bb2 are on both. The Lead pushes trunk before landing. C113 E-2 lesson:
the body names these commits on their branches only and makes NO statement about trunk. C113 E-1 lesson: the title is L-2 verbatim with
no insertion (L-2 carries its own date parenthesis and source note). C114 Add. 1 E-1 lesson: the GAPS UPDATE head carries «<DATE>»,
filled with the landing date at landing. C115 E-1 lesson: the premise route is checked against what RESULTS records (G-4 below). C116
G-1: the UPDATE tail rule of R105 is applied unchanged ((9)). C116 G-2: a name clash is settled by one body sentence (G-3; the sentence
is in the body, Honest limits (viii)). In the body (title + entry), L-2 is the current line; sentences about the earlier line say «at
L-1».
to check: FLAGS FIRST (G-1 to G-11; none REQUIRED from my side; no referee raised any of them as REQUIRED), then the CLEAN items and
(0)-(14), then the proposed Dead-ends row DE36 (after the UPDATE; the Lead decides).
- G-1, TITLE SHAPE AND SOURCE NOTE (note; no Lead insertion). L-2 contains «2026» once, as « (2026-11-04) — », the only « — » (by
  script), and ends with the source parenthesis «(P-IDEAL-CUBE, docs/new/P-IDEAL-CUBE.md; L-NEW successor 50)». The title is "### R106
  [refereed-only] " + L-2 + the fill ", CHECKER PASS (docs/checker/C117.md, checker PENDING)" (as R90-R105), nothing inserted. NOTE:
  unlike R104's and R105's source notes, L-2's names no fixes file, while docs/new/P-IDEAL-CUBE-fixes.md at a0bb2694 holds entries 1-2.
  Entry 1 replaces packet text (§0 l. 30-31, the «faces never tie» sentence; fixes l. 7-13) and says «No proof in the packet changes.»
  (fixes l. 15); entry 2 is L-2's word diff and changes the line only. Both referees checked L-2 against the packet with entries 1-2
  (REFEREE §C l. 169 «L-2 against packet + entries 1-2:»; REFEREE-2 L2 §2 l. 29-32 on entry 1 and §1 on entry 2) and neither asked for
  the fixes in the source note. The body names «fixes entries 1-2» wherever the body speaks (Object, Fixes); only the title keeps L-2's
  words. A one-word line change is not needed for any signed statement (my reading; the Lead decides; C116 §4's closing note ruled
  R105's «with its fixes entry 1» true, a different case).
- G-2, STRICT SYMBOL TEST (notes; both referees' clause checks are clean on L-2, (7)). (i) «T» is not bound in L-2; it is R105's «T
  steps of a run» (RESULTS l. 10155) and P-IDEAL-RED §0's «T := the number of steps (R104's L(G)).», carried by the premise «RESULTS
  R105» (packet l. 26-27 lists T in P-IDEAL-RED's notation). (ii) «C_b(x)» and «b» are used with «C_s(x)» bound on states and Q_G bound
  as «{0, 1}^D2 of states»; packet l. 33-34 «We» «write C_b, Ξ_b for C_(s_b), Ξ_(s_b).» (iii) «[b(x) ≠ C_b(x)]» is an Iverson bracket
  over x ∈ D2, not glossed; packet l. 74 «E(b) := Σ_(x ∈ D2) o_G(b)_x · 2^π(x)» with o_G(b)_x := 1 iff b(x) ≠ C_b(x) (l. 49), so the sum
  in L-2 is E(b). (iv) «e_x» (the x-th unit vector), «face», «free coordinate» and «sink» are plain cube words; «combed» and
  «decomposable» are glossed in L-2's parentheses. (v) The orientation clause «directs the edge between b and b ⊕ e_x away from the
  endpoint whose x-coordinate differs from C_b(x)» presupposes that C_b(x) = C_(b⊕e_x)(x), which is DECOMP (o) (packet l. 66-67); L-2
  does not state (o) as a clause (REFEREE §6 l. 108 «definitions of D2, Q_G, C_s(x) and o_G (= D-ORI)»: MATCHES). (vi) The bare «LP» in
  «so LP ≥ 2^(N/2+1) − 2» is LP_(L_K) at the start b_0, LP_G(s_0) as bound earlier in the line (packet l. 108-109). (vii) «#Mv_t» = the
  number of movers moved at step t («the set Mv_t» in the same clause; packet l. 90 «Σ_t |Mv_t|»). (viii) «level-0» and «gate indices»
  are R104's (level, gate index). None is a claim clause's quantifier left free.
- G-3, NAMES, SAME LABELS, OTHER MEANINGS (by script on RESULTS 83095028 / GAPS bc53d078; note; C116 G-2's remedy applied). 0 times in
  RESULTS and GAPS: «P-IDEAL-CUBE», «DECOMP», «MULTI→SINGLE», «LADDER-LP», «LADDER», «L_K», «Q_G», «o_G», «LP_G», «UP(i)», «D-ORI»,
  «D-DEC», «unique sink», «decomposable», «combed», «improvement orientation», «Weber», «2207.05985», «W-key», «C117». Same names, other
  meanings: (a) «R106» 2 times in RESULTS, l. 5407 «L-RED's R106 pin» and l. 5416 «L-RED's R106 mkr.py» (R86's entry), an L-RED box
  label, prefixed; (b) «LP» as a word 45 times in RESULTS and 6 times on GAPS l. 11: RESULTS R27's «Theorem LP» and «Corollary LP′»
  (title l. 1218, l. 1241-1314; GAPS l. 11, R27's UPDATE), R91's DATA check label «LP» (l. 6619-6621), «P-N5-LP» file names, and linear
  programs in DE32 («LP-guided», l. 10834) and DE33 (l. 10865); (c) «D2» 12 times in RESULTS as review-item labels («REFEREE-2 §C D2»,
  l. 5279-5450; «LATEP-D2», l. 6800-6966); (d) «AUSO» once (R3, l. 61, «RAR is defined on AUSOs»), the same meaning (acyclic unique sink
  orientations), no clash. After landing, «LP» and «R106» name two things; in L-2 «LP» is bound («LP_G(s_0), the largest length of a
  directed path of o_G from the start») and scoped by «In the IDEAL model of RESULTS R104». Applied (C116 G-2, «a name clash is settled
  by a body clause, not a rename»): one body sentence, Honest limits (viii). No line change.
- G-4, PREMISE ROUTE (the C115 E-1 class): CLEAN (my check). L-2's premise parenthesis: «premises: R104's definition of the model, and
  P-IDEAL-RED's Lemma ENC and Lemma LOCAL (b), RESULTS R105». What RESULTS records: R104's title (l. 9864) carries the model definition;
  R105's title (l. 10155) states «(ENC) the Ξ-order of β-sets is the order of the integers Σ ±2^rank» and «(LOCAL) an option's value
  depends only on the states on its chain», and R105's body records ENC verbatim (l. 10211, «(a) Lemma ENC (§1, l. 64-74)») and LOCAL
  (a)-(c) (l. 10214-10217, «(b) Lemma LOCAL (§1, l. 75-85)», with «(b) the same for every k when s, s′ agree on every strict
  Ξ-descendant of x»), both SIGN in both referees' tables; P-IDEAL-RED §0's notation is R105's body «Setting» (l. 10193). P-IDEAL-RED's
  own text of (b) (0ebddcf5, l. 78-79): «(b) If s, s′ agree on every strict Ξ-descendant of x, then Ξ_s(x, k) = Ξ_(s′)(x, k) for every
  k; if moreover s(x) = s′(x), then» «cur, A and c of x are the same under s and s′.» The CUBE proofs use exactly «C_b(x) depends only
  on b at strict Ξ-descendants of x» (packet l. 66), i.e. the first half of (b). The packet (l. 17-23): «LANDED: RESULTS R104
  (P-N5-REALIZE), ONLY its definition of the IDEAL model, as restated in P-IDEAL-RED §0.»; «SIGNED, not yet landed: P-IDEAL-RED
  (docs/new/P-IDEAL-RED.md at 0ebddcf5, sha1 06f2c186…, with fixes entries 1-2; both» «referees signed; RESULTS R105 when landed).»;
  «External definitions: [WW22] Def. 4 and §2.2, quoted verbatim in §1. Only the definitions are used; no theorem of [WW22] is a»
  «premise.»; «Nothing from docs/lit or docs/sources.» R105 has landed since (C116 Add. 1, 49f85ffc: «Verdict: R105 landed exactly as
  checked.»), so REFEREE's landing condition CUBE-P1 (l. 18-20) is met (§C l. 148-149 «CUBE-P1 is MET: the premise route is now landed
  R104 +» «landed R105.»), and L-2 cites «RESULTS R105» (fixes l. 21). Both referees checked the route: REFEREE §2 l. 47-53 (premises
  used, LOCAL (c) «cited but not needed», «No» «docs/lit and no docs/sources (grep).»); REFEREE-2 §0 l. 29-34 («**Premise route ✓, with
  two remarks.**», «No docs/lit, no lane file.»); REFEREE-2 L2 l. 38 «Premises: R104's definition, P-IDEAL-RED ENC and LOCAL (b) (R105,
  landed), and [WW22] v1 definitions.» LOCAL (c) was listed at L-1 and in the packet (l. 19-20) but used nowhere (REFEREE §2 l. 51;
  REFEREE-2 LC-P2); L-2 drops it (fixes entry 2, item 6). L-RED R178 appears in L-2 only as R104's attribution of the model («(the model
  first stated in L-RED R178 §1)», as in R105's landed title). My grep (by script) of the packet: «docs/lit» once (l. 23, the premise
  list), «R178» 0 times, «R201» once (l. 182, §5 READING), «box153» 3 times (l. 4 the source note, l. 162 and 171 the machine check);
  none inside a proof block (l. 65-78, 86-89, 91-92, 135-147, 148-154). The step rule used in MULTI→SINGLE's proof («P-IDEAL-RED §0, the
  step rule», l. 86) is R104's definition («an IDEAL step moves every mover to the lexicographically least key … among its current
  option and the options with a strictly better Ξ-value», RESULTS l. 9864). No unlanded result, no lit note and no lane file is a
  premise; the only outside source is [WW22]'s definitions (G-11).
- G-5, L41 (the C109 E-1 class): not triggered (my reading; neither referee mentions L41). L-2 contains «referee-originated» 0 and
  «lane-authored» 0 times. The proofs are L-NEW successor 50's (packet l. 4-5 «Labels: PROVED (L-NEW 50, unrefereed) /» «DATA /
  READING.»). THREE POINTS TO CHECK: (a) fixes entry 1's sentence (acyclicity separates the two faces of x) is REFEREE-2's P-1 (§2 l.
  55-57), written into §0's definition by the lane as a «packet precision» (fixes l. 6), with «No proof in the packet changes.» (fixes
  l. 15); REFEREE §C l. 150-153 «CORRECT», «This is the argument my P-IDEAL-RED §3 (ii) used. No proof changes.» It makes C_s(x) well
  defined; it is not a signed statement of its own. (b) The two REQUIRED line changes are wording (REFEREE-2's LC-1 and LC-2 taken
  verbatim, REFEREE-2 L2 l. 22-23 «✓ verbatim as I asked»), not proof. (c) «The path is a path, not merely a walk, by DECOMP (b).»
  (REFEREE-2 §2 l. 90; also l. 75-76 for the corollary): the packet's proofs say «Concatenating the paths of MULTI→SINGLE gives a
  directed path» (l. 91) and «directed edges, consecutive (each starts where the previous ended)» (l. 154) and defines LP_G with «finite
  by DECOMP (b)» (l. 57); that a directed walk in an acyclic orientation repeats no vertex is the one-line consequence of DECOMP (b),
  proved in the packet. Not referee-originated (my reading).
- G-6, L43 (DEADs): CLEAN. L-2 has no DEAD (by script: «DEAD» 0, «O(» 0, «linear» 0). «polynomial» 3 times: «T ≤ LP cannot by itself
  give a polynomial bound», «(READING: a polynomial bound on T must use the W-key rule)», «bounds nothing polynomially». The first is
  the signed consequence of Corollary T ≤ LP and Theorem LADDER-LP for one proof route (REFEREE §C l. 162-163 «The signed part is now
  only «T ≤ LP cannot by itself give a polynomial bound». That follows from T ≤ LP and LADDER-LP: LP is» «exponential on L_K.»;
  REFEREE-2 §4 l. 119-120 «What is proved is narrower: T ≤ LP alone cannot give a» «polynomial bound.»); it is not a DEAD of an
  asymptotic statement, and its proof is refereed with explicit instances (REFEREE-2 §4 l. 117-118: «so «LP is polynomially bounded on
  degree-2 IDEAL-ACYC» is false, with a refereed proof. L43 is satisfied.»). The packet's own «DEAD» (l. 181, «The route «bound LP» is
  DEAD by Theorem LADDER-LP.») is §5 READING, not to sign, and is not in L-2. See (14) for the Dead-ends row.
- G-7, DATA vs READING (the C108 E-1 class): CLEAN. L-2 labels its unsigned text: «(READING: a polynomial bound on T must use the W-key
  rule)» (= REFEREE-2 LC-2, REFEREE CUBE-L1 met); «(DATA: on L_K with gate indices increasing in the option index, the IDEAL run from
  that start is empty)» (= REFEREE-2 LC-1); and the closing DATA parenthesis (decomp.py and ladder.py). NOTE on the middle DATA clause:
  it names no range of K. The lane's DATA is K = 1..10 (ladder.py, «ideal_T 0»), REFEREE's K = 1..7 (cube_gateT.txt «T(increasing gates)
  0 T(decreasing gates) 1»), REFEREE-2's K = 1..12 (run1.log «ideal_T 0»; decreasing gates T = 1 for K = 1..5, §3 l. 113-114, no
  committed log), mine K = 1..10 ((10)). The packet's reason (l. 157-158 «With all movers at level 0, the W-key rule picks the
  gate-least option, and with gates» «increasing in k that run has T = 0 from b_0 (DATA, §5).») is not a signed statement; both referees
  accepted the clause as DATA (REFEREE §C l. 165-168 «CHECKED»; REFEREE-2 L2 l. 23 «✓ verbatim as I asked»). My reading: a DATA clause
  on explicit instances, not an overclaim; it carries no claim weight (no signed statement uses it). Packet §5's READING (l. 179-182) is
  in L-2 only through LC-2's label.
- G-8, LEAD READINGS AND RULINGS AS ON FILE (the C111 E-1 class): CLEAN. L-2 cites no Lead reading and no ruling (by script: «Lead
  reading» 0, «L4» 0, «D1» 0). The lane works under D14 / D18 (packet l. 2 «L-NEW successor 50 (Opus 5.5), D14 / D18.») and D19 (NOW
  roster «D14/D18/D19»). The freeze was a Lead brief (packet l. 2-3: «Lead brief BOX 154, 2026-11-04 01:56Z:», quoting «make it
  landable. Freeze packet P-IDEAL-CUBE for both» «referees»), not a DECISIONS entry; L47 names P-IDEAL-RED only (DECISIONS l. 415-416).
  D18's «Clearly distinguish proven results from conjectures and open problems.» (DECISIONS l. 333): the packet labels PROVED / DATA /
  READING (l. 4-5), and §5 is «DATA / READING (not to sign)» (l. 14).
- G-9, STALE LANE TEXT (notes; nothing here lands). (i) The frozen packet still reads «RESULTS R105 when landed» (l. 19, 20), «R105
  when» «landed» (l. 30-31) and «(signed; R105 when landed)» (l. 66); R105 landed at 91c1464f (2026-11-04T02:59:26Z), after the freeze
  (d97555d4, 01:59:51Z); L-2 reads «RESULTS R105» (fixes l. 21). (ii) Packet l. 19-20 lists «Lemma LOCAL (b) and» «(c)», (c) unused
  (G-4). (iii) Packet l. 30-31 is superseded by fixes entry 1. (iv) Packet l. 3 «Written 2026-11-04 (date -u: see the commit).»: the
  freeze commit d97555d4 has committer and author date 2026-11-04T01:59:51Z. (v) Packet l. 38 «Opened (ar5iv HTML, 2026-11-04)» and
  notes l. 26 (HTML text extraction); both referees read the v1 LaTeX source (REFEREE §1 l. 29; REFEREE-2 §0 l. 12-13), «Verbatim,
  modulo LaTeX rendering» (REFEREE l. 36). (vi) The fixes header (l. 3) «Both SIGN all 4 statements» counts DECOMP as one statement;
  REFEREE-2's table has seven SIGN rows (DECOMP (o), (a), (b), (c) split). (vii) Packet l. 181-182 READING cites «(L-RED R201)», an
  L-RED box, as the open question; READING only. (viii) notes/L-NEW.md l. 61 (box 153, 43125a61): «DEAD: Xi-side-only route (2-wide
  Xi-ladder LP 8/22/52/114, K = 2..5).», a lane DEAD on DATA before the packet; superseded by Theorem LADDER-LP (the packet's §4 family
  L_K, not box 153's climbed ladder).
- G-10, SHA1 PINS IN check.sh (the C110 F-1 class; C116 G-3 recommendation TAKEN). experiments/new/check.sh at d97555d4 (853 lines) had
  no pin; abe2b94c (860 lines; commit «check.sh pins P-IDEAL-CUBE sha1s (CHECKER C116 G-3)») added a pin block for the packet and L-1;
  a0bb2694 (860 lines) extends it to L-2 and the fixes (l. 853-859: «P-IDEAL-CUBE pins (packet 366afedc, line L-1 99ae8fac, line L-2
  449421e4, fixes 006274ec): PASS»). Re-run at this fill from the archive of a0bb2694: PASS ((10)). Blocks w102 (l. 841-846) and w103
  (l. 847-852) are byte-equal at d97555d4, abe2b94c and a0bb2694 (sha1 of l. 841-852: 06d53a5250bddc7627fd5cafb287ae18cfe48795 at each).
- G-11, EXTERNAL SOURCE [WW22] (CLAUDE.md «Every cited result has an opened source»; note). S. Weber, J. Widmer, «Realizability Makes a
  Difference: A Complexity Gap for Sink-Finding in USOs», arXiv:2207.05985 (packet l. 37). Only definitions are used: Def. 4 (USO;
  D-USO), the §2.2 sentence on combed faces (D-DEC drops «not influenced by any other dimension», packet l. 54-56), Def. 3 (orientation,
  DECOMP (o)); the remark after Thm 18 is quoted only for the word «decomposable». Both referees opened the source themselves: REFEREE
  §1 l. 27-44 (abs page: only v1; LaTeX e-print main.tex; numbering on one shared counter; «The packet's numbers are CORRECT.»; each
  quote «EQUAL»; «No theorem of [WW22] is a premise.»); REFEREE-2 §0 l. 11-28 (v1 e-print tarball sha256 88e1f1b7…; «**Every quote is
  verbatim**, with LaTeX math rendered»; «Only definitions are used. No [WW22] theorem is a premise (Thm 18 is quoted only for the word
  «decomposable»). ✓»). L-2 cites «arXiv:2207.05985v1, Def. 4» and «§2.2 of that paper» (CUBE-L2 = LC-P3). I did NOT open [WW22] (not
  verified by me; Addendum (8)); the lane's notebook records it under «Sources opened (box 153)» (notes l. 62-64).
- CLEAN AT L-2 (the pre-check against CHECKER's recurring items, by script on 449421e4):
  C106 E-1 (old line as current): the title is L-2; L-1 occurs in the body only in «at L-1» sentences and in the line history.
  C113 E-1 (title «verbatim» after an insertion): no insertion; the title is byte-equal to prefix + L-2 + fill (Addendum (2)).
  C113 E-2 (trunk status that goes stale): the body has no trunk statement (header).
  C114 Add. 1 E-1 (UPDATE date): <DATE> placeholder.
  C115 E-1 (a premise route RESULTS records as not established): G-4 (R104's definition and R105's ENC, LOCAL (b) are landed text).
  C110 F-1 / C116 G-3 (pins): G-10 (pins present and PASS).
  C111 E-1 (stale Lead-reading statements): G-8.
  C116 G-2 (name clash): G-3, one body sentence.
  «|»: 0 in L-2, 0 in the entry block, 0 in the UPDATE, 0 in the proposed DE36 row (by script, Addendum (3)).
(0) PLACEMENT. R106 goes DIRECTLY AFTER R105 and BEFORE «**Erratum E-1**». docs/RESULTS.md at local trunk 58198d07 (= origin trunk
8b31b166 for this file) has sha1 8309502865f8caa43403f415a5e0dd757a0c0ad1, 10,934 lines, last changed by 91c1464f (R105's landing). «###
R105» is l. 10155 (entry l. 10155-10399, l. 10400 blank); «**Erratum E-1**» is l. 10401; «## Dead ends (kept;» is l. 10414; the last row
DE35 ends at l. 10934, the last line of the file. PROPOSED (R102's to R105's layout): insert R106's entry after l. 10400 (R105's blank
line) and before «**Erratum E-1**», with one blank line after it, so the R-entries stay contiguous and the erratum closes the Results
section. The erratum's line references (l. 7963-9195) lie before the insertion and do not move. "### R106" occurs 0 times in RESULTS and
GAPS, «R106» 2 times (G-3 (a)). GAPS has sha1 bc53d0789e3528366ebc9bc9e10b04f1a114639a, 23 lines, last changed by 91c1464f. The Lead
re-checks (6) and (9) at landing only if RESULTS or GAPS change after 91c1464f.
(1) TITLE. The title is the line file docs/new/P-IDEAL-CUBE-line-L2.txt (l-new a0bb269499779a9dd766b6fe504f0fc6166d0b31,
2026-11-04T03:42:52Z, the file's only commit, sha1 449421e4cfaedbef577f68720fab4924111cd170; identical at the l-new head, which is
a0bb2694 itself), verbatim: one line, no outer quotes, no final period, 2,733 characters (2,801 bytes plus the newline), 511 whitespace
tokens, 39 / 39 parentheses (depth never negative), one «…» (L-2's own, in «i = 0, …, K − 1»). NO HEADING MARKER, verified by script:
the file begins «In the IDEAL model of RESULTS R104», with no «#» at its start, no "R??" and no lane tag (L41 «Lanes write line files
without a heading marker»). NOTHING is stripped and NOTHING is inserted: the heading is the level-3 marker, then "R106 [refereed-only]
", then the file without its newline, then the fill ", CHECKER PASS (docs/checker/C117.md, checker PENDING)" (as R90-R105, no space
before the comma; C117 is the next CHECKER file, NOW roster «C117 = R106 (P-IDEAL-CUBE) when the draft is routed»). L-2 holds one « — »,
its own date parenthesis «(2026-11-04)» and no "|" (G-1). Built by script (scratch fill106.py: assert the sha1 449421e4…, equality with
the blob at a0bb2694 and at the l-new head, one line, no marker, one « (2026-11-04) — », no "|"; prepend, append) and re-checked after
writing this file: equal, byte for byte. Heading: 2,812 characters, 2,880 bytes; sha1 of the heading line without its newline
f690eeed485ff523f320a4774357d938721fd2cc; it is l. 350 and the only «### R» line of this file.
(2) LINE HISTORY: L-1 99ae8face50615b4ce1ce5cd5e69f223f17208e1 (docs/new/P-IDEAL-CUBE-line-L1.txt, d97555d4, 2026-11-04T01:59:51Z,
frozen with the packet; 2,715 bytes, 497 tokens; REFEREE «NOT YET» (CUBE-L1), REFEREE-2 «does NOT match yet» (LC-1, LC-2)) → L-2
449421e4 (a0bb2694, 03:42:52Z; 2,802 bytes, 511 tokens; fixes entry 2). Each line file has one commit. L-1 → L-2 (scratch wdiff106.py,
output wdiff106.out): difflib over whitespace tokens, 8 non-equal opcodes, 476 tokens in common; L-1 with entry 2's changes as six
replacements (each old phrase found once, with its context) equals L-2: True. The eight hunks (fixes l. 23-30): (1) «(c), signed,»
deleted after «Lemma LOCAL (b),» (LC-P2: LOCAL (c) unused); (2) «R105 when landed;» → «R105; π a topological order of the Ξ-graph;»
(R105 landed; LC-P1, π bound at first use); (3) «arXiv:2207.05985,» → «arXiv:2207.05985v1,» (CUBE-L2 = LC-P3); (4) «(π a topological
order of the Ξ-graph)» deleted at the comb clause (LC-P1, moved to (2)); (5) «(all movers of degree 2, distinct gate indices)» inserted
after «L_K» (CUBE-L3); (6), (7) «bound, and the W-key rule must carry any such bound;» → «bound (READING: a polynomial bound on T must
use the W-key rule);» (REQUIRED CUBE-L1 = LC-2); (8) «with gate indices increasing in the option index,» inserted (REQUIRED LC-1). =
REFEREE §C l. 154-155 «Entry 2 against my own word diff (split on blanks, diff) of L-1 → L-2: exactly 8 hunks, equal to entry 2's list,
and nothing else» «differs.»; = REFEREE-2 L2 l. 14 «difflib gives 8 hunks. Byte test: L-1 with exactly the 6 replacements below, each
old phrase occurring once, equals L-2: **True**.», l. 25 «Nothing else differs. Entry 2's hunk list agrees with mine.» No signed
statement differs between L-1 and L-2: every change edits the premise list (LOCAL (c) dropped, R105 landed, π bound earlier), the source
version, L_K's completeness, the READING label or the DATA clause's gate order.
(3) THE LINE AT BOTH REFEREES. L-2 (the title): REFEREE successor 23, docs/referee/R-P-IDEAL-CUBE.md «## §C (2026-11-04T04:16Z by date
-u, successor 23; Opus 5.5, D15): fixes entries 1-2 and line L-2» l. 142-174 (3c3185d8, 2026-11-04T04:16:05Z, +34; the file now 174
lines, sha1 b4f1d9e5842c1de3edfeedfd23348aa506e828e2; l. 1-140 unchanged from 5ef7bf47, byte prefix): l. 174 «VERDICT: line L-2 MATCHES.
All 4 statements stay SIGNED, and entry 1 changes no proof.» REFEREE-2 successor 26, docs/referee-2/R2-P-IDEAL-CUBE-L2.md (993c1710,
2026-11-04T04:17:33Z, new file, 43 lines, sha1 2746d78b0bbb26d41be12c0e4f1dc9c05a5a985c): l. 2 «Verdict: **MATCHES**.», l. 35
«**MATCHES.**», l. 36 «L-2 (449421e4) = L-1 + the two REQUIRED changes (LC-1, LC-2) + the optional LC-P1 to LC-P3, CUBE-L3 and the R105
citation.», l. 37 «Every clause is a signed statement with its exact hypotheses: acyclic, degree ≤ 2.» At L-1: REFEREE report (5ef7bf47,
02:49:13Z, new file, 140 lines, sha1 64a1aa4ff476b00d75617f00129d4426bb8d9b10) l. 127 «VERDICT: line L-1 NOT YET. It matches once
CUBE-L1 is applied.»; REFEREE-2 R2-P-IDEAL-CUBE.md (0787732b, 02:52:00Z, new file, 160 lines, sha1
8c6f69f5162d21bc5838ce46882fd9a80a646e99) l. 50 «**does NOT match yet**: REQUIRED LC-1, LC-2 (§5)». Both MATCH L-2.
LINE-ITEM NAMES: REFEREE CUBE-L1 (READING stated as a statement, REQUIRED), CUBE-L2 (version, optional), CUBE-L3 (L_K complete,
optional), CUBE-P1 (landing after R105: a landing condition, not a line change, l. 127-128); REFEREE-2 LC-1 (gate order of the DATA
clause, REQUIRED), LC-2 (= CUBE-L1, REQUIRED), LC-P1 (π at first use), LC-P2 (drop LOCAL (c)), LC-P3 (= CUBE-L2), P-1 (packet precision,
§0). Entry 2 «Taken: 1 (READING stated as a reading), 2 (DATA with the packet's gate order: gate indices increasing in the option index,
as in» «box154/ladder.py g(x, k) = 2x + k), 3 (arXiv:2207.05985v1), 4 (L_K: all movers of degree 2, distinct gate indices), 5 (π bound»
«at first use, in the premises list), 6 (LOCAL (c) dropped: unused; only LOCAL (b) is used).» (fixes l. 18-20). All REQUIRED items and
all optional line items are in L-2.
(4) CLAIMS SIGNED = the four statements below (DECOMP with its parts (o)-(c)), each SIGN in BOTH referees' verdict tables (REFEREE "##
0. Verdicts" l. 8-17 of R-P-IDEAL-CUBE.md at 5ef7bf47; REFEREE-2 "## 1. Verdict table" l. 38-50 of R2-P-IDEAL-CUBE.md at 0787732b),
checked clause by clause against the packet and its fixes; the cells are the reports' words:
| item (packet §, lines) | REFEREE (successor 23) | REFEREE-2 (successor 26) |
| --- | --- | --- |
| §1 definitions D-ORI, D-USO, D-COMB, D-DEC and the [WW22] quotes (l. 36-57) | l. 11 «quotes VERBATIM (v1); definitions faithful»; §1 l. 26-44 | l. 41 «✓ (quotes verbatim against v1; D-DEC is the packet's own)»; §0 l. 11-28 |
| (a) Lemma DECOMP (o), (a), (b), (c) (§2, l. 59-80) | l. 12 «SIGN»; §3 l. 57-65 | l. 42-45 «**SIGN**» (four rows); §2 l. 58-69 |
| (b) Lemma MULTI→SINGLE (§3, l. 83-89) | l. 13 «SIGN»; §3 l. 66-67 | l. 46 «**SIGN**»; §2 l. 70-74 |
| (c) Corollary T ≤ LP (§3, l. 90-93) | l. 14 «SIGN»; §3 l. 68 | l. 47 «**SIGN**»; §2 l. 75-76 |
| (d) Theorem LADDER-LP with Facts F0-F4 and Claim UP(i) (§4, l. 95-158) | l. 15 «SIGN»; §3 l. 69-82 | l. 48 «**SIGN**»; §2 l. 77-90 |
Both, verbatim: REFEREE FINDINGS l. 137 «DECOMP, MULTI→SINGLE, T ≤ LP and LADDER-LP are SIGNED, with no proof gap.»; REFEREE-2 l. 52 «No
gap in the mathematics. Packet precision P-1 (§2).», FINDINGS l. 156 «No mathematical gap.»
AFTER THE FIXES: REFEREE §C (3c3185d8) l. 150 «Entry 1 (REFEREE-2 P-1, §0 «faces never tie»): CORRECT.», l. 174 «All 4 statements stay
SIGNED, and entry 1 changes no proof.»; REFEREE-2 L2 (993c1710) l. 29 «## 2. Fixes entry 1 (my P-1) ✓», l. 32 «That is exactly the
correction I asked for. «No proof in the packet changes» is correct.»
Clause checks (L-2 against the packet and its fixes): the setting parenthesis = §0 l. 26-34 (D2 l. 29, C_s(x) l. 30-31 as fixed by entry
1, Q_G l. 33, π l. 28) and D-ORI l. 49-50; DECOMP = §2 l. 61-64 ((a) with D-USO = [WW22] Def. 4, l. 42-43 and 51; (b) with E(b) of l.
74; (c) with D-COMB l. 52-53 and D-DEC l. 54); MULTI→SINGLE = l. 83-85; T ≤ LP = l. 90 with LP_G of l. 57; LADDER-LP = L_K of l. 96-107
(N = 2K at level 0, degree 2, l. 96; targets l. 98-99; even parities l. 100; rank blocks l. 101-104; gates «any distinct values» l. 105;
start l. 106) and the bound of l. 108-109; «T ≤ LP cannot by itself give a polynomial bound» = (c) + (d) (G-6). Nothing in L-2 is wider
than signed (REFEREE §C l. 171 «The hypotheses are exact: acyclic, degree ≤ 2.»; REFEREE-2 L2 l. 37).
Signed by both, NOT stated by L-2 as separate items: DECOMP (o) (presupposed by o_G's definition, G-2 (v)); Facts F0-F4 and Claim UP(i)
(proof steps of LADDER-LP); the definitions D-ORI to D-DEC (stated in L-2 through their glosses). Not signed, so NOT landed: packet §5
(machine check, «does NOT claim», READING, TARGET diff; «DATA / READING (not to sign)», l. 14); fixes entry 1 as text (a definition
precision, «No proof in the packet changes»).
(5) OTHER TEXTS THE ENTRY DEPENDS ON: RESULTS R104's definition of the IDEAL model (title l. 9864; no R104 theorem); RESULTS R105's
Lemma ENC and Lemma LOCAL (b) with P-IDEAL-RED §0's notation (R105 title l. 10155; body Setting l. 10193, (a) l. 10211, (b) l. 10214);
[WW22] v1's definitions (G-11). Nothing else. The lane source docs/new/N5-CUBE-box153.md (box 153, 43125a61; packet l. 4 «this packet
governs») and box 155 (abe2b94c; notes l. 14) are history only; no lane file and no lit note is a premise (G-4).
(6) PREMISE LABELS (stale-label test; RESULTS at 91c1464f's version, GAPS likewise). RESULTS labels in L-2 (by script): «R104» 2
(«RESULTS R104», «R104's definition»); «R105» 1 («RESULTS R105»); «R178» 1, an L-RED box label, prefixed («L-RED R178 §1»). R104 (l.
9864) exists and carries the definition (Ξ-targets, β-ranks with parities, distinct gate indices, levels, the step rule, the Ξ-graph).
R105 (l. 10155) exists and carries ENC and LOCAL (title; body (a), (b)); R105's own premise is R104's definition only. No Lead reading
and no other RESULTS label is cited. No label is retired by a later entry. G-N5-TIME open (GAPS l. 11).
(7) SYMBOL TEST of the title (my own strict test of every symbol of L-2; IN = bound in the line; else the carrier):
| symbol | where |
| --- | --- |
| IDEAL model, Ξ-graph, acyclic, mover, level, option, β, rank, parity, Ξ-target, exit, gate index, state, step, IDEAL run, start | RESULTS R104 (the premise) |
| Lemma ENC, Lemma LOCAL (b), T, Ξ-value, strictly better | RESULTS R105 / P-IDEAL-RED §0 (the premise; G-2 (i)) |
| π, D2, Q_G, C_s(x), o_G, b ⊕ e_x | IN (the premise parenthesis) |
| unique sink orientation, face, sink, combed, decomposable | IN (glossed) and [WW22] v1 Def. 4, §2.2 (G-11) |
| Mv_t, LP_G(s_0), L_K, K, N = 2K, u_i, v_i, pairs | IN |
| C_b(x), b, [·], e_x, # | not glossed (G-2 (ii)-(iv), (vii); packet l. 33-34, 74) |
| LP (bare, in «so LP ≥ …») | LP_G at L_K's start (G-2 (vi)) |
| L-RED R178 §1 | attribution, prefixed |
| READING clause | READING, labelled |
| DATA clauses: gate order and the empty run; decomp.py, 25 corpus genomes, 478,953 faces; ladder.py K = 1..10, K ≤ 7 | DATA, cited |
Agreeing tests: REFEREE §6 l. 104-128 (L-1) and §C l. 169-173 (L-2); REFEREE-2 §5 l. 122-147 (L-1) and L2 §1 (l. 13-27).
(8) FIXES AND STATUS NOTES (docs/new/P-IDEAL-CUBE-fixes.md, L-NEW successor 50, append-only, two entries, one commit): at a0bb2694 sha1
006274ec3f0aa82ceac8fa9b8f294f1f8d2e138e, 30 lines (both referees checked this version: REFEREE §C l. 145
«docs/new/P-IDEAL-CUBE-fixes.md: sha1 006274ec…, 30 lines;»; REFEREE-2 L2 l. 9 «fixes 006274ec3f0aa82ceac8fa9b8f294f1f8d2e138e (30
lines).»). Header (l. 2-4): «Packet docs/new/P-IDEAL-CUBE.md at d97555d4 (sha1 366afedcf7cd04a31302e25cec47c7fb3df455bb,» «186 lines),
NOT edited. Referees: REFEREE 23 5ef7bf47, REFEREE-2 26 0787732b. Both SIGN all 4 statements, no math gap.»
Entry 1 (l. 6-15, «packet precision, REFEREE-2 P-1; optional, taken»): §0's «Two faces never tie» sentence (packet l. 30-31) replaced by
«Two faces never tie: face k's β-set contains β(x, k) and» «not β(x, 1 − k), because by acyclicity neither chain returns to x, so the
two β-sets differ; ENC (P-IDEAL-RED, RESULTS R105) then» «makes them unequal in the order.» (l. 11-13). Entry 2 (l. 17-30): L-2 and its
eight-hunk word diff ((2)). No fix changes a signed statement.
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-2 states no CONJECTURE and kills nothing of RESULTS or GAPS. A line-11 UPDATE is proposed
at the end, to go AFTER R105's UPDATE (GAPS at 91c1464f: the last UPDATE on l. 11 is R105's «UPDATE 2026-11-04 02:59Z: RESULTS R105
(P-IDEAL-RED; CHECKER C116 e85c3bb2) [refereed-only] LANDED: …», ending «G-N5-TIME stays open.» before the row's closing « |»; l. 11
holds 76 "|" and 40 «UPDATE 2026-»), as a pure insertion with one separating space. BUILT FROM L-2 (scratch upd106.py: upd105.py's
controls and upd100L3.py's build() unchanged; R105's sentinel procedure as a function, unchanged). CONTROLS (same script, same run, rc
0): R97's to R105's LANDED UPDATEs (GAPS l. 11 at 91c1464f) rebuilt from their lines byte for byte (True ×9; R105's from P-IDEAL-RED L-2
at ffeb9736 with head «UPDATE 2026-11-04 02:59Z: RESULTS R105 (P-IDEAL-RED; CHECKER C116 e85c3bb2) [refereed-only] », 3,807 bytes, also
equal to R105-draft l. 600 with <DATE> 2026-11-04, <HH:MM> 02:59, <checker> e85c3bb2). R106: the R105 procedure unchanged (C116 G-1
«PASS» on that rule: «the stamp head», «each of the 16 labels moved behind its clause», « (2026-11-03) — » → «: », the two scope
sentences dropped, «(DATA: …)» opened, «the source parenthesis kept», «. G-N5-TIME stays open.» appended): build()'s label move on the
claim body plus a sentinel tail, with start «for every genome G: » (3 labels, each found once after it, in order); « (2026-11-04) — » →
«: »; the DATA parenthesis before the source parenthesis opened as «; DATA: …»; «; G-N5-TIME stays OPEN» and «; not M3, not a step-4
pass, not a TARGET.md claim» dropped; the source parenthesis kept; «. G-N5-TIME stays open.» appended. The READING parenthesis and the
inner DATA parenthesis («(DATA: on L_K …)») stay as they are (only the last DATA parenthesis before the source is opened, as for R105).
L-2 holds no "|", so no replacement list. Checked by script: one line, 0 "|", one «<DATE>», one «<HH:MM>», one «<checker>», 2,835 bytes,
510 tokens; «2026-11-04» 0 times (the date parenthesis is dropped by the rule). Head «UPDATE <DATE> <HH:MM>Z: RESULTS R106
(P-IDEAL-CUBE; CHECKER C117 <checker>) [refereed-only] » («P-IDEAL-CUBE» 0 times in GAPS and RESULTS); <DATE> = the landing date.
(10) DATA of record = packet §5 (l. 161-172), NOT signed; L-2's DATA parentheses state its counts. Re-run at this fill (scratch, git
archive of a0bb2694's experiments/new and docs/new; box150/, box153/, box154/ and the box14* / box152 inputs have no diff between
d97555d4 and a0bb2694, by git diff --stat; from experiments/new, as check.sh's «cd ..»), 2026-11-04T04:46:17Z-04:46:47Z, rc 0, outputs
w102.out, w103.out, blocks.out:
- w102: «DECOMP genomes 25 faces 478953 USO 0 COMB 0 ORDER 0 ACYC 0 JUMP 0 maxjump 7» and «LONGPATH ladlp_5.json n2 10 longest 114
  ideal_T 1»: byte-equal to the block's two grep -qxF strings (l. 842). The corpus glob expands to 48 files; decomp.py keeps the 25 with
  degree ≤ 2 and 1 to NMAX = 10 degree-2 movers.
- w103: ten lines ending « OK» (K = 1..10, paths 2, 6, 14, 30, 62, 126, 254, 510, 1022, 2046 = 2^(K+1) − 2, «nonimproving 0», flips [2,
  4, …, 2^K], «ideal_T 0»; DP_longest 2, 6, 14, 30, 62, 126, 254 for K ≤ 7, «None» for K ≥ 8), and the K = 7 line contains the block's
  grep -qF string «LADDER K 7 N 14 path 254 = 2^(K+1)-2 True nonimproving 0 flips [2, 4, 8, 16, 32, 64, 128] DP_longest 254 ideal_T 0
  OK».
- The three blocks run as written (l. 841-859, inside a shell with check.sh's «set -euo pipefail» and «cd»): «box 153 DECOMP:
  improvement orientation is a decomposable AUSO (0 violations); Xi-ladder K 5 longest improving path 114: PASS», «box 154 LADDER-LP:
  Xi-ladder L_K has a directed improving path of length 2^(K+1)-2 (K = 1..10; DP exact K <= 7): PASS», «P-IDEAL-CUBE pins (packet
  366afedc, line L-1 99ae8fac, line L-2 449421e4, fixes 006274ec): PASS».
- Own gate-order probe (scratch gateT106.py, ladder.py's genome(K) and box150's simulator, so NOT independent of the lane's code;
  2026-11-04T04:51:46Z, rc 0, gateT106.out): T = 0 with gates 2x + k (increasing in k) and T = 1 with gates 2x + 1 − k (decreasing), K =
  1..10 (= REFEREE cube_gateT.txt for K = 1..7 and REFEREE-2 §3 l. 113-114 for K = 1..5).
NOT re-run: box153/longpath.py on the corpus (packet l. 171 «x3_L8: LP 16 vs T 8; dc_d8: 64 vs 23»); box 153's 119-genome run (603,741
faces, l. 163-164); the referees' tools (docs/referee/scratch/cube_probe.py; docs/referee-2/R2-P-IDEAL-CUBE/cube_check.py); I read their
committed logs (REFEREE cube_probe.txt at 5ef7bf47, cube_gateT.txt at 3c3185d8; REFEREE-2 run1.log and control.log at 0787732b) and they
equal the reports' numbers (Data in the body). check.sh's other blocks and scripts/verify.sh: not run.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 the source note names no fixes file (G-1). D-2 REFEREE §2 l. 52
«L-RED R178 and R201 appear only in attributions and the READING»: the packet has «R178» 0 times (it is in L-1 and L-2 only, as an
attribution) and «R201» once (l. 182, READING). D-3 REFEREE's CUBE-L1 proposed «a bound on LP alone cannot give a polynomial bound on T
(READING: a polynomial bound on IDEAL runs must use the W-key rule)» (l. 121-122); L-2 took REFEREE-2's LC-2 wording («T ≤ LP cannot by
itself give a polynomial bound (READING: a polynomial bound on T must use the W-key rule);», §5 l. 141); REFEREE §C l. 161 «my CUBE-L1
is MET». D-4 neither gate-order probe's code is committed: REFEREE's output is (cube_gateT.txt, K = 1..7); REFEREE-2's decreasing-gate
probe (K = 1..5) has no committed log (cube_check.py builds increasing gates only, l. 109); my probe is in scratch ((10)). D-5 REFEREE
l. 18-19 «RESULTS has no R105 at trunk bf60f418»: true at 02:49 (R105 landed at 02:59:26Z); superseded by §C l. 148-149. D-6 the corpus
counts differ by filter: decomp.py 25 genomes with ≤ 10 degree-2 movers (478,953 faces); REFEREE-2 18 genomes with ≤ 9 degree-2 movers
(62,730 faces of dimension ≥ 1; «30 files skipped as degree 3 or larger», table l. 107); REFEREE 400 random genomes only (95,136 faces).
D-7 ladder.py's OK test checks «lp is None or lp >= n» (DP ≥ path), not equality; the printed DP values equal 2^(K+1) − 2 for K ≤ 7 (my
re-run), as packet l. 170 says, and check.sh tests the K = 7 line verbatim only. D-8 the fixes header (l. 3) «Both SIGN all 4
statements» vs REFEREE-2's seven SIGN rows (G-9 (vi)). D-9 REFEREE-2 l. 4 «A names-only `git ls-tree` on origin/claude/referee found 0
files matching «cube» at 02:50Z.», while REFEREE's report commit 5ef7bf47 has committer time 02:49:13Z; a commit time is not a push time
(push.sh runs verify first), so both can be true; not verifiable from the repository. D-10 the packet's quotes were taken from ar5iv
HTML (l. 38), the referees' checks from the v1 LaTeX source (G-9 (v)); both «verbatim» findings are «modulo LaTeX rendering».
(12) Excluded: packet §5 (DATA, «does NOT claim», READING, TARGET diff); box153/longpath.py's corpus LP figures and the climbed 2-wide
Ξ-ladder ladlp_5.json (LP 114 at N = 10), DATA only; docs/new/N5-CUBE-box153.md (lane source; its [MC94] reading, notes l. 65-67,
«nothing imported»); box 155 (gate.py exact W-side search, Lemma MULTI-CHARGE and SINGLE-SHORT; lane-level, unreviewed; abe2b94c, notes
l. 14-15); every «Does NOT claim» item of the packet (l. 79-80, 93, 155-158, 173-178); any theorem of [WW22]; fixes entry 1 as a
statement; the referees' tools. Not part of this entry.
(13) Commits: lane (claude/l-new): 43125a61 (2026-11-04T00:54:56Z; box 153, the source: N5-CUBE-box153.md, box153/decomp.py,
longpath.py, ladlp.py, ladlp_5.json, check.sh block w102) → d97555d4 (01:59:51Z; freeze: packet +186, L-1 +1, box154/ladder.py +58,
check.sh block w103 +6, notebook +5) → abe2b94c (02:48:38Z; check.sh pin block for packet and L-1 +7; box 155 tools) → a0bb2694
(03:42:52Z; fixes +30, L-2 +1, pin block extended to L-2 and fixes). REFEREE (claude/referee): 5ef7bf47 (02:49:13Z; report, new file 140
lines, sha1 64a1aa4f…; scratch/cube_probe.py, xinew_logs/cube_probe.txt) → 3c3185d8 (04:16:05Z; §C, +34; 174 lines, sha1 b4f1d9e5…;
xinew_logs/cube_gateT.txt). REFEREE-2 (claude/referee-2): 0787732b (02:52:00Z; report, new file 160 lines, sha1 8c6f69f5…;
R2-P-IDEAL-CUBE/cube_check.py, logs/) → 993c1710 (04:17:33Z; R2-P-IDEAL-CUBE-L2.md, new file 43 lines, sha1 2746d78b…; handover).
R2-P-IDEAL-CUBE.md is unchanged at 993c1710 (sha1 8c6f69f5…, by cmp). CHECKER: C116 e85c3bb2 (R105 PASS), C116 Add. 1 49f85ffc (R105
landed 91c1464f PASS); none yet for R106 (C117). Trunk: see the header.
(14) Placement: see (0). DEAD-ENDS ROW: PROPOSED (DE36, drafted after the UPDATE below; the Lead decides). Unlike R105 (C116 G-4: «The
only refuted form is the lane's own «any degree» over-statement»; no row), this entry kills a proof route by a refereed theorem with an
explicit family: «T ≤ LP cannot by itself give a polynomial bound» (L-2, signed; G-6) is the statement that bounding LP_G(s_0)
polynomially, and with it T through Corollary T ≤ LP, is impossible on degree-≤-2 IDEAL-ACYC genomes, since Theorem LADDER-LP gives LP ≥
2^(N/2+1) − 2 on L_K. WHY A ROW (proposal): (a) the Dead-ends heading asks for «the exact obstruction or counterexample and the instance
that killed it» (RESULTS l. 10414): the counterexample is the family L_K, explicit in the signed statement (packet l. 96-107), built by
experiments/new/box154/ladder.py (gates 2x + k) and machine-checked for K = 1..10 (DP-exact K ≤ 7; REFEREE-2 K = 1..12, DP-exact K ≤ 8;
REFEREE DP-exact K ≤ 6); the obstruction is the proof's own mechanism (Claim UP(i): every change of B_(i−1) makes both movers of pair i
improving, and each of their two switches changes B_i, so pair i is re-armed twice per change below it); (b) L43's condition for «DEAD»
holds (a refereed proof; REFEREE-2 §4 l. 118 «L43 is satisfied.»); (c) CLAUDE.md «Record every dead end with the exact obstruction and
the instance that killed it.»; the lane recorded the route as DEAD in its READING (packet l. 181) and its notebook (l. 61, box 153, on
DATA), but no RESULTS row exists; (d) precedent for a route row: DE27 («the k-pools attack on (NEST*-BOUNDED) … is CLOSED»), DE21 («the
R12 (c) route with D ≤ 3 and the R13 (c) route with c = 2 are dead on data»). AGAINST (for the Lead): no conjecture of RESULTS or GAPS
is killed («bound LP» was never a fleet conjecture: «LP_G», «L_K» and «LADDER» occur 0 times in RESULTS and GAPS, G-3); the entry itself
records the obstruction; R103 / R104 / R105 had no row (C116 G-4). The row must NOT say that a bound on T «must use the W-key rule»
(READING only, CUBE-L1 / LC-2), and must keep IDEAL-ACYC-POLY and G-N5-TIME open. Its date is the landing date (<DATE>); it goes after
DE35 (RESULTS l. 10934, the file's last line; after R106's insertion it is still the last row).
### R106 [refereed-only] In the IDEAL model of RESULTS R104 (the model first stated in L-RED R178 §1), on acyclic Ξ-graphs, at degree ≤ 2 (premises: R104's definition of the model, and P-IDEAL-RED's Lemma ENC and Lemma LOCAL (b), RESULTS R105; π a topological order of the Ξ-graph; D2 the movers with two options; the improvement cube Q_G = {0, 1}^D2 of states; C_s(x) the option of x with the strictly better Ξ-value at s; the improvement orientation o_G directs the edge between b and b ⊕ e_x away from the endpoint whose x-coordinate differs from C_b(x)), for every genome G: (DECOMP) o_G is a unique sink orientation in the sense of Weber and Widmer, arXiv:2207.05985v1, Def. 4 (every non-empty face has exactly one sink); it is acyclic (Σ_x [b(x) ≠ C_b(x)] 2^π(x) falls along every edge); and in every face of dimension ≥ 1 the free coordinate of largest π is combed (all its edges in that face point the same way), so o_G is decomposable (every face combed, as in §2.2 of that paper); (MULTI→SINGLE) every step of an IDEAL run that moves the set Mv_t is the directed path of o_G that switches the movers of Mv_t one at a time in increasing π, so T ≤ Σ_t #Mv_t ≤ LP_G(s_0), the largest length of a directed path of o_G from the start; and (LADDER-LP) for every K ≥ 1 the explicit genome L_K (all movers of degree 2, distinct gate indices) with N = 2K level-0 movers in pairs (u_i, v_i), i = 0, …, K − 1, where both options of u_0 and v_0 go to the exit, option 0 (option 1) of u_i and v_i goes to u_(i−1) (v_(i−1)) for i ≥ 1, all parities are even, every rank of pair i − 1 is above every rank of pair i, the ranks within pair 0 increase as β(u_0, 0) < β(v_0, 0) < β(u_0, 1) < β(v_0, 1) and within pair i ≥ 1 as β(u_i, 0) < β(u_i, 1) < β(v_i, 0) < β(v_i, 1), with start u_0, v_0 on option 0 and all other movers on option 1, has a directed path of o_(L_K) of length 2^(K+1) − 2 from that start, so LP ≥ 2^(N/2+1) − 2 (2026-11-04) — a STRUCTURE / REDUCTION statement inside the IDEAL model, together with an exponential lower bound for LP, not for IDEAL runs: T ≤ LP cannot by itself give a polynomial bound (READING: a polynomial bound on T must use the W-key rule); nothing is said about real IDEAL runs beyond T ≤ LP (DATA: on L_K with gate indices increasing in the option index, the IDEAL run from that start is empty); bounds nothing polynomially; Ξ-cyclic genomes and degree ≥ 3 are not covered; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (DATA: experiments/new/box153/decomp.py 0 violations on 25 corpus genomes, 478,953 faces; experiments/new/box154/ladder.py: the path of the proof checked for K = 1..10, and the longest path equals 2^(K+1) − 2 for K ≤ 7) (P-IDEAL-CUBE, docs/new/P-IDEAL-CUBE.md; L-NEW successor 50), CHECKER PASS (docs/checker/C117.md, checker PENDING)
- Object (L-NEW successor 50, Opus 5.5, D14 / D18 / D19; frozen, unchanged during review): packet P-IDEAL-CUBE,
  docs/new/P-IDEAL-CUBE.md, sha1 366afedcf7cd04a31302e25cec47c7fb3df455bb, 186 lines (l-new freeze d97555d4, 2026-11-04T01:59:51Z, the
  file's only commit; identical at abe2b94c and a0bb2694). Both referees measured the sha1 (REFEREE l. 4 «docs/new/P-IDEAL-CUBE.md: sha1
  366afedcf7cd04a31302e25cec47c7fb3df455bb, 186 lines;»; REFEREE-2 §0 l. 8-9 «sha1 366afedcf7cd04a31302e25cec47c7fb3df455bb,» «186
  lines. Re-hashed: match.»). Title (l. 1): «Packet P-IDEAL-CUBE (box 154): the improvement cube of a degree-2 IDEAL-ACYC genome is a
  decomposable acyclic USO (DECOMP); every IDEAL run follows a directed path of it (MULTI→SINGLE, T ≤ LP); and directed paths can be
  exponential: an explicit Ξ-ladder family with LP ≥ 2^(K+1) − 2 = 2^(N/2+1) − 2 (Theorem LADDER-LP)». Status (l. 4-5): «Labels: PROVED
  (L-NEW 50, unrefereed) /» «DATA / READING. Not a TARGET.md claim. No polynomial bound. G-N5-TIME stays OPEN.» To sign: §2 Lemma
  DECOMP, §3 Lemma MULTI→SINGLE and Corollary T ≤ LP, §4 Theorem LADDER-LP, with the §1 definitions (table l. 8-14); §5 «DATA / READING
  (not to sign)». Sections: premises (l. 16-23), §0 setting (l. 25-34), §1 definitions and the [WW22] text (l. 36-57), §2 DECOMP (l.
  59-80), §3 MULTI→SINGLE and T ≤ LP (l. 82-93), §4 LADDER-LP (l. 95-158), §5 machine check, «does NOT claim», READING, TARGET diff (l.
  160-186). Source: «docs/new/N5-CUBE-box153.md (box 153, 43125a61); this packet governs.» (l. 4).
  Fixes: docs/new/P-IDEAL-CUBE-fixes.md, fixes entries 1-2 (append-only; one commit, a0bb2694; 30 lines, sha1
  006274ec3f0aa82ceac8fa9b8f294f1f8d2e138e, the version both referees checked). Entry 1 replaces §0's «faces never tie» sentence (packet
  l. 30-31) by the acyclicity argument, «No proof in the packet changes.» (l. 15); entry 2 is L-2's word diff. The packet read with
  entry 1 is the text of record.
  The RESULTS line is L-2, 449421e4cfaedbef577f68720fab4924111cd170 (docs/new/P-IDEAL-CUBE-line-L2.txt, l-new a0bb2694,
  2026-11-04T03:42:52Z, the file's only commit; fixes entry 2). The title is L-2 verbatim, with nothing inserted (its date parenthesis
  «(2026-11-04)» and its source note are the line's own; the source note names no fixes file). L-2 MATCHES at both referees: REFEREE §C
  (3c3185d8) l. 174 «VERDICT: line L-2 MATCHES. All 4 statements stay SIGNED, and entry 1 changes no proof.»; REFEREE-2
  R2-P-IDEAL-CUBE-L2.md (993c1710) l. 2 «Verdict: **MATCHES**.», l. 37 «Every clause is a signed statement with its exact hypotheses:
  acyclic, degree ≤ 2.»
  L-2 differs from the line at L-1 by exactly the eight hunks of fixes entry 2 (l. 22-30): LOCAL (c) dropped from the premises; «RESULTS
  R105» for «R105 when landed»; π bound in the premise list instead of at the comb clause; «arXiv:2207.05985v1»; «(all movers of degree
  2, distinct gate indices)» for L_K; the READING label on «a polynomial bound on T must use the W-key rule»; the gate order in the DATA
  clause. REFEREE §C l. 154-155: «exactly 8 hunks, equal to entry 2's list, and nothing else» «differs.»; REFEREE-2 L2 l. 36 «L-2
  (449421e4) = L-1 + the two REQUIRED changes (LC-1, LC-2) + the optional LC-P1 to LC-P3, CUBE-L3 and the R105 citation.»
  History. At L-1 (99ae8face50615b4ce1ce5cd5e69f223f17208e1, docs/new/P-IDEAL-CUBE-line-L1.txt, l-new d97555d4, frozen with the packet),
  REFEREE l. 127 «VERDICT: line L-1 NOT YET. It matches once CUBE-L1 is applied.» and REFEREE-2 l. 50 «**does NOT match yet**: REQUIRED
  LC-1, LC-2 (§5)»: at L-1 the clause «the W-key rule must carry any such bound» stated a READING as a statement (REFEREE CUBE-L1 =
  REFEREE-2 LC-2; REFEREE l. 119-120 «is not proved. Which runs the step rule allows without the key is not defined, so» ««must» has no
  signed content.»), and «(DATA: on L_K the IDEAL run from that start is empty)» held only for gates increasing in the option index
  (REFEREE-2 LC-1, l. 135-136). Neither referee found a hole in a proof; the one packet precision is REFEREE-2's P-1 (C_s(x) well
  defined needs acyclicity, §2 l. 55-57), taken as fixes entry 1.
  Setting (packet §0, l. 25-34; RESULTS R104's model in P-IDEAL-RED §0's notation): degree ≤ 2 throughout; «D2 := the movers with two
  options; the others have one option and never move.» (l. 29); C_s(x) (x ∈ D2), the option of x whose Ξ-value is strictly better at s
  (l. 30; well defined by fixes entry 1); «x is improving at s iff s(x) ≠ C_s(x).» (l. 32); the cube Q_G := {0, 1}^D2, a vertex b being
  the state s_b (l. 33-34). D-ORI (l. 49-50): «For x ∈ D2 and b ∈ Q_G, the outmap is o_G(b)_x := 1 if b(x) ≠ C_b(x), else 0.»; D-USO =
  [WW22] Def. 4 (l. 51); D-COMB (l. 52-53): «A dimension x is combed in a face F (free coordinates X_F ∋ x) iff all edges of F in
  dimension x point in the same» «direction.»; D-DEC (l. 54): «An orientation is decomposable iff every face of dimension ≥ 1 has a
  combed dimension.»; LP_G (l. 57): «LP_G(b) := the largest number of edges of a directed path in the orientation starting at b (finite
  by DECOMP (b)).»
- Claims signed (both referees Opus 5.5, D15: REFEREE l. 2 «(Opus 5.5, D15)», REFEREE-2 l. 2 «Opus 5.5 (D15)»; REFEREE successor 23
  (report 5ef7bf47; §C on fixes entries 1-2 and L-2 3c3185d8); REFEREE-2 successor 26 (report 0787732b; R2-P-IDEAL-CUBE-L2.md
  993c1710)). Items (a)-(d) are SIGN in both verdict tables (REFEREE "## 0. Verdicts" l. 8-17 of R-P-IDEAL-CUBE.md; REFEREE-2 "## 1.
  Verdict table" l. 38-50 of R2-P-IDEAL-CUBE.md), and both verdicts stand after the fixes (REFEREE §C l. 174 «All 4 statements stay
  SIGNED, and entry 1 changes no proof.»; REFEREE-2 L2 l. 32 «That is exactly the correction I asked for. «No proof in the packet
  changes» is correct.»); the table is to-check (4). All hold for every IDEAL genome of degree ≤ 2 with an acyclic Ξ-graph (any width,
  any levels, π any topological order); (d) is for the explicit family L_K. No item bounds a count polynomially.
  (a) Lemma DECOMP (§2, l. 59-80; degree ≤ 2, any IDEAL-ACYC genome G, any width, any levels): «(o) o_G is an orientation in the sense
      of [WW22] Def. 3.» «(a) It is a USO (D-USO).» «(b) It is acyclic.» «(c) In every face F of dimension ≥ 1, the free coordinate y of
      largest π is combed. Hence o_G is decomposable (D-DEC).» (l. 61-64); acyclicity through «E(b) := Σ_(x ∈ D2) o_G(b)_x · 2^π(x)» (l.
      74), which falls strictly along every edge. Cells: REFEREE «SIGN» (l. 12; §3 l. 57-65); REFEREE-2 «**SIGN**» for each of (o), (a),
      (b), (c) (l. 42-45; §2 l. 58-69).
  (b) Lemma MULTI→SINGLE (§3, l. 83-89; degree ≤ 2, IDEAL-ACYC): «List Mv_t as» «x_1, …, x_m in increasing π. Let b^0 := s_(t−1) and b^j
      := b^(j−1) ⊕ e_(x_j). Then every edge b^(j−1) → b^j is a directed edge of» «o_G, and b^m = s_t.» (l. 83-85). Cells: REFEREE «SIGN»
      (l. 13; §3 l. 66-67); REFEREE-2 «**SIGN**» (l. 46; §2 l. 70-74).
  (c) Corollary T ≤ LP (§3, l. 90-93): «For every IDEAL run of a degree-≤-2 IDEAL-ACYC genome from s_0:» T is at most the total number
      of moves Σ_t #Mv_t, which is at most LP_G(s_0) (l. 90). Cells: REFEREE «SIGN» (l. 14; §3 l. 68 «The concatenation is a directed
      path from s_0, and LP is finite by (b).»); REFEREE-2 «**SIGN**» (l. 47; §2 l. 75-76).
  (d) Theorem LADDER-LP (§4, l. 95-158, with Facts F0-F4 and Claim UP(i)): the genome L_K (K ≥ 1): «N = 2K movers, all of level 0 (no
      W-targets), all of degree 2.» (l. 96); pairs (u_i, v_i), pair 0 the deepest; both options of u_0 and v_0 to the exit, option 0
      (option 1) of u_i and v_i to u_(i−1) (v_(i−1)) for i ≥ 1 (l. 98-99); all parities even (l. 100); ranks 0, …, 4K − 1, pair 0 the
      top four, every rank of pair i − 1 above every rank of pair i, «β(u_0, 0) < β(v_0, 0) < β(u_0, 1) < β(v_0, 1)» and «β(u_i, 0) <
      β(u_i, 1) < β(v_i, 0) < β(v_i, 1)» (l. 101-104); «Gate indices: any distinct values (W plays no role in this theorem).» (l. 105);
      start b_0 with u_0, v_0 on option 0 and every other mover on option 1 (l. 106). «Theorem LADDER-LP. For every K ≥ 1, o_(L_K) has a
      directed path of length 2^(K+1) − 2 starting at b_0. So» «LP_(L_K)(b_0) ≥ 2^(K+1) − 2 = 2^(N/2+1) − 2.» (l. 108-109). Proof: Claim
      UP(i) makes «exactly 2^(K−i+1) − 2 switches, each along a directed edge of o_(L_K)» (l. 132), by induction on K − 1 − i; the path
      is u_0's switch, UP(1), v_0's switch, UP(1) (UP(1) only if K ≥ 2; l. 148-154). Cells: REFEREE «SIGN» (l. 15; §3 l. 69-82, «I
      checked every fact.»); REFEREE-2 «**SIGN**» (l. 48; §2 l. 77-90, «I checked every fact against the rank layout.»).
  Both, verbatim: REFEREE l. 137 «DECOMP, MULTI→SINGLE, T ≤ LP and LADDER-LP are SIGNED, with no proof gap.»; REFEREE-2 l. 52 «No gap in
  the mathematics. Packet precision P-1 (§2).» The RESULTS line (L-2) states (a)-(d), DECOMP (o) as part of o_G's definition, and the
  consequence «T ≤ LP cannot by itself give a polynomial bound» of (c) and (d) (REFEREE §C l. 162-163), and nothing wider (to check
  (4)); REFEREE-2 L2 l. 37 «Every clause is a signed statement with its exact hypotheses: acyclic, degree ≤ 2.»
- Premise: RESULTS R104's definition of the IDEAL model, and RESULTS R105's Lemma ENC and Lemma LOCAL (b) with P-IDEAL-RED §0's
  notation; [WW22] v1's definitions (no theorem). L-2: «premises: R104's definition of the model, and P-IDEAL-RED's Lemma ENC and Lemma
  LOCAL (b), RESULTS R105». ENC is used once, in §0, to order the two faces of a mover (with acyclicity, fixes entry 1); LOCAL (b) in
  DECOMP (o), (b), (c), MULTI→SINGLE and Fact F1 / F4 (REFEREE §2 l. 49-50). Packet l. 17-23: «LANDED: RESULTS R104 (P-N5-REALIZE), ONLY
  its definition of the IDEAL model, as restated in P-IDEAL-RED §0.»; «External definitions: [WW22] Def. 4 and §2.2, quoted verbatim in
  §1. Only the definitions are used; no theorem of [WW22] is a» «premise.»; «Nothing from docs/lit or docs/sources.» REFEREE §C l.
  148-149 «CUBE-P1 is MET: the premise route is now landed R104 +» «landed R105.»; REFEREE-2 §0 l. 29 «**Premise route ✓, with two
  remarks.**» (LOCAL (c) unused; land after R105), L2 l. 38 «Premises: R104's definition, P-IDEAL-RED ENC and LOCAL (b) (R105, landed),
  and [WW22] v1 definitions.» [WW22] (S. Weber, J. Widmer, arXiv:2207.05985v1) was opened and checked verbatim by both referees: REFEREE
  §1 l. 27-44 («The packet's numbers are CORRECT.», «No theorem of [WW22] is a premise.»); REFEREE-2 §0 l. 11-28 («**Every quote is
  verbatim**, with LaTeX math rendered», «Only definitions are used.»). L-RED R178 is named in L-2 only as the model's first statement,
  an attribution.
- L41 and L43. The proofs are L-NEW successor 50's (packet l. 4-5). Fixes entry 1's sentence is REFEREE-2's P-1, a definition precision
  that changes no proof (fixes l. 15; REFEREE §C l. 153); the line changes LC-1 and LC-2 are wording. Nothing referee-originated is a
  premise or a proof step of the entry (my reading; neither referee mentions L41). No DEAD in L-2 (L43); «T ≤ LP cannot by itself give a
  polynomial bound» rests on a refereed proof with explicit instances (REFEREE-2 §4 l. 117-118 «with a refereed proof. L43 is
  satisfied.»).
- Fixes (docs/new/P-IDEAL-CUBE-fixes.md, L-NEW successor 50, append-only, fixes entries 1-2; a0bb2694, 30 lines, sha1
  006274ec3f0aa82ceac8fa9b8f294f1f8d2e138e, the version both referees checked).
  - Entry 1 (l. 6-15, «packet precision, REFEREE-2 P-1; optional, taken»): §0's «Two faces never tie (P-IDEAL-RED ENC, signed; R105
    when» «landed: distinct options carry distinct β's, so their β-sets differ).» (packet l. 30-31) becomes «Two faces never tie: face
    k's β-set contains β(x, k) and» «not β(x, 1 − k), because by acyclicity neither chain returns to x, so the two β-sets differ; ENC
    (P-IDEAL-RED, RESULTS R105) then» «makes them unequal in the order.» (l. 11-13); «Reason: «distinct β's» alone does not separate the
    sets» (l. 14). REFEREE §C l. 150 «CORRECT.»; REFEREE-2 L2 l. 32 «That is exactly the correction I asked for.»
  - Entry 2 (l. 17-30, «line L-2; REQUIRED 1-2: REFEREE CUBE-L1 = REFEREE-2 LC-2, REFEREE-2 LC-1; OPTIONAL 3-6: both / CUBE-L3 / LC-P1 /
    LC-P2»): L-2 and its word diff against L-1, eight hunks; «Line L-1 (sha1 99ae8face50615b4ce1ce5cd5e69f223f17208e1) is unchanged» (l.
    4).
  No fix changes a signed statement (to check (8)).
- Not signed: packet §5 (machine check, «does NOT claim», READING, TARGET diff; «DATA / READING (not to sign)», l. 14), in particular
  its READING «So any proof of IDEAL-ACYC-POLY must use the W-key gate. The route «bound LP» is DEAD by Theorem LADDER-LP.» (l. 181) and
  «Whether the gate can follow such a path is the open question (L-RED R201).» (l. 182); L-2 carries the first only as «(READING: a
  polynomial bound on T must use the W-key rule)». OPEN, not claimed: any bound on T, U, KF or LP (packet l. 175 «no polynomial bound on
  T, U, KF or LP;»); any lower bound on IDEAL run lengths (l. 176 «no lower bound on IDEAL run lengths, and no super-polynomial IDEAL
  family;»); the converse of T ≤ LP (l. 93); whether o_G is of Matoušek type (l. 79-80); G-N5-TIME.
- Referee strengthening (NOT part of this entry; referee remarks and own checks):
  (i) REFEREE §1 l. 43 and REFEREE-2 §0 l. 26-27: DECOMP (c) proves the stronger §2.2 form («C_b(y) is constant on F, so y is not
      influenced by the other free coordinates», REFEREE).
  (ii) REFEREE-2 §3 l. 99-101: the ladder path exact for K = 1..12, Facts F0-F3 checked at every state of the path, DP longest path =
       2^(K+1) − 2 for K ≤ 8 («one further than the lane's 7»); REFEREE §4 l. 91-92: DP longest path 2^(K+1) − 2 for K = 1..6.
  (iii) REFEREE-2 §3 l. 111-112: a control, «the SMALLEST-π free coordinate is not combed in 1,495 of 18,095 faces of dimension ≥ 2. So
        (c)'s choice «largest π»» «matters».
  (iv) REFEREE §C l. 168 and REFEREE-2 §3 l. 113-114: with the gates of every mover in decreasing order, L_K's IDEAL run from b_0 has T
       = 1, so the DATA clause needs the gate order it states.
- Honest limits: (i) a STRUCTURE / REDUCTION statement inside the IDEAL model, at degree ≤ 2 only, with an exponential LOWER bound for
  LP, not for IDEAL runs: it bounds nothing polynomially; T ≤ LP is an upper bound by a quantity that is exponential on L_K, so it
  cannot by itself give a polynomial bound on T; G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim. (ii) LADDER-LP
  is about directed paths of o_(L_K), not about runs: on L_K with gate indices increasing in the option index the IDEAL run from b_0 is
  empty (DATA; packet l. 157-158 «With all movers at level 0, the W-key rule picks the gate-least option, and with gates» «increasing in
  k that run has T = 0 from b_0 (DATA, §5). The theorem is about directed paths, not runs.»). No super-polynomial IDEAL family and no
  lower bound on IDEAL run lengths is claimed (l. 176). (iii) Not covered: degree ≥ 3 (the cube is not binary, l. 79) and Ξ-cyclic
  genomes; the converse of T ≤ LP («most directed paths are not IDEAL runs: an IDEAL step also needs the W-key rule», l. 93); whether
  o_G is of Matoušek type (l. 79-80). (iv) «a polynomial bound on T must use the W-key rule» is a READING (REFEREE l. 119-120: «must»
  has no signed content). (v) Every statement is about R104's IDEAL model on acyclic Ξ-graphs; nothing is said about a real N5 run or a
  parity game beyond what R104 already says (packet l. 177). (vi) The weights 2^π(x) of DECOMP (b)'s potential are a proof device, not a
  computed quantity; TARGET §3 (bit cost) is not engaged (my reading; neither referee addresses it). (vii) Premises: RESULTS R104's
  definition and RESULTS R105's ENC and LOCAL (b); [WW22]'s definitions only; no lit note, no lane file. No Lean. (viii) Names: «LP» in
  this entry is LP_G(s_0), the largest length of a directed path of the improvement orientation o_G from the start; it is not RESULTS
  R27's Theorem LP or Corollary LP′ (different statements) and not a linear program (DE32, DE33); «D2» here is the set of movers with
  two options.
- Data (DATA, not proof): experiments/new/box153/decomp.py (l-new 43125a61, sha1 c82e850ece00a2b2a39b5f9e08d7ccc48b8066e9, 50 lines) and
  box153/longpath.py (43125a61, sha1 2ca0b0c3965900ebf88ac9658f9162495020babd, 49 lines), wired into experiments/new/check.sh block w102
  (l. 841-846); experiments/new/box154/ladder.py (l-new d97555d4, sha1 be946388ca29b9ac208e59641c31a362cfe420a8, 58 lines; L_K with gate
  indices 2x + k), block w103 (l. 847-852); all unchanged at a0bb2694; the three scripts reuse box150/check.py's simulator. Packet §5
  (l. 161-172): decomp.py checks DECOMP (o)-(c) and switch-all «by brute force over every face: 0 violations on 25 corpus genomes with»
  «≤ 10 degree-2 movers (478,953 faces).»; ladder.py: «DATA: OK for K = 1..10 (path lengths 2, 6, …, 2046); DP longest = 2^(K+1) − 2
  exactly for K ≤ 7; IDEAL T = 0.» (l. 170); longpath.py: «(x3_L8: LP 16 vs T 8; dc_d8: 64 vs 23)» and «ladlp_5.json (LP 114 at N = 10)»
  (l. 171-172).
  The blocks' outputs, reproduced by both referees and re-run for this draft (2026-11-04T04:46:17Z-04:46:47Z, from a `git archive` of
  a0bb2694's experiments/new, rc 0, byte-equal to the blocks' expected strings): «DECOMP genomes 25 faces 478953 USO 0 COMB 0 ORDER 0
  ACYC 0 JUMP 0 maxjump 7»; «LONGPATH ladlp_5.json n2 10 longest 114 ideal_T 1»; ten ladder lines ending « OK», the K = 7 line «LADDER K
  7 N 14 path 254 = 2^(K+1)-2 True nonimproving 0 flips [2, 4, 8, 16, 32, 64, 128] DP_longest 254 ideal_T 0 OK». REFEREE §4 l. 85-86
  «w103 at d97555d4 (box154/ladder.py 10): ten «OK» lines.», l. 87-88 (the two w102 strings, «These equal packet §5»); REFEREE-2 §3 l.
  93-96 («reproduce the check.sh strings»).
  REFEREE (successor 23; own docs/referee/scratch/cube_probe.py, sha1 9717764dc783266b52aab8d6e35641c4ea6f5e8f, on xinew_probe's β-set
  simulator «written from R104's text»; log xinew_logs/cube_probe.txt): L_K «built from §4's TEXT», DP longest path from b_0 «2, 6, 14,
  30, 62, 126 = 2^(K+1) − 2 for K = 1..6» (l. 91); «400 random degree-≤-2 IDEAL-ACYC genomes (1-7 degree-2 movers), 95,136 faces: unique
  sink 0 failures; acyclicity (DFS) 0; the» «largest-π free coordinate combed 0; MULTI→SINGLE 0; T ≤ LP(s_0) 0.» (l. 93-94); «No
  negative control was run for the cube checks. The proofs carry the signatures.» (l. 95); gate order (xinew_logs/cube_gateT.txt, §C l.
  166-168): T = 0 for K = 1..7 with increasing gates, T = 1 with decreasing gates.
  REFEREE-2 (successor 26; own docs/referee-2/R2-P-IDEAL-CUBE/cube_check.py, sha1 25088b5d1ef4a859214ff8d1a2a73f2b92177adf, values from
  its own R2-P-IDEAL-RED simulator; logs/run1.log, control.log): the ladder exact for K = 1..12, DP longest = 2^(K+1) − 2 for K ≤ 8,
  ideal_T 0 (l. 99-101); DECOMP over every face, COMB under 3 random topological orders, MULTI→SINGLE and T ≤ Σ_t #Mv_t ≤ LP on every
  start, 0 violations on 18 corpus genomes (62,730 faces, 2,880 runs), 400 random genomes (27,975 faces, 4,507 runs) and 150 wide random
  genomes (11,227 faces, 1,265 runs) (table l. 105-109); control l. 111 «the SMALLEST-π free coordinate is not combed in 1,495 of 18,095
  faces of dimension ≥ 2»; the logs at 0787732b print these numbers.
  No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-P-IDEAL-CUBE.md: successor 23's report 5ef7bf4724bcee2f487cd1f4c4a493f321dcca57
  (2026-11-04T02:49:13Z, new file, 140 lines, sha1 64a1aa4ff476b00d75617f00129d4426bb8d9b10, with scratch/cube_probe.py and
  xinew_logs/cube_probe.txt): DECOMP, MULTI→SINGLE, T ≤ LP, LADDER-LP SIGN (l. 12-15, 137), L-1 «NOT YET» (CUBE-L1, l. 127); §C
  3c3185d862a270c1d76b80ebad9a7a78b8c3c711 (2026-11-04T04:16:05Z, +34, l. 142-174; the file now 174 lines, sha1
  b4f1d9e5842c1de3edfeedfd23348aa506e828e2, with xinew_logs/cube_gateT.txt): entry 1 «CORRECT», CUBE-P1 «MET», «VERDICT: line L-2
  MATCHES.» (l. 174).
  REFEREE-2 (successor 26): docs/referee-2/R2-P-IDEAL-CUBE.md 0787732b82ea500ee63797d4be5664852e909df4 (2026-11-04T02:52:00Z, new file,
  160 lines, sha1 8c6f69f5162d21bc5838ce46882fd9a80a646e99; with R2-P-IDEAL-CUBE/cube_check.py and logs/): every statement SIGN (l.
  42-48), «No gap in the mathematics.» (l. 52), L-1 not yet (LC-1, LC-2, l. 50); R2-P-IDEAL-CUBE-L2.md
  993c1710952a57be2736855117ef54ae03d9838c (2026-11-04T04:17:33Z, new file, 43 lines, sha1 2746d78b0bbb26d41be12c0e4f1dc9c05a5a985c):
  «Verdict: **MATCHES**.» (l. 2) for L-2 and entry 1 «✓» (l. 29). Lane: freeze and L-1 d97555d425d4995244dd1648d00b7c53418cd03d, fixes
  entries 1-2 and L-2 a0bb269499779a9dd766b6fe504f0fc6166d0b31.
  INDEPENDENCE: REFEREE l. 2 «Independent: I did not read docs/referee-2/.»; REFEREE-2 l. 4 «I opened nothing in docs/referee/. A
  names-only `git ls-tree` on origin/claude/referee found 0 files matching «cube» at 02:50Z.», l. 5 «My checker imports no lane code.»
  REFEREE's report (02:49:13Z) precedes REFEREE-2's (02:52:00Z) by 2 min 47 s; the L-2 rounds are 88 s apart (04:16:05Z, 04:17:33Z), and
  neither L-2 file cites the other's L-2 verdict. Each referee wrote its own simulator (REFEREE from R104's text, REFEREE-2 from its
  R2-P-IDEAL-RED checker).
  Differences, resolved: REFEREE stated CUBE-P1 (landing after R105) as a landing condition, REFEREE-2 as a remark (§0 l. 34); REFEREE
  alone raised the optional CUBE-L3; REFEREE-2 alone raised LC-1 (gate order), P-1 (acyclicity for C_s(x)) and LC-P1; LOCAL (c) unused
  was noted by both (REFEREE §2 l. 51; REFEREE-2 LC-P2); both raised CUBE-L1 = LC-2 and CUBE-L2 = LC-P3. Both SIGN the same four
  statements with no gap, both accept entry 1, and both MATCH L-2. No disagreement in substance.
- TARGET.md diff: TARGET.md §1-§3 define parity games («A parity game is G = (V, V_E, V_O, E, pr) with V finite»), the regions W_E, W_O,
  M4 (§2 «There is a deterministic algorithm A and a polynomial p such that for every parity game G, A on input G halts within» «p(n +
  m) steps and outputs the pair (W_E(G), W_O(G)).») and the word-RAM cost model; no statement of this entry mentions a parity game, a
  winning region, an algorithm's running time or a cost model (packet §5 l. 183-186 «No statement here mentions a game, a region or an
  algorithm's running time. Each is about the improvement cube of the IDEAL» «model of R104. Not M4, not M3, not a gauntlet step.»;
  REFEREE §5 l. 98-102 «Agreed with packet §5: not M4, not M3, not a gauntlet step. G-N5-TIME OPEN.»; REFEREE-2 §0 l. 35-36 «**TARGET.md
  diff ✓.**»). LADDER-LP is «an exponential lower bound on directed paths, not on any algorithm's run» (REFEREE l. 100). The line (L-2)
  makes no M4 claim and no TARGET claim; its tail reads «a STRUCTURE / REDUCTION statement inside the IDEAL model» and «G-N5-TIME stays
  OPEN; not M3, not a step-4 pass, not a TARGET.md claim» (L-2, by script). Not a step-4 pass. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER R105's UPDATE of G-N5-TIME (GAPS at 91c1464f, last changed by 91c1464f: the last
UPDATE on l. 11 is R105's, «UPDATE 2026-11-04 02:59Z: RESULTS R105 (P-IDEAL-RED; CHECKER C116 e85c3bb2) …», before the row's closing «
|»), built by script (upd106.py: upd100L3.py's build() unchanged for the label move, on the claim body with a sentinel tail as for R102
and R105; the tail rule of (9); to check (9)) only from the clauses of the title line L-2: labels behind their clauses; « (2026-11-04) —
» → «: »; the DATA parenthesis before the source parenthesis opened as «; DATA: …»; «G-N5-TIME stays OPEN» and «not M3, not a step-4
pass, not a TARGET.md claim» dropped; the source parenthesis kept; «. G-N5-TIME stays open.» at the end. The same script reproduces
R97's to R105's LANDED UPDATEs (GAPS l. 11) byte for byte. L-2 holds no "|"; the UPDATE holds none. <DATE> is the landing date
(YYYY-MM-DD, by date -u at the landing commit; C114 Add. 1 E-1), <HH:MM> the landing time and <checker> the CHECKER C117 commit, all
filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R106 (P-IDEAL-CUBE; CHECKER C117 <checker>) [refereed-only] LANDED: In the IDEAL model of RESULTS R104 (the model first stated in L-RED R178 §1), on acyclic Ξ-graphs, at degree ≤ 2 (premises: R104's definition of the model, and P-IDEAL-RED's Lemma ENC and Lemma LOCAL (b), RESULTS R105; π a topological order of the Ξ-graph; D2 the movers with two options; the improvement cube Q_G = {0, 1}^D2 of states; C_s(x) the option of x with the strictly better Ξ-value at s; the improvement orientation o_G directs the edge between b and b ⊕ e_x away from the endpoint whose x-coordinate differs from C_b(x)), for every genome G: o_G is a unique sink orientation in the sense of Weber and Widmer, arXiv:2207.05985v1, Def. 4 (every non-empty face has exactly one sink); it is acyclic (Σ_x [b(x) ≠ C_b(x)] 2^π(x) falls along every edge); and in every face of dimension ≥ 1 the free coordinate of largest π is combed (all its edges in that face point the same way), so o_G is decomposable (every face combed, as in §2.2 of that paper) (DECOMP); every step of an IDEAL run that moves the set Mv_t is the directed path of o_G that switches the movers of Mv_t one at a time in increasing π, so T ≤ Σ_t #Mv_t ≤ LP_G(s_0), the largest length of a directed path of o_G from the start (MULTI→SINGLE); and for every K ≥ 1 the explicit genome L_K (all movers of degree 2, distinct gate indices) with N = 2K level-0 movers in pairs (u_i, v_i), i = 0, …, K − 1, where both options of u_0 and v_0 go to the exit, option 0 (option 1) of u_i and v_i goes to u_(i−1) (v_(i−1)) for i ≥ 1, all parities are even, every rank of pair i − 1 is above every rank of pair i, the ranks within pair 0 increase as β(u_0, 0) < β(v_0, 0) < β(u_0, 1) < β(v_0, 1) and within pair i ≥ 1 as β(u_i, 0) < β(u_i, 1) < β(v_i, 0) < β(v_i, 1), with start u_0, v_0 on option 0 and all other movers on option 1, has a directed path of o_(L_K) of length 2^(K+1) − 2 from that start, so LP ≥ 2^(N/2+1) − 2 (LADDER-LP): a STRUCTURE / REDUCTION statement inside the IDEAL model, together with an exponential lower bound for LP, not for IDEAL runs: T ≤ LP cannot by itself give a polynomial bound (READING: a polynomial bound on T must use the W-key rule); nothing is said about real IDEAL runs beyond T ≤ LP (DATA: on L_K with gate indices increasing in the option index, the IDEAL run from that start is empty); bounds nothing polynomially; Ξ-cyclic genomes and degree ≥ 3 are not covered; DATA: experiments/new/box153/decomp.py 0 violations on 25 corpus genomes, 478,953 faces; experiments/new/box154/ladder.py: the path of the proof checked for K = 1..10, and the longest path equals 2^(K+1) − 2 for K ≤ 7 (P-IDEAL-CUBE, docs/new/P-IDEAL-CUBE.md; L-NEW successor 50). G-N5-TIME stays open.

Proposed Dead-ends row (the Lead decides, (14); NOT part of the entry; to append after DE35 as the last line(s) of RESULTS, with <DATE>
the landing date; no "|"):
- DE36 (<DATE>): the route «bound LP» for IDEAL runs: bound the number T of steps of an IDEAL run of a degree-≤-2 IDEAL-ACYC genome
  through RESULTS R106's Corollary T ≤ LP (T ≤ LP_G(s_0), the largest length of a directed path of the improvement orientation o_G from
  the start) by a polynomial bound on LP. DEAD by a refereed proof: RESULTS R106 (LADDER-LP) (SIGN by REFEREE 23,
  docs/referee/R-P-IDEAL-CUBE.md 5ef7bf47, and REFEREE-2 26, docs/referee-2/R2-P-IDEAL-CUBE.md 0787732b; line L-2 449421e4 MATCHES at
  both): for every K ≥ 1 the explicit genome L_K (N = 2K level-0 movers of degree 2 in pairs (u_i, v_i), the Ξ-targets of pair i in pair
  i − 1, all parities even, every rank of pair i − 1 above every rank of pair i) has LP ≥ 2^(K+1) − 2 = 2^(N/2+1) − 2 from its start
  b_0. Instances: experiments/new/box154/ladder.py K (l-new d97555d4, sha1 be946388…; gate indices 2x + k; check.sh block w103) builds
  L_K and checks the proof's path for K = 1..10 (lengths 2, 6, …, 2046, every switch improving), DP longest path = 2^(K+1) − 2 exactly
  for K ≤ 7 (L_7, N = 14: 254); REFEREE-2's cube_check.py: K = 1..12, DP exact for K ≤ 8; REFEREE's cube_probe.py: DP exact for K ≤ 6.
  Obstruction (packet §4, Claim UP(i)): each change of B_(i−1), the option index that points to the better mover of pair i − 1, makes
  both movers of pair i improving, and each of their two switches changes B_i, so pair i re-arms pair i + 1 twice per change below it
  and B_i changes 2^(i+1) times along the path (ladder.py: flips [2, 4, …, 2^K]). The IDEAL run of L_K from b_0 is empty (DATA: T = 0
  for gate indices increasing in the option index, K = 1..10; T = 1 with decreasing gates): the W-key gate does not follow the path. Not
  dead: a polynomial bound on T itself (IDEAL-ACYC-POLY) and G-N5-TIME, both OPEN; that such a bound must use the W-key rule is a
  READING (RESULTS R106's line), not a signed statement.

Addendum (subagent, for the Lead; does not land; written 2026-11-04T05:01:27Z by date -u). (1) FIRST FILL on line L-2 (l-new a0bb2694,
sha1 449421e4…), to CHECKER C117. L-2 MATCHES at both referees (REFEREE 23 §C 3c3185d8; REFEREE-2 26 R2-P-IDEAL-CUBE-L2.md 993c1710).
NOT committed, NOT pushed; no tracked file edited; this file is new and untracked. The commits d97555d4, abe2b94c, a0bb2694, 5ef7bf47,
3c3185d8, 0787732b, 993c1710 (and C116 Add. 1 49f85ffc) are on local trunk 58198d07 (merge 3f4ea5aa) but not on origin trunk 8b31b166 at
this fill (header): push trunk before landing. (2) TITLE l. 350 = "### R106 [refereed-only] " + L-2 without its newline + ", CHECKER
PASS (docs/checker/C117.md, checker PENDING)", checked by script after the fill (fill106.py, chk106.py): equal, byte for byte (True);
the only «### R» heading of this file. (3) BODY l. 350-540 (title l. 350 to the last body line; 0 "|" in the range, by script);
GAPS preamble l. 542-550; UPDATE l. 551 (one line, 0 "|", one <DATE>, one <HH:MM>, one <checker>; controls True ×9:
R97's-R105's landed UPDATEs); proposed DE36 row l. 555-569 (0 "|", one <DATE>). A landing script in the shape of land104.py
slices d[349:540] for the entry and reads d[550] for the UPDATE (and d[554:569] for DE36 if the Lead takes it,
joined with "\n"). (4) RE-RUNS: check.sh blocks w102, w103 and the pin block from a git archive of a0bb2694 (04:46:17Z-04:46:47Z, rc 0,
byte-equal to the expected strings, three PASS lines), and my gate-order probe (04:51:46Z, rc 0) ((10)). NOT RUN: the referees' tools
(logs read instead), box153/longpath.py on the corpus, the full check.sh, scripts/verify.sh. (5) QUOTE SWEEP: chk106.py (q104.py's rule
as in chk105.py: outermost guillemet quotes, whitespace joined, split at the ellipsis, parts of 6+ characters; sources: packet, L-1,
L-2, fixes, the four referee files at their head commits, the referees' logs, notes/L-NEW.md at a0bb2694, check.sh at a0bb2694 and
abe2b94c, P-IDEAL-RED at 0ebddcf5, RESULTS, GAPS, DECISIONS, NOW, TARGET.md, CLAUDE.md, C116, my re-run outputs, the commit subject of
abe2b94c): 513 outermost quotes, 435 parts of 6+ characters, every part found (0 not found); in the title and body alone 154 quotes, 145
parts, 0 not found. Line-precise check of the referee verdicts and other cited lines: 242 of 242 (source, cited line range, quote)
triples found verbatim, whitespace-normalised, inside the cited lines. Every sha1, line count and commit time cited was re-measured in
this session (sha1sum, wc -l, cmp, git log -1 on the commit), not copied from a report. (6) DISCREPANCIES: see (11) (D-1 to D-10; none
affects a verdict) and G-1 to G-11 (notes). I found no error in a signed statement and no mismatch between a report and the lane files.
(7) FLAGS LEFT FOR CHECKER: none REQUIRED from my side. Notes: G-1 (source note names no fixes file), G-2 (unbound «T», «C_b», the
Iverson bracket; DECOMP (o) presupposed by o_G's definition), G-3 («LP», «R106», «D2» also name other RESULTS items; body sentence
Honest limits (viii) added under C116 G-2), G-5 (L41 not triggered, my reading; three points), G-7 (the gate-order DATA clause names no
K range), G-11 ([WW22] not opened by me), the DE36 proposal ((14)). (8) NOT VERIFIED: [WW22] itself (I did not open arXiv:2207.05985;
both referees did); the Lead brief of 01:56Z (packet l. 2) and the routing of 03:36Z (fixes l. 3) are not in the repository; REFEREE-2's
decreasing-gate probe has no committed log (D-4); the referees' tools were not re-run; I did not open docs/new/N5-CUBE-box153.md beyond
its commit (history only). Scratch files (not committed) in
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r106: R106-template.md, fill106.py,
chk106.py / chk106.out, upd106.py / upd106.txt / upd106.out, wdiff106.py / wdiff106.out, land106.py / land106.out, gateT106.py /
gateT106.out, w102.out, w103.out, blocks.out, runall.sh, runblocks.sh, the extracted sources (pkt.md, fixes.md, L1.txt, L2.txt, ref.md,
ref_5ef7.md, r2.md, r2L2.md, notes.md, checksh.txt, cs_*.txt, pred.md, the referees' logs and tools) and archa0bb/ (the archive). (9)
LANDING SIMULATION (land106.py, on in-memory copies of RESULTS and GAPS at local trunk 58198d07): RESULTS 10,934 -> 11,126 lines, a pure
insertion of 192 lines (the entry block with "checker PENDING)" filled, plus one blank line) directly before the erratum: True; R106 at
l. 10401-10591, blank l. 10592, the erratum moves to l. 10593; R105 and every other line byte-unchanged (common prefix and suffix); 0
"|" inserted. With DE36 (optional): a pure append after DE35 at l. 11127-11141: True. GAPS: only l. 11 changes: True; new l. 11 = old l.
11 with its closing " |" replaced by " " + the filled UPDATE + " |": True; "|" on l. 11 76 -> 76; 23 -> 23 lines. Fill values used only
for the simulation: <DATE> 2099-01-01, <HH:MM> 00:00, <checker> 0000000. (10) THIS DRAFT'S SHA1: a file cannot state its own sha1. The
sha1 of this file with the forty hex digits after the next colon replaced by forty «0» characters is:
1573b9dcf05f144f272f210874bc946687cd6a3e. The file's actual sha1 and line count are in the hand-back to the Lead (and re-measurable with
sha1sum).
