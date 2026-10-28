# R97: phase-length climbs at k = 3. New record PL 130 = 3.25n at n = 40 (pinned, verified), no growth with n; the fallback-clocked ladder design and the τ-hold conflict
L-RED successor 23 (Opus 5.5; D14/D15/D18; Lead 2026-10-28 21:27Z and 22:07Z: the intrinsic count is the phase length PL; pin anything
with PL/n clearly above 3.02, the long121 record). Written 2026-10-28 from 23:02Z (date -u). Labels (D18 / L40): DATA / READING / OPEN.
No kill: a constant-factor record is not a super-linear family.

## 1. Pins (DATA; experiments/red/sel/instances/; vrun.sh: n5.py = n5b --mode spec, Oink zlk "OK strategies verified" for both)
| instance | sha1 game | sha1 start | n | Odd choice vertices (out-degree) | iterations n5 / n5b (fallbacks) | PL (longest phase) | SW (vertex, returns) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| pl130_n40 | 895f1128… | 193678c2… | 40 | 0 (9), 1 (8), 6 (4) | 131 / 131 (11) | 130 = 3.25n | 23 (vertex 23, 20 returns) |
| pl129_n40 | 61aeeda9… | 796f807d… | 40 | 0 (8), 1 (9), 6 (8) | 130 / 130 (8) | 129 = 3.23n | 15 (vertex 14, 11 returns) |
| snap30 (scratchpad; SW climb, §2) | bab4ba4a… | 4be44c2d… | 40 | 0 (6), 1 (7), 6 (4) | 103 / 103 (11) | 102 | 30 (vertex 30, out-degree 4, 28 returns) |
- In each, τ changes once (at iteration 1) and the remaining 130 / 129 iterations are ONE phase. PL is measured with τ and both cycle-node
  maps constant (phsw.py).
- Start files are full (every vertex) and are written by experiments/red/sel/fullstart2.py: S3, overridden by the seed's start where the
  edge still exists.

## 2. Climbs (DATA; experiments/red/sel/xrclimb.py, k ≤ 3, L-NEW's mutate (read-only), optional clone mutation; 2400-3000 s each)
| fitness | seed | n | best |
| --- | --- | --- | --- |
| SW·1000 + PL | long121_n40 (pinned start) | 40 | SW 30, PL 102 (snap30); SW 19, PL 89 |
| SW·1000 + PL | long121, padded + clone | 48 | SW 26, PL 82 |
| SW·1000 + PL | lev_l_x (k = 1, S3) | 32 | SW 15, PL 73 |
| PL·1000 + fallbacks | long121_n40 | 40 | 128 (3.20n); with clone 129 (3.23n) |
| PL·1000 + fallbacks | snap30 | 40 | 130 (3.25n) |
| PL·1000 + fallbacks | long121, padded + clone | 56 | 134 (2.39n) |
- Reading: the climbs add a few percent at n = 40. At n = 56 the absolute PL grows by only 4, so PL/n falls. This is the same plateau as
  R88 (125 at n 48) and the XR climbs of R96 §3. No sign of super-linear growth.
- Mechanism in the pins (trace.py): long121's 1-sink structure persists (§3). The extra length comes from more in-phase fallbacks (11 vs 8)
  with the W/Ξ ping-pong of one vertex per fallback, i.e. L-SI's SW-LIN mechanism (docs/si/N5-ALT-box23.md §10, l-si 85709361).

## 3. Why long121's gate 0 stays split for the whole phase (READING; trace on the pinned start)
- long121 is a 1-SINK game. Every Ξ-play, W-play and best-reply play ends at vertex 11 (priority 10, even), and τ(0) = 11 goes straight to
  the sink. Values are signed path sets above 11, and most of Even's vertices have odd (penalty) priorities.
- Gate 0 is a W-ATTRACTOR. Through τ it gives the empty path, the best value any route into 0 can have. Through σ̄ it gives the worst
  current route into Even's network (σ̄(0) moves among 13, 19, 31).
  - An Even edge into 0 is W-best but Ξ-improving only once Ξ(0) has risen above the vertex's current value.
  - So Even's network converges by lexicographic shortest-path steps. The W-attractor makes S4a idle while W-rejected Ξ-improving edges
    remain, and those fire as in-phase fallbacks.
- The split is NOT held by a special gadget. σ̄(0) ≠ τ(0) only while Even's network is not yet converged. The phase length is the
  convergence time of this hybrid dynamic (arena by Ξ, choice by W against the fixed τ), about 3n here.
- selfesc.py (R96 §4): 241 of 292 split-gate states self-escape (Even's best reply to τ returns through the gate); 3 are "held" with no Iσ
  edge on the route.

## 4. The fallback-clocked ladder (design (a′), READING; experiments/red/sel/mkladchain.py, prclimb.py)
- Design: two-way chain v_1..v_L between tops t_L, t_R (Even) that read the newest odd / even rung of a LADDER l_1..l_m.
  - Rung j: current edge → marker → gate o (W through τ(o) = X); ladder edge → l_{j−1}.
  - The ladder edge is W-rejected, so it fires only at a fallback, and a fallback can only happen when S4a is idle, i.e. after the chain's
    wave. So each rung would re-arm one wave, PL ~ m·L at k = 1.
  - The tops read the ladder, not the chain, so R95's self-read (O4) does not apply.
- What works on paper (bit model, one gate):
  - (U1) the rung edge is not improving while the lower rung is unfired (ascending even markers);
  - (U2) it is improving once the lower rung fired (the cycle-node reward of the fired ladder beats σ̄(o)'s);
  - (U3) it is W-rejected (W(o) = W(X) dominates).
- What fails: the τ-HOLD.
  - τ(o) = X must stay optimal against Even's best reply (Iτ depends on τ only, so Iτ = ∅ must hold from the phase start).
  - At the same time σ̄(o) = Z must stay parked below X, and Z's region must not improve.
  - Every placement I tried (direct escape through o; an escape with an odd marker that counts in Ξ_σ but not in Ξ_τ; 1-sink versions) needs
    the same vertex to be counted positive in one comparison and negative in another under the same cycle-node order. This is R96's O5 pattern;
    the 3 held states of §3 show that O5 as a lemma is false.
  - Priority-only climbs on the fixed topology (prclimb.py, L 4, m 4, n 28, 40-90 s) found at most 1 fallback in a phase.
- Status: OPEN. The construction stands or falls with a long-lived split gate under a constant τ. long121 gets one only because its
  network converges slowly.

## 5. OPEN (next)
- A family whose hybrid convergence time (§3) is super-linear. This is the 1-sink lexicographic shortest-path problem under the W-attractor;
  L-SI's decremental-SSSP reading (docs/si/N5-ALT-box23.md §5).
- A τ-hold gadget for §4. It would make the fallback ladder a clock and give PL ~ n²/c at k = 1.
- Tools: phsw.py (PL, SW, returns; plfb), fullstart2.py, xrclimb.py --pl / --sw / --kmax / --start / --clone, mkladchain.py, prclimb.py.
