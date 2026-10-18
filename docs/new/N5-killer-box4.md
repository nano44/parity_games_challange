# N5 killer attempts, box 4 (L-NEW successor 2; started 2026-10-18 21:05Z by date -u; DATA and arguments, unrefereed)
Subject: N5 SSI-GLOBAL (docs/new/N5-ssi-global.md, SPEC S1-S5). Under D1 N5 is wrong until proved otherwise; this box tries to kill it.
Every run below uses experiments/new/n5.py UNMODIFIED (last changed 334f057). The analysis scripts copy n5.py's loop for logging,
and each one asserts that its counts equal n5.run's (n5_trace.py; n5_adv2.py re-runs every improved best through n5.run).
Every solution cited is checked by check_sol2.py (Oink zlk + harness/verify.py) or by zielonka.py + verify.py (n5_adv2.py).
Outputs: experiments/new/n5/box4/.

## Result: NOT KILLED. Forced fallback ("lock") exists but does not scale; obstruction below.

## 1. Deeptrap oscillation (26 / 15 / 33 / 18 at N = 6 / 7 / 8 / 9): explained, linear
Per-iteration traces: n5_trace.py on gen_deeptrap.sh N (sha1 5134273723.., 835ce1326c.., 3ce8d18866.., b88d40574b..),
n5/box4/trace_deeptrap_N{6..9}.txt. At EVEN N the last stage is a chain. Exactly two σ-switches happen per iteration, one link
of each of two parallel chains: 27,29,..,43 (Friedmann's ascending lane chain, priorities 55, 57, ..) and 56,57,64,65,..,88.
Each link becomes improving only after the previous link has switched. That adds ~N + 3 iterations (N = 6: iterations 15-26;
N = 8: 19-33). At ODD N the run reaches the final stage with the chains already set, so there is no chain phase.
Reading: N5's Even step only uses edges improving w.r.t. Ξσ (Odd's optimal reply). A one-link-per-iteration propagation along a
path of length L therefore costs L iterations. This is linear and is the same weakness every SI rule has on a chain. It is not a lever
for a super-polynomial family by itself (a counter needs the chain to be re-run, and the traces show no reset).

## 2. Stall lemma (proved, and checked by computer)
Notation: V_{σ,τ} = VJ valuation of the profile (σ, τ); Ξσ = V_{σ,σ̄} (σ̄ = Odd's optimal counterstrategy).
LEMMA. Suppose N5's Even step leaves σ unchanged (σ' = σ, e.g. in a fallback iteration). Let (v, w) ∈ Iσ be such that the
(σ,τ)-play from w does not visit v, and v is not the cycle node of its own (σ,τ)-play. Then Ξσ(σ(v)) ◁ V_{σ,τ}(σ(v)). In words: on the
play from σ(v), Odd's CURRENT τ is strictly worse for Odd than its optimal reply σ̄. The dual statement holds for Odd's step
(σ worse for Even than τ̄ on the play from τ(u), for each such (u, x) ∈ Iτ).
Proof.
- σ' = σ means σ is the optimum of Even's one-player arena H_σ against τ.
- Pointwise optimality against the single-switch profile σ[v↦w]:
  - The (σ,τ)-play from w avoids v, so w's value is unchanged under σ[v↦w].
  - v is not a cycle node, so V(v) = extend(v, V(σ(v))). Likewise the switched value of v is extend(v, V(w)).
  - extend preserves the order: a common cycle node adds v to both path sets or to neither, plus one step each; different cycle
    nodes compare by the cycle node first.
  - Hence V_{σ,τ}(w) ⊴ V_{σ,τ}(σ(v)).
- σ̄ minimises every vertex at once (VJ00 §5, the Ωσ valuation), so Ξσ ⊴ V_{σ,τ} pointwise.
- (v, w) ∈ Iσ gives Ξσ(σ(v)) ◁ Ξσ(w).
- Chain: Ξσ(σ(v)) ◁ Ξσ(w) ⊴ V_{σ,τ}(w) ⊴ V_{σ,τ}(σ(v)). ∎
The exclusions are needed. Instance: prio [2,6,0,1], owner [0,1,0,0], succ [[0,2],[1,3],[0],[0,1,2]], σ = (0↦0, 2↦0, 3↦1),
τ(1) = 1. Odd's improving edge (1, 3) closes the cycle 1→3→1. Odd's step keeps τ, yet Ξτ(τ(1)) = V(τ(1)).
Computer check (n5_lock.py; only cycle-closing switches excluded, i.e. the stronger statement): EVERY start pair (σ0, τ0)
(≤ 4,000 sampled per game). Random games with distinct-ish priorities, out-degree ≤ 3:
- n = 4, 5, 6: 300 games each;
- n = 7: 400 games;
- n = 8: 300 games.
The lemma held on every fallback iteration. Fallbacks checked: 181, 227, 391 (n = 4..6), 1,275 (n = 7), 2,786 (n = 8); 0 violations.
CONSEQUENCE (necessary condition for any fallback): both players are simultaneously off their best replies, each on the other's
improving plays. If Iτ ≠ ∅, both mistakes are needed. If τ = σ̄ on those plays, the Even step is never empty.

## 3. Termination: the SPEC sentence "each iteration strictly improves σ or τ (in Ξ)" is FALSE as written
Same instance as above: Odd's switch 1→3 (a fallback) changes τ and leaves Ξτ IDENTICAL: (0,0,0), (1,0,0), (0,0,1), (1,0,1)
before and after; afterwards Iτ = ∅. Termination still held in every run: n5_lock.py detects repeated (σ, τ) states and found none
in all runs from all start pairs above. A repair (not proved here, for step 4): Ξ weakly increases at every switch of an improving edge.
While Ξ is constant, every switch moves to a successor of strictly larger key under the SAME valuation. So the pair (Ξ, the sum over
vertices of the key rank of Ξ(σ(v))) increases lexicographically. Owner of the proof: step 4. Recorded as a spec gap, not a kill.

## 4. Locks: consecutive fallback iterations
A LOCK is a run of consecutive fallback iterations. During a lock, τ is frozen, and Iτ depends on τ only, so Iτ is frozen too. Even
then performs classical switch-all steps. A lock that lasts through a Friedmann switch-all run would kill N5 (L-LIT T20 caveat 3).
(a) From ALL start pairs on small random games (n5_lock.py, outputs lock_allstarts_*.txt): the longest lock is
    2 (n = 4), 1 (5), 2 (6), 1 (7), 1 (8).
(b) Hill climb with fitness = (longest lock, fallbacks, iterations) from the best-reward start (n5_adv2.py, mutations as box 3's
    n5_adv.py; every improved best checked OK):
| n | steps | longest lock | fallbacks / iterations | instance (sha1) |
| --- | --- | --- | --- | --- |
| 12 | 4000 | 8 | 10 / 20 | instances/n5lock/lock_n12_seed212.pg (808e91bee6e9..) |
| 24 | 3000 | 11 | 11 / 19 | lock_n24_seed224.pg (e46d695ea5ca..) |
| 48 | 3000 | 9 | 9 / 24 | lock_n48_seed248.pg (665339029a11..) |
| 96 | 2000 | 7 | 8 / 34 | lock_n96_seed296.pg (becd62cd2d89..) |
Locks exist (11 consecutive fallbacks at n = 24), but their length does not grow with n under random search.
Anatomy of the n = 12 lock (trace_lock_n12.txt, iterations 7-14):
- Odd's τ(5) = 5 is a self-loop of priority 1. That is a blunder: under σ̄, Odd prefers 5→0 (cycle priority 5).
- The fix (5, 0) is NOT in Iτ: against Even's best reply τ̄, τ̄(0) = 9 reaches an Even-winning cycle.
- So τ stays frozen with |Iτ| = 4 throughout.
- Against τ, every play reaches the gift cycle at 5. Even's improving switches lead to the cycle at 11 (priority 3), which is worse
  against τ, so Even's step is empty.
- Even does 7 single switch-all steps (a chain 10, 11, 8, 3, 2, 0) until Iσ = ∅.
- The lock length = the length of Even's switch-all run from the lock state: a chain, so linear.
(c) SANDWICH (PROVED; also checked by computer). In every lock step k → k+1 with τ frozen:
    Ξσ_{k+1} ⊴ V_{σ_{k+1},τ} ⊴ V_{σ_k,τ} pointwise.
    Proof: at a fallback, σ_k' = σ_k, i.e. σ_k is the optimum of Even's one-player arena H_{σ_k} against τ. VJ optimality is
    pointwise maximal over all strategies of that arena (VJ00 §5, Lemma 5.8, "maximum element"). The fallback σ_{k+1} uses only
    edges of A_{σ_k}, so it is a strategy of H_{σ_k}, and V_{σ_{k+1},τ} ⊴ V_{σ_k,τ}. The left inequality holds because σ̄ minimises
    every vertex at once. ∎
    Data: 0 violations on the 10 instances in instances/n5lock and instances/n5adv (sandwich_instances.txt), and on 3,000 random
    games, 89 lock steps (sandwich_random.txt).
    Consequence: over a lock of length L, Ξσ_0 ◁ Ξσ_1 ◁ .. ◁ Ξσ_L ⊴ V_{σ_L,τ} ⊴ .. ⊴ V_{σ_0,τ}. Odd's frozen blunder must give Even,
    from the lock's start, at least everything Even will reach in the lock: V_{σ_0,τ} ⊵ Ξσ_L pointwise.
(d) What the stalls use (n5_stallclass.py, n5/box4/stallclass.txt): at Even-stall iterations, improving edges are lemma-covered
    (C) 119 times, cycle-closing (X) 18, own cycle node (N) 2, summed over the 10 instances. Locks found so far use the lemma's
    mechanism, not its exemptions.
(e) Killer attempt 5: a structured lock search (lockgadget.py). A gadget of K vertices is attached to switchallexp(N) only through
    N-independent label templates (global labels; bit 0 / top bit), so the same genome builds every N. Climbs, every improved best
    checked by zielonka.py + verify.py:
    - K = 6, fitness on N = 2, 3: lock 11 at N = 2 and 3 (instances/lockgadget/gadget_K6_seed61.json). Transferred to N = 4..8:
      lock 0, 0 fallbacks, iterations 11, 13, 15, 17, 19 (all OK). It overfits small N.
    - K = 10 (N = 2, 3): lock 2.
    - K = 6 and K = 8 with fitness on N = 3 and 4 JOINTLY (min of the two locks): lock 2.
    No gadget found whose lock grows with N.
## 5. Killer attempt 4: stall gadget with Friedmann's switchallexp behind it (designed; NOT killed)
Design (dummygift.py):
- Every edge (x, y) of an Even vertex with ≥ 2 successors becomes x → D → {y, g}.
- D is an Odd dummy of the lowest priority. g is one shared gift: an Even self-loop, priority top-even ("top") or 0 ("low").
- Intent: τ(D) = g freezes Odd on a blunder, every Even candidate ties against τ, and N5 falls back to switch-all on Friedmann's game.
Result (dummygift.txt, all OK by Oink zlk + verify.py): iterations 8, 9, 11, 13, 15 (top) and 14, 16, 18, 20, 22 (low) at N = 2..6.
0 fallbacks. Linear.
Why it fails (argument; it matches the data):
- If g is top-even, the blunder is no blunder in VJ terms. At an even cycle, Odd prefers the LONGER path, so its fix D → y → D' → g
  is improving against τ̄ AND better against σ. Odd leaves g at once.
- With g low, D's fix carries y's own priority into the path set. Odd vertices y of odd priority make the fix improving.
- Even when every Even candidate ties against τ, Engine.evaluate's tie-break is STATIC (BFS first discovery / smallest index;
  SPEC S1 (iv)). Even's step then becomes a fixed index rule ("move to the lowest-index candidate"), not a stall. A vertex that
  switch-all flips both ways (a ↔ b) cannot be stuck at both times under a static preference.

## 6. The obstruction, as necessary conditions a killer must meet (for gauntlet step 4 and for L-RED)
Any family that makes N5 super-polynomial THROUGH FALLBACKS (caveat 3) must have, at all but polynomially many iterations:
K1 (lemma §2) both players off their best replies, each on the other's improving plays. Odd's current τ is strictly worse for Odd
   than σ̄ on the play from every σ(v) with a non-cycle-closing improving edge. If Iτ ≠ ∅, also σ is worse than τ̄ on every τ(u)'s play.
K2 (frozen Odd) the lock state's τ must survive, unchanged, the whole switch-all run: it must not be improvable against τ̄
   (Iτ fixed), and no fix in the fixed Iτ may help against any σ_k of the run.
K3 (dynamic preference) against the frozen τ (the lemma's exemptions, cycle-closing edges and own cycle nodes, are the only
   other door; §4(d) shows the found locks do not use them), the preference between a vertex's candidates must DEPEND ON σ downstream.
   - The τ-plays from candidate successors must cross Even vertices whose σ-choices change during the run.
   - Otherwise (every candidate enters the gift structure directly) preferences are static. Then any vertex flipped both ways by
     switch-all breaks the lock (§5).
   - In words: the lock must "read the counter".
K4 (sandwich, PROVED §4(c)) V_{σ_k,τ} is non-increasing along the lock and stays above the rising Ξσ_k. The blunder's value
   at the lock start must dominate the whole lock's progress.
K5 (no length lever) inside an even-cycle gift, Odd's fix is improving whenever the fix route is longer. A gift reached through
   per-edge exits therefore needs exit lengths that decrease strictly along every fix route. That is impossible on the σ-cycles
   of the run (a potential argument; sketch, not a proof).
Families that make N5 slow WITHOUT fallbacks:
- They must defeat the restricted best response against τ.
- When τ = σ̄ (Odd has no real choices, as in switchallexp: only h0, h1 choose), Even's step is the optimum of the one-player arena
  over keep-or-improving edges, which jumps.
- Bench data: 2N iterations on switchallexp. Also 2N with τ fixed to Odd's final optimal τ* from the start: n5_taustar.py,
  N = 1..8: 5, 8, 8, 8, 10, 12, 14, 16, 0 fallbacks.
- So the opponent's strategy has to be steered (DLM's distraction, caveat 1) in a way that also satisfies K1-K3 at the steps
  where it matters.

## 7. Not done in this box (named)
- DLM-distraction module (caveat 1) as a construction: the time went to the lock analysis, and K1-K3 are the conditions such a
  module must meet.
- A proof of the termination repair (§3).
- Locks of larger n by a structured search.
