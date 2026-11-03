# Box 136 N5-SELF: self-feeding is static (z-world), dominated comparisons are static (DOM); every observed stretch is D″-acyclic
L-NEW successor 46, 2026-11-01 18:4x-19:1xZ (date -u). Lead GO 18:37Z (box 136, last before parking). Code: experiments/new/box136/
(dmerge2.py, runcorp.sh, d_corpus.txt). check.sh block «box 136 DMERGE2». Labels: PROVED (lane), CONJECTURE, READING, DATA, DEAD,
OPEN. Premises and notation as in docs/new/P-N5-ANCHOR-box134.md §1 with its fixes entry 1 (L46 as amended), and box 135 (MERGE,
CASC-M, stretches).

## 0. Answer
- The Ξ-analogue of C-STATIC holds, in the form the Lead asked for (Lemma C-STATIC-Ξ, PROVED, lane).
  - f_x compares an option y only against x's CURRENT option z, evaluated in the z-WORLD (σ(x) = z): at the present state, and at the
    next state when the idempotence step needs it.
  - If y's Ξ-play reaches x, it continues x → z. So y's value is (private prefix y..x) ⊕ Ξ(z), and the comparison with z is a STATIC
    predicate of the prefix y..x and w: x's own choice is not a dependency.
  - Moving x onto such an option would close a new cycle through x that avoids w, so x's Ξ cycle node would change. That is a stretch
    boundary, counted by CYC-MONO.
  - So SELF-edges are cut.
- odxi_many_n32's D′-cycles were NOT self-loops: they are 2-cycles 13 ↔ 30 and 1 ↔ 30.
  - 13 reads 30 through the ODIFF gate 9 (σ̄(9) = 30), and 30 reads 13 as a W-tight option.
  - They are inert: 13 never moves in that stretch.
  - The reason is DOMINANCE (Lemma DOM, PROVED, lane): the comparison is decided by a vertex in the fixed HEAD of the gate side (the part
    up to the first Even vertex other than x, fixed by σ̄ and x's choice), which is more relevant than anything on the tails.
    Such a comparison adds no dependency.
- With both cuts, the refined digraph D″ is acyclic on EVERY stretch observed:
  - corpus 10 / 10 (29 FL transitions);
  - odxi_many_n32 3 / 3;
  - odxi_min_n12, odxi_lasso_n13, odxi_n37, u23sw64_n32.
  CASC-M with D″ holds with 0 violations.
- Theorem CASC-M″ (PROVED, lane): FL run ≤ n_E · (1 + SBCH + n(n − 1) + CNMOV) for every FL run whose stretches have acyclic D″.
  - The remaining circular items are (1) D″-cycles (none observed anywhere; OPEN) and (2) CNMOV.
  - CNMOV was not reached in this box (§3).
- Construction recipe for L-RED (READING): a D″-cycle needs a mutual dependency through a gate, x reads v and v reads x, whose
  comparison is NOT head-dominated. The decisive (most relevant) vertex of the symmetric difference must lie in a tail, beyond the
  first Even vertex. odxi_many has the mutual dependency, but its comparison is head-dominated.

## 1. PROVED (lane)
- Setting: a stretch of an FL run (σ̄ fixed; the cycle node of Ξ fixed at every vertex; no W-cycle-node move), x an Even vertex ∉ CN,
  T′ := T_x ∪ {σ(x)}. For z ∈ T′, the z-WORLD at state s is σ_s with x's strategy replaced by z, and Odd playing σ̄. Plays, w,
  segments (MERGE) and «before the merge point» are taken in that world.
- Lemma C-STATIC-Ξ.
  - Claim: let y, z ∈ T′ have the same cycle node w in the z-world, and let y's z-world play reach x. Then:
    - the pre-merge segment of y is y..x, and that of z is empty;
    - Ξ_z(y) ▷ Ξ_z(z) iff (w, rel_w(y..x), |y..x|) ▷ (w, ∅, 0).
    The predicate depends on the sequence y..x and on w only.
  - Proof. After x the play follows z, so y's play up to w is y..x · (z's play up to w). MERGE then applies with m = z.
- Lemma DOM.
  - Claim. In a world as above, take the segments Y′, Z′ of a pair (y, z). Let HEAD(P) be the part of P up to and including its first
    Even vertex other than x; it is determined by σ̄ and x's world strategy. Let d be the most relevant vertex above w in
    HEAD(Y′) Δ HEAD(Z′). If d is more relevant than every vertex above w on the two tails, the order of y and z is decided by d's side.
  - Proof: the path sets are compared by the most relevant element of their symmetric difference above w. The heads are fixed; the
    tails contribute only vertices less relevant than d. ∎
- Theorem CASC-M″.
  - Definition: D″ on Even vertices ∉ CN: x → v for every Even v ≠ x on Y′ ∪ Z′ of a pair (y, z) ∈ T′² with equal cycle node in the
    z-world, at some state of the stretch at which the pair is not DOM-decided, plus the W-key edges of box 135.
  - Claim: if D″ is acyclic, the stretch has ≤ height(D″) + 1 transitions.
  - Proof: box 135's induction, with two changes.
    - (i) R(z) := {z} ∪ {y : y ▷ z in the z-world}. After x's D″-successors settle, each comparison used is fixed:
      - DOM-decided: heads are fixed, and the order is d's.
      - Otherwise: the segments consist of settled successors, or the play is DOM-decided before an unsettled vertex is reached.
        After settling, the fixed part of the segment determines which case occurs, so it never alternates.
    - (ii) Idempotence across worlds. Let z′ := f_x(z), so z′ ▷ z in the z-world. z′'s play does not reach x (else a new cycle through
      x, against fixed w). Take y ∈ R(z′).
      - If y's play reaches x: by C-STATIC-Ξ the same static predicate decides it in both worlds, so y ∈ R(z).
      - Otherwise y's and z′'s values do not depend on the world, and transitivity gives y ▷ z.
      Hence R(z′) ⊆ R(z), and z′ is κ-least, so f_x(z′) = z′. ∎
- Corollary: FL run ≤ n_E (1 + SBCH + CYCCH + CNMOV) with CYCCH ≤ n(n − 1), whenever every stretch has acyclic D″.

## 2. DATA (813 distinct pairs, E-1; d_corpus.txt, 0 script errors)
| quantity | corpus | odxi_many_n32 | odxi_n37 | u23sw64_n32 |
| --- | --- | --- | --- | --- |
| stretches / FL transitions | 10 / 29 | 3 / 8 | 1 / 8 | 1 / 8 |
| D″-acyclic / cyclic | 10 / 0 | 3 / 0 (D′: 1 / 2) | 1 / 0 | 1 / 0 |
| CASC-M″ violations / max height / longest stretch | 0 / 18 / 8 | 0 / 8 / 3 | 0 / 9 / 8 | 0 / 9 / 8 |
| DOM-decided comparisons cut | 1,387 | 117 | 630 | 630 |
| x on its own option's segment (excluded by C-STATIC-Ξ) | 21 | 0 under DOM (7 in D′) | 18 | 18 |
| W-cycle-node moves cut out (CNMOV) | 13 | 0 | 0 | 0 |
- DOM here is checked at every observed state of the stretch. The theorem's hypothesis is exactly that per-state condition, so the
  DATA tests the hypothesis; it does not test the lemma.

## 3. Open (for successor 47 / L-RED)
- (1) D″-cycles: none observed. The construction recipe is in §0.
- (2) CNMOV: W-cycle-node moves inside FL runs (corpus 13, cw11_n24 7). FL-ANCHOR (ii) bounds them per epoch (≤ #T_c − 1 after
  settling). Bounding epochs that contain cycle-node moves by CYC-MONO is NOT done.
  - A starting point: a W-cycle-node move changes the W-cycle's edge set but not W, and in cw11 every such move changed Ξ(c) (CMXICH 7 / 7).
  - DEAD route (checked here, scratch script, corpus games with CN moves): «every W-cycle-node move changes the CYCLE NODE of Ξ(c), so
    CYC-MONO bounds CNMOV». The cycle node of Ξ(c) changes at 0 of 11 such moves: cw11_n24 0 / 7 (Ξ(c) itself changes at 7 / 7),
    nep22f_n64 0 / 2 (2 / 2), tog6a_n32 and tog6b_n32 0 / 1 each (Ξ(c) unchanged).
    So CN moves raise Ξ(c) only in the path-set or length component (or not at all).
  - The remaining handle is FL-ANCHOR (ii): a cycle node moves only along strictly Ξ-improving options, in a fixed order, once its
    options' values are fixed. A bound needs the epochs that contain CN moves to be counted, which is the same circular object as GCH
    for the CN term.
