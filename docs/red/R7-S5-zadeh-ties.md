# R7: S5 (Zadeh least-entered + fixed index tie-break, adversary's numbering): where the published tie-break is used (L-RED, 2026-10-15)

Lead's ask (14:18Z): take DFH's (arXiv 1911.01074) or Friedmann's (IPCO'11, PGSolver zadehexp) Zadeh construction, find
exactly where the strategy-dependent tie-break is used, and either make those steps tie-free so that ANY fixed index order
gives the same run (then test under S5), or state precisely which step needs a strategy-dependent tie-break.

## Verdict: HELD so far (search still running at N >= 4; this file is updated when it ends)
No fixed total order of the edges, hence no numbering, reproduces the published Zadeh run at any N >= 2: the run's tie
decisions contain reversals (the same pair chosen in both orders) in every level and every class, driven by two predicates
of the current strategy (section 2). The tie steps cannot be made tie-free from inside the game (section 3). Fixed orders
can still run long on the same game: at N = 2, 3 the best numbering found (47, 169) beats the published tie-break
(43, 159); the growth beyond N = 3 is the open question of section 4.

## 1. The published run and its tie steps (Friedmann's construction, PGSolver's tie-break, ported faithfully)
Code: experiments/red/zadeh_lb.py = Zadeh's rule with PGSolver's lower-bound tie-break, ported line by line from
src/lib/solvers/stratimpralgs/switch_zadeh.ml @ d3cd624 (clone in scratchpad, opened): improvement_policy_optimize_fair
(lines 1407-1457: least occurrence record among improving edges), improvement_policy_optimize_fair_sub_exp_tie_break
(lines 1462-1591: state bits by "leads to" tests on the path sets, state', idxmap, the class function mp, then list order),
initial_strategy_for_exp_game (lines 1612-1650). Instances: L-SI's zadehexp(N) port of zadehexp.ml (labelled copies pinned
as experiments/red/instances/zadehexp_N{2,3}_labelled.pg). No OCaml toolchain in the container, so the port is checked by
growth only: switches 43, 159, 467, 1227, 3019 for N = 2..6 (first differences 116, 308, 760, 1792, ratios 2.65, 2.47,
2.36 = Theta(N 2^N) growth; PGSolver's zadehexp.ml line 100 calls the family "Exponential Lower Bound for Zadeh's rule").
Index tie-break (vj.py pick_zadeh, lexicographic in (v, w), same start): 41, 71, 155, 271, 419 (quadratic, R4).

| N | switches (lb tie-break) | tie steps (>= 2 candidates with the minimal record) | 'chosen before competitor' constraints | fixed total order consistent with all of them | direct reversals (pairs chosen in both orders) |
| --- | --- | --- | --- | --- | --- |
| 2 | 43 | 38 | 131 | none (cycle p1->d0 < q0->d0 < m0->d0 < p1->d0) | 10 |
| 3 | 159 | 142 | 474 | none (cycle b1->E1 < v1->X1 < a1->E1 < b1->E1) | 79 |
| 4 | 467 | 408 | 1047 | none (cycle b3->E3 < b1->E1 < b3->E3) | 212 |
| 5 | 1227 | 1046 | 1823 | none (cycle r1->d0 < w3->q3 < r1->d0) | 390 |

Almost every step of the published run is a tie step (the counter keeps all records within one of each other, that is the
design), and the choices made at them are inconsistent with every fixed total order of the edges at every N >= 2. An index
order (lexicographic in vertex indices) is a fixed total order, so no numbering reproduces the published run. This is
exact (zadeh_lb.py --rev lists every reversal with the bit state sp of the strategy at both times).

## 2. Which steps, which classes (item 1 of the ask)
PGSolver's mp function ranks a candidate edge by its class and by two strategy-dependent predicates:
- h(c, i): "does the partner gate node of level i currently point into the cycle" (a_i -> E_i, b_i -> E_i, v_i -> X_i,
  w_i -> X_i); used for the escape edges o_i, p_i, q_i, r_i (rank -4N+... if the own gate is closed, +N+... if open) and for
  the second edge of a gate (a_i -> E_i ranks after b_i -> E_i's partner state). DFH's counterpart: the split of the escape
  edges into E^1 (cycle vertex points to its cycle centre) and E^0 (it does not), with E^1 before B, S, E^0 (Def 6.4, p.15,
  opened), and D^1 criterion 1 (open cycles first, p.15).
- state'(sigma): the bit vector derived from which gates are closed (sp[i] = sp[i+1]*s_i + (1-sp[i+1])*f_i, idxmap);
  used in f_i, g_i to decide which of the two cycles of level i (E_i or X_i) is entered first: E_i first iff bit i+1 is
  unset. DFH's counterpart: E^1 criteria 2-3 (exactly one cycle centre of the level closed / halfopen escaping to t->),
  D^1 criteria 2 and 4 (bit beta_i, active cycle centre F_{i, beta_{i+1}}), pp.14-15.
The direct reversals of section 1, by edge class (zadeh_lb.py --rev; N = 2: 10 pairs; N = 3: 79; N = 4: 212; N = 5: 390):
| reversal pair (classes) | predicate that flips it | count N = 2 / 3 / 4 / 5 | example (N = 2) |
| --- | --- | --- | --- |
| a_i -> E_i vs w_i -> X_i, b_i -> E_i vs v_i -> X_i (same level, the two cycles) | state' (bit i+1) | 3 / 9 / 20 / 35 | step 1: a0 -> E0 at sp = 00; step 30: w0 -> X0 at sp = 01 |
| escape vs escape, o/p/q/r -> d0 or -> m1, across levels and within a level | h (own gate closed) and level | 6 / 48 / 128 / 232 | step 6: o0 -> d0 before p1 -> d0 at sp = 10 (gate 0 closed); step 35: p1 -> d0 first at sp = 11 |
| same class, different level (p_i -> d0 vs p_j -> d0, a_i -> E_i vs a_j -> E_j, ...) | h (closed level first beats the level order) | 1 / 14 / 40 / 72 | step 9: p0 -> d0 before p1 -> d0; step 35: p1 -> d0 before p0 -> d0 |
| gate edge vs escape of another level (a -> o, w -> q, ... vs p/r -> d0) | h | 0 / 8 / 24 / 51 | |
Both predicates produce reversals at every N and in every level; neither is confined to one phase or one class.

## 3. Can those steps be made tie-free (item 1, second half)? No, for the reasons below
- Reversal lemma. If one run chooses a over b at a tie step t1 and b over a at a tie step t2, no fixed total order
  reproduces it (trivial), and no change of the INITIAL occurrence records does either: at both steps rec(a) = rec(b), so
  an initial offset delta(a) - delta(b) != 0 makes the same edge strictly smaller at both steps. Zadeh's records count
  switches, not entries: pads, relays and fillers (the S7 tools of R3/R5) change entry counts and traffic, which Zadeh
  never reads, and low-priority relays do not change which switches are improving (the valuation order of two targets is
  decided by the most relevant vertex in the symmetric difference of their path sets; relays sit below every original
  vertex), so they leave the improving sets and the records alone. The only lever on a Zadeh run is the tie-break.
- Making a reversal pair tie-free from inside the game would need one of the two edges to be switched an extra time
  between t1 and t2. For a gate edge (a_i -> E_i) an extra switch means the gate opens and closes once more, i.e. a
  different counter run; for an escape edge (o_i -> d0) it means the escape leaves d0 and comes back, which the counter
  does exactly once per reset of level i. Friedmann's construction already uses every such switch to keep the records
  within one of each other (that is why 38 of 43 steps are ties); there is no slack switch to spend.
- Cutting the pairs apart by relays (two copies of an edge with their own records) is not available under S5: injective
  priorities (p' = 2 rank + parity, part of the candidate) make two copies of an edge have different valuations, so the
  lower copy is never taken and the pair is one edge again; copies with equal valuation need equal priorities, which the
  candidate excludes.

## 4. Fixed orders need not reproduce the published run: search (item 2)
The cyclic constraints only say the published run is unreachable; a different, equally long fixed-order run may exist.
Two searches on zadehexp with the exp-game start (the start of the lower bound; S5's best-reward start is a different
run, R4): zadeh_anyorder.py (exhaustive DFS over the tie decisions consistent with a growing partial order, i.e. every
fixed total order, index orders included) and zadeh_climb_fast.py (hill-climb over numberings, scored by vjfast zadeh
--start spec:<exp start>, 3 restarts x 3000 swaps).
| N | published tie-break | identity numbering | any fixed total order (DFS, 3M nodes, budget hit) | best numbering found |
| --- | --- | --- | --- | --- |
| 2 | 43 | 41 | 47 | 47 |
| 3 | 159 | 75 | | 169 (all 3 restarts) |
| 4 | 467 | 101 | | RUNNING |
| 5 | 1227 | 197 | | RUNNING |
| 6 | 3019 | 343 | | RUNNING |
| 7 | 7131 | 495 | | RUNNING |
Identity numbering for N = 8: 595. The best numbering found at N = 3 (scratchpad zfast_3.pg) has no readable class
structure (Even vertices in index order: a1 g1 d0 b0 w0 o0 s1 a0 w1 q1 d1 p0 a2 v1 r1 b1 o1 m2 q0 v0 s0 g0 p1 r0 o2 m0 b2
m1 p2 g2); R4's class-structured schemes stay polynomial.

## 5. The precise statement (item 3)
Zadeh's rule reads nothing but the improving set and the per-edge switch counts; the published exponential runs (Friedmann
IPCO'11 / PGSolver, DFH 1911.01074) keep every record within one of each other and let a strategy-dependent order pick
among the equal ones at 9 of 10 steps. Two predicates of the current strategy are consulted, and each one is consulted in
both directions on the same pair of edges within one run (section 2):
- (P-gate) at level i, the cycle entered first is E_i when bit i+1 of the counter is 0 and X_i when it is 1 (PGSolver f_i,
  g_i; DFH E^1 criterion 4 / D^1 criterion 4 in MDP context, criteria 2-3 in PG context). A fixed order picks one cycle
  for both states of bit i+1.
- (P-escape) an escape edge (o_i, p_i, q_i, r_i -> d0 / m1; DFH's e_{i,j,k}) is taken before the escape edges of the other
  levels while its own gate is closed, and after them while it is open (PGSolver h; DFH E^1 before B, S, E^0). A fixed
  order ranks the escapes of levels i and j once, so one of the two states takes the wrong escape first.
Open problem (sharp form, for S5). Is there a family of sink parity games with injective priorities, with a numbering of
its vertices, on which Zadeh's rule with ties broken by the smallest (source index, target index) pair makes
2^{Omega(n^c)} switches? Equivalently: a Zadeh counter whose tie steps are all decided the same way in every strategy,
i.e. a counter in which (i) each level has one cycle, or its two cycles are always entered in the same order regardless
of the higher bits, and (ii) the switch counts of the escape edges of a closed level and an open level differ at every tie
between them, so that closing a level costs its escapes a record the open levels' escapes do not pay (or vice versa),
consistently through the whole count. Friedmann's and DFH's counters violate both (i) and (ii) at every level and every
N >= 2; no fixed order reproduces their runs, and no change of the initial records, no pads, relays or fillers can change
that (section 3). Whether a different counter satisfies (i) and (ii) is open; the search of section 4 is the evidence
either way at small N.

## DONE / FINDINGS / NEEDS
- DONE: zadeh_lb.py (port + constraint analysis), zadeh_anyorder.py, zadeh_order_climb.py, zadeh_climb_fast.py; tables of
  sections 1, 2, 4; check.sh pins zadeh_lb N = 2 (43 switches, no fixed order; index 41).
- FINDINGS: (1) the published Zadeh runs are unreachable by any fixed order at every N (reversals in every class, two
  strategy predicates); (2) the tie steps cannot be made tie-free by records, pads or relays; (3) fixed orders can beat the
  published tie-break at N = 2, 3 on the same game; growth beyond N = 3 pending.
- NEEDS: none yet.
