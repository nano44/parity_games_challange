# FB-POLY beyond 𝒞^1O: in-phase fallbacks per phase on every game (box 44, item (i))
L-NEW successor 23 (Opus 5.5), D14 / D18, Lead reading L40; Lead's GO (i) 01:53Z (Lead's stamp). Written 2026-10-26 01:55Z-02:01Z (date -u).
Working doc, not a packet, unrefereed. Labels: PROVED (L-NEW 23, unrefereed) / CONJECTURE / OPEN / DATA / READING.
TARGET.md diff: nothing here is a claim of TARGET.md §1. No polynomial bound for N5 is proved on any class beyond 𝒞^1O ∪ 𝒞^1E.
Source ported: docs/new/P-N5-FBPOLY-box41.md (= RESULTS R48, landed; its fixes file P-N5-FBPOLY-fixes-box41.md), cited "FBP §x".

## 0. Setting (every game)
- N5, phases (maximal runs with (λ_Ξ, τ) constant; = joint λ-phases, R38 (a)), in-phase transitions (S4a steps or Even S4c fallbacks),
  g_1 < g_2 < … the in-phase fallbacks of a phase: as in FBP §0.1.
- The set-form choice. FB-POLY works entirely in the HONEST frame (Ξ, next_t := σ_t at Even vertices, σ̄_t at Odd ones); W enters
  only through FBL-N (ii) in CN-ONLY. On 𝒞^1O its single non-forced vertex is o, which is why its terminal set is T = {o, c_θ} and its
  graphs drop o. On a general game σ̄_t can move at EVERY Odd choice vertex inside a phase (τ is fixed, σ̄ is not), so the right set is
  not D_k but the static set
  - Q := the Odd vertices of out-degree ≥ 2 (Odd choice vertices), and
  - C := the honest cycle nodes of the phase (λ is constant on a phase, so C and the classes below are constant),
  - T := C ∪ Q (TERMINALS), and for c ∈ C the HONEST CLASS U_c := λ^{-1}(c).
  On 𝒞^1O with U = U_{c_θ}: T ∩ U = {o, c_θ}, FB-POLY's T. The other classes of 𝒞^1O contain no Odd choice vertex.
- κ per class: for z ∈ U_c, κ_t(z) := (signed weight of P(Ξ_t z), s_c·ℓ(Ξ_t z)) with s_c := +1 if Ω(c) is odd, −1 if even; wt_c(v) :=
  sgn(v)·2^rank(v) if rank(v) > rank(c), else 0; κwt_c(v) := (wt_c(v), s_c). (FBP §0.1 with c for c_θ.)
- At a fallback k → k+1: S_k := the switched (Even) vertices; S := S_k ∖ T; S_c := S ∩ U_c; x*_v := σ_{k+1}(v).
- Graphs (c ∈ C; a sink keeps no edges): G_c := U_c ∖ (Q ∖ {c}) with c a sink, Even vertices keeping their edges inside, Odd
  vertices (all forced there) their edge if inside. For q ∈ Q ∩ U_c, q ≠ c: G_c^q := U_c ∖ (T ∖ {q}) ∪ {q} with q a sink, same rules.
  κopt_c(z) := max{κwt_c(p ∖ {c}) : p a simple path of G_c from z to c}.
- A Q_c-RUN: a maximal run of consecutive states of the phase with Ξ(q) constant for every q ∈ Q ∩ U_c (on 𝒞^1O: a θ-run). A
  Q-RUN: the same with all q ∈ Q.
- ρ := the number of pairs (transition t → t+1 of the phase, q ∈ Q) with Ξ_{t+1}(q) ≠ Ξ_t(q).

## 1. The steps, one by one (the Lead's list)
| FB-POLY step (FBP §) | verdict | form on every game | one-Odd use in the 𝒞^1O proof, and its replacement |
| --- | --- | --- | --- |
| facts (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′) (§0.3) | SURVIVE | per class U_c, c for c_θ | none: (V1), R15 (a), S1, lasso shape |
| (HP) (§0.3) | FAILS as stated; set form (HP_D) holds | honest play = (σ, τ)-play off D_k | "Odd vertices ≠ o are forced" (FO). Not needed below: every use of (HP) is replaced by "honest play avoids Q" (definition) |
| (YB) (§0.3) | SURVIVES per vertex | for q ∈ U_c on its own honest cycle: P(Ξ(q)) = ∅, ℓ ≤ |U_c| − 1 | none (top of the cycle is c) |
| κ-FB-ROUND (§1) | SURVIVES verbatim | every Even v ∈ U_c ∖ {c}, every successor x ∈ U_c, every class | none ((Aκ), (M1κ), (M2κ), S4c) |
| κ-HAT-FREEZE (a)-(c) (§1) | SURVIVES in set form | G_c (drops Q ∖ {c} instead of o); (b), (c) for z whose honest play avoids Q ∖ {c} | (a): "z Odd ⇒ forced": true in G_c, which keeps only non-choice Odd vertices. (b): "z ∈ F ⇒ honest play avoids o" (HP) → hypothesis "honest play avoids Q ∖ {c}" |
| κ-PFZ (§1) | SURVIVES per terminal | for each q ∈ Q ∩ U_c: paths of G_c^q to q, on Q_c-runs (κ(q) constant) | "z Odd (z ≠ o) ⇒ forced": true in G_c^q |
| κ-Y-FORM (§1) | SURVIVES per terminal (repaired Y) | Y^q_t := {y ∈ succ(q) ∩ U_c : y's honest play avoids q}; at states where q is on no honest cycle: κ(q) = κwt(q) + min_{Y^q} κ(y) | "every other Odd vertex is forced" made y's (σ, τ′)-play its honest play; with τ′ := σ̄_t except τ′(q) := y this holds by definition (the ledger's repair, N5-MULTI §2) |
| EXIT-SWITCH (§2) | SURVIVES, several terminals | per class: some u ∈ S_c has a target whose k-play meets T ∩ U_c before u; e ∈ T ∩ U_c | "Odd w ≠ o forced, so next_{k+1}(w) = next_k(w)" for non-terminal w: non-terminal Odd vertices have out-degree 1 by definition of Q |
| FREEZE-EXIT (§3) | SURVIVES per class | g_j with j ≥ |U_c|, i-th fallback of its Q_c-run with i ≥ |U_c| ⇒ S_c = ∅ (conservative indices; FBP's |U| − 1 form not needed) | none beyond the three above |
| CN-ONLY (§4) | SURVIVES (new proof of one case) | a fallback with S = ∅ is CN-LAST; ≤ 1 per phase | (1) used (HP) + FBL-N (ii) to make switched y ∉ U cycle nodes: with T ⊇ C, S = ∅ gives it directly. (2), case "meets o first": replaced by "meets some q ∈ Q first" (§2.3) |
| THETA-AFTER (§5) | FAILS as proved | — | Y ⊆ F ∩ U was frozen by HAT-FREEZE (c) because Y's plays avoid o, the only terminal; with several terminals y ∈ Y^q may route through another q′ ∈ Q, whose value is not frozen. Obstruction §3; DATA §4 |
| FB-POLY (§6) | REDUCED | f ≤ 1 + (n − 1)(2 + ρ) (Theorem FB-RED, §2.4) | THETA-AFTER replaced by the count ρ |

## 2. Proofs of the set-form steps (PROVED, every game)
Each proof is the FBP proof with the substitutions of the table. Only the changed lines are written out.
### 2.1 Facts and κ-FB-ROUND
- (Aκ): for z ∈ U_c ∖ {c}: λ_t(z) = c ≠ z, so (V1) gives Ξ_t(z) = z ⊕ Ξ_t(next_t z) with cycle node c; next_t(z) ∈ U_c, and κ_t(z) =
  κwt_c(z) + κ_t(next_t z) (FBP's no-double-count argument with c). (A0κ), (M1κ), (M2κ), (INJ), (SP′): FBP §0.3 with c for c_θ
  ((SP′): the prefix of z's honest play up to its first visit of T ∩ U_c is simple, since c ∈ T lies on the cycle).
- κ-FB-ROUND: FBP §1 verbatim with U_c, c (its proof uses only (Aκ), (M1κ), (M2κ) and S4c's best-key rule).
### 2.2 κ-HAT-FREEZE, κ-PFZ, κ-Y-FORM
- κ-HAT-FREEZE (a): for t > g_j, z ∈ U_c ∖ (Q ∖ {c}) and every simple path p of G_c from z to c with ≤ j edges, κ_t(z) ≥
  κwt_c(p ∖ {c}). Induction as FBP: Odd z on p is a vertex of G_c, hence not in Q, hence forced, and its forced successor x is
  next_t(z); Even z uses κ-FB-ROUND at g_j. (b): if z's honest play at t avoids Q ∖ {c} and z ∈ U_c, its prefix to c is a simple
  path of G_c ((SP′); Even edges σ_t, Odd vertices on it are not in Q, so forced), and (Aκ) gives κ_t(z) ≤ κopt_c(z). (c): simple
  paths of G_c have ≤ |U_c ∖ (Q ∖ {c})| − 1 ≤ |U_c| − 1 edges; with ≥ 1 vertex of Q ∖ {c} in U_c, ≤ |U_c| − 2. So for t > g_{|U_c|−1}
  (or g_{|U_c|−2} if Q ∩ U_c ⊄ {c}), κ_t(y) = κopt_c(y) for every y ∈ U_c whose honest play at t avoids Q ∖ {c}.
- κ-PFZ (per q ∈ Q ∩ U_c, q ≠ c, Θ a Q_c-run): for t ∈ Θ with t > f^Θ_j, z ∈ U_c ∖ T and every simple path p of G_c^q from z to q
  with ≤ j edges: κ_t(z) ≥ κwt_c(p ∖ {q}) + κ_t(q). FBP §1 verbatim (Odd vertices of G_c^q other than q are forced).
- κ-Y-FORM (per q ∈ Q ∩ U_c, q ≠ c, at a state t where q lies on no honest cycle): κ_t(q) = κwt_c(q) + min_{y ∈ Y^q_t} κ_t(y).
  "≥": σ̄_t(q) ∈ Y^q_t (its honest play is the rest of q's, which does not return to q). "≤": for y ∈ Y^q_t let τ′ := σ̄_t except
  τ′(q) := y. y's (σ_t, τ′)-play is its honest play (it avoids q, the only vertex where τ′ and σ̄_t differ), so V_{σ_t,τ′}(y) = Ξ_t(y)
  and V_{σ_t,τ′}(q) = q ⊕ Ξ_t(y). Lemma S (a) (R18 (d)): Ξ_t(q) ⊴ q ⊕ Ξ_t(y); both have cycle node c; (M1κ). ∎
### 2.3 EXIT-SWITCH, FREEZE-EXIT, CN-ONLY
- EXIT-SWITCH_D. Let k → k+1 be an in-phase fallback and S_c ≠ ∅. Then some u ∈ S_c has: the honest play at k from x*_u visits
  T ∩ U_c before it visits u. For the first such vertex e: p_u := u · (that play up to e) is a simple path of G_c (e = c) or G_c^e
  (e ∈ Q), and κ_k(x*_u) = κwt_c(p_u ∖ {u, e}) + κ_k(e). Proof: FBP §2 with S_U → S_c, T → T ∩ U_c. The one changed sentence: a vertex
  w ∈ U_c ∖ T with w ∉ S_k has next_{k+1}(w) = next_k(w), because Even w keeps σ, and Odd w ∉ Q has one successor. (The k+1-play from
  v ∈ S_c stays in U_c by (Aκ) and visits c ∈ T by (SP′); the rest is verbatim.)
- FREEZE-EXIT_D (conservative indices). If k = g_j with j ≥ |U_c|, and k is the i-th fallback of its Q_c-run Θ with i ≥ |U_c|,
  then S_c = ∅. Proof (FBP §3 with one more round of slack). Suppose S_c ≠ ∅; take u, e, p_u from EXIT-SWITCH_D. p_u is simple in U_c,
  so it has ≤ |U_c| − 1 edges.
  - e = c: p_u is a path of G_c from u (u Even, so u ∉ Q). k > g_{|U_c|−1} (j ≥ |U_c|), so κ-HAT-FREEZE (a) at k gives κ_k(u) ≥
    κwt_c(p_u ∖ {c}) = κwt_c(u) + κ_k(x*_u) (EXIT-SWITCH_D, κ_k(c) = (0, 0)).
  - e = q ∈ Q: p_u is a path of G_c^q from u ∈ U_c ∖ T; k ∈ Θ and k > f^Θ_{|U_c|−1} (i ≥ |U_c|), so κ-PFZ gives κ_k(u) ≥
    κwt_c(p_u ∖ {q}) + κ_k(q) = κwt_c(u) + κ_k(x*_u).
  In both cases (Aκ) at u gives κ_k(σ_k u) ≥ κ_k(x*_u), against the gate Ξ_k(x*_u) ▷ Ξ_k(σ_k u) (both in U_c; (M1κ)). ∎
  (FBP's sharper |U| − 1 indices use that p_u avoids one of the two terminals; with |T ∩ U_c| ≥ 2 the same sharpening holds, but it
  is not needed for a polynomial bound.)
- CN-ONLY_D. If an in-phase fallback k → k+1 has S = ∅, then every gate (y, z) has λ_k(y) = y and lev(Ξ_k(σ_k y), Ξ_k(z)) = −1; so
  (CN-LAST, R38 (f), every game) k + 1 is the last state of its phase, and a phase has at most one such fallback.
  Proof. (1) S4c switches exactly the gate sources; S = ∅ means each lies in T; they are Even, so in C: cycle nodes. (No (HP), no
  FBL-N (ii).) (2) For a switched y ∈ C: P(Ξ_k σ_k y) = ∅ (FBP §4 (2) first bullet). For x*_y: x*_y = next_{k+1}(y) lies on y's
  honest cycle at k+1 and λ_k(x*_y) = y. Let π be the k-play from x*_y up to its first vertex of T ∩ U_y (it reaches y, so π exists).
  Its vertices are in U_y ∖ T: not switched (S = ∅), Even with σ unchanged or Odd with one successor; so π is also the k+1-play.
  - First T-vertex is y: y's k+1 cycle is y · π, its top is y, so P(Ξ_k x*_y) = ∅.
  - First T-vertex is q ∈ Q, q ≠ y: the k+1-play from y is y · π · q · (q's k+1-play) and returns to y, so π and q lie on y's k+1
    cycle, below y in rank: wt_y = 0 on π, and P(Ξ_{k+1}(q)) = ∅, i.e. M_{k+1}(q) = 0. By (Aκ) along π at k and (M2κ) at q:
    M_k(x*_y) = M_k(q) ≤ M_{k+1}(q) = 0. The gate and (A0κ) (M_k(σ_k y) = 0) with (M1κ) give M_k(x*_y) ≥ 0. So M_k(x*_y) = 0 and
    P(Ξ_k x*_y) = ∅ (INJ).
  (This is FBP §4 (2)'s last bullet, with q for o; it needs no H1-type fact.) (3) FBP §4 (3) verbatim. ∎
### 2.4 Theorem FB-RED (PROVED, every game)
For every phase of N5 on any game, with f its in-phase fallbacks and ρ its Ξ-changes at Odd choice vertices (§0):
f ≤ 1 + (n − 1) + (n − 1)·(1 + ρ) = 1 + (n − 1)(2 + ρ).
Proof. Split the fallbacks g_j:
- S = ∅: at most 1 (CN-ONLY_D).
- S ≠ ∅ and j ≤ n − 1: at most n − 1.
- S ≠ ∅ and j ≥ n: some class c has S_c ≠ ∅; j ≥ n ≥ |U_c|; by FREEZE-EXIT_D g_j is among the first |U_c| − 1 ≤ n − 1
  fallbacks of its Q_c-run, hence among the first n − 1 of its Q-run (a Q-run is a sub-run of the Q_c-run containing it).
  The phase has at most 1 + ρ Q-runs, each with ≤ n − 1 such fallbacks.
Total ≤ 1 + (n − 1) + (n − 1)(1 + ρ). ∎
On 𝒞^1O, ρ = the θ-changes of the phase (Q = {o}); FB-POLY's THETA-AFTER bounded the ones after the hat freeze by deg_U(o) + |U| − 2,
which is what made FB-POLY unconditional. (The constant here, n − 1 instead of |U| − 2, comes from FREEZE-EXIT_D's conservative indices.)

## 3. THETA-AFTER: the obstruction (OPEN)
- On 𝒞^1O after the hat freeze, at H1 states κ(o) = κwt(o) + min over Y ⊆ F ∩ U, and HAT-FREEZE (c) fixes every κ(y), y ∈ Y, at
  κoptÛ(y): κ(o) takes ≤ deg_U(o) values at H1 states, ≤ |U| − 1 at ¬H1 states.
- Several terminals. κ-Y-FORM still gives κ(q) = κwt(q) + min_{y ∈ Y^q} κ(y). But y ∈ Y^q may route to another terminal q′ ∈ Q ∩ U_c
  before c: then κ(y) = κwt(path y → q′) + κ(q′) by (Aκ). κ-HAT-FREEZE freezes only vertices whose honest play avoids Q ∖ {c}; for
  routed y, κ-PFZ gives only a LOWER bound per Q_c-run, and κ(q′) itself moves. So κ(q) has no value set independent of the run, and
  THETA-AFTER's count does not transfer. This is the honest-frame face of the multi-terminal problem (the W-frame face is Δ-RT,
  N5-DELTA-box44 §8): values at Odd choice vertices depend on each other through routes, a two-player shortest-path structure,
  where 𝒞^1O had one Odd decision per play.
- What a repair would need (CONJECTURE ρ-POLY): ρ ≤ poly(n) per phase. A natural route: a nested freeze. Order the terminals by
  the round at which their routing stabilises; if, after round r, the terminal graph (which terminal each Y^q routes to) is acyclic
  and stable, values freeze bottom-up, and each level costs ≤ deg + |U| changes. Two gaps: the terminal graph need not stabilise
  (σ̄ moves), and nesting depth up to |Q| multiplies the per-level counts, which gives (deg + |U|)^{|Q|}, exponential in k. OPEN.
- DATA (§4): the per-terminal THETA-AFTER bound (Ξ(q)-changes after g_{|U_c|−2} ≤ deg_{U_c}(q) + |U_c| − 2) held in every sample so far (733 checks, 0 violations; §4). So THETA-AFTER fails as PROVED, with no instance against
  its per-terminal statement yet; climbs aimed at one (fbclimb.py --obj ta, 4 runs) found none (§4).

## 4. Data (DATA, not proof): experiments/new/box44/fbf.py, fbclimb.py
fbf.py checks per phase: CN-ONLY_D (≤ 1 fallback with S = ∅, followed by the phase end), EXIT-SWITCH_D (at each fallback and class
with S_c ≠ ∅), FREEZE-EXIT_D (in FBP's sharper form j ≥ |U_c| − 1, i ≥ |U_c| − 1, which implies the conservative form proved), FB-RED,
and the per-terminal THETA-AFTER bound (TA); it records the max in-phase fallbacks per phase (FMAX) and max ρ. Canonical S3 start.
| sample | runs | phases | FMAX (n) | CN-ONLY_D (S = ∅) / viol. | EXIT-SWITCH_D / viol. | FREEZE-EXIT_D / viol. | FB-RED viol. | TA checks / viol. | max ρ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `--list ../box41/lib41.txt` | 412 | 2,335 | 33 (n 48, 𝒞^1O) | 26 / 0 | 689 / 0 | 29 / 0 | 0 | 65 / 0 | 160 |
| `--rand 2000 5 14 51` | 2,000 | 4,200 | 1 | 59 / 0 | 0 / 0 | 28 / 0 | 0 | 405 / 0 | 4 |
| `--rand 1500 10 26 52` | 1,500 | 3,950 | 1 | 65 / 0 | 0 / 0 | 34 / 0 | 0 | 263 / 0 | 8 |
| box43 + box44 instances (9) | 9 | 54 | 4 (n 24) | 0 / 0 | 13 / 0 | 4 / 0 | 0 | 2 / 0 | 36 |
Frontier games (≥ 2 Odd and ≥ 2 Even choice vertices) in lib41: 126; their largest in-phase fallback count per phase is 14
(experiments/red/n5inj/instances/returns_rt64.pg, n 64, 2 Odd choice vertices); then 8 (phase2_pk48, n 48), 7 (elimn_cex_n48, n 48,
3 Odd), 6 (returns_rt32 / phase2_pk32, n 32). The 𝒞^1O maxima are larger (33 at n 48, ccl_w48_n48), within FB-POLY.
Climbs for FMAX vs n (fbclimb.py, random starts, k = Odd choice vertices): k 2 n ≤ 10: 1; k 3 n ≤ 16: 1; k 3 n ≤ 24: 1; k 4 n ≤ 32: 1;
k 4 n ≤ 48: 9 (n 47). Random frontier games almost never have two fallbacks in one phase; seeded climbs from the lib41 frontier games
above were run next (appended 02:06Z):
| seed game (lib41, frontier) | n | its FMAX | climbed FMAX (n) | max ρ there |
| --- | --- | --- | --- | --- |
| returns_rt32 | 32 | 6 | **17** (n 32) | 10 |
| phase2_pk48 | 48 | 8 | 10 (n 46) | 4 |
| elimn_cex_n48 (3 Odd) | 48 | 7 | 8 (n 47) | 30 |
| returns_rt64 | 64 | 14 | **21** (n 64) | 27 |
| frz40 (4 Odd) | 40 | 3 | 9 (n 40) | 18 |
(3,000 steps each, fbclimb.py 0 0 3000 71-75 --seed; no violation of any PROVED statement in any scored game.)
Instance experiments/new/box44/instances/fb17_n32.pg (n 32, 2 Odd and 23 Even choice vertices, sha1 398e23e2eb18aac3c75af0b500a5d292f57a1d1e):
one phase with 17 in-phase fallbacks (29 iterations in all, 5 phases), ρ = 10; FB-RED's bound there is 1 + 31·12 = 373. N5's output:
Oink verify OK, regions = Oink --zlk, harness verify.py OK. Reading: frontier fallbacks per phase reach ~n/2 in climbs (17 at n 32,
21 at n 64); the 𝒞^1O maxima are similar (33 at n 48). No superlinear growth is visible; DATA, not a bound.
TA climbs (fbclimb.py --obj ta, seeds 81-84: k 3 n ≤ 16, k 4 n ≤ 24, k 2 n ≤ 12, frz40 seed): 0 violations of the per-terminal
THETA-AFTER bound in every scored game (max ρ 22, 20, 6, 33). So THETA-AFTER fails as a PROOF on the frontier, but no instance
against its per-terminal statement is known.
Runs 2026-10-26 01:56Z-02:05Z (date -u), from experiments/new/box44.

## 6. ρ-POLY: the nested-freeze attempt (Lead's GO 02:21Z; written from 02:31Z by date -u)
### 6.1 Theorem FB-RED, late form (PROVED, every game)
Only Q-runs that hold a LATE fallback (g_j with j ≥ n) count: f ≤ 1 + (n − 1) + (n − 1)·N_late, with N_late := the number of Q-runs
of the phase holding a fallback g_j, j ≥ n. Proof: §2.4's third bullet counts, per Q-run, only the fallbacks g_j with j ≥ n.
N_late ≤ 1 + ρ_late, ρ_late := Ξ-changes at Odd choice vertices at transitions after g_{n−1}. (On 𝒞^1O this is the form FB-POLY uses:
THETA-AFTER bounds only the θ-runs that meet late states.)
### 6.2 Lemma TV (terminal-value freeze; PROVED, every game)
Let Θ be a Q-run of a phase, c ∈ C, and t ∈ Θ with t > g_{|U_c|−1} and t > f^Θ_{|U_c|−1} (after |U_c| − 1 fallbacks of the phase and
of Θ). Then for every z ∈ U_c ∖ T:
κ_t(z) = V_z(κ(Q)) := max( κopt_c(z), max_{q ∈ Q ∩ U_c, q ≠ c} [κopt^q(z) + κ_Θ(q)] ),
with κopt^q(z) := max{κwt_c(p ∖ {q}) : p a simple path of G_c^q from z to q} (max over an empty set omitted).
Proof. "≥": every simple path of G_c or G_c^q has ≤ |U_c| − 1 edges; κ-HAT-FREEZE (a) at t > g_{|U_c|−1} gives κ_t(z) ≥ κopt_c(z);
κ-PFZ at t > f^Θ_{|U_c|−1} (Θ lies inside a Q_c-run, so its fallbacks are fallbacks of that run) gives κ_t(z) ≥ κopt^q(z) + κ_Θ(q).
"≤": z's honest play at t up to its first vertex e of T ∩ U_c is a simple path ((SP′)) whose Odd vertices before e are forced; if
e = c it is a path of G_c and (Aκ) gives κ_t(z) ≤ κopt_c(z); if e = q it is a path of G_c^q and κ_t(z) = κwt_c(path ∖ {q}) + κ_t(q)
≤ κopt^q(z) + κ_Θ(q). ∎
So late in a Q-run every non-terminal κ is a fixed function of the terminal vector κ(Q); and by κ-Y-FORM / (YB), each terminal value
satisfies κ(q) ∈ {κwt_c(q) + V_y(κ(Q)), κwt_c(q) + κ(q′) (y = q′ ∈ Q), κwt_c(q) (y = c) : y ∈ succ(q) ∩ U_c} at states where q is on no
honest cycle, and κ(q) ∈ {(0, s_c·ℓ) : 1 ≤ ℓ ≤ |U_c| − 1} where it is.
### 6.3 Why the nested freeze stalls (OPEN)
- Gap 1 (short late Q-runs). TV applies only after |U_c| − 1 fallbacks INSIDE the Q-run. A Q-run can end, by an S4a step or a
  fallback that raises some κ(q), before that. Each such run contributes ≤ |U_c| − 1 fallbacks, which FB-RED already counts; what
  is not bounded is how many there are. On 𝒞^1O, THETA-AFTER bounded them through values, not through run lengths.
- Gap 2 (no small value set). On 𝒞^1O the late values of κ(o) lay in a fixed set of ≤ deg + |U| values (Y frozen). Here, by 6.2, the
  late values of κ(Q) are constrained only by the consistency system κ(q) ∈ Φ_q(κ(Q)), whose solutions are sums of path weights
  through the terminal graph (Odd at q picks y, the play then follows an Even-maximal path to c or to a next terminal). Their number is
  not bounded by a polynomial a priori: the weights are 2^rank.
- What the system is (READING): a min-max total-weight reachability game on the terminal set Q ∪ {c} per class, Odd choosing at q,
  Even choosing paths, with the frozen path weights κopt_c, κopt^q as edge weights. A run of late Q-runs with S4c rounds in between
  looks like value iteration on that game. Value iteration on total-weight games with exponential weights is not polynomial in
  general, so a proof of ρ-POLY needs more than freezing: some monotonicity of the terminal order (L-SI's TC-SWITCH asks a similar
  question for terminal changes on R_D).
- The nesting route of §3 (bottom-up freeze when the terminal routing is acyclic and stable) gives at best (deg + |U|)^{depth}, with
  depth up to |Q|: polynomial for fixed k, exponential in k, the same shape as Φ-kO.
- Verdict: ρ-POLY stays CONJECTURE; FB-RED (both forms) and TV are what is PROVED.
### 6.4 DATA on ρ and on the late regime
fbf.py now also checks FB-RED's late form (REDL) and records N_late and ρ_late. Max ρ per phase (all Odd choice vertices summed):
| sample | max ρ in one phase | N_late / ρ_late max | REDL viol. |
| --- | --- | --- | --- |
| lib41 (412 runs, 2,335 phases) | 160 (leanT_N32, n 256, 64 Odd choice vertices; 96 on leanT_N24, n 192) | 0 / 0 | 0 |
| box43 + box44 instances (10) | 36 | 0 / 0 | 0 |
| ρ climbs, random start (fbclimb.py --obj rho 91-93) | 6 (k 2, n 12), 15 (k 3, n 20), 25 (k 4, n 31) | 0 / 0 | 0 |
| ρ climbs seeded (95-97: returns_rt32, elimn_cex_n48, frz40) | 13 (n 31), 28 (n 47), 32 (n 40) | 0 / 0 | 0 |
Reading (DATA): ρ per phase stays below n in every climb (and ≈ 0.6n on the tcpert family with |Q| ≈ n/4). NO phase in any sample or
climb has n in-phase fallbacks, so the late regime (j ≥ n) where FB-RED's third bullet, TV and THETA-AFTER act is never reached: as
on 𝒞^1O (FBP §8), the open count is vacuous in the data, and ρ-POLY rests on nothing but a proof that is not there.
Runs 2026-10-26 02:31Z-02:33Z (date -u).

## 7. Direction (b): late Q-runs as value iteration on a terminal game (Lead 02:47Z; chosen by L-NEW 23, see notebook; written 02:54Z by date -u)
Source opened (notebook "Sources opened"): T. Brihaye, G. Geeraerts, A. Haddad, B. Monmege, "To Reach or not to Reach? Efficient
Algorithms for Total-Payoff Games", arXiv:1407.5030v4 (14 Jul 2015), pdf sha256 c2587986…, cited [BGHM]. Used: §3 Algorithm 1 and the
operator F (x_i = Val^{≤i}, i-step min-cost-reachability value), Theorem 1 item 4 (values in O(|V|²|E|W) time; O(|V|²W) iterations,
"(2|V| − 1)W|V| + |V| steps" in the text after Algorithm 1), and the Figure 2(a) example (a 3-vertex game needing 2W iterations).
### 7.1 The terminal game Γ_c and Lemma VI-LB (PROVED, every game)
- Γ_c (per phase, c ∈ C): vertices U_c; Even vertices maximise, ALL Odd vertices (choice or not) minimise, over successors inside
  U_c; target c (value (0, 0)); a play's payoff is κwt_c summed along it until c; a play that never reaches c is −∞ (worst for Even).
  Integer form (order-preserving, since |Σ s_c| ≤ |U_c| < 2n + 1): ω(v) := (2n + 1)·wt_c(v) + s_c. Up to negation (Even ↦ Min,
  Odd ↦ Max, κ ↦ −κ) this is [BGHM]'s min-cost reachability game with target c, and its j-step values Val^{≤j}_c are the mirrored
  iterates x_j of [BGHM] Algorithm 1 (x_0 = −∞ off c).
- Lemma VI-LB. For every j ≥ 0, every state t of the phase with t > g_j and every z ∈ U_c: κ_t(z) ≥ Val^{≤j}_c(z).
  Proof by induction on j. j = 0: Val^{≤0} is −∞ off c, and κ_t(c) = (0, 0). Step: z = c trivial. Even z ≠ c: κ-FB-ROUND at g_j gives
  κ_{g_j+1}(z) ≥ κwt_c(z) + κ_{g_j}(x) for every successor x ∈ U_c, the hypothesis at g_j (> g_{j−1}) gives κ_{g_j}(x) ≥ Val^{≤j−1}(x),
  and (M2κ) carries it to t; take the max over x. Odd z ≠ c: (Aκ) gives κ_t(z) = κwt_c(z) + κ_t(σ̄_t z) with σ̄_t(z) ∈ U_c, so
  κ_t(z) ≥ κwt_c(z) + min_{x ∈ succ(z) ∩ U_c} κ_t(x) ≥ κwt_c(z) + min_x Val^{≤j−1}(x) (hypothesis at t > g_{j−1}). ∎
- This is the two-player form of κ-HAT-FREEZE (a): HAT-FREEZE used only Odd vertices outside Q (forced), i.e. the one-player relaxation
  of Γ_c with the Odd choice vertices removed; VI-LB keeps them as minimisers. So each in-phase fallback is (at least) one round of
  [BGHM]'s value iteration on every Γ_c simultaneously.
### 7.2 What the known bound gives (READING, with the source)
- If VI on Γ_c stabilised after R_c rounds AND the honest values were bounded above by the stable value (κ_t ≤ Val_c), then a FREEZE-EXIT
  argument would give: after max_c R_c fallbacks no S-switching fallback, so f ≤ 1 + max_c R_c + (CN-ONLY). The upper bound is OPEN: Γ_c
  lets Odd avoid c (payoff −∞ for Even), which in G means another cycle node, not a lower κ; so κ_t ≤ Val_c is not implied by Lemma S (a).
- Even granting it, [BGHM] Theorem 1 (4) bounds R_c by O(|U_c|²·W) with W = max |ω| ≈ (2n + 1)·2^{rank range above c}: EXPONENTIAL in
  n, not polynomial. No polynomial VI bound for min-cost reachability / total-payoff games with arbitrary integer weights is known to me;
  [BGHM] call theirs "the first pseudo-polynomial time algorithm" for total-payoff games (abstract). So the cross-field route gives
  pseudo-polynomial = exponential here, unless the weights are polynomial (ranks above c in U_c spanning O(log n) levels).
### 7.3 The obstruction, instance-style (OPEN; no N5 instance)
- [BGHM] Figure 2(a): v1 (Max) → v3 (target) weight −W, v1 → v2 weight −1, v2 (Min) → v1 or → v3; VI needs 2W rounds because Min
  gains −1 per loop. Mirrored into Γ_c: an Even vertex v2 and an Odd choice vertex v1 on a 2-cycle inside U_c, with a low even-rank
  vertex (rank r) on the cycle and an exit from v1 to c through a high even-rank vertex (rank R > r). Val^{≤j} rises by about 2^r per two
  rounds.
- In N5 the honest values are values of SIMPLE paths ((SP′)), so κ_t ≤ the simple-path ceiling K_c (< 2^{R+1} in the wt component).
  Lemma VI-LB then forces the phase to have fewer than j fallbacks once Val^{≤j}_c exceeds K_c somewhere. On the gadget that happens after
  about 2^{R+1−r} rounds: the cycle is cut off, but only after an exponential number of rounds when R − r is large. So neither direction
  closes: VI-LB gives no polynomial count on such gadgets, and nothing shows N5 performs one fallback per VI round there.
- What a counterexample to ρ-POLY / to a polynomial fallback count would need: a phase whose fallbacks track the VI iterates of such a
  gadget (each fallback raising the honest value at v2 by one cycle increment, without changing λ). OPEN; and the late regime (≥ n
  fallbacks in a phase) is vacuous in all data (§4, §6.4), so no data speak to it.
- Verdict for (b): no known polynomial value-iteration bound applies (the opened one is pseudo-polynomial, exponential with 2^rank
  weights); VI-LB (PROVED) makes each fallback a VI round on Γ_c; the freeze at the VI fixed point (κ_t ≤ Val_c) is OPEN.

## 8. The converse side: why N5 can beat value iteration (Lead 03:07Z; written 03:13Z by date -u)
### 8.1 (i) Is a fallback (plus the S4a block after it) a strategy-improvement step?
- On G, in the honest frame: YES, exactly (PROVED, from the SPEC). Ξ_k is σ_k's valuation against Odd's best response σ̄_k (S1). S4c
  switches EVERY Even vertex with an improving edge (S2: strictly better Ξ_k-value than its current successor) to the improving successor
  of best (Ξ_k, index) key. That is one switch-all, best-improvement ("greedy all-switches") step of Vöge-Jurdziński strategy
  improvement for Even on G, R15 (a) gives its monotonicity. The S4a steps in between are further improvements (each switches along gate
  edges; R15 (a)), computed as Even's one-player optimum against the fixed τ (R18 (d) Lemma S (c), "⇒" form), not against σ̄.
- On Γ_c: NOT literally. Γ_c's minimiser may avoid c (payoff −∞ for Even), so Odd's best response in Γ_c can differ from σ̄_k, which
  is Odd's best response in G (avoiding c there means another cycle node, which σ̄_k rejected). Γ_c is a lower-bound device (VI-LB),
  not a model of N5's dynamics.
### 8.2 (ii) What is known about SI vs VI on these games (source opened: [BGHM], arXiv:1407.5030v4)
- [BGHM] §1: for total-payoff games "the best algorithm to compute the values runs in exponential time [9], and consists in iteratively
  improving strategies" ([9] = Gawlitza-Seidl, not opened by me); [BGHM] give the first pseudo-polynomial algorithm, by value iteration.
- [BGHM] appendix (the comparison with Björklund-Vorobyov's longest-shortest-path problem, printed pp. 16-17): the strategy iteration
  algorithm of [1] (Björklund-Vorobyov, not opened by me) needs 2^n iterations on "the LSP instance presented in Fig. 2 of [1], with
  2n + 1 vertices but a biggest weight W exponential in n", which their value iteration solves in time linear in n; conversely
  [BGHM] Figure 2(a) needs 2W VI iterations.
- READING: neither paradigm dominates on min-cost reachability / total-payoff games; both have exponential worst cases with exponential
  weights. No polynomial bound for either is known to me with 2^rank weights.
### 8.3 (iii) Lemma ACCEL (PROVED, every game): N5's switches are paid by simple-path value levels, not by VI rounds
For c ∈ C and z ∈ U_c let K_c(z) := {κwt_c(p ∖ {c}) : p a simple path of G[U_c] from z to c} (all edges of G inside U_c; Odd choice
vertices included). Then in every phase:
- (a) κ_t(z) ∈ K_c(z) at every state t, for every z ∈ U_c;
- (b) the in-phase transitions at which some Even vertex z with λ(z) ≠ z switches number at most N_K := Σ_{c} Σ_{Even z ∈ U_c ∖ {c}}
  (|K_c(z)| − 1);
- (c) f ≤ 1 + N_K.
Proof. (a) z's honest play up to c is a simple path of G[U_c] ((SP′), via (Aκ) it stays in U_c), and (Aκ) along it gives κ_t(z) =
κwt_c(path ∖ {c}). (b) At an in-phase transition L → L+1, a switched Even y with λ_L(y) ≠ y gains strictly: Ξ_{L+1}(y) ▷ Ξ_L(y)
(RESULTS R19 (d), key step (SG), signed "on all games, not only 𝒞^1O"; the switch is along a gate edge at S4a and at S4c). With (M1κ),
κ_{L+1}(y) > κ_L(y). By (M2κ) κ(y) never decreases in the phase, and by (a) it moves in the finite set K_c(y); so y switches at ≤
|K_c(y)| − 1 transitions; charge each transition to one such y. (c) A fallback with S = ∅ is at most one (CN-ONLY_D, P-N5-FBRED §2);
a fallback with S ≠ ∅ switches an Even y ∉ T, so λ(y) ≠ y (y ∉ C), and is counted in (b). ∎
- The gadget collapses (PROVED as an instance of (b)): in the mirrored [BGHM] Figure 2(a) gadget (§7.3), an Even vertex v2 and an Odd
  vertex v1 on a 2-cycle with exits, each of v1, v2 has ≤ 2 simple paths to c through the gadget, so |K(v)| ≤ 2 for the gadget's own
  choices, and v2 switches at most once per phase. VI-LB's iterates climb by walking the 2-cycle repeatedly; N5's values never do (a
  repeated cycle would be an honest cycle without c, i.e. a λ-change). So the 2^{R+1−r} VI rounds are not N5 rounds: N5's escape
  mechanism is POSITIONAL values (simple paths) plus STRICT gain at every non-cycle-node switch. This answers L-RED's routed target in
  the negative for the bare gadget (READING; L-RED may test it).
- What ACCEL does NOT give: a polynomial bound. |K_c(z)| can be exponential (distinct subsets of high-rank vertices on simple paths).
  ACCEL is the honest-frame analogue of "SI terminates after at most #valuations steps"; it bounds switching transitions by value
  levels, not by n^O(1). Transitions that switch only cycle nodes are not counted by (b).
- The obstruction that remains (OPEN, instance-style): a phase in which some vertex's honest value climbs MONOTONICALLY through
  exponentially many simple-path values of U_c, one or a few per transition, without λ or τ changing. That is a binary-counter
  structure inside ONE phase (Friedmann's lower bounds for strategy improvement count across many λ-phases; N5 is about linear on his
  families, N5-MULTI §4.5, DATA). VI-type gadgets (cycle accumulation) cannot produce it, by ACCEL (a).
### 8.4 DATA (experiments/new/box44/sgcheck.py; canonical S3 start)
| sample | in-phase transitions | (SG) checks / viol. | max switching transitions in one phase | max distinct κ-values of one vertex in one phase |
| --- | --- | --- | --- | --- |
| lib41 (412 runs) | 6,554 | 12,653 / 0 | 112 | 52 |
| box43 + box44 instances (10) | 105 | 263 / 0 | 44 | 17 |
| `--rand 2000 5 20 71` | 382 | 430 / 0 | 3 | 3 |
Reading (DATA): the per-vertex value levels actually used in a phase stay small (≤ 52 on lib41, games up to n 492); nothing in the data
approaches an exponential climb inside one phase.

## 9. The one-phase counter question (Lead 03:26Z; route (a); written 03:28Z by date -u)
Question: inside one phase, can κ_t(z) pass through more than poly(n) simple-path levels? Route (a), structural. The Lead's
cross-field reading, "N5's in-phase dynamics on G_τ is one-player SI; super-polynomial behaviour must come from σ̄ changing at Q", is
formalised here by epochs.
### 9.1 Lemma EPOCH (PROVED, every game)
An EPOCH of a phase: a maximal run E of consecutive states of the phase on which σ̄_t|Q is constant (then σ̄_t is constant on E: Odd
vertices outside Q have one successor). Let G_E := G with every Odd vertex fixed to σ̄_E (a one-player game), and for z ∈ U_c let
opt_E(z) := max{κwt_c(p ∖ {c}) : p a simple path of G_E[U_c] from z to c}. Let e_1 < e_2 < … be the in-phase fallbacks k → k+1 with
k ∈ E. Then:
- (a) (freeze) for every state t ∈ E with t > e_j and every z ∈ U_c: κ_t(z) ≥ max{κwt_c(p ∖ {c}) : p a simple path of G_E[U_c] from z
  to c with ≤ j edges}; hence for t ∈ E with t > e_{n−1}, κ_t = opt_E on every class (Ξ is frozen on all of V).
- (b) (no switch after the freeze) no transition t → t+1 with t, t+1 ∈ E and t > e_{n−1} switches an Even vertex z with λ(z) ≠ z; and the
  part of E after e_{n−1} has at most 4n(n − 1) + 1 transitions.
- (c) (count) the phase has f ≤ 1 + n·N_ep in-phase fallbacks, N_ep := its number of epochs.
Proof.
- (a) Induction on j (as κ-HAT-FREEZE (a), with every Odd vertex forced to σ̄_E). j = 0: the path is (c); κ_t(c) = (0, 0). Step: p = z·p′,
  p′ from x with ≤ j − 1 edges. Odd z: on E, next_t(z) = σ̄_E(z) = x, and (Aκ) with the hypothesis at t gives κ_t(z) ≥ κwt_c(z) +
  κwt_c(p′ ∖ {c}). Even z: k := e_j < t, k ∈ E, k > e_{j−1}; κ-FB-ROUND at k gives κ_{k+1}(z) ≥ κwt_c(z) + κ_k(x), the hypothesis at k gives
  κ_k(x) ≥ κwt_c(p′ ∖ {c}), and (M2κ) carries κ_{k+1}(z) to t. For the equality: z's honest play at t ∈ E is a simple path of G_E[U_c]
  to c ((SP′); Even edges σ_t, Odd edges σ̄_E), so κ_t(z) ≤ opt_E(z); simple paths in U_c have ≤ |U_c| − 1 ≤ n − 1 edges.
- (b) If such a z switched, (SG) (R19 (d), every game) would give κ_{t+1}(z) > κ_t(z) = opt_E(z) ≥ κ_{t+1}(z) (the latter by (a)'s upper
  bound at t + 1 ∈ E): impossible. After e_{n−1}, every transition with both ends in E leaves Ξ = Ω_σ unchanged (a), and Ω_τ is constant
  (τ is constant on a phase); RESULTS R15 (d): at most 4n(n − 1) consecutive iterations leave both unchanged. Add the transition that
  leaves E.
- (c) In each epoch: at most n − 1 fallbacks e_1..e_{n−1}; after e_{n−1}, a fallback with both ends in E switches only cycle nodes ((b)),
  so S = ∅ and it is the phase's one CN-ONLY_D fallback; and at most one fallback is E's last transition. So f ≤ Σ_E ((n − 1) + 1) + 1.
  ∎
- What EPOCH gives: FREEZE-type collapse inside every epoch, from the one-player structure alone (R17-style, Bellman rounds = fallbacks).
  Every super-polynomial count of fallbacks in a phase needs super-polynomially many epochs, i.e. σ̄|Q changing that often (the
  Lead's "moves only at Q", made exact for f). Compared with FB-RED (f ≤ 1 + (n − 1)(2 + ρ)), EPOCH counts σ̄-changes instead of
  Ξ-changes at Q; neither dominates (a Ξ(q)-change need not change σ̄(q), and σ̄(q) can change at a tie without a Ξ(q)-change).
- What EPOCH does NOT give: the S4a steps of an epoch BEFORE its freeze (between e_j and e_{j+1}) are not counted; nor N_ep.
### 9.2 Can N_ep be bounded by ∏ deg(q) (no repeated σ̄|Q in a phase)? NO (DATA, instance)
For τ, Corollary Φ-kO uses "no τ repeats along a run" (R15 on G^d). The analogue for σ̄|Q inside a phase FAILS:
- Instance experiments/new/box25/laps/lap_n6_s1_110421.pg (n 6, 𝒞^1O with Q = {2}, sha1 4f4fe69c51e1c6f170c9c732feca025da70e7edb):
  N5 from S3: 2 iterations, both in one phase (λ ≡ 5, τ(2) = 0 throughout); σ̄_t(2) = 0, 4, 0 at states 0, 1, 2 (no fallback). A repeat.
- lib41: 91 phases with a repeated σ̄|Q (87 of them on 𝒞^1O, |Q| = 1); up to 36 repeats and 50 epochs in one phase
  (experiments/si/orlens/instances/lev_l_x.pg, n 32, |Q| = 1).
- So N_ep is not bounded by the number of σ̄|Q configurations; on 𝒞^1O it is polynomial only because the whole phase is (RESULTS R51).
  Obstruction for a fixed-k bound by this route: Odd's best response at q alternates between successors as their values rise in turn
  (min over increasing values), which no potential on σ̄|Q forbids.
### 9.3 The answer to the question, as far as it goes
- PROVED: inside an epoch, after n − 1 fallbacks the honest values are frozen (EPOCH (a)); so a vertex's levels inside a phase are visited
  only (i) at transitions before its epoch's freeze, or (ii) at epoch boundaries. Levels per vertex per phase ≤ Σ_E (1 + number of
  switching transitions of E before e_{n−1}) (ACCEL's strict gains, restricted to epochs).
- OPEN: (i) needs a bound on S4a runs between fallbacks inside an epoch (gated W-optimal steps; the 𝒞^1O version of this is what R50 /
  R51 needed T*-type machinery for); (ii) needs a bound on N_ep, which the ∏deg route cannot give (§9.2).
- Route (b) (a counter) is not attempted here: by EPOCH, a one-phase counter must either flip σ̄|Q super-polynomially often inside the
  phase or run long S4a stretches before epoch freezes. That is the instance shape for L-RED's climb (objective: N_ep per phase, or the
  longest pre-freeze S4a run).
### 9.4 DATA (experiments/new/box44/epoch.py; canonical S3 start)
| sample | phases | max N_ep (n) | phases with a σ̄|Q repeat / max repeats | EPOCH (c) viol. | epochs reaching n − 1 fallbacks | longest S4a run in an epoch | max levels of one vertex in a phase |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lib41 (412 runs) | 2,335 | 50 (n 32) | 91 / 36 | 0 | 0 | 55 | 52 |
| box43 + box44 instances (10) | 59 | 17 (n 44) | 2 / 7 | 0 | 0 | 7 | 17 |
| `--rand 2000 5 20 81` | 4,610 | 2 | 0 / 0 | 0 | 0 | 3 | 3 |
Reading (DATA): EPOCH (a)/(b) are vacuous in the data (no epoch reaches n − 1 fallbacks); EPOCH (c) holds everywhere. Epochs and σ̄
repeats are frequent on 𝒞^1O, where N5 is polynomial anyway (R51).

## 10. (3) A potential for N_ep (Lead 03:39Z; written 03:47Z by date -u)
### 10.1 Lemma ALT (PROVED, every game): Odd's alternations raise Ξ at q, except at ties and in two named cases
Let t → t+1 be an in-phase transition, q ∈ Q ∩ U_c with q ≠ c, and σ̄_{t+1}(q) ≠ σ̄_t(q) =: y1, y2 := σ̄_{t+1}(q). Call the change CLEAN if
q lies on no honest cycle at t and at t+1 (H1_q at both) and y2's honest play at t avoids q. Then for a CLEAN change:
κ_{t+1}(q) ≥ κ_t(q), with equality only if κ_t(y2) = κ_t(y1) and κ_{t+1}(y2) = κ_t(y2) (a TIE at t).
Proof. κ-Y-FORM_D (P-N5-FBRED §1.2) at t + 1 (H1_q): κ_{t+1}(q) = κwt_c(q) + κ_{t+1}(y2), y2 ∈ U_c. (M2κ): κ_{t+1}(y2) ≥ κ_t(y2). y2 ∈ Y^q_t
(clean), so κ-Y-FORM_D at t (H1_q) gives κ_t(y2) ≥ min_{Y^q_t} κ_t = κ_t(y1) = κ_t(q) − κwt_c(q). Equality throughout is the tie. ∎
Corollary. N_ep ≤ 1 + Σ_{q ∈ Q} (ρ_q + tie_q + nc_q + cyc_q), where per phase ρ_q counts transitions changing Ξ(q), tie_q the clean ties,
nc_q the non-clean changes, cyc_q the changes at q with λ(q) = q (an epoch ends only at a transition where some σ̄(q), q ∈ Q, changes).
### 10.2 The three candidate potentials (the Lead's list), evaluated
- (Ξ on the successors of Q, lexicographic): non-decreasing (R15 (a)), so it is a potential, but its number of values is the product of
  the successors' level counts; nothing smaller follows. An alternation y1 → y2 → y1 at q needs κ(y1) to rise past κ(y2) and then κ(y2)
  past κ(y1): two non-decreasing sequences with values in finite sets K, K′ cross at most |K| + |K′| − 2 times, and no better bound
  follows from monotonicity alone. MONO plus positional simple-path values give exactly that, i.e. crossings ≤ levels (ACCEL (a)); they do
  NOT give "each ordered pair swaps at most once per phase" (READING; no proof, and lap_n6_s1_110421 has a swap and a swap back in one
  phase). "At most once per epoch" is true but empty: a swap of σ̄(q) ends the epoch by definition.
- (R15's potential on G_σ's Odd side): R15's (Ω, φ) potential orders strategies of the IMPROVING player; σ̄_t is Odd's best response to
  σ_t, not an improving sequence of Odd's, and Odd's own valuation Ω_τ is constant on a phase (τ fixed). There is no Odd-side quantity
  that the SPEC makes monotone besides L_σ = Ξ itself (R18 (d) Lemma S (b): L non-decreasing). So this candidate reduces to the next.
- (honest values at Q, which change only through Even switches): this is the one that works, and ALT makes it exact: up to ties and the
  two non-clean cases, every alternation is a strict rise of Ξ(q). So N_ep is ρ (FB-RED's quantity) plus residuals.
### 10.3 Verdict on (3)
- PROVED: N_ep ≤ 1 + ρ + (ties) + (non-clean) + (cycle-node changes) (ALT). So EPOCH (c) and FB-RED count the same thing, honest-value
  changes at Odd choice vertices inside a phase; there is no independent potential for Odd's alternations.
- OPEN: ρ (Ξ-levels at Q per phase), and the residuals (ties: a potential on the S1 tie-break, unlikely to be the obstruction; non-clean:
  q joining or leaving c's honest cycle, or y2 routed through q at t).
- So the one-phase counter question reduces, by ACCEL + EPOCH + ALT, to: can Ξ(q), q ∈ Q, take super-polynomially many values in one
  phase? (= ρ-POLY, §6.)
### 10.4 DATA (experiments/new/box44/altcheck.py; canonical S3 start)
| sample | σ̄(q) changes in-phase | CLEAN: strict / tie | NONCLEAN: ¬H1_q / y2 through q | λ(q) = q | ALT viol. |
| --- | --- | --- | --- | --- | --- |
| lib41 (412 runs) | 2,051 | 1,910 / 75 | 9 / 56 | 1 | 0 |
| box43 + box44 instances + lap_n6 (11) | 36 | 35 / 1 | 0 / 0 | 0 | 0 |
| `--rand 2000 5 20 91` | 33 | 24 / 2 | 4 / 1 | 2 | 0 |
Reading (DATA): 93% of Odd's in-phase alternations strictly raise Ξ(q); ties and non-clean changes are a few percent.

## 11. FB-2T for any number of terminals per class (Lead 04:04Z; after L-SI 11's docs/si/N5-2O-box16.md at l-si 67fd31d9, read-only; written 04:07Z by date -u)
Notation as L-SI's note §0 (= FBRED §0): Q_c := (Q ∩ U_c) ∖ {c}, m_c := |Q_c|, w_c := |U_c| − 1, d_q := |succ(q) ∩ U_c|, DIRECT, A_q (|A_q| ≤
d_q + w_c), PFZ-q (q-runs), DIR (L-SI §3, PROVED there). Late fallbacks i = 1, 2, … with source states k_1 < k_2 < … (index j ≥ n);
x_i(q) := κ_{k_i}(q). Conditional on P-N5-FBRED (its late form, κ-HAT-FREEZE_D (a), κ-FB-ROUND), as L-SI's note is. All labels PROVED =
L-NEW 23, unrefereed; L-SI's lemmas are cited from its lane note (unrefereed).
### 11.1 Lemma ROUTE-k (PROVED, every game)
At every state t of a phase and in every class, let par_t(q) := the first vertex of Q_c ∖ {q} on q's honest play before c, for q ∈ Q_c not
direct (par_t(q) undefined if q is direct). Then the relation q → par_t(q) has no cycle; so every chain ends at a direct terminal, and the
DEPTH of q (the length of its chain) is ≤ m_c − 1.
Proof. If q → par(q) = p, q's play from its visit of p on is p's play (positional). A chain q = p_0 → p_1 → … → p_r = q would put p_1, …,
p_r on q's play in this order, so q's play would revisit q; then q lies on its own play's cycle, whose top is c, and q's play visits c
before revisiting q only if c precedes p_1, against "p_1 before c". So q is on its own honest cycle, which makes q direct: contradiction. □
(L-SI's ROUTE-2 is the case m_c = 2.)
### 11.2 Lemma SAT-k (PROVED, every game)
Let t > g_{w_c} be a state, q ∈ Q_c not direct at t, p := par_t(q), Θ_p the p-run containing t, and t > f^{Θ_p}_{w_c}. Then
κ_t(q) ∈ S_{q,p} + κ_t(p), with S_{q,p} := {κwt_c(q) + κopt^p(y) : y ∈ succ(q) ∩ U_c ∖ T, κopt^p(y) defined} ∪ {κwt_c(q) : p ∈ succ(q)};
|S_{q,p}| ≤ d_q.
Proof. y := σ̄_t(q) = next_t(q) ∈ U_c, κ_t(q) = κwt_c(q) + κ_t(y) ((Aκ)); y's play is the rest of q's, so it avoids q and its first terminal
is p. If y = p, done. Otherwise y ∉ T (its first terminal is p, and y ≠ c because p comes before c). "≤": the prefix of y's play up to p is
a simple path ((SP′)) avoiding T ∖ {p}, with Even edges σ_t's and forced Odd vertices: a path of G_c^p, so κ_t(y) = κwt_c(prefix ∖ {p}) +
κ_t(p) ≤ κopt^p(y) + κ_t(p). "≥": PFZ-q (L-SI §1) at t > f^{Θ_p}_{w_c} (paths of G_c^p have ≤ w_c edges): κ_t(y) ≥ κopt^p(y) + κ_t(p). □
(It is L-SI's SAT-2 with the parent named by the actual route, which removes the max over targets.)
### 11.3 Theorem FB-kT (PROVED, every game; CONDITIONAL on P-N5-FBRED, like FB-2T)
In every phase, with D_c := max_{q ∈ Q_c} d_q + w_c (≤ 2n):
  N_late ≤ 1 + Σ_c Σ_{q ∈ Q_c} (V_q − 1), and V_q ≤ Σ_{h=0}^{m_c − 1} D_c·((m_c − 1)·D_c)^h ≤ m_c·D_c·((m_c − 1)·D_c)^{m_c − 1},
where V_q := the number of distinct values x_i(q) over the late fallbacks. Hence f ≤ 1 + (n − 1)(1 + N_late) (FBRED late form) is
POLYNOMIAL whenever every class has a bounded number of terminals; on 𝒞^kO (k fixed, so m_c ≤ k): N_late ≤ 1 + k²·(2n)·(2(k − 1)n)^{k−1}
= O(n^k) and f = O(n^{k+1}) per phase. (k = 2 gives O(n³), L-SI's FB-2O, with a different constant.)
Proof.
1. (Outer sum.) Two late fallbacks lie in one Q-run iff their tuples x are equal (L-SI FB-2T step 1, (M2κ)). The tuple sequence is
   coordinatewise non-decreasing, so each change of tuple raises at least one coordinate to a value it never had before; hence
   #distinct tuples ≤ 1 + Σ_q (V_q − 1).
2. (Values by depth.) Let V_{q,h} := #distinct x_i(q) over the indices i at which q has depth h (at k_i).
   - h = 0 (q direct at k_i; k_i > g_{n−1} ≥ g_{w_c}): x_i(q) ∈ A_q by DIR; V_{q,0} ≤ |A_q| ≤ D_c.
   - h ≥ 1: let p := par_{k_i}(q), of depth h − 1 at k_i. Group the indices by (p, α := x_i(p)). For fixed p, the indices with x(p) = α are
     consecutive (monotone) and their source states lie in one p-run Θ (equal values with (M2κ) force constancy in between); every
     index of the group after the first w_c indices WITH x(p) = α has k_i > f^Θ_{w_c} (those earlier indices are fallbacks of Θ with
     earlier source states), so SAT-k gives x_i(q) ∈ S_{q,p} + α. So the group contributes ≤ w_c + d_q ≤ D_c values. The α's that occur
     are values of x(p) at indices where p has depth h − 1, at most V_{p,h−1} of them. So V_{q,h} ≤ Σ_{p ∈ Q_c ∖ {q}} D_c·V_{p,h−1}.
   - Induction: V_{·,h} ≤ D_c·((m_c − 1)·D_c)^h (max over terminals), and h ≤ m_c − 1 (ROUTE-k).
3. V_q ≤ Σ_h V_{q,h}; combine with 1 and FBRED's late form. □
### 11.4 Why this is nested, and what a SUM bound would need (READING + model obstruction)
- The nesting is in step 2: per value α of the parent, the child may take up to d_q values (one per shift in S_{q,p}). Step 1 already sums
  over terminals; only the per-terminal value count V_q is a product over depth.
- MODEL OBSTRUCTION (PROVED as a statement about the lemmas, not about N5): the constraints used (ROUTE-k, DIR, SAT-k, (M2κ), the
  w_c-saturation rule) are satisfied by abstract tuple sequences with ∏ over a chain of d_q·|A_root| distinct values: take a chain q_1 (direct,
  values α_1 < … < α_a in A) ← q_2 ← … ← q_h with shift sets S_r = {s_{r,1} < … < s_{r,d}} spread so that s_{r,d} + (any value of the parent)
  < s_{r,1} + (the parent's next value); list the tuples lexicographically (parent value first, then shifts), w_c filler indices per new
  parent value; every coordinate is non-decreasing and every saturated index satisfies SAT-k. So NO sum bound follows from these lemmas
  alone; a sum bound must use more of N5. The candidate extra ingredient (OPEN): Odd's MIN at q (κ-Y-FORM_D) together with saturation —
  with the parent's value fixed and saturated, the shift s = κwt(q) + κopt^p(σ̄(q)) can rise only if Odd's argmin y changes, and the
  successors routed through p have FROZEN values κopt^p(y) + α; so inside an α-block, x(q) can change only when a successor of q changes
  its route (an Even switch on y's play, moving its first terminal). If each successor changed its first terminal O(1) times per block,
  the per-block count would be O(d_q) but the product would remain; a sum needs "x(q) changes only when x(par) changes", i.e. no
  in-block rises, which the model shows is not implied. OPEN; no N5 instance either way.
- DATA: none new. The late regime (j ≥ n) is vacuous in every sample and climb (FBRED fixes N-FBRED-4: max f − n = −2 / −4); FB-kT, like
  FB-2T and FB-RED's late form, rests on its proof. ROUTE-k is statewise and could be checked; not run.
### 11.5 With the phase count (READING)
On 𝒞^kO (k fixed): phases ≤ n(n − 1) + ∏ deg(q) ≤ n(n − 1) + n^k (RESULTS R54 (e) Φ-kO), f = O(n^{k+1}) per phase (FB-kT, conditional on
FBRED), so in-phase fallbacks over a run are O(n^{2k+1}). Still missing for N5 polynomial on 𝒞^kO, k ≥ 2 (each OPEN): (i) crossings per
phase (R30 (c) / R34 (f) on 𝒞^1O; needs R-STICK in set form, L-SI §5); (ii) transitions per phase given f (R50 (h) on 𝒞^1O; blocked on the
frontier at LEN / Δ-RT, N5-DELTA-box44 §8, L-SI N5-FRONTIER-box15 §3); (iii) BIT and OUT beyond 𝒞^1O (R51's Lemmas BIT, OUT; OUT's proof
is game-general per REFEREE §C on DUAL, BIT is game-free) — READING.

## 12. Crossings per phase in set form: R-STICK_D (Lead 04:19Z; written 04:30Z by date -u)
Setting: R55 (P-N5-GD, landed): D_k, R_D(k) (vertices whose (σ_k, τ_k)-play meets D_k), F_D := V ∖ R_D, W_k (σ_k's valuation in G_τ),
G_D (a) (Ξ = W on F_D, no hypothesis). λ := the honest cycle-node map (constant on a phase), λ_W := W's. A vertex v is SPLIT at k if
λ_W(v) ≠ λ(v), UNSPLIT otherwise. A CROSSING is an in-phase transition with R_D(s) ≠ R_D(s+1) (D may change too). Landed premises: R21 (a)
XW (Ξ_k ⊴ W_k; game-general per the referees' premise-class confirmation on R55/R56); R23 (g) WM (W_{k+1} ⊵ W_k at an in-phase non-fallback
transition; its proof is σ_k ∈ its own S4a arena + R17 (F1) on G_τ, game-general); injective rewards (S1).
### 12.1 Lemma R-STICK_D (PROVED, every game)
At an in-phase S4a transition s → s+1, every split v ∈ R_D(s) lies in R_D(s+1) (whatever D_{s+1} is).
Proof (R30 (c)'s, verbatim in set form). Suppose v ∈ R_D(s) ∩ F_D(s+1); c := λ(v), c′ := λ_{W,s}(v) ≠ c. G_D (a) at s+1: W_{s+1}(v) =
Ξ_{s+1}(v), cycle node c (phase). WM: W_{s+1}(v) ⊵ W_s(v); the cycle nodes differ, so rew(c) > rew(c′). XW at s: Ξ_s(v) ⊴ W_s(v), cycle
nodes c and c′, so rew(c) < rew(c′). Contradiction. □
One-Odd uses in R30 (c) and replacements: R19 (a) "off R, Ξ = W" → G_D (a) (R55); "v ∈ R_s has W-cycle node c_w(s) and λ(v) = c_θ" (HP: all
of R routes through o) → dropped: the statement is per vertex. Nothing else.
### 12.2 Corollary SN-PREFIX_D (PROVED, every game)
- (a) Along a run of consecutive in-phase S4a transitions, for each vertex v the states at which v is unsplit form a prefix of the run.
  Proof: WM makes W(v) non-decreasing, so rew(λ_W(v)) is non-decreasing (cycle nodes compare by reward first); XW gives rew(λ_W(v)) ≥
  rew(λ(v)) with equality iff λ_W(v) = λ(v); λ(v) is constant. So once split, v stays split for the rest of the run. □
- (b) In such a run, after its unsplit prefix a vertex v changes its R_D-membership at most once (it may enter, it cannot leave: R-STICK_D).
- (c) Per phase: X_D ≤ (f + 1)·n + f + X_SN^D, where X_D := crossings, f := in-phase fallbacks, and X_SN^D := crossings at which some
  vertex that is UNSPLIT at the source state changes membership. Proof: split the phase at its fallbacks into ≤ f + 1 S4a runs; a
  crossing inside a run at which every membership-changing vertex is split moves only split vertices, each of which (by (a), (b)) does so
  at most once per run, so ≤ n such crossings per run; the f fallback transitions are counted separately. □
- On 𝒞^1O this is R30 (c) with "c_w = c_θ" (a property of o, shared by all of R) replaced by "v unsplit" (per vertex), and (n − 1) by n
  (o ∈ R always on 𝒞^1O).
### 12.3 X_SN^D: what the 𝒞^1O chain used and what replaces it
On 𝒞^1O, X_SN is bounded by R34 (f) X-SN-PHASE, via R33 (g) X-RUN′ ⇐ R32 (e) X-RUN ⇐ R32 (c)-(d) (P^c_ℓ, FREEZE: COARSE_{ℓ−1}(θ) takes
≤ 2d_o values) and R34 (d)-(e) TOGGLE / TOGGLE-COUNT. Step by step (ledger docs/new/N5-MULTI-ledger-box43.md rows R32-R34, re-read):
| 𝒞^1O step | one-Odd use | set-form status |
| --- | --- | --- |
| R32 (c) P^c_ℓ (coarse R17 with COARSE_ℓ) | R20 Lemma C (RT: one route terminal) | REPLACED by CR_D (docs/new/N5-DELTA-box44.md §3: coarse freeze on any L-run under (h_D) ∧ (h3_D); = L-SI's CR-D′); PROVED, unrefereed |
| R32 (d) FREEZE / RATCHET / BLOCK | "COARSE_{ℓ−1}(θ) takes ≤ 2d_o values" at the single o | per terminal: ≤ 2d_u values of COARSE(Ξ(u)) per u ∈ D, if the per-o argument ports (it uses θ = Ξ(o) only); NOT CHECKED; and |D_k| moves inside a phase (Δ1, OPEN) |
| R32 (e) X-RUN | via FREEZE + ABS-COUNT′ (absorptions at o, R30 (f)) | absorptions at each u ∈ D: per-terminal index (I); not written |
| R33 (b) H2-STICK, (e) R-CONST | HP ("honest play agrees with the (σ, τ)-play up to o") | (HP_D) holds by definition off D_k; but R-CONST ("at every ¬H1 state R̄ = U") is a one-terminal identity: FAILS in set form (several terminals, regions of different terminals) |
| R33 (c) Lemma G′ | FO ("Odd vertices other than o are forced") | FAILS (ledger F) |
| R34 (b) L-MONO | case split assumes the cycle node c is Even or forced | FAILS for an Odd-choice cycle node (ledger U) |
| R34 (d) TOGGLE | FO: "Odd vertices other than o have one successor and c ≠ o, so c ∈ V_E" | FAILS: see the instance below |
| R34 (f) X-SN-PHASE | via X-RUN′ and TOGGLE-COUNT | FI |
- Obstruction, instance-style (DATA): experiments/new/box44/instances/qc_toggle.pg (n 5, Q = {0, 2, 3, 4}, sha1 27850ecc3d9e660aefa6a3401d6af0cfc2b3317c;
  N5 output verified by Oink verify). N5 from S3: one S4a transition, one phase; every vertex has honest cycle node 4, and 4 is an ODD
  CHOICE vertex (4 → 0, 3); D = {0}; vertex 1 is unsplit (λ_W = λ = 4) and ENTERS R_D at the transition (σ(1): 2 → 0). So an X_SN^D
  crossing occurs in a class whose cycle node is an Odd choice vertex: exactly the configuration that TOGGLE's "c ∈ V_E" and L-MONO's
  case split exclude on 𝒞^1O. (This is a configuration instance, not a counterexample to any bound: the phase has one crossing.)
- Verdict (READING): crossings per phase in set form reduce, PROVED, to X_SN^D (crossings involving an unsplit vertex). X_SN^D is OPEN: the
  𝒞^1O bound's chain fails at G′, R-CONST, L-MONO and TOGGLE (one-Odd steps), and at Δ1 (D moves inside a phase). Ports that look
  available: P^c_ℓ → CR_D; FREEZE per terminal (unchecked).
### 12.4 DATA (experiments/new/box44/rstick.py; canonical S3 start)
| sample | phases | R-STICK_D checks / viol. | SN-PREFIX_D viol. | crossings X_D (max per phase) | X_SN^D share | Odd-choice cycle node at an X_SN^D crossing | X_D bound viol. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lib41 (412 runs) | 2,335 | 14,253 / 0 | 0 | 3,222 (99) | 3,102 | 6 | 0 |
| box43 + box44 instances (10) | 59 | 0 / 0 | 0 | 54 (27) | 54 | 0 | 0 |
| `--rand 2000 5 20 101` | 4,601 | 23 / 0 | 0 | 50 (2) | 50 | 9 | 0 |
Reading (DATA): nearly all crossings are X_SN^D (unsplit vertices), as on 𝒞^1O; post-prefix crossings are rare. The bound of 12.2 (c)
therefore moves almost nothing into proved territory in practice; the work is in X_SN^D.

## 13. X_SN^D with Odd-choice cycle nodes: charging to epochs (Lead 04:40Z; written 04:49Z by date -u)
### 13.1 Fact D-EPOCH (PROVED, every game)
On a phase, τ is constant, so D_s = {u ∈ Q : σ̄_s(u) ≠ τ(u)} changes only where σ̄|Q changes, i.e. only at epoch boundaries (P-N5-ACCEL §0).
On an epoch E, D and σ̄ are constant (in particular σ̄(c) is constant for an Odd-choice cycle node c); the honest frame is the one-player
game G_E and the W-frame the one-player game G_τ, and they differ exactly at the vertices of D.
- Consequence for TOGGLE's failure point (§12.3, qc_toggle.pg): the configuration "c ∈ Q, σ̄(c) moves" can change only at an epoch
  boundary; inside an epoch an Odd-choice cycle node behaves like a forced vertex (its honest edge is σ̄_E(c), fixed).
### 13.2 Lemma X-EP (PROVED, every game)
For every phase, with N_ep its epochs and f its in-phase fallbacks:
X_D ≤ (N_ep − 1) + N_ep·(n² + n + 4n(n − 1)) + Σ_E X_SN^pre(E),
where X_SN^pre(E) := the crossings with both ends in E, before E's (n − 1)-th fallback, at which some vertex unsplit at the source changes
R_D-membership. With ALT (P-N5-FBK §4): N_ep ≤ 1 + Σ_q (ρ_q + tie_q + nc_q + cyc_q).
Proof. Crossing transitions are of three kinds.
- At an epoch boundary (σ̄|Q changes): at most N_ep − 1.
- Inside an epoch E, after its (n − 1)-th fallback: by EPOCH (b) (P-N5-ACCEL §3) E has at most 4n(n − 1) + 1 transitions there.
- Inside E, before that: these lie in ≤ n − 1 fallback transitions and ≤ n runs of consecutive S4a transitions (split by those fallbacks).
  In each S4a run, a crossing at which every membership-changing vertex is split is counted by SN-PREFIX_D (b) (§12.2): each split
  vertex enters at most once and never leaves, so ≤ n such crossings per run; the rest are X_SN^pre(E).
Sum: (N_ep − 1) + Σ_E [(4n(n − 1) + 1) + (n − 1) + n·n + X_SN^pre(E)]. □
- So: crossings per phase = O(n²)·(1 + ρ + ties + non-clean + cycle-node changes) + Σ_E X_SN^pre(E). The epoch-boundary part, which is
  where Odd-choice cycle nodes act, is now charged to the same quantity as fallbacks (FB-RED's ρ, via ALT); that is the Lead's target
  shape for that part.
### 13.3 What is left: X_SN^pre (OPEN)
- X_SN^pre(E) lives inside one S4a run of one epoch: D, σ̄ and τ are all fixed, the two frames are two FIXED one-player games (G_E for Ξ,
  G_τ for W, differing on D), and N5's steps there are gated W-optima (S4a). Unsplit vertices (λ_W(v) = λ(v)) may leave and re-enter R_D.
- This is the same ground as "transitions per phase given f" (pre-freeze S4a runs; L-SI's item), restricted to crossings. On 𝒞^1O the
  corresponding count is the within-run part of R32 (e) X-RUN with σ̄(o) fixed. Its set form needs the route order between terminals (Δ-RT,
  N5-DELTA-box44 §8) when |D| ≥ 2; with |D| = 1 the R19-R20 machinery ports (N5-DELTA-box44 §7, PIECE_D, XA_D).
- No instance against a polynomial bound; in data the residual is the bulk (13.4).
### 13.4 DATA (experiments/new/box44/rstick.py, extended; canonical S3 start)
| sample | crossings | at epoch boundaries | inside epochs | of which after the epoch freeze | inside, pre-freeze, unsplit (X_SN^pre) |
| --- | --- | --- | --- | --- | --- |
| lib41 (412 runs) | 3,222 | 1,269 | 1,953 | 0 | 1,833 |
| box43 + box44 instances (11) | 55 | 18 | 37 | 0 | 37 |
| `--rand 2000 5 20 101` | 50 | 41 | 9 | 0 | 9 |
Reading (DATA): 39% of lib41's crossings are at epoch boundaries (now charged to N_ep); no epoch ever reaches its freeze; X_SN^pre is the
remaining bulk (57%).

## 14. DATA addendum: random start pairs (Lead 04:54Z, after L-SI's tcwult2_against_n8; run 04:58Z by date -u)
Every PROVED statement of this doc, N5-DELTA-box44 and the packets P-N5-ACCEL / P-N5-FBK is per phase and start-free; until now the lane's
checks used SPEC S3's start only. experiments/new/box44/randstarts.py re-runs rstick.py, altcheck.py, epoch.py, sgcheck.py, fbf.py, crd.py
with start pairs drawn uniformly from the successor lists.
| sample | violations of PROVED statements (R-STICK_D, SN-PREFIX_D, X-bound, ALT, EPOCH (c), (SG), CN-ONLY_D, EXIT-SWITCH_D, FREEZE-EXIT_D, FB-RED + late form, LAM_D, CR_D, C_D, FBL_D) | context |
| --- | --- | --- |
| lib41 (n ≤ 64) × 3 random starts (seed 7) | 0 | 5,461 phases; crossings 3,637 (2,006 at epoch boundaries, 1,537 X_SN^pre); σ̄(q) changes 2,542 (2,408 strict, 111 ties); max N_ep 31 (n 48), σ̄|Q repeats in 147 phases; max f per phase 23 (n 32); (SG) 15,349 checks; one cross-terminal fallback switch (DIFFSW 1) |
| 1,500 random 𝒞^kO games (n 5-18) × 5 random starts (seed 8, games seed 111) | 0 | 21,010 phases; crossings 247 (192 at epoch boundaries); σ̄(q) changes 225; Odd-choice cycle node at an X_SN^D crossing: 63 |
Reading (DATA): random starts reproduce the S3-start picture; no proved statement fails; the late regime (j ≥ n) is still never reached.

## 5. How a fallbacks-per-phase bound combines with the phase count (READING)
- Phases. Lemma Φ (R47 (a), every game): λ changes ≤ n(n − 1); Corollary Φ-kO (P-N5-DUAL, N5-MULTI §1.4): distinct τ's ≤ ∏_{q∈Q}
  deg(q), so phases ≤ n(n − 1) + ∏_q deg(q). On 𝒞^kO with k fixed that is ≤ n(n − 1) + n^k, polynomial; for k growing with n it is
  exponential (the per-vertex sharpening "τ(q) changes ≤ deg(q) − 1" is FALSE, N5-MULTI §3).
- Fallbacks over the run ≤ (phases) · max_phase f ≤ (n(n − 1) + ∏ deg(q)) · (1 + (n − 1)(2 + ρ_max)).
- Iterations. A fallback bound is not an iteration bound: S4a steps per phase need the analogue of R50 (T per phase given f), whose
  frontier form fails at LEN / Δ-RT (L-SI's N5-FRONTIER-box15 §3; N5-DELTA-box44 §8). Even with f and T per phase polynomial, the
  total is polynomial only where the phase count is: 𝒞^kO with k fixed (and 𝒞^kE by MIRROR); not the frontier with k ~ n, where
  the known exponential-SI families live (N5-MULTI §3.5).
- So for the frontier three counts are open: ρ per phase (here), T per phase given f (Δ-RT), and phases (τ-changes; Φ-kO is
  exponential in k). FB-RED reduces the first of the Lead's two to ρ.
