# Box 202 (D18): the Ξ-feedback-number class — k measured, k = 1 attempted (L-NEW successor 67, Opus; written 2026-11-09T02:43Z by date -u)
Lead 2026-11-09 02:32Z: «(a), the Ξ-FEEDBACK-NUMBER class — a parameterized extension of LANDED R122 … (1) define k exactly … MEASURE k on
the corpus … with T3, C, R … (2) attempt k = 1 FIRST … (3) then general k: target T3 ≤ (N + M)^O(k), or the exact obstruction with a frozen
instance. Premises: landed R-ids (R122 is landed) + P-N5-CHAIN facts (R125 pending) + P-N5-SPLIT; label each.»
Labels: PROVED (lane) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD / READING. Nothing here is a TARGET.md claim; G-N5-TIME OPEN.
Tools: experiments/new/box202/ (fvs202.py: k and T3 / C / R / F; gflip202.py: per-gate flips; k1srch202.py: random k = 1 search);
outputs fvs202.out, gflip202.out, k1s_202.log, k2s_203.log; instance k1fail_202.json; inst/ = the corpus copies + SHA1SUMS.

## 0. Answer
- (1) k(G) := the minimum size of a set F of movers whose removal makes the Ξ-graph acyclic. The Ξ-graph is RESULTS R104's: vertices =
  the N movers; an edge x → xt(x, j) for every option (x, j) whose Ξ-target is a mover; self-loops count. k = 0 is R122's class.
  Measured exactly (branch and bound per strongly connected component; «>12» where the search was capped) on 53 corpus genomes (§2).
- DATA: bounded k does NOT bound C or R by a constant. MW(n) has k = 2 for every n while C = R = 2n + 1. L-COMP's frontier family
  C2-C12 has k ≤ 2 while C = 2-12. FW(d, k′) has k = 1, C = k′ + 1 ≤ 5. On every k ≤ 2 instance T3 ≤ 0.25·(N + M) + 3: linear. So
  «T3 ≤ (N + M)^O(k)» is consistent with every measured run, and so is the stronger «T3 = O(N + M) for k ≤ 2». No run is long.
- CORRECTION to box 201 (l-new 47b325f6): its «CONJECTURE SEG-H» is the LANDED RESULTS R118 Theorem BR-SEG (every maximal run of p-steps,
  i.e. steps changing neither a cycle node nor σ̄, has at most N steps). With R118 Theorem T-CYC (T ≤ C + R + (C + R + 1)·N, where R118's
  C counts steps with a Λ-change and R118's R counts steps with a σ̄-change), box 201's «T3 ≤ (F + L + 1)(N + 2)» is R118 (l). I missed it.
  The obstruction stated in box 201 is unchanged: F = R118's R is close to T3 on every instance. Note the name clash: box 200's R (returns
  of one edge) is not R118's R (σ̄-changing steps); the latter is F here and in box 201.
- (2) k = 1: NOT proved. The natural route is DEAD on data, and so is the natural lemma:
  - Route: through R118 T-CYC, a polynomial bound on the σ̄-changing steps F suffices, since R118's C ≤ n3(2M + 2) is polynomial. F ≤ the
    total number of gate flips. So it suffices to bound each gate's flips.
  - CONJECTURE K1-FLIP «at k = 1 each gate flips at most 2·lamch(g) + 1 times, lamch(g) := #steps at which Λ changes at pe_g or pβ_g» would
    give F ≤ M(8M + 9) and T3 polynomial (Corollary K1-POLY below, PROVED conditional). It is DEAD. Instance k1fail_202.json (sha1
    99bba752, N 15, M 45, k 1; random search seed 202): gate (4, 0) flips 2 times with lamch 0. 67 failing gates in 20,000 random k = 1
    genomes (k1s_202.log). Max flips per gate in the sample is 4.
  - What the kill shows: at k = 1 a gate can flip at CONSTANT face cycle nodes. The flip is decided by Π, i.e. by the e-parts of the two
    face plays ending at the same node, not by Λ. That is the same mechanism as MW's gate flips at k = 2 (4n + 2 flips, lamch 0).
- Exact obstruction (where R122's proof stops): BETA-ACYC's step (3) («a cycle with no e- and no K-vertex is a cycle of the Ξ-graph:
  impossible») fails exactly at the Ξ-cycles through the feedback vertex f. A cycle through f whose cycle node is an odd β has reward
  < −5, which is BETTER for Odd than w* ∈ {K1 (5), K2 (3)}. So Odd may take an e-face at any gate whose e-face play reaches an odd f-cycle,
  and leave it again when Even's choices re-route that play. With Λ fixed, these reroutings are decided by Π: a gate re-flips each time
  the e-part of one face play overtakes the other's. Bounding that is the same leapfrog as LEAP (box 200), at one gate. k = 1 does not
  remove it; it only says that all non-core odd cycles share f.
- CONJECTURE K1-FLIP(2) («flips(g) ≤ 2·(lamch(g) + 1) at k = 1») has 0 failures on the same 20,000 genomes. With Corollary K1-POLY
  it would give T3 polynomial on k = 1. It is the k = 1 statement left standing, with thin data (§1).
- (3) General k: no theorem. The obstruction is the same per feedback vertex. MW (k = 2) realizes 4n + 2 flips at one gate (2n + 1 returns to each face) with face Λ
  fixed: any k-parameterized bound must charge Π-decided flips to something that grows. With MW, that is linear.

## 1. What is PROVED here (lane)
**Corollary K1-POLY (PROVED, CONDITIONAL on a per-gate flip bound; premises RESULTS R118 (d) BR-SEG, (l) / T-CYC with CYC-COUNT on Γ3
(«T3 ≤ C + R + (C + R + 1)·N and C ≤ (N + 7M + 10)(2M + 2)»), P-N5-CHAIN CYC and LOC-K2-3).** Let G be any genome (any k). If every gate g
of Γ3(G) flips at most φ(g) times in the run, then T3 ≤ C′ + F + (C′ + F + 1)·N with F ≤ Σ_g φ(g) and C′ ≤ (N + 7M + 10)(2M + 2).
Proof. R118's R counts steps at which σ̄ changes somewhere. σ̄(K2) = r at every state (LOC-K2-3), so every such step flips a gate:
R ≤ Σ_g flips(g) ≤ Σ_g φ(g). Insert into R118 (l). ∎
- With φ(g) = 2·lamch(g) + 1 (K1-FLIP): lamch(g) ≤ 2·(2M + 2) by CYC (each face's Λ takes ≤ 2M + 3 values and changes only upward), so
  F ≤ M(8M + 9). K1-FLIP is DEAD (§0), so this instance of the corollary has no premise. The corollary stands with any φ.
- With φ(g) = c·(lamch(g) + 1), c an absolute constant: CONJECTURE K1-FLIP(c) «on every genome with k = 1, every gate flips at most
  c·(lamch(g) + 1) times». It gives F ≤ c·M(4M + 5) and T3 polynomial on k = 1 (K1-POLY).
  - DATA for c = 2: counter k1c2fail (unit: gate; total) is 0 on 20,000 random k = 1 genomes (k1s_202c.log, the same sample as §2.3).
    Small genomes only (N ≤ 15, T3 ≤ 9), so the data say little.
  - At k = 2 no constant c works on MW: the flipping gate of MW(n) has lamch 0 (gflip202: MW4_2 18, MW8_2 34, MW16_2 66 flips = 4n + 2, all with lamch 0;
    gflip_mw.out). So K1-FLIP(c) is DEAD at k = 2 for every c, on MW. Whether k = 1 admits an MW-like family is the open design question.

## 2. DATA
### 2.1 k on the corpus (fvs202.py; unit: genome; T3 / C / R / F on the padded Γ3, N5′-xi from S3, up to the first fallback)
k, number of non-trivial Ξ-SCCs, largest SCC, movers on Ξ-cycles; T3; C (max c_y, per (v, I, y)); R (box 200's returns, per (u, b, w)); F
(steps with a gate flip = R118's R). Full table: box202/fvs202.out (53 rows). Selection:
| family / instance | N + M | k | T3 | C | R | F |
| --- | --- | --- | --- | --- | --- | --- |
| FW4_2 … FW16_2, FW6_3, FW6_4, FW8_4 | 163-1127 | 1 | 17-53 | 3-5 | 2 | 4-16 |
| C2_NM33 (L-COMP frontier) | 33 | 1 | 3 | 2 | 2 | 1 |
| MW4_2 … MW32_2, MW5_2, MW12_2, MW26_2 | 145-957 | 2 | 31-199 | 9-65 | 9-65 | 22-162 (= 5n + 2) |
| C3 … C12 (L-COMP frontier, 21e61663) | 45-176 | 2 | 6-24 | 3-12 | 3-12 | 6-24 |
| WC4_2 … WC16_2 | 60-216 | 2 | 4 | 1 | 1 | 1 |
| CT12_cap200 / CT26 / CT27 (L-RED MW mutants) | 200-400 | 12 / 8 / 8 | 46-79 | 12-27 | 12-27 | 14-18 |
| CX4_n21, C2CX4_n23, ROUTELOW_n21 | 56-61 | 4 | 10-11 | 2-5 | 4 | 10-11 |
| RWX_n95, C6G8_n54, DHIB18/26, DWT20, GROW8, HOLD2K/3K, W86, DSALT9 | 200-1217 | > 12 | 13-30 | 3-6 | 4-8 | 13-27 |
- Reading: the families where C grows (MW, frontier C-family, CT) have k ≤ 2 or k = 8-12; growth of C is not tied to large k. The
  climbed instances (L-RED's) have large k, because climbs add Ξ-edges freely, but C ≤ 6 there.
### 2.2 Per-gate flips (gflip202.py; unit: gate; per genome: maxflip, lamch at the argmax, k1fail = #gates with flips > 2·lamch + 1)
- FW4_2 (k 1): maxflip 1, k1fail 0. C2_NM33 (k 1): 1, 0. WC4_2 (k 2): 1, 0. MW4_2 (k 2): maxflip 18 at gate (46,0), lamch 0, k1fail 1.
  C3_NM45 (k 2): 6, lamch 0, k1fail 1. CX4_n21 (k 4): 7, lamch 0, k1fail 3. (box202/gflip202.out)
### 2.3 Random k = 1 / k = 2 search (k1srch202.py; generator eg195.gen 'acyc' + edges into one (two) chosen movers; unit: gate, totals
### over the sample; scope: Γ3, N5′-xi from S3, cap 3000)
- k = 1, seed 202, 20,000 genomes (4,050 generated with k ≠ 1 skipped): k1fail 67, k1c2fail 0, maxflip 4, max T3 9, max T3/N 2.0
  (k1s_202.log; k1c2fail from the identical re-run k1s_202c.log).
- k = 2, seed 203, 2,000 genomes: k1fail 7, maxflip 4, max T3 8 (k2s_203.log).
- Control K1_CTRL=1 (lamch := −1), seed 1, 50 genomes: k1fail 810, k1c2fail 101 (both fire; k1ctrl.log).
- Limits: these random genomes are tiny (N ≤ 15) and their runs short (T3 ≤ 9). They kill a constant; they say nothing about growth.
- First k = 1 failure frozen: box202/k1fail_202.json (sha1 99bba752a9fb9621c76324fec2e9a0d91115da1b).

## 3. Against TARGET.md (READING)
- Nothing here bounds N5′-xi on any class beyond R122's Ξ-acyclic one. The conditional K1-POLY is a restatement of R118 (l) with flips
  per gate in place of σ̄-changing steps. A k-parameterized polynomial bound would still be a RESTRICTED-CLASS result (TARGET.md §4: not
  M4), on Γ3(G) for N5′-xi only, and would not touch G-N5-TIME.
- Next step if pursued (READING): a per-gate statement that charges each Π-decided flip at constant face Λ to an e-letter entering one
  face's play. That is L-SI 48's GATE-RACE / TRIGGER, now at the feedback vertex's cycles. Then: whether at k = 1 such entries are bounded
  per gate by a polynomial. MW shows that at k = 2 they are not bounded by a constant.

## 4. Corrections to box 201 and to N5-CORE-forms (appended there as addenda that point here)
- C1 (box 201 §0, §1, «R's maximum sits at a GATE»): FALSE as a general data statement. L-RED 62 (claude/l-red c99bca51, R228-box200.md
  Addendum A, relayed by the Lead 02:43Z) has R = C at a MOVER on CT12_cap200 (12, out-degree 7) and CT27_cap400 (27, out-degree 14), every
  gate ≤ 2. My own box201/rarg.out already showed it, and I misread it:
  - mover strictly on top: RWX_n95 (x3: 3 vs gates ≤ 2), DHIB18_2805 (x12: 6 vs 5), FW16_2 (x258: 2 vs 1);
  - tie: CX4_n21 (x18 4 = gate (10,0) 4), MW32_2 (x299 65 = gate (298,0) 65);
  - gate strictly on top: C6G8_n54 (6 vs 5), DHIB26_2804 (8 vs 7).
  The corrected statement is: R's maximum is at a gate or at a mover, and the two are often equal (on MW, the race mover and its gate
  move together). So box 201's conclusion «every Even-side restriction leaves R untouched» is withdrawn. The mover out-degree class is
  dead for another reason: MW32_2's gate attains R = 65 at out-degree 2. That kills «R bounded by mover out-degree» but not «R bounded on
  genomes whose movers AND gates are restricted». Box 201's other conclusions (multi-switch steps are the norm; F ≈ T3) stand.
- C2 (box 201 «CONJECTURE SEG-H»): it is RESULTS R118 BR-SEG, landed (§0 above). L-RED 62's re-count: longest constant-(σ̄, Λ) run 7.
- C3 (N5-CORE-forms §4, A* column): the values given for FW16_2 («0-1») and DHIB26_2804 («6») are L-SI 48's ROUTE-vertex values. §1 defines
  A* over ALL vertices; L-RED 62 measured all-vertex A* = 9 on DHIB26_2804 and 8 on FW8_2 (relayed, not re-run here). The equivalence (5)
  is unaffected: it is proved for the all-vertex A*.
- C4 (k on climbed genomes, L-RED 62's bounds, relayed): RWX_n95 15, C6G8 / DHIB26 11-15, CT12 6-13, CT27 5-15. Mine (§2.1, exact
  where < 13): CT12 12, CT26 8, CT27 8; «>12» for RWX, C6G8, DHIB18/26. The two agree where both are defined.
