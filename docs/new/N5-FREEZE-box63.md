# N5-FREEZE (box 63): Lemma ODD-FREEZE for plain N5 (proved, exact hypotheses), where it freezes Odd and where it does not
L-NEW successor 34 (Opus 5.5), D14 / D18, Lead reading L40. Lead's brief 2026-10-29 19:10Z (BOX 63 (a)-(c); L-RED 29's reading, cpl.py).
Written 2026-10-29 from 19:17Z (date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME OPEN. Labels: PROVED (lane) /
DATA / READING / CONJECTURE / OPEN / DEAD.
- Engine: box21/n5x.trace (plain N5), with start files where an instance has one, else S3.
- Valuations as SPEC S1: Ξ^d_τ on G^d, computed with Even's optimal counter τ̄(τ) (the "U_τ" frame).
- NOT read for this box: box 21 Theorem B, R86 (NM*, NM*^U), R109 §4. They are cited only as the Lead relays them.

## 1. (a) Lemma ODD-FREEZE (PROVED, lane)
Setting. N5's state (σ, τ). Let τ̄ := τ̄(τ) be Even's optimal counterstrategy to τ (SPEC S1 on G^d). Let o be an Odd vertex and
e ∈ succ(o) with e ≠ τ(o). Write P_e for the (τ, τ̄)-play from e, cut at the first visit of o.
Hypotheses (at this state):
- (H1) the (τ, τ̄)-play from e reaches o before it repeats a vertex;
- (H2) the (τ, τ̄)-play from τ(o) has no vertex in P_e;
- (H3) the most relevant vertex x of P_e has even priority, and x is more relevant than the cycle node w of the (τ, τ̄)-play from τ(o).
Claim. (o, e) ∉ Iτ. Hence N5's next τ has τ_new(o) ≠ e. If (H1)-(H3) hold at every state after Odd leaves e, Odd never returns to e.
Proof.
- By H1 and H2, the play from e is P_e followed by the play from τ(o). It has the same cycle (node w) as the play from τ(o), and its
  path set (vertices more relevant than w) is that of τ(o)'s play plus the vertices of P_e more relevant than w.
- By H3, the most relevant vertex of the symmetric difference is x, which is even and lies on e's side. So in SPEC S1's order Ξ_τ(e) is
  strictly better for EVEN than Ξ_τ(τ(o)), i.e. strictly worse for Odd.
- S2 on G^d puts (o, e) into Iτ only if Ξ^d_τ(e) is strictly better for Odd than Ξ^d_τ(τ(o)). So (o, e) ∉ Iτ.
- Every change of τ is a switch of Iτ edges: S4b's arena gives Odd only τ(v) and the targets of Iτ(v); S4c's Odd branch picks from Iτ.
  This is P-N5-SF SF-TERM (i), which reads the same for N5. So τ_new(o) ∈ {τ(o)} ∪ Iτ(o), and τ_new(o) ≠ e. □
Variant ("Even CAN close"; PROVED, lane, same argument plus optimality). Replace H1 by H1′: some positional Even strategy σ_e, equal to
τ̄ off P_e, makes the (τ, σ_e)-play from e reach o along P_e. Keep H2 and H3 for that play. The conclusion is unchanged.
- S1's τ̄ is the pointwise optimum for Even ("minimising this order at every vertex at once", read on G^d). So Ξ_τ(e) is at least the
  value of the σ_e-play, which is strictly better for Even than Ξ_τ(τ(o)) by the computation above.
- This is the Lead's ODD-FREEZE: "Odd left an option whose continuation Even can make U_τ-worse".

## 2. DATA
- Exact per-state check, box59/freeze2.py: at every state of N5's run, every (o, e) satisfying H1-H3 is tested for membership in Iτ.
  - dw_3: 81 hypothesis hits, 0 violations.
  - nep22f_n64: 153 hits, 0. lend47_n32: 6 hits, 0. gci3_n24: 0 hits.
  - Corpus (box59/sbcg.lst, 719 games): box59/freeze2_all.txt, see §2.1.
- At-leave-time form (box59/freeze.py). It tests only "Odd leaves e at k; P_e under the NEW τ reaches o with an even top", with no H2,
  no H3 relative to w, and no persistence, and asks whether Odd ever returns.
  - 719 games: 9175 leaves, 833 of them with that form; 1684 returns, 117 of those protected at leave time, in 48 games.
  - So "protected when left ⇒ never returns" is DEAD as stated. First instance: n5-epoch/instances/gci3_n24.pg, step 2, o = 0, e = 6.
  - The exact lemma is not contradicted: those returns happen at states where H1-H3 no longer all hold (Even's best reply changed),
    e.g. gci3_n24 has 0 exact hits.
- Coupled / dual families (R111-R113's instances, own start files):
  - relay_L3 / L10 / L10_s3: 7 / 21 / 21 leaves, 0 returns.
  - ewin_runquad: 7 leaves, 0 returns.
  - dewin_runquad_K3_m4 and d_s3quad_K3_m4: 37 leaves, 20 returns.
  - d_runquad_K8_m30_n192: 513 leaves, 450 returns.
  - d_hntop_n8 (n 168, N5 291 iterations): 3642 leaves, 3276 returns.
  - In none of them did a return follow a protected leave. Odd is NOT frozen in general: on the dualised families Odd's own τ-run is
    long, with returns at unprotected options.
### 2.1 Corpus per-state check
- 719 games (box59/sbcg.lst; S3 start), all printed: 35780 hypothesis hits, 0 violations (box59/freeze2_all.txt).

## 3. (b) What ODD-FREEZE gives toward G-N5-TIME (READING / CONJECTURE)
- Call an option e of o PROTECTED if H1′-H3 hold at every state of the run. Then Odd's τ(o) visits each unprotected option in turn, and
  each protected option at most once (only as the starting value). So #τ-changes ≤ Σ_o (#returns among unprotected options).
- If every non-final option of every Odd vertex is protected, then τ(o) changes at most deg(o) − 1 times, and #τ − 1 ≤ m. That is
  dwN / fcN, where Odd's options at h_i are the closable cycle e_i (protected: top h_i even, more relevant than q) and the escape: τ
  changes exactly N times (DATA).
- With CONJECTURE FRAME-STRETCH (box 62, 0 / 719), #σ − 1 < (n + m)·#τ. So on the class "all Odd options protected", N5 would make
  I < (n + m)(m + 1) + m iterations: a polynomial bound conditional only on FRAME-STRETCH.
- How it composes with R86's NM* / NM*^U: NOT READ; I do not claim a composition.
- What it does not give: any bound when Odd has unprotected options. The dualised families above have thousands of unprotected returns.
  There the τ-run is a genuine Odd-side improvement run, and ODD-FREEZE is silent.

## 4. (c) Prediction for L-RED's frozen-run climb (CDAG_n plus Odd masks) (READING)
- Under pinned τ, Even's run against a frozen frame is the "unary forced" regime (L-RED's R109 §4, as relayed). For the climb to be long,
  Odd's τ must keep changing, i.e. Odd must return to options it left.
- ODD-FREEZE says each return has to be at an option that is NOT protected at that moment: Even cannot route it back to o through an
  even top more relevant than o's current cycle node.
- So Odd masks built from closable cycles (Even-closable, even top) must fail. A working mask must give Odd options whose continuation
  Even cannot loop back with an even top, as in the dualised hntop / runquad families (d_hntop_n8: 3276 returns).
- If CDAG_n's Odd masks are closable cycles, the attack fails at the first mask bit. If they are odd-topped or exit-type options, the
  lemma is silent, and the question becomes FRAME-STRETCH plus the length of Odd's own unprotected run.

## DONE / FINDINGS / NEEDS
- DONE: box59/freeze.py, freeze2.py; freeze_all.txt, freeze2_all.txt; this note.
- FINDINGS:
  (1) PROVED (lane): Lemma ODD-FREEZE with exact hypotheses H1 (or H1′: Even CAN), H2, H3, from S2 on G^d, S4b / S4c and S1's
  optimality. 0 per-state violations on 719 games (35780 hits).
  (2) DEAD: the at-leave-time form (117 protected-then-return cases in 48 games, first gci3_n24); protection must hold at the return state.
  (3) READING: all-protected Odd options give #τ − 1 ≤ m, hence, with FRAME-STRETCH, polynomial N5. dwN / fcN are in that class;
  the dualised families are not (thousands of unprotected returns).
  (4) Prediction: L-RED's climb must use unprotected Odd masks.
- NEEDS: none from the owner.
