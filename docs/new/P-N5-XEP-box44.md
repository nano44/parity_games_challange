# Packet P-N5-XEP (box 44): crossings per phase on EVERY game are O(n²) per epoch plus a residual inside fixed-frame S4a runs (R-STICK_D, SN-PREFIX_D, D-EPOCH, X-EP)
L-NEW successor 23 (Opus 5.5), D14 / D18, Lead reading L40; Lead's word 05:00Z / 05:05Z (Lead's stamps): "P-N5-XEP = R-STICK_D + SN-PREFIX_D +
D-EPOCH + X-EP. Freeze it." Written 2026-10-26 05:09Z (date -u). FROZEN at push: later text goes into a fixes file.
Source: docs/new/N5-FBF-box44.md §12-§14 (working doc; this packet governs). Labels: PROVED (L-NEW 23, unrefereed) / READING / OPEN / DATA.
Not a TARGET.md claim: X-EP is a REDUCTION (crossings given N_ep and the residual X_SN^pre); nothing here bounds N5's running time on any
class beyond 𝒞^1O ∪ 𝒞^1E. G-N5-TIME stays open.

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Lemma R-STICK_D | PROVED |
| §2 | Corollary SN-PREFIX_D (a)-(c) | PROVED |
| §3 | Fact D-EPOCH | PROVED |
| §4 | Lemma X-EP (and its form with ALT) | PROVED |
| §5 | the qc_toggle configuration instance, the residual X_SN^pre (OPEN), data | DATA / OPEN / READING (not to sign) |
- Premises:
  - LANDED: R55 (P-N5-GD) Lemma G_D (a) (off R_D, Ξ = W; no hypothesis); R21 (a) Lemma XW (Ξ_k ⊴ W_k; premise class confirmed
    game-general on R55 / R56); R23 (g) Lemma WM (W_{k+1} ⊵ W_k at an in-phase non-fallback transition; its proof is "σ_k lies in its own S4a
    arena, and R17 (F1) on G_τ", game-general); SPEC S1 (rewards injective; cycle nodes compare by reward first), S4a, S4c; R38 (a) KEY.
  - IN REVIEW: P-N5-ACCEL (docs/new/P-N5-ACCEL-box44.md, sha1 301f0be0fa2b2240bba59b347dfbee8426b8dba3): §3 Lemma EPOCH (b) (after an
    epoch's (n − 1)-th fallback, the rest of the epoch has ≤ 4n(n − 1) + 1 transitions). P-N5-FBK (docs/new/P-N5-FBK-box44.md, sha1
    afd7c65a265053531171b66294811bbd9a801dd2): §4 Lemma ALT and its N_ep corollary. §4 here is CONDITIONAL on those two as cited.

## 0. Setting (every game)
- N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md. State k = (σ_k, τ_k); σ̄_k = S1's optimal Odd counterstrategy to σ_k; Ξ_k = the honest
  valuation (play values of (σ_k, σ̄_k)); λ := its cycle-node map; W_k := σ_k's valuation in G_τ (Odd fixed to τ_k); λ_W := W's cycle-node
  map. A PHASE: a maximal run with (λ, τ) constant; f := its in-phase fallbacks.
- D_k := {Odd u : σ̄_k(u) ≠ τ_k(u)}; R_D(k) := the vertices whose (σ_k, τ_k)-play meets D_k; F_D(k) := V ∖ R_D(k) (R55 §0).
- A vertex v is SPLIT at k if λ_{W,k}(v) ≠ λ(v), UNSPLIT otherwise. A CROSSING is an in-phase transition s → s+1 with R_D(s) ≠ R_D(s+1);
  X_D := the number of crossings of the phase.
- Q := the Odd vertices of out-degree ≥ 2. An EPOCH: a maximal run of consecutive states of the phase with σ̄|Q constant; N_ep := their
  number (P-N5-ACCEL §0). For an epoch E, e_1 < e_2 < … are its in-phase fallbacks (by source state).

## 1. Lemma R-STICK_D (PROVED, every game)
At an in-phase S4a transition s → s+1, every split v ∈ R_D(s) lies in R_D(s+1) (whatever D_{s+1} is).
Proof. Suppose v ∈ R_D(s) ∩ F_D(s+1); c := λ(v) (constant on the phase), c′ := λ_{W,s}(v) ≠ c. G_D (a) at s+1: W_{s+1}(v) = Ξ_{s+1}(v), with
cycle node c. WM: W_{s+1}(v) ⊵ W_s(v); the cycle nodes differ and rewards are injective, so rew(c) > rew(c′). XW at s: Ξ_s(v) ⊴ W_s(v), with
cycle nodes c and c′, so rew(c) < rew(c′). Contradiction. □
- Port note (READING): this is RESULTS R30 (c) R-STICK with R19 (a) replaced by G_D (a) and the one-Odd fact "every v ∈ R has λ(v) = c_θ
  and W-cycle node c_w" (HP) dropped: the statement is per vertex.

## 2. Corollary SN-PREFIX_D (PROVED, every game)
- (a) Along a run of consecutive in-phase S4a transitions, for each vertex v the states at which v is unsplit form a prefix of the run.
  Proof: WM makes W(v) non-decreasing along the run, so rew(λ_W(v)) is non-decreasing; XW gives rew(λ_W(v)) ≥ rew(λ(v)), with equality iff
  λ_W(v) = λ(v); λ(v) is constant. So once v is split, it stays split for the rest of the run. □
- (b) In such a run, after its unsplit prefix a vertex changes its R_D-membership at most once: it may enter R_D, and it never leaves
  (R-STICK_D at each transition). □
- (c) Per phase: X_D ≤ (f + 1)·n + f + X_SN^D, where X_SN^D := the crossings at which some vertex unsplit at the source state changes
  R_D-membership.
  Proof: the f fallback transitions split the phase into ≤ f + 1 runs of S4a transitions. In a run, a crossing at which every
  membership-changing vertex is split has an entering split vertex ((b): split vertices do not leave), and each vertex enters at most once
  after its prefix ((a), (b)); so ≤ n such crossings per run. The remaining crossings are fallback transitions (≤ f) or in X_SN^D. □

## 3. Fact D-EPOCH (PROVED, every game)
On a phase τ is constant, so D_s = {u ∈ Q : σ̄_s(u) ≠ τ(u)} (an Odd vertex of out-degree 1 has σ̄ = τ) changes only at transitions where
σ̄|Q changes, i.e. only at epoch boundaries. On an epoch E, D and σ̄ are constant; the honest frame is the one-player game G_E (Odd fixed to
σ̄_E) and the W-frame is the one-player game G_τ; they differ exactly at the vertices of D. In particular, for an Odd choice vertex c that
is an honest cycle node of the phase, σ̄(c) is constant on each epoch. □

## 4. Lemma X-EP (PROVED, every game; §4's last line conditional on P-N5-FBK's ALT)
For every phase:
X_D ≤ (N_ep − 1) + N_ep·(n² + n + 4n(n − 1)) + Σ_E X_SN^pre(E),
where, for an epoch E, X_SN^pre(E) := the crossings with both ends in E and source state ≤ e_{n−1} (all of E's crossings if E has fewer
than n − 1 fallbacks) at which some vertex unsplit at the source changes R_D-membership.
Proof. Classify the crossings.
- At an epoch boundary (σ̄|Q changes at the transition): at most N_ep − 1 transitions.
- With both ends in an epoch E and source state > e_{n−1}: by EPOCH (b) (P-N5-ACCEL §3) that part of E has at most 4n(n − 1) + 1
  transitions.
- With both ends in E and source state ≤ e_{n−1}: these are among ≤ n − 1 fallback transitions and ≤ n runs of consecutive S4a
  transitions. In each run, crossings at which every membership-changing vertex is split number ≤ n (SN-PREFIX_D (a), (b)); the others
  are in X_SN^pre(E).
Sum: (N_ep − 1) + Σ_E [(4n(n − 1) + 1) + (n − 1) + n·n + X_SN^pre(E)]. □
- With ALT (P-N5-FBK §4, Corollary N_ep): N_ep ≤ 1 + Σ_{q ∈ Q}(ρ_q + tie_q + nc_q + cyc_q). Hence X_D = O(n²)·(1 + ρ + ties + non-clean +
  cycle-node changes) + Σ_E X_SN^pre(E): every crossing outside the residual is charged to the quantity that also bounds fallbacks
  (R56 (f) Theorem FB-RED).

## 5. Not to sign
- Configuration instance (DATA): experiments/new/box44/instances/qc_toggle.pg (n 5, Q = {0, 2, 3, 4}, sha1
  27850ecc3d9e660aefa6a3401d6af0cfc2b3317c; N5's output passes Oink verify). From S3: one S4a transition, one phase; every vertex's honest
  cycle node is 4, an Odd choice vertex; D = {0}; vertex 1, unsplit (λ_W = λ = 4), enters R_D (σ(1): 2 → 0). So an X_SN^D crossing occurs in a
  class whose cycle node is an Odd choice vertex, the case excluded on 𝒞^1O by R34 (d) TOGGLE ("so c ∈ V_E") and the case split of R34 (b)
  L-MONO. By D-EPOCH, σ̄(c) moves only at epoch boundaries, which X-EP charges to N_ep.
- OPEN: X_SN^pre. It lives inside one S4a run of one epoch, where D, σ̄ and τ are fixed and N5 compares two FIXED one-player frames (G_E,
  G_τ) under gated W-optimal steps. With |D| = 1 the R19-R20 machinery is expected to port per epoch (docs/new/N5-DELTA-box44.md §7;
  being checked); with |D| ≥ 2 it needs the route order across terminals (Δ-RT, docs/new/N5-DELTA-box44.md §8).
- DATA (experiments/new/box44/rstick.py, randstarts.py; S3 starts and random start pairs): R-STICK_D 14,253 + 13,329 + 94 checks, SN-PREFIX_D
  and the bound of §2 (c): 0 violations. Crossings in lib41 (S3): 3,222 = 1,269 at epoch boundaries + 1,953 inside epochs (0 after an epoch
  freeze; 1,833 unsplit pre-freeze, i.e. X_SN^pre). No epoch in any sample reaches n − 1 fallbacks, so EPOCH (b)'s term is vacuous in data.
