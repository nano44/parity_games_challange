# Referee report R-TL2 (second independent referee): L-RED's transfer lemma, Random-Facet on FHZ's shortest-path graphs = Random-Action-Removal on sink parity games

Referee: REFEREE. Date: 2026-10-15 (routed by the Lead 12:38Z, 3 h box). Written BEFORE reading docs/referee-2/R2-TL.md
(the comparison is §7, appended afterwards). Claim: claude/l-red 0d50d4a (head 9d1c06c differs only in the FHZ-omission
section and the notebook), docs/red/R2-RAR.md section "Transfer Lemma", experiments/red/fhz.py.
Sources opened by me (isolated directories): Friedmann–Hansen–Zwick arXiv 1410.7530 (LaTeX source + PDF): Table 1 and the
zero-/one-edge convention (Actual-Construction.tex 28–66, 101–104), B_0 (144–152), Def. functional (156–160), Def. B_F (234),
Lemma L-Sigma-optimal (305), the Random-Facet pseudocode and its shortest-path reading (RandomFacet.tex 47–50, 70–86, 181–195),
Thm 6.3 = thm:main with the parameter discussion (Lower-RandomFacet.tex 118–142, 706, 760–763), introduction.tex 24–26 and the
abstract (the lane's quotes); errata arXiv 1410.7871 §1–2 (Fig. 1 pseudocode, the RF/RF* mistake, "It is not difficult to
obtain similar examples for parity games", p.4); Zwick arXiv 2607.06334 §2 (AUSO, orientation a → b iff VAL_a ≺ VAL_b),
§3, Appendix D Fig. 1 (Rand-Act-Rem); Friedmann arXiv 1106.0778 §3 (node valuations, set order by the maximum of the
symmetric difference, length component) and §5 (1-sink games: the cycle component is constant, longer paths are better).
Machine checks (mine, independent of experiments/red): docs/referee/scratch/tl2check.py.

## Verdict: OK with fixes (sign, subject to findings 1–2 being applied; nothing changes the lemma's truth)
| item (Lead's list) | verdict |
| --- | --- |
| 1. prior plausibility; why FHZ do not state it | plausible, and the omission is explained (§1): the needed observation is specific to G_{n,r,s,t}'s level-lexicographic costs; FHZ had no reason to look back at parity games in a paper whose point was "even shortest paths", and the parity-game status of ORIGINAL Random-Facet was left open by the errata |
| 2. the lemma line by line | TRUE (my own complete case analysis, §3); the written proof has one missing sub-case in (2) (finding 1) and one loose constant in (1)/(3) (finding 2); (3)'s entry argument is correct |
| 2'. run equivalence RF ↔ RAR | correct (§4): same candidate sets, same test, same pivot, ties treated alike; one condition on S1's tie convention to confirm (finding 3) |
| 3. independent computation | all trees of G, all non-tree edges, three-way verdict (better / tie / worse) identical in G and P on every case run (§5); my own Random-Facet and my own Rand-Act-Rem on the same random stream make identical switch sequences |
| the kill of S1 | follows from FHZ Thm 6.3 (black box, errata-surviving) + the lemma: e^{Ω(√n)} expected switches on parity games with Θ(n^{3/2} log^3 n) vertices, priorities compressible to TARGET's range; not polynomial expected time |

## 1. Prior plausibility and the FHZ omission
What is transferred. FHZ 1410.7530 prove (thm:main, verbatim): "The expected number of switches performed by the Random-Facet
algorithm, when run on the graph G_{n,r,s,t}, where r = Θ(log n), s = Θ(√n log n), and t = Θ(log n), with initial tree B_0, is
at least e^{Ω(√n)} = e^{Ω(M^{1/3}/log M)}, where M is the number of edges in G_{n,r,s,t}", with B_0 "a tree consisting
entirely of zero-edges" (Lower-RandomFacet.tex 122–123; zero-edges are the superscript-0, i.e. costly, edges, 101–104). The
algorithm is the recursive Random-Facet of RandomFacet.tex Fig. F-RandomFacet / errata Fig. 1: pick e uniformly from F \ B,
recurse on F \ {e}, pivot iff e is a strictly improving switch for the returned tree, recurse on F.
Why a transfer to parity games is plausible. Strategy improvement on a 1-sink parity game (Friedmann §5) compares, for each
vertex, the set of relevant vertices on its path to the sink in the lexicographic order of priorities, then the path length. A
shortest-path tree problem compares sums of costs. The two orders coincide when the costs are "lexicographic": each level's
cost dominates everything below it and within a level the alternatives are totally ordered by small offsets. G_{n,r,s,t} has
exactly this shape by design (Table 1: level-i costs 0, 2^{2i}, 2^{2i+1} + δ with 0 ≤ δ < 2), because FHZ's binary counter
needs level i to dominate the lower levels. So the construction is "almost" a parity game already; the lemma makes this exact.
Why FHZ did not say it. I confirmed the lane's quotes in the source (introduction.tex 24: "the simplest form of deterministic
1-player games"; 26: "perhaps surprising ... even for acyclic shortest paths problems"; the abstract's "stochasticity ... is not
needed"; errata p.4 "It is not difficult to obtain similar examples for parity games", said about the RF ≠ RF* examples). The
paper's thesis is downward (MDPs → shortest paths); the audience is the simplex one; and at the time (Oct 2014) their 2011
parity-game bound for original Random-Facet had just been retracted (errata §1: "The main result of [1] is thus flawed", "the
lower bound for Random-Facet* remains correct"), leaving original Random-Facet on parity games without a published bound.
Nothing in either text names an obstacle to going back up. Zwick 2607.06334 (2026) cites Friedmann [Fri11] and Fearnley
[Fea10] for deterministic lower bounds and gives no lower bound for Rand-Act-Rem on games, consistent with L-LIT's RANKING §4
("open"). Conclusion: the lemma is not a known result, it is not implausible, and its proof is elementary once the cost
structure is read as a priority order; that is exactly the kind of statement that gets omitted when nobody needs it.
Note on novelty (for L-LIT, not re-checked by me): the lemma is specific to G_{n,r,s,t}; it is not a reduction from shortest
paths to sink parity games (additive costs are not lexicographic in general), and the lane says so.

## 2. The construction and the encoding, against the sources
G_{n,r,s,t}: the lane's description (R2-RAR.md "G_{n,r,s,t}" and fhz.py build()) matches Table 1 edge by edge, including
a_{i,j,s} → b_{i,1} (0) and b_{i,rs} → w_{i+1} (0), the t copies of every costly edge, of u_i → b_{i,1} and of w_i → a_{i,j,1},
and ε = 1/(rs) (fhz.py scales all costs by rs to integers: order-preserving). B_0 = first copy of every costly edge: a tree of
zero-edges as the theorem requires (any such tree is admitted by the theorem's wording). "Functional" F (Def. 5.2) = at least
one copy of every multi-edge, so every vertex keeps an out-edge: correct. In fact the lemma's per-edge statement does not
depend on F at all (whether e improves B depends only on B and e), so quantifying over functional F is harmless.
P_{n,r,s,t} (fhz.py build(), parity part): sink 0 Odd, priority 1, self-loop; every other vertex Even; G-vertices and relays
priority 0 (invisible to the valuation since the cycle node has priority 1); class A exit b_{i,rs} → w_{i+1} through a shared
EVEN vertex g_i of priority base_i + 4rs; class C escapes with offset d through a shared ODD vertex o_{i,d} of priority
base_i + 1 + 2d; class B (cost 2^{2i}) no class vertex; base_i = 2 + (i − 1)(4rs + 2). Hence within band i the priorities are
o_{i,0} < o_{i,1} < … < o_{i,2rs−1} < g_i (all distinct, odd/odd/…/even), and every band-(i+1) priority exceeds every band-i
priority: so the set order is lexicographic by level from the top, and within a level A ≻ B ≻ C(0) ≻ C(1) ≻ … (checked
against the exported instance fhz_n3_r1s1t1.pg: 9 vertices of priority ≥ 2, all distinct). One stale comment: fhz.py's module
docstring describes an older band layout (base_i + 1 for class B, base_i + 3 + 2d for C, band 4rs + 4); the code and the report
use the layout above (finding 4). Sizes: |V(P)| = |V(G)| + |E(G)| + n(2rs + 1) = Θ(nrst) = Θ(M); the maximum priority
base_n + 4rs = Θ(nrs) ≤ |V(P)|, and TARGET's compression preserves order and parity, which is all the valuation reads.
Valuation in P (fhz.py Parity.values/improving): the set is encoded as a signed sum Σ ±2^{rank}, rank increasing with priority;
since the top element of a symmetric difference outweighs all lower ones, sign(S(M) − S(N)) is Friedmann's set order ("M ≺ N
iff max(M Δ N) ∈ (N ∩ V_even) ∪ (M ∩ V_odd)", 1106.0778 §3); equal sets are then compared by length, longer better (odd cycle
node, Friedmann §3/§5). Improving edge: Ξ(head of e) ≻ Ξ(σ(x)), strict. Correct. The relay per copy makes copies of a
multi-edge tie exactly (same set, same length), as costs tie in G.

## 3. The lemma, re-derived (my own case analysis; the lane's (1)–(3) checked against it)
Setting. Fix a tree B and e = (x, y) ∉ B. The two competing paths from x, π_e = x →e y →B … t and π_B = x →B … t, coincide
from their first common vertex m onward (both follow B), so the verdict in G is decided by the costs of the two prefixes
x → … → m, and in P by their class sets and lengths (the suffix's class vertices lie at levels ≥ level(m) and cancel; the
shared class vertices of the two prefixes cancel in the symmetric difference). Entry points of a level are u_i and w_i only
(a-vertices are entered from w_i, b_{i,1} from u_i or the a-chains, other b's and a's from their chain predecessor); exits
are: from u_i: u1 → b_{i,1} (within the level, cost 0) or u0 → u_{i+1} (class B, 4^i); from w_i: → a-chain (within, 0) or
w0 → w_{i+1} (B, 4^i); from a-chains: escape → u_{i+1} (class C, 2·4^i + (k − 1)ε) or on to b_{i,1}; from b-chains: escape →
u_{i+1} (C, 2·4^i + 1 + (j − 1)ε) or exit b_{i,rs} → w_{i+1} (class A, 0). Class offsets: a-escapes < 1 ≤ b-escapes < 2.
Per level the cost order A < B < C(d) < C(d') (d < d') is the P order A ≻ B ≻ C(d) ≻ C(d') (§2). Merges happen at b_{i,1}
(within a level), at u_{i+1}, at w_{i+1}, or at t.
Step 1 (the divergence level ℓ = level(x)). The two prefixes leave x by different edges. If they exit level ℓ to the same
vertex they merge there (or earlier at b_{ℓ,1}); this is the lane's case (2) and all its sub-cases are: copies of one edge
(tie in G; in P same set, same length: tie); x = w_ℓ with two a-chains that both exit (merge at b_{ℓ,1}; tie, equal lengths
s + 1 each) or both escape at the same k (tie, equal lengths) or at different k (C vs C, offset order = P order); x = u_ℓ,
u0 vs u1→b-chain→escape (B vs C, both to u_{ℓ+1}: B cheaper and B ≻ C); x = w_ℓ, w0 vs chain→exit (B vs A, both to w_{ℓ+1}:
A cheaper and A ≻ B); x a chain vertex, escape at x vs chain-then-escape later in the same level (C(d) vs C(d'), d < d'
strictly because offsets increase along the chains and b-offsets exceed a-offsets; merge at u_{ℓ+1}): consistent. The last
sub-case is MISSING from the lane's (2), which says "If x is a chain vertex, both are escapes (the chain edge is unique):
different copies of the same offset, equal cost" (finding 1). Equal (class, offset) at level ℓ forces a merge at level ℓ or at
the entry of level ℓ + 1 (same class from the same x lands on the same vertex: A → w, C → u, B → x's side), so after a tie at ℓ
nothing remains to compare: G ties ⟺ P ties (and P never decides by length in a continuing comparison, see below).
Step 2 (continuing comparisons). Otherwise the classes at ℓ differ and the prefixes land on different vertices u_{ℓ+1}, w_{ℓ+1}
(pairs: (A, B_u), (A, C), (B_w, C); in each the path landing at w is strictly cheaper at ℓ, by 4^ℓ, 2·4^ℓ + δ, 4^ℓ + δ resp.,
and better in P). From then on, before the merge, the prefixes are at u_i and w_i at every level entry (the only entry points,
and equal entry = merge). Possible pairs (u-side class, w-side class) at a full level i: (B_u, B_w) tie, continue;
(B_u, A_w) w cheaper by 4^i, continue; (C_u, B_w) w cheaper by 4^i + δ, continue; (A_u, C_w) u cheaper by 2·4^i + δ, continue
with the sides swapped; (B_u, C_w) merge at u_{i+1}, u cheaper by 4^i + δ; (C_u, C_w) merge at u_{i+1}, w cheaper by
(d_u − d_w)ε ∈ (0, 2) since b-offsets exceed a-offsets; (A_u, B_w) merge at w_{i+1}, u cheaper by 4^i; (A_u, A_w) is impossible
as a full level (both pass b_{i,1}: merge there); a within-level merge at b_{i,1} (u1 vs a-chain) costs 0 on both sides and
carries no class vertex (lengths differ: the a-chain side is longer). In P the contributions of a pair differ iff the classes
differ (A: {g_i}, B: ∅, C: {o_{i,d}}), with the same winner as the cost; (C_u, C_w) contributes {o_{i,d_u}} vs {o_{i,d_w}}, the
smaller offset winning in both.
Step 3 (adding up). Let j* be the highest full level where the classes differ (it exists: level ℓ differs). Above j*, the
only pairs with equal classes and different cost are (C_u, C_w), which can occur only at the merge level (both land on
u_{i+1}), hence at most once, with difference < 2 and with the w-side path winning; between j* and that level only (B_u, B_w)
occurs, so the path on the w side after j* is the w-side path at the (C_u, C_w) level and wins both there and at j*
(at j* the pairs that continue are (B_u, A_w), (C_u, B_w), (A_u, C_w), (A_w, C_u), and in each the path landing on the w side
is cheaper by ≥ 4^{j*}; if j* is the merge level the pairs are (B_u, C_w), (A_u, B_w), where the u-side path wins by ≥ 4^{j*}).
Below j*, every level pair differs by less than 2·4^i + 2, so the total below j* is < Σ_{i<j*} (2·4^i + 2) = (2/3)(4^{j*} − 4) +
2(j* − 1) < 4^{j*} − 2 (the lane's (1), verified: 6j* − 14 < 4^{j*}). Hence the cost difference has the sign of level j*
(gap ≥ 4^{j*} > (4^{j*} − 2) + 2 ≥ sum below + offset difference above), and in P the maximum of the symmetric difference is
at the (C_u, C_w) level if it exists (same winner) and at j* otherwise (same winner). Ties in G occur only in Step 1's
tie sub-cases, where P ties too. This is the lemma, ties included. The lane's (3) is this argument (its "entry" observation,
"one from w_j and one from u_j ... because entering at the same vertex would mean an earlier merge, and a w_j path through
b_{j,1} would meet the u_j path there", is right); its stated inequality "4^{j*} − 2 > sum + offset difference" is not what
the numbers give (sum + offset can reach 4^{j*} − ε), but the class gap at j* is ≥ 4^{j*}, not 4^{j*} − 2, so the conclusion
holds (finding 2).
Every rank, side and offset claim above is what the exhaustive check of §5 tests on every tree.

## 4. Run equivalence (RF on G from B_0 = RAR on P from σ_{B_0})
Zwick Fig. 1 (Appendix D), verbatim structure: B ← actions not in a; if B = ∅ return a; r ← Rand(B); b ← RAR(H \ r, a);
c ← b[r]; if (c → b) ∈ H⃗ return b else return RAR(H, c); with the orientation a → b iff VAL_a ≺ VAL_b (§2). On P the
actions are the relay edges of G's edges at G's vertices (every other Even vertex has one action, never in B); so B = F \ B_G,
the random choice is the same, removing r = removing e, "(c → b) ∈ H⃗" = "VAL_c ≺ VAL_b" = "r is not a strictly improving
switch for b", pivot = tree switch. By the lemma every test gives the same answer, so the two recursions perform the same
sequence of switches for the same random choices: same distribution of runs, same number of switches. Conditions: (i) S1's
rule treats a tie (VAL_c = VAL_b, which happens with multi-edge copies) as "not improving" (Zwick's AUSO has no ties; the
lemma says G and P tie together, so any strict convention is fine, a "switch on ties" convention would not be) — L-SI's si.py
was not read by me (finding 3); (ii) S1's start is a zero-edge tree: the lane argues the best-reward start of si.py is one; not
re-verified by me (finding 3); the theorem admits every zero-edge tree.
What the theorem then gives: Thm 6.3's expected switch count e^{Ω(√n)} on P_{n,r,s,t} with |V(P)| = Θ(nrst) =
Θ(n^{3/2} log^3 n) vertices; each switch costs at least one valuation, so S1's expected time is e^{Ω(|V|^{1/3}/log |V|)}:
not polynomial, consistent with Zwick's upper bound e^{O(√(n ln(m/n)))}. The theorem itself is taken as a black box
(published, and the errata says the construction is unaffected by the RF/RF* error).

## 5. Machine checks (docs/referee/scratch/tl2check.py)
My own G from Table 1 (costs scaled by rs), my own P from the description in §2, my own valuation (Friedmann's set order via
the maximum of the symmetric difference, then length), three-way verdict better/tie/worse. For every tree B (all products of
out-edge choices, F = E) and every non-tree edge e:
| (n, r, s, t) | trees | tests | ties in G | mismatches mine | mismatches, lane's G/P objects (fhz.py build(), same trees) |
| --- | --- | --- | --- | --- | --- |
| (2,1,1,1) | 256 | 2,048 | 0 | 0 | 0 |
| (3,1,1,1) | 4,096 | 49,152 | 0 | 0 | 0 |
| (2,2,1,1) | 9,216 | 129,024 | 6,144 | 0 | 0 |
| (2,1,2,1) | 4,096 | 49,152 | 0 | 0 | 0 |
| (2,1,1,2) | 20,736 | 414,720 | 138,240 | 0 | 0 |
| (4,1,1,1) | 65,536 | 1,048,576 | 0 | 0 | 0 |
| (3,2,1,1) | 884,736 | 18,579,456 | 884,736 | 0 | 0 |
| (3,1,2,1) | 262,144 | 4,718,592 | 0 | 0 | 0 |
Further runs ((2,2,1,2), (5,1,1,1), (2,2,2,1), (3,1,1,2); lockstep (5,2,2,2), (6,1,3,2)) were still running at the time of
this push; their results are appended in §8 when complete.
Lockstep: my Random-Facet (errata Fig. 1) on G and my Rand-Act-Rem (Zwick Fig. 1) on P, same random stream, from B_0:
identical switch sequences and final trees on (3,1,1,1) seeds 0–2 (18, 12, 16 switches), (4,2,2,2) seeds 0–1 (117, 74)
[LOCK]; the final tree has no improving edge in G.
The lane's own evidence (lockstep, lockstep3, relation) is random trees only; the exhaustive runs above cover every tree of
the small graphs, including the missing sub-case of finding 1 (x = a_{i,j,k} or b_{i,j}, escape vs chain-then-escape) and every
tie.

## Findings
1. (S) Proof case (2), chain-vertex start: add the sub-case "e and B(x) are the escape at x and the chain edge, and the chain
   path escapes later in the same level": equal class C, offsets d < d' (strict: offsets increase along a chain and b-offsets
   exceed a-offsets), merge at u_{ℓ+1}; cost and P order agree as in the w_i sub-case. The sentence "both are escapes" is
   false as a description of the case.
2. (S) Case (1)/(3) constants: the class gap at level j is ≥ 4^j (B − A = 4^j, C − B ≥ 4^j), not "4^j − 2"; the sum below j
   is < 4^j − 2 and the single offset difference above is < 2, so gap > sum + offset. Write it that way.
3. (N) State the two conditions on S1 that the run equivalence needs: strict improvement (ties are not switched) and a
   zero-edge start tree; cite the si.py lines (not read by me).
4. (N) fhz.py module docstring describes an older band layout (class B vertex at base_i + 1, C at base_i + 3 + 2d, band
   4rs + 4); the code and the report use no B vertex, C at base_i + 1 + 2d, A at base_i + 4rs, band 4rs + 2. Fix the docstring.
5. (N) Record in the report that the lemma does not depend on F (only on B and e), so "functional F" is only needed for the
   algorithm's well-formedness, not for the lemma.

## Gaps
- FHZ Thm 6.3 is a black box (published; the errata says the construction is unaffected); L-LIT's novelty check and the
  CHECKER are the Lead's next steps.
- The lemma is proved in prose (mine and the lane's); machine evidence is exhaustive for the parameter sets of §5 and random
  (lane) beyond.
- S1's tie convention and start tree in si.py: not read by me (finding 3).
- Zwick's Rand-Act-Rem is stated for AUSOs (no ties); its use on a game with ties is L-SI's rule S1, whose definition I take
  from the lane's report.
