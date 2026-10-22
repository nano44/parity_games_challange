# Draft RESULTS R9 (Lead, 2026-10-17 13:27Z by date -u) — LANDED as RESULTS R9 (CHECKER C9 PASS a9258e6; N-1..N-5 and fall3 wording applied)

### R9 [refereed-only] Packet 6 on A_DTL: per-context budgets reduce GAP-A to (CTX⁺) and (FALL) (2026-10-17) — partial step-4 reduction (not M3, not a step-4 pass)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Packet pinned at
  trunk 8ff4085, docs/alg/GAP-A-M.md §22f (line 2049) and §22j (line 2213), building on RESULTS R5 (h) (FDL), R7 (PREFIX-MONO,
  ROOT-BOUND, reduction), R8 (STR-DET). A phase fixes G' and p; S is its number of searches; e* is the first difference of
  consecutive searches on the reduced log.
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) For every best_vertices context R, the potential Π_R is a function of (R, p, T) (no X or W read; str read only at 73, deciding a str write only); T grows along a
      phase; clean later visits never lower Π_R. Hence the e*-at-R transitions number at most (F_R + 1)(H + 1), where F_R counts
      EVERY transition at R where Π_R does not rise (descents, incomparable steps, and Π-blind e* transitions).
  (b) For a fixed tattr input I of a −1 attractor or a Dom step, the output is a triggered closure monotone in T (DTL-proof 1.2b;
      for Dom, the closure triggered by the new part, with only the top pushed), so the transitions whose e* has input I form a
      strictly increasing chain: at most n per input. A −1 attractor's input is a function of (R, X) alone (dtl.cpp 898-912). A
      Dom step's input is (X ∪ Dom_{<j}, R \ Dom_{<j}, τ_j, pr τ_j), which depends on T and is NOT fixed by (R, X).
  (c) Hence S − 1 ≤ Σ_{R ∈ C_bv} (F_R + 1)(H + 1) + n·(|C_T| + |C_Dom|) + 1, where C_bv are the distinct first-difference
      best_vertices contexts, C_T the distinct −1 attractor contexts (R, X) and C_Dom the distinct Dom INPUTS at first
      differences; and GAP-A ⇐ (CTX⁺) ∧ (FALL), with
      (CTX⁺): |C_bv| + |C_T| + |C_Dom| is polynomial per phase;
      (FALL): Σ_R F_R (F_R as in (a)) is polynomial per phase.
      The (DOM-e*) hypothesis of RESULTS R7 (e) is no longer needed (absorbed into |C_Dom|).
  (d) The remark that the raw per-input bound S − 1 ≤ n·|I_fd| + 1 is vacuous on data (|I_fd| ≈ S − 1) is DATA, used only as
      motivation.
- Signatures: REFEREE docs/referee/R-P6.md (referee 9f77ff9 + 0c0e3ce): (a) SIGN WITH GAPS (G6-a1, G6-a2, closed); (b) SIGN WITH
  GAPS (G6-b1 closed; G6-b2: Dom input not fixed by (R, X), so |C_Dom| counts inputs, OPEN inside (CTX⁺)), revised in the
  comparison §C (ad4be01) to SIGN once (CTX⁺) says "inputs" for Dom, as (c) here does; (c) SIGN.
  REFEREE-2 docs/referee-2/R2-P6.md (referee-2 5ef09aa; comparison §5 c7634a7): (a) SIGN WITH GAPS (G-F1 = G6-a1); (b) SIGN with
  reading R-I (the Dom input includes the whole current X; "fixed" means equal in s and s+1 at a first difference, not
  determined by (R, X)); (c) SIGN. Independent (each read the other's P6 report only after pushing its own). No REJECT. Item letters: R9 (b)+(c) = reports' (b); R9 (d) = reports' (c).
- Gaps (union). G-R9-1..3 closed in the reports, to be imported into §22f/§22j; G-R9-4..5 OPEN (they are the hypotheses);
  G-R9-6 dependencies:
  G-R9-1 F_R must count every non-rise of Π_R at R, not only descents (REFEREE G6-a1 = REFEREE-2 G-F1); data: 0 such non-
         descent non-rises after L-ALG's G-Ψ tool fix (one apparent case on cross union 411 was a tool artifact; full re-run
         of corpus, mixed and cross unions in both orders: 0, GAP-A-M §22n, l-alg e4e52ac).
  G-R9-2 §22f's display alone omits the Dom term and the +1 of R7 G-R7-3 (REFEREE G6-a2; agreed REFEREE-2 §5).
  G-R9-3 Dom pushes only its top (Q = {top}, Z = X), so DTL-proof Lemma 1.2 applies as "the closure triggered by the new part",
         same proof (REFEREE G6-b1; REFEREE-2 R-I). §22j's (CTX⁺) wording "contexts" of Dom steps reads "inputs" (REFEREE
         G6-b2, a wording item closed in the reports).
  G-R9-4 OPEN (CTX⁺), including Dom INPUTS: DATA only (first-difference contexts ≤ 10 per phase on the SPP families; Dom e* 0 on
         all data; REFEREE probe: Dom input varies at fixed (R, X, top) in 105/2,110 (stable) and 111/2,166 (Oink)
         phase-contexts, up to 4 inputs). (CHAIN) is FALSE (DE16).
  G-R9-5 OPEN (FALL): DATA only. "Descends only where RV falls" (73/72) is data; the "≤ 2 per context" maximum is BROKEN on data
         by L-RED fall3_n76 (experiments/red/carry/instances/fall3_n76.pg, sha1 a85133ec, docs/red/R31-fall3.md: 3 descents at one
         context, both orders; Lead re-ran pinned Oink (10 iterations, verified) and dtl_rootmono.py (max 3 per context, both
         orders; also re-run by CHECKER C9, a9258e6)), DATA unrefereed, which does not refute (FALL); "≤ 2" was never signed.
  G-R9-6 Dependencies: R5 (h), R7 (a)-(d), R8; DTL-proof 1.2b; phases ≤ D + 2 (R5 (g)); bit cost via DTL-proof §3(e) (R5 (k)).
         H's (d + 2) factor counts distinct threshold levels while the code loops t = 0..max_prio (dtl.cpp 721-722); still
         polynomial (REFEREE nit).
         Nothing Lean-checked.
- Scope: a reduction, not a bound. GAP-A stays OPEN on (CTX⁺) and (FALL), which have different causes (GAP-A-M §22g), so this
  is not the L32 single-statement criterion. GAP-C (completeness) is separate and open (DE13, DE15). Gauntlet step 4 stays open.
