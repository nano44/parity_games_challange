# R-P-N5-CHAIN: DRAFT working notes (NO VERDICTS) on box 196 «CLOSE THE Γ3 CHAIN» (L-NEW successor 64)
REFEREE successor 29 (Opus 5.5, D15). date -u at writing 2026-11-08T08:33Z. Status: DRAFT. The object is not frozen. Lead 08:11Z: prepare; convert
to the first review when the frozen packet P-N5-CHAIN's SHA arrives.
Read: claude/l-new f725af5a + Addendum 1 08801298 (ancestor of origin/claude/l-new, checked), docs/new/N5-CHAIN-box196.md (264 lines,
28,013 B at 08801298). NOT read: L-RED's R224-chain.md (until my derivations are written; they are below now) and docs/referee-2/.
Everything here is to be re-checked against the frozen text. Box line numbers are at 08801298.

## 1. Derivations (re-done, step by step; no verdicts)
- §2 ESC3-ALL.
  - (K0, K1) ∈ Iσ: K3 (b) (R117, every genome).
  - β_g: in H every play from xt(g) follows pe at every gate (τ), so it descends one level per e-step to c_W (node c_W, even). pb_g → K0
    → {pA → K3 → K2 → K2 (τ), K1 → s → K1}: odd nodes. So W*(β_g) goes via xt. β_g's only in-edge is from pβ_g, which only a gate enters,
    and gates play pe in H; so β_g is on no H-cycle and TIE(β_g) = {xt(g)}.
  - K0: TIE(K0) = {pA} (node K2 beats node K1). K1 and K3: A = {σ} (only (K0, K1) is improving in a standard state).
  - Re-derived. No Ξ-edge is followed except in H-plays that start at xt(g) and never leave by a β-face. AGREES.
- §2 W3-ALL (i)-(iii): lengths 5ℓ + 5 / 4 / 3 / 2 / 1 from x / m / g / pe / e. Every H-play from a pad of x has the same length and node
  c_W, since H's Odd plays pe. x is on no H-cycle. TIE(x) = A(x). Re-derived. AGREES.
- REACH3-ALL: the induction is R118 (k)'s, with ESC3-ALL and W3-ALL. TIE(x) = A(x) ∋ every strictly better successor, so the Ξσ-best
  element of TIE(x) is a ⊴-best successor (a Howard step with N5′-xi's tie order). At T3, A(x) = {σ(x)}, so S4c fires. Re-derived.
  AGREES. The Remark (N5 = SPEC is not Howard on Ξ-cyclic genomes) is consistent with my R-P-N5-END §4 (C).
- §3:
  - CN2-3: from PAD (a) (every cycle has a vertex of Ω ≥ 3 except c_X's loop, and c_X has no other in-edge) and ranks by Ω first.
    AGREES.
  - LOC-GATE3: P-N5-QUIET §3's case analysis uses only [OPT], F3, F4′ and «g is not a cycle node and in no Π». Each holds on Γ3 by
    CN2-3. AGREES.
  - LOC-K2-3: K1 → s frozen; Odd prefers node K1 (−p′(K1) < −p′(K2)), so σ̄(K2) = r. Ω(r) = (K1, ∅, 1) ◁ (K1, ∅, 2) = Ω(K2) (odd node,
    longer is better). AGREES.
  - B-ONLY3: under τ_β (pβ everywhere, r at K2) the only e-vertex a play can meet is at its start (pe_g → e_g). Its node is below every
    e-vertex; [OPT] gives reward(Λ_t(v)) ≤ that reward. This excludes Λ = e (even, higher reward) and Λ = c_W, K0 (higher reward).
    K3 is never a cycle node (F-E3). Re-derived. AGREES.
  - NO-TIE3 and (F-cls3) / (F-E3): AGREE.
- QUIET3: each of (Q1)-(Q6) of P-N5-QUIET §4 (at claude/l-new 559cdffc, l. 128-163) checked with the box's substitutions.
  - (Q2): CN2-3 covers the pad m.
  - (Q4): pβ_g → β_g → z with class(pβ_g) = class(β_g) = class(z); pe_g → e_g → y. The exit through pb_g → K0 … is constant by
    LOC-K2-3.
  - (Q5): the e-face value is ext(pe, ext(e, Ω(y))). The Bellman-Ford step needs F3 and F4′ at m, g, the face pad and the face, which
    are in no Π (CN2-3 and (Q4)).
  - (Q3) / (Q6): k_t ∈ {0, …, n3 − 1}, so L3 = (M + 1)(2M + 1)(N + 1) + N(n3 − 1).
  - No step uses the tie rule: DOM holds for any best choice. AGREES.
- §4 E-MON3, CHAIN-DECOMP3, HUB-ASC-G3 (2M + 3 nodes: M e's, M β's, c_W, K1, K2; c_X only for c_X itself), UP-JUMP3 / UP-B3:
  - The structural steps agree: pads change no level; β → pb enters the closed core; e_g → W-target is unpadded.
  - Still to check against the frozen text: P-N5-ASC §5 / §6 word for word (R121's L-5 text).
- §5 CHAIN3 arithmetic: T3 + 3 ≤ (1 + n3((2M + 3)F′_U(M) − 1))(L3 + 1) + 3 follows from T-QUIET3 with D^tot_E ≤ (2M + 3)F′_U.
  - deg_M F′_B = 5·2^B − 3 (F_B = (M² + M + 1)(1 + M·F_(B−1)²), deg 3 + 2·deg).
  - n3 ≥ N + M, so polynomial in n3. AGREES.
- Addendum 1:
  - F1 from R15 (a): a Howard step's switch set is a non-empty unambiguous set of improvements in Γ3 (valuation on the full game,
    non-movers fixed by σ). F6 / F5 / DOM / STRICT as stated. AGREES.

## 2. Candidate findings (DRAFT; to be ruled on the frozen text)
- CH-1 ([OPT] source):
  - §3 cites «[OPT]: σ̄_t is a pointwise optimum (R57 (b) / R21 (a), as P-N5-QUIET §1)».
  - P-N5-QUIET's L-2 (559cdffc, QT-L1, both referees) now has [OPT] = R118's σ̄ (R118 (b), XICYC l. 75) and R21 (a), and says «R57 (b)
    concerns the output of SPEC's S1 procedure and is not used». HOW3's σ̄_t is a defined object, as IDEAL-CYC's was.
  - Expected: required wording (as QT-L1). Not a proof gap.
- CH-2 (C10, [E-LEV]): the box offers «HYPOTHESIS, or … Lead reading 23:54Z (referees decide)». The referees decided: HYPOTHESIS
  (R-P-N5-QUIET QT-L3; P-N5-ASC signs UP-B under [E-LEV]). Expected: CHAIN3 PROVED-CONDITIONAL on (or «under») [E-LEV] only.
- CH-3 (bit cost): §5 «Each iteration is polynomial at bit cost (SPEC S1-S4 are one-player VJ evaluations; R117 / SPEC)».
  - The landed source for N5 is R57's Lemma BIT-G.
  - For N5′-xi the S4a change (TIE sets and Ξσ-best) needs one line of its own.
  - This sentence is outside CHAIN3's iteration-count statement; it should be scoped or cited.
- CH-4 (premise status): CHAIN3 rests on P-N5-END (two first reviews; mine SIGN), P-N5-ASC (R121) and P-N5-QUIET (lane packets).
  The box says so (§5 «Premises not landed»). The label must stay PROVED-CONDITIONAL on their landing, or wait for it.
- CH-5 (DATA controls): the box lists nonstd, cnlow, k2fail, crossflip and emon as counters without a control. In my replay tqfail
  (T-QUIET3's bound) also never fires under ctrl1. Expected: a note, not an item.

## 3. My replay (own code; scratch/chain_replay.py; chain_logs/sweep.out)
- Engine:
  - HOW3: my Γ3 builder xicyc_replay.build(G, pad=True); non-movers frozen at the standard state; Odd by my VJ best reply; Howard steps,
    my tie rule (keep, else largest index).
  - REACH3-ALL on my N5′-xi engine (end_replay.py, mode xi, hook per iteration).
  - Genomes from my own generator (end_replay.gen: rand, selfl, deep, wide, acyc; 400 each, seed 2961), plus the 61 pinned genome files
    of box189 corpus / inst and box191-196 inst (incl. RT_n1).
- Result: 2,061 runs, 1,580 Ξ-cyclic. Every counter 0:
  - CN2-3, NO-TIE3, LOC-GATE3, LOC-K2-3, B-ONLY3, QUIET3 (wfail, Tfail, crossflip), T-QUIET3 (tqfail), E-MON3, CHAIN-DECOMP3,
    UP-JUMP3, UP-B3, the 2M + 3 count;
  - REACH3-ALL: nonstd, nohoward, fbpos; and E0 / one fallback.
  - Max T 129 (LEAP_k64), W 32 (RS2_L32M6), equal to the box's numbers.
- Controls:
  - ctrl1 (L3 := 0, U := −1): wfail 22, Tfail 21, upfail 23,455 in 100 runs.
  - ctrl2 (LOC-GATE3 order reversed): locfail 2,795. The same CTRL=2 also starts end_replay from its own control state, so nonstd 200,
    fbpos 100 and e0fail 300 fire there too.
- My N5′-xi's T3 equals my HOW3 run length on every run (same tie mechanics). The lane's RT_n1 numbers (T3 = 1 vs T_CYC = 2) are
  tie-dependent (the box's §6). With my tie rule both are 2. That is consistent: the box claims only that the runs can differ.

## 4. To do on freeze
Byte-check the frozen packet against these notes; quotes by script (RESULTS R15, R117, R118 (k), P-N5-REACH §6.5-§6.6); P-N5-ASC §5-§6
and P-N5-QUIET §4 word for word against their landed / line texts; the lane's check196.sh re-run; DATA rule clause by clause (the line);
TARGET.md diff; then read L-RED R224 and compare.
