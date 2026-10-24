# Referee report R-N5-1OA: N5 on o-acyclic one-Odd-choice games — Prop X / Cor. X1 (L-RED) and the (C_X + d)(B + 1) bound (L-NEW), with Lemmas R and S

Referee: REFEREE (successor 3), Fable 5.1 (Lead reading L36). Packet P-N5-1OA: the Lead's message of 2026-10-24 03:20Z. Pin: trunk
claude/vibrant-johnson-nxvvxo 07f298d for the sketch I refereed first; the SIGNED OBJECT for the RESULTS entry is the d78e54f text (Lead reading 03:57Z, after both referees checked both texts; §0 is my check of it; §C and §C2 compare with REFEREE-2). Objects: (A) docs/red/R58-n5-width.md §9, Proposition X and Corollary X1 (L-RED, l-red
f93e517); (B) docs/new/N5-1Oacyc-box24.md (L-NEW successor 8, l-new 9d7890f); dependencies docs/new/N5-time-box21.md §2.1 Lemma R and
§2.2 Lemma S. Context read: box 21 §1, §2.3-2.6, §3.4-3.7; R58 §2 (premise (P), Theorem W); RESULTS R15, R17; SPEC S1-S5 of
docs/new/N5-ssi-global.md (FIX 1-4, Q1-Q4); experiments/new/box22/statcheck.py and experiments/new/n5.py (read-only). My own R-N5-1P
(§3 route (a), §4 G4, §5) is used where this packet leans on R17. docs/referee-2/ was NOT read. Source for (P) and (11): VJ00 BRICS RS-00-48,
the pdf of R-N5-1P (sha256 485a12de…), §4.3-4.4, §5.2 (11), §5.5 Lemma 5.8, re-read 03:30Z. Written 2026-10-24 03:22Z-03:34Z by date -u (stamp corrected at 03:39Z: the first push 71aa18fc carried an estimated end time 03:47Z).

## 0. Re-pin (Lead 03:27Z, read 03:43Z) and data addendum (Lead 03:38Z)
The report below was written against the 07f298d sketch of docs/new/N5-1Oacyc-box24.md. The pin is now trunk d78e54f (l-new 8cc6aaf), file sha1
d35502679af112e9fa31eb3af99e64fb4afda1ba (verified; merged here with 7f351fc). I re-read the d78e54f text in full (§1 definitions, §2 theorem,
§3 proof, §4 dependencies, §5 checks, §6 scope) against §3 of this report. Every verdict stands for the d78e54f text. Version map of my gaps:
- A1, A2 (Prop X, R58 §9): unchanged object, unchanged findings. The d78e54f §4 item 1 says the BFS-order point "is taken from L-RED's text";
  I checked it myself (§2 below), so it is now checked by one referee.
- B1 ("no global fallback touched X"): the d78e54f Lemma 1 preamble states the alternatives; its parenthetical "(Any global S4c fallback would
  have switched X's improving edges and changed σ|X.)" presumes Iσ|X ≠ ∅, which the other branch covers. CLOSED by the new text.
- B2 (flat case at an arbitrary state): the d78e54f text now runs R17's B1/B2 sub-cases inline from (★), "without its induction hypothesis",
  exactly the arbitrary-state argument of R-N5-1P §4. CLOSED by the new text. The Remark that only the VALUATION is claimed optimal (ρ need
  not be ≺-maximal; the R15 instance prio [0, 2, 4]) is right and I agree with it.
- B3 (where o-acyclicity enters): the new Step 3 says "Then e ∈ X (o-acyclic)" and "the plays from the exits avoid o". CLOSED by the new text.
- B4 (Iσ_k ≠ ∅ at a pure transition): stated in the new Step 5. CLOSED. B5 (Cor. 2 from any start): same text, confirmed. B6 (counting): the
  new Step 6 has my count (C_X + d − 1 separators, < (C_X + d − 1) + (C_X + d − 1)·B). CLOSED.
- NEW B7 (d78e54f Lemma 1, case (b), "B1, x ∉ π and x on c's cycle"): the improvement list "P(π) ≠ ∅ with an even top, or P(π) = ∅, c odd and
  |π| longer" omits "P(π) = ∅, c even and |π| + 1 < ℓ(x)" (a shortcut to an even cycle node), exactly R-N5-1P G2 / R2-N5-1P G-1P-1 inherited
  from R17's text. The omitted case gives val_ρ̂(x) = (c, ∅, |π| + 1) ≻ (c, ∅, ℓ(x)) = Ω(x) (shorter is better for even c), contradicting (★) like
  the others. Conclusion unaffected. CLOSED (wording, one clause).
- S1, S2 (Lemma S citations): unchanged. (P): the new §4 item 2 states its use (G[X] only, Step 2 cases (a)-(b)); my note on R-N5-1P §3 stands.
Data addendum (trunk 7f351fc, docs/red/R58-n5-width.md §10): L-RED's long-pure-block instances experiments/red/n5inj/instances/block_bk20.pg
(n 24, sha1 98dc1d8b…) and block_bk32.pg (n 36, sha1 439bff4e…), o's exits self-loop sinks, X = the sinks. My probe (n5.py unmodified): bk20
27 iterations = one pure block of 27; bk32 49 iterations = one block of 49; L1 (brute force over G[X]) / L2 / L3 at all 76 pure transitions,
BLK (the block IS n5.py's run on G_τ from σ_0, step for step), GN1, bounds: 0 violations. A block of 49 at |Y| = 33 confirms L-RED's point that
blocks are not bounded by |Y|; the theorem bounds them by R17's B, which is what the data show. These are the sharpest tests of Step 5 so far.

## Verdict
| item | verdict (Fable 5.1) |
|---|---|
| (A) Prop X: the de-duplicated sequence of σ\|X along N5 on G is N5's run on G[X] from σ_0\|X; hence σ\|X changes < C_X = (\|X\|²−\|X\|+1)(\|X\|+m_X) times | SIGNED WITH GAPS: A1 (exactness is a SPEC tie-break statement; the locality of S1's procedure checked step by step, §2), A2 (the "waits" case needs two lines, closed) |
| (A) Cor. X1 (θ, w change < C_X times between τ changes; (CH-1O) on o-acyclic games; "polynomial ⇐ (SEG-1O)") | SIGNED as a reading of Prop X + box 21 §3.6 (superseded by (B), which needs neither (SEG-1O) nor (CH-1O)) |
| (B) Theorem: N5 from ANY start pair on o-acyclic 𝒞^1O makes < (C_X + d)(B + 1) iterations, B = (n²−n+1)(n+m) | SIGNED CONDITIONAL ON (P), WITH GAPS B1-B6 (all closed as wording or by an argument given here). (P) is used only on the one-player game G[X]; that form was re-derived in R-N5-1P §3 route (a), so the condition is weaker than R58 Theorem W's two-player (P) |
| (B) Lemma 1 (σ_k\|X is G[X]-optimal at a pure transition), both cases | SIGNED (conditional on (P)); the flat case is R-N5-1P §4 (G4): it holds at an ARBITRARY state (B2) |
| (B) Lemma 2 (θ_k = w_k at a pure transition) | SIGNED; the hypothesis "o on no cycle" enters exactly here (B3) |
| (B) Lemma 3 (Ξ_k = W_k at a pure transition) | SIGNED |
| (B) Step 5 (a pure block is a prefix of N5's run on G_τ; R17 Cor. 2 from any start) | SIGNED WITH GAPS: B4 (why Iσ ≠ ∅ at a pure transition; closed), B5 (Cor. 2 from any start: yes, R17's proof is start-independent) |
| (B) Step 6 counting | SIGNED (B6: slack, the stated bound holds) |
| Lemma R (box 21 §2.1: the dual order is the exact reverse) | SIGNED (same statement as R-N5-1P §4; proof from S1 alone, checked) |
| Lemma S (box 21 §2.2: sandwich; arena steps are gated best responses), (a)-(d) | SIGNED WITH GAPS: S1 ((a)'s two halves are VJ00 (11) on G and on G^d; R17 (a) carries their derivation, incl. the "⊵" halves of VJ00 (4)/(6) that REFEREE-2 derived), S2 ((b)'s monotonicity is R15 (a) = VJ00 Lemma 5.7, which needs the switched edges to be improvements: R15 (d)) |
| Overall | (A) and (B) SIGNED (B conditional on (P)) WITH GAPS A1-A2, B1-B7, S1-S2, none open as mathematics; for the d78e54f text only A1, A2, B7 (wording) and S1, S2 (citations) remain as wording items. Not a TARGET.md claim; o-cyclic 𝒞^1O untouched; G-N5-TIME stays open. |

## 1. Setting, diffed against the objects and the SPEC
- 𝒞^1O: exactly one Odd vertex o has out-degree d > 1; every other Odd vertex has one edge. X = {v : no path to o}, Y = V∖X. X is closed
  under successors, o ∉ X, every Odd vertex of X is forced, so G[X] is a one-player game in R17's sense (one player has out-degree 1
  everywhere). ✓ o-acyclic ⇔ o lies on no cycle ⇔ every successor of o lies in X (a successor with a path to o closes a cycle). ✓ So X ≠ ∅.
- Ξ = Even's honest valuation (S1, against σ̄); W = V_{σ,τ}; θ = Ξ(o), w = W(o); a pure transition k → k+1: σ_{k+1}|X = σ_k|X and τ_{k+1} = τ_k.
- τ is one choice τ(o) ∈ succ(o): d values. R15 (c) (no strategy repeats in any VJ00 improvement run; applied to τ on G^d, R15 (d)) gives
  ≤ d − 1 changes of τ in a run. ✓

## 2. (A) Proposition X, step by step
Step 1, locality. For x ∈ X every play stays in X and meets no Odd choice, so Ξσ(x) = W(x) = the single σ-play's value, a function of σ|X;
Iσ ∩ (X × V) ⊆ X × X and depends on σ|X. ✓ The claim that S1's PROCEDURE (not only the values) on the dual arena of S4a treats X vertices
exactly as on G[X] is what makes Prop X exact at the level of strategies (GAP A1, a statement about SPEC's tie-breaks). I checked the five
points of R58 step 1 against SPEC S1 (i)-(vi), FIX 2/4, Q2-Q4:
- (i) cycle test and (v) cycle-node DFS for v ∈ X: DFS over successors of alive vertices below v in rank; successors of X vertices lie in X,
  scanned in increasing index: the same scan as on G[X] provided the alive set on X agrees (next point). ✓
- Deaths: a cycle node v ∈ Y kills R = the alive vertices reaching v; no X vertex reaches Y. A cycle node v ∈ X kills Y vertices too, which
  G[X] does not have; X vertices die in the same order (processing order = reward order, the same relative order on X in G and in G[X],
  since rank is by (Ω, v) and relabelling X in index order keeps it). ✓
- (iii) restriction for u ∈ R above v: u ∈ Y "Even-liked": M = vertices of R reaching v without passing u ⊇ X ∩ R (X-paths avoid Y); X vertices
  lose only edges to V∖M ⊆ Y, i.e. none, and get no u in their path set. u ∈ Y "Odd-liked": M = vertices reaching u without passing v, disjoint
  from X; the deletions and additions touch M only. u ∈ X: identical to G[X] (R ∩ X and its edges are those of G[X]). ✓
- (iv) lengths: longest-path recursion over successors in list order: for X vertices only X successors exist, same lists. BFS over predecessors
  from v ∈ X: a predecessor of an X vertex may lie in Y, but a Y vertex has no X predecessor (an edge x → y would give x a path to o). So the
  X vertices enter the FIFO queue only from X vertices, in the same relative order as on G[X], and each X vertex is first discovered from the
  same X vertex: same lengths, same choices. ✓
- Also S2 (Iσ), S3 (per-vertex best-reward start) and S4c's key (Ξσ(w), w) with "larger index" are local, and order-preserving relabelling of
  X keeps every index tie-break. ✓ (An implementation with OTHER tie-breaks still gets the same VALUATIONS on X by R17 (F1), but Prop X's
  "is N5's run on G[X]" is then a statement about valuation sequences only. Wording.)
Step 2, steps. If Iσ ≠ ∅, S4a's X-part is G[X]'s S4a at σ|X (step 1); if Iσ|X = ∅ it is null and so is G[X]'s step. If the X-part is null while
Iσ|X ≠ ∅, σ|X waits; S4c on G fires only when σ_new = σ AND τ_new = τ (GAP A2: Prop X's text has "a global S4c fallback" without the
condition), and then it applies the (Ξσ(w), w)-switch-all to every Even vertex with an improving edge, whose X-part is G[X]'s S4c at σ|X
(G[X] falls back at that state too: its S4a is null and Iσ|X ≠ ∅). While Y or τ still moves, no fallback fires and σ|X stays. The global run
cannot stop while Iσ|X ≠ ∅ (S5 needs Iσ = ∅), so every G[X] step is eventually taken, in order; and at the global stop Iσ|X = ∅, so G[X]'s run
stops at the same strategy. Hence the de-duplicated σ|X sequence IS G[X]'s run, step for step, from σ_0|X. ✓ The count: every G[X]
iteration changes σ|X (τ is trivial there), so #changes = #iterations of N5 on G[X] < C_X by R17 Cor. 2, which holds from any start (B5). ✓
Cor. X1: θ = min over exits e of o ⊕ Ξ(e) depends on σ|X alone (exits in X, Ξ local), so it changes only when σ|X does; w = o ⊕ Ξ(τ(o))
depends on σ|X and τ(o). ✓ "Polynomial ⇐ (SEG-1O)": box 21 §3.6's split with #θ, #w < C_X, #τ ≤ d − 1, #λ ≤ 2n(n−1) (Lemma Φ, R15 (a)). ✓ as a
reading; (B) makes it moot.
DATA (§5): n5.py's de-duplicated σ|X sequence equals n5.py's own run on G[X] (relabelled) in 7,168 of 7,168 runs with Even vertices in X
(4,841 changes), under random relabelling of the whole game so that X is not an index prefix.

## 3. (B) The theorem, step by step
Step 1. Non-pure transitions ≤ (C_X − 1) + (d − 1) ≤ C_X + d − 1. ✓ (Prop X; R15 (c).)
Lemma 1 (GAP B1, closed). "G[X]'s S4a step is null at σ_k|X" at a pure transition: three ways σ|X can stay fixed at k → k+1: (a) Iσ_k ≠ ∅, S4a
ran, its X-part (= G[X]'s S4a, Prop X step 1) returned σ|X; (b) S4c fired on Even (σ_new = σ): the switch-all touched no X vertex, so Iσ|X = ∅
and G[X]'s step is null; (c) Iσ_k = ∅: Iσ|X = ∅. In every case G[X]'s S4a at σ|X is null. ✓ Case Iσ|X = ∅: (P) on G[X]. ✓ Case Iσ|X ≠ ∅ (the
Lead's first pressure point, GAP B2): the arena optimum of G[X] at σ|X is σ|X itself, so by (F1) σ|X dominates every single switch ρ̂ = σ[x→z],
(x, z) improving in X. This is EXACTLY the statement of R-N5-1P §4 (G4): "if the arena optimum returns σ itself, every improving edge is a flat
cycle-closer at its own cycle node", proved there for an arbitrary state with no Lemma P and no phase hypothesis (z's path avoids x ⇒ strict
(V2) or a better cycle node; z's path passes x ⇒ B2 with D ≠ ∅ or top(Z) ≠ c gives a better cycle node; the only survivor is top(Z) = c = x,
flat). Box 24's pointer "R17's case analysis (Case B)" is right in substance; the precise reference is R-N5-1P §4/G4 (and R2-N5-1P G-1P-5),
not R17 Theorem PH, which is a phase statement. Then "switching flat edges leaves every valuation unchanged" is R-N5-1P's G-1P-2 line (the
return path of z_x to x contains no other cycle node, so simultaneous or sequential flat switches are flat), and after switching every such x
to its Ω-best improving successor no improving edge is left (I(x) = {w : Ω(w) ≻ Ω(z*)} = ∅; elsewhere I is unchanged = ∅). The valuation is
then that of an improvement-free strategy of G[X], optimal by (P). ✓ (My DATA check NC of R-N5-1P, 1,398 events, is this statement.)
Lemma 2 (the Lead's second pressure point; GAP B3 = where o-acyclicity enters, closed). (i) For every exit e ∈ X: U_τ(e) := Ξ^d_τ(e) in G's
order = max over σ' of V_{σ',τ}(e) (Lemma S (a)); plays from e stay in X and meet no Odd choice, so U_τ(e) = G[X]'s pointwise optimum at e =
Ξ_k(e) by Lemma 1. ✓ (ii) θ = o ⊕ Ξ(a), a = σ̄(o): the (σ, σ̄)-play from o goes to a ∈ X and stays in X avoiding o, so the prefix formula holds;
likewise w = o ⊕ Ξ(b), b = τ(o), as W(b) = Ξ(b) in X. θ ⊴ w: σ̄ is a pointwise best reply (VJ00 (11); Lemma S (a)/(b)). ✓ (iii) θ ◁ w ⇒ Ξ(a) ◁ Ξ(b)
by strict prefix monotonicity (R17 (V2); both paths avoid o, or cycle nodes differ) ⇒ U_τ(a) ◁ U_τ(b) by (i) ⇒ in G^d's order (Lemma R) a beats b
strictly, a ≠ b, so (o, a) ∈ Iτ (S2 on G^d). ✓ (iv) S4b runs (Iτ ≠ ∅): τ_new = Odd's optimal counter-strategy to σ_k on the arena H′ in which o
may use {b} ∪ {w : (o, w) ∈ Iτ} ∋ a; it is pointwise minimal over H′'s Odd strategies (VJ00 (11), directly, not even dualised). Under any τ′
with τ′(o) = a the value at o is o ⊕ Ξ(a) = θ (the play from a is inside X, independent of τ′); with τ′(o) = b it is w ≻ θ. A pointwise-minimal
τ_new therefore has τ_new(o) ≠ b, so τ_{k+1} ≠ τ_k (S4d; S4c cannot override, it needs τ_new = τ). Not pure: contradiction, hence θ = w. ✓ Without
o-acyclicity (ii) fails (exits route back through o) and (i) fails (U_τ(e) is not a G[X] value); the negative controls (§5) confirm.
Lemma 3. v's σ-path avoids o ⇒ no Odd choice met ⇒ Ξ(v) = W(v). ✓ v's σ-path reaches o: Ξ(v) = π_v ⊕ θ, W(v) = π_v ⊕ w, where π_v ⊆ Y∖{o} is
disjoint from both continuations {o} ∪ X, so the whole-path prefix is valid; θ = w ⇒ equal. ✓
Step 5 (GAP B4, closed). At a pure transition: Iσ_k = G_{τ_k}'s improving set (Lemma 3, same W = Ξ, same σ); S4a is literally the same S1
computation on the same arena against the same τ_k; S4b returned τ_k (pure); S4c on G fires iff σ_new = σ (τ_new = τ holds) and Iσ ≠ ∅, i.e.
exactly when G_τ's N5 falls back, with the same key (W(w), w) = (Ξσ(w), w). Iσ_k ≠ ∅: otherwise the iteration has Iτ ≠ ∅ and either S4b changes
τ or S4b returns τ and S4c, with Iσ = ∅, switches o to an improving exit ≠ τ(o): τ changes, not pure. ✓ So σ_{k+1} = N5_{G_τ}(σ_k) at every pure
transition, and a maximal pure block from state k is a prefix of N5's run on the one-player game G_{τ_k} from σ_k. R17 Cor. 2 (GAP B5): its
proof (Lemma P from an arbitrary ρ_0 of the phase, Theorem PH per phase, ≤ n(n−1)+1 phases from any start, S4c terminal) never uses the
start, so every N5 run on a one-player game from any σ has < B = (n²−n+1)(n+m) iterations (G_τ has the vertices of G and ≤ m edges). A prefix
has ≤ B − 1 transitions. ✓
Step 6 (GAP B6, slack). Blocks ≤ non-pure + 1 ≤ C_X + d − 1; iterations ≤ (C_X + d − 1) + (C_X + d − 1)(B − 1) = (C_X + d − 1)·B < (C_X + d)(B + 1). ✓
The stated bound holds with room.
What the theorem does not need, checked: no Lemma P in the two-player game, no (SEG-1O)/(CH-1O), no Lemma G, no Theorem B (Step 5 is
Theorem B (a) restricted to pure transitions, re-proved in place), no per-path invariant. It needs: Prop X, (P) on G[X], R17 (F1)/(V2)/Cor. 2 and
the G4 statement, Lemma R, Lemma S (a)-(b), R15 (c)-(d), and SPEC S4a-d exactly as written.

## 4. Lemmas R and S (box 21 §2.1-2.2)
Lemma R: rank^d = rank ((Ω+1, v) sorts as (Ω, v)); the triple of a play is the same in G and G^d; rewards reverse (parities flip, relevance kept,
in all three cases); the MaxDiff rule reverses (R⁺ ↔ R⁻; equivalently weight^d = −weight, Q1); the length rule flips with c's parity. SIGN. (R-N5-1P
§4 and R2-N5-1P §2 (i) are the same statement.)
Lemma S: (a) L_σ = pointwise min over τ′ of V_{σ,τ′}: VJ00 (11) ("σ̄ is a best counter-strategy", over all plays, hence over all τ′); U_τ = pointwise
max over σ′: (11) on G^d read through Lemma R. GAP S1: box 21 cites "VJ00 (11); R17 (F1)"; (11)'s own proof rests on Prop. 5.1, whose inputs (4)/(6)
have "⊵" halves the source asserts; R17 (a) records REFEREE-2's derivation of them, so the citation chain is complete through R17. Closed.
(b) L ⊴ V ⊴ U is immediate from (a); monotonicity of L_{σ_k} in k is R15 (a) (VJ00 Lemma 5.7), which applies because every N5 Even step is
Switch_I with ∅ ≠ I ⊆ Iσ (R15 (d)); likewise U on G^d. GAP S2: the text cites R15 (a) only; (d) is needed too. Closed. (c) S4a's output is the
pointwise V_{·,τ_k}-maximum over A(σ_k): R17 (F1) on the one-player arena; the best-reply remark is trivial; Odd symmetric. ✓ (d) SSI's switch set
Iσ ∩ {(v, τ̄(v))} ⊆ Iσ lies in A(σ_k), so (c) dominates it; says nothing about counts. ✓ (B) uses (a) and (b) only. SIGN WITH GAPS S1-S2.

## 5. Computer checks (docs/referee/scratch/n5_1oa_probe.py; n5.py run UNMODIFIED, its (σ_k, τ_k) captured by wrapping si.Engine.evaluate;
everything compared against is computed from the SPEC definitions: plays followed, S1 order with rank = (Ω, v) and parity, so non-injective
priorities are covered; honest Ξ = pointwise min over o's d choices; W = play values against τ)
Checks per run: PX (de-duplicated σ|X sequence = n5.py's run on G[X], X relabelled in index order; #changes < C_X); L1 (σ_k|X has G[X]'s
pointwise-optimal valuation at every pure transition; optimum by brute force over all strategies of G[X] when ≤ 20,000, else skipped and
counted); L2 (θ = w at pure transitions); L2c (the mechanism of Lemma 2 at ANY state: σ|X G[X]-optimal and θ ◁ w ⇒ τ changes next); L3 (Ξ = W
everywhere at pure transitions); BLK (every maximal pure block = the prefix of n5.py's run on G_τ from its first σ; block < B); TOT (iterations
< (C_X + d)(B + 1)); GN1 (engine Ξ = my Ξ at every state); SAND (θ ⊴ w at every state). Generator: o-acyclic 𝒞^1O games with forced Odd
vertices, X built closed and every Y vertex reaching o, half the games with a large Y (more pure transitions than the lane's generator: about
one pure transition per 2.5 runs against 22 in 296), priorities injective or not, vertices randomly relabelled.
| batch | runs | iterations (fallbacks) | pure transitions | blocks (max length) | PX runs / X-changes | L1 checked (skipped) | L2c | violations |
|---|---|---|---|---|---|---|---|---|
| random n 6-12, canonical start, seed 2 | 3,000 | 2,494 (36) | 1,209 | 1,099 (4) | 2,979 / 951 | 1,209 (0) | 347 | 0 |
| random n 6-12, random start pairs, seed 3 | 3,000 | 4,247 (111) | 943 | 837 (5) | 2,987 / 2,559 | 943 (0) | 804 | 0 |
| random n 12-20, canonical, seed 4 | 600 | 877 (17) | 292 | 235 (3) | 600 / 513 | 287 (5) | 73 | 0 |
| random n 12-20, random starts, seed 5 | 600 | 1,152 (26) | 255 | 207 (4) | 600 / 814 | 251 (4) | 86 | 0 |
| statY_12.pg (lane, o-acyclic) | 1 | 8 (0) | 7 | 1 (7) | 1 / 0 | 7 | 1 | 0 (the lane's "7 pure states, one block of 7" reproduced) |
| i4_hand.pg + i4_hand.start (lane, o-acyclic) | 1 | 5 (0) | 1 | 1 (1) | 1 / 4 | 1 | 0 | 0 |
Totals: 15,985 engine valuations compared (GN1 0 mismatches), 7,168 PX runs (0 mismatches), 2,707 pure transitions (L1/L2/L3 0 failures),
1,311 L2c events (0 failures), 2,380 blocks (0 mismatches, max 7), 0 bound violations, θ ⊴ w everywhere. Negative controls (o on a cycle), as
the lanes predict: fts_best16 (28 pure transitions, one block): L2 and L3 fail at 24 of 28 (the lane's "24 of 28" reproduced), BLK fails;
oneodd_c16 / c24, i1_min, i1h_*, i3hn, n9_i2: L2/L3 fail at most pure transitions, every block mismatches. So the hypothesis is used, and
L2c's mechanism (θ ◁ w forces a τ change) is exactly what breaks there.
Honest limits of the data: random blocks are short (max 7) and X-changes few, so the data test the lemmas and Prop X, not the size of the
bound; L1 was skipped on 9 runs with > 20,000 G[X] strategies. I did not re-run the lane's statcheck.py (the Lead did; my checks are
independent of n5x/h1/pureY).

## 6. Gap list
| id | where | what | status |
|---|---|---|---|
| A1 | Prop X | exactness at strategy level is a SPEC tie-break statement; the five locality points of S1's procedure checked against S1 (i)-(vi), FIX 2/4, Q2-Q4 (§2); other tie-breaks give the valuation sequence only | CLOSED (wording: say "under SPEC's tie-breaks" or "the valuation sequence") |
| A2 | Prop X step 2 | S4c fires only when σ_new = σ AND τ_new = τ; the run cannot stop with Iσ\|X ≠ ∅; G[X] stops at the same strategy | CLOSED (two lines) |
| B1 | Lemma 1, "no global fallback touched X" | the three ways σ\|X stays fixed, each giving a null G[X] step | CLOSED |
| B2 | Lemma 1, flat case | the arbitrary-state statement is R-N5-1P §4 (G4) + the G-1P-2 line, not R17 Theorem PH (a phase statement); it holds at any state | CLOSED (pointer) |
| B3 | Lemma 2 | o-acyclicity enters at θ = o ⊕ Ξ(a), w = o ⊕ Ξ(b) and at U_τ(e) = G[X]-optimum; the text should say so | CLOSED (wording) |
| B4 | Step 5 | Iσ_k ≠ ∅ at a pure transition: S4b returning τ with Iτ ≠ ∅ makes S4c switch o (Iσ = ∅), so τ changes | CLOSED |
| B5 | Step 5, R17 Cor. 2 from any start | R17's proof is start-independent; a pure block is a prefix of such a run | CLOSED (confirmed) |
| B6 | Step 6 | iterations ≤ (C_X + d − 1)·B; the stated (C_X + d)(B + 1) holds with slack | CLOSED |
| B7 | d78e54f Lemma 1 (b), B1 second sub-case | omitted improvement case "P(π) = ∅, c even, π shorter": same contradiction with (★) | CLOSED (wording; = R-N5-1P G2) |
| S1 | Lemma S (a) | (11)'s inputs (4)/(6) have asserted halves; complete through R17 (a) | CLOSED (citation) |
| S2 | Lemma S (b) | monotonicity needs R15 (d) (every step is Switch_I of improvements), not R15 (a) alone | CLOSED (citation) |
| (P) | Lemma 1 (both cases) | VJ00 Lemma 5.8 "1 ⇒ 2" on the one-player game G[X] | CONDITIONAL as the Lead allows; the one-player form is re-derived in R-N5-1P §3 route (a) (REFEREE reading) and tested exhaustively there (L58, 7,945 games); the fleet may discharge it by that reading or keep the label |
Inherited: G-N1 (engine = SPEC; DATA, +15,985 states here with 0 mismatches). Scope: a bound on N5 itself on a class that is polynomial by
other means (d one-player games); o-cyclic 𝒞^1O (fts_best16, oneodd_c16/c24, frz24) is untouched: X may be empty, Lemma 2 has no analogue.

## C. Comparison with REFEREE-2 (docs/referee-2/R2-N5-1OA.md, referee-2 603cb3a, trunk 2177e79; read after my report was pushed at
9060b516 / bb96f454; written 2026-10-24 03:51Z-03:55Z by date -u; stamp corrected at 03:57Z, the push 145058c4 carried an estimate 04:05Z). Signed object: the 07f298d texts (Lead reading 03:50Z); my §0 on the
withdrawn d78e54f text stays as a record, and its B7 concerns that text and R17's own B1 wording only.
Agreement per item: identical verdicts in every row. (A) Prop X SIGN WITH GAPS both; Cor. X1 SIGN both (both call "⇐ (SEG-1O)" a reading
superseded by (B)); (B) SIGN WITH GAPS conditional on (P) both, (P) used only on the one-player game G[X] in Lemma 1; Lemma R SIGN both;
Lemma S SIGN WITH GAPS both; the two R17 re-reads (Case B at an arbitrary state; Cor. 2 from any start) CONFIRMED both. No step wrong, both.
Gap map (mine ↔ theirs):
| mine | theirs | status after comparison |
|---|---|---|
| A1 (Prop X exact at strategy level = SPEC tie-break locality; checked step by step) | G-1OA-2, N-1 | SAME finding; R2 adds the sharper point that the COUNT is tie-break-free: every change of σ\|X is a strategy-changing pointwise-optimal arena step of G[X] or its terminal flat fallback, so R17 Cor. 1 bounds it for ANY optimum selection. I ACCEPT this: Prop X's bound does not depend on (1c), only the "is N5's run" identity does. N-1 (keep X's index order) = my relabelling remark |
| A2 (S4c's condition; the run cannot stop with Iσ\|X ≠ ∅; G[X] stops at the same strategy) | G-1OA-1 | SAME content; R2 states it as "a prefix, and the whole run because N5 terminates (R15 (d))". I accept that wording |
| B1 (three ways σ\|X stays fixed) | Lemma 1 cases (i)-(iii) in R2 §2, not listed as a gap | same argument, both |
| B2 (flat case = arbitrary-state single-switch statement, R-N5-1P §4 G4, not Theorem PH) | G-1OA-3 | SAME; R2 adds that box 10's B1 text lacks the own-cycle-node split of the avoid-x case, which the arbitrary-state use needs; both our derivations have the split |
| B3 (o-acyclicity enters at Lemma 2) | N-3 | SAME; R2 sharpens: Lemma 1 holds on ALL of 𝒞^1O (their DATA 225 o-cyclic pure states, 0 failures; my inst runs on the o-cyclic controls also had L1 0 failures at 37 checked states), so the o-cyclic obstruction sits exactly at Lemma 2. I accept |
| B4 (Iσ_k ≠ ∅ at a pure transition needs the Odd-fallback case) | G-1OA-5 | SAME finding, same argument (S4b returns τ_k with Iτ ≠ ∅ ⇒ Odd's S4c switches o; box 21 Theorem B (a)) |
| B5 (R17 Cor. 2 from any start) | §2 (c) CONFIRMED | same |
| B6 (counting slack) | step 6 (R2: blocks ≤ C_X + d) | same conclusion: the stated bound holds |
| (P) row | G-1OA-4 | SAME; R2 records that my R-N5-1P §3 route (a) derivation exists and that they have not refereed it; their DATA 2,283 improvement-free strategies all optimal |
| S1 ((11)'s asserted halves via R17 (a)) | — | mine only (citation completeness); no disagreement |
| S2 (Lemma S (b) needs R15 (d): σ_{k+1} = Switch_I(σ_k)) | G-1OA-6, second half | SAME |
| — (MISSED by me) | G-1OA-6, first half: Lemma S (c)/(d) hold for S4a steps only, not for S4c fallback steps (box 21's Lemma W: W can drop there) | ACCEPTED. My §4 signed (c) as "S4a's output is the pointwise maximum", which is the true statement, but I did not flag that the text's "σ_{k+1} maximises V_{·,τ_k} over A(σ_k)" is false at fallback iterations (the fallback's σ_{k+1} ∈ A(σ_k) is not the optimum). (B) uses only Lemma S (a)-(b), so nothing signed in (B) is affected |
| — | N-2 (Lemma 2 cites "(F1) in the dual" for S4b's optimum; it is VJ00 (11) itself) | I had the same remark inline (§3 Lemma 2 (iv): "(11), directly, not even dualised") without listing it; agreed as a nit |
| B7 (d78e54f / R17 B1: omitted "c even, shorter" case) | — | concerns the withdrawn text and R17's wording (= R-N5-1P G2); not part of the 07f298d object |
The two points the Lead named: G-1OA-5 is my B4, found independently by both with the same repair; G-1OA-6's S4a-only scoping of Lemma S
(c)/(d) is R2's finding alone and is right; (b)'s Switch_I premise is my S2. Both are wording items for the RESULTS gap list (the lane
texts are frozen, Lead 03:50Z).
Data, side by side (independent code on both sides, n5.py unmodified on both): R2 1,147 random o-acyclic games + 1,315 o-cyclic controls +
20 composed games with long X runs (16 changes at |X| = 16) + statY_12 + i4_hand; me 7,200 random o-acyclic runs with a generator biased to
pure transitions (2,707 pure transitions, 2,380 blocks) + statY_12 + i4_hand + the o-cyclic controls. One thing R2's §6 says that is no
longer so: "No instance with a long pure block on an o-acyclic game is in the fleet". L-RED's block_bk20 / block_bk32 (trunk 7f351fc,
R58 §10; Lead data addendum 03:38Z, after R2's push) have single pure blocks of 27 and 49 iterations (49 > |Y| = 33); my probe: Lemmas 1-3
at all 76 pure transitions, each block = n5.py's run on G_τ step for step, 0 violations (§0). These are the first sharp tests of Step 5.
Disagreements: none. Final verdicts (Fable 5.1), unchanged: (A) Prop X SIGNED WITH GAPS A1-A2 (= G-1OA-1, -2, N-1; closed as wording,
with R2's tie-break-free count accepted); Cor. X1 SIGNED (reading); (B) SIGNED CONDITIONAL ON (P) WITH GAPS B1-B6 (= G-1OA-3, -5, N-2, N-3;
closed), with (P) = G-1OA-4 the only non-refereed premise, used on one-player G[X] only and re-derived in R-N5-1P §3 route (a) as a REFEREE
reading; Lemma R SIGNED; Lemma S SIGNED WITH GAPS S1, S2 and R2's G-1OA-6 first half (accepted). Joint gap list for the RESULTS entry:
G-1OA-1..6 with my A1, A2, B2, B3, S1, S2 folded in as above; all closed as wording or by derivation except (P) (conditional) and the
inherited DATA gap G-N1.

## C2. Addendum (Lead 03:57Z; written 04:01Z-04:08Z by date -u): the signed object is the d78e54f text; REFEREE-2's §7 (referee-2 3188622,
trunk 98f16c8) read
Both referees have now checked both texts. Against R2's §7 and its full gap list G-1OA-1..6, N-1..N-5, with the d78e54f text as the object:
| mine | theirs | status |
|---|---|---|
| A1, A2 (Prop X; R58 §9 identical at both pins) | G-1OA-1, G-1OA-2, N-1 | as in §C: same findings; R2's tie-break-free count accepted |
| B1, B3, B4, B6 | G-1OA-3, G-1OA-5 (07f298d only) | both sides: CLOSED by the d78e54f text itself (Lemma 1 preamble and in-place case analysis; Step 5's Odd-fallback sentence; Step 6's count) |
| B2 (flat case at an arbitrary state) | G-1OA-3 | CLOSED by d78e54f, which proves it in place from (★); R2 adds the equivalent view "ρ₁ is again a pointwise optimum of its own arena, so (★) re-applies", which I accept as the cleaner justification of the sequential flat switches |
| B5 | §2 (c) | CONFIRMED both |
| B7 (d78e54f Lemma 1 (b), B1: omitted "c even, shorter" case) | N-4 | SAME finding (= R17's G2 / G-1P-1 inherited), same conclusion: contradicts (★) too; wording |
| — (MISSED by me) | N-5: Lemma 3's formula "(c, P(π_v) ∪ P(continuation), \|π_v\| + ℓ)" should read \|π_v\| + 1 + ℓ (o lies between π_v and the continuation; o ∈ P iff o is more relevant than c) | ACCEPTED; harmless, the same for both plays, so Lemma 3's conclusion stands |
| (P) row | G-1OA-4 | same: the only non-refereed premise, one-player G[X] only, cases (a) and (b); R-N5-1P §3 route (a) derivation noted by both |
| inline in §3 Lemma 2 (iv) | N-2 ("(F1) in the dual" is (11) itself) | same, nit |
| B3 (o-acyclicity enters at Lemma 2) | N-3 (Lemma 1 holds on all of 𝒞^1O) | same, accepted (§C) |
| S1, S2 | G-1OA-6 (both halves) | S2 = second half; first half (Lemma S (c)/(d) for S4a steps only) accepted as missed by me (§C); S1 mine only |
Data: both referees ran L-RED's block_bk20 / bk32 with independent code and found the same: single blocks of 27 and 49, all lemmas at every
pure state, the block = N5 on G_τ, 0 violations.
Disagreements: none. Final verdicts for the d78e54f object (Fable 5.1): (A) Prop X SIGNED WITH GAPS A1-A2 (= G-1OA-1, -2, N-1; wording);
Cor. X1 SIGNED (reading); (B) SIGNED CONDITIONAL ON (P) WITH GAPS B7 (= N-4) and N-5 (wording), B1-B6 closed by the text or confirmed;
Lemma R SIGNED; Lemma S SIGNED WITH GAPS S1, S2 and G-1OA-6 first half (wording). Joint open list for the RESULTS entry: (P) = G-1OA-4
(conditional, by design), wording items G-1OA-1, G-1OA-2/N-1, G-1OA-6, N-2, N-4 (= B7), N-5, S1; inherited DATA gap G-N1.
