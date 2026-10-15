# L-RED notebook (independent adversary; Lead brief 2026-10-15 11:30Z, 8 h box)
Owns docs/red/, experiments/red/, this file. Reads other lanes' files, never edits them. Messages only the Lead.

## Resume point
2026-10-15 ~14:30Z. R1 (MSF killed, 7a7ed5e) done. R2 (S1 Random-Action-Removal killed by FHZ 1410.7530 Thm 6.3 + transfer lemma,
docs/red/R2-RAR.md, experiments/red/fhz.py) written, kill messaged 14:05Z; pushing now. Larger relation checks done: (8,2,3,2) 400, (10,1,1,1) 1500,
(6,3,3,3) 300 samples, 0 differences (recorded in R2).
Box ends ~19:20Z; idle after the push unless the Lead sends more.

## Queue
1. Push R2; message the SHA. 2. Optional: a growth run with FHZ's parameter
scaling (r = t = ceil(log2 n), s = ceil(sqrt(n) log2 n)) for n up to ~16 to show the mean leaving the n^2 trend (slow).

## Things only I know
- L-SI's branch is read through a detached worktree in the scratchpad (git worktree add <scratch>/lsi origin/claude/l-si);
  experiments/red/xcheck.py --lsi <that path> compares switch sequences with si.py. The worktree is not in the repo.
- vj.py classifies "cycle-creating" by Odd's play (on_play), not by the path bit; its stats line prints cycle-creating /
  escapes / cycle-node changes per run. In a sink game every switch that closes an even 2-cycle is an escape.
- gated_bland: ids sink 0; a_i = 5i-4, b_i = 5i-3, d_i = 5i-2, e_i^a = 5i-1, e_i^b = 5i; b_{N+1} = 5N+1. Gate priorities
  4..4N+2 (even), d_i = 3, underlying shifted by 4N+4. Best-reward start = sigma_0 (e_i^a has the higher even priority).
- Runtime of vj.py msf on gated_bland: N=10 1.3 s, N=12 6.9 s, N=13 17 s (one valuation per switch, no incremental update).
- Oink is built (scripts/setup_oink.sh, ~3 min); MSF on tc/tc+/counter_* via si.py was linear or near-linear (sweep in
  the scratchpad, not pinned: tc N=8 275, tc+ N=10 595; all PGSolver families linear in N).

## Things only I know (R2)
- fhz.py: FHZ's "zero-edges" are the bit-0 edges a0, b0, u0, w0 = the COSTLY ones (B0 is made of them); "one-edges" are the
  0-cost chain edges (the optimum). I first read it the other way and got 0 switches.
- The parity encoding must share class vertices across entries into a level (class B = nothing, class A = shared even g_i,
  class C = shared odd o_{i,d}); separate cost vertices per source with equal priority break the lexicographic tie by index and
  the models disagree (first attempt, caught by the lockstep assert at n=3).
- fhz.py export prints the start as 'spec:v:w ...' for si.py; for t=1 it equals the best-reward start; for t>1 best-reward
  takes the last copy, also a zero-edge tree.
- Speed: my RF driver re-evaluates the whole tree per test (O(|V|)): (7,2,3,3) with 72k tests takes ~1 min; si.py rar on
  fhz_n5_r2s2t2 (256 vertices) takes minutes per seed.

## Sources opened (arXiv id or DOI, theorem/section)
- Friedmann-Hansen-Zwick, "Random-Facet and Random-Bland require subexponential time even for shortest paths", arXiv 1410.7530
  (PDF opened 2026-10-15 ~13:25Z): section 3 p.7 (how Random-Facet finds shortest-path trees), section 4 pp.7-9 (randomized
  counter, Fig. 3 one level with r=s=t=1, "zero-edges"/"one-edges", gadgets: t copies, paths of length s, r copies), section 5
  Table 1 p.14 (edges, costs 2^{2i+1}+(k-1)eps, 2^{2i+1}+1+(j-1)eps, 2^{2i}; eps = 1/(rs)), p.14 B0 "composed entirely of
  zero-edges", Def. 5.2 (functional), Def. 5.4 (B_F), Lemma 5.5 (optimal edges = B_F), Claims 5.6-5.7, Lemma 5.10, section 6
  p.22 (parameters r = Theta(log n), s = Theta(sqrt n log n), t = Theta(log n); N = Theta(nrs), M = Theta(nrst)), Theorem 6.3.
- Friedmann-Hansen-Zwick, errata arXiv 1410.7871 v1: abstract, section 1 ("The main result of [1] is thus flawed"; "the lower
  bound for Random-Facet* remains correct"; [5] = Hansen's thesis 2^Omega~(m^{1/3}) for Random-Facet on MDPs; [3] = 1410.7530
  transfers it to shortest paths), section 2 (Random-Facet pseudocode on shortest paths: pick e in F \ B, recurse on F \ {e},
  improve-and-pivot, recurse on F).
- Zwick, arXiv 2607.06334 v1: Appendix D Fig. 1 (Rand-Act-Rem pseudocode: B = actions not in a; r random; b = recurse on H \ r;
  c = b[r]; if (c -> b) in H return b else recurse on (H, c)), section 3 (VAL_sigma, orientation a -> b iff VAL_a prec VAL_b).
- Friedmann, "An exponential lower bound for the latest deterministic strategy iteration algorithms", LMCS 7(3:19) 2011,
  arXiv 1106.0778 (PDF opened 2026-10-15 ~11:50Z). Section 3 pp.4-6: play decomposition v1..vk (w1..wl)^omega, node
  valuation (w1, {v_i > w1 : 1 <= i <= k}, k), set order M < N iff max(M delta N) in (N cap V_even) cup (M cap V_odd),
  valuation order (length: e < f worse when u odd, e > f worse when u even), improving edge, Thm 3.2, Thm 3.3.
  Section 5 p.8: 1-sink games, "the path-length component equals the cardinality of the path component". Section 6.1
  pp.9-10: simple cycle (Table 1: d_i Even p_i, e_i Odd p_i+1, h_i exit), Lemma 6.1 (tau(e_i) = h_i when closed; = d_i when
  open and sigma(d_i) prec h_i), Lemma 6.2 (open cycle closes when sigma(d_i) = max D_i prec h_i; "the player 1 node hides
  the fact that there is a highly profitable node on the other side"). Section 6.4 Table 4 (G_n), 6.5 phases (skimmed).
- Disser-Loho-Maat-Mosis, "Lower bounds for ranking-based pivot rules", arXiv 2512.16684 v2 (PDF opened ~12:25Z): Thm 4.3
  (p.13: l-index-based rules need m^omega(1) on sink parity games), Fig. 4.1 (p.14: G_n, priorities a_i 2i+1, b_i 2i+2,
  b_{n+1} 2n+4, Bland numbers 2i / 2i-1, sigma_0 in bold), Lemma 4.4 (p.13: "Strategy improvement with Bland's rule takes
  2^n - 1 iterations to solve the sink parity game G_n with initial strategy sigma_0"; proof by induction, p.14).
- Fleet files: TARGET.md v1.0 sections 2, 3, 5; docs/NOW.md; claude/l-si 95d37d3: docs/si/candidates/S1.md, S2.md,
  docs/si/RESULTS.md, DEAD.md, README.md, experiments/si/si.py, gens.py, families.py, freeze_test.py, adversarial.py,
  notes/L-SI.md; docs/lit/T12-MSF-barriers.md; experiments/harness/pg.py, verify.py, zielonka.py.

## Dead ends
- None yet for the attack. Not pursued: a non-sink killer (the sink-game gate suffices); porting Disser-Mosis D_n with Odd
  gates (T12 section 4) is unnecessary, the Bland counter plus gates is smaller.
