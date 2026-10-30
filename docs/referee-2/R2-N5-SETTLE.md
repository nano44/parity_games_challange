# R2-N5-SETTLE: independent second-referee report on P-N5-SETTLE (REFEREE-2 successor 23, Opus 5.5, D15)
Object: docs/si/P-N5-SETTLE-box52.md @ l-si 6a70a520 (sha1 aef403c3d8a003bcfc6742c4d1da084a1e21669f, 248 lines); line
docs/si/P-N5-SETTLE-line.txt (sha1 6aa094e32b03317797a551ac2fc719749cf59ca7). Both re-hashed in a detached worktree at 6a70a520: match the
Lead's 18:43Z figures. Independence: written before opening any docs/referee/ file for SETTLE.
Sources opened: RESULTS R15 (a), (d), R57, R86 (a) (and its dual sentence), R89; L-RED R143 docs/red/R143-settle.md @ 717f407a; L-LIT T54
docs/lit/T54-stalling.md @ 96cfda95 §4.1-§4.2; L-RED R140 @ 47000632; SPEC S1-S4 and experiments/si/si.py Engine.evaluate l. 78-203 (the
code Claim RG′, LEX-BFS and IDX-MONO are about).
Owner rulings: D1 «Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.»; D18 «Clearly
distinguish proven results from conjectures and open problems.»
Scope: REDUCTIONS and one EQUIVALENCE inside W-runs of N5, plus a whole-run reformulation (T-XCH). Nothing is bounded. G-N5-TIME stays OPEN.

## 1. Verdict table
| § | item | verdict (Opus 5.5, D15) | gaps / notes |
| --- | --- | --- | --- |
| 1 | setting, premises | CHECKED | N-1: «y ⊕ · preserves and reflects ⊴ and ◁» on one cycle node needs y ∉ P of both arguments (the WRUN Fact EXT point); every use satisfies it |
| 2 | quotes | R143, T54, R89, R57, R15, R86 quotes verbatim at their SHAs | N-2: the ARENA-MAX quote drops one list marker («- » before «Proof.»); otherwise verbatim (l-red 47000632 l. 41-46) |
| 2 | T54 IDX-MONO / LEX-BFS as used in §5 Case 2a | SIGNED as used (one S4a evaluation, W_(k+1)-tight, keys on (σ_(k+1), τ)-paths) | checked against si.py's longest-path recursion and BFS, with RG′ |
| 3 | Claim RG′ | SIGNED | none |
| 4 | Lemma PLAY-CAUSE; W-MON; PATH | SIGNED | none |
| 5 | Theorem RUN-SETTLE (S_j, X_j; Cases 1, 2a, 2b, 2c); Corollary RUN-COUNT | SIGNED | none |
| 6 | Theorem HEAD-RED | SIGNED | none |
| 7 | Corollary T-XCH | SIGNED | none |
| 8-9 | CONJECTURES, DATA, DEAD, READING | not signed | DATA reproduced with my own engine (§4) |
| line | 6aa094e3 | content MATCHES §3, §5-§7 | REQUIRED: L-1 F unquantified; L-2 Iσ_k unbound; L-3 T unbound. Precision L-4..L-6 |

No gap in the packet. Nothing FALSE among the items to sign.

## 2. The items, as I checked them
### 2.1 Setting and quotes
- STEP-SW inside a W-run (τ fixed, no S4c): S4a changed σ (R15 (d)). ✓ MON from R15 (a), (d). ✓
- N-1. «On values with one cycle node c, y ⊕ · preserves and reflects ⊴ and ◁» fails if y lies in the path set of exactly one argument:
  x = (c, {w}, ℓ), x′ = (c, {y}, ℓ) with y, w even, y above w above c: x ◁ x′, but y ⊕ x = (c, {w, y}, ℓ + 1) ▷ y ⊕ x′ = (c, {y}, ℓ + 1).
  So even the non-strict monotonicity can flip. Every use in §5 applies it to values of plays that avoid y: Case 2 (W_k(a), W_k(b): a =
  σ_k(y), b's path avoids y), Case 2b (W_k(a), W_(k+1)(a): both paths avoid y), Case 2c (the disjointness is argued explicitly). Fix:
  «on values with one cycle node c whose path sets do not contain y». No signed item changes.
### 2.2 Claim RG′ (§3), against si.py Engine.evaluate l. 112-149
- The engine runs on the dual of H_k with dual-Even fixed to τ, so its «Odd» is original Even. par in the dual is Ω + 1, so the code's
  «par 0» branch (Even likes u, in the engine) is original-bad u. I re-derived the invariant per processed u:
  - bad u: M = reach(c avoiding u); bits go to q ∉ M; u's and M's edges are restricted to M. A remaining edge x → y with x ∉ M ∪ {u} and
    y ∈ M would put x in M, so remaining edges cross M only out of u. u ∉ M carries bit u, and its remaining successors lie in M.
  - good u: M = reach(u avoiding c); bits go to q ∈ M; the edges of M ∖ {u} are restricted to M. An edge x → y with x ∉ M, x ≠ c,
    y ∈ M would put x in M. u ∈ M carries bit u.
  - Later deletions only remove edges. So on every remaining edge x → y with x ≠ c, path[x] = path[y] ∪ ({x} if rank(x) > rank(c)).
    (If x ∈ path[y], the edge cannot have dist(y) = dist(x) − 1, since y's path would pass x; the claim restricts to those edges.)
- (B) tight edges survive: the three deleted-edge cases are non-tight (bit u on one end only; or, for bad u's own edge into y ∉ M, every
  path from y to c passes u, so ℓ(y) > ℓ(u)). ✓ With R57 the computed (c, path, dist) is W_(k+1). ✓
- «No step of the proof uses W_(k+1) = W_k»: confirmed.
### 2.3 IDX-MONO, LEX-BFS as used (§2, §5 Case 2a)
- Ω(c) odd → dual-even cycle → the engine's longest-path recursion over hs[x] in increasing index; «if d > best» keeps the first maximum.
  The successors of maximal dist are those with dist(y) = dist(x) − 1, which by RG′ are exactly the W_(k+1)-tight arena edges. So the
  choice is the smallest-index tight edge of H_k(y). ✓
- Ω(c) even → dual-odd cycle → BFS from c over the restricted predecessor lists, which are in increasing index (gp is built in index order;
  restrict() only removes entries). Layer j + 1 is scanned from layer j in queue order, so queue order is lexicographic in (key(parent),
  own index), which is the key read on the BFS tree, i.e. on (σ_(k+1), τ)-paths. A vertex is discovered from its first queued successor
  of dist one less, i.e. (RG′) its lex-least tight successor. ✓ Keys of distinct vertices differ in the last coordinate. ✓
- Both are statements about one S4a evaluation at an arbitrary transition of a W-run, with tightness read at W_(k+1). That is how §5 uses
  them. SIGNED as used. Mechanically: every S4a step of the corpus, every Even y ∉ C (§4, IDX / LEX).
### 2.4 PLAY-CAUSE, W-MON, PATH (§4)
- PLAY-CAUSE. i (the first index in D_(k+1) ∪ C) exists, since before D the play is the W-play, whose first C-vertex is λ_W(x) (a C-vertex
  on the W-path is its own cycle node, so the W-play ends in its cycle). Ξ_(k+1)(x) = (w, rel(y_0 … y_i) above w ∪ P(Ξ(y_(i+1))), i + 1 +
  ℓ(Ξ(y_(i+1)))) when w ∉ {y_0 … y_i}, and (y_j, rel(y_0 … y_(j−1)), j) otherwise, with w the cycle node of Ξ(y_(i+1)). So it is a function of
  y_0 … y_i and Ξ_(k+1)(y_(i+1)), even when y_(i+1)'s play re-enters y_0 … y_i (path sets are sets). With no switch among the Even y_t
  (t ≤ i), no event (i) (σ̄ and D unchanged) and no event (iii) at y_(i+1) ∈ U_(k+1), the (σ_k, σ̄_k)-play has the same prefix, the same
  index i and the same Ξ(y_(i+1)). So Ξ_k(x) = Ξ_(k+1)(x). The switching y_t has t < i (y_i is Odd in D, or in C and not switching), so
  y_t ∉ C and lies on the W-path before λ_W(x). ✓
- W-MON (ARENA-MAX with ρ = σ_k ∈ H_k; τ_k = τ_(k+1)). ✓ PATH. ✓
### 2.5 RUN-SETTLE, RUN-COUNT (§5)
- j = 0: no CN switch, so ℓ ≥ 1. ✓ S_j ⇒ X_j by PLAY-CAUSE (ℓ(x) = t + ℓ(y_t) ≥ ℓ(y_t)). ✓
- Least violator y, L, a, b, c; ℓ_(k+1)(b) = L − 1 (y ∉ C, the W-path y → b → … → c is simple); (MIN); every vertex of b's path has ℓ ≤ L − 1,
  so PATH gives W_k(b) = W_(k+1)(b), ℓ_k(b) = L − 1 and the same path, which avoids y. ✓
- Case 1: b ∉ H_(k−1)(y). Ξ_k(b) ▷ Ξ_k(a) ⊵ Ξ_(k−1)(a) ⊵ Ξ_(k−1)(σ_(k−1)(y)); if Ξ(b) did not change at k − 1 → k, then (y, b) ∈ Iσ_(k−1)
  (b ≠ σ_(k−1)(y), else b ∈ H_(k−1)(y)), so b ∈ H_(k−1)(y). Hence Ξ(b) changes, X_(j−1) gives ℓ_k(b) ≥ j > L − 1. ✓
- Case 2: ρ = σ_k[y ↦ b] ∈ H_(k−1) (σ_k(v) ∈ H_(k−1)(v) for all v, being S4a's choice there). ARENA-MAX, W-MON, and reflection by y ⊕ ·
  (both paths avoid y) give W_(k+1)(y) = W_k(y) and both a, b W_k-tight. ✓
  - 2a: a W_(k+1)-tight; MIN and PATH keep a's and b's paths, so keys agree under σ_k and σ_(k+1); LEX-BFS (or IDX-MONO) at k − 1 → k and at
    k → k + 1 give opposite strict orders. ✓ (c is the same cycle node at both transitions: λ_W is fixed on F.)
  - 2b: ρ′ = σ_(k+1)[y ↦ a] ∈ H_k; y ⊕ W_(k+1)(a) ⊴ W_(k+1)(y) = y ⊕ W_k(a) ⊴ y ⊕ W_(k+1)(a); so a is tight. ✓ (λ_W(a) = c at both
    states, and both paths avoid y, so N-1's condition holds.)
  - 2c: u exists (else a's σ_(k+1)-path would be its σ_k-path, which avoids y), u ∉ C, u ≠ y; Z = P ∪ Q is a simple cycle avoiding c; W_(k+1)(u)
    = (c, S_k(u) ⊔ R, ℓ_k(u) + |Z|) (P is disjoint from y's σ_(k+1)-path, which carries P(W_k(y)) = rel(Q) ⊔ S_k(u)); W-MON then forces R's top
    even, or R = ∅ with c odd; under ρ′ the play from y closes Z with top z*, reward(z*) > reward(c) in both cases; so val(ρ′, τ)(y) ▷
    W_(k+1)(y), against ARENA-MAX. ✓
  - The four cases exhaust: b ∉ / ∈ H_(k−1)(y); in the second, a tight / not tight, and if not tight, a's σ_(k+1)-path avoids y / contains y. ✓
- The bound and RUN-COUNT: ✓ (event-free transitions form ≤ E_F + 1 blocks of ≤ n − 1).
### 2.6 HEAD-RED (§6), T-XCH (§7)
- HEAD-RED: each event has a kind, and each kind is counted on the right; Σ_o ≤ n·max, Σ_c ≤ n·max, Σ_u ≤ n·max; converse trivial. ✓
- T-XCH: T ≤ Σ_v SW(v) (R15 (d)); R86 (a) on both sides (the landed text has «Dually for Odd v with U.»), R = the whole run;
  Σ_c d_E(c)·RISE(c) ≤ m_E·XE, likewise for Odd. ✓ Converse trivial. A reformulation of G-N5-TIME, as the packet says.

## 3. The proposed line (6aa094e3): strict symbol test, TARGET.md diff
- **L-1 (REQUIRED).** F is defined («W-run F := RESULTS R89's …») but not quantified in the claims: RUN-SETTLE («the transitions k0, …,
  k1 − 1 of F»), RUN-COUNT («|F| ≤ n(E_F + 1) − 1») and HEAD-RED («E_F ≤ …»). This is the WRUN-L3 pattern. Fix: «…: for every N5 run and
  every W-run F of it, (Claim RG′) …».
- **L-2 (REQUIRED).** Iσ_k is used in H_k's definition («{σ_k(v)} ∪ Iσ_k(v)») but not defined in the line. Fix: «Iσ_k := Even's improving
  edges at k (SPEC S2)».
- **L-3 (REQUIRED).** T-XCH: «every run has T ≤ …»: T is unbound. Fix: «every run with T transitions has T ≤ …».
- L-4 (precision). RUN-SETTLE «has ℓ_(k+1) ≥ k − k0 + 1»: give the argument, «ℓ_(k+1)(v) ≥ k − k0 + 1 for that vertex v».
- L-5 (precision). The proof parenthesis cites ARENA-MAX (L-RED R140) and T54's LEX-BFS / IDX-MONO, which are not landed. Say that they are
  used as signed here («LEX-BFS / IDX-MONO as signed in this packet's review, at one S4a evaluation»), or that ARENA-MAX is the S4a half of
  the R57 premise already carried by the line.
- L-6 (precision). The closing clause lacks the usual «not M3, not a step-4 pass, not a TARGET.md claim».
- Bound: τ, C (on F), W_k, ℓ_k, Ξ_k, σ̄_k, D_k, U_k, EVENT, E_F, SB_F, CN_F, HXU_F, H_k, dist and remaining edges (via si.py), n, m_E,
  m_O, U, tightness, XE, XO, k0, k1, k.
- Content: RG′, RUN-SETTLE, RUN-COUNT, HEAD-RED and T-XCH are the packet's statements; PLAY-CAUSE / W-MON / PATH are not stated (allowed). No
  M4 claim. TARGET.md's n.

## 4. DATA: re-run with my own engine
Tool docs/referee-2/R2-N5-SETTLE/settle_check.py (my R2-N5-LATEP state construction; U_k, events, blocks, the case split and the IDX / LEX
choice rule written from the packet text; lane heads52 code NOT imported). Run set: the lane's 1,134 runs (sbcg.lst 719; alt_all 94 with
starts, comp54_n80 repaired, + 319 without; latew_K16_m32 and fx_K8_m32 with starts). Logs in R2-N5-SETTLE/logs/.
- **0 violations** of S, X, BLK, RC, PC, HR, WM, IDX, LEX, TX on every run (and of the premise checks XIPLAY, XW, XIMON).
- IDX-MONO / LEX-BFS with RG′, read at every S4a step of every W-run for every Even y ∉ C: 175,533 IDX and 651,871 LEX checks, 0 failures.
- Case split of switches at j ≥ 1: Case 1 13,998; WR 186; Case 2a 13; Case 2b 0; Case 2c 0. These equal the packet's §9 figures exactly.
- Events: (i) 4,625, (ii) 37, (iii) 4,741 transitions (counted per kind; a transition can carry several). Max E_F 528 (latew_K16_m32).
- N-3 (DATA). Longest event-free block: mine 67 (red/usplit/instances/gate_K64_n581 + start, n 581), 55 (red/xing/instances/x32_rand64,
  n 64), 49 (ladderd0_k48_n156). The packet's §9 says «the longest event-free block is 44 at n 48 (x32_rand48)». All are ≤ n − 1, so
  nothing is contradicted, but the «longest» figure does not match my blocks on the same corpus. Maybe rwin.py measures blocks
  differently, or over a sub-corpus; I did not reconcile it. Not signed material.

## DONE / FINDINGS / NEEDS (this report)
- DONE: this report; settle_check.py; logs.
- FINDINGS: (1) every item to sign SIGNED, no gap, nothing FALSE; T54 IDX-MONO / LEX-BFS SIGNED as used. (2) Line: three REQUIRED binding
  fixes (F unquantified; Iσ_k; T), precision L-4..L-6. (3) N-1: the ⊕-monotonicity sentence in §1 needs «y ∉ P» (instance given); N-2: the
  ARENA-MAX quote drops a list marker.
- NEEDS: Lead: route L-1..L-3 (and N-1, N-2) to L-SI 34 (docs/si/P-N5-SETTLE-fixes.md).
