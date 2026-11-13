# R2-SPEC-LEAN: independent reading of L-FORMAL's PROPOSED SPEC definitions in Lean (claude/l-formal 0ee5b8bc) against SPEC, si.py and n5x.py
REFEREE-2 successor 40 (session_01V5yGRWQ1pY9BpJ6WvVvBoi; Opus 5.5 under D1 / D21 / L53). Date -u at writing: 2026-11-13T03:45Z. Lead item D
(routed 03:43Z): «For each definition give MATCH or DEVIATION, saying whether the deviation can change output (with a small input if so),
and list every deviation the lane's own list D1-D9 / G1-G2 does not name.» Written without coordination with the Lead's own diff.
This is a reading, not a signature: the files hold definitions only (no theorem), and nothing here is a statement about N5.

## 0. Objects (git show; sha1 of the blob)
- claude/l-formal 0ee5b8bc997c8c879b716dabfbdca46e958777c1 (an ancestor of origin/claude/l-formal, checked): lean/lemmas/PGLemmas/Spec.lean
  sha1 9156c048717d753f9fce6270bc93d6549052c3a6 (582 lines, 29,877 B); SpecGamma3.lean sha1 354e890e5b8eea6e08a856834e735c5f3fb4afb0
  (60 lines, 3,157 B). Both equal the Lead's pins.
- SPEC: docs/new/N5-ssi-global.md at origin/claude/l-new, blob 81e966da04e0bb2976b3c36f71f3233ed8604bc7 (= the Lead's blob; file sha1
  66fde9ef…, the same as at trunk e8b6abf0), l. 24-127 (S1-S5, FIX 1-4, Q1-Q4).
- References: experiments/si/si.py at 0ee5b8bc (sha1 e688b963…), Engine l. 29-265 (evaluate l. 78-205); experiments/new/box21/n5x.py
  (sha1 e9c14eb4…) step l. 15-45, start_pair l. 47-59, trace l. 61-73; experiments/new/n5.py dual.
- Read beyond the brief: lean/lemmas/check/out/speccheck.out, speccheck_gamma3.out and their controls (to see which paths the lane's
  DATA exercises; §3); Gamma3.lean only for `start3` (l. 55, 223). Not built: Lean is not run on this branch (no lakefile); this is a
  reading. No Lean output of mine is cited.

## 1. Definition by definition (Spec.lean)
| definition | reference | verdict | note |
| --- | --- | --- | --- |
| SGame | SPEC «Input» | MATCH | arrays of ℕ; see U-2 for inputs outside the contract |
| SGame.dual | SPEC S1 «Odd's side», n5.py dual | MATCH | owner `1 - ·` in ℕ equals Python's 1 − o for o ∈ {0, 1} (U-2) |
| Eng.ofGame: succ | si.py l. 33 `sorted(set(s))` | MATCH | `dedup` then `mergeSort (≤)` |
| Eng.ofGame: pred | si.py l. 34-37 | MATCH | built in increasing v from the sorted succ: each pred list increasing |
| Eng.ofGame: rank | SPEC S1 «sorted by (Ω(v), v)», si.py l. 38-41 | MATCH | lexPrioLe is a total order with no ties (v distinct) |
| par, pp, rew, rankpar | si.py l. 42-48 | MATCH | |
| order | si.py l. 94 `sorted(range(n), key=rew)` | MATCH | rew injective (pp injective), so the stable sorts agree |
| Eng.bit | si.py `bit[u] = 1 << rank[u]` | MATCH | |
| SVal | SPEC (c, P, ℓ); si.py tuple (cycle node, mask, length) | MATCH | si.py's docstring says «signed path weight», its code stores the mask, as here |
| Eng.weight | SPEC S1 signed weight; si.py l. 54-65 | MATCH | Lean sums ranks r < n; masks hold only ranks < n. SPEC Q1's rule is equivalent (D1) |
| Eng.key, keyLt | SPEC S1 order; si.py `key` l. 68-70, Python tuple order | MATCH | ℓ signed by the parity of c |
| Eng.extend | si.py l. 72-75 | MATCH | |
| reach | si.py l. 117-124 | MATCH | DFS order differs from Python set iteration only in visiting order; the set is the same; fuel n + 1 suffices (each vertex pushed once) |
| restrict | si.py l. 126-131 | MATCH | `List.erase` = `list.remove` (first occurrence); hp lists have no duplicates |
| LSt, longest | SPEC S1 (iv), FIX 4; si.py l. 148-168 | MATCH | first strict maximum over hs[x] in list order; memo; busy = si.py's None state (raise → bad, D2); depth fuel n + 1 suffices |
| EvalOut | si.py `(val, tau_full)` | MATCH | |
| Eng.evaluate (i) cycle test | SPEC S1 (i); si.py l. 98-106 | MATCH | LIFO stack (cons / head = append / pop); `break` leaves the inner scan as Python's; pushes ≤ n, so n + 1 rounds suffice |
| (ii) R | SPEC S1 (ii); si.py l. 108-113 | MATCH | Rl is a list in reverse discovery order; si.py a set (D3) |
| (iii) restriction | SPEC S1 (iii); si.py l. 114-146 | MATCH | decreasing rank; Even u: M = reach(v, excl u), path for q ∉ M, restrict u then each q ∈ M; Odd u: M = reach(u, excl v), path and restrict for q ∈ M \ {u}. Order of restricts over q irrelevant (each removes a distinct vertex from hp lists; relative order of hp entries kept) |
| (iv) lengths | SPEC S1 (iv), FIX 4; si.py l. 147-180 | MATCH | Even Ω(v): longest from every x ∈ R (memo makes the call order irrelevant); odd: BFS layers FIFO over hp in list order, first discovery sets the choice |
| (v) cycle node's choice | SPEC FIX 2, Q2; si.py l. 182-195 | MATCH | push-time marking, parent default v; walk stops at the child of v; self-loop gives v (D4: `is not` read as `!=`, I agree there is no defect: the only stack object equal to v is v) |
| (vi) | si.py l. 196-201 | MATCH | |
| EvalOut.valOf | — | MATCH (helper) | default only where `bad` |
| Eng.improving | SPEC S2; si.py l. 220-228 | MATCH | strict, against Ξσ(σ(v)); (v, w) increasing |
| Eng.initialBest | SPEC S3 + FIX 1; si.py `initial("best")` l. 234-240 | MATCH | key (Ω, w) for even Ω, (−Ω, −w) for odd: si.py's (r, w if r even else −w) with r = ±Ω (r even ⟺ Ω even). Keys are injective in w, so Python's first-max = this fold's max. Odd entries 0 instead of −1 (D1) |
| improvSet | SPEC S4a «A(v) = {σ(v)} ∪ …»; n5x l. 23-25 | MATCH | dedup + sort = sorted(set) |
| arenaH, arenaH' | SPEC S4a, S4b; n5x l. 25, 33 | MATCH | |
| s4a | SPEC S4a; n5x l. 26-29 | MATCH except D2 | the dual of H evaluated on τ (dual-Even = G's Odd); choice read at G's Even vertices. Where the procedure gives no choice si.py stores None (ns[v] = None), Lean keeps σ(v) and sets bad (D2) |
| s4b | SPEC S4b; n5x l. 33-37 | MATCH except D2 | as s4a, on H' (not dual) evaluated on σ |
| fallbackAt | SPEC S4c, FIX 3, A7; n5x l. 42-44 | MATCH | max of (key, index), ties to the larger index; Odd's with G^d's engine and values |
| specStep | SPEC S4, S5; n5x step | MATCH | both sets from the old pair (D5); fallback test by whole-array equality, as n5x's list equality (the ignored entries are equal on both sides) |
| startPair | n5x start_pair (S3 best-reward, overwritten by a given pair) | MATCH except D7 | no start validation |
| specRun | n5x trace | MATCH on the states; U-1 | see U-1 for `stopped` at the cap |
| playTo, rootKey, lexLe, Eng.tied, keyRuleAt, keyRule | R24's reading, not SPEC (D8) | not a SPEC object | a predicate on the procedure's output; not used by specStep / specRun, so it cannot change their output. I did not diff it against R24's text (outside the brief) |

## 2. SpecGamma3.lean
| definition | verdict | note |
| --- | --- | --- |
| optList, vertList, vert3List, nV3 | MATCH under WF (G1) | the enumeration order is irrelevant when idx3 is a bijection onto 0..n − 1 (gamma3_card, lane) |
| sgame3 | MATCH under WF (G1) | prio3, owner (isOdd3 → 1), successors = E3 through idx3 (then sorted by the engine) |
| start3Pair | DEVIATION from SPEC S3, named (G2); see U-3 | Γ3's start given at every vertex |
| n5Gamma3 | MATCH to SPEC S1-S5 from a GIVEN start pair; equal to «N5 from S3 on Γ3» only under U-3 | |

## 3. The lane's deviations D1-D9, G1-G2: can each change output?
- D1 (representation): no. Entries at the other player's vertices are never read: evaluate reads `strat` only at owner-0 vertices of
  the game it is run on; the arenas read τ only at Odd's and σ only at Even's vertices; the fallback's array equality compares
  entries that are copied unchanged on both sides.
- D2 (fuel, bad): no on any input where si.py runs without raising and never stores None: I checked each loop's bound (each pops a
  vertex pushed at most once: ≤ n pops + 1; BFS ≤ n layers + 1; recursion depth ≤ |R|). Where si.py raises (cycle in the restricted
  graph, missing cycle, missing length or choice), si.py has no output and Lean has one with bad = true: a difference only on inputs
  where the reference itself fails, and the flag makes it visible. si.py's None choice (ns[v] = None) would make the next evaluate
  build gs[v] = [None] and raise; Lean keeps σ(v). No input known; VJ00 gives every x ∈ R a path to v in the restricted graph.
- D3 (Python sets): no. Path updates commute; restricts on distinct vertices commute and keep the relative order of hp entries; the
  memoised longest is a function of the final restricted graph; the fallback assignments are per vertex.
- D4 (`is not`): no (agreed with the lane's argument; I did not re-run its probe).
- D5: no (it is SPEC's wording). D6 (S5 output not defined): not a deviation of a defined object; it means no Lean statement about
  N5's output can be made from these files yet. D7 (no start validation): only on invalid starts (a start move that is not an edge,
  or set at the other player's vertex); then n5x in strict mode raises and in non-strict mode runs the same computation as Lean.
  Small input: G with Even vertex 0 → {1}, a start σ0(0) = 0; Lean evaluates the non-edge 0 → 0; n5x (strict) exits. D8: no (not
  used by specStep / specRun). D9: no.
- G1: no under WF (bijective idx3); without WF a vertex can overwrite another's slot (the lane says so).
- G2: see U-3.

## 4. Deviations the lane's list does not name
- U-1 (specRun, harmless). With the cap reached, specRun still evaluates one more `specStep` and sets `stopped := true` if it returns
  none; n5x `trace` stops at the cap without testing S5. The states and steps are equal; only the flag `stopped` carries one extra
  fact. Cannot change the states.
- U-2 (input contract, harmless on TARGET-valid games). On inputs outside SPEC's «Input» — arrays of length ≠ n, owner ∉ {0, 1},
  a successor index ≥ n, an EMPTY successor list — Lean's `a[i]!` returns a default (0 / [] / none) and computes on, where Python
  raises (IndexError, or `max()` of an empty list in initial("best")). Example: n = 1, succ = [[]]: si.py's initial("best") raises;
  Lean's initialBest gives 0 (headD 0), a non-edge. TARGET.md §1 requires a successor at every vertex, so no valid input is affected;
  a later theorem should carry a well-formedness hypothesis (every list non-empty, entries < n, owner ∈ {0, 1}, sizes n).
- U-3 (G2's equivalence is unstated). n5Gamma3 runs from `start3` given at EVERY vertex (G2), while the landed results on Γ3 (R124,
  R125, R127, and box 212's RF-D) are about N5 «from SPEC's default start S3». The two runs are the same iff start3Pair equals SPEC S3's
  best-reward start computed on sgame3 at every Even vertex (σ) and on its dual at every Odd vertex (τ); R117's Lemma S3-START says
  this for R117's Γ3, and Gamma3.lean cites it only as the source of start3 (l. 55: «R117, Lemma S3-START's right side»). So
  «n5Gamma3 = N5 from S3 on Γ3(G)» needs a stated lemma (or a check: `startPair E Ed none = (start3 σ, τ)` on sgame3), and the lane's
  DATA does not test it: every speccheck_gamma3 instance runs with «start=file» (25 of 25), and the S3 path (initialBest, startPair
  none) is exercised only on 25 general instances of speccheck.out («start=S3»). It can change output exactly when the two starts
  differ; I know no instance (and expect none, by S3-START), but nothing in 0ee5b8bc checks it.
- Not a deviation, recorded for the Lead's comparison: SPEC S1 (iv) says «recursion over successors in list order, first strict maximum
  wins» and FIX 4 «smallest index among the successors of maximum length»; both readings equal the Lean `longest` because hs[x] stays
  sorted under `restrict` (filter keeps order).

## 5. Verdict
Every definition of Spec.lean that transcribes SPEC MATCHES si.py / n5x.py line by line, with the lane's D1-D9 as the only deviations
in the computation of the states, and none of them can change the states on a TARGET-valid input on which si.py runs without raising.
SpecGamma3.lean MATCHES under WF (G1); its run equals «N5 from S3 on Γ3» only under U-3, which no file states or checks. Unnamed items:
U-1 (harmless), U-2 (contract; needs a well-formedness hypothesis in later theorems), U-3 (needs a lemma or a check before any theorem
about N5 from S3 on Γ3 uses n5Gamma3).
