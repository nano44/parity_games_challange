# Referee report: L-COMP's Python ports of PGSolver (generators and strategy-improvement solvers)

Referee: REFEREE. Date: 2026-10-14. Routed by the Lead 2026-10-14 18:36Z (generators) and 18:40Z (solvers).
Part A: the three generator ports (verdict OK). Part B: `pgsolver_si.py`, switch-all and switch-best (verdict OK with
one deviation to state). Both at claude/l-comp e3e7e4e; `pgsolver_port.py` is byte-identical between 135888c and e3e7e4e.

# Part A: generators

## Claim and source
- Port: branch claude/l-comp, head 135888c, file `experiments/hard-families/pgsolver_port.py` (functions
  `SymbolicPG`, `recursiveladder`, `switchallexp`, `switchbestexp`, `mkli`). The file says it transcribes PGSolver at
  commit d3cd624.
- Original: github.com/tcsprojects/pgsolver, commit `d3cd624b61cd66739c45aff9554f6bbdcdd05401`, cloned by me into my
  session scratchpad (untrusted download, not committed). Files read in full: `src/lib/generators/recursiveladder.ml`
  (48 lines), `src/lib/generators/policyiter/generators/switchallexp.ml` (75 lines),
  `src/lib/generators/policyiter/generators/switchbestexp.ml` (82 lines),
  `src/lib/generators/policyiter/stratimprgenerators.ml` lines 1–60 (SymbolicParityGame), and
  `src/lib/paritygame/paritygame.ml` lines 19 (`nd_show`), 25–40 (nodeset = TreeSet), 128–139 (players,
  `plr_benefits pr = pr mod 2`), 175 (`pg_create`), 201–206 (`pg_add_edge`), 365–387 (`output_game`).
- Method: every OCaml statement matched to the Python statement that transcribes it; priorities, owners, successor
  lists, loop bounds and index assignment compared term by term. I could not run PGSolver (no OCaml toolchain here),
  so this is a reading check, not an output diff.

## Verdict: OK (all three ports faithful). Two cosmetic findings.

### recursiveladder (recursiveladder.ml:13–46 ↔ port lines "recursiveladder")
| OCaml | port | match |
| --- | --- | --- |
| `height = 1 + arg` (13), `w = 5` (15), `pg_create (5*height-5)` (17) | same | ✓ |
| loop `i = 0..height-1` (19); `start_idx = i*w-2`, `p = (i+1)*3+2`, `start_pl = i mod 2`, `o = 1-start_pl`, `mx`, `mfx`, `mn` (20–26) | same | ✓ |
| `prnt j pr pl succs`: priority `pr`; owner `plr_benefits (start_pl+pl)` = `(start_pl+pl) mod 2`; desc `nd_show (start_idx+j)` = decimal string; edges `w+start_idx` for each `w` in `succs` (the lambda's `w` shadows the outer `w = 5`) (28–33) | `prio`, `own = (start_pl+pl) % 2`, `desc = str(start_idx+j)`, `succ.add(x+start_idx)` | ✓ |
| `if not mn`: `prnt 0 o 1 [3-w;1]`; `prnt 1 o 0 (if mx then [0] else [0;2])` (36–39) | same | ✓ |
| `if not mx`: `prnt 2 p 1 [w+1;3]`; `prnt 3 (p-1) 0 ((mn?[]:[3-w]) @ (mfx?[]:[w+3]) @ [4])`; `prnt 4 (p-2) 1 (if mx then [3] else [3;w+1])` (40–44) | same | ✓ |
| output: `parity n-1;` then, for nodes with `pr >= 0 && 0 <= pl <= 1`, `i pr pl succs "desc";` with successors from a TreeSet (ascending, duplicates merged) and desc printed when present and non-empty (`output_game`, 365–386) | `parity {size-1};`, same filter, `sorted(set)`, desc always present for printed nodes | ✓ |

Index coverage (my check): i = 0 fills 0..2, i = 1..height−2 fill 5i−2..5i+2, i = height−1 fills 5height−7..5height−6:
all of 0..5height−6, so every printed line has a priority ≥ 0 and all edge targets are printed nodes.

### SymbolicParityGame (stratimprgenerators.ml:7–47 ↔ `SymbolicPG`)
`create_new x` ignores `x` (14) ✓. `internal_add`: existing symbol → its index, data overwritten only if `override`;
new symbol → index = current table size (27–35) ✓ (`_internal_add`). `add_node`: add/override the node with
`(pr, pl, desc)`, then for each target `internal_add symb' (-1) plr_Even None false` and add the edge (40–45) ✓.
`to_paritygame`: `pg_create (Hashtbl.length ht)`, node data and TreeSet successors copied by index (16–25); the
port prints directly with the same `output_game` filter ✓. Touched-but-never-added symbols would print nothing
(pr = −1); none occur in either generator (every referenced symbol is added within its range; checked for
switchallexp: CycleSelector j < n, DecLaneEven ≤ 2n−1, UpperSelectorHelper ≤ n−2, CycleSelectorDecelerator ≤ n−1;
for switchbestexp: DecLaneEven ≤ 6n, incl. 6(n−1)+6 = 6n, the others as above).

### switchallexp (switchallexp.ml:30–66 ↔ port `switchallexp`)
All 17 `add` statements compared term by term (symbol, priority, owner, successor list, including the `i < 2`
DecLaneOddRoot case, the `i = 0` empty prefixes, the `i = n−1` / `i = n−2` cases of UpperSelector and
UpperSelectorHelper, the `mkli` ranges `n` and `n−1`, loop bounds `0..2n−1` and `0..n−1`) ✓. Descriptions
`symb_to_str` (25) ↔ `lab` ✓.

### switchbestexp (switchbestexp.ml:34–74 ↔ port `switchbestexp`)
All 24 `add` statements compared term by term, including the DecLane loop bound `0..6n` inclusive (`range(6n+1)`),
`CycleNodeToLane1`'s conditional `DecLaneEven (6i+4)` for `i < n−1`, `CycleNodeToLane2`'s `DecLaneEven (6i+6)`,
and the CycleAccessDistributer node ✓. Descriptions (29) ↔ `lab` incl. `e'`, `f'`, `g'`, `c` ✓. The port's remark
that the registered description string (79) is copied from switchallexp is correct.

## Findings (cosmetic, no effect on generated games)
1. The port's line citations for switchallexp are off by +2 (e.g. "line 41" for FinalCycle is line 39; "lines 50-53"
   are 48–51; "lines 55-66" are 53–64; "33-67" is 30–66). The switchbestexp and recursiveladder citations are exact.
2. The docstring cites `stratimprgenerators.ml:11-50` for SymbolicParityGame; it is lines 7–47.

## Gaps
- Reading check only: no execution of the OCaml originals (not available here; owner question Q4 in NOW.md covers
  running the PGSolver binaries). An output diff on a few sizes would close this.
- TreeSet ordering assumed to be ascending integer order (`ns_nodeCompare = compare`, paritygame.ml:29); standard.


# Part B: `experiments/hard-families/pgsolver_si.py` (claude/l-comp e3e7e4e)

## Claim and source
- Port: `SI` class (orderings, initial strategies, valuation ordering, best decision, `evaluate`, `policy_switchall`,
  `policy_switchbest`, `solve`), `alternating_transformation`, `cheap_escape_cycles_transformation`, `solve_switchbest`;
  it imports `experiments/harness/pg.py` (max-parity PGSolver format, `Game(prio, owner, succ)`, `read`, `write_sol`).
- Original, PGSolver d3cd624, read in full for the cited ranges: `src/lib/solvers/stratimpralgs.ml` 54–199 (orderings,
  initial strategies, `node_valuation_ordering`, `best_decision_by_ordering`, `strategy_improvable`, `winning_regions`,
  `winning_strategies`, `evaluate_strategy`), 441–616 (`strategy_improvement`, `strategy_improvement'`), 636–637,
  659–669, 693–696 (registration of "switchall" inside `universal_solve`);
  `src/lib/solvers/switch_globally_best.ml` 1–119; `src/lib/paritygame/transformations.ml` 271–320 and 338–413;
  `src/lib/paritygame/paritygame.ml` 33–53 (TreeSet nodesets; the list version at 59–102 is commented out), 112–120
  (`ns_some` is random for lists but the active `ns_some = TreeSet.choose`, and `TreeSet.choose = min_elt`,
  tcsset.ml:426), 139, 181–191, 473–474 (`reward`), 1214–1237; `src/lib/paritygame/univsolve.ml` 23–66, 267–650,
  665–780 (`universal_solve_run`); `src/apps/pgsolver/pgsolver.ml` 102–116 (the `-dgo -dsd -dlo -dsg` flags).
- tcslib at 6778419 (the commit L-COMP cites; cloned by me): `src/data/tcsgraph.ml` 8–226 (`GraphUtils`,
  `DynamicGraph`), `tcsset.ml` 132–166, 284–287, 426 (fold/iter ascending, `sym_diff`, `choose = min_elt`),
  `tcslist.ml` 35–42 (`min_elt`/`max_elt`), `tcsarray.ml` 48–52, `tcsbasedata.ml` 181–227 (`Iterators`).

## Line-by-line correspondence (all ✓ unless noted)
| OCaml | port | note |
| --- | --- | --- |
| `relevance_total_ordering` with `node_total_ordering_by_position` (66–67): compare (prio, id) | `rel` | ✓ |
| `reward` (paritygame.ml:473): `−prio` if parity ≠ player and prio ≥ 0 | `reward` | ✓ |
| `reward_total_ordering` (69–74): by reward, ties by position, reversed when `ri mod 2 ≠ 0` | `rew` | ✓; OCaml `(−3) mod 2 = −1` and Python `−3 % 2 = 1` are both ≠ 0, so the test agrees for negative rewards |
| `ns_max` (paritygame.ml:120): fold ascending from `ns_some = TreeSet.choose = min_elt`, replace acc when `lessf acc x` | `ns_max` (acc = first of the sorted list) | ✓ |
| `initial_strategy_by_best_reward` (85–87), `..._by_last_edge` (83, `ns_last = max_elt`) | the two `initial_strategy_*` | ✓ (−1 for Odd nodes) |
| `node_valuation_ordering` (92–107): cycle node by reward ordering; then path sets by the most relevant element of the symmetric difference (`min_elt` of a set ordered by flipped relevance); then length with the parity of the second node | `nvo` | ✓ (`max(r, key=(pr, id))` is that element) |
| `node_valuation_total_ordering` (109–112), `best_decision_by_ordering` (114–118) | `nvto`, `best`, `best_in` | ✓ |
| `strategy_improvable` (123–128) | `improvable` in `solve` | ✓ |
| `winning_regions`, `winning_strategies` (130–145) | `win`, `ws` in `solve` | ✓ |
| `evaluate_strategy` (147–199): strategy graph (`paritygame_to_dynamic_paritygame_by_strategy`, 1229–1237); nodes in ascending reward order (snapshot set; nodes already valued or deleted are skipped); `depth_find` with filter `rel u v ≤ 0` and target `has_edge u v` (fold ascending, short-circuit); `sub_graph_by_node_closure` over predecessors; descending-relevance pass with the two reachability sets (predecessors excluding `u`, resp. `v`), path-set updates and `del_other_edges`; distances by `iterate_with_maximal_distance_single_loop` (cached `1 + max` over successors, 0 at `v`) for even `v`, BFS layers over predecessors for odd `v`; then `del_node` for the closure | `evaluate` | ✓ term by term; unreached nodes keep distance 0 as in OCaml (`dist.get(u, 0)`) |
| `strategy_improvement` (441–595): init, evaluate, loop `while improvable` with `counter` incremented per improvement and once after the loop; result regions/strategies | `solve` | ✓; `check_policy` is false for both registered solvers, so the `less_valuation` check is rightly absent |
| `improvement_policy_optimize_all_locally` (659–666) | `policy_switchall` | ✓ |
| "switchall" = `strategy_improvement game initial_strategy_by_best_reward node_total_ordering_by_position …` (668–669), no transformation | `SI(g).solve()` | ✓ |
| `improvement_policy_optimize_all_globally` (switch_globally_best.ml:13–107): pruned copy for Even nodes (keep successors with valuation ≥ the current one); Odd nodes lose successors valued above their best; Even nodes with > 1 pruned successor removed; sink elimination via `check` (min-first); `valued`; `todo`/`rest`; `compute_update'`, `compute_update` (fold from `min_elt`, strict `>`); the inner `todo` loop with the "impossible" guard; the `rest` step: `temp`, list built by prepending over an ascending fold (hence descending), `list_max … (valu_ord a b > 0)` = keep the first element and replace it whenever the current one is valued strictly above the candidate | `policy_switchbest` | ✓ term by term (I rederived `ListUtils.max_elt`/`min_elt`, tcslist.ml:35–42: the port's "first minimum" reading is right) |
| "switchbest" = `strategy_improvement_by_policy` (636–637) = `strategy_improvement'` (600–616): `alternating_transformation game true`, `cheap_escape_cycles_transformation game' false`, SI from `initial_strategy_by_last_edge`, restriction back, strategies of lost nodes cleared | `solve_switchbest` | ✓; the `total` branch for successor-less nodes is omitted because `pg.Game` rejects such games (pg.py:13–14) |
| `alternating_transformation` (338–393): dummy index order = first encounter in (i ascending, successor ascending); dummies get priority 0, the opponent owner, one edge back | `alternating_transformation` | ✓ |
| `cheap_escape_cycles_transformation` with `keep_scc = false` (271–320): priorities +2, escape edge to n (Even) / n+1 (Odd), four new nodes (1,Odd)→n+2, (0,Even)→n+3, (0,Even)→n, (0,Odd)→n+1 | `cheap_escape_cycles_transformation` | ✓ |
| `alternating_revertive_restriction` (397–413): a strategy into a dummy is replaced by the dummy's only successor | `solve_switchbest` tail | ✓; the port additionally maps a strategy into an escape node to None, where the OCaml would index out of range (never happens for a winning strategy) |

## The deviation (L-COMP's "DEVIATION" note): what it changes
PGSolver's registered "switchall" and "switchbest" (stratimpralgs.ml:693–696, switch_globally_best.ml:116–119) run the
strategy-improvement loop as the *backend* of `universal_solve` (univsolve.ml:267–650): global optimisation (removal of
useless self-cycles, solving useful self-cycles with attractor closure, 692–780), SCC decomposition with topological
processing and attractor propagation between SCCs (326–646), special-case solvers for single-parity and single-player
SCCs (410–455), and local optimisation (priority propagation, priority compaction, 463–480). The backend therefore
sees each non-trivial SCC separately, after priorities were compacted and after everything forced into already-solved
regions was removed; its iteration counter (`last_iteration_count`) is per backend call.

L-COMP's port runs the loop on the whole game. That is exactly PGSolver with all four optimisations switched off
(`-dgo -dsd -dlo -dsg`, pgsolver.ml:102–116); then `universal_solve_run` uses the dummy decomposition (univsolve.ml:
343–362), skips special games and local optimisation (options false), and the backend solves the whole game in one
call (513–545, "backend solved nothing" aside). So the port's counts are PGSolver's counts under those flags, not
under its defaults.

Does it change what the blow-up demonstrates? No for the claim M1 is about, with one caveat:
- The lower bound is a statement about the strategy-improvement algorithm (switch-all, resp. switch-best, with
  Vöge–Jurdziński valuations) on the family: the number of improvement steps grows exponentially. That is the bare
  loop's count, which the port measures. The games have a bottom SCC {FinalCycle} with a useful self-loop and a
  chain FinalSink → FinalCycle; with PGSolver's defaults those two nodes and whatever the attractor closure pulls in
  (Odd nodes whose only edge leads there, e.g. the CycleLeaver/UpperSelector tails near i = n−1) are solved before the
  backend runs, and priorities are compacted. Whether that lowers, raises or preserves the backend's count on this
  family I cannot say without running PGSolver; a priori it changes the backend's input, so the two counters are
  different quantities.
- Caveat for the write-up: any sentence of the form "PGSolver takes K iterations on switchallexp n" must say
  "PGSolver with -dgo -dsd -dlo -dsg" (or "the strategy-improvement loop"); the default binary is not what was measured.
- A second, smaller deviation: the port counts iterations as PGSolver does (one per improvement plus one), so the
  numbers are comparable to PGSolver's "solved with K iterations" line under those flags.

## Execution check (my own, see the note on reproduction below)
(pending: regions vs Oink on random games and iteration counts on the families are running; numbers follow in the next commit.)

## Verdict for Part B: OK (faithful to the bare strategy-improvement loop), with the deviation stated above to be
carried into any M1 claim verbatim.

## Gaps (Part B)
- Reading check plus my execution check against Oink's Zielonka for regions; no diff against the PGSolver binary's
  iteration counts (no OCaml toolchain here; owner question Q4). The counts in L-COMP's results are therefore
  unconfirmed by an independent implementation of the same loop.
- `pg.py` rejects games with successor-less vertices, so the `total = true` branch of `alternating_transformation`
  is untested; it is not exercised by the three families (every vertex has a successor).
