# Draft RESULTS R8 (Lead, 2026-10-17 12:44Z by date -u) — NOT LANDED; awaiting CHECKER gate

### R8 [refereed-only] Lemma STR-DET on A_DTL: equal set-level logs force equal extraction (2026-10-17) — partial step-4 lemma (not M3, not a step-4 pass)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Packet pinned at
  trunk f920dc2, docs/alg/GAP-A-M.md §22i (L-ALG). s -> s+1 are consecutive searches of one phase; their reduced logs (repeated
  sptl passes deleted, RESULTS R5 (h)) are aligned up to a point π with equal inputs and equal set outputs before π.
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) No tangle that s lacked when it computed a given sptl region before π (i.e. in T_{s+1} \ T_s^ρ for the region at point
      ρ < π) fires in that region in s+1.
  (b) Hence every sptl region computation before π is step-identical in s and s+1, str included.
  (c) Hence the extracted SCCs, the W bits and the `more` flag agree before π; s+1 creates no tangle before π.
  (d) A transition with no differing tattr ends in a barren s+1 (search returns false, dtl.cpp 1068; run() breaks, 1113/1120),
      so it is the last search of the phase (at most one per phase).
  Consequences signed by both: gap G-STR is CLOSED for every first-difference location (best_vertices, −1 attractor, sptl,
  Dom); the str part of G-h1 is closed; RESULTS R5 (h) (First-Difference Lemma) holds without the (STR-DET) condition; the
  (STR-DET-w) hypothesis of RESULTS R7 (e) is discharged.
- Signatures: REFEREE docs/referee/R-P5.md (referee ca03021): (a) SIGN WITH GAPS, closed (W-a1, G-a2); (b), (c), (d) SIGN.
  REFEREE-2 docs/referee-2/R2-P5.md (referee-2 6d508da): (a), (b), (c), (d) SIGN. Independent (neither read the other's P5
  report before pushing its own). No REJECT.
- Gaps (union; all closed in the reports, to be imported into §22i):
  G-R8-1 Wording W-a1: state (a) for T_{s+1} \ T_s^ρ (the tangle set s held at the region's point ρ), not T_s^π (REFEREE).
  G-R8-2 Case A's step Z_τ ⊆ Dom_P(s): the cited PREFIX-MONO absorbed case needs a step-ideal later run, which Dom is not
         known to be; correct argument: Dom attracts into X (136), the union of Dom's parts for tops ≥ τ is closed under the
         threshold-pr(τ) triggered rules (74-90; tangle rule at the last escape pop), so it contains Cl(P(τ⁺)∪{τ}) ⊇ Z_τ by
         (S0) (REFEREE G-a2; REFEREE-2 gives the same D_{≥σ} argument in its own (a)).
  G-R8-3 Dependencies: context chain R-PROVED2 §C5 (RESULTS R5 (b)), SCC1 (R5 (a)), (S0) (R7 (a)), O1, DTL-proof 1.2b. Nothing
         Lean-checked.
- Data (evidence only): weak STR-DET 1,065/1,065 (Oink) and 1,035/1,035 (stable) on the corpus plus 4 instances, 3,377/3,377 on
  600 cross unions (stable) (L-ALG); 0 of 4,290 same-phase pairs (REFEREE-2 R2-P4 probe).
- Scope: STR-DET removes one hypothesis from the GAP-A reduction; GAP-A still needs (CTX) and (DIRTY)/(FALL) and the Dom term
  (RESULTS R7 (e); GAPS G-DOM). Gauntlet step 4 stays open.
