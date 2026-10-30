# R-N5-GAP: REFEREE report on packet P-N5-GAP (L-NEW box 69): the gap set {Ξ ≠ W} at in-phase fallbacks; FB-LIN as a reduction
Referee: REFEREE (successor 19), Opus 5.5 (owner ruling D15). Lead brief 2026-10-30 01:22Z (date -u). REFEREE-2 successor 21 reviews in parallel.
- Object and pin: docs/new/P-N5-GAP-box69.md at claude/l-new 28ceeadc, `git show 28ceeadc:docs/new/P-N5-GAP-box69.md | sha1sum` =
  d67f8e04b54d5621ebecf27e7fe7151ce57793cd (175 lines), unchanged at origin/claude/l-new head; RESULTS line docs/new/P-N5-GAP-box69-line.txt at
  l-new 901f242d, sha1 f1c5c5d5f4ec824da68df6b56a0b60322fe1b0ec. Both equal the Lead's figures. Fixes go to an append-only fixes file on l-new.
- Runs 2026-10-30T01:50Z-01:53Z; report written 01:54Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independence: no docs/referee-2/ file opened. The packet's OPT-OFF (§2.4) is checked on ITS OWN text (Lead 01:22Z), not through my
  P-N5-CUT review of L-SI's OPT-OFF.
- Premises opened: SPEC at da3fa7fa (the 6 [Q SPEC] quotes: 6/6 verbatim by my script); RESULTS R15 (a), (d), R17 (a) (F1), R21 (a), R38 (a),
  R56, R88, R89 (the 3 RESULTS quotes verbatim); R17's object docs/new/N5-phase-bound-box10.md at da3fa7fa ([⊕], [V1], [V2]: verbatim).
- Scope (D1): a REDUCTION of CONJECTURE FB-LIN (in-phase fallbacks per phase) to Σ_v WCH^S4a_P(v) and ZF_P, neither bounded. FB-LIN and
  G-N5-TIME stay OPEN. Not a TARGET.md claim, not M3, not a step-4 pass.

## Verdicts
| § | item | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| 1 | setting, quotes, definitions (phase, in-phase, τ-fixed Even fallback, piece, BLOCKED, Z_t, WCH^S4a) | CHECKED (the in-phase dichotomy re-derived) |
| 2.1 | Lemma XW | SIGNED; standing premise GAP-N1 |
| 2.2 | Lemma W-MON | SIGNED |
| 2.3 | Lemma FB-W | SIGNED |
| 2.4 | Lemma OPT-OFF | STATEMENT TRUE; PROOF HAS A HOLE (G-GAP-1, Case 2 (ii) when c's ρ-play meets v's cycle node u before v); SIGNED WITH MY REPAIR GAP-R1 (§2), to go into the fixes file |
| 2.5 | Lemma W-SUCC | SIGNED (given OPT-OFF as repaired) |
| 3.1 | Lemma LATE-W | SIGNED (given OPT-OFF as repaired) |
| 3.2 | Corollary LATE-PIECE | SIGNED |
| 4.1 | Lemma GAP-MON | SIGNED |
| 4.2 | Lemma SW-IN | SIGNED |
| 4.3 | Lemma Z-FLAT (a)-(d) | SIGNED (consequences, not a characterisation: GAP-N3) |
| 4.4 | Lemma REOPEN-W, Corollary REOPEN-CHARGE | SIGNED |
| 5 | Theorem GAP-RED | SIGNED (it uses OPT-OFF nowhere: XW, W-MON, FB-W, GAP-MON, REOPEN-W, [R15] only) |
| 6 | DEAD, DATA, READING | not signed; pinned blocks «box 66», «box 67», «box 68» reproduced (§7) |
| — | RESULTS line (901f242d) | MATCHES §2-§5 and claims nothing more, after three small additions (§8: GAP-L1..L3); no E-item |
One gap (G-GAP-1), in a proof, with a repair; the statement is true and nothing FALSE is claimed. Theorem GAP-RED does not depend on the gap.

## 1. Setting
- In-phase dichotomy ✓: both states in one phase ⇒ τ_{t+1} = τ_t ⇒ σ changes (R15 (d)); a non-fallback σ-change is S4a's σ_new (S4d), a
  fallback with τ kept is S4c's Even branch (the Odd branch changes τ). Data: 0 in-phase transitions outside the two (INPHASE).

## 2. Carried lemmas and OPT-OFF
- XW ✓: σ̄_t is Odd's pointwise optimum against σ_t ([S1-Xi]); τ_t is a positional Odd strategy; so Ξ_t = val(σ_t, σ̄_t) ⊴ val(σ_t, τ_t). That
  S1's procedure does realise Ξ as the values of σ̄_t's plays is the standing premise RESULTS R57 (a) (VJ) / R21 (a) (GAP-N1; the packet cites
  R21 (a), whose proof it rightly calls game-general).
- W-MON ✓ (H_t one-player, σ_t ⊆ H_t, plays of H_t and G_{τ_t} agree for strategies inside H_t, [F1]). FB-W ✓: S4c fires only if σ_new =
  σ_k, and σ_new is S1's optimum of H_k, so σ_k is optimal in H_k; σ_{k+1} uses only edges of H_k (S4c picks from Iσ_k); τ_{k+1} = τ_k; [F1].
- OPT-OFF. Case 1 ✓ ([V1] at v; [V2] strict; [F1]). Case 2, ρ-play from c visits v, π := its part before the first v, u := v's cycle node.
  Two sub-cases, which the packet does not separate:
  - (2a) u ∉ π. Then c's play is π, v, then v's play: Ω_ρ(c) = (u, P(ρ v) ⊔ S, ℓ(ρ v) + |π| + 1), S := {y ∈ π ∪ {v} : y above u}; Z = v, π
    does not contain u. The packet's (i) and (ii) are correct here (in (ii) all of Z is below u). ✓
  - (2b) u ∈ π. This happens exactly when v lies on the cycle of its own play and c's play enters that cycle between v and u (e.g. (v, u)
    itself an edge of H, c = u). Then P(ρ v) = ∅ (ρ v runs along the cycle to u, all of whose vertices are below u), Ω_ρ(c) = (u, S′, ℓ_c)
    with S′ := the vertices of π before u that are above u, and ℓ_c := the index of u in π — NOT ℓ(ρ v) + |π| + 1. The ρ′-cycle Z = v, π
    CONTAINS u. (i) S′ ≠ ∅: max S′ is Z's top, the packet's argument works. (ii) S′ = ∅: the packet says "longer wins, so u is odd. Every
    vertex of Z is less relevant than u" — both steps fail: the lengths are ℓ_c vs ℓ(ρ v) with no fixed order, and u ∈ Z. G-GAP-1.
  - Data: sub-case (2b) occurs 11,948 times among the 436,677 checked (v, c) pairs on my corpus, (2b) with S′ = ∅ 11,781 times; the
    lemma's conclusion holds in all of them (OPT 0 violations). So the statement survives; the proof is incomplete.
  - REPAIR GAP-R1 (case (2b)(ii), S′ = ∅): then Z's top is u, so the ρ′-play from v has cycle node u; it is v, c, …, u with no vertex above u
    before u, so Ω_ρ′(v) = (u, ∅, 1 + ℓ_c) = v ⊕ Ω_ρ(c) as triples (v is below u, so ⊕ adds no vertex). Also Ω_ρ(v) = (u, ∅, 1 + ℓ(ρ v)) =
    v ⊕ Ω_ρ(ρ v) ([V1]). Both triples have cycle node u and v ∉ their P, so ⊕ preserves the strict order (the formal content of [V2]: the
    same term is added to both signed weights, 1 to both lengths): Ω_ρ(c) ▷ Ω_ρ(ρ v) gives Ω_ρ′(v) ▷ Ω_ρ(v), against [F1]. □ (This is the
    argument of Case 3 in L-SI's independent OPT-OFF (ii), P-N5-CUT §2, which I signed in R-N5-CUT §2; here it is applied to L-NEW's text.)
- W-SUCC ✓ (one piece, τ fixed; OPT-OFF in H_t at t + 1 with ρ = σ_{t+1}, (v, σ_t v) ∈ σ_t ⊆ H_t; W-MON).

## 3. LATE-W, LATE-PIECE
- LATE-W ✓: W_{t′}(c) ▷ W_{t′}(σ_{t′} v) (blocked) ⊵ W_{s+1}(σ_{s+1} v) (W-SUCC on [s + 1, t′], states of Q) ⊵ W_{s+1}(c) (OPT-OFF in H_s with ρ =
  σ_{s+1}, (v, c) = (v, σ_s v) ∈ H_s, v off-cycle at s + 1). Strict. ✓ MUT 4 (off-cycle premise dropped): 10 violations (bites).
- LATE-PIECE ✓: for i ≥ 2 a leave of c lies in (u_{i−1}, u_i) (σ_{u_{i−1}+1} v = c ≠ σ_{u_i} v, both states in Q), so the latest leave s_i ≥
  u_{i−1} + 1 and the windows [s_i + 1, t′_i] ⊆ (u_{i−1}, u_i] are disjoint; off-cycle windows get a W(c)-change at t ∈ [s_i + 1, t′_i − 1]
  (LATE-W), the others are in CL; the first counts 1. ✓

## 4. Gap set
- GAP-MON ✓: v ∉ Z_k: W_{k+1}(v) ⊴ W_k(v) (FB-W) = Ξ_k(v) ⊴ Ξ_{k+1}(v) (R15 (a), (d): the fallback is Switch_I with one improving edge per
  vertex, an unambiguous I) ⊴ W_{k+1}(v) (XW): all equal.
- SW-IN ✓: b := Ξ_{k+1}(w) ⊵ Ξ_k(w) ▷ Ξ_k(σ_k v) =: a; [V1] at k and at k + 1 (v off its own Ξ-cycle at both) writes Ξ(v) = v ⊕ (successor's
  value) with v ∉ either P and v not either cycle node; ⊕ is strictly monotone on such triples ([V2]); GAP-MON's contrapositive puts v in Z_k.
  MUT 1 (own-cycle exclusion dropped): 36 violations (bites).
- Z-FLAT ✓ (each item is the cited lemma; (d) is the definition Z_{k+1} = Z_k). GAP-N3: the title "characterisation" is a list of
  consequences; nothing is claimed in the converse direction.
- REOPEN-W ✓: in-phase ⇒ τ kept ⇒ W-MON and [R15]; W_{k+1}(v) = W_k(v) would give Ξ_{k+1}(v) ⊵ Ξ_k(v) = W_k(v) = W_{k+1}(v) ⊵ Ξ_{k+1}(v) (XW),
  v ∉ Z_{k+1}. MUT 2 (the same at τ-changing S4a steps, W in the new frame): 0 violations in 4,401 checks: the in-phase premise is used by the proof (W-MON needs τ kept) but its necessity is not exhibited. REOPEN-CHARGE ✓ (one W(v)-change per counted pair).

## 5. GAP-RED
✓. Along the in-phase transitions of P, |Z| starts at |Z_a| ≤ n, stays ≥ 0, drops by ≥ 1 at a non-Z-flat in-phase fallback (GAP-MON: Z_{k+1}
⊊ Z_k), is unchanged at a Z-flat one, and grows by ≤ |Z_{k+1} ∖ Z_k| at an S4a step (it may also drop there). So #(non-Z-flat fallbacks) ≤
|Z_a| + RO_P, and f_P ≤ |Z_a| + RO_P + ZF_P ≤ n + Σ_v WCH^S4a_P(v) + ZF_P (REOPEN-CHARGE). MUT 5 (ZF_P dropped): 33 violations (bites; ZF_P is needed). MUT 3 (GAP-MON
claimed at S4a steps): 3,375 violations (the gap set does grow at S4a steps, as REOPEN-W says).

## 6. Notes (for the fixes file; GAP-R1 is required, the rest are not)
- G-GAP-1 / GAP-R1: §2 above. The fixes file should state Case 2 as (2a) u ∉ π (the packet's text) and (2b) u ∈ π (GAP-R1), and drop "Ω_ρ(c)
  is |π| + 1 longer" for (2b).
- GAP-N1 (standing premise): XW and FB-W / W-MON rest on S1's procedure returning a pointwise optimum that realises Ξ (R57 (a) (VJ), R17 (a)
  (F1)); the packet names [F1] and R21 (a), not R57 (a); G-N5T-1 (code = SPEC) for DATA.
- GAP-N2: [V2] is quoted for "values whose paths both avoid x"; SW-IN applies it to values of two DIFFERENT strategy pairs (states k and k + 1).
  The formal triple statement covers this (v ∉ P, v not the cycle node); worth one sentence.
- GAP-N3: Z-FLAT is a list of consequences, not a characterisation.

## 7. Pinned checks and data
- Pinned: experiments/new/check.sh l. 315-332 («box 66», «box 67», «box 68») run alone in a clean `git worktree add --detach` at 28ceeadc: three
  PASS lines, exit 0.
- Own control docs/referee/scratch/gap_probe.py (rl_engine; no lane code) on the lane's corpus (experiments/si/root/logs/alt_all.lst, 413
  games with starts, + fb38_n48, pl130_n40, long121_n40; both the given start and the S3 start): 394 games with n ≤ 140 (22 larger skipped), 481 runs, 11,064 transitions: 0 violations of XW (493,493 vertex checks), FBW and
  GAP-MON (948 τ-fixed Even fallbacks), SW-IN (2,945), Z-FLAT (74 Z-flat fallbacks; most in one phase 10), REOPEN-W (9,050 re-openings, every
  one with a W-rise), GAP-RED (2,624 phases; most in-phase fallbacks in one phase 38), OPT-OFF (436,677 (v, c) pairs, at S4a steps with ρ =
  σ_{t+1} and at Even fallbacks with ρ = σ_k), LATE-W (1,075), LATE-PIECE (1,918 (piece, edge) checks; most re-blocked adoptions 2).
  MUT 1 / 3 / 4 / 5 bite (36 / 3,375 / 10 / 33); MUT 2 does not (§4).
- Pins: nep22f_n64 (given start): 10 Z-flat in-phase fallbacks in one phase (lane 10); lend9_n8: 3 in-phase fallbacks; b6_xl2_n32: one
  re-blocked late adoption per piece and edge (LP_max 1, lane max-per-piece-edge 1).

## 8. RESULTS line (901f242d), symbol by symbol
| symbol | where | status |
| --- | --- | --- |
| N5, SPEC S1-S5 | IN | ✓ |
| W_t | IN | ✓ |
| Ξ_t | SPEC S1 (Ξσ) | GAP-L1: add "Ξ_t := Ξ_{σ_t} (SPEC S1)" |
| Z_t | IN | ✓ |
| phase, in-phase | IN (R38 (a)) | ✓ |
| τ-fixed Even fallback | IN | ✓ (τ kept follows from S4c; fine) |
| piece | IN | ✓ |
| blocked | IN (R88) | ✓ |
| S4a step, "read with τ_t" | SPEC S4a | ✓ (W^{τ_t}; the line's "read with τ_t" carries the frame) |
| one-player game, optimal ρ, Ω_ρ | MISSING in part | GAP-L2: "a one-player game of Even (Odd fixed), ρ a pointwise-optimal Even strategy (R17 (a) (F1)), Ω_ρ its [S1-val] valuation" |
| own W- / Ξ- / Ω_ρ-cycle node | IN (by use) | ✓ |
| leave, late adoption, re-blocked | IN | ✓ (the line's paraphrase matches §3.2) |
| WCH_Q(c), CL_Q(v, c) | IN | ✓; the line drops "other than the first" from CL: a superset, the bound stays true |
| f_P, RO_P, WCH^S4a_P(v), ZF_P, |Z_a|, n | IN | ✓ |
| scope words | IN | ✓ (REDUCTION of FB-LIN; not bounded; FB-LIN, G-N5-TIME open; not M3; not a TARGET.md claim) |
| premises | partial | GAP-L3: name R15 (a), (d), R17 (a) (F1) with R57 (a) (VJ), R21 (a), R38 (a), R88 |
Every displayed inequality equals the packet's. The line makes no claim beyond §2-§5. Verdict (Opus 5.5, D15): MATCHES after GAP-L1..L3
(definitions only; no E-item). The OPT-OFF clause is true as stated; its packet proof needs GAP-R1.

## DONE / FINDINGS / NEEDS
- DONE: this report.
- FINDINGS: 12 of 13 items SIGNED on the packet's text; OPT-OFF's statement TRUE, its proof has one hole (G-GAP-1, Case 2 (ii) with v's cycle
  node on π) with my repair GAP-R1; Theorem GAP-RED SIGNED and independent of it; RESULTS line MATCHES after GAP-L1..L3.
- NEEDS: Lead: route G-GAP-1 / GAP-R1 and GAP-N1..N3, GAP-L1..L3 to L-NEW's fixes file; the §C word after REFEREE-2's report.
