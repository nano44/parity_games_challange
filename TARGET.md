# TARGET (DRAFT v0.1, awaiting owner approval; only the owner changes this file)

Status: DRAFT. No attack lane starts before the owner approves this file. Section 7 lists the choices the owner must confirm.

## 1. Objects
- A parity game is G = (V, V_E, V_O, E, pr) with V finite, V = V_E ⊔ V_O (Even's and Odd's vertices),
  E ⊆ V × V, every vertex has at least one successor (self-loops allowed), and pr : V → {0, 1, ..., n-1}.
  n = |V|, m = |E|, d = |pr(V)| ≤ n. Priorities sit on vertices.
- Input encoding: n, the owner bit of each vertex, pr(v) in binary, and the edge list. Input length is Θ((n + m) log n).
  (Games with arbitrary natural priorities are first compressed to {0..n-1} by sorting, preserving order and parity; this
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
- Output of regions suffices: positional winning strategies follow from a region oracle with polynomially many calls,
  but a claim that also outputs strategies is preferred because strategies are checkable in polynomial time.

## 4. What does not count as M4 (may count as M3 if new against the literature map)
- Polynomial only on a restricted class (bounded d, treewidth, Strahler/register number, ...).
- Polynomial in n + m with d treated as a constant (already known: FPT in d).
- Expected or high-probability polynomial time with randomness (Lead proposal: M3, flagged to the owner; see 7b).
- Any bound that hides a quasi-polynomial or exponential term, or a pseudo-polynomial term in numbers the algorithm builds.
- Correctness or running time resting on an unproved conjecture, an empirical observation, or a "clearly".

## 5. Gauntlet for any algorithm claim (owner's text, verbatim)
1. Exact pseudocode in the lane notebook and one implementation.
2. It agrees with Zielonka on 10,000 random games of varied sizes and on every hard family; runtime growth is plotted
   and recorded. A second independent implementation follows only if the first survives.
3. A barrier statement: which known lower-bound frameworks it lies outside, and why. L-LIT signs off.
4. Written correctness and running-time proofs, double-refereed with every gap listed. A claim presented as M4 also needs
   its correctness formalized in Lean against TARGET.md (no sorry, allowed axioms only).
5. CHECKER passes on the exact commit, then I am told before anything else happens.
Only then does it enter docs/RESULTS.md, labelled formalized or refereed-only.

## 6. Lean form of the statement (to be written by L-FORMAL, then frozen here on owner approval)
- Formalized: correctness only. `theorem solve_correct : ∀ (G : ParityGame) (v : G.V), v ∈ (solve G).1 ↔ EvenWins G v`,
  and the same for `(solve G).2` and `OddWins`, where `EvenWins`/`OddWins` quantify over general strategies and infinite plays
  as in section 1, and `solve` is the claimed algorithm written as a Lean function.
- Allowed axioms: propext, Classical.choice, Quot.sound. No sorry, no new axioms, no `implemented_by`/`extern` in the proof path.
- Running time: proved in prose and double-refereed; a Lean step-count bound is optional (Lead proposal: not required, 7c).
- Statement drift check: the CHECKER diffs the Lean definitions of ParityGame, EvenWins, OddWins and the theorem statement
  against this section word for word.

## 7. Choices for the owner to confirm
a. Priorities in {0..n-1} with the compression step charged to the algorithm (section 1). Alternative: arbitrary naturals, time polynomial in input length.
b. Randomized (Las Vegas, expected polynomial) algorithms: M3, not M4 (section 4).
c. Lean covers correctness only; running time is refereed-only (section 6), matching the gauntlet's wording.
d. Winning regions only; strategies optional (section 3).
e. M3 partial results must each be stated as a precise theorem in this file's vocabulary before work on the proof starts,
   and are checked for novelty against the literature map by L-LIT.
