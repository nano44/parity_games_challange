# Draft RESULTS R101 (Lead; first fill 2026-11-01T03:08:02Z by date -u, read in the same command as the fill of this file (subagent); on GATE line — LANDED in RESULTS Results 2026-11-01 05:28Z (CHECKER C111 Add. 1 d53e1d4f PASS), after R100
L-1, docs/new/P-N5-GATE-line-L1.txt (l-new afb8b99e, sha1 d677161c4123dd184db14c17d26630e037b51027); packet, frozen line 245ce9fe, L-1,
fixes F0 + entry 1, REFEREE's R-N5-GATE (successor 21's report c9bc161c; successor 22's Addendum 1 c9644446 and §C ffbdc404) and
REFEREE-2's R2-N5-GATE (e35e8280) and R2-N5-GATE-L1 (9b30c652) read at the origin heads fetched at the start of the fill, 2026-11-01
before 02:51Z (l-new 7965c774, referee ffbdc404, referee-2 9b30c652, checker d293d5be; origin trunk 5cf4eb85; local trunk head 5cf4eb85 at the
start and c9283fb3 at the fill, which changes neither RESULTS nor GAPS); RESULTS R100 read LANDED (trunk 5cf4eb85); L-NEW's box 117, 118
and 120 pin blocks of experiments/new/check.sh re-run from a git archive of afb8b99e 2026-11-01 02:52:25Z-02:52:27Z, rc 0; box120/pincheck.sh
from the same archive 02:54:03Z-02:55:04Z, rc 0; DATA re-summed 02:56:46Z) — to CHECKER C111
REFEREE successor 22's Addendum 1 (c9644446) and §C (ffbdc404) are on origin claude/referee and on the local trunk head c9283fb3 (merge
d734f419, 2026-11-01 02:50:19Z), NOT on origin trunk 5cf4eb85: the Lead pushes trunk before landing. Every other commit cited here is on
both (by script, firsttrunk.py). R100 is LANDED (trunk 5cf4eb85, 2026-11-01 02:21Z; CHECKER C110 d293d5be PASS, no E-item). In the body
(title + entry), sentences about the earlier line revision say «at the frozen line»; every other sentence of the body describes L-1.
to check: FLAGS FIRST. G-1 is the item the Lead asked to flag prominently; G-2 is REFEREE 22's optional note; G-3 to G-5 are what the
pre-check of L-1 against CHECKER's recurring E-items (C106 E-1, C108 E-1, C109 E-1 / E-2 / E-3 with L43, R100's F-1) raised. None was
raised as REQUIRED by a referee; I changed nothing in the line. The same pre-check's CLEAN items follow the flags; soft spots D-1 to D-9.
- FLAG G-1, A CLASS-FREE ITEM OF A SUBCLASS R-LINE CITED "ON EVERY GAME" (CHECKER decides whether this is acceptable). L-1 cites «R18 (d)
  (Lemma R and Lemma S (a)-(b), the sandwich, used on every game: its proof uses no 𝒞^1O hypothesis: VJ00 (11), Lemma R, R15 (a), (d))».
  R18's heading reads «N5 on o-acyclic one-Odd-choice games» and its Setting line (RESULTS l. 785) «𝒞^1O = games in which exactly one Odd
  vertex o has out-degree d > 1.»; item (d) itself (l. 803-807) carries no class hypothesis. Both referees confirm the class-free proof:
  REFEREE §1 l. 24 «R18 (d) Lemma S (a)-(b), and whether it uses any 𝒞^1O hypothesis. It does not.», l. 32-33 «VJ00 (11), Lemma R
  (proved from SPEC S1 alone, R-N5-1OA l. 47), R15 (a) and R15 (d) are all game-general. Nothing in the argument refers to the single Odd
  choice vertex o, to X or to o-acyclicity.»; §C l. 140-141 «It is accurate: §1 above, and REFEREE-2 §2.» REFEREE-2 §2 l. 26 «**No.** I
  re-read box 21 §2.2 (trunk docs/new/N5-time-box21.md). It is the text R18 (d) signs.», l. 31 «Nothing in (a)-(b) mentions o, X,
  out-degrees, or o-acyclicity. In R18 those enter only in Proposition X and Lemmas 1-3 of (c).», l. 40-42 «Formal status (NEEDS): R18's
  heading scopes the R-line to o-acyclic 𝒞^1O, while item (d) itself is stated and proved class-free.», «Citing «R18 (d) … used on every
  game» is therefore correct as mathematics.», «Whether a CHECKER accepts a class-free item of a subclass R-line as a premise «on every
  game» is a Lead reading (cf. L42).»; R2-N5-GATE-L1.md l. 25 «The no-𝒞^1O statement is accurate: box 21 §2.2 (a) is VJ00 (11) on G and
  on G^d through Lemma R, and (b) is R15 (a) with (d).», l. 27 «Its formal acceptability as a citation of a subclass R-line item stays
  the Lead's reading, as before.»
  STATUS OF THE READING: the form applied is the Lead's brief to L-NEW successor 44, quoted in fixes F0 l. 14-15 («Cite it as «RESULTS
  R18 (d) Lemma S (a)-(b) (its proof uses no 𝒞^1O hypothesis: VJ00 (11), Lemma R, R15 (a), (d))». That meets REFEREE P-4 and REFEREE-2
  P-1 / P-2.») and logged in LEAD-STATE (2026-11-01 01:28Z: «Lead reading: cite Lemma S with «its proof uses no 𝒞^1O hypothesis»»). It
  is NOT a numbered Lead reading in docs/DECISIONS.md: the last there is L43, and «1O hypothesis» occurs 0 times in DECISIONS.md and in
  DECISIONS-INDEX.md (by grep). Fixes entry 1 (e) l. 104-105: «The Lead's reading above is the one applied. It is the Lead's, not mine.»
  LANDED PRECEDENTS (body, not title): R56 (RESULTS l. 2847-2850) «R18 (d) Lemma S (a) is signed under a 𝒞^1O setting line; both
  referees read its proof (VJ00 (11) and R17 (F1) on the one-player game G_σ) and CONFIRM it holds on every game (N-FBRED-3 = REFEREE
  §1)»; R55 (l. 2791-2793) «R17 (a)-(c), R18 (c) flat case, R18 (d) Lemma S (c) in its landed "⇒" form, R21 (a) XW, R21 (c) FBL-N (i),
  each signed under a 𝒞^1O setting line, whose proofs both referees read and CONFIRM use no one-Odd step»; R47's Lemma Φ (every game)
  uses «RESULTS R18 (d) Lemma S (b)» (l. 2337). NEW in R101: the class-free reading sits in the TITLE («used on every game: its proof uses
  no 𝒞^1O hypothesis: …»); R55 / R56 carry it in their bodies.
  RELATED SOFT SPOTS (no referee raised them): (i) R18's signature line keeps «Lemma S SIGNED WITH GAPS S1, S2, G-1OA-6 (first half)»
  (l. 825) and its joint open list ends «wording items G-1OA-1, G-1OA-2/N-1, G-1OA-6, N-2, N-4, N-5, S1.» (l. 830-831). REFEREE §1 reads
  both S1 and S2 as closed for (a)-(b) (l. 29 «The «⊵» halves of (4)/(6) are derived in R17 (a) (gap S1, closed).»; l. 30-31 «… by R15
  (d) (gap S2, closed).»); R47's body l. 2339-2341 «S1 does not touch (b) (it concerns Lemma S (a)), and S2 is (b)'s own citation, a
  citation item and not open mathematics»; G-1OA-6 is Lemma S (c)-(d) (l. 805-807), which L-1 does not cite. (ii) R18 (c) is a theorem
  «conditional on (P) for the one-player game G[X]» (l. 797); L-1 cites R18 (c) only for its reading «R17 Corollary 2, which both
  referees confirmed holds from any start» (l. 801-802), which is about R17 (e) (Corollary 2); L-1 applies it to R17 (d) (Corollary 1,
  switch-best). Both referees accept: REFEREE l. 41 ««Any start» is R18 (c)'s reading, as cited ✓.»; REFEREE-2 §3 l. 71 «R17 (d) bounds
  every such run by < B, from any start (R18 (c)'s reading), for every pointwise-optimal choice.» (D-4).
- FLAG G-2, TWO COLONS IN A ROW (REFEREE 22's optional note, §C l. 153-154: «Optional (not required): item 1 has two colons in a row
  («every game: its proof …: VJ00 …»). «(proof: VJ00 (11), Lemma R, R15 (a), (d); no 𝒞^1O hypothesis)» reads more cleanly. Left to
  CHECKER.»). L-1 reads «used on every game: its proof uses no 𝒞^1O hypothesis: VJ00 (11), Lemma R, R15 (a), (d))»; the second colon
  introduces the proof's ingredients, not a binder. L-1 has 24 colons (the frozen line 21). The UPDATE builder searches labels only after
  the binder «every vertex v, every transition k → k + 1 and all states k0 < k1: » (once in L-1), so neither colon moves a label. Not
  applied: the title is L-1 verbatim. If CHECKER asks for REFEREE 22's form, a line L-2 makes it and the title and UPDATE are rebuilt with
  the same scripts (fill101.py, upd101.py). REFEREE §1 l. 37-38 suggested the same form first («CHECKER may want the citation «(proof: VJ00
  (11), Lemma R, R15 (a), (d); no 𝒞^1O hypothesis)».»); L-NEW 44 took the Lead's form instead (fixes entry 1 (e) l. 99-100).
- FLAG G-3, L41 CLAUSE WITHOUT THE WORD «referee-originated» (the C109 E-1 class; CHECKER decides). L-1 contains «referee-originated» 0
  times (C109 E-1's literal test, C109 l. 42 «L-2 contains «referee-originated» 0 times.»). Its premise clause reads «the premises R17 (F1)
  and R18 (d) Lemma S (a) rest on derivations written by REFEREE and REFEREE-2 (R17 (a))» (unchanged from the frozen line). L41
  (DECISIONS.md l. 355-361) asks that the scope tail «says the proof is referee-originated»; the clause says so in other words. R17 (a)
  (RESULTS l. 739-740): «(F1) has two independent derivations: REFEREE via the dual of VJ00 Lemma 5.5's proof, REFEREE-2 via VJ00 (11) in
  the dual game plus the "⊵" halves of (4)/(6), which VJ00 asserts and REFEREE-2 derived.» R17 landed 2026-10-22, before L41 (2026-10-30).
  Both referees accept the clause: REFEREE §8 l. 106 «L41 tail («R17 (F1) and R18 (d) Lemma S (a) rest on derivations written by REFEREE
  and REFEREE-2 (R17 (a))») ✓.»; REFEREE-2 §6 l. 125-127 «L41: no proof in this packet is referee-originated.», «The tail clause «the
  premises R17 (F1) and R18 (d) Lemma S (a) rest on derivations written by REFEREE and REFEREE-2 (R17 (a))» is accurate.»; L1 l. 29 «The
  scope tail and the L41 premise clause are unchanged.» R100 (landed) used the word: «… whose proof is referee-originated (RESULTS R99:
  G-ST-1 = P-1) …». Reach: CONSISTENT-RED uses R17 (d), whose proof uses (F1)/(F2) (R17 (a)); SETTLE-MON, BRACKET-MON and the REDs use
  [SQZ] = R18 (d) Lemma S (a)-(b), whose (a) rests on (F1)'s «⊵» halves (gap S1). The clause names both; it does not name the claims
  that use them (as R100's does). If CHECKER wants the word, a line L-2 can read "… rest on referee-originated derivations, written by
  REFEREE and REFEREE-2 (R17 (a))" (my wording).
- FLAG G-4, STRICT SYMBOL TEST (the C109 E-2 class; soft, CHECKER decides). (i) «Ξ^d_(τ_k)» in «HI_k(v) := Ξ^d_(τ_k)(v) read as a triple
  of G (R18 (d) Lemma R)» is not glossed in L-1. «Ξ^d» occurs 0 times in RESULTS and GAPS (R18 (d) writes U_τ); SPEC S2 has «Iτ the same
  on G^d for τ» (docs/new/N5-ssi-global.md l. 47); the packet §1 l. 19 defines it («the valuation of v under τ_k and Even's optimal
  counterstrategy on G^d (SPEC S1 on G^d)»). (ii) «G» in «read as a triple of G» is not named in L-1, which says «every game»; G is
  TARGET.md §1's game («A parity game is G = (V, V_E, V_O, E, pr)») and R18 (d) Lemma R's («the order of the dual game G^d is the exact
  reverse of G's»). Both referees' symbol tests pass the line: REFEREE §8 l. 97-98 «All defined: n, m, K, values, Iσ_k, LO_k, HI_k, W_k,
  SET_k, lcp, CS (R93 (a)), B_k, SG, BG, G_τ, IW_k, τ-stretch, consistent, INC, λ_W-phase, B.»; REFEREE-2 §6 l. 129-130 «SET, B_k, SG, BG,
  IW_k, INC, τ-stretch, λ_W-phase and B are defined. No free symbol.»; L1 l. 28 «No free symbol.»; REFEREE §C l. 145 «No free
  symbol.» Neither
  lists Ξ^d or G. The packet's own pre-check (§9 l. 120-121) reads them «Ξ, Ξ^d per SPEC S1 («values … as in SPEC S1»). None free.»
- FLAG G-5, «τ-STRETCH» BESIDE R89's «τ-stretch» (name check; note). R89's title (l. 5854): «a τ-stretch := a maximal run of consecutive
  states with τ constant»; L-1: «a τ-STRETCH is a maximal set of consecutive transitions k → k + 1 with τ_k = τ_(k+1) all equal». The same
  object counted in transitions (the transitions between the states of R89's stretch); R89 is not cited by L-1. «SG» also names R19 (d)'s
  step (SG) (e.g. RESULTS l. 3070, «R19 (d)'s step (SG)»), a different object in a different arity («SG (BG) := the largest number …»).
- CLEAN AT L-1 (the same pre-check, by script on d677161c; wdiff101.py): C106 E-1 (stale body / old line as current): the title is L-1;
  the body describes L-1 as current, the frozen line only in history sentences («at the frozen line»); the old count «107 > 31» occurs in
  the body only in quotes of the frozen line, packet §6, REFEREE §6 / table and the first-state count. C108 E-1 (DATA overclaims): L-1 has
  0 «DATA», 0 «corpus», 0 «games», no count of a data set; its one «both» is «both checked against L-COMP's n5b and Oink» (the two DEAD
  instances; D-6); «referee» 0, «REFEREE» 2 (both in the L41 clause). C109 E-3 / L43 (asymptotic DEADs): 0 «O(», 0 «c·n», 0 «linear», 0
  «unbounded»; the one DEAD, «every λ_W-phase of a τ-stretch has at most n − 1 W-changing transitions», is killed at the EXPLICIT bound
  n − 1 by two pinned instances with both counts (403 > 289; 106 > 31), the L43 / R90 form; both referees: REFEREE §6 l. 65 «The killed
  statement has the explicit bound n − 1 (R17 (c)'s), so it is allowed in a line under L43.»; REFEREE-2 §3 l. 76-77 «It is an instance
  kill at an explicit bound, not an asymptotic DEAD, so it may enter the line (L43 form).». R100's F-1 (stale pins vs landed labels): no
  lane commit is pinned; every premise is a landed RESULTS label (R57, R17, R18, R15, R93, R99) or SPEC (S4 with FIX 3); the paths and sha1
  prefixes in the DEAD clause are instance files, not premises (fixes entry 1 l. 117 «The instance paths are files, not premises.»); R98
  and R100 are not used. C109 E-1 (L41): G-3. C109 E-2 (free symbols): G-4 and D-1 to D-3.
- Soft spots, no referee raised them as REQUIRED (details in (7)): D-1 the R57 gloss «σ_(k+1) is a pointwise optimum of the one-player
  arena in which Even y keeps … and Odd follows τ_k» (landed glosses read «the pointwise optimum of the one-player arena H_k»; L42 «σ_(k+1)
  is the pointwise optimum of H_k»); D-2 «Iσ_k(y)» used in the gloss before Iσ_k is defined (C110 N-5); D-3 V and E unglossed in «n :=
  |V|, m := |E|» (R96 precedent; TARGET.md §1); D-4 R18 (c)'s any-start reading (about Corollary 2) applied to R17 (d) (G-1 (ii)); D-5
  R17's setting has injective priorities (REFEREE-2 §3 l. 73); D-6 «both checked against L-COMP's n5b and Oink» is the lane's check; D-7
  «L-NEW box 116b» is a lane box label; D-8 claims stated narrower than signed; D-9 sha1 prefixes of 8 hex digits in the line.
(0) PLACEMENT, R100 LANDED. R101 goes after R100. R100 (P-N5-ROOT box 114) LANDED at trunk 5cf4eb85 (2026-11-01 02:21Z; CHECKER C110
d293d5be PASS), on origin trunk. docs/RESULTS.md at origin trunk 5cf4eb85 (identical at the local trunk head c9283fb3) has sha1
9f416da63ce875c8e0db71b9417af23584f37ecc, 9,771 lines, last changed by 5cf4eb85. «### R100» is l. 8918 (entry l. 8918-9249, l. 9250
blank); «## Dead ends (kept;» is l. 9251; "### R101", "R101" and «P-N5-GATE» occur 0 times in RESULTS and in GAPS (sha1
1f8fa46492e9575a5812ad42e494fdc9ac19ad2b, 23 lines, last changed by 5cf4eb85). R100's landed heading = «### R100 [refereed-only] » + ROOT
line L-3 + «, CHECKER PASS (docs/checker/C110.md, checker d293d5be)» (True, by script). R101's entry goes after R100's entry and its blank
line l. 9250, before «## Dead ends (kept;» (l. 9251), with one blank line after it (R97-R100's layout). The Lead re-checks (6) and (9) at
landing only if RESULTS or GAPS change after 9f416da6 / 1f8fa464.
(1) TITLE. The title is the line file docs/new/P-N5-GATE-line-L1.txt (l-new afb8b99ec47d8630c7409e19c17a5fada4fc288e, 2026-11-01T01:33:41Z,
the file's only commit, sha1 d677161c4123dd184db14c17d26630e037b51027; identical at l-new head 7965c774 and at trunk c9283fb3; first on
trunk by merge b13df772, 01:55:24Z), verbatim: one line, no outer quotes, no final period, 3,489 characters (3,601 bytes plus the newline),
638 whitespace tokens. NO HEADING MARKER, verified by script: the file begins «N5 on EVERY game (SPEC S1-S5, under the standing SPEC
premise», with no «#», no «R??» and no lane tag (Lead reading L41 «Lanes write line files without a heading marker (C104 N-1).»). So, as
in R95-R100, NOTHING is stripped: the heading is the level-3 marker, then "R101 [refereed-only] ", then the file without its newline, then
the fill. «2026-11-01» occurs exactly once in L-1, in « (2026-11-01) — REDUCTIONS and EQUIVALENCES» (by script), so NO date is inserted
(the R93-R100 rule). The line holds four "|": «|V|» and «|E|»; they stay in the heading (R91, R93-R100 carry "|") and are replaced in the
GAPS UPDATE only ((9)). The checker fill ", CHECKER PASS (docs/checker/C111.md, checker PENDING)" is appended as in R90-R100 (no space
before the comma); L-1 ends «… L-NEW successors 43-44)», so the heading ends "… successors 43-44), CHECKER PASS (…)". Built by script
(scratch fill101.py: assert the sha1 d677161c…, equality with the working-tree file and with the blob at afb8b99e, one line, no marker,
one «2026-11-01», four "|"; prepend "### R101 [refereed-only] ", append the fill) and re-checked after writing this file: equal, byte for
byte. Heading: 3,568 characters, 3,680 bytes; sha1 of the heading line without its newline cbaaee0124cef40312a7f3bb9698ecd84f662fc3, with its newline
da0f504a74c5c081a80f071a6cac0ee7f17b5ad7; it is l. 348.
Title features shared with landed titles (no new precedent): the scope words «REDUCTIONS and EQUIVALENCES» (R95, R99, R100); a lane DEAD
in the scope tail naming its instances (R90, R95, R100), here at an explicit bound with both counts (R90's «570 > 538» form); landed
entries cited by number (R57, R17, R18, R15, R93, R99); an L41 clause about the referee-written proofs of cited premises (R100). NEW in a
title, for CHECKER: (i) a class-free reading of a subclass R-line item, «used on every game: its proof uses no 𝒞^1O hypothesis: …» (G-1;
R55 / R56 carry such readings in their bodies); (ii) instance files pinned by path and sha1 prefix inside the scope tail (REFEREE P-3);
(iii) the L41 clause worded without «referee-originated» (G-3); (iv) «the sandwich is R18 (d)'s, not claimed here», a scope note that a
premise is not claimed.
(2) LINE HISTORY: the frozen line docs/new/P-N5-GATE-line.txt (sha1 245ce9feac30a6462ec31edca2c724e1409d9f06, committed with the packet in
516717da, 2026-11-01T00:07:39Z; 3,160 characters, 604 tokens, four "|", no marker, one date; the line both reports reviewed) → L-1
d677161c (docs/new/P-N5-GATE-line-L1.txt, l-new afb8b99e, 01:33:41Z, 3,489 characters, 638 tokens; fixes F0 + entry 1). The frozen line
is history, not the title. Each line file has one commit (git log on l-new). Word diff measured (difflib over whitespace tokens, scratch
wdiff101.py): 604 → 638 tokens, 14 non-equal opcodes, 589 tokens in common, grouped into exactly five changes:
- (1) R18 (d): «game),» → «game: its proof uses no 𝒞^1O hypothesis: VJ00 (11), Lemma R, R15 (a), (d)),» (REFEREE §1 precision / P-4;
  REFEREE-2 P-1, P-2; fixes entry 1 (e));
- (2) SG (BG): «SET» → «SET_k», «(B» → «(B_k» (REFEREE P-1; entry 1 (b));
- (3) CONSISTENT-RED: «with τ := τ_(k0),» inserted; «τ_k» → «τ_j» and four «k» → «j» (REFEREE P-2, REFEREE-2 P-3; entry 1 (c));
- (4) the DEAD instances pinned: «fbg_K12_m6_m24» → «experiments/new/box116/inst/fbg_K12_m6_m24.pg (sha1 2f035ca0…)», «(L-NEW» →
  «fbg_K12_m6_m24_fixed.start (9f03f81f…, L-NEW», «lend107_n32, 107» → «experiments/n5-epoch/instances/lend107_n32.pg (ab4c9811…) with
  lend107_n32.start (9df4ea2c…), n = 32, 106» (REFEREE P-3; REFEREE-2 GATE-L1, REQUIRED; entry 1 (a), (d));
- (5) the source note: «docs/new/P-N5-GATE-box120.md;» → «docs/new/P-N5-GATE-box120.md with its fixes entry 1,
  docs/new/P-N5-GATE-fixes-box120.md;», «successor 43)» → «successors 43-44)» (entry 1 (f)).
= fixes entry 1 l. 108-109 («Nothing else changes. The L41 clause («the premises R17 (F1) and R18 (d) Lemma S (a) rest on derivations
written by REFEREE and REFEREE-2 (R17 (a))») stays word for word.»); = REFEREE §C l. 139 («The diff has exactly five changes. Nothing else
in the line changed:»), items 1-5 l. 140-150; = REFEREE-2 R2-N5-GATE-L1.md l. 6-15 («Token diff: every change, nothing else», five items).
No inequality of a signed statement differs between the frozen line and L-1: change (3) renames a local index and names τ; the other
four touch a premise citation, a definition's wording, the DEAD's instances and count, and the source note ((4) checks each clause).
(3) THE LINE AT BOTH REFEREES. L-1 (the title): REFEREE successor 22, docs/referee/R-N5-GATE.md «## §C (successor 22, 2026-11-01T01:58Z by
date -u; Opus 5.5, D15): word-diff of line L-1» l. 136-155 (ffbdc404, 01:58:27Z, +21/−0): l. 147 «P-3 met. The sha1s equal my pins
(Addendum 1).»; l. 148-149 «GATE-L1 met: 106 equals my own strict recount (scratch/gate_strict.py: λ_W changes at transitions 1, 108,
109; phase 2-107) and L-NEW's box120/inphase.py («maxFirst 107 maxInPhase 106 at (2, 107)»).»; l. 155 «Verdict: line L-1 **MATCHES**
(GATE-L1 met; P-1..P-4 met). My Addendum 1 «REQUIRED GATE-L1» is discharged.» REFEREE-2 successor 25, docs/referee-2/R2-N5-GATE-L1.md
(9b30c652, 01:56:04Z, new file, 37 lines, sha1 88bfd512c07fc853d71ea812108c06055b779295): l. 2 «(re-hashed: match)»; l. 18 «**GATE-L1 is
closed.**»; l. 22 «The four pinned sha1 prefixes match my own hashes in R2-N5-GATE.md §4.»; l. 32 «**MATCHES** (Opus 5.5, D15). All my
GATE line items are closed.» ffbdc404 is on the local trunk only (header); 9b30c652 is on both (merge 83d99f04).
Frozen line: REFEREE successor 21, table l. 21 «MATCHES the signed items. Precision items only (§8)», l. 109 «Verdict: MATCHES the signed
items (precision P-1..P-4 optional).»; REFEREE-2 25 §6 l. 131 «Verdict on the line: **REQUIRED** (GATE-L1). Then a word-diff of the
revision.» REFEREE successor 22's Addendum 1 (c9644446, 01:31:04Z, +16/−0, l. 120-134), read after REFEREE-2's report: l. 131-133
«Verdict: I **concur with GATE-L1**. My §6 «107 … This equals the packet» is corrected to 106 under the line's wording. The DEAD stands
either way (106 > 31). My line verdict changes from MATCHES to **REQUIRED GATE-L1** (either «106 > 31», or a phase definition by first
states that keeps 107).» So the referees AGREE on the frozen line after Addendum 1 (one REQUIRED item, GATE-L1), and both MATCH L-1.
LINE-ITEM NAMES: each referee numbers its own items. REFEREE P-1 (B vs B_k), P-2 (τ := τ_(k0)), P-3 (pin the DEAD instances), P-4 (the
Lemma S premise, §1's precision); REFEREE-2 GATE-L1 (REQUIRED), P-1 (cite R15 (d)), P-2 (state the no-𝒞^1O proof), P-3 (local index j),
N-1 (packet §7's 118 → 116, DATA, not to sign). REFEREE P-2 and REFEREE-2 P-3 are merged in entry 1 (c); REFEREE P-4 and REFEREE-2 P-1 /
P-2 are met by entry 1 (e). Fixes F0's table (l. 18-28) maps every item; «Not applied: none.» (l. 30).
(4) CLAIMS SIGNED = the items below, each SIGNED in BOTH referees' verdict tables (REFEREE "## Verdicts" l. 11-21 of R-N5-GATE.md;
REFEREE-2 "## 1. Claims table" l. 14-21 of R2-N5-GATE.md and its FINDINGS l. 136-137), AND stated by L-1 (checked clause by clause
against the packet statements):
| item (packet §, lines) | REFEREE (successors 21, 22) | REFEREE-2 (successor 25) |
| --- | --- | --- |
| (a) Corollary SETTLE-MON (§2, l. 43-49; statement l. 45-46) | l. 15 «SIGNED»; §2-4 l. 46 | l. 17 «**SIGNED**»; §3 l. 48-51 |
| (b) Corollary BRACKET-MON (§3, l. 51-58; statement l. 52-54) | l. 16 «SIGNED»; §2-4 l. 47-50 | l. 18 «**SIGNED**»; §3 l. 52-57 |
| (c) SETTLE-RED and BRACKET-RED, EQUIVALENCES (§4, l. 60-67; statement l. 62-63) | l. 17 «SIGNED»; §2-4 l. 51-52 | l. 19 «**SIGNED**»; §3 l. 58-63 |
| (d) Lemma CONSISTENT-RED and its Corollary (§5, l. 69-85; statement l. 70-72, Corollary l. 81-83) | l. 18 «SIGNED»; §5 l. 55-62 | l. 20 «**SIGNED**»; §3 l. 64-74 |
| (e) the DEAD at the explicit bound n − 1 (§6, l. 87-98) | l. 19 «CONFIRMED on both instances by my own engine (lend107_n32 107 > 31; fbg_K12_m6_m24 403 > 289)»; §6 l. 65-71; 107 corrected to 106 by Addendum 1 l. 131 | l. 21 «**SIGNED** (instance check). fbg_K12 is exact (403 > 289). lend107 has **106** > 31 under the packet's own phase definition, not 107 (GATE-L1)»; §4 l. 97-107 |
Both lists, verbatim: REFEREE FINDINGS l. 114 «Every item to sign is SIGNED, with no gap.»; REFEREE-2 l. 136-137 «SETTLE-MON, BRACKET-MON,
SETTLE-RED / BRACKET-RED, CONSISTENT-RED with its Corollary, and the §6 DEAD are all SIGNED (Opus 5.5, D15). There is no gap.»; fixes F0 l.
8-9 for REFEREE («SIGNS SETTLE-MON, BRACKET-MON, SETTLE-RED / BRACKET-RED, CONSISTENT-RED and its Corollary. Confirms the §6 DEAD on both
instances.»). The packet's to-sign list (l. 9-10) names exactly these five. The DEAD row reads «CONFIRMED» at REFEREE and «**SIGNED** (instance
check)» at REFEREE-2: the same check, two words; REFEREE's count was corrected by its own Addendum 1 (l. 131).
Clause checks (L-1 against the packet): (a) l. 45-46, with «for every j ≥ k» for «every j with k ≤ j ≤ K» (j ranges over states) and k a
transition of the binder (k < K, the packet's «every k < K»). (b) l. 53, and «so B_k is non-decreasing in [0, n(n + 2)]» (l. 54); «and
rises at most n(n + 2) times» (l. 54) is not stated. (c) l. 62's four inequalities; «So, over any family of games, N5's iteration count is
polynomial ⟺ SG is polynomial ⟺ BG is polynomial.» (l. 62-63) is carried only by the label «EQUIVALENCES» (REFEREE-2 §3 l. 62 «The
equivalence is per run, so «over any family» means over any family of runs. ✓»). (d) l. 70-72 with τ := τ_(k0) and the local index j
(entry 1 (c)); the Corollary's bound l. 81 «at most (INC + 1)(B − 1) + INC transitions»; its «stretch lengths are polynomial over a family
⟺ their INC counts are» (l. 82-83) as «an EQUIVALENCE with INC». The Remark (l. 84-85, R18 (c) Lemma 3 as a special case) is not stated
(REFEREE-2 l. 75 «Not to sign.»). (e) the DEAD: l. 88-90's statement in L-1's wording «every λ_W-phase of a τ-stretch has at most n − 1
W-changing transitions», instance 1 (l. 91-93) as stated, instance 2 (l. 94-95) with 106 for 107 (GATE-L1). Nothing in L-1 is wider than
signed.
Signed by both, NOT stated by L-1, so NOT landed: BRACKET-MON's «rises at most n(n + 2) times»; the family readings of (c) and (d) as
sentences; the Remark. Not signed, so NOT landed: §7 DATA, §8 READING (packet l. 11).
(5) OTHER TEXTS THE ENTRY DEPENDS ON: the premises are landed RESULTS labels and SPEC ((6)); no lane packet is a premise. The proofs rest on
R18 (d) Lemma S (a)-(b) for [SQZ] (SETTLE-MON, BRACKET-MON and both REDs) and on R17 (d) with R18 (c)'s any-start reading for
CONSISTENT-RED (G-1). Lemma S's proof text is docs/new/N5-time-box21.md §2.1-§2.2 (R18's object (B), RESULTS l. 781-782 «with Lemma R and
Lemma S of docs/new/N5-time-box21.md §2.1-§2.2»), which REFEREE-2 re-read (§0 l. 10, §2 l. 26); REFEREE read its signed proof
docs/referee/R-N5-1OA.md l. 136-142 (§1 l. 28). The source notes docs/new/N5-SQUEEZE-box117.md and docs/new/N5-GATE-box118.md are «history
only» (packet l. 7-8 «This packet restates everything it uses; the notes are not needed to check it.»).
(6) PREMISE LABELS (stale-label test; RESULTS at 9f416da6 = origin trunk 5cf4eb85 = trunk c9283fb3). RESULTS labels in L-1 (by script):
«R57» 1, «R17» 4 (the premise, «R17 (c)'s bound», «R17 (F1)», «(R17 (a))»), «R18» 5, «R15» 1, «R93» 1, «R99» 1; «R98» 0. Every label
exists and carries the named item:
- R57 (l. 2893): the standing SPEC premise 1E-N3 (R57 (b) l. 2915-2916 «(1E-N3 = N-1E-1)»); S4a is Lead reading L42's reading of R57
  («R57's standing SPEC premise (1E-N3) covers S1's procedure and S4a (σ_(k+1) is the pointwise optimum of H_k).»). L-1's gloss writes the
  arena out (no H_k symbol; the C109 E-2 move) and says «a pointwise optimum» (D-1). CONSISTENT-RED uses it at S4a steps only (REFEREE §5 l.
  59 «[1E-N3] makes σ_(k+1) a pointwise optimum of that arena.»). L42's S4b restriction is not touched: the HI half of [SQZ] uses only that
  τ moves along Iτ (R15 (d)), not S4b optimality (REFEREE-2 §2 l. 34-37).
- R17 (l. 730): (b) Lemma P l. 741-742, (c) Theorem PH l. 743-744, (d) Corollary 1 l. 745-746 («switch-best on one-player games makes fewer
  than (n² − n + 1)(n + m) steps», «the bound holds for every pointwise-optimal choice»); (a) (F1) l. 738-740. Setting l. 734-736:
  «injective priorities» (D-5); switch-best «ρ_{k+1} = an optimal strategy of the arena H_k in which every vertex x may use {ρ_k(x)} ∪
  I_k(x) (VJ00 improving edges, §4.4 eq. (2))». REFEREE §1 l. 39-41; REFEREE-2 §0 l. 9 «RESULTS R17 (b)-(e), R18 (c)/(d), R15 (a)/(d), R57,
  R93, R99 (Lemma SANDWICH), all on trunk.»
- R18 (l. 778): (c) l. 797-802 (the any-start reading, G-1 (ii)); (d) l. 803-807, Lemma R «the order of the dual game G^d is the exact
  reverse of G's» and Lemma S (a)-(b) («(b) L_{σ_k} ⊴ V_{σ_k,τ_k} ⊴ U_{τ_k}, with L non-decreasing and U non-increasing along the run»);
  Setting l. 785 (𝒞^1O; G-1).
- R15 (l. 624): (a) Lemma A l. 631-632, (d) l. 640-643 («every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅
  ≠ I ⊆ Iτ to Odd's τ (on G^d)»), cited inside the R18 (d) parenthesis.
- R93 (l. 6972): (a) Fact LEX l. 7031-7036 («x ◁ y iff CS(x) < CS(y) lexicographically»; CS(x) := (rew(c); s_{n−1}, …, s_0; ℓ̂), length n
  + 2). The packet's [LEX] reads «R93 (a): CS is order-preserving and injective» (l. 37).
- R99 (l. 8596): «(Lemma SANDWICH) for sequences x, y, z of one length in lexicographic order, x ≤ y ≤ z implies lcp(x, z) = min(lcp(x, y),
  lcp(y, z))» (by script). REFEREE l. 42 «R99 SANDWICH (signed by me in R-N5-STAIR §3) ✓.»
- SPEC S4 with FIX 3: docs/new/N5-ssi-global.md l. 88 «FIX 3 (S4c, A7). In a fallback iteration with Iσ ≠ ∅ only σ changes (τ_new = τ);
  n5.py l. 61-62. Odd falls back only if Iσ = ∅.»; landed as a premise before (e.g. R68, RESULTS l. 3529 «SPEC (S2, S4a, S4c
  with FIX 3)»). REFEREE l. 43 «SPEC S4 with FIX 3: the arenas and the fallback rule as used ✓.»
- VJ00 (11): an equation of the opened source (Vöge-Jurdziński, BRICS RS-00-48; RESULTS R15 l. 627-629), cited in R17 (a) and R18 (d).
- Name check against landed text (RESULTS / GAPS at 9f416da6 / 1f8fa464; by script, word boundaries, a hyphen counted as a word character):
  «P-N5-GATE», «SETTLE-MON», «BRACKET-MON», «SETTLE-RED», «BRACKET-RED», «CONSISTENT-RED», «SET_k», «B_k», «BG», «IW_k», «INC», «LO_k»,
  «HI_k», «λ_W-phase», «Ξ^d», «SQZ», «fbg_K12_m6_m24», «lend107_n32», «box 116b» occur 0 times in both. «SG» 15 times in RESULTS, R19 (d)'s
  step (SG) (G-5); «τ-stretch» 27 times in RESULTS and «τ-STRETCH» twice, R89's / R90's stretch of states (G-5); «G_τ» 65 times, the
  one-player game with Odd fixed to τ (the same object; R17 / R18's); «lcp» 20 times in RESULTS, R99's (the same object); «sandwich» 4
  times, of which l. 3555 and l. 4542 are other lanes' (MON) sandwiches; «FALLBACK» 5 times (SPEC S4c's fallback, the same object);
  «GATE» 8 times in RESULTS, none a packet name (R74's GATE at t, l. 3890; R92's GATE term and pin counts, l. 6859-6929). "### R101" and
  "R101": 0 in both.
(7) SYMBOL TEST of the title (my own strict test of every symbol of L-1, by hand; IN = bound in the line; else the carrier):
| symbol | where |
| --- | --- |
| N5, SPEC S1-S5, «Even», «Odd», S4a, S4c, SPEC S2, SPEC S4 with FIX 3 | SPEC (named) |
| R57 gloss: k, σ_(k+1), y, σ_k(y), Iσ_k(y), τ_k | k IN («for S4a at a transition k → k + 1»); y the gloss's own letter («Even y keeps»); Iσ_k defined later in the line (D-2) |
| premises R17 (b)-(d), R18 (c), R18 (d), R15 (a), (d), R93, R99; VJ00 (11); 𝒞^1O | cited; see (6); 𝒞^1O by R18's Setting (G-1) |
| B | IN («B := (n² − n + 1)(n + m)») |
| run, states (σ_k, τ_k), K, transition k → k + 1, FALLBACK | IN («k = 0, …, K»; «a FALLBACK is a transition at which S4c fires») |
| n, m, V, E | n, m IN; V, E not glossed (D-3); = TARGET.md §1 l. 8 «n = \|V\|, m = \|E\|» |
| values, ⊴, ◁, ▷ | «as in SPEC S1» |
| Iσ_k, LO_k, HI_k, W_k | IN; Ξ_(σ_k) SPEC S1's; Ξ^d and G unglossed (G-4) |
| SET_k, lcp, B_k, CS | IN; CS by «R93 (… the coordinate sequence CS of (a))» |
| SG, BG | IN («SG (BG) := …»; «SET_k grows (B_k rises)», REFEREE P-1) |
| G_τ, τ, IW_k, y, z | G_τ IN (τ its parameter); IW_k IN for a transition with τ_(k+1) = τ_k; y, z bound in the set |
| τ-STRETCH, CONSISTENT, INC, λ_W-PHASE, W(v), «cycle node» | IN; «cycle node of W(v)» is SPEC S1's (c, P, ℓ) first component (R89's λ_W) |
| binder: run, game, v, k, k0, k1 | IN («for every N5 run on every game, every vertex v, every transition k → k + 1 and all states k0 < k1») |
| SETTLE-MON: j | IN («for every j ≥ k») |
| CONSISTENT-RED: τ, j | IN («with τ := τ_(k0)», «for k0 ≤ j ≤ k1», «with k0 ≤ j < k1»; REFEREE §C l. 144-145) |
| scope tail: the sandwich, R18 (d), «R17 (c)'s bound», instance paths and sha1 prefixes, n = 290, n = 32, L-COMP's n5b, Oink, R17 (F1), R18 (d) Lemma S (a), R17 (a), G-N5-TIME, M3, step-4, TARGET.md | cited; files pinned by path and prefix (D-9); n5b / Oink tools (D-6); GAPS l. 11, TARGET.md |
Agreeing tests: REFEREE §8 l. 93-98 (binder, «All defined: …»), §C l. 144-145 («Binder check: j is bound by its own clause, k0 and k1 by
«all states k0 < k1», and τ by «:=». The outer «every transition k → k + 1» no longer collides. No free symbol.»); REFEREE-2 §6 l. 129-130,
L1 l. 28 («P-3 is met by item 3. τ is now defined, j is local, and k0, k1 stay bound by the binder («all states k0 < k1»). No free
symbol.»). Neither lists Ξ^d, G, V or E (G-4, D-3).
DOUBTS for CHECKER (no referee raised any as REQUIRED; no change proposed by me):
D-1 R57 gloss «is a pointwise optimum of the one-player arena in which Even y keeps {σ_k(y)} ∪ Iσ_k(y) and Odd follows τ_k». Landed
  glosses (R93-R100) read «σ_(k+1) is the pointwise optimum of the one-player arena H_k, H_k := …»; L42 «(σ_(k+1) is the pointwise
  optimum of H_k)». «a» matches the packet's [1E-N3] (l. 32-33 «σ_new is a pointwise optimum of the one-player arena H_k») and R17 (d)'s
  «The arena optimum is not unique»; CONSISTENT-RED needs only that σ_(k+1) is one of the optima. The arena is written out, so no H_k.
D-2 «Iσ_k(y)» in the R57 gloss before «Iσ_k := SPEC S2's improving set of σ_k» (C110 N-5: the same order in R93 / R100, a note).
D-3 V and E in «n := |V|, m := |E|» unglossed (R96, RESULTS l. 7748, has «n := |V|,» unglossed; TARGET.md §1 l. 6-8 names V and E).
D-4 R18 (c)'s reading «R17 Corollary 2, which both referees confirmed holds from any start» is about Corollary 2 (R17 (e)); L-1 applies
  «from any start» to Corollary 1 (R17 (d)), switch-best on a one-player game. Corollary 2 is N5 on one-player games, whose step is
  switch-best (R17 (e) l. 747); the any-start property is the same argument (Lemma P is stated for ρ_0 arbitrary, l. 741-742). Both
  referees accept (G-1 (ii)). R18 (c) itself is conditional on (P); the reading is not (R18 Honest limits (ii): (P) is «used only in
  Lemma 1 on G[X]»).
D-5 R17's setting has injective priorities (l. 735); REFEREE-2 §3 l. 73 «R17's setting assumes injective priorities. SPEC S1's rank
  relevance gives that, as in R17 (e).» L-1 does not say it.
D-6 «both checked against L-COMP's n5b and Oink»: a statement about the lane's checks, not the referees'. Record: L-NEW box118/pincheck.txt
  and box120/pincheck.txt (both instances: «identical state sequences: True», «--zlk verified», «--tl verified», «AGREE True»); my re-run of
  box120/pincheck.sh from the afb8b99e archive, identical to the stored output (by cmp; Data). REFEREE-2 ran Oink 8fbf0a7 on both (§4 l.
  108-109 «Oink 8fbf0a7 `--zlk -v` on both instances (logs/oink_pins.txt; tool R2-N5-ROOT114/oink_pins.py): «verified», and the regions
  equal N5's final regions.»); REFEREE ran its own engine only (§7 l. 89-90 «The two DEAD instances were re-run on my own engine, which is
  independent of n5b / n5x.»). The clause claims no referee check, so it is not wider than the record (C108 E-1 tested). The Oink commit is
  not in the line (the repository pin is scripts/setup_oink.sh «OINK_COMMIT="${OINK_COMMIT:-8fbf0a7}"»).
D-7 «(9f03f81f…, L-NEW box 116b)»: the repaired start is named by a lane box label; it was added by l-new 4d4c26b0 («box 116b CARRY-ODD»,
  2026-10-31T18:42:24Z), the last commit touching it.
D-8 L-1 states less than signed in places ((4): BRACKET-MON's rise count, the family sentences, the Remark) and nowhere more; SETTLE-MON's
  k ranges over transitions (k < K), so the k = K case of the packet's «every j with k ≤ j ≤ K» is trivially omitted.
D-9 the instance files are pinned by 8-hex-digit sha1 prefixes in the line; the full sha1s are in fixes entry 1 (d) l. 96-97 and in the
  body (Data), re-hashed by me at afb8b99e, 516717da and trunk (equal).
(8) FIXES AND STATUS NOTES (fixes file at afb8b99e, sha1 bd45881670fdb8feaf08b76e24e414872c6db430, 124 lines, the file's only commit; =
l-new head 7965c774 = trunk c9283fb3; recorded under Fixes): F0 and entry 1, one commit afb8b99e (2026-11-01T01:33:41Z, with L-1 and
experiments/new/box120/), author L-NEW successor 44 (l. 4 «Author: L-NEW successor 44 (Opus 5.5), D14 / D18. Newest entry last.»).
Quotes checked by script (this fill): F0's REFEREE line l. 7 «claude/referee c9bc161c (file sha1 c5fff4c5; unchanged at 65b74579)» =
c9bc161c's file sha1 c5fff4c540e4…; l. 11 «claude/referee-2 e35e8280 (file sha1 70484101)» = 70484101a57a…; entry 1's REFEREE blocks
(l. 34-36, l. 38-44), the leading «> » stripped, = R-N5-GATE.md l. 36-38 and l. 99-105; its REFEREE-2 blocks (l. 47-52, l. 54-60, l.
62-68) = R2-N5-GATE.md l. 40-45, l. 101-107 and l. 112-118 (True ×5, line for line; scratch fxq101.py). REFEREE §C l. 140-150
checks entry 1 item by item; REFEREE-2 L1 l. 23-28 checks P-1 to P-3.
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-1 states no CONJECTURE. A line-11 UPDATE is proposed at the end, to go AFTER R100's UPDATE
(GAPS at 1f8fa464: the last UPDATE on l. 11 is R100's «UPDATE 2026-11-01 02:21Z: RESULTS R100 (P-N5-ROOT box 114; CHECKER C110 d293d5be)
…», ending «G-N5-TIME stays open.» before the row's closing « |»; l. 11 holds 76 "|" and 35 «UPDATE 2026-»), as a pure insertion with
one separating space. Built by script (scratch upd101.py: upd100L3.py's build() unchanged, read from that file; labels searched after the
binder's colon «every vertex v, every transition k → k + 1 and all states k0 < k1: »). Construction (R94's-R100's): «LANDED: » + the title
body with each clause label moved behind its clause; the scope tail " (2026-11-01) — REDUCTIONS and EQUIVALENCES (X) (source)" → ":
REDUCTIONS and EQUIVALENCES; X′ (source). G-N5-TIME stays open.", X′ = X minus «G-N5-TIME stays OPEN» and «not M3, not a step-4 pass, not a
TARGET.md claim»; the source parenthesis is KEPT; X′ keeps the DEAD and the L41 clause, as R99's and R100's landed UPDATEs keep theirs.
CONTROLS (same script, same run): R97's, R98's, R99's and R100's LANDED UPDATEs (GAPS l. 11 at 1f8fa464) from SRC L-5 (l-red a5340f2d), ODD
L-3 (l-si 2f8e5b2e), STAIR L-3 (l-new 7dc1eb7c) and ROOT L-3 (l-new 4cac9dc5), byte for byte (True ×4; 4,179, 4,260, 4,870 and 4,768
bytes). CONSISTENT-RED's inner «; hence a τ-stretch has at most …» stays before its label (the script moves each label to the end of its
whole clause, as for R100's DESC-ROOT). The UPDATE must hold no "|"; L-1 holds four, so these replacements were made, which are NOT title
text: (q1) «n := |V|» → «n := the number of vertices of the game» (= R98's and R100's (q1)); (q2) «m := |E|» → «m := the number of edges of
the game» (new; L-1 is the first line with m). Checked by script: one line, 0 "|", one «<HH:MM>», one «<checker>», 3,695 bytes, 649
tokens. Head «UPDATE 2026-11-01 <HH:MM>Z: RESULTS R101 (P-N5-GATE; CHECKER C111 <checker>) [refereed-only] » («P-N5-GATE» occurs 0
times in RESULTS and GAPS, so no box number is needed, unlike R100's F-4); <HH:MM> and <checker> are filled at landing (if R101 lands
after 2026-11-01, the date is corrected).
(10) DATA of record = the packet's §7 (l. 100-111), with the count fixed by N-1. Re-summed for this draft (python3 -I, scratch sum101.py
over the stored outputs in the git archive of afb8b99e: experiments/new/box120/i_sbcg.txt (719 rows) and i_alt.txt (413 rows), added by
afb8b99e; 2026-11-01 02:56:46Z by date -u, rc 0): 1,132 rows, 0 unparsed; runs exceeding n − 1 in one λ_W-phase: 118 by first state
(box 118's gate.py grouping, = packet §7 l. 110 «118 runs exceed the §6 bound») and 116 in-phase (the line's definition, = REFEREE-2 §4 l.
94 and fixes entry 1 (a) l. 85); maxFirst − maxInPhase ∈ {0, 1} on every row (= fixes l. 86 «The two groupings differ by at most 1.»).
The other §7 figures (INC 12,433 of 17,841 climb steps; 575 runs with INC 0; SG ≤ 3.41n, BG ≤ 2.91n; the separation rows) were NOT
re-summed by me; REFEREE-2 reproduced the first three with its own tool (§4 table l. 88-94). No signed statement uses any count.
(11) Discrepancies, recorded for CHECKER, no verdict affected: (i) REFEREE successor 21's §6 l. 66-67 «a largest λ_W-phase with 107
W-changing transitions. 107 > 31 ✓. This equals the packet.» and its verdict-table row (l. 19, «lend107_n32 107 > 31») are corrected by
Addendum 1 l. 131 (106 under the line's wording); the report body was not edited (+16/−0). (ii) The frozen packet keeps «107 > 31» (§6 l.
95) and «118 runs exceed the §6 bound» (§7 l. 110); fixes entry 1 (a) l. 75 records 106 and 116, «the frozen packet is not edited». (iii)
REFEREE's Addendum 1 l. 127-128 has λ_W changing «at transitions 1, 108 and 109»; REFEREE-2 §4 l. 102 «with λ_W changing at transitions 1
and 108»; both give the phase 2-107 and 106 (REFEREE's strict_lend107.txt: «lam-changes at [1, 108, 109] strict 106 first-state 107»).
(iv) REFEREE §7 l. 87 «71 runs exceed the §6 bound n − 1 (the lane's 118 is on its 1,132-line list)»: REFEREE's own 719-game list, 656
analysed, by s21's first-state probe (Addendum 1 l. 123-124); not re-counted strictly («I did not re-run the corpus count. It is DATA, not
signed.», l. 133-134). (v) REFEREE-2 §0 l. 9 opened «RESULTS R17 (b)-(e)»; L-1 cites (b)-(d) (and (a) in the L41 clause). (vi) REFEREE §1
l. 39 «R17 (b)-(d) (RESULTS l. 1-17 of R17)» is a within-entry line range, not a RESULTS line number. (vii) Packet §6 l. 96 names the check
«experiments/new/box118/gate.py G START (field maxWchPerPhase)», whose first-state grouping is GATE-L1's cause; box120/inphase.py (fixes
entry 1 (a) l. 78) prints both. (viii) fixes F0 heading «(2026-11-01 01:3xZ by date -u)» has an unfilled minute; the commit is 01:33:41Z.
(ix) REFEREE-2 L1 l. 3 «577 → 610 words»; this draft's whitespace tokens 604 → 638 ((2)); the same changes.
(12) Excluded: L-NEW boxes 117-119 lane items not in this packet (docs/new/N5-SQUEEZE-box117.md, N5-GATE-box118.md; box 119's «INC ≤
released blocked-edge switches» DEAD at constant 1, packet §7 l. 111 «(not part of this packet)»); box 121 (7965c774, after the freeze);
the §7 separation DATA (TBR / ARSB) and the §8 READING; REFEREE's and REFEREE-2's tools (docs/referee/scratch/gate_probe.py,
gate_strict.py, gate_logs/; docs/referee-2/R2-N5-GATE/gate_check.py, phases.py, logs/). Not part of this entry.
(13) Commits: lane (claude/l-new): 401d283a (2026-10-31T21:18:02Z; box 117) → 5ea2e738 (22:26:54Z; box 118, erratum) → 516717da
(2026-11-01T00:07:39Z; freeze: packet +135, frozen line +1) → afb8b99e (01:33:41Z; fixes F0 + entry 1 +124, L-1 +1, box120/). REFEREE on
claude/referee: c9bc161c (00:36:30Z; successor 21's report, new file 118 lines; gate_probe.py, gate_logs/) → c9644446 (01:31:04Z;
successor 22's Addendum 1, +16/−0) → ffbdc404 (01:58:27Z; §C on L-1, +21/−0). REFEREE-2 on claude/referee-2: e35e8280 (00:39:34Z; report,
new file 144 lines; R2-N5-GATE/ tools and logs) → 9b30c652 (01:56:04Z; R2-N5-GATE-L1.md, new file 37 lines). Trunk merges that brought
each in (the first first-parent trunk commit containing it; scratch firsttrunk.py): 401d283a → f1b1044e (2026-10-31 22:19:06Z); 5ea2e738
→ 2a75f7fa (23:12:04Z); 516717da → e7c7fe4c (2026-11-01 00:33:28Z); c9bc161c, e35e8280 → c6fff8cb (01:28:45Z); afb8b99e → b13df772
(01:55:24Z); 9b30c652 → 83d99f04 (02:21:17Z); c9644446, ffbdc404 → d734f419 (02:50:19Z, local trunk only at this fill).
(14) Placement: after R100 (LANDED; R100 is l. 8918-9249, l. 9250 blank, "## Dead ends (kept;" l. 9251, at 9f416da6; see (0)). No
Dead-ends row: no signed item kills a conjecture of RESULTS or GAPS; the DEAD «every λ_W-phase of a τ-stretch has at most n − 1 W-changing
transitions» is the packet's own §6 item, signed as an instance check, and named in the title as R90 / R95 / R100 name theirs (none has a
Dead-ends row). The Lead decides on a row (C110 §6 «the Lead decides on a row»).
### R101 [refereed-only] N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum; for S4a at a transition k → k + 1, σ_(k+1) is a pointwise optimum of the one-player arena in which Even y keeps {σ_k(y)} ∪ Iσ_k(y) and Odd follows τ_k); premises SPEC S4 with FIX 3, RESULTS R17 (b)-(d) (switch-best on a one-player game makes fewer than B := (n² − n + 1)(n + m) steps, for every pointwise-optimal choice, from any start as read in RESULTS R18 (c)), R18 (d) (Lemma R and Lemma S (a)-(b), the sandwich, used on every game: its proof uses no 𝒞^1O hypothesis: VJ00 (11), Lemma R, R15 (a), (d)), R93 (Fact LEX and the coordinate sequence CS of (a)) and R99 (Lemma SANDWICH)), with: a run is the sequence of states (σ_k, τ_k), k = 0, …, K, a transition is written k → k + 1, a FALLBACK is a transition at which S4c fires; n := |V|, m := |E|; values, ⊴, ◁, ▷ as in SPEC S1; Iσ_k := SPEC S2's improving set of σ_k; LO_k(v) := Ξ_(σ_k)(v), HI_k(v) := Ξ^d_(τ_k)(v) read as a triple of G (R18 (d) Lemma R), W_k(v) := the valuation of the (σ_k, τ_k)-play from v; SET_k := {v : LO_k(v) = HI_k(v)}; lcp := the length of the longest common prefix and B_k := Σ_v lcp(CS LO_k(v), CS HI_k(v)); SG (BG) := the largest number of consecutive transitions at none of which SET_k grows (B_k rises); G_τ := the game with Odd fixed to τ, and for a transition with τ_(k+1) = τ_k, IW_k := {(y, z) : y Even, z ≠ σ_k(y), W_k(z) ▷ W_k(σ_k(y))}; a τ-STRETCH is a maximal set of consecutive transitions k → k + 1 with τ_k = τ_(k+1) all equal, a transition of it is CONSISTENT if it is not a fallback and Iσ_k = IW_k, INC := the number of its other transitions; a λ_W-PHASE of a τ-stretch is a maximal set of its consecutive transitions at whose states the map v ↦ cycle node of W(v) is constant: for every N5 run on every game, every vertex v, every transition k → k + 1 and all states k0 < k1: (Corollary SETTLE-MON) SET_k ⊆ SET_(k+1), and v ∈ SET_k implies LO_j(v) = W_j(v) = HI_j(v) = LO_k(v) for every j ≥ k; (Corollary BRACKET-MON) lcp(CS LO_k(v), CS HI_k(v)) ≤ lcp(CS LO_(k+1)(v), CS HI_(k+1)(v)), so B_k is non-decreasing in [0, n(n + 2)]; (SETTLE-RED and BRACKET-RED, EQUIVALENCES) K ≤ (n + 1)(SG + 1) and K ≤ (n(n + 2) + 1)(BG + 1), while SG, BG ≤ K; (Lemma CONSISTENT-RED) with τ := τ_(k0), if τ_j = τ for k0 ≤ j ≤ k1 and every transition j → j + 1 with k0 ≤ j < k1 is consistent, then σ_(k0), …, σ_(k1) are k1 − k0 strategy-changing switch-best steps on G_τ and k1 − k0 < B; hence a τ-stretch has at most (INC + 1)(B − 1) + INC transitions, an EQUIVALENCE with INC (2026-11-01) — REDUCTIONS and EQUIVALENCES (no count is bounded here; the sandwich is R18 (d)'s, not claimed here; «every λ_W-phase of a τ-stretch has at most n − 1 W-changing transitions» (R17 (c)'s bound transferred) DEAD: experiments/new/box116/inst/fbg_K12_m6_m24.pg (sha1 2f035ca0…) with its repaired start fbg_K12_m6_m24_fixed.start (9f03f81f…, L-NEW box 116b), n = 290, 403 W-changing transitions in one λ_W-phase, 403 > 289, and experiments/n5-epoch/instances/lend107_n32.pg (ab4c9811…) with lend107_n32.start (9df4ea2c…), n = 32, 106 > 31, both checked against L-COMP's n5b and Oink; the premises R17 (F1) and R18 (d) Lemma S (a) rest on derivations written by REFEREE and REFEREE-2 (R17 (a)); G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim) (P-N5-GATE, docs/new/P-N5-GATE-box120.md with its fixes entry 1, docs/new/P-N5-GATE-fixes-box120.md; L-NEW successors 43-44), CHECKER PASS (docs/checker/C111.md, checker PENDING)
- Object (L-NEW successor 43, Opus 5.5, D14 / D18; frozen, unchanged during review): packet P-N5-GATE (box 120),
  docs/new/P-N5-GATE-box120.md, sha1 ac88915dfb07fc8b5644db99762671eee8ef7312, 135 lines (l-new freeze 516717da, 2026-11-01T00:07:39Z,
  the file's only commit; identical at afb8b99e, at l-new head 7965c774 and at trunk; first on trunk by merge e7c7fe4c, 00:33:28Z). Both
  referees measured the sha1 at 516717da (REFEREE l. 3-5 «Both equal the Lead's figures.»; REFEREE-2 §0 l. 6 «Re-hashed: match.»). Title
  (l. 1): «the settled set and the bracket never move back; a τ-stretch is R17's one-player climb except at inconsistent steps». Scope (l.
  3-6): «Scope: REDUCTIONS / EQUIVALENCES and one DEAD at an explicit bound.», «No count is bounded here. G-N5-TIME stays OPEN. This is not
  M3, not a step-4 pass and not a TARGET.md claim.», «The sandwich itself is NOT claimed here: it is landed RESULTS R18 (d) Lemma S (a)-(b)
  (box 21 §2.2), with Lemma R. This packet uses it as a premise (§1 [SQZ]).» To sign (l. 9-10): «To sign: §2 Corollary SETTLE-MON; §3
  Corollary BRACKET-MON; §4 SETTLE-RED and BRACKET-RED; §5 Lemma CONSISTENT-RED with its Corollary; §6 the DEAD (an instance check,
  explicit bound n − 1).» «Not to sign: §7 (DATA), §8 (READING).» (l. 11). Source notes (l. 7-8): docs/new/N5-SQUEEZE-box117.md and
  docs/new/N5-GATE-box118.md, «history only». Sections: §1 setting, premises (l. 14-41), §2 SETTLE-MON (l. 43-49), §3 BRACKET-MON (l.
  51-58), §4 SETTLE-RED and BRACKET-RED (l. 60-67), §5 CONSISTENT-RED, its Corollary and a Remark (l. 69-85), §6 the DEAD (l. 87-98), §7
  DATA (l. 100-111, not to sign), §8 READING (l. 113-116, not to sign), §9 the drafter's pre-check (l. 118-129).
  The RESULTS line, history: (1) the frozen line docs/new/P-N5-GATE-line.txt (sha1 245ce9fe…, committed with the packet), the line both
  referees reviewed: REFEREE 21 MATCHES with precision P-1 to P-4 (§8 l. 99-109); REFEREE-2 25 REQUIRED GATE-L1 (§5 l. 114, §6 l. 131).
  At the frozen line the DEAD clause read «… DEAD: fbg_K12_m6_m24 with its repaired start (L-NEW box 116b), n = 290, 403 W-changing
  transitions in one λ_W-phase, 403 > 289, and lend107_n32, 107 > 31, both checked against L-COMP's n5b and Oink»: 107 counts the
  phase's closing transition (lane gate.py's first-state grouping), and the line's own phase definition gives 106 (REFEREE-2 §4 l. 101-107;
  REFEREE Addendum 1 l. 125-128). REFEREE successor 22's Addendum 1 (c9644446) concurs and turns REFEREE's verdict to «REQUIRED GATE-L1»
  (l. 131-133). (2) L-1 d677161c4123dd184db14c17d26630e037b51027 (docs/new/P-N5-GATE-line-L1.txt, l-new afb8b99e, 2026-11-01T01:33:41Z,
  the file's only commit; first on trunk by merge b13df772, 01:55:24Z; fixes F0 + entry 1) = the frozen line with exactly five changes
  (word diff by script; to check (2)): R18 (d)'s citation «used on every game: its proof uses no 𝒞^1O hypothesis: VJ00 (11), Lemma R, R15
  (a), (d)» (REFEREE P-4; REFEREE-2 P-1, P-2; the Lead's citation form, fixes F0 l. 14-15); «SET_k grows (B_k rises)» (REFEREE P-1);
  CONSISTENT-RED «with τ := τ_(k0), if τ_j = τ for k0 ≤ j ≤ k1 and every transition j → j + 1 with k0 ≤ j < k1 is consistent» (REFEREE
  P-2, REFEREE-2 P-3); the DEAD's instances pinned by path and sha1 prefix, with «n = 32, 106 > 31» for lend107_n32 (REFEREE P-3;
  REFEREE-2 GATE-L1); the source «… with its fixes entry 1, docs/new/P-N5-GATE-fixes-box120.md; L-NEW successors 43-44». Fixes entry 1 l.
  108 «Nothing else changes.» REFEREE 22 L-1: §C (ffbdc404) l. 139 «The diff has exactly five changes. Nothing else in the line
  changed:», l. 155 «Verdict: line L-1 **MATCHES** (GATE-L1 met; P-1..P-4 met). My Addendum 1 «REQUIRED GATE-L1» is discharged.»
  REFEREE-2 25 L-1: R2-N5-GATE-L1.md (9b30c652) l. 6 «Token diff: every change, nothing else», l. 32 «**MATCHES** (Opus 5.5, D15). All my
  GATE line items are closed.»
  L-1 supersedes the frozen line; the title is L-1 verbatim with its own date (to check (1)). Neither referee found a FALSE claim
  statement in the packet; every line item corrects the DEAD's count, pins its instances, binds a symbol (τ, j), disambiguates B and B_k,
  or states why R18 (d) holds on every game.
  Setting (packet §1, l. 14-41): N5 = SPEC S1-S5 on an arbitrary game G, n := |V|, m := |E|; a run is the sequence of states (σ_k, τ_k),
  k = 0..K, a transition k → k + 1, a FALLBACK if S4c fired at it (l. 15-16); LO_k(v) := Ξ_k(v), «HI_k(v) := Ξ^d_(τ_k)(v)» read as a
  triple of G (RESULTS R18 (d) Lemma R), W_k (l. 19-21); G_τ and IW_k (l. 22-23); τ-STRETCH, CONSISTENT, INC (l. 24-25); CS (R93 (a)) and
  lcp (l. 26-27). Premises (l. 28-41): [SPEC] SPEC S4 with FIX 3; [1E-N3] (R57); [SQZ] R18 (d) Lemma S (a)-(b) with Lemma R «on every
  game» (l. 34-36); [LEX] R93; [SAND] R99 (Lemma SANDWICH); [R17] R17 (b)-(d) «from any start (RESULTS R18 (c): «R17 Corollary 2, which
  both referees confirmed holds from any start»)» (l. 40-41). REFEREE's premise row: «premises, incl. THE KEY CHECK: R18 (d) Lemma S
  (a)-(b) «on every game»» → «CHECKED, holds on every game (§1)» (l. 14); REFEREE-2 §0 l. 8-12 «Premises opened:». L-1's notation is the
  packet's, with SET_k (§2 l. 44), B_k (§3 l. 54), SG / BG (§4 l. 61), B (§1 l. 40) and the λ_W-phase (§6 l. 88-89).
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 21 (report c9bc161c) and successor 22 (Addendum 1 c9644446, §C on L-1
  ffbdc404); REFEREE-2 successor 25 (report e35e8280, R2-N5-GATE-L1.md 9b30c652)). Items (a)-(e) are SIGNED in both verdict tables
  (REFEREE "## Verdicts" l. 11-21 of R-N5-GATE.md, the DEAD row «CONFIRMED»; REFEREE-2 "## 1. Claims table" l. 14-21 of R2-N5-GATE.md);
  the table is to-check (4). All hold for every N5 run on every game. Premises LANDED (as L-1 names them): SPEC S1-S5, S4 with FIX 3;
  RESULTS R17 (b)-(d) with R18 (c)'s any-start reading; R18 (d) Lemma R and Lemma S (a)-(b), class-free in their proof (Flag G-1 of the
  draft; both referees confirm); R15 (a), (d) inside that citation; R93 (Fact LEX, CS); R99 (Lemma SANDWICH); standing premise: RESULTS
  R57's SPEC premise in its 1E-N3 form, used at S4a steps by CONSISTENT-RED (Lead reading L42 covers S4a; no item uses S4b optimality).
  The code's match to SPEC is DATA (R15 G-N5T-1). No item bounds a count.
  (a) Corollary SETTLE-MON (§2, l. 43-49): «SET_k := {v : LO_k(v) = HI_k(v)}.» (l. 44); statement (l. 45-46): «For every N5 run on every
      game and every k < K: SET_k ⊆ SET_(k+1). For v ∈ SET_k and every j with k ≤ j ≤ K: LO_j(v) = W_j(v) = HI_j(v) = LO_k(v).»; proof:
      the monotone halves of [SQZ] (induction on j) and the sandwich at j give a ⊴ LO_j(v) ⊴ W_j(v) ⊴ HI_j(v) ⊴ a, and [LEX] gives
      equality. Cells: REFEREE «SIGNED» (l. 15; l. 46 «SETTLE-MON ✓: a ⊴ LO_j ⊴ W_j ⊴ HI_j ⊴ a, and ⊴ is linear.»); REFEREE-2 «**SIGNED**»
      (l. 17; §3 l. 48-51; l. 57 «SETTLE-MON is in fact the case lcp = n + 2 of BRACKET-MON (CS injective).»).
  (b) Corollary BRACKET-MON (§3, l. 51-58): statement (l. 52-54) «lcp(CS LO_k(v), CS HI_k(v)) ≤ lcp(CS LO_(k+1)(v), CS HI_(k+1)(v)).»,
      «Hence B_k := Σ_v lcp(CS LO_k(v), CS HI_k(v)) is non-decreasing, takes values in [0, n(n + 2)], and rises at most n(n + 2) times.»;
      proof: a ≤ a′ ≤ b′ ≤ b lexicographically ([SQZ], R93 (a)), and [SAND] twice. Cells: REFEREE «SIGNED» (l. 16; l. 49 «SANDWICH on
      (a, a′, b) gives lcp(a, b) ≤ lcp(a′, b). SANDWICH on (a′, b′, b) gives lcp(a′, b) ≤ lcp(a′, b′).»); REFEREE-2 «**SIGNED**» (l. 18;
      §3 l. 52-57).
  (c) SETTLE-RED and BRACKET-RED, EQUIVALENCES (§4, l. 60-67): «SG := the largest number of consecutive transitions of the run at none of
      which SET grows (SET_(k+1) ≠ SET_k); BG := the same with «B rises».» (l. 61); statement (l. 62-63) «For every N5 run on every game:
      K ≤ (n + 1)(SG + 1) and K ≤ (n(n + 2) + 1)(BG + 1); and SG ≤ K, BG ≤ K.»; proof: SET grows at r ≤ n transitions, the rest form ≤ r
      + 1 windows of ≤ SG transitions; the same with ≤ n(n + 2) rises of B; correction (l. 67) «the bound proved is K ≤ (n + 1)(SG + 1);
      the equivalence is unchanged.» Cells: REFEREE «SIGNED» (l. 17; l. 51-52 «The correction of box 117's «(n + 1)·SG» is right.»);
      REFEREE-2 «**SIGNED**» (l. 19; §3 l. 58-63, l. 63 «K = SG + 1 with r = 1 is possible.»).
  (d) Lemma CONSISTENT-RED and its Corollary (§5, l. 69-85): statement (l. 70-72) «Let k0 < k1 be states of an N5 run on any game, with τ_k
      = τ for k0 ≤ k ≤ k1, and let every transition k → k + 1, k0 ≤ k < k1, be consistent (not a fallback, Iσ_k = IW_k). Then (σ_(k0), …,
      σ_(k1)) is a sequence of k1 − k0 switch-best steps on G_τ, each changing the strategy; hence k1 − k0 < B.», in L-1 with τ := τ_(k0)
      and the local index j (REFEREE P-2, REFEREE-2 P-3); proof: a consistent transition changes σ (else S4c fires, a fallback); S4a's
      arena with Iσ_k = IW_k is R17's switch-best arena on G_τ; [1E-N3] makes σ_(k+1) a pointwise optimum of it; R17 (d) for every choice
      from any start. Corollary (l. 81-83): «A τ-stretch with INC inconsistent transitions has at most (INC + 1)(B − 1) + INC transitions».
      Cells: REFEREE «SIGNED» (l. 18; §5 l. 55-62, l. 57-58 «IW_k is VJ00's improving set of σ_k in G_τ, because the VJ00 valuation of
      σ_k in the one-player game G_τ is W_k.»); REFEREE-2 «**SIGNED**» (l. 20; §3 l. 64-74; §4 l. 96 «CONS / OPT: 0 violations.»).
  (e) the DEAD (§6, l. 87-98): «Statement killed: «in every τ-stretch of every N5 run, every λ_W-phase (maximal set of consecutive
      transitions of the stretch at whose states the map v ↦ cycle node of W(v) is constant) contains at most n − 1 transitions at which W
      changes» (R17 (c)'s bound for switch-best, transferred).» (l. 88-90); instance 1 (l. 91-93) fbg_K12_m6_m24 with its repaired start,
      «n = 290, K = 404, 0 fallbacks; transitions 1 → 404 form one τ-stretch (403 transitions) and one λ_W-phase, and W changes at all 403:
      403 > 289 = n − 1.»; instance 2 (l. 94-95) lend107_n32 «107 > 31 (the run has 10 fallbacks)», 106 under the line's definition (GATE-L1).
      Cells: REFEREE «CONFIRMED on both instances by my own engine (lend107_n32 107 > 31; fbg_K12_m6_m24 403 > 289)» (l. 19; §6 l. 65-71),
      106 by its own strict recount (Addendum 1 l. 127-128, scratch/gate_strict.py, gate_logs/strict_lend107.txt and strict_fbg.txt);
      REFEREE-2 «**SIGNED** (instance check). fbg_K12 is exact (403 > 289). lend107 has **106** > 31 under the packet's own phase
      definition, not 107 (GATE-L1)» (l. 21; §4 l. 97-107, logs/pins.txt and logs/lend107_phases.txt, tool phases.py).
  The RESULTS line (L-1) claims less than the reports in places (no rise count in BRACKET-MON, no family sentences, no Remark) and nowhere
  more: every claim clause L-1 states is one of (a)-(d); its scope tail states the DEAD (e), a scope note on the sandwich, an L41 note on
  two premises, and no other claim (to check (4), (7)).
- Premise R18 (d) on every game (the Lead's flag; draft G-1). R18's heading names o-acyclic one-Odd-choice games and its Setting line
  𝒞^1O (RESULTS l. 785); item (d) (l. 803-807) has no class hypothesis. L-1 says why it is used on every game: «its proof uses no 𝒞^1O
  hypothesis: VJ00 (11), Lemma R, R15 (a), (d)». Both referees confirm it: REFEREE §1 l. 24 «R18 (d) Lemma S (a)-(b), and whether it uses
  any 𝒞^1O hypothesis. It does not.», l. 34 «So [SQZ] holds on every game, including the HI half, which uses R15 (d)'s Odd clause (τ moves
  only by Switch_I with I ⊆ Iτ on G^d).», FINDINGS l. 115 «R18 (d) Lemma S (a)-(b) uses no 𝒞^1O hypothesis. Its proof is VJ00 (11) on G
  and G^d, Lemma R and R15 (a)/(d), all game-general.»; REFEREE-2 §2 l. 40-41 «Formal status (NEEDS): R18's heading scopes the R-line to
  o-acyclic 𝒞^1O, while item (d) itself is stated and proved class-free.», «Citing «R18 (d) … used on every game» is therefore correct as
  mathematics.», FINDINGS l. 138 «R18 (d) Lemma S (a)-(b) needs no 𝒞^1O hypothesis: its proof is VJ00 (11) on G and G^d, Lemma R, and R15
  (a)+(d).» Both ran the sandwich and both monotone halves on every state of their corpora (REFEREE §7 l. 86 «VIOLATIONS 0 for SQZ, SET,
  BR, RED and CR.»; REFEREE-2 §2 l. 38-39 «[SQZ], all three inequalities: 1,679,311 vertex-state checks, 0 violations (§4).»). Whether a
  class-free item of a subclass R-line is accepted as a premise «on every game» is the Lead's reading (REFEREE-2 l. 42; L1 l. 27); the
  form applied is the Lead's brief quoted in fixes F0 l. 14-15, now recorded as Lead reading L44 (docs/DECISIONS.md, 2026-11-01 03:17Z), whose conditions (i) and (ii) hold here (above). Landed precedents carry
  the same reading in their bodies: R56 «R18 (d) Lemma S (a) is signed under a 𝒞^1O setting line; both referees read its proof (VJ00 (11)
  and R17 (F1) on the one-player game G_σ) and CONFIRM it holds on every game (N-FBRED-3 = REFEREE §1)»; R55 for R17 (a)-(c), R18 (c)'s
  flat case and R18 (d) Lemma S (c); R47 (Lemma Φ, every game) uses R18 (d) Lemma S (b). For CHECKER C111 to rule on.
- L41 (referee-written proofs): no proof text of THIS packet is referee-originated (REFEREE-2 §6 l. 125 «L41: no proof in this packet is
  referee-originated.»; REFEREE: no gap, no repair; fixes entry 1 l. 116 «L41: no proof in this packet is referee-originated.»). Two
  premises rest on derivations written by the referees: R17 (F1) (R17 (a): «(F1) has two independent derivations: REFEREE via the dual of
  VJ00 Lemma 5.5's proof, REFEREE-2 via VJ00 (11) in the dual game plus the "⊵" halves of (4)/(6), which VJ00 asserts and REFEREE-2
  derived.»), used by R17 (d) and so by CONSISTENT-RED; and R18 (d) Lemma S (a), whose «⊵» halves are those of R17 (a) (gap S1; REFEREE §1
  l. 29; REFEREE-2 §6 l. 128 «Lemma S (a) is (11) on G and G^d with those halves (gap S1).»), used through [SQZ] by SETTLE-MON,
  BRACKET-MON and both REDs. L-1's scope tail names them: «the premises R17 (F1) and R18 (d) Lemma S (a) rest on derivations written by
  REFEREE and REFEREE-2 (R17 (a))» (unchanged from the frozen line). Both referees: REFEREE §8 l. 106 (✓); REFEREE-2 §6 l. 126-127 «is
  accurate. R17 (a) records two referee derivations of (F1), one of them REFEREE-2's via VJ00 (11) plus the ⊵ halves of (4)/(6).» The
  clause does not use the word «referee-originated» (R100's tail does): for CHECKER (draft G-3).
- Fixes (docs/new/P-N5-GATE-fixes-box120.md, L-NEW successor 44, APPEND-ONLY, F0 and entry 1, one commit afb8b99e
  (2026-11-01T01:33:41Z, new file, 124 lines, sha1 bd45881670fdb8feaf08b76e24e414872c6db430; = l-new head 7965c774 = trunk)). Header (l.
  2-3): the frozen packet and line, «Neither is edited.» Each entry:
  - F0 (l. 6-30): REFEREE 21's report c9bc161c «SIGNS SETTLE-MON, BRACKET-MON, SETTLE-RED / BRACKET-RED, CONSISTENT-RED and its
    Corollary. Confirms the §6 DEAD on both instances.» «No gap.» (l. 8-9); REFEREE-2 25's report e35e8280 «SIGNS every item. No gap in
    the mathematics.» (l. 12), «Line: REQUIRED GATE-L1. Optional P-1 to P-3. Note N-1.» (l. 13); the Lead's citation form (l. 14-15); the
    item map (l. 18-28); «Not applied: none.» (l. 30).
  - Entry 1 (l. 32-124): REFEREE's precision items and REFEREE-2's §2 / §4 / §5 text quoted verbatim (l. 33-68); repairs (a)-(f) in L-1
    (l. 70-109): (a) GATE-L1 «taken in its first form (keep the line's λ_W-phase definition, correct the count)» (l. 71), with the cause
    (l. 73-74), the packet's 106 / 116 recorded and «the frozen packet is not edited» (l. 75-76), box120/inphase.py, pincheck.sh,
    runinphase.sh (l. 78-86); (b) «SET_k grows (B_k rises)»; (c) τ := τ_(k0) and the local j; (d) the instance pins with full sha1s (l.
    96-97); (e) the Lead's citation form, and «Not taken: REFEREE-2's example form «whose proof (box 21 §2.1-§2.2) …». It cites a lane file
    in a line; the Lead's form cites only landed labels and VJ00.» (l. 102-103); (f) the source note; the drafter's pre-check of L-1 (l.
    111-119).
  No fix changes a signed statement: entry 1 corrects an instance count of the DEAD (GATE-L1), pins, binds, renames, and words a premise
  citation (REFEREE §C l. 139-150; REFEREE-2 L1 l. 6-29).
- Not signed: §1 (premises and notation; REFEREE «CHECKED, holds on every game (§1)», l. 14); §7 DATA and §8 READING (packet l. 11; REFEREE
  l. 20 «not to sign»; REFEREE-2 §5 l. 118 N-1 «Not to sign»). The DEAD is item (e), signed as an instance check; L-1's scope tail states
  it: «every λ_W-phase of a τ-stretch has at most n − 1 W-changing transitions» (R17 (c)'s bound transferred) DEAD, with both instances
  pinned (at the frozen line, unpinned and with «107 > 31»). L43's test («one instance exceeding an EXPLICIT bound»): 403 > 289 at n = 290
  and 106 > 31 at n = 32, each above n − 1. OPEN, not claimed: whether SG, BG or INC is polynomially bounded (packet §4 l. 62-63, §5 l.
  82-83); G-N5-TIME. The §8 READING (l. 114-116, «CONSISTENT-RED says that inside a τ-stretch only the steps where Ξ's gate and W's
  objective disagree can be super-polynomial») is not landed.
- Referee strengthening (NOT part of this entry; remarks of one referee, or of both outside the verdict cells):
  (i) SETTLE-MON is the case lcp = n + 2 of BRACKET-MON (REFEREE-2 §3 l. 57).
  (ii) SET grows at r ≤ n − |SET_0| transitions (REFEREE-2 §3 l. 59), a sharper count than the packet's r ≤ n.
  (iii) Mutation controls (REFEREE §7 l. 81-83): «MUT 1 (HI := W): SET_V 30, BR_V 73, SQZM_V 239.», «MUT 2 (BR compared with LO_(k+1)
       instead of HI): BR_V 3,394.»; REFEREE-2 §2 l. 39 «A wrong dual encoding would fail the sandwich at once.»
  (iv) OPT (an OPT-OFF-form check at consistent transitions): REFEREE-2 §4 l. 96 «OPT has 347,234 checks at consistent transitions;
       consistent windows are all < B.»
  (v) REFEREE 22's optional form «(proof: VJ00 (11), Lemma R, R15 (a), (d); no 𝒞^1O hypothesis)» for the two colons in a row (§C l.
       153-154): not applied by L-1; OPEN, for CHECKER C111 (draft G-2).
- Honest limits: (i) REDUCTIONS and EQUIVALENCES: no count is bounded. SETTLE-RED / BRACKET-RED move K to the settle gap SG and the
  bracket gap BG, and CONSISTENT-RED moves τ-stretch lengths to INC; each up to polynomial factors. G-N5-TIME stays open. (ii) The
  sandwich and its monotone halves are R18 (d)'s, not claimed here; R101 uses them «on every game» on the strength of their class-free
  proof, which both referees confirm; the acceptability of that citation is for CHECKER (Flag G-1 of the draft). (iii) The DEAD shows
  only that R17 (c)'s per-phase bound n − 1 does not transfer to τ-stretches; it is not a lower bound on N5's iteration count (fbg_K12
  has K = 404 at n = 290). (iv) INC can be close to the stretch length on L-RED's builds (packet §7 l. 107-108, DATA: «cp_K4 43 / 44,
  s3quad_K8_m30 263 / 264, fbg_K12_m6_m24 395 / 403»), so CONSISTENT-RED alone gives no bound there. (v) Premises: R17 (d) holds for every
  pointwise-optimal choice and, by R18 (c)'s reading, from any start; R17's setting has injective priorities (REFEREE-2 §3 l. 73). The
  standing premise R57 (1E-N3) is used at S4a steps (Lead reading L42); no S4b optimality is used. The code's match to SPEC is DATA (R15
  G-N5T-1). (vi) Counts are transitions and lcp lengths, not bit operations; no running-time bound. (vii) Not M3, not a step-4 pass, not a
  TARGET.md claim; G-N5-TIME stays open. (viii) OPEN OPTIONAL PRECISION, for CHECKER C111 to rule on: REFEREE 22's two-colon note (§C l.
  153-154; draft G-2). The title is L-1 verbatim; if CHECKER asks for the change, a line L-2 makes it and the title and UPDATE are
  rebuilt with the same scripts.
- Data (DATA, not proof): pinned. experiments/new/check.sh at afb8b99e (the L-1 commit): sha1 db9c2878ef7202e66fd5e232ba875eb95ca7e6e0, 634
  lines (at 516717da and 5ea2e738: 1bac4380a290bfe02afcdfba7ddcd0065811071c, 628 lines; the 6 added lines are the box 120 block, l.
  628-633); the box 117 block is l. 616-621 and the box 118 block l. 622-627, identical at 5ea2e738, 516717da and afb8b99e (by diff); at
  the l-new head 7965c774 and trunk c9283fb3 a box 121 block follows (l. 634-639; sha1 e8ba10ed…, 640 lines). The packet and line files are
  NOT sha1-pinned in L-NEW's check.sh (C109 N-1, C110 N-6). Re-run for this draft from a `git archive` of afb8b99e (experiments/ and
  docs/new/; from experiments/new; GIT_DIR set to the repository), l. 1-8 (set -euo pipefail, cd, tmp) plus l. 616-633, 2026-11-01
  02:52:25Z-02:52:27Z by date -u, rc 0; output:
  «box 117 SQUEEZE: switchbestexp_2 N5 interval never widens (HIRISE 0, UNSET 0, settle gap 16); TBR widens (HIRISE 2, UNSET 3): PASS»;
  «box 118 GATE: cp_K4 one tau-stretch of 44, ungated one-player climb 2, INC 43; switchbestexp_2 INC 6, stretch 18 vs one-player 16:
  PASS»; «box 120 fixes GATE-L1: lend107_n32 one lambda_W-phase of 106 W-changing in-phase transitions (107 by first state): PASS». The
  box 120 block greps «INPHASE lend107_n32.pg n 32 K 112 maxFirst 107 maxInPhase 106 at (2, 107)» (the DEAD's instance 2 under the line's
  definition); the box 117 block greps «SQZ switchbestexp_2.pg N5 n 60 iters 32 SANDV 0 LODROP 0 HIRISE 0 UNSET 0 set0 4 setK 60 growths
  14 maxgap 16»; the box 118 block greps «GATE cp_K4.pg n 192 iters 44 stretches 1 climbsteps 44 fb 0 flat 0 gated 43 » and «onep 2
  maxratio 22.0 INC 43 maxConsistentWindow 1». The DEAD's instance 1 has no check.sh block: from the same archive I ran box120/inphase.py
  on it (02:52:41Z-02:52:54Z, rc 0): «INPHASE fbg_K12_m6_m24.pg n 290 K 404 maxFirst 403 maxInPhase 403 at (1, 403)». Supporting run of
  experiments/new/box120/pincheck.sh (fixes entry 1 (a) l. 79-82; same archive with tools/ linked to the repository's Oink build at
  8fbf0a7), 02:54:03Z-02:55:04Z, rc 0, output byte-identical to the stored box120/pincheck.txt (by cmp): «OINK lend107_n32 --zlk
  verified», «OINK lend107_n32 --tl verified», «PINWIN lend107_n32.pg n 32 states 113 fallbacks 10 W0 32 AGREE True», «n5b iterations 112
  fallbacks 10 states 113 | n5x states 113 | identical state sequences: True»; «OINK fbg_K12_m6_m24 --zlk verified», «OINK fbg_K12_m6_m24
  --tl verified», «PINWIN fbg_K12_m6_m24.pg n 290 states 405 fallbacks 0 W0 0 AGREE True», «n5b iterations 404 fallbacks 0 states 405 |
  n5x states 405 | identical state sequences: True». Pin files (sha1 at afb8b99e = 516717da = trunk): fbg_K12_m6_m24.pg
  2f035ca0a99946217bde6b740b87dd77bf884baf, fbg_K12_m6_m24_fixed.start 9f03f81fae5984fe92290f11c90dfaac3aecd419 (both last changed by
  4d4c26b0); lend107_n32.pg ab4c9811b311e303e5d41a9e923766a4b3fdae33, lend107_n32.start 9df4ea2ceafe43c4a7d88ef1e1f262101d7f0c35 (both
  dda29260); each equals fixes entry 1 (d) l. 96-97.
  DATA OF RECORD (packet §7 l. 100-111, with N-1's 116): corpus L-SI box 53's 1,132 runs, 0 violations of [SQZ], SETTLE-MON, BRACKET-MON;
  «SG ≤ 3.41n, BG ≤ 2.91n; INC 12,433 of 17,841 climb steps; 575 runs with INC 0» (l. 109-110); runs exceeding n − 1 in one λ_W-phase:
  116 (in-phase; 118 by first state). Re-summed (116 / 118 only) from the stored box120 outputs: equal (to check (10)).
  REFEREE (successor 21; own docs/referee/scratch/gate_probe.py, «no lane code», l. 73): «Corpus: 719 distinct games, MAXN 100 (656
  analysed, 63 skipped), start file when present (gate_logs/sum.txt).» (l. 84); «K 11,289 iterations, SQZ 529,356 checks, 619 τ-stretches
  (9,379 transitions, INC 7,083), SG ≤ 120, BG ≤ 98.» (l. 85); «VIOLATIONS 0 for SQZ, SET, BR, RED and CR.» (l. 86); pins (l. 66-71) and
  the strict recount (Addendum 1 l. 126-130).
  REFEREE-2 (successor 25; own docs/referee-2/R2-N5-GATE/gate_check.py, «The lane's box117 / box118 scripts are not imported.», l. 83):
  corpus 1,132 runs (l. 85), «RESULT PASS, 0 violations, in all three.» (l. 86); table l. 88-94 («12,433 / 17,841 | 12,433 / 17,841», «575
  | 575», «3.375, 2.875 (both within)», «116 (see GATE-L1: in-phase transitions only)»); «0 (1,679,311 SQZ vertex-state checks)» (l. 90);
  pins (l. 97-107); Oink (l. 108-109).
  No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-GATE.md: successor 21's report c9bc161c8523ed35ee29c1c607401c53047f5087 (2026-11-01T00:36:30Z, new
  file, 118 lines, sha1 c5fff4c540e4c70950dce2606e528d41c5640354, with docs/referee/scratch/gate_probe.py and gate_logs/; first on trunk by
  merge c6fff8cb, 01:28:45Z): §1 CHECKED, §2-§5 SIGNED, §6 CONFIRMED, no gap, line MATCHES with precision P-1..P-4; successor 22's
  Addendum 1 c96444460135942aa3afb25a9e0240d228fc4320 (01:31:04Z, +16/−0, l. 120-134; the file then 134 lines, sha1
  e7beb42d5b8b21a6994c7772909df97e1a8b5836; with scratch/gate_strict.py and gate_logs/strict_*.txt): concurs with GATE-L1, line REQUIRED
  GATE-L1; §C ffbdc404d0a580aa04a63b94accf02e0135ce8b4 (01:58:27Z, +21/−0, l. 136-155; the file now 155 lines, sha1
  13aab8d973502e5aa35fde3f0c0d445782d22a8a, = referee head): «Verdict: line L-1 **MATCHES** (GATE-L1 met; P-1..P-4 met).» (l. 155).
  c9644446 and ffbdc404 are on the local trunk by d734f419 (2026-11-01 02:50:19Z), NOT on origin trunk 5cf4eb85. REFEREE-2 (successor
  25): docs/referee-2/R2-N5-GATE.md e35e8280570e34592a5eeb36b25c089afd9c1226 (00:39:34Z, new file, 144 lines, sha1
  70484101a57a59c3cc29beb8d61b0b8fe5b8ce3f, unchanged since; with R2-N5-GATE/ tools and logs; on trunk by c6fff8cb, 01:28:45Z): every item
  SIGNED (l. 17-21, l. 136-137), line REQUIRED GATE-L1 (l. 131); R2-N5-GATE-L1.md 9b30c652eef548e77fac010578d7f5d0fd482b63 (01:56:04Z, new
  file, 37 lines, sha1 88bfd512c07fc853d71ea812108c06055b779295, = referee-2 head for this file; on trunk by 83d99f04, 02:21:17Z):
  «**MATCHES** (Opus 5.5, D15). All my GATE line items are closed.» (l. 32). Lane: freeze 516717daa2547291f0c9d98e5b7e8f15885af494, L-1
  and fixes afb8b99ec47d8630c7409e19c17a5fada4fc288e.
  INDEPENDENCE: REFEREE l. 6 «Independence: I opened no docs/referee-2/ file for this packet.»; Addendum 1 l. 121 «Read after my report of
  record (c9bc161c): REFEREE-2 25, docs/referee-2/R2-N5-GATE.md at e35e8280». REFEREE-2 l. 3 «Independence: written without opening
  docs/referee/ for this packet.»; L1 l. 4 «Written without opening REFEREE's GATE files.» The two reports were committed 3 minutes apart
  (c9bc161c 00:36:30Z, e35e8280 00:39:34Z). Neither review imported lane code (REFEREE l. 73 «no lane code»; REFEREE-2 l. 83); the lane's
  scripts ran only as the pinned blocks (REFEREE l. 89 «Lane check.sh blocks «box 116»-«box 118» were not re-run by me.»).
  Differences, resolved: GATE-L1 found by REFEREE-2 only, and conceded by REFEREE 22 in Addendum 1 (l. 123-124 «Cause, found in my own
  tool: s21's gate_probe.py (§6 above) assigns transition j → j + 1 to the phase of its FIRST state j. So it also counts the transition at
  which λ_W changes.»); line items numbered differently (to check (3)); both MATCH L-1. No disagreement in substance; the one open
  question, the citation of R18 (d) «on every game», is the Lead's reading (draft G-1).
- TARGET.md diff: «n := |V|, m := |E|» are TARGET.md §1 l. 8's n and m («n = |V|, m = |E|, d = |pr(V)| ≤ n + 1.»), V and E TARGET's (l.
  6); games are TARGET.md §1 games (REFEREE-2 §6 l. 121 ««N5 on EVERY game», n := |V|, m := |E|, as in TARGET §1. No algorithm claim, no
  polynomial bound proved, no unit-cost arithmetic.»). The line (L-1) makes no M4 claim and no TARGET claim; its own scope clause reads
  «REDUCTIONS and EQUIVALENCES (no count is bounded here; the sandwich is R18 (d)'s, not claimed here; …; the premises R17 (F1) and R18
  (d) Lemma S (a) rest on derivations written by REFEREE and REFEREE-2 (R17 (a)); G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a
  TARGET.md claim)» (L-1, by script). REFEREE §8 l. 108 «TARGET.md diff: scope words ✓, no algorithm claim.»; REFEREE-2 §6 l. 122-124
  «This is consistent with TARGET §2 and §4.», «Asymptotic words: none. The DEAD is at the explicit bound n − 1 with both counts (L43).»;
  REFEREE §C l. 151-152 «TARGET.md diff: no algorithm claim ✓.»; REFEREE-2 L1 l. 29 «The TARGET.md scope words are unchanged.» Not a claim
  of TARGET.md §1 or §2 (monotonicity of the settled set and of the bracket, two reductions of N5's iteration count to gaps, and a
  reduction of τ-stretch lengths to inconsistent steps; no bound on a run or on running time; no algorithm claim); not a step-4 pass.
  GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER R100's UPDATE of G-N5-TIME (GAPS at 1f8fa464, last changed by 5cf4eb85: the last
UPDATE on l. 11 is R100's, «UPDATE 2026-11-01 02:21Z: RESULTS R100 (P-N5-ROOT box 114; CHECKER C110 d293d5be) …», before the row's closing
« |»), built by script (upd101.py: upd100L3.py's build rule, labels searched after the binder) only from the clauses of the title line L-1,
with R94's-R100's construction (labels behind their clauses; the scope tail as in R95's-R100's UPDATE: the DEAD, the sandwich note and the
L41 clause stay inside the scope words, before the source note, which is kept). The same script reproduces R97's, R98's, R99's and R100's
LANDED UPDATEs (GAPS l. 11) byte for byte. L-1 holds four "|"; the UPDATE holds none: (q1) «n := |V|» → «n := the number of vertices of
the game»; (q2) «m := |E|» → «m := the number of edges of the game»; these replacements are not title text (to check (9)). Date
«2026-11-01» (the landing date; corrected at landing if later); time and CHECKER commit to be filled at landing:
UPDATE 2026-11-01 <HH:MM>Z: RESULTS R101 (P-N5-GATE; CHECKER C111 <checker>) [refereed-only] LANDED: N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum; for S4a at a transition k → k + 1, σ_(k+1) is a pointwise optimum of the one-player arena in which Even y keeps {σ_k(y)} ∪ Iσ_k(y) and Odd follows τ_k); premises SPEC S4 with FIX 3, RESULTS R17 (b)-(d) (switch-best on a one-player game makes fewer than B := (n² − n + 1)(n + m) steps, for every pointwise-optimal choice, from any start as read in RESULTS R18 (c)), R18 (d) (Lemma R and Lemma S (a)-(b), the sandwich, used on every game: its proof uses no 𝒞^1O hypothesis: VJ00 (11), Lemma R, R15 (a), (d)), R93 (Fact LEX and the coordinate sequence CS of (a)) and R99 (Lemma SANDWICH)), with: a run is the sequence of states (σ_k, τ_k), k = 0, …, K, a transition is written k → k + 1, a FALLBACK is a transition at which S4c fires; n := the number of vertices of the game, m := the number of edges of the game; values, ⊴, ◁, ▷ as in SPEC S1; Iσ_k := SPEC S2's improving set of σ_k; LO_k(v) := Ξ_(σ_k)(v), HI_k(v) := Ξ^d_(τ_k)(v) read as a triple of G (R18 (d) Lemma R), W_k(v) := the valuation of the (σ_k, τ_k)-play from v; SET_k := {v : LO_k(v) = HI_k(v)}; lcp := the length of the longest common prefix and B_k := Σ_v lcp(CS LO_k(v), CS HI_k(v)); SG (BG) := the largest number of consecutive transitions at none of which SET_k grows (B_k rises); G_τ := the game with Odd fixed to τ, and for a transition with τ_(k+1) = τ_k, IW_k := {(y, z) : y Even, z ≠ σ_k(y), W_k(z) ▷ W_k(σ_k(y))}; a τ-STRETCH is a maximal set of consecutive transitions k → k + 1 with τ_k = τ_(k+1) all equal, a transition of it is CONSISTENT if it is not a fallback and Iσ_k = IW_k, INC := the number of its other transitions; a λ_W-PHASE of a τ-stretch is a maximal set of its consecutive transitions at whose states the map v ↦ cycle node of W(v) is constant: for every N5 run on every game, every vertex v, every transition k → k + 1 and all states k0 < k1: SET_k ⊆ SET_(k+1), and v ∈ SET_k implies LO_j(v) = W_j(v) = HI_j(v) = LO_k(v) for every j ≥ k (Corollary SETTLE-MON); lcp(CS LO_k(v), CS HI_k(v)) ≤ lcp(CS LO_(k+1)(v), CS HI_(k+1)(v)), so B_k is non-decreasing in [0, n(n + 2)] (Corollary BRACKET-MON); K ≤ (n + 1)(SG + 1) and K ≤ (n(n + 2) + 1)(BG + 1), while SG, BG ≤ K (SETTLE-RED and BRACKET-RED, EQUIVALENCES); with τ := τ_(k0), if τ_j = τ for k0 ≤ j ≤ k1 and every transition j → j + 1 with k0 ≤ j < k1 is consistent, then σ_(k0), …, σ_(k1) are k1 − k0 strategy-changing switch-best steps on G_τ and k1 − k0 < B; hence a τ-stretch has at most (INC + 1)(B − 1) + INC transitions, an EQUIVALENCE with INC (Lemma CONSISTENT-RED): REDUCTIONS and EQUIVALENCES; no count is bounded here; the sandwich is R18 (d)'s, not claimed here; «every λ_W-phase of a τ-stretch has at most n − 1 W-changing transitions» (R17 (c)'s bound transferred) DEAD: experiments/new/box116/inst/fbg_K12_m6_m24.pg (sha1 2f035ca0…) with its repaired start fbg_K12_m6_m24_fixed.start (9f03f81f…, L-NEW box 116b), n = 290, 403 W-changing transitions in one λ_W-phase, 403 > 289, and experiments/n5-epoch/instances/lend107_n32.pg (ab4c9811…) with lend107_n32.start (9df4ea2c…), n = 32, 106 > 31, both checked against L-COMP's n5b and Oink; the premises R17 (F1) and R18 (d) Lemma S (a) rest on derivations written by REFEREE and REFEREE-2 (R17 (a)) (P-N5-GATE, docs/new/P-N5-GATE-box120.md with its fixes entry 1, docs/new/P-N5-GATE-fixes-box120.md; L-NEW successors 43-44). G-N5-TIME stays open.

Addendum 1 (subagent, for the Lead; does not land; written 2026-11-01T03:08:02Z by date -u). (1) BUILT ON LINE L-1 (l-new afb8b99e, sha1 d677161c…), the
line both referees MATCH (REFEREE 22 ffbdc404; REFEREE-2 25 9b30c652). NOT committed, NOT pushed; no other file edited. c9644446 and
ffbdc404 are on the local trunk only (d734f419): push trunk before landing. (2) TITLE l. 348 = "### R101 [refereed-only] " + L-1
without its newline + ", CHECKER PASS (docs/checker/C111.md, checker PENDING)", checked by script after the fill (fill101.py): equal, byte
for byte (True); the only «### R» heading of this file. (3) BODY l. 348-573; GAPS preamble l. 575-582; UPDATE l. 583 (one line, 0
"|", one <HH:MM>, one <checker>; controls True ×4: R97's, R98's, R99's and R100's landed UPDATEs). (4) PINS: from a git archive of afb8b99e
(experiments/, docs/new/), from experiments/new, GIT_DIR set: check.sh l. 1-8 + 616-633 (boxes 117, 118, 120) 02:52:25Z-02:52:27Z, rc 0,
three PASS lines; inphase.py on fbg_K12_m6_m24 02:52:41Z-02:52:54Z, rc 0; box120/pincheck.sh 02:54:03Z-02:55:04Z, rc 0, identical to the
stored pincheck.txt; DATA re-sum 02:56:46Z, rc 0 (116 / 118). (5) QUOTE SWEEP: q101.py (outermost guillemet quotes, whitespace joined, split at the ellipsis; sources: packet, frozen line, L-1, fixes, R-N5-GATE.md at ffbdc404, R2-N5-GATE.md at e35e8280, R2-N5-GATE-L1.md at 9b30c652, REFEREE's strict_lend107.txt, RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, TARGET.md, LEAD-STATE.md, SPEC, setup_oink.sh, C108-C110, check.sh at afb8b99e, my pin outputs, my UPDATE and word diff, commit subjects): to-check notes l. 1-347: 329 quotes, 293 parts of 6+ characters, all found; entry (title + body) l. 348-573: 148 quotes, 151 parts, all found, none found only in my own outputs or commit subjects; GAPS preamble and UPDATE l. 575-583: 8 quotes, 7 parts, all found; this Addendum: 5 quotes, 3 parts, all found. Found only in my own UPDATE (by design): the UPDATE head and the (q2) phrase. Line check: 171 quotes preceded by an l. N, 25 heuristic misses, read by hand: each a table-cell or nearest-l. artefact (the regex takes the packet's line range before a referee cell, or a quote of L-1 after a packet range), none a wrong line. (6) FLAGS FOR CHECKER IN L-1 (no referee made
any REQUIRED): G-1 R18 (d) cited «on every game» (the Lead's flag; the reading is a Lead brief, not a DECISIONS.md entry; landed body
precedents R47, R55, R56); G-2 REFEREE 22's two-colon note; G-3 the L41 clause without «referee-originated»; G-4 Ξ^d and G unglossed;
G-5 «τ-stretch» / «SG» beside R89's / R19's; soft spots D-1 to D-9. Found none of: DATA overclaim, asymptotic DEAD, stale pin, old line as
current. (7) NOT RUN / NOT DONE: the referees' own tools (not re-run); the §7 corpus re-run (the stored box120 outputs were re-summed for
116 / 118 only; INC, SG, BG and the separation rows were not re-summed); L-NEW's box 117 / 118 pincheck.sh (box120/pincheck.sh covers
both DEAD instances); lend107_n32 and fbg_K12 n5b runs beyond pincheck.sh. Scratch files (not committed) are in
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad: R101-template.md, assemble101.py,
fill101.py, fxq101.py, upd101.py / upd101.txt, wdiff101.py / wdiff101.out, sum101.py / sum101.out, q101.py / q101.out, pin101.time / pin101.out
(archafb8/experiments/new/pin101.sh), inph_fbg.time / inph_fbg.out, pc120.time / pc120.out, check_afb8.sh, archafb8/.

Addendum 2 (Lead, 2026-11-01 04:35:46Z by date -u, read in the same command as this edit; for C111 Add. 1): CHECKER C111 E-1 (claude/checker 54645970) applied verbatim: body l. 445 «, not a numbered Lead reading in docs/DECISIONS.md.» → «, now recorded as Lead reading L44 (docs/DECISIONS.md, 2026-11-01 03:17Z), whose conditions (i) and (ii) hold here (above).» (once). No other change; title l. 348, UPDATE l. 583 and the line are unchanged.
