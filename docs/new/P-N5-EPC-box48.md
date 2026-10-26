# Packet P-N5-EPC (box 48): a fallback raises the honest level of every configuration at its next visit (RET-FB), so a configuration has O(n²) epochs per phase plus its fallback-free returns (VIS, EP-C); a saturated fallback ends the phase or retires its configuration (SAT-FB), so f ≤ n·|𝒞_f| (FB-C′); and the epoch count reduces to X_dir, X_big, the multi-gate configurations and their fallback-free returns (EP-ASM) — every game
L-NEW successor 27 (Opus 5.5), D14 / D18, Lead reading L40; Lead's word of 14:32Z (Lead's stamp): "GO: freeze P-N5-EPC-box48 NOW. The FBC reviews
do not block it: it is a separate packet, and it should be self-contained rather than cite FBC." Written 2026-10-26 14:34Z onward (date -u).
FROZEN at push: later text goes into a fixes file.
Source: docs/new/N5-NCONF-box48.md (working doc, l-new 29d8deeb … 98d02d85; this packet governs). Tools: experiments/new/box48/ (nconf.py,
vislev.py, retfb.py, satfb.py, r0shape.py, ncclimb.py, laps.py).
Labels: PROVED (L-NEW 27, unrefereed) / IMPLICATION / DATA / DEAD / OPEN / READING. Not a TARGET.md claim. Nothing here bounds N5's running time
on any class; G-N5-TIME stays open. Pinned at trunk f4562054 (merged into l-new before the freeze); every quote is checked there (§7).

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Lemma FB-RISE_C (restated with proof): an in-phase fallback from a C-state raises LEV_C by one | PROVED (to sign) |
| §1 | Lemma SAT_C (restated with proof): at a saturated C-state Ξ = B_C, and Ξ is constant up to any later C-state | PROVED (to sign) |
| §2 | Lemma RET-FB: after an in-phase fallback t → t + 1, LEV_C(s) ≥ min(LEV_C(t) + 1, n − 1) at every later C-state s, for EVERY configuration C | PROVED (to sign) |
| §2 | Corollary VIS: V_C ≤ 2n² − n + R⁰_C epochs of C per phase; Theorem EP-C: N_ep ≤ NCONF·(2n² − n) + R⁰ | PROVED (to sign) |
| §3 | Lemma SAT-FB, Corollary SAT-FB1 (≤ 1 saturated fallback per configuration), Theorem FB-C′: f ≤ n·|𝒞_f(P)| | PROVED (to sign) |
| §4 | Corollary EP-ASM: N_ep ≤ (4n² − 3n) + (1 + 4n² − 3n + X_dir + X_big)(T*_Q + 2) + NCONF_{≥2}·(2n² − n) + R⁰_{≥2} | PROVED as an assembly; its second term is an IMPLICATION from (Στ) (to sign as such) |
| §5 | the remark (elementary) D changes + 1 ≤ N_ep; DEAD: "a saturated fallback is flat and ends the phase" (rho3_253_n32) | PROVED / DEAD (to sign the remark; the DEAD item is data) |
| §6 | data, open items | DATA / OPEN / READING (not to sign) |
- Premises (LANDED, or signed by both referees and awaiting landing):
  - SPEC S1-S5 of docs/new/N5-ssi-global.md (FIX 1-4); in particular S2, S4a's "Else σ_new = σ.", S4c, S5 and FIX 3 (quotes §7). Standing premise
    1E-N3 (RESULTS R57), with R57 (a) (VJ) the bridge from SPEC's Ξ to VJ00's Ω.
  - (MON): RESULTS R15 (a) (with R15 (d)): Ξ is non-decreasing along a run.
  - RESULTS R17 (a) (V1), (V2) (box 10 l. 20-21); RESULTS R17 (b) Lemma P, Case A only (A1, A2), with Ω := Ξ_t.
  - P-N5-HONFF (signed by both referees, no gap; Q-A answered YES by both; notes in docs/new/P-N5-HONFF-fixes-box47.md, sha1 ccc520dd…): Lemma
    FB-RISE (a)'s items 2 and 3, and Corollaries HON-0-FF (b) and REC-1-FF (c) (§4 only).
  - P-N5-HON = RESULTS R68: HON-FB (iv)'s last-state argument (§3); the definitions of X_dir, X_big, T*_Q, (Στ) (§4).
  - RESULTS R64 (the epoch); RESULTS R38 (a) (the phase).
  - Not a premise: P-N5-FBC (under review). Its FB-RISE_C and SAT_C are restated here with their proofs (§1), so this packet does not depend on
    its review. REFEREE 15's FBC report proves SAT-FB1 by another route (§3, remark); cited as a referee note, not as a premise.

## 0. Setting (every game)
N5 = SPEC S1-S5. State k = (σ_k, τ_k); σ̄_k = S1's Odd counterstrategy to σ_k; Ξ_k := the value of the HONEST play (σ_k at Even, σ̄_k at Odd
vertices); λ := Ξ's cycle-node map. A PHASE P: a maximal run with (λ, τ) constant (RESULTS R38 (a)); an in-phase transition has both ends in P;
f := the in-phase S4c fallbacks of P. value(r) := (u, P(r), |r|) for a simple path r ending at a cycle node u of λ (R17 Lemma P). Q := the Odd
vertices of out-degree ≥ 2. A CONFIGURATION is C = σ̄|Q; k is a C-STATE if σ̄_k|Q = C. σ̄_C(v) := C(v) for v ∈ Q, the unique successor otherwise.
H_C := G with every Odd v cut to its edge σ̄_C(v). At a C-state the honest play from every vertex is a play of H_C, so Ξ_k = σ_k's valuation in
the one-player game H_C. LEV_C(k) := the largest j ≤ n − 1 with Ξ_k(x) ⪰ value(r) for every vertex x and every simple H_C-path r from x to a
cycle node of λ with ≤ j edges; defined at EVERY state of P (C need not be k's configuration); non-decreasing on P, since H_C and λ are fixed on
P and Ξ is non-decreasing ((MON)). SATURATED: LEV_C = n − 1. B_C(x) := the maximum of value(r) over all simple H_C-paths r from x to a cycle
node of λ. An EPOCH: a maximal run of P with σ̄|Q constant (RESULTS R64); N_ep(P) their number; D_E := {q ∈ Q : σ̄_E(q) ≠ τ(q)}. NCONF(P) := the
number of distinct configurations of P's states; NCONF_{≥2}(P) := those with |D_C| ≥ 2. For a configuration C: its epochs E_1 < … < E_V
(V = V_C) with first states s_1 < … < s_V; a RETURN is a pair (i, i + 1). 𝒞_f(P) := the configurations of the sources of P's fallbacks.

## 1. Lemma FB-RISE_C and Lemma SAT_C (PROVED, every game; restated from P-N5-FBC-box47 with their proofs)
Lemma FB-RISE_C. Let t → t + 1 be an in-phase S4c fallback of P whose source t is a C-state. Then LEV_C(t + 1) ≥ min(LEV_C(t) + 1, n − 1).
Proof. Let x be a vertex, u a cycle node of λ, r a simple H_C-path from x to u with |r| ≤ min(LEV_C(t) + 1, n − 1). If |r| = 0, x = u and
Ξ_{t+1}(u) = (u, ∅, 0) = value(r). Otherwise r = x → z → r′, r′ avoids x, |r′| ≤ LEV_C(t), so Ξ_t(z) ⪰ value(r′).
- x Odd. z = σ̄_C(x) = σ̄_t(x) (t is a C-state), so x's honest play at t is x followed by z's. If λ(x) ≠ x, (V1) gives Ξ_t(x) = x ⊕ Ξ_t(z) with
  z's path to λ(x) avoiding x, and (V2) (r′ avoids x) gives Ξ_t(x) ⪰ x ⊕ value(r′) = value(r). If λ(x) = x, Ξ_t(x) = (x, ∅, 0) and z's honest play
  returns to x, so Ξ_t(z) has cycle node x while value(r′) has cycle node u ≠ x; Ξ_t(z) ⪰ value(r′) makes x better than u, and (x, ∅, 0) ≻
  value(r). Then Ξ_{t+1}(x) ⪰ Ξ_t(x) (MON).
- x Even. Items 2 and 3 of the proof of FB-RISE (a) (P-N5-HONFF §1) verbatim, with G_τ replaced by H_C. They use only: the edge (x, z) of G
  (Even vertices keep all their edges in H_C), Ξ_t(z) ⪰ value(r′), the fallback rule (S4c: z*(x) is the (Ξ_t(w), w)-maximum of Iσ_t(x); FIX 3),
  Lemma P's Case A with Ω := Ξ_t (Q-A, YES from both referees), (MON), (V1)/(V2) at t + 1 and λ_{t+1} = λ. None of them uses the frame of r′.
  They give Ξ_{t+1}(x) ⪰ value(r). □
Lemma SAT_C. (1) If t is a C-state of P with LEV_C(t) = n − 1, then Ξ_t = B_C. (2) If t < t′ are C-states of P with LEV_C(t) = n − 1, then Ξ is
constant on t, …, t′.
Proof. (1) At a C-state the honest play from x follows a simple H_C-path r_x to its first visit of λ(x), so Ξ_t(x) = value(r_x) ⪯ B_C(x);
LEV_C(t) = n − 1 gives Ξ_t ⪰ B_C. (2) Ξ_t = B_C ⪰ Ξ_{t′} (t′ is a C-state, (1)'s first half) ⪰ Ξ_t (MON); so Ξ_{t′} = Ξ_t, and Ξ, being
non-decreasing, is constant on t, …, t′. □
(P-N5-FBC's SAT_C also bounds t′ − t by 4n(n − 1) through R15 (d); that part is used here only in Corollary VIS (a), with R15 (d) and R57 (a) as
its premises: τ is constant on P, so Ωτ is too, and R15 (d) allows at most 4n(n − 1) consecutive iterations with Ωσ = Ξ and Ωτ both unchanged.)

## 2. Lemma RET-FB, Corollary VIS, Theorem EP-C (PROVED, every game)
Lemma RET-FB. Let t → t + 1 be an in-phase S4c fallback of P, C ANY configuration, and s ≥ t + 1 a C-state of P. Then
LEV_C(s) ≥ min(LEV_C(t) + 1, n − 1).
Proof. Let L := min(LEV_C(t) + 1, n − 1). We show Ξ_s(y) ⪰ value(r) for every vertex y and every simple H_C-path r from y to a cycle node u of λ
with |r| ≤ L, by induction on |r|. |r| = 0: Ξ_s(u) = (u, ∅, 0) = value(r). Let |r| ≥ 1, r = y → z → r′; r′ avoids y and |r′| ≤ L − 1.
- y Even. |r′| ≤ L − 1 ≤ LEV_C(t), so Ξ_t(z) ⪰ value(r′) (LEV_C(t) ranges over all vertices, at every state). Items 2 and 3 of FB-RISE (a)'s
  proof, read in H_C as in §1, give Ξ_{t+1}(y) ⪰ value(r). (They do not need t to be a C-state: they use only G's edge (y, z), the bound on
  Ξ_t(z), S4c, Case A with Ω := Ξ_t, (MON), (V1)/(V2) at t + 1 and λ_{t+1} = λ.) Then Ξ_s(y) ⪰ Ξ_{t+1}(y) (MON; t + 1 ≤ s, both in P).
- y Odd. s is a C-state, so σ̄_s(y) = σ̄_C(y) = z and y's honest play at s is y followed by z's. By induction, Ξ_s(z) ⪰ value(r′). The Odd case of
  §1 at the C-state s (with t replaced by s) gives Ξ_s(y) ⪰ value(r).
So LEV_C(s) ≥ L. □
- What RET-FB adds to FB-RISE_C: the fallback may come from ANY configuration. Its relaxation of the Even vertices is frame-free, so it acts in
  every H_C at once; the Odd vertices catch up at the next state where they follow C. At a non-C state an Odd vertex with σ̄ ≠ C can sit below
  its H_C-paths (Odd's best reply undercuts them), which is why the bound is stated at C-states.
Corollary VIS. For every phase P and configuration C, V_C ≤ 2n² − n + R⁰_C, where R⁰_C := the returns (i, i + 1) of C with no in-phase fallback
source in [s_i, s_{i+1}) and LEV_C(s_i) ≤ n − 2.
Proof. Split the V_C − 1 returns.
- (a) LEV_C(s_i) = n − 1. Let i₀ be the least such i. By SAT_C (2) and R15 (d) (§1's last paragraph), every C-state t′ > s_{i₀} of P has
  t′ − s_{i₀} ≤ 4n(n − 1). Two C-epochs are separated by a non-C state, so s_{j+1} ≥ s_j + 2 and V_C − i₀ ≤ 2n(n − 1). LEV_C is non-decreasing, so
  these are all the returns of kind (a).
- (b) LEV_C(s_i) ≤ n − 2 and some in-phase fallback has its source t ∈ [s_i, s_{i+1}). Then t + 1 ≤ s_{i+1}, and RET-FB with (MON) gives
  LEV_C(s_{i+1}) ≥ min(LEV_C(t) + 1, n − 1) ≥ min(LEV_C(s_i) + 1, n − 1). LEV_C rises by ≥ 1 along each such return from a value in {0, …, n − 2}
  and never drops: at most n − 1 returns of kind (b).
- (c) the rest: R⁰_C.
V_C = 1 + #returns ≤ 1 + 2n(n − 1) + (n − 1) + R⁰_C = 2n² − n + R⁰_C. □
Theorem EP-C. For every phase P, N_ep(P) ≤ NCONF(P)·(2n² − n) + R⁰(P), R⁰(P) := Σ_C R⁰_C. Moreover R⁰(P) ≤ Σ_S REV(S) over the maximal
fallback-free runs S of P (at most f + 1 of them), REV(S) := (epoch starts in S) − (distinct configurations among them).
Proof. N_ep = Σ_C V_C; sum VIS over the NCONF(P) configurations. A return counted in R⁰_C has no fallback source in [s_i, s_{i+1}), so s_i, …,
s_{i+1} lie in one fallback-free run S, both epochs start in S, and a configuration with V′ epoch starts in S has at most V′ − 1 such returns. □

## 3. Lemma SAT-FB, Corollary SAT-FB1, Theorem FB-C′ (PROVED, every game)
Lemma SAT-FB. Let t be a C-state of P with LEV_C(t) = n − 1 whose transition t → t + 1 is an in-phase S4c fallback. Then t + 1 is the last state
of P, or P has no C-state after t.
Proof. Let t′ > t be a C-state of P. By SAT_C (2), Ξ_{t+1} = Ξ_t (t + 1 ≤ t′).
- Iσ_{t+1} = ∅. S2 reads Iσ at t + 1 with Ξ_{t+1} = Ξ_t. The fallback is Even's (in-phase, FIX 3). An Even x with Iσ_t(x) = ∅ keeps its edge, so
  Iσ_{t+1}(x) = Iσ_t(x) = ∅. An Even x with Iσ_t(x) ≠ ∅ has σ_{t+1}(x) = z*, the (Ξ_t(w), w)-maximum of Iσ_t(x); a w with Ξ_t(w) ≻ Ξ_t(z*) ≻
  Ξ_t(σ_t(x)) would lie in Iσ_t(x) with a larger value. So Iσ_{t+1}(x) = ∅.
- At t + 1 S4a keeps σ (Iσ = ∅); then S4b changes τ, or S4c fires for Odd (FIX 3: Odd falls back only if Iσ = ∅) and changes τ, or N5 stops
  (S5), exactly as in HON-FB (iv)'s proof (P-N5-HON, RESULTS R68 (c)). τ is constant on P, so t + 1 is the last state of P. □
Corollary SAT-FB1. For every phase P and configuration C, at most one in-phase fallback of P has a saturated C-state as its source.
Proof. If t₁ < t₂ were two, t₂ is a C-state after t₁, so t₁ + 1 is the last state of P (SAT-FB); but t₂ ≥ t₁ + 1 is the source of an in-phase
transition. □
Theorem FB-C′. In every phase P of N5 on every game, f ≤ n·|𝒞_f(P)|.
Proof. Fix C ∈ 𝒞_f(P) and let t_1 < … < t_N be the fallback sources of P that are C-states. Unsaturated ones: by FB-RISE_C, LEV_C(t_i + 1) ≥
LEV_C(t_i) + 1, and LEV_C is non-decreasing, so consecutive unsaturated ones have strictly rising LEV_C in {0, …, n − 2}: at most n − 1.
Saturated ones: at most 1 (SAT-FB1). So N ≤ n; sum over C. □
- Consequences. |𝒞_f(P)| ≤ N_ep(P), so f ≤ n·N_ep, which implies RESULTS R60 (c) Lemma EPOCH (f ≤ 1 + n·N_ep); the per-configuration form is
  stronger where configurations recur. On 𝒞^kO with maximum out-degree Δ, f ≤ n·Δ^k per phase; if every state of P has |D_k| ≤ 1,
  f ≤ n(1 + m).
- Remark (another proof; a referee note, not a premise). REFEREE 15's report on P-N5-FBC (docs/referee/R-N5-FBC.md at claude/referee 0addfc5f,
  note FBC-N3) proves the same statement (at most one saturated fallback per configuration and phase, f ≤ n·|𝒞_f(P)|): two saturated C-sources
  make the first fallback Ξ-flat by SAT_C (2); RESULTS R15 (b) then makes every gate a length-only switch at a cycle node, and RESULTS R38 (f)
  CN-LAST ends the phase at t + 1. The proof above reaches the same last-state conclusion directly from S2 and S4c's maximum (no improving edge
  is left at t + 1), without R15 (b) or R38 (f). Both proofs use SAT_C (2). REFEREE-2's FBC report was pending at the freeze.

## 4. Corollary EP-ASM: the epoch count, assembled (every game)
Split the epochs of P by |D_E|: N_ep = N_0 + N_1 + N_{≥2}.
- N_0 ≤ 4n² − 3n: Corollary HON-0-FF (b) (P-N5-HONFF; signed by both referees, no gap).
- N_1 ≤ (1 + 4n² − 3n + X_dir + X_big)·(T*_Q + 2): Corollary REC-1-FF (c) (P-N5-HONFF; an IMPLICATION from (Στ), signed as such; it holds at RESULTS
  R65's audit strength). X_dir, X_big, T*_Q as in RESULTS R68.
- N_{≥2} ≤ NCONF_{≥2}(P)·(2n² − n) + R⁰_{≥2}(P): Corollary VIS summed over the configurations with |D_C| ≥ 2; R⁰_{≥2} := Σ_{|D_C| ≥ 2} R⁰_C (PROVED, §2).
Corollary EP-ASM. N_ep(P) ≤ (4n² − 3n) + (1 + 4n² − 3n + X_dir + X_big)·(T*_Q + 2) + NCONF_{≥2}(P)·(2n² − n) + R⁰_{≥2}(P), the second term as an
implication from (Στ). □
- READING. On this route the epoch count of a phase rests on four quantities: X_dir and X_big (RESULTS R68's open terms), NCONF_{≥2} (distinct
  multi-gate configurations) and R⁰_{≥2} (fallback-free returns to them). RESULTS R61 (f)'s ρ count is not used. With RESULTS R64 (transitions =
  Σ epoch lengths) the per-phase transition count also needs the lengths of |D_E| ≥ 2 epochs (the "|D_E| ≥ 2 S4a core").

## 5. A remark, and a DEAD guess
- PROVED (elementary). In a phase τ is fixed, so D_k is a function of σ̄_k|Q: a change of D is a change of configuration, and (D changes + 1) ≤
  N_ep. L-SI's docs/si/N5-RUND-box17.md §27.2 calls its count “an upper proxy for R63's epochs”; it is a lower bound (L-SI §28 recounted: nep90 89
  boundaries, nep76 75; relayed by the Lead).
- DEAD: "a fallback from a saturated C-state is flat and ends the phase" (successor 26's guess, docs/new/N5-FB-box47.md §5: “a fallback at a
  saturated C-state is flat and ends the phase”). Instance: experiments/red/fbr/instances/rho3_253_n32.pg (L-RED), random start (satfb.py
  `12 3 --list out/satfb_nonflat3.txt`): phases with several saturated fallbacks, none flat, all but the last of each phase not last; each one
  leaves its configuration for good, as SAT-FB says. In liball n ≤ 34 (S3 + 2, seed 7): 12 of 68 saturated fallbacks non-flat, 8 not last
  (cond_stuck_symsi3_YE n 32, gapb_dup_n20, rho3_253_n32). The disjunction in SAT-FB is the right form.

## 6. DATA (not to sign; experiments/new/box48/, outputs in out/) and OPEN
- nep90_n40 / nep76_n40 / long121_n40, each from its own start (L-SI / L-RED): N_ep 90 / 76 / 37 against NCONF 48 / 40 / 14; at most 6 / 5 / 7
  epochs of one configuration; f 7 / 6 / 8, |𝒞_f| 4 / 3 / 5. Each long phase is two LAPS of one configuration block; lap 2 replays lap 1 on the
  active Even vertices and differs on dormant ones switched by a fallback (out/laps_nep90.txt). NCONF_{≥2} / N_ep^{≥2}: 38 / 74, 36 / 71, 12 / 35.
- RET-FB (retfb.py): liball n ≤ 34, S3 + 2, seed 7: 776 checks, 0 violations, VIS_V 0 (93 phases over the level budget, skipped); nep90 75
  checks, long121 36, 0 violations; control MUT=1 (t := s − 1) 346 violations of 1,236 (bites). R⁰ = 2 of nep90's 42 returns, 3 of long121's 23.
- vislev.py: of 794 returns in liball n ≤ 34, LEV_C rises at 640 and stalls at 122, every stall fallback-free.
- SAT-FB (satfb.py): liball n ≤ 34: 68 saturated fallbacks, SATFB_V 0, SATFB1_V 0; random 3,000 𝒞^kO: 546, all flat and last.
- r0shape.py, liball n ≤ 40: 616 fallback-free returns, 583 to configurations with |D_C| ≤ 1 and 33 to |D_C| ≥ 2; 610 change σ̄ at one vertex.
  NCONF_{≥2} per phase: 0 or 1 in 7,468 of 7,571 phases, max 35. nconf.py: NCONF ≤ n in every library phase; nep90's start gives 48 at n 40.
- ncclimb.py (S3 start, fitness NCONF_{≥2}): seeded from nep90 / nep76, best 15 / 17 at n 47-48.
- OPEN: NCONF_{≥2} (no argument; READING: Ξ is monotone, but sibling values can leapfrog any number of times, so counting alone falls back on
  ρ); R⁰_{≥2}; X_dir, X_big; CONJECTURE SAT-1 (no C-epoch after a saturated C-state; data: at most 1 saturated epoch per configuration in
  liball n ≤ 34). By SAT_C (2) a return after saturation needs S4a steps with Ξ unchanged (length-only switches at cycle nodes, RESULTS R15 (b))
  and a change of σ̄|Q through a tie of S1; not excluded.

## 7. Quotes and pins (checked by script)
Every quote below, set in curly double quotes, is verbatim from the named file at trunk f4562054 unless another revision is named.
- S2, docs/new/N5-ssi-global.md l. 47: “Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than Ξσ(σ(v))}”. S4a, l. 53: “Else σ_new = σ.”
  S4c, l. 56-57: “for every Even v with an improving edge set σ_new(v) = the w with (v, w) ∈ Iσ maximising (Ξσ(w), w) (best valuation, ties: larger
  index)”. S5, l. 59: “S5 Stop when Iσ = Iτ = ∅.” FIX 3, l. 88: “In a fallback iteration with Iσ ≠ ∅ only σ changes (τ_new = τ)”; “Odd falls back
  only if Iσ = ∅.”
- (MON): docs/RESULTS.md l. 631: “Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}.”
- (V1), (V2): docs/new/N5-phase-bound-box10.md l. 20-21: “(V1) if x is not its own cycle node then Ω_ρ(x) = x ⊕ Ω_ρ(ρ(x)) and the ρ-path from ρ(x) to
  λ(x) avoids x.” and “(V2) PREFIX MONOTONICITY: if a ⪯ b are values whose paths both avoid x (or whose cycle nodes differ), then x ⊕ a ⪯ x ⊕ b”.
- FB-RISE (a), docs/new/P-N5-HONFF-box47.md l. 56-57: “Lemma P's Case A (A1 if λ(x) ≠ x, A2 if λ(x) = x) with Ω := Ξ_t, ρ := σ_t (Q-A) gives”; l. 58:
  “Then x is switched, σ_{t+1}(x) = z* := z*(x), and Ξ_t(z*) ⪰ Ξ_t(z) ⪰ value(r′)”. Q-A: docs/new/P-N5-HONFF-fixes-box47.md §1.
- HON-0-FF (b) and REC-1-FF (c), P-N5-HONFF l. 85 and 88-89: “each number at most 4n² − 3n”; “the |D_k| = 1 states, and the epochs with |D_E| = 1,
  number at most (1 + 4n² − 3n + X_dir + X_big)·(T*_Q + 2)”.
- HON-FB (iv), docs/new/P-N5-HON-box46.md l. 106: “so S4a returns σ_{h+1}; then S4b changes τ, or S4c fires for Odd (Iσ = ∅, FIX 3) and changes τ, or N5 stops.”
- Epoch, docs/RESULTS.md l. 3213: “An EPOCH is a maximal run E = (x, …, y) of a phase on which σ̄|Q is constant”. R60 (c), l. 3079: “(c) f ≤ 1 + n·N_ep.”
  R60's limit, l. 3085: “σ̄|Q REPEATS inside a phase”. R68, l. 3526-3527: “X_dir := the in-phase transitions with |D_k| = |D_{k+1}| = 1 and D_k ≠
  D_{k+1}; X_big := those with |D_k| ≥ 2 and |D_{k+1}| = 1.”
- FBC-N3, docs/referee/R-N5-FBC.md (claude/referee 0addfc5f, on trunk f4562054): “Per phase P and configuration C, at most one in-phase fallback has
  a saturated C-state source.”; “So RESULTS R38 (f) CN-LAST applies: t + 1 is the last state of P.”
- L-SI §27.2, docs/si/N5-RUND-box17.md l. 1124: “an upper proxy for R63's epochs”. Successor 26's guess, docs/new/N5-FB-box47.md: “a fallback at a
  saturated C-state is flat and ends the phase”.
- Pins: P-N5-HONFF-box47.md sha1 98101d1fe723a570f3c79085b929a456ebb7dff5; P-N5-HONFF-fixes-box47.md sha1 ccc520dd83c9086b57a2417c1cdcede44e7b7865;
  P-N5-FBC-box47.md sha1 32d3776cf4090fb15c1d0cb4c8b4f59276f64e21 (not a premise); working doc docs/new/N5-NCONF-box48.md (sha1 in the freeze
  message); instances long121_n40.pg sha1 c667c08535641a986d771c7a5f3d76bb3c0eef0f (+ .start d750664a79160e60196abb9f8daabaf141b0e780).
- Script: `python3 experiments/new/box48/quotecheck2.py docs/new/P-N5-EPC-box48.md f4562054:docs/new/N5-ssi-global.md f4562054:docs/RESULTS.md
  f4562054:docs/new/N5-phase-bound-box10.md f4562054:docs/new/P-N5-HONFF-box47.md f4562054:docs/new/P-N5-HON-box46.md f4562054:docs/referee/R-N5-FBC.md
  f4562054:docs/si/N5-RUND-box17.md f4562054:docs/new/N5-FB-box47.md` (output experiments/new/box48/out/quotecheck_epc.txt); every quote found.
