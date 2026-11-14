# B7, part 2: the schedule of RF's run on K^s_n and a proof sketch of the doubling (L-RED-B successor 8, 2026-11-14)
Companion of docs/red-b/B7-RF.md (the family, the rule and the DATA are there, §4). Status: the SCHEDULE of §1 is DATA (equal to
the real run, iteration by iteration, for n = 1..9, tool b7sched.py); the count of §2 is arithmetic on the schedule; §3-§5 are a
PROOF SKETCH by this lane, UNREFEREED, with its gaps listed in §6. Nothing here is a result (D1, reading L43).

## 1. The schedule (DATA, n ≤ 9)
Notation: gate γ = (i, c); L = the gate list; «γ′ after γ» = later in L (nearer to R); below(γ) = the reader of the next gate,
or R. Counter t = 1, …, 2^n − 1. j(t) := the lowest set bit of t. cx_t(i) := the lowest set bit of t above i (x if none).
CUR(t) := {(i, cx_t(i)) : bit i set in t}: the CURRENT gates. A closed gate outside CUR(t) is STALE at t.
Step t consists of the following iterations of RF, in this order; the vertices named are exactly the vertices that switch.
 1. CLOSE: d(j, c) → e(j, c), with j = j(t), c = cx_t(j).
 2. ROOT: R → f(j, c); in the same iteration g_j → f(j, c) if j ≥ 2.
 3. SKIPS: for i = j − 1, j − 2, …, 2, one iteration each: g_i → s(i, j).
 4. RESETS: while some stale closed gate QUALIFIES, the qualifying gate that is latest in L opens (d → below), one iteration
    each. A stale closed gate (i, c′) qualifies at t iff the bits 1, …, i − 1 are all set in t and (bit i is set in t, or
    (i, cx_t(i)) comes before (i, c′) in L).
The run stops after step 2^n − 1 (then every gate is closed iff it is in CUR(2^n − 1) = {(i, i + 1) : i < n} ∪ {(n, x)}).
DATA: `python3 experiments/red-b/b7/b7sched.py 1 9` → for every n ≤ 9 the schedule and the real run have the same length and
the same set of switches in every iteration (sdiff 0, ldiff 0; 2 + 7 + 19 + … + 1,771 = 3,460 iterations compared). Control
B7S_CTRL=1 (the EARLIEST qualifying gate opens first) fires from n = 3 on.
What the schedule says in words: the closings are the 2^n − 1 increments of a binary counter (bit i closes in the gate whose
context is the lowest set bit above it); a closed gate of an unset bit is not opened at once: it waits until nothing below it
in L can still move, and then the stale gates open bottom-up.

## 2. The count (arithmetic on the schedule)
Step t has 2 iterations of kinds 1-2 and max(0, j(t) − 2) skips; the number of t ≤ 2^n − 1 with j(t) = j is 2^(n−j). Every gate
that is ever closed is closed once per closing iteration, and all but the n final ones are opened again, one iteration each. So
 iterations = 2(2^n − 1) + Σ_{j=3..n} (j − 2)·2^(n−j) + (2^n − 1 − n) = 2(2^n − 1) + (2^(n−1) − n) + (2^n − 1 − n)
            = 7·2^(n−1) − 2n − 3,
the law of B7-RF.md §4.2 (measured to n = 15 there). For the kill only «at least 2^n − 1» matters: the closings alone.

## 3. Values (what every comparison reduces to)
Order facts used (from the rule's priorities): (O1) every high vertex (s, f, h) is above every low vertex (R, C, d, e, g);
(O2) the band of bit i + 1 is above the band of bit i, and inside a band every s is below every f, every f below every h;
s and f are odd, h is even; (O3) in a gate C < d < e with C, d odd and e even.
All strategies on the run have the SHAPE: R → x or an entry f(γ); g_i → an entry f(i, ·) or a skip s(i, ·); d(γ) → e(γ)
(closed) or below(γ) (open). Assume (Lemma SINK, gap G1) that under every strategy on the run every play ends in x. Then a
valuation is the set of vertices of the play (Friedmann §5), compared by its most relevant differing vertex, and:
- closed γ: Odd at e(γ) must leave by h(γ) (the cycle e, d has the even top e). Ξ(e(γ)) = E(γ) := {e(γ), h(γ)} ∪ X(γ), where
  X(γ) := ∅ if c = x and Ξ(g_c) otherwise; Ξ(f(γ)) = {f(γ)} ∪ E(γ); Ξ(d(γ)) = {d(γ)} ∪ E(γ).
- open γ: Ξ(d(γ)) = {d(γ)} ∪ B(γ) with B(γ) := Ξ(below(γ)); Ξ(e(γ)) = {e(γ)} ∪ min({d(γ)} ∪ B(γ), {h(γ)} ∪ X(γ)).
- reader: Ξ(C(γ)) = {C(γ)} ∪ min(Ξ(d(γ)), B(γ)). Open γ: Odd DROPS (d(γ) is odd). Closed γ: Odd drops iff {d(γ)} ∪ E(γ) ≺ B(γ).
**Lemma TEST.** d(γ) is improvable iff (γ is open and E(γ) ≻ B(γ)) or (γ is closed and B(γ) ≻ E(γ)).
Proof. Open: the only other target is e(γ); {e, d} ∪ B ≻ B by (O3), so Ξ(e(γ)) ≻ B(γ) iff {e, h} ∪ X ≻ B. Closed: the only
other target is below(γ). ∎ So every gate «wants» to be closed iff its EXIT value E beats its ESCAPE value B; a gate whose
state disagrees is WRONG, and the wrong gates are exactly the improvable d's.
For a set of bits S whose gates γ_k (k ∈ S) are closed with contexts chained (the context of γ_k is the next element of S, the
last one x) and whose selectors point to them, write H(S) := {f(γ_k), h(γ_k) : k ∈ S}. Then the high part of Ξ(f(γ_k)) is
H(S ∩ [k, n]), and by (O2) H(S) ≺ H(S′) iff the binary number of S is smaller than that of S′ (the top differing band holds an
h): the value of R is a binary counter.

## 4. The stable state Z(t) and the three facts (sketch)
Z(t) := the state after step t. By the schedule: R → the entry of the gate of the lowest set bit; g_i → f(γ_i) if bit i is set,
g_i → s(i, cx_t(i)) otherwise; closed gates = CUR(t) ∪ the stale gates that did not qualify. Let j be the lowest UNSET bit of t
and c = cx_t(j). The qualification rule gives: no stale gate of a bit below j is closed; of bit j exactly the stale gates
before (j, c) in L may be closed; the stale gates of the bits above j are all still closed. So every closed gate AFTER (j, c)
in L is current.
**(V1) Right-context gates of unset bits are PENDING.** For an unset bit i with c″ = cx_t(i): the high part of E(i, c″) is
{h(i, c″)} ∪ H(S ∩ (i, n]); every escape value is at most the value through R, whose high part is H(S); the top differing
vertex is h(i, c″) (even, band i, against bands below i). So E ≻ B.
**(V2) Current gates are right.** For k ∈ S: the high part of E(γ_k) is {h(γ_k)} ∪ H(S ∩ (k, n]); B(γ_k) is at most the value
through R, high part H(S), which has in addition f(γ_k) (odd, the top of the difference). So E ≻ B, and for the same reason
Odd does not drop into a current gate.
**(V3) A gate whose context bit is unset, or is not the lowest set bit above, is worth less than its escape** once the
selectors have moved: its exit runs through a skip s(c′, ·), odd and above every bonus of the bits below c′ (O2), or misses the
band of a set bit that the escape has. So a stale closed gate is WRONG (it wants to open) and an open gate with a wrong context
is right (it stays open). This is the GENUINE RESET; it does not depend on any timing.
**(ORDER) In Z(t) the only dependency sink is d(j, c).** Improvable vertices in Z(t): the pending gates (V1) and the stale
closed gates (V3); R and the selectors are not improvable. The play from below(j, c) passes only gates after (j, c): open
gates with wrong contexts (not improvable), current gates (Odd does not drop, V2), then R and the entry chain: nothing
improvable, so d(j, c) is a sink. Every other improvable d(γ) has γ before (j, c) in L, and its escape play (its current
play if γ is pending, its improving target if γ is stale) runs down L until Odd drops into a wrong closed gate (improvable) or
reaches C(j, c), where Odd drops into the open gate (j, c): so it depends on an improvable vertex later in L. Exits never
enter an open gate in Z(t) (a selector of an unset bit rests on a skip), so all dependencies point down L, no two improvable
vertices are mutually dependent, and {d(j, c)} is the only component without an outgoing edge. RF closes (j, c): iteration 1
of step t + 1.
**(ROOT)** After the closing, f(j, c) beats R's current entry (top differing vertex h(j, c)) and every other closed gate's
entry; R's plays hold nothing improvable; g_j likewise (f(j, c) against its skip: top h(j, c)). Every other improvable vertex
has R on its escape play. So exactly R and g_j switch: iteration 2.
**(SKIP)** Now the entry chain is S′ = {j} ∪ (S above j). For 2 ≤ i < j the selector g_i sees its skip s(i, j) → g_j beat its
current gate (top h(j, c)), every other skip (they miss band j) and every entry of an open gate of bit i (s < f, O2: this is
the point of the skip edges). g_i's current play passes g_(i+1) while that one is improvable; so the selectors move top-down,
one per iteration: iteration kind 3. The gates γ_k (k < j) are now wrong (B has h(j, c), E does not: V3) but each depends on
the selector on its exit until it has moved.
**(RESET)** After the skips the wrong closed gates are the old current gates of the bits below j and the older stale gates.
Such a gate is a sink iff no improvable vertex lies on its plays: its exit holds none (the selectors have moved); its escape
runs down L and meets a pending gate of bit i′ < i (if some bit below i is unset), a pending gate of its own bit after it, or
a wrong closed gate after it. That is the qualification rule, and it opens the qualifying gates bottom-up: iteration kind 4.
When none qualifies, the state is Z(t + 1) and (ORDER) applies again.

## 5. Why this is a counter
The entry chain of R is the set of set bits; by §3 its value is the binary number t. (ORDER) + (ROOT) say that between two
moves of R exactly one gate closes, the gate of the lowest unset bit with the right context, and that R then moves to it: the
number grows by exactly 1 per closing. The run ends only when nothing is improvable; by (V1) that needs every bit set. So the
run contains 2^n − 1 closings: RF makes at least 2^n − 1 iterations on a game with 3n² + 3n + 1 vertices.

## 6. Gaps of the sketch (for the proof packet and the referees)
- G1 Lemma SINK: every play ends in x under every strategy of the run (used to read valuations as path sets). DATA: every
  evaluation of every run has all cycle nodes = x. Proof idea: Theorem 3.2 of the source (valuations only grow) and Odd wins
  every vertex; an entry of R or g into an OPEN gate would close an Odd-won cycle through an f, so it is never improving.
- G2 The values of the STALE closed gates in every intermediate state (inside a step), and that Odd's drops into them never
  change the sign of a test of §4. §4 treats them only in Z(t) and only through (V3).
- G3 (V3) in full: every wrong-context gate in every intermediate state, with the selector either moved or not yet moved.
- G4 The bookkeeping of kind 4: that the qualifying gates open one per iteration and bottom-up (the upper one sees the lower
  one because Odd drops into a wrong closed gate), and that nothing else is improvable-and-unblocked meanwhile.
- G5 The statement for the tie rule and S1: on K^s_n no two successors have equal valuations (argued in B7-RF.md §1), to be
  written as a lemma.
- The schedule itself is checked by machine for n ≤ 9 only; the law for n ≤ 15 (two engines of this lane).

## 7. Must-0 counters on the real run (DATA, tool experiments/red-b/b7/b7facts.py, n ≤ 8)
At EVERY iteration of RF's run: `sink` (vertices whose cycle node is not x: Lemma SINK), `eqval` (pairs of distinct successors
of one vertex with equal valuations: gap G5), `test` (gates for which «d improvable» differs from «wrong» in the sense of Lemma
TEST, with E and B read from the engine's valuation). At every STABLE state Z(t) (the next iteration is a CLOSE): `zclosed` (the
closed gates are CUR(t) plus the stale gates that the qualification rule leaves closed), `zsel` (R and the selectors point as
§4 says), `zimp` (the improvable set is exactly the right-context gates of the unset bits plus the stale closed gates: V1-V3),
`zsink` (RF's sinks are exactly {d(j, c)}: ORDER). All seven are 0 for n = 1..8 (out/b7facts_1_8.out; 255 stable states and
877 iterations at n = 8; the number of stable states is 2^n − 1 for every n). Controls: B7F_CTRL=1 (right context := the
HIGHEST set bit above) fires zimp from n = 3; B7F_CTRL=2 (qualification without its second clause) fires zclosed and zimp from
n = 2.
Not yet counted separately: ROOT, SKIP and RESET inside a step (they are implied by the schedule test of §1, which compares
the set of switches of every iteration).

## 8. The repaired dependency (the Lead's question of 15:20Z; DATA, tool experiments/red-b/b7/rfrep.py)
- Reading A, «every Even vertex with a choice on the two plays»: CH := the Even vertices with at least two successors;
  D′(v) := (π(σ(v)) ∪ ⋃_{w ∈ T(v)} π(w)) ∩ CH ∖ {v} for v ∈ CH (T(v) empty if v is not improvable); a component of (CH, D′) is
  ACTIVE if it holds an improvable vertex; the improvable vertices of the active components that reach no other active
  component move. (Without «active» the literal rule stalls as soon as a sink component holds no improvable vertex.)
- Reading B, «a fixed point of the sink selection»: start from RF's S; drop every v ∈ S that, after the switches of S, has an
  improvable vertex outside S on the play of its new target; repeat until nothing is dropped.
| family | n | RF | reading A | reading B |
| --- | --- | --- | --- | --- |
| K^s_n | 1..8 | 2, 7, 19, 45, 99, 209, 431, 877 | the same eight numbers | the same eight numbers |
| Friedmann G_n (fig4) | 1..6 | 5, 9, 12, 15, 18, 21 | 5, 9, 12, 15, 18, 21 | 5, 10, 14, 18, 22, 26 |
K^s_n SURVIVES both repairs with the same count 7·2^(n−1) − 2n − 3 (out/repair_A_ks.out, out/repair_B_ks.out). READING: the
family uses no blind spot. Its order is a real dependency (the lower pending gate lies on the higher one's escape play), its
reset is a valuation fact (V3), and no step of the schedule moves a vertex «too early»; a rule that waits MORE than RF leaves
a run unchanged in which every iteration already moves the only unblocked vertices. Neither repair makes RF Howard-like on
K^s_n (Howard: at most 10 iterations for n ≤ 7).

## 9. The SPEC's default start S3 (the Lead's item of 15:46Z; DATA)
RF's SPEC starts from S3 (docs/new/N5-ssi-global.md, SPEC S3 with FIX 1: every Even vertex takes its successor of best reward).
On K^s_n itself S3 is NOT σ_0: d(γ) prefers e(γ) (even) to below(γ) (odd), so S3 starts with every gate CLOSED, and from there
**RF is fast on K^s_n: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91 iterations at n = 1..13 = n(n + 1)/2**
(out/ks_s3_1_13.out, C++; n ≤ 8 also on the Python engine, out/ks3_py_1_8.out). So K^s_n kills «RF from σ_0», not the SPEC.
**Family K^s3_n** (rfc2.py `build(n, True, pads=True)`, option --pads): K^s_n with two one-successor pads per gate γ, both of even
priority, in the low block of γ, which becomes C = p, d = p + 2, e = p + 3, y = p + 5, z = p + 7 (p += 8 per gate; the
vertices are listed y, z, C, d, e, f, h per gate): d(γ) → e(γ) | y(γ), y(γ) → below(γ); C(γ) → d(γ) | z(γ), z(γ) → below(γ).
Then S3 = σ_0 (d prefers y to e: asserted by the generator for every n), Odd still drops into an open gate ({d, y} ∪ B
against {z} ∪ B: the top differing vertex is z, even, on the continue side), and no test of §3 changes (the pads are low).
|V| = 4n² + 4n + 1 = (2n + 1)². DATA: **RF from S3 on K^s3_n makes 2, 7, 19, 45, 99, 209, 431, 877, 1,771, 3,561, 7,143, 14,309
iterations at n = 1..12 = 7·2^(n−1) − 2n − 3** (out/ks3_s3_1_12.out, C++; n ≤ 8 on the Python engine with the same numbers).
Instances inst/Ks3_n.pg (+ .start = S3 = σ_0), n = 2..10. So the candidate AS SPECIFIED (start S3) is exponential on K^s3_n
in DATA; the schedule, the sketch and the counters of §1-§7 are written for K^s_n and carry over with y, z added to the
escape values (not re-run on K^s3_n at this commit: b7sched.py and b7facts.py take K^s_n only). By the law the first n beyond
|V|² = (2n + 1)⁴ is n = 20 (3,669,973 > 41⁴ = 2,825,761).
