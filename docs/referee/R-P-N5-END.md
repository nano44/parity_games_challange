# R-P-N5-END: first referee report on packet P-N5-END (L-NEW successor 63)
REFEREE successor 29 (Opus 5.5, D15). date -u at writing 2026-11-08T05:58Z. Independent: docs/referee-2/ not read for this packet before this
verdict was written. L-RED 57 R222 (claude/l-red 6f56004c) is context only and is not a signature; I did not use its code.

## 0. Verdicts
| statement | label in packet | verdict |
| --- | --- | --- |
| Lemma E0 (τ fixed, Iτ = ∅) | PROVED, every genome | SIGN |
| Lemma E1 (core frozen until a fallback) + Corollary | PROVED, every genome | SIGN |
| Lemmas E2, E3, E4 (a), (b) | PROVED, every genome | SIGN |
| Lemma TERM-XI | PROVED, every genome | SIGN |
| Theorem ENDGAME-3 (N5′-xi), Theorem ENDGAME-3-N5 (N5) | PROVED, every genome | SIGN |
| Corollary EXACT-L | PROVED, G ∈ IDEAL-ACYC (self-loops count); premise R117 (f) | SIGN (scope note EN-1: SPEC's tie-breaks) |
| Corollary END-T3 | PROVED-CONDITIONAL on REACH3-CYC | SIGN as PROVED-CONDITIONAL on REACH3-CYC (R118 (k), itself PROVED-CONDITIONAL on [REACH-L]) |
| §7-§9 DATA, machine checks, TARGET diff | not to sign | DATA replayed EQUAL (§4); DATA rule §5 |
- No GAP. No required change to the frozen packet's mathematics. Required for the line (there is no line L-1 yet): LN-1..LN-8 (§7).
- Optional (fixes entry if the lane wants): EN-1 (tie-break dependence of EXACT-L, stated), EN-2 (ENDGAME-3-N5 holds for every
  pointwise-optimal S4a choice), EN-3 («bound N5» → «bound N5's iteration count»), EN-4 ((H) wording).
- Ruling asked by the Lead ([OPT] vs [1E-N3] for σ̄): [1E-N3] is the right premise here (§2.2).

## 1. Objects
- claude/l-new 131b4c1c0b98cca2c0b40f6e9cf96c840a4deb25 (ancestor of origin/claude/l-new, checked). docs/new/P-N5-END.md sha1
  5cae845b1da1a1c40b52e73da6edae3d6aadbf29, 22,967 B (git show | sha1sum / wc -c: EQUAL to the brief).
- experiments/new/box195/end.pins: 36 rows, all match at 131b4c1c (sha1sum -c, DOCS/ = ../../../docs/new/).
- check.sh blocks «BOX 195 END» (l. 1020-1028) and «P-N5-END» (l. 1029-1035) read; they test what §8 says.

## 2. Premises (§1)
### 2.1 Quotes, by my own script
- scratch/end_quotes.py (joined-line search, fragments split at «…») on the packet's §1 against 51eb65348 (the packet's trunk;
  ancestor of trunk) and against trunk 8f490d7a: all 33 quotes found, same status on both (end_logs/quotes_51eb.out, quotes_trunk.out).
- Entries checked by hand where the script's «first match» was another entry:
  - [REACH3]: R117 (f), RESULTS l. 13445-13447 (the script's first hit, l. 9959, is R104's Γ(G) version of the same sentence).
    R117 (f)'s proof (l. 13448-13452) says «S4c does not fire … an FL transition» and «At j = L … a fallback». So «FL transitions,
    which are not fallbacks» in EXACT-L's proof is R117's own reading.
  - [R3C]: R118 (k), l. 13704-13712: «PROVED-CONDITIONAL on [REACH-L]»; «T3 is the first state at which no mover has a strictly better
    successor in Γ3;»; «transition T3 + 1 is an S4c fallback.» The packet's «CONDITIONAL there» is accurate.
  - [TAU3]: P-N5-REACH §6.4 l. 202 at trunk; signed for every genome (R118's quote «R117's entry signs S3-START, PAD, K3 and TAU3
    for every genome»). The standard state's τ is pe at every gate and K2 → K2 (P-N5-REACH §3 l. 137-139), i.e. the packet's τ0.
  - [TERM]: R15 (a) l. 631, (c) l. 637.
- All premises are landed RESULTS entries (R15, R57 via R104, R104, R117, R118) or the frozen SPEC / packets those entries land.

### 2.2 Ruling: [1E-N3], not R118 (b)'s [OPT]
- The packet uses σ̄ = S1's output and σ_new = S4a's output inside SPEC runs (N5, and N5′-xi, which changes S4a only). [1E-N3]
  (R57 (b) as landed in R104, quote found at R104 l. 9864 ff.) is about exactly these objects: «S1's σ̄ … are pointwise optima; and
  S4a's σ_new … is a pointwise optimum of that arena».
- R118 (b)'s [OPT] is about IDEAL-CYC's defined σ̄_t, which this packet never uses. (My predecessor's ruling for P-N5-QUIET was the
  reverse case: there σ̄_t was IDEAL-CYC's.)
- R117 (f)'s own proof uses «[1E-N3] P2» for the same S4a step (l. 13448). The packet is consistent with the entry it builds on.

## 3. Proofs, each step re-derived
- §2 facts. (R): β ≥ 6 > K1 = 5 > K2 = 3 > every pad / mover / gate / c_X (Ω ≤ 2); e < c_W = top < K0 = top + 2 < K3 = top + 3
  (top even, so K0 even, K3 odd). (C): core edges match [G3] (pads pA, s, q, r). (S): S3 / FIX 1 gives κ0, β → xt, pe, K2 → K2
  (also checked by machine: my FIX-1 start = builder start on every run, §4). (W): from a gate of a level-ℓ mover, g, pe, e, then per
  level a mover, its m-pad, its gate, pe, e: 5ℓ + 3 steps; no vertex above c_W: (c_W, ∅, 5ℓ + 3). CORRECT.
- (H): σ_new pointwise optimum ⇒ its value at v is W*(v); the cycle node of W*(v) is not v, so the value at v is v ⊕ (value at
  σ_new(v)) = v ⊕ W*(σ_new(v)); hence σ_new(v) ∈ TIE(v). For N5′-xi, [N5XI] picks inside TIE(v). CORRECT. (EN-4: «not its own
  H-cycle node» is read as «the cycle node of W*(v) is not v».)
- E0. Iτ depends on τ only (Ξτ on G^d with τ̄ optimal). [TAU3] gives Iτ = ∅ at τ0. S4b needs Iτ ≠ ∅; S4c changes τ only when
  Iσ = ∅ (FIX 3). Induction. CORRECT.
- E1. Odd at K2 under κ0: r gives node K1 (K1 → s → K1), loop node K2; K1 more relevant odd ⇒ σ̄(K2) = r. Values recomputed:
  K1 (K1, ∅, 0), s (K1, ∅, 1), r (K1, ∅, 1), K2 (K1, ∅, 2), K3 (K1, {K3}, 3), pA (K1, {K3}, 4), K0 (K1, {K0, K3}, 5), q (K1, {K0, K3}, 6).
  (a) K0: K1 vs pA differ by K3 (odd) in pA's set ⇒ K1 better: improving. K1: q's set has {K0, K3}, top K3 odd ⇒ worse. K3: same set,
  node odd, K2 longer (2 > 0) ⇒ K2 better: K1 not improving. (b) H: via pA node K2, via K1 node K1; reward(K2) > reward(K1) for Even;
  K0 on no H-cycle (only q enters K0, A(K1) = {s}); TIE(K0) = {pA}. CORRECT. Corollary: by induction over non-fallback iterations.
- E2. Input κ0 (Corollary), τ0 (E0); Iσ ≠ ∅ ⇒ Even fallback, τ kept (FIX 3); on the core only (K0, K1). CORRECT.
- E3. Under κ1: σ̄(K2) = r (node K1 beats node K2 for Odd). Values recomputed as in the packet. Iσ on the core = {(K1, q)}
  ({K0} even in q's set). H: A(K1) = {s, q}; via q the cycle K1 → q → K0 → K1 has node K0 (largest reward); W*(K1) = (K0, ∅, 2);
  K1 ⊕ W*(s) = (K0, ∅, 4) ≠ W*(K1) ⇒ σ_new(K1) = q (both rules). σ_new ≠ σ ⇒ not a fallback. CORRECT.
- E4 (a). Under κ2: r → K1 → q → K0 → K1 has node K0 ⇒ Odd plays the loop: σ̄(K2) = K2. Core values recomputed. Iσ on the core
  = {(K3, K1)} (reward node K0 vs node K2). β with σ = xt(g): [1E-N3] ⇒ Ξσ(xt) ⊴ value under «pe everywhere», which ends in c_W's
  loop (W); reward(c_W) < reward(K0) = Ξσ(pb_g)'s node ⇒ (β_g, pb_g) ∈ Iσ. H: β_g on no H-cycle (pβ_g its only in-edge, gates play pe in
  H); via pb node K0, via xt node c_W ⇒ σ_new(β_g) = pb_g; K3 on no H-cycle ⇒ σ_new(K3) = K1. CORRECT.
- E4 (b). Under σ* (κ3, every β on pb): from a gate, any Odd deviation to some pβ_h reaches pb_h → K0 → K1 → q → K0 (node K0), worse
  for Odd than c_W; ρ* attains the least value at every gate; at K2 the loop (node K2) beats r (node K0). Movers: all options are
  m-pads to gates of the same mover, value (c_W, ∅, 5ℓ + 4) each: no strict improvement. β: pb (K0, ·) vs xt (c_W, ·): none.
  Core: none (recomputed). Every other Even vertex has one successor. Iσ* = ∅, Iτ = ∅ (E0): S5. CORRECT.
- TERM-XI. E0 ⇒ every iteration has Iσ ≠ ∅ and changes σ; the change is Switch_I for a non-empty unambiguous I ⊆ Iσ (σ_new(v) ∈ A(v);
  the fallback picks one best improving edge per vertex). Iσ is VJ00's improvement set on the full game G (SPEC S1: σ̄ is Odd's optimum
  in G, not in H). R15 (c) ⇒ no σ repeats; finitely many σ. CORRECT.
- ENDGAME-3 / ENDGAME-3-N5. Termination + «no stop under κ0» + «κ changes only at a fallback» ⇒ a first fallback F; E2, E3, E4 ⇒
  exactly F + 2 iterations and no second fallback. Only (H) is used about S4a, so the N5 proof is the same. CORRECT.
- EXACT-L. R117 (f): transitions 1..L non-fallback, L + 1 fallback ⇒ F = L + 1 ⇒ L + 3. CORRECT. Necessity of the self-loop clause:
  SELFL_n3 (my acyclicity test: Ξ self-loops at x0 and x1 count as cycles; L(G) 1 by t3r_sim; N5 total 3 by n5b spec), EQUAL.
- END-T3. [R3C] ⇒ F = T3 + 1 ⇒ T3 + 3 by ENDGAME-3. CORRECT as a conditional.

## 4. Replays with my own code (scratch/; logs scratch/end_logs/)
- Γ3(G): my builder xicyc_replay.build(G, pad=True) (successor 26). S3 start: my FIX-1 code (end_replay.s3_start), equal to the
  builder's start and to n5b's start on every run below (0 differences; 0 priority ties at S3).
- (A) ENDGAME-3 / E0-E4 with MY engine (scratch/end_replay.py on xicyc_vj.VJ; no lane code): modes xi (N5′-xi) and n5w (N5 with S4a =
  a pointwise optimum of H whose ties keep σ(v); NOT SPEC's S1 tie-break). Own generator, families rand, acyc, selfl, deep, wide,
  600 each, seed 2951, plus the 60 genome files of box189/corpus, box189/inst, box191-195/inst: 3,060 runs per mode, 6,120 in all.
  Every counter 0 (e0fail-e4fail, stopfail, finsbar, fintie, nfb, nofb, capped); tally «one fallback, 3 iterations from F» on every
  run. Controls fire: CTRL=1 (k1/k2 swapped) e2fail = e3fail = e4fail = 100 of 100 (both modes); CTRL=2 (τ(K2) = r, σ(K1) = q)
  e0fail 300, nofb 100 (both modes). (end_logs/sweep_own.out)
- (B) EXACT-L and ENDGAME-3-N5 under SPEC's exact tie-breaks: L-COMP's n5b.py --mode spec (an engine that is not L-NEW's), on MY Γ3,
  checked by my code (scratch/end_exactl.py); L(G) by t3r_sim (successor 24's own IDEAL simulator).
  - 14 corpus genomes: all IDEAL-ACYC; F = L + 1 and total L + 3 on every one; L up to 59 (RECT_d11_T59_norm: F 60, 62 iterations,
    EQUAL to the packet). SELFL_n3: F 1, total 3. (end_logs/exactl_files.out)
  - Own generator, 5 families × 300, seed 2952: 1,500 runs, all structure counters 0 (τ constant, one fallback, κ0..κ3 at the right
    states, total F + 2, final β's on pb); 341 IDEAL-ACYC genomes, lfail 0 (L ≤ 3). (end_logs/exactl_n5b.out)
- (C) EXACT-L depends on SPEC's S1 tie-breaks (EN-1). With my n5w (another pointwise-optimal S4a choice): 600 acyc genomes (seed 2951),
  382 with L ≥ 1: EXACT-L fails on all 382 (F = 1: at S3, every mover's options tie in H because Odd follows pe there); the 218 with
  L = 0 hold. ENDGAME-3-N5 still holds on all of them (A). (scratch/end_tiedep.py, end_logs/tiedep.out)
  - Reading: REACH3's induction picks the mover move by [RULE] among TIE(x) = R(x) (R117 (f) proof l. 13449), i.e. by SPEC's tie
    rule. The packet's «N5 (SPEC S1-S5)» includes FIX 1-4, so EXACT-L is not false; but the identity is a property of SPEC's tie-break,
    while ENDGAME-3-N5 is not. D18 «Clearly distinguish proven results from conjectures» favours saying so (EN-1, LN-3).
- (D) The lane's own checks at 131b4c1c: check195.sh re-run in a detached worktree: output byte-identical to check195.out (138 lines,
  2 min 13 s). data/sweep195.out read: 32 sweep rows + 14 corpus rows, every fail counter 0; tally (1, 3) on every row.

## 5. DATA rule on §7, clause by clause
- Unit sentence: CORRECT (runs of N5′-xi / N5 from S3 on Γ3(G); gamma3.build, n5v.step).
- E0 (states), E1 (iterations before F), E2-E4 (a) (iterations F, F + 1, F + 2), E4 (b) (final states): units given. EQUAL to
  sweep195.out. Note: eg195.py's docstring calls e1fail's unit «states before the first fallback»; the count is the same (one input
  state per iteration), and ctrl2 counts it in states (no fallback). The line should use one unit (LN-6).
- «nofb 0, late 0, capped 0»: NO UNIT in the packet. From eg195.py: nofb = runs (cap reached without fallback), late = iterations after
  F + 2 (l. 87), capped = runs. Required in the line (LN-6).
- Sets: «xi 24,000 runs and spec 24,000 runs (8 families × 1,500 × seeds 1951, 1952)»: 16 rows × 1,500 per mode in sweep195.out,
  EQUAL. «+ spec on the 14 R117 corpus genomes»: 14 rows, EQUAL. check195.sh: 8 × 300 (seed 1953) per mode + the pinned genome files:
  EQUAL to the script and to its output.
- EXACT-L «lfail 0 … on 4,297 genomes (4,283 random IDEAL-ACYC ones among the spec sweep, 3,000 of them from acyc, and the 14 corpus
  genomes, L(G) up to 59: RECT_d11_T59_norm, 62 iterations)»: spec rows' acyc column 2,169 (seed 1951) + 2,114 (seed 1952) = 4,283,
  acyc family 2 × 1,500 = 3,000, + 14 = 4,297: EQUAL. «L(G) by L-RED's ideal.traj … record only»: check195.sh runs without LRED, so
  check.sh does NOT re-check lfail (in check195.out every acyc / lfail column is 0, even on the 600 acyc-family runs, because LRED is unset). The line must say «record
  only» or cite this report's replay (§4 (B)) (LN-6). Note: the xi rows also print lfail 0; EXACT-L is about N5, so only spec rows count.
- Witness SELFL_n3 (L 1, total 3): EQUAL (data/selfl195.out; my replay).
- Controls ctrl1 «100 of 100», ctrl2 «e0fail 200, e1fail 200 (states), no fallback»: EQUAL (check195.out; check.sh tests both).
- Independent replay (L-RED R222): cited, not re-run: correctly labelled as L-RED's counter.
- «maxxi» in the outputs is not used by the packet: fine.

## 6. Optional changes (fixes entry; the packet stays frozen)
- EN-1. After EXACT-L or in Scope: «EXACT-L uses SPEC's S1 tie-breaks (through REACH3's [RULE] choice); with another pointwise-optimal
  S4a choice the identity can fail (REFEREE R-P-N5-END §4 (C): F = 1 on 382 of 382 IDEAL-ACYC genomes with L ≥ 1).»
- EN-2. ENDGAME-3-N5 uses only (H), so it holds for every rule whose S4a output is a pointwise optimum of H (my n5w data, §4 (A)).
- EN-3. Consequence l. 190: «a polynomial bound on L(G) would bound N5 on them» → «… would bound N5's iteration count on them» (the
  cost per iteration at bit cost is a separate gauntlet step-4 item).
- EN-4. (H): «not its own H-cycle node» → «the cycle node of W*(v) is not v».

## 7. Line requirements (no line L-1 exists; what I will test L-1 against)
- LN-1. Statements and labels exactly as the «To sign» table: E0-E4, TERM-XI, ENDGAME-3, ENDGAME-3-N5 PROVED (every genome);
  EXACT-L PROVED for «G ∈ IDEAL-ACYC (R104: the Ξ-graph is acyclic; self-loops count as cycles)», premise RESULTS R117 (f); END-T3
  PROVED-CONDITIONAL on REACH3-CYC (RESULTS R118 (k), itself PROVED-CONDITIONAL on [REACH-L]).
- LN-2. Objects: Γ3(G) of RESULTS R117 (n = N + 7M + 10); N5 = SPEC S1-S5 with FIX 1-4; N5′-xi = RESULTS R118's [N5XI]; start S3;
  counted: iterations (SPEC S4). ENDGAME-3's form: «exactly one fallback, at an iteration F ≥ 1, and exactly F + 2 iterations».
- LN-3. EXACT-L's sentence names SPEC's tie-breaks (EN-1 in substance), or says «N5 (SPEC S1-S5 with its FIX 1-4 tie-breaks)».
- LN-4. T3 defined as R118 (k): «the first state at which no mover has a strictly better successor in Γ3».
- LN-5. Premises named: [1E-N3] (RESULTS R57 (b) as landed in R104), RESULTS R15 (c), [TAU3] (RESULTS R117 / P-N5-REACH §6.4),
  RESULTS R117 (f), RESULTS R118 (k). Not R118 (b)'s [OPT].
- LN-6. DATA with a unit for every counter (e0fail states; e1fail one unit; e2fail-e4fail iterations F, F + 1, F + 2; stopfail, finsbar,
  fintie final states; nofb and capped runs; late iterations after F + 2), the sets of §5 (24,000 + 24,000; + 14 corpus spec), EXACT-L
  on spec runs only (4,297 genomes; L ≤ 59; RECT_d11_T59_norm 62 iterations) with «L(G) by L-RED's ideal.traj, record only (not
  re-run by check.sh)», the witness SELFL_n3 (L 1, total 3), and the controls. Every number in the line must appear in a pinned output.
- LN-7. Scope: Γ3(G) only; nothing on F, L(G) (OPEN) or T3; not M3, not M4, not a gauntlet step-4 pass; G-N5-TIME stays OPEN;
  N5′-xi stays a CANDIDATE (D1).
- LN-8. Source note: P-N5-END, docs/new/P-N5-END.md (frozen at claude/l-new 131b4c1c), with its fixes file if any; L-NEW successor 63;
  credit L-RED 56 (conjecture ENDGAME-3, skeleton, family generator).

## 8. Scope sentence and TARGET.md diff
- TARGET.md §2 (M4: polynomial on every parity game), §4 («Polynomial only on a restricted class …» is not M4), §5 step 4. The
  packet claims no bound: an exact endgame on Γ3(G) and an identity between N5's count on {Γ3(G) : G ∈ IDEAL-ACYC} and L(G). Its §9 says
  «Not M3, not M4, not a step-4 pass. G-N5-TIME stays OPEN». CORRECT. The Consequence's «polynomial in n iff L(G) polynomial in N + M»
  holds since N + M ≤ n = N + 7M + 10 ≤ 7(N + M) + 10; it is a statement about iteration counts (EN-3).
- D1: N5 and N5′-xi stay candidates; nothing here moves G-N5-TIME.

## 9. Tools and outputs (committed, docs/referee/scratch/)
- end_replay.py (own N5-w / N5′-xi engine + counters + controls; own genome generator), end_exactl.py (n5b spec on my Γ3, my checks),
  end_tiedep.py, end_quotes.py; logs end_logs/sweep_own.out, exactl_n5b.out, exactl_files.out, tiedep.out, quotes_51eb.out,
  quotes_trunk.out, check195_rerun.diff.

## §C. Fixes entries 1-2 and line L-2 (REFEREE successor 29, Opus 5.5, D15; date -u at writing 2026-11-08T07:53Z)
(The Lead asked for «§8»; §8 above is the TARGET.md diff, so this is §C, in the house form of the other reports.)
- Objects: claude/l-new 2fcee038 (ancestor of origin/claude/l-new, checked).
  - Packet unchanged: 5cae845b…
  - L-1 docs/new/P-N5-END-line-L1.txt: 68a69176…, 5,903 B (l-new a60733b8; SUPERSEDED; not reviewed on its own).
  - L-2 docs/new/P-N5-END-line-L2.txt: sha1 e8a8ac51cc79c9de4000749899e7f0b860eeebe5, 6,988 B, one line, 101 «(» = 101 «)». EQUAL
    to the Lead's check.
- Byte checks:
  - mkl2_195.py re-run at 2fcee038 prints «R1-R16 old once each, applied; sha1 e8a8ac51… 6988 bytes» and leaves the worktree clean.
    It needs trunk c8f42538 in the object store; I fetched trunk first.
  - end.pins: 41 rows, all match.
  - I had no strings of my own for L-1 → L-2 (no line existed at my review). So I test L-2 as a whole against LN-1..LN-8 and the packet.
- Quotes (scratch/end_l2quotes.py, end_logs/l2_quotes.out): all 8 source quotes in L-2 are found verbatim (joined lines) in trunk
  RESULTS / P-N5-XICYC / P-N5-REACH, or in fixes entry 1 (W-1's sentence). The ninth «…», «one fallback, 3 iterations from it», is the
  packet's own tally label (packet §7, once).
- Fixes entry 1 (L-RED 58 R223):
  - W-1: CORRECT. «under the standing SPEC premise 1E-N3» is in R57's heading (RESULTS l. 2893), and R104's (l. 9864) and R117's
    (l. 13362) headings carry 1E-N3 too. E0-E4, (H) and TERM-XI use it, as my §2.2 says. No statement changes.
  - T-1: a tool remark; quotes_end.py now reads every source from trunk. My own quote check (§2.1) already read from git objects.
    CORRECT.
- Fixes entry 2 (my EN-1..EN-4, taken): the texts match §6. CORRECT.
- L-2 against my line requirements (§7):
  - LN-1: PASS. «each PROVED (every genome)» for E0-E4, TERM-XI, ENDGAME-3, ENDGAME-3-N5. EXACT-L is «PROVED for G ∈ IDEAL-ACYC (R104:
    the Ξ-graph is acyclic; self-loops count as cycles; «…»), premise RESULTS R117 (f)». END-T3 is «PROVED-CONDITIONAL on REACH3-CYC,
    RESULTS R118 (k), itself PROVED-CONDITIONAL on [REACH-L]», with R118's condition quoted. The sentence on which R117 rows are signed
    for every genome and which for acyclic Ξ-graphs only is R118 (k)'s own text (RESULTS l. 13707-13709).
  - LN-2: PASS. Γ3(G) of R117 with n = N + 7M + 10; N5 = SPEC S1-S5 with FIX 1-4; N5′-xi = R118's [N5XI]; S3; SPEC S4 iterations;
    ENDGAME-3's form verbatim.
  - LN-3: PASS. EXACT-L names SPEC's tie-breaks and cites my 382 of 382 with commit and output path.
  - LN-4: PASS. T3 as in R118 (k), quoted.
  - LN-5: PASS. [1E-N3] = R57 (b) as landed in R104, R15 (c), [TAU3], R117 (f), R118 (k). «R118 (b)'s [OPT] is not used».
  - LN-6: PASS.
    - Every counter has a unit: e0fail states; e1fail iterations before the first fallback; e2fail-e4fail the iterations F, F + 1,
      F + 2; final states; nofb and capped runs; late iterations after F + 2.
    - The sets of my §5 and the controls (ctrl2 also «nofb 100 (unit: runs)», EQUAL to check195.out).
    - EXACT-L on spec runs only (4,297; 4,283; 3,000; 14; L ≤ 59; RECT 62 iterations), «record only (not re-run by check.sh, which
      leaves LRED unset)».
    - Each number is in sweep195.out / check195.out (pinned) or in my tiedep.out (cited by commit).
  - LN-7: PASS. Bounds none of F, T3, L(G) (OPEN), nothing outside Γ3(G); G-N5-TIME OPEN; CANDIDATE (D1); not M3 / M4 / step 4 /
    TARGET.md claim; TARGET.md §2 and §4 named.
  - LN-8: PASS. Frozen at l-new 131b4c1c, sha1 5cae845b, fixes entries 1-2, L-NEW successors 63-64, credit L-RED 56.
  - EN-3 in the line: PASS («a statement about iteration counts; the cost per iteration at bit cost is a separate gauntlet step-4 item»).
- Optional, not required:
  - EL-1. «their transfer to the Γ3 run (equal runs at exact VJ ties) is NOT proved»: the parenthesis is hard to read. Clearer:
    «(the Γ3 run can differ from the IDEAL-CYC run at exact VJ ties, R118's DATA)», as in P-N5-QUIET's L-2.
  - EL-2. «independent replays, every fail counter 0, … REFEREE 29 R-P-N5-END §4»: true of my §4 (A) and (B). §4 (C) is the
    tie-break observation, which the line cites separately under EXACT-L. Naming «§4 (A), (B)» would be exact.
  - The citation of L-RED 58 R223 item 1 (claude/l-red 143f0b4c, an ancestor of origin/claude/l-red; checked) is L-RED's counter, cited,
    not re-run, and labelled so.
- Verdict:
  - Fixes entries 1-2 CORRECT. L-2 MATCHES the packet with its fixes entries, and meets LN-1..LN-8.
  - All statements stay as in §0: SIGN; END-T3 as PROVED-CONDITIONAL on REACH3-CYC.
