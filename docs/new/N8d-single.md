# N8d: Koh-Loho tree strategy iteration (perfect tree) with a SINGLE-SWITCH pivot rule (L-NEW successor 5, Opus 5.5; box 15)
Lead 03:16Z 2026-10-23 (date -u). Machinery: experiments/new/kl/kl.py unchanged (its §0 fidelity table in N8a-kohloho.md applies to every
function reused); new code experiments/new/kl/kl_single.py (only the pivot rule is new; map in §1).

## 0. Rules (FROZEN at 2026-10-23 03:21Z by date -u, before any N8d run; changes only in new sections)
Algorithm 1 of Koh-Loho (arXiv 2108.13338 §3) with line 5 "Pivot to a strategy τ′ by selecting admissible arc(s)" restricted to ONE arc:
- R1 (lowest index): among the Odd nodes that have at least one admissible arc (an Odd arc violated w.r.t. µ, §3), take the one with the
  smallest node id; switch it to its admissible arc with the LARGEST Tighten(µ, vw) (⊤ largest; ties: smallest successor id).
- R2 (random node): the same, but the node is drawn uniformly at random among the Odd nodes with an admissible arc, by
  random.Random(seed) created at the start of each Algorithm 1 run (primal and dual runs each start a fresh generator with the same seed);
  seed 1 for the bench, seeds 2-3 as robustness checks. The arc is again the largest-Tighten admissible arc.
Both rules switch exactly one arc per iteration, so Algorithm 1's invariants (no loose arcs in G_τ; µ feasible in G_τ after the least-
fixed-point step) hold as in §3 of the paper, and Theorem 3.1 (correctness, termination ≤ n·|L(T)| iterations) applies unchanged.
Why tree labels might differ from the VJ/discounted single-switch lower bounds (Friedmann LMCS 2011, B8; Avis-Friedmann 1305.3944,
single-switch round-robin; DLMM 2512.16684, index rules, B9): those constructions are for valuations that are a FUNCTION of the current
strategy, so a run is a walk in the strategy order. Koh-Loho's µ is the least fixed point ABOVE the previous µ: it depends on the history,
strategies may recur (§3), and the progress measure is µ, not the strategy. R53 §6 (L-RED) observed that on the H_k family one switch
closes the odd cycle and the least fixed point then jumps to ⊤, whereas switch-all keeps the cycle open while counting. That is the only
reason to expect a difference; there is no argument that single-switch avoids the crawl (a crawl needs only that SOME sequence of single
admissible switches keeps an odd cycle open, and the rule chooses which).
Measure: Algorithm 1 iterations (pivots), primal and dual; against n per family; fitted exponent where it grows.

## 1. Code ↔ paper (new functions only)
| kl_single.py | paper | note |
| --- | --- | --- |
| `rule_r1`, `rule_r2` | Algorithm 1 line 5 (pivot rule) | admissible arc = violated arc of an Odd node (§3); Tighten as in kl.py (§2.2) |
| `strategy_iteration` | Algorithm 1 | copy of kl.strategy_iteration with the rule passed as a function; τ_1 = first successor as in kl.py |
| `solve` | Thm 2.3 + dual game | identical to kl.solve |

## 2. Bench
(filled after the runs)
