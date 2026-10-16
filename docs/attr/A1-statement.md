# A1 statement: Strahler threshold of psolQ and of arXiv 2511.03752 Algorithm 1 (L-ATTR, written before computation)
Written 2026-10-14 22:15Z (citation line numbers corrected 22:16Z), before any program in experiments/attr/ was run (TARGET.md section 7e). Vocabulary: TARGET.md
section 1 (max-parity, G = (V, V_E, V_O, E, pr), W_E, W_O). Sources opened by L-ATTR, with numbers, are in notes/L-ATTR.md.
Text marked "L-ATTR reading" is my fixing of a convention the source leaves implicit; everything else is the source's.

## 1. Sources and their numbering (as opened)
- DJT: L. Daviaud, M. Jurdzinski, K. S. Thejaswini, "The Strahler number of a parity game", arXiv 2003.08627 (v2 e-print, LaTeX
  source, files tuning.tex = section 2, coda.tex = section 6; shared theorem counter). Section 2: parity game, trap, dominion,
  attractor, Steven d-attractor decomposition, tree of a decomposition, Strahler number of a tree, of a decomposition, of a game.
  Proposition 1 (decomposition of a trap gives a dominion), Theorem 2 (positional determinacy via decompositions),
  Proposition 3 (Str(T) <= h and Str(T) <= floor(lg n)+1 for an (n,h)-small tree), Proposition 4 (tree of a decomposition of an
  (n,d)-small game is (n, ceil(d/2)+1)-small), Lemma 7 and Theorem 8 (Strahler number = Lehtinen number), Theorem 32 (games of
  Strahler number k solved in time n^{O(1)} (d/2k)^k, polynomial when k lg(d/k) = O(log n)), Remark 33.
- HKP: M. Huth, J. H. Kuo, N. Piterman, "Fatal Attractors in Parity Games: Building Blocks for Partial Solvers" (title per the arXiv abs page and
  archiv.tex:46), arXiv 1405.0386v2 (LaTeX source archiv.tex). MIN-parity (archiv.tex:366-367: "Player 0 wins play r iff min Inf(r)
  is even"). Definition 1 (control predecessor, attractor), Definition 2 (trap), Definition 3 (monotone control predecessor
  and attractor MA^p(A, X, c)), Definition 4 (fatal attractor), Definition 6 (permissive monotone predecessor/attractor,
  equations (5)-(6), archiv.tex:936-950), Definition 7 (layeredAttr is fatal if X is a subset of it), Figure 5
  (layeredAttr and psolQ pseudocode, archiv.tex:966-1002), Theorem 4 (soundness of fatal layered attractors, archiv.tex:1060),
  Theorem 5(3) (psolQ runs in O(|V|^2 |E| |c|)), Theorem 7 (psolB solves Büchi games), Theorem 8 (psolB solves games whose
  SCCs have constant colour), Lemma 5 (psolB solves deterministic games; "easily modified" for psol and psolQ), Example 6 and
  Figure 6 (8-vertex 1-player game "modified by neither psol, psolB nor psolQ", archiv.tex:1154-1200), Figure 4(a),(b) and
  Example 5 (psol and psolB incomparable).
- AVH: R. van der Heijden, arXiv 2511.03752v1 (e-print main.tex, sha256 9840db37...3f8b, the same file L-COMP opened), Algorithm 1
  (main.tex:370-395), as implemented in experiments/m2/avh.py (trunk 209865a) following notes/L-COMP.md "M2 pseudocode",
  which the REFEREE found faithful (docs/decisions/M2-arxiv-2511.03752.md, AM1-AM9). I do not re-derive it; I fix the
  implementation as the object.

## 2. Definitions fixed for A1
D1 (attractor decomposition; DJT section 2, max-parity, TARGET vocabulary). Let d be even and pr(V) <= d. A Steven
(= Even) d-attractor decomposition of G is H = <A, (S_1, H_1, A_1), ..., (S_l, H_l, A_l)> with: A = Attr_E(G, pr^{-1}(d));
G_1 = G \ A; for i = 1..l: S_i a non-empty trap for Odd in G_i with pr(S_i) <= d-2, H_i an Even (d-2)-attractor decomposition
of G ∩ S_i, A_i = Attr_E(G_i, S_i), G_{i+1} = G_i \ A_i; and G_{l+1} empty. If d = 0 then l = 0. Odd decompositions: swap
the players and take d odd. Tree T_H = <> if l = 0, else <T_{H_1}, ..., T_{H_l}>. Strahler number of a tree (DJT section 2):
Str(<>) = 1; Str(<T_1..T_l>) = m if exactly one child has Strahler number m = max_i Str(T_i), else m+1.
D2 (Strahler number of a game; DJT section 2, last paragraph). Str(G) = max(Str_E(W_E), Str_O(W_O)), where Str_E(W_E) is the
minimum of Str(T_H) over all Even d-attractor decompositions H of G ∩ W_E, and dually for Odd.
L-ATTR reading (D2a): d is the least even number >= max pr(V) for Even and the least odd number >= max pr(V) for Odd
(DJT define decompositions for "(n,d)-small" games with d given; the minimal d is the natural one). The empty dominion has
the decomposition <A = {}> with l = 0, tree <>, Strahler number 1; so Str(G) >= 1 for every G, and Str(G) <= floor(lg n)+1
(DJT Prop. 3) and Str(G) <= ceil(d/2)+1 (DJT Prop. 4). Whether a larger d can lower the minimum is checked empirically
(section 5, step 4); if it can, D2a is replaced by the minimum over all admissible d and the change is recorded here.
D3 (psolQ; HKP Fig. 5, Defs 6-7). Run on the min-parity game c = M - pr with M = max pr(V) rounded up to even (order reversed,
parity kept; the same map as experiments/m2/avh.py and bench/make_hkp.py). For player p, colour c, node sets A, X:
  PMpred_p(A, X, c) = {v in V_p : (c(v) >= c or v in X) and v.E ∩ (A ∪ X) != {}} ∪ {v in V_{1-p} : (c(v) >= c or v in X) and v.E ⊆ A ∪ X};
  PMAttr_p(X, c) = mu Z. PMpred_p(Z, X, c)                                                   (HKP Def. 6, eqs (5)-(6); the target X is
  external: a node of X is in PMAttr only if attracted to X in >= 1 move, archiv.tex:532-535).
  layeredAttr(G, p, X) [all nodes of X have parity p]: A = {}; b = max c(X); for d = p, p+2, ..., b: Y = {v in X : c(v) <= d};
  A = PMAttr_p(A ∪ Y, d); return A.
  psolQ(G): for colours b in ascending order: X = {v : c(v) <= b and c(v) % 2 = b % 2}; cache = {}; while X != {} and X != cache:
  cache = X; W = layeredAttr(G, b % 2, X); if X ⊆ W: return psolQ(G \ Attr_{b%2}(G, W)) [the removed set is decided for
  player b % 2]; else X = X ∩ W. After the loop return G (the undecided residual).
  L-ATTR readings: (D3a) "colours b" ranges over the colours occurring in the current G (HKP Thm 5(3) counts "the loop on b" by |c|);
  (D3b) strategies, required by TARGET section 5 (D2 change 5) but not in HKP's pseudocode (archiv.tex:635-638 omit them):
  on W, every v in V_p gets the successor that witnessed its entry into PMAttr (a node of A_{d-2} ∪ Y_d ∪ A_{d,i-1}, in the
  notation of HKP's proof of Thm 4); on Attr_p(G, W) \ W the attractor strategy; verify.py checks every output.
  "psolQ solves G completely" = the final residual is empty (HKP's class Solved, Def. 8, transferred from psolB to psolQ).
D4 (Algorithm 1 of AVH = avh.py). Input max-parity; internally min-parity as D3; pre-routine P1-P2 (self-loops), operator
A(G,d) by D1-D4 of the M2 pseudocode, main loop lines 1-12, strategies S1-S2, STUCK guard. Outcomes on a game G:
SOLVED (terminates, regions equal Zielonka's, strategies pass verify.py), WRONG (regions differ from Zielonka's or
strategies fail), STUCK (exit 3: both A(G, dbar) and A(G, dhat) empty with V != {}, the vertices left are undecided).

## 3. The questions
For a solver P in {psolQ, Alg1} let k(P) = sup { k in N : every parity game G with Str(G) <= k is solved completely and
correctly by P } (sup of the empty set is 0; "correctly" is automatic for psolQ by HKP Thm 4 and is checked anyway).
- Q1: k(psolQ).  - Q2: k(Alg1).
- Q3: for each P, a game G with Str(G) = k(P)+1 on which P fails (psolQ: non-empty residual; Alg1: STUCK or WRONG), minimal first
  in n = |V| and then in m = |E| over all such games with priorities in {0..n} (TARGET section 1), with the minimality established
  by exhaustive enumeration up to that n (canonical forms, section 5), not by sampling.
Since Str(G) >= 1 for every G (D2a), k(P) = 0 means: P already fails on a game of Strahler number 1, i.e. one whose two
dominions both have chain-shaped (branching-free) attractor decompositions.

## 4. Calibration (owner's and L-LIT's conditions)
- TARGET section 4: a polynomial solver complete on "Strahler <= k" is M3 at most, and DJT Thm 32 already makes that class
  polynomial for every constant k (indeed for k lg(d/k) = O(log n)). A positive answer k(P) >= 1 would therefore be a
  statement about the solver P, not about the class; novelty is then "P, a psolB-type fatal-attractor solver with no
  recursion and no progress measure, is complete on Strahler <= k", to be checked by L-LIT against HKP Thm 7-8 and DJT.
- A negative answer (k(P) = 0) is still a result for this lane: it says that the Strahler number (branching of
  decompositions, the parameter behind the quasi-polynomial bounds) does not measure what fatal-attractor solvers miss,
  and the minimal instance of Q3 names what they miss. It explains the M2 refutation structurally (L-LIT rank-3 deliverable:
  "explains WHY the claim fails").
- No completeness claim for a natural class will be made from data alone; a proof is listed as NEEDS.
- Hand computation recorded before running anything (notes/L-ATTR.md, "Things only I know"): under D1-D2a, HKP Fig. 6
  (8 vertices, Even wins all, HKP say psolQ leaves it untouched) has an Even decomposition with tree <<>> and the Odd dominion
  is empty, so Str = 1; the M2 counterexample ce1_4v.pg likewise has tree <<>>, Str = 1. If the programs confirm both, then
  k(psolQ) = k(Alg1) = 0 and Q3 is about the minimal Strahler-1 failures. This expectation is recorded so that the
  computation cannot be accused of being fitted to it.

## 5. Computation plan (all in experiments/attr/, every output checked by experiments/harness/verify.py)
1. psolq.py: D3 verbatim, with the HKP line numbers in the notebook pseudocode; CLI compatible with compare.py on games it
   solves completely (exit 3 "UNDECIDED k" otherwise, like avh.py's STUCK).
2. strahler.py: exact Str(G) for small games by dynamic programming over subsets: regions from harness zielonka.py (cross-checked
   with brute_force for n <= 6); f(R, d, player) = minimal Strahler number over all d-decompositions of the subgame R, computed by
   enumerating every trap S ⊆ G_i with the priority bound, recursing, and folding the children's minimal Strahler numbers with
   the tree rule (a child never gains from a non-minimal decomposition because Str(<T_1..T_l>) is monotone in each child).
3. Validation: HKP Fig. 6 (psolQ decides nothing, HKP Ex. 6), Fig. 4(a) and 4(b) (HKP Ex. 5 describes psol/psolB; psolQ's
   outcome is recorded), ce1_4v.pg and cex1/cex2 of M2 (Alg1 WRONG), 2000 seeded random games (psolQ sound, i.e. no vertex
   decided against Zielonka; Alg1 outcomes as in M2).
4. Exhaustive enumeration in canonical form: priorities matter only through their order and parity for both solvers and for Str
   (all three use priorities only via comparisons and parity), so each game is enumerated once per (owner vector, surjective
   rank map V -> {0..r-1}, parity bit per rank, successor sets); n <= 3 fully (all m), n = 4 by increasing m until the first
   failure of each solver, then the full m-class of the first failure; n = 4 fully if the time box allows. D2a's d-sensitivity
   checked on n <= 4: Str with d and d+2.
5. Random corpora (gen.py, n = 4..8, several seeds) and shrinking of every failure (delete a vertex / an edge while the
   failure and the Strahler number persist) as a second route to minimal instances; exhaustive data decide minimality.
6. Tabulate failures against Str, tree height, number of leaves, and HKP's known classes (Büchi, SCC-constant colour,
   deterministic, 1-player), to say what the minimal failures have in common.
Time box: 24 h from 22:07Z 2026-10-14. Dead ends and every failing instance go to notes/L-ATTR.md and experiments/attr/instances/.
