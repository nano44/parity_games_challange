# Draft RESULTS R26 (Lead, 2026-10-25 00:1xZ by date -u) (rev. 00:34Z: fixes file cited) — LANDED in RESULTS Results 00:48Z (CHECKER C35 3653d4a PASS), after R25

### R26 [refereed-only] N5 on one-Odd-choice games: W-flat runs outside route form are short (CASC-U2 for U2 stretches; CASC-U3 for U3 and U23 stretches, between events), with counting corollaries given fallbacks, W-changes and events (2026-10-25) — partial step-4 lemmas for N5 on a subclass (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C35.md, checker PENDING)
- Object (packet P-N5-U23, pinned trunk 7666336, unchanged during review): docs/new/P-N5-U23-box31.md, sha1
  ee3e5d1ef95623d3f5e08a34af416fa6b2d09186 (L-NEW successor 11, Opus 5.5). The referees' repairs are collected by the lane in
  docs/new/P-N5-U23-fixes-box31.md (l-new 0274bd5, on trunk; sha1 870c63a35ceafbd6d8cf94ea9b43923002c68ca6, L-NEW successor 12; a
  record, not itself refereed text).
  Setting as in R22 and R24 (𝒞^1O; a PHASE is a joint λ-phase with τ constant; R ∋ o, F := V \ R; route form). A STRETCH is a
  maximal run of states of a phase with R, θ, w constant; a W-FLAT RUN is a maximal run of consecutive non-fallback transitions of a
  stretch with W unchanged at every vertex of R. U2: ¬H1 and c_θ := λ_Ξ(o) ≠ o, with the W frame in route form; U3: ¬H2 and
  c_w := λ_W(o) ≠ o, with the honest frame in route form; U23: ¬H1, ¬H2, c_θ ≠ o, c_w ≠ o. π_v is v's σ-route (its (σ, τ)-path before
  its first visit of o); level ℓ(v) := |π_v|.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma CASC-U2: in a W-flat run of a U2 stretch, an R-vertex v switches only at run steps 0, …, ℓ(v) − 2. Proof: R24 CASC step 3
      with three new steps (levels constant via P-N5-NH (R1), W half; honest values on R are route functions with constant terminals
      θ and Ξ(c_θ); R24 TB's choice rule with keys depending only on σ along π_z).
  (b) Corollary: a U2 stretch with f fallback transitions and K_W non-fallback transitions with a W-change on R has at most
      f + K_W + (K_W + f + 1)(|R| − 2) transitions that change Ξ, W or σ on R.
  (c) Lemma CASC-U3 (U3 and U23 stretches; under ¬H2, o lies on its W-cycle o → A1 → c_w → A2 → o; v ∈ R \ {o} is of KIND A if
      c_w ∈ π_v, else KIND B; an EVENT is a switch of an Even R-vertex that changes its kind, or a switch of c_w, whose choice is SPEC
      S1 (v) / FIX 2): in an event-free sub-run, kinds are constant, and (i) a kind-B vertex v switches only at sub-run steps
      ≤ |π_v| − 2; (ii) a kind-A vertex v whose σ-path reaches c_w after λ(v) steps switches only at sub-run steps
      ≤ max(L_B − 1, 0) + λ(v) − 2, with L_B the largest |π| over kind B (0 if kind B is empty); (iii) no R-vertex switches at a sub-run
      step ≥ 2|R| − 4. The packet's (ii) "≤ L_B + λ(v) − 3" is unproved when kind B is empty (L_B = 0: the proof gives ≤ λ − 2);
      repaired as above (U3-1 = G-U23-1; REFEREE's form max(L_B, 1) + λ − 3 is the same bound); no counterexample. "Kinds constant"
      is proved by induction along the new routes when several vertices switch at once (U3-2); the case c_θ = c_w under U23 is
      covered (Ξ(c_w) = (c_w, ∅, 0); U3-3).
  (d) Corollary: a U3 or U23 stretch with f fallbacks, K_W non-fallback W-changes on R and E transitions containing an event has at
      most f + K_W + E + (K_W + f + E + 1)(2|R| − 4) R-changing transitions. (Sharper per-sub-run factor available: L_B + λ ≤ |R| − 2,
      REFEREE §2.4, accepted by REFEREE-2.)
- Reading (checked by both referees, not signed): with R24 §6, (NH') reduces to (X), NFB-O, (E) and (K_W). Stretch counts under ¬H1
  need the θ-changes, which TF (it needs H1) does not cover: under ¬H1, θ = (c_θ, ∅, d) with d monotone (R15 (a)), so θ changes at
  most |R| − 1 times per phase (REFEREE R-1 = REFEREE-2 N-U23-2; closed by R-1's argument, re-checked by REFEREE-2).
- Honest limits: (i) SUBCLASS 𝒞^1O; a bound on N5 itself. (ii) Both bounds are GIVEN f, K_W and E. (E) (events per W-flat run:
  kind crossings and c_w's switches) and (K_W) (non-fallback W-changes on R outside route form; R24's κ_w-freeze does not transfer)
  are OPEN, as are (X) and NFB-O; G-N5-TIME stays open. (iii) DATA is thin: CASC-U2 is exercised only by L-RED's u2flat_n32
  (experiments/red/xing/instances/u2flat_n32.pg, l-red bee6487, sha1 1a016c446d8c48b0e856d88b4527f61dfb1983e0; Lead re-run n5 13/3,
  Oink zlk OK strategies verified, one Odd choice vertex): 2 U2 W-flat switches at run step 0 (REFEREE), 7 over 20 starts with the
  bound attained (REFEREE-2); the kind-B half of CASC-U3 is vacuous in all data; the literal (ii) never failed, but its L_B = 0 corner
  had no switch in any sub-run. (iv) Lane DATA (not re-checked by the referees): every (E) and (K_W) transition seen is tame in
  RESULTS R25's sense (78 of 78), so neither is charged to J. (v) The lane's checker u23check.py tests less than the packet (U23
  stretches unchecked, (iii) at 2|R|, (ii) and corollaries untested; L-RED box 35); L-RED's u23x.py checks the packet as stated: 0
  violations on ~90 pinned 𝒞^1O instances.
- Data (DATA, not proof; every probe asserts one Odd choice vertex): REFEREE u23_probe.py (own code): 120 named 𝒞^1O instances
  (U2 / U3 / U23 stretches 39 / 54 / 90), 5,500 random runs (all W-flat runs switch-free, vacuous), 3 climbs (7,845 candidates);
  nr_u23_n32 32 kind-A switches within (ii); u3ev_n16 8 W-flat switches, all events (n5 6/0, Oink OK); 0 failures. REFEREE-2
  u23_check.py (own code): 6,650 batch runs + 28,800 climb runs, 34,230 kind-A switches within the repaired bound (closest bound − 1),
  1,364 ¬H1 states with θ of the form (c_θ, ∅, d), 0 violations.
- Signatures: REFEREE docs/referee/R-N5-U23.md (referee 7ffbd9f; Appendix A 2bdb045; §C cde420b): CASC-U2 and Corollary SIGNED;
  CASC-U3 (i), (iii) SIGNED WITH GAPS (U3-2 closed, downgraded to wording in §C; U3-3 wording); (ii) SIGNED WITH GAP U3-1 (closed by
  the repair); Corollary SIGNED; §3 READING correct with R-1. REFEREE-2 docs/referee-2/R2-N5-U23.md (referee-2 07b22b0; §C 5e24010):
  CASC-U2 and Corollary SIGN; kinds/events, (i), (iii) SIGN, after §C SIGN WITH GAPS (U3-2, U3-3 accepted as precisions; closed);
  (ii) SIGN WITH GAPS (G-U23-1, closed); Corollary SIGN; §3 READING correct with N-U23-2. §C: no disagreement. Joint gap map
  (REFEREE §C.3, REFEREE-2 §C.6): U3-1 = G-U23-1 (closed); U3-2 (closed); U3-3 (wording); §2.4 sharpening (accepted); R-1 =
  N-U23-2 (closed); N-U23-1 (CASC-U2 vacuous) superseded by u2flat_n32.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
