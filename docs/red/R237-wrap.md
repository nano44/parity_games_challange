# R237 (item 1): Lemma WRAP's six counters on L-RED's own engine (L-RED successor 66)
Written 2026-11-12 (date -u in the commit). Lead 17:08Z: «(1) Run WRAP's six must-0 counters on YOUR engine n5x236 over the frozen
W(H, s0) instances: the 300 random, W_n and F_n n = 2..8, and W(G_n, ι) on Friedmann's Table 4 game n = 1..4. Report the iteration
counts against L-SI's … Any difference is to be classified as in your 16 (tie rule / start / fallback / real). (2) Attack WRAP's new step
(W4) … If R237 will not fit, do (1) only and hand (2) over.» Object: claude/l-si 26704e01 experiments/si/box104. Labels: DATA (unit, set,
scope, counter). Independence: «up to SPEC's cycle-node and S4b tie rules» (R236 §2).
Tools: experiments/red/r236/wr237.py, cls237.py.
- wr237.py reuses box 104's wrap104.py for the OBJECTS only: wrap(), fried_game(), lmcs_game() and the frozen JSON (env BOX104, LNEW,
  LRED, LLIT = claude/l-lit 5c53efbd).
- The N5′-xi run (n5x236), the H-valuation (n5x236.Val + Odd's one-player optimum on H) and the six counters are L-RED's own.
Item (2) is NOT done: it is handed over (notes/L-RED.md, HANDOVER 66 → 67).

## 1. Results (must-0: s3fail, nonstd, nohoward, fbwrong, endwrong, wrong; unit as in wrap104.py's header)
- W(G_n, ι), arXiv 1106.0778v2's G_n:
  - n = 1..4, both priority versions (fig4 and table4): iterations 11 / 29 / 65 / 137 = T + 3 with T = 8 / 26 / 62 / 134, equal to box
    104's 11, 29, 65, 137.
  - Every counter is 0. Outputs: out/wr237_lmcs_fig4.out, out/wr237_lmcs_table4.out.
- W(switchallexp_n): n = 2, 3 give 33 / 73 = Howard T + 3 (30 / 70), every counter 0. Larger n not run here; F_n = Γ3* of the same G_n
  is R236 (n = 2..8).
- F_n, n = 2..8 (R236, out/f236_free.out): 33 / 73 / 153 / 313 / 633 / 1,246 / 2,489, with 1 fallback, equal to box 104.
- The 300 frozen random games (inst/rand300.json; out/wr237_json.out):
  - every counter is 0 on all 300;
  - 286 rows equal box 104's (T, iterations, |W|); 14 rows differ by ±1 in T and in iterations together, so iterations = T + 3 holds on
    both engines.
- Control CTRL=1 («best» := worst): nohoward 660 on W(switchallexp_2) (fires). out/wr237_ctrl.out.

## 2. The 14 differing rows, classified (cls237.py, against box 190's n5v xi on the same W(H, s0); out/cls237.out)
- Rows 32, 56, 57, 75, 79, 97, 161, 190, 198, 203, 257, 260, 263, 264.
- start 0, fallback 0, real divergence 0: all 14 are the tie rule.
- In each row the first differing state, restricted to H's Even vertices, is state 1. At every Even vertex of H whose choice differs
  there, BOTH engines' choices are best successors by H's own valuation at state 0: a Howard tie in H.
- Inside W(H, s0) such a tie is decided by N5′-xi's S4a rule (best Ξσ, then SPEC's choice, then the larger index). My engine's readings
  R2 / R3 (cycle-node and S4b ties) can resolve it differently from n5v, and H's Howard run then takes a different but equally legal
  path (T ± 1).
- This is WRAP's own statement («a Howard run of H», any legal tie resolution), so it confirms WRAP on both runs.

## 3. CORRECTION (L-RED successor 68, 2026-11-12T20:37Z by date -u; Lead brief item 2): n5x236's «spec» mode is not SPEC's tie rule
- R236 §4 (docs/red/R236-fn.md l. 64) says «n5x236 in spec mode, with my tie readings, gives 3 iterations on every F_n». The «3» is
  correct only as a property of n5x236's own tie readings (R1-R3). It is NOT N5's (SPEC's) count, so nothing about N5 may cite it.
- N5's count on F_n, from the SPEC-exact engine n5s237 (successor 67; state by state equal to box 190's n5v on 8,900 random games,
  experiments/red/r237/out/xs237.out, xg237.out), experiments/red/r237/out/fn_spec.out (committed 0f27cab02):
  | n | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | n5s237 spec (iterations, 1 fallback each) | 5 | 5 | 5 | 5 | 6 | 6 | 6 |
  | box 104 n5v spec (claude/l-si 26704e01 experiments/si/box104/out/free_spec.out) | 5 | 5 | 5 | 5 | 6 | not run | not run |
  | n5x236 «spec» (own readings, NOT SPEC) | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
- So N5 (SPEC) and box 104 agree on n = 2..6 (5 / 5 / 5 / 5 / 6). The Lead brief's wording «5/5/5/5/6 on F_n n = 2..5» lists five
  values, which are the counts for n = 2..6.
- Rule from here on: anything about N5's tie or key rule (box 105's replay, (W4)'s N5 half, WRAP (v)) runs on n5s237. n5x236 stays a
  second engine for N5′-xi only, where its readings change tie resolution but not WRAP's counters (§2).
- R236's F_n verdict for N5′-xi (33 / 73 / … / 2,489; R236 §1-§3) is unaffected: it is xi mode, not spec mode.
