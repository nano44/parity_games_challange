# L13: exact prefix gadget on rows 0-21 of the level-8 target (BOX L13; L-LOWER successor 12)
Labels: PROVED (lane) / CONJECTURE / DATA / DEAD. Every UNSAT below holds only for its scope: that base genome's wiring and ranks,
with the stated free movers and candidate lists, enc32's model (R104 rules; L-COMP read-only copy experiments/lower/l12/enc32_lcomp.py,
sha1 a8c4f5e3), and the target rows 0..t. No claim about other wirings, ranks or helper sets.

## 0. Question and tools (experiments/lower/l13/)
- Question PG(base, XS, G, t): free wiring on the options of the culprit core movers XS and of the helpers G (G = the top k movers
  64-k..63 of the d 32 base), insertion ranks for those options in the base's fixed order, signs / helper gate bits / helper starts /
  helper states free everywhere, ALL core constraints, the run equal to the target on rows 0..t (no fixed point). Candidates:
  XS options: -1, G, own base targets; G[i] options: -1, G[j > i], own base target, and every mover that reaches no free mover and
  not pair 7 (NOREACH 14, 15, as in L-COMP's gadget.py). Acyclic for every choice.
- Targets: core8 = experiments/lower/l10/out/core8_HIT7.txt (sha1 c6e19673); S8_R2 = experiments/lower/l12/out/S8_R2_core.txt
  (fd5b112c). They agree on rows 0-20 (row 21 differs), so every result with t ≤ 20 holds for both.
- pgad.py (v2) / pgad3.py (v3: XS keep their own base targets unfiltered) generalize L-COMP gadget.py (claude/l-comp
  71670ff9, sha1 07c08c97). scan.sh / scan3.sh: per k, ascending prefixes to the first UNSAT. culprit.sh: single-mover drops.
  pdrup.py: Glucose4 proof + l8/sat/drup.c, then proof and CNF deleted (CNF sha1 kept; the same command regenerates it).
  prefcheck.py: free-run replay with sim6 and fenc (rows followed).
- FINDING (encoder; affects SAT answers only). enc32's insertion-rank mode (--freerank) puts no transitivity constraint on free
  options that share an insertion slot. A model may then carry a cyclic order that decode() cannot realize. Found on C4, k 1, prefix 10:
  SAT, but the decoded genome was rejected by enc32 --fix all at prefix 3, and the sim6 run left the target at row 3. pgad.py adds both
  3-cycle bans for every triple of free options (a sound strengthening). With the bans, the same instance is UNSAT (DRUP VERIFIED).
  UNSATs of the unbanned encoding remain valid, since it is a relaxation. Its SAT answers, including L-COMP gadget.py's, hold only
  after a replay. Every SAT below passed the CHECK (decoded genome, all fixed, same prefix) and, for the frozen ones, sim6 = fenc.
- The k questions are NOT nested. The static reach filter removes candidates (R0 inputs, own targets) as G grows. Example: C4, v2,
  k 3 is UNSAT at prefix 10, while k 2 is SAT at 10. So each k is its own question.

## 1. Results (DATA, exact SAT; unit = core row; base without a gadget: first UNSAT 7 on seed/C4/C10, 1 on SEED_R2, L12 §5)
| base (sha1) | XS | version | k = 1 | k = 2 | k = 3 | k = 4 |
| --- | --- | --- | --- | --- | --- | --- |
| C10 (3ef36801) | 11 (f5) | v2 | 15 | 17 | 17 | 17 |
| C10 | 11, 12 (f5, q6) | v2 / v3 | 7 / 15 | 9 / 17 | — / 17 | |
| C4 (42fef4dd) | 13 (f6) | v2 | 9 | 11 | running | |
| SEED_R2 (bb30e201), target S8_R2 | 12, 13 | v3 | 8 | 8 | 8 | |
Entry = first UNSAT prefix t (rows 0..t-1 realizable). Solve times grow fast at the frontier: C10 X11 at t 17 took 0 / 3 / 92 / 2,407 s for k 1-4.
- DRUP VERIFIED (out/drup.txt): C10 X11 k 1 t 15 (CNF 8da97a4f), k 2 t 17 (e6ab2851), k 3 t 17 (d244dcb2; 845,863 lemmas RUP-checked);
  C4 X13 k 1 t 9 (0d4b5bb6), k 2 t 11 (136b787b). Others: solver only.
- Culprits (single core-mover drops that make the UNSAT SAT; out/culprits.txt): C10 X11 k 1 t 15: {11}; C10 X11 k 2 t 17: {11, 12};
  C10 X11,12 v3 k 2 t 17: {11, 12}; SEED_R2 X12,13 k 2 t 8: {1, 8, 9, 11, 14}. At SEED_R2 the conflict is spread over the lower
  pairs: ROOM_R2's own ranks for pairs 0-5 do not fit, so it is not a start-up hold.
- Frozen partial gadgets (rec/; replay sim6 = fenc, rows followed of BOTH targets): PG_C10_X11_k2_t16_dec.txt sha1 e0a10ff4 (rows 0-16),
  PG_C4_X13_k2_t10_dec.txt sha1 e74892e7 (rows 0-10).
- Structural fact (DATA, C10): every mover of C10 other than f5 reaches f5 (11) through fixed edges, so R0 is empty. Any f5 gadget on
  C10's wiring is an isolated helper system: its members read only each other, and their only outside input is the key gating
  (free iff s ≠ o(l−1)). With k ≤ 4 such helpers, no realization of rows 0..17 exists; the binding pair is f5 / q6 at row 16 → 17.
- Status: no prefix gadget for rows 0-21 at k ≤ 4 (C10), k ≤ 2 (C4), k ≤ 3 (SEED_R2). Step 2 (splice + full-target comparison) has
  not been reached. NOT DEAD: helper sets other than the top k movers are untested.

## 2. Lemma PREF-FUEL and the walls at k = 0, 1 (PROVED, lane; R104 rules, R105 ENC, acyclicity)
- Definition. For a core mover x and target rows 0..P, the required-preference sequence is the list of pairs (t, ns_(t+1)(x)) over
  the steps t < P at which x is FREE. Freedom is read from the target rows and the core gates: level l ≥ 1, s_t(x) ≠ o_(l−1) of
  row t+1; level 0, the gate rule. At a free step, R104 sets ns(x) = pref_x(S_t), so in any realization pref_x(S_t) must equal the
  listed value. R_x(P) = the number of changes between consecutive entries of the list (experiments/lower/l13/reqpref.py).
- Lemma PREF-FUEL. In any genome (any wiring, ranks, signs, gates, starts) whose run realizes target rows 0..P,
  R_x(P) ≤ (number of moves of closure(x) in steps 0..P−1) ≤ 2^|closure(x)| − 1.
- Proof. Take consecutive list entries (t1, a), (t2, b) with a ≠ b. pref_x(S_t1) = a ≠ b = pref_x(S_t2). pref_x depends only on the
  states of closure(x) (x ∉ closure(x); R105), so some closure mover changes between S_t1 and S_t2, i.e. it moves at a step in
  [t1, t2 − 1]. These intervals are disjoint for different changes, which gives the first inequality. FUEL-DOUBLING (L10 §3a)
  orders closure(x) as a DAG y_1..y_k with M(y_i) ≤ 2^(i−1), so the closure moves at most Σ 2^(i−1) = 2^k − 1 times. ∎
- DATA (unit = change; set = the 16 core movers; scope = core8 c6e19673 with C10's core gates, which equal HIT7's on levels 0-6):
  R over the full target = 1, 1, 3, 3, 7, 7, 15, 15, 31, 31, 63, 63, 127, 127, 255, 254 for movers 0..15. Hence:
  COROLLARY (PROVED, lane). Every realization of core8 has |closure(x)| ≥ j + 1 for each mover x of pair j ≤ 6, and ≥ 8 for pair 7.
  This is a universal floor, far below the realized closures (HIT7: 30-32 for the busiest movers, L10 §3a).
- Application to the prefix (f5 = 11 on core8). Its list is (0..5, 0), (6, 1), (13, 1), (14, 0), (20, 0), so R_f5(7) = 1 and
  R_f5(15) = 2. Two consequences:
  - With both of f5's options exiting (C10's own wiring), closure(f5) = ∅ and rows 0..7 are infeasible for ANY other wiring and
    ranks. This explains L-COMP's C10 UNSAT at 7 with the unique culprit f5.
  - With closure(f5) of size 1 (a single isolated helper, e.g. any h whose candidate list holds only exits), rows 0..15 are
    infeasible. This matches the exact sweep (§3).
  Through row 21, R_f5 = 2, so counting allows |closure(f5)| = 2. The plateau at 17 for k = 2-4 is therefore NOT a counting
  obstruction. READING: f5's closure must change at exactly steps 5 → 6 and 13 → 14 (consecutive list entries), and in C10 every
  core mover's chains pass through f5 into the gadget. q6 (R_q6(21) = 5) then sees the gadget's changes, and the exact culprits at
  t 17 are {f5, q6}. This is an interaction of timing, not a fuel bound. Not proved.

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. All statements are about
the IDEAL model's step sequence (R104's definition) on 𝓛^R_d and core target rows. Not M3, not a gauntlet step-4 pass, and not a
TARGET.md claim.
