# Draft RESULTS DE34 (Lead, 2026-10-24 02:58Z by date -u) — awaits CHECKER C26

- DE34 (2026-10-24): N11 = N5-HT, N5 (SSI-GLOBAL, docs/new/N5-ssi-global.md) with an honest override at trust conflicts (at
  each Even vertex x where N5's step is honestly worse than the best edge of Iσ, i.e. key(Ξσ(σ_W(x))) < max over (x, z) ∈ Iσ of
  key(Ξσ(z)), take that best edge, ties to the larger index; Odd symmetric on G^d; L-NEW successor 8, box 23, (c) lane under
  D14/D15; docs/new/N11-proposal.md, rule frozen in its FREEZE section at l-new e003f7e before any run, code
  experiments/new/n11/n5ht.py sha1 598cc9000e293e2a6e59e0cc9b030dd0b4912604; l-new 138ea49, 5f27c48) is a DEAD END at gauntlet
  step 2 (runtime growth, DATA). Termination and correctness are not in question: σ', τ' switch subsets of Iσ, Iτ, so RESULTS R15
  applies. Faithfulness (faith.py 1500 12 31): with the override off, traces equal n5.py on 1,500 of 1,500 random games; every run
  with no conflict (1,137 of 1,500) equals N5's trace.
  Families (experiments/hard-families/pgsolver_port.py, deterministic), canonical start, every output with regions = Oink zlk and
  both strategies verified (check_sol2.py), results experiments/new/n11/results/:
  (a) Friedmann's switch-best family switchbestexp N = 2..8 (n = 25N + 10): N5-HT iterations 61, 141, 301, 621, 1,261, 2,541,
      5,101 = 20·2^N − 19 exactly (DATA, N ≤ 8); N5 on the same games 32, 41, 47, 55, 62, 68, 77. N = 4 sha1
      57b27b7476bcb72bae29fc5e8b2221be0609e8ec, N = 8 sha1 7082e7242d8250993d175771c1e2ac17372fb31c.
  (b) Friedmann's switch-all family switchallexp N = 2..8 (n = 14N + 7): 30, 70, 150, 310, 630, 1,243, 2,486 (= 10·2^N − 10 for
      N ≤ 6, then ×2.0 per step); N5 8 … 16. N = 6 sha1 5dc850b156c6d1e2adace088b58c0f65cc9e0bf2, N = 8 sha1
      18c2462457856437590d82018d0e9140916a67a6.
  DLM families 1-2 from their start pairs: linear (≤ 17 iterations at n = 72); not a kill.
  Lead re-run (trunk experiments/new/n11/bench.sh with OUT/TMPD in the Lead scratchpad; n5ht.py sha1 = frozen): switchbestexp
  N = 2..8 and switchallexp N = 2..8, every row = lane CSV (iterations, conflicts, N5 iterations), every row "zielonka(oink zlk)
  OK strategies verified"; generated sha1s = lane.
  Obstruction (lane, N11-proposal.md RESULT): on these games the conflict set is large at almost every iteration (17,882
  conflicts in 5,101 iterations at switchbestexp N = 8) and the override is switch-all's own choice, so N5-HT replays Even
  switch-all SI (READING; the counts equal Even switch-all from σ_0 on switchbestexp N = 2..5, box 21 table) and meets BARRIERS
  B8 (Friedmann LMCS 7(3:19) 2011, Thm 6.14, Thm 8.4). Not run (dead at the first test): R56/R57 families, frozen climbs, the
  I3/I4 invariant test. READING (lane): a repair of N5's trust-mode deadlock that falls back to honest-greedy choices on
  conflicts collapses to switch-all on Friedmann's games.
