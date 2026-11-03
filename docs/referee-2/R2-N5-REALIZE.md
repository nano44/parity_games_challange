# R2-N5-REALIZE: REFEREE-2 report on P-N5-REALIZE (L-RED 45): Fact DUAL, Fact X, Lemmas K, PLAY, SBAR, TAU, ESC, W, KEY, Theorem REALIZE, Corollary REAL-IDEAL
Referee: REFEREE-2 successor 26, Opus 5.5 (D15). Written 2026-11-02 (date -u; see the commit).
Independence:
- I wrote this without opening docs/referee/ for this packet. At 04:03Z, `git ls-tree` on origin/claude/referee listed 0 files matching «realize».
- I did not import any lane script.
- I did read r187/stab.py build() before writing my builder, for the JSON field order opts[x][k] = [wt, xt, b]. My builder is written
  from packet §3.1, and BUILD compares it byte-for-byte with the four pins.
- I opened pinck.sh, realck.py and t2.py only to run them.

## 0. Object
- Packet: docs/red/P-N5-REALIZE.md at claude/l-red e609c5d2c689e87c1dc658e5e65a956fe0478222. sha1 067f06b6c67969adf346621b4a92b253491ab2b9,
  278 lines. Re-hashed: match. e609c5d2 is an ancestor of origin/claude/l-red.
- Line: docs/red/P-N5-REALIZE-line.txt, sha1 53dd6e9fd727a6ff2d5e49648366f28d7398e9d9. Re-hashed: match.
- Premises opened:
  - SPEC docs/new/N5-ssi-global.md: S1-S5, FIX 2-4, Q1-Q4.
  - RESULTS R57 (1E-N3; its two forms P1/P2 as quoted in R68 / R72 entries, RESULTS l. 3461, 3595, 5918), R102 (S4B-OPT, its 1E-N3 quote),
    R103 (citing line, (R1), FL definition, bridge B), R15 (termination).
  - DECISIONS L41-L46 with L46's Amendment. docs/lit/T21-VJ00-check.md («Unaffected: a stop with no improvement is optimal: BRICS Lemma
    5.8 "1 ⇒ 2"»).
  - My predecessor's R2-N5-ANCHOR.md (the (R1) ruling, G-ANC-1).

## 1. Verdict table
| § | item | verdict |
| --- | --- | --- |
| §1 | Fact DUAL | **SIGNED** |
| §2 | Fact X | **SIGNED** |
| §3.2 | Lemma K (a)-(d) | **SIGNED** ((c) uses P1 on G^d, see G-REAL-1 (a)) |
| §3.3 | Lemma PLAY (a)-(c) | **SIGNED** |
| §3.4 | Lemma SBAR | **SIGNED**, with G-REAL-1 (a) (P1 used, not named in §1; covered by the landed 1E-N3) |
| §3.5 | Lemma TAU | **SIGNED** (P1 on G^d, G-REAL-1 (a)); its proof uses no acyclicity (my data: I_τ = ∅ at state 0 on all 294 Ξ-cyclic probes) |
| §3.6 | Lemma ESC | **SIGNED** |
| §3.7 | Lemma W (i)-(iii) | **SIGNED** |
| §3.8 | Lemma KEY (a), (b) | **SIGNED** |
| §4 | Theorem REALIZE | **SIGNED**, with G-REAL-1 (b): proof text applies [1E-N3] / [RULE], stated for σ_j at a non-fallback transition, to S4a's σ_new before the transition is known to be non-fallback. Closed by landed items (§2 below), and a second time directly from SPEC S1's text (§3 below). No new proof; L41 not triggered |
| §5 | Corollary REAL-IDEAL (a) NECESSITY, (b) TRANSFER | **SIGNED** |
| §1 | premise [VJ-LOC] | only «1 ⇒ 2» is used (SBAR (ii)); K (d), ESC, TAU use only the definition of a pointwise optimum / P1. ✓ |
| §1 | premise [RULE] | citing line verbatim = RESULTS R103's. Bridge B's conclusion is Lemma W (iii), signed here, which is what L46 asks of a citing packet («bridge B … is signed in the citing packet»). ✓ |
| §6 | scope (acyclic only) | checked; the §6 DATA is reproduced exactly. Every use of acyclicity is listed correctly |
| §7 | DATA labelling | checked; every row reproduced exactly; one imprecise ratio (N-2) |
| line | P-N5-REALIZE-line.txt | **REQUIRED**: REAL-L1 (1E-N3 gloss), REAL-L2 (parity direction of the IDEAL order). Precision P-1, P-2 |

Joint gap map on my side: G-REAL-1, minor, a proof-text / premise-statement gap, CLOSED by landed items. Nothing is open on the signed items.

## 2. G-REAL-1: premise restatement narrower than its use (minor; closed)
§1 says «Premises (named; nothing else is used)» and restates [1E-N3] as «at a non-fallback transition j, σ_j is a POINTWISE OPTIMUM of
H_(j−1)». That is form P2, restricted to σ_j at non-fallback transitions. The proof uses more:
- **(a) P1 is used but not named.** P1 = «S1's σ̄ is Odd's pointwise optimum in G_σ» (RESULTS l. 3461 «in two forms … P1, … P2»).
  Where it is used:
  - SBAR (ii): [VJ-LOC] gives «ρ is optimal». The conclusion «φ = Ξσ» needs Ξσ, the value of S1's σ̄, to be THE optimal value: P1.
  - SBAR (iii): «SPEC's σ̄ is optimal, so φ_(σ,σ̄) = Ξσ = φ».
  - TAU and K (c): «τ̄ maximises Γ's order» is P1 on G^d.
  The same packet's §1 «Ξ_j := … OPTIMAL counterstrategy σ̄_j, … SPEC S1» reads it into the definition, which is SPEC's text. That S1's
  procedure achieves it is exactly the premise. It is covered by 1E-N3 as landed: R57 (b) «that S1's procedure realises an optimal σ̄ is
  VJ00 §6 plus SPEC conformance», read on every valid input (L45, R102).
- **(b) σ_new before S4c.** REALIZE's step j < L applies [1E-N3] and [RULE] to σ_new at transition j + 1. That transition being
  non-fallback is what the step concludes, so this is circular against the §1 form. At step L, transition L + 1 IS a fallback.
  - At L + 1 only, the stated form is enough by contradiction: if L + 1 were non-fallback, σ_(L+1) = σ_new = σ and τ_new = τ, so S4c
    would fire.
  - At j < L it is not enough. A fallback at j + 1 leaves σ_new unconstrained by the §1 form.
  - The landed premise covers σ_new itself:
    - R102 / L45: «the Odd strategy that S1's procedure outputs for σ* on G* is a pointwise optimum against σ* in G*», for every finite
      game graph. S4a's σ_new is, by SPEC S4a's text, S1's output on dual(H) for τ. This is P2 in the form RESULTS l. 5918 quotes:
      «S4a's σ_new is Even's one-player optimum of H_t».
    - [RULE]: TB steps 1, 3-5 describe the output of one S1 call on dual(H) (my predecessor's (R1) ruling, R2-N5-ANCHOR §2, landed in
      R103). That output is σ_new whatever S4c does afterwards.
- Repair (wording; the lane writes it into the fixes file):
  - §1 [1E-N3] should state both forms: (P1) S1's σ̄ (and τ̄ on G^d) is a pointwise optimum; (P2) S4a's σ_new, S1's output on dual(H),
    is a pointwise optimum of H at every transition with Iσ ≠ ∅, before S4c.
  - [RULE]'s «σ_j(x)» should read «σ_new(x) (= σ_j(x) at a non-fallback transition)».
- §3 gives an independent closure of (b) that needs neither P2 nor [RULE].

## 3. A direct reading of S4a in the standard state (my check of REALIZE's σ-step; no premise)
SPEC S4a defines σ_new as S1's procedure on dual(H) against τ_0. I traced that procedure at a standard state (dual priorities Ω + 1; S1
processes vertices by increasing dual reward):
1. **K0 comes first** (the G-even vertex of largest p′). It is not a cycle node. In H it keeps {K1, K3}; K3 outranks it; K1 keeps only
   K1. So it is skipped.
2. **c_W comes second.** It is a self-loop. R(c_W) = the movers, the gates (τ_0 to e), the e-vertices, and the β with a mover target
   (via xt). K is closed, so K0 and K3 are not in R. No vertex of R outranks c_W, so step (iii) deletes nothing.
3. **BFS from c_W.** Ω_d(c_W) is odd, so (iv) takes the SHORTEST path: BFS from c_W, FIX 4. Each G-Even vertex of R gets its
   discoverer:
   - β with targets {xt, u} gets xt (u is not in R). This is Lemma ESC.
   - Within one BFS layer, discovery order is the lexicographic order of root-first index keys (induction on layers: order by the
     discoverer's position, then by own index).
   - So every mover gets the R(x)-gate with the least root-first key under the σ_new / τ_0 tree. This is [RULE] with KEY (b).
4. **K2 comes later** (a cycle node, Ω_d 4 even). R(K2) = {K2, K3, K0, β with target X}. Step (iii) for K3, then K0, leaves K0 → K3
   as K0's only edge inside R. (iv) LONGEST gives σ_new(K0) = K3. This is Lemma K (d). K1 (self-loop) and K3 (one H-edge) keep σ.
So REALIZE's σ-step holds at every standard state from SPEC's text alone, whatever S4c does afterwards. My tool checks it (RULE, ESC,
IDEAL counters below). P1, for Ξσ and Ξτ in SBAR / TAU / KEY (a), remains a premise: the standing one.

## 4. Review notes (paper check, item by item)
- **Fact DUAL.**
  - Ranks agree, since (Ω + 1, v) orders as (Ω, v).
  - p′ > p′(c) ⟺ rank > rank(c), parity-free.
  - x ↦ −x − 1 is decreasing.
  - Signed weights flip.
  - The length rule swaps with c's parity.
  - So Iτ(v) = {w ≠ τ(v) : Ξτ(w) ◁ Ξτ(τ(v))}. ✓
- **Fact X.**
  - The chain of (x, k) contains b(x, k).
  - Every later chain element is an option of a mover reachable from x by ≥ 1 Ξ-edge. Acyclicity makes that mover ≠ x, and b is a
    bijection, so b(x, k) ∉ B_s(x, k′).
  - The top-of-symmetric-difference rule is SPEC Q1. ✓
- **Lemma K.**
  - (a) is read off the plays.
  - (b): K0's switch to K1 removes K3 (odd) from P: improving. K1 → K0 adds K0, K3, and the top (K3) is odd: not improving.
    K3 → K1 is the shorter path to an odd node: not improving. ✓
  - (c): K1 → K0 → K1 is an even cycle (node K0), so Even's optimum at K1 has reward ≥ p′(K0) > 0 > −p′(K2). ✓
  - (d): the H-plays from K0 end in K1 (Ω 5) or K2 (Ω 3), and −p′(K2) > −p′(K1). K0 is on no H-cycle. ✓
- **Lemma PLAY.**
  - Under ρ no gate takes an e-face. So the play from β_g is the X-chain, then u, K0, K3, K2, K1.
  - From e_g (lev ≥ 1): e_g, wt(g), g′, β_(g′), …. This may pass x, the owner of g, again (x →W m →Ξ … x is allowed: only the Ξ-graph
    is acyclic). It then leaves x by σ(x) and its β, never by e. So e_g occurs once and the P-set is {e_g} ∪ B(g′) ∪ {K0, K3}. ✓
- **Lemma SBAR.**
  - (i): e_g outranks every β and is even. lev 0: even c_W against odd K1. K2: the longer play to the odd K1 is better for Even. ✓
  - (iii): an own-cycle through g and e_g lies outside K, c_W, c_X. Its top is an e-vertex (even), against K1. Off-cycle, the P-sets
    (lev ≥ 1) or the cycle nodes (lev 0) differ. ✓
- **Lemma TAU.**
  - Every play from e_g ends at c_W: movers have only gate edges, τ takes e, and levels drop.
  - From β_g, Even has β_g → u → K0 ⇄ K1 (ESC edge; for target X it is the only edge).
  - The rewards differ strictly: p′(K0) > p′(c_W). ✓
- **Lemma ESC.** In H every play from xt(g) ends at the even c_W, and from u at an odd node (K (d)). β is on no H-cycle, since gates
  take e in H. Iσ(β) may contain u; then R(β) = {xt, u} and xt is chosen. ✓
- **Lemma W.**
  - The play from a level-ℓ mover takes three steps per level, through vertices below c_W, so P = ∅.
  - (ii) holds for every H-play: movers' options are gates, gates take e, and e has one edge.
  - (iii): x ⊕ W*(y) = W*(x) with lengths 3ℓ + 2 → 3ℓ + 3. Levels drop, so x is not on y's path: no corner. ✓
- **Lemma KEY.**
  - (a) is Fact X plus the identical β-rank and parity order in Γ(G) (6 + 2br + bp) and in IDEAL.
  - (b): the reversed play has the form e_(g_0), g_0, m_0, …, e_(g_ℓ), g_ℓ. Equal prefixes force equal owners.
  - e-indices are allocated in gate-index order (§3.1 and stab.py: `sorted(gv, key=lambda q: gv[q])`), so the first difference
    compares gate indices.
  - The Ω-order of the e-vertices, by (lev, gate), is never used. My MUT=eprio control (random even e-priorities above every β, repeats
    allowed): 0 violations. ✓
- **Theorem REALIZE.** The induction is right, modulo G-REAL-1 (b), which is closed.
  - SPEC S4b «Else τ_new = τ» gives τ_new = τ_0.
  - S5 never stops: (K0, K1) ∈ Iσ.
  - S4c fires iff σ_new = σ and τ_new = τ. This is the right test (FIX 3 is not needed: Iσ ≠ ∅).
  - Maximality: there is no transition before state 0, and L + 1 is a fallback.
  - L(G) is finite: if IDEAL never stopped, the induction would give an infinite N5 run, against R15.
  - The case L = 0 is degenerate but true (P-2).
- **Corollary REAL-IDEAL.**
  - Sizes: n = N + 3M + 6 ≤ 3(N + M) + 6; edges ≤ 6M + 10; Ω ≤ 4M + 9 (bmax ≤ 2M + 5, eb ≤ 2M + 6, max Ω(e) ≤ 4M + 4,
    top ≤ 4M + 6). My SIZE counter checks these.
  - (a): q(t) = p(3t + 6), with p nondecreasing.
  - (b): N + M ≤ n ≤ 3(N + M) + 6, so «super-polynomial in N + M» transfers to n. ✓
  - The not-claimed list (converse, S3 start, Ξ-cyclic) is correct and needed.

## 5. My tool and data (docs/referee-2/R2-N5-REALIZE/realize_check.py; log logs/run1.log)
- **How it works.**
  - My builder (§3.1) and my IDEAL implementation (§2) feed a SPEC S1-S5 loop on si.py's Engine. The loop records S4a's σ_new before S4c.
  - Checks at every state j ≤ L and at transition L + 1 (each count must be 0):
    - build and size: BUILD (byte-for-byte vs the pins), SIZE;
    - the run: STD, FB, W1 (formulas and W_j = W_0);
    - Ξ and the core: SBAR, PLAY, KA, KB, TAU, KC;
    - S4a's step: ESC, W2, TIE (fully optimal, no corner), FX (Fact X);
    - movers: AV, KEYB (κ order vs IDEAL key order on every pair of R(x)), RULE (σ_new = κ-least), IDEAL (σ_new = s_(j+1), or s_L at
      j = L).
  - BF=m enumerates every positional Odd strategy (gates × K2). It checks that Ξ is the pointwise minimum and that ρ is the UNIQUE
    pointwise optimum: P1 and SBAR (iii), independently of si.py.

| input | genomes | IDEAL steps (= FL transitions) | states | mover checks | violations |
| --- | --- | --- | --- | --- | --- |
| 7 R178 champions + R188 x3_L8, g4_L12; 4 pins compared byte-for-byte (BUILD) | 9 | 17 / 32 / 42 / 54 / 39 / 64 / 48, 8 / 12 (all «stuck») | 325 | 6,146 | 0 |
| random ACYC (my generator: deg 1-4, upward and downward Ξ-targets, d ≤ 8, N ≤ 40) | 1,160 | 978 | 2,138 | 16,197 | 0 |
| perturbed champions (1-6 mutations of xt / br / bp / gate / start, kept if acyclic) | 200 | 2,516 (199 stuck, 1 opt) | 2,716 | 52,155 | 0 |
| BF=11 random (M ≤ 11): 490,800 Odd strategies at 392 states | 300 | 209 | 509 | 1,811 | 0 |
| MUT=eprio (the line's looser e-priority description) | 240 | 600 | 840 | 11,356 | 0 |

- **Boundary probes.**
  - L = 0 (the start already stops: S4c at transition 1): 428 genomes.
  - N = 1: 347 genomes.
  - Both stop kinds: «opt» 419, «stuck» 1,250 (of the 1,669 non-control genomes).
- **Controls** (each must fire):
  - MUT=noesc (drop β → u): TAU fires on 2 / 2 champions and on 191 random genomes, as the Remark under Lemma TAU says. FB, STD and W1
    follow.
  - MUT=eorder (e-indices in reversed gate order): KEYB 33, IDEAL 20, RULE 0. The real run still follows the κ-rule; it is the IDEAL
    match that breaks.
- **Scope probe** (Ξ-cyclic random genomes, 294 cyclic): σ̄ ≠ β at some gate already at state 0 in 134. So §6's limit is real.
  I_τ = ∅ at state 0 on all 294.
- **Lane re-runs** at e609c5d2 (worktree; logs in my scratch, quoted here):
  - lemck.py: the 7 champions and 2 R188 genomes (L 17 / 32 / 42 / 54 / 39 / 64 / 48 / 8 / 12, all 0); --rand 20 3 451 / 20 4 187 /
    20 5 452: sums 19 / 24 / 20, 0 violations; --perturb 60 189: sum 1011, 0. These are exactly the check.sh block's strings and §7.
  - realck.py: champions FAITHFUL = IDEAL, EQUAL True; --rand ×3: 20 / 20 equal.
  - t2.py CLASS=full: seed 187 d 3: 14 / 30 equal; seed 188 d 4: 20 MISMATCH lines. These are §6's numbers.
  - Pins: all 8 sha1s match §7. pinck.sh on all four: «PIN OK (startck, zlk+verify, tl+verify, xeng)», exit 0.
  - My own oink_pins.py (my N5 loop vs Oink 8fbf0a7 --zlk -v): regions equal and verified on all four. N5 iterations 35 / 67 / 11 / 15
    = L + 3.

## 6. Line (P-N5-REALIZE-line.txt, 53dd6e9f)
Checked against the packet, item by item. Binder pass: N, M, lev, s, L(G), n, p are bound; u = K0 and «top» are defined inside the
game description. L41: nothing referee-originated. L43: no DEAD clause. L44 / L46: «whose proof uses no 𝒞^1O hypothesis (Lead reading
L46 and its amendment)». ✓
- **REAL-L1 (REQUIRED).** The 1E-N3 gloss «at a non-fallback transition j − 1 → j, σ_j is a pointwise optimum …» is narrower than the
  proof's use (G-REAL-1). Quote R57 (b) as R102's line does («that S1's procedure realises an optimal σ̄», on every valid input,
  L45), or name both forms: P1 (S1's σ̄, and τ̄ on G^d, are pointwise optima) and P2 (S4a's σ_new is a pointwise optimum of its arena).
- **REAL-L2 (REQUIRED).** «compared by the β of largest rank in the symmetric difference and its parity» does not say which way.
  Packet §2 / Fact X: the option containing that β is better iff its parity is 0 (even). Read the other way, the IDEAL model is a
  different model, and the realisation claim would be false (Ω parity = bp). State the direction.
- **P-1 (precision, optional).** «start σ = …, β → Ξ-target» could read «β → its Ξ-target (u when the target is X)».
- **P-2 (precision, optional).** For L(G) = 0 the «one FL run [0, L(G)] of length 0» is the empty set of transitions. A clause «(L(G) ≥ 1
  for a non-empty run)» or nothing: (a) and (b) are unaffected.
- **DATA in the line.** Every number is reproduced: 7 champions L 17 to 64; 2 R188; 60 random + 60 perturbed; the four pin sha1s and
  L_FL 32 / 64; Oink zlk / tl + verify; two engines. «random Ξ-cyclic genomes do mismatch» is reproduced (t2 numbers; my 134 / 294).

## 7. Notes (not gaps)
- **N-1.** Lemma TAU and K (c) do not use acyclicity. §6's list of acyclicity uses is right to omit them.
- **N-2.** §7 «L / n ≈ 0.2-0.26 on the champions» is 0.177 (big_d3, n 96) to 0.260 (grow_top_N24, n 246). And «every IDEAL-ACYC run
  found is LINEAR in N» is an asymptotic word on 7 fixed genomes. It is DATA in a not-to-sign section and not in the line, so it costs
  nothing here (cf. C108 E-1: «A DATA label does not cure an overclaim» if it ever moves into a line).
- **N-3.** §7's last clause (z3 maxima 4 / 8, L 9 UNSAT) was not re-run by me. It is not in the line.
- **D18 label.**
  - Theorem REALIZE and Corollary REAL-IDEAL: PROVED (two referee signatures pending; mine is given here), under the standing premise
    1E-N3.
  - IDEAL-LIN and FL-POLY: OPEN.
  - G-N5-TIME: OPEN.

## DONE / FINDINGS / NEEDS
- DONE: report of record. Every to-sign item is SIGNED. G-REAL-1 (minor) is closed. The line is REQUIRED on REAL-L1 and REAL-L2.
- FINDINGS:
  - The premise restatement omits P1 and binds P2 to σ_j at a non-fallback transition, but the proof uses σ_new before S4c. This is
    covered by the landed 1E-N3, and a second time by a direct SPEC trace.
  - The line leaves the IDEAL order's parity direction unstated.
  - All DATA reproduces exactly.
- NEEDS: L-RED: fixes entry for G-REAL-1 and line L-1 for REAL-L1 / REAL-L2.

## Addendum 1: comparison with REFEREE 22 (docs/referee/R-N5-REALIZE.md, origin/claude/referee 05b865e0; read after my push bcd43b5a)
- Verdicts agree: every to-sign item SIGNED by both; no gap in the mathematics.
- **REFEREE REAL-L1 (e-index order missing from the line): I AGREE, REQUIRED. I missed it.**
  - My MUT=eorder control (logs/run1.log) is a concrete instance. It builds Γ(G) as the line describes it, with every e-vertex
    priority and edge as stated, but indexes the e-vertices in REVERSED gate order.
  - The real N5 run then leaves the IDEAL run: KEYB 33, IDEAL 20 on big_d4_k3_W3 and grow_top_N24, first at state 0, mover x = 2.
  - RULE stays 0, so N5 still picks the κ-least gate; it is the IDEAL key order that no longer matches.
  - So the line's Γ(G), read without §3.1's index layout, makes the state-for-state claim false. REFEREE's «gap in the line's
    construction» is confirmed by a failing instance.
  - Repair as REFEREE says: «e-vertices indexed in the order of their gates' gate indices (packet §3.1)». My REAL-L2 (parity direction)
    is the same kind of omission.
- **REFEREE REAL-P1 (Lemma R + TB not redundant; bridge B redundant): agree.** My §3 adds that, at standard states, TB's conclusion can
  also be read directly off SPEC S1's procedure, so the packet need not rely on it. That is optional.
- **REFEREE REAL-P2 (L = 0) = my P-2; REAL-P3 (finiteness not circular) = my §4 REALIZE note:** agree.
- **My G-REAL-1 and REAL-L1 (1E-N3 gloss) are not in REFEREE's report.**
  - REFEREE marks «[1E-N3] ✓ for S4a (R57) and for S1's σ̄». That is the same premise in its R57 (b) form, which is what my closure
    uses. So we agree on substance.
  - My point is that the packet's §1 / line restatement (P2, for σ_j at non-fallback transitions only) is narrower than that use. I keep
    REAL-L1 (gloss) REQUIRED; the Lead may rule it a precision if the gloss is read as a label for R57 (b).
- **My REAL-L2 (parity direction of the IDEAL order) is not in REFEREE's report.** I keep it REQUIRED, for the same reason as
  REFEREE's REAL-L1: the reversed reading makes the realisation claim false.
- **Joint line list:** REFEREE REAL-L1 (e-index order) + my REAL-L1 (1E-N3 gloss) + my REAL-L2 (parity direction); optional: REFEREE
  REAL-P1 to P3 and «top»; my P-1 and P-2.

## Addendum 2: correction of my [VJ-LOC] row (after CHECKER C115 E-1, claude/checker fbca67cf)
- **What I got wrong.** My §1 row «premise [VJ-LOC]: only «1 ⇒ 2» is used (SBAR (ii)) … ✓» signed a premise route the fleet's record
  does not establish:
  - RESULTS R15 (iii): VJ00 Lemma 5.8 «1 ⇒ 2» «uses VJ00's unproved Lemma 5.9 and Prop. 5.10; not re-derived by either referee».
  - R36's Reading: Lemma P1 «does NOT discharge the two-player VJ00 Lemma 5.8».
  - I took the route from L-LIT T21 (c) («Unaffected»), a lit note, which is never a source by itself.
- **The correct carrier** is RESULTS R36 (c) Lemma P1, applied on G^d to Odd's one-player game Γ_σ. I confirm in R2-N5-REALIZE-L2.md §2
  that it covers SBAR (ii) in class, orientation and hypothesis.
- **The «P1» in my G-REAL-1 (a)** is 1E-N3's form (S1's σ̄ is optimal), as C115 says. It covers «φ = Ξσ», SBAR (iii), TAU and K (c),
  not «no improving edge ⇒ optimal».
- **Effect.** SBAR's mathematics and my signature stand, on [SPEC], R36 (c) and 1E-N3. No other item used [VJ-LOC]. Line L-2 carries the
  re-route (fixes entry 3).
