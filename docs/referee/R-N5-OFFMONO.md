# R-N5-OFFMONO: REFEREE report on packet P-N5-OFFMONO (L-NEW box 49: Lemma OFFSET-MONO, Corollaries CHAIN-SUM and CHAIN-COUNT; every game)
Referee: REFEREE (successor 15), Opus 5.5 (owner ruling D15). FIRST referee (Lead queue of 17:02Z by date -u).
- Object and pin: docs/new/P-N5-OFFMONO-box49.md, sha1 d9705ac6cede9849d68bf9b8d0fc5c54ab6fc3c4, 160 lines, author L-NEW successor 28: the same
  sha1 on my tree and at the l-new freeze 1f816370 (an ancestor of HEAD). Its quote base 58061d91 is an ancestor of the freeze.
- Written 2026-10-26T17:25Z-17:29Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ file on OFFMONO on my tree, on trunk or on origin/claude/referee-2 at any of my fetches
  (re-listed in the same turns; 0 / 0 / 0 at 17:29Z). No lane code run (experiments/new/box48/offmono2.py, reset.py, quotecheck2.py neither executed nor
  imported; lane start files read as data). D1.
- Premises read against their text: SPEC S1's order (l. 30-31), S4a, S4c; RESULTS R38 (a); R56 setting, (a) (Aκ), (A0κ), (M1κ), (M2κ), (d)
  κ-Y-FORM_D; R18 (d) Lemma S (a) (l. 803-804) with R57 (a) (VJ) and 1E-N3 (S1's σ̄ is Odd's optimum); (SW) as in R72's premises (l. 3768-3769).
- Quotes and pins: all 12 curly-quoted passages of §6 verbatim (whitespace normalised) at 58061d91, each ending at its cited line (my
  scratch/fbc_quotes.py). Pins N5-ssi-global.md 66fde9ef, P-N5-FBRED-box44.md 11b15455, P-N5-FBPOLY-box41.md de244dcd at 58061d91: match.
- Tool: scratch/offmono_probe.py (own engine rl_engine; checks in §3). Logs scratch/offmono_logs/.

## Verdicts (sign-off line per item)
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | Lemma OFFSET-MONO | SIGNED |
| §2 | Corollary CHAIN-SUM | SIGNED |
| §2 | Corollary CHAIN-COUNT | SIGNED (a REDUCTION: EXIT_x, CYC_c and the offset-value count D are not bounded here, as the packet says) |
| §1 | Remarks (i)-(iii) | (iii) CHECKED (true, and used); (i), (ii) READINGS |
| §3-§5 | READING, data, open | not signed (as briefed) |
No gap. Notes OFFMONO-N1..N4. Nothing here bounds ρ, N_ep, f or the exit changes; no running-time bound; not a TARGET.md claim; G-N5-TIME stays
OPEN.

## 1. OFFSET-MONO, re-derived (parentheticals checked one by one)
- Setting ✓. par_{t+1}(q) is the first vertex of Q ∖ {q} on q's honest play at t + 1 strictly before c, else c. π runs from y2 to p on that
  play; its vertices lie in U (on q's play; λ fixed on the phase) ✓; none is in Q: not in Q ∖ {q} (p is the first such) and ≠ q "(the play is
  simple before c by (Aκ) iterated and q ≠ c)" ✓ — even when q lies on an honest cycle at t + 1, that cycle is c's and the play from q meets c
  before it returns to q. y2 ≠ q (a self-loop at q would make q its own cycle node, λ(q) = c ≠ q) ✓.
- Step 1 ✓. Backwards along π; at p both offsets are (0, 0). (Aκ) at t + 1 for x ∈ π (x ≠ c: x precedes p, which is c or precedes c) ✓. The
  remaining inequality κwt_c(x) + κ_t(x′) ⪰ κ_t(x): x Odd ⇒ x ∉ Q ⇒ x′ = next_t(x) ✓; x Even unswitched ✓; x Even switched to x′ ⇒ (x, x′) ∈ Iσ_t by
  (SW) (S4a's arena or S4c), x′ ∈ U (on q's (t+1)-play) and σ_t(x) ∈ U, so (M1κ) turns Ξ_t(x′) ▷ Ξ_t(σ_t x) into κ_t(x′) ≻ κ_t(σ_t x) ✓.
  "No step uses where x's play went at t" ✓.
- Step 2 ✓. (Aκ) at t + 1 and at t for q (q ≠ c) ✓. Case N: y2 ∈ Y^q_t and κ-Y-FORM_D's minimum is at y1 = σ̄_t(q) ✓ (q on no honest cycle at
  t, the hypothesis). Case L: y2's play at t meets q before c (else q would lie on c's cycle, an honest cycle at t) ✓; (Aκ) iterated along ζ
  (vertices in U ∖ {c}) gives κ_t(y2) = κwt_c(Z) + κ_t(y1) ✓; under (σ_t, τ″) the play from q is the cycle Z (ζ avoids q until its end, so
  τ″'s change at q is not met) ✓; Lemma S (a) with Ξ_t = L_{σ_t} (1E-N3: S1's σ̄ is Odd's optimum; R57 (a) for every game) gives Ξ_t(q) ⊴
  V_{σ_t,τ″}(q) with different cycle nodes c ≠ u*, so reward(u*) > reward(c) ✓. A vertex of Z above c: u* above c, wt_c(Z) has u*'s sign, and
  u* odd would have reward −p′(u*) below both ±p′(c) ✓, so u* even and wt_c(Z) > 0 ✓. All of Z below c: c even is impossible (p′(c) beats every
  lower vertex's reward) ✓, so c odd, s_c = +1, κwt_c(Z) = (0, |Z|) ≻ (0, 0) ✓. In both cases the claim ✓.
- Remark (iii) ✓: only "q on no honest cycle at t" is used; Step 2's (Aκ) at t + 1 holds for every z ∈ U ∖ {c}. The hypothesis is used twice
  (κ-Y-FORM_D in Case N needs it; Case L needs q met before c). In data it is never needed: my MUT=3 (admit q on an honest cycle at t) checked
  4,006 such (t, q), all of Case L type, and the conclusion held at every one (OFFMONO-N4).
- The packet's "What this is" bullet ("(E1), (E2) of KPOLY §2 are NOT needed") is consistent with the proof: neither Step uses where x's or y1's
  play went beyond the facts above. (Not a signed item.)

## 2. CHAIN-SUM and CHAIN-COUNT, re-derived
- CHAIN-SUM ✓. The (t+1)-chain's vertices lie on q's (t+1)-play before c, distinct, in Q ∩ U ∖ {c} ✓; for i ≥ 1, par_{t+1}(x_i) = x_{i+1} because
  x_i's play is the suffix of q's and x_i does not recur before c ✓; the telescoping sum ✓ with κ(c) = (0, 0) (A0κ) ✓; each term with x_i on no
  honest cycle at t is OFFSET-MONO at x_i with p = x_{i+1} ✓.
- CHAIN-COUNT ✓. A κ(q)-changing transition outside CYC_c has all chain levels on no honest cycle at t, so all terms ⪰ (0, 0) and one is ≻ (0, 0)
  ✓; if that level's parent changed, it is in EXIT_x ✓; else it lies in an x-piece (not in EXIT_x ∪ CYC_c), where OFFSET-MONO applies with one
  fixed p at every transition, so off(x; p) is non-decreasing on the piece and rises strictly ≤ D − 1 times ✓; x-pieces ≤ |EXIT_x ∪ CYC_c| + 1 ✓;
  the sum ✓. D is a uniform bound assumed over every x-piece (a hypothesis, stated) ✓.

## 3. Data (own engine; DATA, not proof; 0 failures of every signed check)
Checks: OM (OFFSET-MONO at every in-phase transition and every q ∈ Q ∩ U ∖ {c} on no honest cycle at t, p := par_{t+1}(q), κ with the class
sign s_c), STEP1 (Step 1 at every vertex of q's (t+1)-path from y2 to p), CS (CHAIN-SUM: the identity and the sign of every term at a level on
no honest cycle at t), CC (CHAIN-COUNT on J := the phase, with D := the actual maximum number of offset values over all x-pieces).
| sample | runs | phases with ≥ 2 states | OM checks (Case L; parent changed) | STEP1 | CS | CC (max D; max κ-changes of one vertex) |
| --- | --- | --- | --- | --- | --- | --- |
| scratch/fbc_lib.txt, n ≤ 40 (870 files), S3 + 2 random | 2,610 | 2,205 | 30,635 (117; 1,769) | 112,498 | 34,641 | 9,024 (61; 60) |
| random 3,000 games (n 6-22, ≤ 8 Odd choice vertices, seed 551), S3 + 4 random | 15,000 | 3,607 | 7,619 (4; 330) | 9,966 | 9,233 | 8,398 (3; 2) |
| nep90_n40 / nep76_n40 / long121_n40 at their start files | 3 | 3 | 455 / 390 / 363 (0 / 0 / 2; 53 / 60 / 48) | 3,308 / 2,304 / 2,886 | 455 / 390 / 363 | 5 / 5 / 3 (69 / 16 / 11; 72 / 62 / 44) |
- The packet's check counts reproduce exactly at the lane's start files (455 / 390 / 363) and Case L on long121 (2); my "parent changed"
  column differs (OFFMONO-N1).
- Mutations (n ≤ 40 library, S3 + 2 random): MUT=1 (p := par_t(q), the OLD routing vertex, where it differs): 490 failures of 1,769 — the
  lemma is about the NEW routing vertex; MUT=2 (the opposite length sign in κ): 1,308 failures. MUT=3 (admit q on an honest cycle at t):
  0 failures of 4,006 (OFFMONO-N4).
## 4. Notes (none blocks a signature)
- OFFMONO-N1 (data, "parent changed"). At the lane's three start files my count of checks with par_t(q) ≠ par_{t+1}(q) is 53 / 60 / 48 (nep90 /
  nep76 / long121) against the packet's 28 / 42 / 26, while the check counts agree exactly (455 / 390 / 363) and Case L agrees on long121 (2). The
  difference is in a DATA column only; the lane should state its definition of "parent changed" (mine: par_t(q) ≠ par_{t+1}(q), par as §0).
- OFFMONO-N2 (CHAIN-COUNT's D). On the lane instances D is large (max D 69 on nep90's phase, against at most 72 κ-changes of one vertex), so
  CHAIN-COUNT is weak exactly where R61's product is; the packet's §3 reading says so in other words.
- OFFMONO-N3 (premise wording). Step 2's Case L uses Lemma S (a) through the standing premise 1E-N3 (S1's counterstrategy is Odd's pointwise
  optimum, form P1); the packet says so in the proof; the premise list could name P1 as P-N5-FLIP §1 does.
- OFFMONO-N4 (data on the hypothesis). OFFSET-MONO's conclusion also held at all 4,006 (t, q) with q on an honest cycle at t (n ≤ 40 library);
  a CONJECTURE that the hypothesis can be dropped would be the natural next item; it is not proved here (Case N's κ-Y-FORM_D and Case L's
  "q before c" both use it).

## §C (unit: OFFMONO + add1 + add2 + add3). Comparison with REFEREE-2 (written 2026-10-28T21:07Z by date -u, after the Lead's word of 21:05Z;
REFEREE-2's unit report docs/referee-2/R2-N5-OFFMONO.md at origin/claude/referee-2 4e9a6372, read only after all four REFEREE reports were pushed:
R-N5-OFFMONO 04a563d3 and R-N5-OFFMONO-add c2a97189 (successor 15), R-N5-OFFMONO-add2 d6e07396 and R-N5-OFFMONO-add3 907e21b9 (successor 16))
Written by REFEREE successor 16: as SUCCESSOR to the author (successor 15) for OFFMONO and add1, as author for add2 and add3. For the first two
I re-read the reports, the packets' statements and REFEREE-2's report; the data cited below for them are my predecessor's, and the
OFFSET-MONO⁺ and add2 probes I ran (add2_probe.py, add3_probe.py) re-check OFFSET-MONO and CHAIN-SUM along the way. Every verdict is
labelled (Opus 5.5, D15).
### Verdicts
| file § | item | REFEREE | REFEREE-2 (4e9a6372) | joint |
| --- | --- | --- | --- | --- |
| OFFMONO §1 | OFFSET-MONO | SIGNED | SIGN | SIGNED |
| OFFMONO §2 | CHAIN-SUM, CHAIN-COUNT | SIGNED | SIGN | SIGNED |
| add1 §0 | (CYC-ID), (CYC-SHAPE) | SIGNED | CORRECT | SIGNED |
| add1 §1-§2 | Z-CONST, CHAIN-COUNT′ (Step A, forms, Remarks) | SIGNED (OFFADD-N1 on Remark (i)) | SIGN | SIGNED |
| add1 §3 | ZCH-COUNT and its Corollary | SIGNED | SIGN ("c Even / Odd" = owner, N-OFF-5) | SIGNED, owner reading |
| add2 §0-§3 | (A-F), FT-COUNT, FT-CONST, CHAIN-COUNT″ | SIGNED | SIGN (FT-CONST's offset clause for x ∈ Q, N-OFF-3) | SIGNED, with N-OFF-3 |
| add2 §4 | PF-CHOICE, TIE-CHARGE (code-level, si.py e688b963) | SIGNED | SIGN | SIGNED |
| add3 §1-§2 | OFFSET-MONO⁺, CHAIN-COUNT‴ | SIGNED | SIGN | SIGNED |
| quotes | all | OFFMONO 12, add1 15, add2 23, add3 9 verbatim | 53 of 55 verbatim; the 2 REFEREE-file quotes in add3 left to its §C | all verbatim: I checked those 2 at c2a97189 (R-N5-OFFMONO-add3 header) |
Verdicts identical on every item. Joint gap map: EMPTY.
### Notes, matched
| REFEREE | REFEREE-2 | joint |
| --- | --- | --- |
| OFFMONO-N3 (Case L uses Lemma S (a) through 1E-N3) | its §0 premise column (Lemma S (a), standing premise 1E-N3) | same |
| OFFMONO-N4, OFFADD-N2 (on-cycle levels: conjecture) | N-OFF-7, N-OFF-9 | ANSWERED by add3's OFFSET-MONO⁺ (signed by both); mark both "PROVED by add3" (ADD3-N3) |
| OFFMONO-N1, N2 (data: parent changes; D large on lane instances) | N-OFF-8 (max EXIT per level 6), §2 (sum form tight in 2,857 cases) | compatible data notes |
| OFFADD-N1 (CHAIN-COUNT′ ⇒ CHAIN-COUNT goes through the sum form) | N-OFF-6 (the sum forms are the sharper statements; the D forms need D ≥ 1) | compatible; both accepted |
| ADD2-N1 (per vertex ≤ n F-touching changes, by contiguity of F: proof) | N-OFF-8 (FT-COUNT's factor 2 never needed in data, CTL_ft1 0) | compatible: mine is the proof, REFEREE-2's the data |
| ADD2-N2 (TIE-CHARGE's Even step: x′ ∈ U_c from (Aκ), not from add1's "on Z_{t+1}(c)") | its §1.4 makes the same step ("next_{t+1}(z) ∈ U_c by (Aκ)") without a note | REFEREE's citation note, consistent with REFEREE-2's reading |
| ADD2-N3 (si.py executed as the object), ADD2-N4 (cut ZC″ sound, not shown necessary) | N-OFF-2 (cut versions' bounds) | compatible |
| — | N-OFF-1 (R38 (a) KEY's quoted sentence is about λ_U; λ_Ξ constancy comes from the phase definition) | ACCEPTED (I read KEY's text: its quoted clause is λ_U's; the (λ_Ξ, τ)-phase fixes λ_Ξ by definition) |
| — (my add2 probe evaluates par at every vertex of Z_t(c)) | N-OFF-3 (FT-CONST's offset clause: par is defined for q ∈ Q ∩ U only; read x ∈ Z_t(c) ∩ Q) | ACCEPTED (OFFMONO §0 defines par for Q only; Step A″ uses only x ∈ Q) |
| — | N-OFF-4 (the minimum is attained by R56 (d) with (Aκ)) | ACCEPTED |
| — (my predecessor's zch_probe uses the owner of c) | N-OFF-5 (CEVEN / ODDC by the OWNER of c) | ACCEPTED |
| my add3 report §2: "the three earlier corollaries follow" from CHAIN-COUNT‴ | N-OFF-2: true of the ROUTE, not of the NUMBERS (a cut version's sum bound is lower in 15 / 10 / 12 of 27,395 pairs; e.g. tcS8_N9 J = 19..21, 39 against 55) | ACCEPTED; I withdraw my wording. Splitting a piece at a cut can lower Σ(v − 1) by one per x, and the cut forms add |ZC| once, not once per x; so the cut bounds do not follow numerically from ‴'s. Suggested wording: "are no longer needed" (add3 §3 is a READING, unsigned) |
| ADD3-N1 (y2 ≠ q: say it) | — (its §1.5 uses it silently) | REFEREE's one-clause note |
| ADD3-N2 (Case L2a never occurs in my data) | N-OFF-7 (L2a with P(Ξ_t y2) ≠ ∅ occurs 2 times in its thin-spot search, and holds) | CORRECTED: L2a is exercised, twice, in REFEREE-2's data only; L1 once in each referee's data (mine: harm_n12_seed412); the landing text can say "L2a exercised twice" |
### Data
Both own engines, 0 failures of every signed item. REFEREE-2's corpus (23,959 runs, 142,287 phase-class pairs) and mine (add2 112,872 runs, add3
103,872 runs) overlap only in lib41. Both find TIE and ODDC rare, the ZC / ZC″ cuts never needed, FT-COUNT's factor 2 unused, and L1 once.
Both PF-CHOICE tie-break controls bite (mine 568, REFEREE-2 2,585 / 13,369 / 645). No disagreement; nothing open between the referees on the unit.
