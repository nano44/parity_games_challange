# P-N5-LP fixes (box 32): the referees' repairs, written out
L-NEW successor 12 (Opus 5.5, D15/D18). Lead relay 01:10Z (read 01:12Z). Written 2026-10-25 by date -u.
- Object: packet docs/new/P-N5-LP-box32.md, pinned at trunk bc42f2c, sha1 d2c8121a0089add13c9417080cfb57620f592c88 (re-checked at this
  commit: the file is unchanged). The packet is NOT edited; this file is its correction layer. P-N5-SO (pinned 1ef02bb) is not affected:
  it uses neither DF nor WAKE.
- Sources: REFEREE docs/referee/R-N5-LP.md (claude/referee 4957b2c); REFEREE-2 docs/referee-2/R2-N5-LP.md (claude/referee-2 4949d6c).
  Both on trunk. §C of either report: not yet received; items from it will go in a new section of this file's successor, not here.
- Rule: this file writes down the referees' repairs. A line of my own is marked "L-NEW".

## 0. Verdicts (both reports)
| statement | REFEREE | REFEREE-2 | repair |
| --- | --- | --- | --- |
| Lemma U, UL, GR, NU | SIGNED | SIGN | — |
| Lemma HI | SIGNED; Consequence SIGNED WITH GAP HI-1 | SIGN; Consequence G-LP-2 (unproved as written) | §3 |
| Theorem LP | SIGNED | SIGN; N-LP-1 (wording) | §4 |
| Lemma DF | NOT SIGNED: FALSE as stated | NOT SIGNED: FALSE as stated | §1: DF FALSE, replaced by DF′ (signed by both) |
| Lemma BAND | SIGNED | SIGN | — |
| Lemma WAKE | SIGNED WITH GAP W-1 (closed) | SIGN WITH GAPS G-LP-1 (closed) | §2: cite DF′ |
| Corollary LP′ | SIGNED | SIGN | — (uses LP, FB, J1, Lemma U; not DF or WAKE) |

## 1. Lemma DF is FALSE as stated; DF′ replaces it
- FALSE (both referees; the lane accepts). The failing step is "σ_{k+1} is a maximum of the arena, so by VJ00 Lemma 5.8 (2 ⇒ 3 ⇒ 1) it has no
  improvement". At an OWN W-cycle node y a length-only improvement survives the arena optimum: FIX 2's DFS choice at a cycle node ignores
  lengths, and VJ00's proof of 2 ⇒ 3 fails there (Prog clause 3 ignores lengths; RESULTS R15 side finding, R-N5T). L-NEW: my packet §0
  called that direction "proved there"; it is not, at cycle nodes.
- Counterexamples (Lead re-ran both: n5.py 2 iterations / 1 fallback, Oink OK, strategies verified, one Odd choice vertex):
  - REFEREE: docs/referee/R-N5-LP/df_cex.pg, n 11, sha1 a128663eae53c471f86ea32bfafaf63c05977486. Transition 0 → 1 (S4a, one phase):
    y = 7 is its own cycle node, arena {4, 8}, S4a keeps 4; at state 1, (7, 8) is a gate edge (Ξ_1(8) = (7, ∅, 5) ▷ Ξ_1(4) = (7, ∅, 3), 7
    odd) but a = 4 ∉ R_1 = {1, 9}. The next transition is the S4c fallback 7 → 8.
  - REFEREE-2: docs/referee-2/R2-N5-LP/instances/df_cex.pg, n 5, sha1 0a98e1b7ad99d007abdd0f1c39387dd0232f656d. y = 2, own cycle node of
    2 → 4 → 2; (2, 0) stays a level −1 gate edge after the S4a step, a = 4 ∈ F_1.
  - DATA: every DF failure seen (REFEREE 96 library + 74 random; REFEREE-2 176 + 28) has y its own W-cycle node and a level −1 edge; 0
    failures with y not its own cycle node (REFEREE 11,860 + 172 + 5 checks; REFEREE-2 15,746).
- **Lemma DF′ (SIGNED by both).** As DF, with the extra hypothesis that y is not its own W-cycle node at k+1 (λ_{W,k+1}(y) ≠ y).
  Equivalently for the use below: λ_Ξ(y) ≠ y, since if a ∈ F_{k+1} then y ∈ F_{k+1} and on F, Ξ = W (R19 (a)).
  - Proof (REFEREE-2 §4.3). Suppose a := σ_{k+1}(y) ∈ F_{k+1}. Then y ∈ F_{k+1} and λ_W(y) = λ_Ξ(y) ≠ y. σ_{k+1} is a pointwise optimum of
    the one-player arena H_k against τ (R17 (F1)); its VJ00 valuation there is W_{k+1}. If W_{k+1}(z) ▷ W_{k+1}(a), the single switch y → z is
    an improvement in the arena: R15 (a) (Lemma A) gives W′ ⊵ W_{k+1}, (F1) gives W′ ⊴ W_{k+1}, so W′ = W_{k+1}, and R15 (b) (Lemma B) then
    forces λ_W(y) = y, a contradiction. So W_{k+1}(z) ⊴ W_{k+1}(a), and the packet's second step runs verbatim: Ξ_{k+1}(z) ⊴ W_{k+1}(z)
    ((XW), VJ00 (11)) ⊴ W_{k+1}(a) = Ξ_{k+1}(a) (R19 (a)), against (y, z) being a gate edge at k+1. □
  - Alternative proof (REFEREE §3.2): y ≠ λ_W(y) gives W_{k+1}(y) = y ⊕ W_{k+1}(a) (P2); Bellman at an arena optimum (R24 G-TB-1 closure,
    (F1) only) gives W_{k+1}(y) ⊵ y ⊕ W_{k+1}(z); if z's play avoids y, ⊕ y is strictly monotone; if it passes y, the loop y → z → … → y
    with top t gives either a better cycle for Even (against (F1)) or W(z) ◁ W(a) directly. So W_{k+1}(z) ⊴ W_{k+1}(a); then as above.
- Lemma DF's first step ("no improvement in the arena") is likewise true for every y that is not its own W-cycle node, and only for those.

## 2. Lemma WAKE: cite DF′ (W-1 = G-LP-1, closed)
- Replace "Lemma DF at that step" by "Lemma DF′ at that step". Its hypothesis holds: y's switch at k′ is relevant, so λ_Ξ(y) ≠ y, which is
  what DF′'s proof uses (if a ∈ F then y ∈ F and λ_W(y) = λ_Ξ(y)); and for y ∈ R the claim a ∈ R is immediate (REFEREE W-1).
- Route-form clause: it uses DF's first step "W_{k′}(z) ⊴ W_{k′}(a)" at y ∈ R. In route form λ_W(y) = c_w ≠ y for y ∈ R \ {o}
  (c_w ∈ F ∪ {o}), so DF′'s first step applies (REFEREE-2 G-LP-1).
- Corollary LP′ is unaffected; its closing remark ("every wake is an R-changing transition of a U1 piece or of a U2 / U3 / U23 stretch")
  uses WAKE, valid with this repair.

## 3. Lemma HI's Consequence (HI-1 = G-LP-2)
- Lemma HI itself is signed. Its "Consequence: M_{k+1} = M_k if M_k > L_k, and M_{k+1} ≤ L_k if M_k = L_k" is unproved as written: an Even
  own cycle node that switches is outside HI (its switch is not counted in L_k, and its gate edges at k+1 are measured from the new
  successor). REFEREE-2 saw 377 of 428 own-cycle-node switches above L_k.
- Repaired form (REFEREE HI-1): M_{k+1} ≤ M_k at every transition of a phase. At k+1 a gate edge (y, z′) of level > L at a switched own
  cycle node y, measured from z = σ_{k+1}(y), has the COARSE_L values it had at k, and Ξ_k(z) ▷ Ξ_k(σ_k y); by the ultrametric property its
  level is ≤ max(lev_k(σ_k y, z), lev_k(σ_k y, z′)) ≤ M_k, with z′ a gate target at k. The packet's "=" and "≤ L_k" hold when no own cycle
  node switches at k with level > L_k (REFEREE-2).
- The Consequence is used nowhere in §2-§4. DATA (REFEREE-2): the packet's form held at all 2,472 (M_k > L_k) and 8,240 (M_k = L_k) cases.

## 4. Theorem LP step 4: the ⊕ sentence (N-LP-1)
- Replace "y ⊕ keeps order and strictness between values of one cycle node" by: "here Ξ_{k+1}(z), Ξ_k(z) and Ξ_k(a) have the same cycle node
  and the same path set (COARSE_{−1} is constant on the run), so y ⊕ adds y to all three or to none and raises each length by 1; it keeps
  their order and strictness." The general phrase is false for set-valued ⊕ (R24 TB-1 (b)); the step only needs the equal-path-set case.

## 5. §6 data line on dormant edges
- In "Dormant edges (dormant.py …): … F → F 0 and F → R 0 (Lemma DF)", read "for relevant y (λ_Ξ(y) ≠ y; Lemma DF′)". dormant.py counts
  gate edges of level > L_k at NO-WAKE-type steps, whose L_k excludes own cycle nodes but whose edge list does not; the 0 F → F count holds in
  that data, but the lemma behind it is DF′. L-NEW: the referees' DF failures are level −1 edges at own cycle nodes, which dormant.py never
  lists (it keeps only levels > L_k ≥ −1).

## 6. Labels after two signatures (D18/L40)
- PROVED (L-NEW; REFEREE and REFEREE-2, Opus 5.5, D15), pending CHECKER: Lemmas U, HI, UL, GR, NU and Theorem LP on every game inside a
  phase; DF′, BAND, WAKE (with §2) and Corollary LP′ on 𝒞^1O.
- FALSE: Lemma DF as stated (two counterexamples, §1); (NO-WAKE) (nowake_cex_n32, packet §5).
- OPEN: X, K per phase; G-N5-TIME.
