# R95: the Odd-minimum next-top selector (R94 design (a)) is DEAD as a wave re-armer: a self-read is a cycle check (O4), and one boundary per chain leaves no wave in the causal loop
L-RED successor 23 (Opus 5.5; D14/D15/D18; Lead GO 2026-10-26 19:18Z, target (1), time box ~2 h). Work 19:19-19:36Z on 10-26 (weekly limit
stop), written up 2026-10-28 from 21:06Z (date -u) after the Lead's RESTART. Labels (D18 / L40): DEAD (for the stated design class) / DATA /
READING / OPEN. Target: R94 §1 and §5 (design (a)); docs/si/N5-EXIT-box22.md §9 (ALTERNATION); docs/si/N5-ALT-box23.md §6 item 1 (XR-LIN).
Sources opened: docs/new/N5-ssi-global.md SPEC S1-S5 + FIX 1-4 (Q1-Q4); docs/si/N5-EXIT-box22.md §0, §8, §9; docs/si/P-N5-DEPTH-box22.md
§0-§6; docs/new/N5-ALTLIT-box49.md (l-new 3e03271f) §0-§4; docs/si/N5-ALT-box23.md §0-§6 (trunk bb399acd).

## 0. Result in one paragraph
- The design: a two-way Bellman-Ford chain v_1..v_L between two Odd selectors x_L, x_R. Each top's σ̄-minimum is meant to rise one option at
  a time, each rise triggered by the OTHER top's wave arriving, so that every rise re-arms a wave of length ~L over the same chain
  (target: phase ~ (#stages)·L ~ n²/12 at k = 2).
- It fails. The stage riser is an Even switch on the selector's own minimum play that reads the chain.
  - When the read point lies on the selector's side of the chain's boundary (a "self-read"), the riser's improving test IS the cycle test of
    the cycle it would close (O4).
  - That cycle must be Even-good, or the later wave toward the selector is not improving.
  - So the riser fires as soon as its own top's wave passes the read point. With one boundary per chain this removes every wave from the
    causal loop (§2).
- Both failure modes are pinned (n5 = n5b, Oink verified): sel_L6_M6 shows the premature cascade, selneg_L6_M6 shows the stall. Data
  run lengths: 4 and 6 at n = 27.
- Also recorded: the fallback-clocked repair (a′). Chained pendency gets past R94's S4c objection, but it needs a gate split (σ̄ ≠ τ) for the
  whole phase, and keeping τ fixed then needs a slow escape. In the bit model that is a regress (§3, READING).

## 1. The construction (experiments/red/sel/mksel.py L M [--neg]) and the pins (DATA)
- Chain v_1..v_L (Even, priority 1, edges to both neighbours); v_0 = x_L, v_{L+1} = x_R (Odd, priority 1).
- Stage values a_k = {H_1..H_k}: a spine H_k → H_{k−1} → … → H_1 → b of high even vertices; b (even, lowest high) is the sink.
  Ranks: H_1 > R_1 > H_2 > R_2 > … > H_M > R_M > b.
- Stage k: Even y_k → {H_k (static), R_k (reader)}. Odd k sits on x_R and reads v_L; even k sits on x_L and reads v_1.
  - Rank window R_k ∈ (H_{k+1}, H_k). Then y_k is Ξ-improving exactly when a_{k+1} is read (R_k ∪ a_{k−1} < a_k < R_k ∪ a_{k+1}), and after it fires
    R_k ∪ a_{k+1} > a_{k+2}, so the selector's minimum moves to the next static stage.
- τ = an Odd-optimal pair (Iτ = ∅, found by enumeration), so the run is one phase. --neg gives R_k odd priority.
- Pins (experiments/red/sel/instances/; experiments/red/ul/vrun.sh; experiments/red/sel/trace.py prints every iteration):

| instance | sha1 game | sha1 start | n | τ | n5 / n5b (fb) | Oink | trace |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sel_L6_M6 | e10abdbc… | 3d7e63dc… | 27 | xL→y6, xR→y5 | 4 / 4 (0) | OK strategies verified | it 1: v1→xL and y1→R1 (self-read through v_L, x_R, y_1); σ̄(x_R) → y3; it 2-4: y2..y6 fire, all stages gone in 4 steps |
| selneg_L6_M6 | e274fd0b… | f35b302e… | 27 | xL→y2, xR→y1 | 6 / 6 (0) | OK strategies verified | one wave v1..v6 → x_L (6 steps), then no reader is improving: stall |

## 2. Obstruction (O4) and the boundary count (READING; each step is SPEC S1/S2 plus RESULTS R15 (a) monotonicity)
Let x be a selector and y_c its current minimum option.
- (i) A rise of Ξ(x) needs a change on x's minimum play.
  - Odd's minimum only rises if the minimum option's value rises.
  - Downstream of Odd choices this ends at an Even switch e → f on the play: the RISER.
  - For the rise to be timed by a wave, f's play must reach the chain at some read point w.
- (ii) Self-read = cycle check (O4). Suppose w lies on x's side of the boundary, i.e. w's play goes to x and then x → y_c ⇝ e. Then f's play
  passes e, and Ξ(f) = [f..e) ⊕ Ξ(σ e). So the edge (e, f) is improving iff the cycle C := e → f ⇝ w ⇝ x → y_c ⇝ e is Even-good (S2 with S1's
  order; the standard SI cycle criterion).
- (iii) After a genuine fire, C must be Even-good. The other top's wave arrives, the riser fires reading the other top's value, and x's
  minimum moves on (otherwise x's value is routed through the chain and cannot exceed the other top).
  - The wave back toward x then switches w. If C were Even-bad, Odd's best response would close C at x after that switch, and x's value
    would fall.
  - That contradicts monotonicity of improving switches. So the switch would not be improving: C must be Even-good.
- (iv) Hence, by (ii), the riser of stage c is improving, and in S4a also W-accepted, at every state where w is on x's side while y_c is x's
  minimum.
  - W-acceptance: W(f) ⊵ [f..x] ⊕ Ξ(x) = Ξ(f) ▷ Ξ(σ e) = W(σ e) when σ e's play passes no gate. This is the gate inequality (O1) of R91 §6.
  - So stage c must never see w on x's side, from x's rise to stage c until its genuine fire.
- (v) One boundary. On a two-way chain every Even-good state has at most one boundary β: the left part points to x_L, the right part to
  x_R. Two neighbours pointing at each other form a low cycle, which is Even-bad.
  - By (iv), x_R's read point w_R satisfies β > w_R at all times, and x_L's read point satisfies β ≤ w_L at all times. So
    w_R < β ≤ w_L for the whole run.
  - Then w_R's play always reaches x_L and w_L's always reaches x_R, through chain segments that never switch. Each top reads the other's
    value with no delay, so the leapfrog cascades without waves.
  - The phase length is then O(#stages + L), not their product. The pins show both regimes:
    - sel_L6_M6: w_R = v_L is on x_R's side at the start, so it cascades.
    - selneg_L6_M6: C is made Even-bad, and the fired value stays below the other top, so it stalls.
- Scope (what is DEAD): a selector rise whose riser lies on the selector's minimum play and reads ONE two-way chain, with waves driven by S4a or
  by fallbacks. Two chains whose boundaries interact were not tried; each chain still obeys (v), so the delay would have to come from the
  coupling.

## 3. The fallback-clocked repair (a′) and why it needs a long-lived split gate (READING)
- Idea: time the rises by fallbacks instead of reads.
  - A ladder of Even rungs e_1..e_m. Rung j+1's ladder edge becomes Ξ-improving only after rung j has fired (chained pendency), so exactly one
    rung is pending at a time. This answers R94's objection that S4c takes all static tops at once.
  - Rungs are W-rejected, so S4a never takes them. A fallback happens only when S4a is idle, i.e. at the end of each wave. The tops t_R, t_L
    (Even) read the newest odd / even rung.
  - On paper this gives one stage per wave, i.e. a phase ~ m·L, with k = 1.
- What it needs: W-rejection of an Ξ-improving edge. That needs the rung's static option to pass a gate g with W(g) ▷ Ξ(g), i.e.
  σ̄(g) ≠ τ(g), for the whole phase.
- τ must stay constant, so S4b must not move τ(g). In the bit model that makes τ(g) optimal against Even's best reply: g's σ̄-option A must
  have best-reply value ⊵ that of τ(g), while its current value is lower. So Even's improvement in A's region must stay pending for the
  whole phase:
  - An escape through g itself closes a cycle with g. It is Even-good iff it is improving, and then S4a takes it at once (O1).
  - A slow escape that is a BF chain finishes in ≤ n steps.
  - A slow escape that is a fallback ladder needs its own W-rejecting gate. With bit values, one gate needs ladder values < BIG (for W-rejection)
    and an escape value ⊵ BIG (for τ-optimality). Two gates g1, g2 that serve each other need BIG1 ≤ (values of ladder 1) < BIG2 and
    BIG2 ≤ (values of ladder 2) < BIG1, which is impossible.
- Status: READING. This is a bit-model argument, not a theorem about all games. It matches L-COMP 6's DATA on Friedmann's H_n (BOX 16:
  S4b shuts the gates in the first n iterations). Not built: (a′) with a non-optimal τ would end the phase at step 1 by S4b.

## 4. What this leaves (OPEN)
- XR ≤ phase length (trivial), so a kill of XR-LIN (docs/si/N5-ALT-box23.md §6 item 1) needs an ω(n) phase at fixed k. A wave re-armed once per
  top rise is excluded by §2 for the selector class. The remaining routes are:
  - (1) the counter recursion of N5-ALT §1 / §4 (TOP-ONCE is dead on lev_l_sc: a top bit re-enters 7 times per run) as a parametrised family;
  - (2) a gate kept split for ω(n) steps (long121's gate 0 is split for a 3n phase, R88): what keeps τ(0) optimal there is the obstruction to
    study (§3);
  - (3) Lead's BOX 16 hint (an H_n variant that holds τ at a gate's opening edge). §3's constraint applies to it: any gate that stays split
    in one phase needs an escape whose improvement stays pending for the whole phase.
- Tools: experiments/red/sel/mksel.py (generator, Odd-optimal τ by enumeration), experiments/red/sel/trace.py (per-iteration N5 trace; the
  same loop as experiments/new/n5.py run(), mode n5; iteration counts agree on both pins).
