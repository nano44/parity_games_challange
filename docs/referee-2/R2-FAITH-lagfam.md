# R2-FAITH-lagfam: faithfulness check of DE21 (addenda) and the R12 (c) / R13 (c) post-landing notes on pinned C++ — REFEREE-2, 2026-10-18 (date -u ~03:45Z)
(Opus 5.5, D12). The Lead asked for this at 03:53Z (Lead clock). It is not a packet. Trunk 9338ddd.

## What was run
- Instances: `python3 -I experiments/red/lag/lagfam.py D out.pg` for D = 2, 3, 4, 5, 6, 7, 8, so n = 7D + 22 = 36 … 78.
  The D = 4 and D = 8 outputs have sha1 prefixes c8fd8616 and 46ad828c. These are byte-identical to the pinned fam_D4_n50 and
  fam_D8_n78 cited in DE21.
- Solver: my logging-only instrumentation of the pinned dtl.cpp @ 8fbf0a7 (docs/referee-2/R2-P9/dtl_probe9.patch: set-level
  logs, plus a log line on each successful attractTangle).
  - Every run reproduces the pinned build exactly: "solved in D + 8 iterations" (10 … 16), and the same "found 1 dominions
    and 2D + 9 tangles".
  - Every run ends with "solution verified".
  - The pinned binary tools/oink/build/oink gives the same iteration counts.
- Orders:
  - pinned: the file as generated, Oink's own sort;
  - stable: docs/referee-2/R2-P9/stablerel.py relabels by (priority, input id), so Game::sort keeps the order (game.cpp 480),
    plus ascending ins (R2_REV=1).
- Checkers: my own docs/referee-2/R2-P9/an9.py (events, re-steals, CHARGE causes as in R2-P9 §2, depth) and
  docs/referee-2/R2-P10/an10.py (entries/exits on the FIXED grid: every round, including G9-b2 virtual rounds, × every p-vertex
  τ of R, × every w ∈ R). They do not use L-ALG's dtl_stealdepth.py or dtl_prefexits.py or pyref.

## Results (identical in both orders, for every D)
| D | n | iterations | re-steals | all with a CHARGE cause | max depth | max k_q | max exits per (σ, w) | events Σ_q k_q | max total exits in one context (= all exits) | max \|F_σ(i)\| |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 36 | 10 | 2 | yes | 2 | 2 | 2 | 6 | 64 | 8 |
| 3 | 43 | 11 | 4 | yes | 3 | 3 | 3 | 9 | 111 | 9 |
| 4 | 50 | 12 | 6 | yes | 4 | 3 | 3 | 12 | 177 | 10 |
| 5 | 57 | 13 | 9 | yes | 5 | 4 | 4 | 16 | 264 | 11 |
| 6 | 64 | 14 | 12 | yes | 6 | 4 | 4 | 20 | 376 | 12 |
| 7 | 71 | 15 | 16 | yes | 7 | 5 | 5 | 25 | 515 | 13 |
| 8 | 78 | 16 | 20 | yes | 8 | 5 | 5 | 30 | 685 | 14 |
- No failures of any lemma check: CHARGE's corrected intermediate claims, ENTRY-CHARGE steps 1-3, N*_R ≤ N_ent, C3, and
  |F_σ(i)| ≤ |region| − 1.
- The narrow-grid variant (an10b.py, τ ∈ V_r of the earlier visit) gives the same exit counts on this family. So the grid choice
  does not matter here.

## Answers
(1) Re-steal depth and k. My checkers give max depth = D and max k_q = ⌊(D+1)/2⌋ + 1 for every D in 2-8, in both orders.
Every re-steal has a cause under my own CHARGE definition (an event at a pair strictly between, at a strictly earlier step,
with the prefix P(σ⁺)).
- This AGREES with DE21's addendum: depth = D; k = 2, 3, 3, 4, 4, 5 at D = 2, 3, 4, 5, 6, 8.
- So (STEAL-DEPTH_D) is false for every constant D on a faithful run. CONFIRMED.

(2) Exits on the fixed grid. Max exits per (σ, w) = ⌊(D+1)/2⌋ + 1 = ⌈D/2⌉ + 1, i.e. 2, 3, 3, 4, 4, 5, 5 for D = 2 … 8, in both
orders.
- For EVEN D this AGREES with ADDENDUM 2 (2, 3, 4, 5 at D = 2, 4, 6, 8; D/2 + 1).
- So (EXIT_c) is false for every constant c on a faithful run. CONFIRMED.

(3) Disagreements with the Python tools. None in substance. Two wording or definition points:
- The formula. The Lead's message writes "⌊D/2⌋ + 1", and ADDENDUM 2 writes "D/2 + 1". The addendum measured only even D. At
  ODD D my max is ⌈D/2⌉ + 1, one more than ⌊D/2⌋ + 1 (3 at D = 3, 4 at D = 5, 5 at D = 7). The formula valid for all D on my
  data is ⌊(D+1)/2⌋ + 1, the same as max k. The refutation is unaffected.
- Totals. My max total exits per context, 64 / 177 / 376 / 685 at D = 2 / 4 / 6 / 8, are larger than ADDENDUM 2's
  25 / 75 / 166 / 310 per context. On this family all exits fall in one context.
  - My count includes virtual rounds (G9-b2) on the fixed grid; ADDENDUM 2 presumably counts aligned rounds only.
  - My grid definition is the one the ENTRY-CHARGE step count needs (R2-P10 G10-a1).
  - Both are polynomial on these data (mine grows roughly as D², about n²/9). So "(EXITS-POLY) not refuted on the family"
    stands under either definition.
- Faithfulness verdict: the counterexample data of DE21 and its addenda REPRODUCE on instrumented pinned C++ in both orders.
  This is not an artefact of the Python tools.
