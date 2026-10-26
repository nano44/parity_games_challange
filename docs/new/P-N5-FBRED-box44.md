# Packet P-N5-FBRED (box 44): in-phase fallbacks per phase on EVERY game are ≤ 1 + (n − 1)(2 + ρ), ρ = honest-value changes at Odd choice vertices (FB-POLY's lemmas in set form; Theorem FB-RED; Lemma TV)
L-NEW successor 23 (Opus 5.5), D14 / D18, Lead reading L40; Lead's order 02:21Z (Lead's stamp): "Packet it together with ρ-POLY if that
closes, or alone if ρ stalls." ρ-POLY stalled (§5), so this packet is FB-RED alone. Written 2026-10-26 02:36Z-02:38Z (date -u).
FROZEN at push: later text goes into a fixes file. Source: docs/new/N5-FBF-box44.md §0-§2, §6 (working doc; this packet governs).
Port of: docs/new/P-N5-FBPOLY-box41.md (= RESULTS R48), cited "FBP §x". Labels: PROVED (L-NEW 23, unrefereed) / CONJECTURE / OPEN /
DATA / READING. Not a TARGET.md claim: FB-RED is a REDUCTION (fallbacks per phase given ρ); nothing here bounds N5's running time on
any class beyond 𝒞^1O ∪ 𝒞^1E. G-N5-TIME stays open.

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1.1 | facts (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′), per honest class | PROVED |
| §1.2 | κ-FB-ROUND_D | PROVED |
| §1.2 | κ-HAT-FREEZE_D (a)-(c) | PROVED |
| §1.2 | κ-PFZ_D (per Odd choice vertex q) | PROVED |
| §1.2 | κ-Y-FORM_D (per q, repaired Y^q) | PROVED |
| §2 | EXIT-SWITCH_D, FREEZE-EXIT_D (conservative indices), CN-ONLY_D | PROVED |
| §3.1, §3.2 | Theorem FB-RED and its late form | PROVED |
| §3.3 | Lemma TV | PROVED |
- Not to sign: §4 (the step table vs FBP, READING), §5 (THETA-AFTER fails as proved; CONJECTURE ρ-POLY; the obstruction), §6 (DATA).
- Hypotheses: none on the class, on (h_D), (h3_D), D_k, H1, τ or c_w. Every statement is per phase of N5 on any game.
- Premises (landed; R-numbers): (V1) (R17 (a)); R15 (a) (Ξ never drops); S1 / S2 / S4c (SPEC, FIX 3); Lemma S (a) (R18 (d)); CN-LAST
  (R38 (f), every game); KEY (R38 (a)). READING for the referees: Lemma S (a) is signed under R18's 𝒞^1O setting line, but its proof is
  VJ00 (11) on G_σ with no one-Odd step (ledger N5-MULTI §2: "survives verbatim").

## 0. Setting (every game)
- N5, phases (maximal runs with (λ_Ξ, τ) constant; = joint λ-phases, R38 (a)), in-phase transitions (S4a steps or Even S4c fallbacks),
  g_1 < g_2 < … the in-phase fallbacks of a phase: as in FBP §0.1. N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md.
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
  vertices (all forced there) their edge if inside. For q ∈ Q ∩ U_c, q ≠ c: G_c^q := U_c ∖ (T ∖ {q}) (so c and the other Odd choice vertices are dropped) with q a sink, same rules.
  κopt_c(z) := max{κwt_c(p ∖ {c}) : p a simple path of G_c from z to c}.
- A Q_c-RUN: a maximal run of consecutive states of the phase with Ξ(q) constant for every q ∈ Q ∩ U_c (on 𝒞^1O: a θ-run). A
  Q-RUN: the same with all q ∈ Q.
- ρ := the number of pairs (transition t → t+1 of the phase, q ∈ Q) with Ξ_{t+1}(q) ≠ Ξ_t(q).

## 1. Facts and the κ lemmas (PROVED, every game)
### 1.1 Facts and κ-FB-ROUND
- (Aκ): for z ∈ U_c ∖ {c}: λ_t(z) = c ≠ z, so (V1) gives Ξ_t(z) = z ⊕ Ξ_t(next_t z) with cycle node c; next_t(z) ∈ U_c, and κ_t(z) =
  κwt_c(z) + κ_t(next_t z) (FBP's no-double-count argument with c). (A0κ), (M1κ), (M2κ), (INJ), (SP′): FBP §0.3 with c for c_θ
  ((SP′): the prefix of z's honest play up to its first visit of T ∩ U_c is simple, since c ∈ T lies on the cycle).
- κ-FB-ROUND: FBP §1 verbatim with U_c, c (its proof uses only (Aκ), (M1κ), (M2κ) and S4c's best-key rule).
### 1.2 κ-HAT-FREEZE_D, κ-PFZ_D, κ-Y-FORM_D
- κ-HAT-FREEZE (a): for t > g_j, z ∈ U_c ∖ (Q ∖ {c}) and every simple path p of G_c from z to c with ≤ j edges, κ_t(z) ≥
  κwt_c(p ∖ {c}). Induction as FBP: Odd z on p is a vertex of G_c, hence not in Q, hence forced, and its forced successor x is
  next_t(z); Even z uses κ-FB-ROUND at g_j. (b): if z's honest play at t avoids Q ∖ {c} and z ∈ U_c, its prefix to c is a simple
  path of G_c ((SP′); Even edges σ_t, Odd vertices on it are not in Q, so forced), and (Aκ) gives κ_t(z) ≤ κopt_c(z). (c): simple
  paths of G_c have ≤ |U_c| − 1 edges, so for t > g_{|U_c|−1}, (a) and (b) give κ_t(y) = κopt_c(y) for every y ∈ U_c whose honest play
  at t avoids Q ∖ {c}.
- κ-PFZ (per q ∈ Q ∩ U_c, q ≠ c, Θ a Q_c-run): for t ∈ Θ with t > f^Θ_j, z ∈ U_c ∖ T and every simple path p of G_c^q from z to q
  with ≤ j edges: κ_t(z) ≥ κwt_c(p ∖ {q}) + κ_t(q). FBP §1 verbatim (Odd vertices of G_c^q other than q are forced).
- κ-Y-FORM (per q ∈ Q ∩ U_c, q ≠ c, at a state t where q lies on no honest cycle): κ_t(q) = κwt_c(q) + min_{y ∈ Y^q_t} κ_t(y).
  "≥": σ̄_t(q) ∈ Y^q_t (its honest play is the rest of q's, which does not return to q). "≤": for y ∈ Y^q_t let τ′ := σ̄_t except
  τ′(q) := y. y's (σ_t, τ′)-play is its honest play (it avoids q, the only vertex where τ′ and σ̄_t differ), so V_{σ_t,τ′}(y) = Ξ_t(y)
  and V_{σ_t,τ′}(q) = q ⊕ Ξ_t(y). Lemma S (a) (R18 (d)): Ξ_t(q) ⊴ q ⊕ Ξ_t(y); both have cycle node c; (M1κ). ∎
## 2. EXIT-SWITCH_D, FREEZE-EXIT_D, CN-ONLY_D (PROVED, every game)
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
### 3.1 Theorem FB-RED (PROVED, every game)
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

### 3.2 Theorem FB-RED, late form (PROVED, every game)
Only Q-runs that hold a LATE fallback (g_j with j ≥ n) count: f ≤ 1 + (n − 1) + (n − 1)·N_late, with N_late := the number of Q-runs
of the phase holding a fallback g_j, j ≥ n. Proof: §3.1's third bullet counts, per Q-run, only the fallbacks g_j with j ≥ n.
N_late ≤ 1 + ρ_late, ρ_late := Ξ-changes at Odd choice vertices at transitions after g_{n−1}. (On 𝒞^1O this is the form FB-POLY uses:
THETA-AFTER bounds only the θ-runs that meet late states.)
### 3.3 Lemma TV (terminal-value freeze; PROVED, every game)
Let Θ be a Q-run of a phase, c ∈ C, and t ∈ Θ with t > g_{|U_c|−1} and t > f^Θ_{|U_c|−1} (after |U_c| − 1 fallbacks of the phase and
of Θ). Then for every z ∈ U_c ∖ T:
κ_t(z) = V_z(κ(Q)) := max( κopt_c(z), max_{q ∈ Q ∩ U_c, q ≠ c} [κopt^q(z) + κ_Θ(q)] ),
with κopt^q(z) := max{κwt_c(p ∖ {q}) : p a simple path of G_c^q from z to q} (max over an empty set omitted).
Proof. "≥": every simple path of G_c or G_c^q has ≤ |U_c| − 1 edges; κ-HAT-FREEZE (a) at t > g_{|U_c|−1} gives κ_t(z) ≥ κopt_c(z);
κ-PFZ at t > f^Θ_{|U_c|−1} (Θ lies inside a Q_c-run, so its fallbacks are fallbacks of that run) gives κ_t(z) ≥ κopt^q(z) + κ_Θ(q).
"≤": z's honest play at t up to its first vertex e of T ∩ U_c is a simple path ((SP′)) whose Odd vertices before e are forced; if
e = c it is a path of G_c and (Aκ) gives κ_t(z) ≤ κopt_c(z); if e = q it is a path of G_c^q and κ_t(z) = κwt_c(path ∖ {q}) + κ_t(q)
≤ κopt^q(z) + κ_Θ(q). ∎
## 4. Step table against FB-POLY (READING, not to sign)
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
| FB-POLY (§6) | REDUCED | f ≤ 1 + (n − 1)(2 + ρ) (Theorem FB-RED, §3.1) | THETA-AFTER replaced by the count ρ |

## 5. Not to sign: THETA-AFTER and CONJECTURE ρ-POLY (OPEN)
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
- DATA (§6): the per-terminal THETA-AFTER bound (Ξ(q)-changes after g_{|U_c|−2} ≤ deg_{U_c}(q) + |U_c| − 2) held in every sample so far (733 checks, 0 violations). So THETA-AFTER fails as PROVED, with no instance against
  its per-terminal statement yet; climbs aimed at one (fbclimb.py --obj ta, 4 runs) found none (§6).

### 5.1 Why the nested freeze stalls (OPEN)
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
- The nesting route of §5 (bottom-up freeze when the terminal routing is acyclic and stable) gives at best (deg + |U|)^{depth}, with
  depth up to |Q|: polynomial for fixed k, exponential in k, the same shape as Φ-kO.
- Verdict: ρ-POLY stays CONJECTURE; FB-RED (both forms) and TV are what is PROVED.
## 6. Data (DATA, not proof; experiments/new/box44/fbf.py, fbclimb.py; tables in docs/new/N5-FBF-box44.md §4, §6.4)
- 0 violations of CN-ONLY_D, EXIT-SWITCH_D, FREEZE-EXIT_D (FBP's sharper indices), FB-RED and its late form in: lib41 (412 runs, 2,335
  phases), 3,500 random 𝒞^kO runs (k 2-4), the box-43/44 instances, and every game scored by 21 climbs (fallbacks per phase, TA, ρ).
- Max in-phase fallbacks per phase: frontier 17 at n 32 (experiments/new/box44/instances/fb17_n32.pg, sha1 398e23e2…; N5 output
  verified by Oink and harness verify.py), 21 at n 64; 𝒞^1O 33 at n 48. Max ρ per phase 160 (leanT_N32, n 256).
- Thin: NO phase in any sample reaches n fallbacks, so FB-RED's third bullet, its late form and Lemma TV act only in a regime the data
  never reach; they rest on their proofs. The per-terminal THETA-AFTER bound held in every check (733 + climbs), but it is not proved.
- Reproduce (from experiments/new/box44): `python3 fbf.py --list ../box41/lib41.txt` → "runs 412: phases 2335, FMAX 33, …, CNO_V 0,
  EXS_V 0, FEX_V 0, RED_V 0, …, REDL_V 0, …" (~1 min).
