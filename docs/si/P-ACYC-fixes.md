# P-ACYC fixes (the packet docs/si/P-ACYC.md and its line L-1 stay frozen at e3ac4b06, sha1 0e9edcfd… and bb12deec…; every repair is here)

## Entry 1 (fix round 1; L-SI successor 44; Lead 01:22Z and 01:39Z)
Items: REFEREE 28 (claude/referee d3d0a600, docs/referee/R-P-ACYC.md): LC-1, AC-2, AC-3, AC-4, AC-L1 to AC-L5 required; AC-5, AC-6
optional, taken. REFEREE-2 32 (claude/referee-2 bf02e618, docs/referee-2/R2-P-ACYC.md; Addendum 1 at 6c937bc6): W-1 (G-1), W-2 (a)-(d), W-3, D-1, D-2 required;
D-3, D-4, N-1 recommended, taken. Overlaps (Lead 01:39Z): LC-1 = W-1; AC-3 = W-2 (a)-(c); AC-4 = W-2 (d); AC-L4 ∩ D-1 ∩ W-3 and
AC-L5 ∩ D-2 are one clause each in L-2. Strings: this text by experiments/si/box81/fix1/mkfix1.py (each Old asserted once in the frozen
packet); L-2 by fix1/mkL2.py. Both reports are byte-copied in fix1/ (ref_d3d0a600.md, ref2_6c937bc6.md (report + Addendum 1); pinned in fix1/fix1.sha1).

### F-1 (LC-1 = W-1 (G-1), required): LAMBDA-CONST decides w* = K1, and σ̄(K2) is unique
- Old (§2): «w* does not depend on σ. Proof.» New: «w* = K1 for every σ in the frozen frame. Proof.»
- Old (§2, proof): «- w*: the two plays from K2 lie inside the closed core, which does not depend on σ. So Odd's optimal choice at K2 does not depend on σ.»
  New (REFEREE-2's text, which also carries REFEREE's uniqueness point): «- w*: the two plays from K2 lie inside the closed core, which
  does not depend on σ: K2 → K1 (→ r → K1 on Γ3) ends in the K1 loop (cycle node K1, odd, priority 5), and K2's own loop has cycle node
  K2 (odd, priority 3). The odd cycle node of higher priority is worse for Even, so every optimal σ̄ has σ̄(K2) toward K1, and w* = K1
  for every σ (R118's Lemma K2-r). This is needed: K1 (and s on Γ3) has cycle node K1 under the frozen start, so «w* for every other
  vertex» holds because w* = K1.»
- The last proof sentence («Under a fixed deterministic rule it is the same in every state.») stays and is now redundant: the optimum at
  K2 is unique (REFEREE: K1 on Γ, r on Γ3), so no tie rule is involved.
- §3 ACYC-LIN, R = 0. Old: «at K2 the same choice (LAMBDA-CONST's proof).» New: «at K2 the unique optimal choice, toward K1 (K1 on Γ, r on Γ3; LAMBDA-CONST's proof as
  repaired in F-1).» This closes REFEREE's LC-1 for ACYC-LIN; ACYC-XI inherits it (on Γ3 also by (k)'s own Lemma K2-r).
- DATA (referees' own counters): lamfail 0 and wstar_not_K1 0 (REFEREE-2, 17,204 states); lamfail 0 (REFEREE, 768 + 44 states on Γ
  and Γ3, and 3,842 states from random starts).

### F-2 (AC-2, required): «attained» corrected
- Old (§3): «- The bound is attained: T_CYC = N on some genomes of §6's set A (max T/N = 1.0).»
  New (REFEREE's text): «- T_CYC = N occurs in set A only at N = 1 (10 runs); over N ≥ 2 the largest T_CYC / N is 0.8 (N 5, T 4).»
- Re-measured by fix1/tn81.py (lemma81's generator stream, seed 7) → fix1/tn81.out: N = 1: 16 runs, T = N on 10; N ≥ 2: T = N on 0,
  max T/N 0.800 (N 5). T_CYC ≤ N is unchanged (it is a bound, not claimed tight for N ≥ 2). REFEREE-2 Add. 1 (r2_TN.out) agrees and
  adds that on its own set R2, T = N occurs once at N = 2 (optional addition, not taken into the packet text: set R2 is not §6's set).

### F-3 (AC-3 = W-2 (a)-(c), required): scope sentences, the two referees' texts reconciled
- Both texts say the same thing: §4 bounds the mover phase only. REFEREE-2's adds that a lower bound may come from the iterations after
  the first fallback; REFEREE's adds «on Γ3(G) from S3» and «games not of the form Γ3(G)». I keep both additions. Where the two disagree
  in wording I take REFEREE-2's «C + R» (R118 (l) bounds T3 by C and R; on acyclic genomes both are 0), because «R must grow» alone
  ignores C.
- (a) Header. Old: «Hence a super-polynomial tower family would bear on N5 only, and N5′-xi lower bounds need Ξ-cyclic genomes.»
  New: «Hence a super-polynomial tower family would bear on N5's FL run (R117), not on N5′-xi's mover phase (its first N + 1
  iterations); a genome family on which N5′-xi's mover phase on Γ3(G) from S3 is super-polynomial must have Ξ-cycles, and a lower bound
  for N5′-xi as a whole may also use the iterations after the first fallback or games not of the form Γ3(G), which are not covered here.»
- (b) §5 (REFEREE-2 (b)). Old: «A family of towers with L super-polynomial in N + M would therefore bear on N5 (R117's Corollary REAL-IDEAL-S3), not on N5′-xi.»
  New: «A family of towers with L super-polynomial in N + M would therefore bear on N5 (R117's Corollary REAL-IDEAL-S3); on N5′-xi it
  bears only through the iterations after the first fallback, which are not bounded here.»
- (c) §5. Old: «For N5′-xi to be slow, R must grow (R118 (l)'s equivalence), and R = 0 on every Ξ-acyclic genome. So a candidate counter for   N5′-xi must have a Ξ-cycle.»
  New: «For N5′-xi's mover phase on Γ3(G) to be long, C + R must grow (R118 (l) bounds T3 by C and R), and C = R = 0 on every Ξ-acyclic
  genome. So a genome family with a long N5′-xi mover phase must have Ξ-cycles; the iterations after the first fallback, and games not
  of the form Γ3(G), are not covered.»

### F-4 (AC-4 = W-2 (d), required)
- Old (§5): «its FL run has length exactly L(G) (R117:» New: «its FL run has length exactly L(G) if L(G) ≥ 1 (no FL run if L(G) = 0) (R117:»

### F-5 (W-3 fix (a) + D-1 + AC-L4, required): the standard-state counter reads τ; «no fallback» is in the line
- Tool: fix1/pacyc81t.py = box81/pacyc81.py (unchanged: the frozen packet cites it) with REFEREE-2's two diffs applied
  (pacyc81_tau_counter.diff, pacyc81_full_run.diff at bf02e618). New counter taubad = states 0, …, k1 − 1 whose τ is not R118 (k)'s
  standard τ (τ(g) = pe_g at every gate, τ(K2) = K2).
- Re-run (fix1/pacyc81t_agen_300_7.out, _towers.out, _cyclic_control.out; re-run and diffed by box81/check81.sh): taubad 0 on set A
  (768 states), set B (44) and the control (59). Every other total equals the frozen out/pacyc81_*.out.
- §6, ACYC-XI unit. Old: «states 0, …, k1 − 1 that are non-standard.»
  New: «states 0, …, k1 − 1 that are not standard (σ off the movers and τ); genomes with no fallback.» Counts: A 0, 0, 0; B 0, 0, 0.
- L-2: ONE replacement of REFEREE-2's longer old string «σ̄ off the β-face 0, non-standard states 0, genomes with first fallback after
  iteration N + 1 0;», which contains REFEREE's AC-L4 old string. New = REFEREE-2 Add. 1's combined string (claude/referee-2 6c937bc6),
  fix (a) form: «σ̄ off the β-face 0, states that are not standard (σ off the movers and τ) 0, genomes with no fallback 0, genomes with
  first fallback after iteration N + 1 0 (k = T3 + 1 is R118 (k)'s own clause, and N5's L(G) is R117's: no separate DATA);». Parts:
  «states that are not standard (σ off the movers and τ) 0» = REFEREE-2 W-3 (a); «genomes with no fallback 0» = REFEREE-2 D-1 =
  REFEREE AC-L4; the parenthesis = REFEREE AC-L4.

### F-6 (AC-L5 = D-2 required, D-3 recommended): the control clause, one clause in L-2
- New = REFEREE's AC-L5 string (REFEREE-2 accepts it in place of its D-2 string, Add. 1), with REFEREE-2's D-3 insertion «;
  e-priorities ordered by (lev, gate index), as in ref gamma3.build» before «)»: «control, five Ξ-cyclic genomes rd2_d3, rd2_d4, rd3_d3,
  rf_d4, RS2 (59 states; the same counts on IDEAL-CYC and along N5′-xi on Γ3; e-priorities ordered by (lev, gate index), as in ref
  gamma3.build): σ̄ off the β-face in 121 (state, gate) pairs, C 15, R 25».
- Sources of the counts: lemma81.py rgen (IDEAL-CYC, out/lemma81_cyclic_control.out: «states 59 notbeta 121 nonstrict 121 C 15 R 25»)
  and pacyc81.py (Γ3, out/pacyc81_cyclic_control.out, same 59 / 121 / 15 / 25); D-2's tool names are here and in check81.sh.
- D-3: R104 fixes only «e of even priority above every β». REFEREE-2 32 measures 111, 15, 20 on 51 states under gate-index order; the
  acyclic counts are 0 under both orders, and no lemma depends on the order.

### F-7 (AC-L1, AC-L2, AC-L3 required: line; N-1 recommended: packet only)
- AC-L1, AC-L2, AC-L3 (form A) are REFEREE's new strings verbatim in L-2.
- N-1 is applied to the packet text only, so that AC-L1's string stays byte-exact in the line (both touch «the order ⊴ and σ̄ of R118
  [VJ]»). Packet §0, R118 bullet: after «by a fixed deterministic rule»;» add «optimal = pointwise optimal (RESULTS R57 (b), 1E-N3, as read in R104: «S1's σ̄,
  and τ̄ on the dual game, are pointwise optima»);». §1 notation: «every v (R118 [VJ]: the order of VJ00 §4.2, Friedmann §3).» gets the same source. The quote occurs verbatim in trunk
  docs/RESULTS.md (R104, l. 9864; asserted by mkL2.py). R21 (a) is not added (optional).

### F-8 (D-4, recommended): output for «2 more after the first fallback»
- Old (§4): «(DATA: 2 more on every genome of §6, but no bound)» New: «(DATA: 2 more on every genome of §6, but no bound; fix1/pacyc81t*.out: 2 on 300 of 300 genomes of A,
  4 of 4 of B, 5 of 5 of the control)».

### F-9 (AC-5, AC-6, optional, taken)
- AC-5, §1. Old: «is the k-th pass of SPEC S4,» New: «is the k-th iteration of SPEC S4 (one pass with Iσ ∪ Iτ ≠ ∅),».
- AC-6, §3, after «By R118 (d) BR-SEG it has at most N steps: T_CYC ≤ N. ∎» add: «Any start mover state is covered: the run from σ_0 is the run of IDEAL-CYC(G′) with G′ = G with its
  start replaced by σ_0; Γ(G′) = Γ(G), since the start enters no priority of Γ, and G′ is Ξ-acyclic.»

### Line L-2
docs/si/P-ACYC-line-L2.txt: sha1 3a3096a45df6ca22e8099ca4e1a9ac1779c1321e, 2741 B = L-1 with five replacements (AC-L1; AC-L2; AC-L3; W-3 (a) + D-1 ⊃ AC-L4 as one;
AC-L5 = D-2, + D-3), built by fix1/mkL2.py, which asserts each Old string once in L-1 and every count against fix1/ and out/ outputs.
It differs from REFEREE's predicted c8ed32a8… (2,638 B) because REFEREE-2's items touch the same clauses (Lead 01:39Z: expected).
LC-1 / W-1, AC-2, AC-3 / W-2, AC-4, D-4, AC-5, AC-6 change packet text only.
