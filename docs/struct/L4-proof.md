# L4: strong separators for vertex-priority games are super-polynomial on the diagonal (L-STRUCT write-up, 2026-10-14)

Status: signed by the first referee (REFEREE, referee 9bf5301, after the two fixes of 1f5e004 applied at 50dc28b); the
second, independent referee checks L4 together with T3 as one M3 package (Lead 21:35Z). Lead reading L7: L4 is a supporting lemma; T3 + L4 count as M3. Nothing here is a result
until signed. Vocabulary: docs/struct/S1-statement.md (D1-D5, conventions E/S/V, Lemma 2), S3 D6 (diagonal).

Attribution. The reduction below is L-LIT's Claim R (docs/lit/T6-S3.md, unrefereed there), which L-STRUCT derived
independently in the weaker "split G_t" form (S3 §4b route R1) and the REFEREE sharpened (delta check, finding 8). The
vertex-splitting construction itself is a published remark: Parys-Wiącek, arXiv 2305.00308v1, p.2, verbatim: "(A general
method for switching from priorities on edges to priorities in vertices is to replace each vertex by d vertices, one
for each priority, and to redirect every edge to a copy of the target vertex having the appropriate priority; then the
number of vertices changes from n to nd.)" Stated without proof or theorem number; p.8 (§4): "for games with
priorities on edges it can be shown that n-universality is indeed required [8,1]. However most papers (including ours)
define parity games with priorities on vertices, in which case the necessity proof does not apply." L4 closes that
caveat up to the n/d' loss below. Claim R makes a re-run of CDFJLP's Lemma 5.1 unnecessary: Theorem 5.1 is used as
a black box. (The REFEREE's split-G_t route gives the same bound by re-running Lemma 5.1 on a vertex-labelled G'_t;
it is not written here. If the second referee wants a self-contained proof, that is the route.)

## 1. Statements (TARGET vocabulary)
Recall (S1 D5) s^X(n,d), w^X(n,d) for X ∈ {E, S, V} over Σ_d = {1..d}; (S3 D6) S(n) = s^V(n,n), W(n) = w^V(n,n), the
sizes relevant to TARGET games with n vertices (priorities {0..n}; letter 0 removed by S1 Lemma 2(b-V)).

Lemma L4.1 (transfer; Claim R). For all k ≥ 1 and d ≥ 2:
    s^E(k, d) ≤ s^V(k·d, d)     and     w^E(k, d) ≤ w^V(k·d, d).
Lemma L4.2 (monotonicity; S1 Lemma 2(a) made explicit). For all n' ≤ n and d' ≤ d: s^V(n', d') ≤ s^V(n, d) and
    w^V(n', d') ≤ w^V(n, d).
Theorem L4. For all n ≥ 1,
    S(n) = s^V(n, n) ≥ max { C(⌊lg⌊n/d'⌋⌋ + d'/2 − 1, ⌊lg⌊n/d'⌋⌋) : d' even, 2 ≤ d' ≤ n }.
Corollary L4.3 (closed form). For all n ≥ 64, with a0 = ⌊½ lg n⌋ − 2 ≥ 1 and b0 = ⌈√n/2⌉ − 2 ≥ 2,
    S(n) ≥ C(a0 + b0, a0) ≥ (b0/a0)^{a0} ≥ (√n / (2 lg n))^{⌊½ lg n⌋ − 2},
which is n^{Ω(lg n)}: super-polynomial. (For n < 64 the bound is ≤ 1 and the table gives the values.)
Corollary L4.4 (TARGET reading). Every deterministic algorithm of the product class (S2 §1 (i)-(iii)) whose automaton
A_{n} is a deterministic STRONG separator (every known quasi-polynomial product algorithm, CDFJLP §3.3-§4) spends time
≥ n·S(n) = n^{Ω(lg n)} on TARGET games with n vertices. This is the vertex-priority form of barrier B1
(docs/lit/BARRIERS.md). It says nothing about weak separators: that is T3's job (S3).

## 2. Proof of Lemma L4.1
Fix k, d and an edge-labelled Σ_d-graph H = (V, E), E ⊆ V × Σ_d × V, with |V| ≤ k (convention E; S and V are
sub-cases). Define the vertex-labelled graph H' (Parys-Wiącek's conversion):
    V' = V × Σ_d,   pr'(v, p) = p,   E' = { ((u, p), (v, q)) : (u, q, v) ∈ E, p ∈ Σ_d }.
H' is a V-graph (S1 D1: E' ⊆ V' × V', labels on vertices) with |V'| ≤ k·d vertices, which is all the lemma needs.
(a) Paths. A path v0 -q1-> v1 -q2-> v2 -q3-> ... of H (word q1 q2 q3 ...) lifts, for any p ∈ Σ_d, to the path
    (v0, p) → (v1, q1) → (v2, q2) → ... of H', whose vertex word is p · q1 q2 q3 .... Conversely a path
    (v0, p0) → (v1, p1) → (v2, p2) → ... of H' projects to the path v0 -p1-> v1 -p2-> v2 ... of H (the edge
    ((v_i, p_i), (v_{i+1}, p_{i+1})) ∈ E' means (v_i, p_{i+1}, v_{i+1}) ∈ E), and its word p0 p1 p2 ... is p0 followed by
    the word of the projected path. So  Words(H') = { p · w : p ∈ Σ_d, w ∈ Words(H) }  (for infinite paths).
(b) Cycles. A cycle (v0,p0) → (v1,p1) → ... → (v_{m−1},p_{m−1}) → (v0,p0) of H' projects to a closed walk
    v0 -p1-> v1 -p2-> ... -p_{m−1}-> v_{m−1} -p0-> v0 of H whose multiset of labels {p1, ..., p_{m−1}, p0} equals the
    multiset of vertex labels of the H'-cycle; so the two have the same maximum. A closed walk of H decomposes into
    simple cycles of H, and its maximum is the maximum over them. Hence: if every cycle of H has even (odd) maximum,
    so has every cycle of H'. Conversely a simple cycle v0 -q1-> ... -q_m-> v0 of H lifts to the cycle
    (v0, q_m) → (v1, q1) → ... → (v_{m−1}, q_{m−1}) → (v0, q_m) of H' with the same label multiset. So H' is even iff
    H is even, and odd iff H is odd.
(c) Languages. By (a), (b):  for every w ∈ Σ_d^ω and p ∈ Σ_d,
      w ∈ EvenCycles^E_{k,d} ⇒ p·w ∈ EvenCycles^V_{kd,d},      w ∈ OddCycles^E_{k,d} ⇒ p·w ∈ OddCycles^V_{kd,d},
    and limsup(p·w) = limsup(w), so w ∈ LimsupOdd_d ⇔ p·w ∈ LimsupOdd_d.
(d) The automaton. Let A = (Q, q0, δ) be a deterministic safety automaton over Σ_d that is a strong (resp. weak)
    (kd, d)-separator in convention V. Put q1 := δ(q0, 1). Then q1 ≠ ⊥: the word 2^ω is in EvenCycles^E_{k,d} (one vertex with a self-loop labelled 2;
    here d ≥ 2 is used), so 1·2^ω ∈ EvenCycles^V_{kd,d} ⊆ L(A), and the run of A on 1·2^ω does not reach ⊥; in particular
    q1 ≠ ⊥. Define A' = (Q, q1, δ) (same states and transitions, new
    initial state; unreachable states may be dropped). For every w: A' accepts w iff A accepts 1·w.
    - Strong: EvenCycles^E_{k,d} ⊆ L(A') since w ∈ EvenCycles^E ⇒ 1·w ∈ EvenCycles^V_{kd,d} ⊆ L(A); and
      L(A') ⊆ LimsupEven_d since w ∈ L(A') ⇒ 1·w ∈ L(A) ⊆ LimsupEven_d ⇒ w ∈ LimsupEven_d. So A' is a deterministic
      strong (k,d)-separator in convention E with |A'| ≤ |A|; hence s^E(k,d) ≤ s^V(kd,d).
    - Weak: the first inclusion as above; and L(A') ∩ OddCycles^E_{k,d} = ∅ since w ∈ OddCycles^E ⇒ 1·w ∈
      OddCycles^V_{kd,d}, rejected by A, so w is rejected by A'. Hence w^E(k,d) ≤ w^V(kd,d).            ∎
Checks asked by L-LIT (T6, points (i)-(iii)): (i) S1's V convention emits pr(u) when leaving u, so the word of a V-path
is the sequence of vertex labels, which is what (a) uses, and the start letter is the label of the start vertex, as
used; (ii) the construction is identical from E, S or V sources (an S- or V-graph is an E-graph); (iii) q1 ≠ ⊥ is
shown in (d) for d ≥ 2.

## 3. Proof of Lemma L4.2
Let A be a strong (weak) (n,d)-separator in convention V. (n' ≤ n) Every V-graph with ≤ n' vertices has ≤ n vertices,
so EvenCycles^V_{n',d} ⊆ EvenCycles^V_{n,d} and OddCycles^V_{n',d} ⊆ OddCycles^V_{n,d}; A is a strong (weak) (n',d)-separator.
(d' ≤ d) Restrict δ to Σ_{d'}: a Σ_{d'}-graph is a Σ_d-graph with the same cycle maxima, so EvenCycles^V_{n,d'} ⊆
EvenCycles^V_{n,d} ⊆ L(A), and the restricted automaton accepts exactly L(A) ∩ Σ_{d'}^ω ⊆ LimsupEven_{d'} (strong) or
avoids OddCycles^V_{n,d'} ⊆ OddCycles^V_{n,d} (weak). States do not increase.                                      ∎

## 4. Proof of Theorem L4 and Corollary L4.3
Fix n and an even d' with 2 ≤ d' ≤ n; put k = ⌊n/d'⌋ ≥ 1. By L4.2 (d' ≤ n, then k·d' ≤ n), L4.1 and CDFJLP Thm 5.1
(arXiv 1807.10546v2 §5, verbatim: "Every non-deterministic safety strong (n, d)-separator has at least
C(⌊lg n⌋+d/2−1, ⌊lg n⌋) states"; a deterministic separator is a non-deterministic one; the bound counts non-rejecting
states, S1 D4; and Thm 5.1 is a theorem about convention E, since its graphs G_t carry parallel self-loops, REFEREE S2
§2):
    s^V(n, n) ≥ s^V(n, d') ≥ s^V(k·d', d') ≥ s^E(k, d') ≥ C(⌊lg k⌋ + d'/2 − 1, ⌊lg k⌋).
Maximising over d' gives Theorem L4. For the closed form take d' = 2⌊√n/2⌋ (even; √n − 2 ≤ d' ≤ √n). Then
k = ⌊n/d'⌋ ≥ ⌊√n⌋ ≥ √n − 1, so ⌊lg k⌋ ≥ ⌊lg(√n − 1)⌋ ≥ ⌊½ lg n⌋ − 2 =: a0 for n ≥ 16 (as √n − 1 ≥ √n/2 there), and
d'/2 − 1 = ⌊√n/2⌋ − 1 ≥ (⌈√n/2⌉ − 1) − 1 = ⌈√n/2⌉ − 2 =: b0 (REFEREE 1f5e004, fix 2). C(a+b, a) is non-decreasing in a and in b, so the bound is at least
C(a0 + b0, a0) ≥ ((a0 + b0)/a0)^{a0} ≥ (b0/a0)^{a0}; for n ≥ 64, a0 ≥ 1 and b0 ≥ 2, and b0/a0 ≥ √n/(2 lg n) once
√n/2 − 2 ≥ √n/4 (n ≥ 64) and a0 ≤ ½ lg n. Hence (b0/a0)^{a0} ≥ (√n/(2 lg n))^{⌊½ lg n⌋ − 2} = 2^{Θ(lg² n)}.  ∎
Numerical check (experiments/weak-sep/l4_bound.py, exact binomials): the optimised bound of Theorem L4 and the closed
form of L4.3 for n = 64, 256, 1024, 4096, 2^16 are 36 / 3, 816 / 28, 52360 / 680, 11716640 / 46376, 2.6·10^13 /
6.5·10^9; the closed form never exceeds the optimised bound for n ≤ 5000. Consistency with the table
(experiments/weak-sep/results/table.md): for n ≤ 4 the bound is ≤ 1 ≤ s^V(n,n); nothing to compare yet.

## 5. What L4 does and does not give
- It gives: S(n) = n^{Ω(lg n)}, so the strong-separator product class is super-polynomial on TARGET games (L4.4),
  and S3's T3-neg conditional barrier becomes unconditional IF T3 is proved (W(n) = S(n) ⇒ W(n) = n^{Ω(lg n)}).
- It does not give: any bound on W(n) (the weak transfer L4.1 has no edge lower bound to pull back: w^E is as open as
  w^V); nor the sharp exponent (the edge bound's exponent lg(d/lg n) − 2 at d = n loses to lg(d'/lg k) − 2 at d' ≈ n^{0.6}
  optimal numerically, i.e. a constant factor in the exponent); nor anything for d < lg n-ish, where Thm 5.1 is void.
- Novelty: L-LIT T6 found no vertex-priority lower bound in print; Parys-Wiącek state the construction as a remark and
  say the necessity proof "does not apply". L4 is the small step that applies it. M3 status per L7: supporting lemma.
