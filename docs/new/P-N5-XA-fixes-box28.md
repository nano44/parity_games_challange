# P-N5-XA fixes (box 28): the referees' repairs, written out
L-NEW successor 10 (Opus 5.5, D15/D18). Lead GO 2026-10-24 16:18Z. Written 16:21Z-16:40Z (date -u).
- Object: packet docs/new/P-N5-XA-box27.md, pinned at trunk b70aa59, sha1 832d0da2b45bcc0850929b0f614bb1d9b19ed7b3. The packet is NOT
  edited; this file is the correction layer.
- Sources:
  - REFEREE: docs/referee/R-N5-XA.md §1-§9 and §C1-§C6 (referee f39972d, 1123baf).
  - REFEREE-2: docs/referee-2/R2-N5-XA.md §1-§8, §C and §C2 (referee-2 9d3f1fb, 4df15e63, and the C2 commit).
- Rule for this file: it writes down the referees' repairs. Where I add a line of my own, it is marked "L-NEW". Nothing here is
  new mathematics beyond what the two reports state, except where marked.
- Labels (L40): SIGNED (both referees, "(Opus 5.5, D15)"), OPEN, READING.
- Scope:
  - These are lemmas about the candidate N5 on 𝒞^1O inside a throttled stretch S with (h) at every state.
  - They are not a running-time bound for N5, not a TARGET.md claim, and not a step-4 pass. G-N5-TIME stays OPEN.
  - Not covered: states without (h); u* = none (for FBL, XA and the Corollary); the number of throttled stretches; (CYC'), (NH),
    (XING), (FB-1O).
Notation: as in the packet §0-§1 (S, c, u*, V*, COARSE, ⪯, R_k, F_k, π_v, θ, w, gate = Iσ_k, (V1), (V2), (F1), R15 (a), (d)).

## Summary: final status per item (joint position: REFEREE §C6, REFEREE-2 §C2.4)
| packet item | final status | text below |
| --- | --- | --- |
| §1 setting, Lemma C | SIGNED as written | — |
| Lemma FBL | SIGNED for u* ≠ none, in the strong gate form; u* = none OPEN | §1 |
| Lemma FBF | SIGNED for every u*, with the repaired step 1 | §2 |
| Lemma P^c / CR | SIGNED; wording XA-3, XA-4; B-fallback case vacuous (N-XA-1) | §3 |
| Theorem XA | SIGNED; sharper count ≤ n − 1 per vertex (N-XA-2); no end-to-end data | §4 |
| Corollary | SIGNED by REFEREE-2 (§C2.3) in the form of §6, given the texts of §5 and §6 below; REFEREE's §C5 gives the same closure of XA-5 | §5, §6 |

## 1. Lemma FBL, replaced (gaps XA-1 = G-XA-1 (a), G-XA-1 (b))
Statement (replaces packet §3). Let S be a throttled stretch with **u* ≠ none**, and let k → k+1 (k, k+1 ∈ S) be an S4c fallback. Then:
- (gate form) at k the gate has no R → R edge and no F → R edge; every gate edge is either a LEAVE (x ∈ R_k, z ∈ F_k) or a flat F → F
  edge (x = λ(x), z in x's region; switching it changes no value);
- hence every edge the fallback switches is a leave or a flat F → F edge.
Proof.
1. Packet step 1 is unchanged. τ is constant on S, so the fallback is Even's, and σ_k is a pointwise optimum of the S4a arena in G_τ. By
   the flat-case analysis (R18 (c)), every W-improving gate edge is flat.
2. R → R, F → F and R → F are as in the packet.
3. F → R (this replaces the packet's text, which is not a proof; see "Why" below). Let (x, z) be an F → R gate edge at k.
   - It is W-improving, as in the packet: π_z ⊕ w ⊵ π_z ⊕ θ ▷ W_k(σ_k(x)). So it is flat: x = λ(x), and z's W-play ends at x. z's W-play
     ends at c, so x = c.
   - Flatness means the cycle c → z → π_z → o → … → c has D = ∅ (R17 B2). So P(W_k(z)) = A_z ∪ P(w) = ∅, and in particular P(w) = ∅.
   - (x, z) is in the gate, so Ξ_k(z) = (c, P(θ), ·) ▷ Ξ_k(σ_k(c)) = (c, ∅, ·). That needs P(θ) = ∅ or a top of P(θ) that is even.
   - An even top would give θ ▷ w (since P(w) = ∅), against θ ◁ w. So P(θ) = ∅ = P(w), which is u* = none, against the hypothesis.
   So there is no F → R gate edge. □
- Why the packet's F → R text fails (both referees):
  - (a) c's best gate edge by (Ξ-key, index) may be a flat F → F edge. Then an F → R gate edge exists at k without being switched.
  - (b) If c does switch to z ∈ R_k, a vertex of π_z may leave R in the same fallback. Then c → z does not lead back to o at k+1, and
    (h) at k+1 is not contradicted.
- **OPEN: u* = none.** FBL's statement is unproved there. The configuration not excluded is: c odd, P(θ) = P(w) = ∅, θ ◁ w by length only,
  z's route above c empty, and (o, σ̄(o)) ∉ Iτ. Then the switched edge (c, z) with z ∈ R_k \ R_{k+1} is neither a leave nor a flat F → F
  edge.
  - No instance is known: REFEREE found 12 u* = none stretches and REFEREE-2 found 44, with 0 fallbacks inside any of them. REFEREE-2 also
    ran climbs aimed at this case.
  - No proof is known either.
  - Downstream effect: none. FBF holds for every u* (§2), CR does not use FBL (§3, N-XA-1), and XA and the Corollary assume u* ≠ none.

## 2. Lemma FBF, step 1 replaced (gap XA-2 = G-XA-2)
The statement is unchanged and holds for **every** u*: after an S4c fallback L → L+1 inside S, for every state t ≥ L+1 of S, R_t ⊆ R_{L+1}
and every v ∈ R_t has its L-path (hence its L-route value). In particular no vertex enters R after L inside S.
Proof (REFEREE-2's (h) base plus REFEREE's best-key inductive step).
0. (h) base (REFEREE-2 §3, §C.4): **c ∉ R_t at every state t of S.**
   - c is w's cycle node and w is constant on S, so o's W-play at t reaches c.
   - If c ∈ R_t, then c's σ_t-path leads to o, so o's W-play returns to o. That contradicts (h) at t.
1. The transition L → L+1.
   - At L the only possible gate edges into R_L come from c. R → R gate edges do not exist (FBL step 2). An F → R gate edge is W-improving,
     hence flat, hence starts at c (§1 step 3, first bullet; this part needs no u* hypothesis).
   - Let v ∈ R_{L+1} with (L+1)-path v = p_0, …, p_m = o. Suppose some p_i switched at L, and take the largest such i.
     - p_{i+1}, …, p_m did not switch, so p_{i+1} ∈ R_L ∪ {o}. So p_i switched along a gate edge into R_L ∪ {o}.
     - Odd vertices never switch (τ is constant), so p_i is Even. A switched edge into R_L must start at c, so p_i = c.
     - But p_i ∈ R_{L+1}, against step 0.
   - So no p_i switched: v's path is its L-path, and v ∈ R_L. This gives R_{L+1} ⊆ R_L with unchanged paths, for every u*.
2. Best-key fact (REFEREE §4). After the fallback at L, every Even y satisfies Ξ_L(σ_{L+1}(y)) ⊵ Ξ_L(z) for EVERY successor z of y.
   - If y had no gate edge, then σ_{L+1}(y) = σ_L(y) and no successor improves on it.
   - If y had one, S4c switched y to z* of maximal Ξ_L-key among its gate edges. Every other successor is either a gate edge (Ξ_L(z) ⊴
     Ξ_L(z*)) or not (Ξ_L(z) ⊴ Ξ_L(σ_L(y)) ◁ Ξ_L(z*)).
3. Induction for t ≥ L+1 (claim: no gate edge at t points into R_t, R_{t+1} ⊆ R_t, and paths are unchanged).
   - Assume R_t ⊆ R_{L+1} ⊆ R_L with L-paths. Then for z ∈ R_t, Ξ_t(z) = Ξ_L(z): the path is the same and θ is the same (Lemma G (b) under
     (h) at t).
   - For every Even y, Ξ_t(σ_t(y)) ⊵ Ξ_{L+1}(σ_{L+1}(y)) ⊵ Ξ_L(σ_{L+1}(y)) ⊵ Ξ_L(z) = Ξ_t(z).
     - The first step holds because the successor value of y never falls: an unchanged successor keeps or raises its value by R15 (a),
       and a switch is along a gate edge.
     - The second step is R15 (a); the third is step 2.
   - So (y, z) is not a gate edge, for any y, c included. S4a and S4c switch only gate edges. The "largest switched p_i" argument of
     step 1 (now with no excluded edge at all) gives R_{t+1} ⊆ R_t with unchanged paths. □
- Either inductive step works: the packet's own (for y ≠ c, with step 0 keeping c out of R) or REFEREE's best-key form above.

## 3. Lemma P^c / Lemma CR: wording (XA-3, XA-4) and N-XA-1
- **XA-3** (packet §5, "B1, x ∉ π, x on c′'s cycle"). W-improvement allows a third case besides (α) and (β):
  - (γ) P(π) = ∅, c′ even, and |π| + 1 shorter than x's current length.
  - Then val_σ̂(x) = (c′, ∅, |π| + 1) = x ⊕ Ω_k(z). The chain of (β) and of the first B1 sub-case concludes: Ω^c_{k+1}(x) ⪰
    x ⊕_c Ω^c_k(z) ⪰ COARSE(value(r)).
  - Inherited from R17's text (R-N5-1P G2, R-N5-1OA B7). The conclusion is unaffected.
- **XA-4** (packet §5, Case A_c). For an Odd vertex x (forced, or o with τ constant on S), σ_k(x) is read as x's only current successor
  τ(x). The only z with an edge (x, z) used by a path r of G_τ is that successor. So Case A_c holds with equality, and A1/A2 apply as
  written.
- **N-XA-1** (REFEREE-2 §4, accepted by REFEREE §C4): case B-fallback is VACUOUS.
  - At a fallback, σ_k is the arena optimum in G_τ, so every W-improving gate edge is flat.
  - A flat edge is coarse-equal: same cycle node x, empty path sets on both sides, length ignored.
  - A coarse-strict edge is W-improving ((Cstrict) with Lemma C), so it cannot exist at a fallback.
  - The packet's B-fallback text is correct but covers an empty case. So **Lemma CR does not depend on FBL**, and the u* = none gap of §1
    does not touch CR.

## 4. Theorem XA: count (N-XA-2)
The statement and proof are SIGNED as written (u* ≠ none). The count is sharper per vertex:
- the intervals (L, E+1] of one vertex x are disjoint;
- each contains a strict coarse increase of x;
- Lemma CR confines the strict coarse increases to the first n − 1 transitions of S.
So x has ≤ n − 1 such re-entries, and S has ≤ n(n − 1) in all.
- DATA caveat (both referees): no re-entry after an S4a leave inside a throttled stretch has been observed. REFEREE ran 26,483 random runs
  plus 25 named instances; REFEREE-2 ran 16,672 runs plus climbs. XA rests on the proof alone. REFEREE-2 checked its order core (steps 4-5)
  on 6,446 real route pairs, with 0 failures.

## 5. Pieces pass through flat fallbacks (closes XA-5; REFEREE §C5, REFEREE-2 §C.5 and §C2.2)
Claim. Inside S with u* ≠ none, let k → k+1 be a fallback that switches no leave (a FLAT fallback). Then PIECE's two arena runs (on 𝓡*,
P-1 form, and on 𝓕) continue through k → k+1 as value-flat steps. So a piece may be taken as a maximal run without crossings and without
NON-flat fallbacks, and it still has ≤ (|R| − 1) + (|F| − 1) ≤ n − 2 value-changing transitions.
Proof.
1. The flat fallback changes no value and touches neither R nor (h).
   - By FBL (§1, u* ≠ none), every switched edge is a flat F → F edge (x = λ(x), z ∈ F in x's region). Distinct switched x have disjoint
     regions, so W and Ξ are unchanged on F.
   - On R nothing switches.
   - If c itself switches, its new cycle lies in F (z ∈ F does not reach o). So o's plays still stop at their first visit of c, θ and w
     are unchanged, and o stays off every cycle: (h) holds at k+1.
   - No F-vertex is redirected towards o, so R is unchanged.
2. R17's Lemma P invariant (R17 §2: Ω_k(x) ⪰ value(r) for every simple r of ≤ j edges, j = the number of arena steps so far) is a
   statement about the values at the current state. Its induction step k → k+1 (cases A1, A2, B1 including (γ) of §3, B2) uses only:
   - the values and the strategy at k;
   - (V1) for that strategy;
   - (F1) for that step's arena, which is built from Iσ_k and the current σ_k.
   It never uses how σ_k arose. After a flat fallback the invariant holds with the same j (values unchanged), and the next arena step runs
   with the post-fallback σ. The same holds on 𝓕 and on 𝓡*.
3. Equivalent view (REFEREE-2 §C.5): σ_{k+1} has the same values as σ_k and differs only along gate edges, which on F are 𝓕-improving
   (Lemma G (a)). So σ_{k+1} is another pointwise optimum of the arena at k. R17 (d) holds for every pointwise-optimal choice, so the flat
   fallback is a legitimate value-flat switch-best step of both piece runs. □
- So flat fallbacks are not separators, and the circularity of XA-5 is gone. REFEREE-2 checked this text: SIGN (§C2.2).
- DATA (REFEREE-2, piece_flatfb.py): 1,052 pieces, 0 violations; 64 pieces contain a flat fallback.
  - This is weak evidence: those pieces have only 10 value-changing steps in all.
  - Throttled stretches had no flat fallback at all: all 576 fallbacks in them contained leaves.

## 6. Value-preserving runs (N-XA-3) and the Corollary as signed
- **N-XA-3** (R15 (d)). R15 (d) (RESULTS "### R15"): "at most 4n(n−1) consecutive N5 iterations leave both Ωσ and Ωτ unchanged".
  - L-NEW: on S, τ is constant, so Ωτ (which depends on τ alone) is unchanged.
  - L-NEW, definition. A transition of S is VALUE-CHANGING if it changes Ξ or W at some vertex, and VALUE-PRESERVING otherwise.
    A value-preserving transition leaves Ωσ = Ξ and Ωτ unchanged, so R15 (d) applies directly.
  - L-NEW, why the definition is needed. At a transition with NO crossing, Ξ changes iff W changes:
    - on F, Ξ = W (Lemma G (a));
    - on R (the same set at k and k+1), Ξ(v) = π_v ⊕ θ and W(v) = π_v ⊕ w with θ, w fixed. Both are unchanged iff (A_{π_v}, |π_v|) is
      unchanged (Lemma G (b)).
    At a crossing transition this can fail. If x leaves R and W_{k+1}(x) = W_k(x) = π_v ⊕ w, then Ξ_{k+1}(x) = W_{k+1}(x) ≠ π_v ⊕ θ =
    Ξ_k(x). So W-flat does not imply Ξ-flat there.
  - The count in (iv) below therefore counts transitions changing Ξ or W. Inside a piece (no crossing) the two notions coincide, and
    PIECE's bound applies to both. Crossing and non-flat-fallback transitions are counted separately in any case.
  - Hence every run of value-preserving transitions of S has length ≤ 4n(n − 1). In REFEREE-2's wording (§C2.3) "value-changing" is
    not defined; this definition makes its step (v) exact.
- **Corollary** (replaces packet §7; SIGNED by REFEREE-2 §C2.3 in this form; REFEREE's §C5 gives the same closure and its §C6 leaves only
  the REFEREE-2 check open, now given). Let S be a throttled stretch with **u* ≠ none** and (h) at every state. Then:
  - (i) entries into R ≤ n + n(n − 1) = n². All entries come before S's first fallback (FBF, §2). Re-entries there follow S4a leaves, so
    XA applies (≤ n(n − 1)), and first entries number ≤ n.
  - (ii) leaves ≤ entries + n. So crossing transitions number ≤ 2n² + n.
  - (iii) every non-flat fallback contains a leave (FBL, §1). So non-flat fallbacks number ≤ n² + n.
  - (iv) value-changing transitions (Ξ or W) ≤ (n − 2)·(X + N + 1) + X + N ≤ (n − 1)·(X + N + 1) = O(n³), where X = #crossing
    transitions and N = #non-flat fallbacks.
    - There are ≤ X + N + 1 pieces, each with ≤ n − 2 value-changing transitions. This is PIECE through flat fallbacks (§5), with P-1
      and P-2 (inside one joint λ-phase).
    - The X + N separating transitions are counted once each.
  - (v) all transitions of S ≤ (#value-changing + 1)·(4n(n − 1) + 1) = O(n⁵) (N-XA-3).
  So S has O(n³) crossings, non-flat fallbacks and value-changing transitions, and O(n⁵) transitions.
- Not covered:
  - u* = none stretches (FBL's u* = none gap, and XA step 4);
  - non-(h) states;
  - the number of throttled stretches per joint λ-phase. This is (CYC'), θ- and w-changes per phase; with (NH) it is the remaining part of
    the box-27 reduction (READING).
  G-N5-TIME stays OPEN.

## 7. Gap ledger (both reports)
| id | where | final |
| --- | --- | --- |
| XA-1 = G-XA-1 (a) | FBL F → R: c's best gate edge may be in F | CLOSED for u* ≠ none (§1, strong gate form) |
| G-XA-1 (b) | FBL F → R: z's route may leave in the same fallback | CLOSED for u* ≠ none (§1); **OPEN for u* = none** |
| XA-2 = G-XA-2 | FBF step 1 premise | CLOSED for every u* (§2) |
| XA-3 | P^c B1 omits (γ) | CLOSED, wording (§3) |
| XA-4 | P^c Case A for Odd vertices | CLOSED, wording (§3) |
| N-XA-1 | CR B-fallback vacuous | remark; CR independent of FBL (§3) |
| N-XA-2 | XA count ≤ n − 1 per vertex | remark (§4) |
| XA-5 | Corollary: flat fallbacks as PIECE separators | CLOSED by §5 (REFEREE §C5; REFEREE-2 §C2.2 SIGN) |
| N-XA-3 | value-preserving runs ≤ 4n(n − 1) | written (§6) |
