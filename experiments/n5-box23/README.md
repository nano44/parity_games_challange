# Box 23: true maxima of R*_F and FL_F per W-run of plain N5 (L-COMP successor 8)
Lead brief 2026-10-30 (D18): "a measurement beats an inference". FRONTIER: inside one W-run of plain N5, R3-POLY ⇐ R*-POLY ∧ FL-POLY
(l-new 893b9346, docs/new/N5-FREE-box85.md §3, Theorem FREE-RED, lane-PROVED: |F| ≤ (n − 1)(R*_F + 1) + FL_F). Every number here is
DATA unless labelled. Labels: DATA, PROVED (mine, unrefereed), CONJECTURE, READING. Not a TARGET.md claim. G-N5-TIME open.
STATUS: IN PROGRESS (interim push; tables (b), (c) are being filled).

## Definitions (from the text: RESULTS R88, R89; box 85 §3). Implementation rstar.py, on L-COMP's engine n5b (SPEC mode)
- State t = (σ_t, τ_t); transitions = n5b.N5.run's loop body (box17.Eng.step); fb_t = S4c fallback flag of t → t + 1.
- Ξ_t := VJ valuation of σ_t (Odd best reply); Iσ_t := Even edges (y, z) with Ξ_t(z) strictly better than Ξ_t(σ_t y) (SPEC S2).
- W_t := VJ valuation of σ_t in the game with Odd restricted to τ_t (the (σ_t, τ_t)-plays); λ_W := its cycle-node map.
- W-run (R89): maximal run of consecutive states of one τ-stretch none of whose transitions is an S4c fallback or changes λ_W.
- BLOCKED at state q (R88): y Even, z ∈ succ(y), z ≠ σ_q(y), W_q(z) ▷ W_q(σ_q y) and (y, z) ∉ Iσ_q.
- R*_F (R88's R*_T on F): transitions t → t + 1 of F at which some Even y adopts (σ_{t+1}(y) = z ≠ σ_t(y)) an edge BLOCKED at an
  earlier state q of F. Headline reading "strict" q < t (Lead reading 13:22Z; = xirise.py); "incl" q ≤ t also computed.
  PROVED (mine, one line): incl = strict on every run. S4a moves y only to σ_t(y) or along Iσ_t (its arena), and S4c only to a
  Ξ_t-best, hence improving, successor; an edge blocked at t is not in Iσ_t, so it is never adopted at t → t + 1. Checked: 0 W-runs
  with incl ≠ strict anywhere below.
- FL_F (R89's FL_S on F): transitions of F with σ_{t+1} ≠ σ_t and W_{t+1} = W_t.
- Also per W-run: |F|, la = max late adoptions of one edge, sig0 = transitions with σ unchanged (box 84 §4: always 0; 0 everywhere here).

## (a) Cross-check against L-NEW's xirise.py (read only, l-new 893b9346), box-83 corpus (1,132 runs) — DONE, 0 disagreements
- xcheck.py: per game, (number of W-runs, max R*_F, max FL_F, max |F|, FREE-RED violations) from rstar.py vs L-NEW's committed
  new/box85/xirise_{sbcg,alt}.txt; and xirise.py re-run (unmodified, own process) on the first 15 games of each list: 30/30 print exactly
  the committed line. Result (results/xcheck.txt): 1,132 / 1,132 agree, 0 disagree, 0 failures. Corpus max R*_F 64 (gate_K64_n581),
  max FL_F 8 (u23sw64_n32): L-NEW's maxima reproduced.
- One disagreement found and resolved on the way: red/n3/instances/n3cov_lean.start is INVALID (L-RED R99 erratum: wrong-owner entries).
  n5x drops wrong-owner entries implicitly; my first reader did not (run of 20 iterations instead of 35). rstar.py now builds the start as
  R99's fullstart2.py does (S3, overridden by every valid entry); with that and with n3cov_lean_fixed.start both tools give R*_F 4,
  |F| 30 (n3cov_phi_fixed: 5, 9). The corpus line for n3cov_lean is therefore a faithful run (= the _fixed start).
- Limitation: the comparison is per game (maxima and run count), not per W-run.
