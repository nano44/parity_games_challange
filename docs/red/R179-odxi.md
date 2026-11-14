# R179 Ξ-changes at ODIFF vertices inside real N5 FL runs exist and are easy to make: odxi_min_n12 (one Odd choice vertex, ODIFF 1, n 12; the Ξ-cycle through o is broken by a W-flat move), odxi_lasso_n13 (o off its own Ξ-cycle), odxi_many_n32 (43 such changes in 8 FL transitions, 24 of them inside a run past its first transition); the 813-pair corpus has 0 (L-RED successor 42)
Started 2026-11-01 12:56Z (Lead queued R179 12:35Z, date -u). Brief: «find one real N5 FL run (not the idealised model) with ≥ 1 Ξ-change
at an ODIFF vertex. The 813-pair corpus has 0. L-NEW 46 box 133 tries to prove at the same time that it cannot happen, or happens O(1)
times. Pins as usual.» Labels: DATA, READING. Not a TARGET.md claim. G-N5-TIME stays OPEN. Not a kill: every run here is short.

## 0. Answer
- Yes. Three pinned games, each with N5's own run from the default S3 start (written out).
- Definitions (red/r179/odxi.py):
  - An FL transition j: no fallback at j; τ_j = τ_(j−1); σ̄_j = σ̄_(j−1); σ_j ≠ σ_(j−1); and W_j = W_(j−1) at every vertex (W = the
    valuation against τ_(j−1)).
  - An ODIFF vertex o: Odd with σ̄(o) ≠ τ(o).
  - A Ξ-change: Ξ_j(o) ≠ Ξ_(j−1)(o).
- Independent re-check (red/r179/lassock.py): W and Ξ recomputed without si.py, as lasso valuations of the functional graphs
  σ + τ and σ + σ̄ (σ, τ, σ̄ taken from N5's run). The counts are identical.

| pin | sha1 (12) | n | Odd choice vertices | K | FL transitions (runs) | max ODIFF | Ξ-changes at ODIFF vertices | o on its Ξ-cycle / lasso | at a run's first transition / later |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| odxi_min_n12 | 51661a75a4ec | 12 | 1 (𝒞^1O) | 2 | 1 (1) | 1 | 1 | 1 / 0 | 1 / 0 |
| odxi_lasso_n13 | 5cf187982d72 | 13 | 2 | 4 | 1 (1) | 2 | 1 | 0 / 1 | 1 / 0 |
| odxi_many_n32 | 42094483eefd | 32 | 12 | 26 | 8 (3, 3, 2) | 12 | 43 | 0 / 43 | 19 / 24 |

- Each pin: startck OK; Oink 8fbf0a7 --zlk + verify = N5's regions, verify of N5's strategies OK (oinkcmp «OINK OK»); --tl + verify
  exit 0; xeng (n5b) state sequences identical.
- Corpus (red/r179/runcorp.sh on the 813 distinct pairs, RESULTS Erratum E-1, c_corpus.txt, 0 errors): 37 FL transitions, 0 Ξ-changes
  at ODIFF vertices. That agrees with the Lead's / L-NEW's count. The corpus never produced the case; the climb (red/r179/climb179.py,
  score 1000·XICH + 10·FL + K, seeded from u23sw64_n32 / u2flat73_n32) finds it within a few thousand mutations. The small pins come
  from shrink.py (greedy vertex and edge deletion keeping XICH ≥ 1).

## 1. The n = 12 instance (READING of its trace)
- Odd 10 (priority 12) has edges 7 and 8. τ(10) = 8 and σ̄(10) = 7 at every state: ODIFF 1, and I_τ = ∅ throughout, so this is a
  𝒞^1O game.
- Even 7 (priority 16) has options 2 and 10; σ_0(7) = 10.
- State 0:
  - 10's Ξ-play closes the cycle 10 → 7 → 10 with cycle node 7 (even): Ξ(10) = (7, ∅, 1).
  - Odd prefers it: the τ-side reaches cycle node 5 (priority 30, even), which is better for Even.
- Transition 1 (I_σ = {(7, 2)}, no fallback): 7 moves 10 → 2.
  - W-flat: W(7) = (5, ∅, 6) by either option, an exact length tie at an even W-cycle node, so TB-even chooses.
  - Ξ-improving, because it breaks Odd's cheap cycle.
  - W is unchanged everywhere, so this is an FL transition.
  - Ξ(10) changes to (5, ∅, 7). σ̄(10) stays 7, because Odd still prefers the longer route to the even cycle node 5.
- Transition 2 is W-strict (6 moves 9 → 3), and the run ends at K = 2.
- So the anchor's Ξ changes because a W-tied mover sits on o's own Ξ-cycle. In odxi_lasso_n13 o is not on its Ξ-cycle: the change
  is in the path set (the weight 296 → 120 at the same cycle node 8 and the same length).
- In odxi_many_n32 every change is of the lasso type, and 24 of the 43 happen at an FL transition whose predecessor is also FL.

## 2. What this means (READING)
- For L-NEW 46 box 133: «cannot happen» is false. The data stop well short of answering «O(1) times», per run or per window.
  - The largest count here is 43 Ξ-changes in 8 FL transitions (n 32, ODIFF up to 12), i.e. several ODIFF vertices change together.
  - The longest FL run is 3.
  - So this is no growth evidence. FL-ANCHOR's (n + m)(1 + changes) bound is not violated; it simply has to count these changes.
- The natural next measurement (not done): Ξ-changes at ODIFF vertices per FL run against n, on climbs that score XICH per run.

## 3. Files and checks (experiments/red/r179/)
- odxi.py (count), lassock.py (independent re-check), classify.py, climb179.py, shrink.py, runcorp.sh + c_corpus.txt.
- instances/ (three pins, default starts, pins.sha1); out/ (climb outputs).
- check.sh block «R179»: pins, odxi and lassock lines for all three, xeng and oinkcmp on odxi_min_n12.
