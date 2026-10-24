# Draft RESULTS R23 (Lead, 2026-10-24 21:1xZ by date -u) — awaits CHECKER C32; lands in "## Results" after R22, before "## Dead ends"

### R23 [refereed-only] N5 on one-Odd-choice games: crossings have active crossers (ACT, LOOP), what fallbacks can switch (NOFE, NOFL-E, GAP), W never drops at arena steps (WM), and crossings are bounded by reversals of R (LV′, Corollary Z) (2026-10-24) — partial step-4 lemmas for N5 on a subclass (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C32.md, checker PENDING)
- Object (packet P-N5-Z, pinned trunk fba7177, unchanged during review; a post-pin edit on the lane branch was reverted to the pinned
  bytes before merge): docs/si/P-N5-Z-box5.md, sha1 a027638f06d18143ed0779290b24f8e5decb8249 (L-SI successor 2, Opus 5.5). The lane's
  data corrections and the referees' repairs are in docs/si/P-N5-Z-fixes-box5.md (l-si c3c62ef, on trunk; sha1
  c6d9c13f6b06c0df3b6ca1b9ada04e0c716112ee; a record, not itself refereed text).
  Setting as in R21 (𝒞^1O; a PHASE is a joint λ-phase with τ constant). Convention of this packet: R excludes o and R̄ := R ∪ {o};
  F := V \ R̄, and the crossing transitions (R changes) are the same as in R19-R22.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Step (K): at an S4c fallback inside a phase, no arena edge (y, z) raises W at y (from R21 (c) FBL-N (i)).
  (b) Lemma ACT: at a transition with τ unchanged, (i) if R̄ gains a vertex, some switched Even s ∈ F_k with σ_{k+1}(s) ∈ R̄_k enters;
      (ii) if R̄ loses a vertex, some switched s ∈ R_k with σ_{k+1}(s) ∈ F_k leaves, or a new cycle avoiding o lies inside R_k and
      contains a switched vertex.
  (c) Lemma LOOP and Corollary: inside a phase with H1 at k, ACT (ii)'s cycle alternative does not occur, so every leave has an active
      leaver. (H1 is needed: REFEREE's probe saw the cycle alternative 88 times, all without H1.)
  (d) Lemma NOFE, strong form: at an S4c fallback inside a phase, every switched edge y → z with y ∈ F_k and z ∈ R̄_k has y on o's
      W-play at k. (Also a one-line corollary of R21 (c) FBL-N (ii): y is a W-cycle node on o's W-play; Z-2.)
  (e) Lemma NOFL-E and Corollary: at a fallback from a state with Ξ = W and H2, no switched edge goes R → F; with H1 ∧ H2 such a
      fallback has no leave.
  (f) Lemma GAP: at a fallback with (h) at k, every switched edge y → z with y ∈ R_k, z ∈ F_k satisfies
      Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ W_k(σ_k y) (the evicted target lies in the trust gap).
  (g) Lemma WM and Corollary: inside a phase, W_{k+1} ⊵ W_k pointwise at every transition that is not an S4c fallback; so every
      W-decrease is at a fallback.
  (h) Lemma LV′: sign each crossing '+' (R̄ grows), '−' (R̄ shrinks) or '±'; with Z := #'±' + #(sign changes between consecutive pure
      signs), X ≤ (n − 1)(Z + 1) + Z and Z ≤ X. "Runs" of equal pure signs are runs adjacent among crossing transitions, so a '±'
      breaks a run (Z-1 = N-Z-1; read "ignoring ±", the monotonicity step fails).
  (i) Corollary Z: inside one phase, #transitions ≤ (3n²(1 + X + O) + X + O + 1)(4n(n − 1) + 1) with X ≤ (n − 1)(Z + 1) + Z, so
      O(n⁵(1 + Z + O)) (from R21 (g) within its signed hypotheses, and LV′).
- Honest limits: (i) SUBCLASS 𝒞^1O; a bound on N5 itself. (ii) LV′ moves (X) to (Z) up to a factor n; Z is OPEN. The lane locates its
  hard part in carries (C), i.e. '+−' reversals at evicting fallbacks (fixes file: a drain counts once); OPEN, CONJECTURE (CL) only.
  (iii) The phase count (Lemma Φ) is unrefereed, so a running-time bound is still a READING. (iv) DATA on Z: lane climbs Z 11 / 18 /
  22 at n 24 / 32 / 48 (zcl_fb2_n32: 13 carries in one phase); L-RED box 32: X ≈ 0.86n from random seeds, X 65 at n 32 from wave
  seeds; L-COMP b6_xw_n32: X 67 at n 32 (Lead re-runs). (v) Refuted lane forms (packet §10): NOFE's first form (nofe_cyc_n8),
  (U*-DROP), (W-LAY). s_rt32_final (si/orlens) is NOT in 𝒞^1O (two Odd choice vertices); it is excluded from all counts.
- Data (DATA, not proof; out-of-class files excluded): REFEREE z_probe.py (appendix 555cbeb): ACT (i) 1,126 / (ii) 855, NOFE 17, GAP
  511, WM 3,957, LV′ 595 phases (max X 78, max Z 22), 0 failures. REFEREE-2 z_check.py (own code): 13,756 runs, 38,186 transitions,
  35,072 phases, 0 violations (ACT 9,174 / 7,951, LOOP 2,689, GAP 1,950 edges, WM 15,717; 963 of 1,153 fallbacks lower W, no
  non-fallback does; 21 F→R̄ fallback edges, all tails W-cycle nodes on o's W-play).
- Signatures: REFEREE docs/referee/R-N5-Z.md (referee c818ef2; data appendix 555cbeb; §C dcee223): LV′ SIGNED WITH GAP Z-1 (wording);
  Corollary Z SIGNED; NOFE SIGNED (Z-2 remark, Z-3 wording); Step (K), ACT, LOOP, NOFL-E, GAP, WM SIGNED; §C: no disagreement.
  REFEREE-2 docs/referee-2/R2-N5-Z.md (referee-2 1a5854b; §C fde0448): every statement SIGN (N-Z-1 wording, N-Z-2 data); §C: no
  disagreement, Z-2 and Z-3 accepted. Joint gap map: Z-1 = N-Z-1 (CLOSED); N-Z-2 = appendix 555cbeb (data); Z-2 (remark); Z-3 (wording).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
