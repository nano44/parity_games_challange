# L-NEW notebook ((c) design lane under D14; Lead reading L35)
Overwrite the top sections; append to "Sources opened" and "Dead ends". Box 1 started 2026-10-18 09:10Z (date -u).

## Resume point
- 2026-10-18 ~09:55Z: (i) renumbering sweep running (experiments/new/run_renum.sh -> out/renum/summary.csv); no kill so far.
  (ii) N1 DISC-ANNEAL implemented (experiments/new/anneal.py), N2/N3 proposed. N1 bench sweep (--nocompress) running
  (run_anneal.sh -> out/anneal/summary.csv). Confound (merging) found and removed; ablation shows annealing is what helps on
  switchallexp. Next: finish sweeps, 10,000 random games, adversarial search, a reveal-time-equalising killer.
- Instance generation (out/inst, gitignored): for N in 2..8: si/gens.py {randomfacetsubexp,zadehexp,dlmm_bland,dlmm_ML,
  cunninghamexp}; hard-families/pgsolver_port.py {recursiveladder,switchallexp,switchbestexp} (also N = 1, 9..12);
  red/gens_red.py {gated_bland,fhz_padded}; si/gated.py {zadehexp,switchallexp,switchbestexp} -> gated_*; Oink build
  generators {tc,tc+,counter_*} N = 1..8.

## Queue
1. (i) S5 (zadeh, index tie-break) and S6 (cunningham, index order): hard bench, gated_*, fhz_padded, randomfacetsubexp, M_L,
   zadehexp, cunninghamexp; renumbering hill climb on the iteration count.
2. (ii) up to three own approaches in docs/new/<name>.md (pseudocode, novelty, barrier draft, cheapest killer) before code.
3. Implement the most promising; Zielonka agreement and strategy check first; then hard bench and its killer.

## Sources opened
- arXiv 1008.0530 v1 (Hansen-Miltersen-Zwick, "Strategy iteration is strongly polynomial for 2-player turn-based
  stochastic games with a constant discount factor"), opened 2026-10-18 09:2xZ (pdf, 13 pp). Thm 6.5: Strategy-Iteration
  from any start terminates within (m+1)(1 + log_{1/γ}(n²/(1−γ))) = O(m/(1−γ) · log(n²/(1−γ))) iterations (the n² is
  n²/(1-γ) inside the log). Proof via Lemma 6.4 (every L̄ iterations a new action is never used again). §7: SI is
  "exponential for non-discounted 2TBSG, or when the discount factor is part of the input" (citing Friedmann).
- arXiv 0909.5653 v1 (Fearnley-Jurdziński-Savani, Lemke / Cottle-Dantzig for discounted games), opened 2026-10-18.
  Lemke as a homotopy in the covering parameter z at fixed discount (text near l.250: "how much further z can be decreased
  before σi ceases to be optimal"); Thm 18: Lemke 2^(n+1) - 2 iterations on G_n; Thm 19 Cottle-Dantzig; p. near l.557:
  "standard reductions [16, 21, 13] convert this parity game into average-reward ... discount factor ... very close to 1".
- NOT yet opened (needed for N1's termination bound only): Zwick-Paterson TCS 158 (1996) discount threshold; Puri thesis.

## Dead ends
(none yet)

## Things only I know
- N1 stop test: "sigma has no VJ improving switch" is WRONG as a stop test (a region-correct sigma need not be VJ-optimal;
  tc 4 stalled at j = 102 forever). The certificate (sign of values + harness/verify.py on both restricted strategies) is right.
- Merging equal-parity neighbouring priorities alone kills Friedmann's switchallexp for plain VJ switch-all (10, 7, 9, 11, 13 for
  N = 2..6): the counter depends on strict priority order; merged ties are ranked by index. Any test of an SI-type method must
  say whether it merges. Adversary can block merging by dummies.
- N1 on switchallexp is invariant under priority spreading p -> K p (K = 3, 9: identical even/odd iteration counts; phases
  scale by K). Reveal order of decisions, not their absolute horizon, determines the run.
- N1 ablation (straight at the final gamma) = Friedmann's counts exactly, matching 1106.0778 Thm 9.5 / Lemma 9.6.
- The exact integer-scaled evaluation (Q = b^n * prod over cycles (b^L - a^L)) is only ~25% faster than Fractions; the cost is
  the number of phases (~(d+3) log2 n without merging) times big-number comparisons.
- Index dependence in L-SI's engine: the vertex numbering enters (a) the injective priority rank (ties of equal priority by
  index), (b) the best-reward start (ties), (c) the zadeh tie-break / the cunningham cyclic order. A renumbering changes all three.
