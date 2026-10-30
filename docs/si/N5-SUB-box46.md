# N5-SUB (box 46): GP*-RUN on sub-intervals, and the local form of FW-R*. Both proved; neither bounds REP (latew: 640 local late transitions in one W-run)
L-SI successor 31 (Opus 5.5), D15 / D18, Lead reading L40. Lead 2026-10-30 01:23Z: «your queued idea, GP*-RUN on a SUB-interval of a W-run
with lateness read relative to that sub-interval. First check that every property GP*-RUN's proof uses is inherited by sub-intervals. Then see
whether it gives REP* ≤ poly per W-run, or a plain-wave bound. Test it first on L-RED's latew_K20_m32 / K24_m40 … Any bound must allow
that.» Working note, unrefereed. G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Tool: experiments/si/odd/repchain.py + per-W-run counters WCH, RT (= R*_T), RLOC, REP (maxima WCHW, RTW, RLOCW, REPW) and LOC_V.
  Corpus odd/out/repchain_corpus.txt (re-run). latew_K24_m40 is not on l-red's tree (checked at box 45): not run.

## 1. Inheritance (PROVED, lane; a READING of R88 §3-§4 = R89 GP*-RUN's proof, line by line)
- R88's proofs of GP* and FW-R* (docs/si/P-N5-GP-box31.md §3, §4; R89 GP*-RUN reads them on W-runs) use, of F = [a, b]:
  (1) no transition of F is a fallback and τ is constant (W-MON at each k → k + 1, [S4a]'s arena H_k);
  (2) λ_W constant on F (base case L = 0; B1′ (ii), B2a, B2b (i), (iii); "u is a cycle node of state a" in FW-R*);
  (3) BLOCKED and Iσ read at states of F; (4) nothing about a − 1 or b + 1 (maximality is never used).
- All four hold for every sub-interval F′ = [a′, b′] ⊆ F, with "cycle node of state a′" (= of state a, by (2)) and BLOCKED read at states
  of F′. So: Lemma GP*-SUB (PROVED, lane): GP* and FW-R* hold on every sub-interval of a W-run, with R*_T(F′) := the transitions of F′
  containing an adoption of an edge blocked at an earlier state OF F′.

## 2. The local form (PROVED, lane; from FW-R*'s proof)
- FW-R*'s proof charges each W-changing transition k ≥ a + n − 1 to a late adoption at τ ∈ (t, k] of an edge blocked at t = k − 1 − i ≥
  k − n + 1. So τ − t ≤ n − 1: the blocked state lies in the last n − 1 states before the adoption.
- Corollary LOC-R* (PROVED, lane). Call a late adoption at u LOCAL if its edge was blocked at some state ≥ u − n + 1 of F. Then
  WCH(F) ≤ (n − 1)(RLOC(F) + 1), RLOC := the transitions of F containing a LOCAL late adoption. (FW-R* with R*_T replaced by RLOC ≤ R*_T;
  the same charging, each τ charged by ≤ n − 1 values of k.)
- GP*-SUB is the special case "blocked at a state ≥ a′".

## 3. DATA, and the verdict on REP
| instance | n | WCH (max W-run) | R*_T | RLOC | REP in that W-run | LOC-R* violations |
| --- | --- | --- | --- | --- | --- | --- |
| latew_K20_m32 (L-RED, .start) | 538 | 700 | 640 | 640 | 570 | 0 |
| runfam_K40 | 79 | 159 | 8 | 8 | 1 | 0 |
| corpus (719 games) | | | max 17 (so_j19_n48) | = R*_T in every game | max 6 | 0 |
- Every late adoption measured is LOCAL (RLOC = R*_T in all 720 runs). So the sub-interval and local forms sharpen nothing in the data.
- REP: they give no bound on REP* per W-run. A repeat of (y, z) can be local (latew: all 570 are), and LOC-R* only bounds W-changes by local
  late transitions, the same circle as before (REP ≤ WCH(z) + SIL + CYC, P-N5-CUT §6).
- Plain-wave bound: no. Between two local late transitions the W-run has at most n − 1 W-changes (that is LOC-R*); the plain waves of box 45
  are exactly these, and their number is RLOC + 1, unbounded here.
- DEAD: CONJECTURE REP-LIN (box 42, REP_F ≤ n per W-run). Kill: latew_K20_m32 (L-RED, sha1 063d173c2de7, with its .start): 570 > n = 538
  REPEAT late adoptions in ONE W-run (my engine, repchain.py; L-RED R128 measures the same family). Obstruction: one FIRST late adoption
  re-enables Θ(n) edges (breadth, box 45).
- The quantity any bound must allow: R*_T = 640 > n in one W-run at n 538. So R* per W-run is not linear either; [P-REP] / [P-LATE] need at
  least a quadratic exponent.

## 4. Composition toward G-N5-TIME
- §1-§2: two sharper forms of GP*-RUN (PROVED, lane). They change no premise of P-N5-CUT: [P-REP] stays OPEN, and REP-LIN is DEAD; any
  polynomial [P-REP] must allow REP = Θ(n²)-type growth (latew).

## DONE / FINDINGS / NEEDS
- DONE: repchain.py counters; corpus re-run; si/check.sh «box 45» pin extended, «box 46» pin; DEAD.md «box 46»; this note.
- FINDINGS: 1. PROVED (lane): GP*-SUB, Corollary LOC-R*. 2. DATA: every late adoption is local (corpus and latew). 3. DEAD: REP-LIN
  (latew_K20_m32, 570 > 538 in one W-run). 4. No REP bound and no plain-wave bound from the sub-interval form.
- NEEDS: none from the owner.
