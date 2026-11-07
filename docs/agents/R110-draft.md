# Draft RESULTS R110 (Lead; first fill 2026-11-05T14:30:27Z on line L-2 (draft sha1 dd6624ba, CHECKER C122 80ed31a6: FAIL E-1, E-2, E-3; G-0 confirmed); SECOND FILL 2026-11-05T17:48:59Z by date -u (subagent) on P-IDEAL-FLIP line L-3, docs/new/P-IDEAL-FLIP-line-L3.txt, l-new 47b4e165, sha1 4089bd73baf65929cf5b6094ef31882df817fd53) — to CHECKER C122 Add. 1 — LANDED in RESULTS 2026-11-05 20:08Z (CHECKER C122 32f65fe0 PASS), after R109, before Erratum E-1
SECOND FILL (2026-11-05T17:48:59Z by date -u, subagent; for CHECKER C122 Add. 1). Read at the origin heads fetched at its start (git
fetch, 2026-11-05T17:4xZ): l-new a9851eba (its parent 47b4e165 holds L-3), referee bfeca123, referee-2 8fde383f, checker 80ed31a6;
origin trunk 33428ff6. Local trunk d599bdf0 = three merges (--no-ff) into 33428ff6: 9ebdc441 (l-new a9851eba), 71459c3a (referee-2
8fde383f), d599bdf0 (checker 80ed31a6); referee bfeca123 is not merged (no L-3 item in it, below). Not pushed. RESULTS, GAPS and
TARGET.md are byte-equal to 67ec1151 (last commit on them: 67ec1151; RESULTS sha1 6772d9c4…, 11,901 lines; GAPS b79c582c…), so (0), (6)
and (9) stand. New sources: docs/checker/C122.md (80ed31a6, 2026-11-05T15:47:18Z, 127 lines, sha1
50af2c30700b4f435a0d5434a125e50eb966df4c): FAIL E-1 (G-9 (i)), E-2 (G-9 (ii)), E-3 (G-1), G-0 CONFIRMED, all four fixed by one L-3 = L-2
with the replacements R1-R4 of its §5; line L-3, docs/new/P-IDEAL-FLIP-line-L3.txt (l-new 47b4e165, 2026-11-05T16:26:08Z, the file's
only commit; sha1 4089bd73baf65929cf5b6094ef31882df817fd53 with newline, 4,715 bytes, = C122 §5's expected values); fixes entry 2
(docs/new/P-IDEAL-FLIP-fixes.md l. 59-81 at 47b4e165; file 81 lines, sha1 4220c44e6caa0bc6e2b2d4363ba3f5ec97505de6, l. 1-57 unchanged);
REFEREE-2's byte test of L-3 (docs/referee-2/R2-P-IDEAL-FLIP-L2.md Addendum 1, l. 32-42, 8fde383f, 17:06:22Z: MATCHES). REFEREE's byte
test of L-3 (its §C add. 1 to docs/referee/R-P-IDEAL-FLIP.md) is NOT on origin claude/referee at this fill (head bfeca123; the report
file was last changed by 74fae0fa; 840a3c11 adds only the tool docs/referee/scratch/flip_l3_bytetest.py): the entry carries ONE marked
placeholder for it, in Signatures, to be replaced by the Lead before landing. My byte test of L-3 (scratch fill2/l3rel.py, rc 0): R1-R4
copied from C122 §5 by script (line wraps joined), each old string once in L-2 and each new string once in L-3, L-2 with R1-R4 = L-3
(True); 53 «(» / 53 «)», depth never negative, final 0; 0 "|"; one « — »; «2026» once. Re-runs: check.sh block «P-IDEAL-FLIP» from a git
archive of 47b4e165 (17:47:06Z-17:47:27Z, rc 0, PASS; flipcheck raw output byte-equal to the first fill's); the UPDATE rebuilt from L-3
(upd110b.py, 13 controls True); the quote sweep and the landing simulation (Addendum 2). Changed at this fill, and nothing else: this
header line and this paragraph; the title (L-3); in the entry, Object (the packet at 47b4e165, the line of record L-3, line history, the
L-3 byte tests), Claims (L-3), Premise (L-3), Fixes (entry 2), Honest limits (viii), Data (L-3's DATA parenthesis, now closed; the pins
and the re-run at 47b4e165), Signatures (L-3; the placeholder), TARGET.md diff (L-3); the GAPS preamble and the UPDATE (rebuilt from
L-3); the digest of Addendum (10); Addendum 2 (new). The FIRST FILL text below (from FIRST FILL (this text) to (14)) and Addendum
(1)-(9) are kept byte-unchanged as the record of the fill on L-2: where they call L-2 the title line or the current line, say that no
L-3 exists, or give the first fill's line numbers and counts, they describe draft dd6624ba at 14:30Z; C122 ruled its flags G-0, G-9 and
G-1 as above, and the entry block follows L-3.
FIRST FILL (this text). Read at the origin heads fetched at its start (git fetch, then git ls-remote, 2026-11-05T14:21:18Z: l-new
4c2e5124, referee 74fae0fa, referee-2 b2c0fff8, checker 177f8368, l-comp 6f19564f; origin trunk 61a1175c, the Lead's commit «Lead:
T^R(3) = 8 independent; audit routed; L-SI box 65 negative, box 66 GO; sweep 12:03Z; log»). Local trunk 08c460d1 = five merges (--no-ff,
one per lane head, none an ancestor of 61a1175c before): fe409908 (l-new 4c2e5124), 47230937 (referee 74fae0fa), a7eba516 (referee-2
b2c0fff8), 4ef99b6b (checker 177f8368), 08c460d1 (l-comp 6f19564f); not pushed. RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, NOW,
TARGET.md and CLAUDE.md are byte-equal at 61a1175c and 08c460d1 (git diff --quiet, exit 0); RESULTS (sha1
6772d9c4efc7d723d4064ab47f9e5f823ec52904, 11,901 lines) and GAPS (sha1 b79c582ce9bed929a6df54a7fdc88e5c629aced9, 23 lines) were last
changed by the R109 landing commit 67ec1151 (2026-11-04T23:38:33Z). UPDATE (same fill, 14:3xZ by date -u): the Lead committed 93e68aa4
(2026-11-05T14:20:57Z, «Lead: REFEREE 24 started (T^R(3) audit); R110 draft under way; L-RED (c); L-COMP queue; L-SI box 67; sweeps
13:04Z/14:02Z; log») on top of 08c460d1 in this working tree (not pushed; origin trunk still 61a1175c at 14:3xZ); it changes only
docs/NOW.md, docs/agents/LEAD-STATE.md and docs/agents/ROSTER-ARCHIVE.md; RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, TARGET.md and
CLAUDE.md are byte-equal at 08c460d1 and 93e68aa4 (git diff --quiet, exit 0), so (0), (6) and (9) stand. Its log entry records that
REFEREE successor 24 started 14:09Z on an independent second audit of T^R(3) ≤ 8; nothing of that audit is on file, and the body makes
no statement about it (G-8 (d)).
Sources read: the packet docs/new/P-IDEAL-FLIP.md (frozen 9effea1f; unchanged at 4c2e5124, by sha1), line L-1 (9effea1f), fixes entry 1
and line L-2 (4c2e5124); REFEREE successor 23's docs/referee/R-P-IDEAL-FLIP.md (report eaa941b9, §C 74fae0fa; l. 1-159 at 74fae0fa = the
report, by cmp) with scratch/flip_probe.py and xinew_logs/flip_probe.txt; REFEREE-2 successor 27's docs/referee-2/R2-P-IDEAL-FLIP.md
(dc622d03, unchanged at b2c0fff8) with R2-P-IDEAL-FLIP/flip_check.py, R2-P-IDEAL-FLIP-L2.md (8b53a9e2) and, as status only,
R2-T3R-audit.md (d1c4a530); experiments/new/check.sh at 9effea1f and 4c2e5124; experiments/new/box162/flipcheck.py, box150/check.py and
the three instance files; docs/new/N5-SLOT-box160.md l. 50; notes/L-NEW.md (4c2e5124, l. 1-40); notes/REFEREE.md and notes/REFEREE-2.md
(P-IDEAL-FLIP rows); RESULTS R104 (title l. 9864), R108 (l. 10812), R109 (l. 11030-11321), Erratum E-2 (l. 11336-11362) and the
Dead-ends section (l. 11364-); GAPS l. 11 (the R109 UPDATE of 2026-11-04 23:38Z is its last); DECISIONS L41, L42, L43;
docs/agents/LEAD-STATE.md (2026-11-05 entries); docs/checker/C118.md-C121.md and notes/CHECKER.md (177f8368); docs/agents/R109-draft.md
(the model of this draft).
Re-runs (scratch, git archive of 4c2e5124's experiments/new and docs/new): check.sh block «P-IDEAL-FLIP» (w162 / pin162, l. 903-910),
2026-11-05T14:12:13Z-14:13:02Z, rc 0, PASS line and raw output in w162.out / w162raw.out; my split of flipcheck.py's genome sets
(fcstats.py, rc 0); my own checks of the three instances (mysim110.py: my R104 simulator of the R109 draft, and my own c-step, forced
run and V_k written from packet §1's text; no lane code imported; rc 0); the L-1 → L-2 token diff and byte test (wdiff110.py, rc 0); the
UPDATE build with 13 controls (upd110.py, rc 0); the quote sweep and the landing simulation.
TRUNK STATUS (git merge-base --is-ancestor at 14:2xZ, local trunk then 08c460d1, now 93e68aa4, which contains it): 9effea1f, 4c2e5124,
e93b0e82, 279dd656, eaa941b9, 74fae0fa, dc622d03, 8b53a9e2, d1c4a530, b2c0fff8 and 6f19564f are ancestors of local trunk 08c460d1 and
NOT of origin trunk 61a1175c; the Lead commits ef4150d5, 92a78041, ca8c640a and 61a1175c, and 67ec1151, are on both. The Lead pushes
trunk before landing. The body makes NO statement about trunk (C113 E-2).
LESSONS APPLIED. C113 E-1: the title is L-2 verbatim with no insertion. C114 Add. 1 E-1: the UPDATE head carries «<DATE>». C115 E-1: the
premise route is checked against what RESULTS records (G-4; the R109 quote byte for byte). C116 G-1, C118 §4, C120 §4, C121 §4: the
UPDATE rule of R105 with R107's step for the unlabelled DEAD clause, unchanged ((9); one adaptation for the unclosed DATA parenthesis,
G-0). C116 G-2: name clashes settled by one body sentence (G-6). C117 E-1 / E-2: no sentence wider than signed; DATA scoped as measured;
the instance inlined in full. C118 E-1: no stale status sentence; the entry calls nothing «pending» (the only «PENDING» is the title
fill); REFEREE-2's audit of L-COMP's encoding is stated as a fact with its date and commit, and the entry says what would change the
label, not when. C118 §3 / Erratum E-2: every DEFINITION in the title line diffed against the packet (G-2). C118 §5: a lane conjecture
killed inside a landed line gets no Dead-ends row ((14)). C120 §5 / C121 §5 G-9 RULE: «From the next line on, though, the C118 G-8
advice («name the statements a DATA count covers») is a check item. A line that leaves it out gets an E-item.» (G-9). C120 §3 note on
«…» that is not a quotation (G-8). C119 E-1: every «referee X did Y» is checked against that referee's file (line-precise sweep).
to check: FLAGS FIRST (G-0 to G-14; three of them are for CHECKER to rule: G-0, G-9 (ii), G-1), then the CLEAN items and (0)-(14).
- G-0, THE LINE'S PARENTHESES DO NOT BALANCE (NEW; FLAG for CHECKER; nothing in the referees' reports or the fixes mentions it). By
  script on L-2: 51 «(» and 50 «)», the depth never negative, final depth 1. The only unmatched «(» is the one of «(DATA: W-ONLY, step
  form:» (character 3,255 of 4,301); the DATA parenthesis is never closed, and the source parenthesis «(P-IDEAL-FLIP,
  docs/new/P-IDEAL-FLIP.md; L-NEW successor 53)» sits inside it. L-1 has the same defect (49 «(», 48 «)»); the referees' byte tests and
  token diffs (L-1 → L-2) cannot see it. The intended reading is plain from R105-R109's lines: the DATA parenthesis closes before «
  (P-IDEAL-FLIP,». No statement, definition or count is affected. Since the title is L-2 verbatim, the RESULTS heading would carry the
  unclosed parenthesis. Options (not mine to choose): (a) a note (no content change); (b) an L-3 = L-2 with one «)» inserted before «
  (P-IDEAL-FLIP,», byte-tested by both referees, as C121 §5 did for R109's L-4. The UPDATE is unaffected: opening the DATA parenthesis
  drops its «(», and the result is balanced (42 «(» / 42 «)») and byte-equal to the UPDATE built from L-2 with the missing «)» inserted
  (upd110.out «cross-check … True»).
- G-9, DATA (the C120 §5 / C121 §5 check item): BY THE LETTER, MET; two precision items and one scope item for CHECKER's ruling. L-2's
  DATA parenthesis names a statement for every count: «W-ONLY, step form» (44,084 real steps), «W-ONLY, ISO independence» (31,320
  (state, q) pairs), «W-ONLY, frozen form» (1,044 (ISO genome, q) pairs), «T ≤ T_2(d − 1) + 2» (28,896 ISO runs), «NOW-ONCE, real runs»
  (307 pairs), «SWAP» (15,660 (state, c) pairs), «FLIP-1 upper bounds» (1,312 pairs, k = 0, …, 6), «SC-ISO» (the instance replayed), and
  it names the items without lane DATA: «NOW-ONCE for c_t-step sequences and the T_k(m) values for m ≥ 2: no signed DATA». Every count
  equals my re-run of w162 at 4c2e5124 (CHECKED line, (10)). Items: (i) PRECISION, the genome set: the line's «300 random 𝓛^R genomes
  with d = 2, 3, 4, a quarter of them not ISO» is the drawing rule (flipcheck.py draws genome i without the ISO constraint iff i % 4 =
  3, packet l. 220 «3 of 4 ISO»); measured (fcstats.out): 100 genomes each at d = 2, 3, 4; 75 drawn without the constraint, of which 65
  are not ISO by flipcheck's own is_iso and 10 are ISO by chance; 50 corpus genomes (d = 2: 8, d = 3: 29, d = 4: 13; 36 ISO); every one
  has d ≤ 4, so «every start» holds (38,912 runs = Σ 2^N). The ISO-only counts use the 225 + 36 = 261 genomes known ISO (the 10
  chance-ISO ones are not used there), so no count is inflated; the share of non-ISO genomes is 65 / 300, not a quarter. (ii) SCOPE,
  «SWAP: 0 violations on 15,660 (state, c) pairs»: all 15,660 pairs come from the 261 ISO genomes (flipcheck.py runs the SWAP check
  inside «if iso:»; 261 × 30 states × 2 values of c), while the line states Lemma SWAP «on 𝓛^R_d» without ISO; and the clause labelled
  (SWAP) also carries the concatenation statement (SWAP-RUN, fixes F-b), which no lane tool counts and which is not in the «no signed
  DATA» list. The count names its statement and its unit, so it is not the C121 E-1 pattern verbatim (there the counts named no
  statement); but a reader may take the 15,660 pairs as covering non-ISO genomes and SWAP-RUN. FOR CHECKER: note or E-item (C121 §5:
  «DATA whose scope is wider than its coverage»). I cannot change the line; the body states the coverage exactly (Data, Honest limits
  (v)). (iii) PRECISION, «W-ONLY, frozen form: 0 violations on 1,044 (ISO genome, q) pairs»: one start state per pair (the stored start
  with q at 0 and 1), against the statement «from any state with q at 0 and 1»; the unit is named, so the count is exact. Neither
  referee raised (i)-(iii) (REFEREE l. 127-128 «DATA: every count is scoped to its statement and equals my w162 re-run, and the
  unsupported items are named»; REFEREE-2 l. 110-111 «DATA scope per statement in the line: matches what the tool counts»).
- G-1, TITLE SHAPE AND SOURCE NOTE (FLAG, note-class by precedent; CHECKER to rule). L-2 contains «2026» once, as « (2026-11-05) — »,
  the only « — » (by script), and ends with the source parenthesis «(P-IDEAL-FLIP, docs/new/P-IDEAL-FLIP.md; L-NEW successor 53)»
  (inside the unclosed DATA parenthesis, G-0). The source note names the packet only, not docs/new/P-IDEAL-FLIP-fixes.md. Unlike R108
  (fixes = packet remarks only; C120 §5 «G-1 (source note names no fixes file): note.») and R109 (its note named fixes entry 1), two
  clauses of L-2 are proved only in the fixes file: NOW-ONCE's c_t-step half without ISO (F-a, (b′)) and SWAP's unconditional
  concatenation (F-b). Both referees signed F-a and F-b in their second rounds, and the body names the fixes file (Object, Fixes). The
  title is "### R110 [refereed-only] " + L-2 + the fill ", CHECKER PASS (docs/checker/C122.md, checker PENDING)" (as R90-R109), nothing
  inserted. L-2 has no attribution of the model's first statement («R178» 0 times); R104 carries it.
- G-2, DEFINITIONS DIFFED AGAINST THE PACKET (the C118 §3 / Erratum E-2 lesson; my own diff, by reading and by script where literal).
  (i) «𝓦_d the genomes with levels 0, …, d − 1 whose level-0 movers are exactly two movers named 0 and 1» = §1 l. 52-53 («𝓦_d (d ≥ 2):
  the IDEAL-ACYC genomes with levels 0, …, d − 1 whose level-0 movers are exactly two movers, named 0 and 1 (any degrees, any number of
  movers on the levels ≥ 1)»); IDEAL-ACYC is the line's «on acyclic Ξ-graphs»; the line drops «(d ≥ 2)» (at d = 1 every 𝓦_1 statement of
  the line is vacuous: no mover of level ≥ 1; the corollary binds «(d ≥ 2)» itself); precision note. (ii) «𝓛^R_d ⊆ 𝓦_d the 2-wide
  degree-2 ladders in L-RED's R197 convention (movers 2l and 2l + 1 on level l, all of degree 2, no other movers, option k of a mover of
  level l ≥ 1 W-pointing to mover 2(l − 1) + k)» = §1 l. 54-56 («N = 2d movers 0, …, 2d − 1, lev(x) = ⌊x/2⌋, every mover of degree 2,
  and wt(x, k) = 2(lev(x) − 1) + k for lev(x) ≥ 1»; «Ξ-data, β's, gates and start arbitrary»; «𝓛^R_d ⊆ 𝓦_d for d ≥ 2»); equal (REFEREE-2
  l. 118 «(«no other movers» = N = 2d)»). (iii) «T^R(d) the largest number of steps over 𝓛^R_d and all starts (kept apart from R109's
  T*(d) over 𝓛_d; T^R(d) ≤ T*(d))» = §1 l. 56-58 («T^R(d) := the largest T over 𝓛^R_d and all starts.»; «𝓛^R_d ⊆ 𝓛_d, so T^R(d) ≤
  T*(d)»); «largest» is a maximum (T is integer-valued and bounded on 𝓛^R_d, by T^R(d) ≤ T*(d) and RESULTS R109's SANDWICH, or directly
  by RESULTS R108's LEVEL-PRODUCT; the packet uses neither). (iv) «ISO the property that no option has Ξ-target 0 or 1» = §1 l. 59. (v)
  «b_0(s) = 1 iff g(0, s(0)) < g(1, s(1))» = §1 l. 60 («b_0(s) := 1 if g(0, s(0)) < g(1, s(1)), else 0»); the «else 0» is implicit in «c
  = b_0» with c ∈ {0, 1}. (vi) The c-step: «for c ∈ {0, 1} the c-step the step rule on the movers of level ≥ 1 (A-sets under the old
  state, keys under the new state, movers 0 and 1 kept) with every level-1 option W-pointing to mover w keyed by (κ^c_w, its own gate),
  κ^c_0 = 1 − c, κ^c_1 = c» = §1 l. 62-65 (s′(y) := s(y) for y ∈ {0, 1}; level by level from level 1, the option in A_s(x) with the
  least key^c under s′; key^c = (κ^c_(wt(x, k)), g(x, k)) at level 1, the W-target's key^c followed by g(x, k) above); «the step rule»
  is read without the run's two stop rules: the c-step is a total map (my reading; the packet's definition has no stop rule; both
  referees diffed the definition: REFEREE l. 124, REFEREE-2 l. 119); equal. (vii) «T_k(m) the supremum, over the ISO genomes of
  𝓛^R_(m+1), their starts u_0 and the bit sequences c_1, …, c_L with at most k changes, of the number of t with u_t ≠ u_(t−1) on the
  levels ≥ 1, where u_t is the c_t-step of u_(t−1)» = §1 l. 66-68 (forced run; moves; flips over t ∈ [2, L]; «T_k(m) := the supremum of
  moves over all such G, s_0, L and c with flips ≤ k (a priori possibly ∞)»); the line drops «m ≥ 1» (m = 0: no mover above level 0,
  every count 0); «changes» = flips; equal. (viii) W-ONLY: «on 𝓦_d every step of a run equals, on the levels ≥ 1, the c-step with c =
  b_0 of the new state» = (a) l. 73; «under ISO the A-sets of the levels ≥ 1 do not depend on the options of 0 and 1» = (b) l. 74 (its
  A-set half; its Ξ-value half is not in the line: narrower); «freezing 0 and 1 at options q gives an IDEAL genome whose run from any
  state with q at 0 and 1 is the iterated b_0(q)-step» = (c) l. 76-79, whose run is «stopped at the first application of Step^c_G that
  changes nothing»: «the iterated b_0(q)-step» is read up to its first fixed point (a run is finite and stops when nothing changes;
  precision note, REFEREE §C l. 188 «this is W-ONLY (c)'s statement. Correct.»); «under ISO» governs both halves, as in (b), (c); «hence
  every run of an ISO genome of 𝓛^R_d (d ≥ 2) has T ≤ T_2(d − 1) + 2» = (d) l. 80. (ix) NOW-ONCE: «on 𝓛^R_d, on an interval of steps
  over which b_0 of the states is constant» = (a) l. 113-114 (b_0(s_t) the same for t ∈ [a, b], no ISO); «the states» are s_a, …, s_b (a
  reader who adds s_(a−1) gets a stronger hypothesis, so a narrower claim); «and in a c_t-step sequence on an interval over which c_t is
  constant» = fixes F-a (b′) l. 12-13 (any G ∈ 𝓛^R_d, no ISO), which extends packet (b) l. 115-116 ([forced runs, ISO]); «every level-1
  mover moves at most once» = both. (x) SWAP: «on 𝓛^R_d, the (1 − c)-step of G equals the c-step of G^swap» = l. 131 («For every state s
  and c ∈ {0, 1}: Step^(1−c)_G(s) = Step^c_(G^swap)(s).»); «the genome G with the W-targets of the two options of every level-1 mover
  exchanged (in R109's 𝓛_d, not in 𝓛^R_d)» = l. 128-130; «so under ISO a c_t-step sequence with k changes is a concatenation of at most
  k + 1 runs of two fixed IDEAL genomes» = fixes F-b l. 22-27 (q ANY options of 0 and 1; «each block [a, b] with c = v is a prefix of
  the run of H_q»; «moves = the sum of the pieces' lengths»), which replaces packet SWAP-RUN's reading l. 137-146; «runs» are prefixes
  of runs followed by idle frames (F-b l. 24-26), and its own summary uses the same word («a concatenation of at most k + 1 runs of the
  two fixed IDEAL genomes H_q and (G^swap)_q»); precision note. (xi) FLIP-1: «T_0(1) = 2 and T_k(1) = 3 for every k ≥ 1 (upper bounds by
  proof; lower bounds by two explicit instances, …kf0_d2_t2.json, sha1 c2233e05…, and kf1_d2_t3.json, sha1 d368d441…)» = §5 l. 149-176
  (the sha1s = check.sh pin162 and my measurement). (xii) The DEAD: «the lane conjecture SC-ISO («for every d ≥ 3, in every run of every
  ISO genome of 𝓛^R_d, the number of steps before the first step that moves 0 or 1 plus the number of steps after the last such step is
  at most T^R(d − 1)»)» against §6 l. 179-180 («for every d ≥ 3, in every run of every ISO genome of 𝓛^R_d, seg1 + tail ≤ T^R(d − 1)»)
  with seg1 / tail of §1 l. 69-70 (a LEVEL-0 STEP moves mover 0 or 1; seg1 = T if there is none; tail = 0 if none): the line spells seg1
  and tail out and leaves the no-level-0-step case implicit («the number of steps before the first step» of a run without one is all of
  them; the instance has two such steps, so both forms are killed by it); the text in «…» is the line's wording, not a quotation (G-8).
  «by the ISO genome iso_d4_st9 of 𝓛^R_4 (…, sha1 7ca1e68c…; T 11 from its stored start, mover 1 moving at step 7 and mover 0 at step 8,
  6 + 3 = 9 steps outside)» = §6 l. 181-190 (and my run, (10)); «together with the machine premise T^R(3) ≤ 8 (CaDiCaL UNSAT on L-RED's
  encoding, not Lean, not refereed; without it the instance shows that SC-ISO at d = 4 forces T^R(3) ≥ 9)» = §6 l. 191-193; the label
  «CONDITIONAL DEAD (premise T^R(3) ≤ 8, machine)» = REFEREE FL-L3 (l. 139-140), fixes l. 50-51. (xiii) The scope tail: «a REDUCTION of
  the W-channel part of SLOT-TRADE to an external-flip model inside the IDEAL model» is the line's category label; it is the packet's §7
  READING (l. 233-234, «W-ONLY + SWAP turn the W-channel part of SLOT-TRADE into a question about TWO fixed genomes», not signed), and
  «W-channel part» is not defined in any signed text (note; both referees MATCHED the tail: REFEREE-2 l. 127 «Scope tail and DATA tail
  ✓»); «bounds nothing polynomially», «the CONJECTURES FLIP-ADD and SLOT-TRADE are not claimed» (l. 6-7, 227), «Ξ-cyclic genomes and
  genomes outside 𝓦_d are not covered». (xiv) The DATA parenthesis: G-9. ALL EQUAL, with the precision notes (i), (vi), (viii), (x),
  (xii), (xiii). Both referees diffed every definition of L-1 (REFEREE «## 6. Line L-1 (definitions diffed; DATA scoped per C120)», l.
  118-128; REFEREE-2 «## Line L-1: clause by clause, every definition against the packet», l. 117-127), and on L-2 REFEREE l. 191 «All
  other definitions and clauses are unchanged from L-1, which I diffed in §6.»; REFEREE-2 L2 file l. 23-26 (byte test True).
- G-3, STRICT SYMBOL TEST (notes). (i) «d»: 𝓦_d, 𝓛^R_d, T^R(d) are defined for a free d; W-ONLY's corollary binds «(d ≥ 2)»; NOW-ONCE
  and SWAP say «on 𝓛^R_d» without «d ≥ 2» (the packet's §3, §4 assume d ≥ 2; at d = 1 there is no level-1 mover, so both are vacuous).
  (ii) «m» and «k» are bound in T_k(m); «q» in W-ONLY (c); «c» by «for c ∈ {0, 1}»; «w» in the c-step; «G» in SWAP is the genome of
  𝓛^R_d under discussion. (iii) «u_t», «u_0» and «c_1, …, c_L» are bound inside T_k(m)'s definition and reused in NOW-ONCE and SWAP as
  «a c_t-step sequence» (F-a's definition, any start u_0 and bits). (iv) s in b_0(s) is a state; g(·, ·) is R104's gate. (v) «the levels
  ≥ 1» = U of §1. (vi) «IDEAL model», «Ξ-graph», «mover», «level», «option», «W-target», «Ξ-target», «gate», «step», «run», «start»,
  «state», «A-set», «key» are R104's model words (RESULTS l. 9864) and packet §0. (vii) «iso_d4_st9», «kf0_d2_t2.json», «kf1_d2_t3.json»
  are data files, named with their paths and abbreviated sha1s. (viii) «L-RED's R197 convention», «L-RED's encoding»: attributions,
  prefixed. None is a free quantifier of a claim clause except (i), whose reading is fixed by the packet and by vacuity.
- G-4, PREMISE ROUTE (the C115 E-1 class): CLEAN (my check). L-2's premise parenthesis: «premise: R104's definition of the model only,
  no theorem of R104 used; and RESULTS R109's SEG-ONCE at l = −1 only». What RESULTS records (by script, prem110.py): the packet's quote
  of R109 (l. 21-24, 314 characters, «(SEG, SEG-ONCE; restated in full from P-IDEAL-SEG) on an interval of steps …moves at most once in
  it») is a byte-exact substring of RESULTS l. 11030 (R109's title), once, and occurs nowhere else in RESULTS; REFEREE l. 24 «The quote
  is FOUND verbatim in the landed R109 line (trunk 42c7711b, RESULTS l. 11030; grep -F: 1 hit).»; REFEREE-2 l. 26 «the quoted clause is
  verbatim in the landed R109 entry (docs/RESULTS.md l. 11030; Python substring test True)». Use: SEG-ONCE with l = −1 and the interval
  [1, T] (vacuous hypothesis) at degree ≤ 2 gives «each level-0 mover … moves at most once in the whole run» (packet l. 24-25), used in
  W-ONLY (d) (l. 104-105) and NOW-ONCE (c) (l. 118; (c) is not in the line). R109's SEG-ONCE is stated «at degree ≤ 2» with no 𝓛_d
  restriction, and every mover of 𝓛^R_d has degree 2. R104's definition: packet §0 (l. 32-50) is headed «(RESULTS R104's definition, as
  restated in P-IDEAL-SLOT §0)»; my diff against P-IDEAL-SLOT §0 (e46e98a4, l. 26-45): the definition lines (chain, Ξ-value, comparison,
  A-set, key, step) are equal; the packet drops SLOT §0's «M := Σ deg(x)», the degree-1 remark, KP_s, the ladder definition and the
  width remark, adds «(in particular no option has its own mover as Ξ-target)» (a consequence of acyclicity) and the two facts (F1),
  (F2); both referees checked (F1), (F2) as immediate (REFEREE l. 23; REFEREE-2 l. 23-25). OTHER RESULTS TEXT NAMED BY THE LINE
  (definitions, not theorems): R109's 𝓛_d and T*(d), in «(kept apart from R109's T*(d) over 𝓛_d; T^R(d) ≤ T*(d))» and «(in R109's 𝓛_d,
  not in 𝓛^R_d)»; both are true from R109's definitions alone (𝓛^R_d ⊆ 𝓛_d; G^swap has two degree-2 movers per level, W-targets one
  level down); packet l. 25-26 «R109's 𝓛_d and T*(d) are named in §1 and §4 only to keep them apart from 𝓛^R_d and T^R(d); no statement
  here uses a value or a bound of T*.»; REFEREE l. 26 «T* is named but never used.»; REFEREE-2 l. 27 «R109's 𝓛_d / T*(d) are only named,
  never used for a bound.». Fixes F-c uses R109's SHIFT (quoted, two pieces, each a byte-exact substring of RESULTS l. 11030) for an
  unsigned remark only (fixes l. 46-47). Not used: packet l. 27-28 «Not used: RESULTS R105 (so its Erratum E-2 does not bear on this
  packet), R106, R107, R108, docs/lit, docs/sources, any other lane file.»; REFEREE l. 26 «No R105 (E-2 irrelevant), R106 to R108,
  docs/lit or docs/sources.»; REFEREE-2 l. 28 «No R105 item (so Erratum E-2 is irrelevant), no R106-R108, no docs/lit. Confirmed by
  reading every proof step.». RESULTS R108 (b) states the same whole-run fact; it is not cited. The one machine premise (T^R(3) ≤ 8) is
  not a RESULTS item; it is the DEAD item's listed gap, inside the line (G-8). No unlanded result, no lit note and no lane file is a
  premise of a signed statement.
- G-5, RESULTS ERRATUM E-2 TO R105 DOES NOT BEAR ON R110 (note). E-2 (RESULTS l. 11336-11362) corrects R105's CHAINED binder, TOP-MONO's
  RANK_t and KEYFLIP's moves(x). R110 cites no R105 item. Its premise R109 SEG-ONCE rests in R109 on R105's LOCAL, key half (R109's own
  premise), which E-2 lists among the unaffected definitions («Unaffected: R105's other definitions»); RESULTS R109 is landed text and
  is cited as such. By script, the packet contains «R105» only at l. 27 (the «Not used» line), and «CHAIN», «KEYFLIP», «RANK»,
  «moves(x)» 0 times; L-2 contains «R105» 0 times.
- G-6, NAMES, SAME LABELS, OTHER MEANINGS (by script on RESULTS 6772d9c4 / GAPS b79c582c; note; C116 G-2's remedy). 0 times in RESULTS
  and GAPS: «P-IDEAL-FLIP», «SC-ISO», «FLIP-ADD», «W-ONLY», «NOW-ONCE», «SWAP-RUN», «𝓦», «𝓛^R», «T^R», «T_k(», «iso_d4_st9»,
  «kf0_d2_t2», «kf1_d2_t3», «flipcheck», «G^swap», «H_q», «external-flip», «CONDITIONAL DEAD», «FL-G1», «C122», «R110», «box160»,
  «box162»; «SWAP» and «ISO» as words 0. Same names, other meanings: (a) «FLIP-1» in RESULTS R69 (l. 3614: Lemma FLIP's part «(b)
  FLIP-1: if p1 is intact at t2, …», about N5 on parity games) and inside «G-FLIP-1» / «N-FLIP-1» (R69); R110's FLIP-1 is the one-level
  value of T_k. (b) «G-FLIP-1» 4 times in RESULTS (R69: REFEREE-2 successor 16's joint gap on P-N5-FLIP, l. 3586, 3604, 3640-3641); the
  R110 body cites REFEREE-2 successor 27's G-FLIP-1 (the machine premise), a different gap with the same label, and says so once (Honest
  limits (ix)). (c) «b_0» 9 times in RESULTS (R106: the start b_0 of the ladder L_K, l. 10467-10550, and DE36, l. 11892, 11898); R110's
  b_0(s) is the key bit, defined in the line. (d) «κ» 347 times in RESULTS and 11 times in GAPS (N5's κ values); R110's κ^c_w is bound
  in the line. (e) «c-step» once (R87, inside «S4c-step»). (f) «SLOT-TRADE» 4 times in RESULTS (R109) and once in GAPS (R109's UPDATE):
  the same conjecture as R110's (R109's CONJECTURE SLOT-TRADE); consistent. Applied: one body sentence, Honest limits (ix). No line
  change.
- G-7, L41 (the C109 E-1 class): not triggered (my reading; POINT TO CHECK). L-2 contains «referee-originated» 0 and «lane-authored» 0
  times. The packet's proofs are L-NEW successor 53's (packet l. 5 «Labels: PROVED (L-NEW 53, unrefereed)»). The fixes are lane-written
  too (fixes l. 2 «L-NEW successor 53. Each entry: what is changed, why, by whose finding, and the full text of every new argument.»),
  but two of them carry referee-found content: F-a is REFEREE's FL-N1 (l. 51-52, the proof of (b) uses no ISO), and F-b's exchange
  argument was found by both referees independently (REFEREE FL-N2, l. 59-65, «I checked this argument. It is not in the packet's text
  (see FL-L2).»; REFEREE-2 N-1, l. 55-57); after the lane wrote them out, both referees signed them (REFEREE §C l. 166, 173, «It is the
  same argument as my FL-N2, in a cleaner form (no c* needed).»; REFEREE-2 L2 file l. 9, 15, «It is my N-1 written out.»). So the proofs
  in RESULTS are lane-authored and signed by both; the ideas are referee findings, credited in the body (Fixes). L41 governs proofs
  WRITTEN by a referee; it is not needed here, but CHECKER may prefer a credit sentence, which the body has.
- G-8, THE CONDITIONAL DEAD (L42, L43) and the C120 «…» note: NOTE, with one point for the Lead. (a) R110 is the first «CONDITIONAL
  DEAD» in RESULTS (0 occurrences). L43 (DECISIONS l. 369-374) asks for «a refereed proof, or one instance exceeding an EXPLICIT bound»;
  here the bound T^R(3) rests on a machine premise. REFEREE ruled (l. 80-83) «The DEAD cannot be signed unconditionally now. L43 needs a
  refereed proof or an instance beyond an EXPLICIT ESTABLISHED bound, and here the bound itself is the open premise.» and «Under Lead
  reading L42 (an uncovered premise is stated as an explicit hypothesis, labelled CONDITIONAL), it CAN be signed now as «CONDITIONAL
  DEAD (premise: T^R(3) ≤ 8, machine)», with the gap listed.»; REFEREE-2 (l. 82-85) «SIGN WITH GAP», «RESULTS must keep that wording.
  The item must not be cited as an unconditional DEAD.». L42's text (DECISIONS l. 362-367) is about R57's SPEC premise («(or stated with
  the premise as an explicit hypothesis, labelled CONDITIONAL)»); its use for a machine premise is REFEREE's reading, which the Lead's
  routing applied (Lead commit ca8c640a, 11:48:17Z, «Lead: P-IDEAL-FLIP signed (DEAD conditional); fix round; L-COMP priority; L-RED
  status; log») without a DECISIONS entry. POINT FOR THE LEAD: whether a Lead reading should record it (not required for this entry; the
  label and the gap are in the line). (b) The killed statement is the packet's W-channel ISO form only; the lane's «single-channel
  trade» for the NOW channel is not claimed (packet l. 194 «Does NOT claim: anything about the NOW channel at d = 4 (UNKNOWN; box 160
  §0)»), and the box 160 READING «The single-channel trade «seg1 + tail ≤ T^R(d − 1)» is EXACT at d = 3 for both channels»
  (docs/new/N5-SLOT-box160.md l. 50) is lane DATA. (c) The C120 note («Note: a «…» that is not a quotation should be avoided in later
  lines»): the SC-ISO text in «…» is the line's wording of §6's form (G-2 (xii)), as R108's REPLAY and R109's SEG1-2D; note only.
  «polynomial» 1 time in L-2 («bounds nothing polynomially»); «linear» 0; «O(» 0 (FLIP-ADD's «O(m)» is not in the line). (d) STATUS OF
  THE MACHINE PREMISE (a fact, not a claim of R110): L-COMP successor 9 reports T^R(3) = 8 by its own encoding (claude/l-comp 6f19564f,
  experiments/comp/box27/ENCODING.md); REFEREE-2 audited that encoding (R2-T3R-audit.md, d1c4a530, 2026-11-05T12:49:17Z: l. 63
  «**G-FLIP-1 CLOSES on my side**», l. 66 «Under D1's two-referee rule the other referee's audit is still needed before the change
  lands.»); REFEREE successor 23 wrote on L-2 that it had not audited either encoding (74fae0fa l. 195-196 «I have not audited either
  encoding.»); the Lead's log of 14:15Z (93e68aa4) routes an independent second audit to REFEREE successor 24. Both referees say the
  label changes only through a separate landed item (REFEREE l. 197-198; REFEREE-2 L2 file l. 28-30). So R110's DEAD stays CONDITIONAL
  exactly as L-2 says; the one audit on file is REFEREE-2's and is not a signature of R110. The body states only the audit on file, with
  its commit and date, and what changes the label (a separately landed item); it names no other referee's status, so no sentence goes
  stale when a second audit is filed.
- G-10, LEAD READINGS AND RULINGS AS ON FILE (the C111 E-1 class): CLEAN. L-2 cites no Lead reading and no ruling (by script: «Lead
  reading» 0, «L42» 0, «L43» 0, «D1» 0). The lane works under D14 / D18 (packet l. 2 «L-NEW successor 53 (Opus 5.5), D14 / D18;»). The
  freeze was a Lead brief (packet l. 2 «Lead brief BOX 162 (2026-11-05): «freeze packet P-IDEAL-FLIP for the referees»»; Lead commit
  ef4150d5, 09:29:14Z, «Lead: L-NEW 52 parked, 53 started (P-IDEAL-FLIP freeze); sweep 09:03Z; roster; log»). Routing to the referees:
  Lead commit 92a78041 (11:11:06Z). Fix round: fixes l. 4 «Lead 11:49Z fix round» (Lead commit ca8c640a, 11:48:17Z; the lane commit
  4c2e5124 is 11:49:46Z; the stamp is not verifiable from the repository, D-2). REFEREE's use of L42 is a referee reading (G-8 (a)).
- G-11, STALE LANE TEXT (notes; nothing here lands). (i) Packet l. 1 (title) and l. 16 (table) say «DEAD» for SC-ISO; the line and both
  referees make it CONDITIONAL; the packet is frozen and the fixes file carries the change (fixes l. 50). (ii) Packet §4 l. 145-146 (the
  «no q» caveat) is superseded by F-b (fixes l. 34). (iii) Packet §4 l. 147 «The two genomes are in 𝓛_d, so T* (not T^R) caps each
  piece» is wrong as stated and corrected by F-c (fixes l. 39-47; REFEREE-2 F-1, l. 58-62); not in the line. (iv) Packet §6 l. 181
  «(sha1 in §7)»: §7 prints no digest; the digest 7ca1e68c52e4bb02ee260ccc36e8323146cdc6b3 is in check.sh pin162, in L-1 and L-2
  (abbreviated) and in both referees' reports (REFEREE l. 7, REFEREE-2 l. 7). (v) Packet §7 l. 209 «T_0(3) ≥ 9 RUNNING at the freeze:
  UNKNOWN» and the notebook l. 10 are lane status; not used. (vi) Packet §7 l. 220 «3 of 4 ISO» (the drawing rule, G-9 (i)). (vii) The
  lane notebook has no «Dead ends» entry for SC-ISO; it records the kill at l. 7, 34 and 62-63. (viii) Packet §0's heading says «as
  restated in P-IDEAL-SLOT §0»; the restatement is not verbatim (G-4), and the referees checked it as a restatement.
- G-12, SHA1 PINS IN check.sh (the C110 F-1 / C116 G-3 class): present. experiments/new/check.sh at 9effea1f (911 lines, sha1
  808cd43c74cb349edf11870e3697e1337fa0f86d) adds block «P-IDEAL-FLIP» (l. 903-910: flipcheck.py, the box 150 checker on the instance,
  pin162 of the packet, L-1, the instance and the two FLIP-1 instances); 4c2e5124 (911 lines, sha1
  96e7e25b1709b1a6f0653be8421dad98bd6b352d) extends pin162 by the fixes f8d3677e and L-2 8099415b (l. 905-907 changed; PASS line «… I-1
  d368d441, fixes f8d3677e, line L-2 8099415b: PASS»). Re-run at this fill from the archive of 4c2e5124: PASS ((10)).
- G-13, THE REFEREES' ROUNDS (note). L-1 (36418d16): REFEREE (eaa941b9) SIGN W-ONLY (a)-(d), NOW-ONCE (a)-(c), SWAP, SWAP-RUN, FLIP-1;
  DEAD SC-ISO «SIGN AS CONDITIONAL, gap FL-G1»; line «NOT YET: REQUIRED FL-L1, FL-L2, FL-L3» (l. 9-19, 129-143). REFEREE-2 (dc622d03)
  SIGN all, DEAD «**SIGN WITH GAP G-FLIP-1**»; line «**MATCHES** (optional P-1 to P-3)» (l. 10-19, 117-133). Fix round (fixes entry 1,
  L-2): FL-L1 by F-a (extension), FL-L2 by F-b, FL-L3 by the label; optional P-1 and P-3 taken; F-c answers REFEREE-2's F-1 (a remark);
  P-2 needed no change. L-2 (8099415b): REFEREE §C (74fae0fa) l. 192 «VERDICT: line L-2 MATCHES.», with F-a and F-b SIGN; REFEREE-2
  (8b53a9e2) «## Line L-1 → L-2: MATCHES» (L2 file l. 22), with F-a and F-b SIGN and a byte test (l. 23-26).
- G-14, THE FIXES FILE CARRIES SIGNED CONTENT (note; new for this entry). F-a (NOW-ONCE (b′), any G ∈ 𝓛^R_d) and F-b (SWAP-RUN for any
  q) are new signed statements, proved in docs/new/P-IDEAL-FLIP-fixes.md (fixes l. 9-19, 22-33), not in the frozen packet; both referees
  signed them in their second rounds (REFEREE §C l. 166, 173; REFEREE-2 L2 file l. 9, 15). The entry lists them as signed, with their
  source (Claims (c), (e)); the packet's (b) and its SWAP-RUN with the caveat stay signed and are implied by them.
- CLEAN AT L-2 (the pre-check against CHECKER's recurring items, by script on 8099415b):
  C106 E-1 (old line as current): L-2 is the current line; no L-3 exists (docs/new/P-IDEAL-FLIP-line-L3.txt absent at the l-new head
  4c2e5124); L-1 appears only in the line history.
  C113 E-1 (title «verbatim» after an insertion): no insertion; the title is byte-equal to prefix + L-2 + fill (Addendum (2)).
  C113 E-2 (trunk status that goes stale): the body has no trunk statement (header).
  C114 Add. 1 E-1 (UPDATE date): <DATE> placeholder.
  C115 E-1 (premise route): G-4, G-5.
  C110 F-1 / C116 G-3 (pins): G-12.
  C111 E-1 (stale Lead-reading statements): G-10.
  C116 G-2 (name clash): G-6, one body sentence.
  C117 E-1 (a sentence wider than signed; DATA scope): G-2, G-9; the body's Data sentences give each count's genome set and unit.
  C117 E-2 (instance under-specified): the body inlines iso_d4_st9 (every option field, the start, the twelve states) with its full
  sha1, path and commit, and the two FLIP-1 instances likewise.
  C118 E-1 (stale status sentence): no «pending» in the entry; the audit status is dated and attributed (G-8 (d)).
  C118 §3 / Erratum E-2 lesson (definitions diffed): G-2.
  C120 §5 G-9 / C121 E-1 (DATA count without its statements): MET by the letter; G-9 (ii) for CHECKER's ruling.
  C120 §3 note («…» that is not a quotation): NOTE, G-8 (c).
  «|»: 0 in L-2, 0 in the entry block, 0 in the UPDATE (by script, Addendum (3)).
  Parentheses: NOT balanced in L-2 (G-0, new).
(0) PLACEMENT. R110 goes DIRECTLY AFTER R109's block. docs/RESULTS.md at local trunk 08c460d1 (= origin trunk 61a1175c for this file)
has sha1 6772d9c4efc7d723d4064ab47f9e5f823ec52904, 11,901 lines (wc -l), last changed by 67ec1151 (R109's landing). «### R108» is l.
10812; «### R109» is l. 11030 (entry l. 11030-11321, l. 11322 blank); «**Erratum E-1**» is l. 11323; «**Erratum E-2**» is l. 11336; «##
Dead ends (kept;» is l. 11364; DE36 begins at l. 11885. PROPOSED (R102's to R109's layout): insert R110's entry after l. 11322 (R109's
blank line), with one blank line after it, so the R-entries stay contiguous and both errata follow them. "### R110" occurs 0 times in
RESULTS and GAPS; «R110» 0 times. GAPS has sha1 b79c582ce9bed929a6df54a7fdc88e5c629aced9, 23 lines, last changed by 67ec1151. The Lead
re-checks (6) and (9) at landing only if RESULTS or GAPS change after 67ec1151. R109's own landing followed its draft's simulation
exactly (C121 Add. 2).
(1) TITLE. The title is the line file docs/new/P-IDEAL-FLIP-line-L2.txt (l-new 4c2e512421db51180279a63475e98d1081414e8d,
2026-11-05T11:49:46Z, the file's only commit, sha1 8099415b58689ea9241f2da9d642ba8a1af74cf9; it is the l-new head), verbatim: one line,
no outer quotes, no final period, 4,301 characters (4,433 bytes plus the newline), 810 whitespace tokens, 51 «(» / 50 «)» (depth never
negative; the DATA parenthesis unclosed, G-0), one guillemet pair (SC-ISO's text) and six «…». NO HEADING MARKER, verified by script:
the file begins «In the IDEAL model of RESULTS R104», with no «#». NOTHING is stripped and NOTHING is inserted: the heading is the
level-3 marker, then "R110 [refereed-only] ", then the file without its newline, then the fill ", CHECKER PASS (docs/checker/C122.md,
checker PENDING)" (as R90-R109). C122 is free: docs/checker/C122.md is absent at the checker head 177f8368, «C122» occurs 0 times in
RESULTS and GAPS, and notes/CHECKER.md l. 14 says «NEXT: the next new check is C122 (the Lead routes it).»; LEAD-STATE (11:11Z) names
«C122 = R110». L-2 holds one « — », its own date parenthesis «(2026-11-05)» and no "|" (G-1). Built by script (fill110.py: assert the
sha1 8099415b…, equality with the blob at 4c2e5124 and at the l-new head, one line, no marker, one « (2026-11-05) — », no "|"; prepend,
append) and re-checked after writing this file: equal, byte for byte. Heading: 4,380 characters, 4,512 bytes; sha1 of the
heading line without its newline 6298cee3b8daeefe3d0ae9db6423deea769578c3; it is l. 459 and the only «### R» line of this file.
(2) LINE HISTORY: two lines. L-1 36418d164ac759472fadf0b411d81901db32e6da (9effea1f, frozen with the packet; first written at e93b0e82,
09:46:11Z, «draft (not frozen)», sha1 b755af14…; 4,396 bytes, 803 tokens, 49 «(» / 48 «)»): REFEREE required FL-L1 to FL-L3, REFEREE-2
MATCHED with optional P-1 to P-3 (G-13). L-2 8099415b58689ea9241f2da9d642ba8a1af74cf9 (4c2e5124; 4,433 bytes, 810 tokens): fixes entry 1
lists 3 word-diff hunks (fixes l. 49-56); my token diff L-1 → L-2 (difflib on whitespace tokens, wdiff110.py) finds 3 non-equal hunks,
the same 3 («DEAD:» → «CONDITIONAL DEAD (premise T^R(3) ≤ 8, machine):»; the insertion «from any state with q at 0 and 1»; «start for d
≤ 4, 40 random starts otherwise);» → «start);»), and L-1 with the three replacements of REFEREE-2's byte test (L2 file l. 23-26) equals
L-2 byte for byte (True); REFEREE l. 186 «L-2: my own word diff (git diff --word-diff) finds exactly 3 hunks, equal to entry 1's list.».
No hunk changes a definition; F-a and F-b change what the line's unchanged words are proved by (G-14). So the title is L-2, and L-1 is
history.
(3) THE LINE AT BOTH REFEREES. REFEREE successor 23, docs/referee/R-P-IDEAL-FLIP.md: report eaa941b9 (2026-11-05T11:14:44Z, new file,
159 lines, sha1 40a4a1ba8ad3d59c5a2f392e3425240290fff217), §C 74fae0fa (12:55:02Z, 198 lines, sha1
333749f26b47f580c3c74f67dc7cee335e84933a): l. 192 «VERDICT: line L-2 MATCHES.». REFEREE-2 successor 27:
docs/referee-2/R2-P-IDEAL-FLIP.md (dc622d03, 11:17:53Z, new file, 136 lines, sha1 f7e1a3bd259f17b0c2049af4cdb4a3dc7dabfe99; unchanged at
b2c0fff8): L-1 «**MATCHES**»; docs/referee-2/R2-P-IDEAL-FLIP-L2.md (8b53a9e2, 12:54:46Z, new file, 30 lines, sha1
96faae6e865c9f116907417e1c8d8d521e0766d8): «## Line L-1 → L-2: MATCHES» (l. 22). Both MATCH L-2.
(4) CLAIMS SIGNED = the items below, each SIGN in BOTH referees' verdicts (REFEREE "## 0. Verdicts" l. 9-19 and §C l. 166, 173, 192-194;
REFEREE-2 "## Verdicts" l. 10-19, "## Signatures" l. 134-136, L2 file l. 9, 15), checked clause by clause against the packet and the
fixes; the cells are the reports' words:
| item (source) | REFEREE (successor 23) | REFEREE-2 (successor 27) |
| --- | --- | --- |
| (a) Lemma W-ONLY (a)-(c) (packet §2 l. 72-79, proofs l. 81-101) | l. 12 «SIGN»; §2 l. 32-43 | l. 13 «**SIGN** (Opus 5.5, D12)»; l. 38-43 |
| (b) Corollary W-ONLY (d) (§2 l. 80, proof l. 102-106) | l. 12 (the same row); §2 l. 44-47 | l. 14 «**SIGN** (Opus 5.5, D12)»; l. 44-45 |
| (c) Lemma NOW-ONCE (a), (b), (c) (§3 l. 109-125) and (b′) (fixes F-a l. 8-19) | l. 13 «SIGN (note FL-N1: (b) does not need ISO)»; §C l. 166 «F-a, NOW-ONCE (b′) without ISO (new signed content): SIGN.» | l. 15 «**SIGN** (Opus 5.5, D12)»; L2 file l. 9 «F-a, NOW-ONCE (b′) without ISO (new signed content): SIGN (Opus 5.5, D12).» |
| (d) Lemma SWAP (§4 l. 128-136) | l. 14 «SIGN» | l. 16 «**SIGN** (Opus 5.5, D12)» |
| (e) Corollary SWAP-RUN (§4 l. 137-146), in the F-b form (fixes l. 21-36) | l. 15 «SIGN (note FL-N2: the «no such q» caveat is removable)»; §C l. 173 «F-b, SWAP-RUN for ANY q (exchange argument): SIGN.» | l. 16 (the same row) «(N-1: the «no q» caveat is unnecessary)»; L2 file l. 15 «F-b, SWAP-RUN with ANY q: SIGN (Opus 5.5, D12).» |
| (f) Proposition FLIP-1 (§5 l. 149-176) | l. 16 «SIGN» | l. 17 «**SIGN** (Opus 5.5, D12)» |
| (g) DEAD SC-ISO by iso_d4_st9, CONDITIONAL on T^R(3) ≤ 8 (§6 l. 178-195) | l. 17 «SIGN AS CONDITIONAL, gap FL-G1 (machine premise T^R(3) ≤ 8). The unconditional part, «SC-ISO at d = 4 ⇒ T^R(3) ≥ 9», is SIGNED» | l. 18 «**SIGN WITH GAP G-FLIP-1** (Opus 5.5, D12): ruling below»; l. 80-81 signed content (i)-(iii) |
Both, verbatim: REFEREE §C l. 193-194 «Signed: W-ONLY, NOW-ONCE (incl. (b′)), SWAP, SWAP-RUN (F-b form) and FLIP-1.» «SC-ISO is
CONDITIONAL DEAD (gap FL-G1), and its implication «SC-ISO at d = 4 ⇒ T^R(3) ≥ 9» is signed.»; REFEREE-2 l. 135-136 «W-ONLY (a)-(d),
NOW-ONCE, SWAP / SWAP-RUN, FLIP-1: SIGN (Opus 5.5, D12). DEAD SC-ISO: SIGN WITH GAP G-FLIP-1 (machine premise T^R(3) ≤ 8; signed content
(i)-(iii) above).». The two gap labels name the same gap (FL-G1 = REFEREE-2's G-FLIP-1 on P-IDEAL-FLIP: the machine premise T^R(3) ≤ 8).
F-c is «CORRECT» at both (REFEREE §C l. 181; REFEREE-2 L2 file l. 18) and is an unsigned remark.
Clause checks (L-2 against the packet and fixes; G-2): the setting = §1 l. 51-70; W-ONLY = l. 73-80; NOW-ONCE = l. 113-116 and F-a; SWAP
= l. 128-131 and F-b; FLIP-1 = l. 149-176; DEAD = l. 179-193. Nothing in L-2 is wider than signed (G-2 (viii), (x) are precision notes).
Signed by both, NOT stated by L-2 as separate items: W-ONLY (b)'s Ξ-value half and «So Step^c_G(s)|U is a function of s|U and c.» (l.
74-75); NOW-ONCE (c) (l. 117-118); the key facts KP_s / KP^c (l. 110-112); G^swap ∈ 𝓦_d and «G is ISO iff G^swap is.» (l. 129-130);
«moves = the sum of the pieces' lengths» (F-b l. 27); the frame-by-frame runs of I-0 and I-1 (l. 165-175). Not signed, so NOT landed:
packet §7 (DATA, machine checks, EXCLUDED, TARGET diff, READING; «DATA / READING (not to sign)», l. 17), in particular the T_k(m) table
(l. 198-211) and the T^R values (l. 216-217); fixes F-c (a remark; fixes l. 42 «Corrected remark (not a signed statement; no bound is
claimed)»); the machine premise T^R(3) ≤ 8 itself.
(5) OTHER TEXTS THE ENTRY DEPENDS ON: RESULTS R104's definition of the IDEAL model (title l. 9864; no R104 theorem); RESULTS R109's
SEG-ONCE (title l. 11030), at l = −1. Nothing else for a signed statement. The lane sources docs/new/N5-SLOT-box160.md §1 and
docs/new/N5-FLIPADD-box161.md §1 (packet l. 3-4) are history only; the DEAD instance and the FLIP-1 instances are data files ((10)); the
machine premise is the DEAD item's listed gap (G-8).
(6) PREMISE LABELS (stale-label test; RESULTS at 67ec1151's version, GAPS likewise). RESULTS labels in L-2 (by script): «R104» 3
(«RESULTS R104», «R104's definition», «theorem of R104»); «R109» 3 («RESULTS R109's SEG-ONCE», «R109's T*(d)», «R109's 𝓛_d»; «𝓛_d»
itself twice); «R197» 1, an L-RED convention label, prefixed («L-RED's R197 convention»). R104 (l. 9864) exists and carries the
definition. R109 (l. 11030) exists and carries SEG-ONCE, 𝓛_d and T*(d). No erratum touches R104 or R109 (E-1: R97-R100 counts; E-2:
R105). No Lead reading and no other RESULTS label is cited. G-N5-TIME open (GAPS l. 11).
(7) SYMBOL TEST of the title (my own strict test of every symbol of L-2; IN = bound in the line; else the carrier):
| symbol | where |
| --- | --- |
| IDEAL model, Ξ-graph, acyclic, mover, level, option, W-target, Ξ-target, gate g, step, run, start, state, A-set, key | RESULTS R104 (the premise; packet §0) |
| SEG-ONCE at l = −1 | RESULTS R109 (the premise; G-4) |
| 𝓛_d, T*(d) | RESULTS R109's definitions, named to keep apart (G-4) |
| 𝓦_d, 𝓛^R_d, T^R(d), ISO, b_0, c-step, κ^c, T_k(m), u_t, c_t, q, G^swap | IN |
| d, m, k | free in the definitions; «(d ≥ 2)» in W-ONLY's corollary; NOW-ONCE and SWAP vacuous at d = 1 (G-3 (i)) |
| levels ≥ 1 | U of packet §1 |
| two fixed IDEAL genomes | H_q and (G^swap)_q of F-b (G-2 (x)) |
| SC-ISO's text in «…» | the line's wording of §6 l. 180 with seg1 / tail spelled out (G-2 (xii)) |
| iso_d4_st9, kf0_d2_t2.json, kf1_d2_t3.json, sha1s | data objects ((10); body Claims (f), (g)) |
| L-RED's R197 convention, L-RED's encoding | attributions, prefixed |
| CONJECTURES FLIP-ADD, SLOT-TRADE | named as not claimed (packet l. 6-7, 227) |
| DATA clause | per statement (G-9) |
Agreeing tests: REFEREE §6 l. 118-143 and §C l. 186-191; REFEREE-2 l. 117-133 and L2 file l. 22-30.
(8) FIXES AND STATUS NOTES (docs/new/P-IDEAL-FLIP-fixes.md, L-NEW successor 53, append-only, one entry, one commit): at 4c2e5124 sha1
f8d3677e4754fde9922208782483f9d4bff168ac, 57 lines. Header l. 1-2 («(append-only; the packet docs/new/P-IDEAL-FLIP.md, sha1 92803bd5…,
frozen 9effea1f, is NOT edited)»). Entry 1 (l. 4-57): «Makes line L-2 (docs/new/P-IDEAL-FLIP-line-L2.txt). No signed statement is
weakened; F-a and F-b extend two statements, F-c corrects a «does NOT claim» remark;» (l. 5-6); F-a (l. 8-19, REFEREE FL-L1: NOW-ONCE
(b′) without ISO, with its proof); F-b (l. 21-36, REFEREE FL-L2 = REFEREE-2 N-1: SWAP-RUN for any q, with its proof); F-c (l. 38-47,
REFEREE-2 F-1: the remark corrected via R109's SHIFT); the L-1 → L-2 word diff, 3 hunks (l. 49-56); «Nothing else changed.» (l. 57). The
packet file itself is unchanged since 9effea1f (sha1 92803bd5… at 9effea1f and at 4c2e5124).
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-2 states no CONJECTURE as claimed and kills nothing of RESULTS or GAPS (SC-ISO and
FLIP-ADD occur 0 times there; SLOT-TRADE is R109's open conjecture and stays open). A line-11 UPDATE is proposed at the end, to go AFTER
R109's UPDATE (GAPS at 67ec1151: the last UPDATE on l. 11 is R109's «UPDATE 2026-11-04 23:38Z: RESULTS R109 (P-IDEAL-SLOT; CHECKER C121
9f9c60c0) [refereed-only] LANDED: …», ending «G-N5-TIME stays open.» before the row's closing « |»; l. 11 holds 76 "|" and 44 «UPDATE
2026-»), as a pure insertion with one separating space. BUILT FROM L-2 (scratch upd110.py = upd109.py's controls and procedure
unchanged, plus R109's control; upd100L3.py's build() unchanged). CONTROLS (same script, same run, rc 0): R97's to R109's LANDED UPDATEs
(GAPS l. 11 at 67ec1151) rebuilt from their lines byte for byte (True ×13; R109's from P-IDEAL-SLOT L-4 at d488d06d with head «UPDATE
2026-11-04 23:38Z: RESULTS R109 (P-IDEAL-SLOT; CHECKER C121 9f9c60c0) [refereed-only] », 3,508 bytes, also equal to R109-draft l. 824
and to r109/upd109.txt with <DATE> 2026-11-04, <HH:MM> 23:38, <checker> 9f9c60c0). R110: the R107 / R108 / R109 procedure (C121 §4 «The
token diff against L-3 is the R107 / R108 rule»): L-2's claim body ends with the unlabelled clause «; and CONDITIONAL DEAD (premise
T^R(3) ≤ 8, machine): the lane conjecture SC-ISO … forces T^R(3) ≥ 9)» after the last labelled clause (FLIP-1); the procedure runs on
L-2 with that clause cut out (build()'s label move on the claim body plus a sentinel tail, start «where u_t is the c_t-step of u_(t−1):
», 4 labels, each found once after it, in order; « (2026-11-05) — » → «: »; the DATA parenthesis before the source parenthesis opened as
«; DATA: …»; «; G-N5-TIME stays OPEN» and «; not M3, not a step-4 pass, not a TARGET.md claim» dropped; the source parenthesis kept; «.
G-N5-TIME stays open.» appended), and the clause is put back verbatim between the moved «(FLIP-1)» and the tail's «: » (one occurrence,
by script). ONE ADAPTATION (G-0): the tail step needs a closed DATA parenthesis; it is run on L-2 with the missing «)» inserted before «
(P-IDEAL-FLIP, » and cross-checked against opening L-2's unclosed DATA parenthesis directly (drop its «(» only): the two tails are equal
(True), so the UPDATE does not depend on where the missing «)» would go. The W-ONLY clause keeps its inner «; under ISO» and «; hence»
(build() cuts at the last «; » before the next label). L-2 holds no "|", so no replacement list. Checked by script: one line, 0 "|", one
«<DATE>», one «<HH:MM>», one «<checker>», 4,468 bytes, 809 tokens, 42 «(» / 42 «)»; «2026-11-05» 0 times; token multiset diff against
L-2 = the head, the four moved labels, «(DATA:» opened, the two dropped scope sentences, « — » and the final sentence (upd110.out). Head
«UPDATE <DATE> <HH:MM>Z: RESULTS R110 (P-IDEAL-FLIP; CHECKER C122 <checker>) [refereed-only] » («P-IDEAL-FLIP» 0 times in GAPS); <DATE>
= the landing date.
(10) DATA of record = packet §7 (l. 197-236), NOT signed; L-2's DATA parenthesis states its counts per statement (G-9). Re-run at this
fill (scratch, git archive of 4c2e5124's experiments/new and docs/new; box150, box160 and box162 are unchanged from 9effea1f to
4c2e5124, git diff --stat lists only docs/new files and check.sh), check.sh l. 1-5 plus «set -euo pipefail», the «cd» and the «tmp»
line, then l. 903-911, 2026-11-05T14:12:13Z-14:13:02Z, rc 0:
- PASS line: «P-IDEAL-FLIP: flipcheck 0 violations (controls fire), instance iso_d4_st9 (T 11, seg1 6, tail 3), FLIP-1 instances V_0 2 /
  V_1 3; pins packet 92803bd5, line L-1 36418d16, instance 7ca1e68c, I-0 c2233e05, I-1 d368d441, fixes f8d3677e, line L-2 8099415b:
  PASS».
- w162 raw: «RANDOM seed 162 genomes 300 + corpus 50 runs 38912 steps 44084 states 7830 WONLY 0 ISOA 0 FROZ 0 CONS 0 SWAP 0 SWAPNEG
  12594 NOWONCE 0 NOWCTRL 307 FLIP1 0»; «CHECKED WONLY 44084 ISOA 31320 FROZ 1044 CONS 28896 SWAP 15660 NOWONCE 307 FLIP1 1312»; «INST
  iso_d4_st9 LR True ISO True d 4 T 11 level-0 steps [7, 8] seg1 6 tail 3»; the WIT lines, among them «WIT kf0_d2_t2.json LR True ISO
  True V_0 2» and «WIT kf1_d2_t3.json LR True ISO True V_1 3» (twelve more, for the §7 table, not used); the box 150 checker «TOTAL
  genomes 1 runs 1 steps 11 XSIM 0 TOPO 0 MONO 0 XINEW 0 RISE 0 CHAIN 0 KEYFLIP 0 DECR 0 TOPMONO 0 RBOUND 0 RESTR 0 ICHARGE 0 REC 0 VIOL
  0 (info REC148 0)». Equal to both referees' runs at 9effea1f (REFEREE l. 104-111; REFEREE-2 l. 96-98).
- My split of the genome sets (fcstats.py: flipcheck.py run unchanged with one recording line; fcstats.out): random 300 = 100 each at d
  = 2, 3, 4; 225 drawn ISO, 75 drawn without the constraint (65 non-ISO, 10 ISO by chance); corpus 50 (d = 2: 8, 3: 29, 4: 13; 36 ISO);
  every genome d ≤ 4; runs 38,912 = Σ 2^N (every start), ISO runs 28,896; ISO genomes used by the ISO-only checks 261 (82 of them with d
  = 2: 82 × 16 = 1,312 FLIP-1 pairs; 261 × 4 = 1,044 FROZ pairs; 261 × 120 = 31,320 ISOA pairs; 261 × 60 = 15,660 SWAP pairs).
- My own checks (mysim110.py, mysim110.out): the three instance files equal the packet's option tables field for field (iso_d4_st9 16
  options, I-0 and I-1 8 each: True ×3); each is valid (acyclic, ranks and gates distinct, W one level down), in 𝓛^R and ISO; my R104
  simulator runs iso_d4_st9 from its stored start through the twelve states of packet §6 (True), T 11, mover 1 moving at step 7 and
  mover 0 at step 8, seg1 6, tail 3; my forced runs: I-0 with c = (0, 0, 0) U-frames (0, 0), (0, 1), (1, 1), (1, 1), moves 2, flips 0;
  I-1 with c = (0, 1, 1) U-frames (1, 0), (1, 1), (0, 1), (0, 0), moves 3, flips 1; my V_k from the stored starts, k = 0, …, 6: I-0 [2,
  2, 2, 2, 2, 2, 2], I-1 [1, 3, 3, 3, 3, 3, 3] (REFEREE l. 95-97 and REFEREE-2 l. 68-70 report the same).
- Word diff and byte test: wdiff110.py / wdiff110.out ((2)).
NOT re-run: the referees' tools (docs/referee/scratch/flip_probe.py; docs/referee-2/R2-P-IDEAL-FLIP/flip_check.py); I read REFEREE's
committed log (xinew_logs/flip_probe.txt at eaa941b9: the instance line, «kf0_d2_t2.json LR True ISO True frames [[0, 0], [0, 1], [1,
1], [1, 1]] moves 2 V_0 2 V_1 2 V_6 2», «kf1_d2_t3.json LR True ISO True frames [[1, 0], [1, 1], [0, 1], [0, 0]] moves 3 V_0 1 V_1 3 V_6
3», 6,400 pairs, 367 steps, «violations {'v0': 0, 'vk': 0, 'wonly': 0}»), which equals REFEREE §3 l. 89-100; REFEREE-2 committed no log
for flip_check.py. The SAT runs of the T_k(m) table and of T^R(3) (§7; lane DATA, not signed), L-COMP's cubes and REFEREE-2's re-run of
them: not run. check.sh's other blocks and scripts/verify.sh: not run.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 L-2's unbalanced parentheses (G-0). D-2 fixes l. 4 «Lead 11:49Z fix
round» against the Lead commit ca8c640a (11:48:17Z) and the lane commit 4c2e5124 (11:49:46Z); packet l. 2 «Lead brief BOX 162
(2026-11-05)» against ef4150d5 (09:29:14Z) and the freeze 9effea1f (10:21:28Z); stamps not verifiable from the repository. D-3 the
packet's «3 of 4 ISO» / the line's «a quarter of them not ISO» against the measured 65 non-ISO of 300 (G-9 (i)). D-4 packet l. 181
«(sha1 in §7)», which §7 does not print (G-11 (iv)). D-5 REFEREE l. 98 «400 random ISO genomes of 𝓛^R_2 × 16 starts = 6,400 pairs» and
REFEREE-2 l. 105 «200 random ISO 𝓛^R_2 genomes × 16 starts (3,200 pairs)» are the referees' own sets, not the lane's 1,312 pairs. D-6
REFEREE-2 l. 2-3 «Independent: docs/referee/ not read for this packet before this push.» with its push at 11:17:53Z, 3 min after
REFEREE's report commit 11:14:44Z (independence as stated; REFEREE l. 2 «Independent: I did not read docs/referee-2/.»). D-7 REFEREE-2
uses the label «G-FLIP-1» for this packet's gap and, as successor 16, for P-N5-FLIP's gap (RESULTS R69; notes/REFEREE-2.md l. 778); G-6
(b). D-8 REFEREE l. 24 cites «trunk 42c7711b, RESULTS l. 11030»: true (RESULTS unchanged from 67ec1151 to 61a1175c). No discrepancy
between a report and the lane files beyond these.
(12) Excluded: packet §7 (T_k(m) table, T^R values, machine checks, the encoding READING, EXCLUDED, TARGET diff, READING); CONJECTURES
FLIP-ADD and SLOT-TRADE (l. 227); every READING and DATA row of docs/new/N5-SLOT-box160.md and docs/new/N5-FLIPADD-box161.md (l.
227-229); fixes F-c (remark); the machine premise T^R(3) ≤ 8 and its status (L-RED's xcnf.py, L-COMP's box 27, REFEREE-2's audit): DATA
about the gap, not part of this entry beyond G-8 (d) and Honest limits (iii); the referees' own probes and counts (Data bullet only).
Not part of this entry.
(13) Commits: lane (claude/l-new): e93b0e82 (2026-11-05T09:46:11Z; packet draft «not frozen», L-1 draft, flipcheck.py, the two FLIP-1
instances) → 9effea1f (10:21:28Z; freeze: packet 92803bd5 (236 lines), L-1 36418d16, check.sh block P-IDEAL-FLIP) → 4c2e5124 (11:49:46Z;
fixes entry 1 +57, L-2 +1, pin162 extended). The DEAD instance: experiments/new/box160/out/iso_d4_st9.json (l-new 279dd656,
2026-11-05T02:20:19Z, «L-NEW box 160: d 3 exact channel table; ISO d 4 seg1+tail 9 witness», its only commit). REFEREE (claude/referee):
eaa941b9 (11:14:44Z; report, new file 159 lines; scratch/flip_probe.py 75 lines, sha1 b1acee9b55c824fdb86db08724c5ec4d81765ac3;
xinew_logs/flip_probe.txt 4 lines, sha1 350019bb6600b9529acdae4c127640ffdc7f762e) → 74fae0fa (12:55:02Z; §C, +39 lines; handover note in
notes/REFEREE.md). REFEREE-2 (claude/referee-2): dc622d03 (11:17:53Z; report, new file 136 lines; R2-P-IDEAL-FLIP/flip_check.py 203
lines, sha1 ae91714fe49908c635bbccffcd55df878358e865) → d1c4a530 (12:49:17Z; R2-T3R-audit.md, 66 lines, sha1
751979956af86ebb7c65348726720beb4ee1fc71; status only) → 8b53a9e2 (12:54:46Z; L2 file, new, 30 lines) → b2c0fff8 (13:38:20Z; handover).
L-COMP (claude/l-comp): 6f19564f (11:50:27Z; box 27 ENCODING.md, 64 lines, sha1 2ba6b1a0aeb4ef7079878f98b52acacc2404741f; status only).
CHECKER: 177f8368 (01:20:50Z; C121 closed; C122 next). Lead: ef4150d5 (freeze GO), 92a78041 (to the referees), ca8c640a (fix round),
61a1175c (audit routed). Trunk: see the header.
(14) Placement: see (0). DEAD-ENDS ROW: NONE (not drafted). R110 kills a lane conjecture (SC-ISO), CONDITIONALLY, by an explicit
refereed instance inside its line. CHECKER C118 §5 confirmed «no row» for lane conjectures killed inside a landed line («DE37: the
Lead's «no row» is CONFIRMED.», with REP-LIN, BIP-REL-1, frz32, fbg_K12 and odxi as precedent, and «DE34-DE36 are candidate algorithms
and a proof route, a different class.»); C120 §5 and C121 §6 applied it to R108's REPLAY and R109's SEG1-2D («No Dead-ends row: agreed
(C118 §5).»). Here a row would also overstate: the kill is conditional on a machine premise. SC-ISO occurs 0 times in RESULTS and GAPS,
so no fleet conjecture or route depends on it; R110's line records the instance, its numbers and the premise, and the body inlines the
instance (Claims (g)), so CLAUDE.md's «Record every dead end with the exact obstruction and the instance that killed it.» is met inside
RESULTS. The packet has ONE DEAD item: the lane's «single-channel trade» is killed only in its W-channel ISO form SC-ISO (packet l.
179-180); its NOW-channel form is not claimed (l. 194), so there is no second dead end to record. The next free Dead-ends number stays
DE37 («DE37» 0 times in RESULTS).
### R110 [refereed-only] In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of R104 used; and RESULTS R109's SEG-ONCE at l = −1 only), on acyclic Ξ-graphs, with 𝓦_d the genomes with levels 0, …, d − 1 whose level-0 movers are exactly two movers named 0 and 1, 𝓛^R_d ⊆ 𝓦_d the 2-wide degree-2 ladders in L-RED's R197 convention (movers 2l and 2l + 1 on level l, all of degree 2, no other movers, option k of a mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k), T^R(d) the largest number of steps over 𝓛^R_d and all starts (kept apart from R109's T*(d) over 𝓛_d; T^R(d) ≤ T*(d)), ISO the property that no option has Ξ-target 0 or 1, b_0(s) = 1 iff g(0, s(0)) < g(1, s(1)), for c ∈ {0, 1} the c-step the step rule on the movers of level ≥ 1 (A-sets under the old state, keys under the new state, movers 0 and 1 kept) with every level-1 option W-pointing to mover w keyed by (κ^c_w, its own gate), κ^c_0 = 1 − c, κ^c_1 = c, and T_k(m) the supremum, over the ISO genomes of 𝓛^R_(m+1), their starts u_0 and the bit sequences c_1, …, c_L with at most k changes, of the number of t with u_t ≠ u_(t−1) on the levels ≥ 1, where u_t is the c_t-step of u_(t−1): (W-ONLY) on 𝓦_d every step of a run equals, on the levels ≥ 1, the c-step with c = b_0 of the new state; under ISO the A-sets of the levels ≥ 1 do not depend on the options of 0 and 1, and freezing 0 and 1 at options q gives an IDEAL genome whose run from any state with q at 0 and 1 is the iterated b_0(q)-step; hence every run of an ISO genome of 𝓛^R_d (d ≥ 2) has T ≤ T_2(d − 1) + 2; (NOW-ONCE) on 𝓛^R_d, on an interval of steps over which b_0 of the states is constant, and in a c_t-step sequence on an interval over which c_t is constant, every level-1 mover moves at most once; (SWAP) on 𝓛^R_d, the (1 − c)-step of G equals the c-step of G^swap, the genome G with the W-targets of the two options of every level-1 mover exchanged (in R109's 𝓛_d, not in 𝓛^R_d), so under ISO a c_t-step sequence with k changes is a concatenation of at most k + 1 runs of two fixed IDEAL genomes; (FLIP-1) T_0(1) = 2 and T_k(1) = 3 for every k ≥ 1 (upper bounds by proof; lower bounds by two explicit instances, experiments/new/box162/out/kf0_d2_t2.json, sha1 c2233e05…, and kf1_d2_t3.json, sha1 d368d441…); and CONDITIONAL DEAD (premise T^R(3) ≤ 8, machine): the lane conjecture SC-ISO («for every d ≥ 3, in every run of every ISO genome of 𝓛^R_d, the number of steps before the first step that moves 0 or 1 plus the number of steps after the last such step is at most T^R(d − 1)») is false, by the ISO genome iso_d4_st9 of 𝓛^R_4 (experiments/new/box160/out/iso_d4_st9.json, sha1 7ca1e68c…; T 11 from its stored start, mover 1 moving at step 7 and mover 0 at step 8, 6 + 3 = 9 steps outside) together with the machine premise T^R(3) ≤ 8 (CaDiCaL UNSAT on L-RED's encoding, not Lean, not refereed; without it the instance shows that SC-ISO at d = 4 forces T^R(3) ≥ 9) (2026-11-05) — a REDUCTION of the W-channel part of SLOT-TRADE to an external-flip model inside the IDEAL model; bounds nothing polynomially; the CONJECTURES FLIP-ADD and SLOT-TRADE are not claimed; Ξ-cyclic genomes and genomes outside 𝓦_d are not covered; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (DATA: W-ONLY, step form: experiments/new/box162/flipcheck.py, 0 violations on 44,084 real steps (300 random 𝓛^R genomes with d = 2, 3, 4, 225 of them drawn ISO and 75 drawn without that restriction, 65 of these not ISO, and the 50 𝓛^R genomes in box160/out and box162/out, 36 of them ISO, every start); W-ONLY, ISO independence: the same tool, 0 violations on 31,320 (state, q) pairs of the 261 ISO genomes among them (the 225 drawn ISO and the 36 ISO corpus genomes); W-ONLY, frozen form: 0 violations on 1,044 (ISO genome, q) pairs; T ≤ T_2(d − 1) + 2: 0 violations on 28,896 ISO runs (b_0 changing at most twice and the steps moving levels ≥ 1 at most the exact per-genome maximum with two changes); NOW-ONCE, real runs: 0 violations on 307 pairs of consecutive moves of a level-1 mover; SWAP: 0 violations on 15,660 (state, c) pairs of the same 261 ISO genomes (no non-ISO genome tested); FLIP-1 upper bounds: 0 violations on 1,312 (2-level ISO genome, start) pairs, k = 0, …, 6; SC-ISO: the instance replayed by the same tool and by the box 150 checker; NOW-ONCE for c_t-step sequences, the concatenation clause of SWAP and the T_k(m) values for m ≥ 2: no signed DATA (the packet's §7 table is DATA only)) (P-IDEAL-FLIP, docs/new/P-IDEAL-FLIP.md with its fixes entry 1, docs/new/P-IDEAL-FLIP-fixes.md; L-NEW successor 53), CHECKER PASS (docs/checker/C122.md, checker PENDING)
- Object (L-NEW successor 53, Opus 5.5, D14 / D18; frozen, unchanged during review): packet P-IDEAL-FLIP, docs/new/P-IDEAL-FLIP.md, sha1
  92803bd5b750924f0d0bc7db3c57eddf5725dfcb, 236 lines (l-new freeze 9effea1f, 2026-11-05T10:21:28Z; identical at 4c2e5124 and 47b4e165).
  Both referees measured the sha1 (REFEREE l. 5 «packet 92803bd5 (236 lines);»; REFEREE-2 l. 6 «docs/new/P-IDEAL-FLIP.md sha1
  92803bd5b750924f0d0bc7db3c57eddf5725dfcb, 236 lines;»). Status (l. 5-7): «Not a TARGET.md claim. Every statement is about the
  IDEAL-ACYC model only. No polynomial bound is claimed. FLIP-ADD, SLOT-TRADE and G-N5-TIME stay OPEN.» To sign: §2 W-ONLY (a)-(d), §3
  NOW-ONCE (a)-(c), §4 SWAP and SWAP-RUN, §5 FLIP-1, §6 the DEAD of SC-ISO with its machine premise listed (table l. 10-17); §7 «DATA /
  READING (not to sign)». Sections: premises (l. 19-30), §0 the model (l. 32-50), §1 classes and the external-flip model (l. 51-70), §2
  (l. 72-107), §3 (l. 109-125), §4 (l. 127-147), §5 (l. 149-176), §6 (l. 178-195), §7 (l. 197-236). Sources (l. 3-4):
  docs/new/N5-SLOT-box160.md §1 and docs/new/N5-FLIPADD-box161.md §1 (successor 52); «This packet governs: every proof is written out in
  full here and is checked against this text only.» (l. 4-5).
  Fixes: docs/new/P-IDEAL-FLIP-fixes.md, append-only, entry 1 (4c2e5124; 57 lines, sha1 f8d3677e4754fde9922208782483f9d4bff168ac) and
  entry 2 (47b4e165; 81 lines, sha1 4220c44e6caa0bc6e2b2d4363ba3f5ec97505de6): F-a extends NOW-ONCE (b) to every genome of 𝓛^R_d (no
  ISO); F-b proves SWAP-RUN for any level-0 options q (the packet's caveat dropped); F-c corrects an unsigned remark; line L-2; entry 2
  makes line L-3. «No signed statement is weakened; F-a and F-b extend two statements, F-c corrects a «does NOT claim» remark;» (l.
  5-6).
  The RESULTS line is L-3, 4089bd73baf65929cf5b6094ef31882df817fd53 (docs/new/P-IDEAL-FLIP-line-L3.txt, l-new 47b4e165,
  2026-11-05T16:26:08Z, the file's only commit; 4,715 bytes). The title is L-3 verbatim, with nothing inserted (its date parenthesis
  «(2026-11-05)» and its source note are the line's own; the source note names the packet and its fixes entry 1, where F-a and F-b are).
  L-3's parentheses balance (53 «(» / 53 «)»): its DATA parenthesis closes before its source parenthesis. Line history: L-1 (36418d16,
  9effea1f, frozen with the packet); L-2 (8099415b, 4c2e5124, fixes entry 1: «CONDITIONAL DEAD (premise T^R(3) ≤ 8, machine)» for
  «DEAD», the frozen form's «from any state with q at 0 and 1», and «every start» in the DATA; my token diff equals the entry's 3 hunks,
  and L-1 with the three replacements equals L-2 byte for byte); L-3 (4089bd73, 47b4e165, fixes entry 2: CHECKER C122's four
  replacements R1-R4, DATA scope and source note only: the measured genome counts of the DATA (225 random genomes drawn ISO, 75 drawn
  without that restriction, 65 of these not ISO; 36 ISO corpus genomes; the ISO-only counts on those 261), the SWAP count bounded to the
  same 261 ISO genomes, the concatenation clause of SWAP added to the items without signed DATA, the DATA parenthesis closed, and fixes
  entry 1 named in the source note; no statement, definition or premise changes; L-2 with R1-R4 equals L-3 byte for byte, by my script).
  L-2 MATCHES at both referees: REFEREE (74fae0fa) l. 192 «VERDICT: line L-2 MATCHES.»; REFEREE-2 (8b53a9e2) R2-P-IDEAL-FLIP-L2.md l. 22
  «## Line L-1 → L-2: MATCHES», after a byte test (l. 23-26, «the result equals L-2 (True).»). L-3 MATCHES at REFEREE-2 (8fde383f, the
  same file, Addendum 1, l. 42 «- Verdict: L-3 MATCHES.»), after a byte test against C122 §5 (l. 36-37, «L-2 with R1, R2, R3, R4 applied
  equals L-3 exactly (True; 4,715 = 4,715 bytes).»); L-3 MATCHES at REFEREE (5c02d44d, R-P-IDEAL-FLIP.md §C add. 1, l. 211 «- Verdict: L-3 MATCHES (L-2 + C122 §5 R1-R4, nothing else).»), after its own byte test against C122 §5. Both diffed every definition of the line
  against the packet (REFEREE l. 118-128 and l. 191; REFEREE-2 l. 117-127); L-3 changes no definition.
- Claims signed (REFEREE successor 23 «(Opus 5.5, D15)», report eaa941b9, §C 74fae0fa; REFEREE-2 successor 27 «(Opus 5.5, D12/D19)»,
  report dc622d03, L-2 file 8b53a9e2). Items (a)-(f) are SIGN in both verdict tables (REFEREE "## 0. Verdicts" l. 9-19 of
  R-P-IDEAL-FLIP.md; REFEREE-2 "## Verdicts" l. 10-19 of R2-P-IDEAL-FLIP.md), the F-a and F-b forms in both second rounds (REFEREE §C l.
  166, 173; REFEREE-2 L2 file l. 9, 15); (g) is signed CONDITIONAL on the machine premise T^R(3) ≤ 8 by both (REFEREE l. 17, «gap
  FL-G1»; REFEREE-2 l. 18, «G-FLIP-1»: the same gap). (a) holds on 𝓦_d at any degree (its parts (b) and (c) under ISO); (b), (c), (d)
  and (e) on 𝓛^R_d (all movers of degree 2; (b) and (e) under ISO); (f) on the ISO genomes of 𝓛^R_2; (g) on the ISO genomes of 𝓛^R_4. No
  item bounds a count polynomially; W-ONLY (d) bounds T by T_2(d − 1) + 2 and leaves T_2 unbounded.
  (a) Lemma W-ONLY (a)-(c) (§2 l. 72-79): (a) [G ∈ 𝓦_d, d ≥ 2; no ISO needed] for every step t ∈ [1, T] of every run, s_t and
      Step^c_G(s_(t−1)) agree on U, «with c := b_0(s_t).»; (b) [G ∈ 𝓦_d, ISO] for x ∈ U, every option k and states s, s̃ that agree on
      U: «Ξ_s(x, k) = Ξ_s̃(x, k), hence A_s(x) = A_s̃(x).»; «(c) [G ∈ 𝓦_d, ISO, frozen form]» … «Then H_q is IDEAL-ACYC, and from every
      state s with s(0) = q(0), s(1) = q(1) the run of H_q is s, Step^c_G(s), Step^c_G(Step^c_G(s)), … with c := b_0(q), stopped at the
      first application of Step^c_G that changes nothing.». Here U is the set of movers of level ≥ 1, Step^c_G the c-step of §1 (l.
      62-65) and H_q the genome G in which 0 and 1 keep only the options q(0), q(1). Proof (l. 81-101): (a) by induction on the level:
      at level 1 the real key (g(w, s_t(w)), g(o)) and the c-key (κ^c_w, g(o)) order any two options alike, since both put mover 0's
      options first iff b_0(s_t) = 1 iff c = 1; above, the prefixes are the same options; both pick from the same A-set; (b) under ISO
      no chain of an option of U passes 0 or 1; (c) H_q is IDEAL-ACYC, lies in 𝓦_d, has b_0 constant = b_0(q) and the A-sets of G on U,
      and stops exactly when the c-step changes nothing. Cells: REFEREE l. 12 «SIGN»; REFEREE-2 l. 13 «**SIGN** (Opus 5.5, D12)».
  (b) Corollary W-ONLY (d) (§2 l. 80): «(d) Corollary [G ∈ 𝓛^R_d, d ≥ 2, ISO]: T ≤ T_2(d − 1) + 2, for every start.». Proof (l.
      102-106): with c_t := b_0(s_t), the forced run from s_0 under c_1, …, c_T equals the run on U (by (b), then (a)); c changes only
      at a step that moves 0 or 1, and «by RESULTS R109 SEG-ONCE (l = −1) each of 0, 1 moves at most once in the run», so flips ≤ 2 and
      the steps moving U number at most T_2(d − 1); the other steps move only level-0 movers, at most 2. Cells: REFEREE l. 12 (the same
      row); REFEREE-2 l. 14 «**SIGN** (Opus 5.5, D12)».
  (c) Lemma NOW-ONCE (§3 l. 109-125, and fixes F-a): for G ∈ 𝓛^R_d (d ≥ 2) and a level-1 mover x, x's key-smaller option is option 0 iff
      b_0(s) = 1 (real keys) and iff c = 1 (c-keys) (l. 110-112). «(a) [real runs, no ISO needed] If [a, b] ⊆ [1, T] and b_0(s_t) is the
      same for all t ∈ [a, b], every level-1 mover moves at most once in [a, b].» (l. 113-114); (b) [forced runs, ISO] the same for u_t
      with c_t constant (l. 115-116); (c) the corollary for the four movers of levels 0 and 1 over a whole run with b_0 constant (l.
      117-118; not in the line). F-a (fixes l. 9-19): for any G ∈ 𝓛^R_d, ISO or not, the c_t-step sequence u_t := Step^(c_t)_G(u_(t−1))
      from any u_0 (0 and 1 kept at u_0's options); «NOW-ONCE (b′) [G ∈ 𝓛^R_d, no ISO]. If c_t is the same for all t ∈ [a, b] ⊆ [1, L],
      every level-1 mover x has u_t(x) ≠ u_(t−1)(x) for at most one t ∈ [a, b].» (l. 12-13). Proofs: by (F2) a moving degree-2 mover
      takes its key-least option, which depends only on b_0 (resp. c), so two consecutive moves in the interval would take the same
      option, against the move between them; (b′) uses no Ξ-value and no ISO (fixes l. 19). Cells: REFEREE l. 13 «SIGN (note FL-N1: (b)
      does not need ISO)», §C l. 166 «F-a, NOW-ONCE (b′) without ISO (new signed content): SIGN.»; REFEREE-2 l. 15 «**SIGN** (Opus 5.5,
      D12)», L2 file l. 9 «F-a, NOW-ONCE (b′) without ISO (new signed content): SIGN (Opus 5.5, D12).».
  (d) Lemma SWAP (§4 l. 128-136): G^swap is G with the W-targets of the two options of every level-1 mover exchanged; it is IDEAL-ACYC,
      in 𝓦_d and R109's 𝓛_d, not in 𝓛^R_d (l. 128-130); «Lemma SWAP. For every state s and c ∈ {0, 1}: Step^(1−c)_G(s) =
      Step^c_(G^swap)(s).» (l. 131). Proof (l. 132-136): equal Ξ-data, so equal A-sets; at level 1, κ^c_(1−k) = κ^(1−c)_k, so the key^c
      of an option in G^swap is its key^(1−c) in G; above level 1 the W-targets agree, and the keys follow by induction. Cells: REFEREE
      l. 14 «SIGN»; REFEREE-2 l. 16 «**SIGN** (Opus 5.5, D12)».
  (e) Corollary SWAP-RUN, in the form of fixes F-b (fixes l. 21-36; it replaces the reading of packet l. 137-146 and drops the caveat of
      l. 145-146): «Let G ∈ 𝓛^R_d with ISO, u_0, …, u_L a forced run with flips ≤ k, and q ANY options of 0 and 1; put v := b_0(q)»; cut
      [1, L] into the maximal blocks of constant c (at most k + 1); each block [a, b] with c = v is a prefix of the run of H_q from
      u_(a−1) with q at 0 and 1, each block with c = 1 − v a prefix of the run of (G^swap)_q from that state, each followed by idle
      frames; «So a forced run with k flips is a concatenation of at most k + 1 runs of the two fixed IDEAL genomes H_q and (G^swap)_q,
      each started where the previous piece was cut; moves = the sum of the pieces' lengths.» (l. 26-27). Proof (l. 28-33): W-ONLY (b)
      and (c) for G with c = v; for c = 1 − v, SWAP gives Step^(1−v)_G = Step^v_(G^swap), and G^swap is ISO with the same level-0 gates,
      so W-ONLY (c) applies to it with the same v; an idle step stays idle. Cells: REFEREE l. 15 «SIGN (note FL-N2: the «no such q»
      caveat is removable)», §C l. 173 «F-b, SWAP-RUN for ANY q (exchange argument): SIGN.»; REFEREE-2 l. 16 «(N-1: the «no q» caveat is
      unnecessary)», L2 file l. 15 «F-b, SWAP-RUN with ANY q: SIGN (Opus 5.5, D12). It is my N-1 written out.».
  (f) Proposition FLIP-1 (§5 l. 149-176): T_0(1) = 2 and T_k(1) = 3 for every k ≥ 1, on the ISO genomes of 𝓛^R_2. Upper bounds (l.
      150-163): of the two level-1 movers, one (v) has both options with Ξ-target X (ISO and acyclicity), so it changes at most once (to
      its better option); the other (u) has exactly one better option, determined by v's option, so two consecutive changes of u need a
      change of v between them, and u changes at most twice: moves ≤ 3 for any bits; with no flip NOW-ONCE (b) gives ≤ 2. Lower bounds,
      two explicit instances (l. 164-175; option fields W-target, Ξ-target, gate, β rank, β parity; X the exit): I-0,
      experiments/new/box162/out/kf0_d2_t2.json (sha1 c2233e05b6212233acf5e3121b0ed088b7863b3c, l-new e93b0e82): «mover 0: (−, X, 0, 7,
      odd), (−, X, 2, 6, odd); mover 1: (−, X, 3, 5, odd), (−, X, 1, 4, odd); mover 2: (0, X, 2005, 2, odd), (1, 3, 2006, 0, odd); mover
      3: (0, X, 2004, 3, odd), (1, X, 2007, 1, odd)», start (0, 0) on (2, 3), c ≡ 0: moves 2, flips 0. I-1,
      experiments/new/box162/out/kf1_d2_t3.json (sha1 d368d441b13b512c3453ea168d187734fe92b45e, e93b0e82): «mover 0: (−, X, 1, 7, even),
      (−, X, 3, 6, even); mover 1: (−, X, 2, 5, even), (−, X, 0, 4, even); mover 2: (0, X, 2004, 3, even), (1, X, 2007, 0, odd); mover
      3: (0, 2, 2005, 2, odd), (1, X, 2006, 1, odd)», start (1, 0) on (2, 3), c = (0, 1, 1): moves 3, flips 1. Cells: REFEREE l. 16
      «SIGN»; REFEREE-2 l. 17 «**SIGN** (Opus 5.5, D12)».
  (g) CONDITIONAL DEAD of the lane conjecture SC-ISO (§6 l. 178-195): «for every d ≥ 3, in every run of every ISO genome of 𝓛^R_d, seg1
      + tail ≤ T^R(d − 1)» (l. 180), seg1 the number of steps before the first step that moves mover 0 or 1 (T if none), tail the number
      after the last such step (0 if none) (l. 69-70). Instance experiments/new/box160/out/iso_d4_st9.json (sha1
      7ca1e68c52e4bb02ee260ccc36e8323146cdc6b3, l-new 279dd656), a genome of 𝓛^R_4 with ISO, option fields W-target, Ξ-target, gate, β
      rank, β parity (l. 181-187): «mover 0: (−, 3, 0, 8, odd), (−, X, 2, 11, even); mover 1: (−, 3, 1, 9, odd), (−, X, 3, 4, odd);»
      «mover 2: (0, 5, 2005, 10, even), (1, X, 2006, 14, odd); mover 3: (0, 6, 2004, 5, odd), (1, 2, 2007, 12, even);» «mover 4: (2, 2,
      2008, 13, even), (3, 5, 2011, 0, odd); mover 5: (2, X, 2009, 15, odd), (3, X, 2010, 7, even);» «mover 6: (4, 7, 2012, 3, even),
      (5, 2, 2015, 1, even); mover 7: (4, 4, 2013, 2, even), (5, 5, 2014, 6, even);» «start 11111011 (movers 0..7). The Ξ-graph is
      acyclic (topological order 1, 0, 3, 6, 7, 4, 2, 5); no Ξ-target is 0 or 1 (ISO).». Its run (l. 188-190): «11111011, 11110011,
      11110010, 11110000, 11100100, 11001101, 11001111, 10011111, 00010111, 00010110, 00010100, 00000100. T = 11; mover 1 moves at step
      7, mover 0 at step 8, no other step moves 0 or 1. So seg1 = 6, tail = 3, seg1 + tail = 9.». SIGNED UNCONDITIONALLY: the instance
      computation and the implication «SC-ISO at d = 4 ⇒ T^R(3) ≥ 9» (REFEREE l. 76 «So «SC-ISO at d = 4 ⇒ T^R(3) ≥ 9» is PROVED (by the
      instance alone). That part I SIGN.»; REFEREE-2 l. 80-81 «What I sign: (i) the instance computation (seg1 + tail = 9 on an ISO
      genome of 𝓛^R_4); (ii) the implication «SC-ISO (at d = 4) ⇒ T^R(3) ≥ 9»; (iii) «SC-ISO is false IF T^R(3) ≤ 8».»). CONDITIONAL:
      «SC-ISO is false» holds under the machine premise T^R(3) ≤ 8 (packet l. 191-193: «CaDiCaL UNSAT of «some genome of 𝓛^R_3 and start
      with T ≥ 9»», L-RED's xcnf.py encoding, «not Lean, not refereed»), which is NOT a result of this entry or of RESULTS. Cells:
      REFEREE l. 17 «SIGN AS CONDITIONAL, gap FL-G1 (machine premise T^R(3) ≤ 8). The unconditional part, «SC-ISO at d = 4 ⇒ T^R(3) ≥
      9», is SIGNED»; REFEREE-2 l. 18 «**SIGN WITH GAP G-FLIP-1** (Opus 5.5, D12): ruling below», l. 85 «RESULTS must keep that wording.
      The item must not be cited as an unconditional DEAD.». «Does NOT claim: anything about the NOW channel at d = 4 (UNKNOWN; box 160
      §0); anything about SLOT-TRADE or FLIP-ADD (both OPEN); that seg1 + tail can exceed T^R(d − 1) by more than 1.» (l. 194-195).
  The RESULTS line (L-3) states (a)-(g) with their exact hypotheses, and nothing wider.
- Premise: RESULTS R104's definition of the IDEAL model and of the Ξ-graph (no R104 theorem), restated in packet §0; and RESULTS R109's
  SEG-ONCE, at l = −1 only, quoted verbatim by the packet (l. 21-24) from R109's title, where the quote occurs once, byte for byte. L-3:
  «premise: R104's definition of the model only, no theorem of R104 used; and RESULTS R109's SEG-ONCE at l = −1 only». Use: with l = −1
  the interval may be the whole run, and every mover of 𝓛^R_d has degree 2, so each level-0 mover moves at most once in a run; this
  gives W-ONLY (d)'s «flips ≤ 2» (l. 104-105) and NOW-ONCE (c) (l. 118). R109's 𝓛_d and T*(d) are named in the line only to keep them
  apart (packet l. 25-26; REFEREE l. 26 «T* is named but never used.»; REFEREE-2 l. 27). Not used: RESULTS R105 (so RESULTS Erratum E-2
  to R105 does not bear on this entry), R106, R107, R108, docs/lit (packet l. 27-28; REFEREE l. 26; REFEREE-2 l. 28 «Confirmed by
  reading every proof step.»). The DEAD's machine premise T^R(3) ≤ 8 is its listed gap, not a premise of a signed statement. The
  instances are data files, recomputed by both referees with their own simulators (REFEREE «β-set simulator written from R104's text»,
  l. 89; REFEREE-2 l. 74-76, «= packet §6 exactly»).
- L41, L42 and L43. The proofs are L-NEW successor 53's (packet l. 5), including F-a and F-b, which the lane wrote out after the
  referees' findings: F-a is REFEREE's note FL-N1 (the proof of (b) uses no ISO), F-b the exchange argument both referees found
  independently (REFEREE FL-N2, REFEREE-2 N-1); both signed the written forms. Nothing referee-written is a proof step of the entry (my
  reading; neither referee mentions L41). The DEAD (g) refutes an explicit bound by one instance only under a machine premise, so it is
  labelled CONDITIONAL, as REFEREE ruled under its reading of L42 (an uncovered premise stated as an explicit hypothesis, labelled
  CONDITIONAL) and L43 (an instance must exceed an EXPLICIT ESTABLISHED bound), and as REFEREE-2 signed it «WITH GAP»; the line keeps
  the instance's unconditional content («without it the instance shows that SC-ISO at d = 4 forces T^R(3) ≥ 9»).
- Fixes (docs/new/P-IDEAL-FLIP-fixes.md, L-NEW successor 53, append-only; entry 1 at 4c2e5124, 57 lines, sha1
  f8d3677e4754fde9922208782483f9d4bff168ac; entry 2 at 47b4e165, 81 lines, sha1 4220c44e6caa0bc6e2b2d4363ba3f5ec97505de6, l. 1-57
  unchanged). Entry 1 (l. 4-57), after REFEREE eaa941b9 and REFEREE-2 dc622d03:
  - F-a (l. 8-19): «### F-a (REFEREE FL-L1): NOW-ONCE (b) without ISO. CHOICE: extend (b); L-2 keeps L-1's unconditional wording for
    c_t-step sequences.»; the c_t-step sequence for any G ∈ 𝓛^R_d, NOW-ONCE (b′) and its proof (Claims (c)). REFEREE §C (74fae0fa, l.
    166-172): «No Ξ-value and no ISO is used. Correct; it closes FL-L1 by extension.»; REFEREE-2 (8b53a9e2, l. 9-14), with its own DATA:
    «1,500 random 𝓛^R_d genomes (d 2-4; 1,300 non-ISO), random bit sequences, 163 consecutive-change pairs, 0 violations.».
  - F-b (l. 21-36): «### F-b (REFEREE FL-L2 = REFEREE-2 N-1): SWAP-RUN without the «some q with b_0(q) = c_1» caveat (exchange
    argument)»; the statement for any q and its proof (Claims (e)); «The packet's caveat («If no q with b_0(q) = c* exists …») is no
    longer needed: q is arbitrary, and the bit c* = c_1 plays no role.» (l. 34). REFEREE §C l. 179 «It is the same argument as my FL-N2,
    in a cleaner form (no c* needed).»; REFEREE-2 L2 file l. 15-17 «It is my N-1 written out.», «The caveat is correctly dropped.».
  - F-c (l. 38-47): «### F-c (REFEREE-2 F-1): SWAP-RUN's «Does NOT claim» remark corrected»: H_q and (G^swap)_q have degree-1 level-0
    movers, so they are not in R109's 𝓛_d; by R109's SHIFT their shifted forms lie in 𝓛_(d−1), so each piece has at most T*(d − 1)
    moves; «Corrected remark (not a signed statement; no bound is claimed)» (l. 42); «This uses R109 SHIFT and nothing else; the
    packet's premise list is not changed for any signed statement (the remark is outside the signed text).» (l. 46-47). REFEREE §C l.
    181 «F-c (REFEREE-2 F-1, unsigned remark): CORRECT.»; REFEREE-2 L2 file l. 18 «F-c (my F-1): CORRECT.». Not part of this entry.
  - Line L-2 (l. 49-57): three hunks: «(1) REQUIRED (REFEREE FL-L3): [-DEAD:-]{+CONDITIONAL DEAD (premise T^R(3) ≤ 8, machine):+}.» (l.
    50); the F-a choice, no hunk (l. 52-53); REFEREE-2's optional P-3 (the frozen form «from any state with q at 0 and 1») and P-1
    («every start)», since every checked genome has d ≤ 4) (l. 54-56); «Nothing else changed.» (l. 57). REFEREE §C l. 186 «L-2: my own
    word diff (git diff --word-diff) finds exactly 3 hunks, equal to entry 1's list.»; REFEREE-2 L2 file l. 23 «Token diff: exactly the
    3 hunks of entry 1.».
  - Entry 2 (l. 59-81), after CHECKER C122 (80ed31a6): «Makes line L-3 (docs/new/P-IDEAL-FLIP-line-L3.txt) = L-2 (8099415b) with exactly
    the four replacements R1-R4 of CHECKER C122 §5» (l. 60); «DATA scope and source-note wording only: no statement, definition or
    premise changes.» (l. 62); the word diff L-2 → L-3 (l. 64-75) and R1-R4 with their E-items (l. 76-80); «Applied; nothing else
    changed.» (l. 81). REFEREE-2 Addendum 1 (8fde383f, l. 36-37): each old string once in L-2, each new string once in L-3, «L-2 with
    R1, R2, R3, R4 applied equals L-3 exactly».
  No fix weakens a signed statement; F-a and F-b extend (c) and (e); entry 2 changes DATA scope and the source note only.
- Not signed: packet §7 (DATA, machine checks, EXCLUDED, TARGET diff, READING; «DATA / READING (not to sign)», l. 17), in particular the
  T_k(m) table (m = 1, 2, 3; l. 198-211: «Each count covers ONLY the statement «T_k(m) ≥ t» (SAT) or «T_k(m) ≤ t − 1» (UNSAT at t) on
  𝓛^R_(m+1) with ISO»), the T^R values (l. 216-217), the encoding READING (l. 212-215) and the READING «W-ONLY + SWAP turn the W-channel
  part of SLOT-TRADE into a question about TWO fixed genomes alternating at most three times (k = 2)» (l. 233-234); fixes F-c (a
  remark). The machine premise T^R(3) ≤ 8 is not signed by either referee as a result (REFEREE l. 101 «Not checked by me: T^R(3) ≤ 8.»).
  OPEN, not claimed: CONJECTURE FLIP-ADD (T_2(m) ≤ T^R(m) + O(m), l. 227); CONJECTURE SLOT-TRADE (RESULTS R109); any bound on T_k(m) for
  m ≥ 2; T^R(d) for d ≥ 3 as a result; whether T^R(d) = T*(d) (l. 58); the NOW channel; Ξ-cyclic genomes; genomes outside 𝓦_d;
  G-N5-TIME.
- Referee strengthening (NOT part of this entry; referee remarks and own checks):
  (i) REFEREE-2 l. 43: W-ONLY (c) «holds without ISO too, since states of H_q carry q at 0, 1; not needed.».
  (ii) REFEREE l. 98-99 and REFEREE-2 l. 105-106: FLIP-1's bounds are reached on random ISO genomes of 𝓛^R_2 (6,400 and 3,200 (genome,
       start) pairs; maxima 2 at k = 0 and 3 at k ≥ 1).
  (iii) REFEREE-2 l. 100-104: its genome sets are random genomes of 𝓦_d (d ≤ 5; level-0 movers of degree 1-3, widths 1-3 above, degrees
        1-3, half ISO), random 𝓛^R_d genomes (3/4 ISO) and the 50 corpus genomes; W-ONLY (a) on 23,160 real steps «(incl. non-𝓛^R 𝓦_d
        genomes with degree-1 and degree-3 movers, which the lane DATA does not cover)»; SWAP on 72,128 (state, c) pairs; NOW-ONCE (b)
        on 5,935 pairs.
  (iv) REFEREE-2 L2 file l. 13-14: NOW-ONCE (b′) on 1,500 random 𝓛^R_d genomes, 1,300 of them non-ISO.
  (v) REFEREE-2 l. 89-93 (DATA, not a proof): with L-RED's encoding re-run (not independent), and by hill-climbs on 𝓛^R_3 with its own
      simulator, no T ≥ 9 was found (T 8 reached from the T = 8 witness, never 9).
- Honest limits: (i) A REDUCTION inside the IDEAL model: W-ONLY (d) bounds T on the ISO genomes of 𝓛^R_d by T_2(d − 1) + 2, a quantity
  of the external-flip model, and SWAP-RUN writes a forced run with k flips as at most k + 1 pieces of runs of two fixed IDEAL genomes
  (that the two together turn the W-channel part of SLOT-TRADE into a question about two genomes alternating at most three times is the
  packet's READING, l. 233-234, not signed); it bounds nothing polynomially (T_2 is not bounded here); G-N5-TIME stays open; not M3, not
  a step-4 pass, not a TARGET.md claim. (ii) W-ONLY (a) holds on all of 𝓦_d; W-ONLY (b)-(d), SWAP-RUN and FLIP-1 are stated under ISO;
  NOW-ONCE and SWAP are about 𝓛^R_d, the R197-convention ladders only (not R109's 𝓛_d: G^swap is in 𝓛_d and not in 𝓛^R_d); Ξ-cyclic
  genomes are not covered. (iii) The DEAD (g) is CONDITIONAL: SC-ISO is false only together with the machine premise T^R(3) ≤ 8, a
  CaDiCaL UNSAT on L-RED's encoding, not Lean and not landed; unconditionally, the instance shows that SC-ISO at d = 4 forces T^R(3) ≥
  9. REFEREE-2's audit of an independent encoding of the same premise by L-COMP (claude/l-comp 6f19564f; R2-T3R-audit.md, d1c4a530,
  2026-11-05 12:49Z) is one referee's audit; it is not a signature of this entry, and the label changes only through a separately landed
  item. Only the W-channel ISO form of the lane's single-channel trade is touched; the NOW channel is not claimed. (iv) FLIP-1 is exact
  at m = 1 only; for m ≥ 2 the T_k(m) values are lane DATA (packet §7), not signed. (v) The DATA is per statement, as the line's DATA
  parenthesis says, with these exact sets: flipcheck.py runs 300 random genomes of 𝓛^R_d (100 each at d = 2, 3, 4; 225 drawn with ISO,
  75 drawn without it, of which 65 are not ISO) and the 50 𝓛^R genomes in box160/out and box162/out (36 ISO), every start (all have d ≤
  4); W-ONLY step form and NOW-ONCE (real runs) on all of them; the ISO independence, frozen form (one start per (genome, q)), the bound
  T ≤ T_2(d − 1) + 2, SWAP and FLIP-1 checks on the 261 ISO genomes only (FLIP-1 on the 82 with d = 2); SWAP's 15,660 (state, c) pairs
  are of ISO genomes only, though Lemma SWAP needs no ISO; SWAP-RUN, NOW-ONCE (b′) and the T_k(m) values for m ≥ 2 have no lane DATA
  (the referees' own checks, Data). (vi) Every statement is about R104's IDEAL model on acyclic Ξ-graphs, or the c-step defined from it;
  nothing is said about a real N5 run or a parity game beyond what R104 already says (packet l. 230-232). (vii) Premises: RESULTS R104's
  definition and RESULTS R109's SEG-ONCE at l = −1 only; no R105 item, so RESULTS Erratum E-2 does not bear; RESULTS R108 is not used.
  No lit note, no lane file, no outside source. No Lean. (viii) Two of the line's clauses (NOW-ONCE for c_t-step sequences without ISO,
  SWAP's concatenation for any q) are proved in docs/new/P-IDEAL-FLIP-fixes.md (F-a, F-b), which the line's source note names
  («docs/new/P-IDEAL-FLIP.md with its fixes entry 1, docs/new/P-IDEAL-FLIP-fixes.md»). (ix) Names: «FLIP-1» here is the one-level value
  of T_k, not part (b) of R69's Lemma FLIP; the gap «G-FLIP-1» cited here is REFEREE-2 successor 27's gap on P-IDEAL-FLIP, not the joint
  gap G-FLIP-1 of R69; b_0 here is the key bit of the two level-0 movers, not R106's start b_0 of L_K; κ^c is bound in the line, not
  N5's κ. (x) The DEAD instance iso_d4_st9 is the lane's own (box 160), used here only as a counterexample under the premise; its T is
  R104's number of steps.
- Data (DATA, not proof): experiments/new/box162/flipcheck.py (l-new e93b0e82, sha1 9fd0b1926b78eeec0f5d83f8cac42f4a6fbe6965, 156 lines;
  the c-step, the forced run and the exact per-start maximum V_k by memoised search, on the box 150 simulator
  experiments/new/box150/check.py, l-new 0ebddcf5, sha1 019de0f7b36dcbd47743b3d27b4a1a93549d574b, 214 lines), wired into
  experiments/new/check.sh block «P-IDEAL-FLIP» (l. 903-910 at 4c2e5124, with sha1 pins of the packet, L-1, the three instances, the
  fixes and L-2; at 47b4e165 the pins also hold L-3 4089bd73 and the fixes file at entry 2, 4220c44e, l. 905-907 changed); unchanged at
  4c2e5124 and 47b4e165. L-3's DATA parenthesis: «(DATA: W-ONLY, step form: experiments/new/box162/flipcheck.py, 0 violations on 44,084
  real steps (300 random 𝓛^R genomes with d = 2, 3, 4, 225 of them drawn ISO and 75 drawn without that restriction, 65 of these not ISO,
  and the 50 𝓛^R genomes in box160/out and box162/out, 36 of them ISO, every start); W-ONLY, ISO independence: the same tool, 0
  violations on 31,320 (state, q) pairs of the 261 ISO genomes among them (the 225 drawn ISO and the 36 ISO corpus genomes); W-ONLY,
  frozen form: 0 violations on 1,044 (ISO genome, q) pairs; T ≤ T_2(d − 1) + 2: 0 violations on 28,896 ISO runs (b_0 changing at most
  twice and the steps moving levels ≥ 1 at most the exact per-genome maximum with two changes); NOW-ONCE, real runs: 0 violations on 307
  pairs of consecutive moves of a level-1 mover; SWAP: 0 violations on 15,660 (state, c) pairs of the same 261 ISO genomes (no non-ISO
  genome tested); FLIP-1 upper bounds: 0 violations on 1,312 (2-level ISO genome, start) pairs, k = 0, …, 6; SC-ISO: the instance
  replayed by the same tool and by the box 150 checker; NOW-ONCE for c_t-step sequences, the concatenation clause of SWAP and the T_k(m)
  values for m ≥ 2: no signed DATA (the packet's §7 table is DATA only))». Genome sets: the 300 random genomes are drawn with seed 162,
  100 each at d = 2, 3, 4, genome i without the ISO constraint iff i % 4 = 3 (75 genomes; 65 of them are not ISO, 10 are ISO by chance);
  the corpus is every 𝓛^R genome in box160/out and box162/out (50: 8, 29 and 13 at d = 2, 3, 4; 36 ISO); every start of each (38,912
  runs, 44,084 real steps). The ISO-only checks use the 225 random genomes drawn ISO and the 36 ISO corpus genomes (261): ISOA 30 random
  states × 4 level-0 configurations each, FROZ the stored start with each of the 4 configurations, CONS every start (28,896 runs), SWAP
  30 random states × 2 bits each, FLIP1 every start of the 82 with d = 2, k = 0, …, 6. Controls: «SWAPNEG 12594» (G^swap at the same c
  differs) and «NOWCTRL 307» (all consecutive move pairs; none lies in an interval of constant b_0).
  The block's outputs, reproduced by both referees at 9effea1f and re-run for this draft (2026-11-05T14:12:13Z-14:13:02Z from a `git
  archive` of 4c2e5124's experiments/new and docs/new, rc 0, PASS; again at the second fill, 2026-11-05T17:47:06Z-17:47:27Z from a `git
  archive` of 47b4e165's, rc 0, PASS line ending «fixes 4220c44e, line L-2 8099415b, line L-3 4089bd73: PASS», flipcheck raw output
  byte-equal to the first run's): «RANDOM seed 162 genomes 300 + corpus 50 runs 38912 steps 44084 states 7830 WONLY 0 ISOA 0 FROZ 0 CONS
  0 SWAP 0 SWAPNEG 12594 NOWONCE 0 NOWCTRL 307 FLIP1 0»; «CHECKED WONLY 44084 ISOA 31320 FROZ 1044 CONS 28896 SWAP 15660 NOWONCE 307
  FLIP1 1312»; «INST iso_d4_st9 LR True ISO True d 4 T 11 level-0 steps [7, 8] seg1 6 tail 3»; «WIT kf0_d2_t2.json LR True ISO True V_0
  2»; «WIT kf1_d2_t3.json LR True ISO True V_1 3»; on the instance «TOTAL genomes 1 runs 1 steps 11 XSIM 0 TOPO 0 MONO 0 XINEW 0 RISE 0
  CHAIN 0 KEYFLIP 0 DECR 0 TOPMONO 0 RBOUND 0 RESTR 0 ICHARGE 0 REC 0 VIOL 0 (info REC148 0)». REFEREE §4 l. 103-111 («All match
  check.sh's patterns.», «pin162: all five sha1s EQUAL.»); REFEREE-2 l. 96-98 («PASS, exit 0.»).
  REFEREE (successor 23; own docs/referee/scratch/flip_probe.py, sha1 b1acee9b55c824fdb86db08724c5ec4d81765ac3, «β-set simulator written
  from R104's text; c-step and forced runs from §1's text»; log xinew_logs/flip_probe.txt): the instance's twelve states equal §6's list
  (l. 91-93); I-0 and I-1 replayed, V_0 = V_1 = V_6 = 2 for I-0 and V_0 = 1, V_1 = V_6 = 3 for I-1 (l. 94-97); «400 random ISO genomes
  of 𝓛^R_2 × 16 starts = 6,400 pairs. max V_0 = 2, max V_6 = 3:» 0 violations (l. 98-99); «W-ONLY (a) on 367 real steps of 400 random
  𝓛^R_3 genomes (ISO not required): 0 violations.» (l. 100).
  REFEREE-2 (successor 27; own docs/referee-2/R2-P-IDEAL-FLIP/flip_check.py, sha1 ae91714fe49908c635bbccffcd55df878358e865, «my
  simulator; c-step, forced run, H_q, G^swap, exact FLIP-1 search all my own», no committed log): W-ONLY (a) on 23,160 real steps, (d)
  on 9,380 ISO 𝓛^R runs, (b) 40,632 state pairs, (c) 40,480 frozen runs, SWAP 72,128 (state, c) pairs, NOW-ONCE (a) 307 move pairs and
  (b) 5,935 pairs, «19,312 runs in all. 0 violations.» (l. 102-104); FLIP-1 exact on 3,200 pairs (l. 105-106); controls FNEG and SWAP at
  the same c (l. 107); the instance recomputed (l. 74-76); and (L2 file l. 13-14) NOW-ONCE (b′) on 1,500 genomes, 1,300 non-ISO.
  No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-P-IDEAL-FLIP.md: successor 23's report eaa941b96cfa89bceca7f97968ad9c07e6573f0a
  (2026-11-05T11:14:44Z, new file, 159 lines, sha1 40a4a1ba8ad3d59c5a2f392e3425240290fff217, with scratch/flip_probe.py and
  xinew_logs/flip_probe.txt): W-ONLY, NOW-ONCE, SWAP, SWAP-RUN, FLIP-1 SIGN, the DEAD SIGN AS CONDITIONAL (l. 12-17, 153-154); §C
  74fae0fa4305b46677d9751d84b4dd83596d4e69 (12:55:02Z, 198 lines, sha1 333749f26b47f580c3c74f67dc7cee335e84933a): F-a and F-b SIGN (l.
  166, 173), «VERDICT: line L-2 MATCHES.» (l. 192), «Signed: W-ONLY, NOW-ONCE (incl. (b′)), SWAP, SWAP-RUN (F-b form) and FLIP-1.» (l.
  193). L-3: successor 24's §C add. 1 5c02d44d775d67d8812087b762398a7562da0134 (2026-11-05T17:26:52Z, file sha1 675727cdc73fba7a1b1c8fc3c302fde2a7b51056): «- Verdict: L-3 MATCHES (L-2 + C122 §5 R1-R4, nothing else).» (l. 211).
  REFEREE-2 (successor 27): docs/referee-2/R2-P-IDEAL-FLIP.md dc622d031fbcf487ca000cbf4cde9b0b0153527b (2026-11-05T11:17:53Z, new file,
  136 lines, sha1 f7e1a3bd259f17b0c2049af4cdb4a3dc7dabfe99; with R2-P-IDEAL-FLIP/flip_check.py): every statement SIGN, the DEAD «SIGN
  WITH GAP G-FLIP-1», L-1 MATCHES (l. 10-19, 134-136); docs/referee-2/R2-P-IDEAL-FLIP-L2.md 8b53a9e2653ff89a20763ac7f33e18a00feab6b3
  (12:54:46Z, new file, 30 lines, sha1 96faae6e865c9f116907417e1c8d8d521e0766d8): F-a and F-b SIGN (l. 9, 15), «## Line L-1 → L-2:
  MATCHES» (l. 22), after the byte test of l. 23-26; Addendum 1 to the same file, 8fde383fb248bd8a8216c039e002350d4002387f (17:06:22Z,
  42 lines, sha1 7137cb341c136925f5db0ff8fd571834f6064b9b; l. 1-30 = 8b53a9e2's, by cmp): the byte test of L-3 against C122 §5 (l.
  36-37), «- Verdict: L-3 MATCHES.» (l. 42). Lane: freeze and L-1 9effea1fff84fae8170b181e858fd88363d717fa, fixes entry 1 and L-2
  4c2e512421db51180279a63475e98d1081414e8d, fixes entry 2 and L-3 47b4e16514ad10548b2724b780fee01202cc77d2.
  INDEPENDENCE: REFEREE l. 2 «Independent: I did not read docs/referee-2/.»; REFEREE-2 l. 2-3 «Independent: docs/referee/ not read for
  this packet before this push.». REFEREE's report (11:14:44Z) precedes REFEREE-2's (11:17:53Z) by 3 min; neither cites the other's
  first report; each recomputed the instance with its own simulator written from R104's text and replayed both FLIP-1 instances.
  Differences, resolved: on L-1 REFEREE required three line changes (FL-L1 to FL-L3), REFEREE-2 MATCHED with optional items; both found
  the SWAP-RUN caveat removable (FL-N2 = N-1); REFEREE-2 alone found the wrong T* remark (F-1, now F-c, unsigned); both treat the DEAD
  as conditional on the same machine premise. Both SIGN the same statements and both MATCH L-2; REFEREE-2 MATCHES L-3. No disagreement
  in substance.
- TARGET.md diff: TARGET.md §1-§3 define parity games («A parity game is G = (V, V_E, V_O, E, pr) with V finite»), the regions W_E, W_O,
  M4 (§2 «There is a deterministic algorithm A and a polynomial p such that for every parity game G, A on input G halts within») and the
  word-RAM cost model; no statement of this entry mentions a parity game, a winning region, an algorithm's running time or a cost model
  (packet §7 l. 230-232 «Diff against TARGET.md: no statement mentions a parity game, a winning region, an algorithm's running time or a
  complexity class.» «None is an M4 or M3 claim, none bounds anything polynomially, none is a gauntlet step. G-N5-TIME stays OPEN.»;
  REFEREE §5 l. 116 «Agreed with §7: not M4, not M3, not a gauntlet step. G-N5-TIME OPEN.»; REFEREE-2 l. 114-115 «No M4 / M3 claim, no
  gauntlet step. FLIP-ADD, SLOT-TRADE, G-N5-TIME OPEN. The packet's §7 diff is correct.»). The line (L-3) makes no M4 claim and no
  TARGET claim; its tail reads «a REDUCTION of the W-channel part of SLOT-TRADE to an external-flip model inside the IDEAL model» and
  «G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim» (L-3, by script). Not a step-4 pass. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER R109's UPDATE of G-N5-TIME (GAPS at 67ec1151, last changed by 67ec1151: the last
UPDATE on l. 11 is R109's, «UPDATE 2026-11-04 23:38Z: RESULTS R109 (P-IDEAL-SLOT; CHECKER C121 9f9c60c0) …», before the row's closing «
|»), built by script (upd110b.py: upd110.py's 13 controls and procedure, unchanged, run on L-3: upd100L3.py's build() unchanged for the
label move, on the claim body with a sentinel tail as for R102 and R105-R109; the tail rule of (9) with R107's step for the unlabelled
CONDITIONAL DEAD clause; L-3's DATA parenthesis is closed (C122 R4), so the first fill's adaptation for an unclosed one is not used;
cross-checked against a direct opening of the DATA parenthesis and against C122 §4's expected line, the first fill's UPDATE with R1-R4,
R4 without its added «)»: both True; to check (9)) only from the clauses of the title line L-3: labels behind their clauses; the
CONDITIONAL DEAD clause verbatim after (FLIP-1); « (2026-11-05) — » → «: »; the DATA parenthesis before the source parenthesis opened as
«; DATA: …»; «G-N5-TIME stays OPEN» and «not M3, not a step-4 pass, not a TARGET.md claim» dropped; the source parenthesis kept; «.
G-N5-TIME stays open.» at the end. The same script reproduces R97's to R109's LANDED UPDATEs (GAPS l. 11) byte for byte. L-3 holds no
"|"; the UPDATE holds none (4,748 bytes, 52 «(» / 52 «)»; sha1 of the line without newline, placeholders unfilled:
d76a5cfb4b09dcf1d24dfc7acad17c6ac1db185c, = C122 §4). <DATE> is the landing date (YYYY-MM-DD, by date -u at the landing commit; C114
Add. 1 E-1), <HH:MM> the landing time and <checker> the CHECKER C122 commit, all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R110 (P-IDEAL-FLIP; CHECKER C122 <checker>) [refereed-only] LANDED: In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of R104 used; and RESULTS R109's SEG-ONCE at l = −1 only), on acyclic Ξ-graphs, with 𝓦_d the genomes with levels 0, …, d − 1 whose level-0 movers are exactly two movers named 0 and 1, 𝓛^R_d ⊆ 𝓦_d the 2-wide degree-2 ladders in L-RED's R197 convention (movers 2l and 2l + 1 on level l, all of degree 2, no other movers, option k of a mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k), T^R(d) the largest number of steps over 𝓛^R_d and all starts (kept apart from R109's T*(d) over 𝓛_d; T^R(d) ≤ T*(d)), ISO the property that no option has Ξ-target 0 or 1, b_0(s) = 1 iff g(0, s(0)) < g(1, s(1)), for c ∈ {0, 1} the c-step the step rule on the movers of level ≥ 1 (A-sets under the old state, keys under the new state, movers 0 and 1 kept) with every level-1 option W-pointing to mover w keyed by (κ^c_w, its own gate), κ^c_0 = 1 − c, κ^c_1 = c, and T_k(m) the supremum, over the ISO genomes of 𝓛^R_(m+1), their starts u_0 and the bit sequences c_1, …, c_L with at most k changes, of the number of t with u_t ≠ u_(t−1) on the levels ≥ 1, where u_t is the c_t-step of u_(t−1): on 𝓦_d every step of a run equals, on the levels ≥ 1, the c-step with c = b_0 of the new state; under ISO the A-sets of the levels ≥ 1 do not depend on the options of 0 and 1, and freezing 0 and 1 at options q gives an IDEAL genome whose run from any state with q at 0 and 1 is the iterated b_0(q)-step; hence every run of an ISO genome of 𝓛^R_d (d ≥ 2) has T ≤ T_2(d − 1) + 2 (W-ONLY); on 𝓛^R_d, on an interval of steps over which b_0 of the states is constant, and in a c_t-step sequence on an interval over which c_t is constant, every level-1 mover moves at most once (NOW-ONCE); on 𝓛^R_d, the (1 − c)-step of G equals the c-step of G^swap, the genome G with the W-targets of the two options of every level-1 mover exchanged (in R109's 𝓛_d, not in 𝓛^R_d), so under ISO a c_t-step sequence with k changes is a concatenation of at most k + 1 runs of two fixed IDEAL genomes (SWAP); T_0(1) = 2 and T_k(1) = 3 for every k ≥ 1 (upper bounds by proof; lower bounds by two explicit instances, experiments/new/box162/out/kf0_d2_t2.json, sha1 c2233e05…, and kf1_d2_t3.json, sha1 d368d441…) (FLIP-1); and CONDITIONAL DEAD (premise T^R(3) ≤ 8, machine): the lane conjecture SC-ISO («for every d ≥ 3, in every run of every ISO genome of 𝓛^R_d, the number of steps before the first step that moves 0 or 1 plus the number of steps after the last such step is at most T^R(d − 1)») is false, by the ISO genome iso_d4_st9 of 𝓛^R_4 (experiments/new/box160/out/iso_d4_st9.json, sha1 7ca1e68c…; T 11 from its stored start, mover 1 moving at step 7 and mover 0 at step 8, 6 + 3 = 9 steps outside) together with the machine premise T^R(3) ≤ 8 (CaDiCaL UNSAT on L-RED's encoding, not Lean, not refereed; without it the instance shows that SC-ISO at d = 4 forces T^R(3) ≥ 9): a REDUCTION of the W-channel part of SLOT-TRADE to an external-flip model inside the IDEAL model; bounds nothing polynomially; the CONJECTURES FLIP-ADD and SLOT-TRADE are not claimed; Ξ-cyclic genomes and genomes outside 𝓦_d are not covered; DATA: W-ONLY, step form: experiments/new/box162/flipcheck.py, 0 violations on 44,084 real steps (300 random 𝓛^R genomes with d = 2, 3, 4, 225 of them drawn ISO and 75 drawn without that restriction, 65 of these not ISO, and the 50 𝓛^R genomes in box160/out and box162/out, 36 of them ISO, every start); W-ONLY, ISO independence: the same tool, 0 violations on 31,320 (state, q) pairs of the 261 ISO genomes among them (the 225 drawn ISO and the 36 ISO corpus genomes); W-ONLY, frozen form: 0 violations on 1,044 (ISO genome, q) pairs; T ≤ T_2(d − 1) + 2: 0 violations on 28,896 ISO runs (b_0 changing at most twice and the steps moving levels ≥ 1 at most the exact per-genome maximum with two changes); NOW-ONCE, real runs: 0 violations on 307 pairs of consecutive moves of a level-1 mover; SWAP: 0 violations on 15,660 (state, c) pairs of the same 261 ISO genomes (no non-ISO genome tested); FLIP-1 upper bounds: 0 violations on 1,312 (2-level ISO genome, start) pairs, k = 0, …, 6; SC-ISO: the instance replayed by the same tool and by the box 150 checker; NOW-ONCE for c_t-step sequences, the concatenation clause of SWAP and the T_k(m) values for m ≥ 2: no signed DATA (the packet's §7 table is DATA only) (P-IDEAL-FLIP, docs/new/P-IDEAL-FLIP.md with its fixes entry 1, docs/new/P-IDEAL-FLIP-fixes.md; L-NEW successor 53). G-N5-TIME stays open.

Addendum (subagent, for the Lead; does not land; written 2026-11-05T14:30:27Z by date -u). (1) FIRST FILL on line L-2 (l-new 4c2e5124,
sha1 8099415b…), to CHECKER C122. NOT pushed; the only commits I made are the five merges (--no-ff) fe409908 (l-new 4c2e5124), 47230937
(referee 74fae0fa), a7eba516 (referee-2 b2c0fff8), 4ef99b6b (checker 177f8368) and 08c460d1 (l-comp 6f19564f) into trunk 61a1175c, as
briefed; this draft is a new, untracked file. Push trunk before landing. (2) TITLE l. 459 = "### R110 [refereed-only] " + L-2 without
its newline + ", CHECKER PASS (docs/checker/C122.md, checker PENDING)", checked by script after the fill (fill110.py, chk110.py): equal,
byte for byte (True); the only «### R» heading of this file. (3) BODY l. 459-710 (title l. 459 to the last body line; 0 "|" in
the range, by script); GAPS preamble l. 712-721 (its only "|" are the two inside the quoted closing « |», as in R107's to R109's
preambles); UPDATE l. 722 (one line, 0 "|", one <DATE>, one <HH:MM>, one <checker>; controls True ×13: R97's-R109's landed UPDATEs).
No Dead-ends row is drafted ((14)). A landing script in the shape of land109.py slices d[458:710] for the entry and reads
d[721] for the UPDATE (with «R110», «R109» as PREV, «C122» and the GAPS l. 11 assertion on «RESULTS R109 (P-IDEAL-SLOT» in place of
R109's values). (4) RE-RUNS: check.sh block «P-IDEAL-FLIP» from a git archive of 4c2e5124 (14:12:13Z-14:13:02Z, rc 0, PASS); my
genome-set split (fcstats.py); my own instance checks (mysim110.py); the L-1 → L-2 diff and byte test (wdiff110.py); the premise quote
test (prem110.py); the UPDATE build with its 13 controls (upd110.py). NOT RUN: the referees' tools (REFEREE's log read instead;
REFEREE-2 has none), the SAT runs behind the T_k(m) table and T^R(3) (lane DATA, not signed), L-COMP's cubes, the full check.sh,
scripts/verify.sh. (5) QUOTE SWEEP: chk110.py (chk109.py's rule: outermost guillemet quotes, whitespace joined, split at the ellipsis,
parts of 6+ characters; sources: packet, L-1, L-2, fixes, the referee files at their head commits, REFEREE's log, R2-T3R-audit.md,
notes/L-NEW.md, notes/REFEREE.md, notes/REFEREE-2.md, docs/new/N5-SLOT-box160.md, check.sh and flipcheck.py at 4c2e5124, the instance
JSON files, P-IDEAL-SLOT at e46e98a4, RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, NOW, LEAD-STATE, TARGET.md, CLAUDE.md, C118-C121,
notes/CHECKER.md, R109-draft, my re-run outputs, the commit subjects cited): 557 outermost quotes, 463 parts of 6+ characters, every
part found (0 not found); in the title and body alone 133 quotes, 131 parts, 0 not found; GAPS preamble and UPDATE 9 quotes, 7 parts, 0
not found. Line-precise check of the referee verdicts and other cited lines: 141 of 141 (source, cited line range, quote) triples found
verbatim, whitespace-normalised, inside the cited lines. Every sha1, line count and commit time cited was re-measured in this session
(sha1sum, wc -l, cmp, git log -1 on the commit), not copied from a report. (6) DISCREPANCIES: see (11) (D-1 to D-8; none affects a
verdict) and G-0 to G-14. I found no error in a signed statement. (7) FLAGS FOR THE LEAD AND CHECKER: G-0 (unbalanced parentheses in
L-2: note or L-3, CHECKER's call); G-9 (ii) (SWAP's DATA count covers ISO genomes only and not SWAP-RUN: note or E-item, CHECKER's
call); G-1 (the source note does not name the fixes file, which proves two clauses); G-8 (a) (CONDITIONAL DEAD under REFEREE's reading
of L42; whether a Lead reading records it). Nothing else is REQUIRED from my side. (8) NOT VERIFIED: the Lead brief of BOX 162 and the
routing of 11:49Z beyond the Lead commits ef4150d5, 92a78041 and ca8c640a; REFEREE-2's runs have no committed log; the referees' tools
were not re-run; the machine premise T^R(3) ≤ 8 (L-RED's encoding; L-COMP's encoding and REFEREE-2's audit of it) is not checked by me
and is not used by any signed statement; the lane's T_k(m) table is not re-run (not to sign). Scratch files (not committed) in
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r110: R110-template.md, fill110.py,
chk110.py / chk110.out, lp110.py, upd110.py / upd110.txt / upd110.out, wdiff110.py / wdiff110.out, prem110.py, fcstats.py / fcstats.out,
mysim110.py / mysim110.out, runw162.sh / raw162.sh / w162.out / w162raw.out, sim110.py / sim110.out, and the archive arch4c2e/. (9)
LANDING SIMULATION (sim110.py, on in-memory copies of RESULTS and GAPS at local trunk): RESULTS 11,901 -> 12,154 lines, a pure insertion
of 253 lines (the entry block with "checker PENDING)" filled, plus one blank line) directly after R109's block (R109 l. 11,030-11,321,
blank l. 11,322, byte-unchanged: True; R108's block, l. 10,812-11,028, byte-unchanged: True): True; R110 at l. 11,323-11,574, blank l.
11,575, the next line (**Erratum E-1**) moves to l. 11,576, «**Erratum E-2**» to l. 11,589, «## Dead ends» to l. 11,617; order R109,
R110, E-1, E-2, Dead ends: True; every other line byte-unchanged (common prefix and suffix: True); 0 "|" inserted. GAPS: only l. 11
changes: True; new l. 11 = old l. 11 with its closing " |" replaced by " " + the filled UPDATE + " |": True; "|" on l. 11 76 -> 76 (pipe
count unchanged); «UPDATE 2026-» 44 -> 44 plus 1 UPDATE head with the simulation year 2099, now the last on the line; 23 -> 23 lines.
Fill values used only for the simulation: <DATE> 2099-01-01, <HH:MM> 00:00, <checker> 0000000. (10) THIS DRAFT'S SHA1: a file cannot
state its own sha1. The sha1 of this file with the forty hex digits after the next colon replaced by forty «0» characters is:
d65d61a50e920bebd66fcc85170de2a623f24adb. The file's actual sha1 and line count are in the hand-back to the Lead (and re-measurable with
sha1sum).

Addendum 2 (subagent, for the Lead; does not land; written 2026-11-05T17:48:59Z by date -u). (1) SECOND FILL on line L-3 (l-new
47b4e165, sha1 4089bd73…), to CHECKER C122 Add. 1. NOT pushed; my commits: the three merges (--no-ff) 9ebdc441, 71459c3a, d599bdf0 and
one commit holding this file. (2) TITLE l. 484 = "### R110 [refereed-only] " + L-3 without its newline + ", CHECKER PASS
(docs/checker/C122.md, checker PENDING)", checked by script (chk110b.py): equal, byte for byte (True); the only «### R» heading of this
file. (3) BODY l. 484-757 (python slice d[483:757]; 0 "|"); GAPS preamble l. 759-771; UPDATE l. 772 (d[771]; one line, 0 "|", one each
of <DATE>, <HH:MM>, <checker>; 4,748 bytes; sha1 d76a5cfb4b09dcf1d24dfc7acad17c6ac1db185c of the line without newline, computed on the
UNFILLED form, as C122 §4 states it, «sha1 d76a5cfb4b09dcf1d24dfc7acad17c6ac1db185c of the line without newline»: equal). A landing
script slices d[483:757] for the entry and reads d[771] for the UPDATE. (4) THE ONE PLACEHOLDER (Signatures, REFEREE, L-3 sentence; and its pointer in Object) was replaced by the Lead at 18:29Z by date -u
with REFEREE §C add. 1 (5c02d44d); everything else in the entry is final for C122 Add. 1. (5) QUOTE
SWEEP (chk110b.py: chk110.py's rule and sources plus L-3, fixes and check.sh at 47b4e165, R2-P-IDEAL-FLIP-L2.md at 8fde383f, C122, my
second-fill outputs): 583 outermost quotes, 480 parts of 6+ characters, every part found (0 not found); in the title and body alone 142
quotes, 140 parts, 0 not found; GAPS preamble and UPDATE 12 quotes, 7 parts, 0 not found. Line-precise: 153 of 153 (source, cited line
range, quote) triples found verbatim, whitespace-normalised, inside the cited lines. (6) WORD DIFF dd6624ba → this file (wd110b.py,
difflib on whitespace tokens, Addendum 2 left out): 20 line regions, 76 token hunks (99 tokens deleted, 1198 inserted), every hunk in a
region listed in the SECOND FILL paragraph. (7) STALE STATUS in title and body (by script): «pending» once (the placeholder (4)) plus
the title fill «checker PENDING)»; «not yet» 0; «L-2» only as history (the line history, the L-2 verdicts and byte tests, the fixes
entries, the check.sh pins, the file name R2-P-IDEAL-FLIP-L2.md), never as the line of record; L-2 named as the current line, by script:
0 times. (8) LANDING SIMULATION (sim110.py, unchanged, on in-memory copies of RESULTS and GAPS at local trunk): RESULTS 11,901 -> 12,176
lines, a pure insertion of 275 lines (the entry block with "checker PENDING)" filled, plus one blank line) directly after R109's block
(R109 l. 11,030-11,321, blank l. 11,322, byte-unchanged: True; R108's block, l. 10,812-11,028, byte-unchanged: True): True; R110 at l.
11,323-11,596, blank l. 11,597, the next line (**Erratum E-1**) moves to l. 11,598, «**Erratum E-2**» to l. 11,611, «## Dead ends» to l.
11,639; order R109, R110, E-1, E-2, Dead ends: True; every other line byte-unchanged (common prefix and suffix: True); 0 "|" inserted.
GAPS: only l. 11 changes: True; new l. 11 = old l. 11 with its closing " |" replaced by " " + the filled UPDATE + " |": True; "|" on l.
11 76 -> 76 (pipe count unchanged); «UPDATE 2026-» 44 -> 44 plus 1 UPDATE head with the simulation year 2099, now the last on the line;
23 -> 23 lines. Fill values used only for the simulation: <DATE> 2099-01-01, <HH:MM> 00:00, <checker> 0000000. (9) NOT VERIFIED:
REFEREE's byte test of L-3 (not on file); the referees' tools not re-run; scripts/verify.sh and the full check.sh not run; the machine
premise T^R(3) ≤ 8 as before. Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r110/fill2 (edit110b.py, chk110b.py,
lp110b.py, wd110b.py, l3rel.py, R110-draft-dd6624ba.md) and
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r110/ (upd110b.py, upd110L3.txt,
runw162L3.sh, w162L3.out, w162L3raw.out, arch47b4/).
