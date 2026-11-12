# L18: f6's full-horizon correctness inside the search (BOX L18; L-LOWER successor 15)
Labels: PROVED (lane) / CONJECTURE / DATA / DEAD. Lead approval 16:09Z 2026-11-12; re-aim and frame L18b 19:57Z. Every DATA clause names its
counter (unit, set, scope). Model: R104's IDEAL model at degree ≤ 2 (sim6; fenc for replays). Target core8 (c6e19673). Tools experiments/lower/l18/.

## 0. The box and what a result would mean
- Box (Lead 16:09Z, quoted): «pgad5 with f6's clamped-run constraints over the full horizon (rows 0..510) inside the search, and q6 among
  the free clients from the start». Re-aim (Lead 19:57Z, quoted): «The target is the largest P with f6 correct over the WHOLE horizon (all
  129 free pre-states, rows 0..510). That, not a long prefix with f6 broken, is what a lower-bound construction needs.» Frame change, quoted:
  «FRAME L18b = L18 + q5 free».
- A design that follows core8 rows 0..P with f6 correct on all 129 free pre-states is DATA: one more realized prefix in the IDEAL model with
  the cluster sink served over the whole horizon. It is NOT a lower bound for N5, NOT the level-8 tower (rows 0..510 are needed for that),
  and says nothing about N5 on games (L17 §0 applies unchanged).

## 1. Tools (experiments/lower/l18/README.md)
- enc32c.py: copy of the read-only enc32 (sha1 a8c4f5e3) with CLAMP_FROM / CLAMP_KEEP: on transitions t ≥ P only f6's constraint is kept
  and the core is forced to core8 (= the clamped run of l16/f6check.py) with the same design variables. Validation (ccheck.py, design fixed):
  A3x5_P15 (f6check first mismatch at row 18) prefix 15: SAT at R 17, 18; UNSAT at R 19, 20. A2_solved prefix 6: SAT at R 64 and R 510.
- pgad6.py: l16/pgad5.py on enc32c with horizon F6R = R. Soundness of horizon refinement: UNSAT at R implies UNSAT at 510 (the R 510
  question only adds constraints); every SAT is checked by f6check on rows 0..510 anyway.
- Size (DATA; unit clauses; frame L18, P 13): ≈ 163k per clamped row (R 64: 11.5M clauses, 1.6 GB); the full frame at R 510 (≈ 85M) does
  not fit. Base-neighbourhood form (n.sh: BASE = a design, few clients free, other ranks fixed at build): R 510 = 50M clauses, 5.3 GB, fits.
- Search aids. Phase hints (PHASE, PHASESTATES) are NOT followed by CaDiCaL here (A2_solved's design phased: 524 s; as assumptions: 0.2 s).
  LNS (assume a hint's design except chosen movers) is used instead: a SAT is a real design (decoded, CHECKed, replayed); an UNSAT is
  «this neighbourhood only», never a frame verdict.
- inframe.py checks a design lies in the frame relative to A2_solved (wiring differs only on clients' options; other options keep their
  relative rank order; f6 pair signs / gate / starts and core gates unchanged). run/inframe.txt: every decode OK.

## 2. Frame L18 (XS 8, 11, 12, 14, 15; XORD 8 < 11 < 12 < 15 < 14; FIXC 16, 17; base A2_solved)
- Full questions: P 13 R 32 (two hints): no answer 2,900 s each; P 10 R 64, P 7 R 130: no answer 2,900 s. P 7 R 64: SAT 384 s
  (P7R64_dec 187aba91, rows 0..7, f6 first wrong at row 122, 44 / 129).
- LNS: P 7 R 130 SAT (H7 350449ba, f6 to row 137); P 8 R 64 SAT (C8 3b86b22a, rows 0..8, f6 first wrong 114); P 9: 3 + 1 neighbourhoods
  LNS-UNSAT or no answer. Largest P with f6 globally correct in L18: 6 (A2_solved itself).
- Drift (DATA, run/pairsilence.txt; counter = changes of the f6 pair (16, 17) in the clamped run): in every L18 design with P ≥ 7 the pair
  changes on a 16-row rhythm, then falls silent from row 102 / 118 / 134 to 289, and f6 goes wrong 4-12 rows after the silence starts.
  f6's chains pass through rewired clients (drift.py: 11 via 28 → 32 in P7R64). A2_solved does not use the pair (1 change) and is correct.

## 3. Frame L18b (L18 + q5 = mover 10 free; XORD 8 < 11 < 10 < 12 < 15 < 14)
- LNS: P 9 R 64 SAT (L18b_C9 9c5767d5, rows 0..10, f6 18 / 129 first 122); P 7 R 256 SAT (L18b_H7 6e363295, f6 15 / 129, first 394; pair
  last change 390). P 11 around L18b_C9: 3 neighbourhoods LNS-UNSAT → the f6-broken climb stops at P 11 (stop rule of 19:57Z).
- Full-horizon designs (base-neighbourhood questions at R 510; all replayed sim6 = fenc, f6check 0 / 129 on rows 0..510, inframe OK):
  | P asked | base | clients free | result | design (sha1) | rows followed |
  | 7 | L18b_H7 | 10, 11 | SAT 929 s | L18b_N510 13ea6547 | 0..8 |
  | 9 | L18b_N510 | 10, 12 | SAT 1,443 s | L18b_N9a 5b634aac | 0..9 |
  | 10 | L18b_N9a | 10, 14 | SAT 2,514 s | L18b_N10a d3b6e342 | 0..10 |
  | 11 | L18b_N10a | 15 | SAT 1,109 s (wall 1,213, cap 6,000) | L18b_N11a a6e0185b | 0..11 |
  DATA (unit = core8 rows followed by the free run, counter f6 = 129 free pre-states of rows 0..510, scope frame L18b on A2_solved):
  largest P with f6 globally correct = 10 (L18b_N10a); 11 after §4 (L18b_N11a). The pair keeps moving to row 505 in L18b_N510 (65 changes): the «silence» of §2 was a
  property of those designs, not of the frame.
- Climb continues (§4 log).

## 4. Climb log (base-neighbourhood questions at R 510; one job at a time, 13 GB cap)
- P 10: base L18b_N9a, clients 10, 14 (diag at row 10: movers 10, 13, 14): SAT 2,514 s (close to the 2,900 s cap; solve times 929 →
  1,443 → 2,514 s for P 7 → 9 → 10). Next: P 11 on base L18b_N10a with the movers diag names at row 11 (successor 16).
- P 11 (successor 16): base L18b_N10a, client 15 alone (diag at row 11: mover 15 only, «better» says stay): SAT, solve 1,109 s (cap 6,000 s, wall 1,213 s, 63.3M clauses;
  RSS 7.9 GB seen at 16 min) → L18b_N11a a6e0185b (run/SHA1SUMS): rows 0..11, sim6 = fenc, f6check 0 / 129 on rows 0..510, inframe OK. One free client
  solves faster than two (2,514 s at P 10 with clients 10, 14). diag at row 12: mover 14 only. Next: P 12, client 14.

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. All statements are about the IDEAL
model's step sequence on degree-≤-2 genomes and core8's rows. Not M3, not a gauntlet step-4 pass, not a TARGET.md claim.
