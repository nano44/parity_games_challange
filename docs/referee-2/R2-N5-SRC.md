# R2-N5-SRC: second-referee report on P-N5-SRC (REFEREE-2 successor 24, Opus 5.5, D15)
- Object: docs/red/P-N5-SRC.md @ l-red 0521fb82, sha1 3caae56e3afdfaab80739c0e12e397b3d6cc7a8b, 195 lines. Line:
  docs/red/P-N5-SRC-line.txt, sha1 3101a0c04f7959ccd50b86f5e6fa76789bdf6995. Both re-hashed: match.
- Base: [SET] = l-si 6a70a520 docs/si/P-N5-SETTLE-box52.md (sha1 aef403c3, re-hashed) and [L-2] = l-si 86becaa0 (sha1 1fcb33c5).
- Independence: written before opening any docs/referee/ file on SRC. I read [SET] and my predecessor's R2-N5-SETTLE.md.
- Scope: a REDUCTION and an EQUIVALENCE inside W-runs. Nothing is bounded. G-N5-TIME stays OPEN.
- Lead 22:17Z asked me to sign §2, §3 (C1-C7), §4 and §5, and not §6.

## 1. Verdict table
| § | item | verdict | gap |
| --- | --- | --- | --- |
| 1 | (R1), (R2), NEW definitions | checked ✓ | none |
| 2 | Lemma PLAY-CAUSE^S | SIGNED | none |
| 3 | (S_j), (X_j) on source blocks, C1-C7 | SIGNED, with G-SRC-1 closed by my Lemma ONE-STEP (§3.2) | G-SRC-1 (inherited from [SET] §5 Case 2 / 2b) |
| 4 | Lemma TAIL (T0), (T1) | SIGNED | none |
| 5 | Theorem SRC-SETTLE; Corollary SRC-COUNT; EQUIVALENCE (both directions) | SIGNED (rests on §3) | none of its own |
| 6 | F1, F2 | not signed (READING); not used in §2-§5: confirmed | — |
| line | proposed RESULTS line | REQUIRED changes SRC-L1, SRC-L2, SRC-L3 (§6) | — |

## 2. §1 and §2
- (R1). In a W-play to c = λ_W(b) ≠ b, every vertex before c has λ_W = c and is not its own cycle node. So no vertex before c is in C.
  - W(b) = (c, the vertices of the path up to c that are more relevant than c, its length). This uses nothing of σ(c).
  - W(c) = (c, ∅, 0) at every state of F, because λ_W(c) = c is fixed on F. ✓
- (R2) is S1. ✓
- PLAY-CAUSE^S, checked step by step.
  - i exists. An Odd y_t ∉ D_(k+1) plays τ. So until S_k the (σ_(k+1), σ̄_(k+1))-play is the W_(k+1)-play, and that play visits
    λ_W(x) ∈ C before it repeats a vertex. The prefix y_0 … y_(i−1) is simple.
  - Ξ(x) is f(y_0 … y_(i−1), Ξ(y_i)), for a fixed f:
    - if the cycle node w of Ξ(y_i) is y_j with j < i, then Ξ(x) = (w, rel(y_0 … y_(j−1)) above w, j);
    - otherwise Ξ(x) = (w, rel(y_0 … y_(i−1)) above w ∪ P(Ξ(y_i)), i + ℓ(Ξ(y_i))).
    The eventual cycle of x's play is that of y_i's play.
  - Suppose no Even y_t with t < i switches. The Odd y_t with t < i are outside D_k ∪ D_(k+1), so σ̄_k(y_t) = τ(y_t) = σ̄_(k+1)(y_t).
    So the (σ_k, σ̄_k)-play has the same prefix and the same i, and S_k is one set for both states. Source-freeness gives
    Ξ_k(y_i) = Ξ_(k+1)(y_i). Hence Ξ_k(x) = Ξ_(k+1)(x).
  - The switching y_t has t < i, so y_t ∉ C, it lies on x's W_(k+1)-path before λ_W(x), and ℓ_(k+1)(x) = t + ℓ_(k+1)(y_t).
  - The word-diff against [SET] §4 is as listed. The packet's new argument covers σ̄-changes, because D_k ∪ D_(k+1) ⊆ S_k. ✓ SIGNED.

## 3. §3 (S_j), (X_j)
### 3.1 C1-C7
- C1: PLAY-CAUSE^S yields y ∉ C, so (S_j) as restricted applies. ✓
- C2: y ∉ C ⇒ λ_W(y) ≠ y ⇒ ℓ ≥ 1. ✓
- C3, C4: the least violator is taken among y ∉ C. (MIN) is then exactly what minimality gives. ✓
- C5: (PATH) on b's path, c excluded.
  - The vertices before c are ∉ C (R1) and have ℓ_(k+1) ≤ L − 1 < L. By (MIN), none of them switches; Odd vertices play τ.
  - So the path up to c is the same at k and k + 1, and W_k(b) = W_(k+1)(b) by (R1), even if c switches. ✓
- C6: keys list the path vertices before c. (MIN) and (PATH) cover a's path in Case 2a (ℓ_(k+1)(a) = L − 1, so y is not on it). ✓
- C7: if no vertex before c on a's σ_k-path switched, a's σ_(k+1)-path up to c would be its σ_k-path, which avoids y. That contradicts
  Case 2c, so u exists. u ∉ C (R1), and u ≠ y. The rest of 2c closes Z before reaching c and never reads σ(c). ✓
- «Nowhere is σ_k(c) compared with σ_(k+1)(c)»: confirmed for Case 1, Case 2a, Case 2b and Case 2c, and for W-MON (ARENA-MAX with
  ρ = σ_k).
### 3.2 G-SRC-1 (a proof-text gap in [SET] §5, inherited by §3): CLOSED by Lemma ONE-STEP (referee-originated)
- Case 2 of [SET] §5 reads: «ρ := σ_k with y ↦ b is a strategy of H_(k−1). Its play from y is y, then b's (σ_k, τ)-path, which avoids
  y.» It then uses val(ρ, τ)(y) = y ⊕ W_k(b).
- That holds only up to c. After c, ρ follows c's (σ_k, τ)-cycle Z_c. y ∉ C does NOT keep y off Z_c: a non-top vertex of c's cycle has
  λ_W = c and is not in C.
- If y ∈ Z_c, the ρ-play runs c → … → y → b → … → c, a different cycle. Its top z* may be a vertex of b's path more relevant than c.
  Then val(ρ, τ)(y) has cycle node z* ≠ c, and the written equality is false.
- Case 2b's «ρ′ := σ_(k+1) with y ↦ a … its play from y is y, then a's (σ_(k+1), τ)-path» has the same gap, with c's
  (σ_(k+1), τ)-cycle.
- [SET]'s two reports did not raise it. Successor 23's §2.5 reads «ARENA-MAX, W-MON, and reflection by y ⊕ · … ✓».
- REACHABLE. My tool finds 4 states (red/n3/instances/ret22_n40.pg with its start file, t = 2-5, y 5, z 23, c 0) where y lies on c's
  cycle, z ∈ H_t(y), z's path avoids y, and the ρ-play's cycle top is 23 (odd), not c.
  - Example: ρ-value (23, ∅, 1) against the written y ⊕ W(z) = (0, {23}, 2).
  - In none of them does y then switch to z, so no instance of Case 2 or 2b itself is wrong. The sentence is false on reachable
    states; the conclusion it feeds is true, by the lemma below.
- **Lemma ONE-STEP** (REFEREE-2 24, PROVED).
  - Statement. Let t → t + 1 be a transition of a W-run F, y ∉ C an Even vertex, c := λ_W(y), z ∈ H_t(y) with λ_W(z) = c, and z's
    (σ_(t+1), τ)-path to c avoiding y. Then y ⊕ W_(t+1)(z) ⊴ W_(t+1)(y).
  - Proof.
    - ρ := σ_(t+1) with y ↦ z is a strategy of H_t: σ_(t+1)(v) ∈ H_t(v) for every Even v, and z ∈ H_t(y). By ARENA-MAX,
      W_(t+1)(y) ⊵ val(ρ, τ)(y). The ρ-play from y is y, then z's path to c (ρ = σ_(t+1) there), then from c along c's
      (σ_(t+1), τ)-cycle Z_c.
    - (α) y ∉ Z_c: the play ends in Z_c with top c, so val(ρ, τ)(y) = y ⊕ W_(t+1)(z). Done.
    - (β) y ∈ Z_c: write Z_c = c → … → y → σ_(t+1)(y) → … → c.
      - z's path meets Z_c only after y: entering the c … y segment would lead to y before c.
      - So Z′ := (the segment of Z_c from c to y) ∪ (z's path) is a simple cycle. Its top z* is c or the most relevant vertex of z's
        path, because c is the top of Z_c.
      - z* = c: val(ρ, τ)(y) = y ⊕ W_(t+1)(z). Done.
      - z* ≠ c, even: reward(z*) = p′(z*) > p′(c) ≥ reward(c), so val(ρ, τ)(y) ▷ W_(t+1)(y). That contradicts ARENA-MAX, so this
        case does not occur.
      - z* ≠ c, odd: y's W_(t+1)-path is the segment of Z_c from y to c, so P(W_(t+1)(y)) = ∅, and y is less relevant than c. Also
        z* ∈ P(W_(t+1)(z)), and z* is its most relevant vertex. So y ⊕ W_(t+1)(z) = (c, P(W_(t+1)(z)), ·) loses to (c, ∅, ·) at the
        odd z*: y ⊕ W_(t+1)(z) ◁ W_(t+1)(y). □
- Use.
  - Case 2 is ONE-STEP at t = k − 1 with z = b. b ∈ H_(k−1)(y) is Case 2's own hypothesis; λ_W(b) = c; b's σ_k-path avoids y. It gives
    exactly «W_k(y) ⊵ y ⊕ W_k(b)», and the chain of Case 2 then reads as written.
  - Case 2b is ONE-STEP at t = k with z = a. It gives «y ⊕ W_(k+1)(a) ⊴ W_(k+1)(y)».
  - Case 2c already closes Z before c. Case 1 uses no ρ. TAIL uses ARENA-MAX only with actual strategies σ_(k+1), σ_(k+2).
  - ONE-STEP reads only one state's strategy, so it holds with C switching (SRC) and without (SETTLE).
- Mechanical: OS = 0 on 852,572 instances (the corpus and 20,000 random runs, §5). OS_newtop_even = 0.
- Status under L41: proved by me. It needs REFEREE's independent signature before §3 (and [SET] §5, i.e. RUN-SETTLE) counts as
  double-signed with an empty gap map. Until then G-SRC-1 is LISTED: §3 is SIGNED by me with this repair.

## 4. §4 Lemma TAIL
- (T0) Ξ: PLAY-CAUSE^S with no switching Even vertex outside C. ✓
- (T0) W: σ is unchanged off C, and (R1). ✓
- (T0) H: off C and at a non-switching c, the arenas are equal (σ(x) is unchanged, and Iσ depends only on Ξ and σ(x)). At a switching
  c (a → b): b ∈ Iσ_k(c), so Iσ_(k+1)(c) = {z : Ξ_k(z) ▷ Ξ_k(b)} ⊆ {z : Ξ_k(z) ▷ Ξ_k(a)}, by transitivity. ✓
- (T1) W_(k+2) = W_(k+1):
  - ⊵ by ARENA-MAX at k + 1 with σ_(k+1) ∈ H_(k+1);
  - ⊴ by ARENA-MAX at k with σ_(k+2) ∈ H_(k+1) ⊆ H_k, an actual strategy, so the value is exactly W_(k+2). ✓
- (T1) choices off C:
  - Equal candidate sets: H_(k+1)(x) = H_k(x) for x ∉ C. Equal tightness: W_(k+2) = W_(k+1). Same c, same branch.
  - IDX branch: immediate.
  - LEX branch: induction on L.
    - L = 1: the only W-tight successor of length 0 with cycle node c is c.
    - L ≥ 2: keys of layer L − 1 read Even vertices ∉ C of ℓ ≤ L − 1 (equal by induction) and Odd vertices (τ). Keys of distinct
      vertices differ in the last coordinate. ✓
  - Both steps are S4a steps of F (k + 1 → k + 2 ∈ F is assumed). ✓
- SIGNED, no gap.

## 5. §5 and DATA
- SRC-SETTLE.
  - (T1) applies inside the block, because each next transition is again source-free. So the C-only transitions form a suffix.
  - Normal positions j satisfy j + 1 ≤ ℓ ≤ n − 1, so there are at most n − 1 of them.
  - In the tail, Ξ* is constant (T0). Each switch of an Even c ∈ C goes into Iσ(c), so Ξ*(σ(c)) strictly rises among |succ(c)| values.
    The tail therefore has at most m_C transitions, since each transition switches some Even vertex ([SET] §1). ✓
- SRC-COUNT: there are at most E^S_F + 1 maximal source-free blocks. ✓
- EQUIVALENCE.
  - ⇐: |F| ≤ (E^S_F + 1)(n + m_C) ≤ (1 + n·max HXS)(n + m_E).
  - ⇒: HXS_F(v) ≤ |F|.
  - E^S_F ≤ Σ HXS: each source event is counted at some v ∈ S_k. ✓
- Note: the line states SRC-SETTLE for MAXIMAL source-free runs, the packet for every source block. The line's form is the narrower one.
- My tool: docs/referee-2/R2-N5-SRC/src_check.py. It is my code: my LATEP state loop and WRUN start handling. Lane xcn/*.py is not
  imported.
  - It checks PCS, S, X, ORD, T0, T1, NRM, TL, BLK, SC, HXS and ONE-STEP (OS), plus XIPLAY / XW / XIMON.
  - Logs are in R2-N5-SRC/logs.
| run | games / runs | violations | longest source block | longest tail | OS checks (y on c's cycle / new top) |
| --- | --- | --- | --- | --- | --- |
| sbcg.lst (runs=1) | 719 / 719 | 0 | 67 (gate_K64_n581) | 1 (tog6b_n32) | 452,450 (3,457 / 0) |
| alt_all, with start (runs=0) | 94 / 94 | 0 | 49 (ladderd0_k48_n156) | 0 | 214,299 (671 / 4, ret22_n40) |
| alt_all, start-less (runs=1) | 319 / 319 | 0 | 55 (x32_rand64) | 1 | 167,786 (2,151 / 0) |
| random seeds 21, 22 (2,500 games each, n 6-16, 4 starts) | 5,000 / 20,000 | 0 | 3 | 1 | 18,037 (2,776 / 0) |
| pins cn3_n9, xcn4_n12 (start files at 0521fb82) | 2 / 2 | 0 | 3 (cn3_n9) | 2 (cn3_n9; E^S = 0) | 47 |
- These equal the lane's maxima: block 67 on gate_K64_n581; tail 1 on the corpus, 2 on cn3_n9.
- I analysed all 1,132 games; the lane reports 2 RUN-ERRORs. My start reader repairs invalid starts (predecessor's convention, notebook),
  so that is a run-set difference, not an engine difference.
- I did not count total source events (the lane's 4,546). DATA is not to sign.

## 6. Proposed line: strict symbol test (clause by clause) and TARGET.md diff
- **SRC-L1 (REQUIRED).** |F| is used in SRC-COUNT («|F| ≤ E^S_F + …», «HXS_F(v) ≤ |F|») and is never defined.
  - Fix: add «|F| := the number of transitions of F» to the definitions. This is the Lead's D-1 for SETTLE L-3.
- **SRC-L2 (REQUIRED).** The quoted R57 premise «for S4a, σ_new is the pointwise optimum of the one-player arena H_t» has t free (H_k is
  the line's symbol), and σ_new is not a line symbol.
  - Fix: «for S4a at a transition k → k + 1, σ_(k+1) is the pointwise optimum of the one-player arena H_k». This is D-2.
- **SRC-L3 (REQUIRED, from G-SRC-1).** The source-block proof note cites «P-N5-SETTLE's RUN-SETTLE induction (l-si 6a70a520,
  signed …)». That induction has the gap of §3.2.
  - Fix: append «, with Case 2 and Case 2b's comparison step by Lemma ONE-STEP (REFEREE-2 docs/referee-2/R2-N5-SRC.md §3.2,
    referee-originated)».
  - Alternatively, state ONE-STEP in the line: «(Lemma ONE-STEP) if y ∉ C is Even, z ∈ H_k(y) has λ_W(z) = λ_W(y) and z's
    (σ_(k+1), τ)-path avoids y, then y ⊕ W_(k+1)(z) ⊴ W_(k+1)(y)». The line then needs ⊕, as [L-2] defines it.
  - The scope tail should say it is referee-originated (L41).
- N-1 (precision). «σ̄-changes, switches at C and σ̄-changes at own Ξ-cycle nodes are not events» → «… are not source events (unless
  they change Ξ at a source)».
- Binders, every other symbol:
  - from SPEC / R89 / the line's definitions: k, k0, k1, x, y, v, c, τ, C, λ_W, ℓ_k, D_k, H_k, S_k, E^S_F, HXS_F, m_C, m_E, n, succ;
  - F by «every W-run F of it»;
  - the sums by their own ranges.
  No other free symbol.
- TARGET.md: no complexity or M-claim. The tail says REDUCTION, G-N5-TIME OPEN, not M3, not a step-4 pass, not a TARGET.md claim. ✓

## Verdict (Opus 5.5, D15)
- §2 PLAY-CAUSE^S: SIGNED.
- §3 (S_j)/(X_j), C1-C7: SIGNED with G-SRC-1, closed by my Lemma ONE-STEP. ONE-STEP awaits REFEREE's independent signature (L41).
- §4 TAIL: SIGNED.
- §5 SRC-SETTLE, SRC-COUNT, EQUIVALENCE: SIGNED.
- Line: REQUIRED SRC-L1, SRC-L2, SRC-L3; N-1 is optional.
- Carried over to SETTLE: G-SRC-1 sits in [SET] §5 itself. RUN-SETTLE (P-N5-SETTLE, R96 in drafting) carries the same gap and needs the
  same repair.
