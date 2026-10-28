# Box 16: N5 on Friedmann's H_n (L-COMP successor 6; Lead GO 2026-10-26 19:18Z; D18)
Everything here is DATA. Nothing is PROVED. Not a TARGET.md claim.
Subject: O. Friedmann, "An exponential lower bound for the latest deterministic strategy iteration algorithms", LMCS 7(3:19) 2011,
arXiv 1106.0778 ([F]; pdf sha256 46c96f44775aa2b07cad20912cb325b177e38c94cb2e40297df66b6047679611, the same file L-NEW 29 opened).
The full text was opened. Sections, tables and figures used: §2 (Ω injective), §3-§5, §8.1 (Table 5, Fig. 7, Lemma 8.1), §8.2 (Fig. 8),
§8.3 (Table 6, Fig. 9, Lemma 8.2), §8.4 (Table 7, Fact 8.1, the start ι_{H_n}, Fig. 10, Lemma 8.3), §8.5 (Theorem 8.4). Recorded in
notes/L-COMP.md under "Sources opened".

## 1. The game (hn.py) and its faithfulness
- I built H_n from [F]'s §8.4 Table 7 (21n vertices). I did NOT reuse M1's port. M1's `switchbestexp` is PGSolver's generator, with
  25N + 10 vertices: a different family, not H_n.
- Two readings of the printed text (findings against the paper's text):
  - (a) Priorities collide. As printed, Table 7 is not injective, although §2 assumes injective Ω. Gate n collides with the lane:
    Ω(d2_n) = 8n+3 = Ω(t1), d3_n = t2, e_n = a2, y_n = t3, g_n = a3.
    Figures 8, 9 and 10 put the gate priorities 6 lower: d1_i = 8i−5, d2_i = 8i−3, d3_i = 8i−1, e_i = 8i, y_i = 8i+1, g_i = 8i+2.
    That is Table 6 with p'_i = 8i−5, and it makes Ω injective. **Mode `fig` (the default, used for every result below)** = Table 7
    with these gate priorities. **Mode `table`** = Table 7 verbatim; it is run as a control.
    Figure 10's labels for s, r (30, 32) and for k, f, h are not used: they contradict Table 7 and Fact 8.1 (highest priority 24n + 6).
  - (b) Lane length. The text says "length 6n − 3", but Table 7 indexes a_i, t_i for i ≤ 6n − 2 (= m of §8.1). I used 6n − 2.
- hn.py asserts all of Fact 8.1: 21n nodes, 3.5n² + 40.5n − 4 edges (this count fixes j ≥ 0 in the edge sets), highest priority 24n + 6.
- Check against Theorem 8.4 (iglo.py). This is PGSolver's I^glo policy (switch_globally_best.ml, ported in
  experiments/hard-families/pgsolver_si.py). It is the implementation [F] §8.4 cites for Fig. 11. I ran it as a bare loop from ι_{H_n}.
  Mode `fig`:

  | n | 1 | 2 | 3 | 4 | 5 | 6 |
  | --- | --- | --- | --- | --- | --- | --- |
  | I^glo steps | 11 | 43 | 107 | 235 | 491 | 1003 |
  | 2^n | 2 | 4 | 8 | 16 | 32 | 64 |

  So steps = 16·2^n − 21 exactly (consecutive differences 32·2^(n−1)), which is ≥ 2^n. Lemma 8.3 also holds at every step: Odd wins
  everywhere, and the cycle component is x at every node.
  Mode `table` gives only 43 (n = 3) and 139 (n = 5), so its collisions change the run. **H_n (mode fig) reproduces Theorem 8.4's
  exponential behaviour; I take it as faithful.**

## 2. N5 runs (box16.py; N5 SPEC S1-S5 = n5b; n5 = n5b asserted)
- Starts:
  - **F** = (ι_{H_n}, σ̄(ι)). This is [F]'s Even start. Odd starts at its optimal counterstrategy to ι, which is [F]'s τ_σ (§3, Lemma 3.1);
    READING: the natural N5 analogue of [F]'s start.
  - **Fs3** = (ι, S3's τ). It is the same pair as F on every n (equal start sha1).
  - **S3** = SPEC S3 for both players.
  - **G<k>** = (σ_k, σ̄(σ_k)), where σ_k is the I^glo strategy after k steps from ι (mid-counter starts; k = ¼, ½, ¾ of the I^glo run).
- Checks on every run: the n5.py state sequence (L-NEW, exh.trace with check) = the n5b SPEC state sequence = the state sequence of
  L-SI's common.rows; regions = Oink zlk @ 8fbf0a7; both engines' strategies pass harness/verify.py; census.analyse checks the landed
  statements EP0, ALT (R61 (e)), NEP, XEP, SPLIT, EPOCH, MONO and D-EPOCH.
- **45 runs, all OK, 0 violations.** Full table: results/tables.md. Per-run JSON: results/<run>.json.
  Pinned games (sha1 of instances/H<n>.pg):

  | game | sha1 |
  | --- | --- |
  | H3 | f7bdd38a |
  | H4 | 66afd1d7 |
  | H5 | 700e3b2a |
  | H6 | 6f6bb32c |
  | H7 | 950a5acc |
  | H8 | 36659f25 |
  | H10 | 7d5a5f69 |
  | H12 | e155f78c |
  | H16 | 08541238 |

  The start files are instances/<run>.start; their sha1s are in results/tables.md.

| n | V | F: it | F: phases | F: longest | F: τ ch | F: λ_W ch | F: max N_ep / NCONF / ALT | S3: it | S3: phases | S3: longest | S3: max N_ep / ALT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 63 | 34 | 4 | 25 | 3 | 6 | 5 / 4 / 4 | 22 | 4 | 16 | 3 / 1 |
| 4 | 84 | 41 | 5 | 31 | 4 | 7 | 6 / 5 / 5 | 28 | 5 | 21 | 3 / 1 |
| 5 | 105 | 49 | 6 | 38 | 5 | 8 | 7 / 6 / 6 | 34 | 6 | 26 | 3 / 1 |
| 6 | 126 | 59 | 7 | 47 | 6 | 9 | 9 / 8 / 8 | 40 | 7 | 31 | 3 / 1 |
| 7 | 147 | 66 | 8 | 53 | 7 | 10 | 10 / 9 / 9 | 46 | 8 | 36 | 3 / 1 |
| 8 | 168 | 73 | 9 | 59 | 8 | 11 | 10 / 9 / 9 | 52 | 9 | 41 | 3 / 1 |
| 10 | 210 | 90 | 11 | 74 | 10 | 13 | 13 / 12 / 12 | 64 | 11 | 51 | 3 / 1 |
| 12 | 252 | 107 | 13 | 89 | 12 | 15 | 16 / 14 / 15 | 76 | 13 | 61 | 3 / 1 |
| 16 | 336 | 138 | 17 | 116 | 16 | 19 | 19 / 18 / 18 | 100 | 17 | 81 | 3 / 1 |

Every run has fallbacks f = 0 and λ_Ξ changes = 0 (1-sink games, as [F] §5).

G starts (n = 3..6): 18-56 iterations. The ¼ start has n phases (max ALT n + 1). The ½ and ¾ starts are one phase (τ is already
Odd-optimal), with longest phase 18-41 and ALT ≤ n. Mode `table` (n = 3, 5, 8): the same shape; counts differ from mode fig by at most 3.

### Definitions of the per-phase counters (box16.py header)
- **Phase**: R38 (a), a maximal run of states with (λ_Ξ, τ) constant.
- **len**: in-phase transitions.
- **end**: why the phase ended: tau (τ changed, λ_Ξ did not), lam, both, or final.
- **dW**: in-phase λ_W changes.
- **f**: in-phase fallbacks.
- **N_ep, NCONF, NCONF2**: as computed by nconf.phase_stats (box 14).
- **S**: the fallback-free, λ_W-constant runs of the phase.
- **ALT**: max over S and c of ALT_c(S), exactly as N5-EXIT-box22 §9 states it (not evenside's first-match classes). A transition of S
  counts when σ̄ changes at a gate u ∈ U_c ∩ Q_c ∩ (D_k ∪ D_{k+1}), AND either D ∩ U_c changes or a D-direct offset changes at a gate
  whose σ̄ changes. D, U_c, D-direct and the offsets come from L-SI's gcx.state_info / gcx.offs (read-only import).
- **SBG**: phase transitions with a σ̄ change at a gate (an upper count for ALT).

### Phase shape: the same on every n (per-phase lists in results/tables.md)
- **F**:
  - Phase 0: 6 transitions, then a τ change.
  - Phases 1 .. n−1: EMPTY phases (0 in-phase transitions). Each is ended by one τ change, at one gate, e_i : d1_i → h_i.
    Odd leaves the stubborn cycles one gate per iteration, top gate first.
  - Final phase: τ fixed with τ(e_i) = h_i for all i. Length 7.06n + 3.4, N_ep ≈ n + 3, ALT = SBG ≈ n + 2 (σ̄ at e_i flips about once per
    gate). The rest of it is the deceleration lane walking down one t_i per iteration (t_{i+1} → t_i for i up to 6n − 3).
- **S3**:
  - n τ changes in n short phases (phase 0: 3 transitions; then empty phases).
  - Final phase: 5n + 1 transitions, N_ep = 1, ALT = 0. It is a pure Even optimisation against a fixed τ that has no D.

## 3. Growth fits (table.py; least squares over n = 3..16)

| start | iterations | longest phase |
| --- | --- | --- |
| S3 | **6n + 4** (exact, residual 0) | **5n + 1** (exact) |
| F / Fs3 | 8.06n + 9.4 (max residual 1.2) | 7.06n + 3.4 (max residual 1.2) |

The per-step ratio of the last two n is 1.07, falling with n; that is linear growth, not a base > 1.

**Answer to the key question (DATA, n ≤ 16, 3 + G starts):**
- N5 does NOT take exponentially many iterations on H_n. Iterations are linear in n, and so is the longest phase: about 7n, i.e. 0.40 V at n = 3 falling to 0.35 V at n = 16.
- The [F] counter never runs. Its counting is Even's busy updating while Odd's best response at e_i opens and closes the stubborn cycles.
  N5's S4b instead moves τ(e_i) to h_i at every gate, one gate per iteration, in the first n iterations. After that each cycle closing is
  W-invisible to Even, which is L-NEW 29's §2 (c) dichotomy, now observed.
- The last phase is linear: the lane walk plus about one σ̄ flip per gate (ALT ≈ n + 2).
- So on this family the exponential mechanism is neither inside one phase nor spread over many: it does not happen.
- READING (not tested beyond H_n): [F]'s construction needs Odd to keep playing its best response at every gate. N5's τ is a strategy
  that also improves, and it shuts the gates. Whether some H_n variant forces τ to stay or return (repeated τ flips at a gate) is open;
  such a variant would be an L-RED / L-NEW design target.

## 4. Robustness: random and mid-counter starts (randstarts2.py; Lead 2026-10-28 21:05Z)
- **Runs.** Per game:
  - the S3 start and the F start;
  - R seeded uniform random start pairs: R = 200 for n 3..8, R = 100 for n 10 and 12;
  - G<k> starts: (σ_k, σ̄(σ_k)) for every GSTEP-th I^glo step k from ι (n 3..8, about 32 per n). These cover the whole exponential
    I^glo run; the I^glo run lengths are 107, 235, 491, 1003, 2027, 4075 = 16·2^n − 21 for n 3..8.
- **Checks on every run.** Regions = Oink zlk, and verify.py on n5b's strategies. At every state, σ̄ from L-SI's Engine equals the
  SPEC σ̄ (an engine cross-check).
- **Counters, per phase (R38 (a)), maximised over the run:**
  - XR = max over v of the number of Ξ(v) changes in one phase (the Lead's XR); XRQ = the same over Q;
  - ALT = max over S and c of ALT_c(S), same counter as box16.py;
  - TF = max τ changes at one Q vertex over the run. In H_n, Q = {e_i}, so TF is the gate-flip count. TFG is the same on gate labels;
    it was added later, so it shows "-" in logs written before it existed.
- Logs: results/rs2_<n>.log (one line per run, END lines with the worst value of each counter per start family).
  Table: results/rs2_table.md (rs2table.py).
- **1,612 runs on H_n, 0 FAIL.** Worst over all start families:

| n | runs | max it | max phases | max longest phase | max XR | max ALT | max TF (gate flips) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 237 | 43 (G30) | 6 | 26 | 16 | 6 | 2 |
| 4 | 235 | 53 (G91) | 9 | 35 | 17 | 8 | 2 |
| 5 | 234 | 70 (G90) | 13 | 43 | 24 | 10 | 2 |
| 6 | 234 | 79 (G217) | 12 | 50 | 24 | 10 | 2 |
| 7 | 234 | 75 (G126) | 12 | 56 | 14 | 10 | 2 |
| 8 | 234 | 81 (G1778) | 17 | 61 | 14 | 11 | 2 |
| 10 | 102 | 92 (rand94) | 19 | 74 | 15 | 13 | 2 |
| 12 | 102 | 117 (rand31) | 19 | 90 | 16 | 15 | 2 |

- **READING (DATA).** No start found an exponential run.
  - The worst iteration count is 1.02 to 1.43 times the F-start count at the same n, with no growth beyond linear (n 3..12).
  - The longest phase is ≤ 9n (8.7n at n 3, 7.5n at n 12). XR ≤ 24 overall (at most 0.25 V, at n 3). ALT ≤ 2n.
  - Fallbacks: 0 in every run.
  - Gate flips: τ changes at most twice at any gate e_i (h → d1 → h, for example rand99 at n 3: a start with τ(e1) = h1 whose σ makes
    d1_1 better first). So τ re-flips at a gate occur, but at most once more, and never repeatedly.
  - Mid-counter starts (G) taken anywhere along the 16·2^n − 21 steps of I^glo also finish in ≤ 81 iterations: N5 does not resume
    [F]'s count from any counter state.

## 5. Variants in which Odd's τ cannot shut a gate permanently (hn_var.py; Lead 2026-10-28 21:05Z item 5). DATA probes.
- **dual** = dual(H_n): owners swapped, priorities + 1.
  - Odd is now [F]'s counting player (lane, stubborn cycles, access nodes), and the gates e_i are Even's.
  - Oink: Even wins every vertex (the mirror of H_n).
  - S3 / F (F = (S3's σ, ι as τ)) / 100 random starts per n, for n 3, 4, 5, 6, 8.
- **ex** = H_n with Odd's exit from e_i routed through a new Even node u_i: e_i → {d1_i, u_i}, u_i → {h_i, d2_i}, Ω(u_i) = 8i − 4.
  - Even can send the exit back into the stubborn cycle, so the exit is never safe for Odd on its own.
  - Oink: Even wins all but 3 vertices, for every n run (the game is no longer 1-sink and is not a lower-bound construction).
  - S3 / F / 100 random starts per n for n 3..8, 50 for n 10, 50 for n 12, 20 for n 16.
- Logs: results/rs2_<n>dual.log and rs2_<n>ex.log; table: results/rs2_table.md. **0 FAIL** (Oink zlk regions, verify.py, engine
  cross-check).

| variant | n | S3 it | F it | max it (all starts) | F phases | max phases | max longest | max XR | max ALT | max TFG (gate flips) | max TF (one Q vertex) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dual | 3 | 22 | 34 | 37 | 35 | 38 | 0 | 0 | 0 | 2 | 14 |
| dual | 4 | 28 | 41 | 43 | 42 | 44 | 0 | 0 | 0 | 2 | 14 |
| dual | 5 | 34 | 49 | 52 | 50 | 53 | 0 | 0 | 0 | 2 | 14 |
| dual | 6 | 40 | 59 | 62 | 60 | 63 | 0 | 0 | 0 | 2 | 14 |
| dual | 8 | 52 | 73 | 77 | 74 | 78 | 1 | 1 | 0 | 2 | 18 |
| ex | 3 | 22 | 28 | 31 | 12 | 14 | 18 | 18 | 12 | 1 | 1 |
| ex | 4 | 28 | 34 | 37 | 15 | 18 | 22 | 22 | 15 | 1 | 1 |
| ex | 5 | 34 | 40 | 43 | 18 | 19 | 30 | 30 | 20 | 1 | 1 |
| ex | 6 | 40 | 46 | 47 | 21 | 23 | 36 | 35 | 28 | 1 | 1 |
| ex | 7 | 46 | 52 | 52 | 24 | 24 | 40 | 40 | 35 | 1 | 1 |
| ex | 8 | 52 | 58 | 58 | 27 | 27 | 47 | 47 | 37 | 1 | 1 |
| ex | 10 | 64 | 70 | 70 | 33 | 33 | 59 | 59 | 52 | 1 | 1 |
| ex | 12 | 76 | 82 | 82 | 39 | 39 | 72 | 72 | 50 | 1 | 1 |
| ex | 16 | 100 | 106 | 106 | 51 | 51 | 95 | 95 | 82 | 1 | 1 |
- **READING (DATA).**
  - **dual.** N5 is symmetric here: every iteration count equals H_n's (S3 6n + 4, F identical).
    - Every iteration is its own phase, because the counting player is Odd and τ changes at every step. So the phase count = it + 1:
      linear, all phases of length ≤ 1 (one phase of length 1, at n 8), ALT 0.
    - Gate flips (σ at e_i): at most 2.
    - τ re-flips at a single Odd vertex DO repeat: up to 14 times (18 at n 8, e.g. d1_2 and d1_3 in rand75). These are the counting
      player's stubborn-cycle nodes, mirroring H_n's Even busy-updating. The count does not grow exponentially, and the total is ≤ it.
  - **ex.** Odd changes τ at a gate at most once (TFG ≤ 1; 0 from S3 and F): Odd mostly keeps d1_i and Even closes the cycles.
    - The phase count grows linearly: F-start phases = 3n + 3.
    - Iterations are linear: S3 6n + 4, the same as H_n; F 6n + 10.
    - The longest phase and XR grow linearly (about 6n from random starts); ALT up to 5.2n, larger than in H_n.
  - **No exponential growth in either variant, n ≤ 16.** Neither variant makes τ flips repeat at a gate (TFG ≤ 2). In dual, repeated τ
    flips appear at the counting player's own nodes, but they are linear in total.
  - The question of an Odd gate that MUST re-open many times stays open. Both variants let one side settle the gates early. A design
    in which Odd's gate preference is forced to alternate with a counter state needs Odd's own improvement (S4b, an optimum within A_τ
    against σ) to be a counter. That is an L-RED / L-NEW design target, not run here.

## 5. Commands
```
python3 hn.py N [--mode fig|table] --out H.pg [--start H.start]     # the game; ι_{H_n} as SIGMA0
python3 iglo.py N [--mode fig|table]                                # I^glo from ι (Theorem 8.4 check)
P=4 ./run.sh                                                        # box16.py over jobs.txt -> results/box16.log, results/*.json
python3 table.py > results/tables.md
P=4 ./rs2.sh; python3 rs2table.py > results/rs2_table.md             # §4 (rs2_jobs.txt); P=4 JOBS=var_jobs.txt ./rs2.sh for §5
# randstarts.py / rs.sh: the first §4 attempt (no XR/ALT), superseded by randstarts2.py; its partial logs were not kept
bash check.sh                                                       # fast self-check (verify.sh)
```
Oink: scripts/setup_oink.sh (8fbf0a7). Engines: experiments/n5-second/n5b.py (L-COMP), n5.py via experiments/n5-exhaustive/exh.py
(L-NEW), experiments/si/root/common.py + gcx.py (L-SI). The other lanes' code is imported read-only and not edited.
