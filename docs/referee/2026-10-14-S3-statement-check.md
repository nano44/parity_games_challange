# Referee report: S3 statement (diagonal W(n), S(n); T3-neg, T3-pos, L4, H1), L-STRUCT ef95a93

Referee: REFEREE. Date: 2026-10-15. Routed by the Lead 2026-10-14 20:27Z. Source: claude/l-struct ef95a93,
docs/struct/S3-statement.md, with S1 (D1–D5, Lemmas 1–3), S2 and my earlier reports (C1: 762c598; S2: d96b686,
92846bf).

## Verdict: CHANGES (well-posed and correctly conditioned; six precision findings, one false sentence in §3)

## (1) Well-posedness of the diagonal (D6)
- Alphabet. A TARGET game with n vertices has pr : V → {0..n} (TARGET §1), letters pr+2 ∈ {2..n+2} under S1's
  mapping; subtracting 2 is a parity- and order-preserving bijection onto {0..n}, so "weak separator for V-graphs over
  the letters a TARGET game can have" = weak separator over {0..n} in convention V. With 0 neutral (CFGO Thm 6.2: for
  max-parity a word with finitely many non-zero letters has limsup 0, even; otherwise the limsup of its projection),
  S1 Lemma 2(b) gives w^V(n, {0..n}) = w^V(n, n) and the same for s. So W(n) := w^V(n,n), S(n) := s^V(n,n) is
  exactly the quantity my S2 finding 3 asked for (not w^V(n, n+2)). ✓
- Lemma 2(b) in convention V needs its own one-line proof, which S1 does not give and my S2 repair (a self-loop
  labelled 2) does not supply, since in V a loop at x carries pr(x). Proof: contract 0-vertices by adding, for every
  path x → u1 → … → uk → y with all u_i labelled 0 and pr(x), pr(y) ≠ 0, the edge (x, y); its letter is pr(x), so the
  result is vertex-labelled, has ≤ n vertices, and the same cycle maxima except for 0-only cycles (even, absent in odd
  graphs). For an even path that ends in a 0-only cycle (word u·0^ω), at least one 0-vertex was removed, so add a fresh
  vertex z labelled 2 with edges x → z and z → z: no new cycle through x, u·2^ω is a word of an even V-graph with ≤ n
  vertices, so a Σ_n-separator does not reach ⊥ on u. Needs n ≥ 2; n = 1 is checked directly (W(1) = S(1) = 1 below).
  Finding 1: write this into S1 Lemma 2(b) (V version) or S3 D6.
- Minima exist (S1 F1). W(n) ≤ S(n) ≤ s^E(n,n). ✓

## (2) The two algorithm consequences
- Lower bound (product class). An algorithm of class (i)–(iii) (my S2 §3(c): A deterministic safety automaton depending
  only on (n,d); decision by solving G ⊲ A from (v, q0); time at least the product size) that is correct on all TARGET
  games with ≤ n vertices has |A| ≥ W(n): correctness on the all-Odd game built from an even V-graph forces (W1), and
  on the all-Even game built from an odd V-graph forces (W2), both over the letters {2..n+2} (S2 §3(b)); then D6 and
  Lemma 2(b). Running time ≥ n·|A| ≥ n·W(n) by (iii). ✓ as stated.
- Upper bound. A deterministic weak (n,n)-separator A of convention V, computable in time t(n): extend by 0-loops and
  shift letters (Lemma 2(b), V version), apply S1 Lemma 1 (its proof uses only the graphs arising from the game, whose
  letters are in {2..n+2}, so a separator for those letters suffices), build G ⊲ A with n·|A| vertices and m·|A|
  edges in time O((n+m)·|A|), solve the safety game in linear time (attractor computation; CFGO Thm 2.5 cited by S1
  F4's chain), read off W_E = {v : (v, q0) winning}. Total O(t(n) + (n+m)·|A|). ✓ Regions, yes.
  Finding 2: "positional strategies follow from the safety strategy" is not right as stated: a positional strategy in
  G ⊲ A projects to a strategy with memory |A| in G, not a positional one. Positional strategies come from the region
  oracle at polynomially many calls (TARGET §3, D2), which the gauntlet requires anyway; say that.
- Exact class covered by the lower bound: (i)–(iii) above; excluded: non-deterministic/GFG automata, automata that
  depend on G, product solving below product size, non-product algorithms. S3 cites (i)–(iii) correctly. ✓

## (3) What is conditional on what
- T3-neg (W = S) alone: the product class is bounded below by n·S(n); a barrier for TARGET needs L4 (S(n)
  super-polynomial). S3 says exactly this. ✓
- T3-pos (polynomial W with a construction) ⇒ an algorithm meeting TARGET §2 via (2); independent of L4. ✓
- Finding 3: S3 §2 calls T3-neg and T3-pos "mutually exclusive". They are exclusive only given L4: if S(n) were
  polynomial, W = S and W polynomial would both hold (and strong V-separators would already give a product algorithm).
  State "exclusive under L4". T3-mid is the remaining case under L4.
- L4: open, correctly described: CDFJLP Thm 5.1 is E-only (its G_t uses parallel self-loops, my S2 §2); s^V ≤ s^E
  and s^V(4,4) = 7 < 8 = s^E(4,4) (table; my n = 4 run pending below). The citation to Parys–Wiącek in BARRIERS.md B1
  I have not checked (L-LIT's file). ✓ as a statement.
- H1 (saturation in d): well-posed (D(n), F(n) defined); correctly marked non-algorithmic; F(n) ≥ W(n) ✓.
  Finding 4: the evidence line attributes "s^V(2,2h) = h+1 → ∞" to my S2 §0; what I showed is s^E(2,2h) = h+1 (CFGO,
  universal trees) and s^V(2,2h) = h+1 only for h ≤ 4 (SAT); "→ ∞" for V is unproven. Also the list for d = 2..12
  has eleven entries while the text says d = 11 was not run.

## (4) Diagonal values, my own tools (docs/referee/scratch/wsepsat.py over maximal V-graphs by brute force, every SAT
answer re-checked against all graphs by wsepref.py)
| n | W(n) = w^V(n,n) | S(n) = s^V(n,n) | my evidence |
| --- | --- | --- | --- |
| 1 | 1 | 1 | k = 1 SAT (δ(0,1) = ⊥; the only graph is the odd loop) |
| 2 | 2 | 2 | weak k=1 UNSAT, k=2 SAT; strong k=1 UNSAT, k=2 SAT |
| 3 | 5 | 5 | weak k=4 UNSAT, k=5 SAT; strong k=4 UNSAT, k=5 SAT |
| 4 | 7 | 7 | strong k=6 UNSAT (683 s), strong k=7 SAT (re-verified over all V-graphs with ≤ 4 vertices; a strong separator is weak, so W(4) ≤ 7); weak k=6 UNSAT (1.67M clauses, 1428 s); hence W(4) = S(4) = 7 |
Matches S3's W = S = 1, 2, 5, 7 for n ≤ 4. ✓ (n = 4 added 2026-10-15 after the background cells finished; the
redundant weak k=7 cell was stopped.)

## (5) Other checks on §3 ("why n = 2 is degenerate")
- "In an even 2-vertex graph no two consecutive letters are odd": right (two consecutive odd letters on vertices u, v
  force an odd loop or the odd-maximum 2-cycle u → v → u, since with two vertices the next vertex is u or v). ✓
- Finding 5: "every word of EvenCycles_{2,d} has each odd letter immediately followed by a larger even letter" is FALSE:
  u labelled 3 with edge u → v, v labelled 2 with a loop, is an even V-graph (its only cycle is the loop 2), and its
  word 3·2^ω has the odd 3 followed by the smaller even 2. The witness of course accepts 3·2^ω (checked). The correct
  statement is: an odd letter is followed by an even letter, and if the path ever returns to the odd vertex the
  intervening even letters include one larger than it. The sentence is heuristic context, not used in a target, but it
  must not stand as written.
- "(9 4 8)^ω is a lasso word of the (2,10) witness that no 2-vertex odd graph realises": checked; the witness has the
  cycle 0 →9 3 →4 1 →8 0, and a closed walk of length 3 on two vertices uses a loop or a 2-cycle whose maximum (4 or 8)
  is even, so no odd 2-vertex E-graph (hence S, V) realises it. ✓

## Findings
1. Lemma 2(b) in convention V needs the contraction-with-predecessor-label proof and the fresh-vertex repair (n ≥ 2).
2. Positional strategies: via the region oracle (TARGET §3), not "from the safety strategy".
3. T3-neg and T3-pos are mutually exclusive only under L4.
4. H1 evidence: s^V(2,2h) = h+1 is verified only for h ≤ 4; the formula and "→ ∞" are for E; fix the d-list count.
5. §3: replace the false "immediately followed by a larger even letter" sentence.
6. Diagonal n = 4 from my tools: W(4) = S(4) = 7, confirmed (table line).

## Gaps
- My SAT encoding is unproven; its answers agree with L-STRUCT's and L-COMP's on every cell all have run.
- Nothing machine-checked; statements only, as S3 says.

## Delta check, L-STRUCT a67bd78 (routed 2026-10-14 20:38Z): OK for R1–R5 as applied; one new finding on §3 M0; one observation on §4b
- S1 Lemma 2(b-V): the contraction-with-predecessor-label proof and the fresh-vertex repair are stated as in my finding 1,
  with n ≥ 2 and n = 1 direct. OK.
- S3 §1 strategies [R2], §2 exclusivity under L4 [R3], §3 H1 evidence [R4] (h ≤ 4 in V by SAT, all h in E by universal
  trees; d-list now consistent), the false n = 2 sentence removed [R5]. OK.
- T3 as restated ("w^V(n,d) = s^V(n,d) for 1 ≤ d ≤ n+1"): well-posed; my cells agree on every (n,d) with d ≤ n+1 that I
  ran: (1,1): 1/1; (2,2): 2/2; (2,3): 3/3 (weak and strong k=2 UNSAT, k=3 SAT); (3,3): 5/5; (3,4): 5/5 (k=4 UNSAT, k=5 SAT
  both); (4,4) strong ≥ 7 (k=6 UNSAT, 683 s), weak and the k=7 cells still running.
- §3 Fact M0: true as written, but loose: n consecutive edges already visit n+1 vertices, so every window of n letters
  (not n+1) of a word of OddCycles_{n,d} contains a factor with odd maximum; the n = 2 instance quoted ("no two
  consecutive odd letters") is the n-letter version, which the n+1 statement does not give. Finding 7 (one word).
- §4b (b): confirmed with my tools: results/automata/weak_V_n3_d3.json is a weak (3,3)-separator (all V-graphs with
  ≤ 3 vertices) and the transitions it traverses on words of even graphs contain an odd cycle (states 1 →3 4 →2 2 →2 3
  →1 1, maximum 3), so "prune the even-used part" cannot be the proof of T3. OK.
- §4b Route R1 (L4): plausible as stated, and the fallback already suffices. Checked against CDFJLP §5 (source): the
  embedding claim uses only (a) a run of A on α_t avoiding rejecting states, which holds whenever α_t is the word of an
  even graph the separator must accept, and (b) the tree decomposition, which comes from strongness alone (Lemma 5.2).
  G_t's vertex v_i emits several distinct out-letters along α_t (the odd letters 2k−1 at every level where ℓ_i is the
  last leaf of a non-first child, the even 2k where it is the first leaf, and the loop 2), so a vertex-labelled
  realisation needs copies. Splitting every v_i into one copy per out-letter (at most d copies), each copy keeping all
  in-edges of v_i and the out-edges of its letter, gives a vertex-labelled graph G'_t with ≤ n·d vertices; it is even
  (every cycle projects to a closed walk of G_t with the same labels) and realises α_t (the path picks the copy whose
  letter comes next). So c ≤ d with no further work, and Lemma 5.1 re-run verbatim gives s^V(n·d, d) ≥
  C(⌊lg n⌋ + d/2 − 1, ⌊lg n⌋), i.e. the bound form S3 writes with c = d (floors and non-divisible n handled by
  monotonicity in n). S3 says this fallback "still yields a super-polynomial bound at d = Θ(n/lg n) but not at d = n":
  that misses S1 Lemma 2(a). s^V is monotone in d, so for the diagonal s^V(n,n) ≥ s^V(n,d) for every even d ≤ n, and
  choosing d = 2⌊√n/2⌋ gives s^V(n,n) ≥ C(⌊lg(n/d)⌋ + d/2 − 1, ⌊lg(n/d)⌋) ≥ ((n/d)/lg(n/d))^{⌊lg(n/d)⌋} = n^{Ω(lg n)}.
  So L4 (s^V(n,n) super-polynomial) follows from the fallback plus monotonicity, with no need for c = O(1); the only
  remaining task is to write the re-run of Lemma 5.1 for V-graphs in full (the referee has not re-derived the claim's
  induction line by line; it is CDFJLP's and depends on α_t only). The exact bound form asked by the Lead: yes, it is
  what Lemma 5.1 gives, with c = d available immediately. Observation 8 (for L-STRUCT; a proof is theirs to write).
- Route R2 (T3): a plan, not checked beyond its stated obstruction, which I confirmed above.
Findings from this delta: 7 (M0 window length). Observation 8 (R1: c = d suffices for L4 via monotonicity in d).
