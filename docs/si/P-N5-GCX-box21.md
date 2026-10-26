# P-N5-GCX (box 21): gate migrations split; the unforbid-switch count reduces to gate events under a late-freeze premise; and a settling bound in an abstract model
L-SI successor 17 (Opus 5.5; D18, Lead reading L40). Packet for the referees, frozen at its push (the sha1 goes to the Lead). Lead's
instruction 16:34Z: «freeze what is proved (MIG-SPLIT, UL-RED conditional, ABS-HEIGHT in the abstract model, plus whatever lift step closes)
as a packet ... with exact premises». Working note: docs/si/N5-GCX-box21.md (§1-§9; data, dead ends, readings).
Labels (D18 / L40): PROVED (lane, unrefereed) / CONJECTURE / OPEN / DATA / READING. Not a TARGET.md claim. Nothing here bounds N5's running
time on any class; G-N5-TIME stays OPEN.
Quotes: every [Q path@commit:lines] «…» is verbatim from the tagged source, checked by experiments/si/rund/quotecheck.py (pinned in
experiments/si/check.sh, with a shifted-line control that must fail).

## 0. What is claimed (all PROVED, lane, unrefereed)
| item | statement in one line | premises |
| --- | --- | --- |
| §2 Lemma MIG-SPLIT | a migration of z into a D-direct gate's region is a D-leave of z's old gate or an Even switch on z's path in front of it | SPEC (definitions only) |
| §3 Corollary UL-RED | IF no unforbid-switch happens late in a global C-interval (premise UL_G), THEN |U(S)| and every vertex's coarse W changes are polynomial in n and the number K(S) of C-cuts | UL_G (a CONJECTURE, §5) and RESULTS R67 (f) CHARGE-U |
| §4 Lemma ABS-HEIGHT | in the acyclic abstract model ABS, the run is fixed after ≤ height ≤ n steps | none (self-contained model) |
| §4 Lemma ABS-TIE | in ABS with any deterministic W-tie rule, fixed after ≤ max over paths of Σ deg ≤ m steps | none |
| §4 Lemma LOC | in the cyclic model, a change of v at t+1 → t+2 needs a successor whose M, N or viability changed | none |
Not claimed (§5): the lift of §4 to N5, and the CONJECTURES UL_C / UL_G, FINAL-EACH / ABS-CYC.

## 1. Setting and definitions (every game)
- Setting as in RESULTS R62 / R67: [Q docs/RESULTS.md@7d87f9be:3451-3452] «A run S: consecutive states k_0, …, k_1 inside one phase, all of
  whose transitions are S4a steps (no fallback)», and [Q docs/RESULTS.md@7d87f9be:3452] «(ii) := λ_W constant on S».
  D_k as in R55: [Q docs/RESULTS.md@7d87f9be:2786] «D_k := {Odd u : σ̄_k(u) ≠ τ_k(u)}».
  U(S): [Q docs/RESULTS.md@7d87f9be:3457-3458] «U(S) := the S4a switch events (k′, (y, z)) of S into an edge forbidden at some state of
  [k′ − n + 1, k′ − 1] ∩ S (UNFORBID-SWITCHES)», at level L = −1 throughout this packet.
- For a cycle node c of the phase: U_c := λ^{-1}(c) (constant on the phase). At state t: the PLAY of z is its (σ_t, τ)-play; A_t := {z ∈ U_c :
  z's play meets no vertex of D_t}; for u ∈ D_t ∩ U_c, R_u(t) := {z ∈ U_c : the first D_t-vertex on z's play is u}; DD_t := {u ∈ D_t ∩ U_c :
  σ̄_t(u) ∈ A_t and τ(u) ∈ A_t} (D-DIRECT gates); for u ∈ DD_t, Δ_t(u) := M_t(τ u) − M_t(σ̄ u), with M_t(z) the signed weight of the path set of
  Ξ_t(z).
- X-MIGRATION into u at t → t+1: a vertex z ∈ R_u(t+1) ∖ (R_u(t) ∪ A_t), with u ∈ DD_t ∩ DD_{t+1}. X_u(S) := the transitions of S that carry
  one. G_c(S) := the transitions of S with A_{t+1} ⊄ A_t.
- GLOBAL C-INTERVAL of S: a maximal sub-interval of S on which, for every cycle node c, A_t (of U_c) is non-increasing, D_t is constant and
  every Δ_t(u), u ∈ DD_t, is constant. A C-CUT: a transition of S in no global C-interval. K(S) := the number of C-cuts.

## 2. Lemma MIG-SPLIT (PROVED, elementary)
Statement. Let t → t+1 be an in-phase S4a transition and z an X-migration into u at t → t+1, with first D_t-vertex u′ (u′ ≠ u, since
z ∉ R_u(t) ∪ A_t). Then (L) u′ ∉ D_{t+1}, or (S) some Even vertex w on the part π of z's play at t before u′ (z included) has σ_{t+1}(w) ≠
σ_t(w); in case (S) z's play changes at t → t+1.
Proof. Suppose u′ ∈ D_{t+1} and no Even vertex of π switches. The Odd vertices of π are not in D_t, so they follow τ, which is constant on
the phase; so z's play at t + 1 begins with π and reaches u′. Its first D_{t+1}-vertex is u′ unless some vertex of π lies in D_{t+1}; then it is
the first such vertex. It must be u, since z ∈ R_u(t+1). But u ∈ DD_t ⊆ D_t, and π has no D_t-vertex. So it is u′ ≠ u, against z ∈ R_u(t+1).
In case (S), w lies on z's play at t and its successor changes, so the play changes. □
- Consequence. X_u(S) ≤ #{transitions of S at which some vertex of D ∩ U_c leaves D} + #{transitions of S at which some z ∈ U_c changes its
  play (its W-play)}.

## 3. Corollary UL-RED (PROVED, conditional on UL_G)
Premise UL_G (a CONJECTURE, §5): for every run S with (ii), every U event (k′, e) ∈ U(S) whose transition k′ → k′+1 lies in a global
C-interval [a, b] has k′ − a < n − 1.
Statement. Under UL_G, for every run S with (ii), with n_E the number of Even vertices:
- (a) |U(S)| ≤ n_E·((n − 1)(K(S) + 1) + K(S));
- (b) for every vertex x, COARSE_{−1}(W(x)) changes ≤ (n − 1)(1 + n_E·((n − 1)(K(S) + 1) + K(S))) times on S.
Proof. (a) A U event is a switch of one Even vertex at one transition, so a transition carries ≤ n_E U events. The C-cuts number K(S).
There are ≤ K(S) + 1 global C-intervals, and by UL_G at most n − 1 transitions of each can carry U events. (b) RESULTS R67 (f), Corollary
CHARGE-U: [Q docs/RESULTS.md@7d87f9be:3485-3486] «Corollary CHARGE-U (hypothesis (ii) only): for every x the changes of COARSE_L(W(x)) on
S number ≤ (n − 1)(1 + |U(S)|)», with L = −1, and (a). □
- Scope. Only the arithmetic is new. The content is the premise UL_G. K(S) is not bounded here. It counts the transitions at which some
  class's A grows, D changes, or a D-direct offset changes.

## 4. The abstract model and its settling bounds (PROVED in the model; self-contained)
Model ABS. A finite digraph on NON-TERMINALS V (|V| = n) and TERMINALS, each terminal t with constants h(t) ≤ T(t); each v ∈ V has weight
w(v) and successors succ(v) ≠ ∅. Values lie in a totally ordered abelian group (e.g. Z, or Z × Z lexicographically). A STRATEGY s picks
s(v) ∈ succ(v). It is VALID if every play reaches a terminal; then M_s(v) := Σ_{u on v's play} w(u) + h(end) and N_s(v) := the same with T.
A STEP from a valid s: ARENA Al_s(v) := {s(v)} ∪ {y ∈ succ(v) : M_s(y) > M_s(s(v))} (M_s(t) := h(t), N_s(t) := T(t) at terminals); s′ := a
valid strategy using arena edges only whose N is pointwise maximal among those. The model ASSUMES one exists, and in the CYCLIC model the
run is restricted to games where it does. Ties are broken by a deterministic rule R(arena, values, current choice); the basic rule keeps
the current choice when it is a maximiser. ACYCLIC model: the digraph on V is acyclic.
- Lemma ABS-HEIGHT (acyclic; basic tie rule). The run is fixed (s′ = s) after at most height ≤ n steps (height: longest path to a
  terminal, in vertices).
  Proof. Call v SETTLED from state t if every successor of v has constant (M, N) from state t on. Then s_{t+2}(v) = s_{t+1}(v). Let y1 :=
  s_{t+1}(v), an N-maximiser over Al_t(v); in the acyclic model the pointwise optimum chooses at v an N_{t+1}-maximiser over the arena,
  since successors' optimal values do not depend on v. If y1 = s_t(v), then Al_{t+1}(v) = Al_t(v), because the M-values are unchanged,
  and y1 stays a maximiser, kept by the rule. Otherwise M(y1) > M(s_t v), so Al_{t+1}(v) = {y1} ∪ {y : M(y) > M(y1)} ⊆ Al_t(v); the
  N-values are unchanged, so y1 is still a maximiser and is kept. So v and its values are constant from t + 1. A vertex whose successors
  are all terminals is settled from 0; by induction in reverse topological order, a vertex of height h is constant from state h on. □
- Lemma ABS-TIE (acyclic; any deterministic tie rule R). The run is fixed after at most D := max over paths of Σ deg(v) ≤ m steps.
  Proof. Let v be settled from t. A later change of v at a step goes to y ∈ Al(v) ∖ {s(v)}, so M(s(v)) strictly rises and the arena strictly
  shrinks. The N-maximum over the arena is still attained (at the new choice). So after the first step there are ≤ deg(v) − 1 changes, and
  a step with no change repeats the inputs of R, so the changes are consecutive. v is constant from t + deg(v); induct as above. □
- Lemma LOC (cyclic model; basic or any deterministic rule). If s_{t+2}(v) ≠ s_{t+1}(v), then some successor y of v has M_t(y) ≠
  M_{t+1}(y), or N_{t+1}(y) ≠ N_{t+2}(y), or changes VIABILITY for v (its play avoids v under s_{t+1} but not under s_{t+2}, or the reverse).
  Proof. In a pointwise maximal valid arena strategy, v's choice is an N-maximiser over the VIABLE arena successors (any viable one can be
  substituted at v alone, keeping validity; a non-viable one closes a cycle). If none of the three changes, the proof of ABS-HEIGHT applies
  to the viable successors verbatim. □
- Remarks (PROVED in the model). (MONO) M and N are non-decreasing along the run: policy improvement on improving edges, and the current
  choice is in the arena. (MONO-SUCC) M(s_t(v)) is non-decreasing in t. (NO-RETURN) If v leaves y at t1 and takes it again at t2 > t1, then
  M_{t2}(y) > M_{t1}(y).

## 5. Not claimed (CONJECTURE / OPEN / READING), with data pointers
- READING (why the model): in a global C-interval in which every gate is D-direct ("pure"), once A has frozen, each gate u is a terminal
  with constant h_u = wt(u) + M(σ̄ u) and T_u = wt(u) + M(τ u) = h_u + Δ(u), and S4a acts on U_c as the model's step. The freeze takes
  ≤ |A_a| − 1 steps, by FREEZE-A (b) of the P-N5-ROOT packet (in review, not landed). The model's honest values are Ξ's (M, length) pairs,
  and its W-values are W's. The arena is SPEC S4a's Iσ, and the step is Even's optimum of the arena. This identification is not part of
  the claims.
- OPEN, the lift to N5: (i) cycles in G_c. The naive cyclic settling order is DEAD (docs/si/DEAD.md "DEAD box 21b", instance
  abscyc.py DEEP). (ii) N5's actual tie rule: ABS-TIE covers any deterministic rule in the acyclic model. (iv) impure intervals (non-direct
  gates).
- CONJECTURE FINAL-EACH (cyclic model): every transition with a change holds some vertex's final change; hence ≤ n steps (ABS-CYC). DATA:
  0 violations in 22,989 transitions (random cyclic games, n = 4-6); 9 hill-climbs reach exactly n (note §8, §9).
- CONJECTURE UL_C (per class) / UL_G (global, §3's premise): no U event late in a C-interval. DATA (note §4): 0 violations on lib41 (KMIN 1,
  S3 + 4 random starts: 1,504 U events inside C-intervals), lib2o, L-RED's mkpp / mkgate, nep90, nep76, the UF-ONCE / U-SPLIT killers,
  6,000 random 𝒞^kO games, climbs. Support is thin (17 lib41 intervals reach |U| − 1). L-RED 22 and L-COMP 5 are attacking it (Lead
  16:22Z, 16:34Z).
- DEAD (own candidates, docs/si/DEAD.md "DEAD box 21", "DEAD box 21b"): C-ONCE, UE-ONCE_C, the naive cyclic settling order.
- DATA on G_c / X_u (note §2): on L-RED R90's families G_c(S) = 2 while X_u(S) = Θ(K), a Bellman-Ford wave on fresh content; on nep90 / nep76
  every X-migration is case (L) of MIG-SPLIT.
