# R-N5-CORE: REFEREE report on packet P-N5-CORE (L-SI box 23: EVERY-SWITCH, PHASE-SW, RISE-SW, RISE-GATE-CLEAN, FRESH-RED, FRESH3-COUNT)
Referee: REFEREE (successor 17), Opus 5.5 (owner ruling D15). FIRST referee (Lead brief of 2026-10-28 22:36Z by date -u, STEP 1).
- Object and pin: docs/si/P-N5-CORE-box23.md, sha1 7b66f1bae1a1b675c0fda0af1e5eaabf13f128a0, 111 lines, author L-SI successor 19: the same
  sha1 at l-si 081ae740 (an ancestor of origin/claude/l-si 0ecca76e), at 0ecca76e and on my tree (trunk 4eb5cbfb). Quote base 33f43c20.
- Probe and data runs 2026-10-28T22:50Z-22:59Z; report written 2026-10-28T23:01Z-23:02Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ file on CORE on my tree, on trunk or on origin/claude/referee-2 (path names re-listed in the
  same turn as the fetch, 23:00Z: 0 / 0 / 0 files matching "N5-CORE"; the other "core" hits are counter_core plots and logs, not opened).
  No lane code run or imported (experiments/si/root/corecheck.py, experiments/si/rund/quotecheck.py, si.py, n5.py untouched). D1.
- Premises read against their text at 33f43c20: SPEC S1, S2, S4 (a)-(d), FIX 3 (docs/new/N5-ssi-global.md); RESULTS R15 (a), (d) (l. 625-645),
  R17 (a) (V1) (l. 738), R38 (a) KEY (l. 1825-1826), R56 setting line and (a), (d) (l. 2847-2859), R72's premise (SW) (l. 3768-3769);
  P-N5-FBRED-box44 §0-§1.2 at 3732ab55 (κ, κwt_c, (Aκ), κ-Y-FORM proof); P-N5-GCX-box21 §1 at 02240121 and its fixes file F2 (definition).
- Quotes: all 10 [Q path@commit:lines] passages verbatim in their cited ranges (own checker scratch/flip_quotes.py: QUOTES 10 FAILED 0).
- Tool: scratch/core_probe.py (sha1 be6bb900…, own engine scratch/rl_engine.py written from SPEC S1-S5 + FIX 1-4; checks listed in its
  docstring; MUT 1-6). Logs scratch/core_logs/. Engine agreement with the lane's kill instances: swlin_kill_n26 (given start) has one Even
  vertex with 27 switches in one phase, l121reader_n41 (given start) a 121-transition phase: both as stated in the packet §6.

## Verdicts (sign-off line per item)
| item | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| (C1) EVERY-SWITCH | every in-phase transition changes σ | SIGNED |
| (C2) PHASE-SW | |P| ≤ Σ_w SW_P(w) | SIGNED, with |P| read as the number of TRANSITIONS of P (CORE-N1; the state count reading is false) |
| (C3) RISE-SW | Even switch at w, w off honest cycles at t and t + 1 ⇒ Ξ_{t+1}(w) ▷ Ξ_t(w); Remark; Consequence | SIGNED (all three) |
| (C4) RISE-GATE-CLEAN | clean σ̄ change y1 → y2 at u ⇒ κ_{t+1}(y1) ⪰ κ_t(y1), strict unless κ_{t+1}(y1) = κ_{t+1}(y2); the two closing sentences | SIGNED (the tie clause is NEEDED: CORE-N4) |
| (C5) FRESH-RED | |I| ≤ m_E + NOFRESH(I), with its parenthesis | SIGNED |
| (C6) FRESH3-COUNT | three counts on a global C-interval | SIGNED (in either scope of "interval": CORE-N3) |
| §6 | data pointers, unclean gate changes, FRESH3, DEAD forms, READING | not signed (as the packet says) |
No gap. Notes CORE-N1..N6. Nothing here bounds switches per vertex, Ξ-changes per vertex, return-only transitions or the phase length; not
M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. (C1), (C2) re-derived
- (C1) ✓. One transition = one S4 pass with Iσ ∪ Iτ ≠ ∅ (S4 header; the stop S5 is not a transition). τ_{t+1} = τ_t holds by the DEFINITION
  of a phase (the citation of R38 (a) is not needed for it; R38 (a) is the remark that the (λ_Ξ, τ)-phase is the joint λ-phase). Three cases:
  - no fallback: S4d sets (σ, τ) := (σ_new, τ_new) and S4c did not fire, so (σ_new, τ_new) ≠ (σ, τ); τ_new = τ, so σ_new ≠ σ ✓;
  - fallback with Iσ ≠ ∅: every Even v with an improving edge is set to some w with (v, w) ∈ Iσ, w ≠ σ(v) by S2, at least one such v ✓, and
    τ is not changed (FIX 3) ✓;
  - fallback with Iσ = ∅: then Iτ ≠ ∅ and Odd's switch-all moves τ (S2 on G^d: w ≠ τ(v)), so the transition leaves the phase ✓.
- (C2) ✓ under the reading of CORE-N1: each in-phase transition has at least one Even vertex whose σ changes (C1), so the map transition ↦
  one of its switching vertices shows #transitions ≤ Σ_w SW_P(w).

## 2. (C3) re-derived, step by step
1. y := σ_{t+1}(w) ∈ Iσ_t(w): (SW) ✓ (and directly: S4a's arena gives Even v only {σ(v)} ∪ Iσ-targets; S4c uses Iσ). So Ξ_t(y) ▷ Ξ_t(σ_t w) (S2) ✓.
2. Ξ_{t+1}(y) ⊵ Ξ_t(y): R15 (d) puts every N5 iteration in the scope of R15 (a) (Switch_I, ∅ ≠ I ⊆ Iσ), and Lemma A is pointwise ✓. Ξσ depends
   on σ alone (R15 (d): "Ωσ is against ⊖'s optimal reply, not against τ"), so the packet's "(τ is unchanged in the phase)" is not needed
   either; harmless.
3. Plays avoiding w ✓: S1 defines Ξσ as the valuation under ONE counterstrategy σ̄ optimal at every vertex at once, so every Ξ_t(v) is the value
   of v's honest (σ_t, σ̄_t)-play, and off its cycle Ξ(v) = v ⊕ Ξ(next v): this is R17 (a) (V1) (the packet cites "SPEC S1"; CORE-N2). w off the
   cycle of its own play means w occurs once on it, so the suffix plays from y (at t + 1) and from σ_t(w) (at t) avoid w ✓.
4. Same cycle node c = λ(w) ✓ (λ_Ξ constant on the phase; a suffix play has the same cycle).
5. w ⊕ · is strictly monotone on values of w-free plays with cycle node c ✓: c is fixed, so the S1 order compares the signed weight of P, then ℓ
   in the direction fixed by Ω(c); w ∉ either P (w-free), so adding w (when p′(w) > p′(c)) adds the same term ±2^rank(w) to both weights, and
   ℓ grows by 1 on both. (w ≠ c since c is on the cycle.)
6. Ξ_{t+1}(w) = w ⊕ Ξ_{t+1}(y) ▷ w ⊕ Ξ_t(σ_t w) = Ξ_t(w) ✓ (step 1 + 2 give Ξ_{t+1}(y) ▷ Ξ_t(σ_t w), both w-free).
- Remark ✓ and it matters: y's honest t-play passes through w in 1,585 of the 27,194 checked switches (alt_all; lib1140 3,391 of 40,019), so
  "Ξ_t(y) ▷ Ξ_t(σ_t w), then ⊕" would not be available at t; the packet compares at t + 1 for y, where the play is w-free.
- Consequence ✓: by (C1) map each transition to one switching (w, t); it is counted by XR_P(w) when w is off the honest cycles at t and t + 1
  ((C3): Ξ(w) changes), and by the second term otherwise.

## 3. (C4) re-derived
- Setting ✓: u ∈ Q ∩ U_c, u ≠ c; U_c and c are constant on the phase, so κ-Y-FORM_D applies at t and at t + 1 (u off honest cycles at both).
  κ_t(z) = (signed weight of P(Ξ_t z), s_c·ℓ(Ξ_t z)) with lexicographic order (FBRED §0): a TOTAL order, so "strict unless equal" is meaningful.
- At t: (Aκ) with next_t(u) = σ̄_t(u) = y1 gives κ_t(u) = κwt_c(u) + κ_t(y1); κ-Y-FORM_D gives κ_t(u) = κwt_c(u) + min_{Y^u_t} κ; so κ_t(y1) is the
  minimum and, y2 ∈ Y^u_t, κ_t(y1) ⪯ κ_t(y2) ✓. At t + 1 the same with roles swapped (y1 ∈ Y^u_{t+1}): κ_{t+1}(y2) ⪯ κ_{t+1}(y1) ✓.
- (M2κ) at y2 ∈ Y^u_t ⊆ U_c: κ_t(y2) ⪯ κ_{t+1}(y2) ✓ (= R15 pointwise monotonicity with (M1κ), cycle node c at both ends).
- Chain κ_t(y1) ⪯ κ_t(y2) ⪯ κ_{t+1}(y2) ⪯ κ_{t+1}(y1) ✓; if κ_{t+1}(y2) ≺ κ_{t+1}(y1) the last step is strict ✓. y1 ∈ U_c at both ends, so the
  rise is a Ξ-rise of y1 ((M1κ)) ✓. "Charged by at most the number of Odd u with σ̄_t(u) = y1": a counting remark, true ✓.
- Every step was also checked separately in data: (Aκ) and κ-Y-FORM_D at both ends of every gate change, (M2κ) at y2 (0 failures).

## 4. (C5), (C6) re-derived
- (C5) ✓: an edge is fresh at most once in I (after its fresh transition it is held at a state of I), so fresh transitions ↦ one fresh edge is
  injective into the Even edges. The parenthesis ✓: by (C1) every transition of I has a switching Even vertex, and a non-fresh one is exactly
  one at which every switch goes to an edge held at an earlier state of I. (The bound m_E could be m_E − n_E: edges held at I's first state are
  never fresh. Not needed.)
- (C6) ✓: the first two counts are the (C5) injection for Even edges and for Odd (vertex, option) pairs (an option held at a is never new, so
  ≤ deg(u) − 1 per Odd u). Third: on good transitions A_{t+1} ⊆ A_t in every class, so a vertex leaves A at most once and never returns; each
  strict shrink removes ≥ 1 vertex of ∪_c A_a(U_c), and the classes are disjoint, so ≤ Σ_c |A_a(U_c)| ≤ n ✓. Only "A non-increasing" is used:
  the D-, DD- and Δ-clauses of goodness are not needed (CORE-N3).

## 5. Data, vacuity and thin spots (scratch/core_logs/; 0 failures in every MUT=0 run)
| run | games / runs | in-phase transitions | (C3) checked | (C4) clean / unclean / tie at t+1 / no rise | (C5) intervals | (C6) intervals ph / ff |
| --- | --- | --- | --- | --- | --- | --- |
| alt_all.txt (413 games of root/logs/alt_all.lst, n ≤ 600; given start when valid, best-reward, 1 random) | 413 / 918 | 12,937 | 27,194 | 4,953 / 1,764 / 29 / 2 | 98,053 | 1,891 / 1,874 |
| lib41.txt (lib41, n ≤ 48) | 349 / 698 | 9,059 | 16,958 | 1,126 / 1,561 / 6 / 0 | 72,464 | 1,550 / 1,536 |
| lib1140.txt (fbc_lib.txt, n ≤ 64, br + 2 random) | 1,024 / 3,072 | 22,018 | 40,019 | 3,195 / 3,361 / 41 / 0 | 175,359 | 3,925 / 3,832 |
| rand3000.txt (n 3-14) | 3,000 / 6,000 | 695 | 537 | 37 / 18 / 4 / 0 | 741 | 591 / 475 |
| mut2_rand40k / mut2_rand8k (n 3-9 / 8-18; MUT=2) | 48,000 / 96,000 | 10,492 | 7,682 | 455 / 252 / 96 / 0 | 11,104 | — |
- Premise checks at every state / in-phase transition, 0 failures: (V1) (Ξ = value of the honest play, every vertex), (SW), R15 pointwise
  monotonicity, (C3) steps 1-5 separately (w-freeness of both plays, cycle node c), (Aκ) and κ-Y-FORM_D at both ends, (M2κ) at y2, C6 "A grows".
- Vacuity: every hypothesis is met many times (table). Thin spots: (C3)'s off-cycle hypothesis is NECESSARY in data: Even switches on an honest
  cycle at t or t + 1 with no Ξ(w) rise: alt_all 73 of 128, lib1140 328 of 615, rand40k 2,524 of 3,240. (C4)'s tie clause is NECESSARY: CORE-N4.
- Ranges: max phase length 121 (alt_all, l121reader), max SW per vertex in a phase 48 (alt_all), (C5) max fresh 71 / max NOFRESH 90, (C6) max
  counts 64 / 19 / 42 (alt_all). In every run the bounds hold with room; none is tight in data.

## 6. Mutation controls (scratch/core_logs/mutN*.txt; 4-instance set: swlin_kill_n26, l121reader_n41, nep90_n40, ret14_n48)
| MUT | change | result |
| --- | --- | --- |
| 1 | (C3) demanded of the abandoned option σ_t(w) | BITES: 579 failures (4-instance set) |
| 2 | (C4) demanded strictly (no tie clause) | BITES on alt_all: 2 (nep22f_n64, CORE-N4); does not bite on lib41, rand40k, rand8k |
| 3 | (C1) demanded at the phase-leaving transitions too | BITES: 4 of 52 (τ-only moves, e.g. swlin_kill_n26 given start, transition 48) |
| 4 | (C6) third count over ARBITRARY in-phase intervals (A may grow), bound Σ_c |A_i(U_c)| | does NOT bite (max 17): necessity of goodness not exhibited in data |
| 5 | (C5) fresh measured against I's first state only (injectivity removed) | does NOT bite (max 103 = m_E of l121reader_n41, not above) |
| 6 | (C5) without the NOFRESH term (|I| ≤ m_E) | BITES: 40 failures, l121reader_n41 (phase of 121 transitions, m_E = 103) |
Controls 4 and 5 do not bite; (C5) and (C6) rest on the injections of §4, which I checked by proof; the data are a sanity check only.

## 7. Notes (for the lane's fixes file; none changes a verdict)
- CORE-N1 (definition, (C2) and §3's Consequence): |P| is not defined in the packet, and §1 calls a phase a run of STATES, so |P| literally reads
  as a state count. The proof counts transitions, the reading the downstream count (iterations) needs; RESULTS R51 and R65 report "max phase length
  112" on library runs, and my maximum TRANSITION count on lib1140 is 112 (consistent with that convention, not a proof of it). Under the state count (C2) is FALSE: every one-state phase has |P| = 1 > 0 = Σ SW
  (13,932 of 16,595 phases in lib1140). Wording: "|P| := the number of transitions of P".
- CORE-N2 (citations): (a) the R15 (d) quote stops mid-sentence; the source continues «(on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d)», so the
  quoted part alone reads as "every iteration switches σ", which is (C1)'s content and holds only inside a phase. The packet's use (τ fixed) is
  right. (b) "If v is not on its play's cycle, Ξ(v) = v ⊕ Ξ(next v)" is RESULTS R17 (a) (V1) (as FBRED's (Aκ) says), not a sentence of SPEC S1.
  (c) (C1)'s "τ_{t+1} = τ_t ... (R38 (a))" and (C3)'s "(τ is unchanged in the phase)": the first is the phase definition, the second is not
  needed (Ξσ is independent of τ, R15 (d)).
- CORE-N3 (scope, (C6)): P-N5-GCX defines global C-intervals inside a fallback-free sub-run S (GCX §1, "of S"); CORE §1 drops S. (C6)'s proof
  uses only A non-increasing, so it holds in both scopes; I checked both (ph and ff columns, §5). The table's "premises (all LANDED)" is
  inaccurate for (C6): P-N5-GCX is signed by both referees but not in RESULTS (`grep -c GCX docs/RESULTS.md` = 0 at 4eb5cbfb); only its
  definition is used, so nothing rests on an unlanded claim.
- CORE-N4 (the tie clause of (C4) is needed): nep22f_n64 (sha1 d98de59f…, given start n5-epoch/instances/nep22f_n64.start, sha1 a7ecb00e…),
  transition 8 → 9 (a fallback), class c = 18: u = 9 changes σ̄ 57 → 30 and u = 56 changes 6 → 1, both clean, with κ = (0, 4) at y1 and y2 at t
  and t + 1. So κ(y1) does not rise, and "strictly unless κ_{t+1}(y1) = κ_{t+1}(y2)" cannot be shortened to "strictly". These are the only two
  such cases in my data (alt_all; 0 in lib41, lib1140 and 48,000 random games).
- CORE-N5 (data hygiene, not the packet's): three start files listed in root/logs/alt_all.lst do not fit their games: red/n3/instances/
  comp54_n80.start gives forced Odd vertex 11 (only successor 11) the move 11 → 51 (I used 11); n3cov_lean.start and n3cov_phi.start are
  invalid (move not an edge or missing; I skipped those given starts and ran best-reward + random only).
- CORE-N6 (§6, unsigned, reproduced on my engine): FRESH3 (every σ̄-changing transition of a global C-interval has one of (C6)'s three events)
  fails on 4 of 1,379 such transitions in alt_all (4 of 96 on the 4-instance set, which includes ret14_n48), consistent with the packet's DEAD
  verdict; it holds on all 1,816 (lib41) and 2,851 (lib1140).

## DONE / FINDINGS / NEEDS
- DONE: R-N5-CORE.md (this file), scratch/core_probe.py, scratch/core_logs/ (alt_all, lib41, lib1140, rand3000, mut1-6, mut2_lib41,
  mut2_alt_all, mut2_rand40k, mut2_rand8k).
- FINDINGS: (C1)-(C6) all SIGNED, no gap. CORE-N1: |P| must be the transition count ((C2) false for states). CORE-N4: the (C4) tie clause is
  needed (nep22f_n64, transition 8 → 9, two gates). CORE-N2/N3 citation and scope wording. CORE-N5: three invalid lane start files.
- NEEDS: Lead: route CORE-N1..N5 to L-SI's fixes file (N5 to the owners of experiments/red/n3/instances/) after REFEREE-2 reports; the §C
  word when REFEREE-2's R2-N5-CORE is pushed.
