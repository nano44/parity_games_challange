# R47: chain-keeping transitions are polynomial per q-phase on 𝒞^1P (L-RED box 15; produced on Opus 5.5)
Status: READING, unrefereed. Self-contained. Written 2026-10-19 ~01:50Z (date -u). Target: the open gap of P-C1P (REFEREE R-C1P R-2 /
REFEREE-2 R2-C1P G-R46-1): R46 §3's "S − 1 = |P|" presupposes (CHAIN-CHANGE). As both referees proved, S − 1 = |P| + I, where I is
the number of chain-keeping transitions. This file bounds I.
TARGET.md diff: a statement about A_DTL's search count (gauntlet step 4 objects) on a subclass; no definition changed; no M4 claim.
Code: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, src/solvers/dtl.cpp (line numbers below), every order datum.

## 0. Setting and what is cited
- G ∈ 𝒞_C^dist: every vertex of q = 1 − C has exactly one successor, and the q-parity priorities are pairwise distinct
  (TARGET.md §1 objects plus these class hypotheses; GAP-A-M §27b). One q-phase, G′ fixed, consecutive searches s, s + 1.
- Depth-0 chain c(s) = (state_0, …, state_m), state_j = (R_j, ρ_j, V_j, piece_j), with piece_j = R_j \ R_{j+1}, as in R46 and
  GAP-A-M §35a. A transition is CHAIN-KEEPING if c(s) = c(s+1), and CHAIN-CHANGING otherwise. |P| is the number of chain-changing
  transitions and I the number of chain-keeping ones, so S − 1 = |P| + I.
- Cited, signed:
  - RESULTS R5 (h) FDL with R8 STR-DET (both referees). Let e* be the first tangle-attractor computation (tattr) whose output
    differs between s and s+1, on the logs with s's repeated sptl passes deleted. Then e* has the same input in both searches and
    a strictly larger output in s+1, and s+1 learns no tangle before e*.
  - RESULTS R9 (a) with R8 (both referees; original constants given STR-DET). For every best_vertices context R, the e*-at-R
    transitions of a phase number at most (F_R + 1)(H + 1). H is the polynomial of RESULTS R7 (d), and F_R counts the transitions
    at R where Π_R does not rise.
  - RESULTS R11 (c): F_R ≤ 3·N*_R, where N*_R counts the visit pairs of R with a relevant steal.
  - P-C1P items signed by both referees: NOSTEAL-1P (no relevant steal in any context of a q-phase on 𝒞_C^dist), so N*_R = 0 and
    F_R = 0.
  - Attractor monotonicity, DTL-proof Lemma 1.2b as used in R9 (b): for a fixed seed, subgame and cap, a tattr's output is
    monotone in T and in the seed set.
- Proved here: Lemma EMPTY-REC (§1), Lemma NO-PIECE-E* (§2), Lemma SPTL-SANDWICH (§3), and Theorem CK (§4).

## 1. Lemma EMPTY-REC (PROVED, reading; needs only "every q-vertex has one successor")
Statement. In every search(q) of a game in 𝒞_C, every recursive call search_rec(Z, q, depth + 1) (dtl.cpp 954) has Z = ∅.
Proof. Look at the −1 threshold branch of search_rec (dtl.cpp 898-955).
- (a) Seeds. The loop at 899-911 visits the vertices in index order, which is priority order. It sets t := priority(v) only while
  Q is empty, and once Q is nonempty it breaks at the first higher priority (902-904). So every seed (a vertex with
  attracts(q, v, X, R) true) has priority exactly t.
- (b) Region. The loop at 916-921 grows Z from the seeds with attractVertices and attractTangles (player q, cap t, subgame R
  consumed). Claim: every vertex of Z has a path inside Z to a seed. The path uses, at a q-vertex, its unique edge, and at a
  C-vertex, any edge. Induction on the order in which vertices enter Z:
  - A vertex added by attractVertices(q, u, …) is a predecessor of the popped u ∈ Z (66-107). A q-vertex has u as its unique
    successor; a C-vertex has an edge to u.
  - The vertices of a tangle t added by attractTangle(t, q, …) (110-196) are added because some escape of t is in Z. Escapes
    are targets of C-edges of t (tout: the C-vertices' edges leaving t). The tangle is strongly connected using its strategy at
    q-vertices, which is the unique edge, and its C-vertices' internal edges. So every vertex of t reaches, inside t, a
    C-vertex with an edge to that escape, and so reaches Z's earlier part.
- (c) Removal. 935-940 move every vertex of Z with priority t to X and push it. Every seed is among them, by (a). Then 942-946 run
  attractVertices(1 − q, u, Z, X, Z, t) and remove each popped vertex from Z.
  - For a predecessor w ∈ Z of a popped vertex: a C-vertex w (owner 1 − q) is attracted at once.
  - A q-vertex w is attracted when none of its successors lies in Z \ X. It has one successor, the popped vertex, which is in X.
  - The cap t is no restriction, since every vertex of Z has priority ≤ t (the attractor of 916-921 has cap t).
  - So the removed set is the backward closure, inside Z, of the priority-t vertices. By (b) that closure is all of Z.
- (d) Hence Z is empty at 954. search_rec(∅) returns at once: best_vertices finds no q-vertex and returns 0 (668), and
  search_rec returns (854), with no tattr. □
Mechanical check (R42 §2, experiments/red/xctx/dagchk.py): 98 of 98 depth-≥1 calls of q-phases on L-ALG's class set have an
empty subgame. 700,000 random class games (R42 §3): 0 tangle births at depth ≥ 1 in any phase.

## 2. Lemma NO-PIECE-E* (PROVED, reading): at a chain-keeping transition, e* is not a −1 attractor; Dom steps are budgeted
Let s → s+1 be chain-keeping, and suppose e* exists. By EMPTY-REC, e* is at depth 0 in position j of the common chain.
- (i) e* is not the −1 threshold attractor of position j (916-921).
  - Its input (seeds, R_j, t) is equal in s and s+1, and its output Z is strictly larger at s + 1 (FDL).
  - Every vertex of Z leaves R_j at this iteration: R is consumed at 920; the priority-t vertices and the opponent-attracted
    vertices go to X at 935-946; and `X |= Z` at 951.
  - So piece_j = Z, which is strictly larger at s + 1: the chain changes. Contradiction.
- (ii) Dom steps are NOT excluded, but they are budgeted (Lemma DOM-MONO below).

Lemma DOM-MONO (PROVED, reading; uses distinct q-priorities). Fix a Dom call: Dom(V*, R) after a stable call (878-891) or
Dom(prevV, R) in the −1 branch without seeds (962-975), with fixed (R, X_0, V), where X_0 = G′ \ R at depth 0.
- The call loops over the tops τ_1 > τ_2 > … of V (decreasing index, which is decreasing priority because the q-parity priorities
  are distinct). It skips τ_i if τ_i ∈ X. Otherwise it sets X[τ_i] and runs a tattr that pushes only τ_i, with target X, cap
  c_i = priority(τ_i) and subgame R consumed.
- Let X_i(T) be X after step i under tangle set T.
- Claim: T ⊆ T′ implies X_i(T) ⊆ X_i(T′) for every i.
Proof. Induction on i, and inside step i on the order in which vertices join X under T. Write X_i = X_i(T) and X′_i = X_i(T′).
- A top τ_i ∈ X_i: either τ_i ∈ X′_{i−1}, or run T′ adds it at step i.
- A vertex v attracted under T at step i by the vertex rule (attractVertices, 66-107; pr(v) ≤ c_i):
  - If v is a C-vertex, all its successors in R lie in X_i; if v is a q-vertex, its unique successor does. By induction those
    successors lie in X′_i.
  - At least one of them, u, joined X during the Dom call under T, because v was triggered by a popped vertex. By induction u is
    in X′_i \ X_0, so under T′, u also joined during the call and was popped.
  - Consider, under T′, the last pop among v's successors that lie in X′_i \ X_0. It happens at some step k ≤ i, with cap
    c_k ≥ c_i ≥ pr(v). At that moment all of v's successors in R are in X′, so attractVertices adds v (or v is already in X′).
- A tangle t attracted under T at step i (attractTangle, 110-196): its vertices have priority ≤ c_i, and all its escapes are in X
  or outside the subgame. The same last-pop argument, applied to its escapes (attractTangles is triggered by a popped escape),
  shows that t is attracted under T′ at a step k ≤ i, or its vertices are already in X′. T′ ⊇ T, so t is available.
- So X_i ⊆ X′_i. □
Consequence. Along a phase T only grows, so for a fixed Dom input (R, V) the vector (X_1, …, X_{|V|}) is monotone non-decreasing
over all searches that run this call. At a transition whose e* is step i of this call, X_i strictly grows (FDL: same input,
strictly larger output). The vector has |V| ≤ n entries, each a subset of G′. So the transitions whose e* is a step of the Dom
call with input (R, V) number at most n·|V| ≤ n² per phase.
(Monotonicity does NOT give a strict change of the final piece: a vertex attracted earlier under T′ may still be attracted at a
later step under T. That is why Dom-e* transitions are budgeted rather than excluded.)

## 3. Lemma SPTL-SANDWICH (PROVED, reading): e* is not in sptl
Repeated sptl passes of s are deleted by the FDL convention. A pass k ≥ 2 of s + 1 runs only if pass k − 1 learned something
(`more`, 870-874), and s + 1 learns nothing before e* (FDL). So the remaining case is pass 1 of s + 1 at a stable position j.
- (a) Same inputs. Fix the stable call at position j. Its final best_vertices round (the one that returned 1 at 716) computes, for the tops
  a_1 > a_2 > … of V*, the regions BV(a_k): seed {a_k}, cap priority(a_k), subgame CurR, from which earlier regions were consumed
  (691-705; consumption at 699).
  - sptl pass 1 (481-499) computes, for the same tops in the same order, regions SP(a_k): seed {a_k}, cap priority(a_k), subgame
    R, from which earlier regions were consumed (490).
  - The skip tests agree: BV skips a top that lies in an earlier region (`!Z[top]`, 692); SP skips a top that is no longer in R
    (482), that is, one consumed by an earlier region.
  - The attraction calls are the same (attractVertices and attractTangles with player q, the same cap, subgame = target
    complement).
  - So if the regions of a_1 … a_{k−1} agree, the inputs for a_k agree. Write f_k(T) for the output as a function of the tangle set.
- (b) The tangle sets. Let T^j_s be the tangles of s when it reaches position j.
  - BV at s uses T^j_s.
  - SP at s uses T^j_s ∪ L_k, where L_k is what pass 1 learned at tops before a_k.
  - At s + 1, before e*, nothing has been learned in s + 1 (FDL). So both BV and SP at s + 1 use T_{s+1}, and
    T_{s+1} ⊇ T^j_s ∪ L_k, because L_k is learned during s and T only grows inside a phase.
- (c) Suppose e* lies in sptl pass 1 of s + 1 at top a_k. Then no BV region of this call differs between s and s + 1, since BV
  precedes SP in the log. By induction on k (using (a)):
  - f_k(T^j_s) = BV_s(a_k) = BV_{s+1}(a_k) = f_k(T_{s+1}).
  - Monotonicity sandwiches SP_s(a_k) = f_k(T^j_s ∪ L_k) between them.
  - And SP_{s+1}(a_k) = f_k(T_{s+1}).
  - So SP_s(a_k) = SP_{s+1}(a_k), with equal inputs for the next top.
  - Hence no SP region differs. That contradicts e* lying there. □
(The DATA in GAP-A-M §22e, "e* never in sptl or Dom" in 1,865 transitions, agrees with §2-§3.)

## 4. Theorem CK (PROVED, reading, on the cited signed results)
On 𝒞_C^dist, every q-phase satisfies I ≤ (n + 1)(|P| + 1)(H + 1 + n²) + 1, with H the polynomial of RESULTS R7 (d). Hence
S − 1 = |P| + I ≤ |P| + (n + 1)(|P| + 1)(H + 1 + n²) + 1.
Proof.
- (1) If the logs of s and s + 1 (repeated sptl passes of s deleted) are identical, then every extraction of s + 1 repeats one of
  s.
  - Those SCCs are stored (duplicate check) and are not dominions, because s is not the last search of the phase. So s + 1 learns
    nothing, returns false (1068) and is the last search of the phase.
  - This happens at most once per phase: the "+ 1".
- (2) Otherwise e* exists. By EMPTY-REC every depth-≥1 call is on ∅ and contains no tattr, so e* is at depth 0, in position j
  of the common chain.
  - By §2 (i) it is not the −1 threshold attractor, and by §3 it is not an sptl region.
  - So it lies either in the best_vertices call at R_j (regions or threshold loop, 691-771), which makes it an e*-at-R_j
    transition in the sense of R9 (a), or in a step of the Dom call of position j, with input (R_j, V_j).
- (3) Budgets per phase:
  - each context R has at most H + 1 e*-at-R transitions, by R9 (a) with F_R = 0 (R11 (c) and NOSTEAL-1P);
  - each Dom input (R, V) has at most n² Dom-e* transitions, by DOM-MONO.
- (4) The contexts. The chain changes only at chain-changing transitions, so a phase sees at most |P| + 1 distinct chains. A chain
  has at most n + 1 positions, because every piece except the last is nonempty. So the pairs (R_j, V_j) of chain-keeping
  transitions form a set of size ≤ (n + 1)(|P| + 1).
- (5) Summing (1)-(4) gives I ≤ (n + 1)(|P| + 1)(H + 1 + n²) + 1. □

## 5. Consequence with R46 (reading)
With R46 §2b-§3 (the K-constraint and L-NEST*, signed in P-C1P), |P| ≤ (2(d + 2)(n + 1)²K)^d with d = NEST*(P) and
K = (n + 3)(n + 1)². Theorem CK then gives S ≤ poly(n)·|P| + poly(n).
Hence, with phases ≤ D + 2 (RESULTS R5 (g)) and CTRL for the controller's searches: GAP-A on 𝒞^1P ⇐ (NEST*-BOUNDED), ONE named
statement. (CHAIN-CHANGE) is no longer needed: chain-keeping transitions cost only a polynomial factor. DATA: I = 0 on every
class run so far (0 of 1,046 class transitions; 5,566 random).
Weak points for the referees:
- DOM-MONO uses the distinct q-priorities to order Dom's caps, and the trigger structure of attractVertices / attractTangles
  (a vertex or tangle is examined only when a successor or escape is popped).
- §3 (a) identifies BV's final-round regions with sptl's pass-1 regions line by line (692/699 against 482/490).
- (4) uses "every piece except the last is nonempty". A −1 piece contains prevV or the seeds; a stable piece contains V*; the
  last call returns 0.
