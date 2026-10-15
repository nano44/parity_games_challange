# L1 statement: straight-line symbolic programs (SLPs) and the first lower-bound target (L-LOWER; v2, 2026-10-15)

Status: revised after REFEREE report R-L1 (claude/referee 9b01cbb, docs/referee/2026-10-14-L1-statement-check.md, verdict
CHANGES, findings 1-9 all addressed below) and L-LIT T9 (docs/lit/T9-L1.md). Nothing here is a result in the sense of CLAUDE.md.
Every source quoted was opened by L-LOWER (notes/L-LOWER.md, "Sources opened"); Emerson-Jutla FOCS 1991 was not opened (cited
through ANP [10] and Bradfield-Walukiewicz [46]). Vocabulary is TARGET.md section 1 (max-parity, priorities on vertices, every
vertex has a successor, W_E = Even's region), with the translation of section 1.0 below.

## 1. The model (fixed here; every later claim refers to this section)

**1.0 Translation to TARGET vocabulary (R-L1 findings 1, 2).** TARGET.md writes d = |pr(V)| for the NUMBER of distinct priorities.
This document never uses that d. It uses **p ≥ 0 for the largest priority allowed**: "priorities bounded by p" means pr(V) ⊆
{0, ..., p}; such a game has at most p + 1 distinct priorities, i.e. d_TARGET ≤ p + 1. TARGET games satisfy pr(v) ≤ |V|;
this document admits the alphabet {0, ..., p} (for Büchi: {1, 2}) regardless of |V|. The only games this adds are those with
pr(v) > |V| (for Büchi: the one-vertex game with priority 2). Adding games can only raise a minimum, so every lower bound
below holds a fortiori for the TARGET class, and under TARGET's convention C(n, p) = C(n, min(p, n)). The exact small-n
values in docs/lower/L1-report.md are for the alphabet-{1, 2} class (the one-vertex priority-2 game included; it changes no value).

**Definition 1.1 (base sets).** For a parity game G = (V, V_E, V_O, E, pr) with pr(V) ⊆ {0, ..., p}, the base sets are
P_q = {v : pr(v) = q} for q = 0, ..., p, the set V_E, and ∅. (V = V \ ∅ and V_O = V \ V_E are Boolean combinations.)

**Definition 1.2 (Cpre).** Cpre_E(X) = {v ∈ V_E : E(v) ∩ X ≠ ∅} ∪ {v ∈ V_O : E(v) ⊆ X}, where E(v) = {w : (v, w) ∈ E}.

**Definition 1.3 (SLP over p).** A straight-line symbolic program over p is a finite sequence X_1, ..., X_L of gates, each of
one of the forms
  (base)  P_q (0 ≤ q ≤ p), V_E, ∅;
  (bool)  X_j ∪ X_k, X_j ∩ X_k, V \ X_j with j, k < i;
  (cpre)  Cpre_E(X_j) with j < i.
Its value on a game G is obtained by evaluating the gates in order on G; its output is the value of X_L. The gate list depends
on p (which P_q exist) and not on n; n enters only through Definition 1.4 (finding 9).
Cost c(P) = number of (cpre) gates. Depth δ(P) = maximum number of (cpre) gates on a path of the gate DAG. δ(P) ≤ c(P).

**Definition 1.4 (solving).** P solves (n, p) if for every game G of TARGET.md section 1 (modulo 1.0) with |V| ≤ n and
pr(V) ⊆ {0, ..., p}, the output of P on G equals W_E(G). (Games with fewer than n vertices are included.)
  C(n, p) = min { c(P) : P solves (n, p) }.   (The minimum exists: Lemma 2.3 and Transfer 2.4 give solving programs.)
Büchi variants (priorities in {1, 2}; Even wins iff priority 2 occurs infinitely often, TARGET max-parity):
  B_2(n) = min cost over programs whose output equals W_E(G) on every game with |V| ≤ n and pr(V) ⊆ {1, 2};
  B_1(n) = the same over the one-player games (V_O = ∅, so Cpre_E = Pre and V_E = V).
B_1(n) ≤ B_2(n) ≤ C(n, 2) (a program for priorities {0, 1, 2} runs with P_0 = ∅) and C(n, p) ≤ C(n, p') for p ≤ p'.

**Restrictions, stated so that no proof silently assumes more (R1-R6).**
- R1 Non-adaptive: the gate sequence is fixed before the game is seen; it may depend on n and p (a non-uniform family).
- R2 Vertex-anonymous: the only inputs are the base sets of Def. 1.1. No singleton sets, no "pick a vertex", no counting, no
  ⊆ or = tests (their results could not influence the fixed sequence anyway).
- R3 The only one-step gate is Cpre_E. Cpre_O(X) = V \ Cpre_E(V \ X) and Pre(X) = (V_E ∩ Cpre_E(X)) ∪ (V_O \ Cpre_E(V \ X))
  cost 1 and 2 gates. Post (successors) is not expressible: it is not bisimulation invariant (R-L1 §1 gives the two-game witness),
  while every gate is (Lemma 1.5). So SLPs are a subclass of CDHL's algorithms (section 2(a)) and CDHL lower bounds transfer.
- R4 Boolean gates are free and unrestricted: complement is allowed everywhere, including inside Cpre arguments.
  A bound proved only for complement-free ("monotone") programs is a weaker theorem and must say so.
- R5 Cost counts Cpre gates, not depth: a depth lower bound (Lemma 1.6) is a cost lower bound only through δ ≤ c.
- R6 Correctness is required on ALL games with at most n vertices: a lower-bound family may use any games of size ≤ n,
  and none with more.

**Lemma 1.5 (invariance).** Let Z be a bisimulation between games G and G' respecting pr and the owner bit (u Z u' implies
pr(u) = pr(u'), u ∈ V_E iff u' ∈ V'_E, and the usual forth/back conditions on successors). Then for every gate X_i and every pair
u Z u': u ∈ X_i(G) iff u' ∈ X_i(G'). Proof: induction over the gate sequence, simultaneously for all pairs of Z. Base sets are
label tests, which Z respects. Boolean gates are pointwise. For Cpre_E(X_j): if u ∈ V_E has a successor w ∈ X_j, the forth
condition gives a successor w' of u' with w Z w', and w' ∈ X_j by the induction hypothesis; symmetrically with back. If u ∈ V_O,
every successor w' of u' has (back) a Z-partner w among the successors of u, w ∈ X_j, so w' ∈ X_j; symmetrically. ∎
Isomorphism is a bisimulation. W_E is also bisimulation invariant (a winning strategy transfers along Z; alternatively W_E is the
value of a μ-calculus formula, Transfer 2.4), so "P solves (n, p)" can be decided on the bisimulation quotient of the class of
pointed games with ≤ n vertices; experiments/lower/quotient.py (claude/l-lower b90c514) does exactly this.

**Lemma 1.6 (locality).** The value of a gate of nesting depth k at a vertex v is determined by the depth-k unravelling of
(v, G) (the tree of paths of length ≤ k from v, labelled by pr and the owner bit). Proof: induction on k over the DAG; a
Boolean gate's depth is the maximum of its inputs' depths; Cpre_E(X_j) at v is a function of the owner of v and of the bits
[w ∈ X_j] for the successors w of v, each determined by the depth-(k − 1) unravelling of (w, G), a subtree. ∎

## 2. Known bounds, re-derived for this model

### (a) Lower bounds
**Lemma 2.1 (direct). B_1(n) ≥ n − 1 for n ≥ 2.** Let G^+ be the one-player game on v_1 → v_2 → ... → v_n → v_n (self-loop
at v_n), pr(v_n) = 2 and pr(v_i) = 1 otherwise; G^- is the same with pr(v_n) = 1. Both are TARGET games. W_E(G^+) = V and
W_E(G^-) = ∅. The depth-(n − 2) unravellings of (v_1, G^+) and (v_1, G^-) coincide, so by Lemma 1.6 a program of depth ≤ n − 2
gives v_1 the same answer on both; a solving program has δ ≥ n − 1, hence c ≥ n − 1. ∎

**Lemma 2.1' (sharper; L-LOWER 2026-10-15, unrefereed). B_1(n) ≥ 2n − 2 for n ≥ 2.** Let G^cyc be the cycle a_1 → a_2 → ... →
a_n → a_1 with pr(a_{n−1}) = 2 and all other priorities 1, rooted at a_1 (W_E = V); let G^tail be a_1 → ... → a_{n−1} → z → z
with z a fresh vertex of priority 1 (n vertices; a_1 is losing). Both are deterministic, so their depth-D unravellings are their
label words: G^cyc gives P_1^{n−2} P_2 P_1^{n−1} P_2 ..., with the second P_2 at position 2n − 2; G^tail gives P_1^{n−2} P_2 P_1^ω.
They agree up to depth 2n − 3, so by Lemma 1.6 every solving program has δ ≥ 2n − 2, hence c ≥ 2n − 2. ∎
(The pair is the deepest fooling pair for n = 2, 3, 4 by exhaustive search, experiments/lower/fooling.py; depth 2n − 2 is the
exact minimal depth for n ≤ 4, experiments/lower/depthneeded.py.) Hence, for p ≥ 2: C(n, p) ≥ B_2(n) ≥ B_1(n) ≥ 2n − 2.

**Transfer 2.2 (CDHL, arXiv 1711.09148 v1; printed pages).** Model (§2, p.4, verbatim): the graph "can be accessed only by the
following two types of operations: 1. Basic set operations like ∪, ∩, \, ⊆, and =; 2. One-step operations to obtain the
predecessors or successors of the vertices of S in G", Pre(S) = {v | ∃s ∈ S : (v, s) ∈ E}, Post(S) = {v | ∃s ∈ S : (s, v) ∈ E};
the algorithm is otherwise unrestricted (adaptive, free computation, any number of stored sets; p.1-2). Theorem 3.10 (1), p.8:
any symbolic algorithm solving Büchi(T) needs "Ω(n) even for instances with constant D" one-step operations. Its proof (p.13)
uses Reduction 3.9 (p.7): vertices v_0, ..., v_k; edges v_i → v_j for all i < j; a loop at v_k; a loop at v_j (j < k) iff
x_j = y_j = 1 (x Alice's, y Bob's Set-Disjointness input); T = {v_0, ..., v_{k−1}}; "v_0 is winning for Büchi(T) iff there is a
loop for one of the vertices in T iff S_x ∩ S_y ≠ ∅". CDHL then say only "By the same argument as in the proof of Theorem 3.2
... each symbolic one-step operation just needs constant communication"; the argument written out (Lemma 3.4, p.5-6) is for
Reduction 3.1. For Reduction 3.9 the step is (R-L1 gap G3, written out here): let S ≠ ∅ be the argument of a Pre operation and
v_max its vertex of largest index. Every v_i with i < max has the definite edge v_i → v_max, so {v_i : i < max} ⊆ Pre(S). A
vertex v_i with i > max has edges only to v_j with j > i > max and its own loop, none into S, so v_i ∉ Pre(S). v_max itself is
in Pre(S) iff it has a loop, which is definite if max = k and otherwise depends on x_max and y_max: Alice sends the bit x_max,
Bob sends y_max. Dually for Post(S) with v_min (only its loop is in doubt). So each one-step operation costs two bits, and an
algorithm with N one-step operations gives a Set-Disjointness protocol with 2N bits; by CDHL Theorem 2.1 (p.5, Ω(k) bits), N = Ω(k).
  Check list for the transfer: (i) every vertex of Reduction 3.9 has a successor (v_i → v_k for i < k; loop at v_k), so these
  are TARGET games with V_O = ∅, P_2 = T, P_1 = {v_k}, n = k + 1 ≥ 2; (ii) on one-player games Cpre_E(X) = Pre(X), so an SLP
  with c Cpre gates is a deterministic algorithm of CDHL's class with c one-step operations, and "v_0 ∈ output" is a basic set
  operation; (iii) Theorem 3.10 covers deterministic algorithms. Hence B_1(n) = Ω(n) with n = k + 1; with the deterministic
  communication complexity of Set Disjointness ≥ k this gives B_1(n) ≥ (n − 1)/2, weaker than Lemmas 2.1 and 2.1'.
  L-LOWER reading: the two-party method is capped by the communication complexity of the problem divided by the bits per
  operation; on these graphs that is Θ(n) (section 4).

### (b) Upper bounds
**Lemma 2.3 (unfolded Büchi). B_2(n) ≤ n^2.** On games with pr(V) ⊆ {1, 2},
  W_E = νZ. μY. Cpre_E((P_2 ∩ Z) ∪ (P_1 ∩ Y))                                                          (†)
(the "successor-priority" form; the textbook form νZ.μY.(P_2 ∩ Cpre_E(Z)) ∪ (P_1 ∩ Cpre_E(Y)), Bradfield-Walukiewicz formula
(1) p.19 / Emerson-Jutla 1991, costs n(n + 1) gates). Proof of (†) in TARGET vocabulary (finding 3). Write Φ(Z) = μY. Cpre_E((P_2 ∩ Z)
∪ (P_1 ∩ Y)), Y_0 = ∅, Y_{j+1} = Cpre_E((P_2 ∩ Z) ∪ (P_1 ∩ Y_j)) (Kleene approximants; Φ(Z) = Y_n since the chain has ≤ n
strict steps on ≤ n vertices), and Z* = νZ.Φ(Z), so Z* = Φ(Z*).
(⊆) Give every v ∈ Z* its least j ≥ 1 with v ∈ Y_j (approximants of Φ(Z*)). Even's positional strategy: from v ∈ V_E ∩ Z*
move to a successor in (P_2 ∩ Z*) ∪ (P_1 ∩ Y_{j−1}) (one exists by v ∈ Y_j); from v ∈ V_O all successors lie in that set.
Every consistent play from Z* stays in Z*, and while it visits P_1 vertices their index j strictly decreases, so a P_2 vertex is
visited within n steps from every position: priority 2 occurs infinitely often and Even wins. So Z* ⊆ W_E.
(⊇) Let σ be a positional winning strategy for Even on W_E (positional determinacy, TARGET §1). For u ∈ W_E let r(u) be the
largest number of steps a σ-consistent play from u can make before its first visit to a P_2 vertex (the first step counts 1).
r(u) ≤ n (finite: u ∈ W_E forces P_2 ≠ ∅ and a first P_2 visit on every σ-consistent play): a σ-consistent path of n steps inside P_1 repeats a vertex, and the repeated segment is a σ-consistent cycle inside
P_1 that Odd can follow forever, a play consistent with σ with maximal priority 1, contradicting that σ wins from u ∈ W_E.
Claim: u ∈ Y_{r(u)} for the approximants of Φ(W_E). Induction on r(u): every σ-move from u (if u ∈ V_E) or every move (if
u ∈ V_O) leads to a vertex w ∈ W_E (σ-consistent plays stay in W_E) with w ∈ P_2, or w ∈ P_1 and r(w) ≤ r(u) − 1, so w ∈ (P_2 ∩
W_E) ∪ (P_1 ∩ Y_{r(u)−1}) by the induction hypothesis, hence u ∈ Y_{r(u)}. So W_E ⊆ Φ(W_E), W_E is a post-fixpoint of Φ, and
W_E ⊆ νZ.Φ(Z) = Z*. ∎
The SLP: Z_0 = V; for i = 1..n: Y_0 = ∅, Y_j = Cpre_E((P_2 ∩ Z_{i−1}) ∪ (P_1 ∩ Y_{j−1})) for j = 1..n, Z_i = Y_n; output Z_n.
Each monotone chain over ≤ n vertices has ≤ n strict steps, so Y_n = Φ(Z_{i−1}) and Z_n = Z*. n·n Cpre gates. ∎
Machine check: experiments/lower/check_vs_zielonka.py (b90c514): 0 mismatches against the harness Zielonka on every Büchi
game with ≤ 3 vertices (both players), all 810 000 one-player games with 4 vertices, every 13th of the 12 960 000 two-player
games with 4 vertices, and (vec5.py) all 916·10^6 one-player games with 5 vertices.

**Transfer 2.4 (ANP, LIPIcs.CSL.2021.9).** ANP evaluate θ_d x_d ... θ_1 x_1 . f(x_1, ..., x_d) for a monotone black-box
f : (B^n)^d → B^n by the two-tree recursion ‖F‖_{U,V} (their §3.1, cases (1)-(3), p.9:5; their d is the arity, our p + 1).
Lemma 3.2 (verbatim): "There is an algorithm that computes ‖F‖_{U,V} using |U|·|V| queries to the function f." Lemma 3.1: if U, V
are (n, |Θ|_μ)- and (n, |Θ|_ν)-universal then ‖F‖_{U,V} = ‖F‖. Prop. 2.5: S_{n,h} is (n, h)-universal with n^{lg(h/lg n)+O(1)}
leaves. p.9:2 and p.9:9 state the resulting symmetric bound n^{2·lg(d/lg n)+O(1)} explicitly.
  Reading into SLPs: the recursion is straight-line (the sequence of queries and their arguments depend only on U, V, Θ,
  never on answers; the restrictions f_{A,B}(x) = A + B ∗ f(x) are free Boolean gates). For a parity game with priorities
  bounded by p take Θ = ⟨θ_p, ..., θ_0⟩, θ_q = ν for even q and μ for odd q, and g(x_0, ..., x_p) = ∪_q (P_q ∩ Cpre_E(x_q)),
  monotone, p + 1 Cpre gates per query. Its nested fixpoint is W_E: Emerson-Jutla FOCS 1991 (cited by ANP p.9:3 as [10];
  not opened), stated in TARGET's max-parity convention as formula (1), p.19 of Bradfield-Walukiewicz, "The mu-calculus and
  model-checking", Handbook of Model Checking (author copy, opened; unnumbered display after Theorem 7, with the typo
  γ(Z_0..Z_d) for γ(Z_0..Z_{2d+1})), and as the numbered automata form Emerson-Jutla-Sistla TCS 258 (2001) Theorem 3.2 /
  Lemma 3.5 (opened). Universality for n' ≤ n vertices follows from universality for n. Hence
    C(n, p) ≤ (p + 1) · |S_{n,h_μ}| · |S_{n,h_ν}| ≤ n^{2·lg(p/lg n) + O(1)}, with h_ν = ⌊p/2⌋ + 1, h_μ = ⌈p/2⌉.
  With f'(x) = Cpre_E(∪_q (P_q ∩ x_q)) (priority of the successor) each query is ONE Cpre gate; its nested fixpoint is also
  W_E (the play's priority sequence is shifted by one position, which does not change its limsup; the Büchi case is (†) above);
  this removes the factor p + 1 and changes no exponent. Machine check (R-L1 §3 and experiments/lower/check_vs_zielonka.py):
  the g-form SLP with S trees agrees with Zielonka on all 74 088 games with 3 vertices and priorities {0, 1, 2} and on every
  101st of the 65 610 000 four-vertex ones; cost (p + 1)·|U|·|V| exactly.
  CAUTION (confirmed by R-L1 and L-LIT T9; T7 amended): ANP's bound n^{lg(d/lg n)+O(1)} (Cor. 3.7) rests on Lemma 3.6, whose
  proof is "a standard worklist algorithm" that re-evaluates "only ... those equations in which at least one variable was
  modified in the previous stage": ADAPTIVE. A non-adaptive round-robin evaluation of the same |V| monotone equations needs at
  most 1 + n·|V| stages of |V| queries, again n^{2·lg(p/lg n)+O(1)}. CDHS arXiv 1909.04983 Algorithm 1 is a worklist too. So the
  best exponent DERIVABLE non-adaptively from the opened sources is 2·lg(p/lg n) + O(1); whether lg(p/lg n) + O(1) is attainable
  non-adaptively is open. ANP Theorem 5.1 / Remark 5.5 apply only to programs of the shapes ‖·‖_{U,V}, ‖·‖_V, not to Def. 1.3.

**Known picture (this model), p ≥ 2:** 2n − 2 ≤ B_1(n) ≤ B_2(n) ≤ n^2 and 2n − 2 ≤ C(n, p) ≤ n^{2·lg(p/lg n)+O(1)}.
Exact values (docs/lower/L1-report.md): B_1(1..5) = 0, 2, 4, 6, 8 = 2n − 2 (n ≤ 4 by chain programs, n = 5 by a non-chain
witness verified on all 916·10^6 five-vertex games), and the depth-(2n − 1) bisimulation type determines W_E on one-player Büchi
games with ≤ n vertices (report, Theorem B).

## 3. Targets (precise statements; nothing proved)

**T-L1 (headline; L-LIT's T7-1', strong form; finding 5).** There is ε > 0 such that B_1(n) ≥ n^{1+ε} for all sufficiently large n.
In words: every straight-line symbolic program (Def. 1.3, R1-R6) that outputs Even's winning region on every one-player Büchi
game with at most n vertices uses at least n^{1+ε} Cpre gates.
Weak form T-L1w: B_1(n) ≠ O(n), i.e. limsup B_1(n)/n = ∞ (strictly weaker than ω(n), which would be lim B_1(n)/n = ∞).
Consistency: 2n − 2 ≤ B_1(n) ≤ n^2, so ε ≤ 1 and nothing in §2 excludes either form. The data of docs/lower/L1-report.md
(B_1(n) = 2n − 2 for n ≤ 5) stands against T-L1; the target is kept as the statement to prove or refute, and the report's
working hypothesis is the opposite: B_1(n) = 2n − 2 for all n.

**Why it would matter (finding 6).** Def. 1.3 differs from CDHL's model in three ways at once: (a) non-adaptive, (b) vertex-
anonymous (CDHL allow singleton sets; their p.2 remark reads the whole graph with 2n one-step operations), (c) no Post. In
CDHL's model one-player Büchi costs O(n) one-step operations (their §4.2, p.10, verbatim "O(min(SCC + D, |T|·D))", with SCC =
O(n) by [GPP08]); that algorithm uses (b) and (c). T-L1 would therefore separate the SLP model from CDHL's, not isolate
non-adaptivity. Where the super-linearity would have to come from: in ANY model with vertex naming and unrestricted Boolean
post-processing, n singleton Pre queries read the adjacency matrix, so no ω(n) bound exists there, adaptive or not; a bound
for SLPs must use R2 (anonymity) together with the pointwise (per-vertex) Boolean post-processing of R4. It would be the first
super-linear symbolic lower bound for an ω-regular objective in an anonymous model (L-LIT T7: none found; L-LIT to check the
matrix-vector query model, R-L1 gap G6).

**T-L2 (stretch; L-LIT's T7-1).** B_2(n) = Ω(n^2 / polylog n), ideally already B_1(n).
**T-L3 (the rank-2 goal, for later).** C(n, p) ≥ n^{lg(p/lg n) − O(1)}: ANP Theorem 5.1 for arbitrary SLPs.

REFEREE: items changed in v2: 1.0 (findings 1, 2), Lemma 1.5 proof (9), Transfer 2.2 (G3, 8), Lemma 2.3 proof of (†) (3, G2),
experiment cites now at b90c514 (4), T-L1 quantifiers (5), "why it would matter" (6), "known picture" hypothesis p ≥ 2 (7),
sources for the nested fixpoint (8). New and unrefereed: Lemma 2.1' and the report.

## 4. Proof routes and the known obstructions (sketch; details in docs/lower/L1-report.md)
- Depth is capped: Lemma 2.1' and the report's Theorem B give 2n − 2 ≤ minimal depth ≤ 2n − 1. So Lemma 1.6 (locality) alone
  can never give more than 2n − 1 gates; a super-linear bound must count gates at bounded depth.
- Two-party communication (CDHL's method) is capped at Θ(n) on Reduction 3.9 (two bits per operation, Θ(n) bits of
  communication complexity). A super-linear bound would need a family where every Cpre still costs O(1) bits but the problem
  costs ω(n) bits, or a different measure (R-L1: with vertex naming no such family exists; anonymity must be used).
- Candidate measure: by Lemma 1.5 a program with c Cpre gates is a modal formula DAG with c diamonds; T-L1 is a DAG-size lower
  bound for "there is a path with ≥ n visits to P_2" on ≤ n-vertex graphs. The exact minima for n ≤ 4 are reached by chains
  s_i = ◇f_i(P_2, s_{i−1}) whose output combines distance-profile and two-visit bits (report §3), i.e. by pigeonhole witnesses
  tuned to n; whether such chains exist for all n is exactly the question.
