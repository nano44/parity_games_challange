# N5 on 𝒞^1O: fallbacks per phase are O(n²), with no crossing term (Theorem FB-PHASE), so crossings per phase are polynomial (Corollary FX), and a phase is polynomial given its wakes K (box 14)
L-SI successor 9 (Opus 5.5; D18, L40), session_018jN1MJkw56F58G3qcfcuZA. Written 2026-10-25 18:48Z (date -u). Lead's GO 18:25Z, item (2).
Lane write-up, not a packet.

Labels:
- PROVED (L-SI 9): my proof, unrefereed.
- RESTATED: an existing lane or packet proof, re-checked here with the change named.
- READING; DATA; OPEN.

Scope: the candidate N5 (SPEC S1-S5, docs/new/N5-ssi-global.md) on 𝒞^1O, inside one phase. Not a running-time bound for N5, not a
TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN.

What this does to the ledger (docs/si/N5-LEDGER-box14.md, sha1 c54e8560, frozen):
- It closes weakest link 1, the f ↔ X loop, GIVEN the dependencies below.
- What is left on 𝒞^1O is K (wakes per phase, link 2) and the signature of Lemma Φ (link 3).

## 0. Setting, notation, dependencies
- Phase, U, Û := U ∖ {o}, g_1 < g_2 < … (the in-phase Even S4c fallbacks), Iσ_k (gates), honest frame Ξ, λ, next, θ, c_θ, R, R̄, F,
  (V1), (A), (A0), (M1′), (M2′), (INJ), (HP), (SP): exactly as in docs/new/P-N5-RHO-box40.md §0 (pinned c8144551; signed by both
  referees). d_o := deg(o).
- In a phase every transition is an S4a step or an Even S4c fallback (RHO §0). S4c switches EVERY Even v that has a gate, to its
  Ξ-best gate target (P-N5-PFZ §0).
- CLASSES. For a cycle node c of the phase (λ(c) = c), U_c := λ^{-1}(c).
  - The classes partition V. U_{c_θ} = U. For c ≠ c_θ, o ∉ U_c, so every Odd vertex of U_c is forced.
  - wt_c(v) := sgn(v)·2^rank(v) if rank(v) > rank(c), else 0. s_c := +1 if Ω(c) is odd, −1 if even.
  - κ_t(z) := (M_t(z), s_c·ℓ(Ξ_t z)) for z ∈ U_c, where M_t(z) is the signed weight of P(Ξ_t z). κ is compared lexicographically.
  - G_{U_c}: the graph on U_c in which Even v ∈ U_c ∖ {c} keeps its edges into U_c and Odd vertices keep their forced edge. Its
    TERMINALS are c, and also o when c = c_θ; terminals are sinks.
- Class forms of the RHO §0 facts. Proofs as there, with c for c_θ; the length half of (A) is RHO's own "ℓ(Ξ_t z) = 1 + ℓ(Ξ_t next_t z)".
  - (Aκ) For z ∈ U_c ∖ {c}: next_t(z) ∈ U_c and κ_t(z) = (wt_c(z), s_c) + κ_t(next_t z).
  - (M1κ) For y, z ∈ U_c at states t, t′ of the phase: Ξ_t(y) ⊴ Ξ_{t′}(z) ⇔ κ_t(y) ≤ κ_{t′}(z). This is RHO (M1′)'s iff form.
  - (M2κ) κ_{t+1}(z) ≥ κ_t(z) at every in-phase transition. This is R15 (a) + (M1κ).
- Dependencies:

| tag | statement used | where | status |
| --- | --- | --- | --- |
| R15 (a), (d) | Ξ never decreases; σ_{k+1}(v) ∈ {σ_k(v)} ∪ Iσ_k(v) | RESULTS R15 | LANDED |
| (SG) | at any N5 transition a switched Even y with λ(y) ≠ y gains strictly | RESULTS R19 (d) | LANDED |
| CN, (C5) | in-phase own-cycle-node switch has gate level −1; a ◁ b ⊴ c ⇒ lev(a, b) ≤ lev(a, c) | RESULTS R29 (d), (a) | LANDED |
| CN-LAST | an Even fallback all of whose gates have λ(y) = y and level −1 ends its phase | RESULTS R38 (f) | LANDED |
| X_SN | S4a crossings at states with c_w = c_θ per phase ≤ 13(d_o + 1)n³(f + 1 + T) + T | RESULTS R34 (f) | LANDED |
| R-STICK | at an S4a step from a state with c_w ≠ c_θ, R_s ⊆ R_{s+1} | RESULTS R30 (c) | LANDED |
| OX (v) | T_P ≤ (m − n + 1)((n + 1)(2f + 2X + K + 1)n(n − 1) + X + 1) | RESULTS R28 (c) | LANDED |
| FB-ROUND | every in-phase Even fallback is a Bellman-Ford round on U (M form) | P-N5-PFZ §1 | SIGNED-IN-LANDING (both) |
| P-FREEZE | M = Mopt_Θ on U after \|U\| − 1 fallbacks of a θ-run Θ | P-N5-PFZ §2 | SIGNED-IN-LANDING (both) |
| HAT-FREEZE | M = MoptÛ on F_t ∩ U after g_{\|U\|−2} | P-N5-RHO §2 | SIGNED-IN-LANDING (both) |

## 1. Lemma κ-ROUND (RESTATED: P-N5-PFZ §1 for κ and for every class; the κ form for U is L-NEW 19's κ-FB-ROUND, N5-FBCAP-route §1)
Statement. Let k → k+1 be an in-phase Even S4c fallback, and c a cycle node of the phase. For every Even v ∈ U_c ∖ {c} and every
successor x ∈ U_c of v: κ_{k+1}(v) ≥ (wt_c(v), s_c) + κ_k(x).
Proof. FB-ROUND's two cases, with κ for M.
- Case 1: Ξ_k(x) ⊴ Ξ_k(σ_k v). Then (wt_c(v), s_c) + κ_k(x) ≤ (wt_c(v), s_c) + κ_k(σ_k v) = κ_k(v) ≤ κ_{k+1}(v), by (M1κ), (Aκ) at k and
  (M2κ).
- Case 2: (v, x) ∈ Iσ_k. S4c sets σ_{k+1}(v) = x* with Ξ_k(x*) ⊵ Ξ_k(x).
  - In-phase: λ_{k+1}(v) = c ≠ v. So (Aκ) at k+1 gives x* ∈ U_c and κ_{k+1}(v) = (wt_c(v), s_c) + κ_{k+1}(x*).
  - (M2κ), then (M1κ): κ_{k+1}(x*) ≥ κ_k(x*) ≥ κ_k(x). □
- Nothing about θ, H1-H3, τ(o) or c_w is used.

## 2. Lemma κ-FREEZE (RESTATED: P-N5-PFZ §2 for κ; part (ii) is new only in that it is applied to a class without o)
Statement.
- (i) Let Θ be a θ-run, and f_1 < f_2 < … its Even fallbacks with both ends in Θ. Put κ_Θ(o) := κ(θ), which is constant on Θ, and
  κ(c_θ) := (0, 0). Let κopt_Θ(z) be the maximum, over simple paths p of G_U from z to a terminal, of
  Σ_{u ∈ p ∖ end} (wt(u), s_θ) + κ_Θ(end). Then κ_t = κopt_Θ on U for every t ∈ Θ with t > f_{|U|−1}.
- (ii) Let c ≠ c_θ, and let κopt^c(z) be the same maximum in G_{U_c} with the single terminal c. Then κ_t = κopt^c on U_c for every state
  t > g_{|U_c|−1} of the phase.
Proof. P-FREEZE's proof, word for word with κ for M.
- (UB): the honest play of z up to its first terminal is a simple path of G_{U_c} ((Aκ), (SP)). (Aκ) along it gives κ_t(z) =
  Σ(wt, s) + κ_t(end) ≤ κopt.
  - In (i), κ_t(o) = κ(θ_t) = κ_Θ(o) on Θ.
  - In (ii), o ∉ U_c. The play never visits o, and every Odd vertex on it is forced.
- (LB) by induction on j: for t > f_j (resp. g_j) and a simple path p with ≤ j edges, κ_t(z) ≥ the path's value.
  - The Even step is κ-ROUND at f_j (resp. g_j) followed by (M2κ).
  - The Odd step uses the forced edge.
- Simple paths of G_{U_c} have ≤ |U_c| − 1 edges. □

## 3. Lemma θ-SET (PROVED, L-SI 9; κ form of HAT-FREEZE (c) as in N5-FBCAP-route §1)
Statement. Assume c_θ ≠ o. For every state t > g_{|U|−2} of the phase, θ_t lies in
  Vθ := {o ⊕ ξ(x) : x ∈ succ(o) ∩ Û} ∪ {(c_θ, ∅, ℓ) : 1 ≤ ℓ ≤ n − 1},
where ξ(x) is the valuation with cycle node c_θ and key κoptÛ(x), the optimum over simple paths of G_Û from x to c_θ. So |Vθ| ≤ d_o + n − 1.
θ never decreases (R15 (a)), so θ changes at most d_o + n − 2 times among the states t > g_{|U|−2}. If c_θ = o, θ = (o, ∅, 0) on the
whole phase.
Proof.
- κ-HAT-FREEZE: HAT-FREEZE (RHO §2) with κ for M, by κ-ROUND for U. For t > g_{|U|−2} and y ∈ F_t ∩ U, κ_t(y) = κoptÛ(y).
- H1 at t. Let x0 := σ̄_t(o).
  - λ(o) = c_θ ≠ o, so (V1) gives θ_t = o ⊕ Ξ_t(x0), and λ(x0) = c_θ, so x0 ∈ Û.
  - H1 means o's honest play never returns to o. So x0's honest play avoids o, and on 𝒞^1O it equals x0's (σ_t, τ)-play ((HP)). Hence
    x0 ∈ F_t.
  - By κ-HAT-FREEZE, Ξ_t(x0) = ξ(x0); κ determines P by (INJ), and ℓ.
- ¬H1 at t. o lies on its honest cycle, whose top is c_θ. Every vertex of o's play before c_θ lies on that cycle and has rank < rank(c_θ).
  So P(θ_t) = ∅ and θ_t = (c_θ, ∅, ℓ) with 1 ≤ ℓ ≤ n − 1.
- If c_θ = o, θ is o's own cycle-node value (o, ∅, 0). □

## 4. Theorem FB-PHASE (PROVED, L-SI 9)
Statement. Let a phase have f in-phase Even S4c fallbacks, and put N0 := max(0, |U| − 2, max_{c ≠ c_θ}(|U_c| − 1)). Then
  f ≤ N0 + (d_o + n − 2) + (d_o + n − 1)(|U| − 1) + 1 ≤ 2n² + n.
Proof.
- Key step (no switch after a freeze). Let k → k+1 be an in-phase fallback and v ∈ U_c ∖ {c} an Even vertex that switches.
  - By (SG), Ξ_{k+1}(v) ▷ Ξ_k(v), so κ_{k+1}(v) > κ_k(v) by (M1κ). So κ is NOT constant on U_c across k → k+1.
  - Hence, by κ-FREEZE:
    - (a) if c ≠ c_θ, then k ≤ g_{|U_c|−1}, i.e. the fallback is among the first |U_c| − 1 fallbacks of the phase;
    - (b) if c = c_θ and θ_{k+1} = θ_k, the fallback is among the first |U| − 1 fallbacks of its θ-run.
  - (SG) is checked directly from the facts: (Aκ) at k+1 and at k, the gate κ_k(x*) > κ_k(σ_k v), and (M2κ) at x*.
- Count the fallbacks g_j.
  - (0) j ≤ N0: at most N0 of them.
  - For j > N0, both k = g_j and k + 1 are states > g_{|U|−2}, and by (a) no vertex of U_c ∖ {c}, c ≠ c_θ, switches at g_j.
  - (1) θ_{k+1} ≠ θ_k: by θ-SET at most d_o + n − 2 of them.
  - (2) θ_{k+1} = θ_k: g_j lies in a θ-run Θ that contains a state > g_{|U|−2}. By θ-SET there are at most d_o + n − 1 such θ-runs.
    - (2a) g_j is among the first |U| − 1 fallbacks of Θ: at most (d_o + n − 1)(|U| − 1) of them.
    - (2b) Otherwise, by (b) no vertex of U ∖ {c_θ} switches either. So every switched vertex y is an own cycle node, λ_k(y) = y.
      - S4c switches every Even vertex that has a gate. So every gate (y, z) ∈ Iσ_k has λ_k(y) = y.
      - CN gives level −1 for y's taken gate (y, z*). For any other gate (y, z), Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ Ξ_k(z*), so (C5) gives
        lev ≤ −1. Distinct values with one cycle node have lev ≥ −1, so lev = −1.
      - CN-LAST: k + 1 is the last state of the phase. At most 1 such fallback.
- Sum. With |U|, d_o ≤ n and N0 ≤ n − 1: f ≤ (n − 1) + (2n − 2) + (2n − 1)(n − 1) + 1 = 2n² − 1 ≤ 2n² + n. □
- Remarks.
  - FB-PHASE needs no hypothesis on H1, H2, H3, τ(o), c_w, X, θ_ph or K.
  - N5-FBCAP-route §2 cases (i)-(v) are all covered by the key step. (iv), route changes inside R̄, is handled by the θ-run freeze (i),
    whose terminal o carries κ(θ). (v), outside U, is handled by the class freeze (ii).
  - N5-FBCAP-route §2's "cycle case" does not arise. The key step compares v's value with itself, not along a concatenated path.
  - L-RED's CONJECTURE FB-CAP (≤ max(1, |U| − 2)) is much sharper. FB-PHASE is the polynomial version.

## 5. Corollary FX: crossings per phase (PROVED, L-SI 9, from FB-PHASE and landed results)
Statement. X ≤ n(f + X_SN) + n − 1, with X_SN ≤ 13(d_o + 1)n³(f + 1 + T) + T (R34 (f)) and T ≤ n² + 2n − 1. With FB-PHASE,
X = O(d_o·n⁶) = O(n⁷).
Proof.
- A crossing is a fallback (≤ f), an S4a step from a state with c_w = c_θ (≤ X_SN), or an S4a step from a state with c_w ≠ c_θ.
- The last kind has R_k ⊊ R_{k+1} (R-STICK).
- Between two consecutive crossings of the first two kinds, R ⊆ V ∖ {o} only grows, so at most n − 1 crossings of the third kind
  occur there. □

## 6. Corollary T-K (READING built on FB-PHASE, FX and LANDED R28 OX (v))
- T_P ≤ (m − n + 1)((n + 1)(2f + 2X + K + 1)n(n − 1) + X + 1) = O(m·n³·(d_o n⁶ + K)).
- So **a phase is polynomial iff its wakes K are**. With L1-L3 of the ledger (#phases ≤ n(n − 1) + d, Lemma Φ unrefereed):
  N5 on 𝒞^1O is polynomial ⇐ (K-poly) ∧ Lemma Φ.
- K (R27 (e) definition): relevant Even switches of level above the previous used level, between consecutive relevant transitions,
  with no fallback and R constant. In U1 pieces they are bounded given f (R24 (d)), so now polynomially. In U2 / U3 / U23 stretches
  (¬H1 or HN states) they need (E), (K_W) (R26): OPEN.
- Not claimed: any bound on K, any iteration bound.

## 7. DATA (experiments/si/fb14/fbphase.py; logs in experiments/si/fb14/logs/)
- Corpus: REFEREE-2's library list (docs/referee-2/R2-N5-OUT/files.lst) with the S3 start + 3 random starts. Also 532 extra instance
  files (referee climbs, red/si/new instances; 𝒞^1O only, 342 kept) with the S3 start + 1 random start. SPEC mode, REFEREE-2's tracer.
- Checked:
  - (SG) at every fallback switch;
  - κ-FREEZE (i) states and "no U switch after the θ-run freeze";
  - κ-FREEZE (ii) per class;
  - θ-SET's count;
  - FB-PHASE's bound.
- Extra corpus: 0 failures. 2,427 SG checks. Max 37 fallbacks in a phase, at most 0.04 of the bound.
  - THIN: the post-freeze hypotheses occur rarely: θ-run freeze 2 times (2 state checks), class freeze 11 classes (89 state checks).
  - Max distinct θ values after g_{|U|−2}: 0.077·(d_o + n).
- Library corpus (295 files, 1,180 traces, 308 phases with a fallback): 0 failures; 3,002 SG checks; class freeze 14 classes (84 state
  checks); θ-run freeze 0 times (vacuous); max 37 fallbacks in a phase (0.062 of the bound); max distinct θ after g_{|U|−2}: 0.2·(d_o + n).
- Companion counts (experiments/si/fb14/hfb.py, logs/lib_r3.txt, extra_*.txt). Switch classes at in-phase fallbacks by state type:
  - after g_{|U|−2} only "outside U, cycle" switches were seen (4);
  - no eviction after g_{|U|−2} in any data, matching N5-FBCAP-route (iii);
  - no FB-CAP violation (fbcap check, library, 4 starts per file).
- The DATA is vacuous for most of the theorem's post-freeze content. FB-PHASE rests on its proof.

## 8. Corrections to the ledger (docs/si/N5-LEDGER-box14.md is frozen; corrections go here)
- Ledger §4 1 (b) said that at (h) states F → R̄ gates are impossible, at THR "with FBL-N (ii)" and at EQ "no gate from F at all".
  - This holds only for gates of level ≥ 0 at THR states with r ≥ 0.
  - Level −1 gates from own cycle nodes exist: b4_n5_other_0.pg, S3 start, fallback 1 → 2 at an EQ (h) state, v = 4 = c_θ, 4 → o,
    lengths 3 → 2. These are FBW (ii)'s exception (R31 (b)).
  - FB-PHASE does not use the claim.
- Ledger X7 and the TYPE Q / TYPE N READING remain valid, but they are now superseded for the count: Corollary FX bounds X in every
  phase type without FBCAP (iii), Q-SPLIT or NHN.
