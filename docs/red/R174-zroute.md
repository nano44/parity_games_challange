# R174 Route (Z) of R173: inside one λ_W-phase a W-strict climb through a shared portal is possible only by Ξ-gating (Lemma PHASE-PORTAL, PROVED, lane); a pivot whose own level markers sit in its option prefixes cannot be Ξ-gated (Corollary SELF, PROVED, lane), so the natural two-pivot ping-pong dies. No kill (L-RED successor 41)
Started 2026-11-01 07:48Z (Lead GO R174, date -u). Brief: «route (Z): a pivot whose portal's honest Ξ sink climbs once per wave …
Aim for a W-strict climb at bounded ODIFF (2-3) with PHNF super-linear per λ_W-phase. If it is not possible, give the exact obstruction.
Check first that R88 (λ_Ξ constant on a frozen W-phase) does not already rule (Z) out inside one TWO-FIX window. If (Z) dies quickly,
go on to (C).» Labels: PROVED (lane), DATA, READING, OPEN. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Answer
- R88 does not rule (Z) out. A frozen W-phase holds λ_Ξ constant by its definition (N5-FRZ-box29 §0). A TWO-FIX window does not: its
  fallback-free stretches do contain λ_Ξ(X) changes.
  - DATA: pair_d20 (R173 pin). Inside one fallback-free window stretch, X = 12 has Ξ-cycle nodes 33 → 31 → 19 → 4 while h = 1 climbs
    3 W-strict levels through X.
- Lemma PHASE-PORTAL (PROVED, lane, §1).
  - Setting: an Even vertex h makes two consecutive moves i_0 → i_1 → i_2 between options of one portal class X, in a fallback-free
    window stretch. X's W-cycle node θ is the same at both moves (TH), e.g. inside one λ_W-phase.
  - Conclusion: if i_2 was already Ξ-improving at the first move, the second move is an exact τ-tie.
  - So every W-strict climb step through one portal inside one λ_W-phase is Ξ-gated: the next option becomes Ξ-improving only later.
    With R173's ZC this needs a λ_Ξ(X) change between the two moves. Route (Z) is therefore necessary, not just one option.
- Corollary SELF (PROVED, lane, §2). Suppose the top-ranked vertex of prefix(i_0) ∪ prefix(i_2), counted above X's Ξ-cycle node,
  favours i_2. Then the Ξ-gate is open at the first move, and PHASE-PORTAL makes the second move W-flat.
- READING (§3): this kills the natural (Z) family, a two-pivot ping-pong whose pivots' Ξ-cycle nodes are the partner's thresholds.
  - A pivot's level-x cycle node is the top vertex of its own option-x prefix: the only level-specific part of its cycle.
  - So the gate it needs at level x + 1 is already open at level x, in both parities. One W-strict level per λ_W-phase per portal.
  - The waves themselves can carry cycle values hop by hop, so they are not the obstruction (§3).
- DATA (§4):
  - Corpus, de-duplicated per Erratum E-1: 813 distinct runs on 719 games; PHASE-PORTAL VIOLATIONS 0.
  - 4 zclimb runs: the longest W-strict same-portal run is 3 moves (pair_d20). In every one of them X's W-cycle node changes at every
    step (WCH = moves − 1): no Ξ-gated step inside a λ_W-phase was found.
- No family with PHNF super-linear per λ_W-phase at bounded ODIFF. (C) was not built (§5).

## 1. Lemma PHASE-PORTAL (PROVED, lane)
- Setting and notation as in R173 §1 (TWO-FIX window, G_F, W_j = val(σ_j, τ), Ξ_j = val(σ_j, σ̄), prefix, cls, K_c, ≻_c, the prefix
  equation (P1), the choice rule (P2)).
- Statement: let h move i_0 → i_1 at transition j_1 and then, as its next move, i_1 → i_2 at transition j_2, with no S4c fallback at
  j_1..j_2 and cls(h, i_1) = cls(h, i_2) = X. Assume:
  - (TH) node(W_{j_1}(X)) = node(W_{j_2}(X)) =: θ;
  - (NRW) h and the vertices of prefix(h, i_1), prefix(h, i_2) are off X's W-play at states j_1 and j_2.
  If i_2 ∈ I_{j_1−1}(h), then W_{j_2}(i_1) = W_{j_2}(i_2).
- Proof.
  - By (P1) for W at j_1 and at j_2, W_j(i_1) vs W_j(i_2) is ≻_θ at both times, the same static order (it depends only on θ).
  - At j_1, i_2 is in h's arena and h chose i_1. By (P2), i_1 ⪰_θ i_2. At j_2, h chose i_2 while i_1 = σ_{j_2−1}(h) was in the arena,
    so i_2 ⪰_θ i_1.
  - Hence K_θ(i_1) = K_θ(i_2) and |prefix i_1| = |prefix i_2|, and (P1) at j_2 gives equal values. ∎
- Corollary PP-1 (PROVED, lane).
  - Setting: a λ_W-phase (every W-cycle node fixed, so (TH) holds), with (NRW).
  - Claim: a W-strict second move i_1 → i_2 needs i_2 ∉ I_{j_1−1}(h). So i_2 becomes Ξ-improving over h's choice only after the first move.
  - If moreover (ZC) and (NR) of R173 hold on [j_1 − 1, j_2 − 1], the Ξ-order is static and i_2 ≻_Z i_1 ≻_Z i_0, so i_2 ∈ I_{j_1−1}.
    Hence a W-strict second move inside a λ_W-phase needs X's Ξ-cycle node to change between j_1 − 1 and j_2 − 1 (or NR to fail).

## 2. Corollary SELF (PROVED, lane)
- Statement: in the setting of PHASE-PORTAL, add:
  - (NRX) h and the vertices of prefix(h, i_0), prefix(h, i_2) are off X's Ξ-play at state j_1 − 1, and cls(h, i_0) = X;
  - (H) let Z := node(Ξ_{j_1−1}(X)) and let u be the top-ranked vertex of K_Z(i_0) Δ K_Z(i_2). Then u exists and favours i_2: either u is
    even and u ∈ prefix(h, i_2), or u is odd and u ∈ prefix(h, i_0).
  Then i_2 ∈ I_{j_1−1}(h), so the move at j_2 is an exact τ-tie.
- Proof: by (P1) for Ξ at j_1 − 1, Ξ(i_2) ≻ Ξ(i_0) = Ξ(σ_{j_1−1}(h)) is decided by u, which favours i_2 under (H). So i_2 ∈ I_{j_1−1}(h).
  Then apply PHASE-PORTAL. ∎
- What it means: a W-strict climb of two consecutive levels inside one λ_W-phase through one portal needs, at the first move, a prefix
  structure in which the level after next is still Ξ-worse than the current level.

## 3. The natural (Z) family, and why it dies (READING, with the proved pieces marked)
- The family I tried, on paper (runquad's two pivots A, B and reactors, with values carried by Ξ-cycles):
  - A's options share one portal X_A. Their Ξ-suffix runs to r_m and on into whichever pivot the reactors point to.
  - When the reactors point to B, A's portal sees B's Ξ-cycle. Its node is the threshold Z_A that gates A.
  - A's level-x cycle closes when the wave toward A completes: r_m → a-chain → A → prefix_x → X_A → r_m. Its node c^A_x becomes B's
    threshold.
  - The leapfrog needs c^A_x ≺ c^B_x ≺ c^A_{x+1} (Even's order): the reactors flip to the pivot whose cycle is better.
- The waves work (READING, checked by hand):
  - r_j's a-route through r_{j−1} reaches B's cycle without passing A's prefix (r_{j−1} still on b). The bad marker a_j makes it worse
    than b_j.
  - Once r_{j−1} points to A, the a-route carries A's prefix marker. That marker is counted above B's node and good, so r_j switches.
    One reactor per step, as in runquad.
  - At the end, r_m's switch closes A's cycle.
- The gate fails (Corollary SELF applies):
  - The only level-specific vertices on A's level-x cycle are those of prefix_x. So c^A_x is the top vertex of prefix_x, unless a
    constant part dominates, in which case the node would not change.
  - Even nodes (rising): at A's move x → x + 1, Z_A = c^B_x < c^A_{x+2}. The top of prefix_x ∪ prefix_{x+2} is c^A_{x+2}: it ranks above
    c^A_x, and c^A_x is prefix_x's top. It is even, in prefix_{x+2}, and counted above Z_A. So (H) holds and the climb x + 1 → x + 2 is
    W-flat.
  - Odd nodes (falling ranks): rank c^A_x > rank Z_A = rank c^B_x > rank c^A_{x+1} > rank c^A_{x+2}, and every vertex of prefix_{x+2} has
    rank ≤ rank c^A_{x+2}. The top of the union is c^A_x: odd, in prefix_x \ prefix_{x+2}, counted. If c^A_x were in prefix_{x+2}, A's
    level-(x+2) node would rank ≥ c^A_x. So (H) holds again.
  - Blocking with extra odd markers does not help. A blocker above c^A_{x+2} in prefix_{x+2} would sit on A's level-(x+2) cycle and
    become its node.
  - Result: A rises W-strictly at most once per λ_W-phase per portal. PHNF per λ_W-phase is O(number of portals + ODIFF) for this
    family.
- What is not covered (OPEN):
  - level-specific vertices on the pivot's cycle outside its prefix, e.g. a selector vertex elsewhere on the cycle. That selector is
    itself a climber, and PHASE-PORTAL applies to it in turn;
  - Ξ-gating by an external source: Z_A taken from a third structure that is not a pivot's own cycle;
  - (C): moves made while h is on X's play (NR fails).

## 4. DATA
| set | runs | same-portal pairs | TH + NRW | i_2 available at j_1 (AV) | AV ties | VIOLATIONS | W-strict gated (not AV) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| box 53 corpus, de-duplicated (sbcg.lst 719 + alt_all lines with a start 94 = 813 distinct, E-1) | 813 | 0 | 0 | 0 | 0 | 0 | 0 |
| R173 pins pair_d20 / c_24_12 / tie_k6 | 3 | 11 / 5 / 0 | 0 | 0 | 0 | 0 | 0 |
- zclimb (longest W-strict same-portal run per game): corpus max 1 move (no W-strict same-portal pair in any of the 813 runs). Climbs zcl.py (n 24-40, 4 runs, ≤ 30,000 mutations; score
  1000·moves + 10·span) reach 2 moves with span ≤ 17 (z_24_41, z_28_44). The n 32 and n 40 runs were stuck at 1 move. Every reported
  run has WCH = moves − 1: X's W-cycle node changes at each step, so it is never inside one λ_W-phase.

## 5. Route (C)
- Not attempted beyond the ping-pong: there the pivots move only while the reactors point to the partner, i.e. while they are off
  their own cycle, so NR holds at their moves. A family where h moves while on X's play is OPEN.

## 6. Tools (experiments/red/r174/)
- phasepair.py G START (PHASE-PORTAL check), zclimb.py G START (longest W-strict same-portal run, ZCH / WCH), zcl.py (climb),
  runcorp.sh (de-duplicated corpus, out/corp.txt).
- check.sh block «R174»: phasepair and zclimb on pair_d20.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/red/r174/*; check.sh block R174; R173 note corpus line de-duplicated per E-1; notebook. SHAs in the
  push / message.
- FINDINGS:
  - R88 does not exclude (Z) inside a TWO-FIX window (λ_Ξ(X) changes in fallback-free stretches, pair_d20).
  - PHASE-PORTAL PROVED (lane): inside a λ_W-phase a W-strict second same-portal move is Ξ-gated (the option was not improving at the
    first move). With ZC that needs a λ_Ξ(X) change, so (Z) is necessary.
  - SELF PROVED (lane): if the top counted vertex of the two prefixes favours the later option, the gate is open and the climb is flat.
    The natural ping-pong meets SELF's hypothesis in both parities (READING), so it rises once per λ_W-phase per portal.
  - DATA: corpus 0 violations; no Ξ-gated W-strict step inside a λ_W-phase found by corpus or climbs.
  - No kill. (C) and external Ξ-gating are open.
- NEEDS: Lead: PHASE-PORTAL / SELF to L-NEW 45 (box 128 PORTAL-COUNT) as inputs. My next-box suggestion: an external Ξ-gating source
  (a third structure whose Ξ-cycle rises once per wave), or (C).
