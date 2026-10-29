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

## DEAD box 16 (L-SI successor 11, 2026-10-26T04:37Z by date -u): TC-W, "a terminal change moves to the gate with the larger W" (own conjecture, never sent as a lemma)
- Statement killed (three forms, all on 𝒞^2O with |D_k| = 2 and D_k unchanged at the transition): at an in-phase S4a transition k → k+1
  at which v ∈ R_D switches its gate u → u′, W_k(u′) ▷ W_k(u). The three forms:
  - (first gate) u(v) is the first D-vertex on v's W-play;
  - (ultimate gate) the first W-direct D-vertex;
  - (ultimate gate, gate structure fixed, v ∉ D_k).
- Obstruction (mechanism): S4a takes Even's pointwise W-optimum of its arena. A route to a gate with a lower W(u′) wins when its own path
  part is better, e.g. shorter at an even cycle node, or through a higher even vertex. So W(v) rises while the gate's value falls. No
  fixed order of the gates by W (or by Ξ) is respected.
- Instances (experiments/si/fb2o/instances/, checked by experiments/si/fb2o/tcdir.py; logs/tcdir_*.txt):
  - tcw_against_n12.pg (sha1 90b9651c…, S3 start): first-gate form. v = 5 switches from gate 2 (the even W-cycle node, W = (2, ∅, 0)) to
    gate 3, which routes through 2 (W = (2, ∅, 3)). The ultimate gate is unchanged, so this kills only the first form.
  - tcwult2_against_n8.pg (sha1 c2cceba0…) with tcwult2_against_n8.start.json (sha1 4a123025…): all three forms. v = 1 switches from
    gate 0 to gate 4 at transition 0, against both W and Ξ.
    gatev=0 D2=1 dchange=4 changes=5 same_stretch=1 toW=0 toX=0 toWX=0 againstW=1 tieW=0
AGAINST_W ('experiments/si/fb2o/instances/tcwult2_against_n8.pg', 0, 1, 0, 4, -1)
    → "againstW=1" (also with ULT=1).
- Frequency (random 𝒞^2O, 150,000 games, n 5-12, seed 9; tcdir.py --rand with K=2):
  - first-gate form: 21 of 94 qualifying changes go against W;
  - ultimate form with structure fixed: 5 of 21.
  - On the library (lib41's frontier games), the first-gate form held 47 / 47 with D fixed. Only random start pairs exposed it.
- Consequence for TC-SWITCH (docs/si/N5-2O-T-box16.md §4.2): a per-vertex count of terminal changes cannot come from an order on the
  gates. The natural monotone quantity at a terminal change is W(v) itself (WM), and bounding its changes per run is Theorem RUN's job.
  So TC-SWITCH is no easier than RUN_D on two gates.

## DEAD box 17 (L-SI successor 12, 2026-10-26T06:5xZ by date -u): "every twin change strictly raises COARSE_L(W(v)) at the twin level" (own plan, sent to the Lead 06:23Z as a planned lemma; never stated as proved)
- Statement killed: at an in-phase S4a transition k → k+1 at which v changes its first gate u → u′ (u_k(v) ≠ u_{k+1}(v)) with λ_W(v)
  unchanged and D_k = D_{k+1}, COARSE_L(W_{k+1}(v)) ≻ COARSE_L(W_k(v)) at L = top(P(W(u)) Δ P(W(u′))).
- Obstruction: W(v) can change ONLY IN LENGTH (same cycle node, same path set). Then no coarse value changes at any L ≥ −1. WM-G gives
  W_{k+1}(v) ⊵ W_k(v) and nothing more.
- Instance: experiments/si/rund/instances/lenonly_n8.pg (sha1 725c2766a5b9e9011d200e3ba1a3d81aac8e144b), S3 start. At transition 1 → 2,
  v = 2 switches gate 6 → 4 with D constant; W(2) = (4, ∅, 4) → (4, ∅, 3). Check: `python3 -I experiments/si/rund/rund.py --one
  experiments/si/rund/instances/lenonly_n8.pg` prints `LENONLY ('…lenonly_n8.pg', 1, 2, 6, 4, (4, 0, 4), (4, 0, 3))`
  (also in experiments/si/check.sh).
- Found in random 𝒞^2O (`K=2 rund.py --rand 3000 5 12 41`, games #321 and #933, both S3 starts).
- Replacement: the offset count, Theorem TWIN-GAP (docs/si/N5-RUND-box17.md §5), which counts the changes of v's offset Δ(v) = s^W − s^Ξ
  by the rise of two monotone integer scores, not by coarse values.

## DEAD box 17b (L-SI successor 12, 2026-10-26T07:1xZ by date -u): CONJECTURE OFFSET-ONCE (docs/si/N5-RUND-box17.md §6 (R2), §10)
- Statement killed: inside one stretch_D (D_k, R_D and the gates' values Ξ(u), W(u) constant) of a fallback-free in-phase run with
  (h3_D), no vertex's offset Δ(v) = w(P(W v)) − w(P(Ξ v)) returns to a value it has left.
- Obstruction: monotonicity of s^Ξ, s^W allows a return whenever the route to the first gate gains ≥ |δ_A − δ_B| in between. A delay
  chain on that route (one Even switch per transition, as S4a propagates) delivers the gain late: v leaves u1 for u2, then comes back.
- Instance: experiments/si/rund/instances/offret_n23.pg (sha1 8fdfc38d0e11c4217c39700ca202d00c5740e80b) with offret_n23.start (sha1
  634dbc59d3ad9a73bdd931cf7579c8e841d0128e). States 0-3: D = {4, 12}, τ = (2, 10), the gates' values unchanged, c = 0, (h3_D), no
  fallback. v = 22: offset 131204 → 264200 → 131204. `python3 -I experiments/si/rund/gap.py --one …offret_n23.pg …offret_n23.start`
  prints `RETURN ('…offret_n23.pg', 0, 3, 22, [131204, 264200, 264200, 131204])` (also in experiments/si/check.sh).
- Family: mkalt.py K → K − 1 offset changes of one vertex in one stretch_D at n = Θ(K²) (K = 10: 9 at n = 182, offalt_K10.pg, sha1
  b03fe313…).

## DEAD box 17c (L-SI successor 12, 2026-10-26T07:3xZ by date -u): the strong ("levels only increase") form of CONJECTURE LEVEL-COUNT
- Statement killed: inside one stretch_D with (h3_D), the rise level of v at successive offset changes strictly increases.
- Obstruction: a return can be paid by removing a high ODD vertex from the old route, winning at a lower level.
- Instance: experiments/si/rund/instances/incdown_n23.pg (sha1 18a5d000…) with incdown_n23.start (sha1 634dbc59…; built by mkinc.py 2 4).
  v = 22: offset-change levels [20, 19]. Pinned in experiments/si/check.sh (lvl.py prints VIOLATION ('INC', …, 0, 3, 22, [20, 19])).
- The count form (|OC(v)| ≤ |RL(v)|) is NOT killed: CONJECTURE (docs/si/N5-RUND-box17.md §12).

## DEAD box 17d (L-RED kill, reproduced by L-SI successor 13, 2026-10-26T08:1xZ by date -u): CONJECTURE LEVEL-COUNT, count form
- Statement killed: inside one stretch_D segment with (h3_D) (fallback-free, one phase), |OC(v)| ≤ |RL(v)| for every v with constant
  cycle nodes (OC: offset changes; RL: the set of rise levels of s^W and s^Ξ together). docs/si/N5-RUND-box17.md §12.
- Obstruction: a lag between the two scores. W rises at level a (offset changes), then Ξ rises at the same a (offset changes back): two
  offset changes, one level. RULER (per score) holds.
- Instances (L-RED, experiments/red/h3/instances/): lcount_n23.pg (sha1 f86125a08f0e3b0caf3d825cb48e6dcdc0ee3b04) + lcount_n23.start,
  v = 1, OC 3, RL {18, 21}; lcount2_n23.pg (sha1 dd9847c6b19cb9f44af73bcc23de7ca2aca9a14c) + .start, v = 12, 16, 20, OC 3, RL {20, 21}.
  `python3 -I experiments/si/rund/lvl.py --one <pg> <start>` prints `VIOLATION ('LC', …, 0, 3, 1, 3, [18, 21])` (pinned in
  experiments/si/check.sh).
- Replacement: CONJECTURE LC2 (|OC| ≤ |(score, level) pairs|) and PAIR-OC (note §15), both 0 violations on these instances and all data.

## DEAD box 18a (REFEREE-2 16 side finding, R2-N5-RUND §4, referee-2 7a02a1f2; reproduced by L-SI successor 14, 2026-10-26T10:3xZ by date -u): CONJECTURE UF-ONCE
- Statement killed: in every λ_W-constant fallback-free in-phase run S, every Even vertex makes at most one unforbid-switch (U(S) event,
  Corollary CHARGE-U). docs/si/N5-RUND-box17.md §16, §22.1.
- Obstruction: offset returns are realised. An Even vertex is tempted by W and blocked by Ξ at a gated successor, switches, goes back by
  an ordinary switch, and is blocked and unblocked again, all inside one run.
- Instances: experiments/red/so/instances/so_th_n32.pg (sha1 ae9126ad1bf963114bdd56b6e50c8c1cc571779e, 𝒞^1O) +
  experiments/si/rund/instances/so_th_n32_s0.start (sha1 2284f723…): Even 24 makes 3 U events into (24, 21) at 4 → 5, 15 → 16, 21 → 22.
  experiments/red/n5inj/instances/phase2_pk48.pg (sha1 83dead9bc3cd96a27f4754e99bb876956cd60268, two Odd choice vertices) +
  experiments/si/rund/instances/phase2_pk48_s1.start (sha1 36dc43e7…): Even 44 makes 2 U events, into (44, 11) at 16 → 17 and into
  (44, 19) at 25 → 26. `python3 -I experiments/si/rund/sched.py --one <pg> <start>` prints `VIOLATION ('UF_ONCE', …)` with exactly
  these events (pinned in experiments/si/check.sh). CHARGE, FZ, UNF, OFFUP: 0 violations on both.
- Lane fault: `sched.py --list` defaults to KMIN = 2, so the lane's 0 never covered a 𝒞^1O game (REFEREE-2: 33 of its 34 failures are 𝒞^1O).
- Unaffected: CHARGE-U (PROVED). Closed route: |U(S)| ≤ n_E.

## DEAD box 18b (L-RED 20 kill, R80, l-red 64182fe1; reproduced by L-SI successor 14, 2026-10-26T10:5xZ by date -u): CONJECTURE U-SPLIT
- Statement killed (lane note §17, not in any packet): every U event (k′, (y, z)) of a run raises y's offset or straddles a stretch_D
  boundary (D, or a gate's (Ξ, W) value, differs inside [f, k + 1]).
- Obstruction: §18's scenario, built. z's unblocking switch moves z from gate u (offset > 0) to a zero-offset gate u0, and y's U event goes
  offset 0 → 0. D, R_D and every gate value stay constant.
- Instance: experiments/si/rund/instances/usplit_rd_s3_n27.pg (copy of L-RED's experiments/red/usplit/instances/usplit_rd_s3_n27.pg, sha1
  1e9ca56d75237422ae3a3c705c56a36b139cb21f; n 27, 𝒞^2O, SPEC S3 start, no start file). `NOGEN=1 USTRUCT=1 python3 -I
  experiments/si/rund/sched.py --one <pg> -v` prints `NB k=1 f=0 y=26 z=25 a_f=20 a_k=20 off_y 0->0 …` and the single violation
  `VIOLATION ('U_OTHER', …, 0, 1, (26, 25))` (pinned). L-RED: 4 iterations, 0 fallbacks, Oink zlk OK. L-RED's earlier usplit_s3_n16 / n14 /
  n23 kill only §17's BD text, not the full STRETCH_D (R_D changes there; R80 §0a).
- Effect: the reduction "|U| ≤ Σ N_y^↑ + n·n_E·B(S)" (§17) is closed. CHARGE-U is unaffected.

## DEAD box 18c (L-RED 20 kill, R81, l-red 64182fe1; reproduced by L-SI successor 14, 2026-10-26T10:5xZ by date -u): CONJECTURE PAIR-OC
- Statement killed (note §15; packet §7): no (score, level) pair rises at two offset changes of one vertex in one stretch_D segment.
- Obstruction: the kill pattern the lane gave L-RED. One score rises at a, b, a (b > a) at three offset changes.
- Instance: experiments/si/rund/instances/pairoc_n58.pg (copy of L-RED's, sha1 4824c73cd544c12533a894d1ace902da6c73de3d) +
  pairoc_n58.start (sha1 2f5630e98f5484e5c901ad45ae1bd752a5a7a4a8). `python3 -I experiments/si/rund/lvl2.py --one <pg> <start>` prints
  `VIOLATION ('PAIROC', …, 0, 3, 57, [(0, 47, 52, True), (1, 48, 51, True), (2, 47, 49, True)])`: v = 57, W rises at 47, 48, 47 (pinned).
- Survivor: CONJECTURE LC2 holds there (|OC| 3 ≤ |SL| 5: SL = {(W, 47), (W, 48), (X, 49), (X, 51), (X, 52)}; no LC2 violation, pinned).

## DEAD box 20 (L-SI successor 16, 2026-10-26T15:11Z by date -u): the charge "root offset resets → ping-pong entries or FLIP events"
- Statement killed (a candidate charge, Lead's 15:02Z item, never claimed): every change of the root's gate offset Δ(r) = M(τ r) − M(σ̄ r) at an
  in-phase S4a transition with r a D-direct gate coincides with a ping-pong entry into r's gate region or a change of some class terminal's
  chosen exit (R69 FLIP-type event).
- Obstruction: the changes are the root's own Bellman-Ford cascade events (a downstream switch in the direct region raises the root's best
  option; note §28.2 PATH triggers), with no entry into the gate region and no chosen-exit change at that transition.
- Instance: nep90_n40 (experiments/red/rec0/instances/nep90_n40.pg + experiments/si/rund/instances/nep90_n40.start), phase@4, root 0: 32 of 63
  root offset resets have no charge but ρ at the root (`python3 -I experiments/si/root/resets.py --one <pg> <start>` prints
  R_DELTA_U=63 and R_DELTA_U_ONLYSELF=32; pinned). nep76_n40 phase@9: 13 of 51.
- Survivor: these events lie inside FREEZE-A pieces and are bounded there (FREEZE-A (c), RESET-PIECE (i)).

## DEAD box 21 (L-SI successor 17, 2026-10-26T16:06Z by date -u): own candidates C-ONCE and UE-ONCE_C (never claimed; note docs/si/N5-GCX-box21.md §4)
- Statements killed: (C-ONCE) inside a C-interval (A_c non-increasing, D ∩ U_c constant, every D-direct gate offset constant) no vertex
  migrates twice between gate regions; (UE-ONCE_C) inside a C-interval every Even edge is unforbid-switched (CHARGE-U's U event) at most once.
- Obstruction (both): Bellman-Ford staggering inside the first |U| − 1 states of the interval. A short route through one gate is taken
  first, a longer better route through another gate arrives later, and the vertex (or the edge's tail) moves again.
- Instances (N5 via experiments/new/box21/n5x.py, read-only; SPEC S3 start; climbed by experiments/si/root/climbmig.py):
  - experiments/si/root/instances/cone_n65.pg (sha1 3e95fca9088f6a52cdf16325fe06933296ed357e): phase@1, class 8, C-interval [0, 4], vertices 2,
    14, 20, 26, 29, 30, 44, 59 migrate twice between the non-direct gates 12 and 64. `python3 -I root/gcx.py --one <pg>` (from experiments/si)
    prints MIG2_cint=1 (pinned). cone_n69.pg (sha1 dd03ba782ca821491ad5c54303ab61def7c7aff1): one interval of 19 transitions, up to 3
    migrations per vertex (gates 20, 29, 35).
  - experiments/si/root/instances/ueonce_n27.pg (sha1 c90d5ab8569a93bba3389002e0c85bb64bb0c214): phase@1, C-interval [1, 10], edge (10, 23)
    has U events at k = 1 and k = 5. `UEV=1 python3 -I root/gcx.py --one <pg>` prints UE2_Cr=1 (pinned). Also lib41
    experiments/si/xing/instances/zcl_cu_n48.pg with a random start (edge (16, 20), C-interval [7, 23]).
- Survivor: CONJECTURE UL_C (no U event at index ≥ |U_c| − 1 of its C-interval): 0 violations on everything above, the UF-ONCE killers and the
  libraries with KMIN 1; the killers' repeated U events on one edge all sit at C-cuts.

## DEAD box 21b (L-SI successor 17, 2026-10-26T16:48Z by date -u): the naive cyclic settling order (own; note docs/si/N5-GCX-box21.md §9)
- Statement killed (never claimed): in the cyclic abstract model (§8), a changer at transition k whose new play contains no other changer at k
  (a DEEPEST changer) has made its final change. It was the candidate for lifting §7's "most downstream changer is final" to cycles.
- Obstruction: changes on the plays of non-chosen successors. A successor that is not viable at k (its play runs through v) can change at k
  and become viable and better at k + 1.
- Instance: experiments/si/root/abscyc.py DEEP (`python3 -I root/abscyc.py --deep` from experiments/si prints DEEP REPRODUCED; pinned):
  non-terminals 0, 1, 2; succ(0) = succ(1) = {2, t3, t4}, succ(2) = {0, 1, t3}; w = (2, −8, 0); t3: (h, T) = (51, 101), t4: (2, 29); start
  (2, t4, 1); vertex 1 is deepest at transition 0 and changes again at transition 1.
- Survivor: CONJECTURE FINAL-EACH (every transition holds some vertex's final change; 0 violations in 22,989 transitions), which implies
  ≤ n steps.

## DEAD box 22 (L-SI successor 18, 2026-10-26T17:40Z by date -u): PER-EXIT-MONO (own candidate; note docs/si/N5-EXIT-box22.md §5)
- Statement killed (never claimed): for x ∈ Q_c and an exit p, off(x; p) = κ(x) − κ(p), read at the states where par(x) = p, never falls over the
  whole phase, including when x returns to p after leaving it. Inside one x-piece this is OFFSET-MONO (P-N5-OFFMONO). The candidate would
  have bounded same-exit offset rises per (x, p) over the phase instead of per piece, which is where CHAIN-COUNT's D·(EXIT_x + …) factor comes from.
- Obstruction: while x routes elsewhere, κ(p) can rise more than κ(x). x's options towards p are then not chosen, and nothing ties their
  offsets to κ(x). On return the offset can be lower.
- Instance: nep90_n40 at its start (experiments/red/rec0/instances/nep90_n40.pg, experiments/si/rund/instances/nep90_n40.start):
  exitx.py counter PEM_drop_ret = 6 (of 45 returns). Also 5 / 4 / 8 / 7 / 10 drops on nep76, long121 and L-NEW's three climbs
  (experiments/si/root/logs/exitx_long10.txt).

## DEAD box 23a (L-SI successor 19, 2026-10-28T23:1xZ by date -u; Lead 23:10Z): CONJECTURE ABS-DEPTH-TIE for general (non-keep) tie rules
- Statement killed (a lane CONJECTURE, P-N5-DEPTH-box22 §6, never signed): in the cyclic abstract model, the run is fixed within max d* steps
  without GEN, for any deterministic tie rule.
- Obstruction: a NON-KEEP tie rule (one that may leave a current choice that is still a maximiser) lets a vertex change while all its inputs
  (arena values, viability) are constant. The depth argument charges each step to a successor's change, so it fails.
- Instances (both referees, independently):
  - REFEREE, docs/referee/R-N5-DEPTH.md §3, DEPTH-N2: the one-vertex LOC game of R-N5-GCX (docs/referee/scratch/loc_cex.py; one non-terminal v,
    w(v) = 0, terminals a (h 0, T 0), b (h 1, T 5), c (h 2, T 5), s_0(v) = a), max d* = 1, fixed only after 2 steps under the rules "anti" and
    "sizedep" (and a hash rule in random models).
  - REFEREE-2, docs/referee-2/R2-N5-DEPTH.md §3, N-DEPTH-3: non-terminals 0, 1; terminals T2 (h 0, T 2), T3 (h 2, T 2); succ(0) = {T2},
    succ(1) = {0, T2, T3}; w = (−2, −1); start s(1) = 0; under rule "flip" the run s(1) = 0 → T2 → T3 is fixed after 2 steps, against max d* = 1.
- Survivor: CONJECTURE ABS-DEPTH-TIE_keep (for tie rules that keep a maximal current choice) stays OPEN; no counterexample in either referee's
  data (P-N5-DEPTH-fixes-box22 F2). CONJECTURE STATIC-DEPTH-TIE (N5's own S1 rule) is not touched. Same mechanism as G-GCX-1 (LOC).

## DEAD box 23b (L-SI successor 19, 2026-10-28): index of the box 23 dead ends recorded in docs/si/N5-ALT-box23.md (instances and obstructions there)
- XR-LIN (§8): l121reader_n41, an Odd READER's Ξ changes 86 > 2n = 82 times in one phase (run unchanged; condition (R) of REFEREE's READER-INV holds).
- SW-LIN (§10): swlin_kill_n26, one Even vertex switches 27 > n = 26 times in one phase; fallbacks re-arm its option cycle (n5b agrees).
- GATE-ONEWAY (§4): pp_K48_n449, gate 447 (out-degree 3) alternates 48 times in one global C-interval.
- TOP-ONCE (§4): lev_l_sc, z = 0, the same top change 7 times in one run (counter recursion live).
- FRESH at run scope (§4): x32_rand48, 22 return-only transitions (a D = ∅ wave, not alternation).
- FRESH2 (§4): post31_n48 t = 20. FRESH3 (§3): ret14_n48 t = 21 (one-vertex flip-flop of Even 27 and gate 0).

## DEAD box 24 (L-SI successor 20, 2026-10-29T00:1xZ by date -u): CONJECTURE RUN-LIN (and RUN-LIN-OPT)
- Statement killed: «every fallback-free run of a phase has ≤ 2n transitions» (N5-ALT-box23 §13), and its τ-optimal form RUN-LIN-OPT
  (docs/si/N5-RUNLIN-box24.md §3).
- Instance: experiments/si/runlin/instances/runfam_K10.pg (sha1 faf218f125d1516d4677393991d53a08a9f4f3bb; start runfam_K10.start,
  56e4dec67323e6f5b832ac2d95ef832d6ce3a013), n = 49: one phase [1, 100], 0 fallbacks, a fallback-free run of 99 > 98 transitions; I_τ = ∅ at
  every state. n5x = L-COMP's n5b (identical 101 states) = experiments/new/n5.py (100 iterations, 0 fallbacks); check_sol2: zlk OK, strategies
  verified. Family mkrunfam.py K: run = 74 + ⌊5K/2⌋ (K ≤ 34), then 2n + 13 (n = 39 + K); runfam_K40 (n 79): 171.
- Obstruction: one Odd choice vertex whose options are the two ends of a two-way Even corridor; every σ̄ change restarts a wave along the
  corridor (one Even switch per transition), so the run is a sum of up to G + 1 waves of length up to n − 1; two full waves and a partial
  third already exceed 2n. Linearity is not killed (run ≤ 2.17n on the family).

## DEAD box 25 (L-SI successor 21, 2026-10-29T06:13Z by date -u): CONJECTURE L-WAVE (docs/si/N5-GRUN-box25.md §5)
- Statement killed: «between two consecutive non-L REL cuts (cuts other than length-only changes of Ξ at the changing gates) of a fallback-free
  run, or the run's ends, there are ≤ n − 1 transitions».
- Killer: experiments/si/grun/instances/lwkill_n31 (.pg sha1 4c083c557b69f7ceb263ae492bce33ff1ea6887e, .start sha1
  177dd289ae04262e5ce63cdbf34bde04bcf6b17c; n 31, one Odd choice vertex u = 5), found by grun/gclimb.py OBJ=LW from run49_n32 in 358 steps.
  Run [2, 40] (38 transitions, one phase, 0 fallbacks); REL segments [2, 7], [8, 28], [29, 38], [39, 40]; the cuts 7 → 8 and 28 → 29 change
  only the length of Ξ(5) (path sets 1073741824 and 838860800 unchanged across them), the cut 38 → 39 changes its path set. So the gap [2, 39]
  has 37 > n − 1 = 30 transitions. n5x = L-COMP's n5b (identical 41 states) = experiments/new/n5.py (40 iterations, 0 fallbacks); check_sol2:
  zlk OK, strategies verified. Every REL segment is within STATIC-DEPTH-REL's bound (relseg PASS; longest 20).
- Obstruction: the path set of Ξ(5) changes INSIDE segment [8, 28] (from 1073741824 to 838860800) while σ̄(5) stays on option 28: a P-change of
  a gate's value without a σ̄ change, which is no cut. L-WAVE counted P-changes only at cuts. Refined CONJECTURE L-WAVE′ (events also at every
  P-change of Ξ at an Odd choice vertex of RO_b): holds on the killer (max gap 19) and on alt_all (default and pinned starts); OPEN.

## DEAD box 26 (L-SI successor 22, 2026-10-29T07:0xZ by date -u (07:04:10)): candidate invariants for CONJECTURE L-WAVE′ (docs/si/N5-LWP-box26.md §3)
Lane candidates, never claimed; each would have proved L-WAVE′ (or a 2n form). Gap [x, b] as in the note §0 (b = y − 1 when the gap closes
at an event y). Engine n5x via root/common.rows; killer pins grun/out/lwp_a (.pg sha1 19d105416929800709707a2489b335a6a936e883, .start
ebe3da481098f568ee171b061ab70e2d0f786bbd; n 26, gap [1, 26] of 25 = n − 1 transitions, one gate u = 4, L-cuts at 5 and 16) and lwp/out/xk_k
(.pg 1ad8d0036d3d1503b8f672199110d3f41c65030a, .start a2e00ea7c3383b9cd35d21f306c77c8fc3f57684; n 26, gap 24 on [1, 25]).
- VS-STEP («every transition of a gap makes some vertex value-settled»): lwp_a, 13 of 25 transitions (lwp/vstep.py KEY=V). Obstruction: the
  L-cut 15 → 16 changes the length of Ξ at 13 vertices, so values reached in the snake are not final.
- PS-STEP («... (c, P)-settled»): lwp_a t = 2; alt_all 109 (default) / 144 (pinned starts) failing transitions, e.g. lend27_n24 [5, 7] t = 6.
  Obstruction: vertices pass through intermediate path-set levels (lwp_a: three levels).
- PV-STEP («... (c, P)- or value-settled», a 2n bound): lwp_a t = 2 (5 Even switches, 6 path-set changes, none to a final level or value).
  0 failures on alt_all: the killer is the climb instance.
- GAP-DEPTH («gap ≤ max_Q d at the reference state», STATIC-DEPTH-REL across L-cuts): lwp_a 25 > 23; xk_k 24 > 23; alt_all 8 + 5 gaps
  (gci2_n12: gap 6, depth 0). Obstruction: the gate's competitors rise off the end-state plays (GRUN §5 READING), and that time is not depth.
- LAST-SWITCH per gap («every transition of a gap is some Even vertex's last switch in the gap», gap ≤ |Even|): lwp_a t = 2, 3 (23 switching
  vertices, 25 transitions; the excess equals the 2 L-cuts); xk_k one transition. 0 failures on alt_all and lib41. The per-REL-segment form
  (CONJECTURE SEG-LAST) and SWL (gap ≤ switchers + L-cuts) survive.
- Kill searches for L-WAVE′ itself (no kill): note §1.
- CYC-SET («every J_b-cycle vertex of a REL-admissible segment is W- and H-settled from the segment's start»; would remove (H4′_rel) from
  Theorem LAST-STEP, note §7): run34_n40 (experiments/red/n3/instances, pinned start), segment [11, 14], 14 cycle vertices settled only from
  12-14 (lwp/laststep_alt_start.txt); and lwp/out/h4a_k.pg (n 60, sha1 957c7c9e2ce5a6d57890e42b0e8ca0a0911ecefd, default start), segment
  [0, 4], cycle vertices settled from 1 and NO frontier vertex at t = 0 (found by lwp/xclimb.py OBJ=H4 from dl_4_4). Obstruction: a J_b-cycle
  settles in one transition with its unsettled Even vertices switching together (1: 28 → 59 and 37: 6 → 58 at t = 0); SEG-LAST holds there.
- K-ARENA («at every step some terminal part K of J_b on the unsettled set has σ_b(v) in v's S4a arena for all v ∈ K»; with GEN_W it gives
  SEG-LAST without (H4′_rel), note §8): lwp/instances/karena_kill_n71.pg (n 71, sha1 8b659497688c47075235957ae1e636b5564ec235, default
  start; found by lwp/xclimb.py OBJ=KA from cycset_kill_n60 in 511 steps). Segment [0, 4], t = 0: the only terminal part is K = {1, 3, 35, 41,
  46, 50, 64}; 41 has σ_0(41) = 50 ≠ σ_b(41) = 35 and (41, 35) is not improving at 0 (it is at 1, after 35 switched 46 → 50 at 0). K settles in
  two layers (35, 46, 50 from state 1; the rest from 2). Obstruction: an Even vertex of K whose honest J_b-successor is in K and still
  switching. SEG-LAST holds there (1 and 35 switch at 0 for the last time).
- WX-ARENA («at every step some terminal part is a single vertex or has an off-target W-exit vertex, i.e. one whose W-J_b-successor is
  settled, with its target in the arena»; with the per-vertex Lemma W-EXIT it would give SEG-LAST): lwp/instances/cycset_kill_n60.pg at
  t = 0 and karena_kill_n71.pg at t = 0 (lwp/laststep.py WX_V=1 on each). Obstruction: there the last switches at t (1 and 37 in
  cycset_kill_n60) are not W-exits; the step is a joint switch of the part (Theorem K-REDUCTION covers the first instance, nothing covers the
  second).
- SET-STEP («at every step of a REL segment some switcher is W- and H-settled from t + 1»; it implies SEG-LAST): lwp/instances/
  setstep_kill_n71.pg (n 71, sha1 b6360888a8180a9afef84c38845500f46626b548, default start; found by lwp/xclimb.py OBJ=KA from cycset_kill_n60). Segment [1, 4]: at one step no
  switcher is settled from t + 1 (lwp/seglast.py SS_V=1), while SEG-LAST holds (every step is still some vertex's last switch). Obstruction:
  the last switch at that step goes to a target whose plays still change later (layered settling of a terminal part of 10 vertices).

## DEAD box 27 (L-SI successor 23, 2026-10-29T08:25Z by date -u (08:24:59)): W-GROW (docs/si/N5-LAY-box27.md §2-§4)
- W-GROW («in a REL-admissible segment with GEN_W, the W-settled part of E_b grows at every transition»; equivalently, by Theorem SINK-STEP,
  «some W-sink is arena-ready at every step»; with Theorem SINK-STEP it would prove SEG-LAST without (H4′_rel)): killed by
  experiments/si/lay/instances/wgrow_kill_n90.pg (n 90, sha1 f9a7ef090b3df5bb4293301e6bd1236e33a92cd0; start = N5's S3 start, written out
  as wgrow_kill_n90.start, sha1 a4ead4deae5534731a199c8697c072f407643ca2), found by lay/wclimb.py (score: steps with no frontier vertex +
  unready W-sinks) from lwp/instances/karena_kill_n71 in 10,666 steps. Segment [0, 3], t = 1: the only W-sinks are 37 and 57 (σ_1 = 1, target
  5 for both; 5 is W-settled from 0 but H-settled only from 2), and (37, 5), (57, 5) are not improving at 1 (Ξ_1(5) ⋫ Ξ_1(1)); they become
  improving at 2 and both switch then for the last time. Checks: n5b (L-COMP's independent implementation, SPEC mode) gives the identical
  state sequence (root/n5bcmp.py: 9 iterations, 1 fallback, identical: True); n5b's improving-edge sets equal n5x's at t = 0, 1, 2; W-plays
  recomputed from (σ_t, τ) directly (τ constant on [0, 3]). Obstruction: the W-sinks' common target 5 is W-final while its honest value
  still rises at 1 → 2 (its own H-chain), so the arena at 1 excludes it. SEG-LAST holds (43 and 55 switch at 1 for the last time), and so
  does CONJECTURE H-GROW (the H-sink 55 switches to its target 48 at 1).
- H-GROW («... the H-settled part of E_b grows at every transition»; equivalently «some H-sink switches to its target at every step»; with
  Theorem SINK-STEP it would prove SEG-LAST without (H4′_rel)): killed by experiments/si/lay/instances/hgrow_kill_n89.pg (n 89, sha1
  998a4a5e770c97b409ebf9f0a9d0ca08fac9bcbd; S3 start written out as hgrow_kill_n89.start, sha1 5895810a61760e4180d70202911768bd75f2beea),
  found by lay/wclimb.py OBJ=H from lwp/instances/cycset_kill_n60 in 1,208 steps. Segment [1, 8]: H-GROW fails at 6 of its 7 steps
  (t = 1..6): the H-sinks 1, 46, 73 (σ = 27, target 23, ready from t = 1) wait while a W-frame snake settles one W-sink per step
  (38/70 → 48, 49 → 38, 64 → 49, 77/78 → 64, 22 → 77, 28/33 → 22), and switch only at t = 7, when their W-chain end 34 settles. Checks: n5b
  state sequence identical (13 iterations, 0 fallbacks); honest successor maps (σ̄) and improving sets equal n5b's at all 14 states.
  Obstruction: an H-sink's W-chain is still unsettled, so S4a (W-optimal) does not yet take its target. W-GROW, SINK-GROW and SEG-LAST hold.
- SEG-LAST (CONJECTURE, box 26 §4: «in every maximal REL-admissible segment [a, b], every transition t → t + 1 (a ≤ t < b) is the last
  switch in [a, b] of some Even vertex»; 0 failures in 3,134 library segments and every box-26 climb) and SINK-GROW (box 27: «at every step
  of a REL segment the W-settled or the H-settled part of E_b grows»; it implies SEG-LAST by Theorem SINK-STEP): killed by
  experiments/si/lay/instances/seglast_kill_n110.pg (n 110, sha1 8a2201816d3a522cd2c4da238678d9f6b075f68a; S3 start written out as
  seglast_kill_n110.start, sha1 107cbf0828cdf1120d8f70b80cdef0e75e9908a4), found by lay/wclimb.py OBJ=S from hgrow_kill_n89 in 6,286 steps.
  Run = phase [2, 8] (τ changes at 1 → 2, no fallback), one maximal REL segment [2, 8] (6 transitions; (H4′_rel) fails: a 16-vertex
  J_b-cycle {1, 4, 7, 26, 31, 32, 34, 35, 37, 40, 69, 75, 83, 85, 106, 109}, none settled before 8). At t = 2 the ONLY switch is vertex 1:
  82 → 25; vertex 1 switches again at t = 7 (25 → 21 = σ_8(1)). So 2 → 3 is no vertex's last switch. Observed GEN_W holds on [2, 8] (0
  failures, by n5x's W-values and by S1-rank valuations computed from n5b's plays). Checks: n5b (L-COMP, SPEC mode) state sequence identical
  (16 iterations, 0 fallbacks); lay/relcheck.py recomputes phase, run, REL-admissibility (σ̄ from n5b on RO_b, CW_b, CH_b), maximality,
  the switch history and observed GEN_W from n5b ALONE (lay/relcheck_seglast_kill_n110.txt). Obstruction (the deadlock of note §5): at
  t = 2 the only W-sink 37 (target 35) waits for 35's honest value, and the only H-sink 1 (ready, target 21) waits for its W-chain (1 → 31 →
  … → 37 → 35); S4a breaks it with an INTERMEDIATE switch of 1 (82 → 25), after which 37 is ready (t = 3) and a W-snake 37, 40, 69, 26, 4
  settles one vertex per step; 1 reaches 21 at t = 7. What survives here: b − a = 6 ≤ 7 = Even vertices switching in [2, 8] (all in E_b,
  |E_b| = 48), so the COUNT forms (SWL-type) and b − a ≤ n − 1 are not touched.
- SEG-LAST, smaller killer (box 27): experiments/si/lay/instances/seglast_kill_n29.pg (n 29, sha1 976fc4e88a514b1615ef81caa8b4af17a42b1c5f;
  .start sha1 9afeb2aaf26dd63460216185b6a405a02b07474f), seglast_kill_n110 shrunk by lay/wclimb.py OBJ=M (keep a SEG-LAST failure, minimise
  n). Run [2, 4] (phase key (λ_Ξ, τ): τ changes at 1 → 2, λ_Ξ at 4 → 5) is one REL segment; t = 2: the only switch is vertex 1, 9 → 23 (an
  H-sink, target 19, ready; the only W-sink 25, target 4, not ready); t = 3: 1 → 19 and 25 → 4, both final. Reproduced from n5b alone,
  run boundaries from n5b's own (λ_Ξ, τ) key included (lay/relcheck_seglast_kill_n29.txt); observed GEN_W holds.
- PSI-DROP (box 27, note §7: «PSI1 := |U^W_t| + |U^H_t| + unready W-sinks strictly drops at every transition of a REL segment»; it would
  give b − a ≤ 3(n − 1) on REL segments; 0 failures in 14,103 library steps and on every earlier pin): killed by
  experiments/si/lay/instances/psidrop_kill_n70.pg (n 70, sha1 9cd26eeded045052b769175e3c18dbb72936d404; S3 start written out as .start,
  sha1 6ba80572a67873884d21a7cfd26140f7950c2d59), found by lay/wclimb.py OBJ=P from seglast_kill_n29 in 4,107 steps. Segment [2, 5], t = 2:
  the switches are 1: 14 → 48 (intermediate) and 29: 8 → 31 (final, but 29 is neither a W-sink nor an H-sink, so nothing becomes settled
  in either frame), and the only W-sink 24 stays unready: PSI1 = 24 at 2 and at 3. n5b state sequence identical (9 iterations, 1
  fallback). Obstruction: a final switch of a non-sink vertex is progress PSI1 does not see. SEG-LAST, SEG-COUNT hold there.

## DEAD box 28 (L-SI successor 24, 2026-10-29T10:28Z by date -u (10:28:08)): (a) of the SEG-COUNT charging, INTER-JOINT, DL-HSW, DL-NEXT, GROW-PERSIST (docs/si/N5-CHG-box28.md §3, §5)
- (a) in its general form EARLY («an H-sink h that is not a W-sink makes its last switch exactly at s_h = fW(jW h) − 1, together with its
  W-chain»; needed by box 27 Corollary JOINT to charge a deadlock step): killed by the box-27 pin experiments/si/lay/instances/wgrow_kill_n90.pg
  (sha1 f9a7ef090b3df5bb4293301e6bd1236e33a92cd0, .start a4ead4de…), segment [0, 3]: H-sinks 34, 47, 61 at t = 0 switch at 0 to their
  targets for the last time, their W-chain settles at 3 (s_h = 2); 55 at t = 1 likewise. chg/suffix.py EARLY FAIL. It holds on
  psidrop_kill_n70 and on the ladders k12/k24/k48. Obstruction: an H-sink may go straight to its target before the target's W-play is final.
- INTER-JOINT («such an h that makes an INTERMEDIATE switch, to neither σ_t(h) nor σ_b(h), finalizes exactly at s_h»; the ladder's pattern):
  killed by experiments/si/chg/instances/interjoint_kill_n70.pg (n 70, sha1 79a7c76af6e44bce47a6bd2c8e52b47ddf926d23; .start sha1
  9b313151306069cb9c1f470bf0846730ae111331), found by chg/cclimb.py OBJ=IE from red/ul/instances/ladderd0_k12_n48 (pinned start) in 2,971
  steps. REL segment [1, 7] = the fallback-free run; H-sink 10: σ = 32, 21, 36, 24, 24, 28, 28 on [1, 7], target 28, jW(10) = 0 W-settled
  only at 7, so s_h = 6, but L(10) = 5; about 25 H-sinks with target 28 do the same. Checks: n5b state sequence identical (root/n5bcmp.py:
  10 iterations, 1 fallback); chg/ijcheck.py from n5b alone (run (1, 7), REL segments [(1, 7)], REL fails at 0, sink status, L = 5, s_h = 6,
  observed GEN_W 0 failures). SEG-COUNT holds there. What the proof needs instead: no early finalization must come from the deadlock
  condition (CONJECTURE DL-JOINT, 15/15) or the charging must avoid it (CONJECTURE DL-RUN).
- DL-HSW («at a deadlock step only H-sinks switch»): killed by experiments/si/lay/out/c_sk.pg (box-27 climb output, committed), segment
  [5, 14], t = 5: 1, 41, 48, 127, 131 switch, only 1 is an H-sink (also lay/out/d29a, d29c, ll29). Not needed.
- DL-NEXT («the step after a deadlock step is a W-growth step»): killed by experiments/si/lay/out/d29a.pg (default start), segment [4, 20],
  t = 4: at 5 no W-sink is ready (30 finalizes, a non-sink); also d29c, d29d, p29. Not needed.
- GROW-PERSIST («after the first growth step of a REL segment every step is a growth step»; all 13 deadlock segments of the box-27 climbs have
  the pattern D F* G*): killed by experiments/si/chg/instances/growpers_kill_n73.pg (n 73, sha1 ff73bab1641c7f5b8f0756b25df2b24709d1bcdb;
  .start b496c9b9dffb33880c4fe632ad47d606ef8ffd84), chg/cclimb.py OBJ=GP from psidrop_kill_n70 in 5 steps: segment [2, 5], pattern G F G
  (t = 3: vertex 1 finalizes, no sink settles); n5b state sequence identical (9 iterations, 1 fallback).
- DL-RUN («a deadlock step of a REL segment is the first transition of its fallback-free run»), DL-FIRST («... the first step a of its
  segment») and NEWFINAL («at a transition t > r0, some switch to an edge outside the arena of t − 1 is a last switch»; DATA had 0 failures on
  ~12,000 library and 240 climb late transitions): killed by L-RED's hand-built R105 instances (claude/l-red 22d7c6ab, experiments/red/seg/
  instances; byte-identical copies in experiments/si/chg/instances/red/): segcount_kill_n20 (sha1 2783f64d82f271ebc9a26b470b26a9938fd5295c,
  .start 97ba6b298917676e10cb209e21f49ee442b73686), run [0, 4] = one REL segment, deadlocks t = 0 and t = 2 (r0 = 0); segfam_k3_n29 (sha1
  0d242a9b…, deadlocks 0, 2, 4), segfam_k8_n79 (sha1 ddb67eff…, deadlocks 0, 2, …, 14). chg/dlock.py: DLRUN FAIL, DLFIRST FAIL, NEWFINAL FAIL;
  n5x and n5b identical (root/n5bcmp.py, 0 fallbacks). Obstruction: after r0 a deadlock is still possible when the H-sink's next
  intermediate option enters its arena only through a W-sink's final switch (C_i through w_{i−1}). The same instances kill CONJECTURE
  SEG-COUNT (L-RED R105, the charging's injectivity (b)).
- DL-SEP («two deadlock steps of one REL segment are separated by a growth step»), DL-NOCONSEC («no two consecutive deadlock steps»),
  FROZEN-COUNT («a maximal run of non-growth steps is no longer than the Even vertices switching in it»), DL-SOMEH («some H-sink switches
  at every deadlock step»), ZIG («... the end of an unready W-sink's H-chain switches»), and with them the conditional length bounds (L2)
  b − a ≤ 2·FIN and (L3) b − a = O(n²) of N5-CHG-box28 §6: killed by experiments/si/chg/instances/dlsep_kill_n70.pg (n 70, sha1
  e500ea47e1dc0163b32a97042ff9752daf6db83a; .start sha1 f5569821f5d951de4922a4a9853b3bb4c9bf0284), found by chg/cclimb.py OBJ=GP from L-RED's
  segfam_k3_n29 (copy chg/instances/red/) in ~10,000 steps. The fallback-free run [0, 12] is one maximal REL segment: 12 transitions,
  pattern F D D D F D D D D D G G, deadlocks t = 1, 2, 3, 5, 6, 7, 8, 9; one frozen run [0, 10) with 9 switching Even vertices; t = 10
  finalizes 11 vertices. Deadlocks 5, 6, 7 are a snake of intermediate switches of non-sinks (4: 31 → 10; 15: 23 → 4; 35: 23 → 15).
  Checks: n5x and n5b identical (root/n5bcmp.py: 16 iterations, 0 fallbacks); lay/relcheck.py from n5b alone: run (0, 12), REL segments
  [(0, 12), …], REL fails at −1 (run start), every listed t is no vertex's last switch, observed GEN_W 0 failures. SEG-COUNT-type counts
  hold there (12 ≤ 26 switchers). Obstruction: deadlocks are not tied to the sink structure; an honest snake of intermediate switches
  can run inside one frozen sink structure.
- LENE («every maximal REL segment has b − a ≤ |E_b|»; tight on L-RED's R105 family) and LEN2 («b − a ≤ 2·SW + 1»): killed by L-RED's R106
  pin runquad_K8_m30_n192 (claude/l-red 86f24219, experiments/red/seg/instances; byte-identical copy experiments/si/chg/instances/red/,
  sha1 ebaa6ac57ec60948fb986210c27479cb3a7961d9, .start 4ba9f8605a1b18891dffb40d508bce929cf7c952): one fallback-free run [0, 263] = one maximal
  REL segment with |E_b| = 49, SW = 47 switching Even vertices, 218 deadlock steps (chg/lenstat.py). Obstruction: two pivots climbing in
  alternation drive a reactor chain back and forth; each reactor switches 2K − 1 = 15 times (chg/pervert.py), so switches per vertex, not
  vertices, carry the length.

## DEAD box 29 (L-SI successor 25, 2026-10-29 by date -u; docs/si/N5-FRZ-box29.md §4-§5): W-frame and Ξ-frame forms of R17's Lemma P inside frozen W-phases
- «A W-phase (in-phase run without fallbacks and λ_W changes, σ̄ free) has ≤ n − 1 W-changing transitions»: experiments/si/runlin/instances/
  x135_n59.pg (sha1 e71e8af0a7e0d0d07b7f609ee88628151af99002, start 4afb7e8c1eb830c46715a893d0295e77667f5418): W-phase [1, 136], 135 W-changing
  transitions > 58, |D| = 1, 11 σ̄-changes (frz/wphase.py); n5x and n5b identical (root/n5bcmp.py: 136 iterations, 0 fallbacks). Obstruction:
  every σ̄-change restarts a Bellman-Ford wave (as in RUN-LIN, box 24); its seven frozen W-phases have ≤ 43 each.
- SETTLE («in a frozen W-phase [a, b], W_{a+k}(x) = W_b(x) once W_b(x).length ≤ k») and RD («a W-rise at step k has length ≥ k»):
  experiments/si/frz/instances/s_elim24_final.pg (sha1 ddb99d6c103e4d60b1b1d4a6b8c3b5ab9070b21b; copy of orlens/instances/
  s_elim24_final.pg) with its S3 default start written out (s_elim24_final.start, sha1 f576e9ef3c67584b82c0ac15ebee19e0e2b9c333): frozen W-phase [17, 33], |D| = 1, x = 11 has final length
  3 and changes W at k = 16 (frz/settle.py, frz/risedepth.py); n5b identical (66 iterations, 4 fallbacks). Obstruction: optimism-trapped
  vertices (plays into D, where τ flatters Even) move late with short plays.
- SETTLE_X and RDX (the same in Ξ): experiments/red/ul/instances/ladderd0_k12_n48.pg (L-RED's ladder; sha1
  c654bf9ec7445726f7526738f9c5efc6bc1049fd, start 674f6eeb580b88de302d0b968d1cf79d05e0b295): frozen W-phase [0, 13], |D| = 14, x = 14 has
  final Ξ-length 2 and changes Ξ at every step k = 2..13 (one D-gated rung per tick); n5b identical (14 iterations, 0 fallbacks).
  Obstruction: Ξ-rises driven through D gates are not depth-ordered; FW-BF still holds there (13 ≤ 47).
- CASEA-W (an edge outside the arena is never W-better than σ_t(x)), CASEB-Ξ (an arena switch is never Ξ-better than S4a's choice),
  B-MONO (the blocked set is monotone), FRESH (every transition enters a not-yet-entered edge), ENT1 (an edge is entered ≤ once per
  W-phase): all on x135_n59 inside frozen W-phases (frz/caseA.py: 1,721 / 278 triples; frz/blocked.py: 21 growth and 5 shrink events;
  frz/fresh.py: 59 re-entry-only transitions, an edge entered 3 times).
- TRAP-MONO («inside a frozen W-phase the trapped set S^p (vertices whose (σ, τ)-play meets D) only grows», and its value form
  {W ▷ Ξ}; N5-FRZ-box29 §7): play form killed by experiments/si/frz/instances/fbrestart_cex_n12.pg (sha1
  35223b6c46750b2c1c961d68485025a9a5e69d87, start a2bf7077e797f2ea50ebb05ac9baabc4668a443e = S3 default written out; copy of
  new/box35/instances/fbrestart_cex_n12.pg): frozen W-phase [4, 5], vertex 8 leaves S^p at t = 5; value form by
  n5-epoch/instances/lend107_n32 (sha1 ab4c9811b311e303e5d41a9e923766a4b3fdae33, start 9df4ea2ceafe43c4a7d88ef1e1f262101d7f0c35), frozen
  W-phase [27, 38], vertices 1, 18 leave at t = 28 (frz/epoch.py); n5b identical on both (5 iterations / 2 fallbacks; 112 / 10).
  Obstruction: a trapped vertex can find an honest D-free route at least as good as its optimistic one; the epoch count is not ≤ n.

## DEAD box 31 (L-SI successor 27, 2026-10-29T15:59Z by date -u): the gap-step Lemma P and three single-frame variants (docs/si/N5-SPC-box31.md §2)
- GAP-STEP Lemma P («in a same-pair frozen W-phase, W_k(x) ⊵ value(r) for every simple G_τ path r to a cycle node of the phase start
  with |r| ≤ k − a − TC_k, TC_k = basin-changing transitions before k»; the Lead's untried idea in its natural form), and the same with Ξ_k
  vs G_σ̄ paths, W_k vs G_σ̄ paths, W_k vs paths of the edges admitted at some state: killed by
  experiments/si/runlin/instances/runfam_K100.pg (sha1 86cf1884919b223c18f982eed6a00a4256a501dd), start runfam_K100.start (sha1
  843b9f4e83a21d8ee5bd56df97f7b43f59edc394), frozen W-phase [52, 167], n 139, D = {5}, c₁ = c₂ = 20: lag 113 with TC = 2 (forms: 109 / 108 /
  108); core/sp.py; n5b identical (root/n5bcmp.py: 293 states). Obstruction: a long-lived F1 refusal (vertex 26 refused (26, 27), W-better
  from state 69 at the latest, adopted at 164 → 165) during a trapped wave; W never changes at 26 meanwhile, so no single-frame Lemma P
  holds, while WCH = 115 < n − 1. What survives: the timely Lemma P (GP / GP+, §3) and FW-R (§4).
- CONJECTURE R-LIN (box 31 §5: «a frozen W-phase has at most n − 1 late adoptions», R counted per (vertex, transition); stated in
  l-si 76c83301): killed by experiments/si/core/instances/rlin_cex_n40.pg (sha1 670ba1ffc22c8f9b170e11ca3e43c33cee9329ca), start
  rlin_cex_n40.start (sha1 e488c00fe1359818b9a665a415cc7b2962015318), frozen W-phase [1, 11], n 40, |D| = 1 (gate not tail-disjoint): R = 129
  in 10 transitions (core/gp.py PLUS=1, core/late.py); n5b identical (13 iterations). Found by core/spclimb.py SCORE=r from
  n5-epoch/instances/lend13_n16. Obstruction: many vertices adopt in one transition; the per-transition count R_T (FW-R′) replaces R.

## DEAD box 32 (L-SI successor 28, 2026-10-29T17:37Z by date -u 17:37:12): CONJECTURE R*-TC in every frozen W-phase (docs/si/N5-RTC-box32.md §2)
- CONJECTURE R*-TC («R*_T ≤ TC in every frozen W-phase», docs/si/N5-SPC-box31.md §6): killed by experiments/red/fbx/instances/kt6_n58.pg
  (sha1 41d4f7cbe8644ac77bac9e2fd03a17ed4b2c7915), S3 start written out as experiments/si/core/instances/kt6_n58_S3.start (sha1
  3ec0dab4b7769651de02ae86effec0318cfe7056); frozen W-phase [5, 20], n 58, D = {18}, λ_Ξ(18) = 18 ≠ λ_W(18) = 0, U = ∅: R*_T = 5, TC = 0
  (core/inj.py); n5b identical (38 iterations). Obstruction: c₁ ≠ c₂ forces TC = 0 (TRAP-FIX) while blocked edges inside the single basin are
  adopted later (no prefix comparison across different tails). What survives: R*-TC restricted to the same-pair core (CONJECTURE R*-TC(SP),
  0 failures on 255 phases) and Lemma LATE-BASIN.

## box 33 (L-SI successor 29, docs/si/N5-ODD-box33.md §1; experiments/si/odd/reent.py, check.sh «box 33»)
- "Every unprotected Odd re-entry is charged to a carry of the option's valuation U(e)". Kill: d_runquad_K2_m30 (dual of mkr.py 2 30,
  regenerated in experiments/si/odd/inst/): 61 of 90 re-entries have only MATCHED P-changes of U(e) in their window (no carry, no λ^U(e)
  change). Obstruction: SW-RETURN charges a re-entry to any rise of U(e); matched rises suffice.
- CONJECTURE ENT-NM (ENT_R(o, e) ≤ 1 + NM^U_R(e) per λ^U-run). Kill: d_runquad_K3_m30 (sha1 5c77dea9), run [0, 99], o 42, e 43: 3 entries, NM^U(e) = 1.
- CONJECTURE ENT-PCH (ENT_R(o, e) ≤ 1 + PCH^U_R(e)). Kill: red/fbr/instances/lev74_n40.pg (sha1 6f13c0b0; S3), run [0, 18], o 6, e 0: 2 entries,
  PCH^U(e) = 0 (a length-only re-entry; Lemma LEN-REENTRY describes it). Also nep87_n40, nep92_n40.

## box 34 (L-SI successor 29, docs/si/N5-CARX-box34.md §3; experiments/si/odd/carx.py, check.sh «box 34»)
- CARRY-CLIMB (between matched P-changes of U(x) the carries' entering top ranks strictly increase). Kill: experiments/si/odd/inst/
  d_hntop_n2 (dual of hnh1.py 2 topfix), vertex 4, λ^U-run from 0, t = 7: top 38 then 35.
- SWEEP-GAIN (R85's Φ just after successive matched P-changes strictly increases in a λ-run). Kills: red/n5inj/instances/wide_h16.pg
  (sha1 990ecbcf; Odd side, S3), vertex 2, run from 13, t = 23, Φ 18 then 18; new/box59/out/fc_3.pg (9af7ca12; Even side, S3), vertex 6,
  t = 23, Φ 155 then 88. Obstruction: a reset can land at lower Φ after a carry burst; R85's Φ is not a net-progress potential.
