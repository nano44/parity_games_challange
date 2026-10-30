# T56: path algebras (dioids, k-stability, Bellman-Ford / label-correcting over semirings, algebraic routing) against the VJ path-set valuation and BIP-POLY
L-LIT successor T54/T55/T56 (Opus 5.5), D18. Lead's brief 2026-10-30 15:45Z (T56, algebra × SI): L-NEW 38's BIP (docs/new/N5-ONEP-box88.md,
N5-BIP-box89.md) read as label-correcting in G_ρ with a τ-optimiser order. Written 2026-10-30 15:46Z-16:20Z (date -u). Working note,
unrefereed, not a TARGET.md claim. G-N5-TIME, BIP-POLY, BIP-REL-1, [P-INT] stay OPEN.
Labels as in T54: PROVED-in-source / SECONDARY / PROVED (L-LIT, elementary, unrefereed) / READING / DATA / OPEN.

## Summary
- (b) PROVED (L-LIT, elementary). Fix the cycle node c. On simple paths to c, the VJ valuation (c, P, ℓ) with SPEC S1's order is
  order-isomorphic to an integer weight φ = (2n+1)·Σ_{u∈P} ±2^rank(u) ± ℓ, and φ is ADDITIVE along paths with fixed vertex weights.
  - So the one-player fixed-cycle-node valuation is the max-plus dioid (ℤ ∪ {−∞}, max, +), with vertex weights of n + O(log n) bits.
  - Every element of that dioid is either 0-stable (a ≤ 0) or k-stable for NO k (a > 0). "k-stable for some k = poly(n)" therefore
    collapses to "0-stable", i.e. "no improving circuit".
  - On a W-optimal component (inside a W-run, against τ) every circuit is 0-stable (Lemma CIRC). In G_ρ during BIP, circuits that would
    change the cycle node are positive, i.e. absorbing, i.e. not stable.
  - The full VJ valuation, with the cycle node as first coordinate, is not a semiring path weight at all: the cycle node depends on where
    the play closes.
- (a) Definitions and theorems (opened: Minoux 1976, Mohri 2002, Rote 1989, Sobrinho 2005, Daggitt-Gurney-Griffin 2021, Daggitt-Griffin
  2018). With no 0-absorbing circuit, A* = A^(N−1), and Jacobi / Ford sweeps converge in ≤ N − 1 (K) SWEEPS (Minoux Thms 2, 4, 5). These
  bounds are algebraic and independent of weight magnitudes, but for the max-plus dioid they say no more than the numeric Bellman-Ford
  pass bound for REAL weights (T54 §3).
- (c) No opened source bounds the number of relaxations under an ARBITRARY (adversarial) order in a k-stable or 0-stable dioid.
  - Mohri Thm 1: any queue discipline terminates, with ≤ card(P_k(q)) updates per vertex, «exponential».
  - Minoux's generalised Moore algorithm («sélectionner un sommet quelconque»): convergence only.
  - Algebraic routing counts synchronous ROUNDS: ≤ n² for strictly increasing algebras (Daggitt-Griffin ICNP 2018 Thm 1). Event counts
    are «exponential … in the worst case» (Karloff SODA 2004, SECONDARY there).
  - By (b), Shier-Witzgall's exponential LIFO instances (T54 §3.1: nonnegative integer lengths ~2^n) have the right type for the parity
    dioid. So stability cannot give BIP-POLY. Any bound must come from the τ-optimiser order: a property such as L-NEW's BIP-REL-1, the
    Goldfarb-Hao-type arc re-entry rule of T54 §1.7.
- The Lead's premise «stability … defeats the 2^rank weights» holds for SWEEP counts, where it buys exactly what the real-weight theory
  already gives (n − 1 passes). It does not hold for arbitrary-order counts, where the algebraic theory is as exponential as the numeric one.

## 1. (a) Definitions and theorems
### 1.1 Minoux, "Structures algébriques généralisées des problèmes de cheminement dans les graphes", RAIRO-RO 10(V2) (1976) 33-62: OPENED (numdam.org RO_1976__10_2_33_0.pdf, sha256 9f41d65c…, pp. 38-53; OCR loses formulas, which are reconstructed from the text)
- p-regular (p. 38): h^(k) := e ⊕ h ⊕ … ⊕ h^k; «un endomorphisme h ∈ H est p-régulier si» h^(p) = h^(p+1). Then h* = h^(p).
- No p-absorbing circuit (p. 39): «G est sans circuit p-absorbant si et seulement si l'endomorphisme t(γ) … associé à chaque circuit γ de
  G est p-régulier». p = 0: t(γ) ⊕ e = e (0-stable, "absorptive" circuits).
- Theorem 2 (p. 39): no 0-absorbing circuit ⇒ A^(k) sums over elementary paths with ≤ k arcs, and «A* = lim A^(k) = A^(N−1)».
- p ≥ 1 (p. 40): no general finite bound, «La cardinalité des chemins … ne peut en effet être bornée». Theorem 3 (Gondran 1974):
  commuting endomorphisms give K = v·p·N + N − 1, with v = the number of elementary circuits (can be exponential).
- K-stable (p. 41): «h1⊗h2⊗…⊗hK = h_ε». Theorem 4: A* = A^(K).
- Generalised Bellman (Jacobi), p. 47: «Si on a : A^(K) = A*, alors l'algorithme converge en K étapes au plus.» Theorem 5 (p. 48):
  generalised Ford (a Gauss-Seidel sweep over all arcs) «converge en K itérations au plus».
- Generalised Moore (A2), pp. 49-50: «sélectionner un sommet quelconque». Only convergence, «plus rapide (moins de marquages)». NO count.
- Theorem 6 (p. 53): generalised Dijkstra, N iterations under (H2)-(H4).
### 1.2 Mohri, "Semiring frameworks and algorithms for shortest-distance problems", JALC 7(3) (2002) 321-350: OPENED (cs.nyu.edu/~mohri/pub/jalc.pdf, sha256 1d609fa6…, preprint pp. 3-20)
- Definition 6 (p. 5): «A semiring … is k-closed if: ∀a ∈ K, ⊕_{n=0}^{k+1} a^n = ⊕_{n=0}^{k} a^n». k = 0: 1 ⊕ a = 1. Definition 8 (p. 8):
  k-closed for G (cycle weights only). P_k(q) = paths from s to q with at most k occurrences of a cycle.
- Theorem 1 (p. 13): if K is k-closed for G, the Generic-Single-Source-Shortest-Distance algorithm terminates with d[q] = δ(q). The proof
  bounds the relaxations at q by card(P_k(q)). p. 14: «vertices can be extracted from S in any chosen order and this won't affect the
  correctness of the algorithm or its termination». pp. 14-15: «since the number of simple paths from s to q may be exponential …, the
  complexity of the algorithm is exponential». Topological order: linear on acyclic graphs (Theorem 2). FIFO = Bellman-Ford only for the
  tropical semiring (p. 20).
### 1.3 Rote, "Path problems in graphs" (preprint April 1989; Computing Suppl. 7 (1990) 155-189 not opened): OPENED (page.mi.fu-berlin.de/rote, sha256 28b94592…, pp. 9, 18, 24)
- §5.2 (p. 18): x^[l] = (I ⊕ A ⊕ … ⊕ A^l)e_j. «If the iteration does not converge after n steps, we know that there is a negative cycle.»
  For idempotent semirings Gauss-Seidel «never needs more iterations than the Jacobi algorithm». Sweep counts only.
### 1.4 Algebraic routing
- Sobrinho, "An algebraic theory of dynamic network routing", IEEE/ACM ToN 13(5) (2005) 1160-1173: OPENED (sha256 485afb23…, pp. 1160,
  1164-1165).
  - Theorem 1: «In a free network, the path-vector protocol converges to local-optimal in-trees.»
  - Theorem 3: «If the algebra is monotone, then the path-vector protocol can be made to converge … whatever the network.»
  - No rate.
- Daggitt-Gurney-Griffin, arXiv 2106.01184v2 (SIGCOMM 2018 extended): OPENED (sha256 5a96dd3d…, pp. 2-3, 11-15).
  - Definitions: Def 19 distributive f(x ⊕ y) = f(x) ⊕ f(y); Def 20 increasing x ≤⊕ f(x); Def 21 strictly increasing x ≠ ∞ ⇒ x <⊕ f(x).
  - Theorems 3, 5: convergence under arbitrary asynchronous schedules (strictly increasing, finite S; increasing path algebras). No rate.
  - p. 15: «Θ(n) … distributive, strictly increasing», «Θ(n²) … non-distributive, strictly increasing» (SECONDARY there).
- Daggitt-Griffin, "Rate of convergence of increasing path-vector routing protocols", ICNP 2018 335-345: OPENED (cl.cam.ac.uk/~tgg22,
  sha256 376beef0…, pp. 1-3, 7, 11).
  - Theorem 1 (p. 11): «For any strictly increasing path algebra … σ converges in at most n² iterations from every starting state X».
  - Counted: SYNCHRONOUS iterations σ(X) = A(X) ⊕ I. Lower-bound family: n²/4 − n/2 + c.
  - p. 1: «a simple shortest-paths path-vector protocol may require an exponential number of events to occur in the worst case»
    (Karloff, SODA 2004, NOT OPENED).
### 1.5 NOT OPENED
Gondran-Minoux, Graphs, Dioids and Semirings (Springer 2008; the chapters served a JavaScript challenge page); Carré 1971 (OUP 403) and
1979; Griffin-Sobrinho Metarouting 2005 (404); Sobrinho SIGCOMM 2003; Karloff SODA 2004; Baras-Theodorakopoulos.

## 2. (b) Is the VJ / N5 path-set valuation a dioid, and is it k-stable? (PROVED, L-LIT, elementary)
Setting: SPEC S1. rank, p′, reward as in S1. Even's one-player arena against a fixed Odd strategy (τ, or ρ in BIP). For a fixed cycle node
c, the valuations of simple paths x → c are (c, P, ℓ): P = the vertices of the path more relevant than c (rank > rank(c)), ℓ = the length.
S1's order compares P by S(P) := Σ_{u∈P} (+2^rank(u) if Ω(u) even, −2^rank(u) if odd), then ℓ (longer better for Even if c is odd,
shorter if c is even).
- Lemma ISO. Let s_c := +1 if Ω(c) is odd, −1 if even, and φ(c, P, ℓ) := (2n+1)·S(P) + s_c·ℓ. Then for valuations with the same cycle
  node c and ℓ ≤ n:
  - (i) (c, P, ℓ) is better for Even than (c, P′, ℓ′) iff φ > φ′;
  - (ii) prepending a vertex u ∉ P to the path (si.py Engine.extend) adds the fixed weight w_c(u) := (2n+1)·[rank(u) > rank(c)]·
    (±2^rank(u)) + s_c.
  - Proof. (i) S is an integer and |s_c ℓ − s_c ℓ′| ≤ n < 2n + 1, so φ orders lexicographically by (S, s_c ℓ), which is S1's order.
    (ii) extend adds u to P iff u is more relevant than c, and adds 1 to ℓ; S is additive over disjoint unions. □
- Corollary DIOID. Per fixed c, best-path valuation is the path problem of the max-plus dioid (ℤ ∪ {−∞}, max, +) with vertex weights w_c(u)
  of |w_c(u)| ≤ (2n+1)·2^n + 1, i.e. n + O(log n) bits. That dioid is selective and its ⊗ is a group, so for every element a:
  - if a ≤ 0 = e, then e ⊕ a = e: a is 0-stable (Mohri k = 0, Minoux p = 0);
  - if a > 0, then a^k strictly increases, and a is not k-stable for any k.
  - So "k-stable for some k = poly(n)" holds iff it holds for k = 0, iff no circuit has positive φ-weight.
- Lemma CIRC. Let E′ be a set of Even edges such that W (the valuation of some σ ⊆ E′ against τ) is optimal for Even over E′ against τ.
  Examples: E′ = OPT_W (G_I's Even edges), or the arena of a W-flat S4a step. In the c-component {x : λ_W(x) = c}, every circuit Γ of
  E′-edges and τ-edges avoiding c has Σ_{u∈Γ} w_c(u) < 0. So every circuit is 0-stable.
  - Proof. Let g be the most relevant vertex of Γ. Following Γ forever from a vertex of Γ is available over E′, with cycle node g ≠ c.
    W is optimal at that vertex, and ranks are injective, so reward(g) < reward(c).
  - If rank(g) > rank(c): S(Γ) has the sign of g's parity, and |S| ≥ 2^rank(g) − Σ_{r<rank(g)} 2^r ≥ 1. Since reward(g) ≤ reward(c) and
    g is more relevant than c, g is odd, so S < 0 and φ(Γ) ≤ −(2n+1) + s_c·|Γ| < 0.
  - If rank(g) < rank(c): φ(Γ) = s_c·|Γ|. If c is odd then s_c = +1, but every g less relevant than an odd c has reward(g) > reward(c)
    (an even g has positive reward; an odd g has −p′(g) > −p′(c)). That contradicts optimality, so this case does not occur. If c is even,
    φ(Γ) = −|Γ| < 0. □
- Consequences.
  - Inside a W-run (τ fixed, W optimal against τ on the arena σ ∪ offers; S4a), the fixed-c path problem is a 0-stable max-plus instance.
    Minoux Thm 2 gives A* = A^(N−1), the n − 1 sweep bound: T54's Bellman-Ford, and box 88's NO-DEV / GP* epochs of n − 1.
  - In G_ρ (BIP offers judged by val(σ, ρ), with ρ ≠ τ and σ not optimal against ρ), a circuit whose most relevant vertex is better for
    Even than the current cycle node has positive φ-weight, i.e. it is 0-absorbing and not k-stable for any k. In the label-correcting
    reading, such circuits are exactly the cycle-node changes. A semiring path weight cannot represent them; SI handles them by closing
    the play.
  - The full valuation (c, P, ℓ) is not a semiring path weight: concatenation does not determine c. Only the fixed-c restriction is a dioid.
  - G_I itself (two players, Odd keeps all edges; Ξ = Even's value against Odd's best reply) is a min-max path problem, not a semiring path
    problem. The dioid applies to the one-player W and to val(·, ρ) for fixed ρ (BIP), not to Ξ in general.

## 3. (c) Arbitrary but monotone relaxation order in a k-stable dioid
- Opened bounds: none for an arbitrary order. Mohri Thm 1: ≤ card(P_k(q)) per vertex, «exponential». Minoux A2: convergence only.
  Routing: synchronous rounds only. ICNP 2018 Thm 1 gives n² rounds for strictly increasing algebras, and the parity dioid is not
  increasing (w_c(u) > 0 for even relevant u). Event counts are exponential (Karloff, SECONDARY).
- READING (not checked step by step). By Corollary DIOID, every integer label-correcting instance with weights of n + O(log n) bits and no
  positive circuit has the type of a one-player parity instance with fixed c: one odd vertex of distinct rank per weighted arc, and ranks
  spaced so that F = 8 in Shier-Witzgall's G_n, e.g. a_i = 2^(3i), c_i = 2^(3i+1), b = 0, which meets their Lemma 3 hypotheses F ≥ 2,
  c > a + b, c > a. So LIFO-order label-correcting over the parity dioid is exponential, and no algebraic stability property can rule
  that out.
- What BIP-POLY needs therefore is a property of the ORDER, not of the algebra. BIP is not stale-label label-correcting: labels are
  recomputed exactly, as in network simplex for shortest paths (T54 §3.4). Its order is the τ-optimum of σ ∪ ρ-offers. Candidate
  properties:
  - L-NEW's CONJECTURE BIP-REL-1 (each Even edge is released at most once per frozen stretch). This is the analogue of Goldfarb-Hao's
    arc re-entry rule (T54 §1.7), which is what makes their max-flow simplex nm.
  - A pass property PASS-BIP (T54 §3.4).
  - Neither is in the opened literature for adversarial orders.

## 4. Table (the brief's (a)-(d))
| source (opened unless marked) | (a) definition / theorem | (b) hypothesis | (c) does the parity / N5 valuation meet it? | (d) bound for BIP / [P-INT] |
| --- | --- | --- | --- | --- |
| Minoux 1976 Thm 2 | no 0-absorbing circuit ⇒ A* = A^(N−1) | 0-stable circuits | yes, inside a W-run per fixed c (CIRC); no in G_ρ before optimality | N − 1 sweeps (Jacobi), = numeric Bellman-Ford |
| Minoux 1976 Thm 4, 5 | K-stable ⇒ A* = A^(K); Ford sweeps ≤ K | K-stability | k-stable ⇔ 0-stable here (DIOID) | as above |
| Minoux 1976 A2 (Moore) | arbitrary vertex selection | 0-stable | yes | convergence only, no count |
| Mohri 2002 Def 6, 8, Thm 1 | k-closed; generic algorithm, any queue | k-closed for G | yes (k = 0) on W-optimal components | ≤ card(P_k(q)) per vertex: exponential |
| Rote 1989 §5.2 | Jacobi / Gauss-Seidel sweeps | idempotent semiring | yes | ≤ n sweeps |
| Sobrinho 2005 Thm 1, 3 | free networks / monotone algebras converge | monotone (increasing) | no (w_c(u) > 0 for even relevant u) | convergence only |
| Daggitt-Gurney-Griffin 2021 Thm 3, 5 | asynchronous convergence | (strictly) increasing | no | none |
| Daggitt-Griffin 2018 Thm 1 | ≤ n² synchronous rounds | strictly increasing | no | none; events exponential (Karloff, SECONDARY) |
| Gondran-Minoux 2008; Carré 1971 (NOT OPENED) | — | — | — | — |
| this note §2 | ISO, DIOID, CIRC | — | fixed-c one-player valuation = max-plus over ℤ, n-bit weights | stability = "no improving circuit"; nothing beyond numeric theory |

## DONE / FINDINGS / NEEDS
- DONE: this note; notes/L-LIT.md (sources).
- FINDINGS:
  1. PROVED (L-LIT, elementary): ISO, DIOID, CIRC.
     - With c fixed, the VJ valuation is the max-plus dioid over ℤ with n-bit vertex weights. k-stability collapses to 0-stability ("no
       improving circuit").
     - That holds on W-optimal components inside a W-run, and fails exactly at cycle-node improvements in G_ρ.
     - The full valuation is not a semiring path weight, and Ξ (two players) is not a dioid path problem.
  2. (a) Minoux 1976 Thms 2, 4, 5: N − 1 / K sweeps (Jacobi, Ford). Mohri 2002 Def 6 and Thm 1: any queue order terminates with ≤
     card(P_k(q)) updates, exponential.
  3. (c) No opened source bounds adversarial-order relaxation counts in a stable dioid. Routing bounds are in synchronous rounds (n²,
     strictly increasing; not our algebra). READING: Shier-Witzgall's LIFO instances fit the parity dioid. BIP-POLY must come from the
     τ-optimiser order (BIP-REL-1 / PASS-BIP), not from algebra.
- NEEDS: none from the owner. Optional (owner, library access): Gondran-Minoux 2008 ch. 4, Carré 1971, Karloff SODA 2004.
