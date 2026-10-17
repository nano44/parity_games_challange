# R18: (LEX) and (NR) are FALSE on A_DTL (L-RED successor 3, 16:25Z by date -u; produced on Opus 5.5)
Targets: L-ALG successor 4's candidates, relayed by the Lead 16:16Z (tool experiments/alg/dtl_plateau.py not yet read;
my statement is the Lead's relay). Fix a phase (player p, no dominion between) and a depth-0 context R; consecutive
best_vertices calls at R, searches s < s'. d(v) = ACTUAL death round of each p-parity v in R (INF if in the stable result);
vertices ordered by index, priority-major.
(LEX): if d_s != d_s', the highest-index changed vertex v* has d_s'(v*) > d_s(v*).
(NR): a vertex that has FALLEN at a context is never again the top changed vertex there.
(LEX-R): at the first differing round r0, V_r0 grows strictly.

## 1. Tool
experiments/red/carry/lex.py (L-ALG's dtl_regvec.py read-only via LALG_DIR, l-alg d2ae597; order from DTL_ORDER; index =
L-ALG's internal id, priority-major). Nesting level of a step = 0 if its top vertex never fell at this context before, else
1 + the level of the step that last knocked it down. Seed check: on the 20 deficit games (L-ALG instances/h4_*, my h4_*,
lemmaS_*, cm_mdrop_*) 0 (LEX) and 0 (NR) violations in both orders, matching L-ALG's data. Climb dtl_search --fitness lex
(seed 601, Oink order, from cm_mdrop_both_n28) found the instance below in about 3 minutes.

## 2. FINDING: counterexample with INJECTIVE priorities, both orders (experiments/red/carry/instances/lex_viol_inj_n28.pg)
n = 28, sha1 6868a699, priorities injective (so Oink's order and the stable order index the vertices identically).
Pinned Oink: 1 dominion, 23 tangles, 8 iterations, solution verified (13 strategies); dtl_pyref 8 searches; lex.py gives
the same in DTL_ORDER=oink and stable: 6 (LEX) violations, 7 (NR) violations, max level 1 (7 contexts |R| 28..22).
Player 1 (Odd), context R = G (|R| 28). Deaths of the changed vertices, original id/priority: before -> after, top first:
| step | ideal | changed deaths (top first) |
|---|---|---|
| s4 -> s5 | moved | 2/43: 6->8, 18/39: 3->5, 7/35: 4->6, ... (all rise) |
| s5 -> s6 | SAME (DEF step) | **2/43: 8->7**, 20/41: 3->6, 18/39: 5->6, 7/35: 6->7, 13/31: 7->6, 14/29: 7->5, 10/25: 11->10, 6/21: 13->12, 4/19: 12->11, 12/11: 10->9, 26/7: 6->4, 27/5: 9->8 |
| s6 -> s7 | SAME | **2/43: 7->9** (top again: NR level 1), 20/41: 6->7, 18/39: 6->7, ... (all rise) |
| s7 -> s8 | SAME | 2/43: 9->INF, ... (actual becomes stable) |
- (LEX) fails at s5 -> s6: the top changed vertex (2, the highest Odd priority 43) FALLS 8 -> 7 while 20 (41) and 18 (39)
  rise. The vector read top-down drops lexicographically.
- (NR) fails at s6 -> s7: vertex 2, knocked down at s5 -> s6, is again the top changed vertex, and rises.
- (LEX-R) HOLDS on this instance: V_r0 grows strictly at every step (r0 = 2, 3, 3, 6, 7). At s5 -> s6, round 3 gains
  vertex 20, and that makes the top vertex 2 die a round EARLIER. So the strict growth of V_r0 does not give (LEX).

## 3. The same with priority ties, Oink order only (experiments/red/carry/instances/lex_viol_tie_n28.pg)
sha1 0cb8bde4; the climb's raw output. Vertices 2, 18 and 20 share priority 23. Oink's std::sort reindexing puts 2 above 20,
so in Oink order the violation is the one in section 2; in the stable order (20 above 2) the top changed vertex is 20, which
rises, and lex.py finds 0 violations. carry/injective.py (new) rewrites priorities injectively in a chosen tie order,
parity kept; with Oink's tie order the violation survives in both orders (section 2), with the id order it disappears.

## 4. Tool caveat found on the way (for L-ALG's r0, not a claim about A_DTL)
dtl_regvec.py stores the rounds of a STABLE call up to the fixpoint (the loop breaks without appending). The r0
computation in dtl_regvec.py / dtl_crm.py / my r0d.py pads a shorter list with the EMPTY set. For a stable call that is
wrong past its last round (the set stays at the fixpoint). It changes r0 only when the two calls have different lengths
and one is stable. My first (LEX-R) check made this mistake at s7 -> s8 (V_7 7 -> 0); with fixpoint padding it is 7 -> 9.

## 5. Reading (L-RED)
(LEX) is the "death vector rises lexicographically" potential; it fails at the first DEF step that adds a high vertex to
an early round: the extra survivor shortens the top vertex's life. The top vertex then recovers (NR). Level 1 only so far;
a nest of depth >= 2 is the next climb target (fitness lex, injective).
