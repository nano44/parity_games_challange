# N5-QRET (box 99): one mechanism behind the quadratic Even-edge returns. In sbq2_K8_m16, obs_K12_m24 and latew_K16_m32 every return is FREE (box 84: REG 0, E0 0). Every return traces back to a FRESH Even entry. The dominant roots are the K fresh ticks of ONE clock vertex (vertex 4, out-degree K + 1, walking monotonically through its successors, period m + 3), and each tick roots ≈ 3m returns. Theorem CASCADE-EQ (PROVED, lane, modulo one case of FRESH-ROOT): WRUN-POLY ⇔ «returns rooted at one fresh entry are polynomial». CONJECTURE CASCADE-LIN: ≤ n/2 (corpus max 0.483n, 9,455 returns, every root FRESH; the depth figure in §2.4 / §3 is CORRECTED in box 100)
L-NEW successor 40 (Opus 5.5), D14 / D18, Lead reading L40. Lead 21:21Z: «BOX 99: the REG/FREE classification of latew_K16_m32's 496 return
transitions. Which targets g are re-entered, how often per g, and what raises Ξ(g) between consecutive entries … Do the same on sbq2_K8_m16
… and obs_K12_m24 … Goal: identify the ONE mechanism … If so, state it as a lemma candidate («each Ξ-rise at a re-entered target g is caused
by …») that a proof could charge.» Written 2026-10-30 21:22Z-21:3xZ (date -u). Working note, unrefereed. Labels: PROVED (lane) / CONJECTURE /
DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN; no W-run count is bounded here.

## 0. Sources, tools
- Box 92 packet P-N5-WRUN (R95 draft, line L-5), signed by both referees: the return definition («a return of X to g is a transition of F at
  which X enters g having held g at an earlier state of F»), REG / E0 / FREE (§4.1), TRIPLE-RED, and RET-ΞRISE («RET_F(X, g) ≤ ΞCH_F(g)»).
- Box 98 (N5-RET-box98.md): Lemma PAY and the fresh / return split.
- L-SI box 53 (l-si aeb8c311): Lemma TIE, used in §2 (d).
- Box 84 retclass.py (REG / E0 / FREE, re-run unchanged).
- New: experiments/new/box99/retcause.py, runcause.sh, cause_sbcg.txt / cause_alt.txt / cause_pins.txt. Pin: new/check.sh «box 99 QRET».
- Counting unit. Box 98's RETT_F counts TRANSITIONS with a return (latew 496). Here «returns» counts return ENTRIES (Even X re-entering g),
  so several per transition (latew 1,922).

## 1. DATA: the three quadratic pins
| pin | n | |F| | return entries (transitions) | REG / E0 / FREE (box 84) | re-entered edges = targets g | max returns per g | clock ticks (vertex 4: out-degree, switches, all fresh, period) | returns per tick |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sbq2_K8_m16 | 261 | 152 | 450 (120) | 0 / 0 / 450 | 60 | 8 = K | deg 9, 8, yes, 19 = m + 3 | 45 = 3m − 3 |
| obs_K12_m24 | 272 | 324 | 818 (289) | 0 / 0 / 818 | 72 | 12 = K | deg 13, 12, yes, 27 = m + 3 | 71 |
| latew_K16_m32 | 482 | 560 | 1,922 (496) | 0 / 0 / 1,922 | 124 | 16 = K | deg 17, 16, yes, 35 = m + 3 | 93 = 3m − 3 |
- Every re-entered edge has its own target g: the counts of re-entered edges and targets coincide. Each g is re-entered at most K times,
  i.e. once per clock tick.
- What raises Ξ(g) between consecutive entries (the first divergence of g's (σ, σ̄)-play at the rise; retcause.py):
  - Mostly an Even switch of vertex 4 itself (sbq2 240 of 653 rise classifications, obs 288 of 1,324, latew 992 of 2,837).
  - The rest are Even switches of the gadget's own vertices (e.g. 119, 122, … in sbq2: 14 each), or Odd flips inside the gadget (sbq2
    170: 171 ↔ 122, 7 each way; latew 330: 331 ↔ 234, 15 each way). These trace back to vertex 4's tick in one step (chain depth 1).
  - W(g) also changes in every return window (450 / 818 / 1,922 of the returns).
  - GXC / TXC events were not measured here.
- Vertex 4 is Even with priority 348 / 508 / 668 (sbq2 / obs / latew). Its successors are visited in increasing index order, each once.
  So each tick is a FRESH entry (box 98 sense).
- MECHANISM (DATA, the same in all three families): ONE Even «clock» vertex of out-degree K + 1 advances K times by fresh entries, every
  m + 3 transitions. Each advance raises Ξ at the ≈ m observer targets whose plays pass through the clock (e.g. in sbq2 the targets 121, 124, …; 121
  is an Odd vertex whose only successor is 4), and every observer gadget re-enters its edges once (≈ 3 return entries per gadget). So
  |F| ≈ K(m + 3), and return entries ≈ K·3m. This is L-RED's reactor / observer construction read through the return lens. L-COMP 8's
  R*_F = K·m on latew (Lead 21:21Z) is the same product.

## 2. Lemma FRESH-ROOT and Theorem CASCADE-EQ
### 2.1 The canonical root
- Fix a W-run F.
- For a return of Even X to g at k → k + 1, let j be the last state of F before k + 1 at which X held g, and q₀ the FIRST transition in
  [j, k] at which Ξ(g) changes. RET-ΞRISE's proof gives such a q₀. DATA: norise 0.
- For a change of Ξ(z) at q → q + 1, the FIRST DIVERGENCE is the first vertex x on z's (σ_q, σ̄_q)-play (followed until it repeats a
  vertex) whose successor differs at q + 1. It exists, because Ξ(z) is a function of that play.
- root(q, z):
  - (c) x is Even (σ switched at x):
    - if the entry (x, σ_{q+1}(x)) is FRESH, root := that entry;
    - otherwise it is a return of x at q, and root := the root of that return (its window ends at q, so the recursion goes strictly back
      in time).
  - (d) x =: o is Odd, flipping a → b: root := root(q, a). This needs Ξ(a) to change at q → q + 1.
- The ROOT of a return is root(q₀, g).

### 2.2 Lemma FRESH-ROOT (PROVED, lane, in the cases stated; DATA for the rest)
- Statement. root is total on returns, and its value is a fresh entry at a transition ≤ k.
- Proof.
  - (c) recurses on a return whose window lies strictly before q. Time decreases, so the recursion stops, and it can only stop at a
    fresh entry.
  - (d), the case where o is non-own at q and at q + 1 and the common prefix P = (z, …, o) lies off the cycles of both plays:
    - Ξ_q(z) = P ⊕ Ξ_q(o) and Ξ_{q+1}(z) = P ⊕ Ξ_{q+1}(o), by (⊕) (L-SI box 53 §2).
    - So Ξ(o) changes. If Ξ(a) did not change, L-SI's Lemma TIE gives «Ξ(o) and Ξ(t2) are fixed», a contradiction. So Ξ(a) changes.
    - a's play at q is the suffix of z's play after o, so the next first divergence lies strictly further along z's play at q. Hence
      the (d)-steps at one q are at most n.
- NOT proved: (d) when the prefix meets a cycle, and (d) when o is its own cycle node. There the decomposition Ξ(z) = P ⊕ Ξ(o) can fail.
  DATA: on the corpus (§3) every one of 9,455 roots is FRESH, with no TIE, LOOP or CYC root. So these cases never blocked the chain.
  - The 9 «CYC» roots of the first run were a tool bug: the walk stopped at the old cycle node and missed divergences on the cycle. They
    are fixed and FRESH now.

### 2.3 Theorem CASCADE-EQ (PROVED, lane, given FRESH-ROOT)
- Statement. For a fresh entry e of F, let CASC_F(e) := the returns of F whose root is e. Then:
  - Σ_{X, g} RET_F(X, g) = Σ_e CASC_F(e);
  - the number of fresh entries is ≤ m_E − n_E;
  - |F| ≤ (m_E − n_E)(1 + max_e CASC_F(e)) (Lemma PAY);
  - so WRUN-POLY ⇔ CASC-POLY := (max_e CASC_F(e))-POLY.
- Proof.
  - ⇒: CASC_F(e) ≤ Σ RET_F ≤ n_E·|F|.
  - ⇐: by PAY, |F| ≤ (m_E − n_E) + RETT_F ≤ (m_E − n_E) + Σ_e CASC_F(e). □
- This is a REDUCTION, like box 92's list. Its use: the quadratic pins have CASC linear (3m − 3 ≈ 0.2n), fresh roots linear (K), and
  nothing else.

### 2.4 CONJECTURE CASCADE-LIN and the charge a proof would need
- CONJECTURE CASCADE-LIN: in every W-run, every fresh entry roots at most n/2 returns.
  - It would give |F| ≤ (m_E − n_E)(1 + n/2), so WRUN-POLY with an O(n·m_E) bound.
  - DATA: max CASC / n = 0.483 (switchbestexp_2, n 60: 29). Then fcobs_3 0.477, fc_3 0.471. The quadratic pins: 0.17 / 0.26 / 0.19.
- Lemma candidate in the Lead's form: «each Ξ-rise at a re-entered target g is caused (first divergence, then the root chain) by a fresh
  Even entry, at depth ≤ 2. In the quadratic families it is a tick of one clock vertex on g's play.» The part a proof would have to charge
  is the cascade size: why one fresh entry re-opens each target at most O(1) times. In the pins it is exactly once per observer per tick.
- Why this is the right target (READING):
  - An exponential W-run would need a counter.
  - With canonical roots, a counter's lower bits re-enter because of higher bits' RETURNS. That means chain depth ≥ 2 repeated, and a
    cascade that grows with the depth.
  - The corpus has chain depth ≤ 2 (8,738 / 709 / 8 returns at depth 0 / 1 / 2). CORRECTED in box 100: false, a tool bug; depth
    reaches 49 on topfix_N (width 1 there).
  - L-RED kill target: one W-run whose root chains have unbounded depth, or one fresh entry rooting > n returns.

## 3. DATA: corpus (runcause.sh, 2026-10-30 21:2xZ by date -u)
- Scope: box 50b's corpus (719 sbcg + 413 alt) + 3 pins. 602 W-runs with returns, 9,455 return entries. 0 errors, 0 timeouts at 300 s.
- Root kinds: FRESH 9,455. Chain depth: 0 for 8,738, 1 for 709, 2 for 8.
  - CORRECTED in box 100 (N5-CASC-box100.md §2.3): these depths were a tool bug (absolute-depth memo). The true depths reach 49
    (topfix_N). Roots and CASC are unaffected.
- Largest cascades: latew 93, obs 71, fc_8 / switchbestexp_8 66 (n 135 / 148), topfix_n10 50.
  - topfix_N grows linearly: 8, 14, 26, 38, 50 for N = 3, 4, 6, 8, 10.
- Largest CASC / n: 0.483.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box99/ (retcause.py, runcause.sh, cause_*.txt); new/check.sh «box 99 QRET». SHA: see the commit.
- FINDINGS:
  - DATA: the quadratic returns are all FREE. They are rooted at the K fresh ticks of one clock vertex (out-degree K + 1, period m + 3),
    ≈ 3m returns per tick. It is the same mechanism in sbq2, obs and latew.
  - PROVED (lane): FRESH-ROOT in the cases (c), and (d) with a non-own flip off the cycles (DATA for the rest: 9,455 / 9,455 FRESH).
    CASCADE-EQ: WRUN-POLY ⇔ CASC-POLY.
  - CONJECTURE CASCADE-LIN: CASC ≤ n/2 (max 0.483n). It would give |F| ≤ (m_E − n_E)(1 + n/2).
- NEEDS: Lead: route CASCADE-LIN (or the depth target, §2.4) to L-RED for a kill attempt.
