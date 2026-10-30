# R-N5-WCH: REFEREE report on packet P-N5-WCH (L-NEW box 79): returns, tie switches and gap levels paid by per-vertex W-changes; one premise [P-WCHτ]
Referee: REFEREE (successor 19), Opus 5.5 (D15). Lead brief 2026-10-30 09:57Z (date -u). REFEREE-2 successor 22 reviews in parallel.
- Object and pin: docs/new/P-N5-WCH-box79.md at claude/l-new 2ad78f51, `git show 2ad78f51:<path> | sha1sum` =
  31caa72e5265b7373218ce64e38d253112189506 (550 lines); line docs/new/P-N5-WCH-box79-line.txt sha1 9ac6fdba5ca5910a4585babff5938a0d8d107a78.
  Both equal the Lead's figures.
- Runs 2026-10-30T10:00Z-10:06Z; report written 10:08Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independence: no docs/referee-2/ file for this packet opened.
- Premises opened: SPEC at aefb71a3 (l. 25-57); RESULTS R90 entry (items (a) OPT-OFF, (b) W-MON′, (c) W-SUCC, (d) W-RETURN-G, (e) CUT-CHARGE,
  (g) LATE-SPLIT: labels present, l. 6116 ff.), R91 entry (items (a) XW, (b) W-MON, (c) FB-W, (h) GAP-MON, (i) SW-IN, (k) REOPEN-W, (m) GAP-RED:
  labels present, l. 6384 ff.), R15, R17 (a), R56, R86, R88 (f), R89; P-N5-CUT and P-N5-GAP, which I refereed.
- Quotes: the 3 SPEC quotes at l. 47, 51-53, 56-57 are verbatim. The 4 S1 quotes ([S1-rank] «SPEC:26», [S1-val] «27-28», [S1-ord] «29-30»,
  [S1-Xi] «31») are verbatim, but their line tags are ONE LINE LOW at the quote base aefb71a3, where they sit at l. 27, 28-29, 30-31 and 32
  (WCH-N1). The packet runs no quote check for box 79.
- Scope (D1): a REDUCTION for N5 on every game to one premise [P-WCHτ] plus residual counts, none bounded. §7 (N5-LZC) is a labelled VARIANT.
  G-N5-TIME stays OPEN. Not a TARGET.md claim.

## Verdicts
| § | item | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| 1 | setting, premises, definitions | CHECKED; standing premise named (R57 1E-N3, R90 (a) (i)) |
| 2.1 | Fact REW (R1, R2), Fact LEX, COMMON PREFIX | SIGNED |
| 3 | Lemma TIE (a), (b) | SIGNED (cases (a1)-(a3), (b) re-derived; wording note WCH-N2) |
| 4.1 | Lemma NEW-BOUND | SIGNED |
| 4.2 | Theorem RET-WCH | SIGNED (Steps 1-2, (i)-(iii), the cycle-node exclusion, distinctness re-derived; WCH-N2) |
| 4.3 | Corollaries RUN-WCH, REP-WCH | SIGNED; REP-WCH needs only RET-WCH and R90 (g)'s definitions, NOT FW-R*′ (§4) |
| 5.1 | Lemma SIL-Z (a)-(c), Corollary SC-GXC | SIGNED; uses only landed R90 (a) (ii), (b), (c), (d), Fact B, R91 (a), R15, [S2], [S4a], [V1], [V2] (§5) |
| 5.2 | Lemma GXC-CLOSE, Theorem GXC-SPLIT | SIGNED |
| 5.3 | Lemma LEVEL-MON, Corollary DROP-PAID | SIGNED |
| 5.4 | Corollaries FBO-R56, FBO-SPLIT, ZF-SPLIT | SIGNED |
| 6 | Theorem WCH-RED, Corollary WCH-ONE | SIGNED (each displayed inequality re-derived) |
| 7.1-7.4 | N5-LZC: LZ-OPT, W-MON_LZ, LZ-STRICT, RUN-WCH_LZ / REP-WCH_LZ | SIGNED, for the VARIANT only |
| 7.5 | LZ-NOSIL (the implication) | SIGNED; and ASSUMPTION OPT-ONLY CHECKED TRUE (§7): R90's proofs of Fact B, (a) (ii), (b), (c), (d) use S4a's σ_new only through OPT-OFF (i) (pointwise optimality), never through S1's tie-break |
| — | OPT-ONLY in the N5 part | NOT used: OPT-ONLY / LZ occur only in §0, §7, §8 (grep) |
| 8 | trimmed, DATA, READING, symbol table | not signed; pinned «box 79» PASS (§9) |
| — | RESULTS line (9ac6fdba) | MATCHES §2-§7 and claims nothing more; my strict symbol test finds no free symbol (§10) |
No gap. Nothing FALSE. Notes WCH-N1..N4.

## 3-4. TIE, NEW-BOUND, RET-WCH (the Lead's first watch item)
- TIE ✓. (a): v not its own W′-cycle node excludes v own W-cycle node (else W(v) = (v, ∅, 0) = W′(v)); [V1] for σ_t. (a1) π avoids v: [F1]
  and [V2] squeeze v ⊕ W′(d) between W(v) and W′(v). (a2) v on π's cycle AFTER c* (π reaches c* before v): P(W′(v)) = ∅; P(W′(d)) = ∅ gives
  ρ's cycle top c* and equality; else its top u is odd ([F1], R1) and v ⊕ W′(d) ◁ W′(v), against [V2]'s W(v) ⊴ v ⊕ W′(d). (a3) v on π
  BEFORE c* (on the path or on the cycle before c*): c* ∉ X; u = top of X; above c*: odd, and either u ∉ P(W(d)) (then P(W′(d)) ⊋ P(W(d))
  with odd top: W′(d) ◁ W(d), against W′ ⊵ W) or u ∈ P(W(d)) (then u, v share a σ⁺-cycle whose top is c*: contradiction); below c*: R = ∅,
  W′(d) = (c*, P(W(d)), ℓ(W(d)) + q + 1), c* odd contradicts [F1] by R2, c* even makes W′(d) longer and worse. (b) ✓ (π misses v: worse
  reward; π reaches v: P(W′(d)) ≠ ∅ would have an even top above v, and ρ's cycle would beat W′(v)).
- WCH-N2 (wording, both TIE and RET-WCH): "(a2) / (ii) v lies on π's cycle" must be read as "v is reached only after π's cycle node", and "(a3)
  / (iii) v lies on π's path part" as "v is reached BEFORE the cycle node" (this includes v on the cycle before c*). With that reading the
  three cases partition; with the literal "path part = the lasso's tail" reading, the configuration "v on the cycle between π's entry and c*"
  would fall into (a2) / (ii), whose argument then uses «π's path to c* avoids v», which is false there. This is the configuration of P-N5-GAP's
  G-GAP-1. The proofs of (a3) / (iii) cover it verbatim (they only use that v precedes c* on π), so it is wording, not a gap.
- NEW-BOUND ✓ (one new switch per Even edge; every other transition holds a return).
- RET-WCH ✓.
  - λ_W constant on F: v is its own W-cycle node at all states of F or at none; at all states, W(v) is constant, excluded by W_{k+1}(v) ≠ W_k(v).
    This is the cycle-node case, closed.
  - Step 1 ✓ ([V1] at k with σ_k(v) = e).
  - Step 2: ρ := σ_{k+1}[v ↦ e] ∈ H_k, [F1] in H_k. (i) ✓. (ii) ✓, under WCH-N2. (iii) ✓, checked line by line: v above c would put v in
    P(W_{u+1}(e)), so e's σ_{u+1}-play would cycle through v (σ_{u+1}(v) = e) before c; u* above c is odd, and either W_{u+1}(v) ◁ W_{k+1}(v)
    (against W-MON on the S4a steps of [k + 1, u]) or u* and v share a cycle; u* below c: c even contradicts W-MON, c odd contradicts [F1] by R2.
  - The final chain W_{u+1}(v) = v ⊕ W_{k+1}(e) ◁ W_{k+1}(v) ⊴ W_{u+1}(v) ✓.
  - Distinctness ✓ (k₂ ≥ u₁ + 1; the intervals [k, u] are disjoint).
- RUN-WCH ✓ (a TT transition is a TIE event; one target per leave). REP-WCH ✓ — the Lead's second watch item. A REPEAT at u₂ has an earlier
  late adoption at u₁ of the same edge, so σ_{u₁+1}(y) = z, u₁ + 1 ≤ u₂, σ_{u₂}(y) ≠ z: a return. REP_F ≤ Σ RET_F ≤ Σ_e d_E(e)·WCH_F(e) +
  TIE_F follows from RET-WCH and RUN-WCH's TT ≤ TIE alone. Neither FW-R*′ (P-N5-LATEP, unlanded at freeze) nor any LATE′ notion is used ✓.

## 5. SIL-Z, SC-GXC (the Lead's third watch item), GXC-CLOSE, GXC-SPLIT
- SIL-Z (a) ✓: the chain OPT-OFF (ii) at q − 1 → q (R90 (a)), W-SUCC on [q, j − 1] (R90 (c)), W-MON′ at j − 1 → j (R90 (b)), W-RETURN-G (R90 (d)),
  and constancy of W*(c) on [q, j] (the class-S definition, R90 (e)): all LANDED R90 items, read in the frame τ* = τ_{j−1} (R90 K8). Then [V1]
  at j − 1 and j. (b) ✓ ([S4a] ⇒ (v, c) ∈ Iσ_{j−1}; [S2]; R91 (a) XW; [V1], [V2] across the two pairs as formal triple facts, as R91 H12
  states). (c) ✓ (R15; [S2]; [V1] at j for c, at j − 1 for d; [V2]). No unlanded lemma, no LATE′, no box-70 statement is used ✓.
- SC-GXC ✓: a class-S re-entry outside NC and NT is the GXC event (v, j − 1) (W_j = W*_j because τ_j = τ*); a phase meeting R lies in R; R's
  phases are cut only by its τ-changing transitions: ≤ B_R + 1.
- GXC-CLOSE ✓ (exits ≤ [x ∈ Z_a] + entries; no entries at τ-fixed fallbacks by R91 (h); entries at S4a steps are W-rises by R91 (k)).
- GXC-SPLIT ✓ (at an S4a step R91 (b) and ⊴ give equality: a TIE event; else a fallback, CL or FBO).

## 6. LEVEL-MON, DROP-PAID, FBO-*, ZF-SPLIT, WCH-RED, WCH-ONE
- Fact LEX ✓ (the top differing rank decides the signed weight: |Σ_{r<R}| ≤ 2^R − 1); COMMON PREFIX ✓ (lexicographic sandwich).
- LEVEL-MON ✓: Ξ_t ⊴ Ξ_{t′} (R15) ⊴ W_{t′} (XW) ⊴ W_t (W-flat S4a steps; FB-W at fallbacks); the prefix of length LEV_t − 1 is shared.
- DROP-PAID ✓ (≤ 1 + WCH segments; on a segment LEV is non-decreasing over the states with v ∈ Z, n + 2 values, ≤ n + 1 strict rises).
- FBO-R56 ✓, FBO-SPLIT ✓, ZF-SPLIT ✓ (SW-IN gives v ∈ Z_k, Z-flat gives v ∈ Z_{k+1}, LEVEL-MON with t′ = k + 1 makes ≠ into >).
- WCH-RED ✓ (each line is the cited corollary; (G)'s ZF bound is (n + 1)·Σ_v(1 + WCH)). WCH-ONE ✓ (WCH_F(e), WCH^S4a_P(v) ≤ WCH_S(·) for the
  τ-stretch S ⊇ F, P; the arithmetic n + n·w, (n + 1)·n·(1 + w), m_E·w checked).

## 7. N5-LZC and OPT-ONLY
- LZ-OPT ✓ (consistency of every step with W*; ℓ drops by 1 and the cycle node is kept; at c the rule-2 / [V1] case closes a cycle with top c;
  the path set accumulates exactly P(W*(x))). W-MON_LZ ✓. LZ-STRICT ✓ (TIE applies to σ⁺ = σ′, a pointwise optimum with W′ = W*; its (a) / (b)
  is the keep-rule). RUN-WCH_LZ / REP-WCH_LZ ✓ (every premise of §4 re-proved for the variant; a W-run transition switches some Even vertex,
  since σ′ = σ_t with τ kept triggers S4c).
- ASSUMPTION OPT-ONLY, checked against R90's object (P-N5-CUT §1-§3, which I refereed, R-N5-CUT §1-§3): Fact B uses only S4a-S4d and R15 (d)
  read on σ′; OPT-OFF (i) uses only that σ_new is the pointwise optimum of A = G_{τ*}|H_t; (ii), W-MON′, W-SUCC, W-RETURN-G use only (i), [V1],
  [V2], Fact B and the frame conventions. No step uses S1's tie-break or the identity σ_new = S1's output. So OPT-ONLY HOLDS for N5-LZC (given
  LZ-OPT), and LZ-NOSIL holds outright, not only under the assumption. (A finding for the lane: the label can be discharged by citing this.)
- The N5 part (§1-§6) never uses OPT-ONLY, LZ-OPT or any §7 statement ✓.

## 8. Notes
- WCH-N1 (quotes): four [Q SPEC:…] line tags are one line low at aefb71a3 (text verbatim). Fix the tags, or quote at 7039eb524 (where
  R90's packet quotes them at l. 28-32). Add a quote check to «box 79».
- WCH-N2 (wording): TIE (a2)/(a3) and RET-WCH (ii)/(iii): state the split as "v reached after / before π's cycle node" (see §3-4).
- WCH-N3 (finding): OPT-ONLY is true (§7); LZ-NOSIL can be stated without the assumption.
- WCH-N4 (data): NC_R = NT_R = 0 on my whole corpus, so SIL-Z (b)'s own-Ξ-cycle exclusion (MUT 5) and the NT term are never exercised; the
  premises are used by the proofs (V1 at j − 1; W_j = W*_j) but not exhibited.

## 9. Pinned checks and own control
- Pinned: experiments/new/check.sh l. 400-405 («box 79») in a clean `git worktree add --detach` at 2ad78f51: PASS, exit 0. It covers RET-WCH on
  tog6b_n32 (N5: returns 4, paid-W 3, TT 1, TIE 2; N5-LZC: returns 3, paid-W 3, TIE 0) and symtest.py PASS.
- Own control: docs/referee/scratch/wch_probe.py on rl_engine (no lane code); N5-LZC built by replacing one line of rl_engine.run (S4a's
  σ_new → the §7.1 keep-rule, with an LZ-OPT check at every S4a computation). tog6b_n32 (S3): N5 returns 4, W-paid 3, TT 1, TIE events 2;
  N5-LZC returns 3, TT 0, TIE 0: the lane's pins, independently.
- Corpus: the lane's sbcg.lst ∪ alt_all (719 distinct games; given start and S3; n ≤ 80, 84 larger skipped), 722 runs, 12,087 transitions.
  N5: 0 violations of TIE (260 W-flat switches), NEW-BOUND, RET-WCH (2,656 returns: 2,612 W-paid in [k, u], 44 TT), RUN-WCH, REP-WCH (15 REPEATs),
  SIL-Z (a)-(c) and SC-GXC (42 class-S re-entries = the lane's / R90's 42; all GXC events; NC 0, NT 0), GXC-CLOSE (CL 1,813), GXC-SPLIT (GXC
  2,222), LEVEL-MON (190,139 segment checks), DROP-PAID (3,303 drops), FBO-R56, FBO-SPLIT (FBO 211, FBOS 178), ZF-SPLIT (ZF 90 = NZ 42 + ZFS 39 +
  drops), GAP-RED (783 in-phase fallbacks).
  N5-LZC: LZ-OPT exact at all 11,456 S4a computations, LZ-STRICT 0 violations, TIE = TT = 0, RET-WCH 2,552 returns all W-paid, class-S
  re-entries 0 (LZ-NOSIL), 0 violations.
- MUTs: 1 (RET-WCH without TT) BITES, 43; 2 (GXC-SPLIT without TIE) BITES, 17; 3 (LEVEL-MON across W(v)-changing S4a steps) BITES, 1,176;
  4 (ZF-SPLIT without DROP) BITES, 3; 5 (SIL-Z (b) at own-Ξ-cycle v) never (NC = 0: WCH-N4).

## 10. My strict symbol test of the line (9ac6fdba)
Every symbol found bound in the line or by a cited landed item: N5 / SPEC S1-S5 (Ξ_σ, σ̄, "more relevant", S4a, S4c, [S1-val]); R57 premise; H_t;
σ_t, τ_t (the run); ⊴ ◁ ⊵ ▷; Iσ_t; n, n_E, m_E, d_E(e); t → t + 1; "switched"; Ξ_t, λ_Ξ; "own Ω-cycle node" (Ω ∈ {Ξ_t, W_t, W′}); W_t, W(v), λ_W;
Z_t; τ-stretch, W-run, |F| (R89); phase, in-phase, f_P, ZF_P, WCH^S4a_P(v) (R38 (a), R91); λ-run (R86); S4a steps, boundaries, B_R, class-S
re-entries, SIL_R (R90 (e)); late adoption, REPEAT, REP_F, REP* (R88 (f), R90 (g)); ρ_P (R56); σ⁺, W′, d, ⊕ (with c, Q, ℓ); returns (u), WCH_F(e),
TT_F(v, e) (k); TIE_F, TIE_P, TIE*; GXC event, GXC_X (X ∈ {R, P}); NC_R, NT_R (j); a (first state of P); FBO_P; LEV_t(v) and the coordinate
sequence; DROP_P(v); FBOS_P; NZ_P (k); ZFS_P; S, e, w(n), [P-WCHτ](w); σ*, σ′, W* (N5-LZC); ASSUMPTION OPT-ONLY. The item labels R90 (a)-(e),
(g) and R91 (a)-(c), (h), (i), (k), (m) all exist in the landed entries (checked). No free symbol. The lane's symtest.py (182 symbols, 0
failures) agrees.
- Precision (not required): NZ_P uses «at k or k + 1» with k bound only through ZF_P's gloss («those k → k + 1 with Z_{k+1} = Z_k»); it
  reads correctly.
Verdict on the line (Opus 5.5, D15): MATCHES §2-§7, claims nothing more, every symbol bound.

## DONE / FINDINGS / NEEDS
- DONE: this report; scratch/wch_probe.py, wch_logs/.
- FINDINGS: every PROVED item SIGNED; no gap; the three watch items hold (RET-WCH's tie-leave and cycle-node cases; REP-WCH without FW-R*′; SIL-Z
  from landed R90 only); OPT-ONLY is true and unused by N5; line MATCHES; notes WCH-N1 (quote tags off by one), WCH-N2 (case wording), WCH-N3 (OPT-ONLY true), WCH-N4 (NC, NT not exhibited).
- NEEDS: Lead: route WCH-N1..N4 to L-NEW; the §C word after REFEREE-2 22.
