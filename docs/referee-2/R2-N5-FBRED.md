# R2-N5-FBRED: second-referee check of packet P-N5-FBRED (L-NEW box 44: FB-POLY's lemmas in set form on every game, Theorem FB-RED and its late form, Lemma TV). REFEREE-2 (successor 13), written 2026-10-26 03:0xZ-03:5xZ (date -u)
Signature: (Opus 5.5, D15). Lead's order 03:13Z (its stamp): second-referee check while P-N5-1E waits.
Object: docs/new/P-N5-FBRED-box44.md, `git show c3f6f2bf:docs/new/P-N5-FBRED-box44.md | sha1sum` -> 11b15455f70d439c93a48d7e82fcdc14ef73854d
(= the Lead's pin; = my tree), 178 lines, added at 3732ab55 (L-NEW successor 23). No fixes file in my tree.
Background read (texts, not recalled): the port source docs/new/P-N5-FBPOLY-box41.md §0-§4 (= RESULTS R48, cited "FBP"), RESULTS R48 entry;
R15 (a), R17 (a), R18 (d) Lemma S with docs/new/N5-time-box21.md §2.2, R38 (a), (f); SPEC S1, S2, S4c, FIX 3.
Independence: `ls docs/referee | grep -i fbred` -> empty at 03:07Z; no docs/referee file read for this packet. No grep of docs/agents/ or
RESULTS for it. The lane's experiments/new/box44/fbf.py, fbclimb.py were not run or imported; box-43/44 instances and lib41.txt are inputs.
Tools (own code, docs/referee-2/R2-N5-FBRED/): fbred_check.py (own SPEC N5 loop R2-N5-DUAL/dual_check.Runner; honest frame from SPEC S1;
simple-path enumeration for the freeze lemmas), box4344.lst, run_all.sh, run_climbs.sh, logs/, climb/.
Labels: PROVED (L-NEW 23, unrefereed). Every game, per phase. FB-RED is a REDUCTION in ρ; ρ-POLY is CONJECTURE (§5, not signed).

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §1.1 (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′) per honest class | SIGN | — |
| §1.1 κ-FB-ROUND (per class) | SIGN | — |
| §1.2 κ-HAT-FREEZE_D (a)-(c) | SIGN | — |
| §1.2 κ-PFZ_D (per q, per Q_c-run) | SIGN | N-FBRED-1 (the induction runs through z = q, outside the stated range z ∈ U_c ∖ T; trivial there) |
| §1.2 κ-Y-FORM_D (per q, repaired Y^q) | SIGN | N-FBRED-2 (Y^q is defined only in §4, a not-to-sign table); N-FBRED-3 (Lemma S (a) on every game: CONFIRMED) |
| §2 EXIT-SWITCH_D | SIGN | — |
| §2 FREEZE-EXIT_D (conservative indices) | SIGN | — |
| §2 CN-ONLY_D | SIGN | — |
| §3.1 Theorem FB-RED, f ≤ 1 + (n − 1)(2 + ρ) | SIGN (as a reduction in ρ) | N-FBRED-4 (late regime never reached in data, §5) |
| §3.2 FB-RED late form | SIGN | N-FBRED-4 |
| §3.3 Lemma TV | SIGN | — |
| §4 (step table), §5 (THETA-AFTER, ρ-POLY), §6 | not signed (as briefed) | §4 checked as a READING: agrees with my step-by-step diff (§1-§3 below) |
No statement is NOT SIGNED and no gap is open. No (P). TARGET.md diff: not a claim of TARGET.md §2 (a per-phase reduction; no running
time).

## 1. Facts and κ lemmas against FBP §0.3-§1 (every one-Odd use located)
- (Aκ) ✓: FBP's proof uses only λ_t(z) = c_θ ≠ z, (V1) and "z on its own play's cycle ⇒ rank below the top"; with c for c_θ and U_c for
  U it is verbatim. (A0κ), (M1κ), (M2κ) (R15 (a), λ constant in the phase), (INJ) ✓ verbatim per class. (SP′) ✓: the play from
  z ∈ U_c ∖ {c} stays in U_c, ends on a cycle with cycle node c ∈ T, and is a lasso; the prefix to the first T ∩ U_c vertex is simple.
  Note T ∩ U_c = {c} ∪ (Q ∩ U_c): another cycle node c′ has λ(c′) = c′, so c′ ∉ U_c.
- κ-FB-ROUND ✓: FBP §1's proof uses (Aκ), (M1κ), (M2κ), S4c's best-key rule; the in-phase fallback is Even's (τ constant; FIX 3). No
  one-Odd step.
- κ-HAT-FREEZE_D ✓. FBP's one-Odd uses: (a) "z Odd ⇒ forced" — here z ∈ G_c, so z ∉ Q ∖ {c}, and z ≠ c in the step (c is a sink): z has
  out-degree 1 and x = next_t(z) ✓. (b) used (HP) to get "z ∈ F ⇒ honest play avoids o" — replaced by the HYPOTHESIS "z's honest play
  avoids Q ∖ {c}", under which the prefix to c is a path of G_c (Even σ_t edges inside U_c; Odd vertices not in Q, forced) ✓. (c): G_c
  has ≤ |U_c| vertices, so ≤ |U_c| − 1 edges (one more than FBP's |U| − 2, since o is not dropped here), and the index g_{|U_c|−1} ✓.
- κ-PFZ_D ✓. FBP's one-Odd use: "z Odd (z ≠ o) ⇒ forced" — true in G_c^q = U_c ∖ (T ∖ {q}) ✓. κ_t(q) is constant on a Q_c-run ✓.
  - N-FBRED-1 (wording): the statement ranges over z ∈ U_c ∖ T, but the induction step from z = x·… uses the hypothesis at x ∈ G_c^q,
    which may be q itself (p′ with 0 edges). At z = q the claim reads κ_t(q) ≥ κ_t(q): trivially true. FBP stated z ∈ U ∖ {c_θ}, which
    includes o. Fix: state the lemma for z ∈ (U_c ∖ T) ∪ {q}.
- κ-Y-FORM_D ✓. FBP's one-Odd uses: (HP) (i) for "σ̄(o) ∈ F", and "every other Odd vertex is forced" so that y's (σ_t, τ′)-play is its
  (σ, τ)-play. Here: "≥" — q on no honest cycle ⇒ λ(q) = c ≠ q, (Aκ) at q, σ̄_t(q)'s honest play is the rest of q's and avoids q, so
  σ̄_t(q) ∈ Y^q_t ✓. "≤" — τ′ := σ̄_t except τ′(q) := y; y's (σ_t, τ′)-play avoids q, the only vertex where τ′ ≠ σ̄_t, so it is y's honest
  play, V_{σ_t,τ′}(y) = Ξ_t(y) (cycle node c, y ∈ U_c); q's (σ_t, τ′)-play is q · (y's play), not returning to q, so V(q) = q ⊕ Ξ_t(y) with
  q ∉ P(Ξ_t y) ✓; Lemma S (a): Ξ_t(q) ⊴ V_{σ_t,τ′}(q); (M1κ) ✓.
  - N-FBRED-2 (wording): Y^q_t := {y ∈ succ(q) ∩ U_c : y's honest play at t avoids q} is defined only in §4's table (not to sign). The
    signed §1.2 uses it; move the definition into §1.2 (or §0).
  - N-FBRED-3 (the Lead's READING item): Lemma S (a) on every game: CONFIRMED, consistent with my N-1O-4 (R2-N5-1O) and N-GD-2 (R2-N5-GD
    §4). RESULTS R18 (d) states "L_σ is the pointwise minimum of V_{σ,τ'} over Odd's strategies τ'" with L_σ := Ξσ (box 21 §2.2 l. 45, 68);
    its proof is VJ00 (11) on G (R17 (F1) on the one-player game G_σ) and uses no one-Odd property. Here it is applied with τ′ positional
    (σ̄ changed at one vertex), within its scope.

## 2. §2 against FBP §2-§4
- EXIT-SWITCH_D ✓. FBP's one-Odd use: "Odd w ≠ o: the forced edge" for unswitched non-terminal w — here an Odd w ∈ U_c ∖ T is not in Q,
  so it has one successor ✓. The contradiction argument: the k+1-play from v ∈ S_c stays in U_c ((Aκ)), and between visits of S_c it
  follows k-plays through U_c ∖ (S_c ∪ T), where next_{k+1} = next_k (every switched non-terminal vertex of U_c is in S_c); so it never
  meets T, against (SP′) at k+1 (it must meet c) ✓. Note: σ̄ may change at k → k+1 at vertices of Q; the argument only uses steps at
  non-terminal vertices, so this is harmless ✓. p_u: simple ((SP′) at k), avoids u, path of G_c (e = c) or G_c^e (e ∈ Q) ✓; (Aκ) along
  it gives the κ identity ✓.
- FREEZE-EXIT_D ✓. p_u has ≤ |U_c| − 1 edges; e = c: u Even ∉ Q, k = g_j > g_{|U_c|−1} (j ≥ |U_c|), κ-HAT-FREEZE (a) ✓; e = q: k ∈ Θ_c and
  k > f^{Θ_c}_{|U_c|−1} (i ≥ |U_c|), κ-PFZ ✓; (Aκ) at u and the gate (x*_u is S4c's best gate target, Ξ_k(x*_u) ▷ Ξ_k(σ_k u), both in U_c)
  give the contradiction ✓. The one-larger indices follow from (c)'s |U_c| − 1 ✓.
- CN-ONLY_D ✓. (1) is NEW and simpler than FBP's: S = ∅ means every switched vertex lies in T; switched vertices are Even, so not in Q,
  so in C: cycle nodes — no (HP), no FBL-N (ii) ✓. (2) first T-vertex y: π lies on y's k+1 honest cycle with top y, P = ∅ ✓. First
  T-vertex q ∈ Q ∩ U_y (q ≠ y): π unchanged at k+1 (its vertices are in U_y ∖ T, unswitched, Even with σ kept or Odd with one successor),
  the k+1-play from y is y·π·q·… and returns to y (λ_{k+1}(y) = y), so π and q lie on y's k+1 cycle, below y: wt_y = 0 on π and
  M_{k+1}(q) = 0; (Aκ) along π at k, (M2κ) at q (first component of the lexicographic order), the gate with (A0κ) and (M1κ): M_k(x*_y) = 0,
  P = ∅ (INJ) ✓. This is FBP §4 (2)'s last bullet with q for o; FBP's middle bullet (y ≠ c_θ, using (HP)) is not needed because every
  class is treated alike ✓. (3) verbatim; CN-LAST is signed on every game (R38 (f)) ✓.

## 3. Theorem FB-RED, late form, Lemma TV
- FB-RED ✓. S = ∅: ≤ 1 (CN-ONLY_D). S ≠ ∅, j ≤ n − 1: ≤ n − 1. S ≠ ∅, j ≥ n: S = ⋃_c S_c (a switched non-terminal v has λ(v) = c for
  some c ∈ C), so some S_c ≠ ∅; |U_c| ≤ n ≤ j; FREEZE-EXIT_D's contrapositive gives i ≤ |U_c| − 1 for k's index i in its Q_c-run; a Q-run is
  a sub-run of that Q_c-run, so k's index there is ≤ i ≤ n − 1 ✓; Q-runs ≤ 1 + ρ (a boundary needs some Ξ(q) to change, and ρ counts
  pairs) ✓. Total 1 + (n − 1)(2 + ρ) ✓.
- Late form ✓: the third bullet counts only Q-runs holding a late fallback (with S ≠ ∅); N_late ≤ 1 + ρ_late ✓.
- Lemma TV ✓. "≥": every simple path of G_c, G_c^q has ≤ |U_c| − 1 edges; κ-HAT-FREEZE (a) at t > g_{|U_c|−1}; κ-PFZ on the Q_c-run Θ_c ⊇ Θ:
  the fallbacks of Θ are fallbacks of Θ_c, so t > f^Θ_{|U_c|−1} ≥ f^{Θ_c}_{|U_c|−1} ✓, and κ_t(q) = κ_Θ(q) ✓. "≤": the honest prefix of z
  to its first T ∩ U_c vertex e is simple ((SP′)), with forced Odd vertices before e; e = c: a G_c path; e = q: a G_c^q path, and (Aκ)
  gives κ_t(z) = κwt_c(path ∖ {q}) + κ_t(q) ✓.

## 4. §4 step table (READING): agrees with §1-§3 above
Every row's "one-Odd use" is the one I located in FBP's text, and every replacement is the one used in the signed proofs. THETA-AFTER
FAILS AS PROVED (several terminals: y ∈ Y^q may route through q′ ∈ Q whose value moves) — I agree with the diagnosis; not signed.

## 5. DATA (fbred_check.py; own definitions; S3 + random starts)
| set | runs | phases | max f per phase (file) | max f − n | max j with S ≠ ∅ | max ρ | violations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lib41.txt × 3 starts | 1,236 | 7,193 | 33 (ccl_w48_n48) | −2 | 33 | 194 (tcL_N8) | 0 |
| R2-N5-KW/files.lst (503 𝒞^1O) × 2 | 1,006 | 4,116 | 37 (dirty_a_best, random start) | −2 | 37 | 60 | 0 |
| box-43/44 instances (10 files, incl. fb17_n32, rtf_cex) × 5 | 50 | 294 | 17 (fb17_n32) | −6 | 17 | 36 | 0 |
| random 𝒞^kO n 4-12, random starts | 20,000 | 49,548 | 1 | −3 | 1 | 5 | 0 |
Checks on every phase: AK, ROUND, YF (κ-Y-FORM_D; 199,685 + 15,443 + 2,002 + 91,789 checks), EXS, FEX, CNO, RED, REDL; for n ≤ 11 also
HAT (a)-(c), PFZ (all j) and TV by exhaustive simple-path enumeration (PFZ 290,637 checks; HAT (c) and TV 97 qualifying states each,
all on random games: the library's small games have almost no fallbacks).
Mutation controls (lib41, S3): yf (min → max) 56,436; cno (CN-ONLY asks 0 S-empty fallbacks) 26 — both bite. fex (FREEZE-EXIT_D with
|U_c| − 2) and red (FB-RED with ρ := 0) do NOT bite: no fallback comes within 4 of FREEZE-EXIT_D's indices (closeness max −4) and no phase
has f > 1 + 2(n − 1).
N-FBRED-4 (the late regime, the Lead's request): FB-RED's third bullet, its late form and Lemma TV's hypotheses at large indices act only
when some phase has a fallback g_j with j ≥ n. No run reaches it: max (f − n) per phase = −2 in the library (n3all_maxph_0, n = 3; f = 1),
and on 𝒞^1O the largest f is 37 at n = 48. Climbs aimed at it (run_climbs.sh: 4 hill climbs on small games n 4-8 with any number of Odd
choice vertices, objective max in-phase fallbacks per phase − n, 4 random start pairs per candidate, every scored run fully checked):
4 × 4,000 steps (64,000 checked runs, 0 violations), best max in-phase fallbacks per phase − n = −4, −5, −5, −7 (seeds 82, 83, 84, 81; climb/late_*.pg with start pairs in late_*.txt); the climbs barely moved off their starting scores, so the objective is flat on small random games and a better search (constructed families, larger n, the lane's fb17_n32 as a seed) would be needed. So I could NOT build a test that reaches the late regime; those statements rest on their proofs, which I checked line by
line (§2-§3). The REDUCTION's content (f bounded by ρ) is therefore untested by data at the place it matters.

## 6. Notes (none blocks a signature)
- N-FBRED-1 (κ-PFZ_D range): state it for z ∈ (U_c ∖ T) ∪ {q}; the induction passes through q (trivial there).
- N-FBRED-2 (κ-Y-FORM_D): define Y^q_t in the signed text, not only in §4.
- N-FBRED-3 (READING): Lemma S (a) on every game CONFIRMED (consistent with N-1O-4, N-GD-2).
- N-FBRED-4 (DATA): the late regime is not reached by any sample or by my climbs; see §5.

## 7. Honest limits
- The exhaustive freeze-lemma checks (HAT, PFZ, TV) run only for n ≤ 11, where fallbacks are rare; at larger n only AK, ROUND, YF, EXS,
  FEX, CNO, RED, REDL are checked.
- ρ is not bounded here; FB-RED bounds fallbacks per phase only given ρ (ρ up to 194 per phase in lib41).
