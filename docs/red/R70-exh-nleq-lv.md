# R70: exhaustive RISE-LAST search, NL=, level −1 fallbacks, fallbacks after a rise (L-RED successor 16, box 40; GO 2026-10-25 13:36Z, date -u)
Targets (Lead 13:36Z, 13:48Z, 13:53Z, 14:33Z, 14:56Z, 15:41Z):
- (1) EXHAUSTIVE small-n search for RISE-LAST: a COARSE_L(θ) change at an S4a step strictly between consecutive in-scope fallbacks of a
  scope run (the (Σ)-rise that P-N5-ENT's CYC-EV / TEV-FB / ENT-X need).
- (2) XSN-RUN exhaustively for n ≤ 12, if (1) finishes quickly.
- (3) L-SI succ. 6's CONJECTURE NL= (docs/si/N5-STR-box11.md §3; shape in N5-STR2-box11.md, sha1 b6ed9476).
- (4) In-scope THR fallbacks with M = −1 and (β) gates (docs/si/N5-LV-box11.md, sha1 407c5520; kill shape N5-LV3-box12.md §4,
  sha1 20ba05d7). Then P-N5-LV2's LV-NONE (≤ n·n_E + 1 r = −1 THR fallbacks per scope run) and SCOPE-FB (≤ 4·n·n_E + 3 S4c fallbacks
  per scope run) (docs/si/P-N5-LV2-box12.md, sha1 3b23a41f).
- (5) REFEREE-2's "Reachability" observation (R2-N5-ENT): after a rise that follows a fallback with r > L, the scope run has no further
  fallback.
𝒞^1O only: exactly one Odd vertex with out-degree > 1, asserted in every checker. Labels per L40. G-N5-TIME stays OPEN.

## 0. Result
- **NL= is FALSE (CANDIDATE until the Lead re-runs): nleq_cex_n48.pg**, sha1 e72e40343b33df295d5877ff29125b154e71949c. NL (ii)
  ("no leave") fails at an S4a step with r_j = L. L-SI's own nleq.py agrees. NJB's straddle stays OPEN. D_M ≤ 1 (P-N5-ENT, CONDITIONAL on
  (P)) is not affected.
- (1) Exhaustive, n ≤ 5: every target is VACUOUS. No run has two in-scope fallbacks with an S4a step between them, and no in-scope THR
  fallback exists at all (§2). The events start near n 11 (the smallest library instance with an in-scope fallback pair). Random n 6-12
  games never reach them.
- (2) XSN-RUN for n ≤ 12 exhaustively: NOT RUN (infeasible beyond n 5 with this enumeration; §3).
- (4) REFEREE-2's best_lv_9401 reproduces one (β)-fallback (7 (β) gates). LV-NONE / SCOPE-FB: no violation; max ratios in §5.
- (5) No fallback after a rise in a scope run (§6).

## 1. Tools (experiments/red/so/; written from the source texts)
- ex16.py: exhaustive driver.
  - Enumeration: my own re-implementation of L-COMP's stated canonical subset (exh.py docstring). It covers distinct priorities, ids in
    priority order, minimal values per parity pattern, every o position and owner pattern, Even out-degree ≤ K, forced Odd vertices
    optional, and o out-degree ≥ 2 (or exactly K).
  - Trace: my own copy of n5.py's loop from a start pair. It equals n5.run on 3,000 canonical games, and equals L-COMP's exh.trace_fb on
    2,712 random start pairs.
  - Exact prefilter for RISE-LAST: two Even fallbacks with none between, at least one S4a step between, and τ constant. The same
    prefilter is necessary for (5). Prefiltered runs get the scope-run check (H1 / H2 / H3, W, M, (Σ)).
  - Every run with an Even fallback also gets lv16 and nleq16.
- nleq16.py: NL (i)-(iii) at every in-scope S4a step after an in-scope fallback, L = M of the last one (≥ 0), with (h) at j and (A_j).
  It splits r_j > L (Lemma NL, PROVED: a sanity check) from r_j = L (NL=).
- lv16.py: in-scope THR / EQ fallbacks, M = −1 THR fallbacks, and the LV-SHAPE kinds α / β / γ per gate (LVX = a gate of none of them).
  Also CN-LAST at fallbacks without (β), (β) per scope run, and P-N5-LV2's LVNONE / SCOPEFB per scope run.
- rnd16.py: random scan. climb16.py modes: far / nleq / lv / lvn (plus the box-39 modes).
- Data: data16/ex/*.json.

## 2. Exhaustive tables (DATA, exact in the stated spaces)
| space | games | runs | max fallbacks / run | prefilter passes | in-scope THR fb | EQ fb | NL= steps | failures |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| n 3, all start pairs, full space | 9,600 | 48,600 | 1 | 0 | 0 | 276 | 0 | 0 |
| n 4, canonical start, full space | 4,828,736 | 4,828,736 | 1 | 0 | – | – | – | 0 |
| n 4, all start pairs, full space | 4,828,736 | 83,607,552 | 2 | 0 | 0 | 1,080,648 | 0 | 0 |
| n 5, canonical start, no forced Odd, Even out-deg ≤ 2, o out-deg 2 | 81,000,000 | 81,000,000 | 1 | 0 | 0 | 357,770 | 0 | 0 |

- "Full space" means every parity pattern, o position, owner pattern (Even with any non-empty successor set, or forced Odd), and every o
  successor set of size ≥ 2. The n 4 canonical row predates the lv / nleq columns.
- So at n ≤ 4 (every start) and on the n 5 subset there is no fallback pair inside a scope run and no in-scope THR fallback. RISE-LAST,
  the (Σ)-rise, (5), NL= and the LV targets are all vacuous there.
- Random scan (rnd16.py; 3,000 games × (canonical + 3 random start pairs) per n): n 6 / 8 / 10 / 12 have 0 prefilter passes and 0
  in-scope THR fallbacks (169-252 EQ fallbacks each).
- Smallest library instance with an in-scope fallback pair: n 11 (i1h_fts_best16, experiments/new/box22). An exhaustive search that
  reaches the events needs n ≈ 11, far beyond enumeration (n 5's full space is already ≈ 7·10^9 games).

## 3. XSN-RUN exhaustive (NOT RUN)
- n ≤ 12 exhaustively is infeasible with ex16's enumeration: n 5's full canonical space is already ≈ 7·10^9 games. Not attempted. R69 §3
  stands (climbed best 8 at n 10, margin 1).

## 4. NL= (L-SI succ. 6, CONJECTURE): FALSE (CANDIDATE)
(see §4 body below; filled at box end)

## 5. Level −1 fallbacks, LV-NONE, SCOPE-FB
(filled at box end)

## 6. Fallbacks after a rise (REFEREE-2 "Reachability")
(filled at box end)

## 7. Labels
(filled at box end)
