# Draft RESULTS R87 (Lead, 2026-10-29 17:34Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C96 (REVISED 18:02Z by date -u for C96 E-1, moves 1-3 applied verbatim (d65350f7 §3): output correctness is NOT claimed; the R57 (b) OUT-G note below is thereby answered in the entry. Earlier: Lead reviewed 17:41Z by date -u: subagent draft, sha1 2d0c8e0c before review; one change: the subagent's "Draft note" on
R57 (b) Lemma OUT-G moved out of the entry to this header, as a note to CHECKER only: OUT-G (landed) is stated for every σ with Iσ = ∅; R57's
"Not signed" (RESULTS l. 2932-2936) records the removal of G-N5T-3's output half as a Lead reading, not a signed statement; neither referee
nor the packet applies it to N5-SF's stop, so (C96 E-1, superseding the first version of this note) the entry claims no output correctness for N5-SF. Lead decisions for CHECKER to check:
the optional clause "(and SPEC S1 conformance, as R57 (b))" is a premise disclosure in the Premises line, not in the title; the title is
the approved line verbatim except its output-correctness status clause (C96 E-1 move 1) (ONE-PLAYER, signed by both, is in Claims signed, not in the title); no GAPS row changes (a variant result).)

### R87 [refereed-only] N5-SF (SPEC S1-S5 with S4a's opponent τ replaced by Odd's best reply σ̄(σ), S4b mirrored) terminates (Lemma SF-TERM; R15 (c), (d)); its sequence of distinct σ depends on σ_0 alone and that of τ on τ_0 alone (Lemma DECOUPLE); and its iteration count I satisfies SBC/2 ≤ I < (n + m + 1)(2(n² − n + 1) + SBC), SBC = the σ-changes at which σ̄(σ) changes plus the mirror (Theorem SF-RED; R15 (a), (c), (d), R17 (c), (e)): a reduction, polynomial iff SBC is (2026-10-29) — a REDUCTION for a VARIANT (N5-SF) of N5 (SBC is not bounded here; CONJECTURE SF-POLY (SBC polynomial) OPEN; output correctness not claimed (N5-SF stops, like N5, at a σ with Iσ = ∅, the hypothesis of RESULTS R57 (b) Lemma OUT-G; that application is not signed here); it says nothing about N5 itself; not M3, not a gauntlet pass, not a TARGET.md claim; G-N5-TIME untouched), CHECKER PASS (docs/checker/C96.md, checker PENDING)
- Object (L-NEW successor 33, Opus 5.5, D14/D18, Lead reading L40; frozen, unchanged during review): packet P-N5-SF,
  docs/new/P-N5-SF-box55.md, sha1 dbc2345f62454d442e951de025b1b2aef8a35317, 172 lines (l-new freeze
  95a7a581353157ebc13bd57ae1ffe318e3ba581d, 2026-10-29T15:46:10Z; `git diff 95a7a581 3d8b357d` on the file is empty; quote base trunk
  305cc8be (2026-10-29T15:12:21Z); 18 quotes, experiments/new/box49/quotecheck3.py, sha1 eaf184117e025caa94e06bcecf456b595dffc9d5,
  "quotes=18 bad=0", --mut "quotes=18 bad=18", "QUOTES FAIL"; the packet sha1 is pinned in experiments/new/check.sh block "Box 55"
  (l. 190-210 at trunk 3d8b357d); both referees measured the packet sha1 at 95a7a581): §0 definitions, §2 Lemma SF-TERM and Lemma
  DECOUPLE, §3 Lemma ONE-PLAYER and Theorem SF-RED (a)-(c), Remarks 1-2 (READING), §4 DATA and the pinned check, §5 not to sign. The
  RESULTS line is the packet's "Proposed RESULTS line (as sent to the Lead 15:27:39Z, verbatim)" (packet l. 14-18), approved by the
  Lead as the packet records it (l. 5: «Lead 15:39Z: «push. Your RESULTS line is approved as worded at 15:27:39Z.»»); the title above
  is that line, unchanged, with the date and the scope parenthesis. The referees' notes are answered by the lane in
  docs/new/P-N5-SF-fixes-box55.md (F1-F6: L-NEW successor 33, l-new 122c2f6866c21f46b10a9aad47b32c0a4d4bb7eb, 2026-10-29T16:22:01Z,
  sha1 b4534e02cb143add059e567b9a015d3ea020c7df there, 35 lines; F7-F13 appended at l-new e9daffde325fcf0fda0ef76f986e7a667a940ef6,
  2026-10-29T16:52:01Z, append-only (`git diff 122c2f68 e9daffde`: 52 lines added, 0 removed); at e9daffde and on trunk 3d8b357d sha1
  d937c8a9110297e961cc2fb9398631e7c41472ac, 87 lines; 6 quotes at trunk e251d147 (2026-10-29T16:39:24Z), checked by quotecheck3.py,
  "quotes=6 bad=0", --mut "quotes=6 bad=6", "QUOTES FAIL", pinned in check.sh block "P-N5-SF fixes file" (l. 232-238)). The fixes
  file: «Each item is a CLARIFICATION: no statement of the packet is widened or changed.» F1 and F7 name ONE-PLAYER (a)'s standing
  premises; F2 gives the τ-side mirror of ONE-PLAYER (b) (S1 on the dual of a G^d-arena is H′ with Ω + 2); F3 reads SF-RED (a)'s proof
  with "a prefix of a λ-phase"; F8 cites R17's source proof for "the S4c step changes no valuation"; F9 gives the full S4a quote
  (with «Else σ_new = σ»); F10 says "the same arena H" is the same graph with the same increasing-index lists; F6 reads "iff" in SF-RED
  (c); F4, F5, F11, F12 are DATA; F13 says the LAM argument is proved in place. The statements below are in the frozen wording, read
  with F3, F7, F8, F9 (and F2, F10 in the proofs).
  Setting (every game): G = (V, E, Ω, owner) as in SPEC (docs/new/N5-ssi-global.md), n := |V|, m := |E|; priorities made injective by
  p′ (S1). σ̄(σ) := Odd's optimal counterstrategy to σ computed by S1's procedure (a deterministic function of (G, σ)); Ξσ := the
  valuation of every vertex under (σ, σ̄(σ)) (S1); Iσ := Even's improving edges (S2); λ_Ξ(σ) := v ↦ the cycle node of Ξσ(v); mirror
  τ̄(τ), Ξτ, Iτ, λ_Ξ(τ) on G^d. N5-SF := SPEC S1-S5 with exactly two changes: S4a′ (in S4a's arena H every Odd v keeps only the edge to
  σ̄(σ)(v), not τ(v), and σ_new is S1's Odd optimum in the dual of H to σ̄(σ)), S4b′ (mirrored: every Even v of H′ keeps only τ̄(τ)(v));
  S4c (with FIX 3), S4d, S5 and the iteration count unchanged. A(σ) := S4a′'s σ_new (Iσ ≠ ∅); F(σ) := A(σ) if A(σ) ≠ σ, else σ with
  every Even v that has an improving edge switched to S4c's choice (argmax of (Ξσ(w), w) over (v, w) ∈ Iσ); F undefined when Iσ = ∅;
  F^d the mirror. The run: states (σ_k, τ_k), k = 0..I, I the number of iterations; the distinct-σ sequence σ^(0), …, σ^(p) (consecutive
  repetitions removed), #σ := p + 1; τ^(0), …, τ^(q), #τ := q + 1. G_σ̄ := G with every Odd v cut to the single edge (v, σ̄(v)), a
  one-player game in R17's sense. SBC_σ := #{j < p : σ̄(σ^(j+1)) ≠ σ̄(σ^(j))}; LAM_σ := #{j < p : λ_Ξ(σ^(j+1)) ≠ λ_Ξ(σ^(j))}; SBC_τ,
  LAM_τ the mirror (τ̄, G^d); SBC := SBC_σ + SBC_τ. A STRETCH: a maximal interval [a, b] of indices of the distinct-σ sequence on which
  σ̄(σ^(j)) and λ_Ξ(σ^(j)) are constant. §0 cells: REFEREE «CHECKED (well formed; S4a′/S4b′ are S4a/S4b with the opponent argument
  replaced, nothing else)» (l. 16); REFEREE-2 «SIGNED (well formed; F is a function of σ alone)» (l. 36); both §Cs: "same content"
  (REFEREE §C l. 13), "agreed" (REFEREE-2 §C l. 14).
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 18, REFEREE-2 successor 20). Each item below is SIGNED in both verdict
  tables (REFEREE "## Verdicts", l. 13-25 of R-N5-SF.md; REFEREE-2 "## 0. Verdicts", l. 33-46 of R2-N5-SF.md; REFEREE §C table l. 10-21
  "SIGNED" in the joint column; REFEREE-2 §C C.1 l. 11-24 "SIGNED by both"), in the frozen wording read with F3, F7, F8, F9. On every
  parity game; every start pair; no item is about N5's own run. Premises LANDED: SPEC S1 (injective priorities, order, Ξσ, Odd's side),
  S2, S4, S4a (packet quote l. 51-53 and its full form with «Else σ_new = σ», F9, at e251d147), S4c, FIX 3, S5 (quote base 305cc8be);
  RESULTS R15 (a), (c), (d); RESULTS R17 (c), (e), with R17's source proof for the flatness of the S4c step (F8:
  docs/new/N5-phase-bound-box10.md §3, Theorem PH proof, l. 69-72 at e251d147, «no valuation changes (every play that met x still meets
  x with the same path set)»). Standing premise of ONE-PLAYER (a), named by F1/F7 (disclosure, not a widening; both referees'
  optional clause "(and SPEC S1 conformance, as R57 (b))", REFEREE l. 23 and §5 l. 78, REFEREE-2 §C l. 21 and C.6 l. 112): (i) the
  code's match to SPEC, RESULTS R15 limit (ii) = G-N5T-1 (DATA); (ii) «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC
  conformance, and the code's match to SPEC is DATA (R15 G-N5T-1)» (RESULTS R57 (b), l. 2915-2916 at e251d147 and at 3d8b357d). F7:
  «It is NOT the VJ00 Lemma 5.8 / G-N5T-3 premise; SF-RED does not use output correctness.»
  (a) Lemma SF-TERM (§2, l. 77): "Every run of N5-SF stops, after I ≤ (#σ − 1) + (#τ − 1) iterations, at a state with Iσ = Iτ = ∅, and
      outputs S5's output." (Each σ-change is Switch_J(σ), ∅ ≠ J ⊆ Iσ, one edge per vertex (S4a′'s arena; S4a «Else σ_new = σ», F9;
      S4c's Even branch needs Iσ ≠ ∅); R15 (c): every such change goes strictly up in the strict partial order ≺, on G for σ and on G^d
      for τ, so no σ and no τ recurs; S4c makes every iteration change σ or τ; the loop exits only at S5.) «The CORRECTNESS of that
      output is not claimed here» (l. 88). Cells: REFEREE "SIGNED" (l. 17), REFEREE-2 "SIGNED" (l. 37).
  (b) Lemma DECOUPLE (§2, l. 89-90): "σ^(j+1) = F(σ^(j)) for every j < p, and Iσ^(p) = ∅. So the distinct-σ sequence is σ_0, F(σ_0),
      F(F(σ_0)), …, up to the first strategy with no improving edge, and it does not depend on τ_0. The mirror holds for τ with F^d and
      τ_0." (Iσ, Ξσ, σ̄(σ) are functions of σ (R15 (d), S1 deterministic); if A(σ) ≠ σ, S4c does not fire and σ := F(σ); if A(σ) = σ,
      σ changes only by S4c's Even branch, which by FIX 3 sets F(σ); τ decides WHEN σ stalls, not to what it moves.) Cells: REFEREE
      "SIGNED" (l. 18), REFEREE-2 "SIGNED" (l. 38).
  (c) Lemma ONE-PLAYER (§3, l. 102-104), with F7 (premise) and F10: "Let σ be an Even strategy with Iσ ≠ ∅, σ̄ := σ̄(σ), and G_σ̄ as in
      §0. Then: (a) the valuation of σ in G_σ̄ (SPEC S1 on G_σ̄) equals Ξσ, and the improving set of σ in G_σ̄ equals Iσ; (b) F(σ) equals
      N5's iteration (SPEC S4a + S4c) on G_σ̄ from (σ, τ := σ̄), restricted to σ." F10: «"The same arena H" means the same graph: the same
      vertex ids, owners and priorities, and the same successor lists in increasing index order, which S1's procedure uses». The τ side
      (used by SF-RED (b)'s mirror), F2: «Ω + 2 keeps every rank, every parity and every successor list, so S1's output is the same. …
      So the mirror of ONE-PLAYER (b) holds verbatim.» Cells: REFEREE "SIGNED (with the standing S1-conformance premise named, SF-N1)"
      (l. 19); REFEREE-2 "SIGNED (the τ-side mirror needs one line: N-SF-2)" (l. 39). F2 checked by both: REFEREE-2 §C C.3 (l. 69)
      "Correct; matches my OPb check"; REFEREE §C P2 (l. 33) "Correct" ("dual of dual adds 2 to every priority and swaps owners back").
  (d) Theorem SF-RED (a) (§3, l. 111), with F3 and F8: "Every stretch [a, b] has b − a ≤ n + m, and at most n − 1 of its transitions
      change Ξ." F3: «"these b − a transitions lie in one λ-phase of that run" is to be read as: they are a PREFIX of a λ-phase of N5's
      run on G_σ̄ started at (σ^(a), σ̄). … R17 (c) bounds the whole λ-phase, hence the prefix. The bound b − a ≤ n + m is unchanged.»
      F8: the S4c step «switches each such own-cycle-node x to an Ω-best improving successor (the Remark after Theorem PH), so it is a
      step of that kind and changes no valuation». (DECOUPLE and ONE-PLAYER (b): σ^(a..b) are consecutive N5 states on G_σ̄; R17 (e):
      S4a steps are switch-best, an S4c step leaves no improving edge, so it is the last transition of [a, b]; R17 (c): < n + m′ ≤ n + m
      switch-best steps in a λ-phase, ≤ n − 1 value-changing.) Cells: REFEREE "SIGNED (the S4c-step-is-flat link reads R17 (e) through
      R17's Theorem PH proof, SF-N2)" (l. 20); REFEREE-2 "SIGNED" (l. 40); REFEREE-2 §C C.1 (l. 18): "SIGNED by both, with the citation
      of C.2" (C.2 l. 27-35: the second clause "needs the S4c step on G_σ̄ to change no valuation"; "The first clause (b − a ≤ n + m)
      and (b), (c) do not depend on it"); discharged by F8 (REFEREE-2 C.5 l. 95; REFEREE §3 addendum l. 66).
  (e) Theorem SF-RED (b) (§3, l. 112-113): "#σ − 1 < (n + m + 1)(1 + LAM_σ + SBC_σ), LAM_σ ≤ n(n − 1); the mirror for τ. Hence
      I < (n + m + 1)(2(n² − n + 1) + SBC)." (At most LAM_σ + SBC_σ stretch boundaries, so S ≤ 1 + LAM_σ + SBC_σ stretches and
      #σ − 1 = Σ (b − a) + (S − 1) < S(n + m + 1); LAM_σ from R15 (a) on each Switch_J, the cycle node's reward compared first, p′
      injective (F13: proved in place, R47 deliberately not cited); G^d has the same n and m; then SF-TERM.) Cells: REFEREE "SIGNED"
      (l. 21), REFEREE-2 "SIGNED" (l. 41).
  (f) Theorem SF-RED (c) (§3, l. 114-115): "Conversely SBC_σ ≤ #σ − 1 and SBC_τ ≤ #τ − 1, so SBC ≤ 2I. N5-SF makes polynomially many
      iterations on a class of games iff SBC is polynomially bounded there." F6 (first sentence): the «iff» «quantifies over all runs
      on the class, i.e. every game of the class and every start pair». Cells: REFEREE "SIGNED" (l. 22), REFEREE-2 "SIGNED" (l. 42);
      REFEREE-2 §2.5 (l. 120): "The equivalence follows, read over all runs of the class."
  The proposed RESULTS line: REFEREE "MATCHES the signed content and claims no more (§5); one optional clause (SF-N1)" (l. 23);
  REFEREE-2 "MATCHES the signed content (§2.6)" (l. 43); REFEREE-2 §C C.1 (l. 21): "MATCHES, per both. I support the optional clause:
  it names the premise F1 now states". The optional clause is carried above as a premise disclosure, not in the title.
- Not signed: §3 Remarks 1-2 (READING, "not to sign", packet table l. 27); Remark 2's phrase «nothing about σ̄ beyond its being a
  function of σ» is replaced by F1 and F7 («F1 and F7 together replace that phrase of Remark 2»; REFEREE §3 addendum l. 65 "Remark 2
  was not signed, so its replacement touches no signed item"). Remark 1's sharper b − a < n + m: READING (F5: «Remark 1 stays a
  remark»). §4: DATA and the pinned check (DATA, not to sign). §5: CONJECTURE SF-POLY (SBC polynomially bounded on every game) OPEN;
  with SF-RED (c) it is EQUIVALENT to N5-SF being polynomial («it is not an easier statement; it only names where the cost sits»).
  Output correctness: S5 on the final σ, as in N5. The packet (l. 88, l. 170) rests it on VJ00 Lemma 5.8 (RESULTS R15 limit (iii),
  G-N5T-3). Since RESULTS R57 (b) Lemma OUT-G (every game, every σ with Iσ = ∅; standing premise 1E-N3), N5's output correctness rests on
  OUT-G, and the output half of G-N5T-3 is removed (R57 Not signed; GAPS G-N5-TIME). Neither the packet nor either referee applies OUT-G to
  N5-SF's stop, so output correctness is not claimed here. Gauntlet status (TARGET.md §5): «N5-SF has passed no gauntlet step in full» (packet l. 172;
  docs/new/N5-SF-gauntlet-box55.md, not reviewed). The packet's "Consequence (timing only)" (l. 98-99) is not a row of either verdict
  table: its "#σ only on σ_0 and #τ only on τ_0" is DECOUPLE's content, and "I depends on both starts" is not claimed. F12's sharper
  "n − 1" stretch bound: «a sharper statement (n − 1) would be a new claim for both referees» (not made).
- Referee strengthening (NOT part of this entry; remarks of one or both referees outside the verdict cells, or optional wording):
  (0) F6's per-start-rule form of SF-RED (c): «(b) and (c) are inequalities per run, so the same equivalence also holds for any fixed
  start rule (e.g. SPEC S3)». REFEREE-2 N-SF-6 (§4 l. 182-183) and §C C.3 (l. 73): "a direct reading of the signed per-run inequalities,
  not a new claim"; REFEREE §C P7 (l. 38): "Correct: (b), (c) are per-run inequalities, so the equivalence holds over ANY set of runs
  (all starts, or S3 starts only). It adds an immediate consequence, it widens no signed statement". Not in either verdict cell.
  (i) REFEREE §3 (l. 49), ONE-PLAYER (a): "It does NOT need σ̄(σ) to be a one-step minimiser (the FIX 2 / Lemma DF trap is not
  touched)." (one referee). (ii) REFEREE §4 (c) (l. 68): the equivalence uses "m ≤ n², self-loops included". (iii) REFEREE-2 §2.4
  (l. 102-103), a second derivation that an in-stretch S4c step is last: "Iσ^(j+1) in G equals its set in G_σ̄, which is ∅ (ONE-PLAYER
  (a)). Hence j + 1 = p = b". (iv) REFEREE-2 §2.5 (l. 116-117): "The inequality stays strict even when #σ = 1." (v) REFEREE-2 §1
  (l. 53-54): R15 (c)'s "every non-empty switch of improvements goes strictly up in ≺" "is for VJ00's unambiguous switches, which is what
  SF-TERM (i) supplies". (vi) REFEREE §4 (b) (l. 65) and SF-N7: the LAM argument "is R47 Lemma Φ (a)'s argument, re-proved here from
  R15 (a)"; REFEREE-2 §C (l. 49) "record only". (vii) REFEREE §C P4 (l. 35) and REFEREE §4 (l. 57-58): "the phase starts at a, since the
  G_σ̄ run starts there" — the same point as F3, "made from the other end" (REFEREE-2 §C l. 54-55).
- Honest limits: (i) SF-RED is a REDUCTION for a VARIANT (N5-SF) of N5: it bounds N5-SF's iterations by a polynomial times SBC and SBC by
  2I; SBC is NOT bounded here (CONJECTURE SF-POLY OPEN). DATA only (packet §5, not refereed): «SBC ≤ 1.17n on the library, ≤ 16 on the
  M1 families; on PGSolver's switchbestexp N = 1..16 SBC = 1, 4, 11, 26, 49, 56, 60, 75, 92, 97, …, 138, 179, 232 (0.57n at N = 16)».
  (ii) It says nothing about N5 itself: N5-SF is a different algorithm (REFEREE-2 X_ORBN5, DATA: on 2,787 of 14,220 runs N5's
  distinct-σ sequence differs from N5-SF's; REFEREE MUT 1, N5's own S4a in place of S4a′, bites: ORB 113, TAU_E 119, ONEPb 120 on
  1,000 runs). No statement here transfers to N5's run; G-N5-TIME untouched. (iii) I counts iterations, not bit operations; no
  running-time bound. (iv) Output correctness: not claimed (Not signed;
  RESULTS R57 (b) OUT-G covers S5 at every σ with Iσ = ∅, its application to N5-SF unsigned) (DATA: REFEREE-2 WIN, N5-SF's final regions equal N5's on all
  14,220 runs; packet: WIN PASS and OPT PASS on box 54's runs). (v) Sharpness (DATA): no stretch exceeds n − 1 transitions in either
  referee's data (REFEREE max 47 families / 44 library, MUT 2 does not bite; REFEREE-2 X_SEGn1: 0 on lib41, alt_all, fam, hard, max
  69 / 59 / 56 / 52); the lane's max is 101 at switchbestexp_16, n = 410 (F5, F12; not re-run by REFEREE-2, C.3 l. 72). The signed
  bound n + m stays. (vi) Not M3, not a gauntlet pass, not a TARGET.md claim.
- Data (DATA, not proof): pinned (packet §4; experiments/new/box55/pcheck.py, sha1 f4d741c2271b09fed3783d808af081bfd618860a, imports
  box54/n5sf.py, sha1 1ea3bdc79d1ee0f4110c9a1b61e37f854210ad4f, and box21/n5x.py, sha1 bbc7d4c9277011e8ddff7684a6f0e8b90192191a;
  box55/ntcheck.py sha1 7d60b5dde930c72fec7125e2fb170cf9880ad709; all four equal at 95a7a581 and 3d8b357d; check.sh block "Box 55";
  instances switchbestexp_2.pg b3d5bc293d1b76ce5c7ae8dadc4e9b0b51294484 and n3cov_lean.pg bcf8dbf64cba48123dc7da849b179793257e13e1,
  pinned there). Re-run for this draft on trunk 3d8b357d (experiments/new, `python3 -I`, outputs to a scratch file, exit codes read):
  n3all_maxph_0 «ROW E_ n 3 m 6 values 3 orbit 3 SBC 1 LAM 1 SEG 2 SEGMAX 1», CHECK PASS; switchbestexp_2 «ROW E_ n 60 m 130 values
  59 orbit 59 SBC 4 LAM 0 SEG 5 SEGMAX 18», CHECK PASS; n3cov_lean «ROW E_ n 48 m 128 values 29 orbit 29 SBC 11 LAM 4 SEG 12 SEGMAX 6»
  and «ROW O_ n 48 m 128 values 6 orbit 6 SBC 3 LAM 5 SEG 6 SEGMAX 0», CHECK PASS; MUT=1 on switchbestexp_2 «E_ORB_V», CHECK FAIL (exit
  1); ntcheck NT PASS; quote checks as in Object. All exactly as packet §4 and check.sh. Start convention (F4): unlisted vertices take
  their S3 start successor; n3cov_lean.start's SIGMA0 47:18 sits on an Odd vertex and has no effect (F11). Packet corpora (§4, lane
  DATA): alt_all 413 / 413 CHECK PASS, sicorpus 276 of 277 entries (1 not run: no TAU0 line), box 54 families 20 / 20, hard families
  (switchbestexp N = 1..8, switchallexp N = 1..6, Oink M1 generators) 73 / 73; 0 violations, 0 timeouts. REFEREE (successor 18; own
  scratch/sf_probe.py, sha1 24a38b5b…, its own N5-SF on rl_engine, no lane code; pinned re-runs from a clean worktree at 95a7a581,
  exact): 4,482 runs (random rand_ck n 5-14 4,000; library n ≤ 48 378; box 54 families + hard families + pins n ≤ 200 104), 12,826
  iterations, CONF 695,462 vertex checks (Ξσ = play value of (σ, σ̄(σ))), ONEP 15,614, 18,434 stretches, 353 in-stretch S4c steps
  (all Ξ-flat and last), max SBC 60, max stretch 47, 0 violations; skipped 63 library games with n > 48 and 6 hard-family games with
  n > 200; two given starts rejected by its parser (S3 only there). REFEREE-2 (successor 20; own R2-N5-SF/sf_check.py on si.py and its
  lane's dual_check.Runner; lane tools only run as check.sh's commands from a worktree at 95a7a581, never imported): 14,220 runs,
  34,162 iterations (random n 4-14 12,000, n 15-30 1,200, lib41 820, alt_all 93, box 54 families 34, hard 73), OP checks 28,052 /
  17,111 (Even / Odd), fallbacks 610 / 642, 0 violations of TERM, ORB, ORB2, OPa, OPb, SEG, FBLAST, BND, WIN; its own N5-SF reproduces
  the lane's SBC / LAM / stretch count / max stretch on all three pins, both sides, under the S3 fill (first-successor fill gives E SBC
  12 and 13 stretches on n3cov_lean, N-SF-4); max SBC 75 / 16 (E / O, hard), max LAM 28, max I 489; strict quote check 18/18, SHIFT=1
  control 0/18; at C.5 the fixes file's 6 quotes 6/6. No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-SF.md (report 500b51d7a78853710c88d4d49dd2603f923d815c, 2026-10-29T16:20:04Z, sha1
  d2311efa0e7fc1218f452c9018ccc08d1cd48fdf, 127 lines, = trunk 3d8b357d; successor 18); §C docs/referee/R-N5-SF-C.md (6bbf0aed,
  2026-10-29T16:37:34Z, sha1 827f81e3c56fdd7f1b6779e238f53fdd94fa137d there, 57 lines; §3 addendum 530e09c9, 2026-10-29T17:12:39Z,
  append-only (`git diff 6bbf0aed 530e09c9`: 16 added, 0 removed), sha1 247f82c56d68180a73d1dd188fa70bc381d7f28f, 73 lines, = trunk):
  §0 CHECKED; SF-TERM, DECOUPLE, ONE-PLAYER (a), (b), SF-RED (a), (b), (c) SIGNED; RESULTS line MATCHES (optional clause SF-N1); notes
  SF-N1..N7; "No gap. Nothing FALSE." REFEREE-2 docs/referee-2/R2-N5-SF.md (report 3ae22a6d8c0498326e09cd811b8ce6e12f4c8734,
  2026-10-29T16:03:33Z, sha1 031834ba91cb794e174d2b91786da5f94aacf63a, 193 lines, = trunk; successor 20); §C
  docs/referee-2/R2-N5-SF-C.md (42022bca, 2026-10-29T16:34:33Z, sha1 60a850b760e75e61a9c8640250b06d90158727ef there, 97 lines; C.5
  894a1971, 2026-10-29T17:16:25Z, sha1 1e20eb1d0308e76bab627893f2dbd2f28a4b737f, 112 lines, = trunk; `git diff 42022bca 894a1971`: 18
  added, 3 removed: the placeholder "## C.5 F7-F13" / "Pending (the Lead will send the SHA)." and the NEEDS line were replaced, no
  verdict line changed): §0 SIGNED; SF-TERM, DECOUPLE, ONE-PLAYER (a), (b), SF-RED (a), (b), (c) SIGNED; RESULTS line MATCHES; notes
  N-SF-1..6; "No gap. No item FALSE." INDEPENDENCE: REFEREE l. 7: "no REFEREE-2 SF file opened (none on my tree)"; REFEREE §C l. 3-4:
  REFEREE-2's report "read only after the Lead's word (my report pushed first)". REFEREE-2 l. 17-18: name count of SF files on
  origin/claude/referee 0 at 15:55:17Z and 16:03:20Z, "No docs/referee/ file opened"; REFEREE-2 §C l. 5-6: REFEREE's report "First
  opened 16:31Z, after my report was pushed (3ae22a6d, 16:09Z)" (commit time of 3ae22a6d: 16:03:33Z). No review imported lane code.
  §C (both): verdicts identical (REFEREE §C l. 22: "VERDICTS IDENTICAL. Nothing FALSE on either side. JOINT GAP MAP: EMPTY. E-ITEMS:
  NONE"; REFEREE-2 §C l. 24: "Joint gap map: EMPTY. No gap, nothing FALSE. Every to-sign item is SIGNED by both referees."). E-item
  classes differ: REFEREE-2 classes SF-N2 (citation) and SF-N3 (quote) as E (C.2), discharged by F8 and F9 (C.5 l. 95-96, l. 103-104:
  "With F1-F13, the P-N5-SF joint gap map stays EMPTY and has no open E-item"); REFEREE classes them as notes (§3 addendum l. 66: "I
  classed SF-N2 as a note: the step was already right, now cited"). Fixes accepted by both: F1-F6 (REFEREE §C l. 48 "CONFIRMED for
  F1-F6"; REFEREE-2 C.3 l. 75 "F1-F6 are ACCEPTED"), F7-F13 (REFEREE §3 addendum l. 72: "none widens or changes a signed statement";
  REFEREE-2 C.5 l. 102 "F7-F13 ACCEPTED"). REFEREE §3 addendum l. 73: "Nothing open on P-N5-SF; SF-POLY OPEN, G-N5-TIME untouched."
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a reduction, for the variant N5-SF of N5, of N5-SF's iteration count to the
  best-reply change count SBC, which is not bounded; no running-time bound, no algorithm claim; N5-SF has passed no gauntlet step in
  full). GAPS G-N5-TIME: open, untouched.

Proposed GAPS line-11 UPDATE (append-only): no GAPS row changes. G-N5-TIME (GAPS l. 11) is "N5 SSI-GLOBAL makes polynomially many
iterations"; R87's title clauses are about N5-SF, a different algorithm ("it says nothing about N5 itself"; "G-N5-TIME untouched"),
so they neither change that row's status nor add a step toward it; no GAPS row names N5-SF, SBC or CONJECTURE SF-POLY, and SF-POLY is
the lane's open conjecture (packet §5), not a gap of a signed claim. Nothing to append.
