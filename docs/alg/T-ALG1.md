# T-ALG1: the Strahler threshold of psolC is exactly 1; the nested hierarchy NE'(k) tracks the Strahler number (L-ALG, 2026-10-15)

Status: statement (a) below is PROVED here in prose by L-ALG (unrefereed; a candidate M3 "tighter analysis of a known
algorithm" in the sense of Lead reading L9, like T-A1); statement (b) is DATA; (c) is a conjecture. Nothing here is a result
until two referees sign (CLAUDE.md). Vocabulary: TARGET.md section 1 (max-parity, pr: V -> {0..n}); Strahler number of a
parity game as in Daviaud-Jurdzinski-Thejaswini, arXiv 2003.08627v2 (ICALP 2020), p.4-5 (restated in section 1 below);
psolC as in Huth-Kuo-Piterman DTR15-4 Fig. 5 with Definition 1-2 read literally (start colour included; the reading the
REFEREE found FAITHFUL in experiments/attr/psolc.py, referee 1600917), restated in docs/attr/A3-psolC-results.md section 1.

## 0. Statements
(a) Theorem (proved in section 2). For every parity game G of Strahler number 1, psolC decides every vertex of G.
    Moreover, on such a game the first call tryPlayer(G, Even) returns exactly W_E(G) (if non-empty), and the next
    successful call returns W_O(G).
(b) Sharpness (data, exhaustive). The 4-vertex game experiments/attr/instances/psolc_min_n4_m6.pg has Strahler number 2
    and psolC decides none of its vertices (A3, DE3). Every one of the 1,380 canonical 4-vertex games psolC leaves partly
    undecided has Strahler number 2 (none has 1); the 9 psolC failures with n = 5..18 in experiments/attr/instances/ have
    Strahler number 2. Hence: the largest k such that psolC decides every vertex of every game of Strahler number <= k is
    k = 1 (L-LIT RANKING row 3, "first problem", answered for psolC; for psolQ the answer is 0: psolq_min_n3_m4.pg has
    Strahler number 1 and psolQ leaves it undecided).
(c) Conjecture. NE'(k) (docs/alg/candidates/C2.md) decides every vertex of every game of Strahler number <= k + 1.
    Data: all 45 shrunk games on which NE'(1) fails (experiments/alg/out/c2k1_fail_seeds.jsonl, found by crossover search)
    have Strahler number exactly 3; NE'(2) solves them. If (c) holds, NE'(floor(lg n)) is a complete solver (DJT Prop. 3:
    Strahler <= floor(lg n) + 1) running in n^{O(log n)} time: quasi-polynomial, no improvement on DJT Thm 32.

## 1. Definitions used (DJT p.4-5, max-parity, Even = DJT's Steven, Odd = Audrey)
Let d be even, >= every priority of G. An Even d-attractor decomposition of G is H = <A, (S_1, H_1, A_1), ..., (S_l, H_l, A_l)>
with: A = Attr_E(G, P_d) (P_d = vertices of priority d, possibly empty); G_1 = G \ A; for i = 1..l: S_i a non-empty trap for
Odd in G_i with all priorities <= d - 2, H_i an Even (d-2)-attractor decomposition of G ∩ S_i, A_i = Attr_E(G_i, S_i),
G_{i+1} = G_i \ A_i; and G_{l+1} empty; if d = 0 then l = 0. The tree T_H is the trivial tree if l = 0 and <T_{H_1}, ..., T_{H_l}>
otherwise. Str of a tree: 1 for the trivial tree; for <T_1..T_l> with m the largest Str(T_i): m if exactly one i attains m,
m + 1 otherwise. Str(H) = Str(T_H). The Strahler number of G is the maximum over the two players of the smallest Str(H)
over attractor decompositions H of that player's largest dominion (W_E(G) for Even, W_O(G) for Odd). DJT Prop. 1: a trap
with a decomposition is a dominion. Observation: Str(T) = 1 iff every node of T has at most one child (T is a chain).

## 2. Proof of (a)
Let G have Strahler number 1 and W = W_E(G) be non-empty. Fix an Even decomposition of G ∩ W with a chain tree. Unfolding
the chain gives sets W = S_0 ⊋ S_1 ⊋ ... ⊋ S_r (r >= 0) and even numbers d_0 > d_1 > ... > d_r (d_j = d - 2j) with, for
every j: T_j := P_{d_j} ∩ S_j (possibly empty), B_j := Attr_E(S_j, T_j) (the attractor inside the subgame G ∩ S_j),
G'_j := S_j \ B_j, and either G'_j = ∅ (then j = r) or S_{j+1} ⊆ G'_j is a trap for Odd in G'_j with all priorities
<= d_{j+1} and Attr_E(G'_j, S_{j+1}) = G'_j (the chain has one child: l = 1 and G'_j \ A_1 = ∅). All priorities in S_j are
<= d_j. W is a trap for Odd in G.
Even's strategy sigma (the dominion strategy of DJT Prop. 1): at v ∈ W let j be the largest index with v ∈ S_j; if v ∈ B_j \ T_j
play the attractor strategy of B_j towards T_j; if v ∈ T_j play any successor inside S_j (exists: S_j is a trap for Odd in G'_{j-1},
so Even's vertices of S_j keep a successor in S_j; for j = 0, W is a trap for Odd in G); otherwise v ∈ G'_j \ S_{j+1}: play the
attractor strategy of G'_j towards S_{j+1}.
Claim 1 (structure of plays). Every play consistent with sigma stays in W; whenever it is in S_j at some position it stays in S_j
for ever or leaves S_j by an Odd move into B_i \ T_i... more precisely into S_i \ G'_i = B_i for some i < j ("an upward exit").
Proof: Odd's vertices of S_j (j >= 1) have all their successors inside S_j or outside G'_{j-1}, i.e. in S_{j-1} \ G'_{j-1} = B_{j-1}
(trap in G'_{j-1}); Even never leaves S_j by sigma. By induction the same holds for the enclosing S_{j-1} and so on; W = S_0 is a
trap for Odd in G. []
Claim 2 (reaching the tops). From every v ∈ W, every play consistent with sigma visits T := ∪_j T_j. Proof: let j be the
largest index with v ∈ S_j. If v ∈ T_j done. If v ∈ B_j \ T_j the attractor strategy reaches T_j in at most |S_j| moves unless
Odd makes an upward exit (Claim 1). If v ∈ G'_j \ S_{j+1}, the attractor strategy reaches S_{j+1} unless Odd makes an upward
exit; inside S_{j+1} apply the same reasoning with j + 1 (the chain is finite: at level r, G'_r = ∅ so S_r = B_r and T_r is
reached). An upward exit lands in B_i with i < j, from where the attractor strategy reaches T_i unless Odd exits upward again,
to some i' < i; upward exits strictly decrease the level, so there are at most r of them in a row, and the play reaches T. []
Claim 3 (the tops are a post-fixpoint of psolC's operator). Let X := T (every vertex of T has an even priority, so
T ⊆ P_Even). Then T ⊆ Wr_Even(G, T), i.e. from every x ∈ T Even can force a LATER visit to T at which the maximum priority
seen since x (x included) is even. Proof: let x ∈ T_j and let Even play sigma. By Claim 2 applied to the successor of x, the
play visits T again, say first at y ∈ T_i. Case (i): the play stayed in S_j between x and y: all priorities seen are <= d_j and
pr(x) = d_j, so the maximum is d_j, even. Case (ii): Odd made upward exits; let i be the level of the last one before y
(so y ∈ T_i, reached by the attractor strategy inside B_i, or an even higher level); every vertex seen since x lies in S_i,
with priorities <= d_i, and pr(y) = d_i, so the maximum is d_i, even. []
Claim 4 (psolC's greatest fixpoint contains T, and its attractor is W). psolC's operator F(X) = X ∩ Wr_Even(G, X) is monotone
in X (Wr is an attractor to the target X x {even colours} in the product graph; a larger X has a larger target). Its iteration
X_0 = P_Even ⊇ X_1 = F(X_0) ⊇ ... reaches the greatest fixpoint X* ⊆ X_0; since T ⊆ X_0 and T ⊆ F(T), induction gives T ⊆ X_i
for all i, so T ⊆ X*. tryPlayer(G, Even) returns D = Attr_E(G, X*) ⊇ Attr_E(G, T) ⊇ W by Claim 2 (sigma forces T from all of W,
and plays never leave W). By soundness (DTR Thm 2) D ⊆ W_E(G) = W. So D = W. []
The remaining game G \ W has W_O(G \ W) = W_O(G) and the same Odd decomposition (Odd's winning strategy never enters W),
so the same argument with the players swapped shows that tryPlayer(G \ W, Odd) returns W_O(G) (tryPlayer(G \ W, Even)
returns ∅ by soundness). If W_E(G) = ∅ the first call returns ∅ and the second returns W_O(G). Hence psolC decides every
vertex. (The argument uses the literal reading of DTR Def. 1, start colour included: with the start excluded, in case (i)
the maximum could be an odd priority < d_j seen before reaching a deeper T_{j'}; so (a) is claimed only for literal psolC.) []

## 3. What (a)-(c) mean for M4 (L-ALG reading)
The fatal-attractor family is the Strahler/register hierarchy in disguise: psolC = depth 1, each nesting level of NE' adds one
register (DJT Thm 8: Strahler number = Lehtinen register number). Games of every Strahler number exist (DJT, perfect binary
decomposition trees), so no fixed-depth member is complete, and depth lg n costs n^{O(lg n)}. Candidate designs in this family
cannot reach M4 unless they compress the register state space adaptively, which no member does. This is the exact obstruction
recorded for C1 and C2 in docs/alg/DEAD.md.

## 4. Checks a referee would want (L-ALG list)
- G1: Claim 1's description of Odd's possible exits (only to B_i, i < j) relies on S_j being a trap for Odd in G'_{j-1} and on the
  decomposition's subgames; a referee should re-derive it from DJT's definition (the subgame G ∩ S_i is where H_i lives).
- G2: monotonicity of Wr in X and the "later visit" reading (start colour included) against DTR15-4 Def. 1-2.
- G3: W_O(G \ W_E(G)) = W_O(G) and decomposition unchanged (standard; DJT Prop. 1 direction).
- Machine evidence: every psolC failure found (1,389 games) has Strahler number 2 (experiments/attr/strahler.py); no
  Strahler-1 failure in 27.3 M canonical 4-vertex games (26,632,540 of them have Strahler number 1 per A1's all-strahler run).
