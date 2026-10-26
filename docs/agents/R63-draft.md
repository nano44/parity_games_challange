# Draft RESULTS R63 (Lead, 2026-10-26 06:38Z by date -u; both §Cs and the fixes file filled) — to CHECKER C72

### R63 [refereed-only] N5 on EVERY game: at an in-phase S4a step a split vertex never leaves the disagreement region (R-STICK_D), unsplit states form a prefix of each S4a run (SN-PREFIX_D), the disagreement set changes only at epoch boundaries (D-EPOCH), and crossings per phase are at most (N_ep − 1) + N_ep·O(n²) + Σ_E X_SN^pre(E) (Lemma X-EP), so every crossing outside a residual inside fixed-frame S4a runs is charged to epochs, hence (with ALT) to ρ and its residuals (2026-10-26) — partial step-4 lemmas for N5 beyond one Odd choice vertex (a reduction; the residual X_SN^pre is OPEN; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C72.md, checker PENDING)
- Object (packet P-N5-XEP, added at l-new a4fa94b0, pinned trunk 8460897d, unchanged during review): docs/new/P-N5-XEP-box44.md, sha1
  237dd5eb31f60f19ef70099dc9351532e88b56f8 (L-NEW successor 23, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-XEP-fixes-box44.md (l-new 2c02b015, sha1 639a70981b5fa0161e92b5b6111a6ce5dc57f3cf, L-NEW successor 24: XEP-N1 = N-XEP-1,
  N-XEP-2, XEP-N2, XEP-N3 data); on trunk; repairs only, no signed statement changes.
  Setting (every game): N5 = SPEC S1-S5; state k = (σ_k, τ_k); σ̄_k, Ξ_k, λ, W_k (σ_k's valuation in G_τ), λ_W as in RESULTS R55; phases as
  in RESULTS R38 (a); f := the in-phase fallbacks of a phase. D_k := {Odd u : σ̄_k(u) ≠ τ_k(u)}; R_D(k) := the vertices whose (σ_k,
  τ_k)-play meets D_k; F_D(k) := V ∖ R_D(k). A vertex v is SPLIT at k if λ_{W,k}(v) ≠ λ(v), UNSPLIT otherwise. A CROSSING is an in-phase
  transition s → s+1 with R_D(s) ≠ R_D(s+1); X_D := the crossings of the phase. Q := the Odd vertices of out-degree ≥ 2; an EPOCH is a
  maximal run of the phase with σ̄|Q constant, N_ep := their number, and e_1 < e_2 < … the in-phase fallbacks of an epoch E (by source).
  X_SN^pre(E) := the crossings with both ends in E and source state ≤ e_{n−1} (all of E's crossings if E has fewer than n − 1 fallbacks)
  at which some vertex unsplit at the source changes R_D-membership.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: RESULTS R55 (a) G_D (a), R21 (a)
  XW, R23 (g) WM (signed under a 𝒞^1O line; its proof, P-N5-Z §8, is game-general, and so is the route via (F1) in G_τ with (VJ) of R57:
  XEP-N2 = REFEREE-2 §1, both referees), R38 (a), and RESULTS R60 (c) Lemma EPOCH (b); §4's last line uses RESULTS R61 (e)-(f) (ALT and its
  N_ep corollary):
  (a) Lemma R-STICK_D: at an in-phase S4a transition s → s+1, every split v ∈ R_D(s) lies in R_D(s+1), whatever D_{s+1} is.
  (b) Corollary SN-PREFIX_D: (a) along a run of consecutive in-phase S4a transitions, for each vertex v the states at which v is unsplit
      form a prefix of the run; (b) after its unsplit prefix a vertex changes its R_D-membership at most once (it may enter R_D, and never
      leaves); (c) per phase, X_D ≤ (f + 1)·n + f + X_SN^D, where X_SN^D := the crossings at which some vertex unsplit at the source changes
      R_D-membership.
  (c) Fact D-EPOCH: on a phase, D_s changes only at epoch boundaries; on an epoch E, D and σ̄ are constant, the honest frame is the
      one-player game G_E (Odd fixed to σ̄_E) and the W-frame is the one-player game G_τ, and they differ exactly at the vertices of D; in
      particular σ̄(c) is constant on each epoch for an Odd choice vertex c that is an honest cycle node of the phase.
  (d) Lemma X-EP: for every phase, X_D ≤ (N_ep − 1) + N_ep·(n² + n + 4n(n − 1)) + Σ_E X_SN^pre(E). With RESULTS R61 (f), N_ep ≤ 1 +
      Σ_{q ∈ Q} (ρ_q + tie_q + nc_q + cyc_q), hence X_D = O(n²)·(1 + ρ + ties + non-clean + cycle-node changes) + Σ_E X_SN^pre(E): signed as
      an inequality; the packet's clause "every crossing outside the residual is charged to the quantity that also bounds fallbacks (R56 (f))"
      is a READING, since R56 (f) bounds f by ρ only and ties, non-clean and cycle-node changes are extra (N-XEP-2, REFEREE-2; accepted by
      REFEREE).
  Sharpening (XEP-N1 = N-XEP-1, found independently by both referees; the packet's weaker forms are true as written): by R55 (a) every split
  vertex already lies in R_D, so R-STICK_D's hypothesis v ∈ R_D(s) is automatic, split vertices never change membership at S4a transitions,
  SN-PREFIX_D (b)'s "at most once" is "never", and so X_D ≤ f + X_SN^D, and X-EP holds without the n² term: X_D ≤ (N_ep − 1) + N_ep·(n + 4n(n
  − 1)) + Σ_E X_SN^pre(E).
- Not signed (packet §5): the qc_toggle configuration instance (experiments/new/box44/instances/qc_toggle.pg, n 5, sha1
  27850ecc3d9e660aefa6a3401d6af0cfc2b3317c: every honest cycle node is the Odd choice vertex 4, and an unsplit vertex enters R_D at an S4a
  step; a configuration, not a counterexample); the residual X_SN^pre (OPEN; for epochs with |D| ≤ 1 L-NEW's P-N5-EPR, in review, reduces it
  to one-Odd-choice phases; |D| ≥ 2 needs Δ-RT); the data.
- Honest limits: (i) A REDUCTION: N_ep (equivalently ρ and its residuals) and X_SN^pre are not bounded here. (ii) Most crossings are in the
  residual: of lib41's 3,222 crossings (S3 start), 1,269 are at epoch boundaries, 1,833 are X_SN^pre and 120 have only split changers (all
  at fallback transitions), none after an epoch freeze. (iii) EPOCH (b)'s term is vacuous in data (XEP-N3).
- Data (DATA, not proof): REFEREE (successor 12, own engine, random start pairs): 11,302 runs, 0 failures; G_D (a) 1.58M and WM 0.85M
  checks; reproduces the packet's lib41 S3 figures exactly (R-STICK_D 14,253 checks; 3,222 = 1,269 + 1,833 + 120) and qc_toggle. REFEREE-2
  (successor 14, own xep_check.py, S3 and random start pairs; lane code not run): 22,969 runs, 66,022 phases, 0 violations; reproduces the
  same lib41 counts exactly (178 split-only crossings over its starts, all at fallbacks); mutations rstick_all (6,444) and xsn0 (607) bite.
- Signatures: REFEREE docs/referee/R-N5-XEP.md (referee 62f4bd2c, successor 12; §C ead5fdb3): R-STICK_D, SN-PREFIX_D (a)-(c), D-EPOCH, X-EP
  SIGNED; notes XEP-N1..N3; no gap. REFEREE-2 docs/referee-2/R2-N5-XEP.md (referee-2 fd43a69f, §C b7b04fad, successor 14): all SIGN; notes
  N-XEP-1, N-XEP-2; no gap. §C (both): verdicts identical; joint gap map empty; XEP-N1 = N-XEP-1 with REFEREE's extension (drop the n² term)
  accepted by REFEREE-2; N-XEP-2 accepted by REFEREE; XEP-N2 = REFEREE-2 §1; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a reduction; no running time). GAPS G-N5-TIME: open.
