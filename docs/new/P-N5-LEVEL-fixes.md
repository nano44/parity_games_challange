# P-N5-LEVEL fixes (append-only; the packet docs/new/P-N5-LEVEL.md stays frozen at l-new 1e6df499, sha1 7c956df443cfddbf23bfbaa18a26a98369b176ec)

## Fixes entry 1 (L-NEW successor 74; written 2026-11-12 23:24Z by date -u; LINE-ONLY: no statement, proof, bound or label of the packet changes)
Both referees SIGN every statement of the packet (§3-§8): REFEREE 34 (first review, claude/referee 4c8d6c4f, docs/referee/R-P-N5-LEVEL.md,
file sha1 374a1ba06f845ab9376f78b5ef82d24a3e4d2fc5, §0) and REFEREE-2 39 (second review, claude/referee-2 43824abc,
docs/referee-2/R2-P-N5-LEVEL.md, file sha1 77a38f1ae36c32aed245fdd0a1bb0777ec9690fb, §5.5). Both ask for changes to the proposed line
L-1 only. The Lead's ruling (2026-11-12 21:43Z, by message; quoted, elisions marked «…»): «REQUIRED: - REFEREE-2 39 R-1 … ALL-TCYC's Consequences in the line.
This is the same point as REFEREE 34's LO-2, so use R-1's exact string. - REFEREE 34 LT-1, LT-2, LT-3 … ADOPTED optional items: REFEREE-2
R-2 (NO-TIE and LOC-GATE in (K4); DOM with CN2 in (K5) and PLATEAU's H0), and REFEREE 34 LO-1 (rv208's counter names). NOTES: REFEREE-2's
N-1..N-3 and REFEREE 34's N-L1 go into the fixes entry as recorded notes, with no line change.»
### Line items applied (line L-2 = docs/new/P-N5-LEVEL-line-L2.txt, written by experiments/new/box211/mkl2_211.py, output mkl2_211.out)
Every old and new string is EXTRACTED by the script from the two reports at the pinned commits (both reports' rule: one space wherever the
report wraps a line inside a string); none is retyped here or in the script. Order: LT-1, LT-2, LT-3, then R-1, R-2, LO-1.
| item | referee, place | what it changes in the line | ruling |
| --- | --- | --- | --- |
| LT-1 | REFEREE 34 §5 (L43, §4 item 5) | the «no run tests the constants» clause names instance, tool, unit and file | REQUIRED |
| LT-2 | REFEREE 34 §5 (L43, §4 item 4) | the G_N counter is named k5, with L-COMP BOX 43 README item 1 (b) | REQUIRED |
| LT-3 | REFEREE 34 §5 (§7) | the Lean citation form (PG.-names, «Lean-checked (lane) … not through CHECKER», f74d38a4) | REQUIRED |
| R-1 | REFEREE-2 39 §5.4 (= REFEREE 34 LO-2) | ALL-TCYC's «Consequences»: R, Q and D^tot(v) − 1 within the same bound | REQUIRED |
| R-2 | REFEREE-2 39 §5.4 | the premise sentence names NO-TIE and LOC-GATE in (K4), DOM with CN2 in PLATEAU's H0 | ADOPTED (optional) |
| LO-1 | REFEREE 34 §5 | «the 49 must-0 counters of rv208.py» says where they are named | ADOPTED (optional) |
- Byte checks printed by mkl2_211.py: L-1 sha1 28565b3c60fe8167f4b660c83fa27c00cd7b4fe9 asserted; after LT-1..LT-3 the line has sha1
  389645a2a646522a8fb57f05dba4458695ac74f2 (7,706 B), equal to REFEREE 34's reported L-1′ (§5) and asserted; after R-1, R-2, LO-1:
  L-2 sha1 d18125ed1c62f8ad20396d9f94eac8bdbc624cf4, 7,970 B, one line, no «|», 93 «(» = 93 «)», each new string exactly once.
- For LT-3, as the Lead ruled: the line cites the Lean commit the packet cites (f74d38a4), not later L-FORMAL commits.
### Notes recorded (no line change; no statement changes)
- REFEREE-2 39 N-1 (§1.1): (K1)'s Λ half also follows from F1 with (VJ-1); REFEREE-2 signs (K1) on either route. The packet keeps
  R118 (e)'s reason (and the line keeps «use neither PLATEAU nor F1», which is true of the packet's proofs as frozen).
- REFEREE-2 39 N-2 (§1.3): the packet's «(K4) is stated there (K4Statement) and NOT proved in Lean» and §12's «NOT formalized» list are
  true at f74d38a4, the commit they name, and stale at later L-FORMAL commits (REFEREE-2's Addendum 1, claude/referee-2 3cf594cc,
  measures them at l-formal 78c32d90). The packet stays as frozen; its Lean sentences are read as dated to f74d38a4.
- REFEREE-2 39 N-3 (§5.2): §9's list of genome-only steps omits (D3) / LOC-K2 inside (K2), CN2 / (D4) in (L3) and CN2 in (P7)'s H0;
  REFEREE-2's full list of 14 steps is its §5.2. §9 is READING, not to sign; the list is read as REFEREE-2's.
- REFEREE 34's notes N-1..N-5 (§0, «Notes (no change asked)»: N-1 (K3 c), N-2 (H's priorities), N-3 (§8's N ≤ M), N-4 (class order),
  N-5 (Lean names in the body)). The Lead's message names «REFEREE 34's N-L1»; no item of that name is in R-P-N5-LEVEL.md at 4c8d6c4f
  or at claude/referee 99df2458, so this entry records the report's notes N-1..N-5 under that heading (Lead to correct if another
  item was meant). REFEREE 34's Erratum (22:12Z, typed timestamps in its header) changes no content.
### Pins and checks
- box211/level.pins gains this file, L-2, mkl2_211.py and mkl2_211.out; experiments/new/check.sh's «P-N5-LEVEL» block checks that
  L-2 is pinned and that mkl2_211.out ends with L-2's sha1. mkl2_211.py itself needs the referees' git objects and is not run by check.sh
  (it is re-run by hand: `git fetch origin claude/referee claude/referee-2; python3 experiments/new/box211/mkl2_211.py`).
