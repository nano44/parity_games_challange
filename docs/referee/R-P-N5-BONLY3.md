# R-P-N5-BONLY3: first referee report on packet P-N5-BONLY3 (L-SI box 96)
**STATUS (2026-11-11T23:32Z by date -u): P-N5-BONLY3 WITHDRAWN as a landing packet by the Lead (23:33Z message: duplicates P-N5-CHAIN §5
Lemma B-ONLY3, GT-1 / B-1). This report is kept as the record of my read, written before the withdrawal; no line will be tested.**
REFEREE successor 31 (Opus 5.5, D15; D1). Date -u at writing: 2026-11-11T23:32Z. Not read before my verdict: docs/referee-2/; L-RED 64's R230 read
only for its numbers in §5 (context), after §0 was drafted.

## 1. Object and premises
- claude/l-si 681bfccf (ancestor of origin/claude/l-si, checked), docs/si/P-N5-BONLY3.md sha1 a6baa60b5c4116006419b16b55ffa3c029f0f52e,
  13,288 B, 126 lines. No line yet.
- Premise quotes, by script (scratch/bonly3 quote check inline in this session; every «…» located): [DEF] three quotes verbatim in RESULTS
  R104; [DEF3] verbatim in R117 (and in P-N5-CHAIN's [G3]); [FRAME3] verbatim in R122; [VJ] verbatim in R118; [OPT] verbatim in R123;
  R123 B-ONLY verbatim; R118 (k)'s two quotes verbatim; R122's «an optimal counterstrategy being pointwise optimal …» verbatim (R122);
  REACH3-ALL verbatim in P-N5-CHAIN's frozen text 6e613ba7. Non-premise quotes (the Lead's ruling, «fix G…», P-N5-REALIZE l. 89 for
  wording, P-N5-GATE fixes G1) are not RESULTS text and are not used as premises: fine.
- **B-1 (overlap, REQUIRED in any line).** P-N5-CHAIN (frozen 6e613ba7, landing as R125) §5 already contains a **Lemma B-ONLY3** with the
  SAME name, the SAME exception list (c_W, the e-vertices whose successor is c_W, and their pads pe_g) and the SAME conclusion, PROVED for
  every state of HOW3(G) (states 0..T3), in its «To sign» table, SIGNED by both referees (R-P-N5-CHAIN.md §0; R2-P-N5-CHAIN.md), stated in
  R125's line L-5 (473344b1). Its proof is the same τ_β argument (credit L-RED R221 §3, as here). NO-TIE3 there is derived from it.
  P-N5-BONLY3 does not cite it. What this packet adds is the FRAME-WIDE form: any σ in [FRAME3] (arbitrary movers) with any optimal σ̄,
  not only HOW3's states; and the corollaries NO-E-CYCLE3, PROVISO3, LAM-UP3 (one-line consequences). Corollary RUN3 under [STD3] adds
  nothing to R125: [STD3]'s pending form IS P-N5-CHAIN's REACH3-ALL, and on those states P-N5-CHAIN's B-ONLY3 already holds.
  - The packet must cite P-N5-CHAIN's Lemma B-ONLY3 as an overlap (cite, do not duplicate), and the two lemmas need distinct names in
    RESULTS (e.g. this one «B-ONLY3-FRAME»), or this statement is folded into R125's as a frame-wide strengthening.
  - It also corrects the record: P-N5-GATE fixes G1's «B-ONLY on Γ3 … not among P-N5-CHAIN's facts» (quoted in this packet's §4) is false
    (R-P-N5-GATE GT-1).

## 2. Proofs, each step re-derived
- Lemma B-ONLY3 (frame-wide): CORRECT.
  - τ_β (β-face pβ_g at every gate, σ̄(K2) kept) is a positional Odd strategy. Into e_g only pe_g, into pe_g only g ([DEF3]); under τ_β g
    goes to pβ_g; so an e-vertex can be on a τ_β-play only as its first or second vertex (v = e_g or v = pe_g), never on its cycle.
  - c_W's in-edges are its loop and the e's with successor c_W ([DEF]); such an e is reachable only at the start, so c_W is on v's
    τ_β-play only for the excluded v. (A gate of such an e goes to pβ under τ_β: not excluded and not reaching c_W. Correct.)
  - [CORE] in [FRAME3]: K0 → pA → K3 → K2; K2 → r → K1 or its loop; K1 → s → K1; nothing in the core leads back to K0 (K1 is frozen at s,
    not q), and the core has no exit. So K0, K3 are on no cycle, for any Odd strategy.
  - So the τ_β cycle node w′ is not an e-vertex, c_W, K0, K3; by [RANK] it is less relevant than every e-vertex, so its reward is below
    the least e-vertex's reward (e-vertices even; a less relevant vertex has smaller reward whatever its parity).
  - [OPT] and [VJ] (reward of the cycle node first): reward(Λ(v)) ≤ reward(w′). Λ(v) is a cycle node, so not K0, K3; if it were an
    e-vertex or c_W its reward would exceed reward(w′). Hence Λ(v) is less relevant than every e-vertex. ∎ Uses only [FRAME3], [OPT],
    [VJ], [DEF], [DEF3]: as stated. Identical in substance to P-N5-CHAIN l. 201-208, with «state t» replaced by «σ in [FRAME3]».
- NO-E-CYCLE3: a cycle through e_g contains D = e_g's successor; D = c_W is impossible (c_W only loops); D is a mover (W-target), not an
  exception, and its play is that cycle, so Λ(D) is e_g or more relevant: contradiction. CORRECT.
- PROVISO3: D = c_W: its loop; else e_o ∈ P(D) closes the play at D, a cycle through e_o: NO-E-CYCLE3. CORRECT. (= my R-P-N5-GATE §2.4.)
- LAM-UP3: pβ_o is no exception, so Λ(pβ_o) ≠ c_W; e_o → c_W gives Λ(pe_o) = c_W ≠ Λ(pβ_o); otherwise pe_o is no exception and Λ(pe_o) is
  less relevant than e_o. CORRECT. (= my R-P-N5-GATE §2.2, K10 on Γ3.)
- Face transport (§4, fix G3): a single-successor v has P(v) = v · P(succ v) or lies on that cycle; Λ(v) = Λ(succ v). CORRECT.
- Corollary RUN3 under [STD3]: each state 0..T3 is a pair in [FRAME3] (standard states: σ(K0) = pA, σ(K1) = s, σ(K3) = K2, β → Ξ-target or
  pb_g, as [G3]'s standard state; σ̄_t optimal by [1E-N3] / R57 (b) as R122 cites it). CORRECT, conditional on [STD3].
- [STD3]'s status (§3): for Ξ-cyclic G, R118 (k) is CONDITIONAL (quoted correctly); pending form = P-N5-CHAIN REACH3-ALL (R125). Correct as
  stated. Scope «up to the first fallback only»: correct and necessary (the frame fails after the fallback: K0 switched, §5).

## 3. Replay with my own code (scratch/bonly3_replay.py; log bonly3_logs/replay.out)
- Own Γ3 builder and VJ best_reply (my lane's), no lane code. Pairs tested: every HOW3 state (0..T3) and 50 uniformly random mover
  strategies in [FRAME3] per genome, each with its optimal σ̄; the 19 instances of box 91 / box 93 (sha1-checked). Counters (must be 0):
  bonly (B-ONLY3 at every vertex), ecyc (NO-E-CYCLE3), dpass (PROVISO3), lamup (LAM-UP3), transp (face transport). Controls: cNopad
  (pad exceptions dropped) and a_bonly (Odd's anti strategy, e-face at every gate, in place of σ̄): must fire.
- RESULTS (seed 2026): 1,833 pairs (HOW3 states plus 950 random frame strategies), 531,737 (pair, gate) pairs: bonly 0, ecyc 0, dpass 0,
  lamup 0, transp 0 on all 19 instances. Controls fire on every instance: cNopad 467,241 (the pad clause is needed), a_bonly 935,350
  (optimality of σ̄ is needed). After-fallback failure (L-RED 64): not re-run (my engine has no N5′-xi fallback); context only.

## 4. TARGET.md diff: CLEAN
- A lemma about the plays of Γ3(G) under frame strategies and optimal Odd replies, and its reading on N5′-xi's pre-fallback states. No
  bound, no algorithm claim; the packet says «Not a TARGET.md claim; not M3 or M4; not a gauntlet step; G-N5-TIME stays OPEN». CLEAN.

## 5. Line requirements (no line yet)
- LB-1 (B-1): cite P-N5-CHAIN's Lemma B-ONLY3 (pending R125; same exceptions, HOW3 states) as an overlap; give this lemma a distinct name
  or state it as the frame-wide form of R125's; RUN3 stated as following from R125's REACH3-ALL and B-ONLY3 (no new content on the run).
- LB-2: scope: any σ in [FRAME3] with any optimal σ̄; on N5′-xi only states 0..T3; «after the first fallback the conclusion fails (DATA:
  L-RED 64, MWR4_2 sha1 856d369b…, states 32-33)» kept, as L-RED DATA.
- LB-3: DATA units as read in d96.py: bonly per (state, vertex) over the RUN's states only (not frame-wide), exceptions by the closure of
  fix G5; dpass, lamD per (gate, state); sfail, relD, unlD per gate; CTRL=anti counts aptpass (a PROVISO control, not a B-ONLY control);
  CTRL=nopad fires on g3 only. Frame-wide coverage: L-RED 64's FRAME-X census (cited as L-RED DATA) and my §3 replay.
- LB-4: TARGET tail in the landed R123 / R124 form.

## 0. Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §2 | Lemma B-ONLY3 (frame-wide) | **SIGN** (B-1: overlaps P-N5-CHAIN's Lemma B-ONLY3 on HOW3 states; distinct name or fold required) |
| §2 | NO-E-CYCLE3, PROVISO3, LAM-UP3 | **SIGN** |
| §3 | Corollary RUN3 | **SIGN**, CONDITIONAL on HYPOTHESIS [STD3] (= R118 (k), conditional for Ξ-cyclic G; = P-N5-CHAIN REACH3-ALL, R125 PENDING) |
| §4 | caveats removed (READING) | agrees with R-P-N5-GATE GT-1 (which reaches the same from P-N5-CHAIN's B-ONLY3 directly) |
No GAP; nothing refused. Pending-packet premise: P-N5-CHAIN (R125) for RUN3's [STD3] pending form. Recommendation to the Lead: since
P-N5-CHAIN's B-ONLY3 already gives every Γ3 use P-N5-GATE needs, P-N5-BONLY3 adds only the frame-wide generality; land it (if at all)
as a short entry citing R125, not as the first B-ONLY on Γ3.
