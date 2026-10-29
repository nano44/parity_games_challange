# N5-CARRY (box 57): the early carry is F's stale frame at Odd-reset steps. Forced by S4a′, not by a tie. CARRY-CUT stays a CONJECTURE that a gated counter can refute
L-NEW successor 33 (Opus 5.5; D14, D18, Lead reading L40). Lead's message 2026-10-29 16:24Z, BOX 57 (the CARRY-CUT route): «(a) Explain the
early carry as an F-mechanism: which Even step of F makes a higher CC see its exit early, and is that step forced by F's single-frame rule
(S4a with σ̄ fixed), rather than by this arena? (b) If it is forced, state it as a lemma, CONJECTURE CARRY-CUT ... Try to prove it. ... Say
explicitly whether CARRY-CUT uses anything beyond MONO-XI + argmin. If L-RED blocks the early carry with a variant, CARRY-CUT is dead and the
variant is your counterexample.» Written from 16:30Z (date -u). Working note, unrefereed, not a TARGET.md claim.
Symbols: F, σ̄, orbit as in P-N5-SF §0. I^glo = Schewe's optimal step: the optimum of the arena game H (Even: {σ(v)} ∪ Iσ(v); Odd FREE),
evaluated with the NEW counterstrategy (L-LIT T44 / T46 §1 (a)). Labels as usual. Vertex names are switchbestexp's (PGSolver port,
experiments/hard-families/pgsolver_port.py): e_i, f_i, g_i = CycleNode0/1/2(i) (Even), h_i = CycleCenter(i) (Odd; successors e_i, m_i),
m_i = CycleLeaver(i), g′_i = CycleNodeToLane2(i), x = BitSelector, y = LowestBit, w = HighEntryBit, a_k / b_k = the deceleration lane.
Bit i = 1 iff σ̄(h_i) = m_i (Odd exits bit i's cycle).
Tools (experiments/new/box56/): carry.py (switches and bit patterns along F's orbit), carry2.py (closing edges of C_i, stale vs true value),
carry3.py (states where F's step ≠ I^glo's step from the same state), hybrid.py (one-sided runs F / I^glo / hybrids; CLS=g takes I^glo's
step exactly where the two differ at a g-vertex), forced.py (at a divergence, is F's option strictly better in the STALE frame and strictly
worse in the TRUE frame?). Logs: box56/hyb_67.txt; the other runs are inline (commands below, all deterministic).

## 0. Summary
- (a) DATA, exact on switchbestexp N = 4..7. F's orbit and I^glo's step differ only at a few states. The ones that matter are the
  ODD-RESET steps: steps after which Odd's best reply at some cycle centre h_i flips from exit m_i to stay e_i (bit i resets). This happens
  in F's run and in I^glo's step alike.
  - At such a step I^glo OPENS the access g_j → g′_j (to the lane) for every j ≤ i, and routes x → w.
  - F keeps g_j → h_j and routes x → y, y → l_0. F is computed against the stale σ̄(σ), in which h_j still exits to m_j.
  - F's option is STRICTLY better in the stale frame and STRICTLY worse in the true frame (forced.py on switchbestexp_5 at orbit states
    101, 178, 217 (g_0 and g_1), 218). So it is forced by S4a′, not by a tie-break.
  - Taking I^glo's step at exactly these states, and F's step everywhere else, restores I^glo's whole count: 286, 590, 1198, 2414 steps at
    N = 4, 5, 6, 7, equal to I^glo's (PGSolver's switch-best: 289, 593, 1201, 2417). It needs 4, 11, 26, 57 = 2^(N−1) − N corrected
    steps. F itself makes 258, 364, 412, 456 steps.
  - So the early carry is caused entirely by F's single frame at Odd-reset steps. The "higher CC sees its exit early" is a downstream
    timing effect of these one-step lags (x → y instead of x → w shifts the lane and bit-selector schedule), not a separate event.
- (b) What is forced is a general fact about F (Lemma STALE, PROVED: F(σ) is a pointwise optimum against σ̄(σ), never against σ̄(F(σ))).
  What breaks the counter is arena-specific: in switchbestexp, the reset bit's cycle access g_j offers a lane option, and the stale and
  true frames rank it differently. CONJECTURE CARRY-CUT (§2) is stated, but I could not prove it. I expect it to be FALSE: a gated
  counter in which every Odd-reset step leaves F and I^glo with the same arena optimum should keep I^glo's doubling. That is L-RED's
  construction (D1); recipe in §3.
- Beyond MONO-XI + argmin? YES. Lemma STALE and the mechanism use the discrete choice rule of F: the arena optimum against the OLD
  reply, (F1) of R17 (a) in G_σ̄(σ). This is exactly the kind of ingredient the parametric barrier (N5-SBC2 §4) asks for. But on
  switchbestexp it acts as a TIMING perturbation of one counter, not as a potential. It gives no bound.

## 1. The mechanism (DATA)
- Where F and I^glo differ along F's orbit (carry3.py switchbestexp_5 0 222). Only at orbit states 70 (v_0: r_1 vs v_1), 101, 147 (v_1: r_2 vs v_2), 178, 217, 218.
  At each, I^glo's strategy has a true Ξ ⊵ F's at every vertex, and strictly better at some (GLO > F at 4-14 vertices, GLO < F at 0).
- Which differences matter (hybrid.py, CLS = letters of the vertices at which a difference triggers I^glo's step):
| N | F steps | I^glo steps | hybrid CLS=g (I^glo where they differ at some g_j) | corrected steps | hybrid CLS=v |
| --- | --- | --- | --- | --- | --- |
| 4 | 258 | 286 | 286 (16 distinct patterns) | 4 | . |
| 5 | 364 | 590 | 590 (32) | 11 | 364 (30): no effect |
| 6 | 412 | 1198 | 1198 (64) | 26 | . |
| 7 | 456 | 2414 | 2414 (128) | 57 | . |
  (CLS=xyw gives the same corrected set as CLS=g: the x / y and g differences occur together.)
- What each corrected step is (SHOWD=1; N = 5, all 11). Every one is an Odd-reset step, «sbar now > after F / after I^glo» = h_i: m_i >
  e_i / e_i, so Odd resets bit i in both branches. F differs from I^glo exactly at g_0..g_i (F: h_j; I^glo: g′_j) and at x (y / w),
  y (l_0 / w). The reset bit i is 0 at 7 steps, 1 at 3 and 2 at 1. At N = 4 these counts are 3 and 1.
- Forced (forced.py switchbestexp_5 101,178,217,218): at every differing g_j, F's option h_j is STRICTLY better than g′_j in the stale frame
  val(·, σ̄(σ)) and STRICTLY worse in the true frame Ξ. So no tie-break is involved. S4a′ must pick h_j, and Schewe's optimal step must not.
- How this becomes an early carry (READING, from carry.py 205-232 at N = 5). After the lagged reset (orbit 217-219), F's bit selector
  points to the lowest bit (x → y) where I^glo's points to the high entry (x → w). The deceleration lane and the cycle accesses of the
  higher bits then follow a different schedule (lane reset b_k → s at 216, then b_k → x / d at 220). Bit 4's closing edges e_4 → f_4,
  f_4 → g_4, g_4 → h_4 become improving at 216-220 and close at 218-220. Closing g_4 → h_4 is a TRUE improvement at that state (carry2.py:
  reverting it lowers Ξ at k_4, e_4, f_4, g_4, h_4), so I^glo would also take it from F's state. The cut happens because F's earlier lags
  put the run in a state where bit 4's edges are improving while bits 1-0 still have counting to do. Pattern 01100 → 11110 at 219 → 221.

## 2. What is proved, and the conjecture
Lemma STALE (PROVED, lane; R17 (a) (F1) in G_σ̄(σ), as used in P-N5-SF ONE-PLAYER). For every σ with Iσ ≠ ∅ and A(σ) ≠ σ, F(σ) = A(σ) is a
pointwise optimum of the arena game with Odd fixed to σ̄(σ). So for every Even v and every arena option w at v,
val(F(σ), σ̄(σ))(v) ⊵ val(F(σ)[v → w], σ̄(σ))(v). F's choice depends on σ̄(σ) and never on σ̄(F(σ)). In particular, at an Odd-reset step
(σ̄(F(σ))(u) ≠ σ̄(σ)(u)), every Even vertex whose stale-best route uses u's OLD successor keeps it. This holds even when the true frame
after the step ranks it strictly lower (the situation measured in §1).
Proof. A(σ) is S4a′'s arena optimum (S1 procedure on the dual of H, P-N5-SF §0), and (F1) says the optimum of a one-player game dominates
every strategy of that game pointwise. F(σ)[v → w] is a strategy of the same arena. □
CONJECTURE CARRY-CUT (as asked; OPEN). Let G be a game in which Odd's best replies along F's orbit run through all 2^k patterns of k bits,
each bit reset being an Odd-reset step of F. Then at every reset step at which F's and I^glo's arena optima differ, the counter loses at
least one pattern, unless a GATE holds there: the reset bit's Even access vertices have no arena option ranked differently by the stale
and the true frame.
- Status: OPEN. I have no proof. The statement is only about switchbestexp-like counters, and "loses a pattern" is a DATA observation
  (N = 4..7) with no argument behind it. I do not expect it to give a polynomial bound. Even if true, it says only that F must be fed
  GATED counters.
- Which side wins (READING). The gate is a property of the arena, not of F. A counter whose resets are gated, e.g. where the reset bit's
  cycle access has a single arena option at the reset step, so that F and I^glo pick the same strategy there, gives F no point at which
  to lag. If such a counter keeps Friedmann's doubling for I^glo, it keeps it for F, and CARRY-CUT has nothing to say. So I expect
  CARRY-CUT to be harmless for a kill and useless for a proof.
- Beyond MONO-XI + argmin: Lemma STALE uses F's step rule ((F1) on G_σ̄(σ)), which MONO-XI + argmin do not see. CARRY-CUT would use it at
  reset steps. Neither is a potential.

## 3. For the Lead (route to L-RED 28 if useful)
- Kill recipe (READING, untested; I built nothing, D1). Start from switchbestexp, a counter on which I^glo doubles (I^glo's 286, 590, 1198,
  2414 reproduce here). Remove F's 2^(N−1) − N stale-reset lags: make every Odd-reset step one where F's arena optimum equals I^glo's. Two
  possible gates: (i) at the reset step, the reset bit's g_j has no improving lane edge g_j → g′_j, so it has one arena option; (ii) the
  stale exit route through m_j is no better than the lane in the stale frame, e.g. the exit m_j → z_j is already bad when the reset is
  triggered. The hybrid test here (CLS=g) is the oracle: a variant on which F's run equals the CLS=g hybrid's run has no lags, and its
  count is I^glo's.
- Confirmation of L-RED R114's READING («N5-SF leaves it at stale-escape reset steps»): exact here, with the number of such steps
  (2^(N−1) − N on switchbestexp_N, N = 4..7) and the proof that each is forced (strict in both frames).

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box56/carry.py, carry2.py, carry3.py, hybrid.py, forced.py, hyb_67.txt; check.sh block "Box 57".
- FINDINGS: (1) DATA: the early carry is caused entirely by F's stale frame at Odd-reset steps. Correcting exactly 2^(N−1) − N such steps
  restores I^glo's 286 / 590 / 1198 / 2414 at N = 4..7. Each lag is strict in both frames, so it is forced by S4a′. (2) PROVED (lane):
  Lemma STALE, F's choice never sees σ̄(F(σ)). (3) CONJECTURE CARRY-CUT OPEN; expected refutable by a gated counter (recipe §3).
  (4) The ingredient beyond MONO-XI + argmin is F's step rule. Here it acts as a timing perturbation, not a potential.
- NEEDS: none from the owner. Lead: route §3's recipe to L-RED 28 if useful.
