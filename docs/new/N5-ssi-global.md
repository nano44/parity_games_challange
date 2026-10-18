# N5 SSI-GLOBAL: symmetric SI, each player's step = its best subset of improving switches against the opponent's CURRENT strategy
(L-NEW box 3, 2026-10-18, by date -u; Lead pick 18:47Z. DATA, unrefereed.)

Order of work (stated plainly): the Lead asked for the "not covered by DLM" text BEFORE code. I checked it against the opened
text first (18:47-18:50Z, below), but wrote n5.py and ran the DLM validation (18:50Z) before writing this file (19:00Z).

## Exact pseudocode (experiments/new/n5.py, mode n5)
VJ valuations (Vöge-Jurdziński; L-SI's engine experiments/si/si.py, imported read-only): Ξσ = valuation of Even's σ against Odd's
optimal counterstrategy σ̄; Iσ = Even's improving edges. Odd's side on the dual game (owners swapped, priorities + 1): Ξτ, τ̄, Iτ.
Start: best-reward start for both (or a given pair, e.g. DLM's (σ0, τ0)).
Loop:
1. If Iσ = Iτ = ∅: stop (both optimal; 2309.02223 Lemma 5 for sink games; in general: no improving switch for σ means σ is
   optimal (classical SI), and the final regions/strategies are checked anyway).
2. Even: A_σ(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ}. σ' = Even's optimal strategy in the arena where Odd plays τ (fixed) and Even's v may
   use only A_σ(v), computed as Odd's optimal counterstrategy on the DUAL of that arena (Engine.evaluate = VJ00's procedure).
3. Odd: A_τ(v) = {τ(v)} ∪ {w : (v, w) ∈ Iτ}; τ' = Odd's optimal counterstrategy to σ in the arena where Odd's v may use only A_τ(v).
4. If σ' = σ and τ' = τ although Iσ ∪ Iτ ≠ ∅ (possible on non-sink games; see below): FALLBACK = one classical switch-all step for
   Even on Iσ (for Odd on Iτ if Iσ = ∅); counted.
5. σ, τ := σ', τ'.
Termination: σ' differs from σ only by edges of Iσ, so σ' is σ with a subset of its improving switches applied: Ξσ' ⊵ Ξσ, strictly
unless σ' = σ (standard SI lemma); the same for τ; step 4 always improves one side. So each iteration strictly improves σ or τ.
Output: Engine.regions(σ) (regions and both players' strategies), checked by check_sol2.py (Oink zlk + harness/verify.py).

## SPEC (EXACT; the reference for an independent implementation; written 2026-10-18 ~20:55Z by date -u). n5.py implements this.
Input: parity game G = (V, E, Ω, owner), V = {0..n-1}, Even = owner 0. Optional start pair (σ0 on Even vertices, τ0 on Odd vertices).
S1 Valuations (Vöge-Jurdziński, as in Friedmann 1106.0778 §3; L-SI's experiments/si/si.py):
  - injective priorities: rank(v) = position of v in V sorted by (Ω(v), v); p'(v) = 2·rank(v) + (Ω(v) mod 2).
  - valuation of v under (σ, σ̄): (c, P, ℓ), c = the most relevant (max p') vertex of the cycle the play from v ends in, P = set of
    vertices on the play before reaching c with p' > p'(c), ℓ = number of steps to reach c.
  - order (better for Even): compare reward of c (p'(c) if even, −p'(c) if odd); then P by the signed weight
    Σ_{u∈P} (+2^rank(u) if Ω(u) even else −2^rank(u)); then ℓ: if c is odd, longer is better for Even; if c even, shorter is better.
  - Ξσ = valuation of every vertex under σ and Odd's OPTIMAL counterstrategy σ̄ (minimising this order at every vertex at once).
  - σ̄ is computed by Vöge-Jurdziński's procedure exactly as si.py Engine.evaluate (lines 78-205): graph Gσ = Even vertices keep
    only σ(v), Odd vertices keep all edges; all vertices "alive". For v in V in increasing order of reward(v) (= p'(v) if even,
    −p'(v) if odd; Odd's preferred cycle nodes first), skipping dead v: (i) v is a cycle node iff DFS from v over Gσ-successors,
    visiting only alive vertices of rank < rank(v), returns to v; otherwise skip. (ii) R = alive vertices that reach v in Gσ.
    (iii) Restricted graph on R; path[x] = ∅. For u in R with rank(u) > rank(v), in decreasing rank: if Ω(u) even (Even likes u):
    M = vertices of R reaching v without passing u; add u to path[q] for q ∉ M; delete edges from u and from every q ∈ M to
    vertices outside M. If Ω(u) odd (Odd likes u): M = vertices of R reaching u without passing v; add u to path[q] for q ∈ M;
    delete edges from every q ∈ M \ {u} to vertices outside M. (iv) Lengths: if Ω(v) even, Odd takes the LONGEST path to v in the
    restricted graph (recursion over successors in list order, first strict maximum wins); if Ω(v) odd, the SHORTEST (BFS from v
    over predecessors in list order; first discovery sets Odd's choice). (v) If v is Odd: its choice is the first successor on a
    DFS-found cycle back to v through alive vertices of rank < rank(v). (vi) Every x in R gets valuation (v, path[x], length[x]) and
    Odd's choice from (iv)/(v); R becomes dead. Successor and predecessor lists are in increasing index order.
  - Odd's side: everything on the DUAL game G^d (owner swapped, Ω + 1); τ is an "Even" strategy of G^d; Ξτ, τ̄ (= Even's optimal
    counterstrategy to τ, as a G^d-Odd strategy), Iτ computed there.
S2 Improving edges: Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than Ξσ(σ(v))}; Iτ the same on G^d for τ.
S3 Start (unless a start pair is given): Even v: σ(v) = the successor w maximising (r(w), w if r(w) even else −w), r(w) = Ω(w) if
  even else −Ω(w) (PGSolver best-reward); Odd v: the same rule on G^d (r computed from Ω + 1).
S4 Iteration (one iteration = one pass with Iσ ∪ Iτ ≠ ∅; both steps computed from the SAME (σ, τ), applied together):
  a. If Iσ ≠ ∅: A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v. Arena H: Even v keeps only edges to A(v); Odd v keeps only the edge
     to τ(v). σ_new = Odd's optimal counterstrategy (S1 procedure) in the dual of H to the dual-Even strategy τ, read as an Even
     strategy of G. (Even's one-player optimum against τ among "keep or take an improving edge".) Else σ_new = σ.
  b. If Iτ ≠ ∅: A(v) = {τ(v)} ∪ {w : (v, w) ∈ Iτ} for Odd v. Arena H': Odd v keeps only edges to A(v); Even v only the edge to σ(v).
     τ_new = Odd's optimal counterstrategy (S1 procedure on H', not dual) to σ. Else τ_new = τ.
  c. FALLBACK, if σ_new = σ and τ_new = τ: if Iσ ≠ ∅, for every Even v with an improving edge set σ_new(v) = the w with (v, w) ∈ Iσ
     maximising (Ξσ(w), w) (best valuation, ties: larger index); otherwise do the same for Odd on Iτ with G^d's valuations. Count it.
  d. σ, τ := σ_new, τ_new.
S5 Stop when Iσ = Iτ = ∅. Output: Even wins v iff the cycle node of Ξσ(v) has even Ω; Even's strategy = σ on Even's region; Odd's
  strategy = σ̄ (Odd's optimal counterstrategy to the FINAL σ, S1) on Odd's region. (Not τ.)
Invariants: each iteration strictly improves σ (in Ξ) or τ (in Ξ on G^d), so the loop terminates; correctness at the stop is
classical SI (σ has no improving edge => optimal). Tie-breaks in S1/S3/S4c fix the exact iteration counts; an implementation with
other tie-breaks should reproduce regions and verified strategies exactly and iteration counts only approximately.
Reference counts for checking a second implementation: dlm1 (DLM start pair) n = 1..6: 1, 2, 4, 4, 6, 7; dlm2 n = 1..7: 2, 4, 7, 8,
11, 12, 13; switchallexp (best-reward start) N = 1..8: experiments/new/n5/switchallexp.csv; mode ssi on dlm1: 2^(n+1) − 3.

### SPEC vs L-COMP's ambiguities A1-A10 (experiments/n5-second/README.md, l-comp 2b6a965 on trunk); successor 2, 2026-10-18 21:06Z by date -u
Line numbers: n5.py = experiments/new/n5.py at this commit (last changed in 334f057, before the spec commit 8925171 L-COMP read); si.py = experiments/si/si.py (trunk, read-only).
| id | settled by | code | note / fix |
| --- | --- | --- | --- |
| A1 rank ties | S1 "rank(v) = position in V sorted by (Ω(v), v)" | si.py l. 38-41 | settled; L-COMP's reading = SPEC |
| A2 best-reward start | S3 | n5.py l. 23; si.py l. 234-240 | settled. Spelled out (FIX 1 below): ties go to the LARGEST index for even r, the SMALLEST for odd r; L-COMP's PGSolver port must match this (the si.py comment "max index" is right only for even r) |
| A3 dual ids / order | S1 "Odd's side ... G^d (owner swapped, Ω + 1)"; "lists in increasing index order" | n5.py l. 18 (same ids, same lists); si.py l. 33 (lists sorted) | settled; ranks of G^d equal those of G (Ω + 1 keeps the order and the index ties) |
| A4 improving edges | S2 (strict, w.r.t. Ξσ at σ(v)) | si.py l. 220-228 | settled; L-COMP's reading = SPEC |
| A5 tie-break of σ', τ' | S1 (iv)-(v) + S4a/b | n5.py l. 47-50, 55-58; si.py l. 152-195 | settled, but L-COMP's reading DIFFERS: SPEC's σ' is the counterstrategy of the VJ procedure (longest-path ties to the smallest index; BFS first discovery; DFS cycle choice at the cycle node), NOT "per vertex the successor of best valuation, ties by index". FIX 2 below pins the DFS order. Counts may differ under L-COMP's rule; regions and verified strategies must not |
| A6 old or new σ | S4 "both steps computed from the SAME (σ, τ), applied together" | n5.py l. 46-48 (old τ), 54-56 (old σ), 65 | settled; L-COMP's reading = SPEC |
| A7 fallback choice | S4c "(Ξσ(w), w) ... ties: larger index" | n5.py l. 59-64 | settled: ties to the LARGER index (L-COMP wrote "ties by index": must be the larger). FIX 3: τ is not changed in an iteration where Even falls back |
| A8 iterations | S4 "one iteration = one pass with Iσ ∪ Iτ ≠ ∅" | n5.py l. 28-32 | settled (final pass with both sets empty is not counted); L-COMP's reading = SPEC |
| A9 output Odd strategy | S5 "σ̄ ... (Not τ.)" | n5.py l. 66; si.py l. 254-264 | settled; L-COMP's reading = SPEC |
| A10 valuation by reference | S1 (full definition, order and procedure) | si.py l. 54-204 | settled for implementation; the VJ00 source citation is box-4 item (4) |
FIX 1 (S3, A2). Even's v: σ0(v) = argmax over successors w of (r(w), w if r(w) even else −w), r(w) = Ω(w) if Ω(w) even else −Ω(w):
highest even priority, else lowest odd priority; equal priorities: largest index if even, smallest if odd. Odd's v (the rule on G^d), in
G's terms: highest ODD Ω(w), else lowest EVEN Ω(w); equal priorities: largest index if Ω(w) odd, smallest if even.
FIX 2 (S1 (v), A5). The cycle node v's own choice (when v is the optimiser's): explicit-stack DFS from v over the successors of the
fixed-strategy graph Gσ (NOT the restricted graph), successors scanned in increasing index, each unvisited alive y of rank < rank(v)
marked visited and pushed when scanned, last pushed popped first; the scan stops at the first successor equal to v; v's choice = the
first vertex after v on the DFS tree path to that vertex (v itself for a self-loop). si.py l. 182-195.
FIX 3 (S4c, A7). In a fallback iteration with Iσ ≠ ∅ only σ changes (τ_new = τ); n5.py l. 61-62. Odd falls back only if Iσ = ∅.
FIX 4 (S1 (iv), A5). "first strict maximum" in the longest-path recursion = smallest index among the successors of maximum length
(si.py l. 160-168); BFS: layers in FIFO order, each layer's vertices scanned in discovery order, predecessor lists in increasing
index, a vertex's choice is the vertex from which it was first discovered (si.py l. 176-180). Every Odd vertex x ≠ v of R gets
the choice, including those whose valuation is not affected.

## Why N5's step is NOT covered by 2309.02223 (opened pdf, sha256 10e6794d82aba465..; page numbers = running heads)
- Improvement rules (p. 5): "an improvement rule, which is a function f : P(E) → P(E) that takes as input a set of improving
  edges, and outputs a set of improving edges", with "f(S) ⊆ S for all S ∈ P(E)" and at most one outgoing edge per node.
- SSI (Algorithm 2, p. 7): "I ← f((Iσ ∩ {(v, τ̄(v)) | v ∈ V0}) ∪ (Iτ ∩ {(v, σ̄(v)) | v ∈ V1}))". So every SSI switch at an Even v
  is the edge (v, τ̄(v)), and only when that edge is improving.
- Generalized SSI (Algorithm 3, p. 8): "I ← f((Iσ ∩ Jσ(τ)) ∪ (Iτ ∩ Jτ(σ)))", with Jσ(τ) = {(v, w) : v ∈ V0 ∧ Ξτ(w) ⊵ Ξτ(σ(v))}.
- Theorem 1 (p. 2): SSI is exponential "independently of the improvement rule"; Theorem 13 (p. 14): also for generalized SSI.
- p. 3: "This suggests that one needs a different approach involving more than only local information to benefit from insights
  in the interplay of strategies for both players." p. 15: the algorithms "can make too few crucial switches, as they are
  distracted by their opponent's (bad) strategy".
N5 is outside both algorithms as DEFINED: (i) its switch at v can be any edge of Iσ, including edges w ≠ τ̄(v) (Algorithm 2 cannot
switch there) and edges with Ξτ(w) ◁ Ξτ(σ(v)) (outside Jσ(τ), so outside Algorithm 3); (ii) its choice is not a function of the
candidate SET alone: it is a one-player optimum over the whole arena against τ. Risk (why it might still behave like SSI): N5 also
steers by the opponent's current strategy τ (the p. 15 mechanism). DLM's own families were therefore the first test.

## First test: DLM's own families (generator: experiments/new/dlm_gen.py, transcribed from Table 1 pp. 9-10 and Table 2 p. 13,
with their start pair (σ0, τ0); NOT Oink's counter_symsi, which has the same sizes 10N + 2 but different priorities)
Validation of the engine: n5.py mode ssi (Algorithm 2 with SWITCH-ALL) reproduces Proposition 7 EXACTLY on family 1:
1, 5, 13, 29, 61, 125 = 2^(n+1) − 3 (n = 1..6); and on family 2 gives 2, 9, 23, 51, 107, 219, 443 = 7·2^(n−1) − 5 (n = 1..7), the
count Proposition 11 states for generalized SSI.
| family (start σ0, τ0) | n (paper) | SSI (Alg. 2, switch-all) | N5 iterations | check |
| --- | --- | --- | --- | --- |
| DLM family 1 (Table 1) | 1..6 | 1, 5, 13, 29, 61, 125 | 1, 2, 4, 4, 6, 7 (no fallback) | Oink zlk OK, strategies verified, every n |
| DLM family 2 (Table 2) | 1..7 | 2, 9, 23, 51, 107, 219, 443 | 2, 4, 7, 8, 11, 12, 13 (no fallback) | same |
So N5 defeats both DLM families (data). Larger n and the rest of the bench: experiments/new/n5/<family>.csv (runner run_n5.sh).

## Cost at bit cost (Lead item 4)
Per iteration: 2 valuations (Ξσ on G, Ξτ on the dual) + at most 2 one-player optima, each ONE call of Engine.evaluate, i.e. the
Vöge-Jurdziński counterstrategy computation (VJ00, as implemented by L-SI; polynomial; L-NEW has not opened VJ00 for its exact
bound), plus a fallback step (no extra evaluation). Valuations are (vertex, n-bit path set, length): comparisons cost O(n) bits; no
big-number arithmetic anywhere (no discount, no weights). So the cost is poly(n) per iteration; the open question is the
iteration count, which is what the sweeps measure (iterations and fallbacks per row).

## Deep traps and padding
VJ valuations depend only on the priority order (injective rank), so priority gaps and isolated dummies change nothing; a trap
option (top priority P on a path into an odd cycle of priority q = B + 1 above every original priority) is Even's worst option
under VJ. Measured: experiments/new/n5/deeptrap.csv and padsae.csv.

## STEP-2 REPORT (2026-10-18 20:3xZ by date -u; data at this commit; DATA, not a claim, D1)
Gauntlet step 2 for N5: agreement with Zielonka on 12,000 random games and on EVERY M1 hard family, growth plotted.
(d) Verifier: every row is checked by experiments/new/check_sol2.py = regions equal to Oink zlk (pinned 8fbf0a7; Oink tl where zlk
hit the 4 GB cap, labelled per row) AND experiments/harness/verify.py (L-COMP's strategy checker, the D2 change 5 tool) on BOTH
players' positional strategies. Random games: harness/zielonka.py + harness/verify.py in-process (n5_random.py). Counts per family
= the "rows checked" column (all rows of every family verified; no mismatch anywhere).
(e) Stops: Python engine, 600 s budget per family (run_n5.sh BUDGET); the stopping row is named in the table ("BUDGET600_REACHED at
N = k" means sizes 1..k-1 finished and k was not started); families without a stop ran to NMAX = 40.
Start pair: best-reward for both players, except dlm1/dlm2 = DLM's (σ0, τ0).
| family | N (n) covered; stop | N5 iterations first .. last | (a) local log-log slope in n, last 3 | fallbacks (total) | rows verified |
| --- | --- | --- | --- | --- | --- |
| counter_core | N = 1..22 (n = 9..135); BUDGET600_REACHED at N = 23 | 2 .. 44 | [1.03, 1.02, 1.02] | 0 | 22/22 |
| counter_dp | N = 1..40 (n = 8..164) | 2 .. 40 | [0.0, 2.03, 0.0] | 0 | 40/40 |
| counter_m | N = 1..40 (n = 6..123) | 1 .. 21 | [1.97, 0.0, 1.98] | 0 | 40/40 |
| counter_ortl | N = 1..29 (n = 6..146); BUDGET600_REACHED at N = 30 | 2 .. 30 | [0.97, 0.97, 0.97] | 0 | 29/29 |
| counter_qpt | N = 1..40 (n = 2..80) | 1 .. 1 | [0.0, 0.0, 0.0] | 0 | 40/40 |
| counter_rob | N = 1..19 (n = 14..1238); BUDGET600_REACHED at N = 20 | 3 .. 55 | [0.56, 0.56, 0.56] | 0 | 19/19 |
| counter_rr | N = 1..40 (n = 4..160) | 1 .. 2 | [0.0, 0.0, 0.0] | 0 | 40/40 |
| counter_symsi | N = 1..22 (n = 12..222); BUDGET600_REACHED at N = 23 | 7 .. 99 | [1.3, 0.22, 0.89] | 84 | 22/22 |
| recursiveladder | N = 1..40 (n = 5..200) | 1 .. 40 | [2.03, 0.0, 2.03] | 0 | 40/40 |
| switchallexp | N = 1..40 (n = 21..567) | 5 .. 80 | [1.01, 1.01, 1.01] | 0 | 40/40 |
| switchbestexp | N = 1..32 (n = 35..810); BUDGET600_REACHED at N = 33 | 20 .. 242 | [0.8, 1.47, 0.67] | 0 | 32/32 |
| tc | N = 1..26 (n = 8..2158); BUDGET600_REACHED at N = 27 | 1 .. 83 | [-1.9, 1.64, 1.51] | 3 | 26/26 |
| tc+ | N = 1..17 (n = 8..5304); BUDGET600_REACHED at N = 18 | 1 .. 178 | [0.25, 0.67, 0.57] | 7 | 17/17 |
| dlm1 | N = 1..40 (n = 4..82) | 1 .. 41 | [0.97, 0.98, 0.0] | 0 | 40/40 |
| dlm2 | N = 1..21 (n = 12..212); BUDGET600_REACHED at N = 22 | 2 .. 34 | [-0.61, 1.27, 1.25] | 0 | 21/21 |
| deeptrap | N = 1..40 (n = 47..1295) | 4 .. 145 | [4.88, 0.55, 0.56] | 0 | 40/40 |
| padsae | N = 1..40 (n = 50..1220) | 5 .. 80 | [1.02, 1.02, 1.02] | 0 | 40/40 |
Plots (a): docs/new/plots/n5_<family>.png (17): iterations and fallbacks against n, seconds per iteration against n, log-log.
(a) switchbestexp (Friedmann's switch-best family, nearest relative of a global best step), iterations per N = 1..32:
[20, 32, 41, 47, 55, 62, 68, 77, 83, 89, 98, 104, 110, 117, 123, 129, 136, 122, 150, 153, 159, 165, 171, 177, 183, 189, 195, 214, 220, 226, 237, 242]; about +6 per N (n = 25N + 10), slope in
n 0.7-1.5 over the last sizes, no fallbacks. Switch-best SI doubles on this family (M1 bench, experiments/hard-families/switchbestexp/README.md: PGSolver switch-best
23, 61, 137, ..., 4849 at N = 1..8).
(b) Fallbacks per N (a fallback = one classical switch-all step taken because N5's selection made no progress):
- counter_core: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/44 = 0.00
- counter_dp: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/40 = 0.00
- counter_m: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/21 = 0.00
- counter_ortl: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/30 = 0.00
- counter_qpt: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/1 = 0.00
- counter_rob: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/55 = 0.00
- counter_rr: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/2 = 0.00
- counter_symsi: [1, 4, 5, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]; fallback fraction at largest N 4/99 = 0.04
- recursiveladder: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/40 = 0.00
- switchallexp: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/80 = 0.00
- switchbestexp: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/242 = 0.00
- tc: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/83 = 0.00
- tc+: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1]; fallback fraction at largest N 1/178 = 0.01
- dlm1: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/41 = 0.00
- dlm2: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/34 = 0.00
- deeptrap: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/145 = 0.00
- padsae: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/80 = 0.00
Only counter_symsi (4 per N, constant from N = 4), tc (3 in total) and tc+ (1-2 per N from N = 12) use fallbacks; the fraction at
the largest N is <= 0.04 everywhere. N5 does not degenerate into switch-all SI on any family.
(c) Measured cost: seconds per iteration against n (local log-log slope, last 3 sizes; Python, shared cores):
- switchbestexp: [1.88, 1.41, 2.53]
- tc: [2.72, 0.17, 2.62]
- tc+: [1.84, 1.8, 1.87]
- deeptrap: [1.19, 4.02, 1.94]
- padsae: [1.05, 3.18, 1.05]
i.e. about n^1.8-2.5 per iteration on the large families (VJ00 evaluations in Python), polynomial; no big numbers.
Random games: seed 1, 10,000 games n <= 60: AGREE 10000/10000 (max 11 iterations, 1,057 fallbacks in total); seed 2, 2,000 games
n = 60..400: AGREE 2000/2000 (max 15 iterations, 369 fallbacks) (n5/random.txt).
CAVEATS: one implementation (Python, L-SI's engine); sizes modest (n <= 5304, most families n <= 1300); the bench was built against
other algorithms, so it is weak evidence against N5; no barrier statement yet beyond N4N5-proposals.md; no adversarial family yet
(next item: own killer attempt).

## Killer attempt 1 (box 3, 20:39Z by date -u): adversarial hill climb, NOT killed
experiments/new/n5_adv.py n 4000 seed: random game (n vertices, out-degree <= 3, distinct priorities), mutations = edge target,
priority swap, owner flip; fitness = N5 iterations + 0.5 per fallback (the fallback trigger is where N5 hands over to classical
switch-all). Best found (pinned: experiments/new/instances/n5adv/best_n<n>_seed<n>.pg, every improved best checked: Zielonka +
verify.py, all OK):
| n | best N5 iterations | fallbacks in that run | sha1 (first 12) |
| --- | --- | --- | --- |
| 8 | 13 | 3 | 8c15f67e059e |
| 12 | 14 | 4 | 0a6d5f7c1d27 |
| 16 | 21 | 5 | 62a4c6e40a87 |
| 24 | 39 | 10 | 8aca328d1a66 |
Reading: <= 1.6 n iterations; no doubling. LEAD for the next attempt: the fallback share grows under adversarial pressure (25% at
n = 24, vs <= 4% on the bench). A family that forces N5's selection to stall at every step would make N5 = classical switch-all SI
(Friedmann-hard). Concrete design: a non-sink gadget where, against Odd's current τ, every improving switch of Even is worse than
staying (the one-player optimum keeps σ) while symmetric for Odd; then embed Friedmann's switchallexp counter behind it.

## Killer attempt 2 (20:43-20:44Z by date -u): maximise FALLBACKS (n5_adv.py ... fb), NOT killed
Fitness = fallback count (ties by iterations), 4,000 steps, n = 16, 24, 32 (seeds 116, 124, 132): best fallbacks/iterations 2/12,
13/31 (n = 24, instances/n5adv/best_fb_n24_seed124.pg sha1 f27b128efa82..), 9/35 (n = 32, best_fb_n32_seed132.pg sha1 0173afdccde9..);
every improved best checked (Zielonka + verify.py, all OK). The climb cannot make fallbacks dominate (<= 42%); forcing a stall at
every step needs a designed gadget (the lead above), not random search.
