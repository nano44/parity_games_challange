# Draft RESULTS R30 (Lead, 2026-10-25 04:33Z by date -u) (rev. 04:38Z: fixes file cited; rev. 04:53Z: C39 E-1, N-1, N-2) — LANDED in RESULTS Results 05:04Z (CHECKER C39 09c8dc7 + Addendum 262104b PASS), after R29

### R30 [refereed-only] N5 on one-Odd-choice games: anatomy of an ε-transition (OR, TC-SPLIT), R never shrinks at S4a steps outside the c_w = c_θ regime (R-STICK, SN-PREFIX, H3H2), who can leave R (LEAVE), counting absorptions (ABS-COUNT′, with H1-DROP and H1-KEEP), wakes in the odd mode (WK), and absorptions above a fallback level (ABS-L) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C39.md, checker PENDING)
- Object (packet P-N5-SN, pinned trunk 2c70ef6, unchanged during review): docs/new/P-N5-SN-box33.md, sha1
  340d4f298d8ee137b53ff76d7dd81de49f8fa542 (L-NEW successor 13, Opus 5.5). The referees' repairs and the lane's repair of SN-1 are in
  docs/new/P-N5-SN-fixes-box33.md (l-new 9de7820, on trunk; sha1 f242b0118a30cf3362cda59e48787cc0bd1768b2, L-NEW successor 13); its §2b (H1-DROP, H1-KEEP, ABS-COUNT′) is new
  proof text, signed by both referees in addenda (REFEREE-2 R2-N5-SN §B, REFEREE R-N5-SN Addendum 2); the rest of the file is a record.
  Setting as in RESULTS R27-R29 (𝒞^1O; phase with λ_Ξ and τ constant; R, F, H1-H3, (h), c_θ := λ(o), c_w := the W-cycle node of o,
  crossings; relevant changes, E_k, O_k, L_k; ε-transition: O_k > E_k; x0 := σ̄_k(o); scope runs and r := lev(θ, w) as in R29). An
  ABSORPTION is an ε-transition with x0 ∈ F_k ∩ R_{k+1}; REL_run := the number of exits of o leaving R at transitions of a run; d_o :=
  |succ(o)|; f := fallback transitions of the phase.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma OR: at an ε-transition, (a) x0's H_{k+1}-path to c visits o, so x0 ∈ R_{k+1}; (b) under H1 at k, x0 ∈ F_k (an absorption);
      (c) lev(θ_k, θ_{k+1}) = O_k and θ_{k+1} ▷ θ_k.
  (b) Lemma TC-SPLIT: at every phase transition with θ_{k+1} ≠ θ_k, lev(θ_k, θ_{k+1}) ≤ E_k, or k is an ε-transition and
      lev(θ_k, θ_{k+1}) = O_k.
  (c) Lemma R-STICK: at an S4a transition of a phase, every v ∈ R_s whose W-cycle node differs from λ(v) stays in R_{s+1}; so if
      c_w(s) ≠ c_θ, R_s ⊆ R_{s+1}. Corollary SN-PREFIX: in a run of consecutive non-fallback transitions of a phase, the states with
      c_w = c_θ form a prefix; after it R never loses a vertex, so at most n − 1 crossings follow; per phase, crossings ≤
      (f + 1)(n − 1) + f + X_SN, X_SN := S4a crossings at states with c_w = c_θ. (WM, R23 (g), applies on this phase: its proof uses only
      τ_{k+1} = τ_k at a non-fallback step and the S4a optimum; both referees.)
  (d) Lemma H3H2: H1 ∧ H3 ⇒ H2; so under H1 the regime c_w = c_θ is exactly (h).
  (e) Lemma LEAVE: at an S4a transition with H1, a vertex q ∈ R_s \ {o} leaving R has (h) at s, and q's H_{s+1}-path before its cycle node
      carries a relevant change of level ≥ r_s (L_s ≥ r_s); for r_s = ⊥ such a relevant change still exists (SN-3, wording).
  (f) Lemma H1-DROP (fixes §2b): inside a phase, H1 at k and ¬H1 at k+1 force P(θ_k) = ∅. Corollary H1-KEEP: at an ε-transition with H1
      at k and O_k ≥ 0, H1 holds at k+1. Corollary ABS-COUNT′: in a fallback-free run of a phase, the H1 ε-transitions number at most
      (d_o − 1) + REL_run if the run's last H1 ε-transition has O ≥ 0, and at most d_o + REL_run otherwise; per phase, ε_{H1} ≤
      (d_o − 1)(f + 1) + REL + f + ε⁽⁻¹⁾, with ε⁽⁻¹⁾ := runs whose last H1 ε-transition has O = −1 and + f for ε-transitions at fallbacks.
      The packet's ABS-COUNT ("(d_o − 1) + REL_run" for every run; per phase (d_o − 1)(f + 1) + REL) was unproved as written: "ends
      ≤ d_o − 1" needs H1 at the run's last state, and ε-transitions at fallbacks belong to no run (SN-1 = G-SN-1 (a), SN-2 = G-SN-1 (b));
      §2b closes SN-1 except ε⁽⁻¹⁾.
  (g) Lemma WK: a wake y: a → z (R27 (e)) with y not its own W-cycle node and W unchanged at a and z has an even W-cycle node at y (BFS
      mode); so in the odd mode every wake transition changes W on R. (y ⊕ is strictly monotone between W(z) and W(a) since y lies on
      neither W-path: N-SN-1, wording; REFEREE's Bellman route via R24 G-TB-1 also closes it.)
  (h) Lemma ABS-L (premises R29 (e) NL and (f) CLS1's proof): in a scope run, between consecutive fallbacks k0 < k with L := M_{k0} and
      r_j > L on [k0+1, k], every transition with lev(θ_j, θ_{j+1}) > L is an absorption whose exit stays in R up to k; so at most d_o − 1
      θ-changes above L in (k0, k).
- Refuted (not signed; L-RED, own checkers; Lead re-runs: n5 + Oink zlk + check_sol2, one Odd choice vertex, and L-NEW's orx.py EPS=1 /
  oddlev.py): CONJECTURE EXIT-R (an absorbed exit stays in R until the next fallback) is FALSE: experiments/red/so/instances/
  exitr_cex_n48.pg (sha1 7a663df2…, transition 4 absorbs exit 13, which leaves R at the S4a step 5→6, f = 0 in the phase), and
  exitr_cex_n16.pg (6971211e…). Its consequence "ε_{H1} ≤ (d_o − 1)(f + 1) per phase" is FALSE: epsseg_cex_n48.pg (b4c7dcb0…, phase f = 0,
  17 H1 ε-transitions against 16; exit 33 released at 8→9 and re-absorbed at 14) and epsseg_cex_n16.pg (8d83f7c2…, 6 against 5);
  ABS-COUNT′ holds on all of them (REL ≥ 1, tight on epsseg_cex_n48). Also lane forms (not signed): H-RE FALSE (b6_xl_n48); (KW-M) and
  NO-WAKE FALSE (R27).
- Honest limits: (i) SUBCLASS 𝒞^1O; inside a phase. (ii) REL (exit releases in the c_w = c_θ prefix), X_SN and K per phase are OPEN;
  ε⁽⁻¹⁾ and ε at fallbacks are OPEN but never observed; G-N5-TIME stays open. (iii) DATA is thin for WK (its hypothesis held at none of
  the observed wakes) and ABS-L (no θ-change above L in any window); no ¬H1 ε-transition was observed anywhere. (iv) K per phase can
  be Θ(n) (L-NEW K-chain family, DATA: kchain4/10/32 with 3/9/31 wakes; Lead re-ran kchain4; REFEREE reproduced 3/9/31 wakes, Oink OK).
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE sn_probe.py + absc_climb.py (own code): 243 library files,
  the K-chain instances, 11,000 random games, 5 + 4 climbs, 0 failures (17 in-phase H1 → ¬H1 transitions, all with P(θ_k) = ∅; 349
  H1 ε-transitions on its 245-file Addendum-2 library, all O ≥ 0). REFEREE-2 (own code): library × 3 starts + 5,500 random, climbs 47,200 + 42,000 runs, 0 failures
  (R-STICK 867,072 checks; 39,461 crossings after a c_w = c_θ prefix; 23,798 H1 leaves, 14,438 tight; 15,716 in-phase H1 → ¬H1
  transitions, all P(θ_k) = ∅; 18,669 H1 ε-transitions, none with O = −1; 728 H1 ε-transitions on library × 3 + 5,500 random, all O ≥ 0). L-RED box 37 (Lead
  relay; own checker, library 241 files): 0 failures of OR, TC-SPLIT, R-STICK, SN-PREFIX, ABS-L; X_SN = X = 29 at n 32 (xsn29_n32); 31
  crossings after the prefix at n 48 (post31_n48; ≤ 47); CHECKER C39 re-ran both.
- Signatures: REFEREE docs/referee/R-N5-SN.md (referee 59a886d; addendum 58dd6e8; §C 3d49e0a; Addendum 2 on §2b 2f465ff): OR, TC-SPLIT,
  R-STICK, SN-PREFIX, H3H2, WK, ABS-L SIGNED; LEAVE SIGNED WITH GAP SN-3 (wording); ABS-COUNT SIGNED WITH GAPS SN-1, SN-2; H1-DROP,
  H1-KEEP, ABS-COUNT′ SIGNED. REFEREE-2 docs/referee-2/R2-N5-SN.md (referee-2 ddbecaf; §A 91d95e8; §C 80d2e45; §B on §2b 4c8dcfd): OR,
  TC-SPLIT, R-STICK, SN-PREFIX, H3H2, LEAVE SIGN; WK SIGN (N-SN-1); ABS-COUNT SIGN WITH GAPS G-SN-1; ABS-L SIGN (premises signed);
  H1-DROP, H1-KEEP, ABS-COUNT′ SIGN. WM transfer VALID in both. §C: no verdict differs. Joint gap map (REFEREE §C, REFEREE-2 §C): SN-1 =
  G-SN-1 (a) (closed by §2b except ε⁽⁻¹⁾); SN-2 = G-SN-1 (b) (+ f); SN-3, N-SN-1 (wording); ABS-L unconditional (R29).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
