# N2 PRIO-ANNEAL: priority annealing (top-down coarsening) with warm-started strategy iteration (L-NEW; before code)

Status: PROPOSED (not implemented in box 1).

## Exact pseudocode
Input G, distinct priorities q_1 > q_2 > ... > q_k (after compression).
For t = 1..k: G_t = G with every priority below q_t replaced by 0 (an even priority below all kept ones), i.e. a cycle
whose top priority is below q_t counts as won by Even. G_k = G.
sigma := best-reward start on G_1. For t = 1..k: run switch-all SI with Vöge-Jurdziński valuations on G_t from sigma until
optimal; sigma := the result. Output: final sigma's regions and both strategies (verified as in N1).
Variant N2': replace "0" by alternating the default parity per phase (first Even, then Odd), to avoid a one-sided bias.

## Why new
S4 (DE8) restarted from a SUBGAME optimum; N2 restarts from the optimum of the same arena with coarser priorities, so the
top bits of the counter are already set when the low ones appear. No fleet lane anneals priorities in SI. Zielonka's
recursion also works top-down, but recomputes subgames rather than warm-starting one strategy on the whole arena.

## Barrier statement draft
As N1 for B1-B3, B9-B17. B8: inside in part (switch-all phases). Friedmann's counters set their bits by low-priority
cycle structure, so a coarsened phase may make all bits trivially decided and the final phase may replay the full count.

## Cheapest killer expected
switchallexp: its bits are encoded by priorities in a narrow band; the final phase sees almost the original game.
Second: tc (two counters), where Oink's FPI/ZLK die (B6).
