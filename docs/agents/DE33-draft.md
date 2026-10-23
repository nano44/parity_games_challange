# Draft RESULTS DE33 (Lead, 2026-10-23 21:25Z by date -u) — awaits CHECKER C25 (re-runs at the exact commit, statement diff)

- DE33 (2026-10-23): N10a, N10b, N10c = LP relaxations of the 0-1 program ACYC (N9-screen §1(e), level 0) strengthened by ESCAPE cuts,
  separated exactly by minimum cuts (L-NEW successor 7, box 19, (c) lane under D14/D15; docs/new/N10-screen.md §0-§3,
  experiments/new/esc/; l-new b8a4282, 25b7ac2). Lemma B (§0, PROVED by the lane, unrefereed): ESCAPE cuts are valid, and ACYC + ESC1 is
  exact on one-player games of either owner (data: 924 one-player queries and circ(n,1,2), n = 3..10, 0 gaps). All three are DEAD ENDS
  at gauntlet step 2 on two-player games (DATA):
  (a) N10a (ACYC + ESC1): gaps (feasible although Odd wins a vertex) in 15 of 800 two-player queries (random seeds 0..299, n = 3..12;
      results/rand300.txt); in 12 of the 15 no ESC1 cut was ever violated.
  (b) N10b (+ ESC-tau, Odd's strategy tau from the REGION LP of N9b): 0 gaps in 800 and 3 in 5,432 random queries, 0 in 17,528
      exhaustive n = 3 queries (every 10th game), 2 on hard families (counter_symsi N = 2, 3, Odd query). Smallest gap:
      instances/esc_gap_r1794_Q1.pg (n = 8, sha1 ab859e3f4acf4ca223bc7af905010d59db758d66; Oink zlk: Even wins only vertex 5); no
      violated cut was found.
  (c) N10c (conditioning on the N10b oracle; Lemma D, PROVED by the lane, unrefereed: YES answers are correct, NO-instances get NO,
      never wrong on one-player games; errors one-sided): STUCK on yes-instances r1569 (n = 14, instances/cond_stuck_r1569_YE.pg, sha1
      c7715537ff454341b3309ea058796c1f759c1ba6; 1 of 8,000 random games) and counter_symsi N = 3 restricted to W_E (n = 32,
      instances/cond_stuck_symsi3_YE.pg, sha1 4483eb7c813989cb79edf76c6e604367d39db75a); the r1569 failure is an N10b gap at n = 14
      (instances/esc_gap_from_r1569.pg, sha1 194a1ff6c5d83307f221180b39cdba11eb891c06; the LP point passes a residual check ≤ 1e-6).
      The hard-family run was stopped after counter_symsi N = 3; tc, tc+ N = 1, 2 and switchallexp N = 3 are NOT FINISHED for N10c.
  Lead re-run (pip scipy 1.18.1, highspy, networkx; experiments/new/esc, python3 -I): all five pinned sha1s reproduced;
  esctest.py files esc_gap_r1794_Q1.pg --tau: "GAP … Q1 n=8 cuts=0" (N10b); without --tau: gaps on Q1 and Q2 (N10a); condtest.py
  files cond_stuck_symsi3_YE.pg cond_stuck_r1569_YE.pg: STUCK on both (21 oracle calls, 654 s); Oink zlk: Even wins exactly 1 of the
  8 vertices of esc_gap_r1794_Q1 and all 14 of cond_stuck_r1569_YE.
  READING (lane, §5): one-player exactness is cheap (a min-cut family); the remaining difficulty is Odd's strategy tau, which the cuts
  do not supply; every N10 failure is a game where no LP-guided tau exposes a violated cut. N10d (exact (U, tau) separation) not run:
  finding a separating tau is finding an Odd dominion, the problem itself.
