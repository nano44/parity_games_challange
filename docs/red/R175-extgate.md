# R175 External Ξ-gating: an odd Ξ-cycle node at the portal allows at most two consecutive W-strict climbs (Lemma ODD-GATE, PROVED, lane); an even one needs an Even-winning Ξ-cycle at a τ-stable ODIFF vertex, and every re-armable gate source recurses to one fresh branching vertex per level. No kill (L-RED successor 41)
Started 2026-11-01 09:15Z (Lead GO R175, date -u). Brief: «external Ξ-gating: a third structure whose Ξ-cycle node rises once per wave
and gates the pivot's portal … W-strict same-portal climbs inside ONE λ_W-phase at ODIFF 2-3 … PHNF super-linear per λ_W-phase. Check
first whether the gating structure is itself a climber (so PHASE-PORTAL applies and it recurses); if so, say what the recursion costs per
level … If external gating dies, try (C).» Labels: PROVED (lane), READING, OPEN. Not a TARGET.md claim. G-N5-TIME stays OPEN.
Nothing here is reported DEAD: no explicit-bound kill, and no new DATA beyond R174.

## 0. Answer
- Lemma ODD-GATE (PROVED, lane, §1). Inside one λ_W-phase, three consecutive W-strict moves of a vertex through one portal X cannot
  happen while X's Ξ-cycle node Z is odd.
  - Reason: an odd node only falls in rank (Ξ is non-decreasing, RESULTS R15), so Ξ's comparisons only refine. A refining gate opens
    at most twice in a row.
- So a sustained external gate must give the portal an EVEN, rising Ξ-cycle node. The portal's honest Ξ-play then ends in an
  Even-winning cycle.
- For a single climber this works (§2, READING): odd blockers in the option prefixes, Ξ's even ties broken by length, and W blind to the
  blockers. So PHASE-PORTAL's escape is real.
- The gate source:
  - A re-armable source has to climb. It climbs W-strictly unless the engine switches on exact τ-ties, which tie_k6 says it does not.
    So PHASE-PORTAL and SELF apply to it, and it needs its own external gate.
  - The recursion ends only at a source whose levels sit in distinct classes. That means one fresh branching vertex per level: an
    ODIFF vertex as in runquad, or an Even gate, which R173 §2 (E) reduces to a per-level divergence.
  - A non-re-armable source (a clock of delay chains) costs Θ(m) fresh vertices per level instead.
  - Cost per level of the recursion, the quantity asked for: one fresh branching vertex, or Θ(m) fresh vertices. With K levels this
    gives ODIFF Θ(K), or PHNF linear in n.
- The even gate also has a stability cost (§3, READING). The ODIFF vertex d₂ that closes the Even-winning Ξ-cycle must keep I_τ(d₂) = ∅.
  - Under Even's dual best reply, d₂'s σ̄-route is the cycle body plus its τ-route, and none of the body may rank above the cycle node.
  - So it needs a hostile Even detour. Every detour I built either reopens the regress (a further ODIFF vertex), or is Ξ-improving, or
    is seen by the main portal.
- (C) (§4) was not built.

## 1. Lemma ODD-GATE (PROVED, lane)
- Setting and notation as in R173 §1 and R174 §1. Let h make three consecutive moves x_0 → x_1 (transition t_1) → x_2 (t_2) → x_3 (t_3)
  inside one fallback-free stretch of a TWO-FIX window, with:
  - cls(h, x_i) = X for i = 0..3;
  - (TH) one W-node θ of X at t_1, t_2, t_3;
  - (NRW) and (NRX): h and the four prefixes are off X's W-plays at t_1..t_3 and off X's Ξ-plays at s_i := t_i − 1;
  - all three moves W-strict.
  Let Z_i := node(Ξ_{s_i}(X)).
- Claim: Z_1, Z_2, Z_3 are not all odd.
- Proof.
  - (a) W is static. By (P1) and (TH), W_t(x) vs W_t(y) is ≻_θ at t_1, t_2, t_3. The moves are W-strict, so
    x_0 ≺_θ x_1 ≺_θ x_2 ≺_θ x_3.
  - (b) Gates. At s_1, h picked the W-best of {x_0} ∪ I_{s_1}(h). So x_2, x_3 ∉ I_{s_1}(h): Ξ_{s_1}(x_j) ⪯ Ξ_{s_1}(x_0) for j = 2, 3,
    while Ξ_{s_1}(x_1) ≻ Ξ_{s_1}(x_0). Likewise:
    - at s_2: x_2 ≻ x_1 and x_3 ⪯ x_1;
    - at s_3: x_3 ≻ x_2.
    By (P1) for Ξ (NRX), each comparison at s_i is ≻_{Z_i}: K_{Z_i}-sets first, then lengths by the parity of Z_i.
  - (c) Refinement. Ξ_t(X) is non-decreasing in t (RESULTS R15: a switch of improving edges does not decrease Ξ pointwise; σ̄ is
    fixed). For odd nodes that means rank Z_1 ≥ rank Z_2 ≥ rank Z_3, and every comparison uses the "longer is better" rule.
    - If x ≻_{Z_i} y by sets (the top element of K_{Z_i}(x) Δ K_{Z_i}(y) favours x), then x ≻_{Z_j} y for every j ≥ i: the same top
      element is still counted and still the top.
  - (d) At s_1: x_1 ≻ x_0 ⪰ x_2, so x_1 ≻_{Z_1} x_2. This cannot be by sets, or by (c) x_1 ≻_{Z_2} x_2, contradicting move 2. So
    K_{Z_1}(x_1) = K_{Z_1}(x_2), and |x_1| ≥ |x_2| in prefix length.
  - (e) At s_2: x_2 ≻_{Z_2} x_1. The sets agree above Z_1 and |x_2| ≤ |x_1|, so the win is by sets: the top element u of
    K_{Z_2}(x_1) Δ K_{Z_2}(x_2) has rank in (Z_2, Z_1] and favours x_2.
  - (f) Also at s_2: x_2 ≻ x_1 ⪰ x_3, so x_2 ≻_{Z_2} x_3. By (c) this cannot be by sets, or move 3 fails. So K_{Z_2}(x_3) = K_{Z_2}(x_2).
  - (g) Then K_{Z_2}(x_1) Δ K_{Z_2}(x_3) = K_{Z_2}(x_1) Δ K_{Z_2}(x_2) has top element u, which favours x_3. So x_3 ≻_{Z_2} x_1,
    contradicting x_3 ⪯_{Z_2} x_1 in (b). ∎
- Remarks.
  - Only refinement is used: rank Z non-increasing on [s_1, s_3]. The parity enters only through R15's monotonicity, which makes odd
    nodes refine.
  - With Z even and rising (coarsening), the analogue fails: §2 gives a working single climber.
  - Corollary OG-1: under the premises, a stretch of r consecutive W-strict same-portal moves inside one λ_W-phase with Z odd
    throughout has r ≤ 2.

## 2. A single climber under an external even gate (READING; the construction behind the lemma's sharpness)
- Options y = 1..K of h, each a choice-free prefix into the portal X (an ODIFF vertex: σ̄ to the gate source, τ to the W-sink Ω):
  - one odd blocker b_y with rank in (Z_{y−2}, Z_{y−1}];
  - padding so that |prefix y| decreases in y;
  - all of it ranked below θ = node(W(X)), which is even and constant.
- Ξ at gate value Z_x (even, rising): b_{x+1} is no longer counted, b_y for y ≥ x + 2 still is. So x + 1 ties x on sets and wins on
  length (even: shorter), while y ≥ x + 2 are blocked.
- W at θ: blind to the blockers, shorter is better, so W strictly increases with y. Each move is W-strict, and λ_W does not change.
- Hence one W-strict climb per gate step, provided some structure supplies Z_1 < Z_2 < … (even) as X's Ξ-cycle nodes, one per wave.

## 3. The gate source (READING)
- (i) An Even-winning Ξ-cycle needs a closing ODIFF vertex.
  - X's Ξ-play must end in cycles with even, rising nodes E_1 < E_2 < …, while its W-play ends at Ω (λ_W constant).
  - If such a cycle were made of Even choices and single-edge Odd vertices only, the W-world would see it too, and λ_W would change at
    its vertices when it changes.
  - So the cycle closes through an ODIFF vertex d₂ (σ̄ closes it, τ exits to Ω). With the portal d, that is ODIFF ≥ 2.
- (ii) d₂'s τ-stability.
  - Ξ: Odd prefers the cycle, so Ω must be even and above every E_j.
  - Dual (Even best-replies to τ): d₂'s σ̄-successor reaches d₂ again only through its τ-edge, so its value is (cycle body) ⊕ (τ-route).
  - For I_τ(d₂) = ∅ the body must help Even. A counted even vertex above Ω would sit on the Ξ-cycle and become its node. A shorter path
    is impossible, since the body adds length.
  - So the help must come from Even's best reply leaving the body at some q through a hostile route R_h:
    - (a) R_h without ODIFF vertices: its Ξ-value and dual value end in the same sink up to σ versus best reply. A delay chain gives σ
      a bad sink and the best reply Ω, but the chain then propagates, changing λ_W, or its base must sit behind a new ODIFF vertex (regress).
    - (b) R_h through the portal d: Ξ sees d's σ̄-route, including the even marker m_d that d needs for its own stability, so R_h becomes
      Ξ-improving for q.
    - (c) R_h through d₂, with padding on d₂'s τ-route: d₂'s σ̄-route is again (body) ⊕ (its own τ-route), longer.
    - (d) R_h through a new ODIFF vertex d₃: d₃ has the same stability problem (regress).
  - runquad closes its regress with per-level W-loops, and its lowest level with an exact tie (YH). I found no bounded-ODIFF analogue.
    This is OPEN, not proved impossible.
- (iii) Recursion if the source is a climber (the Lead's question).
  - A re-armable source changes its Ξ-cycle once per wave by moves of its own vertices. These are W-strict unless the engine switches on
    exact τ-ties; tie_k6 (R173) shows it keeps σ on such ties.
  - If those moves go through a shared portal, PHASE-PORTAL and SELF apply: the source needs a gate outside its own prefixes, i.e.
    another source.
  - A tower of depth d needs a base climbing K levels without Ξ-gating, i.e. options in K distinct classes: K fresh branching vertices.
  - Cost per level: one fresh branching vertex at the base (an ODIFF vertex as in runquad and mkrw, or an Even gate, which needs a
    per-level divergence per R173 §2 (E)).
  - Alternatively, a non-re-armable clock (K delay chains of lengths m, 2m, …, Km) costs Θ(m) fresh vertices per level. Then
    n = Θ(K²m) against Θ(Km) transitions: PHNF linear in n.
  - This per-level charge is what L-NEW's recursive gate charge must bound.

## 4. Route (C)
- Not built. In every design above the climbing vertex moves while off its own cycle, so NR holds at its moves. A family whose climber
  moves while on X's play (h on its own cycle with a dynamic return path) is OPEN.

## DONE / FINDINGS / NEEDS
- DONE: this note; notebook. No new tools or pins: ODD-GATE is a proof, and R174's corpus already has 0 same-portal pairs, so a corpus
  check of ODD-GATE would be vacuous.
- FINDINGS:
  - ODD-GATE PROVED (lane): inside a λ_W-phase, at most 2 consecutive W-strict same-portal moves while the portal's Ξ-node is odd
    (R15 monotonicity makes odd nodes refine).
  - A sustained gate needs an even, rising Ξ-cycle at the portal. The single climber then works (§2).
  - Gate sources:
    - the closing ODIFF vertex's τ-stability regresses in every detour I tried (OPEN);
    - a re-armable source recurses under PHASE-PORTAL / SELF to one fresh branching vertex per level;
    - a clock costs Θ(m) per level.
  - No kill at bounded ODIFF.
- NEEDS: Lead: ODD-GATE and the per-level charge (one fresh branching vertex, or Θ(m) fresh vertices) to L-NEW 45 for its recursive gate
  charge. Next: (C), or a bounded-ODIFF stabiliser for an Even-winning Ξ-cycle (§3 (ii)), whichever you prefer.
