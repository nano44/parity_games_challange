# R72: P-N5-FX and P-N5-FBPOLY red-teamed (no kill); EXIT-SWITCH "loop" kind occurs; K growth survey (L-RED successor 18, box 42; GO 2026-10-25 19:52Z, date -u)
Targets (Lead 19:52Z):
- (1) P-N5-FX (docs/si/P-N5-FX-box14.md, sha1 aa227b0b), Corollary FX (a) and (b); P-N5-FBPOLY (docs/new/P-N5-FBPOLY-box41.md,
  sha1 de244dcd), §0.3 facts, §1 κ-lemmas, EXIT-SWITCH, FREEZE-EXIT, CN-ONLY, THETA-AFTER, FB-POLY (a)-(d).
- (2) K growth survey (wakes per phase; RESULTS R27, docs/si/N5-LEDGER-v2-box14.md §3, sha1 8ab27359).
- (3) FB-CAP at |U| ≥ 3; beta2 cascade.
𝒞^1O only: exactly one Odd vertex with out-degree > 1, asserted in every checker. Labels per L40: PROVED / CONJECTURE / OPEN / DATA /
READING. Nothing here is a running-time bound. G-N5-TIME stays OPEN.

## 0. Result
- **No kill of P-N5-FX or P-N5-FBPOLY.** 0 FAIL of every check on:
  - the library: 252 𝒞^1O runs at S3, then 750 runs at S3 + 2 random start pairs per file;
  - 8,546,164 random runs (S3 + 3 random start pairs per game, n 6-19).
- I also read both proofs line by line (§3) and found no gap. Two wording points are for the referees (§3); neither changes a statement.
- **DATA correction to P-N5-FBPOLY §7 / §8.** The packet says the "loop" kind (a switched u ∈ U ∖ T whose x*_u-play returns to u before T)
  "never occurs in data". It does occur: 10 times in the random runs. It is pinned as exsw_loop_n15 (§4). EXIT-SWITCH still holds there:
  other switched vertices exit to T. Not a kill: the lemma only claims SOME switched vertex exits.
- **K (DATA):**
  - Library: K = 0 per phase on 247 / 252 𝒞^1O runs.
  - L-NEW's K-chain family: Kt = K − 1 per phase, exactly, at K = 4, 10, 20, 32, 48 (n = 11K + 14). That is linear in n.
  - Climbs aimed at K: best Kt = 6 at n 58 (kchain4 seed, from 3) and 9 at n 124 (kchain10 seed, no gain). No superlinear growth.
  - Wording point. "K := #wakes" (R27) and "K counts transitions with a wake" (LEDGER-v2 §3) are different counts. A climb drives the
    switch count to 28 per phase at n 58 with a single wake transition. The ρ / T_P bound needs the transition count (§5).
- **FB-CAP:** n 6 random games × every start pair: no violation in 20,654,028 runs (§6). A READING of why the simplest |U| = 3
  configuration cannot give 2 fallbacks is in §6. FB-CAP stays OPEN. The beta2 cascade was not started.

## 1. Tools (experiments/red/fbx/; written from the frozen packet texts, not from fbpoly.py / fbpoly17.py / pfz17.py)
- fbx18.py, an exact checker for every statement of P-N5-FBPOLY §0.3-§6 and P-N5-FX §1 (a). Per phase (λ_Ξ and τ constant), it checks:
  - TKIND: in-phase transitions change σ only; at a fallback, the switched set = the gate sources, and x*_v = argmax (Ξ_k(w), w);
  - the facts (Aκ), (A0κ), (M2κ), (HP) (i), (ii) and agreement, (YB) and κ-Y-FORM, at every state;
  - κ-FB-ROUND for every Even v ∈ U ∖ {c_θ} and successor x ∈ U, at every fallback;
  - κ-HAT-FREEZE (a) for every j up to min(#fallbacks before t, |U| − 2), and (b), (c);
  - κ-PFZ for every j up to the θ-run fallback count, and its G_U form when o = c_θ (FB-POLY (c));
    path optima for both are exact: simple paths by reverse DFS from the sink with a 400,000-step budget; a phase over budget skips
    only the path checks (SKIP_paths);
  - EXIT-SWITCH: existence, p_u simple, p_u a path of G_Û / G_U^o (G_U if o = c_θ), and the κ identity, for EVERY exiting u;
  - FREEZE-EXIT, plus its two halves per exiting u (kind ct at j ≥ |U| − 1; kind o at i ≥ |U| − 1; at o = c_θ, i ≥ |U|);
  - CN-ONLY (gates, last state, count ≤ 1), THETA-AFTER, FB-POLY (a)-(d);
  - R-STICK at S4a steps with c_w ≠ c_θ; X ≤ n(f + X_SN) + n − 1 with X_SN = S4a crossings at states with c_w = c_θ.
  Trace: sox.trace (= n5.run, SPEC S3) or ex16.trace from a start pair.
- Checker bug found and fixed before any number below: the first version typed o = c_θ phases as "e = c_θ" in EXIT-SWITCH and
  reported false FAIL_EXSW_graph. These were checker errors, not kills. Every number below is from the fixed version.
- rfbx18.py (random games × start pairs), libst18.py (library × start pairs), lib18.sh (library, 4 parts), loopfind18.py (§4).
- k18.py: K from the R27 definition (relevant change, used level L_k, NU, consecutive relevant transitions, no fallback, R constant).
  It reports Kt (transitions with a wake) and Ks (wake switches), with the state type at the wake. kclimb18.py climbs on (max Kt,
  total Kt, iterations).

## 2. Data for (1) (0 FAIL in every row)
| space | runs | phases | AK | FBR | KHa / KHb / KHc | KPFZ (G_U form) | KYF / YB | EXSW kinds ct / o / loop | CNO fallbacks | THA phases (U ≥ 3) | RST | SKIP_paths |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| library, S3 + 2 random starts (libst18, seed 42) | 750 | 3,203 | 469,234 | 124,921 | 206,950 / 151,105 / 111 | 74,379 | 13,477 / 1,697 | 2,282 / 31 / 0 | 54 | 70 (6) | 1,186 | 591 |
| random n 6-13 / 6-16 / 6-19, S3 + 3 random starts (rfbx18 seeds 1-3, 3 × 2,400 s) | 8,546,164 | 19,903,984 | 136.9 M | 2.33 M | 17.2 M / 86.3 M / 652 k | 311 k (23 k) | 12.7 M / 9.4 M | 1,560 / 139 / 10 | 337,460 | 948,354 (18,320) | 7,261 | 0 |
Maxima (slack = value − bound; ≤ 0 means the bound holds):
- FB-POLY slack 0 (the bound is attained; the phase type was not recorded). FB-CAP slack 0.
- THETA-AFTER slack −1 everywhere.
- FX slack −2 in the library and −4 in the random runs. Max X = 100 in the library (n ≤ 70) and 6 in the random runs.
- The canonical-start library run (lib18.sh, re-run with the fixed checker: 252 runs, 1,047 phases) agrees: 0 FAIL, FX slack −2, THA
  slack −1.
- Regime (as in R71 and P-N5-FBPOLY §8): FREEZE-EXIT's hypothesis (j ≥ |U| − 1 and i ≥ |U| − 1, o ≠ c_θ) never occurs.
  So FREEZE-EXIT is tested only through its two halves, and only where those can occur.
- FX (a) pins re-measured: fx2_n11 (R71 §7) gives X = 8, slack −2.

## 3. READING of the two proofs (adversarial, line by line)
- P-N5-FX §1 (a). The proof partitions crossings into kinds (i)-(iii). Kind (iii) uses R-STICK, LANDED (R30 (c)). Inside a segment, R
  never shrinks: transitions that are not crossings leave R unchanged by definition, and kind (iii) crossings enlarge it. So R grows
  strictly at most n − 1 times per segment. No gap. (b) is substitution. The data slack is −2, so (a) is nearly tight
  (e.g. fx2_n11: X = 8, f = X_SN = 0, n − 1 = 10).
- P-N5-FBPOLY.
  - I traced (Aκ), (SP′), (HP), (YB), κ-FB-ROUND, the induction steps of κ-HAT-FREEZE (a) and κ-PFZ, EXIT-SWITCH's contradiction
    argument, FREEZE-EXIT's two cases, CN-ONLY's four sub-cases of (2), THETA-AFTER's value sets V_H / V_N, and the FB-POLY count. No gap.
  - Points for the referees (wording; no statement changes):
    - (W1) EXIT-SWITCH as stated says p_u "is a path of G_Û if e = c_θ and of G_U^o if e = o". When o = c_θ, both graphs drop the
      terminal, and FB-POLY (c) silently switches to G_U. Suggest one clause in §2: "if o = c_θ, of G_U". (My first checker made
      exactly this mistake.)
    - (W2) §7 / §8 say the "loop" kind never occurs. It does (§4). The §7 OPEN item ("whether it can occur for SOME switched vertex")
      is answered: yes, from a random start pair. Not yet seen from S3.

## 4. EXIT-SWITCH "loop" kind (DATA; not a counterexample)
- experiments/red/fbx/instances/exsw_loop_n15.pg (sha1 e38329f881ba6ad96b0a4f3d75c799188fc60056); start pair in
  exsw_loop_n15.start.json (sha1 03f43926523075f67364a3430d19a110a61deec9). 𝒞^1O, o = 12.
- Oink `--zlk --verify` on the game: exit 0, "solution verified (11 strategies)". This is a check of the game file only. A
  data point needs no N5 / Oink comparison.
- The run: the fallback 0 → 1 is in-phase, with c_θ = 0 and U = all 15 vertices. It switches 7: 12 → 0, 8: 3 → 14, 13: 8 → 14 and
  14: 5 → 1. The honest 0-plays from the new targets:
  - from x*_7: 0 (exits at c_θ);
  - from x*_8: 14 → 5 → 8 (back to u = 8 before T: kind loop);
  - from x*_13: 14 → 5 → 8 → 3 → 7 → 12 (exits at o);
  - from x*_14: 1 → 2 → 11 → 0 (exits at c_θ).
  So u = 8 is a loop, and EXIT-SWITCH holds through 7, 13 and 14.
- Frequency: 10 loop vertices among 1,709 switched U ∖ T vertices in 8.5 M random runs; 0 in the library (S3 and start pairs).

## 5. (2) K growth (DATA)
| set | n | max Kt per phase | max Ks per phase | iterations |
| --- | --- | --- | --- | --- |
| library (252 𝒞^1O runs, S3) | ≤ 70, plus kchain | 0 on 247 runs; so_k2_n32 2; nowake_cex_n32 1 | same | – |
| kchain K = 4 / 10 / 20 / 32 / 48 (kchain.py; K = 4, 10, 32 = L-NEW pins 2be32f30 / 4af3726f / 63c5b0dd; K = 20, 48 regenerated, sha1 8496b64a / cea4b0b6) | 58 / 124 / 234 / 366 / 542 | 3 / 9 / 19 / 31 / 47 | same | K + 2 |
| climb on Kt from kchain4 (kclimb18 seed 22, 2,700 s); pinned instances/kt6_n58.pg, sha1 41d4f7cb…, Oink `--zlk --verify` exit 0 | 58 | 6 | 6 | 38 |
| climb on Kt from so_k2_n32 (seed 21, stopped at 245 s) | 32 | 2 | 2 | 47 |
| climb on Kt from kchain10 (seed 31, 1,800 s) | 124 | 9 (no gain) | 12 | 53 |
| climb on Ks from so_k2_n32 / kchain4 (first objective, abandoned) | 32 / 58 | 1 / 1 | 20 / 28 | 6 / 10 |
- Every wake in every row is at a ¬H1 ∧ ¬H2 state (k18 type "U23"). That includes the K-chain family, which docs/new/N5-K-box33.md
  calls U3; by the H1 test (o on its honest cycle), its wake states are ¬H1.
- Growth: Kt = K − 1 = (n − 25)/11 on the family: linear. The climbs found no family with faster growth.
- READING (why superlinear K needs long phases):
  - Inside a run of consecutive relevant transitions that are all wakes, the used levels rise strictly. The levels are vertex ranks in
    the BAND (R27 (e)), so such a run has at most n wakes.
  - More wakes per phase need many non-wake relevant transitions (level drops), with R constant and no fallback.
  - The library phases never show this. N5's iteration counts there are ≤ a few hundred.
- Counting point (for L-SI 10 / L-NEW 21). Ks can be made large cheaply: many Even vertices wake at one transition. R28 (c)'s ρ ≤ 2f + 2X +
  K is a count of rises, i.e. transitions, so the transition count Kt is the one that must be bounded. R27's "K := #wakes" should be
  read as Kt (or the bound holds a fortiori with Ks ≥ Kt).

## 6. (3) FB-CAP (OPEN)
- fbcap17 (R71's tool, unchanged), random n 6 games × every start pair (seed 18, 3 jobs, 2,100 s): 20,654,028 runs, 0 violations (also FB-PHASE slack ≤ −7, FX slack ≤ −3);
  per-|U| max of g − max(1, |U| − 2): 0 / 0 / 0 / −1 / −2 / −3 for |U| = 1-6. This extends R71's n ≤ 5 tables to n = 6, in part.
- READING (an obstruction sketch, not a proof). Take |U| = 3, o = c_θ, U = {o, a, b}. Two non-CN fallbacks need the chain "b: a → o,
  then a: o → b".
  - The Ξ-gates force κwt(a) < 0 < κwt(b) and κwt(a) + κwt(b) ≤ 0. So a is odd, b is even, and rank(a) > rank(b) > rank(o).
  - Neither switch may be W-improving (else S4a takes it). This needs W's signs on a and b to be opposite to Ξ's.
  - For every rank position of c_w (above a, between b and a, below b) one of the two switches is W-improving. So the chain fails.
  - The sketch does not cover W-plays through a and b (τ(o) ∈ U), larger U, or chains with o-routes after a θ-change. Those are FB-CAP's
    real cases (P-N5-FBPOLY §7 (FB-CAP-1), (FB-CAP-2)).
- beta2 cascade (≥ 3 r = −1 fallbacks in one scope run): NOT STARTED this box.

## 7. Dead ends of this box (each with its obstruction and instance)
- Climbing on Ks (wake switches): the climb inflates simultaneous switches at one wake transition (snap_kch4: Ks 28, Kt 1, n 58). The
  transition count does not grow. Obstruction: Ks is the wrong quantity (§5).
- Random-game hunting for FREEZE-EXIT / THETA-AFTER failures: their hypotheses need j ≥ |U| − 1, which is FB-CAP's regime. It is never
  reached (§2, and R71).

## 8. Open (for the Lead to route)
- FB-CAP at |U| ≥ 3 (a kill would open FREEZE-EXIT's regime); beta2 cascade.
- Whether the "loop" kind occurs from S3.
- K: a two-chain construction (wake chain, level drop, second chain, all with R constant) is the natural next attempt at superlinear Kt.
