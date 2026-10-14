# L1 statement: straight-line symbolic programs (SLPs) and the first lower-bound target (L-LOWER, 2026-10-14)

Status: DRAFT for the Lead and a fresh REFEREE (TARGET.md section 7e: statement before proof work). Nothing here is a result.
Every source quoted below was opened by L-LOWER on 2026-10-14; theorem numbers and pages are in notes/L-LOWER.md.
Vocabulary is TARGET.md section 1 (max-parity, priorities on vertices, every vertex has a successor, W_E = Even's region).

## 1. The model (fixed here; every later claim refers to this section)

**Definition 1.1 (base sets).** For a parity game G = (V, V_E, V_O, E, pr) with pr(V) ⊆ {0, ..., d}, the base sets are
P_p = {v : pr(v) = p} for p = 0, ..., d, the set V_E, and ∅. (V = V \ ∅ and V_O = V \ V_E are Boolean combinations.)

**Definition 1.2 (Cpre).** Cpre_E(X) = {v ∈ V_E : E(v) ∩ X ≠ ∅} ∪ {v ∈ V_O : E(v) ⊆ X}, where E(v) = {w : (v, w) ∈ E}.

**Definition 1.3 (SLP over (n, d)).** A straight-line symbolic program over (n, d) is a finite sequence X_1, ..., X_L of gates,
each of one of the forms
  (base)  P_p (0 ≤ p ≤ d), V_E, ∅;
  (bool)  X_j ∪ X_k, X_j ∩ X_k, V \ X_j with j, k < i;
  (cpre)  Cpre_E(X_j) with j < i.
Its value on a game G is obtained by evaluating the gates in order on G. Its output is the value of X_L.
Cost c(P) = number of (cpre) gates. Depth δ(P) = maximum number of (cpre) gates on a path of the gate DAG (nesting depth).
Clearly δ(P) ≤ c(P).

**Definition 1.4 (solving).** P solves (n, d) if for every game G of TARGET.md section 1 with |V| ≤ n and pr(V) ⊆ {0, ..., d},
the output of P on G equals W_E(G). (Games with fewer than n vertices are included.)
  C(n, d) = min { c(P) : P solves (n, d) }.
Büchi variants (priorities in {1, 2}: Even wins iff priority 2 occurs infinitely often; TARGET max-parity):
  B_2(n) = min cost over programs whose output equals W_E(G) on every game with |V| ≤ n and pr(V) ⊆ {1, 2};
  B_1(n) = the same over the one-player games (V_O = ∅, so Cpre_E = Pre and V_E = V).
Trivially B_1(n) ≤ B_2(n) ≤ C(n, 2) (a program for priorities {0, 1, 2} is run with P_0 = ∅), and C(n, d) ≤ C(n, d').
for d ≤ d'.

**Restrictions, stated so no proof silently assumes more (R1-R6).**
- R1 Non-adaptive: the gate sequence is fixed before the game is seen; it may depend on n and d (a non-uniform family).
- R2 Vertex-anonymous: the only inputs are the base sets of Def. 1.1. There is no "pick a vertex", no singleton sets,
  no counting, no comparison of sets (no ⊆ or = tests; their results could not influence the fixed sequence anyway).
- R3 The only one-step gate is Cpre_E. Cpre_O(X) = V \ Cpre_E(V \ X) and Pre(X) = (V_E ∩ Cpre_E(X)) ∪ (V_O \ Cpre_E(V \ X))
  cost 1 and 2 gates. Post (successors) is not expressible at all (backward modality), so SLPs are WEAKER than the
  model of CDHL (item (a) in section 2), and CDHL lower bounds transfer to SLPs.
- R4 Boolean gates are free and unrestricted: complement is allowed everywhere, including inside Cpre arguments.
  A bound proved only for complement-free ("monotone") programs is a weaker theorem and must say so.
- R5 Cost counts Cpre gates, not depth: a depth lower bound (Lemma 1.6) is not a cost lower bound beyond itself.
- R6 Correctness is required on ALL games with at most n vertices: a lower-bound family may use any games of size ≤ n,
  but may not use games with more than n vertices.

**Lemma 1.5 (invariance).** The value of every gate is invariant under isomorphism of games and, more strongly, under
bisimulation of pointed games (v, G) ~ (v', G') with respect to the labels pr and the owner bit: v ∈ X_i(G) iff v' ∈ X_i(G').
Proof: induction over the gate sequence; base sets are label tests, Boolean gates are pointwise, and Cpre_E(X) at v
depends only on the owner of v and the X-membership of its successors, which bisimulation preserves. (W_E is also
bisimulation invariant, so the problem is well posed on the bisimulation quotient; this is what experiments/lower uses.)

**Lemma 1.6 (locality).** The value of a gate of nesting depth k at a vertex v is determined by the depth-k unravelling
of (v, G) (the tree of paths of length ≤ k from v, labelled by pr and the owner bit). Proof: induction on k.

## 2. Known bounds, re-derived for this model

### (a) Lower bound Ω(n), two ways
**Lemma 2.1 (direct). B_1(n) ≥ n − 1 for n ≥ 2.** Proof: let G^+ be the one-player game on v_1 → v_2 → ... → v_n → v_n
(self-loop at v_n), pr(v_n) = 2 and pr(v_i) = 1 otherwise; G^- is the same with pr(v_n) = 1. Both are TARGET games
(every vertex has a successor). W_E(G^+) = V and W_E(G^-) = ∅. The depth-(n − 2) unravellings of (v_1, G^+) and
(v_1, G^-) coincide (they only see v_1, ..., v_{n−1}). By Lemma 1.6 a program of depth ≤ n − 2 gives v_1 the same
answer on both, so a solving program has δ ≥ n − 1, hence c ≥ n − 1.
Hence C(n, d) ≥ B_2(n) ≥ B_1(n) ≥ n − 1 for all d ≥ 2.
**Lemma 2.1' (sharper, L-LOWER 2026-10-15, unrefereed). B_1(n) ≥ 2n − 2 for n ≥ 2**, and this is the exact minimal DEPTH
for n ≤ 4 (experiments/lower/depthneeded.py). Proof: G^cyc = the cycle a_1 → a_2 → ... → a_n → a_1 with pr(a_{n−1}) = 2, all
others 1, root a_1 (winning: W_E = V); G^tail = a_1 → ... → a_{n−1} → z → z with z a fresh vertex of priority 1 (n vertices,
losing from a_1). Both are deterministic, so their depth-D types are their label words: G^cyc gives P_1^{n−2} P_2 P_1^{n−1} P_2 ...
with the second P_2 at position 2n − 2; G^tail gives P_1^{n−2} P_2 P_1^ω. They agree up to depth 2n − 3, so by Lemma 1.6 any
solving program has δ ≥ 2n − 2. (Found by experiments/lower/fooling.py as the deepest fooling pair for n = 2, 3, 4.)

**Transfer 2.2 (CDHL, arXiv 1711.09148 v1).** Model (their §2, verbatim): the graph "can be accessed only by the following
two types of operations: 1. Basic set operations like ∪, ∩, \, ⊆, and =; 2. One-step operations to obtain the predecessors
or successors of the vertices of S in G", Pre(S) = {v | ∃s ∈ S : (v, s) ∈ E}, Post(S) = {v | ∃s ∈ S : (s, v) ∈ E};
the algorithm is otherwise unrestricted (adaptive, unbounded free computation, any number of stored sets, p.1-2).
Their Theorem 3.10 (1): any symbolic algorithm that solves Büchi(T) needs "Ω(n) even for instances with constant D"
one-step operations. The proof (their p.13) uses Reduction 3.9: vertices v_0, ..., v_k, edges v_i → v_j for i < j, a loop
at v_k, and a loop at v_j (j < k) iff x_j = y_j = 1; T = {v_0, ..., v_{k−1}}; "v_0 is winning for Büchi(T) iff there is a loop
for one of the vertices in T iff S_x ∩ S_y ≠ ∅"; every one-step operation costs O(1) bits of communication, so o(n)
operations would give an o(k) protocol for Set Disjointness, contradicting their Theorem 2.1.
  Check list for the transfer: (i) every vertex of Reduction 3.9 has a successor (v_i → v_k for i < k; loop at v_k), so
  these are TARGET games with V_O = ∅, P_2 = T, P_1 = {v_k}; (ii) on one-player games Cpre_E(X) = Pre(X), so an SLP with
  c Cpre gates is a symbolic algorithm with c one-step operations, and "v_0 ∈ output" is a basic set operation; (iii) an
  SLP is a (degenerate, non-adaptive) algorithm in their class, which they allow to store arbitrarily many sets. Hence
  B_1(n) = Ω(n) with n = k + 1. L-LOWER reading: this is the same order as Lemma 2.1 with an unspecified constant; the
  communication method cannot give more than the two-party communication complexity of the problem divided by the
  bits per operation, and on their graphs that is Θ(n) (see section 4).

### (b) Upper bounds
**Lemma 2.3 (unfolded Büchi). B_2(n) ≤ n^2.** W_E = νZ. μY. Cpre_E((P_2 ∩ Z) ∪ (P_1 ∩ Y)) on games with pr(V) ⊆ {1, 2}
(standard; it is the d = 2 instance of (c) below with the priority of the successor read, see Remark 2.5). The SLP:
Z_0 = V; for i = 1..n: Y_0 = ∅, Y_j = Cpre_E((P_2 ∩ Z_{i−1}) ∪ (P_1 ∩ Y_{j−1})) for j = 1..n, Z_i = Y_n; output Z_n.
Each monotone chain over a set of ≤ n vertices has at most n strict steps, so Y_n and Z_n are the fixpoints. n·n Cpre gates.
(Checked against Zielonka for n ≤ 4 in experiments/lower, section 3.)

**Transfer 2.4 (ANP, LIPIcs.CSL.2021.9).** ANP evaluate θ_d x_d ... θ_1 x_1 . f(x_1, ..., x_d) for a monotone black-box
f : (B^n)^d → B^n by the two-tree recursion ‖F‖_{U,V} (their §3.1, cases (1)-(3), p.9:5). Lemma 3.2 (verbatim): "There is
an algorithm that computes ‖F‖_{U,V} using |U|·|V| queries to the function f." Lemma 3.1: if U, V are (n, |Θ|_μ)- and
(n, |Θ|_ν)-universal then ‖F‖_{U,V} = ‖F‖. Prop. 2.5: S_{n,h} is (n, h)-universal with n^{lg(h/lg n)+O(1)} leaves.
  Reading into SLPs: the recursion is straight-line (the sequence of queries and their arguments depend only on U, V,
  Θ, never on answers; the restrictions f_{A,B}(x) = A + B ∗ f(x) are free Boolean gates). For a parity game take
  g(x_0, ..., x_d) = ∪_p (P_p ∩ Cpre_E(x_p)), monotone, d + 1 Cpre gates per query; its alternating nested fixpoint is W_E
  (standard μ-calculus characterisation; L-LOWER has not yet opened a primary source for this, see NEEDS). Hence
    C(n, d) ≤ (d + 1) · |S_{n,h_μ}| · |S_{n,h_ν}| ≤ n^{2·lg(d/lg n) + O(1)}, with h_μ, h_ν ≤ ⌈(d + 1)/2⌉.
  CAUTION (correction to the T7 reading): ANP's bound n^{lg(d/lg n)+O(1)} (Cor. 3.7) comes from the asymmetric algorithm
  of Lemma 3.6, whose proof uses "a standard worklist algorithm" that "re-evaluate[s] right sides only of those equations
  in which at least one variable was modified in the previous stage". That is ADAPTIVE (which queries are made depends on
  answers). A non-adaptive round-robin evaluation of the same |V| equations needs up to 1 + n·|V| stages (each stage but
  the last raises some bit), i.e. |V|·(1 + n·|V|) queries, again n^{2·lg(d/lg n)+O(1)}. So the best SLP upper bound
  L-LOWER can currently derive from ANP is the SYMMETRIC one, exponent 2·lg(d/lg n) + O(1), not lg(d/lg n) + O(1).
  Whether the exponent can be halved non-adaptively is open to L-LOWER (a question for L-LIT: is any symbolic
  progress-measure algorithm, e.g. CDHS arXiv 1909.04983, oblivious?). For d = 2 none of this matters: Lemma 2.3 gives n^2.
  Remark 2.5: with f'(x) = Cpre_E(∪_p (P_p ∩ x_p)) (priority of the successor) each query is ONE Cpre gate, which removes
  the factor d + 1; L-LOWER believes θ-nested f' also equals W_E (the play's priority sequence is shifted by one step,
  which does not change its limsup), but this needs a source or a proof before use; it does not change any exponent.
  ANP Theorem 5.1 and Remark 5.5 (lower bound) apply only to programs of the shape ‖·‖_{U,V} or ‖·‖_V, not to Def. 1.3.

**Known picture (this model):** 2n − 2 ≤ B_1(n) ≤ B_2(n) ≤ n^2, and 2n − 2 ≤ C(n, d) ≤ n^{2·lg(d/lg n)+O(1)}.
Exact values (experiments/lower, SAT on the bisimulation quotient, cross-checked by BFS for n ≤ 3): B_1(1..4) = 0, 2, 4, 6 = 2n − 2,
attained by chain programs (each gate reads only P_2 and the previous gate). See docs/lower/L1-report.md for n = 5 and the
depth theorem (depth-(2n−1) types determine W_E on one-player Büchi games with ≤ n vertices), which caps any lower bound
argument based on depth at Θ(n).

## 3. Targets (precise statements; nothing proved)

**T-L1 (first target; L-LIT's T7-1').** B_1(n) = ω(n): for every constant K there is n with B_1(n) > K·n.
Strong form: there is ε > 0 with B_1(n) ≥ n^{1+ε} for all large n. In words: every straight-line symbolic program
(Def. 1.3, restrictions R1-R6) that outputs Even's winning region on every one-player Büchi game with at most n vertices
uses super-linearly many Cpre gates.
Why it would matter (L-LIT T7 §b, re-checked by L-LOWER against CDHL §4 "Upper Bounds for Liveness", p.14: Büchi(T) is solved
with O(min(SCC + D, |T|·D)) symbolic operations, with SCC = O(n) by [GPP08]): in the adaptive model of Transfer 2.2 one-player
Büchi costs O(n) one-step operations, so T-L1 would separate non-adaptive anonymous programs from adaptive symbolic
algorithms on an ω-regular objective, the first super-linear symbolic lower bound for any such objective (L-LIT: none found).

**T-L2 (stretch; L-LIT's T7-1).** B_2(n) = Ω(n^2 / polylog n), ideally already B_1(n).

**T-L3 (the rank-2 goal, for later).** C(n, d) ≥ n^{lg(d/lg n) − O(1)}: ANP Theorem 5.1 for arbitrary SLPs.

Novelty: L-LIT (T7) found no lower bound beyond linear for any non-adaptive symbolic model; the modal-logic succinctness
results (Jung-Kołodziejski, Hella-Vilander) concern equivalence over all structures, not over structures with ≤ n states.
REFEREE: please check Def. 1.3-1.4, Lemmas 1.5, 1.6, 2.1, 2.3, Transfers 2.2 and 2.4 (including the CAUTION), and that T-L1
is stated in TARGET vocabulary and is not already in the literature.

## 4. Proof routes and the known obstruction (for section 3 of the report; sketch only)
- Two-party communication (CDHL's method) is capped at the communication complexity of the problem per bit of
  communication per operation; on Reduction 3.9 every operation costs O(1) bits and the problem costs Θ(n), so the method
  as used gives Θ(n) and no more. A super-linear bound needs either a family where the problem has ω(n) communication
  complexity while every Cpre still costs O(1) bits, or a different measure.
- Candidate measure: by Lemma 1.5, a program with c Cpre gates is a modal formula DAG with c diamonds; T-L1 is a
  DAG-size lower bound for "exists a path with ≥ n visits to P_2" (the Büchi region on ≤ n vertices, by the pigeonhole
  on repeated P_2 vertices) on the class of ≤ n-vertex graphs. The nesting (count × distance) structure of Lemma 2.3 is
  what a proof must show to be unavoidable; the danger is a program that counts cleverly (data in section 3 of the report).
