# Packet P-N5-GATESHUT: at a Friedmann-type Odd gate, a shut gate (τ(e) = h) does not reopen while (H1)-(H3) hold (Lemma GATE-SHUT) — every game
L-LIT successor (Opus 5.5), D18, Lead reading L40. Lead's instruction of 11:01Z (message): "GATE-SHUT: freeze it as a SEPARATE packet
docs/lit/P-N5-GATESHUT.md, same standard (every symbol from SPEC / RESULTS, (H2) and the dual-(VJ) step fully explicit, premises named,
pinned check docs/lit/T34-gateshut-check.py + expected output, quote check)". Written 2026-10-29 from 11:19Z (date -u). FROZEN at push;
later text goes into docs/lit/P-N5-GATESHUT-fixes.md. Working note: docs/lit/T34-friedmann-vs-n5.md §2-§3. This packet governs.
Its text is Part (B) of docs/lit/P-N5-MPGS.md (a23179b0) verbatim, with the premise list restricted to what (B) uses; P-N5-MPGS is
WITHDRAWN in favour of the two separate packets P-N5-MATCHPHI (12b7d12a) and this one (P-N5-MPGS-fixes.md F1).

What this is and is not:
- A structural lemma on Odd's improving edges, every game. It explains why Friedmann's lower-bound gadgets do not delay N5
  (T34 §3, READING). It bounds no count. Not a TARGET.md claim; no running-time bound; G-N5-TIME stays open.
- Labels: PROVED (L-LIT, unrefereed; to sign) / DATA (not to sign) / READING (not to sign). L-COMP's code is used read-only by the check;
  its data are DATA only, never premises.
- Quote check: docs/lit/P-N5-GATESHUT-quotecheck.py (every [Q …] against git at its commit; expected output "quotes=9 bad=0").

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| B1 | Fact B1 (dual order on equal cycle nodes reverses the path-set comparison), Fact B2 ((VJ) on G^d) | PROVED (to sign) |
| B2 | Lemma GATE-SHUT: at a state t with τ_t(e) = h, (H1)-(H3) ⇒ (e, d) ∉ Iτ_t | PROVED (to sign) |
| B2 | **Added statement:** "(H1)-(H3) at every state of a stretch on which τ(e) = h ⇒ (e, d) ∉ Iτ at every state of it, and τ never moves from h to d at a transition from it" | PROVED (to sign) |
| B3 | pinned check | DATA |
| B4 | reading | READING |

## Premises (LANDED), quoted
- **[S1-rank]** SPEC S1:
  - [Q docs/new/N5-ssi-global.md@1f15c91b:27] «injective priorities: rank(v) = position of v in V sorted by (Ω(v), v); p'(v) = 2·rank(v) + (Ω(v) mod 2).»
- **[S1-val]** SPEC S1:
  - [Q docs/new/N5-ssi-global.md@1f15c91b:28] «valuation of v under (σ, σ̄): (c, P, ℓ), c = the most relevant (max p') vertex of the cycle the play from v ends in, P = set of»
  - [Q docs/new/N5-ssi-global.md@1f15c91b:29] «vertices on the play before reaching c with p' > p'(c), ℓ = number of steps to reach c.»
- **[S1-order]** SPEC S1:
  - [Q docs/new/N5-ssi-global.md@1f15c91b:31] «Σ_{u∈P} (+2^rank(u) if Ω(u) even else −2^rank(u)); then ℓ: if c is odd, longer is better for Even; if c even, shorter is better.»
  - The line before it (l. 30): "order (better for Even): compare reward of c (p'(c) if even, −p'(c) if odd); then P by the signed weight".
- **[S1-dual]** SPEC S1, Odd's side:
  - [Q docs/new/N5-ssi-global.md@1f15c91b:45] «Odd's side: everything on the DUAL game G^d (owner swapped, Ω + 1); τ is an "Even" strategy of G^d; Ξτ, τ̄ (= Even's optimal»
- **[A3]** SPEC ambiguity table, row A3:
  - [Q docs/new/N5-ssi-global.md@1f15c91b:73] «settled; ranks of G^d equal those of G (Ω + 1 keeps the order and the index ties)»
- **[S2]** SPEC S2:
  - [Q docs/new/N5-ssi-global.md@1f15c91b:47] «S2 Improving edges: Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than Ξσ(σ(v))}; Iτ the same on G^d for τ.»
- **[S4bc]** SPEC S4b, S4c (l. 54-57). S4b: "A(v) = {τ(v)} ∪ {w : (v, w) ∈ Iτ} for Odd v ... τ_new = Odd's optimal counterstrategy
  (S1 procedure on H', not dual) to σ". S4c (Odd's fallback): "otherwise do the same for Odd on Iτ with G^d's valuations".
- **[VJ]** RESULTS R57 (a), signed by both referees, on every game:
  - [Q docs/RESULTS.md@1f15c91b:2907] «(a) Premise (VJ), on every game: for every positional σ and every positional Odd strategy τ′, Ξσ(v) ⊴ V_{σ,τ′}(v) at every v; read from»
- **[DELTA]** RESULTS R84 (a), signed by both referees:
  - [Q docs/RESULTS.md@1f15c91b:4967] «(a) Fact DELTA (§1, with F4): for sets A ≠ B of ranks, weight(B) > weight(A) iff d := d(A, B) is even and d ∈ B ∖ A, or d is odd and»
  - It continues: "d ∈ A ∖ B", where weight(A) := Σ_{r ∈ A} s(r)2^r, s(r) = +1 for even r and −1 for odd r, and a rank is even or odd
    as Ω of its vertex (R84 F5).


## B0. Setting and symbols
- **State t of an N5 run** (any game).
  - σ := σ_t, τ := τ_t.
  - G^d: the dual game (owner swapped, Ω + 1) [S1-dual].
  - Ξτ: S1's valuation of τ on G^d [S1-dual].
  - τ̄: S1's optimal counterstrategy on G^d to τ, an Even strategy of G. On G^d, τ is the "Even" strategy and τ̄ the "Odd" one.
- **Orders.**
  - ⊴ is S1's order on G ("better for Even" [S1-order]).
  - ⊴_d is S1's order on G^d ("better for G^d's Even player", i.e. better for Odd of G).
- **Iτ.** By [S2]: (e, w) ∈ Iτ iff e is Odd, w ≠ τ(e), and Ξτ(w) ▷_d Ξτ(τ(e)) (strictly better in ⊴_d).
- **Plays.** For an Even strategy σ′ of G and Odd strategy τ, π(x; σ′, τ) is the play from x under (σ′, τ). It is a lasso: a
  simple prefix, then a simple cycle.
  - V^d_{τ,σ′}(x) is S1's valuation on G^d of that play (S1's (c, P, ℓ) read on G^d).
  - Ξτ(x) = V^d_{τ,τ̄}(x) by definition.
- **The gate.**
  - e: an Odd vertex.
  - h := τ(e).
  - d: a successor of e with d ≠ h.
  - π = (π_1, …, π_m), m ≥ 1, with π_1 = d: a sequence of distinct EVEN vertices of G with edges π_k → π_{k+1} (k < m) and
    π_m → e.
  - Q := {π_1, …, π_m, e}. Its vertices are distinct, since e is Odd.
  - ρ := π(h; τ̄, τ), the play from h that defines Ξτ(h).
  - c_h := the cycle node of Ξτ(h).
- **Hypotheses at state t.**
  - (H1) rank(u) > rank(c_h) for every u ∈ Q.
  - (H2) ρ, prefix and cycle, contains no vertex of Q.
  - (H3) the vertex of largest rank in Q has even Ω (in G).

## B1. Two facts used (each with its proof; to sign with the Lemma)
**Fact B1 (dual order on equal cycle nodes).** For valuations X = (c, P, ℓ) and X′ = (c, P′, ℓ′) with the same cycle node c and
P ≠ P′: X ◁_d X′ iff X′ ◁ X.

Proof.
- By [A3], G^d has the same ranks as G. So the set P of a play is the same in both readings: by [S1-rank] on either game, p'(u) > p'(c)
  iff rank(u) > rank(c).
- The cycle node is the same vertex in both readings. It is the vertex of maximal p' on the cycle, and p' and G^d's p' are both
  2·rank + (0 or 1), so in both it is the vertex of maximal rank.
- By [S1-order] with Ω + 1, G^d's signed weight of P is Σ_{u ∈ P} (+2^rank(u) if Ω(u) + 1 is even else −2^rank(u)) = −weight(P).
- The cycle nodes are equal, so both orders go to the path sets next, and these differ (P ≠ P′). The ℓ component is never reached.
- So X ◁_d X′ iff −weight(P) < −weight(P′) iff weight(P′) < weight(P) iff X′ ◁ X. □

**Fact B2 ((VJ) on G^d).** For every positional Even strategy σ′ of G and every x: Ξτ(x) ⊴_d V^d_{τ,σ′}(x).

Proof. [VJ] holds "on every game", hence on the parity game G^d. G^d's "Even" strategy is τ and its "Odd" strategies are G's Even
strategies σ′ [S1-dual]; S1's valuation of τ on G^d is Ξτ. Instantiate [VJ] with σ := τ and τ′ := σ′. □

## B2. Lemma GATE-SHUT (PROVED, L-LIT, unrefereed; to sign)
**Statement.** At a state t with τ(e) = h, (H1), (H2) and (H3) imply (e, d) ∉ Iτ.

**Proof.**
1. **A deviation σ′.** Let σ′ := τ̄ except σ′(π_k) := π_{k+1} for k < m and σ′(π_m) := e. σ′ is a positional Even strategy of G and
   differs from τ̄ only on {π_1, …, π_m} ⊆ Q.
2. **The play from h is unchanged (this is where (H2) is used).** π(h; σ′, τ) = ρ. Every vertex ρ visits is outside Q by (H2), and
   at every such Even vertex σ′ = τ̄. At every Odd vertex both plays follow τ. So the two plays agree step by step, cycle included.
3. **The play from d.** π(d; σ′, τ) = π_1, …, π_m, e, then ρ.
   - It follows σ′ along π, then τ(e) = h, then step 2.
   - It is a lasso with the same cycle as ρ: the prefix π·e is simple and disjoint from ρ by (H2).
   - So its cycle node is c_h, and its set is P(ρ) ∪ {u ∈ Q : rank(u) > rank(c_h)} = P(ρ) ∪ Q, by (H1) and the P-membership rule of
     Fact B1's proof.
   - Write V := V^d_{τ,σ′}(d) = (c_h, P(ρ) ∪ Q, ℓ(ρ) + |Q|). Here Q ∩ P(ρ) = ∅ by (H2).
4. **V is strictly worse for Odd than Ξτ(h) (this is where (H3) is used).**
   - The sets P(ρ) ∪ Q and P(ρ) differ exactly by Q. The largest rank d* of the difference is that of the top vertex of Q: even by
     (H3) and in the larger set.
   - So [DELTA] gives weight(P(ρ) ∪ Q) > weight(P(ρ)). Same cycle node, so Ξτ(h) ◁ V.
   - By Fact B1, V ◁_d Ξτ(h).
5. **Optimality of τ̄ (this is where (VJ) is used).** Fact B2 with x = d: Ξτ(d) ⊴_d V.
6. **Conclusion.** Ξτ(d) ⊴_d V ◁_d Ξτ(h) = Ξτ(τ(e)). So Ξτ(d) is not strictly better than Ξτ(τ(e)) in ⊴_d, and by [S2]
   (e, d) ∉ Iτ. □

**Added statement (B), Corollary.** Let [t_0, t_1] be a stretch of states of one run with τ_t(e) = h and (H1)-(H3) at every
t ∈ [t_0, t_1]. Then (e, d) ∉ Iτ_t for every such t, and τ_{t+1}(e) ≠ d for every t ∈ [t_0, t_1].

Proof.
- The first claim is the Lemma at each t.
- S4b: τ_{t+1}(e) ∈ A(e) = {τ_t(e)} ∪ {w : (e, w) ∈ Iτ_t} [S4bc], and d ≠ h is not in it.
- S4c (Odd's fallback): τ_{t+1}(e) is τ_t(e) or a w with (e, w) ∈ Iτ_t [S4bc].
- S4a does not change τ.
- So τ never moves from h to d at these transitions. □

**What is not claimed.**
- (H1)-(H3) are state-dependent. The Corollary does not say they persist. In particular a cycle node above the gate can appear
  (B3: every observed reopening is of that kind).
- No count is bounded.

## B3. Pinned check (DATA)
docs/lit/T34-gateshut-check.py, sha1 7c33508b2ef6639da2ce736028bcf013f152ed75. It runs N5 (L-COMP's n5b, SPEC mode) on Friedmann's
H_n (L-COMP's hn.py, mode fig), imported read-only. At every visited state with τ(e_i) = h_i it tests (H1), (H2) for gate i:
- d = d1_i, π = (d1_i, d2_i, d3_i);
- (H3) holds by construction, e_i being the gate's top vertex with even priority.

When they hold, it asserts d1_i ∉ Iτ(e_i). Run as `python3 -I docs/lit/T34-gateshut-check.py N R SEED`; expected output:
```
3 0 0   -> n=3 starts=2 gate-states with tau(e)=h: 135; with (H1),(H2): 135; violations (d1 in I_tau): 0; h->d1 flips: 0, of which with (H1),(H2): 0
3 200 3 -> n=3 starts=202 gate-states with tau(e)=h: 14385; with (H1),(H2): 14217; violations (d1 in I_tau): 0; h->d1 flips: 102, of which with (H1),(H2): 0
4 100 4 -> n=4 starts=102 gate-states with tau(e)=h: 12045; with (H1),(H2): 11911; violations (d1 in I_tau): 0; h->d1 flips: 97, of which with (H1),(H2): 0
5 30 5  -> n=5 starts=32 gate-states with tau(e)=h: 5783; with (H1),(H2): 5705; violations (d1 in I_tau): 0; h->d1 flips: 48, of which with (H1),(H2): 0
```
- S3 and F only for n = 4, 5, 6, 8: 228, 350, 510, 872 gate-states, all with (H1), (H2), 0 violations, 0 flips.
- Starts: S3, F = (ι_{H_n}, σ̄(ι)), and L-COMP's CE.rand_start with the given seed.
- The 247 h → d1 flips all occur where (H1) or (H2) fails. Example: rand4, n = 3, iteration 0. The cycle node of Ξτ(h1) is e2,
  above gate 1, so gate 1's vertices are not in P. The path sets of d1_1 and h1 are equal, and the lengths (9 vs 5) decide.
- The hypotheses are needed: the unhypothesised form is false on these instances.

## B4. READING
- In Friedmann's 1-sink games (arXiv 1106.0778 v2, §5, p.8; opened), the cycle node is the sink, below every gate. So (H1) is
  automatic, and (H2) holds along the runs from S3 and F (B3).
- With the gate shut, S4a (Even's optimum against τ) prices the edge into the gate at its full value. Friedmann's delay by hiding
  (§6.1, Lemma 6.1 (3), Lemma 6.2 (2); §8 p.26, §8.2) therefore has no effect: docs/lit/T34-friedmann-vs-n5.md §3.
- CONJECTURE NO-HIDE there is not part of this packet.
