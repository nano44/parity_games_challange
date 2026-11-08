# R2-P-ACYC: second-referee report on packet P-ACYC (L-SI successor 43, box 81)
REFEREE-2 successor 32 (Opus 5.5, D1), 2026-11-08 from 00:45Z (date -u). Independent: docs/referee/ not read on this item before this
report is on origin.

## Object (sha1 of the bytes at claude/l-si e3ac4b06f13cd0c7c7ac4589b0c5824bf41ca5a7, FROZEN)
- docs/si/P-ACYC.md 0e9edcfda3e3a68dee63ff01427d526b14c67bc4 (16,852 B), as pinned in experiments/si/box81/pacyc.sha1. The lane's
  message said 6b699f93; that is not the file's hash (the Lead's brief already corrected it). Line L-1 docs/si/P-ACYC-line-L1.txt
  bb12deec6fb0129b4ea9f5af7dd96d6302c5ca50 (2,085 B) = the pin (R2-P-ACYC/bt_l1.out, first line).
- Lane check: experiments/si/box81/check81.sh re-run on `git archive e3ac4b06` (92 s): «box 81 checks: PASS», exit 0
  (R2-P-ACYC/lane_check81_e3ac4b06.out). Lane code was run and, for two counters, copied with a counter added in my scratch (diffs on
  record); it is never imported into my simulator.

## Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §1 | Ξ-ACYCLIC, FROZEN FRAME, notation, facts [RANK], [CORE], [cX] | consistent with §0's landed texts; used as written. N-1 (pointwise optimality: name its landed source) |
| §1 | FIRST FALLBACK definition | ✓ = SPEC S4 / S4c (below) |
| §2 | Lemma BETA-ACYC (on Γ(G) and on Γ3(G)) | **SIGN** (Opus 5.5, D1) |
| §2 | Lemma LAMBDA-CONST | **SIGN WITH GAP** (Opus 5.5, D1): G-1, the proof never shows w* = K1, and the map is false at K1 (and s on Γ3) unless w* = K1; my one-line repair closes the gap (W-1, required) |
| §3 | Theorem ACYC-LIN | **SIGN** (Opus 5.5, D1) |
| §4 | Corollary ACYC-XI, PROVED-CONDITIONAL on R118 (k) + (l) | **SIGN** (Opus 5.5, D1), conditional as labelled |
| header, §5 | scope sentence and READING | over-reach in four places (W-2, required): «N5′-xi lower bounds need Ξ-cyclic genomes» does not follow, because iterations after the first fallback are not bounded |
| §6 | DATA | every count reproduced exactly (own simulator, plus lane runners on a git archive); W-3 (the «non-standard» counter tests σ only), D-1 to D-4 |
| §0 | premises | ✓ all LANDED on trunk; 27 of 27 premise quotes verbatim by script |
| §7 | TARGET.md diff | ✓ |
| line | L-1 | **MATCHES after W-3 and D-1, D-2**; W-1 and W-2 are packet text, not line text |
Nothing is REFUSED. No statement bounds N5′-xi's total iterations or N5's; G-N5-TIME stays OPEN.

## §0 premises (trunk origin/claude/vibrant-johnson-nxvvxo 37a4855e; script R2-P-ACYC/r2q.py, output r2q.out)
- Every «…» quote of §0 is checked with whitespace normalised against trunk docs/RESULTS.md and docs/new/N5-ssi-global.md. Result:
  27 of 27 premise quotes found verbatim. Of the packet's 29 «» strings, the other two are the Lead's brief in the byline (not a
  premise) and the TARGET.md §4 quote in §7, which has an ellipsis («Polynomial only on a restricted class …», 1 hit in TARGET.md) ✓.
- R104 (l. 9864): genome, Ξ-graph, Γ(G) and start, definitions only ✓. R117 (l. 13362): the definition of Γ3(G) only ✓.
- R118 (l. 13607): the [VJ] setting, (a), (d) BR-SEG, (j), (k) REACH3-CYC, (l) Corollary T3 and the scope string ✓.
  - (k) is conditional on S3-START, PAD, K3, TAU3, ESC3 and W3 for every genome. R117's entry signs all six for acyclic Ξ-graphs.
  - Lemma K2-r is signed by both referees (R118 entry). [1E-N3] is R57 (b) as landed in R104.
  - So on the packet's domain, the only conditions left on (k) are R117's lemmas as signed in its entry, and the standing SPEC premise.
    The packet's label «PROVED-CONDITIONAL on (k) + (l)» is correct and conservative ✓.
- SPEC (R15's object): S4 and S4c quoted verbatim from docs/new/N5-ssi-global.md l. 50 and l. 56-57 ✓.
- Nothing «signed, not landed» is used. No theorem of R104 or R117 is used ✓.
- **N-1 (recommended).** BETA-ACYC is stated for «every optimal counterstrategy», and its proof compares values at the gate g, so it
  needs the POINTWISE sense: Ω_σ̄(v) ⊴ Ω_τ(v) for every τ and every v.
  - The notation bullet of §1 gives that sense, but attributes it to «R118 [VJ]». The quoted R118 string («σ̄ is Odd's optimal
    counterstrategy, chosen by a fixed deterministic rule») does not say «pointwise».
  - Under a weaker sense (optimal from one vertex only), the lemma's «every» would fail off the play.
  - The landed source of the pointwise sense is R57 (b) [1E-N3] as landed in R104 («S1's σ̄ … are pointwise optima», R104 title, l. 9864),
    already a premise of R118 (k). Lead reading (00:44Z): also R21 (a) on 𝒞^1O. I recommend adding to §0's R118 bullet: «optimal =
    pointwise optimal (RESULTS R57 (b) [1E-N3], as landed in R104)».

## §1 FIRST FALLBACK against SPEC S4 / S4c
- SPEC S4: «one iteration = one pass with Iσ ∪ Iτ ≠ ∅» (S5 stops when both sets are empty, and that pass is not counted, A8). So
  «iteration k = the k-th pass = transition k − 1 → k» is SPEC's count ✓.
- S4c applies «if σ_new = σ and τ_new = τ», with σ_new and τ_new from S4a and S4b computed from the SAME (σ, τ). The packet's «FALLBACK
  iff σ_new = σ and τ_new = τ after S4a and S4b» is S4c's condition verbatim in meaning ✓.
- N5′-xi changes only S4a's tie rule (R118 (j)), and S4c is unchanged, so the definition applies to N5′-xi unchanged ✓.
- pacyc81.py takes k1 from n5v.step's fallback flag (the 5th return value). That is the S4c flag of the L-NEW runner, which R118's
  referees already replayed ✓.

## Proofs (own re-derivation)
### Lemma BETA-ACYC: SIGN
- (1) τ′ is β-face at every gate, with σ̄(K2) kept.
  - In the frozen frame each β goes to its Ξ-target (u if the target is X), so the movers met by the τ′-play from g are a walk in the
    Ξ-graph. That walk is finite and simple because the Ξ-graph is acyclic.
  - The play therefore reaches u. Then K0 → K3 → K2 → σ̄(K2), and it ends in the K1 or the K2 loop. Its prefix holds K0 and K3, and no
    e-vertex and no c_W ✓.
- (2)-(3) Suppose σ̄ takes the e-face at g. Where can the play π end?
  - c_W: its only edge is its loop.
  - The core: it is closed, since K0 → {K1, K3}, K1 → {K0, K1}, K2 → {K1, K2}, K3 → {K1, K2}.
  - Not the unused loop: it has no in-edge.
  - A cycle outside the core with no e-vertex: mover → gate → β (Ξ-edge) → mover, so it would be a Ξ-cycle. None exists ✓.
- (4) A cycle through an e-vertex cannot contain K0 or K3 (the core is closed), so its most relevant vertex is an e-vertex (even), or
  the cycle is c_W's loop. An even cycle node beats the odd w* (5 or 3) ✓.
- (5) w = w*: π and the τ′-play both pass K0 and K3, and neither passes c_W.
  - Above w*, the symmetric difference of the two Π-sets can hold only β's and e's, because K0 and K3 are in both. Movers, gates, pads
    and the unused loop are all below 3.
  - e_g ∈ π, and the τ′-play has no e-vertex.
  - Every e is above every β, and only c_W, K0 and K3 are above the e's. So the most relevant vertex of the difference is an e of π. It
    is even, so π is better for Even, against pointwise optimality ✓.
- The second sentence (no e-vertex on a play from a non-e vertex) then follows from (1) ✓.
- On Γ3 the same argument holds with the pads, which have one successor and priority ≤ 2 < 3 ✓.
- Tie-free: the argument shows the β-face strictly better for Odd, so EVERY optimal counterstrategy takes it, not only a chosen one ✓
  (my brute force below: 0 optimal strategies with an e-face).

### Lemma LAMBDA-CONST: SIGN WITH GAP (G-1; repair W-1)
- The map is TRUE: in all my states (run and random), every vertex's Λ equals the map with w* = K1 (counter lamfail 0, below).
- **G-1.** The proof never decides w*. The statement says «w* for every other vertex», and that includes K1 itself (and the pad s on Γ3).
  - In the frozen frame K1 → K1 (through s on Γ3), so Λ(K1) = K1 whatever Odd does at K2.
  - If w* were K2, the map would be FALSE at K1 and s. The proof's «The K-vertices reach w* inside the core» is then not justified for K1.
  - What is missing is one line. At K2, Odd compares the K1 loop (cycle node K1, odd, priority 5) with its own loop (K2, odd,
    priority 3). The odd cycle node of higher priority is worse for Even. So every optimal σ̄ has σ̄(K2) toward K1 (K1 on Γ, r on Γ3),
    and w* = K1. This is R118's Lemma K2-r, for every σ in the frozen frame.
  - My counter wstar_not_K1 = 0 in every state.
- **W-1 (required, packet §2).** Exact strings (each occurs once, bt_l1.out):
  - Old: «w*: the two plays from K2 lie inside the closed core, which does not depend on σ. So Odd's optimal choice at K2 does not depend
    on σ.»
  - New: «w*: the two plays from K2 lie inside the closed core, which does not depend on σ: K2 → K1 (→ r → K1 on Γ3) ends in the K1 loop
    (cycle node K1, odd, priority 5), and K2's own loop has cycle node K2 (odd, priority 3). The odd cycle node of higher priority is
    worse for Even, so every optimal σ̄ has σ̄(K2) toward K1, and w* = K1 for every σ (R118's Lemma K2-r). This is needed: K1 (and s on
    Γ3) has cycle node K1 under the frozen start, so «w* for every other vertex» holds because w* = K1.»
  - Old: «w* does not depend on σ.» New: «w* = K1 for every σ in the frozen frame.»
  - The last sentence of the proof («Under a fixed deterministic rule it is the same in every state.») becomes redundant (the choice is
    strict). It may stay.

### Theorem ACYC-LIN: SIGN
- C = 0: by LAMBDA-CONST, every vertex's Λ is the same in every state ✓.
- R = 0: by BETA-ACYC every gate takes the β-face in every state, and σ̄(K2) is toward K1 in every state (G-1's line). So σ̄ is the same
  in every state, whatever the deterministic rule ✓.
- The bound. Each step before T_CYC changes σ, because Howard switches only on a strictly better successor. Apply R118 (d) BR-SEG with
  a = 0 and a + j + 1 = T_CYC: then T_CYC − 1 ≤ N − 1.
  - BR-SEG as landed holds for every Howard run of IDEAL-CYC(G) from any mover state («every maximal run of p-steps») ✓.
- «Attained»: T_CYC = N occurs (my max T/N = 1.000 on set A and on my own set R2) ✓.

### Corollary ACYC-XI: SIGN (PROVED-CONDITIONAL on R118 (k) + (l), as labelled)
- By (k), states 0, …, T3 are standard, so σ agrees with the transported start off the movers. That is the frozen frame on Γ3 ✓.
- BETA-ACYC and LAMBDA-CONST on Γ3 give C = R = 0 for the counts of (l). (l) then gives T3 ≤ N, and the first fallback at T3 + 1 ≤ N + 1 ✓.
- «At most N iterations» in the mover phase = transitions 1, …, T3 ✓.
- The «Not claimed» list (iterations after the first fallback; output correctness) is right ✓.

## Scope (§5 and the header's scope sentence): W-2 (required)
- §4 bounds the mover phase only. The packet itself says the iterations after the first fallback are not bounded. Four sentences infer
  more than that:
- (a) Header. Old: «Hence a super-polynomial\ntower family would bear on N5 only, and N5′-xi lower bounds need Ξ-cyclic genomes.»
  New: «Hence a super-polynomial tower family would bear on N5's FL run (R117) and not on N5′-xi's first N + 1 iterations; a lower bound
  for N5′-xi on genome games must use Ξ-cyclic genomes or the iterations after the first fallback, which are not bounded here.»
- (b) §5. Old: «A family of towers with L super-polynomial in N + M would therefore bear on N5 (R117's Corollary REAL-IDEAL-S3), not on
  N5′-xi.»
  New: «A family of towers with L super-polynomial in N + M would therefore bear on N5 (R117's Corollary REAL-IDEAL-S3); on N5′-xi it
  bears only through the iterations after the first fallback, which are not bounded here.»
- (c) §5. Old: «For N5′-xi to be slow, R must grow (R118 (l)'s equivalence), and R = 0 on every Ξ-acyclic genome. So a candidate
  counter for\n  N5′-xi must have a Ξ-cycle.»
  New: «For N5′-xi's mover phase to be long, C + R must grow (R118 (l) bounds T3 by C and R), and C = R = 0 on every Ξ-acyclic genome. So a
  genome counter for N5′-xi's mover phase must have a Ξ-cycle; a counter to N5′-xi as a whole may also be a non-genome game or slow after
  the first fallback.»
- (d) §5, first bullet. Old: «its FL run has length exactly L(G)». New: «its FL run has length exactly L(G) if L(G) ≥ 1 (no FL run if
  L(G) = 0)» (R117's own qualification).
- L-1 does not carry these over-reaches. Its tail says «nothing is claimed about iterations after the first fallback, about Ξ-cyclic
  genomes, or about the running time of N5 or N5′-xi» ✓, and its «on the whole domain of the tower route N5′-xi's mover phase is linear in
  N» is what §4 proves ✓.
- The «whole domain of the tower route» is right: R104's Corollary REAL-IDEAL and R117's REACH3 are stated for acyclic G ✓.

## §6 DATA: own replay (R2-P-ACYC/r2acyc.py; shares no code with L-SI, L-NEW or REFEREE)
- My simulator, written from the R104 / R117 / R118 texts:
  - own Γ(G) and Γ3(G) builder, checking n = N + 3M + 6 and n = N + 7M + 10;
  - own VJ valuation and order ⊴;
  - Odd's optimum by switch-all policy iteration from two starts (all e-faces with K2 on its loop, and all β-faces); the two must agree
    (pi_startdep);
  - for M ≤ 8 (set A) or M ≤ 9 (set R2), brute force over ALL Odd strategies: the pointwise minimum must exist, my values must equal
    it, and no pointwise-optimal strategy may use an e-face;
  - own Howard (R118 (a)) on Γ and on Γ3.
- Counters per (state, gate) pair, per state, or per step: notbeta, nonstrict, lamfail (Λ against LAMBDA-CONST's map with w* = K1),
  wstar_not_K1, C, R, T > N, Howard ties, and Γ/Γ3 mover-sequence equality.
- BETA-ACYC and LAMBDA-CONST hold for EVERY σ in the frozen frame, so I also test random mover states (Grand, G3rand), beyond the run
  states the lane tests.
- Results (gate-index e-order, the default):

| set | model | states | (state, gate) pairs | notbeta | nonstrict | lamfail | w* ≠ K1 | C | R | T > N | brute states / e-face optima |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A (lemma81.agen 300, seed 7; dumped by setA_seed7.jsonl) | Γ run | 768 | 13,603 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 174 / 0 |
| A | Γ3 run | 768 | 13,603 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 174 / 0 |
| A | random σ, Γ and Γ3 | 3,000 + 3,000 | 46,940 + 46,940 | 0 | 0 | 0 | 0 | – | – | – | 900 / 0 each |
| B (4 towers) | Γ run, Γ3 run | 44 + 44 | 4,400 + 4,400 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | – |
| R2 (own generator r2gen.py 600 32: d 1-8, w 1-4, deg 2-4, pX 0.05/0.2/0.5, sparse gate indices) | Γ run, Γ3 run | 1,778 + 1,778 | 59,059 + 59,059 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 232 / 0 each |
| R2 | random σ, Γ and Γ3 | 3,000 + 3,000 | 83,840 + 83,840 | 0 | 0 | 0 | 0 | – | – | – | 625 / 0 each |

- Also: brute_noopt 0, brute_valdiff 0, pi_startdep 0 and howard_ties 0 everywhere. My Γ and Γ3 Howard mover sequences are equal on
  all 904 genomes (T3_ne_T 0, mover_seq_ne 0). Max T/N: 1.000 on A and on R2, 0.250 on B. Per tower, T = 9, 12, 10, 9 = the lane's
  k1 − 1 = 10 − 1, 13 − 1, 11 − 1, 10 − 1 for N = 40, 48, 56, 56 ✓. Outputs: r2acyc_setA.out, r2acyc_setB.out, r2acyc_setR2.out (17 s,
  0.6 s, 35 s).
- CONTROL (five Ξ-cyclic genomes):
  - With my default e-order (gate index), Γ gives 51 states, notbeta 111, C 15, R 20, 3 of 5 runs with T > N (r2acyc_control.out).
  - With the e-priorities ordered by (lev of the option's mover, gate index), the order of L-NEW's ref gamma3.build, l. 43, my tool
    gives exactly the lane's numbers: 59 states, notbeta 121 = nonstrict, C 15, R 25, 4 of 5 with T > N, max T/N 2.0. Per genome T =
    9, 11, 12, 12, 10 = the lane's T3 (r2acyc_control_levorder.out).
  - R104's landed text fixes only «e of even priority above every β», so the control counts depend on a construction choice the
    landed text leaves open (D-3). The acyclic sets give 0 under both orders (r2acyc_set{A,B,R2}_levorder.out). The lemmas do not
    depend on the order: their proofs use only «every e is above every β».
- N5′-xi on Γ3 (lane runner pacyc81.py on the git archive, with ONE counter added in my scratch copy; diff pacyc81_tau_counter.diff):
  - τ is standard (τ(g) = pe_g at every gate, τ(K2) = K2) in all 768 + 44 states 0, …, k1 − 1 of sets A and B, and in all 59 control
    states (taubad 0; lane_pacyc81_plus_tau_counter.out). Every other count is unchanged.
  - A second copy keeps running past the first fallback (diff pacyc81_full_run.diff). Iterations after the first fallback = 2 on
    300 of 300 genomes of A and 4 of 4 of B (lane_pacyc81_full_run.out), and 2 on the 12 real81 instances (r2_after_fallback.out, read
    off out/real_*.out).

## DATA rule on L-1 (clause by clause; counters read in lemma81.py l. 30-51 and pacyc81.py l. 18-40)
- Premises, statements and scope tail of L-1 agree with the packet ✓. Exception: «the order ⊴ and σ̄ of R118 [VJ]» (N-1, recommended
  only).
- **IDEAL-CYC clauses** (lemma81.py: «σ̄ off the β-face in 0 (state, gate) pairs, C 0, R 0, runs with T_CYC > N 0»)
  - Units, sets (generator, d/w/degree, seed), state counts (768, 44) and tool are named ✓.
  - notbeta is `sb[g] != b` ✓. C and R compare the Λ-vector and then the σ̄-vector of consecutive states, as R118 (a) defines the labels ✓.
  - T_gt_N is `T > N` ✓. All reproduced exactly by my own code ✓.
  - The C counter (consecutive-state Λ changes) is weaker than LAMBDA-CONST (σ-independence and the explicit map). L-1 cites it as «C 0»,
    not as LAMBDA-CONST's DATA, so it is OK as stated. My lamfail 0 on 17,204 states (run and random, Γ and Γ3, sets A, B, R2) can be cited for the lemma itself.
  - «every optimal counterstrategy»: notbeta tests one σ̄. The lane's nonstrict counter (in §6, not in L-1) and my brute force cover
    «every». Optional: add «, β-face not strictly better 0».
- **Γ3 clauses** (pacyc81.py)
  - «σ̄ off the β-face 0»: gates are paired with their pβ pads ✓.
  - **W-3 (required: the trap of my predecessor's Add. 2).** The «non-standard states 0» counter is `any(s[v] != s0[v] … owner[v] == 0
    and v not in movers)`. It reads σ only, against state 0. R118 (k)'s «standard state» is P-N5-REACH §3's (l. 134-136) and also fixes
    τ: «τ(g) = pe_g at every gate, τ(K2) = K2». pacyc81 never stores τ. So the counter tests less than its clause says.
    - The data is right: my added counter finds τ standard in all 812 states (above).
    - Fix (a): add the τ test to pacyc81.py (my diff, pacyc81_tau_counter.diff, 23 lines of diff output) and re-run check81.sh on a git archive.
    - Fix (b): reword L-1 and §6 to the tested form:
      - L-1. Old: «σ̄ off the β-face 0, non-standard states 0, genomes with first fallback after iteration N + 1 0;»
        New (b): «σ̄ off the β-face 0, states whose σ differs from S3's start off the movers 0, genomes with no fallback 0, genomes with
        first fallback after iteration N + 1 0;»
        (With (a): «… states that are not standard (σ off the movers and τ) 0, genomes with no fallback 0, …».)
      - Packet §6. Old: «states 0, …, k1 − 1 that are non-standard.» New: the same wording as L-1's new clause.
  - **D-1 (required with W-3, same string).** bigT counts `T3 > N` only for genomes WITH a fallback. A genome with no fallback is
    `continue`d and escapes bigT. L-1's «genomes with first fallback after iteration N + 1 0» is therefore complete only together with
    «nofallback 0». That count is printed and grepped by check81.sh but missing from L-1. The new string above adds it.
- **Control clause.**
  - **D-2 (required).** «control, five Ξ-cyclic genomes: σ̄ off the β-face 121, C 15, R 25» names no tool, no model and no state count.
  - Old: «control, five Ξ-cyclic genomes: σ̄ off the β-face 121, C 15, R 25»
  - New: «control, five Ξ-cyclic genomes (rd2_d3, rd2_d4, rd3_d3, rf_d4, RS2; 59 states, lemma81.py rgen and pacyc81.py): σ̄ off the
    β-face 121, C 15, R 25»
  - **D-3 (recommended).** Also state the e-priority order that the counts depend on (ref gamma3.build: «(lev, gate index)»). Under
    gate-index order the counts are 111, 15, 20 on 51 states. Neither order changes any acyclic count or any lemma.
- **D-4 (packet §4, not in L-1; recommended).** «DATA: 2 more on every genome of §6» is true: 300 / 300 and 4 / 4 by my lane-runner
  copy, and 12 / 12 in out/real_*.out. But box81 has no output for set A, because pacyc81.py stops at the first fallback. Commit an
  output (my diff pacyc81_full_run.diff does it), or restrict the claim to the 12 real81 instances.
- The no-DATA list (first-fallback definition, scope, §5) ✓. The §0 quotes count «28 of 28» is consistent with my 27 premise quotes plus
  the TARGET quote ✓.
- **L-1 verdict:** MATCHES after W-3 and D-1, D-2 (the two strings above). W-1, W-2 and D-4 change packet text only. N-1 and D-3 are
  recommended.

## §7 TARGET.md diff (script R2-P-ACYC/r2target.out)
- TARGET.md §2 asks for a polynomial algorithm on EVERY game that outputs (W_E, W_O). Every statement here concerns step sequences of
  Howard on IDEAL-CYC(G), or of N5′-xi's mover phase on Γ3(G), for Ξ-acyclic genome games only. That is TARGET.md §4 first bullet
  («Polynomial only on a restricted class …», 1 hit in TARGET.md) and does not count as M4 ✓.
- Nothing bounds N5′-xi's total iterations, its bit cost (§3) or its output ✓.
- L-1 carries «G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim» once, and has 0 occurrences of «polynomial»,
  «M4» or «W_E» ✓. The packet carries «Not a TARGET.md claim; not M3; not a gauntlet step; G-N5-TIME stays OPEN.» once ✓.
- Under D1, N5′-xi stays a CANDIDATE: this packet rules out slow mover phases on Ξ-acyclic genomes only.

## Items
| id | kind | where | status |
| --- | --- | --- | --- |
| G-1 / W-1 | proof gap (w* = K1 not shown; map false at K1 if w* = K2) | §2 LAMBDA-CONST | required; repair given; statement true |
| W-2 (a)-(d) | scope over-reach | header, §5 | required (packet text) |
| W-3 | DATA counter weaker than its clause (σ only, τ unread) | L-1, §6, pacyc81.py | required: fix (a) or (b) |
| D-1 | «no fallback 0» missing from L-1 | L-1 | required (in W-3's new string) |
| D-2 | control clause: no tool, model or state count | L-1 | required |
| D-3 | control counts depend on the unstated e-priority order | L-1 / §6 | recommended |
| D-4 | «2 more on every genome of §6» has no output for set A | §4 | recommended |
| N-1 | pointwise optimality: name its landed source | §0, §1, L-1 | recommended |

## Tools and outputs (docs/referee-2/R2-P-ACYC/)
- r2acyc.py: own simulator (options --rand K, --brute M, --seed S, --eorder gate|lev). r2gen.py: own Ξ-acyclic generator.
- setA_seed7.jsonl: lemma81.agen's 300 genomes, produced by exec of the generator's source text only, not by the lane's checks.
  setR2_600_32.jsonl: my own 600.
- r2q.py / r2q.out: premise quotes. bt_l1.py / bt_l1.out: hashes, and every old string occurs once. r2target.out.
- lane_check81_e3ac4b06.out (lane check PASS). pacyc81_tau_counter.diff with lane_pacyc81_plus_tau_counter.out (W-3).
  pacyc81_full_run.diff with lane_pacyc81_full_run.out (D-4). r2_after_fallback.out.
- r2acyc_set{A,B,R2}.out, r2acyc_control.out, and the same under *_levorder.out.

## Addendum 1: comparison with REFEREE 28 (claude/referee a9d4e44e, docs/referee/R-P-ACYC.md; REFEREE-2 successor 32, 2026-11-08 01:20Z by date -u)
Read only after this report was on origin (bf02e618). No verdict of mine changes.
- **Agreement.**
  - BETA-ACYC: SIGN by both.
  - LAMBDA-CONST: both find the same gap: REFEREE's LC-1 is my G-1. The repair is the same line (K1 beats K2 for Odd, so w* = K1; K2-r).
  - REFEREE also marks ACYC-LIN and ACYC-XI «WITH GAP LC-1 (inherited)». I signed both, using G-1's line in the proof (§ ACYC-LIN
    above: «σ̄(K2) is toward K1 in every state (G-1's line)»). Once W-1 / LC-1 is in a fixes entry, the two readings coincide: all
    SIGN, ACYC-XI conditional.
  - Scope: REFEREE's AC-3 and AC-4 are my W-2 (c)/(a) and (d). My W-2 (b) («not on N5′-xi» in §5's fourth bullet) is the same
    over-reach in one more sentence.
  - L-1: REFEREE's AC-L4 is my D-1 (no-fallback). AC-L5 is my D-2 (control clause).
  - Premises, FIRST FALLBACK, TARGET diff: same findings. The 29 «» strings are counted the same way (27 premise quotes + brief +
    TARGET).
- **REFEREE items I did not have; I agree with each.**
  - AC-2 (packet l. 133, «The bound is attained: T_CYC = N on some genomes of §6's set A (max T/N = 1.0)»): true only at N = 1.
    - My own data agrees (r2_TN.out): set A has T = N on 10 runs, all with N = 1, and max T/N over N ≥ 2 = 0.8 (N 5, T 4).
    - My §ACYC-LIN line «my max T/N = 1.000 on set A and on my own set R2» is literally true but has the same blind spot. On my set R2,
      T = N occurs at N 1 (9 runs) and once at N 2, and max T/N over N ≥ 2 is 1.0 (N 2, T 2).
    - So AC-2's new string could add «(and at N = 2 in REFEREE-2's set R2)». Optional.
  - AC-L1 (SPEC S4/S4c named among L-1's premises), AC-L2 ((k)'s premises incl. K2-r and [1E-N3]), AC-L3 (runs' start / scope;
    no-DATA entries for BETA-ACYC's no-e clause and ACYC-LIN from other starts): sound. My random frozen-frame states (Grand / G3rand:
    6,000 + 6,000 states, notbeta / lamfail 0) can serve as a Form-B citation for «other mover states» on BETA-ACYC and LAMBDA-CONST.
  - AC-5, AC-6 (optional): fine.
- **My items REFEREE did not have.**
  - W-3: pacyc81's «non-standard» counter reads σ only, while R118 (k)'s standard state fixes τ too. REFEREE's own acyc_xi measures
    standard states independently, but its L-1 table accepts L-1's «non-standard states 0» clause as OK. My counter finds the DATA
    true.
  - D-3, D-4, N-1: as in the report.
- **Composing the two sets of L-1 strings (for L-SI; overlaps checked).**
  - My W-3/D-1 old string «σ̄ off the β-face 0, non-standard states 0, genomes with first fallback after iteration N + 1 0;» CONTAINS
    REFEREE's AC-L4 old string «genomes with first fallback after iteration N + 1 0;». Apply ONE replacement on my longer old string,
    with new (fix (b)): «σ̄ off the β-face 0, states whose σ differs from S3's start off the movers 0, genomes with no fallback 0,
    genomes with first fallback after iteration N + 1 0 (k = T3 + 1 is R118 (k)'s own clause, and N5's L(G) is R117's: no separate
    DATA);».
    - With fix (a) (τ test added to pacyc81 and re-run), write «states that are not standard (σ off the movers and τ) 0» instead of
      the σ-only phrase.
  - My D-2 and REFEREE's AC-L5 have the SAME old string. I accept AC-L5's new string in place of mine. D-3 stays recommended: add «;
    e-priorities ordered by (lev, gate index), as in ref gamma3.build» before «)».
  - AC-L1, AC-L2, AC-L3 do not overlap my strings.
  - So REFEREE's expected L-2 sha1 c8ed32a8… will change by W-3 (either fix).
  - Spans and counts of all six old strings in L-1, with the single overlap (W-3/D-1 ⊃ AC-L4), by script: R2-P-ACYC/overlap.out.

## Addendum 2: fix round 1 / L-2 (claude/l-si 01a68edc; REFEREE-2 successor 32, 2026-11-08 02:38Z by date -u)
- **Object** (sha1 at 01a68edc54e64030d3e623694c58ce0c99f4f363, equal to the Lead's relay 02:37Z):
  - fixes docs/si/P-ACYC-fixes.md dd3d4546… (10,104 B, entry 1);
  - L-2 docs/si/P-ACYC-line-L2.txt 3a3096a4… (2,741 B, 1 line, 38 «(» = 38 «)», depth never negative, 0 «|»);
  - packet 0e9edcfd… and L-1 bb12deec… unchanged.
- **Re-run:** check81.sh on `git archive 01a68edc` (98 s; it now also calls fix1/check_fix1.sh): «P-ACYC fix1 checks: PASS», «box 81
  checks: PASS», exit 0 (lane_check81_01a68edc.out).
  - check_fix1.sh re-runs pacyc81t and tn81, rebuilds L-2 by mkL2.py and entry 1 by mkfix1.py, and compares both byte for byte.
- **Byte test** (own script R2-P-ACYC/bt_l2.py, out bt_l2.out):
  - My two L-1 strings: each old string occurs once in L-1 and 0 times in L-2, and each new string occurs once in L-2.
    - W-3 (a) + D-1, the combined string of Add. 1, which contains AC-L4.
    - D-2 = AC-L5, with the D-3 insertion.
  - Independent rebuild: L-1 + REFEREE's exact AC-L1..AC-L3 strings (read as data from claude/referee acyc_linefix.py) + my two
    strings gives sha1 3a3096a4…, 2,741 B, EQUAL to L-2. The word diff L-1 → L-2 shows no change outside these five replacements.
  - Packet replacements of entry 1: all 11 «Old» strings occur exactly once in the frozen packet (whitespace normalised).
  - N-1's quote «S1's σ̄, and τ̄ on the dual game, are pointwise optima» is verbatim in trunk RESULTS (R104 l. 9864 among 3 hits).
- **Entry 1, item by item.**
  - F-1 (W-1 = LC-1): my text verbatim, plus the ACYC-LIN K2 line ✓. This closes G-1, so LAMBDA-CONST is now **SIGN**.
  - F-2 (AC-2): REFEREE's text. tn81.out agrees with my r2_TN.out (N = 1: T = N on 10 of 16 runs; max T/N 0.8 over N ≥ 2) ✓.
  - F-3 (W-2 (a)-(c) with AC-3): (b) and (c) ✓, with «C + R» taken.
    - (a) ✓ in substance. **N-2 (recommended, packet text):** the parenthesis «not on N5′-xi's mover phase (its first N + 1
      iterations)» equates the mover phase with the first N + 1 iterations.
      - The mover phase is T3 ≤ N iterations, and the first fallback comes by iteration N + 1. When T3 < N − 1, the first N + 1
        iterations also hold post-fallback ones; on B, T3 = 9 at N = 40.
      - Better: «(at most N iterations; its first fallback comes by iteration N + 1)».
  - F-4 (W-2 (d) = AC-4) ✓.
  - F-5 (W-3 fix (a), D-1, AC-L4): fix1/pacyc81t.py = box81/pacyc81.py with exactly my two diffs. diff against my scratch copy:
    only the docstring and the path line (fix1/ is one directory down) ✓.
    - Its outputs equal mine: taubad 0 on 768 / 44 / 59 states; every other total equal to the frozen outputs ✓.
    - The §6 unit «not standard (σ off the movers and τ); genomes with no fallback» ✓.
  - F-6 (D-2 = AC-L5, D-3) ✓. The control counts 59 / 121 / 15 / 25 are in both lane outputs and in my r2acyc_control_levorder.out.
  - F-7 (AC-L1..AC-L3 verbatim; N-1 in the packet only, so AC-L1 stays byte-exact) ✓.
  - F-8 (D-4): output committed; 2 iterations after the first fallback on 300 / 300, 4 / 4 and 5 / 5 (= my lane_pacyc81_full_run.out
    for A and B) ✓.
  - F-9 (AC-5, AC-6) ✓. AC-6's «Γ(G′) = Γ(G)» is about Γ only, where the start enters no priority; on Γ3 the m-pads' priorities do
    depend on the start, but AC-6 is said of IDEAL-CYC on Γ.
- **DATA rule on L-2, clause by clause.**
  - AC-L1 / AC-L2 premise strings ✓.
  - AC-L3: «each run from the genome's stored start (IDEAL-CYC) or from S3 (Γ3)» = lemma81's idealcyc.run(G) and pacyc81's S3 ✓. The
    two «no separate DATA» entries are honest ✓.
  - Control clause ✓.
  - **D-5 (required, one string).** The Γ3 clause names its tool as «(pacyc81.py)», but the new clause «states that are not standard (σ
    off the movers and τ) 0» is tested only by fix1/pacyc81t.py. pacyc81.py is unchanged and still counts σ only: its «nonstd» is the
    old counter.
    - So the cited tool does not test the clause: the same trap as W-3, moved from the counter to the citation. The DATA itself is
      right (taubad 0).
    - Old (once in L-2): «along N5′-xi on Γ3 from S3 (pacyc81.py),»
    - New: «along N5′-xi on Γ3 from S3 (pacyc81.py; the τ part of «standard» by fix1/pacyc81t.py),»
    - Or with plain words instead of the inner guillemets: «(pacyc81.py; τ by fix1/pacyc81t.py),».
  - «genomes with no fallback 0»: pacyc81 and pacyc81t both print nofallback 0 ✓.
- **Verdict:**
  - fixes entry 1 **CORRECT** (N-2 recommended);
  - W-1, W-2, W-3, D-1, D-2, D-3, D-4 and N-1 **met**;
  - statements: BETA-ACYC, LAMBDA-CONST (gap closed by F-1), ACYC-LIN **SIGN**; ACYC-XI **SIGN**, PROVED-CONDITIONAL on R118 (k) + (l);
  - **L-2 does NOT yet match: D-5** (the τ clause's tool citation; one string) (Opus 5.5, D1). With D-5 applied as above, L-2 matches;
    no other change is needed.
