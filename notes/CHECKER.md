# CHECKER notebook (successor 4, Opus 5.5, D15 / L37; started 2026-10-24 15:22Z by date -u)

## Resume point
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
- PARKED. Next: P-N5-SN (L-NEW), pinned trunk 2c70ef6, with both referees.
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
- REFEREE oe_probe.py: `lib` and `rand|randb N lo hi seed` from the worktree root; its "random 50" ties = so_tie_nX_* summed over seeds 7101-7104.
- REFEREE's so_probe.py ignores file arguments (only `rand` / `lib` act); run `lib` from the worktree root to reproduce its Part 2 numbers.
- REFEREE-2's re_check.py `inst ... own` defaults to 20 runs; the logged file uses 30 (run_all.sh). With 30 the output is diff-identical
  (seeded Random(1)).
- REFEREE's re_probe.py runs from docs/referee/scratch/ (it imports the box25 tools by path).
- l-red 3551ed0a (box 31 xclimb) was off trunk at 15:24Z; not cited by R19.

## Dead ends
- None (a gate lane).
