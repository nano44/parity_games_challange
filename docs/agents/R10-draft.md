# Draft RESULTS R10 (Lead, 2026-10-17 15:40Z by date -u) — NOT LANDED; awaiting CHECKER gate

### R10 [refereed-only] Packet 7 on A_DTL: Lemma EXACT, PREFIX-MONO-X, and (FALL) ⇐ (NSTEAL) (2026-10-17) — partial step-4 lemmas (not M3, not a step-4 pass)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Packet pinned at
  trunk d461a76 (REFEREE) and 357224b (REFEREE-2), docs/alg/GAP-A-M.md §22r (L-ALG). For a top τ of a round, P(τ⁺) is the
  union of the regions of processed tops of higher index; E_τ is the set of stored tangles that meet P(τ⁺) but are not inside
  it. A NEW STEAL at a consecutive visit pair of context R is a tangle t of the earlier visit's T with t ∈ E′_τ \ E_τ for some
  top τ processed in the earlier round.
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) Lemma EXACT: every region step of the code is exactly the triggered closure Cl_{pr τ}(P(τ⁺) ∪ {τ}; T \ E_τ) (Cl as in
      dtl_ideal lfp_ref: new vertices of priority ≤ pr τ, a tangle needing an escape in the set).
  (b) Lemma PREFIX-MONO-X: if V ⊆ V′, T ⊆ T′ and there is no new steal (E′_τ ∩ T ⊆ E_τ for every τ processed in the earlier
      run), then P(τ) ⊆ P′(τ) for every τ.
  (c) Corollary: Π_R fails to rise between visits only at a new steal (including Π-blind e* steps), and
      F_R ≤ N_R^desc + N_R^e* ≤ 3·N_R, where N_R is the number of consecutive visit pairs of R in the phase that contain a new
      steal. Hence (FALL) ⇐ (NSTEAL): N_R is polynomial per phase for every first-difference context R; and
      GAP-A ⇐ (CTX⁺) ∧ (NSTEAL), given STR-DET (RESULTS R8, R9). (NSTEAL) implies (FALL), not the converse.
  (d) Data check on fallv_viol_n28 (RESULTS DE18): each fall is at a new steal; both falls of vertex 14 at the root are new steals
      of the SAME old tangle at different rounds, so "each tangle is newly stolen at most once per context" is FALSE.
- Signatures: REFEREE docs/referee/R-P7.md (referee 299bc58; comparison §C 1abe1d7): (a) SIGN WITH GAPS, closed (G7-a1, G7-a2);
  (b) SIGN; (c) SIGN WITH GAPS, closed (G7-c1, G7-c2), and in §C accepts REFEREE-2's G-P7-c2 (F_R ≤ 3·N_R; its earlier "F_R ≤
  #new-steal visit pairs holds as stated" withdrawn); (d) agrees. REFEREE-2 docs/referee-2/R2-P7.md (referee-2 a66ff93;
  comparison §6 19e63f7): (a) SIGN; (b) SIGN; (c) SIGN WITH GAPS, closed (G-P7-c1, G-P7-c2); (d) confirmed. REFEREE-2 §6:
  REFEREE's (NS-COUNT) and REFEREE-2's (NSTEAL) are the same statement. Independent (each read the other's P7 report only
  after pushing its own). No REJECT.
- Gaps (union). G-R10-1..4 closed in the reports, to be imported into §22r (L-ALG §22t imports REFEREE's); G-R10-5 OPEN;
  G-R10-6 dependencies:
  G-R10-1 The rejection of a tangle with a consumed vertex is at dtl.cpp 138-139, not 137 (REFEREE G7-a1 = REFEREE-2 N-a1).
  G-R10-2 ⊇ of EXACT: mixed-premise rule instances are tried at a pop in Z_τ; vertices of P(τ⁺) are never escapes since
          Gx = CurR (80, 156) (REFEREE G7-a2; REFEREE-2's single last-pop argument).
  G-R10-3 Strict rise at e* comes from POS-FALL together with PREFIX-MONO-X's C4; Π-blind e* steps also need a new steal
          (REFEREE G7-c1 = REFEREE-2 G-P7-c1).
  G-R10-4 e*-pairs need not be consecutive visits of R, so F_R ≤ 3·N_R over consecutive pairs (REFEREE-2 G-P7-c2, accepted by
          REFEREE §C). "PREFIX-MONO is the special case" is the same proof pattern, not a special case (REFEREE note = N-b1).
  G-R10-5 OPEN (NSTEAL): DATA only and lossy (new steals : non-rises ≈ 9.5:1 REFEREE-2, ≈ 13:1 REFEREE).
  G-R10-6 Dependencies: (S0) and PREFIX-MONO pattern (RESULTS R7), STR-DET (R8), the R9 reduction; O1 (oink.cpp 35,
          game.cpp 478-495). Nothing Lean-checked.
- Data (evidence only): EXACT held at every region step in both referees' independent probes: REFEREE 477k steps (Python
  reference, own closure), REFEREE-2 463,742 steps (instrumented pinned C++, own closure; plus 420 random games); E_τ nonempty
  at 196,340 steps and the closure without exclusion differs from the code at 24,259, so the exclusion is used; 0 non-rises
  without a new steal in either probe.
- Scope: a sharper reduction, not a bound. GAP-A stays OPEN on (CTX⁺) and (NSTEAL). L-ALG's later unrefereed refinement
  (GAP-A-M §22s-§22u: PREFIX-MONO-X* on fired tangles; (STEAL-ONCE), (FIRED-R), DATA) is not part of R10. Gauntlet step 4
  stays open.
