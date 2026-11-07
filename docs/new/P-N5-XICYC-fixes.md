# P-N5-XICYC fixes (append-only; the packet docs/new/P-N5-XICYC.md stays frozen)

## Fixes entry 1 (L-NEW successor 59, proactive, before any referee item; Lead 06:38Z: «Apply the DATA rule clause by clause»)
- Scope: line L-1 (docs/new/P-N5-XICYC-line-L1.txt) → line L-2 (docs/new/P-N5-XICYC-line-L2.txt). Exactly ONE string is replaced,
  once. Nothing else changes in the line. The packet is unchanged.
- D-1 (DATA rule): every clause of the line now has a counter of matching unit, set and scope, or the entry «no separate DATA».
  - BR-SEG, CYC-COUNT, ONEP-POLY, LEVEL0, BR-SEG-G, REACH3-CYC: counters.
  - T-CYC, RED-XI: «no separate DATA».
  - The Γ3 = IDEAL-CYC counts are moved to «context, not a clause»: no clause of the line asserts them.
  - The DEAD items name their pinned instances and the counts read off them.
- D-2 (new tool): experiments/new/box191/level0_191.py, the counter for LEVEL0, which had no counter in L-1. Its output:
  «LEVEL0 count 1000 seed 41: states 3422, (state, level-0 gate) pairs 17013, sigma-bar on the e-face 0».
- R-1, exact old string (in L-1, once):
«DEAD SEG-2P (Λ-keeping runs ≤ N fails: 9 steps at N 8, 15 at N 14, 21 at N 18) and DEAD ODD-FIXED, on pinned genomes; DATA: Γ3 = IDEAL-CYC on 22/22 genomes, random 1,271/1,300 with every divergence at an exact VJ tie; REACH3-CYC 0 violations in 2,167 transitions; Friedmann's switchallexp N 2-7 (Howard): C = 0, R = 4 … 241, T = 30 … 1243, p-runs ≤ 19;»
- R-1, exact new string (in L-2, once):
«DEAD SEG-2P («every run of consecutive Λ-keeping steps has at most N steps» fails: longest such run 9 steps at N 8, 15 at N 14, 21 at N 18, on the pinned genomes experiments/new/box191/inst/DEAD_SEG2P_d4_N8.json, DEAD_SEG2P_d7_N14.json, DEAD_SEG2P_d9_N18.json, read off subrun191.py's step labels) and DEAD ODD-FIXED (those three runs contain 1, 8 and 6 R-steps respectively); DATA, clause by clause (unit, set, command; every random set is rand191.rgen with d 1-6 (1-5 where stated), width 1-3, degree 2-3): BR-SEG: p-runs longer than N in 0 of 1,000 genomes (subrun191.py 1000 21, two-player IDEAL-CYC); CYC-COUNT: C > N·M (a stronger bound than the clause) in 0 of 300 genomes for each of the one- and two-player models (seg1p191.py 300 11); T-CYC: no separate DATA (it follows from BR-SEG and CYC-COUNT); ONEP-POLY: in the one-player model, a Λ-keeping run longer than N, or C > N·M, in 0 of 300 genomes (seg1p191.py 300 11); LEVEL0: σ̄ on the e-face in 0 of 17,013 (state, level-0 gate) pairs, from 3,422 states of 1,000 genomes (level0_191.py 1000 41); BR-SEG-G: a p-run longer than n_E in 0 of 2,000 random games (n 12, owners and priorities uniform, out-degree 1-3; brseg_gen191.py random 2000 3 12; H0 itself is not checked by the tool, which counts 555 steps in these runs where some switching Even vertex is its own cycle node); and, on Friedmann's switchallexp for N = 2, …, 7 (pgsolver_port.py switchallexp N, Howard from si.py's best-reward start): C = 0; R = 4, 10, 24, 54, 116, 241; T = 30, 70, 150, 310, 630, 1243; longest p-run 9, 11, 13, 15, 17, 19 against n_E = 23, 32, 41, 50, 59, 68; RED-XI: no separate DATA (a reduction); REACH3-CYC: 0 non-standard states, 0 non-Howard mover steps and 0 bad stops in 2,167 mover-phase transitions of 1,000 genomes (d 1-5; howard3_191.py 500 31 and 500 32); context for REACH3-CYC, not a clause: Γ3 mover sequences equal the IDEAL-CYC run state for state, with xi = T + 3, on 22 of 22 pinned genomes (8 L-RED R215 Ξ-cyclic genomes in inst/cyc*.json and the 14 P-N5-REACH corpus genomes; eq191.py), and on 1,271 of 1,300 random genomes (d 1-5; rand191.py eq 300 1 and eq 1000 2); each of the other 29 diverges first at an exact VJ tie;»
- Pins: experiments/new/box191/xicyc.pins now also pins this file, line L-2 and level0_191.py (check.sh block «P-N5-XICYC»).
- D-3: in L-2's BR-SEG-G clause, «with 0 H0 events» (the draft's first wording) was wrong and is not used. brseg_gen191.py's sub-count
  «of which with an H0 event: 0» counts H0 events among violations only. The total over the 2,000 games is 555 steps with some
  switching Even vertex that is its own cycle node (recount 2026-11-07). This does not affect the p-run counter (0 violations).
  The box doc docs/new/N5-XICYC-box191.md §2 «no H0 event» is corrected there (history doc, not frozen).

## Fixes entry 2 (2026-11-07 from 08:3xZ by date -u; L-NEW successor 59; Lead relay 08:24Z of the fix round)
Sources:
- REFEREE 26: docs/referee/R-P-N5-XICYC.md at claude/referee 695b610c.
- REFEREE-2 30: docs/referee-2/R2-P-N5-XICYC.md at claude/referee-2 a0befd6c.
- Nothing was REFUSED. Every exact string below was copied by script from the reports (wrapped lines joined with single spaces).
- The packet (149e2414) and entry 1 are unchanged. Where this entry and the packet differ, this entry governs.

### Packet repairs
- XC-1 (REFEREE) = W-1 (REFEREE-2), ACCEPTED: F4 is false as stated. REFEREE's instance: w (priority 2), y (4), v (9);
  A = (w, ∅, 3) ▷ B = (w, {v, y}, 3), but ext(v, A) ◁ ext(v, B).
  - F4 is REPLACED by F4′: if v ∉ Π(A) ∪ Π(B), then A ⊴ B ⇒ ext(v, A) ⊴ ext(v, B), and A ◁ B ⇒ ext(v, A) ◁ ext(v, B). It also holds
    whenever v ranks below Λ(A) and Λ(B): then ext adds 1 to k on both sides only.
  - Proof: the packet's own. With v in neither Π, v is added to both sets or to neither, so the symmetric difference is unchanged, and
    both lengths grow by 1. With different Λ, the order is decided by Λ, which ext keeps.
  - Every use of F4 in §4 satisfies F4′ (REFEREE §2.1):
    - DOM, STRICT and PATH's mover case apply ext at movers, which have priority 0, below every possible cycle node of Γ(G) (F6).
    - PATH's non-mover case applies ext(z_0, ·) to Ω_t(z_1) and val(tail). z_0 ∉ Π(Ω_t(z_1)), since that is z_0's own play after its
      first step and z_0 is not its cycle node. z_0 ∉ Π(val(tail)), since π is simple.
    - §7's Corollary T3 on Γ3: movers have Ω 0, below every cycle node (PAD (b): Ω ≥ 3).
  - So BR-SEG, T-CYC and ONEP-POLY stand as stated.
- XC-2 (REFEREE) = G-1 (REFEREE-2), ACCEPTED: on general games (§5) DOM is false, and STRICT's and PATH's proofs as written use F4
  outside F4′. Instances: REFEREE §2.1 (w, x, y); REFEREE-2 r2dompex.out. The STATEMENT of BR-SEG-G stands. Its proof is replaced by
  REFEREE's repair (REFEREE §2.2), stated here in full. I chose it because each step uses only F1, F3, F5 and F4′, which I checked line
  by line. REFEREE-2's lexicographic Z × Z repair with ext⁺ (its §5 «Repair», machine-checked there: DOM⁺ 0 / 16,384) is an
  independent second route and is not used here.
  - STRICT-G. Let x switch at step t → t+1 with Λ_t(x) ≠ x ≠ Λ_(t+1)(x) (H0), and put y′ := σ_(t+1)(x).
    - Ω_(t+1)(y′) ⊵ Ω_t(y′) by F1, and Ω_t(y′) ▷ Ω_t(σ_t(x)) by F5; so Ω_(t+1)(y′) ▷ Ω_t(σ_t(x)).
    - Neither Π contains x: each value is x's own play after its first step (at t + 1 and at t), and x is not its cycle node.
    - F4′ (strict) and F3 at t and t + 1 give Ω_(t+1)(x) = ext(x, Ω_(t+1)(y′)) ▷ ext(x, Ω_t(σ_t(x))) = Ω_t(x). ∎
  - PATH-G, the case of an Even z_0 (t − 1 ∈ [a, b], (t − 1) − a ≥ μ − 1). Put y := σ_t(z_0).
    - Ω_t(y) ⊵ Ω_(t−1)(y) by F1.
    - Ω_(t−1)(y) ⊵ Ω_(t−1)(z_1), since the Howard step t − 1 → t gives z_0 a ⊴-best successor under Ω_(t−1).
    - Ω_(t−1)(z_1) ⊵ val(tail) by induction.
    - z_0 is in neither Π(Ω_t(y)) (Λ_t(z_0) = w ≠ z_0) nor Π(val(tail)) (π is simple). F4′ and F3 give
      Ω_t(z_0) = ext(z_0, Ω_t(y)) ⊵ ext(z_0, val(tail)) = val(π).
    - The Odd and frozen cases are as in the packet (F4′ applies there). ∎
  - BR-SEG-G (a) then follows by BR-SEG's argument, with STRICT-G and PATH-G in place of STRICT and PATH. (b) and (c) are as stated.
    RED-XI inherits the repaired (c). No DOM is used in §5 or §6.
- XC-3 (REFEREE), ACCEPTED. In [REACH-L], K3 (b) ends «These values hold once SBAR3 gives σ̄(K2) = r», and SBAR3 is IDEAL-ACYC. So §7's
  «Not used: KEY3, PLAY3, SBAR3, Fact X» is CORRECTED to «Not used: KEY3, PLAY3, Fact X; SBAR3's conclusion σ̄(K2) = r is used through
  K3 (b) and is proved for every genome below».
  - Lemma K2-r (every genome; REFEREE §3.2, verbatim in substance). In every standard state σ(K1) = s and s → K1, so K1's play is
    K1 → s → K1 (cycle node K1, Ω 5) whatever Odd does. The core is closed: its only in-edges come from the pads pb_g. K2's options:
    - r leads to node K1, with reward −p′(K1);
    - the loop has node K2, with reward −p′(K2).

    K1 outranks K2 (Ω 5 > 3) and both are odd, so −p′(K1) < −p′(K2): r is strictly better for Odd. S1's σ̄ is a pointwise optimum
    ([1E-N3] P1), so σ̄(K2) = r. ∎
  - K3 (a)-(d), and with them ESC3 and the TIE sets {xt(g)} at β_g and {pA} at K0, therefore hold for every genome.
  - The same argument on Γ(G) with K1 frozen to its loop (IDEAL-CYC) gives σ̄(K2) = K1 (node K1 against node K2).
- XC-4 (REFEREE), ACCEPTED. §1 gains the premise [1E-N3] for §7: RESULTS R57 (b) as landed in R104 (R104, l. 9864, «the standing SPEC
  premise of RESULTS R57 (1E-N3 …), used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima; and S4a's σ_new … is a
  pointwise optimum of that arena»). §7 uses it to identify N5′-xi's Ξσ with §4's Ω and its W* with the optimum of H.
- N-1 (REFEREE-2), ACCEPTED. LEVEL0's «R-flips happen only at gates of level ≥ 1» also needs σ̄(K2) constant. On Γ(G) (IDEAL-CYC)
  σ̄(K2) = K1 in every state, and on Γ3 σ̄(K2) = r (Lemma K2-r): unique by REWARD, so every rule picks it.
- O-1 (REFEREE), ACCEPTED. In ONEP-POLY, «the deterministic rule picks the same σ̄(K2)» is replaced by «K2's optimal choice is UNIQUE
  (node K1 beats node K2 for Odd by REWARD), so every rule picks it».
- O-2 (REFEREE), DONE. experiments/new/box191/level0_191.py now imports from its own directory instead of an absolute /home/user path.
  Its output is unchanged (data/level0_1000_41.out).
- O-3 (REFEREE) is a note; the line handles it through R2 (W-3).
- REFEREE-2 N-2, DONE. The outputs of the line's seeded commands are now committed in experiments/new/box191/data/ and pinned:
  - subrun_1000_21.out
  - brseg_random_2000_3_12.out
  - level0_1000_41.out
  - howard3_500_31.out and howard3_500_32.out
  - rand_eq_1000_2.out
  - sae_6_7.out

  inst/sae_6.pg (5dc850b1…) and inst/sae_7.pg (ff46e32f…) are pinned too.
- DATA notes, both referees: 388 of the 2,072 steps of the 2,000 random games fail H0 (REFEREE-2 brseg_r2.out). The random-game data is
  therefore not data for H0 runs only; L-3 says so (R3).

### Line L-3
L-3 (docs/new/P-N5-XICYC-line-L3.txt, sha1 1690b6adae191bcd7a9fa9c42b0b5743b688b005, 1 line with its newline, 5,543 bytes, 67 «(» = 67 «)», depth never negative,
0 «|») = L-2 (857d21c8) with exactly these six replacements, applied by script. Each old string occurs exactly once in L-2; no other
byte changes.
- REFEREE-2 W-4 and REFEREE XC-L1 replace the SAME old string with different texts. W-4's text is used, and XC-L1 is RESOLVED by it
  (Lead ruling 08:24Z: «If the two exact texts conflict, use REFEREE-2's W-4 text and record XC-L1 as resolved by it»).
- XC-L2 is applied in REFEREE's «Equivalent» form («pin sae_6/7 and commit the lane's own output»), with the lane's own text below.
- L-2 + W-2..W-4 alone equals REFEREE-2's predicted dbdb1e61fc230de6ff8591fc9ee46f0aa453d3d9 (4,680 B; recomputed here).
- R1 (REFEREE-2 W-2): «and DEAD ODD-FIXED (those three runs contain 1, 8 and 6 R-steps respectively)» → «and DEAD ODD-FIXED («σ̄ is constant on every run of Λ-keeping steps» fails: those three runs contain 1, 8 and 6 R-steps respectively, each a Λ-keeping step at which σ̄ changes)»
- R2 (REFEREE-2 W-3): «ONEP-POLY: in the one-player model, a Λ-keeping run longer than N, or C > N·M, in 0 of 300 genomes (seg1p191.py 300 11);» → «ONEP-POLY: in the one-player model, a Λ-keeping run longer than N, or C > N·M, in 0 of 300 genomes (seg1p191.py 300 11; R is not counted, R = 0 has no separate DATA);»
- R3 (REFEREE-2 W-4; resolves REFEREE XC-L1, Lead ruling): «H0 itself is not checked by the tool, which counts 555 steps in these runs where some switching Even vertex is its own cycle node» → «H0 is not checked by the tool, and these runs include steps at which H0 fails»
- R4 (REFEREE XC-L2, «Equivalent» form: lane pins and lane output): «against n_E = 23, 32, 41, 50, 59, 68;» → «against n_E = 23, 32, 41, 50, 59, 68 (N 2-5: inst/sae_2..5.pg and check191.out; N 6, 7: inst/sae_6.pg and inst/sae_7.pg, the outputs of pgsolver_port.py switchallexp 6 and 7, sha1 5dc850b1… and ff46e32f…, pinned in xicyc.pins, with brseg_gen191.py's output experiments/new/box191/data/sae_6_7.out);»
- R5 (REFEREE XC-L3): «0 non-standard states, 0 non-Howard mover steps and 0 bad stops in 2,167 mover-phase transitions of 1,000 genomes» → «0 genomes with a non-standard state among states 0, …, T3, 0 non-Howard mover steps, and 0 genomes whose first state with no strictly better mover successor is followed by a transition that changes a mover, in 2,167 mover-phase transitions of 1,000 genomes (the tool does not read the fallback flag; the fallback at transition T3 + 1 is checked by REFEREE R-P-N5-XICYC on 22 of 22 pinned and 300 of 300 random genomes, docs/referee/scratch/xicyc_logs/reach3_*.out)»
- R6 (REFEREE XC-L4): «(Theorem REACH3-CYC, CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3, not landed)» → «(Theorem REACH3-CYC, CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3, not landed, with σ̄(K2) = r proved for every genome in P-N5-XICYC's fixes (K3 (b) otherwise cites SBAR3, which is IDEAL-ACYC), and on the landed premise [1E-N3] (RESULTS R57 (b), as landed in R104: S1's σ̄ and S4a's arena optimum are pointwise optima))»
- Pins: experiments/new/box191/xicyc.pins gains L-3, this file's new sha1, data/*.out, inst/sae_6.pg, inst/sae_7.pg and the new level0_191.py; check.sh block «P-N5-XICYC» pins the new xicyc.pins.
