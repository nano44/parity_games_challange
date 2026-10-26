# R-N5-STAU: REFEREE report on packet P-N5-STAU (L-NEW box 45: Lemma Στ-STEP, its corollary, and the audit table of the R48 (i) / R50 (h) chain; every game)
Referee: REFEREE (successor 13, session_01Nzrjhmm1pgUnEvdgjCBhTv), Opus 5.5 (owner ruling D15).
- Routing: the Lead's brief of 07:31Z and GO of 07:48Z (Lead's stamps).
- Object: docs/new/P-N5-STAU-box45.md at trunk ca0a4e97, sha1 7446d9a9e198ffa5073e0d43823d753b6aa46b3b (checked with
  `git show 010bfdae:docs/new/P-N5-STAU-box45.md | sha1sum` and on my tree; identical), 158 lines, frozen at l-new 010bfdae. Author: L-NEW successor 24.
- Written 2026-10-26T07:49Z-08:37Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ STAU file opened. No lane code run (experiments/new/box45/n5tau.py, divshow.py; L-COMP's
  citeclosure.py, which the Lead reports equal to the packet's list, was not opened). D1.
- Premises checked against their text: SPEC S1-S5 with FIX 3 (docs/new/N5-ssi-global.md at ca0a4e97, l. 24-60, 88); RESULTS R15 (proof in
  docs/new/G-N5-TERM-reading.md §3, "N5." paragraph); R18 (d) Lemma S (a) (game-general; successor 12's R-N5-1E §1, from VJ00's text).
  Standing premise (1E-N3, R57): S1's procedure returns an optimal counterstrategy, here on S4b's arena H′.
- Tools (own engine; no lane imports; `python3 -I`): scratch/stau_probe.py (N5 and N5^τ step from every state of both runs; checks (b),
  (c), (c) for N5, (c) converse, (d), the Corollary's difference sentence, and R48 (i) on N5^τ phases of 𝒞^1O games), scratch/stau/closure2.py
  (RESULTS citation closure with every excluded match printed). Logs scratch/stau_logs/ (run_all.sh), scratch/stau/closure_R48_R50.txt.

## Verdicts
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 (a) | N5 and N5^τ share Ξ, W, Iσ, Iτ, σ_a and the S4c switch-alls | SIGNED |
| §1 (b) | N5 keeps τ ⇒ N5^τ makes the same transition | SIGNED |
| §1 (c) | N5^τ keeps τ ⇒ τ-stable and Σ-transition (also for N5); τ-stable ⇒ N5^τ's transition is Σ | SIGNED |
| §1 (d) | every N5^τ iteration is a non-empty improving switch of σ and/or τ; R15 (c), (d) apply to N5^τ runs | SIGNED (note STAU-N1: R15 (a) too) |
| §1 Cor. | transfer clause: a per-phase N5 proof transfers to N5^τ unless it uses more than the listed facts | SIGNED |
| §1 Cor. | sentences 1-2: "in-phase transitions … are exactly Σ-transitions from τ-stable states"; "They differ only in WHEN a phase ends: at a τ-stable state …" | SIGNED WITH GAP STAU-1 (both false as written; one-line repairs below; the transfer clause and every use in §2 / P-N5-EPR are unaffected) |
| §2 | audit table | CHECKED: question (1) YES, question (2) NO implicit use (details §2 below) |
| §3, §4 | data, conclusion line | not signed (as briefed); own data in §3 below |
One gap, STAU-1 (wording of the Corollary; witness is0_c1o264). Not a running-time bound, not a TARGET.md claim; G-N5-TIME stays OPEN.
If REFEREE-2 also confirms the table, (Στ) holds as P-N5-EPR states it, and EP-1 is unconditional (with its EPR-1 repair).

## 1. Lemma Στ-STEP
- (a) Ξ, W, Iσ, Iτ are functions of (σ, τ) by S1, S2 ✓. S4a's arena (Even v: {σ(v)} ∪ Iσ(v); Odd v: τ(v)) and S4a's procedure (S1 on its dual
  against τ) depend on (σ, τ, Iσ) only; the SPEC computes S4a and S4b from the SAME (σ, τ) (S4, A6), so S4a never sees S4b's output ✓.
  The S4c switch-alls read Iσ, Ξσ, indices (Even) or Iτ, the dual valuation, indices (Odd) ✓. S4b^τ replaces only S4b's output ✓.
- (b) τ_{k+1} = τ. An Odd fallback (only when Iσ = ∅; then Iτ ≠ ∅ since the iteration needs Iσ ∪ Iτ ≠ ∅) switches every Odd vertex with
  an Iτ edge to an Iτ target ≠ τ(v), so it did not occur; hence S4b's output is τ (S4d) ✓. If Iτ ≠ ∅, S4b's output τ is S1's
  counterstrategy on H′, whose valuation is the pointwise minimum over H′'s Odd strategies (Lemma S (a) on H′ + standing premise), so τ is
  value-optimal and S4b^τ returns τ ✓; if Iτ = ∅ both return τ ✓. Same σ_a ((a)), same fallback condition σ_a = σ, same (Even's) switch-all ✓.
- (c) N5^τ keeps τ. Iσ = ∅ is impossible: then σ_a = σ, and Iτ = ∅ stops the run (S5), S4b^τ moving τ changes τ, and S4b^τ keeping τ fires
  Odd's fallback, which moves τ ✓. If Iτ ≠ ∅: S4b^τ returned τ either by the rule (τ value-optimal) or as SPEC's output (value-optimal by
  the standing premise) ✓. So the state is τ-stable, and the transition is (σ_a, τ) if σ_a ≠ σ, else Even's switch-all ✓ = Σ. For N5 the
  same with "S4b's output is τ" ✓. Converse: at a τ-stable state S4b^τ returns τ (Iτ = ∅: H′ gives Odd only τ; else the rule), and the
  same case split gives Σ (Iσ ≠ ∅ makes a fallback Even's) ✓.
- (d) σ_a ≠ σ: σ_a(v) ∈ {σ(v)} ∪ Iσ(v), so σ_a = Switch_I(σ), ∅ ≠ I ⊆ Iσ ✓; a moved τ is SPEC's S4b output, a strategy of H′, so it is
  Switch_J(τ), ∅ ≠ J ⊆ Iτ ✓; otherwise the fallback switches every vertex of one non-empty improving set ✓. R15's proof (G-N5-TERM-reading
  §3: Lemma A, Lemma B, Theorem; "N5." paragraph) uses exactly: each iteration's σ is σ or a non-empty improving switch of σ, the same for τ
  on G^d, at least one changes, and Iσ, Ξσ (Iτ, Ξτ) are functions of σ (τ) alone ✓. So R15 (c), (d) hold for N5^τ ✓.
  - STAU-N1 (note): R15 (a) (Ξ non-decreasing; Lemma A per switch) transfers by the same property; the table's R22 row cites "R15 (a), (d)"
    and rests on this.
- Corollary, transfer clause: SIGNED. The listed facts are what (a)-(d) give; my §2 check found no proof in the chain that uses more.
- Corollary, sentences 1-2: GAP STAU-1 (wording; the claim used downstream is unaffected).
  - "The in-phase transitions … are exactly Σ-transitions from τ-stable states." In-phase also needs λ unchanged: a Σ-transition from a
    τ-stable state can change λ_Ξ and end the phase (my data: 25,997 state visits, on N5 and N5^τ runs of the 𝒞^1O sample, whose N5^τ transition keeps τ and changes λ_Ξ).
    For N5 the converse direction fails too: at a τ-stable state SPEC's S4b can return a value-equal τ′ ≠ τ (the packet's own point).
  - "They differ only in WHEN a phase ends: at a τ-stable state where S1's procedure on H′ returns a value-equal τ′ ≠ τ …". FALSE as
    written: they also differ at states with Iσ = ∅ (not τ-stable), where τ is value-optimal in H′ and SPEC's S4b returns τ′ ≠ τ. N5 goes to
    (σ, τ′); N5^τ keeps τ in S4b^τ, so Odd's S4c fallback fires and switches every Iτ vertex to its best dual target. Both leave the phase,
    to DIFFERENT states, so the runs differ after that point.
    - Witness: scratch/stau_inputs/is0_c1o264.pg (sha1 b0006099716e5c57932c0ce7f334ae3750ff9188; n 12, 𝒞^1O, o = 5 with succ {1, 9, 10, 11},
      Ω(5) = 22 the top priority, so o is its own cycle node and every choice at o has value (5, ∅, 0)). From the canonical start
      (best-reward): Iσ = ∅, Iτ = {(5,1), (5,10), (5,11)}, τ(5) = 9 value-optimal in H′; SPEC's S4b returns τ(5) = 11 (N5), N5^τ falls back
      to τ(5) = 10. Reproduce: `RANDSTARTS=0 python3 -I stau_probe.py stau_inputs/is0_c1o264.pg` (DIFF_IS0 2: the same state on both runs).
      In the samples: DIFF_IS0 44 (27 + 17 + 0) (all at Iσ = ∅); every other A ≠ B is the Corollary's τ-stable case (DIFF_TS 4,761); DIFF_OTHER 0.
  - Repair (one line each): "The τ-keeping transitions of N5^τ are exactly the Σ-transitions from τ-stable states; N5's are those among
    them at which SPEC's S4b returns τ; the in-phase ones are the τ-keeping ones with λ unchanged." and "N5 and N5^τ make different
    transitions only (i) at a τ-stable state where SPEC's S4b returns a value-equal τ′ ≠ τ (N5 leaves the phase, N5^τ need not), and (ii) at
    a state with Iσ = ∅ where SPEC's S4b returns a value-equal τ′ ≠ τ (both leave the phase, N5^τ by Odd's fallback)."
  - Effect: none on (a)-(d), on the transfer clause, on §2, or on P-N5-EPR: (Στ) concerns phases of N5^τ runs, case (ii) is a
    phase-ending transition in both runs, and every τ-change of N5^τ is still an improving switch ((d)).

## 2. AUDIT (CHECK, not signed): the two questions
### Question (1): is the §2.1 list the whole per-phase chain of R48 (i) and R50 (h)? YES.
- RESULTS level, by my own tool (scratch/stau/closure2.py over RESULTS.md at ca0a4e97, every "R<k>" in an entry's text, transitively,
  each excluded match printed in closure_R48_R50.txt and read): the true closure is R15, R17, R18, R19-R34, R38, R39, R42, R44, R45, R48,
  R50, plus R47 only in R50's "Not signed" reading. This is the packet's list exactly.
  - Excluded matches, all read: REFEREE-2 document names (R2-N5-…, "R2 §C2.3", "R2's §1.3"), L-RED item numbers (R58, R63, R71, R72, R73:
    "L-RED R71", docs/red/R72-…), labels ("OUT-R1", "NEB-R1", "(R1)" as a check name in R22 / R26). Range starts such as "R19-R22",
    "R27-R30", "R28-R34" are real citations; all their members are in the closure. Forward pointers inside R18 (L-RED R58) and R22 (L-RED
    R63) are L-RED items, not RESULTS entries.
  - R18 is used only through (d) (Lemma R, Lemma S (a)-(b); R50's premise list "R18 (d)") and through R31 (a)'s remark on G-1OA-6. R50's
    premise list (RESULTS l. 2507) is "R15, R17, R18 (d), R19, R21 (a) XW, R22, R23 (g), R24, R26, R27, R30 (c), R34 (e), (f), R38 (a)".
- File level: the documents named in those entries are the packet's 66 files plus four it omits; none of the four carries a proof step of
  the chain:
  - docs/new/N5-ssi-global.md (the SPEC; a premise);
  - docs/lit/T21-VJ00-check.md (R15's literature side finding; R15's proof is G-N5-TERM-reading);
  - docs/new/N5-brchanges-box11.md (R17 "Honest limits" only: three false invariants);
  - docs/red/R58-n5-width.md §9 (R18 (a) Proposition X; no entry of the closure cites R18 (a)).
  The packet also lists files that are not on the signed chain (N5-1Oacyc-box24 = R18 (c); docs/si/N5-KW-box15 and N5-KW-box42 = R50 §11
  lane proofs "neither is to sign"); harmless over-inclusion.
- Second level (documents cited INSIDE the 66 files; 50 names): each is a superseded working source ("this packet governs"), a data or
  work-log pointer, an attribution, or a later packet. I read every proof-adjacent one: κ_w-freeze (P-N5-U1-box31 §1: proof restated in
  place, pointer N5-U1-box30), MONO (P-N5-FB-box7: proof in place, pointer docs/si/N5-C-box5 §6.2), (F1)/(F2) (N5-phase-bound-box10: VJ00 §5,
  pointer N5-K10-box8 Lemma F), CN-LAST (P-N5-SCOPE-box36 restates N5-DROP-box35 §7 with "(filled in)" steps), P-N5-OUT-box37 l. 25
  ("P-N5-RL … not used"). N5-KW-box42 cites P-N5-NH-box42 (R53) for its own assembly, but that file is a not-signed lane proof (P-N5-KW §11);
  the signed Corollary PHASE (P-N5-KW §8) cites only R19 (a), (d), R22 (a), R24 (e), R27 (a), (d), (g), R30 (c), R34 (e), (f) and Theorem RUN:
  inside the closure ✓. P-N5-KW l. 296 states Lemma SW (b)'s fact with "it is not cited" and proves it in place ✓.
- Scope of my reading: the RESULTS closure, all 66 files by search (below), and the proofs named above line by line. I did not re-read every
  proof of the 66 files in full (10,307 lines); question (2) rests on the search plus the targeted reading.
### Question (2): does any proof in the chain use S4b's output implicitly, beyond the kinds of §2.2? NO.
- What would be an implicit use. At an in-phase N5 state, τ is SPEC's S4b output on H′ (when Iτ ≠ ∅); at an in-phase N5^τ state it is
  only value-optimal there. So the one property N5 has and N5^τ lacks is "τ is S1's CHOICE among the H′-optimal strategies" (its tie-breaks:
  smallest index / BFS discovery / FIX-2 DFS at a cycle node). A proof that used it, or anything about "which" optimal τ, would not transfer.
- My search (own term list, wider than the lane's): the lane's terms (S4b, Iτ, I_τ, τ_new, "τ unchanged", "fallback fires", Odd's step /
  fallback / move, τ changes / moves, τ_{k+1}: 108 hits, the same count as the packet's) plus "H'" (ASCII prime: SPEC writes H', the lane
  searched H′; 14 hits, none is S4b's arena), "S1's procedure", "counterstrateg", "best repl/response", "optimal against / to σ / for Odd",
  "Odd's optimal", "returns / returned / leaves / keeps τ", "value-optimal", "τ-optimal", "DFS", "smallest index", "first successor",
  "larger index", "tie", and every "τ(o)" line with index / FIX / DFS / tie / first / choice / optimal / minimi / best (hits in
  scratch/stau/hits_mine.txt (108) and hits_extended.txt (172), read in context).
  - Every tie-break hit concerns S4a's choice (Lemma TB, P-N5-U1-box31 §2 / P-N5-U23-box31 / P-N5-KW-box15 §5: Even's arena tie-break,
    shared by N5 and N5^τ at the same state by (a)) or σ̄ (Odd's honest counterstrategy in G_σ, S1 on the GAME, the same in N5 and N5^τ: e.g. P-N5-SO-box32 l. 34-37
    Lemma SO via R24 Lemma R; docs/si/P-N5-FB-fixes(2)-box7 CAP-1 at σ̄'s FIX-2 choice) or S4a (P-N5-U1-box31 l. 63; R24 Lemma TB). None
    concerns τ.
  - The two main proof files: P-N5-FBPOLY-box41 (R48 (i)) uses τ only as a fixed strategy of the phase (l. 42-46, 100, 134) and τ′ only as
    Lemma S (a)'s quantifier (l. 154-156); P-N5-KW-box15 (R50 (h)) the same (l. 47-61, 77, 133, 166, 295, 302, 337).
  - VAL rows (N5-1Oacyc-box24 l. 99-103; si/P-N5-RL-box10 Step 1; NEEDB (F-a) via BL Step 1) argue that τ is NOT value-optimal, from a
    strict value inequality; then S4b^τ = SPEC's S4b, and its output is the same τ′ ✓.
  - END rows: SCOPE l. 204-207 (CN-LAST (iii)) reads the same three cases with S4b^τ ✓ (= §1 (c)).
  - HYP / FIX / DEF rows: re-read at the cited lines; each uses only τ_{k+1} = τ_k, the S4a optimum, or SPEC's definition ✓.
- Quotes in the §2.3 table checked by script against the cited files: 7 of 18 match verbatim; 9 differ only by case ("Inside" /
  "inside"), prime (τ' / τ′), omitted words ("S4b (Odd's step) returns τ_k"; R21 "S4c step k → k+1: …, since τ is fixed and τ_{k+1} = τ_k"), or symbolic paraphrase (R18 "Theorem B (a)") ✓;
  two cite files outside the 66 (P-N5-RL-box10, P-N5-NEEDB-box13), read directly ✓.
- VERDICT (CHECK): the table is correct; to question (1) YES (with the four omitted files above, none on the chain), to question (2) NO.

## 3. Own data (DATA, not signed; scratch/stau_logs/)
Own engine (rl_engine, SPEC from the text), N5^τ with S4b^τ as defined in the packet §0; at EVERY state of the N5 run and of the N5^τ run
from each start: (b), (c), (c) for N5 (C1N), (c) converse, (d), the Corollary's difference sentence; on 𝒞^1O games R48 (i) on every N5^τ
phase (in-phase fallbacks f ≤ 1 + (n − 2)(2n − 1)) and "every in-phase N5^τ transition is Σ" (INPH_NOT_SIG).
| sample | runs | states | (b) / (c) / (c) N5 / (c) conv. / (d) checks | failures | DIFF_TS | DIFF_IS0 | N5^τ phases (𝒞^1O) | max f | TIEKEEP in-phase |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| random games, n 3-10, k ≤ min(4, n − 1) Odd choice vertices, 20,000 games, seed 7, canonical + 3 random starts | 80,000 | 224,169 | 99,423 / 103,300 / 99,423 / 103,300 / 224,169 | 0 | 3,877 | 27 | 38,051 | 1 | 74 |
| random 𝒞^1O, n 5-20, 5,000 games, seed 22, canonical + 3 random starts | 20,000 | 62,777 | 35,438 / 36,271 / 35,438 / 36,271 / 62,777 | 0 | 833 | 17 | 46,404 | 1 | 89 |
| lib41 (412 files, rho_probe.lib(); 45 with n > 64 SKIPPED), canonical + 2 random starts (seeded by relative path) | 1,101 | 32,443 | 28,056 / 28,107 / 28,056 / 28,107 / 32,443 | 0 | 51 | 0 | 3,110 | 33 | 16 |
- "failures" = B, C1, C1N, C2, D, DIFF_OTHER, INPH_NOT_SIG and R48 all 0. Counts are state VISITS (a state on both runs counts twice).
- DIFF_IS0 (STAU-1's case (ii)) occurs on 𝒞^1O too (17); it is never a τ-stable state.
- lib41's max f = 33 on N5^τ phases equals the packet's lib41 row (33); I did not run its REFEREE-2 file list or its §3 seeds.
- Reproduce: scratch/stau_logs/run_all.sh (from docs/referee/scratch/); logs rand20000_n3-10_k4_s7.txt, c1o5000_n5-20_s22.txt, lib41_rs2.txt,
  is0_c1o264.txt.

## 4. Notes for the author (not gaps)
- STAU-N1: §1 (d) could name R15 (a) as well (used by the R22 row).
- STAU-N2: §2.1's file list omits the four entry-named files of §2 (1) above; say why (not on the chain).
- STAU-N3: §0's "PHASE: maximal run with (λ_Ξ, τ) constant" is the joint λ-phase of R38 (a) KEY; worth citing, since R19-R25 were signed
  under the key (λ_Ξ, λ_U, τ) (P-N5-SN-box33 l. 35) and λ_U is constant when τ is.

DONE (REFEREE successor 13, (Opus 5.5, D15)).
