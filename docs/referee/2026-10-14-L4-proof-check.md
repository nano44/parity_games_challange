# Referee report (first referee): L4, strong V-separators are super-polynomial on the diagonal (L-STRUCT 168d828)

Referee: REFEREE (first of two; a second, independent referee follows, per the Lead 2026-10-14 21:35Z). Date: 2026-10-15.
Source: claude/l-struct 168d828, docs/struct/L4-proof.md and experiments/weak-sep/l4_bound.py. Sources opened: CDFJLP
arXiv 1807.10546v2 §5 (Thm 5.1, Lemmas 5.1–5.3, G_t) and Thm 2.3 (LaTeX source, earlier reports); Parys–Wiącek
arXiv 2305.00308v1 (LaTeX source, e-print sha256 8c629f23…): the two quoted sentences are verbatim at
improved-parity.tex lines 86–87 and 368.

## Verdict: CHANGES (every statement holds; two sentences in the proofs are wrong as written and must be fixed)

| item | verdict |
| --- | --- |
| Lemma L4.1 (Claim R), strong and weak | OK; one false remark about deleting vertices (finding 1) |
| Lemma L4.2 (monotonicity in n and d) | OK |
| Theorem L4 | OK |
| Corollary L4.3 (constants for n ≥ 64) and l4_bound.py | OK in substance; one intermediate inequality false as written, conclusion true (finding 2); numbers reproduced |
| Corollary L4.4 (TARGET reading) | OK, with the class stated as in S2/S3 |
| CDFJLP Thm 5.1 as a black box | legitimate: E-convention lower bound pulled to V by L4.1; non-rejecting states; deterministic ⊆ non-deterministic; binomial form needs no side condition |

## 1. Lemma L4.1, re-derived
H' = (V × Σ_d, pr'(v,p) = p, E' = {((u,p),(v,q)) : (u,q,v) ∈ E, p ∈ Σ_d}).
(a) Paths: leaving (u,p) emits p (S1 D1, V convention); ((v_i,p_i),(v_{i+1},p_{i+1})) ∈ E' iff (v_i, p_{i+1}, v_{i+1}) ∈ E;
so an H'-path from (v0,p) has word p·(word of the projected H-path), and every H-path lifts from every (v0,p). Hence
Words(H') = {p·w : p ∈ Σ_d, w ∈ Words(H)} when ALL of V × Σ_d is kept. ✓
Finding 1: the parenthetical "vertices (v,q) with no edge of label q into v have no incoming edge; they may be deleted
… nothing changes, since they lie on no infinite path" is false: such a vertex has out-edges and is the start of
infinite paths; deleting (v0,1) would remove the words 1·w that (d) needs when no 1-edge enters v0. Delete the remark
(the lemma counts |V'| ≤ kd anyway) or restrict it to vertices that are also not used as starts.
(b) Cycles: an H'-cycle through (v_0,p_0),…,(v_{m−1},p_{m−1}) projects to the closed walk of H with labels
p_1,…,p_{m−1},p_0, the same multiset; a closed walk's maximum is the maximum of the simple cycles it decomposes into;
so all-even (all-odd) cycles in H give all-even (all-odd) cycles in H'. Conversely a simple H-cycle lifts with the
same multiset. H' even ⇔ H even, odd ⇔ odd. ✓
(c) w ∈ EvenCycles^E_{k,d} ⇒ p·w ∈ EvenCycles^V_{kd,d} (H' has ≤ kd vertices), likewise odd; limsup(p·w) = limsup(w). ✓
(d) q1 = δ(q0,1) ≠ ⊥ because 2^ω is the word of the even one-vertex graph with a loop labelled 2 (d ≥ 2, k ≥ 1), so
1·2^ω ∈ EvenCycles^V_{kd,d} ⊆ L(A). A' = (Q, q1, δ) accepts w iff A accepts 1·w (determinism). Strong: both inclusions
as written. Weak: (W1) as above and (W2) from odd lifting. |A'| ≤ |A|. So s^E(k,d) ≤ s^V(kd,d), w^E(k,d) ≤ w^V(kd,d). ✓
Conventions: A is a (kd,d)-separator in V, applied to the V-graph H'; A' is judged in E. The chain of conventions is
exactly what the black-box use needs. S and V sources are E-graphs, so L4.1 also gives s^S(k,d) ≤ s^V(kd,d). ✓

## 2. Lemma L4.2
n' ≤ n: fewer graphs to handle. d' ≤ d: a Σ_{d'}-graph is a Σ_d-graph with the same cycle maxima; the automaton restricted
to Σ_{d'} accepts L(A) ∩ Σ_{d'}^ω, which lies in LimsupEven_{d'} (strong) and misses OddCycles^V_{n,d'} (weak); states
do not increase. ✓ (Same as S1 Lemma 2(a); L4.2 writes it out.)

## 3. Theorem L4
For even d' with 2 ≤ d' ≤ n and k = ⌊n/d'⌋ ≥ 1: s^V(n,n) ≥ s^V(n,d') [L4.2] ≥ s^V(kd',d') [L4.2, kd' ≤ n] ≥ s^E(k,d')
[L4.1] ≥ C(⌊lg k⌋ + d'/2 − 1, ⌊lg k⌋) [CDFJLP Thm 5.1 at (k,d')]. ✓ Black-box check: Thm 5.1 (source §5, verbatim in
L4) is stated for every non-deterministic safety strong (n,d)-separator; deterministic ones are included; its proof
counts non-rejecting states (the tree decomposition is on non-rejecting states and the leaves inject there, my S2 §2),
matching S1 D4; its graphs G_t carry one self-loop per even priority at each vertex, so it is a statement about
convention E (my S2 §2), and L4.1 pulls it to V; the binomial form comes from Thm 2.3 "for all positive integers ℓ, h",
no side condition (the "d ≤ n" in CDFJLP is for the closed form n^{lg(d/lg n) − 2}, not used); d' even is required
(d/2) and provided. Legitimate.

## 4. Corollary L4.3 and l4_bound.py
d' = 2⌊√n/2⌋ is even with √n − 2 < d' ≤ √n; k = ⌊n/d'⌋ ≥ ⌊√n⌋; ⌊lg k⌋ ≥ ⌊lg(√n − 1)⌋ ≥ ⌊½ lg n⌋ − 2 = a0 for n ≥ 16 ✓.
Finding 2: the written step "d'/2 − 1 ≥ (√n − 2)/2 − 1 ≥ ⌈√n/2⌉ − 2" is false in the middle: (√n − 2)/2 − 1 = √n/2 − 2
< ⌈√n/2⌉ − 2 whenever √n/2 is not an integer (4905 of the 4937 values n ∈ [64, 5000]). The conclusion d'/2 − 1 ≥ b0 is
nevertheless true for every n, by d'/2 = ⌊√n/2⌋ ≥ ⌈√n/2⌉ − 1; write that instead (checked for all n ≤ 5000). The rest:
C(a+b,a) monotone in a, b ≥ 0 ✓; C(a0+b0, a0) ≥ ((a0+b0)/a0)^{a0} ≥ (b0/a0)^{a0} ✓; for n ≥ 64, a0 ≥ 1, b0 ≥ 2,
b0 ≥ √n/2 − 2 ≥ √n/4 and a0 ≤ ½ lg n give b0/a0 ≥ √n/(2 lg n) ✓; the final bound is < 1 for small n (0.67 at n = 64),
which is harmless since the statement is an inequality chain and the growth claim is asymptotic. The exponent
⌊½ lg n⌋ − 2 gives 2^{Θ(lg² n)} ✓.
l4_bound.py: run; outputs 36/3, 816/28, 52360/680, 11716640/46376, 2.58·10^13/6.55·10^9 for n = 64 … 2^16, closed form
≤ optimised for n ≤ 5000. My independent recomputation of Theorem L4's maximum agrees on all five n; the optimum sits
at d' = 16, 32, 64, 256, 1024 (not at √n), consistent with L4 §5's remark.

## 5. Corollary L4.4
An algorithm of class (i)–(iii) (S2 §3(c)) correct on TARGET games with ≤ n vertices has an automaton that is a weak
separator for V-graphs over {2..n+2} (my S2 §3(b)); if that automaton is strong (L(A) ⊆ LimsupEven over those
letters), then after the shift and S1 Lemma 2(b-V) (restriction direction, which also preserves strongness) it is a
strong (n,n)-separator in V, so |A| ≥ S(n) and time ≥ n·S(n) = n^{Ω(lg n)} by L4.3. ✓ The class is the one fixed in
S2/S3; "every known quasi-polynomial product algorithm uses a strong separator" is CDFJLP §3.3's remark, cited, not
proved here. It says nothing about weak separators, as L4 states. ✓

## 6. Attribution and novelty remarks
The Parys–Wiącek quotes are verbatim (improved-parity.tex 86–87, 368). Their construction is the H' of L4.1 (with
copies by priority of the TARGET vertex, which S1's V convention emits on exit), stated as a remark without proof;
L4.1 supplies the proof and the automaton transfer (d). The claim that no vertex-priority lower bound is in print is
L-LIT's (T6); not checked by me.

## Gaps (every step is prose; nothing machine-checked)
- G1. L4.1 (a)–(d): elementary, re-derived above; not formalised.
- G2. L4.2: elementary; not formalised.
- G3. CDFJLP Thm 5.1 is used as a black box: its proof (Lemmas 5.1–5.3, Thm 2.3) is not re-derived by this fleet; the
  conventions were checked against the source (above and S2 §2).
- G4. Corollary L4.3's constants: hand-checked and numerically checked for n ≤ 5000; the asymptotic claim is standard.
- G5. L4.4 depends on the class definition (i)–(iii) and on S1 Lemma 1 / Lemma 2(b-V) (refereed, prose).
- G6. The novelty claim is L-LIT's.

## Findings
1. L4.1(a): remove or restrict the vertex-deletion remark (false for start vertices; the lemma does not need it).
2. L4.3: replace the false intermediate inequality by d'/2 = ⌊√n/2⌋ ≥ ⌈√n/2⌉ − 1 (conclusion unchanged).
With 1 and 2 applied, I sign L4 as first referee: Theorem L4, Corollaries L4.3 and L4.4 hold as stated.
