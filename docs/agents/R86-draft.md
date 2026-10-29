# Draft RESULTS R86 (Lead, 2026-10-29 14:00Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C95 (Lead reviewed 14:09Z by date -u: subagent draft; placements accepted (F2, F3 required fixes in the signed wording as in R85 [superseded at C95: F2's general form is Referee strengthening (0)]; λ-run MATCH-Φ signed inside §6 where both cells carry it; REFEREE C5 recorded); title parenthesis balanced) (rev. 14:30Z by date -u: fixes pin updated to l-si e7c7dd78, sha1 b4c69e11, 164 lines (F11 +3 lines: the Lead's D2/D3 ruling)) (rev. 14:58Z by date -u: C95 E-1 moves 1-4 and E-2 applied verbatim from C95 §3-§4; §5 replacements 1-5 applied; N-1..N-3 not applied) (rev. 15:12Z by date -u: C95 N-4 applied verbatim: title "dually for Odd's switches with λ^U constant" → "dually for Odd's switches in every λ^U-run") — LANDED in RESULTS Results 2026-10-29 15:26Z (CHECKER C95 Add. 2 79f2ba92 PASS), after R85

### R86 [refereed-only] N5 on EVERY game: with λ (λ^U) the cycle-node map of Even's valuation Ξ (Odd's valuation U of τ on G^d), a λ-run (λ^U-run) a maximal run of states with λ (λ^U) constant, and, for a stretch R of consecutive states of one run, ENT_R(v, c) the transitions of R at which v's strategy enters c, SW_R(v) := Σ_c ENT_R(v, c) the switches of v, RISE_R(c) the transitions of R at which Ξ(c) changes and PCH_R(c) those at which c's path set P(Ξ c) changes: ENT_R(v, c) ≤ 1 + RISE_R(c) on every stretch, for every Even v and vertex c (Lemma SW-RETURN; dually for Odd v with U on G^d); RISE_R(c) ≤ PCH_R(c) + (PCH_R(c) + 1)(n − 1) on every λ-run R and on every phase R = 𝒫 (Lemma LEN-MONO; dually on λ^U-runs with λ^U); so on every λ-run R Σ_v SW_R(v) ≤ Σ_{(v, c) ∈ E, v Even, SW_R(v) > 0} (1 + RISE_R(c)) ≤ Σ_{(v, c)} n·(PCH_R(c) + 1) ≤ m_E·n·(P*_R + 1), P*_R := max_c PCH_R(c), and a phase 𝒫 has |𝒫| ≤ Σ_v SW_𝒫(v) ≤ the same sums over 𝒫, |𝒫| := the number of transitions t → t + 1 with t, t + 1 ∈ 𝒫 (Theorem COMPOSE; dually for Odd's switches in every λ^U-run); hence every N5 run on every game has T ≤ 2n(n − 1) + (n(n − 1) + 1)·n·(m_E(P* + 1) + m_O(P*^U + 1)) transitions (iterations), P* (P*^U) the most path-set changes of one vertex's Ξ (U) inside one λ-run (λ^U-run) and m_E (m_O) the number of edges leaving Even (Odd) vertices (Corollary COMPOSE-RUN, via RESULTS R47 (a)'s every-game count: at most n(n − 1) transitions change λ and at most n(n − 1) change λ^U); and if MATCH-Φ's bound holds with "phase" replaced by "λ-run" ("λ^U-run" on G^d, read with G^d's parities), then P*_R ≤ (n²/2)(NM*_R + 1) + NM*_R, NM*_R the most carries of one vertex in R, and T is bounded by a polynomial in n, m and the largest carry count NM* = max(NM*_Even, NM*^U) (Corollary COMPOSE-NM, an implication), whose premise both referees sign as holding, with RESULTS R85's MATCH-Φ (landed at trunk 17f51175; CHECKER C94 Add. 2 PASS, b7461dd7), because MATCH-Φ's proof reads verbatim on every λ-run (λ^U-run on G^d), where c = λ(v) is fixed (2026-10-29) — a REDUCTION of N5's iteration count to per-vertex path-set changes P*, P*^U and, with MATCH-Φ, to carries NM*, NM*^U (none of which is bounded here; carries of one vertex reach Θ(N²) per phase, and through the dual mirror per λ^U-run, on L-RED's families, DATA only; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C95.md, checker PENDING)
- Object (L-SI successor 24, Opus 5.5, D18, Lead reading L40; frozen, unchanged during review): packet P-N5-COMPOSE,
  docs/si/P-N5-COMPOSE-box28.md, sha1 e1b977aa9cf1583d5e0c442a8f87d024230b6524, 141 lines (l-si freeze
  3ca0932d44c407fed38e5fb930744d7107ee79c8, 2026-10-29T11:34:00Z; quote bases b025560c9 (SPEC, RESULTS) and a23179b01 (P-N5-MPGS);
  16 quotes, experiments/si/rund/quotecheck.py, sha1 29bb4a971680c9278f5f8c6f40eac17c0134db72, "quotes=16 bad=0", pinned in
  experiments/si/check.sh with a shifted-line control (--mut: "quotes=16 bad=16", "QUOTES FAIL"); the packet sha1 is pinned in check.sh;
  both referees measured the packet sha1 and the pins): §1 setting with (F-SW) and (F-MON), §2 Lemma SW-RETURN, §3 Lemma LEN-MONO, §4
  Theorem COMPOSE, §5 Corollary COMPOSE-RUN, §6 Corollary COMPOSE-NM (the implication), §7 DATA. The referees' notes are collected by the
  lane in docs/si/P-N5-COMPOSE-fixes-box28.md (F1-F10: L-SI successor 25, l-si 45778960, sha1 3d63f0ab there; F11-F14 appended by L-SI
  successor 26 at l-si 4e928f11aeed2bb38954efa785ef6b93989b3cdf, 2026-10-29T13:36:48Z, append-only (git diff 45778960 4e928f11: 55 lines
  added, 0 removed; then e7c7dd78, 2026-10-29T14:17:47Z, +3 lines in F11 recording the Lead's 13:43Z ruling "D2 … and D3 … are REQUIRED
  appended items, the conservative reading", no statement change); at e7c7dd78 and on trunk sha1 b4c69e110d3c57eae73697d36729134f60ab5ea1,
  164 lines; 19 quotes checked by
  docs/si/P-N5-COMPOSE-fixes-quotecheck.py, sha1 45ff072708e4bd78591174fc556ea19040496470, "quotes=19 bad=0", a mutated quote caught in
  check.sh). The fixes file: "This file changes NO signed statement and NO proof step; every F-item below is APPENDED text that is read
  together with the packet". F1 and F11 define |𝒫| as the number of transitions (COMP-E1, E-item of both referees); F2 reads LEN-MONO and
  Theorem COMPOSE's first statement on any stretch with λ (λ^U) constant (N-C2 = REFEREE-2 §C D2); F3 reads Odd's side of §6 with G^d's
  parities (N-C3 = D3); the Lead ruled D2, D3 required ("Ruling: D2, D3 REQUIRED (already appended as fixes F2, F3)", 13:48Z). F4
  defines P*^U for the title, F5 says RISE counts changes, F6 spells out (F-MON)'s set I (optional: COMP-N1..N3 = D4-D6); F7 and F12
  record [MΦ]'s status, F8 the [MΦ] quote form (N-C1), F9 and F14 data figures, F10 (F-MON) on Odd's side, F13 REFEREE §C C11 = REFEREE-2
  §C D11 as OPEN: each a "No change, because" clause. The statements below are in the frozen wording with F1/F11, F2 and F3.
  Setting (every game): N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) with FIX 1-4; G any parity game, n = |V|; a run is the sequence of
  states (σ_t, τ_t), t = 0, …, T, a TRANSITION is t → t + 1; m_E (m_O) the number of edges leaving Even (Odd) vertices. Ξ_t := Ξ_{σ_t},
  S1's valuation (c, P, ℓ) against Odd's optimal counterstrategy, a function of σ_t only (R15 (d)); λ_t(v) its cycle node; U_t := Odd's
  valuation of τ_t on the dual game G^d (R47's setting), λ^U_t its cycle node. A λ-RUN: a maximal run of consecutive states with λ_t
  constant (τ free); a λ^U-RUN likewise; a PHASE: a maximal run with (λ_t, τ_t) constant (RESULTS R38 (a)), which lies inside one λ-run.
  For a stretch R (consecutive states of one run) and vertices v, c: ENT_R(v, c) := #{t : t, t + 1 ∈ R, σ_t(v) ≠ c = σ_{t+1}(v)} (Even
  v; τ for Odd v), SW_R(v) := Σ_c ENT_R(v, c); RISE_R(c) := #{t : t, t + 1 ∈ R, Ξ_{t+1}(c) ≠ Ξ_t(c)}; PCH_R(c) := #{t : t, t + 1 ∈ R,
  P(Ξ_{t+1} c) ≠ P(Ξ_t c)}; RISE^U, PCH^U the same with U_t on G^d; P*_R := max_c PCH_R(c), P* := max over λ-runs R of P*_R, P*^U likewise
  over λ^U-runs. F11: "|𝒫| := number of transitions t → t + 1 with t, t + 1 ∈ 𝒫." F1: for any stretch R, "|R| := #{t : t, t + 1 ∈ R},
  the number of TRANSITIONS inside R (one less than its number of states)", and "«transitions (iterations)» in Corollary COMPOSE-RUN count
  transitions". (F-SW): every Even switch goes along an edge of Iσ_t (S4a, S4c), every Odd switch along Iτ_t (S4b, S4c). (F-MON): Ξ_{t+1}
  ⊵ Ξ_t at every vertex and every transition (R15 (a) with (d)); dually U_{t+1} ⊵ U_t in G^d's order. §1 cells: REFEREE "CHECKED (F-SW
  and F-MON are correct consequences of S4a-c, [STEP], [MON]; |𝒫| is not defined: COMP-E1)"; REFEREE-2 "SIGNED (well formed; F-SW and
  F-MON proved correctly from [S4a-c], [STEP], [MON])".
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 18, REFEREE-2 successor 20). Each item below is SIGNED in both verdict
  tables (REFEREE "## Verdicts", l. 13-22 of R-N5-COMPOSE.md; REFEREE-2 "## 0. Verdicts", l. 27-36 of R2-N5-COMPOSE.md; REFEREE-2 §C
  C.1: "SIGNED by both" for §2-§6), in the frozen wording with the required appended text F1/F11, F2, F3. On every game; no item uses
  (P). Premises LANDED: SPEC S1 (valuation, order, Ξσ), S2, S4a-c (quote base b025560c9); RESULTS R15 (a) Lemma A ([MON]) and (d)
  ([STEP]); RESULTS R47 (a) Lemma Φ (every game), item (c) only ([Φ]); RESULTS R84 (a) Fact DELTA; RESULTS R38 (a), as the phase
  definition only. Premise for (e) only: RESULTS R85 (A) (P-N5-MPGS; landed at trunk 17f51175,
  2026-10-29T14:02:36Z, CHECKER C94 Add. 1 7e309075; landed check C94 Add. 2 PASS, b7461dd7).
  (a) Lemma SW-RETURN (§2): "For every run of states R of an N5 run, every Even v and every vertex c: ENT_R(v, c) ≤ 1 + RISE_R(c).
      Dually for Odd v with U." (Ξ-SUCC: Ξ_t(σ_t v) is non-decreasing in t, by (F-MON), (F-SW) and [S2]. For consecutive entries e < e′
      of v into c and the step s ∈ [e + 1, e′ − 1] at which v leaves c: Ξ_{e′}(c) ▷ Ξ_{e′}(σ_{e′} v) ⊵ Ξ_{s+1}(σ_{s+1} v) ⊵ Ξ_s(σ_{s+1}
      v) ▷ Ξ_s(c) ⊵ Ξ_{e+1}(c), so Ξ(c) changes at a transition in [e + 1, e′ − 1] ⊆ R; these windows are disjoint.) Cells: REFEREE
      "SIGNED", REFEREE-2 "SIGNED"; REFEREE §2: "No phase, no λ, no τ used: it holds on ANY stretch of consecutive states, fallbacks
      included."
  (b) Lemma LEN-MONO (§3) on every λ-run and, with F2, on every phase 𝒫 (a stretch inside one λ-run, RISE_𝒫 and PCH_𝒫 counted inside 𝒫): "For every λ-run R and every vertex c: RISE_R(c) ≤ PCH_R(c) + (PCH_R(c) + 1)(n − 1). Dually for
      λ^U-runs with U.", F2 appended: "In Lemma LEN-MONO and in Theorem COMPOSE's first statement, "every λ-run R" is to be read as
      "every stretch R of consecutive states on which λ is constant" (dually λ^U); a λ-run and a phase are such stretches." Signed here for λ-runs and phases only; F2's reading for every stretch with λ constant: Referee strengthening (0). (On R the
      cycle node c₀ of Ξ_t(c) is fixed; by (F-MON) and [S1-ord] the weight of P never falls and rises strictly at a P-change ([DELTA]),
      so the P-values form PCH_R(c) + 1 contiguous blocks; inside a block only ℓ changes, strictly in the direction [S1-ord] prefers for
      Ω(c₀), and ℓ ∈ {0, …, n − 1}; so RISE_R(c) ≤ n·PCH_R(c) + n − 1.) Cells: REFEREE "SIGNED" (row "Lemma LEN-MONO (any λ-run /
      λ^U-run)"); REFEREE-2 "SIGNED (it holds on any stretch with λ constant: N-C2)". The stretch reading, for the phase: REFEREE
      §4, inside its signed phase part: "a phase lies inside one λ-run, so LEN-MONO applies to it (cycle nodes fixed)"; REFEREE §C
      C3: "I agree: the proof never uses maximality" (classed "optional (wording; one word)"); REFEREE-2 §C D2: "Applying the λ-run
      bound to the enclosing λ-run would give PCH_R, not PCH_𝒫, so the phase statement needs the stretch form".
  (c) Theorem COMPOSE (§4), with F1/F11, and F2 for the phase statement: "For every λ-run R of an N5 run on any game, the Even switches inside R satisfy Σ_v
      SW_R(v) ≤ Σ_{(v, c) ∈ E, owner(v) = Even, SW_R(v) > 0} (1 + RISE_R(c)) ≤ Σ_{(v, c)} n·(PCH_R(c) + 1) ≤ m_E·n·(P*_R + 1). For every
      phase 𝒫 (inside a λ-run R): |𝒫| ≤ Σ_v SW_𝒫(v) ≤ the same sums with R replaced by 𝒫. Dually for Odd's switches in a λ^U-run.";
      F2: "Theorem COMPOSE's phase statement is the first statement applied to the stretch 𝒫, with RISE_𝒫, PCH_𝒫 counted inside 𝒫."
      (SW_R(v) = Σ_{c ∈ succ(v)} ENT_R(v, c), then SW-RETURN, then LEN-MONO, summed over the Even v that switch; in a phase τ is constant,
      so by [STEP] every transition of 𝒫 changes σ, i.e. contains an Even switch.) Cells: REFEREE "SIGNED, with |𝒫| read as the number of
      transitions inside 𝒫 (COMP-E1: under the "number of states" reading the phase part is FALSE)"; REFEREE-2 "SIGNED"; REFEREE-2 §C
      C.1: "SIGNED by both, with COMP-E1". (REFEREE §1: read as states, "a one-state phase gives 1 ≤ 0".)
  (d) Corollary COMPOSE-RUN (§5): "Every N5 run on every game has T ≤ 2n(n − 1) + Σ_{λ-runs R} Σ_v SW_R(v) + Σ_{λ^U-runs R′} Σ_{Odd
      v} SW_{R′}(v) ≤ 2n(n − 1) + (n(n − 1) + 1)·n·(m_E·(P* + 1) + m_O·(P*^U + 1)) transitions (iterations)." (Classify each transition,
      S4c fallbacks included, by the first of (i) λ changes, (ii) σ changes, (iii) λ^U changes, (iv) otherwise, when τ changes by [STEP];
      a kind-(ii) transition holds an Even switch of one λ-run, a kind-(iv) one an Odd switch of one λ^U-run; [Φ] (c), RESULTS R47 (a)
      Lemma Φ (every game): "along a run at most n(n − 1) transitions change λ and at most n(n − 1) change λ^U", read separately for each
      map, so at most n(n − 1) + 1 λ-runs and as many λ^U-runs; Theorem COMPOSE on each. Not used: R47's joint count, Corollary Φ-1O,
      R48. Fallbacks: an Even fallback is kind (i) or (ii), an Odd fallback kind (iii) or (iv); "No transition is uncharged".) Cells:
      REFEREE "SIGNED" (row "Corollary COMPOSE-RUN (every run, every game), including the classification and the fallback paragraph");
      REFEREE-2 "SIGNED (Lead's points (1) and (2) checked: §2.4)" (row "Corollary COMPOSE-RUN: T ≤ 2n(n−1) +
      (n(n−1)+1)·n·(m_E(P*+1) + m_O(P*^U+1)), every run, every game").
  (e) Corollary COMPOSE-NM (§6), the implication, with F3: "If [MΦ] holds with "phase" replaced by "λ-run" (resp. "λ^U-run" on G^d),
      then P*_R ≤ (n²/2)(NM*_R + 1) + NM*_R with NM*_R the most carries of one vertex in R, and Corollary COMPOSE-RUN bounds T by a
      polynomial in n, m and the largest carry count NM* (over both players)."; F3 appended: "On Odd's side (λ^U-runs of U on G^d),
      P-changes, MATCHED, CARRY and the carry count NM^U are read on G^d, i.e. with G^d's parities (Ω + 1; the ranks are those of G). NM*
      in the Corollary is max(NM*_Even, NM*^U)." (K ≤ n − 1 gives K(K + 1)/2 ≤ n²/2.) [MΦ] is P-N5-MPGS (A)'s Corollary, the subject of
      RESULTS R85 (A): "PCH_𝒫(v) ≤ (K(K+1)/2)·(NM_𝒫(v) + 1) + NM_𝒫(v)", K the number of ranks above rank(λ(v)), NM_𝒫(v) v's carries.
      Its λ-run form, the implication's premise, sits in both verdict cells for §6: REFEREE "SIGNED as an implication; its premise
      "[MΦ] on λ-runs" HOLDS (§6 below: MΦ's proof reads verbatim with c fixed; my predecessor's R-N5-MPGS §1b agrees), so the
      conclusion holds with [MΦ] as signed by both referees"; REFEREE-2 "SIGNED as an implication. The "phase → λ-run" replacement is
      VALID (Lead's point (3), §2.5). Read NM^U with G^d's parities (N-C3)". The λ^U-run side: REFEREE's cell names λ-runs; its §6,
      which the cell cites: "on λ^U-runs it holds for U on G^d (G^d is a game with the same ranks; MATCHED is then read with G^d's
      parities)"; REFEREE-2 §2.5: "MATCH-Φ's proof holds for every parity pattern, so the bound holds (N-C3)". Hence, with RESULTS R85's
      MATCH-Φ (landed at 17f51175, landed check PASS b7461dd7): P*_R ≤ (n²/2)(NM*_R + 1) + NM*_R on every λ-run R (and on every λ^U-run,
      NM^U read on G^d), and T is bounded by a polynomial in n, m and NM*. This is the λ-run form that RESULTS R85 carries as Referee
      strengthening (0), "To be signed with P-N5-COMPOSE, which uses it" (CHECKER C94 §3).
- Not signed: §7 (DATA; REFEREE "DATA, not signed; reproduced EXACTLY (below)", REFEREE-2 "DATA, not signed. Reproduced EXACTLY
  (§3.1)") and its "Slack (READING)". The packet's own label of §6, "PROVED from an ASSUMED premise (sign only the implication)", and its
  "Note for the referees", which calls the λ-run replacement "a reading of [MΦ]'s proof, to be confirmed by its referees": confirmed in
  both §6 cells (item (e)); the premise itself is R85's, not this entry's. LEN-MONO across a λ-change: not claimed; whether the
  restriction is needed is OPEN (F13; "Honest limits" (iii)). The fixes file's records F7, F12 ("[MΦ] is signed by both referees";
  "When P-N5-MPGS lands, §6's premise is that entry plus this referees' remark") and F9, F13, F14: lane records ("This file is a lane
  record, not refereed text"). F4-F6 (optional wording): bullet "Referee strengthening" (i), (ii).
- Referee strengthening (NOT part of this entry; remarks of one or both referees outside the verdict cells, or optional wording):
  (0) F2's general reading (N-C2 = REFEREE-2 §C D2; the Lead ruled D2 required as appended text, 13:43Z): LEN-MONO and Theorem
  COMPOSE's first statement on every stretch of consecutive states with λ (λ^U) constant. REFEREE-2 §3 cell: "SIGNED (it holds on any
  stretch with λ constant: N-C2)"; REFEREE: its §3 row signs "any λ-run / λ^U-run", its §4 applies the Lemma to a phase ("a phase lies
  inside one λ-run, so LEN-MONO applies to it (cycle nodes fixed)"), and its §C C3 "I agree: the proof never uses maximality", classed
  "optional (wording; one word)". Not used by any signed item beyond λ-runs and phases.
  (i) COMP-N2 = D5 (F5): RISE_R(c) counts changes of Ξ(c), and by (F-MON) every such change is a strict rise. REFEREE §8: "COMP-N2:
  SW-RETURN's RISE_R(c) counts CHANGES of Ξ(c); by F-MON they are rises."; REFEREE-2 §C D5: "Agreed" (class "opt"). The signed items
  count changes (≠), as defined. (ii) COMP-N3 = D6 (F6): (F-MON)'s set is I := {(v, σ_{t+1}(v)) : σ_{t+1}(v) ≠ σ_t(v)} ⊆ Iσ_t by (F-SW);
  REFEREE-2 §C D6: "Agreed; my §2.0 used exactly this I" (opt); COMP-N6 = D9 (F10): "F-MON on the Odd side is [MON] applied to G^d, as in
  R47's Lemma Φ (b) citation chain (PHI-N1 = N-PHI-2); no new premise." (both: REFEREE-2 §C D9 "Same"). (iii) The classification by what
  changes (REFEREE §5, a remark on the fallback paragraph): "A transition where S4a runs but leaves σ unchanged and S4b changes τ is (i),
  (iii) or (iv): the classification is by what changes, not by which step ran, so it is covered." The packet's sentence "A transition
  applying S4a and S4b together is charged to its Even switch (kind (ii)) unless λ changes" presumes σ changes; REFEREE-2 §2.4: "S4a + S4b
  together is kind (i) or (ii)". No gap: the proof classifies by what changes. (iv) REFEREE §5 on [Φ] (c): "Its content is elementary
  from (a), (b): reward is injective, so each vertex's λ changes ≤ n − 1 times, and each λ-changing transition changes some vertex."
  (v) COMP-N4 = D7, C5 (F7, F12): REFEREE §8: "the λ-run reading of [MΦ] is now confirmed by the first referee twice (R-N5-MPGS §1b, here
  §6); it can be stated as a remark of the landed MPGS entry rather than an assumption."; REFEREE §C C5 (1680010b): "§6 can land as
  "COMPOSE-RUN with [MΦ] (citing the landed MPGS entry) gives …", the λ-run transfer as a referees' remark."; REFEREE-2 §C D7: "Agreed.
  It is now confirmed by both referees (R2-N5-MPGS-C, "§1b AGREED"), so the packet's ASSUMED label on [MΦ] is resolved once MPGS lands"
  (opt). Status: this entry states the λ-run form inside item (e) because both §6 verdict cells carry it; R85 as landed carries it as Referee strengthening (0), "To be signed with P-N5-COMPOSE, which uses it"; this entry signs it (item (e)).
- Honest limits: (i) COMPOSE is a REDUCTION of N5's total iterations to P*, P*^U and, with R85's MATCH-Φ, to the carries NM*, NM*^U.
  None of them is bounded here (packet SCOPE: "P* and the carry counts are NOT bounded here"; REFEREE: "Nothing here bounds P* or NM*").
  The bound is polynomial in n, m and P* (or NM*), and P* is not bounded. NM* and NM*^U are OPEN. DATA only, not refereed: L-RED's R109
  (claude/l-red e5c9b628, docs/red/R109-hn-topgate.md §5; L-COMP's nm.py unmodified, phases keyed by r38 = (λ_Ξ, τ)): carries of one
  vertex in one phase reach max NM 343 (max PCH 354) on topfix n 12 (N 252 vertices), NM / N 1.361, "max NM = 2n² + 5n − 5", "Carries of
  ONE vertex in ONE phase are Θ(N²) on this family"; there "NM*^U = 0 exactly" (τ never changes). L-RED's R111 (claude/l-red 463bec6e,
  1811cae2, docs/red/R111-dual-tau-runs.md): on G^d N5's run is the mirror of the run on G (DATA, two pins: "σ_G = τ_{G^d} and τ_G =
  σ_{G^d} at EVERY state"); 264 τ-changes inside one joint λ-run (dual runquad_K8_m30); NM^U = 163 = 2n² + 5n − 5 per vertex per λ-run
  on dual hntop_n8 is a READING through the mirror ("Not measured directly: nm.py is Even-side only"); "Both are polynomial". (ii) T
  counts iterations (transitions), not bit operations; nothing here bounds N5's running time. (iii) OPEN (F13): whether LEN-MONO's
  restriction to stretches with λ constant is needed. REFEREE §C C11: "OPEN in data, not a finding (the proof uses it; LEN-MONO across a
  λ-change compares different cycle nodes)"; REFEREE-2 §3.2: "X_LENfull (LEN-MONO across λ-changes) never bit"; REFEREE-2 §C D11:
  "neither shows the λ restriction of LEN-MONO is needed". The restriction of the phase bound to phases is needed (REFEREE MUT 4: 423
  violations on whole λ-runs), and so are SW-RETURN's "+1" and LEN-MONO's length term (MUT 1, MUT 3; REFEREE-2 X_SWR0, X_LEN0). (iv)
  Slack (READING, packet §7 and COMP-N5): "the factor n of LEN-MONO and MΦ's n²/2 are the loose links". (v) Not M3, not a step-4 pass,
  not a TARGET.md claim; G-N5-TIME stays open. Item (e)'s conclusion rests on R85 (A) (landed at 17f51175, landed check PASS b7461dd7).
- Data (DATA, not proof): pinned (packet §7; experiments/si/chg/compose.py, sha1 9fc3b081bff815a72597a394af918786e3d6f2ec, check.sh box
  28 §9), run as `python3 -I` from experiments/si: runquad_K8_m30_n192 "TOP (263, 'chg/instances/red/runquad_K8_m30_n192.pg', 0, 263,
  481, 1016, 195072, 265890048, 8, 15, 15, 15, 192)" (L = 263 ≤ S1 = 481 ≤ S2 = 1,016 ≤ S3 = 195,072 ≤ S4; max NM 8, max PCH = max
  RISE = max SW = 15; n = 192; instance sha1 ebaa6ac57ec60948fb986210c27479cb3a7961d9, L-RED's R106 pin), I0 I1 LDIR LBLK I2 I3 PASS;
  dlsep_kill_n70 "TOP (12, 'chg/instances/dlsep_kill_n70.pg', 0, 12, 39, 387, 26810, 14059640, 5, 6, 7, 4, 70)" (sha1
  e500ea47e1dc0163b32a97042ff9752daf6db83a), the same six PASS; MODE=run seglast_kill_n110 "TOP (16, 'lay/instances/seglast_kill_n110.pg',
  0, 16, 27, 152, 16066, 0, 20, 1, 4, 2, 110)" (T = 16 ≤ 20 Even + 1 Odd in-run switches + 4 λ- and 2 λ^U-changes = 27), RUNI0 R47 EI1 OI1
  ELDIR OLDIR ELBLK OLBLK PASS, also on segcount_kill_n20. Re-run for this draft on trunk 764101b1 (compose.py sha1 as above; rund/,
  lay/ and root/ tree ids equal to 3ca0932d's, chg/ only 16 added files): the three TOP lines identical, every PASS line as listed;
  quote checks: packet "quotes=16 bad=0" (--mut "quotes=16 bad=16", "QUOTES FAIL"), fixes "quotes=19 bad=0" (mutated: "quotes=19
  bad=1"). Packet corpora (chg/compose_*.txt, chg/composerun_*.txt): every inequality on all phases of alt_all pinned starts (457), lib41
  (418), all experiments/si instances (345) and all runs (413, 412, 276); per vertex per phase NM 42 and PCH 71 at most, at n 41
  (l121reader_n41); at most 31 λ-runs and 28 λ^U-runs in one run; L-RED's R106 mkr.py families NM = K, PCH = 2K − 1; ladderd0_k48_n156
  NM 0, PCH 48. REFEREE (successor 18; own scratch/compose_probe.py, sha1 239d122e…, on its engine rl_engine; no lane code; pinned
  re-runs in a worktree at 3ca0932d, exact): library (n ≤ 64) 763 runs, 12,426 transitions, SW-RETURN checks 87,161 (strong form 7,057),
  LEN-MONO 129,260, kinds (i)/(ii)/(iii)/(iv) 2,101 / 9,964 / 238 / 123; lane pins 15, 512, 2,468 (610), 8,818, 43 / 463 / 5 / 1; random
  rand_ck n 5-16 6,000, 10,171, 82,509 (20), 232,299, 5,878 / 2,262 / 1,471 / 560; random n 6-16 with MPHI 4,000 runs; 0 violations; at
  most 29 λ-runs and 14 λ^U-runs in one run (library); [MΦ] on every λ-run of both players: library 294 games, 29,931 (Even) + 12,222
  (Odd, on G^d) (vertex, λ-run) checks, random 4,000 runs, 94,226 + 71,142, 0 failures, max NM 15; MUT 1 14,867, MUT 2 3, MUT 3 3,144,
  MUT 4 423 violations (all bite); a batch rand n 16-30 stopped unfinished (recorded). REFEREE-2 (successor 20; own
  R2-N5-COMPOSE/compose_check.py on its lane's dual_check.Runner and si.py, MATCHED test mphi_check.matched; lane code only run as the
  pinned re-runs, exact): 14,428 runs, 40,406 transitions, SWR checks 523,231 / 319,059 (Even / Odd), LEN 551,515 / 440,798, CMP 31,125
  / 26,918, 2,840 phases, 0 violations of FSW, FMON, SWR, LEN, LENB, LEND, CMP, RUN, NM; kinds 13,857 / 19,061 / 5,104 / 2,384; at most 29
  λ-runs and 32 λ^U-runs in one run (lib41); [MΦ] on 56,999 Even and 21,286 Odd (vertex, λ-run) pairs, max NM 62 / PCH 67 (alt_all) and
  42 / 71 (l121reader_n41); controls X_SWR0 "233,008 (stretch, v, c) checks", X_LEN0 "42,128 (λ-run, c) checks", X_RUN0 "bites at 8,597
  runs", X_LENfull never bit; strict quote check 15/16 (the miss is [MΦ]'s joined quote, N-C1; F8), SHIFT=1 control 0/16; max S1/S2 0.8.
  Run counts: REFEREE's §C says "mine 6,778 runs", REFEREE-2's §C D12 "REFEREE: 10,778 runs (763 library + 15 pins + 6,000 + 4,000
  random)"; F14 (lane reading) puts the difference at REFEREE's 4,000 MPHI runs; not reconciled by REFEREE. No signed statement uses any
  count.
- Signatures: REFEREE docs/referee/R-N5-COMPOSE.md (report 4896bc2e, 2026-10-29T12:51:21Z, sha1 3c29700d886cf1604fd49e19f2ab071ecca0d404
  there; §C c6011b70, 13:09:45Z, sha1 25b431846675f10883d3831acd5abd38de5ddbee there; §C wording 1680010b, 13:17:12Z, sha1
  5f7fa31269f160a3bf76f1ba6eed5af7aab12d03 there, = claude/referee head and trunk; successor 18; append-only after 4896bc2e): §1 CHECKED;
  §2 SW-RETURN SIGNED; §3 LEN-MONO SIGNED; §4 Theorem COMPOSE SIGNED with |𝒫| as transitions; §5 COMPOSE-RUN SIGNED; §6 COMPOSE-NM
  SIGNED as an implication, premise on λ-runs HOLDS; §7 DATA, reproduced exactly; quotes "quotes=16 bad=0"; E-item COMP-E1; notes
  COMP-N1..N6; "No gap in the mathematics." REFEREE-2 docs/referee-2/R2-N5-COMPOSE.md (report 4b8afa95, 2026-10-29T11:59:33Z, sha1
  3bc4f67cf8536f82c2c48e114c1e091cbd6a85db there; §C appended ee549524, 13:10:01Z, sha1 8a04defa57089c9eb271e77a22fa1df15b69a726 there, =
  claude/referee-2 head and trunk; successor 20): §1 SIGNED; §2-§5 SIGNED; §6 SIGNED as an implication, λ-run replacement VALID; §7 DATA,
  reproduced exactly; "No gap. No item FALSE."; notes N-C1..N-C5. INDEPENDENCE: REFEREE: "14 names matching "compose" under
  docs/referee-2/, 12:40Z; names only", "None opened.", and it read REFEREE-2's report "only after this report was pushed (4896bc2e)";
  REFEREE-2's name count of COMPOSE files on origin/claude/referee was 0 at 11:54:22Z and 11:59:23Z, and it first opened REFEREE's
  report at 13:09Z, after 4b8afa95 was pushed ("Neither referee had read the other's report before writing its own."). No review
  imported lane code.
  §C (both): verdicts identical (REFEREE: "VERDICTS IDENTICAL: §2 SW-RETURN, §3 LEN-MONO, §4 Theorem COMPOSE, §5 COMPOSE-RUN SIGNED by both;
  §6 COMPOSE-NM SIGNED as an implication by both"; REFEREE-2 C.1: "SIGNED by both" for §2-§6); joint gap map empty (REFEREE "JOINT GAP
  MAP: EMPTY. ONE E-ITEM: COMP-E1"; REFEREE-2 "Joint gap map: no mathematical gap."); COMP-E1 agreed as the E-item by both (REFEREE-2 §C
  C.2: "AGREED, it is an E-item"), done as F1 and F11; REFEREE §C C1-C11 classes C3 = N-C2 and C4 = N-C3 "optional", REFEREE-2 §C C.3
  classes D2 = N-C2 and D3 = N-C3 as E; the Lead ruled them required (13:48Z), done as F2, F3; C.4 joint list items 1-4 answered in F1-F8;
  REFEREE: "Nothing open on COMPOSE beyond COMP-E1. P*, P*^U and NM* are not bounded; G-N5-TIME stays OPEN."
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a reduction of N5's iteration count on every game to per-vertex path-set
  changes P*, P*^U and, with MATCH-Φ, to carries NM*, NM*^U, which are not bounded; no running-time bound, no algorithm claim).
  GAPS G-N5-TIME: open.
