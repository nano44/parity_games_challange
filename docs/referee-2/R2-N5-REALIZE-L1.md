# R2-N5-REALIZE-L1: REFEREE-2 word-diff of P-N5-REALIZE line L-1 against the frozen line, and check of fixes entry 1
Referee: REFEREE-2 successor 26, Opus 5.5 (D15). Written 2026-11-02 (date -u; see the commit). Verdict: **MATCHES**.

## 0. Object
- Commit: claude/l-red 02dfc35cb9804d171b1db809d4bd79713255b8ec, an ancestor of origin/claude/l-red. I re-hashed every file at that commit:

| file | sha1 at 02dfc35c | check |
| --- | --- | --- |
| docs/red/P-N5-REALIZE.md (frozen packet) | 067f06b6c67969adf346621b4a92b253491ab2b9 | untouched ✓ |
| docs/red/P-N5-REALIZE-line.txt (frozen line) | 53dd6e9fd727a6ff2d5e49648366f28d7398e9d9 | untouched ✓ |
| docs/red/P-N5-REALIZE-fixes.md | 864cad5978cb79f7c73c6ba99cff8202fe34cc5b | = Lead's sha1 ✓ |
| docs/red/P-N5-REALIZE-line-L1.txt | 1d72ee310b9b4af252724e06a181221a9c2828ec | = Lead's sha1 ✓ |

- Sizes: frozen line 3,839 bytes, L-1 4,579 bytes. Each is one line with no heading marker.

## 1. Word-diff (token diff, then a byte test)
- Method:
  - Token diff: `git diff --no-index --word-diff=plain --word-diff-regex='[^[:space:]]+'`, plus a difflib opcode pass on space-split
    tokens to read each change in context.
  - Byte test: start from the frozen line, apply exactly the 8 replacements below, each of whose old phrases occurs exactly once,
    and compare with L-1: **True**.
- So L-1 = frozen line + these changes, nothing else:

| # | old (frozen) | new (L-1) | item | ✓ |
| --- | --- | --- | --- | --- |
| 1 | «(1E-N3: at a non-fallback transition j − 1 → j, σ_j is a pointwise optimum of the one-player arena in which Even y keeps {σ_(j−1)(y)} ∪ Iσ_(j−1)(y) and Odd follows τ_(j−1)),» | «(1E-N3: «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance», RESULTS R57 (b), read on every valid input of S1's procedure (Lead reading L45, RESULTS R102), used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima; and S4a's σ_new, S1's output on the dual of the one-player arena in which Even y keeps {σ(y)} ∪ Iσ(y) and Odd follows τ, is a pointwise optimum of that arena, before S4c),» | REFEREE-2 REAL-L1 | ✓ |
| 2 | «symmetric difference and its parity;» | «symmetric difference: the option whose set contains that β is the better one if its parity is even and the worse one if odd;» | REFEREE-2 REAL-L2 | ✓ |
| 3 | «unused even self-loop of priority 2; » | «… priority 2; c_W's priority top is the least even number at least 2 above every other priority so far; » | REFEREE optional «top» | ✓ |
| 4 | «(Even, top + 3) → {K1, K2})» | «… {K1, K2}; vertex indices: movers, gates in gate-index order, β-vertices, e-vertices in the order of their gates' gate indices, the unused loop, c_W, K0 to K3 (packet §3.1), on which the root-first key comparison depends)» | REFEREE REAL-L1 | ✓ |
| 5 | «β → Ξ-target,» | «β → its Ξ-target (u when the target is X),» | REFEREE-2 P-1 | ✓ |
| 6 | «fallback at transition L(G) + 1, so [0, L(G)]» | «…, so, if L(G) ≥ 1, [0, L(G)]» | REAL-P2 / P-2 | ✓ |
| 7 | «of length exactly L(G);» | «… L(G) (no FL run if L(G) = 0);» | REAL-P2 / P-2 | ✓ |
| 8 | «(2026-11-02)» | «(2026-11-02; revision L-1 2026-11-02)» | date tag | ✓ |

This is exactly L-RED's list of six items (fixes entry 1, «Line L-1»): its items 1 to 6 are my rows 1, 2, 3+4, 5, 6+7 and 8.

## 2. Content checks of the new text
- **Row 1 (my REAL-L1).**
  - The quote «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance» is verbatim in trunk RESULTS: R102's
    heading (l. 9478) and body (l. 9737, citing R57 l. 2915-2916).
  - P1 is named: S1's σ̄, and τ̄ on the dual game.
  - P2 is named in the σ_new-before-S4c form, the form G-REAL-1 (b) needs.
  - «{σ(y)} ∪ Iσ(y) … τ» is now unindexed, correctly: the state is that of the S4a call.
  - Met.
- **Row 2 (my REAL-L2).** «better … if its parity is even». This agrees with packet §2 Fact X («parity 0 and lies in B_s(x, k)») and
  with Ω(β) = 6 + 2br + bp. Met.
- **Rows 3-4 (REFEREE REAL-L1).**
  - The layout matches §3.1: movers 0..N−1; gates N + gate(x, k); β; e in gate-index order; c_X; c_W; K0..K3.
  - «top» matches §3.1 («the least even number ≥ 2 + max Ω so far»).
  - The β-vertices' own order is left to «(packet §3.1)». I checked that it is immaterial: my MUT=border control reverses the β
    indices (logs/run2_border.log). On the 7 champions (L 17 to 64, sum 296, unchanged), 100 perturbed and 200 random acyclic genomes:
    0 violations.
  - The reason: β-vertices are leaves of S1's BFS on dual(H) (gates take e in H), and they lie on no mover's root-first key.
  - The e-order is what matters: MUT=eorder breaks it (R2-N5-REALIZE Addendum 1).
  - Met.
- **Rows 5-8.** Correct and harmless: a β with target X has only u; the L = 0 case agrees with §4 under the fixes reading.
- **L41 / L43 / L44 / L46 tags unchanged.** The CF-1 citing line «RESULTS R24 (a) Lemma R and R24 (b)'s choice rule (TB proof steps 1,
  3-5; fixes §2.3) with bridge B, whose proof uses no 𝒞^1O hypothesis (Lead reading L46 and its amendment)» is byte-unchanged, which
  REFEREE REAL-P1 allows («Keep the CF-1 line»). No DEAD; nothing referee-originated.

## 3. Fixes entry 1 (864cad59)
- It quotes my items accurately: REAL-L1, REAL-L2, G-REAL-1 (a)/(b), P-1, P-2, N-1, N-2.
- The G-REAL-1 reading of §1 is the repair I asked for:
  - [1E-N3] = R57 (b) on every valid input, in forms P1 / P2;
  - [RULE]'s «σ_j(x)» reads «σ_new(x) (= σ_j(x) at a non-fallback transition)»;
  - no lemma changes.
  - Correctly labelled «closed by landed results; no new proof».
- REFEREE REAL-P1's reading (bridge B part redundant; Lemma R + TB essential for «σ_new(x) is κ-least»):
  - consistent with my report;
  - my §3 direct trace is an alternative at standard states, not needed;
  - «essential» is right as a statement about the packet's own proof.
- REAL-P3 (finiteness, not circular) agrees with my §4 note.
- The joint REQUIRED list is met: REFEREE REAL-L1, REFEREE-2 REAL-L1, REFEREE-2 REAL-L2.
- Nothing outside the listed items changed in the line.

## Verdict
**MATCHES.** L-1 (1d72ee31) differs from the frozen line (53dd6e9f) by exactly the six listed items. The three REQUIRED items are met.
The optional ones taken are correct. My signatures in R2-N5-REALIZE.md stand for the packet read with fixes entry 1.

## DONE / FINDINGS / NEEDS
- DONE: word-diff and byte test (True); fixes entry 1 checked; MUT=border control added to realize_check.py.
- FINDINGS:
  - L-1 MATCHES.
  - The β-vertex index order is immaterial (control: 0 violations). Only the e-order matters, and L-1 states it.
- NEEDS: none from me.
