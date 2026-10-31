# Draft RESULTS R97 (Lead, 2026-10-31 00:11:55Z by date -u, read in the same command as the fill of this file; subagent draft; packet, fixes entries 1-3, line files 3101a0c0 / L-1 / L-2 / L-3, both reports, REFEREE's R-N5-SETTLE Addendum 1, both §Cs (REFEREE Part 1 and Part 2), REFEREE's and REFEREE-2's L-3 word-diffs read at the origin heads fetched at the start of this draft, 2026-10-30 23:55:40Z by date -u (l-red 916dac49, referee 8197e182, referee-2 b441f3da, l-si 4f015585, checker ede249b4; origin trunk 4880f3f5, local trunk head 24675af3); pinned «R147» / P-N5-SRC blocks of experiments/red/check.sh re-run 2026-10-30 23:59:06Z-23:59:07Z (0521fb82, 564bef5a); DATA re-summed 2026-10-30 23:59:36Z) — to CHECKER C107
to check: (0) PLACEMENT, R96 PENDING. R97 goes after R96. R95 is LANDED (trunk 2a136552, 2026-10-30 22:14:44Z; CHECKER C105 Add. 1
3c59333c, C105 CLOSED ede249b4). R96 is NOT landed: docs/RESULTS.md at the local trunk head 24675af3 (= origin trunk 4880f3f5) has sha1
7eae120343f6e024872390453cc0f1c8fcdc1658, 8,268 lines, unchanged since 2a136552 (the R95 landing); the last "### R" heading is R95 (l. 7476);
«## Dead ends (kept;» is at l. 7748; «R96» and «R97» occur 0 times in RESULTS.md and in GAPS.md (sha1 d7eb1a0e55b02fc1615b4b7d2e1bd3458eb7d7ef,
23 lines, unchanged since 2a136552). The R96 draft (docs/agents/R96-draft.md, sha1 fd49e5751f1d7fc9b20ae411cf81242596ff403d, 476 lines,
last commit 5e79f732, 2026-10-30 22:01:05Z) still carries SETTLE line L-2 as its title and is held: SETTLE is at line L-4 (l-si b04a1bbb,
docs/si/P-N5-SETTLE-line-L4.txt, sha1 6ed61d848613df4b501b785e9418c3e2c1e8fc43) with REQUIRED SETTLE-L6 / SETTLE-L7 (REFEREE 21,
R-N5-SETTLE-C.md l. 135 at 8197e182, «Verdict on L-4: does NOT yet match. REQUIRED SETTLE-L6 and SETTLE-L7») and SET-L4-1 (REFEREE-2 24,
R2-N5-SETTLE-L4.md l. 43 at b441f3da), so R96 will land with a later SETTLE line (L-5 or after; C106 not yet on claude/checker). Every
RESULTS line number below is at 7eae1203, BEFORE R96; R97's entry is to be inserted after R96's entry, before «## Dead ends (kept;». The Lead
RE-CHECKS (6) (stale labels and names) and (9) (GAPS) at landing against RESULTS / GAPS with R96 in.
(1) TITLE. The title is the line file docs/red/P-N5-SRC-line-L3.txt (l-red 564bef5ad4d3b3397a3281c51105a8b2b92c1a2b,
2026-10-30T23:10:33Z, the file's only commit, sha1 5736d8ab828d8244c6466abbc08d4fa8d8c03b41; identical at l-red head 916dac49, at origin
trunk 4880f3f5 and at the local trunk head 24675af3; first on trunk by c0759f75, 23:25:19Z), verbatim: one line, no outer quotes, no final
period, 3,878 characters (4,037 bytes plus the newline), 746 whitespace tokens. NO HEADING MARKER, verified by script: the file begins «N5
on EVERY game (SPEC S1-S5, under the standing SPEC premise», with no «#», no «R??» and no lane tag (the frozen line 3101a0c0 has none
either; Lead reading L41 «Lanes write line files without a heading marker (C104 N-1).»). So, as in R95 / R96, NOTHING is stripped: the
heading is the level-3 marker, then "R97 [refereed-only] ", then the file without its newline, then the fill. «2026-10-30» occurs exactly
once in L-3, in « (2026-10-30) — a REDUCTION» (by script), so NO date is inserted (the R93-R96 rule). The line holds ten "|": «|V|» once,
«|succ(c)|» once, «|F|» three times; they stay in the heading (R91, R93-R96 carry "|") and are replaced in the GAPS UPDATE only ((9)). The
checker fill ", CHECKER PASS (docs/checker/C107.md, checker PENDING)" is appended as in R90-R96 (no space before the comma); L-3 ends «…
fixes docs/red/P-N5-SRC-fixes.md entries 1-3)», so the heading ends «… entries 1-3), CHECKER PASS (…)». Built by script (scratch
build97.py: assert the sha1 5736d8ab…, one line, no marker, one «2026-10-30», ten "|"; prepend "### R97 [refereed-only] ", append the fill)
and re-checked after writing this file: equal, byte for byte. Heading: 3,956 characters, 4,115 bytes; sha1 of the heading line
without its newline b2523121c1b3e98e1ae2b5a2e10a80ede32c5e7d, with its newline 2251663c5312caea7f22cf7d20554c5e5558ad3d.
Title features shared with R96 (no new precedent): a source parenthesis after the scope tail «(P-N5-SRC, docs/red/P-N5-SRC.md; L-RED
successor 35; fixes docs/red/P-N5-SRC-fixes.md entries 1-3)»; a referee-originated proof named in a proof note with both signatures, and the
scope tail saying so (R94's FLAT-SW / SW-KEEP, L41). One feature without a precedent: the scope tail carries a DATA statement, «and are not
O(1) per W-run: pins xcn4_n12, cn3_n9» (DOUBT D-1, (7)).
(2) LINE HISTORY: frozen 3101a0c0 (docs/red/P-N5-SRC-line.txt, l-red 0521fb82, 3,422 characters, 677 tokens, no marker, one date; the line
both reports reviewed) → L-1 059d2733 (…-line-L1.txt, 6e323e0a, 22:32:34Z, 702 tokens; fixes entry 1 from the Lead's relay of REFEREE-2's
items, SUPERSEDED, never word-diffed by a referee) → L-2 9fcb5790 (…-line-L2.txt, 77a6d979, 22:48:45Z, 705 tokens; fixes entry 2, the
report's own wording) → L-3 5736d8ab (564bef5a, 23:10:33Z, 746 tokens; fixes entry 3). 3101a0c0, L-1 and L-2 are history, not the title.
Each line file has one commit (git log on l-red), and L-1 / L-2 / L-3 are byte-identical to their copies in the fixes file (l. 27, l. 63, l.
85; by script). Word diffs measured for this draft (difflib over whitespace tokens, scratch wdiff97.py):
- 3101a0c0 → L-1: 677 → 702 tokens, 4 non-equal opcodes: «H_t);» → «H_t, H_t := S4a's arena at t (Even keeps σ_t ∪ Iσ_t, Odd follows
  τ_t));» (E1.2); «it:» → «it, with |F| its number of transitions:» (E1.1); «source» inserted before «events,» (E1.3); «35)» → «35; fixes
  docs/red/P-N5-SRC-fixes.md entry 1)». = fixes entry 1 l. 22 («L-1 = the frozen line with these four replacements and nothing else»).
- L-1 → L-2: 702 → 705 tokens, 6 non-equal opcodes: «S4a, σ_new» → «S4a at a transition k → k + 1, σ_(k+1)» and «H_t, H_t := … τ_t));» →
  «H_k);» (E2.2, SRC-L2 in REFEREE-2's form); «|F| := the number of transitions of F;» inserted after E^S_F's definition and the quantifier
  restored to «it:» (E2.1, SRC-L1); «events,» → «events (unless they change Ξ at a source),» (E2.3, N-1); «entry 1)» → «entries 1-2)».
  = fixes entry 2 l. 34-35 («L-1 with the four replacements below, and nothing else»; the opcode count is 6 because E2.1 and E2.2 each touch
  two places).
- L-2 → L-3: 705 → 746 tokens, 4 non-equal opcodes: «|V|,» → «|V| (V the vertex set of the game),» (E3.2, REFEREE's precision); after
  «restricted to Even vertices outside C,» the insertion «with Case 2 and Case 2b's comparison step by (Lemma ONE-STEP, REFEREE-2 R2-N5-SRC
  §3.2, claude/referee-2 e8c1b62d; signed by REFEREE, claude/referee 8951ef7c), which closes gap G-SRC-1 (REFEREE R-N5-SRC §3, claude/referee
  81f6b89c),» (E3.1, SRC-L3); «cn3_n9)» → «cn3_n9; Lemma ONE-STEP is referee-originated)» (E3.1 scope tail, L41); «1-2)» → «1-3)». = fixes
  entry 3 l. 69-70; = REFEREE §C (8197e182) l. 131-138 («Nothing else changed.»); = REFEREE-2 R2-N5-SRC-L3.md l. 13-19 («(705 → 746
  tokens): four changes, nothing else»).
- 3101a0c0 → L-3: 677 → 746 tokens, 8 non-equal opcodes, the union. No inequality and no quantifier of a claim clause changes: PLAY-CAUSE^S,
  the source-block clause, TAIL, SRC-SETTLE's «k1 − k0 ≤ (n − 1) + m_C» and SRC-COUNT's «|F| ≤ E^S_F + (E^S_F + 1)(n − 1 + m_C)» are
  token-identical in 3101a0c0 and L-3; the changes are the R57 gloss (k, σ_(k+1), H_k), the |F| definition, V named, the ONE-STEP proof note,
  the scope tail and the source note.
(3) THE LINE AT BOTH REFEREES. L-3 (the title): REFEREE successor 21, docs/referee/R-N5-SRC-C.md, section «## Line revision L-3 (…)» l.
130-147 (added by 8a1ba423, 2026-10-30T23:37:41Z; its stamp corrected «23:40Z» → «23:37Z» by 8197e182, 23:37:49Z, +1/−1): l. 130 names
the file, l-red 564bef5a, sha1 5736d8ab… and fixes sha1 f8d54eec…; l. 138 «Nothing else changed.»; l. 144 «No free symbol.»; l. 145 «L41:
the line cites both signatures (author REFEREE-2 e8c1b62d; REFEREE 8951ef7c), and the scope tail says it is referee-originated. ✓»; l. 147
«Verdict on L-3: MATCHES SRC-L1, SRC-L2, SRC-L3 and N-1 (Opus 5.5, D15). No REQUIRED change remains on the SRC line.» REFEREE-2 successor
24, docs/referee-2/R2-N5-SRC-L3.md (new file at 0f7f3010, 23:27:02Z; table escapes and «five» → «four» changes in §1 by b441f3da,
23:27:18Z, +2/−2; 25 lines, sha1 569fb407e84d7fa2ce00daab7921af7615eeac8b): l. 2 «sha1 5736d8ab828d8244c6466abbc08d4fa8d8c03b41 (re-hashed:
match)»; l. 20 «No free symbol.»; l. 24-25 «L-3 (5736d8ab): **MATCHES** (Opus 5.5, D15). No required change. Every SRC line item of both
referees (SRC-L1, SRC-L2, SRC-L3, N-1 and REFEREE's V) is closed.» Both optional: «by (Lemma ONE-STEP, …)» would read better as «by Lemma
ONE-STEP (…)» (REFEREE l. 146; REFEREE-2 l. 21); not applied, no change proposed. 8a1ba423, 8197e182, 0f7f3010 and b441f3da are on the
LOCAL trunk only (merges 73feb559 and a1379017, 23:55:24Z), not on origin trunk 4880f3f5 at the start of this draft.
Earlier lines: 3101a0c0: REFEREE R-N5-SRC.md l. 23 «REQUIRED CHANGES: SRC-L1 (|F| undefined), SRC-L2 (t free in the R57 gloss «H_t»). … Precision
SRC-L3 (§8)», l. 116 «Verdict: MATCHES the signed items once SRC-L1 and SRC-L2 are applied.»; REFEREE-2 R2-N5-SRC.md l. 18 «REQUIRED changes
SRC-L1, SRC-L2, SRC-L3 (§6)», l. 167 «Line: REQUIRED SRC-L1, SRC-L2, SRC-L3; N-1 is optional.» Joint REQUIRED set (REFEREE §C Part 2 l.
83-86): SRC-L1 (|F|), SRC-L2 (t free, σ_new unbound), SRC-L3 (ONE-STEP cited, scope tail referee-originated). SRC-L3 was precision for
REFEREE (l. 109-111) and REQUIRED for REFEREE-2 (l. 146-152); REFEREE upgraded it (§C Part 1 l. 17 «I agree it is REQUIRED: the cited
induction is signed only through ONE-STEP. Upgraded»; Part 2 l. 56 «I upgrade it to REQUIRED.»), so no ruling was needed (Part 2 l. 116);
the Lead had also ruled REQUIRED (LEAD-STATE 23:25Z «SRC-L3 REQUIRED (REFEREE-2) vs precision (REFEREE) → Lead ruling REQUIRED»). L-2:
REFEREE §C Part 2 l. 104 «Verdict on L-2: MATCHES SRC-L1, SRC-L2 and N-1 (Opus 5.5, D15).»; REFEREE-2 checked 3101a0c0 → L-2 only inside
its L-3 file (l. 5-11, «not diffed by me before; checked here»). L-1 was never given a referee verdict (superseded by L-2 within 16
minutes).
(4) CLAIMS SIGNED = the items below, each SIGNED in BOTH referees' verdict tables (REFEREE "## Verdicts" l. 14-23 of R-N5-SRC.md; REFEREE-2
"## 1. Verdict table" l. 9-18 of R2-N5-SRC.md), in REFEREE-2's §C table (C.1 l. 7-15) and in both REFEREE §C cross-maps (Part 1 l. 8-19;
Part 2 l. 44-58), AND stated by L-3. The brief's list was checked item by item against L-3's clauses:
| item (packet §, lines) | REFEREE (successor 20) | REFEREE-2 (successor 24) |
| --- | --- | --- |
| (a) Lemma PLAY-CAUSE^S (§2, l. 56-82; statement l. 57-58) | R-N5-SRC.md l. 18 «SIGNED»; §2 l. 25-33; §C P1 l. 11, P2 l. 47 «agree» | R2-N5-SRC.md l. 13 «SIGNED» / «none»; §2 l. 25-36 «✓ SIGNED.»; l. 163; §C C.1 l. 11 «SIGNED by both» |
| (b) (S_j), (X_j) on source blocks (§3, l. 84-110; statement l. 85-87): the line's «(source blocks)» clause | l. 19 «SIGNED. One sub-case is omitted from [SET] §5 Cases 2 and 2b, which this packet reuses: GAP G-SRC-1, closed here (§3).»; §3 l. 35-61; R-N5-SETTLE.md Add. 1 l. 185; §C P1 l. 12, P2 l. 48-50 | l. 14 «SIGNED, with G-SRC-1 closed by my Lemma ONE-STEP (§3.2)» / «G-SRC-1 (inherited from [SET] §5 Case 2 / 2b)»; §3 l. 38-92; l. 164; §C C.1 l. 12 «SIGNED by both; G-SRC-1 found independently by both, closed (C.2)» |
| (c) Lemma TAIL (§4, l. 112-141; (T0) l. 114, (T1) l. 115) | l. 20 «SIGNED»; §4 l. 63-76; §C P1 l. 13, P2 l. 51 | l. 15 «SIGNED» / «none»; §4 l. 94-110 «SIGNED, no gap.»; l. 165; §C C.1 l. 13 |
| (d) Theorem SRC-SETTLE (§5, l. 144-156) | l. 21 «SIGNED»; §5 l. 79-83; §C P1 l. 14, P2 l. 52 | l. 16 «SIGNED (rests on §3)» / «none of its own»; §5 l. 113-117; l. 166; §C C.1 l. 14 |
| (e) Corollary SRC-COUNT and the EQUIVALENCE (§5, l. 157-162) | l. 21 (same row); l. 84-85 «SRC-COUNT ✓» / «Equivalence ✓»; §C P1 l. 14 | l. 16 (same row); l. 118-122; §C C.1 l. 14 |
The (S_j) of (b) is the packet's statement name; it is not the line's source set S_k. (d): the line states SRC-SETTLE for «every maximal
run … of source-free transitions», the packet for every source block; both referees call the line's form the narrower one (REFEREE §8 l.
103-104 «a narrowing … which is acceptable»; REFEREE-2 §5 l. 123; REFEREE §C P1 l. 14). (c): the line states (T1) as «σ_(k+2)(x) =
σ_(k+1)(x) for every Even x ∉ C whenever k + 1 → k + 2 is a transition of F», the packet adds «it is C-only», which follows; nothing wider.
Joint gap maps: REFEREE §C Part 1 l. 22-23 «Packet items to sign: no open gap. G-SRC-1 (inherited from [SET]) is CLOSED by ONE-STEP, which is
signed by both referees (REFEREE-2 as author, mine in R-N5-SETTLE Addendum 1). Nothing FALSE.»; Part 2 l. 77 «Packet items to sign: no open
gap on either side. Nothing FALSE.»; REFEREE-2 §C l. 47-48 «G-SRC-1 is closed by two independent repairs, each signed by the other referee;»
«joint gap map: EMPTY after closure; G-SRC-1 is recorded as found and CLOSED.», stated (l. 46) «once REFEREE's explicit verdict on my
ONE-STEP arrives». That verdict exists (8951ef7c, 22:47:50Z) and predates REFEREE-2's §C commit (824651dd, 22:56:32Z), which still says
(l. 69) «REFEREE's verdict on my ONE-STEP is pending»; REFEREE-2 records it later in R2-N5-SRC-L3.md l. 17 «8951ef7c holds REFEREE's
ONE-STEP signature (R-N5-SETTLE.md Addendum 1 (2))», and REFEREE Part 2 l. 113-115 «That verdict is SIGNED … G-SRC-1 is CLOSED, and the
joint gap map is EMPTY of open gaps.» The only REQUIRED items of either referee are LINE items (SRC-L1, SRC-L2, SRC-L3), all closed in L-3.
L41 APPLIES to (b): the line's proof note rests Case 2 and Case 2b's comparison step on Lemma ONE-STEP, a referee-originated proof. Its
author REFEREE-2 24 signs it in its report (R2-N5-SRC.md l. 66 «**Lemma ONE-STEP** (REFEREE-2 24, PROVED).»; l. 164 «§3 (S_j)/(X_j), C1-C7:
SIGNED with G-SRC-1, closed by my Lemma ONE-STEP.»); the OTHER referee independently checks and signs it (REFEREE successor 20,
R-N5-SETTLE.md Addendum 1 at 8951ef7c, l. 163-164 «(2) Lemma ONE-STEP (REFEREE-2 24, docs/referee-2/R2-N5-SRC.md §3.2, claude/referee-2
e8c1b62d, confirmed an ancestor of origin): SIGNED (Opus 5.5, D15).», with «My check.» l. 167-174 and the instantiations l. 178-184); the
joint gap map is quoted above; the scope tail reads «Lemma ONE-STEP is referee-originated». REFEREE found G-SRC-1 before seeing ONE-STEP
(R-N5-SRC.md l. 9 «I opened no docs/referee-2/ file for this packet.»; Add. 1 l. 156-157 «written before I saw REFEREE-2's R2-N5-SRC or
the Lead's 22:29Z message») and closed it with its own four-way split (R-N5-SRC §3 l. 48-58), which REFEREE-2 SIGNED (R2-N5-SRC-C.md l. 41
«**Verdict on REFEREE's G-SRC-1 closing argument: SIGNED (Opus 5.5, D15).** No gap. No FALSE step.»). So G-SRC-1 has two cross-signed
referee-originated repairs (as R94's SW-KEEP / OWN); the line relies on ONE-STEP only («ONE-STEP is the proof of record (Lead reading L41)»,
REFEREE §C Part 1 l. 12). ONE-STEP's statement is NOT in the line and does NOT land as a claim (the line does not define ⊕, which it would
need: REFEREE §C Part 2 l. 108); it lands as the named proof step of (b).
Signed by both, NOT stated by L-3, so NOT landed: (R1), (R2) and the NEW definitions as statements (§1, «CHECKED» / «checked ✓»: REFEREE l.
17, REFEREE-2 l. 12); Lemma ONE-STEP and REFEREE's four-way split as statements (proof steps of (b), above); TAIL's «it is C-only» (implied);
SRC-SETTLE's normal-part / tail decomposition (proof). Quoted from [SET], NOT re-signed here (packet §0 l. 22): [SET] §1, §3 Claim RG′, §4
W-MON and PATH, §5 Cases 1-2c; they are R96's material (RG′ and RUN-SETTLE land there). What does NOT land at all: §6 F1, F2 (READING;
«not signed», REFEREE l. 22; REFEREE-2 l. 17 «not signed (READING); not used in §2-§5: confirmed»); §7 DATA and pins; §5 l. 163-165
«Against [SET] §6 HEAD-RED and L-SI box 53's HEAD-RED′ (READING, not to sign)»; the residual, max HXS_F polynomial (the Lead's freeze word
«HXS-POLY», packet l. 3), which is OPEN; R147's other text (docs/red/R147-xcn.md, l-red 47fd9163; the packet governs, l. 7).
(5) OTHER LANES' TEXTS THE PACKET DEPENDS ON (packet §1 l. 26-41), checked for this draft by script (scratch q97.py: every outermost «…»,
whitespace joined, «…» elisions split): 9 quotes in l. 26-41, all found, in [SET] = docs/si/P-N5-SETTLE-box52.md @ l-si 6a70a520 (sha1
aef403c3d8a003bcfc6742c4d1da084a1e21669f; R96's object), L-RED R140 docs/red/R140-friedmann-port.md @ 47000632 and SETTLE L-2 (86becaa0);
and 30 quotes in §2's word-diff (l. 76-82) and §3's change list (l. 88-109): 17 found verbatim in [SET]; 12 are the packet's new
right-hand sides (e.g. «S_j ⇒ X_j by PLAY-CAUSE^S», «(MIN) No Even u ∉ C with ℓ_(k+1)(u) < L switches at k.»); 1, the old side «Ξ(y_(i+1)),
y_(i+1) ∈ U_(k+1)», joins two [SET] fragments (l. 131 «Ξ(y_(i+1))», l. 135 «y_(i+1) ∈ U_(k+1)») and is not one verbatim string. REFEREE l. 10-11
«the [SET] pieces in §1 are those I quote-checked for R-N5-SETTLE: verbatim, and ARENA-MAX verbatim at 47000632. The word-diff lists of §2
and §3 match [SET] §4 and §5 as I read them.» The packet reuses [SET]'s §5 induction («quoted there in full», l. 88) through the seven
changes C1-C7 and «Why no other step changes» (l. 103-109); both referees checked C1-C7 (REFEREE l. 36-41; REFEREE-2 §3.1 l. 40-50). L-LIT
T54 IDX-MONO / LEX-BFS (as quoted in [SET] §2) are used in §3 Case 2a and, NEW here, in §4 (T1) at two consecutive evaluations; both SRC
referees checked that use (REFEREE §4 l. 69-75; REFEREE-2 §4 l. 102-109, its tool «checks … IDX, LEX»); not landed (see D-3).
(6) PREMISE LABELS (stale-label test; RESULTS at 7eae1203, see (0)). RESULTS labels in L-3 (by script): «R57» 2, «R15» 2, «R89» 1; «R140»
is an L-RED report number, «T54» L-LIT's, «R2» only inside «R2-N5-SRC» (a file name); none of these is a RESULTS label. Every RESULTS label
exists and carries the named item:
- R57 (l. 2893): the standing SPEC premise; L-3's gloss begins «(1E-N3: S1's procedure realises the pointwise optimum;», which occurs in
  RESULTS at R91 (l. 6384), R93 (l. 6972) and R95 (l. 7476) (by script), and continues with its own form «for S4a at a transition k → k + 1,
  σ_(k+1) is the pointwise optimum of the one-player arena H_k)» (REFEREE-2's SRC-L2 text; 0 occurrences in RESULTS; the R91-R95 form is
  «for S4a, σ_new is … H_t, H_t := …»). «the R57 premise above» in the proof note refers to it.
- R15 (l. 624): (a) Lemma A l. 631, (d) l. 640.
- R89 (l. 5854): «a maximal run of consecutive states of one τ-stretch none of whose transitions is an S4c fallback or changes λ_W» —
  verbatim in R89's title (by script: 1 occurrence, l. 5854) and in L-3's W-run parenthesis.
- NOT a RESULTS label but RESULTS-shaped: «RESULTS line L-2, l-si 86becaa0» in the proof note names SETTLE's line revision L-2, which will
  NOT be R96's title (see (0)); DOUBT D-2, (7). L-3 does NOT cite «RESULTS R96» («R96» 0 times; by script).
- Name check against landed text (RESULTS / GAPS at 7eae1203 / d7eb1a0e): «PLAY-CAUSE^S», «SRC-SETTLE», «SRC-COUNT», «ONE-STEP»,
  «G-SRC-1», «HXS», «m_C», «C-ONLY», «SOURCE EVENT», «source block», «P-N5-SRC» occur 0 times in both. «TAIL» as a word occurs 16 times in
  RESULTS and 3 times in GAPS: landed R39's Lemma TAIL (title l. 1862 «(FREEZE-STEP, TAIL)», body l. 1881 «TAIL: from»; GAPS l. 11, R39's
  UPDATE) and compounds (LEN-TAIL, RHO-TAIL, TAIL-DISJOINT). A NAME CLASH, not inside the title: R97's «(Lemma TAIL)» is defined by its own
  clause; R39's TAIL is a different statement about one-Odd-choice games (DOUBT D-4; the entry says so under Setting). «D_k := {Odd o :
  σ̄_k(o) ≠ τ(o)}» has the meaning of landed R92's «D_s» (l. 6656).
- R96 (pending) will add «RUN-SETTLE», «Claim RG′», «HEAD-RED», and, if its line keeps SETTLE L-4's citation, «ONE-STEP» (with the same SHAs
  e8c1b62d / 8951ef7c). AT LANDING (R96 in): re-run the grep for «R97», «PLAY-CAUSE^S», «SRC-SETTLE», «SRC-COUNT», «HXS», «m_C», «G-SRC-1»
  and «ONE-STEP» in RESULTS and GAPS; check that R96's ONE-STEP citation (if any) names the same commits; check whether R96's title is still
  anything called «line L-2» (D-2). The R96 draft lists «L-RED R144-R147 (incl. R147 SRC-SETTLE, 47fd9163)» as excluded work (R96-draft l.
  261), so R96 claims nothing of this entry.
(7) SYMBOL TEST of the title (my own strict test of every symbol of L-3, by hand; IN = bound in the line; else the carrier):
| symbol | where |
| --- | --- |
| N5, SPEC S1-S5, «Even», «Odd», S4a, S4c, [S1-val], Ξ_{σ_k} | SPEC (named) |
| standing SPEC premise of RESULTS R57 (1E-N3); R15 (a), (d); R89 | cited premises, each a landed RESULTS item; see (6) |
| k, σ_(k+1), H_k in the R57 gloss | k IN («at a transition k → k + 1»); σ_(k+1) IN by «a run is the sequence of states (σ_k, τ_k)» (later in the line); H_k IN, defined later «for a state k of F» (REFEREE §C P2 l. 99-103: «a forward reference to a defined symbol»). Soft spot: the gloss ranges over every S4a transition of the run, H_k is defined «for a state k of F»; every state lies in exactly one W-run (R89's W-runs cut the run at τ-changes, S4c fallbacks and λ_W-changes), whose τ is τ_k, so H_k is defined at every state |
| run, states, σ_k, τ_k; transition k → k + 1; «y switches at k» | IN |
| n, V | IN: «n := \|V\| (V the vertex set of the game)» (SRC-L3 precision, E3.2); = TARGET.md §1 l. 8 «n = \|V\|» |
| m_E; succ(v) | IN; m_E ≤ TARGET's m |
| values (c, P, ℓ), cycle node, path set, length; ⊴, ◁, ⊵, ▷ | IN («as in SPEC S1»); ⊕ does not occur in L-3 (not needed: ONE-STEP is not stated) |
| Ξ_k, σ̄_k, Iσ_k; (y, z) in Iσ_k's set | IN («for a state k: …»; set-builder variables) |
| W-run F; τ-stretch, S4c fallback, λ_W, W in «the cycle-node map of W» | R89 (cited: «RESULTS R89's (…)»); W there is R89's W_t, equal to the line's W_k on F (soft spot, as in R96) |
| τ, C | IN («with τ and C := {v : λ_W(v) = v} fixed on F») |
| W_k, ℓ_k(x), D_k (o), H_k (v) | IN («for a state k of F: …») |
| S_k, SOURCE EVENT, SOURCE-FREE, C-ONLY | IN («for a transition k → k + 1 of F: …»; «for some v ∈ S_k») |
| E^S_F, \|F\|, HXS_F(v), m_C | IN (the four definitions; \|F\| by SRC-L1, E2.1). Soft spots: m_C depends on F through C and carries no F subscript; E^S_F, \|F\|, HXS_F, m_C are defined before the global binder, with F the W-run named in «W-run F := …» (as R96); «\|succ(c)\|» is the cardinality of succ(c) (notation, as \|V\|) |
| global binder | «for every N5 run on every game and every W-run F of it:», which every claim clause follows |
| PLAY-CAUSE^S: k, x, y, λ_W(x), ℓ_(k+1) | IN («if k → k + 1 is a source-free transition of F and x is a vertex …»; «some Even y ∉ C switching at k»); k + 1 is a state of F |
| source blocks: k0, k1, k, v | IN («if the transitions k0, …, k1 − 1 of F are all source-free, then for k0 ≤ k < k1 every Even vertex v ∉ C … and every vertex v …»); «Ξ changes at k» unsubscripted = Ξ_(k+1)(v) ≠ Ξ_k(v), by use (soft spot, as R96) |
| proof note: RUN-SETTLE, «Case 2», «Case 2b», ONE-STEP, G-SRC-1, Claim RG′, ARENA-MAX, R140, T54, LEX-BFS / IDX-MONO, W_(k+1), SHAs | names with sources, not claim symbols; «Case 2», «Case 2b» are the cited induction's cases (REFEREE §C l. 141); every cited SHA is on origin (REFEREE §C l. 142-143; re-checked: e8c1b62d, 8951ef7c, 81f6b89c, 6a70a520, 86becaa0, 47000632 all ancestors of their origin branch heads) |
| TAIL: k, x; H_(k+1) ⊆ H_k «arena by arena»; σ_(k+2) | IN; «arena by arena» = H_(k+1)(x) ⊆ H_k(x) for every Even x (packet l. 119; soft spot); σ_(k+2) is a run state, read only «whenever k + 1 → k + 2 is a transition of F» |
| SRC-SETTLE: k0, k1 | IN («every maximal run k0, …, k1 − 1 of source-free transitions of F») |
| SRC-COUNT: Σ_(v ∈ V), max_(v ∈ V), «for every v», «polynomially many», «polynomial over all W-runs F» | IN (ranges); «polynomial» in the game size, by use (soft spot, as R96); F re-quantified «over all W-runs F» inside the global binder, harmless (as R96's HEAD-RED) |
| scope tail: G-N5-TIME, M3, step-4, TARGET.md, «σ̄-changes, switches at C and σ̄-changes at own Ξ-cycle nodes», «O(1) per W-run», pins xcn4_n12, cn3_n9 | GAPS l. 11, NOW, TARGET.md; pins = experiments/red/xcn/instances/{xcn4_n12,cn3_n9}.pg + .start (no path in the line); «not O(1) per W-run»: DOUBT D-1 |
A mechanical binder-presence check (each IN symbol's binding phrase occurs in L-3: scratch symcheck97.py, 35 pairs) gives «binders missing
0»; it cannot see clause scope; the test of record is the hand test. Agreeing tests: REFEREE R-N5-SRC.md §8 l. 112-115 (frozen
line: «run, transition, … m_C are all bound;», «k0 and k1 are bound in their clauses; x and y are bound in PLAY-CAUSE^S; v is bound in its
clauses»); REFEREE-2 §6 l. 155-159 («No other free symbol.»); REFEREE §C P2 l. 98-103 (L-2's new tokens) and l. 139-144 (L-3's);
REFEREE-2 L3 l. 20.
DOUBTS for CHECKER (neither referee raised them; I propose no line change; CHECKER decides whether any is an E-item):
D-1 «and are not O(1) per W-run: pins xcn4_n12, cn3_n9» (scope tail). Read literally, «not O(1)» is an asymptotic claim (no constant
bounds these counts per W-run over all games); two finite pins cannot show it, and packet §7 (l. 174-192, «DATA, pins», NOT to sign) is its
only source (l. 192 «These show that the dropped terms are not O(1) per W-run»). The lane's own meaning is that they repeat in one W-run: R147
l. 1 «XCN and CN do repeat in one W-run (4 and 3 at one vertex, n ≤ 12). No super-linear family was built.»; l. 147 «Nothing here shows
them super-linear.» Both referees re-ran the two pins (REFEREE §7 l. 97-100; REFEREE-2 §5 l. 134), and my re-run reproduces them
((10)): xcn4_n12 has 4 own-node σ̄-flips at one Odd vertex in a W-run of 4 transitions; cn3_n9 has 3 CN switches at one c, E^S_F = 0. What
the pins show is "not at most one per W-run", not "not O(1)". It is in the scope tail, not a claim clause, and no claim uses it. If CHECKER
requires it, a one-phrase revision L-4 = L-3 with «and are not O(1) per W-run: pins xcn4_n12, cn3_n9» → «and can repeat in one W-run (pins
xcn4_n12, cn3_n9: 4 and 3 at one vertex)» would close it (occurs once; the GAPS UPDATE carries the same phrase and would take the same
replacement).
D-2 «(l-si 6a70a520, signed; RESULTS line L-2, l-si 86becaa0)» in the source-block proof note. It does not cite «RESULTS R96», so R97 has
no textual dependence on R96's label. But «RESULTS line L-2» names SETTLE's proposed line revision L-2 (docs/si/P-N5-SETTLE-line-L2.txt,
sha1 1fcb33c5…), which is superseded (SETTLE L-3 a79d33db, L-4 b04a1bbb; L-5 pending) and will not be R96's title. Read as «the proposed
RESULTS line, revision L-2, at l-si 86becaa0», it is an immutable pointer (file at a SHA), correct but superseded; read as «the RESULTS line»,
it names text RESULTS will not contain. RUN-SETTLE's statement is the same in L-2 and L-4 (SETTLE's later revisions bind σ_new and add the
ONE-STEP citation / L41 tail). If CHECKER requires it, «RESULTS line L-2, l-si 86becaa0» → «RESULTS R96» (only after R96 has landed) or →
«line L-2, l-si 86becaa0» (any time) would close it; either needs a word-diff from both referees.
D-3 TAIL's proof dependences are not named at TAIL. Packet (T1) (l. 126-141) uses ARENA-MAX at k and at k + 1, Claim RG′ and T54
IDX-MONO / LEX-BFS «read at the evaluations of H_k and of H_(k+1)»; the line names these only in the source-block proof note, as «L-LIT T54's
LEX-BFS / IDX-MONO as signed in that packet's review» (SETTLE's review signed them «as used in Case 2a»: R-N5-SETTLE.md l. 26; R2-N5-SETTLE.md
l. 17). The (T1) use is signed in the SRC reports themselves (REFEREE §4 l. 69-75; REFEREE-2 §4 l. 99-109). TAIL's clause carries no proof
note. A soft spot (no clause is wider than signed); recorded under Honest limits.
D-4 NAME CLASH «Lemma TAIL» with landed R39's TAIL ((6)). No change proposed; the entry's Setting says which TAIL is meant.
Other soft spots, as in landed titles (R96 list): the R57 gloss's k over every S4a transition (covered, above); m_C without F; σ̄, Ξ
unsubscripted in «Ξ changes at k» and in the scope tail; «arena by arena»; «polynomial» without p(n); «W» in R89's W-run parenthesis; the
re-quantified F in the equivalence.
(8) FIXES AND STATUS NOTES (fixes file; recorded under Fixes): entries 1-3 are LINE items only; each says «No TO-SIGN item of the frozen
packet changes.» (l. 10, l. 34, l. 69). The fixes file's quotes were checked for this draft by script: entry 2's quotes of REFEREE-2 (l.
30-33 the verdict rows, l. 38-39 SRC-L1, l. 43-45 SRC-L2, l. 51-52 N-1, l. 55-58 SRC-L3) are all found in R2-N5-SRC.md (e8c1b62d); entry
3's quote of REFEREE (l. 76-77, SRC-L3 precision) is found in R-N5-SRC.md (81f6b89c); entry 3 l. 67-68's «Case 2 = ONE-STEP(t=k-1, z=b),
Case 2b = ONE-STEP(t=k, z=a)» is from 8951ef7c's commit message (found there), as the entry says. Not found as quotes: the Lead's words
(entry 1 l. 4, l. 13, l. 16-17, l. 20; entry 2 l. 29 «e8c1b62d is now on origin …»; entry 3 l. 65; messages, not on file). Entry 1 says
its item texts are «the Lead's relay, quoted verbatim from the Lead's message, NOT from the report» (l. 7-9); entry 2 replaced them by the
report's wording (l. 40, l. 46). Entry 1 l. 23-24 planned SRC-L3 for L-2; it went into L-3 (entry 2 E2.4 l. 59).
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-3 states no CONJECTURE. A line-11 UPDATE is proposed at the end, to go AFTER R96's UPDATE
(pending; R96-draft l. 476); at present the last UPDATE on l. 11 is R95's («UPDATE 2026-10-30 22:14Z: RESULTS R95 (P-N5-WRUN; CHECKER C105
3c59333c) …»; l. 11 holds 76 "|"). Built by script (build97.py) from L-3's clauses only, with R94's-R96's construction: «LANDED: » + the
title body with each clause label moved behind its clause («(source blocks)» behind its proof note, two parentheses in a row, as R96's
RUN-SETTLE); the scope tail « (2026-10-30) — a REDUCTION (X) (source)» → «: a REDUCTION; X′ (source). G-N5-TIME stays open.», X′ = X minus
«G-N5-TIME stays OPEN» and «not M3, not a step-4 pass, not a TARGET.md claim» (R94-R96 drop both); the source parenthesis is KEPT, before the
final sentence (as the R96 draft). The UPDATE must hold no "|" (l. 11 is a table row); L-3 holds ten, so these replacements were made, which
are NOT title text: (r1) «n := |V| (V the vertex set of the game)» → «n := the number of vertices of V (V the vertex set of the game)»; (r2)
«Σ_(Even c ∈ C) (|succ(c)| − 1)» → «Σ_(Even c ∈ C) (the number of successors of c, minus 1)»; (r3) the definition «|F| := the number of
transitions of F; » deleted (every use is spelled out); (r4) «|F| ≤ E^S_F» → «the number of transitions of F ≤ E^S_F»; (r5) «HXS_F(v) ≤ |F|»
→ «HXS_F(v) ≤ the number of transitions of F» (R93-R96 wording for |F|). Checked by script: with the five labels removed from both and
(r1)-(r5) undone, the UPDATE equals the title body up to the tail (string equality); the tail equals the rule above; no "|". The UPDATE's
stamp is a placeholder «<YYYY-MM-DD> <HH:MM>Z» (the landing will be on 2026-10-31 or later; the title's own «(2026-10-30)» is dropped by
the tail rule, so the UPDATE holds no date until the fill); if CHECKER takes D-1, the UPDATE takes the same replacement.
(10) DATA of record = the packet's §7 (l. 174-192). Re-summed for this draft (python3 -I, scratch sum97.py over
experiments/red/xcn/src_corpus.txt from the 0521fb82 archive, sha1 7b21c28fa024e70848dc1e881d011a701e130e96, 1,132 rows; identical at
564bef5a (cmp); 2026-10-30 23:59:36Z by date -u, rc 0): 1,130 rows parsed, 2 RUN-ERROR (red/n3/instances/n3cov_phi, n3cov_lean: «RUN-ERROR
edge 0->-1 out of range»; = packet l. 180 «the invalid starts of L-RED R99»); VIOL 0, VIOL2 0, TAILV 0, BLKV 0, CNOX 0; source events (Es2)
4,546 against R143-style events (E) 4,724 (= packet l. 182); longest source block (maxblk2) 67 (red/usplit/instances/gate_K64_n581, n 581,
src_corpus.txt l. 428, the sbcg list, i.e. the default best-reward start; the same game from its .start (l. 1077): 5); longest C-only tail 1
(4 rows: tog6a_n32, tog6b_n32, each in both lists). Tool note: srcsettle.py's «Es2» is E^S_F (its docstring l. 9 «Variant S2 (no CN
event): EVENT^S2 := (iii^src) only»); its «Esrc» (4,554) also counts CN switches as events and is not E^S_F. Random games
(xcn/srcrand_out.txt, sha1 b423d0a90c0cab62ad325ea635a2e8209cf07687; seeds 11-14, 2,500 games each, n 6-14): VIOL 0, VIOL2 0, TAILV 0, BLKV
0, CNOX 0 in all four; maxL ≤ 3 (= packet l. 185-186 «all four counters 0», «random W-runs are short (|F| ≤ 3)»).
SOURCE-BLOCK RECONCILIATION (67 / 63): the rank order of source blocks in src_corpus.txt is 67 (gate_K64_n581, n 581), 63
(si/runlin/instances/runfam_K40, n 79, l. 532), 58 (new/box52/out/topfix_n10), 55 (red/xing/instances/x32_rand64, in both lists), 52
(red/so/instances/xsnf52_n64). On n ≤ 100 the longest is 63 (runfam_K40). REFEREE: «Longest source block 63 (n ≤ 100; the packet's 67 is
gate_K64_n581, n 581, outside my MAXN).» (R-N5-SRC.md l. 95); REFEREE-2: 67 on sbcg.lst (gate_K64_n581), 49 on alt_all with start
(ladderd0_k48_n156), 55 on alt_all start-less (x32_rand64) (R2-N5-SRC.md l. 130-132; per-list maxima, not a top three), «These equal the
lane's maxima: block 67 on gate_K64_n581» (l. 135); REFEREE §C P2 l. 70-73 «REFEREE-2: 67, on gate_K64_n581 (n 581).», «Mine: 63 at n ≤ 100.»,
«This is a run-set difference, the same one as in R-N5-SETTLE-C §2.»; REFEREE-2 §C C.4 l. 63 «REFEREE 63 (MAXN 100, so it skips n > 100);
mine 67 (gate_K64_n581, n 581) = the lane's. A run-set difference.» All figures equal my re-sum. 67 at gate_K64_n581 is also SETTLE's
longest event-free block (packet l. 183-184; R96-draft (10); src_corpus.txt l. 428 has maxblk 67 = maxblk2 67). Every block is far below
(n − 1) + m_C; REFEREE l. 96 «MUT 1 (block bound one less) never bites: the bound (n − 1) + m_C is not tight on the corpus.» No signed item
uses a count.
(11) Discrepancies, recorded for CHECKER, no verdict affected: (i) TWO REFEREE SESSIONS (a Lead slip). REFEREE successor 20 and successor 21
both wrote on claude/referee between 23:10Z and 23:26Z: successor 20 pushed §C Part 1 (9d67aa1e, 23:13:30Z) and its handover (67aabca0);
successor 21 pushed its own §C (957c3e90, 23:12:50Z, written «23:11-23:13Z … without sight of Part 1»), then merged both (8a1ba423,
23:37:41Z, a merge commit, parents 46cea2aa and 9d67aa1e; no rebase, no force-push). The merged file keeps Part 1 (l. 1-30) byte-identical
to 9d67aa1e (diff: none) and holds Part 2 (l. 32-128) = 957c3e90's text with its title line dropped, its "##" headings demoted to "###" and
a two-line merge note (l. 32-33 «Both are kept, nothing was rewritten. The verdicts agree item by item»); checked by diff. LEAD-STATE
23:40Z: «LEAD SLIP: two sessions on claude/referee — I created REFEREE 21 at 23:10 while REFEREE 20 was still doing the two items I sent at
22:56 … 21 merged both §C parts, no rebase/force». Both parts are by REFEREE (the same role); the two-referee count is unchanged (REFEREE
and REFEREE-2), and the verdicts of Part 1 and Part 2 agree item by item (checked: every packet item SIGNED, G-SRC-1 CLOSED by ONE-STEP,
SRC-L1/L2/L3 REQUIRED). Part 1 was written by the author of REFEREE's report (successor 20); Part 2 and the L-3 verdict by successor 21, who
calls 81f6b89c / 8951ef7c «My report» and says they «were written by successor 20» (P2 l. 36-37). (ii) Stamps: REFEREE-2's §C says «Lead
22:56Z» (l. 4) and was committed 22:56:32Z (70 new lines 32 s after the stamp); its report says «Lead 22:17Z asked me …» (l. 7) and was
committed 22:24:08Z with a 1,132-game corpus run and 20,000 random runs (R96's (11) (i) has the same pattern); REFEREE's Addendum 1 heading
says «~22:50Z by date -u» (l. 154), its commit is 22:47:50Z (a stamp after its commit); REFEREE §C L-3 section first said «23:40Z», after
its 23:37:41Z commit, corrected to «23:37Z» by 8197e182. Push times are not on record. (iii) REFEREE's Addendum 1 is +33/−0 but INSERTED
before the report's «## DONE / FINDINGS / NEEDS» (now l. 187-193, unchanged text), not appended at the end; the report's FINDINGS (l. 190)
still read «Every packet item to sign is SIGNED, … No gap. Nothing FALSE.» about SETTLE, which Addendum 1 corrects (G-SRC-1 «a joint miss»,
l. 161). (iv) REFEREE-2's §C l. 69 says ONE-STEP's REFEREE verdict «is pending» though 8951ef7c was committed 9 minutes earlier ((4)).
(v) R-N5-SRC.md has no «## 1» and no «## 6» heading (sections §2-§5, §7, §8); the verdict table numbers rows by packet §. (vi)
experiments/red/check.sh at 564bef5a l. 477 still reads «L-1 (entry 1), L-2 (entry 2) sha1 pinned» while l. 480 also pins L-3. (vii)
Counts that differ by run set, not by violations (0 everywhere): REFEREE n ≤ 100, 813 runs, 1,060 W-runs, 8,066 transitions, 12,729
PLAY-CAUSE^S, 27,157 IDX and 266,486 LEX checks (l. 93-94); REFEREE-2 1,132 games (repairs the two invalid starts, l. 136-137) plus 20,000
random runs, OS 852,572 checks (l. 90; = 452,450 + 214,299 + 167,786 + 18,037, by sum), y on c's cycle 9,055, new top ≠ c 4, all odd, at
ret22_n40 + start, none at an actual switch (REFEREE §C P2 l. 60-69 reconciles REFEREE's CYC 3 with this: different predicates).
(12) Excluded: lane work after the freeze other than the SRC fixes commits 6e323e0a (entry 1, L-1), 77a6d979 (entry 2, L-2) and 564bef5a
(entry 3, L-3): L-RED R148 (CASCADE-LIN DEAD; «R148-hxs: HXS at ONE source … = 36 at K4 m8», check.sh l. 450 at 564bef5a), R149 (NARROW
DEAD), R150 (CASC-EDGE DEAD, 916dac49), R147's working note beyond the packet; L-SI box 53 (ROOT-FLIP, HEAD-RED′, ONE-STEP-O, XCN-ONE DEAD)
and SETTLE fixes 3-4 / lines L-3, L-4 (R96's business); REFEREE's and REFEREE-2's SETTLE L-4 files. Not part of this entry.
(13) Commits: lane (claude/l-red): 0521fb82 (parent 47fd9163; freeze: packet, line, check.sh +3) → … → 6e323e0a (entry 1 +27/−0, L-1) →
77a6d979 (entry 2 +36/−0, L-2) → 564bef5a (entry 3 +22/−0, L-3; check.sh pins L-1..L-3). REFEREE on claude/referee: 81f6b89c (successor
20, report, new file 125 lines) → 8951ef7c (successor 20, R-N5-SETTLE.md Addendum 1, +33/−0) → 9d67aa1e (successor 20, §C Part 1, new file
30 lines) ‖ 957c3e90 (successor 21, §C) → 8a1ba423 (successor 21, merge, Part 2 + L-3 verdict) → 8197e182 (successor 21, stamp). REFEREE-2
on claude/referee-2 (successor 24): e8c1b62d (report, new file 169 lines) → 824651dd (§C, new file 70 lines) → 0f7f3010 (L-3 file) →
b441f3da (escapes). First trunk commits containing each (first-parent walk of the local trunk since 2026-10-30 20:00Z, git merge-base
--is-ancestor): 0521fb82 → 6d73243d (22:55:17Z); 81f6b89c → 0787f1d4 (22:55:17Z); e8c1b62d → b4002ba6 (22:41:48Z); 6e323e0a, 77a6d979 →
d9990584 (23:10:23Z); 8951ef7c → 5e499cb3 (23:10:24Z); 824651dd → b046d169 (23:10:24Z); 564bef5a → c0759f75 (23:25:19Z); 9d67aa1e →
f6a77a03 (23:40:50Z); 957c3e90, 8a1ba423, 8197e182 → 73feb559 (23:55:24Z, LOCAL only); 0f7f3010, b441f3da → a1379017 (23:55:24Z, LOCAL
only).
(14) Placement: after R96 (pending; at 7eae1203 R95 is l. 7476 and "## Dead ends (kept;" l. 7748). No Dead-ends row: the packet kills no
conjecture.

### R97 [refereed-only] N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum; for S4a at a transition k → k + 1, σ_(k+1) is the pointwise optimum of the one-player arena H_k); premises RESULTS R15 (a), (d)), with: a run is the sequence of states (σ_k, τ_k), a transition is written k → k + 1 (states k, k + 1), and an Even vertex y switches at k if σ_(k+1)(y) ≠ σ_k(y); n := |V| (V the vertex set of the game), m_E := the number of edges leaving Even vertices, succ(v) := the successors of v; values (c, P, ℓ) (cycle node, path set, length) as in SPEC S1, ⊴, ◁, ⊵, ▷ the SPEC S1 order (better for Even) and its strict and reverse forms; for a state k: Ξ_k := Ξ_{σ_k}, σ̄_k := S1's Odd counterstrategy to σ_k, and Iσ_k := Even's improving edges at k (SPEC S2: {(y, z) : Ξ_k(z) ▷ Ξ_k(σ_k(y))}); W-run F := RESULTS R89's (a maximal run of consecutive states of one τ-stretch none of whose transitions is an S4c fallback or changes λ_W, the cycle-node map of W), with τ and C := {v : λ_W(v) = v} fixed on F; for a state k of F: W_k := the [S1-val] valuation of the (σ_k, τ)-plays and ℓ_k(x) its length component at x, D_k := {Odd o : σ̄_k(o) ≠ τ(o)}, and H_k := S4a's arena at k (Even v keeps {σ_k(v)} ∪ Iσ_k(v), Odd follows τ); for a transition k → k + 1 of F: S_k := D_k ∪ D_(k+1) ∪ C (the SOURCES), the transition is a SOURCE EVENT iff Ξ_(k+1)(v) ≠ Ξ_k(v) for some v ∈ S_k and SOURCE-FREE otherwise, and it is C-ONLY iff every Even vertex switching at k is in C; E^S_F := the number of source events of F; |F| := the number of transitions of F; for v ∈ V: HXS_F(v) := the number of transitions k → k + 1 of F with v ∈ S_k and Ξ_(k+1)(v) ≠ Ξ_k(v); m_C := Σ_(Even c ∈ C) (|succ(c)| − 1) (≤ m_E): for every N5 run on every game and every W-run F of it: (Lemma PLAY-CAUSE^S) if k → k + 1 is a source-free transition of F and x is a vertex with Ξ_(k+1)(x) ≠ Ξ_k(x), then some Even y ∉ C switching at k lies on x's (σ_(k+1), τ)-path to λ_W(x), so ℓ_(k+1)(x) ≥ ℓ_(k+1)(y); (source blocks) if the transitions k0, …, k1 − 1 of F are all source-free, then for k0 ≤ k < k1 every Even vertex v ∉ C switching at k and every vertex v whose Ξ changes at k has ℓ_(k+1)(v) ≥ k − k0 + 1 (proof: L-SI P-N5-SETTLE's RUN-SETTLE induction (l-si 6a70a520, signed; RESULTS line L-2, l-si 86becaa0) restricted to Even vertices outside C, with Case 2 and Case 2b's comparison step by (Lemma ONE-STEP, REFEREE-2 R2-N5-SRC §3.2, claude/referee-2 e8c1b62d; signed by REFEREE, claude/referee 8951ef7c), which closes gap G-SRC-1 (REFEREE R-N5-SRC §3, claude/referee 81f6b89c), using R15 (a), Claim RG′ of that packet, ARENA-MAX (L-RED R140, l-red 47000632; the S4a half of the R57 premise above) and L-LIT T54's LEX-BFS / IDX-MONO as signed in that packet's review, read at one S4a evaluation with W_(k+1)); (Lemma TAIL) if k → k + 1 is a source-free C-only transition of F, then Ξ_(k+1) = Ξ_k, W_(k+1) = W_k, H_(k+1) ⊆ H_k arena by arena, and σ_(k+2)(x) = σ_(k+1)(x) for every Even x ∉ C whenever k + 1 → k + 2 is a transition of F; (Theorem SRC-SETTLE) every maximal run k0, …, k1 − 1 of source-free transitions of F has k1 − k0 ≤ (n − 1) + m_C; (Corollary SRC-COUNT, an EQUIVALENCE) |F| ≤ E^S_F + (E^S_F + 1)(n − 1 + m_C) with E^S_F ≤ Σ_(v ∈ V) HXS_F(v), and, as HXS_F(v) ≤ |F| for every v, for every family of games every W-run has polynomially many transitions iff max_(v ∈ V) HXS_F(v) is polynomial over all W-runs F (2026-10-30) — a REDUCTION (no count is bounded here; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim; σ̄-changes, switches at C and σ̄-changes at own Ξ-cycle nodes are not source events (unless they change Ξ at a source), and are not O(1) per W-run: pins xcn4_n12, cn3_n9; Lemma ONE-STEP is referee-originated) (P-N5-SRC, docs/red/P-N5-SRC.md; L-RED successor 35; fixes docs/red/P-N5-SRC-fixes.md entries 1-3), CHECKER PASS (docs/checker/C107.md, checker PENDING)
- Object (L-RED successor 35, Opus 5.5, D1/D18; frozen, unchanged during review): packet P-N5-SRC, docs/red/P-N5-SRC.md, sha1
  3caae56e3afdfaab80739c0e12e397b3d6cc7a8b, 195 lines (l-red freeze 0521fb820cdf9ecd5717a789ca0e63a9851ffd3c, 2026-10-30T21:37:27Z, the
  file's only commit; identical at l-red head 916dac49, at origin trunk 4880f3f5 and at the local trunk head 24675af3; pinned in
  experiments/red/check.sh l. 446). Both referees measured the sha1 at 0521fb82 (REFEREE l. 3-5 «Both equal the Lead's figures.»; REFEREE-2
  l. 2-3 «Both re-hashed: match.»). The Lead's freeze word is quoted at l. 2-5 («FREEZE a packet P-N5-SRC for the referees. It is SRC-SETTLE
  as a delta on P-N5-SETTLE … PLAY-CAUSE^S, the new step (T) in full, and Theorem SRC-SETTLE with its corollary (polynomial W-runs ⟺
  HXS-POLY, both directions). …»; a message, not on file). Status (l. 12): «Status: a REDUCTION and an EQUIVALENCE. No count is bounded
  here. G-N5-TIME stays OPEN. Not M3, not a step-4 pass, not a TARGET.md claim.» «Object: N5 only (SPEC S1-S5).» (l. 13). Source (l. 7):
  docs/red/R147-xcn.md (l-red 47fd9163), «Where the two differ, THIS packet governs.»; not refereed here. Base (l. 8-11): [SET] =
  P-N5-SETTLE, l-si 6a70a520 (sha1 aef403c3…; R96's object), its line L-2 (86becaa0, sha1 1fcb33c5…) and its fixes (F0, entries 1, 2;
  E1.12 used in §3). Sections: §0 what to sign (l. 15-24), §1 setting, [SET] quotes, NEW definitions, remarks (R1), (R2) (l. 26-54), §2
  PLAY-CAUSE^S (l. 56-82), §3 (S_j), (X_j) on source blocks, C1-C7 (l. 84-110), §4 Lemma TAIL (l. 112-141), §5 SRC-SETTLE, SRC-COUNT,
  EQUIVALENCE (l. 143-165), §6 Facts F1, F2 (READING, l. 167-172), §7 DATA and pins (l. 174-192), proposed line (l. 194-195).
  The RESULTS line, history: (1) the frozen line docs/red/P-N5-SRC-line.txt (0521fb82), sha1 3101a0c04f7959ccd50b86f5e6fa76789bdf6995, the
  line both referees reviewed: REFEREE REQUIRED SRC-L1 (|F|), SRC-L2 (t free), precision SRC-L3 (l. 23, l. 102-116); REFEREE-2 REQUIRED
  SRC-L1, SRC-L2, SRC-L3 (ONE-STEP), N-1 optional (l. 18, l. 140-160). (2) L-1 059d2733 (6e323e0a): from the Lead's relay; superseded. (3)
  L-2 9fcb5790 (77a6d979): SRC-L1, SRC-L2, N-1 in REFEREE-2's wording; REFEREE §C P2 l. 104 MATCHES. (4) L-3 5736d8ab (564bef5a): plus
  SRC-L3 (ONE-STEP cited, L41 tail) and V named; REFEREE §C l. 147 and REFEREE-2 L3 l. 24: MATCHES (Opus 5.5, D15). L-3 supersedes the
  earlier lines; the title is L-3 verbatim with its own date (to check (1)). Neither referee found a FALSE statement; every REQUIRED item
  binds a symbol (|F|; k, σ_(k+1), H_k in the R57 gloss) or cites the repair of an inherited proof-text gap (SRC-L3).
  Setting (packet §1): N5 = SPEC S1-S5, any parity game; a W-run F as in R89 (quoted verbatim, l. 29-30), on which «τ_k =: τ and C := {v :
  λ_W(v) = v} are fixed» (l. 31); «Every transition of F switches some Even vertex: with τ fixed and no S4c fallback, S4a changed σ (SPEC
  S4).» (l. 32); D_k, H_k as in [SET] (l. 33-34); ARENA-MAX (L-RED R140 §2, l-red 47000632) = the S4a half of [R57] (l. 35-37). NEW (l.
  42-48): SOURCES S_k := D_k ∪ D_(k+1) ∪ C; a SOURCE EVENT changes Ξ at some v ∈ S_k; E^S_F, HXS_F(v); C-ONLY transitions; m_C := Σ over the
  Even c ∈ C of (|succ(c)| − 1) ≤ m_E. Remarks (l. 49-54): (R1) for b with λ_W(b) = c ≠ b, W_k(b) reads b's path up to c, which meets no other
  W-cycle node, so W_k(b) does not depend on σ_k(c) and W_k(c) not on σ_k; (R2) Ξ_k is a function of σ_k. §1 cells: REFEREE «CHECKED» (l.
  17); REFEREE-2 «checked ✓» / «none» (l. 12). Names: the line's «Lemma TAIL» is this packet's §4 lemma, NOT landed R39's TAIL (RESULTS l.
  1862, one-Odd-choice games); D_k has the meaning of R92's D_s; the line's S_k is the source set, not SETTLE's induction statement (S_j)
  (to check (6)).
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 20 (report, Addendum 1, §C Part 1) and successor 21 (§C Part 2, line
  L-3); REFEREE-2 successor 24). Items (a)-(e) are SIGNED in both verdict tables (REFEREE "## Verdicts" l. 14-23 of R-N5-SRC.md; REFEREE-2 "##
  1. Verdict table" l. 9-18 of R2-N5-SRC.md), in REFEREE-2's §C C.1 (l. 7-15) and in both parts of REFEREE's §C (Part 1 l. 8-19; Part 2 l.
  44-58); the table is to-check (4). All are about N5 on every game, inside W-runs. Premises LANDED (as L-3 names them): SPEC S1-S5; RESULTS
  R15 (a), (d); R89's W-run; standing premise: RESULTS R57's SPEC premise (1E-N3), used as ARENA-MAX by (b) (Cases 2, 2b, 2c and ONE-STEP)
  and (c) ((T1) both directions). Signed in [SET]'s review and quoted, not re-signed here: Claim RG′ and [SET] §5's induction (R96's
  material), L-LIT T54 LEX-BFS / IDX-MONO, L-RED R140 ARENA-MAX. The code's match to SPEC is DATA (R15 G-N5T-1). No item uses a count.
  (a) Lemma PLAY-CAUSE^S (§2, l. 56-82): «Let k → k + 1 be a source-free transition of F. If Ξ_(k+1)(x) ≠ Ξ_k(x), then some Even y with
      λ_W(y) ≠ y switches at k and lies on x's (σ_(k+1), τ)-path to λ_W(x). In particular ℓ_(k+1)(x) ≥ ℓ_(k+1)(y).» (l. 57-58); proof: the
      first index i of x's play in S_k exists; Ξ(x) is a fixed function of y_0 … y_(i−1) and Ξ(y_i); with no Even switch before i every Odd
      y_t (t < i) is outside D_k ∪ D_(k+1), so the k-play has the same prefix and source-freeness gives Ξ_k(y_i) = Ξ_(k+1)(y_i). Cells:
      REFEREE «SIGNED» (l. 18; §2 l. 25-33: «This is a genuine strengthening of [SET]'s PLAY-CAUSE: it needs no «no σ̄-change» and no «no CN
      switch», because S_k contains D_k ∪ D_(k+1) and C itself.»); REFEREE-2 «SIGNED», «none» (l. 13; §2 l. 25-36 «✓ SIGNED.»).
  (b) (S_j), (X_j) on source blocks (§3, l. 84-110): «Let the transitions k0, k0 + 1, …, k1 − 1 of F all be source-free (a SOURCE BLOCK).»;
      «(S_j) Every Even y ∉ C that switches at k has ℓ_(k+1)(y) ≥ j + 1.»; «(X_j) Every vertex x with Ξ_(k+1)(x) ≠ Ξ_k(x) has ℓ_(k+1)(x) ≥ j +
      1.» (j := k − k0; l. 85-87). Proof: [SET] §5's induction with changes C1-C7 (l. 89-102); «Nowhere is σ_k(c) compared with σ_(k+1)(c).»
      (l. 106). Case 2 and Case 2b's comparison step is Lemma ONE-STEP (below; gap G-SRC-1). Cells: REFEREE «SIGNED» with G-SRC-1 closed (l.
      19; §3 l. 35-61; Addendum 1 l. 185 «Verdict: [SET] §5 (RUN-SETTLE) stays SIGNED, with Case 2 and Case 2b read through ONE-STEP. The
      same holds for SRC §3.»); REFEREE-2 «SIGNED, with G-SRC-1 closed by my Lemma ONE-STEP (§3.2)» (l. 14; §3 l. 38-92).
      Lemma ONE-STEP (referee-originated; proof step of (b), NOT a landed statement; L41): «Let t → t + 1 be a transition of a W-run F, y ∉ C
      an Even vertex, c := λ_W(y), z ∈ H_t(y) with λ_W(z) = c, and z's (σ_(t+1), τ)-path to c avoiding y. Then y ⊕ W_(t+1)(z) ⊴
      W_(t+1)(y).» (R2-N5-SRC.md l. 67-68); proof l. 69-83: ρ := σ_(t+1) with y ↦ z is a strategy of H_t, ARENA-MAX, and a split by the top
      z* of the new cycle when y lies on c's cycle (z* = c: equality; z* even: contradicts ARENA-MAX; z* odd: strict ◁). Use (l. 85-87):
      «Case 2 is ONE-STEP at t = k − 1 with z = b.»; «Case 2b is ONE-STEP at t = k with z = a.» Author: REFEREE-2 24, «**Lemma ONE-STEP**
      (REFEREE-2 24, PROVED).» (l. 66). Other referee: REFEREE 20, R-N5-SETTLE.md Addendum 1 (8951ef7c) l. 163-164 «SIGNED (Opus 5.5,
      D15)», own check l. 167-174, instantiations «(both CONFIRMED)» l. 178-184. G-SRC-1 (R-N5-SRC.md l. 42-61; R2-N5-SRC.md l. 51-65): in
      [SET] §5 Case 2, «val(ρ, τ)(y) = y ⊕ W_k(b)» «holds only if y is NOT on c's σ_k-cycle» (REFEREE l. 45); REFEREE-2's tool finds 4
      reachable states where the written equality is false (red/n3/instances/ret22_n40.pg with its start, t = 2-5, y 5, z 23, c 0; «In none
      of them does y then switch to z, so no instance of Case 2 or 2b itself is wrong.», l. 64-65); the conclusion holds by ONE-STEP.
      REFEREE's own closing argument (R-N5-SRC §3 l. 48-58, a four-way split) is SIGNED by REFEREE-2 (R2-N5-SRC-C.md l. 41) and is the same
      split (C.2 l. 39-40). The same gap sits in [SET] §5 (R96's RUN-SETTLE): «a joint miss» of both SETTLE reports (Addendum 1 l. 161; R2
      §C C.4 l. 64-65); SETTLE fixes entry 4 (l-si b04a1bbb) records it; R96's business.
  (c) Lemma TAIL (§4, l. 112-141): «Let k → k + 1 be a source-free C-only transition of F.»; «(T0) Ξ_(k+1) = Ξ_k, W_(k+1) = W_k, and H_(k+1)
      ⊆ H_k (arena by arena).»; «(T1) If k + 1 → k + 2 is a transition of F, it is C-only: σ_(k+2)(x) = σ_(k+1)(x) for every Even x ∉ C.»
      (l. 113-115). Proof: (T0) by PLAY-CAUSE^S, (R1) and transitivity of ▷ at a switching c (l. 116-124); (T1) W_(k+2) = W_(k+1) by
      ARENA-MAX at k + 1 and at k (σ_(k+2) ∈ H_(k+1) ⊆ H_k), then equal candidate sets and keys, IDX branch immediate, LEX branch by induction
      on L (l. 125-141). Cells: REFEREE «SIGNED» (l. 20; §4 l. 63-76; l. 76 «(T1) uses only that k → k + 1 is source-free and C-only.»);
      REFEREE-2 «SIGNED», «none» (l. 15; §4 l. 94-110 «SIGNED, no gap.»).
  (d) Theorem SRC-SETTLE (§5, l. 144-156): «For every N5 run on every game, every W-run F of it, and every source block k0, …, k1 − 1 of F:
      k1 − k0 ≤ (n − 1) + m_C.»; proof: by (T1) a block is normal transitions then a C-only TAIL; normal positions j ≤ n − 2 by (S_j); in the
      tail Ξ is constant (T0), so each switch of an Even c ∈ C strictly raises Ξ*(σ(c)) among |succ(c)| values: at most m_C tail
      transitions. The line states it for every MAXIMAL run of source-free transitions (narrower). Cells: REFEREE «SIGNED» (l. 21; §5 l.
      79-83); REFEREE-2 «SIGNED (rests on §3)», «none of its own» (l. 16; §5 l. 113-117).
  (e) Corollary SRC-COUNT and the EQUIVALENCE (§5, l. 157-162): «For every N5 run on every game and every W-run F of it, |F| ≤ E^S_F +
      (E^S_F + 1)(n − 1 + m_C).» («the source-free transitions form at most E^S_F + 1 maximal source blocks»); «For every family of games,
      every W-run has polynomially many transitions iff max_(v ∈ V) HXS_F(v) is polynomial over all W-runs F.» (⇐ via E^S_F ≤ n·max_v HXS_F(v)
      and m_C ≤ m_E; ⇒ via HXS_F(v) ≤ |F|). |F| is the number of transitions of F (L-3, SRC-L1). Cells: REFEREE «SIGNED» (l. 21; l. 84-85
      «Equivalence ✓: |F| ≤ (E + 1)(n + m_C) − 1 ≤ (1 + n·max HXS)(n + m_E), and HXS ≤ |F|.»); REFEREE-2 «SIGNED» (l. 16; l. 118-122).
  Gap maps: REFEREE §C Part 1 l. 22-23 and Part 2 l. 76-82 (joint: no open gap; G-SRC-1 CLOSED by ONE-STEP, «Lemma ONE-STEP is
  referee-originated (L41).»); REFEREE-2 §C l. 46-49 and l. 67-70 («Every SRC item to sign is SIGNED by both referees.»; «G-SRC-1 was found
  by both and is CLOSED.»), with REFEREE's ONE-STEP signature confirmed in R2-N5-SRC-L3.md l. 17 (to check (4)). Nothing FALSE on either
  side.
  The RESULTS line (L-3) claims less than the reports: no (R1), (R2) as statements, no ONE-STEP statement, no «it is C-only» in (T1), and
  SRC-SETTLE for maximal runs only. Every clause it states is one of (a)-(e).
- Fixes (docs/red/P-N5-SRC-fixes.md, L-RED successor 35, APPEND-ONLY, three entries, three commits each +N/−0: 6e323e0a (+27/−0), 77a6d979
  (+36/−0), 564bef5a (+22/−0, sha1 f8d54eecf704613491b0fa679fe8d2b071129a54, 85 lines; = l-red head = origin trunk 4880f3f5 = local
  24675af3; the last commit touching the file)). Header (l. 2): «The frozen files are never edited. Each entry names the item, says whether
  a TO-SIGN item is affected, and gives the change.» Each entry, with the referees' words:
  - Entry 1 (l. 4-27; Lead's relay of REFEREE-2 at 22:29Z, e8c1b62d «NOT fetchable» at the time, l. 7-9): E1.1 SRC-L1 (|F| in the
    quantifier), E1.2 SRC-L2 (R93's H_t gloss), E1.3 N-1; L-1 at l. 27; superseded by entry 2 (l. 60 «Entry 1's line L-1 (059d2733…) is
    superseded by L-2. It stays filed.»).
  - Entry 2 (l. 29-63; the report verbatim): E2.1 SRC-L1 «|F| := the number of transitions of F» (l. 38-42); E2.2 SRC-L2 «for S4a at a
    transition k → k + 1, σ_(k+1) is the pointwise optimum of the one-player arena H_k» (l. 43-50; «That leaves σ_new unbound, which the
    report also flags.», l. 46); E2.3 N-1 (l. 51-53); E2.4 SRC-L3 deferred to L-3 (l. 55-59); L-2 at l. 63.
  - Entry 3 (l. 65-85; after REFEREE signed ONE-STEP): E3.1 SRC-L3, the ONE-STEP proof-note insertion and the L41 scope tail (l. 71-75);
    E3.2 REFEREE's precision, V named (l. 76-78); REFEREE's SRC-L1 / SRC-L2 «already applied in L-2, in REFEREE-2's wording» (l. 79-81);
    L-3 at l. 85.
  No fix changes a signed statement of the packet: every entry says «No TO-SIGN item of the frozen packet changes.» (l. 10, l. 34, l. 69);
  all fixes bind symbols, word the line, or cite the repair. G-SRC-1 itself is a proof-text gap of the reused [SET] §5, closed by ONE-STEP
  (Claims (b)); it is recorded in the fixes through E2.4 / E3.1.
- Not signed: §1 (setting, (R1), (R2), NEW definitions; «CHECKED» / «checked» by both); the [SET] pieces quoted in §1 (not re-signed; packet
  l. 22); §6 F1 («A CN switch at Even c ∈ C (a → b) with Ξ_(k+1)(c) = Ξ_k(c) has λ_Ξ(c) = c at k or at k + 1.», l. 168; «I have not proved
  that proviso here.», l. 170; DATA «CNOX = 0 on the corpus and on 10,000 random games») and F2 (l. 172), READING, «not used in §2-§5:
  confirmed» (REFEREE-2 l. 17); §5's comparison with HEAD-RED / HEAD-RED′ (l. 163-165, READING); §7 DATA and pins. OPEN, not claimed: max
  HXS_F polynomial over all W-runs (the residual of (e); «HXS-POLY» in the Lead's freeze word) and G-N5-TIME. No CONJECTURE of the packet
  is killed; no dead end in this entry. Lane work after the freeze other than the SRC fixes commits is not part of this entry (to check
  (12)).
- Referee strengthening (NOT part of this entry; remarks of one referee, remarks of both outside the verdict cells, readings):
  (i) REFEREE §2 l. 32-33 and REFEREE §C P2 l. 47: PLAY-CAUSE^S strengthens [SET]'s PLAY-CAUSE (no «no σ̄-change», no «no CN switch»).
  (ii) REFEREE l. 76 / REFEREE-2 l. 109: (T1) needs only that k → k + 1 is source-free and C-only (REFEREE §C P2 l. 51 «My note … = R2's»).
  (iii) REFEREE l. 57-58: in Case 2 sub-case (iv) the chain «W_k(y) ▷ y ⊕ W_k(b) = W_(k+1)(y) ⊵ W_k(y)» is a contradiction, so (iv) is
      excluded there (REFEREE-2 §C l. 34 «REFEREE's extra remark is also right»).
  (iv) REFEREE-2 §C l. 36-38: REFEREE's split needs «b's path to be disjoint from c's arc from c to y»; «It is: if b's path entered that arc,
      it would reach y before c»; a precision, stated in ONE-STEP (β) (REFEREE §C P2 l. 117-118 «I accept it.»).
  (v) Mutation control: REFEREE l. 96 «MUT 1 (block bound one less) never bites: the bound (n − 1) + m_C is not tight on the corpus.» So
      the block bound has no biting control.
  (vi) Self-corrections: REFEREE Addendum 1 l. 161 «My signature of [SET] §5 (§5 above, «Case 2 ✓», «Case 2b ✓») missed this. It was a
      joint miss with REFEREE-2 23.»; REFEREE-2 §C C.4 l. 64 «my predecessor's SETTLE report (§2.5) and §C missed G-SRC-1».
  (vii) READING (packet §5 l. 163-165): «the terms SB_F, CN_F and XCN_F do not occur, and ROOT-FLIP is not used»; «the heads are the
      sources D ∪ C in place of the targets U (or U ∪ τ(Odd))». Not signed.
- Honest limits: (i) a REDUCTION and an EQUIVALENCE: no count is bounded; max HXS_F polynomial and G-N5-TIME stay open; the equivalence
  is a reformulation of «polynomial W-runs», not a bound. (ii) Everything is inside W-runs; W-runs are not whole runs (τ-changes, S4c
  fallbacks and λ_W-changes cut runs into W-runs, R89). (iii) (b) rests on [SET] §5's induction (R96's RUN-SETTLE, pending) with changes
  C1-C7, and its Case 2 / 2b comparison step on Lemma ONE-STEP, a referee-originated proof (author REFEREE-2 24, signed by REFEREE 20; L41;
  REFEREE's own four-way split signed by REFEREE-2 as a second repair). (iv) (b), (c) rest on L-LIT T54's LEX-BFS / IDX-MONO and on Claim
  RG′ (R96, pending), not landed here: signed «as used» in SETTLE's review (Case 2a) and checked in their (T1) use by both SRC referees
  (REFEREE §4; REFEREE-2 §4); the line names them in the source-block proof note only, not at TAIL (to check (7), D-3). (v) Claim RG′ and
  the choice rules are about S1's evaluation as SPEC S1 and si.py define it; standing premise R57 (1E-N3); the code's match to SPEC is DATA
  (R15 G-N5T-1). (vi) No biting mutation control for the block bound (Referee strengthening (v)). (vii) The scope tail's «not O(1) per
  W-run» rests on two pins only (to check (7), D-1): the pins show repeats (4 and 3 at one vertex in one W-run), not a growing family; R147 l.
  179 «Not done: a super-linear XCN or CN family.» (viii) Counts are transitions, not bit operations; no running-time bound. (ix) Not M3,
  not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open.
- Data (DATA, not proof): pinned (packet §7 l. 187-188: «Pins (experiments/red/check.sh «R147»; sha1 in xcn/pins.sha1; xeng state sequences
  identical; Oink 8fbf0a7 --zlk winners equal and verify passes)»). experiments/red/check.sh at 0521fb82: sha1
  ed5f9faa1cd80728bdb541fb19b324dfffebf257, 450 lines; at 564bef5a: sha1 21f901459271882aab35b09e0c4f0930962e8160, 483 lines; l. 1-447
  identical (by diff). This entry's blocks: l. 437-444 («R147»: xcn/pins.sha1, xcn4_n12 by xcn.py, cn3_n9 by srcsettle.py, srcrand seed 1,
  xeng and Oink on both pins) and l. 445-447 (packet and frozen line sha1) at both commits, and at 564bef5a l. 477-480 (L-1, L-2, L-3 sha1).
  l. 448-476 at 564bef5a (R148, R149) are not this entry. Re-run for this draft from a `git archive` of each commit (experiments/ and
  docs/red/; tools/oink/build linked to the session's Oink build so the Oink branch runs; from experiments/red), l. 5-7 (set -euo pipefail,
  cd, temp dir) plus those blocks, 2026-10-30 23:59:06Z-23:59:07Z by date -u (read before and after), rc 0 each. Single pins (564bef5a
  archive, 23:59:13Z, rc 0 each): «XCN xcn4_n12.pg n 12 iters 5 wruns 2 maxL 4 maxCN 0 maxCNc 0 maxXCN 4 maxXCNo 4 sumCN 0 sumXCN 4»; «SRC
  cn3_n9.pg n 9 VIOL 0 E 3 Esrc 3 CN 3 CNO 3 CNOX 0 FLIPONLY 0 maxblk 0 maxL 3 maxEsrc 3 maxE 3 maxHXS 0 VIOL2 0 TAILV 0 BLKV 0 maxblk2 3
  maxtail 2 Es2 0»; «OINK OK» on both pins; xcn/pins.sha1 «OK» for all four files (cn3_n9.pg 0d5eb838…, .start e65854b7…; xcn4_n12.pg
  e43dc878…, .start 22eb4725…). Tools identical at 0521fb82 and 564bef5a: xcn/srcsettle.py 43a2ea9fe7e9b40dff1e253b86f5c79d4a8658b5, xcn.py
  8d61d49a8d905b5319f4405032b5fb0d794a1e54, srcrand.py 81c4127c066faca535d7f9ad32913c0274e98652.
  DATA OF RECORD (packet §7 l. 179-186; box 50b's lists sbcg 719 + alt 413 = 1,132 games, n5b SPEC traces, xcn/runsrc.sh): 1,130 games
  analysed, 2 RUN-ERROR (invalid starts); VIOL2 0, TAILV 0, BLKV 0, CNOX 0; source events 4,546 against [SET]'s events 4,724; longest source
  block 67 (gate_K64_n581, n 581, default best-reward start), 63 on n ≤ 100 (runfam_K40, n 79); longest C-only tail 1 (2 on the pin cn3_n9);
  random games (seeds 11-14, 2,500 each, n 6-14) all counters 0, W-runs ≤ 3 transitions. Re-summed for this draft: equal (to check (10)).
  Second engine: seg/xeng.py state sequences identical on both pins; Oink 8fbf0a7 --zlk winners equal and verify passes on both pins (pinned
  l. 443-444).
  REFEREE (successor 20; own docs/referee/scratch/src_probe.py, «adapted from settle_probe.py», l. 87): «813 runs (740 games, 73 skipped), all
  RC 0, 1,060 W-runs, 8,066 transitions.» (l. 93); «12,729 PLAY-CAUSE^S checks; 27,157 IDX and 266,486 LEX checks. VIOLATIONS 0 for every
  check.» (l. 94); «Longest source block 63 (n ≤ 100; …)» (l. 95); CYC (G-SRC-1's configuration at actual Case-2 switches): «3 occurrences,
  all of type (ii)» (l. 59); pins cn3_n9 and xcn4_n12, 0 violations (l. 97-100).
  REFEREE-2 (successor 24; own docs/referee-2/R2-N5-SRC/src_check.py, «Lane xcn/*.py is not imported.», l. 124): checks PCS, S, X, ORD, T0,
  T1, NRM, TL, BLK, SC, HXS and OS (l. 126); 0 violations on sbcg.lst (719), alt_all with start (94) and start-less (319), random seeds 21,
  22 (5,000 games, 20,000 runs) and the pins (l. 128-134); «OS = 0 on 852,572 instances (the corpus and 20,000 random runs, §5).
  OS_newtop_even = 0.» (l. 90); longest source block 67 (gate_K64_n581) (l. 130). No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-SRC.md (report 81f6b89ca179cfa0512f0e5f6d0e9789fb659a60, 2026-10-30T22:19:54Z, committed directly
  on claude/referee, first on trunk by 0787f1d4 (22:55:17Z); sha1 de52a7f4973ae2129716b89692dac7b0d264cbcb, 125 lines, unchanged since (=
  referee head 8197e182 = trunk); successor 20): §1 CHECKED; §2-§5 SIGNED; «Verdict: MATCHES the signed items once SRC-L1 and SRC-L2 are
  applied.» (l. 116, on 3101a0c0). REFEREE docs/referee/R-N5-SETTLE.md Addendum 1 (8951ef7c98cb14326cf4b6435fc6a0ed5a4356f6,
  2026-10-30T22:47:50Z, +33/−0, 193 lines, sha1 f93eedacfb9fbc550fc5b36f259b4e10e151c148, unchanged since (= referee head = trunk); first on
  trunk by 5e499cb3, 23:10:24Z; successor 20): «(1) G-SRC-1 CONFIRMED, as a proof-text gap in [SET] §5 Case 2 and Case 2b.» (l. 155); «(2)
  Lemma ONE-STEP (…): SIGNED (Opus 5.5, D15).» (l. 163-164); «Verdict: [SET] §5 (RUN-SETTLE) stays SIGNED, with Case 2 and Case 2b read
  through ONE-STEP. The same holds for SRC §3.» (l. 185). REFEREE §C docs/referee/R-N5-SRC-C.md: Part 1 (successor 20,
  9d67aa1ea2fce04d05c9440c0284c0a79222d0ff, 23:13:30Z, new file, 30 lines, sha1 e7687a089317f954dc4dbdb2ff73c535162f251d; first on trunk by
  f6a77a03, 23:40:50Z): cross-map «agree» on every item (l. 8-19), joint gap map (l. 21-25); Part 2 (successor 21, 957c3e90, 23:12:50Z,
  merged by 8a1ba423 23:37:41Z) with the L-3 section (8a1ba423; stamp fix 8197e1821997ba02eeef9bba1a08d424a076b54a, 23:37:49Z; the file at
  8197e182: 147 lines, sha1 729e80f001d96f7b6d7721c9ef813a6be197bc6b, = referee head; on the LOCAL trunk only, merge 73feb559, 23:55:24Z):
  «Verdict on L-2: MATCHES SRC-L1, SRC-L2 and N-1 (Opus 5.5, D15).» (l. 104); «Verdict on L-3: MATCHES SRC-L1, SRC-L2, SRC-L3 and N-1
  (Opus 5.5, D15). No REQUIRED change remains on the SRC line.» (l. 147). REFEREE-2 docs/referee-2/R2-N5-SRC.md (report
  e8c1b62dcb5023db58999f36c24e80f0d3492f76, 2026-10-30T22:24:08Z, committed directly on claude/referee-2, first on trunk by b4002ba6
  (22:41:48Z); sha1 bd04826d25e8c9f1daf91515400d6e3f287a7eb1, 169 lines, unchanged since; successor 24): §1 checked; §2, §4, §5 SIGNED; §3
  SIGNED with G-SRC-1 closed by its Lemma ONE-STEP (l. 162-169). §C docs/referee-2/R2-N5-SRC-C.md (824651ddd7b13f90b8da353b9a9d764df2ef515f,
  2026-10-30T22:56:32Z, new file, 70 lines, sha1 4131357d951c81118637ac6674dd3ba372a5c356, unchanged since; first on trunk by b046d169,
  23:10:24Z): «**Verdict on REFEREE's G-SRC-1 closing argument: SIGNED (Opus 5.5, D15).**» (l. 41); «Every SRC item to sign is SIGNED by
  both referees.» (l. 68). Line file R2-N5-SRC-L3.md (0f7f3010bb09319000abb2f6b9753a427e29d71a, 23:27:02Z; b441f3da50e96ed9aed940ad38452dc99af16865,
  23:27:18Z, 25 lines, sha1 569fb407e84d7fa2ce00daab7921af7615eeac8b, = referee-2 head; on the LOCAL trunk only, merge a1379017, 23:55:24Z):
  «L-3 (5736d8ab): **MATCHES** (Opus 5.5, D15). No required change.» (l. 24).
  INDEPENDENCE: REFEREE l. 9 «Independence: I opened no docs/referee-2/ file for this packet.»; REFEREE §C Part 1 l. 4-5 «My report
  R-N5-SRC.md (81f6b89c) was written and pushed before I opened R2-N5-SRC.md. I opened it for the ONE-STEP check (R-N5-SETTLE Addendum 1,
  8951ef7c) and for this §C.» REFEREE-2 l. 5 «Independence: written before opening any docs/referee/ file on SRC.»; REFEREE-2 §C l. 3-4: its
  report «pushed before I opened REFEREE's report», REFEREE's report «opened after my push (Lead 22:56Z)». G-SRC-1 was found by each referee
  before seeing the other's report (REFEREE 81f6b89c 22:19:54Z; REFEREE-2 e8c1b62d 22:24:08Z; Addendum 1 l. 156-157). No review imported
  lane code (REFEREE src_probe.py; REFEREE-2 l. 124); the lane's scripts ran only as the pinned blocks.
  §C (both): verdicts on every packet item identical; no disagreement in substance. Differences of reading, resolved: SRC-L3 (REFEREE
  precision → REQUIRED, §C P1 l. 17, P2 l. 56); REFEREE's «V» item (precision; REFEREE-2 «not raised», applied in L-3); the G-SRC-1
  configuration counts (REFEREE CYC 3 over actual Case-2 switches vs REFEREE-2 OS over all eligible z; reconciled, REFEREE §C P2 l. 60-69,
  REFEREE-2 §C l. 42-45); the block-length figures (63 vs 67, run set, to check (10)).
- TARGET.md diff: «n := |V| (V the vertex set of the game)» is TARGET.md §1 l. 8's n («n = |V|, m = |E|, d = |pr(V)| ≤ n + 1.»), V TARGET's
  vertex set (l. 6); m_E ≤ TARGET's m; succ(v) the successors under TARGET's E; games are TARGET.md §1 games (REFEREE-2 §C l. 57, a
  table cell with escaped bars: «precision; TARGET.md l. 8 binds n = \|V\| fleet-wide, so optional»). The line makes no M4 claim and no
  TARGET claim; its own scope clause reads «a REDUCTION (no count is bounded
  here; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim; … Lemma ONE-STEP is referee-originated)». REFEREE l. 12
  «Scope (D1): a REDUCTION and an EQUIVALENCE inside W-runs of N5. No count is bounded. G-N5-TIME stays OPEN. Not a TARGET.md claim.»;
  REFEREE-2 l. 6 «Scope: a REDUCTION and an EQUIVALENCE inside W-runs. Nothing is bounded. G-N5-TIME stays OPEN.»; REFEREE-2 l. 160
  «TARGET.md: no complexity or M-claim.» Not a claim of TARGET.md §1 or §2 (a lemma on Ξ-changes, a bound on source blocks and an
  equivalence about W-runs of N5 runs on every game; no bound on a W-run, on a run or on running time; no algorithm claim); not a step-4
  pass. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER R96's UPDATE of G-N5-TIME (pending, R96-draft l. 476; at present the last on l. 11
is R95's, «UPDATE 2026-10-30 22:14Z: RESULTS R95 (P-N5-WRUN; CHECKER C105 3c59333c) …»), built by script only from the clauses of the title
line L-3, with R94's-R96's construction (labels behind their clauses; the scope tail as in R95's / R96's UPDATE, the source parenthesis
kept). L-3 holds ten "|"; the UPDATE holds none: (r1) «n := |V| (V …)» → «n := the number of vertices of V (V …)»; (r2) «(|succ(c)| − 1)» →
«(the number of successors of c, minus 1)»; (r3) «|F| := the number of transitions of F; » deleted; (r4), (r5) «|F|» → «the number of
transitions of F» (twice); these replacements are not title text (to check (9)). Landing date and time and CHECKER commit to be filled at
landing:
UPDATE <YYYY-MM-DD> <HH:MM>Z: RESULTS R97 (P-N5-SRC; CHECKER C107 <checker>) [refereed-only] LANDED: N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum; for S4a at a transition k → k + 1, σ_(k+1) is the pointwise optimum of the one-player arena H_k); premises RESULTS R15 (a), (d)), with: a run is the sequence of states (σ_k, τ_k), a transition is written k → k + 1 (states k, k + 1), and an Even vertex y switches at k if σ_(k+1)(y) ≠ σ_k(y); n := the number of vertices of V (V the vertex set of the game), m_E := the number of edges leaving Even vertices, succ(v) := the successors of v; values (c, P, ℓ) (cycle node, path set, length) as in SPEC S1, ⊴, ◁, ⊵, ▷ the SPEC S1 order (better for Even) and its strict and reverse forms; for a state k: Ξ_k := Ξ_{σ_k}, σ̄_k := S1's Odd counterstrategy to σ_k, and Iσ_k := Even's improving edges at k (SPEC S2: {(y, z) : Ξ_k(z) ▷ Ξ_k(σ_k(y))}); W-run F := RESULTS R89's (a maximal run of consecutive states of one τ-stretch none of whose transitions is an S4c fallback or changes λ_W, the cycle-node map of W), with τ and C := {v : λ_W(v) = v} fixed on F; for a state k of F: W_k := the [S1-val] valuation of the (σ_k, τ)-plays and ℓ_k(x) its length component at x, D_k := {Odd o : σ̄_k(o) ≠ τ(o)}, and H_k := S4a's arena at k (Even v keeps {σ_k(v)} ∪ Iσ_k(v), Odd follows τ); for a transition k → k + 1 of F: S_k := D_k ∪ D_(k+1) ∪ C (the SOURCES), the transition is a SOURCE EVENT iff Ξ_(k+1)(v) ≠ Ξ_k(v) for some v ∈ S_k and SOURCE-FREE otherwise, and it is C-ONLY iff every Even vertex switching at k is in C; E^S_F := the number of source events of F; for v ∈ V: HXS_F(v) := the number of transitions k → k + 1 of F with v ∈ S_k and Ξ_(k+1)(v) ≠ Ξ_k(v); m_C := Σ_(Even c ∈ C) (the number of successors of c, minus 1) (≤ m_E): for every N5 run on every game and every W-run F of it: if k → k + 1 is a source-free transition of F and x is a vertex with Ξ_(k+1)(x) ≠ Ξ_k(x), then some Even y ∉ C switching at k lies on x's (σ_(k+1), τ)-path to λ_W(x), so ℓ_(k+1)(x) ≥ ℓ_(k+1)(y) (Lemma PLAY-CAUSE^S); if the transitions k0, …, k1 − 1 of F are all source-free, then for k0 ≤ k < k1 every Even vertex v ∉ C switching at k and every vertex v whose Ξ changes at k has ℓ_(k+1)(v) ≥ k − k0 + 1 (proof: L-SI P-N5-SETTLE's RUN-SETTLE induction (l-si 6a70a520, signed; RESULTS line L-2, l-si 86becaa0) restricted to Even vertices outside C, with Case 2 and Case 2b's comparison step by (Lemma ONE-STEP, REFEREE-2 R2-N5-SRC §3.2, claude/referee-2 e8c1b62d; signed by REFEREE, claude/referee 8951ef7c), which closes gap G-SRC-1 (REFEREE R-N5-SRC §3, claude/referee 81f6b89c), using R15 (a), Claim RG′ of that packet, ARENA-MAX (L-RED R140, l-red 47000632; the S4a half of the R57 premise above) and L-LIT T54's LEX-BFS / IDX-MONO as signed in that packet's review, read at one S4a evaluation with W_(k+1)) (source blocks); if k → k + 1 is a source-free C-only transition of F, then Ξ_(k+1) = Ξ_k, W_(k+1) = W_k, H_(k+1) ⊆ H_k arena by arena, and σ_(k+2)(x) = σ_(k+1)(x) for every Even x ∉ C whenever k + 1 → k + 2 is a transition of F (Lemma TAIL); every maximal run k0, …, k1 − 1 of source-free transitions of F has k1 − k0 ≤ (n − 1) + m_C (Theorem SRC-SETTLE); the number of transitions of F ≤ E^S_F + (E^S_F + 1)(n − 1 + m_C) with E^S_F ≤ Σ_(v ∈ V) HXS_F(v), and, as HXS_F(v) ≤ the number of transitions of F for every v, for every family of games every W-run has polynomially many transitions iff max_(v ∈ V) HXS_F(v) is polynomial over all W-runs F (Corollary SRC-COUNT, an EQUIVALENCE): a REDUCTION; no count is bounded here; σ̄-changes, switches at C and σ̄-changes at own Ξ-cycle nodes are not source events (unless they change Ξ at a source), and are not O(1) per W-run: pins xcn4_n12, cn3_n9; Lemma ONE-STEP is referee-originated (P-N5-SRC, docs/red/P-N5-SRC.md; L-RED successor 35; fixes docs/red/P-N5-SRC-fixes.md entries 1-3). G-N5-TIME stays open.
