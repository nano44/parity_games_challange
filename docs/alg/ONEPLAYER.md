# ONEPLAYER: in one-player games, A_DTL's per-context budgets hold with no steal (referee brief)

L-ALG successor 9, box 11, 2026-10-18 (produced on Opus 5.5). Source: docs/alg/GAP-A-M.md §27b. Status: READING, UNREFEREED.
Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). "N" = dtl.cpp
line N (tools/oink/src/src/solvers/dtl.cpp). Signed results used: RESULTS R8 (STR-DET), R9 (c), R11 (c).

## Honest label
HONEST LABEL (Lead 10:27Z): one-player parity games are solvable in polynomial time by other means (cycle detection on the
controller's graph), so a bound for A_DTL on 𝒞^1P is a MODEST result. Its value would be that it is the FIRST proved structural
bound for A_DTL, and that the technique (no steals ⇒ the computation at a fixed context is monotone along a phase) may transfer.
The price of NOSTEAL-1P is the hypothesis that the q-parity priorities are pairwise distinct. Without it the lemma is OPEN:
the proof fails at step 1, and no instance is known (3,600 forced tie runs of the designed steal instances, all k = 0, §27c).

## Class (a property of the game)
For C ∈ {0, 1} and q = 1 − C, the class 𝒞_C holds the parity games (TARGET.md §1) in which every vertex of player q has exactly one
successor. 𝒞_C^dist is 𝒞_C with the priorities of parity q pairwise distinct. 𝒞^1P := 𝒞_0^dist ∪ 𝒞_1^dist.
- Oink's renumber (game.cpp 618-637) is strictly increasing on values, so "pairwise distinct" survives it, and after the reindex
  (vertices sorted by priority, O1) a higher index among q-parity vertices means a strictly higher priority.
- A vertex keeps its unique successor in every G′ of the run. A vertex whose only successor is solved is attracted with it by the
  dominion attractor (1031-1036, attractVertices(player, v, G, S, G, −1)), whoever owns it.

## Lemma CTRL
In 𝒞_C, every tangle that search(C) extracts is a dominion. Hence every search(C) that returns true finds a dominion, and player C
makes at most n + 1 searches in the run.
Proof.
1. extractTangles computes escapes from the q-vertices of the SCC only (329-338: `if (owner(v) != pl)`, targets with `G[to]` that
   are not in the tangle).
2. A q-vertex in an SCC with ≥ 2 vertices has an out-edge inside the SCC, and that is its only edge. A one-vertex SCC needs a
   self-loop (is_tangle, 315-317), which is then the vertex's only edge.
3. So the escape list is empty, and the SCC is recorded as a dominion (347-376, dominions++), not as a tangle.
4. search returns true only if tangles or dominions changed (1068). Here only dominions can change, and every dominion's vertices
   leave G. So C's true searches are ≤ n, plus one final false search. □

## Lemma NOSTEAL-1P
In 𝒞_C^dist, in every phase of player q, under every order datum, no best_vertices context has a relevant steal. A relevant steal
(R11): a tangle t ∈ F_τ, fired in top τ's region step of round r at visit i, that the later prefix P_{i+1}(τ⁺) meets but does not
contain. Here P(τ⁺) is the union of the round-r regions of the tops before τ.
Proof. Let A := t ∩ P_{i+1}(τ⁺), and suppose A ≠ ∅. A vertex enters a round-r region (690-701) in one of three ways: as the top
(692), through attractVertices (66-89), or through attractTangle (110-197). All of these run with R = G = CurR and Z = CurZ.
1. No vertex of t is a top of a prefix region.
   - Every vertex of t has priority ≤ pr(τ). t fired in τ's region: attractTangle refuses a vertex outside CurZ with priority
     > pr(τ) (140), and CurZ is τ plus vertices attracted under the cap pr(τ) (74, 140).
   - The prefix tops are q-parity vertices (V ⊆ q-parity, 661-667) with index above τ (top loop 691, descending). So their
     priority is > pr(τ), by distinctness and O1.
2. Every vertex of A has all its t-successors in A. Here the t-successors of a q-vertex y are its unique successor s(y); those of a
   C-vertex o are its successors that lie in t. Note t ⊆ R, because t fired inside R at visit i.
   - y entered through attractVertices: it was pulled by a popped v ∈ CurZ with y ∈ ins(v) (74, 88; pl = q, so no escape test).
     So v = s(y), and v is in the prefix.
   - y entered with a tangle t″: t″'s strategy at y is its only edge s(y) ∈ t″. For a one-vertex t″ this is the self-loop.
   - o entered through attractVertices: no successor of o is in CurR \ CurZ (75-85). A successor x ∈ t ⊆ R is in CurZ, or it was
     popped earlier in round r. In both cases x is in the prefix.
   - o entered with t″: a successor x ∉ t″ is an escape of t″ (x ∈ G′ ⊆ the G at t″'s extraction), and attractTangle needs every
     escape in CurZ or outside CurR (152-157). So again x is in the prefix.
3. t is strongly connected in exactly these edges. It is an SCC of extractTangles' graph: str, the unique successor, for
   q-vertices, and region edges for C-vertices; restricted to t, the latter are the C-successors in t. By 2, A is forward-closed,
   so A = t, and t ⊆ P_{i+1}(τ⁺). □
Corollary (on signed results, given STR-DET (R8)):
- On 𝒞^1P, N*_R = 0 at every context of q's phases, so F_R ≤ 3·N*_R = 0 (R11 (c)), and Π_R rises at every e*-at-R transition.
- R9 (c) gives S − 1 ≤ (H + 1)|C_bv| + n(|C_T| + |C_Dom|) + 1 per phase of q, with H polynomial (R7 (d)).
- CTRL bounds C's searches by n + 1.
- Hence GAP-A on 𝒞^1P ⇐ (CTX⁺) on 𝒞^1P.

## Scope and caveats
- Not a bound by itself: (CTX⁺) on 𝒞^1P stays open. CTRL alone makes the controller's phases trivial.
- Without "dist": step 1 fails, since a later top of the same priority can be in t. Data on 32 one-player lagfam conversions,
  with ties, show k = 0 too, so dropping "dist" is open, not refuted.
- Statement diff against TARGET.md: the objects are those of §1 (vertex priorities, max-parity, every vertex has a successor).
  The class only adds hypotheses on owners, out-degrees and q-parity priorities. These are lemmas about the search count of
  A_DTL, not an M4 claim.
- Data (evidence only): GAP-A-M §27b. The lagfam conversions keep long phases (D + 7) with max k = 0. Every improvement of the
  class climbs (fixd_ctx1p.py) is checked for k = 0: 0 violations so far. Calibration caveat: steal-scoring climbs find no steal
  even in unrestricted games, so the zeros are not evidence by themselves.
