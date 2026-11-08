# Draft RESULTS R121 (Lead; first fill 2026-11-08T02:00:21Z by date -u (subagent) on P-N5-ASC line L-2, docs/new/P-N5-ASC-line-L2.txt, l-new a5dcf9c6, sha1 f109cb69507efd863133a08a2e90096ad2acb7f5 (draft sha1 04323afb, CHECKER C135 0942e8be: FAIL E-1..E-4); SECOND FILL 2026-11-08T06:04:48Z by date -u (subagent) on P-N5-ASC line L-4, docs/new/P-N5-ASC-line-L4.txt, l-new a744677e, sha1 4017305a34eac21615ba8f172a9b899544d25659) — to CHECKER C135 Add. 1 — NOT LANDED; goes after R120 (LANDED at 5470cc0c), before Erratum E-1
SECOND FILL (2026-11-08T06:04:48Z by date -u, subagent; for CHECKER C135 Add. 1). Read at the origin heads of one fetch at 2026-11-08T05:50:40Z (git
fetch of claude/l-new, claude/referee, claude/referee-2, claude/checker, claude/vibrant-johnson-nxvvxo; date -u before and after the
fetch 05:50:40Z; I merged, committed and pushed nothing and edited docs/agents/R121-draft.md only): l-new 1a846565
(1a8465652b7e4125d6ed565f5c911142135ecb7b, 2026-11-08T05:20:47Z, «L-NEW successor 63 handover (box 195 / P-N5-END, P-N5-ASC L-3/L-4,
P-N5-QUIET L-1 and draft entry 2; open duties; traps); park», the branch head; git diff a744677e 1a846565 names only six files under
experiments/new/box194/draft_entry2/ and notes/L-NEW.md; the packet, the fixes file, L-1 to L-4, experiments/new/box193 and
experiments/new/check.sh are byte-equal at both, git diff --quiet), so the objects are those of a744677e
(a744677ea9e3721a3a29b59ffb69d3ae4272f520, 2026-11-08T04:54:26Z, «L-NEW P-N5-ASC fixes entry 4 + line L-4 (REFEREE 28 §E R5:
CHAIN-DECOMP hypothesis as packet l. 80); L-4 sha1 4017305a = REFEREE prediction; asc.pins 39 rows», L-NEW successor 63, the commit of
record) and of a2512364 (a25123643acfe5699a15f00887dbeec88faff9bc, 2026-11-08T03:44:19Z, «L-NEW P-N5-ASC fixes entry 3 + line L-3
(CHECKER C135 E-1..E-4: R1 source note, R2 L41 AS-1 sentence, R3 CHAIN-DECOMP signed sentence, R4 seq_t/ascent defined); L-3 sha1
0012d671 = C135 target; asc.pins 37 rows», successor 63). referee 8505df48 (8505df485ebb34ddba407dd3858442572cdd9936,
2026-11-08T05:24:04Z, «REFEREE successor 29: handover check (five questions)», the branch head); docs/referee/R-P-N5-ASC.md there is the
file of 013f821b (013f821bd31de10ee93abf4f5c279962e1570de9, 2026-11-08T04:24:28Z, «REFEREE 28: R-P-N5-ASC §E (L-3 = L-2 + R1-R4, byte
test PASS; R5 required: CHAIN-DECOMP hypothesis in the line)»; 312 lines, 27,052 bytes, sha1 600f8ba3677bc2ef38f7994d07bbdf7dc59dfedd;
cmp equal; its l. 1-270 = 94062059's file, by cmp) and has no §F at this fetch. REFEREE successor 29's byte test of L-4 (§F):
<R29-SF>. This draft states no REFEREE verdict on L-4; the token stands where that report's commit and verdict go, here and in the
entry (Addendum 2 (4) lists each place).
referee-2 05eb5181 (05eb5181e0af63723a038279cefe7582fe3d9846, 2026-11-08T05:25:54Z, «REFEREE-2 R2-P-N5-ASC Add. 5: packet
line numbers corrected (70-71, 74-76)», the branch head); docs/referee-2/R2-P-N5-ASC.md there 387 lines, 33,038 bytes, sha1
c00d75e653fe1be6acbfaaf170756ec3137d2df8; its l. 1-343 = 98b9622b's file (98b9622b99e0dfd16353c68572a74c9ee8eb7c8f,
2026-11-08T04:30:58Z, «REFEREE-2 32: R2-P-N5-ASC Addendum 4: L-3 (C135 R1-R4) MATCHES»; 343 lines, 28,766 bytes, sha1
8ea4552ae1f76c443b980017f0cd44894456da79) and its l. 1-316 = d3fed33c's, by cmp; Addendum 5 was committed at caa26282
(caa262828941b73116bb018351cfd605a1f04b95, 2026-11-08T05:25:44Z, «REFEREE-2 R2-P-N5-ASC Addendum 5: L-4 = L-3 + R5 byte test (MATCHES);
own OLDHYP/GLOSS counters»; the same size, sha1 322985ea0aca063432a499e5b70a52258e8fe444), and 05eb5181 changes two of its lines (packet
line numbers only). checker fa8add12 (fa8add12b8f81e827af46da77b051e1be13a970e, 2026-11-08T03:51:39Z, «CHECKER successor 21: HANDOVER to
successor 22 (C135 open: Add. 1 next)», the branch head; it adds notes/CHECKER.md lines only); docs/checker/C135.md is the file of
0942e8be (0942e8bebe1d18b63436daaec83b8a9b7f5eb52f, 2026-11-08T03:04:02Z, «CHECKER C135: R121 (P-N5-ASC) draft 04323afb @ 5b8c84dc FAIL
E-1..E-4 (source note, L41 tail, READING in CHAIN-DECOMP, seq_t/ascent undefined); exact L-3 0012d671, UPDATE f545cba7»; 93 lines,
10,123 bytes, sha1 87dfa1eb7dd600a33cb0ad7aad2fca516bdabbc4; cmp equal at fa8add12). a2512364, a744677e, 1a846565, 013f821b, 8505df48,
98b9622b, caa26282, 05eb5181, 0942e8be and fa8add12 are NOT ancestors of the local trunk c9591e35 or of origin trunk c8f42538 (git
merge-base --is-ancestor); a5dcf9c6, 94062059, d3fed33c and 5b8c84dc are. The Lead merges claude/l-new, claude/referee,
claude/referee-2 and claude/checker before landing.
Trunk: local HEAD c9591e35 (c9591e35ac3aca556e718468e701ab91c84eba4c, 2026-11-08T05:40:39Z, «Lead: R122 first fill (P-ACYC over L-3;
G-7 L41 + G-1 ruled, L-4 routed); REFEREE 29 + REFEREE-2 33 roster/restart rows; L-SI 45 + REFEREE-2 33 checks 5/5; log 05:05Z-05:25Z»;
origin trunk c8f42538 its parent; the working tree has the Lead's uncommitted docs/NOW.md and docs/agents/LANE-RESTART.md, and RESULTS
and GAPS equal HEAD, git diff --quiet). docs/agents/R121-draft.md at HEAD and at origin trunk is the first fill, sha1
04323afb36f0be67115e62694af2b850912b4b04 (committed at b83443b6, 2026-11-08T02:12:16Z; C135's object). RESULTS at HEAD: sha1
66e7119615efa5a0bb25b898e32b5b371c55c122 (= RESULTS at the first fill's 8912e145 and at 5470cc0c, R120's landing), 14,962 lines;
«### R118» l. 13607, «### R119» l. 13879, «### R120» l. 14114-14318, «**Erratum E-1**» l. 14320, «**Erratum E-2**» l. 14333, «**Note
E-3**» l. 14361, «## Dead ends (kept;» l. 14392. GAPS at HEAD: sha1 2a41c7654d4e9dedee7abc8591dfb792633bc2c9 (= the first fill's), 23
lines, l. 11 76 "|", 55 «UPDATE 2026-», the last R120's «UPDATE 2026-11-07 21:05Z: RESULTS R120 (P-TOWER-FUEL; CHECKER C134 0c816917)».
«R121», «C135» and «P-N5-ASC» occur 0 times in RESULTS and in GAPS (by script). Nothing landed on trunk since the first fill.
New sources: CHECKER C135 (read in full): «Verdict: FAIL (E-1 to E-4; one L-3 with four replacements, §5)» (l. 15); «All four are the
drafter's flags with its exact strings: G-1 (R-B), G-7 (R-G, the Lead's L41 ruling), G-2 (R-R) and G-2 (ii) (R-Q).» (l. 16); E-1..E-4
(l. 20-37); the G-U ruling «R118's procedure applies» (l. 38-43); G-P (l. 44); everything else PASS (§4: the two blocks re-run from git
archive df0d2a25, every DATA figure against check193.out, units, premises, quotes, the TARGET.md diff); §5: L-3 (sha1 0012d671…, 5,154
bytes) and its UPDATE (sha1 f545cba7…, 5,184 bytes, «It is 6635b14e with R1-R4 applied.», l. 82), and the second-fill list (l. 83-84).
Fixes entries 3 and 4 (docs/new/P-N5-ASC-fixes.md l. 93-125 at a2512364 and l. 127-140 at a744677e; read in full; the file at
a744677e 140 lines, 12,728 bytes, sha1 9fb85374b6555e9e2858004fa33ef9d09b2c39aa); L-3 (a2512364, the file's only commit) and L-4
(a744677e, the file's only commit); experiments/new/box193/mkl3_193.py (28 lines) and mkl4_193.py (14 lines), read in full;
experiments/new/box193/asc.pins at a744677e (39 rows, 2,310 bytes, sha1 d7d10aaed0fa29b462c38143472b4ab3e9e37152; against a5dcf9c6's:
the fixes file re-pinned, L-3, mkl3_193.py, L-4 and mkl4_193.py added); REFEREE's §E (l. 272-312, read in full; its scratch tools listed,
not re-run); REFEREE-2's Addenda 4 (l. 318-343) and 5 (l. 345-387), read in full (its tools listed, not re-run); docs/agents/LEAD-STATE.md
l. 2729 («LEAD READINGS today: L41 applies to G-7 (R121 R-G)»), l. 2742 (REFEREE 28's R5 and the routing) and l. 2745 (the R121 plan).
Checks run at this fill (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r121b;
nothing written into the repository but this file). (a) l4rel121b.py: R1-R4 parsed from C135 §5 (wrapped lines joined with one space)
and from fixes entry 3 (l. 103-119): equal (True ×4); R5 parsed from REFEREE §E l. 303-304 and from fixes entry 4 l. 135-136: equal
(True); each old string once in L-2 (R1-R4) and in L-3 (R5), and once in the running line; L-2 + R1..R4 = L-3, L-3 + R5 = L-4, L-2 +
R1..R5 = L-4 (True ×3); each new string once in L-4; L-4 = 4017305a34eac21615ba8f172a9b899544d25659, 5,198 bytes, one line with its
newline, 5,094 characters, 867 tokens, 125 «(» / 125 «)», depth never negative, final depth 0, 0 "|", one « — », «[» 11 times,
«under [E-LEV]» 4 times, «R1xx» 0, «gauntlet» 0, «not a step-4 pass» once; token diff L-3 → L-4 two hunks (one token out, ten in), both
inside R5; the packet at a744677e and at the l-new head = the frozen 9c9cb50d… (True). mkl3_193.py (on C135 from 0942e8be) and
mkl4_193.py re-run from the archive of a744677e: rc 0, output cmp-equal to L-3 and to L-4. (b) check193.sh from a git archive of
a744677e (experiments, docs/new, scripts), 2026-11-08T05:53:16Z-05:54:01Z by date -u, rc 0, 71 output lines, byte-equal to the committed
check193.out (cmp); then the two check.sh blocks «BOX 193 ASC» and «P-N5-ASC» (check.sh l. 988-1003 at a744677e, byte-equal to
a5dcf9c6's, copied into a script and run from experiments/new of the archive), 2026-11-08T05:54:06Z-05:54:52Z, rc 0, «BOX 193 ASC: …
= frozen: PASS» and «P-N5-ASC: packet and 39 pinned files match asc.pins: PASS». (c) upd121b.py: r121/tools/upd121.py l. 1-69 exec'd
unchanged (r120b/tools/upd120b.py l. 1-311 with its one relaxed assertion, then the R120 control as landed, then run121() on L-2; its
file write not executed): the controls R97-R116 rebuilt from their lines and compared with GAPS l. 11 byte for byte, True ×20; R117,
R118, R119 and R120 as landed, each = its GAPS l. 11 segment, True ×4; all controls True ×24, the last UPDATE on l. 11 R120's; the
first fill's UPDATE on L-2 reproduced (6635b14e…, = draft d[491], True). run121() unchanged (R118's procedure, C135 G-U) on L-3: sha1
f545cba7c97eee853387a5efb617984538e27806, 5,184 bytes, = C135 §5's (True) and = 6635b14e… with R1-R4 applied, each old string once
(True). On L-4: sha1 d3a423302a45850e3400c0e15e14d7dfdd600508 (no newline, unfilled), 5,228 bytes, 5,126 characters, 866 tokens, 125
«(» / 125 «)», 0 "|", one each of «<DATE>», «<HH:MM>», «<checker>», «2026-11-07» 0 times, « — » 0 times; = the direct build (True). R5's
old string occurs 0 times in f545cba7…, because the procedure moves its label «(Lemma CHAIN-DECOMP)» behind the clause; R5 without that
label, «if the first e-vertex on v's play is f, then» → «if seq_t(v) = (f, …), i.e. the first e-vertex on v's play is f and f ∈
Π_t(v), then», has its old string once in f545cba7… and once in L-3, and f545cba7… with it applied = the L-4 UPDATE (True). Token diff
L-4 → UPDATE: 11 hunks, 43 tokens out, 42 in, the 11 hunks of C135's G-U ruling (the head; the five labels moved behind their clauses,
the fifth whole; « (2026-11-07) —» → «:»; the drop words; «61-62)» → «61-62). G-N5-TIME stays open.»). Appended after R120's UPDATE on
GAPS l. 11 it keeps 76 "|", R121's last, the prefix byte-unchanged (True). (d) opt121b.py (the optional R-I and R-A below, counts and
sha1s only); chk121b.py (title, block, UPDATE, placeholders, pipes, stale grep, quote sweep), lp121b.py (line-precise quotes new at this
fill), sim121b.py (landing simulation on c9591e35) and rec121b.py (the first fill's record byte-unchanged): Addendum 2.
C135's E-items and REFEREE's R5, resolved in L-4 (string checks by script, l4rel121b.py): E-1 (G-1, the source note) by R1: L-4 ends
«(P-N5-ASC, docs/new/P-N5-ASC.md with fixes entries 1-2, docs/new/P-N5-ASC-fixes.md; L-NEW successors 61-62)». E-2 (G-7, L41; the Lead's
ruling) by R2: «the proof of record of HUB-ASC-G's B = 0 case (F′_0 = F_0, DESC-POLY on the whole interval) is referee-originated
(REFEREE R-P-N5-ASC §3 AS-1, restated in P-N5-ASC's fixes entry 1 AS-1), signed by both referees» once in L-4, in the scope tail after
«§3-§5 do not use [E-LEV];», before «; DATA, clause by clause»; the entry's L41 and L43 quote both signatures and the empty joint gap
map. E-3 (G-2, the READING) by R3: «hence seq_t(v) = (f, seq_t(y_f))» once, «one forest» 0 times in L-4; the Reading stays in the body as
a proof step of HUB-ASC-G. E-4 (G-2 (ii)) by R4: «with seq_t(v) the e-vertices in Π_t(v) in play order, E_t(v) their set, an ascent of
seq_t(v) a step to a more relevant element,» once. R5 (REFEREE §E, new since C135): «(Lemma CHAIN-DECOMP) if seq_t(v) = (f, …), i.e. the
first e-vertex on v's play is f and f ∈ Π_t(v), then» once in L-4; the DATA clause «CHAIN-DECOMP: violations 0 in 24,818 (state, vertex)
pairs with a nonempty e-sequence» counts exactly the (state, vertex) pairs where this hypothesis holds (asc193.py l. 66-68: decunits per
(state, vertex) with seq, the e-vertices of v's play in Π_t(v), nonempty), so R5 also aligns the clause with its counter.
NOTES at this fill (for CHECKER; no line change proposed; the optional strings are exact, each old string once in L-4 and once in the
UPDATE, opt121b.py):
- N-I, THE «i.e.» IN CHAIN-DECOMP (REFEREE-2 Add. 5 N-1; NOTE, optional R-I). L-4's hypothesis is «seq_t(v) = (f, …)», glossed «i.e.
  the first e-vertex on v's play is f and f ∈ Π_t(v)». The gloss implies the hypothesis on every game (REFEREE-2 l. 365-367). The
  converse needs that no e-vertex g ∉ Π_t(v) precede f; REFEREE-2 shows that it can fail only when v's cycle node is an e-vertex (l.
  368-375) and measures 0 such plays (l. 376-377), and rules «note, no change required» (l. 368); no text shows that an e-vertex is never
  a cycle node, so the «i.e.» is an exact restatement on all measured data, not a proved one. The clause stays correct (it states the
  signed hypothesis first, and under either reading the conclusion holds). If CHECKER wants the line to assert no unproved equivalence:
  R-I "(f, …), i.e. the first e-vertex on v's play is f and f ∈ Π_t(v), then" → "(f, …), then" (the packet's l. 80 verbatim, with
  seq_t(v) defined in the line by R4): L-4 + R-I sha1 a51e0e899e5ba6ebbb0a53ca54f3dc865eccb6a5 (5,138 bytes, 124 «(» / 124 «)»), its
  UPDATE = the L-4 UPDATE with R-I, sha1 a5d63cb51369a960e65e680bd801fe41571bd82f (5,168 bytes).
- N-A, ASCENTS IN CS(M) (NOTE, optional R-A; not raised by C135). R4 defines «an ascent of seq_t(v)»; HUB-ASC(B)'s clause uses
  ascents of a hub's value in CS(M), whose items are compared by number (packet §2 l. 55 defines an ascent for any «sequence (c_1, …,
  c_p) of distinct items»). Optional R-A: "(items 1..M, a run of forests with every chain lex-nondecreasing)" → "(items 1..M compared by
  number, a run of forests with every chain lex-nondecreasing, an ascent a step to a larger item)": L-4 + R-A sha1
  eaff3343fa07decba94802bca0a46d97e8efcbf7 (5,252 bytes), its UPDATE 73154925b2faa666a7813393c7c4dee6d45956d5 (5,282 bytes); with R-I and
  R-A both: L-4 fe4d3f902b6afde93384ebf625fa9bebcea0e1d0 (5,192 bytes), UPDATE 3571ef76373c0143e5611cc34289e73ef139fadc (5,222 bytes).
- N-S, THE SOURCE NOTE'S SUCCESSORS (CLEAN by C135 E-1's statement of the rule, in my reading). L-4's note names «L-NEW successors
  61-62»; fixes entries 3-4, L-3 and L-4 are successor 63's (fixes l. 93, l. 127). Entries 3-4 carry no proof and change no statement
  («No tool or DATA output changes», l. 125, l. 139); C135 l. 22-23: «the note names the authors of proof-bearing text; a line-only
  entry need not be named». R118 and R120 landed with the same shape.
- D-8, STAMPS (history, no verdict affected). Fixes entry 4's heading «Lead 04:56Z» (l. 127) and LEAD-STATE l. 2742 «04:56Z Lead: R5 to
  L-NEW 63 (fixes entry 4 + L-4).» are later than a744677e (2026-11-08T04:54:26Z, author and committer date), which carries that entry;
  a Lead log stamp quoted by the lane, not the lane's own time. REFEREE §E «date -u at writing 2026-11-08T04:09Z» and REFEREE-2 Add. 4
  «2026-11-08 04:09Z by date -u», Add. 5 «2026-11-08 05:25Z by date -u» are each before or at their commits (04:24:28Z, 04:30:58Z,
  05:25:44Z).
Changes at this fill, and nothing else: line 1 (the header); this section; the title (L-4); in the entry: Object (successors 61-63; the
packet at a744677e and 1a846565; four fixes entries; L-4 the line of record; its line history L-1 to L-4; the L-3 and L-4 rounds of both
referees and C135), Claims signed (the rounds of §E, §F, Add. 4 and Add. 5; statement verdicts unchanged; (c) the Reading out of the line),
The RESULTS line (L-4; its clauses), Premise (the trunk c9591e35), L41 and L43 (the Lead's ruling, L-4's scope-tail sentence, both
signatures, the joint gap map), Fixes (header, entry-3 and entry-4 bullets, closing bullet), Not signed (the Reading; the R5 witnesses),
Referee strengthening (iv) (new), Honest limits (i) (trunk), (viii) (re-worded), (x) (new), Data (a744677e; asc.pins 39 rows; the re-run
for this entry and C135's), Signatures (REFEREE §E, §F, REFEREE-2 Add. 4, Add. 5, successor 63's commits), INDEPENDENCE (L-3's and L-4's
wording and byte tests; REFEREE-2's Add. 4 miss), TARGET.md diff (L-4); the GAPS preamble and the UPDATE (rebuilt from L-4); Addendum 2
(new). The FIRST FILL text below (from "FIRST FILL (this text)" to (14)) and the Addendum (1)-(10) are kept byte-unchanged as the
record of draft 04323afb on L-2 (rec121b.py): where they call L-2 the title line or the current line, raise G-1, G-7, G-2, G-2 (ii) or
G-U, propose R-B, R-G, R-R or R-Q, or give the first fill's line numbers, counts, slices and UPDATE sha1 (6635b14e…), they describe draft
04323afb at 02:02Z; C135 ruled G-1, G-7, G-2 and G-2 (ii) as E-1..E-4 (fixed by R1-R4 = R-B, R-G, R-R, R-Q), ruled the UPDATE procedure
(G-U: R118's) and kept the placement after R120 (G-P); REFEREE's R5 (§E) came after C135; the entry block now follows L-4.
FIRST FILL (this text). Read at the origin heads fetched at 2026-11-08T01:45:33Z-01:45:35Z by date -u (git fetch of claude/l-new,
claude/referee, claude/referee-2, claude/checker, claude/vibrant-johnson-nxvvxo and, for R220, claude/l-red; rc 0; I merged, committed
and pushed nothing and edited docs/agents/R121-draft.md only): l-new d9c49489 (d9c49489cef17fd829ea33d7b1e60c126dcab93e,
2026-11-08T01:08:08Z, «L-NEW P-N5-QUIET fixes entry 1 (L-RED R221): …», the branch head; git diff --quiet a5dcf9c6 d9c49489 on the
packet, the fixes file, L-1, L-2 and experiments/new/box193: equal; d9c49489 changes P-N5-QUIET files, box194 and one check.sh line of
the BOX 194 block), so the objects are those of a5dcf9c6 (a5dcf9c642d191aa95b0bbab08a97b180ce88925, 2026-11-08T00:40:20Z, «L-NEW
P-N5-ASC fixes entry 2 + line L-2 (W-3 E-MON unit incl. c_W; W-4 strict upward test in asc193.py, upfail 0 in 1,956); CS(8,1) = 126
(cubic's 128 fails)», L-NEW successor 62, the commit of record); the packet freeze 95dc76d7 (95dc76d7b71fd6832794eed94a3f76c1258cddf5,
2026-11-07T21:45:00Z, L-NEW successor 61) and fixes entry 1 / L-1 19cc23e3 (2026-11-07T23:23:53Z, successor 62). referee 94062059
(94062059582976623de438f1873a7725345f2252, 2026-11-08T01:11:46Z, «REFEREE 28: R-P-N5-ASC §D (fixes entry 2 CORRECT; L-2 MATCHES)», the
branch head; docs/referee/R-P-N5-ASC.md there 270 lines, 23,512 bytes, sha1 fba70e079241e258579d1b91903c85311e5655bb; its l. 1-238 =
d4b39be0's file (d4b39be0e5589cba49d08df3ca185332519b8dd6, 2026-11-07T23:51:43Z, §C: 238 lines, 20,911 bytes, sha1
51f3e4c7e8298cfedec9a31eea9d788771dd38b6) and its l. 1-196 = 26b2b516's file (26b2b51667d9ee3a0df318d127f844e6279b1d07,
2026-11-07T22:27:05Z, the report: 196 lines, 16,913 bytes, sha1 0f17c43c51c8658f82b51564c71b3a49f989b0d2), by cmp). referee-2 d3fed33c
(d3fed33cbe4694c3961e563e42cf438258697a9e, 2026-11-08T01:19:51Z, «REFEREE-2 32: R2-P-N5-ASC Addendum 3: fixes entry 2 CORRECT, W-3/W-4
met, L-2 MATCHES (l-new a5dcf9c6)», the branch head; docs/referee-2/R2-P-N5-ASC.md there 316 lines, 26,251 bytes, sha1
70dae6a5b89cc97ce1cb5847495bfe9d3082390f; its prefixes, by cmp: l. 1-281 = fcdc16b4's file (fcdc16b45ea2086ae307137036bacbcfc8d36a23,
2026-11-07T23:52:10Z, Add. 2: 281 lines, 23,056 bytes, sha1 073aadb16a09b4a04824736b6c63651897f04218), l. 1-230 = c4166c8b's
(c4166c8b49ffbace7ec09bd2edb5c6d9189b7f67, 2026-11-07T22:47:01Z, Add. 1: 230 lines, 18,574 bytes, sha1
4a9d3c1f411ddace1ecc6bde82a254ad68597278), l. 1-190 = 533744a5's (533744a51d23c45d7d6107041eef4dee29129253, 2026-11-07T22:17:18Z, the
report: 190 lines, 15,361 bytes, sha1 fd2c4e034d945e57d857f2a45c9a11b91335f372)). checker d38a2194
(d38a219480c105126bdee27e31ac4110d3af2e2a, 2026-11-07T22:38:19Z, «CHECKER C134 CLOSED: …», the branch head; docs/checker/ ends at
C134.md; C135 does not exist; notes/CHECKER.md l. 6: «Coming (Lead 22:37Z): C135 = P-N5-ASC (L-NEW, frozen 95dc76d7) after both
signatures and the first fill;»). l-red 86a7a7a8 (head); the adversary file docs/red/R220-asc.md at 68a1f609
(68a1f609b25f8cd75688650114e3f596e8ae3dac, 2026-11-07T22:21:39Z, L-RED successor 55; 69 lines, 5,530 bytes, sha1
a807fb90ff1f65103bf43f97c9c09c65c5616ebb; an ancestor of origin/claude/l-red). 95dc76d7, 19cc23e3, a5dcf9c6, 26b2b516, d4b39be0,
94062059, 533744a5, c4166c8b, fcdc16b4, d3fed33c and 68a1f609 are NOT ancestors of the local trunk 8912e145 (git merge-base
--is-ancestor); a5dcf9c6 is an ancestor of origin/claude/l-new, 94062059 of origin/claude/referee, d3fed33c of origin/claude/referee-2.
The Lead merges claude/l-new, claude/referee and claude/referee-2 before landing.
Trunk: local HEAD 8912e145 (8912e145f47fa1242731d5162d015707679f7681, 2026-11-08T01:42:09Z, «Lead: L-RED 57 and L-LOWER 9 roster;
restart rows; log (HIT7 end to end; P-N5-ASC L-2 MATCHES at REFEREE; P-ACYC reviews)»; origin trunk 51eb6534 its parent; the working
tree has the Lead's uncommitted docs/NOW.md and docs/agents/LANE-RESTART.md, and RESULTS and GAPS equal HEAD, git diff --quiet).
RESULTS at HEAD: sha1 66e7119615efa5a0bb25b898e32b5b371c55c122, 14,962 lines; «### R118» l. 13607, «### R119» l. 13879, «### R120» l.
14114-14318, «**Erratum E-1**» l. 14320, «**Erratum E-2**» l. 14333, «**Note E-3**» l. 14361, «## Dead ends (kept;» l. 14392. GAPS at
HEAD: sha1 2a41c7654d4e9dedee7abc8591dfb792633bc2c9, 23 lines, l. 11 76 "|", 55 «UPDATE 2026-», the last R120's «UPDATE 2026-11-07
21:05Z: RESULTS R120 (P-TOWER-FUEL; CHECKER C134 0c816917)». «R121», «C135» and «P-N5-ASC» occur 0 times in RESULTS and in GAPS.
Sources read: the packet docs/new/P-N5-ASC.md (frozen 95dc76d7; sha1 9c9cb50d89e8bba3232ca2790ddbf95f85580af6, 225 lines, 19,345 bytes;
read in full); docs/new/P-N5-ASC-fixes.md at a5dcf9c6 (sha1 28cf8f9f3231aedd53a079ec5e810200ab16075f, 91 lines, 8,108 bytes; entries
1-2; read in full; its l. 1-67 = the file at 19cc23e3, sha1 68139c3e3dc170d6aaaf95a2fe6c683a52834f12, 5,973 bytes, by cmp); line L-1
docs/new/P-N5-ASC-line-L1.txt (19cc23e3, the file's only commit before a5dcf9c6, unchanged there; sha1
08cced78a214080dac3f8f07ebc900510e3f35ab, 4,896 bytes); line L-2 docs/new/P-N5-ASC-line-L2.txt (a5dcf9c6, the file's only commit; sha1
f109cb69507efd863133a08a2e90096ad2acb7f5, 4,907 bytes); experiments/new/box193/asc.pins at a5dcf9c6 (35 rows, 2,066 bytes, sha1
0926b73f9b14b41d0d52a9f2a55677b0ddc578c6); experiments/new/check.sh at a5dcf9c6 (1,020 lines, 106,599 bytes, sha1
87b319fac6351893e60a48549c503a986a7233b4; the block «BOX 193 ASC» l. 988-996 and the block «P-N5-ASC» l. 997-1003, read);
experiments/new/box193/asc193.py (101 lines, sha1 14b96e1039aa1c269ff20a11d64362c3e0b78e01, read in full), ug193.py, noup193.py,
hubasc193.py, skel193.py (read in full), chain193.py (header), check193.sh (header), check193.out (sha1
d4fb21644db639435806886bb6c709add84d9ded, 71 lines); REFEREE's file at 26b2b516, d4b39be0 and 94062059 (read in full; its scratch tools
listed, not re-run); REFEREE-2's file at 533744a5, c4166c8b, fcdc16b4 and d3fed33c (read in full; its tools listed, not re-run); L-RED
R220 at 68a1f609 (read in full; context, not a signature); RESULTS R104 (l. 9864, 10085), R118 (l. 13607-13878, read), R120 (the
landed form, l. 14114-14318); GAPS l. 11; DECISIONS l. 355-358 (L41) and DECISIONS-INDEX l. 34 (its L41 row); docs/agents/LEAD-STATE.md
(the P-N5-ASC lines 2617-2673, by grep); docs/NOW.md (grep); docs/checker/C134.md at d38a2194 (§2-§3, the E-1..E-4 classes, sha1
da15e761d4f5b56eebba41b40d0937fc8197c4b6) and notes/CHECKER.md (grep); the frozen P-N5-XICYC.md at fd1266a5 (l. 68-76, F1-F3);
L-RED's three NOUPC .pg files at 68a1f609 (sha1 by git show; = inst/SHA1SUMS); docs/agents/R120-draft.md and R119-draft.md (the house
form; R120's first-fill record l. 116-426, its entry d[426:631] and UPDATE d[639]) and docs/agents/R118-draft.md's model, R118 landed.
Checks run at this fill (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r121;
nothing written into the repository but this file). (a) l2shape121.py: L-2's shape, its labels and premise quotes against RESULTS at
8912e145, the L-1 → L-2 byte test, the proposed R-B and R-G. (b) check193.sh from a git archive of a5dcf9c6 (experiments, docs/new,
scripts), 2026-11-08T01:49:02Z-01:49:43Z, rc 0, 71 output lines, byte-equal to the committed check193.out (cmp); then the two check.sh
blocks «BOX 193 ASC» and «P-N5-ASC» (check.sh l. 988-1003 copied into a script in the archive, run from experiments/new),
2026-11-08T01:49:48Z-01:50:30Z, rc 0, both PASS (a first try from an archive without experiments/harness failed with a
ModuleNotFoundError for pg, rc 1: my archive, not the lane's code; recorded, not a finding). (c) data121.py: every DATA clause of L-2 against the re-run output
and the counter code it names. (d) upd121.py: the UPDATE with controls R97-R120 (r120b/tools/upd120b.py l. 1-311 exec'd unchanged but for
one assertion, Addendum (8)). (e) chk121.py (title, block, UPDATE, quote sweep, stale grep) and sim121.py (landing simulation): Addendum.
LESSONS APPLIED (R120's list, plus C134). C113 E-1 / C123 E-1 / C133 E-1: the title is L-2 verbatim, nothing inserted and nothing
stripped; L-2 has no «R1xx» and no ledger tag before its claims (CLEAN). C133 E-3: the scope tail « (2026-11-07) — … not a TARGET.md
claim» and «G-N5-TIME stays OPEN» are in the line (CLEAN). C134 E-3: the drop words are the landed «not M3, not a step-4 pass, not a
TARGET.md claim» («gauntlet» 0 times in L-2; CLEAN). C120-C134 / C134 E-4: EVERY DATA clause tested against the code of its counter for
unit, set and scope (G-9). C122 G-0: parentheses balanced (L-2 SHAPE). C122 E-3 / C132 E-2 / C133 E-2 / C134 E-1: the source note names
every proof-carrying file and the lane successors (G-1: FLAG). C132 E-7 / C133 E-6 / C134 E-2: a referee-originated proof step is named in
the scope tail (L41; G-7: FLAG). C117 E-1 / E-2: no sentence of the line wider than the signed statements (G-2: FLAG on the Reading).
C118 E-1 / C132 E-1: no status word that goes stale at landing (G-11). C115 E-1: premises checked against RESULTS, landed entries only
(G-4). C116 G-2: name clashes (G-6). C116 G-3: pins (G-12). C119 E-1: every «referee X did Y» checked against that referee's file. C130
G-P / C133 G-P: the UPDATE builder carries a control for every UPDATE that lands before this one (R97-R120 landed). C132 Add. 1: block
re-run times as a date -u interval.
FLAGS FIRST (G-1 makes CHECKER FAIL as L-2 stands by the C122 E-3 / C132 E-2 / C133 E-2 / C134 E-1 precedents; G-7 needs the Lead's
L41 ruling, and if it is L41's case CHECKER FAIL as it stands by C132 E-7 / C133 E-6 / C134 E-2; G-2 and G-U are CHECKER's rulings;
G-9 (i)-(iv) are notes). Exact replacements R-B, R-G (and optional R-R, R-Q), each old string once in L-2, by script; L-2 with R-G then
R-B: sha1 c23e11d0905a8d73e6f605993c8533b488facc7c with its newline, 5,126 bytes, 118 «(» / 118 «)», 0 "|", one « — »; its UPDATE by
the procedure of G-U 988c1e7ade9ee9c4fbf3412bca696f926b1aab16 (5,156 bytes); R-R and R-Q not built into a line.
- G-1, SOURCE NOTE (FLAG; the C122 E-3 / C132 E-2 / C133 E-2 / C134 E-1 class; CHECKER FAIL as it stands). L-2's last parenthesis is
  «(P-N5-ASC, docs/new/P-N5-ASC.md with fixes entries 1-2, docs/new/P-N5-ASC-fixes.md; L-NEW successor 61)». It names the fixes file, but
  both fixes entries and both lines are L-NEW successor 62's (fixes l. 3 «## Fixes entry 1 (L-NEW successor 62;», l. 69 «## Fixes entry
  2 (L-NEW successor 62;»; check.sh l. 997 «# P-N5-ASC (L-NEW successor 61; fixes entry 1 + line L-1, successor 62)»). Entry 1 carries
  text the line rests on: the [E-LEV] scope of NOUP (W-1), the unit counts (D-1), the AS-1 argument for F′_0 = F_0 (G-7) and the D_E(v)
  definition (AS-4). C134 E-1 on R120 named «L-LOWER successors 5-6» for the same reason. Proposed R-B: "; L-NEW successor 61)" → "; L-NEW
  successors 61-62)". Old string once in L-2 and once in the UPDATE (script).
- G-7, L41: THE B = 0 STEP OF HUB-ASC-G (FLAG for the Lead's ruling; the C132 E-7 / C133 E-6 / C134 E-2 class if ruled L41). The
  packet's proof of HUB-ASC-G ends «Inside one such level the active items form a run of CS(M_w) restricted to those times, and §4's proof
  applies word for word.» (l. 160); for B = 0 that gives (M² + 3M + 1)·F_0, not the stated F′_0 = 1 + M(M + 1)/2 (REFEREE l. 117-118:
  «F′_0 is not obtained «word for word» per level (that would give a factor M² + 3M + 1).»). The argument for F′_0 = F_0 is REFEREE's
  (l. 118-119, optional AS-1), restated in fixes entry 1 AS-1 (l. 53-56), stated in L-2 («F′_0 = F_0 (DESC-POLY on the whole
  interval)»). REFEREE signs it (§C l. 215, l. 238); REFEREE-2 checked it independently after its report (Add. 1 l. 212-215) and
  accepted it (Add. 2 l. 254); the joint gap map is empty (both tables SIGN, REFEREE «the bound is right», l. 119). Differences from the
  R118 / R120 cases: the step is marked «optional» by its author, no referee found a false step, and the statement was SIGN in the first
  round at both. So it is the Lead's ruling whether L41 applies to a referee-written step that makes a stated constant follow. If it
  does, L-2 lacks the scope-tail sentence («referee» occurs in L-2 only in «REFEREE-2 control CTRL=elevrev», by script). Proposed R-G
  (the R118 / R120 form, inside the scope words): "; §3-§5 do not use [E-LEV]; DATA, clause by clause" → "; §3-§5 do not use [E-LEV];
  the proof of record of HUB-ASC-G's B = 0 case (F′_0 = F_0, DESC-POLY on the whole interval) is referee-originated (REFEREE
  R-P-N5-ASC §3 AS-1, restated in P-N5-ASC's fixes entry 1 AS-1), signed by both referees; DATA, clause by clause". Old string once in
  L-2 and once in the UPDATE (which keeps the scope words), where the sentence lands at the same place (script: the proposed UPDATE = the
  L-2 UPDATE with R-B and that one insertion, True).
- G-2, THE READING IN CHAIN-DECOMP'S CLAUSE (FLAG for CHECKER's ruling; the C117 E-1 / E-2 class). L-2's CHAIN-DECOMP clause ends «so the
  e-vertices of one Λ-class form one forest whose paths are the sequences seq_t(v)». That is the packet's «Reading:» after the lemma
  (l. 89-90: «Reading: at each state, next_t(f) := the first element of seq_t(y_f) (⊥ if none) defines one forest on the e-vertices with
  cycle node w, and every seq_t(v) is a path of it starting at v's first e-vertex.»), and the packet's labels say «READING (not to
  sign)» (l. 5). In my reading it is covered: both referees checked it as a proof step («The «Reading» (next_t is one forest on the
  e-vertices with cycle node w): the plays' prefixes have distinct vertices, so next is acyclic.», REFEREE l. 73-74; «The Reading
  (next_t defines one forest on the e-vertices with cycle node w, and the chain of an active item x is seq_t(x)) holds,», REFEREE-2 l.
  55), HUB-ASC-G's signed proof uses it («At each t ∈ I, next_t on the active items is one forest (CHAIN-DECOMP)», l. 156), and both
  referees read L-1 / L-2 clause by clause and found every clause matching (REFEREE §C l. 230-232; REFEREE-2 Add. 2 l. 256). Optional
  R-R (if CHECKER wants the signed form only): "so the e-vertices of one Λ-class form one forest whose paths are the sequences
  seq_t(v)" → "hence seq_t(v) = (f, seq_t(y_f))" (the lemma's own second sentence, l. 81; old string once in L-2 and once in the
  UPDATE).
- G-U, THE UPDATE PROCEDURE (FLAG for CHECKER's ruling; no line change needed). L-2 has R118's line shape (L-NEW, P-N5-XICYC L-4):
  labels BEFORE their clauses after «more relevant than w): », one « (2026-11-07) — », scope words with the DATA inline («; DATA, clause
  by clause (…): …», no «(DATA: » or «(DATA, » parenthesis), the drop words, the source parenthesis. So R105's sentinel_build («(DATA: »)
  and R111's sentinel_build111 («(DATA, ») do not apply; R118's run118() does, with R121's start, labels and source prefix in place of
  R118's and nothing else changed (upd121.py run121(): build() with the sentinel, the source parenthesis kept, «; G-N5-TIME stays OPEN»
  and «; not M3, not a step-4 pass, not a TARGET.md claim» dropped, «. G-N5-TIME stays open.» appended), cross-checked by a direct build
  (True). Result: the five labels behind their clauses, « (2026-11-07) — » → «: », the drop words dropped, the source parenthesis kept;
  token diff L-2 → UPDATE 11 hunks, 43 tokens out, 42 in, nothing else (Addendum (8)). The fifth label «(Lemma UP-JUMP, Corollary UP-B,
  Corollary NOUP; UP-JUMP, UP-B and NOUP under HYPOTHESIS [E-LEV])» carries a «; » inside it; build() finds labels by their full text and
  cuts clauses at the last «; » before the next label, so it moves whole (by script). CHECKER rules whether this is the procedure.
- G-9, DATA, CLAUSE BY CLAUSE (the C120-C134 rule: unit, set and the statement's scope of every count, against the counter code it names;
  every signed clause matched to a count or a no-DATA entry). Every figure is in check193.out and reproduced by my re-run ((b) above);
  data121.py sums the 13 instance lines. Counter code: asc193.py l. 44-95 (analyse()), ug193.py l. 9-14, noup193.py l. 36-46,
  hubasc193.py l. 11-32, skel193.py l. 8-30, chain193.py.
  - E-DOM «violations 0 in 1,892 vertices»: edomfail (l. 50) counts vertices other than c_W, K0, K3 and the e's that are more relevant
    than the least relevant e; edomunits (l. 55) the vertices other than c_W, K0, K3 and the e's, per instance, summed 1,892 over the 13.
    MATCH. NOTE: the unit is per genome (static), and «vertices» is shorter than the counter's set (REFEREE §C l. 234-235: «L-1's units
    «vertices» (E-DOM) and «W-target with Λ fixed» (E-MON) are shorter than fixes entry 1's definitions»; the E-MON one is fixed by W-3).
  - E-MON (TAIL-MON form) «violations 0 in 2,552 (consecutive state pair, W-target or c_W with Λ fixed) pairs»: tmonfail / tmonunits (l.
    70-72), at every y in W.values() (each e's only successor: W-target mover or c_W) with Λ(y) equal at t − 1 and t; 2,552, of which
    229 = Σ T are c_W units (REFEREE-2 Add. 2 l. 259; data121.py Σ T 229). MATCH. NOTE: narrower than the lemma's every v (stated in the
    line; REFEREE-2 l. 140-141; its every-vertex 46,830 is referee data).
  - CHAIN-DECOMP «violations 0 in 24,818 (state, vertex) pairs with a nonempty e-sequence»: decfail / decunits (l. 66-68): per (state,
    vertex) with seq nonempty, Λ(y_f) = Λ(v) and e-part(v) = {f} ∪ e-part(y_f). MATCH (= REFEREE-2's own «CDEC_units 24818», Add. 2 l.
    242). NOTE: the Reading part of the clause (G-2) is not counted separately; it follows from the counted equality on every state.
  - UP-JUMP «violations 0 in 1,956 ascents of movers' plays with Λ below every e»: asc / upfail (l. 74-81): movers v (name «x») with
    rank(Λ) < the least e rank, every ascent (a, b) of seq(v), upfail unless some β on the segment has a mover Ξ-target of level ≥ la and
    > the level of the β's own mover (W-4, l. 79-80). MATCH (both referees read l. 79-80 against the lemma, REFEREE §D l. 260-263,
    REFEREE-2 Add. 3 l. 294-300).
  - The set parenthesis «(asc193.py; set: the 13 instances, 8 L-RED R217 instances in inst/ and 5 in box192/inst/, all pinned in
    asc.pins)» follows the four comma-separated asc193 clauses and binds to all four (the two asc193.py calls in check193.sh l. 7-10);
    the 13 file names are in asc.pins (rows 18-25, 28-32). MATCH.
  - UP-B «max ascents ≤ U(G) on all 13 instances (unit: max ascents over (state, vertex) plays; ug193.py)»: ug193.py l. 12-14, U(G) =
    options with a mover Ξ-target of higher level, maxasc = asc193's max over all (state, vertex) plays; 13 lines, all OK
    (data121.py). MATCH.
  - NOUP «300 random genomes with no strictly upward Ξ-edge, 179 Ξ-cyclic, max ascents 0, max D_E per Λ-interval 3 (noup193.py 300 1)»:
    noup193.py (Ξ-targets X or level ≤ the option's level, l. 17-18), «NOUP genomes 300 seed 1: Xi-cyclic 179; max ascents 0; …; max D_E
    per Lambda 3». MATCH. NOTE: maxDE is keyed by (v, Λ value) over the run (asc193.py l. 69, 94); by F1 + F2 each Λ value is one
    interval, so it is per Λ-interval.
  - HUB-ASC(B) «B 0 max 11 at M 4 (= F_0), B 1 max 16 at M 4 and 29 at M 5»: hubasc193.py (only the hub's chain limited, l. 24-25). MATCH.
  - SKELETON «violations 0 on all forests of CS(4) and CS(5)»: skel193.py with A 99 («SKELETON CS(M 4, A 99): forests 125, violations
    0», M 5: 1,296). MATCH.
  - Tightness «F_0 attained for M 1-7 (2, 4, 7, 11, 16, 22, 29; …)»: chain193.py at A 0, i.e. every chain ≤ 0 ascents. NOTE: attainment on
    that sub-family of runs is attainment on all runs (F_0 is an upper bound there by HUB-ASC(0)). MATCH.
  - [E-LEV] necessity (scope tail): REFEREE-2's «UPB/NOUP fail on 209 of 21,116 plays of U = 0 genomes (up to 2 ascents).» (l. 134,
    verbatim at 533744a5, REFEREE §C l. 218) and R220's «NOUPC_1 / 2 / 3 have U(G) = 0 and max ascents 2 / 3 / 4» (l. 47-48), the .pg
    sha1s 82e41194…, 7ea66452…, 94db68d5… (git show at 68a1f609 = inst/SHA1SUMS, my check). DATA of others, cited as such. NOTE (no
    change): L-2 says «one route only»; REFEREE §C l. 221-225 re-derived the U(G) and max-ascent numbers on its own engine («So «one route
    only» is now two routes for the max-ascent numbers.»), not the witness «t 0, v 10» (l. 226). The line understates; it does not
    overstate.
  - No-DATA list «HUB-ASC(B) with B ≥ 2, HUB-ASC-G's constants, the whole-run corollary and UP-B's D_E bound»: the signed clauses without
    a count. NOUP's D_E bound is the whole-run corollary at B = 0 (covered by that entry); NOUP's DATA tests its ascent claim and the
    per-interval D_E (3). CLEAN.
  - (i) NOTE. «E-DOM part of E-MON's proof» is a proof step, not a clause of the line; its count is DATA for E-MON's proof.
  - (ii) NOTE. The DATA scope «(scope IDEAL-CYC unless abstract; …)»: every game counter runs box191's IDEAL-CYC on box189's Γ(G),
    whose e-order is (level, gate), so [E-LEV] holds on all game DATA (REFEREE l. 32-33; REFEREE-2 l. 39).
- G-4, PREMISE ROUTE (the C115 E-1 class): CLEAN (l2shape121.py on RESULTS 66e71196 at 8912e145). R-labels in L-2: «R104» 3, «R118» 1,
  «R217» 2 (L-RED's round, «L-RED R217 §2», «8 L-RED R217 instances»; not a RESULTS label, RESULTS has no R217); R104 and R118 landed
  (### R104 l. 9864, ### R118 l. 13607). L-2's one quote «C ≤ n·(2M + 2).» is at R118 l. 13691 (found). The packet's [DEF] quotes: seven
  in R104's title (found ×7) and «the exact e-priorities to packet §3.1» at l. 10085 (found). F1-F3 are in the frozen P-N5-XICYC.md
  (fd1266a5, sha1 149e2414), l. 69-73, which R118 (b) incorporates. «[LOC]», «OVT-DV», «IN-BOUND» 0 in RESULTS (not used, as stated).
  The literature item (VJ00 §4.2 / Friedmann arXiv 1106.0778 §3) is R118's landed premise, in the same words.
- G-6, NAMES (by script on RESULTS 66e71196 / GAPS 2a41c765). 0 times in RESULTS and GAPS: «R121», «C135», «P-N5-ASC», «HUB», «DESC-POLY»,
  «CHAIN-DECOMP», «SKELETON», «UP-JUMP», «NOUP», «E-DOM», «TAIL-MON», «F_B», «CS(M», «OVT-DV», «IN-BOUND», «[LOC]», «R217». «E-MON»: 25
  in RESULTS and 4 in GAPS, all inside «SETTLE-MON» / «VALUE-MONO» (no label collision). «U(G)» once in RESULTS (R105 body l. 10267,
  another U). «E-LEV» twice, inside «CODE-LEVEL» (l. 4026, 4068). «D_E» 28 / 5 times as R-series notation of another quantity (D_E an
  Odd vertex set of an epoch); a near-clash of notation, not of label. Honest limits (vii).
- G-P, PLACEMENT (Lead). R120 LANDED (RESULTS l. 14114-14318, GAPS l. 11 last). R121's block goes after R120's, before «**Erratum E-1**»
  (l. 14320), and its UPDATE after R120's on GAPS l. 11. Simulated on 8912e145 (sim121.py): Addendum (7). P-N5-QUIET «lands after R121»
  (LEAD-STATE l. 2649).
- G-0, THE CHECKER NUMBER. docs/checker/ on claude/checker (d38a2194) ends at C134.md; «C135» occurs 0 times in RESULTS, GAPS,
  DECISIONS-INDEX, once in NOW and LEAD-STATE (the routing), once in notes/CHECKER.md (l. 6, quoted above). This draft uses C135 (title
  fill, UPDATE head, GAPS preamble).
- G-5, ERRATA (note). E-1 (R97-R100 counts), E-2 (R105's CHAIN-BACK, RANK_t, KEYFLIP) and Note E-3 (R110's SC-ISO) do not bear on R104's
  definitions or R118 (a), (b) F1-F3, (e).
- G-8, SCOPE AND TARGET (note). L-2's scope words «this bounds the e-set height D_E,I(v) only, NOT R and NOT any running time: the step
  from D_E to R needs OVT-DV ([LOC], L-RED R217 §2) and CONJECTURE IN-BOUND (box 192 Addendum 9), neither landed;» equal packet l. 9-11
  in meaning; REFEREE «Scope sentence: CORRECT.» (l. 185), REFEREE-2 «**Scope sentence ✓.**» (l. 106). No statement mentions a parity
  game's winning region, an algorithm's running time or a complexity class.
- G-10, LEAD RULINGS AND READINGS. L-2 cites no Lead reading by label («Lead reading» 0, «L4» 0 in L-2). LEAD-STATE l. 2649 records a
  Lead reading «[E-LEV] = R104 (vi) via frozen packet §3.1 (R118 (b) precedent; referees decide)»; the referees kept [E-LEV] a
  HYPOTHESIS (REFEREE-2 l. 38 «**[E-LEV]** is not landed; it is a hypothesis.»; REFEREE §C l. 228-229 checked the §3.1 wording), and the
  line states it as a HYPOTHESIS «not in a landed line», the conservative form. No line change asked; the Lead may record whether the
  reading changes anything (I read: no).
- G-11, STALE WORDS (notes). L-2 has no «pending», «not landed», «NOT YET», «candidate», «will » (0 each). It has «neither landed» (OVT-DV,
  IN-BOUND) and «not in a landed line» ([E-LEV]): true at landing and dated by the line's «(2026-11-07)»; they become history if either
  lands later (the R118 precedent: «no bound on R is claimed (OPEN)»). check.sh l. 997's comment names «fixes entry 1 + line L-1» only
  (the block reads asc.pins, 35 rows, so it checks L-2): history, not a pin gap.
- G-12, PINS (the C116 G-3 class; CLEAN). asc.pins pins the packet, the fixes file, L-1, L-2, every tool and the 13 instances (35 rows,
  all match: my re-run of the block, (b)); the frozen check193.out is pinned and diffed. C116 l. 67's «NOT required before landing.» is not
  needed here.
- G-13, THE REFEREES' ROUNDS: (3), (4). D-items: (11).
- G-14, THE FIXES FILE (note). Two entries (entry 1: W-1 / AS-2 / AS-3, W-2 / AS-D2, D-1 / AS-D1, D-2, D-3, AS-1, AS-4, Not taken N-1,
  N-2; entry 2: W-3, W-4 (a)); entry 1 carries the AS-1 step (G-7). L-1 + the two entry-2 strings = L-2 (True, my script).
- G-N, NOVELTY (note). The only outside source is R118's VJ00 / Friedmann premise; the entry makes no literature claim.
- (ii) under G-2: SYMBOLS (note; optional R-Q). L-2 uses seq_t(v), «ascents», Π_t(v), Λ_t(v), «hub», «chain», U(G), F′_B, M without
  defining seq_t(v) and «ascent» (packet §2 l. 52-55); Λ, Π are R118's premise notation, the rest is defined in the line. The C124 G-9
  (vii) ruling covers landed notation; seq_t(v) and «ascent» are new. Optional R-Q: "with E_t(v) the set of e-vertices in Π_t(v)," →
  "with seq_t(v) the e-vertices in Π_t(v) in play order, E_t(v) their set, an ascent of seq_t(v) a step to a more relevant element,"
  (old once in L-2; by script). Both referees MATCHED L-1 and L-2 without it.
- CLEAN AT L-2 (by script on f109cb69): C113 E-1 / C123 E-1 / C133 E-1 (L-2 starts «The e-set height of one vertex on IDEAL-CYC», «R1xx»
  0); C133 E-3 (« (2026-11-07) — » once, «not a TARGET.md claim» once, «G-N5-TIME stays OPEN» once); C134 E-3 («not a step-4 pass» once,
  «gauntlet» 0); C114 Add. 1 E-1 (<DATE>); C115 E-1 (G-4); C116 G-2 (G-6); C122 G-0 (116 / 116); C116 G-3 (G-12); the DATA clauses (G-9,
  notes only); «|»: 0 in L-2, 0 in the entry block, 0 in the UPDATE (Addendum). NOT CLEAN: C122 E-3 (G-1); for the Lead: L41 (G-7); for
  CHECKER: G-2 and the UPDATE procedure (G-U).
- (L-2 SHAPE, by l2shape121.py) L-2 is one line: 4,907 bytes and 4,810 characters with its newline, 818 whitespace tokens, 116 «(» / 116
  «)», depth never negative, final depth 0, 0 "|", one « — », «[» 11 times (each «[E-LEV]» or «[LOC]»; none a label), «R1xx» 0,
  «(DATA: » 0, «(DATA, » 0, «DATA, clause by clause» once, «under [E-LEV]» 4 times, one guillemet quote («C ≤ n·(2M + 2).»).
(0) PLACEMENT. RESULTS at the local trunk 8912e145: sha1 66e7119615efa5a0bb25b898e32b5b371c55c122, 14,962 lines; "### R121" 0 times in
  RESULTS and GAPS. PROPOSED (R102's to R120's layout): insert R121's entry, with one blank line after it, directly before «**Erratum
  E-1**» (l. 14320), after the blank line that follows R120's block (G-P). Simulation: Addendum (7).
(1) TITLE. The title is the line file docs/new/P-N5-ASC-line-L2.txt (l-new a5dcf9c6, 2026-11-08T00:40:20Z, the file's only commit, sha1
  f109cb69507efd863133a08a2e90096ad2acb7f5, 4,907 bytes with the newline; byte-equal at the l-new head d9c49489), verbatim: NOTHING is
  stripped and NOTHING is inserted: "### R121 [refereed-only] ", then the file without its newline, then ", CHECKER PASS
  (docs/checker/C135.md, checker PENDING)" (as R90-R120). Built by script and re-checked after writing (chk121.py): equal.
(2) LINE HISTORY: two lines. L-1 08cced78 (19cc23e3 with fixes entry 1; 4,896 bytes, 116 «(» / 116 «)»; REFEREE MATCHES, REFEREE-2 NOT YET
  on W-3, W-4). L-2 f109cb69 (a5dcf9c6; 4,907 bytes): fixes entry 2, L-1 with exactly two replacements (W-3's string and «entry 1» →
  «entries 1-2»), each old string once in L-1, each new string once in L-2, L-1 + the two = L-2 (True, my script); both referees by their
  own scripts.
(3) THE LINE AT BOTH REFEREES. REFEREE: report 26b2b516 (successor 27; no line existed: «There is no line file in the frozen packet.», l.
  19), §C d4b39be0 (L-1 MATCHES, l. 238), §D 94062059 (successor 28; L-2 MATCHES, l. 270). REFEREE-2: report 533744a5 (successor 31; «No
  line file exists for this packet yet;», l. 9), Add. 1 c4166c8b (agreement), Add. 2 fcdc16b4 (L-1 NOT YET: W-3, W-4, l. 280), Add. 3
  d3fed33c (successor 32; L-2 MATCHES, l. 315).
(4) CLAIMS SIGNED = every statement row of both verdict tables (REFEREE l. 5-17; REFEREE-2 l. 11-24): SIGN at both from the first round,
  unchanged in every later round. Not signed: §7-§9 (DATA, both), the «Context, not a clause» row, the adversary data, REFEREE-2's N-1,
  N-2 (constants, not taken).
(5) OTHER TEXTS THE ENTRY DEPENDS ON: RESULTS R104 (definitions), R118 (a), (b) F1-F3 (via the frozen P-N5-XICYC.md), (e); the 13
  instances and the box 193 tools (L-NEW 61-62); REFEREE-2's control output and L-RED R220's frozen NOUPC files (cited in the scope tail).
(6) PREMISE LABELS: G-4.
(7) SYMBOL TEST: G-2 (ii).
(8) FIXES AND STATUS NOTES: G-14; body Fixes.
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-2 states no CONJECTURE as claimed (it names CONJECTURE IN-BOUND as not landed) and kills no
  statement («P-N5-ASC», «HUB-ASC» 0 times in GAPS). A line-11 UPDATE is proposed at the end, BUILT FROM L-2 AS IT STANDS (upd121.py:
  r120b/tools/upd120b.py l. 1-311 exec'd, Parts A-E2 unchanged but for one assertion (Addendum (8)): R97's to R116's LANDED UPDATEs
  rebuilt from their lines and compared with GAPS l. 11 byte for byte, True ×20; R117, R118 and R119 as landed, True ×3; then the R120
  control, LANDED: R105's procedure on R120's L-3 (l-lower 4f25ae6f) = R120-draft.md d[639], unfilled sha1 17cba597…, filled with GAPS
  l. 11's stamp 2026-11-07 21:05 0c816917 = that segment, True; all controls True ×24, the last UPDATE on l. 11 R120's; then R121 (G-U)).
(10) DATA of record = packet §7 with fixes entries 1-2, NOT signed; L-2's DATA states its counts (G-9). Re-run (b): PASS.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 the packet header «Written from 21:4xZ (date -u)» is a partial stamp;
  commit 95dc76d7 21:45:00Z. D-2 REFEREE-2's headings: the report «2026-11-07 from 22:1xZ (date -u)» (533744a5 22:17:18Z; partial); Add. 1
  «REFEREE-2 successor 31, 2026-11-07 22:5xZ by date -u» but c4166c8b is dated 22:47:01Z (author and committer), earlier than any 22:5x;
  Add. 2 «REFEREE-2 successor 31, 2026-11-08 00:0xZ by date -u» but fcdc16b4 is dated 2026-11-07T23:52:10Z, earlier; the C132 Add. 1 class
  of heading stamp; history, not a verdict. REFEREE's headings (22:25Z, 23:51Z, 01:07Z) are before their commits. D-3 REFEREE-2 Add. 3 l.
  287-288: «(DOCS/ → docs/new/, as check193.sh l. 998 does)»: that rule is experiments/new/check.sh l. 998 («pinA=…»), not check193.sh
  (30 lines, no sed); a slip in a file name, the check itself is right. D-4 REFEREE §D l. 246 «asc193.py (the W-4 test, two lines)»
  and REFEREE-2 Add. 3 l. 294 «one line changed»: git diff 19cc23e3 a5dcf9c6 shows asc193.py +2 / −1 (one line replaced by two); both
  describe the same change. D-5 L-2's source note and check.sh l. 997's comment (G-1, G-11).
(12) Excluded: box 193's other lane items (Lemma ASC-GATE, Construction ASC-EXP, DEAD RMON-2, PTR-MON-HI, FIXTOP, RECUR, LOW-SHAPE, the CS(M,
  A) values and CS(8, 1) = 126 of a5dcf9c6), BOX 194 / P-N5-QUIET (frozen 9329859d, its own packet; «lands after R121»), the packet's
  «Context, not a clause» row, N-1 / N-2 (sharper constants). Not part of this entry.
(13) Commits: lane (claude/l-new): 95dc76d7 (2026-11-07T21:45:00Z; packet FROZEN, asc.pins 27 rows, check blocks; L-NEW successor 61),
  e9993378 (BOX 194, other work), 19cc23e3 (23:23:53Z; fixes entry 1, L-1, asc193.py unit fields, ug193 on 13, chain193 M 6-7, asc.pins
  34; successor 62), 9329859d (P-N5-QUIET FROZEN, other work), a5dcf9c6 (00:40:20Z; fixes entry 2, L-2, asc193.py W-4, asc.pins 35;
  successor 62), d9c49489 (P-N5-QUIET fixes, other work). REFEREE: 26b2b516 → d4b39be0 → 94062059. REFEREE-2: 533744a5 → c4166c8b →
  fcdc16b4 → d3fed33c. L-RED: 68a1f609 (R220). CHECKER: docs/checker/ ends at C134.
(14) DEAD-ENDS ROWS: NONE (no statement killed; the [E-LEV] necessity is a scope fact of a hypothesis, recorded in the scope tail).

### R121 [refereed-only] The e-set height of one vertex on IDEAL-CYC is polynomial when its plays have boundedly many ascents (HUB-ASC-G), in particular, under the e-priority hypothesis [E-LEV], on genomes with boundedly many upward Ξ-edges (UP-B) (premises: RESULTS R104's definitions of the genome and of Γ(G) only; RESULTS R118 (a) IDEAL-CYC(G), (b) F1, F2, F3 and (e) «C ≤ n·(2M + 2).» in its per-vertex form (Λ_t(v) takes at most 2M + 3 values, in increasing reward); VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the value (Λ, Π, k) and its order ⊴; HYPOTHESIS [E-LEV] (only for §6 UP-JUMP, UP-B and NOUP): lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′)), the order of Γ(G) as built by experiments/new/box189/gamma3.py (and of R104's packet §3.1), not in a landed line; not used: [LOC], OVT-DV, IN-BOUND, any L-RED lane lemma, F4/F4′, F5, F6), with seq_t(v) the e-vertices in Π_t(v) in play order, E_t(v) their set, an ascent of seq_t(v) a step to a more relevant element, sets of e-vertices compared lexicographically by their most relevant differing element, and D_E,I(v) the number of distinct E_t(v) on an interval I of states with Λ_t(v) = w fixed (M_w := the number of e-vertices more relevant than w): (Lemma E-MON) if Λ_t(v) = Λ_(t+1)(v) then E_t(v) ≤ E_(t+1)(v); (Lemma CHAIN-DECOMP) if seq_t(v) = (f, …), i.e. the first e-vertex on v's play is f and f ∈ Π_t(v), then f's successor y_f is a mover with Λ_t(y_f) = Λ_t(v) and E_t(v) = {f} ∪ E_t(y_f), hence seq_t(v) = (f, seq_t(y_f)); (Lemma SKELETON and Theorem HUB-ASC(B)) in the abstract chain system CS(M) (items 1..M, a run of forests with every chain lex-nondecreasing), a hub whose value has at most B ascents at every time takes at most F_B(M) distinct values, F_0(M) = 1 + M(M + 1)/2 (DESC-POLY), F_B(M) = (M² + M + 1)(1 + M·F_(B−1)(M)²), a polynomial of degree 5·2^B − 3 for fixed B; (Corollary HUB-ASC-G) for every genome G, every vertex v and every interval I with Λ_t(v) = w, if seq_t(v) has at most B ascents for every t ∈ I then D_E,I(v) ≤ F′_B(M_w), F′_0 = F_0 (DESC-POLY on the whole interval), F′_B(M) = (M² + 3M + 1)(1 + M·F′_(B−1)(M)²), and over the whole run the number D_E(v) of distinct (Λ_t(v), E_t(v)) is at most (2M + 3)·F′_B(M); (Lemma UP-JUMP, Corollary UP-B, Corollary NOUP; UP-JUMP, UP-B and NOUP under HYPOTHESIS [E-LEV]) an ascent of seq_t(v) needs a Ξ-edge from a mover to a mover of strictly higher level, so under [E-LEV] every seq_t(v) has at most U(G) ascents (U(G) := the number of options whose Ξ-target has a higher level) and D_E(v) ≤ (2M + 3)·F′_(U(G))(M); under [E-LEV], if U(G) = 0 then every seq_t(v) is descending and D_E(v) ≤ (2M + 3)(1 + M(M + 1)/2) (2026-11-07) — this bounds the e-set height D_E,I(v) only, NOT R and NOT any running time: the step from D_E to R needs OVT-DV ([LOC], L-RED R217 §2) and CONJECTURE IN-BOUND (box 192 Addendum 9), neither landed; [E-LEV] is NECESSARY for UP-JUMP, UP-B and NOUP: with the e-priorities in decreasing level order (still R104's shape) NOUP fails on 209 of 21,116 plays of U(G) = 0 genomes, up to 2 ascents (REFEREE-2 control CTRL=elevrev, docs/referee-2/R2-P-N5-ASC.md at claude/referee-2 533744a5), and L-RED's frozen NOUPC_1 / 2 / 3 have U(G) = 0 and max ascents 2 / 3 / 4 under the e-order (−level, gate) (witness NOUPC_1, t 0, v 10; claude/l-red 68a1f609, experiments/red/r220/inst/, .pg sha1 82e41194…, 7ea66452…, 94db68d5…; one route only); §3-§5 do not use [E-LEV]; the proof of record of HUB-ASC-G's B = 0 case (F′_0 = F_0, DESC-POLY on the whole interval) is referee-originated (REFEREE R-P-N5-ASC §3 AS-1, restated in P-N5-ASC's fixes entry 1 AS-1), signed by both referees; DATA, clause by clause (scope IDEAL-CYC unless abstract; tools in experiments/new/box193/, run by check193.sh): E-DOM part of E-MON's proof: violations 0 in 1,892 vertices, E-MON (TAIL-MON form): violations 0 in 2,552 (consecutive state pair, W-target or c_W with Λ fixed) pairs, CHAIN-DECOMP: violations 0 in 24,818 (state, vertex) pairs with a nonempty e-sequence, UP-JUMP: violations 0 in 1,956 ascents of movers' plays with Λ below every e (asc193.py; set: the 13 instances, 8 L-RED R217 instances in inst/ and 5 in box192/inst/, all pinned in asc.pins); UP-B under [E-LEV]: max ascents ≤ U(G) on all 13 instances (unit: max ascents over (state, vertex) plays; ug193.py); NOUP under [E-LEV]: 300 random genomes with no strictly upward Ξ-edge, 179 Ξ-cyclic, max ascents 0, max D_E per Λ-interval 3 (noup193.py 300 1); HUB-ASC(B), only the hub constrained: B 0 max 11 at M 4 (= F_0), B 1 max 16 at M 4 and 29 at M 5 (unit: distinct hub values; set: all runs of CS(M); abstract; hubasc193.py); SKELETON: violations 0 on all forests of CS(4) and CS(5) (skel193.py); tightness of B = 0: F_0 attained for M 1-7 (2, 4, 7, 11, 16, 22, 29; chain193.py, M 6 and 7 re-run by check193.sh); no separate DATA for HUB-ASC(B) with B ≥ 2, HUB-ASC-G's constants, the whole-run corollary and UP-B's D_E bound; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-ASC, docs/new/P-N5-ASC.md with fixes entries 1-2, docs/new/P-N5-ASC-fixes.md; L-NEW successors 61-62), CHECKER PASS (docs/checker/C135.md, checker PENDING)
- Object (L-NEW successors 61-63, D1 / D14 / D18, box 193; frozen, unchanged during review): packet P-N5-ASC, docs/new/P-N5-ASC.md,
  sha1 9c9cb50d89e8bba3232ca2790ddbf95f85580af6, 225 lines, 19,345 bytes (l-new 95dc76d7, 2026-11-07T21:45:00Z, the file's only commit;
  identical at 19cc23e3, a5dcf9c6, a2512364, a744677e and the l-new head 1a846565). Both referees measured it (REFEREE l. 24
  «docs/new/P-N5-ASC.md sha1 9c9cb50d89e8bba3232ca2790ddbf95f85580af6 (EQUAL to the Lead's relay), 19,345 bytes»; REFEREE-2 l. 5
  «docs/new/P-N5-ASC.md 9c9cb50d89e8bba3232ca2790ddbf95f85580af6 (19,345 B) = the Lead's relay.»). Labels (l. 5): «PROVED (L-NEW 61,
  unrefereed) / HYPOTHESIS (stated in the theorem) / DATA / READING (not to sign).». To sign (l. 13-21): §2 definitions; §3 Lemma E-MON,
  Lemma CHAIN-DECOMP; §4 Lemma SKELETON, Theorem HUB-ASC(B) («B = 0 is DESC-POLY»); §5 Corollary HUB-ASC-G; §6 Lemma UP-JUMP, Corollary
  UP-B, Corollary NOUP; §7-§9 «DATA / READING (not to sign)». The packet's own scope (l. 6, l. 9-11): «This packet is NOT a TARGET.md
  claim and NOT M3. It does not decide G-N5-TIME. N5′-xi stays a CANDIDATE.» and «It bounds the e-set height D_E,I(v), the number of
  distinct sets of e-vertices on v's plays while v's cycle node is fixed, and NOT R and NOT any running time».
  Fixes: docs/new/P-N5-ASC-fixes.md, append-only, four entries, entries 1-2 by L-NEW successor 62 and entries 3-4 by L-NEW successor 63
  (a744677e: 140 lines, 12,728 bytes, sha1 9fb85374b6555e9e2858004fa33ef9d09b2c39aa; its l. 1-91 are the file at a5dcf9c6, sha1
  28cf8f9f3231aedd53a079ec5e810200ab16075f, 8,108 bytes, and its l. 1-125 the file at a2512364, sha1
  bd379c52352cbf6a72b7a53d6723c4f927d78977, 11,085 bytes, by script; byte-equal at the l-new head 1a846565). Entry 1 (19cc23e3,
  2026-11-07T23:23:53Z, l. 1-67; the file then 67 lines, 5,973 bytes, sha1 68139c3e3dc170d6aaaf95a2fe6c683a52834f12): W-1 = AS-2 + AS-3
  + R220's scope item ([E-LEV] for NOUP too; three packet strings), W-2 = AS-D2 (five box192 instances pinned), D-1 = AS-D1 (unit
  counts), D-2 (ug193.py on all 13 instances), D-3 (M 7 tightness re-run), AS-1 (F′_0 = F_0, DESC-POLY on the whole interval; wording
  and its reason), AS-4 (D_E(v) defined), line L-1; «Nothing was REFUSED.» (l. 8). Entry 2 (a5dcf9c6, 2026-11-08T00:40:20Z, l. 69-91):
  REFEREE-2's W-3 (E-MON unit wording) and W-4 (UP-JUMP's tested form, option (a): asc193.py's upfail made strict), line L-2; «The packet
  is unchanged; entry 1 is unchanged; where they differ, this entry governs.» (l. 72). Entry 3 (a2512364, 2026-11-08T03:44:19Z, l.
  93-125): CHECKER C135's E-1..E-4 with its R1-R4, «All four ACCEPTED as written.» (l. 95), line L-3 written by
  experiments/new/box193/mkl3_193.py from C135 §5. Entry 4 (a744677e, 2026-11-08T04:54:26Z, l. 127-140): REFEREE successor 28's R5
  (§E), «ACCEPTED.» (l. 129), line L-4 written by experiments/new/box193/mkl4_193.py. Entry 1 carries the AS-1 argument for HUB-ASC-G's B
  = 0 case (see L41 and L43); entries 2-4 carry no proof, and entries 3-4 change the line only («No tool or DATA output changes», l. 125
  and l. 139).
  The RESULTS line is L-4, 4017305a34eac21615ba8f172a9b899544d25659 (docs/new/P-N5-ASC-line-L4.txt, l-new a744677e,
  2026-11-08T04:54:26Z, the file's only commit; 5,198 bytes; byte-equal at the l-new head 1a846565). The title is L-4 verbatim, with
  nothing inserted and nothing stripped (its date parenthesis «(2026-11-07)», its scope tail and its source note are the line's own; the
  source note names the packet with its fixes entries 1-2 and «L-NEW successors 61-62», see Honest limits (viii)). L-4's parentheses
  balance (125 «(» / 125 «)»). Line history: L-1 (08cced78a214080dac3f8f07ebc900510e3f35ab, 4,896 bytes, 19cc23e3, fixes entry 1, the
  first line, written by script with every entry-1 string applied); L-2 (f109cb69507efd863133a08a2e90096ad2acb7f5, 4,907 bytes,
  a5dcf9c6, fixes entry 2: L-1 with exactly two strings replaced once each, «(consecutive state pair, W-target with Λ fixed) pairs» →
  «(consecutive state pair, W-target or c_W with Λ fixed) pairs» (W-3) and «with fixes entry 1» → «with fixes entries 1-2» (the source
  tail)); L-3 (0012d6710983ec339be8f5d4e051a205cc9207ba, 5,154 bytes, a2512364, fixes entry 3: L-2 with CHECKER C135 §5's R1-R4 applied
  in that order, each old string once: R1 «; L-NEW successor 61)» → «; L-NEW successors 61-62)» (E-1, the source note); R2 inserts «the
  proof of record of HUB-ASC-G's B = 0 case (F′_0 = F_0, DESC-POLY on the whole interval) is referee-originated (REFEREE R-P-N5-ASC §3
  AS-1, restated in P-N5-ASC's fixes entry 1 AS-1), signed by both referees» after «§3-§5 do not use [E-LEV];» (E-2, L41); R3 «so the
  e-vertices of one Λ-class form one forest whose paths are the sequences seq_t(v)» → «hence seq_t(v) = (f, seq_t(y_f))» (E-3, the
  READING out of the signed clause); R4 «with E_t(v) the set of e-vertices in Π_t(v),» → «with seq_t(v) the e-vertices in Π_t(v) in play
  order, E_t(v) their set, an ascent of seq_t(v) a step to a more relevant element,» (E-4, the two terms defined)); L-4
  (4017305a34eac21615ba8f172a9b899544d25659, 5,198 bytes, a744677e, fixes entry 4: L-3 with REFEREE's R5 applied once, «(Lemma
  CHAIN-DECOMP) if the first e-vertex on v's play is f, then» → «(Lemma CHAIN-DECOMP) if seq_t(v) = (f, …), i.e. the first e-vertex on
  v's play is f and f ∈ Π_t(v), then»). L-1 + the two entry-2 strings = L-2, L-2 + R1..R4 = L-3, L-3 + R5 = L-4 (my script, True ×3;
  token diff L-3 → L-4 two hunks, one token out, ten in, both inside R5). L-1: REFEREE «Verdict: fixes entry 1 CORRECT for AS-2, AS-3,
  AS-D1, AS-D2, AS-1 and AS-4. L-1 MATCHES. All statements stay SIGN.» (d4b39be0 §C l. 238); REFEREE-2 «**L-1 NOT YET: W-3 and W-4**
  (DATA rule, wording or counter only; no statement changes) (Opus 5.5, D1).» (fcdc16b4 Add. 2 l. 280). L-2 MATCHES at both referees,
  each after its own byte test: REFEREE successor 28 (94062059, 2026-11-08T01:11:46Z) §D l. 248-252 («Each old string occurs once in
  L-1 and 0 times in L-2. Each new string occurs once in L-2.»; «L-1 with exactly these two changes is byte-equal to L-2: sha1
  f109cb69…, 4,907 B.»), l. 257-263 (W-3 and W-4 in meaning: «W-3 in meaning: CORRECT.»; «W-4 in meaning: CORRECT.»; «That is exactly
  the lemma's condition: the mover a β is entered from is its own mover x.»), l. 270 «Verdict: fixes entry 2 CORRECT (W-3, W-4). L-2
  MATCHES, by the byte test and in meaning. All statements stay SIGN.»; REFEREE-2 successor 32 (d3fed33c, 2026-11-08T01:19:51Z)
  Addendum 3 l. 289-293 (own bt_l2.py: «Word diff L-1 → L-2: exactly «or c_W» inserted, and «entry 1,» → «entries 1-2,» (the source
  tail); nothing else ✓»), l. 294-305 (W-4 read against the lemma: «This is UP-JUMP's statement verbatim»), l. 312-316 «fixes entry 2
  **CORRECT**;» … «**L-2 MATCHES** (byte test, the counter read against the lemma, the re-run, and the DATA rule clause by clause) (Opus
  5.5, D1).» … «Statement verdicts unchanged: all SIGN.». L-3: CHECKER C135 (0942e8be, 2026-11-08T03:04:02Z) wrote its four
  replacements («L-3 with R1-R4 (my script): sha1 0012d6710983ec339be8f5d4e051a205cc9207ba with its newline (5,154 bytes)», l. 78);
  REFEREE successor 28 §E (013f821b, 2026-11-08T04:24:28Z; l. 272-312), own scratch/asc_l3.py: «L-2 + R1..R4 in order is byte-equal to
  L-3.» (l. 280), R1-R4 read in meaning (l. 282-293), and a new finding on the CHAIN-DECOMP clause, which R1-R4 did not touch: «The line
  (L-1 to L-3, unchanged by R1-R4) says «(Lemma CHAIN-DECOMP) if the first e-vertex on v's play is f, then f's successor y_f is a mover
  with Λ_t(y_f) = Λ_t(v) and …».» (l. 296-297), against «The packet's lemma (l. 80) says «If seq_t(v) = (f, …), then …», which needs f ∈
  Π_t(v).» (l. 298), with the instance «v = e_g for any level-0 gate g. The first e-vertex on v's play is v itself, its successor is c_W,
  which is not a mover, and Λ_t(v) = c_W, so v ∉ Π_t(v).» (l. 299-300), shown on RS2 and LEAP_k8 by its own scratch/asc_cd_l0.py (l.
  301-302); verdict «L-3 = L-2 + exactly R1-R4 (byte test PASSES). R1-R4 are CORRECT in meaning.» (l. 310), «L-3 does NOT YET MATCH the
  packet: R5 is required.» (l. 311), «All statements of P-N5-ASC stay SIGN (the packet's form).» (l. 312). REFEREE-2 successor 32
  Addendum 4 (98b9622b, 2026-11-08T04:30:58Z; l. 318-343), own bt_l3.py, «**Verdict: L-3 MATCHES** (Opus 5.5, D1).» (l. 343), which
  successor 33 withdrew in Addendum 5: «**Correction to Add. 4:** «L-3 MATCHES» in Add. 4 was a miss.» (l. 382), «I agree with R5 and with
  its verdict that L-3 did not yet match.» (l. 383-384). L-4: REFEREE-2 successor 33 Addendum 5 (caa26282, 2026-11-08T05:25:44Z; two
  packet line numbers in its text corrected at 05eb5181, 2026-11-08T05:25:54Z; l. 345-387), own bt_l4.py on R5 typed from REFEREE §E:
  «Rebuilding L-3 + R5 gives 4017305a…, 5,198 B, which is L-4 byte for byte («L-4 == L-3 + R5: True»). Nothing else changed.» (l. 353);
  R5 read against packet l. 80 and measured with its own counters (r2cd5.py: «OLDHYP_notinPi = OLDHYP_concl_fails = 8,284» of 33,102
  plays on the pinned instances, l. 361-362, and 1,819 of 5,409 on 300 own random genomes, l. 363); its note N-1 on the «i.e.» (l.
  368-381; Honest limits (x)); «**Verdict: L-4 MATCHES** (Opus 5.5, D1). All statement verdicts are unchanged: SIGN.» (l. 387). REFEREE
  successor 29, R-P-N5-ASC.md §F (the byte test of L-4): <R29-SF>.
- Claims signed (REFEREE successor 27, report 26b2b516 and §C d4b39be0, successor 28 §D 94062059 and §E 013f821b, successor 29 §F
  <R29-SF>; REFEREE-2 successor 31, report 533744a5, Addendum 1 c4166c8b and Addendum 2 fcdc16b4, successor 32 Addendum 3 d3fed33c and
  Addendum 4 98b9622b, successor 33 Addendum 5 caa26282 / 05eb5181). REFEREE's table («## 0. Verdicts», l. 5-17
  of R-P-N5-ASC.md) reads §1 premises «all LANDED; every quote verbatim (script)», Lemma E-MON «(with its E-DOM derivation from R104's
  priorities)», Lemma CHAIN-DECOMP, Lemma SKELETON, Theorem HUB-ASC(B) «(B = 0: DESC-POLY), degree 5·2^B − 3» «SIGN», Corollary HUB-ASC-G
  «and the whole-run corollary» «SIGN (optional AS-1: the B = 0 case of F′ is DESC-POLY on the whole interval, not «word for word» per
  level)», Lemma UP-JUMP, Corollary UP-B, Corollary NOUP «each under [E-LEV]» «SIGN; AS-2 (required, text)», the scope sentence
  «CORRECT», §7 DATA «every replayed number EQUAL (own code)» with AS-D1, AS-D2, §9 «CLEAN». REFEREE-2's table («## Verdicts», l.
  11-24 of R2-P-N5-ASC.md) reads every statement row of §3-§6 «**SIGN** (Opus 5.5, D1)», W-1 and W-2 required (scope strings, pins), §7
  «reproduced by my own code; D-1..D-3 for the line», §9 «✓», and «Nothing is REFUSED. Nothing here bounds R or a running time;
  G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE.» (l. 25). No statement was signed WITH GAP at either referee; every required item
  (AS-2, AS-3, AS-D1, AS-D2; W-1, W-2, D-1, D-2, D-3; then W-3, W-4) was text, pins or DATA wording, and each is closed: REFEREE §C
  l. 238 (entry 1 «CORRECT for AS-2, AS-3, AS-D1, AS-D2, AS-1 and AS-4»), REFEREE-2 Add. 2 l. 279 («W-1, W-2, D-1 (counts), D-2 and D-3
  **met**; AS-1 and AS-4 taken correctly»), REFEREE-2 Add. 3 l. 314 («W-3 and W-4 **met** (W-4 by option (a))»), REFEREE §D l. 270.
  Second and third rounds change no verdict: REFEREE §C l. 238 and §D l. 270 «All statements stay SIGN.»; REFEREE-2 Add. 2 l. 281
  «Statement verdicts are unchanged: all SIGN.» and Add. 3 l. 316 «Statement verdicts unchanged: all SIGN.». The line rounds L-3 and L-4
  change no statement verdict either: REFEREE §E l. 312 «All statements of P-N5-ASC stay SIGN (the packet's form).»; REFEREE-2 Add. 4 l.
  343 «Statement verdicts unchanged: all SIGN.» and Add. 5 l. 387 «All statement verdicts are unchanged: SIGN.». R5 corrects the line's
  wording of CHAIN-DECOMP's hypothesis, not the signed lemma («The statement as signed (the packet's) is unaffected. The line misstates
  its hypothesis.», REFEREE §E l. 307). Nothing is REFUSED.
  Setting: IDEAL-CYC(G) of R118 (a) on Γ(G) of R104, every genome G (Ξ-cycles allowed), values (Λ, Π, k) and ⊴ as in R118's premises;
  §4 is abstract (the chain system CS(M)). Statements as signed (packet with fixes entries 1-2; entries 3-4 change the line only):
  (a) Definitions (§2 l. 51-63): seq_t(v) «the e-vertices that lie in Π_t(v), in the order of the play from v under (σ_t, σ̄_t)», E_t(v)
    their set; lex order on sets of e-vertices; ascents; U_w, M_w, D_E,I(v); CS(M), forests, runs, hubs; the whole-run D_E(v) defined by
    fixes entry 1 AS-4 («the number D_E(v) of distinct (Λ_t(v), E_t(v))», l. 59).
  (b) Lemma E-MON (§3 l. 66-78) [IDEAL-CYC, every genome]: «If Λ_t(v) = Λ_(t+1)(v), then E_t(v) ≤ E_(t+1)(v).»; its proof contains the
    E-DOM step from R104's priorities («Every vertex more relevant than some e-vertex is an e-vertex, c_W, K0 or K3, by [DEF]», l. 70).
    REFEREE SIGN (l. 9), REFEREE-2 SIGN (l. 15).
  (c) Lemma CHAIN-DECOMP (§3 l. 80-88) [IDEAL-CYC]: «If seq_t(v) = (f, …), then the successor y_f of f is a mover, Λ_t(y_f) = Λ_t(v) and
    E_t(v) = {f} ∪ E_t(y_f).» «Hence seq_t(v) = (f, seq_t(y_f)).»; with the packet's «Reading» (l. 89-90: next_t is one forest on the
    e-vertices with cycle node w, every seq_t(v) a path of it), labelled Reading in the packet and checked by both referees (REFEREE l.
    73-74; REFEREE-2 l. 55-56). The Reading is not a clause of the line («A RESULTS line carries signed statements only.», CHECKER C135
    l. 32); it is a proof step of HUB-ASC-G («At each t ∈ I, next_t on the active items is one forest (CHAIN-DECOMP)», packet l. 156).
    The line states the lemma with the packet's hypothesis «seq_t(v) = (f, …)» (R5) and its second sentence (R3). REFEREE SIGN (l. 10),
    REFEREE-2 SIGN (l. 16).
  (d) Lemma SKELETON (a)-(c) (§4 l. 98-107) [any forest of CS(M)]: the τ-path lies on chain(x) in order; the segment elements z satisfy
    z < τ^(i+1)(x) and τ(z) = τ^(i+1)(x), and τ^(i+2)(x) < τ^(i+1)(x); the step from a nonempty segment into τ^(i+1)(x) is an ascent. With
    «τ(x) is non-decreasing in rank» and the level count (§4 l. 94-96). REFEREE SIGN (l. 11), REFEREE-2 SIGN (l. 17).
  (e) Theorem HUB-ASC(B) (§4 l. 109-147) [any run of CS(M) with a hub]: «In any run of CS(M) with a hub whose value has at most B ascents
    at every time, the hub takes at most F_B(M) distinct values.» with F_0(M) := 1 + M(M + 1)/2 (B = 0: DESC-POLY), F_B(M) := (M² + M +
    1)(1 + M·F_(B−1)(M)²), «For fixed B, F_B is a polynomial in M of degree 5·2^B − 3.». REFEREE SIGN (l. 12), REFEREE-2 SIGN (l. 18).
  (f) Corollary HUB-ASC-G (§5 l. 150-163) [every genome G, every vertex v and every interval I of states with Λ_t(v) = w]: «If seq_t(v)
    has at most B ascents for every t ∈ I, then D_E,I(v) ≤ F′_B(M_w).», F′_0 := 1 + M(M + 1)/2 (= F_0; by fixes entry 1 AS-1 «DESC-POLY
    on the whole interval», l. 54-56), F′_B(M) := (M² + 3M + 1)(1 + M·F′_(B−1)(M)²), «No hypothesis is made on any other vertex's
    plays.»; the whole-run corollary «D_E(v) ≤ (2M + 3)·F′_B(M)» from R118 (e). REFEREE SIGN (l. 13), REFEREE-2 SIGN (l. 19).
  (g) Lemma UP-JUMP (§6 l. 166-177) [under [E-LEV]]: an ascent a → b of seq_t(v) with a = e_(x,k), ℓ := lev(x), uses «a β-vertex whose
    Ξ-target is a mover of level > the level of the mover it was entered from, and ≥ ℓ». Corollary UP-B (§6 l. 179-185) [under
    [E-LEV]]: «every seq_t(v) has at most U(G) ascents, so D_E(v) ≤ (2M + 3)·F′_(U(G))(M) for every vertex v.». Corollary NOUP (§6 l.
    187-188) [under [E-LEV], by W-1 in the packet's §1 and table too]: if U(G) = 0, every seq_t(v) is descending and «D_E(v) ≤ (2M +
    3)(1 + M(M + 1)/2).». REFEREE SIGN (l. 14, «each under [E-LEV]»), REFEREE-2 SIGN (l. 20, «(each under [E-LEV])»).
  (h) Hypothesis [E-LEV] (§1 l. 46-48, as fixed by entry 1 W-1): «lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′))»; a hypothesis
    of UP-JUMP, UP-B and NOUP only, not in a landed R-id; §3-§5 do not use it (REFEREE l. 53-55; REFEREE-2 l. 40-41, its CTRL=elevrev
    control: §3-§5 counters stay 0; L-RED R220 §4).
- The RESULTS line (L-4, the title): «The e-set height of one vertex on IDEAL-CYC is polynomial when its plays have boundedly many
  ascents (HUB-ASC-G), in particular, under the e-priority hypothesis [E-LEV], on genomes with boundedly many upward Ξ-edges (UP-B)» …
  «(2026-11-07) — this bounds the e-set height D_E,I(v) only, NOT R and NOT any running time:» … «G-N5-TIME stays OPEN; not M3, not a
  step-4 pass, not a TARGET.md claim (P-N5-ASC, docs/new/P-N5-ASC.md with fixes entries 1-2, docs/new/P-N5-ASC-fixes.md; L-NEW
  successors 61-62)». Its clauses: the notation = (a) in part (seq_t(v), E_t(v), ascents of seq_t(v), the lex order, D_E,I(v), M_w; U_w
  is the packet's); E-MON = (b); CHAIN-DECOMP = (c) in its signed form, hypothesis «if seq_t(v) = (f, …), i.e. the first e-vertex on v's
  play is f and f ∈ Π_t(v), then» and second sentence «hence seq_t(v) = (f, seq_t(y_f))», without the Reading; SKELETON and HUB-ASC(B) =
  (d), (e) (SKELETON named, not stated); HUB-ASC-G = (f) with the whole-run corollary; UP-JUMP, UP-B, NOUP = (g) under (h); the scope tail
  = packet l. 9-11 with the [E-LEV] necessity clause (W-1's measured evidence: REFEREE-2's CTRL=elevrev, L-RED R220's NOUPC_1-3), «§3-§5
  do not use [E-LEV]» and the L41 sentence on HUB-ASC-G's B = 0 case (L41 and L43, below); DATA clause by clause, inline («DATA, clause
  by clause (scope IDEAL-CYC unless abstract; tools in experiments/new/box193/, run by check193.sh):» …); the source note.
- Premise: RESULTS R104's definitions of the genome and of Γ(G) only (packet [DEF], seven quotes verbatim in R104's title, l. 9864;
  «the exact e-priorities to packet §3.1», l. 10085), no R104 theorem; RESULTS R118 (a) IDEAL-CYC(G) (l. 13677: «The game is Γ(G) with
  every Even vertex that is not a mover frozen at its start successor. Odd is unrestricted (gates and K2).»), (b) F1, F2, F3 («(b) Facts
  F1-F6 (§3 l. 68-83) with F4 REPLACED by F4′», l. 13682; F1-F3 quoted from the frozen P-N5-XICYC.md, sha1 149e2414, l. 69-73, inside
  that range), (e) «C ≤ n·(2M + 2).» (l. 13691) in its per-vertex form (Λ_t(v) takes at most 2M + 3 values, in increasing reward); the
  value (Λ, Π, k) and ⊴ of VJ00 §4.2 / Friedmann arXiv 1106.0778 §3, as in R118's premises; HYPOTHESIS [E-LEV] for UP-JUMP, UP-B and
  NOUP only. «Not used anywhere: [LOC], OVT-DV, IN-BOUND, any L-RED lane lemma, F4/F4′, F5, F6.» (packet l. 49). Both referees checked
  every premise quote against RESULTS at 5470cc0c (REFEREE l. 36-45, asc_quotes.py; REFEREE-2 l. 27-34, r2q.py); RESULTS at the local
  trunk c9591e35 (sha1 66e7119615efa5a0bb25b898e32b5b371c55c122, = RESULTS at 5470cc0c, where R120 landed) has R104 at l. 9864 and R118
  at l. 13607 (my script: the R118 quote at l. 13691, R104's l. 10085 quote, the seven [DEF] quotes in R104's title). E-MON uses F1 and
  [VJ]; CHAIN-DECOMP F3 and [DEF]; §5 F1, F2 and (e); §6 [DEF] and [E-LEV] (REFEREE l. 47-49). R1-R5 change no premise.
- L41 and L43. The packet's proofs are L-NEW successor 61's (packet l. 2-4, «This packet carries every proof in full.»), with one
  referee-written step: the B = 0 case of HUB-ASC-G. The packet derives F′_B «word for word» from §4 per refined level (l. 160-161),
  which for B = 0 gives a factor M² + 3M + 1 over F_0; REFEREE wrote the argument that gives F′_0 = F_0 («It is DESC-POLY on the whole
  interval I, which works because τ(x) is monotone on x's active interval and x is active at both times of each change it is blamed
  for.», report l. 117-119, optional AS-1); fixes entry 1 restates it («τ(x) is monotone on x's active interval, and x is active at both
  times of each change it is blamed for.», l. 55-56) and L-4 says «F′_0 = F_0 (DESC-POLY on the whole interval)». The Lead ruled that L41
  (DECISIONS l. 355-358) applies («The Lead ruled that L41 applies.», CHECKER C135 l. 26-27; «L41 applies to G-7 (R121 R-G)»,
  LEAD-STATE l. 2729), and L-4's scope tail carries the sentence C135 wrote (R2): «the proof of record of HUB-ASC-G's B = 0 case (F′_0 =
  F_0, DESC-POLY on the whole interval) is referee-originated (REFEREE R-P-N5-ASC §3 AS-1, restated in P-N5-ASC's fixes entry 1 AS-1),
  signed by both referees». The two signatures: REFEREE, the author, signs it («AS-1, AS-4: taken.», §C l. 215; «Verdict: fixes entry
  1 CORRECT for AS-2, AS-3, AS-D1, AS-D2, AS-1 and AS-4. L-1 MATCHES. All statements stay SIGN.», l. 238; on R2: «R2 (AS-1): CORRECT. I
  read it as the author lane.», §E l. 284); REFEREE-2 checked it independently after its own report and signs it («I agree. I checked
  it now: the top of seq_t(v) is monotone on I (≤ M changes), and an item x blamed for a change lies on the hub's value at both times,
  so it is active at both.», Add. 1 l. 212-214; «A good clarification; it changes no verdict.», l. 215; «AS-1 «F′_0 = F_0 (DESC-POLY on
  the whole interval)» ✓», Add. 2 l. 254; on R2: «True. My predecessor checked AS-1 independently in Add. 1», Add. 4 l. 333). The joint
  gap map: empty. Corollary HUB-ASC-G is SIGN at both from the first round (REFEREE l. 13, «SIGN (optional AS-1: the B = 0 case of F′
  is DESC-POLY on the whole interval, not «word for word» per level)»; REFEREE-2 l. 19), neither referee lists a gap on it in any round,
  and REFEREE's AS-1 ends «One sentence would make this explicit; the bound is right.» (report l. 119). L43: no statement is asymptotic
  beyond its explicit polynomial; the [E-LEV] necessity clause is DATA of others (a control and a lane's frozen instances), not DEAD; no
  statement is killed.
- Fixes (docs/new/P-N5-ASC-fixes.md, append-only; entries 1-2 by L-NEW successor 62, entries 3-4 by L-NEW successor 63; entry 1 at
  19cc23e3, l. 1-67, under «Lead 22:41Z, 22:46Z, 22:48Z: «GO, fixes entry 1, now. One entry»» (l. 3); entry 2 at a5dcf9c6, l. 69-91,
  under «Lead 00:15Z: «P-N5-ASC fix round 2 … Write fixes entry 2 (append-only) and line L-2 by script»» (l. 69); entry 3 at a2512364,
  l. 93-125, under «Lead 03:30Z: «P-N5-ASC fix round 3, from CHECKER 21 C135 … Write fixes entry 3 (append-only) and
  docs/new/P-N5-ASC-line-L3.txt by script»» (l. 93); entry 4 at a744677e, l. 127-140, under «Lead 04:56Z: «P-N5-ASC fix round 4: ONE
  required string (R5), from REFEREE 28 §E»» (l. 127)):
  - W-1 (REFEREE-2) = AS-2 + AS-3 (REFEREE) + R220's scope item: three packet strings («(only for §6 UP-JUMP, UP-B and NOUP)», the table
    string, the title string «in particular, under the e-priority hypothesis [E-LEV], on genomes with boundedly many upward Ξ-edges
    (UP-B)»); every UP-B / NOUP clause of the line carries «under [E-LEV]» (4 times in L-4, by script); the scope sentence kept.
  - W-2 = AS-D2: asc.pins gains the five box192/inst instances (34 rows with the fixes file and L-1; 35 with L-2 at a5dcf9c6).
  - D-1 = AS-D1: asc193.py prints edomunits, decunits, tmonunits; the sums 1,892, 24,818, 2,552 and UP-JUMP's «asc» 1,956 are in the line.
  - D-2: ug193.py on all 13 instances, output committed. D-3: chain193.py M 6 and 7 at A 0 re-run by check193.sh.
  - AS-1 (optional, TAKEN): F′_0 = F_0, DESC-POLY on the whole interval (above). AS-4 (optional, TAKEN): D_E(v) defined.
  - Not taken (l. 61-62): REFEREE-2's N-1 and N-2 («both are sharper constants; the stated ones stay valid»).
  - Entry 2: W-3 (the E-MON unit string; «tmonunits counts every successor y of an e-vertex with Λ(y) fixed, c_W included», l. 77) and
    W-4 option (a) (upfail requires the Ξ-step to go strictly up from the β's own mover; «upfail 0 in 1,956 ascents (the «asc» sum), so
    the set is unchanged», l. 85); line L-2 by script; asc.pins 35 rows.
  - Entry 3: CHECKER C135 «Verdict: FAIL (E-1 to E-4; one L-3 with four replacements, §5)» (l. 15), «No statement, proof, definition or
    DATA figure changes; E-3 narrows one clause to its signed form.» (l. 17): E-1 the source note (R1), E-2 the L41 sentence (R2), E-3 the
    READING inside CHAIN-DECOMP's clause (R3), E-4 seq_t(v) and «ascent» undefined in the line (R4); L-3 by mkl3_193.py, which asserts
    C135's sha1 0012d671… (fixes l. 97-100); asc.pins 37 rows (l. 124). C135's ruling on the UPDATE procedure: «R118's procedure applies»
    (l. 38); its placement: «R121 after R120 (landed 5470cc0c), before «**Erratum E-1**»; its UPDATE after R120's.» (l. 44).
  - Entry 4: REFEREE's R5 (§E l. 303-304), CHAIN-DECOMP's hypothesis in the packet's form; L-4 by mkl4_193.py, which asserts REFEREE's
    predicted sha1 4017305a… (fixes l. 137-138); «DATA rule: R5 is a statement wording; its witness is REFEREE's asc_cd_l0.py. No tool or
    DATA output changes.» (l. 139); asc.pins 39 rows (l. 140).
  - No statement of the packet changes; entry 1 changes the [E-LEV] scope words, pins, unit counts and the F′_0 sentence; entry 2
    changes one unit string and one counter condition; entries 3-4 change five strings of the line and the pins.
- Not signed: packet §7-§9 (DATA, machine checks, TARGET diff and limits), the «Context, not a clause» row (l. 208), the packet's
  Reading after CHAIN-DECOMP (l. 89-90; a proof step of HUB-ASC-G, see (c)), the L-RED R220 adversary data and REFEREE-2's control (DATA
  of others, cited in the scope tail as evidence for [E-LEV]'s necessity), REFEREE's asc_cd_l0.py witness and REFEREE-2's r2cd5.py
  counters (referee data on the old line wording), box 193's other lane items (ASC-GATE, ASC-EXP, DEAD RMON-2, the CS(M, A) values),
  BOX 194 (P-N5-QUIET, separate packet).
- Referee strengthening (NOT part of this entry; referee checks):
  (i) REFEREE: own asc_quotes.py, asc_cs.py, asc_game.py («IDEAL-CYC replay on successor 26's own VJ engine xicyc_vj.py and Γ builder
    xicyc_replay.py, written from R104's text», l. 31): the CS(M) maxima for M 1-5 at B 0 and B 1 equal to §7 (l. 132-142); RSG_K4,
    cR_d2_w8_R22, rd2_d9, RS3 replayed, every E-MON, CHAIN-DECOMP and UP-JUMP unit 0 violations, U(G) and max ascents equal to §7's four
    UP-B rows (l. 147-154); at §C a second route for the NOUPC numbers («So «one route only» is now two routes for the max-ascent numbers.»,
    l. 225).
  (ii) REFEREE-2: own r2hub.py (exhaustive CS(M), M 1-6, B 0-3: «**0 violations of F_B.**», l. 113), r2asc.py on its own builder
    (13 instances: EMON on 46,830 (step, vertex) pairs at every vertex, CDEC 24,818, UPJ 10,751 ascents in the full form, UPB 50,881,
    HUBG on 4,051 (vertex, Λ-interval), all 0, l. 123-128; 300 own NOUP genomes, seed 31, max ascents 0, l. 129-130); the control
    CTRL=elevrev (l. 131-135).
  (iii) L-RED successor 55, R220 (claude/l-red 68a1f609, docs/red/R220-asc.md; an adversary, not a signature): «No BROKEN, no GAP.» (l.
    17); exhaustive CS(M) M ≤ 5, B 0-3 (§1); HUB-ASC-G on 58 runs under both e-orders, 0 violations (§2); «Finding (scope, not a kill):
    [E-LEV] is necessary for UP-JUMP, UP-B and NOUP.» (l. 54).
  (iv) The L-3 / L-4 round. REFEREE §E: the old CHAIN-DECOMP hypothesis fails at level-0 e-vertices, shown on RS2 and LEAP_k8 with its own
    builder and engine (scratch/asc_cd_l0.py, asc_logs/cd_level0.out; «It holds in every genome that has a level-0 mover.», l. 302).
    REFEREE-2 Add. 5: own counters in R2-P-N5-ASC/r2cd5.py (outputs r2cd5_inst.out on the 13 pinned instances from a git archive of
    a744677e, r2cd5_noup.out on 300 own random genomes, seed 33): «This confirms REFEREE 28's R5 witness independently. CDEC 0 of 24,818
    reproduces the lane's CHAIN-DECOMP count exactly.» (l. 364); the converse of the «i.e.»: «Measured: 0 plays with an e-vertex as cycle
    node among the 50,881 plays of the pinned instances and the 20,549 plays of the random genomes.» (l. 376-377).
- Honest limits: (i) Nothing here bounds R, a run length or a running time; the step from D_E to R needs OVT-DV and CONJECTURE IN-BOUND,
  neither in RESULTS («OVT-DV» and «IN-BOUND» 0 times in RESULTS and GAPS at c9591e35). (ii) UP-JUMP, UP-B and NOUP hold only under
  [E-LEV], which is in no landed entry: it is the order of the fleet's builder (box189/gamma3.py) and of R104's packet §3.1, and R104's own text
  leaves the order among e-priorities open (l. 10085); without it they are false (REFEREE-2's control; L-RED's NOUPC_1-3). (iii) F_B is
  far from tight (degree 5·2^B − 3 against the exact maxima; REFEREE-2 N-3) and super-polynomial if B grows like log M (packet l.
  222-223). (iv) The DATA units are narrower than the statements: E-MON is counted at W-targets and c_W only (TAIL-MON form), UP-JUMP on
  ascents of movers' plays with Λ below every e, E-DOM per vertex (static); the every-vertex counts are referee data (REFEREE-2's 46,830
  and 10,751). (v) HUB-ASC(B) for B ≥ 2 and HUB-ASC-G's constants have no DATA of their own; the exhaustive data stop at M 7 (B 0) and M
  5 or 6 (B 1). (vi) All game DATA are runs of implementations (box191 idealcyc.py, box189 gamma3.py; the referees' own engines) on 13
  instances and 300 random genomes. (vii) Names: «E-MON», «CHAIN-DECOMP», «SKELETON», «HUB-ASC», «DESC-POLY», «UP-JUMP», «UP-B»,
  «NOUP», «E-DOM», «TAIL-MON», «[E-LEV]» are new to RESULTS («E-MON» occurs there only inside «SETTLE-MON» and «VALUE-MONO»); «U(G)»
  occurs once in R105's body for another quantity; «R217» in the line is an L-RED round label (docs/red/), not a RESULTS label. (viii) The
  source note names fixes entries 1-2 and «L-NEW successors 61-62», the authors of the packet and of the proof-bearing entry 1; the
  line-only entries 3-4 and their author, successor 63, are not named (CHECKER C134's N-S ruling, as C135 E-1 states it: «the note
  names the authors of proof-bearing text; a line-only entry need not be named», l. 22-23; R118's and R120's landed notes likewise). (ix)
  Literature: VJ00 §4.2 and Friedmann arXiv 1106.0778 §3, as cited by R118 (landed); no novelty is claimed. (x) CHAIN-DECOMP's «i.e.»:
  the line's gloss «the first e-vertex on v's play is f and f ∈ Π_t(v)» implies «seq_t(v) = (f, …)» on every game (REFEREE-2 Add. 5 l.
  365-367); the converse fails only if an e-vertex is v's cycle node (l. 368-375), which no measured play has (l. 376-377); REFEREE-2
  calls it «note, no change required» (l. 368). The hypothesis the lemma is signed with is «seq_t(v) = (f, …)», first in the clause.
- Data (DATA, not proof): experiments/new/box193/ at l-new a744677e, run by check193.sh (asc193.py, ug193.py, noup193.py, hubasc193.py,
  skel193.py, chain193.py and the rest; IDEAL-CYC by box191/idealcyc.py on box189/gamma3.py), its output committed as check193.out
  (sha1 d4fb21644db639435806886bb6c709add84d9ded, 71 lines; unchanged since a5dcf9c6: from a5dcf9c6 to a744677e the only box193 changes are
  asc.pins and the new mkl3_193.py and mkl4_193.py, git diff); wired into experiments/new/check.sh as blocks «BOX 193 ASC» (l. 988-996:
  the diff against check193.out and three grep lines) and «P-N5-ASC» (l. 997-1003: the 39 rows of asc.pins, sha1
  d7d10aaed0fa29b462c38143472b4ab3e9e37152, the packet, the fixes file, L-1 to L-4, the tools, mkl3_193.py, mkl4_193.py and the 13
  instances), run by scripts/verify.sh; both blocks byte-equal at a5dcf9c6 and a744677e. Re-run from a git archive of a744677e
  (experiments, docs/new, scripts): check193.sh 2026-11-08T05:53:16Z-05:54:01Z, rc 0, 71 lines, byte-equal to check193.out; the two
  check.sh blocks 2026-11-08T05:54:06Z-05:54:52Z, rc 0, «BOX 193 ASC: … = frozen: PASS» and «P-N5-ASC: packet and 39 pinned files match
  asc.pins: PASS»; mkl3_193.py and mkl4_193.py re-run (C135 from 0942e8be), rc 0, output cmp-equal to L-3 and L-4. CHECKER C135 re-ran
  the two blocks from a git archive of df0d2a25 (02:48:22Z-02:49:02Z, rc 0, l. 47-50). Sums over the 13 instance lines (my script):
  edomunits 1,892, tmonunits 2,552, decunits 24,818, asc 1,956, edomfail, tmonfail, decfail, upfail, gfail 0; ug193.py 13 lines, max
  ascents ≤ U(G) on each; NOUP «genomes 300 seed 1: Xi-cyclic 179; max ascents 0»; HUB-ASC 11 (M 4, B 0), 16 (M 4, B 1), 29 (M 5, B 1);
  SKELETON 125 and 1,296 forests, 0 violations; CS(M, A 0) 2, 4, 7, 11, 16, 22, 29 for M 1-7 (= F_0). Both referees re-ran check193.sh
  at a5dcf9c6 (REFEREE §D l. 264-268, byte-equal; REFEREE-2 Add. 3 l. 301-303, byte-equal) and their own engines (above). R1-R5 add no
  DATA and change no count (REFEREE-2 Add. 4 l. 342, Add. 5 l. 385-386; fixes l. 125, l. 139). Instances: experiments/new/box193/inst/{CLR_k8s16,
  FPORT_n2, FPORT_n3, LEAP_k8, RS2, RS2_L8M6, RS3, RSG_K4}.json (L-RED R217's) and experiments/new/box192/inst/{cR_d2_w8_R22, rd2_d9,
  rd2_d10, rd3_d7, rf_d5}.json, each pinned in asc.pins.
- Signatures: REFEREE docs/referee/R-P-N5-ASC.md: successor 27's report 26b2b51667d9ee3a0df318d127f844e6279b1d07 (2026-11-07T22:27:05Z;
  «Written from 2026-11-07T22:25Z (date -u); the header time of record is the commit time.»), «I did NOT read docs/referee-2/ for this
  report.» (l. 3), verdict table l. 5-17; §C d4b39be0e5589cba49d08df3ca185332519b8dd6 (2026-11-07T23:51:43Z; heading «date -u at writing
  2026-11-07T23:51Z»), l. 198-238, verdict l. 238 «Verdict: fixes entry 1 CORRECT for AS-2, AS-3, AS-D1, AS-D2, AS-1 and AS-4. L-1
  MATCHES. All statements stay SIGN.»; successor 28's §D 94062059582976623de438f1873a7725345f2252 (2026-11-08T01:11:46Z; heading «date
  -u at writing 2026-11-08T01:07Z»), l. 240-270, «Verdict: fixes entry 2 CORRECT (W-3, W-4). L-2 MATCHES, by the byte test and in
  meaning. All statements stay SIGN.» (l. 270); successor 28's §E 013f821bd31de10ee93abf4f5c279962e1570de9 (2026-11-08T04:24:28Z; heading
  «date -u at writing 2026-11-08T04:09Z»), l. 272-312, «L-3 = L-2 + exactly R1-R4 (byte test PASSES). R1-R4 are CORRECT in meaning.» (l.
  310), «L-3 does NOT YET MATCH the packet: R5 is required.» (l. 311), «All statements of P-N5-ASC stay SIGN (the packet's form).» (l.
  312); successor 29's §F: <R29-SF>. REFEREE-2 docs/referee-2/R2-P-N5-ASC.md: successor 31's report
  533744a51d23c45d7d6107041eef4dee29129253 (2026-11-07T22:17:18Z), «Independent: docs/referee/ not read on this item.» (l. 2), verdict
  table l. 11-25; Addendum 1 c4166c8b49ffbace7ec09bd2edb5c6d9189b7f67 (2026-11-07T22:47:01Z), l. 192-230, «**Order.** Read only now: my
  report (533744a5) was on origin before I opened it (Lead 22:48Z). REFEREE did not read mine.» (l. 193), «**Verdict.** The two reports
  agree.» (l. 224); Addendum 2 fcdc16b45ea2086ae307137036bacbcfc8d36a23 (2026-11-07T23:52:10Z), l. 232-281, «fixes entry 1
  **CORRECT**;» (l. 278); successor 32's Addendum 3 d3fed33cbe4694c3961e563e42cf438258697a9e (2026-11-08T01:19:51Z; heading «2026-11-08
  01:08Z by date -u»), l. 283-316, «**L-2 MATCHES** (byte test, the counter read against the lemma, the re-run, and the DATA rule clause
  by clause) (Opus 5.5, D1).» (l. 315), «Statement verdicts unchanged: all SIGN.» (l. 316); successor 32's Addendum 4
  98b9622b99e0dfd16353c68572a74c9ee8eb7c8f (2026-11-08T04:30:58Z; heading «2026-11-08 04:09Z by date -u»), l. 318-343, «**Verdict: L-3
  MATCHES** (Opus 5.5, D1). Statement verdicts unchanged: all SIGN.» (l. 343), corrected by Addendum 5 (l. 382-384); successor 33's
  Addendum 5 caa262828941b73116bb018351cfd605a1f04b95 (2026-11-08T05:25:44Z; heading «2026-11-08 05:25Z by date -u»; its packet line
  numbers corrected at 05eb5181e0af63723a038279cefe7582fe3d9846, 2026-11-08T05:25:54Z, «REFEREE-2 R2-P-N5-ASC Add. 5: packet line numbers
  corrected (70-71, 74-76)»), l. 345-387, «**Verdict: L-4 MATCHES** (Opus 5.5, D1). All statement verdicts are unchanged: SIGN.» (l.
  387). Lane (claude/l-new): L-NEW successor 61, 95dc76d7 (packet FROZEN, asc.pins, check blocks); successor 62, 19cc23e3 (fixes entry 1,
  L-1) and a5dcf9c6 (fixes entry 2, L-2); successor 63, a2512364 (fixes entry 3, L-3) and a744677e (fixes entry 4, L-4).
- INDEPENDENCE: the packet's proofs are L-NEW's except the AS-1 step (L41 and L43, above); each referee re-derived every proof step
  (REFEREE «## 3. Proofs (each step re-derived)»; REFEREE-2 «## Proofs (own re-derivation)») and replayed the statements on its own code
  (REFEREE: asc_cs.py, asc_game.py on its own VJ engine and Γ builder; REFEREE-2: r2hub.py, r2asc.py on its own builder; «Lane code was
  run only, never read for my checks or imported.», REFEREE-2 l. 8). Each referee wrote its first report without reading the other's
  (REFEREE l. 3; REFEREE-2 l. 2); REFEREE-2 compared afterwards (Add. 1, «**Verdicts: identical.**», l. 194). The L-1 and L-2 wording is
  the lane's under the Lead's routing (fixes l. 3, l. 69); L-3's four replacements are CHECKER C135's (§5) and L-4's one replacement is
  REFEREE's R5 (§E), each applied by the lane's script. Each referee byte-tested every line with its own script (REFEREE §C, §D
  scratch/asc_l2.py, §E scratch/asc_l3.py; REFEREE-2 Add. 2 bt_l1.py, Add. 3 bt_l2.py, Add. 4 bt_l3.py, Add. 5 bt_l4.py) and read it in
  meaning. REFEREE-2 records its own round-1 miss on W-4 («**My miss in round 1:** I had not read the counter and called this clause
  OK.», Add. 2 l. 267-268) and its Add. 4 miss on the CHAIN-DECOMP hypothesis («It did not compare the CHAIN-DECOMP hypothesis of L-1 to
  L-3 against packet l. 80. REFEREE 28 found the gap.», Add. 5 l. 382-383). L-RED R220 read neither referee file («Referee files not read.»,
  R220 l. 2).
- TARGET.md diff: TARGET.md §1 defines a parity game; IDEAL-CYC of R104 / R118 is a Howard run on the genome game Γ(G), and no statement of
  this entry bounds a running time, an iteration count or R; the bounded quantity D_E,I(v) counts distinct e-sets on one vertex's plays
  (packet §9: «This packet proves no algorithm polynomial.», «The quantity is not a running time.»; REFEREE §7 l. 191-192 «It is not M3
  (§7 e needs a precise theorem in TARGET vocabulary). CLEAN.»; REFEREE-2 l. 175-176 «D_E,I(v) is a count of distinct e-sets in
  IDEAL-CYC runs of R104 / R118 genomes, not a running time (TARGET.md §2-§4); not M3/M4, not a gauntlet step ✓.»). «M» is R104's number
  of options / e-vertices, not TARGET.md's m (REFEREE l. 193). It is not an algorithm claim, so TARGET.md §5's gauntlet does not apply, and
  it is not a step-4 pass. L-4 carries «G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim» and «this bounds the
  e-set height D_E,I(v) only, NOT R and NOT any running time» (by script), as L-2 did when C135 passed its TARGET.md diff (l. 64-65); of
  R1-R5 only R2 touches the scope tail, adding the L41 sentence. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER the last UPDATE on GAPS l. 11 at landing (R120's, «UPDATE 2026-11-07 21:05Z:
RESULTS R120 (P-TOWER-FUEL; CHECKER C134 0c816917)», the last at the local trunk c9591e35), as a pure insertion with one separating space
before the row's closing « |». BUILT FROM L-4 by upd121b.py (R118's procedure, which CHECKER C135 ruled applies: run121() unchanged,
with R121's start «more relevant than w): », its five labels and its source prefix; controls R97-R116 rebuilt byte for byte and the
R117-R120 controls as landed, each compared with GAPS l. 11, True ×24; on L-3 the same build gives C135 §5's
f545cba7c97eee853387a5efb617984538e27806; sha1 d3a423302a45850e3400c0e15e14d7dfdd600508 of the line without newline and unfilled, =
f545cba7… with R5 applied without its label, which the procedure moves behind the clause). <DATE>, <HH:MM> and <checker> are the
landing date, time and the C135 commit, all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R121 (P-N5-ASC; CHECKER C135 <checker>) [refereed-only] LANDED: The e-set height of one vertex on IDEAL-CYC is polynomial when its plays have boundedly many ascents (HUB-ASC-G), in particular, under the e-priority hypothesis [E-LEV], on genomes with boundedly many upward Ξ-edges (UP-B) (premises: RESULTS R104's definitions of the genome and of Γ(G) only; RESULTS R118 (a) IDEAL-CYC(G), (b) F1, F2, F3 and (e) «C ≤ n·(2M + 2).» in its per-vertex form (Λ_t(v) takes at most 2M + 3 values, in increasing reward); VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the value (Λ, Π, k) and its order ⊴; HYPOTHESIS [E-LEV] (only for §6 UP-JUMP, UP-B and NOUP): lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′)), the order of Γ(G) as built by experiments/new/box189/gamma3.py (and of R104's packet §3.1), not in a landed line; not used: [LOC], OVT-DV, IN-BOUND, any L-RED lane lemma, F4/F4′, F5, F6), with seq_t(v) the e-vertices in Π_t(v) in play order, E_t(v) their set, an ascent of seq_t(v) a step to a more relevant element, sets of e-vertices compared lexicographically by their most relevant differing element, and D_E,I(v) the number of distinct E_t(v) on an interval I of states with Λ_t(v) = w fixed (M_w := the number of e-vertices more relevant than w): if Λ_t(v) = Λ_(t+1)(v) then E_t(v) ≤ E_(t+1)(v) (Lemma E-MON); if seq_t(v) = (f, …), i.e. the first e-vertex on v's play is f and f ∈ Π_t(v), then f's successor y_f is a mover with Λ_t(y_f) = Λ_t(v) and E_t(v) = {f} ∪ E_t(y_f), hence seq_t(v) = (f, seq_t(y_f)) (Lemma CHAIN-DECOMP); in the abstract chain system CS(M) (items 1..M, a run of forests with every chain lex-nondecreasing), a hub whose value has at most B ascents at every time takes at most F_B(M) distinct values, F_0(M) = 1 + M(M + 1)/2 (DESC-POLY), F_B(M) = (M² + M + 1)(1 + M·F_(B−1)(M)²), a polynomial of degree 5·2^B − 3 for fixed B (Lemma SKELETON and Theorem HUB-ASC(B)); for every genome G, every vertex v and every interval I with Λ_t(v) = w, if seq_t(v) has at most B ascents for every t ∈ I then D_E,I(v) ≤ F′_B(M_w), F′_0 = F_0 (DESC-POLY on the whole interval), F′_B(M) = (M² + 3M + 1)(1 + M·F′_(B−1)(M)²), and over the whole run the number D_E(v) of distinct (Λ_t(v), E_t(v)) is at most (2M + 3)·F′_B(M) (Corollary HUB-ASC-G); an ascent of seq_t(v) needs a Ξ-edge from a mover to a mover of strictly higher level, so under [E-LEV] every seq_t(v) has at most U(G) ascents (U(G) := the number of options whose Ξ-target has a higher level) and D_E(v) ≤ (2M + 3)·F′_(U(G))(M); under [E-LEV], if U(G) = 0 then every seq_t(v) is descending and D_E(v) ≤ (2M + 3)(1 + M(M + 1)/2) (Lemma UP-JUMP, Corollary UP-B, Corollary NOUP; UP-JUMP, UP-B and NOUP under HYPOTHESIS [E-LEV]): this bounds the e-set height D_E,I(v) only, NOT R and NOT any running time: the step from D_E to R needs OVT-DV ([LOC], L-RED R217 §2) and CONJECTURE IN-BOUND (box 192 Addendum 9), neither landed; [E-LEV] is NECESSARY for UP-JUMP, UP-B and NOUP: with the e-priorities in decreasing level order (still R104's shape) NOUP fails on 209 of 21,116 plays of U(G) = 0 genomes, up to 2 ascents (REFEREE-2 control CTRL=elevrev, docs/referee-2/R2-P-N5-ASC.md at claude/referee-2 533744a5), and L-RED's frozen NOUPC_1 / 2 / 3 have U(G) = 0 and max ascents 2 / 3 / 4 under the e-order (−level, gate) (witness NOUPC_1, t 0, v 10; claude/l-red 68a1f609, experiments/red/r220/inst/, .pg sha1 82e41194…, 7ea66452…, 94db68d5…; one route only); §3-§5 do not use [E-LEV]; the proof of record of HUB-ASC-G's B = 0 case (F′_0 = F_0, DESC-POLY on the whole interval) is referee-originated (REFEREE R-P-N5-ASC §3 AS-1, restated in P-N5-ASC's fixes entry 1 AS-1), signed by both referees; DATA, clause by clause (scope IDEAL-CYC unless abstract; tools in experiments/new/box193/, run by check193.sh): E-DOM part of E-MON's proof: violations 0 in 1,892 vertices, E-MON (TAIL-MON form): violations 0 in 2,552 (consecutive state pair, W-target or c_W with Λ fixed) pairs, CHAIN-DECOMP: violations 0 in 24,818 (state, vertex) pairs with a nonempty e-sequence, UP-JUMP: violations 0 in 1,956 ascents of movers' plays with Λ below every e (asc193.py; set: the 13 instances, 8 L-RED R217 instances in inst/ and 5 in box192/inst/, all pinned in asc.pins); UP-B under [E-LEV]: max ascents ≤ U(G) on all 13 instances (unit: max ascents over (state, vertex) plays; ug193.py); NOUP under [E-LEV]: 300 random genomes with no strictly upward Ξ-edge, 179 Ξ-cyclic, max ascents 0, max D_E per Λ-interval 3 (noup193.py 300 1); HUB-ASC(B), only the hub constrained: B 0 max 11 at M 4 (= F_0), B 1 max 16 at M 4 and 29 at M 5 (unit: distinct hub values; set: all runs of CS(M); abstract; hubasc193.py); SKELETON: violations 0 on all forests of CS(4) and CS(5) (skel193.py); tightness of B = 0: F_0 attained for M 1-7 (2, 4, 7, 11, 16, 22, 29; chain193.py, M 6 and 7 re-run by check193.sh); no separate DATA for HUB-ASC(B) with B ≥ 2, HUB-ASC-G's constants, the whole-run corollary and UP-B's D_E bound (P-N5-ASC, docs/new/P-N5-ASC.md with fixes entries 1-2, docs/new/P-N5-ASC-fixes.md; L-NEW successors 61-62). G-N5-TIME stays open.

Addendum (subagent, for the Lead; does not land; written 2026-11-08T02:02:20Z by date -u). (1) FIRST FILL on line L-2 (l-new a5dcf9c6, sha1
f109cb69…), to CHECKER C135. I edited docs/agents/R121-draft.md only; no merge, no commit and no push by me; the Lead commits this file.
Re-fetch at 2026-11-08T02:02:10Z (claude/l-new, claude/referee, claude/referee-2, claude/checker, claude/vibrant-johnson-nxvvxo; rc 0):
l-new a2024f59 (a2024f59de74e42e5b4e6a2377d72f56718c3d65, committed 2026-11-08T01:33:15Z, on origin only after the first fetch; «L-NEW
successor 62 handover (box 194 results, P-N5-ASC / P-N5-QUIET duties, open items, traps); park»; git diff d9c49489 a2024f59 names only
notes/L-NEW.md; the packet, the fixes file, L-1, L-2 and experiments/new/box193 equal a5dcf9c6's, git diff --quiet), referee 94062059,
referee-2 d3fed33c, checker d38a2194, origin trunk 51eb6534 (all unchanged); local trunk HEAD 8912e145 (unchanged). (2) TITLE d[271]
(l. 272) = "### R121 [refereed-only] " + L-2 without its newline + ", CHECKER PASS (docs/checker/C135.md, checker PENDING)", checked
by script (chk121.py): equal, byte for byte (True); and the title minus that prefix and that tail is L-2 (True); the only «### R»
heading of this file; 4,888 characters, 4,985 bytes, sha1 of the heading line without its newline
0b8eed9affbea3100ee73f88842e9b140c9dc0a1; 117 «(» / 117 «)» (L-2's 116 and the fill's), 0 "|", «R1xx» 0, «[refereed-only]» once. (3)
SHAPE. The entry block is l. 272-482 (python slice d[271:482], 211 lines), followed by a blank line (d[482]); 0 "|" in it; the title's fill string
once in it (three times in the whole file: the title, item (1) of the record and item (2) of this Addendum). The GAPS preamble is
l. 484-491 (d[483:491]); the UPDATE is l. 492 (d[491]), one line, sha1 6635b14ea1e7c98457d671c451318120412a7079 without newline and
unfilled (= upd121L2.txt, True), 4,937 bytes, 4,842 characters, 817 tokens, 116 «(» / 116 «)», 0 "|", one each of «<DATE>», «<HH:MM>»,
«<checker>», «2026-11-07» 0 times, « — » 0 times. A landing script slices d[271:482] for the entry and reads d[491] for the UPDATE, with
«R121», «C135», PREV = R120's block and UPDATE (landed, G-P). The FIRST FILL record is l. 2-270 (d[1:270]), then a blank line. (4) WHAT IS
LEFT: the Lead's ruling on G-7 (L41) and on G-1's R-B; CHECKER C135 on this file (G-1, G-7, G-2 with optional R-R, G-U, optional R-Q);
if any replacement is taken, an L-3 by L-NEW (fixes entry 3, line only), both referees' byte tests, and a second fill (title, line
history, Object, L41 and L43 (the scope-tail sentence), Honest limits (viii), Signatures, the UPDATE rebuilt from L-3). The Lead merges
claude/l-new (a5dcf9c6 or later), claude/referee (94062059) and claude/referee-2 (d3fed33c) before landing, then lands R121 after R120
with <DATE>, <HH:MM> and <checker> filled. (5) QUOTE SWEEP (chk121.py: outermost guillemet quotes, nested ones inside them, split at
«…», parts of 6+ characters, whitespace-normalised, NO docs/agents draft as a source; sources: the packet, fixes, L-1, L-2, asc.pins
and check.sh at a5dcf9c6, REFEREE's file at 26b2b516, d4b39be0 and 94062059, REFEREE-2's at 533744a5, c4166c8b, fcdc16b4 and d3fed33c,
R220 at 68a1f609; at HEAD RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, LEAD-STATE, NOW, TARGET.md, CLAUDE.md; C134, C116 and
notes/CHECKER.md on claude/checker; asc193.py, ug193.py, noup193.py, hubasc193.py, skel193.py, chain193.py, check193.sh and check193.out
at a5dcf9c6; P-N5-XICYC.md at fd1266a5; the subjects of the commits cited (a2024f59's included); r120b/tools/upd120b.py; my outputs blk2.out, data121.out,
upd121.out, upd121p.out, upd121L2.txt, l2shape121.out and the re-run check193 output): on the draft before this Addendum, the first-fill record 191 quotes, 150 parts, 0 not
found; title and body 160 quotes, 150 parts, 0 not found; GAPS preamble and UPDATE 4 quotes, 3 parts, 0 not found; whole file 355
quotes, 303 parts, 0 not found; negative control (a made-up quote) reported missing (True); the run on the final file is in
chk_final.out. lp121.py: 109 quotes and line references at their cited lines (REFEREE l. 3-270, REFEREE-2 l. 2-316, packet l. 4-219,
fixes l. 3-85, R220 l. 2-54, check.sh l. 988-1003, RESULTS l. 4026, 4068, 9864, 10085, 10267, 13607, 13677-13678, 13682, 13691,
DECISIONS l. 355-358, LEAD-STATE l. 2649, notes/CHECKER.md l. 6, C116 l. 67, asc193.py l. 50-94), 0 failed (one reference corrected
from l. 212-213 to l. 212-214 before the final run). (6) STALE STATUS (chk121.py): in the entry block «PENDING» 1 (the title's fill),
«NOT YET» 1 (REFEREE-2's L-1 verdict, quoted as history), «first fill» 2 (L41 and L43 and Honest limits (viii): the open flags G-7 and
G-1, to be re-worded at the second fill or at landing), «R-B» 1 and «R-G» 1 (the same two sentences); «pending», «will », «not landed» 0;
GAPS preamble and UPDATE: «first fill» 1 (the preamble names R120's UPDATE as the last at this first fill); line 1 «NOT LANDED» 1 (R121 is not landed).
(7) LANDING SIMULATION (sim121.py on in-memory copies of RESULTS 66e71196… and GAPS 2a41c765… at the local trunk 8912e145): R121 a pure
insertion directly before «**Erratum E-1**» (prefix byte-unchanged True, suffix byte-unchanged True); RESULTS 14,962 → 15,174 lines
(+212); R118 l. 13,607, R119 l. 13,879, R120 l. 14,114, R121 at l. 14,320-14,530, blank l. 14,531, «**Erratum E-1**» to l. 14,532, E-2
14,545, Note E-3 14,573, Dead ends 14,604; order R110-R121, E-1, E-2, E-3, Dead ends: True. GAPS: only l. 11 changes (True), the closing
" |" replaced by " " + the filled UPDATE + " |"; "|" on l. 11 76 → 76; «UPDATE 2026-» 55 → 55 plus one head with the simulation year
2099 after R120's (True); R121's UPDATE last (True); 23 → 23 lines. Fill values used only for the simulation: 2099-01-08, 00:00,
0000000. (8) UPDATE (upd121.py): r120b/tools/upd120b.py l. 1-311 (Parts A-E2) exec'd, with one assertion relaxed, as upd120.py did for
R118: its l. 242 asserts that R119's UPDATE is the last on l. 11, which R120's landing ended, so «and last==l.find(h119L)» is dropped
there; then Part F, the R120 control AS LANDED: R105's procedure on L-3 (4f25ae6f) = R120-draft.md d[639] (unfilled sha1 17cba597…,
True), filled with GAPS l. 11's stamp 2026-11-07 21:05 0c816917 = that segment (True); all controls True ×24 (R97-R120), the last UPDATE
on l. 11 R120's (True). Part G, R121 by run121() (run118()'s steps; G-U), = the direct build (True). Token diff L-2 → UPDATE, 11 hunks,
43 tokens out, 42 in: the head inserted («UPDATE <DATE> <HH:MM>Z: RESULTS R121 (P-N5-ASC; CHECKER C135 <checker>) [refereed-only]
LANDED:»); the five labels moved behind their clauses («E_(t+1)(v) (Lemma E-MON);», «seq_t(v) (Lemma CHAIN-DECOMP);», «B (Lemma
SKELETON and Theorem HUB-ASC(B));», «3)·F′_B(M) (Corollary HUB-ASC-G);», «(Lemma UP-JUMP, Corollary UP-B, Corollary NOUP; UP-JUMP, UP-B
and NOUP under HYPOTHESIS [E-LEV]):» in place of « (2026-11-07) —»); «bound; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a
TARGET.md claim» → «bound»; «61)» → «61). G-N5-TIME stays open.». Nothing else. With R-G then R-B (each old string once in L-2 and once
in the UPDATE): L-2 + proposals sha1 c23e11d0905a8d73e6f605993c8533b488facc7c (5,126 bytes, 118 / 118, one " — "), its UPDATE by the same
procedure 988c1e7ade9ee9c4fbf3412bca696f926b1aab16 (5,156 bytes; = the L-2 UPDATE with R-B applied and R-G's sentence inserted after
«§3-§5 do not use [E-LEV]», True; upd121p.py). R-R and R-Q not built into a line or an UPDATE (each old string once in L-2 and once in
the UPDATE, by script). Pipe rule: the filled R121 UPDATE appended after R120's (landed) keeps 76 "|" on l. 11, R121's last, prefix
byte-unchanged (True). (9) NOT VERIFIED / NOT DONE: scripts/verify.sh not run (check193.sh in full and the two P-N5-ASC check.sh blocks
only, from a git archive of a5dcf9c6; not the whole experiments/new/check.sh); the referees' tools not re-run (their files read);
REFEREE-2's control and L-RED's NOUPC run not re-run by me (only the three .pg sha1s checked); no IDEAL-CYC engine of my own (the game
DATA are the lane's tools, re-run); idealcyc.py and gamma3.py not read beyond the imports; the proofs not re-derived by me beyond reading
both referees' re-derivations against the packet (the G-7 and G-2 items are text checks); VJ00 / Friedmann not opened by me (R118's
landed premise, cited in the same words); no Oink run (L-2 cites no Oink check). (10) Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r121/ (fetch.out, fetch.time,
fetch2.out, fetch2.time; src/ (the packet, fixes, L-1, L-2, asc.pins, check.sh, the referee files at each commit, R220); arch/ = git
archive of a5dcf9c6 (experiments, docs/new, scripts), check193.rerun, check193.rc, blk.start, blk.end, blk2.out, blk2.rc, blk2.start,
blk2.end; tools/upd121.py, upd121.out, upd121L2.txt; tools/upd121p.py, upd121p.out, L2prop.txt, upd121prop.txt,
upd121prop_expected.txt; tools/l2shape121.py, l2shape121.out; tools/data121.py, data121.out; tools/chk121.py, chk_p1.out,
chk_final.out; tools/lp121.py, lp_p1.out, lp_final.out; tools/sim121.py, sim_p1.out, sim_final.out; tools/assemble121.py, parts/,
filltime.txt, addtime.txt; R121-draft.md).

Addendum 2 (subagent, for the Lead; does not land; written 2026-11-08T06:08:25Z by date -u). (1) SECOND FILL on line L-4 (l-new a744677e, sha1
4017305a…), to CHECKER C135 Add. 1. I edited docs/agents/R121-draft.md only; no merge, no commit and no push by me; the Lead commits
this file. Heads at the fetch of 2026-11-08T05:50:40Z: l-new 1a846565, referee 8505df48, referee-2 05eb5181, checker fa8add12, origin
trunk c8f42538; local trunk HEAD c9591e35. Re-fetch at 2026-11-08T06:06:58Z (the same five branches; rc 0): all five heads unchanged,
local trunk HEAD c9591e35 unchanged; REFEREE's §F still not on origin. (2) TITLE l. 405 (d[404]) = "### R121 [refereed-only] " + L-4
without its newline + ", CHECKER PASS (docs/checker/C135.md, checker PENDING)", checked by script (chk121b.py): equal, byte for byte
(True); the title minus that prefix and that tail is L-4's bytes without the newline (True); the only «### R» heading of this file;
5,172 characters, 5,276 bytes, sha1 of the heading line without its newline 878504c449d8acc4eb20acd95bcf844dbe9f4132; 126 «(» / 126
«)» (L-4's 125 and the fill's), depth never negative, 0 "|", «R1xx» 0, «[refereed-only]» once. (3) SHAPE. The entry block is l. 405-706
(python slice d[404:706], 302 lines), followed by a blank line (d[706]); 0 "|" in it; «checker PENDING)» once in it (three times in the
file before this Addendum: the title, item (1) of the first fill's record and item (2) of the first fill's Addendum). The GAPS preamble is l. 708-715
(d[707:715]); the UPDATE is l. 716 (d[715]), one line, sha1 d3a423302a45850e3400c0e15e14d7dfdd600508 without newline and unfilled (=
upd121L4.txt, True), 5,228 bytes, 5,126 characters, 866 tokens, 125 «(» / 125 «)», 0 "|", one each of «<DATE>», «<HH:MM>»,
«<checker>», «2026-11-07» 0 times, « — » 0 times. A landing script slices d[404:706] for the entry and reads d[715] for the UPDATE, with
«R121», «C135», PREV = R120's block and UPDATE (landed, G-P). The SECOND FILL section is l. 2-134, the first fill's record l. 135-404
(rec121b.py: 04323afb's l. 2-271, byte-unchanged, directly before the title, True) and the first fill's Addendum l. 718-787 (04323afb's
l. 494-563, byte-unchanged, directly after the UPDATE and a blank line, True). (4) PLACEHOLDER. One token, R29-SF in angle brackets,
stands where REFEREE successor 29's §F (its byte test of L-4) gives its commit and verdict; it is not on origin at either fetch, and this
draft states no REFEREE verdict on L-4. It occurs 4 times: l. 18 (the SECOND FILL section, the referee head), l. 478 (Object,
the line rounds, after REFEREE-2's L-4 verdict), l. 480 (Claims signed, the list of REFEREE rounds) and l. 671 (Signatures, after
REFEREE's §E); 0 times in the GAPS preamble and the UPDATE (the UPDATE carries no referee verdict) and 0 times in this Addendum. Each is
to be replaced by the §F commit (40 hex digits where the neighbouring text gives them, as in Signatures; 8 in Object and Claims signed)
with its time and its verdict line quoted with its line number; if §F does not find L-4 MATCHES, the draft needs a further fill.
(5) WHAT IS LEFT: REFEREE successor 29's §F on L-4 and the four tokens filled; CHECKER C135 Add. 1 on this file (G-U, the notes N-I and
N-A with their optional R-I and R-A, N-S, D-8); the Lead merges claude/l-new (a744677e or later), claude/referee (013f821b and §F),
claude/referee-2 (05eb5181) and claude/checker before landing, then lands R121 after R120 with <DATE>, <HH:MM> and <checker> filled.
(6) QUOTE SWEEP (chk121b.py: chk121.py's rule, outermost guillemet quotes, nested ones inside them, split at «…», parts of 6+
characters, whitespace-normalised, NO docs/agents draft as a source; sources: the first fill's (r121/src: the packet, fixes, L-1, L-2,
asc.pins and check.sh at a5dcf9c6, REFEREE's file at 26b2b516, d4b39be0 and 94062059, REFEREE-2's at 533744a5, c4166c8b, fcdc16b4 and
d3fed33c, R220) plus, at a744677e, the packet, fixes, L-1 to L-4, asc.pins, check.sh, the box193 tools, check193.sh, check193.out,
mkl3_193.py and mkl4_193.py; the fixes file at a2512364; REFEREE's file at 013f821b (= the head); REFEREE-2's at 98b9622b, caa26282 and
05eb5181; at HEAD c9591e35 RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, LEAD-STATE, NOW, TARGET.md, CLAUDE.md; C134, C135, C116 and
notes/CHECKER.md on claude/checker; P-N5-XICYC.md at fd1266a5; the subjects of the commits cited; r120b/tools/upd120b.py; the first
fill's outputs and mine (blk.out, check193.rerun, l4rel121b.out, upd121b.out, opt121b.out, upd121L4.txt)): on the draft before this
Addendum, SECOND FILL section 80 quotes, 69 parts, 0 not found; first-fill record 191 quotes, 150 parts, 0 not found; title and body
231 quotes, 224 parts, 0 not found; GAPS preamble and UPDATE 4 quotes, 3 parts, 0 not found; first-fill Addendum 42 quotes, 27 parts, 0
not found; whole file 548 quotes, 473 parts, 0 not found; negative control (a made-up quote) reported missing (True); the run on the
final file is in chk_final.out. lp121b.py: 70 quotes and line references new at this fill (REFEREE l. 119-312, REFEREE-2 l. 212-387,
fixes l. 93-140, C135 l. 15-84, packet l. 55, 80, 156, LEAD-STATE l. 2729, 2742, DECISIONS l. 355-358, asc193.py l. 66-68) each at its
cited lines, 0 failed. (7) STALE STATUS (chk121b.py): in the entry block, the title's fill excepted, «pending», «will », «awaiting», «to
come», «not landed», «second fill» and «first fill» 0 times each (case-insensitive); «not yet» 4 times, all inside quotes of the
referees' L-1 and L-3 verdicts (history); «R-G» once, inside the quote of LEAD-STATE l. 2729; «R-B», «R-R», «R-Q», «6635b14e» and
«f545cba7» 0 times. GAPS preamble and UPDATE: the same seven words 0 times each. Line 1 «NOT LANDED» once (R121 is not landed). Model
names: «Opus» 8 times in the file before this Addendum, all in the entry block, all inside quoted referee verdicts. (8) LANDING SIMULATION (sim121b.py: r121/tools/sim121.py
unchanged but for printing the trunk, on in-memory copies of RESULTS 66e71196… and GAPS 2a41c765… at the local trunk c9591e35, equal at
origin trunk c8f42538): R121 a pure insertion directly before «**Erratum E-1**» (prefix byte-unchanged True, suffix byte-unchanged True;
the inserted block = the draft's entry block, True); RESULTS 14,962 → 15,265 lines (+303); R118 l. 13,607, R119 l. 13,879, R120 l. 14,114,
R121 at l. 14,320-14,621, blank l. 14,622, «**Erratum E-1**» to l. 14,623, E-2 14,636, Note E-3 14,664, Dead ends 14,695; order
R110-R121, E-1, E-2, E-3, Dead ends: True; "|" in RESULTS unchanged (1,477). GAPS: only l. 11 changes (True), the closing " |"
replaced by " " + the filled UPDATE + " |"; "|" on l. 11 76 → 76; «UPDATE 2026-» 55 → 55 plus one head with the simulation year 2099
after R120's (True); R121's UPDATE last (True); 23 → 23 lines. Fill values used only for the simulation: 2099-01-08, 00:00, 0000000.
(9) UPDATE: (c) of the SECOND FILL section; upd121b.out has the controls and the 11 token hunks. (10) NOT VERIFIED / NOT DONE:
scripts/verify.sh not run (check193.sh in full, the two P-N5-ASC check.sh blocks and mkl3_193.py / mkl4_193.py only, from a git archive
of a744677e; not the whole experiments/new/check.sh); the referees' tools not re-run (REFEREE's asc_l3.py and asc_cd_l0.py, REFEREE-2's
bt_l3.py, bt_l4.py and r2cd5.py; their files read); REFEREE's R5 witness not reproduced by me (no IDEAL-CYC engine of my own); the N-1
proviso (no e-vertex is a cycle node) not proved or refuted by me; the proofs not re-derived by me; data121.py not re-run (no tool or
DATA output changed since a5dcf9c6: check193.out byte-equal, re-run (b)); REFEREE successor 29's §F not read (not on origin); no Oink
run (L-4 cites no Oink check). (11) Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r121b/ (fetch.time, fetch2.out; src/
(the packet, fixes, L-1 to L-4, asc.pins, check.sh at a744677e; fixes_a2512364.md; ref_013f821b.md, ref_head.md; ref2_98b9622b.md,
ref2_caa26282.md, ref2_05eb5181.md; R121-draft-04323afb.md, the first fill, not a quote source); arch/ = git archive of a744677e
(experiments, docs/new, scripts), check193.start, check193.end, check193.rc, check193.rerun, blocks.sh, blocks_run.sh, blk.start,
blk.end, blk.rc, blk.out; mk/ (C135.md, mkl3.out, mkl4.out, the regenerated L-3 and L-4); tools/l4rel121b.py, l4rel121b.out;
tools/upd121b.py, upd121b.out, upd121L3.txt, upd121L4.txt; tools/opt121b.py, opt121b.out; tools/chk121b.py, chk_p1.out, chk_p2.out,
chk_final.out; tools/lp121b.py, lp_p1.out, lp_final.out; tools/sim121b.py, sim_p1.out, sim_final.out; tools/rec121b.py, rec_final.out;
tools/assemble121b.py, parts/ (secondfill.txt, obj.txt, claims.txt, mid.txt, tail.txt, preamble.txt, addendum2.txt, record1.txt,
add1.txt, body.txt), filltime.txt, addtime.txt; R121-draft.md).
