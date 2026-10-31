# N5-DESCSTAR (box 113): which descents count — witness by switches, every descent copies a ROOT descent, root descents are fuel re-routes or relays
L-NEW successor 42, 2026-10-31 (date -u: started 13:04Z). Lead brief 13:0xZ: DESC*, proof side (L-RED R162, claude/l-red 54832628).
Labels: PROVED (lane), DEAD (instance), DATA, CONJECTURE, READING, OPEN. No count is bounded here. G-N5-TIME stays OPEN. This is not M3, not a
step-4 pass and not a TARGET.md claim.

## 0. Answer
- PROVED (lane) SW-WIT. The switch sites witness F. At every W-changing transition k, every changed vertex v copies the change of the first
  vertex y on its new play that switched at k, and W(y) changes. So U = S*_F := {y : y switched at some k with W(y) changed at k}
  satisfies R162's STAIR-U premise. Corpus: WITVIOL 0 on 1,132 games.
- DEAD: U = switch sites as a PASSIVE-PROOF witness set. On cp_K4 (L-RED R162) the passive observers are Even switching vertices, so
  DESC_S = DESC = 388 = 2.02n. READING: no rule that reads only a vertex's own behaviour can exclude a passive switching observer, because
  it behaves like a core switching vertex. A passive-proof U has to use the reader structure, and R162 §3 shows how in-edge rules are
  inflated in turn. So there is no canonical U in this sense, and DESC* stays a set-cover minimum.
- But passives inflate the counted set by at most a factor n, which is harmless for POLYNOMIAL time. PROVED (lane) DESC-ROOT: every descent
  (v, k) is a copy, along an unswitched prefix of v's play, of a descent (x, k) of one of three types:
  - R (root): x switched at k;
  - T (tie): x switched without a W-change inside the descent window;
  - S (stale switch): x switched at its own previous change.
  - Hence DESC_F ≤ n·(R_F + T_F + S_F), with T_F ≤ TS_F, the W-flat switches of F.
- PROVED (lane) Theorem ROOT-STAIR (an EQUIVALENCE):
  |F| ≤ T1_F + n(3n + 1) + (3n + 1)·n·(R_F + S_F + TS_F), and conversely R_F + S_F ≤ n·WCT_F, TS_F ≤ n·|F|.
- PROVED (lane) ORIGIN-NEW. A root change whose new target's W does not change at k enters by an edge that is not in H_(k−1), so it is
  newly Ξ-improving at k. Corpus: 25,679 origin root changes, 0 violations. An old-edge root change is therefore a RELAY: its target's W
  changes at the same transition.
- DATA / CONJECTURE ROOT-FUEL′. Every NEW-edge root descent is an L-SI fuel re-route (P-N5-ODD §6): corpus 7,559 / 7,559.
  - DEAD as stated for all root descents: 47 corpus root descents enter by an OLD edge. They are all relays, as ORIGIN-NEW forces
    (instance red/n5inj/instances/frz32: 3, at k = 3 (2 → 17) and k = 7 (17 → 5, 13 → 5); w_re3_1: 2).
- Where root descents still nest (READING, §5). Per pair, FUEL-COUNT bounds the fuel re-routes by the target's higher-key Ξ-changes
  (HC). Feeding that back closes the loop into R95's XI-CH-POLY core (XI-RUN), not into anything smaller. So this box gives a REDUCTION
  (descents → root descents → fuel re-routes + relays), not a bound. The corpus maxima are small: per W-run at most 5 root descents at one
  vertex and 2 at one pair. obs has 12 at one PASSIVE pair, one per round.

## 1. Setting
- As in P-N5-STAIR §1 (frozen packet, sha1 31771241, under review): W-run F = [p, q], τ and λ_W fixed, C := {v : λ_W(v) = v}, W_j the
  (σ_j, τ)-valuation, β the oriented bit encoding (3n + 1 bits), first-difference positions q, descents as in DESC-COPY / ASC-RUN.
- s_j(v) := v's successor at state j: σ_j(v) for Even v, τ(v) for Odd v. Even y SWITCHES at k if σ_(k+1)(y) ≠ σ_k(y). Sw_k := the
  vertices switched at k.
- A ROOT CHANGE at k is a pair (y, k) with y ∈ Sw_k and W(y) changing at k. A TIE SWITCH is a pair (y, k) with y ∈ Sw_k and W(y) not
  changing at k. TS_F := the number of tie switches on F.
- Premises: the packet's [1E-N3], [W-MON], [PLAY] and Lemma COPY (§6 of the packet), plus the SPEC S2 improvement fact used by [1E-N3]: a
  pointwise optimum of a one-player arena has no improving edge in that arena.

## 2. Lemma COPY⁺ (the converse of COPY) and Lemma SW-WIT — PROVED (lane)
- COPY⁺. In COPY's situation (v ∉ C, s_k(v) = s_(k+1)(v) = z), W(v) changes at k iff W(z) changes at k, and the change positions satisfy
  q_v = π_v(q_z), with π_v strictly increasing.
  - Proof. COPY gives "only if" and the position map.
  - For "if": v is not in the path set of W_j(z), for j = k, k + 1. Otherwise v would occur on z's play before λ_W(v), and since
    s_j(v) = z the play from z would cycle through v without reaching λ_W(v), against λ_W(z) = λ_W(v).
  - So v's own rank bit is constant in W_j(z), every other bit is copied, and the threshold shift is a bijection on the lengths that
    occur. Hence a flip of W(z) is a flip of W(v). □
- SW-WIT. Let k be W-changing and v a vertex whose W changes at k. Walk x_0 := v, x_(i+1) := s_(k+1)(x_i). Let m be the least index with
  x_m ∈ C ∪ Sw_k. Then x_m ∈ Sw_k \ C, W(x_m) changes at k, and v's change is x_m's change mapped by π_(x_0) ∘ … ∘ π_(x_(m−1)).
  - Proof. The walk meets C, because the play reaches λ_W(v), so m exists.
  - x_0, …, x_(m−1) are unswitched, so s_k = s_(k+1) on them. Apply COPY⁺ along the prefix: W(v) changes iff W(x_m) changes.
  - C-vertices keep the constant value (c, ∅, 0) (COPY). So x_m ∉ C, which forces x_m ∈ Sw_k. □
- Corollary. S*_F witnesses F. R162's STAIR-U gives |F| ≤ T1_F + |S*_F|(3n + 1) + (3n + 2)·DESC_(S*_F).

## 3. Lemma DESC-ROOT and Theorem ROOT-STAIR — PROVED (lane)
- DESC-ROOT. Let v have a descent at k, with previous change at k′ < k (both in F).
  - Walk x_i along v's play at state k + 1, as in §2. Let j be the least index such that x_j ∈ C or x_j switched at some transition of
    [k′, k].
  - Then x_j ∉ C. W(x_j) changes at k′ and at k and at no transition strictly between, and it has a descent at k.
  - Exactly one type holds:
    - (R) x_j switched at k;
    - (T) not (R), and x_j switched at some t with k′ < t < k, a TIE switch, because W(x_j) does not change at t;
    - (S) x_j switched at k′ and at no transition of (k′, k].
- Proof.
  - The prefix x_0, …, x_(j−1) is unswitched at every transition of [k′, k], so each of them has one successor at all states k′, …, k + 1.
  - By COPY⁺ along the prefix, at each transition of [k′, k] W(v) changes iff W(x_j) changes, and the positions are mapped by one strictly
    increasing composite map.
  - If x_j ∈ C, W(v) would be constant on [k′, k + 1]. So x_j ∉ C.
  - v changes at k′ and k and not between. So does x_j, and q_k(x_j) > q_(k′)(x_j) because the map is strictly increasing.
  - The types follow from where x_j's switch in [k′, k] lies. In (T), W(x_j) does not change at t ∈ (k′, k). □
- Counting.
  - For fixed (x, k), the preimages v are distinct vertices whose walks pass x, so there are at most n of them.
  - T-type descents of x are charged to a tie switch of x in (k′_x, k). For fixed x these windows are disjoint, so T_F ≤ TS_F.
  - R_F, S_F, T_F count the image descents (x, k) of each type. In particular, R_F is the number of root changes that are descents.
- Theorem ROOT-STAIR.
  - DESC_F ≤ n(R_F + S_F + T_F). With P-N5-STAIR's Theorem STAIR:
    |F| ≤ T1_F + n(3n + 1) + (3n + 1)·n·(R_F + S_F + TS_F).
  - Conversely R_F + S_F ≤ DESC_F ≤ n·WCT_F and TS_F ≤ n·|F|. So WRUN-POLY ⟺ (T1 + R + S + TS)-POLY. □
  - Per-transition form: at most n image descents per transition, so DESC_F ≤ n²·DTR_F, where DTR_F counts the transitions with an image
    descent. That count is not inflatable by copies, but it is inflatable by suffix observers (R162 suf_K, where every descent is type R).

## 4. Lemma ORIGIN-NEW — PROVED (lane)
- Statement. Let (y, k) be a root change with k − 1 ∈ F, and let z := σ_(k+1)(y). If W(z) does not change at k, then (y, z) ∉ H_(k−1).
  Hence (y, z) ∈ Iσ_k \ H_(k−1): z ≠ σ_(k−1)(y), and the edge is newly Ξ-improving at k.
- Proof.
  - Suppose (y, z) ∈ H_(k−1). σ_k is the pointwise optimum of H_(k−1) [1E-N3], and W_k is its valuation. So (y, z) is not improving:
    W_k(z) ⊴ W_k(z0), with z0 := σ_k(y), in the successor order of SPEC S2.
  - y is in neither path set: not in that of W_k(z0) (s_k(y) = z0) and not in that of W_(k+1)(z) (s_(k+1)(y) = z), by the argument of
    COPY⁺. Both values have the cycle node λ_W(y).
  - So Φ(y; ·) is order-preserving on them ([PLAY], COPY): W_(k+1)(y) = Φ(y; W_(k+1)(z)) = Φ(y; W_k(z)) ⊴ Φ(y; W_k(z0)) = W_k(y).
  - With [W-MON], W_(k+1)(y) = W_k(y), so (y, k) is not a root change. □
- Corollary (relay). A root change entering by an edge of H_(k−1) has W(z) changing at k. The same SANDWICH argument gives y's change
  position ≥ π_y(z's change position).
- DATA: 25,679 origin root changes on the corpus, ONVIOL 0.

## 5. Root descents against FUEL-LEX / FUEL-COUNT (L-SI P-N5-ODD §6, claude/l-si 0afc0d70a) — DATA, CONJECTURE, READING
- DATA (desc4.py, corpus).
  - Every root descent has k − 1 ∈ F (RD_K1 = RD = 7,606; a descent needs an earlier change in F).
  - 7,559 enter by a new edge ((y, z) ∉ H_(k−1)), and all 7,559 are fuel re-routes (Ξ_(k−1)(z) ≠ Ξ_k(z)): RD_NEWNOTFUEL 0.
  - 47 enter by an old edge. All are relays (ORIGIN-NEW; VERB lines on frz32 and w_re3_1 print «relay True»).
- CONJECTURE ROOT-FUEL′: every new-edge root descent is a fuel re-route. Not proved: (y, z) ∈ Iσ_k \ H_(k−1) can also arise from a change
  of Ξ(σ_k(y)) or of σ_k(y), with Ξ(z) fixed.
- If ROOT-FUEL′ holds:
  - FUEL-COUNT gives R^new_F(y, z) ≤ n(n + 2)(HC_(y,z) + n) per pair. With the trivial remark (distinct re-routes have distinct rise
    transitions), R^new_F(y, z) ≤ XCH_F(z).
  - So R^new_F ≤ Σ_(y,z) XCH_F(z) ≤ d_E·Σ_z XCH_F(z). That is R95 XI-RUN's shape again.
  - READING: the chain descents → root descents → fuel re-routes closes into the landed XI-CH-POLY core, not into a smaller named
    statement.
- Where they nest (READING). A root descent at (y, z) needs a fresh rise of Ξ(z) at a key above the pair's last key (FUEL-LEX ASC / EQHI).
  - A multiplicative nest therefore needs z's higher-key Ξ-changes to be produced, inside the same W-run, by root descents further down.
    That is R161's recursive leapfrog, still OPEN, with depth 2 realised (fbg: 4 re-routes per pair, one per phase) and depth 3 not built.
  - The relays (old edges) add no new entry: their change is at or below the copied change of the target (§4 corollary). Whether they can
    be folded into DESC-ROOT's copy map is OPEN.
- Box 110 link: a root descent is not the same as a trade-down switch. RESET-ROOT's roots are resets, and a root change can be an ascent
  with resets below it. ROOT-STAIR counts descents only, so trade-downs that never descend are already paid by STAIR's Ψ.

## 6. DATA (desc3.py / desc4.py, in experiments/new/box113/)
- Corpus = L-SI box 53's 1,132 games (lists of box 111): 1,692 W-runs, 14,028 transitions, WCT 13,949, DESC 14,755 (equal to box 111).
  - DMISS 0 (DESC-ROOT holds), ROOTMISS 0 (SW-WIT), WITVIOL_S 0.
  - R 7,606, S 932, T 1 (red/h3/instances/lcount2_n23, a tie switch inside a window), TS 397.
  - Max copies per image (MAPMAX) 105. Max over games of DESC / (R + S + T) is 14 (tcS8_N9).
  - Origin root descents 6,982, relay root descents 624.
- Pins (all faithful here: n5b SPEC = xeng state by state «state sequences identical: True», and Oink 8fbf0a7 --zlk winners equal N5's
  with verify OK (red/rel2/oinkcmp.sh «OINK OK»)):

| instance | n | WT | DESC | R | S | T | copies (pure / blocked) | RD_OLDEDGE | RD_FUEL | MAXRD_V / PAIR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fbg_K4_m6_m48 (L-RED R158) | 250 | 235 | 640 | 210 | 0 | 0 | 430 / 0 | 0 | 210 | 5 / 4 |
| cp_K4 (L-RED R162) | 192 | 44 | 388 | 388 | 0 | 0 | 0 / 0 | 0 | 388 | 4 / 4 |
| suf_K4 (R162) | 103 | 44 | 28 | 28 | 0 | 0 | 0 | 0 | 28 | |
| w_re3_1 (R160) | 32 | 25 | 20 | 11 | 2 | 0 | 7 / 2 | 2 | 9 | 2 / 1 |
| hit_b6a_1 (box 109) | 32 | 38 | 24 | 17 | 1 | 0 | 6 / 1 | 0 | 17 | 1 / 1 |
| frz32 (red/n5inj) | 32 | 43 | 28 | 21 | 2 | 0 | 5 / 2 | 3 | 18 | 2 / 1 |
| lcount2_n23 (red/h3) | 23 | 3 | 6 | 1 | 1 | 1 | 0 / 5 | 0 | 1 | 1 / 1 |
| obs_K12_m24 | 272 | 324 | 12 | 12 | 0 | 0 | 0 | 0 | 12 | 12 / 12 (passive) |
| sbq2_K8_m16, hd_H40 | 261, 122 | 152, 40 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

- fbg: the 430 «delay-line» descents (R162) are PURE copies of 210 root descents at 14 transitions. Every root descent there is a fuel
  re-route, and 192 of the 210 are relays through new edges.
- Pin «box 113 DESCSTAR» in experiments/new/check.sh: desc4 on w_re3_1, hit_b6a_1, frz32, lcount2_n23, cp_K4.

## 7. Dead ends (this box)
- «U = switch sites is a passive-proof witness set»: DEAD, cp_K4 (DESC_S = 388 = DESC; the observers switch).
- «Every root descent is a fuel re-route»: DEAD, frz32 (3 old-edge relay root descents) and w_re3_1 (2). Repaired to ROOT-FUEL′ (new-edge
  ones only; DATA 7,559 / 7,559).
- «No tie switch occurs inside a descent window» (which would make T = 0): DEAD, lcount2_n23 (T = 1; TS 397 on the corpus).

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box113/ (desc3.py, desc4.py, run3.sh, run4.sh, sum3.py, d3_* / d4_* corpus outputs, inst/ = read-only
  copies of L-RED's fbg_K4_m6_m48, w_re3_1, cp_K4, suf_K4, suf_K8 from claude/l-red 54832628); check.sh pin «box 113 DESCSTAR».
- FINDINGS:
  - PROVED (lane): COPY⁺, SW-WIT, DESC-ROOT, ROOT-STAIR (equivalence), ORIGIN-NEW.
  - DEAD: switch-site U as passive-proof (cp_K4); ROOT-FUEL for all root descents (frz32); T = 0 (lcount2_n23).
  - CONJECTURE ROOT-FUEL′ (7,559 / 7,559). READING: the reduction closes into XI-CH-POLY (XI-RUN), with no smaller named statement; DESC*
    has no canonical witness set; polynomiality is insensitive to passives (factor ≤ n).
- NEEDS: Lead: routing. Options: (a) proof attempt of ROOT-FUEL′; (b) L-RED: a core whose root descents per pair grow (recursive leapfrog,
  depth 3); (c) fold the S / relay terms into the copy map.
