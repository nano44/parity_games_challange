# R-N5-COMPOSE: REFEREE report on packet P-N5-COMPOSE (L-SI box 28): Lemmas SW-RETURN, LEN-MONO, Theorem COMPOSE, Corollaries COMPOSE-RUN, COMPOSE-NM
Referee: REFEREE (successor 18), Opus 5.5 (owner ruling D15). FIRST referee (Lead brief 2026-10-29 12:14Z by date -u).
- Object and pin: docs/si/P-N5-COMPOSE-box28.md at claude/l-si 3ca0932d (an ancestor of my HEAD), `git show 3ca0932d:<path> | sha1sum` =
  e1b977aa9cf1583d5e0c442a8f87d024230b6524, 141 lines: equal to the Lead's figures. Fixes go to docs/si/P-N5-COMPOSE-fixes-box28.md.
- Runs 2026-10-29T12:28Z-12:51Z; report written 2026-10-29T12:50Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independence: REFEREE-2's COMPOSE files exist on my tree after the trunk merge (14 names matching "compose" under docs/referee-2/, 12:40Z;
  names only). None opened.
- Premises opened at the quoted commits: SPEC S1, S2, S4a-c (docs/new/N5-ssi-global.md @ b025560c9), RESULTS R15 (a), (d) (l. 631, 640-642),
  R47 (l. 2322-2345: (c) is item (c) of "(a) Lemma Φ (every game)"), R84 (a) DELTA, P-N5-MPGS (A) @ a23179b0 l. 97-105.
- Scope (D1): a REDUCTION of N5's iteration count to per-vertex path-set-change counts (P*, P*^U), and with [MΦ] to carry counts NM*. Nothing
  here bounds P* or NM*. Not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays OPEN.

## Verdicts
| § | item | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | setting, symbols, (F-SW), (F-MON) | CHECKED (F-SW and F-MON are correct consequences of S4a-c, [STEP], [MON]; |𝒫| is not defined: COMP-E1) |
| §2 | Lemma SW-RETURN (any stretch, both players) | SIGNED |
| §3 | Lemma LEN-MONO (any λ-run / λ^U-run) | SIGNED |
| §4 | Theorem COMPOSE (λ-run sums; phase part) | SIGNED, with |𝒫| read as the number of transitions inside 𝒫 (COMP-E1: under the "number of states" reading the phase part is FALSE) |
| §5 | Corollary COMPOSE-RUN (every run, every game), including the classification and the fallback paragraph | SIGNED |
| §6 | Corollary COMPOSE-NM (implication only) | SIGNED as an implication; its premise "[MΦ] on λ-runs" HOLDS (§6 below: MΦ's proof reads verbatim with c fixed; my predecessor's R-N5-MPGS §1b agrees), so the conclusion holds with [MΦ] as signed by both referees |
| §7 | data, pinned checks | DATA, not signed; reproduced EXACTLY (below) |
No gap in the mathematics. One E-item (COMP-E1, a missing definition). Notes COMP-N1..N6.

## 1. Setting and the two facts
- (F-SW) ✓. S4a: σ_new is a strategy of H, where Even v keeps only edges to A(v) = {σ(v)} ∪ Iσ(v); so a changed σ_new(v) is an Iσ-target. S4b the
  same for τ in H′. S4c: the fallback sets v to a w with (v, w) ∈ Iσ (resp. Iτ). All three steps compute from the same source state t.
- (F-MON) ✓. If σ changes, the changed vertices with their new targets form I ⊆ Iσ_t, one edge per vertex (unambiguous), σ_{t+1} = Switch_I(σ_t)
  ([STEP]), and [MON] gives Ξ_t ⊴ Ξ_{t+1} pointwise. If σ does not change, Ξ_{t+1} = Ξ_t (Ξ depends on σ alone, [STEP]). The Odd side is [MON] on
  G^d (a parity game with the same ranks, priorities + 1; VJ00 needs no restriction), with [STEP]'s Odd clause; U depends on τ alone.
- COMP-E1 (E-item). |𝒫| (§4) is used but never defined. It must be the number of TRANSITIONS t → t + 1 with t, t + 1 ∈ 𝒫 (compose.py's L = j − i).
  Read as the number of STATES the phase part is FALSE: a one-state phase gives 1 ≤ 0, and phases with L = Σ_v SW_𝒫(v) exist (my data: PH_eq
  247 phases on the library, 844 on random games, e.g. every one-transition phase with one switch). One clause in the fixes file.

## 2. Lemma SW-RETURN: re-derived
- Ξ-SUCC ✓: no switch: Ξ_{t+1}(σ_t v) ⊵ Ξ_t(σ_t v) by F-MON; switch to w: Ξ_{t+1}(w) ⊵ Ξ_t(w) ▷ Ξ_t(σ_t v) by F-MON, F-SW and [S2].
- The chain ✓, link by link: Ξ_{e′}(c) ▷ Ξ_{e′}(σ_{e′} v) is [S2] for the switch v → c at e′ (F-SW); ⊵ Ξ_{s+1}(σ_{s+1} v) is Ξ-SUCC (s + 1 ≤ e′);
  ⊵ Ξ_s(σ_{s+1} v) is F-MON; ▷ Ξ_s(c) is [S2] for the switch away from σ_s(v) = c at s; ⊵ Ξ_{e+1}(c) is F-MON (s ≥ e + 1). Since ⊴ is a total
  preorder on keys, Ξ_{e′}(c) ▷ Ξ_{e+1}(c), so Ξ(c) changes at some transition u with e + 1 ≤ u < e′, inside R (e, e′ + 1 ∈ R).
- The intervals [e + 1, e′ − 1] of successive entries are disjoint, so k entries need k − 1 distinct changes: ENT_R(v, c) ≤ 1 + RISE_R(c). ✓
- No phase, no λ, no τ used: it holds on ANY stretch of consecutive states, fallbacks included. Odd side: the same on G^d with U, τ, Iτ. ✓

## 3. Lemma LEN-MONO: re-derived
- On a λ-run the cycle node c₀ of Ξ_t(c) is fixed, so the reward ties and [S1-ord] compares weight(P), then ℓ. By F-MON Ξ_t(c) never falls; at a
  P-change the weights differ (DELTA), so the weight strictly rises; elsewhere it is constant. So each P-value is one contiguous block (it cannot
  recur after a strict rise), PCH + 1 blocks.
- Inside a block a change is a change of ℓ alone, strictly in [S1-ord]'s preferred direction for Ω(c₀) (shorter if even, longer if odd), and
  ℓ ∈ {0, …, n − 1} (steps to the first visit of c₀ along a lasso on ≤ n vertices). So ≤ n − 1 changes per block. ✓
- RISE_R(c) ≤ PCH + (PCH + 1)(n − 1) = n·PCH + n − 1. ✓ Dually on λ^U-runs on G^d (ℓ's preferred direction flips with c₀'s G^d parity).

## 4. Theorem COMPOSE
- Σ_v SW_R(v) = Σ_v Σ_{c ∈ succ(v)} ENT_R(v, c) ≤ Σ_{(v, c), SW_R(v) > 0} (1 + RISE_R(c)) (SW-RETURN; terms with ENT = 0 only enlarge the sum)
  ≤ Σ n(PCH_R(c) + 1) (LEN-MONO: 1 + n·PCH + n − 1) ≤ m_E·n·(P*_R + 1). ✓
- Phase part ✓ (with COMP-E1): in a phase τ is constant, so by [STEP] every transition inside it changes σ, i.e. holds an Even switch; a phase lies
  inside one λ-run, so LEN-MONO applies to it (cycle nodes fixed), and SW-RETURN applies to any stretch.

## 5. Corollary COMPOSE-RUN: the three points the Lead pressed
- (1) The λ-run counts. RESULTS R47 l. 2336-2340: "(a) Lemma Φ (every game): (a) reward(λ_{k+1}(v)) ≥ reward(λ_k(v)) … with equality iff …;
  (b) …; (c) along a run at most n(n − 1) transitions change λ and at most n(n − 1) change λ^U". Item (c) is part of the every-game Lemma, not of
  Corollary Φ-1O (R47 (b), 𝒞^1O). Its content is elementary from (a), (b): reward is injective, so each vertex's λ changes ≤ n − 1 times, and
  each λ-changing transition changes some vertex. The packet uses only the two separate counts, never the joint 2n(n − 1) + 1, R47 (b) or R48. ✓
  So ≤ n(n − 1) + 1 λ-runs and ≤ n(n − 1) + 1 λ^U-runs (maximal runs between changing transitions). ✓
- (2) The classification, fallbacks included. First applicable of (i) λ changes, (ii) σ changes, (iii) λ^U changes, (iv) rest. In (ii) λ is
  unchanged so t, t + 1 lie in one λ-run and some Even vertex switches; in (iv) σ, λ, λ^U are unchanged, so by [STEP] τ changes and t, t + 1 lie
  in one λ^U-run with an Odd switch. Each switch is counted once, in one run. Every transition lands in exactly one kind. ✓
  Fallbacks: an Even fallback (S4c with Iσ ≠ ∅) changes σ (every Even v with an improving edge moves to w ≠ σ(v)) and not τ (S4c reached only
  when τ_new = τ): kind (i) or (ii). An Odd fallback (Iσ = ∅) changes τ, not σ: kind (iii) or (iv). ✓ A transition where S4a runs but leaves σ
  unchanged and S4b changes τ is (i), (iii) or (iv): the classification is by what changes, not by which step ran, so it is covered. ✓
- (3) MATCH-Φ on λ-runs: §6.
- Arithmetic ✓: T = #(i) + #(ii) + #(iii) + #(iv) ≤ 2n(n − 1) + Σ_R Σ_v SW_R + Σ_{R′} Σ_{Odd v} SW_{R′}, and Theorem COMPOSE on each run with P*_R ≤ P*
  gives the closed form.
- COMP-N1 (wording): the title's formula uses P*^U but the title defines only P*.

## 6. Corollary COMPOSE-NM and the MATCH-Φ transfer to λ-runs
- The implication ✓: K ≤ n − 1 gives K(K + 1)/2 ≤ n(n − 1)/2 ≤ n²/2; substitute in COMPOSE-RUN: a polynomial in n, m_E, m_O, NM*.
- The transfer (re-read independently of R-N5-MPGS §1b): MΦ's proof uses (1) R_c, pos, w, Φ, W: functions of c and the ranks; (2) P_t ⊆ R_c,
  from [S1-val] with c fixed; (3) the MATCHED / carry split, a property of the pair (P_t, P_{t+1}); (4) rise ≤ W + fall, falls only at carries.
  No step reads τ, the phase or (MON). On a λ-run c = λ(v) is fixed, so the Corollary holds verbatim there; on λ^U-runs it holds for U on G^d
  (G^d is a game with the same ranks; MATCHED is then read with G^d's parities). AGREES with my predecessor (R-N5-MPGS §1b). The packet calls this
  a reading to be confirmed by MΦ's referees: confirmed by the first referee; REFEREE-2 did not address λ-runs in R2-N5-MPGS (its N-MPGS-6 only
  says the Lemma uses no phase).
- Data: the Corollary on every λ-run of both players (compose_probe.py MPHI=1, matched() from scratch/matchphi_probe.py): library n ≤ 40, 294 games,
  29,931 (Even) + 12,222 (Odd, on G^d) (vertex, λ-run) checks; random n 6-16, 4,000 runs, 94,226 + 71,142 checks: 0 failures; max NM 15.
  Odd-side λ^U-run data are new (my predecessor's LAMRUN data were Even-only).

## 7. Re-runs and own control
- Pinned, from a clean worktree at 3ca0932d (`git worktree add --detach`), `python3 -I`, read first (compose.py sha1 9fc3b081…, quotecheck.py
  29bb4a97…):
  - quotecheck: "quotes=16 bad=0", QUOTES PASS; --mut: "quotes=16 bad=16", QUOTES FAIL (control bites).
  - compose.py runquad_K8_m30_n192: TOP (263, …, 0, 263, 481, 1016, 195072, 265890048, 8, 15, 15, 15, 192), I0 I1 LDIR LBLK I2 I3 PASS, exit 0.
  - compose.py dlsep_kill_n70: TOP (12, …, 0, 12, 39, 387, 26810, 14059640, 5, 6, 7, 4, 70), PASS ×6, exit 0.
  - MODE=run seglast_kill_n110: TOP (16, …, 0, 16, 27, 152, 16066, 0, 20, 1, 4, 2, 110), RUNI0 R47 EI1 OI1 ELDIR OLDIR ELBLK OLBLK PASS, exit 0;
    segcount_kill_n20 the same eight PASS. All EXACTLY as §7 and check.sh l. 595-610.
- Own control: scratch/compose_probe.py (sha1 239d122e…) on my engine rl_engine (SPEC from the text; no lane code). Per run, both players: FSW,
  FMON, Ξ-SUCC, SW-RETURN on the whole run, on 3 random stretches, on every λ-run and every phase, its strong form (a change of Ξ(c) between
  consecutive entries), LEN-MONO (cycle node fixed, direction, ℓ ≤ n − 1, block length, bound), COMPOSE sums on every λ-run (Even) / λ^U-run (Odd),
  the phase part, and the full COMPOSE-RUN classification with the fallback rule asserted.
  | corpus | runs | transitions | SW-RETURN checks (strong form) | LEN-MONO checks | kinds (i)/(ii)/(iii)/(iv) | fallbacks E (i)/(ii), O (iii)/(iv) | violations |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | library (rho_probe.lib(), n ≤ 64; given + S3 + 1 random start) | 763 | 12,426 | 87,161 (7,057) | 129,260 | 2,101 / 9,964 / 238 / 123 | 91 / 952, 1 / 17 | 0 |
  | lane pins (runquad n192, dlsep n70, seglast n110, segcount n20, l121reader n41) | 15 | 512 | 2,468 (610) | 8,818 | 43 / 463 / 5 / 1 | 1 / 8, 0 / 1 | 0 |
  | random rand_ck n 5-16 (3,000 games, S3 + 1 random) | 6,000 | 10,171 | 82,509 (20) | 232,299 | 5,878 / 2,262 / 1,471 / 560 | 6 / 231, 2 / 113 | 0 |
  | random n 6-16 with MPHI (2,000 games) | 4,000 | — | — | — | 4,296 / 1,586 / 951 / 408 | 5 / 155, 1 / 88 | 0 |
  A batch rand n 16-30 (400 games) was stopped unfinished at 12:51Z (too slow, no output; compose_logs/rand400.txt says so).
  At most 29 λ-runs and 14 λ^U-runs in one run (library); no Even fallback outside (i)/(ii), no Odd fallback outside (iii)/(iv).
- Mutation controls (random n 8-20, 1,000 games × 2 starts; compose_logs/mut1-4.txt), all BITE:
  | MUT | change | result |
  | --- | --- | --- |
  | 1 | SW-RETURN without the "+1" | 14,867 violations |
  | 2 | SW-RETURN with PCH(c) in place of RISE(c) (length-only rises dropped) | 3 violations (rand524, rand898: whole-run stretches) |
  | 3 | LEN-MONO without the length term (RISE ≤ PCH) | 3,144 violations |
  | 4 | the phase bound on whole λ-runs (τ-only transitions counted) | 423 violations |
  So the "+1", the length term and the restriction to phases are all used.

## 8. Notes (for L-SI's fixes file)
- COMP-E1 (E-item, §1): define |𝒫| := #{t : t, t + 1 ∈ 𝒫} (transitions). Under "states" the phase part of Theorem COMPOSE is false.
- COMP-N1: the title defines P* but its formula also uses P*^U.
- COMP-N2: SW-RETURN's RISE_R(c) counts CHANGES of Ξ(c); by F-MON they are rises. Say so where RISE is defined (the name suggests it, the definition says ≠).
- COMP-N3: F-MON's "I is unambiguous: σ_{t+1} is a strategy" — say that I := {(v, σ_{t+1}(v)) : σ_{t+1}(v) ≠ σ_t(v)} ⊆ Iσ_t by F-SW (the link from
  S4a's arena to R15 (d)'s "Switch_I with I ⊆ Iσ" is [STEP] itself; one clause).
- COMP-N4 (§6 note): the λ-run reading of [MΦ] is now confirmed by the first referee twice (R-N5-MPGS §1b, here §6); it can be stated as a
  remark of the landed MPGS entry rather than an assumption.
- COMP-N5 (slack, DATA): Σ SW / Σ(1 + RISE) = 0.10 overall on the library, 0.28 on random games; the factor n of LEN-MONO and MΦ's n²/2 are the
  loose links, as §7's READING says.
- COMP-N6 (premise): F-MON on the Odd side is [MON] applied to G^d, as in R47's Lemma Φ (b) citation chain (PHI-N1 = N-PHI-2); no new premise.

## DONE / FINDINGS / NEEDS
- DONE: this report; scratch/compose_probe.py, compose_logs/ (run_all.sh, lib, pins, rand3000, mut1-4, mphi_lib, mphi_rand); pinned checks re-run exactly.
- FINDINGS: SW-RETURN, LEN-MONO, Theorem COMPOSE, COMPOSE-RUN SIGNED; COMPOSE-NM SIGNED as an implication and its λ-run premise holds. One
  E-item: |𝒫| must be defined as transitions (COMP-E1). Classification and fallbacks correct; λ-run counts come from R47's every-game Lemma Φ (c).
- NEEDS: Lead: route COMP-E1, COMP-N1..N6 to L-SI (fixes file); the COMPOSE §C word when I may open REFEREE-2's report.
