# N5-ORD (box 97): the Gimbert–Horn / Auger order template (L-LIT T60 §3.3) on N5's W-runs. ORDER-DET holds in a refined form on the FIXED target set A_F (PROVED, lane, given L-SI's SEL), but not in T60's U-form (DEAD, n5s_maxph_0, n = 5). NO-REPEAT is DEAD (thetaA_n7, n = 7; 89 corpus games). With the order set fixed (max |U_k| = 6, |A_F| = 11, 6 distinct orders), σ̄ changes K times in one W-run on gate_K (K = 16, 64). So no bound SB_F ≤ f(max |U_k|) or f(|A_F|) exists, and this template gives no subclass
L-NEW successor 40 (Opus 5.5), D14 / D18, Lead reading L40. Lead 2026-10-30 (brief received after 20:00Z): «BOX 97 … (1) Prove ORDER-DET, or
kill it with an instance … (2) Test NO-REPEAT on the corpus and on the quadratic families (sbq2_K8_m16, latew, obs). Kill it or keep it as a
conjecture. (3) If both hold, state the FPT bound exactly.» Written 2026-10-30 20:05Z-20:1xZ (date -u). Working note, unrefereed. Labels:
PROVED (lane) / CONJECTURE / DEAD / DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN; no W-run count is bounded here.

## 0. Sources and setting
- L-LIT T60 §3.3 (l-lit 54584c0c, docs/lit/T60-best-reply-flips.md; read from origin/claude/l-lit, not on trunk). The two lemmas, as T60 states
  them:
  - «ORDER-DET (OPEN): inside a W-run, between CN switches, σ̄_k is determined by σ_k and the ⊴-ORDER (not the values) of Ξ_k on U_k»;
  - «NO-REPEAT (OPEN): the sequence of head orders visited in F never repeats a (σ-pattern, order) pair».
  - The source template: [ABS] Auger–Badin de Montjoye–Strozecki arXiv 2102.04922, proof of Thm 29 pp.16-17, and [GH] Gimbert–Horn via [ABS]
    §5.1 (an f-strategy is fixed by a total order f of the r random vertices; improving f-strategies never repeat, so there are ≤ r! of them).
    I did NOT open [ABS] or [GH] in this box. Nothing below uses their theorems: §3 only tests whether N5 meets the template's hypotheses.
- L-SI box 53 (l-si aeb8c311, docs/si/N5-SBF-box53.md; not on trunk). Quoted and used:
  - NON-OWN (o is non-own at k iff the cycle node of Ξ_k(o) is not o);
  - Lemma SEL §2.1 (σ̄_k(o) ∈ T_k(o); least index if the cycle node c is even, least key_k if c is odd). L-SI marks SEL «PROVED modulo the
    reading» that Claim RG′ and T54's LEX-BFS / IDX-MONO apply to S1's evaluation. Everything below that uses SEL inherits that reading.
  - Lemma NOCLOSE §2.2: if o is non-own at k, t* := σ̄_k(o), and o ∈ path_k(y) for a successor y, then Ξ_k(y) ▷ Ξ_k(t*);
  - the fact (⊕) of §2 («y ⊕ · preserves and reflects ⊴ and ◁ and is injective» off the paths, for any cycle nodes).
- P-N5-SETTLE §1 (l-si 6a70a520). Notation: Ξ_k, σ̄_k, ⊴, ◁, W-run (RESULTS R89 verbatim), C, D_k, [R57], [R15] (a).
- L-RED R143's heads, verbatim as quoted there: «U_k := {σ̄_k(g) : g Odd, σ̄_k(g) ≠ τ(g)} ∪ {the Ξ-successor of c (σ_k(c), or σ̄_k(c) if c is
  Odd) : c ∈ C}».
- Tool: experiments/new/box97/orderdet.py (W-run segmentation as box92/xirun.py). Corpus driver: box97/runod.sh, which runs box 50b's corpus
  (new/box59/sbcg.lst + si/root/logs/alt_all.lst, as L-SI box 53) and the three quadratic pins. Outputs: box97/od_sbcg.txt, od_alt.txt,
  od_pins.txt. Pins: new/check.sh «box 97 ORD».
- Quadratic pins, copied read-only from origin/claude/l-red into experiments/new/box97/inst/ (sha1 .pg / .start):
  - sbq2_K8_m16: 70f485cd / 98b0927a (R145);
  - obs_K12_m24: 7df541fb / 23db47dd;
  - latew_K16_m32: 6d34c161 / 0c847d29.

## 1. Definitions (this box)
- Fix a W-run F with frozen τ, states a..b.
  - O_F := the Odd vertices whose σ̄ changes somewhere in F.
  - U_F := ∪_{k∈F} U_k.
  - A_F := U_F ∪ τ(O_F), a vertex set FIXED on F.
  - U′_k := U_k ∪ τ(Odd), L-SI box 53's U′.
- Refined key, for a vertex t at state k. Let x := Ξ_k(t) with cycle node c. Then
  r_k(t) := (Ξ_k(t) in the order ⊴, tb_k(t)), where tb_k(t) := index(t) if c is even, and tb_k(t) := key_k(t) (L-SI's T54 key: the
  (σ_k, σ̄_k)-path of t to c, read from c's end) if c is odd.
  - Compare lexicographically, smaller = preferred by Odd.
  - Equal Ξ-values have the same cycle node, so tied entries always compare by the same kind of tb. Two distinct vertices with one value
    have distinct tb, so ≺_k (r_k-order) is a strict total order on any vertex set.
- «The refined order of X at k» := the list of X sorted by r_k. «The ⊴-preorder of X at k» := the dense ranks of Ξ_k on X.

## 2. ORDER-DET
### 2.1 Literal form: TRUE but empty
- σ̄_k is SPEC S1's deterministic output on σ_k (σ̄_k := S1(σ_k), P-N5-SETTLE §1). So «σ̄_k is a function of σ_k and of anything else» holds
  trivially.
- It gives no count. Inside a W-run every transition switches σ (P-N5-SETTLE §1), so consecutive states never share σ. A count by
  «distinct (σ, order) pairs» is therefore at least the number of distinct σ's visited, and bounds nothing beyond |F|.
- The [GH] template needs the reply to be a function of the ORDER ALONE (plus data fixed on F). §2.2-§2.3 test exactly that.

### 2.2 T60's U-form is DEAD (instance n5s_maxph_0, n = 5)
- Claim tested (ORDER-DET-U): inside a W-run, if two states k, k′ have U_k = U_k′ and the same ⊴-preorder of Ξ on U_k, then σ̄_k = σ̄_k′
  at the Odd vertices non-own at both.
- Instance: experiments/n5-exhaustive/instances/n5s_maxph_0.pg (L-COMP's exhaustive family, read only; sha1 04a10d8a).
  - Vertices (priority, owner, successors): 0 (0, Odd, {1, 2}); 1 (2, Even, {2, 3}); 2 (4, Even, {3}); 3 (6, Even, {4}); 4 (7, Even,
    {0, 2}).
  - Default start: σ = (1↦3, 2↦3, 3↦4, 4↦2), τ(0) = 1.
- Run (orderdet.py VERBOSE=1; states printed with box21/n5x.py):
  - States 0-1 form ONE W-run: τ(0) = 1, no fallback, λ_W fixed, C = {4}, Ξ-successor of 4 = σ(4) = 2.
  - State 0: σ̄(0) = 1 = τ(0), so D_0 = ∅ and U_0 = {2}.
    - Ξ_0(1) = Ξ_0(2) = (4, ∅, 2). The cycle node 4 is odd, so the tie is broken by key: key(1) = (3, 1) < key(2) = (3, 2).
  - Transition 0 → 1: σ(1) switches 3 → 2, so Ξ(1) = (4, ∅, 3). A longer path is better for Even when the cycle node is odd, so Odd now
    prefers 2.
  - State 1: σ̄(0) = 2 ≠ τ(0), so U_1 = {2} again.
  - So U_0 = U_1 = {2}, the order on a singleton is the same, and σ̄(0) changes 1 → 2.
- Exact obstruction: the old target 1 = τ(0) is NOT a head. U_k sees σ̄(o) only for o ∈ D_k. A flip OUT of τ(o) is caused by a rise of
  Ξ(τ(o)), which U_k does not record. This is L-SI box 53's flipev_n20 phenomenon (ROOT-FLIP's o* ∉ D_k case) at n = 5.
- DATA (corpus, §4): ODU conflicts in 20 games (284 conflicting state pairs).
- DEAD: ORDER-DET-U (order of Ξ on U_k alone). The repair must add τ(Odd): §2.3.

### 2.3 Lemma ORDER-DET-R (PROVED, lane; premises SEL, NOCLOSE, [R57], (⊕))
- Statement. Let k be any state of an N5 run (τ := τ_k), o an Odd vertex non-own at k, and X ⊆ V a vertex set with σ̄_k(o) ∈ X. Then
  σ̄_k(o) = the ≺_k-least element of succ(o) ∩ X.
  - In particular this holds:
    - (U′) with X = U′_k, at every state. Every σ̄_k(o) lies in U′_k: σ̄_k(o) ∈ U_k if o ∈ D_k, and σ̄_k(o) = τ(o) otherwise.
    - (A) with X = A_F, for o ∈ O_F at every state k of a W-run F. Here σ̄_k(o) ∈ U_k ⊆ U_F, or σ̄_k(o) = τ(o) ∈ τ(O_F).
- Proof. Let t* := σ̄_k(o) and y ∈ succ(o) ∩ X, y ≠ t*. We show t* ≺_k y.
  - Case o ∈ path_k(y). NOCLOSE gives Ξ_k(y) ▷ Ξ_k(t*). Odd prefers smaller values, so t* ≺_k y.
  - Case o ∉ path_k(y).
    - Let ρ := σ̄_k with o ↦ y. The (σ_k, ρ)-play from y is y's (σ_k, σ̄_k)-play, since it avoids o. So val(σ_k, ρ)(o) = o ⊕ Ξ_k(y).
    - o is non-own, so path_k(t*) avoids o and Ξ_k(o) = o ⊕ Ξ_k(t*) (L-SI box 53 §2, second fact).
    - [R57] (S1 realises Odd's pointwise optimum) gives Ξ_k(o) ⊴ val(σ_k, ρ)(o), i.e. o ⊕ Ξ_k(t*) ⊴ o ⊕ Ξ_k(y).
    - Neither path contains o, and o is not a cycle node of either value. So (⊕) reflects ⊴: Ξ_k(t*) ⊴ Ξ_k(y).
    - If the inequality is strict, then t* ≺_k y.
    - If Ξ_k(t*) = Ξ_k(y), then o ⊕ Ξ_k(y) = Ξ_k(o), so y ∈ T_k(o). Both values have the cycle node c of Ξ_k(o).
      - SEL-E (c even): t* is the least-index element of T_k(o), so index(t*) < index(y).
      - SEL-O (c odd): t* is the key-least element of T_k(o), so key_k(t*) < key_k(y).
      - Either way tb_k(t*) < tb_k(y), so t* ≺_k y. □
- Corollary ORDER-DET-A (the [GH]-type form). On a W-run F, the restriction of σ̄_k to the vertices non-own at k is a function of:
  - the refined order of A_F at k;
  - the set of vertices non-own at k;
  - data fixed on F: succ, and σ̄ on Odd ∖ O_F, which is constant on F.
  - Proof: §2.3 (A), together with: σ̄(o) is constant on F for o ∉ O_F. □
- Corollary ORDER-DET-U′ (per state, with L-SI's U′). σ̄_k(o) = min_{≺_k}(succ(o) ∩ U′_k) for every non-own o.
  - So σ̄_k on the non-own vertices is a function of (U′_k, refined order of U′_k, non-own set).
- Corollary FLIP-ORD (PROVED, lane). Let SBT_F := the transitions of F at which σ̄ changes, and ORDCH_F := the transitions of F at which the
  refined order of A_F changes. Then SBT_F ≤ ORDCH_F + XCN_F, with XCN_F as in L-SI box 53 §3 (a flip at an Odd vertex that is its own
  cycle node at k or at k + 1).
  - Proof. Take a transition with a flip at some o non-own at k and at k + 1. Then o ∈ O_F, and (A) at k and at k + 1 gives two different
    ≺-minima of the same set succ(o) ∩ A_F. So the refined orders differ. □
  - Also ORDCH_F ≤ Σ_{u ∈ A_F} RCH_F(u), where RCH_F(u) := the transitions at which r(u) changes: Ξ(u) changes, or u's key changes at a
    fixed odd-cycle-node value. This is a weak cousin of L-SI's HEAD-RED′; A_F is a static superset. It is recorded only because §3 needs
    it.
- What ORDER-DET-R is NOT:
  - The unrefined ⊴-preorder may not suffice. Ties at an odd cycle node are broken by key_k, which is not a function of the values. On the
    corpus the unrefined A-form had 0 conflicts (ODA 0), so this case never decided an outcome there. No instance and no proof: OPEN, not
    needed.
  - The parameter is |A_F| ≥ |τ(O_F)|, not max |U_k| as T60 proposed (§2.2 shows why).
- DATA: REFMINX 0 and REFMINUX 0 (the (A) and (U′) formulas checked at every state of every W-run); ODR 0. Corpus: §4.

## 3. NO-REPEAT is DEAD, and so is every bound SB_F ≤ f(order-set size)
### 3.1 Kill at n = 7 (thetaA_n7)
- Instance: experiments/n5-exhaustive/instances/thetaA_n7.pg + .start (sha1 cd2a3bc8 / 11851dd1; L-SI box 53's §1 instance). The whole run
  (states 0-3) is one W-run, τ(6) = 5, C = {2}.
- U_0 = U_1 = U_3 = {2} and U_2 = {1, 2}. O_F = {6}, so A_F = {1, 2, 5}.
- σ̄(6) runs 5, 5, 1, 5:
  - transition 1 → 2: Ξ(5) rises (σ(5): 4 → 0), so 1 ≺ 5;
  - transition 2 → 3: Ξ(1) rises (σ(1): 3 → 6), so 5 ≺ 1 again.
- The refined order of A_F (and the ⊴-preorder, and the U-form order) at state 3 equals the one at state 0. In between there is a σ̄-change.
  orderdet.py: NRU 1, NRA 1, NRR 1, NRRS 1.
- DEAD: NO-REPEAT in each of its forms (U-form, ⊴-preorder on A_F, refined order on A_F).
- Why: the [GH] argument is «order ⇒ strategy ⇒ values; values strictly improve; so an order cannot recur». In N5 the order fixes only σ̄
  (§2.3). Ξ_k = val(σ_k, σ̄_k) also depends on σ_k, which keeps improving. So a recurring order is no contradiction: the two successors'
  values leapfrog (L-LIT T60 §4.2 PAIR-CROSS; L-SI box 53 §1 «the monotone object is the VALUE vector Ξ, not the selection»).

### 3.2 Fixed order set, linear σ̄-changes (gate_K, pp_K; L-RED's usplit families, read only)
| instance (sha1 .pg / .start) | n | |F| | max_k |U_k| | |A_F| | |O_F| | SBT_F | ORDCH_F | distinct refined orders |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gate_K16_n197 (3eeddc86 / 0fd36d6a) | 197 | 23 | 6 | 11 | 5 | 16 | 16 | 6 |
| gate_K64_n581 (a93c7c8b / 9eb6df2f) | 581 | 71 | 6 | 11 | 5 | 64 | 64 | 6 |
| pp_K12_n161 (8808ba5d / eb95d52b) | 161 | 19 | 7 | 15 | 6 | 14 | 14 | 6 |
| pp_K48_n449 (a161569d / ead17654) | 449 | 55 | 7 | 15 | 6 | 50 | 50 | 6 |
- Each row is one W-run of the run from the .start (PERRUN=1).
- On gate_K the parameter stays fixed (max |U_k| = 6, |A_F| = 11), the order cycles through 6 orders, and SBT_F = K.
- DEAD: any bound SBT_F ≤ f(max_k |U_k|) or SBT_F ≤ f(|A_F|) with f independent of n. In particular the [GH] count «≤ r!» (r := |A_F| or
  max |U_k|) fails for the family: no single instance violates r! (64 < 11!), but gate_K16 → gate_K64 multiplies SBT by 4 at fixed r, so
  no function of r alone bounds SBT on gate_K.
- Not killed: an FPT bound f(r)·poly(n). These rows are linear in K. But such a bound would not come from the order template. It would need
  a bound on how often orders RECUR, i.e. on leapfrogging, which is XI-CH-POLY / HX′-POLY again (FLIP-ORD: ORDCH_F ≤ Σ_{u∈A_F} RCH_F(u)).

### 3.3 Quadratic families (the brief's (2))
| pin | n | |F| | max |U_k| | |A_F| | SBT_F | distinct refined orders | NO-REPEAT |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sbq2_K8_m16 | 261 | 152 | 50 | 113 | 144 | 145 | holds (no recurrence) |
| obs_K12_m24 | 272 | 324 | 49 | 97 | 1 | 25 | holds |
| latew_K16_m32 | 482 | 560 | 96 | 191 | 513 | 529 | holds |
- On the three quadratic pins the refined order never recurs. But the order set grows with n: max |U_k| ≈ n/5, |A_F| ≈ 0.4n. So even
  there the template gives only |A_F|!, which is useless.
- READING: the families that make σ̄ flip often do it in one of two ways:
  - by a SMALL order set that cycles (gate, pp, fcobs: NO-REPEAT fails);
  - by a LARGE head set that never recurs (sbq2, latew).
  The template needs both a small set and no recurrence, and no family seen has both while σ̄ flips often.

## 4. DATA (corpus; runod.sh, runs 2026-10-30 20:05Z-20:1xZ, date -u; the second run added REFMINUX)
- Scope: 1,132 corpus runs (719 sbcg + 413 alt) + 3 pins = 1,135 runs. Every run finished within the 300 s cap (0 unparsed lines).
  - 1,695 W-runs over 646 runs with a W-run.
- Exact claims, 0 violations:
  - REFMINX 0 and REFMINUX 0 (Lemma ORDER-DET-R in forms (A) and (U′), at every state of every W-run);
  - ODR 0 (the refined A_F-order determines σ̄ on the non-own vertices).
- Kills:
  - ODU: conflicts in 20 runs (284 state pairs). Smallest: n5s_maxph_0, n = 5.
  - NO-REPEAT, refined order on A_F, with a σ̄-change between the recurrences (NRRS): 89 runs, 132 W-runs. Smallest: thetaA_n7.
  - Other forms: NRU 150 runs, NRA 91, NRR 93.
- ODA 0: the unrefined ⊴-preorder on A_F never conflicted (§2.3, «What ORDER-DET-R is NOT»).
- Largest SBT_F at small |A_F|: gate_K64 (64 at |A_F| = 11), pp_K48 (50 at 15), fcobs_6 (43 at 15). Largest |U_k|: sbq2_K8_m16 (50).

## 5. The brief's (3): the FPT bound
- Both lemmas do not hold. ORDER-DET holds only in the refined A_F / U′ form (§2.3). NO-REPEAT is DEAD (§3.1). The order-set parameter does not
  bound σ̄-changes (§3.2). So there is no FPT statement to land.
- For the record, the exact conditional statement (PROVED, lane, and VACUOUS on the corpus): if on a W-run F the refined order of A_F never
  recurs, then SBT_F ≤ XCN_F + ORDCH_F ≤ XCN_F + |A_F|! − 1. Proof: FLIP-ORD and the pigeonhole principle.
- Even then it would bound only the SB term. By L-SI's HEAD-RED′ (box 53 §3) the SB term is already gone from the W-run count. The residual
  there is CN_F + XCN_F + Σ HXU′_F, i.e. Ξ-CHANGES (not order changes) at the heads.
  - An order template counts order changes, not value changes. So even both lemmas would give no W-run bound and no subclass result. A
    subclass would need max |U_k| = O(log n) AND a bound on Ξ-changes at the heads.
- READING (D18, no source opened): this is the gap between kinetic sorting and the [GH] setting. In kinetic data structures the number of swaps
  among r monotone trajectories is bounded only through an algebraic bound on pairwise crossings (bounded-degree motion). Arbitrary monotone
  trajectories can swap any number of times (here: gate_K's pair swaps K times). [GH] avoids this because the order fixes the values. N5 lacks
  that, because σ keeps moving underneath. A usable bridge would need a «bounded-degree motion» property of Ξ on the heads per W-run, i.e. a
  pairwise-crossing bound. That is PAIR-CROSS / HX′-POLY again, OPEN.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box97/ (orderdet.py, runod.sh, od_sbcg.txt, od_alt.txt, od_pins.txt, inst/ with three L-RED pins);
  new/check.sh «box 97 ORD». SHA: see the commit.
- FINDINGS:
  - ORDER-DET, literal: true but empty (σ̄_k = S1(σ_k)).
  - ORDER-DET, U-form: DEAD, n5s_maxph_0 (n = 5): the flip out of τ(o) is invisible on U_k.
  - Lemma ORDER-DET-R: PROVED (lane, given SEL). σ̄_k(o) = the ≺_k-least of succ(o) ∩ X for any X ∋ σ̄_k(o), e.g. X = A_F or U′_k.
    Corollary FLIP-ORD: SBT_F ≤ ORDCH_F + XCN_F.
  - NO-REPEAT: DEAD, thetaA_n7 (n = 7; 89 corpus runs). On sbq2, obs and latew it holds, but there |A_F| ≈ 0.4n.
  - Any bound SB_F ≤ f(max |U_k|) or f(|A_F|): DEAD, gate_K16 → gate_K64 (SBT 16 → 64 at |U| ≤ 6, |A_F| = 11, 6 orders).
  - (3) No FPT bound and no subclass. Even with both lemmas only the SB term would be bounded, and HEAD-RED′ has already removed it.
- NEEDS: none from the owner.
