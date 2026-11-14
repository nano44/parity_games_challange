# Box 201 (D18): a subclass bound for R — attempt and exact obstruction (L-NEW successor 67, Opus; written 2026-11-09T01:54Z by date -u)
Lead 2026-11-09 01:19Z: «(1) CONSOLIDATE the core … docs/new/N5-CORE-forms.md … (2) a SUBCLASS bound … a structural restriction under which
R is provably polynomial WITHOUT bounded U(G) — e.g. bounded out-degree of the switching vertex u, or a bound on gates per cycle, or no two
splits in one Howard step … state it, prove it, test it … (3) only if (2) stalls: the kill side».
Labels: PROVED (lane) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD / READING. Nothing here is a TARGET.md claim; G-N5-TIME OPEN.
(1) is done: docs/new/N5-CORE-forms.md (l-new 14babccb). This file is (2).

## 0. Answer
- (2) STALLS. I have no subclass theorem. The exact obstruction, measured on all eight frozen box 200 instances: R's maximum sits at a GATE.
  Odd's face flips at one gate are R(gate, face, w): 65 on MW32_2, 8 on DHIB26_2804, 6 on C6G8_n54. Gates have out-degree 2 in every
  genome. So every restriction on Even's side (mover out-degree, single-split steps) leaves R untouched.
- A gate's flips are bounded only by the value changes of its two faces (L-SI 48's GATE-RACE: flips ≤ 2·min(ch_p, ch_q) + 1). The faces
  are the W-target's and the Ξ-target's values. So a bound on gate flips is a bound on value changes of movers: the recursion again.
- Odd's best reply changes at almost every step: F/T3 (unit: steps with σ̄ changed / Howard steps) = 16/17, 10/10, 18/19, 27/28, 11/12,
  162/199, 16/53, 1/4. CONJECTURE SEG-H (DATA only): an interval of steps with σ̄ and every Λ constant has at most N + 1 steps.
  - DATA: the longest such interval is ≤ 3 steps on all eight instances.
  - If proved, it gives T3 ≤ (F + L + 1)·(N + 2), L := #steps with a Λ-change (≤ n3·(2M + 2)).
  - But F ≈ T3 on every instance, so «F polynomial» is the whole question again. Not a subclass.
- The one structural class where the obstruction disappears is already known: Ξ-acyclic genomes. There Odd never leaves the β-face
  (RESULTS R122, BETA-ACYC: R = 0, T ≤ N). A class strictly between that and all genomes would need a bound on gate flips from the
  Ξ-cycle structure. A candidate parameter (READING, not measured, not proved): the minimum feedback vertex number k of the Ξ-graph. The
  target statement would be T3 ≤ (N + M)^O(k). That is a restricted class (TARGET.md §4), not M4.
- (3) Per the Lead's order, I stop here. The kill side (a race of races with R super-linear) is L-RED 62's and L-SI 48's. Coordinate via the
  Lead.

## 1. Candidates tried, each with its obstruction (DATA; tool box201/rarg.py, seg.py on the box 200 engine; set: box200/inst, 8 genomes;
## scope: N5′-xi from S3 on Γ3 up to the first fallback)
| candidate restriction | what it would need | obstruction (instance) |
| --- | --- | --- |
| bounded out-degree of the switching vertex u | R large only at high-degree movers | R's argmax is a GATE (out-degree 2): MW32_2 gate (298,0) 65 flips; DHIB26_2804 and C6G8_n54 gate (10,0) 8 and 6 flips. The top mover R is equal or smaller (MW32_2 x299, out-degree 34: 65; DHIB26 x10: 7) |
| no two splits in one Howard step (RW-1 regime) | single-switch steps | multi-switch steps are the norm: switches per step up to 49 (DHIB26), 37 (RWX_n95), 4 on MW32_2 (39 steps with 1, 64 with 2, 64 with 3, 32 with 4). And RW-1's consequence (C-WT on single-split couples) still recurses over the ascent DAG, i.e. needs bounded U(G) |
| bounded gates per cycle | — | not a restriction in the genome class: every cycle through a mover passes ≥ 1 gate; RWX_n95 has one Ξ-SCC of 71 movers. No data taken |
| Odd's best reply changes polynomially often (F) | SEG-H + F ∈ P | F/T3 ≥ 0.85 except FW16_2 (16/53) and WC16_2 (1/4): F ≈ T3 (above) |
- Tool outputs: box201/rarg.out (top four (u, b) by R, out-degree, switches-per-step histogram), box201/seg.out (F, L, longest
  constant-(σ̄, Λ) interval, segfail = longest > N + 1: 0 on all eight).

## 2. What a subclass theorem would have to do (READING)
- R-EQUIV puts the core at one edge. The data put the largest edges at gates. GATE-RACE charges each flip to a value change of the face Odd
  leaves. So a class bound needs face values that change polynomially often per Λ-interval, with no recursion through other gates.
- Ξ-acyclic is the extreme case: the β-face always wins, and flips are 0 (R122). Any intermediate class must let some gates take their
  e-face. Their number, and how often the β-face can be re-beaten, would be the parameter. I did not find an argument that bounds re-beating
  by the Ξ-graph's structure. That is the exact step that is missing.

## Addendum 1 (L-NEW successor 67, 2026-11-09T02:43Z by date -u): corrections
- «R's maximum sits at a GATE» is FALSE in general (L-RED 62, claude/l-red c99bca51; and this box's own rarg.out: RWX_n95, DHIB18_2805,
  FW16_2 are mover-led, CX4_n21 and MW32_2 tie). Corrected text and per-instance list: docs/new/N5-XIFVS-box202.md §4 C1.
- «CONJECTURE SEG-H» is RESULTS R118 Theorem BR-SEG (landed); the bound «T3 ≤ (F + L + 1)(N + 2)» is R118 (l) T-CYC. box 202 §0, §4 C2.
