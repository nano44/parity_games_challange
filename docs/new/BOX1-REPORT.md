# L-NEW box 1 report (2026-10-18, 09:09Z-14:10Z by date -u; Opus 5.5 under D8)

## (i) S5 (Zadeh, index tie-break) and S6 (Cunningham, index order): fast kill test
Details: docs/new/S5S6-renum.md. Verdict: NOT KILLED, not defended. Renumbering hill climbs on 13 bench families (identity
vs best: at most quadratic growth except switchbestexp). switchbestexp: per-N climbs give Cunningham 395, 939, 2935 (N = 2..4,
pinned with sha1s) and Zadeh 274, 540, 983, 1363; but the MECHANICALLY lifted numbering (no climbing) gives Cunningham 3886,
4719, 5626, 6602 at N = 5..8 (polynomial). Successor item: extract a numbering rule from the climbed numberings.

## (ii) Own approaches
| id | approach | status |
| --- | --- | --- |
| N1 | LS24 IncreasingDiscountPI (Loff-Skomra, arXiv 2402.03975 Fig. 12 / 2610.22149 Fig. 7.2) on parity-induced rewards ±n^pr; Odd's best response by Post-Ye's rule | KNOWN ALGORITHM, new input class; not killed; step-2 bench polynomial-looking; (PHASE-POLY) is a DATA hypothesis |
| N2 | priority annealing with warm-started VJ Howard | proposed, parked |
| N3 | exact discount homotopy (Blackwell path) | proposed; follow-up if N1 dies |
| X1 | bit-scaled energy value iteration | dead end by argument (notebook) |

### N1 evidence (every row: regions = Zielonka, both strategies verified; Even switches unless stated)
- 12,000 random games (10,000 with n <= 60, 2,000 with n = 60..400): all agree.
- switchallexp N = 1..13: plain VJ Howard doubles (10 ... 79253); N1 ~2.6 N² (13 ... 442); largest phase 2N + 5.
  Ablation (Howard straight at N1's final discount) = Friedmann's counts exactly (Friedmann 1106.0778 Thm 9.5, Lemma 9.6).
- switchbestexp N = 1..10: plain 21 ... 20461; N1 26 ... 704 (quadratic); largest phase 6N + 6.
- gated_switchallexp N = 2..6: plain 17 ... 38; N1 51, 90, 134, 188, 246 (quadratic; steepest N1 family).
- tc N = 1..12: N1 0 ... 268 (above plain Howard's 31, ~linear in n = 492); fhz_padded N = 2..11: N1 <= 56.
- All other bench families: linear or constant (summary_c.csv / summary_py.csv; plots docs/new/plots/).
- Confounds removed: priority merging (alone kills switchallexp for VJ Howard); the stop rule (certificate-stopped VJ Howard
  still doubles: 14 ... 2490).
- Weak-evidence caveat: Friedmann's families are trivial for Howard from Odd's side (dual: 2..7 iterations), so a two-sided
  baseline also beats them.
- Killer attempts (none killed): spreading, delay chains (4 kinds), bait chains, gap traps, all-vertex traps, calibrated
  traps (inapplicable), per-edge delay search, small-game adversarial searches, lock variants p0/loop/loop2.
  Sketch and lock design problem: docs/new/N1-killer-sketch.md.
- Bit cost: J <= (d + 2) log2 n + O(1) phases, O(nJ + d log n)-bit numbers, Odd's inner loop O(n³m² log² n) by Post-Ye
  (1208.5083 Thm 3.7). Polynomial iff (PHASE-POLY): Howard at γ_j from the γ_{j−1} optimum makes poly(n) switches.
- Literature: no worst-case lower bound for IncreasingDiscountPI in 2402.03975 or 2610.22149; both say (verbatim) "for
  mean-payoff games, or for discount factors γ exponentially close to 1, no upper-bound is known on the number of
  iterations, significantly better than the number of policies".

## Code (experiments/new/)
renum.cpp (S5/S6 adversary), anneal.py / anneal.cpp (N1, cross-checked on 1,000 games), vjcert.cpp (certificate-stopped
baseline), xcheck_c.py, rand_c.py, run_anneal_c.sh, run_renum.sh, transforms (delay, bitdelay, keydelay, bait, gaptrap,
alltrap, caltrap, spread, lock, dual, compress), plot_n1.py, check.sh (run by verify).
