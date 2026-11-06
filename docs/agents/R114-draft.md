# Draft RESULTS R114 (Lead; first fill 2026-11-06T17:42:16Z by date -u (subagent) on P-IDEAL-RISE line L-2, docs/new/P-IDEAL-RISE-line-L2.txt, l-new 0320ab9e, sha1 25170417891fec8d815cc23a30aa71c839369ada (draft sha1 ecd79952, CHECKER C127 5793c1e2: FAIL E-1); SECOND FILL 2026-11-06T20:18:52Z by date -u (subagent) on P-IDEAL-RISE line L-3, docs/new/P-IDEAL-RISE-line-L3.txt, l-new 0548afaa, sha1 4a553a296533b86de8bb3fce20a90ff0e13393e9) — to CHECKER C127 Add. 1 — NOT LANDED; goes after R113, before Erratum E-1
SECOND FILL (2026-11-06T20:18:52Z by date -u, subagent; for CHECKER C127 Add. 1). Read at the origin heads fetched at its start (git
fetch, 2026-11-06T20:1xZ): l-new a6744977 (its ancestor 0548afaa holds L-3 and fixes entry 2; the packet, L-1, L-2, L-3, the fixes,
experiments/new/box182/ (risecheck.py, risecheck.out, the four certificates), box150/check.py, box162/flipcheck.py and check.sh are
byte-equal at 0548afaa and a6744977, git diff empty; a6744977 adds L-NEW box 186 and changes no P-IDEAL-RISE file), referee 3489d797 (§C
add. 1 of R-P-IDEAL-RISE.md, the L-3 byte test; its l. 1-152 = 807a59c4's file, by diff), referee-2 bdbf0dde (Addendum 2 of
R2-P-IDEAL-RISE.md, the L-3 byte test; its l. 1-130 = 6c88dc46's file, by diff), checker 5793c1e2 (docs/checker/C127.md,
2026-11-06T18:30:21Z, 111 lines, sha1 c6e3cd19ed6b40e4c6009ac969ac1aab8971c1f8); origin trunk da6ff143 («Lead: REDUCE-XI (MOVES-2D =
quadratic T^R), DENSE kill query, box 186; log»), pushed, which holds the first-fill draft ecd79952 (commit 00a1805f, an ancestor). Local
trunk b876c884 = four merges (--no-ff, none an ancestor of da6ff143 before) into da6ff143: 9a426b8a (l-new a6744977), faa8c611 (referee
3489d797), d7eb47d8 (referee-2 bdbf0dde), b876c884 (checker 5793c1e2); then the commit holding this file. Not pushed; 0548afaa, 3489d797,
bdbf0dde and 5793c1e2 are NOT ancestors of origin trunk da6ff143 (git merge-base --is-ancestor); the Lead pushes trunk before landing.
RESULTS (sha1 ec119661…, 13,003 lines), GAPS (sha1 a27514c3…, 23 lines), TARGET.md, DECISIONS, DECISIONS-INDEX and CLAUDE.md are
byte-equal at b5ca0d4d and the local trunk (git diff, empty; last commit on RESULTS and GAPS: b5ca0d4d, R113's and Note E-3's landing);
docs/NOW.md changed after b5ca0d4d (the Lead's resume points) and the entry cites nothing from it. So the first fill's (0), (5), (6) and
the GAPS state in (9) stand (L-3's premise parenthesis is L-2's, by script), and Addendum 2 (8) re-runs the landing simulation. New
sources: docs/checker/C127.md: FAIL E-1 only (the first fill's G-9 (i): the «so R(x, k) ≥ moves(z)» half of the MOVE-RISE clause has no
counter and is not in the no-DATA list), notes G-M, G-2 (i), KEY without DATA, G-8 and G-11, G-U PASS, everything else PASS; E-1 fixed by
L-3 = L-2 with the one replacement of its §4 (l. 91-93), the UPDATE rebuilt by the same replacement; expected L-3 sha1 4a553a29… and
rebuilt UPDATE sha1 acc07ee1… (l. 94-97); the body sentences to update (l. 98-101). Line L-3, docs/new/P-IDEAL-RISE-line-L3.txt (l-new
0548afaa, 2026-11-06T18:56:55Z, the file's only commit; sha1 4a553a296533b86de8bb3fce20a90ff0e13393e9 with newline, 4,255 bytes, = C127
§4's expected value); fixes entry 2 (docs/new/P-IDEAL-RISE-fixes.md l. 44-59 at 0548afaa, L-NEW successor 57; file 59 lines, 5,734 bytes,
sha1 d8046a92f9081c01f488fbcdf51ba13843a9bcaf, l. 1-42 = entry 1's file, by script); REFEREE's byte test of L-3
(docs/referee/R-P-IDEAL-RISE.md §C add. 1, l. 154-166, 3489d797, 2026-11-06T19:37:37Z, file sha1
428c4bd5ba47cf99a963a2d96fa36265b64f6859, 166 lines: l. 159 «It gives sha1 4a553a29…, 4,255 bytes: EQUAL to L-3.», l. 166 «Verdict: L-3
MATCHES. All items stay SIGNED.»); REFEREE-2's byte test of L-3 (docs/referee-2/R2-P-IDEAL-RISE.md Addendum 2, l. 132-141, bdbf0dde,
2026-11-06T19:37:52Z, file sha1 d605db5658ba63aa37c8476d1ad8fd0550968f46, 141 lines: l. 136 «**Fixes entry 2: CORRECT.**», l. 140 «**Line
L-3: MATCHES.**», l. 141 «My SIGNs stand.»). My byte test of L-3 (fill2/l3rel114.py, rc 0): the old / new pair parsed by script from C127
§4 l. 92-93 (wrapped lines joined by one space, outermost guillemets), the old string once in L-2, the new string once in L-3, L-2 with
it = L-3 (True), one token hunk; fixes R5 (l. 55-56) carries the same pair (True); 74 «(» / 74 «)», depth never negative, final 0; 0 "|";
one « — »; «2026» once. Re-runs: check.sh block «P-IDEAL-RISE» from a git archive of 0548afaa's experiments/new and docs/new (l. 1-6, the
«cd» and «tmp» lines, l. 927-935; 2026-11-06T20:19:10Z-20:19:14Z, rc 0, PASS line «P-IDEAL-RISE: risecheck 0 violations, 4 certificates
CERTIFIED (output = frozen risecheck.out); pins packet 573ef117, line L-1 7e4273a9, tool 404df6de, output 3685b69b, certificates bf65a4e6
f878699f 7f3d88c3 71fb1683, fixes d8046a92, line L-2 25170417, line L-3 4a553a29: PASS» (fill2/runw182L3.sh, w182L3.out); risecheck.py's
raw output byte-equal to risecheck.out and to the first fill's, cmp); the UPDATE rebuilt from L-3 (fill2/upd114b.py: upd114.py's
procedure and controls unchanged, run on L-3; the 17 controls, R97-R113, are the landed UPDATEs, byte for byte, True, and their 58 output
lines are byte-equal to the first fill's, cmp; it equals the first fill's UPDATE with C127 §4's replacement, True; sha1 = C127 §4's
acc07ee1…, True); the quote sweep, the stale-status grep, the word diff and the landing simulation (Addendum 2). Changed at this fill,
and nothing else: this header line and this paragraph; the title (L-3); in the entry, Object (the packet identical at 0548afaa, fixes
entry 2, the line of record L-3, L-2 moved into the line history, the L-3 byte tests, L-3 changes no definition), Claims signed (the
third rounds), Claims (L-3), Premise (L-3), Fixes (entry 2: the header, two new bullets, the closing sentence), Data (the pins at
0548afaa, L-3's DATA parenthesis, the block re-run at 0548afaa), Signatures (REFEREE §C add. 1, REFEREE-2 Addendum 2, the lane commit),
INDEPENDENCE (L-3; the third rounds), TARGET.md diff (L-3); the GAPS preamble and the UPDATE (rebuilt from L-3); the digest of Addendum
(10); Addendum 2 (new). Honest limits (iv) and the Data paragraph's «not R(x, k) ≥ moves(z)» are unchanged: they already say that
MOVE-RISE's R(x, k) ≥ moves(z) has no lane count, which is what L-3's DATA now says (C127 §4 l. 100-101 «they stay true»). The FIRST FILL
text below (from FIRST FILL (this text) to (14)) and Addendum (1)-(9) are kept byte-unchanged as the record of the fill on L-2: where
they call L-2 the title line or the current line, quote L-2's DATA phrase «the identity of R(x, k) with the rises of cv of the Ξ-target:
no separate DATA» as the line's, flag G-9 (i) for a ruling or propose its wording, or give the first fill's line numbers, counts and
UPDATE sha1, they describe draft ecd79952 at 17:50Z; C127 ruled G-9 (i) E-1, G-M, G-2 (i), G-8 and G-11 notes and G-U PASS, as above,
used the number C127 (G-0), and the entry block follows L-3.
FIRST FILL (this text). Read at the origin heads fetched at its start (git fetch, just before the merges of 2026-11-06T17:30:04Z): l-new 0320ab9e (fixes entry 1, line
L-2 and the extended pins; the packet, L-1 and experiments/new/box182/ are byte-equal at the freeze 2f4d96de and at 0320ab9e, git diff
empty), referee 807a59c4 (§C of R-P-IDEAL-RISE.md; l. 1-129 = the report 33d148cd's, by diff), referee-2 6c88dc46 (Addendum 1 of
R2-P-IDEAL-RISE.md; l. 1-115 = the report 3b03d364's, by diff), checker bbc4a897 (already an ancestor of trunk; docs/checker/ ends at
C126.md); origin trunk b5ca0d4d («Lead: RESULTS R113 IDEAL-ALIGN landed (P-IDEAL-ALIGN line L-3; C125 Add. 1 bd7cb5e4) and RESULTS Note
E-3 (C126 Add. 1 2f58a8bf); GAPS line-11 UPDATE; log»), pushed. Local trunk 8ac6757b = three merges (--no-ff, none an ancestor of
b5ca0d4d before) into b5ca0d4d: e6afb606 (l-new 0320ab9e), 14783386 (referee 807a59c4), 8ac6757b (referee-2 6c88dc46); then the commit
holding this file. Not pushed. 0320ab9e, 807a59c4 and 6c88dc46 are NOT ancestors of origin trunk b5ca0d4d (git merge-base
--is-ancestor); 2f4d96de, 33d148cd and 3b03d364 are. The Lead pushes trunk before landing. The body makes NO statement about trunk (C113
E-2). RESULTS (sha1 ec119661a26a07ebfe06c511966548c2b10f365d, 13,003 lines), GAPS (sha1 a27514c3363bd52aa248039dd2db5203b9705abe, 23
lines; l. 11 76 "|", 48 «UPDATE 2026-»), TARGET.md, DECISIONS, DECISIONS-INDEX, NOW and CLAUDE.md are byte-equal at b5ca0d4d and
8ac6757b (git diff --quiet). Last commit on RESULTS and GAPS: b5ca0d4d (2026-11-06T17:00:48Z, R113's and Note E-3's landing).
Sources read: the packet docs/new/P-IDEAL-RISE.md (frozen 2f4d96de, sha1 573ef1171eec0f48aad974d221050681fc09ecc4, 220 lines, 24,930
bytes; unchanged at 0320ab9e), line L-1 (2f4d96de, 7e4273a97993e6e67fb8b7c81d6e215ceaa7bbbe, 3,914 bytes), fixes entry 1 (0320ab9e,
docs/new/P-IDEAL-RISE-fixes.md, sha1 469cb2915b58e716ed8b7c692b12fa70e6c3f245, 42 lines, 4,070 bytes), line L-2 (0320ab9e, sha1
25170417891fec8d815cc23a30aa71c839369ada, 4,218 bytes); experiments/new/box182/risecheck.py (sha1
404df6de34c24ea8e86c305ae059ca3ce43db746, 203 lines; read in full), risecheck.out (sha1 3685b69bcdc03bf261931e94ef3427550026a1b6, 6
lines), the four certificates experiments/new/box182/cert/cert_PHX_d3_s1793.json (71fb16831f47d8f2de6fc58791b749e672c3dc2a),
cert_PBG_d2_s179.json (bf65a4e6cd20d497b7fed5dc7ab7c03752bf38cf), cert_PBG_d3_s1793.json (f878699ff959bf08f26d001275de2000a6bb68f1),
cert_PBG_d4_s1794.json (7f3d88c349511baa4abe78139ac5f9f019edd339), the simulator experiments/new/box150/check.py (Gen, topo; sha1
019de0f7…, 214 lines) and experiments/new/box162/flipcheck.py (rand_lr, is_lr; sha1 9fd0b192…), experiments/new/check.sh block
«P-IDEAL-RISE» (l. 927-934 at 2f4d96de and at 0320ab9e; the file 935 lines, sha1 a23e35127cfedec9f04ab2372981a9790d353b0b at
0320ab9e); REFEREE successor 24's docs/referee/R-P-IDEAL-RISE.md (report 33d148cd, §C 807a59c4) with scratch/cert_check.py,
scratch/rise_probe.py and rise_logs/ (cert_PHX_d3.txt, cert_PBG.txt, cert_controls.txt, probe.txt); REFEREE-2 successor 28's
docs/referee-2/R2-P-IDEAL-RISE.md (report 3b03d364, Addendum 1 6c88dc46) with R2-P-IDEAL-RISE/r2cert.py, r2cert.out, r2rise.py and
r2rise_seed182.out; RESULTS R104 (title l. 9864), R105 (l. 10155), R110 (l. 11323), R111 (l. 11598), R112 (l. 11909-12150), R113
(l. 12152-12392), Erratum E-1 (l. 12394), E-2 (l. 12407), Note E-3 (l. 12435) and the Dead-ends heading (l. 12466); GAPS l. 11;
docs/agents/LEAD-STATE.md (2026-11-06 entries to 17:00Z); docs/checker/C120.md-C126.md; docs/agents/R112-draft.md and R113-draft.md as
landed (the models of this draft).
Re-runs (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r114, from a git
archive of 0320ab9e's experiments/new and docs/new, nothing written into the repository): (a) check.sh block «P-IDEAL-RISE» (l. 1-6,
the «cd» and «tmp» lines, l. 927-934), 2026-11-06T17:33:57Z-17:34:02Z, rc 0, PASS line «P-IDEAL-RISE: risecheck 0 violations, 4
certificates CERTIFIED (output = frozen risecheck.out); pins packet 573ef117, line L-1 7e4273a9, tool 404df6de, output 3685b69b,
certificates bf65a4e6 f878699f 7f3d88c3 71fb1683, fixes 469cb291, line L-2 25170417: PASS» (runw182.sh, w182.out); risecheck.py's raw
output byte-equal to risecheck.out (cmp; w182raw.out); (b) my split of risecheck.py's counter sets (rsstats.py: runs the frozen tool's
source unchanged in a namespace, its 6 output lines captured, then measures on the tool's own sets; my DATA, not lane DATA, not wired
into check.sh): corpus 201 files (box150 3, box152 4, box156 3, box157 1, box160 52, box162 12, box163 37, box164 50, box165 6, box169
1, box171 3, box172 3, box173 1, box174 7, box175 1, box180 17; d 1: 2, 2: 10, 3: 70, 4: 66, 5: 38, 6: 13, 8: 2) with 170 distinct
parsed contents (20 groups of copies), 199 of them carrying a stored «xorder»; every corpus, random and certificate genome Ξ-acyclic by
my own depth-first search; 200 random genomes, all in 𝓛^R_d by is_lr (d 1: 52, 2: 49, 3: 57, 4: 42); PHIK: 15,392 states of the
random genomes, 13,409 of them with a step (1,983 without: the run stops there), 1,491 drops of exactly 1; 975 steps of the 201 corpus
runs, 281 drops of exactly 1; totals 14,384 and 1,772 (= the tool); PHIK-T (T ≤ Φ_K(s_0) ≤ 2^(d+2) − 2d − 4, and T = 0 from an
all-aligned start) 0 violations on the 401 stored-start runs; RISE: 401 runs = 201 corpus + 200 random, 57 of them with T = 0, 1,968
moves, 18,780 (step, option) pairs; the identity of R(x, k) with the rises of cv of the Ξ-target 0 violations on 5,076 (run, option)
pairs; MOVE-RISE's R(x, k) ≥ moves(z) 0 violations on the 3,248 (run, option with a mover Ξ-target) pairs (equality on 2,726); T ≤ 1 + M
max R 0 violations on the 401 runs; the four certificate files: PHX d 3 61 / 7 / 5 (dec / lo / hi) rows over 64 distinct genomes, PBG d
2 21 / 7 / 10 over 36, PBG d 3 58 / 9 / 10 over 67, PBG d 4 79 / 12 / 17 over 60, every row's genome carrying «xorder» (rsstats.out);
(c) both referees' certificate checkers re-run on the four certificate files of the archive (2026-11-06T17:38:31Z-17:38:36Z, rc 0 ×8):
REFEREE's scratch/cert_check.py prints «residual-features 0 sum_a 1 sum_b 1» and the bounds 22, 8 and the two p/q; REFEREE-2's
r2cert.py prints «VERIFIED» four times; both p/q digit-identical to risecheck.out's and to the referees' committed logs (pq114.py:
equal ×4; refcert_referee.out, refcert_referee2.out); (d) the L-1 → L-2 byte test and token diff (wdiff114.py); (e) the premise quote
test (prem114.py); (f) the UPDATE build with 17 controls (upd114.py); (g) the quote sweep, the line-precise check, the stale-status grep
and the landing simulation (chk114.py, sim114.py).
LESSONS APPLIED. C113 E-1: the title is L-2 verbatim with no insertion. C114 Add. 1 E-1: the UPDATE head carries «<DATE>». C115 E-1:
the premise route is checked against what RESULTS records (G-4; prem114.py, hits per quote). C116 G-1, C118-C125 §4: the UPDATE rule
of R111 (sentinel_build111 with its default drops and the «(DATA, » opening, and its DEAD-clause step), one adaptation flagged (G-U).
C116 G-2: name clashes settled by one body sentence (G-6). C117 E-1 / E-2: no sentence wider than signed (one flag, G-2 (i)); the
feature classes inlined in Claims (f). C118 E-1: no stale status sentence; the entry calls nothing «pending» (the only «PENDING» is the
title fill) and states no other item's status as current except landed RESULTS entries (G-11). C118 §3 / Erratum E-2: EVERY
DEFINITION of L-2 diffed against the packet, and §5's feature definitions against risecheck.py's code (G-2). C120 §5 / C121 §5 / C122
E-2 / C124 E-1 / C125 E-1: EVERY DATA clause of L-2 tested against risecheck.py's counter code: unit, set, and the statement's scope
(G-9; one clause flagged, G-9 (i)). C122 G-0: parentheses balanced (G-1). C122 E-3: the source note names every proof-carrying file
(G-1). C123 E-1: no lane label and no packet name in the title before the claims (G-1). C123 E-2: no stale referee state (G-13).
C119 E-1: every «referee X did Y» is checked against that referee's file (line-precise check, Addendum (5)). R112 / C123 §3: the
machine items say exactly what rests on the machine (body «What rests on the machine»; G-M).
to check: FLAGS FIRST (G-0 to G-14; the ones for the Lead or CHECKER: G-0 (number), G-9 (i) (MOVE-RISE's DATA does not cover its «so
R(x, k) ≥ moves(z)» half; C125 E-1 class), G-M (the tool's acyclicity test is vacuous on the certificate genomes; what rests on the
machine), G-U (one UPDATE adaptation), G-2 (i) (KEY's equal-option clause at level 0) and G-8 (scope tail)), then the CLEAN items and
(0)-(14). A NOTE FOR THE LEAD that is NOT part of this entry: G-C (R113 is landed and carries ALIGN (a), (c) and KP-MOVE; L-RED's
lane work on RISE-2D).
- G-0, THE CHECKER NUMBER. «C127» occurs 0 times in the repository at 8ac6757b and on every origin branch (git grep over the fetched
  heads); «R114» 0 times in RESULTS and GAPS; docs/checker/ ends at C126.md (C125 = R113, C126 = Note E-3). This draft uses C127 (title
  fill, UPDATE head, GAPS preamble).
- G-9, DATA (the C120 §5 / C121 §5 / C124 E-1 / C125 E-1 check item: unit, set and the statement's scope of every count, against
  risecheck.py's counter code, read by me in full at 404df6de). Every figure of L-2's DATA parenthesis equals risecheck.out and my
  re-run: «14,384 steps» = «phik_steps 14384»; «equality on 1,772» = «phik_tight 1772» (drops of exactly 1, i.e. equality in Φ_K(s_t) ≤
  Φ_K(s_(t−1)) − 1); «200 random» = «random 200»; «201 in-tree … genome files» = «corpus_files 201»; «72 forcing genomes» =
  «optk_transitions 72» (= 2 · (1 + … + 8)); «401 stored-start runs» = «rise_runs 401»; «1,968 moves» = «rise_moves 1968»; «the four
  certificates» = the four CERT lines, each «CERTIFIED». Counter by counter:
  - PHIK (l. 42-52): phik_step counts the transition s → step(s) only where step(s) is defined (l. 43-44, «if n is None: return»), from
    every state of the 200 random genomes (l. 47-49) and from every state of the 201 stored-start corpus runs (l. 50-52; its last state
    has no step). Unit «steps», set as worded: MATCH (my split: 13,409 + 975). Scope: PHIK-DESCENT is stated on 𝓛^R_d; the random genomes
    pass is_lr and are Ξ-acyclic by construction (rand_lr draws Ξ-targets later in a random order; my DFS: all acyclic); the corpus is
    filtered by is_lr and acyclic (l. 36). REFEREE l. 106-107; REFEREE-2 l. 85-87.
  - OPTK (l. 90-101): one check per τ(l, p) genome, the conjunction of: step(s) defined, τ in 𝓛^R_d and acyclic, Mv_1 = {p}, k(p) 1 → 0,
    both level-(l + 1) movers 0 → 1, every other k bit unchanged, and the all-1 and all-0 k-states exist (built level by level, l. 85-89).
    «the OPT-K forcing step and both extreme states on the 72 forcing genomes for d = 1-8, 0 failures»: MATCH (REFEREE l. 108; REFEREE-2
    l. 88-89). The Theorem is proved for every d; d ≤ 8 is the DATA range only, as the line says.
  - RISE_A (l. 112), per (run, step, option): a FALL of an option value; «non-decreasing values»: MATCH. RISE_B (l. 118), per run: «R(x,
    k) ≤ T»: MATCH. RISE_C (l. 119), per run: «T ≤ 1 + #{t ≤ T − 1 with a rise} ≤ 1 + Σ R» with rs counted over t ≤ T − 1 (l. 113): MATCH
    (its «and T >= 1» guard is harmless: at T = 0 the inequality holds). The identity of R(x, k) with the rises of cv of the Ξ-target: no
    counter, and the line says «no separate DATA» (fixes W-2 counter check l. 14-18; REFEREE §C l. 141-144 «The text is EXACT.»;
    REFEREE-2 Add. 1 l. 122).
  - (i) MOVE-RISE (FLAG, C125 E-1 class: set). «MOVE-RISE 0 violations on 401 stored-start runs with 1,968 moves»: the counter MOVERISE
    (l. 114-117) tests, at every move of z, «g.face(S[t], z, S[t][z]) > g.face(S[t - 1], z, S[t - 1][z])», i.e. only the first half of the
    line's MOVE-RISE clause, «a move of z at step t gives cv_(s_t)(z) > cv_(s_(t−1))(z)». The clause's second half, «so R(x, k) ≥ moves(z)
    when the Ξ-target of (x, k) is the mover z» (packet §4 l. 163, Corollary MOVE-RISE-R), has no counter. It does NOT follow by
    arithmetic from the counted checks alone (the C125 G-9 (iii) test for a note): it needs the identity of R(x, k) with the rises of
    cv(z), which the line itself gives «no separate DATA». (Inside the tool the identity holds by the code of face, which sums the ε's
    along the chain (box150/check.py l. 58-65), i.e. by ENC as implemented, not by a check.) Measured for this draft on the same 401
    runs (rsstats.py; my DATA, not lane DATA, not wired into check.sh): R(x, k) ≥ moves(z) 0 violations on 3,248 (run, option with a
    mover Ξ-target) pairs, the identity 0 violations on 5,076 (run, option) pairs. Both referees' own tools cover MOVE-RISE-R (their
    DATA, not the line's): REFEREE l. 89 (5,234 checks), REFEREE-2 l. 75 «MOVE-RISE-R: 125,856 pairs.». Neither raised it on the line:
    REFEREE-2's W-2 (l. 90-93, 111-113) named only (a)'s identity, and REFEREE §C l. 141-144 checked the W-2 text. Per the brief the line
    is not changed here; CHECKER rules E-item or note. If E: one possible L-3 wording, not mine to choose and not a quotation: the old
    string "the identity of R(x, k) with the rises of cv of the Ξ-target: no separate DATA" (once in L-2, by script) → "the identity of
    R(x, k) with the rises of cv of the Ξ-target and MOVE-RISE's R(x, k) ≥ moves(z): no separate DATA".
  - CERT (l. 165-201): one check per certificate file, the conjunction of: every row's genome in 𝓛^R_d with N = 2d and acyclic (l.
    167-169), every «next» equal to the simulator's step (l. 170-172), features recomputed in Fractions (l. 173-178), the multipliers
    re-solved by exact Gaussian elimination on the certificate's support (l. 179-193), not inconsistent, 0 negative, 0 free (l. 194-195).
    «the four certificates experiments/new/box182/cert/*.json re-checked in exact arithmetic»: MATCH (the directory holds exactly these
    four .json files). The acyclicity part is vacuous on these genomes: G-M.
  - (ii) PHIK-DESCENT's «so T ≤ Φ_K(s_0) ≤ 2^(d+2) − 2d − 4 and T = 0 from a start where every mover is on KP» (PHIK-T; NOTE, C125 G-9
    (iii) class): no counter of its own; it follows by arithmetic from the per-step PHIK check on the same runs (Φ_K ≥ 0 and the drop ≥ 1
    at every step of each checked run; Φ_K(s_0) ≤ Σ_x w_lev(x)). My measurement: 0 violations on the 401 stored-start runs.
  - (iii) RISE-EQUIV's «≤ 1 + M max_(x,k) R(x, k), so on any family max_(x,k) R(x, k) is bounded by a polynomial in N + M iff T is»
    (NOTE): the first is arithmetic from Σ R ≤ M max R (my measurement: 0 violations), the second is not a finite check.
  - (iv) KEY (NOTE): the DATA parenthesis names no count for KEY and has no «no separate DATA» phrase for it (R113's DATA said «KP-MOVE
    outside 𝓛^R_d: no separate DATA»). risecheck.py has no KEY counter; PHIK and OPTK use KP through kbits (l. 22-23). An absence, not a
    wrong count.
  - (v) SCOPE (NOTE): RISE-EQUIV and MOVE-RISE are stated «at any degree»; their DATA is on the 401 runs of the 𝓛^R_d genomes of the DATA
    head only (the C125 PATH-RISE note, the C122 W-ONLY precedent). OPT-K's parenthesis «(forcing genomes with every Ξ-target the exit X,
    in which every mover moves at most once)»: «every Ξ-target the exit X» holds by construction (l. 61, Ξ-target −1); «every mover moves
    at most once» is not counted (OPTK tests the first step only).
  - (vi) PRECISION, «201 in-tree 𝓛^R_d genome files»: 201 files with 170 distinct parsed contents; «files» is exact (C124 G-9 (vi), R113
    Honest limits (iv) precedent); the glob is box150 to box181 (l. 32), and no box181 file is in the set. Note.
- G-M, WHAT RESTS ON THE MACHINE (FLAG for CHECKER; the R112 / C123 §3 item). (a) The two certificate items C-PHX3 and C-PBG are signed
  by both referees as machine items (REFEREE l. 17 «SIGN as CERTIFIED machine items: all four certificates RE-VERIFIED independently
  (§3)»; REFEREE-2 l. 17 «**SIGN as machine-certified** (Opus 5.5, D12): all 4 certificates re-verified by my own independent code in
  exact arithmetic»); the line says «by exact rational certificates checked by machine». The body's «What rests on the machine»
  separates (i) PROVED (the certificate inequality, packet l. 185-188; «exactly 22» from Φ_K), (ii) MACHINE (the four files satisfy the
  certificate conditions; the exact bounds), (iii) the trusted base (three Python programs in exact Fraction arithmetic: the lane's
  risecheck.py with box150's Gen, REFEREE's cert_check.py with t3r_sim.py, REFEREE-2's r2cert.py with r2sim.py; no formal verification,
  no Lean), (iv) NOT TRUSTED (the floating-point LP that produced the certificates; the stored float multipliers), (v) NOT MACHINE (the
  five proved items). (b) PRECISION OF THE LANE'S CHECK (note, no result affected): packet l. 190-191 says the tool «checks every genome
  is in 𝓛^R_d and Ξ-acyclic». risecheck.py's acyclic() (l. 25-27) calls topo, which returns a stored «xorder» unchecked (box150/check.py
  l. 38 «if "xorder" in G: return list(G["xorder"])»); every row of the four certificate files carries «xorder» (rsstats.py), so the
  tool's explicit acyclicity test is vacuous on them. Acyclicity holds: my DFS (all certificate genomes Ξ-acyclic); the tool's xheight
  (l. 124-130, called by feats on every row's genome) recurses over every Ξ-edge and would fail on a Ξ-cycle (unbounded recursion, a RecursionError, so no «CERTIFIED»); REFEREE l. 74
  «Every transition equals my simulator's step, and every genome is in 𝓛^R_d and acyclic.»; REFEREE-2 l. 61 checks «that every genome
  is in 𝓛^R_d and Ξ-acyclic». The body states it (What rests on the machine (vi)). (c) The machine premise's files (the four certificates,
  risecheck.py) are named in the line's DATA parenthesis, not in its source note; REFEREE-2 l. 104-105 «The source note names
  P-IDEAL-RISE.md, the only file with proofs; the certificate files are named in the DATA.». CHECKER: note or E-item.
- G-U, THE UPDATE RULE, ONE ADAPTATION (FLAG). L-2 has five labelled clauses (KEY, PHIK-DESCENT, OPT-K, RISE-EQUIV, MOVE-RISE) and then
  one unlabelled clause, «; and, by exact rational certificates checked by machine, … for PBG at d = 2, 3, 4», before the date. build()
  takes every label's clause up to the next label, and the last label's clause to the end of the claims, so the default R111 call puts
  «(MOVE-RISE)» behind the certificate clause, i.e. it would label the certificate clause MOVE-RISE (upd114.py prints it: True). The
  R111 procedure has the step for exactly this shape: r111_proc cuts the unlabelled «; and DEAD: …» clause before the build and puts it
  back behind the last label. upd114.py applies that step, unchanged in form, to the certificate clause (cut before the build, put back
  behind «(MOVE-RISE)»). Cross-check: a direct build (claims split before each «; (LABEL) », each label behind its clause, the
  certificate clause after the last, the tail opened and the two scope sentences dropped by string replacement) is equal (True).
  Everything else is R111's default call (drops, «(DATA, » opening, source parenthesis kept, «. G-N5-TIME stays open.»).
- G-2, DEFINITIONS DIFFED (the C118 §3 / Erratum E-2 lesson; my own diff). (o) Premise parenthesis = packet l. 22-41 (G-4). Definitions:
  «T the number of steps of a run» = §0 l. 57 («T := the number of steps.»); «Mv_t the movers of step t» = l. 57; «moves(x) the number
  of steps t with x ∈ Mv_t» = l. 65, the E-2 (E2c) binder; «KP_s(x) the option of x with the least key under s» = l. 66 (unique by
  (F1)); «k_s(x) := [s(x) ≠ KP_s(x)]» = l. 66; «on 𝓛^R_d w_l := 2^(d−l) − 1» = l. 73 for 0 ≤ l ≤ d − 1 (w_d := 0 is a proof device of
  §2, not in the line); «Φ_K(s) := Σ_x w_lev(x) k_s(x)» = l. 73; «v_s(x, k) the integer value of option (x, k) under s (R105 ENC)» = l.
  71 (v_s(x, k) := Σ over the β's of Ξ_s(x, k) of ±2^rank, + for even parity); «cv_s(z) := v_s(z, s(z))» = l. 71; «R(x, k) the number of
  steps t with v_(s_t)(x, k) > v_(s_(t−1))(x, k)» = l. 71-72 (t ∈ [1, T] implicit); «M the number of options» = l. 72 (= R104's «M := Σ
  deg(x)»). N, lev(x), option index, gate index, step and run are R104's. Claims: KEY = §1 (a) l. 76-77 (its «Hence» sentence not in
  the line: narrower), (b) l. 78, (c) l. 79 (see (i)); PHIK-DESCENT = §2 l. 91 with PHIK-T l. 92-93 (the middle «Σ_x w_lev(x) = 2
  Σ_(l=0..d−1) (2^(d−l) − 1)» not in the line); OPT-K = §3 l. 117-121 (the intermediate «≥ Σ_x w_x» not in the line; «range on every
  genome» = «max_s Φ(G, s) − min_s Φ(G, s)» per G); RISE-EQUIV = §4 l. 151-154 (the middle «#{t ∈ [1, T − 1] : …}» term not in the
  claim, only in the DATA); MOVE-RISE = l. 160 with MOVE-RISE-R l. 163; the certificate clause = §5 C-PHX3 l. 180-182 and C-PBG l.
  183-184 with the range binder of R1 = §5's «sup_(G,s) Φ − inf_(G,s) Φ … (over G ∈ 𝓛^R_3 and their states)»; «every potential linear
  in the features with weights not depending on the genome» = l. 178-179 (a class potential with a constant a; the line's «linear» is
  the same class, the constant cancels in a range); «falls by at least 1 at every step» = the decrease property «Φ(G, s) − Φ(G, step(s))
  ≥ 1 at every transition». The feature classes are named in the line by glosses plus «of the packet»: «PHX (key, Ξ-unhappiness and
  pair-state bits, Ξ-height counts, cross-level products)» = BASE + P + H + X, «PBG (key, Ξ-unhappiness and pair-state bits, value
  budgets and value gaps from the ENC integers of the maximal Ξ-paths)» = BASE + P + B + G (l. 168-179); the glosses do not name u = z·k
  or ord_l(s), which BASE and P contain; the exact classes are §5's, inlined in the body (Claims (f)). §5 against risecheck.py's feats
  (l. 139-164) and xheight / pathvals (l. 124-138), by me: z by «g.face(s, x, 1 - s[x]) > g.face(s, x, s[x])» (the ENC order; RI-P1), k, u =
  z & k; P: the indicator «pair%d_%d%d%d%d» of the realised (k(2l), k(2l + 1), z(2l), z(2l + 1)) and «ord%d» = [K[2l] < K[2l + 1]]; H:
  per (level, height) the counts of z = 1 and of u = 1, h by recursion over every option with X counting 0; X: z(a)k(b) and k(a)z(b) for
  l ≤ d − 2; B: P − 1 − ic, (P − 1 − ic) / max(1, P − 1) and the level sums; G: io − ic, max(0, io − ic), max(0, io − ic) / max(1, P −
  1) and k · max(0, io − ic); PV the sorted distinct path integers. ALL EQUAL. Both referees wrote the features from §5's text and
  reproduced every bound (REFEREE l. 61-66; REFEREE-2 l. 59-62).
  (i) FLAG (C117 E-1 class: no sentence wider than signed). KEY's third part in L-2, «two movers of one level on the same option j have
  the order of their keys given by their gate indices of option j», is stated for every level of 𝓛^R_d; packet (c) concludes only «If
  s(2l) = s(2l + 1) = j and l ≥ 1, then ord_l(s) = γ_l(j).» (l. 79; its hypothesis line also lists «l = 0», with no conclusion for it).
  At level 0 the clause holds by the definition of keys: §0 l. 54 «key_s(x, k) := (g(x, k)) if lev(x) = 0», and KEY (a)'s proof l. 80
  «Level 0: key_s(y, k) = (g(y, k)) for every s.»; so it is true and its proof is in the packet's text, but packet (c) does not state it.
  Both referees MATCHED the clause (REFEREE l. 103-104 «Claims KEY, PHIK-DESCENT, OPT-K, RISE-EQUIV and MOVE-RISE MATCH their signed
  forms.»; REFEREE-2 l. 102-103 «each equal or weaker than the signed statements»). CHECKER: note or E-item (an E-item would be an L-3
  inserting «l ≥ 1» or a fixes-entry sentence; not mine to choose).
  (ii) NOTE. «KP_(s_t)» in KEY's degree-2 clause is KP_(s_t)(x) for the moving mover (packet (b) l. 78).
- G-3, STRICT SYMBOL TEST (notes). s, t, x, z, k, j, l, a, w_x are bound in their clauses; «d» is free in 𝓛^R_d (each clause «on 𝓛^R_d»
  or «for d ≥ 1»); «N» is R104's number of movers; «X» is R104's exit; «𝓛^R_d» is R110's (premise); «cv of the Ξ-target» is cv_s(z) for
  the Ξ-target z; «PHX», «PBG» and «Ξ-unhappiness» are glossed in the line and defined in packet §5 (z_s(x)); «MOVES-2D» is named in the
  scope tail without a definition (it is defined in docs/new/N5-RISEPROOF-box181.md l. 20-21, not in the packet; «not claimed», so
  nothing rests on it); «RISE-2D» is glossed in the tail («(every option of a run on 𝓛^R_d rises at most 2d times)» = packet §4 l.
  164-165).
- G-4, PREMISE ROUTE (the C115 E-1 class): CLEAN (prem114.py on RESULTS at 8ac6757b = b5ca0d4d for this file). L-2's premise
  parenthesis: «premise: R104's definition of the model only, no theorem of R104 used; RESULTS R105's ENC, MONO, XI-NEW and RISE only;
  RESULTS R110's definition of 𝓛^R_d only; and RESULTS R111's CASCADE only» = packet l. 22-41. Hits, whitespace normalised: ENC (265
  characters) 2: R105's title l. 10155 (the source) and R113's body l. 12254-12255 (its Premise quotes R105 verbatim); MONO (69
  characters) 2: l. 10155 and R113's body l. 12256 (the same); XI-NEW (169 characters) 1, l. 10155; RISE (136 characters) 1, l. 10155;
  R110's 𝓛^R_d wording (191 characters) 3: R110's title l. 11323 (the source), R112's body l. 12020-12021 and R113's body l. 12257-12259
  (both quote R110 verbatim); with its R110 context («(premise: R104's definition of the model only, no theorem of R104 used; and RESULTS
  R109's SEG-ONCE at l = −1 only), on acyclic Ξ-graphs, with 𝓦_d …») 1 hit, l. 11323; CASCADE (225 characters) 1, R111's title l.
  11598. At the packet's trunk c8fefddb (2026-11-06T12:12:20Z): ENC, MONO, XI-NEW, RISE and CASCADE 1 hit each, R110's wording 2 (R110,
  R112) (D-2). R104: the packet restates the definition in §0 (l. 44-73, «RESULTS R104's definition, as restated in P-IDEAL-FLIP §0»);
  R104's own wording, «an IDEAL genome G has N movers x with levels lev(x), M := Σ deg(x) options (x, k), …» (861 characters, as packet
  P-TR3 §1 l. 7-14 quotes it), 1 hit, R104's title l. 9864; REFEREE-2 l. 22-24 diffed §0 against its P-IDEAL-KEYS diff of R104 «plus
  (F3) (keys read only lower levels), which follows from the recursive key». Use: ENC in §4 and as the name of the path order in §5
  (fixes RI-P1, l. 8-11), MONO in RISE-EQUIV (a), XI-NEW and RISE in RISE-EQUIV (c) (packet l. 155-159), R110's wiring in KEY (a), (c) and
  through them in PHIK-DESCENT, OPT-K and the certificates, CASCADE in PHIK-DESCENT (l. 99-100) and OPT-K's forcing step (l. 138); R104's
  definition everywhere. Not used: packet l. 38-41 (R105 KEYFLIP, LOCAL and every other R105 item; R106-R110 theorems; R111 PAIR-KF,
  LOCAL-KP and its other items; R112; P-IDEAL-ALIGN, now RESULTS R113 (G-11 (i)); docs/lit, docs/sources, any other lane file). The
  only machine premise is §5's tool, for the two certificate items (packet l. 40-41). Erratum E-2 does not bear (G-5). No unlanded
  result, no lit note and no lane file is a premise of a signed statement. REFEREE §1 l. 22 «Byte tests on trunk c8fefddb, each FOUND
  verbatim (1 hit): R105 ENC, MONO, XI-NEW, RISE; R110's 𝓛^R_d wording; R111 CASCADE.»; REFEREE-2 l. 22-23 «verbatim substring of
  docs/RESULTS.md at trunk c8fefddb».
- G-5, ERRATA (note). Erratum E-1 concerns R97-R100 counts. Erratum E-2 corrects R105's CHAIN-BACK binder (E2a), TOP-MONO's RANK_t
  (E2b) and KEYFLIP's moves(x) (E2c); L-2 uses R105's ENC, MONO, XI-NEW and RISE, which E-2 leaves unaffected («Unaffected: R105's other
  definitions»); moves(x) carries the (E2c) binder anyway (packet l. 29-31). Note E-3 concerns R110's CONDITIONAL DEAD; L-2 uses R110's
  definition of 𝓛^R_d only. Not bearing.
- G-6, NAMES (by script on RESULTS ec119661 / GAPS a27514c3; note; C116 G-2's remedy). 0 times in RESULTS and GAPS: «R114», «C127»,
  «P-IDEAL-RISE», «PHIK», «OPT-K», «RISE-EQUIV», «MOVE-RISE», «RISE-2D», «MOVES-2D», «PHX», «PBG», «C-PHX3», «C-PBG», «Φ_K», «k_s(x)»,
  «risecheck». Same names, other meanings: «(KEY)» once, in R38's title (l. 1816), and «Lemma KEY» inside R104's body (l. 9954, 10053,
  10086, R104's packet lemma); «R(x, k)» in R111 (title l. 11598, RETURN: «R(x, k) the number of steps at which cv of the Ξ-target of
  (x, k) rises»; body l. 11697) is the rises of cv of the Ξ-target, here the rises of the option value v(x, k): equal by RISE-EQUIV
  (a); «P(x)» in packet §5 counts maximal Ξ-paths, as R113's P(z), not R99's P(z). Consistent: «RISE» and «XI-NEW» are R105's items
  (premises, same meaning); «CASCADE» is R111's (premise). One body sentence (Honest limits (viii)).
- G-7, L41 (the C109 E-1 class): not triggered (my reading). The proofs are L-NEW successor 56's (packet l. 2, 6-7); the fixes entry
  carries no proof; R1 is REFEREE-2's W-1 form and R2 REFEREE-2's W-2 text verbatim (fixes l. 22, 25), line wording, not proof steps;
  the referees' cert_check.py, r2cert.py and simulators are checking tools. Neither referee mentions L41.
- G-8, THE SCOPE TAIL (NOTE for CHECKER). (a) «a POTENTIAL / EQUIVALENCE statement inside the IDEAL model» describes the potential items
  (PHIK-DESCENT, OPT-K, the certificates) and RISE-EQUIV's equivalence; KEY and MOVE-RISE are structure lemmas. A description, not a
  claim; no clause is narrowed by it. (b) «the conjectures RISE-2D (…) and MOVES-2D are not claimed»: MOVES-2D is undefined in the line
  and the packet (G-3); nothing rests on it. (c) «Ξ-cyclic genomes and genomes outside 𝓛^R_d (outside RISE-EQUIV, MOVE-RISE and the
  degree-2 clause of KEY) are not covered» keeps the any-degree clauses apart. (d) «bounds nothing polynomially (PHIK-DESCENT gives the
  exponential bound 2^(d+2) − 2d − 4, the certificates are lower bounds on potentials, not on T)»: true; PHIK-T's bound has the value of
  RESULTS R113's T-BOUND (packet §2 l. 113), which the line does not mention (a remark, not needed). No DEAD, no CONDITIONAL, no L43 item.
  «polynomially» once in the tail and «a polynomial in N + M» once in RISE-EQUIV (an equivalence, no polynomial bound claimed). Both
  referees MATCHED the tail.
- G-10, LEAD READINGS AND RULINGS (the C111 E-1 class): CLEAN. L-2 cites no Lead reading and no ruling (by script: «Lead reading» 0,
  «L4» 0, «D1» 0). The lane works under D14 / D18 / D20 (packet l. 2). The freeze brief (packet l. 2 «Lead brief BOX 182 (2026-11-06
  12:43Z)»; the freeze 2f4d96de is 12:57:51Z) and the fix-round relay (fixes l. 3 «Lead relay 15:09Z of fix round 1»; the lane commit
  0320ab9e is 15:09:11Z; LEAD-STATE 15:57Z) are messages; their exact minutes are not verifiable from the repository (D-1).
- G-11, STALE LANE TEXT (notes; nothing here lands as current). (i) Packet l. 38-40 and §1 l. 86-87 call P-IDEAL-ALIGN signed but not
  landed and re-prove its ALIGN (a), (c) and KP-MOVE (a) as KEY: P-IDEAL-ALIGN is RESULTS R113 since b5ca0d4d (2026-11-06T17:00:48Z),
  after the freeze and after both referees' rounds. KEY does not use R113 (both referees: REFEREE l. 24, REFEREE-2 l. 25); the body says
  in the present tense that R113 now also carries those facts and is not a premise. (ii) Packet l. 9-10 (CONJECTURES «stay OPEN») and §4
  l. 164-165: RISE-2D is a lane conjecture. L-RED's lane work after the freeze reports it false at d = 5, 6 (claude/l-red 3d6eca45,
  2026-11-06T13:10:04Z, R213; LEAD-STATE 13:45Z «RISE-2D DEAD at d 5/6»; notes/L-NEW.md l. 7): not landed, not refereed, not used. The
  line says only «not claimed», which stays true; the entry states no status of RISE-2D or MOVES-2D. (iii) Packet §6 l. 216-217's READING
  «T^R(d) = 4, 8, 13»: fixes RI-P2 (l. 12-13) labels the values; T^R(3) = 8 is RESULTS R112; not signed, not in the entry. (iv) Packet §2
  l. 113 «P-IDEAL-ALIGN's T-BOUND value»: now R113's T-BOUND. (v) REFEREE l. 24 «No unlanded premise.» and REFEREE-2 l. 25 «Unlanded
  P-IDEAL-ALIGN is not used»: true then; history.
- G-12, SHA1 PINS IN check.sh (the C110 F-1 / C116 G-3 class): present. experiments/new/check.sh block «P-IDEAL-RISE» (2f4d96de, l.
  927-934; at 0320ab9e the same lines with pin182 extended by the fixes 469cb291 and L-2 25170417) compares risecheck.py's output with the
  frozen risecheck.out, requires the zero counter line and four «CERTIFIED» lines, and pins the packet, L-1, the tool, its output, the
  four certificates, the fixes and L-2. Re-run: PASS (Re-runs (a)). It does not pin box150/check.py or box162/flipcheck.py, which the
  tool executes; a change to them would change the output and fail the block's diff.
- G-13, THE REFEREES' ROUNDS (note; state on file at this fill). L-1 (7e4273a9): REFEREE (33d148cd) every item SIGN, the certificates
  «SIGN as CERTIFIED machine items», L-1 required RI-L1 (l. 19, 111-116), optional RI-L2, RI-P1, RI-P2; REFEREE-2 (3b03d364) every item
  SIGN, «No gap. No REFUSE.» (l. 19), L-1 «**MATCHES after W-1 (required) and W-2 (required, DATA)**; P-1 optional» (l. 18). Fix round
  (fixes entry 1, 0320ab9e): RI-P1, RI-P2 notes, the W-2 counter check, L-2 = L-1 with R1-R4. Second round: REFEREE §C (807a59c4) «Fixes
  entry 1: CORRECT.» (l. 137), «Verdict: L-2 MATCHES. Every item stays SIGNED. Open items of mine: none.» (l. 152); REFEREE-2 Add. 1
  (6c88dc46) «**Fixes entry 1: CORRECT.**» (l. 121), «**Line L-2: MATCHES.**» (l. 126), «My SIGNs stand.» (l. 130). No addendum after
  these is on origin (the branch heads are 807a59c4 and 6c88dc46). No gap is open at either referee.
- G-14, THE FIXES FILE (note). Fixes entry 1 changes no statement, proof or DATA of the packet (l. 6-7); RI-P1 and RI-P2 are reading
  notes, the W-2 counter check re-reads the tool, R1-R4 change the line only. The source note names it (G-1).
- G-T, THE TAG (note; the R112 precedent). Two of the seven items are machine items signed by both referees; the ledger's labels are
  formalized and refereed-only (RESULTS l. 2), and R112 (a machine statement) carries «[refereed-only]». Kept; the machine character is
  in the line («by exact rational certificates checked by machine») and in the body (What rests on the machine; Honest limits (iii)).
- G-C, NOTE FOR THE LEAD (not part of R114): R113 is landed and states ALIGN and KP-MOVE; R114's KEY re-proves its (a), (c) parts and
  KP-MOVE's first half, and PHIK-T's bound equals R113's T-BOUND value by another route (a potential). L-RED's lane result on RISE-2D
  (G-11 (ii)) is lane work, outside this entry.
- CLEAN AT L-2 (the pre-check against CHECKER's recurring items, by script on 25170417):
  C106 E-1 (old line as current): L-2 is the current line; no L-3 exists (docs/new/P-IDEAL-RISE-line-L3.txt absent at 0320ab9e); L-1
  appears only in the line history.
  C113 E-1 (title «verbatim» after an insertion): no insertion; the title is byte-equal to prefix + L-2 + fill (Addendum (2)).
  C113 E-2 (trunk status that goes stale): the body has no trunk statement (header).
  C114 Add. 1 E-1 (UPDATE date): <DATE> placeholder.
  C115 E-1 (premise route): G-4.
  C110 F-1 / C116 G-3 (pins): G-12.
  C111 E-1 (stale Lead-reading statements): G-10.
  C116 G-2 (name clash): G-6, one body sentence.
  C117 E-1 / E-2 (scope; instance under-specified): G-2 (i) flagged; the feature classes inlined in Claims (f), the certificates named
  by path and sha1.
  C118 E-1 (stale status sentence): no «pending» in the entry; R111, R112 and R113 named as landed; no status of RISE-2D (G-11).
  C118 §3 / Erratum E-2 lesson (definitions diffed): G-2.
  C120 §5 / C121 E-1 / C122 E-2 / C124 E-1 / C125 E-1 (DATA unit, set and scope against the counter code): G-9; one clause flagged ((i)).
  C122 G-0 (parentheses): 72 / 72, depth never negative (G-1).
  C122 E-3 (source note): CLEAN (G-1), with G-M (c).
  C123 E-1 (lane label or packet name before the claims): none (G-1).
  C123 E-2 (stale referee state): G-13.
  C123 §3 (machine items stated exactly): G-M.
  «|»: 0 in L-2, 0 in the entry block, 0 in the UPDATE (by script, Addendum (3)).
- G-1, TITLE SHAPE AND SOURCE NOTE: CLEAN (my script). L-2 is one line, 4,091 characters, 4,218 bytes with the newline, 763 whitespace
  tokens, 72 «(» / 72 «)», depth never negative, final depth 0 (C122 G-0: met); 0 "|"; 0 guillemets; one « — », with its own date
  parenthesis «(2026-11-06)», «2026» once. It begins «In the IDEAL model of RESULTS R104»: no packet name and no lane label before the
  claims (C123 E-1: met); the packet name occurs only in the source note, as in R109-R113. Source note «(P-IDEAL-RISE,
  docs/new/P-IDEAL-RISE.md with its fixes entry 1, docs/new/P-IDEAL-RISE-fixes.md; L-NEW successor 56)»: the packet carries every proof
  (packet l. 6-7 «This packet carries every proof in full and is checked against this text only; no other file carries a proof of a
  statement below.»); fixes entry 1 l. 6-7 «No statement, proof or DATA of the packet changes. The line changes only (L-2 below).». Every
  proof-carrying file is named (C122 E-3: met); the machine files are in the DATA (G-M (c)). REFEREE §C l. 151 «The source note names
  the fixes file.». The title is "### R114 [refereed-only] " + L-2 + the fill ", CHECKER PASS (docs/checker/C127.md, checker PENDING)",
  nothing inserted.
(0) PLACEMENT. R114 goes DIRECTLY AFTER R113's block. docs/RESULTS.md at local trunk 8ac6757b (= origin trunk b5ca0d4d for this file)
has sha1 ec119661a26a07ebfe06c511966548c2b10f365d, 13,003 lines (wc -l), last changed by b5ca0d4d (R113's and Note E-3's landing).
«### R113» is l. 12152 (entry l. 12152-12392, l. 12393 blank); «**Erratum E-1**» is l. 12394; «**Erratum E-2**» is l. 12407; «**Note
E-3**» is l. 12435; «## Dead ends (kept;» is l. 12466. PROPOSED (R102's to R113's layout): insert R114's entry after l. 12393 (R113's
blank line), with one blank line after it, so the R-entries stay contiguous and the errata and Note E-3 follow them. "### R114" occurs 0
times in RESULTS and GAPS; «R114» 0 times. GAPS has sha1 a27514c3363bd52aa248039dd2db5203b9705abe, 23 lines, last changed by b5ca0d4d.
(1) TITLE. The title is the line file docs/new/P-IDEAL-RISE-line-L2.txt (l-new 0320ab9ecb965836c426a48eb26aa2fc35dff72a,
2026-11-06T15:09:11Z, the file's only commit, sha1 25170417891fec8d815cc23a30aa71c839369ada, 4,218 bytes with the newline; it is the
l-new head), verbatim: one line, no heading marker (it begins «In the IDEAL model of RESULTS R104»), no outer quotes, no final period.
NOTHING is stripped and NOTHING is inserted: the heading is the level-3 marker, then "R114 [refereed-only] ", then the file without its
newline, then the fill ", CHECKER PASS (docs/checker/C127.md, checker PENDING)" (as R90-R113). Built by script (fill114.py: assert the
sha1 25170417…, equality with the blob at 0320ab9e and at the l-new head, one line, no marker, one « (2026-11-06) — », no "|"; prepend,
append) and re-checked after writing this file (chk114.py): equal, byte for byte. Heading: 4,170 characters, 4,296 bytes; sha1 of
the heading line without its newline b36de18ecaea8862b4b455923d71251ef3447c0e; it is l. 424 and the only «### R» line of this file.
(2) LINE HISTORY: two lines. L-1 7e4273a97993e6e67fb8b7c81d6e215ceaa7bbbe (2f4d96de, frozen with the packet, the file's only commit;
3,914 bytes, 706 tokens, 68 «(» / 68 «)»): REFEREE required RI-L1, REFEREE-2 required W-1 (= RI-L1) and W-2 (G-13). L-2 25170417
(0320ab9e; 4,218 bytes, 763 tokens, 72 / 72): fixes entry 1 lists four replacements R1-R4 (fixes l. 22-31) and their word diff (l.
32-42); my byte test (wdiff114.py: R1-R4 parsed from fixes l. 22-31, wrapped lines joined by one space, the last two outermost
guillemet quotes of each bullet as old / new; each old string once in the current text when applied in order, each new string once in
L-2) gives L-1 with R1-R4 = L-2 byte for byte (True); my token diff (difflib on whitespace tokens) finds 6 non-equal hunks (3 tokens
out, 60 in), all inside R1-R4, the same six as fixes l. 34-42. Both referees byte-tested L-2 the same way (REFEREE §C l. 146 «L-1 +
R1..R4, parsed from the fixes file, each old string once, gives sha1 25170417…, 4,218 bytes: EQUAL to L-2.»; REFEREE-2 Add. 1 l.
127-128 «Applying them gives a string byte-identical to L-2 (4,218 B).»). R1 binds the certificates' range (RI-L1 = W-1); R2 names
the RISE-EQUIV counters and the uncounted identity (W-2); R3 lengthens the two truncations (P-1 = RI-L2); R4 names the fixes file. No
hunk changes a claim. So the title is L-2, and L-1 is history.
(3) THE LINE AT BOTH REFEREES. REFEREE successor 24, docs/referee/R-P-IDEAL-RISE.md: report 33d148cd (2026-11-06T14:13:52Z, new file,
129 lines, sha1 93b7d6572fe639b46a8e9b00f079b9b3974b116d), §C 807a59c4 (2026-11-06T15:55:20Z, 152 lines, sha1
20adb3aaffb87869772293ec7a86858b588e2b82): «Verdict: L-2 MATCHES.» (l. 152). REFEREE-2 successor 28, docs/referee-2/R2-P-IDEAL-RISE.md:
report 3b03d364 (2026-11-06T13:57:02Z, new file, 115 lines, sha1 6838e657a0f919dbf7612d259d7378ef049ffb9c), Addendum 1 6c88dc46
(2026-11-06T15:55:22Z, 130 lines, sha1 052764c8257c07a3071d8aa64103b97e4ee84e70): «**Line L-2: MATCHES.**» (l. 126). Both MATCH L-2.
(4) CLAIMS SIGNED = the items below, each SIGN in BOTH referees' verdict tables (REFEREE "## 0. Verdicts" l. 10-19; REFEREE-2 "##
Verdicts" l. 10-19), unchanged in their second rounds (REFEREE §C l. 152; REFEREE-2 Add. 1 l. 130); the cells are the reports' words:
(a) Lemma KEY (a), (b), (c) (packet §1 l. 75-87): REFEREE l. 13 «SIGN»; REFEREE-2 l. 13 «**SIGN** (Opus 5.5, D12)». (b) Theorem
PHIK-DESCENT and Corollary PHIK-T (§2 l. 89-114): REFEREE l. 14 «SIGN»; REFEREE-2 l. 14 the same words. (c) Theorem OPT-K (§3 l.
116-147): REFEREE l. 15 «SIGN»; REFEREE-2 l. 15 the same words. (d) Lemma RISE-EQUIV (a)-(c) and (e) Lemma MOVE-RISE with Corollary
MOVE-RISE-R (§4 l. 149-165): REFEREE l. 16 «SIGN» (one row); REFEREE-2 l. 16 the same words (one row). (f) Certificate item C-PHX3 and
(g) C-PBG (§5 l. 167-197): REFEREE l. 17 «SIGN as CERTIFIED machine items: all four certificates RE-VERIFIED independently (§3)»;
REFEREE-2 l. 17 «**SIGN as machine-certified** (Opus 5.5, D12): all 4 certificates re-verified by my own independent code in exact
arithmetic». REFEREE-2 l. 19 «No gap. No REFUSE.»; REFEREE §C l. 152 «Open items of mine: none.». No gap is open at either referee.
Clause checks (L-2 against the packet; G-2): KEY = l. 76-79; PHIK-DESCENT = l. 91-93; OPT-K = l. 117-121; RISE-EQUIV = l. 151-154;
MOVE-RISE = l. 160, 163; the certificate clause = l. 180-184. Nothing in L-2 is wider than signed, except the level-0 case of KEY's
third part (G-2 (i), true by §0's key definition; flagged).
Signed by both, NOT stated by L-2 as separate items: KEY (a)'s «Hence» sentence; the per-level facts and the Claim of PHIK-DESCENT's
proof; the forcing-step Lemma of OPT-K (in the line only as the parenthesis on the forcing genomes); the middle terms of PHIK-T and
RISE-EQUIV (c); the certificate definition and inequality of §5 (in the body). Not signed, so NOT landed: packet §6 (DATA, machine
checks, EXCLUDED, READING, TARGET diff; «DATA / READING (not to sign)», l. 20), §3's READING (l. 146-147), the earlier DATA of boxes
179-181 (l. 211-212), the PHX / PHXV / PHXVD / PHXVDBG lower bounds at d ≥ 4 (l. 213), the READING on C-PBG (l. 216-217).
(5) OTHER TEXTS THE ENTRY DEPENDS ON: RESULTS R104's definition of the IDEAL model (title l. 9864; no R104 theorem); RESULTS R105's
ENC, MONO, XI-NEW and RISE (title l. 10155); RESULTS R110's definition of 𝓛^R_d (title l. 11323); RESULTS R111's CASCADE (title l.
11598). Nothing else for a signed statement. The certificate items rest also on the machine check (What rests on the machine). The
sources docs/new/N5-LPOT-box179.md, N5-RISES-box180.md and N5-RISEPROOF-box181.md (packet l. 5-6) are history.
(6) PREMISE LABELS (stale-label test; RESULTS and GAPS at b5ca0d4d's version). RESULTS labels in L-2 (by script): «R104» 3 («RESULTS
R104», «R104's definition», «theorem of R104»); «R105» 2 («RESULTS R105's ENC, MONO, XI-NEW and RISE only», «(R105 ENC)»); «R110» 1;
«R111» 1. Each exists: R104 l. 9864, R105 l. 10155, R110 l. 11323, R111 l. 11598. Erratum E-2 governs R105's KEYFLIP, CHAIN-BACK and
TOP-MONO, none used. No Lead reading and no other RESULTS label is cited. G-N5-TIME open (GAPS l. 11).
(7) SYMBOL TEST: G-3. Every symbol of L-2 is R104's (IDEAL model, Ξ-graph, acyclic, mover, level, option, key, gate index, state, step,
run, exit X, N, M), R105's (ENC, the integer value), R110's (𝓛^R_d), bound in the line (T, Mv_t, moves(x), KP_s(x), k_s(x), w_l, Φ_K,
v_s, cv_s, R(x, k) and the clause variables), a class named with «of the packet» (PHX, PBG), a file with its path (risecheck.py, the
certificates, the packet, the fixes), or a named conjecture «not claimed» (RISE-2D, MOVES-2D). Agreeing tests: REFEREE l. 103-104;
REFEREE-2 l. 101-103.
(8) FIXES AND STATUS NOTES (docs/new/P-IDEAL-RISE-fixes.md, L-NEW successor 56, append-only, one entry, one commit 0320ab9e): sha1
469cb2915b58e716ed8b7c692b12fa70e6c3f245, 42 lines, 4,070 bytes. Header l. 1. Entry 1 (l. 3-42): reports answered (l. 4-7); RI-P1 (l.
8-11); RI-P2 (l. 12-13); W-2 counter check (l. 14-18); line L-2 with R1-R4 (l. 19-31) and the word diff (l. 32-42). Verdicts: REFEREE
§C l. 137-152; REFEREE-2 Add. 1 l. 121-130.
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-2 states no CONJECTURE as claimed and kills nothing («RISE-2D», «MOVES-2D», «PHIK»,
«P-IDEAL-RISE» occur 0 times in GAPS). A line-11 UPDATE is proposed at the end, to go AFTER R113's UPDATE (GAPS at b5ca0d4d: the last
UPDATE on l. 11 is R113's «UPDATE 2026-11-06 17:00Z: RESULTS R113 (P-IDEAL-ALIGN; CHECKER C125 bd7cb5e4) [refereed-only] LANDED: …»,
ending «G-N5-TIME stays open.» before the row's closing « |»; l. 11 holds 76 "|" and 48 «UPDATE 2026-»), as a pure insertion with one
separating space. BUILT FROM L-2 (scratch upd114.py = upd113b.py l. 1-298 unchanged (controls R97-R112; its l. 299, the state assertion
that R112's UPDATE is the last on l. 11, is dropped because R113's now follows it), plus R113's control, plus R114). CONTROLS (same
script, same run, rc 0): R97's to R113's LANDED UPDATEs (GAPS l. 11 at b5ca0d4d) rebuilt from their lines byte for byte (True ×17;
R113's from P-IDEAL-ALIGN L-3 at e0d49b59 through upd113b.py's R113 call with head «UPDATE 2026-11-06 17:00Z: RESULTS R113
(P-IDEAL-ALIGN; CHECKER C125 bd7cb5e4) [refereed-only] », 3,457 bytes filled, also equal to R113-draft l. 649 and to
r113/fill2/upd113L3.txt with <DATE> 2026-11-06, <HH:MM> 17:00, <checker> bd7cb5e4). R114: the R111 procedure (sentinel_build111 of
upd111.py, unchanged, default drops) on L-2 with the certificate clause cut and put back behind «(MOVE-RISE)» (G-U): 5 labels, each
found once after the start «and M the number of options: », in order, moved behind their clauses; « (2026-11-06) — » → «: »; the DATA
parenthesis before the source parenthesis opened as «; DATA, …» (R111's «(DATA, » opening); «; G-N5-TIME stays OPEN» and «; not M3,
not a step-4 pass, not a TARGET.md claim» dropped; the source parenthesis kept; «. G-N5-TIME stays open.» appended. Labels with inner
«; »: KEY's clause has one («… gate indices of option j; at any degree elsewhere, …»); build() cuts at the last «; » before the next
label, so KEY's clause stays whole (the direct build agrees). L-2 holds no "|", so no replacement list. Checked by script: one line, 0
"|", one «<DATE>», one «<HH:MM>», one «<checker>», 4,251 bytes, 4,127 characters, 762 tokens, 71 «(» / 71 «)», balanced; «2026-11-06» 0
times; token multiset diff against L-2 = the head, the five moved labels, «(DATA,» opened, the two dropped scope sentences, « — » and
the final sentence (upd114.out). Head «UPDATE <DATE> <HH:MM>Z: RESULTS R114 (P-IDEAL-RISE; CHECKER C127 <checker>) [refereed-only] »
(«P-IDEAL-RISE» 0 times in GAPS); <DATE> = the landing date.
(10) DATA of record = packet §6 (l. 199-220), NOT signed; L-2's DATA parenthesis states its counts per statement, with the flag of G-9
(i). Re-run at this fill: Re-runs (a)-(c) in the header (PASS; my split; both referees' certificate checkers).
- PASS line: «P-IDEAL-RISE: risecheck 0 violations, 4 certificates CERTIFIED (output = frozen risecheck.out); pins packet 573ef117, line
  L-1 7e4273a9, tool 404df6de, output 3685b69b, certificates bf65a4e6 f878699f 7f3d88c3 71fb1683, fixes 469cb291, line L-2 25170417:
  PASS».
- risecheck raw (byte-equal to risecheck.out, cmp): four CERT lines (PHX d 3 «rows 73 (dec 61 lo 7 hi 5) bad 0 inconsistent False
  negative 0 free 0 bound 22.000000 (= 22) CERTIFIED»; PBG d 2 rows 38, bound 8; PBG d 3 rows 77, bound 18.859681 = p/q with a 67-digit
  numerator; PBG d 4 rows 108, bound 35.553557 = p/q with a 122-digit numerator), «SCOPE corpus_files 201 random 200 phik_steps 14384
  phik_tight 1772 optk_transitions 72 rise_runs 401 rise_moves 1968», «PHIK 0 OPTK 0 RISE_A 0 RISE_B 0 RISE_C 0 MOVERISE 0 CERT 0».
  Equal to both referees' runs of the block at 2f4d96de (REFEREE §4 l. 93; REFEREE-2 l. 82).
NOT re-run: the referees' rise probes (docs/referee/scratch/rise_probe.py; docs/referee-2/R2-P-IDEAL-RISE/r2rise.py); I read their
committed logs (rise_logs/probe.txt; r2rise_seed182.out), whose counts equal the reports (REFEREE §4 l. 84-90; REFEREE-2 l. 70-76).
check.sh's other blocks and scripts/verify.sh: not run.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 packet l. 2 «Lead brief BOX 182 (2026-11-06 12:43Z)» and fixes l. 3
«Lead relay 15:09Z of fix round 1» against the lane commits 2f4d96de (12:57:51Z) and 0320ab9e (15:09:11Z), the relay in the commit's
minute; stamps of messages, not verifiable from the repository. D-2 REFEREE §1 l. 22 «(1 hit)» for R110's 𝓛^R_d wording: at c8fefddb
it had 2 hits (R110's title and R112's body quote), 1 with R110's context (G-4). D-3 the referees' corpora are their own: REFEREE §4 l.
84 «186 corpus 𝓛^R genomes (N ≤ 10)», REFEREE-2 l. 80 «the 110 𝓛^R corpus runs my loader reads»; not the lane's 201 files. D-4 REFEREE
l. 90-92: a first probe run reported 10 «violations», all on odd-N files outside 𝓛^R_d; the probe was fixed and the artifact recorded.
D-5 independence timing: REFEREE-2's report (13:57:02Z, stamped «13:56Z (date -u)») precedes REFEREE's (14:13:52Z) by 16 min 50 s; each
states it did not read the other's directory (REFEREE l. 2-3; REFEREE-2 l. 2-3); R1 is «REFEREE-2's form, copied from
R2-P-IDEAL-RISE.md» (fixes l. 22) and REFEREE knew REFEREE-2's items through the entry only (§C l. 136); the two second rounds were
pushed 2 s apart (15:55:20Z, 15:55:22Z). D-6 packet l. 190-191 vs the tool's acyclic() on «xorder» genomes (G-M (b)). D-7 packet l. 24
«used in §4 only» for R105's four items, while §5's PV / ic / io are defined through ENC integers (RI-P1; fixes l. 8-11; REFEREE's
set-order re-check reproduces the bounds without ENC).
(12) Excluded: packet §6 (DATA counts, machine checks, pins, EXCLUDED, READING, TARGET diff); §3's READING; CONJECTURES RISE-2D and
MOVES-2D; the PHX / PHXV / PHXVD / PHXVDBG lower bounds at d ≥ 4; the obstruction READINGs and the «O(1) flips between rises» DEAD of
box 181 (DATA only, l. 213-215); boxes 183- (later lane work). Not part of this entry.
(13) Commits: lane (claude/l-new): 2f4d96de (2026-11-06T12:57:51Z; freeze: packet 573ef117 (220 lines), L-1 7e4273a9, risecheck.py,
risecheck.out, the four certificates, check.sh block P-IDEAL-RISE) → 0320ab9e (2026-11-06T15:09:11Z; fixes entry 1, 42 lines; L-2;
pin182 extended); the commits between them (eeafb12e, 95a32e19, 8ccb3af0: boxes 183-184) change no P-IDEAL-RISE file and nothing under
box150-box182. REFEREE (claude/referee): 33d148cd (report; scratch/cert_check.py 126 lines, scratch/rise_probe.py 133 lines,
rise_logs/) → 807a59c4 (§C, +23 lines). REFEREE-2 (claude/referee-2): 3b03d364 (report; R2-P-IDEAL-RISE/r2cert.py 136 lines, r2cert.out,
r2rise.py 88 lines, r2rise_seed182.out) → 6c88dc46 (Addendum 1, +15 lines). CHECKER: docs/checker/ ends at C126 (bbc4a897). Trunk: see
the header.
(14) Placement: see (0). DEAD-ENDS ROWS: NONE (not drafted). R114 kills nothing.

### R114 [refereed-only] In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of R104 used; RESULTS R105's ENC, MONO, XI-NEW and RISE only; RESULTS R110's definition of 𝓛^R_d only; and RESULTS R111's CASCADE only), on acyclic Ξ-graphs, with T the number of steps of a run, Mv_t the movers of step t, moves(x) the number of steps t with x ∈ Mv_t, KP_s(x) the option of x with the least key under s, k_s(x) := [s(x) ≠ KP_s(x)], on 𝓛^R_d w_l := 2^(d−l) − 1 and Φ_K(s) := Σ_x w_lev(x) k_s(x), v_s(x, k) the integer value of option (x, k) under s (R105 ENC), cv_s(z) := v_s(z, s(z)), R(x, k) the number of steps t with v_(s_t)(x, k) > v_(s_(t−1))(x, k) and M the number of options: (KEY) on 𝓛^R_d, KP_s of a level-0 mover does not depend on s and both movers of a level l ≥ 1 have KP_s equal to the option index k for which mover 2(l − 1) + k has the smaller current key, and two movers of one level on the same option j have the order of their keys given by their gate indices of option j; at any degree elsewhere, a mover of degree 2 that moves at step t moves to KP_(s_t) and was not on it before; (PHIK-DESCENT) on 𝓛^R_d, Φ_K(s_t) ≤ Φ_K(s_(t−1)) − 1 at every step, so T ≤ Φ_K(s_0) ≤ 2^(d+2) − 2d − 4 and T = 0 from a start where every mover is on KP; (OPT-K) for d ≥ 1, if a + Σ_x w_x k_s(x), with real a and w_x not depending on the genome, falls by at least 1 at every step of every genome of 𝓛^R_d from every state, then w_x ≥ 2^(d−lev(x)) − 1 for every x and its range on every genome of 𝓛^R_d is at least 2^(d+2) − 2d − 4, with equality for Φ_K (forcing genomes with every Ξ-target the exit X, in which every mover moves at most once); (RISE-EQUIV) at any degree, every option value is non-decreasing along a run, R(x, k) is the number of rises of cv of the Ξ-target of (x, k) (0 if it is X), R(x, k) ≤ T, and T ≤ 1 + Σ_(x,k) R(x, k) ≤ 1 + M max_(x,k) R(x, k), so on any family max_(x,k) R(x, k) is bounded by a polynomial in N + M iff T is; (MOVE-RISE) at any degree, a move of z at step t gives cv_(s_t)(z) > cv_(s_(t−1))(z), so R(x, k) ≥ moves(z) when the Ξ-target of (x, k) is the mover z; and, by exact rational certificates checked by machine, for the feature classes PHX (key, Ξ-unhappiness and pair-state bits, Ξ-height counts, cross-level products) and PBG (key, Ξ-unhappiness and pair-state bits, value budgets and value gaps from the ENC integers of the maximal Ξ-paths) of the packet, every potential linear in the features with weights not depending on the genome that falls by at least 1 at every step of every genome of 𝓛^R_d has range (supremum minus infimum over all genomes of 𝓛^R_d and their states) at least 22 for PHX at d = 3 (so exactly 22, attained by Φ_K) and at least 8, 18.8596… and 35.5535… for PBG at d = 2, 3, 4 (2026-11-06) — a POTENTIAL / EQUIVALENCE statement inside the IDEAL model; bounds nothing polynomially (PHIK-DESCENT gives the exponential bound 2^(d+2) − 2d − 4, the certificates are lower bounds on potentials, not on T); the conjectures RISE-2D (every option of a run on 𝓛^R_d rises at most 2d times) and MOVES-2D are not claimed; Ξ-cyclic genomes and genomes outside 𝓛^R_d (outside RISE-EQUIV, MOVE-RISE and the degree-2 clause of KEY) are not covered; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (DATA, experiments/new/box182/risecheck.py: PHIK-DESCENT 0 violations on 14,384 steps (every state of 200 random 𝓛^R_d genomes, d 1-4, and the stored-start runs of the 201 in-tree 𝓛^R_d genome files of experiments/new/box150 to box181), equality on 1,772; the OPT-K forcing step and both extreme states on the 72 forcing genomes for d = 1-8, 0 failures; RISE-EQUIV (non-decreasing values, R(x, k) ≤ T and T ≤ 1 + #{t ≤ T − 1 with a rise} ≤ 1 + Σ R) and MOVE-RISE 0 violations on 401 stored-start runs with 1,968 moves; the identity of R(x, k) with the rises of cv of the Ξ-target and MOVE-RISE's R(x, k) ≥ moves(z): no separate DATA; the four certificates experiments/new/box182/cert/*.json re-checked in exact arithmetic) (P-IDEAL-RISE, docs/new/P-IDEAL-RISE.md with its fixes entry 1, docs/new/P-IDEAL-RISE-fixes.md; L-NEW successor 56), CHECKER PASS (docs/checker/C127.md, checker PENDING)
- Object (L-NEW successor 56, Opus 5.5, D14 / D18 / D20, box 182; frozen, unchanged during review): packet P-IDEAL-RISE,
  docs/new/P-IDEAL-RISE.md, sha1 573ef1171eec0f48aad974d221050681fc09ecc4, 220 lines (l-new freeze 2f4d96de, 2026-11-06T12:57:51Z;
  identical at 0320ab9e and at 0548afaa). Both referees measured the sha1 (REFEREE l. 5 «docs/new/P-IDEAL-RISE.md: sha1
  573ef1171eec0f48aad974d221050681fc09ecc4, 220 lines;»; REFEREE-2 l. 6 «docs/new/P-IDEAL-RISE.md sha1
  573ef1171eec0f48aad974d221050681fc09ecc4, 220 lines;»). Labels (l. 7-8): «Labels: PROVED (L-NEW 56, unrefereed) / CERTIFIED
  (machine, exact rational arithmetic; not a hand proof) / DATA / READING (not to sign).» To sign (table l. 13-20): §1 KEY, §2
  PHIK-DESCENT and PHIK-T, §3 OPT-K, §4 RISE-EQUIV, MOVE-RISE and MOVE-RISE-R (PROVED); §5 C-PHX3 and C-PBG (CERTIFIED (machine)); §6
  «DATA / READING (not to sign)». Sections: premises (l. 22-42), §0 the model and notation (l. 44-73), §1 (l. 75-87), §2 (l. 89-114), §3
  (l. 116-147), §4 (l. 149-165), §5 (l. 167-197), §6 (l. 199-220). Sources (l. 5-6): docs/new/N5-LPOT-box179.md, N5-RISES-box180.md,
  N5-RISEPROOF-box181.md; «This packet carries every proof in full and is checked against this text only; no other file carries a proof
  of a statement below.» (l. 6-7).
  Fixes: docs/new/P-IDEAL-RISE-fixes.md, append-only, two entries. Entry 1 (L-NEW successor 56, 0320ab9e; 42 lines, sha1
  469cb2915b58e716ed8b7c692b12fa70e6c3f245): RI-P1 and RI-P2 reading notes, the W-2 counter check of risecheck.py, line L-2. Entry 1:
  «No statement, proof or DATA of the packet changes. The line changes only (L-2 below).» (l. 6-7). Entry 2 (L-NEW successor 57,
  0548afaa, 2026-11-06T18:56:55Z; l. 44-59; the file then 59 lines, 5,734 bytes, sha1 d8046a92f9081c01f488fbcdf51ba13843a9bcaf, its l.
  1-42 = entry 1's file, by script): CHECKER C127 E-1 answered by a counter check and line L-3; «No statement, proof or other DATA
  changes; the packet and entry 1 stay as they are.» (l. 48).
  The RESULTS line is L-3, 4a553a296533b86de8bb3fce20a90ff0e13393e9 (docs/new/P-IDEAL-RISE-line-L3.txt, l-new 0548afaa,
  2026-11-06T18:56:55Z, the file's only commit; 4,255 bytes). The title is L-3 verbatim, with nothing inserted (its date parenthesis
  «(2026-11-06)» and its source note are the line's own; the source note names the packet, which carries every proof, and the fixes
  file, which carries none; the machine premise's files are named in the line's DATA parenthesis). L-3's parentheses balance (74 «(» /
  74 «)»). Line history: L-1 (7e4273a9, 2f4d96de, frozen with the packet); L-2 (25170417, 0320ab9e, fixes entry 1: L-1 with exactly
  four replacements R1-R4, fixes l. 22-31: the certificates' «range» bound to «(supremum minus infimum over all genomes of 𝓛^R_d and
  their states)» (RI-L1 = W-1), the RISE-EQUIV DATA named by its counters with the identity of R(x, k) «no separate DATA» (W-2), the
  truncations «18.8596…» and «35.5535…» (P-1 = RI-L2), the fixes file named in the source note; L-1 with R1-R4 equals L-2 byte for byte,
  by my script); L-3 (4a553a29, 0548afaa, fixes entry 2: L-2 with exactly one replacement R5, fixes l. 55-56 = CHECKER C127 §4 l.
  92-93 (E-1), «the identity of R(x, k) with the rises of cv of the Ξ-target: no separate DATA» → «the identity of R(x, k) with the
  rises of cv of the Ξ-target and MOVE-RISE's R(x, k) ≥ moves(z): no separate DATA»: the second half of the MOVE-RISE clause (Corollary
  MOVE-RISE-R), which no counter of risecheck.py checks, joins the «no separate DATA» list; L-2 with R5 equals L-3 byte for byte, by
  my script, one token hunk). L-2 MATCHES at both referees, each after its own byte test: REFEREE (807a59c4) §C l. 146 «L-1 + R1..R4, parsed from
  the fixes file, each old string once, gives sha1 25170417…, 4,218 bytes: EQUAL to L-2.», l. 152 «Verdict: L-2 MATCHES.»; REFEREE-2
  (6c88dc46) Addendum 1 l. 126 «**Line L-2: MATCHES.**», l. 127-128 «Applying them gives a string byte-identical to L-2 (4,218 B).».
  L-3 MATCHES at both referees, each after its own byte test against C127 §4: REFEREE (3489d797) §C add. 1 l. 158-159 «with C127 §4's
  one replacement (claude/checker 5793c1e2), parsed from the CHECKER file», «It gives sha1 4a553a29…, 4,255 bytes: EQUAL to L-3.», l.
  166 «Verdict: L-3 MATCHES.»; REFEREE-2 (bdbf0dde) Addendum 2 l. 140 «**Line L-3: MATCHES.**», l. 141 «The pushed L-3 has the same
  sha1.».
  Both diffed every definition of L-1 against packet §0 (REFEREE l. 103 «Definitions diffed against §0: KP_s, k_s, w_l, Φ_K, v_s, cv_s,
  R(x, k), M and moves(x) (E2c) all MATCH.»; REFEREE-2 l. 101-102); L-2 changes no definition and no claim (R1 binds a range that §5
  already states joint; R2 lies inside the DATA parenthesis; R3 lengthens two truncated values, exact truncations of the tool's p/q; R4
  is the source note); L-3 changes none either (R5 lies inside the DATA parenthesis and only adds an item to its «no separate DATA»
  list; C127 §2 l. 18-19 «No statement, definition or premise changes.»).
- Claims signed (REFEREE successor 24 «(Opus 5.5, D15)», report 33d148cd, §C 807a59c4, §C add. 1 3489d797; REFEREE-2 successor 28 «(Opus 5.5,
  D12/D20)», report 3b03d364, Addendum 1 6c88dc46, Addendum 2 bdbf0dde). Items (a)-(e) are SIGN and items (f), (g) SIGN as machine items in both verdict tables
  (REFEREE "## 0. Verdicts" l. 10-19 of R-P-IDEAL-RISE.md; REFEREE-2 "## Verdicts" l. 10-19 of R2-P-IDEAL-RISE.md) and stand in both
  second rounds (REFEREE §C l. 152 «Every item stays SIGNED. Open items of mine: none.»; REFEREE-2 Add. 1 l. 130 «My SIGNs stand.»)
  and in both third rounds (REFEREE §C add. 1 l. 166 «All items stay SIGNED.»; REFEREE-2 Addendum 2 l. 141 «My SIGNs stand.»).
  REFEREE-2 l. 19 «No gap. No REFUSE.». Every item is about R104's IDEAL model on acyclic Ξ-graphs; (a)'s first and third parts, (b),
  (c), (f) and (g) on 𝓛^R_d (RESULTS R110's 2-wide degree-2 ladders: movers 2l and 2l + 1 on level l, all of degree 2, no other movers,
  option k of a mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k; levels 0, …, d − 1); (a)'s second part for a mover of degree 2
  of any acyclic genome; (d), (e) at any degree and width. Notation (packet §0 l. 57-73): T the number of steps; Mv_t := {x : s_t(x) ≠
  s_(t−1)(x)}; moves(x) := #{t ∈ [1, T] : x ∈ Mv_t} (the binder of Erratum E-2 (E2c)); KP_s(x) the option k of x with the least
  key_s(x, k) (unique by (F1)); k_s(x) := [s(x) ≠ KP_s(x)] (x key-misaligned at s); for u ≠ w of one level ord_s(u, w) := [key_s(u, s(u))
  < key_s(w, s(w))]; on 𝓛^R_d ord_l(s) := ord_s(2l, 2l + 1), and for 1 ≤ l ≤ d − 1 c_l(s) := 0 if ord_(l−1)(s) is true, else 1, γ_l(j)
  := [g(2l, j) < g(2l + 1, j)]; v_s(x, k) := Σ over the β's of Ξ_s(x, k) of ±2^rank (+ for even parity), cv_s(x) := v_s(x, s(x)); R(x,
  k) := #{t ∈ [1, T] : v_(s_t)(x, k) > v_(s_(t−1))(x, k)}; M the number of options; w_l := 2^(d−l) − 1 for 0 ≤ l ≤ d − 1 (w_d := 0 in
  the proof), Φ_K(s) := Σ_x w_lev(x) k_s(x); step(s) := s_1 of the run started at s_0 = s. (F1) the keys of two distinct options of one
  level differ; (F2) if x ∈ Mv_t, then s_t(x) is available and strictly Ξ-better under s_(t−1), and at degree 2 s_(t−1)(x) is x's other
  option; (F3) key_s(x, k) depends only on the options under s of movers of level < lev(x) (l. 59-63).
  (a) Lemma KEY (§1 l. 75-87): «(a) Hypotheses: G ∈ 𝓛^R_d, s any state. For y ∈ {0, 1}, KP_s(y) is the same option for every s. For 1
      ≤ l ≤ d − 1 and x ∈ {2l, 2l + 1}, KP_s(x) = c_l(s).»; «(b) Hypotheses: G IDEAL-ACYC; x a mover with deg(x) = 2; any run. If x ∈
      Mv_t, then s_t(x) = KP_(s_t)(x) and s_(t−1)(x) ≠ KP_(s_t)(x).»; (c) «If s(2l) = s(2l + 1) = j and l ≥ 1, then ord_l(s) = γ_l(j).».
      In the line these are, in order, KEY's three parts; its third part is worded for «two movers of one level», which at level 0 holds
      by the definition of keys (§0 l. 54, keys of level-0 options are their gates; KEY (a)'s proof l. 80). Proof: R110's wiring makes
      key_s(x, k) the key of the current option of mover 2l − 2 + k followed by g(x, k); the two prefixes are keys of options of two
      distinct movers of level l − 1, unequal by (F1), and decide; (b) by (F2) both options are available and the step takes the one with
      the least key under s_t; (c) equal options give equal prefixes and the gates decide. KEY re-proves ALIGN (a), (c) and KP-MOVE (a) of
      RESULTS R113, which now also carries them; R113 is not a premise (packet l. 38-40). Cells: REFEREE l. 13 «SIGN»; REFEREE-2 l. 13
      «**SIGN** (Opus 5.5, D12)».
  (b) Theorem PHIK-DESCENT and Corollary PHIK-T (§2 l. 89-114) [G ∈ 𝓛^R_d (d ≥ 1); any run; t ∈ [1, T]]: «Theorem PHIK-DESCENT. Φ_K(s′)
      ≤ Φ_K(s) − 1.» (s := s_(t−1), s′ := s_t); «Corollary PHIK-T. Every run from s_0 has T ≤ Φ_K(s_0) ≤ Σ_x w_lev(x) = 2 Σ_(l=0..d−1)
      (2^(d−l) − 1) = 2^(d+2) − 2d − 4. In particular a start with k_(s_0)(x) = 0 for every x has T = 0.». Proof: with f_l the flip
      indicator of the level-l pair, m_l its number of movers and Δ_l the weighted change of its k bits, KEY (a), (b) give the per-level
      facts (a non-mover's k toggles iff the pair below flips; a mover lands aligned) and CASCADE gives f_l = 1 ⇒ m_l ≥ 1 or f_(l−1) = 1;
      five cases bound Δ_l, and a downward induction with S_(l+1) ≤ 2w_(l+1) = w_l − 1 gives S_l ≤ 0, ≤ −1 or ≤ 2w_l by case; at the least
      moving level f = 0 and m ≥ 1, so S_0 ≤ −1. PHIK-T: Φ_K ≥ 0. The bound is the value of R113's T-BOUND, reached here by one potential
      (§2 l. 113). Cells: REFEREE l. 14 «SIGN»; REFEREE-2 l. 14 «**SIGN** (Opus 5.5, D12)».
  (c) Theorem OPT-K (§3 l. 116-147) [d ≥ 1; real a and w_x (x = 0, …, 2d − 1) independent of the genome; Φ(G, s) := a + Σ_x w_x k_s(x)
      with Φ(G, s) − Φ(G, step(s)) ≥ 1 for every G ∈ 𝓛^R_d and every state s with step(s) defined]: «Then w_x ≥ 2^(d−lev(x)) − 1 for every
      x, and for every G ∈ 𝓛^R_d, max_s Φ(G, s) − min_s Φ(G, s) ≥ Σ_x w_x ≥ 2^(d+2) − 2d − 4.»; Φ_K attains equality in both. Proof: the
      forcing genome τ(l, p) (every Ξ-target X, every parity even, ranks making s(x) Ξ-better at every x ≠ p and 1 − s(p) better at p,
      gates forcing the level-l pair to flip) has Mv_1 = {p}, k(p) 1 → 0, both level-(l + 1) movers 0 → 1 and no other k change (the
      forcing-step Lemma, by (F3), KEY and CASCADE); so w_p − w_(2l+2) − w_(2l+3) ≥ 1 and w_p ≥ 1 at the top, hence W_l ≥ 2W_(l+1) + 1;
      the all-1 and all-0 k-states exist in every G (built level by level by (F3)). In τ(l, p) every mover moves at most once (each has
      every Ξ-target X: after a move it is on its Ξ-better option; §3 l. 144-145). Cells: REFEREE l. 15 «SIGN»; REFEREE-2 l. 15
      «**SIGN** (Opus 5.5, D12)».
  (d) Lemma RISE-EQUIV (§4 l. 149-159; premises R105 ENC, MONO, XI-NEW, RISE) [IDEAL-ACYC, any degree, any width; any run]: «(a) For
      every option (x, k) and t ∈ [1, T], v_(s_t)(x, k) ≥ v_(s_(t−1))(x, k); and R(x, k) = the number of rises of cv(xt(x, k)) if xt(x,
      k) is a mover, R(x, k) = 0 if it is X. (b) R(x, k) ≤ T. (c) T ≤ 1 + #{t ∈ [1, T − 1] : some option value rises at step t} ≤ 1 +
      Σ_(x,k) R(x, k). Hence T ≤ 1 + M · max_(x,k) R(x, k), and on any family of genomes and runs, max_(x,k) R(x, k) is bounded by a
      polynomial in N + M iff T is.». Proof: (a) ENC writes v_s(x, k) as ε(x, k) plus the current value of the Ξ-target, and MONO; (b) a
      value changes at most once per step; (c) every step t ∈ [2, T] has a least-level mover, which by XI-NEW and RISE moves to an option
      whose value rose strictly at step t − 1. Cells: REFEREE l. 16 «SIGN»; REFEREE-2 l. 16 «**SIGN** (Opus 5.5, D12)».
  (e) Lemma MOVE-RISE and Corollary MOVE-RISE-R (§4 l. 160-165) [the same hypotheses]: «MOVE-RISE. If z ∈ Mv_t, then cv_(s_t)(z) >
      cv_(s_(t−1))(z).»; «Corollary MOVE-RISE-R. If xt(x, k) = z is a mover, then R(x, k) ≥ moves(z).». Proof: by (F2) and ENC the new
      option was strictly better under s_(t−1), and by RISE-EQUIV (a) its value did not fall at step t; the distinct steps moving z are
      distinct rises of cv(z), and R(x, k) counts the rises of cv(z). Cells: the RISE-EQUIV row of both tables (REFEREE l. 16; REFEREE-2
      l. 16).
  (f) Certificate item C-PHX3 and (g) C-PBG (§5 l. 167-197; CERTIFIED: machine, exact rational arithmetic; not hand proofs) [G ∈ 𝓛^R_d,
      d = 3 for (f), d = 2, 3, 4 for (g)]. The feature classes, verbatim (l. 168-179), «for G ∈ 𝓛^R_d and a state s»,
      with x ranging over movers and l over levels: «z_s(x) := [Ξ_s(x, 1 − s(x)) ▷ Ξ_s(x, s(x))]»; «u := z·k»; «h(x) := the number of
      movers on the longest Ξ-path from x (1 + the largest h of a mover Ξ-target of x, with X counting 0)»; «PV(x) := the sorted list of
      the integers (ENC) of the β-sets of the P(x) maximal Ξ-paths from x»; «ic(x), io(x) := the positions in PV(x) of cv_s(x) and of
      v_s(x, 1 − s(x))»; P(x) the length of PV(x); «BASE (in every class): z_s(x), k_s(x), u_s(x) for every x.»; «P: for every l, the indicator of each value of
      (k(2l), k(2l + 1), z(2l), z(2l + 1)) ∈ {0, 1}^4, and ord_l(s).»; «H: for every l and every height value η, #{x of level l : h(x) =
      η, z_s(x) = 1} and #{… : u_s(x) = 1}.»; «X: for l ≤ d − 2, a ∈ {2l, 2l + 1}, b ∈ {2l + 2, 2l + 3}: z(a)k(b) and k(a)z(b).»; «B: for
      every x, P(x) − 1 − ic(x) and (P(x) − 1 − ic(x)) / max(1, P(x) − 1); for every l, the sum of P(x) − 1 − ic(x) over level l.»; «G: for
      every x, io(x) − ic(x), max(0, io(x) − ic(x)), max(0, io(x) − ic(x)) / max(1, P(x) − 1), and k(x) · max(0, io(x) − ic(x)).»; «Class
      PHX := BASE + P + H + X. Class PBG := BASE + P + B + G. A class potential is Φ(G, s) := a + Σ_f w_f f(G, s) with real a, w_f, one
      weight per feature name (the names carry the mover / level / height / value index above), independent of G.». ENC here only names
      the path order (fixes RI-P1: REFEREE's re-check orders the path sets by R104's set order and gets the same bounds). The items:
      «Item C-PHX3. Every PHX potential Φ with Φ(G, s) − Φ(G, step(s)) ≥ 1 at every transition of every G ∈ 𝓛^R_3 satisfies sup_(G,s) Φ
      − inf_(G,s) Φ ≥ 22 (over G ∈ 𝓛^R_3 and their states).», and since Φ_K is a PHX potential with range 22 on every G, the least such
      range is exactly 22 = 2^(3+2) − 2·3 − 4 (l. 181-182); «Item C-PBG. Every PBG potential with the same decrease property on 𝓛^R_d has
      sup − inf ≥ β_d with β_2 = 8» and β_3, β_4 the exact rationals printed by the tool: β_3 =
      4453034537330914972934687138651844782266251622384354227549825781993/236113987463513159107937918015511027189365978263843195746985017635
      = 18.859681… and β_4 = 22634873719829676833082543646859240882461448320366329878712583233393321387431622964969514556217442183989
      655534985455385639/6366416048588669711956190787368718150508096470492210455447970446960109733638512538947399915610545049296325
      61284182102267 = 35.553557… (numerator and denominator wrapped here; risecheck.out l. 3-4). The sup and inf are joint over all
      genomes of 𝓛^R_d and their states (the lo and hi rows come from different genomes; REFEREE l. 55-57, REFEREE-2 l. 55-56); they bound
      no per-genome range and nothing about T. Certificate (l. 185-188): transitions (G_i, s_i → step(s_i)) with y_i ≥ 0 and states with
      a_j, b_j ≥ 0, Σ_j a_j = Σ_j b_j = 1, such that for every feature f «Σ_i y_i (f(G_i, s_i) − f(G_i, step(s_i))) + Σ_j a_j f(G_j, s_j)
      − Σ_j b_j f(G_j, s_j) = 0»; then «Σ_i y_i ≤ Σ_i y_i (Φ(s_i) − Φ(step(s_i))) = Σ_j b_j Φ(G_j, s_j) − Σ_j a_j Φ(G_j, s_j) ≤ sup Φ −
      inf Φ (the constant a cancels)»; this inequality is PROVED (both referees: «Sound.», REFEREE l. 54, REFEREE-2 l. 54). The four
      certificate files are experiments/new/box182/cert/cert_PHX_d3_s1793.json (sha1 71fb1683…; 73 rows: 61 transitions, 7 lo, 5 hi),
      cert_PBG_d2_s179.json (bf65a4e6…; 38 rows), cert_PBG_d3_s1793.json (f878699f…; 77 rows), cert_PBG_d4_s1794.json (7f3d88c3…; 108
      rows). Cells: REFEREE l. 17 «SIGN as CERTIFIED machine items: all four certificates RE-VERIFIED independently (§3)»; REFEREE-2 l. 17
      «**SIGN as machine-certified** (Opus 5.5, D12): all 4 certificates re-verified by my own independent code in exact arithmetic».
  The RESULTS line (L-3) states (a)-(g) with their exact hypotheses and nothing wider, apart from KEY's third part at level 0, which holds
  by §0's definition of keys.
- What rests on the machine (packet §5 l. 185-197; both referees' §3 / machine checks): (i) PROVED (lane, signed): (a)-(e) above, and
  the certificate inequality of §5 (l. 185-188) that turns a certificate into the bound Σ_i y_i; «exactly 22» for PHX at d = 3 adds Φ_K
  (PHIK-DESCENT, OPT-K: its range is 22 on every G, from the all-0 to the all-1 k-state). (ii) MACHINE: that each of the four files is a
  certificate: every genome in 𝓛^R_d and Ξ-acyclic, every stored transition equal to step(s_i), every feature value of §5, the
  multipliers unique (0 free variables) and ≥ 0, every feature equation and Σ_j a_j = Σ_j b_j = 1, and the exact value Σ_i y_i (22, 8
  and the two p/q). (iii) TRUSTED BASE: Python's Fraction arithmetic and three programs, each recomputing the transitions, the features
  and the exact elimination: the lane's experiments/new/box182/risecheck.py (block CERT, simulator box150/check.py's Gen); REFEREE's
  docs/referee/scratch/cert_check.py with its t3r_sim.py, «Written from §5's text only; risecheck.py's feature code was not read.» (l.
  61), path sets ordered by R104's set order, all rows solved with an independent residual check (l. 64-66); REFEREE-2's
  docs/referee-2/R2-P-IDEAL-RISE/r2cert.py with its r2sim.py, «No lane code is used» (l. 59). No formal verification, no Lean; REFEREE l.
  80-81 «That is CERTIFIED machine evidence, not a hand proof; the trusted base is two Python programs.».
  (iv) NOT TRUSTED: the floating-point LP that produced the certificates (packet l. 194-195 «The certificates came from a floating-point
  LP (box179/lpot.py, HiGHS); only the exact re-check is the premise.»); the float multipliers stored in the files, which differ from
  the exact ones by at most 4.7e-10 (REFEREE-2 l. 69). (v) RE-CHECK SCOPE: all four certificates by all three programs (REFEREE §3 l.
  67-75; REFEREE-2 l. 63-69); controls at REFEREE bite (lo and hi swapped: 61 negative multipliers, bound −22; one stored «next»
  replaced: caught; one transition row dropped: inconsistent; l. 76-79). (vi) PRECISION: risecheck.py's acyclic() (l. 25-27) accepts a
  stored «xorder» without checking it (box150/check.py l. 38), and every certificate row carries one, so the lane tool's explicit
  acyclicity test is vacuous on the certificate genomes; acyclicity is checked by both referees' programs (REFEREE l. 74; REFEREE-2 l.
  61), and the lane tool's xheight recursion over every Ξ-edge would fail on a Ξ-cycle (a RecursionError). (vii) NOT MACHINE: (a)-(e) are hand
  proofs; their DATA (risecheck.py's PHIK, OPTK, RISE and MOVERISE counts) is not a premise («The §5 items use a machine premise (the
  tool of §5); no other signed item does.», packet l. 40-41).
- Premise: RESULTS R104's definition of the IDEAL model and of the Ξ-graph (no R104 theorem), restated in packet §0 (REFEREE-2 l. 22-24
  checked the restatement); RESULTS R105's ENC, MONO, XI-NEW and RISE, each quoted verbatim by the packet (l. 24-29: «(ENC) the Ξ-order
  of β-sets is the order of the integers Σ ±2^rank (+ for even parity), so, with ε(x, k) := ±2^rank(x, k) (+ for even parity), the value
  of option (x, k) is ε(x, k) plus the current value of its Ξ-target (ε(x, k) alone if the Ξ-target is the exit X)»; «(MONO) the current
  Ξ-value of every mover never decreases along a run»; «(XI-NEW) for t ≥ 2 every least-level mover h of step t moves to an option w ∉
  A_(s_(t−2))(h) (A_s(h): h's current option under s and its options strictly better under s)»; «(RISE) that option's value rose
  strictly at step t − 1, and some strict Ξ-descendant of h on its chain under s_(t−2) moved at step t − 1»), found in R105's title (l.
  10155), ENC and MONO also quoted from there in R113's body; RESULTS R110's definition of 𝓛^R_d, quoted verbatim by the packet (l.
  32-34: «the 2-wide degree-2 ladders in L-RED's R197 convention (movers 2l and 2l + 1 on level l, all of degree 2, no other movers,
  option k of a mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k)»), found in R110's title (l. 11323) and quoted from there in
  R112's and R113's bodies; RESULTS R111's CASCADE, quoted verbatim by the packet (l. 35-37: «(CASCADE) at any degree, at every step at
  which two distinct movers p, q of one level l flip, p or q moves, or l ≥ 1, neither moves, their current W-targets w_p ≠ w_q and (w_p,
  w_q) flips at the same step, and flips(p, q) ≤ T»), 1 hit (R111's title, l. 11598), with R111's flip = packet §0's (l. 37, 67-68).
  Whitespace normalised. L-3: «premise: R104's definition of the model only, no theorem of R104 used; RESULTS R105's ENC, MONO, XI-NEW
  and RISE only; RESULTS R110's definition of 𝓛^R_d only; and RESULTS R111's CASCADE only». Use: ENC in RISE-EQUIV and MOVE-RISE and as
  the name of the path order in §5 (fixes RI-P1); MONO in RISE-EQUIV (a); XI-NEW and RISE in RISE-EQUIV (c); R110's wiring in KEY (a),
  (c) and through them in PHIK-DESCENT, OPT-K and the certificates; CASCADE in PHIK-DESCENT and OPT-K's forcing step. Not used: R105
  KEYFLIP, LOCAL and every other R105 item, R106-R110 theorems, R111 PAIR-KF, LOCAL-KP and its other items (KEY re-proves the key facts),
  RESULTS R112, RESULTS R113 (P-IDEAL-ALIGN; KEY re-proves its ALIGN (a), (c) and KP-MOVE (a); PAIR-DOUBLE and PATH-RISE are not used),
  docs/lit, docs/sources, any other lane file (packet l. 38-41; REFEREE l. 21-27; REFEREE-2 l. 21-25). The only machine premise is §5's
  tool, for (f) and (g). Both referees byte-tested the six quotes against RESULTS at the packet's trunk c8fefddb (REFEREE l. 22;
  REFEREE-2 l. 22-23). Erratum E-2 does not bear (packet l. 29-31; REFEREE l. 23; REFEREE-2 l. 24).
- L41 and L43. The proofs are L-NEW successor 56's (packet l. 2, 6-7); the fixes entry carries none; the referees' cert_check.py,
  rise_probe.py, r2cert.py and r2rise.py are checking tools. Nothing referee-written is a proof step of the entry (my reading; neither
  referee mentions L41). No DEAD item; L43 does not bear.
- Fixes (docs/new/P-IDEAL-RISE-fixes.md, append-only; entry 1 by L-NEW successor 56 at 0320ab9e, 42 lines, sha1
  469cb2915b58e716ed8b7c692b12fa70e6c3f245, after REFEREE 33d148cd and REFEREE-2 3b03d364; entry 2 by L-NEW successor 57 at 0548afaa, l. 44-59, the file then 59
  lines, sha1 d8046a92f9081c01f488fbcdf51ba13843a9bcaf, after CHECKER C127 5793c1e2):
  - RI-P1 (l. 8-11, note): ENC is used «in §4» and «as the name of the path order in §5»; the certificates do not depend on ENC as a
    premise. REFEREE §C l. 138-139; REFEREE-2 Add. 1 l. 123-124.
  - RI-P2 (l. 12-13, note): the READING's T^R values are labelled; T^R(3) = 8 is RESULTS R112, T^R(2) = 4 and T^R(4) = 13 are lane DATA;
    the READING is not signed. REFEREE §C l. 140; REFEREE-2 Add. 1 l. 125.
  - W-2 counter check (l. 14-18): «RISE_A increments only when an option value falls between consecutive states», RISE_B checks max R ≤
    T, RISE_C checks T ≤ 1 + rs ≤ 1 + Σ R, MOVERISE checks the strict rise at every move; «The identity «R(x, k) = the rises of cv of
    the Ξ-target» is not counted». REFEREE §C l. 141-144 «The text is EXACT.»; REFEREE-2 Add. 1 l. 122.
  - Line L-2 (l. 19-31): L-1 «with exactly these four replacements, applied by script» (l. 20), R1-R4 (l. 22-31), and the word diff (l.
    32-42).
  - Entry 2, counter check (l. 49-51): MOVERISE «counts moves at which cv(z) does not rise strictly; no counter compares R(x, k) with
    moves(z)», so the corollary «R(x, k) ≥ moves(z)» of MOVE-RISE joins the identity in «no separate DATA». REFEREE §C add. 1 l. 161
    «Content: true. MOVE-RISE-R (R(x, k) ≥ moves(z)) has no risecheck.py counter.»; REFEREE-2 Addendum 2 l. 136 «**Fixes entry 2:
    CORRECT.**».
  - Line L-3 (l. 52-59): L-3 = L-2 «with exactly one replacement, applied by script» (l. 53), R5 (l. 55-56; = C127 §4 l. 92-93, by
    script), and the word diff (l. 57-59).
  No fix changes a statement, a proof or a hypothesis; RI-P1 and RI-P2 re-read packet text, the W-2 check and entry 2's counter check
  re-read the tool, R1-R5 change the line's wording only.
- Not signed: packet §6 (DATA, machine checks, excluded parts, READING, TARGET diff; «DATA / READING (not to sign)», l. 20), in
  particular the earlier DATA of boxes 179-181 (l. 211-212), the PHX / PHXV / PHXVD / PHXVDBG lower bounds at d ≥ 4
  («sampling-limited», l. 213), the obstruction READINGs and the box-181 DEAD (l. 213-215), the READING on C-PBG (l. 216-217), and §3's
  READING (l. 146-147). Not claimed: the lane conjectures RISE-2D and MOVES-2D (the line: «not claimed»; this entry states no status
  for them). OPEN, not claimed: any polynomial bound on T; any bound on R(x, k) (RISE-EQUIV only transfers bounds, §4 l. 164); PHIK-DESCENT, OPT-K and the certificates outside 𝓛^R_d; KEY's
  degree-2 clause at degree ≥ 3; the certificate classes for d ≥ 5 and other classes (§5 l. 196-197); whether the PBG bounds grow
  exponentially in d; G-N5-TIME.
- Referee strengthening (NOT part of this entry; referee remarks and own checks):
  (i) REFEREE §4 (rise_probe.py on its simulator, set order; rise_logs/probe.txt): PHIK-DESCENT from every state of 150 random 𝓛^R_d
      genomes (d 1-5) and 186 corpus 𝓛^R genomes, 100,470 transitions, 0 violations; T ≤ Φ_K(s_0) 0; Φ_K's range = 2^(d+2) − 2d − 4 on
      336 genomes; its own τ(l, p) for d = 1-7 (56 genomes), 0 failures; RISE-EQUIV (a)-(c), MOVE-RISE, MOVE-RISE-R: «32,966 / 615 / 473 /
      2,969 / 5,234 checks, 0 violations»; control: weights 2^(d−l) − 2 fail PHIK 7,329 times (l. 84-92).
  (ii) REFEREE-2 (r2rise.py on its r2sim.py, seed 182; r2rise_seed182.out): 1,500 random 𝓛^R_d ladders (d 1-4), PHIK-DESCENT from every
       state on 110,742 transitions (drop exactly 1 on 12,632); PHIK-T on 12,000 runs; RISE-EQUIV (a) on 229,528 (step, option) pairs and
       its identity on 260,752 (run, option) pairs, (c) on 24,000 runs; MOVE-RISE on 31,653 moves, MOVE-RISE-R on 125,856 pairs, the rise
       items also on 1,500 random any-degree genomes; its own forcing genomes, 1,440 transitions (d 1-8, 20 variants each), 0 failures
       (l. 70-79).
- Honest limits: (i) A POTENTIAL / EQUIVALENCE statement inside the IDEAL model: on 𝓛^R_d the weighted count Φ_K of key-misaligned
  movers falls at every step (PHIK-DESCENT), so T ≤ 2^(d+2) − 2d − 4, the value of RESULTS R113's T-BOUND by one potential; no potential
  linear in the key bits does better (OPT-K, proved for every d, its forcing genomes have short runs); option values never fall, every
  move raises its mover's value, and the largest number of rises of one option is polynomial iff T is (RISE-EQUIV, MOVE-RISE). It bounds
  nothing polynomially; G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim. (ii) KEY's first and third parts,
  PHIK-DESCENT, OPT-K and the certificates are stated on 𝓛^R_d only, KEY's second part at degree 2 only; Ξ-cyclic genomes are not
  covered. (iii) The two certificate items are MACHINE items: lower bounds 22 (PHX, d = 3) and 8, 18.8596…, 35.5535… (PBG, d = 2, 3, 4)
  on the JOINT range (sup minus inf over all genomes of 𝓛^R_d and their states) of potentials with the decrease property, resting on
  three Python programs in exact arithmetic (What rests on the machine); they bound neither a single genome's range nor T, and say
  nothing for d ≥ 5 or other classes; OPT-K's exponential range is forced on genomes whose runs are short (§3 READING, not signed). (iv)
  The DATA is per statement, as the line's DATA parenthesis says, with these exact sets and units (risecheck.py, read by me): 201
  in-tree 𝓛^R_d genome files of box150-box181 (170 distinct contents; with a start, acyclic) and 200 random 𝓛^R_d genomes (d 1-4); PHIK
  counts the 14,384 steps s → step(s) from every state of the random genomes that has a step (13,409) and of the 201 stored-start
  corpus runs (975); OPTK one check per forcing genome, of its first step and both extreme states; RISE_A, RISE_B, RISE_C and MOVERISE on
  the 401 stored-start runs (201 + 200), MOVERISE per move (1,968), testing cv's strict rise only; the identity of R(x, k) with the rises
  of cv of the Ξ-target and MOVE-RISE's R(x, k) ≥ moves(z) have no lane count; CERT one check per certificate. (v) Every statement is
  about R104's IDEAL model; nothing is said about a real N5 run or a parity game beyond what R104 already says. (vi) Premises: RESULTS
  R104's definition, R105's ENC, MONO, XI-NEW and RISE, R110's definition of 𝓛^R_d and R111's CASCADE; R106-R109, R112 and R113 are not
  used. No lit note, no lane file, no outside source; one machine premise, §5's tool, for the two certificate items only. No Lean. (vii)
  Every proof is in docs/new/P-IDEAL-RISE.md, which the line's source note names with the fixes file (which carries no proof); the
  machine premise's files are named in the line's DATA parenthesis. (viii) Names: «R114» here is this RESULTS entry; «KEY» is this
  lemma, not R104's Lemma KEY nor R38's (KEY); «R(x, k)» counts the rises of the option value v(x, k), and RESULTS R111's R(x, k) (the
  rises of cv of the Ξ-target) is the same number by RISE-EQUIV (a); «P(x)» counts maximal Ξ-paths, as R113's P(z), not R99's P(z);
  «RISE» and «XI-NEW» are R105's items; «RI-L1», «RI-L2», «RI-P1», «RI-P2» (REFEREE) and «W-1», «W-2», «P-1» (REFEREE-2) are this packet's
  referee labels; «PHX» and «PBG» are packet §5's feature classes.
- Data (DATA, not proof): experiments/new/box182/risecheck.py (l-new 2f4d96de, sha1 404df6de34c24ea8e86c305ae059ca3ce43db746, 203
  lines; deterministic, seed 182; simulator: experiments/new/box150/check.py's Gen; random genomes: experiments/new/box162/flipcheck.py's
  rand_lr), output frozen in experiments/new/box182/risecheck.out (sha1 3685b69bcdc03bf261931e94ef3427550026a1b6, 6 lines) and wired
  into experiments/new/check.sh block «P-IDEAL-RISE» (l. 927-934, with sha1 pins of the packet, L-1, risecheck.py, risecheck.out, the
  four certificates, the fixes (d8046a92), L-2 and L-3 at 0548afaa; at 0320ab9e the same block pinned the fixes as 469cb291 and no L-3,
  at 2f4d96de no fixes and no L-2). L-3's DATA parenthesis:
  «(DATA, experiments/new/box182/risecheck.py: PHIK-DESCENT 0 violations on 14,384 steps (every state of 200 random 𝓛^R_d genomes, d
  1-4, and the stored-start runs of the 201 in-tree 𝓛^R_d genome files of experiments/new/box150 to box181), equality on 1,772; the
  OPT-K forcing step and both extreme states on the 72 forcing genomes for d = 1-8, 0 failures; RISE-EQUIV (non-decreasing values, R(x,
  k) ≤ T and T ≤ 1 + #{t ≤ T − 1 with a rise} ≤ 1 + Σ R) and MOVE-RISE 0 violations on 401 stored-start runs with 1,968 moves; the
  identity of R(x, k) with the rises of cv of the Ξ-target and MOVE-RISE's R(x, k) ≥ moves(z): no separate DATA; the four
  certificates experiments/new/box182/cert/*.json re-checked in exact arithmetic)». What each count covers (risecheck.py, read by me): PHIK every transition s → step(s), where defined,
  from every state of the random genomes and of the corpus runs (14,384; «equality» = a drop of exactly 1, 1,772); OPTK per forcing
  genome (72); RISE_A every (run, step, option) fall, RISE_B max R ≤ T per run, RISE_C T ≤ 1 + rs ≤ 1 + Σ R per run (401 runs); MOVERISE
  cv_(s_t)(z) > cv_(s_(t−1))(z) per move (1,968), not R(x, k) ≥ moves(z); CERT per certificate (4). The block's outputs, reproduced by
  both referees at 2f4d96de (REFEREE §4 l. 93 «risecheck.py regenerates risecheck.out identically.»; REFEREE-2 l. 82, «exit 0») and
  re-run for this draft (first fill 2026-11-06T17:33:57Z from a `git archive` of 0320ab9e's experiments/new and docs/new, rc 0, PASS
  line ending «fixes 469cb291, line L-2 25170417: PASS»; second fill 2026-11-06T20:19:10Z from a `git archive` of 0548afaa's, rc 0, PASS
  line ending «fixes d8046a92, line L-2 25170417, line L-3 4a553a29: PASS»; risecheck.py's output byte-equal to risecheck.out both
  times): «SCOPE corpus_files 201 random 200
  phik_steps 14384 phik_tight 1772 optk_transitions 72 rise_runs 401 rise_moves 1968»; «PHIK 0 OPTK 0 RISE_A 0 RISE_B 0 RISE_C 0
  MOVERISE 0 CERT 0»; four CERT lines «CERTIFIED». No signed statement uses any count; the certificate items use the CERT check as their
  machine premise (What rests on the machine).
- Signatures: REFEREE docs/referee/R-P-IDEAL-RISE.md: successor 24's report 33d148cdd5613842902b1ad48a817feed29b4bfd
  (2026-11-06T14:13:52Z, new file, 129 lines, sha1 93b7d6572fe639b46a8e9b00f079b9b3974b116d, with scratch/cert_check.py,
  scratch/rise_probe.py and rise_logs/): every item SIGN, the certificates as CERTIFIED machine items after its independent
  re-verification, L-1 required RI-L1, optional RI-L2, RI-P1, RI-P2 (l. 10-19, 25-27, 98-119); §C 807a59c489fcdc005a3c92d5870d7cccaf8619bb
  (2026-11-06T15:55:20Z, 152 lines, sha1 20adb3aaffb87869772293ec7a86858b588e2b82; l. 1-129 = 33d148cd's, by diff): «Fixes entry 1:
  CORRECT.» (l. 137), the W-2 text «EXACT» against risecheck.py (l. 141-144), the byte test of L-2 (l. 145-147), «RI-L1 MET» (l. 148),
  «RI-L2 MET» (l. 150), «Verdict: L-2 MATCHES. Every item stays SIGNED. Open items of mine: none.» (l. 152); §C add. 1
  3489d79779d29449c1c84e23f281d3ae9295c40c (2026-11-06T19:37:37Z, 166 lines, sha1 428c4bd5ba47cf99a963a2d96fa36265b64f6859; l. 1-152 =
  807a59c4's, by diff): the byte test of L-3 against C127 §4 (l. 158-159), «Content: true.» (l. 161), its own miss recorded (l.
  163-165), «Verdict: L-3 MATCHES. All items stay SIGNED.» (l. 166). REFEREE-2
  docs/referee-2/R2-P-IDEAL-RISE.md: successor 28's report 3b03d364db59b0329dfb0193eb95e8451661405f (2026-11-06T13:57:02Z, new file, 115
  lines, sha1 6838e657a0f919dbf7612d259d7378ef049ffb9c, with R2-P-IDEAL-RISE/r2cert.py, r2cert.out, r2rise.py, r2rise_seed182.out):
  every item SIGN, the certificates «SIGN as machine-certified», «No gap. No REFUSE.», L-1 MATCHES after W-1 and W-2, P-1 optional (l.
  10-19, 84-94, 100-115); Addendum 1 6c88dc46d8322881f2984d24b4f17f8c2c50ec17 (2026-11-06T15:55:22Z, 130 lines, sha1
  052764c8257c07a3071d8aa64103b97e4ee84e70; l. 1-115 = 3b03d364's, by diff): «**Fixes entry 1: CORRECT.**» (l. 121), «**Line L-2:
  MATCHES.**» after its byte test (l. 126-128), «My SIGNs stand.» (l. 130); Addendum 2 bdbf0ddec38ccafefa5ad72165357c296e5bdacf (2026-11-06T19:37:52Z, 141 lines,
  sha1 d605db5658ba63aa37c8476d1ad8fd0550968f46; l. 1-130 = 6c88dc46's, by diff): «**Fixes entry 2: CORRECT.**» (l. 136), its own miss
  recorded (l. 138-139), «**Line L-3: MATCHES.**» after its byte test (l. 140-141), «My SIGNs stand.» (l. 141). Lane: freeze and L-1
  2f4d96de1a46b952fda1a0f7c40334f5485a442a, fixes entry 1 and L-2 0320ab9ecb965836c426a48eb26aa2fc35dff72a, fixes entry 2 and L-3
  0548afaa935381250f09fe5732b121ff16d19c3a.
  INDEPENDENCE: REFEREE l. 2-3 «Independent: I did not open or list docs/referee-2/ on this packet before this report was pushed.»;
  REFEREE-2 l. 2-3 «Independent: docs/referee/ not read for this packet before this push.». REFEREE-2's report (13:57:02Z) precedes
  REFEREE's (14:13:52Z); neither cites the other's first report; each re-verified the four certificates with its own simulator, its own
  feature code written from §5's text and its own exact elimination (REFEREE l. 61; REFEREE-2 l. 59-60), and REFEREE ordered the path
  sets without ENC. In the second round REFEREE knew REFEREE-2's items only through the fixes entry (§C l. 136 «I know REFEREE-2's items
  (W-1, W-2, P-1) only through the entry.»). Differences, resolved: both required the certificates' range binder (RI-L1 = W-1, R1 in
  REFEREE-2's form); REFEREE-2 alone required W-2 (DATA); REFEREE alone raised RI-P1, RI-P2; both offered the longer truncations (RI-L2 =
  P-1). Both SIGN the same items and both MATCH L-2 and L-3 (each byte-tested both with its own script). The two second rounds were
  pushed 2 s apart (15:55:20Z, 15:55:22Z); the two third rounds were committed 15 s apart (19:37:37Z, 19:37:52Z), each parsing C127 §4
  itself, and each records as its own miss that its second round did not check the second half of the MOVE-RISE clause against the
  no-DATA list (REFEREE §C add. 1 l. 163-165; REFEREE-2 Addendum 2 l. 138-139). No disagreement in substance.
- TARGET.md diff: TARGET.md §1-§3 define parity games («A parity game is G = (V, V_E, V_O, E, pr) with V finite»), the regions W_E, W_O,
  M4 (§2 «There is a deterministic algorithm A and a polynomial p such that for every parity game G, A on input G halts within») and the
  word-RAM cost model; no statement of this entry mentions a parity game, a winning region, an algorithm's running time or a cost model
  (packet §6 l. 218-220 «Diff against TARGET.md: no statement mentions a parity game, a winning region, an algorithm's running time or a
  complexity class.» «None is an M4 or M3 claim, none bounds anything polynomially (PHIK-T is exponential; RISE-EQUIV is an
  equivalence), none is a gauntlet step. G-N5-TIME stays OPEN.»; REFEREE §5 l. 96-97 «Nothing is polynomial (PHIK-T is exponential;
  RISE-EQUIV is an equivalence). Not M3, not M4, not a gauntlet step. G-N5-TIME OPEN.»; REFEREE-2 l. 97-98 «IDEAL model only; PHIK-T is
  exponential; RISE-EQUIV is an equivalence; the certificates bound potentials, not T; not M3 / M4 / step 4; G-N5-TIME OPEN.»). The
  line (L-3) makes no M4 claim and no TARGET claim; its tail reads «a POTENTIAL / EQUIVALENCE statement inside the IDEAL model» and
  «G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim» (L-3, by script). Not a step-4 pass. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER R113's UPDATE of G-N5-TIME (GAPS at b5ca0d4d: the last UPDATE on l. 11 is
R113's, «UPDATE 2026-11-06 17:00Z: RESULTS R113 (P-IDEAL-ALIGN; CHECKER C125 bd7cb5e4) …», before the row's closing « |»), built by script
(fill2/upd114b.py: upd114.py with its 17 controls (R97-R113, all landed, byte for byte, True; printed exactly as at the first fill)
and its R114 call unchanged, run on L-3; sentinel_build111 of upd111.py unchanged, default drops, the «(DATA, » opening; R111's
clause step applied to the certificate clause (G-U); cross-checked against a direct build: True; equal to the first fill's UPDATE with
C127 §4's one replacement: True) only from the clauses of the title line L-3: the five labels behind their
clauses, the certificate clause after «(MOVE-RISE)»; « (2026-11-06) — » → «: »; the DATA parenthesis before the source parenthesis
opened as «; DATA, …»; «G-N5-TIME stays OPEN» and «not M3, not a step-4 pass, not a TARGET.md claim» dropped; the source parenthesis
kept; «. G-N5-TIME stays open.» at the end. L-3 holds no "|"; the UPDATE holds none (4,288 bytes, 73 «(» / 73 «)»; sha1 of the line
without newline, placeholders unfilled: acc07ee177f6a1bf161313383e2c70dc2e11cb1f, = C127 §4's). <DATE> is the landing date (YYYY-MM-DD, by date -u
at the landing commit; C114 Add. 1 E-1), <HH:MM> the landing time and <checker> the CHECKER C127 commit, all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R114 (P-IDEAL-RISE; CHECKER C127 <checker>) [refereed-only] LANDED: In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of R104 used; RESULTS R105's ENC, MONO, XI-NEW and RISE only; RESULTS R110's definition of 𝓛^R_d only; and RESULTS R111's CASCADE only), on acyclic Ξ-graphs, with T the number of steps of a run, Mv_t the movers of step t, moves(x) the number of steps t with x ∈ Mv_t, KP_s(x) the option of x with the least key under s, k_s(x) := [s(x) ≠ KP_s(x)], on 𝓛^R_d w_l := 2^(d−l) − 1 and Φ_K(s) := Σ_x w_lev(x) k_s(x), v_s(x, k) the integer value of option (x, k) under s (R105 ENC), cv_s(z) := v_s(z, s(z)), R(x, k) the number of steps t with v_(s_t)(x, k) > v_(s_(t−1))(x, k) and M the number of options: on 𝓛^R_d, KP_s of a level-0 mover does not depend on s and both movers of a level l ≥ 1 have KP_s equal to the option index k for which mover 2(l − 1) + k has the smaller current key, and two movers of one level on the same option j have the order of their keys given by their gate indices of option j; at any degree elsewhere, a mover of degree 2 that moves at step t moves to KP_(s_t) and was not on it before (KEY); on 𝓛^R_d, Φ_K(s_t) ≤ Φ_K(s_(t−1)) − 1 at every step, so T ≤ Φ_K(s_0) ≤ 2^(d+2) − 2d − 4 and T = 0 from a start where every mover is on KP (PHIK-DESCENT); for d ≥ 1, if a + Σ_x w_x k_s(x), with real a and w_x not depending on the genome, falls by at least 1 at every step of every genome of 𝓛^R_d from every state, then w_x ≥ 2^(d−lev(x)) − 1 for every x and its range on every genome of 𝓛^R_d is at least 2^(d+2) − 2d − 4, with equality for Φ_K (forcing genomes with every Ξ-target the exit X, in which every mover moves at most once) (OPT-K); at any degree, every option value is non-decreasing along a run, R(x, k) is the number of rises of cv of the Ξ-target of (x, k) (0 if it is X), R(x, k) ≤ T, and T ≤ 1 + Σ_(x,k) R(x, k) ≤ 1 + M max_(x,k) R(x, k), so on any family max_(x,k) R(x, k) is bounded by a polynomial in N + M iff T is (RISE-EQUIV); at any degree, a move of z at step t gives cv_(s_t)(z) > cv_(s_(t−1))(z), so R(x, k) ≥ moves(z) when the Ξ-target of (x, k) is the mover z (MOVE-RISE); and, by exact rational certificates checked by machine, for the feature classes PHX (key, Ξ-unhappiness and pair-state bits, Ξ-height counts, cross-level products) and PBG (key, Ξ-unhappiness and pair-state bits, value budgets and value gaps from the ENC integers of the maximal Ξ-paths) of the packet, every potential linear in the features with weights not depending on the genome that falls by at least 1 at every step of every genome of 𝓛^R_d has range (supremum minus infimum over all genomes of 𝓛^R_d and their states) at least 22 for PHX at d = 3 (so exactly 22, attained by Φ_K) and at least 8, 18.8596… and 35.5535… for PBG at d = 2, 3, 4: a POTENTIAL / EQUIVALENCE statement inside the IDEAL model; bounds nothing polynomially (PHIK-DESCENT gives the exponential bound 2^(d+2) − 2d − 4, the certificates are lower bounds on potentials, not on T); the conjectures RISE-2D (every option of a run on 𝓛^R_d rises at most 2d times) and MOVES-2D are not claimed; Ξ-cyclic genomes and genomes outside 𝓛^R_d (outside RISE-EQUIV, MOVE-RISE and the degree-2 clause of KEY) are not covered; DATA, experiments/new/box182/risecheck.py: PHIK-DESCENT 0 violations on 14,384 steps (every state of 200 random 𝓛^R_d genomes, d 1-4, and the stored-start runs of the 201 in-tree 𝓛^R_d genome files of experiments/new/box150 to box181), equality on 1,772; the OPT-K forcing step and both extreme states on the 72 forcing genomes for d = 1-8, 0 failures; RISE-EQUIV (non-decreasing values, R(x, k) ≤ T and T ≤ 1 + #{t ≤ T − 1 with a rise} ≤ 1 + Σ R) and MOVE-RISE 0 violations on 401 stored-start runs with 1,968 moves; the identity of R(x, k) with the rises of cv of the Ξ-target and MOVE-RISE's R(x, k) ≥ moves(z): no separate DATA; the four certificates experiments/new/box182/cert/*.json re-checked in exact arithmetic (P-IDEAL-RISE, docs/new/P-IDEAL-RISE.md with its fixes entry 1, docs/new/P-IDEAL-RISE-fixes.md; L-NEW successor 56). G-N5-TIME stays open.

Addendum (subagent, for the Lead; does not land; written 2026-11-06T17:50:34Z by date -u). (1) FIRST FILL on line L-2 (l-new 0320ab9e, sha1
25170417…), to CHECKER C127. NOT pushed; my commits: the three merges (--no-ff) e6afb606 (l-new 0320ab9e), 14783386 (referee 807a59c4),
8ac6757b (referee-2 6c88dc46) and one commit holding this file. Push trunk before landing. (2) TITLE l. 424 = "### R114
[refereed-only] " + L-2 without its newline + ", CHECKER PASS (docs/checker/C127.md, checker PENDING)", checked by script (chk114.py):
equal, byte for byte (True); the only «### R» heading of this file; 72 + 1 «(» and 72 + 1 «)», balanced; no «[lane», no packet name
before the claims. (3) BODY l. 424-694 (python slice d[423:694]; 0 "|" in the range, by script); GAPS preamble l. 696-705 (two "|", both
inside quotation marks: the row's closing « |» and «holds no "|"»); UPDATE l. 706 (d[705]; one line, 0 "|", one each of <DATE>,
<HH:MM>, <checker>; 4,251 bytes; sha1 7aae445df618c04e4b378c54092664a3a41cf0a3 of the unfilled line without newline; controls True ×17:
R97's-R113's landed UPDATEs). No Dead-ends row is drafted ((14)). A landing script in the shape of R113's slices d[423:694] for the entry
and reads d[705] for the UPDATE (with «R114», «R113» as PREV, «C127», and the GAPS l. 11 assertion on «RESULTS R113 (P-IDEAL-ALIGN» as
the last UPDATE). (4) RE-RUNS: listed in the header paragraph "Re-runs", (a)-(g). NOT RUN: the referees' rise probes (their committed
logs read); scripts/verify.sh; the full check.sh. (5) QUOTE SWEEP (chk114.py: the rule of chk113b.py: outermost guillemet quotes,
whitespace joined, split at the ellipsis, parts of 6+ characters; sources: the packet, L-1, L-2, the fixes, risecheck.py and
risecheck.out, check.sh, box150/check.py and box162/flipcheck.py at 0320ab9e, N5-RISEPROOF-box181.md, both referee files at 807a59c4 /
6c88dc46 with cert_check.py, rise_probe.py, rise_logs, r2cert.py, r2cert.out, r2rise.py and r2rise_seed182.out, P-TR3.md at d3e3cde8
(for the R104 quote), RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, NOW, LEAD-STATE, TARGET.md, CLAUDE.md, notes/L-NEW.md, C120-C126,
R112-draft, R113-draft at the local trunk, the commit subjects of the cited commits, my re-run outputs): 462 outermost quotes, 376 parts of 6+ characters, every part found (0 not found); in the title and body alone 132 quotes, 111 parts, 0 not found; GAPS preamble and UPDATE 12 quotes, 8 parts, 0 not found. Line-precise: 117 of 117 (source, cited line range, quote) triples found verbatim, whitespace-normalised, inside the cited lines.
Every sha1, line count and commit time cited was re-measured in this session (sha1sum, wc -l, diff, git log -1). STALE STATUS in title
and body (by script): «pending» 0 apart from the title fill «checker PENDING)»; «not yet» 0; «not landed» 0; «unlanded» 0; «provisional» 0; «stays OPEN» / «stay OPEN» 3 (each about G-N5-TIME: the title's own «G-N5-TIME stays OPEN» and two quotations in the TARGET.md diff); no sentence states a status of RISE-2D or MOVES-2D (they are «not claimed»); L-1 only as history; «L-3» 0. (6) DISCREPANCIES: (11) D-1 to D-7. I found no error in a signed statement. (7) FLAGS FOR THE LEAD AND
CHECKER: G-0 (C127), G-9 (i) (MOVE-RISE's DATA covers cv's strict rise only, not «so R(x, k) ≥ moves(z)»; C125 E-1 class; line not
changed, per the brief), G-M (what rests on the machine; the lane tool's vacuous acyclicity test on «xorder» genomes; the machine files
named in the DATA), G-U (the certificate clause's place in the UPDATE), G-2 (i) (KEY's equal-option clause at level 0), G-8 (the scope
tail; MOVES-2D undefined); NOTE G-C. (8) NOT VERIFIED: the referees' rise probes were not re-run (their logs were read); the Lead brief
of BOX 182 and the 15:09Z relay beyond the lane commits; L-RED's RISE-2D result (G-11 (ii)) was not checked (lane work, not used);
scripts/verify.sh and the full check.sh were not run. (9) LANDING SIMULATION (sim114.py, on in-memory copies of RESULTS and GAPS at the
local trunk, R113 as landed): RESULTS 13,003 -> 13,275 lines (wc -l), a pure insertion of 272 lines (the entry block with "checker PENDING)" filled, plus one blank line) directly after R113's landed block (R113 l. 12,152-12,392, blank l. 12,393, byte-unchanged: True; R110's, R111's and R112's blocks byte-unchanged: True): True; R114 at l. 12,394-12,664, blank l. 12,665, the next line (**Erratum E-1**) moves to l. 12,666, the Erratum E-2 line to l. 12,679, the Note E-3 line to l. 12,707, the Dead ends heading to l. 12,738; order R110, R111, R112, R113, R114, E-1, E-2, E-3, Dead ends: True; every other line byte-unchanged (common prefix and suffix: True); 0 "|" inserted. GAPS: only l. 11 changes: True; new l. 11 = old l. 11 with its closing " |" replaced by " " + the filled UPDATE + " |": True; "|" on l. 11 76 -> 76 (pipe count unchanged); UPDATE 2026- heads 48 -> 48 plus 1 UPDATE head with the simulation year 2099, directly after R113's and now the last on the line; 23 -> 23 lines (wc -l). Fill values used only for the simulation: <DATE> 2099-01-03, <HH:MM> 00:00, <checker> 0000000. (10) THIS DRAFT'S SHA1: a file cannot state its own sha1. The sha1 of this file with the forty hex
digits after the next colon replaced by forty «0» characters is: 120da50e7855a4c72af3ccf12c5ed7b39cb1d6f0. The file's actual sha1 and
line count are in the hand-back to the Lead (and re-measurable with sha1sum). Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r114/ (runw182.sh / w182.out /
w182raw.out, rsstats.py / rsstats.out, refcert_referee.out, refcert_referee2.out, pq114.py, wdiff114.py / wdiff114.out, prem114.py /
prem114.out, upd114.py / upd114.out / upd114L2.txt, fill114.py, chk114.py, lp114.py, sim114.py).
Addendum 2 (subagent, for the Lead; does not land; written 2026-11-06T20:18:52Z by date -u). (1) SECOND FILL on line L-3 (l-new 0548afaa,
sha1 4a553a29…), to CHECKER C127 Add. 1. NOT pushed; my commits: the four merges (--no-ff) 9a426b8a, faa8c611, d7eb47d8, b876c884 and one
commit holding this file. (2) TITLE l. 473 = "### R114 [refereed-only] " + L-3 without its newline + ", CHECKER PASS
(docs/checker/C127.md, checker PENDING)", checked by script (chk114b.py): equal, byte for byte (True); the only «### R» heading of this
file; 74 + 1 «(» and 74 + 1 «)», balanced; no «[lane», no packet name before the claims. (3) BODY l. 473-774 (python slice d[472:774]; 0
"|"); GAPS preamble l. 776-786 (two "|", both inside quotation marks: the row's closing « |» and «holds no "|"»); UPDATE l. 787 (d[786];
one line, 0 "|", one each of <DATE>, <HH:MM>, <checker>; 4,288 bytes; sha1 acc07ee177f6a1bf161313383e2c70dc2e11cb1f of the line without
newline, computed on the UNFILLED form, as C127 §4 l. 96 states it, «Rebuilt UPDATE (the same replacement in d[705], line without
newline, unfilled): sha1 acc07ee177f6a1bf161313383e2c70dc2e11cb1f»: equal). A landing script slices d[472:774] for the entry and reads
d[786] for the UPDATE (with «R114», «R113» as PREV, «C127», and the GAPS l. 11 assertion on «RESULTS R113 (P-IDEAL-ALIGN» as the last
UPDATE). (4) NO PLACEHOLDER: both referees' byte tests of L-3 are on file, so everything in the entry is final for C127 Add. 1 (the only
fill left is the title's «checker PENDING)» and the UPDATE's three placeholders, at landing). (5) QUOTE SWEEP (chk114b.py: chk114.py's
rule and sources, plus L-3, the fixes and check.sh at 0548afaa, R-P-IDEAL-RISE.md at 3489d797, R2-P-IDEAL-RISE.md at bdbf0dde, C127, the
first-fill draft ecd79952, the commit subjects of the new commits, my second-fill outputs): 546 outermost quotes, 446 parts of 6+
characters, every part found (0 not found); in the title and body alone 157 quotes, 137 parts, 0 not found; GAPS preamble and UPDATE 12
quotes, 8 parts, 0 not found. Line-precise: 151 of 151 (source, cited line range, quote) triples found verbatim, whitespace-normalised,
inside the cited lines. (6) WORD DIFF ecd79952 → this file (wd114b.py, difflib on whitespace tokens, Addendum 2 left out): 24 line
regions, 56 token hunks (58 tokens deleted, 1701 inserted), every hunk in a region listed in the SECOND FILL paragraph. (7) STALE STATUS
in title and body (by script): «pending» 0 apart from the title fill «checker PENDING)»; «not yet» 0; «not landed» 0; «unlanded» 0;
«provisional» 0; «stays OPEN» / «stay OPEN» 3 (each about G-N5-TIME, as at the first fill); no sentence states a status of RISE-2D or
MOVES-2D; L-2's old DATA phrase «the identity of R(x, k) with the rises of cv of the Ξ-target: no separate DATA», by script: 0 times in
the title and the UPDATE, once in the body, as the old string of R5 in the line history (followed by « → »); L-3's phrase once each in
the title and the UPDATE; «L-2» only as history (the line history, the L-2 verdicts and byte tests, fixes entry 1, the check.sh pins and
the first-fill PASS line, R5's base), never as the line of record; L-2 named as the current line («RESULTS line is L-2», «title is L-2»,
«The RESULTS line (L-2)», «line (L-2)», «L-2's DATA parenthesis», «(L-2, by script)», «L-2's parentheses», «title line L-2», «L-2 holds
no», and L-2 with a colon before the premise quote), by script in the title, the body, the GAPS preamble and the UPDATE: 0 times. (8)
LANDING SIMULATION (sim114b.py: sim114.py with the UPDATE's sha1 assertion acc07ee1…, otherwise unchanged, on in-memory copies of RESULTS
and GAPS at the local trunk, R113 as landed): RESULTS 13,003 -> 13,306 lines (wc -l), a pure insertion of 303 lines (the entry block with
"checker PENDING)" filled, plus one blank line) directly after R113's landed block (R113 l. 12,152-12,392, blank l. 12,393,
byte-unchanged: True; R110's, R111's and R112's blocks byte-unchanged: True): True; R114 at l. 12,394-12,695, blank l. 12,696, the next
line (**Erratum E-1**) moves to l. 12,697, the Erratum E-2 line to l. 12,710, the Note E-3 line to l. 12,738, the Dead ends heading to l.
12,769; order R110, R111, R112, R113, R114, E-1, E-2, E-3, Dead ends: True; every other line byte-unchanged (common prefix and suffix:
True); 0 "|" inserted. GAPS: only l. 11 changes: True; new l. 11 = old l. 11 with its closing " |" replaced by " " + the filled UPDATE +
" |": True; "|" on l. 11 76 -> 76 (pipe count unchanged); UPDATE 2026- heads 48 -> 48 plus 1 UPDATE head with the simulation year 2099,
directly after R113's and now the last on the line; 23 -> 23 lines (wc -l). Fill values used only for the simulation: <DATE> 2099-01-03,
<HH:MM> 00:00, <checker> 0000000. (9) NOT VERIFIED: the referees' tools not re-run (their files read); scripts/verify.sh and the full
check.sh not run; the Lead's 18:57Z relay (fixes l. 46) is a message, not verifiable from the repository; rsstats.py (first fill (b)) not
re-run (risecheck.py, box150/check.py, box162/flipcheck.py, the certificates and risecheck.out are byte-equal at 0320ab9e and 0548afaa,
so its measurements stand). (10) NOTES, no verdict affected: (i) fixes entry 2 l. 46 «copied by script from C127 §5» and REFEREE-2's Add.
2 l. 140 «C127 §5's single replacement» name a §5; C127 has no §5 (its sections are 1-4 and DONE / FINDINGS / NEEDS) and the replacement
is in §4 (l. 91-93); R5 equals C127 §4's pair (l3rel114.py), and REFEREE parsed it from 5793c1e2 (§C add. 1 l. 158). (ii) fixes entry 2
l. 46-47 says C127 «was not on origin» at 18:58Z (checker head 36b2f02e); C127's commit 5793c1e2 is 2026-11-06T18:30:21Z (commit time;
its push time is not in the repository) and 36b2f02e (17:59:03Z) is its ancestor; the text is final either way (R5 = C127 §4). (iii)
L-3's source note still reads «with its fixes entry 1» and «L-NEW successor 56», as C127 §4 requires (one replacement, nothing else
changes; the R113 precedent: R113's L-3 kept «with its fixes entry 1» with entry 2 on file); entry 2 is by successor 57 and is named in
the body (Object, Fixes, Signatures). (iv) C127 §3's wording option «KEY: no separate DATA» (l. 60) is not in L-3 and is not applied (not
required). (v) After the packet, L-NEW box 185 (4fd6598a, «REDUCE-XI (T <= 1 + sum of Xi-target moves; MOVES-2D <=> quadratic T^R)»,
lane, unrefereed) and box 186 (a6744977) treat MOVES-2D; the entry states no status for MOVES-2D (the line: «not claimed») and uses
neither. Scratch: /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r114/fill2/
(edit114b.py, header1.txt, secondfill.txt, addendum2.raw / addendum2.txt / add2.py, l3rel114.py / l3rel114.out, upd114b.py / upd114b.out
/ upd114L3.txt, runw182L3.sh / w182L3.out / w182L3raw.out, chk114b.py / chk114b.out, lp114b.py, wd114b.py / wd114b.out, sim114b.py /
sim114b.out, R114-draft-ecd79952.md, arch0548/).
