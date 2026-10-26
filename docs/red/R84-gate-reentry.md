# R84: one gate leaves and re-enters D Θ(n) times in ONE phase, driven by a chain disjoint from its readers; a reader's edge is re-blocked Θ(n) times but never released (mkgate) (L-RED successor 20, box 51; Lead 11:13Z, date -u)
Target: the Lead's gate re-entry test (R83 §4's key sub-question for route (i)). Labels per L40. DATA, READING. Every game. Nothing
here bounds N5. Not a TARGET.md claim. G-N5-TIME stays open.

## 0. Result (DATA)
- **Yes: a gate can leave and re-enter D Θ(n) times inside one phase.**
- Family experiments/red/usplit/mkgate.py K LG OUT (LG = K + 6). mkpp's two leapfrogging risers vA and vB drive one gate u (Odd)
  with successors aU → vA and bU → vB.
  - τ(u) = aU is Odd-optimal, because Even's best response tops vB's side at the higher g*.
  - σ̄(u) is the lower riser's side, so u ∈ D exactly while vA leads.
  - The drivers (risers, lines, routes x_j) are disjoint from u's readers.
- Two readers:
  - reader 1: rx → {sx → Z, z → u};
  - reader 2: x2 → {y2 → vB, z2 → u}. (x2, z2) is W-tempted (W(u) = W(vA side) via τ) and Ξ-blocked (Ξ(z2) = min ≤ Ξ(y2)) exactly while
    vA leads.

| K | n | iterations (n5.py / mine) | phases | fallbacks | D changes | toggles of u | max ρ_q | forbidden episodes of (x2, z2) | switches into (x2, z2) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | 133 | 15 | 1 | 0 | 8 | 6 | 7 | 3 | 0 |
| 16 | 197 | 23 | 1 | 0 | 16 | 14 | 15 | 7 | 0 |
| 32 | 325 | 39 | 1 | 0 | 32 | 30 | 31 | 15 | 0 |
| 64 | 581 | 71 | 1 | 0 | 64 | 62 | 63 | 31 | 0 |

- Counts are from my experiments/red/usplit/gatecount.py:
  - D changes, toggles per Odd vertex, ρ_q, and forbidden EPISODES per edge (maximal runs of forbidden states, L = −1 as in N5-RUND §16);
  - every K: OUT OK and Oink OK.
- n5.py and check_sol2 reproduce the iteration counts at K 16 and 64, with "zielonka(oink zlk) OK strategies verified".
- Pins: gate_K16_n197.pg (sha1 3eeddc86ae0b56dcaf8afed00d21b298cda69796) and gate_K64_n581.pg (sha1
  a93c7c8be2c39e333cd61755f7ae4cd8ebc0ff98), each with .start and .start.json (start pairs).

## 1. READING
- Gate re-entry is cheap: it costs nothing beyond the drivers' content (one fresh C_j per toggle, RULER).
- A block re-arms at every toggle: (x2, z2) is forbidden again in each vA-led interval.
- So a block CAN re-arm without fresh content of its own. What is missing for route (i) of R83 §2 is RELEASE: a switch into the re-blocked
  edge at each episode (a U event per episode).
  - Release needs Ξ(z2) above Ξ(y2) while W still prefers z2, inside one leapfrog interval. Within one interval the drivers are
    constant, so release needs a second, faster clock: the same timing problem as R83 §4.
- An attempt to add a re-thawing third reader (x3: {y3 → vB, e3 (even) → u}) broke the phase (τ changed: 2 phases). I removed it; not
  pursued.
- The FS conjecture of N5-RUND §16 (an edge forbidden at k is forbidden at no k′ ≥ k + n) is NOT touched here: the whole run is shorter
  than n (71 < 581).
