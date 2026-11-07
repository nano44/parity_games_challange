# R2-P-N5-REACH: second-referee report on packet P-N5-REACH (L-NEW successor 58, box 189)
REFEREE-2 successor 29 (Opus 5.5, D1/D18/D20). Written 2026-11-07 03:0xZ to 03:3xZ (date -u). Independent: docs/referee/ not read for
this packet before this push.

## Object
- claude/l-new 73b3d1fd. Re-hashed, all match the brief: docs/new/P-N5-REACH.md b7bd693744fd… (345 lines); P-N5-REACH-line-L1.txt
  b12ec57aa188… (1 line, 3,105 B, 52 «(» = 52 «)», 0 «|»); box189/reachcheck.py c368b363…, reachcheck.out af50ee34…, gamma3.py
  8758456f…, subdiv.py 63c7ae38…, reach.pins f0fc1ba6…, xcheck.sh eeddd8bb….

## Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §2 | Theorem NO-REACH (a)-(c); (d) | **SIGN** (Opus 5.5, D1) |
| §3 | Γ3(G) (definition) and its size N + 7M + 10 | **SIGN** (Opus 5.5, D1) (N-2: c_X) |
| §4 | Lemma S3-START | **SIGN** (Opus 5.5, D1) |
| §5 | Lemma PAD (a)-(c) | **SIGN** (Opus 5.5, D1) |
| §6 | Lemmas K3, PLAY3, SBAR3, TAU3, ESC3, W3, KEY3 | **SIGN** (Opus 5.5, D1) (N-1 on K3's «every genome») |
| §7 | Theorem REACH3 | **SIGN** (Opus 5.5, D1) |
| §8 | Corollary REAL-IDEAL-S3 (a), (b) (reduction / necessity only) | **SIGN** (Opus 5.5, D1) |
| §9 | DEAD SUBDIV (instances A, B) | **SIGN** (Opus 5.5, D1) (replayed on my engine) |
| line | L-1 | **MATCHES after W-1, W-2** (both required) |
No statement is REFUSED; no gap. N-1..N-4 are notes that do not affect a verdict.

## Premise route (landed RESULTS + SPEC; byte-checked)
- All 38 outer «…» quotes of §1 matched by script against trunk 6ca995ed (docs/RESULTS.md, and docs/new/N5-ssi-global.md, sha1
  66fde9ef = the packet's «66fde9ef…»), whitespace-unwrapped: 34 verbatim; the other 4 are labels or quotes with a marked elision «…»
  («## SPEC (EXACT …)», «N5 (SPEC S1-S5 …)», «maximising (Ξσ(w), w) …; otherwise …», «changes at least one of them …»), each verbatim
  up to the elision (SPEC l. 24, l. 57; RESULTS l. 9864, l. 641). Line numbers spot-checked: R104 l. 9864/9878/9975/9989/10004/10011,
  R57 l. 2915, R36 l. 1723/1730, R15 l. 640, SPEC l. 26/47/48/51/53/54/56/81: all correct.
- [1E-N3], [RULE], [VJ-LOC] are R104's own landed premises, used in R104's forms; [RULE] carries R24 (a), R24 (b) and R103 B through
  R104's premise text (L-1 names them). [TERM] R15 (d) only for termination. No R104 THEOREM used ✓. No docs/lit ✓.

## Proof checks (own re-derivation; LENGTH and INDEX spots re-derived with the padded lengths and indices)
- §0 Fact DUAL: c's parity flips under Ω + 1; reward(G^d) = −reward(Γ) − 1 in both parities; P-tops flip parity; the length rule flips:
  G^d's order is Γ's reversed ✓. Fact X ✓.
- §2 NO-REACH. j = 0 by S3/FIX 1: K0 → K1 (r −5 > −(top + 3)), K1 → K0 (r top + 2 > −5) ✓. Step: K1's loop vs K0: (K0, ∅, 1) vs (K0,
  ∅, 0), c even, shorter better: not improving ✓; K3 via K1: (K0, {K3}, 2), {K3} odd: worse ✓; via K2: Odd's loop bounds Ξσ(K3) to
  reward −p'(K2) < 0 ✓; S4a keeps A(v) = {σ(v)}, S4c touches only Iσ's tails ✓. (d): the only entry to K is β → K0; a cycle outside K
  without an e-vertex is a Ξ-graph cycle ✓; nodes ranked above every β ✓.
- §3 count: pads 4 + 2M + M + M ✓; n3 = N + 7M + 10 ✓; top unchanged (pads Ω ≤ 2) ✓.
- §4 S3-START at every multi-successor vertex: mover (unique Ω-2 pad) ✓; β_g (xt Ω 0 r 0 vs pb Ω 1 r −1) ✓; K0 → pA ✓; K1 → s ✓; K3 →
  K2 (r −3 > −5) ✓; Odd gate (G^d rule: highest odd) → pe ✓; Odd K2 → K2 ✓.
- §5 PAD (a): every cycle through a mover passes a gate whose successors are pads to e or β (Ω ≥ 6); core cycles contain K0, K1, K3 or
  K2's loop (Ω 3); c_X is the only exception ✓. (b), (c) ✓.
- §6.1 K3 (a) values ✓ (eight values recomputed). (b): K0 P-SET {K3} odd → K1 improving ✓; K1 P-SET top K3 odd → q worse ✓; **K3
  LENGTH**: (K1, ∅, 0) vs (K1, ∅, 2), c = K1 odd, longer better for Even → K2 kept ✓ (Γ: 0 vs 1, same direction ✓). (c) REWARD ✓.
  (d) H-plays from K0: node K1 vs node K2, −p'(K2) > −p'(K1) → pA, K0 on no H-cycle ✓.
- §6.2 PLAY3 ✓ (P = β's of the X-chain ∪ {K0, K3}; e_g once for lev ≥ 1).
- §6.3 SBAR3: lev ≥ 1 P-SET top e_g (even) → pe worse for Odd ✓; lev 0 REWARD ✓; **K2 LENGTH**: φ(K2) = (K1, ∅, 2) vs φ(r) = (K1, ∅, 1),
  c odd, longer better for Even → loop not Odd-improving ✓; (ii) R36 (c) on G^d ✓; (iii) both cases ✓.
- §6.4 TAU3: pe_g plays all end at c_W; pβ_g → β → pb → K0 → K1 → q → K0, node K0 (top + 2 > top) ✓.
- §6.5 ESC3: β_g: xt (node c_W, even) vs pb (odd cycle) → strict ✓; β on no H-cycle ✓.
- §6.6 **W3 lengths**: per level x → m → g → pe → e → (next level or c_W) = 5 steps, so W(x) = 5ℓ + 5, m 5ℓ + 4, g 5ℓ + 3, pe 5ℓ + 2,
  e 5ℓ + 1, β_g 5·lev(xt) + 6 ✓; P = ∅ (nothing above c_W on these plays) ✓; β with xt = X: pb → K0 → pA → K3 → K2 loop under τ,
  independent of s ✓. (ii), (iii) ✓ (x ⊕ (c_W, ∅, 5ℓ + 4) = (c_W, ∅, 5ℓ + 5); no corner).
- §6.7 KEY3 (a) ✓ (Ω(β) = 6 + 2·rank + parity: rank order and parity preserved). **(b) INDEX**: the root-first sequence from c_W
  (excluded) to y = m_ℓ is e_0, pe_0, g_0, m_0, x_0, …, e_ℓ, pe_ℓ, g_ℓ, m_ℓ, length 5ℓ + 4 for every option; each block is a function of
  g_i; the first difference is at e_(g_i) vs e_(g'_i), whose indices follow gate indices (unchanged in Γ3: pads appended after) ✓.
- §7 REACH3: the induction, the level induction inside S4a's RULE, step L and maximality ✓. RULE at the stop transition is read for
  σ_new before S4c exactly as in R104's REALIZE (my R2-N5-REALIZE check «IDEAL … = s_L (j = L)») (N-4).
- §8 (a), (b) ✓ (L = 0 trivial). §9 statement and instances ✓ (below).

## Machine checks (own code; outputs in docs/referee-2/R2-P-N5-REACH/)
- **Engine not L-NEW's.** r2reach.py (sha1 8dd52cb4…) builds Γ(G) with MY builder from my R104 review (R2-N5-REALIZE/realize_check.py,
  6c35c530…, written from R104's packet §3.1), adds the §3 pads by my own pad3, computes S3/FIX 1 by my own s3, and runs SPEC S1-S5
  with my lane's state loop on the fleet reference si.py Engine. No box21/n5x, no box189 code.
- **Builder vs pins:** my Γ3 and my S3 start equal box189/inst/REC_d10_tower_mu30_g3.pg/.start and RECT_d11_T59_g3.pg/.start BYTE FOR
  BYTE ✓.
- **REACH3 on all 14 corpus genomes** (r2reach_corpus.out): for each, S3 start = the standard state; states 0..L = the transported
  IDEAL states; transitions 1..L FL (no fallback, τ kept, σ changed, W kept at every vertex); L + 1 a fallback; W(x) = (c_W, ∅, 5 lev + 5)
  at movers; **FL runs = [L(G)] exactly**, L(G) = 9, 15, 13, 11, 13, 24, 59, 33, 35, 44, 48, 17, 25, 31; iterations L + 3, 1 fallback;
  n3 = N + 7M + 10. 0 failures. E.g. REC_d10_tower_mu30: L 35, n 310, FL [35], 38 iterations; RECT_d11_T59: L 59, n 340, FL [59], 62.
- **NO-REACH on the same 14** (Γ from S3): σ(K0) = K1, σ(K1) = K0 at every state; no improving edge out of K0, K1; 1 iteration ✓.
- **Third engine:** L-COMP's experiments/n5-second/n5b.py --mode spec on the two pinned Γ3 games: 38 and 62 iterations, 1 fallback
  each (n5b.out) = my engine ✓.
- **Control** (CTRL=mprio0: all mover pads Ω 0): S3 start not standard, REACH3 fails, FL runs [1] / [2] (r2reach_ctrl.out) ✓.
- **SUBDIV** (my own G^pad from §9's text, my engine; r2reach_subdiv.out): A: G from (σ0, τ0) 1 iteration 1 fallback; G^pad (n 8) from
  S3 1 iteration 0 fallbacks; S3 = transported True; projected states equal True. B: 2 vs 3 iterations (n 17) ✓ = §9.
- **Check blocks** «BOX 189 REACH» and «P-N5-REACH» in an archive of 73b3d1fd: both PASS, exit 0 (blk189.out, 17.6 s).
- Oink cross-check (xcheck.sh): NOT RUN by me (Oink not built here); xcheck.out has 28/28 «OK strategies verified» lines (lane DATA).

## DATA rule (§10, not signed; reachcheck.py read)
- NO-REACH (a), (b): NR-STD, NR-CORE, NR-LAM per state ✓; NR-LAM checks only the cycle node of Ξσ(K0), not the full value (K0, ∅, 0)
  (D-1, wording). (d): NR-BETA per (state, vertex ∉ {K2, K3, c_X}) ✓. S3-START per genome ✓. PAD per (state, vertex ≠ c_X, world), scope
  «pairs that occur» stated ✓. REACH3 per genome (standard states 0..L, FL 1..L, fallback L + 1) ✓. W3 per (state, mover) ✓. Iteration
  histogram, BLIND, SUBDIV-APPROX labelled DATA / CONJECTURE ✓. «No separate DATA» list covers the rest ✓. R440's gen matches its
  description (d ≤ 4, ≤ 3 movers per level, degrees 2-3, IDEAL-ACYC asserted) ✓.

## Notes (no verdict changes)
- N-1: K3 is labelled «every genome» but (b) says «These values hold once SBAR3 gives σ̄(K2) = r», and SBAR3 is IDEAL-ACYC. For every
  genome it holds anyway: K is closed, so K's values depend only on the strategies on K, and Odd's unique best at K2 is r (node K1 vs
  its own loop, node K2: −p'(K1) < −p'(K2)). REACH3 uses K3 only under IDEAL-ACYC.
- N-2: c_X is not defined in the packet or in R104's line; it is R104 packet §3.1's name for «an unused even self-loop of priority 2».
- N-3: §13's priority bound top + 3 ≤ 4M + 9 assumes β-ranks 0..M − 1 (box189/norm.py normalises; the IDEAL run depends only on the
  rank order). Not signed.
- N-4: RULE at transition L + 1 (σ_new before S4c) is used as R104 used it.

## Line L-1 (clause by clause against the packet)
- Premises, NO-REACH, REACH3 (pads, priorities, n, S3-START, PAD, states, FL, fallback, L + 1 iterations), REAL-IDEAL-S3, the DATA
  counts (908 states, 1 iteration, 454 genomes, L 9-59, 28/28) and the NOT-claims match the packet and my replays ✓.
- **W-1 (required).** L-1 puts «S3 can be simulated on every game by subdividing every edge» in guillemets as the DEAD statement; the
  packet's killed statement (§9) is specific (priorities + 4, Ω-coded pads, the run equal state for state and transition for transition,
  fallbacks included), and the quoted words are not in the packet. Replace by: «the statement that, for every game and start pair, the
  game with every priority + 4 and every edge subdivided by an Even pad of priority 2 (Even, start edge), 1 (Odd, start edge) or 0 has
  an N5 run from S3 equal state for state and transition for transition (fallbacks included) to the run of the game from that start pair
  is DEAD».
- **W-2 (required).** L-1 uses «c_X» (NO-REACH clause), which R104's line does not define. Replace «outside {K2, K3, c_X}» by «outside
  K2, K3 and the unused even self-loop of priority 2».

## Findings
- F-1: every statement SIGN; LENGTH spots (K3 (b) at K3, SBAR3 at K2, W3) and the INDEX spot (KEY3 (b)) re-derived on Γ3.
- F-2: independent replay on my own builder + SPEC loop (si.py Engine) and on L-COMP's n5b: FL run = L(G) on all 14 corpus genomes
  (up to L 59, n 340); NO-REACH on all 14; my Γ3 builder equals the lane's pins byte for byte.
- F-3: L-1 MATCHES after W-1, W-2.

## Addendum 1: fix round 1 / L-2 (claude/l-new 571c75c5; REFEREE-2 successor 30, 2026-11-07 03:5xZ by date -u)
- Object (sha1 of the bytes at 571c75c5, equal to the Lead's relay 04:00Z): docs/new/P-N5-REACH-line-L2.txt 4de27b32d5ed…, 3,628 B;
  P-N5-REACH-fixes.md 307651b2779f…, 5,344 B (entry 1); L-1 b12ec57a… unchanged.
- Byte test (own script R2-P-N5-REACH/bt_l2.py, output bt_l2.out): RE-L1, W-1, W-2 old strings each occur exactly once in L-1, new strings
  once in L-2; L-1 with the three replacements == L-2 byte for byte (sha1 4de27b32…, 3,628 B); 1 line, 57 «(» = 57 «)», depth never
  negative, 0 «|», no «c_X» ✓.
- W-1 (old span chosen by L-NEW): my predecessor's W-1 gave the new text from «the statement that, …» to «… is DEAD», replacing the
  guillemet quote that L-1 presented as the DEAD statement. The span «the statement «S3 can be simulated on every game by subdividing every
  edge» is DEAD» is exactly what that new text replaces; the following «as stated (DEAD SUBDIV: …)» stays. This is W-1's intent ✓.
- W-2: «outside K2, K3 and the unused even self-loop of priority 2», verbatim ✓.
- RE-L1 counts, re-run (git archive 571c75c5; reachcheck.py with counters added only, R2-P-N5-REACH/reachcheck_r2.py, runs from
  experiments/new/box189 of that archive; output reachcheck_r2.out; its lane lines are identical to the committed reachcheck.out apart from
  the --approx line, which I did not run). Counter code read (gamma_counts l. 78-96, gamma3_counts l. 98-112):
  - «the β-free P-sets of NO-REACH 0 on 42,880 (state, vertex) pairs»: NR-PAIRS = the 908 states of the Γ runs from S3 × every vertex
    except K2, K3, c_X (all vertices: 45,604). The line's NO-REACH clause is itself stated «at a vertex outside K2, K3 and the unused even
    self-loop of priority 2», so the pairs «of NO-REACH» carry that scope in the line ✓. NR-BETA also counts «cycle node ranked ≤ some β»,
    which is packet §2 (d) exactly (stronger than the line's wording; 0 either way) ✓. All 454 genomes are acyclic (asserted), as (d) needs ✓.
  - «S3-START 0 on 454 genomes» ✓ (one count per genome).
  - **«PAD 0 on 693,030 (state, vertex, world) triples of the S3 runs on Γ3»: the counter skips c_X** (l. 110 «if v == cX: continue»);
    over every vertex the triples are 698,204. Its predicate «cycle node Ω < 3 or pad in P» is packet §5 (b), which is stated for v ≠ c_X
    only (c_X's own cycle node has Ω 2, so the predicate would fire there). The line's PAD clause («no pad is ever a cycle node or in a
    P-set») has no exception and is true at c_X too: my added counter gives 0 pads in the P-set or as cycle node at c_X on its 5,174
    triples, cycle node always c_X. So the number is correct but its set is not the one the line names: a reader counting the line's
    triples gets 698,204. This is the C129 E-1 class (unit / set of a DATA count).
    **W-3 (required, wording; old string occurs once in L-2):** «PAD 0 on 693,030 (state, vertex, world) triples of the S3 runs on Γ3,» →
    «PAD 0 on 693,030 (state, vertex, world) triples of the S3 runs on Γ3 (every vertex but the unused even self-loop of priority 2),»
    (L-2 with W-3: sha1 46c2e5079e47e0dc67993ec184933a21d2f17b5d with its newline, 3,687 B, 1 line, 58 «(» = 58 «)»; own computation.)
  - «both DEAD SUBDIV instances re-run»: the two SUBDIV-DEAD lines (my run: identical; my own r2reach_subdiv.out agrees) ✓.
  - «Corollary REAL-IDEAL-S3 no separate DATA»: packet §10 no-DATA list ✓.
- Entry 1's notes N-1..N-4, D-1 quote my predecessor's items correctly ✓.
- Verdict: entry 1 **CORRECT** for W-1, W-2, RE-L1 as applied; **L-2 MATCHES after W-3** (Opus 5.5, D1). Statement verdicts unchanged
  (all SIGN); W-3 is wording only and changes no count.

## Addendum 2: fix round 2 / L-3 (claude/l-new 727163f0; REFEREE-2 successor 30, 2026-11-07 04:5xZ by date -u)
- Object (sha1 of the bytes at 727163f0, equal to the Lead's relay 04:51Z): docs/new/P-N5-REACH-line-L3.txt adfbb3b82190…, 3,748 B;
  P-N5-REACH-fixes.md 547740887c79…, 7,851 B (entries 1-2); L-2 4de27b32… and the packet b7bd6937… unchanged.
- Byte test (own script R2-P-N5-REACH/bt_l3.py, output bt_l3.out): R1 = my W-3 verbatim, R2 = REFEREE RC-2 (claude/referee cc9f4afd,
  R-P-N5-REACH.md l. 179-180) in the Lead-ruled form «1 (Odd, start edge) or 0 has an N5 run» → «1 (Odd, start edge) or 0, the pads
  indexed after the game's vertices in (a, b) order, has an N5 run». Each old string occurs exactly once in L-2, each new string once in
  L-3; L-2 with R1, R2 == L-3 byte for byte, sha1 adfbb3b8219026b23a80b2081a3c227c35730451, 3,748 B; 1 line, 59 «(» = 59 «)», depth
  never negative, 0 «|», no «c_X» ✓.
- R1 (W-3) meaning: as in Addendum 1 (counted set = every vertex but c_X; reachcheck_r2.out) ✓. It names the same set as REFEREE's RC-1
  («vertex other than the unused loop»), so the Lead's ruling that R1 resolves RC-1 is consistent with both texts ✓.
- R2 (RC-2) meaning:
  - Packet §9 (l. 271-272): «EVERY edge (a, b) subdivided by an Even pad p(a, b) (indices n, n + 1, … in (a, b) order; …)». L-3's «the
    pads indexed after the game's vertices in (a, b) order» states exactly this: indices start at n (after the vertices 0..n−1) and follow
    the (a, b) order ✓. «(a, b) order» is the packet's own phrase; REFEREE's «edge order» is the same order only if edges are listed
    (a, b)-sorted, so the Lead's form is the exact one ✓.
  - subdiv.pad (experiments/new/box189/subdiv.py at 727163f0, l. 13): «E = sorted((a, b) for a in range(n) for b in g.succ[a]); P = {e: n
    + i for i, e in enumerate(E)}»: pad of (a, b) gets index n + (rank of (a, b) in lexicographic order) ✓. So the DEAD instances
    (reachcheck.out SUBDIV-DEAD lines) are runs of the statement as now worded ✓.
  - My predecessor's independent builder (R2-P-N5-REACH/r2reach.py subdiv(), l. 133-137) appends pads in the order a = 0..n−1, b in sc[a];
    in instances A and B every successor list is sorted ([1], [0, 1, 2], [0]; [1, 3, 4], [2, 3], [3, 4], [0, 2, 3], [1, 4]), so this is
    the same (a, b) order, and r2reach_subdiv.out (A: fallbacks 1 vs 0; B: iterations 2 vs 3, projected states differ) is a replay of the
    corrected statement too ✓.
- Entry 2 of the fixes file: read; it applies R1 and R2 as stated and changes no statement, proof, tool, output or instance ✓.
- Verdict: entry 2 **CORRECT**; **L-3 MATCHES** the packet with fixes entries 1-2, in bytes and in meaning (Opus 5.5, D1). Statement
  verdicts unchanged (all SIGN); W-1, W-2, W-3 all met.
