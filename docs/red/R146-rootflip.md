# R146: no kill of L-SI 35's Theorem ROOT-FLIP. Its proof checks out line by line (DESCENT forces the chain to a non-own Odd vertex with fixed Ξ, so it cannot end at an own-node or CN event), so a kill must break the SEL reading. An independent n5b check (corpus + 1.2M random games, tie-biased and unbiased) finds 0 violations. (b) A design for repeated release of ONE blocked closure via the sbq2 flip-flop exit is stated, not built
L-RED successor 34 (Opus 5.5; D1/D18). Lead 2026-10-30 20:00Z, R146: «(a) L-SI 35's Theorem ROOT-FLIP … Kill it if you can … try a tie flip
whose descent chain ends at an own-cycle-node or CN event instead of a value-changed flip. (b) L-NEW 39's adversarial form … make one
h_i-type exit flip σ̄ repeatedly inside ONE W-run with τ fixed, so that one W-better closure is Ξ-blocked and released super-linearly often.»
Written 2026-10-30 from 20:00Z (date -u). Labels: PROVED (lane) / DEAD / DATA / READING. Not a TARGET.md claim. G-N5-TIME OPEN.
Sources opened: l-si aeb8c311 docs/si/N5-SBF-box53.md §2.1-§2.5 (SEL, NOCLOSE, TIE, DESCENT, ROOT-FLIP); l-new 185422e0
docs/new/N5-TAU-box96.md §0-§3 and NEEDS.

## 1. (a) ROOT-FLIP: the proof, read against the Lead's kill idea (READING, checked step by step; not refereed)
- The Lead's idea was a tie flip whose descent chain ends at an own-cycle-node or CN event. DESCENT (§2.4) excludes exactly that:
  - The first divergence w of the old and new key paths of t ∈ {t1, t2} satisfies Ξ_k(w) = Ξ_(k+1)(w) with cycle node c ≠ w. So w is
    non-own at both times.
  - w is not Even: an Even switch at w would raise Ξ(w) strictly, by ⊕ injectivity on paths that avoid w.
  - So w is a non-own Odd flip with ℓ(w) < ℓ(o), and the induction ends only at a flip whose old target's Ξ changed. Own-node flips and
    CN switches can START a cascade, but cannot be its root in ROOT-FLIP's sense.
- So a counterexample must break a premise, and the only premise not already landed or lane-proved is SEL. SEL is the reading that
  Claim RG′ and T54's LEX-BFS / IDX-MONO transfer to S1's own evaluate(σ_k).
  - Where it could break: SEL-O needs queue order within a BFS layer = lex order of path keys, with the tree parent of an Odd vertex
    equal to σ̄_k(x). In n5b's evaluate_choice, the BFS scans sorted(hp[y]) and sets choice[x] at first discovery, so both hold by
    construction in this engine.
  - SEL-E needs the longest() recursion's first strict maximum in sorted successor order, and that holds too.
  - I found no gap.
- DATA (flipev/rootflip.py on L-COMP's n5b SPEC, independent of L-SI's rootflip.py on n5x), every transition, not only W-runs:
  - corpus (flipev/runroot.sh, 1132 runs, 300 s each; n3cov_lean / n3cov_phi have partial starts, R99): 7,485 transitions with non-own
    flips, 24,530 non-own flips, 2 tie flips (L-SI also reports 2, in nep22f_n64), BAD 0;
  - random (--rand, n 10-20, out-degree 1-3, default start): seeds 2 and 3 tie-biased (vertex 0 Odd, top odd priority), 400k games each,
    207,763 + 208,675 non-own flips, 178 + 175 ties, BAD 0. Seed 4 unbiased, 400k games, 231,646 flips, 137 ties, BAD 0.
  - Total 1.2M random games, 648,084 non-own flips, 490 tie (descent) flips, 0 violations.
  - The three FLIP-EV kill instances (flipev_n10, flipevr_n10, L-SI's flipev_n20) each contain a tie flip (TIE 1) whose root is a
    changed-target flip. BAD 0 on all three.

## 2. (b) One closure blocked and released many times in one W-run: a design (READING; not built)
- Ingredients from R145 §3: the degree-2 root of sbq2_K8_m16 is an h_i-type exit. τ(root) = obs, and σ̄(root) alternates obs / obs1 at
  every wave step, K·m times in ONE W-run with τ fixed.
- Closure (y, z) with z's Ξ-play through the root: Ξ(z) = min(Ξ(obs), Ξ(obs1)) + μ_z, while W(z) reads τ(root) = obs.
  - If y's alternative h reads obs with marker μ_h < μ_z, then the phases alternate between blocked (W-better, Ξ-worse) and offered. But
    W(z) − W(h) = μ_z − μ_h is fixed, so after the first adoption y never leaves z: one release only.
- What repeated releases need: rel2's three-signal pattern (h_i < a_(i+1) < b_i < h_(i+1)) supplied by waves instead of fresh chains.
  - Ξ(z) must cross Ξ(h) upward twice per round, and W(h) must cross W(z) upward once per round, which lets y leave.
  - So y's alternative must carry a signal whose W-value rises past W(z) between releases, i.e. a second exit flipping in anti-phase on
    the W side.
  - Per round this is R144's accounting: each round costs one wave of length m, so releases of one edge ≤ K·m/const, quadratic at best.
    That is still only quadratic, as with SB and ΞCH.
- Not built within this context budget. It is the resume point for successor 35 (notes/L-RED.md).

## DONE / FINDINGS / NEEDS
- DONE: flipev/rootflip.py, flipev/runroot.sh, outputs; this note; notes/L-RED.md PARK section.
- FINDINGS:
  1. No kill of ROOT-FLIP. The proof checks out; DESCENT rules out own-node or CN roots. Independent n5b data: corpus 24,530 flips and 1.2M random games (648,084 flips, 490 ties), 0 violations.
  2. READING: repeated release of one closure needs a W-side anti-phase exit. Each release costs a wave, so it tops out at quadratic.
- NEEDS: none from the owner.
