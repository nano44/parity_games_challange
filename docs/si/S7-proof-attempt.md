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

## 5. Status
Not a proof; not a disproof. Named gaps: T1 (genericity), D1-D2 (cycles in plays), P1 (re-openings by incomparable
switches), P2 (no fixed progress order). The data on which 3.1 and 3.3 rely: experiments/si/out traces (vjfast --trace).
