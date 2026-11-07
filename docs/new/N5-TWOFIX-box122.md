# N5-TWOFIX (box 122): inside a TWO-FIX window, R17's per-phase bound survives in the data once fallbacks cut the phases; TWO-FIX-POLY reduces to three counts
- L-NEW successor 44 (Opus 5.5), D14 / D18. Lead GO 2026-11-01 02:50Z: «GO for (a): BOX 122 TWO-FIX-POLY, with the ODIFF = 1 study
  first. … The key question: is «improving set from G_σ̄, choice = arena optimum in G_τ» a known rule, or reducible to one? … Until then,
  cite nothing from T12's pointers.»
- Definitions as in box 121 (docs/new/N5-BRTREE-box121.md §4): a TWO-FIX window [a, b] has τ and σ̄ fixed (σ̄ := si.Engine's optimal Odd
  counterstrategy to σ). ODIFF := the Odd vertices with σ̄ ≠ τ. W := the valuation in G_τ, Ξ := the valuation in G_σ̄.
  - A FALLBACK-FREE RUN is a maximal set of consecutive window transitions with no S4c fallback.
  - λ_W-phases are as in P-N5-GATE line L-1 (in-phase: λ_W is equal at both states of the transition).
- Tools: experiments/new/box122/windows.py (every window, one line), odiff1.py (per-step trace of an ODIFF = 1 window), runcorp.sh
  (→ w_sbcg.txt, w_alt.txt), runred.sh (→ red.txt), pincheck.sh (→ pincheck.txt).
- Status words: PROVED (lane), DATA, CONJECTURE, DEAD, READING. No literature is cited (Lead 02:50Z); L-LIT is opening the sources.

## 0. Answer
- ODIFF = 1 (DATA, §2): b5_os_n40's window of 77 steps is 9 fallbacks plus 10 fallback-free runs of at most 17 steps each.
  - W FALLS at exactly the 9 fallbacks (S4c's Even branch takes Ξ-best edges that are W-worse). W rises at every other step.
  - Ξ(o) changes twice and W(o) never changes.
  - Across the corpus, ODIFF = 1 windows have 471 fallbacks in 2,986 window transitions. The slowness is in the fallbacks, not in the
    climbs between them.
- CONJECTURE TF-PH (§3): inside a TWO-FIX window, a λ_W-phase intersected with a fallback-free run has at most n − 1 W-changing
  transitions. This is R17 (c)'s bound.
  - 0 violations in 408 corpus windows and 172 windows on L-RED's builds.
  - The same statement for a whole τ-stretch is DEAD (P-N5-GATE §6: fbg_K12_m6_m24, 403 > 289, 0 fallbacks). That stretch splits into 37
    TWO-FIX windows (σ̄ moves) and satisfies TF-PH in each.
  - So the hypothesis «σ̄ fixed» is exactly what R17's phase bound needs in the data.
- PROVED (lane) TF-RED (§4): a TWO-FIX window has L ≤ FB + (FB + 1)·(n(n − 1) + (n(n − 1) + 1)(P + F)).
  - FB := its fallbacks. P (F) := the most W-changing (W-flat) transitions in one λ_W-phase of one fallback-free run.
  - So TWO-FIX-POLY ⇐ TF-PH (P ≤ n − 1) + F poly + FB poly.
  - On the data F is ≈ 0 (32 flat steps in all ODIFF = 1 windows). FB is the live count: up to 28 at n = 32 (farrise25_n32).
- Not done: whether the rule is a known pivot rule. That waits for L-LIT's sources.

## 1. Lemmas (PROVED, lane)
- Lemma GAP-D. In a TWO-FIX window, {v : Ξ_j(v) ≠ W_j(v)} ⊆ D_j := the vertices whose (σ_j, σ̄)-play visits an Odd vertex of ODIFF.
  - So every edge in G_τ's improving set but not in Is_j (blocked), and every edge in Is_j but not G_τ's, has its target or its source's
    current successor in D_j.
  - Proof: if the play from v visits no ODIFF vertex, the (σ_j, σ̄)- and (σ_j, τ)-plays from v coincide, and VJ00 values depend only on the
    play. ∎
  - DATA, b5_os_n40: |D_j| runs from 1 to 32. GAP is constant inside early runs and grows inside later ones (odiff1.py), so it is not a
    potential.
- Lemma W-MON-RUN. At a non-fallback transition of a τ-stretch, W_(j+1) ⊵ W_j pointwise.
  - Proof: σ_j lies in S4a's arena, and the arena optimum of the one-player game G_τ dominates every strategy of the arena (RESULTS R17 (a)
    (F2)). ∎
  - DATA: W falls only at fallbacks (b5_os_n40: WDN > 0 at exactly the 9 fallback transitions).
- Lemma LAM-COUNT. A fallback-free run of a τ-stretch has at most n(n − 1) λ_W-changing transitions.
  - Proof: by W-MON-RUN each W(v) is non-decreasing along the run. In VJ00's order the cycle node is compared first, by its reward
    (injective priorities). So the cycle node of W(v) changes only to a strictly better one, at most n − 1 times per vertex. A λ_W-changing
    transition changes it at some v. ∎

## 2. ODIFF = 1 (DATA)
- Corpus windows by ODIFF (distinct (game, start, window) of length ≥ 4): 0: 122; 1: 181; 2: 42; 3: 31; ≥ 4: 32.
- b5_os_n40 (n-exhaustive/instances/b5_os_n40.pg, box121/inst/b5_os_n40_default.start).
  - Window [0, 77]: o = 7, σ̄(7) = 2, τ(7) = 7. FB 9; fallback-free runs ≤ 17; switch-best on G_σ̄ from σ_0 takes 7.
  - odiff1.py trace: W falls exactly at the fallbacks. Ξ(o) changes at transitions 29 and 31. W(o) is constant.
- Families:
  - b5_os_n12 … n40: L 16 / 20 / 24 / 32 / 49 / 60 / 67 / 77, FB 4 / 6 / 7 / 7 / 7 / 8 / 8 / 9, longest run 5 / 7 / 8 / 10 / 14 / 13 /
    14 / 17.
  - returns_rt48 / rt64 / ph64: L 68 / 76 / 93, FB 14 / 14 / 15, runs ≤ 9.
  - farrise25_n32: L 33 with FB 28 and runs ≤ 2.
- gci3_n24 (n5-epoch/instances/gci3_n24.pg with gci3_n24.start): an ODIFF = 1 window of 20 steps that IS switch-best on G_σ̄ (SBSTEP 20 = SB
  20). ODIFF counts σ̄ ≠ τ at a vertex even when it does not matter.
- Observed, NOT proposed as a conjecture: every fallback-free run of an ODIFF ≥ 1 window is shorter than n (max 20 / 24).
  - ODIFF = 0 windows already reach 49 at n = 36 (block_bk32), through several λ_W-phases. An «< n» bound has no structural reason. The
    phase form (§3) is the one that matches R17.

## 3. CONJECTURE TF-PH and its DATA
- Statement: for every N5 run on every game, every TWO-FIX window, every fallback-free run R of it and every λ_W-phase Φ: R ∩ Φ has at most
  n − 1 transitions at which W changes.
- DATA (windows.py field PHNF; corpus = L-SI box 53's 1,132 runs with box 118's lists and repaired starts):

| windows | count | PHNF > n − 1 | largest PHNF / (n − 1) | W-flat fallback-free | λ_W-changing fallback-free | fallbacks | transitions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ODIFF 0 | 122 | 0 | 44 / 47 (x32_rand48) | 2 | 88 | 14 | 2,181 |
| ODIFF 1 | 181 | 0 | 20 / 23 (gci3_n24) | 32 | 111 | 471 | 2,986 |
| ODIFF ≥ 2 | 105 | 0 | 12 / 15 (lend13_n16) | 0 | 336 | 118 | 1,608 |
| L-RED builds (box122/red.txt) | 172 | 0 | 151 / 198 (suf_K8) | 0 | — | 0 | — |

- With ODIFF = 0 every window step is consistent, and TF-PH is R17 (c) via CONSISTENT-RED. That row is a control.
- Phases that do not reset at fallbacks DO exceed n − 1 (field MAXPH):
  - x31_lem_e24: 50 > 23 (ODIFF 1); returns_ph64 91 > 63; lend107_n32 106 > 31 (ODIFF 3, the P-N5-GATE instance).
  - So the fallback cut is needed in TF-PH.
- s3quad_K8_m30: its one window of 263 transitions changes λ_W at every step (PHNF 0). The whole climb is LAM-COUNT's kind of step there
  (263 ≤ n(n − 1)).

## 4. TF-RED (PROVED, lane)
- Statement: a TWO-FIX window with FB fallbacks has L ≤ FB + (FB + 1)·(n(n − 1) + (n(n − 1) + 1)(P + F)), with P, F as in §0.
- Proof:
  - The fallbacks cut the window into ≤ FB + 1 fallback-free runs.
  - In a run, the λ_W-changing transitions are ≤ n(n − 1) (LAM-COUNT). They cut the rest into ≤ n(n − 1) + 1 in-phase pieces, each lying
    in one λ_W-phase, with ≤ P W-changing and ≤ F W-flat transitions. ∎
- With TF-PH (P ≤ n − 1), TWO-FIX-POLY ⇐ F ≤ poly and FB ≤ poly. Both are needed: each is ≤ L. So TWO-FIX-POLY ⇔ (P, F, FB all poly),
  an EQUIVALENCE.
- For N5 inside a τ-stretch this leaves: the σ̄-change transitions (box 121 §3, the fbA / fbg regime), and FB, P, F per window.

## 5. Pins (box122/pincheck.sh → pincheck.txt)
- gci3_n24 (05b980fb85a6…, start gci3_n24.start 80346d9405b9…). farrise25_n32 (red/so/instances, 8941d1c90594…, start
  box122/inst/farrise25_n32_default.start 07e800703f7e…, n5x's default start written out). b5_os_n40 (as box 121).
- All three: Oink 8fbf0a7 --zlk and --tl «solution verified»; regions AGREE; n5b identical (21 / 35 / 81 iterations).

## 6. READING (not to sign)
- TF-PH says the gate «improve in G_σ̄» does not slow the climb within a phase; it only adds fallbacks.
  - The fallback is where N5 gives up on W. S4c takes the Ξ-best switch, and W drops.
  - So for TWO-FIX the open count is how often N5 must fall back while τ and σ̄ stand still. That is a count of Ξ-progress events that are
    not W-progress.
- Next (untested), either of:
  - (a) prove TF-PH by adapting R17 (b) Lemma P (path progress), using GAP-D: blocked edges touch D_j;
  - (b) a fallback count for TWO-FIX: each fallback strictly raises Ξ while W falls back below a value it held. Test whether
    «W after a fallback ⊴ W at the previous fallback» ever repeats a W-vector, which would be a potential.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box122/{windows.py, odiff1.py, runcorp.sh, w_sbcg.txt, w_alt.txt, runred.sh, red.txt, pincheck.sh,
  pincheck.txt, inst/farrise25_n32_default.start}; check.sh block «box 122».
- FINDINGS:
  - GAP-D, W-MON-RUN, LAM-COUNT and TF-RED PROVED (lane).
  - CONJECTURE TF-PH: R17 (c)'s n − 1 holds per (phase ∩ fallback-free run) inside TWO-FIX windows (580 windows, 0 violations), while
    it is DEAD for τ-stretches.
  - DATA: ODIFF = 1 slowness = fallbacks (471 of 2,986 transitions).
- NEEDS: Lead: GO on (a) TF-PH proof or (b) the TWO-FIX fallback count; L-LIT's pivot-rule sources when opened.
