# Referee report R-N5-1P: switch-best (= N5 on one-player games) is polynomial — Lemma P, Theorem PH, Corollaries 1-3

Referee: REFEREE (successor 3), Fable 5.1 (Lead reading L36). Packet P-N5-1P: the Lead's message of 2026-10-21 23:32Z. Pin: trunk
claude/vibrant-johnson-nxvvxo 26905f0; object docs/new/N5-phase-bound-box10.md §1-§4, plus the Lead's addendum of 23:42Z: the SCOPE line
and §6 (VJ00 dependencies) at trunk 0f899f3 (29 inserted lines, 0 deleted against the pin: §1-§4 are unchanged; merged here at 74a6ecc2). Context read: N5-K8-box8.md §3c-§3d, N5-K10-box8.md (Lemma F), N5-SB-box9.md, N5-ssi-global.md (SPEC S1-S5),
N5-K9-Pstrict-counter.md §5, N5-killer-box4.md §3, RESULTS R15, R-N5T.md and R-N5K9.md (my predecessor's). docs/referee-2/ was NOT read.
Source opened by me: Vöge-Jurdziński, BRICS RS-00-48, pdf sha256 485a12de432a2a8c88640b0718bd2042d855fa86d6a82092a0d538fd41ba9e65
(same file as R-N5T), §4.1-4.5, §5.1-5.6 (Lemmas 5.2, 5.5, 5.7, 5.8, 5.9, Props. 5.1, 5.3, 5.4, 5.6, 5.10), §6 (Prop. 6.1, Thm 6.2), §7
(Prop. 7.4, Claim 7.2). Written 2026-10-21 23:36Z to 2026-10-22 00:10Z by date -u (the addendum was read at 00:08Z). §5 of the object (two-player bridge) is context and is
not signed here.

## Verdict
| claim | verdict (Fable 5.1) |
|---|---|
| (V1), (V2) prefix facts | SIGN |
| (F1), (F2) | SIGN WITH GAPS: G1 (two source routes: §6's route via equation (11) in the dual is fully proved in the source and needs the order reversal of §4; the Lemma 5.8 route leans on unproved Lemma 5.9 / Prop. 5.10 and is re-derived by me in §3; DATA exhaustive) |
| Lemma P (all four cases A1, A2, B1, B2, both cycle-closing sub-cases) | SIGN WITH GAPS: G1, G2 (B1's improvement case list omits "c even, shorter"; the conclusion survives, closed) |
| Theorem PH (≤ n − 1 value-changing steps per phase, < m flat steps) and the phase count ≤ n(n − 1) + 1 | SIGN WITH GAPS: G1, G3 (stop convention and tie-break: the statement must read "any pointwise-optimal strategy of the arena"; closed) |
| Corollary 1 (O(n²·m) steps, ≤ n³ − n² + n value-changing) | SIGN WITH GAPS: G1, G3, G5 (phase-boundary accounting, closed) |
| Corollary 2 (N5 on one-player games = switch-best; fallback; < (n² − n + 1)(n + m) iterations) | SIGN WITH GAPS: G1, G4 (the fallback argument needs no Lemma P; closed), G-N1 inherited (engine = VJ00 optimum, DATA; 0 mismatches in 7,224 n5.py runs here) |
| Corollary 3 (reading of VJ00 Prop. 7.4) | SIGN as a reading: Cor. 1 gives O(n³) value-changing steps for the arena-optimum rule; the single-switch half cites K9's CDAG_n (R-N5K9, confirmed there) |
| "switch-best = N5 on one-player games" against SPEC S1-S5 | YES (§4 below): S4a/S4b are the arena optimum, S4c fires only in the all-flat situation and ends the run |
| §6 (dependency list on VJ00) and the SCOPE line (0f899f3) | SIGN WITH GAPS: the list is right for the proof (nothing beyond §4.2, §5.1 (3)-(10), Prop. 5.1, Lemma 5.2 / (11), §4.4 (2) is used; Lemmas 5.5, 5.7, 5.8 and P1/P2/I1/I2 are not), with G7 (Improve cited as §5.4 "maximising successor": it is §4.4 (2), Switch_I), G8 (the computer-check note says the fixpoint rule relies on Lemma 5.8 "2 ⇒ 1": it relies on "1 ⇒ 2", the direction whose source proof is the incomplete one), G9 (Prop. 7.4 is on printed p. 27, not p. 36) |
| Overall | SIGNED WITH GAPS G1-G9 (Fable 5.1). No step is wrong. No TARGET.md claim is involved (scope as the SCOPE line and the Lead state). |

## 1. Definitions diffed against the source
- Ω_ρ(x) = (c, P, ℓ) with c = λ(P) the most relevant vertex of the cycle, P = Prefix ∩ V_{>c}, ℓ = |Prefix|: VJ00 §4.1 verbatim (play value
  Θ(P) = (λ(P), π(P), #(P))). In a one-player game (⊖ out-degree 1) Plays_ρ(v) has one element, so Ω_ρ(v) = Θ of the ρ-play (VJ00 §4.3). ✓
- Order: reward of c first, then P by MaxDiff (B ≺ C iff MaxDiff ∈ (B∖C) ∩ R⁻ or ∈ (C∖B) ∩ R⁺), then ℓ (ℓ ∈ R⁻: longer better; ℓ ∈ R⁺: shorter
  better): VJ00 §4.2. The packet's "longer better iff c is odd" is this. Total on play values with injective priorities. ✓
- Improving edge (x, z): Ω(ρ(x)) ◁ Ω(z) (VJ00 §4.4 (2)); z = ρ(x) is never improving. ✓ The arena H_k and switch-best as in K8 §3c. ✓
- (V1): if x ≠ λ_ρ(x), Ω_ρ(x) = x ⊕ Ω_ρ(ρ(x)) and the ρ-path from ρ(x) to λ(x) avoids x. Checked: x off the cycle is visited once; x on the
  cycle (not its top) is left and not re-entered before the top. This is VJ00 (6) with "=_ℓ" sharpened to equality of sets, which holds
  because the path is simple. ✓
- (V2): with the same cycle node, x is added to both sets or to neither, the symmetric difference and the length order are unchanged;
  with different cycle nodes the prefix changes nothing. ✓ The "paths avoid x" hypothesis is needed (sets, not multisets) and is
  supplied at every use: A1 (r′ simple; (V1)), B1 (π avoids x; r′), Theorem bullet 1 (x ∉ π; (V1)). ✓

## 2. Lemma P, step by step
Base k = 0: L = 0 forces x = u, Ω_0(u) = (u, ∅, 0). ✓ (A simple path with ≥ 1 edge cannot return to x, so x ≠ u whenever L ≥ 1; used in A2, B2.)
Induction step, r = x → z → r′, |r′| ≤ k, r′ avoids x, value(r) = x ⊕ value(r′). ✓ Paths of length 0 at step k + 1: u is still its own
cycle node in the phase. ✓ Paths of length ≤ k are also covered by IH + (F2); the proof's decomposition covers them anyway. ✓
- Case A, (x, z) ∉ I_k ⇒ Ω_k(z) ⪯ Ω_k(ρ_k(x)) (total order; includes z = ρ_k(x) and forced vertices). ✓
  - A1: value(r) = x ⊕ value(r′) ⪯ x ⊕ Ω_k(ρ_k(x)) = Ω_k(x) ⪯ Ω_{k+1}(x). (V2) applies: both paths avoid x, or cycle nodes differ. ✓
  - A2: x = λ_k(x), Ω_k(x) = (x, ∅, 0), x ≠ u. x better than u: Ω_k(x) ≻ value(r), then (F2). x worse than u: Ω_k(ρ_k(x)) has cycle node x,
    value(r′) has cycle node u, so value(r′) ≻ Ω_k(ρ_k(x)), contradiction. ✓
- Case B, (x, z) ∈ I_k; ρ̂ = ρ_k[x → z] ∈ H_k; (F1) gives Ω_{k+1}(x) ⪰ val_ρ̂(x). ✓ c = λ_k(z), π = the ρ_k-path z..c.
  - B1, x ∉ π, x not on c's cycle: the ρ̂-play from x is x, π, c's cycle; val_ρ̂(x) = x ⊕ Ω_k(z) ⪰ x ⊕ value(r′) = value(r) by (V2). ✓
  - B1, x ∉ π, x on c's cycle: Z = x, π, arc(c → x) is a simple cycle (π's cycle part is the arc w → c for the first cycle vertex w of π, which
    excludes x; the arc c → x is inside c → w). P(Ω_k(ρ_k(x))) = ∅ (cycle vertices are below c). ✓ Improvement cases: (i) P(π) ≠ ∅ with even
    top e: top(Z) = e ≻ c in reward, (F1) ⇒ λ_{k+1}(x) ≠ c, phase ended, contradiction ✓; (ii) P(π) = ∅: the packet lists only "c odd, |π| longer"
    and OMITS "c even, |π| shorter than ℓ(ρ_k(x))" (a shortcut to c; possible when x ∉ π). In both (ii) cases top(Z) = c and val_ρ̂(x) =
    (c, ∅, |π| + 1) = x ⊕ Ω_k(z) ⪰ value(r). So the conclusion is unchanged. GAP G2 (wording), closed.
  - B2, x ∈ π: Z = {x} ∪ π[z..x) simple; λ_k(x) = c; the decomposition of P(Ω_k(z)) and P(Ω_k(ρ_k(x))) is right (π simple; (V1) for
    ρ_k(x) when x ≠ c; both P's empty of x when x = c), D = P(π[z..x)) ∪ ({x} if x > c) — also right for x = c. Here |π| > ℓ(ρ_k(x)) always,
    so with D = ∅ the improvement needs c odd: the packet's list is complete in B2. ✓ D ≠ ∅: top(Z) = top(D) even ≻ c, phase ends,
    contradiction ✓. D = ∅, top(Z) ≠ c: top(Z) below the odd c, reward better, phase ends ✓. D = ∅, top(Z) = c: c ∉ π[z..x), so c = x,
    val_ρ̂(x) = (x, ∅, 0) = Ω_k(x) (flat). x better than u: (F2) ✓; x worse than u: Ω_k(z) has cycle node x, value(r′) has u, contradicts IH ✓.
Nothing in the proof uses VJ00 Lemma 5.8 (2 ⇒ 1), I1 or I2 (the parts R15 records as failing at cycle nodes). It uses (F1) = Lemma 5.8
(1 ⇒ 2) on the one-player arena, see G1.

## 3. (F1): what the source proves, and my re-derivation (GAP G1)
(F1) as used: the arena optimum ρ_{k+1} of H_k satisfies Ω_{k+1} ⪰ Ω_κ pointwise for every strategy κ of H_k. This is the definition of a
maximum element of (Strategies, ⊑) (VJ00 §4.3, pointwise). Its existence is: (a) some strategy of H_k has no improvement (improvement
sequences terminate: VJ00 Lemma 5.7 plus RESULTS R15 (c), since VJ00's own I1 fails at cycle nodes); (b) VJ00 Lemma 5.8 "1 ⇒ 2"
(contrapositive: Improve(σ) = σ ⇒ σ maximum). The proof of (b) in the source (p. 20) uses Lemma 5.9 ("proved similarly to Lemma 5.5",
no proof given) and Prop. 5.10 (stated without proof). R15 (iii) records this as G-N5T-3, "not re-derived by either referee".
My re-derivation for a one-player game H (every ⊖-vertex forced; Plays(v) = all plays from v), σ with no improvement, Ξ = Ω_σ = (Λ, Π):
- Step 1, OverProg(Ξ, e) for EVERY edge e = (v, w) of H. For e ∈ E_σ (σ's edges and the forced edges), Prog(Ξ, e) holds (Prop. 5.1, from (3),
  (6), (8), (9)), and Prog implies OverProg (equalities ⇒ ⊵). For v ∈ M⊕, w ≠ σ(v): Ξ(w) ⊴ Ξ(σ(v)) (no improvement) and OverProg(Ξ, (v, σ(v))),
  so OverProg(Ξ, (v, w)) by Prop. 5.10 clause 2. Prop. 5.10 clause 2 itself: Λ(v) ⪰ Λ(σ(v)) ⪰ Λ(w); if Λ(v) = Λ(w) =: ℓ then Λ(σ(v)) = ℓ and
  Π(σ(v)) ⊵_ℓ Π(w); clause 2 (ℓ ≠ v): Π(v) ⊵_ℓ Π(σ(v)) ⊕ v ⊵_ℓ Π(w) ⊕ v because ⊕ v is monotone for ⊵_ℓ on multisets (§4.5: B ⊎ {v} ∖_M B′ ⊎ {v}
  = B ∖_M B′, both lengths + 1); clause 3 (ℓ = v): the same with ⊵̃_ℓ and Π(v) = (∅, 0) carried over. ✓
- Step 2 (Lemma 5.9 for H), for any play P from v, eventually periodic with cycle C: Λ is non-increasing along P (OverProg clause 1), so
  constant = ℓ on C and Λ(v) ⪰ ℓ. If ℓ ∉ C: clause 2 around C and monotonicity give Π(w) ⊵_ℓ Π(w) ⊕ C for w ∈ C, so not Π(w) ◁_ℓ Π(w) ⊕ C,
  and Prop. 5.6 clause 2 (proved in the source, read) gives max(C) ⊁ ℓ, hence λ(P) ≺ ℓ. If ℓ ∈ C: Prop. 5.10 clause 1 around C gives
  Π(w) ⊵̃_ℓ Π(w) ⊕ C, and Prop. 5.6 clause 1 gives max(C) ⊁ ℓ, hence λ(P) ⪯ ℓ. So λ(P) ⪯ ℓ ⪯ Λ(v). If λ(P) ≺ Λ(v): Θ(P) ◁ Ξ(v). Else
  Λ = ℓ = λ(P) on the whole of P; clause 2 along the prefix to the first visit of ℓ, with Π(ℓ) = (∅, 0), gives Π(v) ⊵_ℓ (π(P), #(P)), so
  Θ(P) ⊴ Ξ(v). ✓ With P the κ-play from v this is (F1).
- So (F1) holds for every one-player game, in particular for every arena H_k (a one-player game). (F2) follows since ρ_k ∈ H_k. ✓
Route (b), the one §6 of the addendum names, which AVOIDS Lemma 5.8 altogether: VJ00 defines Ω_σ(v) as the ⊴-minimum over ALL plays from
v consistent with σ (§4.3), and (11) Ω_σ = Θ_{σσ̄} (Prop. 5.1 from §5.1 (3), (6), (8), (9); Lemma 5.2's proved direction) says a single
positional ⊖-strategy σ̄ attains that minimum at every vertex at once: "σ̄ is a best counter-strategy against σ" (p. 16). Take the dual
H_k^d of the arena (owners swapped, priorities + 1): ⊕'s unique strategy there is the forced one, every play of H_k is consistent with it,
and the dual order is the exact reverse of H_k's (§4 below). So (11) in H_k^d yields a positional ⊕-strategy of H_k whose play value at
every vertex is the ⊴-MAXIMUM over all plays from that vertex, hence ⪰ every strategy's value: (F1), with existence included. The chain
§5.1 → Prop. 5.1 → Lemma 5.2 is proved in the source (§5.1's shortest-path existence is argued from "all cycles in G^ℓ_σ have non-negative
weight", which Prop. 5.6 gives; the closed-semi-ring Remark "left as an exercise" concerns only the algorithm). Route (b) is what N5's S4a
computes and what Lemma F of N5-K10-box8.md meant by "VJ00 §5". ✓
DATA (mine, from the definitions): L58 = "a strategy with no improving edge has the pointwise-maximal valuation over ALL strategies",
exhaustive over all strategies of every game with n ≤ 6 and ≤ 20,000 strategies: 7,945 games, 8,813 such strategies, 0 failures; F1 per
step: the chosen arena optimum dominates every arena strategy (exhaustive), 462,110 strategy comparisons, 0 failures (see §6).
G1 status: CLOSED twice over: by route (b), which is fully proved in the source and is the dependency §6 lists (so the BOUNDS of this packet
do not rest on G-N5T-3 at all), and by route (a), my dualisation of Lemma 5.5's proof above, plus the exhaustive data. Where Lemma 5.8
(1 ⇒ 2) IS still needed: only for "the valuation at a no-change stop / at I = ∅ is H's optimum", i.e. the correctness of the run's
OUTPUT (N5's S5), which is outside this packet and is R15's G-N5T-3; route (a) re-derives its one-player case. The two-player G-N5T-3
(VJ00 Lemma 5.8 for G with ⊖ choosing) is untouched and stays as R15 left it.

## 4. "switch-best = N5 on one-player games" against SPEC S1-S5 (N5-ssi-global.md)
- Game with Odd out-degree 1 everywhere: Iτ = ∅ at every iteration (S2 needs w ≠ τ(v)), so τ never moves and σ̄ = τ is forced; Ξσ (S1,
  against the optimal counterstrategy) = the one-player valuation Ω_σ of H = G; Iσ = VJ00's improving edges of H. ✓
- S4a: arena H with Even v restricted to {σ(v)} ∪ Iσ(v), Odd fixed; σ_new = the S1 counterstrategy in the dual of H to τ. The dual (owners
  swapped, priorities + 1, ranks unchanged: SPEC A3) has exactly the reversed order on play values: rewards reverse (parities flip, relevance
  kept), the MaxDiff rule reverses, and the length rule reverses (c odd in G is even in G^d). So the dual's best counterstrategy (the
  pointwise MIN of the dual order, VJ00 (11)) is the pointwise MAX of G's order over the arena: a switch-best step, as the packet says. ✓
  The identification rests on the S1 procedure computing VJ00's σ̄ (VJ00 §6, Prop. 6.1 / Thm 6.2; the fleet's G-N1 = G-N5T-1, DATA). My
  check (§6, mode n5): n5.py's loop UNMODIFIED, every iteration's σ_{k+1} lies in the arena of σ_k and has the exhaustive arena-optimum
  valuation, or is the S4c fallback: 7,224 runs, 0 failures; the engine's Ξσ = my valuation at every evaluated σ: 0 mismatches.
- The mirrored case (Even out-degree 1, Odd moves) is S4b with G^d's valuation: the same statement with the roles swapped. ✓
- S4c (fallback) and the no-change optimum: GAP G4. The packet says the fallback fires "only in the value-flat situation ... by the
  Theorem's argument"; the Theorem's argument is for k ≥ n − 1, but the fact holds at EVERY k and needs no Lemma P: if the arena optimum
  returns σ itself, (F1) gives val_{σ[x→z]}(x) ⪯ Ω(x) for every improving (x, z); if z's path avoids x this contradicts strict (V2) (x not its
  own cycle node) or gives a better cycle node (x its own cycle node); if it passes x, the B2 analysis (which uses only the improvement
  condition) gives a better cycle node unless top(Z) = c = x, the flat case. So every improving edge is a flat cycle-closer at its own cycle
  node. The fallback switches each such x to its Ω-best improving successor; the switched vertices are distinct cycle nodes, no path from a
  z_x to x passes another cycle node (it would make x's cycle node that other node), so the combined switch is flat and I(x) = ∅ afterwards:
  the run stops at the next S5 test. ✓ (DATA: NC in §6, 1,398 no-change events, 0 failures.) Closed, wording.
- Iteration count: one N5 iteration = one switch-best step (S4a) or one fallback (flat, terminal). So N5's iterations ≤ the Theorem's bound. ✓

## 5. Theorem PH, phase count, Corollaries 1-3
- Phase count: λ_{k+1}(x) ≠ λ_k(x) with Ω_{k+1}(x) ⪰ Ω_k(x) forces a strictly better reward (injective priorities), so ≤ n − 1 changes per
  vertex, ≤ n(n − 1) + 1 phases. ✓
- After n − 1 in-phase steps, Lemma P covers every simple path (≤ n − 1 edges); c = λ(z) is a cycle node of ρ_0 (the set of cycle nodes is
  the image of λ, unchanged in the phase). ✓ Bullet 1 (x ∉ π, x off c's cycle): (V1) + strict (V2) contradict the improvement; the extra
  condition "x off c's cycle" is not needed for this bullet (the same argument works for x on the cycle, x ∉ π) but is harmless since the
  second bullet covers it via B1. ✓ Bullet 2: the B1/B2 analysis at k = n − 1 gives λ-changing, or (B1 (ii)) x ⊕ Ω(z) ≻ Ω(x) against Lemma P
  (contradiction), or flat with top(Z) = x. ✓ (G2 applies to B1 (ii) here too: both P(π) = ∅ sub-cases give val_ρ̂(x) = x ⊕ Ω(z); closed.)
- Flat regime: when every improving edge is flat, EVERY arena strategy has the same valuation (the argument of G4 for combined flat
  switches), so the step is value-flat whatever optimum the engine returns, and Lemma P's conclusion persists (same Ω); each flat step that
  changes the strategy strictly raises Ω(ρ(x)) at a switched x among x's fixed successor values, at most deg(x) − 1 times: < m flat steps. ✓
  GAP G3: the Theorem counts "steps" of "the optimal strategy of the arena", which is not unique. The claims hold for ANY pointwise-optimal
  choice (the proof uses only (F1)/(F2)), but a run needs the convention that a step returning ρ_k itself stops it (lemmaP_check.py: break;
  N5: the fallback, which then stops). The valuation at such a stop is optimal (applying all flat switches gives a strategy with I = ∅ and
  the same valuation; VJ00 "no improvement ⇒ maximum" = Lemma 5.8 (1 ⇒ 2), re-derived for one-player games in §3 route (a); this is
  the output-correctness fact, not a step count, and the packet's bounds do not need it). The step COUNTS depend on the tie-break (G6).
  Closed by this reading; the statement should say "any pointwise-optimal strategy" and name the stop rule.
- Corollary 1 arithmetic (GAP G5, closed): the λ-changing steps lie between phases (Lemma P's phase is ρ_0..ρ_k with k in-phase steps).
  With Φ ≤ n² − n + 1 phases, ≤ n + m − 1 steps each and Φ − 1 boundary steps: ≤ Φ(n + m) − 1 < (n² − n + 1)(n + m) ✓; value-changing
  ≤ Φ(n − 1) + Φ − 1 = n³ − n² + n − 1 ≤ n³ − n² + n ✓ (the packet's bound is right and slightly loose). O(n²·m). ✓
- Corollary 2: §4. ✓ "Closes K8's constant case for every G_c": inside a τ_k = c stretch Even's N5 moves are switch-best on the one-player
  game G_c (R-N5K9 Step 1, confirmed there), so the per-stretch count is bounded by Cor. 1 with G_c's n, m. ✓ (This bounds a stretch, not
  N5's run: the number of stretches is the open part, as the packet says.)
- Corollary 3: VJ00 Prop. 7.4 (p. 27) states O(n³) for one-player games with no proof and no named rule (read by me; L-LIT T22). Cor. 1 gives
  O(n³) VALUE-CHANGING steps for the arena-optimum rule and O(n²·m) with flat steps; the "false for arbitrary single switches" half is
  K9's CDAG_n (R-N5K9 and REFEREE-2 confirmed a 183-step chain at n = 10). As a reading, ✓. It is not a claim that VJ00 meant this rule.

## 6. Computer checks (docs/referee/scratch/n5_1p_probe.py, written from the definitions: plays simulated, §4.2 order coded directly;
no si.py; n5.py only as the object under test in mode n5)
Per switch-best step the arena is enumerated exhaustively (≤ 20,000 strategies, else switch-all SI inside the arena, which agreed with the
exhaustive optimum in every case where both ran: SIvsEXH 0). Tie-break among optimal strategies: rand / keep (prefer ρ_k, maximises no-change
events) / far (maximal switching). Checks: F1X (a pointwise maximum exists), F1, F2, LP (Lemma P for every cycle node of ρ_0, every x, every
simple path of ≤ k edges, DFS table), PH (no value-changing step at in-phase index ≥ n − 1; value-changing ≤ n − 1; flat ≤ m − n; steps < n + m),
PC (phases ≤ n² − n + 1; steps < (n² − n + 1)(n + m); value-changing ≤ n³ − n² + n), NC (no-change optimum ⇒ all improving edges flat
cycle-closers; fallback flat and I = ∅ after), L58 (§3), N5 (§4). Random one-player games as the packet generates them (Odd with prob. 1/4,
out-degree 1; Even out-degree ≤ 4; injective priorities); 2 random starts per game.
| run | games (n) | runs | steps | F1 comparisons | LP checks | NC events | violations (all checks) |
|---|---|---|---|---|---|---|---|
| rand, seed 11 | 3,000 (≤ 7) | 6,000 | 6,124 | 38,736 | 4,687 | 298 | 0 |
| keep + n5, seed 12 | 3,000 (≤ 7) | 6,000 | 6,370 | 78,287 | 5,471 | 881 | 0 (n5.py: 5,915 iterations, 282 fallbacks, 0 mismatches) |
| far, seed 13 | 3,000 (≤ 7) | 6,000 | 5,978 | 38,815 | 4,065 | 0 | 0 |
| rand, seed 14 | 1,000 (≤ 9) | 2,000 | 2,289 | 23,156 | 1,925 | 109 | 0 |
| keep + n5, seed 15 | 300 (≤ 12) | 600 | 856 | 29,321 | 958 | 108 | 0 (n5.py 781 it., 20 fb) |
| far + n5, seed 16 | 300 (≤ 12) | 600 | 828 | 46,156 | 575 | 0 | 0 (n5.py 828 it., 22 fb) |
| packet instances, keep + n5 | 12 (10-24) | 12 | 166 | 125,022 | 10,168 | 2 | 0 (n5.py 166 it.) |
| packet instances, far + n5 | 6 (10-16) | 6 | 76 | 53,966 | 3,109 | 0 | 0 (n5.py 77 it.) |
| packet instances n = 32-64, rand + n5 (LP skipped: table exponential) | 6 | 6 | 195 | 28,651 | — | 0 | 0 (n5.py 195 it.) |
Instances (sha1 as in experiments/new/tail/box10_instances.sha1): phase/rel_g12 (20db1b22…), rel_g16 (c3dfe417…), fl_n16, ph_n16, ph_g16,
fl_g16, fl_r24, ph_r24, rel_g24, ph_n48 (bae0aba3…), ph_g48, fl_r32, fl_r48, ph_r64; sb1p/sb1_counter_n10 (755099c5…), n16 (6babed79…), n48;
sb1p/sb2_fail. Longest in-phase value-changing count seen: 45 at n = 48 (ph_n48, rand), 20 at n = 24 (rel_g24, keep), 14 at n = 16; all
≤ n − 1. Totals: F1 462,110 comparisons, LP 30,958 checks, NC 1,398 events, L58 7,945 games / 8,813 improvement-free strategies, all 0.
Honesty note: my first version had both signs of the MaxDiff rule reversed; the switch-all loop inside the arena then CYCLED (a wrong order
breaks VJ00 Lemma 5.7), which is how I found it. Nothing was recorded before the fix.
Packet scripts re-run by me (unmodified): lemmaP_check.py inst rel_g12 rel_g16 fl_n16: 2,402 checks, 0 violations, longest phase 14 at n = 16;
lemmaP_check.py 300 5 8: 343 checks, 0; f1_check.py 300 5 10: 703 steps, 17,286 checks, 0. phase_vc.py: rel_g12 (11, 11) at n = 12,
rel_g16 (15, 15) at n = 16, rel_g24 (21, 21) at n = 24. CORRECTION (§C, from REFEREE-2's N-2): phase_vc.py counts the λ-changing step that
closes a phase inside it, so rel_g16's 15 is 14 in-phase + 1 closing (my own probe's 14 at n = 16 above is the in-phase count) and only
rel_g12 (one phase, no closing step) attains n − 1 in-phase, for the packet's sbstep rule.
GAP G6 (DATA note, not a claim): the tight count is tie-break dependent. On rel_g12 from the committed .start, sbstep takes 11 steps in one
phase (all value-changing); n5.py, the actual N5 engine, takes 10 iterations; my 'keep' optimum 10 and 'far' 9. So "N5 attains n − 1 per
phase" is shown for the packet's switch-all-in-the-arena engine, not for n5.py's VJ00-procedure engine. Also tail/logs/phase_vc.txt line 12
reports rel_g12 as steps=14 phases=5 (max phase (11, 11)), while the committed instance + .start give steps=11 phases=1 (max (11, 11)):
a stale log line (rel_g16's line reproduces exactly). L-NEW may want to re-log it.

## 7. Gap list
| id | where | what | status |
|---|---|---|---|
| G1 | (F1), used in Lemma P Case B, (F2), Theorem PH | the packet's citation "VJ00 §5; Lemma F" was unspecific; the Lemma 5.8 (1 ⇒ 2) route rests on Lemma 5.9 ("similarly") and Prop. 5.10 (unproved) = fleet gap G-N5T-3; the (11)-in-the-dual route (§6 of the addendum) is fully proved in the source but needs the order reversal under dualisation stated | CLOSED: route (b) + my §4 reversal; independently route (a) by my dual reading (§3); exhaustive DATA; the bounds do not depend on G-N5T-3; the two-player G-N5T-3 is untouched |
| G2 | Lemma P, B1 second sub-case | improvement case list omits "P(π) = ∅, c even, π shorter than the cycle arc"; same conclusion | CLOSED (wording; the Theorem's bullet 2 inherits the fix) |
| G3 | Theorem PH, Cor. 1 | "the optimal strategy" is not unique; stop rule for a no-change optimum unstated; counts tie-break dependent | CLOSED by reading: holds for any pointwise-optimal choice with the stop/fallback rule |
| G4 | Cor. 2 | "by the Theorem's argument" for the fallback: needs no Lemma P, holds at every k | CLOSED (argument in §4) |
| G5 | Cor. 1 | boundary (λ-changing) steps are outside phases; arithmetic re-done | CLOSED (bounds as stated hold) |
| G6 | §3 Tightness, §4 DATA | n − 1 attained for the sbstep engine; n5.py takes 10 on rel_g12; log line 12 of phase_vc.txt stale | NOTE (DATA), nothing to prove; the addendum's §6 now records the 11-vs-10 difference itself |
| G7 | §6 (0f899f3), "Improving edges" bullet | cites "§5.4, Improve(σ)(v) = a successor maximising Ω_σ (p. 17)"; VJ00's improvement is §4.4 eq. (2) (p. 11), Improve = Switch_I for ANY non-empty set of improvements, not the maximising successor; the proof uses only I_k(x) = {z : Ω_k(z) ≻ Ω_k(ρ_k(x))}, which is (2) | OPEN (citation wording, L-NEW to fix; nothing in the proof changes) |
| G8 | §6, "Rule used by the computer checks" | "relies on Lemma 5.8 '2 ⇒ 1'": the switch-all fixpoint rule is sound iff "Improve(σ) = σ ⇒ σ maximum" = Lemma 5.8 "1 ⇒ 2" (VJ00's numbering: 1 = not maximum, 2 = Improve(σ) ≠ σ); "2 ⇒ 1" is the direction R15 found to fail, and the fixpoint rule does not use it. My probe needs neither: the arena optimum is enumerated, and the fixpoint rule agreed with it in every case (SIvsEXH 0) | OPEN (numbering slip, L-NEW to fix; the EXACT=1 re-run the Lead reports makes the lane's own checks independent of it) |
| G9 | §6, Prop. 7.4 | "p. 36": the statement is on printed p. 27 of BRICS RS-00-48 (pdf of 34 pages) | OPEN (citation, L-NEW to fix) |
Inherited, outside the packet: G-N1 (engine computes VJ00's Ωσ / arena optimum: DATA, +7,224 runs here with 0 mismatches), G-N5T-3
(output correctness at the stop; two-player form untouched, one-player form re-derived in §3 route (a)). The §6 claim "Lemma 5.8 and
postulates I1/I2 are NOT used" is right for the bounds signed here (checked use by use: Lemma P uses (V1) = (6)/(8), (V2), (F1) by route
(b), (F2); Theorem PH and the corollaries add only the order, the definitions and SPEC S4). What the addendum's §6 does not state and the
proof needs: that dualisation reverses the order exactly (my §4) and that (11) is a statement about all plays, not only positional
strategies (VJ00 §4.3), which is what makes the dual's σ̄ dominate every arena strategy. The claim "N5 is polynomial on one-player games" is signed; it is not a TARGET.md claim (one-player parity games are
polynomial by other means), as the Lead's packet says.

## C. Comparison with REFEREE-2 (docs/referee-2/R2-N5-1P.md, referee-2 f954070, read after my report was pushed at dfa87d0d; written
2026-10-22 00:20Z-00:40Z by date -u; trunk 12617fc merged)
Verdicts, claim by claim: identical in every row. (V1)/(V2) SIGN both. (F1)/(F2) SIGN WITH GAPS both (my G1 = their G-1P-4). Lemma P:
R2 SIGN with the wording gap G-1P-1, I SIGN WITH GAPS G1/G2; G2 = G-1P-1 exactly (the B1 "c even, shorter" case; both note B2's list is
complete because z's path is strictly longer). Theorem PH SIGN WITH GAPS both. Corollary 1: R2 SIGN with nit N-1, I SIGN WITH GAPS G5; N-1 = G5
(λ-changing steps lie in no phase; both re-did the arithmetic and get the same bounds; R2 observes the box's n³ − n² + n is the count WITH
the closing steps). Corollary 2 SIGN WITH GAPS both (G-1P-5 = my G4; G-1P-6 = G-N1 inherited). Corollary 3 SIGN as a reading / remark, both,
no attribution. "Switch-best = N5 on one-player games": YES both, by the same order-reversal argument (R2 §2 (i), my §4). Scope statements
agree. No disagreement on any verdict.
Joint gap list (mine ↔ theirs):
| mine | theirs | status after comparison |
|---|---|---|
| G1 ((F1) source) | G-1P-4 | CLOSED by two independent derivations. R2's: (11) in the dual, with the "⊵" halves of VJ00 (4) and (6) re-derived because the source ASSERTS them (R2 §2 (ii)). I ACCEPT this sharpening and withdraw my §3 sentence "the chain §5.1 → Prop. 5.1 → Lemma 5.2 is proved in the source": Lemma 5.2 is, (4)/(6) are not in full. My route (a) (dual of Lemma 5.5, §3) does not need (4)/(6): in the arena ⊕ chooses and ⊖ is forced, so Ω_σ is a single play's value and Prog along σ's edges is play-following; it needs Prop. 5.6 (proved) and Prop. 5.10 (verified by me). Two different proofs, same conclusion, exhaustive data on both sides |
| G2 | G-1P-1 | CLOSED, same finding, same fix (one clause) |
| G3 | G-1P-3 | CLOSED, same finding; R2's formulation is sharper: a deterministic optimum returning ρ_k is STUCK, not "stopped with I = ∅"; counts are of strategy-changing steps plus one terminal stuck/fallback event. I ACCEPT that wording |
| (inside my G4 and §5 "flat regime") | G-1P-2 | CLOSED; R2 lists as its own gap the line "the return path of z_x to x contains no other switched vertex" that Theorem PH's step n and S4c both need. My report has the argument (§4, G4) but did not list it under Theorem PH; I ACCEPT it as a separate gap, closed |
| G4 | G-1P-5 | CLOSED, same finding (the fallback needs no Lemma P and fires at any step) |
| G5 | N-1 | CLOSED, same arithmetic |
| G6 | N-3 | DATA note, same finding (sbstep vs n5.py tie-breaks: rel_g12 11 / 10; both referees' tie-breaks 10 / 10 / 9); R2 adds the method point that every one of the lane's switch-best numbers should name its rule |
| — (my §6 took phase_vc's (15, 15) at face value) | N-2 | ACCEPTED, my §6 corrected above: phase_vc.py counts the closing step; in-phase tightness n − 1 is attained at n = 12 only (rel_g12), rel_g16 is 14 + 1, ph_n48 is 45 + 1. No bound affected |
| (LP skipped above n = 24 in my probe) | G-1P-7 | DATA scope, now REDUCED (see below): Lemma P checked on n5.py's own ph_n48 sequence, all three phases including the 45-step one, for every simple path of ≤ 16 edges at every step: 24,987 checks, 0 violations; longer paths: see the line below |
| G7-G9 (addendum §6 citations) | — | R2's report is on the pin 26905f0 and does not cover the addendum §6 (0f899f3); these stay mine, OPEN for L-NEW |
| inherited G-N1 | G-1P-6 | DATA, both sides (R2: 34,601 iterations, 11,479 optima, 522 fallbacks; me: 7,224 runs), 0 mismatches |
G-1P-7 (Lemma P on ph_n48's 45-step phase), what I did: docs/referee/scratch/n5_1p_ph48.py replays n5.py's loop unmodified on ph_n48 from
its .start (47 iterations, 0 fallbacks, phases of 0 / 45 / 0 in-phase value-changing steps, as R2 and the box report) and checks Lemma P at
every step of every phase over all simple paths of ≤ LMAX edges (exhaustive DFS up to that length): LMAX = 8: 13,325 checks; 11: 18,078;
16: 24,987 (30 s); all 0 violations. LMAX = 24 and the full 47: still running at this push (started 00:22Z, 1,500 s cap each); their outcome goes in a follow-up commit. Paths longer than the largest finished LMAX remain unchecked; the proof
does not depend on it (R2 and I agree).
Disagreements: none. Two self-corrections on my side, both accepted from R2: the (4)/(6) point in G1 and the N-2 count. One addition on my
side R2 does not have: route (a) for (F1) (§3), which avoids both Lemma 5.8 and the asserted halves of (4)/(6), and the addendum §6 slips
G7-G9. Joint picture: the packet's §1-§4 and §6 are signed by both referees with the same gaps, all closed as wording or by derivation,
except the DATA notes (tie-break, N-2, G-1P-7 partial) and the citation slips G7-G9 for L-NEW.
