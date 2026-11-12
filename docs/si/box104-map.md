# Box 104 (D18, the big map): from boxes 208 / 209 to G-N5-TIME and M4 — the link «genome games → all parity games» fails for N5′-xi: on a W-flat wrapper of ANY parity game H it is Howard's rule on H plus 3 iterations (Lemma WRAP), so Friedmann's counter runs; what is left for N5
L-SI successor 52 (Fable 5.2), D18 / D14 / D1 / D21; Lead brief 2026-11-12 («RESEARCH BOX 104 … IF box 208 … and box 209 … both stand,
what EXACTLY follows for G-N5-TIME and for TARGET.md's M4 … write the chain … with every missing link named as a precise OPEN statement.
Do not assume any link; quote it or mark it OPEN»). Written 2026-11-12 (date -u in the commit).
Labels: PROVED (L-SI lane, unrefereed) / CONJECTURE / DATA (counter, unit, set, scope) / DEAD / OPEN / READING. Every «…» on a line marked
[Q] is copied by script from its source at a pinned commit (experiments/si/box104/quotes104.py; out/quotes104.out: 56 quotes, 0 FAIL;
check104.sh re-checks that each quoted string stands in this file).
**SCOPE LINE: nothing here is a TARGET.md claim, M3 or M4, or a gauntlet step. G-N5-TIME stays OPEN. §3-§6 are a CANDIDATE KILL of the
candidate N5′-xi on general parity games: two lane lemmas (WRAP, FREE-REACH) and DATA, unrefereed, not yet replayed by another lane.**
D1 (owner, verbatim): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the
fleet's own, as wrong until it passes the gauntlet below.» The same care applies to a kill: CLAUDE.md, «A "counterexample" from an
unfaithful implementation is not a counterexample: the referee checks pseudocode against the paper first.»
Tools: experiments/si/box104/ (wrap104.py, free104.py, xck104.py, xtraj104.py, freereach104.py, summ104.py, quotes104.py, run104.sh,
runw104.sh, check104.sh; climb104.py = the O2 probe of §8, smoke-tested only, NOT run; outputs out/, instances inst/); «BOX 104» in experiments/si/check.sh. Engines, read-only: L-NEW's box189 gamma3.py and box190 n5v.py / n5bxi.py
(claude/l-new fcba92fc), L-RED 54's r217 comp.py / gdsl.py / fried.py (claude/l-red 8c01d40e).

## 0. Answer
1. **What boxes 208 + 209 would give (Chain A, §1).** If box 209 stands (polynomial T3 on every Γ3(G)), then with landed R125 (REACH3-ALL)
   and R124 (ENDGAME-3): N5′-xi from S3 makes polynomially many iterations on the games Γ3(G), G an R104 genome. Box 208 (IDEAL-CYC on
   Γ(G)) is not a link of that chain; it is the model form of box 209's argument (R125's DEAD RUN-TRANSFER separates the two runs).
2. **What that is in TARGET.md's terms (§2).** A bound for one candidate (N5′-xi, not N5) on one restricted family of games. Not M4
   (TARGET.md §2, §4 first bullet). For the GAPS row G-N5-TIME, whose claim is about N5, nothing follows.
3. **The link «Γ3(G) → every parity game» is not merely missing: for N5′-xi it fails (§3-§6; CANDIDATE KILL).**
   - Lemma WRAP (PROVED, lane; §3): for EVERY parity game H and every positional Even strategy s0 there is a parity game W(H, s0) with
     n + 7·m_E + 6·m_O + n_O + 9 vertices on which N5′-xi from S3 is, at H's Even vertices, a Howard (VJ switch-best) run of H from s0
     until its first fallback, and stops exactly 3 iterations after that run ends. N5′-xi is at least as slow as Howard's rule.
   - Lemma FREE-REACH (PROVED, lane; §4), the same fact in the fleet's genome shape: the landed proofs behind REACH3-ALL and ENDGAME-3
     never use R104's clause that every e-vertex is even and above every β (E-DOM); they hold verbatim on Γ3-shaped games whose β- and
     e-vertices carry ARBITRARY distinct priorities between K1 and c_W (FREE genomes).
   - DATA (§5). H = Friedmann's game for Howard's rule, in two published forms: the journal paper's G_n with its initial strategy
     (arXiv 1106.0778v2, §6.2; rows n = 1, …, 6 at this freeze) and PGSolver's switchallexp_n (n = 2, …, 6; F_n to n = 8). N5′-xi from S3 makes exactly T(H) + 3
     iterations on W(H): 11, 29, 65, 137, 281, 569 on the first at n = 1, …, 6 (T = 9·2^n − 10) and 33, 73, 153, 313, 633 on the second at n = 2, …, 6, one fallback
     each; the same counts, and 1,246, 2,489 at n = 7, 8, on F_n, the
     free Γ3-shaped game of L-RED 54's compiled switchallexp_n with the ORIGINAL priority order. The runs are Howard's runs by H's
     own valuation; two implementations agree and the outputs are correct (W_n: n ≤ 4; W^L_n: n ≤ 4; F_n: n ≤ 5; the larger rows are
     the long runs of Addendum A, not in this commit). With R104's E-DOM priorities the same compiled
     genomes take 17, 19, 21, 23, 25 (n ≤ 6). N5 itself takes 3 to 7 iterations on these games.
   - So N5′-xi's iteration count is exponential wherever Howard's is: Statement XI-EXP (§6), CONDITIONAL on WRAP being refereed and
     on one tie-rule item, with a published theorem (Friedmann, arXiv 1106.0778v2, Theorem 6.14: at least 2^n steps) as its third
     premise. If it stands there is NO chain «box 209 + landed X, Y, Z ⇒ N5′-xi polynomial on all parity games»; the map records
     «N5′-xi is not an M4 candidate» (Lead rulings 14:36Z (c) and 15:19Z). Boxes 208 / 209 stay what their scope lines say: statements
     about R104's genomes, which do not extend to general games for N5′-xi.
4. **Why (§7, the W-FLAT principle; PROVED lane as a corollary of §3-§4).** On these games Odd's τ never moves and ties every option
   of every choosing Even vertex in S4a's arena. The two-sided step is inert there, and N5 with ANY S4a tie rule R is the one-sided
   improvement rule «each vertex takes R's pick among its current and its strictly better options» on the inner game. For R =
   Ξσ-best that is Howard's rule. E-DOM is a restriction on the INPUT family (it kept Friedmann's game out of the genome games: L-RED
   R217 §7; L-LIT T66 / T67), not a property the algorithm enforces.
5. **What is left for G-N5-TIME (N5 itself; §8).** N5 is not hit by these families (on W(H) its key rule is a static index rule).
   Every link from Chain A to «N5 polynomial on all parity games» is OPEN, and none is supplied by boxes 208 / 209: O1 (the key-rule
   run on R104 genomes: the tower question), O2 (NEW: the key-rule run on FREE genomes, a strictly larger adversary class that no
   lane has attacked), O3 (everything off the Γ3 shape: R90's B*, REP*, SC*, O*), O4 (gauntlet items). §9 gives the recommendation.

## 1. Chain A: what boxes 208 + 209 would give, link by link
Objects (landed): the genome G, Γ(G) (R104), Γ3(G) with n3 = N + 7M + 10 (R117), IDEAL-CYC(G) and T_CYC (R118 (a)), HOW3(G) and T3 (R125),
N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md), N5′-xi = SPEC with box 190's S4a′.
- [Q] N5′-xi (claude/l-new docs/new/N5XI-GAUNTLET-box190.md §1): SPEC «with ONE rule changed, inserted after S4a:» the tie among the
  arena-optimal options of an Even vertex is broken by the best Ξσ value. [Q] «Not claimed: that σ_new is still a pointwise optimum of H.
  No argument above needs it.»

| link | statement | status | source |
| --- | --- | --- | --- |
| A0 | box 208, IDEAL-CYC on Γ(G): [Q] «For every genome G: T_CYC ≤ P·(N + 2M + 6) + N, P = 2M(N + 2M).» | CANDIDATE (lane; four checks survived, per the Lead; packet P-N5-LEVEL being frozen) | claude/l-new 8db300fe docs/new/N5-LEVEL-box208.md, Addendum A |
| A1 | box 209, the Γ3 / HOW3 form: [Q] «For every genome G: T3 ≤ P3·(n_E3 + 1) + n_E3, with P3 = 2M(N + 4M) and n_E3 = N + 6M + 9.» and its Corollary N5XI-G3: [Q] «For every genome G, N5′-xi from S3 on Γ3(G) makes exactly T3 + 3 ≤ P3·(n_E3 + 1) + n_E3 + 3 iterations.» | CANDIDATE (lane); its scope line: [Q] «Not N5, not another start, not another game, not M4; G-N5-TIME stays OPEN.» | claude/l-new 3f8960998 docs/new/N5-LEVEL3-box209.md §5 |
| A2 | [Q] «N5′-xi from S3 on Γ3(G) visits only standard states and its mover parts form a run of HOW3(G) until its first fallback, at iteration T3 + 1» | LANDED, every genome | R125 (REACH3-ALL) |
| A3 | [Q] «N5′-xi, and N5, from S3 on Γ3(G) have exactly one fallback, at an iteration F ≥ 1, and exactly F + 2 iterations» | LANDED, every genome | R124 (ENDGAME-3, ENDGAME-3-N5) |
| A4 | [Q] «if REACH3-CYC holds for G, N5′-xi from S3 on Γ3(G) makes exactly T3 + 3 iterations»; R125: REACH3-CYC [Q] «holds without its condition, the premises ESC3 and W3 being proved here for every genome» | LANDED (two lines, one modus ponens) | R124 (END-T3) + R125 |
| A5 | one iteration of N5′-xi costs O(n³(n + m)) word operations at bit cost | PROVED lane (box 190 §3, from R57 (c) for N5: [Q] «iteration and the final output step cost O(n³(n + m)) word operations on O(log(n + m))-bit words and O(n)-bit vectors on every»), unrefereed | claude/l-new box 190 §3 |
| A6 | N5′-xi terminates and its S5 output is correct on every game | PROVED lane (box 190 §2, from R15 (d) and R57 (b) OUT-G: [Q] «Iτ = ∅ is not used; determinacy is derived, not assumed (W_E ∩ W_O = ∅ is proved).»), unrefereed, no Lean | claude/l-new box 190 §2 |

- Conclusion of Chain A (conditional on A1): for every R104 genome G, N5′-xi from S3 on Γ3(G) makes T3 + 3 ≤ poly(n3) iterations. With
  A5 and A6 refereed it would read: «N5′-xi solves the games {Γ3(G)} in polynomial time». Box 209's Corollary N5XI-G3 is A1 + A2 + A4.
- The genome-only premise of A1, named in box 209 §1 itself: E-DOM on Γ3, [Q] «the added vertices are pads of priority ≤ 2 (R117's line
  above), below every e-vertex. Call this (E-DOM3).» It enters at (K2′) (COARSE), on which (K1′), (K4′), (K5′) and both lemmas rest.
- Where box 208 sits: [Q] R125 (DEAD RUN-TRANSFER) «T3 is not the IDEAL-CYC count on Γ(G)»; box 208's own line [Q] «IDEAL-CYC on Γ(G)
  only; not Γ3, not N5′-xi, not M4; G-N5-TIME stays OPEN.» So A0 feeds A1 only as a proof template.
- What the landed lines already say about the reach of this chain:
  - [Q] R118: «no bound on R is claimed (OPEN), so nothing about N5′-xi's or N5's running time follows»; (l): [Q] «N5′-xi's FL run on
    Γ3(G) is polynomial in N + M for every genome» ⇔ «R is polynomial along these Howard runs». A1 would be that bound on R.
  - [Q] R124: «it bounds none of F, T3, L(G) (OPEN), and nothing outside Γ3(G)».
  - [Q] R125: it «says nothing about N5 (whose pre-fallback run on Ξ-cyclic genomes is not a Howard run), about genomes with U(G)
    unbounded (Σ_v D^tot_E(v) stays OPEN), about other games or about general parity games».

## 2. Chain A against TARGET.md and against the GAPS row
- [Q] TARGET.md §2 (M4): «There is a deterministic algorithm A and a polynomial p such that for every parity game G, A on input G halts
  within» p(n + m) steps. [Q] §4, what does not count: «Polynomial only on a restricted class (bounded d, treewidth, Strahler/register
  number, ...).» and [Q] «Correctness or running time resting on an unproved conjecture, an empirical observation, or a "clearly".»
  [Q] §5.4: a claim presented as M4 also needs «its correctness formalized in Lean against TARGET.md (no sorry, allowed axioms only).»
- [Q] GAPS l. 11 (G-N5-TIME), the claim: «N5 SSI-GLOBAL makes polynomially many iterations (gauntlet step 4, running time)». [Q] NOW, M4
  row: «candidate N5 SSI-GLOBAL; gauntlet step 4 (running time, G-N5-TIME) OPEN; termination proved (R15)».
- The links between Chain A's conclusion and M4. Each is a statement that Chain A does not contain.

| id | missing link | status | where |
| --- | --- | --- | --- |
| L1 | ALGORITHM. The row's candidate is N5; Chain A is about N5′-xi. For N5 on Γ3(G): [Q] P-N5-CHAIN §3 Remark «For SPEC's S4a the same induction gives standard states, but SPEC picks in TIE(x) = A(x) by its root-first key, not by Ξσ:» not a Howard step. Boxes 208 / 209 bound Howard's count, so they bound nothing for N5 | OPEN for N5 (§8, O1, O2) | R125's line (quoted in §1); R124 EXACT-L |
| L2 | BEYOND THE FIRST FALLBACK. On Γ3(G): landed (A3). On other games: nothing landed for N5′-xi; for N5 the landed fallback counts are reductions (§8, O3) | LANDED on Γ3(G) only | R124 |
| L3 | FROM Γ3(G) TO EVERY PARITY GAME. No landed statement goes this way: [Q] R104 «a REDUCTION / NECESSITY statement only (no count is bounded; Ξ-cyclic genomes are not covered; nothing about N5's default start S3; the converse is not claimed»; [Q] R117 «a REDUCTION / NECESSITY statement only (no count is bounded; nothing is claimed about whether long IDEAL-ACYC runs exist; Ξ-cyclic genomes are not covered; the converse is not claimed»; [Q] R118, referee note (iv): «so RED-XI says nothing about general games without TIE-FULL» | for N5′-xi: FAILS by Lemma WRAP + Friedmann's family (§3-§6; CANDIDATE KILL). For N5: OPEN (§8) | §3-§6 |
| L4 | COST per iteration at bit cost for N5′-xi (A5) | lane proof to referee | box 190 §3 |
| L5 | CORRECTNESS of N5′-xi on every game (A6), then Lean (TARGET.md §5.4, §6) | lane proof to referee; no Lean | box 190 §2 |
| L6 | GAUNTLET steps 1-3 and 5 for the candidate (TARGET.md §5); box 190 §6 lists what is missing | not done | box 190 §6 |

- L3 decides. L1, L2 and L4-L6 are work items on a chain that L3 cuts.

## 3. Lemma WRAP: every parity game inside a W-flat wrapper (PROVED, lane; a new construction with its own proof, to be refereed)
**Definition (the wrapper W(H, s0)).** Let H = (V, V_E, V_O, E, pr) be any parity game (TARGET.md §1), n := |V|, m_E / m_O the numbers
of edges leaving Even / Odd vertices, n_O := |V_O|, and s0 a positional Even strategy of H. W := W(H, s0) (wrap104.py) consists of:
- the vertices of H with their owners and indices, and Ω(v) := pr(v) + 6;
- for every edge (v, w) with v ∈ V_E: a pad m_(v,w) (Ω 2 if w = s0(v), else 0), an Odd GATE g_(v,w) (Ω 1), pads pe_(v,w) (Ω 1) and
  pβ_(v,w) (Ω 0), with the edges v → m → g, g → pe → c_W and g → pβ → b_(v,w);
- for every edge (o, w) with o ∈ V_O: pads x1, x2, x3 (Ω 0), with the edges o → x1 → x2 → x3 → b_(o,w);
- for every edge (a, w) of H: a VALVE b_(a,w) (Even, Ω 0) and pads y_(a,w) (Ω 2), pb_(a,w) (Ω 1), with the edges b → y → w and
  b → pb → K0;
- for every o ∈ V_O: a pad pe_o (Ω 1), with the edges o → pe_o → c_W;
- c_W (Even, a self-loop, Ω top := the least even number ≥ max Ω(V) + 2), and R117's core with its pads: K0 (Even, top + 2) → {K1, pA},
  pA → K3, K1 (Even, 5) → {q, s}, s → K1, q → K0, K2 (Odd, 3) → {r, K2}, r → K1, K3 (Even, top + 3) → {K1, K2}; pA, s, r have Ω 0, q
  has Ω 1.
Every pad is an Even vertex with one successor; the new vertices are indexed after V. Every vertex has a successor, so W is a parity
game; |W| = n + 7·m_E + 6·m_O + n_O + 9. Every edge a → w of H has become a path of exactly 6 edges from a to w whose inner vertices
have Ω ≤ 2. Γ3(G) is not a W(H, s0), but it is built from the same parts: gates with a τ-face to c_W, valves (its β-vertices) with an
exit to the core, R117's core and pads. W has no levels: every gate's τ-face goes to c_W at once.
- (R_W) Rank order: pads, gates, valves (Ω ≤ 2) < K2 (3) < K1 (5) < every vertex of H (≥ 6) < c_W (top) < K0 < K3. The vertices of H
  are ranked among themselves as in H (same order of priorities, same indices).
- STANDARD STATE of a positional Even strategy s of H: σ(v) = m_(v,s(v)) for v ∈ V_E; σ(b) = y at every valve; σ(K0) = pA, σ(K1) = s,
  σ(K3) = K2; τ0: τ(g) = pe at every gate, τ(o) = pe_o at every o ∈ V_O, τ(K2) = K2. Its H-PART is s.
- HOWARD on H: Ω^H_s := SPEC S1's values of H under s and Odd's optimal counterstrategy. A Howard step moves every v ∈ V_E to a
  ⊴-best successor and keeps s(v) if it is one (ties among best successors by any rule: the definition of R118 (a) / R125's HOW3). A
  Howard run from s0 ends at the first state T at which no Even vertex has a strictly better successor.

**Lemma WRAP.** For every parity game H and every positional Even strategy s0 of H, under the standing SPEC premise 1E-N3 (R57 (b), as
in R104 / R117 / R124 / R125: S1's σ̄ and τ̄ are pointwise optima, and S4a's σ_new is a pointwise optimum of its arena):
- (i) S3's pair on W(H, s0) is the standard state of s0.
- (ii) At every state of the N5′-xi run (and of the N5 run) from S3: τ = τ0 and Iτ = ∅.
- (iii) The N5′-xi run from S3 visits only standard states until its first fallback, the H-parts of these states form a Howard run
  of H from s0 (tie rule: Ξσ-best, then SPEC's choice, then the larger index), and the first fallback is at iteration T + 1, T the
  length of that Howard run.
- (iv) The N5′-xi run has exactly one fallback and exactly T + 3 iterations.
- (v) The N5 run from S3 has exactly one fallback, at an iteration F ≥ 1, and exactly F + 2 iterations; before F its states are
  standard and each v ∈ V_E picks, by SPEC's tie rule, inside A(v) = {its current pad} ∪ {the pads of its strictly ⊴_H-better successors}.
**Proof.** The proofs of P-N5-REACH §4-§6, P-N5-CHAIN §3 and P-N5-END §3-§6 are the template; (W4) is the one new step.
- (W1) [PAD]. A new vertex outside the core lies on a path that ends, without a branch back, in c_W, in K0 or in a vertex of H. So
  every cycle of W is c_W's loop, lies in the core (then it contains K0, K1 or K3, or is K2's loop), or contains a vertex of H: it
  has a vertex of Ω ≥ 3. Hence no pad, gate or valve is ever a cycle node or in a P-set (they rank below every such vertex).
- (W2) [S3-START], by SPEC S3 / FIX 1 at the vertices with two or more successors. v ∈ V_E: its successors are its pads m, all even;
  the highest is the Ω-2 pad of s0(v). A valve: y (Ω 2, even) and pb (Ω 1, odd): y. An Odd gate: pe (Ω 1, odd) and pβ (Ω 0, even): the
  highest odd, pe. o ∈ V_O: its pads x1 (Ω 0, even) and pe_o (Ω 1, odd): pe_o. The core: as P-N5-REACH §4 (K0 → pA, K1 → s, K3 → K2,
  K2 → K2). This is (i).
- (W3) [core]. P-N5-REACH §6.1 K3 (a)-(d) and R118's Lemma K2-r (σ̄(K2) = r in every standard state) hold verbatim: the core, its pads
  and their priorities are R117's, and the core is entered from outside only by pb → K0.
- (W4) [Odd's reply and the values; new]. Let (σ, τ0) be the standard state of s. Then: (a) σ̄(g) = pβ at every gate and σ̄(o) ≠ pe_o
  at every o ∈ V_O; (b) for v ∈ V, Ξσ(v) = (c, P, 6ℓ) where (c, P, ℓ) = Ω^H_s(v); (c) Ξσ(m_(v,w)) = (c, P, 6ℓ + 5) where (c, P, ℓ) =
  Ω^H_s(w); (d) so for v ∈ V_E: (v, m_(v,w)) ∈ Iσ iff Ω^H_s(w) ▷ Ω^H_s(s(v)), and Ξσ orders the pads of v as Ω^H_s orders its successors.
  Proof. Call an Odd strategy of W pe-FREE if it takes no pe at a gate or at a vertex of V_O (it exists: a gate has pβ, and every
  o ∈ V_O has a successor in H, hence a pad x1). Under σ a pe-free play from a vertex outside the core runs along the 6-edge paths
  from vertex of H to vertex of H forever (every valve goes to y), so it never meets c_W or the core, and its cycle node is a vertex
  of H (W1), of rank below c_W. A play that takes a pe ends in c_W's loop, whose reward p′(c_W) > 0 is larger than the reward of
  every vertex of H. If σ̄ took pe at an Odd vertex u, Ξσ(u) would have node c_W, while a pe-free strategy gives u a value with a
  node in H, strictly ◁-smaller: against the pointwise optimality of σ̄ (1E-N3). This is (a). The pe-free Odd strategies of W
  correspond one to one to the positional Odd strategies ρ of H (o ↦ w iff o → x1_(o,w)). Under σ and a pe-free strategy the play
  from v ∈ V is the (s, ρ)-play of H with every edge stretched to 6 edges through vertices that are in no P-set (W1), so its value
  is (c, P, 6ℓ) for the H-value (c, P, ℓ). The map (c, P, ℓ) ↦ (c, P, 6ℓ) is strictly order-preserving for SPEC S1's order (same
  reward, same P, lengths multiplied by 6), and the ranks of H's vertices are ordered in W as in H. σ̄ is pe-free and minimises at
  every vertex over all Odd strategies, so its ρ minimises at every vertex of H: it is an optimal counterstrategy of s in H, and (b)
  follows (the pointwise minimum is unique as a value). (c): the play from m_(v,w) is m → g → pβ → b → y → w followed by w's play,
  five more steps, no new P-element. (d): SPEC S2 compares Ξσ at the successors of v, which are its pads, and (c, P, ℓ) ↦
  (c, P, 6ℓ + 5) is strictly order-preserving. ∎
- (W5) [TAU]. Iτ depends on τ alone. Under τ0 every gate and every o ∈ V_O plays pe, so Ξτ(pe) has reward p′(c_W) whatever Even does.
  From pβ_g, or from a pad x1 of o, Even may play on to the valve and b → pb → K0 → K1 → q → K0 …, a cycle with node K0 (Ω top + 2,
  above c_W); τ̄ maximises, so these options have reward ≥ p′(K0) > p′(c_W): worse for Odd. K2: K3 (c). So Iτ = ∅ whenever τ = τ0;
  S4b changes τ only if Iτ ≠ ∅ and S4c changes τ only if Iσ = ∅ and then along Iτ. With (W2) this is (ii) (P-N5-END §3, E0).
- (W6) [ESC, W-flat]. In a standard state: Iσ ∋ (K0, K1) (K3 (b)). In S4a's arena (Even keeps A(·) = {σ(·)} ∪ Iσ(·), Odd follows
  τ0): every option of v ∈ V_E is a pad m → g → pe → c_W, so W*(m) = (c_W, ∅, 3) for EVERY m ∈ A(v), W*(v) = (c_W, ∅, 4), v is on no
  arena cycle, and TIE(v) = A(v). A valve b has A(b) ⊆ {y, pb}; the arena play via y → w ends in c_W's loop (w ∈ V_E: a pad, its
  gate, pe; w ∈ V_O: pe_w), the arena play via pb → K0 ends in an odd core cycle (K3 (d)): REWARD, y is strictly better; b is on no
  arena cycle (its in-edges come from pβ_g, whose gate plays pe, or from x3, whose o plays pe_o); so every pointwise optimum keeps y
  and TIE(b) = {y}. The core: K3 (d), TIE(K0) = {pA}. Every other Even vertex has one successor.
- (W7) [REACH]. Induction on j: state j is standard. j = 0: (W2). Let j < T. τ_new = τ by (W5) (S4c would act on Iτ only if Iσ = ∅).
  Off V_E, σ_new = σ by (W6), for SPEC's pointwise optimum and for N5′-xi's rule. At v ∈ V_E with |A(v)| ≥ 2, TIE(v) = A(v) (W6) and
  N5′-xi takes the Ξσ-best element of A(v); A(v) holds every pad that is strictly better than σ(v), so by (W4) (d) this is the pad of
  a ⊴-best successor of v in H: a Howard step of H; where A(v) = {σ(v)} the vertex stays. Some v moves, so S4c does not fire and
  state j + 1 is standard. At state T every A(v) is {σ(v)} ((W4) (d)), so σ_new = σ and τ_new = τ while Iσ ∋ (K0, K1): S4c fires at
  iteration T + 1. This is (iii). For N5 the same induction gives standard states until its first fallback, with SPEC's pick in
  TIE(v) = A(v): the first half of (v).
- (W8) [ENDGAME]. P-N5-END's E1-E4 hold with «valve b» for «β_g», «y» for «xt(g)» and, for its fact (W), «from a gate or a vertex
  of V_O the τ0-play is pe → c_W, value (c_W, ∅, 2)». E1, E2, E3 are statements about the core (K-configs κ0 → κ1 → κ2), proved from
  K3 and (H) alone; the fallback of E2 may also move valves, which E3 and E4 allow («any σ at movers and β's»). E4 (a): at κ2 the
  value of pb is (K0, ∅, 1) and the value of y is at most that of the pe-play (node c_W), so (b, pb) ∈ Iσ wherever σ(b) = y, and in
  the arena pb has node K0 against node c_W via y: σ*(b) = pb at every valve, σ*(K3) = K1. E4 (b): at σ* every play that leaves pe at
  a gate or at o ∈ V_O reaches a valve, hence K0's cycle, a larger reward than c_W's; so Odd's optimal reply is pe everywhere, every
  pad m has the value (c_W, ∅, 3), no v ∈ V_E has an improving edge, and neither has a valve (node c_W via y against node K0 at pb)
  or the core: Iσ* = ∅, and Iτ = ∅ by (W5). So there is exactly one fallback, at F = T + 1 for N5′-xi, and F + 2 iterations: (iv),
  and the second half of (v). ∎
- Remarks. (1) WRAP uses no property of H: any owners, priorities, degrees, self-loops. (2) W(H, s0) is solved by Even from every
  vertex but K2 (the valves reach the core, which Even wins once K0 → K1 → q → K0 is closed); the wrapper tests the run, not the
  winner. (3) For N5, (v) with (W6) gives more: the root-first key of a pad m_(v,w) is the index sequence (pe, g, m) of its 3-step
  arena play, the same at every state (R104's premise [RULE]: SPEC picks the key-least option), so before its first fallback each
  v ∈ V_E only ever moves to a pad of smaller key: at most m_E − |V_E| mover steps, F ≤ m_E − |V_E| + 1. So N5 is polynomial on every
  W(H, s0) (lane; not counted by a tool beyond the F column of §5; not a statement about N5 on any other game).
- DATA for WRAP (wrap104.py; scope: the run from S3 on W(H, s0); out/wrap_rand.out). Must-0 counters: s3fail (unit games: S3's pair
  is not the standard state of s0), nonstd (unit states before the first fallback), nohoward (unit (step, Even vertex of H) pairs
  before the first fallback: the new successor is not a ⊴-best successor BY H'S OWN VALUATION, computed by si.Engine on H itself, or
  a best current successor was left), fbwrong (unit games: the first fallback is not at T + 1), endwrong (unit games: fallbacks ≠ 1
  or iterations ≠ T + 3; for N5: ≠ F + 2), wrong (unit games: regions of W ≠ harness Zielonka on W).
  - N5′-xi, seed 1043, 3,000 random games H (harness gen.random_game, 2 ≤ n ≤ 12, a random s0): «s3fail 0 nonstd 0 nohoward 0 fbwrong 0 endwrong 0 wrong 0 | max T 7 sum T 3618 max |W| 284».
  - N5′-xi, seed 1044, 1,000 random games, n ≤ 24: «s3fail 0 nonstd 0 nohoward 0 fbwrong 0 endwrong 0 wrong 0 | max T 7 sum T 1850 max |W| 511».
  - N5 (ALG=spec), seed 1043, 3,000 games: «s3fail 0 nonstd 0 nohoward 0 fbwrong 0 endwrong 0 wrong 0 | max F 4 sum F 4813 max |W| 284» (nohoward, fbwrong not tested in this mode).
  - Controls (out/wrap_ctrl.out, 100 games each): CTRL=1 (best := worst) fires, nohoward 405; CTRL=2 (T shifted by one) fires, fbwrong 100 and
    endwrong 100. s3fail, nonstd and
    wrong have no control.

## 4. FREE genomes and Lemma FREE-REACH: the same fact in the genome shape (PROVED, lane; a reading of landed proofs, to be refereed)
WRAP leaves the genome format. This section stays inside it and changes one clause, to show what separates box 209 from §3.
**Definition (FREE genome).** G* = (G, π): G has the data of an R104 genome without its β-ranks and parities (N movers with levels; M
options q = (x, k), each with a W-target of level lev(x) − 1 (none at level 0), a Ξ-target (a mover or X), a distinct gate index; a
start), and π is an injective map from the 2M CARRIERS β_q, e_q into the integers ≥ 6, of either parity. Γ3*(G*) is R117's Γ3 (same
vertices, indices, owners, edges and pads) with Ω(β_q) := π(β_q), Ω(e_q) := π(e_q), top := the least even number ≥ max π + 2, Ω(c_W) :=
top, Ω(K0) := top + 2, Ω(K3) := top + 3; movers 0, gates 1, c_X 2, K2 3, K1 5 and the pad priorities are R117's. Standard states,
HOW3*(G*) and T3* are defined as in R125, on Γ3*(G*).
- The R104 genomes are the free genomes with π(β_q) = 6 + 2·rank + parity and every π(e) even and above every π(β) ([Q] R104 [DEF]: «e of
  even priority above every β with one edge to the W-target or to the top even self-loop c_W»), the e's in (lev, gate) order.
- (R*) Rank order of Γ3*: pads, movers, gates, c_X (Ω ≤ 2) < K2 (3) < K1 (5) < every β and every e (≥ 6) < c_W (top) < K0 < K3. The
  landed order is [Q] P-N5-CHAIN §2 «(R) Rank order, by Ω first: pads, movers, gates, c_X (Ω ≤ 2) < K2 (3) < K1 (5) < every β (≥ 6) <
  every e < c_W (top) < K0 (top + 2)» (< K3), and [Q] P-N5-REACH §6 «Rank facts (from [DEF] and §3): pads, movers, gates, c_X < K2 (Ω 3)
  < K1 (Ω 5) < every β < every e < c_W < K0 < K3.» (R*) is (R) without the clause «every β < every e» and without the parity of e.
- Γ3*(G*) is a parity game in TARGET.md §1's sense: every vertex has a successor; N5 and N5′-xi read only the order and the parity of
  the priorities (SPEC S1's ranks), so TARGET.md §1's compression to {0..n} applies. In F_n (§4) the largest priority, top + 3, is
  below |V| as built (out/prio.out, out/free_xi.out «maxprio»). The same holds for W(H, s0).

**Lemma FREE-REACH.** For every free genome G*, under the standing SPEC premise 1E-N3 as in R104 / R117 / R124 / R125:
- (a) S3's pair on Γ3*(G*) is the standard state of the genome start.
- (b) At every state with τ = τ0 (pe at every gate, K2 → K2): Iτ = ∅.
- (c) N5′-xi from S3 visits only standard states, and its mover parts form a run of HOW3*(G*) (tie rule: Ξσ-best, then SPEC's
  choice, then the larger index) until its first fallback, at iteration T3* + 1.
- (d) N5′-xi from S3 has exactly one fallback and makes exactly T3* + 3 iterations.
- (e) N5 from S3 has exactly one fallback, at an iteration F* ≥ 1, makes exactly F* + 2 iterations, visits only standard states before
  F*, and at each step before F* every mover x has TIE(x) = A(x) = {current} ∪ {strictly Ξσ-better}, in which SPEC picks by its own
  tie rule (R104's premise [RULE]: the root-first key).
Proof: the landed proofs, read with (R*) in place of (R). The table lists every step of those proofs that cites the rank order or a
priority, and what it uses. No step uses «every β < every e», the parity of a β or of an e, the order of the e's among themselves, or
[E-LEV].

| landed proof | what it uses of the priorities | holds under (R*) because |
| --- | --- | --- |
| P-N5-REACH §4 S3-START | Ω of pads, movers, K0-K3 only (FIX 1 at the vertices with ≥ 2 successors: movers, β with a mover target, K0, K1, K3, gates, K2) | unchanged vertices |
| P-N5-REACH §5 PAD (a) | a cycle through a mover passes pe_g → e_g or pβ_g → β_g [Q] «with Ω(e_g), Ω(β_g) ≥ 6» | π ≥ 6 |
| P-N5-REACH §6.1 K3 (a)-(d); R118's Lemma K2-r | core vertices only: K0, K3 above K1; reward of K1 below K2's | unchanged vertices |
| P-N5-REACH §6.4 TAU3 | under τ every play from pe_g ends in c_W's loop; from pβ_g Even reaches [Q] «node K0 (Ω top + 2, above c_W); τ̄ maximises (Fact DUAL)» | c_W < K0 |
| P-N5-CHAIN §3 ESC3-ALL | H-plays from xt(g) end in c_W's loop (even node); H-plays from pb_g end in an odd core cycle (K1 or K2): REWARD | c_W even, K1 and K2 odd |
| P-N5-CHAIN §3 W3-ALL | the τ-play from a mover runs through movers, pads, gates and e's, [Q] «all less relevant than c_W ((R)): P = ∅.» | every e < c_W |
| P-N5-CHAIN §3 REACH3-ALL | induction on S3-START, TAU3, ESC3-ALL, W3-ALL; [N5XI]'s rule | no priority used |
| P-N5-END §2 (R), (W), (H) | [Q] «K0 is the most relevant EVEN vertex, so a value with» cycle node K0 has the largest reward; (W): the pe-play [Q] «It meets no β and no core vertex, and no vertex above c_W: its value is (c_W, ∅, 5ℓ + 3).» | every carrier < c_W < K0 |
| P-N5-END §3-§5 E0-E4, §6 ENDGAME-3 (and -N5) | core values; node K0 against node c_W, K1, K2 (REWARD); lengths on the pe-play | as above |

- (a) is S3-START; (b) is TAU3 with E0; (c) is REACH3-ALL; (d) is ENDGAME-3 with (c); (e) is ENDGAME-3-N5 with the Remark quoted in L1. ∎
- Difference from WRAP: here an Odd choice is a gate whose e-face is part of the inner game (it leads one level down), so the inner
  games are those of the genome shape; in W(H, s0) the inner game is H itself.
- What is NOT claimed for free genomes, because its landed proof does use E-DOM ([Q] R121: «Every vertex more relevant than some
  e-vertex is an e-vertex, c_W, K0 or K3, by [DEF]»): E-MON / E-MON3, B-ONLY(3), NO-TIE(3), QUIET(3), CHAIN3, every statement of boxes
  208 / 209 ((K2)-(K5), LEVEL, PLATEAU, ALL-TCYC; (K2′)-(K5′), LEVEL3, PLATEAU3, T3-ALL) and of this lane's boxes 99-103 that rests on
  them. LOC-GATE3 was not re-read for (R*).
- DATA for (a)-(e) (freereach104.py; scope: N5′-xi resp. N5 from S3 on Γ3*(G*), own generator: 1 to DMAX levels, 1 to WMAX movers per
  level, 1 to DEGMAX options, Ξ-target X with probability 0.15, π a random permutation of 6, …, 5 + 2M; out/freereach.out). Must-0
  counters: s3fail (unit genomes: S3's pair is not the standard state), nonstd (unit states before the first fallback), nohoward (unit
  (step, mover) pairs: the mover's new choice is not a ⊴-best successor, or it left a best current one), fbwrong (unit genomes: the
  first fallback is not at T3* + 1), endwrong (unit genomes: fallbacks ≠ 1 or iterations ≠ T3* + 3; for N5: ≠ F* + 2), wrong (unit
  genomes: regions ≠ harness Zielonka).
  - N5′-xi, seed 1041, 2,000 genomes (d ≤ 4, w ≤ 3, deg ≤ 3): «s3fail 0 nonstd 0 nohoward 0 fbwrong 0 endwrong 0 wrong 0 | max T3 9 sum T3 3159 max |V| 225 edomok 0».
  - N5′-xi, seed 1042, 1,000 genomes (d ≤ 6, w ≤ 4, deg ≤ 3): «s3fail 0 nonstd 0 nohoward 0 fbwrong 0 endwrong 0 wrong 0 | max T3 9 sum T3 2326 max |V| 368 edomok 0».
  - N5 (ALG=spec), seed 1041, 2,000 genomes: «s3fail 0 nonstd 0 nohoward 0 fbwrong 0 endwrong 0 wrong 0 | max F 5 sum F 3519 max |V| 225 edomok 0» (nohoward and fbwrong are not tested in this mode).
  - Controls (out/freereach_ctrl.out, 100 genomes each): CTRL=1 (Howard test against the worst successor) fires, nohoward 678; CTRL=2
    (T3 shifted by one) fires, fbwrong 100 and endwrong 100. s3fail, nonstd and wrong have no control.
  - None of these random genomes satisfies E-DOM (edomok 0), so the data is on free genomes proper. The runs are short (max T3* 9):
    they test the equivalence, not any length.

## 5. Friedmann's counter inside both shapes (DATA; CANDIDATE KILL of N5′-xi on general parity games)
### 5.1 The games
- G_n := PGSolver's switchallexp_n (trunk experiments/hard-families/pgsolver_port.py), Friedmann's lower-bound family for the
  switch-all / locally optimizing rule; |G_n| = 14n + 7. s_n := its best-reward start. T(G_n) := the number of Howard (VJ switch-best)
  iterations on G_n from s_n, as computed by L-RED 54's fried.howard on si.py's Engine. [Q] R118's line records the same counts: «on
  Friedmann's switchallexp for N = 2, …, 7 (pgsolver_port.py switchallexp N, Howard from si.py's best-reward start): C = 0; R = 4, 10,
  24, 54, 116, 241; T = 30, 70, 150, 310, 630, 1243».
- W_n := W(G_n, s_n) of §3 (wrap104.py); |V(W_n)| = 251n + 65.
- G^L_n := the game G_n of Friedmann's journal paper [F11] (arXiv 1106.0778v2, §6.2) with its initial strategy ι. Graph, owners
  and ι: Table 4 and the four lines after Fact 6.1, in L-LIT's transcription (claude/l-lit 5c53efbd docs/lit/T66-depth-check.py,
  function lmcs, used unmodified); read here against the opened PDF, every row (node, player, successors) and ι agree. Priorities,
  two versions (L-LIT T66 Addendum D, claude/l-lit 9ae31ec3; checked here against the PDF's Table 4 and Fact 6.1):
  - «fig4», the one used for XI-EXP: the INJECTIVE priorities of the paper's Figure 4, d_i = 4i − 1, e_i = 4i, g_i = 4i + 2, k_i =
    8n + 4i + 5, f_i = 8n + 4i + 7, h_i = 8n + 4i + 8, the others as in Table 4. They agree with the paper's §2 («W.l.o.g. we assume
    Ω to be injective») and with Fact 6.1's «12 · n + 8 as highest priority»; wrap104.py asserts both.
  - «table4»: Table 4 as printed, whose six formulas for d, e, g, k, f, h are 2 higher; then pr(g_n) = pr(a_1) = 4n + 4 and the top
    is 12n + 10 (a misprint, per L-LIT). SPEC S1 breaks the tie by index, so it is still a parity game; every count below is the
    same in both versions.
  The node and edge counts equal Fact 6.1's «10 · n + 4 nodes, 1.5 · n2 + 20.5 · n + 5 edges» on every row (out/wrap_lmcs_xi.out,
  «Fact 6.1 (nodes, edges) True»). W^L_n := W(G^L_n, ι), with |V(W^L_n)| = 211, 395, 600, 826, 1,073, 1,341 at n = 1, …, 6.
- F_n, the genome-shaped form. comp(G_n) := L-RED 54's compilation of G_n into a d-2 genome (claude/l-red 8c01d40e
  experiments/red/r217/comp.py, unmodified): a level-0 helper per vertex carrying its priority on a β; Even choice vertices become
  movers; the Odd CycleCenters h_i become gates whose β-face returns into the cycle and whose e-face is the CycleLeaver m_i. L-RED
  built it with R104's priorities and found: [Q] «Steps 1-6 coincide exactly with the original run at every mover. So the compilation
  is faithful until step 7.», the cause of the divergence being [Q] «Obstruction E-DOM (structural fact of R104's Γ(G); P-N5-XICYC
  [DEF], gamma3.build).», and concluded that the counter [Q] «can reach N5′-xi only through the Howard-equivalence on Γ3 genomes
  (REACH3-CYC), and E-DOM blocks the direct port there.» F_n := Γ3*(comp(G_n), π_n) (free104.py): π_n ranks the 2M carriers in ONE
  common order by the original priority each carries (a β by its comp.py key; the e of a CycleCenter gate or of its copy gate by
  pr(m_i), with pr(m_i)'s parity; every other e, which Odd never takes, lowest and even) and gives them the priorities 6, 7, … in
  that order, skipping one where the parity requires it. Nothing else of comp.py or gamma3.build is changed: F_n differs from the
  genome game Γ3(comp(G_n)) of R217 §7 in priorities only. |V(F_n)| = N + 7M + 10 = 309n + 90 (N = 22n + 10, M = 41n + 10).
- F_n is not a genome game: out/prio.out counts 16, 23, 30, 37, 44, 51, 58 odd β-vertices above some e-vertex at n = 2, …, 8 (0 in the E-DOM build). These
  are the odd CycleAccess / UpperSelector priorities above lower CycleLeavers that R217 §7 names.
- Frozen instances (inst/SHA1SUMS): F_2 … F_8 (.pg), W_2 … W_8, WL_1 … WL_4 (W^L_n, Figure 4's priorities) and rand300.json (the first 300 games of seed 1043 with
  their s0, T, iterations and |W|; wrap104.py json replays them, pgjson writes the i-th W); sha1 of each in that file.

### 5.2 DATA (run104.sh, runw104.sh; every row is a run from SPEC's default start S3, which is the standard start on every row)
PGSolver's switchallexp_n («not run»: a row of the long runs, Addendum A):
| n | \|G_n\| | T(G_n): Howard on G_n | \|V(W_n)\| | N5′-xi on W_n: iterations, fallbacks | \|V(F_n)\| | N5′-xi on F_n: iterations, fallbacks | engine 2 on W_n / on F_n: iterations, verdict | F_n state for state: mism | N5′-xi on the E-DOM build of comp(G_n) | N5 (spec) on W_n / F_n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 35 | 30 | 567 | 33, 1 | 708 | 33, 1 | 33, AGREE+CORRECT / 33, AGREE+CORRECT | 0 of 682 | 17 | 3 / 5 |
| 3 | 49 | 70 | 818 | 73, 1 | 1,017 | 73, 1 | 73, AGREE+CORRECT / 73, AGREE+CORRECT | 0 of 2,201 | 19 | 4 / 5 |
| 4 | 63 | 150 | 1,069 | 153, 1 | 1,326 | 153, 1 | 153, AGREE+CORRECT / 153, AGREE+CORRECT | 0 of 6,040 | 21 | 5 / 5 |
| 5 | 77 | 310 | 1,320 | 313, 1 | 1,635 | 313, 1 | not run / 313, AGREE+CORRECT | 0 of 15,239 | 23 | 6 / 5 |
| 6 | 91 | 630 | 1,571 | 633, 1 | 1,944 | 633, 1 | not run / not run | 0 of 36,598 | 25 | 7 / 6 |
| 7 | 105 | 1,243 | 1,822 | not run | 2,253 | 1,246, 1 | not run / not run | not run | not run | not run / not run |
| 8 | 119 | 2,486 | 2,073 | not run | 2,562 | 2,489, 1 | not run / not run | not run | not run | not run / not run |
- Counters and units.
  - iterations, fallbacks on W_n (out/wrap_fried_xi.out, n = 2, …, 6; unit: one run of box190 n5v.py mode xi from S3): iterations −
    T(G_n) = 3, fallbacks 1, and Lemma WRAP's six must-0 counters (§3: s3fail, nonstd, nohoward, fbwrong, endwrong, wrong) are 0 on
    every row: the run is a Howard run of G_n by G_n's own valuation, of fried.howard's length. No tie event on Howard's run of G_n
    for n = 2, …, 8 (out/wrap_ties.out).
  - iterations, fallbacks on F_n (out/free_xi.out; the same engine): iterations − T(G_n) = 3 and fallbacks = 1 on every row, as
    Lemma FREE-REACH (c), (d) says with T3* = T(G_n).
  - state for state on F_n (out/xtraj.out; counter mism, unit: (state t ≤ T(G_n), Even choice vertex of G_n) pairs at which the
    option chosen in F_n at state t is not Howard's successor in G_n at state t): 0 of 60,760 pairs at n = 2, …, 6. Control
    CTRL=1 (states shifted by one): fires, mism 138 and 433 at n = 2, 3.
  - engine 2 (out/wrap_xck.out, out/xck.out; unit: one run of box190 n5bxi.py, implementation 2 of box 190 §1, on L-COMP's n5b with
    pgsolver_si valuations): the same iterations and fallbacks as engine 1; the regions of both engines equal harness Zielonka;
    harness verify.check on both strategy outputs: 0 errors; «AGREE+CORRECT» on W_n at n = 2, 3, 4 and on F_n at n = 2, 3, 4, 5.
  - E-DOM build (out/edom_xi.out): comp(G_n) through plain gamma3.build, i.e. the genome game Γ3(comp(G_n)); iterations = L-RED R217
    §7's genome T (14, 16, 18 at n = 2, 3, 4) + 3.
  - N5 (out/wrap_fried_spec.out, out/free_spec.out; n5v.py mode spec from S3): 3, 4, 5, 6, 7 iterations on W_n and 5, 5, 5, 5, 6 on F_n at n = 2, …, 6, one fallback each;
    6 on every W^L_n, n ≤ 6.
- Growth: the count doubles per level while |V| grows by 251 (W_n) or 309 (F_n). Local exponent log(it_(n+1) / it_n) /
  log(|V|_(n+1) / |V|_n) on F_n: 2.19, 2.79, 3.42, 4.07, 4.59, 5.38 for n = 2, …, 7; on W^L_n: 1.55, 1.93, 2.33, 2.75, 3.16 for n = 1, …, 5. The counts stay
  below |V| on the rows run so far (F_8: 2,489 against 2,562); the claim is about growth.

The paper's own game (runw104.sh; out/wrap_lmcs_xi.out, out/wrap_lmcs_spec.out, out/wrap_xck.out; runs from S3 on W^L_n):
| n | \|G^L_n\|, edges | T: Howard on G^L_n from ι (tie events) | 2^n | \|V(W^L_n)\| | N5′-xi on W^L_n, fig4: iterations, fallbacks | the same, table4 | engine 2 (fig4): iterations, verdict | N5 (spec) on W^L_n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 14, 27 | 8 (0) | 2 | 211 | 11, 1 | 11, 1 | 11, AGREE+CORRECT | 6 |
| 2 | 24, 52 | 26 (0) | 4 | 395 | 29, 1 | 29, 1 | 29, AGREE+CORRECT | 6 |
| 3 | 34, 80 | 62 (0) | 8 | 600 | 65, 1 | 65, 1 | 65, AGREE+CORRECT | 6 |
| 4 | 44, 111 | 134 (0) | 16 | 826 | 137, 1 | 137, 1 | 137, AGREE+CORRECT | 6 |
| 5 | 54, 145 | 278 (0) | 32 | 1,073 | 281, 1 | 281, 1 | not run | 6 |
| 6 | 64, 182 | 566 (0) | 64 | 1,341 | 569, 1 | 569, 1 | not run | 6 |
- T is computed by wrap104.py's own howard() on G^L_n (it equals 9·2^n − 10 on every row, the count L-LIT's T66 reports); «tie
  events» counts the (state, Even vertex) pairs of that run at which the current successor is not best and two or more successors
  are best: 0, so on these games every tie resolution of Howard's rule gives the same run. Lemma WRAP's six counters are 0 on every
  row of both versions; iterations − T = 3; engine 2 agrees and the outputs are correct at n = 1, …, 4 (fig4).

### 5.3 The Lead's three questions (14:36Z, (a) (i)-(iii)), and which landed statements do not apply
- (i) W(H, s0), W_n, W^L_n and F_n are parity games in TARGET.md §1's sense: finite, V = V_E ⊔ V_O, every vertex has a successor
  (self-loops at c_W, K2 and, in F_n, c_X), priorities are natural numbers (in the frozen files the largest is below |V|; SPEC S1
  reads their order and parity only, so TARGET.md §1's compression to {0..n} changes no run).
- (ii) The counts are iterations of N5′-xi as R117 / R118 (k) / R124 / R125 count them: the algorithm is R118's [N5XI] (SPEC S1-S5
  with FIX 1-4 and box 190 §1's S4a′), started at SPEC's default S3, «iterations counted as in SPEC S4» (one iteration = one pass
  with Iσ ∪ Iτ ≠ ∅; the final pass is not counted). The engine is box190 n5v.py mode xi, implementation 1 of box 190 §1 and the
  engine of P-N5-END's and P-N5-CHAIN's DATA; implementation 2 (n5bxi.py) gives the same counts. No variant, no given start pair.
- (iii) The outputs are correct: SPEC S5's regions equal harness Zielonka's and harness verify.check accepts both strategy outputs,
  for both engines, on the 7 + 4 two-engine rows; on all other rows the regions of engine 1 equal Zielonka's (counter wrong 0).
- Outside R104's [DEF]: W(H, s0) is not Γ3-shaped (no levels, no e- and β-vertices). F_n is Γ3-shaped and leaves [DEF] in one clause
  only, the priorities of the β- and e-vertices (§4, Definition): out/prio.out, «odd betas above some e» ≥ 16, against 0 for the
  E-DOM build.
- Landed statements that assume that clause, and so say nothing about F_n (nor, a fortiori, about W(H, s0)): R104's SBAR, PLAY, KEY
  and Theorem REALIZE, R117's REACH3 and R124's EXACT-L (IDEAL-ACYC with [DEF]; σ̄ on the β-face needs e above β); R121 (E-DOM,
  E-MON, HUB-ASC-G); R122 (acyclic: Odd never leaves the β-face); R123 (B-ONLY, NO-TIE, QUIET); R125's B-ONLY3, NO-TIE3, QUIET3,
  T-QUIET3, E-MON3, CHAIN-DECOMP3, UP-B3, CHAIN3; R126 (GATE-CLASS, QUIET-N); boxes 208 / 209; this lane's boxes 99-103. Landed
  statements that hold on F_n by §4: S3-START, PAD, K3, K2-r, TAU3, ESC3-ALL, W3-ALL, REACH3-ALL, E0-E4, ENDGAME-3 (-N5), END-T3.

## 6. Statement XI-EXP (CONDITIONAL; a conjecture until its two items are refereed), and what a refereed statement needs
- DATA (two engines on W_n and W^L_n at n ≤ 4 and on F_n at n ≤ 5): N5′-xi from S3 runs exactly T + 3 iterations, as a Howard run of the inner game, on W_n
  (n ≤ 6) and F_n (n ≤ 8; T = 30, 70, 150, 310, 630, 1,243, 2,486) and on W^L_n (n ≤ 6; T = 9·2^n − 10, both priority versions). The rows n = 7, 8
  of W_n and W^L_n and the two-engine check at n = 5 are the long runs (runw104.sh with LONG=1), started after this freeze; their
  outputs land as Addendum A.
- The published theorems, opened here (pdftotext of the arXiv PDFs; superscripts and indices print flat, «2n» is 2^n, «I loc» is
  I^loc):
  - [F11] O. Friedmann, «An Exponential Lower Bound for the Latest Deterministic Strategy Iteration Algorithms», Logical Methods in
    Computer Science 7 (3:19) 2011, arXiv 1106.0778v2, pdf sha256 46c96f44775aa2b0…. §4: the locally optimizing policy «selects a
    most profitable strategy decision in every point with respect to the current valuation. More formally, it holds for every
    strategy σ, every player 0 node v and every w ∈ vE that w ⊴σ I loc G (σ)(v).» §6.2, Table 4 and Fact 6.1 (the game G_n and its
    size), the initial strategy ι_{G_n}. Theorem 6.14: «Let n > 0. The Strategy Improvement Algorithm with the I loc -policy requires
    at least 2n improvement steps on Gn starting with ιGn .»
  - [F09] O. Friedmann, «A Super-Polynomial Lower Bound for the Parity Game Strategy Improvement Algorithm as We Know it», arXiv
    0901.2731v1, pdf sha256 6c56adb207f38468…. Theorem 8, [Q] as L-RED 54 quotes it (R217 §10): «13·2^n − 9 iterations on G_n using
    the locally optimizing improvement policy.» Its games and counts differ from [F11]'s and from PGSolver's switchallexp.
- L43 (Lead reading, «active»): a lane DEAD of an asymptotic statement is DATA with numbers until a refereed proof or an instance
  beyond an explicit bound exists. No landed bound exists on these games. So the statement is a conjecture with a short named route:
**STATEMENT XI-EXP (CONDITIONAL on (X-WRAP) and (X-TIE); not refereed; no «proved» wording applies).** For every n ≥ 1, N5′-xi from S3
makes at least 2^n + 3 iterations on W^L_n = W(G^L_n, ι), G^L_n with Figure 4's injective priorities: a parity game with O(n²) vertices
(|W| = n_H + 7·m_E + 6·m_O + n_O + 9, n_H = 10n + 4, m_E + m_O = 1.5n² + 20.5n + 5).
- It follows from three items:
  - (X-WRAP) Lemma WRAP (§3), to be refereed; (W4) is its one new step. By (iii) the H-parts of the run are a run of strategy
    improvement on G^L_n from ι in which every Even vertex takes a ⊴-best successor at every step, i.e. a run under a policy with
    [F11] §4's defining property of I^loc; by (iv) the run has exactly T + 3 iterations.
  - (X-F11) [F11] Theorem 6.14, as published: T ≥ 2^n for the I^loc-policy on G_n from ι_{G_n}.
  - (X-TIE) OPEN, small (the «tie item» of the Lead's 15:19Z ruling). [F11] §4 defines I^loc by a property; if two successors
    tie for best, several policies have it, and WRAP's run uses N5′-xi's resolution (and keeps a best current successor). Needed:
    VJ switch-best with that tie rule is an instance of the paper's I^loc, and Theorem 6.14's proof holds for it; or no tie occurs
    on the run. DATA: tie events 0 for n ≤ 6 in both priority versions (§5.2). Not proved for every n.
- The genome-shaped route (FREE-REACH (§4) refereed, plus (X-COMP) OPEN: for every n the HOW3* run of F_n is Howard's run on
  PGSolver's G_n at the movers that stand for its Even choice vertices; DATA: mism 0 for n ≤ 6) is longer and is not needed for
  XI-EXP. Its value is §7's reading: one clause of R104's [DEF] is all that separates box 209's family from Friedmann's.
- If XI-EXP holds, «N5′-xi makes polynomially many iterations on every parity game» is false, and N5′-xi's worst case is at least
  Howard's on every parity game, up to the wrapper's size.

## 7. Why: the W-FLAT principle (PROVED, lane, as a corollary of §3-§4's proofs; READING where marked)
- **Corollary W-FLAT.** Let R be any rule that picks σ_new(x) inside TIE(x) at every Even x in S4a (SPEC's root-first key, box 190's
  Ξσ-best, a largest-index rule, …), all else as SPEC. From S3 on W(H, s0), and on Γ3*(G*), until its first fallback, the run of N5
  with R visits only standard states, and at each step every choosing vertex (v ∈ V_E, resp. a mover) takes R's pick in A(x) = {its
  current option} ∪ {its strictly Ξσ-better options}.
  Proof: (W2), (W5), (W6) and the first two bullets of (W7) use no property of the tie rule, and TIE(v) = A(v) is (W6); on Γ3*(G*)
  the same with FREE-REACH (a), (b), ESC3-ALL and W3-ALL (iii). ∎
- So on these games the algorithm is a ONE-SIDED strategy improvement on the inner game (H itself; resp. HOW3*(G*): movers against
  Odd's best reply at the gates), with the improvement rule «R among current and strictly better options, at all choosing vertices
  at once». τ is constant and the arena values tie: the two-sided step that distinguishes N5 from classical strategy improvement
  carries no information there.
  - R = Ξσ-best: Howard's rule on H (WRAP). Polynomial on the E-DOM genome games if box 209 stands; exponential-looking on Friedmann's.
  - R = SPEC's key: on W(H, s0) a static index rule (§3, Remark 3: polynomial); on Γ3-shaped games the IDEAL rule of R104 with Odd
    replying, where the keys move with the lower levels (O1, O2 in §8).
- READING (what E-DOM is). E-DOM makes the genome's inner game, at class level, a shortest-path game with non-negative weights: box
  208 §0's own reading; its Addendum A5 says of Friedmann's games [Q] «those games are not genome games Γ(G), and ALL-TCYC says
  nothing about them». L-LIT T67: [Q] «DEEP is the only chain link that fails on Friedmann's games.» Boxes 208 / 209 and this lane's
  chain (boxes 99-103) are therefore theorems or conjectures about Howard's rule on E-DOM inner games. §3-§5 show that E-DOM is a
  restriction on the INPUT family, not a property that N5′-xi enforces: the input may be W(H, s0) for any H.
- READING (stop rules; not tested). On every W(H, s0) and every Γ3*-game τ has no improving edge at S3, so τ is already optimal and
  Odd's valuation gives the winning regions at iteration 0: all the fleet's genome games, R104's included, are games in which Odd is
  done at the start and only Even's side runs. A variant that stops when Iσ = ∅ OR Iτ = ∅ would solve these games at once. That is
  not a repair. N5′-xi as specified (box 190 §1) stops only when both are empty; and the stop is defeated by one more closed gadget:
  the mirror image of the core (owners swapped, priorities + 1) is a component in which Odd keeps an improving edge that S4b's arena
  optimum never takes (the mirror of K3 (b), (d)), so Iτ ≠ ∅ for as long as the Even side runs. OPEN as a statement.

## 8. What is left for G-N5-TIME (N5 itself): the open links, each as a statement
N5 is the row's candidate. The landed frame on EVERY game:
- Termination: [Q] R15 (d) «N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ
  (on G^d), and» changes at least one of them; [Q] «h(≺) can be exponential; NO polynomial or other useful iteration bound follows».
- Output and cost: R57 (b) OUT-G, (c) BIT-G (quoted in §1), under the standing SPEC premise.
- Phases: [Q] R47 (a) (c) «along a run at most n(n − 1) transitions change λ and at most n(n − 1) change λ^U, so a run has at most
  2n(n − 1) + 1 joint» λ-runs.
- The count as a whole: R90 (CUT-RED) bounds T by a polynomial in n, m_E, B*, REP*, SC*, O*, [Q] «so T is polynomial if and only if
  B*, REP*, SC* and O* are» (B*: fallbacks or τ-changes inside one λ-run; REP*: repeat late adoptions inside one W-run; SC*: re-entries
  of W-silent or own-cycle edges; O*: τ-changes inside one λ^U-run). None is bounded.
- The genome family in this frame: on Γ3(G) and on Γ3*(G*), τ never changes and there is one fallback (A3, FREE-REACH (b), (e)), so
  B* ≤ 1 and O* = 0 there, and R90's bound reads T ≤ poly(n)·(1 + REP*) + poly(n)·SC*. The family exercises one regime of R90:
  re-adoptions and re-entries inside one τ-constant stretch. Whatever is proved on it says nothing about B* or O*.
- Necessity: [Q] R117 (REAL-IDEAL-S3) «if every FL run of N5 from S3 on every n-vertex game has length at most p(n) for a nondecreasing
  polynomial p (in particular if N5 from S3 makes at most p(n) iterations), then L(G) ≤ p(N + 7M + 10) for every acyclic G»; [Q] R124
  (EXACT-L) «N5 (SPEC S1-S5 with its FIX 1-4 tie-breaks) from S3 on Γ3(G) makes exactly L(G) + 3 iterations» on IDEAL-ACYC.

The open links, in the order in which a kill or a proof would meet them:
- **O1 (IDEAL-ACYC-POLY; the tower question; OPEN).** L(G) ≤ poly(N + M) for every Ξ-acyclic R104 genome (the key rule; Odd stays on
  the β-faces, R122). Landed: [Q] R113 «(T-BOUND) on 𝓛^R_d, F(l) ≤ 2^(l+2) − 2 and T ≤ 2d + 2(F(0) + … + F(d − 2)) ≤ 2^(d+2) − 2d − 4»,
  an exponential upper bound; [Q] L50 (3): «A family doing so on linearly many levels would, by RESULTS R104 Corollary REAL-IDEAL, make
  FL-POLY false.» [Q] NOW (M4 row): «SEVEN capped levels: HIT7 F(6) = 254 at d 28 (L-COMP 11, sha1 6a3b274d, DATA, CANDIDATE tower;
  S(5,6,7) ≤ 20,24,28)». Necessary for G-N5-TIME by R117. Boxes 208 / 209 do not touch it: Howard's count on the same genomes is
  already landed, [Q] R122 «the Howard run of IDEAL-CYC(G) from any mover state has C = 0, R = 0 and T_CYC ≤ N».
- **O1′ (KEY-CYC; OPEN).** F(G) ≤ poly(N + M) for every R104 genome, F the first fallback of N5 from S3 on Γ3(G) (the key-rule run with
  Odd replying on Ξ-cyclic genomes). [Q] R124: «it bounds none of F, T3, L(G) (OPEN), and nothing outside Γ3(G)». Necessary for
  G-N5-TIME (N5 makes F + 2 iterations there). No lane statement bounds it; boxes 208 / 209 do not (L1).
- **O2 (KEY-FREE; NEW; OPEN).** F*(G*) ≤ poly(N + M) for every FREE genome G*, F* the first fallback of N5 from S3 on Γ3*(G*).
  Necessary for G-N5-TIME by FREE-REACH (e): N5 makes exactly F* + 2 iterations on Γ3*(G*). It contains O1 and O1′. Kill side: a
  family of free genomes with F* super-polynomial is a family of parity games on which N5, from its default start, is
  super-polynomial; G-N5-TIME would be false. The adversary of O2 has what the tower route lacked under E-DOM: odd carriers above
  e-vertices, and with them Odd's replies and Ξ-availability driven by an arbitrary two-player inner game (Friedmann's counter runs
  there under Howard's rule, §5). What stays as under E-DOM: a level-0 mover only moves to a smaller gate index (its key is its e's
  index), so a long key run needs many levels, as in R113. DATA so far: F_n has F* = 3, 3, 3, 3, 4 at n = 2, …, 6 (and W(H, s0) is no test: there the key rule is static, §3 Remark 3); 2,000 random free genomes have max F*
  5 (§4). No search has been run. This is the nearest unexamined kill question for N5.
- **O3 (OFF THE Γ3 SHAPE; OPEN).** B*, REP*, SC*, O* of R90 polynomial on every parity game. Γ3-shaped games give B* ≤ 1, O* = 0, so
  O1-O2 are statements about REP* / SC* on one shape only. Fallbacks (B*) are Howard steps of S4c; on Γ3-shaped games the first one
  ends the run (the core flips, E2-E4), elsewhere nothing bounds them ([Q] NOW l. 2: «FB-LIN (f ≤ n per phase; 5 L-RED boxes, no kill,
  data 0.79n) OPEN»).
- **O4 (GAUNTLET; not done).** Steps 4 (written running-time proof, double-refereed) and 5 for N5; Lean correctness.
- Chain for N5, in one line: «N5 polynomial on all parity games» ⇐ O3 ∧ R90 ∧ R57 (b), (c), under the standing SPEC premise; and
  O3 with R90 implies O2, which implies O1′, which implies O1 (each is the iteration count on a subfamily). Boxes 208 / 209 supply none
  of O1-O3. The arrows from them to this line are absent, not open: they bound a different rule (Howard's) on a subfamily (E-DOM) of
  one shape (Γ3).

### 8.1 Relayed by the Lead (cross-lane statements NOT opened by me; recorded as relayed, to be cited from their own files)
- Lead 14:36Z (c): P-N5-LEVEL / box 209 continue; box 104's map must record «N5′-xi is not an M4 candidate»; the open M4 question
  becomes N5 (SPEC tie) on free-priority Γ3-shaped and on general games. Recorded in §0 item 3 as CONDITIONAL on WRAP and (X-TIE)
  until refereed (Lead 15:19Z: «keep «N5′-xi exponential» labelled CONDITIONAL on WRAP + the tie item until refereed»).
- Lead 14:47Z: box 209's T3-ALL does not use DEEP3, E-MON3, CHAIN-DECOMP3 or [E-LEV]; T3-ALL and this lane's DEEP3 chain (boxes
  99-103) are INDEPENDENT routes to a polynomial T3, both genome-only (both rest on E-DOM, §5.3).
- Lead 15:13Z, L-COMP 19 box 43 item 3 (claude/l-comp ae0f65c3): TAIL_h(G) leaves the run unchanged and adds h to the depth of every
  Λ-quiet flip on a sink-ending play, so DEEP3's depth cut-off is not a reduction. This is the reason the DEEP3 route is the weaker
  of the two.
- Lead 14:51Z, L-LIT T70 Addendum A (claude/l-lit 9ae31ec3): (1) one-sided Dijkstra-order settling with non-negative weights is
  known only in the MIRROR orientation (Jurdziński–Trivedi, Lemma 19); (2) Schewe–Trivedi–Varghese, arXiv 1501.06484, Theorem 3.7: a
  symmetric rule needs at most linearly many more iterations than the one-optimal variant (stated; proof not in the opened
  version); (3) van Dijk–Loho–Maat, arXiv 2309.02223, Theorem 1: symmetric strategy improvement is exponential on sink games
  «independently of the improvement rule» (their games violate E-DOM); (4) Dijkstra-order settling of the Odd half at class level
  on Γ(G): NOT FOUND. Reading (mine): (3) is the published neighbour of §7's W-FLAT principle; whether its games and rule class
  cover N5 (SPEC key rule) is a question for L-LIT (none of the three papers was opened by me).

## 9. What follows for the fleet (READING; the Lead decides)
1. Verify §3-§5 before anything rests on them: an independent replay of W_n and F_n (n ≤ 6) on another lane's engines (L-COMP's
   n5b-based N5′-xi; L-RED's own.py for the Howard runs); a referee read of WRAP's proof, (W4) first, and of FREE-REACH's table;
   L-RED's attack on the construction (is n5v.py mode xi box 190 §1's algorithm on these games?); L-LIT for (X-TIE).
2. If §3-§5 survive: N5′-xi leaves the M4 path. Boxes 208 / 209 remain a restricted-class question («Howard's rule with VJ
   valuations is polynomial on the E-DOM genome games»): an M3-type statement at best (TARGET.md §7e asks for a precise theorem and a
   novelty check first), with no arrow to M4. Their refereeing can be priced accordingly.
3. For N5 (D18), the map says where the next information is: O1 (the tower, in progress elsewhere) and O2. Kill side of O2: L-RED's
   tower / climb tools with free carrier priorities (free104.build_free takes any π); L-COMP's exhaustive search at small N + M for
   the key rule on free genomes (max F* against N + M, compared with the E-DOM maximum at the same size). Proof side: nothing in the
   fleet's E-DOM lemmas transfers (§4, last bullets).
4. For the design lane: by W-FLAT, an S4a tie rule is a one-sided improvement rule on these games. A variant of N5 can be polynomial
   only if its rule is polynomial as a one-sided rule on every inner game H, or if the variant is not inert on W-flat games. Any new
   variant should be run on W_n (wrap104.py fried n, with ALG) before any proof effort.

## 10. Sources opened (this box)
- Trunk a9699c30c: TARGET.md; docs/GAPS.md l. 11; docs/NOW.md; docs/DECISIONS.md (L43, L50, D21); docs/RESULTS.md R15, R47, R57, R90,
  R104, R113, R117, R118, R120, R124, R125, R126 (lines and the entries' items quoted above).
- claude/l-new 8db300fe: docs/new/N5-ssi-global.md (SPEC), N5XI-GAUNTLET-box190.md, N5-LEVEL-box208.md, N5-IDEAL-STATE.md, N5-TIME-box200.md,
  P-N5-REACH.md (§3-§6), P-N5-CHAIN.md (§2-§3), P-N5-END.md (§2-§6); experiments/new/box189/gamma3.py, box190/n5v.py, xcheck190.py.
- claude/l-red 06e7ececd: docs/red/R215-xi.md, R217-ovt.md (§7, §10); experiments/red/r217/comp.py, gdsl.py, fried.py, fdiff.py.
- claude/l-lit 4a0db9d17: docs/lit/T67-n5-route-summary.md (T66 through it).
- Opened on arxiv.org (PDF fetched, pdftotext): arXiv 1106.0778v2 (sha256 46c96f44775aa2b0…): title page, §2 (injective Ω), §4, §6.2 Table 4,
  Fact 6.1, the initial strategy, Theorem 6.14; arXiv 0901.2731v1 (sha256 6c56adb207f38468…): abstract page, Theorem 8, the size and
  initial-strategy sentences.
- claude/l-lit 9ae31ec3: docs/lit/T66-deep3-lower-bound-families.md Addendum D (Table 4 against Figure 4); 5c53efbd docs/lit/T66-depth-check.py
  (function lmcs, read against Table 4).
- Relayed by the Lead, NOT opened by me (cited as relayed in §8.1): L-LIT T70 Addendum A (claude/l-lit 9ae31ec3); L-COMP 19 box 43 item 3
  (claude/l-comp ae0f65c3).

## Addendum A (L-SI successor 52, 2026-11-12T17:08:02Z (date -u); append-only, §0-§10 unchanged): the long rows of the wrapped games; two probes of N5 (guided wrapper; free genomes) (DATA)
### A.1 The long rows
`LONG=1 bash runw104.sh` (out/wrap_long.out; about 10 min on one core; check104.sh (5)). Units, counters and engines as in §5.2.
- N5′-xi from S3 at n = 7, 8 (on each row: the six must-0 counters of §3 are 0, iterations − T = 3, one fallback):
  - W^L_7 (1,630 vertices): Howard T = 1,142 with 0 tie events, 1,145 iterations. W^L_8 (1,940 vertices): T = 2,294 with 0 tie events,
    2,297 iterations. Figure 4's priorities; the table4 version was not run at n = 7, 8.
  - W_7 (1,822 vertices): T = 1,243, 1,246 iterations. W_8 (2,073 vertices): T = 2,486, 2,489 iterations: the counts of F_7, F_8.
- Two engines at n = 5 (n5v.py mode xi against n5bxi.py): W^L_5: 281 and 281 iterations; W_5: 313 and 313; one fallback each; the
  regions are equal and equal harness Zielonka's; harness verify.check: 0 errors on both outputs («AGREE+CORRECT»).
- The tables of §5.2 with these rows (summ104.py; «not run» is now final for this box):
| n | \|G_n\| | T(G_n): Howard on G_n | \|V(W_n)\| | N5′-xi on W_n: iterations, fallbacks | \|V(F_n)\| | N5′-xi on F_n: iterations, fallbacks | engine 2 on W_n / on F_n: iterations, verdict | F_n state for state: mism | N5′-xi on the E-DOM build of comp(G_n) | N5 (spec) on W_n / F_n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 35 | 30 | 567 | 33, 1 | 708 | 33, 1 | 33, AGREE+CORRECT / 33, AGREE+CORRECT | 0 of 682 | 17 | 3 / 5 |
| 3 | 49 | 70 | 818 | 73, 1 | 1,017 | 73, 1 | 73, AGREE+CORRECT / 73, AGREE+CORRECT | 0 of 2,201 | 19 | 4 / 5 |
| 4 | 63 | 150 | 1,069 | 153, 1 | 1,326 | 153, 1 | 153, AGREE+CORRECT / 153, AGREE+CORRECT | 0 of 6,040 | 21 | 5 / 5 |
| 5 | 77 | 310 | 1,320 | 313, 1 | 1,635 | 313, 1 | 313, AGREE+CORRECT / 313, AGREE+CORRECT | 0 of 15,239 | 23 | 6 / 5 |
| 6 | 91 | 630 | 1,571 | 633, 1 | 1,944 | 633, 1 | not run / not run | 0 of 36,598 | 25 | 7 / 6 |
| 7 | 105 | 1,243 | 1,822 | 1,246, 1 | 2,253 | 1,246, 1 | not run / not run | not run | not run | not run / not run |
| 8 | 119 | 2,486 | 2,073 | 2,489, 1 | 2,562 | 2,489, 1 | not run / not run | not run | not run | not run / not run |

| n | \|G^L_n\|, edges | T: Howard on G^L_n from ι (tie events) | 2^n | \|V(W^L_n)\| | N5′-xi on W^L_n, fig4: iterations, fallbacks | the same, table4 | engine 2 (fig4): iterations, verdict | N5 (spec) on W^L_n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 14, 27 | 8 (0) | 2 | 211 | 11, 1 | 11, 1 | 11, AGREE+CORRECT | 6 |
| 2 | 24, 52 | 26 (0) | 4 | 395 | 29, 1 | 29, 1 | 29, AGREE+CORRECT | 6 |
| 3 | 34, 80 | 62 (0) | 8 | 600 | 65, 1 | 65, 1 | 65, AGREE+CORRECT | 6 |
| 4 | 44, 111 | 134 (0) | 16 | 826 | 137, 1 | 137, 1 | 137, AGREE+CORRECT | 6 |
| 5 | 54, 145 | 278 (0) | 32 | 1,073 | 281, 1 | 281, 1 | 281, AGREE+CORRECT | 6 |
| 6 | 64, 182 | 566 (0) | 64 | 1,341 | 569, 1 | 569, 1 | not run | 6 |
| 7 | 74, 222 | 1,142 (0) | 128 | 1,630 | 1,145, 1 | not run | not run | not run |
| 8 | 84, 265 | 2,294 (0) | 256 | 1,940 | 2,297, 1 | not run | not run | not run |
- What changes in §0, §5.2, §6: for W_n and W^L_n (fig4), «n ≤ 6» now reads n ≤ 8; two engines agree at n ≤ 5 on W_n, W^L_n and F_n.
  T = 9·2^n − 10 on all eight rows of G^L_n; tie events 0 on its Howard run for n ≤ 8.
- On W^L_8 the iteration count is above the number of vertices: 2,297 against 1,940 (W^L_7: 1,145 against 1,630). Local exponents
  log(it_(n+1) / it_n) / log(|V|_(n+1) / |V|_n) on W^L_n, n = 1, …, 7: 1.55, 1.93, 2.33, 2.75, 3.16, 3.58, 4.00.
- (X-TIE), a reading of the opened text; the item stays OPEN. [F11] §4 gives the locally optimizing policy by the property quoted in
  §6 and states no tie-break; its Lemmas 6.2, 6.6 and 6.8-6.13 are stated for σ′ = I^loc(σ). So (X-TIE) is the statement «the proofs
  of the lemmas behind Theorem 6.14 use only that property»: then the theorem holds for every policy with the property, and WRAP's
  run has it at each of its states (every Even vertex of H takes a ⊴-best successor). I have read those lemmas' statements, not their
  proofs. For L-LIT or a referee; on the eight rows run here no tie occurs, so every such policy gives the same run.

### A.2 Probe: N5 itself on a GUIDED wrapper (DATA; no kill; OPEN question GUIDE-RULE)
WRAP freezes τ at faces that all end in c_W, so S4a's arena is flat and only the tie rule acts; that is why it hits N5′-xi and not N5
(§3 Remark 3). The probe asks what N5 does when the frozen faces lead back into the game.
- The game Wg(H, s0, ρ0) (guide104.py; ρ0 a positional Odd strategy of H). As W(H, s0), with two changes. (1) The S3-face of a gate
  g_(v,w) is a path pg (Ω 1), u1, u2 (Ω 0) to w itself; every o ∈ V_O gets, in place of pe_o, a path z1 (Ω 1), z2, …, z5 (Ω 0) to ρ0(o);
  β-faces and the other edges of o pass a valve as before; there is no c_W. On either face an edge of H is a path of 6 edges.
  (2) The core's K2 < K1 (odd) are placed ABOVE every vertex of H (K2 the least odd number above them, K1 = K2 + 2, K0 = K2 + 3,
  K3 = K2 + 4), so that a valve's exit is not Ξσ-improving before the core flips.
- READING (not proved; the counters below are its DATA): before its first fallback the run keeps τ at these faces (Iτ = ∅: every
  other Odd edge passes a valve, where Even's reply to τ exits to K0's cycle), the valves at y, and Iσ at v ∈ V_E is the set of
  edges that are improving in H. S4a's arena is then the ONE-player game «H with Odd fixed at ρ0, Even restricted to its current and
  its improving edges», and N5's step is Even's optimal strategy there: a best response to a fixed Odd strategy inside the
  improvement arena. For N5′-xi the step is the same wherever the arena has no tie.
- General remark (lane; one line from a published theorem): along any run with τ constant and Iτ = ∅, τ is an optimal Odd strategy
  of the whole game from the first state on (a strategy without an improving edge is optimal: [F11] Theorem 3.3, from VJ00, applied
  to the dual game), while σ is not optimal as long as Iσ ≠ ∅. So on such runs N5's S4a is «Even's best response, inside the
  improvement arena, to an optimal strategy of Odd». On R104's genome games and on W the edge that σ lacks to the end is in the
  core ((K0, K1) ∈ Iσ in every standard state), and the first fallback takes it (ENDGAME).
- DATA (rung104.sh; out/guide104.out; 24 rows; unit: one run from S3; ρ0 = Odd's optimal counterstrategy to s0 in H). On every row:
  S3 standard True (S3's pair is s0, the guide faces, ρ0, y, the core's standard config), τ changes 0 before the first fallback,
  1 fallback, regions = harness Zielonka. On the 21 rows with the core above H: valve moves 0 before the first fallback.
  - H = H_n, the paper's family for the GLOBALLY optimizing policy ([F11] §8.4; L-COMP's hn.py at claude/l-new fcba92fc, mode fig,
    start ι): N5 makes 14, 37, 65, 99, 139, 185 iterations at n = 1, 2, 3, 4, 5, 6 (first differences 23, 28, 34, 40, 46; second differences
    5, 6, 6, 6): quadratic on these rows. For comparison, not rerun here: L-COMP's box 16 README (same commit) reports 22,
    28, 34, 40 iterations of N5 from S3 on H_n itself at n = 3, …, 6 and 107, 235, 491, 1003 steps of the globally optimizing policy.
  - H = G^L_n (the family of §5, ι): 6, 8, 9, 11, 13 at n = 1, 2, 3, 4, 5. H = PGSolver's switchallexp_n: 10, 10, 12, 14 at n = 2, 3, 4, 5.
  - N5′-xi on Wg (hn n = 1, 2, 3; G^L_n n = 1, 2, 3): the same counts as N5.
  - Control of change (2), CORE=low (K1 = 5, K2 = 3) on hn n = 1, 2, 3: valve moves 11, 24, 30 before the first fallback (the valves leave
    y, as expected when the core's cycles are better for Even than H's sink), iterations 14, 28, 34.
- Result: no exponential growth on these three families in this shape; nothing asymptotic is claimed. The guided wrapper makes N5
  slower than on H_n itself (quadratic against linear on the rows above) and so is a new adversary shape for N5.
- OPEN (GUIDE-RULE; a kill question for N5, next to O2): is there a family (H_n, s0, ρ0), or a wrapper whose frozen faces lead into
  any other one-player structure, on which «Even's best response to the fixed faces inside the improvement arena» runs
  super-polynomially? Any such family is a family of parity games on which N5 from S3 is super-polynomial. What an attacker has:
  the improving sets come from an arbitrary two-player game H; the fixed faces may lead to any vertex whose Ξσ-value is never
  below the β-face's (else Odd would use the face in Ξσ and H's values change). What works against the attacker: (a) against the
  fixed faces the value of every vertex is non-decreasing from step to step before the first fallback (σ lies inside the arena and
  σ_new is the arena's pointwise optimum), so a long run needs a long increasing chain of these values, or many tie steps; (b) a
  fixed face cannot copy an Odd reply that depends on several Even choices: in H_n the only Odd vertices with two successors are
  the e_i (→ d1_i or h_i; ρ0(e_i) = d1_i on every row), Odd's true reply leaves to h_i when the stubborn cycle d1_i, d2_i, d3_i, e_i
  ([F11] §8.2) is closed, and on Wg(H_n) a closed cycle is instead an Even win of the arena.

### A.3 Probe for O2 (KEY-FREE): a weak head-to-head search (DATA; no separation)
- runc104.sh (climb104.py; out/climb104.out; about 40 min on one core): 18 hill climbs = 3 shapes × seeds 1, 2, 3 × {free, edom}, 3,000
  steps each. Score: iterations of N5 (n5v.py mode spec) from S3 on the Γ3-shaped game. Mode free: the 2M carriers (β's and e's) in
  any order; mode edom: R104's priorities. Same shape, seed, number of steps and mutations, except the priority move (§8, O2).
| shape: levels × movers per level, options | N, M, \|V\| | free: best iterations (seeds 1, 2, 3) | edom: best iterations (seeds 1, 2, 3) |
| --- | --- | --- | --- |
| 4 × 3, 3 | 12, 36, 274 | 18, 17, 18 | 17, 17, 15 |
| 6 × 2, 3 | 12, 36, 274 | 17, 14, 14 | 18, 18, 20 |
| 8 × 2, 2 | 16, 32, 250 | 16, 18, 14 | 18, 18, 18 |
- Largest count found: free 18, edom 20. At these sizes this search finds no free genome on which N5 runs longer than on the best
  E-DOM genome it finds. A weak search (unit: one climb; 18 climbs); nothing asymptotic; O2 stays OPEN. For scale: NOW's M4 row (quoted
  in §8, O1) has a CANDIDATE tower with F(6) = 254 at d = 28 under E-DOM, far above what a blind climb reaches; a search that starts
  from that tower and frees its carrier priorities is the natural next probe (not done here).

## Addendum B (L-SI successor 52, 2026-11-12T18:03:50Z (date -u); append-only): a scan of the fixed faces at H_n's cycle gates (DATA, negative); a note on tie rules; N5 against the globally optimizing policy (DATA)
### B.1 Gate-face scan for GUIDE-RULE (A.2) on H_n: no variant is faster than quadratic
- gscan104.py (runs104.sh; out/gscan104.out; 40 rows = 10 variants × n = 1, …, 4; unit: one run of N5 (n5v.py mode spec) from S3). The
  game is A.2's Wg(H_n, ι, ρ0) with two more parameters. In H_n the only Odd vertices with two successors are the e_i (→ d1_i or
  h_i); e_i is entered from d3_i (Even) and from f_i (Odd, one successor). GF: where the fixed face of f_i leads (e: to e_i; d1: past
  e_i into the cycle; h: past e_i out to h_i). G3: where the fixed face of the Even edge d3_i → e_i leads (e, d1, h). RE: ρ0(e_i) (d1
  or h). copy 1: a face that skips e_i passes a pad with e_i's priority; copy 0: it does not (then a closed cycle d1_i, d2_i, d3_i
  has an odd top on the fixed faces). Every target is reachable from the skipped vertex by Odd's own moves, so H's values are those
  of H_n up to that pad.
- On all 40 rows: S3 standard True, τ changes 0 and valve moves 0 before the first fallback, 1 fallback, regions = harness Zielonka.
| GF | G3 | RE | copy | iterations at n = 1, 2, 3, 4 | first fallback at n = 1, 2, 3, 4 |
| --- | --- | --- | --- | --- | --- |
| e | e | d1 | 1 | 14, 37, 65, 99 | 12, 34, 62, 96 |
| e | h | d1 | 1 | 13, 19, 25, 31 | 11, 17, 23, 29 |
| h | e | d1 | 1 | 14, 36, 64, 98 | 12, 34, 62, 96 |
| h | h | d1 | 1 | 13, 20, 27, 34 | 11, 18, 25, 32 |
| e | e | h | 1 | 13, 20, 27, 34 | 11, 18, 25, 32 |
| e | d1 | h | 1 | 14, 36, 64, 98 | 12, 34, 62, 96 |
| h | d1 | d1 | 1 | 14, 36, 64, 98 | 12, 34, 62, 96 |
| e | d1 | d1 | 0 | 6, 12, 18, 24 | 4, 10, 16, 22 |
| h | d1 | d1 | 0 | 15, 27, 39, 51 | 4, 10, 16, 22 |
| e | h | h | 1 | 13, 20, 27, 34 | 11, 18, 25, 32 |
- Iterations after the only fallback: 2 on every row, except the variant (e, e, d1, copy 1): 2, 3, 3, 3 (there N5 goes on after the core has flipped); the variant (h, d1, d1, copy 0): 11, 17, 23, 29 (there N5 goes on after the core has flipped).
- Largest count: 99 (n = 4). The variants fall into two groups: those that keep «a closed cycle is an Even win of the arena» grow
  like A.2's row (second differences 5-6), the others linearly. READING (mine, not a counter): on the fixed faces a cycle, once
  closed or once its exit is over-valued, is never worth leaving and re-entering, so every bit is set once and the counter of [F11]
  §8 never counts; about one pass of the deceleration lane (6n − 2 nodes) per bit gives the quadratic rows.
- DEAD (lane, DATA; scope: these ten fixed-face variants on H_n): «N5 on a guided wrapper of H_n follows the globally optimizing
  policy's exponential run». Obstruction: Odd's reply at e_i depends on three Even choices (d1_i, d2_i, d3_i); a positional fixed
  face is exact only for plays that enter through f_i. GUIDE-RULE itself stays OPEN.
### B.2 Tie rules (relayed by the Lead 17:08Z, not opened by me)
- The Lead's words: «The 16 count differences L-RED 66 found between its engine and n5v are all tie rule, which matters for your
  write-up's independence wording.» (Which runs they are on is in L-RED 66's file, not opened by me.) A difference that comes from
  the tie rule among ⊴-best successors is consistent with Lemma WRAP as stated: (iii) is about the Howard run under N5′-xi's own tie rule (Ξσ-best,
  then SPEC's choice, then the larger index), T is the length of THAT run, and wrap104.py's counter nohoward tests «a ⊴-best
  successor by H's own valuation», not equality with another engine's run. A Howard run under another tie rule can have another
  length. §5's rows on G^L_n (n ≤ 8) and on switchallexp_n (n ≤ 8) have no tie event, so there every tie rule gives the same run.
- Wording to use for this box: «two implementations of N5′-xi agree» (n5v.py, n5bxi.py) is agreement of two implementations of the
  same rule, not of independent rules; an engine with another tie rule replays WRAP's counters nohoward (best by H's valuation),
  fbwrong and endwrong against ITS OWN T, not the counts of §3's random rows.
### B.3 Where the fixed faces copy Odd's reply, N5 makes the globally optimal improvement step (DATA; READING WRAP-GLO; CONJECTURE GLO-1P)
- The globally optimizing policy (Schewe's; [F11] §4 and Theorem 4.2): the new strategy is an optimal strategy of the game in which
  Even is restricted to its current and its improving edges and Odd is free. [F11] §8 is the paper's exponential lower bound for it
  (Theorem 8.4, on H_n).
- glo104.py (runq104.sh; out/glo104.out; 18 rows). Per step before the first fallback it computes A(v) = {current} ∪ {improving
  successors of v in H} by H's own valuation and OPT = the optimal valuation of H restricted to A (Howard iteration on that game
  from the current strategy to its fixpoint). Counter iglofail (unit: steps before the first fallback): the H-valuation of N5's
  new H-part differs from OPT at some vertex. cntfail (unit: games): the first fallback is not at (this file's own run of the
  policy from s0) + 1. endfail (unit: games): iterations ≠ first fallback + 2.
  - G^L_n with faces that copy Odd's reply (ρ0(e_i) = d_i; the fixed face of the Even edge d_i → e_i leads to h_i: in G^L_n the only
    Odd vertices with two successors are the e_i, and Odd leaves the simple cycle exactly when d_i → e_i is chosen), n = 1, …, 6:
    iglofail 0, 0, 0, 0, 0, 0; the policy's own run has 3, 4, 5, 7, 9, 11 steps, N5 makes 6, 7, 8, 10, 12, 14 iterations, first fallback at
    4, 5, 6, 8, 10, 12: on every row N5 = the policy's run + 3 iterations.
  - Control, G^L_n with plain faces (to w; ρ0 = Odd's optimal counterstrategy to ι), n = 1, …, 4: iglofail 0, 2, 3, 5: fires for n ≥ 2.
  - Random ONE-player games (harness gen.random_game, every Odd vertex cut to its first successor; a random s0; plain faces):
    «rand1p seed 1045 games 300 n<=12: steps before the first fallback 303 iglofail 0 | cntfail (first fallback != policy steps + 1) 2 endfail (iterations != first fallback + 2) 0 | max steps of the globally optimal policy 5 max |Wg| 291»
    «rand1p seed 1046 games 100 n<=24: steps before the first fallback 147 iglofail 0 | cntfail (first fallback != policy steps + 1) 2 endfail (iterations != first fallback + 2) 0 | max steps of the globally optimal policy 4 max |Wg| 511»
    cntfail is not 0: the two runs can resolve ties between equally valued strategies differently (not analysed further); the
    tested statement is iglofail.
  - H_n (B.1's variants (e, e, d1, 1) and (e, h, d1, 1)), n = 1, 2, 3: iglofail 0, 4, 30 and 1, 2, 2; the policy's own run on H_n has
    11, 43, 107 steps (the counts L-COMP's box 16 README gives for PGSolver's port), N5 on the wrappers 14, 37, 65 and 13, 19, 25.
- READING WRAP-GLO (NOT proved; a candidate lemma with WRAP's proof as template, (W6) replaced). If every Odd vertex of H has one
  successor, then on Wg(H, s0) the real valuation at H's vertices is H's, Iτ = ∅ at the frozen faces, and S4a's arena is H
  restricted to A; so N5's step at H's Even vertices is a step of the globally optimizing policy on H, the first step without a
  change is the first fallback, and the run ends 2 iterations later. The same holds for a two-player H whose Odd reply is copied
  by fixed faces for every Even strategy of the arena (G^L_n above). DATA: the rows above.
- What it would give, if proved: «N5 from S3 makes polynomially many iterations on every parity game» IMPLIES «the globally
  optimizing policy makes polynomially many steps on every one-player parity game, from every start». The latter is CONJECTURE
  GLO-1P (lane; Lead ruling 17:27Z: it «is a CONJECTURE in your text and stays one»); it would be a NECESSARY condition for
  G-N5-TIME, next to O1-O3. No source opened: I have read nothing on policy iteration on one-player games (mean-payoff or
  shortest-path policy iteration, lower bounds for Howard's rule there), so I do not know whether a published bound, upper or
  lower, covers the globally optimizing rule. That is a question of box 105 (Lead 17:27Z).
- A sketch, NOT a proof, and nothing in this box rests on it: on a one-player game, (a) if an optimal successor w of v already
  has its optimal value and the current play from w avoids v, then v has its optimal value after one more step; (b) values never
  decrease and a vertex on a closed cycle has the cycle's value, so the same cycle is not closed twice with the same vertex on it,
  which is what the bits of [F11] §8's counter do. This says why I do not see a one-player copy of that counter; it bounds nothing.
- For the kill side: a counterexample family to GLO-1P, or a two-player family whose Odd replies fixed faces can copy and on which the policy
  is super-polynomial, would make N5 super-polynomial (through Wg). [F11]'s H_n is not such a family (B.1: its stubborn cycles).
