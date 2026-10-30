# R-N5-WRUN: REFEREE report on packet P-N5-WRUN (L-NEW box 92): the within-W-run reduction chain, Theorem XI-RUN, Corollary WRUN-EQ
Referee: REFEREE (successor 20), Opus 5.5 (D15). Lead brief 2026-10-30 16:22Z (date -u). REFEREE-2 reviews independently.
- Object and pin: docs/new/P-N5-WRUN-box92.md at claude/l-new 7668bc9b, `git show 7668bc9b:<path> | sha1sum` =
  fae68aa004015c26e2f1f6d8803a6c45d7464dfa (371 lines). Line file docs/new/P-N5-WRUN-box92-line.txt sha1
  0faa5b80393bac1a6a3f6130926a4e18e3cf6129. Both equal the Lead's figures.
- Runs 2026-10-30T16:23Z-16:30Z; report written from 16:27Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independence:
  - I opened no docs/referee-2/ file for this packet.
  - [SUB] (§2.4): my verdict in §9.1 was written and saved BEFORE I opened docs/referee-2/SUB-check.md, and I opened it only to quote-check
    §2.4 (§1 below).
- Premises opened:
  - RESULTS R15 (a), (b), (d); R86 (a) SW-RETURN; R88 (title, Object) and its packet P-N5-GP-box31.md @ d072bb28 (§1 [FRZ], [H], §2 W-MON / XW,
    §3 GP*, §4 FW-R*); R89 (title: SUCC-MON, LATE-RISE, GP*-RUN, R*-RISE); R91 (title: XW, W-MON, W-SUCC, piece, LATE-W); R93 (a) and NEW-BOUND;
  - SPEC S1 (p′, rank).
- Quotes:
  - §1: every «…» fragment is verbatim in RESULTS (mechanical check, split at «…», whitespace-normalised). The exception is the [R93] LEX quote,
    which is verbatim in R93's object P-N5-WCH-box79.md @ 2ad78f51 (checked in R-N5-FIXD).
  - §2.1-§2.3 block quotes: byte-identical to l-red 47000632 docs/red/R140-friedmann-port.md l. 42-46, and to l-si a0d6f79b
    docs/si/N5-GATE-box51b.md l. 22-47 and l. 276-294. Identical on trunk too.
  - §2.4: byte-identical to docs/referee-2/SUB-check.md l. 5-11 at a11c2868 and at origin/claude/referee-2's head. Compared mechanically,
    after my §9.1 verdict was saved.
- Scope (D1): REDUCTIONS and EQUIVALENCES inside W-runs of N5. No residual is bounded. W-runs are not whole runs. G-N5-TIME stays OPEN. Not a
  TARGET.md claim.

## Verdicts
| § | item | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| 1 | setting, premises, Fact STEP-SW, Fact EXT | CHECKED. STEP-SW ✓. Fact EXT is true only for arguments whose path sets do not contain y (WRUN-N1). Every use satisfies this |
| 2.1-2.3 | ARENA-MAX, INTERVAL-SI / TIGHT-VALUE / FL-INT, RETURN-CHARGE / INT-XCH (other lanes) | quoted verbatim. Not signed as packet items: the Lead has not routed them. FL-INT's counting step, which E7 uses, is SIGNED as part of E7 |
| 2.4 / 9.1 | [SUB] | SIGNED, independently (§9.1) |
| 3.2 | Theorem XI-RUN (any stretch R of a W-run) | SIGNED |
| 3.3 | Corollary WRUN-EQ rows E1-E13 | SIGNED, every row in the direction(s) marked. The "⇔" rows E1-E8 have both directions proved; E8 needs [SUB], which is now signed. The one-way rows are one-way only in the sense "converse not proved" (WRUN-N4) |
| 4.2 | Lemma WAIT-CYCLE′ (Claim A, Cases 1-3), Corollaries DEAD-CYCLE, CHARGE | SIGNED, for the §4.1 definition of a self-routed block. The line drops two of its hypotheses: GAP G-WRUN-1 (line only) |
| 4.3 | Lemma E0-BOUND | SIGNED |
| 4.4 | Theorem TRIPLE-RED | SIGNED |
| 5.1 | Lemma RET-ΞRISE | SIGNED. DEDUPE ✓: it is R86 SW-RETURN's chain started at the leave |
| 5.2 | Theorem FREE-RED | SIGNED |
| 6 | Lemmas GAP-DEV, ΞCH-PCH, Theorem RSTAR-PCH | SIGNED |
| 7 | Lemmas LEX-SIGN, PREFIX-MON, Theorem LEVEL-RED | SIGNED |
| 8 | BIP(ρ, τ), the identification, Lemma BIP-MON, Lemma NO-DEV (corrected) | SIGNED. The correction is right: box 88's «a switched vertex strictly improves its Ξ» fails exactly at own-cycle-node length switches (R15 (b)) |
| 9 | Theorem BIP-RED under [SUB] | SIGNED; unconditional now that [SUB] is signed by both referees |
| 10 | Lemma REL2-WRISE | SIGNED. Its conclusion W_q2(z) ▷ W_{s+1}(z) is already landed: RESULTS R91 Lemma LATE-W, with weaker hypotheses (no (A2), no frozen stretch) (WRUN-N2) |
| 11 | Corollary INT-XCH⁰ | SIGNED |
| 12-13 | CONJECTURES, DATA, DEAD, READING | not signed. Pins re-run with my own engine (§14) |
| — | RESULTS line (0faa5b80) | does NOT match yet: G-WRUN-1 (the line's block definition makes WAIT-CYCLE′ FALSE: instance wc_line_cex.pg), WRUN-L1 (k free in the LEVEL-RED clause), WRUN-L2 (the order on "signed path-set terms" is unbound), WRUN-N4 (wording of "one-way") (§15) |
One gap, G-WRUN-1, in the line only: as worded, the line's WAIT-CYCLE′ is FALSE (instance in §15). It is fixed by restoring the packet's own definition. Nothing in the packet is FALSE. Notes WRUN-N1..N4, WRUN-L1..L2.

## 1-2. Setting; other lanes
- STEP-SW ✓. A W-run transition is not an S4c fallback and has τ_{t+1} = τ_t. By R15 (d) it changes σ. A σ-change that is not a fallback is
  S4a's σ_new ≠ σ_t, so every switched v takes an edge of H_t, i.e. of Iσ_t ([R57]).
- WRUN-N1 (Fact EXT). «strictly order-preserving and order-reflecting» needs y ∉ P(x) for both arguments. If y lay in one path set and not
  the other, adding y would change the symmetric difference. Every use satisfies y ∉ P:
  - REL2-WRISE (i): y's plays to z and to h avoid y, by (A2) and (A1);
  - TRIPLE-RED / RSTAR-PCH / RETURN-CHARGE: v is not its own cycle node, so the successor's play does not revisit v.
  Add the clause «for arguments whose path sets do not contain y» to Fact EXT. Wording only.

## 3. XI-RUN and WRUN-EQ
- XI-RUN ✓. |R| ≤ Σ_v SW_R(v) holds because each transition switches ≥ 1 Even vertex (STEP-SW). SW_R(v) = Σ_c ENT_R(v, c), and
  ENT_R(v, c) ≤ 1 + RISE_R(c) (R86 (a), any stretch, as its REFEREE cell says). Summing over the m_E Even edges gives
  m_E + Σ_c d_E(c)·RISE_R(c). Then Σ_c d_E(c) = m_E. INT-XCH⁰ is R = I ✓.
- Row by row (Lead watch item (1)). For each "⇔" I checked both directions, and that every symbol is in the line's parenthesis.
  - E1 ⇐: XI-RUN. ⇒: ΞCH_F(c) ≤ |F| ✓.
  - E2 ⇐: ΞCH-PCH, n(n + 1 + P*) is polynomial when P* is. ⇒: PCH ≤ ΞCH ✓.
  - E3 (fixed k) ⇐: LEVEL-RED gives PCH ≤ n(2n + 1)^k + DEEP_k, polynomial for fixed k; then E2. ⇒: DEEP_k ≤ PCH ≤ ΞCH ✓. The polynomial
    may depend on k, as "each fixed k" says.
  - E4 ⇐: |F| = WCH_F + FL_F, and WCH_F ≤ (n − 1)(R*_F + 1) (FW-R* on W-runs, R89 GP*-RUN). ⇒: trivial ✓.
  - E5 ⇐: TRIPLE-RED with Σ over ≤ m_E edges of max REG, max FREE. ⇒: REG, FREE ≤ RET ≤ |F| (at most one return of a given edge per
    transition) ✓.
  - E6 ⇐: R93 NEW-BOUND, Σ_e d_E(e)·WCH_F(e) ≤ m_E·max_e WCH_F(e). ⇒: WCH_F(e) ≤ |F|, TIE_F ≤ n_E·|F| ✓.
  - E7 ⇐: FL_F = Σ_I |I| over the WCH_F + 1 maximal W-constant intervals of F (I checked this counting step myself: the transitions of the
    W-constant intervals are exactly the FL transitions), then E4. ⇒: |I| ≤ |F| ✓. This direction needs [P-INT] to be read on W-constant
    intervals OF W-RUNS. The line does that («a W-constant interval I of F is a maximal run of states of F with W constant»). L-SI's own
    wording, «every W-constant interval of every run» (packet l. 108), would allow intervals that span W-run boundaries (a τ-change or
    fallback that keeps W), and those are not bounded by |F|. WRUN-N3: say «of a W-run» at l. 108 as the line does.
  - E8 ⇐: BIP-RED (needs [SUB]). ⇒: SB_F ≤ |F|, R°_Φ ≤ |Φ| ≤ |F|, FL_F ≤ |F| ✓.
  - E9-E13 ✓ as marked.
    - E10 uses BIP-REL-1 ⇒ R°_Φ ≤ m_E: one strict release per Even edge, and each counted transition carries ≥ 1 release.
    - E12 is NO-DEV.
- WRUN-N4. «XI-CH-POLY ⇒ R*-POLY, FL-POLY, SB-POLY and WRUN-POLY ⇒ R3-POLY are one-way» (line) could be read as "the converse is false".
  The packet means only that no converse is proved (E10's «as far as known»). Suggested: «… are proved in one direction only».

## 4. Box 84: WAIT-CYCLE′, E0-BOUND, TRIPLE-RED
- Claim A, Case 1 (X ∉ Z*) ✓.
  - The play from σ(X) never reaches X, since otherwise X ∈ Z*. So π ∪ {X} is disjoint from it, and
    Ξ(g) = (c*, P′ ∪ A, ℓ′ + 1 + |π|) with A ∩ P′ = ∅.
  - If A ≠ ∅, the symmetric difference is A and its top m decides. The block forces m odd, so rew(m) = −p′(m) < rew(c*) in both parities of c*.
  - If A = ∅, Ξ(g) is longer by |π| + 1 ≥ 1. With c* odd that would be improving, so c* is even and rew(z) ≤ p′(z) < p′(c*).
- Case 2 ✓: the arc from σX to c* lies inside Z*, whose other vertices are below c*. Since π avoids Z*, c* ∉ C.
- Case 3 ✓: REG with c* = X forces A ≠ ∅, and A's top is odd, else (X, g) would be improving.
- The final step ✓. The (σ_t, ρ′)-play from X follows g, then π with the t1 choices (Pat on Even, σ̄_t1 on Odd), back to X: C repeated, so its
  cycle node is z. Pointwise optimality (S1, [R57]) gives rew(λ(Ξ_t(X))) ≤ rew(z) < rew(c*), and then Ξ_t(X) ◁ Ξ_t1(X), against MON.
- The hypothesis «π avoids Z* when X ∈ Z*» is used in Case 2, to keep c* off C. G-WRUN-1 (§15) concerns the line, which omits it.
- DEAD-CYCLE ✓. It also covers t = t1. CHARGE ✓.
- E0-BOUND ✓.
  - Ξ_{t1}(g) ∈ K = {(X, ∅, ℓ)}.
  - (X, g) ∈ Iσ_{t2−1} by STEP-SW, so SUCC-MON and the block give a strict rise of Ξ(g) inside [t1^i, t2^i − 1].
  - The windows are disjoint, because s^{i+1} ≥ t2^i: X holds g from t2^i until its next leave.
  - K is an interval (LEX: the first n + 1 coordinates of CS are fixed), so Ξ(g) stays in K on [t1^1, t1^last].
  - So last − 1 ≤ n − 1.
- TRIPLE-RED ✓. Charge each transition to one switch. A first adoption in F happens at most once per Even edge (≤ m_E); every other switch is
  a return, of exactly one class.

## 5-7. RET-ΞRISE, FREE-RED, GAP-DEV, ΞCH-PCH, RSTAR-PCH, LEX-SIGN, PREFIX-MON, LEVEL-RED
- RET-ΞRISE ✓. The chain is
  Ξ_k(g) ▷ Ξ_k(σ_k X) ⊵ Ξ_{s+1}(h) ⊵ Ξ_s(h) ▷ Ξ_s(g),
  using SUCC-MON on [s + 1, k] and MON. Windows [s, k] of successive returns are disjoint ✓.
- FREE-RED ✓.
- GAP-DEV ✓. The chain is W_q(z) ▷ W_q(σ_q y) ⊵ Ξ_q(σ_q y) ⊵ Ξ_q(z) (XW; "not improving" plus totality). The second part ✓.
- ΞCH-PCH ✓.
  - λ changes strictly raise rew(λ), by MON and LEX, at most n − 1 times.
  - A block with (λ, P) fixed has a strictly monotone ℓ ∈ [0, n − 1].
  - Total: (n − 1) + PCH + (n + PCH)(n − 1) = n² − 1 + n·PCH ≤ n(n + 1 + PCH).
- RSTAR-PCH ✓ (R89 R*-RISE).
- LEX-SIGN ✓.
- PREFIX-MON ✓. I re-derived the three cases (0, +1), (−1, +1), (−1, 0) at the top differing rank r against the term order:
  - (r, +) beats (r, −), every lower-rank term and NONE;
  - (r, −) is beaten by every lower-rank term and NONE, because (r, −) < (r′, −) iff r > r′.
  Depth d ≥ k leaves pre_k equal; d < k raises it strictly. 2n + 1 term values.
- LEVEL-RED ✓. At most n λ-blocks in F, and at most (2n + 1)^k − 1 shallow changes per block.

## 8-10. BIP, NO-DEV, BIP-RED, REL2-WRISE
- §8.1 identification ✓: on a frozen stretch σ̄_t ≡ ρ, so Ξ_t = val(σ_t, ρ) and Iσ_t = Iρ_t; the step is [R57]'s optimum of H_t.
- BIP-MON ✓: R15 (a) in the game G_ρ, where ρ is Odd's only strategy; and the pointwise optimum against τ over an arena containing σ_t.
- NO-DEV (corrected) ✓ (Lead watch item (2)).
  - GAP-DEV gives R*_F = 0, so WCH_F ≤ n − 1.
  - At an FL transition W, hence Ξ (= W), is unchanged, and Ωτ is unchanged (τ fixed), so R15 (d) caps each FL block at 4n(n − 1).
  - With ≤ n blocks: |F| ≤ (n − 1) + 4n²(n − 1).
  - I agree that the old bound ≤ n − 1 had no proof: R15 (b) leaves exactly the own-cycle-node length switches.
- BIP-RED ✓.
  - The SB_F transitions change σ̄. The rest lie in the SB_F + 1 frozen stretches Φ, which are sub-intervals of F.
  - [SUB] on Φ, with R*_T(Φ) = R°_Φ (the strict-release definition is the late-adoption definition on Φ), bounds the W-changing ones by
    (n − 1)(R°_Φ + 1).
  - The FL ones total at most FL_F.
- REL2-WRISE ✓.
  - (i): π_s ∈ H_s; ARENA-MAX (= [R57]); (A2) gives val(π_s, τ)(z) = W_{s+1}(z) and y not on a cycle; (A1) gives W_{s+1}(y) = ext(y, W_{s+1}(h));
    EXT reflects (y in neither path set).
  - (ii): W-SUCC in the piece (a W-run lies in one R91 piece: τ constant, every transition an S4a step).
  - (iii): the BLOCKED definition.
  - WRUN-N2: RESULTS R91 Lemma LATE-W (landed) already states «in a piece, if v leaves c at s → s + 1 and (v, c) is blocked at a later state
    t′ of the piece, with v not its own W-cycle node on [s + 1, t′], then W_{t′}(c) ▷ W_{s+1}(c)». That is REL2-WRISE's conclusion without
    (A2) and without the frozen-stretch / strict-release setting. REL2-WRISE's second conclusion, Ξ_q2(z) ⊴ Ξ_q2(h2), is the definition of
    BLOCKED. Suggest citing R91 LATE-W instead (used by no reduction, as the packet says).

## 9.1 [SUB] (signed independently; verdict written before opening docs/referee-2/SUB-check.md)
- Statement (packet l. 133-138, the line's [SUB]). For every W-run F = [a, b] and every sub-interval F′ = [a′, b′] ⊆ F,
  WCH_{F′} ≤ (n − 1)(R*_T(F′) + 1), with R*_T(F′) the transitions of F′ adopting an edge blocked at a state of F′ before them.
- Verdict: TRUE, SIGNED (Opus 5.5, D15). Proof: R88's GP* and FW-R* proofs (P-N5-GP-box31.md @ d072bb28, §3-§4) go through on [a′, b′] verbatim.
  - GP* on F′. Its definitions are local to the states they name: BLOCKED at t uses W_t, ρ_t, Iσ_t; «unblocked at state k» uses states
    k − 1 − i ≥ a′ and L ≤ k − a′; and «u is a W-cycle node of state a′».
    - Base k = a′: W_{a′}(u) = (u, ∅, 0).
    - The step k → k + 1 uses only W-MON at that transition (true in F: S4a step, τ fixed; R91 W-MON / R88 W-MON via R89 GP*-RUN), [CASE-A]
      at state k, [R57] in H_k (Case B), and «λ_W constant» (B1′ (ii), B2b (i), (iii)), which holds on F ⊇ F′.
    - σ̄ need not be constant: R89 (h) GP*-RUN already drops it.
  - FW-R* on F′.
    - Transitions with k < a′ + n − 1: at most n − 1.
    - For k ≥ a′ + n − 1 with W_{k+1}(x) ≠ W_k(x): the ρ_{k+1}-play π from x to u = λ_W(x) has L ≤ n − 1 ≤ k − a′, and u is a W-cycle node of
      state a′ (λ_W is constant on F).
    - If π were unblocked at k, GP* on F′ and W-MON would give W_{k+1}(x) = W_k(x). So some (y_i, y_{i+1}) is blocked at t = k − 1 − i ≥ a′.
    - It is adopted at some τ ∈ (t, k] (S4a takes only {ρ_t} ∪ Iσ_t), which is a late adoption relative to F′, with k − τ ≤ n − 2.
    - Each τ is charged by at most n − 1 values of k.
  - The remark that R*_T(F′) ≤ the F-relative count restricted to F′ ✓: an edge blocked at t ∈ [a′, τ) is blocked at a state of [a, τ).
- DATA (own engine): every sub-interval of every W-run of the run set (§14), 82,358 sub-interval checks on n ≤ 100, plus 201,323 on the three large pins, 0 violations. MUT 3 ((n − 2) in place of
  (n − 1)): did not bite on 150 random games (n ≤ 10); I did not run it on the run set. The (n − 1) factor is not tight in these data, so this mutation is not a usable control for [SUB]; XI-RUN's sub-stretch check does bite under MUT 4.

## 14. Controls and pins (own engine; docs/referee/scratch/wrun_probe.py, `python3 -I`)
- Checks:
  - STEP, STEPI: STEP-SW and the H_t edges;
  - XR: XI-RUN on F and on every sub-stretch; SWR: SW-RETURN per edge;
  - RET, RETC: RET-ΞRISE per return and per edge;
  - WC: WAIT-CYCLE′ over every REG block, against all later states of the whole run;
  - GD, GD2: GAP-DEV;
  - XP, RS, PM, LR: ΞCH-PCH, RSTAR-PCH, PREFIX-MON and LEVEL-RED for k = 1, 2, 3;
  - ND: NO-DEV; SUB: [SUB] on every sub-interval; BR: BIP-RED.
- Run set: box 83's lists (sbcg.lst 719 with the best-reward start; alt_all.lst 413 with the listed start), n ≤ 100. Results:
  - 813 runs (740 games, 73 skipped for n > 100), all RC 0: 4949 W-runs, 8066 W-run transitions, 269,250 REG blocks tested for WAIT-CYCLE′
    against every later state, 69,979 blocked (edge, state) records for GAP-DEV, 189 NO-DEV W-runs.
  - VIOLATIONS 0 for every check.
  - Maxima: |F| / (m_E + Σ d_E·ΞCH) 0.272 (the packet says 0.273, thetaA_n6); NO-DEV |F| 55 (x32_rand64, n 64); R*_F 17; SB_F 35.
- Mutations: MUT 4 (XI-RUN without m_E) bites (XR 8 on 150 random games). MUT 1 (WAIT-CYCLE′ with only «π avoids Z*» dropped): 0 recurrences over 283,077 blocks, so the data never needed that clause. MUT 5 (the LINE's block definition: also g = σ_t(X) allowed) bites at once (§15).
- Pins (sha1s equal the packet's; best-reward start; WAIT-CYCLE′ off for size; all 0 violations):
  - pftheta34_n32: |F| 34, ratio 0.034 (packet: bound 1010);
  - fx_K8_m32 (e995709e…): 280 W-run transitions, max R* 16;
  - latew_K16_m32 (6d34c161…): 560 transitions, SB_F 513 (packet 513);
  - gate_K64_n581 (a93c7c8b…): R*_F 64 (packet 64).

## 15. RESULTS line (0faa5b80): diff against the packet and the strict symbol test
- G-WRUN-1 (GAP in the line; the packet is right). The line defines blocks as «(X, g) not improving and the (σ_t, σ̄_t)-play from g reaching
  X, E0 iff X is the cycle node of Ξ_t(X) and every vertex of the route is below X». §4.1 also requires:
  - g ≠ σ_t(X);
  - «If X lies on the cycle Z* of its own (σ_t, σ̄_t)-play, π is also required to avoid Z*».
  WAIT-CYCLE′'s Case 2 uses the second requirement (c* ∉ C). Without it, a REG "block" can have c* on C, so Claim A (rew(top C) < rew(c*))
  fails and the proof gives nothing.
  - FALSE as worded (instance). docs/referee/scratch/wrun_logs/wc_line_cex.pg (sha1 a8a5013bbb4860a2d700b0f554b065b08487d65a; n 4;
    0: prio 6, Odd → 3; 1: prio 1, Even → 1, 3; 2: prio 0, Even → 1, 3; 3: prio 3, Even → 0, 1, 2), N5 from the best-reward start.
  - At state 0, σ_0(3) = 0, and the (σ_0, σ̄_0)-play of X = 3 is the cycle {3, 0} with cycle node c* = 0 ≠ X.
  - Take g := 0 = σ_0(X). (X, g) is not improving, and the play from g reaches X with route π = [0]. X is not the cycle node of Ξ_0(X), so
    under the line's wording the block is not E0, i.e. it is REG.
  - At state 1, σ_1(3) = 0 again and π has no Even vertex, so «σ never again has X → g together with the block's choices on π» fails at t = 1.
  - Under the packet's §4.1 definition this is not a block at all: g = σ_0(X), and π meets Z*.
  - My probe with the line's definition (MUT 5) finds 21 such recurrences on nep92_n40 and 8 on 100 random games of n ≤ 6. With the packet's
    definition: 0.
  Fix: restore both clauses in the line's block definition, e.g. «… (X, g) not improving, g ≠ σ_t(X), and the (σ_t, σ̄_t)-play from g
  reaching X along a route that avoids the cycle of X's own play when X lies on it, …».
- WRUN-L1 (FREE SYMBOL). In «(Lemmas LEX-SIGN, PREFIX-MON, Theorem LEVEL-RED) with fixed cycle node the first k signed path-set terms are
  non-decreasing … and PCH_F(v) ≤ n(2n + 1)^k + DEEP_{k,F}(v)», k is not quantified, and DEEP_{k,F}'s definition in the parenthesis uses the
  same free k. Fix: «for every k ≥ 1, …».
- WRUN-L2 (UNBOUND ORDER). «the first k signed path-set terms are non-decreasing» names no order on terms. §7.2's order (plus terms by rank
  upwards, NONE, minus terms by rank downwards; prefixes lexicographic) must be stated, or the clause dropped. LEVEL-RED's inequality does not
  need it.
- WRUN-N4: the wording of "one-way" (§3).
- Token pass. Every other symbol is bound in the parenthesis or by a landed item with a label that exists in RESULTS:
  - n, n_E, m_E, d_E, run, transition, switched / enters / leaves, Ξ_t, σ̄_t, (c, P, ℓ), λ, W_t, val, λ_W, ⊴…, Iσ_t, H_t;
  - τ-stretch / W-run (R89), |F|, blocked / late adoptions / R*_F (R88 / R89), ENT / SW / RISE (R86), ΞCH, WCH(c), WCH, FL, TIE (R93), PCH,
    P*, Q-POLY, WRUN-POLY, XI-CH-POLY;
  - return, RET, REG / E0 / FREE (modulo G-WRUN-1), depth, DEEP (modulo WRUN-L1), frozen stretch, SB, R°_Φ, R°, [SUB], R*_T(F′),
    W-constant interval, XCH_I;
  - R*-, FL-, P*-, DEEP_k-, TIE-, SB-, R°-, R3-, ALT-, FREE-POLY, [P-INT]; (A1), (A2); strict release.
  - Two "used but defined elsewhere" items: «strict release» is defined only implicitly by R°_Φ («adopting an edge blocked at an earlier
    state of Φ»), which is acceptable; ρ in BIP-MON is bound by «σ̄ ≡ ρ».
- Second pass, clause by clause:
  - XI-RUN «every stretch R of consecutive states of a W-run» ✓.
  - WAIT-CYCLE′ «σ never again has …»: «again» = states t > t1 of the same run ✓, but see G-WRUN-1.
  - NO-DEV «if Ξ_t = W_t at every state of F» ✓.
  - BIP-RED needs «under [SUB]», and the line has «an implication from [SUB]» ✓. Since [SUB] is now signed by both referees, the Lead may
    drop the condition.
  - REL2-WRISE's «(y, z) has a strict release in a frozen stretch, y leaves z at s» does not say s is after the release. It is not needed
    (WRUN-N2).
- Verdict: the line MATCHES the packet's signed items once G-WRUN-1, WRUN-L1 and WRUN-L2 are applied.

## Addendum 1 (2026-10-30 ~16:50Z by date -u): BIP-REL-1 erratum
- The Lead reports (16:34Z) that L-RED 34 R143 (l-red 717f407a) KILLED CONJECTURE BIP-REL-1: rel2_R2_n82 has two strict releases of one edge
  in one frozen stretch, and the family gives R releases at n ≈ 20R². I have NOT re-run this kill. It is recorded here as the Lead's report.
- Effect on this review:
  - Row E10 («BIP-REL-1 ∧ SB-POLY ∧ FL-POLY ⇒ WRUN-POLY», under [SUB]) stays PROVED as an implication, but its hypothesis is now known to be
    false, so the row is vacuous.
  - §9's remark «With CONJECTURE BIP-REL-1 R° ≤ m_E» likewise has a false premise.
  - BIP-RED itself (|F| ≤ SB_F + (SB_F + 1)(n − 1)(R° + 1) + FL_F) and row E8 do not use BIP-REL-1 and are unaffected.
  - The line names BIP-REL-1 only in its closing "open" list. That should become «BIP-REL-1 is false (L-RED R143)» in the fixes file.

## DONE / FINDINGS / NEEDS
- DONE: this report; wrun_probe.py; wrun_logs/ (run.sh, sums, pins).
- FINDINGS:
  1. Every packet item put up for signing is SIGNED, and [SUB] is signed independently, so BIP-RED and E8 are unconditional. No gap in the packet.
  2. G-WRUN-1: the line's block definition drops g ≠ σ_t(X) and «π avoids Z*». As worded, WAIT-CYCLE′ is FALSE (wc_line_cex.pg, n 4). WRUN-L1: k free. WRUN-L2: term
     order unbound.
  3. Notes: WRUN-N1 (EXT clause), N2 (REL2-WRISE = landed R91 LATE-W), N3 ([P-INT] «of a W-run»), N4 (one-way wording).
  4. Own-engine data: 0 violations on the run set; pins as in §14.
- NEEDS: Lead: route G-WRUN-1, WRUN-L1, WRUN-L2 and N1-N4 to L-NEW 39 (fixes file); send me the §C word after REFEREE-2's report.
