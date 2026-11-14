# Box 145 N5-ENERGY: the threshold / Hopfield energy cast does not bound U. A direct threshold cast is DEAD (the one-step map is not unate: x3_L8, nest_d3_L4, g4_L12, lag2c_d4, up_d3); a cast with hidden units always exists but carries the β-weights 2^rank, so the energy bound is pseudo-polynomial = exponential (the parity → mean-payoff weight blow-up again). The model already HAS a Hopfield-type energy (VAL-MONO), and its level count is PATHS. Each triangular half alone is linear (PROVED, lane); the obstruction is the coupling of two OPPOSITE triangular orders, not triangularity
L-NEW successor 48, 2026-11-02 (date -u: see the commit). Lead GO 05:31Z (box 145, D18 cross-field: Goles-Olivos / Goles-Martínez threshold
networks and C-element circuit theory against C-ELEM / CHAIN-BACK). Labels: PROVED (lane), READING, DATA, DEAD.
G-N5-TIME, IDEAL-ACYC-POLY and U-LIN stay OPEN. Not a TARGET.md claim.

## 0. Answer
- Sources opened (notebook «Sources opened», box 145; quotes checked in the PDFs):
  - [GM89] E. Goles, S. Martínez, «Exponential transient classes of symmetric neural networks for synchronous and sequential updating»,
    Complex Systems 3 (1989) 589-597 (publisher PDF, complex-systems.com v03_i06_a03).
    - Theorem 1: for every n there is a SYMMETRIC threshold network with synchronous transient ≥ 2^(n/3).
    - Theorem 2: sequential updating, of order 2^(n/6).
    - Steady states have period ≤ 2 (cited there as [2], [3]).
    - The construction is recursive. Each new control cell's weights must exceed the sums over the earlier cells (conditions (2.8)-(2.16),
      p. 593-594), so the weights are super-increasing, i.e. exponential.
  - [SOA99] J. Šíma, P. Orponen, T. Antti-Poika, «Some afterthoughts on Hopfield networks», SOFSEM'99, LNCS 1725, 459-469,
    DOI 10.1007/3-540-47849-3_34 (self-archived accepted version, jyx.jyu.fi).
    - Theorem 1: any fully parallel computation of an n-neuron binary network with ASYMMETRIC weights that converges within t* updates
      is simulated by a symmetric (Hopfield) net of 6n + 2 neurons within 4t* steps, driven by a symmetric binary-counter clock.
    - §3: the energy gives an O(W) convergence bound in the weight size W, i.e. polynomial only for polynomial weights.
    - Theorem 2: in terms of the M-bit description, convergence is between 2^Ω(M^(1/3)) and 2^O(M^(1/2)). The upper bound counts the
      distinct ENERGY LEVELS (distinct subset sums of the weights).
  - [OBP13] L. I. L. Oliveira, V. C. Barbosa, F. Protti, arXiv:1311.6126 (k-reversible processes).
    - Lemma 2: the energy is monotone. Theorem 3: period ≤ 2. Theorem 4: transient ≤ E(t_max) + n − 1.
    - I used it only for the energy method's form; it reports the Goles-Olivos results [GO81 Inform. Control 51 (1981) 98-104; GO85
      DAM] that I did NOT open (paywalled).
  - C-element / speed-independent circuit theory (Muller-Bartky semimodularity, Brzozowski-Zhang): NOT opened. A search found no arXiv
    or DOI source I could read with a transient theorem, so I make no claim from that literature.
- (2) Is IDEAL-ACYC a threshold network?
  - DEAD (direct cast): «each mover's next state is a linear threshold function of the previous state».
    - The one-step map Φ is not unate. thr.py checks Φ_x on all 2^N states; a threshold function is unate in every variable and
      2-asummable.
    - x3_L8 (R188 exact pin): Φ_2 is neither increasing nor decreasing in s_3, its own sibling. Witnesses: raising s_3 from
      (1,1,0,0,1,1) raises Φ_2, and from (1,1,1,0,0,0) lowers it.
    - Also: 2 / 3 non-unate / non-2-asummable movers on x3_L8, 1 / 1 on nest_d3_L4 (R189), 5 / 6 on g4_L12, 6 / 7 on lag2c_d4, 1 / 2 on
      up_d3. Only lag1, lag1u and lag_min_d2 pass.
  - Cast with hidden units: always possible and useless (READING from [SOA99] Theorem 1).
    - C-ELEM writes x(t) = MAJ(A_x(t), B̃_x(t−1), x(t−1)), a threshold gate (weights 1, 1, 1, threshold 2; B̃ := x on a Ξ-tie).
    - A_x is the ladder's key logic and B_x a lexicographic comparison of two signed path sums, so both need hidden units.
    - With hidden units [SOA99] makes the whole run symmetric. But the comparison weights are the β-weights ±2^(4 + 2·rank + parity),
      so the energy bound O(W) is 2^Θ(n).
    - That is exactly the parity → mean-payoff blow-up (weights n^p), and [GM89] shows that super-increasing weights DO realise
      exponential transients in symmetric networks. An energy argument gives a polynomial bound only through POLYNOMIALLY many energy
      levels, never through symmetry alone.
  - The model's own energy: PROVED (lane), Proposition VAL-ENERGY.
    - The vector (Ξ_t(y))_y of current values is componentwise non-decreasing and strictly increases at some coordinate at every step
      (box 139 VAL-MONO).
    - So steps ≤ Σ_y (|{values Ξ(y) takes}| − 1) ≤ Σ_y (VX(y) − 1). This is the energy-level count of [SOA99] Theorem 2, and it is box
      139 PATHS summed.
    - It decreases (strictly) at every unchained step too, but its range is exponential at mid-ladder movers (TWO-SIDED). So it bounds U
      only by PATHS. The cast adds nothing beyond box 139.
- (3) Triangular weights: the Lead's premise is reversed.
  - PROVED (lane), Lemma TRI: a synchronous network in which unit i reads only units j < i and itself, and in which every unit under
    constant inputs enters its periodic orbit within c steps, has transient ≤ c·n. For a C-element with constant inputs, c = 1.
  - In IDEAL-ACYC each half is triangular:
    - A reads strictly LOWER levels in the same step;
    - B reads strictly π-LATER movers with one step of delay.
  - PROVED (lane), Corollary HALVES: if the A-inputs of x are constant on an interval, x moves ≤ 1 time there, and likewise for B
    (C-ELEM). So a run with frozen W-keys or frozen Ξ-faces has ≤ n_E steps.
  - Exponential transients need feedback. Here the feedback is the coupling of two triangular orders that run OPPOSITE ways (in the UP
    shape: A downward in level, B upward). This is the TWO-SIDED obstruction of box 140 in network language.
  - [GM89]'s symmetric exponential networks need symmetric FEEDBACK plus super-increasing weights, so their mechanism is not
    triangularity either.
- Net (READING): the energy literature turns «polynomial transient» into «polynomially many energy levels». For IDEAL-ACYC that is
  IDEAL-ACYC-POLY again: the trivial energy E(s) = −(remaining steps from s) has polynomially many levels iff runs are polynomial.
  - A useful energy must be a state function whose level count is NOT the number of Ξ-path values.
  - Candidate for a next box: E = Σ over levels of (number of split levels, ABSORB) weighted by π-position. It is untested; it would
    have to fall at every unchained step (CHAIN-BACK).

## 1. Proofs (PROVED, lane)
- Proposition VAL-ENERGY.
  - VAL-MONO (box 139): every mover's current face value is non-decreasing and strictly increases at each of its moves.
  - Every step has a mover. So the vector (Ξ_t(y))_y rises in the product order, strictly at every step.
  - A chain in a product of chains of lengths m_y has length ≤ Σ (m_y − 1). Each m_y ≤ VX(y) (box 139 PATHS: values are Ξ-path
    values). ∎
- Lemma TRI.
  - Induction on i. Units 1..i−1 are periodic from time c(i−1) on.
  - Unit i's inputs are then periodic, and by hypothesis it settles within c further steps.
  - For deg-2 C-elements with constant inputs, a unit moves at most once, so c = 1. ∎
- Corollary HALVES: from C-ELEM, between two moves of x both A_x and B_x flip. ∎
- DEAD witness: thr.py prints (x, j, s_up, s_down). Φ is the R178 §1 one-step map (box139/paths.py run(cap=1)) from every state, with Φ(s)
  = s at an «opt» or «stuck» state.

## 2. DATA
- Tool: experiments/new/box145/thr.py.

| genome | N | images of Φ | NONUNATE | NONASUM2 | witness (x, j) |
| --- | --- | --- | --- | --- | --- |
| x3_L8 (R188) | 6 | 30 / 64 | 2 | 3 | (2, 3) |
| g4_L12 (R188) | 8 | 61 / 256 | 5 | 6 | (0, 5) |
| nest_d3_L4 (R189) | 6 | 18 / 64 | 1 | 1 | (5, 0) |
| lag2c_d4 (R189) | 8 | 59 / 256 | 6 | 7 | (0, 2) |
| up_d3 (box 140) | 6 | 20 / 64 | 1 | 2 | (0, 3) |
| lag1, lag1u (R189), lag_min_d2 (box 142) | 6, 6, 4 | 3, 3, 4 | 0 | 0 | none |

## 3. Status
- DEAD: direct threshold cast (x3_L8: Φ_2 not unate in s_3).
- PROVED (lane): VAL-ENERGY (= PATHS as an energy-level count), TRI, HALVES.
- READING: a hidden-unit symmetric cast exists by [SOA99] Thm 1 but carries 2^rank weights, so its energy is pseudo-polynomial
  (exponential). [GM89] shows such weights do give exponential symmetric transients. Triangularity is not the obstruction; the opposite
  coupling is.
- NOT OPENED: Goles-Olivos 1981/1985 and the C-element literature (no claim made from them).
- OPEN: U-LIN, IDEAL-ACYC-POLY, G-N5-TIME.
