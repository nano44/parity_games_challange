# TARGET v1.0 (approved by the owner 2026-10-14, ruling D2; only the owner changes this file)

Status: FROZEN at v1.0. History: v0.1 drafted by the Lead 2026-10-14; v1.0 = v0.1 plus the five changes of D2 (docs/DECISIONS.md).

## 1. Objects
- A parity game is G = (V, V_E, V_O, E, pr) with V finite, V = V_E ⊔ V_O (Even's and Odd's vertices),
  E ⊆ V × V, every vertex has at least one successor (self-loops allowed), and pr : V → {0, 1, ..., n}.
  n = |V|, m = |E|, d = |pr(V)| ≤ n + 1. Priorities sit on vertices.
- Input encoding: n, the owner bit of each vertex, pr(v) in binary, and the edge list. Input length is Θ((n + m) log n).
  (Games with arbitrary natural priorities are first compressed to {0..n} by sorting, preserving order and parity; this
  costs O(n log n) and is part of any claimed algorithm.)
- A play is an infinite path v0 v1 v2 ... following E. Max-parity: Even wins the play iff
  max{ p : pr(v_i) = p for infinitely many i } is even; otherwise Odd wins.
- A strategy for a player maps every finite play ending in that player's vertex to a successor. Strategies are general
  (history-dependent); positional determinacy is a theorem that may be used, not a definition.
- W_E(G) = vertices from which Even has a strategy winning every consistent play; W_O(G) likewise for Odd.
  By determinacy W_E ⊔ W_O = V.

## 2. The target statement (M4)
There is a deterministic algorithm A and a polynomial p such that for every parity game G, A on input G halts within
p(n + m) steps and outputs the pair (W_E(G), W_O(G)).

## 3. Model of computation
- Word RAM with words of O(log(n + m)) bits; equivalently (up to polynomial factors) a multitape Turing machine on the encoding above.
- Arithmetic on numbers longer than one word costs its bit complexity. An algorithm whose analysis gives unit cost to
  numbers of unbounded size (for example mean-payoff weights n^d) does not meet the target.
- The target requires the regions: positional winning strategies follow from a region oracle with polynomially many calls.
  Every implementation entering the gauntlet must nevertheless also output positional strategies (section 5, D2 change 5).

## 4. What does not count as M4 (may count as M3 if new against the literature map)
- Polynomial only on a restricted class (bounded d, treewidth, Strahler/register number, ...).
- Polynomial in n + m with d treated as a constant (already known: FPT in d).
- Any bound that hides a quasi-polynomial or exponential term, or a pseudo-polynomial term in numbers the algorithm builds.
- Correctness or running time resting on an unproved conjecture, an empirical observation, or a "clearly".

## 4b. M4-R (D2 change 4)
A randomized algorithm that always outputs the correct (W_E, W_O) (Las Vegas) and whose expected running time on every
input is at most p(n + m) is labelled M4-R, not M3, runs the same gauntlet, and is reported to the owner at once like an M4 claim.

## 5. Gauntlet for any algorithm claim (owner's text, verbatim)
1. Exact pseudocode in the lane notebook and one implementation.
2. It agrees with Zielonka on 10,000 random games of varied sizes and on every hard family; runtime growth is plotted
   and recorded. A second independent implementation follows only if the first survives.
3. A barrier statement: which known lower-bound frameworks it lies outside, and why. L-LIT signs off.
4. Written correctness and running-time proofs, double-refereed with every gap listed. A claim presented as M4 also needs
   its correctness formalized in Lean against TARGET.md (no sorry, allowed axioms only).
5. CHECKER passes on the exact commit, then I am told before anything else happens.
Only then does it enter docs/RESULTS.md, labelled formalized or refereed-only.
Owner addition (D2 change 5), verbatim: "every implementation also outputs positional strategies, and L-COMP verifies them on every
test game."

## 6. Lean form of the statement (to be written by L-FORMAL, then frozen here on owner approval)
- Formalized: correctness only. `theorem solve_correct : ∀ (G : ParityGame) (v : G.V), v ∈ (solve G).1 ↔ EvenWins G v`,
  and the same for `(solve G).2` and `OddWins`, where `EvenWins`/`OddWins` quantify over general strategies and infinite plays
  as in section 1, and `solve` is the claimed algorithm written as a Lean function.
- Allowed axioms: propext, Classical.choice, Quot.sound. No sorry, no new axioms, no `implemented_by`/`extern` in the proof path.
- Running time: proved in prose and double-refereed; a Lean step-count bound is not required (7c).
- Implementation match (D2 change 2): the Lean `solve` must implement exactly the pseudocode whose running time is analysed.
  The REFEREE signs a line-by-line correspondence between the Lean `solve` and that pseudocode; the CHECKER diffs it on the exact commit.
- Statement drift check: the CHECKER diffs the Lean definitions of ParityGame, EvenWins, OddWins and the theorem statement
  against this section word for word.

## 7. Owner choices (resolved by D2)
a. Approved with change 1: priorities in {0..n}, d ≤ n + 1, compression charged to the algorithm (section 1).
b. Changed: Las Vegas expected-polynomial algorithms are M4-R, reported at once like M4 (section 4b).
c. Approved: Lean covers correctness only; running time is refereed-only (section 6), matching the gauntlet's wording.
d. Approved: winning regions only; strategies optional (section 3).
e. Approved: M3 partial results must each be stated as a precise theorem in this file's vocabulary before work on the proof starts,
   and are checked for novelty against the literature map by L-LIT.
