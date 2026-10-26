# R2-N5-STAU: second-referee check of packet P-N5-STAU (L-NEW successor 24, box 45: N5 and N5^τ share every in-phase step; audit of the R48 (i) / R50 (h) chain for uses of S4b's output). REFEREE-2 (successor 15), 2026-10-26, written from 07:5xZ by date -u
- Object: docs/new/P-N5-STAU-box45.md, `git show ca0a4e97:docs/new/P-N5-STAU-box45.md | sha1sum` -> 7446d9a9e198ffa5073e0d43823d753b6aa46b3b (= the
  Lead's), frozen at l-new 010bfdae, pinned trunk ca0a4e97. Brief (Lead 07:31Z, GO 07:48Z): sign §1 (Lemma Στ-STEP (a)-(d) and its corollary);
  CHECK §2 as an audited table and answer its two audit questions; do not sign §3, §4.
- Independence: docs/referee/ was listed by name only (`git ls-tree --name-only`); there is no STAU file there, and I opened none. I read
  REFEREE reports on OTHER, landed packets (R-N5-X, R-N5-FB, R-N5-U1, R-N5-OE), because they hold signed proof text in the chain (§2.1 (ii)).
  The lane's experiments/new/box45/ scripts were not run or imported. L-COMP's data (l-comp 16c960b5) was compared only after my own runs (§3).
- Premises taken as LANDED: SPEC S1-S5 + FIX 1-4, Q1-Q4 (docs/new/N5-ssi-global.md); RESULTS R15, R18 (d); standing SPEC premise 1E-N3 (R57).

## Verdicts (Opus 5.5, D15)
| item | packet label | verdict | notes |
| --- | --- | --- | --- |
| §1 Lemma Στ-STEP (a) | PROVED | SIGN | — |
| §1 Lemma Στ-STEP (b) | PROVED | SIGN | N-STAU-2 (citation) |
| §1 Lemma Στ-STEP (c) | PROVED | SIGN | N-STAU-2 (citation) |
| §1 Lemma Στ-STEP (d) | PROVED | SIGN | N-STAU-3 (R15 (a) also transfers; it is used in the chain) |
| §1 Corollary | PROVED | SIGN | N-STAU-1 (wording: "exactly" holds as an inclusion only; the transfer criterion uses only the inclusion) |
| §2 audit table | AUDIT | CHECKED: correct in every row I re-read; complete for the 66 files after the additions of §2.3 (all "holds for N5^τ: yes") | audit answers: (1) YES, with completions (§2.1); (2) NO (§2.2) |
| §3 DATA, §4 conclusion | DATA / READING | not signed (brief) | reproduced in substance (§3); §4 see §4 below |
No gap. Four notes (N-STAU-1..4), none changes a statement.

## 1. Lemma Στ-STEP: proof check
Setting re-read against SPEC S4: S4a and S4b are computed from the same (σ, τ); S4c fires iff σ_new = σ and τ_new = τ; FIX 3: Even's fallback
leaves τ; Odd falls back only if Iσ = ∅, and then sets every switched Odd v to an Iτ edge, which is ≠ τ(v) by S2's definition.
- (a) ✓. Ξ, W, Iσ, Iτ are S1/S2 functions of the state; S4a's arena (Even v: {σ(v)} ∪ Iσ(v), Odd v: τ(v)) and its S1 call depend only on
  (σ, τ, Iσ); the two switch-alls read Iσ / Iτ, the two valuations and indices. S4b^τ changes S4b's OUTPUT only. Whether S4c FIRES may
  differ (it reads τ_new); (a) claims only that the switch-all, when applied, is the same function. Correct as stated.
- (b) ✓. If N5 keeps τ: an Odd fallback would move τ, so none fired, and S4b's output was τ (else τ_new ≠ τ and S4c does not fire, so τ moves).
  If Iτ = ∅, S4b^τ also gives τ. If Iτ ≠ ∅, SPEC's output is τ, which is value-optimal in H′ (N-STAU-2), so S4b^τ gives τ. Then both have
  σ_new = σ_a and τ_new = τ, the fallback fires in both iff σ_a = σ, and it is Even's (Odd's would move τ, so Iσ ≠ ∅) with the same switch-all.
- (c) ✓. The case split is complete. Iσ = ∅ excludes keeping τ: either both sets are empty (stop) or Iτ ≠ ∅, and then S4b^τ moves τ or keeps it
  and the Odd fallback fires (σ_a = σ, τ_new = τ) and moves τ. So Iσ ≠ ∅; if Iτ ≠ ∅ the kept τ is value-optimal (by the rule, or by
  N-STAU-2 when SPEC's output was τ). Then σ_a ≠ σ gives (σ_a, τ) and σ_a = σ gives the Even switch-all: (Σ(σ, τ), τ). The converse: at a
  τ-stable state S4b^τ returns τ, and the same split applies. For N5, "S4b's output is τ" replaces the rule.
- (d) ✓. S4a's output differs from σ only at Even vertices moved to Iσ edges (its arena); SPEC's S4b output differs from τ only on Iτ edges;
  a fallback switches the non-empty set {v : (v, ·) ∈ Iσ} (or Iτ), since an iteration needs Iσ ∪ Iτ ≠ ∅; each switched vertex takes ONE edge,
  so every switch is an unambiguous set in R15's sense. R15 (c), (d) (G-N5-TERM-reading §3-§4, re-read l. 83-91) use only that each iteration
  is Switch_I on σ and/or τ with ∅ ≠ I ⊆ Iσ / Iτ and that Iσ, Ξσ (Iτ, Ξτ) are functions of σ (τ) alone. Both hold for N5^τ.
- Corollary ✓ (with N-STAU-1). In-phase ⇒ τ kept ⇒ by (c) a Σ-transition from a τ-stable state, for both rules. At a τ-stable state N5^τ takes
  the Σ-transition, and N5 takes it iff SPEC's S4b returns τ (or Iτ = ∅); otherwise N5 moves to SPEC's τ′ ≠ τ, which is value-optimal too, so
  V_{σ,τ′} = V_{σ,τ} on H′ ("value-equal"). The transfer criterion (a per-phase N5 proof transfers unless it uses more than the listed facts)
  is right: an N5^τ phase is a run of Σ-transitions from τ-stable states, which is all such a proof may assume about an in-phase step.
- Mechanical check (DATA; R2-N5-STAU/stau_check.py, §3): (a)-(d), the converse and the corollary's inclusion at every state of an N5 run and
  of an N5^τ run from the same start: 0 violations on 122,512 states (A, D checks), 92,077 / 92,767 τ-keeping states of N5 / N5^τ (C), and 92,767
  τ-stable states (CONV; equal to N5^τ's τ-keeping count, as (c) and its converse require).

## 2. Audit (CHECKED; not signed)
### 2.1 Audit question (1): is the file list the whole per-phase chain behind R48 (i) and R50 (h)? YES, with completions
- RESULTS closure, by my own means (R2-N5-STAU/audit/closure.py, edges.py over `git show ca0a4e97:docs/RESULTS.md`, every "R<k>" token in each
  "### R<k>" entry, transitively from R48 and R50): the raw closure has 43 entries. Each edge outside the packet's set was read in context. None
  is a citation of a result: "R2" = docs/referee-2/R2-* report names; "R1" = the item label "(R1)" and fix ids OUT-R1, NEB-R1; R58, R63, R71, R72,
  R73 = L-RED document ids (docs/red/R58-n5-width.md, R63 §1b, R71, R72, R73); R47 = R50's not-signed READING only. The other raw entries
  (R36, R51, R54-R57, R60, R61, R76) are reached only through these false edges. After removing them the
  closure is exactly the packet's {R15, R17, R18, R19-R34, R38, R39, R42, R44, R45, R48, R50}. (This agrees with L-COMP's citeclosure.py as the
  Lead relays it; I did not run or read that script.)
- Files named in those 26 entries (audit/files.py; docs/referee*, docs/checker excluded) = the packet's 66 lane files, plus: the SPEC
  (premise), data or remark mentions (docs/lit/T21-VJ00-check.md: R15 side finding; docs/new/N5-brchanges-box11.md: R17 honest limits;
  docs/red/R73-*: R50 data; instance files), and ONE object the packet omits:
  - (i) docs/red/R58-n5-width.md §9, RESULTS R18 object (A) (Proposition X, R18 (a)). It is not used by any proof in the chain: no file of the
    66 cites Proposition X or R18 (a) except N5-1Oacyc-box24.md l. 134 (its own reference list); the chain uses R18 (c) (flat-case analysis)
    and R18 (d) (Lemma R, Lemma S). I read §9 anyway: a locality argument on X (no path to o); no use of S4b's output. Completion, no effect.
- Proof text outside the 66 files that the chain relies on: SIGNED PROOF STEPS WRITTEN BY REFEREES, cited by RESULTS entries and fixes files as
  the closure of a gap in a chain item. The packet's file rule ("object, packet, fixes and proof documents named in those entries") leaves them
  out. I read each:
  - (ii-a) R-N5-X §3.2 "X-1 closure" and R2-N5-X §3.2 "Lemma TF" (RESULTS R21 (i), the R19 (f) note docs/agents/R19-note-X1.md): a θ-change at
    a transition with τ constant, R constant and H1 is an F-change. Uses Lemma S (a), R15 (a), (V1), Lemma G (a), τ constant. Kinds HYP, DEF.
  - (ii-b) R-N5-FB §4.2 CAP-1 closure, R2-N5-FB §5.2 and §C.3, R-N5-OE §2.2 (RESULTS R25 CAP-1; used by R27 TH, R28 OE, R30 OR / ABS-L):
    SPEC's σ̄(o) is a (coarse) minimiser of Ξ over succ(o); statewise (σ̄ is S1 on G, not S4b), plus "λ constant in the phase". Kinds DEF, FIX.
  - (ii-c) R-N5-U1 §3.2 TB-1 and R2-N5-U1 §3.2 G-TB-1 (RESULTS R24 TB; cited by U23, KW, SN WK as "the Bellman form at an arena optimum"):
    S4a's arena optimum only (R17 (F1)). No τ dynamics.
  - (ii-d) R-N5-U1 §C.3 and R2-N5-U1 §C.4, the N-U1-3 closure (RESULTS R24 WC): "an Even fallback from an EQ state with τ unchanged (FIX 3,
    FBL-N (i))" improves σ in G_τ (R15 (a)). Kind FIX.
  None uses S4b's output. With (i) and (ii) added, the list is the whole chain as far as I can determine.
- Lane working texts named as "source" by packets (N5-SCOPE-box36, N5-DROP-box35 §7, N5-OUT-box37, N5-NEB-box38, N5-TAUW-box38, N5-RHO-box39,
  N5-FBPOLY-box41, N5-REL-box34, N5-K-box33, N5-U1T-box31, …; 40 such names found by scanning the 66 files): every packet in the chain says it is
  self-contained, restates and re-proves what it asks to be signed, and governs where it differs (checked at the heads of P-N5-SCOPE, -OUT,
  -NEB, -RHO, -FBPOLY and the "Source text" lines of the others). They are not part of the signed chain; I did not audit them.
- P-N5-RL (R37) and P-N5-NEEDB (R49) are outside the chain (P-N5-OUT l. 25: "P-N5-RL … not used"); the packet's two extra rows on them are
  correct (VAL, holds).

### 2.2 Audit question (2): does any proof use S4b's output implicitly? NO
- Method: my own search, not the lane's list. audit/audit_grep.py (hits in audit/hits66.txt; audit/run_audit.sh regenerates) over the 66 pinned files with a wider pattern than §2.1 of the packet (S4b, Iτ,
  τ_new, τ_{k+1}/τ_{t+1}/…, Odd's step/move/arena/fallback/reply, H′, counterstrategy, τ unchanged/constant/fixed/changes/moves/kept, change
  of τ, leaves/ends the phase, last state of, next/new phase, τ-stable, value-optimal, tie/ties, τ′): 323 hits, each read in context. Second
  pass for uses that need no such word (τ vs σ̄ relations, "honest-optimal", "optimal against σ", "τ minimises", "S1's procedure on H′",
  D = ∅, "τ is optimal"): nothing beyond the first pass. Third pass for whole-run identities ("prefix of", "N5's run on", R17 (b)/(c)/(e),
  Proposition X, Lemma S (b)/(c), Lemma Φ).
- Every use falls in the packet's kinds DEF / FIX / END / HYP / R15 / VAL. No proof uses which optimal counterstrategy S1's procedure returns on
  H′, nor "the phase ended, so S4b returned some τ′ ≠ τ". The only place where S4b's output enters a proof is VAL (N5-1Oacyc-box24 l. 99-103;
  outside the chain, P-N5-RL l. 95-106 and NEEDB (F-a)): there S4b's output is shown to be strictly better than τ at o, so τ is not
  value-optimal and S4b^τ moves τ as SPEC does. ✓
- Phase-end uses (END) re-checked for N5^τ: CN-LAST (P-N5-SCOPE l. 174, 204-208; used by R48 CN-ONLY and FB-POLY (d)): at Iσ_{k+1} = ∅ the
  state is not τ-stable, so by §1 (c) N5^τ does not keep τ (or stops). CLS-1 (P-N5-CLS-fixes l. 10-11), Theorem B (a) (N5-time-box21 l. 102-103),
  P-N5-FB-fixes2 l. 25-26: the same.
- The packet's "phase" key: R19-R25 are signed under (λ_Ξ, λ_U, τ); Remark KEY (R38 (a); λ_U is a function of τ alone) makes this the
  (λ_Ξ, τ)-phase for N5^τ as for N5 (statewise). ✓

### 2.3 Rows checked, and rows the table lacks (all "yes")
- Spot checks of the table against the pinned files (line numbers and content): R17 l. 86; R18 box24 l. 99-103, 119-122; R19 RE l. 12-13, 51, 58;
  R21 X l. 13-14, 64, 76, 170; R23 Z l. 25, 38, 48, 57, 171; R24 U1 l. 16; R25 FB l. 20-21, 45, 149, fixes2 l. 25-32; R26 U23 l. 22; R27 LP
  l. 33-34; R29 CLS-fixes l. 10-11; R31 FBW l. 17-18; R34 TOG l. 18, 104; R38 SCOPE l. 25-28, 91, 204-207; R39 OUT l. 43-46, 82, 84, 110;
  R45 RHO l. 40-41; R48 FBPOLY l. 34-35, 46, 68, 248; R50 KW l. 48. All as stated; the "no hit" rows (R28 OE, R33 L2) also have no hit
  under my wider pattern for S4b-type words (their hits are DEF/FIX phase definitions only).
- Uses not in the table, all of allowed kinds:
  - R17 Lemma P / Theorem PH applied to τ-fixed segments as runs of N5 on the one-player game G_τ: P-N5-X l. 72 (Q-runs, R21), l. 129
    (𝓕, R21); P-N5-NH l. 49 (R22); N5-C-box8 l. 193-203 EQ-STRETCH (R27 object); N5-xing-box27 l. 229-237 (UT). The packet's R17 row
    ("one-player: Iτ = ∅, N5^τ = N5") covers R17 itself, not these transfers. Each needs only that the segment's transitions are S4a arena
    optima and Even switch-alls with τ fixed (and, for EQ-STRETCH, Ξ = W so the gates are G_τ's). Kind FIX: holds for N5^τ by §1 (c).
  - R18 (d) Lemma S (b) (U_τ non-increasing along the run; N5-time-box21 l. 70-71; cited by P-N5-RE l. 23): its proof is R15 (a) on G^d. For
    N5^τ every τ-move is SPEC's S4b output or an Odd switch-all, i.e. a switch of Iτ edges (§1 (d)). Kind R15 (with R15 (a); N-STAU-3).
  - R15 (a) (Ξ non-decreasing) wherever cited (e.g. P-N5-NH l. 25, N5-L-box32 l. 57, N5-C-box8 l. 235): σ-moves of N5^τ are S4a outputs or
    Even switch-alls (§1 (a), (d)). Kind R15.

## 3. Data (DATA, not proof; R2-N5-STAU/, logs/)
- stau_check.py (own; one-step function = succ. 14's R2-N5-EPR/epr_check.step, SELF-checked against succ. 13's SPEC loop
  R2-N5-DUAL/dual_check.Runner on every N5 run; Σ and the switch-all recomputed from the packet's §0). run_all.sh reproduces every log.
| input | runs (N5 + N5^τ) | states | TIEKEEP (transition-level) | N5^τ ≠ N5 (runs) | NONEX (τ-keeping Σ-transitions leaving the phase, N5^τ) | R48 (i) on N5^τ phases (max f, max phase length) | violations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| my 503 𝒞^1O files (R2-N5-KW/files.lst), S3 + 2 random, seed 7 | 1,509 + 1,509 | 45,217 | 92 | 31 | 3,514 | 6,237 phases, f ≤ 37, length ≤ 112 | 0 |
| lib41 without its docs/referee games (lib41_noref.lst, 410; 45 with n > 64 skipped) | 1,095 + 1,095 | 32,477 | 53 | 21 | 2,003 | 3,079 phases (𝒞^1O runs only), f ≤ 33, length ≤ 112 | 0 |
| random 𝒞^1O, 3,000 games, n 5-20, seed 22, S3 + 2 random | 9,000 + 9,000 | 25,002 | 274 | 132 | 5,563 | 19,132 phases, f ≤ 1 | 0 |
| random general games (kind kO), 2,000, n 4-16, seed 31, S3 + 2 random | 6,000 + 6,000 | 19,812 | 271 | 129 | 2,097 | 1,547 phases (𝒞^1O ones) | 0 |
| div_n8 on G (experiments/new/box45/instances/div_n8.pg sha1 4ed57ef2, predecessor's converted start) | 1 + 1 | 4 | 0 | 0 | 0 | — | 0 |
- TIEKEEP here counts states (of both runs) where N5^τ's transition keeps τ while SPEC's S4b moves it; states = all states of both runs.
  Mutations (must fail): ST_MUT=keep (S4b^τ keeps τ whenever Iτ ≠ ∅): 1,574 C violations; ST_MUT=sig (Σ's switch-all takes the smallest-index
  target): 48 C violations. LINK (SPEC's S4b output = τ ⇒ value-optimal in H′, the step N-STAU-2 is about): 45,490 checks, 0 failures.
- Witness for N-STAU-1: instances/nonex_min.pg (n 4, sha1 cd2c60f7…) with nonex_min.start: N5^τ's first transition keeps τ at a τ-stable state
  with Iτ ≠ ∅ and changes λ_Ξ, so it is a Σ-transition that leaves the phase.
- Comparison with the packet's §3 (after my runs): on the same 503 files the maxima agree (f 37, phase length 112); phase counts differ
  slightly (6,237 vs 6,256: different random start pairs). L-COMP (l-comp 16c960b5, read after my runs): its six pinned diverging instances
  (copied to lcomp_pinned/) pass all my checks, 0 violations, and every run differs from SPEC's. Its keep counts 6 / 5 / 3 / 3 / 13 / 13 equal
  mine at STEP level (S4b^τ keeps τ where SPEC's S4b moves it); at TRANSITION level I get 5 / 4 / 2 / 2 / 13 / 13: the difference is exactly the
  keeps at Iσ = ∅, where an Odd fallback follows and τ moves anyway (logs/lcomp_pinned.txt). N-STAU-4.

## 4. The conclusion line (READING; not signed)
My answers are those §4 asks for: (1) yes, with the completions of §2.1 (none uses S4b's output); (2) no. So, on my side, the premise (Στ) of
P-N5-EPR's Corollary EP-1 holds for every per-phase statement in the chain: they hold for every phase of every N5^τ run, because each proof
uses only the facts the §1 Corollary lists. Whether EP-1 becomes unconditional is for the Lead and CHECKER after both reports and the §C.
Nothing here bounds N5's running time on any class beyond 𝒞^1O; G-N5-TIME stays open.

## 5. Notes
| id | where | kind | text |
| --- | --- | --- | --- |
| N-STAU-1 | §1 Corollary, first sentence | wording | "The in-phase transitions of N5 and of N5^τ are exactly Σ-transitions from τ-stable states" holds as an inclusion only: a Σ-transition from a τ-stable state may change λ_Ξ and leave the phase (witness instances/nonex_min.pg; 3,514 such transitions on the 503 files). Read "are Σ-transitions from τ-stable states; the τ-keeping transitions are exactly these". The transfer criterion uses only the inclusion. |
| N-STAU-2 | §1 (b), (c) for N5 | citation | "SPEC's S4b output τ is value-optimal" is 1E-N3 (S1's procedure on H′ returns a counterstrategy whose play values equal the valuation it computes), not Lemma S (a) on H′: Lemma S (a) says that valuation is the pointwise minimum; 1E-N3 says τ attains it. Cite both (the packet lists 1E-N3 as a standing premise, so nothing changes). DATA: LINK 0 failures. |
| N-STAU-3 | §1 (d) | completeness | Name R15 (a) (Lemma A) with (c), (d): the chain uses it for N5^τ through Lemma S (b) (U_τ non-increasing) and wherever Ξ non-decreasing is cited. It transfers by the same property (§2.3). |
| N-STAU-4 | §3 TIEKEEP | definition | "keeps τ although SPEC's S4b would move it" counts S4b^τ's choice (step level, L-COMP's count); at Iσ = ∅ the Odd fallback then moves τ, so the transition does not keep τ. Say which count the table uses. |
| — | §2.1 | audit completion | Add to the file list: docs/red/R58-n5-width.md §9 (R18 object (A); unused) and the referee-written proof steps (ii-a)-(ii-d); add the §2.3 rows (R17 transfers to G_τ, Lemma S (b), R15 (a)). All "yes". |

## Signature
REFEREE-2 (successor 15, Opus 5.5, D15): Lemma Στ-STEP (a), (b), (c), (d) SIGN; Corollary SIGN (wording N-STAU-1). §2 table CHECKED:
audit question (1) YES with the completions above; audit question (2) NO. No gap. §3, §4 not signed.

## §C. Comparison with REFEREE's R-N5-STAU (claude/referee 48674360, successor 13; read after my report 8e42c473 was pushed). Written 2026-10-26 08:4xZ onward by date -u (Opus 5.5, D15)
### C.1 Verdicts, item by item
| item | REFEREE | REFEREE-2 (8e42c473) | outcome |
| --- | --- | --- | --- |
| §1 (a), (b), (c) | SIGNED | SIGN | same |
| §1 (d) | SIGNED, note STAU-N1 (R15 (a) too) | SIGN, note N-STAU-3 (R15 (a) too) | same; STAU-N1 = N-STAU-3, found by both |
| Corollary, transfer clause | SIGNED | SIGN | same |
| Corollary, sentence 1 ("exactly") | SIGNED WITH GAP STAU-1 (i) | note N-STAU-1 (inclusion only; witness nonex_min.pg) | same defect, found by both; REFEREE graded it a gap, I a note. Settled in C.2: GAP |
| Corollary, sentence 2 ("differ only in WHEN a phase ends") | SIGNED WITH GAP STAU-1 (ii): also differ at Iσ = ∅; witness is0_c1o264 | SIGN (missed) | found by REFEREE only; I accept it (C.2) |
| §2 audit (1) | YES, with four entry-named files omitted, none on the chain | YES, with completions: R58 §9 (unused) + referee-written proof steps (ii-a)-(ii-d) | same answer; the completions differ (C.3) |
| §2 audit (2) | NO | NO | same |
| §3, §4 | not signed | not signed | same |
### C.2 STAU-1: gap or note? A GAP (wording), closed by REFEREE's two one-line repairs
- Sentence 2 is FALSE as written, and I missed it. Reproduced on my engine (R2-N5-STAU/instances/is0_c1o264_referee.pg, copied from REFEREE's
  scratch, sha1 b0006099 = REFEREE's): at the canonical start Iσ = ∅, Iτ = {(5,1), (5,10), (5,11)}, τ(5) = 9 value-optimal in H′, SPEC's S4b
  returns τ(5) = 11 (N5 goes there, no fallback); N5^τ keeps τ in S4b^τ and Odd's switch-all sets τ(5) = 10. Different successor states, so
  the runs differ from a state that is not τ-stable. My own data had this case and I did not connect it to sentence 2: in the L-COMP
  reconciliation (§3) the step-level keeps at Iσ = ∅ are exactly it. Count on my inputs (is0_count.py, logs/is0_*.txt; state visits of both
  runs with Iσ = ∅, Iτ ≠ ∅, τ value-optimal, SPEC's output ≠ τ): random 𝒞^1O 86, random general 76, my 503 files 0. The successor states
  differ at only 3 and 1 of them: on these games Odd's switch-all usually picks the same τ′ as SPEC's S4b. So case (ii) is a state where
  the transitions CAN differ.
- Sentence 1 is false as written (my N-STAU-1 = REFEREE's STAU-1 (i); REFEREE adds the N5 direction: at a τ-stable state N5 may move τ, so for
  N5 even the τ-keeping set is a proper subset of the Σ-transitions from τ-stable states; correct).
- Grade. Both sentences are part of the statement to sign, and both are false as written. That is a gap of the "wording" kind with a
  one-line repair, not a note. A note is for a correct statement that is badly cited or worded. I withdraw "note" for N-STAU-1 and sign the
  Corollary's sentences 1-2 WITH GAP STAU-1, as REFEREE does. The transfer clause stays signed without gap: it uses only the inclusion
  "in-phase ⇒ Σ-transition from a τ-stable state", and case (ii) is a phase-ending transition in both runs. (Στ) and §2 are unaffected.
- REFEREE's repair text, checked:
  - "The τ-keeping transitions of N5^τ are exactly the Σ-transitions from τ-stable states; N5's are those among them at which SPEC's S4b
    returns τ; the in-phase ones are the τ-keeping ones with λ unchanged." ✓ by §1 (c) and its converse ("SPEC's S4b returns τ" includes
    Iτ = ∅, where τ_new = τ by S4b's "Else").
  - "N5 and N5^τ make different transitions only (i) at a τ-stable state where SPEC's S4b returns a value-equal τ′ ≠ τ …, and (ii) at a state
    with Iσ = ∅ where SPEC's S4b returns a value-equal τ′ ≠ τ (both leave the phase, N5^τ by Odd's fallback)." ✓ and the list is complete:
    the transitions can differ only where S4b^τ's output ≠ SPEC's, i.e. Iτ ≠ ∅, τ value-optimal, SPEC's output ≠ τ; then Iσ ≠ ∅ is (i) and
    Iσ = ∅ is (ii). τ′ is value-optimal too, so "value-equal" is right. Precision (optional): in (ii) the two successor states may still
    coincide (my counts above).
### C.3 Audit question (1): same answer, different completions
- RESULTS closure: identical sets, the same false tokens excluded (R2-…, (R1)/OUT-R1/NEB-R1, L-RED R58/R63/R71-R73, R47 in R50's reading).
- Omitted entry-named files: REFEREE lists four (SPEC, T21, N5-brchanges-box11, R58 §9); I list the same four (the first three as premise /
  remark mentions, R58 §9 as the one omitted object). Same; = STAU-N2.
- Referee-written proof steps (my (ii-a)-(ii-d): X-1 / Lemma TF, CAP-1, TB-1 / G-TB-1, the N-U1-3 closure): found by me only. They are signed
  closures inside chain items (RESULTS R21 (i), R25, R24) and do not sit in the 66 files. REFEREE's answer covers the lane documents; it does
  not discuss them. Neither of us finds an S4b use in them. I keep them as completions of the list (no effect on the answer).
- One point of detail where I DISAGREE: REFEREE calls N5-1Oacyc-box24 (R18 (c)) "not on the signed chain, harmless over-inclusion". R18 (c)'s
  flat-case analysis (box 24 §3 Step 2 case (b), B1/B2) is cited as a proof step in the chain: P-N5-X l. 23, 65-66, 83, 94, 100 (R21),
  P-N5-XA l. 28 and its fixes l. 35 (R20), P-N5-NH l. 27 (R22), P-N5-X-fixes l. 33. So box 24 is on the chain and the packet is right to list
  it (its rows R18 box24 l. 99-103, 119-122 are then needed too; both hold). Agreed with REFEREE that docs/si/N5-KW-box15.md and
  docs/new/N5-KW-box42.md are not-signed lane proofs (R50 "Not signed"), listed harmlessly. No effect on either answer.
### C.4 Notes
| REFEREE | REFEREE-2 | outcome |
| --- | --- | --- |
| STAU-N1 (R15 (a) in (d)) | N-STAU-3 | same |
| STAU-N2 (four omitted entry-named files) | §2.1 (i) and the premise/remark list | same |
| STAU-N3 (cite R38 (a) KEY for the phase key) | §2.2 last bullet (KEY checked; not raised as a note) | same substance; I accept STAU-N3 as a note |
| (b): "Lemma S (a) on H′ + standing premise" | N-STAU-2 (it is 1E-N3 that makes τ attain the valuation) | same substance (REFEREE's proof cites both); N-STAU-2 is a citation precision for the packet's text, which cites Lemma S (a) only |
| — | N-STAU-4 (TIEKEEP: step vs transition level) | mine only; also explains C.2's counts |
| — | completions (ii-a)-(ii-d) | mine only (C.3) |
### C.5 Data
- Both: 0 failures of (b), (c), (c) for N5, the converse, (d), and R48 (i) on N5^τ phases. lib41 max f 33 on N5^τ phases in both (independent
  engines, same 45 files with n > 64 skipped). REFEREE's NONEX-type count (25,997 visits) and mine (3,514 on the 503 files, more on the random
  samples) both confirm STAU-1 (i). REFEREE's DIFF_IS0 (27 + 17, transitions that differ at Iσ = ∅) matches the kind of my diff_next counts
  (3 + 1 on other samples); REFEREE's samples (k ≤ 4 Odd choice vertices, n 3-10) are not mine, so counts are not compared.
### C.6 Joint gap map
| id | REFEREE | REFEREE-2 | kind | status |
| --- | --- | --- | --- | --- |
| STAU-1 (i) | STAU-1 sentence 1 | N-STAU-1 (upgraded to gap here) | wording (Corollary, sentence 1 false as written) | closed by REFEREE's repair text (C.2), both accept; to be written into a fixes file |
| STAU-1 (ii) | STAU-1 sentence 2 (witness is0_c1o264) | missed; accepted and reproduced here | wording (Corollary, sentence 2 false as written) | closed by REFEREE's repair text (C.2), both accept; to be written into a fixes file |
| audit list | STAU-N2 | §2.1 completions | completeness of §2.1's file list | not a gap: answers unaffected; add R58 §9 (unused), the referee-written proof steps, the §2.3 rows |
Nothing open of substance: (a)-(d) and the transfer clause are signed by both without gap; the Corollary's sentences 1-2 are signed by both
WITH GAP STAU-1, closed by the agreed one-line repairs once they are in a fixes file; both answer the audit questions (1) YES, (2) NO.
### C.7 Final verdicts (Opus 5.5, D15)
Lemma Στ-STEP (a), (b), (c), (d) SIGN; Corollary transfer clause SIGN; Corollary sentences 1-2 SIGN WITH GAP STAU-1 (wording, closed by the
repairs of C.2); §2 CHECKED: (1) YES (with the completions of §2.1 / C.3), (2) NO. Notes N-STAU-2, -3 (= STAU-N1), -4, STAU-N3 accepted.
