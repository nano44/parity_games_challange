# L-COMP notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
2026-10-14 20:00Z. M2 CLOSED as BROKEN by the Lead (18:36Z): CE1 (mine) plus an independent 4-vertex counterexample by the
REFEREE (claude/referee 936d47c, docs/referee/scratch/cex1-maxparity.pg) that breaks readings (a)-(d). No 10k run.
M1: 13 sweeps + READMEs pushed (4c0ae44); re-run with strategy checks in progress (run_all.sh); switch-all SI port
(pgsolver_si.py) confirms switchallexp blow-up (iterations double per N); run_si.sh sweep in progress.

## Queue
1. When the re-runs end: make_readmes.py (+ switchallexp-pgs / switchbestexp-pgs), update verdicts, push, report.
2. Port PGSolver switch-best SI (stratimpralgs/switch_globally_best.ml) for switchbestexp.
3. Low priority: add L-LIT's bench list (claude/l-lit a6c530f, docs/lit/2511.03752-position.md: exhaustive tiny
   games, Huth-Kuo-Piterman Fig. 6/4(a)/4(b) witnesses) as generic test families.

## M2 pseudocode
Source: arXiv 2511.03752v1, R. van der Heijden, "Attractors Is All You Need: Parity Games In Polynomial Time"
(submitted 2025-11-04). Opened 2026-10-14 as the LaTeX e-print (sha256 of e-print 4dc6c4b9...ee2e4; main.tex
9840db37...3f8b). Line numbers "tex:N" refer to that main.tex; the paper has no numbered equations. Theorem
numbering follows the paper's counter: Lemma 1 (tex:290), Theorem 2 (tex:322), Lemma 3 (tex:341), Lemma 4 (tex:397),
Theorem 5 (tex:404), Lemma 6 (tex:413), Theorem 7 (tex:421), Theorem 8 (tex:428); Algorithm 1 (tex:370-395).

### Conventions of the paper
- MIN-parity: "Even wins the play iff min{inf(pi)} is even" (Sec. 2, tex:274). TARGET.md is max-parity.
  Implementation maps a max-parity game with priorities 0..P to min-parity by rho'(v) = M - rho(v), M = P rounded up
  to even: order reversed, parity kept, so winning regions and strategies are unchanged. (Mine, not the paper's.)
- player(d) = Even if d even else Odd; par(d) = d mod 2 (tex:301). In A(G,d) the symbol O ("circle") is the player
  of d, O-bar the other (Theorem 2, tex:323: "priority d of player O, A(G,d) is an O-dominion").
- Attr as defined tex:280-286 (standard attractor, computed in the current game G).
- Subgame G \ U (tex:278).

### Pre-routine: self-loops (tex:297, Remark tex:335)
The paper assumes no self-loops and says they "can be removed as a pre-routine [friedmann_solving_2009]"
(doi:10.1007/978-3-642-04761-9_15, NOT opened: awaiting source). Reading used (from PGSolver d3cd624, Friedmann's
code: transformations.ml:15-24 remove_useless_self_cycles_inplace, specialsolve.ml:20-28 find_useful_self_cycles,
univsolve.ml:698-760 their use):
P1. For every v with (v,v) in E, rho(v) of parity NOT the owner's, and |E(v)| > 1: delete edge (v,v).
P2. For p in {Even, Odd}: S_p = {v : (v,v) in E, and (owner(v) = p and par(rho(v)) = p, or E(v) = {v} and par(rho(v)) = p)};
    X_p = p-Attr(G, S_p); W_p += X_p; strategy: v in S_p owned by p plays v->v, attractor strategy on X_p \ S_p;
    G = G \ X_p (Even first, then Odd on the remaining game, recomputing S_Odd there).
    (The "E(v) = {v}, wrong parity" case is my addition: PGSolver leaves such a self-loop in place.)
After P1-P2 no vertex of G has a self-loop (every remaining self-loop vertex was in S_Even or S_Odd or lost its loop).

### Definitions (Sec. 3, tex:301-318), for the current game G and a priority d, O = player(d)
D1. U_d(G) = { v : rho(v) <= d and par(rho(v)) = par(d) }                                     (tex:303)
D2. A*_d(G) = union over k in 0..d with par(k) != par(d) of { v in O-Attr(G, U_{k-1}(G)) : rho(v) = k }   (tex:304)
    (U_{-1} = empty set.)
D3. A'_d(G, A) = O-bar-Attr(G, { v in A \ (A*_d(G) u U_d(G)) : rho(v) < d })                 (tex:309)
D4. U^0 = U_d(G);  A^0 = O-Attr(G, U^0)                                                        (tex:314-315)
    U^{k+1} = U^k \ O-bar-Attr(G, (V \ A^k) u A'_d(G, A^k));  A^{k+1} = O-Attr(G, U^{k+1})     (tex:316-317)
    A(G,d) = intersection over k of A^k                                                         (tex:312)
    Computed by iterating until U^{k+1} = U^k (then every later A^k equals A^k).

### Algorithm 1 (tex:370-395), run on the game left after P1-P2
 1 n = |V|, m = |E|                                         (tex:374)
 2 D = ordered list of priorities (unused afterwards)        (tex:375)
 3 W_E, W_O = {}, {}                                         (tex:376)
 4 while V != {}:                                            (tex:377)
 5   dhat = max priority of G                                (tex:378)
 6   O = Even if dhat even else Odd                          (tex:379; the tex writes "d", read as dhat)
 7   dbar = max priority of O-bar in G                       (tex:380)
 8   compute A(G, dbar)  [an O-bar dominion by Theorem 2]    (tex:382)
 9   W_{O-bar} += A(G, dbar);  G = G \ A(G, dbar)            (tex:383-384)
10   if A(G, dbar) != {}: continue                           (tex:385-387)
11   compute A(G, dhat);  W_O += A(G, dhat);  G = G \ A(G, dhat)   (tex:389-391)
12 return (W_E, W_O)                                         (tex:393)
Implementation guard (mine): if in one iteration both A(G,dbar) and A(G,dhat) are empty and V != {}, stop and report
STUCK (Lemma 4, tex:397-402, says this cannot happen).

### Strategies (not in the paper; my construction, required by D2 change 5)
For a removed set A = A(G,d) = O-Attr(G, U) with U = U^k at the fixpoint:
S1. v in A \ U owned by O: the attractor strategy (a successor in the previous attractor layer).
S2. v in U owned by O: a successor in U if there is one; else a successor in A \ A'_d(G, A) (the case analysis
    in Theorem 2's proof, tex:328-330); else any successor in A (flagged in the log; the proof says it cannot occur).
Pieces are removed as O-attractors, so the remaining game is an O-trap and the per-piece strategies compose.
A failed strategy check therefore does not by itself refute the paper; a region mismatch does.

### Ambiguities (reading chosen; alternatives)
AM1 Parity convention: min-parity as written (tex:274). Alternative: the author meant max-parity (Algorithm 1 starts
    from the MAX priority, which in min-parity is the least significant one). Implementing max-parity instead would be
    a different algorithm; I implement min-parity as written and could add the max-parity variant as a probe.
AM2 Line 6 says "if d is even"; read d = dhat.
AM3 Line 7 when O-bar has no priority in G: reading A(G, dbar) = {} (skip to line 11). Alternative: undefined.
AM4 Self-loop pre-routine: see P1-P2 (cited source not opened; PGSolver's code used; forced wrong-parity self-loop
    vertex handled by me).
AM5 A(G,d) = intersection of the A^k (tex:312): since U^k decreases and Attr is monotone, A^k decreases; computed at
    the fixpoint of U. Alternative readings give the same set.
AM6 All attractors inside D2, D3, D4 are computed in the current G (whole remaining game), not inside A or U.
    Alternative: D3's attractor restricted to A. Chosen: G, as the formulas write "Attr(G, .)".
AM7 D3 uses strict rho(v) < d and excludes A* and U_d (as written).
AM8 Text references "line 12" for continue and "lines 8-10, 14-16" (tex:369, 408), numbering that counts the blank
    \[\] lines; my line numbers above are my own.
AM9 Lemma 3's proof sets D_{dbar} = D cap U_{dtilde} (tex:345), probably a typo for U_{dbreve}; no effect on the algorithm.

## Things only I know
- PGSolver (tcsprojects/pgsolver d3cd624) builds with apt OCaml 4.14 + dune 3.14 after two local edits
  ((lang dune 3.18)->3.14, drop maintenance_intent) in a dune workspace with tcslib 6778419,
  ocaml-sat-solvers 0264291, c-cube/ocaml-minisat aeb7776 (all cloned under experiments/hard-families/out/pgsolver,
  gitignored). Running the built generator.exe was refused by this session's permission classifier ("code from
  external"), so the generators are ported to Python instead; the owner can allow running it, then the port can
  be diffed against the original output.
- Oink rngame is seeded from std::random_device: not reproducible; keep the files, not the parameters.
- Oink mspm (8fbf0a7) is unsound: logic error at mspm.cpp:486 on 3 rngame games, and on one game a wrong answer
  that Oink's own verifier rejects ("loser can escape"). Instances: experiments/harness/regressions/mspm_*.pg.
  Exclude mspm from any "all solvers agree" claim.
- Oink's work counters are solver-specific (iterations, promotions, lifts, major iterations); compare across sizes
  of one solver, never across solvers.

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| github.com/trolando/oink @ 8fbf0a7 | solver list (README), generators src/tools/*.cpp, solution format src/game.cpp:459 | 2026-10-14 | code, not a paper |
| arXiv 2511.03752v1 (LaTeX e-print) | Sec. 2-3, Algorithm 1, Thm 2, Lemmas 3-4 (see M2 pseudocode) | 2026-10-14 | M2 subject |
| github.com/tcsprojects/pgsolver @ d3cd624 | generators recursiveladder.ml, policyiter/generators/*.ml; paritygame.ml conventions | 2026-10-14 | code, not a paper; papers awaiting source |

## Dead ends
- 2026-10-14 (M2 closed BROKEN by the Lead 18:36Z; REFEREE's independent counterexample breaks readings (a)-(d)): arXiv 2511.03752v1 Algorithm 1 as read in
  "M2 pseudocode" is incorrect. Obstruction: Theorem 2 (A(G,d) is a player(d)-dominion) fails; A'_d only removes
  vertices the opponent can force into lower-priority parts, but player(d) (here Odd) can dodge A' on a
  cycle that never returns to U^k, and that cycle can be won by the opponent. Instance: experiments/m2/counterexamples/ce1_4v.pg
  (4 vertices, all Odd's; Even wins all; the algorithm gives all to Odd via A(G,1) = V). Trace in that folder's README.
