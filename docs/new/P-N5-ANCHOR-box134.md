# P-N5-ANCHOR (box 134): inside one W-flat run, N5 settles level by level between gating changes; FL-POLY ⟺ GCH-POLY — a referee packet from L-NEW boxes 130-133
Frozen 2026-11-01 (date -u: see the commit), L-NEW successor 46. For REFEREE and REFEREE-2 (Lead GO 15:36Z).
- Scope: REDUCTIONS / EQUIVALENCE and one DEAD with explicit instances.
  - No count is bounded here: neither FL nor GCH is bounded.
  - G-N5-TIME stays OPEN. This is not M3, not a step-4 pass and not a TARGET.md claim.
- Source notes (history only): docs/new/N5-FLAT-box130.md, N5-CANON-box131.md, N5-ANCHOR-box132.md (with §6), N5-ODXI-box133.md. This
  packet restates everything it uses; the notes are not needed to check it.
- To sign: §2 Lemmas FL-OPT, FL-TIGHT, bridge B; §3 Lemma PREFIX; §4 Theorem FL-ANCHOR; §5 Corollary FL-GCH (the equivalence) and Lemma
  CIRC; §6 the DEAD (instance checks). To rule on: §1 item (R1).
- Not to sign: §7 (DATA), §8 (READING).
- Line: docs/new/P-N5-ANCHOR-line.txt (one line, no heading marker).

## 1. Setting, premises
- N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) on an arbitrary game G, n := |V|, m := |E|.
  - A run is the sequence of states (σ_k, τ_k).
  - A transition j − 1 → j is a FALLBACK if S4c fired at it.
  - Values, ⊴, ◁, ▷ and ⊕ (prepending a vertex to a play's value) are as in SPEC S1.
  - Ξ_j := the valuation of σ_j under Odd's optimal counterstrategy σ̄_j. W_j := the valuation of the (σ_j, τ_j)-play.
  - Iσ_j := SPEC S2's improving set of σ_j.
- An FL RUN is a maximal set of consecutive transitions j − 1 → j (j = a + 1..b) such that each one:
  - is not a fallback;
  - has τ_j = τ_(j−1);
  - has σ_j ≠ σ_(j−1);
  - has W_j = W_(j−1) at every vertex.
  Its states are a..b, and W := W_a = … = W_b.
- Constant over an FL run (W is constant):
  - LEVEL ℓ(v) := the length component of W(v).
  - CN := {v : ℓ(v) = 0}, the W-cycle nodes.
  - For Even x ∉ CN, T_x := {y ∈ succ(x) : x ⊕ W(y) = W(x)}.
  - For Even c ∈ CN, T_c := {y ∈ succ(c) : the cycle node of W(y) is c}.
  - ℓ* := the largest level of an Even vertex ∉ CN (ℓ* := 1 if none).
- ODIFF_j := {o Odd : σ̄_j(o) ≠ τ_a(o)}. GATING DATA G_j := (σ̄_j on Odd vertices, Ξ_j on ODIFF_j, Ξ_j on CN).
  - An EPOCH of the run is a maximal set of consecutive transitions j − 1 → j whose GATING STATES j − 1 carry the same G.
  - GCH := the number of states j with a < j ≤ b − 1 and G_j ≠ G_(j−1).
  - CAP := (ℓ* − 1) + Σ_(c ∈ CN Even) (|T_c| − 1) ≤ n + m.
- Premises:
  - [1E-N3] The standing SPEC premise (RESULTS R57; R102 S4B-OPT under Lead reading L45). At a non-fallback transition j − 1 → j,
    σ_j is a pointwise optimum of the one-player arena H_(j−1), in which:
    - Even y keeps R_j(y) := {σ_(j−1)(y)} ∪ Iσ_(j−1)(y), i.e. σ_(j−1)(y) and every y' with Ξ_(j−1)(y') ▷ Ξ_(j−1)(σ_(j−1)(y));
    - Odd follows τ_(j−1).
    W*_j := the valuation of that optimum.
  - [RULE] (Lead reading L46; REFEREE 472f0dcd CF-1, REFEREE-2 d96d2f9e). Citing line: «RESULTS R24 (a) Lemma R and R24 (b)'s choice
    rule (TB proof steps 1, 3-5; fixes §2.3) with bridge B (§2 below); its proof uses no 𝒞^1O hypothesis».
    - Form used: for every Even x that is not its own W′-cycle node, σ_j(x) is the κ_j-least element of TIE_j(x).
    - TIE_j(x) := the FULLY W′-optimal options of x in H_(j−1), with W′ := W*_j. An option whose play passes x is a corner and lies
      outside the rule.
    - κ_j(y) := the index of y if x's W′-cycle node is odd. If it is even, κ_j(y) := the root-first key of y: the vertex sequence of the
      σ_j / τ_(j−1) play path from the cycle node c to y, c excluded, compared lexicographically by index.
  - (R1) — for the referees to RULE on, not a lane claim: [RULE] is applied at EVERY Even x ∉ CN of an FL transition, including x with
    σ_j(x) = σ_(j−1)(x). The choice rule is S1's output form, so it should cover non-movers. If it is read as movers-only, (R1) is a
    premise of §4.
  - VJ: Ξ is monotone, Ξ_(j−1) ⊴ Ξ_j pointwise along arena steps (VJ00; RESULTS R15 (a)). Used only in §8.

## 2. FL-OPT, FL-TIGHT, bridge B (PROVED, lane; proofs here)
- Lemma FL-TIGHT. In an FL run, σ_j(x) ∈ T_x for every Even x and every state j ∈ [a, b].
  - Proof, x ∉ CN: x is not its own cycle node, so x does not occur on the W_j-play from σ_j(x) before that play reaches x's cycle
    node, and W_j(x) = x ⊕ W_j(σ_j(x)). As W_j = W, this reads W(x) = x ⊕ W(σ_j(x)), i.e. σ_j(x) ∈ T_x.
  - Proof, x ∈ CN: the play from σ_j(x) returns to x, the cycle node of W(x), so W(σ_j(x)) has cycle node x. ∎
- Lemma FL-OPT. At an FL transition j, σ_(j−1) is a pointwise optimum of H_(j−1).
  - Proof: σ_(j−1) is a strategy of H_(j−1), since σ_(j−1)(y) ∈ R_j(y). Its valuation is W_(j−1) = W_j = W*_j. ∎
- Lemma (bridge B). At an FL transition j, let h be Even with h ∉ CN, o := σ_(j−1)(h) and w := σ_j(h) (w = o allowed). Then o and w are
  fully W′-optimal at h, and o, w ∈ TIE_j(h) ⊆ T_h.
  - Proof. h ∉ CN, so h lies on neither play (V1). Hence W_j(h) = h ⊕ W_j(w) and W_(j−1)(h) = h ⊕ W_(j−1)(o) = h ⊕ W_j(o), using
    W_(j−1) = W_j. So h ⊕ W_j(o) = h ⊕ W_j(w) = W*_j(h). Both options are in R_j(h) and attain h's arena optimum. TIE_j(h) ⊆ T_h because
    W′ = W. ∎

## 3. Lemma PREFIX (PROVED, lane)
- Let j be a state of an FL run and y ∉ CN. Follow the W-play from y up to its first vertex A ∈ ODIFF_j ∪ CN. Such an A exists within
  ℓ(y) steps, because the play reaches y's cycle node, which is in CN. Then:
  - (a) Up to A, the Ξ_j-play from y coincides with the W-play from y. Even vertices follow σ_j in both plays, and Odd vertices
    before A are not in ODIFF_j, so σ̄_j = τ there.
  - (b) Every vertex of the prefix p_0 = y, …, p_(k−1) other than y has level < ℓ(y), since the level drops by 1 per step of a W-play
    before its cycle node.
  - (c) Ξ_j(y) = F(p_0 … p_(k−1), Ξ_j(A)) for a fixed function F.
- Proof of (c). Let w be the cycle node recorded in Ξ_j(A). The Ξ_j-play from y ends in the same cycle, so its cycle node is w.
  - If w is one of the p_i, Ξ_j(y) is read off p_0 … w: the relevant set is the vertices of p_0 … p_(i−1) more relevant than w, and
    the length is i.
  - Otherwise the path from y to w is p_0 … p_(k−1) followed by A's path to w. The relevant set is the union of the prefix vertices
    more relevant than w with the set in Ξ_j(A). The length is k plus the length in Ξ_j(A). ∎

## 4. Theorem FL-ANCHOR (PROVED, lane, on §1 premises, [RULE], and (R1) as ruled)
Take an epoch of an FL run with first gating state s0 and last state s1.
- (i) For every ℓ ≥ 1, σ_j restricted to the Even vertices ∉ CN of level ≤ ℓ is constant for j ∈ [s0 + ℓ − 1, s1].
- (ii) After j = s0 + ℓ* − 1 only cycle nodes move, and each Even c ∈ CN moves at most |T_c| − 1 times in the epoch after that point.
- (iii) The epoch has at most CAP transitions. The run has at most CAP · (1 + GCH) transitions.

Proof of (i), by induction on ℓ.
- ℓ = 1: T_x = {c} for the cycle node c of x. A tight option has level 0 and cycle node c, so it is c. FL-TIGHT then fixes σ_j(x) = c.
- ℓ ≥ 2: let x ∉ CN have level ℓ, and j ∈ [s0 + ℓ − 1, s1]; then j − 1 ∈ [s0, s1 − 1] is a gating state of the epoch.
  - Values. Take y ∈ T_x ∪ {σ_(j−1)(x)}; y has level ℓ − 1. If y ∈ CN, Ξ_(j−1)(y) is gating data. Otherwise Lemma PREFIX writes
    Ξ_(j−1)(y) through σ_(j−1) at Even vertices ∉ CN of level ≤ ℓ − 1, through τ_a, and through Ξ_(j−1) at a vertex of ODIFF_(j−1) ∪ CN.
    The first is constant by induction (j − 1 ≥ s0 + ℓ − 2). The others are fixed in the epoch: ODIFF_(j−1) is a function of σ̄_(j−1).
    Write ξ(y) for this constant value.
  - Keys. κ_j(y) depends on σ_j at Even vertices ∉ CN of level ≤ ℓ − 1, on τ_a, and on indices, so it is constant too.
  - Choice. TIE_j(x) = R_j(x) ∩ T_x (bridge B and W′ = W). R_j(x) ∩ T_x = ({z} ∪ {y ∈ T_x : ξ(y) ▷ ξ(z)}) ∩ T_x with z := σ_(j−1)(x)
    ∈ T_x. By [RULE] and (R1), σ_j(x) = f_x(σ_(j−1)(x)), where f_x(z) is the κ-least element of that set.
  - f_x is idempotent. If z' := f_x(z) ≠ z, then ξ(z') ▷ ξ(z), so the set for z' is contained in the set for z (▷ is transitive) and
    contains z'. As z' is κ-least in the larger set and κ is injective, f_x(z') = z'.
  - Hence σ_j(x) = σ_(s0+ℓ−1)(x) for all j ∈ [s0 + ℓ − 1, s1]. ∎

Proof of (ii).
- For j − 1 ≥ s0 + ℓ* − 1 and y ∈ T_c, Ξ_(j−1)(y) =: ξ(y) is constant: by Lemma PREFIX and (i) when y ∉ CN, and as gating data when
  y = c (the only cycle node in T_c).
- A move of c at j has σ_j(c) ∈ R_j(c) \ {σ_(j−1)(c)}, so ξ(σ_j(c)) ▷ ξ(σ_(j−1)(c)), and σ_j(c) ∈ T_c (FL-TIGHT).
- A ▷-increasing sequence in the finite set ξ(T_c) has at most |T_c| − 1 steps. No rule at cycle nodes is used. ∎

Proof of (iii).
- Every FL transition changes σ.
- Transitions j ≤ s0 + ℓ* − 1 of the epoch number at most ℓ* − 1.
- Every later transition moves some cycle node, which by (ii) happens at most Σ_c (|T_c| − 1) times.
- The run splits into at most 1 + GCH epochs. ∎

## 5. Corollary FL-GCH and Lemma CIRC (PROVED, lane)
- Lemma CIRC. GCH ≤ FL − 1, where FL := b − a. Finer: Σ_(v ∈ ODIFF ∪ CN) #{j : Ξ_j(v) ≠ Ξ_(j−1)(v)} ≤ (|ODIFF| + |CN|) · FL, with
  ODIFF the union over the run.
  - Proof. A gating change at state j lies inside the run, a < j ≤ b − 1, which gives the first claim.
  - For the second: Ξ_j(v) is determined by the (σ_j, σ̄_j)-play from v. A change of Ξ at v between j − 1 and j therefore needs a
    change of σ or σ̄ on that play, and both happen only at transition j. Each transition is charged at most once per vertex. ∎
- Corollary FL-GCH (EQUIVALENCE). For every FL run, GCH ≤ FL − 1 and FL ≤ CAP · (1 + GCH) with CAP ≤ n + m. So over any family of
  runs, FL-POLY ⟺ GCH-POLY.
  - Neither side is bounded here.
  - Charging gating changes to the moves that cause them is CIRCULAR: substituting CIRC into §4 (iii) gives a vacuous bound.
  - The content is §4: inside an epoch, an FL run is a level-by-level settling of length ≤ CAP. The CDAG-type blow-up (box 130) can
    come only from in-run gating changes.

## 6. DEAD: «Ξ at ODIFF vertices is constant (or O(1)) inside an FL run»
Pins: Oink 8fbf0a7 --zlk and --tl verified, regions agree (box107/pinwin.py); n5b identical state by state; starts written out and
validated (D-ODD-1, strict start_pair).
- experiments/new/box133/odxi_n37.pg (sha1 83f263c1a4d0377041cd047c6adfc0343e68f02e), start odxi_n37.start (e2ed671588c71e8044ea8b4f7062baae918bec42). L-NEW gadget:
  u23sw64_n32 plus a band vertex 32, gates 33 → {2, 32} and 34 → {32, 36}, chooser 35, and pad 36.
  - In FL run [1, 9], Ξ at the ODIFF gate 33 changes 5 times.
  - One change releases the FL move 35: 34 → 33 at transition 5 → 6, with W(35) unchanged.
  - Check: box133/pincheck.txt; check.sh «box 133 ODXI».
- L-RED R179 instances (claude/l-red a612b0a5, copied read-only into experiments/new/box134/inst/; sha1 as in R179's pins.sha1):
  - odxi_min_n12 (51661a75a4ecef2225c970b8007faa9d0af2ee04, start 91ae8cad39b2cbec6f28c671c59e9ab1dd3f6d62): 𝒞^1O, ODIFF 1. One FL transition. The Ξ-change at the ODIFF vertex 10 is at the
    run's last state (Even 7 breaks Odd's cycle 10 → 7 → 10).
  - odxi_lasso_n13 (5cf187982d72f49e61bcbbbae68d612ec1912755, start c2a4e074f89270b550321b55a79ae5811d26aa4a): one FL transition. Lasso type: same cycle node, same length, path-set weight
    changes.
  - odxi_many_n32 (42094483eefdca2977396f563da134e09ce4839b, start c7565702c35945983b69b4981306e82e434bedb0): 3 FL runs, 8 transitions, 43 ODIFF Ξ-changes over run states, 4 gating changes.
    §4's items hold.
  - Check: box134/pincheck.txt; check.sh «box 134 P-N5-ANCHOR pins».

## 7. DATA (not to sign)
On the 813 distinct (game, start) pairs of experiments/si/anc58/corpus_fixed.lst (RESULTS Erratum E-1; box132/a_corpus.txt,
box133/o_corpus.txt; 0 script errors):

| quantity | value |
| --- | --- |
| FL runs / transitions / epochs | 20 / 42 / 23 |
| violations of §4 (i) timing, level ℓ − 1 targets, epoch ≤ CAP, run ≤ CAP (1 + GCH) | 0 / 0 / 0 / 0 |
| gating changes: Ξ at ODIFF / σ̄ / Ξ at cycle node only | 0 / 0 / 3 (cw11_n24) |
| ODIFF Ξ-changes over all run states | 2 (both at the last state of nep22f_n64's one-transition run, with and without start file) |

- Pins u23sw64_n32 (18b46837d2f0…) and cw11_n24 (5c6dcf2d9668…): box132/pincheck.txt.
- [RULE] DATA (box 131, the same corpus): BFS-key rule 666 / 666 (c even, non-corner), index rule 8 / 8 (c odd).
- L-RED R177 (claude/l-red 95ff289b): 435 flat non-corner moves, 0 violations.

## 8. READING (not to sign)
- §4 + CIRC + L-RED R178's Lemma XI-NEW: every new epoch is opened by an in-run Ξ-rise at a gate or cycle node, caused by an FL move
  of the same run. A long FL run is a self-sustaining loop of gate overtakes. What is missing is a non-circular potential for it
  (L-NEW box 134).
- Odd regime: R177 FL-IDX bounds each vertex directly.
