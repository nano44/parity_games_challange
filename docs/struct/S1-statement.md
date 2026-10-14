# S1: deterministic weak separators, exact statement (L-STRUCT, 2026-10-14)

Status: statement only, written before any proof or computation (TARGET.md §7e). Every source below was opened by
L-STRUCT; theorem numbers are recorded in notes/L-STRUCT.md "Sources opened". CDFJLP = Czerwiński, Daviaud, Fijalkow,
Jurdziński, Lazić, Parys, arXiv 1807.10546v2. CFGO = Colcombet, Fijalkow, Gawrychowski, Ohlmann, arXiv 2104.05262v8.
KV = Kozachinskiy, Vyalyi, arXiv 1902.07175v3. Nothing here is a result; §5 lists what would be one.

## 1. Vocabulary (TARGET.md §1, with the one translation needed)
- A parity game is G = (V, V_E, V_O, E, pr) as in TARGET.md §1: E ⊆ V × V, every vertex has a successor, pr : V → {0..n},
  max-parity, Even wins a play v0 v1 ... iff the largest priority occurring infinitely often is even.
- The priority word of a play is pr(v0) pr(v1) pr(v2) ... (one letter per visited vertex).
- Letters. CDFJLP read edge priorities from Σ_d = {1, ..., d}, d even (§2.1: "its priority π(e) is a positive integer, and
  we use d to denote the smallest even number that priority of no edge exceeds"; §3.1: "each move — in which an edge e is
  followed — is encoded by the letter π(e)"). We keep Σ_d = {1..d} as the alphabet but allow any d ≥ 1; d here is the
  largest letter, NOT TARGET's d = |pr(V)|.
- Translation of a TARGET game: set π(u, v) = pr(u) + 2 on every edge. Then the edge word of a play equals the vertex word
  shifted by +2, parity and order are preserved, and priorities lie in {2..n+2} ⊆ Σ_{n+2}. So CDFJLP's setting contains
  TARGET's; the converse fails (an edge-labelled graph need not have all out-edges of a vertex equally labelled), which is
  why two conventions are kept below. Lemma 2(c) handles the letter 0 / neutral letter of CFGO.

## 2. Definitions
D1 (labelled graphs). An edge-labelled Σ_d-graph is H = (V, E) with E ⊆ V × Σ_d × V (CFGO §2.1 convention: parallel edges
with distinct labels are allowed; CDFJLP §2.1 give one priority per edge and E a set of edges, which is a sub-case).
A vertex-labelled Σ_d-graph is H = (V, E, pr) with E ⊆ V × V and pr : V → Σ_d; its edge (u, v) carries the label pr(u).
A vertex-labelled graph is an edge-labelled graph; the class is strictly smaller.
Words(H) = { labels of infinite paths of H } ⊆ Σ_d^ω (paths from any vertex; sinks contribute nothing).

D2 (even and odd graphs; CDFJLP §2.1, CFGO Lemma 6.1). A cycle is even if the largest label on it is even, odd otherwise.
H is even if all its cycles are even, odd if all its cycles are odd.

D3 (languages). For X ∈ {E, V} (edge- or vertex-labelled) and n ≥ 1, d ≥ 1:
  EvenCycles^X_{n,d} = ∪ { Words(H) : H an even X-labelled Σ_d-graph with at most n vertices },
  OddCycles^X_{n,d}  = ∪ { Words(H) : H an odd  X-labelled Σ_d-graph with at most n vertices },
  LimsupEven_d = { w ∈ Σ_d^ω : limsup w even }, LimsupOdd_d = its complement.
EvenCycles^E is CDFJLP's EvenCycles_{n,d} (§3.1, quoted in docs/lit/T4-weak-separators.md §1). Inclusions:
EvenCycles^V ⊆ EvenCycles^E ⊆ LimsupEven_d and OddCycles^V ⊆ OddCycles^E ⊆ LimsupOdd_d.

D4 (automata; CDFJLP §3.2). A deterministic safety automaton is A = (Q, q0, δ) with δ : Q × Σ_d → Q ∪ {⊥}, ⊥ ∉ Q the
rejecting sink. L(A) = words whose run from q0 never reaches ⊥. The size |A| is |Q| (⊥ is not counted; this matches CFGO,
where a separating automaton is a graph and missing edges reject, and CDFJLP Lemma 5.1, which maps leaves to
non-rejecting states).

D5 (separators; CDFJLP §3.3 verbatim: "an automaton A is an (n, d)-separator if it is a separator of EvenCycles_{n,d}
and OddCycles_{n,d}; and ... a strong (n, d)-separator if it is a separator of EvenCycles_{n,d} and LimsupOdd_d").
For X ∈ {E, V}:
  A is a weak (n, d)-separator (convention X)   iff EvenCycles^X_{n,d} ⊆ L(A) and L(A) ∩ OddCycles^X_{n,d} = ∅;
  A is a strong (n, d)-separator (convention X) iff EvenCycles^X_{n,d} ⊆ L(A) ⊆ LimsupEven_d.
  w^X(n, d) = min { |A| : A a deterministic weak (n,d)-separator, convention X };
  s^X(n, d) = min { |A| : A a deterministic strong (n,d)-separator, convention X }.
"Weak" is CDFJLP's plain "(n,d)-separator"; the word weak is ours, for contrast.

## 3. Facts taken from sources (to be re-derived or cited, not assumed beyond what is quoted)
F1. Strong implies weak, so w^X ≤ s^X, and both minima exist (strong deterministic separators exist: CDFJLP Prop. 3.1,
    C_{n,d} with Θ(n^{d/2}) states, or Thm 4.1's U_{n,d}). Also w^V ≤ w^E and s^V ≤ s^E (fewer words to handle).
F2. s^E(n, d) for even d equals the least number of leaves of an (n, d/2)-universal tree: CFGO Thm 4.1 (smallest
    deterministic (n,Ω)-separating automaton = smallest (n,Ω)-universal graph, Ω positional, prefix-independent, with a
    neutral letter) + Lemma 6.8 ((n, Parity_{2h})-universal graphs and (n,h)-universal trees have the same smallest size)
    + Thm 6.2 (parity qualifies). CFGO's alphabet is [0, d]; Lemma 2(c) below removes the letter 0. Bounds: CFGO Thm 6.9,
    Prop. 6.10 (upper recursion f), Prop. 6.11 (lower recursion g). Exact small values are not given there.
F3. Lower bound, strong only: CDFJLP Thm 5.1: every non-deterministic safety strong (n,d)-separator has at least
    C(⌊lg n⌋ + d/2 − 1, ⌊lg n⌋) states. CDFJLP §3.3: "our proof of the quasi-polynomial lower bound in Section 5 only
    applies to strong (n, d)-separators"; §6 leaves the weak case open (quoted in T4 §1).
F4. Use (CDFJLP Prop. 3.2, verbatim): "If G is a parity game with n vertices and priorities up to d, and if A is a
    deterministic safety (n, d)-separator, then Even has a winning strategy in G if and only if she has a winning strategy
    in the chained-product safety game G ⊲ A." The proof uses only (i) acceptance of the words of Even's positional
    strategy subgraph (an even graph with ≤ n vertices) and (ii) rejection of the words of Odd's (an odd graph).
F5. Only known weak lower bound (KV Thm 2): a DFA separating EvenCycles_{n,2} from OddCycles_{n,2} "in time t" has
    exp(Ω(n^5/t^4)) states. KV's model differs from D4/D5 in three ways: letters are (vertex, priority) pairs; acceptance
    is reaching q_accept (so, as a safety automaton with ⊥ = q_accept, it accepts OddCycles and rejects EvenCycles: the
    roles are swapped, which the shift p ↦ p+1 undoes); and the time bound t. KV p.6: "Even super-linear lower bounds for
    unrestricted separation automata are not known."

## 4. Elementary lemmas needed before the questions make sense (L-STRUCT, proofs to be written in S1-notes; refereed later)
Lemma 1 (regions). For a TARGET game G, a deterministic weak (n, n+2)-separator A of convention V, and v ∈ V:
  v ∈ W_E(G) iff Even wins the safety game G ⊲ A from (v, q0). Proof sketch: restrict F4's argument to the trap W_E
  (Even's positional strategy on W_E yields an even vertex-labelled subgraph on W_E) and to W_O for Odd.
Lemma 2 (invariances). (a) w^X(n,d) and s^X(n,d) are non-decreasing in n and in d. (b) Adding the neutral letter 0
  (CFGO alphabet [0,d]) changes neither w^E nor s^E: extend δ(q,0) = q; contracting 0-edges maps paths of even/odd
  [0,d]-graphs with ≤ n vertices to paths of even/odd Σ_d-graphs with ≤ n vertices. (c) Hence F2 applies to Σ_d.
Lemma 3 (shift). Replacing every label p by p+1 swaps even and odd graphs; so w^X(n,d) for "accept Odd, reject Even"
  over Σ_d equals w^X(n,d) for "accept Even, reject Odd" over {2..d+1}. This is how F5's model is compared with ours.

## 5. The questions (each answer is a candidate M3 or M4 item; none is claimed)
Q1 (separation of the two notions). Is there (n, d) with w^E(n,d) < s^E(n,d)? With w^V(n,d) < s^V(n,d)?
  Deliverable: the table of w^X(n,d), s^X(n,d) for n ≤ 4 (then 5) and d ≤ 6, computed by the SAT encoding in
  experiments/weak-sep/, cross-checked by hand for n ≤ 2 and against F2 (universal-tree sizes) for s^E.
Q2 (growth). Which of the following holds?
  S1-A (would be M4 after the gauntlet, TARGET §5): there are a polynomial p and a deterministic algorithm that, on input
  (n, d), outputs in time p(n, d) a deterministic weak (n, d)-separator of convention V with at most p(n, d) states.
  By Lemma 1 and linear-time safety-game solving on G ⊲ A (n·|A| vertices, m·|A| edges), S1-A gives an algorithm meeting
  TARGET §2 with p'(n+m) = O((n+m)·p(n, n+2)) plus the cost of building A.
  S1-B (a new barrier; M3 status to be ruled, see RANKING.md preamble): for every polynomial p there are (n, d) with
  w^E(n, d) > p(n, d). Sharper target: w^E(n,d) ≥ C(⌊lg n⌋ + d/2 − 1, ⌊lg n⌋) / poly(n, d).
  S1-A and S1-B exclude each other only for convention V versus E through F1 (w^V ≤ w^E); a lower bound for w^E alone does
  not rule out S1-A. A lower bound for w^V would.
Q3 (structure; needed for either direction). Lasso condition, refereed OK (docs/referee/2026-10-14-T4-3c-lasso.md,
  on L-LIT's T4 §3(c)); usable from 2026-10-14 19:00Z (Lead). Form used here, in the REFEREE's sharpened version:
  for every reachable SIMPLE cycle C of A with odd maximum and every finite path P from q0 to C, the word
  π(P)·π(C)^ω is accepted by A, hence must lie outside OddCycles^X_{n,d}: the least number of vertices of an odd
  X-graph generating π(P)·π(C)^ω exceeds n (sharp form). The count |P| + |C| > n with P shortest is only the cheap
  necessary filter (a 3-cycle labelled 3,3,3 has |C| = 3 but 3^ω ∈ OddCycles_{1,d}). Consequences: a weak separator
  with no reachable odd simple cycle is strong; one smaller than s(n,d) has a reachable odd simple cycle whose lasso
  words are realised by no odd graph with ≤ n vertices. Determinism is not needed for the condition itself.
  Data check: the 3-state (2,6) witness (experiments/weak-sep/README.md) has exactly one odd simple cycle, 0 -5-> 2
  -4-> 1 -4-> 0, with P empty; the least odd graph generating (544)^ω has 3 vertices > 2 (each 2-vertex folding
  creates an even cycle), so the sharp form holds with margin 1.

## 6. Convention check (REFEREE finding 4 on T4 §3(b); settled here)
- CDFJLP v2 never says "one label per ordered pair". Their §5 construction of G_t puts, on every vertex v_i, "a self-loop
  ... with the even priority p" for every even p with 1 < p ≤ d: several parallel self-loops with different priorities.
  So their graphs are multigraphs; convention E (CFGO's E ⊆ V × Σ_d × V) is the literature's and is the primary one.
- S (one label per ordered pair) and V are defined explicitly in D1 so that nothing rests on the reading of §2.1.
- Effect on the values (experiments/weak-sep/results/table.md): E and S agree on every computed cell (n ≤ 3, d ≤ 6,
  weak and strong), so the parallel-edge question has not changed w or s where computed; it does change the enumerated
  maximal graphs (for (3,4): 4 even multigraphs vs 1112 simple ones). V is strictly smaller on several cells
  (s^V(4,4) = 7 < 8 = s^E(4,4); w^V(3,6) = 6 < 7 = w^E(3,6)), as Parys-Wiącek's vertex-priority remark predicts.

## 7. What is NOT a result from this lane
A SAT value is a result only after the independent checker in experiments/weak-sep/ re-verifies the automaton (SAT side)
and the UNSAT side is reproduced from the committed encoding by L-COMP or the REFEREE. A polynomial-size family found by
search is a conjecture until S1-A is proved and runs the gauntlet.
