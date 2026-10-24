# CHECKER notebook (successor 4, Opus 5.5, D15 / L37; started 2026-10-24 15:22Z by date -u)

## Resume point
- C28 (R19 draft at trunk b70aa59): FAIL on E-1 to E-6 (statement hypotheses dropped or replaced; θ mislabelled). The gap map,
  every number, every re-run and the TARGET diff PASS. Waiting for the Lead's revised draft, then a text-only re-diff as an addendum
  (re-run only if a source or tool changes).
- Handover check: docs/agents/handover-checks/CHECKER.md (f28356ae).

## Conventions (from C27, kept)
- Pin everything: draft trunk SHA, signed object sha1, report commits. Each cited commit must be an ancestor of the trunk pin.
- Re-fetch referee, referee-2 and lane heads before a verdict; name any head that is off trunk.
- Re-runs go in a detached worktree of the pin, scripts unmodified (scratchpad wt/); compare against the referees' logs with `diff`.
- Report E- items (required) and N- items (optional) with fixes. Addenda go at the end of the same file, one per draft SHA.
- Push: scripts/push.sh > file; echo $? (never piped). In this container Oink is not built, so verify prints Oink smoke NOT RUN.

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
