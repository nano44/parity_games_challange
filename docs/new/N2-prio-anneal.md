# N2 PRIO-ANNEAL: priority annealing (top-down coarsening) with warm-started strategy iteration (L-NEW; before code)

Status: DEAD END on data (box 3, 2026-10-18; commit f301bfb at 18:05Z, UTC); see the last section.

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

## Box 3: first implementation and kill (commit f301bfb, 18:05Z UTC)
Implementation: experiments/new/n2.py (pseudocode above; compression as compress.py) driving n2_si.cpp (verbatim vjfast copy +
one line printing Even's full strategy for warm starts). Every final solution: regions = Oink zlk, strategies verified.
- switchallexp (unpadded): total 10, 18, 27, 32, 37 (N = 1..5): compression merges the counter's priorities (box 1 confound).
- Padded switchallexp (experiments/new/gen_padsae.sh N: one isolated self-loop dummy per priority, so compression merges
  nothing): largest stage 6, 15, 34, 72, 148, 300, 604 switch-all iterations, total 11 ... 624 (N = 1..7, n = 50 ... 230).
  Pinned: experiments/new/instances/killer/padsae_N1..N7.pg, table padsae_n2.csv (sha1 per instance).
  At N = 5 the long stage is stage 86 of 93 (148 iterations); all others have <= 7.
Obstruction: coarsening sets the high bits first, but the stage that reveals the counter's low priorities starts from the
coarse optimum, and from there switch-all replays Friedmann's count. The deep-trap game (deeptrap_sae, padded) gives similar
counts (28, 50, 90 total for N = 2..4): the trap gadget is horizon-specific and plays no role for N2.
