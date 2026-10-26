# R88: one phase of 3n on 𝒞^3O (and 2.25n on 𝒞^2O) found by climbing, with a one-level ruler re-run inside the phase; mechanism = Odd gate deviating into Even's lexicographic shortest-path network; no super-linear trend from the climber (L-RED successor 21, box 55; Lead GO 11:58Z target (1); written 13:34Z, date -u)
Target (1) of the Lead's GO: release of Ξ-blocked, W-tempted edges without fresh content; a family with super-polynomial runs per phase or
unforbid-switches per run, or the obstruction. Labels per L40: DATA, READING (no PROVED item in this report). Every game. Not a TARGET.md
claim. G-N5-TIME stays open. **No family and no obstruction lemma yet.** What is new is DATA on the longest phases known.

## 0. Result (DATA)
- **long121_n40**: ONE phase of 121 transitions at n = 40 (T/n = 3.02) with |Q| = 3 Odd choice vertices, 8 in-phase fallbacks.
  The previous longest phase known relative to n was nep90_n40 (91, T/n 2.27; R79 pin, L-SI §26).
- **long90_k2_n40** (edge-deletion core of it, 86 edges): one phase of 90 transitions, |Q| = 2, 8 in-phase fallbacks.
- Both show a ONE-LEVEL RULER: a block of path-set changes at an Odd choice vertex is run twice, identically, separated by a top-level
  change (§2). This is the shape a super-polynomial phase needs (R83 §2 (ii), R87 §3); here it has depth 1.
- Scaling by the climber is inconclusive and does NOT show super-linear growth: from padded copies of long121, best T = 125 at n 48 and
  124 at n 56 after 10-12 min (T/n 2.60, 2.21). Random "gated shortest path" games (gsp.py, the same shape, n 34, k 3) give T ≤ 9.

| instance (experiments/red/n3/instances/) | sha1 (.pg) | .start sha1 (full start pair) | n | Q | iterations / fallbacks | longest phase T | in-phase fb | checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| long121_n40.pg | c667c08535641a986d771c7a5f3d76bb3c0eef0f | d750664a | 40 | 3 | 122 / 8 | 121 | 8 | n5.py = n5b --mode spec (122 / 8); check_sol2: zielonka(oink zlk) OK strategies verified |
| long90_k2_n40.pg | 6355ce13131617771937d4b48e84b52f3d782852 | 6b80c8bd | 40 | 2 | 92 / 8 | 90 | 8 | n5.py = n5b --mode spec (92 / 8); check_sol2 OK strategies verified |

Climb history (phclimb.py, fitness = longest phase T, n fixed; logs experiments/red/n3/out/ph_*.txt and scratchpad copies summarised here):
| seed | n | start T | best T | time |
| --- | --- | --- | --- | --- |
| random r16 / r24 | 16 / 24 | – | 13 / 28 | 25 / 14 min |
| pftheta34_n32 / xsn29_n32 | 32 | 28 / 28 | 28 / 29 | 6 min each (stuck) |
| nep76_n40 (L-COMP pin) | 40 | 78 | 92 | 10 min |
| nep90_n40 (R79 pin) | 40 | 91 | 117, then 121-122 | 26 + 16 min |
| long121 padded (pad.py, new vertices unreachable at first) | 48 / 56 | 121 / 115 | 125 / 124 | 10-12 min |
- In-phase fallbacks per phase (FIT=F): best 19 at n 24 (from ffin4_n24), 24 at n 40 (from nep90). About 0.6-0.8 n. The n 40 best has
  12 CONSECUTIVE single-vertex fallbacks (a Ξ relaxation running down a path), i.e. linear behaviour.

## 1. The shape (READING from long121's trace; experiments/red/n3/shrink.py core)
- 37 of the 40 vertices are Even-owned; all of those but three have ODD priority. The cycle node is the Odd sink 11 (even priority,
  self-loop, rank 10). So inside the phase, Even solves a lexicographic shortest-path problem: reach 11 avoiding high odd vertices.
- The Odd choice vertices 0, 1, 6 have even priority. τ(0) = 11 (direct to the sink) throughout, but σ̄(0) ∈ {13, 19, 31, 5}: Odd's best
  reply DEVIATES into Even's network the whole phase (D ∋ 0 at every state of the phase; D = {0,1} or {0,1,6}).
  - W(0) is excellent (τ goes straight to the sink); Ξ(0) is Even's WORST current route among 0's options.
  - So every Even edge into 0 is W-tempted and Ξ-blocked until Even's worst route out of 0 beats the reader's current route.
  - Each improvement of that worst route raises Ξ(0) and releases further switches; these switches change the routes again.
- So the feedback that R83 §4 could not build through risers (it closed honest cycles) runs here through an Odd GATE's minimum over Even's
  routes: the gate reads Even's network and Even's network reads the gate, without an honest cycle in the class.

## 2. The ruler re-run (DATA)
Path-set change levels of Ξ(q) in long121's phase (32 / 33 / 40 changes at q = 0 / 1 / 6, ALL path-set changes, no length-only):
- q = 0: [32, 33, 26, **39**, 21, 29, 33, 36, 33, 18, 21, 18, 34, 33, **38**, 30, 29, 28, 23, 26, **37**, 21, 29, 33, 36, 33, 18, 21, 18, 34, 33, **35**]
- q = 1: [28, 33, 26, **39**, 21, 29, 33, 36, 33, 24, 14, 34, 17, **38**, 30, 29, 28, 25, 24, 23, 26, **37**, 21, 29, 33, 36, 33, 24, 14, 34, 17, 33, 35]
- The block after 39 recurs IDENTICALLY after 37 (10 changes at q = 0, 9 at q = 1); the switch sets of transitions 6-57 and 68-115 are
  nearly identical. Each top level is the drop of an ODD vertex from Ξ(0)'s path set (37 at t18, 29 at t58, 16 at t78, 3 at t87, 35 at
  t119: ranks 39, 38, 37, 36, 35), and after each drop lower odd vertices re-enter and leave again.
- In long90_k2_n40 (|Q| = 2) the same: q = 0: [37, 26, 39, (21, 29, 33, 36, 33, 21, 18), 38, 30, 29, 28, 23, 26, 37, (21, 29, 33, 36, 33,
  21, 18), 34, 35].
- So level reuse of a whole block happens in one phase with k = 2; R87's N3-CHAIN / RULER bound 2^{levels} is the only bound in force here.

## 3. What would make it super-polynomial, and what I have not got (READING)
- A depth-d ruler (each top drop re-running the whole lower block, and the block containing its own drops) would give phase length
  ~ 2^d with d = Θ(n): a faithful kill of a polynomial phase bound. long121 has depth 1: the re-run block itself contains no re-run.
- Climbing does not find depth 2 at n ≤ 56 in these budgets, and the best T grows only by +4 from n 40 to n 48. This is not evidence of a
  barrier; hill-climbing at fixed n is weak at this.
- Next (proposed): extract the gate gadget (one Odd gate g with τ(g) = sink, options into an Even lexicographic network, readers with
  edges into g) and build the two-level version by hand: a second gate whose option routes pass through the first gadget's top-level
  vertices, so that a top drop of the outer level re-arms the inner gate. If the inner re-run can be made to contain a drop of its own
  without fresh vertices, depth grows with the number of gates; if it cannot, the reason is the obstruction to write down.

## 4. Tools (experiments/red/n3/)
phlen.py (longest phase; reads .start and .start.json), phclimb.py (FIT=T longest phase, FIT=F in-phase fallbacks), pad.py (padding),
fullstart.py (full start pair as start_pair builds it, needed by n5b), shrink.py (edge-deletion core with T ≥ threshold), gsp.py (random
gated-shortest-path family).

## 5. ADDENDUM (written 13:49Z, date -u; Lead 13:28Z and 13:44Z asks): fallback configurations (FB-C), epochs, runs, and what nesting needs
New pins (experiments/red/n3/instances/; n5.py = n5b --mode spec; check_sol2 "zielonka(oink zlk) OK strategies verified" on both):
| file | sha1 (.pg) | .start sha1 | n | Q | iterations / fb | longest phase |
| --- | --- | --- | --- | --- | --- | --- |
| core41_n40.pg (shrink2.py core of long90_k2, ruler kept) | 59d4ff82a9301751f5b4f0c7748785ccb9af0b62 | 41d60df5 | 40 | 2 | 42 / 6 | 41 |
| comp54_n80.pg (compose.py: two cores, tail of one remapped into the other) | 16c640081c106f58af9d2c50c5ebd4568fa3f2ad | 35dee2db | 80 | 4 | 55 / 6 | 54 |

### 5.1 FB-C quantities (fbconf.py; L-NEW 26's Theorem FB-C: f per phase ≤ #distinct σ̄|Q at fallback sources · (4n² − 3n))
| instance | phase T | f | distinct σ̄|Q at fallback sources | max fallbacks per configuration | Π deg(q) | 4n² − 3n |
| --- | --- | --- | --- | --- | --- | --- |
| long121_n40 | 121 | 8 | 5 | 2 | 60 | 6,280 |
| long90_k2_n40 | 90 | 8 | 4 | 3 | 8 | 6,280 |
| core41_n40 | 41 | 6 | 2 | 4 | 8 | 6,280 |
| comp54_n80 | 54 | 6 | 2 | 4 | 64 | 25,360 |
- FB-C is far from tight here; no tension with it.
- Epochs inside the phase (σ̄|Q constant runs): long121 37 epochs over 14 distinct configurations, one configuration visited 7 times;
  long90_k2 20 epochs over 5 configurations, max 7 visits. So configurations DO repeat inside one phase (the re-run revisits them).
- Fallback-free runs inside the phase: long121 [4, 17, 13, 17, 11, 15, 13, 17, 6] (max 17); long90_k2 max 13; core41 max 7; comp54 max 12.
  The long phases are (f + 1) short runs; the ping-pong is fallback-driven (S4a to the gate, fallback back).

### 5.2 What nesting needs (IMPLICATION from FB-C, which is under review, plus READING)
- IMPLICATION (if FB-C holds; FB-C itself is L-NEW 26's, not mine): in a phase, f ≤ Π_{q∈Q} deg(q) · (4n² − 3n) ≤ Δ^k (4n² − 3n), and the
  phase is f + 1 fallback-free runs, so T ≤ (Δ^k (4n² − 3n) + 1) · R_max, R_max := the longest fallback-free run of the phase.
  - So on 𝒞^kO (k fixed) a super-polynomial phase needs a super-polynomial FALLBACK-FREE run (route (i) of R83 §2), or FB-C false.
  - A fallback-driven ruler like long121's (each re-run costs fallbacks) can nest to depth d only with d ≲ log(#configurations) =
    O(k log Δ): k must grow with d. At fixed k, fallback-driven nesting stays polynomial.
- Re-trigger from inside a block (Lead's first question): NOT observed. In all four instances the re-run is triggered by a top drop
  that happens in an S4a run (t18-19, t24 in core41), and the block itself contains no drop that re-runs a sub-block. The 2-copy
  composition, where the outer copy's exits read vertices of the inner copy, gives T 54 vs 41: the copies run nearly in lockstep, not
  multiplicatively. The 20-minute climb from comp54 is reported below when it ends.
- n cost per level: one level costs the whole core (n = 40 incl. ~10 sub-sink vertices; 67 edges after shrinking). With a second level
  not yet built, the per-level cost is unknown; the composition is 2 × 40.
- Each top drop at q = 0 is a ρ event, ROUTE-driven (L-SI 15 §26); N3-CHAIN (R87) does not apply to it (no flip).
