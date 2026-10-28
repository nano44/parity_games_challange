# R96: anatomy of lev_l_sc's two-digit counter at k = 1 (a BF cascade through the gate's frontier, replayed after one fallback carry), the walls a clean k = 1 rebuild hits, and a correction of R95 §3
L-RED successor 23 (Opus 5.5; D14/D15/D18; Lead 2026-10-26 19:29Z and 2026-10-28 21:05Z: kill CONJECTURE XR-LIN or find an ω(n) phase
at fixed k). Written 2026-10-28 from 21:28Z (date -u). Labels (D18 / L40): DATA / READING / OPEN; no kill here.
Target: docs/si/N5-ALT-box23.md §6 item 1 (XR-LIN: Ξ-changes of one vertex in one phase ≤ 2n). Routed kill design, quoted from
notes/L-SI.md (trunk bb399acd): «Kill design (routed to L-RED): a carry above 24/21 in lev_l_sc that replays the two-digit block.»
Sources opened: docs/si/N5-ALT-box23.md §0-§6; notes/L-SI.md lines 1340-1367 (OR-lens box 3/4 notes); docs/RESULTS.md R51 heading
(per-phase bound T* on 𝒞^1O; O(m·Δ·d_o·n¹³) overall); SPEC S1-S5.

## 0. Why k = 1 is not excluded
RESULTS R51 proves N5 polynomial on 𝒞^1O with a per-phase bound far above n². So a phase of order n² at k = 1 contradicts nothing landed,
and it would kill XR-LIN: the gate's θ = Ξ(o) would change ~n²/c times in one phase.

## 1. Anatomy of lev_l_sc (DATA; experiments/si/orlens/instances/lev_l_sc.pg, sha1 86c17b07…, S3 start; tools experiments/red/sel/trace.py,
xr.py)
- k = 1: vertex 0 (Odd, priority 13, out-degree 15) is the only Odd vertex of out-degree ≥ 2. Phase [2, 54] (τ(0) = 26, constant).
  XR(0) = 46 = 1.44n (xr.py; 45 with λ-split phases).
- LOW DIGIT = a BF cascade along a path through the gate's frontier (t = 12..30). At each step σ̄(0) is the FRONTIER vertex f.
  - f switches to its wave predecessor, whose play runs through the FUNNEL 15 → 14 → 8 → 6 → 0 back to the gate. Under the current σ̄(0) = f
    that is a cycle check (R95 (O4)), and the cycle is Even-good.
  - Odd escapes to the next-smallest option, so σ̄(0) walks 12 → 27 → 1 → 21 → 7 → 20 → 19 → 31 → 9 → 30 → 23 → 2.
  - Each switch is to the previous frontier: 27: 21→12, 1: 21→27, 21: 7→1, 7: 20→21, 20: 19→7, 19: 24→20, 31: 9→19, 9: 30→31, 30: 2→9,
    23: 2→30.
  - Here R95's self-read cascade IS the wave: it is sequential because each step closes one cycle through 0.
  - In the window t = 27..31 the path set of Ξ(0) is constant ({ranks 30, 28, 23, 22}) and only the length falls (11 → 8). The gate is
    strongly split: W(0) = {18, 15, 11}, because τ(0) = 26 → 17 → 11 avoids the punisher 25 (rank 30, odd).
- CARRY = the in-phase fallback at t = 31, then two S4a steps:
  - FB t = 31: 6: 0→25 and 8: 6→25. These are shortcuts that bypass the gate and improve by LENGTH only (6: ℓ 9 → 7). They were
    W-rejected because W(0) ≫ Ξ(0). Also 13: 6→3, a route without the punisher 25.
  - t = 32: 2: 25→13. Punisher avoidance moves one step by BF, i.e. with a LAG.
  - t = 33: mass return (5, 10, 19, 20, 21, 23, 27, 30 back to 2 / 22 / 4) and 6: 25→0 (the funnel is restored).
- HIGH DIGIT = the top odd punisher on the gate's play: rank 30 (vertex 25) until t = 34, rank 29 (vertex 4) from t = 35.
  - The block then REPLAYS below rank 29 with the same edges: t = 33..51 repeats t = 12..30 switch for switch, as returns.
  - Example: 21 goes 7→1 at t = 16, 23, 37, 44. FRESH-RED's NOFRESH term pays for it (docs/si/N5-ALT-box23.md §1).
- Siblings (xr.py, S3): lev_l_x (47a4d340…) XR 51 = 1.59n; lev_l_n28 (827e01aa…) 22; lev_l_n20 (6c365ff7…) 12. L-SI: two digits, never a third.

## 2. What a k = 1 family needs, and the two walls a clean rebuild hits (READING; each wall is checked against SPEC S1/S2/S4 by hand)
Goal: m carries, each replaying a block of length L, so XR(0) ~ m·L. Ingredients:
- (i) a gate o with τ(o) = a clean exit, so that W(o) ≫ Ξ(o) for the whole phase;
- (ii) a chain v_1..v_L with v_i → {v_{i−1}, a_i}, v_0 = a funnel F → o, so the cascade runs as in §1;
- (iii) a carry: a pending (Ξ-improving, W-rejected) edge that fires at the fallback when the cascade ends, followed by a mass return of the
  chain to a_i (the reset) and then a restart of the cascade.
- WALL 1 (lockstep). If the funnel reads o at the carry, its value P_F ⊕ Ξ(o) rises with the alt routes, because o's minimum is an alt route
  or reads the same hub. The reset compares two routes that both contain the new bit, so it is a static comparison and never fires. The
  reset needs the alt routes to see the carry BEFORE the funnel does, i.e. a lag.
- WALL 2 (W-pull). A W-rejected carry edge needs W(o) ≫ every carry value. But a reset done by S4a needs W(alt) ▷ W(funnel) = P_F ⊕ W(o),
  i.e. W(o) below the carry bit. Hence:
  - the reset must also come by fallback (S4a idle), and then no S4a-acceptable edge may exist at that moment;
  - but the funnel's return F → o is a cycle check of the same cycle family as the cascade (Even-good), so it is S4a-acceptable whenever
    σ̄(o) is a routed chain vertex.
  - In my variants either the funnel returns first (no reset), or the parking option that keeps σ̄(o) off the chain must lag the hub, and
    a lag needs an extra Even switch, i.e. one more BF step.
- How lev_l_sc passes both walls (READING from §1):
  - The lag is natural: punisher avoidance spreads by BF from the point of change (13 at the fallback, 2 one step later). The funnel is
    diverted (6, 8 → 25) by length-only shortcuts that fire in the same fallback, so the funnel stops reading o exactly during the reset
    and comes back one step after it.
  - The carry uses the punisher order, not added bits: the high digit drops the top odd vertex (rank 30 → 29) instead of adding a top even
    bit.
- WALL 3 (fresh lag per carry). The natural repair pays each carry with O(1) fresh vertices: a fresh diversion target D_j reading the
  previous rung (a static lag), and a fresh parking option Y_j of the gate. Since o has unbounded out-degree, k stays 1. It fails on the
  ladder in the bit model:
  - The rung edge at ℓ_j must stay non-improving while ℓ_{j−1} is unfired (U1), and become improving once it fires (U2). That forces the
    route of an unfired rung to carry a top ODD marker.
  - But then every reader of a future rung sees a terrible value while that rung is unfired (U4 fails). In particular the parking options
    Y_{j+1}, Y_{j+2}, … become σ̄(o)'s minimum during earlier blocks and stop the cascade.
  - Capping Y with a static even route needs a static value between r_j-dependent values, i.e. again a read of an earlier rung, which
    recurses.
  - So in this model each carry needs its lag readers guarded all the way down. I did not find a bounded guard.
- What a third digit needs (OPEN): a second carry at the end of the replayed block. That means a W-rejected pending edge that becomes
  Ξ-improving only once the second block has ended (chained pendency), plus a next-lower punisher whose avoidance again reaches the alt
  routes one BF step before the funnel. I have not built it. The data (§3) found none.

## 3. Climbs (DATA; experiments/red/sel/xrclimb.py: fitness = max XR of one vertex in one phase, k = 1 enforced, S3 start, L-NEW's mutate,
seeded from lev_l_sc, inert self-loop padding; 2400 s per run)
| seed | n | padding / mutation | best max-XR | XR / n |
| --- | --- | --- | --- | --- |
| lev_l_sc (XR 45 under this fitness) | 32 | none / mutate | 48, 52 | 1.50n, 1.62n |
| lev_l_sc | 40 | random wiring (first try) | 36, 12 | structure destroyed; restarted |
| lev_l_sc | 40 | inert self-loops / mutate | 45, 45 | no gain |
| lev_l_sc | 40 | inert / mutate + clone (copy a core vertex into a padding slot) | 49, 49 | 1.23n |
| lev_l_sc | 48 | inert / mutate | 51, 50 | 1.06n |
- Reading: XR / n falls as n grows. Padding gives the climb room, but it does not find a second carry. This matches L-SI's "no third digit".
- These climbs optimise XR, and XR is now known NOT to be intrinsic. L-SI killed XR-LIN with a passive Odd reader on long121
  (l121reader_n41, XR 86 > 2n; docs/si/N5-ALT-box23.md §8, l-si 6ec0aa2b, per the Lead's message of 2026-10-28 21:27Z; that file was not
  opened by me). The intrinsic targets (Lead, same message) are the phase length PL and the Even switches of one Even vertex in one phase SW.
  experiments/red/sel/phsw.py measures both:

| instance | n | start | PL (longest phase) | SW (max switches of one Even vertex in one phase) |
| --- | --- | --- | --- | --- |
| long121_n40 | 40 | pinned (c667c085…) | 121 = 3.02n | 12 (vertex 32) |
| long121_n40 | 40 | S3 | 18 | 4 |
| lev_l_x | 32 | S3 | 55 = 1.72n | 10 |
| lev_l_sc | 32 | S3 | 46 = 1.44n | 11 (vertex 27) |
| lagx10_n40 | 40 | pinned | 13 | 6 |
| sel_L6_M6 / selneg_L6_M6 | 27 | pinned | 2 / 6 | 1 / 1 |

## 4. Correction to R95 §3 (my own READING, now too strong)
- R95 §3 said that a gate kept split for a whole phase needs a "slow escape", and that in the bit model this is a regress. lev_l_sc
  refutes the conclusion as a statement about N5:
  - gate 0 is split for the whole phase [2, 54];
  - τ(0) = 26 is witnessed by Even's best reply returning THROUGH the gate (… 14 → 8 → 6 → 0 → 26);
  - the split is held because Ξ(0) is low (σ̄ min), so the edge (6, 0) never becomes Ξ-improving, while the region improves slowly through
    the cascade blocks.
- The §3 regress only covered ladders with bit thresholds. A candidate rule "SELF-ESCAPE (O5): a split gate's best-reply witness never passes
  the gate unless some Iσ edge lies on it" also fails: experiments/red/sel/selfesc.py finds 3 held self-escape states each on long121_n40
  (c667c085…) and lagx10_n40 (7258717c…). It is not a lemma.
- R95 §1-§2 (the selector is DEAD by (O4) + one boundary) are unaffected.

## 5. OPEN
- Intrinsic target (Lead 2026-10-28 21:27Z): super-linear PL or SW at fixed k. SW climbs (xrclimb.py --sw) are running; results go in R97.
- The third digit (§2), equivalently Θ(n) carries each replaying a Θ(n) block. A hand-built family on the punisher-descent principle is the
  next construction: punishers P_1 > P_2 > … > P_m (odd, high); a hub whose route drops P_j at carry j; a chain cascade through a gate whose
  τ is clean.
- Tools added: experiments/red/sel/xr.py (XR per vertex per phase, with top-rank trace), xrclimb.py, selfesc.py; trace.py gains a
  states= hook.
