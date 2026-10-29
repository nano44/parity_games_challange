# R117: plain N5 after R116. Why the repeater does not transfer (τ freezes at the first set of each Odd bit), and a first (FO*) probe: masked CDAG_n frozen runs 3 / 5 / 6 at n = 3 / 4 / 5. DATA + READING; G-N5-TIME untouched
L-RED successor 29 (Opus 5.5; D1/D18; Lead 18:46Z: "Your next target, top priority, is plain N5 (G-N5-TIME)"). Written 2026-10-29
~19:20Z (date -u). Labels: DATA / READING / OPEN. Not a TARGET.md claim. Engine: L-COMP's n5b.py SPEC mode (N5 SSI-GLOBAL S1-S5).

## 1. N5 on dwN (DATA)
- cpl.py on experiments/red/sf/instances/dw_N.pg, S3 start. Iterations equal the n5b counts in R116 §3; fallbacks are 0.
  | N | n | iterations | σ-changes | τ-changes | joint λ-runs | longest run (σ-changes) |
  | --- | --- | --- | --- | --- | --- | --- |
  | 3 | 87 | 41 | 41 | 3 | 4 | 26 |
  | 5 | 139 | 55 | 55 | 5 | 6 | 38 |
  | 7 | 191 | 68 | 68 | 7 | 8 | 49 |
- Each h_i changes τ exactly once, e_i → m_i, early in the run. The run then ends in one σ-run of length about 7N.

## 2. Why: the Odd reset is never U_τ-improving (READING; elementary)
- Let τ(h_i) = m_i. In U_τ, Even plays a best reply to τ. Odd's alternative at h_i is e_i: going back into cycle e_i f_i g_i h_i.
  - Under that alternative, Even can close the cycle, whose top h_i is even, and win.
  - So U_τ(e_i) is worse for Odd than U_τ(m_i), and (h_i, e_i) ∉ I_τ.
  - U_τ depends on τ alone, so this holds whatever σ does.
- So an Odd bit that is an Even-closable cycle is set once and never reset.
- Before it is set, N5's S4b choice (Odd's optimum against the CURRENT σ, inside {τ(h_i)} ∪ I_τ(h_i) = {e_i, m_i}) tracks
  σ̄(σ)(h_i) exactly. Odd stays while σ leaves cycle i open, and escapes when σ closes it. Only the reset is missing.
- Once every bit has escaped, τ is the honest optimum τ*. By box 21 Theorem B (L-NEW, lane), N5 is then the FROZEN run:
  σ_(k+1) = Even's G_τ*-optimum inside the arena {σ(v)} ∪ I_σ(v). The old σ lies in that arena, so the G_τ*-valuation (a
  one-player game) never decreases along the frozen run. No reset of any kind can happen there. This is R109 §4's "unary forced under
  pinned τ" with its exact cause.
- Contrast with N5-SF (R116): S4a′ chooses against σ̄(σ), which reverts freely. That reversal is what the repeater exploits.
- Consequence (READING). A super-polynomial N5 run needs one of:
  - (a) Odd bits that are not Even-closable cycles, whose resets become U_τ-improving through Odd's own moves elsewhere (a counter on
    G^d: the coupled route of R111-R113);
  - (b) an exponentially long frozen run, the (FO*) core of G-N5-TIME: a G_τ*-monotone chain whose arena I_σ (honest Ξ_σ, Odd's best
    reply) admits one chain step at a time.

## 3. (FO*) probe: CDAG_n with Odd masks (DATA)
- CDAG_n (L-NEW box 8, claude/l-new docs/new/N5-K9-Pstrict-counter.md) has an Ω-strict single-switch improving chain of length
  2^n − n − 1. N5 solves it in 1 iteration.
- Masked version (experiments/red/sf/cdmask.py n = exhaustive; cdrand.py n K seed = random sample):
  - On each edge x → u (u ≥ 1) put an Odd mask o with edges {u, b}, where b has an odd priority and a single edge to a reader target z ∈
    {sink, 1..n}.
  - Masks can only REMOVE improving edges: Ξ_σ(o) = min(Ξ_σ(u), Ξ_σ(b)).
  - Run: N5 from σ_0 = every CDAG vertex → sink, with τ_0 = τ*, the final τ of an S3 run. τ* has I_τ = ∅ and U_τ depends on τ only, so
    τ stays τ*: this is the frozen run.
  - Configurations where Even does not win all of CDAG are skipped.
- Results:
  | n | configurations | max frozen-run iterations | chain length 2^n − n − 1 | unmasked |
  | --- | --- | --- | --- | --- |
  | 3 | all 24 389 valid of 33^3 | 3 | 4 | 1 |
  | 4 | 20 000 random (seed 1) | 5 | 11 | 1 |
  | 5 | 20 000 random (seed 1) | 6 | 26 | 1 |
  Histogram n = 5: 1: 10 608, 2: 6 463, 3: 2 572, 4: 313, 5: 21, 6: 1. Random sampling at n ≥ 4 is weak evidence.
- Hand analysis at n = 3 (READING):
  - The chain (3,2), (3,1), (2,1), (3,2) needs the mask on 2 → 1 to be closed while σ(3) ≠ 1 and open when σ(3) = 1. So it must read
    the HIGHER vertex 3. The exhaustive best (3 iterations) does exactly that: mask (2,1) reads z = 3 with b = 7.
  - At σ*, 3 → 2. So Odd's option o_21 → b → 3 → 2 → o_21 is a cycle whose top is b (odd), unless the reader's top is even, and then
    the mask never closes.
  - So a mask that reads a higher vertex either closes an Odd-won cycle at σ*, which breaks τ*'s pass-through and Even's win, or never
    closes.
  - In CDAG every higher vertex's play can pass through the masked vertex. OPEN: a chain in which every gate reads only vertices that
    cannot reach it, or readers that read copies.

## 4. (b) fails at m = 3: σ-gating is possible, τ*-transparency is not (READING, exact on this gadget class; Lead 19:10Z)
Setting (as §3): frozen run from τ* on CDAG_3, the chain gen(3) = (3,2), (3,1), (2,1), (3,2), states S0 (all → sink) → S1 → S2 → S3 →
S4 = σ*. A mask on x → u is an Odd vertex o_(x,u) → {u, y}. It is honest-CLOSED at σ when Ξ_σ(y) ≤ Ξ_σ(σ(x)), and τ*-TRANSPARENT when
τ*(o) = u, i.e. Ξ_σ*(y) ≥ Ξ_σ*(u), with Even still winning everything. Masks have priority below the sink cycle (ignored but for length).
Claim. No mask on (2,1) is both closed at S1 and transparent at σ*. Without such a mask, (2,1) is improving at S1 together with (3,1).
N5's arena then holds both, its optimum takes both, and the chain is cut.
Proof (reading, elementary). S1 and σ* agree on every vertex except 2: σ_S1(3) = 2 = σ*(3) (directly, or through a transparent mask),
σ_S1(2) = sink, σ*(2) = o_21, and vertex 1 → sink in both.
- Case 1: the reader play from y never visits 2. Then it is the same play in S1 and σ*, so Ξ_S1(y) = Ξ_σ*(y) =: Y.
  - Closed at S1 needs Y ≤ Ξ(sink).
  - Transparent needs Y ≥ Ξ_σ*(1) = {1} > Ξ(sink).
  - These contradict each other.
- Case 2: the reader play visits 2. At S1 it continues 2 → sink, so its relevant set is X ∪ {2} (X = what it visits before 2).
  - Closed at S1 against σ_S1(2) = sink means that set's most relevant vertex is odd.
  - At σ*, the same play reaches 2 → o_21. If Odd picks y there, the play closes the cycle o_21 → y → … → 2 → o_21. Its vertex set is
    the same X ∪ {2}, plus o_21, which is ignored. Its top is odd, so Odd wins the cycle.
  - So τ*(o_21) = y: the mask is not transparent, and Even loses 2.
□
- What breaks is τ*-transparency. σ-gating alone is easy: the exhaustive n = 3 best (3 iterations) gates (2,1) by reading vertex 3
  (Case 2, b = 7), and it pays with a non-transparent τ*.
- General form (READING, the boundary for L-NEW's ODD-FREEZE). A gate at x cannot be closed at a state σ' and transparent at σ* when σ'
  and σ* agree off x. In Case 1 the two values are equal. In Case 2 the closing odd top becomes an Odd-won cycle through x.
  - CDAG's chain always contains such a pair: the state after a block's first step (m, m−1) agrees with σ* off the vertices the block
    later re-switches. At m = 3 that is S1 versus σ*, differing at 2 only.
  - A chain avoiding the obstruction must never revisit, off x, a configuration that agrees with σ* while x's switch is still closed.
    OPEN whether an exponential G_τ*-monotone chain with that property exists.
  - Gates other than single Odd masks (nested Odd choices on the reader) are not covered. The argument applies to each Odd choice that
    realises the closing value.

## DONE / FINDINGS / NEEDS
- DONE: N5 on dwN (τ anatomy); the Odd-reset reading; the masked-CDAG probe (n = 3 exhaustive, n = 4, 5 sampled).
- FINDINGS: (1) READING: in N5 an Odd bit that is an Even-closable cycle is set once and never reset, so τ freezes and the frozen run is
  G_τ*-monotone; this is the exact reason the R116 repeater has no N5 analogue on the Even side. (2) DATA: masked CDAG frozen runs 3/5/6
  at n = 3/4/5, far below the chain. (3) READING (§4, exact for single Odd masks at m = 3): σ-gating is possible, τ*-transparency is not; S1 and σ* agree off the gated vertex 2.
- NEEDS: none from the owner.
