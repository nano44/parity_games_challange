# Dead SI candidates (L-SI). Each entry: the rule, the family or instance that killed it, the growth it showed, the commit.
Iteration tables: docs/si/RESULTS.md (generated); raw logs experiments/si/out/ (gitignored, regenerate with families.py).

## S4 (subgame-optimal start, then switch-all): DEAD 2026-10-15 10:50Z
- Killer: switchallexp (Friedmann's switch-all family, pgsolver_port.py). Iterations N=1..8: 10, 30, 70, 150, 310, 630, 1243, 2486,
  IDENTICAL to plain switch-all from the best-reward start (doubling per +1 in N: the same run).
  Also switchbestexp N=1..8: 21, 65, 130, 253, 466, 853, 1592, 2963 (b ≈ 1.87, switch-all: 21, 61, 141, 301, 621, 1261, 2541, 5101).
- Obstruction: the optimum σ' of the subgame V \ Attr_Odd(top priority) extends to a start on G that is no closer to σ* in the
  improvement order than the best-reward start: on switchallexp the attractor of the top priority (FinalSink's 16n+12, Odd's)
  is small and σ' restricted to the rest restarts the counter at zero, so the first switch-all step reaches the same strategy as
  from ι. The Lemma 4.3 argument needs σ* itself; an optimum of a subgame is not a surrogate.
- The S4:msf variant inherits msf's behaviour (not switch-all's) and is subsumed by S2.

## S2b LSF (least-significant-first single switch): DEAD 2026-10-15 10:52Z
- Killer: zadehexp (PGSolver zadehexp.ml, "Exponential Lower Bound for Zadeh's rule", port experiments/si/gens.py).
  Iterations N=2..10: 33, 89, 205, 441, 917, 1873, 3789, 15301 (N=10; N=9 not run): b ≈ 2.0 per +1 in N (n = 17N - 6).
  Contrast on the same games: switch-all 4-6, msf 12N - 9 (15, 27, ..., 135 at N=12), steepest 8N - 1, most-improved 8N - 5.
- Obstruction (reading, unrefereed): Zadeh's game is a counter whose cycle gates differ at low priorities (3-6) and whose
  bit selectors sit at priorities 2i + 11; a rule that always serves the least relevant open difference re-opens and
  re-closes the low gates once per higher-bit increment, as Zadeh's least-entered rule does (Disser-Friedmann-Hopp
  arXiv 1911.01074 Thm 6.18 is for Zadeh's rule with its tie-break; the LSF run is an observation, not a proof).
- Regression instance: experiments/si/instances/zadehexp_N5.pg (lsf: 441 iterations; pinned in check.sh).

## S3 steepest (single switch maximising the re-evaluated valuation of the switched vertex): DEAD 2026-10-15 11:20Z
- Killer: the sink-parity-game port of DLMM 2512.16684 Lemma 5.4's MDP M_L (L-LIT T12 section 4; experiments/si/gens.py
  dlmm_ML, start sigma_0 of the lemma). Iterations L=2..10: 4, 11, 26, 57, 120, 247, 502, 1013, 2036 = 2^(L+1) - (L+2),
  IDENTICAL to LSF's run (n = 3L + 4). MSF on the same games: 3L - 2 (4, 7, ..., 28); most-improved: L; switch-all: 2;
  Random-Action-Removal: 3.0 ... 14.4 (mean of 10 seeds, L=2..8).
- Obstruction (reading): the largest re-evaluated gain is the least significant switch here, exactly DLMM's f_Π ≡ 1 case
  (Lemma 5.4 is stated for {Bland, Dantzig, LargestIncrease}-ranking rules choosing the least-preferred switch; this is an
  observation on the port, not a theorem about parity games).
- The most-improved variant (count of vertices whose valuation improves) is linear here and remains open but is subsumed
  by the cost argument (O(n^2 m^2) per iteration) and is not pursued further.
- Regression instance: experiments/si/instances/dlmm_ML_L6.pg (lsf and steepest: 120 iterations from the start in dlmm_ML_L6.start).

## S2a MSF (most-significant-first single switch) and its variants msfa/msfc: DEAD 2026-10-15 12:23Z (killed by L-RED)
- Killer (L-RED, reported by the Lead 12:23Z; files claude/l-red experiments/red/gens_red.py gated_bland, instances
  gated_bland_N6/_N8.pg): the DLMM Bland counter with each a_i choice routed through a Friedmann simple cycle
  (1106.0778 section 6.1, Lemma 6.1) whose two Odd gate vertices carry even priorities decreasing in i. Exactly 2^N - 1
  iterations, n = 5N + 2, from the best-reward start; si.py and L-RED's independent vj.py agree on every row up to N = 13;
  msfa and msfc give identical counts.
- Mechanism (Lead's summary of L-RED): the 2-cycle through the gate sets the switch's LEVEL (the gate's even priority,
  decreasing in i, so MSF processes levels in Bland's order), Odd's current choice at the gate sets its SIGN (Odd goes back
  to a_i exactly when the counter's edge is improving), and the gate's exit sets its EFFECT (as in the plain counter).
  This refutes L-SI's obstruction (b) (notes/L-SI.md 11:25Z): the decoupling of level from effect that Dantzig lower
  bounds get from probability scaling is obtained here by an escaped cycle-creating switch. General lesson (L-RED, lemma in
  preparation): gate relabelling re-assigns the level of any switch, so every rule ranking improving edges by
  first-difference position inherits the index-based lower bounds (DLMM 2512.16684 Thm 4.3 class).
- L-SI reproduction (12:58Z, trunk b5fd882 experiments/red/gens_red.py gated_bland, run on si.py): MSF iterations for
  N = 2..12: 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095 = 2^N - 1 exactly (n = 5N + 2); msfa identical; lsf 1,
  switch-all N, zadeh 2N - 1, cunningham ~4N, Random-Action-Removal 1.8 .. 13.4 (mean of 10 seeds). L-SI's own gate
  variants built from the description before the push did not reproduce (wrong gate placement: the gates must sit on a
  relay d_i after a_i with the underlying priorities shifted above the gate priorities, gens_red.py docstring).
  Regression instance: experiments/si/instances/gated_bland_N6.pg (msf: 63). gated_bland and gate.py transforms are in
  experiments/si/families.py as standard falsification families from now on.

## S1 Random-Action-Removal (original Random-Facet), the M4-R candidate: KILLED, conditional on L-RED's transfer lemma (2026-10-15 12:07Z Lead; REFEREE-2 checking)
- Killer (L-RED, docs/red/R2-RAR.md, experiments/red/fhz.py; trunk be9add4): Friedmann-Hansen-Zwick arXiv 1410.7530
  Theorem 6.3 (p.22): on the shortest-path instances G_{n,r,s,t} (r = Θ(log n), s = Θ(√n log n), t = Θ(log n)) from the
  initial tree B_0, the original Random-Facet performs e^Ω(√n) = e^Ω(M^{1/3}/log M) expected switches. L-RED's transfer lemma:
  a sink parity game P_{n,r,s,t} of size Θ(M) (one player; every G-vertex priority 0 below the sink; relays per edge copy;
  class vertices with even/odd priorities in level bands) on which Random-Action-Removal from the best-reward start runs,
  switch for switch, with the same distribution as Random-Facet on G from B_0 (lockstep evidence: 72,296 tests across the
  weighted, parity and generic-VJ models; 800 random functionals give identical improving sets). Hence S1 needs e^Ω(√n)
  expected switches on games of size Θ(n^{3/2} log^3 n): not M4-R. Status: conditional on the transfer lemma passing
  REFEREE-2 (Lead 12:14Z).
- L-SI's own data (docs/si/RESULTS.md, RESULTS-extra.md): no family or search reached sizes where e^Ω(√n) is visible;
  randomfacetsubexp N ≤ 10 (n ≤ 662) grew like ~n^1.8, adversarial means ≤ 24 at n = 8. Consistent with, and not evidence
  against, the theorem. L-SI's S1.md assumption A1 was expected to be false for exactly this reason (FHZ's construction).
- Closes docs/lit/RANKING.md section 4's "first problem" (Random-Facet on parity games) in the negative, if the lemma holds.

## S7 most-improved (count of improved vertices, steepest-edge tie-break): KILLED 2026-10-15 14:09Z (Lead) by L-RED
- Killer (L-RED, report R5 on claude/l-red, pending push): fhz_padded(n) = the sink-parity encoding P_{n,1,1,1} of
  Friedmann-Hansen-Zwick's one-player Random-Facet counter (arXiv 1410.7530 Fig. 3) with LINEAR pads: W_x·(n+1-i) dangling
  priority-0 Even vertices on each level-i vertex x ∈ {u, w, a, b}, W = (3, 4, 3, 1); size Θ(n²). On vjfast: 16, 44, 104,
  228, 480, 988 iterations for n = 2..7, i.e. i(n) = 2 i(n-1) + 4n (exponential).
- Mechanism (Lead's summary of L-RED): in FHZ's graph the level-i bit vertices take no traffic from the other levels, so pads
  make "lower level first" the count order, and the resets go through a quiet higher level; the run is downstream-first
  (L-RED's exact longest df runs on the same counter: 5, 20, 53, 124 for n = 1..4).
- What it refutes in S7.md: assumption A1 (no polynomial padding scheme) and defence (iii) (padding fails on chain counters:
  true for DLMM G_N, false for FHZ's counter, whose bits are route-isolated). Lemma D (L-RED) was the right structural
  statement; its consequence is that any family with route-isolated bits and a downstream-first counting run is steerable
  by linear pads. docs/si/S7-proof-attempt.md is left in place with the kill noted at its top.
- L-SI reproduction (17:05Z, gens_red.py fhz_padded from claude/l-red ffa4e15, vjfast): most-improved 16, 44, 104, 228, 480,
  988 for n = 2..7 (|V| = 64, 112, 171, 241, 322, 414): EXACT match. On the same games: lsf identical (16 .. 988), zadeh+index
  4n² (16, 36, 64, 100, 144, 196), cunningham+index 16n, msf 4n, switch-all 3n, RAR 8-86 (5 seeds). Pinned:
  instances/fhz_padded_n5.pg (most-improved 228). fhz_padded is in experiments/si/families.py once experiments/red carries it.
- INDEPENDENT KILL from L-SI's own bench (fast sweep, 16:30Z): on PGSolver's randomfacetsubexp (gens.py port, best-reward
  start) S7 takes 4, 106, 233, 1103, 2254, 4557 iterations for N = 2..7 (n = 20, 68, 90, 207, 248, 289): doubling per N from
  N = 5 (ratios 2.04, 2.02); N = 8 exceeded the 900 s limit (> 10^6 evaluations). The run coincides with steepest's
  (S3: 106, 233, 1103 at N = 3..5), i.e. on this family the count order and the steepest-gain order agree. Unconditional,
  no pads needed; regression numbers pinned: instances/randomfacetsubexp_N5.pg, most-improved 1103 (check.sh).
- (JUMP-EQ) (box 6, docs/si/N5-C-box5.md §6.2; CONJECTURE of L-SI succ. 2), FALSE, L-SI succ. 3 box 7 (2026-10-24 21:45Z):
  experiments/red/xing/instances/x31_rx32.pg (sha1 4fe9ec0e, 𝒞^1O, o = 0), transition 53 -> 54. w is constant since the carry
  at level 24; σ̄(o) goes 24 -> 31 (an INR); θ rises at level 25 > 24 and lands in a THR state with θ ≠ w. θ reaches w only at
  state 55. Re-verified: n5.py 55 iterations / 3 fallbacks; Oink zlk OK; strategies verified. Superseded by Theorem FB
  (docs/si/N5-C-box7.md §4), which bounds the fallbacks without it. Script: experiments/si/coarse/jumpeq.py.
- (JU2) (L-SI succ. 3, box 7 §9 CONJECTURE: under (h) with w constant, a non-tame jump below rank(u*) is followed at once by a jump at
  rank(u*)), FALSE: experiments/si/coarse/instances/jcl_x31_cu32i.pg (sha1 00e09994, 𝒞^1O; n5 16/1, Oink zlk OK, strategies
  verified). w is constant and rank(u*) = 30 on states 5-8. θ jumps at levels 27 (5 -> 6), 22 (6 -> 7), 21 (7 -> 8), then 30 (8 -> 9);
  σ̄(o) goes 22 -> 29 -> 13 -> 21 -> 5. Over the named set plus climb bests: 10 of 20 sub-u* jumps fail (JU2) (ju2.py). The
  sub-u* jumps run like a counter over Odd's exits; without releases they are bounded by |succ(o)| per scope run (Corollary JD).
- OG′ (L-SI succ. 3, box 8 §1; own probe: gates into F at k+1 have level ≤ MF_k, the max level of the gates into F at k), FALSE:
  experiments/red/xing/instances/x31_re24.pg (sha1 49eaf50e, 𝒞^1O), transition 1 -> 2. MF_1 = −1, while gate (4, 8) at state 2 has
  level 22. A mass arena leave (|R| 21 -> 1) turns the R -> R gate (8, 14) of level 22 into high gates into F. OFFGATE (bound M_k)
  holds: 7,134 / 0.
- ABS-O as a route to CONJECTURE NJB (L-SI succ. 4, box 9 §3b). The lemma itself is PROVED: an absorption's closed cycle through o
  has no vertex above max(g, rank c) outside P(Ξ_j x0), so rank o ≤ max(g, rank c). It would exclude absorptions inside a level-M
  block only when rank o > M. That never happens: when rank o > rank c, every R -> F gate differs at o, so its level is ≥ rank o,
  and every evicting fallback has M ≥ rank o. Instance: all of them (abso.py: 0 of 778 in-scope fallbacks have
  rank o > max(M, rank c)). Obstruction: o sits below every evicting level.
- CONJECTURE TEV (L-SI succ. 5, P-N5-RL §7 / docs/si/N5-RL-box10.md §5; "after an in-scope THR fallback k0 of level L ≥ 0, every later
  post-rise state t with r > L on [k0+1, t] has the threat's play disjoint from Ev"), FALSE (L-RED 16, Lead re-run 12:27Z), both forms:
  - any earlier k0: experiments/red/so/instances/tev_cex_n40.pg (sha1 17078f78; n5 27 iterations / 16 fallbacks; Oink OK). k0 = 4 (THR,
    L = 33, r = 38, Ev = {5, 8, 12, 15}); 15 more level-33 fallbacks; at t = 23 the threat x_23 = 5 ∈ Ev. With k0 the last fallback
    before t (19, also 18, 11) the threat avoids Ev.
  - TEV-LAST (k0 the last fallback before t): experiments/red/so/instances/tevlast_cex_n40.pg (sha1 ff1e9cb4; n5 11 / 1; Oink zlk OK,
    strategies verified). k0 = 3 (THR, L = 32, r = 38), Ev = {5, 9, 12, 15, 16, 24}; COARSE_32(θ) rises at 6 -> 7; at t = 7 the threat's
    play is 5 -> 15 -> 35 -> 26 -> 28 -> 11. L-SI succ. 6 re-ran threv.py (thr_ev_rise 1, example (3, 7, 32)).
  - Exact obstruction: an S4a state is not a fallback, so gates of level > L into R̄ are allowed there (M_7 = 33 > L). The walk of
    docs/si/N5-TEV-box11.md (Corollary WALK) from e = 15 ends at v = 15 with the gate (15, 21) of level 33 at t = 7, and 15 enters R at 8
    (checked). The threat through Ev is absorbed back at the next S4a step. This is the transient case predicted in N5-TEV-box11.md §5.
  - What survives: TEV at FALLBACK states (N5-TEV-box11.md §3 Remarks, PROVED, no (P)), which is the only form NJB in the ENT setting needs
    (Theorem ENT-X, CONDITIONAL on (P)). Neither instance has a second fallback after the rise, so NJB / ENT are not refuted.

## Box 13 (L-SI succ. 8, 2026-10-25 ~17:10Z by date -u; details docs/si/N5-RISE-box13.md §3; script experiments/si/lv13/oldthreat.py)
- RISE-DROP ("after a rise at j, r_{j+1} ≤ L while S continues"). FALSE.
  - Instance: experiments/red/so/instances/tevlast7_n32.pg (sha1 d905038c), S3 start, own trace: k0 = 11, L = 26, rise at j = 17;
    r = 30 / 27 > L on states 18-40 (in-scope S4a), then EQ.
  - Exact obstruction: the rise level can be below r_j, and an absorption chain of gates into R̄ keeps S going with r > L.
- GATE-ABOVE ("post-rise state with r > L ⇒ M_t > L"). FALSE.
  - Instance: experiments/red/so/instances/rise_thin51_n40.pg (sha1 47aaf46e), S3 / own: k0 = 72, L = 33, j = 75, t = 76, M_76 = 32.
  - Exact obstruction: the gates there are into R̄ at level 32 < L; nothing forces their level above L.
- FEED ("post-rise state with r > L ⇒ some F → R̄ gate"). FALSE.
  - Instance: experiments/red/so/instances/tevlast11_n40.pg (sha1 8421ab30), S3 / own: k0 = 5, L = 33, j = 8, t = 22.
  - Exact obstruction: the only gate is the route improvement (16, 23), R → R̄.
- What survives: CONJECTURE INTO (some gate into R̄), 425 / 425 library states, which with FBL excludes case (i) of the rise claim.
- NONE-LAST / "an in-scope THR fallback with M = −1 is the last fallback of its scope run" (REFEREE-2 N-LV2-3; L-SI succ. 8), and with it
  "after a (β) fallback at M = −1 the next S4a step changes λ_Ξ". FALSE.
  - Instance: experiments/red/so/instances/beta2_n11.pg (sha1 bdea2a23; L-RED 16), canonical S3 start; n 11, o = 1 (rank 9), τ(o) = 8,
    θ = (0, ∅, 2) ◁ w = (0, ∅, 6) (r = −1), λ_Ξ ≡ 0. Confirmed by L-RED ex16, REFEREE (LV2 §C) and the Lead (scopefb.py).
  - SPEC trace: state 0 is a fallback with the (β) gates (5, 2), (5, 6) (R → F, level −1); it evicts 5 (R̄ {1, 5, 7, 10} → {1, 7, 10}).
    State 1 is again a fallback with r = −1, M = −1: the R-vertex 10 now has the (β) gate (10, 5) into the evicted vertex 5 (and (0, 5)
    F → F). λ_Ξ is unchanged.
  - Exact obstruction: eviction cascades. An evicted vertex becomes a (β) target for its R-predecessor, one layer per fallback, with
    COARSE_{−1}(Ξ) and λ_Ξ fixed (FLAT-ALL_{−1}^{none}). The step 0 → 1 is a fallback, not an S4a step, so "the next S4a step changes λ_Ξ"
    has nothing to act on. LV-NONE (≤ n·n_E + 1) is unaffected; this instance exercises its N = 2 step.

## Box 15 (L-SI succ. 10, 2026-10-25 22:48Z by date -u; Lead GO 22:48Z)
- "In scope, THR ⇒ M ≥ 0" (CONJECTURE of docs/si/N5-LV3-box12.md §4-§5, l.157, sha1 20ba05d7; docs/si/N5-LEDGER-box14.md §4 item 4,
  sha1 c54e8560; P-N5-NEEDB §5, not signed). FALSE as stated.
  - Instance: docs/referee-2/R2-N5-LV2/climb/block_9501.pg (sha1 1b5b76fd986487549fe0a35da79f68f5f0d19b3f), n 11, o = 7, one Odd choice
    vertex.
  - Start pair (docs/referee-2/R2-N5-LV2/climb/block_9501.txt): σ0 = [9, 2, 9, 1, 0, 5, 2, 8, 3, 5, 7], τ0 = [9, 2, 9, 1, 0, 5, 2, 5, 0, 5, 3]
    (Even / Odd entries used). The run has 5 states, with one fallback, at 1 → 2.
  - State 1 (an in-phase Even S4c fallback):
    - (h); θ = (5, {9}, 3) ◁ w = (5, ∅, 1), so THR, with r = lev(θ, w) = 10 ≥ 0;
    - M = −1;
    - gates (10, 1), (10, 3), (10, 8), all of level −1, all R → F, i.e. (β);
    - rank o = 2 < rank c_θ = 9 (c_θ = 5);
    - in scope: λ_Ξ and τ are the same at state 2, H2 holds at 2, and w_2 = w_1.
    - This is exactly the counterexample shape N5-LV3 §4 wrote down.
  - Exact obstruction: nothing excludes an in-scope THR fallback whose only gates are level −1 (β) exits R → F. NEED-β (signed) only
    locates the (β) gate on Even's best reply (case B; here (10, 8)); it does not exclude one.
  - Confirmed on three independent engines:
    - REFEREE-2 N-NEEDB-5 (R2-N5-NEEDB.md, referee-2 ef433d32; own / spec / rand traces);
    - REFEREE §C.3 (R-N5-NEEDB.md, referee 7dbd5118; rl_engine);
    - L-SI experiments/si/needb5/repro.py (l-si 34e5225a; n5.py's SPEC loop on si.py; log experiments/si/needb5/saved.txt).
    - Not run: Oink verification of the instance (not built in this container).
  - Nothing signed depends on it (P-N5-NEEDB §5 and N5-LV3 §4-§5 are unsigned). LV-NONE and SCOPE-FB already bound these fallbacks per scope
    run.
- What survives, as a WEAK CONJECTURE only: "from SPEC S3's start, in scope, THR ⇒ M ≥ 0".
  - From S3's start the same game has 4 states, one fallback (at state 0, ¬H1, not THR), and no counterexample state
    (experiments/si/needb5/s3.txt; REFEREE §C.3; RESULTS R43 limit (iii)).
  - Weak, because SPEC allows any start pair, and a run from S3 passes through states that are themselves start pairs. So the S3 form
    restricts only which (σ, τ) are reachable. No current bound needs it.
