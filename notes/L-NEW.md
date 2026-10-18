# L-NEW notebook ((c) design lane under D14; Lead reading L35)
Overwrite the top sections; append to "Sources opened" and "Dead ends". Box 1 started 2026-10-18 09:10Z (date -u).

## Resume point
HANDOVER (2026-10-18 ~12:10Z, context ~500k; box 1 from 09:09Z). Successor: read this, then docs/new/BOX1-REPORT.md,
docs/new/N1-disc-anneal.md, docs/new/N1-killer-sketch.md, docs/new/S5S6-renum.md.
- N1 = "LS24 IncreasingDiscountPI on parity-induced rewards" (credit Loff-Skomra, arXiv 2402.03975 Fig. 12 / 2610.22149
  Fig. 7.2). Not killed. 12,000 random games agree with Zielonka (strategies verified). Bench polynomial-looking on every
  family (switchallexp ~2.6N², switchbestexp quadratic, gated_switchallexp quadratic, tc ~linear in n). (PHASE-POLY) is a
  DATA hypothesis. Evidence weak: Friedmann's families are trivial for Howard from Odd's side (dual). No worst-case lower
  bound in the literature (verbatim "open" sentence under Sources opened).
- Killer attempts all failed (list in N1-killer-sketch.md); the lock is an open design problem (path set vs max).
- S5/S6: not killed on 13 families. Steepest: switchbestexp (Cunningham 341, 928, 1887 at N = 2..4; Zadeh 268 ... 1363 at
  N = 2..5, ratios falling). Lifted chains (s6_chain.sh) were running at handover; results in
  experiments/new/out/s6/switchbestexp_{cunningham,zadeh}_N*.txt (out/ is gitignored; rerun to reproduce).
- C++ N1 sweep (run_anneal_c.sh -> out/anneal/summary_c.csv) still running at handover (switchbestexp N >= 12, then the
  other families). docs/new/plots/ shows the Python sweep (summary_py.csv, N <= 8).
- Build: cd experiments/new; g++ -O2 -std=c++17 -o anneal_c anneal.cpp; -o renum2 renum.cpp; -o vjfast vjfast_copy.cpp;
  -o vjcert vjcert.cpp. Instances (out/inst, gitignored): si/gens.py {randomfacetsubexp,zadehexp,dlmm_bland,dlmm_ML,
  cunninghamexp} N = 2..14; hard-families/pgsolver_port.py {recursiveladder,switchallexp,switchbestexp} N = 1..14;
  red/gens_red.py {gated_bland,fhz_padded}; si/gated.py {zadehexp,switchallexp,switchbestexp} -> gated_*;
  tools/oink/build {tc,tc+,counter_*} N = 1..14.

## Queue
0. (Lead 12:14Z, first for the successor) S6 on switchbestexp: extract a numbering RULE from the climbed numberings
   (instances/s6/*.perm; what the climb does to Friedmann's bit/lane structure, labels via pgsolver_port), generate
   N = 2..8 from the rule alone, run vjfast cunningham. That decides. Alternative: apply lift.py MECHANICALLY (no climbing)
   from the N = 4 numbering to N = 5..8 and run vjfast (lift-only starts so far 688, 1346, 3886). No Lead re-run before a
   rule-generated family exists.
1. Record the S6/S5 switchbestexp chain results (N = 4, 5) in docs/new/S5S6-renum.md; decide polynomial vs doubling
   (Cunningham N = 5: polynomial ~3,300, doubling >= 3,800). If doubling persists to N = 6, extract a numbering scheme
   (lift.py chain) and pin instances with sha1 before calling a kill.
2. N1: finish the C++ sweep (tc+, counter_m/rr/rob, gated_switchbestexp, larger N); regenerate plots from summary_c.csv.
3. N1 killer: a both-sides-hard family / a lock with coupled per-bit audits (sketch); Lead routes to L-RED.
4. N3 (exact discount homotopy) only if N1 dies; N2 parked.

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
  Used instead, as restated in 2610.22149: Prop. 7.11 = [ZP96, Thm 5.2] ‖λ(γ) − λ‖∞ ≤ 2n(1 − γ)‖r‖∞ (normalised values).
- arXiv 1106.0778 (Friedmann, LMCS 7(3:19)), opened 10:30Z, §9: reward r_Ω(v) = (−|V|)^Ω(v); β_G := 1 − 1/(4·|V|·max|r(v)|);
  Thm 9.2 (Puri), Thm 9.5 (Vöge: every parity improving switch is a discounted improving switch), Lemma 9.6 (1-sink games:
  Odd's discounted best response reaches the sink), so the lower bound transfers to discounted payoff games.
- arXiv 2610.22149 v1 (Loff-Skomra, "Smoothed analysis of policy iteration and value iteration for deterministic discounted
  and mean-payoff games played on any graph", 15 Oct 2026), opened 10:35Z. §7.4, Figure 7.2 IncreasingDiscountPI:
  "γ ← (1 + γ)/2; (σ, τ) ← DiscountedPI(σ, τ, γ) until (σ, τ) are optimal in the mean payoff game" = N1. Thm 7.9 (1 − γ <
  1/(4n²Δ(r)) => unique optimal pair), Thm 7.14 (O(m² + m²n⁴Δ(r)² log³(nΔ⁺)) Howard switches), Thm 1.2 (smoothed poly), §9
  open problems. Cites [LS24] = Loff-Skomra, ICALP 2024, LIPIcs 147:1-147:16 (NOT opened).
- arXiv 2402.03975 v1 (Loff-Skomra, "Smoothed analysis of deterministic discounted and mean-payoff games", 6 Feb 2024 =
  [LS24], ICALP 2024 version restricted to ergodic graphs per its HAL listing), opened 11:45Z. Thm 1.10: "The greedy-all
  switches policy iteration rule combined with increasing discount factor solves random instances of deterministic discounted
  or mean-payoff games in polynomial smoothed complexity." Thm 6.6 (Figure 12, IncreasingDiscountPI: halts on every input,
  smoothed polynomial). WORST CASE, verbatim (p. 5, l. 199-201 of the text dump): "Otherwise, for mean-payoff games, or for
  discount factors γ exponentially close to 1, no upper-bound is known on the number of iterations, significantly better
  than the number of policies, which is exponential in √ the number n of states." (same sentence in 2610.22149 §1.2).
  Example 3.5 / §3.2: a deterministic two-player game whose value, as ONE payoff varies in [−1, 1], has 2^Ω(n) break points
  (from [BNRC08] / [ABGJ18]); this is a parametric-PAYOFF statement, not a lower bound for IncreasingDiscountPI. No
  worst-case lower bound for IncreasingDiscountPI is stated in either paper (searched: worst, exponential, lower bound, open).
- arXiv 1208.5083 v2 (Post-Ye), opened 10:38Z: Thm 3.7, the highest-gain simplex rule takes O(n³m²log²n) iterations on
  deterministic MDPs with uniform discount, any discount (Thm 4.8: O(n⁵m³log²n) for distinct discounts).
- Search (WebSearch, 10:30Z) also listed: Madani-Thorup-Zwick, ACM TALG 6(2) 2010, O(mn) for deterministic discounted MDPs
  (abstract page only, NOT opened); Karczmarz arXiv 2110.15070 (NOT opened).

## Dead ends
- X1 SCALE-VI (2026-10-18, screened out by argument before code; Lead 10:00Z: record as dead end by argument). Bit-scaled
  energy value iteration: phase k solves the energy game with weights ceil(w / 2^k), warm-started from 2 f_{k+1} (valid
  lower bound since ceil-weights at k+1 doubled dominate weights at k). Obstruction: vertices whose winner flips to Odd in
  phase k must be lifted to the top value, about n·W_k lifts, and nothing bounds the flips per phase. That is small-progress-
  measure behaviour (pseudo-polynomial per phase). Instance: none run. Any game where a low priority decides an Odd win
  late (a single Odd self-loop of priority 1 reached through high even priorities) forces the climb in the last phase.

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
- N1 counts on switchallexp are insensitive to every delay/trap transform tried (key-edge delays up to 100(i+1): EXACTLY
  25, 42, 64, 90); the largest phase is always the final one (2N + 5). Friedmann's games: Odd wins every vertex.
- In 1-sink games the region certificate needs Odd's discounted best response to be globally winning; certificate-stopped
  VJ Howard reaches that after 2^(N-1) + O(1) iterations (vjcert --certstop); N1 after ~2.6 N².
- The dual transform (owners swapped, priorities +1: dual.py) makes Friedmann's families trivial for Howard (N + O(1)).
- renum's best numberings have no readable class structure (as L-RED R7 found); lift.py transfers numbering by labels and
  keeps most of the count (Cunningham switchbestexp N = 2 -> 3: lifted start 688 vs best 939).
- Big-d random games (n ~ 350, d ~ 350) take minutes in anneal_c: ~3,000 phases of ~1M-bit numbers.
