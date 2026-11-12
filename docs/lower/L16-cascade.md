# L16: a hand-built shared cascade on C12: where the period-8 information comes from, and why grafting it fails (BOX L16; L-LOWER successor 14)
Labels: PROVED (lane) / CONJECTURE / DATA / DEAD. Lead «go» 04:25Z 2026-11-12. Every DATA clause names its counter (unit, set, scope).
Model: R104's IDEAL model at degree ≤ 2 (l6/sim6.py; fenc for replays), facts (M1)-(M5) of L14 §0. Target core8 (l10/out/core8_HIT7.txt,
c6e19673). Base C12 (l14/rec/L14_C12_final_solved.txt, c58041d5). Tools experiments/lower/l16/ (README.md). Instances in l16/run/ (sha1 below).

## 0. The box, and what was run
- Box (Lead, quoted from the brief): «hand-built SHARED cascade on the C12 base (c58041d5), sized by KEY-CLOCK. Target: realize core8 rows 0..P
  for P ≥ 18 (beyond every wall seen: 17 / 14 / 15), milestones P = 18, 21, 24, each replayed (sim6 = fenc) and frozen». Designs in order:
  (D1) graft E_k3_P16_shared onto C12 levels 8-10; (D2) a 4-pair cascade from the relaxed P 32 model; (D3) HIT7_lift_d32's helper cascade.
  «Stop rule: if no hand-built cascade passes P = 18 after D1-D3, write the exact obstruction as the box result.»
- Assumption (D18 «make reasonable assumptions»): a «hand-built» cascade may be designed by an exact SAT question with a fixed frame (which
  slots, which inputs), as long as every design is replayed by independent code before it is cited.

## 1. D1 as specified (DATA)
- Literal graft (l16/graft.py; C12 + E_k3_P16_shared at movers 16-21 → l16/run/C12_E3.txt, 7ef15673). Inside C12 (core clamped to core8) the
  cascade runs exactly as stand-alone (l16/cmpgraft.py; counter = rows 0..20 where the six helper states differ: 0), and it reaches the fixed
  point 011110 by row 13. So the grafted cascade carries no timing past row 16, whatever the clients read. D1 as a clock for P ≥ 18: DEAD
  (instance C12_E3, rows 13..20 constant).
- Free version (l13/pgad3.py on C12, XS = {8, 11, 12, 13}, G = movers 16-21 with free wiring / insertion ranks; 335,822 vars): P 18 NO ANSWER in
  2,900 s (CaDiCaL); P 15 stopped after ~30 min without answer. Not decided.
- Clients only, free to read ANY mover compatible with an order (l16/pgad5.py, XORD 8 < 11 < 13 < 12; signs / gates / starts free as in pgad):
  P 14 SAT in 807 s, decoded genome l16/run/X5_P14_dec.txt (f002cc9f), CHECK consistent, replay: sim6 = fenc, rows 0..14 followed (l13/prefcheck.py).
  P 18 NO ANSWER in 2,900 s (608,664 vars). In X5 the run leaves the target at row 15 at f5 (11) and f6 (13) (l16/diag.py): both tight changes
  at pre-state 14.

## 2. Where the period-8 information must come from
- Lemma CLUSTER-SINK (PROVED, lane; M1). Let C = {12, 13, 14, 15} (pairs 6-7). In every genome (any wiring, acyclic Ξ-graph) some b ∈ C reaches
  no other member of C, so better_b is a function of the states of movers outside C (M2).
  Proof. Reachability restricted to C is a strict partial order (acyclicity); a minimal element reaches no other member. ∎
- DATA (exact, from the frozen wirings; counter = Ξ-reach): in C12 and in X5 the minimal member is f6 (13): q6, q7 and f7 all reach 13. Every
  helper of C12 whose trajectory has period 8 (18, 22, 24: 9-10 moves on rows 0..40 of the clamped run) reaches 13 as well; the period-8 signal
  that q6 / pair 7 read in C12 is f6's own, relayed. f6 itself has no period-8 source.
- DATA (exact; l13/reqpref.py on core8, C12's core gates; counter = free pre-states of f6 on rows 0..510): f6's required preference equals
  XNOR(s10, s11) (q5, f5: pair 5) at 128 of its 129 free pre-states; the exception is pre-state 2 (required 0). Pair 5 sampled at f6's free
  rows runs the Gray cycle 00, 01, 11, 10 (period 16), so f6 is the next counter bit of pair 5, as a binary counter requires.
- READING (not proved). An ENC better function (top-ranked option of the symmetric difference of two chains) does not compute the XOR of two
  movers' states by routing alone: a router mover that gates whose option enters which chain has its OWN state set by what it routes to, so it
  cannot both track s10 and route s11's option into opposite chains. The exact form of this for the C12 chains is the k = 0 line of §3 (UNSAT).

## 3. The cascade f6 needs: one pair, if it may read the slow core pairs (DATA, exact SAT + independent replay)
- Tool l16/ekr2.py (EXACT, extends l15/ekr.py): a private cascade of k pairs on levels L..L+k−1 (degree-2 wiring, free ranks, parities, gate
  bits, starts; clock = the base's o(L−1) on the clamped run, = t mod 2 at L = 8), PLUS external inputs EXT: core / helper movers of the base
  whose chain at row t is the FIXED option set of the base's clamped run, with the base's ranks and signs; cascade and client options get
  free insertion ranks among them. The client (f6) is modelled exactly: its better by ENC must equal its required value at every free
  pre-state ≤ P (not mere separation). Replay l16/sim2.py: independent code (integer ENC values, own chain walk, own movement).
- Results (client f6 = 13; counter = free pre-states of f6 matched, all of them in every SAT line; every SAT replayed by sim2 with 0 mismatches):
  | base | slot level L | EXT | k | P: result |
  | --- | --- | --- | --- | --- |
  | C12 | 8 | 0-11 | 0 | 32: UNSAT |
  | C12 | 8 | 10, 11 | 1 | 16 SAT, 20 SAT; 24, 28, 32 UNSAT |
  | C12 | 8 | 0-11 | 1 | 32, 48, 64, 128, 256 SAT; 510 SAT (937 s; l16/run/ekr2_f6_k1_P510_e0-11.txt, 4fee0495) |
  | C12 | 8 | 0-11, KEEPO (o(8) as in C12) | 1 | 32: UNSAT |
  | C12 | 13 | 37 movers not reaching 13 / slots, KEEPO | 1 | 16, 32 SAT |
  | X5 | 8 | 0-11 (also 34 movers, KEEPO) | 1 | 32: UNSAT |
  | X5 | 13 | 37 movers, KEEPO | 1 | 18 SAT (l16/run/X5_f6_L13_k1_P18.txt, a9f803fd); 20, 22, 24 UNSAT |
- The P 510 design (DATA): cascade movers y0, y1 on level 8; y0's options → q4 (8), y1; y1's options → f4 (9), q2 (5); f6's options → y0, q5 (10);
  gates 0 0. f6 thus reads pair 5 and pair 4 / pair 2 through their fixed chains (which pass C12 helpers 41, 36, 23, 28, 29, …) plus one pair
  driven by the parity clock.
- KEY-CLOCK, exactly (Lead 06:44Z asked for the statement before and after).
  BEFORE (L15 §4, verbatim): «CONJECTURE KEY-CLOCK: a private cascade must have ≥ log2(P) − c pairs to separate a client with a tight change
  near row P.» «Private» there means L15 §0: Ξ-edges only inside H, input = the key cascade, at its lowest level o(7) = t mod 2. The box brief
  used it as a SIZE for the shared cascade («sized by KEY-CLOCK (≈ log2 P − c pairs)»), i.e. read it for cascades that may also read the core.
  AFTER: (i) CONJECTURE KEY-CLOCK (isolated), scope narrowed to exactly L15 §0's private cascades: unchanged, still a CONJECTURE (DATA P ≤ 32,
  L15 §3), not touched by §3 here. (ii) The non-isolated reading «every cascade that serves a client with a tight change near row P has
  ≥ log2(P) − c pairs, also when its movers and the client may read core movers» is DEAD in the ekr2 scope: instance ekr2_f6_k1_P510_e0-11.txt
  (4fee0495), ONE pair, client f6 with a tight change at every 4th row up to P = 510 (R = 127), C12's fixed chains of movers 0-11 as inputs,
  replayed (sim2, 0 mismatches of 129). Scope of the DEAD: the base's chains are held fixed (the graft's own effect on keys and readers above
  level 8 is NOT modelled; §4 is exactly that effect). So the count of pairs is not the binding cost; the coupling of §4 is.

## 4. Why the design does not graft: the slots are read by the cluster (DATA, exact)
- Graft (l16/graft2.py) of the X5 design into X5 at level 13 → l16/run/G1.txt (2a2ab451). Free run (sim6): the core leaves the target at row 2
  (f5); at row 1 already movers 24, 45-49, 51 differ from X5's run (counter = movers whose state differs from X5's free run, rows 0..3:
  0, 7, 7, 12). Cause: rewiring f6 changes the chain values seen by every mover whose chain enters f6's options, and the cascade slots are
  entered by other movers' chains too.
- Indirect readers (counter = movers whose Ξ-reach contains a slot mover; set = all 64; scope = the X5 and C12 wirings; l16/out/readers_X5.txt, readers_C12.txt): every level whose key moves
  in the clamped run (8-25) is reached by 16-62 movers, always including q6, q7, f7 (12, 14, 15); the two levels reached by ≤ 1 mover (26, 31)
  have constant keys o(25), o(30) on rows ≥ 3, so a cascade there moves at most once per mover (M3).
- Keeping every such reader's base better (ekr2 KEEPR) is UNSAT already at P 14, even with f6 forced to its base wiring (FORCEBASE; solver
  only, a diagnostic): the kept readers' chains run through helper 50 into slots 26 / 27, whose base chains (targets 38, 5, 32, 18) the cascade
  cannot reproduce. UNSAT core (DEBUGCORE) over (reader, row): readers 12, 14, 15, 19, 21, 24, rows 0-11.
- Re-solving the readers instead (exact; pgad4 on G1, cascade signs / gates / starts fixed, XS = {12, 14, 15} with pgad's candidates):
  UNSAT at P 15 and at P 18 (CaDiCaL, 53 s each; diagnostics, not cited as lemmas). pgad5 on G1 with XS = {8, 11, 12, 14, 15} free to read
  any mover compatible with 8 < 11 < 12 < 15 < 14 (cascade signs / gates / starts fixed): P 18 NO ANSWER in 2,900 s (1,008,873 vars).

## 5. D2 / D3 as coupling checks (Lead 06:44Z: «run D2 and D3 only as quick coupling checks, at most one capped run each … Run D2/D3 in
full only if a quick check shows a level whose movers are read by fewer than about 4 cluster readers.»)
- Reader sets per helper level (l16/readers.py; out/readers_C12.txt, out/readers_X5.txt). Counter: R(L) = movers r not on level L whose Ξ-reach
  contains a mover of level L (set = all 64 movers; scope = the frozen wiring); cluster readers = R(L) ∩ {12, 13, 14, 15}; key activity =
  changes of o(L−1) on rows 0..40 of the clamped run (core forced to core8).
  C12 (c58041d5): levels 8-14 and 16-18 (keys with 3-40 changes): |R| 13-50, cluster readers ⊇ {12, 14, 15} except level 15 ({14, 15},
  |R| 13, 9 key changes); levels 19, 26, 31 (|R| 1, no cluster reader) have 0-2 key changes; 28 and 30 (cluster reader 12 only) have 0.
  X5 (f002cc9f): every level 8-30 with a moving key has ⊇ {12, 14, 15} among its readers; levels 26, 31 (|R| 1) have 2 and 0 key changes.
- D2 (a 4-pair cascade, levels 8-11) and D3 (HIT7_lift_d32's helper block, levels 7-27) occupy only levels with cluster readers ⊇ {12, 14, 15}
  (both bases), so the criterion for a full run is not met for either. The one level below the threshold (C12 level 15) got the one capped
  run: ekr2 LEVEL 15, k 1, KEEPO, KEEPR (all 26 readers of f6 or of the slots keep their base better), P 18: UNSAT in 7.3 s (solver only;
  diagnostic). UNSAT core over (reader, row): f7 (15) rows 4, 7, 8; helper 49 rows 5-8; helper 53 row 9; f7 and 49 read the slots 30 / 31
  directly. D2, D3: not run in full (criterion not met); recorded as SKIPPED with this reason, not as DEAD.

## 6. Box result (stop rule): the coupling obstruction (DATA, exact; no hand-built cascade passed P = 18)
- Milestone P = 18: NOT reached. Best realized prefix of the box: rows 0..14 (X5_P14_dec f002cc9f, sim6 = fenc). Undecided at P 18 within
  2,900 s: D1 free (levels 8-10), clients-only (pgad5), G1 completion (pgad5 with the cascade fixed).
- The obstruction, exactly. (a) Information: the cluster sink f6 needs XNOR(s10, s11) (§2), which ENC on the core's fixed chains does not
  supply (k 0 UNSAT, DRUP VERIFIED) and ONE fresh pair does, to T 510 (§3, replayed). (b) Coupling: a fresh pair must sit on a level whose key
  moves; on C12 and X5 every such level is reached through Ξ chains by at least two of q6 / q7 / f7, and by 13-62 movers in all (§5, counter
  stated there). (c) Consequence, measured: grafting the P 18 design for f6 (X5 level 13) changes those readers' chain values: instance
  G1 (2a2ab451) drifts at row 1 (movers 24, 45-49, 51) and leaves the target at row 2 (f5); keeping every reader's base better is UNSAT at
  P 14 even with f6 at its base wiring (KEEPR + FORCEBASE; UNSAT core readers 12, 14, 15, 19, 21, 24, rows 0-11); at C12 level 15 it is
  UNSAT at P 18 (core f7, 49, 53). Re-solving the readers instead (G1, pgad5) gave no answer at P 18 in 2,900 s.
- What is NOT claimed. No lower bound: the KEEPR frame is a sufficient condition (readers may change if they still meet the target), and the
  re-solving questions are undecided, not UNSAT. Nothing here bounds N5 on any game. The obstruction is about the C12 / X5 wirings; a base
  built with the cascade from the start (readers designed around it) is not excluded.
- Cited UNSATs and their DRUP (l16/out/edrup.txt; Glucose4 proof + l8/sat/drup.c, s VERIFIED each): C12 k 0 EXT 0-11 P 32 (CNF 713a8028);
  C12 k 1 EXT {10, 11} P 24 (36ed96fc); C12 k 1 EXT 0-11 KEEPO P 32 (c8bac5f4); X5 level 13 k 1 KEEPO P 20 (ccccdfbb). The KEEPR, pgad4 and
  level-15 UNSATs are solver-only diagnostics and are labelled so.
- Labels: PROVED (lane): CLUSTER-SINK. DATA: §1-§6 tables, each with its counter. DEAD: D1's grafted E_k3 cascade as a clock past row 16
  (C12_E3, 7ef15673); the non-isolated reading of KEY-CLOCK in the ekr2 scope (4fee0495). CONJECTURE: KEY-CLOCK (isolated) unchanged.
  READING: ENC routing does not compute XOR (§2).
- Proposed next step (not a decision): build the base AROUND the cascade: freeze the f6 design + its pair first, then let the annealer /
  pgad choose the readers' wiring (q6 / q7 / f7 read f6, not the slots), i.e. move the coupling into the search frame instead of grafting.

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. All statements are about the IDEAL
model's step sequence (R104's definition) on degree-≤-2 genomes and core8's rows. Not M3, not a gauntlet step-4 pass, not a TARGET.md claim.
