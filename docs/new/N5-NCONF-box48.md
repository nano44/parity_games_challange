# Distinct Odd configurations per phase, and the returns to a configuration (box 48)
L-NEW successor 27 (Opus 5.5), D14 / D18, Lead reading L40; Lead's GO of 13:13Z (Lead's stamp): "GO on (1), NCONF, the number of distinct σ̄|Q
per phase … Report distinct configurations against epochs there first." Written 2026-10-26 13:30Z onward (date -u). Working doc, unrefereed.
Not a TARGET.md claim; G-N5-TIME stays open.
Labels: PROVED (L-NEW 27, unrefereed) / CONJECTURE / OPEN / DATA / READING / DEAD.
Builds on docs/new/N5-FB-box47.md (setting §0, LEV_C, Lemma FB-RISE_C, Lemma SAT_C, Theorem FB-C) and docs/new/P-N5-HONFF-box47.md (frozen,
sha1 98101d1f…; Lemma FB-RISE, question Q-A).

## Summary
| § | item | label |
| --- | --- | --- |
| §1 | N_ep (σ̄|Q changes + 1, RESULTS R63/R64's epochs) ≥ the D-change count; L-SI §27.2's 42 / 32 "epochs" on nep90 / nep76 are D changes; N_ep there is 90 / 76 | PROVED (elementary) + DATA |
| §1 | nep90 / nep76: the long phase is two LAPS of one configuration sequence (48 / 40 distinct configurations for 90 / 76 epochs); lap 2 replays lap 1 on the active Even vertices, and differs only on dormant ones switched by the fallback between the laps | DATA |
| §2 | Lemma RET-FB: after an in-phase fallback t → t + 1, at every later C-state s of the phase, LEV_C(s) ≥ min(LEV_C(t) + 1, n − 1), for EVERY configuration C (not only t's) | PROVED (every game; rests on Q-A as FB-RISE does) |
| §2 | Corollary VIS: a configuration has at most 2n² − n + R⁰_C epochs in a phase, R⁰_C := its returns with no fallback in between and LEV_C unsaturated | PROVED |
| §2 | Theorem EP-C: N_ep(P) ≤ NCONF(P)·(2n² − n) + R⁰(P), and R⁰(P) ≤ Σ_S REV(S) over the ≤ f + 1 fallback-free runs S of P | PROVED (a reduction) |
| §3 | data: RET-FB, VIS; at most one saturated epoch per configuration (SAT-1); NCONF ≤ n except nep90 | DATA / CONJECTURE |
| §6 | Corollary EP-ASM: N_ep ≤ (4n² − 3n) + (1 + 4n² − 3n + X_dir + X_big)(T*_Q + 2) + NCONF_{≥2}·(2n² − n) + R⁰_{≥2}: the epoch count reduces to X_dir, X_big, the multi-gate configurations NCONF_{≥2} and their fallback-free returns R⁰_{≥2} | PROVED as an assembly (N_1 term an IMPLICATION from (Στ)) |
| §5 | Lemma SAT-FB: a fallback from a saturated C-state is the phase's last transition, or C never recurs; so at most one saturated fallback per configuration, and Theorem FB-C′: f ≤ n·|𝒞_f(P)| (was |𝒞_f(P)|·(4n² − 3n)); FB-C′ implies RESULTS R60 (c) EPOCH | PROVED (every game) |
| §4 | what is open | OPEN / READING |
| §9 | frozen-side u-stretches: RESTRICT_{u|J} (N5 on a stretch where only u's best reply moves = N5^τ on G^{u|J}) | CONJECTURE (successor 27) → PROVED in §10 |
| §10 | Lemma RESTRICT_H / REPRO_H: R64's restriction holds on any Odd cut H containing τ and every σ̄_k of the run; covers G′_E, G^u, G^{u|J} and the used-edge game G^P of a whole phase (nep90 / nep76 / long121: QP 5 / 5 / 3) | PROVED (L-NEW 28, unrefereed) + DATA |

## 0. Setting (every game)
As docs/new/N5-FB-box47.md §0: N5 = SPEC S1-S5; phase P (maximal run with (λ, τ) constant); Q := Odd vertices of out-degree ≥ 2; a
CONFIGURATION C = σ̄|Q; k is a C-state if σ̄_k|Q = C; H_C := G with every Odd v cut to σ̄_C(v); LEV_C(k) := the largest j ≤ n − 1 with Ξ_k(x) ⪰
value(r) for every vertex x and every simple H_C-path r from x to a cycle node of λ with ≤ j edges. LEV_C is defined at every state of P and is
non-decreasing on P ((MON)). An EPOCH is a maximal run of P with σ̄|Q constant (RESULTS R63, R64), N_ep(P) their number. NCONF(P) := the number
of distinct configurations of P's states. For a configuration C, its C-epochs E_1 < … < E_V (V = V_C) with first states s_1 < … < s_V; a RETURN
is a pair (i, i + 1). REV(P) := N_ep(P) − NCONF(P) = Σ_C (V_C − 1).

## 1. Epochs against configurations: nep90 and nep76 (DATA; one PROVED remark)
- PROVED (elementary). In a phase τ is fixed, so D_k = {q ∈ Q : σ̄_k(q) ≠ τ(q)} is a function of σ̄_k|Q. A change of D is a change of
  configuration, so (D changes + 1) ≤ N_ep. L-SI §27.2 (docs/si/N5-RUND-box17.md at l-si 109776d4) counts D changes + 1 and calls it "an upper proxy
  for R63's epochs"; it is a LOWER bound.
- DATA (nconf.py, laps.py; the starts are L-SI's experiments/si/rund/instances/nep90_n40.start and experiments/n5-epoch/instances/nep76_n40.start):

| instance | phase | L | N_ep (σ̄|Q) | D changes + 1 | NCONF | distinct D | max epochs of one C (VIS) | f | NCF = |𝒞_f| |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nep90_n40 (n 40, |Q| 5) | [4, 95] | 91 | 90 | 42 | 48 | 12 | 6 | 7 | 4 |
| nep76_n40 (n 40, |Q| 5) | [9, 87] | 78 | 76 | 32 | 40 | 9 | 5 | 6 | 3 |

  The L and D-change columns reproduce L-SI's table exactly. σ̄|Q changes at 89 of nep90's 91 transitions: epochs are one state long, not two.
- DATA, LAPS (out/laps_nep90.txt). nep90's configuration sequence (ids by first occurrence) is 0 1 2 | 3 … 43 | 3 3 4 … 38 | 44 … 47: the block 3 … 38
  occurs twice, in the same order. At each state of lap 2 (states 51-90), σ differs from the state of lap 1 with the same configuration only on the
  Even vertices {15, 16, 26, 28, 35, 39} (and 18 from state 75). The fallback at state 50 switches them; lap 2 does not move them. On the active
  Even vertices Even's strategy returns to its lap-1 values move for move. nep76 has the same shape (block 2 … 33 twice). So here
  N_ep ≈ 2·NCONF. The returns are made by Even's strategy coming back, with a few "dormant" vertices changed, not by new configurations.
- READING. A lap is a counter-like mechanism: if dormant layers could be stacked so that each layer change restarts the active lap, N_ep could
  be large while NCONF stays small. §2 shows that every lap restart that passes through a fallback is paid for by a rise of LEV_C, for every
  configuration of the lap at once.

## 2. Lemma RET-FB, Corollary VIS, Theorem EP-C (PROVED, every game)
Lemma RET-FB. Let t → t + 1 be an in-phase S4c fallback of P, C any configuration, and s ≥ t + 1 a C-state of P. Then
LEV_C(s) ≥ min(LEV_C(t) + 1, n − 1).
Proof. Let L := min(LEV_C(t) + 1, n − 1). We show Ξ_s(y) ⪰ value(r) for every vertex y and every simple H_C-path r from y to a cycle node u of λ
with |r| ≤ L, by induction on |r|. |r| = 0: y = u and Ξ_s(u) = (u, ∅, 0) = value(r). Let |r| ≥ 1, r = y → z → r′; r′ avoids y and |r′| ≤ L − 1.
- y Even. Every edge of G at y is an edge of H_C. |r′| ≤ L − 1 ≤ LEV_C(t), so Ξ_t(z) ⪰ value(r′) (definition of LEV_C(t), which ranges over all
  vertices at every state). Items 2 and 3 of the proof of FB-RISE (a) (P-N5-HONFF §1) now apply verbatim with G_τ replaced by H_C: they use the
  G-edge (x, z), Ξ_t(z) ⪰ value(r′), the fallback rule (S4c: the (Ξ_t(w), w)-maximum of Iσ_t(x); FIX 3), Lemma P's Case A with Ω := Ξ_t (Q-A),
  (MON), (V1)/(V2) at t + 1 and λ_{t+1} = λ, and nothing about the frame of r′ (as N5-FB-box47 §2 notes for FB-RISE_C). They give
  Ξ_{t+1}(y) ⪰ value(r). Then Ξ_s(y) ⪰ Ξ_{t+1}(y) by (MON) (t + 1 ≤ s, both in P).
- y Odd. s is a C-state, so σ̄_s(y) = σ̄_C(y) = z (for y ∉ Q, z is y's only successor), and y's honest play at s is y followed by z's. By induction
  (|r′| < |r|), Ξ_s(z) ⪰ value(r′). The Odd case of FB-RISE_C's proof (N5-FB-box47 §2) at the C-state s: if λ(y) ≠ y, (V1) gives Ξ_s(y) =
  y ⊕ Ξ_s(z) with z's path to λ(y) avoiding y, and (V2) (r′ avoids y) gives Ξ_s(y) ⪰ y ⊕ value(r′) = value(r); if λ(y) = y, Ξ_s(y) = (y, ∅, 0),
  Ξ_s(z) has cycle node y and value(r′) cycle node u ≠ y, so y is better than u and (y, ∅, 0) ≻ value(r).
So LEV_C(s) ≥ L. □
- What is new against FB-RISE_C: there t must be a C-state and the bound is at t + 1. Here the fallback can come from ANY configuration; the Even
  vertices are relaxed in every frame at once (the relaxation is frame-free), and the Odd vertices catch up at the next state where they follow C.
  At a non-C state the Odd vertices with σ̄ ≠ C can sit below their H_C-paths (Odd's best reply undercuts them), which is why the bound is
  stated at C-states only.
- With t a C-state and s = t + 1 a C-state this is FB-RISE_C; RET-FB does not give FB-RISE_C when t + 1 is not a C-state.

Corollary VIS. For every phase P and configuration C, V_C ≤ 2n² − n + R⁰_C, where R⁰_C := the returns (i, i + 1) with no in-phase fallback source
in [s_i, s_{i+1}) and LEV_C(s_i) ≤ n − 2.
Proof. Split the V_C − 1 returns.
- (a) LEV_C(s_i) = n − 1. Let i₀ be the least such i. By Lemma SAT_C (N5-FB-box47 §2), every C-state t′ > s_{i₀} of P has t′ − s_{i₀} ≤ 4n(n − 1).
  Two C-epochs are separated by at least one non-C state, so s_{j+1} ≥ s_j + 2, and V_C − i₀ ≤ 2n(n − 1). These are all the returns of kind (a)
  (LEV_C is non-decreasing, so LEV_C(s_i) = n − 1 exactly for i ≥ i₀).
- (b) LEV_C(s_i) ≤ n − 2 and some in-phase fallback has its source t ∈ [s_i, s_{i+1}). Then t + 1 ≤ s_{i+1}, and by RET-FB and (MON),
  LEV_C(s_{i+1}) ≥ min(LEV_C(t) + 1, n − 1) ≥ min(LEV_C(s_i) + 1, n − 1). So LEV_C rises by at least 1 along each such return, from a value in
  {0, …, n − 2}, and never drops: at most n − 1 returns of kind (b).
- (c) the rest: R⁰_C.
V_C = 1 + #returns ≤ 1 + 2n(n − 1) + (n − 1) + R⁰_C = 2n² − n + R⁰_C. □

Theorem EP-C. For every phase P of N5 on every game, N_ep(P) ≤ NCONF(P)·(2n² − n) + R⁰(P), R⁰(P) := Σ_C R⁰_C. Moreover R⁰(P) ≤ Σ_S REV(S), the sum
over the maximal fallback-free runs S of P (runs of states of P with no in-phase fallback transition between consecutive ones; there are at most
f + 1 of them, and f ≤ |𝒞_f(P)|·(4n² − 3n) by Theorem FB-C), REV(S) := (epochs of P meeting S, counted inside S) − (distinct configurations of S).
Proof. N_ep(P) = Σ_C V_C; sum Corollary VIS over the NCONF(P) configurations. A return counted in R⁰_C has no fallback source in [s_i, s_{i+1}),
so the states s_i, …, s_{i+1} lie in one fallback-free run S, and both C-epochs start inside S; distinct returns are distinct pairs of epoch
starts of the same configuration inside S, and a configuration with V′ epoch starts in S contributes at most V′ − 1. □
- READING. EP-C reduces the epoch count to two quantities: the number of distinct configurations, and the returns inside fallback-free runs
  (pure S4a stretches, the territory of RESULTS R67's PIECE_D / SPLIT-RED). A lap of the nep90 kind, restarted through a fallback, is paid for
  by LEV_C; a lap restarted without any fallback would be charged to R⁰. RESULTS R60's honest limit (i) ("σ̄|Q REPEATS inside a phase, so N_ep is
  not bounded by the number of σ̄|Q configurations", lap_n6_s1_110421) stays true; EP-C says by how much it can fail: by the fallback-free
  returns only.
- Compared with landed results (checked by grep in docs/RESULTS.md, 13:3xZ): R61 (f) bounds N_ep by 1 + Σ_q (ρ_q + tie_q + nc_q + cyc_q) (Ξ
  changes at Odd choice vertices and residuals); R60 (c) bounds f by N_ep; R63 / R64 charge crossings and transitions to epochs. None bounds N_ep
  through configurations. EP-C is incomparable with R61 (f): it does not count ρ, but needs NCONF and R⁰.

## 3. DATA (experiments/new/box48/; outputs in out/)
- nconf.py, liball (the 735 pinned .pg files of box47/out/liball.txt), n ≤ 40, S3 + 2 random starts, seed 7 (out/nconf_liball_n40_k2.txt): 7,571
  phases; N_ep summed 10,938 against NCONF summed 9,865; 187 phases with a return; RET_NOFB (returns with no fallback between) 688; max VIS 10
  (j4_n40, |Q| 1); max REV 38 (rise_thin51_n40, |Q| 1); max NCONF 39 (nep76_n40, random start); NCONF ≤ n in every phase. Random 𝒞^kO (2 × 3,000
  games, n 5-24, S3 + 4 starts; out/nconf_rand3000*.txt): phases of length ≤ 4, NCONF ≤ 4: uninformative.
- NCONF > n occurs: nep90 from L-SI's start has NCONF 48 at n = 40 (the only case seen).
- vislev.py (LEV_C at the first states of the C-epochs), liball n ≤ 34, S3 + 2 (out/vislev_liball_n34_k2.txt): 794 returns in 487 returning
  configurations; LEV_C rises at 640, STALLS (equal, unsaturated) at 122, every stall with NO fallback in between (STALL_with_fb_between 0);
  LEV_DROP_V 0; 15 phases UNK (level budget). nep90 with its start (out/vislev_nep90.txt): 42 returns, 40 rises, 2 stalls (the short c16 → c17 →
  c16 bounces at states 20 → 22 and 65 → 67, no fallback); every lap return rises. SAT_VIS_max = 1: no configuration had two epochs at saturated
  LEV_C (CONJECTURE SAT-1 below).
- retfb.py (Lemma RET-FB at every epoch start against the last fallback before it; Corollary VIS). liball n ≤ 34, S3 + 2, seed 7, budget 3·10⁶
  (out/retfb_liball_n34_k2.txt): 776 checks, RETFB_V 0, VIS_V 0 (93 phases UNK, skipped); returns: R⁰ 466 of REV 742 (63%). nep90 with its start
  (out/retfb_nep90.txt): 75 checks, RETFB_V 0, R⁰ = 2 of REV 42: EP-C charges 40 of nep90's 42 returns to LEV_C. nep76 with its start: UNK at
  budget 3·10⁷. Control MUT=1 (t := s − 1, any transition; liball S3 only, out/retfb_liball_n34_MUT.txt): RETFB_V 346 of 1,236: bites.
- CONJECTURE SAT-1. Once LEV_C = n − 1 at a C-state of P, P has no later C-epoch. (Data: SAT_VIS_max 1 over liball n ≤ 34. SAT_C only gives a
  window of 4n(n − 1) states, during which Ξ is constant.) If true, Corollary VIS improves to V_C ≤ n + R⁰_C and EP-C to N_ep ≤ n·NCONF + R⁰.

## 4. OPEN, and what this changes (READING)
- OPEN: NCONF(P) on general games. Data: ≤ n except nep90 (48 at n 40). No argument bounds it by a polynomial; Π_q deg(q) is the trivial bound.
- OPEN: R⁰ (returns inside fallback-free runs). The 122 stalls show LEV_C does not pay for them. Next: what does? Candidates: R67's split
  states and unforbid switches; the switch-best structure of aligned blocks.
- OPEN: CONJECTURE SAT-1.
- The FB-C factor |𝒞_f(P)| is at most NCONF(P); data |𝒞_f| ≤ 7 (box 47) and ≤ 4 on nep90 / nep76.

## 5. Queue item 2: the saturated term of FB-C (PROVED, every game)
Written 13:5xZ (date -u). The obstacle named by successor 26 (N5-FB-box47 §5): in H_C, Ξ = B_C does not exclude an improving edge that closes a
cycle Z whose top is better than the current cycle node but is not a cycle node of λ, so the HON-FB route (arena optimality (F1)) does not
transfer. The route below does not look at the switched edges at all; it uses SAT_C's constancy.
Lemma SAT-FB. Let t be a C-state of P with LEV_C(t) = n − 1 whose transition t → t + 1 is an in-phase S4c fallback. Then t + 1 is the last state
of P, or P has no C-state after t.
Proof. Suppose t′ > t is a C-state of P. By Lemma SAT_C (N5-FB-box47 §2), Ξ is constant on t, …, t′, so Ξ_{t+1} = Ξ_t (t + 1 ≤ t′).
- Iσ_{t+1} = ∅. S2: Iσ(x) = {w ∈ succ(x) : Ξ(w) ≻ Ξ(σ(x))}, read at t + 1 with Ξ_{t+1} = Ξ_t. The fallback is Even's (in-phase, FIX 3). An Even x
  with Iσ_t(x) = ∅ keeps σ_{t+1}(x) = σ_t(x), so Iσ_{t+1}(x) = Iσ_t(x) = ∅. An Even x with Iσ_t(x) ≠ ∅ has σ_{t+1}(x) = z*, the (Ξ_t(w), w)-maximum of
  Iσ_t(x); a w with Ξ_t(w) ≻ Ξ_t(z*) ≻ Ξ_t(σ_t(x)) would lie in Iσ_t(x) with a larger value. So Iσ_{t+1}(x) = ∅.
- With Iσ_{t+1} = ∅, S4a returns σ_{t+1}; then S4b changes τ, or S4c fires for Odd (FIX 3: Odd falls back only if Iσ = ∅) and changes τ, or
  N5 stops (the argument of P-N5-HON's HON-FB (iv), signed). τ is constant on P, so t + 1 is the last state of P. □
Corollary SAT-FB1. For every phase P and configuration C, at most one in-phase fallback of P has a saturated C-state as its source.
Proof. If t₁ < t₂ were two, t₂ is a C-state after t₁, so by SAT-FB t₁ + 1 is the last state of P; but t₂ ≥ t₁ + 1 is the source of an
in-phase transition, so t₂ + 1 ∈ P. □
Theorem FB-C′. In every phase P of N5 on every game, f ≤ n·|𝒞_f(P)|.
Proof. Theorem FB-C's proof with SAT-FB1 for the saturated fallbacks of each C: at most n − 1 unsaturated (FB-RISE_C) plus at most 1 saturated. □
- What this changes. FB-C′ is the bound successor 26 asked for (N5-FB-box47 §5: "would bring the total to f ≤ n·|𝒞_f(P)|. Not proved."). Since
  |𝒞_f(P)| ≤ N_ep(P), FB-C′ gives f ≤ n·N_ep, which implies RESULTS R60 (c) Lemma EPOCH (f ≤ 1 + n·N_ep) and is stronger per configuration.
  So the CORRECTION of N5-FB-box47 §3 (that FB-C's N_ep form was weaker than R60 (c)) no longer applies to FB-C′.
- Premises: SAT_C (which uses (MON), (V1), the H_C-play form of Ξ at a C-state, and the definition of B_C; R15 (d) only for the window, not used
  here), S2, S4c, FIX 3, HON-FB (iv)'s last-state argument; the unsaturated part through FB-RISE_C rests on Q-A (answered YES by both referees
  for P-N5-HONFF, docs/new/P-N5-HONFF-fixes-box47.md §1).
- Not obtained: SAT-1 (no C-EPOCH after saturation). By SAT_C, a return to C after a saturated C-state s needs every transition of [s, s′) to
  keep Ξ; a fallback there ends the phase (as above), so all are S4a steps with Ξ unchanged, i.e. length-only switches at cycle nodes (RESULTS
  R15 (b)), and σ̄|Q must change through a tie of S1's counterstrategy. Not excluded here.
- DATA (satfb.py; flags as in its docstring): random 3,000 𝒞^kO (n 5-18, gseed 111, S3 + 4 starts, seed 8; out/satfb_rand3000.txt): 546
  saturated fallbacks, all FLAT, LAST and with t + 1 a C-state; all 549 switches at own cycle nodes, closing a cycle through x. lib41 n ≤ 16: 20,
  the same. liball n ≤ 34, S3 + 2, seed 7 (out/satfb_liball_n34_k2.txt): 68 saturated fallbacks; 12 NONFLAT, 8 NOT LAST, every one of the 12 with
  t + 1 not a C-state and the switch at a vertex that is not its own cycle node (cond_stuck_symsi3_YE n 32, gapb_dup_n20, rho3_253_n32); up to 3
  in one phase. The same three instances with 12 random starts, seed 3 (out/satfb_nonflat3_k12.txt): 22 saturated fallbacks, all NONFLAT, 18 NOT
  LAST, up to 9 in one phase, SATFB_V 0 (the lemma's disjunction holds), SATFB1_V 0 (one per configuration). Re-run of liball with the direct
  SATFB_V / SATFB1_V counters: out/satfb_liball_n34_k2_v2.txt.
- DEAD (successor 26's guess, N5-FB-box47 §5: "a fallback at a saturated C-state is flat and ends the phase"): rho3_253_n32
  (experiments/red/fbr/instances, L-RED), random start: phase [3, 11] has saturated fallbacks at 8, 9, 10, none flat, the first two not last;
  each leaves its configuration for good. SAT-FB's disjunction is the right form: per phase there can be several saturated fallbacks, at most
  one per configuration.

## 6. Assembly of the epoch count (Corollary EP-ASM; written 14:1xZ by date -u)
Split the epochs of a phase P by |D_E| (D_E := {q ∈ Q : σ̄_E(q) ≠ τ(q)}, a function of the epoch's configuration): N_ep = N_0 + N_1 + N_{≥2}.
- N_0 ≤ 4n² − 3n: Corollary HON-0-FF (b) (P-N5-HONFF §2; signed by both referees, no gap; fixes file P-N5-HONFF-fixes-box47).
- N_1 ≤ (1 + 4n² − 3n + X_dir + X_big)·(T*_Q + 2): Corollary REC-1-FF (c) (same packet; an IMPLICATION from (Στ), signed as such; holds at
  RESULTS R65's audit strength). X_dir, X_big, T*_Q as in RESULTS R68.
- N_{≥2} ≤ NCONF_{≥2}(P)·(2n² − n) + R⁰_{≥2}(P): Corollary VIS summed over the configurations C of P with |D_C| ≥ 2 (NCONF_{≥2} of them),
  R⁰_{≥2} := Σ_{|D_C| ≥ 2} R⁰_C (returns to multi-gate configurations with no fallback in between, LEV_C unsaturated). PROVED (lane, §2).
Corollary EP-ASM. N_ep(P) ≤ (4n² − 3n) + (1 + 4n² − 3n + X_dir + X_big)·(T*_Q + 2) + NCONF_{≥2}(P)·(2n² − n) + R⁰_{≥2}(P) (the second term as
an implication from (Στ)). □
- READING. With RESULTS R64 (transitions per phase = Σ over epochs of their lengths, epoch lengths bounded on |D_E| ≤ 1 by EP-0 / EP-1) and Theorem
  FB-C′, G-N5-TIME's per-phase count now rests on: X_dir, X_big (R68's open terms), NCONF_{≥2} (how many distinct multi-gate configurations a phase
  visits), R⁰_{≥2} (fallback-free returns to them), and the lengths of |D_E| ≥ 2 epochs (the "|D_E| ≥ 2 S4a core", L-SI §27). The ρ count of
  RESULTS R61 (f) is not needed in this route.
- DATA for the multi-gate terms (r0shape.py, liball n ≤ 40, S3 + 2, seed 7; out/r0shape_liball_n40_k2.txt): of the 616 fallback-free returns
  (no LEV_C filter, so an upper count for R⁰), 583 go to configurations with |D_C| ≤ 1 (44 with D_C = ∅, 539 with |D_C| = 1) and 33 to |D_C| ≥ 2
  (28 / 3 / 1 / 1 for |D_C| = 2 / 3 / 4 / 5); 610 change σ̄ at one vertex only. NCONF_{≥2} per phase: 0 in 4,929 phases, 1 in 2,539, ≥ 2 in 103, max
  35. So on the library R⁰_{≥2} is small and NCONF_{≥2} carries the multi-gate epochs.
- DATA, the multi-gate split on the three long phases (each from its own start; inline script, numbers re-derivable with nconf.py's rows):
  nep90 NCONF_{≥2} 38, NCONF_{≤1} 10, N_ep^{≥2} 74 (deg on Q 18, 3, 2, 3, 3: Σ 29, Π 972); nep76 36 / 4 / 71 (15, 4, 5, 5, 2); long121 12 / 2 / 35
  (5, 3, 4). So NCONF_{≥2} can exceed Σ_q deg(q) (nep90: 38 > 29): the configurations combine choices at several vertices, and N_ep^{≥2} ≈ 2·NCONF_{≥2}
  (the laps).
- DATA, climb (ncclimb.py, fitness (max NCONF_{≥2} in one phase, max N_ep^{≥2}), S3 start, 1,500 mutation steps, NMAX 48; out/ncclimb_nep*_s*.txt,
  best games in out/climb/): from nep90 (S3 score 10) seeds 11 / 12 reach 15 (n 48) and 13 (n 48); from nep76 seed 13 reaches (17, 18) (n 47). So
  from S3 the climb does not push NCONF_{≥2} near n; L-RED's chosen start on nep90 gives 38. Start pairs matter more than the game here.
- DATA, long121_n40 (L-RED 21, from its start; out/nconf_long121.txt, out/retfb_long121.txt): one phase, L 121, N_ep 37, NCONF 14, VIS 7, f 8,
  |𝒞_f| 5; two laps again (block 2 3 5 6 7 8 6 8 9 3 5 6 11 twice); RET-FB 36 checks, 0 violations; R⁰ = 3 of REV 23.

## 7. After the freeze of P-N5-EPC (14:42Z): the 33 multi-gate fallback-free returns (DATA, READING; written 14:5xZ by date -u)
- r0shape.py with R0V=1 (out/r0shape_r02_list.txt): of the 33 fallback-free returns to configurations with |D_C| ≥ 2 in liball n ≤ 40, 29 change
  σ̄ at ONE vertex on the whole stretch (18 of them in pft34_h3u_P32: D = {0, 32} constant, σ̄(32) constant, σ̄(0) moving among 0's 19 successors);
  4 change it at 2-3 vertices (lev74_n40, nep80_n40 ×2, nep87_n40; all L-RED instances from random starts).
- READING. A single-vertex stretch is not covered by R68's u-runs (D ⊄ {u}). Cutting every Odd v ≠ u to σ̄(v) keeps Ξ (σ̄ stays a best reply in the
  cut game) but not S4a's arena, which uses τ(v) at Odd v; R64's cut ({τ(v), σ̄(v)} at v ∈ D) keeps N5^τ but leaves |D| Odd choice vertices. So a
  "frozen-side u-run" lemma would need a new restriction. OPEN.

## 8. Item (b): what makes a new multi-gate configuration inside a lap (DATA, READING; Lead's GO 14:47Z; written 14:5xZ by date -u)
Tools newconf.py, rootrel.py (out/rootrel_newconf.txt); each instance from its own start.
- New configurations appear only in lap 1. NEWPAIR (contains a pair (q, σ̄(q)) unseen earlier in the phase) against RECOMB (all pairs seen, a new
  combination): nep90 18 / 30 (27 pairs seen, Σ_q deg 29), nep76 20 / 20 (29 pairs, Σ deg 31), long121 7 / 7 (11 pairs, Σ deg 12), pft34 17 / 0. A
  RECOMB boundary changes one vertex in 25 of 30 cases on nep90, mostly the root 0.
- ROOT × RELAY. Let r be the vertex of Q whose σ̄ changes most often (r = 0 on all four: 66 of nep90's 89 boundaries, 57 of nep76's 75, 19 of
  long121's 36) and R := σ̄ on Q ∖ {r} (the relay sub-configuration). nep90 has 16 distinct R, nep76 19, long121 7. Inside one lap, for a fixed R,
  the root's values do not repeat on nep90 / nep76, and lap 2 replays each R's root sequence in the same order (nep90, R = 6: 20 24 19 31 13 23 |
  20 24 19 31 13 23 | 2 26 5 11). The root sweeps its successors in a common order across R (on nep90 20, 24, 19, 31, 13, 23, … recur in this
  order under different R): a sweep through the root's successors by rising value, interleaved with relay toggles. So NCONF ≈ (root sweep length)
  × (relay toggles), sparse: nep90 has 48 configurations against 17 root values × 16 relay sub-configurations.
- Not general: on pft34 (R constant, σ̄(32) never moves) the root repeats inside fallback-free stretches (21 26 21 7 20 three times in one
  phase with f = 1): fallback-free laps of a single root exist; they are the bulk of R⁰_{≥2} (§7) and are single-vertex.
- READING (a route, not a proof). Within one relay sub-configuration and one lap the root behaves like an Odd vertex sweeping a monotone race
  (σ̄(r) = the argmin of Ξ over succ(r), with Ξ non-decreasing); a return of the root under the same R needs an earlier successor's value to fall
  back below the current one relative to the others, which happens on pft34 through self-feedback via the root (L-SI 15's "self-feedback
  through 0"). A bound of the form NCONF_{≥2}(S) ≤ (relay changes in S + 1)·deg(r) on a fallback-free run S would need (i) no root repeat under
  a fixed R inside S, false on pft34, or (ii) a charge of such repeats to a ρ event at a relay. OPEN. The relay changes are L-RED 21's "relay
  D-leaves" (17 on long121, R89) and L-SI 16's "relays acting as second direct roots" (P-N5-ROOT): the two counts this route would need.

## 9. The frozen-side u-run restriction (CONJECTURE with DATA; READING; Lead's word 14:58Z; written 15:0xZ by date -u)
Setting. A FROZEN-SIDE u-STRETCH J = (x, …, y) of a phase P: a maximal run on which σ̄ is constant on Q ∖ {u} (only u's best reply changes).
D⁻ := {v ∈ Q ∖ {u} : σ̄_J(v) ≠ τ(v)}. G^{u|J}: G with every Odd v ∈ D⁻ cut to {τ(v), σ̄_J(v)}, every other Odd v ≠ u cut to τ(v), and u keeping all
its edges. If D⁻ = ∅, J is a u-run and G^{u|J} = G^u (RESULTS R68 (f)); the new case is D⁻ ≠ ∅ (§7: the single-vertex fallback-free returns).
- CONJECTURE RESTRICT_{u|J}. For k ∈ J, RESULTS R64 (a) (i)-(iv) hold with G′_E replaced by G^{u|J}; hence N5^τ on G^{u|J} from (σ_x, τ) reproduces J
  state by state with the same fallback types (as R64 (b) with EPR-1).
- READING (why it should hold; not a proof). (i) holds as in R64: σ̄_k and τ are strategies of G^{u|J} (σ̄_k(v) = σ̄_J(v) on D⁻, = τ(v) elsewhere off
  u, and u keeps every edge), Odd's options only shrink, and S1's counterstrategy is optimal (1E-N3); so Ξ′_k = Ξ_k and W′_k = W_k. Items (ii)-(iv)
  in R64's proof use the same two facts (τ and σ̄_k survive the cut; Odd edges only shrink), as in R68 (f) for G^u and in box 47's RESTRICT_U; I
  have not re-derived them for this cut.
- DATA (fsrestrict.py; XI_V = Ξ on G^{u|J} differs at a state of J, REP_V = N5^τ on G^{u|J} fails to reproduce σ, τ and the fallback type):
  liball n ≤ 34, S3 + 2, seed 7 (out/fsrestrict_liball_n34_k2.txt): 437 stretches, 362 covered by R68 u-runs, 75 frozen-side (244 epochs, max
  |D⁻| 9, max 35 epochs in one stretch), XI_V 0, REP_V 0. nep90 / nep76 / long121 from their starts (out/fsrestrict_long3.txt): 25 / 21 / 12
  frozen-side stretches, 0 / 0 / 0. Control MUT=1 (v ∈ D⁻ cut to τ(v) only): liball S3 XI_V 27, REP_V 16 of 31; nep90 25 / 11, nep76 21 / 8, long121
  12 / 12 (bites). Blind spot: pft34's D⁻ = {32} has two choices with the same top cycle, so the control cannot bite there.
- What it would give (READING). A frozen-side stretch is one N5^τ phase piece on G^{u|J}, a game with one full Odd choice vertex u and |D⁻| Odd
  vertices of out-degree 2 whose best reply is fixed (≠ τ) on the piece. It does NOT reduce to 𝒞^1O: S4a's arena and W need τ(v) at v ∈ D⁻, so v
  cannot be cut to σ̄_J(v) alone. A bound on such pieces would need a 𝒞^1O-type count (R51) that tolerates fixed two-way gates. OPEN.


## 10. Lemma RESTRICT_H: §9's CONJECTURE is PROVED, in a form that covers every in-phase run (PROVED, every game; DATA; successor 28, written 15:25Z by date -u)
Successor 28 (Opus 5.5, D14 / D18, L40), queue item 4 (Lead's GO of 15:16Z). Labels as above; PROVED here means L-NEW 28, unrefereed.
Setting. An ODD CUT of G is a game H with G's vertices, priorities, owners and Even successor lists, in which every Odd v keeps a non-empty
subset succ_H(v) ⊆ succ_G(v). Let J = (x, …, y) be a run of consecutive states of one phase P of N5 on G (τ constant on P). J is H-ADMISSIBLE if,
for every Odd v, τ(v) ∈ succ_H(v) and σ̄_k(v) ∈ succ_H(v) for every k ∈ J. Objects computed by SPEC on H carry a prime.
- Lemma RESTRICT_H (PROVED, every game; standing premise 1E-N3, as R64). If J is H-admissible and k ∈ J, then at the pair (σ_k, τ): (i) Ξ′_k = Ξ_k
  and W′_k = W_k; (ii) Iσ′_k = Iσ_k, S4a's output on H equals its output on G, and S4c's Even switch-all is the same; (iii) Odd's dual valuation of
  τ is the same on H as on G, so Iτ′_k = Iτ_k ∩ E(H); (iv) if k → k+1 is an in-phase transition of N5 on G and Iτ′_k ≠ ∅, then τ is value-optimal
  against σ_k in S4b's arena of H.
- Proof. RESULTS R64 (a)'s proof (packet P-N5-EPR §1), read with H in place of G′_E. It uses exactly three properties of G′_E, and H has each:
  - (P1) every Odd strategy of H is one of G (H's Odd edges are G's): used in (i) (Lemma S (a) on G against S1's counterstrategy on H) and in (iv)
    (every Odd strategy of S4b's arena on H is one of the arena H′_G on G, because Iτ′_k ⊆ Iτ_k by (iii)).
  - (P2) σ̄_k is an Odd strategy of H (admissibility): used in (i) (Lemma S (a) on H: Ξ′_k ⊴ V_{σ_k,σ̄_k} = Ξ_k). R64 needs σ̄_k = σ̄_E for this;
    here it is the definition of admissibility, so k may range over a run on which σ̄ CHANGES.
  - (P3) τ is an Odd strategy of H and Even keeps all its edges (admissibility; definition of an Odd cut): used in (i) for W (G_τ and H_τ are the
    same one-player game), in (ii) (S4a's arena: Even restricted to {σ_k(v)} ∪ Iσ_k(v), Odd to τ(v), the same game on G and H; Iσ is read from Ξ
    and Even's lists; S1 on the dual is deterministic), in (iii) (S1 on G^d for τ runs on the graph with Odd fixed to τ and Even free, the same
    graph for G and H) and in (iv) (τ is a strategy of S4b's arena on H).
  Nothing else of G′_E is used: not that Odd vertices outside D_E have out-degree 1, not that D_E-vertices have out-degree 2, not that σ̄ is
  constant on the run (each item is a statement at ONE state k). □
- Corollary REPRO_H (PROVED, every game; with R64 (b)'s repair EPR-1). Let J = (x, …, y) be H-admissible and y′ := x + len(J) (y + 1 if
  y → y + 1 is in-phase, else y). Then N5^τ on H from (σ_x, τ) passes through (σ_x, τ), …, (σ_{y′}, τ) with the same fallback / non-fallback type
  at each transition as N5 on G, and x, …, y lie in one phase of that N5^τ run; y′ may leave it (EPR-1), unless J ∪ {y + 1} is admissible too.
  Proof: R64 (b)'s induction verbatim, with RESTRICT_H (ii), (iv) at each k ∈ [x, y′ − 1] ⊆ J, and (i) for λ′ = λ on J. □
- Instances (each is "J is H-admissible" by definition):
  | H | J | status |
  | --- | --- | --- |
  | G′_E (Odd v ∉ D_E cut to τ(v), u ∈ D_E to {τ(u), σ̄_E(u)}) | an epoch E | RESULTS R64 (a), (b) |
  | G^u (Odd v ∈ Q ∖ {u} cut to τ(v), u keeps all edges) | a u-run (D ⊆ {u}) | RESULTS R68 (f) RESTRICT_u, REPRO_u |
  | G^{u|J} (§9) | a frozen-side u-stretch | §9's CONJECTURE RESTRICT_{u|J}: now PROVED (this §) |
  | G^P := Odd v cut to {τ(v)} ∪ {σ̄_k(v) : k ∈ P} (the USED-EDGE game of P) | a whole phase P | NEW: every phase of N5 is one N5^τ phase on G^P, from (σ_x, τ), reproduced state by state through its last in-phase transition |
- What it gives (READING). (1) §9's frozen-side stretches are one N5^τ phase piece on G^{u|J}, now as a lemma, not a conjecture; the open part
  named in §9 (a 𝒞^1O-type count that tolerates fixed two-way gates) is unchanged. (2) For any count of a phase, the game may be replaced by
  G^P, whose Odd choices are only those N5 uses in P: QP := #{Odd v with ≥ 2 edges in G^P} and XDEG := Σ_v (|succ_{G^P}(v)| − 1). A bound
  polynomial in n and exponential only in QP (or XDEG) would bound the phase. QP is not bounded here; on nep90 / nep76 / long121 the whole long
  phase lives on a G^P with QP = 5 / 5 / 3 (DATA below), so those instances are N5^τ phases of games with 5 / 5 / 3 Odd choice vertices. (3)
  RESTRICT_H is the honest-frame analogue of a "used-action" reduction (only the actions an algorithm actually plays matter): it makes N5's
  phase a function of the edge set it touches, so the library of small-QP games (𝒞^kO, k ≤ 5) is a complete test bed for these long phases.
- DATA (experiments/new/box48/phrestrict.py; G^P per phase; XI_V = Ξ on G^P differs at a state of P, REP_V = N5^τ on G^P fails to reproduce σ, τ
  and the fallback type at an in-phase transition of P; MUT=1 drops the edge (v, σ̄_x(v)) for one v with σ̄_x(v) ≠ τ(v), must bite):
  nep90 / nep76 / long121 from their starts (out/phrestrict_long3.txt): one phase each (91 / 78 / 121 transitions), QP 5 / 5 / 3, XDEG 22 / 24 / 8,
  XI_V 0, REP_V 0; MUT: XI_V 1 / 1 / 1 (bites on every phase), REP_V 0 / 1 / 1. Library: see the next item.
  liball n ≤ 34 (experiments/new/box47/out/liball.txt), S3 + 2 random, seed 7, as §9 (out/phrestrict_liball_n34_k2.txt): 1,031 phases with ≥ 2
  states, 8,458 in-phase transitions, 147 phases (898 transitions) with QP ≥ 2, max QP 11, max XDEG 20; XI_V 0, REP_V 0. MUT=1
  (out/phrestrict_liball_n34_MUT.txt): 561 phases mutated, XI_V 514, REP_V 292 (bites).
- Labels. PROVED (L-NEW 28, unrefereed): RESTRICT_H, REPRO_H (a port of signed R64 (a), (b); each step is cited above). Consequently §9's
  RESTRICT_{u|J} is PROVED as an instance; §9's DATA stand as consistency checks. DATA: phrestrict.py. READING: "what it gives". OPEN: any bound
  on QP or XDEG per phase; a count of N5^τ phases on games with QP Odd choice vertices (R51 covers QP = 1 under (Στ)).

## 11. QP, the Odd choice vertices of the used-edge game G^P (PROVED (elementary), DATA, READING, OPEN; Lead's routing of 15:38Z; written 15:5xZ by date -u)
Successor 28. Packet P-N5-RESTRICT-box48 (frozen at l-new 7e56744a, sha1 48c63a8e…) §2 defines G^P and QP(P) := #{Odd v : |succ_{G^P}(v)| ≥ 2}.
Tools: experiments/new/box48/qp.py (survey), qpclimb.py (climb), dunion.py (disjoint copies); outputs out/qp_*.txt, out/qpclimb/.
- Remark QP-D (PROVED, elementary). QP(P) = |⋃_{k ∈ P} D_k|: v has ≥ 2 edges in G^P iff σ̄_k(v) ≠ τ(v) for some k ∈ P. So QP = D0 + ENT, D0 := |D_x| at
  the phase's first state, ENT := the vertices that first enter D later in P. (qp.py asserts the identity at every phase.) An epoch boundary can
  add several vertices to D at once, so ENT is not bounded by N_ep − 1; only ENT ≤ |Q| − D0.
- DATA, library (out/qp_liball_n48_k2.txt; liball n ≤ 48, S3 + 2 random, seed 7): large QP occurs only in SHORT phases (max QP 16 in a 1-transition
  phase, ctx7_n30, all of it D0). Long phases have small QP: len ≥ 10: 481 phases, max QP 8; len ≥ 30: 128 phases, max QP 8; len ≥ 60: 27 phases,
  max QP 3 (the 60+ phases are almost all on |Q| = 1 games: selection bias, the library was built around 𝒞^1O). Random 𝒞^kO with k ≈ 0.4n
  (n 10-40, 300 games, S3 + 2): every phase with QP ≥ 4 has 1 transition (scratch run; same shape).
- DATA, climbs (qpclimb.py, score (min(QP, QT), len) of one phase from S3; climb.mutate keeps the Odd choice set O fixed, so QP ≤ |O|):
  random seeds: QT 4 (|O| 6, n ≤ 24) best len 8 with QP 6; QT 6 (|O| 8, n ≤ 32) best len 13 with QP 8 (stopped at step ≥ 2,587 to free a CPU);
  QT 8 (|O| 10) len 0. Seeds nep90 / nep76 / long121 (from S3, where their phases are short): best len 18 / 32 / 47 with QP 5 / 5 / 3 = |Q|.
  So no climb found a long phase with many disagreeing Odd vertices; the climbs are weak (S3 starts; O fixed), and this is not evidence of a bound.
- DUNION (DATA; READING for the mechanism). k disjoint copies of nep90 with copied start (dunion.py: copy i shifts vertices by 40i and priorities by
  an even offset, so parity and the order inside a copy are kept): ONE phase of 91 transitions, N_ep 90, NCONF 48 (unchanged), QP = 5k at n = 40k
  (k = 2, 3, 4; out/qp_dunion.txt; instances/du/nep90x{2,3,4}.pg sha1 b66f7b15 / 7198f9f7 / 9fadc61a). READING: N5 acts on the copies in lockstep
  (each copy's values and improving sets depend only on that copy; checked here as data, not proved from SPEC's S1 procedure). So QP GROWS LINEARLY
  IN n AT FIXED PHASE LENGTH: QP alone is the wrong parameter, and "every phase is an N5^τ phase on a game with QP Odd choice vertices" gives
  nothing when QP is large for this trivial reason.
- The refinement the union suggests: QP_c := max over cycle nodes c of |⋃_k D_k ∩ λ^{-1}(c)| (per class). nep90: QP_c 5, one class; nep90 × 4:
  QP_c 5, four classes. Library: len ≥ 30, max QP_c 8; len ≥ 60, max QP_c 3.
- OPEN. (1) Whether long phases need classes with many disagreeing Odd vertices: a construction with QP_c growing in n on long phases, or a bound
  on QP_c. (2) A per-class decomposition of N5's phase (S4a is one global arena; classes share Even edges that cross between them), which is what
  would make the per-class count usable. (3) The climbs above do not test (1); a climb that adds Odd choice vertices (O not fixed) and starts from
  long-phase start pairs is the next data step.
- Labels. PROVED (elementary): Remark QP-D. DATA: library, climbs, DUNION. READING: lockstep, "QP is the wrong parameter". OPEN: (1)-(3).
- CORRECTION to §10's READING (2) and to frozen P-N5-RESTRICT §4's first READING (for its fixes file; the packet is not edited): nep90, nep76 and
  long121 have |Q| = 5, 5, 3 themselves (qp.py: QP = |Q| on their long phases), so "their long phases live on G^P with QP = 5 / 5 / 3" is true but
  removes nothing there; the reduction G → G^P is informative only where QP < |Q|. No signed or to-sign statement is affected.

## 12. QP_c on long phases: the climb that moves Odd choice vertices, and the R63 reading (DATA, READING, OPEN; Lead's GO 16:01Z; written 16:1xZ by date -u)
Successor 28. Tool experiments/new/box48/qpcclimb.py (sha1 b6e0737d…): genome = game + start pair, seeded from a long-phase instance and its .start;
mutations: box43 climb.mutate (O fixed) with probability 0.85, an O-move (a forced Odd vertex gains an edge and becomes an Odd choice vertex, or an
Odd choice vertex is cut to its start edge) with 0.15; objective max over phases of (QP_c · len, len). n ≤ 48, 3,000 steps each.
- DATA (out/qpcclimb/log_*.txt; each best game re-checked with qp.py and phrestrict.py, out/qpcclimb/verify.txt):
  | seed (its start) | seed: QP_c, len | best: n, |Q|, QP_c (classes), D0, ENT, N_ep, NCONF, len | RESTRICT_H on the best (XI_V, REP_V) | best game sha1 / start sha1 |
  | --- | --- | --- | --- | --- |
  | nep90_n40, seed 51 | 5, 91 | 48, 13, 13 (1), 7, 6, 84, 82, 99 | 0, 0 | 180e8af5 / ac16f911 |
  | nep76_n40, seed 52 | 5, 78 | 48, 14, 14 (1), 10, 4, 46, 41, 81 | 0, 0 | ae540870 / 6b153deb |
  | long121_n40, seed 53 | 3, 121 | 48, 10, 10 (1), 5, 5, 54, 44, 127 | 0, 0 | 77f5b23a / 96641f67 |
  So at n = 48 a phase of 81-127 transitions can have 10-14 disagreeing Odd vertices IN ONE CLASS (every Odd choice vertex of the game disagrees
  with τ at some state of the phase; QP_c = QP = |Q|), with NCONF close to N_ep (82 of 84 on the nep90 descendant). The climbs raised QP_c from
  5 / 5 / 3 to 13 / 14 / 10 without shortening the phase.
- READING. QP_c is not small on long phases: the per-class refinement of §11 does not by itself make the used-edge game a "few Odd choices" game.
  The data are one size (n = 48); they do not show how the maximum QP_c on long phases scales with n (a climb at n = 64, 80 would). Together with
  §11's DUNION: neither QP nor QP_c is a bounded parameter on long phases in the data, and RESTRICT_H's value is as a reduction tool (it lets a
  count be proved on 𝒞^kO-type games with k = QP), not as a size bound.
- R63 reading (READING; RESULTS R63 opened at docs/RESULTS.md "### R63"). (c) D-EPOCH: D is constant on each epoch and changes only at epoch
  boundaries. (a) R-STICK_D and (b) SN-PREFIX_D concern R_D (the vertices whose (σ, τ)-play meets D), not D itself. RESULTS R61 (e) ALT charges a
  clean change of σ̄ at q to a strict rise of κ(q). None of these bounds D0 (the disagreement at the phase start) or ENT (vertices entering D later):
  a vertex enters D when τ(q)'s option stops being Odd's best reply, i.e. when Ξ of τ(q)'s side rises past another option, and nothing landed limits
  how many distinct q do this in one phase. The data above (ENT 4-6 at n = 48 on long phases, D0 5-10) say both terms are used.
- OPEN. (1) Scaling of max QP_c on long phases with n. (2) A count on N5^τ phases of 𝒞^kO games polynomial in n and in k (not n^k): with RESTRICT_H
  this would bound every phase; R61's f = O(n^{k+1}) is exponential in k, and the climbs say k ≈ |Q| on long phases.
- Labels. DATA: the table. READING: the two READING items. OPEN: (1), (2).
