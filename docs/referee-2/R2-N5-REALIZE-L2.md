# R2-N5-REALIZE-L2: REFEREE-2 word-diff of P-N5-REALIZE line L-2 against L-1 (after CHECKER C115 FAIL E-1), and the R36 (c) re-route of SBAR (ii)
Referee: REFEREE-2 successor 26, Opus 5.5 (D15). Written 2026-11-02 (date -u; see the commit). Verdict: **MATCHES**.

## 0. Object
- Commit: claude/l-red c374be8f3af77dfdf95b2980b115aa30ded9b9a1, an ancestor of origin/claude/l-red. I re-hashed every file at that commit:

| file | sha1 at c374be8f | check |
| --- | --- | --- |
| docs/red/P-N5-REALIZE.md (frozen packet) | 067f06b6c67969adf346621b4a92b253491ab2b9 | untouched ✓ |
| docs/red/P-N5-REALIZE-line.txt (frozen line) | 53dd6e9fd727a6ff2d5e49648366f28d7398e9d9 | untouched ✓ |
| docs/red/P-N5-REALIZE-line-L1.txt | 1d72ee310b9b4af252724e06a181221a9c2828ec | untouched ✓ |
| docs/red/P-N5-REALIZE-fixes.md (entries 1-3) | 64f062c268b2264dfef53bf9efb3673c9921ac82 | = Lead's sha1 ✓ |
| docs/red/P-N5-REALIZE-line-L2.txt | b44456d10b7be37732c65a88ca138a4300fbb6c3 | = Lead's sha1 ✓; one line, 4,799 bytes, no heading marker |

- Read: CHECKER C115 (claude/checker fbca67cf, docs/checker/C115.md) §3 E-1 and §4 G-1, G-2, G-3, G-7, G-10. Also RESULTS R15 (iii)
  (l. 649-650), the R15 side finding, R36 (heading, (c), (d), Reading), and the R57 route (C115's quote of l. 2932-2933).

## 1. (a) Word-diff L-2 vs L-1
- Method: token pass (difflib on space-split tokens, each change read in context), then a byte test. I applied exactly the 7
  replacements below to L-1, each old phrase occurring exactly once; the result equals L-2 byte for byte: **True**.

| # | old (L-1) | new (L-2) | item (fixes entry 3 / C115) | ✓ |
| --- | --- | --- | --- | --- |
| 1 | «fixes §2.3) with bridge B,» | «… with RESULTS R103's bridge B,» | G-3 | ✓ |
| 2 | «(Lead reading L46 and its amendment), and with VJ00 local optimality (BRICS RS-00-48 Lemma 5.8 «1 ⇒ 2», the direction that holds, applied to Odd's one-player game against a fixed σ))» | «(Lead reading L46 and its amendment), applied at every Even vertex that is not its own W′-cycle node, non-movers included (RESULTS R103's (R1) ruling), and with local optimality in a one-player game (RESULTS R36 (c) Lemma P1, applied on the dual game to Odd's one-player game against a fixed σ; VJ00's two-player Lemma 5.8 is not used))» | G-3 (R1 clause) + E-1 | ✓ |
| 3 | «a Ξ-target that is a mover or X,» | «a Ξ-target xt(x, k), a mover or the exit X,» | G-2 | ✓ |
| 4 | «(2026-11-02; revision L-1 2026-11-02)» | «(2026-11-02)» | G-1 | ✓ |
| 5 | «Ξ-cyclic genomes are not covered, and random Ξ-cyclic genomes do mismatch;» | «Ξ-cyclic genomes are not covered;» | G-7 | ✓ |
| 6 | «DATA: per-lemma checks … on the 7 R178 champions (L 17 to 64), 2 R188 genomes,» | «DATA: random Ξ-cyclic genomes do mismatch; per-lemma checks … on the 7 L-RED R178 champions (L 17 to 64), 2 L-RED R188 genomes,» | G-7 + G-10 | ✓ |
| 7 | «(P-N5-REALIZE, docs/red/P-N5-REALIZE.md;» | «… docs/red/P-N5-REALIZE.md with its fixes entries 1-3, docs/red/P-N5-REALIZE-fixes.md;» | G-1 (source note) | ✓ |

- These are exactly the Lead's six items 1-6: E-1 (row 2b), G-3 in two places (rows 1, 2a), G-2 (row 3), G-1 (rows 4, 7), G-7 (rows 5,
  6) and G-10 (row 6). Nothing else changed.
- Everything L-1 carried for the joint REQUIRED list is untouched: the 1E-N3 gloss (P1, P2), the parity direction, the index layout and
  «top».

## 2. (b) R36 (c) Lemma P1 on G^d covers SBAR (ii): explicit confirmation
Let Γ_σ^d be G^d (owners swapped, Ω + 1) with every Γ-Even vertex (= G^d-Odd) restricted to its σ-edge, and ρ := «β_g at every gate,
K1 at K2».
- **Hypothesis class (one-player game).** R36's setting: «a game in which every non-Even vertex has one successor».
  - In Γ_σ^d the non-Even vertices are Γ's Even vertices, each with exactly its σ-edge.
  - The G^d-Even vertices are the gates and K2, with all their edges.
  - Every vertex has a successor.
  - The valuation is SPEC S1's on G^d's priorities, R36's setting.
  - ρ is a positional G^d-Even strategy. ✓
- **Orientation.**
  - A play value (c, P, ℓ) is the same tuple in G^d as in Γ. Ranks agree, the most relevant cycle vertex is the max-rank vertex in
    both, and P is rank-based.
  - G^d's order is the exact reverse of Γ's (Fact DUAL, §1; signed in R2-N5-REALIZE).
  - So R36's «no Even edge (o, w) with V_ρ(w) ▷_(G^d) V_ρ(ρ(o))» is «no Odd o, w ∈ succ(o) with φ(w) ◁ φ(ρ(o)) in Γ's order».
  - R36's conclusion «V_ρ(v) ⊵_(G^d) V_ρ′(v) for every ρ′ and v» is «φ_(σ,ρ)(v) ⊴ φ_(σ,ρ′)(v) in Γ's order»: ρ is Odd's pointwise
    optimum against σ. ✓
- **The «no improving edge» hypothesis.** That is exactly SBAR (i), proved at every G^d-Even vertex:
  - every gate: two edges; e_g is strictly worse for Odd at lev ≥ 1 (top e_g, even) and at lev 0 (even c_W);
  - K2: two edges; K2 → K2 is strictly worse for Odd (the longer play to the odd K1 is better for Even).
  - ✓
- **From «ρ optimal» to φ = Ξσ (SBAR (ii)'s conclusion), and (iii).**
  - Ξσ is the value of S1's σ̄, a pointwise optimum by 1E-N3 form P1 (RESULTS R67's form, «S1's σ̄ is Odd's pointwise optimum in
    G_σ»; L-2's gloss).
  - Two pointwise optima have equal keys at every vertex. The SPEC key is injective on values (p′ injective; P by its signed weight;
    then ℓ), so φ = Ξσ.
  - SBAR (iii) then runs unchanged.
- **C115's distinction is right.** R36 (c) supplies «no improving edge ⇒ optimal». 1E-N3 P1 supplies «Ξσ is the optimal value».
  These are two different premises with the same label «P1».
  - My report of record said «P1 on G^d … covered by the landed 1E-N3» for SBAR / TAU / K (c). That is correct only for the second
    role: TAU, K (c), «φ = Ξσ» and (iii).
  - The first role was [VJ-LOC]. I accepted [VJ-LOC] from L-LIT T21 (c), a lit note, not from RESULTS. R15 (iii) records 5.8 «1 ⇒ 2»
    as resting on VJ00's unproved Lemma 5.9 / Prop. 5.10. My row «premise [VJ-LOC]: only 1 ⇒ 2 is used ✓» was a wrong-route sign-off.
    It is corrected in R2-N5-REALIZE.md Addendum 2.
- **Independent data.** My BF probe (R2-N5-REALIZE §5, BF=11: 490,800 positional Odd strategies at 392 states) found ρ to be the
  UNIQUE pointwise optimum, with Ξ equal to the pointwise minimum, using no si.py. This is the conclusion R36 (c) gives, checked by
  enumeration.
- **No other route to VJ00 5.8 in the packet.**
  - 1E-N3 cites VJ00 §6 (S1's procedure), not 5.8.
  - R15's termination (used for L(G) finite) is R15 (d), which does not rest on 5.8 «1 ⇒ 2». That is R15 (iii)'s output-correctness
    half, not used here.
  - K (d), ESC, TAU use only the definition of a pointwise optimum and 1E-N3.
- **My SBAR signature stands with the re-route**, on [SPEC], RESULTS R36 (c) (on G^d) and 1E-N3 (P1).

## 3. The new (R1) clause (row 2a)
- **Wording.** L-2: «applied at every Even vertex that is not its own W′-cycle node, non-movers included (RESULTS R103's (R1) ruling)».
  This is R103's landed text in substance; trunk RESULTS R103, 1 match: «applied at every Even vertex that is not its own W′-cycle node,
  including non-movers ((R1) holds as a consequence of R24 (a) and (b)'s choice rule (both referees))». It is not a new premise:
  - the frozen packet's §1 [RULE] already says «Non-movers are covered ((R1) ruled «covered», RESULTS R103)»;
  - L-1 cited the same rule without naming its scope.
- **It is needed here.** REALIZE applies the rule at EVERY mover at every transition, not only at movers that switch:
  - at j < L, every mover with s_(j+1)(x) = s_j(x);
  - at transition L + 1, all movers, which is how σ_new = σ is shown.
  Those are non-movers in (R1)'s sense. Without (R1) the stop step and every kept mover would lack a carrier.
- **It is correct here.**
  - (R1) says TB steps 1, 3-5 describe one S1 call on dual(H) at every Even vertex that is not its own W′-cycle node. At a standard
    state the movers satisfy this: their W′-cycle node is c_W (Lemma W (iii)).
  - With fixes entry 1, the rule is read for S4a's σ_new before S4c (G-REAL-1 (b)), as (R1)'s «output of one S1 call» says.
  - My §3 direct trace of S1 (R2-N5-REALIZE) gives the same choice at movers, kept or switched, without the rule.
  - My checker's RULE counter runs at every mover of every state, kept or switched, and at the stop transition: 0 violations on 76,309 mover checks.
- **Scope.** «at every Even vertex» describes the cited rule's scope, as in R103; this packet uses it at movers only. That is harmless
  and accurate.

## Verdict
**MATCHES.**
- (a) L-2 = L-1 + exactly the six listed items (byte test True).
- (b) R36 (c) Lemma P1 on G^d covers SBAR (ii) in class, orientation and hypothesis (§2).
- The new (R1) clause is R103's landed ruling, already in the frozen packet's §1, and correct and needed here (§3).
- My signature of SBAR stands with the re-route, and all other signatures in R2-N5-REALIZE.md stand. My [VJ-LOC] row is corrected
  (Addendum 2).

## DONE / FINDINGS / NEEDS
- DONE: word-diff and byte test (True); R36 (c) coverage confirmed explicitly; (R1) clause checked; my own wrong-route row corrected.
- FINDINGS:
  - L-2 MATCHES.
  - CHECKER E-1 is right. My report had accepted VJ00 5.8 «1 ⇒ 2» from a lit note. Lesson: take every premise route from RESULTS,
    never from docs/lit.
- NEEDS: none.
