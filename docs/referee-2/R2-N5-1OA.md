# R2-N5-1OA: second-referee check of Proposition X / Corollary X1 (L-RED) and the o-acyclic 𝒞^1O theorem (L-NEW box 24). REFEREE-2, 2026-10-24 03:35Z (date -u)
Signature: (Fable 5.1). Packet P-N5-1OA (Lead 03:20Z), pinned at trunk claude/vibrant-johnson-nxvvxo 07f298d; RE-PINNED by the Lead
(03:27Z, read by me after my 603cb3a4 push) at d78e54f, whose docs/new/N5-1Oacyc-box24.md (sha1 d3550267…) is a rewritten, self-contained
packet. §1-§6 below were written against 07f298d; §7 re-checks every finding against the d78e54f text and says which version each refers
to. (A), Lemmas R/S, R17, R15, the SPEC and the engine are identical at both pins (empty diff).

Objects:
- (A) docs/red/R58-n5-width.md §9 at 07f298d: Proposition X and Corollary X1 (L-RED successor 13, PROVED, unrefereed).
- (B) docs/new/N5-1Oacyc-box24.md at 07f298d: N5 on o-acyclic 𝒞^1O makes fewer than (C_X + d)(B + 1) iterations from any start pair
  (L-NEW successor 8, PROVED, unrefereed), with its Lemmas 1-3 and steps 5-6.
- Dependencies refereed here: docs/new/N5-time-box21.md §2.1 Lemma R and §2.2 Lemma S (unrefereed); RESULTS R17 re-read at the two
  places the Lead named (Case B at an arbitrary state; Corollary 2 from any start); the SPEC docs/new/N5-ssi-global.md S1-S5 (S4c included);
  R15 (c)/(d) for the τ count. Premise (P) = VJ00 Lemma 5.8 "1 ⇒ 2" ("no improving edge ⇒ optimal"): used ONLY in (B) Lemma 1, on the
  one-player game G[X]; (B) is signed conditional on (P) for one-player games, as the Lead allowed.
Inputs read: the two objects; box 21 §0, §2, §3 (3.1-3.6); R58 §1-§2 (Theorem W, premise (P)); R17 (as landed, with its honest limits);
R15; the SPEC; experiments/new/n5.py and experiments/si/si.py (unchanged since the R17 pin 26905f0: empty diff), experiments/new/box21/n5x.py,
h1.py, box22/pureY.py, statcheck.py (read-only, to learn the lane's measurements). I did not read docs/referee/ before pushing this report.
Tools (docs/referee-2/R2-N5-1OA/, own code): oa_check.py (replays n5.py's loop read-only from a worktree of 07f298d and checks every
claim below with my R2-N5-1P definitions: own play following, VJ00 order, improving edges, play-maximum optimum, honest valuation as the
pointwise minimum over Odd's d choices at o), compose.py (o-acyclic games whose X part is a long R17 instance); logs/ (every run, every
instance with sha1 in logs/instances.sha1).

## Verdicts (Fable 5.1)
| item | verdict | gaps |
| --- | --- | --- |
| (A) Proposition X (R58 §9) | SIGN WITH GAPS | G-1OA-1 (statement: prefix / whole run), G-1OA-2 (step 1 is an engine-level claim: checked against si.py; the COUNT is tie-break-free, §1), N-1 (vertex order of G[X]) |
| (A) Corollary X1 | SIGN | — (follows from Prop X; "⇐ (SEG-1O) alone" is a reading, superseded by (B)) |
| (B) box 24 theorem, conditional on (P) for one-player games | SIGN WITH GAPS | G-1OA-3 (Lemma 1's pointer to "R17 Case B": the needed statement is the single-switch analysis at an arbitrary state, §2), G-1OA-4 ((P) is the only non-refereed premise; where it enters), G-1OA-5 (step 5's "otherwise the iteration would move τ" needs the Odd fallback case), N-2 (citations), N-3 (Lemma 1 holds on all of 𝒞^1O) |
| Lemma R (box 21 §2.1) | SIGN | — (the same statement as R2-N5-1P §2 (i)) |
| Lemma S (box 21 §2.2) | SIGN WITH GAPS | G-1OA-6 ((c) holds for S4a steps, not for S4c steps; (b) needs σ_{k+1} = Switch_I(σ_k), which S4a/S4c give) |
| R17 re-read: Case B at an arbitrary state; Corollary 2 from any start | CONFIRMED | §2 (c) |
Scope: as both lanes say, this is a bound on N5 ITSELF on a class that is polynomial by other means (d one-player games); not a TARGET.md
claim; G-N5-TIME stays open; the o-CYCLIC case is untouched (Lemma 2 fails there, §4 negative control).

## 1. (A) Proposition X, step by step
Setting. 𝒞^1O; X = vertices with no path to o; X is closed under successors (a successor of x ∈ X reaching o would give x a path to o),
o ∉ X, every Odd vertex in X has out-degree 1. So G[X] (X with its induced edges; every vertex keeps a successor) is a one-player game in
R17's sense. ✓ (X = ∅ makes the statement vacuous.)
Step 1 (locality). Three different claims are bundled, and I separate them:
- (1a) Values: plays from x ∈ X stay in X, so Ξσ(x) (Odd has no choice on the play) and every W(x) depend on σ|X only; hence Iσ restricted
  to X depends on σ|X only (S2 compares Ξ at successors, all in X). ✓
- (1b) The arena optimum: in S4a's arena the option set of x ∈ X is {σ(x)} ∪ Iσ(x) ⊆ X, the same as in G[X]'s arena at σ|X. The global
  optimum σ_new is pointwise optimal (R17 (F1), VJ00 (11) in the dual), so at every x ∈ X its value is the maximum over all global arena
  strategies, which equals the maximum over G[X]'s arena strategies (plays from X stay in X; every G[X]-arena strategy extends). So
  σ_new|X is a pointwise-optimal strategy of G[X]'s arena at σ|X. ✓ This is tie-break-free and is all that the COUNT needs (below).
- (1c) The engine's CHOICE among optimal strategies: R58's five bullets claim that si.py's S1 procedure, run on the dual of the global arena,
  returns on X exactly what it returns on the dual of G[X]'s arena. I checked each bullet against si.py Engine.evaluate (lines 94-204 at
  07f298d, identical to the R17 pin): (i) cycle test and cycle-node DFS use successors only, and X's successors lie in X; alive status of
  X vertices is the same (a Y cycle node's R set is "alive vertices reaching it", which contains no X vertex); (ii) for an Even-liked
  u ∈ Y: M = reach(v, u) contains every X vertex of R (their paths to v stay in X), so no X vertex gets u in its path set and no X edge
  is deleted (X edges end in X ⊆ M); (iii) for an Odd-liked u ∈ Y: M = reach(u, v) contains no X vertex; (iv) for u ∈ X the sets M and the
  deletions restricted to X are those of G[X] (membership of an X vertex in M depends on its paths, which stay in X); (v) longest-path
  recursion: hs[x] for x ∈ X lists X vertices only, same order; BFS over predecessors: Y vertices in a layer discover only Y vertices
  (no X vertex has a Y successor), so the X vertices' relative FIFO order and first discoverers are those of G[X]'s BFS; the cycle-node
  DFS at an Odd cycle node v ∈ X (dual: an Even vertex of G) explores X only. The processing order of cycle nodes (increasing reward)
  restricted to X is G[X]'s. Vertex ids: the engine's index tie-breaks (sorted successor lists, (Ω, v) rank ties, S4c's larger index) are
  preserved iff G[X] keeps the index ORDER of X (N-1). So (1c) holds: the X-part of the global S4a output equals G[X]'s S4a output at σ|X,
  and the same for the S4c rule (its key (Ξσ(w), w) is local by (1a)). ✓ (DATA: §4, exact equality of the runs on 1,882 games.)
Step 2 (steps). If the X-part of S4a is null, σ|X waits; every later global S4a at the same σ|X returns the same null X-part (same
deterministic computation, (1a)-(1c)), so σ|X next changes only by a global S4c, whose X-part is G[X]'s S4c at σ|X. G[X]'s N5 would fall
back at that state iff Iσ|X ≠ ∅ (its S4a is null there), and if Iσ|X = ∅ the X-part of the fallback is empty. After G[X]'s fallback
Iσ|X = ∅ for ever (R17 Corollary 2: the fallback is terminal), so σ|X never changes again. ✓ A global Odd-side fallback (Iσ = ∅) touches
no X vertex. ✓
Step 3. So the sequence of consecutive-distinct σ|X is a PREFIX of N5's run on G[X] from σ_0|X (distinctness is unambiguous: that run
never repeats a strategy, R15 (c)). It is the WHOLE run when the global run terminates (R15 (d)): at the end Iσ = ∅, so Iσ|X = ∅ and G[X]'s
run has also ended; and it is the whole run anyway in the sense that σ|X can only stop changing when Iσ|X = ∅ or when it waits for a
global fallback that must come (Y cannot move for ever, R15). G-1OA-1: the statement should say "prefix, and the whole run since N5
terminates". ✓
Count. Changes of σ|X ≤ N5's iterations on G[X] < (|X|² − |X| + 1)(|X| + m_X) = C_X (R17 Corollary 2, any start). ✓ Tie-break-free
version (G-1OA-2): even without (1c), every change of σ|X is a strategy-changing pointwise-optimal arena step of G[X] (by (1b)) or G[X]'s
S4c switch-all in the value-flat situation (terminal), so R17 Corollary 1 + the fallback bound the number of changes by the same C_X
for ANY optimum selection. So the count does not depend on the engine's internals; only the "is N5's run" identity does.
Corollary X1. If every successor of o is in X: θ = Ξ(o) = min over exits e of o ⊕ Ξ(e) (Ξ(o) = Θ_{σσ̄}(o) by (11), σ̄(o) an Ω-minimal exit,
exits' values independent of Odd's choice) depends on σ|X only, so it changes at most as often as σ|X: fewer than C_X times ✓; w = W(o)
= o ⊕ Ξ(τ(o)) changes only with σ|X or τ, τ at most d − 1 times (R15 (c) on G^d: every τ change is Switch_I with ∅ ≠ I ⊆ Iτ, S4b/S4c,
strictly up, so τ never repeats among its d values) ✓. The "⇐ (SEG-1O) alone" sentence is a reading via box 21 §3.6's decomposition,
now superseded by (B). The READING about kills and the instance remarks (fts_best16, frz24 have X = ∅) are not signed and not disputed.
DATA (own, §4): on 1,882 random 𝒞^1O games with X ≠ ∅ (o-acyclic and o-cyclic), and on 20 composed games whose X part is rel_g12 /
rel_g16 / sb1_counter_n10 / ph_n16 / fl_n16 with 9-16 changes of σ|X each, the distinct-σ|X sequence equals N5's run on G[X]
(order-preserving renumbering) exactly; every one of the 1,531 changes of σ|X is a pointwise optimum of G[X]'s arena by my play maximum;
0 failures.

## 2. (B) The box 24 theorem, step by step (conditional on (P) for the one-player game G[X])
Facts 0. o-acyclic ⇔ every successor of o lies in X (an exit reaching o would close a cycle through o; conversely an exit in X cannot
reach o). X closed, no Odd choice in X. ✓
Step 1 (non-pure transitions). Changes of σ|X < C_X (Prop X, §1 count, tie-break-free); τ changes ≤ d − 1 (above). A non-pure transition
changes σ|X or τ, so there are at most (C_X − 1) + (d − 1) ≤ C_X + d − 1 of them. ✓
Lemma 1 (at a pure transition from state k, σ_k|X has G[X]'s optimal valuation). The transition is one global iteration with τ_{k+1} = τ_k and
σ_{k+1}|X = σ_k|X. Cases: (i) S4a ran (Iσ ≠ ∅) and no fallback: the X-part of the pointwise-optimal σ_{k+1} equals σ_k|X, so by (1b)
σ_k|X is itself a pointwise optimum of G[X]'s arena at σ_k|X. Then the SINGLE-SWITCH analysis at an arbitrary state (R2-N5-1P §3a,
Corollary 2 paragraph = G-1P-5; restated in (c) below) shows every improving edge in X is a value-flat cycle-closer at an own cycle node;
switching all of them at once leaves the valuation unchanged (the return path of each switched z_x to x contains no other switched vertex,
R2-N5-1P G-1P-2) and leaves no improving edge in X; so Ω_{σ_k}|X is the valuation of a strategy of G[X] with no improving edge, which (P)
makes optimal. (ii) The iteration was a global Even fallback (S4c with Iσ ≠ ∅): pure means it switched no x ∈ X, and S4c switches every x
with Iσ(x) ≠ ∅ to a successor ≠ σ(x), so Iσ|X = ∅: optimal by (P). (iii) Iσ = ∅: then Iσ|X = ∅, optimal by (P) (and in fact this
iteration moves τ, see step 5, so it is not pure). ✓ G-1OA-3: the box cites "R17's case analysis (box 10 §2, Case B …)"; box 10's Case B
proves Ω_{k+1}(x) ⪰ value(r), not the contradiction needed here, and its B1 lacks the "x not its own cycle node / own cycle node" split of
the avoid-x case. The statement actually needed is: if σ is a pointwise optimum of its own arena, every improving edge is a flat
cycle-closer at an own cycle node; it is proved in R2-N5-1P §3a (and REFEREE's R-N5-1P §4 G4) and signed in R17 (e). Pointer fix only.
N-3: nothing in Lemma 1 uses o-acyclicity; it holds at every pure transition on all of 𝒞^1O (DATA: 225 pure states on o-cyclic games, 0
failures). G-1OA-4: (P) enters here and nowhere else in (B) (Prop X and R17 do not use it); for the one-player game G[X] REFEREE's
R-N5-1P §3 route (a) gives a derivation by dualising VJ00 Lemma 5.5's proof, which I read after my R2-N5-1P push and have not refereed;
my DATA: 2,283 strategies of G[X] with no improving edge, all pointwise optimal (§4).
Lemma 2 (θ_k = w_k). For an exit e ∈ X: Ξ^d_τ(e) is τ's G^d-valuation against the G^d-Odd (= G-Even) best counter-strategy, i.e. the
G^d-pointwise-minimum over Even strategies σ' of Θ_{σ'τ}(e) (VJ00 (11) on G^d), which by Lemma R is the G-order maximum
U_τ(e) = max_{σ'} V_{σ',τ}(e) (Lemma S (a)); the plays from e stay in X with no Odd choice, so this is G[X]'s optimal value at e, which
equals Ξ_k(e) by Lemma 1. ✓ θ = Ξ(o) = o ⊕ Ξ(a) with a = σ̄(o) an Ω-minimal exit ((11): Ξ(o) = Θ_{σσ̄}(o)), w = o ⊕ Ξ(b) with b = τ(o)
(V_{σ,τ}(b) = Ξ(b): the play from b avoids o), so θ ⊴ w. If θ ◁ w then Ξ(a) ◁ Ξ(b) (prefix by o strictly monotone, (V2); the paths from a, b
avoid o; different cycle nodes decided first), hence Ξ^d_τ(a) ◁ Ξ^d_τ(b) in G's order, i.e. a is better for Odd than b in G^d's order:
(o, a) ∈ Iτ (S2 on G^d). So Iτ ≠ ∅ and S4b runs: τ_{k+1} = Odd's optimal counter-strategy to σ_k in the arena H′ (o restricted to
{b} ∪ Iτ(o) ∋ a), pointwise optimal by VJ00 (11) directly (the box says "(F1) in the dual": (11) itself, N-2). At o the option e gives the
value o ⊕ Ξ(e) whatever else Odd does (plays from exits avoid o), and a is strictly better for Odd than b, so τ_{k+1}(o) ≠ b: the
transition is not pure, contradiction. ✓ (Both S4 steps are computed from the same (σ_k, τ_k), SPEC A6, so S4b's output is τ_{k+1}
unless the fallback fires, which needs τ_new = τ.)
Lemma 3 (Ξ_k = W_k). A vertex whose σ_k-play never meets o meets no Odd choice: the (σ, σ̄)- and (σ, τ)-plays coincide ✓. A vertex v
whose σ_k-path reaches o: π_v ⊂ Y (vertices reaching o are in Y), then o, then the continuation from a (for Ξ) or from b (for W), both in
X and never returning to Y. θ = w gives o ⊕ Ξ(a) = o ⊕ Ξ(b), hence Ξ(a) = Ξ(b) as triples (o is in neither path set). So both plays
from v have the same cycle node, path set ((π_v ∪ {o}) ∩ V_{>c} ∪ P(a)) and length (|π_v| + 1 + ℓ(a)). ✓ (For v = o this is Lemma 2.)
Step 5 (a pure transition is N5's step on the one-player game G_{τ_k}). Gate: Iσ_k is computed from Ξ_k = W_k = V_{σ_k,τ_k}, the
valuation of G_τ, with the same edges: Iσ_k = I^{G_τ}(σ_k) ✓. S4a: the same arena, the same engine call (n5.py builds the arena with
Odd's successors [τ(v)], exactly G_τ's) ✓. S4b produced τ_k (pure) and on G_τ Iτ = ∅ ✓. S4c: on G it fires iff σ_new = σ_k and τ_new = τ_k;
τ_new = τ_k holds, so iff σ_new = σ_k, which is when it fires on G_τ; same rule, same keys (Ξ = W) ✓. Iσ_k ≠ ∅: if Iσ_k = ∅ the
iteration has Iτ ≠ ∅ and either S4b changes τ or (S4b returns τ_k and σ_new = σ_k) the ODD fallback fires, which changes τ(o) to an
improving exit ≠ τ_k(o); either way not pure (G-1OA-5: the box's "otherwise the iteration would move τ" is right but needs this second
case, box 21 Theorem B (a) spells it out). ✓ So σ_{k+1} = F_{τ_k}(σ_k), N5's step on G_{τ_k}, and a maximal pure block from state k is a
prefix of N5's run on the one-player game G_{τ_k} from the arbitrary start σ_k. R17 Corollary 2 from any start bounds it by
< B = (n² − n + 1)(n + m_τ) ≤ (n² − n + 1)(n + m). ✓
Step 6 (counting). Blocks ≤ non-pure transitions + 1 ≤ C_X + d; iterations ≤ (C_X + d − 1) + (C_X + d)(B − 1) < (C_X + d)(B + 1). ✓
(c) R17 re-read, as the Lead asked.
- Case B at an arbitrary state: R17's Lemma P is stated for ρ_0..ρ_k in one phase with ρ_0 arbitrary (every strategy is the ρ_0 of its
  phase), and its Case B computes val_ρ̂(x) for ρ̂ = ρ_k[x → z] at the arbitrary in-phase state ρ_k: (x, z) ∈ I_k; c = λ_k(z), π = z's
  path; x ∉ π and x not on c's cycle ⇒ val_ρ̂(x) = x ⊕ Ω_k(z); x on c's cycle, x ∉ π ⇒ val_ρ̂(x) has cycle node max P(π) (even, better)
  or equals (c, ∅, |π| + 1) = x ⊕ Ω_k(z); x ∈ π ⇒ val_ρ̂(x) has a better cycle node unless D = ∅ and top(Z) = c = x, where it equals Ω_k(x).
  Nothing in that computation uses the phase or the induction; the phase enters only to turn "better cycle node" into a contradiction.
  Applied to a state σ that is a pointwise optimum of its own arena (val_ρ̂(x) ⪯ Ω_σ(x) for every improving single switch): the avoid-x case
  gives x ⊕ Ω(z) ≻ x ⊕ Ω(σ(x)) = Ω(x) by strict (V2) when x is not its own cycle node, and a better cycle node when it is (λ(z) ≠ x and
  Ω(z) ≻ Ω(σ(x)) with cycle node x); the on-cycle and in-π cases give a better cycle node or a strictly longer odd-cycle value ≻ Ω(x);
  all contradict, except the flat case. This is R2-N5-1P §3a's Corollary 2 argument; CONFIRMED again here and used in Lemma 1 (i).
- Corollary 2 from any start: R17's Theorem PH and phase count hold for every run ρ_0, ρ_1, … of switch-best from any ρ_0 (the phase
  decomposition and Lemma P need no property of ρ_0), and the N5 identification (S4a = arena optimum, S4c = terminal flat fallback) holds
  at every state. So the bound < (n² − n + 1)(n + m) applies to N5 on a one-player game from any start, in particular to a block of (B)
  starting at σ_k. CONFIRMED (my R2-N5-1P data used random starts and .start files; §4 here uses random start pairs as well).

## 3. Lemmas R and S (box 21 §2.1-2.2)
Lemma R. rank^d = rank ((Ω + 1, v) orders V as (Ω, v)); parities flip; so Reward^d = −Reward, the set order reverses (B ≺^d C iff C ≺ B:
MaxDiff's side and parity both flip), and the length rule reverses with the cycle node's parity. The same derivation as R2-N5-1P §2 (i).
SIGN. (Nit: "weight^d = −weight" is the encoding; the statement is about the order, and holds for it.)
Lemma S. (a) L_σ(v) = min_{τ′} V_{σ,τ′}(v) is VJ00 (11) (Θ_{σσ̄} = Ωσ = min over plays; the min over Odd strategies equals the min over
plays since every play is realised by a positional strategy); U_τ(v) = max_{σ′} V_{σ′,τ}(v) is (11) on G^d read through Lemma R. ✓
(b) L ⊴ V_{σ,τ} ⊴ U is immediate; monotonicity of L_{σ_k} in k is R15 (a) applied to σ_{k+1} = Switch_I(σ_k), ∅ ≠ I ⊆ Iσ_k, which holds for
S4a (σ_new ∈ A(σ_k)) and S4c, or σ_{k+1} = σ_k; U_{τ_k} the same on G^d. ✓ G-1OA-6 (wording): say so.
(c) "σ_{k+1} maximises V_{·,τ_k} pointwise over A(σ_k)" holds when σ_{k+1} is S4a's output ((F1) on the one-player arena G_{τ_k} ∩ A(σ_k));
it is FALSE for an S4c fallback step (the fallback's strategy is in A(σ_k) but is not the optimum; box 21's own Lemma W says W can drop
there). The heading "Arena steps" scopes it; the statement should say "S4a steps" (G-1OA-6). The best-reply clause and Odd's symmetric
statement ✓. (d) SSI's switch set Iσ ∩ {(v, τ̄(v))} ⊆ Iσ, so SSI's strategy lies in A(σ_k) and is dominated by S4a's output in V_{·,τ_k}
✓ (again for S4a steps; "says nothing about iteration counts" ✓). SIGN WITH GAPS (G-1OA-6).

## 4. Mechanical checks (own code, logs/)
oa_check.py replays n5.py's loop (unmodified functions, read-only) and checks, with my definitions: (A) the distinct-σ|X sequence equals
N5's run on G[X] (order-preserving renumbering) and each change of σ|X is a pointwise optimum of G[X]'s arena (play maximum) or its
flat fallback, and changes < C_X; (B) at every pure transition Lemma 1 (Ω_σ|X = my pointwise maximum over ALL plays of G[X]), Lemma 2,
Lemma 3, gate = G_τ's improving set, step 5 (σ_{k+1} = n5.py's own step on G_τ, and an arena optimum of G_τ by my play maximum, or its
flat fallback), block length < B, non-pure transitions ≤ C_X + d − 1, total < (C_X + d)(B + 1), τ changes ≤ d − 1; the engine's Ξ equals my
pointwise minimum over Odd's d choices; (P) on G[X] by brute force over all strategies when ≤ 3,000. Random 𝒞^1O games: one Odd choice
vertex (out-degree 2-4), other Odd vertices forced (prob. 0.2), Even out-degree 1-3, priorities 0..n+2.
| batch (logs/) | games | iterations | pure transitions / blocks | changes of σ|X (all arena optima) | (P) strategies | max τ changes | violations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| o-acyclic, canonical start, n 5-12 (oa_r12) | 410 | 377 | 28 / 26 | 308 | 513 | 2 | 0 |
| o-acyclic, random start pairs, n 5-12 (oa_r12rs) | 431 | 613 | 26 / 26 | 522 | 559 | 2 | 0 |
| o-acyclic, canonical, n 10-18 (oa_r18) | 143 | 208 | 6 / 6 | 193 | 159 | 2 | 0 |
| o-acyclic, random starts, n 10-18 (oa_r18rs) | 163 | 312 | 15 / 10 | 279 | 237 | 3 | 0 |
| all 𝒞^1O, n 5-10 (oa_cyc): 185 o-acyclic + 1,315 o-cyclic | 1,500 | 1,393 | 688 / 582 | 229 (735 games with X ≠ ∅) | 815 | 3 | 0 on the o-acyclic games; on the o-cyclic ones (negative control) Lemma 2 fails at 42 pure states, Lemma 3 at 42, gate at 10, step 5 at 4; Prop X exact 0 failures, Lemma 1 0 failures (225 checks) |
Instances (sha1 in logs/instances.sha1): statY_12 (o-acyclic, 8 iterations, 7 pure states: all lemmas hold), i4_hand + start (5 iterations,
4 changes of σ|X all arena optima, 1 pure state: holds). Composed games (compose.py: X = rel_g12 / rel_g16 / sb1_counter_n10 / ph_n16 /
fl_n16 with their .start, Y = 4-7 random Even vertices and o with 2-3 exits into X; 20 games): the distinct-σ|X sequence equals N5's run on
G[X] in all 20, with 9-16 changes each; 0 violations. Negative controls (o on a cycle, outside (B)'s hypothesis): fts_best16 (28 pure
states): Lemma 2 fails at 24 of 28 and Lemma 3 at 24 (= the box's "L1 and L2 fail at 24 of 28"), step 5 at 25; Lemma 1 holds at every
checked state; oneodd_c16 / oneodd_c24: Lemma 2/3 fail at most pure states. Random o-acyclic games have at most 3 consecutive pure
transitions, so the DATA tests the lemmas, not the bound's tightness (as the lane says).
Totals on o-acyclic games: 1,147 random + 22 instances; 1,510 + random-start iterations; 75 + 8 pure transitions checked for Lemmas 1-3,
gate and step 5; 1,531 changes of σ|X all pointwise arena optima of G[X]; 2,283 no-improving-edge strategies of G[X] all optimal; 0 violations.

## 5. Gap list
- G-1OA-1 (statement, wording): Prop X's "is N5's run on G[X]" is "a prefix of it, and the whole run because N5 terminates (R15 (d))".
- G-1OA-2 (closed here): step 1 (1c) is an engine-level claim (si.py's tie-breaks are local to X); verified against the code and on data.
  The COUNT is tie-break-free by (1b) + R17 Corollary 1, so Prop X's bound does not depend on (1c). Suggest stating both forms.
- G-1OA-3 (pointer, closed): Lemma 1's flat case needs "a pointwise arena optimum has only flat improving edges", R2-N5-1P §3a / R17 (e),
  not box 10 §2 Case B as written.
- G-1OA-4 (premise, OPEN by design): (P) for one-player games, used only in Lemma 1 (both cases). The bound (B) is conditional on it. A
  derivation for one-player games exists (REFEREE R-N5-1P §3 route (a)); not refereed by me. DATA: 2,283 strategies, 0 failures.
- G-1OA-5 (wording, closed): step 5's "Iσ_k ≠ ∅: otherwise the iteration would move τ" needs the Odd-fallback case (S4b returns τ_k, then
  S4c switches o), as in box 21 Theorem B (a).
- G-1OA-6 (Lemma S, wording): (c)/(d) hold for S4a steps only, not for S4c steps (Lemma W); (b) needs "σ_{k+1} = Switch_I(σ_k) or σ_k".
- Inherited DATA: G-N1 = G-N5T-1 (engine = VJ00's Ωσ / arena optimum / counter-strategy); here +1,510 iterations with Ξ equal to my
  pointwise minimum and every S4a X-part / pure step an arena optimum by my play maximum.
Nits: N-1 (G[X] must keep X's index order for the engine's tie-breaks; R58's xlocal.py presumably does; the statement should say so).
N-2 (Lemma 2 cites "R17 (F1) in the dual" for Odd's S4b optimum: it is VJ00 (11) itself; Lemma 2's first bullet cites Lemma S (a) for the
dual, fine). N-3 (Lemma 1 holds on all of 𝒞^1O; only Lemma 2 needs o-acyclic, through "exits in X"; worth saying, since the o-cyclic
obstruction is then located exactly at Lemma 2: the exit a's honest value is not G[X]-optimal when a can route back through o).

## 6. Things only the data say
- On random 𝒞^1O games the lemmas' hypotheses are rarely exercised (≤ 3 consecutive pure transitions); the composed games exercise Prop X
  with long X runs (16 changes at |X| = 16) but their Y parts settle quickly. No instance with a long pure block on an o-acyclic game is
  in the fleet; the bound's slack is untested, which does not affect the proof.

## 7. Re-pin d78e54f: the rewritten box 24 checked, finding by finding (03:49Z by date -u)
The d78e54f text (sha1 d35502679af112e9fa31eb3af99e64fb4afda1ba) keeps the theorem, the six steps and the dependencies of the 07f298d
sketch and writes out what the sketch pointed to. Checked line by line against §2 above:
- §1 definitions ✓ (X closed under successors; G[X] one-player; pure / block / C_X / B as I used them). §2 theorem: the same statement,
  now explicitly "assume (P) (§4)" and "from any start pair" ✓.
- Step 1 ✓: now cites R15 (c) for "no τ value repeats" with the S4b/S4c switch description; "fewer than C_X + d − 1" ✓.
- Step 2 (Lemma 1): the flat case is now PROVED IN PLACE, "the cases of R17's Lemma P, Case B, without its induction hypothesis", with
  (★) Ω(x) ⪰ val_ρ̂(x) and the B1 split into "x not its own cycle node" (strict (V2)) and "x its own cycle node" (better cycle node c ≠ x);
  this is the argument of my §2 (c). G-1OA-3 (the pointer gap) refers to the 07f298d text and is CLOSED by d78e54f. One wording nit
  remains in B1 (x on c's cycle): the improvement list omits "P(π) = ∅, c even, |π| + 1 < ℓ(x)" (a shortcut), where val_ρ̂(x) =
  (c, ∅, |π| + 1) ≻ Ω(x) contradicts (★) as well; this is R17's G-1P-1 again (N-4, d78e54f). The flat-switch iteration is now sequential
  with the justification "the heads' paths avoid the switched vertices" (the G-1P-2 line) ✓; equivalently, ρ₁'s arena is contained in
  ρ's and Ω_ρ₁ = Ω, so ρ₁ is again a pointwise optimum of its own arena and (★) re-applies. The Remark (only the VALUATION is
  optimal; ρ need not be ≺-maximal; the R15 prio [0, 2, 4] instance) ✓ correct and useful. (P) is used in cases (a) and (b) exactly
  as my G-1OA-4 says; unchanged, OPEN by design (conditional signature).
- Step 3 (Lemma 2) ✓ as in §2; "F1 on the dual" for Odd's S4b optimum is still the N-2 wording (it is VJ00 (11) itself); the line "If
  the iteration's S4a also changes σ, τ still changes, since both are applied (A6)" is right and closes a question I had not raised.
- Step 4 (Lemma 3) ✓; the formula "(c, P(π_v) ∪ P(continuation), |π_v| + ℓ)" should read |π_v| + 1 + ℓ (o lies on the play between π_v
  and the continuation, and o ∈ P iff o is more relevant than c), as my §2 has it; harmless, equal for both plays (N-5, d78e54f).
- Step 5 ✓: "Iσ_k ≠ ∅. Otherwise S4c would have fallen back on Odd, or S4b would have moved τ." G-1OA-5 refers to 07f298d and is CLOSED by
  d78e54f. "Every block has fewer than B transitions" from R17 Corollary 2 at an arbitrary start ✓ (§2 (c)).
- Step 6 ✓: ≤ C_X + d − 1 blocks, total < (C_X + d)(B + 1).
- §4 dependencies ✓: the list is complete (Prop X; (P) with its R15 G-N5T-3 status; Lemma R, Lemma S (a); R17 (a), (b), (c), (e); R15
  (c)-(d); VJ00 (11)); RESULTS line numbers 730 / 624 verified at d78e54f. The sentence "The BFS-discovery-order point in [Prop X's] step 1
  is taken from L-RED's text" is honest; my §1 (1c) checks that point against si.py.
- §5 checks ✓ (the same numbers as 07f298d's; my §4 reproduces the negative control's 24 of 28). §6 scope ✓.
Which finding refers to which version: G-1OA-1, G-1OA-2, N-1 concern Prop X (R58 §9, identical at both pins). G-1OA-3 and G-1OA-5 concern
the 07f298d sketch and are closed by the d78e54f text. G-1OA-4 ((P)), N-2, N-3 concern both versions. N-4, N-5 are new nits on d78e54f.
G-1OA-6 concerns box 21 §2.2 (identical at both pins). The verdict on (B) is unchanged: SIGN WITH GAPS, conditional on (P) for one-player
games, with the open list now G-1OA-4 (by design), N-2, N-4, N-5 (wording).
New data (Lead 03:38Z; trunk 7f351fc, pin unchanged): L-RED's o-acyclic instances with long pure blocks, experiments/red/n5inj/instances/
block_bk20.pg (n 24, sha1 98dc1d8b…) and block_bk32.pg (n 36, sha1 439bff4e…), o's exits = 3 self-loop sinks = X. My oa_check.py: one
block of 27 and of 49 iterations respectively (= R58 §10b), τ fixed, no fallback; Lemma 1, Lemma 2, Lemma 3, gate = G_τ's improving set
and σ_{k+1} = N5's step on G_τ hold at all 27 + 49 pure states; 0 violations (logs/block_bk20.txt, block_bk32.txt, pushed at d5d941a9).
These are the first instances where the lemmas are exercised across long blocks. R58's finding that blocks can exceed |Y| does not touch
the theorem, which bounds blocks by B; agreed.
