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

## 4. NL= (L-SI succ. 6, CONJECTURE): FALSE (Lead re-run 15:52Z: confirmed)
- Statement checked: P-N5-CLS §5 Lemma NL (i)-(iii) with r_j > L weakened to r_j ≥ L. Setting: an in-phase S4a step j → j+1 of a scope
  run, after an in-scope fallback k0 (the last one before j), L = M_k0 ≥ 0, with (h) at j and (A_j).
- **DEAD END for NL=: nleq_cex_n48.pg**, sha1 e72e40343b33df295d5877ff29125b154e71949c, n 48, o = 0, canonical start.
  - Verified: n5 = n5b --mode spec 10/1, Oink zlk OK, strategies verified.
  - L-SI's unmodified experiments/si/tev/nleq.py gives TOTAL {'steps': 2, 'r_eq_L': 2, 'nl2_fail': 1} at (nlc.pg, nl2, 6, 47, 47).
  - Exact obstruction:
    - k0 = 4 is the only fallback, with L = M_4 = 47.
    - r = 47 = L at states 5-7. At the S4a step 6 → 7, (h) and (A_6) hold, and NL= (i) and (iii) hold.
    - Even vertex 40 (priority 17) is in R_6 with σ_6(40) = o, so its route {40} is low. It switches 40 → 9, with 9 ∈ F_6, and leaves R:
      NL (ii) fails.
    - This is a bypass to a FREE vertex (9). It is not N5-STR2 §2's (p, e*) shape (e* = τ(o) = 21). Vertex 17 switches 21 → 41 in
      the same step.
  - The nleq climb from njb_reabs65_n48 reached 33 such leaves in one game: nleq33_n48.pg, sha1
    a1ebd2e0e113ac0e616c89a7daec5bf044d57e6b; n5 = n5b 40/1, Oink zlk OK, strategies verified.
  - Consequence (N5-STR2 §2): NJB's straddling interval stays OPEN. D_M ≤ 1 (P-N5-ENT, CONDITIONAL on (P)) is unaffected.
- Sanity: Lemma NL (r_j > L) has 0 failures on every file and climb (nleq16 "GT" checks).

## 5. Level −1 THR fallbacks, (β) gates, LV-NONE, SCOPE-FB (DATA)
- Exhaustive n ≤ 5 (§2): no in-scope THR fallback at all, so (LV) is vacuous there.
- REFEREE-2's best_lv_9401.pg (sha1 4b74cd84, canonical start): lv16 finds 1 in-scope THR fallback with M = −1. Its 7 gates are all
  (β), it is a (β)-fallback, LVX 0. This reproduces R2-N5-LV §N-LV-3. best_lv_9402-9404 have no (LV) fallback from the canonical
  start. REFEREE-2's hits may use other start pairs; not checked.
- **Two (β)-fallbacks in one scope run** (the second outcome the Lead named at 13:53Z): beta2_n11.pg, sha1
  bdea2a2386741332d654005b81e5691cbf4dc9c5, n 11, o = 1, canonical start.
  - Verified: n5 = n5b --mode spec 4/2, Oink zlk OK, strategies verified.
  - Fallbacks at 0 and 1 are both in-scope THR with r = −1 and M = −1, and both are (β)-fallbacks (gate kinds: 3 β, 1 α). LVX 0, LVCN 0.
  - So the (β)-fallbacks of one scope run can number at least 2. P-N5-LV2's LV-NONE bound n·n_E + 1 = 67 is not threatened.
- lvn climbs (fitness: failures, max r = −1 THR fallbacks per scope run, max S4c fallbacks per scope run, (β)-fallbacks):

| seed | n | n_E | best r = −1 per run (LV-NONE bound) | best S4c per run (SCOPE-FB bound) | evaluations | instance |
| --- | --- | --- | --- | --- | --- | --- |
| best_lv_9401 | 11 | 6 | 2 (67) | 2 (267) | 2,210,397 | beta2_n11.pg |
| best_lv_9404 | 13 | 12 | 0 (157) | 8 (627) | 917,596 | s4c8_n13.pg (2cf723a7…; n5 = n5b 12/8, verified) |

- Library maxima are higher in absolute terms: rise_fb38_n48 has 37 in-scope S4c fallbacks in one scope run (n_E 45; bound 4·48·45 + 3 =
  8,643). Max ratio seen: SCOPE-FB about 8/627 at n 13; LV-NONE 2/67 at n 11. 0 LVNONE / SCOPEFB / LVX / LVCN failures.

## 6. Fallbacks after a rise (REFEREE-2 "Reachability") (DATA)
- ex16.full: for every in-scope fallback a with L = M_a ≥ 0, the first S4a COARSE_L(θ) change j with r > L on [a+1, j], then any later
  fallback of the scope run.
- Exhaustive n ≤ 5: no prefiltered run, so vacuous. Library seeds: rises after fallbacks exist (rise_thin51_n40 3, b6_xl2_n32 7,
  tevlast11_n40 1); none is followed by a fallback.
- far climbs (fitness: fallbacks after such a rise, such rises, fallback pairs, fallbacks):
  - from b6_xl2_n32 (n 32): 25 rises after a fallback, 28 fallbacks, 0 followed by a fallback (164,500 evaluations). farrise25_n32.pg,
    sha1 8941d1c9059415e8e52bfe7e83bee9188114d6d1; n5 = n5b 35/28, Oink zlk OK, strategies verified.
  - from i1h_fts_best16 (n 11): 6 rises, 8 fallbacks, 0 followed by a fallback (1,356,334 evaluations).
- REFEREE-2's observation survives: 0 fallbacks after a rise. RISE-LAST, the (Σ)-rise and TEV-FB / CYC-EV stay vacuous.

## 7. Labels
- DEAD END (Lead-confirmed): NL= (nleq_cex_n48; nleq33_n48 has 33 leaves in one game).
- DATA, 0 failures: RISE-LAST, "no fallback after a rise", Lemma NL (r > L), LV-SHAPE (α / β / γ classification, CN-LAST end),
  LV-NONE, SCOPE-FB.
- DATA: two (β)-fallbacks in one scope run occur (beta2_n11).
- VACUOUS (exact): every box-40 target at n ≤ 4 (all starts, full space) and on the n 5 canonical subset.
- NOT RUN: XSN-RUN exhaustive for n ≤ 12 (infeasible here).
- OPEN: NJB's straddle, G-N5-TIME.

## 8. Traps
- (1) hit() in climb16 flagged every (LV) fallback as a HIT after (β)-fallbacks stopped being failures. Waiters must key on a non-empty
  failure dict.
- (2) The first n 4 all-starts run predated the LV / NL= columns and was restarted (about 15 min lost). Add every counter before a long
  exhaustive run.
- (3) Exhaustive enumeration stops far below the size where these events start (n ≈ 11); a vacuous table is not evidence.
