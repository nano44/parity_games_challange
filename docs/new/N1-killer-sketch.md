# N1 killer: construction sketch (L-NEW, 2026-10-18 10:45Z; for routing to L-RED after gauntlet step 2)

Target: violate (PHASE-POLY) (docs/new/N1-disc-anneal.md): a family G_N, poly size, where ONE phase of N1 makes 2^Ω(N)
Howard switches. N1 = Loff-Skomra IncreasingDiscountPI (2610.22149 Fig. 7.2) with rewards (−n)^pr (sign as Jurdziński).

## What the data say N1 does on Friedmann's switchallexp (unrefereed reading)
- Straight at the final γ, Howard replays Friedmann's counter exactly (ablation = 30, 70, 150, 310, 630). With the schedule
  the count is ~2N² and the largest phase is 2N + 5 (the last one).
- At γ_j the discounted order sees a far, high-priority difference only once γ^t · n^Δp beats the nearer terms. The
  bits are therefore "revealed" over a range of j, and each phase starts from the optimum of the previous one. Plausible
  mechanism for the 2N² count: high bits settle first, and a lower bit, once visible, is set once. That is, NO RESET
  ever happens inside a phase.
- Invariances found: priority spreading p -> Kp leaves the run unchanged (only the phase count scales). Uniform,
  priority-monotone and bit-indexed delay chains (lengths up to 24, or 2(i+1)) leave the growth unchanged. Per-edge delay
  search at N = 2 raised the count from 25 to 49 (plain Howard on the base: 30); no family yet.

## The construction needed (two routes)
(A) Bottom-up reveal. Make bit i's decisions visible at phase j_i with j_0 < j_1 < ... (low bits first). In the phase
    where bit i appears, all lower bits are already visible and at their optimum. Howard from the state "bit i = 0, lower
    bits = optimum" then has to count through the lower bits again (Friedmann's reset). That is ~2^i switches inside one
    phase, so (PHASE-POLY) fails. Requirement: per bit, a delay or reward structure that hides bit i's long-range difference
    until horizon H_i, with H_i increasing in i. It must not change the VJ/Friedmann order at γ -> 1, which needs a
    1-sink game (Lemma 9.6 of 1106.0778). Small bit-indexed delays (c = 2, 8) did NOT do it. Unknown whether lengths of
    order H_i · Δp · ln n (polynomial, ~10^3-10^4 vertices at N = 4) do; this is beyond the exact Python engine (the C++
    port, item 4 of the Lead's list, is the prerequisite).
(B) Bait start. Make the optimum at every horizon below H equal to Friedmann's bad start σ_0, and reveal all of the
    counter between H and 2H. Then one phase is plain Howard from σ_0, i.e. Friedmann's 2^N. Obstruction seen: in a 1-sink
    game the chains' own rewards compete with the targets' path differences, so σ_0 is the short-horizon optimum only
    if x(σ_0(v)) sits above the sink baseline at short horizon. Friedmann's start does not have that property in general.
    A bait gadget (an extra early reward on σ_0's edges that vanishes in the VJ order: a priority below all original ones,
    repeated k times so that k·n^0 matters only at short horizons) is the next thing to try.
Either route needs the C++ engine for N >= 4. Cheapest first instance to try: switchallexp N = 2, 3 with route (B),
since it needs only O(n) extra vertices.

## Status
Sketch only. No instance kills N1 yet. Barrier rows that would then cover N1: none published (B8 covers fixed-γ
Howard only); a kill would be a new lower bound for LS24's IncreasingDiscountPI on worst-case (parity-induced) inputs.

## Route (B) first try (10:55Z, experiments/new/bait.py): did not kill
Chain of k priority-0 Odd vertices on each start edge (originals +2). Plain VJ Howard: 15, 35, 75 (still doubling, N = 2..4).
N1: k = 4: 30, 50, 72; k = 16: 33, 51, 74 (largest phase 9, 11, 13 = the last one). Regions = Zielonka, strategies verified.

## Route (A), key-edge delays (11:05Z, experiments/new/keydelay.py, C++ engine): no effect at all
Only bit i's cycle-closing edge e_i -> h_i delayed by c(i+1) (or c(N-i)) priority-0 Odd vertices, c = 20 and 100, N = 2..5
(n up to 1577): plain VJ Howard 30, 70, 150, 310 (unchanged, doubling); N1 25, 42, 64, 90 in EVERY variant, i.e. exactly
the undelayed counts; largest phase = the last one (9, 11, 13, 15). Regions = Zielonka, strategies verified.
Reading (unrefereed): on this family N1's Even switches do not depend on when a bit's closing edge becomes visible; the
optimum at γ_{J-1} is already within 2N + 5 Howard steps of the parity optimum. A killer must make the optimum of the
previous discount a BAD START for the next one (route B), not merely reorder reveals. HMZ-style arguments do not exclude
it: from a warm start the gap is small, but Howard's iteration bound depends on log(gap_0 / smallest nonzero gap) / (1 − γ),
which is still 2^j-sized for parity rewards.

## A reveal-time tool that does work: priority gaps (11:20Z, argument, not yet built)
Trap gadget at an Even vertex v: option A = a vertex of even priority p, then an Odd-won cycle of priority q < p (A loses);
option B = a small Even-won cycle of low even priority. Discounted value of A ≈ n^p − H n^q (H = 1/(1−γ) up to constants), of
B ≈ small·H. So the parity-correct choice B becomes optimal only once H > n^(p−q), i.e. at phase j ≈ (p − q) log2 n. Delays
can only push a reveal by a polynomial horizon; gaps push it to any phase up to (d + 2) log2 n with O(1) extra vertices.
This also explains why the certificate fires only at J ≈ (d + 2) log2 n (signs of values in 1-sink games need H > n^(p_max)).
Use for route (A): gate bit i's set-decision of a Friedmann-type counter by a trap with gap g_i increasing in i, so bits are
revealed bottom-up. Open: whether gating a bit this way keeps Friedmann's reset behaviour once the bit is revealed (the trap
must disappear from the comparison after its reveal, which an Odd-won cycle on the losing option does: after the reveal,
A is simply worse). Not built in box 1.
Built (11:25Z, experiments/new/gaptrap.py): trap at each e_i, P_i = B + 2 + 2k(i+1) (or 2k(N−i), --rev), cycle B + 1.
k = 1, 3, both orders, N = 2..6: plain VJ 30..630 (unchanged); N1 33, 51, 81, 110, 142 (k = 1) and 45, 65, 99, 136, 180
(k = 3); --rev similar. Largest phase 9..17 = 2N + 5 = the final phase, as without traps. Totals rise by ~1.5x, growth stays
quadratic. Regions = Zielonka, strategies verified. Did not kill. Reading: traps do delay bit i's availability, but when
bit i appears, Howard does not replay the lower count; the lower bits' optimum at the current discount is already what
Friedmann's counter would reach after the reset.

## Route (B) with traps on every Even choice vertex (11:30Z, alltrap.py): did not kill
Trap at every Even vertex with >= 2 successors (P = B + 2 + 2k, cycle priority B + 1, or 1 with --q 1 for the latest reveal).
Plain VJ Howard from best-reward start (= all traps): 33, 73, 153, 313, 633, 1246 (Friedmann + 3, doubling). N1: k = 1, 4:
26, 43, 65, 91, 121 (unchanged from the trap-free game); --q 1: 21, 39, 59, 83, 111, 143 with the traps revealed over the
last ~log n phases (phases of 10-20 switches), not at once. Reading: a trap's reveal time depends on the priority of the even
cycle Even can reach from v, so reveals spread out and come top-down again. A simultaneous reveal needs per-vertex trap
priorities calibrated to v's own winning cycle; not built.

## Lock attempt (Lead 11:40Z item 3; 12:05-12:15Z, experiments/new/lock.py): NOT built; why
Goal: a family where Even wins only with the counter's final strategy, hard for Howard from BOTH sides.
- p0 (FinalSink p -> priority 0; p lies on every play into q, so VJ comparisons are unchanged): plain VJ 30, 70, 150, 310, 630
  (unchanged), certificate-stopped 14, 34, 74, 154, 314, dual certificate-stopped 2, 3, 4, 5, 6 (still trivial from Odd's
  side), N1 35, 64, 101, 146, 199 (N = 2..6; Odd wins everything; regions = Zielonka, strategies verified).
- loop (q's self-loop replaced by q -> L -> s, L Odd, priority 0): Even wins EVERY vertex (36/36 ... 92/92): s -> p -> q -> L -> s
  is a cycle of even top priority. Plain VJ 14..27, certificate at iteration 0 on both sides; N1 21..109.
- loop2 (loop and s loses its edge to p): still Even wins every vertex (the cycle through a bit's access k_i (odd 6n+...) also
  passes m_i (even, higher)); plain VJ 9..17, certificate at 3 / 0; N1 26..120.
Why it fails: Friedmann's counter encodes the bits in the PATH SET (lexicographic order of all priorities on the path to the
sink), while a parity condition sees only the MAXIMUM on a cycle. Closing the plays into a cycle through s makes the winner
depend on the top priority alone, which Even controls at once. A lock needs a gadget that turns "the path set equals the
final counter state" into "the top priority on some cycle Odd can force is even" for every non-final state, e.g. Odd
choosing, from L, which bit i to audit (L -> audit_i), each audit_i cycle being Even-won iff bit i's lane is in its final
position. That is a per-bit check, so Howard can satisfy it bit by bit unless the audits are coupled through the counter's
resets; whether such a coupling exists is the open design problem. Note also: for N1 itself, switchallexp already acts as
a lock on Odd's side (the certificate needs Odd's discounted best response to Even's σ to be globally winning, which
certificate-stopped VJ Howard reaches only after 2^(N−1) + O(1) iterations), and N1 gets there in ~2.6 N² switches. The
"weak evidence" caveat is against the two-sided baseline, not against N1's own mechanism.
