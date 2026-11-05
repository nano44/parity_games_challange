# L-COMP box 27: an independent exact source for the IDEAL ladder numbers (T^R(d)), the external-flip table T_k(m), and the padded class T*(d)
L-COMP successor 9, 2026-11-05 (date -u in the commits). Lead brief BOX 27. Labels: EXACT-BF (exhaustive enumeration in C, my code),
EXACT-SAT (my own CNF, CaDiCaL 1.9.5 via pysat; no proof certificate is checked), DATA, READING. Model: the IDEAL model of
RESULTS R104 (definition only), acyclic Ξ-graphs. Not a TARGET.md claim. No polynomial bound. G-N5-TIME stays OPEN.

## Independence
- sim.py: my simulator, written from R104's text (Ξ-values compared as β-SETS by the largest rank in the symmetric difference;
  R105's ENC is NOT used anywhere in this box). Keys: literal gate tuples along W-chains, lowest level first, under the new state.
- bf2.c, bfk.c: exhaustive C enumerations (my code; literal set comparison, literal key tuples, every in-level gate order).
- cnf.py: my own CNF encoding (chains unrolled hop by hop, comparison = "largest-rank β of the symmetric difference" over a strict
  rank order, keys = recursive lexicographic comparison, every gate order a strict total order per level). No L-RED / L-NEW
  encoder code was read for it beyond the FREE0 / ISO side-condition definitions in L-NEW box160/iso.py (semantics only).
- Second simulator for replays: L-RED's r187/ideal.py (claude/l-red 6f347876, read-only, from git archive in a scratch dir).
- xcheck.py: sim.py = ideal.py on 198,085 runs (290 acyclic genome files of claude/l-red 6f347876 + claude/l-new box150/box160 with
  every start when N <= 10, the stored start otherwise; 3 Ξ-cyclic files skipped; 3,000 random acyclic genomes, width 1-3, d 1-5,
  0-3 degree-1 movers): 0 mismatches (out: xcheck.out).

## (a) T^R(d) (R197 2-wide degree-2 ladders, no padding; option k of a level-l >= 1 mover W-points to mover 2(l-1)+k)
| d | method | result |
| --- | --- | --- |
| 2 | EXACT-BF bf2.c: 5,941 acyclic Ξ-graphs x 8! rank orders x 2^8 parities x 24 x 24 in-level gate orders x 16 starts | max T = 4 (no run longer; histogram in out/bf2_part*.txt) |
| 2 | EXACT-SAT cnf.py | T >= 4 SAT, T >= 5 UNSAT (1.5 s) |
| 3 | EXACT-SAT cnf.py | T >= 8 SAT (205 s; out/R_d3_L8.json, replay OK under sim.py and ideal.py); T >= 9: see below |
| 4 | EXACT-SAT cnf.py (cubes) | running |
- bf2 notes: the 576 gate-order pairs give only 24 distinct transition functions (top-level gates never decide: the two options of a
  top mover W-point to different movers). Witnesses out/bf2_wit0-3.json replay to T = 4 under both simulators.

## (b1) External flips T_k(m) (L-NEW box 160 FREE0 + ISO: level 0 set from outside, b_0 = [key(u_0) < key(v_0)] changes <= k times over
s_0..s_T, every Ξ-target an upper mover or the exit, every step moves an upper mover, T counts steps), EXACT-BF bfk.c
| k | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | unlimited |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_k(1) | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| T_k(2) | 4 | 5 | 7 | 8 | 8 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
- Enumerated: every acyclic ISO Ξ-graph (7 for m 1; 5,941 for m 2), every rank order, every parity vector, every in-level gate order of
  every level (incl. level 0 and the top), every start, every level-0 schedule (longest-path DP over (state, flips left); no cycle in
  any transition graph, so "unlimited" (UNB=1: flips free) is a finite maximum).
- Agrees with L-NEW box 160 on every value it has (k 0-4 and k 8 for m 2; FLIP-1's 2, 3, 3, ... for m 1). New: T_5(2) = 8, T_6(2) = 9,
  and T_k(2) = 9 for EVERY k >= 6 (unlimited flips give 9). So T_k(2) does not grow slowly: it saturates at 9 = 2·T^R(2) + 1.
- Replay: free0.py (python, sim.py's rules, own DP over level-0 schedules) recomputes T_k for the C witness genomes: equal for every
  k checked (0, 1, 2, 3, 5, 6, 12 at m 2; 1 at m 1).

## (b2) Padded class T*(d) (P-IDEAL-SLOT's 𝓛_d: free W-targets one level down, degree-1 movers allowed)
- cnf.py W=free P=p0,p1,...: p_l degree-1 movers at level l (never move; W-target any mover one level down; Ξ-target any mover).
| d | class | result |
| --- | --- | --- |
| 2 | W free, no padding | T >= 5 UNSAT (3.1 s) |
| 2 | W free, 1 + 1 padding | running |
| 2 | W free, 2 + 2 padding | running |
