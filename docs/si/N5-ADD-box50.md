# N5-ADD (box 50): an additive charge for REPEATs. Each edge has at most one REPEAT per window; [P-REP] ⟺ [P-RT] ⟺ [P-WT] ∧ [P-X]; the circle as one premise
L-SI successor 32 (Opus 5.5), D15 / D18, Lead reading L40. Lead 2026-10-30 04:57Z: «[P-REP] needs an ADDITIVE count of repeats along window
chains, not Σ(n·m_E)^d … Find a charging scheme in which each repeat pays a distinct (vertex, W-change) or (edge, W-change) token, so that
REP ≤ poly·(W-changes per W-run). Then compose with WV-R, accepting the circle explicitly as a single premise if needed.» Working note,
unrefereed, not a TARGET.md claim. G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Tool: experiments/si/odd/windag.py (the window DAG: BETA, INDEG, NPATH, LONG, TOK / TOKSH, ETOK_V, SELFL, CHREP, EPATH; docstring).
  Output odd/out/windag_corpus.txt (719 games of odd/sbcg.lst). Pinned in si/check.sh «box 50».
- Instances: odd/inst/red50/wdepth_K4_m16 / m32 = L-RED's mkrw.py (sha1 0a473bd5…, R130) with LATE=2, regenerated here; R130's
  REP 21 / 45 and depth 7 / 15 reproduce.
- Setting and symbols as in box 48 (docs/si/N5-WDEPTH-box48.md): a W-run F (RESULTS R89); late adoption, FIRST / REPEAT (P-N5-CUT §6);
  R*_T(F) := the late transitions of F; a REPEAT ρ of e = (y, z) at u₂ with previous late adoption of e at u₁ and y's last leave of z at
  k is CHAINED if W(z) changes at a transition of [k + 1, u₂ − 1], t*(ρ) the last one; otherwise EXCEPTIONAL (W-silent, own-cycle, SELF),
  X_F their number. The window of t is opened by the last late transition ≤ t (INIT if none). WT_F := W-changing transitions of F.
  n_E := the Even vertices.

## 1. Lemma ONE-PER-WINDOW (PROVED, lane)
- Statement. For every Even edge e, at most one chained REPEAT of e is charged to each window. If e has late adoptions u⁰ < u¹ < … in F,
  the window of t*(ρ_j) (ρ_j the REPEAT at u^j) is opened by a late transition in [u^{j−1}, u^j).
- Proof. y adopts z at u^{j−1}, so σ_{u^{j−1}+1}(y) = z; the leave k has σ_k(y) = z ≠ σ_{k+1}(y), so k ≥ u^{j−1} + 1, and
  t* ≥ k + 1 > u^{j−1}. The transition u^{j−1} contains a late adoption, so the last late transition ≤ t* is ≥ u^{j−1}. And t* ≤ u^j − 1,
  so it is < u^j. The intervals [u^{j−1}, u^j) are disjoint for different j. □
- Corollary (PROVED, lane). Box 48's window capacity n·m_E drops to m_E: REP_F ≤ X_F + m_E·(1 + R*_T(F)), and in Theorem REP-DEPTH
  R₁ ≤ (1 + m_E + X_F)·m_E, R_{d+1} ≤ m_E·R_d. The bound is still multiplicative in the depth: this is a factor n, not the additive count.

## 2. Theorem CIRCLE (PROVED, lane): the three circle quantities are polynomially equivalent
- (a) REP_F ≤ n_E·R*_T(F). Every REPEAT is a late adoption at a late transition, and one transition changes σ(y) at most once per Even y.
- (b) R*_T(F) ≤ m_E + REP_F. A late transition contains a FIRST (at most m_E FIRSTs per W-run, LATE-SPLIT (i)) or a REPEAT.
- (c) REP_F ≤ X_F + Σ_z d_E(z)·WCH_F(z) ≤ X_F + m_E·WT_F. This is the additive charge the Lead asked for. The token of a chained ρ is
  the triple (y, z, t*(ρ)) (edge, W-change of its target). It is injective: for one edge the intervals [k + 1, u₂ − 1] of different
  REPEATs are disjoint (box 48 §2 (i); ETOK_V 0 in all data). A W-change of z at t pays at most d_E(z) tokens.
- (d) WT_F ≤ (n − 1)(R*_T(F) + 1) (RESULTS R89, GP*-RUN with Corollary FW-R*), and Σ_z WCH_F(z) ≤ n·WT_F.
- So, per W-run and up to polynomial factors: [P-REP] ⟺ [P-RT] ⟺ [P-WT] ∧ [P-X], where
  - [P-RT]: R*_T(F) ≤ p(n);
  - [P-WT]: WT_F ≤ p(n);
  - [P-X]: X_F ≤ p(n).
  - Proof. (a)+(b) give the first equivalence. (c) gives ⇐ from the right, and REP ≥ X_F with (d) gives ⇒. □
- Additive form (the Lead's charge). Every REPEAT pays a distinct (edge, W-change) token, so REP_F ≤ X_F + m_E·WT_F. The W-changes are
  counted once, whatever the window depth. Composing with (d) closes the circle, with gain factor m_E(n − 1) and no contraction.
  So the circle cannot be broken by charging alone. It needs one bound on any one of R*_T, WT or REP that comes from somewhere else.

## 3. Composition with WV-R and CUT-RED (PROVED, lane, arithmetic): the circle as ONE premise
- Box 41's Lemma WV-R per guided stretch Q: WCH_Q(w) ≤ Λ_Q + (Λ_Q + 1)(n − 1)(R*_Q + 1), Λ_Q ≤ n(n − 1). With §2 (b):
  WCH_Q(w) ≤ n(n − 1) + (n(n − 1) + 1)(n − 1)(m_E + REP*_Q + 1).
- P-N5-CUT's Theorem CUT-RED (R90 as landing): G-N5-TIME ⇐ B* ∧ REP* ∧ SC* ∧ O*. By §2, REP* may be replaced by either of:
  - [P-WT]* ∧ [P-X]*: every W-run has polynomially many W-changing transitions, and polynomially many exceptional repeats;
  - [P-RT]*: every W-run has polynomially many late transitions.
- [P-WT]* is the circle stated once. It is a statement about the Even one-player dynamics inside one W-run: τ is fixed, λ_W is fixed,
  there is no fallback, and Even's step is W_{t+1} = the W-optimum of the arena H_t = σ_t ∪ Iσ_t (S4a). The two-player content enters only
  through the Ξ-gate Iσ_t.

## 4. DATA: the window DAG (windag.py)
- Nodes are windows (INIT and one per late transition). Each chained REPEAT ρ at u gives an arc from the window of t*(ρ) to u.

| instance | n | REP | late transitions | BETA (most children) | INDEG | NPATH | LONG | TOKSH | EPATH | SELFL / CHREP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| wdepth_K4_m16 (R130) | 146 | 21 | 36 | 1 | 1 | 1 | 7 | 1 | 1 | 0 / 0 |
| wdepth_K4_m32 (R130) | 234 | 45 | 68 | 1 | 1 | 1 | 15 | 1 | 1 | 0 / 0 |
| latew_K20_m32 (R127) | 538 | 570 | 640 | 30 | 1 | 1 | 1 | 1 | 1 | 0 / 0 |
| so_th_n32 | 32 | 2 | 5 | 1 | 1 | 1 | 2 | 1 | 2 | 1 / 0 |
| corpus (719 games; maxima over W-runs) | | ≤ 6 | ≤ 17 | 1 | 1 | 1 | ≤ 2 | 1 | ≤ 2 | 3 / 0 (sums) |

- The DAG is a forest in all data (INDEG 1, NPATH 1). Its components are paths (wdepth: depth (m − 1)/2, one child per window) or stars
  (latew: one FIRST window with 30 leaf children).
- TOKSH = 1 everywhere: no two chained REPEATs share a (vertex, W-change) token (z, t*), even on latew. CONJECTURE TOK1: chained
  REPEATs ≤ Σ_z WCH_F(z), dropping d_E(z) from §2 (c). It is DATA only, and does not touch the circle.
- EPATH = 2 only on so_th_n32: there an edge's REPEAT is charged to the window of its own previous adoption (SELFL). In repchain.py's
  causal reading the parent there is a plain switch (box 48 §3), so this is a timing coincidence, not self-re-arming.

## 5. READING: what an additive bound would need, and a kill target
- The window DAG attributes a REPEAT to a window by time, not by cause. Staggered adoptions put sibling REPEATs into consecutive windows,
  so BETA and LONG measure timing. No branching statement about this DAG can be proved independently of the dynamics.
- The causal chain (repchain.py, box 44: the parent of ρ is the switch at t* on the play from z) agrees with the window chain on R130:
  repchain's causal maxdepth is 7 = MAXWD on wdepth_K4_m16 (parR 18, LDEC_V 0). Along a causal arc ρ′ (adoption by x at t*) → ρ (adoption
  of (y, z) at u), x lies on z's play at t* + 1 and W(z) is constant on [t* + 1, u]. So after u, y's play runs through z and then x: the
  chain moves down the in-tree of the (σ, τ)-plays, and the W-length of the adopter grows (LDEC_V 0 on wdepth). If that held as a
  lemma, causal depth would be ≤ n. It is not proved: plays change between t* + 1 and u, and W(z) may change at u itself.
- Depth ≤ n does not bound REP: a causal tree of depth n and branching b has b^n nodes. Each re-block of a reader (y′, z′) under x needs
  W(z′) to rise past W(σ y′) while Ξ(z′) ⊴ Ξ(σ y′), and each re-adoption needs a new Ξ-rise of z′ (R89 LATE-RISE). Both are a gap at z′:
  Ξ(z′) ⊴ Ξ(σ y′) ⊴ W(σ y′) ◁ W(z′), since Ξσ ⊴ val(σ, τ) pointwise.
- KILL TARGET (for L-RED; a kill of [P-REP], so of REP* as a premise):
  - a causal reader tree of branching 2 and depth Θ(n), inside one W-run;
  - each late adoption at a node re-blocks both children, which are in its in-subtree;
  - the children are released by Ξ at different transitions, so each child's own wave re-arms ITS children again;
  - REP would then be 2^Θ(n).
  - R130 is the depth-only (branching 1) case. latew is the breadth-only (depth 1) case. The two have not been combined.
- POSITIVE ROUTE (for a proof; READING): a reader re-armed by every ancestor wave pays one Ξ-climb at a gap vertex per re-arm. This is
  L-NEW box 70's GXC count (Ξ-climbs at gap vertices with W fixed) read inside one W-run. So [P-WT]* would follow from GXC per W-run
  polynomial if every re-arm's Ξ-climb happens with W(z′) fixed. Not checked; next box.

## 6. DATA: re-blocked REPEATs are paid by TIED Ξ-climbs of their target (odd/tied.py; probe of §5's positive route)
- Split a REPEAT ρ of (y, z) at u (y's last leave of z at k) into two kinds:
  - RE-BLOCKED: (y, z) is BLOCKED at some state of [k + 1, u];
  - STALE: otherwise. It counts as late only because (y, z) was blocked before its previous adoption: late.py's `last` set never forgets.
- A TIED Ξ-CLIMB of z at s ∈ [k, u − 1] is a transition with Ξ_{s+1}(z) ▷ Ξ_s(z) and W_{s+1}(z) = W_s(z).
  - Then z ∈ Z_s automatically: Ξ_s(z) ◁ Ξ_{s+1}(z) ⊴ W_{s+1}(z) = W_s(z), by XW (Ξσ ⊴ val(σ, τ)).
  - It is L-NEW box 70's GXC event read at the TARGET z, with no switch of z required.

| set | REPEATs | re-blocked | stale | tied | untied | untied AND re-blocked | most REPEATs per (z, last tied s) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| latew_K20_m32 | 570 | 570 | 0 | 570 | 0 | 0 | 1 |
| wdepth_K4_m16 | 21 | 21 | 0 | 21 | 0 | 0 | 1 |
| corpus (719) | 41 | 4 | 37 | 9 | 32 | 0 | 1 |

- CONJECTURE TIED-RB: every re-blocked REPEAT of (y, z) has a tied Ξ-climb of z on [k, u − 1].
  - What is proved toward it: from the last blocked state t_b ≤ u − 1, R89's LATE-RISE gives Ξ_u(z) ▷ Ξ_{t_b}(z). It does not give that
    the climb happens with W(z) fixed.
  - With TOK1-style injectivity (DATA: 1 per token), TIED-RB would give re-blocked REP_F ≤ Σ_z d_E(z)·TXC_F(z), TXC = tied Ξ-climbs. That
    charges the families that drive REP (R127 breadth, R130 depth) to GXC-type events instead of to W-changes, and so leaves the circle.
- Stale REPEATs (37 of 41 in the corpus; all of fc_N / switchbestexp_N, ≤ 6 per game) are re-adoptions on a plain wave. They need a
  separate count: W(z) rises past W(σ y) while (y, z) ∈ Iσ, which is the plain-wave mechanism of GP*. Not bounded here.
- Next box (proposed): prove TIED-RB, or kill it with an instance; then bound stale REPEATs per W-run (or drop them by changing the
  late-adoption definition to forget a block at each adoption, and re-check R89 GP*-RUN under that definition).

## DONE / FINDINGS / NEEDS
- DONE: odd/windag.py, odd/tied.py (out/tied_corpus.txt); corpus, latew, wdepth m16 / m32, so_th; si/check.sh «box 50»; this note.
- FINDINGS:
  1. PROVED (lane): Lemma ONE-PER-WINDOW (≤ 1 chained REPEAT per edge per window); REP_F ≤ X_F + m_E(1 + R*_T); REP-DEPTH with ratio m_E.
  2. PROVED (lane): Theorem CIRCLE, [P-REP] ⟺ [P-RT] ⟺ [P-WT] ∧ [P-X]. The additive charge REP ≤ X + Σ_z d_E(z)·WCH_F(z) has
     one distinct (edge, W-change) token per REPEAT.
  3. PROVED (lane, arithmetic): CUT-RED's REP* can be replaced by the single circle premise [P-WT]* ∧ [P-X]* (or [P-RT]*).
  4. DATA: the window DAG is a forest of paths and stars; TOKSH 1 (CONJECTURE TOK1); X 0.
  5. READING: charging alone cannot break the circle (gain m_E(n − 1)). The kill target is a binary causal reader tree; the positive
     route is GXC inside a W-run.
  6. DATA (§6): every re-blocked REPEAT has a tied Ξ-climb of its target (574 / 574; latew 570 / 570). CONJECTURE TIED-RB.
     The 32 untied REPEATs are all stale.
- NEEDS: none from the owner.
