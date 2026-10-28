# R-N5-DEPTH-add: REFEREE report on packet P-N5-DEPTH-add (L-SI box 22, CONDITIONAL companion: Lemma GATE-PUSH, Proposition PURE-LEN, Lemma MONO-REF, Lemma E-ONEWAY)
Referee: REFEREE (successor 16), Opus 5.5 (owner ruling D15). FIRST referee (Lead queue of 19:18Z on 26 Oct and 21:05Z on 28 Oct by date -u).
- Object and pin: docs/si/P-N5-DEPTH-add-box22.md, sha1 4d51aa5ea4e1a1d145da4cb825deab75198abae7, 71 lines, author L-SI successor 18,
  frozen at aa6061d1 (26 Oct 18:47Z), on my tree after merging trunk.
- Written 2026-10-28T21:14Z-21:21Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ file on DEPTH (or DEPTH-add) on my tree, on trunk or on origin/claude/referee-2 (re-listed in
  the same turn as the fetch; 0 / 0 / 0 at 21:18Z). No lane code run (evenside.py, exitx.py, quotecheck.py neither executed nor imported). D1.
- Status of the conditional premises at this review: P-N5-ROOT FREEZE-A (b), (R-LEN): both referees' signatures, joint §C empty (ROOT §C
  da0c1902). P-N5-OFFMONO-add ZCH-COUNT and P-N5-OFFMONO OFFSET-MONO: both signatures, unit §C empty (96b2cd9a). P-N5-DEPTH STATIC-DEPTH (and
  PURE-END, used by PURE-LEN's proof): my signature (R-N5-DEPTH, 1d74c963); REFEREE-2's pending. So PURE-LEN's premises are not yet all
  double-signed. That does not matter for my verdict on it below.
- Quotes: all 5 "[Q path@commit:lines] «…»" quotes verbatim at 78bc0e6a8 (scratch/flip_quotes.py: QUOTES 5 FAILED 0).
- Tool: scratch/dadd_probe.py (own engine rl_engine; offmono_probe's κ and par; root_probe's firstD; checks in §5). Logs scratch/dadd_logs/.

## Verdicts (sign-off line per item)
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | Lemma GATE-PUSH and its Count (CONDITIONAL on FREEZE-A (b), (R-LEN)) | SIGNED, conditional as stated (its premises are now double-signed). NOT EXERCISED in any data (§5): rests on proof alone |
| §2 | Proposition PURE-LEN | NOT SIGNED: FALSE as stated (gap G-DADD-1). A frozen class keeps a long per-class pure C-interval while other classes move (pure_22, §2). The class-local form (the LAST Even switch of U_c) follows by the same proof and holds in all data |
| §3 | Lemma MONO-REF | NOT SIGNED as stated: FALSE when m lies after c on z's play (gap G-DADD-2, frzh3n_701_best, §3). SIGNED with "m at or before the first visit of c" added |
| §3 | Lemma E-ONEWAY | SIGNED with the matching hypothesis (e1 at or before the first c on w's play at every state of [t + 1, t′]), via the repaired MONO-REF. As stated, its proof does not cover the case e1 after c (704 data windows, conclusion held in all of them) |
| §4 | data | not signed |
Two gaps: G-DADD-1 (PURE-LEN as stated false) and G-DADD-2 (MONO-REF as stated false; E-ONEWAY inherits a hypothesis). Notes DADD-N1..N3.
Nothing here bounds N5's running time; not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. GATE-PUSH, re-derived
- Setting. The per-class C-interval is read transition-locally (as R-N5-GCX's GCX-N1, for class c alone): A^c non-increasing, D ∩ U_c
  constant, Δ(u) constant for u ∈ DD^c_t ∩ DD^c_{t+1}. Pure means D ∩ U_c = DD^c at every state. A_t = F_D(t) ∩ U_c, as in FREEZE-A ✓.
  FREEZE-A's hypotheses (S4a steps, A non-increasing) hold on such an interval inside a fallback-free run ✓.
- Proof ✓. "u lies on no honest cycle at t, t + 1 (as in FREEZE-A (c))" ✓: σ̄(u) ∈ A, whose honest plays meet no gate. y2 ∈ A_{t+1} ⊆ A_t (D ∩
  U_c constant, so u ∈ D_{t+1}, and u is D-direct there) ✓, so y2 ∈ Y^u_t ✓. y1 ∈ A_{t+1} gives y1 ∈ Y^u_{t+1} ✓. The chain κ_t(y1) ⪯ κ_t(y2) ⪯
  κ_{t+1}(y2) ⪯ κ_{t+1}(y1) follows from κ-Y-FORM_D at t and t + 1 and (M2κ) ✓. The last step is strict unless κ_{t+1}(y1) = κ_{t+1}(y2) ✓.
  FREEZE-A (b) with t ≥ a + L and y1 ∈ A_{t+1} gives M_{t+1}(y1) = M_t(y1) ✓. (y1 = c is possible only in the tie case, since κ(c) is constant.)
- Count ✓.
  - A switch away from y1 ∉ A_{t+1}: y1 leaves A at that transition, and a direct gate never again points to a vertex outside A. So these
    transitions number ≤ |A_a| ✓.
  - Every other non-tie switch is a strict length rise of y1 ∈ A. By (R-LEN), each y has ≤ |U_c| − 2 such rises on [a + L, b] (κ is
    monotone, M is fixed, ℓ ∈ [1, |U_c| − 1]). Charged to the pair (u, y1), that gives ≤ Σ_u deg(u)(|U_c| − 2) ✓.
  - "(Off D, σ̄ = τ is constant …)" ✓.
- Exercised: NEVER. In 7,295 pure per-class C-intervals (2,492 with gates), no σ̄ change at a gate after a + L with y1 ∈ A_{t+1} occurs (§5).
  GATE-PUSH rests on proof alone (DADD-N1).

## 2. PURE-LEN: false as stated (gap G-DADD-1)
- The proof step that fails: "STATIC-DEPTH applies on U_c and bounds each piece by |U_c| − 1". STATIC-DEPTH's per-vertex part is local: on a
  piece, every vertex of U_c settles by its d* (all H_b-successors of U_c stay in U_c). But its LENGTH conclusion b − a ≤ max d* comes from
  a GLOBAL argument: once σ is unchanged everywhere, the next transition is a fallback. A class that has settled does not stop the run, and
  other classes keep switching. So the length of a per-class C-interval is not bounded by class-c quantities.
- Witness: pure_22 (experiments/new/box22/instances/pure_22.pg, sha1 f7ba3897, n = 22) at its S3 start.
  - Class c = 10, U_c = {4, 9, 10}, all Odd, so there are no Even vertices and no gates (D ∩ U_c = ∅; pure vacuously); A = U_c.
  - On states [23, 33] of one phase (λ_Ξ and τ constant, no fallback) the class is constant, and the transitions are all good, so this is
    one per-class pure C-interval.
  - Bound: L = 2, N_σ̄ = 0, N_cyc = 0, so b − a ≤ 2 + 1·2 = 4. Actual b − a = 10. Meanwhile Even vertices of other classes switch at every
    transition 23 → 24, …, 32 → 33 (5 and 21; 5; 14; 1 and 19; 18; 15; 19; 0; 13; 20).
  - Data: 1,140 per-class pure intervals exceed the bound (lib 402, lib41 396, random 342), every one with class c making no Even switch
    on [a, b] (PLX_frozen = all). Most have |U_c| = 1. Three are non-trivial (|U_c| ≥ 3) at S3 starts: pure_22 twice, and best_2 (sha1 9ee6d36c).
- What does hold (proposed repair; REFEREE check, not a signature on frozen text): the class-local form. "Every Even switch of U_c in [a, b]
  lies at a transition < a + L + (1 + N_σ̄ + N_cyc)(|U_c| − 1) + N_σ̄ + N_cyc", under the same premises and GEN_W on U_c. Proof: the packet's
  cutting, then on each piece [p, q] STATIC-DEPTH's per-vertex induction restricted to U_c. That induction uses (A), (B), W-MONO, Ξ-SUCC and
  P2, all local or global facts that hold. It gives σ_t = σ_q on U_c for t ≥ p + max_{U_c} d*, with max_{U_c} d* ≤ |U_c| − 1. Data (PLSW):
  0 failures in all 7,295 intervals.
  - If the global length is wanted, the hypotheses must be global: every class pure, cuts at σ̄ and cycle changes of every class, and
    STATIC-DEPTH applied to the whole game.

## 3. MONO-REF: false as stated (gap G-DADD-2); E-ONEWAY
- The proof's telescoping "along the T-vertices x_1, …, x_h = m of z's (t+1)-play … with par_{t+1}(x_i) = x_{i+1}" breaks when the list
  passes c. par is defined only up to c, and the term off(c; x_{i+1}) = −κ(x_{i+1}) is non-increasing, not non-decreasing.
- Witness: frzh3n_701_best (experiments/n5-exhaustive/results/box9b/frzh3n_701_best.pg, sha1 6de40c62, n = 8) at its S3 start, t = 1.
  - c = 2: an Odd vertex of priority 6, out-degree 1, so c ∉ Q and s_c = −1.
  - z = 0 (Even), m = 4 ∈ Q. z's honest (t+1)-play is 0 → 2 → 4 → (2). So m ∈ T is on it, m ≠ z, and there is no Q-vertex from z (incl.)
    to m (excl.): the hypothesis holds literally.
  - κ_t(0) = (0, −1), κ_t(4) = (0, −2); κ_{t+1}(0) = (0, −1), κ_{t+1}(4) = (0, −1). So off(0; 4) falls from (0, 1) to (0, 0).
  - Data: 1,527 failures in 29,786 checks with m after the play's first c; 0 failures in 1,411,999 checks with m at or before it.
- Repair: add "m at or before the first visit of c on z's (t+1)-play". With it, MONO-REF is SIGNED.
  - The telescoping identity ✓.
  - Each level term is OFFSET-MONO ✓, at x_i ∈ Q off every honest cycle at t, by the hypothesis.
  - The first term is OFFSET-MONO (z ∈ Q) or Step 1 on the Q-free path ✓. Step 1 needs the path's vertices ≠ c, outside Q, Odd ones of
    out-degree 1, and Even switches along Iσ_t ✓.
  - With add3's OFFSET-MONO⁺ (signed by both referees) the no-cycle hypothesis can also be dropped (DADD-N2).
- E-ONEWAY ✓ with the matching hypothesis.
  - h ✓: h = κwt_c(w) + κwt_c(π_a) = κwt_c(w) + off_s(a; e1) at every s ∈ [t, t′], since π_a and e1 are unchanged.
  - The strict step ✓: (SW), (M1κ) give κ_t(b) ≻ κ_t(a) (a, b ∈ U).
  - MONO-REF at b, at t → t + 1 ✓: e1 lies on b's (t+1)-play, since it lies on w's and w ≠ e1.
  - MONO-REF at w on [t + 1, t′] ✓, then the switch-back contradiction (h ≻ g_{t′} needed, g_{t′} ≻ h held) ✓.
  - Both MONO-REF uses need e1 at or before the first c on the respective plays. The repaired hypothesis "e1 at or before the first c on w's
    honest play at every state of [t + 1, t′]" gives that, also for b at t + 1.
  - Data: 184,217 window checks, 0 switch-backs. 704 of them have e1 after c on w's play, so the conclusion held there too; the case is
    simply outside the proof (DADD-N3).

## 4. Notes
- DADD-N1 (vacuity). GATE-PUSH is never exercised in my data (no σ̄ change at a gate after the A-freeze with y1 ∈ A_{t+1} in 7,295 pure
  intervals). Its count is therefore untested; the landing text should say "rests on proof alone".
- DADD-N2 (premise). With OFFSET-MONO⁺ (add3, both signatures) MONO-REF's "no honest cycle at t" hypothesis is unnecessary. The "before c"
  restriction of G-DADD-2 stays necessary.
- DADD-N3 (E-ONEWAY). The conclusion held in all 704 windows with e1 after c, but the proof does not reach them. Proving it there would need a
  different argument.

## 5. Data (own engine; DATA, not proof)
| set (log in dadd_logs/) | N5 runs | MONO-REF m ≤ c (fail) | m after c (fail) | E-ONEWAY windows / checks (e1 after c) / switch-backs | pure per-class C-intervals (with gates) | PURE-LEN as stated: fail (all frozen) | class-local form: fail | GATE-PUSH checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib 1,140 files, n ≤ 40 (4 parts), S3 + given + 2 random | 2,739 | 749,497 (0) | 12,332 (1,099) | 31,129 / 90,798 (324) / 0 | 3,127 (1,268) | 402 | 0 | 0 |
| lib41 (experiments/new/box41), n ≤ 64, S3 + 2 random | 1,130 | 589,230 (0) | 12,829 (380) | 22,934 / 84,579 (377) / 0 | 2,278 (1,157) | 396 | 0 | 0 |
| random 𝒞^kO, n 4-16, k ≤ 6, seed 231 | 9,000 | 21,237 (0) | 821 (48) | 1,985 / 257 (3) / 0 | 1,861 (50) | 342 | 0 | 0 |
| nep90 / nep76 / long121, L-RED ul instances, cxmig_k (given starts) | 18 | 52,035 (0) | 3,804 (0) | 1,338 / 8,583 (0) / 0 | 29 (17) | 0 | 0 | 0 |
- PURE-LEN failures are all "frozen" (PLX_frozen = PL_FAIL in every set). The n ≤ 24 library run (lib_n24_rs2) gave the same picture: 194
  failures, all frozen; MONO-REF post-c 502 failures.

DONE: this report. FINDINGS: GATE-PUSH SIGNED (never exercised); PURE-LEN FALSE as stated (G-DADD-1; class-local repair holds); MONO-REF FALSE
as stated (G-DADD-2; signed with "m before c"); E-ONEWAY signed with the matching hypothesis. NEEDS: Lead: route G-DADD-1, G-DADD-2 and
DADD-N1..N3 to L-SI's fixes file (docs/si/P-N5-DEPTH-add-fixes-box22.md); §C against REFEREE-2 on your word.
