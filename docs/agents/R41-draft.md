# Draft RESULTS R41 (Lead, 2026-10-25 16:56Z by date -u) — to CHECKER C50

### R41 [refereed-only] N5 on one-Odd-choice games: in-scope THR fallbacks of level −1 have three gate shapes (LV-SHAPE), a fallback without an R → F gate ends its phase (LV-CN, LV-COUNT), and those with r ≥ 0 number at most n·n_E·(d_o + REL(S)) per scope run (FLAT-ALL_{−1}, STRETCH_{−1}, PL_{−1}, LV-PL) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C50.md, checker PENDING)
- Object (packet P-N5-LV, added at l-si b7f18fe, pinned trunk 601df6e, unchanged during review): docs/si/P-N5-LV-box11.md, sha1
  d0d797f084904f9ce4df641e90298cac53c61356 (L-SI successor 6, Opus 5.5), with its not-to-sign addendum docs/si/P-N5-LV-addendum-box11.md
  (l-si 84974fe, sha1 a15a8871024d33d1734a41cbeb9c2dd75ecdadef). The referees' notes are collected by the lane in
  docs/si/P-N5-LV-fixes-box11.md (l-si 6480a0f, sha1 b75ab1fc4b150e7836757c8719ddcd5c928e1ba7, L-SI successor 8: LV-N1, N-LV-1,
  LV-N2 = N-LV-2, LV-N3, N-LV-3, NL= FALSE); on trunk; repairs only.
  Setting as in RESULTS R31, R35, R37 and R38 (𝒞^1O; scope run S; fallbacks, gates, gate levels, M_k; COARSE_L for −1 ≤ L < ∞, (C1)-(C7);
  b_k(y); θ, w, r; R̄ / R / F; routes π; (h); THR; u*; c, the common cycle node of θ and w; x0 := σ̄_k(o)). SETTING (LV): k is an
  in-scope S4c fallback, THR at k, and M_k = −1 (so every gate at k has level −1). The LEVEL −1 BLOCK of S is the set of its fallbacks
  f_1 < … < f_N with M = −1 and r ≥ 0; D_{−1}, REL_{−1} as in R31 PL and R35 at level −1.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P):
  (a) Proposition LV-SHAPE: in setting (LV), for a gate (y, z) with s := σ_k(y), exactly one of: (α) s, z ∈ F_k and y is its own Ξ- and
      W-cycle node; (γ) s ∈ F_k, z ∈ R̄_k, r_k = −1, y = c and P(W_k z) = ∅; (β) y ∈ R_k, z ∈ F_k, rank o < rank c,
      π^k_s ∩ V_{>c} = ∅ and P(Ξ_k z) = P(θ_k), and if r_k ≥ 0 also W_k(s) ▷ W_k(z) at level r_k. The case s, z ∈ R̄_k does not occur.
  (b) Corollary LV-CN: in setting (LV), if no gate at k is of kind (β), then Ξ_{k+1} = Ξ_k, Iσ_{k+1} = ∅ and k + 1 is the last state of
      its phase. Corollary LV-COUNT: in each phase the in-scope THR fallbacks with M = −1 number at most 1 + (those with a (β) gate); if
      rank o > rank c there is at most one, the phase's last transition. The packet's condition "CONDITIONAL on CN-LAST" is discharged:
      CN-LAST is RESULTS R38 (f), with exactly LV-CN's hypotheses (LV-N1; REFEREE's verdict, REFEREE-2's §C).
  (c) Lemma FLAT-ALL_{−1}: at a fallback k of a scope run with M_k = −1, r_k ≥ 0 and (h) at k and k + 1, R31 FLAT-ALL (i)-(iv) hold with
      M := −1. Part (i) uses FBL, the phase and H1 at k + 1 (R31 FBW-1), not H2 (N-LV-1, citation, both referees).
  (d) Lemma STRETCH_{−1}: if COARSE_{−1}(Ξ_t v) is the same for all t ∈ [s, e] and every v, each Even y is a level −1 tail at most n
      times among the fallbacks k of S with s ≤ k ≤ e and M_k = −1 (LV-N2 = N-LV-2: "k ≤ e", which PL_{−1} (a)'s last run needs; the
      packet's "k < e" is repaired; the bound n stays).
  (e) Theorem PL_{−1}: (a) N ≤ n·n_E·(1 + D_{−1}); (b) the first COARSE_{−1}(Ξ) change j of a dirty interval is an S4a step with
      O_j > −1 ≥ E_j, lev(θ_j, θ_{j+1}) = O_j, and an absorption; (c) D_{−1} ≤ (d_o − 1) + REL_{−1}, hence N ≤ n·n_E·(d_o + REL_{−1}).
      In (a) the block's fallbacks lie in at most 1 + D_{−1} runs of constant COARSE_{−1}(Ξ) (LV-N3, wording). Corollary LV-PL: every
      scope run S has at most n·n_E·(d_o + REL(S)) THR fallbacks with M = −1 and r ≥ 0; with LV-COUNT, all but at most one per phase
      are (β)-fallbacks.
- Not signed (packet §5 and the addendum): CONJECTURE "in scope, THR ⇒ M ≥ 0"; OPEN: THR fallbacks with u* = none (r = −1; bounded
  separately by LV-NONE in packet P-N5-LV2, in review), REL(S) at level −1; the addendum's CONJECTURE NL= is FALSE
  (experiments/red/so/instances/nleq_cex_n48.pg, sha1 e72e4034, L-RED successor 16: an NL (ii) leave at r = L = 47, step 6, vertex
  40 → 9; Lead re-run: one Odd choice vertex, n5 10/1, Oink zlk OK strategies verified, L-SI's nleq.py nl2_fail 1), so the reading
  "NJB in full ⇐ (P) ∧ NL=" gives nothing and NJB's straddling interval stays OPEN; no signed item cites NL at r_j = L (both §Cs).
- Honest limits: (i) SUBCLASS 𝒞^1O. (ii) LV-PL bounds level −1 fallbacks with r ≥ 0 per scope run GIVEN REL(S); the u* = none
  fallbacks, REL(S) at level −1, scope runs per phase and the other open pieces of G-N5-TIME stay OPEN. (iii) The r ≥ 0 part (FLAT-ALL_{−1},
  STRETCH_{−1}, PL_{−1}, LV-PL) has vacuous hypotheses in all data of both referees and the lane: no in-scope THR fallback with M = −1
  and r ≥ 0 occurs. The setting with r = −1 (u* = none) IS reachable (N-LV-3): 173,371 such fallbacks in REFEREE-2's climbs (witness
  docs/referee-2/R2-N5-LV/climb/best_lv_9401.pg, sha1 4b74cd84; Lead re-run: one Odd choice vertex, n5 5/1, Oink zlk OK strategies
  verified) and 351,417 in REFEREE's, with LV-SHAPE holding at every gate (1,037,743 and 1,321,606 gates). (iv) The packet's §0
  statuses of R37 / R38 are stale (LV-N1).
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE lv_probe.py (own engine; logs docs/referee/R-N5-LV/):
  288 𝒞^1O games, 788 in-scope THR fallbacks with r ≥ 0, all M ≥ 0, 0 with r = −1, 11 EQ fallbacks with M = −1; a 2,636,361-mutant
  climb that never reached an in-scope THR fallback (weak evidence); in §C, a climb seeded from best_lv_9401 (769,515 evaluations,
  351,417 u* = none fallbacks, LV-SHAPE 0 failures). REFEREE-2 (own code): 66,655 batch runs (the (LV) setting never occurs) and 4
  climbs (850,608 runs, 173,371 u* = none fallbacks), 0 violations. Lane lvm1.py: 1,032 in-scope THR fallbacks with r ≥ 0, all M ≥ 0.
- Signatures: REFEREE docs/referee/R-N5-LV.md (referee 8054da2, successor 9; §C 46a8030): LV-SHAPE, LV-CN, LV-COUNT (CN-LAST
  discharged by R38 (f)), FLAT-ALL_{−1}, STRETCH_{−1}, PL_{−1} (a)-(c), LV-PL SIGNED; notes LV-N1..N3; no gaps. REFEREE-2
  docs/referee-2/R2-N5-LV.md (referee-2 b1038be, successor 9; §C a769ff5): LV-SHAPE, FLAT-ALL_{−1}, STRETCH_{−1}, PL_{−1} (a)-(c), LV-PL
  SIGN; LV-CN, LV-COUNT and LV-PL's last sentence SIGN CONDITIONAL ON CN-LAST (in §C: unconditional now that CN-LAST is R38 (f));
  notes N-LV-1..3; no gap. §C (both): verdicts the same in substance; joint gap map empty; N-LV-1 accepted by REFEREE (missed),
  LV-N2 = N-LV-2, LV-N3 accepted by REFEREE-2, N-LV-3 accepted and re-run by REFEREE.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
