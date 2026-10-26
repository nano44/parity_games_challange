# P-N5-FLIP-box18: where ρ comes from inside one phase (ROOT, ROUTE-RELAY, SELF-FREE, ROOT-C, STATIC, FLIP, N3-LEVEL)
Packet for both referees. Authors: L-SI successor 14 (Opus 5.5; D15, D18, L37, L40). Source: lane note docs/si/N5-RUND-box17.md §22-§25
(not frozen; this packet is). Frozen at the Lead's request of 11:27Z (Lead's stamp); stamp of the freeze: the commit (date -u).
Scope (D1): structural lemmas inside one phase of N5 on EVERY game. Nothing here bounds N5's running time, ρ, N_ep or any count on any
class. Not a TARGET.md claim. G-N5-TIME stays OPEN.
Quotes: every «…» is verbatim from the tagged source; [Q path@commit:lines] is checked by
`python3 -I experiments/si/rund/quotecheck.py docs/si/P-N5-FLIP-box18.md` (QUOTES PASS; whitespace normalised; "…" separates parts). Pinned
in experiments/si/check.sh.

## 0. What to sign
Every item is on EVERY game, inside one phase (a maximal run with (λ_Ξ, τ) constant, RESULTS R38 (a) KEY), fallbacks included unless said.
- §2 Lemma ROOT; §3 Lemma ROUTE-RELAY and Corollary SELF-FREE; §4 Lemma ROOT-C; §5 Lemma STATIC; §6 Lemma FLIP (a) FLIP-COST, (b) FLIP-1,
  (c) Corollary, the necessary condition N1 ∨ N2 ∨ N3, and Lemma N3-LEVEL.
- Not to sign: §7 (CONJECTURES FRZ-RHO and ROOT-C's strong form; OPEN items; READINGs), §8 (DATA).

## 1. Setting, premises and cited text
- N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md. State k = (σ_k, τ_k); σ̄_k := S1's Odd counterstrategy to σ_k; Ξ_k(v) := the VJ00 valuation
  of the (σ_k, σ̄_k)-play from v (cycle node, path set P(Ξ_k v) := the vertices before the cycle node that are more relevant than it,
  length); ⊴ := SPEC S1's order (cycle-node reward first, then the signed weight of the path set, then length; the engine's key).
  Q := the Odd vertices of out-degree ≥ 2. A ρ EVENT at q ∈ Q is an in-phase transition t → t+1 with Ξ_t(q) ≠ Ξ_{t+1}(q) (RESULTS R61 (f)'s ρ_q).
- Classes and κ, as RESULTS R56 sets them: [Q docs/RESULTS.md@6f9451e3:2839-2841] «for c ∈ C the honest class U_c := λ^{-1}(c). κ_t(z) :=
  (signed weight of P(Ξ_t z), s_c·ℓ(Ξ_t z)) for z ∈ U_c, s_c := +1 if Ω(c) is odd, −1 if even; κwt_c(v) := (wt_c(v), s_c), wt_c(v) :=
  sgn(v)·2^rank(v) if rank(v) > rank(c), else 0.» Q_c := (Q ∩ U_c) ∖ {c}. Inside a class, Ξ's order is κ's (λ is fixed in a phase).
- Phase: [Q docs/RESULTS.md@6f9451e3:1825-1826] «(a) Remark KEY (every game): λ_U is a function of τ alone, so on every run of states with
  τ constant it is constant; a (λ_Ξ, τ)-phase is exactly a joint λ-phase (λ_Ξ, λ_U, τ)».
- PREMISES (the standing SPEC premise 1E-N3, in the two forms REFEREE-2 named in R2-N5-RUND §1 and both referees accept):
  - P1: σ̄_k is Odd's pointwise-optimal strategy in the one-player game G_{σ_k}. Landed as (VJ):
    [Q docs/RESULTS.md@6f9451e3:2907] «(a) Premise (VJ), on every game: for every positional σ and every positional Odd strategy τ′, Ξσ(v) ⊴
    V_{σ,τ′}(v) at every v» and the standing premise [Q docs/RESULTS.md@6f9451e3:2915-2916] «that S1's procedure realises an optimal σ̄
    is VJ00 §6 plus SPEC conformance, and the code's match to SPEC is DATA (R15 G-N5T-1) (1E-N3 = N-1E-1).»
  - P2: S4a's σ_{k+1} is Even's pointwise optimum in the arena H_k of G_τ (S1's procedure run on H_k's dual). Landed wording, R62:
    [Q docs/RESULTS.md@6f9451e3:3278-3279] «WM-G rests on the standing SPEC premise that S1 returns the arena optimum, as 1E-N3 in RESULTS
    R57». Used only in §5 (STATIC).
  - Which item uses what: ROOT, ROUTE-RELAY, SELF-FREE, ROOT-C, FLIP (b) use P1 only. FLIP (a), (c) and N3-LEVEL use P1 and (SG)
    below. STATIC uses P1 and P2.
- (SG) pointwise, every transition of a phase (S4a or fallback): Ξ_{k+1}(v) ⊵ Ξ_k(v) for every v. Basis (as the RUND fixes record it,
  docs/si/P-N5-RUND-fixes-box17.md, N-RUND-2): RESULTS R15 (a), (d) via (VJ) under P1:
  [Q docs/RESULTS.md@6f9451e3:631] «(a) Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴
  Ω_{Switch_I(σ)}.» and [Q docs/RESULTS.md@6f9451e3:640] «(d) N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G)».
- Cited landed lemmas (used, quoted):
  - R56 (d) κ-Y-FORM_D: [Q docs/RESULTS.md@6f9451e3:2858-2859] «(d) κ-Y-FORM_D (per q ∈ Q ∩ U_c, q ≠ c, at a state t where q lies on no
    honest cycle): κ_t(q) = κwt_c(q) + min over y ∈ Y^q_t of κ_t(y), with Y^q_t := {y ∈ succ(q) ∩ U_c : y's honest play at t avoids q}».
  - R61 (a) ROUTE-k (context only; not used in a proof): [Q docs/RESULTS.md@6f9451e3:3118] «(a) Lemma ROUTE-k: the relation q → par_t(q)
    has no cycle».
  - R61 (e) ALT (context only): [Q docs/RESULTS.md@6f9451e3:3128-3130] «call the change CLEAN if q lies on no honest cycle at t and at t +
    1 and y2's honest play at t avoids q; then a clean change has κ_{t+1}(q) ≥ κ_t(q), with equality only if κ_t(y2) = κ_t(y1) and
    κ_{t+1}(y2) = κ_t(y2) (a TIE at t).»
- Additivity (used in §3, §6; the decomposition of R56 (e) EXIT-SWITCH): if z ∈ U_c's honest play at s first meets e ∈ Q_c ∪ {c} after the
  vertices r (z included, e excluded), then κ_s(z) = Σ_{v ∈ r} κwt_c(v) + κ_s(e). r and e's play up to c are disjoint: a common vertex v
  would make the play from v run along r back to e, a cycle in U_c that misses c, and every honest cycle in U_c is c's cycle.

## 2. Lemma ROOT (PROVED, every game; P1)
Q-EXIT PATHS at s: for q ∈ Q and y ∈ succ(q), the play from y in G_{σ_s} (σ_s at Even vertices, the unique edge at Odd vertices outside Q)
up to and including the first vertex that is in Q or repeats. Reach_s(Q) := Q ∪ the vertices on these paths.
Statement. If at an in-phase transition t → t+1 every Q-exit path is the same at t and t + 1, then Ξ_t(v) = Ξ_{t+1}(v) for every
v ∈ Reach_t(Q). So every transition carrying a ρ event changes some Q-exit path: some Even vertex on a Q-exit path switches.
Proof. Reach_s(Q) is closed under successors in G_{σ_s}: a vertex of Q has its successors on its own exit paths; an Even or forced Odd
vertex of an exit path has as its unique successor the next vertex of that path (or, for the last vertex, the closing vertex). With equal
paths, Reach_t(Q) = Reach_{t+1}(Q) =: X and the edges of G_{σ_t} and G_{σ_{t+1}} leaving vertices of X coincide. A play from v ∈ X stays in
X, and its valuation depends only on the play. By P1, Ξ_s(v) is the ⊴-least valuation over Odd's positional strategies in G_{σ_s}, i.e.
the optimum of the one-player subgame G_{σ_s}[X]. That subgame is the same for s = t and s = t + 1. □

## 3. Lemma ROUTE-RELAY and Corollary SELF-FREE (PROVED, every game; P1)
For q ∈ Q_c on no honest cycle at t and at t + 1, and y ∈ succ(q) ∩ U_c: the EXIT of y at s is the first vertex of Q_c ∪ {c} on y's honest
play at s; its CLASS EXIT PATH is the part strictly before it. A ρ event at q at t → t+1 is ROUTE if some y ∈ succ(q) ∩ U_c has a different
class exit path or exit at t and t + 1, and RELAY otherwise.
- Lemma ROUTE-RELAY. A RELAY event at q has a SOURCE: an exit e ∉ {q, c} of some y ∈ succ(q) ∩ U_c with κ_t(e) ≠ κ_{t+1}(e), or with e's
  honest play avoiding q at exactly one of t, t + 1.
  Proof. Suppose no class exit path changes and there is no source. (i) Exit c: κ(c) is the same at t and t + 1 (λ constant; c's
  valuation has the empty path set and length 0), and c's play avoids q (q is on no honest cycle). (ii) For an exit e ∉ {q, c}, e's play
  avoids q at t iff at t + 1. So Y^q_t = Y^q_{t+1} (y's play is its class exit path, which avoids q, followed by e's play). (iii) By
  additivity (§1), κ_s(y) = Σ κwt_c(class exit path) + κ_s(e) for y ∈ Y^q_s, the same at s = t, t + 1. (iv) R56 (d) at t and t + 1:
  κ_t(q) = κ_{t+1}(q). Inside the class κ determines Ξ, so the event is not one: a contradiction. □
- Corollary SELF-FREE. If Q_c = {q}, every ρ event at q with q on no honest cycle at t, t + 1 is ROUTE (every exit is q or c, so no source
  exists). □

## 4. Lemma ROOT-C (PROVED, every game; P1): the per-class form of ROOT
Statement. If at an in-phase transition t → t+1 every class exit path of every q′ ∈ Q_c (from every y ∈ succ(q′) ∩ U_c) is the same at t
and t + 1, then κ_t(q) = κ_{t+1}(q) for every q ∈ Q_c. So every transition with a ρ event at a terminal of class c changes a class exit
path of class c.
Proof. Fix s ∈ {t, t + 1} and q ∈ Q_c. Let Π_s(q) be the set of walks q = e_0, y_0, (class exit path of y_0), e_1, y_1, …, e_j = c with
e_i ∈ Q_c distinct, y_i ∈ succ(e_i) ∩ U_c, and e_{i+1} the exit of y_i at s. Class exit paths contain no Odd choice vertex and follow σ_s
and forced Odd edges. So a walk in Π_s(q) reaches c without repeating a vertex: a repeated vertex has the same successor both times, so
the walk would cycle without reaching c. Hence each walk is the play from q of a positional Odd strategy in G_{σ_s} (choose y_i at e_i),
with cycle node c and κ equal to the walk's weight up to c.
(≤) By P1, Ξ_s(q) ⊴ the valuation of each such play. Both have cycle node c, so κ_s(q) ⪯ the walk's κ.
(≥) The optimal play from q at s stays in U_c (each vertex on it has the same optimal play suffix, hence λ = c) and is the walk of σ̄_s's
choices, so it lies in Π_s(q).
So κ_s(q) = min over Π_s(q). Π_t(q) = Π_{t+1}(q) as walks with weights (equal paths, U_c fixed in the phase). □

## 5. Lemma STATIC (PROVED, every game; P1, P2)
A ρ-FREE INTERVAL I: a maximal run of consecutive in-phase transitions with no fallback, and Ξ|Q and σ̄|Q constant.
Statement. On I, σ̄_k = σ̄_I on all Odd vertices and τ_k = τ_I. So Ξ_k is the valuation of σ_k in the fixed one-player game G_{σ̄_I}, W_k
the valuation of σ_k in the fixed one-player game G_{τ_I}, Iσ_k is σ_k's improving set in G_{σ̄_I}, and σ_{k+1} is Even's pointwise
optimum in G_{τ_I} on the arena {σ_k(v)} ∪ Iσ_k(v). So I is a run of "improve in G_{σ̄_I}, choose by G_{τ_I}" on two FIXED one-player games.
Proof. σ̄|Q is constant on I by the cut, and Odd vertices outside Q have one edge. τ is constant on the phase. Ξ_k is the (σ_k, σ̄_k)-play
value (P1 makes it the optimal reply's value). Iσ_k := {(x, z) : Ξ_k(z) ▷ Ξ_k(σ_k x)} (SPEC S2). S4a's choice is P2. □

## 6. Lemma FLIP and Lemma N3-LEVEL (PROVED, every game; P1 and (SG))
For q ∈ Q_c let par_s(q) be the exit of σ̄_s(q)'s class exit path p_s(q), when it is a terminal of Q_c other than q. A FLIP is
(q1, q2, t1 < t2) in one phase with par_{t1}(q1) = q2 and par_{t2}(q2) = q1. Write y1 := σ̄_{t1}(q1), p1 := p_{t1}(q1), p2 := p_{t2}(q2),
and C := the closed walk q1 · p1 · q2 · p2. p1 is INTACT at t2 if every vertex of p1 has the same successor at t2 as at t1 (likewise p2
at t1). X_s := P(Ξ_s q2); lev := the top rank of X_{t1} Δ X_{t2} (−1 if equal).
- (a) FLIP-COST: κ_{t2}(q2) ⪰ κ_{t1}(q2) + wt(C), where wt(C) := (Σ_{v ∈ C} wt_c(v), s_c·|C|), sums with multiplicity.
  Proof. Additivity: κ_{t1}(q1) = κwt(q1) + κwt(p1) + κ_{t1}(q2) and κ_{t2}(q2) = κwt(q2) + κwt(p2) + κ_{t2}(q1). By (SG),
  κ_{t2}(q1) ⪰ κ_{t1}(q1). Substitute (componentwise sums; ⪰ is lexicographic and invariant under adding a constant). □
- (b) FLIP-1: if p1 is intact at t2, the cycle Z that the play from q1 reaches in G_{σ_{t2}} under σ̄′ := σ̄_{t2}[q1 ↦ y1] has a node w
  with rew(w) > rew(c).
  Proof. The σ̄′-play from q1 follows y1 and p1 (intact; no Odd choice vertex on it) to q2, then σ̄_{t2}(q2)'s path p2 back to q1. It
  never reaches c, so w ≠ c. By P1, Ξ_{t2}(q1) ⊴ that play's valuation. Ξ_{t2}(q1) has node c, cycle nodes are compared first, and rew
  is injective, so rew(c) < rew(w). □
- (c) Corollary: if p1 is intact at t2 and p1 ∩ p2 = ∅, then Z = C. Let h be C's top vertex. rew(h) > rew(c) forces either rank(h) >
  rank(c) with h even, so Σ wt_c over C > 0, or rank(h) < rank(c) with c odd, so the weight is 0 and s_c·|C| = |C| > 0. Either way
  wt(C) ≻ 0, and by (a) κ(q2) rises strictly between t1 and t2, by at least wt(C). □
- NECESSARY CONDITION at every flip (from (a)-(c)): (N1) an Even vertex of p1 switches between t1 and t2 (p1 not intact at t2), or (N2)
  p1 ∩ p2 ≠ ∅, or (N3) κ(q2) rises strictly between t1 and t2 by at least wt(C), C an Odd-unattractive cycle through q1 and q2.
- Lemma N3-LEVEL. Let (q1, q2, t1 < t2) be a flip with p1 ∩ p2 = ∅. Let h be C's highest-ranked vertex, with rank(h) > rank(c) and h
  even (both hold when p1 is intact at t2, by (c)). If h ∈ p2, assume also that p2 is intact at t1. Then lev ≥ rank(h).
  Proof. (no cycle) A vertex's honest play at s reaches c, so it cannot meet, before c, a vertex from which the plays at s lead back to
  it. (decomposition) X_{t2} = {q2} ∪ p2 ∪ P(Ξ_{t2} q1) and P(Ξ_{t1} q1) = {q1} ∪ p1 ∪ X_{t1} (disjoint, above c; additivity). Every
  vertex of C has rank ≤ rank(h), so above rank(h), X_{t2} agrees with P(Ξ_{t2} q1) and X_{t1} with P(Ξ_{t1} q1).
  - h = q1: q1 ∈ X_{t2} (q2's play at t2 runs along p2 to q1). q1 ∉ X_{t1}, else q2's play at t1 meets q1, whose play at t1 runs along
    p1 to q2. So lev ≥ rank(h).
  - h ∈ p2: h ∈ X_{t2}. h ∉ X_{t1}, else q2's play at t1 meets h and follows p2 (intact at t1) to q1, then p1 back to q2.
  - h ∈ p1: h ∉ X_{t1} (else p1 leads q2's play back to q2). If h ∈ P(Ξ_{t2} q1), then h ∈ X_{t2}. Otherwise P(Ξ_{t1} q1) ∋ h ∌
    P(Ξ_{t2} q1), and their top differing rank L′ is ≥ rank(h). By (SG) with the same cycle node, P(Ξ_{t2} q1) has the larger signed
    weight. L′ = rank(h) would make P(Ξ_{t1} q1), the set containing the even h, the heavier one: a contradiction. So L′ > rank(h), and
    by the decomposition X_{t1}, X_{t2} differ at L′.
  - h = q2: q2 ∈ P(Ξ_{t1} q1), and q2 ∉ P(Ξ_{t2} q1) (else p2 leads q1's play back to q1). As in the previous case, L′ > rank(h), and
    X_{t1}, X_{t2} differ at L′. □
  Sharp: equality lev = rank(h) occurs (§8, leanT_N6).

## 7. Not to sign
- CONJECTURE FRZ-RHO: on every ρ-free interval I, Ξ on Reach(Q) changes only at transitions with index < n − 1 from I's start. DATA:
  0 violations; tightest xsn29_n32, 27 vs n − 1 = 31. A proof stops at the W-guided arena choice on R_D (note §23.4).
- CONJECTURE ROOT-C (strong form): every (class, transition) with a ρ event has a ROUTE or CYC event at a terminal of that class WITH an
  event. DATA only (ALLRELAY_T = 0). ROOT-C (§4) is the proved weaker form.
- READINGs (note §22.5, §24.4, §25): the re-thaw loop ρT ≤ T_exit ≤ (n − 1)(ρT + 1) (the second inequality needs FRZ-RHO-type freezing);
  on 𝒞^1O the loop is open (SELF-FREE), with m_c ≥ 2 it closes through relay cycles; a flip is never free (N1 / N2 / N3); N3-LEVEL plus a
  per-level ruler count bounds N3 flips of a pair by 2^{#ranks ≥ top(C)}, polynomial only for cycle tops near the class top.
- OPEN: a bound on ρ_q per phase for m_c ≥ 2; a proof of FRZ-RHO. DEAD (for the record; docs/si/DEAD.md 18a-18c, pinned): UF-ONCE,
  U-SPLIT, PAIR-OC.

## 8. DATA (not proof; experiments/si/rund/, own scripts; N5 via experiments/new/box21/n5x.py step, read-only)
| check (script) | sets | result | control |
| --- | --- | --- | --- |
| ROOT (relay.py ROOT_V) | lib41 (KMIN = 1, S3 + 4 random starts; 1,601 phases, 5,437 ρ-transitions), lib2o (183) | 0 | MUT=1 (inverted) fails on frz40 |
| ROUTE-RELAY (R_EMPTY_V), SELF-FREE (ONE_RELAY_V) | same; one-Odd-choice classes 5,042 events, all ROUTE; multi 618 ROUTE / 427 RELAY | 0 / 0 | – |
| ROOT-C strong form (ALLRELAY_T) | same, frz40, nep76_n40 | 0 | – |
| relay-graph cycles (relay.py CYC2 / CYCG) | lib41: 23 / 28 of 1,601 phases; frz40 phase@44 11 ↔ 26 | DATA | – |
| FLIP (a), (b) (flipck.py FLIPCOST_V, FLIP1_V) | frz40, lib41, pp_K12_n161, pp_K48_n449 (L-RED R83) | 0 / 0 | MUT=1 (reversed) fails on frz40, pp_K12 |
| N3-LEVEL (flipck.py N3LEV_V) | pp_K12 15, pp_K48 51, lib41 12 checks | 0 | MUT=2 (strict) fails on leanT_N6 (3 equalities) |
| FRZ-RHO (frzrho.py FRZ_RHO_V) | lib41 2,471 intervals, lib2o 164 | 0 | – |
- Pins (experiments/si/check.sh): frz40 relay graph (exact), FLIP on frz40 and pp_K12_n161 (copied from L-RED, sha1 8808ba5d…), N3-LEVEL on
  leanT_N6 (sha1 f037844a…, RS = 4 starts) with the strict control, FRZ-RHO counts on frz40, this packet's quotes.
- frz40's 11 ↔ 26 flip is N1 (fallbacks at t = 14, 17 re-route 11's successors; Even 9 at t = 28 routes 26's successor 29 into 11); the
  mkpp flips are N3 (intact, strict rise of the receiving terminal). Logs: experiments/si/rund/logs/flip_*.txt, relay_*.txt, frzrho_*.txt.
