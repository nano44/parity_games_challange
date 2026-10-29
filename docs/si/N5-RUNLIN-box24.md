# N5-RUNLIN (box 24): CONJECTURE RUN-LIN is DEAD (a fallback-free run of 2n + 13 transitions for every n ≥ 73, 99 > 98 at n = 49; three engines, Oink-checked); wave anatomy; τ optimal along the long runs
L-SI successor 20 (Opus 5.5; D18, Lead reading L40). Lead's brief 2026-10-28 23:21Z, STEP 1: «CONJECTURE RUN-LIN, a fallback-free run has ≤ 2n
transitions ... Aim for a proof or a kill with an instance». Working note, unrefereed, not frozen. Not a TARGET.md claim. Nothing here bounds
N5's running time; G-N5-TIME stays OPEN. Labels (D18 / L40): PROVED (lane) / CONJECTURE / OPEN / DATA / READING / DEAD.
Counts are TRANSITIONS (REFEREE CORE-N1). A "run" is a maximal fallback-free stretch of one phase ((λ_Ξ, τ) constant, RESULTS R38 (a)).
Tools: experiments/si/runlin/ (trace.py, swcount.py, anatomy.py, keeper.py, allruns.py, growclimb.py, stretch.py). Outputs and logs:
experiments/si/runlin/out/.

## Summary
| § | item | label |
| --- | --- | --- |
| §7 | DEAD RUN-LIN and RUN-LIN-OPT: family runfam_K (n = 39 + K, one Odd choice vertex, one phase, 0 fallbacks, I_τ = ∅ throughout): run = 74 + ⌊5K/2⌋ for K ≤ 34, then + 2 per vertex; run > 2n for every K ≥ 10 (99 at n = 49), run = 2n + 13 for K ≥ 34 | DEAD (instance; three engines agree; N5's output Oink-verified) |
| §1 | the long runs are WAVES: one Even switch per transition along a path, restarted by each σ̄ change; run49's corridor is walked in both directions | DATA |
| §2 | climbs (vertex cloning + box43 mutations): 49 → 53 → 56 (n 32) → 58 (n 33) → 60 → 62 (n 34, 1.82n); L-COMP's n5b agrees on every pinned record; the 62 record is the seed of §7 | DATA |
| §3 | in 41 of 44 runs of length ≥ 0.75n (alt_all), I_τ = ∅ at EVERY state: τ is already an optimal Odd strategy; CONJECTURE RUN-LIN-OPT (now DEAD, §7) | DATA |
| §4 | a ping-pong kill design (K hidden bases at the two ends of a corridor of length L, run ≈ K·L) and why it fails at its top level: every hidden base needs an odd blocker above its reward, and the gate that carries the blocker needs (to keep τ fixed) an escape for Even above the blocker that is Ξ-closed | READING (a design obstruction, not a theorem) |
| §5 | what a proof would have to use; next steps | OPEN |

## 0. Setting and the statement
- N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md). In a phase τ is fixed, so S4a's σ_{t+1} is Even's W-optimum in G_τ restricted to the arena
  A_t(v) = {σ_t(v)} ∪ {w : (v, w) ∈ Iσ_t}; Iσ is computed from Ξ (honest valuation, against Odd's best response σ̄). W_t := the valuation of
  the (σ_t, τ)-play. D_t := {Odd u : σ̄_t(u) ≠ τ(u)}.
- CONJECTURE RUN-LIN (N5-ALT-box23 §13; DEAD, §7): every fallback-free run of a phase has ≤ 2n transitions. With the elementary split
  |P| ≤ f + (f + 1)·max |run| (N5-ALT §13, PROVED) and FB-LIN (L-NEW's), it would give |P| ≤ n + (n + 1)·2n.
- Premises used below for orientation only (nothing new is claimed from them): P-N5-CORE (C1) EVERY-SWITCH (every in-phase transition
  changes σ), (C3) RISE-SW, (C5) FRESH-RED (|run| ≤ m_E + NOFRESH); REFEREE signed (C1)-(C6) with no gap (docs/referee/R-N5-CORE.md at
  referee 9d831869); REFEREE-2 pending.

## 1. DATA: the anatomy of a long run (anatomy.py, trace.py)
| instance | n | m_E | run | single-switch transitions | total switches | switches per vertex (count: vertices) | FRESH / NOFRESH | σ̄-changing G | σ̄-constant pieces |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| run49_n32 (L-RED R89) | 32 | 78 | [2, 51] 49 = 1.53n | 42 | 66 | 1: 3, 2: 13, 3: 11, 4: 1 | 30 / 19 | 3 | 6, 22, 12, 9 |
| best53_n32 (§2) | 32 | 136 | [2, 55] 53 = 1.66n | 41 | 81 | 1: 3, 2: 5, 3: 12, 4: 8 | 35 / 18 | 3 | 6, 20, 11, 16 |
| best56_n32 (§2) | 32 | 122 | [1, 57] 56 = 1.75n | 42 | 97 | 1: 5, 3: 11, 4: 8, 5: 4, 7: 1 | 26 / 30 | 6 | 1, 6, 12, 6, 3, 11, 17 |
| best58_n33 (§2) | 33 | 131 | [1, 59] 58 = 1.76n | 42 | 99 | 1: 3, 2: 4, 3: 9, 4: 10, 5: 3, 6: 1 | 27 / 31 | 7 | 1, 1, 6, 12, 5, 4, 11, 18 |
| best60_n34 (§2) | 34 | 129 | [1, 61] 60 = 1.76n | 44 | 104 | 1: 4, 2: 2, 3: 9, 4: 12, 5: 3, 6: 1 | 29 / 31 | 4 | 1, 7, 22, 13, 17 |
| run34_n40 (R89) | 40 | 93 | [15, 49] 34 = 0.85n | 26 | 67 | 1: 7, 2: 9, 3: 10, 4: 3 | 18 / 16 | 17 | all ≤ 5 |
- WAVES. In run49 most transitions switch ONE Even vertex, and that vertex switches to the vertex that switched one step earlier
  (trace.py; e.g. t = 8 … 19: 27 → 14, 3 → 27, 28 → 3, 23 → 28, 16 → 23, 11 → 16, 4 → 11, 0 → 4, 1 → 0, 8, 22 → 1, 26 → 22, 29 → 26).
  The mechanism: (v, w) enters Iσ only after Ξ(w) has risen, i.e. after w switched; so a W-improvement travels one edge per iteration.
- A σ̄ change starts a new wave. run49 has one Odd choice vertex o = 5 (out-degree 3, τ(o) = 7); σ̄(o) = 14, 29, 14, 7 on the four pieces.
  Waves 2 and 3 walk the same corridor between o's options 29 and 14 in OPPOSITE directions (wave 2 builds 29 → 26 → 22 → 1 → 0 → 4 → 11 → 16
  → 23 → 28 → 3 → 27 → 14, wave 3 builds 14 → 3 → 27 → 28 → 23 → 16 → 4 → 11 → 22 → 1 → 0 → 26 → 29). Each wave ends at o's other option and
  raises its Ξ above the option Odd holds, so σ̄(o) flips, and the flip starts the next wave (RISE-GATE in action).
- So run ≈ Σ_pieces (wave length), with pieces ≤ n − 1 where STATIC-DEPTH applies (N5-GCILEN-box22 §2; its hypotheses (H1)-(H4), GEN_W are
  not checked here). A kill needs ≥ 3 pieces of length close to n, or many σ̄ changes with long pieces.
- Stretching run49's corridor does not lengthen the run: subdividing any two-way Even pair (u ↔ w) by a new Even vertex x (stretch.py and the
  inline loop in this box's log; 8 pairs × 24 priorities × 2 starts) gives at most +2 (51 at n = 33). So the corridor is not a clean
  parametrised gadget.

## 2. DATA: climbs (growclimb.py)
- Objective: the longest fallback-free run R; score R − C·n. Mutations: experiments/new/box43/climb.mutate (Odd choice set fixed) plus CLONE
  (copy an Even vertex with its successors, link it to the original and to one predecessor). Logs out/g2*.log, out/h3*.log, out/k4*.log.
- From run49_n32: C = 1.25 → 50 (n 32); C = 1.0 → 53 (n 32, best53_n32). From best53: C = 1.0 → 55, C = 0.5 → 56 (best56_n32), C = 1.5 →
  54. From best56 with C = 0, NMAX 34: 58 at n 33 (best58_n33), 60 and 62 at n 34 (best60_n34, best62_n34). From run34_n40 and x32_rand64 (seed run 55 at
  n = 64): no ratio above 0.92. C = 0 with NMAX 48 grows n fast and the ratio falls (60 at n = 48): added vertices add ≤ 1 step each.
- At C ≥ 0.5 no accepted step grew n; at C = 0 growth is accepted but adds about one transition per vertex. So the climbs say nothing
  about the ratio's growth with n.
- greedy shrink (shrink.py: delete an Even edge if the run does not drop, a vertex if run − 2n rises) removes nothing from best56_n32.
- Independent engine: L-COMP's experiments/n5-second/n5b.py in SPEC mode (via experiments/si/root/n5bcmp.py, imported, not edited) gives the
  identical state sequence on best53_n32 (56 states, 55 iterations, 0 fallbacks), best56_n32 (58 / 57 / 0), best58_n33 (60 / 59 / 0) and
  best60_n34 (62 / 61 / 0). On all four I_τ = ∅ at every state of the longest run (keeper.py; §3), and they have ONE Odd choice vertex (𝒞^1O,
  like run49), so RESULTS R51 already makes N5 polynomial on them; they matter only as data on the constant of RUN-LIN.
- Instances: experiments/si/runlin/instances/ (sha1 in §6).
- READING (written before §7). The climbs alone stayed below 2n (best 1.82n at n = 34); L-RED R89's fixed-n climbs gave 0.88 (n 16),
  1.13 (24), 1.53 (32), a ratio rising with n. §7 crosses 2n by stretching the 62 record's corridor, not by climbing.

## 3. DATA: long runs happen against an OPTIMAL τ (allruns.py, keeper.py)
- allruns.py on root/logs/alt_all.lst (413 games, n ≤ 600; given start where valid; out/allruns_alt.txt): 1,188 fallback-free runs; 44 have
  length ≥ 0.75n; in 41 of them I_τ = ∅ at EVERY state of the run (TAUOPT), so τ is an optimal Odd strategy throughout. The 3 exceptions are
  run34_n40 (34 = 0.85n), so_sor5_n24 (22 = 0.92n) and xrun8_n10 (8 = 0.8n). The longest run overall is gate_K64_n581 (71, n 581).
- keeper.py: I_τ = ∅ at all 50 / 54 states of the runs of run49_n32 / best53_n32 (D ≠ ∅ at 40 / 37 of them), and at the 18 states of
  l121reader_n41's longest run.
- Consequence (READING). With I_τ = ∅, W* (Even's global optimum against τ) is the game's value. The long runs are Even solving the ONE-player
  game G_τ by S4a, gated by Ξ; D-gates are Odd vertices whose σ̄ branch is under-valued by the current σ. The hard case of RUN-LIN is:
  - CONJECTURE RUN-LIN-OPT: if I_τ = ∅ at every state of a fallback-free run, the run has ≤ 2n transitions.
  - It implies nothing about phases where τ is not optimal; those are cut by τ changes anyway, and the data put the long runs here.

## 4. READING: a ping-pong kill design, and the obstruction at its top level
The anatomy (§1) suggests a family with run ≈ K·L at n ≈ L + O(K): a corridor c_1 … c_L of Even vertices with edges to both neighbours,
and K bases x_1 … x_K attached alternately at c_1 and c_L, each revealed (made Ξ-improving) exactly when the previous wave reaches the
far end. I worked the design out on paper; this section records what each part needs and where it fails. Nothing here is run or proved.
- Cycle node and fillers. One sink cycle node c with high rank (as in L-RED's mkgrow, R82 §1), so corridor vertices and other fillers are in no
  path set and only lengths count; with Ω(c) even, shorter is better, so (c_{i+1}, c_i) is not improving until c_i's value has risen: one
  wave step per iteration (as in §1).
- Bases. x_j has even priority C_j above c, increasing in j, so the corridor wants the newest base.
- Revealing x_{j+1} when wave j completes needs the completion to reach x_{j+1}'s value. Three ways were checked:
  - (i) through PATH VALUES (x_{j+1}'s route passes the corridor end): the corridor later turns towards x_{j+1} and closes a cycle through
    its own route; for the switch into x_{j+1} to be Ξ-improving the closed cycle must be even-topped, which forces the hidden route's top
    to be even as well, so x_{j+1} is not hidden. FAILS.
  - (ii) through an Odd gate z_{j+1} on x_{j+1}'s route that leaves a corridor-dependent option y1 once Ξ(y1) rises (RISE-GATE): Odd must
    prefer y1 while hidden and leave it after, so y1's rise must carry an even vertex above the blocker that hides x_{j+1}, while W wants
    x_{j+1} above the corridor's current value; with x_{j+1}'s blocker ranked above C_{j+1} this forces an even above C_{j+1} into the
    corridor's value before x_{j+1} exists. FAILS in the absolute form; works only with an extra tap vertex (next item).
  - (iii) through a TAP: an Even vertex t_{j+1} on y1's route with options r_{j+1} (an Odd gate whose σ̄ branch carries a high odd Q, so
    x_{j+1} is Ξ-blocked, and whose τ branch has W-value between those of the corridor before and after wave j) and c_L. W moves t_{j+1} to
    c_L exactly when wave j completes; then σ̄(z_{j+1}) flips to the safe option y2 and x_{j+1} is revealed. Ranks: C_{j−1} < E_{j+1} < C_j
    (r's τ branch), Q above every C. On paper the constraints of this level are consistent; it was not built or run.
- The obstruction (the top level). Every gate that carries a blocker must stay in D for the whole time its base is hidden, with τ unchanged.
  In the TAUOPT regime of §3 that needs, for the gate g, val(σ̄ g) ⊵ val(τ g) while Ξ(σ̄ g) ◁ Ξ(τ g): Even must have an escape on the σ̄ branch
  of value above the blocker that the current σ cannot take (Ξ-closed). Chained level by level, the escape of level j's blocker can be
  level j + 1's revealed base, which is Ξ-closed for exactly as long as needed. At the TOP level there is no higher base. The escape must then
  carry an even vertex above the top blocker, and being Ξ-closed needs either an odd vertex above THAT (a higher level) or a TIME delay: a
  delay line of Even vertices fixed one per iteration, as long as the time the top base must stay hidden, ≈ (K − 1)·L. That costs
  n ≥ (K − 1)·L, and the ratio run / n drops below 1.
  - This matches the constructed families: mkgrow and mkpp (L-RED R82 §1, R83 §1) keep their top gate GH in D with a delay chain of length
    LG = K + 6, and both have run < n (mkpp K = 48: 55 iterations at n = 449).
  - It does not match the climbed instances: run49 / best56 have no long delay line and reach 1.53n-1.75n with one Odd choice vertex and
    3-6 σ̄ changes. There the top gate's "escape" is the corridor itself (o's two options are its two ends), and its D-membership is
    re-created at every wave, which is a different mechanism from the static hierarchy above. It scales by stretching the corridor: §7.
- So the obstruction is to this DESIGN (static hiding levels), not to RUN-LIN. It said where a kill must come from, a gate kept in D by
  waves that recur, not by a hierarchy of blockers, and §7's kill is of that kind.

## 7. DEAD: RUN-LIN (and RUN-LIN-OPT) (written 2026-10-29 00:1xZ by date -u)
- Statement killed: «every fallback-free run of a phase has ≤ 2n transitions» (CONJECTURE RUN-LIN, N5-ALT-box23 §13). Also my §3
  CONJECTURE RUN-LIN-OPT (the same with I_τ = ∅ at every state), since the family below has I_τ = ∅ at every state of its run.
- How it was found: climbs (§2) to best62_n34 (62 at n = 34, sha1 below); its trace shows ONE corridor walked THREE times (t = 10-22, 32-43,
  50-62). Greedy subdivision of two-way Even pairs (stretchiter.py, 5 rounds) gave runfam_base_n39 (74 at n = 39); then repeated
  subdivision next to vertex 25 (mkrunfam.py) adds 2 and 3 transitions alternately.
- Family (experiments/si/runlin/mkrunfam.py K OUT; deterministic): base runfam_base_n39; step k: a new Even vertex x of priority 0
  subdivides the two-way pair (25, last) (25: last → x, last: 25 → x, x: {25, last}; start σ0(x) = 25; a held edge 25 → last or last → 25 is
  redirected to x); last := x. n = 39 + K. One Odd choice vertex (5: 2, 7, 9, 14, 18, 28; τ0(5) = 7), so the family lies in 𝒞^1O.
  | K | n | longest fallback-free run | run − 2n | engines |
  | --- | --- | --- | --- | --- |
  | 0 | 39 | 74 | −4 | n5x |
  | 9 | 48 | 96 | 0 | n5x |
  | 10 | 49 | **99** | **+1** | n5x = n5b (identical 101 states) = n5.py (100 iterations, 0 fallbacks); check_sol2: zlk OK, strategies verified |
  | 20 | 59 | 124 | +6 | n5x |
  | 34 | 73 | 159 | +13 | n5x |
  | 40 | 79 | 171 | +13 | n5x = n5b (173 states) = n5.py (172 iterations, 0 fallbacks); check_sol2: zlk OK, strategies verified |
  | 60 / 100 | 99 / 139 | 211 / 291 | +13 / +13 | n5x |
  - K ≤ 34: run = 74 + ⌊5K/2⌋ (every K checked, logs out/chain25_long.log, out/runfam_table.txt). K ≥ 34: + 2 per vertex.
  - Each instance's whole run is ONE phase ([1, 100] at K = 10) with no fallback anywhere, λ_W constant, and I_τ = ∅ at every state
    (keeper.py), with D ≠ ∅ at 65 of the 100 states (K = 10).
- Anatomy (anatomy.py, K = 10 / 40): σ̄-changing transitions G = 9 at both K; σ̄-constant pieces 1, 1, 2, 5, 21, 6, 3, 26, 1, 33 (K = 10) and
  1, 1, 2, 5, 33, 6, 3, 56, 1, 63 (K = 40). Two pieces grow by one per added vertex (the new segment is walked by two waves); the third
  long piece grows only up to K ≈ 22-34, then stops. Every piece stays ≤ n − 1 (consistent with STATIC-DEPTH).
- Obstruction (READING from the trace): run = Σ over σ̄-constant pieces, and a piece is a wave along a corridor of length up to n − 1. A
  one-vertex Odd gate whose options are corridor ends restarts the wave at every σ̄ change (§1). Two such waves over the same long segment
  already give ≈ 2n, and a third partial one gives the excess. A bound of the form c·n needs a bound on the number of LONG pieces per run,
  not on the per-piece length.
- REFEREE's independent reproduction (docs/referee/R-N5-RUNLIN-kill.md, referee c609f779, own engine; relayed by the Lead 00:36Z): runfam_K10
  99 > 98, runfam_K40 171 = 2n + 13, Oink zlk and tl agree; the obstruction above judged FAIR, with two precisions (adopted):
  - (a) gate 5 has 6 options; only 28 is a corridor end. The other end, 25, is one Even step from options 2 and 9.
  - (b) waves also run along other Even chains (e.g. t = 10-21: 26 → 3 → 36 → … → 21); the corridor 28-34-37 … 48-25 is walked FOUR times, in
    alternating directions.
- What survives: every count here is linear in n (run ≤ 2.17n on the family; the family's run − 2n is constant from K = 34 on). So the kill
  is of the constant 2, not of linearity. CONJECTURE RUN-LIN′ (weaker, open): every fallback-free run has O(n) transitions. No constant is
  proposed; whether a third and fourth long wave can be made to grow with n is the open design question (step 2 below).
- Third wave (DATA, written 00:3xZ): from runfam_K40, subdividing next to vertex 28 instead (chain25.py with U = 28, log out/chain28.log)
  again alternates +3 / +2 for 30 steps: 251 at n = 110 (run − 2n = +31, 2.28n), still rising at the stop. So stretching both corridor
  ends in turn keeps a slope of about 2.5 per vertex over the sizes tried; whether it stays above 2 indefinitely is not shown.
  Continued 60 more steps (out/chain28b.log): 276 (n 120), 302 (130), 327 (140), 352 (150), 377 (160), 403 at n = 170 (2n + 63, 2.37n), still
  exactly +2.5 per vertex, no saturation in 90 steps. So the family at vertex 28 has run ≈ 2.5n − c: a third long wave that grows with n.
  The ratio tends to 2.5, a constant: RUN-LIN′ (linear) is untouched. A super-linear run needs the number of long waves to grow with n.
- Pins: experiments/si/runlin/instances/runfam_base_n39 (.pg 6b6fc369…, .start 24b9c519…), runfam_K10 (.pg faf218f1…, .start 56e4dec6…),
  runfam_K40 (.pg 287a185d…, .start bcbfeed3…); full sha1 in §6.

## 5. OPEN and next steps
1. RUN-LIN and RUN-LIN-OPT are DEAD (§7). OPEN: RUN-LIN′ (O(n) per run). No proof route is in hand. The available pieces bound a run by Σ over σ̄-constant pieces
   (STATIC-DEPTH, conditional) or by (n − 1)(1 + |U(S)|) per vertex (N5-RUND-box17 §16 CHARGE-U); both are products, not sums.
2. Make a third (and fourth) long wave grow with n on runfam (stretchiter.py from runfam_K40 is the first try), i.e. pieces ≈ n with
   G growing; that would decide whether RUN-LIN′ holds with any constant.
3. Fixed-n climbs at n = 40, 48 from the best56 structure (embedding plus padding), to see whether the ratio keeps rising with n.

## 6. Pins (experiments/si/runlin/instances/; sha1sum)
| file | .pg sha1 | .start sha1 | n | longest run |
| --- | --- | --- | --- | --- |
| best53_n32 | 80ebed0f00c70c97503875db1733bc29e07d7201 | 4cb465b7fc25a76b351bb9ec3daed50787a7b7ac | 32 | 53 |
| best56_n32 | b41706316c1e1604681e0573380cd1ad1ee19b34 | e31c4c6fe45b06efa2da3cb0f8e7b7c6d598dce7 | 32 | 56 |
| best58_n33 | 147f8c704bb8861c4f09ca61ab8439b91688a4ea | 53dbe1176366ad2bb394435103562ea479bca114 | 33 | 58 |
| best60_n34 | 3e497faff26e122c60c39548ea9d3205db8d46ea | b78fd0441ca827aa34aec8c01474c0c0a95a9e04 | 34 | 60 |
| best62_n34 | 85f1a82810504267771a50848e1b886edb1165c9 | 5ee8494284f50718f3b13567b18bbf1d8fa3b9d9 | 34 | 62 |
| runfam_base_n39 | 6b6fc36985bbb40a1b2a5ac8cb35e80e72cc5c27 | 24b9c5199c3bc958d19bdc0b333893415d288532 | 39 | 74 |
| runfam_K10 (KILL) | faf218f125d1516d4677393991d53a08a9f4f3bb | 56e4dec67323e6f5b832ac2d95ef832d6ce3a013 | 49 | 99 |
| runfam_K40 | 287a185d6b82f3ed196abb65726152c982c71f60 | bcbfeed3a59b13acd442d1032e05655eafd30ec1 | 79 | 171 |
best53-best62: only the run counts are claimed (two engines); N5's output not checked. runfam_K10 / K40: three engines and check_sol2 (above).

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/si/runlin/ tools (mkrunfam.py generates the family), instances, out/ logs; check.sh block "box 24"; DEAD.md box 24.
- FINDINGS: RUN-LIN DEAD: runfam_K10 (n 49) has a fallback-free run of 99 > 98 transitions; the family has run = 2n + 13 for n ≥ 73 (three
  engines, Oink-checked output, I_τ = ∅ throughout, one Odd choice vertex). RUN-LIN-OPT DEAD with it. Linearity is not touched (run ≤ 2.17n
  on the family). Long runs are waves restarted by σ̄ changes; 41 of 44 long library runs have τ optimal throughout. A static-hiding
  ping-pong design fails at its top level (READING, §4); the kill uses recurring waves instead.
- NEEDS: none from the owner.
