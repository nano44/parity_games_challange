# R143: T54's width-2 lex-BFS counter does not run inside one W-constant interval unless "upward events" pay for it. Lemma SETTLE (PROVED, lane): |I| ≤ (D + 1)(E_I + 1) − 1, where E_I counts the transitions of I at which σ̄ flips, a W-cycle node switches, or Ξ changes at an upward head. So INT-LIN holds on every event-free interval (|I| ≤ D ≤ n − 1). This is the exact S2 offer condition the abstract model drops. (b): CONJECTURE BIP-REL-1 is DEAD (rel2_R2_n82: 2 strict releases of one edge in one frozen stretch; family R at n ≈ 20R²)
L-RED successor 34 (Opus 5.5; D1/D18). Lead 2026-10-30 ~15:32Z, FIRST BOX R143 (a): «T54's width-2 lex-BFS counter realised inside ONE
W-constant interval of real N5 … Build them, or name the exact S2 offer condition that blocks them.» Written 2026-10-30 from 15:35Z
(date -u). Labels: PROVED (lane) / DATA / READING / DEAD. Not a TARGET.md claim. G-N5-TIME, [P-INT] and INT-LIN stay OPEN in general.
Sources: L-LIT T54 (l-lit 96cfda95, docs/lit/T54-stalling.md §4, T54-lexarena.py); L-SI box 51b (l-si a0d6f79b,
docs/si/N5-GATE-box51b.md §1 INTERVAL-SI, §8 LAYER-RESET, §10.1 Claim RG, §10.3 RETURN-CHARGE / INT-XCH). Lemmas used: Claim RG (L-SI,
lane-PROVED under R57's premise), LEX-BFS and IDX-MONO (L-LIT, PROVED modulo RG). Nothing else is imported.

## 0. Setting and symbols
- A W-run F (τ fixed, no S4c), and a W-constant interval I = [p, q] of F (wint.py definition: τ fixed, no fallback, σ changes, W equal at
  every vertex). W := W_p. layer(v) := the length component of W(v), fixed on I. C := {v : λ_W(v) = v} (layer 0).
- σ̄_k: SPEC S1's Odd counter-strategy to σ_k (n5b evaluate_choice). Ξ_k := val(σ_k, σ̄_k).
- UPWARD HEADS: U_k := {σ̄_k(g) : g Odd, σ̄_k(g) ≠ τ(g)} ∪ {the Ξ-successor of c (σ_k(c), or σ̄_k(c) if c is Odd) : c ∈ C}.
- EVENT: a transition k → k + 1 of I at which (i) σ̄ changes, or (ii) σ changes at some Even c ∈ C (a CN switch), or (iii) Ξ changes at some
  vertex of U_k ∪ U_(k+1). E_I := the number of events. A WINDOW is a maximal run of states of I with no event between consecutive ones.

## 1. Lemma SETTLE (PROVED, lane; modulo Claim RG, LEX-BFS, IDX-MONO)
- (A) Downward dependence. For a state k of I and a vertex y with layer(y) = d, Ξ_k(y) is a function of σ_k on the Even vertices of
  layers ≤ d, of σ̄_k, and of Ξ_k on U_k.
  - Proof. Follow y's (σ_k, σ̄_k)-play y_0 = y, y_1, … At an Even y_i ∉ C, σ_k(y_i) ∈ OPT_W(y_i) (INTERVAL-SI (i)), so the layer drops by 1. At
    an Odd y_i ∉ C with σ̄_k(y_i) = τ(y_i), τ is W-tight (W = val(σ_k, τ)), so the layer drops by 1. Let h = y_i be the first vertex that is
    in C or is an Odd vertex with σ̄_k(h) ≠ τ(h). Then y_(i+1) ∈ U_k. Every VJ value on a play is (cycle node w, relevant vertices of the
    path to w, distance to w). If w is not among y_0 … y_i, then Ξ_k(y) = y_0 ⊕ … ⊕ y_i ⊕ Ξ_k(y_(i+1)). If w = y_j (j ≤ i), Ξ_k(y) is fixed
    by y_0 … y_j and the cycle node of Ξ_k(y_(i+1)). In both cases it is a function of the segment y_0 … y_i (σ_k on layers ≤ d) and of
    Ξ_k(y_(i+1)). □
- (B) Settling. In a window starting at state k0, an Even x ∉ C of layer d switches at a transition k → k + 1 only if k ≤ k0 + d − 1.
  - S4a's choice at x (Claim RG). σ_(k+1)(x) is the minimum, over the W-tight edges of {σ_k(x)} ∪ Iσ_k(x), of an order ≺ on x's tight
    successors (layer d − 1):
    - EVEN branch (λ_W(x) of even priority): ≺ is the lex order of key_(σ_(k+1)) (LEX-BFS);
    - ODD branch: ≺ is the static index order (IDX-MONO).
    In both cases ≺ depends only on σ_(k+1) on layers ≤ d − 1. Keys of distinct vertices differ in their last coordinate, so the minimum
    is unique.
  - Induction on d. Assume that layers < d have no switch at transitions k ≥ k0 + d − 1 (d = 1: layer 0 is C, constant in a window).
    Then on the states [k0 + d − 1, k1], σ on layers ≤ d − 1 is constant. Within the window σ̄, U and Ξ|U are constant. So by (A) the Ξ-values
    and the ≺-order of x's successors are constant there.
  - Let k ≥ k0 + d. If x switched at k − 1, then Ξ(σ_k x) ▷ Ξ(σ_(k−1) x), so Iσ_k(x) ⊆ Iσ_(k−1)(x). If it did not switch, then
    Iσ_k(x) = Iσ_(k−1)(x). Either way {σ_k(x)} ∪ Iσ_k(x) ⊆ {σ_(k−1)(x)} ∪ Iσ_(k−1)(x), and that set contains σ_k(x), its ≺-minimum. So x
    does not switch at k. □
- (C) Count. Every transition of I switches some Even vertex. Inside a window only vertices outside C switch (a CN switch is an event).
  So a window has at most D := max{layer(v) : v switches in I} transitions, and |I| ≤ E_I + (E_I + 1)·D = (D + 1)(E_I + 1) − 1. □
- Corollary INT-LIN-EF (PROVED, lane). An event-free W-constant interval has |I| ≤ D ≤ n − 1. That covers in particular every interval
  with σ̄ frozen, no CN switch and every upward head's Ξ constant.
- Corollary SETTLE-RED (PROVED, lane). E_I ≤ SBF_I + CN_I + Σ_(u ∈ U*) XCH_I(u), where U* := ∪_k U_k (|U_k| ≤ #Odd + |C|), SBF_I is the
  number of σ̄-changing transitions and CN_I the number of CN switches. Hence [P-INT] ⇐ «in-interval Ξ-changes at upward heads, σ̄-flips
  and CN switches are polynomial».
  - This sharpens L-SI's INT-XCH (Σ over EVERY vertex d, weighted by its in-degree) to the heads alone.
  - It replaces CONJECTURE LAYER-RESET's mixed-radix bound Π_d(1 + m_d) by a product (D + 1)(E_I + 1).

## 2. The answer to (a): the S2 offer condition that blocks the counter
- In T54's LEX-ARENA the adversary may WITHHOLD an offer: it can give x the arena {σ(x)} while a lex-smaller successor is already better,
  and offer it later. That delay is the whole source of 2^(L+1) − 2L − 2.
  - Once the lower layers are fixed, LEX-ARENA too lets a layer settle in one move: its lex-min is unique. The adversary gets length only
    by delaying lower layers.
- S2 cannot withhold. Iσ_k(x) is exactly the set of Ξ-better successors, and by (A) between events it is a function of the lower layers
  alone. So an offer at layer d appears or disappears only through a lower-layer switch or an event. After the lower layers settle, it
  is stationary. This is the exact condition (B) uses.
- Consequence. T54's run of length 2^(L+1) − 2L − 2 has D = L. Realised in one interval of N5, it needs
  E_I ≥ (2^(L+1) − 2L − 1)/(L + 1) − 1 events. With |U_k| ≤ n, some upward head needs exponentially many in-interval Ξ-changes, or σ̄
  must flip exponentially often, or a W-cycle node must switch exponentially often.
  - This is consistent with RETURN-CHARGE (each carry raises the returned-to vertex's Ξ), but stronger: Ξ-rises of vertices that are not
    upward heads buy at most D transitions per window.
- So the counter is not built. The obstruction is named: a kill needs an UPWARD FEEDBACK loop, a low gate g whose deviation target σ̄(g)
  sits higher and whose Ξ keeps changing as the middle layers settle, re-opening the settling below g exponentially often.

## 3. Model FT (frozen trap) and the u23sw64 anatomy (DATA)
- u23sw64_n32 (L-SI's longest interval, [1, 9], 8 transitions):
  - W-cycle node 13 has the top priority (30), so W-tightness is lengths only (all W path sets ∅).
  - One frozen deviation 27 → 20 (σ̄ never flips, SBF 0) closes a Ξ-cycle at 20 (priority 6). Relative to 20 almost every vertex is
    relevant, so Ξ is a 2^rank-weighted path potential.
  - The deviation is not Odd-improving because the dual valuation ties: W*(20) = W*(3) = 5 (It = ∅). Current W lengths are 8-10.
  - U = {20} with Ξ(20) constant, so the interval is event-free: E_I = 0, D = 10, |I| = 8 ≤ D.
- Model FT (lexc/ftmodel.py) idealises exactly this:
  - a length-layered Even DAG, layer j → every vertex of layer j − 1;
  - Ξ(x) = w(x) + Ξ(σ x), w = ±2^rank;
  - S4a in-interval step: lex-min key over {σ(x)} ∪ {Ξ-better tight successors}, new keys layer by layer.
  - Search: exhaustive over ranks, signs and starts (L = 2, 3); random over ranks, signs, starts and index orders (0.3-1.2 M tries each).

  | L (width) | 2 (2) | 3 (2) | 4 (2) | 5 (2) | 6 (2) | 8 (2) | 3 (3) | 4 (3) | 6 (3) |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | FT longest run | 1 (exh.) | 2 (exh.) | 3 | 4 | 5 | 5 | 2 | 3 | 5 |
  | T54 LEX-ARENA (adversarial) | 2 | 8 | 22 | 52 | 114 | — | 15 | — | — |

  FT is event-free by construction, so SETTLE gives ≤ L − 1 (layer 1 never moves). The data meet the bound exactly up to L = 6.
- Template search in real N5 (lexc/lexsearch.py: width-2 DAG, an Odd gadget on every tight edge, random deviations, markers, free
  vertices): longest interval 1 in 16,750 tries at n 22. As R141 found, random W-constant intervals are short.

## 4. Lemma SETTLE on real N5 traces (DATA, lexc/settle.py, lexc/run.sh)
- Checked on box 50b's corpus (L-SI lists: sbcg 719 + alt 413 runs, 300 s each). Two alt entries (n3cov_lean, n3cov_phi) have partial
  start files (R99 erratum); they were re-run on their _fixed.start (no interval).
  - (B) violations: 0. |I| > (D + 1)(E_I + 1) − 1: 0.
  - E_I = 0 on every interval of 1125 of the 1132 runs. Every interval with |I| ≥ 2 and E_I = 0 has |I| ≤ D (max 8 at D = 10, u23sw64).
  - E_I > 0 only on nep13_n24, nep22f_n64, tog6a/b_n32 (|I| = 1) and cw11_n24 ([3, 3, 0] and [2, 2, 0]: every transition a CN switch,
    D = 0).
- Multi-window intervals (an event that re-opens settling at D ≥ 1): hill-climb from the corpus's longest-interval games
  (lexc/winsearch.py, 900 s each).
  - Results, best (windows, |I|) per seed: u23sw64_n32 (4, 7); u1t_own6_n32 (3, 6); u1t_cex_n32 (2, 4); u2flat73_n32 (2, 3). About 40k
    tries each.
  - Pin lexc/winseed_u23_n32 (default S3 start written to .start): |I| = 7, E_I = 3, D = 9, 4 windows, VIOL 0. xeng identical, Oink OK.
  - Events therefore exist and do re-open settling. But no search produced a window longer than a few transitions after an event, nor E_I
    beyond 3.

## 5. Target (b): CONJECTURE BIP-REL-1 is DEAD (rel2/mkrel2.py; DATA, exact, two engines + L-NEW's own counter + Oink)
- The design follows L-NEW box 90's one-line obstruction literally («a climb below τ(o) raises W(z) and not Ξ(z), a later climb below ρ(o)
  raises Ξ(z)»). The missing ingredient was a clock: plain one-player delay chains.
  - D(k, lo, hi): v_k … v_1 Even, v_i → {s_i, v_(i−1)}, increasing stay markers. v_i adopts v_(i−1) at transition i − 1 → i, because offers
    use the old Ξ, so the top's value rises from lo to hi exactly at state k. Chains with no Odd vertex have Ξ = W, so every switch is a
    plain W- and Ξ-improving switch.
- Gadget.
  - Sink c (Even, priority 0, self-loop), so every other vertex is relevant and values are signed 2^rank path sums.
  - y → {z, h} with σ_0(y) = h. z = o_z, an Odd vertex → {A, B} with τ(o_z) = B, so W(z) reads B.
  - Odd's reply ρ(o_z) = A (Ξ(z) reads A) as long as Ξ(A) ⊲ Ξ(B).
  - A, h, B are nested delay chains with value levels h_i < a_(i+1) < b_i < h_(i+1). A's last level lies above B's last, so
    W*(A) ⊵ W*(B), Iτ = ∅ and τ never moves.
- Run (R = 2, states 0-10). For y, a block means W(z) ▷ W(h) with Ξ(z) ⊴ Ξ(h).
  - Block at 0. A rises at 1, and y adopts z at 1 → 2 (strict release 1).
  - h rises at 3, and y leaves for h at 3 → 4. B rises at 5 (block again).
  - A rises at 7, and y adopts z at 7 → 8 (strict release 2). A passes B at 10, so σ̄ flips only there.
  - One W-run (τ fixed), no fallback, σ̄ constant on [0, 9].
- Timing obstruction met and solved: rises must be ≥ 2 iterations apart. At gap 1, ARENA-MAX's look-ahead (R140) already sees h's next
  offer: the arena valued h at m50 > W(z) = m40, so y never took z (first build, 1 release).
- DATA (strictrel.py = L-RED R142b; relpe.py STRICT=1 = L-NEW box 89's own counter on its n5x engine; xeng; Oink zlk + verify):

  | pin | n | iterations | strict releases of (y, z) in one frozen stretch | relpe frozen_edge | xeng | Oink |
  | --- | --- | --- | --- | --- | --- | --- |
  | rel2/instances/rel2_R2_n82 | 82 | 10 | 2 | 2 | identical | OK |
  | rel2/instances/rel2_R4_n322 | 322 | 22 | 4 | 4 | identical | OK |
  | (generator only) R = 3, 6 | 183, 714 | 16, 34 | 3, 6 | — | — | — |

- DEAD: CONJECTURE BIP-REL-1 (≤ 1 strict release per edge per frozen stretch). Instance rel2_R2_n82, edge (y, oz).
  - The family gives R strict releases of ONE edge in ONE stretch at n ≈ 20R², so R° ≥ ⌊√(n/20)⌋.
- What survives (READING). BIP-RED's conclusion needs only R° ≤ p(n), and this family is polynomial (R ≈ √n). So BIP-POLY and BIP-RED's
  route are not killed. Only the per-edge constant 1, and with it the bound R° ≤ m_E, is dead.
  - Every release here costs a fresh delay chain, about 6 vertices per iteration of clock. That is the familiar clock × chain wall: a
    super-polynomial R° would need a clock whose rises are not paid by fresh vertices.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/red/lexc/ (settle.py, run.sh, settle_sbcg.txt, settle_alt.txt, settle_fixed.txt, ftmodel.py,
  lexsearch.py, winsearch.py, pin winseed_u23_n32); experiments/red/rel2/ (mkrel2.py, trace.py, oinkcmp.sh, pins rel2_R2_n82,
  rel2_R4_n322, pins.sha1); check.sh "R143"; notes/L-RED.md.
- FINDINGS:
  1. PROVED (lane, modulo RG / LEX-BFS / IDX-MONO): Lemma SETTLE, |I| ≤ (D + 1)(E_I + 1) − 1. Corollary INT-LIN-EF: INT-LIN holds on
     every event-free W-constant interval. Corollary SETTLE-RED: [P-INT] ⇐ polynomial in-interval Ξ-changes at upward heads + σ̄-flips +
     CN switches.
  2. (a) not built. The S2 condition that blocks T54's counter: offers cannot be withheld, so between events a layer settles one step
     after the layers below it. The counter needs ≥ (2^(L+1) − 2L − 1)/(L + 1) − 1 upward events in one interval.
  3. DATA: model FT (frozen trap, downward-only Ξ) has longest run L − 1 (exhaustive L ≤ 3, random L ≤ 8), against T54's 2^(L+1) − 2L − 2.
  4. DATA: SETTLE checked on 1132 corpus runs, 0 violations; 1125 runs are event-free on every interval. The search pin winseed_u23_n32
     has 4 windows (E_I = 3).
  5. DEAD (b): CONJECTURE BIP-REL-1. rel2_R2_n82 has 2 strict releases of one edge in one frozen stretch, rel2_R4_n322 has 4, and the
     family gives R at n ≈ 20R². BIP-POLY is not killed (R ≈ √n).
- NEEDS: none from the owner.
