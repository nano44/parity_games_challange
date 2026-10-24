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
- C33 (R24 draft at trunk ed14b38, packet P-N5-U1, plus the R22 POST-LANDING NOTE at l.1019): FAIL on E-1 only (REFEREE-2's N-U1-3 proof is in §C.4, not §C.3). Re-runs EXACT. The R22 note PASSES.
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
- REFEREE-2's re_check.py `inst ... own` defaults to 20 runs; the logged file uses 30 (run_all.sh). With 30 the output is diff-identical
  (seeded Random(1)).
- REFEREE's re_probe.py runs from docs/referee/scratch/ (it imports the box25 tools by path).
- l-red 3551ed0a (box 31 xclimb) was off trunk at 15:24Z; not cited by R19.

## Dead ends
- None (a gate lane).
