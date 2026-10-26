# Packet P-N5-FBC (box 47): in the honest frame H_C of a configuration C, an in-phase fallback raises the Ξ-level (Lemma FB-RISE_C), so in every phase of N5 the in-phase fallbacks number at most (distinct configurations at fallback sources) × (4n² − 3n) (Theorem FB-C) — every game
L-NEW successor 26 (Opus 5.5), D14 / D18, Lead reading L40; Lead's GO of 12:32Z (Lead's stamp): "GO: freeze P-N5-FBC-box47 with FB-RISE_C, SAT_C, Theorem FB-C and
corollaries (a)-(d)." Written 2026-10-26 12:34Z onward (date -u). FROZEN at push: later text goes into a fixes file.
Source: docs/new/N5-FB-box47.md (working doc, l-new fc8b88c4 and later; this packet governs). Tools: experiments/new/box47/fbconf.py (fbcount.py,
fbpot.py for the τ-frame context).
Labels: PROVED (L-NEW 26, unrefereed) / OPEN / DATA / READING / DEAD. Not a TARGET.md claim; no running-time bound; G-N5-TIME stays open.
What this is and is not, plainly:
- It bounds f per phase by the number of DISTINCT CONFIGURATIONS σ̄|Q at fallback sources. That number per phase is OPEN on general games
  (Π_q deg(q) in the worst case); nothing here bounds it.
- It is INCOMPARABLE with RESULTS R56 (f ≤ 1 + (n − 1)(2 + ρ)): R56 counts ρ with factor n − 1; FB-C counts distinct configurations with factor
  4n² − 3n.
- It is the per-configuration, whole-phase form of RESULTS R60 (c) Lemma EPOCH (landed; f ≤ 1 + n·N_ep, the same Bellman-Ford mechanism in κ,
  restarting at every epoch). Its Corollary (a) in the N_ep form, and Corollary (d), are WEAKER than EPOCH (c) and are kept only as stated
  consequences; the new content is that a configuration that recurs is paid once (Theorem FB-C, Corollaries (b), (c)).
Relation to P-N5-HONFF (sha1 98101d1fe723a570f3c79085b929a456ebb7dff5, pinned at trunk 4a0a8aba, in the referee queue): FB-RISE_C is FB-RISE (a)'s
proof read in the frame H_C instead of G_τ; its Even part is P-N5-HONFF §1 items 2-3 verbatim. If REFEREE or REFEREE-2 answers P-N5-HONFF's
question Q-A "no", FB-RISE_C falls with it.

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Lemma FB-RISE_C: at an in-phase fallback from a C-state, LEV_C(t + 1) ≥ min(LEV_C(t) + 1, n − 1) | PROVED (to sign) |
| §1 | Lemma SAT_C: LEV_C(t) = n − 1 at a C-state gives Ξ_t = B_C, and the later C-states of the phase lie within 4n(n − 1) transitions | PROVED (to sign) |
| §1 | Theorem FB-C: f ≤ |𝒞_f(P)| · (4n² − 3n) | PROVED (to sign) |
| §2 | Corollaries (a)-(d) | PROVED (to sign); (a)'s N_ep form and (d) weaker than R60 (c) |
| §3 | the τ-frame split and its dead charge (context) | PROVED / DEAD (context, not to sign) |
| §4 | data | DATA (not to sign) |
| §5 | open items | OPEN (not to sign) |
- Premises (LANDED or pinned):
  - SPEC S1-S5 of docs/new/N5-ssi-global.md (FIX 1-4, Q1-Q4): S2 (Iσ = Ξ-improving edges), S4c's rule and FIX 3 (§6 quotes). Standing premise
    1E-N3 (RESULTS R57).
  - (MON): RESULTS R15 (a), (d) (Ξ non-decreasing along a run, S4c included); RESULTS R15 (d)'s "at most 4n(n−1) consecutive N5 iterations leave
    both Ωσ and Ωτ unchanged" (Ωσ read as S1's Ξ, as every per-phase packet does).
  - RESULTS R17 (a) (V1), (V2); R17 (b) Lemma P's Case A (A1, A2) with Ω := Ξ_t (P-N5-HONFF's question Q-A); RESULTS R38 (a) (phases).
  - P-N5-HONFF §1, the proof of FB-RISE (a), items 2 and 3 (Even vertices), used verbatim.
  - For Corollaries (a), (d) only: RESULTS R61 (f) (N_ep ≤ 1 + Σ_q (ρ_q + tie_q + nc_q + cyc_q)); for context RESULTS R56 (f), R60 (c), R61 FB-kO.

## 0. Setting (every game)
As P-N5-HONFF §0 (state k, σ̄_k, Ξ_k, λ, phase P, in-phase, value(r)). Q := the Odd vertices of out-degree ≥ 2. A CONFIGURATION is C = σ̄|Q; k is a
C-STATE if σ̄_k|Q = C. H_C := G with every Odd v cut to its one edge σ̄_C(v) (σ̄_C(v) := C(v) for v ∈ Q, the unique successor otherwise); H_{τ|Q} = G_τ.
At a C-state k the honest play from every vertex is a play of the one-player game H_C, so Ξ_k is σ_k's valuation in H_C.
LEV_C(k) := the largest j ≤ n − 1 such that Ξ_k(x) ⪰ value(r) for every vertex x and every simple path r of H_C with ≤ j edges from x to a cycle
node of λ; defined at EVERY state of P, non-decreasing along P (H_C and λ fixed on P; (MON)). B_C(x) := the maximum of value(r) over the simple
H_C-paths r from x to a cycle node of λ. 𝒞_f(P) := the configurations of the sources of P's in-phase S4c fallbacks.

## 1. Lemma FB-RISE_C, Lemma SAT_C, Theorem FB-C (PROVED, every game)
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

## 2. Corollaries (PROVED)
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
  l. 3076-3079). So (a)'s N_ep form and (d) are WEAKER than a landed result, and the working doc's first version should have cited EPOCH (this packet's header does). What FB-C adds over EPOCH is only
  this: the level is read in the configuration's frame over the WHOLE phase, so the count is per distinct configuration, not per epoch (a
  configuration that recurs is paid once), at the price of the factor 4n² − 3n against n. (b) and (c) are stated in configurations and are not
  implied by EPOCH (an epoch count can exceed the configuration count: 1,399 epochs against 257 configurations at n ≤ 34, §4).
- READING (where this sits). Theorem FB-C turns "f per phase" into "distinct configurations per phase". For fixed k and bounded degree it is
  polynomial with no hypothesis. Its weak point is the factor Π_q deg(q): it is exponential in the number of Odd choice vertices, which is the
  N_ep / configuration question again, not a new one.

## 3. Context (not to sign): the τ-frame split and a dead charge
- In the τ-frame (LEV, LEV_odd of P-N5-HONFF), FB-RISE (a) splits the fallbacks into NB (LEV rises; ≤ n − 1 per phase), OB (Odd-binding: LEV_odd ≤ LEV
  < n − 1) and SAT; the binding Odd vertices lie in D_t. DEAD: "each OB fallback has a ρ event or an epoch change since the previous fallback"
  (experiments/red/so/instances/s4c8_n13.pg: 8 OB fallbacks, 1 ρ-transition in one phase; j5_n16). Those fallbacks raise Ξ strictly between two
  path values of G_τ, invisible to every τ-frame level. The honest frame removes the Odd term (FB-RISE_C's Odd case).

## 4. DATA (not to sign; experiments/new/box47/fbconf.py, outputs in experiments/new/box47/out/)
FBC_V = FB-RISE_C fails; NSC_V = more than n − 1 unsaturated fallbacks of one configuration in a phase; LEVC_MONO_V = LEV_C fell between two
fallbacks of one configuration (all must be 0).
| sample | runs | phases with a fallback | f | FBC_V | NSC_V | LEVC_MONO_V | max unsaturated per C in a phase | max saturated per C | Σ distinct configurations / Σ epochs / Σ ρ-transitions (these phases) | max f in a phase (configurations) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 735-file list, n ≤ 20, S3 + 2 random, seed 5 | 912 | 72 | 170 | 0 | 0 | 0 | 12 (wd16_s2, n 16) | 1 | 73 / 144 / 102 | 12 (1) |
| 735-file list, n ≤ 34, S3 + 2 random, seed 6, budget 3·10⁶ (UNK 15 phases) | 1,527 | 214 | 768 | 0 | 0 | 0 | 25 (farrise25_n32) | 1 | 257 / 1,399 / 1,403 | 25 (1); max 4 configurations (zcl_rx_n32) |
| experiments/red/fbr/instances/fr39_q4_n48.pg with L-RED's start (n5py_start of its .start.json, copied to box47/instances/fr39_q4_n48.start), budget 5·10⁷ | 1 | 1 | 39 | 0 | 0 | 0 | 24 (n − 1 = 47) | 0 | 7 / 11 / 15 | 39 (7) |
| random 3,000 𝒞^kO (n 5-18, gseed 111), S3 + 4 random, seed 8 | 15,000 | 553 | 553 | 0 | 0 | 0 | 1 | 1 | 553 / 558 / 20 | 1 (1) |
- Control: the τ-frame count (fbcount.py) fails on 39 of 50 Odd-binding fallbacks (n ≤ 20); ffdeep.py's CTRL_T fails 636 times (P-N5-HONFF §3).

## 5. OPEN
- The number of distinct configurations visited per phase on general games (the configuration side of N_ep).
- A better saturated term: data show at most 1 saturated fallback per configuration and phase; SAT_C pays 4n(n − 1) + 1. A HON-FB-type flatness
  argument would give f ≤ n·|𝒞_f(P)|; in H_C, Ξ = B_C does not exclude a cycle with a better top through a gate, so it is not proved.

## 6. Quotes and pins (checked by script)
Every quote below, set in curly double quotes, is verbatim from the file and line named, at l-new 80509398.
- SPEC, docs/new/N5-ssi-global.md (sha1 66fde9ef1726602fc0a52ca8d6d6fe8cbbcf110e) l. 56-57: “FALLBACK, if σ_new = σ and τ_new = τ: if Iσ ≠ ∅, for
  every Even v with an improving edge set σ_new(v) = the w with (v, w) ∈ Iσ maximising (Ξσ(w), w) (best valuation, ties: larger index)”; FIX 3,
  l. 88: “In a fallback iteration with Iσ ≠ ∅ only σ changes (τ_new = τ)”.
- RESULTS R15 (a), docs/RESULTS.md l. 631: “Ωσ ⊴ Ω_{Switch_I(σ)}”; R15 (d), l. 642-643: “at most 4n(n−1) consecutive N5 iterations leave both Ωσ and
  Ωτ unchanged”.
- R60 (c) Lemma EPOCH, l. 3076: “Lemma EPOCH: for every phase and epoch E”; l. 3079: “(c) f ≤ 1 + n·N_ep.”
- R56 (f), l. 2865: “f ≤ 1 + (n − 1) + (n − 1)(1 + ρ) = 1 + (n − 1)(2 + ρ).”
- R61 (f), l. 3132: “N_ep ≤ 1 + Σ_{q ∈ Q} (ρ_q + tie_q + nc_q + cyc_q)”; R61 FB-kO, l. 3125: “for fixed k, f = O(n^{k+1})”.
- (V1), (V2), Lemma P's Case A: docs/new/N5-phase-bound-box10.md (sha1 e1a275294232ca4d94d44952fa91312b2f1fcf2e) l. 20-21: “(V1) if x is not its own
  cycle node then Ω_ρ(x) = x ⊕ Ω_ρ(ρ(x)) and the ρ-path from ρ(x) to λ(x) avoids x.”; l. 32: “Case A: (x, z) ∉ I_k, i.e. Ω_k(z) ⪯ Ω_k(ρ_k(x)).”
- P-N5-HONFF items 2-3, docs/new/P-N5-HONFF-box47.md l. 56: “2. x Even and z ∉ Iσ_t(x), i.e. Ξ_t(z) ⪯ Ξ_t(σ_t(x)).”; l. 58: “3. x Even and z ∈ Iσ_t(x).”
- HON step 2's pattern for SAT_C, docs/new/P-N5-HON-box46.md l. 77: “R15 (d) gives h_N − t ≤ 4n(n − 1), hence N − s ≤ 4n(n − 1) + 1.”
- Pins: P-N5-HONFF-box47.md sha1 98101d1fe723a570f3c79085b929a456ebb7dff5; working doc docs/new/N5-FB-box47.md sha1 9ad340b27b4af15578288882ac46ea33c8d9335f; fbconf.py sha1 a5932c09140a63b2d3e2f4ed396cf91074c4a3a6.
- Script: `python3 experiments/new/box47/quotecheck.py docs/new/P-N5-FBC-box47.md 80509398 docs/new/N5-ssi-global.md docs/RESULTS.md
  docs/new/N5-phase-bound-box10.md docs/new/P-N5-HONFF-box47.md docs/new/P-N5-HON-box46.md` (output experiments/new/box47/out/quotecheck_fbc.txt).
