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

## 6. O4: why each attempted two-counter coupling fails (Lead 21:57Z; READING with DATA; 2026-10-23, written after 22:00Z by date -u)
Instrument: experiments/red/n5/perswitch.py. It gives per-vertex switch counts of N5 runs, through n5tr.trace, whose counts are
asserted equal to n5.run.

| game | Even: vertices switching / max at one vertex / vertices with a return | Odd: the same | N5 iterations |
| --- | --- | --- | --- |
| switchbestexp N = 6 (n 160) | 101 / 11 / 77 | 6 / 1 / 0 | 62 |
| switchallexp N = 6 (n 91) | 55 / 4 / 1 | 6 / 1 / 0 | 12 |
| G_ζ gz2 (n 389) | 374 / 5 / 186 | 3 / 2 / 0 | 374 |
| DLM family 1, n = 5 / 6 (DLM start pair) | 5 / 3 / 0; 6 / 4 / 2 | 5 / 4 / 1; 6 / 4 / 2 | 6 / 7 |
| DLM family 2, n = 4 (DLM start pair; instances/dlm2_4.pg) | 8 / 4 / 1 | 8 / 4 / 1 | 8 |

- (C1) One counter, with the opponent as best-replier (Friedmann's switch-best and switch-all games, and G_ζ).
  - The counter needs the opponent's cycle-exit vertices to change with the count. On switch-best, Odd's arena reply τ_sb takes
    2^N values and changes 1, 4, 10, 24 times for N = 1..4 (L-NEW, N5-dlm-box5.md §7, K7).
  - Under N5, each opponent exit vertex switches at most twice and NEVER returns to an earlier successor. On switchbestexp N = 4,
    Odd's only choice vertices h_0..h_3 each switch once, h_i -> m_i.
  - Why: the opponent's gate Iτ is a function of τ alone (S2 on the dual; Ξτ is the valuation against Even's best reply τ̄). An
    exit vertex can flip back only when the honest values of its two successors cross again, and those values move only with the
    opponent's OWN strategy.
  - In a one-counter game the opponent's strategy holds no counter. Its honest values settle after about N switches (§2), and N5
    then runs one pass for the counting player against a fixed τ.
- (C2) Two counters, symmetric (DLM; each player's strategy holds a counter, and each is the other's distracting best-replier).
  - Here the opponent's exits DO return: 1-2 vertices with returns, up to 4 switches at one vertex.
  - But N5's joint restricted optimum takes, in one step, every improving switch that the local rule withholds: K6
    (N5-dlm-box5.md §4; on DLM's families N5 ⊇ SSI at every state, 100% of 342 + 399 vertex events, n = 2..5). The counter is
    skipped in a few iterations (6-8 here).
  - The withheld switches cannot be delayed without destroying the counter:
    - the escape edges are counter edges (SSI takes them, §3b);
    - removing the never-used edges removes threats SSI's counter needs (§3b: 125 -> 10);
    - lanes on the escape edges make SSI itself linear (§3c).
  - L-NEW's opponent-blunder modules (box 5 §3) keep SSI exponential but make N5 faster (2-15): N5 exploits the blunder at once.
- (C3) Time-scale separation by lanes (proposed here against K7, NOT built).
  - If each decisive switch of the counting player is preceded by L lane steps, the opponent's one-step lag (K7) stops mattering.
  - But it does not touch the gate. The opponent's required alternations must still be honest improvements, and by C1 they
    recur only if the opponent's own strategy holds a counter. That leads back to C2, where K6 applies.

O4 (READING). A super-polynomial N5 run needs both of the following.
- (R-a) Each player's strategy holds a counter whose own honest values (Ξσ for Even, Ξτ for Odd) cross at the vertices that face
  the other counter, once per count. This lets the exit vertices alternate through honest improvements. The data show this only
  in symmetric games (C2).
- (R-b) In every state, the honest improving switches that are optimal against the opponent's CURRENT strategy (N5's joint
  optimum) contain no jump ahead in the count. That is, the counter's next step is the only profitable honest change, for both
  players at once.
  - With the opponent fixed, a player's run is short: one-player games are polynomial (RESULTS R17), and fixed-τ two-player runs
    stay within Theorem PH's per-phase bound on the box-10/11 data.
  - So progress must alternate between the players, each opponent move unlocking only a bounded number of new honest switches.
- Every construction tried satisfies at most one of the two. Friedmann's games fail (R-a), because only one strategy counts.
  DLM fails (R-b), because the local rule's withheld switches are honest and profitable, so the joint optimum takes them.
- Delay lanes can enforce (R-b) only on edges that are not themselves counter edges or threats. In DLM they are. No game is known
  in which the count's "jump-ahead" switches use edges disjoint from the counter's edges and threats.
- This is evidence, not proof, against the L1 transfer to N5. G-N5-TIME stays OPEN.
- What would settle it: a proof that (R-a) and (R-b) are incompatible (e.g. that honest crossings at exit vertices force a
  profitable jump-ahead switch somewhere), or a game meeting both.

### 6b. Symmetric climbs (DATA; experiments/red/n5/symclimb.py; 2026-10-23 22:09-22:34Z, date -u)
- Search space: games invariant under mirror + dual. Vertex v has a mirror v ± h with owner swapped, priority + 1 and mirrored
  successors, so both players face the same structure (requirement R-a's shape).
- Fitness: N5 iterations from the best-reward start. Two seeds per size, 1,500 s each.

| n | iterations, seeds 1 / 2 | best / n | best instance (instances/) | check |
| --- | --- | --- | --- | --- |
| 12 | 23 (one 60-s seed) | 1.92 | — | Oink zlk OK, strategies verified; n5b spec 23 |
| 16 | 25 / 24 | 1.56 | sym_h8_s1.pg (sha1 f87fee647f1c…) | Oink zlk OK, strategies verified; n5b spec 25, orig 25 |
| 24 | 34 / 31 | 1.42 | sym_h12_s1.pg (sha1 5de0d6588c61…) | Oink zlk OK, strategies verified; n5b spec 34, orig 28 |
| 32 | 55 / 44 | 1.72 | sym_h16_s1.pg (sha1 a46e6c88f031…) | Oink zlk OK, strategies verified; n5b spec 55, orig 55 |

- The n = 32 best (55 iterations) exceeds the lane's earlier best run, 50 at n = 61 (N5-toggle-box11.md §4).
- perswitch.py on sym_h16_s1: BOTH players switch at 15 vertices each, with returns at 10 vertices each (up to 6 switches at one
  vertex). So symmetry does produce R-a-type behaviour: exits alternate through honest crossings on both sides.
- Growth is still linear, iterations ≈ 1.4n-1.9n. R-b (no profitable jump-ahead) is not met by anything the climb finds.
- Consistent with O4; not a kill.
