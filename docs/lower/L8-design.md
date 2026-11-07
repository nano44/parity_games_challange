# L8: helper schedules decided exactly, ONE-READ XOR, and the RC-PLATEAU test re-read (L-LOWER successor 8, BOX L8)

Box: Lead brief (L-LOWER successor 8; D1 / D14 / D18), GO 2026-11-07 21:13Z. Items: (0) dissect L-COMP 11's KILL230 / KILL238;
(1) the sequential schedule WITH helper pairs, decided exactly; (2) the helper rule; (3) ONE-READ XOR; (4) candidate family G_h or
the obstruction. Written from 21:15Z (date -u).
Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA / DEAD / READING. Every DATA clause names its counter (unit, set, scope).
Nothing here is a result in the sense of CLAUDE.md; G-N5-TIME stays OPEN. Not a TARGET.md claim (§9).

## 0. Model, notation, tools
- Model and notation as docs/lower/L7-design.md §0 (R104's IDEAL rules; simulators l6/sim6.py and l5/fev.c). Sequential target of an
  h-capped tower: l7/sched.py (f_l = 2l + 1 moves α_l steps after each change of c_l, the higher levels run, q_l = 2l moves one step after
  the last of them; α_0 unused). Helper pair = a pair of a level ≥ h (above the top capped level).
- Tools (experiments/lower/l8/): hsched.py (helper trajectories enumerated up front, then a wiring search), hsched2.py (helper
  trajectories chosen inside the wiring search, step by step), l8check.py (run by check.sh). Frozen genomes: l8/rec/ (sha1 in §2).
- Search method (both tools; exact for their scope). Lower pairs 0..h−1 follow the target. Each helper mover follows any trajectory the
  movement rule allows (free at step t iff it is not on c_l(t), computed from the NEW lower states; a free mover moves to c_l or stays),
  any start bit; gates of helper levels below the top: all 4 patterns. Wirings: every acyclic xt without self-targets, built
  sink-first (a placed mover's options point to placed movers or the exit), the joint ranksolve condition set checked after every
  placement and (hsched2) after every helper step; adding conditions never restores feasibility, so pruning loses nothing;
  infeasible partial wirings are memoized. Ranks and signs free (GREEDY-COMPLETE, L7 §3). A «realized» answer is re-simulated by
  sim6 (and fev) from the solved genome. hsched2 restriction for d ≥ h + 2: a helper of level l > h is placed only after both movers
  of level l − 1 (its key needs their states), so a level-(l − 1) helper cannot read it. For d = h + 1 there is no restriction.

## 1. RC-PLATEAU: what the KILL genomes can and cannot test (READING; item 0 preliminary)
- L6 §5d states RC-PLATEAU (role form) as an implication: «with levels 0, …, 5 capped, if there is a Ξ-path (any options) from q₅ to a
  member of pair 6, then F(6) ≤ 222». A genome that passes guard_l6 'noreturn' has NO such path (npaths = 0): it lies outside the
  hypothesis and is consistent with the implication whatever its F(6).
- L6 §5d's last sentence («a climb that forbids the RETURN-CHAIN … a genome with F(6) > 222 kills the conjecture, and a plateau at ≤ 222
  supports it») has the direction reversed relative to that statement, and L7 §1 («RC-PLATEAU SURVIVES … every RC-free genome ≤ 190»)
  repeated the reversal. Correction (this lane's own files): an RC-free genome with F(6) > 222 SUPPORTS the explanatory reading «the
  RETURN-CHAIN is what costs the 32 flips» and refutes «levels 0-5 capped ⇒ F(6) ≤ 222» (no hypothesis on the wiring); an RC-free genome
  at ≤ 222 (L6G_TEST1, L7 §1b) is evidence AGAINST that explanatory reading, not for RC-PLATEAU. A kill of RC-PLATEAU as stated needs
  F(6) > 222 together with a Ξ-path q₅ → pair 6.
- guard_l6 'noreturn' (bca48384, unchanged since) read against L6 §5d: it encodes the hypothesis's negation correctly (q₅ = the second
  mover of the first 5-window with two moves at distinct steps; npaths over both options of every mover; levels 0-5 capped). Gap:
  roles() does not check DOUBLE-EQ (E5) (the same member second in every window); checked explicitly on the KILL files in item 0.
- Status: the KILL230 / KILL238 files (L-COMP 11; sha1 29faf25f…, 54450906… as relayed) were not on origin/claude/l-comp at 21:13Z;
  item 0 is pending them.
- Lead reading (Lead 21:19Z, quoted): «CONJECTURE RC-PLATEAU (j = 6 role form) stays a CONJECTURE: untested by D_l6z, and KILL230/238
  are consistent with it.» «Its contrapositive is the useful form: a 6-capped genome with F(6) > 222 has npaths(q₅, pair 6) = 0. So a
  seventh capped level must be found inside the RC-free set, which is exactly the space L-COMP's gated climb searches.» «What is
  refuted (DATA, pending your re-run on the files): «RC-free genomes with levels 0-5 capped have F(6) ≤ 222». That was the L7 §1
  «RC-free ≤ 190» reading and §1b's stall reading, not a conjecture.» The Lead withdrew its 20:5xZ «DEAD by the stated test» label.
  Forward note: L6 §5d's «test proposed» sentence and L7 §1's «SURVIVES» line are superseded by this section (history not edited).

## 1c. Item 0: KILL238 and KILL230 dissected (DATA; unit as stated per line; scope = stored start)
- Sources: claude/l-comp efdd6010, experiments/comp/box30/out/L6Z_KILL230_d28.txt and L6Z_KILL238_d28.txt; frozen copies
  l8/rec/LCOMP_L6Z_KILL230_d28.txt (sha1 29faf25f347a05e55d7dfb9600fe0241f6226d8c) and l8/rec/LCOMP_L6Z_KILL238_d28.txt
  (sha1 544509062f68eb96b60becfab51924dd5d333913), = the relayed values. sim6 and fev agree: KILL230 T 275, F 2 6 14 30 62 126 230 166 …;
  KILL238 T 283, F 2 6 14 30 62 126 238 174 …; guard_l6 'noreturn' ok on both (caps 6, q₅ = 10, npaths(q₅, pair 6) = 0).
- E5 check (kill_dissect.py → out/kill_dissect.out; unit = 5-window; set = all 63 of each of SL41, L6G_TEST1, KILL230, KILL238): every
  window has two pair-5 moves at distinct steps and mover 10 is second in 63 of 63 in all four. So q₅ = 10 is well defined and the
  guard's role reading (first window only) is exact on these files. Hence (Lead 21:19Z reading) the refutation of «RC-free genomes with
  levels 0-5 capped have F(6) ≤ 222» is confirmed on my re-run: KILL238 is RC-free with F(6) = 238 (DATA, two simulators).
- 6-window profile (l6/struct48.py; unit = 6-window; set = the 127 of each): SL41 79 / 16 / 16 / 16 (both / only 12 / only 13 / none);
  L6G_TEST1 the same; KILL230 99 / 4 / 20 / 4; KILL238 111 / 0 / 16 / 0. Pair 6 is NOT crossed in KILL230/238: 12 → (13, 11),
  13 → (11, 19) (12:0 reads 13 directly).
- SL41's MERGE (11:1 → 9:1 (rank 87) → 54:0 → 22): the prefix 11:1 → 9:1 (87, −) is still there in both KILL files (chain 11:1 at s₀:
  79 → 87 → 54:1 → …), but pair 6 no longer reads 22, and (9, 1) is the decider of 12 or 13 at a pre-state of 0 of 127 6-windows in
  KILL238 (dom87.py; 12 of 28 failing in KILL230). In KILL238 every 6-window under a (9, 1) 5-window is good: SL41's 32 merge-decided
  failures are all repaired.
- Diff vs SL41 (kill_dissect.py; unit = option / mover): KILL238 xt 71 options (movers 0-11: only 10:0, 55 → 17; pair 6: 2; ≥ 14: 68),
  br 87 (pair 6: 4, ≥ 14: 83), bp 47, gates 16 movers ≥ 14, starts 12 movers ≥ 14. KILL230 alike (xt 73, br 87, bp 38). The re-point
  creates the unique Ξ-path q₅ = 10 :0 → 17 :0 → 22 (level 11): the RC-free q₅ trigger of L7 §2 GUARD.
- What the re-point repairs (w80.py, runstats.py; unit = 5-window; set = KILL238's 63): mover 22 moves at u₂ − 1 in 15 windows (8 of
  the 16 opened by (8, 0), 7 of the 8 by (8, 1)); the other PULSE_5 ≥ 2 windows have triggers of levels 7 and 15. Lowest trigger level:
  7 in 31 windows, 11 in 8, 15 in 16. SL41 used mover 12 (level 6, the RETURN-CHAIN) as the trigger of all 16 (8, 0) windows.
- What still blocks 254 (fail16.py, w80.py; unit = 6-window / 5-window; set = KILL238's): the 16 failing 6-windows are 8 consecutive
  pairs, one pair in each of the 8 (8, 0) 5-windows with o(8) = o(9) = 0 (the other 8 (8, 0) windows have o(8) o(9) = 1 1 and are
  triggered by 22). In those 8 windows no mover of closure(10) of level ≥ 7 moves at u₁ (only 11 and 21 move), so PULSE_5 = 1
  (inner windows: 8, = the 8 length-1 6-windows; WINDOW-CAP bound 2·127 − 8 = 246). Each such window costs 2 flips: the length-1
  6-window [u₁, u₁] (13 moves, 12 cannot: WINDOW-CAP) and the next one [u₁ + 1, u₁ + 2] (13 moves at its last step, 12 is decided by
  (13, 1) rank 89, i.e. 12 copies 13 and has no step left). 8 × 2 = 16 = 254 − 238. KILL230 has the same 8 pairs (16 windows) plus 12 more:
  8 under (8, 0) 5-windows with PULSE_5 = 2 (4 only 13, 4 none) and 4 under (9, 0) (only 12); (9, 1) is a decider at some pre-state in
  12 of its 28 failing windows (dom87.py), though no failing window lies under a (9, 1) 5-window.
- Revert each changed part (l5/revert.py with fev → out/revert_SL41_KILL238.out, out/revert_SL41_KILL230.out; unit = one changed
  option target / sign / rank swap / gate order / start bit of the new genome reset to SL41's; set = all of them): KILL238 245 units:
  122 FORCED (84 lose a lower cap, 34 make the graph cyclic, 4 keep caps 6 with lower F(6)), 110 neutral (drift), 0 raise F(6).
  KILL230 237 units: 127 forced (90 / 31 / 6), 95 neutral. Reverting 10:0 alone: caps 0, T 9 in both (it is load-bearing). Level
  blocks 0-4 neutral; levels 5, 6 and every changed helper level ≥ 11 forced: the lower caps rest on the re-built helpers above pair 6,
  as COUPLING-UP (L7 §4) predicts.
- Constraint for L-COMP 11's climbs toward 254 (READING, from the above): keep 10:0 → 17:0 → 22 and the 22-trigger; the target is
  the 8 (8, 0) 5-windows with o(8) = o(9) = 0, which need a level-≥7 mover of closure(10) moving at u₁ (one step after 11) — e.g. a
  second q₅-reachable helper armed in the o(8) o(9) = 0 0 phase, the mirror of 22. A cheap guard/score term: the number of
  6-windows of length 1 (= inner PULSE_5 = 1 5-windows here) must fall from 8 to 0; F(6) ≤ 254 − (that number) by WINDOW-CAP.

## 2. Item 1: the sequential schedule with helpers, decided exactly (DATA; unit = (h, d, α) case; scope = the sequential target)
| h | d | α (α_1, …) | helper levels | result | outputs |
| --- | --- | --- | --- | --- | --- |
| 2 | 2 | 1 / 0 | none | NONE (L7 §7, 5,941 wirings) | l7/exh2_h2.out |
| 2 | 3 | 1 | 2 | NONE (hsched: 5,041 helper trajectories × all wirings; hsched2 agrees) | l8check |
| 2 | 3 | 0 | 2 | REALIZED: HS2_d3 | l8check |
| 2 | 4 | 1 | 2, 3 | REALIZED: HS2a11_d4 | out/h2d4_a11.out |
| 3 | 4 | (0,0), (0,1), (1,0), (1,1) | 3 | NONE in all four | out/h3d4_a*.out |
| 3 | 5 | (0,0), (0,1), (1,0), (1,1) | 3, 4 | running | out/h3d5_a*.out |
- HS2_d3 (rec/HS2_d3.txt, sha1 8ddebddc55e255843bde61f4026a2f448e6b136d): d 3, T 6, F 2 6 2, levels 0-1 capped; sim6 and fev agree.
  xt (pairs 0-2): 0 → (2, ⊥), 1 → (5, ⊥), 2 → (3, 1), 3 → (1, 5), 4 → (⊥, ⊥), 5 → (⊥, ⊥). Helpers 4, 5 are sinks; 5 moves once (step 2,
  KEY-fired: its key o(1) changes at step 2 when q₁ = 2 moves), 4 never moves. Mover 1 (pair 0) reads 5, not q₁; f₁ = 3 reads 1 and 5.
  So the Ξ-cycle f₁ → pair 0 → q₁ → f₁ of L7 §7 is broken at the link «pair 0 learns that q₁ finished»: helper 5 carries it.
  The previous smallest 2-capped record in this lane was KILL_M2D_d6_mu13 (d 6).
- HS2a11_d4 (rec/HS2a11_d4.txt, sha1 68c8f2792bad28d7404b65d44d01ffbfd2307c8d): d 4, T 8, F 2 6 6 4, levels 0-1 capped; sim6 and fev
  agree. With α₁ = 1 (f₁ one step after its key) one helper pair is not enough, two are.
- Lemma SINK (PROVED, lane; acyclicity + ENC). Every acyclic wiring has a mover y with both options to the exit; pref_y is the sign
  of the higher-ranked of y's two options, the same constant p at every state. So at each free step y moves iff the move goes to p
  (level ≥ 1: iff c_y = p): y is a pure function of its key. In HS2_d3 both helpers are such sinks with p = 0; 4 starts on 0 and never
  moves, 5 starts on 1 and moves at the first step at which o(1) = 0 (step 2, the step o(1) changes): a «first time o(1) = 0» flag. This is why d = 2 dies at once in both searches (every mover of
  the sequential h = 2 target changes its label over its free steps), and why a cheap constant-preference helper is the first thing a
  search adds.
- READING: h = 2 needs one helper pair when f₁ is key-fired, two when it waits a step. h = 3 is not realizable with one helper pair in
  any α pattern: the least d for h = 3 in this scope is ≥ 5 (pending the d = 5 runs).

## 3. Item 3: ONE-READ XOR, proved (condition (i) of CONJECTURE CONTEXT-COUPLING, L7 §8)
- Lemma ONE-READ XOR (PROVED, lane; R105 ENC, acyclicity). Let x, a, b be distinct movers of an acyclic wiring with distinct ranks, and
  fix the states of all movers other than a, b. Then pref_x, as a function of (s_a, s_b) ∈ {0, 1}², is not XOR and not XNOR (where
  defined on all four points).
- Proof. For a state s and mover y let V_s(y) = Σ over the chain of y's current option of ±2^rank (sign by parity); then the value of x's
  option k is v_k = e(x, k) + V_s(xt(x, k)) (V(⊥) = 0), and by ENC pref_x = [v_1 > v_0] (the top element of the symmetric difference
  decides the sign of v_1 − v_0; distinct ranks). Acyclicity: a does not reach b or b does not reach a; XOR is symmetric, so name them
  such that b does not reach a. All states except s_a, s_b are fixed, so from any mover y the chain is a fixed prefix up to the first of
  {a, b} it meets, or the exit: V(y) = c_y + V(z_y), z_y ∈ {a, b, ⊥}, c_y, z_y independent of (s_a, s_b). Then V(b) = β(s_b) and
  V(a) = α(s_a) + [z(a, s_a) = b]·β(s_b), where z(a, k) is the first of {b, ⊥} on the chain of a's option k.
  Let D = v_1 − v_0 = c + V(z_1) − V(z_0) with z_0 = z_(xt(x,0)), z_1 = z_(xt(x,1)) (z = x's option target itself if it is a or b).
  (1) If D has the form A(s_a) + B(s_b), XOR and XNOR are impossible: XOR needs D(0,0) < 0, D(1,1) < 0, D(0,1) > 0, D(1,0) > 0, but
  D(0,0) + D(1,1) = D(0,1) + D(1,0) for additive D; XNOR likewise with signs reversed. This covers z_0 = z_1, every pair without a, and
  every pair with a in which [z(a, 0) = b] = [z(a, 1) = b].
  (2) Otherwise exactly one option of a, say k*, leads to b. If {z_0, z_1} = {a, ⊥}: D = ±(c′ + α(s_a) + [s_a = k*]β(s_b)), so at
  s_a = 1 − k* D does not depend on s_b, while XOR(1 − k*, s_b) does. If {z_0, z_1} = {a, b}: D = ±(c′ + α(s_a) + ([s_a = k*] − 1)β(s_b)),
  so at s_a = k* D does not depend on s_b. Contradiction in both cases. ∎
- Remarks. (i) The proof uses only that pref is the sign of a difference of two path sums: it holds for any real weights, so ranks are
  irrelevant (the lemma is about the WIRING). (ii) D18 connection: two-input preferences are exactly the sign functions of a «read-once
  additive branching program»; with two inputs these miss precisely XOR/XNOR, the Minsky-Papert perceptron obstruction (every one of
  the other 14 two-input Boolean functions is a linear threshold function). With three inputs the class contains a multiplexer
  (D = [s_a = 1]β(s_b) + [s_a = 0]γ(s_c)), so it is not the threshold class in general; the context input w of L7 §5 is exactly such a
  selector, which is why 864 of 180,000 context wirings realize the schedule's XOR there.
- Sanity DATA (l8check.py; unit = (random wiring, ranks, signs, reader, inputs, context); set = 40,000 samples, N = 3..7 movers, seed 8;
  scope = all four input combinations defined): 472 depend on both inputs, XOR/XNOR 0 times. Consistent with L7 §5's exhaustive
  0 of 84,000.
- Consequence for CONTEXT-COUPLING (READING): condition (i) holds unconditionally, so the split detector of a doubling pair needs a
  third varying input (a context mover) on its chain; whether that context must come from below (condition (ii)) is still open.

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class; all are about the IDEAL
model's step sequence (R104's definition) on 𝓛^R_d and its F-profile. Not M3, not a step-4 pass, not a TARGET.md claim.
