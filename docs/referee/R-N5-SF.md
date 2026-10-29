# R-N5-SF: REFEREE report on packet P-N5-SF (L-NEW box 55): N5-SF terminates (SF-TERM), decouples (DECOUPLE), reduces to one-player N5 (ONE-PLAYER), and Theorem SF-RED
Referee: REFEREE (successor 18), Opus 5.5 (owner ruling D15). FIRST referee (Lead brief 2026-10-29 15:54Z by date -u). REFEREE-2 reviews in parallel.
- Object and pin: docs/new/P-N5-SF-box55.md at claude/l-new 95a7a581, `git show 95a7a581:<path> | sha1sum` = dbc2345f62454d442e951de025b1b2aef8a35317,
  172 lines: equal to the Lead's figures. 95a7a581 is on origin/claude/l-new; the trunk merge 59d3f707 named by the Lead was NOT yet on origin
  at my fetches (15:56Z: trunk head 03c70a3f), so I reviewed the l-new commit directly. Fixes go to docs/new/P-N5-SF-fixes-box55.md.
- Runs 2026-10-29T15:58Z-16:18Z; report written 16:20Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independence: no REFEREE-2 SF file opened (none on my tree).
- Premises opened at 305cc8be and read in context: SPEC S1 (l. 26-46), S2, S4 a-d, S5 (l. 47-61), FIX 3 (l. 88); RESULTS R15 (a), (c), (d),
  limit (iii) (l. 628-649); R17 (l. 731-760) and its source docs/new/N5-phase-bound-box10.md §3 (Theorem PH proof, Corollary 2, l. 56-90).
- Scope (D1): a REDUCTION for a VARIANT of N5 (N5-SF). It bounds N5-SF's iterations by a polynomial times SBC and SBC by 2I; SBC is not
  bounded (SF-POLY OPEN). Not about N5 (G-N5-TIME untouched), not a TARGET.md claim, no running-time bound, not a gauntlet pass.

## Verdicts
| § | item | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §0 | definitions (σ̄(σ), Ξσ, Iσ, λ_Ξ, N5-SF = S4a′/S4b′, A, F, F^d, distinct sequences, G_σ̄, SBC, LAM, stretch) | CHECKED (well formed; S4a′/S4b′ are S4a/S4b with the opponent argument replaced, nothing else) |
| §2 | Lemma SF-TERM | SIGNED |
| §2 | Lemma DECOUPLE | SIGNED |
| §3 | Lemma ONE-PLAYER (a), (b) | SIGNED (with the standing S1-conformance premise named, SF-N1) |
| §3 | Theorem SF-RED (a) stretch bound b − a ≤ n + m, ≤ n − 1 Ξ-changing | SIGNED (the S4c-step-is-flat link reads R17 (e) through R17's Theorem PH proof, SF-N2) |
| §3 | Theorem SF-RED (b) #σ − 1 < (n + m + 1)(1 + LAM_σ + SBC_σ), LAM_σ ≤ n(n − 1), I < (n + m + 1)(2(n² − n + 1) + SBC) | SIGNED |
| §3 | Theorem SF-RED (c) SBC ≤ 2I; polynomial iff SBC is | SIGNED |
| — | Proposed RESULTS line (15:27:39Z) | MATCHES the signed content and claims no more (§5); one optional clause (SF-N1) |
| §3 Remarks, §4, §5 | READING, DATA, CONJECTURE / status | not signed; pinned checks reproduced EXACTLY (§6) |
No gap. Nothing FALSE. Notes SF-N1..N7.

## 1. Lemma SF-TERM: re-derived
- (i) ✓ S4a′'s arena gives Even v only A(v) = {σ(v)} ∪ Iσ(v), so a changed σ_new(v) is an Iσ-target; with Iσ = ∅, SPEC S4a «Else σ_new = σ»
  (l. 53, the line the packet quotes up to the sentence before; SF-N3); S4c's Even branch picks one Iσ-edge per vertex and needs Iσ ≠ ∅. So a
  σ-change is Switch_J(σ), ∅ ≠ J ⊆ Iσ, one edge per vertex. Mirror: S4b′ (S1 on H′, the original game, as SPEC S4b) and S4c's Odd branch on Iτ.
- (ii) ✓ R15 (c) (l. 637-639): every non-empty switch of improvements goes strictly up in the strict partial order ≺; so no σ recurs, no τ
  recurs. (iii) ✓ S4 runs only with Iσ ∪ Iτ ≠ ∅, and if neither step changes anything, S4c switches a non-empty set (Even's if Iσ ≠ ∅,
  else Odd's): every iteration changes σ or τ, so I ≤ (#σ − 1) + (#τ − 1) < ∞. (iv) ✓ the loop ends only at S5, unchanged; output = S5's on
  the final σ. Correctness of that output is NOT claimed (G-N5T-3), correctly.

## 2. Lemma DECOUPLE: re-derived
- Iσ, Ξσ, σ̄(σ) are functions of σ (R15 (d); S1's procedure is deterministic, list orders fixed «Successor and predecessor lists are in
  increasing index order», l. 43). A(σ) reads only σ, Iσ, σ̄(σ); S4c's Even branch reads only Iσ, Ξσ. So F is τ-free. ✓
- A σ-changing iteration has Iσ ≠ ∅ (SF-TERM (i)). If A(σ) ≠ σ then σ_new = A(σ) ≠ σ, S4c does not fire (its condition σ_new = σ fails),
  S4d sets σ := A(σ) = F(σ). If A(σ) = σ, σ can change only through S4c (which then fires with Iσ ≠ ∅, i.e. the Even branch; FIX 3: τ
  unchanged), setting σ := F(σ). ✓ τ only decides WHEN a stall happens (A(σ) = σ while τ_new ≠ τ: S4c does not fire and σ waits). ✓
- σ^(p): the run stops with Iσ = ∅; every σ^(j), j < p, has a successor, hence Iσ^(j) ≠ ∅; so the sequence is the F-orbit up to the first σ
  with no improving edge. ✓ Mirror: F^d reads only τ, Iτ, Ξτ, τ̄(τ); S4c's Odd branch fires only when Iσ = ∅, which again affects timing only. ✓

## 3. Lemma ONE-PLAYER: re-derived
- (a) In G_σ̄ Odd has a single strategy σ̄, so it is Odd's optimal counterstrategy there, and S1 on G_σ̄ yields the play values of (σ, σ̄).
  The plays under (σ, σ̄) are the same in G and G_σ̄. That these equal Ξσ is SPEC S1-Xi's definition («Ξσ = valuation of every vertex under σ
  and Odd's OPTIMAL counterstrategy σ̄») with σ̄ = σ̄(σ) the procedure's output: the standing S1-conformance premise (SF-N1; the same premise as
  R57 (b), REFEREE-2's N-GS-1). It does NOT need σ̄(σ) to be a one-step minimiser (the FIX 2 / Lemma DF trap is not touched). Data: CONF,
  695,462 vertex checks, 0 mismatches, own cycle nodes included (§6). Even vertices and their edges coincide, so S2 gives the same Iσ. ✓
- (b) N5's S4a on G_σ̄ with τ := σ̄: Even v keeps A(v) (same Iσ by (a)), Odd v keeps τ(v) = σ̄(v): the same arena H, as a graph with the same
  ordered successor lists, as S4a′ on G; the same S1 procedure on its dual returns A(σ). On G_σ̄ every Odd vertex has one successor, so Iτ = ∅,
  τ_new = τ, and S4c fires iff A(σ) = σ, with the same choice (same Iσ, Ξσ). ✓

## 4. Theorem SF-RED: re-derived
- (a) ✓ On [a, b], σ̄ := σ̄(σ^(j)) is constant, so by DECOUPLE and ONE-PLAYER (b) σ^(a..b) are consecutive N5 states on G_σ̄ from (σ^(a), σ̄),
  with valuations Ξσ^(j) there (ONE-PLAYER (a)). λ_Ξ constant ⇒ these b − a transitions lie in one λ-phase of that run (R17's definition; the
  phase starts at a, since the G_σ̄ run starts there). Each transition is an S4a step = switch-best (R17 (e)) or an S4c step. R17 (e): the
  fallback «fires only in the value-flat situation and then leaves no improving edge»: so the G_σ̄ run stops after an S4c step, at most one S4c
  transition lies in [a, b] and it is the last. R17 (c): < n + m′ ≤ n + m switch-best steps in a λ-phase, at most n − 1 value-changing. So
  b − a ≤ (n + m − 1) + 1 = n + m. The S4c step changes no valuation: SF-N2. So ≤ n − 1 transitions change Ξ. ✓
- (b) ✓ Stretch boundaries are j with σ̄ or λ_Ξ changing: ≤ LAM_σ + SBC_σ, so S ≤ 1 + LAM_σ + SBC_σ stretches, and #σ − 1 = Σ (b − a) + (S − 1)
  ≤ S(n + m) + S − 1 < S(n + m + 1). LAM_σ ≤ n(n − 1): R15 (a) gives Ξ pointwise non-decreasing along σ-changes (J unambiguous by SF-TERM (i));
  the order compares the cycle node's reward first and reward is injective (p′), so each v's cycle node changes ≤ n − 1 times, strictly up.
  (This is R47 Lemma Φ (a)'s argument, re-proved here from R15 (a).) The mirror on G^d (n vertices, m edges; R15 (a) on G^d). Then
  I ≤ (#σ − 1) + (#τ − 1) < (n + m + 1)(2 + LAM_σ + LAM_τ + SBC) ≤ (n + m + 1)(2(n² − n + 1) + SBC), since 2 + 2n(n − 1) = 2(n² − n + 1). ✓
- (c) ✓ SBC_σ counts transitions of the distinct-σ sequence, ≤ #σ − 1 ≤ I (each σ-change is in its own iteration); mirror; SBC ≤ 2I. The
  equivalence: I polynomial ⇒ SBC ≤ 2I polynomial; SBC polynomial ⇒ I polynomial by (b) (m ≤ n², self-loops included). ✓
- Remark 2 (not signed) says SF-RED uses «nothing about σ̄ beyond its being a function of σ»; ONE-PLAYER (a) also uses that σ̄(σ)'s plays realise
  Ξσ (SF-N1). Reading only; the signed items are unaffected.

## 5. The proposed RESULTS line against the signed content
- "terminates (Lemma SF-TERM; R15 (c), (d))" = SF-TERM. "its sequence of distinct σ depends on σ_0 alone and that of τ on τ_0 alone" =
  DECOUPLE. "SBC/2 ≤ I < (n + m + 1)(2(n² − n + 1) + SBC)" = SF-RED (b), (c). "SBC = the σ-changes at which σ̄(σ) changes plus the mirror" =
  §0's SBC_σ + SBC_τ (changes counted on the distinct sequence). "polynomial iff SBC is" = SF-RED (c) (on a class of games). "CONJECTURE
  SF-POLY OPEN; output correctness as N5's (rests on G-N5T-3)" = §5, not signed, correctly labelled.
- It claims nothing beyond §2-§3. Premise list R15 (a), (c), (d), R17 (c), (e): complete except the standing S1-conformance premise (SF-N1),
  which every N5 entry carries implicitly; optional to add "(and SPEC S1 conformance, as R57 (b))".

## 6. Re-runs and own control
- Pinned, from a clean worktree at 95a7a581, `python3 -I`, read first (pcheck.py sha1 f4d741c2…, quotecheck3.py eaf18411…, n5sf.py 1ea3bdc7…):
  - check.sh "Box 55" block (l. 191-210), run alone: prints «box 55 P-N5-SF: pcheck PASS on n3all_maxph_0 (fallback), switchbestexp_2 (SBC 4),
    n3cov_lean (LAM 4, SBC 11), MUT bites; quotes PASS: PASS», exit 0 (all its sha1 and ROW assertions pass).
  - Separately: quotecheck3 «quotes=18 bad=0 / QUOTES PASS», --mut «QUOTES FAIL»; n3cov_lean ROW E_ «n 48 m 128 values 29 orbit 29 SBC 11 LAM 4
    SEG 12 SEGMAX 6», ROW O_ «… values 6 orbit 6 SBC 3 LAM 5 SEG 6 SEGMAX 0», CHECK PASS; switchbestexp_2 ROW E_ «n 60 m 130 values 59 orbit 59
    SBC 4 LAM 0 SEG 5 SEGMAX 18», CHECK PASS. All EXACTLY as §4.
- Own control: scratch/sf_probe.py (sha1 24a38b5b…): my own N5-SF on rl_engine (S4a′ / S4b′ from §0's text and SPEC; no lane code), both
  players. Per run: TERM (stop with Iσ = Iτ = ∅, I ≤ (#σ − 1) + (#τ − 1), no repeat), CONF (Ξσ = play value of (σ, σ̄(σ)) at every vertex),
  ORB (distinct sequence = τ-free F-orbit, computed separately) and TAU (a second run from the same σ_0 with another τ_0, and the mirror, gives
  the same distinct sequence), ONEP (a) (S1 on G_σ̄ = Ξσ, same Iσ) and (b) (F(σ) = an N5 step on G_σ̄ computed from G_σ̄'s own values) at EVERY
  j, SEG (every stretch: b − a ≤ n + m, ≤ n − 1 Ξ-changing, an in-stretch S4c is last and Ξ-flat), TOT (SF-RED (b) per side, LAM ≤ n(n − 1),
  the I bound, SBC ≤ 2I).
  | corpus (sf_logs/) | runs | iterations | CONF checks | ONEP checks | stretches | in-stretch S4c | max SBC | max stretch | violations |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | random rand_ck n 5-14, 2,000 games, S3 + 1 random (rand2000) | 4,000 | 6,000 | 159,672 | 8,227 | 14,354 | 309 | 5 | 5 | 0 |
  | library (rho_probe.lib(), n ≤ 48; given + S3 starts) (lib) | 378 | 3,857 | 154,284 | 4,238 | 2,977 | 43 | 26 | 44 | 0 |
  | box 54 families + box 55 hard families + the 3 pins (copies in sf_inputs/, n ≤ 200; given + S3) (fam_hard) | 104 | 2,969 | 381,506 | 3,149 | 1,103 | 1 | 60 | 47 | 0 |
  Skipped: 63 library games with n > 48, 6 hard-family games with n > 200. Two given starts were rejected by my strict start parser
  (n3cov_lean.start: a SIGMA0 entry on an Odd vertex, which the packet's §4 notes; topfix_n8_cmp.start): S3 starts only there (SF-N5).
- Controls: MUT=1 (S4a′ against τ, i.e. N5's own S4a; random n 5-12, 1,000 runs) BITES: ORB 113, TAU_E 119, ONEPb 120. MUT=2 (stretch bound
  n − 1 instead of n + m) does NOT bite on the families: no stretch in my data exceeds n − 1 transitions (SF-N6).

## 7. Notes (for L-NEW's fixes file; none changes a verdict)
- SF-N1 (standing premise, recommended clause). ONE-PLAYER (a) identifies S1's Ξσ with the play value of (σ, σ̄(σ)), σ̄(σ) being the procedure's
  own counterstrategy: SPEC S1-Xi's definition plus procedure conformance (as R57 (b), REFEREE-2's N-GS-1). Name it in ONE-PLAYER's proof and
  in Remark 2 (which says SF-RED uses nothing about σ̄ "beyond its being a function of σ"). It is not the Lemma 5.8 / DF premise. CONF data: 0
  mismatches in 695,462 checks.
- SF-N2 (thin spot, a citation). SF-RED (a) uses that the S4c step on G_σ̄ changes no valuation. R17 (e)'s signed text says the fallback
  «fires only in the value-flat situation and then leaves no improving edge»; that switching then changes no valuation is in R17's source
  (N5-phase-bound-box10.md §3, Theorem PH proof l. 69-75: «it switches only vertices x that are their own cycle nodes … no valuation
  changes»). Cite it. Data: 353 in-stretch S4c steps, all Ξ-flat and last (SEGfb_*: 0).
- SF-N3 (quote). SF-TERM (i) cites SPEC S4a «Else σ_new = σ» (l. 53) outside the quoted text; add it to the [S4a] quote.
- SF-N4 (ONE-PLAYER (b)). "the same arena H" should say: as a graph with the same vertex ids and the same (increasing-index) successor lists, which
  is what makes the S1 procedure's output identical (S1 l. 43).
- SF-N5 (DATA). n3cov_lean.start sets SIGMA0 on an Odd vertex; the lane's tool ignores it, mine rejects the file; my n3cov_lean runs use S3
  and no given start. The pinned figures for that start are reproduced with the lane's tool (§6).
- SF-N6 (sharpness, DATA). Stretches never exceeded n − 1 transitions in my data (max 47 in the families, 44 in the library); the n + m of (a)
  (and n + m + 1 in (b)) is loose in data. Remark 1's sharper constant is consistent with this; nothing to sign.
- SF-N7 (LAM). The LAM_σ ≤ n(n − 1) argument repeats RESULTS R47 Lemma Φ (a)/(c) for N5-SF's σ-sequence; it is self-contained here (it needs
  only R15 (a) and injective rewards), which is correct, since R47 is about N5 runs, not N5-SF runs.

## DONE / FINDINGS / NEEDS
- DONE: this report; scratch/sf_probe.py, sf_inputs/ (copies from l-new 95a7a581), sf_logs/ (run_all.sh, rand2000, lib, fam_hard, mut1, mut2);
  pinned check.sh block and quotecheck re-run exactly.
- FINDINGS: SF-TERM, DECOUPLE, ONE-PLAYER, SF-RED (a)-(c) all SIGNED, no gap, nothing FALSE. The RESULTS line matches the signed content.
  Notes SF-N1 (name the S1-conformance premise) and SF-N2 (cite R17's proof for the flat fallback) are the substantive ones.
- NEEDS: Lead: the SF §C word when REFEREE-2 reports; route SF-N1..N7 to L-NEW (fixes file). Trunk 59d3f707 was not on origin at 15:56Z.
