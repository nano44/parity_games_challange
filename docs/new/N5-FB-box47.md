# The fallback count f: one honest frame per configuration (box 47)
L-NEW successor 26 (Opus 5.5), D14 / D18, Lead reading L40; Lead's item of 12:08Z (Lead's stamp): "NEXT ITEM, at ~330k: the fallback count f
itself … Characterize the Odd-binding fallbacks … Data first, if the charge is unclear." Written 2026-10-26 12:15Z onward (date -u). Working doc,
unrefereed. Not a TARGET.md claim; G-N5-TIME stays open.
Labels: PROVED (L-NEW 26, unrefereed) / CONJECTURE / OPEN / DATA / READING / DEAD.
Builds on docs/new/P-N5-HONFF-box47.md (frozen, sha1 98101d1f…, pinned at trunk 4a0a8aba; Lemma FB-RISE) and docs/new/N5-HONFF-box47.md.

## Summary
| § | item | label |
| --- | --- | --- |
| §1 | the τ-frame split: f ≤ (n − 1) + #OB + #SAT (OB = fallbacks where the Odd term binds); the charge of OB to ρ or to epoch changes since the previous fallback FAILS (39 of 50 OB fallbacks have neither; s4c8_n13) | PROVED (split); DEAD (that charge) |
| §2 | Lemma FB-RISE_C: at an in-phase fallback from a state of configuration C, the Ξ-level in the honest frame H_C rises: LEV_C(t + 1) ≥ min(LEV_C(t) + 1, n − 1); the Odd term never binds there | PROVED (every game) |
| §2 | Theorem FB-C: in every phase, f ≤ |𝒞_f(P)| · (4n² − 3n), 𝒞_f(P) := the configurations σ̄|Q at the sources of P's fallbacks | PROVED (every game) |
| §3 | corollaries (the N_ep form is weaker than landed R60 (c) EPOCH, f ≤ 1 + n·N_ep; see §3): f ≤ (4n² − 3n)·min(N_ep, Π_q deg q); on 𝒞^kO f ≤ Δ^k(4n² − 3n); phases with all |D| ≤ 1: f ≤ (1 + m)(4n² − 3n) | PROVED |
| §4 | data | DATA |
| §5 | what is open | OPEN / READING |

## 0. Setting (every game)
As docs/new/P-N5-HONFF-box47.md §0 (N5 = SPEC S1-S5; state k; σ̄_k; Ξ_k; W_k; λ; phase P; in-phase; value(r); (MON); (V1), (V2)). Q := the Odd
vertices of out-degree ≥ 2. A CONFIGURATION is C = σ̄|Q; k is a C-STATE if σ̄_k|Q = C. H_C := G with every Odd v cut to its one edge σ̄_C(v)
(σ̄_C(v) := C(v) for v ∈ Q; the unique successor otherwise); H_{τ|Q} = G_τ. At a C-state k the honest play from every vertex is a play of the
one-player game H_C, so Ξ_k = σ_k's valuation in H_C.
LEV_C(k) := the largest j ≤ n − 1 such that Ξ_k(x) ⪰ value(r) for every vertex x and every simple path r of H_C with ≤ j edges from x to a cycle
node of λ. It is defined at EVERY state of P (not only at C-states), and it is non-decreasing along P: H_C and λ are fixed on P and Ξ is
non-decreasing (MON). B_C(x) := the maximum of value(r) over all simple H_C-paths r from x to a cycle node of λ. LEV(k) of P-N5-HONFF is LEV_{τ|Q}.

## 1. The τ-frame split, and a charge that fails
- PROVED (from FB-RISE (a), P-N5-HONFF §1). Classify each in-phase fallback t → t + 1 of P by LEV := LEV_{τ|Q} and LEV_odd: NB if LEV(t) < n − 1 and
  LEV_odd(t) > LEV(t); OB (Odd-binding) if LEV_odd(t) ≤ LEV(t) < n − 1; SAT if LEV(t) = n − 1. At an NB fallback LEV(t + 1) ≥ LEV(t) + 1, and LEV is
  non-decreasing with values in {0, …, n − 1}, so P has at most n − 1 NB fallbacks: f ≤ (n − 1) + #OB + #SAT.
- PROVED (elementary). At an OB fallback the binding Odd vertices q (Ξ_t(q) ≺ value(r) for some r = q → τ(q) → r′, |r′| ≤ LEV(t)) lie in D_t: if
  σ̄_t(q) = τ(q), (V1)/(V2) give Ξ_t(q) = q ⊕ Ξ_t(τ(q)) ⪰ q ⊕ value(r′) = value(r) (own-cycle-node case as SAT0's). DATA: BIND_NOTD = 0, §4.
- DEAD (the charge the Lead's item asked about first, in its simplest form): "every OB fallback has a ρ event (a change of Ξ(q), q ∈ Q) or an
  epoch change between it and the previous fallback of the phase". fbcount.py on the 735-file list, n ≤ 20: 50 OB fallbacks, 39 with neither.
  Instance: experiments/red/so/instances/s4c8_n13.pg (n 13), one phase with 8 OB fallbacks and 1 ρ-transition (OB − ρT = 7). Also j5_n16
  (experiments/red/xing/instances), S3, phase [6, 28]: fallbacks 13 and 16 with the identical vector of per-vertex G_τ-levels. Obstruction (DATA,
  fbpot.py): those 39 fallbacks are not Ξ-flat (POT_FLAT_XIUP_OB 39, XIFLAT_OB 0): Ξ rises, but between two path values of G_τ, so no G_τ-level
  (per vertex or global) can see them. The τ-frame is the wrong frame for the Odd-binding fallbacks.

## 2. Lemma FB-RISE_C and Theorem FB-C (PROVED, every game)
Lemma FB-RISE_C. Let t → t + 1 be an in-phase S4c fallback of P whose source t is a C-state. Then LEV_C(t + 1) ≥ min(LEV_C(t) + 1, n − 1).
Proof. P-N5-HONFF's proof of FB-RISE (a), with G_τ replaced by H_C, LEV by LEV_C, and the Odd case done directly. Let x be a vertex, u a cycle node
of λ, r a simple H_C-path from x to u with 1 ≤ |r| ≤ min(LEV_C(t) + 1, n − 1) (|r| = 0 is trivial); r = x → z → r′, r′ avoiding x, |r′| ≤ LEV_C(t),
so Ξ_t(z) ⪰ value(r′).
- x Odd. Then z = σ̄_C(x) = σ̄_t(x) (t is a C-state; outside Q, x has one successor), so x's honest play at t is x followed by z's. If λ(x) ≠ x, (V1)
  gives Ξ_t(x) = x ⊕ Ξ_t(z) with z's path to λ(x) avoiding x, and (V2) (r′ avoids x) gives Ξ_t(x) ⪰ x ⊕ value(r′) = value(r). If λ(x) = x, then
  Ξ_t(x) = (x, ∅, 0) and z's honest play returns to x, so Ξ_t(z) has cycle node x while value(r′) has cycle node u ≠ x; Ξ_t(z) ⪰ value(r′) makes x
  better than u, and (x, ∅, 0) ≻ value(r). Then Ξ_{t+1}(x) ⪰ Ξ_t(x) (MON).
- x Even. Items 2 and 3 of FB-RISE (a)'s proof verbatim: they use only the edge (x, z) of G (Even vertices keep all their edges in H_C as in G_τ),
  Ξ_t(z) ⪰ value(r′), the fallback rule (S4c: z*(x) = the (Ξ_t(w), w)-maximum of Iσ_t(x); FIX 3), Lemma P's Case A with Ω := Ξ_t (question Q-A of
  P-N5-HONFF), (MON), (V1)/(V2) at t + 1 and λ_{t+1} = λ. None of them uses the frame of r′. □
- READING. In the τ-frame an Odd vertex of D can undercut its τ-path, and FB-RISE needs the honest state h to put it one level ahead. In the
  honest frame H_C of the source's own configuration, every Odd vertex follows its frame edge, so its level is automatically one ahead (the
  same fact as SAT0's Odd case, with σ̄_C in place of τ). So in H_C a fallback is a full Bellman-Ford relaxation, at every vertex.
Lemma SAT_C. If t is a C-state of P with LEV_C(t) = n − 1, then Ξ_t = B_C; and if t < t′ are C-states of P with LEV_C(t) = n − 1, then Ξ is constant on
the states t, …, t′ and t′ − t ≤ 4n(n − 1).
Proof. At a C-state the honest play from x follows a simple H_C-path r_x to its first visit of λ(x), so Ξ_t(x) = value(r_x) ⪯ B_C(x) (as HON step 2);
LEV_C(t) = n − 1 gives Ξ_t ⪰ B_C. For t′: Ξ_t = B_C ⪰ Ξ_{t′} (t′ a C-state) ⪰ Ξ_t (MON), so Ξ_{t′} = Ξ_t and, Ξ being non-decreasing, Ξ is constant
on t, …, t′. τ is constant on P, so Ωτ is too, and RESULTS R15 (d) (at most 4n(n − 1) consecutive iterations leave both Ωσ = Ξ and Ωτ
unchanged) gives t′ − t ≤ 4n(n − 1). □
Theorem FB-C. In every phase P of N5 on every game, f ≤ |𝒞_f(P)| · (4n² − 3n), where 𝒞_f(P) is the set of configurations of the sources of P's
in-phase fallbacks.
Proof. Fix C ∈ 𝒞_f(P) and let t_1 < … < t_N be the sources of the fallbacks of P that are C-states. Unsaturated ones (LEV_C(t_i) ≤ n − 2): by
FB-RISE_C, LEV_C(t_i + 1) ≥ LEV_C(t_i) + 1, and LEV_C is non-decreasing on P, so LEV_C(t_{i+1}) ≥ LEV_C(t_i) + 1 for consecutive unsaturated ones;
with values in {0, …, n − 2} there are at most n − 1 of them. Saturated ones (LEV_C(t_i) = n − 1): by SAT_C they lie in a window of at most
4n(n − 1) + 1 consecutive states, so there are at most 4n(n − 1) + 1 of them. So N ≤ (n − 1) + 4n(n − 1) + 1 = 4n² − 3n; sum over C. □
- The fallback count no longer restarts when a configuration recurs: LEV_C is a level of the whole phase, read in a fixed frame, and every return
  to C finds it where it was left.
- For C = τ|Q (the D = ∅ configuration), H_C = G_τ and FB-RISE_C is FB-RISE's general form with the Odd term automatically ≥ LEV + 1 at D = ∅
  sources; the HON-FF route (P-N5-HONFF) is the honest-state version of the same relaxation.

## 3. Corollaries (PROVED)
Let P be a phase.
(a) |𝒞_f(P)| ≤ the number of distinct configurations visited in P ≤ min(N_ep(P), Π_{q ∈ Q} deg(q)) (each epoch has one configuration; a
    configuration is a choice of successor at each q ∈ Q). So f ≤ (4n² − 3n) · min(N_ep(P), Π_q deg(q)).
(b) On a game with k Odd vertices of out-degree ≥ 2 (𝒞^kO) and maximum out-degree Δ: f ≤ Δ^k · (4n² − 3n) per phase. For bounded Δ and fixed k
    this is O(n²). (RESULTS R61 Corollary FB-kO gives f = O(n^{k+1}) on 𝒞^kO; (b) is a different trade, exponential in k through Δ^k, quadratic in n.)
(c) If every state of P has |D_k| ≤ 1, the configurations visited are τ|Q and, for each u ∈ Q and y ∈ succ(u) ∖ {τ(u)}, τ|Q with u moved to y: at
    most 1 + Σ_{q ∈ Q}(deg(q) − 1) ≤ 1 + m. So f ≤ (1 + m)(4n² − 3n). Generally the configurations with |D| ≤ d number at most
    Σ_{j ≤ d} C(|Q|, j)·(Δ − 1)^j.
(d) With RESULTS R61 (f) (N_ep ≤ 1 + Σ_q (ρ_q + tie_q + nc_q + cyc_q)): f ≤ (4n² − 3n)(1 + Σ_q (ρ_q + tie_q + nc_q + cyc_q)). RESULTS R56's
    f ≤ 1 + (n − 1)(2 + ρ) has the better factor (n − 1 against 4n² − 3n) but counts ρ; (a) counts distinct configurations, which can be far
    fewer than epochs (a configuration that recurs is paid once). The two are incomparable in general.
- CORRECTION (12:34Z by date -u, after the Lead's GO; found while collecting quotes): RESULTS R60 (c) Lemma EPOCH (landed; P-N5-ACCEL, L-NEW successor 23)
  already gives f ≤ 1 + n·N_ep on every game, by the same mechanism inside one epoch (fallbacks relax the honest frame G_E in κ; docs/RESULTS.md
  l. 3076-3079). So (a)'s N_ep form and (d) are WEAKER than a landed result, and §1-§2 should have cited EPOCH. What FB-C adds over EPOCH is only
  this: the level is read in the configuration's frame over the WHOLE phase, so the count is per distinct configuration, not per epoch (a
  configuration that recurs is paid once), at the price of the factor 4n² − 3n against n. (b) and (c) are stated in configurations and are not
  implied by EPOCH (an epoch count can exceed the configuration count: 1,399 epochs against 257 configurations at n ≤ 34, §4).
- READING (where this sits). Theorem FB-C turns "f per phase" into "distinct configurations per phase". For fixed k and bounded degree it is
  polynomial with no hypothesis. Its weak point is the factor Π_q deg(q): it is exponential in the number of Odd choice vertices, which is the
  N_ep / configuration question again, not a new one.

## 4. DATA (experiments/new/box47/; outputs in out/)
- fbcount.py (τ-frame split, §1): 735-file list n ≤ 20, S3 + 2 random, seed 5: 912 runs, 72 phases with a fallback, f 170 = NB 90 + OB 50 + SAT 30;
  NB_V 0, NBC_V 0, BIND_NOTD 0, BIND_EMPTY 0; OB with a ρ event since the previous fallback 11, with an epoch change 9, with neither 39 (CHARGE_V 11
  phases); max OB in a phase 8 (s4c8_n13); max SAT in a phase 1.
- fbpot.py (per-vertex G_τ-levels): same sample: POT_FLAT_OB 39 (all 39 with Ξ rising: POT_FLAT_XIUP_OB 39), POT_FLAT_SAT 30 (29 of them Ξ-flat).
- fbconf.py (Theorem FB-C): FBC_V = LEV_C(t + 1) < min(LEV_C(t) + 1, n − 1) (must be 0); NSC_V = more than n − 1 unsaturated fallbacks of one
  configuration in a phase (must be 0); LEVC_MONO_V = LEV_C fell between two fallbacks of one configuration (must be 0).
| sample | runs | phases with a fallback | f | FBC_V | NSC_V | LEVC_MONO_V | max unsaturated per C in a phase | max saturated per C | Σ distinct configurations / Σ epochs / Σ ρ-transitions (these phases) | max f in a phase (configurations) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 735-file list, n ≤ 20, S3 + 2 random, seed 5 | 912 | 72 | 170 | 0 | 0 | 0 | 12 (wd16_s2, n 16) | 1 | 73 / 144 / 102 | 12 (1) |
| 735-file list, n ≤ 34, S3 + 2 random, seed 6, budget 3·10⁶ (UNK 15 phases) | 1,527 | 214 | 768 | 0 | 0 | 0 | 25 (farrise25_n32) | 1 | 257 / 1,399 / 1,403 | 25 (1); max 4 configurations (zcl_rx_n32) |
| experiments/red/fbr/instances/fr39_q4_n48.pg with L-RED's start (n5py_start of its .start.json, copied to box47/instances/fr39_q4_n48.start), budget 5·10⁷ | 1 | 1 | 39 | 0 | 0 | 0 | 24 (n − 1 = 47) | 0 | 7 / 11 / 15 | 39 (7) |
| random 3,000 𝒞^kO (n 5-18, gseed 111), S3 + 4 random, seed 8 | 15,000 | 553 | 553 | 0 | 0 | 0 | 1 | 1 | 553 / 558 / 20 | 1 (1) |
- Distinct configurations are far fewer than epochs where fallbacks are many (257 against 1,399 at n ≤ 34; max epochs − configurations in a
  phase 45, x31_rx32): Corollary (a) pays a recurring configuration once.
- Control: the τ-frame version of the same count (fbcount.py / ffdeep.py CTRL_T) fails on 39 of 50 OB fallbacks (n ≤ 20) and 636 times in the
  HONFF samples; the H_C version never fails.

## 5. OPEN, and what this changes (READING)
- OPEN: the number of distinct configurations visited per phase on general games (Π_q deg(q) in the worst case). This is the configuration side of
  N_ep; Theorem FB-C does not touch it.
- OPEN: a better saturated term. Data: at most 1 saturated fallback per configuration and phase (S_C max 1); Lemma SAT_C pays 4n(n − 1) + 1. A
  HON-FB-type argument (a fallback at a saturated C-state is flat and ends the phase) would bring the total to f ≤ n·|𝒞_f(P)|. Not proved.
- The Lead's question "charge each Odd-binding fallback to a ρ event or an epoch change": in the τ-frame, DEAD in its simplest form (§1). In the
  honest frame the question disappears: the Odd-binding fallbacks are, per configuration, ordinary rises of LEV_C.
