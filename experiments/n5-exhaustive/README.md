# N5 exhaustive small-game searches (L-COMP box 3, 2026-10-24)
Lead brief 13:08Z (box 3) with addenda 13:20Z (theta-changes, D18), 13:42Z (T28 (b), SEG-1O), 14:00Z (ELIM window, E per stretch),
14:10Z (ELIM = noelimrun_both, thetaelim). All quantities are DATA; "CONJECTURE (exhaustive to n <= k)" means only what the table says.

## Tools
| file | what |
| --- | --- |
| `exh.py` | exhaustive enumeration of C^1O games (exactly one Odd vertex o with out-degree > 1) in a stated canonical subset, N5 from the canonical start or from every start pair; per-game measures (below); JSON per table in out/ (gitignored; copies in results/) |
| `rnd.py` | random o-cyclic C^1O games (box25 `rand_c1o`), canonical start + one random start pair, or every start pair (`--all-starts`) |
| `analyse()` in exh.py | the measures, validated against L-RED `retcheck.py` (re-entry classes), box21 `phases.py` (phase lengths), L-SI `elim.py` / `thetaelim.py` (ELIM windows, theta in windows) on returns_rt48, returns_ph64, theta_thf16, fts_best16 (`validate.py`) |
| `check_instance.py` | per reported instance: n5x.trace(check=True) (= n5.run counts), n5b.py SPEC full state sequence equal, regions = Oink zlk @ 8fbf0a7, verify.py; saves instances/NAME.pg (+ .start) |
| `shrink.py` | greedy shrink (delete vertex / edge, lower priority) keeping a theta-driven re-entry (from a start pair, or from the canonical start with `--prop canonA`) |

Canonical subset of exh.py: distinct priorities with vertex ids in increasing priority order (minimal values for the parity
pattern). L-SI's Engine ranks by (priority, id), so every C^1O game is Engine-equivalent to one game of this form up to relabelling;
relabelled copies can differ only through N5's id tie-breaks. Self-loops allowed. Options restrict further (stated per table).

## Measures (per run; maxima over runs in the tables)
- maxph: longest joint lambda-phase in iterations (phases.py convention).
- thch: max theta-changes (theta = Xi_sigma(o)) inside one joint lambda-phase ((CYC)).
- trust: max trust events per (tau, joint-lambda)-phase (box25 trustcount.count).
- re-entries into R inside every phase, retcheck classes: A = theta at re-entry > w at the last leave ("theta-driven"), B = route
  improvement; raw leave / entry counts. (L-NEW's reentry.py classifier was not on claude/l-new during this box.)
- SEG-1O: longest run of transitions inside a joint lambda-phase without a theta change, minus (n - 1).
- (b) trust-route growth (T28): for z in the box25 trust set T_k that stays in R inside one (tau(o), joint-lambda)-phase, is its
  route length to o + 1 at the next state?
- ELIM window (L-SI (ELIM-n)): elim.py noelimrun_both (sigma edge or Odd best-reply edge abandoned for good in the phase), minus
  (n - 1); also sigma-only and sigma-or-tau variants; thetaelim (theta-changes inside a non-eliminating window).
- E (L-LIT (H-E)): per fallback-free (theta, w, tau, lambda)-stretch, changes of admitted status of R-entering Even arcs; reported
  with the longest stretch and the excess of stretch length over (E + 1)(n - 1).

## Results
(see below; filled at the end of the box)
