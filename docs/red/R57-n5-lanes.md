# R57: delay-lane counters against N5 (SSI-GLOBAL), box 25 (L-RED successor 12; produced on Opus 5.5, D15 / L37)
Status: DATA plus readings, unrefereed. Lead wake 2026-10-23 21:40Z (date -u). Recommendation: docs/new/c-lane-synthesis.md §3
(l-new 5e6ab2a).
Object: N5 = docs/new/N5-ssi-global.md SPEC S1-S5, code experiments/new/n5.py (read-only, run unmodified).
Result: NOT KILLED. No counter built here makes N5 super-polynomial. §4 states the obstruction.

## 0. Faithfulness of n5.py to SPEC S1-S5 (READING of the code; DATA from L-COMP's n5b agreement)
Checked line by line against the SPEC text:
- S2: improving edges are strict (si.py improving: key(w) > key(σ(v))).
- S3: best-reward start, with FIX 1's tie-breaks (si.py initial "best": rewcmp (r, w if r even else −w), max). The Odd side is run
  on the dual.
- S4a: Even's arena keeps σ(v) ∪ Iσ(v) for Even vertices (sorted) and τ(v) for Odd vertices. σ_new is read from the dual Engine's
  counterstrategy against τ.
- S4b: Odd's arena keeps τ(v) ∪ Iτ(v) and σ(v); τ_new is read from the primal Engine against σ.
- Both S4a and S4b are computed from the same old (σ, τ) (A6).
- S4c fallback: only if both are unchanged; Even first; ties (key, w) by max, i.e. to the larger index; τ is unchanged (FIX 3).
- Iterations: counted when Iσ ∪ Iτ ≠ ∅ (A8).
- S5: output = Engine.regions(σ), i.e. σ on Even's region and σ̄ on Odd's.
- S1: si.py evaluate. Its longest-path, BFS and cycle-DFS tie-breaks are FIX 2 / FIX 4 (si.py l. 152-195, re-read here).
- n5b.py (L-COMP, independent) agrees in SPEC mode on 526/526 family rows (NOW.md L-COMP row). Not re-run here: no kill to confirm.

## 1. What carries over from R56 (READING)
- M1 and M2 (R56 §1) are tree-label phenomena: truncation hides odd costs (M1), and truncation is idempotent (M2). N5 uses VJ
  valuations, where every odd vertex on a play is charged separately. So neither mechanism exists for N5.
  - In VJ, lanes DO unwind. VJ Random-Edge resets G_ζ's lanes thousands of times (R55 §3b).
- R53's lapping core does NOT carry over:
  - It needs a period in which the strategy recurs while the measure (µ) keeps rising (KL's ratchet).
  - Under N5, σ and τ never recur, and Ξσ, Ξτ rise monotonically (RESULTS R15, Lemma NR).
  - So an N5 counter must be a monotone chain in both VJ orders: a Friedmann-type binary counter, not a lapping cycle.
- R56's delay lanes carry over as a building block. A lane node's inward edge is improving only once the lane ahead of it is
  closed, so N5's gated arena contains one frontier edge per lane per iteration: a lane of length L costs L iterations per
  closing (also L-NEW box 4, N5-killer-box4.md §1).
  - A lane multiplies the run only if it is closed again after a reset, once per counter step. §2-§3 show N5 never re-runs one.

## 2. Data: who moves, on the known counter families (experiments/red/n5/n5tr.py + oddmoves.py)
- n5tr.py replicates n5.run's loop and asserts equal iteration and fallback counts on every run.
- Iterations are N5's; "Odd" = iterations in which Odd's τ changes.

| game | n | N5 iterations | Odd-moving iterations | Odd's last move | Even-moving iterations after it |
| --- | --- | --- | --- | --- | --- |
| switchbestexp N = 2 / 4 / 6 | 60 / 110 / 160 | 32 / 47 / 62 | 2 / 4 / 6 | 14 / 16 / 18 | 18 / 31 / 44 |
| switchallexp N = 4 / 6 | 63 / 91 | 8 / 12 | 4 / 6 | 5 / 7 | 3 / 5 |
| G_ζ gz1 / gz2 (R55; Friedmann's Random-Edge game) | 67 / 389 | 56 / 374 | 3 / 5 | 56 / 114 | 0 / 260 |
| R53 H_0..H_3 | 13-19 | 3 each | 0 | — | 3 |
| R56 HLg_0..HLg_3 | 29-55 | 3 each | 0 | — | 3 |

- Odd moves about N times (once per bit), early, and then never again.
- The rest of the run is Even against a FIXED τ, a single pass over the lanes. On gz2, 374 iterations against n = 389 is about one
  closing per cycle vertex, while VJ Random-Edge needs 824 iterations with about 225 lane openings (R55 §3b).
- Checks: gz2 (N5 374) is Oink zlk OK with strategies verified (check_sol2.py). The other rows are L-NEW's verified bench (sbe/sae
  CSVs) or the trace's own n5.run assertion.
- In switchbestexp, Odd moves in 2-6 iterations only. Friedmann's switch-best counter needs Odd to re-reply at its cycle-exit
  vertices every lap, and N5's Odd does not.

## 3. Attempts against the one symmetric counter, DLM (2309.02223 family 1; both players count under SSI)
- (a) Plain: N5 escapes in iteration 1. Even switches every a_i -> d_{i+1} at once and Odd every d_i -> a_{i+1}; these are not
  SSI's switches (n5tr.py marks them). N5 takes 4 iterations at n = 3 and 4, against SSI's 13 / 29.
- (b) Prune the edges SSI never takes (ssiedges.py): only d_i -> d_1 on family 1, and 10-16 edges on family 2.
  - SSI's counter dies too: family 1 n = 6, SSI 10 iterations instead of 125; N5 7.
  - So the unused edges are threats that shape the valuations. The escape edges a_i -> d_{i+1} are themselves counter edges:
    SSI takes them.
- (c) VJ delay lanes on the escape edges (vjlane.py; Even lane on a_i -> d_{i+1} with exit a_{i+1}, Odd lane on d_i -> a_{i+1} with
  exit d_{i+1}; lane priority 1 / 0):

  | n | L | vertices | N5 | SSI |
  | --- | --- | --- | --- | --- |
  | 3 | 1 / 2 / 4 / 8 | 15 / 21 / 33 / 57 | 5 / 6 / 8 / 12 | 11 / 12 / 14 / 18 |
  | 6 | 1 / 2 / 4 / 8 | 27 / 39 / 63 / 111 | 7 / 8 / 10 / 14 | 23 / 24 / 26 / 30 |

  - N5 = constant + L: one lane pass. SSI becomes linear too, so these lanes destroy the counter rather than protect it.
  - Instances: experiments/red/n5/instances/dl_4_4.pg (sha1 987e2454…) and dl_6_8.pg (sha1 10b7426a…), with start files. Both are
    Oink zlk OK with strategies verified (N5 8 / 14).

## 4. The obstruction (READING; the data of §2-§3)
- (O1) No lapping. N5's σ and τ never recur (R15). A counter must be a monotone chain in Ξσ AND Ξτ; R53/R56's lapping core has no
  analogue.
- (O2) Every exponential VJ-SI construction used so far relies on the opponent BEST-REPLYING at cycle-exit vertices, freshly
  every lap: Friedmann's switch-all, switch-best and Random-Edge games.
  - Under N5 the opponent's strategy is its own honest improvement sequence. τ moves only along Iτ, which depends on τ alone
    (Ξτ is the valuation against Even's best reply τ̄), and Ξτ rises at every Odd move.
  - On every family above, Odd's chain ends after about N moves. From then on N5 is Even against a fixed τ: a one-player-type run.
  - That run is a single pass over the lanes, linear in n (§2). The polynomial bound for N5 on one-player games is RESULTS R17.
  - The fixed-τ two-player case is box-10/11 data (Theorem PH per λ-phase): no counter re-run seen.
- (O3) A lap of a counter flips each cycle-exit vertex back and forth. For an N5 opponent, each flip must be an honest improvement
  in its own Ξ order. So the opponent's own strategy must carry a counter whose state drives the flips.
  - Hence an N5 counter needs TWO coupled counters, one per player, each serving as the other's best-replier. That is DLM's shape.
  - N5 must also be unable to shortcut them with its global one-player optimum.
  - On DLM, the shortcut edges are counter edges (§3b): delaying them with lanes kills the counter for the reference rule SSI as
    well (§3c), and pruning unused edges removes the threats the counter needs (§3b).
- Open, and the precise requirement for a future kill: a symmetric two-counter game in which
  - (i) both players' honest chains are exponential under N5's rule;
  - (ii) the edges N5's global optimum would use to shortcut are disjoint from the counter's own edges and threats, so delay lanes
    can sit on them without changing the counter for the reference rule.
  - No such game is known to the fleet, and none was found here.
- Status of L1 (c-lane-synthesis §1): L1 is DATA for methods whose opponent best-replies (classical SI rules) or whose measure
  ratchets (KL tree labels). N5 is neither. On this evidence L1's scope should EXCLUDE symmetric methods in which the opponent's
  strategy is an independent monotone improvement sequence, unless a two-counter construction as above exists.
- G-N5-TIME stays OPEN. This is not a proof of polynomiality.

## 5. Files
experiments/red/n5/:
- n5tr.py: trace; counts asserted equal to n5.run.
- oddmoves.py: Odd-move statistics.
- ssiedges.py: edges SSI takes; counts asserted equal to n5.run mode ssi.
- vjlane.py: VJ delay lanes on named edges, with start-pair rewrite.
- instances/: dl_*.pg plus start files.
