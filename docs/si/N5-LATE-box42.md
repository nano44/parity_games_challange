# N5-LATE (box 42): late adoptions split into FIRST (≤ m_E per W-run, Ξ-free) and REPEAT (W-paid); R* reduces to repeats
L-SI successor 31 (Opus 5.5), D15 / D18, Lead reading L40. Lead 2026-10-30 00:09Z: «Priority after W-VPOLY-S: whichever of BA or LATE
you judge closer to a proof that avoids the Ξ-route.» (box 41 §4 chose LATE / R*). Working note, unrefereed, not a TARGET.md claim.
G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Tool: experiments/si/odd/laterep.py, a copy of L-NEW's experiments/new/box64/late.py (read-only source; same W-run cut and the same
  late-adoption definition) with a FIRST / REPEAT split. Output odd/out/laterep_corpus.txt (719 games of odd/sbcg.lst). Pinned in
  si/check.sh «box 42».
- Definitions (R89 P-N5-FRAME §3.3-3.4; R88 §4): a W-run F (no fallback, τ and λ_W constant); (y, z) BLOCKED at t: W_t(z) ▷ W_t(σ_t y)
  and (y, z) ∉ Iσ_t; a LATE ADOPTION of (y, z) at u: σ_{u+1}(y) = z after (y, z) was blocked at an earlier state of F.
  A late adoption is FIRST if it is the first late adoption of (y, z) in F, REPEAT otherwise.

## 1. Lemma LATE-SPLIT (PROVED, lane; Ξ-free)
- (i) FIRST: at most one per Even edge per W-run, so #FIRST_F ≤ m_E.
- (ii) REPEAT: let u₁ < u₂ be consecutive late adoptions of (y, z) in F. Then y leaves z at some k with u₁ < k < u₂, and (y, z) is blocked
  at some t with k < t < u₂. If y is not its own W-cycle node on [k + 1, t], then W(z) changes on [k + 1, t].
- Proof of (ii).
  - After u₁, σ(y) = z. A blocked edge needs z ≠ σ_t(y), so y left z at some k between u₁ and the blocked state t.
  - (OPT) at k + 1 (box 37 Lemma OPT-OFF, (y, z) ∈ σ_k ⊆ H_k): W_{k+1}(z) ⊴ W_{k+1}(σ_{k+1} y).
  - W-SUCC on [k + 1, t]: W_{k+1}(σ_{k+1} y) ⊴ W_t(σ_t y).
  - Blocked at t: W_t(σ_t y) ◁ W_t(z).
  - So W_t(z) ▷ W_{k+1}(z). □
- So every REPEAT is a W-paid return of y to z inside F (W-ENT's mechanism, box 37), and
  #REPEAT_F(y, z) ≤ WCH_F(z) + CYC_F(y, z).

## 2. Consequences (PROVED, lane, arithmetic)
- R*_T(F) ≤ #late adoptions in F ≤ m_E + REP_F, with REP_F := the REPEAT late adoptions of F.
- With box 41's Lemma WV-R, on a guided stretch Q, for every vertex w:
  WCH_Q(w) ≤ Λ_Q + (Λ_Q + 1)(n − 1)(m_E + REP*_Q + 1), where Λ_Q ≤ n(n − 1) and REP*_Q is the largest REP_F of a W-run of Q.
- Corollary (Ξ-free; PROVED, lane). If no Even edge is late-adopted twice inside one W-run of Q, then every vertex changes W at most
  n(n − 1) + (n(n − 1) + 1)(n − 1)(m_E + 1) = O(n³ m) times in Q. By W-ENT (box 37 §2) the stretch then has
  |Q| ≤ m_E(1 + O(n³ m)) + SIL_Q + CYC_Q.
- The recursion that is left (READING). Σ_{(y, z)} #REPEAT_F(y, z) ≤ Σ_z d_E(z)·WCH_F(z) + CYC, and WCH_F ≤ (n − 1)(m_E + REP_F + 1) by
  GP*-RUN. The loop "late adoption → wave of ≤ n − 1 W-changes → repeat adoptions" has no contraction factor. A proof needs a reason
  why a W-wave started by one late adoption does not re-block edges already adopted in the same W-run, or does so only O(1) times per
  edge.

## 3. DATA (corpus, 719 games)
- 1,141 late adoptions (the same total as L-NEW's late_all.txt): FIRST 1,100, REPEAT 41. REPEAT without a W-rise of z since y's leave
  of z (off-cycle): 0. CYC: 0. Every late adoption has a Ξ-rise of z (1,141, as in late_all.txt); W(z) rose since blocking in 254.
- Most late adoptions of one edge in one W-run: 3 (so_th_n32). Most REPEATs in one game: 6 (switchbestexp_8 and fc_8, n 210).
- So R* is dominated by FIRST adoptions, which are bounded by m_E with no Ξ argument.
- CONJECTURE REP-LIN: REP_F ≤ n per W-run. DATA: ≤ 6 per game. With [C2] (box 41) it gives W-VPOLY-S in the form O(n³ m) per
  guided stretch.

## 4. Composition toward G-N5-TIME (one line each)
- §1: [P-LATE] (notebook «Conditionals») is now [P-REP] plus m_E. The FIRST part needs no Ξ-route.
- §2: per guided stretch, W-changes are O(n³ m) when no edge is late-adopted twice in a W-run. Repeats are W-paid returns.
- Remaining Even-side frontier: (a) Even fallbacks per phase, (b) τ-changes (Odd half), (c′) REP per W-run, plus SIL / CYC.

## DONE / FINDINGS / NEEDS
- DONE: odd/laterep.py; corpus; si/check.sh «box 42»; this note; notebook conditionals updated.
- FINDINGS:
  1. PROVED (lane): Lemma LATE-SPLIT. FIRST ≤ m_E per W-run; REPEAT ⇒ a W-change of z since y's leave.
  2. PROVED (lane): R*_T ≤ m_E + REP, so W per guided stretch is O(n³ m) when REP = 0 (Ξ-free).
  3. DATA: 1,100 of 1,141 late adoptions are FIRST; REPEAT ≤ 6 per game; LATE-SPLIT (ii) 0 failures.
  4. CONJECTURE REP-LIN.
- NEEDS: none from the owner.
