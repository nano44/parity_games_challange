# Box 24: the true maximum W-run length |F| of plain N5 at small n (L-COMP successor 8)
Lead 2026-10-30 21:21Z (D18), "a measurement beats an inference": the true maximum W-run length |F| as a function of n, over the
smallest classes that can be made exhaustive. Report max |F| and max |F|/n, say whether any small game has |F| > n − 1, and pin the
extremal witnesses. Work 2026-10-30 21:45Z to 2026-10-31 00:1xZ (date -u). Every number is DATA unless labelled. Not a TARGET.md claim;
G-N5-TIME open.
Why n − 1 is the reference: by box 85's FREE-RED, |F| ≤ (n − 1)(R*_F + 1) + FL_F. So a W-run with R*_F = FL_F = 0 has |F| ≤ n − 1,
and |F| > n − 1 needs R*_F ≥ 1 or FL_F ≥ 1. (From R88 / R89 GP*-RUN, landed.)

## Definitions and tools (all from box 23, experiments/n5-box23/)
- W-run, R*_F, FL_F as in box 23 README (RESULTS R88 / R89). |F| := the transitions of the W-run F. Counter rstar.py on n5b SPEC
  (= L-NEW's xirise.py on 1,132 / 1,132 corpus games, box 23 (a)).
- exh23.py: every game of model C(n) (box 17: ids in rank order, distinct minimal priorities per parity pattern, owners free, every
  nonempty successor set), every start pair (σ0, τ0). It enumerates every maximal W-run chain from a head; every trajectory's W-run is a suffix
  of one, so the max over all starts = the max over chains.
- climbs24.sh: n5-box23/climb23.py --fit F (fitness = (longest |F|, its R*_F, its FL_F); start pair mutated too), 600 s or 900 s per run.
- pin23.py (box 23): n5.py = n5b state by state, Oink zlk regions, verify.py, L-RED xeng.py state by state, rstar = xirise.

## Result
| n | class | games | start pairs (states) | W-run chains | max |F| | n − 1 | max |F| / n | chains at the max | |F| > n − 1? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | C(2) EXHAUSTIVE | 144 | 256 | 6 | 1 | 1 | 0.50 | 6 | no |
| 3 | C(3) EXHAUSTIVE | 21,952 | 110,592 | 6,242 | 2 | 2 | 0.67 | 40 | no |
| 4 | C(4) EXHAUSTIVE | 12,960,000 | 268,435,456 | 13,131,476 | 3 | 3 | 0.75 | 480 | no |
| 5 | random C(5), seed 23, all starts | 20,000 | 4,866,523 | 110,270 | 3 | 4 | 0.60 | 37 | no |
| 5 | random C(5), seed 24, all starts | 200,000 | 48,695,594 | 1,073,314 | 3 | 4 | 0.60 | 422 | no |
| 6 | random C(6), seed 23, ≤ 4,096 starts, all starts | 20,000 | 19,320,173 | 274,550 | 4 | 5 | 0.67 | 2 | no |

- Histograms of |F| over chains (exhaustive): C(3) {1: 6,202, 2: 40}; C(4) {1: 12,837,836, 2: 293,160, 3: 480}.
- C(5) is NOT exhaustive: |C(5)| ≈ 2.9·10^10 games (≈ 3·10^12 start pairs); even out-degree ≤ 2 leaves 7.8·10^8 games. At ≈ 0.2 ms per
  state on 4 cores that is out of reach. C(5) is covered by the random sample above and by climbs.

### Climbs on |F| (lower bounds on the true max; free start pair)
| n | seeds × budget | best |F| per seed | max |F| | n − 1 | R*_F, FL_F of the best | witness |
| --- | --- | --- | --- | --- | --- | --- |
| 5 | 5 × 600 s (≈ 2.1M steps) | 4, 4, 4, 4, 4 | 4 | 4 | 1, 0 | F4_n5 |
| 6 | 5 × 600 s | 5, 4, 5, 5, 5 | 5 | 5 | 2, 0 | F5_n6 |
| 7 | 5 × 600 s | 6, 5, 6, 6, 6 | 6 | 6 | 4, 1 | F6_n7 |
| 8 | 1 × 600 s + 2 × 900 s | 8, 7, 7 | 8 | 7 | 4, 0 | F8_n8 |
| 9 | 1 × 600 s + 2 × 900 s | 7, 10, 9 | 10 | 8 | 1, 0 | F10_n9 |
| 10 | 1 × 600 s | 10 | 10 | 9 | 6, 0 | (climbs/F_n10_r1) |
| 11 | 1 × 600 s | 13 | 13 | 10 | 9, 0 | F13_n11 |
| 12 | 1 × 600 s | 8 | 8 | 11 | 7, 3 | (budget-limited) |
- Box 23's |F| climbs (900-1,800 s): 10, 20, 24, 34, 39, 44 at n 10, 15, 20, 30, 40, 60. Its latew family: |F| = K(m + 3) = Θ(n²)
  (L-RED R138 / box 23 (d)).

## Findings
1. DATA (exhaustive): max |F| = n − 1 exactly for n = 2, 3, 4 over every game of C(n) and every start pair. No W-run longer than n − 1
   exists there. The bound is tight at every n ≤ 4 (480 chains at n 4).
2. DATA (search, not exhaustive): at n = 5, 6, 7 the max found is n − 1 (5 independent climbs each, about 2M steps at n 5; random
   samples stay below). The least n where a W-run longer than n − 1 was found is n = 8: F8_n8, |F| 8, with R*_F 4 and FL_F 0. So the
   least such n is in [5, 8]. n ≤ 4 is ruled out exhaustively; 5-7 only by search.
3. CONJECTURE (data only, n ≤ 7): max |F| = n − 1 for n ≤ 7. Note that 220,000 random C(5) games never reach even n − 1 = 4 (max 3);
   only the climbs do. Uniform sampling misses the extremes at n 5.
4. DATA: max |F| / n found: 0.75 (n ≤ 4, exhaustive); 1.0 at n 8 and 10; 1.18 at n 11 (F13_n11); 1.33 at n 15 (box 23). The
   constructions are quadratic (latew).
5. Mechanism at the extremes (READING from the traces):
   - C4_F3 is a one-player Even game (sha1 e2c137fd…): σ climbs one vertex per transition, 1 → 0, 2 → 1, 3 → 2. This is the GP* climb
     of R88: an improvement wave travels down a path, one vertex per step, n − 1 steps, with no blocked edge (R*_F = 0).
   - F4_n5 (n 5, one Odd vertex): vertex 0 switches twice (2 → 1, then 1 → 3), and one adoption (3 → 4) was BLOCKED at state 0
     (R*_F 1). The single late adoption lets the wave continue after vertex 3's switch, but the total is still n − 1.
   - F8_n8 (n 8): every transition switches one or two vertices. Four vertices switch twice (3: 6 → 4 → 6, 0: 5 → 3 → 2, 2: 1 → 7 → 1,
     6: 1 → 3 → 0), and 4 of the 8 transitions adopt an edge blocked earlier. Each re-switch is fed by a late adoption: this is the
     latew mechanism (R138 / R128: re-adoption of a re-blocked edge, once per wave) in its smallest form. Only 1 of 3 climbs at n 8 found it.
   - F10_n9 (n 9, two Odd sinks): |F| 10 > n − 1 = 8 with R*_F = 1. The single late adoption (3 → 8 at transition 3, BLOCKED since state 0)
     splits the W-run into two GP* climbs of 4 and 6 transitions (vertex 6 switches 1 → 0 → 1 → 0). Each climb stays within n − 1,
     and the sum exceeds it, exactly the (n − 1)(R*_F + 1) shape of FW-R*.

## Pinned witnesses (pin23.py ALL OK on every one: n5 = n5b, Oink zlk, verify, xeng, rstar = xirise)
| name | sha1 | n | iterations | |F| | R*_F | FL_F | from |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C4_F3 | e2c137fd4765… | 4 | 3 | 3 | 0 | 0 | exhaustive C(4) |
| R6_F4 | 3e2e718c3925… | 6 | 5 | 4 | 1 | 0 | random C(6) |
| F4_n5 | b0215e76e548… | 5 | 4 | 4 | 1 | 0 | climb |
| F5_n6 | 4c1f8b3b51cd… | 6 | 5 | 5 | 2 | 0 | climb |
| F6_n7 | 467bd866999b… | 7 | 7 | 6 | 4 | 1 | climb |
| F8_n8 | 69af462bf78c… | 8 | 8 | 8 | 4 | 0 | climb (least n with |F| > n − 1 found) |
| F10_n9 | ddd4d99b5a50… | 9 | 10 | 10 | 1 | 0 | climb (|F| > n − 1 with ONE late adoption) |
| F13_n11 | 737563877254… | 11 | 14 | 13 | 9 | 0 | climb |

## Files
climbs24.sh, check.sh (in verify), instances/ (pins), climbs/ (every climb's best .pg/.start), results/ (R5 sample JSON,
climbs_end.txt). The exhaustive C(2)-C(4) and R5 / R6 (seed 23) JSONs are box 23's (experiments/n5-box23/results/).
