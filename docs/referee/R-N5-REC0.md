# R-N5-REC0: REFEREE report on packet P-N5-REC0 (L-NEW box 45: Lemma REC-0, D = ∅ epochs per phase ≤ (f + 1)(n + 1) + 4n(n − 1) + 1; every game)
Referee: REFEREE (successor 13, session_01Nzrjhmm1pgUnEvdgjCBhTv), Opus 5.5 (owner ruling D15). Context at writing: about 370k tokens.
- Routing: the Lead's GO of 08:51Z (Lead's stamp).
- Object: docs/new/P-N5-REC0-box45.md at trunk 64506ecf, sha1 343239b54a35d2701d076805674ef77aa7a21f7d (checked with
  `git show 64506ecf:… | sha1sum` and `git show 18dd8c90:… | sha1sum`; identical), 94 lines, frozen at l-new 18dd8c90. Author: L-NEW successor 24.
- Written 2026-10-26T08:52Z-08:57Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ REC0 file opened. No lane code run (experiments/new/box45/rec0.py, recclimb.py). D1.
- Premises read against their text: SPEC S4a (docs/new/N5-ssi-global.md l. 50-53); R17 (b) Lemma P, proof text docs/new/N5-phase-bound-box10.md §2
  (unchanged since the R17 pin 26905f0: `git diff 26905f0 64506ecf` on the file deletes 0 lines), and my lane's R-N5-1P (gaps G1-G4 closed);
  R18 (d) Lemma S (c) (RESULTS l. 803-807: S4a steps only); R15 (a), (d) (G-N5-TERM-reading §3); P-N5-XEP §0-§2 (split := λ_W(v) ≠ λ(v);
  SN-PREFIX_D (a) and its proof from WM + XW), landed as RESULTS R63; RESULTS R64 (c) EP-0 and its len(E) definition.
- Tool: scratch/rec0_probe.py (own engine; checks the inequality, EP-0, and, with LEVELS=1, each proof step: the level step, persistence,
  base, saturation, t* − t, and kind-(iii) steps per run, by exhaustive simple-path enumeration). Logs scratch/rec0_logs/ (run_all.sh).

## Verdicts
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | Lemma REC-0: N_0 ≤ (f + 1)(n + 1) + 4n(n − 1) + 1 per phase, every game | SIGNED (a REDUCTION in f) |
| §1 | Corollary: in-phase transitions with source in a D = ∅ epoch ≤ ((f + 1)(n + 1) + 4n(n − 1) + 1)(n + m) | SIGNED |
| Q-R17 | is R17 (b)'s induction step used only through the hypothesis at k, the switch-best arena optimum, (F1)/(F2) and an unchanged W-cycle-node map? | YES (§2 below, with the full list) |
| §2, §3 | reading, data | not signed (as briefed) |
No gap. Notes REC0-N1..N3 (citation and wording). Not a running-time bound (f is not bounded here). Not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. Lemma REC-0, step by step
- Setting ✓. D = ∅ at k ⇒ σ̄_k = τ (Odd vertices outside Q have one successor) ⇒ Ξ_k = W_k and λ_W = λ: D = ∅ states are all-unsplit. An
  epoch has D_E = ∅ iff each of its states is D = ∅ (σ̄|Q is constant on E, τ on P).
- Step 1 (level step) ✓, given Q-R17 (§2). At a D = ∅ state Ξ_k = W_k, so Iσ_k (S2, read from Ξ_k) is exactly the set of W_k-improving Even
  edges of G_τ, and S4a's arena (Even v: {σ_k(v)} ∪ Iσ_k(v); Odd v: τ(v)) is R17's switch-best arena H_k of the one-player game G_τ. At an
  S4a step σ_{k+1} maximises V_{·,τ} = W pointwise over that arena (R18 (d) S (c); S4a steps only, as here): that is (F1) for H_k, and
  (F2) W_{k+1} ⪰ W_k. λ_W(k) = λ(k) (D = ∅), λ(k) = λ(k+1) (in-phase), λ(k+1) = λ_W(k+1) (all-unsplit), so no vertex changes its W-cycle
  node between k and k + 1, and every cycle node u of λ is a W-cycle node at k and at k + 1.
- Step 2 ✓. Base: at an all-unsplit state a cycle node u of λ has λ_W(u) = u, so W(u) = (u, ∅, 0) = value of the empty path. Persistence: WM
  (R23 (g), game-general) gives W_{k+1} ⊵ W_k at an in-phase S4a step, and the set of paths in the level condition (G_τ fixed, cycle nodes of
  λ fixed on P) does not change.
- Step 3 ✓. The in-phase transitions of P are S4a steps or Even fallbacks; f fallbacks leave ≤ f + 1 maximal fallback-free runs. Per vertex
  the unsplit states of a run form a prefix (SN-PREFIX_D (a), R63; its proof uses only WM and XW, game-general); the intersection over all
  vertices, the all-unsplit states, is a prefix U(R). Inside U(R) every transition is an S4a step between all-unsplit states (step 2), and
  from a D = ∅ source it adds one level (step 1; "level j + 1" is the same condition as level n − 1 once j ≥ n − 1).
- Step 4 ✓. At an all-unsplit t, W_t(x) is the value of x's G_τ-play: the simple path from x to its first visit of λ_W(x) = λ(x), a cycle
  node of λ, so W_t(x) = value(r_x) ⊴ B(x). Level n − 1 covers every simple path, so W_t ⪰ B, hence W_t = B (the order is total on values).
  For D = ∅ states t′ ≥ t: Ξ_{t′} = W_{t′} ⊴ B = W_t = Ξ_t ⊴ Ξ_{t′} (R15 (a)), so Ξ_{t′} = B; by R15 (a) Ξ is constant on [t, t*]; τ is constant,
  so Ωτ is too; R15 (d) gives t* − t ≤ 4n(n − 1). Every D = ∅ epoch not entirely before t has all its states D = ∅ and ≤ t*, hence a state in
  [t, t*]: ≤ 4n(n − 1) + 1 such epochs ✓.
- Step 5 ✓. The other D = ∅ epochs end before t. All but possibly P's last epoch have an in-phase last transition y → y + 1 with y D = ∅;
  these are distinct. (i) fallbacks: ≤ f. (ii) y ∈ U(R) (y is all-unsplit and the run's all-unsplit states ARE U(R)) and y + 1 ∉ U(R): ≤ 1 per
  run (U(R) is a prefix). (iii) y, y + 1 ∈ U(R): the m-th such step of a run has a source of level ≥ m − 1 (each earlier one added a level,
  the steps between keep it, step 2); a source of level ≥ n − 1 would be saturated, hence ≥ t; so m ≤ n − 1 for sources < t ✓.
  f + (f + 1) + (n − 1)(f + 1) + 1 = (f + 1)(n + 1) ✓.
- Step 6 ✓. Corollary: Σ_{E: D_E = ∅} len(E) with len(E) ≤ n + m (EP-0, RESULTS R64 (c), whose len(E) is "the in-phase transitions whose source
  lies in E", the corollary's count; EP-0 survives EPR-1).
- VERDICT: Lemma REC-0 and its corollary SIGNED, every game.

## 2. Q-R17 (the packet's question): answered YES
I read R17 (b)'s proof (N5-phase-bound-box10.md §2, the signed text) case by case. The step k → k + 1 uses:
1. the hypothesis at k (Ω_k(z) ⪰ value(r′) for simple r′ with ≤ j edges from z to u avoiding x): in A (via transitivity), B1 (first sub-case),
   B2 (last line);
2. that (x, z) ∉ I_k or ∈ I_k is read from Ω_k (cases A / B): the improving edges of the SAME valuation Ω_k = W_k (this is where D = ∅ at k
   is needed: Iσ is defined by Ξ);
3. that ρ̂ = ρ_k[x → z] for (x, z) ∈ I_k is a strategy of the arena, and the step's result is a pointwise optimum of it ((F1)), and (F2) Ω_{k+1} ⪰ Ω_k
   (A1, A2, B1, B2);
4. (V1), (V2) (value algebra of one play; statewise);
5. that u is a cycle node at k (A2, B2: "Ω_k(ρ_k(x)) has cycle node x … value(r′) has cycle node u"; u ≠ x for paths with ≥ 1 edge) and that
   no vertex changes its cycle node from k to k + 1 (B1 second sub-case with P(π) ≠ ∅, B2 with D ≠ ∅ or top(Z) ≠ c: "the phase ended at step
   k + 1, contrary to the assumption");
6. the one-player structure of H (Odd vertices have one successor; true for G_τ).
Nothing uses an earlier step, the phase start (that is the base case k = 0 only, replaced in REC-0 by step 2's base), the number of steps
taken, or uniqueness of the optimum (R17 (d)). R-N5-1P's gaps on Lemma P (G1, G2: B1's improvement case list) are wording, closed, and do
not touch these inputs. So the step is valid at any state k of an N5 run at which 2, 3 and 5 hold, i.e. exactly REC-0 step 1's hypotheses.
- Consistency with R17's honest limit (ii) ("Lemma P's statement is FALSE for N5's Even moves inside a σ̄-segment", seg_r16, seg_n24): there
  Ξ ≠ W, so input 2 fails (S4a's arena is Ξ's gate, not G_τ's switch-best arena). REC-0 applies the step only from D = ∅ states, where
  Ξ = W. No conflict.

## 3. Own data (DATA, not signed; scratch/rec0_logs/)
| sample | runs | phases | REC0 / EP0 checks | level checks: STEP1 / STEP2 / BASE+SAT / T4 / RUNIII | failures | max N_0 | max N_0/(f+1) | max kind-(iii) per run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| random games n 4-9, k ≤ min(3, n − 1) Odd choice vertices, 20,000 games, seed 11, canonical + 3 random starts, LEVELS=1 | 80,000 | 177,184 | 177,184 / 111,443 | 9,805 / 10,740 / 146,411 / 81,762 / 10,391 | 0 | 2 | 2.0 | 1 |
| lib41 (412 files; 45 with n > 64 skipped), canonical + 2 random starts (seeded by relative path) | 1,101 | 5,338 | 5,338 / 2,089 | — | 0 | 5 | 5.0 | — |
| lib41 as above, LEVELS=1 for n ≤ 14 only | 1,101 | 5,338 | 5,338 / 2,089 | 124 / 189 / 659 / 251 / 125 | 0 | 5 | 5.0 | 1 |
- failures = REC0, EP0, STEP1, STEP2, BASE, SAT, T4, PREFIX (all-unsplit states a prefix of each run), RUNIII: all 0.
- Thin: kind-(iii) steps never exceed 1 per run, so step 5's n − 1 cap is not exercised by data; the level step itself is (9,929 checks).
  lib41's max N_0 = 5 equals the packet's lib41 row; its phase count differs (5,338 vs 5,377: my random starts differ).
- Reproduce: scratch/rec0_logs/run_all.sh from docs/referee/scratch/.

## 4. Notes (not gaps)
- REC0-N1 (citation): SN-PREFIX_D (a) is landed as RESULTS R63; cite R63 next to the packet. WM's game-general form is R63's premise list
  (XEP-N2) as well as R23 (g).
- REC0-N2 (wording, step 3): "rises by one at every S4a step from a D = ∅ state of U(R) to a state of U(R)" — the level is the largest j
  ≤ n − 1 with the property; say "level ≥ min(j + 1, n − 1)". The count in step 5 uses only this.
- REC0-N3 (wording, Q-R17): the step also uses (V1)/(V2) and the one-player structure of G_τ (inputs 4, 6 above), both statewise; the
  packet's list of what the step uses should name them.

DONE (REFEREE successor 13, (Opus 5.5, D15)).

## §C. Comparison with REFEREE-2 (R2-N5-REC0, claude/referee-2 a0457eb0 + independence-line correction 82fdc8d4; its §C 1ff6c484 not opened before this), written 2026-10-26T10:07Z by date -u
- Opened only after my report was pushed (6006b963) and on the Lead's word (09:15Z). Read in full (§1-§3).
| item | REFEREE | REFEREE-2 | relation |
| --- | --- | --- | --- |
| Lemma REC-0 | SIGNED | SIGN | same |
| Corollary (via EP-0) | SIGNED | SIGN | same |
| Q-R17 | YES, six inputs listed (§2) | YES, the same inputs (§2) | same |
| REC0-N3: Q-R17's list should also name (V1)/(V2) and the one-player structure of G_τ | mine | N-REC0-2 (first half): (V1), (V2) and "u is a cycle node at k"; it puts the one-player / arena condition under the transfer | same finding; "u is a cycle node at k" is my §2 input 5, now also in the note |
| N-REC0-2 (second half): step 4 reads R15 (d)'s Ωσ as S1's Ξ (code link G-N5T-1) | used without comment | REFEREE-2 | found by REFEREE-2; ACCEPTED (citation) |
| N-REC0-1: step 1's hypothesis should say "an IN-PHASE S4a step" (it uses λ(k) = λ(k+1)) | used ("in-phase" in my step-1 reading) but not flagged as a wording point | REFEREE-2 | found by REFEREE-2; ACCEPTED (wording) |
| REC0-N1 (cite R63 for SN-PREFIX_D) | mine | — (accepted in its §C, per the Lead) | found by REFEREE |
| REC0-N2 (step 3: "≥ min(j + 1, n − 1)") | mine | — (accepted in its §C, per the Lead) | found by REFEREE |
| Data | 0 failures; lib41 max N_0 5; kind (iii) ≤ 1 per run | 0 violations; lib41 / its 503 files max N_0 5; kind (iii) ≤ 1 per run | same; both note the n − 1 cap untested |
- No disagreement. Joint gap map: EMPTY. Nothing open on REC0; the notes N-REC0-1, N-REC0-2 and REC0-N1..N3 go to the lane's fixes file.
