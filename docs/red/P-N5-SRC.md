# P-N5-SRC (packet, L-RED R147): inside every W-run F of N5, read the heads at the deviation SOURCES S_k := D_k ∪ D_(k+1) ∪ C. Then every stretch of F with no Ξ-change on S_k has ≤ (n − 1) + m_C transitions (Theorem SRC-SETTLE). So |F| ≤ E^S_F + (E^S_F + 1)(n − 1 + m_C), and polynomial W-runs ⇔ polynomial Ξ-changes at D ∪ C (Corollary SRC-COUNT, an EQUIVALENCE). No σ̄-flip, CN or own-node-flip term remains
L-RED successor 35 (Opus 5.5), D1/D18. Lead 2026-10-30 21:38Z: «FREEZE a packet P-N5-SRC for the referees. It is SRC-SETTLE as a delta on
P-N5-SETTLE … PLAY-CAUSE^S, the new step (T) in full, and Theorem SRC-SETTLE with its corollary (polynomial W-runs ⟺ HXS-POLY, both
directions). Quote the SETTLE pieces you reuse verbatim, with SHA (l-si 6a70a520 packet; L-2 line). Format: exact statements, proofs, data
pins, and a proposed RESULTS line with no heading marker and every symbol bound.» FROZEN 2026-10-30 (this commit). The sha1 of this file
and of the line file are reported to the Lead.
- Source: docs/red/R147-xcn.md (working note, l-red 47fd9163). Where the two differ, THIS packet governs.
- Base packet: P-N5-SETTLE, l-si 6a70a520 docs/si/P-N5-SETTLE-box52.md (sha1 aef403c3d8a003bcfc6742c4d1da084a1e21669f), quoted below as
  [SET]. Its line revision is L-2, l-si 86becaa0 docs/si/P-N5-SETTLE-line-L2.txt (sha1 1fcb33c5d96a20eb70abe06c29154ef343b33ae0), quoted as
  [L-2]. [SET]'s fixes file (entries F0, 1, 2) applies; entry 1's E1.12 (⊕ monotone only on path sets without the added vertex) is used in
  §5 below.
- Status: a REDUCTION and an EQUIVALENCE. No count is bounded here. G-N5-TIME stays OPEN. Not M3, not a step-4 pass, not a TARGET.md claim.
- Object: N5 only (SPEC S1-S5).

## 0. What to sign
| § | item | origin | label |
| --- | --- | --- | --- |
| 2 | Lemma PLAY-CAUSE^S | L-RED, new (a word-diff of [SET] §4 PLAY-CAUSE, given in full) | PROVED (to sign) |
| 3 | (S_j), (X_j) on source blocks: [SET] §5's induction restricted to Even vertices outside C | L-RED, new (a word-diff of [SET] §5, listed change by change) | PROVED (to sign) |
| 4 | Lemma TAIL (step (T)) | L-RED, new, in full | PROVED (to sign) |
| 5 | Theorem SRC-SETTLE; Corollary SRC-COUNT (EQUIVALENCE, both directions) | L-RED, new | PROVED / EQUIVALENCE (to sign) |
| 1 | [SET] §1 definitions, §3 Claim RG′, §4 W-MON and PATH, §5 Cases 1-2c; [L-2]'s premises | L-SI, signed (both referees; [SET] fixes entry 1) | quoted, NOT re-signed |
| 6 | Fact F1 (CN switch with Ξ(c) fixed ⇒ c is its own Ξ-cycle node); Fact F2 | — | READING, NOT to sign |
| 7 | DATA, pins | — | NOT to sign |

## 1. Setting (from [SET] §1, verbatim where quoted)
- Everything of [SET] §1 is used as stated there: N5, V, n, m_E, values (c, P, ℓ), ⊴ / ◁ / ⊵ / ▷, ⊕, Ξ_k, σ̄_k, W_k, ℓ_k, Iσ_k, H_k,
  W-run, τ, C, D_k, [R57], [R15]. Quoted pieces:
  - «W-run, RESULTS R89 verbatim: «a τ-stretch := a maximal run of consecutive states with τ constant; a W-run := a maximal run of
    consecutive states of one τ-stretch none of whose transitions is an S4c fallback or changes λ_W».»
  - «In a W-run F, τ_k =: τ and C := {v : λ_W(v) = v} are fixed.»
  - «Every transition of F switches some Even vertex: with τ fixed and no S4c fallback, S4a changed σ (SPEC S4).»
  - «Odd vertices in W-plays follow τ; D_k := {Odd o : σ̄_k(o) ≠ τ(o)}.»
  - «H_k := S4a's arena at k: Even v keeps {σ_k(v)} ∪ Iσ_k(v), Odd follows τ_k».
- ARENA-MAX (L-RED R140 §2, l-red 47000632, as quoted in [SET] §2): «Let H_t be the arena of S4a at state t: Even v restricted to
  {σ_t(v)} ∪ Iσ_t(v), Odd fixed to τ_t. Then for every vertex v and every Even strategy ρ of H_t: W_(t+1)(v) ⊵ val(ρ, τ_t)(v), with
  W_(t+1) := val(σ_(t+1), τ_t).»
- [SET] §3 Claim RG′ and T54 LEX-BFS / IDX-MONO (as quoted in [SET] §2, read at one S4a evaluation with W_(k+1), as signed):
  - IDX-MONO: «If Even v ≠ c := λ_W(v) and Ω(c) is odd, then σ_{k+1}(v) = the smallest-index W-tight edge of {σ_k(v)} ∪ Iσ_k(v).»
  - LEX-BFS: «If Ω(c) is even and v ≠ c is Even, then σ_{k+1}(v) = argmin over the W-tight arena edges y of key_{σ_{k+1}}(y).»
  - Key: «key_σ(x) := (x_{ℓ−1}, …, x_1, x_0), where x = x_0 → x_1 → … → x_ℓ = c is the (σ, τ) path».
- NEW definitions (this packet). Fix a W-run F.
  - For a transition k → k + 1 of F: SOURCES S_k := D_k ∪ D_(k+1) ∪ C.
  - A SOURCE EVENT is a transition k → k + 1 of F at which Ξ_(k+1)(v) ≠ Ξ_k(v) for some v ∈ S_k. A transition is SOURCE-FREE iff it is
    not a source event. E^S_F := the number of source events of F.
  - HXS_F(v), for v ∈ V := the number of transitions k → k + 1 of F with v ∈ S_k and Ξ_(k+1)(v) ≠ Ξ_k(v). So E^S_F ≤ Σ_(v ∈ V) HXS_F(v).
  - A transition of F is C-ONLY iff every Even vertex that switches at it is in C, and NORMAL otherwise.
  - m_C := Σ over the Even c ∈ C of (|succ(c)| − 1). So m_C ≤ m_E.
- Two remarks used below, with proofs.
  - (R1) For b with λ_W(b) = c ≠ b, W_k(b) = (c, the relevant vertices of b's (σ_k, τ)-path up to its first visit of c, its length).
    No vertex of that path before c is in C: a W-path to c meets no other W-cycle node. So W_k(b) does not depend on σ_k(c), and W_k(c)
    does not depend on σ_k at all. This is the reading of [SET] §4 (PATH)'s own parenthesis «W(b) = (c, the relevant vertices of the
    path, its length); c ∈ C at both states».
  - (R2) In a state, Ξ is a function of σ alone (S1: Ξ_k := val(σ_k, σ̄_k), σ̄_k := S1's Odd counter-strategy to σ_k).

## 2. Lemma PLAY-CAUSE^S (PROVED, to sign)
- Statement. Let k → k + 1 be a source-free transition of F. If Ξ_(k+1)(x) ≠ Ξ_k(x), then some Even y with λ_W(y) ≠ y switches at k
  and lies on x's (σ_(k+1), τ)-path to λ_W(x). In particular ℓ_(k+1)(x) ≥ ℓ_(k+1)(y).
- Proof.
  - Let x = y_0, y_1, … be the (σ_(k+1), σ̄_(k+1))-play, and i the least index with y_i ∈ S_k.
  - i exists. An Odd y_t ∉ D_(k+1) follows τ, so before S_k the play is the (σ_(k+1), τ)-play, which reaches λ_W(x) ∈ C ⊆ S_k.
  - Every value on a play is (cycle node w of its eventual cycle, the vertices of the path to the first occurrence of w that are more
    relevant than w, the length of that path).
    - The eventual cycle of x's play is that of y_i's play, and w is read off Ξ(y_i).
    - If w = y_j for some j < i, the path is y_0 … y_j.
    - Otherwise the path is y_0 … y_(i−1) followed by the path of Ξ(y_i). (If w = y_i, that path is empty.)
  - So Ξ_(k+1)(x) is determined by the sequence y_0 … y_(i−1) and the value Ξ_(k+1)(y_i), by a function that does not depend on k.
  - Suppose no Even y_t with t < i switches at k.
    - Every Odd y_t with t < i is outside D_k ⊆ S_k, so σ̄_k(y_t) = τ(y_t) = σ̄_(k+1)(y_t).
    - So the (σ_k, σ̄_k)-play from x is y_0 … y_(i−1), y_i, …, with the same first index i.
    - The same function gives Ξ_k(x) from y_0 … y_(i−1) and Ξ_k(y_i).
    - y_i ∈ S_k and the transition is source-free, so Ξ_k(y_i) = Ξ_(k+1)(y_i). Hence Ξ_k(x) = Ξ_(k+1)(x), a contradiction.
  - So some Even y_t with t < i switches at k.
    - It is not in C, since C ⊆ S_k and t < i.
    - It lies on x's (σ_(k+1), τ)-path before λ_W(x), so ℓ_(k+1)(x) = t + ℓ_(k+1)(y_t). □
- Word-diff against [SET] §4 PLAY-CAUSE (quoted there verbatim):
  - «event-free» → «source-free»;
  - «i the least index with y_i ∈ D_(k+1) ∪ C» → «… with y_i ∈ S_k»;
  - the head value «Ξ(y_(i+1)), y_(i+1) ∈ U_(k+1)» → the source value «Ξ(y_i), y_i ∈ S_k» («j ≤ i» → «j < i»);
  - the sentences «If y_i ∈ C is Even it does not switch, by no event (ii)» and «σ̄_k = σ̄_(k+1) and D_k = D_(k+1) (no event (i))» are
    replaced by «every Odd y_t with t < i is outside D_k ⊆ S_k»;
  - «(no event (iii); y_(i+1) ∈ U_(k+1))» → «(source-free; y_i ∈ S_k)».

## 3. (S_j) and (X_j) on a source block (PROVED, to sign)
- Statement. Let the transitions k0, k0 + 1, …, k1 − 1 of F all be source-free (a SOURCE BLOCK). For k0 ≤ k < k1 put j := k − k0.
  - (S_j) Every Even y ∉ C that switches at k has ℓ_(k+1)(y) ≥ j + 1.
  - (X_j) Every vertex x with Ξ_(k+1)(x) ≠ Ξ_k(x) has ℓ_(k+1)(x) ≥ j + 1.
- Proof: [SET] §5's «Proof of the theorem» (quoted there in full), with exactly the following changes.
  - C1. «S_j ⇒ X_j by PLAY-CAUSE» → «S_j ⇒ X_j by PLAY-CAUSE^S». PLAY-CAUSE^S gives a switching y ∉ C with ℓ_(k+1)(x) ≥ ℓ_(k+1)(y), and
    S_j applies to it.
  - C2. «j = 0. A switched y is not in C (no event (ii)), so ℓ_(k+1)(y) ≥ 1.» → «j = 0. A switched y ∉ C has ℓ_(k+1)(y) ≥ 1.»
  - C3. «Among the switched Even y with ℓ_(k+1)(y) ≤ j» → «Among the switched Even y ∉ C with ℓ_(k+1)(y) ≤ j».
  - C4. «(MIN) No Even u with ℓ_(k+1)(u) < L switches at k.» → «(MIN) No Even u ∉ C with ℓ_(k+1)(u) < L switches at k.»
  - C5. (PATH) is applied to «the path from b to c, c excluded».
    - Justification (R1): every vertex of that path except c is outside C, and W(b) and the path up to c do not depend on σ(c). So (MIN)
      of C4 gives exactly [SET]'s conclusions: «W_k(b) = W_(k+1)(b), ℓ_k(b) = L − 1, and b's (σ_k, τ)-path is its (σ_(k+1), τ)-path»,
      up to c. The same holds for a in Case 2a.
  - C6. Case 2a: «key_(σ_k) = key_(σ_(k+1)) on a and on b» holds because a key lists the path vertices before c (Key, §1). The sentence
    «y ∉ C, so the CN branch does not arise» stands (y ∉ C by C3).
  - C7. Case 2c: «Let u be the first vertex on it that switches at k. u exists, u ∉ C, u ≠ y.» →
    «Let u be the first vertex before c on it that switches at k. u exists: otherwise a's (σ_(k+1), τ)-path up to c would be its
    (σ_k, τ)-path, which avoids y. u ∉ C and u ≠ y.»
- Why no other step changes.
  - [SET] §5 uses events only in PLAY-CAUSE (C1) and in «j = 0» (C2).
  - The values of the comparison strategies (ρ := σ_k with y ↦ b in Case 2; ρ′ := σ_(k+1) with y ↦ a in Cases 2b and 2c) are each read
    under ONE strategy, σ_k or σ_(k+1). Nowhere is σ_k(c) compared with σ_(k+1)(c). So letting C switch at k changes nothing there.
  - Case 1, W-MON and ARENA-MAX are used as in [SET].
  - Case 2b's «⊕ is monotone on values with cycle node c» is read with [SET] fixes E1.12's restriction (path sets not containing y), as
    the referees signed it.
- □

## 4. Lemma TAIL (step (T); PROVED, to sign)
- Statement. Let k → k + 1 be a source-free C-only transition of F.
  - (T0) Ξ_(k+1) = Ξ_k, W_(k+1) = W_k, and H_(k+1) ⊆ H_k (arena by arena).
  - (T1) If k + 1 → k + 2 is a transition of F, it is C-only: σ_(k+2)(x) = σ_(k+1)(x) for every Even x ∉ C.
- Proof of (T0).
  - Ξ_(k+1) = Ξ_k: by PLAY-CAUSE^S, a Ξ-change would need a switching Even vertex outside C, and there is none.
  - W_(k+1) = W_k: σ_(k+1) = σ_k off C, and by (R1) no W-value depends on σ on C. (λ_W is fixed on F.)
  - H_(k+1)(x) ⊆ H_k(x) for every Even x.
    - x ∉ C: σ_(k+1)(x) = σ_k(x), and Iσ_(k+1)(x) = Iσ_k(x) because Ξ_(k+1) = Ξ_k. So the arenas are equal.
    - x = c ∈ C that does not switch: the same argument; equal.
    - c ∈ C switching from a := σ_k(c) to b := σ_(k+1)(c): b ∈ H_k(c) ∖ {a}, so b ∈ Iσ_k(c), i.e. Ξ_k(b) ▷ Ξ_k(a). Then
      Iσ_(k+1)(c) = {z : Ξ_k(z) ▷ Ξ_k(b)} ⊆ {z : Ξ_k(z) ▷ Ξ_k(a)} = Iσ_k(c), by transitivity of ▷. So H_(k+1)(c) = {b} ∪ Iσ_(k+1)(c) ⊆ H_k(c).
  - Odd vertices follow τ in both arenas. □
- Proof of (T1).
  - W_(k+2) = W_(k+1).
    - ⊵: ARENA-MAX at k + 1 with ρ := σ_(k+1), a strategy of H_(k+1).
    - ⊴: σ_(k+2) is a strategy of H_(k+1) ⊆ H_k, so ARENA-MAX at k with ρ := σ_(k+2) gives W_(k+1) ⊵ val(σ_(k+2), τ) = W_(k+2).
  - Let x ∉ C be Even, with c := λ_W(x) (fixed on F) and L := ℓ_(k+1)(x) = ℓ_(k+2)(x) ≥ 1.
  - By Claim RG′ with IDX-MONO / LEX-BFS, read at the evaluations of H_k and of H_(k+1):
    - σ_(k+1)(x) is the ≺-least W_(k+1)-tight edge of H_k(x);
    - σ_(k+2)(x) is the ≺-least W_(k+2)-tight edge of H_(k+1)(x).
  - The candidate sets are equal: H_(k+1)(x) = H_k(x) by (T0), and W_(k+2) = W_(k+1). The branch (the parity of Ω(c)) is the same.
  - Ω(c) odd: ≺ is the index order, so σ_(k+2)(x) = σ_(k+1)(x).
  - Ω(c) even: ≺ compares key_(σ_(k+2)) at step k + 1 and key_(σ_(k+1)) at step k on the tight successors, which have layer L − 1.
    Induction on L:
    - L = 1: the only tight successor is c, so the choice is c at both steps.
    - L ≥ 2: by induction σ_(k+2) = σ_(k+1) on every Even vertex outside C with ℓ ≤ L − 1. Those are exactly the Even vertices before c
      on the paths that the keys of layer-(L − 1) successors read. So the keys agree, and so do the argmins (keys of distinct vertices
      differ in their last coordinate).
  - So σ_(k+2) = σ_(k+1) off C. Every transition of F switches some Even vertex ([SET] §1), so if k + 1 → k + 2 is in F it is C-only. □

## 5. Theorem SRC-SETTLE and Corollary SRC-COUNT (PROVED, to sign; premises: [R57], [R15] (a), ARENA-MAX, Claim RG′, LEX-BFS / IDX-MONO, as in [SET] §5)
- Theorem SRC-SETTLE. For every N5 run on every game, every W-run F of it, and every source block k0, …, k1 − 1 of F:
  k1 − k0 ≤ (n − 1) + m_C.
- Proof.
  - By (T1) and induction along the block: once a transition of the block is C-only, every later transition of the block is C-only.
    So the block is a run of normal transitions followed by a run of C-only transitions (the TAIL). Either part may be empty.
  - Normal part. A normal transition at k switches some Even y ∉ C. By (S_j), j + 1 ≤ ℓ_(k+1)(y) ≤ n − 1 (a path to the cycle node is
    simple). So the normal transitions sit at positions j ≤ n − 2: at most n − 1 of them.
  - Tail. By (T0), Ξ is the same at every state of the tail; call it Ξ*.
    - An Even c ∈ C switches in the tail only from σ(c) to a member of Iσ(c), i.e. to a successor z with Ξ*(z) ▷ Ξ*(σ(c)).
    - So along the tail, Ξ*(σ(c)) strictly increases at each switch of c, among the |succ(c)| values Ξ*(z), z ∈ succ(c). That is at most
      |succ(c)| − 1 switches of c.
    - Every transition of F switches some Even vertex, and in the tail only C does. So the tail has at most m_C transitions.
  - Total: k1 − k0 ≤ (n − 1) + m_C. □
- Corollary SRC-COUNT. For every N5 run on every game and every W-run F of it, |F| ≤ E^S_F + (E^S_F + 1)(n − 1 + m_C).
  - Proof: the source-free transitions form at most E^S_F + 1 maximal source blocks.
- EQUIVALENCE (both directions). For every family of games, every W-run has polynomially many transitions iff max_(v ∈ V) HXS_F(v) is
  polynomial over all W-runs F.
  - ⇐: E^S_F ≤ Σ_(v ∈ V) HXS_F(v) ≤ n·max_v HXS_F(v), and m_C ≤ m_E. So |F| ≤ (1 + n·max_v HXS_F(v))(n + m_E).
  - ⇒: HXS_F(v) ≤ |F| for every v.
- Against [SET] §6 HEAD-RED and L-SI box 53's HEAD-RED′ (READING, not to sign):
  - the terms SB_F, CN_F and XCN_F do not occur, and ROOT-FLIP is not used;
  - the heads are the sources D ∪ C in place of the targets U (or U ∪ τ(Odd)).

## 6. Facts (READING, NOT to sign)
- F1. A CN switch at Even c ∈ C (a → b) with Ξ_(k+1)(c) = Ξ_k(c) has λ_Ξ(c) = c at k or at k + 1.
  - Sketch. Otherwise Ξ(c) = c ⊕ Ξ(σ(c)) at both states, and Ξ_(k+1)(b) ⊵ Ξ_k(b) ▷ Ξ_k(a). The step through c ⊕ needs E1.12's proviso
    (c in neither path set). I have not proved that proviso here.
  - DATA: CNOX = 0 on the corpus and on 10,000 random games. NOT to sign. Not used in §2-§5.
- F2. A σ̄-flip at an Odd o with λ_Ξ(o) = o at k and at k + 1 changes no Ξ-value: by (R2), and Ξ(o) = (o, ∅, 0). Not used in §2-§5.

## 7. DATA and pins (NOT to sign)
- Tools: l-red experiments/red/xcn/.
  - srcsettle.py checks (S_j)/(X_j) on source blocks (VIOL2), Lemma TAIL (TAILV), the block bound (BLKV) and F1 (CNOX) on n5b SPEC traces;
  - xcn.py counts XCN and CN per W-run;
  - xclimb.py, xsearch.py and srcrand.py are the searches.
- Corpus: box 50b's lists (sbcg 719 + alt 413) = 1,132 games; xcn/runsrc.sh → xcn/src_corpus.txt.
  - 1,130 games analysed. 2 RUN-ERROR: n3cov_phi and n3cov_lean, the invalid starts of L-RED R99.
  - VIOL2 0, TAILV 0, BLKV 0, CNOX 0.
  - Source events 4,546 against [SET]'s events 4,724.
  - Longest source block 67 (red/usplit/instances/gate_K64_n581, n 581). This is [SET] fixes E1.11's longest event-free block. Longest
    C-only tail 1.
- Random games (srcrand.py seeds 11-14, 2,500 each, n 6-14; xcn/srcrand_out.txt): all four counters 0.
  - Weak evidence: random W-runs are short (|F| ≤ 3).
- Pins (experiments/red/check.sh «R147»; sha1 in xcn/pins.sha1; xeng state sequences identical; Oink 8fbf0a7 --zlk winners equal and
  verify passes):
  - xcn/instances/xcn4_n12: 4 own-node σ̄-flips at ONE Odd vertex in a W-run of length 4;
  - xcn/instances/cn3_n9: 3 CN switches at ONE c, all with Ξ(c) unchanged. The W-run has no source event (E^S_F = 0, |F| = 3); its single
    source block ends in a C-only tail of 2 transitions.
- These show that the dropped terms are not O(1) per W-run, so SRC-SETTLE is not vacuous against [SET]'s event set.

## Proposed RESULTS line
- docs/red/P-N5-SRC-line.txt (one line, no heading marker; sha1 reported with this packet).
