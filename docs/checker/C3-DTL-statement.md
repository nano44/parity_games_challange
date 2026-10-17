# C3: statement check of DTL's gauntlet-step-4 statement (CHECKER, 2026-10-15)

Target: docs/alg/DTL-proof.md §0 (0.1-0.4) at claude/l-alg 5175454, Theorems D1, D2 and L-ALG's own diff §0.4.
Checked against TARGET.md v1.0 §1-3, §5 (including D2 change 5) and §6. Statement diff only; no re-runs (Lead 15:56Z).
Code read: Oink at 8fbf0a7 (tools/oink/src, `git rev-parse` = 8fbf0a7, clean, as built by scripts/setup_oink.sh with
`-DCMAKE_BUILD_TYPE=Release`, setup_oink.sh:19):
- src/solvers/dtl.cpp, dtl.hpp
- src/oink.cpp
- src/tools/solve.cpp (the `oink` CLI)
- src/pgparser.cpp, src/game.cpp
- include/oink/oink.hpp
I make no judgement on whether D1/D2 are true.

## Verdict: FAIL (fixable in the statement; no proof work is invalidated yet)
| item | verdict |
| --- | --- |
| (a) objects and output pair vs TARGET §1-2, §5 change 5 | PASS with notes A-1, A-2 |
| (b) unit cost = bit cost; every number O(log(n+m)) bits | PASS with notes B-1..B-4 (checked in dtl.cpp myself) |
| (c) commutation with TARGET's priority compression | FAIL (minor): the justification is incomplete as written (C-1); the conclusion is not contradicted |
| (d) A_DTL pinned exactly | **FAIL**: self-loop preprocessing is ON in the fleet command the statement cites (D-1); CHECK_UNIQUE block, trace level and sort tie order not pinned (D-2..D-4) |
| (e) what a proof of D1+D2 would still lack for M4 | three shortfalls (E-1..E-3), listed below |

## (a) Objects and output
- Game, strategies, W_E/W_O, max-parity, pr into {0..n}, n = |V|, m = |E|: D1/D0.1 restate TARGET §1. Matches.
- Output pair: D1 gives (W_Even, W_Odd) = (W_E(G), W_O(G)). Matches TARGET §2.
  - D1 also requires that every vertex is solved: "solves every vertex exactly once".
  - This is needed: in release builds the completeness check is under `#ifndef NDEBUG` (dtl.cpp:1146-1151).
  - Oink::solveLoop (oink.cpp:405-420) clears the todo buffer and returns after `run()`, so unsolved vertices stay
    unsolved. The statement's "vertices never solved are output as unsolved" is accurate.
- Strategies (TARGET §5, D2 change 5): D1 requires positional σ_Even on W_Even ∩ V_E (and σ_Odd likewise). Each must win
  every consistent play against general opponent strategies and keep the play inside the region. This meets "every
  implementation also outputs positional strategies". PASS.
- A-1 (note). D1's object is Oink's in-memory Game, not TARGET's input encoding. Oink reads PGSolver text
  (`PGParser::parse_pgsolver_renumber`, pgparser.cpp:350), renumbers ids and builds the out/in edge arrays.
  - TARGET §1's encoding (n, owner bits, binary priorities, edge list) maps to this in O((n + m) log n).
  - D2(e) says "step 0 included" but step 0 is only `ensure_sorted`. Charge the construction of the Game (edge and
    in-edge arrays) explicitly, or define A_DTL's input as TARGET's encoding.
- A-2 (note). The comment at dtl.cpp:1107 says "First solve for player Odd, then solve for player Even". The code
  (1109-1121) runs search(0) (Even) first, then search(1). The statement follows the code. Correct; record it so the
  proof does not follow the comment.

## (b) Bit cost (dtl.cpp read for every stored number)
Numbers on the release path, each bounded:
- vertex indices (< n);
- priorities and thresholds `t` (≤ max priority ≤ n; dtl.cpp:585-594, 722, 898-904);
- `curdist`/`dist` (≤ n, one per pruning round, 655/675);
- queue/stack positions and `pea_curidx` (≤ n);
- tangle indices `tidx = tpr.size()` (≤ tangles(G), 440);
- `tpr[t]` (a priority, or -1 for deleted);
- counters `iterations`, `dominions`, `tangles` (int, dtl.hpp:35-38);
- bitset words.
No weights, no products, no sums of priorities. `steps` is declared and logged but never incremented (dtl.cpp: only
line 1142), so it is always 0. `INT_MAX` occurs only in computeDistanceValues, which is called only under
`#ifndef NDEBUG` (1004-1010, 1046-1052) and from `new_algorithm` (never called).
- B-1 (wording). "No number has more than one word ... met by construction, not by assumption":
  - true for the n-bounded quantities;
  - for `tangles`, `iterations`, `dominions` and tangle indices, the O(log(n+m))-bit bound is a consequence of D2(a),
    (d), (e), not "by construction".
  - Suggest: "every number is ≤ n + 1 or ≤ the number of steps executed, so has O(log(n + m)) bits once (e) holds".
  - Not circular in a harmful way (one conjunction), but the "by construction" phrase overstates.
- B-2 (model). The pinned code stores these counters in 32-bit C++ `int`. The RAM statement should say that A_DTL is
  the code with `int` read as a word of TARGET §3's RAM. Otherwise the C++ program and the RAM algorithm differ once a
  count exceeds 2^31 − 1.
- B-3 (cost to charge). The duplicate-tangle check (dtl.cpp:385-424, compiled in release, see D-2) compares each new
  tangle with every stored tangle: O(tangles(G) · n) per new tangle, O(tangles(G)^2 · n) in total.
  - Polynomial given D2(a), but it is not among the costs D2(b)-(d) name.
  - D2(e) must include it.
  - Likewise `tin[v].push_back` per escape (443) and the `new int[]` copies (446-457).
- B-4 (cost to charge). The threshold loop `for (int t=0; t<=max_prio; t++)` (dtl.cpp:721-722) runs max_prio + 1 times
  per pruning round, whatever priorities occur.
  - On TARGET inputs that is ≤ n + 1, as the statement says.
  - It is why compression is mandatory for D2 (C-1).

## (c) Commutation with compression
The claim (§0.4): DTL's behaviour depends on priorities only through order and parity, because "every comparison in
dtl.cpp is `priority(u) <= t`, `priority(v) > t`, `priority(u) == t`, or `priority & 1`" (list of 12 lines).
- C-1 (FAIL, minor; fix the text). The list is incomplete and "every comparison" is not accurate. Uses of priority
  values outside it:
  - dtl.cpp:721-722: `max_prio = priority(nodecount()-1)` and `t++`. Arithmetic on priority values. The loop visits
    non-occurring thresholds, and its iteration count depends on the values, not only the order.
  - dtl.cpp:585 and 898: the initial threshold `t = 0`, then `t = priority(v)`. A constant compared with priorities.
    With compression, "priority(v) > 0" can change truth value (a minimum priority 2 compressed to 0).
  - dtl.cpp:74 and 1033: `max_prio < 0` sentinel with `max_prio = -1` for unrestricted attraction.
  - dtl.cpp:1088: `Player[v] = priority(v)&1`.
  - dtl.cpp:116-118: `tpr[t] == -1` marks a deleted tangle (a priority slot reused as a flag).
  - game.cpp:495: `std::sort` by `(unsigned int)priority`.
- The conclusion "A_DTL on the compressed game makes the same choices" needs two more sentences:
  - (i) An iteration of the 722 loop at a threshold t with no priority in (t', t] (t' the previous occurring priority)
    attracts nothing new and removes no candidate, because the attractor condition is `priority ≤ t`. So the visited
    states agree; only the iteration count differs.
  - (ii) The initial `t = 0` at 585/898 acts as "the least occurring priority" in both games.
  - Neither sentence is in the statement; I record them as what the statement needs, not as checked mathematics.
- Also state where compression is applied: before Oink's parser, on TARGET's encoding. Oink reads priorities as uint64
  and stores them as int (pgparser.cpp:429 `priority[id] = n` into std::vector<uint64_t>, then into Game's int
  priorities), so uncompressed huge priorities overflow inside the pinned code.

## (d) Pinning A_DTL
Options actually in force for `oink --dtl --no-single --no-wcwc` (src/tools/solve.cpp:321-343, oink.hpp:164-171):
| option | default | fleet command | statement says |
| --- | --- | --- | --- |
| solveSingle | true | off (`--no-single`) | off ✓ |
| removeWCWC | true | off (`--no-wcwc`) | off ✓ |
| **removeLoops** | **true** | **ON (no `--no-loops`)** | **off ✗** |
| parser bad-loop removal (`parse_pgsolver_renumber(in, removeBadLoops)`, solve.cpp:263) | on unless `--no-loops` | **ON** | not mentioned ✗ |
| inflate / compress / renumber | false | off ✓ | off ✓ |
| bottomSCC (`--scc`) | false | off ✓ | not mentioned (fine) |
| trace (`-t`) | 0 | 0 | "trace is not part of the algorithm" (see D-3) |
| build | Release (NDEBUG) | setup_oink.sh:19 ✓ | release ✓ |
| workers (`-w 1` in harness) | n/a | dtl is registered non-parallel (solvers.cpp:77) ✓ | n/a |

- D-1 (FAIL). The statement says "Preprocessing switched off (as in every fleet run: `oink --dtl --no-single
  --no-wcwc`): ... no self-loop removal". That command leaves self-loop handling ON, in two places:
  - The parser drops every self-loop v → v whose owner differs from the parity of pr(v) when v has another successor
    (pgparser.cpp:450-452; kept only if it is the sole edge, 478-481). The game DTL receives is not the input game.
  - `Oink::solveSelfloops()` (oink.cpp:242-268, called at 473) solves winning self-loops and sole losing self-loops,
    then `flush()` (oink.cpp:330-346) attracts to them. All of this happens before DTL runs, which then sees those
    vertices as disabled.
  - Every fleet run I found uses this command without `--no-loops`: experiments/alg/dtl_check.py:20, dtl_growth.sh:4,
    families.py:46, oink_fit.py:15, c4_product.py:51 at 5175454; harness solvers.py:30.
  - Fix, one of:
    - (i) pin A_DTL as `--no-single --no-wcwc --no-loops`. Then the step-2 evidence was gathered on a different
      algorithm and must be re-run on the pinned one.
    - (ii) put the parser's bad-loop removal, solveSelfloops and flush into A_DTL's step 0 and into D1/D2 (they are
      O(n + m)).
  - Either way, the statement and the evidence must name the same command.
- D-2 (pin). `#define CHECK_UNIQUE (1 or !NDEBUG)` (dtl.cpp:23) is always 1, so the duplicate-tangle block (385-424)
  is part of the release algorithm. It sorts the new tangle and discards it if a stored tangle has the same vertex set.
  - The comparison reads only `_tv[2*i]`, the vertices, not the strategies `_tv[2*i+1]`.
  - It also leaves `new_tangles` unset for that tangle, which affects search's return value through `tangles != T`.
  - The statement's "code under #ifndef NDEBUG and trace is not part of the algorithm" does not mention it. Name it
    in 0.1. D2(a)'s tangles(G) counts tangles kept after this check.
- D-3 (pin). Trace code outside `#ifndef NDEBUG` is not pure logging: with trace ≥ 1 a dominion found at depth ≠ 0
  calls `LOGIC_ERROR; exit(-1)` (dtl.cpp:349-354), and with trace = 0 the same dominion is silently accepted. Pin
  "trace = 0 (no `-t`)" explicitly.
- D-4 (pin). Step 0's `ensure_sorted` uses `std::sort` (game.cpp:495), which is not stable, on priorities only.
  - The relative order of equal-priority vertices, and so every later index-order choice (loops over v in index
    order, `Candidates` order, `find_first`), is implementation-defined.
  - The parser's renumbering also fixes the initial ids.
  - The statement must say either "for every order of equal-priority vertices" (the proof then covers all orders) or
    fix one order (e.g. stable by input id) and pin the library.
  - "Deterministic: yes" (§0.4) holds for a fixed standard library, not as an abstract algorithm.
- Pinned correctly: release build (NDEBUG), `interleaved = false` for A_DTL / true for A_IDTL (dtl.hpp:33; IDTL
  registered at solvers.cpp:78), non-bottomSCC solveLoop, no inflate/compress/renumber, solveSingle and removeWCWC off.

## (e) What a correct proof of D1 + D2 would still not give (vs M4, TARGET §2, §5, §6)
- E-1 (Lean). TARGET §5 step 4: "A claim presented as M4 also needs its correctness formalized in Lean against
  TARGET.md (no sorry, allowed axioms only)".
  - §6 fixes the form (`solve_correct` with EvenWins/OddWins over general strategies).
  - Prose proofs of D1 and D2, double-refereed, give "refereed-only" at most. That is not enough for an M4 claim.
- E-2 (object). TARGET §6, D2 change 2: "the Lean `solve` must implement exactly the pseudocode whose running time is
  analysed", with a REFEREE-signed line-by-line correspondence.
  - D1/D2 are stated about dtl.cpp line ranges; the pseudocode is docs/alg/candidates/C5-DTL.md.
  - The step-4 statement should name ONE object for the running-time proof (the pseudocode), and make the dtl.cpp
    correspondence a separate signed item.
  - Otherwise the Lean `solve` must be matched to C++, which §6 does not provide for.
- E-3 (input and size). M4's p(n + m) is measured from TARGET's encoding.
  - D2(e) must include parsing/building the Game (A-1) and, for inputs outside {0..n}, the compression step before
    parsing (C-1).
  - D2's p_e is over n + m of the game DTL receives. That is the same game only if D-1 is resolved by option (i);
    under option (ii) preprocessing removes edges, so p_e must be stated over the input.
- Not shortfalls (checked): existential polynomials p_a..p_e are what TARGET §2 asks; D2(c)'s depth bound uses d ≤ n + 1
  in TARGET's sense; D1's strategy clause is as strong as change 5 needs; A_IDTL's extra "no `solver stuck`" clause is
  the right completeness condition for the interleaved loop.
- Outside the statement (gauntlet bookkeeping): steps 2-3 must be on the pinned A_DTL (see D-1). Step 5 (CHECKER on the
  exact commit) follows the proof.

## Fixes for PASS (statement text only)
1. D-1: choose (i) `--no-loops` added, with step-2 re-runs, or (ii) loop preprocessing inside A_DTL. Make §0.1, D1, D2
   and every fleet command agree.
2. D-2, D-3, D-4: name the CHECK_UNIQUE block, trace = 0, and the equal-priority order (all orders, or one fixed order).
3. C-1: correct the order-and-parity justification (lines 721-722, 585/898, 74/1033, 1088, 116-118, game.cpp:495) and
   add sentences (i)-(ii); apply compression before parsing.
4. B-1, B-2, B-3: reword "by construction"; read `int` as a RAM word; include the duplicate-check and tangle-storage
   costs in D2(e).
5. E-1..E-3: either add the Lean statement (TARGET §6) and name the pseudocode as the analysed object, or label D1/D2
   as the refereed-only part of step 4 with the Lean step still owed. Charge input construction in D2(e).
