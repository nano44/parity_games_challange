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

