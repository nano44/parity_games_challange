# R-N5-SRC: REFEREE report on packet P-N5-SRC (L-RED R147): PLAY-CAUSE^S, (S_j)/(X_j) on source blocks, Lemma TAIL, Theorem SRC-SETTLE, Corollary SRC-COUNT
Referee: REFEREE (successor 20), Opus 5.5 (D15). Lead brief 2026-10-30 22:17Z (date -u). REFEREE-2 24 reviews independently.
- Object and pin: docs/red/P-N5-SRC.md at claude/l-red 0521fb82, `git show 0521fb82:<path> | sha1sum` =
  3caae56e3afdfaab80739c0e12e397b3d6cc7a8b (195 lines). Line docs/red/P-N5-SRC-line.txt sha1 3101a0c04f7959ccd50b86f5e6fa76789bdf6995.
  Both equal the Lead's figures.
- Base: P-N5-SETTLE ([SET], l-si 6a70a520, sha1 aef403c3) and its line L-2 (86becaa0, sha1 1fcb33c5). I refereed both
  (R-N5-SETTLE 1df722e9, R-N5-SETTLE-C §5 d6a33b10).
- Runs 2026-10-30T22:17Z-22:20Z; report written from 22:19Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independence: I opened no docs/referee-2/ file for this packet.
- Quotes: the [SET] pieces in §1 are those I quote-checked for R-N5-SETTLE: verbatim, and ARENA-MAX verbatim at 47000632. The word-diff
  lists of §2 and §3 match [SET] §4 and §5 as I read them.
- Scope (D1): a REDUCTION and an EQUIVALENCE inside W-runs of N5. No count is bounded. G-N5-TIME stays OPEN. Not a TARGET.md claim.

## Verdicts
| § | item | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| 1 | new definitions; (R1), (R2) | CHECKED. (R1) ✓: within F, C is fixed. A W-path to c meets no other W-cycle node before c, so W(b) does not depend on σ(c), and W(c) = (c, ∅, 0) |
| 2 | Lemma PLAY-CAUSE^S | SIGNED |
| 3 | (S_j), (X_j) on source blocks (changes C1-C7) | SIGNED. One sub-case is omitted from [SET] §5 Cases 2 and 2b, which this packet reuses: GAP G-SRC-1, closed here (§3). It also applies to [SET] |
| 4 | Lemma TAIL (T0), (T1) | SIGNED |
| 5 | Theorem SRC-SETTLE; Corollary SRC-COUNT (EQUIVALENCE, both directions) | SIGNED |
| 6-7 | F1, F2, DATA, pins | not signed. Pins re-run with my own engine (§7) |
| — | RESULTS line (3101a0c0) | REQUIRED CHANGES: SRC-L1 (|F| undefined), SRC-L2 (t free in the R57 gloss «H_t»). These are the same two soft spots the R96 drafter found in SETTLE L-2. Precision SRC-L3 (§8) |

## 2. PLAY-CAUSE^S
- i (the first index in S_k) exists ✓: an Odd vertex outside D_(k+1) follows τ, and λ_W(x) ∈ C ⊆ S_k.
- Ξ(x) is a function of (y_0 … y_(i−1), Ξ(y_i)) ✓.
- With no Even switch before i, every Odd y_t (t < i) lies outside D_k ∪ D_(k+1). So σ̄_k(y_t) = τ(y_t) = σ̄_(k+1)(y_t), and the k-play
  has the same prefix and the same first index.
- Source-freeness gives Ξ_k(y_i) = Ξ_(k+1)(y_i) ✓.
- The switching y_t has t < i, so y_t ∉ C ✓.
- This is a genuine strengthening of [SET]'s PLAY-CAUSE: it needs no «no σ̄-change» and no «no CN switch», because S_k contains D_k ∪
  D_(k+1) and C itself.

## 3. (S_j)/(X_j): C1-C7, and G-SRC-1
- C1-C7 ✓.
  - [SET] §5 uses its events only in PLAY-CAUSE and in j = 0.
  - With C allowed to switch, PATH holds «up to c» by (R1).
  - Keys list only the path vertices before c.
  - Case 2c's u is taken before c.
  - Each comparison strategy (ρ, ρ′) is read under one strategy, so σ_k(c) and σ_(k+1)(c) are never compared. That is right.
- G-SRC-1 (exposition gap, in [SET] §5 and inherited here; CLOSED by the sub-case below). The claim is unaffected.
  - In Case 2, [SET] writes «ρ := σ_k with y ↦ b … Its play from y is y, then b's (σ_k, τ)-path, which avoids y», and then uses
    val(ρ, τ)(y) = y ⊕ W_k(b).
  - That holds only if y is NOT on c's σ_k-cycle. If y ≠ c lies on c's σ_k-cycle (then W_k(y) = (c, ∅, ℓ_y)), the ρ-play from y runs y,
    b's path to c, then c's old arc back to y. It closes a different cycle, whose top is the top m of P := P(W_k(b)) if P ≠ ∅.
  - Case 2b has the same pattern with ρ′ = σ_(k+1)[y ↦ a] and «y on c's σ_(k+1)-cycle».
  - Closing argument (Case 2; Case 2b is identical with σ_(k+1), a, ARENA-MAX at k → k + 1). The inequality the proof needs,
    W_k(y) ⊵ y ⊕ W_k(b), holds in every sub-case:
    - (i) y is not on c's σ_k-cycle: as written.
    - (ii) y is on it and P = ∅: the new cycle has top c, so val(ρ, τ)(y) = (c, ∅, 1 + ℓ_k(b)) = y ⊕ W_k(b), and ARENA-MAX applies as
      written.
    - (iii) y is on it and m is even: val(ρ, τ)(y) has cycle node m with reward(m) > reward(c). That contradicts ARENA-MAX
      (W_k(y) ⊵ val(ρ, τ)(y)), so (iii) cannot occur.
    - (iv) y is on it and m is odd: y ⊕ W_k(b) = (c, P ∪ …, ·) ◁ (c, ∅, ℓ_y) = W_k(y) directly. The symmetric difference is P ∪ ({y} if
      relevant), but y is below c on c's cycle, so it is P, whose top is odd.
    - So W_k(y) ⊵ y ⊕ W_k(b) in all cases, and the rest of Case 2 proceeds as written. In (iv) the chain W_k(y) ▷ y ⊕ W_k(b) = W_(k+1)(y) ⊵
      W_k(y) is a contradiction, so (iv) is in fact excluded too.
  - DATA: my control counts the sub-case (switched y ∉ C, b ∈ H_(k−1)(y), y on c's σ_k-cycle) on the run set: 3 occurrences, all of type (ii) (P = ∅, so the written formula happens to be right). (iii) and (iv) never occur, as the argument predicts.
  - Consequence for [SET]: both referees signed [SET] §5 (R-N5-SETTLE, R2-N5-SETTLE) without this sub-case. The theorem is unaffected. A
    [SET] fixes entry should record the four-way split. I report it to the Lead as a joint miss. It does not change [SET]'s line.

## 4. Lemma TAIL
- (T0) ✓.
  - Ξ is unchanged by PLAY-CAUSE^S.
  - W is unchanged by (R1): σ changes only on C.
  - Arenas off C are equal (same σ, same Iσ). A non-switching c is equal too.
  - For a switching c (a → b, b ∈ Iσ_k(c)): Iσ_(k+1)(c) = {z : Ξ_k(z) ▷ Ξ_k(b)} ⊆ Iσ_k(c) by transitivity, and b ∈ H_k(c).
- (T1) ✓.
  - W_(k+2) = W_(k+1): ⊵ is W-MON. For ⊴, σ_(k+2) ∈ H_(k+1) ⊆ H_k, so ARENA-MAX at k gives it.
  - The tight candidate sets of x ∉ C are equal at both evaluations, and the parity branch is the same.
  - Odd c: the smallest index is the same.
  - Even c: induction on L. L = 1: the only tight successor of layer 0 with cycle node c is c. L ≥ 2: the keys of the layer-(L − 1)
    successors read only Even vertices ∉ C with ℓ ≤ L − 1, which are fixed by induction.
  - Hence σ_(k+2) = σ_(k+1) off C.
  - Note: (T1) uses only that k → k + 1 is source-free and C-only. It does not need k + 1 → k + 2 to be source-free, as the statement says.

## 5. SRC-SETTLE, SRC-COUNT
- The normal prefix holds by (T1) and induction. Normal positions j ≤ n − 2 by (S_j) and ℓ ≤ n − 1: at most n − 1 ✓.
- Tail ✓.
  - Ξ* is constant (T0).
  - c switches only to Iσ*(c), so Ξ*(σ(c)) strictly rises among |succ(c)| values: at most |succ(c)| − 1 switches.
  - Every tail transition switches some c (STEP-SW): at most m_C.
- SRC-COUNT ✓: E^S_F + 1 blocks.
- Equivalence ✓: |F| ≤ (E + 1)(n + m_C) − 1 ≤ (1 + n·max HXS)(n + m_E), and HXS ≤ |F|.

## 7. Controls (own engine; docs/referee/scratch/src_probe.py, adapted from settle_probe.py)
- Checks:
  - BLK: source blocks ≤ (n − 1) + m_C; RC: SRC-COUNT; HR: E^S ≤ Σ HXS;
  - T1 / T0: a C-only transition is followed only by C-only ones, with Ξ and W unchanged;
  - SJ, XJ, PC (PLAY-CAUSE^S);
  - IDX, LEX: the choice rules; CYC: G-SRC-1's sub-case count.
- Results: box 83 / 50b lists, n ≤ 100: 813 runs (740 games, 73 skipped), all RC 0, 1,060 W-runs, 8,066 transitions.
  - 12,729 PLAY-CAUSE^S checks; 27,157 IDX and 266,486 LEX checks. VIOLATIONS 0 for every check.
  - Longest source block 63 (n ≤ 100; the packet's 67 is gate_K64_n581, n 581, outside my MAXN). Longest C-only tail 1 (packet ✓).
  - MUT 1 (block bound one less) never bites: the bound (n − 1) + m_C is not tight on the corpus.
- Pins (from the frozen worktree; sha1 equal to xcn/pins.sha1):
  - cn3_n9 (0d5eb838…, .start): |F| 3, one source block of 3 ending in a C-only tail of 2 (packet ✓);
  - xcn4_n12 (e43dc878…, .start): W-run of 4 (packet ✓).
  - 0 violations on both.

## 8. RESULTS line (3101a0c0)
- Content: each clause states the packet's §2-§5 item and nothing more. The SRC-SETTLE clause says «every maximal run … of source-free
  transitions», a narrowing of §5's «every source block», which is acceptable.
- SRC-L1 (REQUIRED): |F| is used in SRC-COUNT («|F| ≤ E^S_F + …», «HXS_F(v) ≤ |F|», «polynomially many transitions») but never defined.
  This is the same as the R96 drafter's D-1 on SETTLE L-2. Fix: «W-run F := … , |F| its number of transitions».
- SRC-L2 (REQUIRED): t is free in the R57 gloss «the one-player arena H_t». This is the same as D-2 on SETTLE L-2. Fix: use «H_k» (defined
  later «for a state k of F») or «for S4a at a state t, … H_t := S4a's arena at t».
- SRC-L3 (precision):
  - «n := |V|»: V is not named (the vertex set of the game).
  - The proof note «RUN-SETTLE induction … signed» could add «(with the Case 2 / 2b sub-case of R-N5-SRC §3, G-SRC-1)».
- Token pass otherwise clean:
  - run, transition, switches, n, m_E, succ, values, the order, Ξ_k, σ̄_k, Iσ_k, W-run, τ, C, W_k, ℓ_k, D_k, H_k, S_k, source event /
    source-free, C-only, E^S_F, HXS_F, m_C are all bound;
  - k0 and k1 are bound in their clauses; x and y are bound in PLAY-CAUSE^S; v is bound in its clauses.
- Verdict: MATCHES the signed items once SRC-L1 and SRC-L2 are applied.

## DONE / FINDINGS / NEEDS
- DONE: this report; src_probe.py; src_logs/.
- FINDINGS:
  1. Every item to sign is SIGNED.
  2. G-SRC-1: a sub-case (y on c's cycle) is missing in the reused [SET] §5 Cases 2 / 2b. It is closed here by a four-way split, and the
     claims are unaffected. Both referees missed it in SETTLE.
  3. Line: REQUIRED SRC-L1 (|F|), SRC-L2 (H_t); precision SRC-L3.
- NEEDS: Lead: record G-SRC-1 in both fixes files ([SET] and SRC); route SRC-L1..L3 to L-RED; send me the §C word after REFEREE-2 24's report.
