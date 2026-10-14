# Referee report: L-COMP's Python ports of PGSolver generators (recursiveladder, switchallexp, switchbestexp)

Referee: REFEREE. Date: 2026-10-14. Routed by the Lead 2026-10-14 18:36Z.

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
