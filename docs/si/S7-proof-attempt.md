# S7 (most-improved single switch): running-time proof attempt, with the gaps named (L-SI, 2026-10-15, UNREFEREED)

Lead brief 13:26Z: "can Lemma D ('downstream first') plus a potential function bound the number of iterations polynomially?
State every gap as a named gap." Answer in one line: no bound is proved; the attempt below isolates two named gaps (P1, P2)
and refutes the two simplest potentials by data. Everything marked PROVED is proved here from the cited statements; marked
CITED is taken from a source; marked OBSERVED is data.

## 0. Objects
G a parity game (TARGET section 1), priorities injective by rank (p' = 2·rank + parity, winner of every cycle unchanged:
PROVED, as in notes/L-SI.md). σ a positional strategy of Even, τ_σ Odd's optimal counterstrategy (Friedmann 1106.0778
Lemma 3.1, CITED), Ξ_σ the VJ valuation, ≺ its order (CITED, section 3 there). P_σ(x) = the (σ, τ_σ)-play from x; up_σ(v) =
{x : v ∈ P_σ(x)} (x is upstream of v; v is downstream of x). Generic σ: distinct plays from a vertex have distinct
valuations (L-RED R3 section 1, CITED; it holds whenever no two plays differ only in vertices below the cycle node with
equal length).
S7 (pseudocode, gauntlet step 1):
```
S7(G):  σ ← best-reward start (PGSolver's initial_strategy_by_best_reward)
        loop:
          (Ξ, τ) ← VJ-valuation(G, σ)                                   -- Friedmann Lemma 3.1
          I ← {(v, w) : v Even, w ∈ E(v), Ξ(w) ≻ Ξ(σ(v))}                 -- improving edges
          if I = ∅: return regions {v : cycle node of Ξ(v) even} / odd, strategies σ on W_E, τ on W_O   -- Thm 3.3
          for each e = (v, w) ∈ I: Ξ_e ← VJ-valuation(G, σ[v→w]); count(e) ← |{x : Ξ_e(x) ≻ Ξ(x)}|
          choose e ∈ I maximising (count(e), Ξ_e(v)); ties: smallest (v, w)    -- index only as a counted last resort
          σ ← σ[e]
```
Cost per iteration: ≤ m + 1 valuations, each O(n² m) word operations (notes/L-SI.md): polynomial; no big integers
(keys of O(n) bits).  Termination and correctness: every switch is an improvement policy step (Friedmann Thm 3.2, CITED):
Ξ strictly increases in the product order, so the run ends, and Thm 3.3 (CITED) gives the regions and strategies.

## 1. Lemmas (L-RED R3 section 1, restated; unrefereed; sketches re-derived here)
Lemma T (count = traffic). For generic σ and improving e = (v, w): count(e) = |up_σ(v)|.
  Sketch (re-derived). (≤) A vertex x whose play avoids v keeps its play available under σ[e] at the old value; Odd minimises,
  Thm 3.2 forbids decrease, so Ξ_e(x) = Ξ(x). (≥) If v ∈ P(x), the old play is no longer available (σ(v) changed), every
  available play is worth ≥ the old value (Thm 3.2), and equality would be a different play of the same value, excluded by
  genericity; so x improves strictly.  Gap T1: non-generic σ (equal-valued plays). Then count(e) ≤ |up(v)| with strict
  inequality possible; nothing below needs equality, only the inclusion {x : Ξ_e(x) ≻ Ξ(x)} ⊆ up_σ(v) (PROVED by (≤)).
Lemma D (downstream dominance). For generic σ: if u ∈ P_σ(v), u ≠ v, then up(v) ⊆ up(u) \ {u}, so count(any edge at u) >
  count(any edge at v).  PROVED from T: x upstream of v is upstream of u (its play passes v then u... [Gap D1: only if the
  play from x reaches u AFTER v; since u ∈ P(v) and plays are deterministic from v on, yes]) and u ∉ up(v) (u's play would
  revisit u before... [u ∈ up(v) means v ∈ P(u), with u ∈ P(v): the play from v visits u and then v again: a cycle through v
  and u; then P(v)'s cycle contains u and v, and "downstream" degenerates; Gap D2: Lemma D is for u, v not on a common cycle
  of the play; on the cycle all vertices have equal traffic]).
Corollary D' (PROVED from D, modulo D1-D2, generic σ): when S7 switches at v, no vertex of P_σ(v) \ {v} off the final
  cycle has an improving edge.

## 2. What a switch does (PROVED from T, Thm 3.2)
After σ' = σ[v→w]: Ξ changes exactly on up_σ(v) (strictly up); plays of vertices outside up_σ(v) are unchanged (their
minimising route is unchanged and still minimal, genericity); the new play of v is v·P_σ(w) if w ∉ up_σ(v), and otherwise
a cycle through v (cycle-creating switch, notes/L-SI.md) that Odd may or may not escape.
A vertex x becomes NEWLY improving after the switch only if some successor y ∈ up_σ(v) improved past Ξ(σ(x)) (if σ(x) ∉
up_σ(v)) or if σ(x) ∈ up_σ(v) and some successor y now beats the improved Ξ'(σ(x)). PROVED (only up_σ(v) changed).

## 3. Potentials tried
3.1 Φ_1 = traffic of the switched vertex, hoped non-increasing along the run (then ≤ n distinct values and ≤ n switches
    per value would follow if a vertex could not repeat at the same traffic: it can). REFUTED by data: on random games
    (300 runs, n ≤ 14) the count sequence has 33 increases and 137 decreases between consecutive switches; on
    gated_switchbestexp N = 4 the sequence rises from 4 to 264 and from 36 to 209 repeatedly (experiments/si/vjfast
    --trace, 15:10Z). The increases are exactly the counter resets: a correction switch of small traffic makes a large
    structure improving again.
3.2 Φ_2 = Σ_x |P_σ(x)| or Σ_x length(Ξ(x)): not monotone (lengths go both ways under ≺).
3.3 Φ_3 = number of vertices whose valuation is final (= Ξ_{σ*}(x) for the ≺-optimal σ*, Friedmann Lemma 4.3's object).
    PROVED: Φ_3 is non-decreasing (Ξ(x) ≤ Ξ_{σ*}(x) always, and Ξ(x) never decreases). Gap P1 (the gap): S7 is not shown
    to make any vertex final per polynomially many switches. The natural claim "when v switches with its downstream
    non-improving (Cor. D'), Ξ'(v) is final" is FALSE: v's new play v·P(w) may pass through vertices that are improving
    (they are downstream of v only after the switch) or through non-improving vertices whose alternative successors
    improve later via switches upstream of v (section 2's second case); both make v improve again. Data: in
    switchallexp N = 6 the vertices of the deceleration lane are switched once per bit increment (count sequence
    "33 30 27 ... 3" repeating), i.e. Θ(2^N) non-final switches in total for switch-all, and for S7 the same lane
    is traversed once per level: the run is 202 switches at N = 6, so the number of non-final switches is not bounded by n
    here either (lane vertices are switched 6 times each).
3.4 Φ_4 = lexicographic vector (Ξ(x_1), ..., Ξ(x_n)) with vertices ordered by traffic, hoped to progress "top-down" like
    the MSF level argument (notes 11:35Z): Gap P2: traffic is not a fixed order (it changes with σ), and the gated and
    switchallexp runs show the top-traffic vertex being re-switched after low-traffic corrections (3.1), so no fixed
    order exists along which S7 is monotone.

## 4. Where the proof breaks, in one paragraph
Lemma D turns S7 into "switch a route-maximal improving vertex, to its steepest edge". That kills every counter whose bits
route through each other (DLMM G_N, M_L, gated_bland: 1 to 3 switches per level), which is the whole content of the
family data. For a polynomial bound one needs, in addition, that a route-maximal vertex cannot be made improving again
polynomially-many-times by switches at route-incomparable vertices (the "corrections" of L-RED R3 section 3). Nothing in
Lemmas T, D or in Thm 3.2 constrains how often an incomparable switch re-opens a vertex: each re-opening needs a successor's
valuation to pass the current one, and valuations have exponentially many values. That is Gap P1 in its sharpest form:
bound the number of times a fixed vertex v is switched by S7 in terms of n and the number of switches at vertices
incomparable to v. Friedmann's switch-all counters re-open the lane vertices Θ(2^n) times; whether S7's route-maximality
plus steepest-edge choice limits re-openings to poly(n) is exactly what L-RED's redesigned reset gadget will test. A proof
would have to exploit the second criterion (steepest edge: Ξ_e(v) maximal), which the attempt above never used beyond
tie-breaking; nothing here shows it is needed or sufficient.

## 4b. Input from L-RED (R3 section 3b, claude/l-red 7da31f7; UNREFEREED, credited to L-RED), and what it does to Gap P1
Two ingredients, both unrefereed:
(1) Lemma D ("downstream first"), as in section 1.
(2) "Closable gates absorb their entries": in a Friedmann cycle gate (1106.0778 section 6), while the gate is closable (Odd at
    e_i prefers d_i's default route to the exit), every play entering the gate passes its decision vertex d_i; by Lemma D the
    closing switch at d_i then outranks every switch at a vertex whose play enters the gate, so a reopened gate re-closes
    before anything upstream of its entries moves. L-RED's statement of what a counter would need: a selector whose
    improvability depends on the lower bits' state while its traffic (Lemma D) does not outrank theirs; its three redesigns
    (split entries, downward exit chains, stripped gates) all fail for stated reasons (R3 section 3b).
Reading for the proof. (2) is a sufficient condition for a vertex to be re-closed "immediately": a vertex d whose every entry
passes d while it is improving cannot be out-waited by its entries' corrections. Turned into a potential claim it reads:
  Claim R (not proved): if every vertex x that can make v improving again (section 2: x upstream of v's successors) has its
  play through v whenever v is improving, then between two switches at v some vertex NOT upstream of v must switch, and such
  a switch never changes v's successors' valuations ... [this last step is FALSE in general: a switch at a route-incomparable
  vertex y changes exactly up(y), which may contain v's alternative successors without containing v; that is the precise
  shape of Gap P1 and of L-RED's "selector whose improvability depends on the lower bits' state while its traffic does not
  outrank theirs": y = the selector, v = the reopened gate.]
So (2) narrows Gap P1 to: vertices y that are route-incomparable to v but upstream of a successor of v (y reaches v's
alternative w without passing v), i.e. the "entries from above" of a gate that avoid its decision vertex. L-RED shows
Friedmann's entries cannot avoid d_i (split entries create Odd-won cycles). A proof of polynomiality would need the
general statement: the number of times a vertex v is re-opened by switches at vertices upstream of its alternative
successors but not of v is polynomial. Nothing here proves it; it is the sharpest form of Gap P1 at the end of the box.

## 4c. Refocus (Lead 14:01Z; L-RED R3 section 3c, claude/l-red 3bcb4d9, UNREFEREED, credited to L-RED): downstream-first runs
Definitions (L-RED). For generic σ, u is downstream of v if v's (σ, τ)-play visits u. A single switch at v is
downstream-first (df) if no other improving vertex is downstream of v; a run is df if all its switches are.
Claim 1 (L-RED, from Lemma D): every S7 switch is df. Claim 2 (L-RED, antichain_check.py): every published exponential
single-switch run the fleet ported is NOT df at a constant fraction of its steps (Bland on G_N: 4/7, 11/15, 26/31; LSF on
M_L: 4/11, 11/26; Zadeh+index on zadehexp: 26/71, 72/155; Cunningham with PGSolver's ordering: 19/38 ... 516/799; MSF on
gated_bland: 26/31). Claim 3 (L-RED): Friedmann-spine gate counters cannot have a df exponential run.
THE STATEMENT S7 NOW RESTS ON (Lead's formulation): "every downstream-first single-switch improvement run in a sink game has
length poly(n)". If true, S7 is polynomial in iterations on sink games (Claim 1), with Gap W for general games; if some
polynomial family has an exponential df run that pads can make route-maximal, S7 dies.

Data, df-filtered rules (L-SI, vjfast df-*: the base rule restricted to df switches; 15:05Z), on the counters that kill the
unfiltered rules (best-reward start; M_L from σ_0; G_n from σ_0):
| rule (df-filtered) | zadehexp N = 4, 6, 8, 10 | M_L L = 4..10 | DLMM G_n n = 4..12 | gated_bland N = 4..10 | switchallexp N = 2, 4, 6 |
|---|---|---|---|---|---|
| df-lsf | 45, 87, 137, 195 | 4, 6, 8, 10 | 1 | 1 | 43, 98, 152 |
| df-index (Bland) | 63, 171, 351, 619 | 4, 6, 8, 10 | 1 | 1 | 43, 125, 237 |
| df-zadeh | 83, 133, 183, 233 | 4, 6, 8, 10 | 1 | 1 | 60, 124, 190 |
| df-cunningham | 27, 47, 73, 93 | 4, 6, 8, 10 | 1 | 1 | 36, 62, 90 |
| df-msf | 43, 61, 79, 97 | 4, 6, 8, 10 | 1 | 1 | 33, 67, 101 |
Unfiltered on the same games: lsf 2^(L+1) on M_L, Bland 2^n - 1 on G_n, msf 2^N - 1 on gated_bland, zadeh ~16N² on
zadehexp. The df restriction alone collapses every counter in the bench to linear or quadratic growth, whichever base rule
is applied inside it (OBSERVED). Adversarial searches for the worst df run (df-index and df-lsf, one-player acyclic sink games
and two-player sink games, n ≤ 14, fast engine): results appended below when finished.

Proof attempt for the df statement, one-player acyclic sink games first (all vertices Even, edges toward the sink, so the
play is the σ-path and "downstream" is "later on the σ-path"):
  Setting: val(x) = the set of vertices on x's σ-path (above the sink), ordered lexicographically by rank (length as a last
  component). x is settled if val(x) = val*(x), the optimum. The sink is settled. x is improving iff some successor w has
  val(w) ≻ val(σ(x)).
  Lemma A (PROVED): on a σ-path with no improving vertex, let u be the last unsettled vertex (closest to the sink). Then
  σ(u) is settled, u has an unsettled alternative successor w* (an optimal successor) with val(w*) ≺ val*(w*), and
  val(w*) ⪯ val(σ(u)) = val*(σ(u)) ⪯ val*(w*). (From non-improving at u and settledness after u.)
  Consequence: a df switch at v happens only while the vertices after v on its path are either settled or "blocked" (their
  optimal successor is itself unsettled). The switch at v moves σ(v) to its best current successor w.
  Gap DAG-1 (the gap): no potential proved. The candidates tried: (i) number of settled vertices (non-decreasing, PROVED;
  not shown to increase within poly many df switches: a df switch at v settles v only if its best current successor is
  settled AND optimal, which fails when the optimal successor is blocked); (ii) number of (x, w) pairs with val(w) = val*(w)
  (non-decreasing; same problem); (iii) depth-ordered lexicographic value vector (progress only if df switches were taken
  deepest-first, which df does not require: df allows switching a shallow vertex while deep improving vertices exist OFF its
  path, e.g. under its alternative successors, and that is exactly how a lower bit could be "counted up" while a higher one
  waits; Claim 2 shows the known counters still needed non-df steps, which is evidence, not a proof).
  Observation (OBSERVED, antichain data of L-RED): in a one-player game a vertex's improvability depends on bits of its own
  path only, so a counter's "bit 1 observes bit 2" forces bit 2 downstream of bit 1 and the df condition then orders the
  switches deepest-first on that path; whether a one-player DAG can encode a counter without this (bits observing each
  other through disjoint paths that merge below) is the open content of Gap DAG-1.
Two-player sink games: Gap O (observation through Odd). An Odd vertex y on v's play with an alternative route through a
  vertex z not on v's play lets a switch at z (not downstream of v, possibly df) change v's valuation by rerouting y. So
  "dependence = downstream" fails, and the df condition no longer forces deepest-first processing of dependent switches.
  L-RED's Claim 3 covers Friedmann-spine gates (where the entries pass the decision vertex); a general argument is missing.
  This is where L-SI expects a construction, if one exists.
Gap W (sink games WLOG?): no reduction known to L-SI. Friedmann 1106.0778 section 5 introduces sink games as a construction
  device, not as a normal form; PGSolver's cheap-escape transformation (transformations.ml:271-320, ported in
  experiments/hard-families/pgsolver_si.py for switch-best) adds to every vertex an escape to a losing cycle of the lowest
  priorities, preserving winners, but L-SI has not shown that every run from the best-reward start is then sink-seeking.
  In general games the cycle component changes at most n² times (notes 11:35Z, S9), so a bound for sink-seeking stretches
  would give a bound for general games only with an argument that stretches between cycle changes behave like sink games.

## 4d. DEAD ROUTE: "every downstream-first run is polynomial" (refuted by L-RED, Lead 14:10Z; pending L-RED's push; credited to L-RED)
L-RED computed, by dynamic programming over all trees, the exact longest downstream-first run on FHZ's one-player counter
G_{n,1,1,1} (arXiv 1410.7530 Fig. 3) encoded as a sink parity game by the R2 encoding: 5, 20, 53, 124 for n = 1..4
(unrestricted longest runs 7, 30, 85, 204); the df run is the counter's own increment sequence (lower bits reset through the
higher level while that level is quiet). So the statement of 4c is FALSE already for one-player acyclic sink games: Gap
DAG-1 is closed in the negative, and the df-filtered data of 4c only say that the ported counters' intended runs are not df,
not that df runs are short. Unpadded S7 on P_{n,1,1,1}: 8, 14, 22, 32, 44 (n = 1..5, quadratic; L-RED).

## 4e. Reformulation (the question S7 rests on at the end of the box)
S7's order is the COUNT order (traffic, Lemma T) with the steepest-edge tie-break, not merely downstream-first. The question:
can count-ranking be steered along an exponential downstream-first run on a polynomial-size game? Precisely: is there a
polynomial family with a downstream-first run of super-polynomial length such that, at every step, the vertex the run switches
is route-maximal among the improving vertices with a strictly larger count than every route-incomparable improving vertex
(pads may add any non-negative constant to the traffic of any vertex, and the same constant to everything downstream of it),
and its switched edge is the steepest? L-RED tests this as a linear program in pad values along FHZ's df run.
For a proof of S7's polynomiality the contrapositive is what must be shown: along ANY exponential df run, the count order is
violated at a constant fraction of steps for every pad assignment. The proof material available: Lemma T (count = traffic),
Lemma D (downstream dominance), and the fact (PROVED, section 2) that a switch at v changes exactly up(v). What a proof would
need beyond these: a lower bound on the traffic of the "correction" vertices that the counter must switch before a reopened
bit, in terms of the traffic of the bit vertex, independent of pads. In FHZ's counter the corrections are the lower bits'
own re-closings, which route through the higher level while it is quiet; whether their traffic can be padded above the
reopened bit's traffic at every step is exactly the LP. Nothing in this box settles it; the attempt stops here.

## 5. Status
Not a proof; not a disproof. Named gaps: T1 (genericity), D1-D2 (cycles in plays), P1 (re-openings by incomparable
switches), P2 (no fixed progress order), O (observation through Odd), W (sink games WLOG); DAG-1 closed negatively (4d);
the live question is 4e (count-steering along a df run). The data on which 3.1 and 3.3 rely: experiments/si/out traces (vjfast --trace).
