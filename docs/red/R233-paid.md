# R233b: adversary on L-NEW 71 Lemma PAID (box 207 Addendum A, claude/l-new b72411cf) (L-RED successor 65)
Written 2026-11-12 (date -u in the commit). Lead 08:59Z: «(a) Read the proof case by case. Quote its premises by script … Watch for the
Γ-vs-IDEAL-CYC scope. (b) Run its must-0 counter on your own engine … with a control that fires.» Engine: experiments/red/r221q/own.py
(IDEAL-CYC on Γ); tool experiments/red/r233/paid233.py; no L-NEW code. Labels: SURVIVES / GAP / DATA / READING.

## 0. Verdict: Lemma PAID SURVIVES (every step), with one wording GAP (P1, harmless)
- Scope: IDEAL-CYC(G) on Γ(G) (R118 (a)). Every premise used is an IDEAL-CYC-on-Γ statement: LEVEL0 is R118 (h); B-ONLY, LOC-GATE, LOC-K2
  are R123. Nothing is claimed for Γ3; the Γ3 analogue would need R125's LOC-GATE3 / B-ONLY3 / LOC-K2-3 and a Γ3 form of LEVEL0. Not checked.
- GAP P1 (wording): Step 0 lists the possible cycles as «K1's self-loop, c_W's self-loop, or passes R». R104 also has «an unused even
  self-loop of priority 2» (c_X). It has no in-edge, so no play reaches it, and the list is complete for plays. A packet should say so.

## 1. Premises (grep of trunk docs/RESULTS.md at 575ac9443)
- R118 (h) Lemma LEVEL0 (l. 13696): «In every state σ̄_t takes the β-face at every gate of a level-0 mover.»
- E-DOM, R121 (b) (l. 14481): «Every vertex more relevant than some e-vertex is an e-vertex, c_W, K0 or K3, by [DEF]».
- R104's Γ(G) (l. 9864):
  - «e of even priority above every β with one edge to the W-target or to the top even self-loop c_W; an unused even self-loop of priority 2;
    … a closed core u = K0 (Even, top + 2) → {K1, K3}, K1 (Even, 5) → {K0, K1}, K2 (Odd, 3) → {K1, K2}, K3 (Even, top + 3) → {K1, K2}».
  - Start: «β → its Ξ-target (u when the target is X), K0 → K3, K1 → K1, K3 → K2».
  - So (D1) e_g's only in-edge is from g, and (D3) the core is entered only at u = K0.
- R123 B-ONLY, LOC-GATE (l. 15076), LOC-K2 (l. 15176): as quoted in box 207 A1 (identical wording).
- [VJ] order ⊴: R118's premise (VJ00 §4.2 / Friedmann arXiv 1106.0778 §3). Lex order on e-sets: landed R121 (a) names it («lex order on
  sets of e-vertices»); its formula is in the frozen packet P-N5-ASC §2 l. 54: «S ≤ S′ iff S = S′ or the most relevant element of S Δ S′
  lies in S′». PAID uses only that formula.

## 2. Case-by-case reading
- Step 0 (a): an e-vertex f on a cycle forces Λ(m) = Λ(f) ⊵ f for the mover m after it, against B-ONLY. ✓
- Step 0 (b): the core is frozen K0 → K3 → K2 → K1 → K1 (R104 start, R118 (a), LOC-K2); nothing leaves it. ✓
- Step 0 (c): a cycle avoiding e's and the core is mover → gate → β → Ξ-target, i.e. a Ξ-cycle, so it passes R (k = 1). ✓ (Gap P1 for c_X.)
- Step 1: c_W is entered only from e's of level-0 options (W-target −1), and those are reached only through their gates, which take β
  (LEVEL0). A level-0 g cannot be on its e-face. So both faces of a non-DIRECT g end at K1. ✓
- Step 2: both plays enter the core at K0 → K3 → K2 → K1. K0 and K3 are more relevant than K1, so they lie in both Π; c_W lies in neither. ✓
- Step 3, Case A (e_g ∉ Π(β_g)): z, the most relevant element of the Π-difference, is e_g or more relevant. By E-DOM and Step 2, z is an
  e-vertex (even), so it lies on the larger side, β's (LOC-GATE: Odd chose e, so Ω(e_g) ◁ Ω(β_g)). And z is the most relevant element of the
  E-difference. ✓
- Step 3, Case B (e_g ∈ Π(β_g)): β_g's play passes g (D1). If e_g were its first e-vertex, the segment β_g … g would be a Ξ-path xt(g) → … → x,
  closing a Ξ-cycle without R (g not DIRECT): impossible. So E(β_g) ⊋ E(e_g). ✓
- (ii): h := the gate of the first e-vertex f on β_g's play; σ̄(h) = f. The vertices before h are movers, gates and β's. β's ARE in Π
  (priority ≥ 6 > 5 = K1's) but are not e-vertices, so E(β_g) = E(e_h). ✓
- Step 4: strictly rising E along a total order, so the gates are distinct and the chain ends within M − 1 steps at a DIRECT gate. ✓
- Remarks (1) (any k with a feedback set F) and (2) (Ξ-acyclic: no e-face, BETA-ACYC's first clause on Γ): consistent with the proof; not
  re-checked by counter.

## 3. DATA (paid233.py, own engine; unit (feedback vertex R, state, gate at its e-face); scope every gate, EVERY single feedback vertex)
- Must-0 counters notK1, nonext, notE, lexfail, nochain: 0 on all of these:
  - MWR4_2, K1L10_n48 (2 feedback vertices), CFI3_n48, RINT_n48, BLKX23_n48 (3), CW8_n, CWRR8_n, K1L7_n48: 1,228 cases, 913 DIRECT, longest
    chain 2 (K1L10). out/paid233_records.out.
  - 300 random k = 1 genomes (r231/dep231.rgen, seed 2331): only 170 cases, 166 DIRECT, chain ≤ 2. Thin: small genomes rarely take e-faces.
    out/paid233_rand2331_k1.out.
- Per feedback vertex the counts equal box 207 A3's: MWR4_2 109 / 109, CFI3 48 / 36, RINT 98 / 64, CW8 284 / 284, CWRR8 22 / 22, K1L7 142 / 73.
- Control PAID_CTRL=1 (R := the first mover that is NOT a feedback vertex): lexfail 109 on MWR4_2, 25 on CFI3_n48 (fires;
  out/paid233_ctrl.out).
