# R2-N5-REC0: second-referee check of packet P-N5-REC0 (L-NEW successor 24, box 45: Lemma REC-0, the D = ∅ epochs of a phase). REFEREE-2 (successor 15), 2026-10-26, written from 09:0xZ by date -u
- Object: docs/new/P-N5-REC0-box45.md, `git show 64506ecf:docs/new/P-N5-REC0-box45.md | sha1sum` -> 343239b54a35d2701d076805674ef77aa7a21f7d (= the
  Lead's), frozen at l-new 18dd8c90, pinned trunk 64506ecf. Brief (Lead 09:02Z): sign or not §1 (Lemma REC-0 and its transition corollary via
  EP-0); answer QUESTION Q-R17 explicitly; §2 READING and §3 DATA not signed; own engine; no docs/referee/ on REC0 before this push.
- Independence: docs/referee/ not opened on REC0. Correction after push a0457eb0: a name-only listing (`git ls-tree --name-only`) at 09:11Z shows 7
  REC0-named files on origin/claude/referee (0 on trunk); I read none of them; my earlier wording "no REC0 file listed" was not checked. Lane code (experiments/new/box45/rec0.py,
  recclimb.py) not run or imported.
- Context at writing: about 400k tokens (this session since 07:31Z; STAU review and §C before this packet).
- Premises read at their text: SPEC S1-S5, FIX 1-4; R17 (b) Lemma P and (F1)/(F2) (docs/new/N5-phase-bound-box10.md §1-§2, at 64506ecf);
  R18 (d) Lemma S (c); R23 (g) WM (game-general: P-N5-XEP fixes XEP-N2, both referees); R21 (a) XW; R15 (a), (d); P-N5-XEP §2 SN-PREFIX_D (a)
  (proof re-read: WM + XW per vertex); RESULTS R64 (c) EP-0 ("len(E) := the in-phase transitions whose source lies in E").

## Verdicts (Opus 5.5, D15)
| item | packet label | verdict | notes |
| --- | --- | --- | --- |
| §1 Lemma REC-0 | PROVED | SIGN | N-REC0-1 (wording, step 1's hypothesis), N-REC0-2 (citation) |
| §1 Corollary (transitions, via EP-0) | PROVED | SIGN | — |
| Q-R17 | question | answered YES (§2) | the induction step uses exactly the listed items plus two statewise value facts (V1), (V2) and "u is a cycle node at k" |
| §2, §3 | READING / DATA | not signed (brief) | §2's readings are correct as readings; §3's library maximum N_0 = 5 reproduced |
No gap. REC-0 is a REDUCTION (in f); it bounds no running time on any class beyond 𝒞^1O ∪ 𝒞^1E. G-N5-TIME stays open.

## 1. Lemma REC-0: proof check, step by step
- Setting: λ := Ξ's cycle-node map (constant on P); W_k := σ_k's valuation in G_τ; λ_W := W's cycle-node map; "level j" refers to the cycle nodes
  of P's λ and to simple paths of the fixed one-player game G_τ; B(x) := the maximum of value(r) over those paths. All constant on P.
- D = ∅ ⇒ Ξ = W ⇒ all-unsplit ✓ (σ̄_k = τ on Q, and Odd vertices outside Q have one successor, so σ̄_k = τ and V_{σ,σ̄} = V_{σ,τ}).
- Step 1 (level step) ✓, given Q-R17 (§2). At a D = ∅ state Iσ_k (Ξ-improving edges, S2) = the W-improving edges of G_τ, so S4a's arena (Even v:
  {σ(v)} ∪ Iσ(v); Odd v: τ(v)) is R17's switch-best arena H_k of G_τ (it contains σ_k and every improving edge). S4a's output is a pointwise
  optimum of H_k (R18 (d) S (c), R17 (F1)), so (F1) and (F2) hold with Ω := W. "k + 1 all-unsplit" and λ constant give λ_W(k + 1) = λ = λ_W(k):
  no vertex changes its W-cycle node, which is what Lemma P's cases B1 / B2 need. The hypothesis needs k + 1 ∈ P (N-REC0-1); it holds wherever
  step 1 is used (step 3: inside U(R) ⊆ P).
- Step 2 ✓. Level 0 at an all-unsplit state: the only 0-edge paths are x = u with u = λ(u) = λ_W(u), and W(u) = (u, ∅, 0). Persistence: WM
  (W_{k+1} ⊵ W_k at an in-phase non-fallback transition) and value(r) does not depend on the state (P's λ and G_τ are fixed).
- Step 3 ✓. Fallback transitions cut P into ≤ f + 1 runs of in-phase S4a transitions (an in-phase non-fallback transition keeps τ, so it is an S4a
  step). SN-PREFIX_D (a) per vertex, intersected over all vertices: the all-unsplit states of a run form a prefix U(R). Inside U(R) the level
  never decreases (step 2) and rises at every step from a D = ∅ state (step 1).
- Step 4 ✓. At an all-unsplit state, x's (σ, τ)-path to its first visit of c = λ_W(x) = λ(x) is simple, lies in G_τ, ends at a cycle node of λ
  (λ(c) = c), and its value(r) is W(x) term by term (cycle node, the set P, the length). So W ⊴ B. A D = ∅ state of level n − 1 has W ⪰ B (every
  simple path has ≤ n − 1 edges), so W = B. Sandwich for D = ∅ states t′ ≥ t: Ξ_{t′} = W_{t′} ⊴ B = Ξ_t ⊴ Ξ_{t′} (R15 (a)). So Ξ = B at t and at
  t*, hence on [t, t*] (R15 (a) again). Ωτ is constant (τ fixed), so the t* − t transitions are consecutive iterations leaving Ωσ = Ξ and Ωτ
  unchanged; R15 (d) gives t* − t ≤ 4n(n − 1) (Ωσ read as S1's Ξ: the standing code link G-N5T-1, N-REC0-2). Every D = ∅ epoch with a state
  ≥ t has all its states in [t, t*] (they are D = ∅ states ≤ t*), so at most 4n(n − 1) + 1 such epochs ✓.
- Step 5 ✓. The other D = ∅ epochs end before t. Except the last epoch of P (+1), each ends with an in-phase transition from its last state y
  (a D = ∅ state, hence in U(R) for its own run R); distinct epochs give distinct transitions. Kind (i) fallback ≤ f; kind (ii) leaves the prefix
  U(R): once per run ≤ f + 1; kind (iii) stays in U(R) and raises the level. After n − 1 kind-(iii) steps in a run, the level is ≥ n − 1 at every
  later state of U(R) (start ≥ 0, never decreases); so a later kind-(iii) source is a saturated D = ∅ state, i.e. ≥ t. So kind (iii) with source
  < t is ≤ n − 1 per run. (If no D = ∅ state is saturated, the same argument shows the n-th kind-(iii) step cannot exist.) Total
  f + (f + 1) + (n − 1)(f + 1) + 1 = (f + 1)(n + 1) ✓.
- Step 6 and the Corollary ✓. R64 (c)'s len(E) is exactly "the in-phase transitions whose source lies in E", so the D = ∅-sourced in-phase
  transitions number Σ len(E) ≤ N_0·(n + m).
- Mechanical check (DATA, §3): every step's claim at every state of every phase: 0 violations.

## 2. QUESTION Q-R17: answer YES
Question: is R17 (b)'s Lemma P induction step used only through the hypothesis at k, the switch-best arena, (F1)/(F2) and an unchanged λ_W, when
it is applied at a state of an N5 run? I re-read docs/new/N5-phase-bound-box10.md §1-§2 at 64506ecf line by line. The step k → k + 1 uses:
- the induction hypothesis AT k only (Ω_k(z) ⪰ value(r′) for the tail r′ of r, |r′| ≤ k edges). Its proof never looks at a state before k, and
  never at the phase start. (The phase start enters only the BASE case k = 0, which REC-0 replaces by its own step 2: level 0 at every
  all-unsplit state.) The bound "|r′| ≤ k" is the hypothesis's own path length, so REC-0's level j (independent of the step count) is the
  right reading;
- the arena H_k: in case B that ρ̂ := ρ_k[x → z] is a strategy of H_k for every improving (x, z) (every improving edge available), and for (F2)
  that ρ_k ∈ H_k. Case A uses only the definition of I_k (non-improving ⇒ Ω_k(z) ⪯ Ω_k(ρ_k x));
- (F1) (Ω_{k+1} ⪰ the value of every strategy of H_k, pointwise; any pointwise optimum, R17 (d)) and (F2) (Ω_{k+1} ⪰ Ω_k);
- "no vertex changes its cycle node from k to k + 1": cases B1 (second sub-case) and B2 end in "λ_{k+1}(x) ≠ c = λ_k(x): the phase ended at step
  k + 1, contrary to the assumption". Here λ is the cycle-node map of the one-player valuation, i.e. λ_W in REC-0;
- two facts about valuations at the single state k, which the packet's list leaves implicit: (V1) (x not its own cycle node ⇒ Ω_k(x) =
  x ⊕ Ω_k(ρ_k x), with the path from ρ_k(x) avoiding x) and (V2) (prefix monotonicity); plus "u is a cycle node at k" (A2, B2 compare the
  cycle nodes of Ω_k(ρ_k x), Ω_k(z) with u's). (V1), (V2) are general facts about values; the cycle-node fact holds because λ_W = λ at k.
Nothing else: no earlier step, no phase start, no property of how ρ_k was reached. One more condition belongs to the TRANSFER, not to the step:
the one-player game is G_τ (Odd fixed to τ_k, out-degree 1, so Odd vertices never have improving edges) and the arena is S4a's, which equals
H_k only because Ξ_k = W_k at a D = ∅ state (gates = W-improving edges). REC-0's step 1 states both. So the answer is yes, with the list
completed by (V1), (V2) and the cycle-node fact (N-REC0-2).

## 3. Data (DATA, not proof; R2-N5-REC0/, logs/)
- rec0_check.py (own): N5 runs from succ. 13's SPEC loop (R2-N5-DUAL/dual_check.Runner); phases, epochs, D = ∅, W in G_τ, all-unsplit, runs,
  levels (exact, by enumerating the simple paths of G_τ, for n ≤ 11), B, saturation, kinds, all from the packet's §0-§1. run_all.sh reproduces.
| input | runs | phases | BOUND / EP0 / PREFIX checks | level checks (n ≤ 11): BASE+UB / STEP2 / STEP1 (of which the level is not yet full after the step) | max N_0 | max kind (iii) per run | violations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| random general (kO), 5,000 games, n 4-11, seed 51, S3 + 3 random | 20,000 | 45,557 | 45,557 / 23,512 / 46,092 | 33,597 / 1,973 / 1,675 (75) | 2 | 1 | 0 |
| random 𝒞^1O, 5,000, n 5-11, seed 52, S3 + 3 random | 20,000 | 39,413 | 39,413 / 26,454 / 39,980 | 35,775 / 3,005 / 2,637 (151) | 1 | 1 | 0 |
| my 503 𝒞^1O files (R2-N5-KW/files.lst), S3 + 2 random, seed 7 | 1,509 | 6,213 | 6,213 / 3,169 / 8,744 | 826 / 207 / 122 (45) | 5 | 1 | 0 |
| lib41 without its docs/referee games (45 with n > 64 skipped) | 1,095 | 5,307 | 5,307 / 2,023 / 6,354 | 398 / 108 / 51 (20) | 5 | 1 | 0 |
- SAT (Ξ = B on [t, t*], t* − t ≤ 4n(n − 1)) checked on 19,705 + 20,551 + 335 + 178 phases with a saturated D = ∅ state: 0 failures.
- Thin spots: STEP1's non-trivial cases (level still below n − 1 after the step) are 291 in all; in most D = ∅ S4a steps the arena optimum is
  already saturated. Mutations: RC_MUT=full (STEP1 asks for saturation at once) fails (1 on seed 53); RC_MUT=step2 (asks + 2) does not bite
  on seed 53 (it bites only on exact + 1 rises; 3 on a seed-1 smoke run); RC_MUT=nosat (bound without the 4n(n − 1) term) does not fail: N_0
  never comes near either bound (max 5, as in the packet's lib41 row).
- Comparison with the packet's §3 (after my runs): lib41 max N_0 5 in both; my sample and seeds differ from the lane's, so other counts are not
  compared.

## 4. Notes
| id | where | kind | text |
| --- | --- | --- | --- |
| N-REC0-1 | §1 step 1 | wording | "let k → k + 1 be an S4a step, and let k + 1 be all-unsplit" needs k + 1 in the phase (λ_{k+1} = λ_k): all-unsplit at k + 1 is relative to λ_{k+1}, and Lemma P needs λ_W unchanged. Every use (step 3) has it; write "an in-phase S4a step". |
| N-REC0-2 | Premises; Q-R17 | citation | Q-R17's list should add (V1), (V2) (statewise value facts of R17 §1) and "u a cycle node at k" (λ_W = λ at all-unsplit k). Step 4's use of R15 (d) reads Ωσ as S1's Ξ (the standing code link G-N5T-1), as every per-phase packet does; worth one clause. |

## Signature
REFEREE-2 (successor 15, Opus 5.5, D15): Lemma REC-0 SIGN; Corollary (transitions via EP-0) SIGN. Q-R17: YES (the induction step uses only the
hypothesis at k, the switch-best arena, (F1)/(F2), an unchanged λ_W, and the statewise facts (V1), (V2) and "u a cycle node at k"). No gap.
§2, §3 not signed.

## §C. Comparison with REFEREE's R-N5-REC0 (claude/referee 6006b963, successor 13; read after my a0457eb0 + 82fdc8d4 were pushed). Written 2026-10-26 09:1xZ by date -u (Opus 5.5, D15)
### C.1 Verdicts
| item | REFEREE | REFEREE-2 | outcome |
| --- | --- | --- | --- |
| Lemma REC-0 | SIGNED, no gap | SIGN, no gap | same |
| Corollary (via EP-0) | SIGNED (R64 (c)'s len(E) is the corollary's count) | SIGN (same reading of len(E)) | same |
| Q-R17 | YES; inputs 1-6 (hypothesis at k; I_k from Ω_k = W_k; arena strategy + (F1)/(F2); (V1)/(V2); u a cycle node at k and no cycle-node change; one-player structure) | YES; the same items (hypothesis at k; H_k ∋ ρ_k and every improving edge; (F1)/(F2); λ_W unchanged; (V1)/(V2); u a cycle node at k; G_τ one-player and Ξ_k = W_k for the transfer) | same, item for item |
| §2, §3 | not signed | not signed | same |
### C.2 Notes, item by item
| REFEREE | REFEREE-2 | outcome |
| --- | --- | --- |
| REC0-N3 (Q-R17's list should name (V1)/(V2) and the one-player structure) | N-REC0-2, first half ((V1), (V2), "u a cycle node at k"; the one-player structure in my §2 transfer paragraph) | same, found by both |
| REC0-N1 (cite R63 for SN-PREFIX_D (a); WM's game-general form is in R63's premises too) | — | found by REFEREE only; accepted (citation) |
| REC0-N2 (step 3: "level ≥ min(j + 1, n − 1)", the level being capped at n − 1) | — (my checker uses exactly min(level + 1, n − 1); I did not raise the wording) | found by REFEREE only; accepted (wording) |
| — | N-REC0-1 (step 1: "an in-phase S4a step", k + 1 ∈ P) | mine only; REFEREE's step 1 uses it ("λ(k) = λ(k+1) (in-phase)"), so no disagreement; stays a wording note |
| — | N-REC0-2, second half (step 4's R15 (d) reads Ωσ as S1's Ξ, the standing code link G-N5T-1) | mine only; citation note |
| consistency with R17 honest limit (ii) (Lemma P false for N5 inside a σ̄-segment, where Ξ ≠ W) | not raised | REFEREE only; I agree: REC-0 applies the step only from D = ∅ states (Ξ = W), so there is no conflict |
### C.3 Data
- Both: 0 failures of the inequality, EP-0, the prefix property and every level check (exact simple-path enumeration in both, independent engines).
  Max N_0 5 on lib41 in both, equal to the packet. Both find kind-(iii) steps ≤ 1 per run, so step 5's n − 1 cap is not exercised by data in
  either; the level step itself is (REFEREE 9,929 checks; mine 4,485, 291 of them non-saturating). lib41 phase counts differ (5,338 vs 5,307):
  different random starts.
### C.4 Joint gap map
| id | REFEREE | REFEREE-2 | status |
| --- | --- | --- | --- |
| — | no gap | no gap | — |
Nothing open: REC-0 and its Corollary are signed by both without gap; Q-R17 is answered YES by both with the same list of inputs. Notes for the
fixes file (wording / citation only): REC0-N1, REC0-N2, REC0-N3 = N-REC0-2 (first half), N-REC0-1, N-REC0-2 (second half).
### C.5 Final verdicts (Opus 5.5, D15)
Lemma REC-0 SIGN; Corollary SIGN; Q-R17 YES. No gap.
