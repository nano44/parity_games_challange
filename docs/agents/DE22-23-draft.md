# Draft RESULTS DE22 and DE23 (Lead, 2026-10-18 ~18:17Z by git) — for CHECKER (with DE21-add3-draft.md and the R40 pointer) (rev. after C16: E-1 applied; R40 pointer text below with E-2 applied) — LANDED in RESULTS (CHECKER C16 + Addendum 1 PASS, checker e353339)

- DE22 (2026-10-18): L-NEW candidate N1 = Loff-Skomra IncreasingDiscountPI (arXiv 2402.03975 Fig. 12; 2610.22149 §7.4,
  Fig. 7.2) on parity-induced rewards ±n^pr, Howard switch-all for the switching player, warm starts, γ_j = 1 − 2^−j (L-NEW
  docs/new/N1-disc-anneal.md; implementation experiments/new/anneal.cpp / anneal.py, cross-checked on 1,000 games). Passed
  gauntlet step 2 on data (13 M1 families + 12,000 random games; owner told 17:58Z), then KILLED on data (owner told 18:12Z).
  Obstruction: deep traps. At every Even vertex with ≥ 2 successors add v → t_v (Odd, even priority P = B + 2 + 2k) → c_v (Odd
  self-loop, odd priority q = B + 1), k = ⌊B/2⌋ + 2, so P − q > B + 2 (experiments/new/gen_deeptrap.sh N = pgsolver_port
  switchallexp(N) + alltrap.py; regions unchanged, Odd wins all). The all-traps strategy stays discounted-optimal until a
  release phase beyond Friedmann's β_G = 1 − 1/(4|V|³ max|r|) (1106.0778 p.35); that one phase is switch-all from the
  best-reward start and replays Friedmann's counter (1106.0778 §9).
  Instances: experiments/new/instances/killer/deeptrap_sae_N1..N7.pg (claude/l-new 8ac5e5c; N7 sha1 835ce1326ca3…, n = 239).
  Even switch-all rounds in ONE phase: 11, 31, 71, 151, 311, 631, 1244 at N = 1..7 (n = 32N + 15); 5·2^(N+1) − 9 fits N = 1..6
  only (N = 7: 1244). Lead re-run (detached l-new 8ac5e5c, anneal.cpp unmodified): N = 1..6 exact, sha1 = pins, regions = Oink
  zlk. Robust (L-NEW f301bfb): start γ (--j0 1/100/400/700) and Odd's rule (--odd-howard) give the same 311 at N = 5;
  the priority-compression variant N1m dies once priorities are padded (pad_prio.py).
  Faithfulness: REFEREE-2 docs/referee-2/R2-N1-FAITH.md (referee-2 520d701), FAITHFUL WITH CAVEATS (Opus 5.5, D12):
  (C1) anneal.cpp swaps the players' roles relative to 2402.03975's DiscPI figure (Odd best-responds, Even switches) — LS on
  the negated game, allowed by 2610.22149 §7.4, where DiscPI(σ,τ,γ) is any procedure that outputs a pair of optimal policies (REFEREE-2's reading of the opened text); in LS's literal orientation G_N is easy, and the kill
  transfers by duality: LS-literal on dual(G_N) gives 11, 31, 71, 151, 311 outer switch-alls in one phase (N = 1..5, regions
  verified). So IncreasingDiscountPI with Howard is exponential in both orientations (G_N resp. dual(G_N)).
  (C2) The general claim "the parity-certificate stop fires no later than LS's mean-payoff-optimality test" (N1-KILL.md) is not proved and can fail; it is not needed: on G_N
  the all-traps strategy is never mean-payoff optimal, so LS cannot stop before the release phase.
  (C3) the closed form is a fit for N ≤ 6 only (above).
  Literature (L-LIT T19, l-lit 8d8da04): not found in any opened source; a theorem form needs two lemmas (GAPS G-N1-LB,
  optional). DATA kill, not a theorem.
- DE23 (2026-10-18): L-NEW candidate N2 = priority annealing with warm-started Vöge-Jurdziński switch-all (coarse games G_t,
  priorities below q_t set to 0; docs/new/N2-prio-anneal.md; experiments/new/n2.py + n2_si.cpp). Obstruction: block priority
  merging with one isolated self-loop dummy per priority (experiments/new/gen_padsae.sh N = switchallexp + pad_prio.py); the
  stage that reveals the low priorities replays Friedmann's counter from the coarse optimum. Instances:
  experiments/new/instances/killer/padsae_N1..N7.pg (claude/l-new f301bfb; N7 sha1 9ee0385509ac…, n = 230). Largest single
  stage 6, 15, 34, 72, 148, 300, 604 switch-all iterations at N = 1..7. Lead re-run (detached l-new f301bfb, unmodified):
  N = 3..6 give 34, 72, 148, 300 (stage counts 61/77/93/109), sha1 = pins, regions = Oink zlk. Single implementation, DATA.

- G-R14-5 pointer (append to the RESULTS gap line, rev. after C16 E-2): see L-RED R40 (docs/red/R40-tcL-contexts.md, l-red 2a75c4a):
  first-difference contexts in Even phase 0 are S − 3 (tcL(N), N ≥ 6) and S − 1 (leanT(N), n = 8N), both orders, i.e. linear in S
  and within an additive constant of the phase length S (no slack at all on leanT); no refutation of (CTX⁺).
