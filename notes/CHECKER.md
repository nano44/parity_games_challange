# CHECKER notebook (successor 5, Opus 5.5, D15 / L37; started 2026-10-25 08:55Z by date -u; successor 4's notes below are kept as history)

## Handover check (successor 5)
Written 2026-10-25 09:01Z (date -u). Predecessor: successor 4, session_01G2KY2Canmj54k82CwBrZYc, handover commit 4d8ba2b5
(C40 Addendum 1, "handover to successor 5"). Every answer measured from the repository; commands named.

1. Branch, head, distance to trunk.
   - Container started on claude/checker at 52a1e489 (C27 Add. 4), 'git status': "up to date with 'origin/claude/checker'" (stale
     remote ref). `git fetch origin claude/checker claude/vibrant-johnson-nxvvxo`: origin/claude/checker 737b1938, later 4d8ba2b5
     (Add. 1 landed 09:00Z, watched by a fetch loop). `git merge --ff-only origin/claude/checker` → 4d8ba2b5.
   - `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` at 4d8ba2b5: 1 ahead, 1 behind trunk 3e339bbb.
   - `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` → merge commit 21b82302: 2 ahead, 0 behind. This file's commit makes 3 ahead.
2. Open work and next step.
   - C28-C40 all CLOSED (`grep -n "CLOSED\|Addendum" docs/checker/C40.md`; C40 Add. 1: R31 landed verbatim at 3f2b5c1). Nothing pending.
   - C41 = R32 (packet P-N5-FRZ). docs/agents/R32-draft.md does not exist (`ls docs/agents/R32*`: none). Inputs at trunk 3e339bbb
     (`sha1sum`): packet docs/new/P-N5-FRZ-box34.md 39df373c… (frozen edbccb69; pin trunk 25fda0f per the Lead), fixes
     docs/new/P-N5-FRZ-fixes-box34.md 168de464…, docs/referee/R-N5-FRZ.md f542c2d7… (3a520ce7, Addendum 3171efc7), docs/referee-2/R2-N5-FRZ.md
     2039d70d… (20a73ca1, §C f546b43c). Still coming: fixes2 (L-NEW successor 15), REFEREE successor 7's §C.
     Branch heads 09:00Z (`git merge-base --is-ancestor`): referee 1f13a6f9 OFF trunk, l-new 5f02ceba OFF trunk, referee-2 f546b43c on trunk.
   - Next step: after GO, setup_oink.sh (tools/ absent in this container), then pre-check pins/sha1 across first-parent states, read
     packet + fixes + both reports, prepare the re-run list; on the Lead's draft sha1, the five checks as in C37-C40, report docs/checker/C41.md.
3. GAPS rows. `awk -F'|' '$4 ~ /CHECKER/' docs/GAPS.md`: no output; CHECKER owns no row (13 rows). Relevant (landing side):
   G-N5-TIME | major | L-NEW (L-LIT T22; referees later) | open; last UPDATE: "R31 [refereed-only] LANDED (P-N5-FBW + fixes; CHECKER
   C40) … In review: P-N5-FRZ (both referees signed; landing next), P-N5-L2, P-N5-NJB, P-N5-TOG". R32 adds one append-only UPDATE to
   this row; my landed check: old row is a prefix of the new one, status stays open.
4. Owner rulings verbatim (docs/DECISIONS.md), status from docs/DECISIONS-INDEX.md (`grep -E "^\| *(D1|D15|D18|L37|L40) "`):
   - D1 (row D1 "active"; key line): "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim,
     including the fleet's own, as wrong until it passes the gauntlet below."
   - D15 (row D15 "active"; L37 "active"): "q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it"
   - D18 (row D18 "active"; L40 "active"): "Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting
     ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where
     needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems."
   For the gate: no landed claim stronger than both signatures (D1); labels "(Opus 5.5, D15)" checked (L37 (1)); PROVED / CONJECTURE /
   OPEN and ASSUMPTION labels exact, nothing resting on an ASSUMPTION called PROVED (L40 (3), (4)).
5. Trap found. The container's clone was stale: local claude/checker AND its remote-tracking ref sat at 52a1e489 (C27, 2026-10-24),
   13 CHECKER reports behind, while `git status` said "up to date". Working from it would have re-done or contradicted C28-C40.
   Check: `git fetch` the branch first and compare `git rev-parse HEAD origin/claude/checker` after the fetch; fast-forward only.
   (Second, measured: tools/oink/build is absent here, so verify's Oink smoke is NOT RUN and re-runs cannot use zlk until setup_oink.sh.)

## Resume point (successor 5)
- IDLE 11:5xZ (date -u): C41-C44 all CLOSED (R32-R35 landed verbatim). Next per the Lead: P-N5-SCOPE and P-N5-RL once drafted.
- C41 (R32, P-N5-FRZ pinned 25fda0f) 09:21Z (date -u): main report docs/checker/C41.md: FAIL at eb3f659 (draft sha1 6d23f986…):
  E-1 REFEREE C.6 commit 9ad6bfba uncited (limit (iii)'s REFEREE half rests on it); E-2 "3,610 in climbs aimed at leaves" = all 12
  climbs (leave climbs 1,040); N-1 fixes2 unrefereed (content = REFEREE-2 C.4 row 4, checked); N-2 R29 (c) vs (e), outside the draft.
  Every re-run EXACT. Add. 1 d43a3222: rev. 2edf33e (d8369b2b) E-1 fixed, E-2 open, N-3 optional. Add. 2 7f5df64b: PASS at 06fbc11
  (5552686a). Add. 3: PASS at f87c5fd (b3f7fc67, + N-3). Add. 4: R32 landed verbatim at trunk 8e6d6c2
  (N-4 optional: GAPS UPDATE omits (L2), ¬H1 SN). C41 CLOSED. Next: C42 = R33 (P-N5-L2) when the Lead sends the draft sha1.
- Worktrees (scratchpad): wt = eb3f659, wtR = 3a520ce, wtC6 = 9ad6bfba; tools/oink/build symlinked; Oink built 09:1xZ (setup_oink.sh exit 0).

- C42 (R33, P-N5-L2 pinned 04b3f48) 10:3xZ (date -u): main report docs/checker/C42.md: FAIL at 8d95c31 (draft sha1 dbadd869…):
  E-1 REFEREE §C cited 5e85c70 (= R-N5-NJB §C) instead of ce241061; E-2 REFEREE-2 "+ e65cbcd" (NJB-only). N-1 limit (iv) "three
  climbs"; N-2 limit (v) vs box-35 DATA instances; N-3 l2_pc needs NMAX=14. Every re-run EXACT. Add. 1: PASS at 48478ab (8d9d6590; E-1, E-2, N-1, N-2
  fixed). Add. 2: R33 landed verbatim at trunk
  00bd18b. C42 CLOSED. Next: R34 (P-N5-NJB), R35 (P-N5-TOG) when the Lead sends draft sha1s (each after a lane fixes2).
- Worktrees: wt42 = 8d95c31, wtR42 = 7626354e. Scratch c42/trace.py = per-state trace via REFEREE l2_probe.states().

- C43 (R34, P-N5-TOG pinned d3daae1) 10:5xZ (date -u): main report docs/checker/C43.md: FAIL at 4be5bba (draft sha1 3b20da39…):
  E-1 "238 files" ×2 = REFEREE-2's text, but its files.lst / 484 logs / 31,434 runs give 239. N-1 fixes2 unrefereed (records only);
  N-2 REFEREE l.9 5e85c706; N-3 REFEREE-2's 238. Every re-run EXACT. Add. 1: PASS at 3c0c2aa (33dbffd3). Next: Add. 2 =
  landed-text check; then NJB = R35.
- Worktrees: wt43 = 4be5bba, wtR43 = fff6e624.

- C44 (R35, P-N5-NJB pinned a7d85b3) 11:3xZ (date -u): main report docs/checker/C44.md: FAIL at a627c7d (draft sha1 c28e6902…):
  E-1 (5′) paraphrased (signed = REFEREE l.27 / fixes NJB-2 verbatim); E-2 REFEREE-2 SIGN list omits ENT-SHAPE (1)-(4).
  N-1 l-si 90b5fb3f edits cited fixes2 in place (8ceee866 → 647386fb, off trunk); N-2 REFEREE C.5 3 rows; N-3 b6 fb18 also on SPEC.
  Every re-run EXACT. Worktrees wt44 = a627c7d, wtR44 = 524d93f5. Add. 1: rev. 7b1a47d (f730b554; fixes2 → 647386fb):
  E-1, E-2 OPEN. Add. 2: PASS at 3fc6cf1 (6f77aca6). Add. 3: R35 landed verbatim at 4151e41, C44 CLOSED.
  C43 Add. 2: R34 landed verbatim at e784554, C43 CLOSED.

## Resume point (successor 4, history)
- PARKED 16:22Z (date -u). C28 CLOSED:
  - main report b53136d7: FAIL E-1..E-6;
  - Add. 1 e5c46943: E-1..E-6 fixed, E-7 = the §A citation;
  - Add. 2 8f2ee01d: PASS at 1494ae1;
  - Add. 3: R19 landed verbatim at trunk 4155cde.
- C29 CLOSED 17:19Z (date -u):
  - main report 5a395403: FAIL E-1..E-3;
  - Add. 1 aa909fd0: PASS at 865a33a (REFEREE §C7 a1de721 signs the Corollary);
  - Add. 2: R20 landed verbatim at trunk c33700c.
- C30 CLOSED 19:3xZ (date -u):
  - main report 7bf19993: FAIL E-1..E-4;
  - Add. 1 679ea117: PASS at f9c75d2, including the R19 POST-LANDING NOTE (RESULTS l.882);
  - Add. 2: R21 landed verbatim at trunk e72db8d.
- C31 CLOSED 20:4xZ (date -u):
  - main report c500832b: FAIL E-1;
  - Add. 1 4db6e4c0: PASS at b112bd5;
  - Add. 2: R22 landed verbatim at trunk 200a511.
- C32 CLOSED 21:3xZ (date -u):
  - main report 2cd52a68: FAIL E-1;
  - Add. 1 0077eed8: PASS at 0d72267;
  - Add. 2: R23 landed verbatim at trunk 8de876b.
- C33 CLOSED 22:3xZ (date -u):
  - main report 0102170b: FAIL E-1; the R22 POST-LANDING NOTE PASS;
  - Add. 1 59a97995: PASS at a85316a;
  - Add. 2: R24 landed verbatim at trunk 7bcf681.
- C34 CLOSED 23:5xZ (date -u):
  - main report 298e4b6d: FAIL E-1, E-2;
  - Add. 1 4278b5a2: fixes part 2 PASS, E-1/E-2 still open;
  - Add. 2 e9f7b674: PASS at 7666336;
  - Add. 3: R25 landed verbatim at trunk 40ef7ed.
- C35 (R26, P-N5-U23 pinned 7666336) 00:4xZ (date -u):
  - main report docs/checker/C35.md: PASS at 37a4a06 (draft sha1 abd35e40…); optional N-1 (limit (v) "~90" relayed only via fixes §5;
    L-RED R65 off trunk 1c2f1d8f), N-2 (no change);
  - Add. 1: R26 landed verbatim at trunk eb8e22e. C35 CLOSED.
- C36 (R27 = P-N5-LP pinned bc42f2c + P-N5-SO pinned 1ef02bb) 01:5xZ (date -u):
  - main report docs/checker/C36.md: FAIL at e8c26f3 (draft sha1 d22885f8…): E-1 joint gap map's SO rows are REFEREE-2 §C only (REFEREE §C
    = Part 1 only); E-2 HI's "≤" Consequence single-signed (REFEREE HI-1); N-1 limit (v) wake type sourced only in notes/L-NEW.md; N-2.
  - Add. 1 c64ec130: PASS at 1d35e8e (draft sha1 a9ba93ec…; E-1, E-2, N-1, N-2 fixed);
  - Add. 2: R27 landed verbatim at trunk 58de2bc. C36 CLOSED.
- C37 (R28, P-N5-OE pinned 361d18c) 02:2xZ (date -u):
  - main report docs/checker/C37.md: PASS at f6786ba (draft sha1 a5229c8e…); optional N-1 (Reading "≡ Z" is one direction, REFEREE §3.6),
    N-2 (696b08c touches only notes/REFEREE.md);
  - Add. 1: R28 landed verbatim at trunk de7a635 (GAPS row: stale R27 "§C pending" clause replaced by the R28 update). C37 CLOSED.
- C38 (R29, P-N5-CLS pinned 486107a) 03:22Z (date -u):
  - main report docs/checker/C38.md: PASS at 42eccf9 (draft sha1 e4189cd3…); optional N-1 (N-CLS-2 is a row of REFEREE C.3 only);
  - Add. 1 f0cf7c90: PASS at 1efb9f9; Add. 2 7d31abaa: PASS at b2fcd17 (N-1 fixed);
  - Add. 3: R29 landed verbatim at trunk cf6801e. C38 CLOSED.
- C39 (R30, P-N5-SN pinned 2c70ef6 + fixes §2b) 04:47Z (date -u):
  - main report docs/checker/C39.md: FAIL at a9fc3c9 (draft sha1 08526310…): E-1 epsseg_cex_n48 re-absorption is transition 14, not 13;
    N-1 L-RED box 37 line sourced only in LEAD-STATE (R67 not on trunk); N-2 sample names; N-3 note.
  - Add. 1 262104b2: PASS at 91582c0 (E-1, N-1, N-2 fixed);
  - Add. 2: R30 landed verbatim at trunk 659f574. C39 CLOSED.
- C40 (R31, P-N5-FBW pinned e69772b) 08:41Z (date -u):
  - main report docs/checker/C40.md: PASS at 61c7cd1 (draft sha1 f2d4a606…); optional N-1 (REFEREE-2's committed logs predate its
    'tight' counter; outside the draft);
  - Add. 1: R31 landed verbatim at trunk 3f2b5c1. C40 CLOSED.
- PARKED for good (successor 4). The Lead starts CHECKER successor 5 for R32 (P-N5-FRZ).
- HANDOVER to successor 5. Every check C28-C40 is CLOSED; nothing is pending in docs/checker/. Next: R32 (P-N5-FRZ). The method is the five-step gate in
  'Conventions' plus: verify every sha1 at the pin and across first-parent states; check each cited commit is an ancestor; re-run named
  instances (n5 + check_sol2 + one-Odd count) and one probe per referee in a detached worktree (symlink tools/oink/build); trace every
  Data number to a referee file line; landed check = cmp block vs draft lines 3-end with the header fill, delete block + cmp rest vs
  the pre-landing RESULTS, GAPS row prefix (append-only, agreed with the Lead 02:46Z).
- Oink is built in this container (tools/oink/build, 8fbf0a7), so verify's Oink smoke now runs. In a worktree, symlink tools/oink/build.
- Handover check: docs/agents/handover-checks/CHECKER.md (f28356ae).

## Conventions (from C27, kept)
- Pin everything: draft trunk SHA, signed object sha1, report commits. Each cited commit must be an ancestor of the trunk pin.
- Re-fetch referee, referee-2 and lane heads before a verdict; name any head that is off trunk.
- Re-runs go in a detached worktree of the pin, scripts unmodified (scratchpad wt/); compare against the referees' logs with `diff`.
- Report E- items (required) and N- items (optional) with fixes. Addenda go at the end of the same file, one per draft SHA.
- Push: scripts/push.sh > file; echo $? (never piped). Oink built here at 19:0xZ by setup_oink.sh (a fresh container must rebuild it).

## Sources opened (for C28)
- docs/new/P-N5-RE-box26.md @52c7261 (sha1 8dba4576…); docs/referee/R-N5-RE.md @a3d1f70; docs/referee-2/R2-N5-RE.md @dd5aaa2;
  docs/new/N5-time-box21.md §3.5 (Lemma G (d), the source of the draft's (a) wording); docs/new/N5-xing-box27.md §6, §8, §9;
  docs/red/R58-n5-width.md §13c.

## Things only I know
- (successor 5) Briefs may name a SHA from the sibling packet (NJB vs L2 on the same branch): check each cited SHA with
  `git show --stat` against the report file. REFEREE l2_pc.py library row needs NMAX=14 (default 9).
- orx.py (EPS=1) ex_ORX = (first ε, second ε, exit) with transition indices; absorption = transition k with x0 ∈ F_k ∩ R_{k+1}.
  Scratch tool c39tools/trace33.py (scratchpad, not committed) prints σ̄(o) and exit-in-R per transition via box32/dormant.py.
- REFEREE oe_probe.py: `lib` and `rand|randb N lo hi seed` from the worktree root; its "random 50" ties = so_tie_nX_* summed over seeds 7101-7104.
- REFEREE's so_probe.py ignores file arguments (only `rand` / `lib` act); run `lib` from the worktree root to reproduce its Part 2 numbers.
- REFEREE-2's re_check.py `inst ... own` defaults to 20 runs; the logged file uses 30 (run_all.sh). With 30 the output is diff-identical
  (seeded Random(1)).
- REFEREE's re_probe.py runs from docs/referee/scratch/ (it imports the box25 tools by path).
- l-red 3551ed0a (box 31 xclimb) was off trunk at 15:24Z; not cited by R19.

## Dead ends
- None (a gate lane).
