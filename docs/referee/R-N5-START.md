# R-N5-START: REFEREE audit: do the landed 𝒞^1O results used by the iteration bound hold for N5 runs from ANY start pair?
Referee audit (REFEREE successor 11, session_01VH2ckvgGP9CGkb8Suno5f1, Opus 5.5 (D15, L37)). NOT a packet verdict: it signs no new
statement. It checks, for each landed result named by the Lead (message of 00:04Z, Lead's stamp), whether the statement and the PROOF
are start-free. Written 2026-10-26T00:07Z-00:10Z by date -u, on trunk 6021ea55 merged into claude/referee.

## 0. What "start-free" means here, and why it is enough
- SPEC S3: "Start (unless a start pair is given)". N5 is memoryless: the next state is a function of the current state (SPEC S4). So
  "every phase of every run from every start pair" = "the first phase of the run from every state (σ, τ)". (P-N5-DUAL §2 says the same.)
- A result is START-FREE if its proof uses only:
  - (S) statewise facts, true at every state (σ, τ) of any game in the class (valuation identities, optimality of Odd's counterstrategy,
    XW, Lemma G (a), …);
  - (T) per-transition facts of N5 steps from an arbitrary state (R15 (a), (c), (d), WM, (SG), FBL-N, CN-LAST, the S4a optimum (F1), …);
  - (W) inductions or counts over a phase / interval / stretch / run / window / θ-run, whose base is at the FIRST state of that window
    and is itself an (S) fact, and whose steps are (T) facts.
- A proof is NOT start-free if some step uses a property of σ_0, τ_0 as given by S3 (the best-reward rule), or of the history before
  the window it bounds (an invariant established in an earlier phase and assumed at the window's first state).
- Method per row: (1) the RESULTS entry's statement; (2) grep of the source packet and its fixes files for S3 / start pair / initial /
  σ_0 / τ_0 / best-reward / "state 0" / canonical / "from the start" / "first state of the phase" / "previous phase" (§3); (3) reading of
  the proof at the level stated in the column "read". Each hit of (2) was opened.

## 1. The table
| result | used for | statement start-free? | proof start-free? | read | where / why |
| --- | --- | --- | --- | --- | --- |
| R47 (a) Lemma Φ | λ / λ^U changes ≤ n(n−1) | yes (every run) | YES | full proof (P-N5-PHI §1) | (T): R15 (a), (d) per transition; R18 (d) Lemma S (b) "U non-increasing along the run" is a per-transition monotonicity; counting over the whole run from whatever its first state is. |
| R47 (b) Φ-1O | phases ≤ n(n−1) + d | yes | YES | full proof (§2) | (T): R15 (c), (d) on G^d (no τ repeats, from any τ); (S): R38 KEY (λ^U a function of τ). |
| R48 κ-FB-ROUND | FB-POLY | yes (per in-phase fallback) | YES | full proof | (T) at one fallback: (Aκ), (M1κ), (M2κ), S4c. |
| R48 κ-HAT-FREEZE (a)-(c) | FB-POLY | yes (per phase) | YES | full proof | (W): induction on j over the phase's own fallbacks g_j; base j = 0 is (A0κ), statewise; (b) is statewise ((HP), (SP′), (Aκ)). No use of any state before the phase. |
| R48 κ-PFZ | FB-POLY | yes (per θ-run) | YES | full proof | (W): induction over the θ-run's own fallbacks f^Θ_j; base j = 0 trivial (z = o). |
| R48 κ-Y-FORM | THETA-AFTER | yes (at an H1 state) | YES | full proof | (S): (Aκ), (HP), Lemma S (a) (R18 (d), statewise), Lemma G (a). |
| R48 EXIT-SWITCH, FREEZE-EXIT, CN-ONLY | FB-POLY | yes | YES | full proofs | (T)/(S) at one fallback; FREEZE-EXIT combines the two (W) lemmas above; CN-ONLY uses FBL-N (ii) (R21 (c)) and CN-LAST (R38 (f)), both per fallback. |
| R48 THETA-AFTER, Theorem FB-POLY | f per phase | yes | YES | full proofs | (W): monotone κ(o) along the phase after g_{|U|−2}, values from statewise sets V_H, V_N; the split of fallbacks counts within the phase. |
| R50-to-be P-N5-KW: W-ONCE | KW-S | yes (every game) | YES | full proof (my R-N5-KW §2) | (T): two consecutive S4a steps; arenas from their own states. |
| P-N5-KW Facts A0/A/B, H-PATH, PAR | all | yes (statewise on a stretch) | YES | full proofs | (S) plus stretch constants (R, θ, w); PAR uses XW (statewise). |
| P-N5-KW FRZ-U, LEN, KIND-MONO, CASC-B, CW-INT, E-SEG | RUN | yes (per run of a stretch) | YES | full proofs | (W): Claim P^c's base at the run's first state k0 is trivial (x = o); steps (T) (WM, (F1), R15 (a), (d)); CASC-B's induction starts at step 0 of any kind-stable W-flat segment (S_1 = 0 holds at any start); CW-INT per window. |
| P-N5-KW Theorem RUN, KW-S, Corollary PHASE | T per phase | yes | YES | full proofs | (W) per run / stretch / phase; PHASE cites only the rows below. |
| R15 (c), (d) | no σ / τ repeats; S4 steps are improving switches | yes (any σ; VJ00 Lemma 5.7 for any non-empty improving set) | YES | statement + RESULTS text | (T). R15's potential is defined on every strategy, not relative to a start. |
| R24 (e) WC | W_ch per crossing-free interval | yes | YES | full proof (P-N5-U1 §5) | (S) for w's form (c_w, ∅, d) under ¬H2; (W) monotone w on each fallback-free stretch of the interval (TB step 1 at o); counts from the interval's first state. N-U1-3 (EQ-state fallbacks) is per fallback. |
| R27 (d) Theorem LP | T ≤ (m−n+1)(T_rel+1) | yes (any game, per phase) | YES | full proof (P-N5-LP §1-§2) | Lemma U per transition; NU, GR, rises, L-runs: (W) inside the phase, base = the phase's first state with no hypothesis on it. |
| R27 (g) TH, SO | Θ, S_o | yes | YES | full proofs (P-N5-SO §1) | TH: (S) CAP-1 (R25 (e): σ̄(o) a full minimiser, statewise), (YB)-type form under ¬H1, F1° per interval; SO: (W) on each θ-constant run (T_k only shrinks; keys frozen), from the run's first state. |
| R30 (c) R-STICK, SN-PREFIX | X ≤ (f+1)(n−1) + f + X_SN | yes (per run of a phase) | YES | full proof (P-N5-SN §3) | (T): WM, XW, Lemma G (a) per S4a step; "initial part" (l. 72) is the prefix of the RUN, not of the N5 run. |
| R34 (b)-(e) L-MONO, Z-COUNT, TOGGLE, TOGGLE-COUNT | T_H := n² + 2n − 1 | yes (per phase) | YES | statements + grep; proofs read at structure level | (W) monotone quantities (cycle length L_k of c's honest play, Z_k) along the phase, (S) Fact (F). No base outside the phase. |
| R34 (f) X-SN-PHASE | X_SN | yes ("no hypothesis on H1") | YES, as far as read | statement + grep; R33 X-RUN′ / X-RUN° statements; R32 FREEZE proof read (P-N5-FRZ §3) | FREEZE / P^c_ℓ: (W) over a WINDOW, base j = 0 at the window's first state k0 by Fact 0 (statewise); X-RUN counts windows inside the phase. R33 (a)-(e) are per phase / per S4a step. Not every R32 / R33 proof step was re-read line by line here (they were refereed in full at landing); the grep (§3) has no start hit. |
| R22 (a) F1° | Ξ-changes on F | yes (per crossing-free interval) | YES | full proof (P-N5-NH §1) | (S) Lemma G (a); (T) FBL-N (ii) at fallbacks, (F1) at S4a steps; R17 Lemma P / Theorem PH on the F-subgame: "a statement about current values, and its step uses only the state it starts from" (P-N5-NH §1 step 4); R17 holds from any start: RESULTS R18 (c) records "R17 Corollary 2, which both referees confirmed holds from any start", and Lemma P's base is the interval's first state. |
| R22 (b) TC | H1 / H2 constant on an interval | yes | YES | full proof of (i) | (S) per state, constants of the phase and interval. |
| R38 (a) KEY | phase = joint λ-phase | yes | YES | statement | (S): U_τ depends on τ alone, so λ^U is a function of τ. |
| R21 (a) XW | Ξ ⊴ W | yes (every state) | YES | statement | (S): σ̄ is Odd's pointwise optimum in G_σ, so Ξ_σ ⊴ V_{σ,τ} = W for every τ. |
| R36 P1 | one-player games (via R37 BL (c), XG) | yes (not about N5 runs) | YES | statement | A statement about optimal strategies of a one-player game; no run, no start. |
| supporting, cited inside the rows above: R17 (F1); R18 (d) Lemma S (a), (b); R19 (a) Lemma G (a), (d) (SG); R21 (c) FBL-N (ii); R23 (g) WM; R25 (e) CAP-1; R38 (f) CN-LAST | — | yes | YES | statements | Each is (S) or (T). (SG): "at any N5 transition"; WM: every in-phase non-fallback transition; CN-LAST: at one fallback (every game). |

## 2. Result
- Every result in the Lead's list is START-FREE, in statement and proof: each proof is built from statewise facts, per-transition facts
  of N5 steps, and inductions / counts whose base is the first state of the window they bound (phase, interval, stretch, run, window,
  θ-run). No proof uses σ_0 or τ_0 as chosen by S3, or an invariant inherited from before its window.
- So for the 𝒞^1O chain: the per-phase bounds (FB-POLY; P-N5-KW's Corollary PHASE given f; the landed X, Θ, S_o, W_ch, LP bounds) bound
  the FIRST phase from every state, and with Φ-1O they bound runs from every start pair. This is the property MIRROR (H-N5) and the
  P-N5-1O assembly need (still CONDITIONAL on P-N5-KW landing; P-N5-FX and P-N5-NH-box42 are not in this list).
- Depth, stated plainly: rows marked "full proof" were read in full for this audit (most also in my own or my predecessors' reviews);
  R34 (b)-(f) and the R32 / R33 chain under X-SN-PHASE were read at structure level plus grep, with R32 FREEZE's induction base read.
  A line-by-line re-read of every R32 / R33 step was NOT done here.
- DATA (consistent, not proof): random start pairs were already used in our probes with 0 failures:
  - scratch/kw_logs/lib3_rs3.txt: library with 3 random start pairs per game: 965 runs, 4,194 phases, every Corollary PHASE inequality, LP, X
    (with X_SN's bound), Θ, S_o, W_ch;
  - scratch/fbpoly_logs/lib_rand4.log (predecessor): FB-POLY on 5,240 phases including 1,012 random-start runs;
  - scratch/dual_logs/lib41_rs2.txt: Φ-kO (hence Φ-1O on the 𝒞^1O files) with 2 random start pairs per game. (The KW climbs ran from the S3
    start only.)

## 3. Grep record (method step (2))
- Pattern: `\bS3\b|start pair|starting|initial|σ_?0\b|τ_?0\b|σ0|τ0|best.reward|k ?= ?0\b|state 0\b|from the start|run's start|canonical`, then
  `first state of the (run|phase)|phase's first|previous phase|earlier phase`, over the source packets and fixes files of R21, R22, R24,
  R27 (LP, SO), R30, R32, R33, R34, R36, R38, R47, R48 and P-N5-KW (+ addendum), excluding DATA / climb / random-start lines.
- Hits, each opened:
  - P-N5-PHI l. 23 "states (σ_k, τ_k), k = 0, 1, …": notation only.
  - P-N5-FBPOLY l. 269, 274-275: DATA (SPEC S3 or a given start; canonical start + random starts).
  - P-N5-LP l. 177: a refuted form (NO-WAKE), not a proof step.
  - P-N5-SN l. 72 "equality holds on an initial part only": SN-PREFIX's prefix of a fallback-free RUN.
  - P-N5-SN-fixes l. 64 "from the run's start": ABS-COUNT′ (R30), counting from the start of a fallback-free run; not in the chain.
  - P-N5-TOG-fixes2 l. 48 "state 0": a data instance (b4_cyc6_0).
  - P-N5-X-fixes l. 63 "Lemma P's induction step uses only its starting state": supports start-freeness.
  - P-N5-FRZ l. 34 "an initial segment": the SN prefix of a run.
- No hit is a dependence on the N5 run's start.

## Addendum 1 (2026-10-26T01:00Z by date -u; REFEREE successor 11, Opus 5.5, D15): the R32 / R33 chain, line by line
- The depth caveat of §2 ("A line-by-line re-read of every R32 / R33 step was NOT done here") is CLOSED. During the P-N5-1O review I read
  P-N5-FRZ-box34 §0-§7 (R32: NL-MF, Fact 0, ARENA, Steps 1-2, Lemma P^c_ℓ with cases A, B1, B2, B-fallback, Theorem FREEZE Steps 3-4,
  RATCHET, BLOCK, X-RUN, SUB) and P-N5-L2-box34 §1-§7 (R33: H3-CONST, H2-STICK, G′, FREEZE′, R-CONST, H1-INT, X-RUN′ / X-RUN°) line by line.
- Every step is statewise, one N5 transition, or a window / run / phase argument based at that window's first state; FREEZE explicitly
  makes "no hypothesis on the states after F" and nothing about states before k0. The table is in docs/referee/R-N5-1O.md §3.
- So the R34 (f) row is now "full proof" as well: every result in §1 is start-free, read in full.
