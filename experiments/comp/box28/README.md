# L-COMP box 28: T^R(4), machine-certified (target: T^R(4) = 13; packet P-TR4 in the P-TR3 format)
L-COMP successor 10, 2026-11-07 (date -u in the commits). Lead brief BOX 28. Labels: CERTIFIED (solver UNSAT + Glucose 4 DRUP proof
accepted by box27/drup.c), EXACT-SAT (solver UNSAT, no checked proof), DATA, CONJECTURE. Model: IDEAL (RESULTS R104, definition
only), 𝓛^R_d of RESULTS R110 (definition only). Not a TARGET.md claim. G-N5-TIME stays OPEN.

## Pipeline = P-TR3's (box27), unchanged code
- Encoder: box27/cnf.py as it stands (sha1 f1f803ae8837822ad3e305ad577957a309f511e7, last changed at 81ed3900), called with d = 4; no
  line changed in box 28. R112 cites it at 557b045b (sha1 fd882af1…); the later edits add only env-gated options (FREE0, ISO, KF, RUN2,
  XCUBE), all off here, and the current file reproduces the P-TR3 d 3 L 9 cube 0 DIMACS byte for byte (sha1 7e70b9e1…, re-measured
  2026-11-07).
- Changes from d = 3 (parameters only): d = 4 (8 movers, levels 0-3, 16 options); L = 14; root cubes fix s_0 of movers 2..7
  (2^6 = 64 roots, cube c sets s_0(2 + i) = bit i of c) on top of SYM (s_0(0) = s_0(1) = 0), exactly the P-TR3 cover with d = 4.
- Size (d 4, SYM + one root cube): L 13: 254,071 vars, 902,936 clauses; L 14: 273,590 vars, 972,056 clauses, 2,376,280 literals
  (d 3 L 9: 58,896 / 204,036).
## Read-back on the known witness
- ext/max_d4_L13.json = claude/vibrant-johnson-nxvvxo experiments/new/box156/ext/max_d4_L13.json (L-RED R197; sha1 f0735b61…,
  same file as box160/ext). pinwit.py (box27/pinck.py's pinned_sat, unchanged): sim T 13 (stop: stuck); pinned CNF SAT at L = 13,
  UNSAT at L = 14 (log/pinwit_max_d4_L13.out).
- symwit.py (the witness under SYM): options of movers 0 and 1 relabelled (both started on option 1; P-TR3 §2 relabelling), start
  [0,0,0,0,0,1,0,1], sim T 13 unchanged; pinned in the SYM=1 + root-cube-40 CNF: SAT at L 13, UNSAT at L 14; pinned in root 41:
  UNSAT at L 13 (log/symwit_max_d4_L13.out).
- mkdimacs.py writes one root cube's DIMACS (same text as box27/mkproof.py; no get_proof()); d 4 L 14 cube 0 sha1 2a07a8e9….
