# P-N5-CHOSEN-box19: relays follow the chosen exit, and a frozen class stays frozen (CHOSEN, RELAY-CHAIN, TV-END)
Packet for both referees. Author: L-SI successor 15 (Opus 5.5; D15, D18, L37, L40). Source: lane note docs/si/N5-RUND-box17.md §26.2,
§27.3 (not frozen; this packet is). Written at the Lead's request of 12:37Z (Lead's stamp: "Packet them together with (a)'s result (or its
precise obstruction) at your box end or handover"). Stamp of the freeze: the commit (date -u).
Scope (D1): structural lemmas inside one phase of N5 on EVERY game. Nothing here bounds N5's running time, ρ, N_ep, f or any count. Not a
TARGET.md claim. G-N5-TIME stays OPEN.
Quotes: every «…» is verbatim from the tagged source; [Q path@commit:lines] is checked by
`python3 -I experiments/si/rund/quotecheck.py docs/si/P-N5-CHOSEN-box19.md` (QUOTES PASS; whitespace normalised; "…" separates parts).
Pinned in experiments/si/check.sh.

## 0. What to sign
Every item holds on EVERY game, inside one phase (a maximal run with (λ_Ξ, τ) constant, RESULTS R38 (a) KEY), fallbacks included.
- §2 Lemma CHOSEN; §3 Corollary RELAY-CHAIN and its two consequences (a), (b); §4 Lemma TV-END.
- Not to sign: §5 (the obstruction map for the per-piece count, a READING; the DATA).

## 1. Setting, premises and cited text
- N5, states, σ̄_k, Ξ_k, Q, ρ events, classes U_c, κ, κwt_c, Q_c := (Q ∩ U_c) ∖ {c}: exactly as packet P-N5-FLIP-box18 §1 (sha1 96a7e088…,
  signed by both referees; repairs in docs/si/P-N5-FLIP-fixes-box18.md, sha1 93a65e1b…). T := Q ∪ {c} for the class at hand.
  - The landed setting line of RESULTS R56, which defines κ: [Q docs/RESULTS.md@6f9451e3:2839-2841] «for c ∈ C the honest class U_c :=
    λ^{-1}(c). κ_t(z) := (signed weight of P(Ξ_t z), s_c·ℓ(Ξ_t z)) for z ∈ U_c, s_c := +1 if Ω(c) is odd, −1 if even; κwt_c(v) :=
    (wt_c(v), s_c), wt_c(v) := sgn(v)·2^rank(v) if rank(v) > rank(c), else 0.»
  - Phase: [Q docs/RESULTS.md@6f9451e3:1825-1826] «(a) Remark KEY (every game): λ_U is a function of τ alone, so on every run of states
    with τ constant it is constant; a (λ_Ξ, τ)-phase is exactly a joint λ-phase (λ_Ξ, λ_U, τ)». Inside a class, Ξ's order is κ's (λ is
    fixed in the phase).
- EXIT and CLASS EXIT PATH (P-N5-FLIP §3, per y; N-FLIP-3): for y ∈ U_c, the exit of y at s is the first vertex of Q_c ∪ {c} on y's honest
  play at s, and its class exit path is the part strictly before it. A ρ event at q ∈ Q_c (q on no honest cycle at t, t + 1) is ROUTE if
  some y ∈ succ(q) ∩ U_c has a different class exit path or exit at t and t + 1, and RELAY otherwise (P-N5-FLIP §3). It is CYC if q = c or q
  lies on its honest cycle at t or t + 1.
- Additivity (P-N5-FLIP §1, signed by both as a proof step, "CORRECT"): [Q docs/si/P-N5-FLIP-box18.md@7ea3d8cf:48-50] «if z ∈ U_c's honest
  play at s first meets e ∈ Q_c ∪ {c} after the vertices r (z included, e excluded), then κ_s(z) = Σ_{v ∈ r} κwt_c(v) + κ_s(e). r and e's
  play up to c are disjoint».
- PREMISES. P1 (the standing SPEC premise 1E-N3 in form P1; σ̄_k is Odd's pointwise optimum in G_{σ_k}) and (SG) (Ξ is pointwise
  non-decreasing at every transition, fallbacks included), with their bases as in P-N5-FLIP §1:
  [Q docs/RESULTS.md@6f9451e3:631] «(a) Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴
  Ω_{Switch_I(σ)}.» and [Q docs/RESULTS.md@6f9451e3:640] «(d) N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G)».
  The last sentence is also the fact (SW) used in §4: every Even switch of N5 (S4a or S4c) is to an edge of Iσ, and
  [Q docs/si/P-N5-FLIP-box18.md@7ea3d8cf:97] «Iσ_k := {(x, z) : Ξ_k(z) ▷ Ξ_k(σ_k x)} (SPEC S2).»
- Cited landed / signed lemmas (used):
  - R56 (d) κ-Y-FORM_D: [Q docs/RESULTS.md@6f9451e3:2858-2859] «(d) κ-Y-FORM_D (per q ∈ Q ∩ U_c, q ≠ c, at a state t where q lies on no
    honest cycle): κ_t(q) = κwt_c(q) + min over y ∈ Y^q_t of κ_t(y), with Y^q_t := {y ∈ succ(q) ∩ U_c : y's honest play at t avoids q}».
  - R56 (g) Lemma TV (only to say when §4's hypothesis holds): [Q docs/RESULTS.md@6f9451e3:2868-2869] «(g) Lemma TV: for a Q-run Θ, c ∈ C,
    and t ∈ Θ after |U_c| − 1 fallbacks of the phase and of Θ, every z ∈ U_c ∖ T has κ_t(z) = max(κopt_c(z), max over q ∈ Q ∩ U_c, q ≠ c,
    of κopt^q(z) + κ_Θ(q)).» (κopt_c, κopt^q, G_c, G_c^q as in R56's setting line, l. 2842-2844 at 6f9451e3.)
  - ROOT-C in its signed form (P-N5-FLIP-fixes-box18 R1, both referees' wording):
    [Q docs/referee/R-N5-FLIP.md@72db1b18:161-162] «Joint repair: "class exit path AND EXIT" in the hypothesis and "changes a class exit
    path or exit" in the consequence (both referees, word for word the same fix).» That is: if every class exit path AND exit of every
    q′ ∈ Q_c is the same at t and t + 1, then κ_t = κ_{t+1} on Q_c.
- Which item uses what: CHOSEN uses P1 (through R56 (d)), (SG), additivity. RELAY-CHAIN uses CHOSEN and the definitions. TV-END uses (SG),
  (SW), additivity, the phase (λ fixed) and ROOT-C (signed form, P1).

## 2. Lemma CHOSEN (PROVED, every game; P1, (SG))
Setting: a transition t → t+1 of the phase, q ∈ Q_c on no honest cycle at t and t + 1, with a RELAY ρ event. Let y* := σ̄_t(q), p := y*'s
class exit path at t and e := its exit (the CHOSEN EXIT of q at t).
Statement. e ≠ c, and either κ_t(e) ≠ κ_{t+1}(e) (e has a ρ event at t → t+1), or e's honest play at t + 1 passes through q (TOG).
Proof.
- y* ∈ U_c (λ(q) = c and q's optimal play enters y*), and y*'s play at t avoids q (q on no honest cycle at t), so y* ∈ Y^q_t. By R56 (d)
  at t (and its "≥" half, i.e. σ̄_t attains the minimum, P1): κ_t(q) = κwt_c(q) + κ_t(y*).
- RELAY: p and e are the same at t + 1. Additivity at s = t, t + 1: κ_s(y*) = κwt_c(p) + κ_s(e).
- Suppose, for a contradiction, that e = c, or that e's play at t + 1 avoids q and κ_{t+1}(e) = κ_t(e). (κ(c) is constant in the phase.)
  - y*'s play at t + 1 is p followed by e's play. p avoids q, because class exit paths stop at Q_c ∋ q. If e = c, c's play is c's cycle,
    which avoids q (q on no honest cycle at t + 1). So y* ∈ Y^q_{t+1} and κ_{t+1}(y*) = κ_t(y*).
  - R56 (d) at t + 1: κ_{t+1}(q) ⪯ κwt_c(q) + κ_{t+1}(y*) = κ_t(q).
  - (SG): Ξ_{t+1}(q) ⊵ Ξ_t(q), and inside the class Ξ's order is κ's, so κ_{t+1}(q) ⪰ κ_t(q).
  - Hence κ_{t+1}(q) = κ_t(q) and Ξ_{t+1}(q) = Ξ_t(q) (κ determines Ξ inside the class): no ρ event, a contradiction. □
- Remark. CHOSEN sharpens ROUTE-RELAY (P-N5-FLIP §3): the source is the exit of q's CHOSEN option. κ(q) is a minimum of option values that
  never decrease, so it can rise only if the option attaining it rises.

## 3. Corollary RELAY-CHAIN (PROVED, every game; from CHOSEN)
Statement. Let q have a RELAY ρ event at t → t+1. Put e_0 := q and, while e_i has a RELAY event at t → t+1, let e_{i+1} := the chosen exit
of e_i at t. The sequence stops, after at most |Q_c| − 1 steps, at e_i whose event at t → t+1 is ROUTE or CYC, or at a TOG step (CHOSEN's
second alternative at e_i).
Proof.
- Each step exists by CHOSEN: e_{i+1} ∈ Q_c ∖ {e_i} has a ρ event, unless TOG holds at e_i.
- e_0's honest play at t is: y*(e_0), its class exit path, e_1, then e_1's play. Inductively it passes e_0, e_1, e_2, … in this order,
  before c.
- If e_i = e_j with i < j, the play from e_i returns to e_i, so e_i lies on its own honest cycle at t, and its event is CYC, not RELAY. Then
  the sequence would already have stopped at e_i. So the e_i are distinct, and the sequence stops within |Q_c| − 1 steps. □
Consequences (same transition t → t+1, same class):
- (a) Every transition with a ρ event at some terminal of the class carries a ROUTE or CYC event of the class, or a TOG step. (This is the
  stronger, per-event form of ROOT-C's consequence, which only asks for a changed class exit path or exit.)
- (b) Counting events over a phase: Σ_{q ∈ Q_c} ρ_q ≤ |Q_c| · (ROUTE_c + CYC_c + TOG_c). Here ROUTE_c, CYC_c are the ROUTE, CYC events in the
  class, and TOG_c the RELAY events ending in a TOG step. Each RELAY event is mapped to the end of its sequence, at the same transition, and
  at most |Q_c| events map to one end. □

## 4. Lemma TV-END (PROVED, every game; P1, (SG), (SW), ROOT-C signed form)
Setting: a phase, a class c, T := Q ∪ {c}, and a Q_c-RUN Θ: a maximal run of the phase with Ξ(q) constant for every q ∈ Q_c. For
z ∈ U_c ∖ T put TV_Θ(z) := max(κopt_c(z), max_{q ∈ Q_c} κopt^q(z) + κ_Θ(q)), with R56's κopt_c, κopt^q. Hypothesis (H) at a state t ∈ Θ:
κ_t(z) = TV_Θ(z) for every z ∈ U_c ∖ T. By R56 (g), (H) holds at every t after |U_c| − 1 fallbacks of the phase and of a Q-RUN, i.e. a run
with ALL of Q constant, which is contained in a Q_c-run.
Statement. If (H) holds at t ∈ Θ and t → t+1 is in the phase, then no Even vertex of U_c ∖ T switches at t → t+1 (S4a or S4c), t + 1 ∈ Θ,
and (H) holds at t + 1. Hence, from t to the end of the phase, class c has no switch in U_c ∖ T and no ρ event, and Θ lasts to the phase's
end.
Proof.
- (i) Let x ∈ U_c ∖ T be Even and switch to z := σ_{t+1}(x). By (SW), (x, z) ∈ Iσ_t: Ξ_t(z) ▷ Ξ_t(σ_t x). In the phase λ_{t+1}(x) = c, and
  x ≠ c, so z's play at t + 1 reaches c and λ(z) = c, i.e. z ∈ U_c. So κ_t(z) ≻ κ_t(σ_t x), and by additivity on x's honest play at t,
  κwt_c(x) + κ_t(z) ≻ κ_t(x).
- (ii) Suppose x is not on z's honest play at t before that play's exit e ∈ T (if z ∈ T, then e = z and the play before e is empty).
  - Then x·(z's class exit path) is a simple path of G_c (e = c) or of G_c^e (e ∈ Q_c), with no vertex of T but its end.
  - By additivity and κ_t(e) = κ_Θ(e): κwt_c(x) + κ_t(z) = κwt_c(x · z's class exit path) + κ_Θ(e) ⪯ TV_Θ(x) = κ_t(x), by (H).
  - This contradicts (i).
- (iii) So every Even x ∈ U_c ∖ T that switches at t → t+1 lies on its target z(x)'s honest play at t, before that play's exit. Let S be
  the set of these x, and suppose S ≠ ∅. Follow x's play at t + 1 from some x ∈ S:
  - it runs x, z(x), then along z(x)'s play at t (unchanged edges at non-switching Even vertices and at forced Odd vertices) up to the first
    vertex of S on it, which comes before any vertex of T, because x itself is on that part;
  - from there it repeats the same step.
  The play never meets T. The vertices passed are non-terminal: Even vertices of U_c ∖ T, or Odd vertices outside Q, hence forced. So the
  play never reaches c, and λ_{t+1}(x) ≠ c, which contradicts the phase. So S = ∅.
- (iv) With S = ∅, every class exit path and exit of class c is the same at t and t + 1. Their vertices lie in U_c ∖ T: Even
  non-switching vertices or forced Odd vertices. By ROOT-C (signed form), κ_{t+1} = κ_t on Q_c, so t + 1 ∈ Θ. For z ∈ U_c ∖ T, z's class
  exit path and exit are unchanged and so is the terminal's value, so κ_{t+1}(z) = κ_t(z) = TV_Θ(z) by additivity: (H) holds at t + 1.
  Induction to the phase's end. □
- Remark. R56 (e) FREEZE-EXIT_D says that the late FALLBACKS switch nothing in the class. TV-END extends this to every in-phase transition,
  and from (H) on, the freeze lasts to the phase's end. It bounds no count: ρ events in the class all occur before (H) first holds.

## 5. Not to sign: the obstruction map for the per-piece count (READING) and DATA
- READING (note §27.1). The fallback side of the 𝒞^1O count (R44, R45 HAT-FREEZE, R48) is landed on every game by R56 (a)-(g). The S4a side
  (R50 FRZ-U / Theorem RUN; R45 BF-F, FREEZE-F) uses one gate. On general games it is R64 (e) EP-1 for |D_E| = 1 (landed with R65), and
  for |D_E| ≥ 2 it is OPEN. So a per-terminal bound for m_c ≥ 2 is the |D_E| ≥ 2 core plus N_ep, not a port.
- DATA (lane scripts experiments/si/rund/chosen.py, tvend.py, flipcls.py, quiet.py; logs in rund/logs/):
  - CHOSEN / RELAY-CHAIN: 0 violations, TOG never occurs.
    - lib41 (S3 + 4 random starts): 5,660 ROUTE, 427 RELAY, 42 CYC events, longest chain 11.
    - lib2o: 202 / 44 / 0.
    - nep90_n40: 153 / 139; nep76_n40: 129 / 48; frz40: 21 / 13; pp_K12_n161: 18 / 13; pp_K48_n449: 54 / 49.
    - Control MUT=1 (the next state's choice instead of the current one) fails on nep90, nep76, frz40, pp_K12.
  - TV-END: 0 violations, but THIN. The script triggers on |U_c| − 1 fallbacks of the phase and of the Q_c-run, a weaker trigger than R56
    (g)'s Q-run. Under it, lib41 reaches the freeze in 20 classes, all with |Q_c| ≤ 1, with 39 frozen transitions. Its control does not bite.
  - Context: nep90_n40 (L-RED, sha1 7348271a…) and nep76_n40 have ρ_q up to 72 and 62 per phase at n = 40, with ACYCLIC relay graphs
    rooted at one terminal whose events are all ROUTE (note §26.3), and 42 and 32 epochs of about 2 transitions each, mostly with |D| ≥ 2
    (note §27.2).
