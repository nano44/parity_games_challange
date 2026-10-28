# N5-READER (box 49): which counts can a passive vertex not inflate? Readers embed anywhere (DEAD for every graph-local restriction); Even switches per Even vertex per phase are DEAD too (SWE-LIN = L-SI's SW-LIN, killed by swlin_kill_n26); an amortized bound SW ≤ deg + PASS (PROVED, lane); two W-potentials for fallback-free runs (§6)
L-NEW successor 30 (Opus 5.5; D14, D18, L40). Working note, unrefereed, not frozen. Written 2026-10-28 from 21:45Z (date -u), on the Lead's
TASK 2 of 21:27Z: find "a potential or count that readers cannot inflate", with ideas from other fields (D18).
Labels: PROVED (lane, unrefereed) / CONJECTURE / OPEN / DATA / READING / DEAD. Not a TARGET.md claim. Nothing here bounds N5's running time;
G-N5-TIME stays OPEN.
Starting point: L-SI's docs/si/N5-ALT-box23.md §8 (l-si 6ec0aa2b, read there; not on trunk at 21:40Z): a READER (an Odd vertex o with no
predecessors and edges into one class) leaves the run unchanged and pushes XR(o) to 86 > 2n on long121, killing XR-LIN.
Tools (experiments/new/box49/, all new): dress.py (builds a dressing and compares the runs), search.py (hill climbing over gadget edge
sets), pairs.py (Even reader on every pair of a class), coresw.py (per-vertex switch counts on plain games), cross.py (pairwise order flips,
PASS, and the checks of §2), runall.sh (the named instances of §1-§2; log out/dress_named.txt). Engine: L-SI's experiments/si/root/common.py
rows() over experiments/new/box21/n5x.py (SPEC S1-S5), imported read-only.

## Summary
| § | item | label |
| --- | --- | --- |
| §0 | DRESSING: new vertices whose edges into the old game are never used; a count is reader-proof if no dressing that keeps the run changes it | definition |
| §1 | Per-vertex Ξ / σ̄ counts restricted to vertices with an Even predecessor, on an Even vertex's play, with any predecessor, or outside a "reader quotient": all inflated to 86 > 2n with the run SAME | DEAD (5 instances) |
| §2 | Every in-phase transition switches an Even vertex, so L ≤ Σ_w SW(w) | PROVED (elementary) + CHECKED |
| §2 | SW-AMORT: SW(w) ≤ PHI0(w) + PASS(w) (potential method) | PROVED (elementary) + CHECKED |
| §2 | SWE-LIN: per phase, every Even vertex switches at most n times (= L-SI's SW-LIN) | DEAD (l-si 85709361, swlin_kill_n26: 27 > 26; re-measured with coresw.py) |
| §2 | Why Even readers inflate less: S4a needs a Ξ-improvement AND the W-optimum of the arena | READING + DATA |
| §3 | Kinetic / envelope view: an Odd gate is a lower envelope; pairwise order flips s(P) reach 0.55n, so no "few crossings" bound | DEAD as a route + DATA |
| §3 | LP / tropical reading: readers are redundant rows; per-row counts are not intrinsic, pivot counts are | READING |
| §4 | Open and next | OPEN |
| §7 | |𝒞_f(P)| (RESULTS R71 / R73's configurations at fallback sources): ≤ 7 on all plain data, but a 2-option reader lifts it to f (5 → 8 = f on long121, run SAME) | DATA + DEAD (as a route easier than f) |
| §8 | FB-LIN (f ≤ n per phase; L-SI §13's conjecture, routed to L-NEW 22:55Z): no kill (3 climbs, best f − n = −9); a reader-proof configuration count |𝒞°_f| (gates read by another play) stays at its base value under every reader; f per read configuration ≤ 0.78n | DATA + CONJECTURE + OPEN |
| §6 | Fallback-free runs: W never falls (DATA, 10,499 transitions); the W*-reach potential F_t stalls at 53% of transitions (xsn43_n48: 43 of 44) | DATA + DEAD |

## 0. Setting and the definition
A phase P of N5 (λ_Ξ and τ constant, as in P-N5-OFFMONO-fixes F1); L := its number of transitions. For a vertex z: XR(z) := the number of
transitions of P at which Ξ(z) changes; SW(w) := the Even switches of an Even w; GCH(u) := the σ̄ changes of an Odd u.
- A DRESSING of a game G with a start (σ0, τ0): new vertices H with any edges, start choices for them, and optionally new edges from old
  vertices into H. It KEEPS THE RUN if, at every state, σ, τ, σ̄ on the old vertices, the fallback flags, every old vertex's Ξ (cycle node,
  path set as a vertex set, length) and the phases are the same as on G (dress.py's comparison, the same test as L-SI's orcheck.py; ranks
  shift when vertices are added, the order on old vertices does not).
- A statement "every vertex of kind K has count ≤ f(n) per phase" is READER-PROOF if no run-keeping dressing gives a vertex of kind K a
  count above f(n + |H|). Counts of OLD vertices are unchanged by definition of keeping the run; the question is always about the new ones.
- Run identity is DATA here: dress.py checks it per instance, and nothing in this note proves it for a class of dressings. For Odd readers
  it is now a theorem under a hypothesis. REFEREE proved Theorem READER-INV under (R): τ(o) never moves at a transition at which τ is
  unchanged on the old vertices (docs/referee/R-N5-READER.md at claude/referee e83fd19d, §1). Without (R) the statement is false (gap
  G-READ-1: S4b moves τ(o), splitting phases and cancelling fallbacks; 5-vertex counterexample, §2 there). It reproduced l121reader_n41,
  with (R) holding there (Iτ(o) = ∅ at all 123 states). My gadgets with new Even vertices, or with edges from old vertices (l121_b, _c,
  _d29, _e100, the Even readers), are outside that theorem: they are per-instance DATA only.

## 1. DEAD: graph-local restrictions do not make per-vertex counts intrinsic
All instances: base experiments/new/box48/instances/long121_n40 (one class, c = 11, Ω(c) = 10 even; one phase [1, 122], L = 121, 8
fallbacks; the old vertices' largest XR is 44), S := {0, 1, 2, 6, 7, 8, 17, 20, 22, 23, 24, 30, 36, 39} (L-SI's set), new vertices priority 0
unless stated. Built by runall.sh; every row is SAME (run kept) in out/dress_named.txt.
| instance (experiments/new/box49/inst/, sha1 of .pg) | dressing | kills (the statement, each with f(n) = 2n) | count |
| --- | --- | --- | --- |
| l121_a (084da8cd…, = L-SI's l121reader_n41) | Odd reader o → S | XR-LIN (L-SI) | XR(o) 86 > 82 (n 41) |
| l121_b (6c751e71…) | + Even e, out-degree 1, e → o | "Ξ-changes of vertices with an Even predecessor ≤ 2n"; "of vertices on the honest play of an Even vertex" (o is on e's play); also XR(e) itself (an Even vertex) | XR(o) = XR(e) = 86 > 84 (n 42) |
| l121_c (1667a4cb…) | Even CHOICE e → {o, e2}, e2 Even forced → o, e starts on o and never switches | the same, for Even vertices of out-degree ≥ 2 | XR(e) 86 = 2n (n 43): DEAD for any f(n) < 2n only; l121_b is the strict kill |
| l121_d29 (408438fe…) | o → S ∪ succ(29) = S ∪ {5}, and the OLD Even vertex 29 gets the edge 29 → o (never improving: Ξ(o) = o ⊕ min ⊲ Ξ(σ(29)) since o ⊕ lengthens and c is even, so shorter is better for Even) | "vertices with an OLD (core) predecessor"; every REDUCTION BY QUOTIENT that deletes vertices with no predecessors, iterated, or keeps the smallest successor-closed set: o is in every successor-closed set containing 29 | XR(o) 86 > 82 (n 41) |
| l121_e100 (989544fc…) | o → S ∪ {e}, e Even forced → o, priority(e) = 100 (even, above every old priority; o ↔ e is an Even-winning cycle that Odd avoids) | "every vertex has a predecessor" (both new vertices have one; no vertex of H can be deleted as predecessor-free) | XR(o) = XR(e) = 86 > 84 (n 42) |
- In the d29 loop, every one of the 36 old Even vertices p accepts such an edge p → o (S ∪ succ(p)) with the run SAME; p = 29 gives the
  largest XR(o). So "unused edges" embed a reader at any Even vertex of this base.
- Obstruction (all five rows): a vertex whose value is a lower envelope (o ⊕ min_S Ξ) can be attached to the game by edges that nobody
  ever uses. Such an edge changes no Iσ, no arena and no honest play of an old vertex. Every local, graph-defined restriction of the
  vertex set (predecessors, Even predecessors, plays of Even vertices, quotients by predecessor-free vertices) admits it.
- What is intrinsic: the run on the old vertices. In particular L, and the switch counts of the old vertices.

## 2. Even switches per Even vertex (the Lead's first example): survives every gadget tried
- Fact NOSW (PROVED, elementary). Every in-phase transition t → t + 1 switches at least one Even vertex: τ_t = τ_{t+1} (phase), and
  (σ_{t+1}, τ_{t+1}) ≠ (σ_t, τ_t) (n5x.step returns a changed pair or stops: S4a/S4b change it, else S4c's fallback changes σ or τ). Hence
  L ≤ Σ_{w Even} SW(w). CHECKED: NOSW = 0 at every in-phase transition of the lib41 run below (11,461 transitions).
- Lemma SW-AMORT (PROVED, elementary; the potential method of amortized analysis). For an Even w and a state t of P let
  Φ_t(w) := #{y ∈ succ(w) : Ξ_t(y) ▷ Ξ_t(σ_t w)}, and PASS(w) := the number of pairs (t, y), y ∈ succ(w), with Ξ_t(y) ⊴ Ξ_t(σ_{t+1} w) and
  Ξ_{t+1}(y) ▷ Ξ_{t+1}(σ_{t+1} w) (an option overtakes w's new choice during the transition). Then SW(w) ≤ Φ_{first}(w) + PASS(w).
  Proof. Split t → t + 1 into (i) σ_t(w) → σ_{t+1}(w) at fixed Ξ_t and (ii) Ξ_t → Ξ_{t+1} at fixed choice b := σ_{t+1}(w). (i): if w switches
  from a to b, then (w, b) ∈ Iσ_t ((SW), RESULTS R72's premises), i.e. Ξ_t(b) ▷ Ξ_t(a); every y ▷ b is ▷ a, and b itself is ▷ a but not ▷ b,
  so the count at fixed Ξ_t drops by at least 1. (ii) raises the count by exactly the number of options y that go from ⊴ b to ▷ b, the
  PASS events of this transition; options that go from ▷ b to ⊴ b only lower it. Φ ≥ 0 at the end. Summing over P: 0 ≤ Φ_first − SW + PASS. □
  CHECKED at every Even vertex of every phase (lib41 run below: 0 violations). Reader-proof: PASS counts overtakes of w's CURRENT choice; an
  option that is never improving (l121_d29's edge 29 → o) never overtakes, so PASS(29) is unchanged; Odd readers add no Even vertex, and
  forced Even vertices (out-degree 1) never switch.
- So L ≤ m_E + Σ_w PASS(w) (m_E := the number of Even edges). DATA: Σ PASS / L = 2.5 on long121 (303 / 121), 2.09 on the lib41 run (23,943
  / 11,461); PASS is of the order of L, so SW-AMORT moves the problem, it does not shrink it.
- DATA: SW on plain games (coresw.py; out/coresw_*.txt). Largest SW of one Even vertex in one phase:
  | set | runs / phases | max SW (instance, L) | max SW / n |
  | --- | --- | --- | --- |
  | lib41 (experiments/new/box41/lib41.txt, n ≤ 48, own start or S3 + 2 random, seed 7) | 1,047 / 1,012 | 14 (box25/instances/sc24, L 20) | 0.58 (sc24, n 24) |
  | L-RED's instances (experiments/red/*/instances/*.pg, 324 files, n ≤ 200, own start or S3) | 311 / 328 | 48 (red/ul/instances/ladderd0_k48_n156, L 49) | 0.375 (red/kw/instances/cw11_n24) |
  | long121_n40, nep76_n40 (n5-epoch), the qpcclimb scale games, si/root/instances | 9 / 12 | 13 (best_qpc_nep90_n40_s61, L 97) | 0.30 (long121: 12 in L 121) |
  For comparison, the largest σ̄ changes of one Odd vertex: 1.53n (lib41, si/orlens lev_l_x: 49, n 32), 1.44n (red/xing x31_rx32), and
  the largest XR: 1.59n / 1.53n. Odd counts reach about 1.5n on plain games; Even switches stay below 0.6n.
- DATA: Even gadgets, all on long121 (run SAME at every reported point; DIFFERENT dressings are discarded by the searches):
  | gadget | best count of the new Even vertex | n (dressed) |
  | --- | --- | --- |
  | Even reader e → S' (search.py evenreader, 300 moves each, seeds 1 and 2): l121_er19, S' = {6, 8, 17, 19, 25, 27, 34} | 19 switches (XR 31) | 41 |
  | Even reader on the most-flipping pair {6, 19} (22 order flips in the phase): l121_er_6_19 | 11 switches | 41 |
  | Even reader on every pair of the class, start on the smaller index (pairs.py; out/pairs_l121.txt): 773 of 780 pairs keep the run, 7 do NOT | 12 switches (pairs {17, 31}, {17, 30}, {2, 23}, {17, 22}) | 41 |
  | Even e over two Odd readers, e → {o1, o2}, o_i → S_i (search.py evenmax2, 400 moves, seeds 1-3) | 16 / 13 / 14 | 43 |
  So Even readers DO inflate the per-vertex Even count above the old vertices' 12 (to 19), but not near n. And Even gadgets are not always
  clean: 7 pair readers change the run (out/pairs_l121_different.txt: six pairs containing 33 first differ at state 5, {4, 17} at state 55;
  the dressed runs are 1-2 states longer; the transition into the first differing state is not a fallback on G; mechanism not classified).
- DEAD SWE-LIN ("in every phase, every Even vertex switches at most n times"; it would give L ≤ n·|V_0| through NOSW). It is the same
  statement as L-SI's SW-LIN, which L-SI killed first: docs/si/N5-ALT-box23.md §10 at l-si 85709361. Instance
  experiments/si/root/instances/swlin_kill_n26.pg (l-si 85709361; sha1 e2f769e1b45bdb883f7808e84f461b318a25e8f1, with its .start). Re-measured
  with my coresw.py: one phase of 46 transitions, one Even vertex switches 27 > n = 26 times. cross.py on it gives NOSW 0 and SW-AMORT 0
  violations (SW 115, PASS 124). Obstruction (L-SI's trace): fallback re-arming. Each S4c fallback resets the vertex to its Ξ-best option,
  and it walks the same option cycle again. So the plain-game maxima above (≤ 0.58n) were a property of the corpus, not of N5. My Even
  gadgets never came near n because none of them was built to re-arm through fallbacks.
  - Lead reading (Lead message 22:17Z): only the transition count per phase is intrinsic. The current route is L-SI's surviving CONJECTURE SW-RUN (per
    fallback-free run, DATA ≤ 0.67n) plus the number of fallbacks per phase. §6 takes that up.
- READING + DATA (why Even readers inflate less: TWO ORDERS). An Odd gate's σ̄ follows one order, close to the Ξ-minimum of its options
  (cross.py: 3,298 of 3,505 σ̄ changes on lib41 are strict order flips of the (old, new) choice at that transition; the other 207 are not,
  ties or options whose play passes the gate; not classified). An Even switch needs two things: (w, b) ∈ Iσ (Ξ-improvement), and b
  chosen by S4a's W-optimum of the arena against the fixed τ (docs/new/N5-ALTLIT-box49.md §2 (a)). On {6, 19}, Ξ flips 22 times in the
  phase but the Even reader switches 11 times.

## 3. Ideas from other fields (D18), each with its status
- Kinetic data structures / lower envelopes. Within a phase every Ξ(z) is non-decreasing ((M2κ) per class). An Odd gate, and every reader,
  is (up to ties and options whose play passes it) the lower envelope of its options' trajectories: 94% of the σ̄ changes on lib41 are a
  strict flip of the old and new choice (§2). A Davenport-Schinzel-type route would bound envelope changes through few flips per pair
  ("pseudo-lines").
  - DEAD as a route. s(P) := the most flips of one pair in one phase. long121: s = 22 (pairs (6, 19) and (6, 24), L 121, n 40); lib41: s = 20
    (red/xing/instances/j4_n40, phase [3, 106]). So s is of order n/2, and pairs leapfrog along the whole phase: no bounded-crossing
    hypothesis holds. (cross.py; out/cross_lib41.txt, out/cross_l121.txt.)
- Amortized analysis (Tarjan's potential method): SW-AMORT above. It turns the per-vertex Even count into PASS, which is reader-proof but
  of order L in data.
- LP / tropical duality (READING, no theorem cited). In the (min, +) system that fixes Odd's best response, a reader is a REDUNDANT ROW: it
  feeds no other row. Redundant rows leave a pivot path unchanged and can be tight or entering any number of times, so per-row counts are
  not intrinsic, while the number of pivots is. In this language SWE-LIN said (DEAD, §2): each Even "variable" enters the basis at most n times per
  phase: a strong structural claim, to be tested (§4 item 1) before it is worked on.
- Lattice / matroid monotonicity: within a phase the vector Ξ_t is a chain in a product of chains; its length is bounded only by the number
  of distinct values (exponential, the P-component). Not developed further; no statement.

## 4. OPEN and next
1. (SWE-LIN is DEAD, §2.) A potential for the transitions of a fallback-free run, or for the fallbacks per phase (§6).
2. A proof that an Even gadget's switches are bounded by the old vertices' counts (TWO ORDERS): an Even reader switches only when the Ξ-order
   and the arena W-order agree on the new option.
3. Run identity of the dressings as a lemma (code-level against si.py, as PF-CHOICE was): for which H is the run provably kept?

## 5. Dead ends recorded (also in notes/L-NEW.md)
- SWE-LIN (per phase, every Even vertex ≤ n switches): DEAD, L-SI's swlin_kill_n26 (l-si 85709361, sha1 e2f769e1…): 27 > 26, fallback re-arming.
- PRED-XR ("Ξ-changes of vertices with an Even predecessor ≤ 2n per phase"): DEAD, l121_b (6c751e71…): XR 86 > 84. Obstruction: a forced Even
  vertex in front of a reader.
- PLAY-XR ("… of vertices on the honest play of some Even vertex"): DEAD, l121_b (o on e's play).
- QUOT-XR ("… outside the reader quotient / with a core predecessor / every vertex with a predecessor"): DEAD, l121_d29 (408438fe…) and
  l121_e100 (989544fc…): XR 86 > 82 / 84. Obstruction: a never-improving edge from an old Even vertex, or a passive Even-winning cycle.
- DS-ROUTE (bounded pairwise crossings of value trajectories): DEAD, long121 pair (6, 19), 22 flips in one phase (n 40).

## 6. Fallback-free runs: two W-potentials (Lead's NEXT of 22:17Z; D18). Tools wamort.py, wstar.py; logs out/wamort_*.txt, out/wstar_*.txt
A fallback-free run is a maximal stretch of a phase with no S4c fallback, so it consists of S4a steps only, with τ fixed. W_t is the
valuation of the (σ_t, τ)-play, in S1's order. σ_{t+1} is Even's W-optimum in the arena H_t = {σ_t} ∪ Iσ_t of the one-player game G_τ.
- DATA (W-MONO). W never falls at any vertex in a fallback-free run: 0 falls in 10,499 transitions (lib41, n ≤ 48, own start or S3 + 2 random,
  seed 7, 1,449 runs), and 0 in 113 transitions on long121. READING: this is the one-player optimality of the arena optimum. σ_t lies in
  H_t, so the optimum dominates it pointwise (standing premise 1E-N3 in form P2). I have not written it as a proof here.
  W is unchanged at every vertex at 65 transitions (WFLAT). So W is a monotone potential, but it is not strict at every step.
- The amortized argument in the W order (wamort.py) needs every switch to be W-strict at time t. It is not: 88 of 19,446 switches have
  W_t(b) ◁ W_t(a), and 8 have W_{t+1}(b) ◁ W_{t+1}(a). So the W form of SW-AMORT fails as stated (181 vertex-runs), and PASS_W is 2.2 L
  (23,612 / 10,499). Nothing gained over the Ξ form.
- DEAD W*-REACH. Let W* be the valuation of Even's optimum in the whole of G_τ (S1's procedure on the dual with all Even edges, as n5x.step
  builds its arena game). Let F_t := {v : W_t(v) = W*(v)}. F_t only grows on a fallback-free run: CHECKED, with 0 shrinks and 0 vertices
  above W*. If F_t grew at every transition, every fallback-free run would have ≤ n transitions. It does not: F_t stalls at 5,579 of
  10,499 transitions on lib41.
  - Instances: experiments/red/so/instances/xsn43_n48 run [1, 44] (43 stalls in 44 transitions, n 48), and long121_n40 run [6, 23] (17 of 17).
  - Obstruction: the arena is cut by Ξ-improvement. A fallback-free run ends at a fallback long before W reaches W*, because the edges of
    σ* are not Ξ-improving.
- What the charging does give, and whose it is. At a continuing S4a step, σ_{t+1} is W-optimal in H_t, so a further W-improvement needs an edge
  that newly entered the arena. This is L-SI's FRESH-RED (docs/si/N5-ALT-box23.md §1: run length ≤ m_E + NOFRESH), not new. I do not
  duplicate it.
- Still OPEN (for the Lead's NEXT): a potential for the fallbacks per phase. At a fallback, no Ξ-improving edge is W-improving, and S4c takes
  the Ξ-best improving edge, which may lower W. Fallback re-arming is exactly what killed SW-LIN (§2). So the fallback count is where the
  per-vertex Even count goes wrong, and it is the quantity to measure next.

## 7. Fallbacks per phase: the number of configurations |𝒞_f(P)| (Lead's GO of 22:36Z). Tools fbconf.py, cfreader.py; logs out/fbconf_*.txt, out/cf*.txt
Ingredients (landed): RESULTS R71 Theorem FB-C, f ≤ |𝒞_f(P)|·(4n² − 3n). R73's SAT-FB1 form is f ≤ n·|𝒞_f(P)| (as the Lead's message
names it; not re-read here). 𝒞_f(P) is the set of configurations C = σ̄|Q at the sources of P's in-phase S4c fallbacks, with Q the Odd
vertices of out-degree ≥ 2. The open part is |𝒞_f(P)|.
- DATA (fbconf.py; f and |𝒞_f| per phase):
  | set | runs / phases (with a fallback) | Σ f / Σ |𝒞_f| | max |𝒞_f| (instance, phase, f) | max f (instance, |𝒞_f|) |
  | --- | --- | --- | --- | --- |
  | lib41 (n ≤ 48, own start or S3 + 2 random, seed 7) | 1,047 / 1,012 (242) | 962 / 303 | 4 (red/n5inj/instances/elimn_cex_n48, [2, 56], f 7) | 33 (si/xing/instances/ccl_w48_n48, 1) |
  | L-RED instances (324 files, n ≤ 200, own start or S3) | 311 / 328 (87) | 410 / 125 | 5 (red/n3/instances/long121_n40, [1, 122], f 8) | 37 (red/so/instances/rise_fb38_n48, 1) |
  | long: si/root/instances (incl. swlin_kill_n26), long121, nep76, qpcclimb scale | 13 / 16 (10) | 71 / 53 | 7 (qpcclimb best_qpc_nep90_n40_s61, [5, 102], f 7) | 8 (l121ereader_n41, 5) |
  On swlin_kill_n26 (the SW-LIN kill), the phase [1, 47] has f = 6 and |𝒞_f| = 3. On plain games |𝒞_f| stays ≤ 7. The long-f phases have
  |𝒞_f| = 1, so FB-C / SAT-FB1 carry them.
- DEAD ("|𝒞_f(P)| is small, or easier to bound than f"). A reader lifts |𝒞_f| to f. Instance experiments/new/box49/inst/l121_cf35_39.pg
  (sha1 36a86755be9671f8eff3f8e95b503fbc68d89e5f, with .start). It is long121_n40 plus an Odd reader o → {35, 39} (priority 0, start 35).
  - The run is SAME and the phases are equal. τ(o) never moves (phases equal), so (R) holds and REFEREE's Theorem READER-INV covers this
    instance, not only DATA.
  - |𝒞_f| rises from 5 to 8 = f: every one of the 8 fallback sources gets its own configuration (out/cf35_39.txt). σ̄(o) changes only 3
    times in the phase.
  - Of the 780 pair readers of the class, 778 keep the run, and the best ones all give 8 (cfreader.py; out/cfreader_l121.txt).
  - Embedded too: l121_cf_emb12.pg (sha1 5440021b27bb0ab23cd4db682ae73bfbf5aaf39a) has o → {0, 15, 35, 39} and the edge 12 → o at the OLD
    Even vertex 12. The run is SAME and |𝒞_f| = 8 (out/cf_emb12.txt).
  - Obstruction: a configuration records the choice of every Odd vertex of out-degree ≥ 2, including vertices that no other honest play
    reads. A passive gate with two options can split all fallback sources into distinct configurations. So any bound |𝒞_f(P)| ≤ g(n) gives
    f ≤ g(n + 1) on the base game. Bounding |𝒞_f| is not easier than bounding f, which is intrinsic (unchanged by the reader).
- What a repair would need (OPEN; not attempted further). FB-C with configurations restricted to the gates that matter, i.e. a reader-proof 𝒞_f.
  - For a reader o with no predecessors, H_C and H_{C′} differ only on o's edge when C and C′ differ only at o. Every H_C-path through o
    starts at o, so LEV_C's constraints at every other vertex agree. Dropping x = o from LEV_C might then let one LEV progress serve both.
  - That would need FB-RISE_C's proof re-read with the restricted LEV. An embedded reader (12 → o) puts o on H_C-paths from 12, so a purely
    graph-defined restriction fails here too (§1's lesson). A run-defined one ("gates whose choice lies on an honest play of a vertex other
    than itself at some fallback source") is the candidate.

## 8. FB-LIN: at most n in-phase fallbacks per phase (L-SI's docs/si/N5-ALT-box23.md §13, l-si 95591448; the Lead's scope word of 22:55Z)
Route asked for: R73's SAT-FB1 (f ≤ n·|𝒞_f(P)|) plus a bound on |𝒞_f(P)|, or a kill. §7 shows the route cannot work with 𝒞_f as defined: a
reader lifts |𝒞_f| to f. The repair tried here is a reader-proof configuration count.
- Definition. Q°(P) := the gates q ∈ Q that lie on the honest play of some OTHER vertex (q met after at least one step of next_t from v ≠ q) at
  some fallback source t of P. The READ configuration at a source t is σ̄_t|Q°(P), and 𝒞°_f(P) is the set of these. A reader (no
  predecessors) is on no other play, and neither is an embedded reader whose edge is never used, so both drop out.
- DATA (fbconf.py; out/fbconf_{lib41,red,long}.txt):
  - Reader-proof on the instances. |𝒞°_f| = 5 on long121, on l121_cf35_39 and on l121_cf_emb12 (|𝒞_f| 5 / 8 / 8). On swlin_kill_n26 the 3
    configurations differ only at unread gates: |𝒞°_f| = 1, f = 6.
  - Size. Max |𝒞°_f| is 4 on lib41 (si/xing/instances/zcl_rx_n32, f 13), 5 on L-RED (long121_n40), and 7 on the long set
    (best_qpc_nep90_n40_s61, f 7). Σ |𝒞°_f| ≤ Σ |𝒞_f| on every set (301 / 303 on lib41, 122 / 125 on L-RED).
  - Fallbacks per read configuration: max 0.78n (red/so/instances/farrise25_n32: 25 at n 32) and 0.75n (box25/instances/wd16_s2: 12 at
    n 16). The largest f with ≥ 2 configurations is 29 at n 48 (red/so/instances/njb_reabs65_n48, phase [2, 68], 2 configurations, 26
    fallbacks from one).
- CLIMBS for a kill (L-SI's experiments/si/root/runfbclimb.py at l-si, OBJ=fb, run from a scratch copy with only its import path changed;
  3,000 steps each, all finished; logs and best games out/fbclimb_*.{log,pg}): from
  rise_fb38_n48 (seeds 21, 22) and ccl_w48_n48 (seed 23). Best f − n = −9 (f 37 at n 46; f 36 at
  n 45); ccl: f 34 at n 46. No kill. The climbs shrink n at fixed f; they do not raise f.
- CONJECTURE FB-C° (reader-proof form of R73's per-configuration count): in every phase, each read configuration is the configuration of at
  most n fallback sources; hence f ≤ n·|𝒞°_f(P)|. DATA only (max 0.78n per read configuration). A proof would re-run FB-RISE_C / SAT-FB with
  LEV restricted to the frame of the read gates (§7's last bullet). It does not give FB-LIN: |𝒞°_f| reaches 7.
- Why the per-configuration route cannot reach FB-LIN alone (READING). FB-LIN needs Σ_C f_C ≤ n. LEV_C rises only at fallbacks from C-states.
  A common level for all configurations of the phase would need Ξ(x) ⪰ value(r) along Odd edges that are not x's current choice, and Odd's
  optimality gives the opposite inequality (Ξ(x) ⊴ x ⊕ Ξ(y) for every option y). So the levels of different configurations do not add up to
  one budget of n. A proof of FB-LIN has to say why few configurations each spend much of their n: in data, 2 configurations with 26 + 3, and
  long-f phases with one configuration.
- Disjoint unions do not build a kill (READING, from SPEC S4c): a fallback fires only when the whole game has no arena step, so the
  fallbacks of two independent parts synchronise instead of adding. n adds, f roughly does not.
- OPEN: FB-LIN; FB-C°.
