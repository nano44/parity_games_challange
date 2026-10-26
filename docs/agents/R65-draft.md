# Draft RESULTS R65 (Lead, 2026-10-26 09:02Z by date -u; both reports and both §Cs filled; fixes file filled 09:20Z by date -u) — to CHECKER C74

### R65 [refereed-only] N5 and its keep-τ-on-ties variant N5^τ compute the same state functions and make the same τ-keeping transitions from τ-stable states, so a per-phase proof for N5 transfers to N5^τ unless it uses more than the Σ-transition, τ fixed, τ-stability, the shared state functions, the phase-end facts and R15 (c), (d) (Lemma Στ-STEP, transfer clause); both referees audited the per-phase chain behind RESULTS R48 (i) and R50 (h) and found it complete and free of any use of S4b's output, so premise (Στ) of RESULTS R64 (e) is confirmed by referee audit and EP-1 holds without it: an epoch with one disagreement vertex has len(E) ≤ T*(G′_E) + 1 = O(m·Δ·n¹¹) (2026-10-26) — a transfer lemma plus an audit for N5 (not M3, not a step-4 pass, not a TARGET.md claim; the number of epochs and epochs with |D_E| ≥ 2 are not bounded; G-N5-TIME stays open), CHECKER PASS (docs/checker/C74.md, checker PENDING)
- Object (packet P-N5-STAU, added at l-new 010bfdae, pinned trunk ca0a4e97, unchanged during review): docs/new/P-N5-STAU-box45.md, sha1
  7446d9a9e198ffa5073e0d43823d753b6aa46b3b (L-NEW successor 24, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-STAU-fixes-box45.md (l-new ee95661f, sha1 42d7b04c7e00bee1a95241b52edf2e7a67004f33, L-NEW successor 25: STAU-1 with
  REFEREE's two repair lines verbatim, N-STAU-2..4, STAU-N1..N3, audit-list completions, box24); on trunk; repairs only, no signed statement
  changes.
  Setting (every game): as in RESULTS R64 (N5 = SPEC S1-S5 with FIX 1-4, Q1-Q4; N5^τ := N5 with S4b replaced by S4b^τ: if Iτ ≠ ∅ and τ is
  value-optimal against σ in S4b's arena H′, keep τ, otherwise SPEC's S4b). σ_a := S4a's output; Σ(σ, τ) := σ_a if σ_a ≠ σ, else S4c's Even
  switch-all on Iσ. A state is τ-STABLE if Iσ ≠ ∅ and (Iτ = ∅ or τ is value-optimal against σ in H′); a Σ-TRANSITION is (σ, τ) → (Σ(σ, τ), τ).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC; RESULTS R18 (d) Lemma S (a)
  (= (VJ), RESULTS R57 (a)); R15 (a), (c), (d); the standing SPEC premise that S1's procedure returns an optimal counterstrategy (1E-N3,
  RESULTS R57), which the packet's (b) uses in citing "S4b's output τ is value-optimal" (N-STAU-2, REFEREE-2; accepted by REFEREE); R15 (a)
  also transfers and belongs in (d) (STAU-N1 = N-STAU-3, both referees):
  (a) Lemma Στ-STEP (a): at every state N5 and N5^τ compute the same Ξ, W, Iσ, Iτ, the same S4a output σ_a and the same S4c switch-alls.
  (b) Lemma Στ-STEP (b): if N5's transition from (σ, τ) keeps τ, N5^τ's transition from (σ, τ) is the same transition.
  (c) Lemma Στ-STEP (c): if N5^τ's (or N5's) transition from (σ, τ) keeps τ, then (σ, τ) is τ-stable and the transition is the Σ-transition;
      conversely N5^τ's transition from a τ-stable state is the Σ-transition.
  (d) Lemma Στ-STEP (d): every N5^τ iteration applies a non-empty improving switch to σ or to τ, so the proofs of RESULTS R15 (c), (d) apply
      to N5^τ runs.
  (e) Corollary, transfer clause: a per-phase proof for N5 transfers to N5^τ unless it uses, at an in-phase transition, more than the
      Σ-transition, τ fixed, τ-stability, the shared state functions ((a)), the phase-end facts "Iσ = ∅ ⇒ τ changes or the run stops" ((c))
      and R15 (c), (d) ((d)). SIGNED by both.
      The Corollary's sentences 1-2 are SIGNED WITH GAP STAU-1 (joint; minor, wording) and read with REFEREE's repair, checked by REFEREE-2:
      "The τ-keeping transitions of N5^τ are exactly the Σ-transitions from τ-stable states; N5's are those among them at which SPEC's S4b
      returns τ; the in-phase ones are the τ-keeping ones with λ unchanged." and "N5 and N5^τ make different transitions only (i) at a
      τ-stable state where SPEC's S4b returns a value-equal τ′ ≠ τ (N5 leaves the phase, N5^τ need not), and (ii) at a state with Iσ = ∅
      where SPEC's S4b returns a value-equal τ′ ≠ τ (both leave the phase, N5^τ by Odd's fallback)." As written, sentence 1's "exactly" is
      only an inclusion (a τ-keeping Σ-transition can change λ_Ξ; witness REFEREE-2's nonex_min.pg, n 4), and sentence 2 misses case (ii)
      (witness REFEREE's is0_c1o264.pg, n 12, sha1 b0006099716e5c57932c0ce7f334ae3750ff9188). The referees differ only on whether sentence 1
      alone was a gap (REFEREE-2) or a note (REFEREE); both close with the repair. No downstream effect: (Στ) and EP-1 use τ-keeping in-phase
      transitions only, and case (ii) ends the phase in both runs.
- Audited (both referees CHECKED the packet's §2 table; an audit, not a signed theorem):
  (f) Audit (1), "is §2.1 the whole per-phase chain behind R48 (i) and R50 (h)?": YES (both). Each referee computed the RESULTS citation
      closure with its own script: R15, R17, R18, R19-R34, R38, R39, R42, R44, R45, R48, R50 (R47 only in R50's not-signed reading), equal to
      the packet's list. Completions, none on a proof path that uses S4b: four entry-named files outside the packet's 66 (the SPEC,
      docs/lit/T21-VJ00-check, N5-brchanges-box11, docs/red/R58-n5-width §9 = R18 (a); STAU-N2 = REFEREE-2 §2.1 (i)); referee-written proof
      steps on the chain (X-1 / TF for R21 (i), CAP-1 for R25, TB-1 and N-U1-3 for R24; REFEREE-2, missed by REFEREE's scan of docs/referee*,
      then checked by it); table rows "R17 Lemma P / Theorem PH on τ-fixed segments as runs on G_τ" and "Lemma S (b)", both "yes" (REFEREE-2).
      Detail: REFEREE called N5-1Oacyc-box24 "not on the chain"; REFEREE-2 shows it is (cited as a proof step by P-N5-X, P-N5-XA, P-N5-NH),
      and the packet lists it; no effect on either answer.
  (g) Audit (2), "does any proof in that chain use S4b's OUTPUT implicitly?": NO (both). Own searches wider than the packet's (REFEREE
      108 + 172 hits, including SPEC's ASCII H′; REFEREE-2 323 hits plus two further passes), all hits read in context; every tie-break used
      is S4a's (Lemma TB) or σ̄'s.
  (h) Consequence (by (e) with (f), (g); both referees state it): premise (Στ) of RESULTS R64 (e) holds, so RESULTS R64 (e) EP-1 holds without
      premise: every epoch E with D_E = {u} has len(E) ≤ T*(G′_E) + 1 = O(m·Δ·n¹¹), and, by R64 (f), X_SN^pre(E) ≤ len(E) there.
- Not signed (packet §3, §4): the data; the conclusion line (READING), replaced by (h). The Corollary's sentences as written (STAU-1).
- Honest limits: (i) (h) rests on an audit: both referees read the closure's proofs by search plus targeted reading, not every line of
  the 66 files (10,307 lines, REFEREE's scope note); a missed implicit use of S4b's output would void (h) for the entry containing it.
  (ii) It bounds |D_E| = 1 epochs only. The number of epochs per phase (N_ep), and epochs with |D_E| ≥ 2, are not bounded here; with R63 and
  R64 these are the open parts of the per-phase count. (iii) (h) is per epoch; no per-phase, per-run or running-time bound on any class
  follows from this entry alone.
- Data (DATA, not proof): REFEREE (successor 13, own stau_probe.py; lane code not run): 0 failures of (b), (c), (c) for N5, (c) converse,
  (d), DIFF_OTHER, "in-phase = Σ", and R48 (i) on N5^τ phases, on 20,000 random games, 5,000 random 𝒞^1O and lib41 (45 files with n > 64
  skipped); lib41 max f 33; DIFF_IS0 44 (all at Iσ = ∅), DIFF_TS 4,761. REFEREE-2 (successor 15, own stau_check.py; lane code not run):
  122,512 states over 503 files (lib41, 3,000 random 𝒞^1O, 2,000 random general games, div_n8), 0 violations of (a)-(d), the converse and
  the corollary inclusion; LINK 45,490 checks, 0; R48 (i) on N5^τ phases max f 37, phase length 112; mutants keep / sig caught (1,574 / 48);
  L-COMP's 6 pinned instances (l-comp 16c960b5): 0 violations, keep counts equal to its own at step level; is0_c1o264 reproduced (is0_count.py:
  86 random 𝒞^1O + 76 random general states of that case, of which 3 + 1 lead to different successors).
- Signatures: REFEREE docs/referee/R-N5-STAU.md (referee 48674360, §C 3a999280, successor 13): Στ-STEP (a)-(d) SIGNED; transfer clause
  SIGNED; sentences 1-2 SIGNED WITH GAP STAU-1; §2 CHECKED, (1) YES, (2) NO; notes STAU-N1..N3. REFEREE-2 docs/referee-2/R2-N5-STAU.md
  (referee-2 8e42c473, §C fbbe66a4, successor 15): (a)-(d) SIGN; Corollary SIGN, in its §C SIGN WITH GAP STAU-1 (it missed sentence 2,
  reproduced is0_c1o264); §2 CHECKED, (1) YES, (2) NO; notes N-STAU-1..4. §C (both): no verdict disagreement; joint gap STAU-1 (wording),
  closed by REFEREE's repair text in the fixes file; STAU-N1 = N-STAU-3; STAU-N2 = REFEREE-2 §2.1 (i); N-STAU-2, N-STAU-4 and the
  referee-written steps accepted by REFEREE; box24 detail as in (f); nothing open of substance.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a transfer lemma, an audit, and a per-epoch consequence; no running-time
  bound). GAPS G-N5-TIME: open.
