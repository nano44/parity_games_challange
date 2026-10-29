# R110: which pivot rules S4b realises for Odd. S4b CAN take a U-non-best improving switch while a U-better one is available (pivot_demo, n 11). In general Odd's step is "the W-optimum against the current σ over {keep} ∪ I_τ", so σ acts as the controller of Odd's strategy improvement on G^d. DATA + READING
L-RED successor 26 (Opus 5.5; D15/D18; Lead 12:36Z: «state either way: whether S4b's choice can make Odd take a NON-best improving
switch while a better one is available, i.e. which pivot rules S4b can realise»). Labels: DATA / READING / OPEN. Not a TARGET.md claim.

## 1. DATA: pivot_demo (experiments/red/ctl/pivot_demo.pg + .start; n 11)
- Game:
  - o (Odd) has successors C, A, B, all one-successor Odd vertices.
  - C → sE (Even self-loop, priority 40).
  - A → ea (Even): ea → sA1 (even self-loop, 30) or → sA2 (odd self-loop, 31).
  - B → eb (Even): eb → sB1 (even self-loop, 34) or → sB2 (odd self-loop, 33).
- Start: τ(o) = C, σ(ea) = sA1, σ(eb) = sB2.
- U-frame (Odd's valuation of τ on G^d, Even best-replying): U(C) ends in sE (40), U(A) in sA1 (30), U(B) in sB1 (34). I_τ(o) = {A, B},
  and A is the U-best improving switch for Odd (the smaller even cycle).
- W-frame against the current σ: W(A) ends in sA1 (30, Even-won), W(B) ends in sB2 (33, Odd-won). So B is W-best for Odd.
- n5b SPEC trace:

| state | σ(ea), σ(eb) | τ(o) | I_τ(o) | I_σ |
| --- | --- | --- | --- | --- |
| 0 | sA1, sB2 | C | {A, B} | {eb: sB1} |
| 1 | sA1, sB1 | **B** | {A} | {} |
| 2 | sA1, sB1 | A | {} | {} |

- Transition 0 takes the NON-best improving switch o → B while the better o → A is available. S4b computes against the old σ, in
  which eb is on sB2. In the same transition S4a moves eb to sB1.
- Checks: L-COMP's n5b and the n5.py/si.py engine give identical state sequences (xeng.py); Oink zlk OK with both strategies
  verified.

## 2. READING (from SPEC S4b, n5b.py step 3)
- S4b: τ_new = Odd's optimal counterstrategy (S1) to σ in H′, where Odd v may use only {τ(v)} ∪ I_τ(v) and Even is fixed to σ.
- That is the pointwise W-optimum, for Odd, of a one-player game. So at every Odd vertex with I_τ(v) ≠ ∅ the step:
  - (a) keeps τ(v) when τ(v)'s W-play against σ is at least as good for Odd as every improving option. "No switch while improving" is
    possible: a stall;
  - (b) otherwise takes the W-best improving option against σ, which need not be the U-best (§1);
  - (c) does (a)/(b) at all Odd vertices at once, consistently (a joint optimum, not independent local choices).
- I_τ depends on τ only (U_τ is a function of τ). So Odd's menu stays fixed until Odd moves, and σ decides, through W, which subset of
  the menu is taken and when.
- Realisable pivot rules: a selection of improving switches S ⊆ I_τ with chosen targets is realised at a state iff the current σ
  makes those targets W-best and "keep" W-best everywhere else.
  - Single-switch rules (one Odd vertex at a time) are realisable whenever σ makes "keep" W-best at all other menu vertices.
  - Non-best-target rules are realisable as in §1.
- Limits (OPEN):
  - σ is not free. It evolves by S4a (W against τ inside I_σ), so the controller is Even's own improvement process. In §1 the
    controlling choice (eb on sB2) is undone in the same transition.
  - Whether S4a can keep re-creating such controlling configurations for super-polynomially many Odd steps inside one λ-run is exactly
    the NM*^U question. Every controlling configuration is a non-optimal σ, so it must keep being re-created by Even's own carries.
- Consequence for the literature route: adversarial-pivot exponential SI paths (one switch at a time, in a chosen order) are not
  excluded by S4b's rule. Their reachability is limited only by what σ's dynamics can present.

## DONE / FINDINGS / NEEDS
- DONE: pivot_demo instance (two engines, Oink), this note.
- FINDINGS:
  1. DATA: S4b takes a U-non-best improving switch while the U-best is available (pivot_demo, transition 0).
  2. READING: Odd's step is the W-optimum against the current σ over {keep} ∪ I_τ. Stalls, single switches and non-best targets are
     realisable whenever σ presents the matching W-ranking. σ is the controller, and its own dynamics are the open part.
- NEEDS: none from the owner.
