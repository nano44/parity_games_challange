# P-N5-LATEP (box 53): late adoptions that forget a block at each adoption (LATE′); FW-R*′; LATE-SPLIT′; GAP-CLIMB; GXC ⊆ TXC ⊆ ZXC; TXC-DESCENT and TXC-RED
L-SI successor 32 (Opus 5.5; D15 / D18, Lead reading L40). DRAFT, NOT FROZEN: the Lead approves the item list before the freeze (Lead
2026-10-30 05:49Z: «freeze ONE packet, P-N5-LATEP: LATE′ + FW-R*′ + LATE-SPLIT′ + GAP-CLIMB + the inclusion chain, plus (i) if it closes.
Every symbol bound, and a line file. Ask me before freezing»). After the freeze, repairs go in docs/si/P-N5-LATEP-fixes-box53.md.
Working notes with data: docs/si/N5-ADD-box50.md, N5-LATEP-box51.md, N5-TXCD-box52.md.
SCOPE (D1): lemmas about one W-run of N5 on every game. Each one is a REDUCTION or a structural fact. No count is bounded here; G-N5-TIME
stays OPEN. Not a TARGET.md claim, not an algorithm claim. Labels: PROVED (lane, unrefereed) / DATA / READING.
Every [Q path@commit:lines] «…» is verbatim (experiments/si/rund/quotecheck.py; pinned in si/check.sh «box 53»).

## 0. What to sign, and what not
| § | item | label |
| --- | --- | --- |
| §2 | Definition LATE′ and its diff against R88 §4 | definition (check the diff) |
| §3 | Corollary FW-R*′ (on every W-run) | PROVED (to sign) |
| §4 | Lemma LATE-SPLIT′ and Corollary CIRCLE′ | PROVED (to sign) |
| §5 | Lemma GAP-CLIMB | PROVED (to sign) |
| §6 | Proposition CHAIN: GXC_F ⊆ TXC_F ⊆ ZXC_F; ZXC = TXC + WZ | PROVED (to sign) |
| §7 | Lemma TXC-DESCENT and Corollary TXC-RED | PROVED (to sign) |
| §8 | READING and DATA | NOT to sign |

## 1. Setting, symbols, premises
- N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) with FIX 1-4, on any game G = (V, E, Ω, owner); n := |V|, n_E := the Even vertices,
  m_E := the Even edges, d_E(z) := the Even edges into z. A run is the sequence of states (σ_t, τ_t); a TRANSITION is t → t + 1.
- Values (c, P, ℓ) and the order ⊴ (◁ strict) as in [S1-val], [S1-ord]. Ξ_t := Ξ_{σ_t} with S1's optimal counterstrategy σ̄_t ([S1-Xi]);
  Iσ_t := [S2]'s improving edges; W_t := the valuation of the (σ_t, τ_t)-plays; λ_W, λ_Ξ the cycle-node maps of W_t, Ξ_t.
  D_t := {Odd u : σ̄_t(u) ≠ τ_t(u)}; Z_t := {v : Ξ_t(v) ≠ W_t(v)}.
- W-RUN (RESULTS R89): a maximal run of consecutive states of one τ-stretch none of whose transitions is an S4c fallback or changes λ_W.
  F = [a, b] denotes a W-run. On F, τ_t = τ and λ_W are constant, and every transition is an S4a step.
- BLOCKED (RESULTS R88, P-N5-GP §3): [Q docs/si/P-N5-GP-box31.md@170e5316:85-86] «An edge (x, z) of G with x Even is BLOCKED at state t ∈ [a,
  b) if W_t(z) ▷ W_t(ρ_t(x)) and (x, z) ∉ Iσ_t.» (ρ_t = σ_t.)
- An ADOPTION of the Even edge (y, z) at u (a ≤ u < b) means σ_{u+1}(y) = z ≠ σ_u(y). A LEAVE of z by y at k means σ_k(y) = z ≠ σ_{k+1}(y).
- Landed premises used, with the item they serve:
  - [S4a] for (A) (SPEC S4a; [Q docs/new/N5-ssi-global.md@170e5316:51] «If Iσ ≠ ∅: A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v»);
  - RESULTS R88 (P-N5-GP): Lemma W-MON, Lemma XW, Lemma GP*, Corollary FW-R* and its proof (§4, l. 143-156);
  - RESULTS R89: Lemma GP*-RUN (R88's GP* and FW-R* on every W-run), Lemma LATE-RISE, Lemma SUCC-MON;
  - RESULTS R15: each S4a / S4c step applies improving switches only, so Ξ is non-decreasing along the run;
  - RESULTS R17 (a): [V1], [V2] ([Q docs/new/N5-phase-bound-box10.md@170e5316:20-22] «(V1) if x is not its own cycle node then Ω_ρ(x) = x ⊕
    Ω_ρ(ρ(x)) and the ρ-path from ρ(x) to λ(x) avoids x. (V2) PREFIX MONOTONICITY: if a ⪯ b are values whose paths both avoid x (or whose
    cycle nodes differ), then x ⊕ a ⪯ x ⊕ b, and strictly if a ≺ b.»). They are read here for the plays of a fixed positional pair: (σ, τ)
    for W, (σ, σ̄) for Ξ, as R88 reads [CASE-A] with Ω := W;
  - RESULTS R90 (P-N5-CUT §2): Lemma OPT-OFF (ii) and Lemma W-SUCC ([Q docs/si/P-N5-CUT-box43.md@170e5316:111-112] «Let [q, p] be states of
    one τ*-piece, v Even and off-cycle for τ* at every state of [q + 1, p]. Then W^{τ*}_t(σ_t v) is non-decreasing on [q, p].»). On F,
    τ* = τ and W^{τ} = W.
- Standing premise: RESULTS R57's SPEC premise (S1's procedure realises the optimal counterstrategy; S4a's σ_{u+1} is Even's pointwise
  optimum in its arena), as R88 / R89 / R90 use it.

## 2. Definition LATE′ (the only change)
- R88 §4, verbatim: [Q docs/si/P-N5-GP-box31.md@170e5316:144-145] «A LATE ADOPTION in F is a transition τ → τ + 1 of F (a ≤ τ < b) at which
  some Even y switches, ρ_{τ+1}(y) = z ≠ ρ_τ(y), to an edge (y, z) that was blocked at some state t ∈ [a, τ).»
- LATE′. The same sentence, with «t ∈ [a, τ)» replaced by «t ∈ [max(a, p + 1), τ), p the previous adoption transition of (y, z) in F (no
  constraint if there is none)». R*′_T(F) := the number of transitions of F containing at least one LATE′ adoption.
- Every LATE′ adoption is late in R88's sense, so R*′_T ≤ R*_T. A LATE′ adoption is FIRST′ if (y, z) has no earlier adoption in F,
  REPEAT′ otherwise; REP′_F := the REPEAT′ adoptions of F.

## 3. Corollary FW-R*′ (PROVED, lane)
- Statement. Every W-run F has WCH_F ≤ (n − 1)(R*′_T(F) + 1), WCH_F := the transitions t → t + 1 of F with W_{t+1} ≠ W_t.
- Proof. R88's proof of FW-R* (P-N5-GP §4) applies on F by GP*-RUN. It runs verbatim up to «y_i adopts (y_i, y_{i+1}) at some transition
  τ → τ + 1 with t < τ ≤ k», having shown ρ_{t+1}(y_i) ≠ y_{i+1}.
  - Choose τ to be the first adoption of (y_i, y_{i+1}) after t.
  - Let p be the previous adoption of that edge before τ, if any. p ∉ (t, τ) by the choice of τ. p ≠ t, since ρ_{t+1}(y_i) ≠ y_{i+1}. So
    p < t, i.e. p + 1 ≤ t.
  - The edge is blocked at t ∈ [max(a, p + 1), τ), so the adoption at τ is LATE′.
  - The rest of the proof (k − τ ≤ n − 2; each τ is charged by at most n − 1 values of k) is unchanged, with R*′_T in place of R*_T. □

## 4. Lemma LATE-SPLIT′ and Corollary CIRCLE′ (PROVED, lane)
- (i) FIRST′ adoptions of F number at most m_E (one per edge).
- (ii) Let ρ be a REPEAT′ of (y, z) at u, with previous adoption p < u and y's last leave of z at k (p < k < u). Then (y, z) is blocked at
  some t_b with k + 1 ≤ t_b ≤ u − 1. If y is off-cycle for τ (P-N5-CUT §2) at every state of [k + 1, t_b], then W(z) changes at some
  transition of [k + 1, t_b − 1]: W_{t_b}(z) ▷ W_{k+1}(z).
- Proof of (ii).
  - Blocked at some t ∈ [p + 1, u) by LATE′. Then σ_t(y) ≠ z = σ_{p+1}(y), so y leaves z at some transition in [p + 1, t − 1]. Hence the
    last leave k before u has k ≤ t − 1, and also k ≥ p + 1.
  - Take t_b := t. t_b ≤ u − 1: (y, z) ∈ A_u(y) by [S4a] (σ_{u+1}(y) = z ≠ σ_u(y)), so (y, z) ∈ Iσ_u, so it is not blocked at u.
  - The chain: W_{k+1}(z) ⊴ W_{k+1}(σ_{k+1} y) (OPT-OFF (ii) at k → k + 1, (y, z) ∈ σ_k ⊆ H_k, y off-cycle at k + 1) ⊴ W_{t_b}(σ_{t_b} y)
    (W-SUCC on [k + 1, t_b]) ◁ W_{t_b}(z) (blocked at t_b). This is P-N5-CUT §6's chain (its l. 162), with the block now after k. □
- So W-silent and SELF repeats (P-N5-CUT §6 (iii)) do not occur under LATE′. The exceptional REPEAT′s are X′_F := those where y is not
  off-cycle for τ at some state of [k + 1, t_b] (own-cycle).
- Corollary CIRCLE′. Per W-run:
  - REP′_F ≤ n_E·R*′_T(F);
  - R*′_T(F) ≤ m_E + REP′_F;
  - REP′_F ≤ X′_F + Σ_z d_E(z)·WCH_F(z), where WCH_F(z) := the transitions of F changing W(z). For one edge, distinct REPEAT′s have
    disjoint intervals [k + 1, u − 1], so the token (edge, last change of W(z) in [k + 1, t_b − 1]) is injective;
  - WCH_F ≤ (n − 1)(R*′_T + 1) (§3).
  Hence REP′ polynomial ⟺ R*′_T polynomial ⟺ (WCH_F polynomial ∧ X′_F polynomial), up to polynomial factors.

## 5. Lemma GAP-CLIMB (PROVED, lane)
- ZXC_F(z) := the transitions s → s + 1 of F with z ∈ Z_s and Ξ_{s+1}(z) ▷ Ξ_s(z).
- Statement. Let the LATE′ adoption of (y, z) at u have last blocked state t_b (max(a, p + 1) ≤ t_b < u). Let s be the first transition of
  [t_b, u − 1] at which Ξ(z) changes. Then s exists, z ∈ Z_s, and Ξ_{s+1}(z) ▷ Ξ_s(z). Distinct LATE′ adoptions of one edge give distinct s.
  Hence, per W-run, #LATE′(y, z) ≤ ZXC_F(z) and Σ_{(y, z)} #LATE′(y, z) ≤ Σ_z d_E(z)·ZXC_F(z).
- Proof.
  - (y, z) ∉ Iσ_{t_b} (blocked) and (y, z) ∈ Iσ_u (§4 proof). LATE-RISE (R89) gives Ξ_u(z) ▷ Ξ_{t_b}(z), so s exists. Ξ is non-decreasing
    (R15), so Ξ_{s+1}(z) ▷ Ξ_s(z).
  - Ξ_s(z) = Ξ_{t_b}(z) ⊴ Ξ_{t_b}(σ_{t_b} y) ([S2]: not improving) ⊴ W_{t_b}(σ_{t_b} y) (XW) ◁ W_{t_b}(z) (blocked) ⊴ W_s(z) (W-MON). So
    Ξ_s(z) ≠ W_s(z), i.e. z ∈ Z_s.
  - For consecutive LATE′ adoptions u′ < u of one edge, t_b(u) ≥ u′ + 1 by LATE′, so the intervals [t_b, u − 1] are disjoint. □

## 6. Proposition CHAIN (PROVED, lane)
- TXC_F(z) := the transitions s of F with Ξ_{s+1}(z) ▷ Ξ_s(z) and W_{s+1}(z) = W_s(z). WZ_F(z) := the transitions of ZXC_F(z) with
  W_{s+1}(z) ≠ W_s(z).
- GXC (L-NEW box 70 §3): [Q docs/new/N5-SC-box70.md@170e5316:48-49] «A GXC EVENT is a pair (v, t) with v Even, σ_{t+1}(v) ≠ σ_t(v), τ_{t+1} =
  τ_t, λ_Ξ unchanged at t → t + 1, v ∈ Z_t, Ξ_{t+1}(v) ▷ Ξ_t(v), and W_{t+1}(v) ⊴ W_t(v).» GXC_F := those with t, t + 1 ∈ F.
- Statement. As sets of pairs (vertex, transition of F): GXC_F ⊆ TXC_F ⊆ ZXC_F, and ZXC_F(z) = TXC_F(z) ⊔ WZ_F(z) with WZ_F(z) ≤ WCH_F(z).
- Proof. GXC ⊆ TXC: on F, W-MON gives W_{t+1}(v) ⊵ W_t(v), so ⊴ is equality. TXC ⊆ ZXC: Ξ_s(z) ◁ Ξ_{s+1}(z) ⊴ W_{s+1}(z) (XW) = W_s(z),
  so z ∈ Z_s. The split is by whether W(z) changes. □
- Both inclusions can be strict: GXC also needs v Even and switching and λ_Ξ fixed; ZXC also admits climbs with a W-rise (§8 DATA).

## 7. Lemma TXC-DESCENT and Corollary TXC-RED (PROVED, lane)
- Lemma TXC-DESCENT. Let (z, s) be a TXC event of F, and x_0 = z, x_1, … z's (σ_{s+1}, σ̄_{s+1})-play. Call x TERMINAL if one of:
  - (T1) λ_Ξ(x) changes at s;
  - (T2) x Even and σ_{s+1}(x) ≠ σ_s(x);
  - (T3) x Odd and x ∈ D_s ∪ D_{s+1};
  - (T4) λ_W(x) = x.
  Let j be the least index with x_j terminal. Then j exists, x_0, …, x_j are distinct, and every (x_i, s), i ≤ j, is a TXC event. If x_j is
  T2 and λ_Ξ is unchanged at s, then (x_j, s) is a GXC event.
- Proof.
  - Let (x, s) be a TXC event with x not terminal, and c := λ_Ξ_s(x) = λ_Ξ_{s+1}(x) (not T1).
  - x ≠ c: otherwise Ξ_s(x) = Ξ_{s+1}(x) = (x, ∅, 0), with no climb.
  - Let y := σ_s(x) = σ_{s+1}(x) if x is Even (not T2), and y := τ(x) = σ̄_s(x) = σ̄_{s+1}(x) if x is Odd (not T3). Then y is x's successor
    in the (σ_t, σ̄_t)-plays and in the (σ_t, τ)-plays, for t = s and t = s + 1.
  - x is not its own Ξ-cycle node, so [V1] gives Ξ_t(x) = x ⊕ Ξ_t(y), with y's path to c avoiding x. Strict [V2] then turns
    Ξ_{s+1}(x) ▷ Ξ_s(x) into Ξ_{s+1}(y) ▷ Ξ_s(y). (If the two values had different cycle nodes, λ_Ξ(y) would change: then λ_Ξ(x) =
    λ_Ξ(y) would change too, which is T1.)
  - Likewise x ≠ λ_W(x) (not T4) gives W_t(x) = x ⊕ W_t(y). With λ_W constant on F, equality of the W(x) values gives equality of the
    W(y) values ([V2] in both directions). So (y, s) is a TXC event.
  - The x_i follow one lasso. If no terminal occurred, the descent would reach the lasso's Ξ-cycle node c with (c, s) a TXC event and
    λ_Ξ(c) = c at s and s + 1: impossible, as above. So j exists before any repetition.
  - T2 with λ_Ξ fixed: the Even x_j switches, τ_{s+1} = τ_s on F, x_j ∈ Z_s (§6), Ξ climbs, W_{s+1} = W_s. That is GXC verbatim. □
- Corollary TXC-RED. With:
  - GATE_F := the TXC events (o, s) of F with o Odd, o ∈ D_s ∪ D_{s+1};
  - CNW_F := the TXC events (x, s) of F with λ_W(x) = x;
  - LCT_F := the transitions of F at which λ_Ξ changes:
  TXC_F ≤ n·(GXC_F + GATE_F + CNW_F) + n²·LCT_F, and over a whole run Σ_F LCT_F ≤ n(n − 1).
- Proof.
  - At a transition s with λ_Ξ unchanged, every TXC event has a terminal of kind T2 (GXC), T3 (GATE) or T4 (CNW). Each terminal pair (x, s)
    serves at most n TXC events (one per starting vertex).
  - At a transition with λ_Ξ changing there are at most n TXC events.
  - Ξ is non-decreasing along the run (R15), so at each change of λ_Ξ(v) the cycle node's reward strictly increases: at most n − 1 changes
    per vertex, and each λ_Ξ-changing transition changes at least one vertex. □
- With §5 and §6: Σ LATE′_F ≤ n_E·TXC_F + Σ_z d_E(z)·WZ_F(z) ≤ n_E·[n(GXC_F + GATE_F + CNW_F) + n² LCT_F] + Σ_z d_E(z)·WZ_F(z).

## 8. READING and DATA (NOT to sign)
- READING: the descent breaks only at Odd gates (σ̄ ≠ τ) and own W-cycle nodes, never at τ-changes (τ is constant on F). The live terms are
  GATE (tied Ξ-climbs at gates) and WZ (the W-change circle at gap climbs).
- READING (for a separate check, not part of this packet): RESULTS R90's REP* and P-N5-CUT's LATE term may be read with LATE′. Box 40's
  LATE re-entries are LATE′, since σ_{j−1}(v) ≠ c forces p + 1 ≤ j − 2.
- DATA (experiments/si/odd/latep.py, txcd.py; corpus of 719 games + latew_K20_m32 + wdepth_K4_m16):
  - FW-R*′ violations 0; LATE′ adoptions that are not R88-late 0; W-silent REPEAT′ 0;
  - GAP-CLIMB violations 0, repeated tokens 0;
  - TXC descent failures 0; terminals: 13,878 gates, 292 GXC, 356 λ_Ξ changes, 0 T4 (corpus).
  - TIED-RB (TXC alone pays every REPEAT′) is DEAD: odd/inst/si51/tiedmut_so_th_n32_11 (two engines identical; Oink NOT RUN).
- Pinned checks: si/check.sh «box 51», «box 52», «box 53».

## DONE / FINDINGS / NEEDS
- DONE: draft packet (this file); line file docs/si/P-N5-LATEP-line.txt; quotes checked; si/check.sh «box 53».
- FINDINGS: the items of §0, all PROVED (lane), none refereed.
- NEEDS: Lead's GO to freeze; two referees (REFEREE-2 needs a fresh successor, Lead 05:49Z).
