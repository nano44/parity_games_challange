# Draft RESULTS R111 (Lead; first fill 2026-11-06T02:17:22Z on line L-2 (draft sha1 462ac44d, CHECKER C124 9c9b03b7: FAIL E-1; G-0: C124 is right); SECOND FILL 2026-11-06T05:47:40Z by date -u (subagent) on P-IDEAL-KEYS line L-3, docs/new/P-IDEAL-KEYS-line-L3.txt, l-new 432edf82, sha1 c29f0a9365e700e0888018be42caf8757df1ac74) — to CHECKER C124 Add. 1 — LANDED in RESULTS 2026-11-06 07:16Z (CHECKER C124 18aa6728 PASS), after R110, before Erratum E-1
SECOND FILL (2026-11-06T05:47:40Z by date -u, subagent; for CHECKER C124 Add. 1). Read at the origin heads fetched at its start (git
fetch, 2026-11-06T05:3xZ): l-new 432edf82 (it holds L-3 and fixes entry 2), l-comp 159df067, referee 6f0daf60 (its parent fadbb9a0 holds
the L-3 byte test; 6f0daf60 adds R-P-IDEAL-ALIGN.md and its scratch files only and leaves R-P-IDEAL-KEYS.md byte-equal, by sha1),
referee-2 ea08029d (its parent 7ff32432 holds the L-3 byte test; ea08029d leaves R2-P-IDEAL-KEYS.md byte-equal, by sha1), checker
9c9b03b7; origin trunk 65231422 («Lead: P-TR3 L-2 MATCHES at REFEREE; P-IDEAL-ALIGN signed by REFEREE (AL-L1); SUM_2 DEAD (L-SI); log»).
Local trunk 7ad0389c = five merges (--no-ff, none an ancestor of 65231422 before) into 65231422: c54f19b8 (l-new 432edf82), 6b95c066
(l-comp 159df067), 02d0f872 (referee 6f0daf60), 1d689e9a (referee-2 ea08029d), 7ad0389c (checker 9c9b03b7). Not pushed. RESULTS, GAPS
and TARGET.md are byte-equal at d056db87, 65231422 and 7ad0389c (last commit on RESULTS and GAPS: d056db87; RESULTS sha1 90dd5827…,
12,176 lines; GAPS d608ac71…), so (0), (6) and (9) stand. New sources: docs/checker/C124.md (9c9b03b7, 2026-11-06T02:54:51Z, 122 lines,
sha1 99d034725d498a3225da7c9b863806b89310b20b): FAIL E-1 only (the first fill's G-9 (i) and (ii), REFEREE-2's P-1), G-0 «C124 is right»,
G-8 (b) a note, everything else PASS; E-1 fixed by one L-3 = L-2 with the one replacement of its §5 (l. 102-106), the UPDATE to be
rebuilt by the same rule (§4, expected sha1 284c9dea8e192568f53cf0425dc6ee00c2d7b42d); line L-3, docs/new/P-IDEAL-KEYS-line-L3.txt
(l-new 432edf82, 2026-11-06T03:41:53Z, the file's only commit; sha1 c29f0a9365e700e0888018be42caf8757df1ac74 with newline, 5,636 bytes,
= C124 §5's expected values); fixes entry 2 (docs/new/P-IDEAL-KEYS-fixes.md l. 102-118 at 432edf82; file 118 lines, sha1
504403c3816279bee51da5358e0e77250ffb8f69, l. 1-100 unchanged); REFEREE's byte test of L-3 (docs/referee/R-P-IDEAL-KEYS.md §C add. 1, l.
228-243, fadbb9a0, 04:09:18Z: l. 243 «Verdict: L-3 MATCHES. All signatures stand.»); REFEREE-2's byte test of L-3
(docs/referee-2/R2-P-IDEAL-KEYS.md Addendum 2, l. 191-201, 7ff32432, 04:13:09Z: l. 195 «**Fixes entry 2: CORRECT.**», l. 199 «**Line
L-3: MATCHES.**»). My byte test of L-3 (scratch fill2/l3rel111.py, rc 0): the one old / new pair parsed from C124 l. 103-104 by script
(line wraps joined), the old string once in L-2 and the new string once in L-3, L-2 with the replacement = L-3 (True); fixes l. 109-110
(R11) carry the same pair (True); 122 «(» / 122 «)», depth never negative, final 0; 0 "|"; one « — »; «2026» once. Re-runs: check.sh
block «P-IDEAL-KEYS» from a git archive of 432edf82 (05:43:30Z-05:43:33Z, rc 0, PASS; keycheck.py's raw output byte-equal to
keycheck.out and to the first fill's); the UPDATE rebuilt from L-3 (upd111b.py, the 14 controls True; it equals the first fill's UPDATE
with the one C124 §5 replacement, True; sha1 = C124 §4's, True); the quote sweep and the landing simulation (Addendum 2). Changed at
this fill, and nothing else: this header line and this paragraph; the title (L-3); in the entry, Object (the packet identical at
432edf82, fixes entry 2, the line of record L-3, line history, the L-3 byte tests), Claims (L-3), Premise (L-3), Fixes (entry 2 and the
closing sentence), Data (L-3's DATA parenthesis; the pins and the re-run at 432edf82), Signatures (REFEREE §C add. 1, REFEREE-2 Addendum
2, the lane commit), INDEPENDENCE (L-3), TARGET.md diff (L-3); the GAPS preamble and the UPDATE (rebuilt from L-3); the digest of
Addendum (10); Addendum 2 (new). Honest limits (v) is unchanged: it already states the KP form and the 516 / 2,188 split (C124 §5). The
FIRST FILL text below (from FIRST FILL (this text) to (14)) and Addendum (1)-(9) are kept byte-unchanged as the record of the fill on
L-2: where they call L-2 the title line or the current line, say that no L-3 exists, quote L-2's DATA phrase «for the constant keys, on
2,704 intervals», or give the first fill's line numbers, counts and UPDATE sha1, they describe draft 462ac44d at 02:17Z; C124 ruled its
flags G-0 (C124 right), G-9 (i)-(ii) (E-1) and G-8 (b) (note) as above, and the entry block follows L-3.
FIRST FILL (this text). Read at the origin heads fetched at its start (git fetch, 2026-11-06T01:5xZ): l-new 06d4238d (its ancestor
1a178aff holds L-2 and fixes entry 1; 06d4238d adds box 175 files and the notebook only, and changes no P-IDEAL-KEYS file, box172 file
or check.sh: the packet, L-1, L-2, the fixes, keycheck.py, keycheck.out and check.sh are byte-equal at 1a178aff and 06d4238d by sha1),
referee cb7e2909, referee-2 6c6f2033, checker 21ff8727; origin trunk 7a976cc4 («Lead: P-IDEAL-KEYS L-2 to referees; TOP-C candidate
(L-RED R209 attack, L-NEW box 175 proof); L-SI 40; sweep 01:02Z; log»). Local trunk 9ab24552 = four merges (--no-ff, one per lane head,
none an ancestor of 7a976cc4 before): d9d540e4 (l-new 06d4238d), 60a9925a (referee cb7e2909), fdd1f0f0 (referee-2 6c6f2033), 9ab24552
(checker 21ff8727); not pushed. RESULTS, GAPS, TARGET.md, DECISIONS, DECISIONS-INDEX, NOW and CLAUDE.md are byte-equal at 7a976cc4 and
9ab24552 (git diff --quiet, exit 0). RESULTS (sha1 90dd5827fa59f504fa0f94a7b61aad46f834d5a1, 12,176 lines) and GAPS (sha1
d608ac714c702ee07218e3d73955d71eecb1d28b, 23 lines) were last changed by the R110 landing commit d056db87 (2026-11-05T20:08:55Z).
Sources read: the packet docs/new/P-IDEAL-KEYS.md (frozen b302bbf5; unchanged at 1a178aff and 06d4238d, by sha1), line L-1 (b302bbf5),
fixes entry 1 and line L-2 (1a178aff); REFEREE successor 24's docs/referee/R-P-IDEAL-KEYS.md (report ece8c4ee, §C cb7e2909; l. 1-176 at
cb7e2909 = the report, by cmp) with scratch/keys_probe.py, keys_check.py, keys_l2_bytetest.py and keys_logs/ (four logs); REFEREE-2
successor 28's docs/referee-2/R2-P-IDEAL-KEYS.md (report ebcf52d0, Addendum 1 87b80d17; l. 1-161 at 87b80d17 = the report, by cmp;
unchanged at 6c6f2033, which touches notes/REFEREE-2.md only) with R2-P-IDEAL-KEYS/r2sim.py, r2lemmas.py and their three outputs;
experiments/new/check.sh at b302bbf5 and 1a178aff; experiments/new/box172/keycheck.py, keycheck.out, box150/check.py and the three
instance files; docs/new/N5-PERMOVER-box165.md, N5-PMKILL-box166.md and N5-PAIRLIN-box169.md (1a178aff, for the three quotes);
notes/L-NEW.md (1a178aff); RESULTS R104 (title l. 9864), R105 (title l. 10155, body items (e) l. 10225-10227 and (h) l. 10236), R110 (l.
11323-11596), Erratum E-2 (l. 11611-11637) and the Dead-ends section (l. 11639-); GAPS l. 11 (R110's UPDATE of 2026-11-05 20:08Z is its
last); DECISIONS L41, L43; docs/agents/LEAD-STATE.md (2026-11-05 22:51Z to 2026-11-06 01:25Z entries); docs/checker/C118.md,
C120.md-C122.md (C122 with Add. 1 and 2) and notes/CHECKER.md (21ff8727); docs/agents/R110-draft.md (the model of this draft,
second-fill version as landed).
Re-runs (scratch, git archive of 1a178aff's experiments/new and docs/new): check.sh block «P-IDEAL-KEYS» (w172 / pin172, l. 911-918),
2026-11-06T01:56:01Z-01:56:04Z, rc 0, PASS line and raw output in w172.out / w172raw.out; my split of keycheck.py's interval and corpus
sets (kcstats.py: keycheck.py unchanged plus recording lines that draw no random number; its first 8 output lines equal keycheck.out);
my own simulator of the three instances (mysim111.py, written from packet §0's text, β-sets compared by the largest rank of the
symmetric difference, no ENC; no lane or referee code imported); the L-1 → L-2 byte test and token diff (wdiff111.py); the premise quote
test (prem111.py); the UPDATE build with 14 controls (upd111.py); the quote sweep and the landing simulation.
TRUNK STATUS (git merge-base --is-ancestor at 02:0xZ): b302bbf5, 1a178aff, 06d4238d, ece8c4ee, cb7e2909, ebcf52d0, 87b80d17, 6c6f2033
and 21ff8727 are ancestors of local trunk 9ab24552 and NOT of origin trunk 7a976cc4; the Lead commits b5d154ad, bc05394a, 7e456b8c,
e7990774 and 7a976cc4, and d056db87, are on both. The Lead pushes trunk before landing. The body makes NO statement about trunk (C113
E-2).
LESSONS APPLIED. C113 E-1: the title is L-2 verbatim with no insertion. C114 Add. 1 E-1: the UPDATE head carries «<DATE>». C115 E-1: the
premise route is checked against what RESULTS records (G-4; every packet quote of RESULTS byte for byte, 1 hit each). C116 G-1, C118 §4,
C120 §4, C121 §4, C122 §4: the UPDATE rule of R105 with R107's step for the DEAD clause, unchanged ((9); one adaptation for the line's
«(DATA, » opening). C116 G-2: name clashes settled by one body sentence (G-6). C117 E-1 / E-2: no sentence wider than signed; DATA
scoped as measured; the instances inlined. C118 E-1 and the brief: no stale status sentence; the entry calls nothing «pending» (the only
«PENDING» is the title fill) and states no other item's status. C118 §3 / Erratum E-2: every DEFINITION in the title line diffed against
the packet and the fixes (G-2). C118 §5: a lane conjecture killed inside a landed line gets no Dead-ends row ((14)). C120 §5 / C121 §5
G-9 RULE: «From the next line on, though, the C118 G-8 advice («name the statements a DATA count covers») is a check item. A line that
leaves it out gets an E-item.» (G-9, with the statements each count covers). C121 / C122 E-2: «DATA whose scope is wider than its
coverage» (G-9 (i)). C122 G-0: parentheses balanced in the title (G-1). C122 E-3: the source note names every proof file (G-1). C119
E-1: every «referee X did Y» is checked against that referee's file (line-precise sweep, Addendum (5)).
to check: FLAGS FIRST (G-0 to G-14; three of them are for the Lead or CHECKER: G-0 (number), G-9 (i)-(ii) (P-1), G-8 (b) (a READING in
the line)), then the CLEAN items and (0)-(14).
- G-0, THE CHECKER NUMBER (FLAG for the Lead). docs/checker/C123.md does not exist at the checker head 21ff8727, and «C123» occurs 0
  times in RESULTS and GAPS; but C123 is already named for another item: notes/CHECKER.md l. 6 «NEXT: C123 = P-TR3 («T^R(3) = 8»,
  L-COMP), when the Lead routes it.», docs/NOW.md l. 96 «idle until C123 (P-TR3)», LEAD-STATE 00:25Z («CHECKER 18
  (session_01V5yGRZJdCaRbBvXAgb1nEA) C123 -> land»). So C123 is not free, and this draft uses the next free number, C124 («C124» 0 times
  in the repository at 9ab24552 before this file, by git grep). If the Lead routes R111 to the CHECKER first and gives it C123, replace
  «C124» by «C123» everywhere in this file (title fill, UPDATE head, GAPS preamble, this flag and the header): a pure substitution, by
  script; nothing else depends on the number.
- G-9, DATA (the C120 §5 / C121 §5 check item): BY THE LETTER, MET; two scope items for CHECKER's ruling (one is REFEREE-2's optional
  P-1) and five precision notes. Every count of L-2's DATA parenthesis names the statement it covers: «LOCAL-KP 0 violations on 27,102
  (state pair, mover) checks» (LOCAL-KP's key half, «they give every option of x the same key»); «for KF_x ≤ WE_x, on 90,811 (run,
  mover) pairs»; «PAIR-KF 0 on 34,113 (run, degree-2 mover of level ≥ 1) pairs»; «CASCADE 0 unclassified of 15,614 flips»; «LADDER's
  first inequality 0 on 231 runs of 𝓛^R genomes»; «RENEW 0 on 520 (step, mover) pairs at the first steps of top-only intervals starting
  at t ≥ 2» (RENEW's clause for the movers of step a); «for the constant keys, on 2,704 intervals»; «MERGE 0 on 19,932 (state, degree-2
  mover) checks»; «RETURN 0 on 722 consecutive move pairs»; «RETURN-COUNT 0 on 50,260 (run, degree-2 mover) pairs»; «flips ≤ T 0 on the
  same runs»; the DEAD items («the two DEAD instances replayed by the same tool and by the box 150 checker»); TOWER's values on
  dd_d5_F14; and the items without DATA: «PAIR-MOVES and the rest of LADDER: no separate DATA». Every count equals my re-run at 1a178aff
  ((10)) and keycheck.out. Items: (i) SCOPE, P-1 (REFEREE-2 Add. 1 l. 185-188, optional, «my miss in the first report»; open; for
  CHECKER): «for the constant keys, on 2,704 intervals» counts keycheck.py's RENEWB, which checks that KP of every top mover is constant
  on [a − 1, b] (keycheck.py l. 173-174, «KP[u][h] != KP[a - 1][h]»), not that every key is; the line's clause is «the keys of every
  mover of level τ are constant on s_(a−1), …, s_b». As written the count names the key form and covers the KP form: the C121 / C122 E-2
  pattern («DATA whose scope is wider than its coverage»), in the weak direction (KP constancy is implied by key constancy). Measured
  (kcstats.py, my recording line on the same runs; DATA of this draft, not lane DATA): every key of every option of every top mover is
  constant on [a − 1, b] on all 2,704 intervals (0 violations); so the full key form also holds on the same set. Both referees' own
  tools check the full key form (REFEREE keys_check.py l. 172-175, RENEWB 3,356 corpus and 669 + 667 random intervals, keys_logs;
  REFEREE-2 r2lemmas.py l. 160, RENEWB 12,501 random and 160 corpus intervals). REFEREE-2's optional rewording: «for the constant key
  preference». Per the brief the line is not changed; CHECKER rules note or E-item. (ii) SCOPE (new; not in either report): the 2,704
  intervals are every top-only interval of the 13,813 runs, 516 with a ≥ 2 and 2,188 with a = 1 (kcstats.out; 516 = keycheck.out's
  «toponly_first 516»), while L-2 states the constant keys inside «if a ≥ 2 then …» (REFEREE §5 l. 144 «The line's RENEW is part (a) at
  a plus part (b), inside «if a ≥ 2»: narrower than signed, fine.»). Packet RENEW (b) (l. 152-153) holds for every top-only interval, so
  no count is false; but 2,188 of the 2,704 intervals lie outside the line's clause, and the line's clause has 516 intervals in the data
  (KP form 0 violations, full key form 0 violations, kcstats.out). Same ruling as (i); one possible wording, not mine to choose (not a
  quotation): "for the constant key preference, on 2,704 top-only intervals (516 starting at t ≥ 2)". (iii) PRECISION, «LADDER's first
  inequality»: in L-2 the LADDER clause lists «F(0) ≤ 2» first and «F(l) ≤ moves(2l) + moves(2l + 1) + F(l − 1)» second; the count is
  for the latter (keycheck.py l. 151-155, for l = 0, …, d − 1 with F(−1) := 0, so at l = 0 it checks F(0) ≤ moves(0) + moves(1), not
  F(0) ≤ 2), as packet §8 l. 260 names it («Corollary LADDER, first inequality only (F(l) ≤ moves(2l) + moves(2l + 1) + F(l − 1))»). Of
  the 231 runs, 58 are of one-level genomes (d = 1, F(0) only), 9, 61, 62, 29, 10 and 2 of d = 2, 3, 4, 5, 6 and 8 (kcstats.out). Note.
  (iv) PRECISION, MERGE: the line states MERGE «at any degree, for two distinct options k, k′ of x»; keycheck.py checks only movers with
  exactly two options, comparing options 0 and 1 (l. 102-109); the unit «(state, degree-2 mover)» says so (W-2 / KY-L4 pattern); within
  the clause's scope, narrower. Note. (v) PRECISION, PAIR-KF: the count checks KF_x = flips(a, b) (or 0 if a = b) per (run, mover) (l.
  146-150); the per-state clause «x key-preferring its option 0 under s iff the current option of a has the smaller key» is not counted
  separately (it implies the count). Note. (vi) PRECISION: «413 in-tree genome files» are 413 files with 384 distinct contents (29
  byte-identical copies, e.g. dd_d5_F14 at box152, box160/ext and box172/inst; my count); «files» is exact. Note. (vii) RENEW's «step a
  − 1 moves a mover of level below τ» has no count (true by maximality; packet proof l. 154) and is not in the «no separate DATA» list.
  Note. Neither referee raised (ii)-(vii) (REFEREE l. 161-162 «DATA: every other count equals §8 and keycheck.out, and is scoped to its
  statement.»; REFEREE-2 l. 144 «DATA: every count names its statement.»).
- G-1, TITLE SHAPE AND SOURCE NOTE: CLEAN (my script). L-2 is one line, 120 «(» / 120 «)», depth never negative, final depth 0 (the C122
  G-0 lesson: met); 0 "|"; one « — », with its own date parenthesis «(2026-11-05)» (the freeze date of L-1, kept by L-2, which was
  written 2026-11-06 00:46Z-00:47Z; precision note), «2026» once; three guillemet pairs, all verbatim quotes (G-8 (c)). The source note
  «(P-IDEAL-KEYS, docs/new/P-IDEAL-KEYS.md with its fixes entry 1, docs/new/P-IDEAL-KEYS-fixes.md; L-NEW successors 54-55)» names both
  proof files (the C122 E-3 lesson): fixes l. 7-8 «the packet and this entry are the only files that carry proofs of the packet's
  statements.»; TOWER is proved in the fixes only (F-a). REFEREE §C l. 220-221 and REFEREE-2 Add. 1 l. 183-184 checked the note. The
  title is "### R111 [refereed-only] " + L-2 + the fill ", CHECKER PASS (docs/checker/C124.md, checker PENDING)" (as R90-R110), nothing
  inserted.
- G-2, DEFINITIONS DIFFED AGAINST THE PACKET AND THE FIXES (the C118 §3 / Erratum E-2 lesson; my own diff, by reading and by script
  where literal). (i) Premise parenthesis: «moves(x) the number of steps t with x ∈ Mv_t as in RESULTS Erratum E-2 (E2c)» = §0 l. 66
  «moves(x) := #{t ∈ [1, T] : x ∈ Mv_t} (the binder of Erratum E-2 (E2c)).» and E-2's correction (RESULTS l. 11628 «Read KEYFLIP's
  moves(x) as the number of steps that move x.»); «R110's definition of 𝓛^R_d» = §0 l. 77-79, the quote of R110 1 hit in RESULTS (l.
  11323). (ii) «Mv_t the movers of step t», «T the number of steps of a run» = §0 l. 60. (iii) «KP_s(x) the option of x with the least
  key under s» = l. 67 (unique by (F1)); «KF_x the number of steps t with KP_(s_t)(x) ≠ KP_(s_(t−1))(x)» = l. 67-68. (iv) «W(x) the
  movers reachable from x along W-targets of any options (x excluded)» = l. 69; «WE_x the number of steps moving a mover of W(x)» = l.
  71. (v) flip: «for two distinct movers p, q of one level a flip of (p, q) at step t a change between s_(t−1) and s_t of the order of
  the keys of their current options» = l. 73-74 (ord_s(p, q) := [key_s(p, s(p)) < key_s(q, s(q))]); «flips(p, q) the number of steps at
  which (p, q) flips» = l. 74. (vi) «v_s(x, k) the integer value of option (x, k) under s (R105 ENC)» = l. 75-76 (the integer Σ ±2^rank
  over Ξ_s(x, k)); «cv_s(x) := v_s(x, s(x))» = l. 76 (the packet adds cv_s(X) := 0; the line uses X only in R(x, k), «(0 if that target
  is the exit X)»). (vii) PAIR-KF's «W-targets a, b of its two options» = l. 97 (a := wt(x, 0), b := wt(x, 1)); the clause «x
  key-preferring its option 0 under s iff the current option of a has the smaller key» is (b) (l. 99, KP_s(x) = 0 iff ord_s(a, b)) and
  is read under «if a ≠ b» (with a = b there is one current option and no comparison; the line drops (a)'s smaller-gate rule: weaker,
  REFEREE-2 l. 136); precision note. (viii) PAIR-MOVES' «such x» = the degree-2 movers of level ≥ 1 of PAIR-KF's clause; «every other
  mover» = the «otherwise» of l. 107. (ix) CASCADE: «their current W-targets w_p ≠ w_q» = l. 120 (wt(p, s_t(p)), wt(q, s_t(q))); the
  line drops «exactly one» (REFEREE l. 145 «CASCADE drops «exactly one»: fine.»). (x) LADDER: «F(l) := flips(2l, 2l + 1)» = l. 79; the
  range 1 ≤ l ≤ d − 1 of l. 133 is implicit; «F(l) ≤ 2 + 3F(l − 1) ≤ 3^(l+1) − 1» = l. 134. (xi) RENEW: «τ the largest level» = l. 80 (τ
  := max_x lev(x)); «a step top-only when all its movers have level τ» = l. 80; «a top-only interval a maximal interval [a, b] of
  top-only steps» = l. 80-81; «step a − 1 moves a mover of level below τ» = LOWER (l. 80, «LOWER otherwise»; Mv_t is nonempty); the
  binder «(A_s(h): h's current option under s and its options strictly better under s)» = §0 l. 56 (A_s(x) := {s(x)} ∪ {k : Ξ_s(x, k) ▷
  Ξ_s(x, s(x))}) and is R105 XI-NEW's own text (1 hit in RESULTS, l. 10155; REFEREE §C l. 216-217); «strict Ξ-descendant» = D(h), l. 72.
  (xii) MERGE: «the movers of the two chains before their first common mover» = Pre_k ∪ Pre_k′ of l. 169-172 (letters k, k′ in the line,
  fixes F-f); «depends only on» = (b) l. 174-175. (xiii) RETURN: «R(x, k) the number of steps at which cv of the Ξ-target of (x, k)
  rises (0 if that target is the exit X)» = l. 195-196. (xiv) TOWER: «a run in which the doubling step of box 169, «F(l) = 2(1 + F(l −
  1))» iterated level after level, reaches F(l) = 2^(l+1) − 2» = fixes F-a l. 17-19 («Let a run have a pair that flips F(l) = 2^(l+1) −
  2 times (the value that the doubling step of box 169, «F(l) = 2(1 + F(l − 1))» …, gives when iterated from F(0) = 2)»); the line's
  F(l) is LADDER's (𝓛^R_d), F-a also covers «any pair a tower designates at level l» (l. 18); narrower or equal (REFEREE-2 Add. 1 l. 183
  «The TOWER clause (R3) is no stronger than F-a, read over 𝓛^R_d's F(l) or over any pair.»). (xv) DEAD: «desc(x) the number of strict
  Ξ-descendants of x» = l. 72; «VR(z) the number of steps at which cv(z) rises» = §7 (b) l. 225-226; PM's universe «for every mover x»
  (fixes F-c: «stated there for every IDEAL-ACYC genome, every start and every mover x») is read with the line's frame («In the IDEAL
  model … on acyclic Ξ-graphs»), as REFEREE-2 l. 151-152 worded it (W-3). ALL EQUAL, with the precision notes (vii), (x), (xiv), (xv).
  Both referees diffed every definition of L-1 (REFEREE l. 140-142 «Definitions diffed against §0:»; REFEREE-2 l. 134-135 «Definitions
  diffed against packet §0:»), and on L-2 REFEREE l. 222 «Definitions: unchanged from L-1 except MERGE's k, k′, all as diffed in §5.».
- G-3, STRICT SYMBOL TEST (notes). (i) x, p, q, k, k′, s, t, h, w, o, z, l, a, b are bound in their clauses; «a, b» are PAIR-KF's
  W-targets and, in RENEW, the interval [a, b] (two scopes; KY-L2 removed the third use, MERGE's); «o» in RETURN is the option x moves
  to at t_1. (ii) «d» is free in 𝓛^R_d (LADDER «on 𝓛^R_d»); LADDER holds for d ≥ 1 (packet l. 132). (iii) «N» in PAIR-MOVES is the
  number of movers (§0 l. 47); «T» is bound in the definitions. (iv) «the doubling step of box 169» is a lane formula, quoted with its
  source; F(l) is LADDER's. (v) «KILL_PM_compose_dd_d5_F14.json», «dd_d5_F14», «c025a4b6…», «06f0e501…» are data files with paths and
  abbreviated sha1s. (vi) «L-RED's 𝓛^R_5 genome»: an attribution, prefixed. None is a free quantifier of a claim clause.
- G-4, PREMISE ROUTE (the C115 E-1 class): CLEAN (my check, prem111.py). L-2's premise parenthesis: «premise: R104's definition of the
  model only, no theorem of R104 used; RESULTS R105's ENC, MONO, XI-NEW and RISE, and at degree ≤ 2 its KEYFLIP, read with moves(x) the
  number of steps t with x ∈ Mv_t as in RESULTS Erratum E-2 (E2c); and RESULTS R110's definition of 𝓛^R_d only». Every packet quote of
  RESULTS (packet l. 24-41), tested as a substring of RESULTS with whitespace normalised, occurs exactly once: ENC, MONO, XI-NEW (with
  its binder), RISE, KEYFLIP and «KP_s(x) the key-preferred option under the keys of s» in R105's title (l. 10155); body item (e) (a),
  (b), (c) at l. 10225-10227; (E2c) at l. 11617-11618; R110's definition of 𝓛^R_d in R110's title (l. 11323). REFEREE l. 28-34 (trunk
  b5d154ad, «Each is FOUND exactly once»); REFEREE-2 l. 33-36 («all FOUND»). R105 states ENC, MONO, XI-NEW and RISE «at any degree» and
  KEYFLIP «at degree ≤ 2 only» (both in l. 10155); the packet uses KEYFLIP only in PAIR-MOVES (every mover of degree ≤ 2) and LADDER
  (𝓛^R_d, all degree 2). Use: ENC in MERGE, RETURN and v_s; MONO in RETURN; XI-NEW and RISE (body item (e)) in RENEW (a); KEYFLIP in
  PAIR-MOVES and LADDER; R110's 𝓛^R_d in LADDER and in naming the PMV instance's class; R104's definition everywhere (packet §0, a
  restatement checked by both referees: REFEREE-2 l. 28-32 against RESULTS l. 9864). Not used: packet l. 42-43 «Not used: R105's LOCAL,
  CHAIN-BACK, U-EQ, DECREMENT, EXACT-ENERGY, TOP-MONO, RANK-BOUND, INTERVAL-RESTRICT, INTERVAL-CHARGE, RECURSION; R106-R109; docs/lit,
  docs/sources; any other lane file; no outside source.»; REFEREE l. 41 «Not used: R105 LOCAL (LOCAL-KP is proved from the definition);
  no docs/lit, no lane file, no machine premise.»; REFEREE-2 l. 44-45. No unlanded result, no lit note, no lane file and no machine
  premise is a premise of a signed statement; the lane files box 165, 166 and 169 are quoted only as the sources of the refuted
  conjectures and of the doubling step.
- G-5, RESULTS ERRATUM E-2 TO R105 BEARS AND IS APPLIED (note). E-2 (RESULTS l. 11611-11637) corrects three R105 definitions. (E2c)
  (KEYFLIP's moves(x)) bears on PAIR-MOVES and LADDER; the packet uses exactly the corrected binder (§0 l. 66; premise l. 38-40) and the
  line states it («read with moves(x) the number of steps t with x ∈ Mv_t as in RESULTS Erratum E-2 (E2c)»). (E2a) (CHAIN-BACK's
  «chained») and (E2b) (TOP-MONO's RANK_t) concern items the packet does not use (premise l. 39-40, 42). ENC, MONO, XI-NEW, RISE: E-2
  «Unaffected: R105's other definitions». KF_x: packet l. 67-68 reads R105's «number of steps at which KP(x) changes» as #{t :
  KP_(s_t)(x) ≠ KP_(s_(t−1))(x)}; REFEREE l. 37-38 checked it against P-IDEAL-RED §5 (l-new 0ebddcf5), REFEREE-2 l. 38-39 against R105
  body item (h) (l. 10236). Both referees: E-2 applied correctly (REFEREE l. 35-40; REFEREE-2 l. 40-42).
- G-6, NAMES, SAME LABELS, OTHER MEANINGS (by script on RESULTS 90dd5827 / GAPS d608ac71; note; C116 G-2's remedy). 0 times in RESULTS
  and GAPS: «P-IDEAL-KEYS», «LOCAL-KP», «PAIR-KF», «PAIR-MOVES», «CASCADE», «RENEW», «RETURN-COUNT», «TOWER», «PMV», «PAIR-LIN»,
  «PM′_S», «RENEW-COUNT», «keycheck», «KILL_PM», «T1_dd_top8», «WE_x», «F(l)», «desc(x)», «R(x, k)», «top-only», «KY-1», «KY-G1»,
  «C124», «DE37». Same names, other meanings: (a) «R111» twice in RESULTS (R86, l. 5393-5394: «L-RED's R111 (claude/l-red 463bec6e, …»,
  an L-RED box); (b) «LADDER» in R106 (LADDER-LP, the genome L_K) and DE36; (c) «MERGE» in R37 and R67 (other lemmas, «MERGE SIGNED WITH
  GAP RL-2», «MERGE-B»); (d) «RETURN» in R12, R73, R76, R86, R89, R90, R93, R95, R96, R98 (SW-RETURN and the RETURN pairs of epochs);
  (e) «W(x)» in R67, R76, R88, R92, R96, R97, R100, R103, R104 and DE34 (other W-objects); (f) «τ» 1,354 times (N5's strategy τ); (g)
  «flips(» and «doubling» once each in DE35 (Gflips, R87's doubling family); (h) «PM» once (R75, a count label «PM 422»); (i) referee
  labels «W-1», «W-3», «R-1», «P-1» occur in RESULTS with other referees' meanings. Consistent: «KF_x», «KP_s(x)», «Mv_t» as in R105 and
  R107-R109; «dd_d5_F14» is R109's LIFT champion (RESULTS l. 11030, 11236), the same genome (box152/dd_d5_F14.json,
  box160/ext/dd_d5_F14.json and box172/inst/dd_d5_F14.json all have sha1 06f0e501…). Applied: one body sentence, Honest limits (ix). No
  line change.
- G-7, L41 (the C109 E-1 class): not triggered (my reading; POINT TO CHECK). L-2 contains «referee-originated» 0 and «lane-authored» 0
  times. The packet's proofs are L-NEW successors 54-55's (packet l. 7 «Labels: PROVED (L-NEW 54/55, unrefereed)»). TOWER's statement is
  the implication REFEREE wrote in its refusal (l. 100-101 «What IS proved, and I sign it: «a run in which the tower reaches F(l) =
  2^(l+1) − 2 at level l has T ≥ 2^(l+1) − 2» (Corollary F ≤ T).») and REFEREE-2's R-1 scope (l. 98-103); the lane wrote it out with its
  one-line proof in fixes F-a (l. 17-21, «Proof. Corollary F ≤ T (signed by both): flips(p, q) ≤ T for every pair of every run. ∎»), and
  both signed that text (REFEREE §C l. 187, REFEREE-2 Add. 1 l. 169). The proof step is the already signed Corollary F ≤ T; no
  referee-written proof enters. The body credits the referees (Fixes).
- G-8, DEADS, L43 AND THE READING IN THE LINE. (a) L43 (DECISIONS l. 369-374, «needs a refereed proof, or one instance exceeding an
  EXPLICIT bound»): PM and PMV are explicit bounds with no unspecified constant, and each instance exceeds its bound (moves(12) = 6 > (2
  − 1)(1 + 4) = 5; VR(6) = 10 > 1 + 7 = 8), recomputed by both referees with their own simulators (REFEREE §3 l. 109-117, t3r_sim.py;
  REFEREE-2 l. 88-94, r2sim.py) and by mine (mysim111.out). CLEAN. The doubling-tower step was REFUSED as DEAD by REFEREE under L43 (l.
  99 «Under L43 a DEAD needs a refuted statement (by instance or proof); here there is none.»), REFEREE-2 withdrew its DEAD sign (Add. 1
  l. 173), and L-2 states it as TOWER, an implication, under no DEAD label. CLEAN. (b) A READING INSIDE THE LINE (NOTE, POINT FOR
  CHECKER): the TOWER clause ends «(a READING, not a refutation: the doubling tower is not a shortcut around G-N5-TIME)»; the packet's
  convention is «READING (not to sign)» (packet l. 7-8; fixes l. 22 «READING (not to sign): the doubling tower is NOT A SHORTCUT.»). The
  parenthesis labels itself, its content is the signed implication read in words (exponential flips need exponential T in the same run),
  and both referees MATCHED L-2 with it (REFEREE §C l. 218-219; REFEREE-2 Add. 1 l. 181-184). R110's line carried an unsigned reading in
  its scope tail («a REDUCTION of the W-channel part of SLOT-TRADE …»), not inside a claim clause; this is the first labelled READING
  inside a claim clause (my reading; note). (c) The C120 «…» note: L-2's three «…» are verbatim quotes, checked: «moves(x) ≤ (deg(x) −
  1)(1 + desc(x))» = docs/new/N5-PERMOVER-box165.md l. 1 (title); «VR(z) ≤ 1 + desc(z)» = N5-PMKILL-box166.md l. 41; «F(l) = 2(1 + F(l −
  1))» = N5-PAIRLIN-box169.md l. 26 (all at 1a178aff; REFEREE §C l. 212-215; REFEREE-2 Add. 1 l. 176-177). «polynomially» once in L-2
  («bounds nothing polynomially (LADDER's bound is exponential)»); «linear» 0; «O(» 0.
- G-10, LEAD READINGS AND RULINGS AS ON FILE (the C111 E-1 class): CLEAN. L-2 cites no Lead reading and no ruling (by script: «Lead
  reading» 0, «L41» 0, «L43» 0, «D1» 0). The lane works under D14 / D18 / D20 (packet l. 2). The freeze brief (packet l. 2 «Lead brief
  BOX 172 (2026-11-05): «freeze packet P-IDEAL-KEYS for the referees»»; Lead commit bc05394a, 22:51:15Z, «Lead: L-NEW 54 parked (box 171
  RENEW), L-NEW 55 started (P-IDEAL-KEYS freeze); I/L measure to L-RED 50; sweep 22:03Z; log»). Routing to the referees: Lead commit
  7e456b8c (23:54:59Z). Fix round: fixes l. 3 «Lead relay 00:47Z of fix round 1» against the lane commit 1a178aff (00:47:11Z) and the
  Lead's log commit e7990774 (00:55:38Z); the relay itself is a message, not verifiable from the repository (D-2). L-2 to the referees:
  Lead commit 7a976cc4 (01:25:28Z).
- G-11, STALE LANE AND LOG TEXT (notes; nothing here lands). (i) Packet l. 1 (title) and l. 19 (table) say «DEAD: PM, PMV and the
  doubling-tower step»; fixes F-a replaces §7 (c) and the table row. (ii) Packet §7 (b) l. 234 «(it is 7 = 1 + desc(6))» is false
  arithmetic (1 + desc(6) = 8), corrected by F-b (KY-1). (iii) Packet §7 (a), (b) guillemet texts are restatements; F-c makes them
  verbatim. (iv) §7 (c) l. 242-243 «top mover with 8 moves» (mover 10 has level 4; τ = 5): F-d. (v) §4 l. 142 «(it is tight at level 3
  of one instance, §7 (c))»: true of the second inequality only, F-e (N-1). (vi) The packet has no §1 (sections §0, §2-§8); the
  numbering is the lane's. (vii) Packet §7 (a) l. 221-222 «L-RED replayed the instance independently (reported in the Lead brief of BOX
  172; not re-checked here)» is not verifiable from the repository (D-3). (viii) notes/L-NEW.md (1a178aff) l. 9 «DEAD: … doubling-tower
  step» (the freeze summary) and l. 49 «doubling tower DEAD as stated» (box 170) predate F-a; l. 15-16 record the relabel. (ix) Lead log
  subjects b5d154ad «tower DEAD (L-NEW box 170)» and LEAD-STATE 00:25Z «Dead today: PM, PMV, INF-2, per-bit W_c, SUM_3, tower, …»
  predate the fix round; they are logs, not truth (CLAUDE.md). The entry says only what L-2 says.
- G-12, SHA1 PINS IN check.sh (the C110 F-1 / C116 G-3 class): present. experiments/new/check.sh at b302bbf5 (919 lines, sha1
  628da239f7bcd5531fc6c4e35d6ce22fbddc9d3b) adds block «P-IDEAL-KEYS» (l. 911-918: keycheck.py output compared with the frozen
  keycheck.out, the box 150 checker on the three instances, pin172 of the packet, L-1, keycheck.py, keycheck.out and the three
  instances); 1a178aff (919 lines, sha1 063b005b7f9c60f4e704bde92cdfa762e3675bf5) extends pin172 by the fixes 26088848 and L-2 fb1b2276
  (l. 913-915 changed; PASS line «… fixes 26088848, line L-2 fb1b2276: PASS»). Re-run at this fill from the archive of 1a178aff: PASS
  ((10)).
- G-13, THE REFEREES' ROUNDS (note). L-1 (f36c6402): REFEREE (ece8c4ee) SIGN §2-§6 and DEAD PM; DEAD PMV «SIGN WITH GAP KY-1»; the tower
  «REFUSE as DEAD (KY-G1)»; line «NOT YET: REQUIRED KY-L1 (tower clause under DEAD); optional KY-L2-L4» (l. 11-25). REFEREE-2 (ebcf52d0)
  SIGN all, the tower «in the scope stated in R-1»; line «**MATCHES** after the exact word changes W-1 to W-3» (l. 12-25). Fix round
  (fixes entry 1, L-2): F-a (TOWER) answers KY-G1, KY-L1, R-1; F-b KY-1; F-c F-1, KY-P1, KY-L3; F-d F-2, KY-P2; F-e N-1; F-f KY-L2;
  R1-R10 make L-2 (fixes l. 100). L-2 (fb1b2276): REFEREE §C (cb7e2909) «L-2 MATCHES.» (l. 224) after a byte test (l. 208-211), every
  item SIGNED (l. 225); REFEREE-2 Add. 1 (87b80d17) «**Line L-2: MATCHES.**» (l. 181) after a byte test, TOWER SIGN, DEAD sign on the
  tower withdrawn (l. 169-173), optional P-1 (G-9 (i)).
- G-14, THE FIXES FILE CARRIES SIGNED CONTENT (note). TOWER (fixes F-a, l. 17-21) is a new signed statement proved in
  docs/new/P-IDEAL-KEYS-fixes.md, not in the frozen packet; both referees signed it in their second rounds. The other fixes change
  packet text only (F-b to F-e) or the line's letters (F-f). The entry lists TOWER as signed with its source (Claims (i)); the source
  note names the fixes file (G-1).
- CLEAN AT L-2 (the pre-check against CHECKER's recurring items, by script on fb1b2276):
  C106 E-1 (old line as current): L-2 is the current line; no L-3 exists (docs/new/P-IDEAL-KEYS-line-L3.txt absent at the l-new head
  06d4238d); L-1 appears only in the line history.
  C113 E-1 (title «verbatim» after an insertion): no insertion; the title is byte-equal to prefix + L-2 + fill (Addendum (2)).
  C113 E-2 (trunk status that goes stale): the body has no trunk statement (header).
  C114 Add. 1 E-1 (UPDATE date): <DATE> placeholder.
  C115 E-1 (premise route): G-4, G-5.
  C110 F-1 / C116 G-3 (pins): G-12.
  C111 E-1 (stale Lead-reading statements): G-10.
  C116 G-2 (name clash): G-6, one body sentence.
  C117 E-1 (a sentence wider than signed; DATA scope): G-2, G-9; the body's Data sentences give each count's genome set and unit.
  C117 E-2 (instance under-specified): the body inlines the PM instance (every option field, the start, the fifteen states) and the PMV
  instance (= movers 0-9, its start and run) with full sha1s, paths and commits.
  C118 E-1 (stale status sentence): no «pending» in the entry; no other item's status is stated (no P-TR3, no SC-ISO, no box 173-175).
  C118 §3 / Erratum E-2 lesson (definitions diffed): G-2.
  C120 §5 G-9 / C121 E-1 / C122 E-2 (DATA count without its statements; scope wider than coverage): MET by the letter; G-9 (i), (ii) for
  CHECKER's ruling.
  C120 §3 note («…» that is not a quotation): CLEAN, G-8 (c).
  C122 G-0 (parentheses): 120 / 120 in L-2, depth never negative (G-1).
  C122 E-3 (source note): CLEAN (G-1).
  «|»: 0 in L-2, 0 in the entry block, 0 in the UPDATE (by script, Addendum (3)).
(0) PLACEMENT. R111 goes DIRECTLY AFTER R110's block. docs/RESULTS.md at local trunk 9ab24552 (= origin trunk 7a976cc4 for this file)
has sha1 90dd5827fa59f504fa0f94a7b61aad46f834d5a1, 12,176 lines (wc -l), last changed by d056db87 (R110's landing). «### R110» is l.
11323 (entry l. 11323-11596, l. 11597 blank); «**Erratum E-1**» is l. 11598; «**Erratum E-2**» is l. 11611; «## Dead ends (kept;» is l.
11639; DE36 begins at l. 12160. PROPOSED (R102's to R110's layout): insert R111's entry after l. 11597 (R110's blank line), with one
blank line after it, so the R-entries stay contiguous and both errata follow them. "### R111" occurs 0 times in RESULTS and GAPS; «R111»
twice in RESULTS, both L-RED's box (G-6 (a)). GAPS has sha1 d608ac714c702ee07218e3d73955d71eecb1d28b, 23 lines, last changed by
d056db87. The Lead re-checks (6) and (9) at landing only if RESULTS or GAPS change after d056db87. R110's own landing followed its
draft's simulation exactly (C122 Add. 2).
(1) TITLE. The title is the line file docs/new/P-IDEAL-KEYS-line-L2.txt (l-new 1a178affc45733577e2f2db0aa1b74f19aa7e244,
2026-11-06T00:47:11Z, the file's only commit, sha1 fb1b22763f5cc5e64fa2cab78468718b1321a846; unchanged at the l-new head 06d4238d),
verbatim: one line, no outer quotes, no final period, 5,395 characters (5,541 bytes plus the newline), 1,037 whitespace tokens, 120 «(»
/ 120 «)» (depth never negative, final 0), three guillemet pairs and three «…». NO HEADING MARKER, verified by script: the file begins
«In the IDEAL model of RESULTS R104», with no «#». NOTHING is stripped and NOTHING is inserted: the heading is the level-3 marker, then
"R111 [refereed-only] ", then the file without its newline, then the fill ", CHECKER PASS (docs/checker/C124.md, checker PENDING)" (as
R90-R110; C124, not C123: G-0). L-2 holds one « — », its own date parenthesis «(2026-11-05)» and no "|" (G-1). Built by script
(fill111.py: assert the sha1 fb1b2276…, equality with the blob at 1a178aff and at the l-new head, one line, no marker, one «
(2026-11-05) — », no "|"; prepend, append) and re-checked after writing this file: equal, byte for byte. Heading: 5,474 characters,
5,620 bytes; sha1 of the heading line without its newline d612228740521569a7a3f218923af627291453d8; it is l. 439 and the only «### R» line of this file.
(2) LINE HISTORY: two lines. L-1 f36c6402064f61511048887bde28a72e270382ee (b302bbf5, frozen with the packet, the file's only commit;
5,187 bytes, 977 tokens, 111 «(» / 111 «)»): REFEREE NOT YET (KY-L1), REFEREE-2 MATCHES after W-1 to W-3 (G-13). L-2
fb1b22763f5cc5e64fa2cab78468718b1321a846 (1a178aff; 5,542 bytes, 1,037 tokens): fixes entry 1 lists ten replacements R1-R10 (fixes l.
59-69) and their word diff (l. 70-99); my byte test (wdiff111.py: R1-R10 parsed from the fixes file with nested guillemets, each old
string once in L-1 when applied in order, each new string once in L-2) gives L-1 with R1-R10 = L-2 byte for byte (True); my token diff
(difflib on whitespace tokens) finds 16 non-equal hunks (83 tokens out, 143 in), all inside R1-R10. Both referees byte-tested L-2 the
same way (REFEREE §C l. 209-211 «EQUAL to L-2 (sha1 fb1b2276…, 5,542 bytes).»; REFEREE-2 Add. 1 l. 181-182 «applying them in order to
L-1 gives a string byte-identical to L-2 (5,542 B).»). No hunk changes a definition except MERGE's letters (R2); R3, R6 and R9 move the
tower out of DEAD (TOWER, a READING, and its values as DATA); R1 adds a binder; R4, R5 make two quotes verbatim; R7, R8 narrow two DATA
units; R10 names the fixes file. So the title is L-2, and L-1 is history.
(3) THE LINE AT BOTH REFEREES. REFEREE successor 24, docs/referee/R-P-IDEAL-KEYS.md: report ece8c4ee (2026-11-05T23:49:08Z, new file,
176 lines, sha1 55cf771dda81da770736e4098e6d6038d9479f0f), §C cb7e2909 (2026-11-06T01:26:42Z, 226 lines, sha1
80d291030b66e05e68141f8b630ec8a7940b1dac): l. 224 «L-2 MATCHES.». REFEREE-2 successor 28, docs/referee-2/R2-P-IDEAL-KEYS.md: report
ebcf52d0 (2026-11-05T23:51:25Z, new file, 161 lines, sha1 5156ea45aba4d865ef976de3f1c2da53b844cffd): L-1 «**MATCHES** after the exact
word changes W-1 to W-3»; Addendum 1 87b80d17 (2026-11-06T01:26:59Z, 189 lines, sha1 493871a6b2502eee6f3c6e17506dcaeb5866865c; unchanged
at 6c6f2033): l. 181 «**Line L-2: MATCHES.**». Both MATCH L-2.
(4) CLAIMS SIGNED = the items below, each SIGN in BOTH referees' final verdicts (REFEREE "## 0. Verdicts" l. 11-25 and §C l. 187-226;
REFEREE-2 "## Verdicts" l. 12-25 and Addendum 1 l. 168-184), checked clause by clause against the packet and the fixes; the cells are
the reports' words:
| item (source) | REFEREE (successor 24) | REFEREE-2 (successor 28) |
| --- | --- | --- |
| (a) Lemma LOCAL-KP (a), (b) (packet §2 l. 83-94) | l. 14 «SIGN» | l. 15 «**SIGN** (Opus 5.5, D12)» |
| (b) Lemma PAIR-KF (a), (b) (§3 l. 96-105) | l. 15 «SIGN» | l. 16 «**SIGN** (Opus 5.5, D12)» |
| (c) Corollary PAIR-MOVES (§3 l. 106-113) | l. 16 «SIGN (KEYFLIP read with the E-2 (E2c) binder, correctly)» | l. 16 (the same row) |
| (d) Lemma CASCADE (a), (b) and Corollary F ≤ T (§4 l. 115-131) | l. 17 «SIGN» | l. 17 «**SIGN** (Opus 5.5, D12) (N-1 on a «Does NOT claim» remark)» |
| (e) Corollary LADDER (§4 l. 132-143) | l. 17 (the same row) | l. 17 (the same row) |
| (f) Lemma RENEW (a), (b) (§5 l. 145-166) | l. 18 «SIGN» | l. 18 «**SIGN** (Opus 5.5, D12)» |
| (g) Lemma MERGE (a), (b) (§6 l. 169-185) | l. 19 «SIGN» | l. 19 «**SIGN** (Opus 5.5, D12)» |
| (h) Lemma RETURN, Corollary RETURN-COUNT (§6 l. 186-202) | l. 20 «SIGN» | l. 20 «**SIGN** (Opus 5.5, D12)» |
| (i) TOWER (fixes F-a l. 10-28; replaces §7 (c)) | l. 23 tower «REFUSE as DEAD (KY-G1)», the implication signed; §C l. 187 «F-a: SIGN TOWER as restated.» | l. 23 DEAD «**SIGN** (Opus 5.5, D12), in the scope stated in R-1»; Add. 1 l. 169 «F-a TOWER: **SIGN** (Opus 5.5, D12).», l. 173 the DEAD sign withdrawn |
| (j) DEAD PM (§7 (a) l. 205-224; F-c) | l. 21 «SIGN» | l. 21 «**SIGN** (Opus 5.5, D12) (F-1: quote not verbatim)» |
| (k) DEAD PMV (§7 (b) l. 225-234; F-b, F-c) | l. 22 «SIGN WITH GAP KY-1»; §C l. 196 «F-b: KY-1 CLOSED.» | l. 22 «**SIGN** (Opus 5.5, D12) (F-1: quote not verbatim)»; Add. 1 l. 174-175 (F-b correct) |
Both, verbatim: REFEREE §C l. 225 «Every item is now SIGNED: §2-§6, DEAD PM, DEAD PMV (KY-1 closed), and TOWER (as restated in F-a).»,
l. 226 «Open items of mine: none.»; REFEREE-2 l. 25 «No statement is REFUSED. No gap is listed: every proof is complete from the landed
premises and the definition.», Add. 1 l. 168 «**Fixes entry 1: CORRECT.**». No gap is open at either referee.
Clause checks (L-2 against the packet and fixes; G-2): LOCAL-KP = l. 85-86; PAIR-KF = l. 98-99; PAIR-MOVES = l. 106-108; CASCADE = l.
117-121 and F ≤ T l. 129; LADDER = l. 133-134; RENEW = (a) at a (l. 147-150; (iii) as «some strict Ξ-descendant of h … moving at step a
− 1») and (b) (l. 152), inside «if a ≥ 2» (narrower); MERGE = (b) l. 174-175; RETURN = l. 187-188 and RETURN-COUNT l. 195-196; TOWER =
F-a; DEAD PM = §7 (a) with F-c; DEAD PMV = §7 (b) with F-c. Nothing in L-2 is wider than signed (G-2 (vii), (xiv), (xv) are precision
notes).
Signed by both, NOT stated by L-2 as separate items: CASCADE's «exactly one» (l. 118); PAIR-KF (a)'s smaller-gate rule (l. 98); RENEW
(a) for every top-only step t ≥ 2 (l. 151) and RENEW (b) for intervals starting at a = 1 (l. 152); MERGE (a)'s explicit difference (l.
173) and the Ξ-order consequence of (b) (l. 175); F(l) ≤ T inside LADDER (l. 134; stated by CASCADE's «flips(p, q) ≤ T»). Not signed, so
NOT landed: packet §8 (DATA, machine checks, EXCLUDED, TARGET diff, READING; «DATA / READING (not to sign)», l. 20); RENEW's «Reading of
(a)+(b)» (l. 160-163); the READING of F-a (l. 22-23; the line labels its own wording «a READING», G-8 (b)); the DATA of F-a (l. 24-27);
the CONJECTURES PAIR-LIN, PAIR-POLY, PM′_S, RENEW-COUNT, SLOT-TRADE (l. 112, 164, 274).
(5) OTHER TEXTS THE ENTRY DEPENDS ON: RESULTS R104's definition of the IDEAL model (title l. 9864; no R104 theorem); RESULTS R105's ENC,
MONO, XI-NEW, RISE (with body item (e)) and KEYFLIP (title l. 10155), read with Erratum E-2 (E2c); RESULTS R110's definition of 𝓛^R_d
(title l. 11323). Nothing else for a signed statement. The lane sources docs/new/N5-PERMOVER-box165.md to N5-FROZEN-box171.md (packet l.
4-6) are history only, except the three quoted formulas (G-8 (c)); the DEAD instances are data files ((10)).
(6) PREMISE LABELS (stale-label test; RESULTS and GAPS at d056db87's version). RESULTS labels in L-2 (by script): «R104» 3 («RESULTS
R104», «R104's definition», «theorem of R104»); «R105» 2 («RESULTS R105's ENC», «(R105 ENC)»); «R110» 1 («RESULTS R110's definition of
𝓛^R_d only»); «Erratum E-2 (E2c)» 1. R104 (l. 9864) exists and carries the definition. R105 (l. 10155) exists and carries ENC, MONO,
XI-NEW, RISE and KEYFLIP; Erratum E-2 (l. 11611) governs the reading of KEYFLIP's moves(x), which L-2 applies; no other erratum touches
R104, R105 or R110 (E-1: R97-R100 counts). R110 (l. 11323) exists and carries 𝓛^R_d. No Lead reading and no other RESULTS label is
cited. G-N5-TIME open (GAPS l. 11).
(7) SYMBOL TEST of the title (my own strict test of every symbol of L-2; IN = bound in the line; else the carrier):
| symbol | where |
| --- | --- |
| IDEAL model, Ξ-graph, acyclic, mover, level, option, W-target, Ξ-target, gate, key, step, run, start, state, chain, Ξ-descendant | RESULTS R104 (the premise; packet §0) |
| ENC, MONO, XI-NEW, RISE, KEYFLIP, A_s(h) | RESULTS R105 (the premise; G-4), KEYFLIP's moves(x) per Erratum E-2 (E2c) |
| 𝓛^R_d | RESULTS R110's definition (G-4) |
| Mv_t, T, KP_s(x), KF_x, W(x), WE_x, flip, flips(p, q), v_s, cv_s, moves(x), F(l), τ, top-only, top-only interval, R(x, k), desc(x), VR(z), w_p, w_q | IN |
| a, b, k, k′, o, t_1, t_2, z, h, w, l, d, N | bound in their clauses (G-3) |
| the doubling step of box 169 | a lane formula, quoted verbatim (G-8 (c)) |
| KILL_PM_compose_dd_d5_F14.json, dd_d5_F14, sha1s | data objects ((10); body Claims (j), (k)) |
| L-RED's 𝓛^R_5 genome | attribution, prefixed |
| CONJECTURES PAIR-LIN, PM′_S, RENEW-COUNT | named as not claimed (packet l. 112, 164; §8 l. 274) |
| DATA clause | per statement (G-9) |
Agreeing tests: REFEREE §5 l. 138-165 and §C l. 208-226; REFEREE-2 l. 133-156 and Add. 1 l. 181-188.
(8) FIXES AND STATUS NOTES (docs/new/P-IDEAL-KEYS-fixes.md, L-NEW successor 55, append-only, one entry, one commit): at 1a178aff sha1
26088848b6a80621fb46a4887be0b2b8ad2a8ebc, 100 lines. Header l. 1 («(append-only; the packet docs/new/P-IDEAL-KEYS.md, sha1 62b35bf7…,
stays frozen)»). Entry 1 (l. 3-100): reports answered (l. 4-6); F-a TOWER (l. 10-28; KY-G1, KY-L1, R-1); F-b (l. 30-32; KY-1); F-c (l.
34-39; F-1, KY-P1, KY-L3); F-d (l. 41-43; F-2, KY-P2); F-e (l. 45-47; N-1); F-f (l. 49-51; KY-L2); the W-2 / KY-L4 counts (l. 53-55);
line L-2 with R1-R10 and the word diff (l. 57-99); l. 100 «Verdict items closed by L-2: KY-L1 (R3, R6, R9), W-1 (R1), W-2 = KY-L4 (R7,
R8), W-3 = KY-L3 (R4, R5), source note (R10), KY-L2 (R2).». The packet file itself is unchanged since b302bbf5 (sha1 62b35bf7… at
b302bbf5, 1a178aff and 06d4238d).
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-2 states no CONJECTURE as claimed and kills nothing of RESULTS or GAPS (PM, PMV,
PAIR-LIN, PM′_S, RENEW-COUNT occur 0 times there). A line-11 UPDATE is proposed at the end, to go AFTER R110's UPDATE (GAPS at d056db87:
the last UPDATE on l. 11 is R110's «UPDATE 2026-11-05 20:08Z: RESULTS R110 (P-IDEAL-FLIP; CHECKER C122 32f65fe0) [refereed-only] LANDED:
…», ending «G-N5-TIME stays open.» before the row's closing « |»; l. 11 holds 76 "|" and 45 «UPDATE 2026-»), as a pure insertion with
one separating space. BUILT FROM L-2 (scratch upd111.py = upd110b.py l. 1-212 unchanged (build() of upd100L3.py, the R97-R109 controls),
plus R110's control, plus R111). CONTROLS (same script, same run, rc 0): R97's to R110's LANDED UPDATEs (GAPS l. 11 at d056db87) rebuilt
from their lines byte for byte (True ×14; R110's from P-IDEAL-FLIP L-3 at 47b4e165 with head «UPDATE 2026-11-05 20:08Z: RESULTS R110
(P-IDEAL-FLIP; CHECKER C122 32f65fe0) [refereed-only] », 4,749 bytes filled, also equal to R110-draft l. 772 and to r110/upd110L3.txt
with <DATE> 2026-11-05, <HH:MM> 20:08, <checker> 32f65fe0). R111: the R107 / R108 / R109 procedure: L-2's claim body ends with the
unlabelled clause «; and DEAD: the lane conjecture PM … and 10 rises)» after the last labelled clause (TOWER); the procedure runs on L-2
with that clause cut out (build()'s label move on the claim body plus a sentinel tail, start «and cv_s(x) := v_s(x, s(x)): », 9 labels,
each found once after it, in order; « (2026-11-05) — » → «: »; the DATA parenthesis before the source parenthesis opened as «; DATA, …»;
«; G-N5-TIME stays OPEN» and «; not M3, not a step-4 pass, not a TARGET.md claim» dropped; the source parenthesis kept; «. G-N5-TIME
stays open.» appended), and the clause is put back verbatim between the moved «(TOWER, by flips ≤ T)» and the tail's «: » (one
occurrence, by script). ONE ADAPTATION: L-2's DATA parenthesis opens «(DATA, » where R105-R110's opened «(DATA: »; sentinel_build's
start test is widened to «(DATA, » (one assertion; nothing else changes), and the result is cross-checked against a direct opening of
the DATA parenthesis (drop its «(» and its closing «)»): equal (True). R104's landed UPDATE already carries «; DATA, » (GAPS l. 11).
Labels with inner «; »: none of the nine clauses has one, so build()'s cut at the last «; » before the next label is exact. L-2 holds no
"|", so no replacement list. Checked by script: one line, 0 "|", one «<DATE>», one «<HH:MM>», one «<checker>», 5,575 bytes, 1,036
tokens, 119 «(» / 119 «)», balanced; «2026-11-05» 0 times; token multiset diff against L-2 = the head, the nine moved labels, «(DATA,»
opened, the two dropped scope sentences, « — » and the final sentence (upd111.out). Head «UPDATE <DATE> <HH:MM>Z: RESULTS R111
(P-IDEAL-KEYS; CHECKER C124 <checker>) [refereed-only] » («P-IDEAL-KEYS» 0 times in GAPS); <DATE> = the landing date.
(10) DATA of record = packet §8 (l. 248-282), NOT signed; L-2's DATA parenthesis states its counts per statement (G-9). Re-run at this
fill (scratch, git archive of 1a178aff's experiments/new and docs/new; box150, box166, box170 and box172 are unchanged from b302bbf5 to
1a178aff, git diff --stat lists docs/new files, box173, box174, notes and check.sh), check.sh l. 1-6 plus the «cd» and the «tmp» line,
then l. 911-918, 2026-11-06T01:56:01Z-01:56:04Z, rc 0:
- PASS line: «P-IDEAL-KEYS: keycheck 0 violations (controls fire, output = frozen keycheck.out), DEAD instances PM / PMV / tower
  replayed (XSIM 0); pins packet 62b35bf7, line L-1 f36c6402, tool 6ce4693d, output 5100eb30, instances c025a4b6 / 06f0e501 / 9aead80e,
  fixes 26088848, line L-2 fb1b2276: PASS».
- w172 raw (keycheck.py output byte-equal to keycheck.out, cmp): «SCOPE corpus 413 random 400 runs 13813 steps 14027»; «COUNTS runs
  13813 steps 14027 pairs_local 27102 kf_movers 90811 pair_flips 15614 own 13393 below 2221 toponly_first 516 renew_h 573 renew_first_h
  520 intervals 2704 merge_states 19932 returns 722 ladder_runs 231 pairkf_movers 34113 keyflip_movers 51431 retcnt_movers 50260»;
  «LOCALKP 0 LOCALCTL 48435 KFWE 0 PAIRKF 0 CASCADE 0 LADDER 0 FLET 0 RENEW 0 RENEWB 0 MERGE 0 MERGECTL 23272 RETURN 0 RETCNT 0 KEYFLIP
  0»; «DEAD PM KILL_PM_compose_dd_d5_F14 valid True deg 2 N 15 T 14 mover 12 desc 4 moves 6 bound 5»; «DEAD PMV dd_d5_F14 valid True LR
  True N 10 T 14 mover 6 desc 7 VR 10 bound 8»; «DEAD TOWER dd_d5_F14 T 14 pair flips by level [2, 3, 6, 14, 7] moves [1, 1, 3, 1, 3, 3,
  7, 7, 3, 2] doubling F(3) = 2(1 + F(2)) True next 2(1 + F(3)) = 30 > T True»; the two «TOWER composition» lines (N 15 and N 18, T 14,
  max pair flips 14); the box 150 checker three times «TOTAL genomes 1 runs 1 steps 14 XSIM 0 TOPO 0 MONO 0 XINEW 0 RISE 0 CHAIN 0
  KEYFLIP 0 DECR 0 TOPMONO 0 RBOUND 0 RESTR 0 ICHARGE 0 REC 0 VIOL 0 (info REC148 0)». Equal to both referees' runs at b302bbf5 (REFEREE
  l. 130-132; REFEREE-2 l. 123-126) and to REFEREE-2's at 1a178aff (Add. 1 l. 189).
- My split (kcstats.py, kcstats.out): top-only intervals 2,704 = 516 with a ≥ 2 + 2,188 with a = 1; every key of every option of every
  top mover constant on [a − 1, b] on all of them (0 violations; keycheck.py checks KP only, G-9 (i)); 231 ladder runs by d: 1: 58, 2:
  9, 3: 61, 4: 62, 5: 29, 6: 10, 8: 2; corpus 413 files, 384 distinct contents, 175 of them 𝓛^R files, largest N 24.
- My own simulator (mysim111.py, mysim111.out): packet §7 (a)'s option fields = the JSON of KILL_PM_compose_dd_d5_F14 (15 movers, True);
  start 110111111000000; my run = §7 (a)'s fifteen states (True), T 14, degree 2, N 15; mover 12: D = {10, 11, 13, 14}, 6 moves at steps
  1, 2, 5, 8, 9, 10 > 5, the only PM violator. dd_d5_F14 = movers 0-9 of that file (True), in 𝓛^R_5 (True); my run = §7 (b)'s list
  (True), T 14; mover 6: D = {1, 2, 3, 5, 7, 8, 9}, cv rises (β-set order) at steps 2, 3, 4, 6, 7, 8, 10, 11, 12, 14: VR 10 > 8;
  moves(6) = 7. F(0..4) = 2, 3, 6, 14, 7; moves(6) = moves(7) = 7 = 1 + F(2); F(3) = 14 < 20 = moves(6) + moves(7) + F(2); 2(1 + F(3)) =
  30 > 14. KILL_PM_compose: largest pair flip count 14; T1_dd_top8: N 18, T 14, largest pair flip count 14, mover 10 of level 4 with 8
  moves, top level 5 (mover 14). All equal to the packet, the fixes and both referees (REFEREE dead_recompute.txt; REFEREE-2
  r2sim_dead.out).
- Byte test and token diff: wdiff111.py / wdiff111.out ((2)).
NOT re-run: the referees' tools (docs/referee/scratch/keys_probe.py, keys_check.py, keys_l2_bytetest.py;
docs/referee-2/R2-P-IDEAL-KEYS/r2sim.py, r2lemmas.py); I read their committed logs (keys_logs/check_corpus.txt, check_any.txt,
check_deg2.txt, dead_recompute.txt; r2lemmas_seed28_4000.out, r2lemmas_corpus.out, r2sim_dead.out), whose counts equal the reports'
(REFEREE l. 124-128; REFEREE-2 l. 113-122). check.sh's other blocks and scripts/verify.sh: not run. L-RED's independent replay of the PM
instance (packet l. 221-222): not on file, not checked.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 C123 named for P-TR3 (G-0). D-2 fixes l. 3 «Lead relay 00:47Z of fix
round 1» against the lane commit 1a178aff (00:47:11Z) and the Lead's log commit e7990774 (00:55:38Z); packet l. 2 «Lead brief BOX 172
(2026-11-05)» against bc05394a (22:51:15Z) and the freeze b302bbf5 (23:00:53Z); stamps not verifiable from the repository. D-3 packet l.
221-222 (L-RED's replay of the PM instance) is not on file. D-4 REFEREE-2 l. 34-35 cites body item (e) at «RESULTS l. 10224-10226»; it
is l. 10225-10227 (l. 10224 ends item (d)); REFEREE l. 31 has l. 10225-10227. D-5 REFEREE-2 l. 144 «Two index ranges are wider in the
line than in the packet:» is followed by «- Exact word changes:»; the two ranges are W-2 (l. 149-150). D-6 REFEREE §3 l. 124 calls its
corpus «box150-179 JSONs at b302bbf5»; at b302bbf5 no box173-box179 exists (its log check_corpus.txt has the glob «box1[5-7][0-9]»), so
the set is box150-box172, as keycheck.py's. D-7 the referees' own counts (REFEREE 10,350 + 4,500 + 4,500 runs; REFEREE-2 88,082 + 119
runs) are their own sets, not the lane's 13,813 runs. D-8 independence timing: REFEREE's report (23:49:08Z) precedes REFEREE-2's
(23:51:25Z) by 2 min 17 s; each states it did not read the other's directory (REFEREE l. 2-3; REFEREE-2 l. 2-3); in the second round
each read the other's item labels through the fixes entry only (REFEREE §C l. 183-184; REFEREE-2 Add. 1 l. 167). No discrepancy between
a report and the lane files beyond these.
(12) Excluded: packet §8 (DATA counts, machine checks, pins, EXCLUDED, TARGET diff, READING); RENEW's reading (l. 160-163); F-a's
READING and DATA; CONJECTURES PAIR-LIN, PAIR-POLY, PM′_S, RENEW-COUNT, SLOT-TRADE, FREE-KP and the B-bit counts, the dynamic κ forms and
the LEVEL-PRODUCT reading, every DATA table and READING of boxes 165-171, the box 170 csp.py results (l. 274-275);
box172/inst/max_d4_L13.json and max_d5_L15.json (copies for box 173, «used by no statement here», l. 272-273); boxes 173-175 (later lane
work). Not part of this entry.
(13) Commits: lane (claude/l-new): b302bbf5 (2026-11-05T23:00:53Z; freeze: packet 62b35bf7 (282 lines), L-1 f36c6402, keycheck.py,
keycheck.out, box172/inst, check.sh block P-IDEAL-KEYS) → 1a178aff (2026-11-06T00:47:11Z; fixes entry 1, 100 lines; L-2; pin172
extended). The instances: experiments/new/box166/out/KILL_PM_compose_dd_d5_F14.json (l-new d3eeb8b3, 2026-11-05T19:42:33Z, sha1
c025a4b61cd6342775aba6cbe2f89a9362dfa172), experiments/new/box172/inst/dd_d5_F14.json (b302bbf5, sha1
06f0e5015d09c0f1e03f1b9293ab3cd8483e435b, byte-equal to L-RED's experiments/red/r197/lag/dd_d5_F14.json at origin/claude/l-red),
experiments/new/box170/out/T1_dd_top8.json (0fd70166, 2026-11-05T21:38:38Z, sha1 9aead80e6123c720255cfbf75af12992bbc8e9b9). REFEREE
(claude/referee): ece8c4ee (report; keys_check.py 221 lines, keys_probe.py 86 lines, four logs) → cb7e2909 (§C, +50 lines;
keys_l2_bytetest.py 45 lines). REFEREE-2 (claude/referee-2): ebcf52d0 (report; r2sim.py 93 lines, r2lemmas.py 187 lines, three outputs)
→ 87b80d17 (Addendum 1, +28 lines) → 6c6f2033 (notebook stamp). CHECKER: 21ff8727 (2026-11-05T21:18:01Z; C122 CLOSED). Lead: bc05394a
(freeze brief), 7e456b8c (to the referees), e7990774 (fix round), 7a976cc4 (L-2 to the referees). Trunk: see the header.
(14) Placement: see (0). DEAD-ENDS ROWS: NONE (not drafted). R111 kills two lane conjectures (PM, PMV) by explicit refereed instances
inside its line. CHECKER C118 §5 confirmed «no row» for lane conjectures killed inside a landed line («DE37: the Lead's «no row» is
CONFIRMED.», with REP-LIN, BIP-REL-1, frz32, fbg_K12 and odxi as precedent, and «DE34-DE36 are candidate algorithms and a proof route, a
different class.»); C120 §5, C121 §6 and C122 §3 applied it to R108's REPLAY, R109's SEG1-2D and R110's SC-ISO («No Dead-ends row (C118
§5; here the kill is also conditional): agreed.»). PM and PMV are per-mover bounds proposed inside L-NEW's boxes 165-166; they occur 0
times in RESULTS and GAPS, so no fleet conjecture or route depends on them; R111's line records each instance and its numbers, and the
body inlines them (Claims (j), (k)), so CLAUDE.md's «Record every dead end with the exact obstruction and the instance that killed it.»
is met inside RESULTS. The doubling tower is no longer DEAD (TOWER, F-a), so there is no third dead end. The next free Dead-ends number
stays DE37 («DE37» 0 times in RESULTS). CONFIRMED by precedent (my reading; CHECKER to confirm).

### R111 [refereed-only] In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of R104 used; RESULTS R105's ENC, MONO, XI-NEW and RISE, and at degree ≤ 2 its KEYFLIP, read with moves(x) the number of steps t with x ∈ Mv_t as in RESULTS Erratum E-2 (E2c); and RESULTS R110's definition of 𝓛^R_d only), on acyclic Ξ-graphs, any number of movers per level, with Mv_t the movers of step t, T the number of steps of a run, KP_s(x) the option of x with the least key under s, KF_x the number of steps t with KP_(s_t)(x) ≠ KP_(s_(t−1))(x), W(x) the movers reachable from x along W-targets of any options (x excluded), WE_x the number of steps moving a mover of W(x), for two distinct movers p, q of one level a flip of (p, q) at step t a change between s_(t−1) and s_t of the order of the keys of their current options, flips(p, q) the number of steps at which (p, q) flips, v_s(x, k) the integer value of option (x, k) under s (R105 ENC) and cv_s(x) := v_s(x, s(x)): (LOCAL-KP) at any degree, if two states agree on W(x) then they give every option of x the same key, so KP(x) is the same and KF_x ≤ WE_x; (PAIR-KF) for a mover x of degree 2 and level ≥ 1 with W-targets a, b of its two options, KF_x = 0 if a = b, and KF_x = flips(a, b) if a ≠ b, x key-preferring its option 0 under s iff the current option of a has the smaller key; (PAIR-MOVES) if every mover has degree ≤ 2, moves(x) ≤ 1 + flips(a, b) for such x with a ≠ b and moves(x) ≤ 1 for every other mover, so T ≤ N + the sum of those flip counts; (CASCADE) at any degree, at every step at which two distinct movers p, q of one level l flip, p or q moves, or l ≥ 1, neither moves, their current W-targets w_p ≠ w_q and (w_p, w_q) flips at the same step, and flips(p, q) ≤ T; (LADDER) on 𝓛^R_d with F(l) := flips(2l, 2l + 1), F(0) ≤ 2, F(l) ≤ moves(2l) + moves(2l + 1) + F(l − 1) and moves(x) ≤ 1 + F(lev(x) − 1) for lev(x) ≥ 1, so F(l) ≤ 2 + 3F(l − 1) ≤ 3^(l+1) − 1; (RENEW) at any degree, with τ the largest level, a step top-only when all its movers have level τ and a top-only interval a maximal interval [a, b] of top-only steps, if a ≥ 2 then step a − 1 moves a mover of level below τ and every mover h of step a, moving to w, has w ∉ A_(s_(a−2))(h) (A_s(h): h's current option under s and its options strictly better under s), v_(s_(a−1))(h, w) > v_(s_(a−2))(h, w) and some strict Ξ-descendant of h on the chain of (h, w) under s_(a−2) moving at step a − 1, and the keys of every mover of level τ are constant on s_(a−1), …, s_b; (MERGE) at any degree, for two distinct options k, k′ of x and a state s, v_s(x, k) − v_s(x, k′) depends only on the options under s of the movers of the two chains before their first common mover; (RETURN) for a mover x of degree 2 that moves to o at step t_1 and next moves at step t_2, the Ξ-target z of its other option is a mover with cv_(s_(t_2−1))(z) > cv_(s_(t_1−1))(z), so moves(x) ≤ 1 + R(x, 0) + R(x, 1) with R(x, k) the number of steps at which cv of the Ξ-target of (x, k) rises (0 if that target is the exit X); (TOWER, by flips ≤ T) a run in which the doubling step of box 169, «F(l) = 2(1 + F(l − 1))» iterated level after level, reaches F(l) = 2^(l+1) − 2 has T ≥ 2^(l+1) − 2 (a READING, not a refutation: the doubling tower is not a shortcut around G-N5-TIME); and DEAD: the lane conjecture PM («moves(x) ≤ (deg(x) − 1)(1 + desc(x))» for every mover x, desc(x) the number of strict Ξ-descendants of x) is false, by experiments/new/box166/out/KILL_PM_compose_dd_d5_F14.json (degree 2, N 15, T 14, mover 12 with desc 4 moving 6 times; sha1 c025a4b6…); the lane conjecture PMV («VR(z) ≤ 1 + desc(z)» for every mover z, VR(z) the number of steps at which cv(z) rises) is false, by L-RED's 𝓛^R_5 genome dd_d5_F14 (experiments/new/box172/inst/dd_d5_F14.json, sha1 06f0e501…; T 14, mover 6 with desc 7 and 10 rises) (2026-11-05) — a STRUCTURE / REDUCTION statement inside the IDEAL model on the key side; bounds nothing polynomially (LADDER's bound is exponential); the conjectures PAIR-LIN, PM′_S and RENEW-COUNT are not claimed; Ξ-cyclic genomes are not covered, and degree ≥ 3 is not covered by PAIR-KF, PAIR-MOVES, LADDER or RETURN; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (DATA, experiments/new/box172/keycheck.py on 413 in-tree genome files from their stored starts and 400 random acyclic genomes from up to 64 starts each, 13,813 runs: LOCAL-KP 0 violations on 27,102 (state pair, mover) checks and, for KF_x ≤ WE_x, on 90,811 (run, mover) pairs; PAIR-KF 0 on 34,113 (run, degree-2 mover of level ≥ 1) pairs; CASCADE 0 unclassified of 15,614 flips; LADDER's first inequality 0 on 231 runs of 𝓛^R genomes; RENEW 0 on 520 (step, mover) pairs at the first steps of top-only intervals starting at t ≥ 2 and, for the constant key preference KP of the top movers on s_(a−1), …, s_b, on all 2,704 top-only intervals (516 of them with a ≥ 2); MERGE 0 on 19,932 (state, degree-2 mover) checks; RETURN 0 on 722 consecutive move pairs and RETURN-COUNT 0 on 50,260 (run, degree-2 mover) pairs; flips ≤ T 0 on the same runs; PAIR-MOVES and the rest of LADDER: no separate DATA; the two DEAD instances replayed by the same tool and by the box 150 checker; TOWER, on dd_d5_F14: F(0..4) = 2, 3, 6, 14, 7 and T 14, the doubling step attained at level 3 (F(3) = 14 = 2(1 + F(2)) = T) and not at level 4 (2(1 + F(3)) = 30 > 14)) (P-IDEAL-KEYS, docs/new/P-IDEAL-KEYS.md with its fixes entry 1, docs/new/P-IDEAL-KEYS-fixes.md; L-NEW successors 54-55), CHECKER PASS (docs/checker/C124.md, checker PENDING)
- Object (L-NEW successor 55, Opus 5.5, D14 / D18 / D20, from successor 54's boxes 165-171; frozen, unchanged during review): packet
  P-IDEAL-KEYS, docs/new/P-IDEAL-KEYS.md, sha1 62b35bf7ed7616bb66ff512edc30fe30431db0e5, 282 lines (l-new freeze b302bbf5,
  2026-11-05T23:00:53Z; identical at 1a178aff and 432edf82). Both referees measured the sha1 (REFEREE l. 6 «docs/new/P-IDEAL-KEYS.md
  sha1 62b35bf7ed7616bb66ff512edc30fe30431db0e5, 282 lines;»; REFEREE-2 l. 7 «docs/new/P-IDEAL-KEYS.md sha1
  62b35bf7ed7616bb66ff512edc30fe30431db0e5, 282 lines;»). Status (l. 8-9): «Not a TARGET.md claim. Every statement is about the
  IDEAL-ACYC model only. No polynomial bound is claimed.» To sign (table l. 11-20): §2 LOCAL-KP, §3 PAIR-KF and PAIR-MOVES, §4 CASCADE,
  F ≤ T and LADDER, §5 RENEW, §6 MERGE, RETURN and RETURN-COUNT, §7 the DEAD items; §8 «DATA / READING (not to sign)». Sections:
  premises (l. 22-44), §0 the model and notation (l. 46-81), §2 (l. 83-94), §3 (l. 96-113), §4 (l. 115-143), §5 (l. 145-166), §6 (l.
  168-202), §7 (l. 204-246), §8 (l. 248-282). Sources (l. 4-6): docs/new/N5-PERMOVER-box165.md to N5-FROZEN-box171.md (successor 54);
  «This packet governs: every proof is written out in full HERE and is checked against this text only; no other file carries a proof of
  a statement below.» (l. 6-7).
  Fixes: docs/new/P-IDEAL-KEYS-fixes.md, append-only, entry 1 (1a178aff; 100 lines, sha1 26088848b6a80621fb46a4887be0b2b8ad2a8ebc) and
  entry 2 (432edf82; 118 lines, sha1 504403c3816279bee51da5358e0e77250ffb8f69, l. 1-100 unchanged): F-a restates the packet's §7 (c) as
  TOWER, a consequence of Corollary F ≤ T, no longer DEAD; F-b to F-e correct packet text; F-f renames MERGE's letters in the line; line
  L-2; entry 2 makes line L-3 (one DATA replacement, CHECKER C124 E-1). Entry 1: «This entry carries one statement with a proof (TOWER,
  F-a below); the packet and this entry are the only files that carry proofs of the packet's statements.» (l. 7-8).
  The RESULTS line is L-3, c29f0a9365e700e0888018be42caf8757df1ac74 (docs/new/P-IDEAL-KEYS-line-L3.txt, l-new 432edf82,
  2026-11-06T03:41:53Z, the file's only commit; 5,636 bytes). The title is L-3 verbatim, with nothing inserted (its date parenthesis
  «(2026-11-05)» and its source note are the line's own; the source note names the packet and its fixes entry 1, the two files that
  carry proofs; fixes entry 2 carries none). L-3's parentheses balance (122 «(» / 122 «)»). Line history: L-1 (f36c6402, b302bbf5,
  frozen with the packet); L-2 (fb1b2276, 1a178aff, fixes entry 1: L-1 with exactly ten replacements R1-R10, fixes l. 59-69: the binder
  of A_s(h) in RENEW, MERGE's letters k, k′, the tower moved out of DEAD into TOWER with its values as DATA, the PM and PMV quotes made
  verbatim, the PAIR-KF and RETURN-COUNT DATA units narrowed to the degree-2 movers the tool counts, and the fixes file named in the
  source note; L-1 with R1-R10 equals L-2 byte for byte, by my script); L-3 (c29f0a93, 432edf82, fixes entry 2: L-2 with exactly one
  replacement R11, CHECKER C124 E-1, DATA wording only: the RENEW count of L-2's «for the constant keys, on 2,704 intervals» now names
  what keycheck.py's RENEWB counts, the key preference KP of the top movers on s_(a−1), …, s_b, on all 2,704 top-only intervals, 516 of
  them with a ≥ 2; no statement, definition or premise changes; L-2 with R11 equals L-3 byte for byte, by my script). L-2 MATCHES at
  both referees, each after its own byte test: REFEREE (cb7e2909) §C l. 211 «Result: EQUAL to L-2 (sha1 fb1b2276…, 5,542 bytes).», l.
  224 «L-2 MATCHES.»; REFEREE-2 (87b80d17) Addendum 1 l. 181 «**Line L-2: MATCHES.**». L-3 MATCHES at both referees, each after its own
  byte test against C124 §5: REFEREE (fadbb9a0) §C add. 1 l. 236 «L-3 is byte-EQUAL to it (cmp).», l. 243 «Verdict: L-3 MATCHES. All
  signatures stand.»; REFEREE-2 (7ff32432) Addendum 2 l. 199 «**Line L-3: MATCHES.**», l. 200 «replacing it gives a string
  byte-identical to L-3 (5,636 B)». Both diffed every definition of L-1 against the packet (REFEREE l. 140-142; REFEREE-2 l. 134-135),
  and REFEREE l. 222 «Definitions: unchanged from L-1 except MERGE's k, k′, all as diffed in §5.»; L-3 changes no definition.
- Claims signed (REFEREE successor 24 «(Opus 5.5, D15)», report ece8c4ee, §C cb7e2909; REFEREE-2 successor 28 «(Opus 5.5, D12/D20)»,
  report ebcf52d0, Addendum 1 87b80d17). Items (a)-(h), (j) are SIGN in both first-round verdict tables (REFEREE "## 0. Verdicts" l.
  11-25 of R-P-IDEAL-KEYS.md; REFEREE-2 "## Verdicts" l. 12-25 of R2-P-IDEAL-KEYS.md); (k) is SIGN at REFEREE-2 and SIGN WITH GAP KY-1
  at REFEREE, the gap closed by fixes F-b (REFEREE §C l. 196 «F-b: KY-1 CLOSED.»); (i) is the statement of fixes F-a, signed by both in
  their second rounds (REFEREE §C l. 187 «F-a: SIGN TOWER as restated.»; REFEREE-2 Add. 1 l. 169 «F-a TOWER: **SIGN** (Opus 5.5,
  D12).»). REFEREE §C l. 225 «Every item is now SIGNED: §2-§6, DEAD PM, DEAD PMV (KY-1 closed), and TOWER (as restated in F-a).»;
  REFEREE-2 l. 25 «No statement is REFUSED. No gap is listed: every proof is complete from the landed premises and the definition.».
  Every item is about R104's IDEAL model on acyclic Ξ-graphs; (a), (d), (f), (g) and (i) at any degree; (b) and (h) for movers of degree
  2; (c) when every mover has degree ≤ 2; (e) on 𝓛^R_d. No item bounds a count polynomially; LADDER's bound 3^(l+1) − 1 is exponential.
  Notation (packet §0 l. 46-81): Mv_t := {x : s_t(x) ≠ s_(t−1)(x)} and T the number of steps; moves(x) := #{t ∈ [1, T] : x ∈ Mv_t} (the
  binder of Erratum E-2 (E2c)); KP_s(x) the option of x with the least key_s(x, ·) (unique by (F1)), KF_x := #{t ∈ [1, T] : KP_(s_t)(x)
  ≠ KP_(s_(t−1))(x)}; W(x) the movers reachable from x along W-targets of any options, x excluded, and WE_x := #{t : Mv_t ∩ W(x) ≠ ∅};
  D(x) the strict Ξ-descendants of x, desc(x) := its size; for p ≠ q of one level, ord_s(p, q) := [key_s(p, s(p)) < key_s(q, s(q))], a
  flip of (p, q) at t a change of ord between s_(t−1) and s_t, flips(p, q) the number of such t; v_s(x, k) := Σ over the β's of Ξ_s(x,
  k) of ±2^rank (+ for even parity), cv_s(x) := v_s(x, s(x)), cv_s(X) := 0, so v_s(x, k) = ε(x, k) + cv_s(xt(x, k)) by ENC; on 𝓛^R_d,
  F(l) := flips(2l, 2l + 1); τ := the top level, a step TOP-ONLY if every mover of Mv_t has level τ, LOWER otherwise, a TOP-ONLY
  INTERVAL a maximal interval [a, b] ⊆ [1, T] of consecutive top-only steps; A_s(x) := {s(x)} ∪ {k : Ξ_s(x, k) ▷ Ξ_s(x, s(x))}. (F1) the
  keys of two distinct options of one level differ; (F2) if x ∈ Mv_t, then s_t(x) ∈ A_(s_(t−1))(x) minus {s_(t−1)(x)}, and at degree 2
  s_(t−1)(x) is x's other option (l. 61-64).
  (a) Lemma LOCAL-KP (§2 l. 83-94) [IDEAL-ACYC, any degree]: «(a) If s(y) = s′(y) for every y ∈ W(x), then key_s(x, k) = key_(s′)(x, k)
      for every option k of x; hence KP_s(x) = KP_(s′)(x).»; «(b) For every run, KF_x ≤ WE_x.». Proof: (a) by induction on lev(x), since
      wt(x, k) ∈ W(x) and W(wt(x, k)) ⊆ W(x); (b) a step with Mv_t ∩ W(x) = ∅ keeps s on W(x), so KP(x) does not change by (a). Cells:
      REFEREE l. 14 «SIGN»; REFEREE-2 l. 15 «**SIGN** (Opus 5.5, D12)».
  (b) Lemma PAIR-KF (§3 l. 96-105) [x of degree 2 and level ≥ 1, options 0, 1, a := wt(x, 0), b := wt(x, 1)]: «(a) If a = b, KP_s(x) is
      the option of x with the smaller gate, for every state s; so KF_x = 0 in every run.»; «(b) If a ≠ b, then for every state s:
      KP_s(x) = 0 iff ord_s(a, b) is true; so KF_x = flips(a, b) in every run.». Proof: key_s(x, k) is the key of x's W-target's current
      option followed by g(x, k); equal prefixes leave the gates to decide; distinct prefixes (two options of one level, (F1)) decide.
      Cells: REFEREE l. 15 «SIGN»; REFEREE-2 l. 16 «**SIGN** (Opus 5.5, D12)».
  (c) Corollary PAIR-MOVES (§3 l. 106-111; premise R105 KEYFLIP read with E-2 (E2c)): «If every mover of G has degree ≤ 2, then in every
      run, for every mover x: moves(x) ≤ 1 + flips(wt(x, 0), wt(x, 1)) if deg(x) = 2, lev(x) ≥ 1 and wt(x, 0) ≠ wt(x, 1); moves(x) ≤ 1
      otherwise.»; hence T ≤ N plus the sum of those flip counts. Proof: KEYFLIP gives moves(x) ≤ 1 + KF_x; PAIR-KF (b) for the first
      kind; KF_x = 0 at degree 2 with equal W-targets or at level 0, and moves(x) = 0 at degree 1; T ≤ the sum of moves(x) since Mv_t is
      nonempty. Cells: REFEREE l. 16 «SIGN (KEYFLIP read with the E-2 (E2c) binder, correctly)»; REFEREE-2 l. 16 (the PAIR-KF row)
      «**SIGN** (Opus 5.5, D12)».
  (d) Lemma CASCADE and Corollary F ≤ T (§4 l. 115-131) [IDEAL-ACYC, any degree; p ≠ q of one level l; t a step at which (p, q) flips]:
      «(a) If l = 0, then p ∈ Mv_t or q ∈ Mv_t.»; (b) if l ≥ 1, exactly one of (own) p ∈ Mv_t or q ∈ Mv_t, and (below) «p, q ∉ Mv_t, the
      current W-targets w_p := wt(p, s_t(p)) and w_q := wt(q, s_t(q)) are distinct movers (of level l − 1), and (w_p, w_q) flips at step
      t.» (l. 120-121). Proof: if neither moves, their options and W-targets are the same in s_(t−1) and s_t; at level 0 the keys are
      constant; with w_p = w_q the constant gates decide; with w_p ≠ w_q, ord_s(p, q) = ord_s(w_p, w_q) for both states. Corollary F ≤
      T: «flips(p, q) ≤ T for every pair and every run» (l. 129). Cells: REFEREE l. 17 «SIGN»; REFEREE-2 l. 17 «**SIGN** (Opus 5.5,
      D12)».
  (e) Corollary LADDER (§4 l. 132-140; premises R110's definition of 𝓛^R_d, R105 KEYFLIP) [G ∈ 𝓛^R_d, d ≥ 1, any run]: «F(0) ≤ moves(0)
      + moves(1) ≤ 2, and F(l) ≤ moves(2l) + moves(2l + 1) + F(l − 1) for 1 ≤ l ≤ d − 1;»; «moves(x) ≤ 1 + F(lev(x) − 1) for lev(x) ≥ 1,
      so F(l) ≤ 2 + 3 F(l − 1) and F(l) ≤ 3^(l+1) − 1; and F(l) ≤ T for every l.». Proof: CASCADE splits the flip steps of (2l, 2l + 1)
      into own steps (at most moves(2l) + moves(2l + 1)) and below steps, which are distinct flip steps of (2l − 2, 2l − 1); PAIR-MOVES
      with the distinct W-targets 2(l − 1) + k; F(l) + 1 ≤ 3 (F(l − 1) + 1). The second inequality is tight at level 3 of dd_d5_F14
      (moves(6) = moves(7) = 7 = 1 + F(2)), the first is not (F(3) = 14 < 20) (fixes F-e, N-1). Cells: REFEREE l. 17 (the CASCADE row);
      REFEREE-2 l. 17 (the same row; N-1).
  (f) Lemma RENEW (§5 l. 145-159; premises R105 XI-NEW, RISE in the signed form of body item (e), LOCAL-KP) [IDEAL-ACYC, any degree; τ
      the top level; [a, b] a top-only interval]: (a) if a ≥ 2, then step a − 1 is a LOWER step, and for every h ∈ Mv_a, with w :=
      s_a(h): «(i) w ∉ A_(s_(a−2))(h);», «(ii) v_(s_(a−1))(h, w) > v_(s_(a−2))(h, w): step a − 1 strictly raised the value of the option
      that h takes at a;», «(iii) some mover z ≠ h on the chain of (h, w) under s_(a−2) lies in Mv_(a−1), and every such z lies in
      D(h).»; the same for every top-only step t ≥ 2 (l. 151); «(b) For every top mover h and every option k of h, key_(s_u)(h, k) is
      the same for all u ∈ [a − 1, b]; so KP_(s_u)(h) is constant on [a − 1, b].». Proof: maximality makes step a − 1 lower; every mover
      of a top-only step has level τ, so it is a least-level mover of its step, and XI-NEW and RISE (body item (e) (a)-(c)) give
      (i)-(iii); for (b), the steps a, …, b move only level-τ movers and W(h) lies below τ, so LOCAL-KP (a) applies. Part (iii) does not
      place z below the top (l. 162-163). Cells: REFEREE l. 18 «SIGN»; REFEREE-2 l. 18 «**SIGN** (Opus 5.5, D12)».
  (g) Lemma MERGE (§6 l. 169-185; premise R105 ENC) [IDEAL-ACYC, any degree; x with two distinct options (the line's k, k′); s a state;
      Pre the movers of the two chains under s before their first common mover m (m := X if none)]: (a) v_s(x, k) − v_s(x, k′) is the
      difference of the ε-sums of the two prefixes, including the options themselves (l. 173); «(b) If a state s′ agrees with s on Pre_a
      ∪ Pre_b, then v_(s′)(x, a) − v_(s′)(x, b) = v_s(x, a) − v_s(x, b); in particular the Ξ-order of (x, a) and (x, b) is the same
      under s′ as under s.» (l. 174-175, the packet's letters). Proof: ENC unrolled along a chain; the terms cv(m) cancel; under s′ both
      chains reach m through the same movers. Cells: REFEREE l. 19 «SIGN»; REFEREE-2 l. 19 «**SIGN** (Opus 5.5, D12)».
  (h) Lemma RETURN and Corollary RETURN-COUNT (§6 l. 186-200; premises ENC, MONO) [x of degree 2, options o, o′; x moves at t_1 to o and
      next at t_2]: «Then z := xt(x, o′) is a mover (not X), and cv_(s_(t_2 − 1))(z) > cv_(s_(t_1 − 1))(z).» (l. 187-188); RETURN-COUNT:
      «moves(x) ≤ 1 + R(x, 0) + R(x, 1)», with R(x, k) the number of steps at which cv of xt(x, k) rises (0 if xt(x, k) = X) (l.
      195-196). Proof: (F2) at t_1 and t_2; v(x, o) = ε(x, o) + cv(xt(x, o)) never decreases (MONO through ENC); so v(x, o′) rose
      strictly, impossible if z = X; RETURN-COUNT by telescoping into the disjoint windows [t_(i−1), t_i − 1]. Cells: REFEREE l. 20
      «SIGN»; REFEREE-2 l. 20 «**SIGN** (Opus 5.5, D12)».
  (i) TOWER (fixes F-a, l. 17-21; it replaces packet §7 (c), which is no longer a DEAD item): «Let a run have a pair that flips F(l) =
      2^(l+1) − 2 times (the value that the doubling step of box 169, «F(l) = 2(1 + F(l − 1))» (docs/new/N5-PAIRLIN-box169.md l. 26,
      verbatim), gives when iterated from F(0) = 2). Then that run has T ≥ 2^(l+1) − 2.»; «Proof. Corollary F ≤ T (signed by both):
      flips(p, q) ≤ T for every pair of every run. ∎». Hypotheses: «IDEAL-ACYC, any degree, any width; for 𝓛^R_d with F(l) of §0, or for
      any pair a tower designates at level l» (l. 17-18). Why it is not DEAD (fixes l. 14-16): box 169's prediction reads «Predicted:
      F(l) = 2^(l+1) − 2, N = O(l²), and T ≥ F(l)» (N5-PAIRLIN-box169.md l. 38), so «It already includes T ≥ F(l), so Corollary F ≤ T
      refutes nothing in it»; «No statement of record is refuted, so nothing is DEAD.». «Does NOT claim: that the tower is DEAD; that no
      IDEAL-ACYC family has exponential T; that a gadget can never add steps.» (l. 28). Cells: REFEREE l. 23 «REFUSE as DEAD (KY-G1).»,
      signing the implication; §C l. 187 «F-a: SIGN TOWER as restated.», l. 192 «KY-G1 is CLOSED.»; REFEREE-2 l. 23 (the DEAD, «in the
      scope stated in R-1»), Add. 1 l. 169 «F-a TOWER: **SIGN** (Opus 5.5, D12).», l. 173 «This supersedes my §7 (c) DEAD SIGN, which I
      withdraw in favour of TOWER.».
  (j) DEAD: the lane CONJECTURE PM (box 165, title; packet §7 (a) l. 205-224 with fixes F-c): «moves(x) ≤ (deg(x) − 1)(1 + desc(x))»,
      stated there for every IDEAL-ACYC genome, every start and every mover x. Instance
      experiments/new/box166/out/KILL_PM_compose_dd_d5_F14.json (sha1 c025a4b61cd6342775aba6cbe2f89a9362dfa172, l-new d3eeb8b3),
      IDEAL-ACYC, every mover of degree 2, N = 15, levels 0-4 (levels 1 and 4 with more than two movers, so neither in 𝓛^R_d nor in
      R109's 𝓛_d). Option fields (W-target, Ξ-target, gate, β rank, β parity; X the exit) (l. 209-215): «mover 0 (lev 0): (−, 4, 4, 7,
      even), (−, 3, 17, 12, odd); 1 (lev 0): (−, 9, 3, 6, odd), (−, X, 9, 10, even); 2 (lev 1): (0, 8, 18, 1, odd), (1, 1, 15, 4, odd);
      3 (lev 1): (0, X, 11, 19, even), (1, X, 16, 9, odd); 4 (lev 2): (2, 6, 6, 16, odd), (3, 9, 2, 15, odd); 5 (lev 2): (2, 8, 19, 13,
      odd), (3, 3, 8, 8, odd); 6 (lev 3): (4, 7, 0, 14, even), (5, 5, 5, 11, odd); 7 (lev 3): (4, 5, 7, 3, even), (5, 2, 10, 2, odd); 8
      (lev 4): (6, 9, 12, 17, even), (7, 3, 14, 18, odd); 9 (lev 4): (6, 3, 13, 5, odd), (7, X, 1, 0, even); 10 (lev 1): (0, X, 21, 26,
      odd), (0, X, 20, 28, even); 11 (lev 1): (1, X, 22, 22, odd), (0, 10, 23, 29, even); 12 (lev 4): (6, 14, 24, 25, even), (7, 13, 25,
      21, even); 13 (lev 4): (6, 11, 26, 24, even), (7, 10, 27, 23, odd); 14 (lev 1): (0, 10, 28, 20, even), (1, 11, 29, 27, even).
      Start 110111111000000 (movers 0..14).». Run (l. 216-218): «110111111000000, 111111101110101, 111111000110001, 111110010110011,
      111110110110011, 111100100110111, 010000000111110, 010001011111110, 010001111011000, 000011101011101, 001011000011001,
      001010010011001, 001010110011001, 001000100011001, 001000000011001.»; T = 14; «Mover 12: D(12) = {10, 11, 13, 14} (desc 4), moves
      at steps 1, 2, 5, 8, 9, 10: moves(12) = 6 > (2 − 1)(1 + 4) = 5.» (l. 207-208). Cells: REFEREE l. 21 «SIGN»; REFEREE-2 l. 21
      «**SIGN** (Opus 5.5, D12) (F-1: quote not verbatim)», the quote made verbatim by F-c.
  (k) DEAD: the lane CONJECTURE PMV (box 166 §1, hypothesis (H-values); packet §7 (b) l. 225-234 with fixes F-b, F-c): «VR(z) ≤ 1 +
      desc(z)» (box 166 §1, verbatim), for every mover z, with VR(z) := #{t ∈ [1, T] : cv_(s_t)(z) > cv_(s_(t−1))(z)}. Instance
      experiments/new/box172/inst/dd_d5_F14.json (sha1 06f0e5015d09c0f1e03f1b9293ab3cd8483e435b; a byte copy of L-RED's claude/l-red
      experiments/red/r197/lag/dd_d5_F14.json), a genome of 𝓛^R_5 whose option fields are those of movers 0-9 in (j) (l. 230); start
      1101111110; run (l. 231-232): «1101111110, 1111111011, 1111110001, 1111100101, 1111101101, 1111001001, 0100000001, 0100010111,
      0100011110, 0000111010, 0010110000, 0010100100, 0010101100, 0010001000, 0010000000.»; T = 14; «Mover 6: D(6) = {1, 2, 3, 5, 7, 8,
      9} (desc 7); cv(6) rises at steps 2, 3, 4, 6, 7, 8, 10, 11, 12, 14: VR(6) = 10 > 1 + 7 = 8.» (l. 228-229). moves(6) = 7 = desc(6)
      ≤ 8 (fixes F-b, KY-1). Cells: REFEREE l. 22 «SIGN WITH GAP KY-1», §C l. 196 «F-b: KY-1 CLOSED.»; REFEREE-2 l. 22 «**SIGN** (Opus
      5.5, D12) (F-1: quote not verbatim)», Add. 1 l. 174-175.
  The RESULTS line (L-3) states (a)-(k) with their exact hypotheses, and nothing wider.
- Premise: RESULTS R104's definition of the IDEAL model and of the Ξ-graph (no R104 theorem), restated in packet §0; RESULTS R105's ENC,
  MONO, XI-NEW and RISE (RISE in the signed form of R105's body item (e)) and, at degree ≤ 2, KEYFLIP, each quoted verbatim by the
  packet (l. 24-37) from R105's title or body, where each quote occurs once, byte for byte (whitespace normalised); KEYFLIP's moves(x)
  read with RESULTS Erratum E-2 (E2c), «Read KEYFLIP's moves(x) as the number of steps that move x.», which is the packet's binder (§0
  l. 66); and RESULTS R110's definition of 𝓛^R_d (quoted verbatim, packet l. 77-78). L-3: «premise: R104's definition of the model only,
  no theorem of R104 used; RESULTS R105's ENC, MONO, XI-NEW and RISE, and at degree ≤ 2 its KEYFLIP, read with moves(x) the number of
  steps t with x ∈ Mv_t as in RESULTS Erratum E-2 (E2c); and RESULTS R110's definition of 𝓛^R_d only». Use: ENC in v_s, MERGE and
  RETURN; MONO in RETURN; XI-NEW and RISE in RENEW (a); KEYFLIP in PAIR-MOVES and LADDER, where every mover has degree ≤ 2; 𝓛^R_d in
  LADDER. E-2's (E2a) and (E2b) concern R105 items not used. Not used: R105's LOCAL, CHAIN-BACK, U-EQ, DECREMENT, EXACT-ENERGY,
  TOP-MONO, RANK-BOUND, INTERVAL-RESTRICT, INTERVAL-CHARGE, RECURSION; R106-R109; docs/lit (packet l. 42-43; REFEREE l. 41; REFEREE-2 l.
  44-45). «No machine premise is used by any signed item.» (packet l. 43). Both referees byte-tested every premise quote against landed
  RESULTS (REFEREE l. 28-34, «Each is FOUND exactly once»; REFEREE-2 l. 33-36, «all FOUND»). The DEAD instances are data files,
  recomputed by both referees with their own simulators written from R104's text (REFEREE §3 l. 107-118, t3r_sim.py; REFEREE-2 l. 88-97,
  r2sim.py, «Ξ-values compared as β-SETS»).
- L41 and L43. The proofs are L-NEW successors 54-55's (packet l. 7), including TOWER's, which the lane wrote in fixes F-a after
  REFEREE's refusal of the tower as DEAD (KY-G1; REFEREE l. 100-103, where it signs the implication) and REFEREE-2's scope note R-1 (l.
  98-103); its proof step is the signed Corollary F ≤ T. Nothing referee-written is a proof step of the entry (my reading; neither
  referee mentions L41). The DEAD items (j) and (k) refute explicit bounds by one instance each (6 > 5, 10 > 8), as L43 requires; the
  doubling-tower step is not a DEAD item, since box 169's prediction includes T ≥ F(l) (REFEREE l. 94 «The prediction INCLUDES T ≥ F(l).
  Corollary F ≤ T is consistent with it and refutes nothing in it.»).
- Fixes (docs/new/P-IDEAL-KEYS-fixes.md, L-NEW successor 55, append-only; entry 1 at 1a178aff, 100 lines, sha1
  26088848b6a80621fb46a4887be0b2b8ad2a8ebc; entry 2 at 432edf82, 118 lines, sha1 504403c3816279bee51da5358e0e77250ffb8f69, l. 1-100
  unchanged); entry 1 after REFEREE ece8c4ee and REFEREE-2 ebcf52d0, entry 2 after CHECKER C124 (9c9b03b7):
  - F-a (l. 10-28): «### F-a (KY-G1 REFUSE, KY-L1, R-1): §7 (c) is no longer DEAD; it becomes a consequence of Corollary F ≤ T plus a
    READING»; the statement TOWER with its proof (Claims (i)); a READING and DATA, both «(not to sign)». REFEREE §C l. 187-195 (TOWER
    SIGN; «KY-G1 is CLOSED.»; both box 169 quotes verified); REFEREE-2 Add. 1 l. 169-173 («Dropping DEAD is right: as my R-1 said, box
    169 predicted T ≥ F(l), so F ≤ T refutes no statement of record.»).
  - F-b (l. 30-32): «(it is 7 = desc(6) ≤ 1 + desc(6) = 8)» replaces packet §7 (b)'s false «(it is 7 = 1 + desc(6))» (REFEREE KY-1).
    REFEREE §C l. 196; REFEREE-2 Add. 1 l. 174-175 («F-b (KY-1): my miss.»).
  - F-c (l. 34-39): the PM and PMV guillemet texts made verbatim (box 165's title; box 166 l. 41), the quantifiers marked as a
    restatement (REFEREE-2 F-1, REFEREE KY-P1, KY-L3). REFEREE §C l. 197-198; REFEREE-2 Add. 1 l. 176-177.
  - F-d (l. 41-43): T1_dd_top8's mover 10 is the gadget's level-4 top with 8 moves; the genome's top level is τ = 5 (REFEREE-2 F-2,
    REFEREE KY-P2). REFEREE §C l. 199; REFEREE-2 Add. 1 l. 177.
  - F-e (l. 45-47): LADDER's «Does NOT claim» corrected: the second inequality is tight at level 3 of dd_d5_F14, the first is not
    (REFEREE-2 N-1). REFEREE §C l. 200-202; REFEREE-2 Add. 1 l. 177.
  - F-f (l. 49-51): in the line only, MERGE's options are k, k′ (REFEREE KY-L2). REFEREE §C l. 203; REFEREE-2 Add. 1 l. 178.
  - The W-2 / KY-L4 counts (l. 53-55): «pairkf_movers 34113» and «retcnt_movers 50260» in keycheck.out are the numbers of L-2. REFEREE
    §C l. 204-205; REFEREE-2 Add. 1 l. 179-180 («So the narrowed ranges are the tool's real ranges.»).
  - Line L-2 (l. 57-100): L-1 with exactly the ten replacements R1-R10; «Verdict items closed by L-2: KY-L1 (R3, R6, R9), W-1 (R1), W-2
    = KY-L4 (R7, R8), W-3 = KY-L3 (R4, R5), source note (R10), KY-L2 (R2).» (l. 100).
  - Entry 2 (l. 102-118), after CHECKER C124 E-1: «No statement, proof or other DATA changes; the packet and entry 1 stay as they are.»
    (l. 105); L-3 = L-2 «with exactly one replacement, copied by script from C124 §5» (l. 107), R11 (l. 109-110): «and, for the constant
    keys, on 2,704 intervals;» → «and, for the constant key preference KP of the top movers on s_(a−1), …, s_b, on all 2,704 top-only
    intervals (516 of them with a ≥ 2);»; the figures «intervals 2704» and «toponly_first 516» of the unchanged keycheck.out (l.
    111-112); the word diff L-2 → L-3 (l. 113-118). REFEREE §C add. 1 (fadbb9a0) l. 237-238: «I read keycheck.py at 432edf82: RENEWB is
    «KP[u][h] != KP[a − 1][h]», over every top-only interval.», «The wording is true.»; REFEREE-2 Add. 2 (7ff32432) l. 195 «**Fixes
    entry 2: CORRECT.**», l. 198 «The new phrase says exactly that: KP, top movers, s_(a−1), …, s_b, all 2,704 intervals, 516 with a ≥
    2.».
  No fix weakens a signed statement; F-a turns a DEAD item into a signed implication; F-b to F-f change packet text or the line's
  wording only; entry 2 (R11) changes one DATA phrase of the line only.
- Not signed: packet §8 (DATA, machine checks, pins, EXCLUDED, TARGET diff, READING; «DATA / READING (not to sign)», l. 20), in
  particular the counts of l. 256-267 and the READING «So T is polynomial at degree ≤ 2 iff the pair flip counts are (PAIR-MOVES with F
  ≤ T), and every bound on them must come through the moves of the pair's own movers, i.e. through the Ξ side (RETURN, RENEW).» (l.
  280-282); RENEW's reading (l. 160-163); TOWER's READING and DATA (fixes l. 22-27). OPEN, not claimed: CONJECTURE PAIR-LIN (l. 112);
  CONJECTURE RENEW-COUNT (l. 164); PM′_S, PAIR-POLY, SLOT-TRADE (l. 274); any bound on flips(a, b), WE_x, KF_x or R(x, k); PAIR-MOVES
  and RETURN at degree ≥ 3; LADDER outside 𝓛^R_d; whether any IDEAL-ACYC family has exponential T; G-N5-TIME.
- Referee strengthening (NOT part of this entry; referee remarks and own checks):
  (i) REFEREE-2 l. 74: RENEW (b) «(Holds also for a = 1, with s_0.)»; packet l. 152 states (b) for every top-only interval.
  (ii) REFEREE-2 l. 86: in RETURN-COUNT, «equal Ξ-targets of the two options are counted twice in R(x, 0) + R(x, 1), which only weakens
       the bound.».
  (iii) REFEREE l. 111: mover 12 is «the only PM violator» of KILL_PM_compose; REFEREE l. 118 and REFEREE-2 l. 96-97: in T1_dd_top8,
        mover 10 (level 4) moves 8 times.
  (iv) The referees' own lemma checks (DATA, not proofs): REFEREE keys_check.py on 434 in-tree files and 2 × 1,500 random genomes
       (19,350 runs; keys_logs, 0 violations, controls fire); REFEREE-2 r2lemmas.py on 4,000 random genomes (88,082 runs) and 119 corpus
       files, «LADDER both inequalities and F(l) ≤ 3^(l+1) − 1 (28,864 ladder runs)», RENEW (b) on the full key form (12,501 intervals),
       0 violations.
- Honest limits: (i) A STRUCTURE / REDUCTION statement on the key side of the IDEAL model: LOCAL-KP, PAIR-KF and CASCADE make a degree-2
  mover's key preference a function of its W-closure and of one pair order, PAIR-MOVES and LADDER bound moves and pair flips by pair
  flips, RENEW, MERGE and RETURN describe the Ξ side; it bounds nothing polynomially (LADDER's bound 3^(l+1) − 1 is exponential; no
  bound on flips(a, b) is claimed); G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim. (ii) PAIR-KF, PAIR-MOVES,
  LADDER and RETURN are stated at degree 2 (PAIR-MOVES: every mover of degree ≤ 2); degree ≥ 3 is not covered by them; Ξ-cyclic genomes
  are not covered. (iii) TOWER is an implication: an exponential flip count of the doubling tower needs an exponential T in the same
  run; it does not say that no IDEAL-ACYC family has exponential T, and the tower is not DEAD. (iv) DEAD PM and PMV kill two per-mover
  lane conjectures by one instance each; the PM instance is outside 𝓛^R_d and R109's 𝓛_d (levels 1 and 4 have more than two movers);
  PMV's instance is in 𝓛^R_5; nothing is claimed about PM restricted to 𝓛^R_d or 𝓛_d, about PM′_S, or about a growth rate of VR. (v) The
  DATA is per statement, as the line's DATA parenthesis says, with these exact sets: keycheck.py runs 413 in-tree genome files of boxes
  150-172 (well-formed, with a start, N ≤ 30; 384 distinct contents) from their stored starts and 400 random IDEAL-ACYC genomes (levels
  1-4, 1-3 movers per level, degree 2 or 3 with some degree-1 movers) from every start if there are at most 64, else the genome start
  and 63 random ones: 13,813 runs, 14,027 steps; LOCAL-KP (a) and MERGE (b) on random states of each genome (MERGE on degree-2 movers
  only, options 0 and 1); the constant-keys clause of RENEW is counted by keycheck.py in its KP form on all 2,704 top-only intervals,
  516 of them with a ≥ 2; LADDER's first inequality on 231 runs of 𝓛^R genomes (58 of them one-level); PAIR-MOVES, the rest of LADDER
  and TOWER have no lane count (TOWER's values on dd_d5_F14 are DATA). (vi) Every statement is about R104's IDEAL model on acyclic
  Ξ-graphs; nothing is said about a real N5 run or a parity game beyond what R104 already says (packet l. 276-278). (vii) Premises:
  RESULTS R104's definition, R105's ENC, MONO, XI-NEW, RISE and (degree ≤ 2) KEYFLIP read with Erratum E-2 (E2c), and R110's definition
  of 𝓛^R_d; R106-R109 are not used. No lit note, no lane file, no outside source, no machine premise. No Lean. (viii) TOWER is proved in
  docs/new/P-IDEAL-KEYS-fixes.md (F-a), which the line's source note names («docs/new/P-IDEAL-KEYS.md with its fixes entry 1,
  docs/new/P-IDEAL-KEYS-fixes.md»). (ix) Names: «R111» here is this RESULTS entry, not L-RED's box R111 (cited in R86); «LADDER» is the
  corollary on 𝓛^R_d, not R106's LADDER-LP; «MERGE» and «RETURN» are this packet's Ξ-side lemmas, not the MERGE items of R37 and R67 nor
  the RETURN and SW-RETURN items of R12 and R73-R98; «W(x)» is the W-closure of x; «τ» is the top level, not N5's strategy τ; «flips(p,
  q)» counts key-order flips, not DE35's Gflips; KF_x, KP_s(x) and Mv_t are R105's; dd_d5_F14 is the genome of R109's LIFT champion of
  that name (sha1 06f0e501…). (x) The instances are the lane's (box 166) and L-RED's (dd_d5_F14), used here only as counterexamples and
  as TOWER's DATA; T is R104's number of steps.
- Data (DATA, not proof): experiments/new/box172/keycheck.py (l-new b302bbf5, sha1 6ce4693dda9f5baac0f524312009955d89a0a41a, 242 lines;
  deterministic, seed 172; simulator: experiments/new/box150/check.py's Gen, l-new 0ebddcf5, sha1
  019de0f7b36dcbd47743b3d27b4a1a93549d574b, 214 lines), output frozen in experiments/new/box172/keycheck.out (sha1
  5100eb30482a1c5ceb60b7ed84b38d7700213770, 8 lines) and wired into experiments/new/check.sh block «P-IDEAL-KEYS» (l. 911-918 at
  1a178aff, with sha1 pins of the packet, L-1, keycheck.py, keycheck.out, the three instances, the fixes and L-2; unchanged at 06d4238d;
  at 432edf82, still l. 911-918, l. 913-915 changed: the pins also hold L-3 c29f0a93 and the fixes file at entry 2, 504403c3). L-3's
  DATA parenthesis: «(DATA, experiments/new/box172/keycheck.py on 413 in-tree genome files from their stored starts and 400 random
  acyclic genomes from up to 64 starts each, 13,813 runs: LOCAL-KP 0 violations on 27,102 (state pair, mover) checks and, for KF_x ≤
  WE_x, on 90,811 (run, mover) pairs; PAIR-KF 0 on 34,113 (run, degree-2 mover of level ≥ 1) pairs; CASCADE 0 unclassified of 15,614
  flips; LADDER's first inequality 0 on 231 runs of 𝓛^R genomes; RENEW 0 on 520 (step, mover) pairs at the first steps of top-only
  intervals starting at t ≥ 2 and, for the constant key preference KP of the top movers on s_(a−1), …, s_b, on all 2,704 top-only
  intervals (516 of them with a ≥ 2); MERGE 0 on 19,932 (state, degree-2 mover) checks; RETURN 0 on 722 consecutive move pairs and
  RETURN-COUNT 0 on 50,260 (run, degree-2 mover) pairs; flips ≤ T 0 on the same runs; PAIR-MOVES and the rest of LADDER: no separate
  DATA; the two DEAD instances replayed by the same tool and by the box 150 checker; TOWER, on dd_d5_F14: F(0..4) = 2, 3, 6, 14, 7 and T
  14, the doubling step attained at level 3 (F(3) = 14 = 2(1 + F(2)) = T) and not at level 4 (2(1 + F(3)) = 30 > 14))». What each count
  covers (keycheck.py, read by me): LOCALKP compares every key of x under a random state s and a state s′ that agrees with s on W(x) (6
  random states per genome, every mover); KFWE every (run, mover); PAIRKF every (run, mover of degree 2 and level ≥ 1), KF_x against
  flips of its W-target pair (0 if equal); CASCADE every flip of a same-level pair, classified own or below; LADDER F(l) ≤ moves(2l) +
  moves(2l + 1) + F(l − 1) for l = 0, …, d − 1 with F(−1) := 0; RENEW the 520 (step, mover) pairs at the 516 first steps a ≥ 2 (573
  pairs at every top-only step t ≥ 2); RENEWB KP of every top mover on [a − 1, b], every top-only interval (2,704: 516 with a ≥ 2, 2,188
  with a = 1); MERGE random states, degree-2 movers, the difference v(x, 0) − v(x, 1) under a state that agrees on the two prefixes;
  RETURN and RETCNT degree-2 movers; KEYFLIP (R105, sanity, not in the line) 51,431 (run, mover) pairs of degree-≤-2 genomes. Controls:
  «LOCALCTL 48435» and «MERGECTL 23272» (changing one mover of W(x), resp. of a prefix, changes a key, resp. the difference).
  The block's outputs, reproduced by both referees at b302bbf5 and re-run for this draft (2026-11-06T01:56:01Z-01:56:04Z from a `git
  archive` of 1a178aff's experiments/new and docs/new, rc 0, PASS line ending «fixes 26088848, line L-2 fb1b2276: PASS»; keycheck.py's
  output byte-equal to keycheck.out; again at the second fill, 2026-11-06T05:43:30Z-05:43:33Z from a `git archive` of 432edf82's
  experiments and docs/new, rc 0, PASS line ending «fixes 504403c3, line L-2 fb1b2276, line L-3 c29f0a93: PASS», keycheck.py's output
  again byte-equal to keycheck.out): «SCOPE corpus 413 random 400 runs 13813 steps 14027»; «LOCALKP 0 LOCALCTL 48435 KFWE 0 PAIRKF 0
  CASCADE 0 LADDER 0 FLET 0 RENEW 0 RENEWB 0 MERGE 0 MERGECTL 23272 RETURN 0 RETCNT 0 KEYFLIP 0»; «DEAD PM KILL_PM_compose_dd_d5_F14
  valid True deg 2 N 15 T 14 mover 12 desc 4 moves 6 bound 5»; «DEAD PMV dd_d5_F14 valid True LR True N 10 T 14 mover 6 desc 7 VR 10
  bound 8»; «DEAD TOWER dd_d5_F14 T 14 pair flips by level [2, 3, 6, 14, 7] moves [1, 1, 3, 1, 3, 3, 7, 7, 3, 2] doubling F(3) = 2(1 +
  F(2)) True next 2(1 + F(3)) = 30 > T True»; on each of the three instances «TOTAL genomes 1 runs 1 steps 14 XSIM 0 TOPO 0 MONO 0 XINEW
  0 RISE 0 CHAIN 0 KEYFLIP 0 DECR 0 TOPMONO 0 RBOUND 0 RESTR 0 ICHARGE 0 REC 0 VIOL 0 (info REC148 0)». REFEREE §3 l. 130-132
  («keycheck.py regenerates keycheck.out identically»); REFEREE-2 l. 123-126 and Add. 1 l. 189 («exit 0»).
  REFEREE (successor 24; own docs/referee/scratch/keys_probe.py and keys_check.py on its simulator t3r_sim.py, «my simulator t3r_sim.py
  from R104's text; no lane code», logs keys_logs/): the three instances recomputed, every value of §7 equal (l. 108-118); its lemma
  checks on 434 in-tree files (10,350 runs) and two sets of 1,500 random genomes (4,500 runs each), 0 violations, with controls (l.
  119-129); «The random sets are weak (short runs); the corpus carries the coverage.» (l. 129).
  REFEREE-2 (successor 28; own docs/referee-2/R2-P-IDEAL-KEYS/r2sim.py and r2lemmas.py, «written from R104's text: Ξ-values compared as
  β-SETS by the largest-rank β of the symmetric difference, not through ENC integers; no lane code imported»; outputs r2sim_dead.out,
  r2lemmas_seed28_4000.out, r2lemmas_corpus.out): the instances recomputed (l. 88-97); 4,000 random genomes, 88,082 runs, and 119 corpus
  files, 0 violations of every check, controls fire (l. 112-122).
  No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-P-IDEAL-KEYS.md: successor 24's report ece8c4eeee5fb7b9529382d7ae745eebd7b8edbf
  (2026-11-05T23:49:08Z, new file, 176 lines, sha1 55cf771dda81da770736e4098e6d6038d9479f0f, with scratch/keys_probe.py, keys_check.py
  and keys_logs/): §2-§6 and DEAD PM SIGN, DEAD PMV SIGN WITH GAP KY-1, the tower REFUSED as DEAD (KY-G1) with its implication signed,
  L-1 NOT YET (KY-L1) (l. 11-25); §C cb7e29098f7605a622577aeeb8a1548dbe8bcc34 (2026-11-06T01:26:42Z, 226 lines, sha1
  80d291030b66e05e68141f8b630ec8a7940b1dac, with scratch/keys_l2_bytetest.py): F-a SIGN, KY-1 and KY-G1 CLOSED, the byte test of L-2 (l.
  208-211), «L-2 MATCHES.» (l. 224), «Every item is now SIGNED: §2-§6, DEAD PM, DEAD PMV (KY-1 closed), and TOWER (as restated in F-a).»
  (l. 225); §C add. 1 fadbb9a06ea3d829366d01023cead7040d389e88 (2026-11-06T04:09:18Z, 243 lines, sha1
  d8ad9026df4de28230e1db7c8d33c839612ed08b; l. 1-226 = cb7e2909's, by cmp): the byte test of L-3 against C124 §5 (l. 233-236), «Verdict:
  L-3 MATCHES. All signatures stand.» (l. 243). REFEREE-2 docs/referee-2/R2-P-IDEAL-KEYS.md: successor 28's report
  ebcf52d06ecae0ae8caea4ae624233636fc103df (2026-11-05T23:51:25Z, new file, 161 lines, sha1 5156ea45aba4d865ef976de3f1c2da53b844cffd,
  with R2-P-IDEAL-KEYS/r2sim.py and r2lemmas.py): every statement SIGN, the tower DEAD in the scope of R-1, L-1 MATCHES after W-1 to W-3
  (l. 12-25); Addendum 1 87b80d170ecca6c6a6c2d4e61e1daf78845ef7fc (2026-11-06T01:26:59Z, 189 lines, sha1
  493871a6b2502eee6f3c6e17506dcaeb5866865c; l. 1-161 = ebcf52d0's, by cmp): fixes entry 1 CORRECT, F-a TOWER SIGN and the DEAD sign
  withdrawn (l. 168-173), «**Line L-2: MATCHES.**» after its byte test (l. 181-184); Addendum 2 7ff32432964d8adbf30d75932f37552de810434d
  (2026-11-06T04:13:09Z, 201 lines, sha1 989ac4de08274fd3f6204bbac85113b2853322d5; l. 1-189 = 87b80d17's, by cmp): fixes entry 2 CORRECT
  (l. 195), «**Line L-3: MATCHES.**» after its byte test (l. 199-201). Lane: freeze and L-1 b302bbf5728feb0b62a1295ba979102617686566,
  fixes entry 1 and L-2 1a178affc45733577e2f2db0aa1b74f19aa7e244, fixes entry 2 and L-3 432edf823ddcf4d70d38a44eb8d07a7e09ef4829.
  INDEPENDENCE: REFEREE l. 2-3 «Independent: I did not open or list docs/referee-2/ on this packet before this report was pushed.»;
  REFEREE-2 l. 2-3 «Independent: docs/referee/ not read for this packet before this push.». REFEREE's report (23:49:08Z) precedes
  REFEREE-2's (23:51:25Z) by 2 min; neither cites the other's first report; each recomputed the three instances with its own simulator
  written from R104's text. In the second round each read the other's item labels only through the fixes entry (REFEREE §C l. 183-184;
  REFEREE-2 Add. 1 l. 167). Differences, resolved: on the tower, REFEREE refused the DEAD and REFEREE-2 signed it only in its R-1 scope;
  both now sign TOWER, and REFEREE-2 withdrew its DEAD sign; REFEREE alone found KY-1 (REFEREE-2 Add. 1 l. 174 «my miss»), REFEREE-2
  alone W-1 and N-1; both found the DATA units (KY-L4 = W-2) and the non-verbatim quotes (KY-P1, KY-L3 = F-1, W-3). Both SIGN the same
  statements and both MATCH L-2 and L-3 (each byte-tested L-3 against C124 §5 with its own script). No disagreement in substance.
- TARGET.md diff: TARGET.md §1-§3 define parity games («A parity game is G = (V, V_E, V_O, E, pr) with V finite»), the regions W_E, W_O,
  M4 (§2 «There is a deterministic algorithm A and a polynomial p such that for every parity game G, A on input G halts within») and the
  word-RAM cost model; no statement of this entry mentions a parity game, a winning region, an algorithm's running time or a cost model
  (packet §8 l. 276-278 «Diff against TARGET.md: no statement mentions a parity game, a winning region, an algorithm's running time or a
  complexity class.» «None is an M4 or M3 claim, none bounds anything polynomially (LADDER's bound is exponential), none is a gauntlet
  step. G-N5-TIME stays OPEN.»; REFEREE §4 l. 135-136 «Not M3, not M4, not a gauntlet step. LADDER's bound is exponential. G-N5-TIME
  OPEN. Agreed with §8.»; REFEREE-2 l. 129-131 «No M3 / M4 / M4-R claim, no gauntlet step; the only bound (LADDER) is exponential.
  G-N5-TIME stays OPEN.»). The line (L-3) makes no M4 claim and no TARGET claim; its tail reads «a STRUCTURE / REDUCTION statement
  inside the IDEAL model on the key side; bounds nothing polynomially (LADDER's bound is exponential)» and «G-N5-TIME stays OPEN; not
  M3, not a step-4 pass, not a TARGET.md claim» (L-3, by script). Not a step-4 pass. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER R110's UPDATE of G-N5-TIME (GAPS at d056db87, last changed by d056db87: the last
UPDATE on l. 11 is R110's, «UPDATE 2026-11-05 20:08Z: RESULTS R110 (P-IDEAL-FLIP; CHECKER C122 32f65fe0) …», before the row's closing «
|»), built by script (upd111b.py: upd111.py's 14 controls and procedure, unchanged, run on L-3; upd111.py: upd110b.py's procedure and
R97-R109 controls unchanged, R110's control added (14 controls, True); build() of upd100L3.py unchanged for the label move, on the claim
body with a sentinel tail as for R102 and R105-R110; the tail rule of (9) with R107's step for the unlabelled DEAD clause; one
adaptation for the «(DATA, » opening, cross-checked against a direct opening of the DATA parenthesis: True; to check (9)) only from the
clauses of the title line L-3: labels behind their clauses; the DEAD clause verbatim after «(TOWER, by flips ≤ T)»; « (2026-11-05) — » →
«: »; the DATA parenthesis before the source parenthesis opened as «; DATA, …»; «G-N5-TIME stays OPEN» and «not M3, not a step-4 pass,
not a TARGET.md claim» dropped; the source parenthesis kept; «. G-N5-TIME stays open.» at the end. The same script reproduces R97's to
R110's LANDED UPDATEs (GAPS l. 11) byte for byte. L-3 holds no "|"; the UPDATE holds none (5,669 bytes, 121 «(» / 121 «)»; sha1 of the
line without newline, placeholders unfilled: 284c9dea8e192568f53cf0425dc6ee00c2d7b42d, = C124 §4; it equals the first fill's UPDATE with
the one C124 §5 replacement, True). <DATE> is the landing date (YYYY-MM-DD, by date -u at the landing commit; C114 Add. 1 E-1), <HH:MM>
the landing time and <checker> the CHECKER C124 commit, all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R111 (P-IDEAL-KEYS; CHECKER C124 <checker>) [refereed-only] LANDED: In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of R104 used; RESULTS R105's ENC, MONO, XI-NEW and RISE, and at degree ≤ 2 its KEYFLIP, read with moves(x) the number of steps t with x ∈ Mv_t as in RESULTS Erratum E-2 (E2c); and RESULTS R110's definition of 𝓛^R_d only), on acyclic Ξ-graphs, any number of movers per level, with Mv_t the movers of step t, T the number of steps of a run, KP_s(x) the option of x with the least key under s, KF_x the number of steps t with KP_(s_t)(x) ≠ KP_(s_(t−1))(x), W(x) the movers reachable from x along W-targets of any options (x excluded), WE_x the number of steps moving a mover of W(x), for two distinct movers p, q of one level a flip of (p, q) at step t a change between s_(t−1) and s_t of the order of the keys of their current options, flips(p, q) the number of steps at which (p, q) flips, v_s(x, k) the integer value of option (x, k) under s (R105 ENC) and cv_s(x) := v_s(x, s(x)): at any degree, if two states agree on W(x) then they give every option of x the same key, so KP(x) is the same and KF_x ≤ WE_x (LOCAL-KP); for a mover x of degree 2 and level ≥ 1 with W-targets a, b of its two options, KF_x = 0 if a = b, and KF_x = flips(a, b) if a ≠ b, x key-preferring its option 0 under s iff the current option of a has the smaller key (PAIR-KF); if every mover has degree ≤ 2, moves(x) ≤ 1 + flips(a, b) for such x with a ≠ b and moves(x) ≤ 1 for every other mover, so T ≤ N + the sum of those flip counts (PAIR-MOVES); at any degree, at every step at which two distinct movers p, q of one level l flip, p or q moves, or l ≥ 1, neither moves, their current W-targets w_p ≠ w_q and (w_p, w_q) flips at the same step, and flips(p, q) ≤ T (CASCADE); on 𝓛^R_d with F(l) := flips(2l, 2l + 1), F(0) ≤ 2, F(l) ≤ moves(2l) + moves(2l + 1) + F(l − 1) and moves(x) ≤ 1 + F(lev(x) − 1) for lev(x) ≥ 1, so F(l) ≤ 2 + 3F(l − 1) ≤ 3^(l+1) − 1 (LADDER); at any degree, with τ the largest level, a step top-only when all its movers have level τ and a top-only interval a maximal interval [a, b] of top-only steps, if a ≥ 2 then step a − 1 moves a mover of level below τ and every mover h of step a, moving to w, has w ∉ A_(s_(a−2))(h) (A_s(h): h's current option under s and its options strictly better under s), v_(s_(a−1))(h, w) > v_(s_(a−2))(h, w) and some strict Ξ-descendant of h on the chain of (h, w) under s_(a−2) moving at step a − 1, and the keys of every mover of level τ are constant on s_(a−1), …, s_b (RENEW); at any degree, for two distinct options k, k′ of x and a state s, v_s(x, k) − v_s(x, k′) depends only on the options under s of the movers of the two chains before their first common mover (MERGE); for a mover x of degree 2 that moves to o at step t_1 and next moves at step t_2, the Ξ-target z of its other option is a mover with cv_(s_(t_2−1))(z) > cv_(s_(t_1−1))(z), so moves(x) ≤ 1 + R(x, 0) + R(x, 1) with R(x, k) the number of steps at which cv of the Ξ-target of (x, k) rises (0 if that target is the exit X) (RETURN); a run in which the doubling step of box 169, «F(l) = 2(1 + F(l − 1))» iterated level after level, reaches F(l) = 2^(l+1) − 2 has T ≥ 2^(l+1) − 2 (a READING, not a refutation: the doubling tower is not a shortcut around G-N5-TIME) (TOWER, by flips ≤ T); and DEAD: the lane conjecture PM («moves(x) ≤ (deg(x) − 1)(1 + desc(x))» for every mover x, desc(x) the number of strict Ξ-descendants of x) is false, by experiments/new/box166/out/KILL_PM_compose_dd_d5_F14.json (degree 2, N 15, T 14, mover 12 with desc 4 moving 6 times; sha1 c025a4b6…); the lane conjecture PMV («VR(z) ≤ 1 + desc(z)» for every mover z, VR(z) the number of steps at which cv(z) rises) is false, by L-RED's 𝓛^R_5 genome dd_d5_F14 (experiments/new/box172/inst/dd_d5_F14.json, sha1 06f0e501…; T 14, mover 6 with desc 7 and 10 rises): a STRUCTURE / REDUCTION statement inside the IDEAL model on the key side; bounds nothing polynomially (LADDER's bound is exponential); the conjectures PAIR-LIN, PM′_S and RENEW-COUNT are not claimed; Ξ-cyclic genomes are not covered, and degree ≥ 3 is not covered by PAIR-KF, PAIR-MOVES, LADDER or RETURN; DATA, experiments/new/box172/keycheck.py on 413 in-tree genome files from their stored starts and 400 random acyclic genomes from up to 64 starts each, 13,813 runs: LOCAL-KP 0 violations on 27,102 (state pair, mover) checks and, for KF_x ≤ WE_x, on 90,811 (run, mover) pairs; PAIR-KF 0 on 34,113 (run, degree-2 mover of level ≥ 1) pairs; CASCADE 0 unclassified of 15,614 flips; LADDER's first inequality 0 on 231 runs of 𝓛^R genomes; RENEW 0 on 520 (step, mover) pairs at the first steps of top-only intervals starting at t ≥ 2 and, for the constant key preference KP of the top movers on s_(a−1), …, s_b, on all 2,704 top-only intervals (516 of them with a ≥ 2); MERGE 0 on 19,932 (state, degree-2 mover) checks; RETURN 0 on 722 consecutive move pairs and RETURN-COUNT 0 on 50,260 (run, degree-2 mover) pairs; flips ≤ T 0 on the same runs; PAIR-MOVES and the rest of LADDER: no separate DATA; the two DEAD instances replayed by the same tool and by the box 150 checker; TOWER, on dd_d5_F14: F(0..4) = 2, 3, 6, 14, 7 and T 14, the doubling step attained at level 3 (F(3) = 14 = 2(1 + F(2)) = T) and not at level 4 (2(1 + F(3)) = 30 > 14) (P-IDEAL-KEYS, docs/new/P-IDEAL-KEYS.md with its fixes entry 1, docs/new/P-IDEAL-KEYS-fixes.md; L-NEW successors 54-55). G-N5-TIME stays open.

Addendum (subagent, for the Lead; does not land; written 2026-11-06T02:17:22Z by date -u). (1) FIRST FILL on line L-2 (l-new 1a178aff,
sha1 fb1b2276…), to CHECKER C124 (G-0: C123 is named for P-TR3; if the Lead gives R111 C123, substitute by script). NOT pushed; the only
commits I made are the four merges (--no-ff) d9d540e4 (l-new 06d4238d), 60a9925a (referee cb7e2909), fdd1f0f0 (referee-2 6c6f2033) and
9ab24552 (checker 21ff8727) into trunk 7a976cc4, as briefed; this draft is a new, untracked file. Push trunk before landing. (2) TITLE
l. 439 = "### R111 [refereed-only] " + L-2 without its newline + ", CHECKER PASS (docs/checker/C124.md, checker PENDING)", checked by
script after the fill (fill111.py, chk111.py): equal, byte for byte (True); the only «### R» heading of this file; 120 + 1 «(» and 120 +
1 «)» (L-2's plus the fill's), balanced. (3) BODY l. 439-725 (python slice d[438:725]; 0 "|" in the range, by script); GAPS
preamble l. 727-738 (its only "|" are the two inside the quoted closing « |», as in R107's to R110's preambles); UPDATE l. 739
(d[738]; one line, 0 "|", one each of <DATE>, <HH:MM>, <checker>; 5,575 bytes; sha1 6a454ec53c0fb5d81daa18cf3bbf475237d7c3f6 of the
unfilled line without newline; controls True ×14: R97's-R110's landed UPDATEs). No Dead-ends row is drafted ((14)). A landing script in
the shape of land110.py slices d[438:725] for the entry and reads d[738] for the UPDATE (with «R111», «R110» as PREV, «C124»
and the GAPS l. 11 assertion on «RESULTS R110 (P-IDEAL-FLIP» in place of R110's values). (4) RE-RUNS: check.sh block «P-IDEAL-KEYS» from
a git archive of 1a178aff (01:56:01Z-01:56:04Z, rc 0, PASS); my interval and corpus split (kcstats.py); my own simulator on the three
instances (mysim111.py); the L-1 → L-2 byte test and token diff (wdiff111.py); the premise quote test (prem111.py); the UPDATE build
with its 14 controls (upd111.py). NOT RUN: the referees' tools (their committed logs read instead), the full check.sh,
scripts/verify.sh. (5) QUOTE SWEEP: chk111.py (chk110b.py's rule: outermost guillemet quotes, whitespace joined, split at the ellipsis,
parts of 6+ characters; sources: packet, L-1, L-2, fixes, the referee files at their head commits, the referee logs and outputs,
docs/new/N5-PERMOVER-box165.md, N5-PMKILL-box166.md, N5-PAIRLIN-box169.md, notes/L-NEW.md at 1a178aff, check.sh and keycheck.py at
1a178aff, keycheck.out, RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, NOW, LEAD-STATE, TARGET.md, CLAUDE.md, C118-C122, notes/CHECKER.md,
R110-draft, my re-run outputs, the commit subjects cited): 521 outermost quotes, 428 parts of 6+ characters, every part found (0 not
found); in the title and body alone 142 quotes, 130 parts, 0 not found; GAPS preamble and UPDATE 15 quotes, 11 parts, 0 not found.
Line-precise check of the referee verdicts and other cited lines: 170 of 170 (source, cited line range, quote) triples found verbatim,
whitespace-normalised, inside the cited lines. Every sha1, line count and commit time cited was re-measured in this session (sha1sum, wc
-l, cmp, git log -1 on the commit), not copied from a report. (6) DISCREPANCIES: see (11) (D-1 to D-8; none affects a verdict) and G-0
to G-14. I found no error in a signed statement. (7) FLAGS FOR THE LEAD AND CHECKER: G-0 (CHECKER number: C124 used, C123 named for
P-TR3); G-9 (i) = REFEREE-2's optional P-1 («for the constant keys» counts KP constancy; open, for CHECKER; line not changed, per the
brief) and G-9 (ii) (2,188 of the 2,704 intervals have a = 1, outside the line's «if a ≥ 2» clause; new); G-8 (b) (a labelled READING
inside TOWER's clause). Nothing else is REQUIRED from my side. (8) NOT VERIFIED: the Lead brief of BOX 172 and the 00:47Z relay beyond
the Lead commits bc05394a, 7e456b8c and e7990774; L-RED's replay of the PM instance (packet l. 221-222); the referees' tools were not
re-run (their logs were read); scripts/verify.sh and the full check.sh were not run. Scratch files (not committed) in
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r111: R111-template.md, fill111.py,
chk111.py, lp111.py, upd111.py / upd111.txt / upd111.out, wdiff111.py / wdiff111.out, prem111.py / prem111.out, kcstats_make.py /
kcstats.out, mysim111.py / mysim111.out, runw172.sh / w172.out / w172raw.out, sim111.py / sim111.out, and the archive arch1a17/. (9)
LANDING SIMULATION (sim111.py, on in-memory copies of RESULTS and GAPS at local trunk): RESULTS 12,176 -> 12,464 lines (wc -l), a pure
insertion of 288 lines (the entry block with "checker PENDING)" filled, plus one blank line) directly after R110's block (R110 l.
11,323-11,596, blank l. 11,597, byte-unchanged: True; R109's block with its blank line, l. 11,030-11,322, byte-unchanged: True): True;
R111 at l. 11,598-11,884, blank l. 11,885, the next line (**Erratum E-1**) moves to l. 11,886, «**Erratum E-2**» to l. 11,899, «## Dead
ends» to l. 11,927; order R110, R111, E-1, E-2, Dead ends: True; every other line byte-unchanged (common prefix and suffix: True); 0 "|"
inserted. GAPS: only l. 11 changes: True; new l. 11 = old l. 11 with its closing " |" replaced by " " + the filled UPDATE + " |": True;
"|" on l. 11 76 -> 76 (pipe count unchanged); «UPDATE 2026-» 45 -> 45 plus 1 UPDATE head with the simulation year 2099, now the last on
the line; 23 -> 23 lines (wc -l). Fill values used only for the simulation: <DATE> 2099-01-01, <HH:MM> 00:00, <checker> 0000000. (10)
THIS DRAFT'S SHA1: a file cannot state its own sha1. The sha1 of this file with the forty hex digits after the next colon replaced by
forty «0» characters is: 58d2452b1847726c0d1f9e1fc22d50b769b21ae4. The file's actual sha1 and line count are in the hand-back to the
Lead (and re-measurable with sha1sum).

Addendum 2 (subagent, for the Lead; does not land; written 2026-11-06T05:47:40Z by date -u). (1) SECOND FILL on line L-3 (l-new
432edf82, sha1 c29f0a93…), to CHECKER C124 Add. 1. NOT pushed; my commits: the five merges (--no-ff) c54f19b8, 6b95c066, 02d0f872,
1d689e9a, 7ad0389c and one commit holding this file. (2) TITLE l. 471 = "### R111 [refereed-only] " + L-3 without its newline + ",
CHECKER PASS (docs/checker/C124.md, checker PENDING)", checked by script (chk111b.py): equal, byte for byte (True); the only «### R»
heading of this file; 122 + 1 «(» and 122 + 1 «)», balanced. (3) BODY l. 471-780 (python slice d[470:780]; 0 "|"); GAPS preamble l.
782-794; UPDATE l. 795 (d[794]; one line, 0 "|", one each of <DATE>, <HH:MM>, <checker>; 5,669 bytes; sha1
284c9dea8e192568f53cf0425dc6ee00c2d7b42d of the line without newline, computed on the UNFILLED form, as C124 §4 states it, «sha1
284c9dea8e192568f53cf0425dc6ee00c2d7b42d of the line without newline»: equal). A landing script slices d[470:780] for the entry and
reads d[794] for the UPDATE. (4) NO PLACEHOLDER: both referees' byte tests of L-3 are on file, so everything in the entry is final for
C124 Add. 1 (the only fill left is the title's «checker PENDING)» and the UPDATE's three placeholders, at landing). (5) QUOTE SWEEP
(chk111b.py: chk111.py's rule and sources, the trunk files at the first fill's trunk 9ab24552, plus L-3, fixes, check.sh at 432edf82,
R-P-IDEAL-KEYS.md at fadbb9a0, R2-P-IDEAL-KEYS.md at 7ff32432, C124, the trunk files at 7ad0389c, my second-fill outputs): 562 outermost
quotes, 464 parts of 6+ characters, every part found (0 not found); in the title and body alone 160 quotes, 151 parts, 0 not found; GAPS
preamble and UPDATE 15 quotes, 11 parts, 0 not found. Line-precise: 201 of 201 (source, cited line range, quote) triples found verbatim,
whitespace-normalised, inside the cited lines. (6) WORD DIFF 462ac44d → this file (wd111b.py, difflib on whitespace tokens, Addendum 2
left out): 19 line regions, 51 token hunks (52 tokens deleted, 1284 inserted), every hunk in a region listed in the SECOND FILL
paragraph. (7) STALE STATUS in title and body (by script): «pending» 0 apart from the title fill «checker PENDING)»; «not yet» once,
REFEREE's L-1 verdict quoted as history (as at the first fill); «L-2» only as history (the line history, the L-2 verdicts and byte
tests, the fixes entries, the check.sh pins and PASS lines, R11's old string), never as the line of record; L-2 named as the current
line, by script: 0 times. (8) LANDING SIMULATION (sim111.py, unchanged, on in-memory copies of RESULTS and GAPS at local trunk): RESULTS
12,176 -> 12,487 lines (wc -l), a pure insertion of 311 lines (the entry block with "checker PENDING)" filled, plus one blank line)
directly after R110's block (R110 l. 11,323-11,596, blank l. 11,597, byte-unchanged: True; R109's block with its blank line, l.
11,030-11,322, byte-unchanged: True): True; R111 at l. 11,598-11,907, blank l. 11,908, the next line (**Erratum E-1**) moves to l.
11,909, «**Erratum E-2**» to l. 11,922, «## Dead ends» to l. 11,950; order R110, R111, E-1, E-2, Dead ends: True; every other line
byte-unchanged (common prefix and suffix: True); 0 "|" inserted. GAPS: only l. 11 changes: True; new l. 11 = old l. 11 with its closing
" |" replaced by " " + the filled UPDATE + " |": True; "|" on l. 11 76 -> 76 (pipe count unchanged); «UPDATE 2026-» 45 -> 45 plus 1
UPDATE head with the simulation year 2099, now the last on the line; 23 -> 23 lines (wc -l). Fill values used only for the simulation:
<DATE> 2099-01-01, <HH:MM> 00:00, <checker> 0000000. (9) NOT VERIFIED: the referees' tools not re-run (their files read);
scripts/verify.sh and the full check.sh not run. Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r111/fill2/ (edit111b.py, chk111b.py,
lp111b.py, wd111b.py, l3rel111.py / l3rel111.out, upd111b.py / upd111b.out / upd111L3.txt, runw172L3.sh / w172L3.out / w172L3raw.out,
arch432e/, R111-draft-462ac44d.md).
