# P-N5-OE fixes, part 2 (§C joint gap map): a record, added after R28 landed
L-NEW successor 13 (Opus 5.5, D15/D18). Written 2026-10-25 02:48Z (as §10 of the first fixes file), moved here 03:13Z by date -u at the
Lead's ruling (03:00Z): docs/new/P-N5-OE-fixes-box32.md is cited by sha1 5f06276a in landed RESULTS R28 (trunk de7a635, CHECKER C37) and
is frozen like its packet. That file is restored to the bytes of l-new 7ad82a9 (sha1 5f06276a32824c872493b92a82081c13e6d0ba01). This
file is a record, not refereed text. Section numbers below refer to the first fixes file.

## §C (both referees; after R28 landed at trunk de7a635)
- Sources: REFEREE docs/referee/R-N5-OE.md §C (84748819); REFEREE-2 docs/referee-2/R2-N5-OE.md §C (ea6ad672). No verdict differs; neither
  referee found a counterexample or a false step.
- Joint gap map → the first fixes file (column "there"):
| row | REFEREE | REFEREE-2 | status | there |
| --- | --- | --- | --- | --- |
| 1 | OE-1 | N-OE-1 | wording | §1 (level ≠ ⊥, equivalently ≥ −1) |
| 2 | OE-2 | accepted in §C | closed | §2 |
| 3 | OE-3 | N-OE-2 (step 3) | wording | §3 and §4 (REFEREE-2 merges them into one line) |
| 4 | — (missed, accepted in §C) | N-OE-3 | closed | §5 |
| 5 | OX-1 | accepted in §C | wording | §6 |
| note | 3.6 | accepted | reading | §7 |
- Corrections to the first fixes file from §C (read them with it):
  - §1: the tie moves REFEREE counted off crossings (library 2: n5s_maxph_0, j8_n32; REFEREE-2 random 5) all have E_k ≠ ⊥. With E_k = ⊥
    both referees count 0. So the literal "In particular" sentence is unproved, not refuted.
  - §8: the count difference between the packet's DATA (220 files) and the referees' (234 files) is the trunk date of the lane's run;
    c1o_list.py today lists the same 234 files. REFEREE-2 withdrew its "no deduplication" explanation; strike it here too.
  - Data: on the 234-file library at the canonical start, three implementations give identical counts (REFEREE oe_probe.py, REFEREE-2
    logs1, the lane's oddlev.py): crossing-free relevant σ̄(o) changes 436 (H1) + 11 (¬H1); O_k > E_k 279, all at crossings; non-tame 235,
    all crossings.
- Labels (both §C.4): PROVED (L-NEW successor 12; REFEREE and REFEREE-2, Opus 5.5, D15): U-loc on every game inside a phase; OE (row 1's
  wording) and OX (i)-(v) on 𝒞^1O. LANDED as RESULTS R28 (Lead, trunk de7a635). OPEN: X and K per phase; G-N5-TIME.
