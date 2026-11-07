# Box 76 TROPICAL-WINDOW: a max-plus route to MOVES-2D — DEAD in its window-type and Ξ-DAG forms (the transfer is a SUM, not a MAX)
L-SI successor 41 (Opus 5.5), D14 / D18 / D20; Lead brief BOX 76 (2026-11-07, 12 h). Written 2026-11-07 from 00:20Z (date -u: see
the commit). Labels: PROVED (L-SI 41, lane, unrefereed) / DEAD (instance, machine-replayed) / DATA / CONJECTURE / READING. Not a
TARGET.md claim. Every statement is about the IDEAL model of RESULTS R104's definition only, on acyclic Ξ-graphs; nothing here is a
polynomial bound; MOVES-2D and G-N5-TIME stay OPEN.

## 0. Premises and notation
- LANDED: RESULTS R104 (the IDEAL model's definition only), R105 (ENC, LOCAL, MONO; quoted in P-IDEAL-MOVES §premises), R110 (the
  definition of 𝓛^R_d only), R113 (ALIGN, F0, MOVES «KF_x = F(l − 1) and moves(x) ≤ 1 + F(l − 1)», PAIR-DOUBLE and its tight genome
  dd_d5_F14). Opened: trunk docs/RESULTS.md at 2ccd037b9, items R104-R114 (R113 l. 12152-12393).
- SIGNED, NOT LANDED: packet P-IDEAL-MOVES (L-NEW 57, claude/l-new d86adc86, docs/new/P-IDEAL-MOVES.md, 202 lines; fix round 1 at
  9995f5a2): Lemma AND-GATE (a)-(c), WINDOW-DOUBLE (a), (b) (BURST-2), SEG-WINDOW, Corollary MOVES-EQUIV («μ(d) ≤ T^R(d) ≤ 3 +
  (2d − 2)·μ(d)»), and its notation (π_s(x), PF_x, KF_x, Φ_j, j-b-step, Z, μ). Every use below is marked «(P-IDEAL-MOVES, signed, not
  landed)».
- Lane DATA of others (not landed): L-RED R213 (claude/l-red 9eac6d70: «RISE-2D DEAD», genome keep/rise_d5_R13.json) and R214
  (36d340c7: «DENSE(5,3,10) SAT …, certified: mover 6 moves 10 = 2d times in a 10-step run», genome out/dense_d5_l3_H10.json). Both
  genomes are byte copies in experiments/si/box76/inst/ and are replayed here by an independent simulator (§5).
- New notation (this note). For a mover y: R(y) := #{t ∈ [1, T] : cv_(s_t)(y) > cv_(s_(t−1))(y)} (rises of the current Ξ-value); for an
  option (x, k): R_k(x) := #{t : v_(s_t)(x, k) > v_(s_(t−1))(x, k)}. On 𝓛^R_d, for a level j ≥ 1, a j-WINDOW is a maximal set ω = [t_0, e]
  of consecutive steps such that no step of [t_0 + 1, e] is a j-b-step; its TYPE is τ(ω) := (Φ, E, Rd) with c := c_j(s_(t_0)), Φ :=
  #{x ∈ {2j, 2j + 1} : s_(t_0−1)(x) ≠ c}, E := [s_(t_0−1)(2j) = s_(t_0−1)(2j + 1)], Rd := #{x ∈ {2j, 2j + 1} : s_(t_0−1)(x) ≠ c and
  π_(s_(t_0−1))(x) = c} («ready»). These are the Lead's «window types»: the AND-GATE state (Rd), which option each pair member is on
  relative to c (Φ, E), the SEG-WINDOW boundary datum (the window boundaries are the flips of the pair below).

## 1. What a max-plus certificate can and cannot give (PROVED, elementary; READING of the brief corrected)
- Fact MP-LIN. Let A be a k × k matrix over ℝ ∪ {−∞}, b ∈ ℝ^k, and x_(j+1) ≤ A ⊗ x_j ⊕ b for j ≥ 0 (max-plus: (A ⊗ x)(τ) = max_σ
  (A(τ, σ) + x(σ))). With λ the maximum cycle mean of A and a := max finite entry: max_τ x_j(τ) ≤ max(λ, 0)·j + C(A, b, x_0) with C
  independent of j.
  - Proof. Unrolling, x_j ≤ (A^⊗j ⊗ x_0) ⊕ ⊕_(i<j) (A^⊗i ⊗ b); A^⊗i(τ, σ) is the largest weight of a length-i path σ → τ in the weighted
    digraph of A. Remove cycles from such a path until a simple path (≤ k − 1 edges) remains: each removed cycle of length L has weight
    ≤ λL, so the weight is ≤ λ(i − r) + r·a with r ≤ k − 1 the remaining length. Hence A^⊗i(τ, σ) ≤ λ·i + (k − 1)(a − λ) for λ ≥ 0 (and
    ≤ (k − 1)·max(a, 0) for λ < 0). ∎
  - Consequence (READING for the brief): every finite max-plus recursion over finitely many types gives AT MOST LINEAR growth, with slope
    max(λ, 0); a maximum cycle mean 0 gives a BOUNDED quantity, not a linear one. MOVES-2D's slope 2 per level would be λ = 2. So the
    whole content of the route is the VALIDITY of an additive transfer inequality; the cycle-mean computation is then routine.
- Lemma WINDOW-ONCE (PROVED; R104 definition, R113 ALIGN). On 𝓛^R_d, for a level j ≥ 1 and a j-window ω: c_j(s_t) is constant for t ∈
  ω, and each of 2j, 2j + 1 moves at most once in ω, to c_j.
  - Proof. c_j(s) is a function of the key order of the pair j − 1 under s (R113 notation), which changes between s_(t−1) and s_t exactly
    at the j-b-steps t; none lies in [t_0 + 1, e]. By ALIGN, a member of the pair that moves at t ∈ ω moves to c_j(s_t) = c; after it,
    it is on c, and a second move in ω would again go to c, but a move of a degree-2 mover changes its option. ∎
  - With BURST-2 (P-IDEAL-MOVES WINDOW-DOUBLE (b), signed, not landed: on a window without flips of the pair j − 1 the pair j flips at
    most twice; ω has none in [t_0 + 1, e], and t_0 adds at most one), a j-window contains at most 3 flips of the pair j; DATA (§4) max 2.
    So the key side obeys a BRANCHING (+, ×) recursion: #(j+1)-windows = 1 + F(j), each j-window spawning ≤ 3 of them, not a max-plus one.

## 2. The Ξ side: Lemma ALT-MIN and Lemma HIT (PROVED; premises below)
- Lemma ALT-MIN. Premises: R104 definition; R105 ENC, MONO; AND-GATE (a)-(c) (P-IDEAL-MOVES, signed, not landed). Hypotheses:
  IDEAL-ACYC, any degree elsewhere, x a mover of degree 2, any run; y_k := xt(x, k).
  - (a) #{t : π(x) changes at t to k} ≤ R_k(x), for k = 0, 1.
  - (b) PF_x ≤ 2·min(R_0(x), R_1(x)) + 1.
  - (c) moves(x) ≤ 2 + 2·min(R_0(x), R_1(x)).
  - (d) R_k(x) = R(y_k) if y_k is a mover, and R_k(x) = 0 if y_k = X. (CONST-BRANCH) If an option of x has Ξ-target X, moves(x) ≤ 2.
  - Proof. (a) AND-GATE (c): a change of π(x) to b at t has v(x, b) rising strictly at t; distinct changes are at distinct steps.
    (b) π(x) ∈ {0, 1}, so its changes alternate in value; the numbers of changes to 0 and to 1 differ by at most 1, so PF_x ≤ 2·min + 1,
    and (a). (c) AND-GATE (b): moves(x) ≤ 1 + PF_x. (d) ENC: v(x, k) = ε(x, k) + cv(y_k) (ε(x, k) alone if y_k = X), ε constant. ∎
  - Does NOT claim: a bound on R; anything at degree ≥ 3.
- Lemma HIT. Premises: R104 definition; R105 ENC, MONO, LOCAL. Hypotheses: IDEAL-ACYC, any degree, any width; y a mover; any run.
  Then cv(y) rises strictly at step t iff some mover of the chain of (y, s_(t−1)(y)) under s_(t−1) (y included) moves at t. Hence R(y) =
  #{t : Mv_t meets that chain} ≥ moves(y).
  - Proof. (⇐) Let z be the first mover of the old chain that moves at t. The movers before z keep their options, so the new chain has
    the same prefix up to z, and by ENC cv(y) = (Σ of ε over the prefix) + cv(z) at both s_(t−1) and s_t. s_t(z) ∈ A_(s_(t−1))(z) \
    {s_(t−1)(z)}, so v_(s_(t−1))(z, s_t(z)) > cv_(s_(t−1))(z); and v(z, k) = ε(z, k) + cv(xt(z, k)) is non-decreasing (ENC + MONO), so
    cv_(s_t)(z) ≥ v_(s_(t−1))(z, s_t(z)) > cv_(s_(t−1))(z). (⇒) LOCAL: if no mover of the chain moves, chain and value are unchanged. A
    move of y itself is the case z = y, so R(y) ≥ moves(y). ∎
- The two sides, as composition laws (READING). AND-GATE: moves(x) ≤ 1 + min(KF_x, PF_x). Key side: KF_x = F(l − 1) (R113 MOVES), a
  level recursion that doubles (PAIR-DOUBLE, tight). Ξ side: PF_x ≤ 2 min(R(y_0), R(y_1)) + 1 with R(y) ≤ Σ_(z on chains of y)
  moves(z) (HIT): a SUM over the Ξ-DAG. Each side alone composes by addition/doubling; a tropical (max) composition holds on neither
  (§3). The min in ALT-MIN is the only tropical operation the dynamics provide.

## 3. DEAD items
- DEAD SUM-COUPLE (kills the max-plus transfer in both its level form and its Ξ-DAG form, for every constant c ≤ 5).
  - Statements killed: (LEV-ADD c) «in every run on 𝓛^R_d, a Ξ-target mover of level j ≥ 1 moves at most c times more than the
    maximum of moves over all movers of levels < j»; (DAG-ADD c) «moves(x) ≤ c + max over strict Ξ-descendants y of x of moves(y)».
    These are the scalar max-plus transfers x_(j+1) ≤ x_j + c (one type) that MP-LIN would turn into μ(d) = O(d).
  - Instance: experiments/si/box76/inst/dense_d5_l3_H10.json (sha1 a449d7719000b8f60a3fb41087449c4f79f02abe; byte copy of L-RED's
    claude/l-red experiments/red/r214/out/dense_d5_l3_H10.json, commit 36d340c7, git blob 5cf65870), 𝓛^R_5, Ξ-acyclic, start 1100110110,
    T = 10, moves by mover 0..9 = 1, 1, 3, 3, 4, 4, 10, 3, 1, 2. Mover 6 (level 3, a Ξ-target) moves at every step 1-10; π(6) alternates
    at every step (10101010101); its options' Ξ-targets are 5 and 4 (level 2, 4 moves each); its strict Ξ-descendants {0, 2, 3, 4, 5, 7,
    8, 9} move at most 4 times; levels 0-2 move at most 4 times. moves(6) − 4 = 6 > 5: LEV-ADD c and DAG-ADD c are false for c ≤ 5.
  - Mechanism (the exact obstruction): moves(6) = 10 = moves(4) + moves(5) + 2. The hits alternate: at odd steps 1, 3, 7, 9 mover 5
    (on chain (6, 0)) moves and π(6) turns to 0; at even steps 2, 6, 8, 10 mover 4 (on chain (6, 1)) moves and π(6) turns to 1; at steps
    4, 5 deeper movers (9, 0; 7) hit. ALT-MIN is the right law (2 + 2·min(R(5), R(4)) = 2 + 2·5 = 12 ≥ 10): the two Ξ-children's rises
    INTERLEAVE, so x collects their sum. Meanwhile c_3 alternates every step (the pair 2 flips at every step, SEG-WINDOW (a)), so the key
    side never blocks. A max over the Ξ-children (or over lower levels) cannot see an interleaving of two counts.
  - Checks: experiments/si/box76/dead76.py block SUM-COUPLE (own simulator; with XCHK the run is replayed by L-NEW's box150 Gen,
    identical states).
  - DATA (not a kill): the largest increment of LEV-ADD over our corpus + L-RED's r213/r214 genomes, by d = 2, 3, 4, 5, 6: 1, 2, 4, 6, 2
    (d = 6 sparsely searched). Nothing says the increment is bounded in d.
- DEAD RISE-N (L-RED's kill, recorded here because it is the natural tropical potential). «R(y) ≤ N (= 2d) for every mover» is false:
  experiments/si/box76/inst/rise_d5_R13.json (sha1 a45d7689208be1b66e6107b5452e09b728bb7a18; byte copy of claude/l-red
  experiments/red/r213/keep/rise_d5_R13.json, commit 9eac6d70, «RISE-2D DEAD»), start 1110110001, T 16: R(8) = 13 > 10 (moves(8) = 5).
  This is L-RED R213's RISE-2D kill; it is not new. It means the value-rise potential R, which HIT and ALT-MIN make exact, is not
  linearly bounded, so ALT-MIN alone cannot give MOVES-2D.
- DEAD SPAWN-2 (the key-side window recursion is multiplicative; realised). On dd_d5_F14 (sha1 06f0e5015d09c0f1e03f1b9293ab3cd8483e435b,
  R113's tight genome; byte copy from claude/l-new experiments/new/box152/dd_d5_F14.json), start 1101111110, T 14: F = 2, 3, 6, 14, 7;
  #j-windows for j = 1..4 = 3, 4, 7, 15; F(3) = 2F(2) + 2. Any recursion that sees only key-side window types inherits this factor 2
  per level on window counts; per window the pair moves ≤ 2 (WINDOW-ONCE), and the temporal max-plus graph of window types has maximum
  cycle mean 2 per WINDOW (self-loop on type (2, 1, 0), §4) — not per level. Answer to the brief's step 2: the maximum cycle mean is not
  0; the windows multiply.

## 4. DATA (FROZEN corpus; not to sign)
- Corpus: the 208 𝓛^R_d genome JSONs (d 1-8) under experiments/new/box150..box187 at l-new 9995f5a2d (the frozen P-IDEAL-MOVES corpus;
  stored in experiments/si/box76/corpus_lr.json.gz with git blob sha1s, re-hashed at load), every start for N ≤ 10, the stored start
  otherwise: 63,223 runs, 140,395 steps (= movescheck.py's INFO). Own simulator (tw.py Sim), cross-checked against L-NEW's Gen on every
  run with XCHK (0 mismatches; tw_x run, 2026-11-07 00:12Z).
- Per (d, level): max F(j) d 3: 2, 6, 7; d 4: 2, 6, 10, 8; d 5: 2, 6, 12, 14, 8. Max moves of Ξ-targets d 3: 1, 3, 3; d 4: 1, 3, 7, 4;
  d 5: 1, 3, 6, 7, 9 (tw.out).
- Window types (Φ, E, Rd), counts and maxima (moves of the pair in the window, flips of the pair j in the window, length): (0,1,0)
  54,841 / 0 / 0 / 6; (1,0,0) 66,492 / 1 / 2 / 8; (1,0,1) 63,358 / 1 / 1 / 6; (2,1,0) 35,026 / 2 / 2 / 10; (2,1,1) 55,883 / 2 / 2 /
  10; (2,1,2) 13,354 / 2 / 1 / 6. Temporal max-plus graph: MCM 2 at the self-loop (2,1,0). Spawn: at most 3 child windows per window.
- ALT-MIN (a)-(c), MONO of option values, HIT, moves ≤ R: 0 violations on 577,740 (run, mover) pairs (tw3.out, tw4.out counters TO_k,
  ALT, MOVEALT, MONO_VIOL, RMV, HIT_VIOL). moves(x) − 2·min(R_0, R_1) ≤ 2, attained (tw3.out «mv-2minRk»).
- PF_x ≤ Σ over strict Ξ-descendants of moves: 0 violations (tw2.out «PF-SD» ≤ 0; this is HIT + AND-GATE (c), not stated as a lemma).

## 5. Machine checks
- experiments/si/box76/check76.sh (wired into experiments/si/check.sh): sha1 pins (--strict) of the tools, corpus, instances and
  frozen outputs; tw.py, tw2.py, tw3.py, tw4.py reproduce tw.out … tw4.out byte for byte; the violation counters are 0; dead76.py's
  assertions pass. The Gen cross-check (XCHK) needs L-NEW's box150/check.py and is run by hand (not in verify).

## 6. What remains (OPEN; READING)
- A valid linear certificate must combine the two sides: at a move of x both π(x) (Ξ side, interleaved sums) and c_l (key side,
  doubling) must point the same way (AND-GATE). SUM-COUPLE shows the Ξ side alone sums; SPAWN-2 shows the key side alone doubles; the
  d = 5 witnesses (dense_d5_l3_H10, L-RED's DENSE(5,3,10)) sit at moves = 2d exactly, so the coupling, if it gives anything, must give
  a bound of the form «interleavings of the two Ξ-children's hits that the key side can serve». No finite-type max-plus statement of
  this coupling is proposed here: CONJECTURE MOVES-2D stays OPEN, and this box adds no conjecture.
- Diff against TARGET.md: no statement mentions a parity game, a winning region, an algorithm's running time or a complexity class.
  Every statement is about the step sequence of R104's IDEAL model. None is an M3/M4 claim, a gauntlet step, or a polynomial bound.

## 7. Box 76b (Lead re-aim 2026-11-07 00:38Z: the DBL-O(1) question; written from 00:55Z)
- Context: L-LOWER 3 (relayed by the Lead, UNREPLICATED, files not on claude/l-lower at 00:50Z) reports μ ≥ 13, 17, 21, 29 at d 6-9,
  with μ tracking T; F-profile at d 9: 2 3 8 9 12 13 28 27 7. So the Lead re-aimed the box at the flip profile: can PAIR-DOUBLE's
  equality F(l) = 2F(l − 1) + 2 hold at many consecutive levels? A level l is DOUBLING in a run if it holds there.
- Lemma DBL-EQ (PROVED, lane; premises R113 ALIGN, F0, PAIR-DOUBLE's notation; WINDOW-DOUBLE (a), (b) and its proof's identity
  (P-IDEAL-MOVES, signed, not landed); WINDOW-ONCE §1). G ∈ 𝓛^R_d, 1 ≤ l ≤ d − 1, any run, p := 2l, q := 2l + 1, Φ := Φ_l.
  - (a) Level l is doubling iff all of: Φ(s_0) = 2; Φ(s_T) = 0; Φ(s_(t−1)) = 0 at every l-b-step t; no step moves both p and q; the
    flips of (p, q) are exactly the steps that move p or q.
  - (b) At a doubling level each of p, q moves exactly once in every l-window; so moves(p) = moves(q) = F(l − 1) + 1.
  - (c) At a doubling level γ_l(0) = γ_l(1) =: γ, and in every l-window the first of p, q to move is p iff γ is false; so the order
    of (p, q) is γ while p, q are on one option and ¬γ while they are split, and c_(l+1) takes one fixed value c* while they are
    together and 1 − c* while they are split.
  - Proof. (a) With W = [1, T], WINDOW-DOUBLE's proof gives F(l) ≤ M + B1 (by (a) of that lemma), M ≤ Σ_t #(Mv_t ∩ {p, q}) = Φ(s_0) −
    Φ(s_T) + Σ_(l-b-steps t) (2 − 2Φ(s_(t−1))), and B1 = #{l-b-steps with Φ(s_(t−1)) = 1}; so F(l) ≤ Φ(s_0) − Φ(s_T) + Σ_b h(Φ(s_(t−1)))
    with h(0) = 2, h(1) = 1, h(2) = −2, and Φ(s_0) ≤ 2, Φ(s_T) ≥ 0. F(l) = 2 + 2F(l − 1) iff every inequality is an equality: Φ(s_0) = 2,
    Φ(s_T) = 0, h = 2 at every b-step (Φ = 0, hence B1 = 0), M = Σ #(Mv_t ∩ {p, q}) (no step moves both), and F(l) = M with B1 = 0 (every
    moving step flips, and by WINDOW-DOUBLE (a) a flip without a move needs a b-step with Φ = 1, of which there are none). Conversely
    these conditions make each inequality an equality. (b) Φ = 2 at the start of every l-window (Φ(s_0) = 2 for the first; for a later
    window starting at a b-step t, Φ(s_(t−1)) = 0 and c_l changes at t, so both are off the new c_l), Φ = 0 at its end (the next b-step
    or s_T), and a member of the pair moves only to c_l (ALIGN), so both move in the window, each at most once by WINDOW-ONCE. (c) In a
    window both start on one option i (off c_l), so their order is γ_l(i) (ALIGN (c)); the first mover A goes to 1 − i = c_l, and then
    the order is [s(p) = c_l] = [A = p]; the second mover brings both to 1 − i, order γ_l(1 − i). Both moving steps flip by (a): γ_l(i) ≠
    [A = p] ≠ γ_l(1 − i). Hence γ_l(i) = γ_l(1 − i) and A = p iff ¬γ. c_(l+1) is a function of the order of (p, q) (R113's c_l). ∎
  - Does NOT claim: anything about two consecutive levels; a bound on F.
- CONJECTURE DBL-GAP (lane; DATA): if levels l and l + 1 are both doubling in a run, then F(l − 1) = 0. DATA: 0 counterexamples on the
  frozen corpus (63,223 runs, 4,534 doubling levels) and on 68 L-RED 𝓛^R_d genomes (claude/l-red 242fbd1e3, experiments/red/r213 and
  r214, byte copies in experiments/si/box76/inst/lred/; together 80,058 runs, 5,396 doubling levels). Pairs of consecutive doubling levels
  occur only as F = (0, 2, 6, …) (e.g. NOL0_1_d4_t8 start 00000000, F 0 2 6 5); never 3 in a row. L-LOWER's relayed d 9 profile 2 3 8 9
  12 13 28 27 7 doubles at l = 2 and l = 6 only (consistent; not replayed). DBL-EQ (a)-(c): 0 violations on all 5,396 levels
  (tw5.out, tw5_lred.out counter DBLEQ_VIOL).
- READING: DBL-GAP, even if true, does not give a polynomial bound: F(l) ≤ 2F(l − 1) + 1 still doubles. What decides DBL-O(1) is the
  average deficit 2F(l − 1) + 2 − F(l) per level, i.e. whether ∏ (F(l) + 2)/(F(l − 1) + 2) over d levels is polynomial. DATA (largest
  (F(l) + 2)/(F(l − g) + 2), tw5.out «RATIO»): g = 1: 2 (only from F(l − 1) = 0); g = 2: 4 at d 4, 5 (only from F = 0, 2, 6), 2.25 at d 6;
  g = 3: 5 at d 5 (dd_d5_F14 start 1100000001, F 0 1 4 8 2). L-LOWER's d 9 profile: 30/11 over l = 3..6. The data are too small in d to
  separate «ratio → 1» from a constant ratio > 1. OPEN.

## 8. Box 77 AMBIGUITY (Lead 2026-11-07 00:50Z / 01:12Z; written from 01:20Z): replay, DBL-GAP dead, what the tower needs
- Source note: the Lead's analogy with A. Weber, H. Seidl, «On the degree of ambiguity of finite automata» (TCS 88 (1991) 325-349) was
  NOT opened in this box and is used by NO statement below; any automaton reading here is a READING only.
- REPLAY (DATA, independent). L-LOWER 3's nine genomes claude/l-lower 4d747490 experiments/lower/l3/kill/*.json (byte copies in
  experiments/si/box76/inst/lower/, sha1s = L-LOWER's README) replayed from the stored start by my simulator and by L-NEW's box150 Gen
  (identical states; replay77.py with XCHK). Every (d, T, mover, moves) of the README table is reproduced (replay77.out); so
  CONJECTURE MOVES-2D is DEAD by an independent replay as well (e.g. KILL_M2D_d6_mu13: d 6, T 13, mover 8 moves 13 > 12).
- DEAD DBL-GAP (§7): REC_d10_tower_mu30.json (sha1 cc94dc9c46ef63f7a3a54b536d9d3b38fdee5255), stored start, T 35, F = 2 6 14 30 23 8
  7 6 2 1: levels 1, 2, 3 are all doubling with F(0) = 2. (R113 T-BOUND's per-level bound F(l) ≤ 2^(l+2) − 2 is attained at l = 0..3.)
- Lemma TOWER-NEED (PROVED, lane; DBL-EQ, ALT-MIN, HIT, R113 PATH-RISE): if level l is doubling and f := F(l − 1), then each member x
  of the pair l moves f + 1 times, has P(x) ≥ f + 2, and both Ξ-targets of x are movers (not X) with R ≥ ⌈(f − 1)/2⌉.
  - Proof. moves = f + 1 (DBL-EQ (b)); f + 1 ≤ R(x) ≤ P(x) − 1 (HIT, PATH-RISE); f + 1 ≤ 2 + 2 min_k R(xt(x, k)) (ALT-MIN (c)), and an
    X-target has R = 0, which would give f + 1 ≤ 2, i.e. f ≤ 1; for f ≥ 2 both targets are movers with R ≥ (f − 1)/2. ∎ (For f ≤ 1 the
    statement on targets is vacuous as written; only P(x) ≥ f + 2 is claimed then.)
  - For a tower from level 1 (F(l) = 2^(l+2) − 2, l = 0..h): the pair l needs Ξ-targets with R ≥ 2^l − 1. The crossed choice (both
    targets in the pair l − 1, R ≥ moves = 2^l − 1) meets this exactly: on the Ξ side the crossed ladder is self-sufficient above the
    bottom. With L-LOWER's lane lemma FEEDBACK (b) (docs/lower/L3-families.md §4, 4d747490, NOT landed): 2^(l+1) − 1 ≤ 2l(1 + |E_l|), so
    the upward-target values must change at least (2^(l+1) − 1)/(2l) − 1 times: the «fuel» must grow exponentially in the tower height.
- Diagnosis of REC_d10_tower (DATA, tower77.out, fuel77.out): pairs 3 (movers 6, 7) and the level-4 mover 8 are crossed onto the pair
  below (6: 4, 5; 7: 5, 4; 8: 7, 6) and move 15, 15, 30 = R; pairs 1, 2 take fuel from above (2: 4, 19; 3: 13, 17; 4: 9, 10; 5: 16,
  3). Level 4 is not doubling because its second mover 9 (moves 7) is fuel for mover 4.
- Fact ACYC-SPLIT (PROVED, trivial: Ξ-acyclicity) with its instance: if a mover w is Ξ-reachable from a mover x, no option of w has
  Ξ-target x. Here 6 and 7 Ξ-reach 4 and 4 has an option with Ξ-target 9, so 9 cannot point to 6 or 7: re-pointing both options of 9
  onto (6, 7) or (7, 6) closes the cycle 9 → 6/7 → 4 → 9 (replay77.py asserts it). So in this genome the fourth doubling level needs a fuel mover for the
  pair 2 other than 9, from outside the Ξ-down-closure of the tower pair 3.
- Climb (DATA): climb77.py from REC_d10_tower, 4 seeds × 20,000 moves (re-target, rank/gate swaps, parity, start): F(4) stays at 23 in
  all four; the best run has T 45 at d 10 (inst/climb77_d10_T45.json, sha1 c5302641a4a7c921ed73c9fe012e2ee8d50f69f7, F 2 6 14 30 23 13
  15 7 3 1, Gen-confirmed; max moves of a Ξ-target 15). A local optimum, not a cap.
- READING (the open core): no landed or signed constraint that I can find caps the number of doubling levels: the Ξ side supports a
  crossed tower (TOWER-NEED is met by the pair below), the key side allows doubling at every level (PAIR-DOUBLE). The brakes are
  temporal: TRI / FEEDBACK (L-LOWER, lane) force the lower levels to settle within 2(l + 1) steps after every change of an upward target,
  so a tower of height h needs ≳ 2^h/h fuel events, and ACYC-SPLIT forces the fuel to live outside the tower's Ξ-down-closure. Whether
  a fuel subsystem of size O(h) can itself change value 2^h/h times (a second tower feeding the first, i.e. an ambiguity-type nesting)
  or only polynomially often is the question; it is OPEN. No conjecture added.
- Negative controls (box 76 counters, requested): tw.py env NEG=2 (key-least option ignoring availability) gives MONO_VIOL 226,066, RMV
  150,575, TO_k 86,709, HIT_VIOL 238,546 (tw3_neg2.out, tw4_neg2.out); ALT and MOVEALT stay 0 under NEG=2 and NEG=1, so their controls
  are the tightness counters ALT_TIGHT / MOVEALT_TIGHT (the bounds minus 1): 112,372 / 7,085 > 0 on the real model (tw3.out). NEG=1
  (key-greatest available) leaves every Ξ-side counter at 0 (tw3_neg1.out): ALT-MIN and HIT do not depend on the key rule, as their
  proofs say.

## 9. Box 77, second pass (Lead 01:46Z: make fuel economy quantitative; S(h) := least d with h consecutive doubling levels)
- Lemma FUEL-NEED (PROVED, lane, CONDITIONAL on L-LOWER's lane lemma FEEDBACK (b), docs/lower/L3-families.md §4 at 4d747490, not
  landed, not refereed; other premises: DBL-EQ (b) §7, R105 MONO, HIT §2, R113 PATH-RISE). Hypotheses: G ∈ 𝓛^R_d, Ξ-acyclic, any
  run, level h ≥ 1 doubling, f := F(h − 1); Up_h, E_h as in FEEDBACK (Ξ-targets of upward options of movers of level ≤ h; steps at
  which the current value of one of them changes). Then
  - (a) |E_h| ≥ (f + 1)/(2h) − 1, and Σ_(y ∈ Up_h) R(y) ≥ |E_h|;
  - (b) some y ∈ Up_h has P(y) ≥ 1 + ((f + 1)/(2h) − 1)/|Up_h|, with |Up_h| ≤ 4h; hence its Ξ-depth dep(y) (the largest number of
    movers on a Ξ-path from y) is ≥ log2 of that.
  - Proof. (a) DBL-EQ (b): a member of the pair h moves f + 1 times; FEEDBACK (b): at most 2h(1 + |E_h|). By MONO a change of cv(y) is a
    rise, so each t ∈ E_h is a rise step of some y ∈ Up_h. (b) Pigeonhole on (a) and PATH-RISE R(y) ≤ P(y) − 1; P(y) ≤ 2^dep(y) by
    induction along the acyclic Ξ-graph (two options per mover, X counts 1). |Up_h| ≤ 2 options × 2 movers × h levels. ∎
  - For a tower from level 1 with F(0) = 2 (f = 2^(h+1) − 2): some fuel target has P ≥ 2^(h+1)/(8h²) roughly, i.e. Ξ-depth ≥ h − 2 log2 h
    − 3. DATA (REC_d10_tower, h = 1, 2, 3): Σ R over Up_h = 17, 40, 40 against needs 0.5, 0.75, 1.5; max P over Up_h = 91. The bound is
    asymptotic and weak at small h.
- What this does and does not force on S(h) (READING; the answer to task (1)):
  - FORCED: a deep fuel target (Ξ-depth ≥ h − O(log h)), and (ACYC-SPLIT) it cannot Ξ-reach the movers it fuels. Movers reached by
    upward options need not be outside the tower (REC_d10_tower: mover 2 (level 1) has the tower mover 4 (level 2) as an upward target);
    only acyclicity separates them.
  - NOT FORCED by anything landed (R104-R114), signed (P-IDEAL-MOVES) or lane-proved here or in L-LOWER's §2-§4: a fuel block of size
    ≥ 2·S(h − 1), or a fuel that is itself a doubling tower. FUEL-NEED needs only Ξ-paths (counting), which a crossed block of
    h − O(log h) levels provides; whether such a block's values actually RISE that often depends on its key side (pass-through flips
    with Φ = 1, WINDOW-DOUBLE (a)) and on AND-GATE timing, which no statement here bounds.
  - So the best LOWER bound I can prove is S(h) ≥ h + 1 (trivial: h doubling levels above level 0). No constraint I know forces S(h)
    super-polynomial; equivalently, nothing proved here or landed rules out T^R(d) ≥ 2^(Ω(d^c)). CONJECTURE: none.
- Construction proposal for L-LOWER (READING; via the Lead): a MUTUAL-FEEDBACK genome. Tower T on levels 1..h (crossed above the bottom,
  as in REC_d10_tower levels 3-4); fuel block C on levels h + 1..h + m, each C pair crossed onto the C pair below (a Ξ-counter, P
  doubling per level), the bottom C pair to X; the upward options of the tower's pairs 1, 2 target the TOP of C (ACYC-SPLIT holds: C
  never points into T). C's keys are driven by the tower top's F(h) through pass-through flips (Φ = 1 at b-steps). If C's values rise
  ~2^h/h times with m = O(h), then S(h) = O(h) and T^R(d) = 2^(Ω(d)). The measurable obstruction to watch: the decay of F above the tower
  (REC_d10_tower: F = 30 at level 3, then 23, 8, 7, 6, 2, 1), i.e. whether pass-through flips can carry F(h) into C.

## 10. Box 77, third pass (Lead 02:08Z: PASS-THROUGH DECAY): flip counts do not decay; the candidate decay lemma is DEAD
- Lemma PASS-FREEZE (PROVED, lane; premises R113 ALIGN (c), R113's definition of c_l; AND-GATE (a) (P-IDEAL-MOVES, signed, not landed)
  for the sufficient condition). G ∈ 𝓛^R_d, 1 ≤ l ≤ d − 2, any run. If neither member of the pair l + 1 moves in the run and they start
  on different options, then F(l + 1) = F(l). A sufficient condition for «never moves»: for each member x, π_s(x) = s_0(x) in every
  state of the run (e.g. both options of x have Ξ-target X and the start option has the larger ε).
  - Proof. The members keep distinct options, so by ALIGN (c) the order of their keys under s is [s(2l + 2) = c_(l+1)(s)], with s(2l + 2)
    constant; c_(l+1)(s) is the key order of the pair l, which changes exactly at the flips of the pair l. So the pair l + 1 flips
    exactly at the flips of the pair l. Sufficient condition: by AND-GATE (a) x moves at t only if s_(t−1)(x) ≠ π_(s_(t−1))(x); with π =
    s_0(x) and x never moving, s_(t−1)(x) = s_0(x) = π, by induction on t. With Ξ-targets X the values are the constants ε. ∎
- DEAD (the Lead's candidate decay «F(l + 1) ≤ F(l) − c unless the level l + 1 has upward fuel», every c ≥ 1, also above a doubling
  level): instance experiments/si/box76/inst/passfreeze77_d5.json (built by append77.py from L-NEW's climbR_d4_s6, l-new 9995f5a2
  experiments/new/box180/out/climbR_d4_s6.json, start 11011111 + a frozen top pair, stored start 1101111101): T 10, F = 2 2 2 6 6.
  Level 3 is doubling (6 = 2·2 + 2); the level-4 pair never moves, has no upward option (top level), and F(4) = F(3) = 6. The lower
  levels' states are identical to the base run (append77.py asserts it).
  - Same construction on REC_d10_tower_mu30 (inst/passfreeze77_tower_d11.json): F(10) = F(9) = 1, the lower run unchanged (DATA).
- Experiment (DATA, freeze77.py): freezing an untargeted pair (6, 7) directly above the doubling level 2 of REC_d12_mu42 / REC_d11_mu40
  (both options to X, start option preferred, start split) does NOT preserve the run: T 48 → 2 or 6, T 44 → 4; the doubling disappears.
  The pair's moves fed the upper levels' keys, whose moves are the lower levels' upward fuel (Ξ-values via upward options). So what
  «decays» in L-LOWER's genomes is fuel activity, not the flip count.
- READING (consequence for S(h)): a cap on doubling levels cannot come from flip counts alone. Keys pass through frozen pairs losslessly
  (PASS-FREEZE); the scarce resource is Ξ-value change of the fuel (FUEL-NEED), whose movers must also obey AND-GATE (π = c at the
  move). The quantity to bound is the number of rises of the fuel targets per unit of key activity reaching them. OPEN; no conjecture.

## 11. Box 77, fourth pass (Lead 02:50Z: FUEL-RECURSION over Ξ-down-closures)
- Target (Lead): for a set D of movers closed downward and U the upward-fuel targets of D: (i) moves(D) ≤ g(levels(D))·(1 + R(U)); (ii)
  R(U) ≤ moves of the movers on U's chains; (iii) those movers lie outside D (ACYC-SPLIT); iterate.
- (i) holds with a POLYNOMIAL g (PROVED, lane, conditional on FEEDBACK (b), L-LOWER lane, not landed): for D_l := the movers of levels
  ≤ l and E_l as in FEEDBACK, Σ_(x ∈ D_l) moves(x) ≤ 2 + 2l·2l·(1 + |E_l|) ≤ 4l(l + 1)(1 + |E_l|). Proof: level 0 movers move ≤ 1 (R113
  F0); a mover of level j, 1 ≤ j ≤ l, moves ≤ 2j(1 + |E_j|) by FEEDBACK (b), and E_j ⊆ E_l (Up_j ⊆ Up_l). ∎ So g is not 2^levels; the
  exponential, if any, must come from |E_l|.
- (ii) holds: |E_l| ≤ Σ_(y ∈ U_l) R(y) (MONO) and R(y) = #{t : Mv_t meets y's old chain} (HIT), so |E_l| ≤ |U_l|·#{t : some mover on a
  chain of U_l moves}, |U_l| ≤ 4(l + 1). (PROVED, lane.)
- (iii) is FALSE: DEAD «the movers on the chains of the fuel targets of D_l lie outside D_l» (RE-ENTRY), instances (reentry77.py,
  static Ξ-graph; reentry77.out):
  - REC_d10_tower_mu30 (sha1 cc94dc9c…), l = 1..4: the fuel target 11 (level 5) has an option with Ξ-target 3 (level 1): 11 → 3; l = 5,
    6: 16 → 14 → 3.
  - KILL_M2D_d6_mu13 (sha1 5301c716…), l = 1: 5 → 3 (5 is level 2, a fuel target of level 1; 3 is level 1); l = 2: 8 → 7 → 2.
  - ACYC-SPLIT only forbids reaching the movers that point to the fuel target (and their Ξ-ancestors), not the rest of D.
- And even where (iii) holds (no re-entry), the iteration does not close: the movers on U_l's chains are at levels > l, and their keys
  read the levels ≤ l (keys depend on all lower levels; PASS-FREEZE shows flips pass up losslessly), so their moves are bounded only in
  terms of D_l's activity again. The ingredients give T ≤ N(1 + |E|) (FEEDBACK (a)) with |E| ≤ |Up|·T: circular. No product over nested
  closures follows, so no polynomial bound and no 2^Ω(d) lower bound follow from these ingredients.
- READING (the structural answer for this model, as far as the current lemmas go): the coupling is two-way — Ξ-fuel goes upward-then-
  back-down (re-entry allowed), keys go upward losslessly — so there is no one-way interface between level blocks along which a nested
  recursion could run. A recursion needs a quantity that an upper block can receive from a lower one only in bounded amounts per unit of
  its own activity; neither flips (PASS-FREEZE) nor fuel chains (RE-ENTRY) are such a quantity. OPEN; no conjecture.

## 12. Box 78 (Lead 03:13Z: RE-ENTRANT fuel loop; interface quantity)
- Coordinated rewire (DATA): in REC_d10_tower_mu30, re-pointing mover 4's option 0 (fuel 9) to any other legal target and mover 9 onto
  (6, 7) / (7, 6), over starts and parities of 9, collapses the run (best F = 0 2 2 6 9 4 1 1 0 0): the tower's fuel is holistic.
- |E_l| saturates (DATA, fuelE78.out): on all ten records |E_l| ≥ 0.77·T for l ≥ 2 (e.g. REC_d12_mu42: 48 of T = 48), so FUEL (i)
  (§11) carries no information beyond T there: the fuel changes at almost every step.
- Landed potentials as an interface (DATA, pot78.out, rank78.out): none bounds fuel changes per unit of lower activity.
  - R105 RANK: the maximum RANK (π a Kahn order) grows with d on the records: 3 (d 6), 4-6 (d 7-10), 7 (d 11, 12); RANK-BOUND then gives
    Σ_(j ≤ 7) C(N, j) − 1, not a fixed polynomial.
  - R114 PHIK-DESCENT: Φ_K(s_0) is near its exponential ceiling (REC_d10_tower: 3,914 of 2^(d+2) − 2d − 4 = 4,072); R105 EXACT-ENERGY:
    E(s_0) ≈ 0.72·(2^N − 1). Both fall by ≥ 1 per step (checked), with exponential slack; both are global, not per level block.
- Searches (DATA, box78/climb78.py; logs box78/runs/): simulated annealing, re-entrant Ξ-targets allowed (any acyclic re-target),
  smooth score Σ_(l ≤ 4) min(F(l), 2^(l+2) − 2) + T/100, TEMP0 3, 1,500,000 moves per seed: seeds 11-13 from REC_d10_tower_mu30 + 2
  frozen top pairs (d 12), seeds 14-15 from climb77_d10_T45. Earlier lexicographic runs: 5 × 60,000. RESULT: no state better than
  the seeds was found in any run (F(4) stays 23; T stays 35 / 45). The seeds are local optima of this neighbourhood; this is not a cap.
- Outcome of box 78: no height-5 tower (F(4) = 62) was built; the exact obstruction was not identified either. What is measured: the
  fuel changes at almost every step (|E_l| ≈ T), and the tower's fuel cannot be re-routed by local changes (the rewire collapses). OPEN.
