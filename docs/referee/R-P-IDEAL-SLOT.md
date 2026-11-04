# R-P-IDEAL-SLOT: REFEREE report on P-IDEAL-SLOT (L-NEW successor 51, box 158)
REFEREE successor 23 (Opus 5.5, D15), 2026-11-04T13:15Z by date -u. Independent: I did not read docs/referee-2/.
- Object: claude/l-new e46e98a4, an ancestor of origin/claude/l-new. I re-measured all three files:
  - docs/new/P-IDEAL-SLOT.md: sha1 62901b5f951598fb44426942b0fb1d999325625a, 192 lines;
  - docs/new/P-IDEAL-SLOT-line-L1.txt: sha1 17236fb18d70c1e2968689108a74a1acac938bd5, 1 line, no «|»;
  - experiments/new/box158/lift_max_d4_L13.json: sha1 33fec48f1a8f1c57891b7574d87cc6bbe5e3bd38.

## 0. Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §1-§2 | SEG, SEG-ONCE (copies) | SIGN: verbatim copies of P-IDEAL-SEG §0-§2, which I signed in R-P-IDEAL-SEG.md (19e0742f) |
| §3 | Lemma SHIFT (any degree) | SIGN |
| §4 | Corollary SEG-CAP (𝓛_d, d ≥ 2), with the finiteness of T* | SIGN |
| §5 | Lemma LIFT (any degree) | SIGN |
| §5 | Corollary SANDWICH | SIGN |
| §6 | DEAD SEG1-2D, instance lift_max_d4_L13 | SIGN (recomputed independently, and the lift rebuilt by me from LIFT's text) |
| §7 | machine checks, exclusions, TARGET diff | not to sign; w108, w109 and pin109 MATCH; diff agreed |
| line | L-1 | NOT YET: REQUIRED SLOT-L1 (SHIFT) and SLOT-L2 (LIFT): two definitions are inexact |
- Labels.
  - PROVED (lane + REFEREE): SHIFT, SEG-CAP, LIFT, SANDWICH. SEG and SEG-ONCE are carried copies.
  - DEAD (instance): SEG1-2D.
  - Nothing is bounded polynomially; the upper recursion gives 3^d − 1. G-N5-TIME OPEN.

## 1. Premise route and the carried copy
- Premises: R104's definition and R105 LOCAL's key half, «a key only on the states below its level» (verbatim in the landed R105 line,
  checked in R-P-IDEAL-SEG §1). P-IDEAL-SEG is not a premise. No docs/lit, no R106 or R107.
- The copy: I diffed §0-§2 against P-IDEAL-SEG.md at 8291ecf7. The only differences are the two headings («(PROVED)» →
  «(carried verbatim from P-IDEAL-SEG §n)»). The text is IDENTICAL, so my P-IDEAL-SEG signatures apply unchanged.
- Used: SHIFT uses no R105 item (it compares keys directly). SEG-CAP uses SEG, SEG-ONCE and SHIFT. LIFT uses no R105 item. SANDWICH
  uses SEG-CAP and LIFT.

## 2. Proof checks
- SHIFT: SIGN.
  - Gates: g′ = g(w)·Γ + g(x, k) determines the pair (quotient, remainder), so new gates are distinct.
    - New gates with g(w) ≥ 1 lie above every old gate.
    - A new gate with g(w) = 0 equals that option's own old gate, which no unchanged gate equals.
  - W-targets: both ends drop one level; the former level-1 options get none; the level-0 movers stay as degree-1 movers without
    W-targets.
  - The Ξ-data are unchanged.
  - Keys: for two options of the same mover, the first G↓ entries compare as the pairs (g(o_0), g(o_1)) lexicographically (since
    g(o_1) < Γ). The remaining entries are equal. So the key orders agree.
  - The step choices and both stop tests then agree, by induction over the levels.
- SEG-CAP: SIGN.
  - T*(1) ≤ 2 (SEG-ONCE, l = −1). The finiteness induction is not circular: SEG-CAP at d needs T*(d − 1) finite, and SANDWICH's upper
    bound then gives T*(d) finite.
  - There are at most two level-0 steps, and T = seg1 + mid + tail + #level-0 steps.
  - Each segment is an interval without level-0 moves. SEG with l = 0, then SHIFT (H's level-0 movers have degree 1), puts H↓ in
    𝓛_(d−1) from start s_(a−1). Its level 0 = G's level 1 plus the frozen degree-1 movers.
  - So each segment is ≤ T*(d − 1).
- LIFT: SIGN.
  - A and B: each option's Ξ-value is its own singleton β, and option 0 holds the larger even rank. So option 0 is strictly better
    under every state, A_s(A) = {0}, and they never move.
  - A and B are nobody's Ξ-target, so old chains and values are unchanged.
  - Every old W-chain ends at (A, 0), so every old key gains the same first entry g(A, 0), and the orders are unchanged. This needs ALL
    old level-0 options to point to the SAME never-moving option, which the construction gives: W-target A, with A fixed at option 0.
- SANDWICH: SIGN.
  - Upper: SEG-CAP + ≤ 2 level-0 steps.
  - Lower: LIFT maps 𝓛_(d−1) into 𝓛_d. The new level 0 is {A, B}, the old degree-1 level-0 movers move up, and there is no level-0 step,
    so seg1 = T.
  - sup seg1 = T*(d − 1) by SEG-CAP.
- DEAD SEG1-2D: SIGN.
  - The precise «2d − 1» form is the packet's own reading of the Lead's «bound the first segments linearly in d». The lane notes
    (N5-SLOT-box158.md) carry no separate statement.
  - The kill is robust: by SANDWICH, ANY bound seg1 ≤ f(d) on 𝓛_d gives T*(d − 1) ≤ f(d).
  - The «largest seg1 3, 5, 6, 9, 10» table is lane DATA. I did not re-run it, and it is not to sign.

## 3. Independent checks (scratch/xinew_probe.py β-set simulator, written from R104's text)
- Instance lift_max_d4_L13 (file at e46e98a4):
  - valid: acyclic, W one level down, distinct ranks and gates;
  - levels [1, 1, 2, 2, 3, 3, 4, 4, 0, 0], all of degree 2: a 5-level 2-wide ladder, no degree-1 movers;
  - T = 13, no level-0 step, so seg1 = 13 > 2·5 − 1 = 9;
  - its old-mover states equal max_d4_L13's run state for state.
- My own LIFT of max_d4_L13, built from §5's text (new ranks R + 1..R + 4, even, larger on option 0; new top gates; old level-0 options
  → A; A, B start at 0): valid, T = 13, the same old-mover states, A and B fixed.
- scratch/slot_probe.py (log xinew_logs/slot_probe.txt):
  - LIFT on 6,000 random genomes: 0 mismatches.
  - SHIFT on 5,290 random genomes, with level-0 movers made degree 1 and every old run compared state for state with the G↓ run: 0
    mismatches.
  - Control MUT=1 (SHIFT with g′ := g(x, k), dropping the level-0 gate): 1,007 of 2,670 mismatch. So the Γ-encoding is what makes SHIFT
    work, and the probe can see it.

## 4. Machine checks at e46e98a4 (detached worktree)
- w108: three «SAME True» lines, plus «lift_max_d4_L13.json d 5 T 13 cuts [] seg1 13» and «lift_max_d5_L15.json d 6 T 15 cuts [] seg1
  15». These are the expected strings (lift_dd_d5_F14: d 6, T 14, seg1 14).
- w109: the box 150 checker on the instance prints «TOTAL genomes 1 runs 1 steps 13 XSIM 0 TOPO 0 … VIOL 0 (info REC148 0)», plus the
  three.py line. These are the expected strings.
- pin109: packet 62901b5f, L-1 17236fb1 and instance 33fec48f all EQUAL.
- w106 (SEG / SEG-ONCE) was re-run and matched in R-P-IDEAL-SEG §3.

## 5. Diff against TARGET.md
- No statement concerns parity games, regions, running time or the cost model. Each is about R104's IDEAL model and its ladder class
  𝓛_d.
- Agreed with §7: not M4, not M3, not a gauntlet step. G-N5-TIME OPEN.

## 6. Line L-1 (every DEFINITION diffed against the packet)
- These MATCH:
  - definitions: T; 𝓛_d (levels 0..d − 1, exactly two degree-2 movers per level, any number of degree-1 movers, none of degree ≥ 3 =
    §4); T*(d) (largest T over 𝓛_d and all starts; finite, so «largest» = sup);
  - the seg1 / mid / tail wording in SEG-CAP;
  - «2-wide degree-2 ladder» in DEAD (= §0, no degree-1 movers). «d ≥ 2» is dropped, which is harmless: at d = 1, seg1 = 0;
  - claims: SEG / SEG-ONCE (l ≥ −1 bound; «the interval's first state» = s_(a−1)); SEG-CAP; SANDWICH; DEAD (instance data, sha1,
    13 > 9; «any bound in terms of d is a bound on T*(d − 1)»);
  - scope, premises, tail, DATA.
- REQUIRED SLOT-L1 (SHIFT definition).
  - «removing one level» can be read as deleting the level-0 movers.
  - The packet keeps them: «every mover of level ≥ 1 has its level lowered by 1, and the level-0 movers stay at level 0». Deleting them
    would break Ξ-targets that point to them.
  - New: «lowering every level ≥ 1 by one, the level-0 movers staying at level 0 (the former level-1 options get …)».
- REQUIRED SLOT-L2 (LIFT definition).
  - «adding two never-moving level-0 movers with two options below a genome, one level up» states the conclusion («never-moving») in
    place of the construction. It leaves the old level-0 options' new W-targets free.
  - If some of them pointed to A and others to B, the keys of two options of one mover would get different first entries, and the run
    could change. So the line, read literally, admits a false instance.
  - New: «adding two level-0 movers A, B with two options each (Ξ-target X, four new even ranks above all others with the larger on
    option 0, four new top gates, start option 0), every old level-0 option getting W-target A, and every old level raised by one».
- OPTIONAL SLOT-L3: in SEG, «the interval's first state» → «the state before the interval's first step (s_(a−1))», to avoid reading it
  as s_a.
- VERDICT: line L-1 NOT YET. It matches once SLOT-L1 and SLOT-L2 are applied.

## DONE / FINDINGS / NEEDS
- DONE:
  - this report;
  - the copy diff;
  - w108, w109 and pin109 MATCH;
  - instance recomputed and lift rebuilt by me;
  - SHIFT and LIFT probes with a biting control.
- FINDINGS:
  - All 7 items SIGN, no proof gap.
  - Line L-1 NOT YET: SLOT-L1 (SHIFT: «removing one level») and SLOT-L2 (LIFT: construction missing; the literal reading admits a false
    case).
  - Optional SLOT-L3.
- NEEDS: Lead: route SLOT-L1/L2 (optionally L3) to L-NEW 51 for line L-2. I will do a §C when it is frozen.
