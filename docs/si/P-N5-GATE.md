# Packet P-N5-GATE: gate races, expulsions and who pays a gate flip, on N5′-xi's Howard run on Γ3 and on IDEAL-CYC
L-SI successor 49 (Opus 5.5), D18 / D14 / D1; Lead brief 2026-11-09 06:33Z («CONSOLIDATE your lane's surviving gate lemmas into a FROZEN
PACKET for the referees, P-N5-GATE»). Written 2026-11-09 (date -u: see the commit). Sources (history only, NOT part of what is signed):
docs/si/box91-expel.md (+ Correction 1), box92-closed.md (+ Addendum 1), box93-k7k6.md (+ Addendum 1), box94-nest.md. This packet carries
every proof in full and is checked against this text only. Labels: PROVED (L-SI, unrefereed) / PROVED-CONDITIONAL (on a named pending
packet) / DATA / DEAD / READING (not to sign). Not a TARGET.md claim; not M3 or M4; not a gauntlet step; G-N5-TIME stays OPEN.

Scope (one sentence). Every lemma here is a statement about ONE run of Howard strategy improvement with Vöge-Jurdziński values (on Γ3(G)
from S3, i.e. N5′-xi's mover phase, and on IDEAL-CYC(G)); together they say which face pays each flip of an Odd gate (the face Odd
leaves), that only letters at least as relevant as the gate's e-vertex can pay on PRIV steps, that a non-PRIV β-face follows the e-face
and costs nothing, that a gate's relocks are bounded by its e-face continuation's value changes, that followers with a common suffix
copy, and that a letter can leave a vertex's play only to a strictly higher letter on a parallel divergent segment. None of them bounds
T3; they are reductions of the open core (C, A*_all, …: L-NEW's N5-CORE-forms) to per-gate or per-continuation quantities.

## To sign, and what is not to sign
| § | statement | label | premises (§1) |
| --- | --- | --- | --- |
| §3.1 | Lemma GATE-RACE (a), (b); Corollary TRIGGER | PROVED | F1, F2, LOC-GATE3, NO-TIE3, E-MON3, [OPT] |
| §3.2 | Lemma GATE-LOW-NULL (a), (b) | PROVED | [VJ], [OPT], F3, (E-DOM), (Core), LOC-GATE3, NO-TIE3, E-MON3 |
| §3.3 | Lemma NP-SHAPE (a), (b) | PROVED | [Γ3] gate structure, [VJ], [OPT] |
| §3.4 | Corollary E-FACE-PAYS (a)-(d); Lemma WAIT-QUIET | PROVED | GATE-RACE (a); F6; CYC (for (c)); [VJ] |
| §3.5 | Lemma SAME-SUFFIX; Lemma STEP-BOUND | PROVED | [VJ], LOC-GATE3, NO-TIE3, [HOW] |
| §3.6 | Lemma PARALLEL | PROVED | [OPT], F3, E-MON3, positional plays |
| §3.7 | Lemma PAIR-EXPEL; Corollary EXPEL-COUNT | PROVED-CONDITIONAL on P-N5-SPLIT (Step 1 quotes its §2 (a)) | F1, F2, F4′, F6, STRICT, CN2-3, LOC-GATE3, NO-TIE3, (E-DOM), (Core), [VJ], [OPT], E-MON3 |
| §3.8 | Corollary A*-EQUIV (with A*_all; the A*_route form) | PROVED-CONDITIONAL on P-N5-SPLIT (SPLIT-COUNT) and P-N5-CHAIN (C-EQUIV) | E-MON3; SPLIT-COUNT; C-EQUIV |
| §4-§8 | overlaps, DEAD list, DATA, controls, TARGET diff, attack record | DATA / DEAD / READING (not to sign) | |

## 1. Premises (named exactly; source and status)
- P-N5-CHAIN (L-NEW; frozen claude/l-new 93531b03; landing as R125, PENDING): the Γ3 facts used by name: F1 (values never fall:
  Ω_(t−1)(v) ⊴ Ω_t(v) for every vertex v), F2 (Λ_t(v) only moves to a larger cycle reward; distinct cycle rewards, so Λ never returns),
  F3 (E_t(v) is the set of e-vertices on v's play at t more relevant than Λ_t(v)), F4′ (the extension inequality used in P-N5-SPLIT §2 (a)),
  F6 (an e-vertex has exactly one successor, its W-target), STRICT, CYC (a vertex's Λ takes at most 2M + 3 values), CN2-3, LOC-GATE3 (at a
  gate Odd plays the ◁-smaller face), NO-TIE3 (the two faces of a gate never have equal values), (E-DOM) (every vertex more relevant than
  some e-vertex is an e-vertex, c_W, K0 or K3), (Core) (K0, K3 lie on both of two plays with the same Λ or on neither), [OPT], E-MON3
  (inside one Λ-interval of v, E_t(v) is lex-nondecreasing, lex = compare by the most relevant element of the symmetric difference; so
  a change has a TOP, the most relevant element of the difference, and the top ENTERS).
- P-N5-SPLIT (L-NEW; frozen claude/l-new 399cda07, sha1 5bc1b1f3, fixes entry 1 at 63515442; referees PENDING): Lemma SPLIT / TRANSFER
  (the split u of a change of v's play and its new successor b), §2 (a) (the mover-step inequality chain), SPLIT-COUNT
  (c_y(v, I) ≤ Σ_(u,b) Dhi_y(b, J_b)); C-EQUIV and the form list in L-NEW's docs/new/N5-CORE-forms.md (claude/l-new 14babccb).
- Landed: RESULTS R118 (IDEAL-CYC(G), Howard switch-best with VJ values (Λ, Π, k) and ⊴; BR-SEG), R121 (E-MON on IDEAL-CYC), R123
  (LOC-GATE, NO-TIE, B-ONLY, CN2, LOC-K2, T-QUIET on IDEAL-CYC; class (Λ, E)). R122 (P-ACYC) is cited in §7 only.
- [VJ]: the VJ value of a vertex is (Λ, Π, k) (cycle node, the set of play vertices more relevant than Λ, path length); two values with
  the same Λ compare by the most relevant vertex of the symmetric difference of their Π's (its parity decides), then by k (R118's
  premises; VJ00 §4.2, Friedmann arXiv 1106.0778 §3, as cited by R118). [HOW]: at each step every Even mover switches to a ▷-best option
  for the values of the previous step (Howard); σ̄_t is Odd's optimal counterstrategy at σ_t (unique at gates by NO-TIE).
- [Γ3] gate structure (gamma3.build at claude/l-new fcba92fc; own.build at claude/l-red 4b309716 for Γ): every option (x, k) of a mover
  has a gate g_(x,k) (Odd) with exactly two successors, its e-face (the e-vertex e_(x,k), on Γ3 through one pad) and its β-face; the
  e-vertex's only in-edge comes from the gate (through the pad); e_(x,k)'s only successor is its W-target (c_W if none).
- IDEAL-CYC reading of the premises: on Γ(G) (R118 (a)) the same lemmas hold with R123's LOC-GATE, NO-TIE, R121's E-MON, R118's
  monotonicity in place of LOC-GATE3, NO-TIE3, E-MON3, F1, F2 (no pads). Every DATA row is on both (§6).

## 2. Definitions used throughout
- A run: states t = 0, …, T (T = T3 on Γ3, T_CYC on IDEAL-CYC). Ω_t(v) the value, P_t(v) the play (a simple path followed by one cycle,
  following σ_t and σ̄_t), Λ_t(v) its cycle node, E_t(v) as in F3. A Λ-interval of v: a maximal interval of states with Λ_t(v) fixed.
- A gate o with e-face p_e (whose play starts with e_o; p_e = e_o on Γ, the pad on Γ3) and β-face p_b. D := e_o's successor (its
  e-face CONTINUATION). o FLIPS at t if σ̄_(t−1)(o) ≠ σ̄_t(o): an UNLOCK (p_b → p_e) or a RELOCK (p_e → p_b).
- ch_f := #{t ≥ 1 : Ω_t(f) ≠ Ω_(t−1)(f)}; lam_f := #{t : Λ_t(f) ≠ Λ_(t−1)(f)}; nl_f := ch_f − lam_f; lamch(o) := #{t : Λ changes at p_e
  or at p_b} (L-NEW box 202's counter). S(x) := {t : Ω_t(x) ≠ Ω_(t−1)(x)}.
- LAM_t: Λ_t(p_e) = Λ_t(p_b). PRIV_t: e_o ∉ E_t(p_b). NP_t := not PRIV_t. UP_t: e_o more relevant than Λ_t(p_e).
  π(X) := {f ∈ X : f at least as relevant as e_o}.
- For a vertex b, a Λ-interval J of b and a letter y: U_y := e-vertices more relevant than y; H_s := E_s(b) ∩ U_y; Dhi_y(b, J) :=
  #distinct H_s, s ∈ J; a_z(b, J) := #maximal runs of states s ∈ J with z ∈ E_s(b); A*_all := max over ALL b, J, z of a_z(b, J);
  A*_route := the same maximum over the route vertices b (new successors of split pairs, P-N5-SPLIT) and letters z ∈ U_y; C := max over
  (v, I, y) of c_y(v, I) (# changes of E(v) in I with top y).

## 3. Statements and proofs
### 3.1 Lemma GATE-RACE and Corollary TRIGGER (PROVED; F1, F2, LOC-GATE3, NO-TIE3; TRIGGER also E-MON3, [OPT], F3)
(a) If o flips at t from face p to face q, then Ω_t(p) ≠ Ω_(t−1)(p). (b) #flips(o) ≤ min(ch_p + ch_q, 2·min(ch_p, ch_q) + 1).
Proof. (a) LOC-GATE3 and NO-TIE3 at t − 1 (Odd on p) and at t (Odd on q), with F1 for q:
Ω_(t−1)(p) ◁ Ω_(t−1)(q) ⊴ Ω_t(q) ◁ Ω_t(p); so Ω_(t−1)(p) ◁ Ω_t(p). (b) Flips alternate p → q, q → p; by (a) the p → q flips are at
distinct change steps of p, the q → p flips at distinct change steps of q; alternation gives the min form. ∎
Corollary TRIGGER. In (a) the change of the left face p at t is (α) a change of Λ(p) (at most 2M + 2 over the run: F2, CYC), or (β)
inside one Λ-interval of p a change of E(p), whose top x enters E_t(p), i.e. x lies on P_t(p) (E-MON3, F3), or (γ) neither (a change of
Π(p) below every e-letter, or of k). ∎ (L-RED 63's Lemma REL-G, R229-box93 §1.3, excludes (γ) for relocks with UP_(t−1); cited, §4.)

### 3.2 Lemma GATE-LOW-NULL (PROVED; [VJ], [OPT], F3, (E-DOM), (Core), LOC-GATE3, NO-TIE3, E-MON3)
(a) At a step t with LAM_t, PRIV_t and e_o ∈ E_t(p_e): Ω_t(p_e) ▷ Ω_t(p_b) ⟺ π(E_t(p_e)) >lex π(E_t(p_b)), and the two π's differ.
(b) If t − 1 and t are LAM ∧ PRIV ∧ UP steps and o flips at t, then π(E(p_e)) or π(E(p_b)) changes at t. (b′) If moreover
Λ(p_e) = Λ(p_b) is the same at t − 1 and t: at a relock π(E(p_e)) rises, at an unlock π(E(p_b)) rises.
Proof. (a) e_o ∈ E_t(p_e) \ E_t(p_b) (PRIV), so the symmetric difference of the e-sets is non-empty; let z be its most relevant element:
z is at least as relevant as e_o, so z is also the most relevant element of π(E_t(p_e)) Δ π(E_t(p_b)), on the same side. With equal
Λ, [VJ] decides by the most relevant vertex of Π_t(p_e) Δ Π_t(p_b). A vertex of that difference more relevant than z would be more
relevant than an e-vertex, hence an e-vertex, c_W, K0 or K3 (E-DOM); not an e-vertex (z is the top among them), not c_W (in no Π: its
self-loop is never on a play with this Λ), not K0 / K3 ((Core): both plays or neither). So the decider is z, an even vertex; the side
holding z is ▷-larger. That is the π comparison. (b) UP at s ∈ {t − 1, t} gives e_o ∈ E_s(p_e) (p_e's play starts with e_o, F3). By
(a) and LOC-GATE3 / NO-TIE3, σ̄_s(o) is a function of (π(E_s(p_e)), π(E_s(p_b))); if neither changes, o does not flip. (b′): at a
relock Odd moves to p_b, so by (a) π(E_(t−1)(p_e)) <lex π(E_(t−1)(p_b)) and π(E_t(p_e)) >lex π(E_t(p_b)). Both faces are in one
Λ-interval over {t − 1, t} (hypothesis), so E(p_b) is lex-nondecreasing (E-MON3), and a lex rise of a set cannot lower its projection π
(the top of the difference is either at least as relevant as e_o, and then it is the top of the projections' difference on the same
side, or below e_o, and then the projections are equal). So π(E(p_b)) does not fall, and π(E(p_e)) must rise. Unlocks: symmetric. ∎
- Scope (L-RED 63, R229-box92): the K3 / K4 / K9 consequences hold on LAM ∧ PRIV ∧ UP steps only; a flip at a LAM ∧ PRIV step with e_o
  not above Λ («below», row K10 of WAIT-CLOSED) is covered by no part of this lemma (but by §3.4).

### 3.3 Lemma NP-SHAPE (PROVED; [Γ3], [VJ], [OPT])
(a) If NP_t then σ̄_t(o) = p_e, P_t(p_b) = A_t · o · P_t(p_e) for a path A_t from p_b to o, Λ_t(p_b) = Λ_t(p_e), and E_t(p_e) ⊆ E_t(p_b).
(b) If o flips at t, not both NP_(t−1) and NP_t; NP_(t−1) implies a relock, NP_t an unlock.
Proof. (a) e_o's only in-edge comes from o's e-face side ([Γ3]), so a play passing e_o passes o and leaves o by p_e: σ̄_t(o) = p_e. From
o on, P_t(p_b) follows the same edges as P_t(p_e) (both follow σ_t, σ̄_t from o); the part before o is A_t. Both plays end in the same
cycle, so Λ is equal, and F3 gives E_t(p_e) ⊆ E_t(p_b). (b) By (a), NP_s forces σ̄_s(o) = p_e; a flip changes σ̄(o), so at most one of
s = t − 1, t has NP, and on that side o plays p_e. ∎ (R229-box93 §1.1: correct; a clause on «unequal Λ» in the box-93 text was vacuous
and is dropped here.)
- Reading: at a non-PRIV state Ω(p_b) = ext(A · o, Ω(p_e)): the β-face follows the e-face, and Odd stays on p_e because the prefix A · o
  is Even-favoured. GATE-LOW-NULL needs PRIV because there the two faces are independent; here they are not.

### 3.4 Corollary E-FACE-PAYS, Lemma WAIT-QUIET and the per-gate bound (PROVED; GATE-RACE (a), F6, [VJ]; (c) also CYC)
(a) relocks(o) ≤ ch_(p_e); unlocks(o) ≤ 1 + relocks(o) ≤ 1 + ch_(p_e); likewise unlocks(o) ≤ ch_(p_b). No PRIV, LAM or UP hypothesis.
(b) At every t with e_o ∉ P_(t−1)(D) ∪ P_t(D): Ω_t(p_e) ≠ Ω_(t−1)(p_e) ⟺ Ω_t(D) ≠ Ω_(t−1)(D). Hence on any window where D's play avoids
    e_o, the value changes of p_e and of D are the same steps.
(c) If D's play avoids e_o over the run: unlocks(o) ≤ 1 + ch_D ≤ 1 + (2M + 2) + Σ_J #changes of E(D) in J + gam(D)
    ≤ 2M + 3 + (2M + 3)·M·C + gam(D), gam(D) := the value changes of D with Λ and E unchanged.
(d) flips(o) ≤ 2·min(ch_(p_e), ch_(p_b)) + 1 ≤ 2·lamch(o) + 2·min_f nl_f + 1. If some face f has nl_f = 0, flips(o) ≤ 2·lamch(o) + 1.
Proof. (a) GATE-RACE (a) applied to relocks (left face p_e) and to unlocks (left face p_b); flips alternate. GATE-RACE (a) uses F1 and
Odd's ◁-choice only. (b) e_o ∉ P(D) at both steps, so P(p_e) = (pad,) e_o · P(D) at both (F6: e_o's only successor is D). The map
(Λ, Π, k) ↦ (Λ, Π ∪ ({e_o, pad} ∩ above-Λ), k + |prefix|) is injective for a fixed prefix not on the play. (c) (a), (b); a value change
of D is a Λ-change (≤ 2M + 2: CYC, F2), or inside a Λ-interval an E-change (each has one top y, so their number is Σ_y c_y(D, J) ≤ M·C;
≤ 2M + 3 intervals), or neither (gam). (d) GATE-RACE (b); ch_f = lam_f + nl_f and lam_f ≤ lamch(o). ∎
Lemma WAIT-QUIET (= (a) + (b)). A gate whose e-face continuation D changes value at most K times while its play avoids e_o unlocks at most
K + 1 times and flips at most 2K + 1 times, whatever its trigger: PRIV or not, Λ-keyed, letter-keyed, length-only, or a copy (the
classes K1-K10 of box 92's WAIT-CLOSED). ∎
- Tightness (DATA, §6): MWR(n): flips 2n + 1 = 2·ch_D + 1 with lamch 0; MW(n)'s race gate: relocks 2n + 1 = ch_(p_e) = ch_D.
- The proviso «D's play avoids e_o» was never violated on any measured instance (L-RED 63: dpass 0 on 29 instances).

### 3.5 Lemma SAME-SUFFIX and Lemma STEP-BOUND (PROVED; [VJ], LOC-GATE3, NO-TIE3, [HOW])
SAME-SUFFIX. Let W be a window of steps inside one Λ-interval of a vertex o, y a vertex, and for every successor f of o a path P_f from f
to y, all constant on W, such that at every t ∈ W, P_t(f) = P_f · P_t(y) and P_t(y) avoids every P_f. Then the ⊴-order of the
successors' values is the same at every t ∈ W; so σ̄_t(o) is constant on W if o is Odd, and σ_t(o) is constant on W from W's second
step on if o is an Even mover.
Proof. Fix f, f′. Both plays end in y's cycle: equal Λ. [VJ] compares the sets of vertices more relevant than Λ by the most relevant
vertex of their symmetric difference; since P_t(y) is common to both and disjoint from both prefixes, that difference is the part of
P_f Δ P_f′ above Λ, constant on W (Λ is constant on W). If it is empty, [VJ] compares lengths, whose difference |P_f| − |P_f′| is
constant. So each pairwise comparison is constant. Odd plays the unique ◁-least face (LOC-GATE3, NO-TIE3); an Even mover switches at t
to a ▷-best option for the values at t − 1 ([HOW]); both are constant. ∎
STEP-BOUND. For every vertex x, S(x) ⊆ {t : some vertex of P_(t−1)(x) changes successor at t}, so ch_x = |S(x)| ≤ T. ∎ (A value is a
function of the play; a play changes only if a successor on it changes.)

### 3.6 Lemma PARALLEL (PROVED; [OPT], F3, E-MON3, positional plays)
Let s − 1, s lie in one Λ-interval J of b (Λ = w), y ≻ w, H_(s−1) ≠ H_s, x := the top of H_(s−1) Δ H_s, Z := H_(s−1) \ H_s (EXPELLED
letters), u′ := the first vertex of P_s(b) whose successor differs at s − 1 (b's split). Then (i) x ∈ P_s(b) \ P_(s−1)(b) and every
z ∈ Z lies in P_(s−1)(b) \ P_s(b); (ii) z ≺ x for every z ∈ Z; (iii) every z ∈ Z lies strictly after u′ on P_(s−1)(b), and x lies
strictly after u′ on P_s(b).
Proof. E_r(b) is the set of e-vertices of P_r(b) more relevant than w (F3), and every letter of U_y is above w. E-MON3: the top enters,
so x ∈ H_s \ H_(s−1); being an e-vertex above w, x is on P_s(b) and not on P_(s−1)(b). Likewise z ∈ H_(s−1) \ H_s is on P_(s−1)(b) and
not on P_s(b). (ii): x is the most relevant element of the difference, which contains z. (iii): the two plays agree up to and including
u′ (positional strategies; u′ is the first vertex whose successor differs), so a vertex of that common prefix is on both plays. ∎

### 3.7 Lemma PAIR-EXPEL and Corollary EXPEL-COUNT (PROVED-CONDITIONAL on P-N5-SPLIT §2 (a); premises as in the table)
Let s < s′ in J be two expulsions of the same z at b (z ∈ H_(r−1) \ H_r, r = s, s′) whose splits (§3.6) are the same pair (u′, b′)
(u′ is b's split at both, b′ its new successor at both); a′ := u′'s successor at s′ − 1 (a′ ≠ b′). Then E_s′(b′) ∩ U_z >lex E_s(b′) ∩ U_z.
Proof.
- Λ: b′ lies on P_s(b) and P_s′(b) after u′, so Λ_s(b′) = Λ_s′(b′) = w; by F1, F2 (Λ monotone, distinct rewards) Λ(b′) = w on [s, s′].
  The same holds for u′, and for a′ at s′ − 1 (on P_(s′−1)(b)).
- Step 1: Ω_(s′−1)(a′) ▷ Ω_s(b′). If u′ is a mover: σ_s(u′) = b′ ≠ σ_(s′−1)(u′) = a′, so u′ leaves b′ at a first s″ ∈ (s, s′ − 1]; then
  (P-N5-SPLIT §2 (a), with F1, STRICT, F4′, CN2-3) Ω_(s′−1)(u′) ⊵ Ω_s″(u′) ▷ ext(u′, Ω_(s″−1)(b′)) ⊵ ext(u′, Ω_s(b′)), and F4′ gives
  the claim. If u′ is a gate: its successors are its two faces, a′ the other one; at s Odd plays b′, so Ω_s(b′) ◁ Ω_s(a′) (LOC-GATE3,
  NO-TIE3), and F1 on a′.
- Step 2: E_(s′−1)(a′) ∩ U_z ⊵lex E_s(b′) ∩ U_z. Both values have Λ = w; [VJ] decides Step 1 by the most relevant vertex d of the
  symmetric difference of the Π's. If d ≻ z, d is an e-vertex ((E-DOM); c_W is in no Π; K0 / K3 by (Core)), even, so d ∈ E_(s′−1)(a′):
  strict lex on U_z. If d ≼ z, the two sets agree on U_z.
- Step 3: E_s′(b′) ∩ U_z >lex E_(s′−1)(a′) ∩ U_z. P_(s′−1)(b) and P_s′(b) agree up to u′; u′ is not an e-vertex (F6: e-vertices have one
  successor), so E_(s′−1)(b) = A ⊔ E_(s′−1)(a′) and E_s′(b) = A ⊔ E_s′(b′) with the same A. The change of E(b) at s′ has top x′ ≻ z
  (§3.6 (ii)), x′ ∈ E_s′(b), and the two sets agree above x′; on U_z the top of the difference is x′, on b′'s side.
- Steps 2, 3 and transitivity of lex order on subsets of U_z. ∎
Corollary EXPEL-COUNT. a_z(b, J) ≤ 1 + Σ_(u′,b′) Dhi_z(b′, J_b′) ≤ 1 + 3M·max Dhi_z. Proof: every run of z in H on J but the last ends with
an expulsion; by PAIR-EXPEL the values E(b′) ∩ U_z at the expulsions through one pair are pairwise distinct and lie in one Λ-interval
J_b′ of b′; the pairs are edges out of movers and gates (≤ 3M; L-RED R228 §2). ∎

### 3.8 Corollary A*-EQUIV (PROVED-CONDITIONAL on P-N5-SPLIT's SPLIT-COUNT and P-N5-CHAIN's C-EQUIV)
(i) C ≤ A*_all and A*_all ≤ 1 + M·C (L-NEW, N5-CORE-forms §3 (5): cited, not re-proved here; uses E-MON3 only).
(ii) C ≤ 3M·(1 + M·A*_route). Proof: for a route tuple (b, J, y), Dhi_y(b, J) − 1 = #changes of H on J (E-MON3: H strictly lex-rises at
each change); each change is an entry of its top x into H, which starts a new run of x, so Dhi_y(b, J) − 1 ≤ Σ_(x ∈ U_y) a_x(b, J) ≤
M·A*_route; SPLIT-COUNT sums ≤ 3M such terms. ∎
(iii) Hence T3 polynomial ⟺ C ⟺ A*_all ⟺ A*_route polynomial (with C-EQUIV). F1 fix (L-RED 62): box 91's «A*» column was A*_route; the
equivalence C ≤ A* needs A*_all (take b = v); both are stated here with their names.

## 4. Overlaps (cite, do not duplicate)
- L-RED 63, R229-box203 §3 (claude/l-red 8c034440): Lemma CLASS-PAYS and Corollary GATE-FLIP-MIN, PROVED (L-RED lane) on IDEAL-CYC:
  each relock is paid by a CLASS (Λ, E) change of e_g, each unlock by one of β_g: flips(g) ≤ 2·min(D^tot(e_g) − 1, D^tot(β_g) − 1) + 1.
  On IDEAL-CYC this is STRONGER than §3.4 (d) (class changes ≤ value changes); on MWR both are exact. §3.4 (d) is the VALUE form and is
  stated for Γ3 as well. L-RED 63 R229-box93 §1.3: Lemma REL-G (no γ-only payment of a relock with UP_(t−1)); it closes TRIGGER's (γ)
  for those relocks.
- L-NEW 68, N5-FLIP-box203 (claude/l-new 764a8f86): Theorem GATE-CLASS (a gate flip changes the class of one face), Corollaries GATE-FLIP
  (sum form) and QUIET-N, PROVED (L-NEW lane) on IDEAL-CYC from landed premises; its Case 2a is GATE-LOW-NULL's argument, its Case 2b is
  NP-SHAPE. CLASS-PAYS names the paying face; GATE-RACE (a) here is the value-level version of the same fact.
- L-NEW N5-CORE-forms (claude/l-new 14babccb): the core forms; §3.8 (i) is its (5).

## 5. DEAD list (instances frozen; sha1 = first 8 hex of the file at the named commit; DATA, two engines unless said)
| design | what dies | instance(s) | sha1 | where |
| --- | --- | --- | --- | --- |
| WC waiting High (route avoiding h_(k−1), SUPERSET) | T3 = 4 at n = 4, 8, 16 | WC4_2, WC16_2 | e7569f92, 995e7132 | box90 inst / box91 inst |
| RA-MULT(K) (constant re-arm multiplicity) | m = n, C = 2n + 1 | MW8_2, MW32_2 | 66b84dcb, 445031d1 | box91 inst |
| polynomial P bound (RA path count) | P = F_(d+2) − 1 with C = 3 | FW8_2, FW16_2 | 108a63cf, 94df42b7 | box91 inst |
| K6 LAG TOWER (merged lagging copy) | CNT ≤ 4 / 3 / 2 / 2 at h = 2 / 3 / 4 / 5 (and h = 6, L-RED lag229, own only) | LT2_* … LT3_* (box 86); LT4_1_0, LT4_1_1, LT4_m1_0, LT4_m1_1, LT5_1_0, LT5_1_1, LT5_m1_0, LT5_m1_1 | box 86 pins.sha1; c14fdb03, 779e1826, 6da63578, 25d4a99f, 458b98d2, d555a6f7, d0124778, 3909c38b | box86 inst; box93 k6/inst |
| K7 probe (High continuation on the race) | C = 2 at n = 4, 8, 16 | Ku_4, Ku_8, Ku_16, Kprev_8 | 1ef4b24c, 54d01b0e, b43e49cd, 9b814f97 | box93 inst |
| K1-FLIP(c), every constant c, at k = 1 (L-RED 63) | flips 2n + 1 with lamch 0 | MWR4_2, MWR8_2, MWR16_2 | 856d369b, 918f1414, 2ccda9a9 | box93 inst (copies of claude/l-red 406ef2fd r229/inst) |
| nesting multipliers (H = 2, 3) | C, max flips, T3 of one MW(n) (simultaneous) or the sum (sequential) | NP*, NV*, ND*, NDV*, NDB*, NSQ2_4, NSQ3_4 (22) | box94 inst/SHA1SUMS (e.g. NP3_8 84a331ba, NDV3_8 65f67838, NSQ3_4 b894e899) | box94 inst |

## 6. DATA, tools and controls (not to sign)
- Engines (two on every number): own = L-RED R221 own.py (claude/l-red 4b309716; IDEAL-CYC Howard on Γ, the genome's start); g3 = L-NEW's
  Γ3 N5′-xi from S3 (gamma3 / n5v / n5x / eg195 at claude/l-new fcba92fc; box91/pins.txt). Tools (claude/l-si, this commit's tree):
  box91/mult91.py, box92/gate92.py, box92/astar92.py, box93/np93.py, box94/lev94.py; checks check91-94.sh (wired in experiments/si/check.sh).
- Counters (unit; set; scope; TOTALS unless «max»): all must-be-0 counters are 0 on both engines, rows IDENTICAL:
  - §3.1: grfail, gr2fail, grwhy, trfail (unit gate, whole run; box 91's 11 instances; own to the end cap 3000, g3 to the first fallback cap 20000).
  - §3.2: decfail, glnfail, lowflip (unit (gate, t); same set; lowch up to 599 changes below e_o never flip a gate).
  - §3.3-§3.4: npside, npsub, npboth, npkind, relfail, unlfail, dfail (proxy), k1both = k1c2 (unit gate; box 91's 11 + k1fail_202 + Ku_8,
    Ku_16, Kprev_8 + MWR4/8/16_2; 18 instances); relG 0 (relocks paid below every e-letter).
  - §3.5: lev94 (unit level; box 94's 22): copy rows S(R_j) = S(R_(j−1)), flips(g_Qj) 0 on NDV / NDB.
  - §3.6-§3.7: par1-3, lexfail, afail, pxfail, dhifail, pefail, ecfail, pelam (unit change of H / tuple (b, J, y) / same-pair couple;
    box 91's 11; 28 / 496 / 10 / 121 / 103 / 74 couples).
  - §3.8: cfail (c_y > a_y) 0 (astar92; unit (v, I, z)).
- Controls (fire; own engine): CTRL=gr (GATE-RACE bound − 1) 8 on MW8_2; CTRL=low (π below e_o) glnfail 26 on C6G8_n54; CTRL=pre (par3 on
  the whole old play) 58 / 80; CTRL=a0 afail 14 / 96; CTRL=uz (U_z := ∅) pefail on every couple; CTRL=swap relfail 4 on C6G8_n54;
  CTRL=tight relfail 176 / 92 on MW8_2 / C6G8_n54; check94 fails on an altered lev94 row.
- Growth (per-tuple maxima): C, A*_all, max gate flips linear on every family (MW(n): C = 2n + 1, flips 4n + 2, A*_all 2n + 2; MWR(n):
  flips 2n + 1, C = n + 1; climbed instances C ≤ 6). Exact per-gate tightness of §3.4 (a) / (d): MW race gate, MWR.
- Independent re-measurement by L-RED (own code): R228-box91 (expel228, 19,436 couples), R229-box92 (gate229, 20 instances),
  R229-box93 (e93_229, 29 instances; exact dexact for (b)), R229-box203 (cls229).

## 7. Against TARGET.md (READING, not to sign)
- These are lemmas about one algorithm's run (Howard / VJ on Γ3(G) from S3 = N5′-xi's mover phase; and on IDEAL-CYC(G)), for every genome.
  They are reductions: each bounds a gate's flips or a letter's presences by another per-vertex quantity of the same run. None bounds T3,
  C or A*_all by a polynomial; G-N5-TIME stays OPEN; nothing here is an M3 / M4 claim or a gauntlet step-4 pass. The only polynomial class
  in the background is R122's Ξ-acyclic one (P-ACYC), not extended here. The conditional labels (§3.7, §3.8) wait on P-N5-CHAIN (R125)
  and P-N5-SPLIT; §3.1-§3.6 use only P-N5-CHAIN's facts on Γ3 and their landed R118 / R121 / R123 counterparts on IDEAL-CYC.

## 8. Attack record (relayed by the Lead; I have not re-run L-RED's tools)
- L-RED 62 R228-box91 (claude/l-red f3903cb8): PARALLEL, PAIR-EXPEL, EXPEL-COUNT, GATE-RACE, TRIGGER, A*-EQUIV SURVIVE; F1 (A*_all vs
  A*_route) fixed in §3.8; F2 (TRIGGER (γ)) answered by GATE-LOW-NULL (b) on LAM ∧ PRIV ∧ UP and by WAIT-QUIET elsewhere.
- L-RED 63 R229-box92 (claude/l-red 406ef2fd): GATE-LOW-NULL SURVIVES; scope corrected to LAM ∧ PRIV ∧ UP (§3.2); «below» named K10.
- L-RED 63 R229-box93 (claude/l-red 8c034440): NP-SHAPE, E-FACE-PAYS, WAIT-QUIET SURVIVE; vacuous clause dropped (§3.3); REL-G added (§4).
- SAME-SUFFIX (box 94): attack pending (routed to L-RED 63 at 06:33Z).
