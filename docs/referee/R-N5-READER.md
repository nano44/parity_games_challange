# R-N5-READER: REFEREE faithfulness check of the READER device (L-SI, docs/si/N5-ALT-box23.md §8 at l-si 6ec0aa2b, §9 at 2e94557d)
Referee: REFEREE (successor 16), Opus 5.5 (owner ruling D15). Task: Lead message of 2026-10-28 21:35Z (date -u). Written 2026-10-28T21:34Z-21:39Z
by date -u. Every verdict is labelled (Opus 5.5, D15).
- Read: SPEC docs/new/N5-ssi-global.md S1-S5 with FIX 1-4 (sha1 66fde9ef); si.py e688b963 l. 78-205 (as SPEC S1 names it); the lane's §8
  and §9 (§8's own wording: «S4b could move τ(o) only, but never did here … It is not proved for all games»).
- No lane code run (mkoreader.py, orcheck.py, evenside.py, gateret.py not executed or imported). L-COMP's independent reproduction not read.
  Own engine rl_engine (SPEC S1-S5 from the text); tools scratch/reader_check.py, scratch/reader_search.py; logs scratch/reader_logs/,
  inputs scratch/reader_inputs/.

## Verdict
| claim | verdict (Opus 5.5, D15) |
| --- | --- |
| READER-INVARIANCE as stated: for EVERY game, appending o (Odd, no predecessors, lowest priority, edges into S inside one class) leaves N5's run on the old vertices, the S4c fallbacks and the phases unchanged | FALSE (gap G-READ-1). S4b moves τ(o) whenever o has an improving edge and the arena optimum differs. That ends a phase (τ changes) inside an old phase, and, at an old Even fallback, cancels the fallback (S4c fires only if σ_new = σ AND τ_new = τ). Counterexamples in §2 |
| Theorem READER-INV (REFEREE; PROVED, every game): the same with the hypothesis (R) "τ(o) never moves at a transition at which τ is unchanged on the old vertices"; (R) holds in particular if Iτ(o) = ∅ at the start and after every change of τ on the old vertices | PROVED (§1) |
| Corollary: on any base game and any τ-constant stretch of its run, a reader started at the stretch's first state with τ0(o) maximal for Odd's dual valuation over S satisfies (R) on that stretch | PROVED (§1) |
| l121reader_n41 reproduction | REPRODUCED with my engine: SAME on vertices 0..39 at all 123 states, phases equal ([0, 0], [1, 122]), Ξ(o) changes 86 times in [1, 122] (> 2n = 82), o ∈ D at 109 states, 75 σ̄(o) changes, 8 fallbacks; Iτ(o) = ∅ at all 123 states, so (R) holds and SAME is an instance of the theorem |
| The kill of XR-LIN | STANDS, and needs no invariance: l121reader_n41 is itself a game in which one vertex's Ξ changes 86 > 2n times in one phase |

## 1. Theorem READER-INV and its proof
Setting. G a game on V = {0..n−1}; G′ = G plus o := n, Odd, with no predecessors, successor set S ⊆ V, any priority. Ranks of G′ are by
(Ω, index), so the old vertices keep their relative order, and o (index n) is inserted somewhere. In l121reader_n41, o has priority 0 like
two old vertices and ranks above them (rank(o) = 2), so "priority below every other" is not literal there, and the theorem does not need it.
Start pairs agree on V; τ0(o) ∈ S.
Lemma (one state). At any pair (σ, τ′) of G′ with τ := τ′|V:
- (a) Ξ′ = Ξ on V, up to the order-preserving relabelling of ranks (as (cycle node, path VERTEX set, length)), and σ̄′|V = σ̄.
  SPEC S1 step by step:
  - (i) o is on no cycle (no predecessors), so it is never a cycle node. Its DFS in (i) and every other DFS of (i) and (v) only follow
    successors, so they never visit o.
  - (ii) R may contain o (it reaches v through S), and nothing else changes: o has no predecessor, so no reach set grows through o.
  - (iii) if rank(o) > rank(v), o is an Even- or Odd-liked u. M = reach(v, o) is R ∖ {o}, so restrict deletes only edges into o, and there
    are none; reach(o, v) = {o}, so only o is affected. Every other M is computed by predecessor traversal and gains at most o itself. Every
    restrict(q, M) with q ≠ o deletes only q's edges, and its targets other than o are as before.
  - (iv) longest: each vertex's value and choice is a function of its successors' (first strict maximum in list order), so o changes
    nothing. BFS: o is discovered by some S vertex and appended to a layer, but its hp list is empty, so it discovers nobody. The relative
    layer order of the other vertices, and hence every first discovery, is unchanged.
  - (vi) ranks enter only through comparisons: reward order, most relevant vertex of a cycle, "rank > rank(v)", and the signed-weight order,
    which is decided by the highest differing rank. An order-preserving relabelling preserves all of them.
- (b) Iσ′ = Iσ (S2 reads Ξ at Even vertices' successors; no Even vertex points to o).
- (c) Iτ′ = Iτ ∪ Iτ′(o) with Iτ′(o) ⊆ {o} × S. The same argument on G^d (o is G^d-Even with no predecessors) gives Odd's dual valuation on V
  unchanged.
- (d) S4a's output on V is the same: its arena differs only at o, and S1 on its dual is (a) again.
- (e) S4b's output on V is the same, whenever S4b runs on G or only on G′ (in the latter case Iτ = ∅, the arena keeps τ on V, and the output
  there is τ). τ′_new(o) is o's arena choice.
- (f) S4c: G′ falls back iff G falls back AND τ′_new(o) = τ′(o). If both fall back, the switches on V are the same: Even's are read from Iσ,
  Ξ and indices; Odd's from Iτ ∩ (V × V) and the dual valuation. FIX 3: in an Even fallback τ is kept, in both games.
Proof of the theorem. Induction on the state index, with (R) applied to the Lemma.
- At a transition where G does not fall back, (d), (e) give the same σ_new and τ_new on V in both games, whatever τ(o) does.
- At a transition where G falls back, (R) gives τ′_new(o) = τ′(o) (τ on V is unchanged at an Even fallback), so G′ falls back too, with
  the same switches (f).
- Termination: when G stops, G′ may continue with steps that move only τ(o). Under (R) such a step cannot occur while τ on V is unchanged,
  so G′ stops with G.
- Phases: λ_Ξ on V agrees by (a). λ(o) is the cycle node of o's choice, the class of min_S Ξ. It is constant wherever λ is constant on V,
  if S lies in one class at every state. τ′ is constant exactly where τ is, by (R). □
- Ξ(o) = o ⊕ min_S Ξ. σ̄′(o) minimises Ξ over S (Odd's optimal counterstrategy, 1E-N3), and o ⊕ is order-preserving: the reward of the cycle
  node is unchanged, and for equal cycle nodes o is added to P for all options or for none. Checked at every state below.
Corollary. Odd's dual valuation of τ′ depends on τ′ only. On a stretch where τ is constant on V and τ(o) has not moved, Iτ′(o) is constant.
So τ0(o) := a G^d-maximal choice over S at the stretch's first state gives Iτ′(o) = ∅ on the whole stretch, hence (R) there. The run of N5
from any state equals the suffix of the run through it (N5 is a function of the state), so the reader may be started at any phase's first
state of any base game. This is what §8's general claim ("on any base, max_z XR ≥ the changes of a minimum over a subset of a class") needs.
It is PROVED for one τ-constant stretch at a time.

## 2. G-READ-1: counterexamples to the unconditional statement
- (A) A fallback cancelled (the RUN changes).
  - Base: reader_inputs/cex_base.pg (sha1 325b9862), n = 5, start cex_base.start (9732b834).
  - Reader: cex_reader.pg (8ccd0285) = base + o = 5 (Odd, priority 0, below every old vertex, which all have priority ≥ 2), S = {0, 2},
    start cex_reader.start (7e765232) with τ0(o) = 2. 0 and 2 lie in one class at every state (cycle node 4 at state 0, 0 afterwards).
  - Base run: state 1 has Iσ = {(0, 2)}, Iτ = ∅. S4a returns σ, τ_new = τ, so S4c's FALLBACK fires (σ(0) := 2); the phases are [0, 0], [1, 2].
  - Reader run: at state 1, Iτ′ = {(5, 0)}, and S4b's arena optimum is τ′_new(5) = 0 ≠ 2. So σ_new = σ but τ_new ≠ τ, and S4c does NOT fire
    (SPEC S4c: "FALLBACK, if σ_new = σ and τ_new = τ"). The transition 1 → 2 moves only τ(o). The fallback fires one state later, at 2 → 3.
  - So the run differs from state 2 on (3 vs 4 states), the fallback flags shift, and the phases are [0, 0], [1, 1], [2, 3].
  - (At state 0, Iτ′ = {(5, 0)} already, but S4b's arena optimum against σ_0 was τ(o) itself: an improving edge alone does not move τ(o).)
  - Random search (reader_search.py, 3,000 games n 4-9, 180 readers on runs with an Even fallback): the phases differ for 27 readers, the run
    on the old vertices for 21.
- (B) Phases split with the run unchanged, on the lane's own instance. l121reader_n41 with every other start τ0(o) ∈ S ∖ {0} (13 variants,
  reader_inputs/l121reader_n41_tau*.start): SAME on the old vertices in all 13, phases different in all 13. τ(o) moves 1-4 times inside the
  old phase [1, 122], which splits; e.g. τ0(o) = 2 gives [1, 24], [25, 121], [122, 122]. Iτ′(o) ≠ ∅ at 122 of 123 states there. So the lane's
  choice τ0(o) = 0 (the dual-optimal one, Iτ′(o) = ∅ throughout) is exactly what makes its instance faithful.

## 3. Answers to the Lead's checklist
- S4b: τ(o) CAN move, at any transition where Iτ′(o) ≠ ∅ and o's arena optimum against σ differs from τ(o), not only at fallbacks. A move
  ends a phase (phases are maximal runs with λ_Ξ and τ constant): §2 (B). At an old Even fallback it also cancels the fallback: §2 (A).
- S1 ranks and tie-breaks after the shift: harmless. Ranks are by (Ω, index) and o has the largest index, so the old order is kept. A tie
  of o's priority with old vertices puts o above them, which is still harmless (Lemma (a), step (iii)). Every tie-break in S1 (longest:
  first strict maximum in list order; BFS: first discovery; DFS cycle choice) is unaffected, since o has no predecessor and appears in no
  old vertex's successor list.
- Iσ, the arena H_t, S4c: Iσ and S4a's arena optimum are unchanged (Lemma (b), (d)). S4c's trigger is the only place where o acts on the old
  vertices, through τ_new (Lemma (f)).

## 4. Reproduction of l121reader_n41 (own engine; scratch/reader_logs/l121reader_n41.txt)
- Files: experiments/si/root/instances/l121reader_n41.pg sha1 084da8cd…, .start 7ca283c4… (measured). Base: experiments/new/box48/instances/
  long121_n40.pg at its .start.
- The diff of the two .pg files is exactly the line "40 0 1 0,1,2,6,7,8,17,20,22,23,24,30,36,39" and the parity header. The start files
  differ only by "40:0".
- Result: SAME on vertices 0..39 at all 123 states (σ, τ, σ̄, fallback flags, and Ξ as (cycle node, path vertex set, length)). Phases equal:
  [0, 0], [1, 122]. In [1, 122]: Ξ(o) changes 86 times (2n = 82), o ∈ D at 109 states, σ̄(o) changes 75 times, 8 fallbacks. Iτ′(o) = ∅ at
  all 123 states, and Ξ(o) = o ⊕ min_S Ξ at all 123. All the lane's figures agree.

## 5. Notes
- READ-N1 (for the lane's §8). Restate READER as: "o with τ0(o) maximal for Odd's dual valuation over S, started at the first state of a
  τ-constant stretch; then the run on the old vertices, the fallbacks and the phases are unchanged on that stretch (Theorem READER-INV)".
  §8's "S4b could move τ(o) only, but never did here" names the right step: it moves for any other τ0(o) (§2).
- READ-N2 (for §8's inflation table). The six-reader instance l121reader6_n46 and its K / DCH / EXIT counts need (R) for every reader. I did
  not check that instance; the theorem says what to check (Iτ′(o_i) = ∅ along the stretch, or no τ(o_i) move outside old τ changes).
- READ-N3 (Even readers, §9). The Lemma's (b) fails for an Even reader: Iσ gains its edges and S4a moves it. The same S4c mechanism then
  cancels fallbacks, as §9 says. Not examined further.

DONE: this report (scratch/reader_check.py, reader_search.py, logs, the counterexample instances in scratch/reader_inputs/).
FINDINGS: READER-INVARIANCE false unconditionally (G-READ-1: S4b moves τ(o), splitting phases and cancelling fallbacks; 5-vertex
counterexample); PROVED under (R), which the dual-optimal start gives on any τ-constant stretch; l121reader_n41 reproduced exactly (86 > 82,
(R) holds); the XR-LIN kill does not depend on invariance.
NEEDS: Lead: route G-READ-1 and READ-N1..N3 to L-SI (the §8 statement should carry (R)); nothing from the owner.
