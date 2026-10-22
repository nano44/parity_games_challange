# psolC: implementation map (L-ATTR, 2026-10-15, for the REFEREE's diff against the paper)
Source: M. Huth, J. H.-P. Kuo, N. Piterman, "Static analysis of parity games: alternating reachability under parity",
Imperial College London DTR 2015/4 (18 pp.), opened 2026-10-15 08:05Z from
https://www.doc.ic.ac.uk/research/technicalreports/2015/DTR15-4.pdf, sha256 a7b61fe3a72926a94a3019e34620339f38aa653fe8aeed9ab4210187763e9cd6
(the hash the Lead and L-LIT T11 give). Page numbers are the report's. Figures 1, 4, 6, 8 were read from the rendered pages
(pdftoppm) since pdftotext drops edges and owners. Implementation: experiments/attr/psolc.py (class PsolC).
Conventions: DTR is MIN-parity (p.3, "Player 0 wins play π iff min Inf(π) is even"); the implementation reads max-parity
(TARGET) and converts with c = M - pr, M = max pr rounded up to even (order reversed, parity kept; the map of psolq.py and
experiments/m2/avh.py). Player 0 = Even. "Game" below means the current residual game G (the set `alive` in the code).

## 1. Line map
| label | DTR text | psolc.py |
| --- | --- | --- |
| C1 | psolC(G): W = tryPlayer(G, 0); if W != {} return psolC(G \ W) (Fig. 5 p.9, lines 1-4) | `run()`: loop over p in (0, 1); on a non-empty D remove it and `break` to restart with p = 0 |
| C2 | else W = tryPlayer(G, 1); if W != {} return psolC(G \ W); else return G (Fig. 5 lines 5-11) | same loop, p = 1; if neither player yields anything the loop ends and `alive` is the returned residual |
| C3 | tryPlayer(G, p): X = fixedpoint(G, {v in V : c(v)%2 = p}, p); if X != {} return Attr_p[G, X] else {} (Fig. 5 lines 13-16) | `try_player()`: `fixedpoint(alive, {v : c[v]%2 == p}, p)`, then `attr(alive, X, p)` |
| C4 | fixedpoint(G, X, p): W = V; repeat { X = X ∩ W; W = X ∩ Wr_p(G, X) } until X ⊆ W; return X (Fig. 5 lines 18-22) | `fixedpoint()`: W = X ∩ Wr_p computed by `wr_in_X`; if X ⊆ W return X, else X = X ∩ W and repeat; X = {} returns {} (Wr of the empty set is not defined in DTR, Def. 1 asks X non-empty; the loop would set W = {} and stop) |
| C5 | Attr_p[G, X]: the standard attractor (p.4, "see e.g. Definition 1 in [13]") | `attr()`: worklist attractor in the subgame `alive`, X included |
| C6 | Definition 1 (p.4): p wins play π for reaching (X, p) under parity iff some j > 0 has v_j in X and min{c(v_i) : 0 <= i <= j}%2 = p | encoded through Definition 2 and Theorem 1, below; the minimum includes c(v_0) (see A1) |
| C7 | Definition 2 (p.5): G^p_X on V x C(G)_⊥, owner of (v, l) = owner of v; edges (1): ((v,⊥),(v', min(c(v), c(v')))) for (v,v') in E; ((v,l),(v', min(l, c(v')))) for (v,v') in E, l in C(G), and (v not in X or l%2 != p) | `wr_in_X()`: forward closure from X x {⊥}: from (v, ⊥) the successor record is min(c[v], c[w]); from (v, l) it is min(l, c[w]); a node (v, l) with l != ⊥, v in X, l%2 == p has no outgoing edges (dead end, p.5 "dead ends ... are target nodes") |
| C8 | Theorem 1 (p.6): Z = X x {c in C(G) : c%2 = p}; W = {v : (v, ⊥) in Attr_p(G^p_X, Z)} is Wr_p(G, X) | `wr_in_X()`: A = attractor of Z for p on the product (p's node: some successor in A; opponent's node: all successors in A, counted over the explored successors); returns {x in X : (x, ⊥) in A} |
| C9 | Fig. 5 caption (p.9): "only X ∩ Wr_p(G, X) needs to be computed ... only constructing nodes and edges in G^p_X that are reachable from X x {⊥} in the non-alternating sense" | `wr_in_X()` builds exactly the forward-reachable part from X x {⊥} and only tests (x, ⊥) for x in X; attractor membership of a node depends only on the nodes reachable from it, so this is exact |
| C10 | edges of G restricted to the residual game (G \ W is the subgame on the remaining nodes, "residual instances" Thm 2 p.8) | all successor scans use `w in alive` |
| C11 | Thm 2 (p.8): time O(\|E\|·\|C(G)\|·\|V\|^2) | not asserted by the code; `stats` counts Wr computations and product nodes; C(G) is the colour set of the residual game as in Def. 2 (the record l ranges over colours actually produced by the min, a subset of C(G)) |
| S | strategies: DTR gives none that are positional (Thm 3 p.9: finite memory needed in general; Question 1 p.10 open) | `positional_strategies()`: a positional winning strategy on each decided region D = Attr_p[G, X] is obtained by solving the subgame induced by D with the harness Zielonka (default) or Oink (`--oink`), asserting that the subgame solver agrees that p wins all of D; required by TARGET section 5 (D2 change 5), checked by harness verify.py. This is a verification aid outside psolC and outside its cost bound; it is MY construction, not the paper's |

## 2. Ambiguities and readings (for the REFEREE)
- A1 (start colour). Definition 1 takes the minimum over 0 <= i <= j, i.e. including the colour of the start node v_0,
  and Definition 2's first edge line records min(c(v), c(v')) from (v, ⊥). The worked Example 3 (pp.10-11, Fig. 6)
  contradicts this at its step (ii): it says v4 (colour 0) is lost "as player 1 can move from [v4] to node v0 (which is
  no longer in X) and then play as for the initial X to get minimal color 1"; with c(v4) = 0 included, every reach of X
  from v4 has minimum 0 and v4 is won. The implementation follows the definitions (literal reading); the switch
  `exclude_start=True` (`--exclude-start`) implements the example's reading (minimum over 0 < i <= j). The outcome on
  Fig. 6 is the same under both (psolC solves nothing); the two readings differ elsewhere: 26 of the 41,440 canonical
  3-vertex games are solved completely by the literal reading and not by the example's reading (A3-psolC-results.md).
  Both readings are sound (Lemma 2's proof works for either). The literal reading is the stronger solver.
- A2 (empty X). fixedpoint may reach X = {}; Wr_p(G, {}) is undefined (Def. 1 asks X non-empty). The code returns {} at once.
- A3 (order of players). Fig. 5 tries player 0 first and restarts from player 0 after every removal; implemented so.
  DTR does not discuss order independence for psolC (Thm 4's proof cites [13] Thm 5 for psolB only).
- A4 (colour set C(G) in the residual). Def. 2 uses C(G) of the game at hand; the implementation's records are the minima
  that actually occur, which lie in C(residual). No difference for Wr.
- A5 (the recursion "psolC(G \ W)"). G \ W is the subgame on V \ W with the induced edges; every remaining vertex keeps a
  successor because W is a p-attractor (complement of an attractor is a trap, hence a subgame).

## 3. Validation (experiments/attr/a3_validate.py, part of check.sh)
| DTR item | expected | implementation |
| --- | --- | --- |
| Example 1 / Fig. 1 (p.4) and Thm 3 (p.9): W_0 = V; Y = V^0 = {v0, v2} is the gfp of F^0_G | psolC solves all three vertices for Even in one step with gfp {v0, v2} | matches (instances/dtr_fig1.pg) |
| Example 2 / Fig. 4 (p.8, p.10): gfp of F^0_G is {v0, v1, v3, v5}, Attr_0 = V, solved completely | one decision, gfp {v0,v1,v3,v5}, all 6 vertices Even | matches (instances/dtr_fig4.pg) |
| Example 3 / Fig. 6 (pp.10-11): psolC solves no node; X sequence V\{v1} -> {v2..v6} -> {v2,v3,v6} -> {v2,v6} -> {v6} -> {} | nothing decided; the printed sequence under the literal reading is V\{v1} -> {v2,v3,v4,v5,v6} -> {v2,v3,v4,v6} -> {v2,v3,v6} -> {v2,v6} -> {v6} -> {} (A1); under `--exclude-start` exactly DTR's sequence | matches on the outcome; A1 on the trace (instances/dtr_fig6.pg) |
| Fig. 8 (p.12) = HKP arXiv 1405.0386 Fig. 6 (bench/hkp_fig6.pg): gfp of F^0_G is {v0, v4, v7}, solved completely; psolQ solves nothing | one decision, gfp {v0,v4,v7}, all 8 vertices Even; psolq.py: undecided | matches |
| Thm 4 (p.12): every node psolB decides, psolC decides | checked per node on every enumerated game (a3_exhaustive.py, column thm4) | holds on all n <= 4 canonical games (see results) |
Soundness against Zielonka on every enumerated and random game; strategies verified by harness verify.py on the decided
regions (a1lib.check_partial) wherever produced.
