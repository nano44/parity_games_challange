# N5 on 𝒞^1O: the G-N5-TIME ledger, v2 (box 14)
L-SI successor 9 (Opus 5.5; D18, L40), session_018jN1MJkw56F58G3qcfcuZA. Written 2026-10-25 19:01Z (date -u), at the Lead's request of 18:41Z
(Lead's stamp): items (a) and (b).
- What this is: READING. It is a NEW file; v1 (docs/si/N5-LEDGER-box14.md, sha1 c54e8560) is frozen.
- Labels: as in v1 (LANDED Rnn / SIGNED-IN-LANDING / IN REVIEW / LANE-PROVED / CONJECTURE / OPEN / DATA / READING).
- NO polynomial bound for N5 is proved. G-N5-TIME stays OPEN.

## 0. What changed since v1
- f per phase now has two independent lane proofs, both LANE-PROVED and unrefereed, both with no X term:
  - FB-POLY (L-NEW 20, docs/new/N5-FBPOLY-box41.md, sha1 7a7087f7, packet P-N5-FBPOLY being frozen):
    f ≤ 1 + (|U| − 2)(deg_U(o) + |U|) ≤ 1 + (n − 2)(2n − 1). It was first, at 18:37Z (Lead's stamp).
  - FB-PHASE (L-SI 9, docs/si/N5-FBPHASE-box14.md, sha1 f7aaa624, 18:48Z by date -u, written without knowledge of FB-POLY):
    f ≤ N0 + (d_o + n − 2) + (d_o + n − 1)(|U| − 1) + 1 ≤ 2n².
    - It is a second route. Its key step is (SG) strictness against a θ-run / λ-class κ-freeze, followed by CN-LAST.
    - It is weaker in the constant than FB-POLY. A referee may use it as a cross-check.
  - Below, f ≤ F* := 1 + (n − 2)(2n − 1) (FB-POLY); either proof serves.
- Lemma Φ: now packet P-N5-PHI (docs/si/P-N5-PHI-box14.md, sha1 35e79ec1, l-si af3a3b5a). It is PROVED from LANDED results only and
  gives #phases ≤ n(n − 1) + d on 𝒞^1O.

## 1. (a) With f bounded per phase, does X close? YES (READING; every input LANDED except f)
- What t_Q is. In R33 (g) X-RUN′, t_Q is the number of H1-toggles with both ends in the SN prefix P of the fallback-free run Q.
  - The fallback-free runs of a phase are disjoint. So Σ_Q t_Q ≤ the H1-toggles of the phase ≤ T := n² + 2n − 1 (R34 (e) TOGGLE-COUNT,
    LANDED).
  - So t_Q needs no X. R34 (f) X-SN-PHASE already sums it: X_SN ≤ 13(d_o + 1)n³(f + 1 + T) + T, with no X term (LANDED).
- Crossings X. FBPHASE §5 Corollary FX, using only R30 (c) R-STICK (LANDED) besides f and X_SN:
  - X ≤ n(f + X_SN) + n − 1.
  - With f ≤ F*: X_SN = O(d_o·n³·n²) = O(n⁶) and X = O(n⁷).
  - Proof idea: a crossing is a fallback, an S4a step at c_w = c_θ (counted by X_SN), or an S4a step at c_w ≠ c_θ, which only grows R by
    R-STICK, at most n − 1 times between two shrink events.
- WCH / SCOPE-COUNT (R38 (b), (c), LANDED): scope runs ≤ (1 + T + f) + (n − 2)(X + 1) + X = O(n⁸). Polynomial. They are no longer needed
  for f.
- θ-changes per phase:
  - R27 (g) Lemma TH (LANDED): Θ ≤ (n − 1) + n(X + 1) + X = O(n⁸), for phases with λ(o) ≠ o.
  - If λ(o) = o, θ = (o, ∅, 0) is constant.
  - After the freeze, θ-SET (FBPHASE §3) gives ≤ d_o + n − 2.
  - So "θ-changes before the freeze" (Lead's 18:37Z guess) is closed by TH once X is.
- The R28 (c) quantities (LANDED, given X): ε ≤ X, J ≤ X, ρ ≤ 2f + 2X + K. Only ρ still carries a free term, K.
- Per phase, now: T_P ≤ (m − n + 1)·((n + 1)(2f + 2X + K + 1)·n(n − 1) + X + 1) = O(m·n³·(n⁷ + K)) (R28 (c) (v), LANDED).
- "S4a steps" (Lead's guess) are NOT a separate link. Theorem LP (R27 (d), LANDED) bounds all transitions of a phase by the relevant
  ones, and the relevant ones by ρ and ε. The only open term in ρ is K.

## 2. Status of every link (𝒞^1O)
| link | bound | status |
| --- | --- | --- |
| #phases | ≤ n(n − 1) + d | P-N5-PHI (PROVED from LANDED; to referee) |
| f per phase | ≤ 1 + (n − 2)(2n − 1) | FB-POLY (LANE-PROVED, packet pending); FB-PHASE second proof (LANE-PROVED). Inputs: P-N5-PFZ §1-§2 and P-N5-RHO §2 (SIGNED-IN-LANDING) |
| X_SN per phase | 13(d_o + 1)n³(f + 1 + T) + T | LANDED R34 (f) |
| X per phase | ≤ n(f + X_SN) + n − 1 | READING / FBPHASE §5 (from LANDED R30 (c)) |
| ε, J | ≤ X | LANDED R28 (c) |
| ρ | ≤ 2f + 2X + K | LANDED R28 (c) |
| **K (wakes) per phase** | none | **OPEN: the single open count** |
| T_P | O(m n³ (n⁷ + K)) | LANDED R28 (c) (v) given the above |
| total | ≤ (n(n − 1) + d)·max_P (T_P + 1) | READING |
- So: N5 on 𝒞^1O is polynomial ⇐ [K polynomial per phase] ∧ [P-N5-PHI, FB-POLY (or FB-PHASE), PFZ, RHO signed and landed]
  (READING).
- The general (multi-Odd-choice) case is untouched. Every link above uses 𝒞^1O. R15 / R18 / R38 KEY are general, and Lemma Φ (a)-(c) is
  general.

## 3. (b) K: what it is, and what R26's (E) and (K_W) need
- Definition (R27 (e), P-N5-LP §3). Let k < k′ be consecutive relevant transitions of a phase with only NU transitions between them, no
  fallback in [k, k′], and R constant on [k, k′ + 1].
  - A WAKE at k′ is a relevant Even switch y: a → z at k′ of level > L_k. K counts transitions with a wake.
  - A wake has a, z ∈ R (Lemma WAKE). It is a σ-change inside R̄ while R is constant: a dormant gate that S4a did not take before is
    taken.
- Where wakes live (Lemma WAKE + R24 / R26):
  - (i) In route form ((h), i.e. H1 ∧ H2 with c_w = c_θ, or λ(o) = o), wakes lie in U1 pieces.
    - R24 (d) Theorem U1 bounds the R-changing transitions of a U1 piece by O((f + 1)|R|³).
    - The number of pieces is polynomial given X, w-changes and f (R19 (f), R22). So **K in route form is now polynomial** (READING).
  - (ii) U2 (¬H1: the honest frame is not in route form) and U3 / U23 (¬H2: the W frame is not in route form, i.e. HN states, and ¬H1
    ∧ ¬H2). R26 (b), (d) bound the R-changing transitions of such a stretch by
    f + K_W + E + (K_W + f + E + 1)(2|R| − 4). Two quantities are open:
    - (K_W): non-fallback transitions with a W-change on R, in U2 / U3 / U23 stretches.
      - R24's κ_w-freeze does not transfer (R26 limit (ii)), and (KW-M) is FALSE (kwm_cex_n24).
      - At S4a steps W never drops (R23 (g) WM), so W on R is monotone between fallbacks. But it is a monotone chain of valuations with
        cycle node c_w, which can a priori be exponentially long.
      - Needed: a Bellman-Ford-type freeze for W on R̄ at S4a steps, analogous to FB-ROUND / BF-F (RHO §4) for Ξ on F.
      - Candidate (CONJECTURE, unchecked): at an S4a step between two states with ¬H2 and R constant, for every Even v ∈ R and successor
        x ∈ R̄ with (v, x) in the arena, W_{k+1}(v) ⊵ v ⊕ W_k(x). This is (F1) in the arena, as in BF-F's last case.
        - The obstruction: dormant edges, which are W-improving but not Ξ-gates, are not in the arena. So the round is partial, and a
          wake is exactly an edge entering the arena.
        - So K_W and K need a count of arena entries. An edge (v, x) with v ∈ R enters the arena when Ξ(x) overtakes Ξ(σ v).
        - Under ¬H2, Ξ on R is π ⊕ θ and W is π ⊕ w with different cycle nodes, so the order of route prefixes can differ between Ξ and
          W only through the top vertices between rank c_θ and rank c_w (BAND, R27 (e)).
        - A route entering the arena changes Ξ's order only when θ changes or a route changes. θ-changes are now polynomial. Route
          changes are the transitions being counted, which suggests an amortised argument: each wake is charged to a θ-change or an
          earlier route change of bounded depth. OPEN.
    - (E): events in a W-flat run of a U3 / U23 stretch. An event is a switch of an Even R-vertex that changes its KIND (c_w ∈ π_v or
      not), or a switch of c_w itself (SPEC S1 (v) / FIX 2).
      - Switches of c_w: c_w = λ_W(o). Under ¬H2 it is the top of o's W-cycle, so a c_w switch changes o's W-cycle length. R34 (b)
        L-MONO is the analogue for c = λ_Ξ(o); for c_w it is NOT proved. CONJECTURE (unchecked): c_w's W-cycle length is monotone in a
        phase, which gives ≤ n − 1 c_w switches.
      - Kind changes: a vertex's kind changes only when its route changes to pass, or to stop passing, c_w. Those are R-changing
        transitions, the quantity being bounded, so this is circular unless kinds are monotone. OPEN.
- Data on K: K ≤ 2 per run in L-NEW's climbs; K = Θ(n) on the kchain family (R30 limit (iv)); the wake term is barely exercised in
  either referee's data (R28 limit (iii)).
- Proposed next attack: K_W via a W-round lemma with arena-entry charging, at HN states first (U3). There BF-F already gives the F-side
  rounds, and SPLIT (R39 (a)) makes R monotone between evictions.
