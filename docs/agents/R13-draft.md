# Draft RESULTS R13 (Lead, 2026-10-18 00:45Z by date -u) (rev. 00:48Z: REFEREE final aabcefd) — NOT LANDED; awaiting REFEREE §C, L-ALG imports, CHECKER gate

### R13 [refereed-only] Packet 10 on A_DTL: Lemma ENTRY-CHARGE, and GAP-A ⇐ (CTX⁺) ∧ (EXIT_c) (2026-10-18) — partial step-4 reformulation (not M3, not a step-4 pass)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Packet pinned at
  trunk 1100f3a, docs/alg/GAP-A-M.md §23q (line 3244) (L-ALG succ. 7), building on RESULTS R11 (c) and R12 (a)-(b). One
  context R and one phase; steps σ = (r, τ) over a FIXED set (every round r ≤ |R| + 1 with the round convention of G-R13-1,
  every p-vertex τ of R); P_i(σ⁺) is the prefix before τ in round r at visit i. An EVENT is (i, q) with q = (σ, t), t ∈ F_σ(i)
  and t a relevant steal at the pair (i, i+1). An ENTRY of w at σ is a visit pair (i, i+1) with w ∉ P_i(σ⁺), w ∈ P_{i+1}(σ⁺);
  an EXIT is the reverse. N_ent and X_R are the numbers of entries and exits over all (σ, w).
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) Lemma ENTRY-CHARGE: Σ_q k_q ≤ |R|·N_ent ≤ |R|·(X_R + (|R|+1)|R|²). Step 1: each event (i, q) gives an entry (σ, w, i)
      with w ∈ t (t fired at σ in visit i, so t ∩ P_i(σ⁺) = ∅ by dtl.cpp 136-139, 690, 699; the steal makes t meet
      P_{i+1}(σ⁺)). Step 2: at most |F_σ(i)| < |R| events share one entry, because every firing adds a new vertex
      (can_attract_new, dtl.cpp 142-146, 153-157, 169-172; the top is in CurZ from 693; a tangle fires at most once per step).
      Step 3: per (σ, w), entries ≤ exits + 1.
  (b) Corollary C1: GAP-A ⇐ (CTX⁺) ∧ (EXITS-POLY), given STR-DET, where (EXITS-POLY): X_R is polynomial per phase for every
      first-difference context R; no (FIRED-R) and no (STEAL-DEPTH) are needed.
  (c) Corollary C2: (EXIT_c) "each (step, vertex) exits at most c times per phase" gives Σ_q k_q ≤ (c+1)(|R|+1)|R|³; hence
      GAP-A ⇐ (CTX⁺) ∧ (EXIT_c) for any constant c, given STR-DET.
  (d) Corollary C3 (honesty): X_R ≤ N*_R·|R|·#steps, so (EXITS-POLY) ⇔ (STEAL-POLY_sum) ⇔ (RELSTEAL) up to polynomial
      factors: a REFORMULATION of a premise already in R10/R11/R12, not a reduction. What is new is the LOCAL sufficient form
      (EXIT_c).
  (e) Data: at most 2 exits per (step, vertex) on all data, both orders; 2 only on stealonce_viol_n76, stealonce_both_n45 and
      resteal34_union_n90.
- Signatures: REFEREE docs/referee/R-P10.md (referee aabcefd; draft 8f2db93, report a09a89d; comparison §C PENDING): (a) SIGN WITH GAPS,
  closed (G10-a1); (b) SIGN (N10-b1); (c) SIGN (constants: X_R ≤ c(|R|+1)|R|², F_R ≤ 3(c+1)(|R|+1)|R|³); (d) SIGN; (e) CONFIRMED
  (dtl_prefexits unmodified + own probe p10entry.py, 140 files, both orders, 0 failures). REFEREE-2 docs/referee-2/R2-P10.md (referee-2 0cbe61e; comparison §6
  57468a8): (a) SIGN WITH GAPS, closed (G10-a1); (b) SIGN (N10-b1); (c) SIGN; (d) CONFIRMED; (e) own probe an10.py, 268 files,
  both orders, 0 failures. Independent (each read the other's P10 report only after pushing its own). No REJECT.
- Gaps (union). G-R13-1..3 closed in the reports, to be imported by L-ALG; G-R13-4..5 OPEN; G-R13-6 dependencies:
  G-R13-1 Counting convention (both G10-a1, complementary halves): entries, exits and events are counted on ONE membership
          sequence per (σ, w): a FIXED σ set (every p-vertex τ of R, not "τ ∈ V_r" read per visit; REFEREE-2) and one round
          convention (repeat the last round after a "no candidates" stop, empty after V = ∅; REFEREE).
  G-R13-2 FIRED-freeness is not new: R12 (a)'s sum form and R11 (c) ((RELSTEAL) via F_R ≤ 3·N*_R) are already free of
          (FIRED-R) (REFEREE N10-b1, REFEREE-2 N10-b1). What ENTRY-CHARGE removes is the #fired factor between exits and
          Σ_q k_q (compare EXIT-CHARGE, §23p, unrefereed).
  G-R13-3 Shorter route (REFEREE-2 N10-b1, one signature): step 1 alone gives N*_R ≤ N_ent, so F_R ≤ 3(X_R + (|R|+1)|R|²)
          without step 2 or R12 (a); with (EXIT_c), F_R ≤ 3(c+1)(|R|+1)|R|².
  G-R13-4 OPEN (EXIT_c): DATA only; c = 2 on all data (both referees' probes and L-ALG dtl_prefexits.py); L-RED's exit climb
          stayed at 2 (R37 addendum, l-red 59b3522).
  G-R13-5 OPEN (CTX⁺): DATA only (max 13); no route (CTX-ROOT DE17, CTX-LAMINAR, PIECES-LAMINAR dead).
  G-R13-6 Dependencies: R12 (a)-(b) (G9-b1 prefix convention), R11 (c), R10, R8 (STR-DET), R9; also open, inherited: (ACYC)
          (G-S5-6, a GAP-C item). Nothing Lean-checked.
- Scope: a reformulation, not a bound. GAP-A stays OPEN on (CTX⁺) and (EXIT_c) (or the equivalent (EXITS-POLY) / (RELSTEAL)),
  both DATA only; (EXIT_c) is a single local statement but has no proof yet, and (CTX⁺) has no route. Not the L32
  single-statement criterion. GAP-C is separate. Gauntlet step 4 stays open.
