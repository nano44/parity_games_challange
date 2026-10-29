# N5-PIVOT (box 36): where the carry shape comes from, and why the generic lemmas cannot limit it
L-SI successor 30 (Opus 5.5), D15 / D18, Lead reading L40. Lead's brief 2026-10-29 20:30Z (BOX 36). Working note, unrefereed, not a
TARGET.md claim. G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Setting as in box 34/35 (docs/si/N5-CARX-box34.md, N5-RESET-box35.md): P-changes, MATCHED changes ("resets") and CARRIES of one
  vertex's valuation (Ξ on G for Even, U on G^d for Odd) inside one λ-run (λ^U-run), R85's definitions.
- Tools (experiments/si/odd/): pivot.py (pivots, §1-§2, §4), barrier.py (§3), fg.py (§5). Corpus: odd/sbcg.lst (719 games, S3 start),
  outputs odd/out/pivot_corpus_{E,O}.txt (719 / 719 finished, 0 timeouts), odd/out/fg_corpus.txt. Pinned in si/check.sh «box 36».
- Assumption (stated, D18): the tools' Engine valuations and n5x.trace are faithful to SPEC S1-S5 (cross-checked by earlier boxes:
  si/check.sh xcheck, n5x.trace's own assert against n5.run).

## 1. Lemma INHERIT-λ (PROVED, lane): every P-change in a λ-run is its pivot's, with no generic-case premise
- Statement. Let x have a P-change at t → t + 1 inside a λ-run, c := λ(x). Let p be the first vertex of x's play at t (σ_t and
  σ̄(σ_t) on G) whose successor differs at t + 1 (the PIVOT; it exists and lies strictly before c). Then
  P(Ξ_t x) Δ P(Ξ_{t+1} x) = P(Ξ_t p) Δ P(Ξ_{t+1} p), and x's change is MATCHED iff p's is.
- Proof.
  - The prefix Π = x … p has the same successors at t and t + 1 (choice of p).
  - At t + 1, x's play is Π followed by p's play. If p's new play met Π ∖ {p}, x's play would close a cycle inside Π ∪ (p's play)
    before reaching c, so λ_{t+1}(x) ≠ c: impossible in a λ-run. The same holds at t. So both of p's plays avoid Π ∖ {p}.
  - Hence P(Ξ_s x) = Q ⊔ P(Ξ_s p) for s = t, t + 1, with Q := the vertices of Π ∖ {p} above c. The symmetric differences agree.
  - Both valuations have the same cycle node c, so R_c, pos and w agree, and R85's MATCHED test reads only A ∖ B, B ∖ A and w.
  - If no vertex before c changed successor, x's play to c is unchanged and P(Ξ x) is unchanged: so p exists. □
- This is box 28 §12's Lemma INHERIT with its "generic case" premise discharged on λ-runs. Odd: the same on G^d with U.
- DATA: pivot.py INH_V = 0 on all 1,438 corpus runs (both sides); --mut (compare x with a wrong vertex) fires (270 on fc_3).
- Composition: NM_R(x) and #MAT_R(x) count changes created at pivots on x's play; any bound must bound how often a carry- (reset-)
  creating pivot change lands on x's play.

## 2. Three pivot laws for a carry segment (DEAD)
- A carry segment of x = its carries between two consecutive MATCHED changes in one λ-run.
- DEAD: PIVOT-DISTINCT (the pivots of one segment are distinct). Kill: fc_3 (new/box59/out/fc_3.pg, sha1 9af7ca12), Even side, vertex 1,
  λ-run from 0, t = 25: pivot 3 again. Fails in 186 / 719 (Even) and 40 / 719 (Odd) corpus games.
- DEAD: PIVOT-DEEP (pivot depths strictly increase). Same kill (depth 1 after 1). Fails in 199 (Even) and 47 (Odd) games.
- DEAD: EDGE-DISTINCT (the pivot edges (p, new successor) are distinct; would give ≤ m carries per segment). Kill: fc_3, Even, vertex 4
  is its own pivot and switches 5 → 1 → 5 → 1 → 5 at t 11, 13, 20, 22 (all carries, one segment). Odd side: red/n5inj/instances/
  wide_h16.pg (990ecbcf), vertex 18, t = 9, edge (18, 25). Fails in 107 (Even) and 12 (Odd) games.

## 3. BARRIER-SI (PROVED, lane, by a checked counter-model): the generic lemmas cannot give CARRY-SEG or RESET-LIN
- The lemmas offered for (a) are rule-generic: (F-SW) and (F-MON) hold for every rule that switches along nonempty subsets of Iσ (R86
  packet §1, l. 63-66); SW-RETURN (R86, from F-SW + F-MON), LEN-MONO (R86 §3, from F-MON + λ constant), SUCC-MON and LATE-RISE (L-NEW 35,
  docs/new/N5-STRETCH-box64.md l. 234-239: from [S2] and F-MON; S4a enters only through F-SW), MATCH-Φ (R85: any P-sequence with c
  fixed), INHERIT-λ (§1: any positional plays). READING: their proofs use N5 only through F-SW.
- Counter-model: plain switch-all SI (si.py rule_switch_all, PGSolver start "best", Odd plays σ̄) on PGSolver's switchallexp_N (port
  experiments/hard-families/pgsolver_port.py; N = 6 sha1 equals new/box54/out/switchallexp_6.pg; N = 7 pinned as
  experiments/si/odd/inst/switchallexp_7.pg, sha1 ff46e32f). barrier.py checks F-MON, SUCC-MON, LATE-RISE, SW-RETURN (whole run) on
  every transition: 0 violations for N = 1..7. Every N = 1..7 has ONE λ-run (measured). Control: barrier.py --mut (the run
  reversed) fires F-MON 255, SUCC-MON 166, LATE-RISE 179 on N = 2 (SW-RETURN is reversal-symmetric there and does not fire).
- DATA (exact, barrier.py):

  | N | n | iterations | max PCH (one vertex, one λ-run) | its carries | its MATCHED | longest carry segment |
  | --- | --- | --- | --- | --- | --- | --- |
  | 1 | 21 | 10 | 5 | 4 | 1 | 4 |
  | 2 | 35 | 30 | 18 | 14 | 4 | 10 |
  | 3 | 49 | 70 | 46 | 38 | 8 | 22 |
  | 4 | 63 | 150 | 110 | 94 | 16 | 46 |
  | 5 | 77 | 310 | 238 | 206 | 32 | 94 |
  | 6 | 91 | 630 | 494 | 430 | 64 | 190 |
  | 7 | 105 | 1243 | 984 | 858 | 126 | 375 |

- So on switchallexp_7 vertex 101 has 126 > n = 105 MATCHED changes (RESET-LIN false for switch-all) and a 375 > n − 1 carry segment
  (CARRY-SEG false for switch-all, already at N = 5: 94 > 76). Fits: iterations 10·2^N − 10, MATCHED = 2^N, segment 3·2^N − 2, each
  for N = 2..6; N = 7 falls a little below all three (1243, 126, 375), not examined.
- Conclusion (PROVED, lane, modulo the tools' faithfulness): no proof whose premises are among F-SW, F-MON, λ constant, SW-RETURN,
  LEN-MONO, SUCC-MON, LATE-RISE, MATCH-Φ, INHERIT-λ (or any other fact true of every improving-switch rule) proves CARRY-SEG or
  RESET-LIN, since all of them hold on this run and both conclusions fail. The "even top + odd block below" carry shape is the switch-all
  counter's shape too. The law must use what N5 adds: S4a's choice (Even's best reply to τ within σ ∪ Iσ) and/or Odd's moves.
- Contrast (DATA): N5 on the same games (pivot.py SIDE=E): switchallexp_6 has 12 iterations, top carries 9 (f5); switchallexp_4 8 / 6.
- Composition: answers (a)'s "or find why not" for the listed tools; any route to G-N5-TIME through CARRY-SEG / RESET-LIN must carry an
  S4a-specific step.

## 4. Is the S4a ingredient the τ-changes? No: resets pile up inside one phase (DATA, DEAD)
- pivot.py TQ_MAT: the most MATCHED changes of one vertex inside one τ-constant stretch of a λ-run (= one phase, λ and τ constant).
- DEAD: "≤ C resets per vertex per phase" for small C, hence any charge of resets to τ-changes alone. Kill: rise_thin51_n40 (Even side),
  vertex 0: 29 MATCHED changes in one phase (all 29 of its λ-run's resets; n = 40). Histogram over 719 Even games: 0: 344, 1: 222,
  2: 47, ≥ 3: 106. Odd side max 7 (d_dlc_d3, n = 109).
- So the hard core of RESET-LIN is the frozen-τ dynamics of S4a: σ_{t+1} = Even's optimum against a FIXED τ in G restricted to
  σ_t ∪ Iσ_t (with S4c at a stall). This is the predecessors' frozen-W-phase setting (boxes 29-32), now seen from the P-side.

## 5. The frozen guide alone breaks the counter (DATA); CONJECTURE GUIDE-POLY
- FG(τ) (fg.py): Even's S4a step with τ frozen for the whole run; at a stall (optimum = σ while Iσ ≠ ∅) one switch-all step. It is an
  improving-switch rule, so §3's generic lemmas hold for it.
- DATA (switchallexp, start "best"; τ ∈ first, last, σ̄(σ_0), three random):

  | N | n | switch-all iterations | FG iterations (range over the 6 guides) | FG max MATCHED per vertex per λ-run |
  | --- | --- | --- | --- | --- |
  | 3 | 49 | 70 | 8-28 | 1 |
  | 5 | 77 | 310 | 10-75 | 1 |
  | 7 | 105 | 1243 | 14-142 | 1 |

- CONJECTURE GUIDE-POLY: for every game, every start σ and every fixed Odd strategy τ, FG(τ) stops after poly(n) iterations.
  Corpus kill search (odd/out/fg_corpus.txt, guides first, σ̄(σ_0), rand:1): see §7.
- Composition: GUIDE-POLY (from every start, with N5's S4c in place of the switch-all stall step) bounds every N5 phase's length, i.e.
  the per-phase term of R86 COMPOSE / box 29 W-SPLIT; it does not bound the number of phases (τ-changes), so it is one of two halves.

## 6. Answers to the brief (one line each)
- (a) The arena lemmas (Iσ, SUCC-MON, LATE-RISE, SW-RETURN) cannot limit the carry block: switch-all satisfies all of them and builds
  2^N resets in one λ-run (§3). The limiting lemma must use S4a; inside one phase (§4), where the τ-guide is frozen (§5).
- (b) Neither CARRY-SEG nor RESET-LIN proved. Subclass where both hold in the polynomial form box 35 §2 says suffices: games where
  every Odd vertex has one successor. There τ never changes, σ̄ = τ, each λ-run is one phase, and box 28 Corollary R17-D0 (PROVED,
  lane: σ̄ = τ on a phase ⇒ < n + m transitions) gives PCH_R(x), NM_R(x), #MAT_R(x) < n + m. Not new beyond R17-D0; it shows the
  difficulty is σ̄ ≠ τ. No kill of CARRY-SEG / RESET-LIN for N5 found (box 34/35 data stand).
- (c) INHERIT-λ: exact reduction of x's carries / resets to pivot events on x's play. BARRIER-SI: rules out every rule-generic proof.
  §4: the per-phase core. GUIDE-POLY: would bound phase length (one half of G-N5-TIME together with a phase count).

## 7. FG corpus (DATA; odd/out/fg_corpus.txt, 719 games × 3 guides = 2,157 runs, start "best", 0 timeouts at 90 s, 0 at the cap)
- No kill of GUIDE-POLY: max iterations / n = 2.66 (b6_xl_n32, guide σ̄(σ_0), 85 at n 32); largest absolute 487 (switchbestexp_8,
  guide first, n 210). Max MATCHED per vertex per λ-run / n = 0.59 (x31_cu32, 19 at n 32); never > n. 129 runs have > n iterations.
- Growth on PGSolver's switchbestexp (guide first; not Friedmann's H_n, see experiments/friedmann-hn/hn.py): 20, 62, 107, 157, 220, 296, 385, 487 for N = 1..8 (n = 25N + 10):
  second differences ≈ 13, so about 6.5·N², quadratic in n. Any GUIDE-POLY bound must allow at least quadratic phase lengths;
  ≤ c·n per phase is false for FG on this family at large N (fit, not run beyond N = 8).
- Composition: consistent with box 29's W-SPLIT data (frozen W-phases short in N5); GUIDE-POLY is the clean one-player-guide form of
  that per-phase question, with the stall step as the only extra rule.

## DONE / FINDINGS / NEEDS
- DONE: odd/pivot.py, odd/barrier.py, odd/fg.py, odd/inst/switchallexp_7.pg; corpus runs; check.sh «box 36»; this note.
- FINDINGS:
  1. PROVED (lane): INHERIT-λ (no premise on λ-runs).
  2. DEAD: PIVOT-DISTINCT, PIVOT-DEEP, EDGE-DISTINCT (fc_3; wide_h16).
  3. PROVED (lane, counter-model): BARRIER-SI: switch-all on switchallexp_7 kills RESET-LIN (126 > 105) and CARRY-SEG (375) with all
     generic lemmas holding; a proof needs S4a.
  4. DEAD: charging resets to τ-changes (29 resets in one phase, rise_thin51_n40).
  5. DATA + CONJECTURE GUIDE-POLY: a frozen guide alone defeats Friedmann's switch-all counter (≤ 142 vs 1243 iterations, ≤ 1 reset).
- NEEDS: none from the owner.
