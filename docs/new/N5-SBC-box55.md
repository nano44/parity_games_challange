# N5-SBC (box 55 (2)): a proof attempt on SBC, Odd's best-reply changes along N5-SF. No polynomial bound; the obstruction is a leapfrog in Ξ's path component
L-NEW successor 33 (Opus 5.5; D14, D18, Lead reading L40). Lead's brief 2026-10-29 15:19Z, BOX 55 (2): «A proof attempt on SBC, Odd's
best-reply changes along an N5-SF run. Is there a monotone quantity on σ̄'s side? DECOUPLE says Even's sequence of distinct σ depends on
σ_0 alone. Use that, plus R15-type well-foundedness on G^d. State any polynomial bound you prove, or the exact obstruction.»
Working note, unrefereed, not frozen, not a TARGET.md claim. Symbols as in docs/new/P-N5-SF-box55.md §0 (F, σ^(j), #σ, SBC_σ, LAM_σ,
stretch, G_σ̄). Labels: PROVED (lane) / CONJECTURE / OPEN / DATA / DEAD / READING.
Tools: experiments/new/box55/sbc.py (candidate quantities along the distinct-σ sequence; SHOW=1 prints the vertex that flips most);
logs box55/sbc_sbe.txt (switchbestexp N = 6..10) and the inline runs quoted below (N = 2..5, same script).

## 0. Summary
- No polynomial bound on SBC is proved. What is proved (§1) sharpens WHERE the count sits:
  - SBC-EQ: SBC_σ ≤ #σ − 1 < (n + m + 1)(1 + LAM_σ + SBC_σ). So SBC is polynomially equivalent to the length of Even's run: bounding it
    is exactly as hard as bounding N5-SF.
  - NO-TRANSFER: SBC_σ and #σ are the same for every τ_0, including a τ_0 from which Odd never moves. So no quantity of Odd's run, and no
    well-foundedness argument on G^d along τ's run (R15 (c) on G^d), can bound SBC_σ. From such a τ_0, N5-SF IS the one-sided
    strategy-improvement rule F, and I = #σ − 1 exactly.
- Monotone quantities on σ̄'s own side (§2), all DEAD with instances: σ̄(σ^(j)) monotone in R15's order on G^d (either direction); O(1)
  entries of an Odd edge into σ̄; O(deg) changes of σ̄ at one Odd vertex; at most n distinct Ξ values per vertex.
- The exact obstruction (§3): a LEAPFROG at an Odd vertex u with two successors a, b. Both Ξ(a) and Ξ(b) rise monotonically (R15 (a)),
  with the same cycle node, in the path-set component P; their order alternates, and σ̄(u) (Odd's argmin) flips at each alternation.
  On switchbestexp_N the flipping vertex is u = 14N + 16 with 1, 3, 7, 15, 25, 27, 29, 33, 39, 41 flips at N = 1..10 (2^N − 1 for
  N ≤ 4). R15 bounds only the cycle-node component (LAM ≤ n(n − 1)) and the length potential (|φ| ≤ n(n − 1)); the P component has
  2^n values, and one vertex takes 290 > n = 260 distinct Ξ values with one cycle node (switchbestexp_10). A proof of SF-POLY must
  bound P-changes, the component Friedmann-type counters use.

## 1. PROVED (lane)
Proposition SBC-EQ. For every game and start: SBC_σ ≤ #σ − 1 < (n + m + 1)(1 + LAM_σ + SBC_σ) ≤ (n + m + 1)(n² − n + 1 + SBC_σ).
Proof. The left inequality: each j counted in SBC_σ is one of the #σ − 1 transitions of the distinct-σ sequence. The right one is
P-N5-SF Theorem SF-RED (b). □
So "SBC_σ is polynomial" and "#σ is polynomial" are the same statement (up to the factor (n + m + 1) and the additive n² term). SBC is
a NAME for where the cost sits (the stretch boundaries), not an easier quantity.
Proposition NO-TRANSFER. Fix G and σ_0. (a) #σ, SBC_σ and LAM_σ are the same for every τ_0. (b) Let τ* be any Odd strategy with
Iτ* = ∅ (for example the final τ of any N5-SF run, SF-TERM). From (σ_0, τ*) N5-SF never changes τ, every iteration changes σ, and
I = #σ − 1; its run is the orbit σ_0, F(σ_0), F(F(σ_0)), … of P-N5-SF §0's map F.
Proof. (a) The distinct-σ sequence is the F-orbit of σ_0 (DECOUPLE), and SBC_σ, LAM_σ, #σ are functions of that sequence. (b) Iτ
depends on τ alone (R15 (d)), so Iτ = ∅ at every state; S4b′ gives τ_new = τ and S4c's Odd branch needs Iσ = ∅ = Iτ, which is S5. Every
iteration therefore has Iσ ≠ ∅ (S4). If A(σ) ≠ σ, σ changes; if A(σ) = σ, then σ_new = σ and τ_new = τ, so S4c's Even branch fires and
σ changes. So each iteration is one F-step and I = #σ − 1. □
DATA (experiments/new/box55/ntcheck.py: rerun from (σ_0, final τ), checks τ constant, I = #σ − 1, same distinct-σ sequence): alt_all
413 games, 0 failures (box55/nt_alt.txt); pinned in check.sh on switchbestexp_2 (I = 58 both ways).
Consequence (the Lead's suggested route). DECOUPLE does hold, but it cuts the wrong way for a proof: it makes Even's run a ONE-SIDED
strategy-improvement run of the deterministic rule F («Even's optimum within its improving edges against Odd's current best reply,
switch-all on Iσ if that optimum is σ»). Odd's run on G^d is ≺_{G^d}-increasing (R15 (c)), but by NO-TRANSFER (b) it can be empty
while SBC_σ is unchanged. A bound on SBC_σ has to come from Even's side alone: it is a running-time bound for the one-sided rule F.
READING: a polynomial bound for a deterministic one-sided strategy-improvement rule on all parity games is not known to me; L-LIT
should say whether F is a known rule (T44 / T45 already say it is not Friedmann's I^glo).
Lemma MONO-XI (PROVED; R15 (a)). Along the distinct-σ sequence, Ξ_{σ^(j)} ⊴ Ξ_{σ^(j+1)} pointwise, and the reward of λ_Ξ(v) never falls.
(This is SF-RED (b)'s LAM argument, stated for use in §3.) So every successor of an Odd vertex has a monotone Ξ chain; only its P and
length components can move inside a stretch.

## 2. Candidate monotone quantities on σ̄'s side (DATA; DEAD with instances)
sbc.py on PGSolver's switchbestexp N (hard-families/pgsolver_port.py; the box-54 instances box54/out/switchbestexp_N.pg, S3 start),
along the distinct-σ sequence (values = #σ). LAM = 0 on all of them: every stretch boundary is a σ̄-change.
| N | n | values | SBC | DUAL UP-only / DOWN-only / mixed | FLIPMAX | ENTMAX | VALMAX | TIE / LOCTIE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 35 | 21 | 1 | 1 / 0 / 0 | 1 | 1 | . | 0 / 0 |
| 2 | 60 | 59 | 4 | 2 / 2 / 0 | 3 | 2 | 27 | 0 / 0 |
| 3 | 85 | 136 | 11 | 5 / 6 / 0 | 7 | 4 | 63 | 0 / 0 |
| 4 | 110 | 259 | 26 | 13 / 13 / 0 | 15 | 8 | 120 | 0 / 0 |
| 5 | 135 | 365 | 49 | 27 / 22 / 0 | 25 | 13 | 171 | 0 / 0 |
| 6 | 160 | 413 | 56 | 31 / 25 / 0 | 27 | 14 | 192 | 0 / 0 |
| 7 | 185 | 457 | 60 | 33 / 27 / 0 | 29 | 15 | 213 | 0 / 0 |
| 8 | 210 | 490 | 75 | 42 / 33 / 0 | 33 | 17 | 229 | 0 / 0 |
| 9 | 235 | 578 | 92 | 53 / 39 / 0 | 39 | 20 | 269 | 0 / 0 |
| 10 | 260 | 620 | 97 | 56 / 41 / 0 | 41 | 21 | 290 | 0 / 0 |
Columns: DUAL = transitions at which σ̄'s valuation on G^d (σ̄ read as Odd's strategy, valued against Even's best reply; larger = better
for Odd) goes up only / down only / both at some vertices; FLIPMAX = most σ̄-changes at one Odd vertex; ENTMAX = most entries of one Odd
edge into σ̄; VALMAX = most distinct Ξ values at one vertex over the run; TIE = σ̄-changes with Ξ unchanged everywhere; LOCTIE = σ̄-changes
at u with Ξ unchanged on every successor of u. (N = 1's VALMAX was not printed by the first script version; N = 1 is not used below.)
- (M1) σ̄(σ^(j)) monotone in R15's order ≺ on G^d, up or down. DEAD: switchbestexp_2 (n 60, sha1 in box55/sha1s.txt). σ̄'s G^d-valuation
  goes DOWN for Odd at vertices 1, 3, 4 at transitions j = 9 and 32, and UP at the same vertices at j = 28 and 41. Two strict moves in
  opposite directions, so no direction of ≺_{G^d} (which needs Ω ◁ pointwise) is monotone. Even a well-founded order on G^d would bound
  SBC only by its height, which is exponential (R15 limit (i)).
- (M2) Each Odd edge enters σ̄ O(1) times. DEAD: switchbestexp_10, an edge enters 21 times (and 2, 4, 8, 13 at N = 2..5).
- (M3) Each Odd vertex changes σ̄ O(deg) times. DEAD: switchbestexp_4, vertex 72 (out-degree 2) changes 15 times; 41 at N = 10.
- (M4) Each vertex takes at most n distinct Ξ values along the run (which with a local rule would give SBC ≤ m·n). DEAD: switchbestexp_4,
  vertex 107 (Even) takes 120 distinct Ξ values with ONE cycle node, n = 110; at N = 10, 290 > 260.
- What survives (DATA): TIE = LOCTIE = 0 on every row. Every σ̄-change at u coincides with a Ξ-change at a successor of u. CONJECTURE LOC
  (every σ̄(u)-change needs a Ξ-change at a successor of u) is OPEN as a proof: S1's procedure breaks ties between successors with equal
  Ξ by its DFS / BFS orders (SPEC FIX 2, FIX 4, Q2), which depend on σ elsewhere, and at a cycle node u the choice comes from S1 (v), not
  from the successors' values. LOC would not bound SBC anyway: it moves the count to Ξ-changes, which are as many (M4).

## 3. The exact obstruction: a leapfrog in the P component
Instance: switchbestexp_2 (n 60), Odd vertex u = 44 with successors a = 39, b = 46 (the vertex 14N + 16 has this shape for every N).
σ̄(u) = 39, 46, 39, 46 at the transitions j = 9, 32, 41 (the only three). Keys (reward, P-weight) of Ξ(a), Ξ(b) before → after (sbc.py
run inline, Engine.key; reward −1 = the same odd cycle node for both, so only P moves):
- j = 9: a 150870679186703328 → 171136785840209920; b 171136785840078848 (unchanged). a rises above b: Odd moves to b.
- j = 32: a 360288004566024266 → 367043369647325216; b 171136785840078848 → 387309567970557824. b rises above a: Odd moves back to a.
- j = 41: a 367043461317247968 → 387309567970688896; b unchanged. a rises above b again: Odd moves to b.
At N = 4 the same vertex (72; successors 67, 74) flips 15 = 2^4 − 1 times in the same pattern (j = 9, 32, 41, 71, 79, 101, 112, 149, …),
and at N = 10 (vertex 156) 41 times.
- READING (the obstruction, stated exactly). Odd's argmin over two successors whose Ξ chains both rise (Lemma MONO-XI) changes once per
  alternation of their order. An alternation needs a strict rise of one chain (elementary when both choices are strict argmins and u is
  not on its own cycle; not proved in general, see LOC). So SBC is bounded by the number of rises of Ξ at successors, and nothing better
  follows from monotonicity alone. R15 makes two of Ξ's three components polynomial: the cycle node (≤ n − 1 changes per vertex, LAM ≤
  n(n − 1)) and the length (through φ, |φ| ≤ n(n − 1), R15 (c)). The path set P is ordered by Σ ±2^rank (SPEC S1) and has up to 2^n
  values; inside one stretch R17 caps value changes at n − 1, but the number of stretches is SBC itself (SBC-EQ). The leapfrog lives in
  P with a fixed cycle node (LAM = 0 on every switchbestexp run). So a proof of SF-POLY must bound how often P can leapfrog at one Odd
  vertex, i.e. bound P-changes of Ξ, which is the component Friedmann-type binary counters encode bits in.
- Growth here (DATA): u's flips are 2^N − 1 for N ≤ 4 and then about 2N + 20 (25, 27, 29, 33, 39, 41 at N = 5..10). Whether a
  switch-best-type family keeps the doubling is L-RED's question (D1: designer and falsifier differ); I built no family.

## 4. Dead ends (also in notes/L-NEW.md)
- (M1) σ̄ ≺_{G^d}-monotone: DEAD, switchbestexp_2 j = 9, 32 (down) vs 28, 41 (up), vertices 1, 3, 4.
- (M2) O(1) edge entries: DEAD, switchbestexp_10 (21). (M3) O(deg) vertex flips: DEAD, switchbestexp_4 vertex 72 (15).
- (M4) ≤ n distinct Ξ values per vertex: DEAD, switchbestexp_4 vertex 107 (120 > 110).
- The route "R15-type well-foundedness on G^d bounds SBC_σ": DEAD by NO-TRANSFER (b) (proved): from τ* Odd's run is empty and SBC_σ
  is unchanged. Obstruction: DECOUPLE separates the two runs completely, so nothing on Odd's run can bound Even's best-reply changes.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box55/sbc.py; logs box55/sbc_sbe.txt.
- FINDINGS: (1) PROVED (lane): SBC-EQ (SBC polynomially equivalent to N5-SF's length) and NO-TRANSFER (Odd's run cannot bound SBC_σ;
  from a τ_0 with Iτ_0 = ∅, N5-SF is the one-sided rule F, I = #σ − 1). (2) DEAD: four monotone quantities on σ̄'s side (instances above).
  (3) Obstruction: a P-component leapfrog at an Odd vertex with two successors (switchbestexp_N vertex 14N + 16; 2^N − 1 flips for
  N ≤ 4). No polynomial bound proved; SF-POLY OPEN.
- NEEDS: none from the owner. To the Lead: L-LIT identification of the one-sided rule F (Proposition NO-TRANSFER makes F the whole
  question).
