# N5-ARV (box 87): XI-CH-POLY via the Ackermann-Röglin-Vöcking rank trick. ARV's template opened and stated; N5's analogue is the k-term signed prefix of Ξ's path set (PREFIX-MON, lane-PROVED: a monotone level with ≤ (2n+1)^k values), giving LEVEL-RED: XI-CH-POLY ⇐ DEEP_k-POLY for any fixed k. Both quadratic families (latew, fx) have depth ≤ 3 (fully ranked); constant depth is DEAD (switchbestexp_N, depth 3N + 3). The analogy breaks at ARV's 1-1 exchange (Lemma 4)
L-NEW successor 38 (Opus 5.5), D14 / D18, Lead reading L40. Lead 2026-10-30 13:34Z: «BOX 87 = XI-CH-POLY / P*-POLY via the ARV rank trick
(D18: congestion games / matroid optimisation × parity games): (1) Open ARV Thm 3's proof yourself and state the template … (2) Find N5's
analogue … Say exactly where the analogy breaks, if it does. (3) Test … on your corpus AND on mkrw LATE=1 … and fx_K8_m32.» Written
2026-10-30 13:40Z-14:20Z (date -u). Working note, unrefereed. Labels: PROVED (lane) / DEAD / CONJECTURE / DATA / READING. Not a TARGET.md
claim. G-N5-TIME OPEN.

## 0. Sources
- [ARV] H. Ackermann, H. Röglin, B. Vöcking, "On the Impact of Combinatorial Structure on Congestion Games", ECCC TR06-067 (full PDF read):
  Definition 2, Theorem 3 with its proof, Lemma 4 with its proof, the remark after Theorem 3, Theorem 7, and the paragraph after
  Theorem 7 ("best responses in matroids can be decomposed into sequences of pairwise exchanges … this 1-1-exchange property is not only
  sufficient but also necessary for fast convergence").
- L-LIT T52 §6 (relayed by the Lead; the pointer only, not cited as a proof). RESULTS R86 (LEN-MONO, P*), R89 (R*-RISE). Boxes 84-86
  (Fact CONVEX, RSTAR-PCH).
- Pins: L-RED experiments/red/rstar/instances/latew_K16_m32.pg + .start (sha1 6d34c161…; l-red 5374e0a5) and experiments/red/free/
  instances/fx_K8_m32.pg + .start (sha1 e995709e…; l-red b656d2a8), read from origin/claude/l-red. The fx family below was regenerated
  from L-RED's own generators (span/mkrw.py K m, then BLK=2 OWNER=0 ABOVE=a free/obsx.py, as in R137 §3); n matches R137's table
  (K 4: m 16 → 130, m 32 → 194).

## 1. ARV's template (Lead step 1)
- Setting: congestion game, n players, m resources, each player's strategies are the bases of a matroid of rank ≤ rk; delays d_r(k).
- Theorem 3 [ARV]: «players reach a Nash equilibrium after at most n²·m·rk(Γ) best responses».
- Proof template, three ingredients.
  - (T1) An exact potential that is a SUM of elementary values: Rosenthal's φ(S) = Σ_r Σ_(i ≤ n_r(S)) d_r(i).
  - (T2) The elementary values come from a FIXED list of at most n·m numbers {d_r(k)}. RANK them (equal values get equal ranks) and replace
    each d_r(k) by its rank d̃_r(k) ≤ n·m.
  - (T3) Lemma 4 [ARV]: a best response that strictly lowers i's delay under d also does so under d̃. Proof: by Schrijver's exchange
    lemma the symmetric difference S*_i Δ S_i has a perfect matching of single-resource exchanges, each with d_r*(·) ≤ d_r(·) and at
    least one strict. Ranking preserves every single comparison, so the sum still drops.
  - Then φ̃ ≤ n·rk·n·m, it is an integer ≥ 0, and it drops by ≥ 1 per best response.
- Why the number of ranks is ≤ n·m: one rank per (resource, load) pair, independent of the delay functions ("Theorem 3 is independent of
  the delay functions"). Theorem 7 [ARV]: outside matroids (no 1-1 exchange) there are exponentially long best-response sequences.

## 2. N5's analogue (Lead step 2)
- Lemma LEX-SIGN (PROVED, lane). For a fixed cycle node c, the [S1-ord] order on path sets above c is the lexicographic order, from the
  highest rank down, on the vector x(P) ∈ {−1, 0, +1}^(ranks) with x_r = +1 if the rank-r vertex is in P with even priority, −1 if it is in
  P with odd priority, 0 if it is absent. Proof: SPEC Q1, «M ◁ N iff r ∈ N and Ω(r) is even, or r ∈ M and Ω(r) is odd», r the top of
  M Δ N. In both cases x_r(N) > x_r(M), and the two vectors agree above r. □
- Lemma PREFIX-MON (PROVED, lane). Write P's signed TERM LIST as its elements in decreasing rank with their signs. Order single terms by
  (r, +) > (r′, +) iff r > r′, every (r, +) > NONE > every (r′, −), and (r, −) < (r′, −) iff r > r′. Let pre_k(P) be the first k terms,
  padded with NONE. Then while λ(Ξ(v)) is fixed, pre_k(P(Ξ_t(v))) is non-decreasing in t (lexicographic on k-tuples), and it takes at most
  (2n + 1)^k values.
  - Proof. Let P ◁ P′ with top differing rank r and d common terms above r. If d ≥ k the prefixes are equal. Otherwise term d + 1 decides.
  - Case x_r(P′) = +1: P′ has (r, +), and P has (r, −), a lower term, or NONE. Each of these is below (r, +).
  - Case x_r(P) = −1, x_r(P′) = 0: P has (r, −), and P′ has a lower term or NONE. Each of these is above (r, −).
  - Ξ(v) is non-decreasing (SPEC Termination). □
- LEVELS. The ARV-style level of v at t is L_k(v, t) := (λ(Ξ_t(v)), pre_k(P(Ξ_t(v)))). There are at most n(2n + 1)^k of them, and L_k
  is rank-monotone inside each λ-block. DEPTH of a path-set change := the number of common terms above the top differing rank. A change
  of depth < k strictly raises pre_k; a change of depth ≥ k leaves pre_k fixed. DEEP_(k,F)(v) counts the latter.
- Theorem LEVEL-RED (PROVED, lane). For every W-run F, vertex v and fixed k:
  PCH_F(v) ≤ n·(2n + 1)^k + DEEP_(k,F)(v), and ΞCH_F(v) ≤ n(n + 1 + PCH_F(v)) (box 86 §3).
  So XI-CH-POLY (and with it R*-POLY, via R89 R*-RISE) follows from DEEP_(k,F)(v) ≤ p(n) for one constant k.
  Proof: λ(Ξ(v)) takes at most n values in the run, so there are ≤ n λ-blocks. In each, the changes of depth < k strictly raise pre_k,
  which has (2n + 1)^k values. □
- Where the analogy breaks (exact).
  - Not at "moving coordinates". ARV's delays are a fixed list. N5's elementary terms are a fixed list too (the vertices' ranks and
    parities never change); only the SET P moves.
  - It breaks at (T3), Lemma 4. ARV's improvement is witnessed by a perfect matching of ONE-FOR-ONE comparisons, so ranking keeps it
    strict. A path-set rise is witnessed by ONE top term against an arbitrary set below it (LEX-SIGN): (r, +) beats any subset of lower
    ranks. A rank-preserving recoding that keeps every such comparison must keep the lexicographic order of depth up to n, and a faithful
    level set then needs (2n + 1)^depth values. This is the 1-to-many exchange, i.e. the absence of [ARV]'s 1-1-exchange property, the
    property whose absence [ARV] Theorem 7 shows allows exponentially long sequences (in congestion games; a reading, not a transfer).
  - So the ARV trick gives exactly a polynomial level set for BOUNDED-DEPTH changes (LEVEL-RED with k constant). The residual DEEP_k is
    the counter part of the lexicographic order (box 86 §4 [FFSS]).

## 3. DATA (Lead step 3)
- Corpus (box87/depth.py, 1132 runs; depth_*.txt): PREFIX-MON 0 violations (k = 1, 2, 3). Depth histogram of path-set changes inside
  W-runs: 0: 27,382; 1: 17,534; 2: 12,787; 3: 13,187; 4: 7,906; 5-9: 9,910; ≥ 10: 5,751 (max 42). Max per (F, v): DEEP_4 42 (fcobs_6, n 163),
  ΞCH 63 (gate_K64_n581).
- The two quadratic families. Every path-set change has depth ≤ 3 (DEEP_4 = 0), so LEVEL-RED with k = 4 covers them completely.
  - latew_K16_m32 (n 482, one W-run): depth ≤ 3, ΞCH ≤ 33, FLIP 1.
  - fx_K8_m32 (n 250): depth ≤ 3, ΞCH ≤ 137, FLIP 9.
  - fx family (BLK 2, m 8): K = 2, 8, 16, 24 → n 70, 154, 266, 378; depth ≤ 3 throughout; ΞCH 11, 41, 81, 121 (= 5K + 1); FLIP 3, 9, 17, 25
    (= K + 1). At K = 4, m = 8, 16, 32: ΞCH 21, 37, 69; FLIP 5 (constant in m).
- DEAD: CONJECTURE SHALLOW-k (all changes of depth < k, k constant).
  - new/box54/out/switchbestexp_N (N = 2..8, n = 25N + 10): max depth 10, 14, 15, 18, 21, 24, 27, i.e. linear in N. DEEP_4 per (F, v) 10, 12,
    13, 15, 17, 19, 21.
  - new/box54/out/hf/counter_symsi_8 (n 82): depth 42, though only 1 change per vertex.
  - The deep changes are real (fcobs_6: 42 of 44 changes of one vertex have depth ≥ 4), but they stay linear.
- DEAD: CONJECTURE FLIP-c (each top-difference rank r is the top of at most c changes per (F, v), c constant). fx family FLIP = K + 1,
  linear in n (n = 14K + 42). Linear, so not a kill of XI-CH-POLY.
- No super-linear ΞCH_F(v) is known (largest ratio in these runs: fx K = 24, ΞCH 121 at n 378, 0.32n; corpus 63 at n 581).

## DONE / FINDINGS / NEEDS
- DONE: experiments/new/box87/depth.py (LEX-SIGN / PREFIX-MON check, depth histogram, DEEP_4, FLIP), run.sh, depth_*.txt (corpus; FLIP
  added after the corpus run, so the FLIP data are from the pins and families above); check.sh section "box 87".
- FINDINGS:
  1. ARV Theorem 3 template (opened): rank a fixed list of ≤ n·m elementary values; Lemma 4's 1-1 exchange keeps every improvement strict.
  2. PROVED (lane) LEX-SIGN and PREFIX-MON: the k-term signed prefix of Ξ's path set is a monotone level with ≤ (2n + 1)^k values per
     cycle node.
  3. PROVED (lane) Theorem LEVEL-RED: PCH_F(v) ≤ n(2n + 1)^k + DEEP_(k,F)(v). XI-CH-POLY (hence R*-POLY) ⇐ DEEP_k-POLY for one constant k.
  4. DATA: both quadratic families (latew_K16_m32, fx_K_m) have depth ≤ 3, so the ARV-type levels account for all their Ξ-changes.
  5. DEAD: SHALLOW-k (switchbestexp_N depth 3N + 3; counter_symsi_8 depth 42) and FLIP-c (fx: K + 1). Exact break: [ARV] Lemma 4's 1-1
     exchange fails for the lexicographic path-set order (1-to-many). CONJECTURE XI-CH-POLY OPEN (max ΞCH 0.32n).
- NEEDS: none from the owner. Lead: the adversary target that would matter is DEEP_4 per (F, v) super-linear (now 42 = 0.26n at
  fcobs_6). L-RED R139 can read depth.py's DEEP_4 directly.
