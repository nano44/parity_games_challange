# R231 (b2): Lemma ONE-CROSS, the first horn of the re-arm dilemma, as a lane lemma (L-RED successor 65)
Written 2026-11-12 (date -u in the commit). Lead 06:32Z (b): «try to turn your dilemma into a lane lemma or an exact failure … with premises
named and quoted by script». Labels: PROVED (lane, unrefereed) / DATA / READING. Scope: IDEAL-CYC(G) on Γ(G), every genome (R118 (a)). The
Lead's wording said «on Γ3»; this lemma is proved for IDEAL-CYC only, because its premise F1 is an IDEAL-CYC fact. The Γ3 / N5′-xi form
is NOT claimed. Nothing here is a TARGET.md claim.

## 1. Premises (quoted by grep from trunk 575ac9443)
- F1, frozen P-N5-XICYC §3 l. 69, a premise of RESULTS R118 (b): «F1 (from [R15a]): Ω_t ⊴ Ω_(t+1) pointwise, for every step t.»
- Corollary NO-TIE, RESULTS R123 (c) (l. 15171): «At every state and every gate g, Ω_t(e_g) ≠ Ω_t(β_g). So LOC-GATE applies at every gate and
  state.»
- Lemma LOC-GATE, RESULTS R123 (d) (l. 15173-15174): «Let G be any genome, t a state of a run of IDEAL-CYC(G), g a gate, a := σ̄_t(g),
  b := its other face, Ω := Ω_t. If Ω(a) ≠ Ω(b), then Ω(a) ◁ Ω(b).»
- ⊴ is the total order on values of VJ00 §4.2 (R118's premise list).

## 2. Lemma ONE-CROSS (PROVED, lane)
Statement. Let g be a gate and a ∈ {e_g, β_g} a face with Ω_t(a) = c for every state t of the run. Then σ̄_t(g) changes at most once over
the run, and if it changes, it changes from the other face b to a.
Proof. By F1, t ↦ Ω_t(b) is ⊴-non-decreasing. By NO-TIE, Ω_t(b) ≠ c for all t; by LOC-GATE, σ̄_t(g) = b iff Ω_t(b) ◁ c. If Ω_s(b) ◁ c and
t ≤ s, then Ω_t(b) ⊴ Ω_s(b) ◁ c. So {t : σ̄_t(g) = b} is an initial segment of the run, and σ̄(g) = a on the rest: at most one change,
from b to a. ∎
- Corollary (the dilemma's first horn, PROVED, lane). A re-arm route through a gate whose exit face has a constant value is one-shot:
  the gate follows the route (β) on an initial segment and exits (e) afterwards, never again following it. In particular this holds when
  the exit's play reaches a fixed cycle through vertices whose successors never change. Example: CWG1/CWG2's y, whose e-face play is
  e_y → z0 → its one gate, and z0's two faces lead to c_W and X, both fixed.
- What the lemma does NOT give: anything when both faces move. The second horn (an exit that moves with the race leads back into R and
  the race cycle traps) is DATA on MWR-based designs only (R231-cwr, R231-rearm2), not a lemma.

## 3. DATA (onecross231.py, own engine r221q/own.py; unit: gates; scope: every gate; must-0 counters xfail (constant face, ≥ 2 changes),
dfail (a change away from the constant face), tie (Ω(e_g) = Ω(β_g) at some state))
- Instances (out/onecross231_inst.out): CWG1_4, CWG1_8, CWG2_8, CW8_n, CWRR8_n, BLKX23_n48, K1L10_n48: 1,184 gates, 1,134 with a constant face
  (17 of them change once), xfail 0, dfail 0, tie 0. CWG1_8's y gate is one of the 2 single changes there; CWG2_8 has 8.
- 1,000 random genomes (seed 233; out/onecross231_rand233.out): 17,468 gates, 7,090 with a constant face, 602 change once; xfail 0, dfail
  0, tie 0. 300 random k = 1 genomes (seed 234; out/onecross231_rand234_k1.out): 1,903 gates, 1,408 constant, 70 once; all 0.
- Counter sees repeated flips: 2,059 gates (random set) with no constant face change ≥ 2 times.
- Control (OC_CTRL=1: «constant» weakened to «equal on the first two states»; out/onecross231_ctrl.out): xfail 324, dfail 297 (fires). The
  weaker control «first value = last value» cannot fire: by F1 a face whose first and last values agree is constant, so that row is
  identical to the uncontrolled run (noted, not an error).
- READING: so the only re-arm gates that can flip repeatedly have two moving faces. At k = 1 in MWR-based designs every moving exit tried
  leads back into the race (R231-cwr §3: every single target; R231-rearm2 design 2). Whether some k = 1 design has a moving exit that does
  not lead back into R is exactly the open shape; ONE-CROSS says no constant exit can serve.
