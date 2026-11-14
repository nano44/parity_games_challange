# R184 Retargeted R183 (after L-NEW 46 box 135 CASC-M): no long D′-cyclic stretch and no super-linear CNMOV. Lemma SELF-FREE (PROVED, lane): D′'s self-edges are not needed for CASC-M, but the D′-cycles in the data survive without them (a 2-cycle of two movers). A W-cycle node has no κ rule, but in data each moves once per FL run (erratum: first written «≤ 2») and CNMAX tracks the number of gadgets (L-RED successor 43)
Started 2026-11-01 18:58Z (Lead retarget 18:37Z, read at 18:58Z; date -u). Brief: «(1) Lengthen a D′-cyclic stretch, starting from
odxi_many_n32's self-edge pattern. Score = transitions inside a D′-cyclic stretch, measured against n. (2) Find a family with growing
CNMOV inside FL runs.»
Labels: PROVED (lane), DATA, READING. Premises: the packet P-N5-ANCHOR (f009a9a1) §1-§2 and box 135's Lemma MERGE / Theorem CASC-M
(claude/l-new 2ee388a7, docs/new/N5-MERGE-box135.md). Not a TARGET.md claim. G-N5-TIME stays OPEN. No kill.

## 0. Answer
- (1) Longest D′-cyclic stretch found: 3 transitions, the same as odxi_many_n32's.
  - Climbs: from odxi_many_n32 (n 32) and odxi_many + 16 random vertices (n 48), 6,000 mutations each, score = longest cyclic
    stretch. They raise the self-edge count (7 → 17), not the length.
  - Pin dcyc3_n48.
- (2) CNMOV per FL run grows with the number k of cycle-node gadgets (1 / 2 / 4 / 6 at k = 1 / 2 / 4 / 8). L_FL does not grow (7-8).
  Each gadget's cycle node moves exactly once inside an FL run (erratum: first written «≤ 2»; ≤ 3 over the whole N5 run), so this
  is linear: one move per gadget.
  - Pin cnmov_k8_n57: its FL run of 7 transitions contains 6 CN moves.
- Lemma SELF-FREE (PROVED, lane, §1):
  - At a transition, x's choice reads only the comparisons of its options with its CURRENT option z = σ(x).
  - When an option's Ξ-play passes x, MERGE puts the merge point at z (Z′ = ∅). The comparison then reads only that option's segment
    before x, never σ(x).
  - So D″ is enough for CASC-M: D″ keeps only the pairs (y, σ_s(x)) and drops x from its own segments. D″ has no self-edges.
  - Also: a move of x to an option whose play passes x ends the stretch, since it changes x's cycle node.
- But the D′-cycles in the data are not only self-edges. odxi_many_n32's two cyclic stretches stay cyclic in D″, through 2-cycles of
  movers: 13 ↔ 30 and 1 ↔ 11.
  - 30's option IS the mover 13. 13's option 9 runs 9 → 30 → σ(30).
  - So the remaining mechanism is two movers each sitting on the other's option play: mutual feeding, not self-feeding.
- Cycle-node gadget (READING + DATA, §3). OVT-KEY (R183) does not apply at a W-cycle node c: c has no κ rule. So a cycle node c whose
  two options are gates with τ → c could in principle return to an option it left. ERRATUM (same day, R185 cnidx): in every
  instance measured, no cycle node returns inside one FL run. The gadgets' cycle nodes move exactly once each, upward in index.
  - But such a gate is self-referential: Odd may route it back through c, so Ξ(A) ⊴ A ⊕ c ⊕ Ξ(σ(c)).
  - In the single gadget, the only «improvement» of c that appears runs through c itself (a corner). S4a's cycle-node choice does not
    take it.
  - With k gadgets reading each other and the core, each c moves once per FL run (erratum: first written «at most twice per run»).

## 1. Lemma SELF-FREE (PROVED, lane)
Setting: a stretch of an FL run (box 135: gating states with the same σ̄ and the same cycle node of Ξ at every vertex; no W-cycle-node
move). Even x ∉ CN, a transition j of the stretch (gating state j − 1), z := σ_(j−1)(x).
- (a) σ_j(x) depends on Ξ_(j−1) only through the comparisons Ξ_(j−1)(y) ▷ Ξ_(j−1)(z), y ∈ T_x.
  - S4a's arena keeps R_j(x) = {z} ∪ Iσ_(j−1)(x), and Iσ (S2) compares every option with σ_(j−1)(x).
  - TIE_j(x) is then read off W′ = W, and κ_j off σ_j and τ ([RULE]). Neither reads Ξ.
- (b) Let y ∈ T_x, and let x lie on y's Ξ_(j−1)-play before its first visit of w (the common cycle node). Write P for the part of that
  play before x. Then:
  - y's play to w is P · x · Z_w, where Z_w is z's play to w;
  - the longest common suffix is Z_w, so m = z, Z′ = ∅ and Y′ = P · x;
  - by MERGE, Ξ(y) ▷ Ξ(z) iff (w, rel_w(P ∪ {x}), |P| + 1) ▷ (w, ∅, 0).
  - That reads the vertices of P and x, and the strategies on P only (x's successor is the merge point). Proof: MERGE. ∎
- (c) Consequence for CASC-M. Define D″ ⊆ D′ by x → v for every Even v ≠ x on Y′ ∪ Z′ of a pair (y, σ_s(x)) at some state s of the
  stretch, plus the W-key edges.
  - If D″ is acyclic, CASC-M's induction goes through unchanged with D″. The order f_x uses is built from pairs (y, z) evaluated at
    states where σ(x) = z.
    - By (b) and MERGE persistence, such a pair is fixed once the strategies on its segments other than x are fixed.
    - x's own strategy is z at every state where the pair is used.
  - So CASC-M holds with D″ in place of D′. ∎
- (d) If x moves at j to y whose Ξ_(j−1)-play passes x before w, no Even vertex of P moves at j, and σ̄_j = σ̄_(j−1), then j is the
  last transition of the stretch.
  - Proof: at state j, x's play is x · y · P · x, a cycle avoiding w (w is not on P, and not x). So x's cycle node at j differs from
    w, which a gating state of the stretch cannot show. ∎
- DATA: D″ on odxi_many_n32: self-edges 7 → 0, cyclic stretches 2 → 2. The cycles are 13 ↔ 30 (stretch 6-9) and 1 ↔ 11 (10-13).
  - Detail of 13 ↔ 30:
    - 30 → 13: 30's options include 13, which is itself a mover.
    - 13 → 30: 13's option 9 has the play 9 → 30 → σ(30). At states where σ(30) = 13 that pair is the static case (b), Z′ = ∅.
  - The same 2-cycles appear on the climb outputs (dcyc3_n48: 15 self-edges, still cyclic in D″).

## 2. (1) Lengthening a D′-cyclic stretch (DATA)
- Tools (experiments/red/r184/):
  - dcyc.py: dmerge.py STRETCH=1 as a library. It reproduces box 135's odxi_many row: 3 stretches, 2 cyclic, height 8, longest 3,
    7 self-edges. REFINE=1 gives D″. SHOWCYC=1 prints one cycle.
  - climb184.py: MODE=cyc / cn.

| climb | n | mutations | best longest cyclic stretch | self-edges | L_FL |
| --- | --- | --- | --- | --- | --- |
| odxi_many_n32 (start) | 32 | – | 3 | 7 | 3 |
| from odxi_many_n32 | 32 | 6,000 | 3 | 10 | 3 |
| odxi_many + 16 random | 48 | 6,000 | 3 | 15-17 | 3 |
- READING, why this is hard. A stretch is inside one FL run, so OVT-KEY / KEY-CHARGE (R183) still caps every non-CN mover at
  (|T_x| − 1)(1 + key changes below it).
  - A long stretch therefore needs repeated lower-level moves on W-key paths, i.e. depth. The D″-cycle has to drive a TB ladder,
    which is the same requirement as R177 / R178.

## 3. (2) CNMOV (DATA, READING)
- Climb from cw11_n24 (box 132's CNMOV leader, 7 CN moves in 4 runs of ≤ 3): 6,000 mutations, CNMAX stays 3 (CNMOV 8).
- Cycle-node gadgets (cngad.py / cnclimb.py, 4,000 mutations each):
  - Gadget: on odxi_n37's core, k gadgets. Each is a W-cycle node c (Even, even priority) with options A, B (Odd gates, τ-face → c),
    whose other edges go to core vertices or to other gadgets' c.

| k | n | CNMAX (CN moves in one FL run) | L_FL | moves of each c inside FL runs |
| --- | --- | --- | --- | --- |
| 1 | 36 | 1 | 8 | ≤ 1 |
| 2 | 39 | 2 | 7 | ≤ 1 |
| 4 | 45 | 4 | 7 | 1 each (erratum: «2 and 5, a return» was over the whole N5 run, not one FL run) |
| 8 | 57 | 6 | 7 | 1 each |
- ERRATUM: the line first written here («returns at a cycle node happen inside one FL run») is FALSE on the data. c = 33 moves at 2, 5
  and 10 of the whole N5 run, and 2 and 5 lie in different FL runs. r184/cnidx.py: 0 returns inside FL runs (gadgets, cw11_n24, corpus;
  docs/red/R185-dprime.md §2).
- Self-referential gates (READING, the k = 1 trace):
  - The gate A that should overtake has σ̄(A) = c, so Ξ(A) = A ⊕ c ⊕ Ξ(σ(c)). This is improving only through c itself.
  - For an honest overtake, A's other face must beat B's value while Odd prefers it to returning to c. Then Ξ(A) ⊴ A ⊕ c ⊕ Ξ(B), and
    the margin is c's own path-set bit.
  - This is R167's self-referential gate again, now at a W-cycle node.
- Pins (experiments/red/r184/instances, pins.sha1; default S3 starts written by r183/mkstart.py): cnmov_k8_n57 (CNMAX 6, L_FL 7),
  dcyc3_n48 (cyclic stretch 3, 15 self-edges). Each passes startck, Oink --zlk + verify (OINK OK), --tl verify (exit 0) and xeng.

## 4. Next (Lead decides)
- Proof side (L-NEW):
  - Use D″ instead of D′. Self-edges are gone.
  - The remaining D″-cycles are 2-cycles of movers where one mover's option is the other mover itself. An SCC argument may charge each
    stretch-internal move on such a 2-cycle to OVT-KEY's key changes (W-depth), since both movers are non-CN.
  - For CNMOV: see R185 §2. Inside FL runs, CN moves are UP in index or shortcuts onto the current W-cycle, with 0 returns on the data.
- Attack side: a cycle node with a high out-degree, d gates, each re-overtaken: CNMAX ≤ (d − 1) per epoch, so a run needs many
  epochs. Next build is one cycle node with d gates fed by d independent core regions, measuring CN moves against d and n.
