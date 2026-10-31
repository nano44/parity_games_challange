# R-N5-SETTLE: REFEREE report on packet P-N5-SETTLE (L-SI box 52): Claim RG′, PLAY-CAUSE, RUN-SETTLE / RUN-COUNT, HEAD-RED, T-XCH
Referee: REFEREE (successor 20), Opus 5.5 (D15). Lead brief 2026-10-30 18:43Z (date -u). REFEREE-2 reviews independently.
- Object and pin: docs/si/P-N5-SETTLE-box52.md at claude/l-si 6a70a520, `git show 6a70a520:<path> | sha1sum` =
  aef403c3d8a003bcfc6742c4d1da084a1e21669f (248 lines). Line docs/si/P-N5-SETTLE-line.txt sha1 6aa094e32b03317797a551ac2fc719749cf59ca7.
  Both equal the Lead's figures.
- Runs 2026-10-30T18:45Z-18:48Z; report written from 18:47Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independence: I opened no docs/referee-2/ file for this packet.
- Premises opened:
  - SPEC docs/new/N5-ssi-global.md S1 (l. 33-44, the procedure: deletions (iii), longest / BFS lengths (iv)), S2, S4a;
  - RESULTS R15 (a), (d), R57, R86 (a), R89 (W-run);
  - L-RED R143 @ 717f407a (U_k, EVENT, SETTLE);
  - L-LIT T54 @ 96cfda95 (IDX-MONO, key, LEX-BFS);
  - L-RED R140 @ 47000632 (ARENA-MAX);
  - L-SI box 51b §10.1 @ a0d6f79b (Claim RG).
- Quotes. Mechanical check: whole text, «…» fragments, whitespace and bullet-normalised.
  - Every «…» from RESULTS, SPEC, R143 and T54 is verbatim at the stated SHAs, and ARENA-MAX is verbatim at l-red 47000632.
  - The Lead's brief cannot be checked.
  - Two notes: SETTLE-N1 (RG′ word-diff incomplete) and SETTLE-N2 (R140 cited without SHA).
- Scope (D1): REDUCTIONS and two EQUIVALENCES (HEAD-RED, T-XCH), N5 only. No count is bounded. G-N5-TIME stays OPEN. Not a TARGET.md claim.

## Verdicts
| § | item | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| 1 | setting; STEP-SW; MON | CHECKED |
| 2 | ARENA-MAX (= [R57] for S4a) | quoted verbatim. Used as [R57] |
| 2 | T54 IDX-MONO, LEX-BFS, read at W_(k+1) at any S4a step of a W-run | SIGNED as used in Case 2a. I re-derived both from SPEC S1 (iv) together with RG′ (§3) |
| 2 | R143 U_k, EVENT (definitions only) | used as definitions. SETTLE (B), (C) are not used (checked: §5 cites neither) |
| 3 | Claim RG′ | SIGNED |
| 4 | Lemma PLAY-CAUSE; W-MON; PATH | SIGNED |
| 5 | Theorem RUN-SETTLE (S_j, X_j by induction; Cases 1, 2a, 2b, 2c); Corollary RUN-COUNT | SIGNED |
| 6 | Theorem HEAD-RED (⇐, ⇒) | SIGNED |
| 7 | Corollary T-XCH | SIGNED (composition of landed R86 (a), both sides, with R15 (d)) |
| 8-9 | CONJECTURES, DATA, DEAD, READING | not signed. Pins re-run with my own engine (§9) |
| — | RESULTS line (6aa094e3) | does NOT match yet: SETTLE-L1 (F unquantified), SETTLE-L2 (T undefined), SETTLE-L3 (k free in RG′) are REQUIRED; SETTLE-L4 is precision (§10) |
No gap in the packet. Nothing FALSE.

## 3. Claim RG′
- The procedure as the packet uses it matches SPEC S1 (iii) on the dual of H_k. Dual parity 0, «Even likes u», is original-bad u, with
  M = reach(c avoiding u): bit to q ∉ M, and the edges of u and M are restricted to M. Dual-odd is original-good u, with M = reach(u avoiding
  c): bit to q ∈ M, and the edges of M ∖ {u} are restricted.
- (A) ✓.
  - Bad u: an edge x → y with y ∈ M, x ∉ M ∪ {u} would make x reach c avoiding u.
  - Good u: an edge x → y with y ∈ M, x ∉ M, x ≠ c would make x reach u avoiding c.
  - So surviving edges disagree on bit u only when they leave u, and u carries its own bit.
  - For a good u with an edge u → y, y ∈ M, both ends carry u. The set identity still holds, and such an edge is never length-tight (y's path
    passes u, so dist(y) > dist(u)). So the reading «exactly … with dist(y) = dist(x) − 1» is unaffected.
- (B) ✓.
  - Each deletion kind separates bit u (q ∈ M vs y ∉ M) or length (bad u, u → y with y ∉ M: y's paths pass u).
  - Bits are added only at u's own turn and never removed, so a separation at u's turn persists to the final values.
  - Tight edges into vertices whose cycle node is c stay inside R.
- Values = W_(k+1) by [R57]. Nothing uses W_(k+1) = W_k ✓.

## 4. PLAY-CAUSE, W-MON, PATH
- PLAY-CAUSE ✓.
  - i exists: off D_(k+1) the Ξ-play is the τ-play, and its first C-vertex is λ_W(x). A C-vertex reached earlier would be the cycle node.
  - y_(i+1) ∈ U_(k+1) ✓.
  - Ξ(x) is a function of (y_0 … y_i, Ξ(y_(i+1))): the cycle node w comes from Ξ(y_(i+1)), and the first occurrence of w is either among
    y_0 … y_i or at i + 1 + ℓ(Ξ(y_(i+1))) ✓.
  - Without a switch of an Even y_t (t ≤ i), and with no events (i) and (iii), the k-play has the same prefix, the same first index and the
    same Ξ(y_(i+1)), so Ξ_k(x) = Ξ_(k+1)(x).
  - t < i, since an Even y_i lies in C and (ii) forbids its switch. y_t ∉ C, by i's minimality ✓.
- W-MON ✓ (ARENA-MAX with ρ = σ_k ∈ H_k). PATH ✓ (C is fixed on F).

## 5. RUN-SETTLE
- j = 0 ✓.
- Least-ℓ violator, (MIN), PATH on b's path ✓.
- Case 1 ✓:
  Ξ_(k−1)(b) = Ξ_k(b) ▷ Ξ_k(a) ⊵ Ξ_(k−1)(a) ⊵ Ξ_(k−1)(σ_(k−1)y)
  would give b ∈ H_(k−1)(y). So Ξ(b) changes at k − 1 → k, inside the block, and X_(j−1) gives ℓ_k(b) ≥ j > L − 1.
- Case 2 ✓: ρ = σ_k[y ↦ b] ∈ H_(k−1). The chain W_k(y) ⊵ y ⊕ W_k(b) = W_(k+1)(y) ⊵ W_k(y) holds, so a and b are both W_k-tight.
- Case 2a ✓.
  - a's and b's paths are unchanged (MIN, PATH), so their keys are equal at k and k + 1.
  - Ω(c) even: LEX-BFS at k − 1 → k gives key(a) < key(b), and at k → k + 1 it gives key(b) < key(a). Keys of distinct vertices differ in
    the last coordinate.
  - Ω(c) odd: IDX-MONO gives index(a) < index(b) < index(a).
  - My derivation of the two rules from SPEC S1 (iv):
    - c odd (in the original game) means dual-even, so «Odd takes the LONGEST path … first strict maximum wins» in list order. The maxima
      are the remaining successors with dist = dist(v) − 1, which are exactly the W_(k+1)-tight arena edges by RG′. So the choice is the
      smallest-index tight edge.
    - c even means dual-odd, so BFS from c over predecessors in increasing index. By induction on the layer, queue order is lexicographic
      order of key_(σ_(k+1)), and v is discovered from the first queued successor in layer dist(v) − 1. These are the tight edges (RG′).
      So the choice is the lex-least key.
- Case 2b ✓: ARENA-MAX at k → k + 1 with ρ′ = σ_(k+1)[y ↦ a]. ⊕ is monotone because a's two paths avoid y.
- Case 2c ✓.
  - u exists: else a's paths would coincide and avoid y.
  - Z = P ∪ Q is simple, c ∉ Z.
  - Path sets: S_k(u) ⊔ R, with P disjoint from y's (σ_(k+1), τ)-path, whose path set equals W_k(y)'s.
  - W-MON forces R ≠ ∅ with an even top, or R = ∅ and c odd (|Z| ≥ 2).
  - ρ′ closes Z, and reward(top Z) > reward(c) in both cases. This contradicts ARENA-MAX.
- The cases exhaust ✓. The bound ✓: ℓ ≤ n − 1 on a simple path.
- RUN-COUNT ✓.

## 6-7. HEAD-RED, T-XCH
- HEAD-RED ✓.
  - Every event transition has a kind counted on the right.
  - Σ_o ≤ n_O·max, Σ_(c ∈ C) ≤ |C|·max, Σ_u ≤ n·max, each ≤ n·max.
  - (⇒) Each count is ≤ |F|.
- T-XCH ✓.
  - T ≤ Σ_v SW(v) holds because every iteration changes σ or τ (R15 (d)).
  - R86 (a) on both sides with R = the whole run.
  - XE, XO ≤ T.

## 9. Controls and pins (own engine; docs/referee/scratch/settle_probe.py, `python3 -I`)
- Checks:
  - BLK: event-free blocks ≤ n − 1; SJ / XJ: the fronts ℓ_(k+1) ≥ j + 1;
  - PC: PLAY-CAUSE; RC: RUN-COUNT; HR: HEAD-RED;
  - TI: σ_(k+1)(v) W_(k+1)-tight in H_k(v); IDX and LEX: the choice rules at every W-run transition.
- Run set: box 83 / 50b lists (sbcg.lst with the best-reward start; alt_all.lst with the listed start), n ≤ 100. Results:
  - 813 runs (740 games, 73 skipped for n > 100), all RC 0; 1,060 W-runs with transitions, 8,066 W-run transitions.
  - Checked: 12,448 PLAY-CAUSE cases; 27,157 IDX-MONO and 266,486 LEX-BFS choice checks (470 with ≥ 2 tight edges).
  - VIOLATIONS 0 for every check.
  - Longest event-free block: 63 (si/runlin/instances/runfam_K40, n 79, best-reward start).
- Mutations:
  - MUT 4 (LEX with argmax) bites (LEX 14 on 4 pin games);
  - MUT 5 (fronts j + 2) bites on gci2_n12 + start (SJ 2, XJ 2), so the front is attained, as the packet says;
  - MUT 1 (block bound n − 2) and MUT 3 (event (iii) dropped) never bit on the pins;
  - MUT 2 (IDX with the largest index) bites on the run set: IDX 6 (lend27_n24, nep22f_n64, nh_n8, obr_eq_n24).
- Pins and lane data:
  - x32_rand48: longest event-free block 44 (packet 44).
  - runfam_K40: 63, which equals the lane's own experiments/si/heads52/rwin_sbcg.txt line «WMAX 63 WN 0.797».
  - SETTLE-N3: the packet's §9 «the longest event-free block is 44 at n 48» is a mislabel. 44 / 48 = 0.92 is the largest RATIO WMAX / n;
    the longest block is 63 (runfam_K40). Data wording only.

## 10. RESULTS line (6aa094e3): diff against the packet and the strict symbol test
- Content: each clause states the packet's §3-§7 item and nothing more. The not-to-sign list and the REDUCTION tail are correct.
- SETTLE-L1 (REQUIRED, F unquantified). «W-run F := RESULTS R89's (…)» defines the term but quantifies nothing. Then RUN-SETTLE «the
  transitions k0, …, k1 − 1 of F», RUN-COUNT «|F| ≤ n(E_F + 1) − 1» and HEAD-RED «E_F ≤ …» leave F free (the K12 / WRUN-L3 pattern).
  Fix: «…): for every N5 run on every game and every W-run F of it: (Claim RG′) …».
- SETTLE-L2 (REQUIRED, T undefined). «every run has T ≤ m_E(1 + XE) + m_O(1 + XO)»: T is not defined in the line. Fix: «every run, with T
  its number of transitions (N5 iterations), has T ≤ …».
- SETTLE-L3 (REQUIRED, k free). «(Claim RG′) at every S4a step of a W-run, … W_(k+1)-tight …»: k is not bound in this clause. The line's
  «H_k := S4a's arena at k» and «W_(k+1)-tight» definitions use a free k too. Fix: «at every S4a step k → k + 1 of a W-run».
- SETTLE-L4 (precision). Bind or cite:
  - «event-free» (= «not an EVENT»);
  - ⊕ (as in RESULTS R93 TIE: x ⊕ (c, Q, ℓ) := (c, Q ∪ {x if x is more relevant than c}, ℓ + 1));
  - Iσ_k (SPEC S2);
  - the ranges of Σ_o (Odd o), Σ_c (c ∈ C) and Σ_u, and of the three «max»;
  - «W-runs are polynomial iff …» should read «for every family of games, every W-run has polynomially many transitions iff …» (packet §6).
  The proof parenthesis names unlanded T54 LEX-BFS / IDX-MONO and R140 ARENA-MAX. These are signed here as used, and ARENA-MAX = [R57], so
  this is acceptable as a proof note.
- Second pass, clause by clause:
  - RUN-SETTLE «for k0 ≤ k < k1» ✓;
  - «every vertex whose Ξ changes at k» = X_j ✓;
  - HEAD-RED's «as each count is ≤ |F|» ✓;
  - T-XCH «XE (XO) the most whole-run changes of one vertex's Ξ (U)» ✓.
- Verdict: MATCHES the packet's signed items once SETTLE-L1, L2 and L3 are applied.

## Notes (packet errata, not gaps)
- SETTLE-N1. §3's «Difference from §10.1 (word-diff …)» lists two changes. (B)'s heading also changed: «Every W-tight arena edge (x, y)
  survives» became «Every W_(k+1)-tight arena edge (x, y) with λ_W(x) = c survives». That is a restriction, it is correct, and it is what
  the statement needs, but the note does not declare it.
- SETTLE-N2. §2 cites R140 «on claude/l-red» without a SHA. The quote is verbatim at l-red 47000632 (the SHA the WRUN packet cites).

## Addendum 1 (2026-10-30 ~22:50Z by date -u): G-SRC-1 and Lemma ONE-STEP
- (1) G-SRC-1 CONFIRMED, as a proof-text gap in [SET] §5 Case 2 and Case 2b.
  - I found it independently in R-N5-SRC §3 (claude/referee 81f6b89c, written before I saw REFEREE-2's R2-N5-SRC or the Lead's 22:29Z
    message).
  - Case 2 writes val(ρ, τ)(y) = y ⊕ W_k(b) for ρ = σ_k[y ↦ b]. That holds only if y is not on c's σ_k-cycle. If y ≠ c lies on that cycle,
    the ρ-play closes a new cycle y → b's path → c → c's old arc → y, whose top can be above c. Case 2b has the same pattern with σ_(k+1),
    a and ρ′.
  - My signature of [SET] §5 (§5 above, «Case 2 ✓», «Case 2b ✓») missed this. It was a joint miss with REFEREE-2 23. The theorem is not
    affected (below).
- (2) Lemma ONE-STEP (REFEREE-2 24, docs/referee-2/R2-N5-SRC.md §3.2, claude/referee-2 e8c1b62d, confirmed an ancestor of origin): SIGNED
  (Opus 5.5, D15).
  - Statement: for a transition t → t + 1 of a W-run F, an Even y ∉ C, and z ∈ H_t(y) with λ_W(z) = λ_W(y) = c whose (σ_(t+1), τ)-path
    avoids y: y ⊕ W_(t+1)(z) ⊴ W_(t+1)(y).
  - My check. ρ′ := σ_(t+1)[y ↦ z] ∈ H_t, and ARENA-MAX gives W_(t+1)(y) ⊵ val(ρ′, τ)(y). The ρ′-play from y is y, then z's path to c
    (avoiding y), then c's σ_(t+1)-cycle.
    - y not on that cycle: val(ρ′, τ)(y) = y ⊕ W_(t+1)(z). Done.
    - y on it, so W_(t+1)(y) = (c, ∅, ℓ_y). The new cycle's top is the top of {c} ∪ P(W_(t+1)(z)); y and the old arc rank below c.
      - Top c (P = ∅): val = (c, ∅, 1 + ℓ(z)) = y ⊕ W_(t+1)(z). ARENA-MAX gives the claim.
      - Top m even: val(ρ′, τ)(y) has cycle node m with reward(m) > reward(c), against ARENA-MAX. Impossible.
      - Top m odd: P(W(z)) has top m odd. y is not added (it is below c), so y ⊕ W_(t+1)(z) = (c, P(W(z)), ·) ◁ (c, ∅, ℓ_y) = W_(t+1)(y).
    - ⊕ is applied to W(z) with y ∉ P(W(z)), because z's path avoids y (E1.12's proviso holds).
  - This is the same four-way split as my R-N5-SRC §3, organised by the top of the new cycle.
  - Own DATA: R-N5-SRC §7 counted the configuration «switched y ∉ C, b ∈ H_(k−1)(y), y on c's σ_k-cycle» 3 times on the n ≤ 100 run set,
    all with top c. REFEREE-2's OS = 0 on 852,572 instances is consistent with this.
- Instantiations (both CONFIRMED):
  - Case 2 = ONE-STEP at t = k − 1 with z = b. Its hypotheses: b ∈ H_(k−1)(y) (Case 2), λ_W(b) = c (y → b on y's W_(k+1)-path, and λ_W is
    fixed), and b's σ_k-path avoids y (shown before Case 1). The conclusion y ⊕ W_k(b) ⊴ W_k(y) is exactly the first inequality of
    Case 2's chain.
  - Case 2b = ONE-STEP at t = k with z = a. Its hypotheses: a = σ_k(y) ∈ H_k(y), λ_W(a) = c, and a's σ_(k+1)-path avoids y (the Case 2b
    hypothesis). The conclusion y ⊕ W_(k+1)(a) ⊴ W_(k+1)(y) is exactly Case 2b's first inequality.
  - Case 2c is unaffected: there the ρ′-play is analysed explicitly (it closes Z).
- Verdict: [SET] §5 (RUN-SETTLE) stays SIGNED, with Case 2 and Case 2b read through ONE-STEP. The same holds for SRC §3.

## DONE / FINDINGS / NEEDS
- DONE: this report; settle_probe.py; settle_logs/.
- FINDINGS:
  1. Every packet item to sign is SIGNED, including T54 LEX-BFS / IDX-MONO as used (re-derived from SPEC S1 (iv)). No gap. Nothing FALSE.
  2. Line: REQUIRED SETTLE-L1 (F), L2 (T), L3 (k); precision L4.
  3. Notes N1 (RG′ word-diff incomplete), N2 (R140 SHA), N3 (DATA: «longest» 44 should be «largest ratio»; longest 63, lane and own engine agree).
- NEEDS: Lead: route SETTLE-L1..L4 and N1-N3 to L-SI; send me the §C word after REFEREE-2's report.
