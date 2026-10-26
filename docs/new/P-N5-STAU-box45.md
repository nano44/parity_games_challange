# Packet P-N5-STAU (box 45): N5 and its keep-τ-on-ties variant N5^τ share every in-phase step (Lemma Στ-STEP), and an audit table showing that the per-phase chain behind RESULTS R48 (i) and R50 (h) never uses which optimal counterstrategy S4b returns — every game
L-NEW successor 24 (Opus 5.5), D14 / D18, Lead reading L40; Lead's order 07:11Z (Lead's stamp), item (2): "packet P-N5-STAU, frozen and
self-contained. To sign: Lemma Στ-STEP (§9.1), with its four parts. To check, not to sign: the §9.3 table, as a referee-audited table like
P-N5-DUAL's §2 … The two audit questions go at the top … Not to sign: the §8 data. Conclusion line: if both referees confirm the table, EP-1
becomes unconditional." Written 2026-10-26 07:18Z (date -u). FROZEN at push: later text goes into a fixes file.
Source: docs/new/N5-EPR-box45.md §8, §9 (working doc, l-new d0c6b44b, bcca6c83, a198c9b9; this packet governs).
Labels: PROVED (L-NEW 24, unrefereed) / AUDIT (to check) / DATA. Not a TARGET.md claim; nothing here bounds N5's running time on any class.
G-N5-TIME stays open.

## The two audit questions (for the referees, about §2)
1. Is the file list of §2.1 the WHOLE per-phase chain behind RESULTS R48 (i) and R50 (h)? (Proofs may sit in a document that a packet cites
   but whose RESULTS entry does not name it.)
2. Does any proof in that chain use S4b's OUTPUT implicitly, beyond the kinds of §2.2 (for instance "the phase ended, so S1's procedure on
   S4b's arena returned some τ′ ≠ τ", or a step that needs S1's specific choice among optimal counterstrategies on that arena)?

## To sign, to check, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Lemma Στ-STEP (a)-(d) and its corollary (τ-stable Σ-transitions) | PROVED (to sign) |
| §2 | the audit table: every use of S4b / Iτ / τ_new / "τ unchanged" in the R48 (i) / R50 (h) chains, classified | AUDIT (to check, not to sign) |
| §3 | DATA: N5^τ on 𝒞^1O, and the DIV instance | DATA (not to sign) |
| §4 | conclusion line | READING |
- Premises (LANDED): SPEC S1-S5 of docs/new/N5-ssi-global.md (with FIX 1-4, Q1-Q4), in particular S2 (improving edges), S4a, S4b, S4c (FIX 3:
  an Even fallback leaves τ unchanged; Odd falls back only if Iσ = ∅), S4d; RESULTS R18 (d) Lemma S (a) (S1's valuation is the pointwise
  minimum of V_{σ,τ′} over Odd's strategies; game-general, R56 landing note N-FBRED-3; = (VJ) of RESULTS R57), on the game and on S4b's arena;
  RESULTS R15 (c), (d) (their proof's hypothesis is named in §1 (d)). Standing SPEC premise: S1's procedure returns an optimal
  counterstrategy (1E-N3, R57).
- Context: packet P-N5-EPR (docs/new/P-N5-EPR-box45.md, sha1 8fecca79…, with fixes docs/new/P-N5-EPR-fixes-box45.md, sha1 5af1fde6…) states
  Corollary EP-1 as an implication from premise (Στ): "RESULTS R48 (i) and R50 (h), with the per-phase statements they cite, hold for every
  phase of every N5^τ run on every game of 𝒞^1O from every start pair". This packet is the check of (Στ).

## 0. Setting (every game)
- N5 = SPEC S1-S5. State (σ, τ); Ξ = S1's valuation of σ; W = V_{σ,τ}; Iσ, Iτ (S2; Iτ on G^d); σ_a := S4a's output at (σ, τ) (σ_a := σ if
  Iσ = ∅); S4b's ARENA H′ at (σ, τ): Odd v restricted to {τ(v)} ∪ Iτ(v), Even fixed to σ. A PHASE: a maximal run of consecutive states with
  (λ_Ξ, τ) constant; an IN-PHASE transition has both ends in one phase.
- N5^τ ("keep τ on ties"): N5 with S4b replaced by S4b^τ: if Iτ ≠ ∅ and τ is VALUE-OPTIMAL against σ in H′ (V_{σ,τ} on H′ equals S1's valuation
  on H′ against σ, pointwise), then τ_new := τ; otherwise τ_new := SPEC's S4b output. All other steps are SPEC's. Phases of N5^τ are defined
  as for N5.
- Σ(σ, τ) := σ_a if σ_a ≠ σ, else the result of S4c's Even switch-all on Iσ (defined when Iσ ≠ ∅).
- A state (σ, τ) is τ-STABLE if Iσ ≠ ∅ and (Iτ = ∅ or τ is value-optimal against σ in H′). A Σ-TRANSITION is (σ, τ) → (Σ(σ, τ), τ).
- Why the variant matters (DATA, §3): SPEC's S4b can return a τ′ ≠ τ with the same valuation as τ (a tie inside S1's procedure on H′); N5
  then leaves the phase, N5^τ does not. On 𝒞^1O runs this happens (TIEKEEP, §3), so N5^τ runs are not N5 runs, and the landed per-phase
  results, signed for N5, need a check before they are used for N5^τ.

## 1. Lemma Στ-STEP (PROVED, every game)
For every game and every state (σ, τ):
- (a) N5 and N5^τ compute the same Ξ, W, Iσ, Iτ, the same S4a output σ_a, and the same S4c switch-all (Even's on Iσ, or Odd's on Iτ).
- (b) If N5's transition from (σ, τ) keeps τ, then N5^τ's transition from (σ, τ) is the same transition.
- (c) If N5^τ's transition from (σ, τ) keeps τ, then (σ, τ) is τ-stable and the transition is the Σ-transition (σ, τ) → (Σ(σ, τ), τ). The
  same holds for N5. Conversely, N5^τ's transition from a τ-stable state is the Σ-transition.
- (d) Every N5^τ iteration applies a switch Switch_I with ∅ ≠ I ⊆ Iσ to σ, or with ∅ ≠ I ⊆ Iτ to τ, or both (as every N5 iteration does);
  hence the proofs of RESULTS R15 (c), (d) apply to N5^τ runs.
Proof.
- (a) S4b^τ replaces only S4b's output; Ξ, W, Iσ, Iτ are functions of the state (S1, S2), S4a's output depends on (σ, τ, Iσ) only (its arena
  restricts Even to {σ(v)} ∪ Iσ(v) and Odd to τ), and the S4c switch-alls read Iσ, Iτ, Ξ, Odd's dual valuation and vertex indices.
- (b) N5 keeps τ: τ_{k+1} = τ. An Odd fallback changes τ (S4c: it switches some Odd vertex to an Iτ edge ≠ τ(v)), so none occurred, and S4b's
  output τ_new equals τ (S4d). If Iτ = ∅, S4b^τ also gives τ. If Iτ ≠ ∅, S4b's output τ is S1's counterstrategy on H′, which is optimal there
  (Lemma S (a) on H′: its valuation is the pointwise minimum over H′'s Odd strategies), so τ is value-optimal and S4b^τ gives τ. Then
  σ_new = σ_a in both, and the fallback fires in both iff σ_a = σ (τ_new = τ in both); if it fires it is Even's in both (Odd's would change τ,
  so Iσ ≠ ∅), with the same switch-all ((a)).
- (c) Let N5^τ keep τ. If Iσ = ∅ then σ_a = σ, and either Iτ = ∅ (N5^τ stops: no transition), or S4b^τ moves τ, or S4b^τ keeps τ and the
  fallback fires with Iσ = ∅, which is Odd's and moves τ; all contradict. So Iσ ≠ ∅. If Iτ ≠ ∅, S4b^τ kept τ, so τ is value-optimal in H′ (by the
  rule, or because SPEC's output was τ itself, optimal by Lemma S (a)). So the state is τ-stable. Then σ_new = σ_a; if σ_a ≠ σ the transition is
  (σ_a, τ); if σ_a = σ the fallback fires and is Even's (Iσ ≠ ∅): (Σ(σ, τ), τ). For N5 the same argument applies with "S4b's output is τ" (which
  implies value-optimality). Conversely, at a τ-stable state S4b^τ returns τ (by SPEC if Iτ = ∅, by the rule otherwise), so the transition is the
  Σ-transition by the same case split.
- (d) If σ_a ≠ σ, σ_a differs from σ only at Even vertices moved to an Iσ edge (S4a's arena), so σ_new = Switch_I(σ) with ∅ ≠ I ⊆ Iσ. If S4b^τ
  moves τ, τ_new is SPEC's S4b output, which differs from τ only on Iτ edges (S4b's arena). If neither moves, the fallback switches a non-empty
  subset of Iσ (or of Iτ if Iσ = ∅), since an iteration needs Iσ ∪ Iτ ≠ ∅. R15 (c), (d)'s proof (docs/new/G-N5-TERM-reading.md) uses only this
  property and that Iσ, Ξσ are functions of σ alone and Iτ, Ξτ of τ alone (S1, S2), both true for N5^τ. □
- Corollary (PROVED). The in-phase transitions of N5 and of N5^τ are exactly Σ-transitions from τ-stable states. They differ only in WHEN a
  phase ends: at a τ-stable state where S1's procedure on H′ returns a value-equal τ′ ≠ τ, N5 leaves the phase and N5^τ does not. So a per-phase
  proof for N5 transfers to N5^τ unless it uses, at an in-phase transition, more than: the Σ-transition, τ fixed, τ-stability, the shared
  state functions ((a)), the phase-end facts "Iσ = ∅ ⇒ τ changes or the run stops" ((c)), and R15 (c), (d) ((d)).

## 2. AUDIT (to check, not to sign): the R48 (i) / R50 (h) chain
### 2.1 The chain and the files read
- Citation closure of R48 and R50 in docs/RESULTS.md (the entries R15-R50 that they cite, transitively, by "R<number>" in their text): R15, R17,
  R18, R19-R34, R38, R39, R42, R44, R45, R48, R50; R47 occurs only in R50's not-signed reading (a phase count across phases; not needed).
  P-N5-EPR's (Στ) also listed R49 (spuriously: P-N5-EPR fixes §2); R49 and the R37 step it uses are audited below anyway.
- Files: the object, packet, fixes and proof documents named in those entries (66 files; docs/new/ unless named): G-N5-TERM-reading;
  N5-phase-bound-box10; N5-time-box21, N5-1Oacyc-box24; P-N5-RE-box26, N5-xing-box27; P-N5-XA-box27 + fixes-box28; P-N5-X-box28 + fixes-box29,
  docs/agents/R19-note-X1; P-N5-NH-box30 + fixes; docs/si/P-N5-Z-box5 + fixes; P-N5-U1-box31 + fixes; docs/si/P-N5-FB-box7 + fixes, fixes2;
  P-N5-U23-box31 + fixes; P-N5-LP-box32 + fixes, P-N5-SO-box32 + fixes, N5-L-box32, docs/si/N5-C-box8; P-N5-OE-box32 + fixes;
  docs/si/P-N5-CLS-box8 + fixes, fixes2; P-N5-SN-box33 + fixes; docs/si/P-N5-FBW-box9 + fixes; P-N5-FRZ-box34 + fixes, fixes2; P-N5-L2-box34 +
  fixes, fixes2; P-N5-TOG-box35 + fixes, fixes2; P-N5-SCOPE-box36 + fixes; P-N5-OUT-box37 + fixes; P-N5-NEB-box38 + fixes; N5-RW-box39,
  P-N5-PFZ-box39, P-N5-PFZ-ext-box39, P-N5-PFZ-fixes-box39; P-N5-RHO-box40 + fixes; P-N5-FBPOLY-box41 + fixes, docs/red/R72-fx-fbpoly-k;
  docs/si/P-N5-KW-box15 + addendum + fixes, N5-KW-box42, docs/si/N5-KW-box15. Outside the closure, checked for the R49 remark:
  docs/si/P-N5-RL-box10 (R37), docs/si/P-N5-NEEDB-box13 (R49).
- Search (lane, 2026-10-26 06:52Z-06:56Z by date -u): `grep -n` over the 66 files for S4b, Iτ, I_τ, τ_new, τ′_new, Odd's step, Odd step, Odd fall,
  Odd's fallback, "optimal counterstrategy to σ", "τ unchanged", "fallback fires", "fallback happens", "S4c fires", "τ is unchanged",
  "τ changes", "Odd moves", τ_{k+1} (108 hits); second pass: Odd's move, τ moves, Odd's arena, H′, τ-step, τ step, τ′, Odd switches, Odd
  improves, τ-optimal, "counterstrategy in the arena" (no further use of S4b's output: H′ in docs/si/P-N5-FB-box7 is a functional graph, τ′
  elsewhere is the quantifier of Lemma S (a)). Each hit was read in context.
### 2.2 Kinds of use
- DEF: a restatement of SPEC S4 (true for N5^τ with S4b^τ in place of S4b, by §1 (a)).
- FIX: "in a phase τ_{k+1} = τ_k, so the transition is an S4a step or an Even S4c fallback" (§1 (c)).
- END: "Iσ = ∅ ⇒ τ changes or the run stops" (§1 (c)).
- HYP: "τ_{k+1} = τ_k" used as a hypothesis of a per-transition fact.
- R15: a use of R15 (c), (d) (§1 (d)).
- VAL: a value statement about S4b's output, used to show that τ is NOT value-optimal in H′, so that S4b moves τ (S4b^τ then equals SPEC's S4b
  and moves τ too).
### 2.3 The table
| RESULTS | file: line(s) | the use | kind | holds for N5^τ? |
| --- | --- | --- | --- | --- |
| R15 | G-N5-TERM-reading: 83, 85, 91 | Iσ / Iτ are functions of σ / τ alone; consecutive flat iterations ≤ 4n(n − 1) | DEF, R15 | yes (§1 (a), (d)) |
| R17 | N5-phase-bound-box10: 86 | "N5's fallback fires only when the arena optimum returns σ unchanged although Iσ ≠ ∅" (one-player games) | DEF | yes (one-player: Iτ = ∅, N5^τ = N5) |
| R18 | N5-time-box21: 77, 99-103, 107, 119 | Odd's step minimises V_{σ_k,·} over its arena; Theorem B (a) "τ_{k+1} = τ_k ⇒ σ_{k+1} = F_{τ_k}(σ_k)"; Iσ = ∅ ⇒ τ changes; Iτ_0 = ∅ ⇒ τ never changes; the fallback fires only when the arena optimum is σ_k | DEF, FIX, END | yes |
| R18 | N5-1Oacyc-box24: 99-103 | "(o, a) ∈ Iτ … S4b runs … the value at o under τ′ ⊴ o ⊕ Ξ(a) ◁ o ⊕ Ξ(b). Hence τ′(o) ≠ b, and S4b changes τ" | VAL | yes |
| R18 | N5-1Oacyc-box24: 119-122 | at a pure transition S4b returned τ; S4c fires iff S4a returns σ_k; Iσ_k ≠ ∅ | FIX | yes (§1 (b), (c)) |
| R19 | P-N5-RE-box26: 12-13, 51, 58; N5-xing-box27: 60 | SPEC; hypotheses τ_{k+1} = τ_k; the fallback fires only when S4a's optimum is σ | DEF, HYP | yes |
| R20 | P-N5-XA-box27: 13-14; P-N5-XA-fixes-box28: 49, 140-143 | SPEC; l. 49 describes an OPEN configuration (not a proof step); R15 (d) for value-preserving transitions | DEF, R15 | yes |
| R21 | P-N5-X-box28: 13-14, 21, 64, 76, 170 | SPEC; R15 (d); "S4c step: Even's, since τ is fixed (S4c switches Odd only if Iσ_k = ∅, and then τ changes)"; hypothesis | DEF, R15, FIX, HYP | yes |
| R22 | P-N5-NH-box30: 25 | R15 (a), (d) | R15 | yes |
| R23 | si/P-N5-Z-box5: 25, 38, 48, 57, 171 | "S4c happens iff S4a returns σ_k and S4b returns τ_k"; (F0) with τ_{k+1} = τ_k; FBL-N (i); WM: "τ_{k+1} = τ_k, σ_{k+1} is S4a's choice" | DEF, HYP, FIX | yes (in an N5^τ phase both conditions of the fallback hold) |
| R24 | P-N5-U1-box31: 13, 16; P-N5-U1-fixes-box31: 171 | "inside a phase S4b returns τ"; the fallback is Even's (FIX 3) | DEF, FIX | yes |
| R25 | si/P-N5-FB-box7: 20-21, 45, 149; si/P-N5-FB-fixes2-box7: 25, 27, 32 | SPEC; an Odd fallback changes τ; FIX 3; WM | DEF, FIX, END | yes |
| R26 | P-N5-U23-box31: 22 | "every non-fallback transition is an S4a step: S4b returns τ" | FIX | yes |
| R27 | P-N5-LP-box32: 14, 33-34 | "every N5 iteration changes σ or τ" | DEF | yes (§1 (d)) |
| R28 | P-N5-OE-box32 (+ fixes) | no hit | — | yes (no use) |
| R29 | si/P-N5-CLS-box8: 17; CLS-fixes: 10-11; CLS-fixes2: 10 | "no gate ⇒ σ unchanged ⇒ τ changes ⇒ the phase is left" | END | yes |
| R30 | P-N5-SN-box33: 35; P-N5-SN-fixes-box33: 12, 19 | WM uses only τ_{k+1} = τ_k and the S4a optimum | HYP | yes |
| R31 | si/P-N5-FBW-box9: 17-18 | "an S4c fallback fires exactly when S4a returns σ_k and S4b returns τ_k" | DEF | yes |
| R32 | P-N5-FRZ-box34: 48 | "an in-phase S4c fallback happens only when S4a returned σ_k" | FIX | yes |
| R33 | P-N5-L2-box34 (+ fixes, fixes2) | no hit | — | yes (no use) |
| R34 | P-N5-TOG-box35: 18, 104 | at an Odd fallback σ is unchanged; "τ is constant in a phase, so it is not an Odd fallback" | DEF, FIX | yes |
| R38 | P-N5-SCOPE-box36: 25-28, 91, 204-207 | SPEC; CN-LAST (iii): at Iσ_{k+1} = ∅, N5 stops, or S4b moves τ, or S4b returns τ and Odd falls back; so k + 1 ends the phase | DEF, END | yes (the same three cases for S4b^τ) |
| R39 | P-N5-OUT-box37: 43-46, 82, 84, 110; P-N5-OUT-fixes-box37: 24 | SPEC; FBL-N, ACT premise rows ("τ unchanged"); the fallback is Even's | DEF, FIX | yes |
| R42 | P-N5-NEB-box38: 34-36, 89, 91; P-N5-NEB-fixes-box38: 32 | as R39 | DEF, FIX | yes |
| R44 | P-N5-PFZ-box39: 33, 67-68 (ext, fixes, N5-RW-box39: no hit) | SPEC; premise rows | DEF | yes |
| R45 | P-N5-RHO-box40: 40-41 | "every transition has τ unchanged, so it is an S4a step … or an Even S4c fallback" | FIX | yes |
| R48 | P-N5-FBPOLY-box41: 34-35, 46, 68, 248 | SPEC; in-phase ⇒ S4a or Even fallback; an Odd fallback ends the phase | DEF, FIX | yes |
| R50 | si/P-N5-KW-box15: 48 | "if S4a leaves σ unchanged and S4b leaves τ unchanged, the S4c fallback is Even's" | FIX | yes |
| (R37, outside) | si/P-N5-RL-box10: 95-106 (Lemma BL, Steps 0-1) | "S4b computes τ_new as Odd's optimal counterstrategy to σ_k in H′ … V_{σ_k,τ_new}(o) ⊴ V_{σ_k,x}(o) … so τ_new(o) ≠ e*, and k is not an S4c fallback" | VAL | yes |
| (R49, outside) | si/P-N5-NEEDB-box13: 100 ((F-a)) | "(o, x0) ∉ Iτ_k (BL Step 1)" | VAL (via BL) | yes |
No row uses which optimal counterstrategy S1's procedure returns on H′.

## 3. DATA (not to sign; experiments/new/box45/, outputs in out/)
- n5tau.py runs N5^τ itself on 𝒞^1O games and checks R48 (i) (f ≤ 1 + (n − 2)(2n − 1)) on every N5^τ phase. TIEKEEP counts the iterations
  where N5^τ keeps τ although SPEC's S4b would move it (from there on the N5^τ run is not the N5 run).
| sample | runs | phases | TIEKEEP (phases with one) | R48 (i) violations | max f per phase | max phase length (n) |
| --- | --- | --- | --- | --- | --- | --- |
| REFEREE-2's 503 𝒞^1O files (docs/referee-2/R2-N5-KW/files.lst), S3 + 2 random, seed 7 | 1,509 | 6,256 | 88 (46) | 0 | 37 | 112 (48) |
| lib41's 𝒞^1O games (253), S3 + 2 random, seed 7 | 759 | 3,164 | 29 (16) | 0 | 33 | 112 (48) |
| 5,000 random 𝒞^1O, n 5-20, games seed 22, S3 + 4 random, seed 9 | 25,000 | 61,452 | 613 (560) | 0 | 1 | 5 (15) |
- So N5^τ runs differ from N5 runs on 𝒞^1O, and their phases stay within R48 (i), with the same maxima as N5 in RESULTS R51's data (f 37,
  phase length 112). R50 (h) is not checked here (L-COMP's engine route, Lead 06:48Z).
- DIV (the reason for N5^τ in P-N5-EPR): experiments/new/box45/instances/div_n8.pg (n 8, sha1 4ed57ef2c1c92ee526ccd2683ae7c28b1caf5bfa) with
  div_n8.start: at an in-phase tie state of N5 on G, SPEC's S4b on the restricted game G′_E returns a value-equal τ′ ≠ τ; reproduced on both
  referees' engines (P-N5-EPR fixes §3).
- Reproduce (from experiments/new/box45): `python3 n5tau.py 2 7 --list ../../../docs/referee-2/R2-N5-KW/files.lst`;
  `python3 n5tau.py 2 7 --list ../box41/lib41.txt`; `python3 n5tau.py 4 9 --rand 5000 5 20 22`; `python3 divshow.py instances/div_n8.pg
  instances/div_n8.start`.

## 4. Conclusion line (READING)
If both referees answer the two audit questions "yes, the list is the whole chain" and "no implicit use", i.e. confirm the table, then (Στ) holds
and P-N5-EPR's Corollary EP-1 becomes unconditional: every epoch E with |D_E| = 1 has len(E) ≤ T*(G′_E) + 1 = O(m·Δ·n¹¹) (with the EPR-1
repair). That is to be recorded in the EPR RESULTS entry or a follow-up entry. Until then EP-1 stays an implication.
