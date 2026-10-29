# P-N5-CORE (box 23): every in-phase transition switches an Even vertex; a switch raises the switcher's value; a clean gate change raises the abandoned option's value; and fresh-edge counting reduces interval lengths to return-only transitions
L-SI successor 19 (Opus 5.5; D15, D18, Lead reading L40). Packet for the referees, frozen at its push (the sha1 goes to the Lead). Lead's
instruction of 2026-10-28 22:06Z: freeze the §11 PROVED core (C1)-(C6) of docs/si/N5-ALT-box23.md as a packet, self-contained, premises quoted from
LANDED RESULTS, with a "What to sign" section and a scope line. Working note: docs/si/N5-ALT-box23.md (§1, §3, §7, §11; data, DEAD items, readings).
Labels (D18 / L40): PROVED (lane, unrefereed). Not a TARGET.md claim.
Scope (D1): elementary reductions inside one phase of N5 on EVERY game. They bound nothing by themselves: no bound on the number of switches
per vertex, on Ξ-changes per vertex, on return-only transitions or on the phase length is claimed. The per-vertex forms XR-LIN and SW-LIN are
DEAD (N5-ALT §8, §10), with instances. G-N5-TIME stays OPEN.
Quotes: every [Q path@commit:lines] «…» is verbatim from the tagged source, checked by experiments/si/rund/quotecheck.py (pinned in
experiments/si/check.sh, with a shifted-line control that must fail). RESULTS and SPEC are quoted at trunk 33f43c20.

## 0. What to sign
| item | statement in one line | premises (all LANDED) |
| --- | --- | --- |
| (C1) EVERY-SWITCH | every transition of a phase changes σ | SPEC S2, S4; RESULTS R38 (a) |
| (C2) PHASE-SW | a phase P has |P| ≤ Σ_w SW_P(w) | (C1) |
| (C3) RISE-SW | an Even switch at w, w off honest cycles at t and t + 1, strictly raises Ξ(w) | SPEC S1, S2; (SW); RESULTS R15 (a), (d); R38 (a) |
| (C4) RISE-GATE-CLEAN | a clean σ̄ change y1 → y2 at u raises κ(y1), strictly unless a tie at t + 1 | RESULTS R56 (a) (Aκ), (M2κ); R56 (d) κ-Y-FORM_D |
| (C5) FRESH-RED | an interval I of a phase has |I| ≤ m_E + NOFRESH(I) | (C1) |
| (C6) FRESH3-COUNT | on a global C-interval: fresh-Even-edge, fresh-option and A-shrink transitions are ≤ m_E, ≤ Σ deg, ≤ n | definitions; P-N5-GCX §1 (transition-local reading) |
Not to sign: §6 (data pointers, conditional form of (C4), readings).

## 1. Setting and premises (every game)
- N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md, FIX 1-4) with the standing premise 1E-N3. A PHASE: a maximal run of states with λ_Ξ and τ
  constant: [Q docs/RESULTS.md@33f43c20:1825-1826] «(a) Remark KEY (every game): λ_U is a function of τ alone, so on every run of states with τ
  constant it is constant; a (λ_Ξ, τ)-phase is exactly a joint λ-phase (λ_Ξ, λ_U, τ)». A transition t → t+1 of a phase P joins two states of P.
- SPEC S2: [Q docs/new/N5-ssi-global.md@33f43c20:47] «Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than Ξσ(σ(v))}».
- SPEC S4 (one iteration, the fallback): [Q docs/new/N5-ssi-global.md@33f43c20:50] «S4 Iteration (one iteration = one pass with Iσ ∪ Iτ ≠ ∅» and
  [Q docs/new/N5-ssi-global.md@33f43c20:56-57] «c. FALLBACK, if σ_new = σ and τ_new = τ: if Iσ ≠ ∅, for every Even v with an improving edge set
  σ_new(v) = the w with (v, w) ∈ Iσ maximising (Ξσ(w), w) (best valuation, ties: larger index); otherwise do the same for Odd on Iτ».
- (SW), landed among R72's premises: [Q docs/RESULTS.md@33f43c20:3768-3769] «(SW): every Even switch of N5 is to an edge of Iσ».
- Monotonicity, R15 (a), (d): [Q docs/RESULTS.md@33f43c20:631] «(a) Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4),
  Ωσ ⊴ Ω_{Switch_I(σ)}.» and [Q docs/RESULTS.md@33f43c20:640] «(d) N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ». Ωσ is Ξσ,
  so Ξ_t ⊴ Ξ_{t+1} pointwise at every transition at which τ is unchanged (Ξ is σ's valuation against Odd's optimal reply).
- Valuations (SPEC S1): the valuation of v's honest play is (c, P, ℓ). If v is not on its play's cycle, Ξ(v) = v ⊕ Ξ(next v), where v ⊕ adds v
  to P when rank(v) > rank(c) and adds 1 to ℓ (next = σ at Even, σ̄ at Odd vertices).
- Per honest class c of the phase, U_c := λ^{-1}(c), κ as in RESULTS R56: [Q docs/RESULTS.md@33f43c20:2851] «(a) Facts (Aκ), (A0κ), (M1κ), (M2κ),
  (INJ), (SP′) per honest class», with (Aκ) as stated in its source packet: [Q docs/new/P-N5-FBRED-box44.md@3732ab55:49-50] «(Aκ): for z ∈ U_c ∖ {c}:
  λ_t(z) = c ≠ z, so (V1) gives Ξ_t(z) = z ⊕ Ξ_t(next_t z) with cycle node c; next_t(z) ∈ U_c, and κ_t(z) = κwt_c(z) + κ_t(next_t z)». (M2κ) is
  κ_t(z) ⪯ κ_{t+1}(z) for z ∈ U_c at in-phase transitions; (M1κ): for valuations with cycle node c, x ⊴ x′ ⇔ κ(x) ≤ κ(x′).
- κ-Y-FORM_D: [Q docs/RESULTS.md@33f43c20:2858-2859] «(d) κ-Y-FORM_D (per q ∈ Q ∩ U_c, q ≠ c, at a state t where q lies on no honest cycle): κ_t(q) =
  κwt_c(q) + min over y ∈ Y^q_t of κ_t(y), with Y^q_t := {y ∈ succ(q) ∩ U_c : y's honest play at t avoids q}».
- Global C-interval: a maximal run of consecutive GOOD transitions, read transition-locally as in docs/si/P-N5-GCX-fixes-box21.md F2 (signed
  reading of both referees of P-N5-GCX): t → t+1 is good if for every class c, A_{t+1} ⊆ A_t (of U_c), D_{t+1} = D_t, DD_{t+1} = DD_t and Δ is
  constant on DD_t. D_t := {Odd u : σ̄_t(u) ≠ τ(u)}; A_t (of U_c): the vertices of U_c whose (σ_t, τ)-play meets no vertex of D_t.

## 2. (C1) EVERY-SWITCH and (C2) PHASE-SW (PROVED, elementary)
Statement (C1). At every transition t → t+1 of a phase, σ_{t+1} ≠ σ_t.
Proof. A transition is one iteration, so Iσ ∪ Iτ ≠ ∅ at t (S4). τ_{t+1} = τ_t, since the phase has τ constant (R38 (a)). If the iteration is not a
fallback, then (σ_new, τ_new) ≠ (σ, τ) (S4c fires exactly when both are unchanged), so σ_new ≠ σ. If it is a fallback with Iσ ≠ ∅, every Even v
with an improving edge gets σ_new(v) = some w with (v, w) ∈ Iσ, and w ≠ σ(v) by S2; at least one such v exists. A fallback with Iσ = ∅ changes
τ (Odd's switch-all on Iτ ≠ ∅, again to edges w ≠ τ(v)), which cannot happen inside a phase. □
Statement (C2). For a phase P and an Even vertex w, let SW_P(w) be the number of transitions of P at which σ(w) changes. Then |P| ≤ Σ_w SW_P(w).
Proof. Each transition is counted at least once on the right, by (C1). □

## 3. (C3) RISE-SW (PROVED)
Statement. Let t → t+1 be a transition of a phase, w an Even vertex with y := σ_{t+1}(w) ≠ σ_t(w), and suppose w lies on no honest cycle at t
and at t + 1. Then Ξ_{t+1}(w) ▷ Ξ_t(w).
Proof.
- y ∈ Iσ_t(w) by (SW), so Ξ_t(y) ▷ Ξ_t(σ_t w) (S2: strictly better).
- Ξ_{t+1}(y) ⊵ Ξ_t(y) by R15 (a), (d) (τ is unchanged in the phase). So Ξ_{t+1}(y) ▷ Ξ_t(σ_t w).
- Both are valuations of plays that avoid w: y's honest (t+1)-play, because w is off the cycle of its play at t + 1 (so its play is w followed
  by y's, and y's does not return to w); σ_t(w)'s honest t-play, for the same reason at t.
- Both have the cycle node c := λ(w) (λ_Ξ is constant on the phase, and w's play is w followed by them).
- On valuations of w-free plays with cycle node c, w ⊕ · is strictly monotone: it adds the same vertex w to both path sets (when
  rank(w) > rank(c)) and 1 to both lengths, so the comparison (path set by top of the symmetric difference, then length in the direction fixed by
  c's parity) is unchanged.
- Hence Ξ_{t+1}(w) = w ⊕ Ξ_{t+1}(y) ▷ w ⊕ Ξ_t(σ_t w) = Ξ_t(w). □
- Remark. The order of the steps matters: Ξ_t(y) itself may be the valuation of a play through w, where w ⊕ is not defined as an extension.
- Consequence (with (C2)): |P| ≤ Σ_w XR_P(w) + #{(w, t) : w switches at t and lies on an honest cycle at t or t + 1}, XR_P(w) := the number of
  transitions of P at which Ξ(w) changes.

## 4. (C4) RISE-GATE-CLEAN (PROVED; landed premises only)
Statement. Let t → t+1 be a transition of a phase, c a class, u ∈ Q ∩ U_c, u ≠ c, on no honest cycle at t and at t + 1, with y1 := σ̄_t(u) ≠
y2 := σ̄_{t+1}(u). Suppose the change is CLEAN: y2 ∈ Y^u_t and y1 ∈ Y^u_{t+1}. Then κ_{t+1}(y1) ⪰ κ_t(y1), strictly unless κ_{t+1}(y1) = κ_{t+1}(y2).
Proof.
- At t: (Aκ) gives κ_t(u) = κwt_c(u) + κ_t(y1) (next_t(u) = y1). κ-Y-FORM_D gives κ_t(u) = κwt_c(u) + min over Y^u_t. So κ_t(y1) is that minimum, and
  κ_t(y1) ⪯ κ_t(y2), as y2 ∈ Y^u_t.
- At t + 1, the same with y2 = next_{t+1}(u) and y1 ∈ Y^u_{t+1}: κ_{t+1}(y2) ⪯ κ_{t+1}(y1).
- (M2κ): κ_t(y2) ⪯ κ_{t+1}(y2).
- Chain: κ_t(y1) ⪯ κ_t(y2) ⪯ κ_{t+1}(y2) ⪯ κ_{t+1}(y1), and the last step is strict unless κ_{t+1}(y2) = κ_{t+1}(y1). □
- So, ties at t + 1 aside, every clean σ̄ change at u is a strict Ξ-rise of the abandoned option at the same transition (Ξ and κ order the class
  alike, (M1κ)). Each such rise of y1 at t is charged by at most the number of Odd vertices u with σ̄_t(u) = y1.

## 5. (C5) FRESH-RED and (C6) FRESH3-COUNT (PROVED, elementary)
Statement (C5). Let I be a set of consecutive transitions of one phase. Call t → t+1 ∈ I FRESH if some Even w switches at it to an edge (w, y)
that w held at no earlier state of I (the first state of I included), and let NOFRESH(I) count the other transitions of I. Then |I| ≤ m_E +
NOFRESH(I), m_E the number of Even edges.
Proof. Map each fresh transition to one of its fresh edges. An edge is fresh at most once in I, so the map is injective. □ ((C1) makes every
transition of I a switching one, so the non-fresh ones are exactly those at which every switching Even vertex returns to an edge it held
before in I.)
Statement (C6). Let I = [a, b] be a global C-interval (§1). Among the transitions of I:
- those with a fresh Even edge (in I's scope) number ≤ m_E;
- those at which some Odd vertex moves σ̄ to an option it did not hold at an earlier state of I number ≤ Σ_{Odd u} (deg(u) − 1);
- those with A_{t+1} ⊊ A_t for some class number ≤ Σ_c |A_a(U_c)| ≤ n.
Proof. The first two are injective maps to (vertex, option) pairs not held at a, as in (C5). For the third: on a global C-interval A_{t+1} ⊆ A_t
for every class at every transition (good transitions), so each vertex leaves A at most once in I, and each strict shrink removes one. □

## 6. Not to sign: pointers
- DATA for the signed items (experiments/si/root/corecheck.py; log root/logs/corecheck.txt; 0 violations): alt_all (413 games, n ≤ 600) 8,084
  in-phase transitions, (C1) at all, (C3) at 16,883 off-cycle Even switches, (C4) at 3,077 clean gate changes (1,165 unclean ones not checked);
  lib41 (n ≤ 48, S3) 6,104 transitions, (C3) 11,771, (C4) 801 clean. Control MUT=1 ((C3) demanded of the new successor's own Ξ) bites: 167 of 202
  on nep90_n40.
- The UNCLEAN gate change: N5-ALT §1 RISE-GATE drops the clean hypothesis using BEST (Fact CL, a proof step of P-N5-OFFMONO §1, in review). Not
  claimed here.
- DATA (N5-ALT §2, §3, §7): every gate change in alt_all and lib41 raised the abandoned option (one unchanged case in 3,420); NOFRESH ≤ 22 per run;
  the conjecture FRESH3 (every σ̄-changing in-interval transition has one of (C6)'s three events) held on 1,590 of 1,592 and is DEAD on ret14_n48.
- DEAD per-vertex forms: XR-LIN (N5-ALT §8, l121reader_n41: one vertex's Ξ changes 86 > 2n times in a phase; reproduced by REFEREE and by
  L-COMP's engine) and SW-LIN (§10, swlin_kill_n26: one Even vertex switches 27 > n times in a phase; L-COMP's n5b agrees). So (C2) and (C3)'s
  consequence cannot be completed by a linear per-vertex bound. READING (§8, §12): per-vertex counts can be raised by passive READER vertices
  (Theorem READER-INV of REFEREE, under its condition (R)); the number of transitions of a phase cannot.
