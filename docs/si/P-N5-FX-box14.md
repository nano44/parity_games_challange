# Referee packet P-N5-FX: with polynomially many fallbacks per phase, crossings per phase are polynomial in every phase type (Corollary FX) (box 14)
L-SI successor 9 (Opus 5.5; D18, L40), session_018jN1MJkw56F58G3qcfcuZA. Written 2026-10-25 19:09Z (date -u), at the Lead's request of
18:57Z (Lead's stamp): "P-N5-FX (docs/si/P-N5-FX-box14.md): Corollary FX". Frozen at this commit: corrections go in a fixes file,
never here.

## 0. Scope, labels, dependencies
- SUBCLASS 𝒞^1O: exactly one Odd vertex o has out-degree d_o > 1.
  - TARGET.md asks about general parity games. Nothing here is a claim about them, a running-time bound for N5, a TARGET.md claim, or a
    gauntlet step-4 pass.
  - G-N5-TIME stays OPEN.
  - Every statement is about the candidate N5 (SPEC S1-S5, docs/new/N5-ssi-global.md) inside one phase.
- Labels: PROVED (L-SI 9, unrefereed); READING (not to sign).
- Source: docs/si/N5-FBPHASE-box14.md §5 (sha1 f7aaa624). This packet re-states it and governs where they differ.
- Notation as in RESULTS R30 / R34 (setting of R28-R34).
  - Phase: λ_Ξ and τ constant. R: the vertices ≠ o whose (σ, τ)-play reaches o.
  - c_θ := λ_Ξ(o); c_w := the cycle node of W(o).
  - A CROSSING is an in-phase transition with R_{k+1} ≠ R_k.
  - f: the in-phase Even S4c fallback transitions of the phase.
  - X_SN: the S4a crossings of the phase at states with c_w = c_θ (R30 (c)).
  - T := n² + 2n − 1 (R34 (e)).
  - In a phase every transition is an S4a step or an Even S4c fallback (τ is constant; SPEC S4c FIX 3).

| tag | statement used | where | status |
| --- | --- | --- | --- |
| R-STICK | at an S4a transition s → s+1 of a phase with c_w(s) ≠ c_θ: R_s ⊆ R_{s+1} | RESULTS R30 (c) | LANDED |
| X-SN-PHASE | X_SN ≤ 13(d_o + 1)n³(f + 1 + T) + T, no hypothesis on H1 | RESULTS R34 (f) | LANDED |
| FB-POLY | f ≤ 1 + (\|U\| − 2)(deg_U(o) + \|U\|) ≤ 1 + (n − 2)(2n − 1) | P-N5-FBPOLY (docs/new/P-N5-FBPOLY-box41.md, sha1 de244dcd, pinned trunk 42d8c3a9) | IN REVIEW |
| FB-PHASE | f ≤ 2n² (independent second proof) | docs/si/N5-FBPHASE-box14.md §4 | LANE-PROVED (cross-check only, not to sign) |

## 1. Corollary FX (PROVED, L-SI 9)
Statement.
- (a) (No hypothesis on f.) In every phase, X ≤ n·(f + X_SN) + n − 1.
- (b) (CONDITIONAL on FB-POLY.) Hence X ≤ n·(F* + 13(d_o + 1)n³(F* + 1 + T) + T) + n − 1 = O(d_o·n⁶), with F* := 1 + (n − 2)(2n − 1).
  Since d_o ≤ n, X = O(n⁷). FB-PHASE's f ≤ 2n² gives the same order.
Proof of (a).
- Every crossing k → k+1 is of exactly one kind:
  - (i) an S4c fallback: at most f;
  - (ii) an S4a step with c_w(k) = c_θ: at most X_SN, by definition;
  - (iii) an S4a step with c_w(k) ≠ c_θ: by R-STICK, R_k ⊆ R_{k+1}, so R_k ⊊ R_{k+1} (it is a crossing).
- Cut the phase at the transitions of kinds (i) and (ii). There are at most f + X_SN cuts, so at most f + X_SN + 1 segments.
  - Inside a segment every crossing is of kind (iii) and strictly enlarges R ⊆ V ∖ {o}. So a segment has at most n − 1 of them.
- X ≤ f + X_SN + (n − 1)(f + X_SN + 1) = n(f + X_SN) + n − 1. □
Proof of (b). Substitute FB-POLY's bound for f in (a) and in X-SN-PHASE. □
- Remarks.
  - (a) uses no phase-type hypothesis: H1, H2, H3, τ(o) and case A/B are not used. So it covers TYPE H, TYPE Q and TYPE N phases
    alike, in the terms of docs/si/N5-LEDGER-box14.md §3.
  - The sharper per-type counts of the ledger (SPLIT, Q-SPLIT, no eviction after g_{|U|−2}) are not needed.

## 2. Not to sign (READING)
- T-K. With RESULTS R28 (c) (iii)-(v) (LANDED: ε ≤ X, J ≤ X, ρ ≤ 2f + 2X + K, T_P ≤ (m − n + 1)((n + 1)(2f + 2X + K + 1)n(n − 1) + X + 1)):
  T_P = O(m·n³·(d_o n⁶ + K)).
  - With P-N5-PHI (#phases ≤ n(n − 1) + d): N5 on 𝒞^1O is polynomial ⇐ (K polynomial per phase) ∧ P-N5-PHI ∧ P-N5-FBPOLY ∧ this
    packet ∧ their inputs (P-N5-PFZ, P-N5-RHO).
  - K is OPEN: wakes at ¬H1 / HN states; RESULTS R26's (E) and (K_W). See docs/si/N5-LEDGER-v2-box14.md §3.
- With X bounded, the R38 (c) SCOPE-COUNT, R39 / R42 HN counts and R27 (g) TH (θ-changes) become polynomial per phase. This is a READING;
  each is LANDED given X and f.

## 3. Data (DATA; not to sign)
FB-PHASE's DATA (experiments/si/fb14/, logs/fbphase_*.txt) checks f. For (a) itself:
- R-STICK and X-SN-PHASE are LANDED with their own data.
- The decomposition (i)-(iii) is exact by definition.
- No separate run was made for this packet.
