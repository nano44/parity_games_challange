# Draft RESULTS R24 (Lead, 2026-10-24 22:1xZ by date -u) (rev. 22:19Z: C33 E-1, N-1) — awaits CHECKER C33 Addendum 1; lands in "## Results" after R23, before "## Dead ends"

### R24 [refereed-only] N5 on one-Odd-choice games: S4a keeps every fully optimal edge (R), its tie-break is a monotone potential (TB), W-flat runs are short (CASC), U1 pieces have polynomially many R-changing transitions given their fallbacks (Theorem U1), and w-changes under ¬H2 (WC) (2026-10-24) — partial step-4 lemmas for N5 on a subclass (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C33.md, checker PENDING)
- Object (packet P-N5-U1, pinned trunk eee0d8a, unchanged during review): docs/new/P-N5-U1-box31.md, sha1
  eb90788d2949050f316ed983fa56c34d7a1dd9c7 (L-NEW successor 11, Opus 5.5). The referees' repairs are collected by the lane in
  docs/new/P-N5-U1-fixes-box31.md (l-new 61a36b9, on trunk; sha1 88675ab782df24a63426756674579e7336c1508c; a record, not itself
  refereed text).
  Setting as in R22 (𝒞^1O; a PHASE is a joint λ-phase with τ constant; R ∋ o, F := V \ R; crossing-free interval; route form; U1 = both
  frames in route form with c_w strictly more relevant than c_θ; a PIECE J is a maximal run with both frames in route form and θ, w
  constant). Level ℓ(v) := |π_v|.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma R: in N5's S1 restriction step, every FULLY optimal successor of x (equal in cycle node, path set and length) survives, so
      the length step chooses among exactly the fully optimal edges (FIX 4 order). The packet's wording "optimal in the cycle-node and
      path-set components" is FALSE at x = u (R-1 = G-R-2; REFEREE's 3-vertex instance; 4,074 / 8,464 such deleted edges, all with
      u = x); the step-1 invariant holds for processed u ≠ x (G-R-1). VJ00 (BRICS RS-00-48) §6 Prop. 6.1 gives only existence of one
      surviving path; Lemma R is the packet's own strengthening (R-2).
  (b) Lemma TB: at an S4a transition without fallback, if an Even v switches with W'(v) = W_k(v) and is not its own cycle node c, then
      (TB-odd) c odd ⇒ σ_{k+1}(v) < σ_k(v) as indices; (TB-even) c even and W' = W_k on v's σ_k-play from v to (before) c ⇒ the
      root-first index key pk(v) strictly decreases lexicographically. Tie-breaks equal SPEC S1 (iv) / FIX 4 exactly (TB-1 = G-TB-1:
      the sandwich case where the optimal play passes x, closed by an (F1)-only case proof; TB-2 wording).
  (c) Lemma CASC: in a W-flat run (consecutive non-fallback transitions of a piece with W unchanged on R), an R-vertex of level ℓ
      switches only at run steps ≤ ℓ − 2; so no R-vertex switches at a run step ≥ |R| − 2. Step 1 uses only TB's choice rule (C-1,
      wording after §C; C-2, C-3 wording).
  (d) Theorem U1: a U1 piece with f fallback transitions has at most |R| + f + K + (K + f + 1)(|R| − 2) transitions that change Ξ, W
      or σ on R, with K ≤ (f + 1)(|R| − 1)(|R| − 2) counting non-fallback transitions (N-U1-1); O((f + 1)|R|³), and ≤ |R|³ for f = 0.
      Includes the κ_w-freeze, with R22 (c)'s P3-1 repair transferred.
  (e) Lemma WC: on a crossing-free interval with ¬H2, the w-changing transitions number WC(I) ≤ (f_I + 1)(|R|² − 1) + f_I, with f_I
      the fallback transitions of I. Sharpened in both §C (N-U1-3): at an EQ state Ξ = W, so an Even fallback switches improving
      edges of G_τ and W does not decrease (R15 (a) / VJ00 Lemma 5.7 in G_τ); hence only fallbacks at OTHER states count in f_I.
- Reduction (READING, checked by both referees, not signed): with RESULTS R22's reduction (itself a READING), (NH') reduces to (X),
  NFB-O (fallbacks at OTHER states) and the U2/U3 re-routings. Unsigned inputs named by REFEREE: the P-N5-NH §4 assembly and its fixes
  §4 one-liner (checked true by TC (iv)).
- Honest limits: (i) SUBCLASS 𝒞^1O; a bound on N5 itself. (ii) U1 is bounded GIVEN f; fallbacks at OTHER states (NFB-O) are open (0
  seen), as are the U2/U3 re-routings and (X). (iii) DATA is thin: K = 0 everywhere, no U1 piece with a fallback was found, and CASC
  climbs never came within 2 steps of the bound. (iv) (U1-T) is FALSE as stated, per vertex (L-RED u1t_cex_n32 sha1 63dfd785; L-NEW
  u1t_cex2_n32 6162a26f; own-switch version L-RED u1t_own6_n32 f6368500, 6 own switches at one W-length in a 6-transition piece);
  Theorem U1 counts transitions per piece. (v) |R| convention: lane scripts printed |R \ {o}|; with R ∋ o the three cex instances have
  |R| = 29 / 29 / 25 (D-1 = N-U1-5); every checked bound grows with |R|, so the lane's checks were stricter.
- Data (DATA, not proof): REFEREE: 3 pinned instances re-run; 78 named 𝒞^1O instances (92 U1 pieces, longest 12); 5,500 random runs
  (U1 pieces single-state, vacuous); 23,000 random arenas (TB-odd 113, TB-even 535); 381,241 choice-rule checks; 3 CASC climbs (7,599
  candidates, best margin −2); 322 EQ-state fallbacks, W non-decreasing; 0 failures. REFEREE-2 (own code): 11,910 runs + 20,000 arenas
  + 13 climbs (70,400 runs), 0 violations; 426,737 key-min checks against SPEC, 0 mismatches.
- Signatures: REFEREE docs/referee/R-N5-U1.md (referee 257fa4c; §C 4de5c2e, stamp fix 5054e81): Theorem U1 SIGNED; CASC SIGNED (C-1
  downgraded to wording in §C); TB SIGNED WITH GAPS (TB-1, TB-2, closed); Lemma R SIGNED WITH GAPS (R-1, R-2, G-R-1, closed by
  restating); WC SIGNED, sharpened (N-U1-3, proved in §C.3); §6 READING correct. REFEREE-2 docs/referee-2/R2-N5-U1.md (referee-2
  28ddf6f; §C 3d68a03, stamp fix cab4e7d): U1 SIGN; CASC SIGN WITH GAPS (C-1 accepted as a citation gap, closed; C-2, C-3 wording); TB SIGN WITH GAPS
  (G-TB-1, closed); R SIGN WITH GAPS (G-R-1, G-R-2, closed); WC SIGN, N-U1-3 closure proved in §C.4; §6 READING correct. Joint gap
  map: TB-1 = G-TB-1; R-1 = G-R-2; R-2 (VJ00 existence only); G-R-1, C-1..C-3, TB-2 wording; N-U1-1 (K counts non-fallback
  transitions); N-U1-3 closed by both; D-1 = N-U1-5, D-2 = N-U1-4 (data notes).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
