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
