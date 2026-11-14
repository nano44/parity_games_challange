# Box 135 N5-MERGE: cross-anchor flips are merge-point flips one level down; with an acyclic merge digraph an FL stretch is CASC-short
L-NEW successor 46, 2026-11-01 17:1x-17:4xZ (date -u). Lead GO 17:06Z (box 135, bound FVCH). Code: experiments/new/box135/ (dmerge.py,
runcorp.sh, runstretch.sh, m_corpus.txt, s_corpus.txt). check.sh block «box 135 DMERGE». Labels: PROVED (lane), CONJECTURE, READING,
DATA, DEAD, OPEN. Premises and notation as in the frozen packet docs/new/P-N5-ANCHOR-box134.md §1 ([1E-N3], [RULE] per L46, bridge B,
(R1)). The packet is not changed.

## 0. Answer
- (b) YES. COMPARE-W one level up holds. Two options y, z of one vertex whose Ξ-plays share the cycle node w compare through the parts
  of their plays BEFORE THEIR MERGE POINT m (the start of the longest common suffix of the two plays up to w), plus w. Nothing after m
  matters (Lemma MERGE).
  - A cross-anchor comparison is therefore a same-merge-point comparison further down.
  - So is the «cycle node on a prefix» case (c): there m is the cycle entry of the play that enters first.
- (a) Charging every cross flip to a cycle-node change is impossible. odxi_n37's cross flip has the same cycle node (20) before and
  after. It charges instead to a MOVE on a pre-merge segment: vertex 2 on gate 33's side.
- This gives a cleaner reduction than FVCH. Let D′ be the MERGE DIGRAPH: x → every Even vertex on a pre-merge segment of a pair of
  x's options, plus x → the Even vertices on its options' W-key paths.
  - Theorem CASC-M (PROVED, lane): on a STRETCH (σ̄ fixed, the cycle node of Ξ fixed at every vertex, no move of a W-cycle node), if D′
    is acyclic then the stretch has ≤ height(D′) + 1 ≤ n_E transitions.
  - Since cycle-node changes are ≤ n − 1 per vertex per run (CYC-MONO):
    FL run ≤ n_E · (1 + SBCH + n(n − 1) + CNMOV), provided every stretch has acyclic D′.
  - The circular part is now exactly: (1) D′-cycles inside a stretch, and (2) the W-cycle-node moves CNMOV.
- DATA (813 distinct pairs, E-1):
  - Stretch level: 10 stretches, 29 FL transitions, ALL with acyclic D′, CASC-M holds (0 violations). Max height 18, longest stretch 8.
    The other 13 FL transitions of the corpus are exactly the cut-out W-cycle-node moves (CNMOV 13; cw11_n24 7, nep22f_n64 2 + 2,
    tog6a/b 1 + 1).
  - Run level (no cuts): D′ acyclic in 19 of 20 runs. The exception is nep22f_n64's cycle-node corner run, once per copy.
- The only D′-cycles seen anywhere are in L-RED R179's odxi_many_n32 (a real N5 run): 2 of its 3 stretches, through 7 SELF-edges. A
  vertex x lies on the Ξ-play of one of its own W-tied options BEFORE the merge point, i.e. the gate's Ξ-side leads back through x.
  - That is the exact remaining mechanism, and the construction recipe for L-RED: self-feeding through a gate. x's own choice changes
    the value of one of its options, and an FL run long beyond n_E · (1 + n²) needs such D′-cycles repeatedly (READING).
  - odxi_many's FL runs stay short (≤ 3).

## 1. PROVED (lane)
- Lemma MERGE.
  - Setup: at a state s, take options y, z whose Ξ_s-plays Y, Z (σ_s at Even, σ̄_s at Odd) have the same cycle node w. Let Y_w, Z_w be
    the plays up to the first visit of w (simple paths), m the first vertex of their longest common suffix, and Y′, Z′ the parts
    before m.
  - Claim: Ξ_s(y) ▷ Ξ_s(z) iff (w, rel_w(Y′), |Y′|) ▷ (w, rel_w(Z′), |Z′|).
  - Proof. Ξ_s(y) = (w, rel_w(Y_w minus w), |Y_w| − 1), and Y_w = Y′ · (m … w), where m … w is common to both and disjoint from Y′ and
    Z′ (simple paths). The common part adds the same set and length to both. Path sets compare by the most relevant element of the
    symmetric difference, and lengths by their difference. ∎
  - Persistence. Fix w. Suppose that between states s and s′ no Even vertex of Y′ ∪ Z′ changes strategy, and σ̄ does not change.
    - Then the plays from y and z still run through Y′ and Z′ to m.
    - From m both follow one common (possibly new) path. That path cannot re-enter Y′ or Z′ before w: otherwise the plays would close
      a cycle avoiding w, against the fixed cycle node.
    - So the formula, and hence the order, is the same at s′.
  - Corollary: under fixed w and σ̄, an order flip between y and z needs a strategy change on Y′ ∪ Z′.
- Theorem CASC-M.
  - Setup: on a stretch of an FL run (a maximal set of consecutive transitions whose gating states have the same σ̄ and the same cycle
    node of Ξ at every vertex, and at which no W-cycle node moves), define D′ on Even vertices ∉ CN. x → v for:
    - every Even v on Y′ ∪ Z′ of a pair of x's options in T_x ∪ {σ(x)} with equal cycle node, at some state of the stretch (v = x
      allowed);
    - every Even v on the W-play of an option of x before its cycle node.
  - Claim: if D′ is acyclic, a vertex of D′-height h does not move after the stretch's (h + 1)-th transition. So the stretch has at
    most height(D′) + 1 transitions.
  - Proof: induction on h, as R24 (c) CASC / R177 CASC-G, with MERGE replacing the per-vertex value argument.
    - Once all D′-successors of x are fixed (from step S_(h−1)), MERGE fixes the order on T_x ∪ {σ(x)} restricted to equal cycle
      nodes. Pairs with different cycle nodes compare by the (fixed) cycle nodes.
    - The κ-keys are fixed by the W-key edges.
    - So σ_j(x) = f_x(σ_(j−1)(x)) with a fixed f_x, idempotent as in the packet's §4. x moves at most once, at step S_(h−1) + 1.
    - Base h = 0: no Even vertex on any pre-merge segment or key path, so the order and the keys are fixed from the start. ∎
- Corollary. FL run ≤ n_E · (1 + SBCH + CYCCH + CNMOV), with CYCCH ≤ n(n − 1) by CYC-MONO, for every FL run all of whose stretches
  have acyclic D′.

## 2. DATA
| quantity | corpus (813 distinct pairs) | odxi_many_n32 (R179) | odxi_n37 | u23sw64_n32 |
| --- | --- | --- | --- | --- |
| stretches / FL transitions in them | 10 / 29 | 3 / 8 | 1 / 8 | 1 / 8 |
| D′ acyclic / cyclic stretches | 10 / 0 | 1 / 2 | 1 / 0 | 1 / 0 |
| CASC-M violations / max height / longest stretch | 0 / 18 / 8 | 0 / 8 / 3 | 0 / 9 / 8 | 0 / 9 / 8 |
| self-edges (x on own option's pre-merge segment) | 0 | 7 | 0 | 0 |
| W-cycle-node moves cut out (CNMOV) | 13 | 0 | 0 | 0 |
- Run-level D′ (no cuts; m_corpus.txt): 19 / 20 acyclic, the exception nep22f_n64 (one CN-move run per copy).
- Pins: as in boxes 132-134 (pincheck.txt files). Oink --zlk / --tl verified, n5b identical.

## 3. Open, and next (Lead decides)
- (1) D′-cycles (self-feeding through a gate) inside a stretch. odxi_many_n32 has them, with short runs. L-RED: make a stretch with a
  D′-cycle long, i.e. a vertex whose own choice repeatedly re-releases its sibling through a gate.
- (2) CNMOV: moves of W-cycle nodes inside FL runs. These are bounded per epoch by FL-ANCHOR (ii) (≤ #T_c − 1 after settling), but not
  per run. Corpus: 13, at most 7 per game (cw11_n24, in 4 runs of ≤ 3).
- Proof side: a CYCLIC D′ argument would need an SCC-level potential, i.e. what R177's UP lemma does for D, now on the smaller D′.
