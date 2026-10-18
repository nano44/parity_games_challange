# R43: (TREE-PIECE⁺) is false in two-player games (L-RED box 14, item 2; produced on Opus 5.5)
Status: KILL (DATA, both orders, L-ALG's unmodified checker), unrefereed. Written 2026-10-18 22:03Z (date -u).
Target: Lead box-14 item 2. The statement is attacked as written in L-ALG docs/alg/GAP-A-M.md §36a at l-alg 5eb1b4bd.
Checker: b12_ident.tp_score with PLUS=1 (the climb score L-ALG uses for (TREE-PIECE⁺)) and `b12_ident.py TREE=1`. Both are
unmodified, and the l-alg 5eb1b4bd copy is byte-identical to the in-tree experiments/alg copy. Pinned Oink @ 8fbf0a7.

## 1. Statement (quoted, §36a)
> For a search s, list its best_vertices calls in execution order; a call c has depth d_c, context R_c, rank ρ_c (n + 2 stable,
> emptying round e for −1, 0 if it returns 0), final V_c, its PIECE (R_c minus the context of the next call at depth d_c before the
> recursion returns to a shallower depth; all of R_c if none) and its position (index among the depth-d_c calls of its parent call).
> Key of v in piece(c): (v, d_c, position, ρ_c, |R_c|, |V_c|).
> (TREE-PIECE⁺): for every consecutive pair s, s+1 of the phase whose call sequences (d, R, ρ, V) differ, some vertex holds at s+1 a
> key it held at no search ≤ s of the phase.

## 2. Counterexample
experiments/red/tpp/instances/tpp_viol_n22.pg, sha1 a5088b091cbddad1b62233335649b8088b7d1089. Two-player, n = 22, 28 edges,
some priorities tied.
- Shrunk greedily from the climb's tpp_viol_n63.pg (sha1 64d0832859a415f8bda8959f35e55bc9520425d9, also pinned). The shrink
  (experiments/red/tpp/shrink.py) keeps the violation in both orders.
- Pinned Oink `--dtl --no-single --no-wcwc --no-loops -v`: 5 iterations (even 4, odd 1), 1 dominion, 4 tangles, solution verified.
  The model also makes 5 iterations, and Zielonka solves the game.
- tp_score PLUS=1: (1, 0, 3, 5) in BOTH orders, that is, 1 violation and margin 0.
- `TREE=1`, both orders: "TREE-PIECE … transitions 3 without a new key 1 first (0, 0)", "identical depth-0 states 1",
  "depth 1: context differs 1".
- The n63 file gives (1, 0, 6, 8) in both orders, with pinned Oink 8 iterations, verified.

Even phase (0, 0), searches 2 → 3 (experiments/red/tpp/explain.py; the stable and Oink orders print the same chains):

| call | depth | s1 | s2 | s3 |
| --- | --- | --- | --- | --- |
| 1 | 0 | −1, e5, piece of 14 | −1, e5, piece of 20 | = s2 |
| 2 | 1 (pos 0) | |R| 12, V {12} | |R| 18, V {12,17,20} | = s2 |
| 3 | 1 (pos 1) | |R| 11 | |R| 14 | = s2 |
| 4 | 1 (pos 2) | R*, −1 e3, V {4,9}, piece {4,9} | R*, −1 e3, V {4,9}, piece {2,4,6,8,14,15,18,19} | R*, −1 e3, V {4,9}, piece {2,4,6,8,9,14,15,18,19} |
| next | 1 | … | |R| 1 = {9}, stable | |R| 0 |

- R* is the same 9-vertex set at s1, s2 and s3.
- Calls 0-3 are identical at s2 and s3, and call 4 keeps its R and outcome. Its piece grows by vertex 9, which SAME-CTX-type
  monotonicity (§36b S3) allows, because the input (R, X) is the same at s2 and s3. So the call sequences differ (the next depth-1
  context goes from {9} to ∅), and (TREE-PIECE⁺) applies to this transition.
- At s3 vertex 9 holds the key (9, 1, 2, 3, 9, 2). It already held that key at s1. At s1, call 4 had the SAME R* and the same outcome
  but a DIFFERENT X, because its parent subgame was smaller (call 2: |R| 12 against 18). With that X, call 4 took the Dom(prevV)
  branch with piece {4, 9}.
- Every other key of s3 was held at s2. So no vertex gets a new key.

## 3. Reading
- Where the proof sketch breaks. The failing step is not §36b S4, a falling outcome at a fixed input: no outcome falls here. It is
  the identification of a call by (d, position, R, ρ, |V|), because S1 fixes a call's behaviour by its INPUT (R, X).
  - At depth ≥ 1, X = parent piece \ R, and the parent's subgame can differ between searches while (d, position, R) stays the same.
  - Then the same key can sit on a vertex in two different pieces, at s1 and s3. In between, at s2, the vertex sits elsewhere.
- Repair options and their cost (reading):
  - Add |X|, or the parent context, to the key. Then the count of keys becomes a count of (parent context, R) pairs. That is a
    per-depth (CTX⁺) count again, the open term of R9 / R14.
  - Restrict the statement to depth 0. There X = G′ \ R (R9 (a)) is fixed by R. This is (VR-NEW_all), which still survives on all
    data (R41; GAP-A-M §32).
- On 𝒞^1P this mechanism is impossible: by R42 §2 (EMPTY-REC) every recursion of a q-search there is on ∅. The 𝒞^1P part of
  (TREE-PIECE⁺) is the depth-0 statement, and (VR-NEW_all) is not touched by this instance.
- How it was found: experiments/red/tpp/tpclimb.py, a graded two-player climb.
  - Score: (violations, −margin, −#new keys at a min-margin transition, −distance of those keys to keys already held by the
    vertex, #falls at a fixed input, transitions). Margin is L-ALG's "fewest vertices with a new key", which plateaus at 1.
  - Run: stable order, seed 33, vertex insertions 5 %, 1,318 steps from experiments/red/ctxp/instances/margin1_n20.pg.
  - The two lower score levels supplied the gradient below margin 1.

## 4. Files
- experiments/red/tpp/tpclimb.py (score and climb), explain.py (side-by-side calls and key provenance), shrink.py.
- experiments/red/tpp/instances/tpp_viol_n22.pg and tpp_viol_n63.pg. Both are pinned in experiments/red/check.sh: sha1, and
  tp_score PLUS=1 = 1 violation in both orders.
